"""
generate_trivia_ai.py
=====================
Generador de Cuestionarios Trivia de bajo consumo de tokens utilizando
exclusivamente las 3 lecturas extendidas del archivo de checkpoint/curso.
Utiliza el modelo optimizado `gemini-flash-lite-latest` (o gemini-2.0-flash-lite/gemini-1.5-flash-8b).
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


def extraer_las_tres_lecturas(checkpoint_path: Path) -> list[dict[str, str]]:
    """Extrae exactamente las 3 lecturas extendidas del archivo checkpoint.md."""
    if not checkpoint_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {checkpoint_path}")

    content = checkpoint_path.read_text(encoding="utf-8").replace("\r\n", "\n")
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
        raise ValueError(f"No se detectaron secciones de 'Lectura' en {checkpoint_path}")

    return lecturas[:3]  # Tomar exactamente hasta 3 lecturas


def construir_prompt_eficiente(lecturas: list[dict[str, str]], num_preguntas: int = 10) -> tuple[str, str]:
    """Crea un system prompt y user prompt hipercompactos para gastar el mínimo de tokens."""
    system_prompt = (
        "Eres un diseñador de trivias educativas. Tu tarea es generar preguntas de opción múltiple "
        "con 4 opciones (A, B, C, D), indicando la clave correcta y una breve retroalimentación explicativa (1-2 líneas). "
        "Usa EXCLUSIVAMENTE el texto de las lecturas provistas como fuente de verdad. "
        "Sé conciso, riguroso y evita todo relleno conversacional."
    )

    corpus = []
    for i, lec in enumerate(lecturas, 1):
        corpus.append(f"--- LECTURA {i}: {lec['titulo']} ---\n{lec['texto']}")

    lecturas_texto = "\n\n".join(corpus)

    user_prompt = f"""Genera {num_preguntas} preguntas estilo trivia distribuidas equilibradamente entre las siguientes 3 lecturas:

{lecturas_texto}

