"""
test_checkpoint.py
==================
Pruebas unitarias para el parser del checkpoint markdown y utilidades del generador IA.
"""

from __future__ import annotations

from pathlib import Path
from scorm_modern.checkpoint_parser import parse_checkpoint_markdown
from scorm_modern.ai_generator import buscar_unidad_en_programa, generar_prompt


def test_buscar_unidad_en_programa():
    programa = {
        "unidades": [
            {"numero": 1, "titulo": "Fundamentos"},
            {"numero": 2, "titulo": "Conceptos Avanzados"},
        ]
    }
    
    # Buscar por número entero
    u1 = buscar_unidad_en_programa(programa, "unidad-1")
    assert u1["numero"] == 1
    
    # Buscar por número de cadena
    u2 = buscar_unidad_en_programa(programa, "2")
    assert u2["numero"] == 2
    
    # Buscar por coincidencia de texto
    u3 = buscar_unidad_en_programa(programa, "Avanzados")
    assert u3["numero"] == 2


def test_parse_checkpoint_markdown():
    mock_md = """# Curso: Curso de IA
## ID Unidad: unidad-1
## Clase: Clase Especial de IA
## Video URL: https://www.youtube.com/embed/12345

# Introducción
Esta es la introducción de la clase de IA.

# Lectura 1: Introducción a LLMs
Los LLMs son modelos lingüísticos de grandes dimensiones...

# Actividad: Conectabloques
Une cada término con su definición.

## Término: Prompt
- Definición: Texto de entrada para una IA
- Origen: En el video se dice "el prompt es el texto..."

# Evaluación: Cuestionario Especial
Responde para verificar conocimientos.

## Pregunta 1
**¿Qué es un LLM?**

A) Large Language Model
B) Low Level Machine
C) Local Language Mode
D) Ninguno de los anteriores

**Respuesta correcta: A**
**Explicación:** Significa Large Language Model.
"""

    parsed = parse_checkpoint_markdown(mock_md)
    
    # Verificar metadatos
    assert parsed["metadata"]["curso"] == "Curso de IA"
    assert parsed["metadata"]["id_unidad"] == "unidad-1"
    assert parsed["metadata"]["clase"] == "Clase Especial de IA"
    assert parsed["metadata"]["video_url"] == "https://www.youtube.com/embed/12345"
    
    # Verificar introducción
    assert parsed["introduccion"] == "Esta es la introducción de la clase de IA."
    
    # Verificar lecturas
    assert len(parsed["lecturas"]) == 1
    assert parsed["lecturas"][0]["titulo"] == "Introducción a LLMs"
    assert "Los LLMs son modelos" in parsed["lecturas"][0]["contenido"]
    
    # Verificar conectabloques
    assert len(parsed["conectabloques"]) == 1
    assert parsed["conectabloques"][0]["termino"] == "Prompt"
    assert parsed["conectabloques"][0]["definicion"] == "Texto de entrada para una IA"
    assert parsed["conectabloques"][0]["origen"] == "En el video se dice \"el prompt es el texto...\""
    
    # Verificar evaluación
    assert parsed["evaluacion"]["titulo"] == "Cuestionario Especial"
    assert len(parsed["evaluacion"]["preguntas"]) == 1
    q = parsed["evaluacion"]["preguntas"][0]
    assert q["numero"] == 1
    assert q["texto"] == "¿Qué es un LLM?"
    assert q["opciones"]["A"] == "Large Language Model"
    assert q["correcta"] == "A"
    assert q["explicacion"] == "Significa Large Language Model."
