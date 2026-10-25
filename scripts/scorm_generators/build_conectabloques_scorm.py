"""
build_conectabloques_scorm.py
==============================
Generador de paquetes SCORM 1.2 independientes para la actividad Conectabloques.
Incluye:
- Selección de múltiples estilos visuales: modern-mint (default), retro-arcade, neon-synthwave, chalkboard, warm-autumn.
- Temporizador regresivo de 20 minutos por defecto.
- Máximo de intentos: N * 2.
- Efectos de sonido sintéticos y música ambiental opcional en Web Audio API (sin archivos externos).
- Comunicación estricta SCORM 1.2 (LMSInitialize, cmi.core.score.raw, cmi.core.lesson_status passed/failed, LMSCommit, LMSFinish).
- Paquete limpio ZIP con imsmanifest.xml e index.html en la raíz.
"""

from __future__ import annotations

import argparse
import html
import json
import re
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


THEMES = {
    "modern-mint": {
        "name": "Modern Mint",
        "bg_style": "background: linear-gradient(135deg, #0f172a 0%, #064e3b 100%); color: #f8fafc; font-family: system-ui, sans-serif;",
        "card_style": "background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 1rem; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.5); backdrop-filter: blur(12px);",
        "block_base": "background: rgba(30, 41, 59, 0.9); border: 2px solid #334155; color: #f1f5f9; border-radius: 0.75rem;",
        "block_hover": "background: rgba(16, 185, 129, 0.15); border-color: #10b981;",
        "block_selected": "background: #10b981; border-color: #34d399; color: #022c22; font-weight: bold; transform: scale(1.02);",
        "block_matched": "border-color: #1e293b; background: rgba(15, 23, 42, 0.6); color: #64748b; opacity: 0.45; text-decoration: line-through; pointer-events: none;",
        "accent_color": "#10b981",
        "header_badge": "background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4);",
        "audio_wave": "sine",
        "notes": [261.63, 329.63, 392.00, 523.25, 440.00]
    },
    "retro-arcade": {
        "name": "Retro Arcade",
        "bg_style": "background-color: #000000; color: #facc15; font-family: 'Courier New', Courier, monospace;",
        "card_style": "background: #0d0d0d; border: 4px solid #eab308; border-radius: 0; box-shadow: 8px 8px 0px #a16207;",
        "block_base": "background: #171717; border: 3px solid #ca8a04; color: #facc15; border-radius: 0; font-weight: bold;",
        "block_hover": "background: #262626; border-color: #facc15;",
        "block_selected": "background: #facc15; border-color: #ffffff; color: #000000; font-weight: 900; transform: scale(1.02);",
        "block_matched": "border-color: #404040; background: #171717; color: #525252; opacity: 0.4; text-decoration: line-through; pointer-events: none;",
        "accent_color": "#eab308",
        "header_badge": "background: #ca8a04; color: #000000; border: 2px solid #facc15;",
        "audio_wave": "square",
        "notes": [261.63, 329.63, 392.00, 523.25, 440.00, 523.25, 349.23, 440.00]
    },
    "neon-synthwave": {
        "name": "Neon Synthwave",
        "bg_style": "background: linear-gradient(135deg, #18052e 0%, #3b0764 100%); color: #fdf4ff; font-family: system-ui, sans-serif;",
        "card_style": "background: rgba(30, 10, 60, 0.85); border: 2px solid #d946ef; border-radius: 1rem; box-shadow: 0 0 25px rgba(217, 70, 239, 0.3); backdrop-filter: blur(12px);",
        "block_base": "background: rgba(59, 7, 100, 0.8); border: 2px solid #86198f; color: #f5d0fe; border-radius: 0.75rem;",
        "block_hover": "background: rgba(217, 70, 239, 0.2); border-color: #f0abfc;",
        "block_selected": "background: #d946ef; border-color: #fdf4ff; color: #ffffff; font-weight: bold; transform: scale(1.02); box-shadow: 0 0 15px #d946ef;",
        "block_matched": "border-color: #4a044e; background: rgba(30, 10, 60, 0.5); color: #701a75; opacity: 0.45; text-decoration: line-through; pointer-events: none;",
        "accent_color": "#d946ef",
        "header_badge": "background: rgba(217, 70, 239, 0.25); color: #f5d0fe; border: 1px solid #d946ef;",
        "audio_wave": "sawtooth",
        "notes": [110.00, 220.00, 87.31, 174.61, 130.81, 261.63, 98.00, 196.00]
    },
    "chalkboard": {
        "name": "Chalkboard",
        "bg_style": "background-color: #1e3a2b; color: #f1f5f9; font-family: 'Comic Sans MS', cursive, sans-serif;",
        "card_style": "background: #14281e; border: 6px solid #854d0e; border-radius: 0.5rem; box-shadow: inset 0 0 40px rgba(0,0,0,0.6);",
        "block_base": "background: rgba(255, 255, 255, 0.05); border: 2px dashed rgba(255, 255, 255, 0.3); color: #e2e8f0; border-radius: 0.5rem;",
        "block_hover": "background: rgba(255, 255, 255, 0.15); border-color: #ffffff;",
        "block_selected": "background: #ffffff; border-color: #ffffff; color: #1e3a2b; font-weight: bold; transform: scale(1.02);",
        "block_matched": "border-color: #274736; background: transparent; color: #476655; opacity: 0.4; text-decoration: line-through; pointer-events: none;",
        "accent_color": "#fef08a",
        "header_badge": "background: rgba(255, 255, 255, 0.1); color: #fef08a; border: 1px dashed #fef08a;",
        "audio_wave": "triangle",
        "notes": [329.63, 392.00, 440.00, 523.25, 587.33, 659.25]
    },
    "warm-autumn": {
        "name": "Warm Autumn",
        "bg_style": "background: linear-gradient(135deg, #2a1b18 0%, #451a03 100%); color: #fef3c7; font-family: system-ui, sans-serif;",
        "card_style": "background: rgba(42, 27, 24, 0.9); border: 2px solid #b45309; border-radius: 1rem; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.5);",
        "block_base": "background: rgba(69, 26, 3, 0.8); border: 2px solid #78350f; color: #fde68a; border-radius: 0.75rem;",
        "block_hover": "background: rgba(180, 83, 9, 0.25); border-color: #f59e0b;",
        "block_selected": "background: #d97706; border-color: #fef3c7; color: #ffffff; font-weight: bold; transform: scale(1.02);",
        "block_matched": "border-color: #3e1f17; background: rgba(30, 15, 12, 0.5); color: #92400e; opacity: 0.45; text-decoration: line-through; pointer-events: none;",
        "accent_color": "#f59e0b",
        "header_badge": "background: rgba(217, 119, 6, 0.2); color: #fde68a; border: 1px solid #f59e0b;",
        "audio_wave": "sine",
        "notes": [196.00, 293.66, 329.63, 392.00, 440.00, 493.88]
    }
}


