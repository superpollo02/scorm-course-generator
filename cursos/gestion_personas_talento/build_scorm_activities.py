import json
import zipfile
from pathlib import Path

BASE_DIR = Path(r"c:\Users\mfischer\Documents\antigravitiy proyectos\aula nueva con moodle\cursos\gestion_personas_talento")
SCORM_DIR = BASE_DIR / "scorm"
SCORM_DIR.mkdir(parents=True, exist_ok=True)

SCORM_API_JS = """// SCORM 1.2 API Wrapper
var scorm = {
    api: null,
    findAPI: function(win) {
        var attempts = 0;
        while ((win.API == null) && (win.parent != null) && (win.parent != win)) {
            attempts++;
            if (attempts > 10) return null;
            win = win.parent;
        }
        return win.API;
    },
    getAPI: function() {
        if (this.api) return this.api;
        var api = this.findAPI(window);
        if (!api && window.opener && window.opener != window) {
            api = this.findAPI(window.opener);
        }
        this.api = api;
        return api;
    },
    init: function() {
        var api = this.getAPI();
        if (api) api.LMSInitialize("");
    },
    complete: function(score) {
        var api = this.getAPI();
        if (api) {
            if (typeof score === 'number') {
                api.LMSSetValue("cmi.core.score.raw", String(Math.round(score)));
                api.LMSSetValue("cmi.core.score.min", "0");
                api.LMSSetValue("cmi.core.score.max", "100");
                api.LMSSetValue("cmi.core.lesson_status", score >= 70 ? "passed" : "completed");
            } else {
                api.LMSSetValue("cmi.core.lesson_status", "completed");
            }
            api.LMSCommit("");
        }
    }
};
window.addEventListener("load", function() { scorm.init(); });
"""

def create_manifest(identifier, title):
    return f"""<?xml version="1.0" standalone="no" ?>
<manifest identifier="{identifier}" version="1.0"
          xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
          xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd
                              http://www.imsglobal.org/xsd/imsmd_rootv1p2p1 imsmd_rootv1p2p1.xsd
                              http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
  </metadata>
  <organizations default="ORG-1">
    <organization identifier="ORG-1">
      <title>{title}</title>
      <item identifier="ITEM-1" identifierref="RES-1">
        <title>{title}</title>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="RES-1" type="webcontent" adlcp:scormtype="sco" href="index.html">
      <file href="index.html"/>
      <file href="scorm_api.js"/>
    </resource>
  </resources>
</manifest>"""

