"""
ai_generator.py
===============
Llama a la API de Google Gemini para generar el contenido del curso a partir de
los insumos del docente (programa.yaml, clase_info.yaml, transcripcion.txt)
y estructurarlo en un archivo markdown intermedio (Checkpoint).
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, List
import yaml

try:
    import google.generativeai as genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

import pydantic
from dotenv import load_dotenv

# Cargar variables de entorno desde .env si existe
load_dotenv()


class Reading(pydantic.BaseModel):
    titulo: str
    contenido_markdown: str


class ConectabloquesConcept(pydantic.BaseModel):
    termino: str
    definicion: str
    origen: str


class Question(pydantic.BaseModel):
    numero: int
    texto: str
    opciones: Dict[str, str]  # Claves: "A", "B", "C", "D"
    correcta: str  # "A", "B", "C" o "D"
    explicacion: str


class CourseCheckpointSchema(pydantic.BaseModel):
    introduccion: str
    lecturas: List[Reading]
    conectabloques: List[ConectabloquesConcept]
    preguntas: List[Question]


def _obtener_config_gemini(api_key: str | None = None) -> str:
    """Configura y retorna la API Key de Gemini."""
    key = api_key or os.getenv("GEMINI_API_KEY")
    if not key:
        raise ValueError(
            "Falta la API Key de Gemini. Por favor configure la variable de entorno "
            "GEMINI_API_KEY o proporcione el parámetro --api-key."
        )
    if HAS_GENAI:
        genai.configure(api_key=key)
    return key


def leer_insumos(ruta_programa: Path, dir_clase: Path) -> Dict[str, Any]:
    """Lee y valida los archivos de entrada (programa y clase)."""
    if not ruta_programa.exists():
        raise FileNotFoundError(f"No se encontró el programa en: {ruta_programa}")
    if not dir_clase.exists() or not dir_clase.is_dir():
        raise FileNotFoundError(f"No se encontró el directorio de clase en: {dir_clase}")

    ruta_clase_info = dir_clase / "clase_info.yaml"
    ruta_transcripcion = dir_clase / "transcripcion.txt"

    if not ruta_clase_info.exists():
        raise FileNotFoundError(f"Falta clase_info.yaml en {dir_clase}")
    if not ruta_transcripcion.exists():
        raise FileNotFoundError(f"Falta transcripcion.txt en {dir_clase}")

    # Cargar programa.yaml
    with open(ruta_programa, "r", encoding="utf-8") as f:
        programa = yaml.safe_load(f)

    # Cargar clase_info.yaml
    with open(ruta_clase_info, "r", encoding="utf-8") as f:
        clase_info = yaml.safe_load(f)

    # Cargar transcripcion.txt
    transcripcion = ruta_transcripcion.read_text(encoding="utf-8")

    return {
        "programa": programa,
        "clase_info": clase_info,
        "transcripcion": transcripcion,
    }


def buscar_unidad_en_programa(programa: Dict[str, Any], id_unidad: str) -> Dict[str, Any]:
    """Busca la unidad correspondiente en el programa utilizando el id_unidad."""
    unidades = programa.get("unidades", [])
    
    # Intentar buscar por número (ej: "unidad-1" -> 1)
    num_str = "".join(c for c in id_unidad if c.isdigit())
    num_buscado = int(num_str) if num_str else None

    for u in unidades:
        if str(u.get("numero")) == str(num_buscado):
            return u
        if str(u.get("numero")) == id_unidad:
            return u
        if id_unidad.lower() in str(u.get("titulo", "")).lower():
            return u

    # Retornar vacío si no se encuentra
    return {}


def generar_prompt(insumos: Dict[str, Any], num_readings: int = 3, num_questions: int = 5) -> tuple[str, str]:
    """Genera el system prompt y el user prompt para alimentar a Gemini."""
    programa = insumos["programa"]
    clase_info = insumos["clase_info"]
    transcripcion = insumos["transcripcion"]

    curso_meta = programa.get("curso", {})
    titulo_curso = curso_meta.get("titulo", "Curso General")
    audiencia = curso_meta.get("audiencia", "Público General")
    enfoque = curso_meta.get("enfoque_pedagogico", "Constructivista")
    objetivos_generales = programa.get("objetivos_generales", [])

    id_unidad = clase_info.get("id_unidad", "1")
    titulo_clase = clase_info.get("titulo_clase", "Clase")
    
    unidad_meta = buscar_unidad_en_programa(programa, id_unidad)
    titulo_unidad = unidad_meta.get("titulo", titulo_clase)
    objetivos_especificos = unidad_meta.get("objetivos_especificicos", [])
    contenidos_minimos = unidad_meta.get("contenidos_minimos", [])

    system_prompt = f"""Eres un experto en diseño instruccional y pedagogía. Tu tarea es procesar la transcripción de una clase dictada por un docente y redactar los contenidos didácticos oficiales para una unidad de aprendizaje interactiva SCORM.

