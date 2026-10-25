"""
generate_conectabloques_ai.py
==============================
Extrae conceptos y definiciones a partir de las 3 lecturas extendidas
de la sección Lectura de un curso/unidad usando el modelo liviano gemini-flash-lite-latest.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

# Integrar scorm_core
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from scorm_core import cache_ai_call

load_dotenv()

try:
    import google.generativeai as genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False


def extraer_las_tres_lecturas(md_path: Path) -> list[dict[str, str]]:
    """Extrae las lecturas extendidas del archivo de la unidad."""
    if not md_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {md_path}")

    content = md_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    sections = re.split(r"\n#\s+", "\n" + content)
    
    lecturas: list[dict[str, str]] = []
    for sec in sections:
        sec_strip = sec.strip()
        if not sec_strip:
            continue
        lines = sec_strip.split("\n")
        title = lines[0].strip()
        body = "\n".join(lines[1:]).strip()

        if title.lower().startswith("lectura") or "lectura" in title.lower():
            lecturas.append({"titulo": title, "texto": body})

    if not lecturas:
        # Si no tiene secciones explícitas de 'Lectura', usamos todo el texto
        lecturas.append({"titulo": md_path.stem, "texto": content})

    return lecturas[:3]


def construir_prompt_conectabloques(lecturas: list[dict[str, str]], num_conceptos: int = 8, dificultad: str = "intermedio") -> tuple[str, str]:
    """Crea prompts compactos para bajo consumo de tokens considerando el nivel de dificultad."""
    system_prompt = (
        f"Eres un diseñador instruccional experto en actividades de asociación de conceptos (Conectabloques). "
        f"Nivel de dificultad requerido: {dificultad.upper()}. "
        f"Tu tarea es extraer conceptos clave con definiciones breves, claras y no ambiguas basadas EXCLUSIVAMENTE "
        f"en las lecturas provistas. Devuelve un JSON estricto sin explicaciones adicionales."
    )

    corpus = []
    for i, lec in enumerate(lecturas, 1):
        corpus.append(f"--- LECTURA {i}: {lec['titulo']} ---\n{lec['texto']}")
    lecturas_texto = "\n\n".join(corpus)

    guia_dificultad = {
        "basico": "Términos claros y directos con definiciones explícitas de vocabulario fundamental.",
        "intermedio": "Conceptos que requieren comprensión de relaciones conceptuales y metodológicas.",
        "avanzado": "Conceptos sutiles, técnicos o situacionales que exigen análisis crítico y diferenciación fina."
    }.get(dificultad.lower(), "Conceptos que requieren comprensión de relaciones conceptuales y metodológicas.")

    user_prompt = f"""Extrae exactamente {num_conceptos} pares conceptuales clave a partir de las siguientes lecturas:

{lecturas_texto}

Criterio de dificultad: {guia_dificultad}

Reglas:
1. 'term': Concepto o término técnico breve (máximo 3-4 palabras).
2. 'definition': Definición clara y diferenciable (máximo 25 palabras). No comiences repitiendo el término.
3. 'sourceSnippet': Cita o fragmento breve textual de donde se obtuvo.

