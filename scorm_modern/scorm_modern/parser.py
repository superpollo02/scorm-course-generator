"""
parser.py
=========
Convierte el markdown fuente de un curso en objetos estructurados:

  - Una (1) Leccion
  - Una (1) Evaluacion (quiz), con sus Preguntas
  - N Actividades / Ejercicios
  - Bloques de "apoyo" en línea (tips, notas, videos) dentro de cualquiera
    de los anteriores
  - Enlaces (si se listan en el propio markdown, se suman a los del config)

Convención de markdown esperada
--------------------------------
El archivo se divide en secciones de nivel 1 (`# `). El tipo de sección se
determina por el prefijo del título (sin distinguir mayúsculas/acentos):

    # Lección: <título>          -> objeto Leccion (debe haber exactamente 1)
    # Evaluación: <título>       -> objeto Evaluacion (0 o 1)
    # Actividad: <título>        -> objeto Actividad (0..N)
    # Ejercicio: <título>        -> tratado igual que Actividad
    # Enlaces                    -> lista de enlaces markdown `- [titulo](url)`

Bloques de apoyo en línea, permitidos dentro de Lección/Actividad:

    :::apoyo
    Contenido de la nota/tip. Puede incluir una línea:
    VIDEO: https://www.youtube.com/watch?v=xxxx
    para insertar un video incrustado.
    :::

Preguntas dentro de una Evaluación:

    ## Pregunta 1
    **Texto de la pregunta**

    A) Opción A
    B) Opción B
    C) Opción C
    D) Opción D

    **Respuesta correcta: B**
    **Explicación:** Texto opcional de explicación.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

__all__ = [
    "ParseError",
    "BloqueApoyo",
    "Pregunta",
    "Evaluacion",
    "Actividad",
    "Leccion",
    "CursoParseado",
    "parsear_markdown",
]


class ParseError(ValueError):
    """Error al interpretar el markdown fuente del curso."""


_RE_SECCION = re.compile(r"^#\s+(.*)$", re.MULTILINE)
_RE_APOYO = re.compile(r":::apoyo\s*\n(.*?)\n:::", re.DOTALL)
_RE_VIDEO = re.compile(r"^\s*VIDEO:\s*(\S+)\s*$", re.MULTILINE)
_RE_PREGUNTA = re.compile(r"^##\s+Pregunta\s+(\d+)\s*$", re.MULTILINE)
_RE_OPCION = re.compile(r"^([A-D])\)\s*(.+)$", re.MULTILINE)
_RE_RESPUESTA = re.compile(
    r"\*\*Respuesta correcta:\s*([A-D])\*\*", re.IGNORECASE
)
_RE_EXPLICACION = re.compile(
    r"\*\*Explicaci[oó]n:?\*\*:?\s*(.*)", re.IGNORECASE | re.DOTALL
)
_RE_ENLACE_MD = re.compile(r"^-\s*\[(.+?)\]\((\S+?)\)(?:\s*[—-]\s*(.*))?$", re.MULTILINE)


@dataclass
class BloqueApoyo:
    """Bloque de apoyo/nota en línea, con soporte opcional de video embebido."""

    contenido_md: str
    video_url: str | None = None


@dataclass
class Pregunta:
    numero: int
    texto: str
    opciones: dict[str, str]
    correcta: str
    explicacion: str = ""

    def validar(self) -> list[str]:
        errores = []
        if not self.texto.strip():
            errores.append(f"Pregunta {self.numero}: falta el texto de la pregunta.")
        if len(self.opciones) < 2:
            errores.append(f"Pregunta {self.numero}: debe tener al menos 2 opciones.")
        if self.correcta not in self.opciones:
            errores.append(
                f"Pregunta {self.numero}: la respuesta correcta '{self.correcta}' "
                f"no está entre las opciones {sorted(self.opciones)}."
            )
        return errores


@dataclass
class Evaluacion:
    titulo: str
    preguntas: list[Pregunta] = field(default_factory=list)
    apoyos: list[BloqueApoyo] = field(default_factory=list)

    def validar(self) -> list[str]:
        errores = []
        if not self.preguntas:
            errores.append(f"Evaluación '{self.titulo}': no tiene preguntas.")
        for p in self.preguntas:
            errores.extend(p.validar())
        return errores


@dataclass
class Actividad:
    titulo: str
    contenido_md: str
    apoyos: list[BloqueApoyo] = field(default_factory=list)


@dataclass
class Leccion:
    titulo: str
    contenido_md: str
    apoyos: list[BloqueApoyo] = field(default_factory=list)
    tipo_seccion: str = "clase"


@dataclass
class CursoParseado:
    leccion: Leccion | None
    evaluacion: Evaluacion | None
    actividades: list[Actividad] = field(default_factory=list)
    enlaces_markdown: list[dict[str, str]] = field(default_factory=list)

    def validar(self) -> list[str]:
        errores = []
        if self.leccion is None:
            errores.append("El curso debe tener exactamente una sección '# Clase: ...' o '# Lectura: ...'.")
        if self.evaluacion is not None:
            errores.extend(self.evaluacion.validar())
        if not self.actividades:
            errores.append("El curso debe tener al menos una '# Actividad: ...'.")
        return errores


def _normalizar(texto: str) -> str:
    """Minúsculas y sin acentos, para comparar prefijos de sección con tolerancia."""
    reemplazos = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")
    return texto.translate(reemplazos).strip().lower()


def _extraer_apoyos(texto: str) -> tuple[str, list[BloqueApoyo]]:
    """Extrae los bloques `:::apoyo ... :::` del texto y los devuelve aparte,
    dejando marcadores `{{APOYO_n}}` en su lugar dentro del contenido restante."""
    apoyos: list[BloqueApoyo] = []

    def _reemplazar(match: re.Match[str]) -> str:
        bloque = match.group(1).strip()
        video_match = _RE_VIDEO.search(bloque)
        video_url = video_match.group(1) if video_match else None
        contenido_sin_video = _RE_VIDEO.sub("", bloque).strip()
        apoyos.append(BloqueApoyo(contenido_md=contenido_sin_video, video_url=video_url))
        return f"{{{{APOYO_{len(apoyos) - 1}}}}}"

    restante = _RE_APOYO.sub(_reemplazar, texto)
    return restante, apoyos


def _parsear_preguntas(texto: str) -> list[Pregunta]:
    posiciones = list(_RE_PREGUNTA.finditer(texto))
    preguntas: list[Pregunta] = []

    for i, m in enumerate(posiciones):
        numero = int(m.group(1))
        inicio = m.end()
        fin = posiciones[i + 1].start() if i + 1 < len(posiciones) else len(texto)
        bloque = texto[inicio:fin].strip()

        # Texto de la pregunta: primera línea en negrita, o primera línea no vacía.
        texto_match = re.search(r"\*\*(.+?)\*\*", bloque)
        texto_pregunta = texto_match.group(1).strip() if texto_match else (
            bloque.splitlines()[0].strip() if bloque.splitlines() else ""
        )

        opciones = {letra: opcion.strip() for letra, opcion in _RE_OPCION.findall(bloque)}

        respuesta_match = _RE_RESPUESTA.search(bloque)
        correcta = respuesta_match.group(1).upper() if respuesta_match else ""

        explicacion_match = _RE_EXPLICACION.search(bloque)
        explicacion = explicacion_match.group(1).strip() if explicacion_match else ""
        # Cortar la explicación en el siguiente separador de sección, si lo hay.
        explicacion = re.split(r"\n---\n|\n#{1,2}\s", explicacion)[0].strip()

        preguntas.append(
            Pregunta(
                numero=numero,
                texto=texto_pregunta,
                opciones=opciones,
                correcta=correcta,
                explicacion=explicacion,
            )
        )

    return preguntas


def _parsear_enlaces(texto: str) -> list[dict[str, str]]:
    enlaces = []
    for titulo, url, descripcion in _RE_ENLACE_MD.findall(texto):
        enlaces.append({
            "titulo": titulo.strip(),
            "url": url.strip(),
            "descripcion": (descripcion or "").strip(),
        })
    return enlaces


def parsear_markdown(md_texto: str) -> CursoParseado:
    """Parsea el markdown completo de un curso y devuelve un CursoParseado."""

    posiciones = list(_RE_SECCION.finditer(md_texto))
    if not posiciones:
        raise ParseError("No se encontró ninguna sección de nivel 1 ('# ...') en el markdown.")

    leccion: Leccion | None = None
    evaluacion: Evaluacion | None = None
    actividades: list[Actividad] = []
    enlaces_markdown: list[dict[str, str]] = []

    for i, m in enumerate(posiciones):
        titulo_crudo = m.group(1).strip()
        inicio = m.end()
        fin = posiciones[i + 1].start() if i + 1 < len(posiciones) else len(md_texto)
        cuerpo = md_texto[inicio:fin].strip()

        titulo_norm = _normalizar(titulo_crudo)

        if (titulo_norm.startswith("leccion:") or titulo_norm.startswith("lección:") or 
            titulo_norm.startswith("clase:") or titulo_norm.startswith("lectura:") or 
            titulo_norm.startswith("lecturas:")):
            if leccion is not None:
                raise ParseError("Solo puede haber una sección '# Clase:', '# Lectura:' o '# Lección:' por curso.")
            
            tipo = "clase"
            if titulo_norm.startswith("leccion:") or titulo_norm.startswith("lección:"):
                tipo = "lección"
            elif titulo_norm.startswith("lectura:") or titulo_norm.startswith("lecturas:"):
                tipo = "lectura"

            titulo = titulo_crudo.split(":", 1)[1].strip()
            contenido, apoyos = _extraer_apoyos(cuerpo)
            leccion = Leccion(titulo=titulo, contenido_md=contenido, apoyos=apoyos, tipo_seccion=tipo)

        elif titulo_norm.startswith("evaluacion:") or titulo_norm.startswith("evaluación:"):
            if evaluacion is not None:
                raise ParseError("Solo puede haber una sección '# Evaluación: ...' por curso.")
            titulo = titulo_crudo.split(":", 1)[1].strip()
            contenido, apoyos = _extraer_apoyos(cuerpo)
            preguntas = _parsear_preguntas(contenido)
            evaluacion = Evaluacion(titulo=titulo, preguntas=preguntas, apoyos=apoyos)

        elif titulo_norm.startswith("actividad:") or titulo_norm.startswith("ejercicio:"):
            titulo = titulo_crudo.split(":", 1)[1].strip()
            contenido, apoyos = _extraer_apoyos(cuerpo)
            actividades.append(Actividad(titulo=titulo, contenido_md=contenido, apoyos=apoyos))

        elif titulo_norm == "enlaces":
            enlaces_markdown.extend(_parsear_enlaces(cuerpo))

        else:
            raise ParseError(
                f"Sección de nivel 1 no reconocida: '# {titulo_crudo}'. "
                "Debe comenzar con 'Clase:', 'Lectura:', 'Lección:', 'Evaluación:', "
                "'Actividad:', 'Ejercicio:' o llamarse 'Enlaces'."
            )

    return CursoParseado(
        leccion=leccion,
        evaluacion=evaluacion,
        actividades=actividades,
        enlaces_markdown=enlaces_markdown,
    )
