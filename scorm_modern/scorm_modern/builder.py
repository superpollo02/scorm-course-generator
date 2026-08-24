"""
builder.py
==========
Orquesta la construcción completa de un paquete SCORM moderno:

  1. Valida la configuración (`CursoConfig`).
  2. Lee y parsea el markdown fuente -> 1 lección + 1 evaluación + N actividades.
  3. Renderiza cada objeto a HTML (con navegación entre páginas).
  4. Genera `ENLACES.md` a partir de los enlaces del config + los del markdown.
  5. Genera `imsmanifest.xml` con títulos por objeto.
  6. Empaqueta todo en un .zip listo para importar en cualquier LMS.
"""

from __future__ import annotations

import zipfile
from dataclasses import dataclass
from pathlib import Path

from .config import ConfigError, CursoConfig, Enlace
from .manifest import ItemManifest, generar_manifest
from .parser import CursoParseado, ParseError, parsear_markdown
from .renderer import PaginaNav, render_actividad, render_evaluacion, render_indice, render_leccion

__all__ = ["BuildError", "ResultadoBuild", "construir_curso"]


class BuildError(RuntimeError):
    """Error durante la construcción del paquete SCORM."""


@dataclass
class ResultadoBuild:
    directorio_salida: Path
    archivo_zip: Path
    curso: CursoParseado
    enlaces: list[Enlace]


def _slug(texto: str, prefijo: str, indice: int | None = None) -> str:
    base = "".join(c if c.isalnum() else "_" for c in texto.lower()).strip("_")
    base = base or prefijo
    if indice is not None:
        return f"{prefijo}_{indice:02d}_{base}"[:60]
    return f"{prefijo}_{base}"[:60]


def _combinar_enlaces(config: CursoConfig, curso: CursoParseado) -> list[Enlace]:
    """Combina los enlaces del config.yaml con los declarados en el markdown,
    evitando duplicados por URL."""
    combinados: list[Enlace] = list(config.enlaces)
    urls_existentes = {e.url.strip().rstrip("/") for e in combinados}

    for enlace_dict in curso.enlaces_markdown:
        enlace = Enlace.from_any(enlace_dict)
        url_norm = enlace.url.strip().rstrip("/")
        if url_norm not in urls_existentes:
            combinados.append(enlace)
            urls_existentes.add(url_norm)

    return combinados


def _generar_enlaces_md(titulo_curso: str, enlaces: list[Enlace]) -> str:
    if not enlaces:
        return f"# Enlaces — {titulo_curso}\n\nEste curso no tiene enlaces externos registrados.\n"

    lineas = [f"# Enlaces — {titulo_curso}\n"]
    for enlace in enlaces:
        lineas.append(enlace.to_markdown())
    lineas.append("")
    return "\n".join(lineas)


