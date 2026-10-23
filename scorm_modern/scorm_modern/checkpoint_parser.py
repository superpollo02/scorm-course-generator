"""
checkpoint_parser.py
=================
Parsea el archivo markdown intermedio (Checkpoint) generado por la IA o editado
por el usuario y lo convierte en objetos de datos estructurados para su compilación.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List


def parse_checkpoint_markdown(filepath_or_content: str | Path) -> Dict[str, Any]:
    """Parsea el contenido de un archivo checkpoint markdown y retorna un diccionario estructurado."""
    if isinstance(filepath_or_content, Path):
        content = filepath_or_content.read_text(encoding="utf-8")
    elif isinstance(filepath_or_content, str) and Path(filepath_or_content).exists():
        content = Path(filepath_or_content).read_text(encoding="utf-8")
    else:
        content = str(filepath_or_content)

    # Normalizar saltos de línea
    content = content.replace("\r\n", "\n")

    # Extraer metadatos iniciales
    metadata = {
        "curso": "Curso General",
        "id_unidad": "1",
        "clase": "Clase",
        "video_url": "",
    }

    # Buscar metadatos en las primeras líneas
    meta_lines = content.split("\n\n")[0].split("\n")
    for line in meta_lines:
        line_strip = line.strip()
        if line_strip.startswith("# Curso:"):
            metadata["curso"] = line_strip[len("# Curso:"):].strip()
        elif line_strip.startswith("## ID Unidad:"):
            metadata["id_unidad"] = line_strip[len("## ID Unidad:"):].strip()
        elif line_strip.startswith("## Clase:"):
            metadata["clase"] = line_strip[len("## Clase:"):].strip()
        elif line_strip.startswith("## Video URL:"):
            metadata["video_url"] = line_strip[len("## Video URL:"):].strip()

    # Dividir el archivo por secciones de nivel 1 (# )
    # Usamos regex para dividir, pero manteniendo el título de la sección
    sections = re.split(r"\n#\s+", "\n" + content)
    
    introduccion = ""
    lecturas: List[Dict[str, str]] = []
    conectabloques: List[Dict[str, str]] = []
    evaluacion_titulo = "Evaluación de la Clase"
    preguntas: List[Dict[str, Any]] = []

    for section in sections:
        sec_strip = section.strip()
        if not sec_strip:
            continue

        lines = sec_strip.split("\n")
        title = lines[0].strip()
        body = "\n".join(lines[1:]).strip()

        # Limpiar posibles metadatos si es la sección del título del curso
        if title.startswith("Curso:"):
            continue

        # Procesar Introducción
        if title.lower() == "introducción" or title.lower() == "introduccion":
            introduccion = body

        # Procesar Lecturas
        elif title.lower().startswith("lectura"):
            # Título de lectura puede ser "Lectura 1: Título de la lectura"
            m = re.match(r"lectura\s+\d+\s*:\s*(.*)", title, re.IGNORECASE)
            title_lectura = m.group(1).strip() if m else title
            lecturas.append({
                "titulo": title_lectura,
                "contenido": body
            })

        # Procesar Conectabloques
        elif "conectabloques" in title.lower():
            # El cuerpo contiene los términos en nivel 2 (## Término: <nombre>)
            concept_blocks = re.split(r"\n##\s+Término\s*:\s*", "\n" + body)
            for block in concept_blocks:
                block_strip = block.strip()
                if not block_strip:
                    continue
                block_lines = block_strip.split("\n")
                term = block_lines[0].strip()
                
                definition = ""
                origin = ""
                for line in block_lines[1:]:
                    line_l = line.strip()
                    if line_l.startswith("- Definición:") or line_l.startswith("- Definicion:"):
                        definition = line_l[len("- Definición:"):].strip()
                    elif line_l.startswith("- Origen:"):
                        origin = line_l[len("- Origen:"):].strip()

                if term and definition:
                    conectabloques.append({
                        "termino": term,
                        "definicion": definition,
                        "origen": origin
                    })

        # Procesar Cuestionario / Evaluación
        elif "evaluación" in title.lower() or "evaluacion" in title.lower() or "cuestionario" in title.lower():
            m_title = re.match(r"evaluaci[oó]n\s*:\s*(.*)", title, re.IGNORECASE)
            if m_title:
                evaluacion_titulo = m_title.group(1).strip()
            
            # Dividir preguntas por ## Pregunta <N>
            q_blocks = re.split(r"\n##\s+Pregunta\s+(\d+)", "\n" + body)
            # El primer fragmento antes de Pregunta 1 es el texto introductorio de la evaluación, lo ignoramos o guardamos si es útil
            q_index = 1
            while q_index < len(q_blocks):
                num_pregunta = int(q_blocks[q_index])
                q_body = q_blocks[q_index + 1].strip()
                
                # Parsear pregunta
                q_lines = q_body.split("\n")
                
                # Texto de la pregunta (buscar negritas **Texto** o primera línea)
                texto = ""
                opciones: Dict[str, str] = {}
                correcta = ""
                explicacion = ""
                
                current_text_lines = []
                for line in q_lines:
                    line_s = line.strip()
                    if not line_s:
                        continue
                    
                    # Opciones A) Opción
                    m_op = re.match(r"^([A-D])\)\s*(.*)$", line_s, re.IGNORECASE)
                    if m_op:
                        letra = m_op.group(1).upper()
                        opciones[letra] = m_op.group(2).strip()
                        continue
                        
                    # Respuesta correcta
                    m_ans = re.match(r"^\*\*Respuesta correcta\s*:\s*([A-D])\*\*$", line_s, re.IGNORECASE)
                    if m_ans:
                        correcta = m_ans.group(1).upper()
                        continue
                        
                    # Explicación
                    if line_s.startswith("**Explicación:**") or line_s.startswith("**Explicacion:**"):
                        explicacion = line_s[len("**Explicación:**"):].strip()
                        continue
                    
                    if not opciones:  # Todo el texto antes de las opciones es parte de la pregunta
                        # Limpiar las negritas externas de la pregunta si las tiene
                        m_bold = re.match(r"^\*\*(.+)\*\*", line_s)
                        if m_bold:
                            current_text_lines.append(m_bold.group(1).strip())
                        else:
                            current_text_lines.append(line_s)
                
                texto = " ".join(current_text_lines).strip()
                
                if texto and opciones and correcta:
                    preguntas.append({
                        "numero": num_pregunta,
                        "texto": texto,
                        "opciones": opciones,
                        "correcta": correcta,
                        "explicacion": explicacion
                    })
                
                q_index += 2

    return {
        "metadata": metadata,
        "introduccion": introduccion,
        "lecturas": lecturas,
        "conectabloques": conectabloques,
        "evaluacion": {
            "titulo": evaluacion_titulo,
            "preguntas": preguntas
        }
    }