Debes alinearte al siguiente marco curricular del curso:
- Curso: {titulo_curso}
- Enfoque Pedagógico: {enfoque}
- Audiencia Objetivo: {audiencia}
- Objetivos Generales del Curso: {objetivos_generales}

Datos específicos de la Unidad y Clase a procesar:
- Unidad: {titulo_unidad} (ID: {id_unidad})
- Título de la Clase: {titulo_clase}
- Objetivos Específicos de la Unidad: {objetivos_especificos}
- Contenidos Mínimos de la Unidad: {contenidos_minimos}

Directrices de generación:
1. **Introducción**: Redacta una introducción breve, motivadora y clara (1 o 2 párrafos) que encuadre el tema que se verá en la unidad, basándote en la clase del profesor.
2. **Lecturas Estructuradas (Generar exactamente {num_readings})**:
   - Expande y formaliza académicamente los temas discutidos en la transcripción.
   - Deben estar redactadas en un tono formal pero andragógicamente accesible (apto para el estudiante adulto).
   - Utiliza Markdown limpio (negritas, listas, tablas y secciones para estructurar la lectura).
   - Incluye bloques de apoyo conceptual si es necesario.
3. **Actividad Conectabloques**:
   - Extrae entre 4 y 7 conceptos o términos técnicos clave explicados en la transcripción.
   - Define cada término de forma concisa y clara.
   - Extrae el fragmento exacto (snippet) de la transcripción de donde proviene el concepto.
4. **Cuestionario de Evaluación (Generar exactamente {num_questions} preguntas)**:
   - Crea preguntas de opción múltiple con 4 opciones (A, B, C, D) basadas en las lecturas de la clase.
   - Cada pregunta debe ser clara, breve (máximo 20 palabras) y evaluar la comprensión profunda.
   - Indica la opción correcta (letra).
   - Proporciona una explicación corta y clara justificando por qué es la correcta.

CRÍTICO: Evita redundancias, circunloquios y repeticiones infinitas de frases. Mantén todas las respuestas y textos concisos, directos y bien formateados. Bajo ningún concepto entres en un bucle repetitivo de texto o bucle infinito de palabras.
"""

    user_prompt = f"""A continuación se te provee la transcripción literal de la clase. Úsala como fuente de datos exclusiva (evita alucinaciones o agregar temas de tu propia autoría que no se desprendan de esta transcripción o de los contenidos mínimos):

--- TRANSCRIPCIÓN ---
{transcripcion}
--- FIN TRANSCRIPCIÓN ---

