import zipfile
from pathlib import Path

import pytest

from scorm_modern.builder import BuildError, construir_curso
from scorm_modern.config import CursoConfig, Enlace

MARKDOWN = """\
# Lección: Intro

Contenido.

# Evaluación: Quiz

## Pregunta 1

**¿2+2?**

A) 3
B) 4

**Respuesta correcta: B**

# Actividad: Uno

Contenido de actividad.

# Enlaces

- [Enlace md](https://ejemplo.com/desde-md)
"""


@pytest.fixture
def proyecto(tmp_path: Path) -> Path:
    (tmp_path / "curso.md").write_text(MARKDOWN, encoding="utf-8")
    return tmp_path


def test_build_genera_zip_y_archivos(proyecto: Path):
    config = CursoConfig(
        identificador="curso-test",
        titulo="Curso de Prueba",
        contenido_md="curso.md",
        salida_dir="salida",
        enlaces=[Enlace(titulo="Enlace config", url="https://ejemplo.com/desde-config")],
    )

    resultado = construir_curso(config, base_dir=proyecto)

    assert resultado.archivo_zip.exists()
    assert (resultado.directorio_salida / "index.html").exists()
    assert (resultado.directorio_salida / "leccion.html").exists()
    assert (resultado.directorio_salida / "evaluacion.html").exists()
    assert (resultado.directorio_salida / "actividad_01.html").exists()
    assert (resultado.directorio_salida / "imsmanifest.xml").exists()
    assert (resultado.directorio_salida / "ENLACES.md").exists()

    # Enlaces combinados: 1 del config + 1 del markdown
    assert len(resultado.enlaces) == 2


def test_zip_contiene_imsmanifest_en_raiz(proyecto: Path):
    config = CursoConfig(identificador="curso-test", titulo="T", contenido_md="curso.md")
    resultado = construir_curso(config, base_dir=proyecto)

    with zipfile.ZipFile(resultado.archivo_zip) as zf:
        nombres = zf.namelist()
        assert "imsmanifest.xml" in nombres
        assert "index.html" in nombres


def test_manifest_tiene_titulos_por_objeto(proyecto: Path):
    config = CursoConfig(identificador="curso-test", titulo="T", contenido_md="curso.md")
    resultado = construir_curso(config, base_dir=proyecto)
    manifest = (resultado.directorio_salida / "imsmanifest.xml").read_text(encoding="utf-8")

    assert "<title>Intro</title>" in manifest
    assert "<title>Quiz</title>" in manifest
    assert "<title>Uno</title>" in manifest


def test_build_falla_si_falta_markdown(tmp_path: Path):
    config = CursoConfig(identificador="curso-test", titulo="T", contenido_md="no_existe.md")
    with pytest.raises(BuildError):
        construir_curso(config, base_dir=tmp_path)


def test_build_falla_con_config_invalida(proyecto: Path):
    config = CursoConfig(identificador="", titulo="T", contenido_md="curso.md")
    with pytest.raises(Exception):
        construir_curso(config, base_dir=proyecto)
