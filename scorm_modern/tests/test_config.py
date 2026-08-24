import pytest

from scorm_modern.config import ConfigError, CursoConfig, Enlace


def test_config_valida_minima():
    config = CursoConfig(identificador="curso-1", titulo="Mi Curso")
    assert config.es_valida()
    assert config.validar() == []


def test_config_sin_identificador_es_invalida():
    config = CursoConfig(identificador="", titulo="Mi Curso")
    errores = config.validar()
    assert any("identificador" in e for e in errores)


def test_config_identificador_con_espacios_es_invalido():
    config = CursoConfig(identificador="mi curso", titulo="Mi Curso")
    errores = config.validar()
    assert any("identificador" in e for e in errores)


def test_config_puntaje_fuera_de_rango():
    config = CursoConfig(identificador="curso-1", titulo="T", puntaje_minimo=150)
    errores = config.validar()
    assert any("puntaje_minimo" in e for e in errores)


def test_enlace_valido():
    enlace = Enlace(titulo="Sitio", url="https://ejemplo.com")
    assert enlace.validar() == []


def test_enlace_url_invalida():
    enlace = Enlace(titulo="Sitio", url="ftp://ejemplo.com")
    errores = enlace.validar()
    assert errores


def test_enlace_sin_titulo():
    enlace = Enlace(titulo="", url="https://ejemplo.com")
    errores = enlace.validar()
    assert any("titulo" in e for e in errores)


def test_config_con_enlaces_duplicados():
    config = CursoConfig(
        identificador="curso-1",
        titulo="T",
        enlaces=[
            Enlace(titulo="A", url="https://ejemplo.com/x"),
            Enlace(titulo="B", url="https://ejemplo.com/x/"),
        ],
    )
    errores = config.validar()
    assert any("duplicado" in e for e in errores)


def test_from_dict_construye_enlaces():
    config = CursoConfig.from_dict({
        "identificador": "curso-1",
        "titulo": "T",
        "enlaces": [{"titulo": "A", "url": "https://ejemplo.com"}],
    })
    assert len(config.enlaces) == 1
    assert config.enlaces[0].titulo == "A"


def test_from_dict_rechaza_campos_desconocidos():
    with pytest.raises(ConfigError):
        CursoConfig.from_dict({
            "identificador": "curso-1",
            "titulo": "T",
            "campo_invalido": 123,
        })
