#!/usr/bin/env python3
"""
create_scorm_modern_package.py
===============================
Punto de entrada del pipeline (estilo `scripts/scorm_generators/*.py`) para
generar paquetes SCORM con el formato moderno: 1 Lección + 1 Evaluación
(quiz interactivo) + N Actividades + enlaces (ENLACES.md).

A diferencia de `create_scorm_package.py` (que espera `# Módulo X: Título`),
este generador espera contenido dividido en `# Lección:`, `# Evaluación:`,
`# Actividad:` / `# Ejercicio:` y, opcionalmente, `# Enlaces`. Ver
`scorm_modern/README.md` para el formato completo.

Uso:
    # Validar config + contenido sin generar nada
    python scripts/scorm_generators/create_scorm_modern_package.py validate <config.yaml>

    # Listar los objetos parseados (lección/evaluación/actividades/enlaces)
    python scripts/scorm_generators/create_scorm_modern_package.py list <config.yaml>

    # Construir el paquete SCORM (.zip)
    python scripts/scorm_generators/create_scorm_modern_package.py build <config.yaml>

Si no se pasa ningún `config.yaml`, se usa el de ejemplo incluido en
`scorm_modern/ejemplo/config.yaml` para verificar que el entorno funciona.
"""

from __future__ import annotations

import sys
from pathlib import Path

# El paquete `scorm_modern` vive en la raíz del repositorio (scorm_modern/scorm_modern).
ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR / "scorm_modern"))

from scorm_modern.cli import main  # noqa: E402


def _config_por_defecto() -> str:
    return str(ROOT_DIR / "scorm_modern" / "ejemplo" / "config.yaml")


if __name__ == "__main__":
    argv = sys.argv[1:]

    if not argv:
        print(
            "Uso: create_scorm_modern_package.py {validate|build|list} <config.yaml>\n"
            "Sin argumentos, se usa el config.yaml de ejemplo para probar el entorno.\n"
        )
        argv = ["validate", _config_por_defecto()]
    elif len(argv) == 1:
        # Solo se indicó el comando (validate/build/list): usar el config de ejemplo.
        argv = [argv[0], _config_por_defecto()]

    sys.exit(main(argv))