def build_conecta_bloques(zip_name, identifier, title, subtitle, pairs):
    pairs_json = json.dumps(pairs, ensure_ascii=False)
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<script src="scorm_api.js"></script>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Segoe UI', Roboto, Arial, sans-serif; background: #f1f5f9; color: #0f172a; padding: 24px; }}
  .container {{ max-width: 1100px; margin: 0 auto; background: #ffffff; border-radius: 14px; padding: 28px; box-shadow: 0 10px 25px rgba(15,23,42,0.08); }}
  .header {{ border-bottom: 2px solid #e2e8f0; padding-bottom: 16px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; }}
  .header h1 {{ font-size: 24px; color: #0f172a; }}
  .header p {{ font-size: 14px; color: #475569; margin-top: 4px; }}
  .stats {{ display: flex; gap: 16px; align-items: center; }}
  .badge {{ background: #e0f2fe; color: #0369a1; padding: 8px 14px; border-radius: 999px; font-weight: 700; font-size: 14px; font-variant-numeric: tabular-nums; }}
  .board {{ display: grid; grid-template-columns: 1fr 1.3fr; gap: 24px; margin-top: 16px; }}
  @media (max-width: 768px) {{ .board {{ grid-template-columns: 1fr; }} }}
  .col-title {{ font-size: 15px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #334155; margin-bottom: 12px; }}
  .card-item {{ background: #f8fafc; border: 2px solid #cbd5e1; border-radius: 10px; padding: 14px 16px; margin-bottom: 10px; cursor: pointer; transition: all 0.2s; font-size: 15px; line-height: 1.4; display: flex; align-items: center; justify-content: space-between; }}
  .card-item:hover {{ border-color: #0284c7; background: #f0f9ff; }}
  .card-item.selected {{ border-color: #0284c7; background: #e0f2fe; box-shadow: 0 0 0 3px rgba(2,132,199,0.2); }}
  .card-item.matched {{ border-color: #16a34a; background: #dcfce7; color: #14532d; cursor: default; opacity: 0.9; }}
  .card-item.wrong {{ border-color: #dc2626; background: #fee2e2; animation: shake 0.35s; }}
  @keyframes shake {{ 0%, 100% {{ transform: translateX(0); }} 25% {{ transform: translateX(-6px); }} 75% {{ transform: translateX(6px); }} }}
  .msg {{ margin-top: 20px; padding: 16px; border-radius: 10px; display: none; font-weight: 600; text-align: center; }}
  .msg.win {{ display: block; background: #dcfce7; color: #166534; border: 1px solid #86efac; }}
  .btn {{ background: #0284c7; color: #fff; border: none; padding: 10px 18px; border-radius: 8px; cursor: pointer; font-weight: 600; }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <div>
      <h1>{title}</h1>
      <p>{subtitle}</p>
    </div>
    <div class="stats">
      <span class="badge" id="scoreBadge">Pares conectados: 0 / 8</span>
      <button class="btn" onclick="initGame()">Reiniciar</button>
    </div>
  </div>
  <div class="board">
    <div>
      <div class="col-title">Conceptos Clave</div>
      <div id="leftCol"></div>
    </div>
    <div>
      <div class="col-title">Definiciones y Aplicaciones en Salud</div>
      <div id="rightCol"></div>
    </div>
  </div>
  <div id="winMsg" class="msg">¡Excelente! Has conectado correctamente los 8 bloques conceptuales. Actividad registrada como completada (100%) en Moodle.</div>
</div>
<script>
const pairs = {pairs_json};
let selectedLeft = null;
let matchedCount = 0;

function shuffle(arr) {{
  return arr.slice().sort(() => Math.random() - 0.5);
}}

function initGame() {{
  selectedLeft = null;
  matchedCount = 0;
  document.getElementById('scoreBadge').textContent = `Pares conectados: 0 / ${{pairs.length}}`;
  document.getElementById('winMsg').className = 'msg';
  const leftCol = document.getElementById('leftCol');
  const rightCol = document.getElementById('rightCol');
  leftCol.innerHTML = '';
  rightCol.innerHTML = '';

  shuffle(pairs).forEach(p => {{
    const el = document.createElement('div');
    el.className = 'card-item';
    el.textContent = p.concept;
    el.dataset.id = p.id;
    el.onclick = () => selectConcept(el);
    leftCol.appendChild(el);
  }});

  shuffle(pairs).forEach(p => {{
    const el = document.createElement('div');
    el.className = 'card-item';
    el.textContent = p.definition;
    el.dataset.id = p.id;
    el.onclick = () => selectDefinition(el);
    rightCol.appendChild(el);
  }});
}}

function selectConcept(el) {{
  if (el.classList.contains('matched')) return;
  document.querySelectorAll('#leftCol .card-item').forEach(c => c.classList.remove('selected'));
  el.classList.add('selected');
  selectedLeft = el;
}}

function selectDefinition(el) {{
  if (!selectedLeft || el.classList.contains('matched')) return;
  if (selectedLeft.dataset.id === el.dataset.id) {{
    selectedLeft.classList.remove('selected');
    selectedLeft.classList.add('matched');
    el.classList.add('matched');
    selectedLeft = null;
    matchedCount++;
    document.getElementById('scoreBadge').textContent = `Pares conectados: ${{matchedCount}} / ${{pairs.length}}`;
    if (matchedCount === pairs.length) {{
      document.getElementById('winMsg').className = 'msg win';
      scorm.complete(100);
    }}
  }} else {{
    el.classList.add('wrong');
    setTimeout(() => el.classList.remove('wrong'), 450);
  }}
}}

initGame();
</script>
</body>
</html>"""
    zip_path = SCORM_DIR / zip_name
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("index.html", html)
        zf.writestr("scorm_api.js", SCORM_API_JS)
        zf.writestr("imsmanifest.xml", create_manifest(identifier, title))
    print(f"Created SCORM Conecta Bloques: {zip_path}")

def build_trivia(zip_name, identifier, title, subtitle, questions):
    q_json = json.dumps(questions, ensure_ascii=False)
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<script src="scorm_api.js"></script>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Segoe UI', Roboto, Arial, sans-serif; background: #0f172a; color: #f8fafc; padding: 24px; }}
  .container {{ max-width: 850px; margin: 0 auto; background: #1e293b; border-radius: 16px; padding: 30px; box-shadow: 0 15px 35px rgba(0,0,0,0.4); border: 1px solid #334155; }}
  .top-bar {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 1px solid #334155; padding-bottom: 14px; }}
  .top-bar h1 {{ font-size: 20px; color: #38bdf8; }}
  .pill {{ background: #0f172a; padding: 6px 14px; border-radius: 999px; font-size: 14px; font-weight: 700; color: #e2e8f0; border: 1px solid #475569; font-variant-numeric: tabular-nums; }}
  .stem {{ font-size: 19px; font-weight: 600; line-height: 1.5; margin-bottom: 20px; color: #ffffff; }}
  .option {{ background: #0f172a; border: 2px solid #334155; border-radius: 10px; padding: 14px 18px; margin-bottom: 12px; cursor: pointer; transition: all 0.2s; font-size: 16px; color: #e2e8f0; text-align: left; width: 100%; display: block; }}
  .option:hover:not(:disabled) {{ border-color: #38bdf8; background: #1e293b; }}
  .option.correct {{ border-color: #22c55e; background: rgba(34,197,94,0.18); color: #bbf7d0; }}
  .option.wrong {{ border-color: #ef4444; background: rgba(239,68,68,0.18); color: #fecaca; }}
  .feedback {{ margin-top: 16px; padding: 16px; border-radius: 10px; background: #0f172a; border-left: 4px solid #38bdf8; display: none; line-height: 1.5; font-size: 15px; color: #cbd5e1; }}
  .btn {{ margin-top: 20px; background: #0284c7; color: #ffffff; border: none; padding: 12px 24px; border-radius: 8px; font-size: 16px; font-weight: 700; cursor: pointer; display: none; }}
  .summary {{ text-align: center; display: none; padding: 24px 0; }}
  .summary h2 {{ font-size: 28px; margin-bottom: 12px; color: #38bdf8; }}
  .summary p {{ font-size: 18px; margin-bottom: 20px; color: #cbd5e1; }}
</style>
</head>
<body>
<div class="container">
  <div class="top-bar">
    <h1>{title}</h1>
    <div>
      <span class="pill" id="progressPill">1 / 10</span>
      <span class="pill" id="scorePill">Puntos: 0</span>
    </div>
  </div>
  <div id="quizArea">
    <div class="stem" id="stemText"></div>
    <div id="optionsBox"></div>
    <div class="feedback" id="feedbackBox"></div>
    <button class="btn" id="nextBtn" onclick="nextQuestion()">Siguiente desafío →</button>
  </div>
  <div class="summary" id="summaryArea">
    <h2 id="finalTitle"></h2>
    <p id="finalStats"></p>
    <button class="btn" style="display:inline-block" onclick="startQuiz()">Jugar otra vez (Preguntas barajadas)</button>
  </div>
</div>
<script>
const rawQuestions = {q_json};
let deck = [];
let idx = 0;
let correctCount = 0;

function shuffle(a) {{ return a.slice().sort(() => Math.random() - 0.5); }}

function startQuiz() {{
  deck = shuffle(rawQuestions);
  idx = 0;
  correctCount = 0;
  document.getElementById('quizArea').style.display = 'block';
  document.getElementById('summaryArea').style.display = 'none';
  renderQuestion();
}}

function renderQuestion() {{
  const q = deck[idx];
  document.getElementById('progressPill').textContent = `${{idx + 1}} / ${{deck.length}}`;
  document.getElementById('scorePill').textContent = `Aciertos: ${{correctCount}}`;
  document.getElementById('stemText').textContent = q.stem;
  document.getElementById('feedbackBox').style.display = 'none';
  document.getElementById('nextBtn').style.display = 'none';

  const box = document.getElementById('optionsBox');
  box.innerHTML = '';
  const opts = q.options.map((text, i) => ({{ text, isCorrect: i === q.correct }}));
  shuffle(opts).forEach(o => {{
    const btn = document.createElement('button');
    btn.className = 'option';
    btn.textContent = o.text;
    btn.onclick = () => checkAnswer(btn, o.isCorrect, q.feedback, opts);
    box.appendChild(btn);
  }});
}}

function checkAnswer(btn, isCorrect, feedbackText) {{
  const buttons = document.querySelectorAll('.option');
  buttons.forEach(b => b.disabled = true);
  if (isCorrect) {{
    btn.classList.add('correct');
    correctCount++;
  }} else {{
    btn.classList.add('wrong');
  }}
  document.getElementById('scorePill').textContent = `Aciertos: ${{correctCount}}`;
  const fb = document.getElementById('feedbackBox');
  fb.innerHTML = `<strong>${{isCorrect ? '¡Correcto!' : 'Revisión conceptual:'}}</strong> ${{feedbackText}}`;
  fb.style.display = 'block';
  document.getElementById('nextBtn').style.display = 'inline-block';
}}

function nextQuestion() {{
  idx++;
  if (idx < deck.length) {{
    renderQuestion();
  }} else {{
    const pct = Math.round((correctCount / deck.length) * 100);
    scorm.complete(pct);
    document.getElementById('quizArea').style.display = 'none';
    document.getElementById('summaryArea').style.display = 'block';
    document.getElementById('finalTitle').textContent = pct >= 70 ? '¡Desafío Superado!' : 'Buen intento, sigue practicando';
    document.getElementById('finalStats').textContent = `Obtuviste ${{correctCount}} de ${{deck.length}} respuestas correctas (${{pct}}%). Tu calificación ha sido sincronizada con Moodle.`;
  }}
}}

startQuiz();
</script>
</body>
</html>"""
    zip_path = SCORM_DIR / zip_name
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("index.html", html)
        zf.writestr("scorm_api.js", SCORM_API_JS)
        zf.writestr("imsmanifest.xml", create_manifest(identifier, title))
    print(f"Created SCORM Trivia: {zip_path}")

u1_pairs = [
    {"id": "1", "concept": "Gestión en Salud", "definition": "Conducción estratégica orientada a personas, sincronización de voluntades y logro de resultados asistenciales."},
    {"id": "2", "concept": "Administración Tradicional", "definition": "Enfoque normativo y ordenador centrado en procesos, licencias, horarios y regularidad técnica."},
    {"id": "3", "concept": "Vector EL SER", "definition": "Identidad institucional compuesta por Misión (propósito), Visión (horizonte), Valores y Principios rectores."},
    {"id": "4", "concept": "Vector EL HACER", "definition": "Dimensión operativa que define prioridades, funciones (finales y de apoyo) y actividades estandarizadas."},
    {"id": "5", "concept": "Vector EL ESTAR", "definition": "Dimensión relacional y física que abarca el ambiente, la estructura organizativa y la cultura."},
    {"id": "6", "concept": "Cultura Tipo Clan", "definition": "Estructura familiar y colaborativa con alta cohesión, sentido de pertenencia y ambiente de confianza."},
    {"id": "7", "concept": "Cultura Tipo Adhocracia", "definition": "Estructura dinámica y flexible orientada a la innovación, asunción de riesgos y proyectos creativos."},
    {"id": "8", "concept": "Cultura Jerárquica", "definition": "Modelo corporativo tradicional centrado en la cadena de mando formal, estabilidad y reglas estrictas."}
]

u2_pairs = [
    {"id": "1", "concept": "Premisa del Factor Humano (2+2≠4)", "definition": "Principio de que los imponderables y factores emocionales impiden fórmulas rígidas en la conducción sanitaria."},
    {"id": "2", "concept": "Emisor Asistencial", "definition": "Profesional responsable de codificar el mensaje adaptándolo a las características de su interlocutor."},
    {"id": "3", "concept": "Perceptor Activo", "definition": "Interlocutor que decodifica e interpreta la información según su edad, vivencias y condicionantes."},
    {"id": "4", "concept": "Equipo de Trabajo en Salud", "definition": "Conjunto de profesionales con habilidades complementarias, metas compartidas y responsabilidad colectiva."},
    {"id": "5", "concept": "Grupo de Trabajo", "definition": "Agrupación basada en afinidades o tareas similares donde la responsabilidad es estrictamente individual."},
    {"id": "6", "concept": "Paradigma del Quirófano", "definition": "Modelo de equipo interdependiente con roles coordinados en tiempo real hacia una meta vital común."},
    {"id": "7", "concept": "Liderazgo Situacional", "definition": "Capacidad de guiar, motivar y persuadir sin coerción, adaptando el estilo según la coyuntura clínica."},
    {"id": "8", "concept": "Empatía Genuina", "definition": "Competencia de comprender la perspectiva del otro para decidir asertivamente, sin caer en permisividad."}
]

u1_questions = [
    {"stem": "¿Cuál es la diferencia sustancial entre administrar y gestionar según la Dra. Susana Salomón?", "options": ["Administrar se orienta a normar procesos y regularidad técnica; gestionar se enfoca en conducir personas y sincronizar voluntades.", "Administrar conduce personas mientras que gestionar establece sanciones normativas.", "Administrar aplica exclusivamente en hospitales privados y gestionar en efectores públicos.", "No existen diferencias; ambos términos son sinónimos en el sector salud."], "correct": 0, "feedback": "Administrar ordena bajo criterios normativos y de procesos, mientras que gestionar conduce estratégicamente el talento humano hacia resultados."},
    {"stem": "Dentro de la tridimensionalidad institucional, ¿a qué vector corresponde la Misión, Visión, Valores y Principios Rectores?", "options": ["Vector del SER.", "Vector del HACER.", "Vector del ESTAR.", "Vector del ENTORNO."], "correct": 0, "feedback": "El SER representa la identidad nuclear no negociable de la organización: qué somos, qué queremos ser y bajo qué valores actuamos."},
    {"stem": "¿Cómo se define la Misión de una institución sanitaria?", "options": ["El propósito, razón de ser y contribución fundamental de la organización a la comunidad en el presente.", "El presupuesto económico anual asignado por el Ministerio.", "El organigrama jerárquico publicado en la oficina de personal.", "La proyección arquitectónica del hospital a veinte años."], "correct": 0, "feedback": "La Misión responde a 'qué somos' hoy y establece el sentido de dirección común para sincronizar esfuerzos."},
    {"stem": "¿Por qué los Principios Rectores y Valores Éticos no son considerados un 'bien transable'?", "options": ["Porque constituyen el cimiento ético innegociable (calidad, seguridad, equidad) que guía toda decisión institucional.", "Porque tienen un valor contable fijo en el balance del hospital.", "Porque solo pueden ser modificados por los proveedores externos.", "Porque únicamente aplican al personal administrativo."], "correct": 0, "feedback": "El SER institucional no se negocia; transigir en los principios rectores destruye la confianza y el propósito sanitario."},
    {"stem": "En el vector del HACER, las funciones organizativas de un hospital se dividen en:", "options": ["Funciones finales (asistenciales directas) y funciones intermedias o de apoyo.", "Funciones jerárquicas y funciones informales.", "Funciones rentables y funciones deficitarias.", "Funciones permanentes y funciones eventuales."], "correct": 0, "feedback": "Las funciones finales atienden directamente al paciente y las de apoyo (laboratorio, mantenimiento, farmacia) garantizan su viabilidad."},
    {"stem": "¿Qué diferencia existe entre la cadena de mando formal y la cadena de mando real en el vector del ESTAR?", "options": ["La formal figura en el organigrama normativo, mientras que la real refleja los referentes de autoridad y consulta efectiva en la práctica diaria.", "Son idénticas en todos los hospitales públicos.", "La cadena real es ilegal y debe sancionarse administrativamente.", "La cadena formal solo aplica a los médicos residentes."], "correct": 0, "feedback": "En las organizaciones complejas coexiste el organigrama oficial con redes reales de liderazgo técnico y moral."},
    {"stem": "¿Cómo se define a la Cultura Organizacional en las instituciones de salud?", "options": ["La personalidad o alma de la organización compuesta por significados, ritos, valores y códigos compartidos.", "El reglamento de licencias y control de ausentismo del empleado público.", "La encuesta de satisfacción que completan los usuarios.", "El manual de procedimientos de bioseguridad hospitalaria."], "correct": 0, "feedback": "La cultura es el alma institucional que da sentido de identidad, pertenencia y pautas de conducta."},
    {"stem": "¿Cuáles son las características centrales de una cultura organizacional de tipo Clan?", "options": ["Ambiente familiar y colaborativo, alta cohesión, trabajo en equipo y fuerte sentido de pertenencia.", "Competencia agresiva entre colegas y foco exclusivo en la rentabilidad.", "Rigidez extrema y apego estricto a la cadena de mando formal.", "Asunción permanente de riesgos disruptivos sin normas compartidas."], "correct": 0, "feedback": "La cultura Clan funciona como una gran familia colaborativa, aunque enfrenta límites cuando la escala institucional crece masivamente."},
    {"stem": "¿Qué caracteriza a una cultura hospitalaria de tipo Adhocracia?", "options": ["Flexibilidad, estímulo a la innovación, creatividad constante y asunción de riesgos frente a nuevos desafíos.", "Rechazo al cambio tecnológico y apego a rutinas tradicionales.", "Estandarización absoluta sin margen para la iniciativa individual.", "Foco exclusivo en la reducción de costos operativos."], "correct": 0, "feedback": "La Adhocracia impulsa la innovación y el dinamismo, enriqueciendo las estructuras tradicionales."},
    {"stem": "¿Cuál es la diferencia precisa entre Clima Laboral y Cultura Organizacional?", "options": ["El clima es la percepción subjetiva coyuntural del ambiente de trabajo, mientras que la cultura es la matriz profunda e histórica de la institución.", "Son sinónimos absolutos en la gestión sanitaria.", "El clima nunca cambia y la cultura varía todos los días.", "El clima depende exclusivamente de la infraestructura edilicia."], "correct": 0, "feedback": "El clima laboral es una parte subjetiva y situacional dentro del entramado más amplio y estable de la cultura organizacional."}
]

u2_questions = [
    {"stem": "¿Qué expresa la premisa 'en la gestión de personas 2+2 nunca es 4' formulada por la Lic. Carla Nani?", "options": ["Que el comportamiento humano está atravesado por imponderables y emociones que impiden aplicar fórmulas rígidas.", "Que las estadísticas hospitalarias suelen presentar errores de carga.", "Que el presupuesto sanitario siempre resulta insuficiente.", "Que los turnos de guardia deben duplicarse."], "correct": 0, "feedback": "Al trabajar con personas existen imponderables y subjetividades que exigen adaptabilidad y flexibilidad constante."},
    {"stem": "En el esquema de comunicación en salud, ¿por qué hablamos de Perceptor y no de receptor pasivo?", "options": ["Porque el interlocutor humano percibe, filtra y decodifica activamente el mensaje según sus propios condicionantes.", "Porque receptor solo se aplica a los médicos de guardia.", "Porque el paciente no tiene capacidad de responder al profesional.", "Porque el mensaje escrito no requiere interpretación."], "correct": 0, "feedback": "Un receptor pasivo es un aparato mecánico (como un buzón de voz); las personas son perceptores que interpretan desde su historia y contexto."},
    {"stem": "¿Sobre quién recae la responsabilidad primordial de lograr una comunicación eficaz en la consulta o pase de sala?", "options": ["Sobre el emisor (profesional de la salud), quien debe adaptar la codificación del mensaje al perfil de su perceptor.", "Exclusivamente sobre el paciente o familiar que escucha.", "Sobre el área administrativa de admisión.", "Sobre el jefe de departamento ausente."], "correct": 0, "feedback": "Como especialistas en salud, somos responsables de diagnosticar los condicionantes de nuestro perceptor y adecuar el código."},
    {"stem": "¿Qué elementos integran los condicionantes del perceptor que pueden modificar la interpretación de un mensaje clínico?", "options": ["Edad, nivel socioeconómico, bagaje cultural, estado emocional agudo, vivencias previas y prejuicios.", "Únicamente el nivel de audición física del paciente.", "El horario de atención del consultorio externo.", "La marca del equipamiento médico utilizado."], "correct": 0, "feedback": "Todos estos factores subjetivos y socioculturales actúan como filtros durante la decodificación del mensaje."},
    {"stem": "¿Cuál es la diferencia fundamental entre un Equipo de Trabajo y un Grupo de Trabajo en salud?", "options": ["El equipo posee habilidades complementarias, meta común y responsabilidad compartida; en el grupo cada uno responde individualmente.", "El grupo trabaja en quirófano y el equipo solo en tareas administrativas.", "En el equipo todos tienen la misma profesión y en el grupo no.", "No existe diferencia entre grupo y equipo en un hospital."], "correct": 0, "feedback": "En un equipo las especialidades se complementan sinérgicamente y las decisiones son sostenidas de forma corresponsable."},
    {"stem": "¿Por qué el Quirófano representa el paradigma por excelencia del trabajo en equipo en salud?", "options": ["Porque convergen especialidades diversas (cirujano, anestesiólogo, instrumentador, enfermería) con roles interdependientes sincronizados tras el bienestar del paciente.", "Porque allí nadie tiene funciones asignadas de antemano.", "Porque las decisiones se toman por votación asamblearia lenta.", "Porque no requiere comunicación verbal ni no verbal."], "correct": 0, "feedback": "En el quirófano cada integrante domina su faceta técnica con interdependencia total y cohesión operativa."},
    {"stem": "¿Cómo se define el Liderazgo Situacional positivo en los servicios asistenciales?", "options": ["La capacidad de guiar, motivar y persuadir sin coerción, adaptando el estilo directivo según la madurez del equipo y la urgencia del contexto.", "La imposición de órdenes mediante sanciones y miedo.", "Mantener exactamente el mismo estilo rígido tanto en una emergencia como en una reunión académica.", "Dejar que el equipo actúe sin ninguna dirección ni objetivos."], "correct": 0, "feedback": "El líder positivo influye por convicción y adapta su conducción a las demandas cambiantes de cada situación sanitaria."},
    {"stem": "¿Cuál es el límite entre la Empatía Genuina y la Permisividad en el ejercicio del liderazgo?", "options": ["La empatía comprende la situación del colaborador para decidir con justicia sin perder los estándares del servicio; la permisividad cede a todo y diluye la autoridad.", "Son conceptos idénticos en recursos humanos.", "La empatía implica perdonar cualquier negligencia clínica reiterada.", "La permisividad fortalece el respeto profesional del equipo."], "correct": 0, "feedback": "Ponerse en el lugar del otro permite acompañar y reacomodar temporalmente al equipo sin claudicar en la responsabilidad asistencial."},
    {"stem": "De acuerdo con la Pirámide de Maslow aplicada al talento humano en salud, ¿cómo empodera un buen líder a sus colaboradores?", "options": ["Reconociendo sus logros, validando sus capacidades, fomentando el sentido de pertenencia y promoviendo su desarrollo profesional.", "Limitándose exclusivamente al control del fichado horario.", "Ocultando información estratégica para volverse indispensable.", "Evitando delegar tareas importantes para no perder poder."], "correct": 0, "feedback": "El reconocimiento, la confianza al delegar y el crecimiento continuo satisfacen las necesidades superiores de estima y autorrealización."},
    {"stem": "¿Cuáles son las causas más frecuentes por las que fracasa un líder en una institución de salud?", "options": ["Falta de escucha activa, impulsividad, incapacidad para delegar, autoritarismo, rigidez contextual y falta de ética.", "Exceso de capacitación académica y diálogo con los residentes.", "Adaptarse rápidamente a los imponderables de la guardia.", "Fomentar el trabajo colaborativo interdisciplinario."], "correct": 0, "feedback": "El líder autocrático que no escucha, no delega y carece de flexibilidad situacional termina aislando y frustrando a su equipo."}
]

final_exam_questions = [
    {"stem": "Un residente de segundo año asume la coordinación de las guardias de fin de semana. Advierte que los pases de sala son desordenados porque cada profesional reporta datos según su criterio individual, derivando en omisiones farmacológicas. La Misión del hospital destaca la «seguridad del paciente», pero no existen actividades estandarizadas en el HACER ni pautas de comunicación. ¿Cuál es la intervención prioritaria?", "options": ["Alinear el HACER con el SER mediante la estandarización de actividades (lista de verificación de pase de guardia) y capacitar al emisor en comunicación eficaz.", "Aplicar sanciones económicas a los residentes sin modificar los procesos del servicio.", "Cambiar la Visión del hospital en el Boletín Oficial sin intervenir en la guardia.", "Solicitar que los familiares transcriban las indicaciones médicas."], "correct": 0, "feedback": "La gestión estratégica exige coherencia entre los valores del SER y las actividades estandarizadas del HACER."},
    {"stem": "En un Centro de Salud, los médicos, enfermeros y trabajadores sociales atienden en consultorios contiguos pero sin intercambiar información. Ante un brote epidemiológico barrial no logran coordinar las visitas domiciliarias. Aplicando el paradigma del Quirófano (Lic. Carla Nani), ¿qué transformación debe impulsar la coordinación?", "options": ["Transformar el grupo en un equipo interdependiente, articulando sus especialidades complementarias y asumiendo responsabilidad compartida por la meta sanitaria común.", "Mantener el trabajo fragmentado para que cada profesional responda solo por su planilla individual.", "Exigir que todos los profesionales realicen exactamente la misma tarea administrativa.", "Cerrar los consultorios de trabajo social y enfermería."], "correct": 0, "feedback": "Un equipo de salud supera la suma individual gracias a la complementariedad de roles y la cohesión."},
    {"stem": "Durante una cirugía compleja, la instrumentadora advierte que un insumo presenta una falla de esterilización y alerta de inmediato en voz clara al cirujano jefe, quien detiene la maniobra, agradece la advertencia y reemplaza el material. ¿Qué dinámica se observa en esta escena?", "options": ["Un equipo de trabajo cohesivo donde las jerarquías formales se dinamizan en favor del rol experto de cada miembro y la seguridad del paciente.", "Una falta grave a la cadena de mando que debería sancionarse administrativamente.", "Una cultura de tipo Mercado basada en la competencia interna.", "Un grupo social formado por afinidad recreativa."], "correct": 0, "feedback": "En el equipo interdependiente la decisión técnica oportuna es respaldada por todo el colectivo."},
    {"stem": "Una médica residente debe explicar un diagnóstico complejo y el tratamiento al alta a un paciente rural de 78 años que se encuentra ansioso y con dificultades auditivas. Si aplica el esquema comunicacional de la Lic. Carla Nani, ¿cómo debe proceder?", "options": ["Asumir su responsabilidad como emisora, reconocer los condicionantes etarios, culturales y emocionales de su perceptor, y codificar el mensaje con lenguaje claro, pausado y empático.", "Entregarle un folleto impreso en jerga médica técnica, ya que como profesional siempre explica todo de la misma manera.", "Culpar al paciente si no comprende los tecnicismos biomédicos.", "Evitar el contacto visual y limitarse a cargar los datos en la computadora."], "correct": 0, "feedback": "En salud no existen receptores mecánicos pasivos; cada paciente y familiar es un perceptor activo."},
    {"stem": "Un hospital público cuenta con su Misión, Visión y Principios Rectores publicados por Resolución Ministerial (el SER). Sin embargo, en el Servicio de Clínica Médica predomina el maltrato verbal en los pases de guardia, el ocultamiento de errores por miedo y una alta rotación de residentes. ¿Cuál es el diagnóstico institucional correcto?", "options": ["Existe una fractura entre el SER formal declarado y el ESTAR cotidiano, manifestada en un clima laboral tóxico que deteriora el bienestar y la productividad asistencial.", "El hospital no necesita gestionar su clima laboral porque ya tiene su Misión escrita en el Boletín Oficial.", "El servicio presenta una cultura tipo Clan altamente saludable.", "Es un problema exclusivamente contable de las funciones de apoyo."], "correct": 0, "feedback": "La gestión estratégica debe alinear el SER, el HACER y el ESTAR promoviendo un clima ético y saludable."},
    {"stem": "En la clasificación funcional del vector del HACER (Dra. Susana Salomón), ¿cómo se articula el Servicio de Laboratorio Central y Mantenimiento con el Servicio de Internación Pediátrica?", "options": ["Internación Pediátrica cumple una función final (asistencial directa) y Laboratorio/Mantenimiento cumplen funciones intermedias o de apoyo indispensables para que aquella se realice.", "Ambos servicios cumplen exclusivamente funciones administrativas de control horario.", "Laboratorio es una función final externa y Pediatría es una función de apoyo.", "No tienen ninguna relación funcional dentro de la estructura hospitalaria."], "correct": 0, "feedback": "Reconocer el valor de las funciones de apoyo fortalece la integración interdisciplinaria en el hospital."},
    {"stem": "Un nuevo Jefe de Servicio intenta implementar un protocolo innovador de telemedicina, pero fracasa porque solo se apoyó en el organigrama impreso sin consultar a los médicos de planta y enfermeros referentes a quienes todo el equipo escucha y respeta desde hace veinte años. ¿Qué elemento del vector del ESTAR ignoró?", "options": ["La cadena de mando real y los líderes naturales que sostienen la cultura del servicio.", "El control administrativo de licencias anuales.", "La liquidación de haberes del servicio de personal.", "El diseño arquitectónico de la fachada del hospital."], "correct": 0, "feedback": "Analizar la estructura en el ESTAR exige comprender tanto el organigrama formal como los liderazgos reales del equipo."},
    {"stem": "Un centro privado de diagnóstico por imágenes evalúa a sus profesionales exclusivamente por la cantidad de estudios facturados por hora, generando rivalidad entre colegas, falta de cooperación en casos dudosos y agotamiento emocional. ¿Qué tipología cultural predomina y cuál es su límite?", "options": ["Predomina la cultura de Mercado; su beneficio es el foco en resultados y rentabilidad, pero su límite es la competencia interna, la desmotivación y el desgaste del compromiso.", "Predomina la cultura tipo Clan familiar y colaborativa.", "Predomina la cultura Jerárquica sin metas de rentabilidad.", "Predomina la cultura de Adhocracia filantrópica."], "correct": 0, "feedback": "Conocer los límites de cada tipología cultural permite equilibrar la eficiencia con el cuidado del talento humano."},
    {"stem": "Durante una guardia nocturna ocurre una caída brusca del suministro eléctrico en un sector de internación y, simultáneamente, ingresa un politraumatismo grave. El equipo reconfigura de inmediato las camas y los roles sin esperar órdenes burocráticas. ¿Qué principio de la Unidad 2 explica esta situación?", "options": ["En salud «dos más dos nunca es cuatro»: los imponderables existen permanentemente y exigen adaptabilidad rápida, trabajo en equipo y liderazgo situacional.", "Las organizaciones de salud son sistemas mecánicos exactos donde nunca ocurre nada fuera de lo programado.", "Ante un imponderable cada profesional debe actuar de forma aislada e individual.", "Solo la administración normativa de expedientes resuelve una emergencia clínica."], "correct": 0, "feedback": "La adaptabilidad frente a los imponderables es una competencia central en la gestión de personas en salud."},
    {"stem": "Una residente de tercer año nota que su compañero de primer año está cometiendo errores de concentración porque atraviesa la internación grave de su hijo. Decide cubrirle la realización de un procedimiento complejo hoy, dialoga con él en privado y acuerda cómo reorganizar sus tareas de la semana sin exponerlo ni humillarlo, manteniendo la calidad del servicio. ¿Qué competencia ejerció?", "options": ["Empatía genuina y liderazgo situacional positivo, comprendiendo el momento humano del colega para cuidar tanto al equipo como al paciente sin caer en permisividad.", "Permisividad destructiva que arruina la disciplina hospitalaria.", "Liderazgo autocrático y coercitivo.", "Desinterés por los objetivos asistenciales del servicio."], "correct": 0, "feedback": "Correr temporalmente a un compañero que atraviesa un mal momento, acompañándolo hasta que se acomode, es propio de un liderazgo empático."},
    {"stem": "Un referente médico pretende que su equipo cumpla las nuevas guías clínicas mediante amenazas y gritos, se niega a escuchar las dificultades operativas que le plantean las enfermeras, toma decisiones impulsivas y nunca delega porque afirma que «nadie hace las cosas como yo». ¿Cuál es el pronóstico de su conducción?", "options": ["Fracasará como líder, ya que reúne las causas clásicas de fracaso: uso de coerción en vez de persuasión, falta de escucha, impulsividad e incapacidad para delegar.", "Tendrá éxito duradero porque el estilo autocrático es el único válido en salud.", "Logrará empoderar a su equipo satisfaciendo las necesidades superiores de Maslow.", "Fomentará una cultura de innovación y adhocracia participativa."], "correct": 0, "feedback": "El líder que no escucha, no delega y no se adapta al contexto termina siendo superado y perdiendo el respaldo del equipo."},
    {"stem": "En los hospitales coexisten profesionales de múltiples especialidades, técnicos, administrativos, personal de limpieza, mantenimiento y seguridad. ¿Cómo define la Dra. Susana Salomón a las instituciones de salud en función de esta característica?", "options": ["Organizaciones complejas con múltiples dominios sociales y técnicos donde coexisten diversos saberes, metas e identidades orientados a dar valor agregado a la salud.", "Organizaciones simples y homogéneas con un único dominio técnico.", "Empresas exclusivamente financieras ajenas al contexto social.", "Estructuras estáticas inmunes a la innovación tecnológica."], "correct": 0, "feedback": "Comprender los múltiples dominios sociales y técnicos del hospital es esencial para integrar a todo el personal en una cultura compartida."},
    {"stem": "En el Servicio de Cirugía General los pases de guardia son breves, verticales y ejecutivos, mientras que en el Servicio de Medicina Interna del mismo hospital se realizan extensos ateneos deliberativos horizontales. ¿Cómo se denomina este fenómeno cultural?", "options": ["Coexistencia de subculturas hospitalarias (quirúrgica vs. clínica) dentro de una misma cultura organizacional, cada una con sus rituales, ritmos y códigos propios.", "Ausencia total de identidad institucional en el hospital.", "Falla administrativa del departamento de contaduría.", "Recepción mecánica pasiva del mensaje."], "correct": 0, "feedback": "Las subculturas enriquecen a la institución siempre que permanezcan alineadas con la Misión y los Principios Rectores comunes."},
    {"stem": "Según la aplicación de la Pirámide de Maslow en la gestión del talento humano (Lic. Carla Nani), ¿qué ocurre cuando un jefe de servicio reconoce públicamente el excelente desempeño de sus residentes y les delega responsabilidades acordes a su crecimiento?", "options": ["Satisface necesidades superiores de pertenencia, reconocimiento, estima y desarrollo profesional, empoderando e inspirando al equipo.", "Pierde autoridad frente al equipo y fomenta la indisciplina.", "Actúa únicamente sobre el escalón fisiológico básico.", "Genera un clima laboral tóxico de competencia agresiva."], "correct": 0, "feedback": "Un buen líder jamás esconde información ni teme que sus colaboradores brillen; los empodera en pos del equipo."},
    {"stem": "Uno de los desafíos contemporáneos del contexto sanitario señalados en la Unidad 1 es la «pulverización por especialidades y subespecialidades». ¿Qué problema genera este fenómeno y cómo debe responder la gestión?", "options": ["Dificulta el abordaje integral e integrado del paciente; la gestión debe responder articulando el trabajo inter y transdisciplinario centrado en la persona.", "Mejora automáticamente la comunicación sin necesidad de coordinar equipos.", "Se resuelve eliminando todas las especialidades médicas del hospital.", "Solo afecta a las áreas de mantenimiento edilicio."], "correct": 0, "feedback": "Integrar saberes diversos en equipos cohesivos es la respuesta estratégica ante la fragmentación asistencial."},
    {"stem": "De acuerdo con la Circular N° 5 que regula este curso en el Campus Virtual ESALUD, ¿cómo opera el Sistema de Doble Candado Automatizado para obtener el Certificado Oficial de 30 Horas Reloj?", "options": ["Exige cumplir dos condiciones encadenadas: 1) Aprobar este Examen Final Integrador con calificación mayor o igual al 70%, y 2) Completar la Encuesta de Calidad Educativa.", "El certificado se emite solo con matricularse en el aula sin rendir evaluaciones.", "Requiere presentar un expediente impreso en papel en la oficina de personal.", "Solo exige ver el primer video sin realizar las prácticas ni el examen final."], "correct": 0, "feedback": "Cumplidas ambas condiciones, el campus habilita automáticamente la descarga del Certificado Oficial de 30 horas."}
]

build_conecta_bloques("u1_conecta_bloques_SCORM.zip", "scorm-u1-conecta-bloques", "Conecta Bloques Unidad 1: Cultura y Gestión", "Empareja los 8 conceptos estratégicos de la Dra. Susana Salomón con sus definiciones.", u1_pairs)
build_conecta_bloques("u2_conecta_bloques_SCORM.zip", "scorm-u2-conecta-bloques", "Conecta Bloques Unidad 2: Comunicación y Liderazgo", "Empareja los 8 conceptos clave de la Lic. Carla Nani con sus definiciones asistenciales.", u2_pairs)
build_trivia("u1_trivia_SCORM.zip", "scorm-u1-trivia", "Trivia Gamificada Unidad 1: Cultura Organizacional", "Autoevaluación formativa con preguntas barajadas sin numeración rígida.", u1_questions)
build_trivia("u2_trivia_SCORM.zip", "scorm-u2-trivia", "Trivia Gamificada Unidad 2: Comunicación y Liderazgo", "Autoevaluación formativa con preguntas barajadas sin numeración rígida.", u2_questions)
build_trivia("examen_final_integrador_SCORM.zip", "scorm-examen-final-integrador", "Examen Final Sumativo Integrador (Unidades 1 y 2)", "Evaluación integradora de 16 casos clínico-institucionales (Aprobación >= 70%).", final_exam_questions)
