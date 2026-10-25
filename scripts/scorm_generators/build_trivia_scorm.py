"""
build_trivia_scorm.py
=====================
Generador autónomo de paquetes SCORM 1.2 interactivos estilo Trivia Gamificada
con Modo Turno (Slideshow/Turn-by-turn), Personalización Neón/Temas,
Barra de Accesibilidad WCAG y Modo Turbo (1 y 2).

Inspirado en ScormQuest Studio (React 18 / Vite / TypeScript / Tailwind).
"""

from __future__ import annotations

import argparse
import html
import json
import random
import re
import sys
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

# Importación unificada del manifest
try:
    from scorm_core.manifest import generar_manifest_scorm_unificado
except ImportError:
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
    from scorm_core.manifest import generar_manifest_scorm_unificado

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


@dataclass
class PreguntaTrivia:
    numero: int
    texto: str
    opciones: dict[str, str]  # ej: {'A': '...', 'B': '...'}
    correcta: str             # ej: 'B'
    explicacion: str = ""


@dataclass
class OpcionesPersonalizacion:
    tema: str = "neon"  # neon, corporate, minimal, high-contrast, sunset, forest, cosmic
    neon_primary: str = "#0c071e"
    neon_accent: str = "#ffd700"
    modo_turno: bool = True
    feedback_timing: str = "immediate"  # immediate | end
    tiempo_limite: int = 0              # minutos (0 = sin límite)
    barajar: bool = False
    modo_accesibilidad: bool = True     # Muestra toolbar A+/A- y alto contraste


@dataclass
class TriviaData:
    titulo: str
    puntaje_minimo: int = 70
    preguntas: list[PreguntaTrivia] = field(default_factory=list)
    personalizacion: OpcionesPersonalizacion = field(default_factory=OpcionesPersonalizacion)


def ajustar_brillo_hex(hex_color: str, percent: int) -> str:
    """Ajusta el brillo de un color hexadecimal de forma segura."""
    try:
        hex_color = hex_color.strip()
        if not hex_color.startswith("#") or len(hex_color) < 7:
            return hex_color
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)

        r = max(0, min(255, r + percent))
        g = max(0, min(255, g + percent))
        b = max(0, min(255, b + percent))

        return f"#{r:02x}{g:02x}{b:02x}"
    except Exception:
        return hex_color


def obtener_configuracion_tema(opt: OpcionesPersonalizacion) -> dict[str, str]:
    """Genera las variables CSS según el tema seleccionado."""
    primary = opt.neon_primary or "#0c071e"
    accent = opt.neon_accent or "#ffd700"

    temas = {
        "neon": {
            "bg": f"radial-gradient(circle, {ajustar_brillo_hex(primary, 15)} 0%, {primary} 100%)",
            "card_bg": ajustar_brillo_hex(primary, 22),
            "accent": accent,
            "text": "#ffffff",
            "text_muted": "#cbd5e1",
            "border": f"1px solid {ajustar_brillo_hex(accent, -30)}",
            "glow": f"0 0 15px {accent}",
            "btn_text": "#000000"
        },
        "corporate": {
            "bg": "#f8fafc",
            "card_bg": "#ffffff",
            "accent": "#2563eb",
            "text": "#1e293b",
            "text_muted": "#64748b",
            "border": "1px solid #e2e8f0",
            "glow": "none",
            "btn_text": "#ffffff"
        },
        "minimal": {
            "bg": "#ffffff",
            "card_bg": "#f9fafb",
            "accent": "#111827",
            "text": "#374151",
            "text_muted": "#6b7280",
            "border": "1px solid #e5e7eb",
            "glow": "none",
            "btn_text": "#ffffff"
        },
        "high-contrast": {
            "bg": "#000000",
            "card_bg": "#0a0a0a",
            "accent": "#ffff00",
            "text": "#ffffff",
            "text_muted": "#e2e8f0",
            "border": "2.5px solid #ffffff",
            "glow": "none",
            "btn_text": "#000000"
        },
        "sunset": {
            "bg": "linear-gradient(135deg, #fdf2f8 0%, #fef3c7 50%, #ffe4e6 100%)",
            "card_bg": "rgba(255, 255, 255, 0.95)",
            "accent": "#ea580c",
            "text": "#3c0d02",
            "text_muted": "#7c2d12",
            "border": "1px solid #ffe4e6",
            "glow": "0 10px 25px rgba(234, 88, 12, 0.15)",
            "btn_text": "#ffffff"
        },
        "forest": {
            "bg": "linear-gradient(135deg, #f0fdf4 0%, #dcfce7 50%, #bbf7d0 100%)",
            "card_bg": "rgba(255, 255, 255, 0.95)",
            "accent": "#15803d",
            "text": "#052e16",
            "text_muted": "#166534",
            "border": "1px solid #dcfce7",
            "glow": "0 10px 25px rgba(21, 128, 61, 0.12)",
            "btn_text": "#ffffff"
        },
        "cosmic": {
            "bg": "radial-gradient(circle at center, #0f172a 0%, #020617 100%)",
            "card_bg": "#1e1b4b",
            "accent": "#c084fc",
            "text": "#f8fafc",
            "text_muted": "#cbd5e1",
            "border": "1px solid rgba(192, 132, 252, 0.3)",
            "glow": "0 0 18px rgba(192, 132, 252, 0.4)",
            "btn_text": "#ffffff"
        }
    }

    return temas.get(opt.tema.lower(), temas["neon"])


