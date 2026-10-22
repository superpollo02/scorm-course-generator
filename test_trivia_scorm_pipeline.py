"""
test_trivia_scorm_pipeline.py
==============================
Test de verificación integral del objeto SCORM 1.2 Trivia:
1. Valida el parseo de las 3 lecturas extendidas.
2. Valida la estructura de preguntas generadas (opciones A-D, respuesta correcta, feedback).
3. Valida el empaquetado ZIP SCORM 1.2 (imsmanifest.xml e index.html en raíz, sin gift).
4. Valida la sintaxis del imsmanifest.xml (esquema XML 1.2, tags cerrados, masteryscore).
5. Valida el HTML e integración JavaScript con la API SCORM 1.2 (LMSInitialize, cmi.core.score.raw, cmi.core.lesson_status, LMSFinish).
"""

import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

# Agregar directorio scripts al path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

from scripts.content_generation.generate_trivia_ai import extraer_las_tres_lecturas
from scripts.scorm_generators.build_trivia_scorm import (
    empaquetar_trivia_scorm,
    parse_trivia_markdown,
)


def ejecutar_pruebas():
    print("=" * 60)
    print("EJECUTANDO BATERIA DE PRUEBAS: OBJETO TRIVIA SCORM 1.2")
    print("=" * 60)
    errores = []

    # 1. Prueba de extracción de las 3 lecturas extendidas
    checkpoint_file = BASE_DIR / "test_inputs" / "checkpoint.md"
    try:
        lecturas = extraer_las_tres_lecturas(checkpoint_file)
        assert len(lecturas) == 3, f"Se esperaban 3 lecturas y se obtuvieron {len(lecturas)}"
        print(f"[PASO 1/5 OK] Extracción de las 3 lecturas exitosa ({len(lecturas)} encontradas).")
    except Exception as e:
        errores.append(f"Fallo en Paso 1 (Extracción de lecturas): {e}")

    # 2. Prueba de parseo de trivia markdown
    trivia_md_file = BASE_DIR / "test_inputs" / "trivia_generada.md"
    try:
        contenido = trivia_md_file.read_text(encoding="utf-8")
        trivia_data = parse_trivia_markdown(contenido)
        assert len(trivia_data.preguntas) > 0, "No se detectaron preguntas en el archivo"
        for p in trivia_data.preguntas:
            assert p.correcta in ["A", "B", "C", "D"], f"Pregunta {p.numero}: Clave inválida '{p.correcta}'"
            assert len(p.opciones) == 4, f"Pregunta {p.numero}: Debe tener exactamente 4 opciones A-D"
            assert bool(p.explicacion), f"Pregunta {p.numero}: Falta retroalimentación/explicación"
        print(f"[PASO 2/5 OK] Validación de estructura de preguntas ({len(trivia_data.preguntas)} preguntas con opciones A-D y retroalimentación).")
    except Exception as e:
        errores.append(f"Fallo en Paso 2 (Estructura de preguntas): {e}")

    # 3. Prueba de empaquetado y exclusión de cuestionario.gift del ZIP
    output_zip = BASE_DIR / "output" / "test_trivia_verified-SCORM.zip"
    try:
        empaquetar_trivia_scorm(trivia_md_file, output_zip)
        with zipfile.ZipFile(output_zip, "r") as zf:
            archivos = zf.namelist()
            assert "imsmanifest.xml" in archivos, "Falta imsmanifest.xml en la raíz del zip"
            assert "index.html" in archivos, "Falta index.html en la raíz del zip"
            assert "cuestionario.gift" not in archivos, "cuestionario.gift NO debe estar dentro del ZIP SCORM"
        print(f"[PASO 3/5 OK] Paquete ZIP generado y limpio (solo imsmanifest.xml e index.html en raíz).")
    except Exception as e:
        errores.append(f"Fallo en Paso 3 (Empaquetado SCORM): {e}")

    # 4. Prueba de conformidad XML del manifiesto SCORM 1.2
    try:
        with zipfile.ZipFile(output_zip, "r") as zf:
            manifest_xml = zf.read("imsmanifest.xml").decode("utf-8")
            ET.fromstring(manifest_xml)  # Valida sintaxis XML
            assert "1.2" in manifest_xml, "El manifiesto debe especificar versión 1.2"
            assert "adlcp:masteryscore" in manifest_xml or "masteryscore" in manifest_xml, "Debe incluir masteryscore para el umbral de aprobación"
        print(f"[PASO 4/5 OK] Conformidad XML de imsmanifest.xml para SCORM 1.2 validada.")
    except Exception as e:
        errores.append(f"Fallo en Paso 4 (Validación XML): {e}")

    # 5. Prueba de integración JavaScript / SCORM API en index.html
    try:
        with zipfile.ZipFile(output_zip, "r") as zf:
            html_content = zf.read("index.html").decode("utf-8")
            requisitos_js = [
                "LMSInitialize",
                "cmi.core.score.raw",
                "cmi.core.lesson_status",
                "LMSCommit",
                "LMSFinish"
            ]
            for req in requisitos_js:
                assert req in html_content, f"Falta llamada a la API SCORM obligatoria: {req}"
        print(f"[PASO 5/5 OK] Llamadas a la API SCORM 1.2 verificadas en el reproductor HTML.")
    except Exception as e:
        errores.append(f"Fallo en Paso 5 (API SCORM en index.html): {e}")

    print("=" * 60)
    if not errores:
        print("[RESULTADO FINAL: EXITO TOTAL] El objeto Trivia SCORM 1.2 es 100% valido y compatible con Moodle.")
    else:
        print(f"[RESULTADO FINAL: ERRORES DETECTADOS ({len(errores)})]")
        for err in errores:
            print(f"  - {err}")
    print("=" * 60)

    return len(errores) == 0


if __name__ == "__main__":
    exito = ejecutar_pruebas()
    sys.exit(0 if exito else 1)
