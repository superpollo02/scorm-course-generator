"""
scorm_core
==========
Núcleo común de abstracciones reutilizables para Aula Lista EDUCAI:
- manifest: Generador canónico de imsmanifest.xml SCORM 1.2
- ai_cache: Sistema de almacenamiento en caché para respuestas de IA (Gemini)
"""

from .manifest import generar_manifest_scorm_unificado
from .ai_cache import cache_ai_call, obtener_hash_cache

__all__ = [
    "generar_manifest_scorm_unificado",
    "cache_ai_call",
    "obtener_hash_cache",
]