def parse_trivia_markdown(contenido_md: str, personalizacion: OpcionesPersonalizacion | None = None) -> TriviaData:
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
    
    for i in range(1, len(bloques_preguntas), 2):
        num_pregunta = int(bloques_preguntas[i])
        cuerpo = bloques_preguntas[i + 1]

        lineas_cuerpo = cuerpo.strip().splitlines()
        texto_pregunta = ""
        opciones: dict[str, str] = {}
        correcta = "A"
        explicacion = ""

        for l in lineas_cuerpo:
            l_str = l.strip()
            if not l_str:
                continue

            if not texto_pregunta and not re.match(r"^[A-D]\)", l_str) and not l_str.lower().startswith("**respuesta"):
                texto_pregunta = re.sub(r"^\*+|\*+$", "", l_str).strip()
                continue

            match_op = re.match(r"^([A-D])\)\s*(.+)$", l_str)
            if match_op:
                opciones[match_op.group(1)] = match_op.group(2).strip()
                continue

            match_corr = re.match(r"^\*\*Respuesta\s+correcta[:\s]+([A-D])\*\*", l_str, re.IGNORECASE)
            if match_corr:
                correcta = match_corr.group(1).upper()
                continue

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

    opt = personalizacion or OpcionesPersonalizacion()
    if opt.barajar:
        random.shuffle(preguntas)
        for i, p in enumerate(preguntas, 1):
            p.numero = i

    return TriviaData(titulo=titulo, puntaje_minimo=puntaje_minimo, preguntas=preguntas, personalizacion=opt)


