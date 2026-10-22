"""
build_trivia_scorm.py
=====================
Generador autónomo de paquetes SCORM 1.2 interactivos estilo Trivia Gamificada
y exportador a formato GIFT de Moodle.

Inspirado en SCORM AI Builder Pro (React 19 / Express / Gemini Flash Lite).
"""

from __future__ import annotations

import argparse
import html
import json
import re
import zipfile
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class PreguntaTrivia:
    numero: int
    texto: str
    opciones: dict[str, str]  # ej: {'A': '...', 'B': '...'}
    correcta: str             # ej: 'B'
    explicacion: str = ""


@dataclass
class TriviaData:
    titulo: str
    puntaje_minimo: int = 70
    preguntas: list[PreguntaTrivia] = field(default_factory=list)


def parse_trivia_markdown(contenido_md: str) -> TriviaData:
    """Parsea el archivo markdown de trivia extrayendo título, preguntas, opciones y claves."""
    lineas = contenido_md.splitlines()
    titulo = "Trivia Interactiva"
    puntaje_minimo = 70
    preguntas: list[PreguntaTrivia] = []

    # Extraer título general
    for l in lineas:
        if l.startswith("# Evaluación:") or l.startswith("# Trivia:") or l.startswith("# Cuestionario:"):
            titulo = l.split(":", 1)[1].strip()
            break
        elif l.startswith("# "):
            titulo = l[2:].strip()
            break

    # Buscar puntaje mínimo si se declara
    match_score = re.search(r"puntaje\s+m[íi]nimo[:\s]+(\d+)", contenido_md, re.IGNORECASE)
    if match_score:
        puntaje_minimo = int(match_score.group(1))

    # Parsear preguntas
    bloques_preguntas = re.split(r"^##\s+Pregunta\s+(\d+)", contenido_md, flags=re.MULTILINE)
    
    # El primer elemento antes de la primera pregunta es cabecera
    for i in range(1, len(bloques_preguntas), 2):
        num_pregunta = int(bloques_preguntas[i])
        cuerpo = bloques_preguntas[i + 1]

        # Extraer texto de la pregunta
        lineas_cuerpo = cuerpo.strip().splitlines()
        texto_pregunta = ""
        opciones: dict[str, str] = {}
        correcta = "A"
        explicacion = ""

        for l in lineas_cuerpo:
            l_str = l.strip()
            if not l_str:
                continue

            # Buscar enunciado
            if not texto_pregunta and not re.match(r"^[A-D]\)", l_str) and not l_str.lower().startswith("**respuesta"):
                # Limpiar posibles asteriscos
                texto_pregunta = re.sub(r"^\*+|\*+$", "", l_str).strip()
                continue

            # Buscar opciones
            match_op = re.match(r"^([A-D])\)\s*(.+)$", l_str)
            if match_op:
                opciones[match_op.group(1)] = match_op.group(2).strip()
                continue

            # Buscar respuesta correcta
            match_corr = re.match(r"^\*\*Respuesta\s+correcta[:\s]+([A-D])\*\*", l_str, re.IGNORECASE)
            if match_corr:
                correcta = match_corr.group(1).upper()
                continue

            # Buscar explicación
            match_exp = re.match(r"^\*\*Explicaci[óo]n[:\s]+\*\*\s*(.+)$", l_str, re.IGNORECASE)
            if match_exp:
                explicacion = match_exp.group(1).strip()
                continue

        if texto_pregunta and opciones:
            preguntas.append(
                PreguntaTrivia(
                    numero=num_pregunta,
                    texto=texto_pregunta,
                    opciones=opciones,
                    correcta=correcta,
                    explicacion=explicacion
                )
            )

    return TriviaData(titulo=titulo, puntaje_minimo=puntaje_minimo, preguntas=preguntas)


def generar_gift(trivia: TriviaData) -> str:
    """Genera exportación en formato GIFT para Moodle."""
    lineas = [f"// =============================================",
              f"// Cuestionario GIFT: {trivia.titulo}",
              f"// Generado por SCORM Trivia Engine",
              f"// =============================================\n"]
    for p in trivia.preguntas:
        lineas.append(f"::P{p.numero} - {p.texto[:30]}::{p.texto} {{")
        for letra, texto in sorted(p.opciones.items()):
            if letra == p.correcta:
                exp = f" #{p.explicacion}" if p.explicacion else ""
                lineas.append(f"  ={texto}{exp}")
            else:
                lineas.append(f"  ~{texto}")
        lineas.append("}\n")
    return "\n".join(lineas)


