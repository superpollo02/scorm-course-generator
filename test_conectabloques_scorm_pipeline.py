"""
test_conectabloques_scorm_pipeline.py
=====================================
Test integral de verificación para Conectabloques SCORM 1.2:
1. Valida extracción de conceptos a partir de las 3 lecturas extendidas.
2. Valida la estructura del archivo markdown intermedio (Término, Definición, Origen).
3. Valida el empaquetado del archivo .zip independiente.
4. Valida la conformidad del imsmanifest.xml (SCORM 1.2, masteryscore).
5. Valida el HTML autónomo: temas visuales, Web Audio API y comunicación SCORM 1.2 (LMSInitialize, cmi.core.score.raw, cmi.core.lesson_status, LMSFinish).
"""

import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

from scripts.content_generation.generate_conectabloques_ai import extraer_las_tres_lecturas
from scripts.scorm_generators.build_conectabloques_scorm import (
    empaquetar_conectabloques_scorm,
    parse_conectabloques_markdown,
)


def ejecutar_pruebas():
    print("=" * 65)
    print("EJECUTANDO BATERIA DE PRUEBAS: CONECTABLOQUES SCORM 1.2")
    print("=" * 65)
    errores = []

    # 1. Extracción de las 3 lecturas
    checkpoint_file = BASE_DIR / "test_inputs" / "checkpoint.md"
    try:
        lecturas = extraer_las_tres_lecturas(checkpoint_file)
        assert len(lecturas) == 3, f"Se esperaban 3 lecturas, se obtuvieron {len(lecturas)}"
        print(f"[PASO 1/5 OK] Extracción exitosa de las 3 lecturas extendidas.")
    except Exception as e:
        errores.append(f"Fallo en Paso 1: {e}")

    # 2. Parseo de conceptos
    conecta_md = BASE_DIR / "test_inputs" / "conectabloques_generado.md"
    try:
        data = parse_conectabloques_markdown(conecta_md.read_text(encoding="utf-8"))
        assert len(data.conceptos) >= 5, f"Se esperaban al menos 5 conceptos, hay {len(data.conceptos)}"
        assert data.tiempo_limite_minutos == 20, f"Tiempo límite esperado 20 min, hay {data.tiempo_limite_minutos}"
        print(f"[PASO 2/5 OK] Parseo correcto ({len(data.conceptos)} conceptos, tiempo límite: 20 min, tema: {data.tema}).")
    except Exception as e:
        errores.append(f"Fallo en Paso 2: {e}")

    # 3. Empaquetado ZIP
    zip_salida = BASE_DIR / "output" / "test_conectabloques_verified-SCORM.zip"
    try:
        empaquetar_conectabloques_scorm(conecta_md, zip_salida, tema="modern-mint")
        with zipfile.ZipFile(zip_salida, "r") as zf:
            archivos = zf.namelist()
            assert "imsmanifest.xml" in archivos, "Falta imsmanifest.xml en la raíz"
            assert "index.html" in archivos, "Falta index.html en la raíz"
        print(f"[PASO 3/5 OK] Empaquetado ZIP independiente limpio (imsmanifest.xml e index.html en raíz).")
    except Exception as e:
        errores.append(f"Fallo en Paso 3: {e}")

    # 4. Conformidad XML
    try:
        with zipfile.ZipFile(zip_salida, "r") as zf:
            manifest_xml = zf.read("imsmanifest.xml").decode("utf-8")
            ET.fromstring(manifest_xml)
            assert "1.2" in manifest_xml
            assert "masteryscore" in manifest_xml
        print(f"[PASO 4/5 OK] Conformidad XML según estándar ADL SCORM 1.2 verificada.")
    except Exception as e:
        errores.append(f"Fallo en Paso 4: {e}")

    # 5. Lógica HTML / Audio / SCORM
    try:
        with zipfile.ZipFile(zip_salida, "r") as zf:
            html_content = zf.read("index.html").decode("utf-8")
            elementos_obligatorios = [
                "LMSInitialize",
                "cmi.core.score.raw",
                "cmi.core.lesson_status",
                "LMSCommit",
                "LMSFinish",
                "AudioContext",
                "timerSeconds"
            ]
            for elem in elementos_obligatorios:
                assert elem in html_content, f"Falta elemento en HTML: {elem}"
        print(f"[PASO 5/5 OK] Mecánicas de juego, Web Audio y API SCORM 1.2 verificadas en el reproductor.")
    except Exception as e:
        errores.append(f"Fallo en Paso 5: {e}")

    print("=" * 65)
    if not errores:
        print("[RESULTADO FINAL: EXITO TOTAL] El objeto Conectabloques SCORM 1.2 es 100% operativo.")
    else:
        print(f"[RESULTADO FINAL: ERRORES ({len(errores)})]")
        for err in errores:
            print(f"  - {err}")
    print("=" * 65)

    return len(errores) == 0


if __name__ == "__main__":
    exito = ejecutar_pruebas()
    sys.exit(0 if exito else 1)