@dataclass
class ConceptoPar:
    id: str
    term: str
    definition: str
    source_snippet: str = ""


@dataclass
class ConectabloquesData:
    titulo: str
    puntaje_minimo: int = 70
    tiempo_limite_minutos: int = 20
    intentos_maximos: int | None = None
    dificultad: str = "intermedio"
    tema: str = "modern-mint"
    conceptos: list[ConceptoPar] = field(default_factory=list)


def parse_conectabloques_markdown(md_texto: str) -> ConectabloquesData:
    """Parsea el markdown estructurado de Conectabloques."""
    titulo = "Actividad Conectabloques"
    puntaje_minimo = 70
    tiempo_limite = 20
    intentos_maximos = None
    dificultad = "intermedio"
    tema = "modern-mint"
    conceptos: list[ConceptoPar] = []

    # Extraer encabezados
    for linea in md_texto.splitlines():
        l = linea.strip()
        if l.startswith("# Actividad: Conectabloques"):
            partes = l.split("-", 1)
            if len(partes) > 1:
                titulo = partes[1].strip()
        elif l.lower().startswith("puntaje mínimo:") or l.lower().startswith("puntaje minimo:"):
            m = re.search(r"(\d+)", l)
            if m:
                puntaje_minimo = int(m.group(1))
        elif l.lower().startswith("tiempo límite:") or l.lower().startswith("tiempo limite:"):
            m = re.search(r"(\d+)", l)
            if m:
                tiempo_limite = int(m.group(1))
        elif l.lower().startswith("intentos máximos:") or l.lower().startswith("intentos maximos:"):
            m = re.search(r"(\d+)", l)
            if m:
                intentos_maximos = int(m.group(1))
        elif l.lower().startswith("nivel de dificultad:"):
            dificultad = l.split(":", 1)[1].strip().lower()
        elif l.lower().startswith("tema visual:"):
            tema_val = l.split(":", 1)[1].strip().lower()
            if tema_val in THEMES:
                tema = tema_val

    # Parsear bloques de términos (## Término: <nombre>)
    bloques = re.split(r"\n##\s+T[ée]rmino\s*:\s*", "\n" + md_texto)
    for idx, b in enumerate(bloques[1:], 1):
        lineas_b = b.strip().splitlines()
        term = lineas_b[0].strip()
        definicion = ""
        origen = ""
        for lb in lineas_b[1:]:
            lbs = lb.strip()
            if lbs.lower().startswith("- definición:") or lbs.lower().startswith("- definicion:"):
                definicion = lbs.split(":", 1)[1].strip()
            elif lbs.lower().startswith("- origen:"):
                origen = lbs.split(":", 1)[1].strip()
        if term and definicion:
            conceptos.append(ConceptoPar(id=f"c{idx}", term=term, definition=definicion, source_snippet=origen))

    return ConectabloquesData(
        titulo=titulo,
        puntaje_minimo=puntaje_minimo,
        tiempo_limite_minutos=tiempo_limite,
        intentos_maximos=intentos_maximos,
        dificultad=dificultad,
        tema=tema,
        conceptos=conceptos
    )


