"""scorm_modern: generador de paquetes SCORM 1.2 (lección + evaluación + N actividades)."""

from .builder import BuildError, ResultadoBuild, construir_curso
from .config import ConfigError, CursoConfig, Enlace
from .parser import Actividad, CursoParseado, Evaluacion, Leccion, ParseError, Pregunta, parsear_markdown

__all__ = [
    "BuildError",
    "ResultadoBuild",
    "construir_curso",
    "ConfigError",
    "CursoConfig",
    "Enlace",
    "Actividad",
    "CursoParseado",
    "Evaluacion",
    "Leccion",
    "ParseError",
    "Pregunta",
    "parsear_markdown",
]

__version__ = "1.0.0"
