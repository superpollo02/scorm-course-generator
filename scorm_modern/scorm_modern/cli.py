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


def cmd_generate(args: argparse.Namespace) -> int:
    from .ai_generator import generar_contenido_clase, leer_insumos, guardar_checkpoint_markdown
    
    ruta_programa = Path(args.programa)
    dir_clase = Path(args.clase)
    ruta_checkpoint = Path(args.output)
    
    try:
        print(f"[*] Iniciando generación con IA para {dir_clase.name}...")
        insumos = leer_insumos(ruta_programa, dir_clase)
        datos = generar_contenido_clase(
            ruta_programa=ruta_programa,
            dir_clase=dir_clase,
            api_key=args.api_key,
            model_name=args.model,
            num_readings=args.readings,
            num_questions=args.questions
        )
        guardar_checkpoint_markdown(datos, insumos, ruta_checkpoint)
        print(f"[OK] Checkpoint generado exitosamente en: {ruta_checkpoint}")
        return 0
    except Exception as exc:
        print(f"[ERROR] Error durante la generación: {exc}", file=sys.stderr)
        return 1


def cmd_compile(args: argparse.Namespace) -> int:
    from .checkpoint_parser import parse_checkpoint_markdown
    from .builder import construir_desde_checkpoint
    
    ruta_checkpoint = Path(args.checkpoint)
    salida_zip = Path(args.output_zip) if args.output_zip else None
    
    if not ruta_checkpoint.exists():
        print(f"[ERROR] El archivo checkpoint no existe: {ruta_checkpoint}", file=sys.stderr)
        return 1
        
    try:
        print(f"[*] Parseando checkpoint {ruta_checkpoint}...")
        checkpoint_data = parse_checkpoint_markdown(ruta_checkpoint)
        
        print("[*] Compilando paquete SCORM...")
        zip_path = construir_desde_checkpoint(
            checkpoint_data=checkpoint_data,
            salida_zip=salida_zip
        )
        print(f"[OK] Paquete SCORM compilado exitosamente en: {zip_path}")
        return 0
    except Exception as exc:
        print(f"[ERROR] Error durante la compilación: {exc}", file=sys.stderr)
        return 1


def cmd_run(args: argparse.Namespace) -> int:
    from .ai_generator import generar_contenido_clase, leer_insumos, guardar_checkpoint_markdown
    from .checkpoint_parser import parse_checkpoint_markdown
    from .builder import construir_desde_checkpoint
    
    ruta_programa = Path(args.programa)
    dir_clase = Path(args.clase)
    ruta_checkpoint = Path(args.checkpoint)
    salida_zip = Path(args.output_zip) if args.output_zip else None
    
    try:
        print(f"[*] Fase 1 & 2: Generando contenido con IA desde {dir_clase.name}...")
        insumos = leer_insumos(ruta_programa, dir_clase)
        datos = generar_contenido_clase(
            ruta_programa=ruta_programa,
            dir_clase=dir_clase,
            api_key=args.api_key,
            model_name=args.model,
            num_readings=args.readings,
            num_questions=args.questions
        )
        guardar_checkpoint_markdown(datos, insumos, ruta_checkpoint)
        print(f"[OK] Checkpoint generado en: {ruta_checkpoint}")
        
        print("\n=======================================================")
        print("FASE DE VERIFICACIÓN INTERMEDIA (Fase 2.5)")
        print(f"Por favor abra y edite el archivo checkpoint en:")
        print(f"  {ruta_checkpoint.resolve()}")
        print("Realice los cambios necesarios en el título, lecturas o preguntas.")
        print("=======================================================")
        
        input("\nPresione ENTER cuando haya terminado de editar para compilar el paquete SCORM...")
        
        print(f"\n[*] Fase 3 & 4: Parseando y compilando desde {ruta_checkpoint.name}...")
        checkpoint_data = parse_checkpoint_markdown(ruta_checkpoint)
        zip_path = construir_desde_checkpoint(
            checkpoint_data=checkpoint_data,
            salida_zip=salida_zip
        )
        print(f"[OK] Paquete SCORM final compilado exitosamente en: {zip_path}")
        return 0
    except Exception as exc:
        print(f"[ERROR] Error en el flujo interactivo: {exc}", file=sys.stderr)
        return 1


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="scorm_modern",
        description="Generador de paquetes SCORM 1.2 (lección + evaluación + actividades).",
    )
    subparsers = parser.add_subparsers(dest="comando", required=True)

    # Comandos heredados
    p_validate = subparsers.add_parser("validate", help="Valida configuración y contenido.")
    p_validate.add_argument("config", help="Ruta al archivo config.yaml del curso.")
    p_validate.set_defaults(func=cmd_validate)

    p_build = subparsers.add_parser("build", help="Construye el paquete SCORM (.zip).")
    p_build.add_argument("config", help="Ruta al archivo config.yaml del curso.")
    p_build.set_defaults(func=cmd_build)

    p_list = subparsers.add_parser("list", help="Lista los objetos del curso.")
    p_list.add_argument("config", help="Ruta al archivo config.yaml del curso.")
    p_list.set_defaults(func=cmd_list)

    # Nuevos comandos con IA (Gemini)
    p_generate = subparsers.add_parser("generate", help="Genera checkpoint intermedio Markdown con IA.")
    p_generate.add_argument("--programa", required=True, help="Ruta al programa.yaml del curso.")
    p_generate.add_argument("--clase", required=True, help="Ruta al directorio de la clase.")
    p_generate.add_argument("--output", required=True, help="Ruta donde se guardará el checkpoint.md.")
    p_generate.add_argument("--model", default="gemini-3.5-flash", help="Modelo de Gemini a utilizar.")
    p_generate.add_argument("--api-key", default=None, help="API Key de Google Gemini.")
    p_generate.add_argument("--readings", type=int, default=3, help="Número de lecturas estructuradas a generar.")
    p_generate.add_argument("--questions", type=int, default=5, help="Número de preguntas del cuestionario.")
    p_generate.set_defaults(func=cmd_generate)

    p_compile = subparsers.add_parser("compile", help="Compila un paquete SCORM ZIP desde un checkpoint.md.")
    p_compile.add_argument("checkpoint", help="Ruta al archivo checkpoint.md.")
    p_compile.add_argument("--output-zip", default=None, help="Ruta del archivo ZIP de salida.")
    p_compile.set_defaults(func=cmd_compile)

    p_run = subparsers.add_parser("run", help="Ejecuta el flujo completo e interactivo (Generar -> Editar -> Compilar).")
    p_run.add_argument("--programa", required=True, help="Ruta al programa.yaml del curso.")
    p_run.add_argument("--clase", required=True, help="Ruta al directorio de la clase.")
    p_run.add_argument("--checkpoint", required=True, help="Ruta donde guardar/leer el checkpoint.md.")
    p_run.add_argument("--output-zip", default=None, help="Ruta del archivo ZIP de salida.")
    p_run.add_argument("--model", default="gemini-3.5-flash", help="Modelo de Gemini a utilizar.")
    p_run.add_argument("--api-key", default=None, help="API Key de Google Gemini.")
    p_run.add_argument("--readings", type=int, default=3, help="Número de lecturas estructuradas a generar.")
    p_run.add_argument("--questions", type=int, default=5, help="Número de preguntas del cuestionario.")
    p_run.set_defaults(func=cmd_run)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = construir_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