def generar_html_conectabloques(data: ConectabloquesData) -> str:
    """Genera el código HTML interactivo autónomo con estilos, audio sintético y API SCORM 1.2."""
    tema_cfg = THEMES.get(data.tema, THEMES["modern-mint"])
    conceptos_json = json.dumps([
        {"id": c.id, "term": c.term, "definition": c.definition}
        for c in data.conceptos
    ], ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(data.titulo)}</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      {tema_cfg['bg_style']}
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 1.5rem;
    }}
    .game-card {{
      {tema_cfg['card_style']}
      width: 100%;
      max-width: 900px;
      padding: 2rem;
      position: relative;
    }}
    .game-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.5rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 1rem;
    }}
    .badge {{
      {tema_cfg['header_badge']}
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: bold;
    }}
    .stats-bar {{
      display: flex;
      gap: 1.5rem;
      align-items: center;
    }}
    .stat-item {{
      text-align: center;
    }}
    .stat-label {{
      font-size: 0.75rem;
      opacity: 0.7;
      text-transform: uppercase;
      letter-spacing: 1px;
    }}
    .stat-val {{
      font-size: 1.25rem;
      font-weight: bold;
      color: {tema_cfg['accent_color']};
    }}
    .instructions {{
      margin-bottom: 1.5rem;
      font-size: 0.95rem;
      opacity: 0.85;
      text-align: center;
    }}
    .columns-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
    }}
    @media (max-width: 640px) {{
      .columns-grid {{ grid-template-columns: 1fr; }}
    }}
    .column-title {{
      font-size: 0.9rem;
      font-weight: bold;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      margin-bottom: 0.75rem;
      opacity: 0.8;
      text-align: center;
    }}
    .blocks-container {{
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }}
    .block-item {{
      {tema_cfg['block_base']}
      padding: 1rem 1.25rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      min-height: 64px;
      user-select: none;
      transition: all 0.2s ease;
      font-size: 0.95rem;
      line-height: 1.4;
    }}
    .block-item:hover:not(.matched) {{
      {tema_cfg['block_hover']}
      transform: translateY(-2px);
    }}
    .block-item.selected {{
      {tema_cfg['block_selected']}
    }}
    .block-item.matched {{
      {tema_cfg['block_matched']}
    }}
    .audio-controls {{
      margin-top: 1.5rem;
      display: flex;
      justify-content: flex-end;
      gap: 0.75rem;
    }}
    .btn-audio {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: inherit;
      padding: 0.4rem 0.8rem;
      border-radius: 0.5rem;
      font-size: 0.8rem;
      cursor: pointer;
      transition: background 0.2s ease;
    }}
    .btn-audio:hover {{
      background: rgba(255, 255, 255, 0.2);
    }}
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.8);
      display: none;
      justify-content: center;
      align-items: center;
      z-index: 1000;
      backdrop-filter: blur(8px);
    }}
    .modal-card {{
      {tema_cfg['card_style']}
      max-width: 500px;
      width: 90%;
      text-align: center;
      padding: 2.5rem 2rem;
    }}
    .modal-score {{
      font-size: 3.5rem;
      font-weight: 800;
      color: {tema_cfg['accent_color']};
      margin: 1rem 0;
    }}
  </style>