Devuelve ÚNICAMENTE un array JSON con esta estructura exacta:
[
  {{
    "term": "Término 1",
    "definition": "Definición concisa...",
    "sourceSnippet": "Fragmento de la lectura..."
  }}
]"""

    return system_prompt, user_prompt


def generar_conceptos_ai(
    md_path: Path,
    api_key: str | None = None,
    model_name: str = "gemini-flash-lite-latest",
    num_conceptos: int = 8,
    dificultad: str = "intermedio"
) -> list[dict[str, Any]]:
    """Invoca Gemini Flash-Lite para extraer los conceptos."""
    lecturas = extraer_las_tres_lecturas(md_path)
    print(f"[*] Lecturas procesadas para Conectabloques: {len(lecturas)}")

    key = api_key or os.getenv("GEMINI_API_KEY")
    if not key:
        print("[!] GEMINI_API_KEY no detectada. Usando plantilla estructurada...")
        return _fallback_local(lecturas, num_conceptos)

    if not HAS_GENAI:
        raise ImportError("google.generativeai no instalado.")

    genai.configure(api_key=key)
    sys_prompt, usr_prompt = construir_prompt_conectabloques(lecturas, num_conceptos, dificultad)

    modelos = [model_name, "gemini-2.0-flash-lite", "gemini-1.5-flash-8b", "gemini-1.5-flash"]

    def _hacer_llamada_gemini():
        for mod in modelos:
            try:
                print(f"[*] Extrayendo conceptos con modelo ligero: {mod}...")
                model = genai.GenerativeModel(
                    model_name=mod,
                    system_instruction=sys_prompt,
                    generation_config={
                        "temperature": 0.2,
                        "response_mime_type": "application/json",
                    }
                )
                resp = model.generate_content(usr_prompt)
                if resp and resp.text:
                    print(f"[OK] Conceptos extraídos exitosamente con {mod}.")
                    raw = resp.text.strip()
                    if raw.startswith("```"):
                        raw = re.sub(r"^```(?:json)?\s*", "", raw)
                        raw = re.sub(r"\s*```$", "", raw)
                    return json.loads(raw)
            except Exception as e:
                print(f"[-] Error con {mod}: {e}. Probando siguiente...")
        raise RuntimeError("No se obtuvo respuesta de Gemini.")

    cache_params = {
        "md_path": str(md_path),
        "num_conceptos": num_conceptos,
        "dificultad": dificultad,
        "model_name": model_name
    }
    return cache_ai_call("generate_conectabloques_ai", usr_prompt, cache_params, _hacer_llamada_gemini)


def _fallback_local(lecturas: list[dict[str, str]], num_conceptos: int) -> list[dict[str, Any]]:
    """Plantilla de respaldo local sin conexión."""
    conceptos = []
    for i in range(1, num_conceptos + 1):
        conceptos.append({
            "term": f"Concepto Clave {i}",
            "definition": f"Definición fundamental asociada a la lectura {((i-1)%len(lecturas))+1}.",
            "sourceSnippet": f"Fragmento de referencia para el concepto {i} extraído de la lectura."
        })
    return conceptos


def guardar_markdown_conectabloques(
    conceptos: list[dict[str, Any]],
    titulo: str,
    salida_md: Path,
    tema: str = "modern-mint",
    duracion_minutos: int = 20,
    intentos: int | None = None,
    dificultad: str = "intermedio"
) -> Path:
    """Guarda los conceptos en el formato markdown estándar de conectabloques."""
    max_intentos = intentos or (len(conceptos) * 2)
    lineas = [
        f"# Actividad: Conectabloques - {titulo}",
        "Puntaje mínimo: 70%",
        f"Tiempo límite: {duracion_minutos} minutos",
        f"Intentos máximos: {max_intentos}",
        f"Nivel de dificultad: {dificultad}",
        f"Tema visual: {tema}\n",
        "Relaciona cada concepto o término con su definición correcta.\n"
    ]

    for c in conceptos:
        lineas.append(f"## Término: {c['term']}")
        lineas.append(f"- Definición: {c['definition']}")
        if "sourceSnippet" in c and c["sourceSnippet"]:
            lineas.append(f"- Origen: {c['sourceSnippet']}")
        lineas.append("")

    salida_md.write_text("\n".join(lineas), encoding="utf-8")
    print(f"[OK] Archivo Markdown de Conectabloques guardado en: {salida_md}")
    return salida_md


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extractor AI de bloques de asociación de conceptos")
    parser.add_argument("lecturas", help="Ruta al markdown con las lecturas extendidas")
    parser.add_argument("-n", "--num-concepts", type=int, default=8, help="Número de conceptos (default: 8)")
    parser.add_argument("-o", "--output", help="Ruta de salida del archivo markdown", default=None)
    parser.add_argument("--theme", default="modern-mint", help="Tema visual (modern-mint, retro-arcade, neon-synthwave, chalkboard, warm-autumn)")
    parser.add_argument("--duration", type=int, default=20, help="Duración en minutos (default: 20)")
    parser.add_argument("--attempts", type=int, default=None, help="Cantidad de intentos permitidos (default: 2*N)")
    parser.add_argument("--difficulty", default="intermedio", choices=["basico", "intermedio", "avanzado"], help="Nivel de dificultad")
    args = parser.parse_args()

    input_path = Path(args.lecturas)
    output_path = Path(args.output) if args.output else input_path.parent / f"{input_path.stem}_conectabloques.md"

    conceptos = generar_conceptos_ai(
        input_path,
        num_conceptos=args.num_concepts,
        dificultad=args.difficulty
    )
    guardar_markdown_conectabloques(
        conceptos=conceptos,
        titulo=input_path.stem,
        salida_md=output_path,
        tema=args.theme,
        duracion_minutos=args.duration,
        intentos=args.attempts,
        dificultad=args.difficulty
    )