def generar_html_trivia(trivia: TriviaData) -> str:
    """Genera el reproductor interactivo moderno autocontenido estilo Trivia con soporte SCORM 1.2."""
    preguntas_json = json.dumps([
        {
            "numero": p.numero,
            "texto": p.texto,
            "opciones": [{"letra": k, "texto": v} for k, v in sorted(p.opciones.items())],
            "correcta": p.correcta,
            "explicacion": p.explicacion
        }
        for p in trivia.preguntas
    ], ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(trivia.titulo)}</title>
  <style>
    :root {{
      --primary: #4f46e5;
      --primary-hover: #4338ca;
      --bg: #0f172a;
      --card-bg: #1e293b;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --success: #10b981;
      --error: #ef4444;
      --accent: #f59e0b;
      --border: #334155;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 1.5rem;
    }}
    .trivia-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 1.25rem;
      box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.5);
      width: 100%;
      max-width: 720px;
      padding: 2.25rem;
      position: relative;
      overflow: hidden;
    }}
    .trivia-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.5rem;
      border-bottom: 1px solid var(--border);
      padding-bottom: 1rem;
    }}
    .badge {{
      background: rgba(79, 70, 229, 0.2);
      color: #818cf8;
      border: 1px solid rgba(129, 140, 248, 0.3);
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 600;
    }}
    .progress-bar {{
      height: 6px;
      background: var(--border);
      border-radius: 9999px;
      margin-bottom: 1.5rem;
      overflow: hidden;
    }}
    .progress-fill {{
      height: 100%;
      background: linear-gradient(90deg, var(--primary), #06b6d4);
      width: 0%;
      transition: width 0.4s ease;
    }}
    .question-title {{
      font-size: 1.35rem;
      font-weight: 700;
      line-height: 1.5;
      margin-bottom: 1.75rem;
    }}
    .options-grid {{
      display: grid;
      gap: 0.85rem;
    }}
    .option-btn {{
      background: rgba(255, 255, 255, 0.03);
      border: 2px solid var(--border);
      border-radius: 0.75rem;
      padding: 1rem 1.25rem;
      color: var(--text);
      font-size: 1rem;
      text-align: left;
      cursor: pointer;
      display: flex;
      align-items: center;
      transition: all 0.2s ease;
    }}
    .option-btn:hover:not(:disabled) {{
      background: rgba(79, 70, 229, 0.15);
      border-color: var(--primary);
      transform: translateY(-2px);
    }}
    .option-btn .opt-badge {{
      background: var(--border);
      font-weight: bold;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      margin-right: 1rem;
      flex-shrink: 0;
    }}
    .option-btn.correct {{
      background: rgba(16, 185, 129, 0.2) !important;
      border-color: var(--success) !important;
      color: #34d399 !important;
    }}
    .option-btn.correct .opt-badge {{
      background: var(--success);
      color: #fff;
    }}
    .option-btn.wrong {{
      background: rgba(239, 68, 68, 0.2) !important;
      border-color: var(--error) !important;
      color: #f87171 !important;
    }}
    .option-btn.wrong .opt-badge {{
      background: var(--error);
      color: #fff;
    }}
    .feedback-box {{
      margin-top: 1.5rem;
      padding: 1.25rem;
      border-radius: 0.75rem;
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid var(--border);
      font-size: 0.95rem;
      line-height: 1.5;
      display: none;
    }}
    .feedback-box.active {{
      display: block;
      animation: fadeIn 0.3s ease;
    }}
    .next-btn {{
      margin-top: 1.5rem;
      width: 100%;
      background: var(--primary);
      color: #fff;
      border: none;
      border-radius: 0.75rem;
      padding: 0.95rem;
      font-size: 1.05rem;
      font-weight: 600;
      cursor: pointer;
      display: none;
      transition: background 0.2s ease;
    }}
    .next-btn:hover {{
      background: var(--primary-hover);
    }}
    .final-screen {{
      text-align: center;
      display: none;
    }}
    .final-score {{
      font-size: 4rem;
      font-weight: 800;
      color: var(--accent);
      margin: 1rem 0;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
  </style>
</head>
<body>
  <div class="trivia-card">
    <div class="trivia-header">
      <span class="badge" id="lbl-categoria">Desafío Trivia</span>
      <span style="font-weight: 600; color: var(--text-muted);" id="lbl-contador">Pregunta 1 de {len(trivia.preguntas)}</span>
    </div>
    
    <div class="progress-bar">
      <div class="progress-fill" id="progress-fill"></div>
    </div>

    <div id="game-container">
      <h2 class="question-title" id="question-text">Cargando desafío...</h2>
      <div class="options-grid" id="options-container"></div>
      <div class="feedback-box" id="feedback-container"></div>
      <button class="next-btn" id="next-btn" onclick="nextQuestion()">Siguiente Pregunta &rarr;</button>
    </div>

    <div class="final-screen" id="final-screen">
      <h2 style="font-size: 2rem; margin-bottom: 0.5rem;" id="final-title">¡Trivia Finalizada!</h2>
      <p style="color: var(--text-muted);" id="final-subtitle">Has completado todos los desafíos del módulo.</p>
      <div class="final-score" id="score-display">0%</div>
      <p id="final-status-msg" style="margin-bottom: 2rem; font-size: 1.15rem;"></p>
      <button class="option-btn" style="justify-content: center; font-weight: bold; width: 100%;" onclick="reiniciarTrivia()">Intentar Nuevamente</button>
    </div>
  </div>

  <script>
    var PREGUNTAS = {preguntas_json};
    var PUNTAJE_MINIMO = {trivia.puntaje_minimo};
    var currentIdx = 0;
    var aciertos = 0;
    var respondido = false;

    // --- COMUNICACIÓN SCORM 1.2 ---
    var scormAPI = null;
    function findSCORMAPI(win) {{
      var attempts = 0;
      while (win && !win.API && win.parent && win.parent !== win && attempts < 10) {{
        attempts++;
        win = win.parent;
      }}
      return win ? win.API : null;
    }}

    function initSCORM() {{
      scormAPI = findSCORMAPI(window);
      if (scormAPI) {{
        scormAPI.LMSInitialize("");
        scormAPI.LMSSetValue("cmi.core.lesson_status", "incomplete");
        scormAPI.LMSCommit("");
      }}
    }}

    function finishSCORM(aprobado, score) {{
      if (scormAPI) {{
        scormAPI.LMSSetValue("cmi.core.score.raw", String(score));
        scormAPI.LMSSetValue("cmi.core.score.min", "0");
        scormAPI.LMSSetValue("cmi.core.score.max", "100");
        scormAPI.LMSSetValue("cmi.core.lesson_status", aprobado ? "passed" : "failed");
        scormAPI.LMSCommit("");
        scormAPI.LMSFinish("");
      }}
    }}

    window.onload = function() {{
      initSCORM();
      renderCurrentQuestion();
    }};

    function renderCurrentQuestion() {{
      respondido = false;
      var q = PREGUNTAS[currentIdx];
      var total = PREGUNTAS.length;

      document.getElementById("lbl-contador").innerText = "Pregunta " + (currentIdx + 1) + " de " + total;
      document.getElementById("progress-fill").style.width = ((currentIdx / total) * 100) + "%";
      document.getElementById("question-text").innerText = q.texto;

      var optsContainer = document.getElementById("options-container");
      optsContainer.innerHTML = "";

      var optsFrag = document.createDocumentFragment();
      q.opciones.forEach(function(opt) {{
        var btn = document.createElement("button");
        btn.className = "option-btn";
        btn.innerHTML = '<span class="opt-badge">' + opt.letra + '</span><span>' + opt.texto + '</span>';
        btn.onclick = function() {{ checkAnswer(opt.letra, btn); }};
        optsFrag.appendChild(btn);
      }});
      optsContainer.appendChild(optsFrag);

      var fb = document.getElementById("feedback-container");
      fb.className = "feedback-box";
      fb.style.display = "none";
      fb.innerHTML = "";

      document.getElementById("next-btn").style.display = "none";
    }}

    function checkAnswer(letraSeleccionada, btnElement) {{
      if (respondido) return;
      respondido = true;
      var q = PREGUNTAS[currentIdx];
      var buttons = document.querySelectorAll(".option-btn");
      buttons.forEach(function(b) {{ b.disabled = true; }});

      var esCorrecta = (letraSeleccionada === q.correcta);
      if (esCorrecta) {{
        aciertos++;
        btnElement.classList.add("correct");
      }} else {{
        btnElement.classList.add("wrong");
        buttons.forEach(function(b) {{
          if (b.innerText.trim().startsWith(q.correcta)) {{
            b.classList.add("correct");
          }}
        }});
      }}

      var fb = document.getElementById("feedback-container");
      fb.innerHTML = (esCorrecta ? "<strong>🎉 ¡Excelente!</strong> " : "<strong>❌ Respuesta incorrecta.</strong> ") +
                     (q.explicacion ? q.explicacion : ("La opción correcta es la " + q.correcta + "."));
      fb.classList.add("active");
      fb.style.display = "block";

      var nextBtn = document.getElementById("next-btn");
      nextBtn.style.display = "block";
      if (currentIdx === PREGUNTAS.length - 1) {{
        nextBtn.innerText = "Ver Resultados Finales 🏆";
      }} else {{
        nextBtn.innerText = "Siguiente Pregunta &rarr;";
      }}
    }}

    function nextQuestion() {{
      if (currentIdx < PREGUNTAS.length - 1) {{
        currentIdx++;
        renderCurrentQuestion();
      }} else {{
        showFinalScreen();
      }}
    }}

    function showFinalScreen() {{
      document.getElementById("game-container").style.display = "none";
      document.getElementById("progress-fill").style.width = "100%";
      var screen = document.getElementById("final-screen");
      screen.style.display = "block";

      var total = PREGUNTAS.length;
      var porcentaje = Math.round((aciertos / total) * 100);
      var aprobado = porcentaje >= PUNTAJE_MINIMO;

      document.getElementById("score-display").innerText = porcentaje + "%";
      var msg = document.getElementById("final-status-msg");
      if (aprobado) {{
        msg.innerHTML = "🏆 <strong>¡Felicitaciones!</strong> Has superado el desafío (Aciertos: " + aciertos + "/" + total + ").";
        msg.style.color = "var(--success)";
      }} else {{
        msg.innerHTML = "⚠️ <strong>No alcanzaste el puntaje mínimo de " + PUNTAJE_MINIMO + "%.</strong> (Aciertos: " + aciertos + "/" + total + "). ¡Repasa y vuelve a intentarlo!";
        msg.style.color = "var(--error)";
      }}

      finishSCORM(aprobado, porcentaje);
    }}

    function reiniciarTrivia() {{
      currentIdx = 0;
      aciertos = 0;
      respondido = false;
      document.getElementById("final-screen").style.display = "none";
      document.getElementById("game-container").style.display = "block";
      initSCORM();
      renderCurrentQuestion();
    }}
  </script>
</body>
</html>
"""


def generar_manifest_scorm(trivia: TriviaData, identifier: str = "TRIVIA_SCORM") -> str:
    """Genera imsmanifest.xml estándar SCORM 1.2."""
    titulo_escaped = html.escape(trivia.titulo)
    return f"""<?xml version="1.0" standalone="no" ?>
<!-- Generator: SCORM AI Builder Pro / Antigravity -->
<manifest identifier="{identifier}" version="1.2"
          xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
          xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd
                              http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
  </metadata>
  <organizations default="org_{identifier}">
    <organization identifier="org_{identifier}">
      <title>{titulo_escaped}</title>
      <item identifier="item_trivia" identifierref="res_trivia">
        <title>{titulo_escaped}</title>
        <adlcp:masteryscore>{trivia.puntaje_minimo}</adlcp:masteryscore>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="res_trivia" type="webcontent" adlcp:scormtype="sco" href="index.html">
      <file href="index.html"/>
    </resource>
  </resources>
</manifest>
"""


def empaquetar_trivia_scorm(ruta_md: Path, salida_zip: Path | None = None) -> Path:
    """Lee el archivo markdown, genera el HTML interactivo, manifest y empaqueta en ZIP."""
    if not ruta_md.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {ruta_md}")

    contenido = ruta_md.read_text(encoding="utf-8")
    trivia = parse_trivia_markdown(contenido)

    if not trivia.preguntas:
        raise ValueError(f"No se detectaron preguntas válidas en {ruta_md}")

    if salida_zip is None:
        salida_zip = ruta_md.with_name(f"{ruta_md.stem}-SCORM.zip")

    html_content = generar_html_trivia(trivia)
    manifest_content = generar_manifest_scorm(trivia, identifier=ruta_md.stem)
    # generar_gift(trivia) si se necesita en el futuro

    # Crear ZIP con manifest en la raíz y index.html (estándar limpio SCORM 1.2)
    with zipfile.ZipFile(salida_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("imsmanifest.xml", manifest_content.encode("utf-8"))
        zf.writestr("index.html", html_content.encode("utf-8"))

    print(f"[OK] Paquete SCORM 1.2 generado exitosamente: {salida_zip}")
    print(f"   - Titulo: {trivia.titulo}")
    print(f"   - Preguntas: {len(trivia.preguntas)}")
    print(f"   - Puntaje Minimo: {trivia.puntaje_minimo}%")
    return salida_zip


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generador de paquetes SCORM 1.2 estilo Trivia")
    parser.add_argument("markdown", help="Ruta al archivo Markdown con las preguntas de la trivia")
    parser.add_argument("-o", "--output", help="Ruta de salida para el archivo .zip", default=None)
    args = parser.parse_args()

    salida = Path(args.output) if args.output else None
    empaquetar_trivia_scorm(Path(args.markdown), salida)