</head>
<body>
  <div class="game-card">
    <div class="game-header">
      <span class="badge">Conectabloques SCORM</span>
      <div class="stats-bar">
        <div class="stat-item">
          <div class="stat-label">Tiempo</div>
          <div class="stat-val" id="timer-counter">20:00</div>
        </div>
        <div class="stat-item">
          <div class="stat-label">Aciertos</div>
          <div class="stat-val" id="matched-counter">0 / {len(data.conceptos)}</div>
        </div>
        <div class="stat-item">
          <div class="stat-label">Intentos</div>
          <div class="stat-val" id="attempts-counter">0 / {len(data.conceptos) * 2}</div>
        </div>
        <div class="stat-item">
          <div class="stat-label">Puntuación</div>
          <div class="stat-val" id="score-counter">0%</div>
        </div>
      </div>
    </div>

    <div class="instructions">
      Asocia cada <strong>término</strong> de la izquierda con su <strong>definición correcta</strong> en la derecha.
    </div>

    <div class="columns-grid">
      <div>
        <div class="column-title">Términos</div>
        <div class="blocks-container" id="terms-column"></div>
      </div>
      <div>
        <div class="column-title">Definiciones</div>
        <div class="blocks-container" id="definitions-column"></div>
      </div>
    </div>

    <div class="audio-controls">
      <button class="btn-audio" id="btn-music" onclick="toggleMusic()">🎵 Música de Fondo: OFF</button>
      <button class="btn-audio" id="btn-sfx" onclick="toggleSfx()">🔊 Efectos: ON</button>
    </div>
  </div>

  <div class="modal-overlay" id="end-modal">
    <div class="modal-card">
      <h2 id="modal-title" style="font-size: 2rem; margin-bottom: 0.5rem;">¡Actividad Finalizada!</h2>
      <p id="modal-desc" style="opacity: 0.85;">Has emparejado todos los conceptos clave de la unidad.</p>
      <div class="modal-score" id="final-score">100%</div>
      <p id="modal-status-msg" style="margin-bottom: 1.75rem; font-size: 1.1rem;"></p>
      <button class="block-item" style="margin: 0 auto; width: 100%; cursor: pointer;" onclick="reiniciarJuego()">Reintentar Actividad</button>
    </div>
  </div>

  <script>
    var ORIGINAL_CONCEPTS = {conceptos_json};
    var PUNTAJE_MINIMO = {data.puntaje_minimo};
    var TIEMPO_LIMITE_SEGUNDOS = {data.tiempo_limite_minutos * 60};
    var MAX_INTENTOS = {data.intentos_maximos or (len(data.conceptos) * 2)};
    var DIFICULTAD = "{data.dificultad}";
    var THEME_NOTES = {json.dumps(tema_cfg['notes'])};
    var THEME_WAVE = "{tema_cfg['audio_wave']}";

    var selectedTermId = null;
    var selectedDefId = null;
    var matchedPairs = new Set();
    var attempts = 0;
    var timerSeconds = TIEMPO_LIMITE_SEGUNDOS;
    var timerInterval = null;
    var isGameOver = false;

    // --- AUDIO CONTEXT SINTETIZADOR ---
    var audioCtx = null;
    var musicGain = null;
    var isMusicPlaying = false;
    var sfxEnabled = true;

    function getAudioContext() {{
      if (!audioCtx) {{
        var AudioClass = window.AudioContext || window.webkitAudioContext;
        if (AudioClass) audioCtx = new AudioClass();
      }}
      if (audioCtx && audioCtx.state === 'suspended') {{
        audioCtx.resume();
      }}
      return audioCtx;
    }}

    function playSfx(type) {{
      if (!sfxEnabled) return;
      var ctx = getAudioContext();
      if (!ctx) return;
      var now = ctx.currentTime;
      var osc = ctx.createOscillator();
      var gain = ctx.createGain();
      osc.connect(gain);
      gain.connect(ctx.destination);

      // Auto-desconexión para evitar fugas de memoria en Web Audio API
      osc.onended = function() {{
        try {{ osc.disconnect(); gain.disconnect(); }} catch (e) {{}}
      }};

      if (type === 'select') {{
        osc.frequency.setValueAtTime(440, now);
        osc.frequency.exponentialRampToValueAtTime(880, now + 0.08);
        gain.gain.setValueAtTime(0.08, now);
        gain.gain.linearRampToValueAtTime(0.01, now + 0.08);
        osc.start(now);
        osc.stop(now + 0.08);
      }} else if (type === 'correct') {{
        osc.type = THEME_WAVE;
        osc.frequency.setValueAtTime(523.25, now);
        osc.frequency.setValueAtTime(659.25, now + 0.1);
        osc.frequency.setValueAtTime(783.99, now + 0.2);
        gain.gain.setValueAtTime(0.12, now);
        gain.gain.linearRampToValueAtTime(0.01, now + 0.35);
        osc.start(now);
        osc.stop(now + 0.35);
      }} else if (type === 'incorrect') {{
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(220, now);
        osc.frequency.linearRampToValueAtTime(110, now + 0.25);
        gain.gain.setValueAtTime(0.15, now);
        gain.gain.linearRampToValueAtTime(0.01, now + 0.25);
        osc.start(now);
        osc.stop(now + 0.25);
      }} else if (type === 'win') {{
        [523.25, 659.25, 783.99, 1046.50].forEach(function(f, i) {{
          var o = ctx.createOscillator();
          var g = ctx.createGain();
          o.connect(g);
          g.connect(ctx.destination);
          o.onended = function() {{
            try {{ o.disconnect(); g.disconnect(); }} catch(e) {{}}
          }};
          o.frequency.setValueAtTime(f, now + i * 0.12);
          g.gain.setValueAtTime(0.12, now + i * 0.12);
          g.gain.linearRampToValueAtTime(0.01, now + i * 0.12 + 0.3);
          o.start(now + i * 0.12);
          o.stop(now + i * 0.12 + 0.3);
        }});
      }}
    }}

    function toggleSfx() {{
      sfxEnabled = !sfxEnabled;
      document.getElementById("btn-sfx").innerText = "🔊 Efectos: " + (sfxEnabled ? "ON" : "OFF");
    }}

    var ambientStep = 0;
    var ambientTimer = null;

    function playAmbientNote() {{
      if (!isMusicPlaying) return;
      var ctx = getAudioContext();
      if (!ctx) return;
      var osc = ctx.createOscillator();
      var gain = ctx.createGain();
      osc.type = THEME_WAVE;
      var note = THEME_NOTES[ambientStep % THEME_NOTES.length];
      osc.frequency.setValueAtTime(note, ctx.currentTime);
      gain.gain.setValueAtTime(0.02, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.8);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.onended = function() {{
        try {{ osc.disconnect(); gain.disconnect(); }} catch (e) {{}}
      }};
      osc.start();
      osc.stop(ctx.currentTime + 0.8);
      ambientStep++;
      ambientTimer = setTimeout(playAmbientNote, 900);
    }}

    function toggleMusic() {{
      isMusicPlaying = !isMusicPlaying;
      if (isMusicPlaying) {{
        document.getElementById("btn-music").innerText = "🎵 Música de Fondo: ON";
        playAmbientNote();
      }} else {{
        document.getElementById("btn-music").innerText = "🎵 Música de Fondo: OFF";
        if (ambientTimer) clearTimeout(ambientTimer);
      }}
    }}

    // --- COMUNICACIÓN SCORM 1.2 ---
    var scormAPI = null;
    function findAPI(win) {{
      var attempts = 0;
      while (win && !win.API && win.parent && win.parent !== win && attempts < 10) {{
        attempts++;
        win = win.parent;
      }}
      return win ? win.API : null;
    }}

    function initSCORM() {{
      scormAPI = findAPI(window);
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

    function shuffle(array) {{
      var copy = array.slice();
      for (var i = copy.length - 1; i > 0; i--) {{
        var j = Math.floor(Math.random() * (i + 1));
        var tmp = copy[i];
        copy[i] = copy[j];
        copy[j] = tmp;
      }}
      return copy;
    }}

    function startTimer() {{
      if (timerInterval) clearInterval(timerInterval);
      timerInterval = setInterval(function() {{
        if (isGameOver) return;
        timerSeconds--;
        var mins = Math.floor(timerSeconds / 60);
        var secs = timerSeconds % 60;
        document.getElementById("timer-counter").innerText =
          (mins < 10 ? "0" : "") + mins + ":" + (secs < 10 ? "0" : "") + secs;

        if (timerSeconds <= 0) {{
          clearInterval(timerInterval);
          finalizarJuego("timeout");
        }}
      }}, 1000);
    }}

    function renderBoard() {{
      var termsContainer = document.getElementById("terms-column");
      var defsContainer = document.getElementById("definitions-column");
      termsContainer.innerHTML = "";
      defsContainer.innerHTML = "";

      var shuffledTerms = shuffle(ORIGINAL_CONCEPTS);
      var shuffledDefs = shuffle(ORIGINAL_CONCEPTS);

      var termsFrag = document.createDocumentFragment();
      shuffledTerms.forEach(function(c) {{
        var div = document.createElement("div");
        div.className = "block-item";
        div.id = "term-" + c.id;
        div.innerText = c.term;
        div.onclick = function() {{ handleSelectTerm(c.id); }};
        termsFrag.appendChild(div);
      }});
      termsContainer.appendChild(termsFrag);

      var defsFrag = document.createDocumentFragment();
      shuffledDefs.forEach(function(c) {{
        var div = document.createElement("div");
        div.className = "block-item";
        div.id = "def-" + c.id;
        div.innerText = c.definition;
        div.onclick = function() {{ handleSelectDef(c.id); }};
        defsFrag.appendChild(div);
      }});
      defsContainer.appendChild(defsFrag);
    }}

    function handleSelectTerm(id) {{
      if (matchedPairs.has(id) || isGameOver) return;
      playSfx('select');
      if (selectedTermId) {{
        var prev = document.getElementById("term-" + selectedTermId);
        if (prev) prev.classList.remove("selected");
      }}
      selectedTermId = id;
      var el = document.getElementById("term-" + id);
      if (el) el.classList.add("selected");
      verificarCoincidencia();
    }}

    function handleSelectDef(id) {{
      if (matchedPairs.has(id) || isGameOver) return;
      playSfx('select');
      if (selectedDefId) {{
        var prev = document.getElementById("def-" + selectedDefId);
        if (prev) prev.classList.remove("selected");
      }}
      selectedDefId = id;
      var el = document.getElementById("def-" + id);
      if (el) el.classList.add("selected");
      verificarCoincidencia();
    }}

    function verificarCoincidencia() {{
      if (!selectedTermId || !selectedDefId || isGameOver) return;
      attempts++;
      document.getElementById("attempts-counter").innerText = attempts + " / " + MAX_INTENTOS;

      var termEl = document.getElementById("term-" + selectedTermId);
      var defEl = document.getElementById("def-" + selectedDefId);

      if (selectedTermId === selectedDefId) {{
        // ACIERTO
        playSfx('correct');
        matchedPairs.add(selectedTermId);
        termEl.classList.remove("selected");
        defEl.classList.remove("selected");
        termEl.classList.add("matched");
        defEl.classList.add("matched");

        var aciertos = matchedPairs.size;
        var total = ORIGINAL_CONCEPTS.length;
        document.getElementById("matched-counter").innerText = aciertos + " / " + total;
        var currentScore = Math.round((aciertos / total) * 100);
        document.getElementById("score-counter").innerText = currentScore + "%";

        selectedTermId = null;
        selectedDefId = null;

        if (aciertos === total) {{
          finalizarJuego("win");
        }} else if (attempts >= MAX_INTENTOS) {{
          finalizarJuego("attempts");
        }}
      }} else {{
        // ERROR
        playSfx('incorrect');
        var tId = selectedTermId;
        var dId = selectedDefId;
        setTimeout(function() {{
          var t = document.getElementById("term-" + tId);
          var d = document.getElementById("def-" + dId);
          if (t) t.classList.remove("selected");
          if (d) d.classList.remove("selected");
        }}, 400);

        selectedTermId = null;
        selectedDefId = null;

        if (attempts >= MAX_INTENTOS) {{
          finalizarJuego("attempts");
        }}
      }}
    }}

    function finalizarJuego(motivo) {{
      isGameOver = true;
      if (timerInterval) clearInterval(timerInterval);
      if (ambientTimer) clearTimeout(ambientTimer);

      var total = ORIGINAL_CONCEPTS.length;
      var aciertos = matchedPairs.size;
      var porcentaje = Math.round((aciertos / total) * 100);
      var aprobado = (porcentaje >= PUNTAJE_MINIMO);

      var modal = document.getElementById("end-modal");
      var title = document.getElementById("modal-title");
      var desc = document.getElementById("modal-desc");
      var score = document.getElementById("final-score");
      var statusMsg = document.getElementById("modal-status-msg");

      score.innerText = porcentaje + "%";

      if (motivo === "win") {{
        playSfx('win');
        title.innerText = "🏆 ¡Felicitaciones!";
        desc.innerText = "Has emparejado todos los conceptos de la unidad exitosamente.";
        statusMsg.innerText = "Estado: APROBADO en el aula Moodle (" + aciertos + "/" + total + " pares).";
        statusMsg.style.color = "{tema_cfg['accent_color']}";
      }} else if (motivo === "timeout") {{
        title.innerText = "⏰ Tiempo Agotado";
        desc.innerText = "El tiempo de 20 minutos ha finalizado.";
        statusMsg.innerText = aprobado ? "Aprobaste con lo completado." : "No alcanzaste el mínimo aprobatorio de " + PUNTAJE_MINIMO + "%.";
        statusMsg.style.color = aprobado ? "{tema_cfg['accent_color']}" : "#ef4444";
      }} else {{
        title.innerText = "⚠️ Límite de Intentos Alcanzado";
        desc.innerText = "Has superado el número máximo de intentos permitidos.";
        statusMsg.innerText = aprobado ? "Aprobaste con los pares alcanzados." : "Repasa las lecturas y vuelve a intentarlo.";
        statusMsg.style.color = aprobado ? "{tema_cfg['accent_color']}" : "#ef4444";
      }}

      modal.style.display = "flex";
      finishSCORM(aprobado, porcentaje);
    }}

    function reiniciarJuego() {{
      matchedPairs.clear();
      attempts = 0;
      selectedTermId = null;
      selectedDefId = null;
      isGameOver = false;
      timerSeconds = TIEMPO_LIMITE_SEGUNDOS;

      document.getElementById("matched-counter").innerText = "0 / " + ORIGINAL_CONCEPTS.length;
      document.getElementById("attempts-counter").innerText = "0 / " + MAX_INTENTOS;
      document.getElementById("score-counter").innerText = "0%";
      document.getElementById("end-modal").style.display = "none";

      initSCORM();
      renderBoard();
      startTimer();
    }}

    window.onload = function() {{
      initSCORM();
      renderBoard();
      startTimer();
    }};
  </script>
</body>
</html>
"""


def generar_manifest_scorm_conectabloques(data: ConectabloquesData, identifier: str = "CONECTABLOQUES_SCORM") -> str:
    """Construye imsmanifest.xml estándar SCORM 1.2 delegando al generador unificado."""
    return generar_manifest_scorm_unificado(
        identifier=identifier,
        title=data.titulo,
        masteryscore=data.puntaje_minimo,
        default_href="index.html",
        generator_name="Aula Lista EDUCAI / Conectabloques Builder"
    )


def empaquetar_conectabloques_scorm(ruta_md: Path, salida_zip: Path | None = None, tema: str | None = None) -> Path:
    """Empaqueta la actividad Conectabloques en un archivo .zip SCORM 1.2 independiente."""
    if not ruta_md.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {ruta_md}")

    md_texto = ruta_md.read_text(encoding="utf-8")
    data = parse_conectabloques_markdown(md_texto)

    if tema and tema in THEMES:
        data.tema = tema

    if not data.conceptos:
        raise ValueError(f"No se encontraron bloques conceptuales válidos en {ruta_md}")

    if salida_zip is None:
        salida_zip = ruta_md.with_name(f"{ruta_md.stem}-SCORM.zip")

    html_content = generar_html_conectabloques(data)
    manifest_content = generar_manifest_scorm_conectabloques(data, identifier=ruta_md.stem)

    with zipfile.ZipFile(salida_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("imsmanifest.xml", manifest_content.encode("utf-8"))
        zf.writestr("index.html", html_content.encode("utf-8"))

    print(f"[OK] Paquete Conectabloques SCORM 1.2 generado exitosamente: {salida_zip}")
    print(f"   - Titulo: {data.titulo}")
    print(f"   - Conceptos: {len(data.conceptos)}")
    print(f"   - Tema visual: {data.tema} ({THEMES[data.tema]['name']})")
    print(f"   - Tiempo limite: {data.tiempo_limite_minutos} minutos")
    print(f"   - Puntaje minimo: {data.puntaje_minimo}%")
    return salida_zip


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Empaquetador SCORM 1.2 independiente de Conectabloques")
    parser.add_argument("markdown", help="Ruta al archivo Markdown de conectabloques")
    parser.add_argument("-o", "--output", help="Ruta del archivo ZIP resultante", default=None)
    parser.add_argument("--theme", choices=list(THEMES.keys()), default=None, help="Tema visual a aplicar")
    args = parser.parse_args()

    salida = Path(args.output) if args.output else None
    empaquetar_conectabloques_scorm(Path(args.markdown), salida, tema=args.theme)
