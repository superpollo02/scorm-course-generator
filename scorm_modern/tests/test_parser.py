import pytest

from scorm_modern.parser import ParseError, parsear_markdown

MARKDOWN_BASICO = """\
# Lección: Intro

Contenido de la lección.

:::apoyo
Nota importante.

VIDEO: https://www.youtube.com/watch?v=abc123
:::

# Evaluación: Quiz

## Pregunta 1

**¿2+2?**

A) 3
B) 4
C) 5
D) 6

**Respuesta correcta: B**

**Explicación:** Aritmética básica.

# Actividad: Ejercicio 1

Haz algo.

# Actividad: Ejercicio 2

Haz otra cosa.

# Enlaces

- [Sitio](https://ejemplo.com) - Un sitio de ejemplo
"""


def test_parsear_estructura_basica():
    curso = parsear_markdown(MARKDOWN_BASICO)
    assert curso.leccion is not None
    assert curso.leccion.titulo == "Intro"
    assert curso.evaluacion is not None
    assert curso.evaluacion.titulo == "Quiz"
    assert len(curso.actividades) == 2
    assert curso.actividades[0].titulo == "Ejercicio 1"
    assert curso.enlaces_markdown == [
        {"titulo": "Sitio", "url": "https://ejemplo.com", "descripcion": "Un sitio de ejemplo"}
    ]
    assert curso.validar() == []


def test_apoyo_extraido_de_leccion():
    curso = parsear_markdown(MARKDOWN_BASICO)
    assert len(curso.leccion.apoyos) == 1
    apoyo = curso.leccion.apoyos[0]
    assert "Nota importante" in apoyo.contenido_md
    assert apoyo.video_url == "https://www.youtube.com/watch?v=abc123"
    assert "{{APOYO_0}}" in curso.leccion.contenido_md


def test_preguntas_parseadas_correctamente():
    curso = parsear_markdown(MARKDOWN_BASICO)
    preguntas = curso.evaluacion.preguntas
    assert len(preguntas) == 1
    p = preguntas[0]
    assert p.numero == 1
    assert p.texto == "¿2+2?"
    assert p.opciones == {"A": "3", "B": "4", "C": "5", "D": "6"}
    assert p.correcta == "B"
    assert "Aritmética" in p.explicacion


def test_error_sin_secciones():
    with pytest.raises(ParseError):
        parsear_markdown("Solo texto sin encabezados de nivel 1.")


def test_error_leccion_duplicada():
    md = "# Lección: Uno\ncontenido\n# Lección: Dos\notro contenido\n"
    with pytest.raises(ParseError):
        parsear_markdown(md)


def test_error_seccion_no_reconocida():
    md = "# Sección Rara\ncontenido\n"
    with pytest.raises(ParseError):
        parsear_markdown(md)


def test_curso_sin_actividades_es_invalido():
    md = "# Lección: Uno\ncontenido\n"
    curso = parsear_markdown(md)
    errores = curso.validar()
    assert any("Actividad" in e for e in errores)


def test_curso_sin_leccion_es_invalido():
    md = "# Actividad: Uno\ncontenido\n"
    curso = parsear_markdown(md)
    errores = curso.validar()
    assert any("Lección" in e for e in errores)