def construir_curso(config: CursoConfig, base_dir: str | Path | None = None) -> ResultadoBuild:
    """Construye el paquete SCORM completo a partir de una configuración válida.

    `base_dir` es el directorio desde el cual se resuelven las rutas relativas
    de `contenido_md` y `salida_dir` (por defecto, el directorio actual).
    """
    config.validar_o_lanzar()

    base = Path(base_dir) if base_dir else Path(".")
    ruta_md = config.ruta_contenido(base)
    if not ruta_md.exists():
        raise BuildError(f"No se encontró el archivo de contenido: {ruta_md}")

    md_texto = ruta_md.read_text(encoding="utf-8")

    try:
        curso = parsear_markdown(md_texto)
    except ParseError as exc:
        raise BuildError(f"Error al parsear el markdown: {exc}") from exc

    errores = curso.validar()
    if errores:
        detalle = "\n  - ".join(errores)
        raise BuildError(f"El curso parseado no es válido:\n  - {detalle}")

    salida_dir = config.ruta_salida(base)
    salida_dir.mkdir(parents=True, exist_ok=True)

    items_manifest: list[ItemManifest] = []
    items_indice: list[tuple[str, str, str]] = []

    # --- Construir la lista de páginas en orden: lección, evaluación, actividades
    paginas: list[tuple[str, str, str]] = []  # (id, titulo, tipo)
    paginas.append(("leccion", curso.leccion.titulo, "leccion"))
    if curso.evaluacion is not None:
        paginas.append(("evaluacion", curso.evaluacion.titulo, "evaluacion"))
    for i, actividad in enumerate(curso.actividades, start=1):
        paginas.append((f"actividad_{i:02d}", actividad.titulo, "actividad"))

    archivos = {pid: f"{pid}.html" for pid, _, _ in paginas}

    def nav_para(indice: int) -> PaginaNav:
        anterior = archivos[paginas[indice - 1][0]] if indice > 0 else None
        siguiente = archivos[paginas[indice + 1][0]] if indice + 1 < len(paginas) else None
        return PaginaNav(anterior=anterior, siguiente=siguiente)

    # --- Renderizar lección
    idx = 0
    html_leccion = render_leccion(curso.leccion, nav=nav_para(idx))
    (salida_dir / archivos["leccion"]).write_text(html_leccion, encoding="utf-8")
    items_manifest.append(ItemManifest("leccion", curso.leccion.titulo, archivos["leccion"]))
    items_indice.append((curso.leccion.titulo, archivos["leccion"], curso.leccion.tipo_seccion.capitalize()))
    idx += 1

    # --- Renderizar evaluación
    if curso.evaluacion is not None:
        html_eval = render_evaluacion(
            curso.evaluacion, puntaje_minimo=config.puntaje_minimo, nav=nav_para(idx)
        )
        (salida_dir / archivos["evaluacion"]).write_text(html_eval, encoding="utf-8")
        items_manifest.append(ItemManifest("evaluacion", curso.evaluacion.titulo, archivos["evaluacion"]))
        items_indice.append((curso.evaluacion.titulo, archivos["evaluacion"], "Evaluación"))
        idx += 1

    # --- Renderizar actividades
    for i, actividad in enumerate(curso.actividades, start=1):
        pid = f"actividad_{i:02d}"
        html_act = render_actividad(actividad, nav=nav_para(idx))
        (salida_dir / archivos[pid]).write_text(html_act, encoding="utf-8")
        items_manifest.append(ItemManifest(pid, actividad.titulo, archivos[pid]))
        items_indice.append((actividad.titulo, archivos[pid], "Actividad"))
        idx += 1

    # --- Índice
    html_indice = render_indice(config.titulo, items_indice)
    (salida_dir / "index.html").write_text(html_indice, encoding="utf-8")

    # --- Enlaces combinados (config + markdown) -> ENLACES.md
    enlaces = _combinar_enlaces(config, curso)
    enlaces_md = _generar_enlaces_md(config.titulo, enlaces)
    (salida_dir / "ENLACES.md").write_text(enlaces_md, encoding="utf-8")

    # --- Manifiesto (el índice no cuenta como sco por separado; usamos index.html como
    #     recurso de entrada implícito referenciado por el LMS, y los objetos reales como items)
    items_manifest_con_indice = [ItemManifest("indice", "Índice del Curso", "index.html")] + items_manifest
    manifest_xml = generar_manifest(
        identificador_curso=config.identificador,
        titulo_curso=config.titulo,
        items=items_manifest_con_indice,
        version=config.version,
    )
    (salida_dir / "imsmanifest.xml").write_text(manifest_xml, encoding="utf-8")

    # --- Empaquetar en .zip
    archivo_zip = salida_dir.parent / f"{config.identificador}-SCORM.zip"
    with zipfile.ZipFile(archivo_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for ruta in salida_dir.rglob("*"):
            if ruta.is_file():
                zf.write(ruta, ruta.relative_to(salida_dir))

    return ResultadoBuild(
        directorio_salida=salida_dir,
        archivo_zip=archivo_zip,
        curso=curso,
        enlaces=enlaces,
    )