Devuelve ÚNICAMENTE un array JSON con esta estructura exacta (sin markdown extra ni texto adicional):
[
  {{
    "numero": 1,
    "texto": "¿Texto directo de la pregunta?",
    "opciones": {{
      "A": "Opción A",
      "B": "Opción B",
      "C": "Opción C",
      "D": "Opción D"
    }},
    "correcta": "B",
    "explicacion": "Explicación breve que retroalimenta y justifica la respuesta correcta según la lectura."
  }}
]"""

    return system_prompt, user_prompt


def generar_preguntas_trivia(
    checkpoint_path: Path,
    api_key: str | None = None,
    model_name: str = "gemini-flash-lite-latest",
    num_preguntas: int = 10,
) -> list[dict[str, Any]]:
    """Invoca la API de Gemini con el modelo ligero de bajo consumo de tokens."""
    lecturas = extraer_las_tres_lecturas(checkpoint_path)
    print(f"[*] Lecturas extendidas detectadas como fuente: {len(lecturas)}")
    for i, l in enumerate(lecturas, 1):
        print(f"    {i}. {l['titulo']}")

    key = api_key or os.getenv("GEMINI_API_KEY")
    if not key:
        print("[!] No se detectó GEMINI_API_KEY. Generando plantilla estructurada basada en las lecturas...")
        # Generador de respaldo determinístico sin tokens si no hay API key presente
        return _generar_plantilla_local(lecturas, num_preguntas)

    if not HAS_GENAI:
        raise ImportError("Se requiere 'google-generativeai'. Instálalo con 'pip install google-generativeai'.")

    genai.configure(api_key=key)
    system_prompt, user_prompt = construir_prompt_eficiente(lecturas, num_preguntas)

    # Probar modelo solicitado o fallbacks ligeros
    modelos_a_probar = [model_name, "gemini-2.0-flash-lite", "gemini-1.5-flash-8b", "gemini-1.5-flash"]

    def _hacer_llamada_gemini():
        for mod in modelos_a_probar:
            try:
                print(f"[*] Consultando modelo eficiente: {mod}...")
                model = genai.GenerativeModel(
                    model_name=mod,
                    system_instruction=system_prompt,
                    generation_config={
                        "temperature": 0.2,
                        "response_mime_type": "application/json",
                    }
                )
                resp = model.generate_content(user_prompt)
                if resp and resp.text:
                    print(f"[OK] Generación completada exitosamente con {mod}.")
                    raw = resp.text.strip()
                    if raw.startswith("```"):
                        raw = re.sub(r"^```(?:json)?\s*", "", raw)
                        raw = re.sub(r"\s*```$", "", raw)
                    return json.loads(raw)
            except Exception as e:
                print(f"[-] Error con modelo {mod}: {e}. Intentando alternativa...")
        raise RuntimeError("No fue posible obtener respuesta válida de Gemini.")

    # Ejecutar con caché persistente SHA-256
    cache_params = {
        "checkpoint": str(checkpoint_path),
        "num_preguntas": num_preguntas,
        "model_name": model_name
    }
    return cache_ai_call("generate_trivia_ai", user_prompt, cache_params, _hacer_llamada_gemini)


def _generar_plantilla_local(lecturas: list[dict[str, str]], num_preguntas: int) -> list[dict[str, Any]]:
    """Fallback seguro sin conexión si el usuario está testeando sin API Key."""
    preguntas = []
    for idx in range(1, num_preguntas + 1):
        lec_asociada = lecturas[(idx - 1) % len(lecturas)]
        preguntas.append({
            "numero": idx,
            "texto": f"Desafío {idx}: Respecto a los conceptos de '{lec_asociada['titulo']}', ¿cuál es la afirmación correcta?",
            "opciones": {
                "A": "Propuesta alternativa A según la lectura.",
                "B": "Enfoque fundamental validado en la lectura.",
                "C": "Distractor metodológico plausible.",
                "D": "Concepto secundario desactualizado."
            },
            "correcta": "B",
            "explicacion": f"Retroalimentación: La opción B refleja el principio central desarrollado en '{lec_asociada['titulo']}'."
        })
    return preguntas


def guardar_trivia_markdown(preguntas: list[dict[str, Any]], titulo_curso: str, salida_md: Path) -> Path:
    """Convierte las preguntas generadas al formato markdown esperado por build_trivia_scorm.py."""
    lineas = [
        f"# Evaluación: Gran Trivia del Conocimiento - {titulo_curso}",
        "Puntaje mínimo: 70%",
        "Tiempo estimado: 20 minutos\n",
        "> **Instrucciones:** Lee atentamente las situaciones basadas en las 3 lecturas de la clase y selecciona la respuesta correcta.\n"
    ]

    for p in preguntas:
        lineas.append(f"## Pregunta {p['numero']}")
        lineas.append(f"**{p['texto']}**\n")
        opts = p["opciones"]
        for letra in ["A", "B", "C", "D"]:
            if letra in opts:
                lineas.append(f"{letra}) {opts[letra]}")
        lineas.append(f"\n**Respuesta correcta: {p['correcta']}**")
        lineas.append(f"**Explicación:** {p.get('explicacion', '')}\n")

    salida_md.write_text("\n".join(lineas), encoding="utf-8")
    print(f"[OK] Archivo Markdown de trivia guardado en: {salida_md}")
    return salida_md


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generador AI de trivias a partir de las 3 lecturas")
    parser.add_argument("checkpoint", help="Ruta al archivo checkpoint.md con las 3 lecturas")
    parser.add_argument("-n", "--num-questions", type=int, default=10, help="Cantidad de preguntas (default 10)")
    parser.add_argument("-o", "--output", help="Ruta del archivo Markdown de salida", default=None)
    parser.add_argument("--model", default="gemini-flash-lite-latest", help="Modelo eficiente a utilizar")
    args = parser.parse_args()

    cp_path = Path(args.checkpoint)
    out_path = Path(args.output) if args.output else cp_path.parent / f"{cp_path.stem}_trivia.md"

    preguntas = generar_preguntas_trivia(
        checkpoint_path=cp_path,
        model_name=args.model,
        num_preguntas=args.num_questions
    )

    guardar_trivia_markdown(preguntas, cp_path.stem, out_path)
