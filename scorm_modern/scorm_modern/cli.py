#!/usr/bin/env python3
"""
cli.py
======
Interfaz de línea de comandos para scorm_modern.

Comandos:
  validate <config.yaml>   Valida configuración + markdown, sin generar nada.
  build <config.yaml>      Construye el paquete SCORM completo (.zip).
  list <config.yaml>       Lista los objetos del curso (lección/evaluación/actividades/enlaces).

Ejemplos:
  python -m scorm_modern.cli validate ejemplo/config.yaml
  python -m scorm_modern.cli build ejemplo/config.yaml
  python -m scorm_modern.cli list ejemplo/config.yaml
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .builder import BuildError, construir_curso
from .config import ConfigError, CursoConfig
from .parser import ParseError, parsear_markdown


def _cargar_config(ruta_config: str) -> CursoConfig:
    return CursoConfig.from_yaml(ruta_config)


def cmd_validate(args: argparse.Namespace) -> int:
    ruta_config = Path(args.config)
    base_dir = ruta_config.parent

    try:
        config = _cargar_config(args.config)
    except ConfigError as exc:
        print(f"[ERROR] Configuración inválida: {exc}", file=sys.stderr)
        return 1

    errores_config = config.validar()
    if errores_config:
        print("[ERROR] Configuración inválida:")
        for e in errores_config:
            print(f"  - {e}")
        return 1

    ruta_md = config.ruta_contenido(base_dir)
    if not ruta_md.exists():
        print(f"[ERROR] No se encontró el archivo de contenido: {ruta_md}", file=sys.stderr)
        return 1

    try:
        curso = parsear_markdown(ruta_md.read_text(encoding="utf-8"))
    except ParseError as exc:
        print(f"[ERROR] Error de parseo: {exc}", file=sys.stderr)
        return 1

    errores_curso = curso.validar()
    if errores_curso:
        print("[ERROR] Curso inválido:")
        for e in errores_curso:
            print(f"  - {e}")
        return 1

    print(f"[OK] Configuración y contenido válidos para '{config.titulo}'.")
    print(f"  - Lección: {curso.leccion.titulo}")
    print(f"  - Evaluación: {curso.evaluacion.titulo if curso.evaluacion else '(ninguna)'}")
    print(f"  - Actividades: {len(curso.actividades)}")
    print(f"  - Enlaces (config + markdown): {len(config.enlaces) + len(curso.enlaces_markdown)}")
    return 0


def cmd_build(args: argparse.Namespace) -> int:
    ruta_config = Path(args.config)
    base_dir = ruta_config.parent

    try:
        config = _cargar_config(args.config)
        resultado = construir_curso(config, base_dir=base_dir)
    except (ConfigError, BuildError) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    print(f"[OK] Paquete SCORM generado en: {resultado.directorio_salida}")
    print(f"[OK] Archivo ZIP: {resultado.archivo_zip} "
          f"({resultado.archivo_zip.stat().st_size / 1024:.1f} KB)")
    print(f"[OK] Enlaces incluidos en ENLACES.md: {len(resultado.enlaces)}")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    ruta_config = Path(args.config)
    base_dir = ruta_config.parent

    try:
        config = _cargar_config(args.config)
        ruta_md = config.ruta_contenido(base_dir)
        curso = parsear_markdown(ruta_md.read_text(encoding="utf-8"))
    except (ConfigError, ParseError, FileNotFoundError) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    print(f"Curso: {config.titulo} ({config.identificador})")
    print(f"  Lección: {curso.leccion.titulo if curso.leccion else '(ninguna)'}")
    if curso.evaluacion:
        print(f"  Evaluación: {curso.evaluacion.titulo} ({len(curso.evaluacion.preguntas)} preguntas)")
    else:
        print("  Evaluación: (ninguna)")
    print(f"  Actividades ({len(curso.actividades)}):")
    for i, act in enumerate(curso.actividades, 1):
        print(f"    {i}. {act.titulo}")
    todos_enlaces = list(config.enlaces) + curso.enlaces_markdown
    print(f"  Enlaces ({len(todos_enlaces)}):")
    for enlace in config.enlaces:
        print(f"    - [config] {enlace.titulo} -> {enlace.url}")
    for enlace in curso.enlaces_markdown:
        print(f"    - [markdown] {enlace['titulo']} -> {enlace['url']}")
    return 0


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="scorm_modern",
        description="Generador de paquetes SCORM 1.2 (lección + evaluación + actividades).",
    )
    subparsers = parser.add_subparsers(dest="comando", required=True)

    p_validate = subparsers.add_parser("validate", help="Valida configuración y contenido.")
    p_validate.add_argument("config", help="Ruta al archivo config.yaml del curso.")
    p_validate.set_defaults(func=cmd_validate)

    p_build = subparsers.add_parser("build", help="Construye el paquete SCORM (.zip).")
    p_build.add_argument("config", help="Ruta al archivo config.yaml del curso.")
    p_build.set_defaults(func=cmd_build)

    p_list = subparsers.add_parser("list", help="Lista los objetos del curso.")
    p_list.add_argument("config", help="Ruta al archivo config.yaml del curso.")
    p_list.set_defaults(func=cmd_list)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = construir_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