Genera los contenidos estructurados respetando el JSON Schema provisto."""

    return system_prompt, user_prompt


def generar_contenido_clase(
    ruta_programa: Path,
    dir_clase: Path,
    api_key: str | None = None,
    model_name: str = "gemini-3.5-flash",
    num_readings: int = 3,
    num_questions: int = 5,
) -> CourseCheckpointSchema:
    """Carga los insumos, llama a Gemini y retorna el resultado estructurado en el esquema."""
    if not HAS_GENAI:
        raise ImportError("El módulo 'google-generativeai' no está disponible.")

    _obtener_config_gemini(api_key)
    insumos = leer_insumos(ruta_programa, dir_clase)
    system_prompt, user_prompt = generar_prompt(insumos, num_readings, num_questions)

    # Definir el esquema JSON manualmente como un diccionario compatible con OpenAPI/Gemini
    schema = {
        "type": "object",
        "properties": {
            "introduccion": {
                "type": "string",
                "description": "Una introducción breve (1-2 párrafos) al tema de la clase."
            },
            "lecturas": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "titulo": {"type": "string", "description": "El título del tema o lectura."},
                        "contenido_markdown": {"type": "string", "description": "El contenido formalizado en Markdown."}
                    },
                    "required": ["titulo", "contenido_markdown"]
                }
            },
            "conectabloques": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "termino": {"type": "string", "description": "El término o concepto clave de la clase (1-3 palabras)."},
                        "definicion": {"type": "string", "description": "La definición concisa del término."},
                        "origen": {"type": "string", "description": "El snippet exacto de la transcripción donde se menciona."}
                    },
                    "required": ["termino", "definicion", "origen"]
                }
            },
            "preguntas": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "numero": {"type": "integer", "description": "El número de la pregunta."},
                        "texto": {"type": "string", "description": "El enunciado de la pregunta."},
                        "opciones": {
                            "type": "object",
                            "properties": {
                                "A": {"type": "string"},
                                "B": {"type": "string"},
                                "C": {"type": "string"},
                                "D": {"type": "string"}
                            },
                            "required": ["A", "B", "C", "D"]
                        },
                        "correcta": {"type": "string", "description": "La letra de la opción correcta (A, B, C, o D)."},
                        "explicacion": {"type": "string", "description": "La justificación de por qué es la correcta."}
                    },
                    "required": ["numero", "texto", "opciones", "correcta", "explicacion"]
                }
            }
        },
        "required": ["introduccion", "lecturas", "conectabloques", "preguntas"]
    }

    # Inicializar el modelo
    model = genai.GenerativeModel(
        model_name=model_name,
        system_instruction=system_prompt,
    )

    # Configurar para obtener una respuesta JSON estructurada basada en el esquema
    generation_config = {
        "response_mime_type": "application/json",
        "response_schema": schema,
        "temperature": 0.2,
    }

    response = model.generate_content(
        contents=user_prompt,
        generation_config=generation_config,
    )

    # Parsear el JSON del texto de respuesta
    try:
        data = CourseCheckpointSchema.model_validate_json(response.text)
        return data
    except Exception as exc:
        # En caso de error, volcar el texto para debugging
        Path("gemini_error_response.json").write_text(response.text, encoding="utf-8")
        raise RuntimeError(f"Error al parsear el esquema estructurado de la respuesta de Gemini: {exc}") from exc


def guardar_checkpoint_markdown(
    datos: CourseCheckpointSchema,
    insumos: Dict[str, Any],
    ruta_salida: Path,
) -> None:
    """Toma la estructura CourseCheckpointSchema y la guarda en un archivo Markdown editable (Checkpoint)."""
    programa = insumos["programa"]
    clase_info = insumos["clase_info"]

    curso_meta = programa.get("curso", {})
    titulo_curso = curso_meta.get("titulo", "Curso General")
    id_unidad = clase_info.get("id_unidad", "1")
    titulo_clase = clase_info.get("titulo_clase", "Clase")
    video_url = clase_info.get("video_url", "")

    lineas = [
        f"# Curso: {titulo_curso}",
        f"## ID Unidad: {id_unidad}",
        f"## Clase: {titulo_clase}",
        f"## Video URL: {video_url}",
        "",
        "# Introducción",
        datos.introduccion.strip(),
        "",
    ]

    # Agregar lecturas
    for i, lec in enumerate(datos.lecturas, 1):
        lineas.extend([
            f"# Lectura {i}: {lec.titulo.strip()}",
            lec.contenido_markdown.strip(),
            "",
        ])

    # Agregar Conectabloques
    lineas.extend([
        "# Actividad: Conectabloques",
        "Relaciona cada concepto o término con su definición correcta.",
        "",
    ])
    for i, con in enumerate(datos.conectabloques, 1):
        lineas.extend([
            f"## Término: {con.termino.strip()}",
            f"- Definición: {con.definicion.strip()}",
            f"- Origen: {con.origen.strip()}",
            "",
        ])

    # Agregar Evaluación
    lineas.extend([
        f"# Evaluación: Cuestionario de la Clase",
        "Responde a las siguientes preguntas para evaluar tu comprensión.",
        "",
    ])
    for q in datos.preguntas:
        lineas.extend([
            f"## Pregunta {q.numero}",
            f"**{q.texto.strip()}**",
            "",
        ])
        for letra in sorted(q.opciones.keys()):
            lineas.append(f"{letra}) {q.opciones[letra].strip()}")
        
        lineas.extend([
            "",
            f"**Respuesta correcta: {q.correcta.strip().upper()}**",
            f"**Explicación:** {q.explicacion.strip()}",
            "",
        ])

    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    ruta_salida.write_text("\n".join(lineas), encoding="utf-8")