def generar_gift(trivia: TriviaData) -> str:
    """Genera exportación en formato GIFT para Moodle."""
    lineas = [f"// =============================================",
              f"// Cuestionario GIFT: {trivia.titulo}",
              f"// Generado por Aula Lista EDUCAI Trivia Engine",
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
    """Genera el reproductor interactivo autocontenido estilo Trivia con Modo Turno, Accesibilidad y Temas Neón."""
    opt = trivia.personalizacion
    cfg = obtener_configuracion_tema(opt)

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
      --bg: {cfg["bg"]};
      --card-bg: {cfg["card_bg"]};
      --accent: {cfg["accent"]};
      --text: {cfg["text"]};
      --text-muted: {cfg["text_muted"]};
      --border: {cfg["border"]};
      --glow: {cfg["glow"]};
      --btn-text: {cfg["btn_text"]};
      --success: #10b981;
      --error: #ef4444;
      --base-font-size: 16px;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg);
      background-attachment: fixed;
      color: var(--text);
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 1.5rem 1rem;
      font-size: var(--base-font-size);
      transition: background 0.3s, color 0.3s;
    }}

    /* Barra Superior de Accesibilidad y Modo Turno */
    .top-toolbar {{
      width: 100%;
      max-width: 780px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.85rem;
      padding: 0.5rem 1rem;
      background: rgba(0, 0, 0, 0.25);
      backdrop-filter: blur(8px);
      border-radius: 999px;
      border: 1px solid rgba(255, 255, 255, 0.1);
      font-size: 0.85rem;
    }}
    .toolbar-left, .toolbar-right {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .tool-btn {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: var(--text);
      padding: 0.25rem 0.65rem;
      border-radius: 999px;
      cursor: pointer;
      font-size: 0.8rem;
      font-weight: 600;
      transition: all 0.2s;
    }}
    .tool-btn:hover {{
      background: var(--accent);
      color: var(--btn-text);
      border-color: var(--accent);
    }}
    .timer-badge {{
      font-family: monospace;
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--accent);
      display: flex;
      align-items: center;
      gap: 0.3rem;
    }}

    /* Card Principal */
    .trivia-card {{
      background: var(--card-bg);
      border: var(--border);
      box-shadow: var(--glow);
      border-radius: 1.5rem;
      width: 100%;
      max-width: 780px;
      padding: 2.25rem 2rem;
      position: relative;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    /* Barra de Navegación por Turnos (Steps) */
    .turn-nav-bar {{
      display: flex;
      gap: 0.4rem;
      overflow-x: auto;
      padding: 0.4rem 0.2rem 1rem 0.2rem;
      margin-bottom: 1rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }}
    .turn-step {{
      flex: 0 0 auto;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.06);
      border: 1.5px solid rgba(255, 255, 255, 0.15);
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.2s;
    }}
    .turn-step:hover {{
      border-color: var(--accent);
      color: var(--text);
    }}
    .turn-step.active {{
      background: var(--accent);
      color: var(--btn-text);
      border-color: var(--accent);
      box-shadow: 0 0 10px var(--accent);
    }}
    .turn-step.answered {{
      background: rgba(16, 185, 129, 0.2);
      border-color: var(--success);
      color: var(--success);
    }}

    /* Header del Desafío */
    .header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.25rem;
    }}
    .tag {{
      display: inline-block;
      padding: 0.35rem 0.85rem;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--accent);
      color: var(--accent);
      border-radius: 999px;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .counter {{
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: 600;
    }}

    /* Pregunta */
    .question-title {{
      font-size: 1.25rem;
      line-height: 1.5;
      font-weight: 700;
      margin-bottom: 1.75rem;
      min-height: 3rem;
    }}

    /* Opciones */
    .options {{
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      margin-bottom: 1.75rem;
    }}
    .option-btn {{
      background: rgba(255, 255, 255, 0.04);
      border: 1.5px solid rgba(255, 255, 255, 0.12);
      border-radius: 0.85rem;
      padding: 1rem 1.25rem;
      color: var(--text);
      font-size: 1rem;
      text-align: left;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 1rem;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      width: 100%;
    }}
    .option-btn:hover:not(:disabled) {{
      background: rgba(255, 255, 255, 0.1);
      border-color: var(--accent);
      transform: translateX(4px);
    }}
    .opt-badge {{
      display: flex;
      align-items: center;
      justify-content: center;
      width: 2rem;
      height: 2rem;
      border-radius: 0.5rem;
      background: rgba(255, 255, 255, 0.08);
      font-weight: 700;
      font-size: 0.9rem;
      flex-shrink: 0;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }}
    .option-btn.selected {{
      border-color: var(--accent);
      background: rgba(255, 255, 255, 0.12);
    }}
    .option-btn.correct {{
      background: rgba(16, 185, 129, 0.2) !important;
      border-color: var(--success) !important;
      color: #86efac !important;
      font-weight: 700;
    }}
    .option-btn.wrong {{
      background: rgba(239, 68, 68, 0.2) !important;
      border-color: var(--error) !important;
      color: #fca5a5 !important;
      font-weight: 700;
    }}

    /* Feedback Box */
    .feedback-box {{
      border-radius: 0.85rem;
      padding: 1rem 1.25rem;
      font-size: 0.95rem;
      line-height: 1.5;
      display: none;
      margin-bottom: 1.5rem;
      animation: fadeIn 0.3s ease;
    }}
    .feedback-box.active {{
      display: block;
      background: rgba(0, 0, 0, 0.3);
      border-left: 4px solid var(--accent);
    }}

    /* Botonera Modo Turno (Anterior / Siguiente) */
    .turn-controls {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      margin-top: 1rem;
    }}
    .nav-btn {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: var(--text);
      padding: 0.75rem 1.5rem;
      border-radius: 999px;
      font-weight: 700;
      cursor: pointer;
      font-size: 0.95rem;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .nav-btn:hover:not(:disabled) {{
      background: rgba(255, 255, 255, 0.15);
      border-color: var(--accent);
    }}
    .nav-btn:disabled {{
      opacity: 0.35;
      cursor: not-allowed;
    }}
    .primary-btn {{
      background: var(--accent);
      color: var(--btn-text);
      border: none;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }}
    .primary-btn:hover:not(:disabled) {{
      filter: brightness(1.1);
      transform: translateY(-2px);
    }}

    /* Pantalla Final */
    .final-card {{
      display: none;
      text-align: center;
      padding: 2rem 1rem;
    }}
    .score-circle {{
      width: 130px;
      height: 130px;
      border-radius: 50%;
      margin: 1.5rem auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-size: 2.25rem;
      font-weight: 800;
      border: 4px solid var(--accent);
      box-shadow: var(--glow);
      background: rgba(0, 0, 0, 0.2);
    }}

    /* Modo Estudiante Alto Contraste */
    body.student-high-contrast {{
      background: #000000 !important;
      color: #ffffff !important;
    }}
    body.student-high-contrast .trivia-card {{
      background: #000000 !important;
      border: 3px solid #ffffff !important;
      box-shadow: none !important;
      color: #ffffff !important;
    }}
    body.student-high-contrast .option-btn {{
      background: #000000 !important;
      border: 2px solid #ffffff !important;
      color: #ffffff !important;
    }}
    body.student-high-contrast .option-btn:hover:not(:disabled) {{
      background: #ffff00 !important;
      color: #000000 !important;
      border-color: #ffff00 !important;
    }}
    body.student-high-contrast .nav-btn.primary-btn {{
      background: #ffff00 !important;
      color: #000000 !important;
      border: 2px solid #ffffff !important;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
  </style>
</head>
<body>

  <!-- Barra de Herramientas Superior: Accesibilidad & Temporizador -->
  <header class="top-toolbar">
    <div class="toolbar-left">
      <span style="font-weight:700;">🎮 Modo Turno</span>
      {f'<div class="timer-badge" id="timer-box">⏱️ <span id="timer-text">00:00</span></div>' if opt.tiempo_limite > 0 else ''}
    </div>
    <div class="toolbar-right">
      <button class="tool-btn" onclick="toggleFontSize(-1)" title="Reducir fuente">A-</button>
      <button class="tool-btn" onclick="toggleFontSize(0)" title="Fuente normal">A</button>
      <button class="tool-btn" onclick="toggleFontSize(1)" title="Aumentar fuente">A+</button>
      <button class="tool-btn" onclick="toggleHighContrast()" title="Alto Contraste WCAG">👁️ Contraste</button>
    </div>
  </header>

  <!-- Contenedor Principal de la Trivia -->
  <main class="trivia-card" id="main-container">
    
    <!-- Barra de Turnos / Pasos -->
    <nav class="turn-nav-bar" id="turn-nav-bar" aria-label="Navegación de turnos"></nav>

    <div id="game-container">
      <div class="header">
        <span class="tag">Desafío Gamificado</span>
        <span class="counter" id="lbl-contador">Turno 1 de {len(trivia.preguntas)}</span>
      </div>

      <h2 class="question-title" id="question-text">Cargando pregunta...</h2>

      <div class="options" id="options-container"></div>

      <div class="feedback-box" id="feedback-container"></div>

      <!-- Controles de Navegación por Turno -->
      <footer class="turn-controls">
        <button class="nav-btn" id="prev-btn" onclick="prevTurn()">← Anterior</button>
        <button class="nav-btn primary-btn" id="next-btn" onclick="nextTurn()">Siguiente →</button>
      </footer>
    </div>

    <!-- Pantalla Final de Resultados -->
    <section class="final-card" id="final-screen">
      <h2>Evaluación Finalizada</h2>
      <p style="color:var(--text-muted); margin-top:0.5rem;">Resultados transmitidos al libro de calificaciones del LMS.</p>

      <div class="score-circle">
        <span id="score-display">0%</span>
      </div>

      <p id="final-status-msg" style="font-size:1.15rem; font-weight:700; margin-bottom:1.5rem;"></p>

      <button class="nav-btn primary-btn" onclick="reiniciarTrivia()">🔄 Reintentar Desafío</button>
    </section>

  </main>

  <script>
    var PREGUNTAS = {preguntas_json};
    var PUNTAJE_MINIMO = {trivia.puntaje_minimo};
    var FEEDBACK_TIMING = "{opt.feedback_timing}";
    var TIEMPO_LIMITE_MIN = {opt.tiempo_limite};
    var currentIdx = 0;
    var respuestas = {{}}; // clave: idxPregunta, valor: {{ letra, esCorrecta }}
    var scormAPI = null;
    var timerInterval = null;
    var tiempoRestante = TIEMPO_LIMITE_MIN * 60;
    var fontStep = 0;

    // --- COMUNICACIÓN SCORM 1.2 ---
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

    // --- TEMPORIZADOR OPCIONAL ---
    function iniciarTemporizador() {{
      if (TIEMPO_LIMITE_MIN <= 0) return;
      var timerElem = document.getElementById("timer-text");
      timerInterval = setInterval(function() {{
        if (tiempoRestante <= 0) {{
          clearInterval(timerInterval);
          alert("⏱️ El tiempo límite ha expirado. Se enviarán tus respuestas actuales.");
          showFinalScreen();
          return;
        }}
        tiempoRestante--;
        var m = Math.floor(tiempoRestante / 60);
        var s = tiempoRestante % 60;
        timerElem.innerText = (m < 10 ? "0" + m : m) + ":" + (s < 10 ? "0" + s : s);
      }}, 1000);
    }}

    // --- ACCESIBILIDAD ---
    function toggleFontSize(direction) {{
      if (direction === 0) fontStep = 0;
      else fontStep = Math.max(-1, Math.min(2, fontStep + direction));
      var sizes = {{ "-1": "14px", "0": "16px", "1": "19px", "2": "22px" }};
      document.documentElement.style.setProperty("--base-font-size", sizes[String(fontStep)]);
    }}

    function toggleHighContrast() {{
      document.body.classList.toggle("student-high-contrast");
    }}

    // --- MODO TURNO: RENDERIZADO Y NAVEGACIÓN OPTIMIZADA ---
    var domCache = {{}};

    function initDomCache() {{
      domCache.lblContador = document.getElementById("lbl-contador");
      domCache.questionText = document.getElementById("question-text");
      domCache.optsContainer = document.getElementById("options-container");
      domCache.fbContainer = document.getElementById("feedback-container");
      domCache.prevBtn = document.getElementById("prev-btn");
      domCache.nextBtn = document.getElementById("next-btn");
      domCache.turnNavBar = document.getElementById("turn-nav-bar");
      domCache.gameContainer = document.getElementById("game-container");
      domCache.finalScreen = document.getElementById("final-screen");
      domCache.scoreDisplay = document.getElementById("score-display");
      domCache.finalStatusMsg = document.getElementById("final-status-msg");
    }}

    function initTurnNavBar() {{
      var bar = domCache.turnNavBar;
      bar.innerHTML = "";
      var frag = document.createDocumentFragment();
      PREGUNTAS.forEach(function(p, i) {{
        var btn = document.createElement("button");
        btn.id = "turn-step-" + i;
        btn.className = "turn-step" + (i === 0 ? " active" : "");
        btn.innerText = i + 1;
        btn.title = "Turno " + (i + 1);
        btn.onclick = function() {{
          currentIdx = i;
          renderTurn();
        }};
        frag.appendChild(btn);
      }});
      bar.appendChild(frag);
    }}

    function updateTurnNavBar() {{
      PREGUNTAS.forEach(function(p, i) {{
        var btn = document.getElementById("turn-step-" + i);
        if (btn) {{
          btn.className = "turn-step" + (i === currentIdx ? " active" : "") + (respuestas[i] ? " answered" : "");
        }}
      }});
    }}

    function renderTurn() {{
      var q = PREGUNTAS[currentIdx];
      var total = PREGUNTAS.length;

      domCache.lblContador.innerText = "Turno " + (currentIdx + 1) + " de " + total;
      domCache.questionText.innerText = q.texto;

      updateTurnNavBar();

      // Configurar botones de navegación por turno
      domCache.prevBtn.disabled = (currentIdx === 0);
      if (currentIdx === total - 1) {{
        domCache.nextBtn.innerText = "Finalizar Evaluación 🏆";
      }} else {{
        domCache.nextBtn.innerText = "Siguiente →";
      }}

      // Opciones
      var optsContainer = domCache.optsContainer;
      optsContainer.innerHTML = "";
      var frag = document.createDocumentFragment();

      var yaRespondida = respuestas.hasOwnProperty(currentIdx);
      var respGuardada = respuestas[currentIdx];

      q.opciones.forEach(function(opt) {{
        var btn = document.createElement("button");
        btn.className = "option-btn";
        btn.innerHTML = '<span class="opt-badge">' + opt.letra + '</span><span>' + opt.texto + '</span>';

        if (yaRespondida) {{
          if (FEEDBACK_TIMING === "immediate") {{
            btn.disabled = true;
            if (opt.letra === q.correcta) btn.classList.add("correct");
            else if (opt.letra === respGuardada.letra) btn.classList.add("wrong");
          }} else {{
            if (opt.letra === respGuardada.letra) btn.classList.add("selected");
          }}
        }}

        btn.onclick = function() {{ handleSelectOption(opt.letra, btn); }};
        frag.appendChild(btn);
      }});
      optsContainer.appendChild(frag);

      // Feedback
      var fb = domCache.fbContainer;
      if (yaRespondida && FEEDBACK_TIMING === "immediate") {{
        var esCorrecta = respGuardada.esCorrecta;
        fb.innerHTML = (esCorrecta ? "<strong>🎉 ¡Excelente!</strong> " : "<strong>❌ Respuesta incorrecta.</strong> ") +
                       (q.explicacion ? q.explicacion : ("La opción correcta es la " + q.correcta + "."));
        fb.classList.add("active");
        fb.style.display = "block";
      }} else {{
        fb.style.display = "none";
        fb.classList.remove("active");
      }}
    }}

    function handleSelectOption(letra, btnElem) {{
      var q = PREGUNTAS[currentIdx];
      var esCorrecta = (letra === q.correcta);

      respuestas[currentIdx] = {{ letra: letra, esCorrecta: esCorrecta }};
      renderTurn();
    }}

    function prevTurn() {{
      if (currentIdx > 0) {{
        currentIdx--;
        renderTurn();
      }}
    }}

    function nextTurn() {{
      if (currentIdx < PREGUNTAS.length - 1) {{
        currentIdx++;
        renderTurn();
      }} else {{
        showFinalScreen();
      }}
    }}

    function showFinalScreen() {{
      if (timerInterval) clearInterval(timerInterval);

      domCache.gameContainer.style.display = "none";
      domCache.turnNavBar.style.display = "none";
      domCache.finalScreen.style.display = "block";

      var total = PREGUNTAS.length;
      var aciertos = 0;
      for (var i = 0; i < total; i++) {{
        if (respuestas[i] && respuestas[i].esCorrecta) aciertos++;
      }}

      var porcentaje = Math.round((aciertos / total) * 100);
      var aprobado = porcentaje >= PUNTAJE_MINIMO;

      domCache.scoreDisplay.innerText = porcentaje + "%";
      if (aprobado) {{
        domCache.finalStatusMsg.innerHTML = "🏆 <strong>¡Felicitaciones!</strong> Has superado el desafío (Aciertos: " + aciertos + "/" + total + ").";
        domCache.finalStatusMsg.style.color = "var(--success)";
      }} else {{
        domCache.finalStatusMsg.innerHTML = "⚠️ <strong>No alcanzaste el puntaje mínimo de " + PUNTAJE_MINIMO + "%.</strong> (Aciertos: " + aciertos + "/" + total + "). ¡Repasa y vuelve a intentarlo!";
        domCache.finalStatusMsg.style.color = "var(--error)";
      }}

      finishSCORM(aprobado, porcentaje);
    }}

    function reiniciarTrivia() {{
      currentIdx = 0;
      respuestas = {{}};
      tiempoRestante = TIEMPO_LIMITE_MIN * 60;
      domCache.finalScreen.style.display = "none";
      domCache.gameContainer.style.display = "block";
      domCache.turnNavBar.style.display = "flex";
      initSCORM();
      iniciarTemporizador();
      initTurnNavBar();
      renderTurn();
    }}

    window.onload = function() {{
      initDomCache();
      initSCORM();
      iniciarTemporizador();
      initTurnNavBar();
      renderTurn();
    }};
  </script>
</body>
</html>
"""


def generar_manifest_scorm(trivia: TriviaData, identifier: str = "TRIVIA_SCORM") -> str:
    """Genera imsmanifest.xml estándar SCORM 1.2 delegando al generador unificado."""
    return generar_manifest_scorm_unificado(
        identifier=identifier,
        title=trivia.titulo,
        masteryscore=trivia.puntaje_minimo,
        default_href="index.html",
        generator_name="Aula Lista EDUCAI / ScormQuest Turbo Engine"
    )


def empaquetar_trivia_scorm(
    ruta_md: Path,
    salida_zip: Path | None = None,
    personalizacion: OpcionesPersonalizacion | None = None
) -> Path:
    """Lee el archivo markdown, genera el HTML interactivo con personalización y empaqueta en ZIP SCORM 1.2."""
    if not ruta_md.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {ruta_md}")

    contenido = ruta_md.read_text(encoding="utf-8")
    trivia = parse_trivia_markdown(contenido, personalizacion=personalizacion)

    if not trivia.preguntas:
        raise ValueError(f"No se detectaron preguntas válidas en {ruta_md}")

    if salida_zip is None:
        salida_zip = ruta_md.with_name(f"{ruta_md.stem}-SCORM.zip")

    html_content = generar_html_trivia(trivia)
    manifest_content = generar_manifest_scorm(trivia, identifier=ruta_md.stem)

    with zipfile.ZipFile(salida_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("imsmanifest.xml", manifest_content.encode("utf-8"))
        zf.writestr("index.html", html_content.encode("utf-8"))

    print(f"[OK] Paquete SCORM 1.2 generado exitosamente: {salida_zip}")
    print(f"   - Título: {trivia.titulo}")
    print(f"   - Preguntas: {len(trivia.preguntas)}")
    print(f"   - Modo Turno: {'Activo' if trivia.personalizacion.modo_turno else 'Inactivo'}")
    print(f"   - Tema Visual: {trivia.personalizacion.tema}")
    print(f"   - Puntaje Mínimo: {trivia.puntaje_minimo}%")
    return salida_zip


def ejecutar_modo_turbo(
    entrada: Path,
    salida_dir: Path | None = None,
    modo_turbo: int = 1
) -> list[Path]:
    """
    Ejecuta el Modo Turbo:
    - Modo Turbo 1 (1-Click Automático): Genera o empaqueta instantáneamente con presets optimizados:
      (10 preguntas intermedias, aprobación 60%, 30 min, barajado aleatorio, tema neón / alto contraste).
    - Modo Turbo 2 (Batch Processing): Procesa una carpeta entera de archivos y empaqueta todos en SCORM 1.2.
    """
    print("=" * 60)
    print(f"🚀 ACTIVANDO MODO TURBO {modo_turbo} (Aula Lista EDUCAI)")
    print("=" * 60)

    # Configuración estandarizada Turbo
    turbo_opts = OpcionesPersonalizacion(
        tema="neon",
        neon_primary="#0c071e",
        neon_accent="#ffd700",
        modo_turno=True,
        feedback_timing="immediate",
        tiempo_limite=30,  # 30 minutos
        barajar=True,
        modo_accesibilidad=True
    )

    salidas = []

    if modo_turbo == 2 or entrada.is_dir():
        archivos = list(entrada.glob("*.md")) if entrada.is_dir() else [entrada]
        out_dir = salida_dir or (entrada if entrada.is_dir() else entrada.parent)
        out_dir.mkdir(parents=True, exist_ok=True)

        for arch in archivos:
            if "trivia" in arch.stem.lower() or "evaluacion" in arch.stem.lower() or "cuestionario" in arch.stem.lower():
                destino = out_dir / f"{arch.stem}-SCORM.zip"
                try:
                    res = empaquetar_trivia_scorm(arch, salida_zip=destino, personalizacion=turbo_opts)
                    salidas.append(res)
                except Exception as e:
                    print(f"⚠️ Error procesando {arch.name}: {e}")
        print(f"🏁 Modo Turbo 2 finalizado. {len(salidas)} paquetes empaquetados.")
    else:
        # Modo Turbo 1 (archivo individual 1-click)
        if salida_dir:
            destino = salida_dir if salida_dir.suffix.lower() == ".zip" else (salida_dir / f"{entrada.stem}_Turbo-SCORM.zip")
        else:
            destino = entrada.with_name(f"{entrada.stem}_Turbo-SCORM.zip")
        res = empaquetar_trivia_scorm(entrada, salida_zip=destino, personalizacion=turbo_opts)
        salidas.append(res)
        print("🏁 Modo Turbo 1 completado con éxito 🚀")

    return salidas


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generador de paquetes SCORM 1.2 estilo Trivia con Modo Turno y Temas Neón")
    parser.add_argument("markdown", help="Ruta al archivo Markdown o directorio con las preguntas")
    parser.add_argument("-o", "--output", help="Ruta de salida para el archivo .zip o directorio", default=None)
    parser.add_argument("--tema", default="neon", choices=["neon", "corporate", "minimal", "high-contrast", "sunset", "forest", "cosmic"], help="Tema visual de la trivia")
    parser.add_argument("--neon-primary", default="#0c071e", help="Color primario en tema neón (hex)")
    parser.add_argument("--neon-accent", default="#ffd700", help="Color de acento en tema neón (hex)")
    parser.add_argument("--tiempo", type=int, default=0, help="Tiempo límite en minutos (0 = sin límite)")
    parser.add_argument("--feedback", default="immediate", choices=["immediate", "end"], help="Momento del feedback")
    parser.add_argument("--barajar", action="store_true", help="Barajar el orden de preguntas")
    parser.add_argument("--turbo", type=int, choices=[1, 2], nargs="?", const=1, help="Activar Modo Turbo (1: Automático 1-click, 2: Por lotes)")
    parser.add_argument("--exportar-gift", action="store_true", help="Generar también archivo GIFT para el banco de Moodle")
    args = parser.parse_args()

    input_path = Path(args.markdown)

    if args.turbo:
        out_path = Path(args.output) if args.output else None
        ejecutar_modo_turbo(input_path, salida_dir=out_path, modo_turbo=args.turbo)
        sys.exit(0)

    salida = Path(args.output) if args.output else None
    opts = OpcionesPersonalizacion(
        tema=args.tema,
        neon_primary=args.neon_primary,
        neon_accent=args.neon_accent,
        modo_turno=True,
        feedback_timing=args.feedback,
        tiempo_limite=args.tiempo,
        barajar=args.barajar,
        modo_accesibilidad=True
    )

    if args.exportar_gift:
        trivia_obj = parse_trivia_markdown(input_path.read_text(encoding="utf-8"), personalizacion=opts)
        gift_file = input_path.with_suffix(".gift.txt")
        gift_file.write_text(generar_gift(trivia_obj), encoding="utf-8")
        print(f"[OK] Archivo GIFT de Moodle generado en: {gift_file}")

    empaquetar_trivia_scorm(input_path, salida, personalizacion=opts)
