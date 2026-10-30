import sys
from pathlib import Path

BASE_DIR = Path(r"c:\Users\mfischer\Documents\antigravitiy proyectos\aula nueva con moodle\cursos\gestion_personas_talento")
REPO_ROOT = Path(r"c:\Users\mfischer\Documents\antigravitiy proyectos\aula nueva con moodle")
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
if str(REPO_ROOT / "scripts" / "scorm_generators") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "scripts" / "scorm_generators"))

from scripts.audio_generators.podcast_engine import generate_podcast_sync
from create_audio_scorm import create_audio_scorm

files = {}

# 00_encabezado_general_curso.html
files["00_encabezado_general_curso.html"] = """---
tipo: etiqueta
nombre: "Presentación Oficial: Gestión de Personas y Talento Humano en Salud"
seccion: "Presentación y Programa Académico"
finalizacion: manual
---

<p><img src="img/banner_general_curso.png" alt="Banner Oficial Curso 3: Gestión de Personas y Talento Humano en Salud" class="img-fluid rounded-lg mb-3"></p>

<h3><i class="fa-solid fa-fw fa-graduation-cap" aria-hidden="true"></i> Curso 3: Gestión de Personas y Talento Humano en Salud</h3>
<p><span class="badge badge-primary">30 Horas Reloj</span> <span class="badge badge-info">100% Virtual Asincrónico</span> <span class="badge badge-secondary">Circular N° 5 ESALUD</span></p>

<p class="lead">En las instituciones sanitarias complejas, la excelencia asistencial no depende únicamente del saber clínico individual, sino de la capacidad estratégica de conducir personas, sincronizar voluntades y construir culturas organizacionales saludables. Este trayecto formativo brinda a los profesionales de las residencias herramientas concretas de cultura institucional, comunicación asertiva, trabajo en equipo interdependiente y liderazgo situacional.</p>

<div class="alert alert-info">
  <h4><i class="fa-solid fa-fw fa-bullseye" aria-hidden="true"></i> Competencias Transversales y Recorrido Tripartito</h4>
  <ul class="mb-0">
    <li><strong>Unidad 1 (Dra. Susana Salomón):</strong> Cultura Organizacional, Gestión vs. Administración y los Vectores del SER, el HACER y el ESTAR.</li>
    <li><strong>Unidad 2 (Lic. Carla Nani):</strong> Gestión de Imponderables, Proceso Comunicacional con Perceptor, Paradigma del Quirófano y Liderazgo Situacional.</li>
    <li><strong>Acreditación (Doble Candado Circular N° 5):</strong> Aprobación del Examen Final Integrador (calificación mayor o igual al 70%) y completamiento de la Encuesta de Calidad Educativa.</li>
  </ul>
</div>
"""

# 01_u1_encabezado.html
files["01_u1_encabezado.html"] = """---
tipo: etiqueta
nombre: "Unidad 1: Encuadre y Preguntas Andragógicas"
seccion: "Unidad 1: Cultura Organizacional y Gestión"
finalizacion: manual
---

<p><img src="img/banner_unidad_1.png" alt="Banner Unidad 1: Cultura Organizacional y Desafíos de la Gestión" class="img-fluid rounded-lg mb-3"></p>

<h3><i class="fa-solid fa-fw fa-flag" aria-hidden="true"></i> Unidad 1: Cultura Organizacional y los Desafíos de la Gestión Institucional</h3>
<p><span class="badge badge-primary">Semanas 1 y 2</span> <span class="badge badge-info">Docente: Dra. Susana Salomón</span></p>

<p class="lead">La gestión de personas en el ámbito sanitario exige superar el enfoque normativo tradicional para conducir estratégicamente el talento humano en escenarios signados por la complejidad y la incertidumbre. Comprender la identidad institucional a través de la tridimensionalidad del <strong>SER</strong>, el <strong>HACER</strong> y el <strong>ESTAR</strong> permite diagnosticar las manifestaciones culturales y promover entornos laborales altamente efectivos.</p>

<div class="alert alert-info">
  <h4><i class="fa-solid fa-fw fa-circle-question" aria-hidden="true"></i> Tres Preguntas Andragógicas Disparadoras (Circular N° 5)</h4>
  <ol class="mb-0">
    <li><strong>Supuestos Inconscientes:</strong> ¿De qué manera las pautas no escritas y los rituales cotidianos de su servicio asistencial condicionan la toma de decisiones clínicas y la integración de los nuevos residentes?</li>
    <li><strong>Tensión Identitaria:</strong> Al observar las dinámicas de su hospital o centro de salud, ¿cómo se manifiestan las tensiones entre los valores declarados (el SER) y la asignación real de prioridades operativas (el HACER)?</li>
    <li><strong>Diagnóstico de Tipología Cultural:</strong> Identificando la cultura predominante en su área (Clan, Adhocracia, Mercado o Jerárquica), ¿cuáles son las principales barreras u oportunidades que esta genera para consolidar un clima laboral saludable?</li>
  </ol>
</div>
"""

# 02_u1_la_clase.html
files["02_u1_la_clase.html"] = """---
tipo: pagina
nombre: "1. La Clase: Cultura Organizacional y Tridimensionalidad de la Gestión"
seccion: "Unidad 1: Cultura Organizacional y Gestión"
finalizacion: ver
---

<h3><i class="fa-solid fa-fw fa-video" aria-hidden="true"></i> 1. La Clase: Cultura Organizacional en Salud</h3>
<p><span class="badge badge-primary">Etapa 1 del Modelo Tripartito</span> <span class="badge badge-secondary">Dra. Susana Salomón</span></p>
<p class="lead">Visualizá la videoclase magistral de la unidad, escuchá el podcast pedagógico de cátedra, repasá las cápsulas audiovisuales de microlearning y descargá las diapositivas oficiales.</p>

<div class="alert alert-info">
  <h4><i class="fa-solid fa-fw fa-bullseye" aria-hidden="true"></i> Qué vas a aprender en esta clase</h4>
  <ul class="mb-0">
    <li>Diferenciar la <strong>administración normativa</strong> de procesos frente a la <strong>gestión estratégica</strong> del talento humano en salud.</li>
    <li>Articular los tres vectores de la identidad hospitalaria: el <strong>SER</strong> (Misión, Visión, Valores y Principios rectores), el <strong>HACER</strong> (Prioridades, Funciones finales y de apoyo, Actividades) y el <strong>ESTAR</strong> (Estructura formal vs. real, Ambiente y Cultura).</li>
    <li>Reconocer las 4 tipologías culturales (Clan, Adhocracia, Mercado y Jerárquica) y distinguir entre clima laboral y cultura organizacional.</li>
  </ul>
</div>

<!-- PODCAST DE LA UNIDAD 1 (CLAUDEMY ENGINE) -->
<div class="card border-info mb-4 shadow-sm">
  <div class="card-header bg-info text-white d-flex align-items-center justify-content-between">
    <h4 class="mb-0 text-white"><i class="fa-solid fa-fw fa-podcast" aria-hidden="true"></i> Podcast de la Unidad 1: Del SER Declarado al ESTAR Cotidiano</h4>
    <span class="badge badge-light text-dark">Microlearning Audio · 2 min</span>
  </div>
  <div class="card-body">
    <p class="card-text"><strong>Diálogo de Cátedra:</strong> Un intercambio dinámico entre la docente y un residente sobre las tensiones reales entre el organigrama impreso, las pautas no escritas en la guardia médica y por qué el núcleo ético del hospital no se negocia.</p>
    <div class="p-3 bg-light rounded mb-3">
      <audio controls style="width: 100%;">
        <source src="media/u1_podcast_cultura.mp3" type="audio/mpeg">
        Tu navegador no soporta el reproductor de audio HTML5.
      </audio>
    </div>
    <div class="d-flex flex-wrap gap-2">
      <a class="btn btn-sm btn-outline-info mr-2" href="media/u1_podcast_cultura.mp3" download><i class="fa-solid fa-fw fa-download" aria-hidden="true"></i> Descargar Audio (MP3)</a>
      <a class="btn btn-sm btn-info text-white" href="scorm/u1_podcast_SCORM.zip" target="_blank"><i class="fa-solid fa-fw fa-box-archive" aria-hidden="true"></i> Módulo SCORM del Podcast</a>
    </div>
  </div>
</div>

<h3>Videoclase Magistral Oficial</h3>
<p>Reproducí la clase completa desde el reproductor embebido o abrila directamente en una pestaña externa:</p>
<p><iframe src="https://www.youtube.com/embed/wEQLqEE7r2I" title="Módulo 4: Unidad 1. CULTURA ORGANIZACIONAL - Dra. Susana Salomón" style="width:100%;aspect-ratio:16/9;border:0" allowfullscreen></iframe></p>

<div class="row">
  <div class="col-md-6 mb-3">
    <div class="card border-primary">
      <div class="card-body">
        <h4 class="card-title text-primary"><i class="fa-solid fa-fw fa-link" aria-hidden="true"></i> Recursos Audiovisuales</h4>
        <p class="card-text">Contás con tres recursos audiovisuales para abordar los ejes de la Dra. Susana Salomón:</p>
        <ul class="mb-3">
          <li><strong>Videoclase Magistral:</strong> Exposición completa de la unidad.</li>
          <li><strong>Video Short NotebookLM:</strong> Síntesis conceptual (<em>Por Qué Gestionar No Es Administrar</em>).</li>
          <li><strong>Video Short HyperFrames:</strong> Microlearning animado en alta definición sobre vectores y tipologías.</li>
        </ul>
        <p class="mb-2"><a class="btn btn-primary" href="https://www.youtube.com/watch?v=wEQLqEE7r2I" target="_blank">Abrir Videoclase Magistral en YouTube</a></p>
        <p class="mb-2"><a class="btn btn-secondary" href="media/u1_video_short_cultura_organizacional.mp4" target="_blank">Ver Video Short NotebookLM (MP4)</a></p>
        <p class="mb-0"><a class="btn btn-info text-white" href="media/u1_hyperframes_short.mp4" target="_blank">Ver Video Short HyperFrames (MP4)</a></p>
      </div>
    </div>
  </div>
  <div class="col-md-6 mb-3">
    <div class="card bg-light">
      <div class="card-body">
        <h4 class="card-title"><i class="fa-solid fa-fw fa-download" aria-hidden="true"></i> Diapositivas Oficiales</h4>
        <p class="card-text">Descargá las placas oficiales de estudio de la Unidad 1 en formato PDF o PowerPoint editable:</p>
        <ul class="mb-3">
          <li><a href="diapositivas/u1_diapositivas_cultura_organizacional.pdf" target="_blank">Descargar Diapositivas Oficiales Unidad 1 (PDF)</a></li>
          <li><a href="diapositivas/u1_diapositivas_cultura_organizacional.pptx" target="_blank">Descargar Presentación Editable Unidad 1 (PPTX)</a></li>
        </ul>
        <p class="card-text mb-0"><strong>Guía de observación activa:</strong> Prestá especial atención a la diferencia entre la cadena de mando formal y los referentes reales a quienes acude el equipo en la urgencia.</p>
      </div>
    </div>
  </div>
</div>

<div class="alert alert-success">
  <h4><i class="fa-solid fa-fw fa-lightbulb" aria-hidden="true"></i> Recuerda</h4>
  <p class="mb-0">El vector del <strong>SER</strong> (Misión, Visión, Valores y Principios Rectores) constituye el núcleo ético de la institución y <strong>no es un bien transable ni negociable</strong>.</p>
</div>
"""

# 03_u1_la_lectura.html
files["03_u1_la_lectura.html"] = """---
tipo: pagina
nombre: "2. La Lectura: Dossier Teórico, Infografías, Glosario y FAQs (Unidad 1)"
seccion: "Unidad 1: Cultura Organizacional y Gestión"
finalizacion: ver
restricciones:
  completar:
    - 02_u1_la_clase.html
---

<h3><i class="fa-solid fa-fw fa-book-open" aria-hidden="true"></i> 2. La Lectura: Profundización Teórica y Síntesis Visual</h3>
<p><span class="badge badge-primary">Etapa 2 del Modelo Tripartito</span> <span class="badge badge-info">Lecturas Mediadas + 2 Infografías NotebookLM</span></p>
<p class="lead">En esta sección profundizamos los marcos conceptuales de la Dra. Susana Salomón mediante tres lecturas estructuradas, dos infografías de síntesis visual, el glosario terminológico y diez preguntas frecuentes sobre dilemas culturales en hospitales.</p>

<h3>Infografía 1.1: Gestión vs. Administración y Vectores de Identidad</h3>
<p><img src="img/u1_infografia_01_gestion_y_vectores.png" alt="Infografía Unidad 1: Gestión y administración institucional sanitaria y vectores SER, HACER y ESTAR" class="img-fluid rounded-lg mb-3"></p>

<h3>Síntesis de las 3 Lecturas Didácticas de la Unidad 1</h3>
<div class="row">
  <div class="col-md-4 mb-3">
    <div class="card">
      <div class="card-body">
        <h4 class="card-title">Lectura 1.1: Gestión vs. Administración</h4>
        <p class="card-text">Mientras <strong>administrar</strong> ordena procesos, horarios y licencias con enfoque normativo, <strong>gestionar</strong> conduce talento humano y sincroniza voluntades frente a un contexto sanitario atravesado por la Inteligencia Artificial, la pulverización por especialidades y la incertidumbre permanente.</p>
      </div>
    </div>
  </div>
  <div class="col-md-4 mb-3">
    <div class="card">
      <div class="card-body">
        <h4 class="card-title">Lectura 1.2: El SER, el HACER y el ESTAR</h4>
        <p class="card-text">El <strong>SER</strong> define la identidad innegociable (Misión, Visión, Valores y Principios rectores). El <strong>HACER</strong> articula prioridades, funciones finales (asistenciales) y de apoyo, y actividades. El <strong>ESTAR</strong> abarca el ambiente, la estructura (cadena formal vs. real) y la cultura.</p>
      </div>
    </div>
  </div>
  <div class="col-md-4 mb-3">
    <div class="card">
      <div class="card-body">
        <h4 class="card-title">Lectura 1.3: Tipologías y Clima Laboral</h4>
        <p class="card-text">La cultura es el alma institucional transmitida por historias, ritos, símbolos y lenguaje. Coexisten subculturas clínicas y quirúrgicas, y cuatro arquetipos: <strong>Clan, Adhocracia, Mercado y Jerárquica</strong>. El clima es la percepción subjetiva coyuntural del entorno.</p>
      </div>
    </div>
  </div>
</div>

<h3>Infografía 1.2: Tipologías Culturales y Clima Laboral Sanitario</h3>
<p><img src="img/u1_infografia_02_tipologias_y_clima.png" alt="Infografía Unidad 1: Las 4 tipologías culturales en salud y diferenciación entre clima y cultura" class="img-fluid rounded-lg mb-3"></p>

<h3><i class="fa-solid fa-fw fa-download" aria-hidden="true"></i> Carpeta Temática de Lecturas Descargables — Unidad 1</h3>
<div class="card border-primary mb-3">
  <div class="card-body">
    <h4 class="card-title text-primary">Repositorio Documental: Cultura Organizacional y Gestión</h4>
    <p class="card-text">Todos los documentos teóricos y presentaciones de esta unidad se encuentran agrupados en su carpeta temática correspondiente:</p>
    <ul class="mb-0">
      <li><a href="lecturas/unidad_1/lectura_1_1_gestion_vs_administracion_y_contexto.docx" target="_blank">Lectura 1.1: Gestión vs. Administración y Complejidad del Contexto Sanitario (DOCX)</a></li>
      <li><a href="lecturas/unidad_1/lectura_1_2_vectores_identidad_ser_hacer_estar.docx" target="_blank">Lectura 1.2: Los Tres Vectores de la Identidad Institucional: SER, HACER y ESTAR (DOCX)</a></li>
      <li><a href="lecturas/unidad_1/lectura_1_3_cultura_tipologias_y_clima_laboral.docx" target="_blank">Lectura 1.3: Cultura Organizacional, Tipologías y Clima Laboral (DOCX)</a></li>
      <li><a href="diapositivas/u1_diapositivas_cultura_organizacional.pdf" target="_blank">Diapositivas de Cátedra Unidad 1: Cultura Organizacional en Salud (PDF)</a></li>
    </ul>
  </div>
</div>

<h3><i class="fa-solid fa-fw fa-book" aria-hidden="true"></i> Glosario Terminológico de la Unidad 1</h3>
<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Término Clave</th>
      <th scope="col">Definición Académica Aplicada en Salud</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Administración en Salud</strong></td>
      <td>Enfoque normativo y ordenador centrado en procesos, cumplimiento de reglamentos, licencias y regularidad técnica.</td>
    </tr>
    <tr>
      <td><strong>Gestión Estratégica</strong></td>
      <td>Conducción centrada en el talento humano, la sincronización de voluntades y el logro eficiente de resultados sanitarios.</td>
    </tr>
    <tr>
      <td><strong>Vector del SER</strong></td>
      <td>Núcleo identitario innegociable integrado por la Misión, la Visión, los Valores estratégicos y los Principios rectores.</td>
    </tr>
    <tr>
      <td><strong>Funciones Finales vs. Apoyo</strong></td>
      <td>Las funciones finales asisten directamente al paciente (guardia, internación, quirófano); las de apoyo proveen el soporte indispensable (laboratorio, farmacia, mantenimiento).</td>
    </tr>
    <tr>
      <td><strong>Cadena de Mando Real</strong></td>
      <td>Red de autoridad técnica y ascendencia moral a la que acuden efectivamente los profesionales más allá del organigrama formal.</td>
    </tr>
    <tr>
      <td><strong>Cultura Organizacional</strong></td>
      <td>Personalidad o alma de la organización conformada por significados compartidos, historias, ritos, símbolos y supuestos inconscientes.</td>
    </tr>
    <tr>
      <td><strong>Subcultura Hospitalaria</strong></td>
      <td>Configuración cultural específica de determinados servicios (ej. área clínica deliberativa frente a área quirúrgica ejecutiva).</td>
    </tr>
    <tr>
      <td><strong>Clima Laboral</strong></td>
      <td>Percepción subjetiva, individual y colectiva sobre el ambiente cotidiano de trabajo y la calidad de la convivencia interna.</td>
    </tr>
  </tbody>
</table>

<h3><i class="fa-solid fa-fw fa-circle-question" aria-hidden="true"></i> Preguntas Frecuentes (FAQs) sobre Dilemas Culturales</h3>
<div class="card bg-light mb-3">
  <div class="card-body">
    <h4 class="card-title">1. ¿Puede un hospital funcionar eficazmente solo con administración tradicional sin gestión?</h4>
    <details>
      <summary>Ver respuesta fundamentada</summary>
      <p class="mt-2 mb-0">No. La administración garantiza el orden procedimental y el control de personal, pero sin gestión estratégica se pierde el rumbo asistencial, se desmotiva al talento humano y la organización no logra adaptarse a la incertidumbre del entorno.</p>
    </details>
  </div>
</div>
<div class="card bg-light mb-3">
  <div class="card-body">
    <h4 class="card-title">2. ¿Por qué los Principios Rectores deben publicarse oficialmente y no son negociables?</h4>
    <details>
      <summary>Ver respuesta fundamentada</summary>
      <p class="mt-2 mb-0">Porque establecen el piso ético de la institución (seguridad del paciente, equidad, honestidad). Si una organización negocia sus principios por conveniencia coyuntural, destruye su legitimidad social y fractura el compromiso ético de sus profesionales.</p>
    </details>
  </div>
</div>
<div class="card bg-light mb-3">
  <div class="card-body">
    <h4 class="card-title">3. ¿Qué riesgo corre un servicio público que adopta una cultura puramente de Mercado?</h4>
    <details>
      <summary>Ver respuesta fundamentada</summary>
      <p class="mt-2 mb-0">Fomenta la competencia agresiva entre colegas, el desgaste emocional (<em>burnout</em>) y el descuido de las actividades preventivas o de difícil cuantificación inmediata.</p>
    </details>
  </div>
</div>
<div class="card bg-light mb-3">
  <div class="card-body">
    <h4 class="card-title">4. ¿De qué manera un clima laboral tóxico impacta en la seguridad del paciente?</h4>
    <details>
      <summary>Ver respuesta fundamentada</summary>
      <p class="mt-2 mb-0">Un clima hostil o punitivo silencia el reporte temprano de incidentes, bloquea la consulta de los residentes ante dudas clínicas y multiplica los errores de comunicación durante los pases de guardia.</p>
    </details>
  </div>
</div>
"""

# 04_u1_la_practica.html
files["04_u1_la_practica.html"] = """---
tipo: pagina
nombre: "3. La Práctica: Desafíos Interactivos, Caso de Triage y Rúbrica (Unidad 1)"
seccion: "Unidad 1: Cultura Organizacional y Gestión"
finalizacion: ver
restricciones:
  completar:
    - 03_u1_la_lectura.html
---

<h3><i class="fa-solid fa-fw fa-puzzle-piece" aria-hidden="true"></i> 3. La Práctica: Aplicación Situada y Gamificación</h3>
<p><span class="badge badge-primary">Etapa 3 del Modelo Tripartito</span> <span class="badge badge-success">Conecta Bloques + Trivia + Caso Situado</span></p>

<div class="alert alert-warning">
  <h4><i class="fa-solid fa-fw fa-triangle-exclamation" aria-hidden="true"></i> Importante: Consigna Orientadora Obligatoria</h4>
  <p class="mb-0">Esta actividad práctica se resuelve integrando los conceptos de la videoclase magistral de la Dra. Susana Salomón, el video short microlearning y las tres lecturas teóricas de la Unidad 1. Analizá críticamente tu servicio hospitalario e identificá cómo los vectores del <strong>SER</strong>, el <strong>HACER</strong> y el <strong>ESTAR</strong> moldean el comportamiento cotidiano antes de realizar el Conecta Bloques, la Trivia y el Caso Situado.</p>
</div>

<h3>Ficha de Desafíos Interactivos de la Unidad 1</h3>
<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Desafío</th>
      <th scope="col">Objetivo de Aprendizaje</th>
      <th scope="col">Modalidad en el Aula</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Conecta Bloques (8 pares)</strong></td>
      <td>Emparejar los conceptos de Gestión, Administración, vectores SER/HACER/ESTAR y Tipologías Culturales con sus definiciones exactas.</td>
      <td>Actividad interactiva de emparejamiento / Paquete SCORM <code>u1_conecta_bloques_SCORM.zip</code></td>
    </tr>
    <tr>
      <td><strong>2. Trivia Gamificada Unidad 1</strong></td>
      <td>Resolver 10 situaciones conceptuales con preguntas barajadas sin numeración rígida y retroalimentación inmediata.</td>
      <td>Cuestionario formativo con intentos ilimitados / Paquete SCORM <code>u1_trivia_SCORM.zip</code></td>
    </tr>
    <tr>
      <td><strong>3. Caso Situado de Gestión</strong></td>
      <td>Diagnosticar la tensión entre rigidez jerárquica e innovación adhocrática en un servicio de Triage de urgencias.</td>
      <td>Resolución analítica evaluada mediante rúbrica de 3 criterios.</td>
    </tr>
  </tbody>
</table>

<h3>Caso Situado de Gestión Hospitalaria: Tensión en el Servicio de Triage</h3>
<div class="card border-primary mb-3">
  <div class="card-body">
    <h4 class="card-title text-primary">Escenario Clínico-Institucional</h4>
    <p class="card-text">El Servicio de Urgencias del Hospital Central registró un incremento del 35% en los tiempos de espera en Triage durante el último semestre. La Misión declarada del hospital establece ser un <em>«centro de excelencia con atención centrada en las personas y respuesta oportuna»</em> (<strong>el SER</strong>). Sin embargo, el servicio opera bajo una cultura estrictamente <strong>Jerárquica</strong>. Los residentes e instructores diseñaron un protocolo ágil de reevaluación dinámica (con rasgos de <strong>Adhocracia</strong>), pero la Jefatura lo rechazó argumentando que <em>«no figura en el manual tradicional ni siguió la vía jerárquica formal»</em>. Esto provocó desmotivación, deterioro del clima laboral y reclamos constantes en la guardia.</p>
    <details>
      <summary>Ver guía de resolución sugerida</summary>
      <p class="mt-2 mb-0"><strong>Claves de intervención:</strong> 1) Evidenciar la contradicción entre el SER (atención oportuna centrada en la persona) y el HACER/ESTAR (burocracia rígida que demora el Triage). 2) Incorporar a los líderes de la cadena de mando real para validar una prueba piloto controlada, combinando la seguridad normativa de la cultura jerárquica con la flexibilidad innovadora de la adhocracia.</p>
    </details>
  </div>
</div>

<h3>Rúbrica Analítica de Evaluación del Caso (Unidad 1)</h3>
<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Criterio</th>
      <th scope="col">Excelente (4 pts)</th>
      <th scope="col">Satisfactorio (3 pts)</th>
      <th scope="col">En Proceso (2 pts)</th>
      <th scope="col">Inicial (1 pt)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Diagnóstico del SER, HACER y ESTAR</strong></td>
      <td>Articula con precisión los 3 vectores y explicita la contradicción entre la Misión declarada y el proceso operativo real.</td>
      <td>Identifica correctamente los 3 vectores, aunque con menor detalle en la distinción entre cadena formal y real.</td>
      <td>Reconoce parcialmente las dimensiones pero confunde funciones del HACER con componentes del ESTAR.</td>
      <td>No distingue los vectores de la identidad institucional en el caso planteado.</td>
    </tr>
    <tr>
      <td><strong>2. Tipología Cultural y Clima Laboral</strong></td>
      <td>Fundamenta con rigor los límites de la cultura Jerárquica, el aporte de la Adhocracia y el impacto en el clima del servicio.</td>
      <td>Clasifica bien la tipología cultural y diferencia clima de cultura de manera general.</td>
      <td>Menciona el malestar del equipo pero confunde clima laboral coyuntural con cultura organizacional.</td>
      <td>No aplica la clasificación de tipologías culturales vista en la unidad.</td>
    </tr>
    <tr>
      <td><strong>3. Propuesta de Gestión Estratégica</strong></td>
      <td>Diseña una intervención viable que sincroniza voluntades, estandariza mejoras en el HACER y preserva los principios rectores.</td>
      <td>Propone medidas correctivas adecuadas pero centradas únicamente en aspectos administrativos.</td>
      <td>Plantea sugerencias aisladas sin abordar la resistencia cultural del servicio.</td>
      <td>Propone medidas puramente punitivas que agravan el clima organizacional.</td>
    </tr>
  </tbody>
</table>
"""

# 05_u1_conecta_bloques_y_trivia.md
files["05_u1_conecta_bloques_y_trivia.md"] = """---
tipo: cuestionario
nombre: "Práctica Gamificada Unidad 1: Conecta Bloques y Trivia de Cultura Organizacional"
seccion: "Unidad 1: Cultura Organizacional y Gestión"
intentos: ilimitados
mezclar_respuestas: true
finalizacion: calificar
restricciones:
  completar:
    - 04_u1_la_practica.html
preguntas:
  - tipo: emparejamiento
    enunciado: "Conecta Bloques Unidad 1: Empareja cada uno de los 8 conceptos estratégicos de la Dra. Susana Salomón con su definición exacta en la gestión hospitalaria."
    parejas:
      - pregunta: "**Gestión en Salud**"
        respuesta: "Conducción estratégica orientada a personas, sincronización de voluntades y logro de resultados asistenciales."
      - pregunta: "**Administración Tradicional**"
        respuesta: "Enfoque normativo y ordenador centrado en procesos, licencias, horarios y regularidad técnica."
      - pregunta: "**Vector EL SER**"
        respuesta: "Identidad institucional compuesta por Misión (propósito), Visión (horizonte), Valores y Principios rectores."
      - pregunta: "**Vector EL HACER**"
        respuesta: "Dimensión operativa que define prioridades, funciones (finales y de apoyo) y actividades estandarizadas."
      - pregunta: "**Vector EL ESTAR**"
        respuesta: "Dimensión relacional y física que abarca el ambiente, la estructura organizativa y la cultura."
      - pregunta: "**Cultura Tipo Clan**"
        respuesta: "Estructura familiar y colaborativa con alta cohesión, sentido de pertenencia y ambiente de confianza."
      - pregunta: "**Cultura Tipo Adhocracia**"
        respuesta: "Estructura dinámica y flexible orientada a la innovación, asunción de riesgos y proyectos creativos."
      - pregunta: "**Cultura Jerárquica**"
        respuesta: "Modelo corporativo tradicional centrado en la cadena de mando formal, estabilidad y reglas estrictas."
    retro: "Excelente. Dominar la distinción entre gestionar y administrar, los vectores SER-HACER-ESTAR y las tipologías culturales es la base del diagnóstico institucional."

  - tipo: opcion_multiple
    enunciado: "¿Cuál es la diferencia sustancial entre **administrar** y **gestionar** según la fundamentación de la Dra. Susana Salomón?"
    opciones:
      - texto: "Administrar se orienta a normar procesos y regularidad técnica, mientras que gestionar se enfoca en conducir personas, sincronizar voluntades y alcanzar resultados."
        correcta: true
        retro: "¡Correcto! Administrar ordena recursos y normas; gestionar conduce talento humano hacia resultados asistenciales."
      - texto: "Administrar conduce personas mientras que gestionar establece sanciones normativas de presentismo."
        retro: "Incorrecto. Es exactamente al revés: el control normativo corresponde a la administración."
      - texto: "Administrar aplica exclusivamente en hospitales privados y gestionar en efectores públicos."
        retro: "Incorrecto. Ambas dimensiones coexisten tanto en instituciones públicas como privadas."
      - texto: "No existen diferencias conceptuales; ambos términos son sinónimos absolutos."
        retro: "Incorrecto. Tienen alcances estratégicos y operativos claramente diferenciados."
    retro: "Recordá el ejemplo hospitalario: la oficina de personal administra horarios y licencias; el área de talento humano gestiona la capacitación y el desarrollo."

  - tipo: opcion_multiple
    enunciado: "Dentro de la tridimensionalidad institucional, ¿a qué vector corresponde la definición de la **Misión, Visión, Valores y Principios Rectores**?"
    opciones:
      - texto: "Dimensión del SER."
        correcta: true
        retro: "¡Exacto! El SER constituye el núcleo identitario y ético no negociable de la organización."
      - texto: "Dimensión del HACER."
        retro: "Incorrecto. El HACER abarca las prioridades, funciones y actividades operativas."
      - texto: "Dimensión del ESTAR."
        retro: "Incorrecto. El ESTAR comprende la estructura, el ambiente y la cultura cotidiana."
      - texto: "Dimensión del MERCADO."
        retro: "Incorrecto. Mercado es una tipología cultural, no uno de los tres vectores identitarios."
    retro: "El SER responde a quiénes somos, hacia dónde vamos y bajo qué principios éticos innegociables actuamos."

  - tipo: opcion_multiple
    enunciado: "¿Cómo se define la **Misión** de una institución sanitaria?"
    opciones:
      - texto: "El propósito, razón de ser y contribución fundamental de la organización a la comunidad en el presente."
        correcta: true
        retro: "¡Muy bien! La Misión expresa qué somos y para quién existimos hoy."
      - texto: "El presupuesto financiero aprobado para el ejercicio anual."
        retro: "Incorrecto. El presupuesto es un instrumento financiero, no la misión institucional."
      - texto: "El plano arquitectónico y de mantenimiento del edificio hospitalario."
        retro: "Incorrecto. La infraestructura física forma parte de los artefactos y recursos."
      - texto: "El listado de sanciones disciplinarias del reglamento interno."
        retro: "Incorrecto. Eso corresponde a normativas administrativas."
    retro: "Sin una misión clara y compartida, los esfuerzos de los distintos servicios no pueden sincronizarse."

  - tipo: opcion_multiple
    enunciado: "¿Por qué se afirma en la cátedra que los **Principios Rectores y Valores Éticos** no son un «bien transable»?"
    opciones:
      - texto: "Porque constituyen las convicciones éticas innegociables (seguridad, calidad, honestidad, equidad) que ningún interés coyuntural puede vulnerar."
        correcta: true
        retro: "¡Correcto! Con el SER ético de la institución no se transa ni se negocia."
      - texto: "Porque su valor monetario está congelado por resolución contable."
        retro: "Incorrecto. No se refiere a un activo financiero sino a convicciones deontológicas."
      - texto: "Porque solo pueden modificarse mediante un acuerdo comercial externo."
        retro: "Incorrecto. Los principios rectores son el cimiento ético permanente."
      - texto: "Porque únicamente obligan a los directivos y no al equipo asistencial."
        retro: "Incorrecto. Guían la conducta de todos los integrantes de la organización."
    retro: "Los principios rectores están en la base de la pirámide identitaria y suelen refrendarse por resolución oficial."

  - tipo: opcion_multiple
    enunciado: "En la dimensión del **HACER**, ¿cómo se clasifican las funciones organizativas dentro de un hospital?"
    opciones:
      - texto: "Funciones finales (asistenciales directas) y funciones intermedias o de apoyo (laboratorio, farmacia, mantenimiento)."
        correcta: true
        retro: "¡Exacto! Ambas son indispensables y complementarias para cumplir la misión sanitaria."
      - texto: "Funciones superiores y funciones prescindibles."
        retro: "Incorrecto. Ninguna función de apoyo es prescindible; sin esterilización o mantenimiento el hospital se detiene."
      - texto: "Funciones contables y funciones publicitarias."
        retro: "Incorrecto. No refleja la división sustantiva del trabajo hospitalario."
      - texto: "Funciones individuales y funciones recreativas."
        retro: "Incorrecto."
    retro: "Las funciones finales brindan la atención directa al usuario y las de apoyo garantizan los insumos y condiciones para que ello ocurra."

  - tipo: opcion_multiple
    enunciado: "¿Qué elementos integran el vector del **ESTAR** institucional?"
    opciones:
      - texto: "El ambiente de intercambio, la estructura organizativa (cadena de mando formal y real) y la cultura."
        correcta: true
        retro: "¡Correcto! El ESTAR abarca dónde y cómo convivimos y nos estructuramos diariamente."
      - texto: "Únicamente los balances contables del último trimestre."
        retro: "Incorrecto."
      - texto: "Las matrículas profesionales individuales de los médicos."
        retro: "Incorrecto."
      - texto: "Exclusivamente la redacción de la visión a largo plazo."
        retro: "Incorrecto. La visión pertenece al vector del SER."
    retro: "En el ESTAR es clave distinguir entre el organigrama impreso (estructura formal) y las redes de referencia efectiva (cadena de mando real)."

  - tipo: opcion_multiple
    enunciado: "¿Cómo se define la **Cultura Organizacional** y cuáles son sus mecanismos de transmisión?"
    opciones:
      - texto: "Es el alma o personalidad de la organización, y se transmite mediante historias, ritos y rituales, símbolos materiales y lenguaje específico."
        correcta: true
        retro: "¡Muy bien! Esos cuatro mecanismos consolidan el sentido de pertenencia e identidad."
      - texto: "Es el código de procedimientos contables y se transmite solo por circulares escritas."
        retro: "Incorrecto. La cultura trasciende lo normativo e incluye supuestos inconscientes."
      - texto: "Es el estado de ánimo pasajero de un lunes por la mañana."
        retro: "Incorrecto. Eso se vincula con percepciones coyunturales de clima, no con la matriz cultural."
      - texto: "Es un reglamento estático que nunca influye en la productividad."
        retro: "Incorrecto. La cultura impacta directamente en la efectividad y retención del talento."
    retro: "Los pases de sala, los ateneos, las casacas distintivas y la jerga médica son manifestaciones culturales cotidianas."

  - tipo: opcion_multiple
    enunciado: "¿Qué caracteriza a una organización sanitaria con cultura predominante de tipo **Clan**?"
    opciones:
      - texto: "Un entorno colaborativo de estilo familiar, con alta cohesión, trabajo en equipo y fuerte sentido de pertenencia."
        correcta: true
        retro: "¡Correcto! Su fortaleza es el compromiso humano, aunque su límite aparece cuando la organización crece masivamente."
      - texto: "Una estructura rígida centrada exclusivamente en el control punitivo de horarios."
        retro: "Incorrecto. Eso describe rasgos de una cultura jerárquica rígida."
      - texto: "Una competencia feroz entre colegas por bonos de productividad individual."
        retro: "Incorrecto. Eso corresponde a una cultura de Mercado."
      - texto: "Un cambio caótico permanente sin ningún sentido de tradición ni equipo."
        retro: "Incorrecto."
    retro: "El modelo de tipologías distingue entre Clan (colaboración), Adhocracia (innovación), Mercado (competencia) y Jerárquica (estabilidad)."

  - tipo: opcion_multiple
    enunciado: "¿Cuál es la principal fortaleza y cuál es el principal límite de una cultura **Jerárquica** en un hospital?"
    opciones:
      - texto: "Su fortaleza es la estabilidad, orden y predictibilidad; su límite es la rigidez, lentitud ante el cambio y escaso estímulo a la creatividad."
        correcta: true
        retro: "¡Exacto! Brinda dirección formal pero puede paralizar la innovación ante imprevistos."
      - texto: "Su fortaleza es la innovación disruptiva y su límite es la falta total de reglas."
        retro: "Incorrecto. Esos rasgos corresponden a la Adhocracia."
      - texto: "No posee ningún límite; es el modelo perfecto para cualquier situación."
        retro: "Incorrecto. Toda tipología cultural presenta beneficios y límites."
      - texto: "Su fortaleza es eliminar los cargos directivos."
        retro: "Incorrecto. La cultura jerárquica se apoya fuertemente en la cadena de mando."
    retro: "Comprender los límites de la estructura jerárquica permite introducir espacios de flexibilidad y feedback en los servicios de salud."

  - tipo: opcion_multiple
    enunciado: "¿Cuál es la relación exacta entre **Clima Laboral** y **Cultura Organizacional**?"
    opciones:
      - texto: "El clima laboral es la percepción subjetiva coyuntural de los miembros sobre su ambiente de trabajo, y constituye una parte dentro del marco más profundo de la cultura."
        correcta: true
        retro: "¡Correcto! El clima se percibe en la convivencia diaria; la cultura es la estructura profunda de valores y supuestos."
      - texto: "Son conceptos idénticos sin ninguna diferencia teórica ni práctica."
        retro: "Incorrecto. Clima y cultura no son lo mismo."
      - texto: "La cultura cambia todos los días mientras que el clima permanece inalterable por décadas."
        retro: "Incorrecto. El clima es mucho más sensible a coyunturas que la cultura profunda."
      - texto: "El clima solo afecta al personal de apoyo y la cultura solo al cuerpo médico."
        retro: "Incorrecto. Ambos atraviesan a toda la institución sanitaria."
    retro: "Promover un clima ético y colaborativo mejora el bienestar del equipo, retiene el talento humano y protege la seguridad del paciente."
---

Resolvé la actividad interactiva **Conecta Bloques** (pregunta de emparejamiento de 8 pares) y las **10 situaciones de la Trivia Gamificada** de la Unidad 1. Disponés de intentos ilimitados con retroalimentación formativa en cada respuesta.
"""

# 06_u2_encabezado.html
files["06_u2_encabezado.html"] = """---
tipo: etiqueta
nombre: "Unidad 2: Encuadre y Preguntas Andragógicas"
seccion: "Unidad 2: Comunicación, Trabajo en Equipo y Liderazgo"
finalizacion: manual
---

<p><img src="img/banner_unidad_2.png" alt="Banner Unidad 2: Comunicación, Trabajo en Equipo y Liderazgo en Salud" class="img-fluid rounded-lg mb-3"></p>

<h3><i class="fa-solid fa-fw fa-flag" aria-hidden="true"></i> Unidad 2: Comunicación, Trabajo en Equipo y Liderazgo Situacional en Salud</h3>
<p><span class="badge badge-primary">Semanas 3 y 4</span> <span class="badge badge-success">Docente: Lic. Carla Nani</span></p>

<p class="lead">La gestión eficiente del talento humano en salud exige comprender la premisa ineludible de que \\(2 + 2 \\neq 4\\), adaptando la comunicación al perceptor y a los imponderables del entorno asistencial. Transformar grupos sociales en equipos de trabajo cohesivos conducidos bajo un liderazgo situacional empático constituye la clave para optimizar la atención en áreas críticas como el quirófano o la guardia.</p>

<div class="alert alert-info">
  <h4><i class="fa-solid fa-fw fa-circle-question" aria-hidden="true"></i> Tres Preguntas Andragógicas Disparadoras (Circular N° 5)</h4>
  <ol class="mb-0">
    <li><strong>Atención a los Condicionantes del Perceptor:</strong> ¿Cómo influyen los condicionantes socioculturales, etarios y emocionales de sus perceptores (pacientes, familias y colegas) al codificar un diagnóstico crítico o una indicación en el pase de guardia?</li>
    <li><strong>Del Grupo al Equipo (Paradigma del Quirófano):</strong> Comparando la dinámica cotidiana de su servicio con el modelo interdependiente del quirófano, ¿qué factores favorecen u obstaculizan la responsabilidad colectiva y la complementariedad de roles?</li>
    <li><strong>Liderazgo Situacional y Empatía:</strong> Reflexionando sobre la conducción de personas en contextos de alta presión, ¿dónde radica el límite entre la empatía genuina y la permisividad, y cómo prevenir las causas habituales de fracaso del líder?</li>
  </ol>
</div>
"""

# 07_u2_la_clase.html
files["07_u2_la_clase.html"] = """---
tipo: pagina
nombre: "1. La Clase: Comunicación Asertiva, Equipo en Quirófano y Liderazgo Situacional"
seccion: "Unidad 2: Comunicación, Trabajo en Equipo y Liderazgo"
finalizacion: ver
---

<h3><i class="fa-solid fa-fw fa-video" aria-hidden="true"></i> 1. La Clase: Comunicación, Trabajo en Equipo y Liderazgo</h3>
<p><span class="badge badge-primary">Etapa 1 del Modelo Tripartito</span> <span class="badge badge-success">Lic. Carla Nani</span></p>
<p class="lead">Visualizá la videoclase magistral de la Lic. Carla Nani, escuchá el podcast pedagógico de la unidad, repasá las cápsulas audiovisuales de microlearning y descargá las diapositivas oficiales.</p>

<div class="alert alert-info">
  <h4><i class="fa-solid fa-fw fa-bullseye" aria-hidden="true"></i> Qué vas a aprender en esta clase</h4>
  <ul class="mb-0">
    <li>Comprender por qué en la gestión del talento humano \\(2 + 2 \\neq 4\\) y cómo responder con adaptabilidad ante los <strong>imponderables</strong>.</li>
    <li>Dominar el proceso comunicacional reconociendo al interlocutor como un <strong>perceptor activo</strong> atravesado por condicionantes emocionales y socioculturales.</li>
    <li>Diferenciar un grupo de un <strong>equipo de trabajo asistencial</strong> tomando al <strong>quirófano</strong> como paradigma de interdependencia y responsabilidad compartida.</li>
    <li>Ejercer un <strong>liderazgo situacional</strong> basado en la persuasión, la escucha activa, la empatía genuina y el reconocimiento de necesidades (Maslow).</li>
  </ul>
</div>

<!-- PODCAST DE LA UNIDAD 2 (CLAUDEMY ENGINE) -->
<div class="card border-success mb-4 shadow-sm">
  <div class="card-header bg-success text-white d-flex align-items-center justify-content-between">
    <h4 class="mb-0 text-white"><i class="fa-solid fa-fw fa-podcast" aria-hidden="true"></i> Podcast de la Unidad 2: El Paradigma del Quirófano y la Comunicación Asertiva</h4>
    <span class="badge badge-light text-dark">Microlearning Audio · 2 min</span>
  </div>
  <div class="card-body">
    <p class="card-text"><strong>Diálogo de Cátedra:</strong> La Lic. Carla Nani y un médico del equipo examinan por qué en salud el paciente y el colega nunca son receptores pasivos, cómo opera la interdependencia estricta en el quirófano y dónde trazar el límite entre empatía y permisividad.</p>
    <div class="p-3 bg-light rounded mb-3">
      <audio controls style="width: 100%;">
        <source src="media/u2_podcast_liderazgo.mp3" type="audio/mpeg">
        Tu navegador no soporta el reproductor de audio HTML5.
      </audio>
    </div>
    <div class="d-flex flex-wrap gap-2">
      <a class="btn btn-sm btn-outline-success mr-2" href="media/u2_podcast_liderazgo.mp3" download><i class="fa-solid fa-fw fa-download" aria-hidden="true"></i> Descargar Audio (MP3)</a>
      <a class="btn btn-sm btn-success text-white" href="scorm/u2_podcast_SCORM.zip" target="_blank"><i class="fa-solid fa-fw fa-box-archive" aria-hidden="true"></i> Módulo SCORM del Podcast</a>
    </div>
  </div>
</div>

<h3>Videoclase Magistral Oficial</h3>
<p>Reproducí la clase completa desde el reproductor integrado o abrila en una nueva pestaña:</p>
<p><iframe src="https://www.youtube.com/embed/ELI-w2KgJSc" title="Módulo 4: Video 2. Motivación, Trabajo en Equipo y Liderazgo - Lic. Carla Nani" style="width:100%;aspect-ratio:16/9;border:0" allowfullscreen></iframe></p>

<div class="row">
  <div class="col-md-6 mb-3">
    <div class="card border-primary">
      <div class="card-body">
        <h4 class="card-title text-primary"><i class="fa-solid fa-fw fa-link" aria-hidden="true"></i> Recursos Audiovisuales</h4>
        <p class="card-text">Disponés de tres recursos audiovisuales para consolidar los contenidos de la Lic. Carla Nani:</p>
        <ul class="mb-3">
          <li><strong>Videoclase Magistral:</strong> Exposición completa con casos hospitalarios.</li>
          <li><strong>Video Short NotebookLM:</strong> Síntesis conceptual (<em>Por Qué el Paciente No Es un Receptor</em>).</li>
          <li><strong>Video Short HyperFrames:</strong> Microlearning animado sobre Emisor-Perceptor y Quirófano.</li>
        </ul>
        <p class="mb-2"><a class="btn btn-primary" href="https://www.youtube.com/watch?v=ELI-w2KgJSc" target="_blank">Abrir Videoclase Magistral en YouTube</a></p>
        <p class="mb-2"><a class="btn btn-secondary" href="media/u2_video_short_comunicacion_liderazgo.mp4" target="_blank">Ver Video Short NotebookLM (MP4)</a></p>
        <p class="mb-0"><a class="btn btn-info text-white" href="media/u2_hyperframes_short.mp4" target="_blank">Ver Video Short HyperFrames (MP4)</a></p>
      </div>
    </div>
  </div>
  <div class="col-md-6 mb-3">
    <div class="card bg-light">
      <div class="card-body">
        <h4 class="card-title"><i class="fa-solid fa-fw fa-download" aria-hidden="true"></i> Diapositivas Oficiales</h4>
        <p class="card-text">Descargá las diapositivas oficiales de la Unidad 2 en formato PDF o PowerPoint editable:</p>
        <ul class="mb-3">
          <li><a href="diapositivas/u2_diapositivas_comunicacion_liderazgo.pdf" target="_blank">Descargar Diapositivas Oficiales Unidad 2 (PDF)</a></li>
          <li><a href="diapositivas/u2_diapositivas_comunicacion_liderazgo.pptx" target="_blank">Descargar Presentación Editable Unidad 2 (PPTX)</a></li>
        </ul>
        <p class="card-text mb-0"><strong>Guía de observación activa:</strong> Analizá cómo en el quirófano las jerarquías formales se articulan dinámicamente con el rol experto de cada integrante en pos de la seguridad del paciente.</p>
      </div>
    </div>
  </div>
</div>

<div class="alert alert-success">
  <h4><i class="fa-solid fa-fw fa-lightbulb" aria-hidden="true"></i> Recuerda</h4>
  <p class="mb-0">En la comunicación asistencial, el <strong>profesional emisor es siempre el responsable</strong> de conocer las características de su perceptor y adecuar la codificación del mensaje para lograr una comunicación eficaz.</p>
</div>
"""

# 08_u2_la_lectura.html
files["08_u2_la_lectura.html"] = """---
tipo: pagina
nombre: "2. La Lectura: Dossier Teórico, Infografías, Glosario y FAQs (Unidad 2)"
seccion: "Unidad 2: Comunicación, Trabajo en Equipo y Liderazgo"
finalizacion: ver
restricciones:
  completar:
    - 07_u2_la_clase.html
---

<h3><i class="fa-solid fa-fw fa-book-open" aria-hidden="true"></i> 2. La Lectura: Comunicación, Equipos Interdependientes y Liderazgo</h3>
<p><span class="badge badge-primary">Etapa 2 del Modelo Tripartito</span> <span class="badge badge-success">Lecturas Mediadas + 2 Infografías NotebookLM</span></p>
<p class="lead">Explorá las tres lecturas fundamentales de la Unidad 2, analizá las dos infografías generadas en NotebookLM y consultá el glosario y las preguntas frecuentes sobre conducción de equipos en salud.</p>

<h3>Infografía 2.1: El Proceso de Comunicación y Equipos en Salud</h3>
<p><img src="img/u2_infografia_01_comunicacion_y_equipos.png" alt="Infografía Unidad 2: Proceso de comunicación Emisor-Perceptor y diferencias entre grupo y equipo en salud" class="img-fluid rounded-lg mb-3"></p>

<h3>Síntesis de las 3 Lecturas Didácticas de la Unidad 2</h3>
<div class="row">
  <div class="col-md-4 mb-3">
    <div class="card">
      <div class="card-body">
        <h4 class="card-title">Lectura 2.1: Imponderables y Perceptor</h4>
        <p class="card-text">En salud \\(2 + 2 \\neq 4\\) por la presencia constante de imponderables. El interlocutor humano no es un receptor mecánico sino un <strong>perceptor activo</strong> que decodifica según su edad, cultura, vivencias y emociones. El emisor es responsable de adecuar el mensaje.</p>
      </div>
    </div>
  </div>
  <div class="col-md-4 mb-3">
    <div class="card">
      <div class="card-body">
        <h4 class="card-title">Lectura 2.2: Equipo vs. Grupo y Quirófano</h4>
        <p class="card-text">Mientras el grupo surge por afinidad y responde individualmente, el <strong>equipo de trabajo</strong> integra habilidades complementarias con responsabilidad colectiva. El <strong>quirófano</strong> es el paradigma donde cirujano, anestesiólogo, instrumentador y enfermería actúan en sinergia total.</p>
      </div>
    </div>
  </div>
  <div class="col-md-4 mb-3">
    <div class="card">
      <div class="card-body">
        <h4 class="card-title">Lectura 2.3: Liderazgo Situacional y Maslow</h4>
        <p class="card-text">Liderar es persuadir e inspirar sin coerción, adaptando el estilo a la situación. Exige <strong>empatía genuina</strong> (sin caer en permisividad), reconocimiento de necesidades superiores (Maslow) y evitar la autocracia, la impulsividad y la falta de escucha.</p>
      </div>
    </div>
  </div>
</div>

<h3>Infografía 2.2: Liderazgo Situacional en el Sector Salud</h3>
<p><img src="img/u2_infografia_02_liderazgo_situacional.png" alt="Infografía Unidad 2: Liderazgo situacional en salud, empatía genuina, Maslow y causas de fracaso" class="img-fluid rounded-lg mb-3"></p>

<h3><i class="fa-solid fa-fw fa-download" aria-hidden="true"></i> Carpeta Temática de Lecturas Descargables — Unidad 2</h3>
<div class="card border-primary mb-3">
  <div class="card-body">
    <h4 class="card-title text-primary">Repositorio Documental: Comunicación, Equipos y Liderazgo</h4>
    <p class="card-text">Descargá las tres lecturas completas y las diapositivas oficiales organizadas en la carpeta temática de la Unidad 2:</p>
    <ul class="mb-0">
      <li><a href="lecturas/unidad_2/lectura_2_1_talento_humano_imponderables_y_comunicacion.docx" target="_blank">Lectura 2.1: Gestión del Talento Humano, Imponderables y Comunicación (DOCX)</a></li>
      <li><a href="lecturas/unidad_2/lectura_2_2_trabajo_en_equipo_vs_grupo_y_quirofano.docx" target="_blank">Lectura 2.2: Trabajo en Equipo vs. Grupo y el Paradigma del Quirófano (DOCX)</a></li>
      <li><a href="lecturas/unidad_2/lectura_2_3_liderazgo_situacional_empatia_y_maslow.docx" target="_blank">Lectura 2.3: Liderazgo Situacional, Empatía Genuina y Pirámide de Maslow (DOCX)</a></li>
      <li><a href="diapositivas/u2_diapositivas_comunicacion_liderazgo.pdf" target="_blank">Diapositivas de Cátedra Unidad 2: Gestión del Talento Humano en Salud (PDF)</a></li>
    </ul>
  </div>
</div>

<h3><i class="fa-solid fa-fw fa-book" aria-hidden="true"></i> Glosario Terminológico de la Unidad 2</h3>
<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Término Clave</th>
      <th scope="col">Definición Académica Aplicada en Salud</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Imponderables (\\(2+2 \\neq 4\\))</strong></td>
      <td>Contingencias emocionales, humanas y clínicas no previsibles que obligan a adaptar con flexibilidad la planificación sanitaria.</td>
    </tr>
    <tr>
      <td><strong>Perceptor Activo</strong></td>
      <td>Sujeto humano que percibe, filtra y decodifica el mensaje desde sus condicionantes socioculturales, etarios y emocionales.</td>
    </tr>
    <tr>
      <td><strong>Comunicación Eficaz</strong></td>
      <td>Convergencia comunicativa en la cual el perceptor interpreta el mensaje con la misma intención con que lo codificó el emisor.</td>
    </tr>
    <tr>
      <td><strong>Equipo de Trabajo</strong></td>
      <td>Conjunto de profesionales con especialidades complementarias, meta común y responsabilidad solidariamente compartida.</td>
    </tr>
    <tr>
      <td><strong>Liderazgo Situacional</strong></td>
      <td>Capacidad de guiar, motivar e influir por convicción (sin fuerza ni coerción), adecuando el estilo al contexto y al equipo.</td>
    </tr>
    <tr>
      <td><strong>Empatía Genuina vs. Permisividad</strong></td>
      <td>La empatía comprende la realidad del colaborador para decidir con justicia manteniendo la meta; la permisividad cede a todo y pierde la conducción.</td>
    </tr>
  </tbody>
</table>

<h3><i class="fa-solid fa-fw fa-circle-question" aria-hidden="true"></i> Preguntas Frecuentes (FAQs) sobre Comunicación y Liderazgo</h3>
<div class="card bg-light mb-3">
  <div class="card-body">
    <h4 class="card-title">1. Si un paciente o familiar no comprende una indicación médica, ¿de quién es la responsabilidad?</h4>
    <details>
      <summary>Ver respuesta fundamentada</summary>
      <p class="mt-2 mb-0">La responsabilidad recae siempre en el <strong>emisor (el profesional de la salud)</strong>. Como especialistas, debemos evaluar la edad, el nivel de instrucción y el estado emocional del perceptor para adecuar el código y verificar su comprensión.</p>
    </details>
  </div>
</div>
<div class="card bg-light mb-3">
  <div class="card-body">
    <h4 class="card-title">2. ¿Por qué un líder que fue exitoso en una emergencia quirúrgica puede fracasar al dirigir un servicio clínico?</h4>
    <details>
      <summary>Ver respuesta fundamentada</summary>
      <p class="mt-2 mb-0">Porque el liderazgo es <strong>situacional</strong>. Una determinación directiva rápida es vital en una urgencia intraoperatoria, pero si ese líder mantiene un estilo autocrático, sin escucha ni consenso en la gestión diaria del servicio, generará frustración y resistencia.</p>
    </details>
  </div>
</div>
<div class="card bg-light mb-3">
  <div class="card-body">
    <h4 class="card-title">3. ¿Cómo se aplica la empatía cuando un integrante del equipo atraviesa una crisis personal grave?</h4>
    <details>
      <summary>Ver respuesta fundamentada</summary>
      <p class="mt-2 mb-0">El líder empático dialoga con honestidad y puede reasignar temporalmente sus tareas críticas a otro colega hasta que se estabilice, dejándole claro que no está siendo desplazado sino cuidado en pos del equipo y del paciente.</p>
    </details>
  </div>
</div>
"""

# 09_u2_la_practica.html
files["09_u2_la_practica.html"] = """---
tipo: pagina
nombre: "3. La Práctica: Desafíos Interactivos, Caso UTI y Rúbrica (Unidad 2)"
seccion: "Unidad 2: Comunicación, Trabajo en Equipo y Liderazgo"
finalizacion: ver
restricciones:
  completar:
    - 08_u2_la_lectura.html
---

<h3><i class="fa-solid fa-fw fa-puzzle-piece" aria-hidden="true"></i> 3. La Práctica: Comunicación, Equipos y Liderazgo en Acción</h3>
<p><span class="badge badge-primary">Etapa 3 del Modelo Tripartito</span> <span class="badge badge-success">Conecta Bloques + Trivia + Caso UTI</span></p>

<div class="alert alert-warning">
  <h4><i class="fa-solid fa-fw fa-triangle-exclamation" aria-hidden="true"></i> Importante: Consigna Orientadora Obligatoria</h4>
  <p class="mb-0">Esta actividad práctica se resuelve integrando los conceptos de la videoclase magistral de la Lic. Carla Nani, el video short microlearning y las tres lecturas teóricas de la Unidad 2. Analizá el proceso de comunicación reconociendo al interlocutor como un <strong>perceptor activo</strong> y evaluá la dinámica de tu servicio bajo el <strong>paradigma del quirófano</strong> y el <strong>liderazgo situacional</strong>.</p>
</div>

<h3>Ficha de Desafíos Interactivos de la Unidad 2</h3>
<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Desafío</th>
      <th scope="col">Objetivo de Aprendizaje</th>
      <th scope="col">Modalidad en el Aula</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Conecta Bloques (8 pares)</strong></td>
      <td>Unir los 8 conceptos clave de la Unidad 2 (Factor humano \\(2+2 \\neq 4\\), Emisor, Perceptor, Equipo, Grupo, Quirófano, Liderazgo Situacional y Empatía) con sus definiciones.</td>
      <td>Actividad interactiva de emparejamiento / Paquete SCORM <code>u2_conecta_bloques_SCORM.zip</code></td>
    </tr>
    <tr>
      <td><strong>2. Trivia Gamificada Unidad 2</strong></td>
      <td>Superar 10 situaciones prácticas sobre comunicación asertiva, equipos y causas de fracaso directivo sin numeración rígida.</td>
      <td>Cuestionario formativo con intentos ilimitados / Paquete SCORM <code>u2_trivia_SCORM.zip</code></td>
    </tr>
    <tr>
      <td><strong>3. Caso Situado en UTI</strong></td>
      <td>Resolver una crisis de comunicación en el pase de guardia y liderazgo autocrático en Terapia Intensiva.</td>
      <td>Análisis situado con rúbrica de evaluación de 3 criterios.</td>
    </tr>
  </tbody>
</table>

<h3>Caso Situado de Gestión Hospitalaria: Falla Comunicacional y Liderazgo Autocrático en UTI</h3>
<div class="card border-primary mb-3">
  <div class="card-body">
    <h4 class="card-title text-primary">Escenario Clínico-Institucional</h4>
    <p class="card-text">En la Unidad de Terapia Intensiva (UTI) se registraron cuatro eventos adversos vinculados a la entrega de guardia en el último mes. El Jefe de Servicio ejerce un estilo <strong>autocrático e impulsivo</strong>: impone directivas sin escuchar a enfermería ni a los residentes. Durante el pase de sala emite indicaciones rápidas con siglas ambiguas sin corroborar cómo las decodifican los residentes de primer año (tratándolos como receptores pasivos en vez de <strong>perceptores</strong>). Ante el último evento adverso, sancionó individualmente al residente saliente, quebrando la cohesión del servicio.</p>
    <details>
      <summary>Ver guía de resolución sugerida</summary>
      <p class="mt-2 mb-0"><strong>Claves de intervención:</strong> 1) Reformular el pase de guardia desde la responsabilidad del emisor, verificando la decodificación de cada perceptor. 2) Migrar de la lógica de grupo fragmentado (culpa individual) a la de equipo interdependiente como el quirófano (responsabilidad compartida y respaldo mutuo). 3) Adoptar un liderazgo situacional que escuche activamente, delegue con formación y empodere según las necesidades de pertenencia y estima (Maslow).</p>
    </details>
  </div>
</div>

<h3>Rúbrica Analítica de Evaluación del Caso (Unidad 2)</h3>
<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Criterio</th>
      <th scope="col">Excelente (4 pts)</th>
      <th scope="col">Satisfactorio (3 pts)</th>
      <th scope="col">En Proceso (2 pts)</th>
      <th scope="col">Inicial (1 pt)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Esquema Emisor-Perceptor</strong></td>
      <td>Fundamenta la diferencia entre receptor y perceptor, identifica los condicionantes de los residentes y asigna la responsabilidad comunicacional al emisor.</td>
      <td>Reconoce el rol del perceptor y propone mejoras en la claridad del pase de guardia.</td>
      <td>Menciona problemas de comunicación general sin aplicar las categorías de codificación, decodificación y condicionantes.</td>
      <td>Trata la comunicación como una transmisión mecánica unidireccional.</td>
    </tr>
    <tr>
      <td><strong>2. Transición de Grupo a Equipo (Quirófano)</strong></td>
      <td>Aplica el paradigma del quirófano para restituir la complementariedad interdisciplinaria y la corresponsabilidad colectiva en la UTI.</td>
      <td>Distingue grupo de equipo y sugiere integrar a enfermería y residentes en la toma de decisiones.</td>
      <td>Define teóricamente al equipo pero mantiene un enfoque de responsabilidad exclusivamente individual.</td>
      <td>Convalida la fragmentación del servicio y el castigo aislado.</td>
    </tr>
    <tr>
      <td><strong>3. Liderazgo Situacional y Prevención del Fracaso</strong></td>
      <td>Diagnostica las causas de fracaso (autocracia, falta de escucha, impulsividad) y diseña un plan basado en empatía genuina y Pirámide de Maslow.</td>
      <td>Identifica los errores del jefe y propone incorporar escucha activa y delegación progresiva.</td>
      <td>Critica el autoritarismo del jefe pero propone soluciones permisivas que diluyen la conducción.</td>
      <td>No aplica los principios del liderazgo situacional ni la motivación del talento humano.</td>
    </tr>
  </tbody>
</table>
"""

# 10_u2_conecta_bloques_y_trivia.md
files["10_u2_conecta_bloques_y_trivia.md"] = """---
tipo: cuestionario
nombre: "Práctica Gamificada Unidad 2: Conecta Bloques y Trivia de Comunicación y Liderazgo"
seccion: "Unidad 2: Comunicación, Trabajo en Equipo y Liderazgo"
intentos: ilimitados
mezclar_respuestas: true
finalizacion: calificar
restricciones:
  completar:
    - 09_u2_la_practica.html
preguntas:
  - tipo: emparejamiento
    enunciado: "Conecta Bloques Unidad 2: Empareja cada uno de los 8 conceptos centrales expuestos por la Lic. Carla Nani con su definición en la gestión del talento humano en salud."
    parejas:
      - pregunta: '**Premisa del Factor Humano (\(2+2 \neq 4\))**'
        respuesta: "Principio de que los imponderables y factores emocionales impiden fórmulas estáticas en gestión."
      - pregunta: "**Emisor Asistencial**"
        respuesta: "Actor responsable de codificar activamente el mensaje adaptándolo a las características de su interlocutor."
      - pregunta: "**Perceptor Activo**"
        respuesta: "Interlocutor que decodifica e interpreta la información según su edad, vivencias y condicionantes."
      - pregunta: "**Equipo de Trabajo**"
        respuesta: "Conjunto de personas con habilidades complementarias, metas compartidas y responsabilidad colectiva."
      - pregunta: "**Grupo de Trabajo**"
        respuesta: "Agrupación basada en afinidades o tareas similares donde la responsabilidad es estrictamente individual."
      - pregunta: "**Modelo del Quirófano**"
        respuesta: "Paradigma de equipo asistencial interdependiente con roles coordinados y metas comunes."
      - pregunta: "**Liderazgo Situacional**"
        respuesta: "Capacidad de guiar, motivar e influir sin coerción, adaptando el estilo según la coyuntura."
      - pregunta: "**Empatía Genuina**"
        respuesta: "Competencia de comprender la perspectiva del otro para decidir asertivamente, sin caer en permisividad."
    retro: "¡Excelente! Conectaste con precisión los 8 pilares de la comunicación, el trabajo en equipo y el liderazgo situacional."

  - tipo: opcion_multiple
    enunciado: '¿Qué expresa la premisa «en la gestión de personas \(2+2\) nunca es \(4\)» sostenida por la Lic. Carla Nani?'
    opciones:
      - texto: "Que el comportamiento humano está sujeto a imponderables y factores emocionales que alteran lo previsto y exigen adaptabilidad rápida."
        correcta: true
        retro: "¡Correcto! A diferencia de las ciencias exactas, al trabajar con personas siempre intervienen imponderables."
      - texto: "Que los registros estadísticos del hospital suelen tener errores numéricos."
        retro: "Incorrecto. Es una metáfora sobre la complejidad e imprevisibilidad de la conducta humana."
      - texto: "Que siempre faltan recursos materiales en la guardia."
        retro: "Incorrecto."
      - texto: "Que las decisiones en recursos humanos se toman al azar."
        retro: "Incorrecto. Se planifica estratégicamente, pero con flexibilidad para adaptarse a los imprevistos."
    retro: "Reconocer la existencia de imponderables es indispensable para dirigir equipos de salud con flexibilidad."

  - tipo: opcion_multiple
    enunciado: "En el proceso de comunicación humana en salud, ¿por qué se utiliza el término **Perceptor** en lugar de receptor?"
    opciones:
      - texto: "Porque el ser humano no reproduce pasivamente el mensaje como un buzón de voz, sino que lo percibe, filtra y decodifica desde sus condicionantes."
        correcta: true
        retro: "¡Exacto! Un receptor es un aparato mecánico; una persona es siempre un perceptor activo."
      - texto: "Porque es un término técnico reservado únicamente para pacientes internados."
        retro: "Incorrecto. Todo interlocutor humano (colega, jefe, paciente o familiar) es un perceptor."
      - texto: "Porque el perceptor es quien inicia la emisión del mensaje."
        retro: "Incorrecto. Quien inicia y codifica el mensaje es el emisor."
      - texto: "Porque en los hospitales no se utiliza el lenguaje escrito."
        retro: "Incorrecto."
    retro: "El perceptor interpreta el mensaje atravesado por su edad, nivel sociocultural, vivencias y estado emocional."

  - tipo: opcion_multiple
    enunciado: "¿Quién tiene la responsabilidad principal de lograr que la comunicación asistencial sea eficaz?"
    opciones:
      - texto: "El emisor (profesional de la salud), quien debe identificar las características de su perceptor y adecuar la codificación del mensaje."
        correcta: true
        retro: "¡Muy bien! No podemos dar el mismo discurso lleno de tecnicismos a todas las personas por igual."
      - texto: "El paciente o familiar, quien tiene la obligación de entender terminología médica compleja."
        retro: "Incorrecto. La responsabilidad ética y comunicacional recae en el profesional especialista."
      - texto: "El personal administrativo de la mesa de entradas."
        retro: "Incorrecto."
      - texto: "Nadie, ya que la interpretación depende del azar."
        retro: "Incorrecto."
    retro: "El mensaje es eficaz únicamente cuando el perceptor lo comprende con la misma intención con que lo emitió el profesional."

  - tipo: opcion_multiple
    enunciado: "¿Cuál es la diferencia estructural entre un **Equipo de Trabajo** y un **Grupo de Trabajo**?"
    opciones:
      - texto: "En el equipo existen habilidades complementarias, cohesión y responsabilidad colectiva por las decisiones; en el grupo la responsabilidad es individual."
        correcta: true
        retro: "¡Correcto! En un equipo las distintas especialidades se complementan y respaldan mutuamente."
      - texto: "En el grupo todos tienen distintas profesiones y en el equipo todos hacen exactamente la misma tarea."
        retro: "Incorrecto. Es al revés: en el grupo suelen tener formación similar y en el equipo son complementarios."
      - texto: "El equipo se forma por afinidad amistosa para salir fuera del horario laboral."
        retro: "Incorrecto. La afinidad social espontánea es característica de los grupos."
      - texto: "No existe ninguna diferencia entre ambos conceptos."
        retro: "Incorrecto."
    retro: "Un equipo asistencial persigue una meta común (explícita o implícita) asumiendo corresponsabilidad por el resultado."

  - tipo: opcion_multiple
    enunciado: "¿Por qué el **Quirófano** es considerado el modelo paradigmático de equipo de trabajo?"
    opciones:
      - texto: "Porque integra diversas especialidades (cirujano, anestesiólogo, instrumentador, enfermería, limpieza) donde cada uno cumple su rol sincronizadamente tras el bienestar del paciente."
        correcta: true
        retro: "¡Exacto! En el quirófano las jerarquías formales se dinamizan en función del rol experto de cada miembro."
      - texto: "Porque allí todos los integrantes tienen el mismo título universitario."
        retro: "Incorrecto. Su riqueza radica justamente en la complementariedad de saberes distintos."
      - texto: "Porque los profesionales del quirófano se eligen por amistad personal."
        retro: "Incorrecto."
      - texto: "Porque en el quirófano nadie asume responsabilidad por las decisiones."
        retro: "Incorrecto. Todos se responsabilizan solidariamente por sacar adelante al paciente."
    retro: "En los equipos quirúrgicos consolidados, incluso una sola mirada (comunicación no verbal) basta para coordinar acciones complejas."

  - tipo: opcion_multiple
    enunciado: "¿Cómo se define el **Liderazgo Situacional** en el ámbito de la salud?"
    opciones:
      - texto: "La capacidad de guiar, motivar e influir mediante la persuasión y convicción (sin fuerza ni coerción), adaptando el estilo según las demandas de cada situación."
        correcta: true
        retro: "¡Correcto! El líder positivo persuade con el ejemplo y la palabra, y se adapta con flexibilidad al contexto."
      - texto: "La imposición de autoridad mediante gritos, sanciones y miedo."
        retro: "Incorrecto. El uso de la coerción corresponde al autoritarismo y conduce al fracaso."
      - texto: "Actuar siempre de manera idéntica sin importar si es una urgencia o una reunión de planificación."
        retro: "Incorrecto. La falta de flexibilidad situacional hace fracasar al líder."
      - texto: "Esconder información para volverse indispensable en el servicio."
        retro: "Incorrecto. El líder positivo no es egoísta: comparte saberes y empodera a su equipo."
    retro: "Un líder situacional sabe cuándo tomar una decisión rápida en una urgencia y cuándo construir consenso participativo."

  - tipo: opcion_multiple
    enunciado: "¿Cuál es la diferencia fundamental entre la **Empatía Genuina** y la **Permisividad** en un líder?"
    opciones:
      - texto: "La empatía comprende la situación que atraviesa el colaborador para tomar decisiones justas sin perder el objetivo; la permisividad dice que sí a todo y destruye la autoridad."
        correcta: true
        retro: "¡Muy bien! Ponerse en el lugar del otro no significa renunciar a la conducción ni a los estándares del servicio."
      - texto: "Ser empático significa perdonar cualquier incumplimiento sin poner límites nunca."
        retro: "Incorrecto. Eso es permisividad."
      - texto: "Ser empático implica ignorar los problemas emocionales del personal."
        retro: "Incorrecto. La falta de empatía e insensibilidad es una causa directa de fracaso."
      - texto: "Son sinónimos en la gestión de recursos humanos."
        retro: "Incorrecto."
    retro: "El líder empático acompaña y reacomoda transitoriamente al colaborador que pasa por un mal momento, cuidando tanto a la persona como al equipo."

  - tipo: opcion_multiple
    enunciado: "Vinculando el liderazgo con la **Pirámide de Maslow**, ¿qué necesidades superiores debe reconocer y estimular un buen líder en su equipo?"
    opciones:
      - texto: "Las necesidades de pertenencia al equipo, reconocimiento explícito de sus logros, estima y desarrollo profesional continuo."
        correcta: true
        retro: "¡Exacto! El ser humano necesita sentirse parte valorada del equipo y crecer profesionalmente."
      - texto: "Únicamente las necesidades fisiológicas básicas de alimentación."
        retro: "Incorrecto. El liderazgo efectivo moviliza los escalones superiores de motivación y autorrealización."
      - texto: "La necesidad de trabajar aislado sin comunicarse con sus pares."
        retro: "Incorrecto."
      - texto: "La necesidad de evitar cualquier tipo de responsabilidad."
        retro: "Incorrecto. El buen líder empodera delegando responsabilidades acordes a las capacidades."
    retro: "Reconocer las fortalezas de cada integrante y delegar con confianza impulsa el crecimiento de todo el servicio."

  - tipo: opcion_multiple
    enunciado: "¿Cuáles de las siguientes conductas constituyen **causas comunes de fracaso de un líder** en salud?"
    opciones:
      - texto: "No escuchar al equipo, tomar decisiones impulsivas, incapacidad para delegar, autoritarismo, rigidez ante el cambio y falta de honestidad."
        correcta: true
        retro: "¡Correcto! Todas estas actitudes erosionan el respeto profesional y desarticulan al equipo."
      - texto: "Capacitarse continuamente y fomentar el desarrollo académico de los residentes."
        retro: "Incorrecto. La actualización permanente fortalece la legitimidad del líder."
      - texto: "Resolver los conflictos mediante el diálogo y la escucha activa."
        retro: "Incorrecto. Esa es una competencia esencial del líder positivo."
      - texto: "Adaptarse con flexibilidad a los imponderables de la guardia."
        retro: "Incorrecto."
    retro: "Un líder 'chato' (que no se actualiza), autocrático o que incumple su palabra pierde rápidamente la confianza de sus pares."

  - tipo: opcion_multiple
    enunciado: "¿Por qué es tan relevante la **comunicación no verbal** durante la interacción con pacientes, familiares y colegas?"
    opciones:
      - texto: "Porque los gestos, la postura y la mirada transmiten contención, actitud e información clave que nos permite saber si estamos llegando adecuadamente al otro."
        correcta: true
        retro: "¡Exacto! En el trabajo con personas, lo gestual habla tanto o más que las palabras."
      - texto: "Porque reemplaza la obligación de escribir la historia clínica."
        retro: "Incorrecto."
      - texto: "Porque no tiene ningún efecto en la percepción del paciente."
        retro: "Incorrecto. El perceptor decodifica constantemente los gestos del profesional."
      - texto: "Porque solo se utiliza cuando no funciona el micrófono."
        retro: "Incorrecto."
    retro: "La coherencia entre lo que decimos verbalmente y nuestra actitud corporal es indispensable para construir confianza asistencial."
---

Resolvé la actividad interactiva **Conecta Bloques** (pregunta de emparejamiento de 8 pares) y las **10 situaciones de la Trivia Gamificada** de la Unidad 2. Disponés de intentos ilimitados con retroalimentación inmediata.
"""

# 11_cierre_encabezado.html
files["11_cierre_encabezado.html"] = """---
tipo: etiqueta
nombre: "Cierre y Certificación: Sistema de Doble Candado (Circular N° 5)"
seccion: "Evaluación Final Integradora y Certificación"
finalizacion: manual
---

<p><img src="img/banner_cierre_evaluacion.png" alt="Banner de Evaluación Final Integradora y Certificación de 30 Horas" class="img-fluid rounded-lg mb-3"></p>

<h3><i class="fa-solid fa-fw fa-star" aria-hidden="true"></i> Evaluación Final Integradora y Certificación Oficial (30 Horas Reloj)</h3>
<p><span class="badge badge-warning">Sistema de Doble Candado Automatizado</span> <span class="badge badge-primary">Circular N° 5 ESALUD</span></p>

<div class="alert alert-warning">
  <h4><i class="fa-solid fa-fw fa-list-check" aria-hidden="true"></i> Requisitos de Acreditación y Desbloqueo del Certificado</h4>
  <ul class="mb-0">
    <li><strong>Condición Preliminar (Candado Académico):</strong> Haber completado las actividades de lectura y práctica gamificada de la Unidad 1 y la Unidad 2.</li>
    <li><strong>Condición 1 (Examen Final Integrador):</strong> Aprobar el cuestionario sumativo integrador de 16 casos clínico-institucionales con una calificación <strong>mayor o igual al 70%</strong> (máximo 2 intentos permitidos, computándose la nota más alta).</li>
    <li><strong>Condición 2 (Encuesta de Calidad Educativa):</strong> Completar la encuesta institucional obligatoria de satisfacción y mejora continua para habilitar la descarga automática del Certificado Oficial por <strong>30 Horas Reloj</strong>.</li>
  </ul>
</div>
"""

# 12_examen_final_integrador.md
files["12_examen_final_integrador.md"] = """---
tipo: cuestionario
nombre: "Examen Final Sumativo Integrador (Unidades 1 y 2)"
seccion: "Evaluación Final Integradora y Certificación"
tiempo_limite: 45
intentos: 2
mezclar_respuestas: true
finalizacion: calificar
restricciones:
  completar:
    - 05_u1_conecta_bloques_y_trivia.md
    - 10_u2_conecta_bloques_y_trivia.md
preguntas:
  - tipo: opcion_multiple
    enunciado: "Un residente de segundo año asume la coordinación de las guardias de fin de semana. Advierte que los pases de sala son desordenados porque cada profesional reporta datos según su criterio individual, derivando en omisiones farmacológicas. La Misión del hospital destaca la «seguridad del paciente», pero no existen actividades estandarizadas en el HACER ni pautas de comunicación. ¿Cuál es la intervención prioritaria?"
    opciones:
      - texto: "Alinear el HACER con el SER mediante la estandarización de actividades (lista de verificación de pase de guardia) y capacitar al emisor en comunicación eficaz."
        correcta: true
        retro: "Correcto. Articula el propósito ético del SER con la estandarización operativa del HACER y la responsabilidad comunicacional del emisor."
      - texto: "Aplicar sanciones económicas a los residentes sin modificar los procesos del servicio."
        retro: "Incorrecto. El enfoque puramente punitivo no resuelve la desarticulación del HACER."
      - texto: "Cambiar la Visión del hospital en el Boletín Oficial sin intervenir en la guardia."
        retro: "Incorrecto. El problema radica en la falta de alineación operativa con el SER ya declarado."
      - texto: "Solicitar que los familiares transcriban las indicaciones médicas."
        retro: "Incorrecto."
    retro: "La gestión estratégica exige coherencia entre los valores del SER y las actividades estandarizadas del HACER."

  - tipo: opcion_multiple
    enunciado: "En un Centro de Salud, los médicos, enfermeros y trabajadores sociales atienden en consultorios contiguos pero sin intercambiar información. Ante un brote epidemiológico barrial no logran coordinar las visitas domiciliarias. Aplicando el paradigma del **Quirófano** (Lic. Carla Nani), ¿qué transformación debe impulsar la coordinación?"
    opciones:
      - texto: "Transformar el grupo en un equipo interdependiente, articulando sus especialidades complementarias y asumiendo responsabilidad compartida por la meta sanitaria común."
        correcta: true
        retro: "Correcto. El modelo del quirófano demuestra cómo saberes distintos actúan con cohesión y corresponsabilidad hacia un mismo objetivo."
      - texto: "Mantener el trabajo fragmentado para que cada profesional responda solo por su planilla individual."
        retro: "Incorrecto. Eso perpetúa la lógica de grupo aislado."
      - texto: "Exigir que todos los profesionales realicen exactamente la misma tarea administrativa."
        retro: "Incorrecto. Anularía la riqueza de las habilidades complementarias."
      - texto: "Cerrar los consultorios de trabajo social y enfermería."
        retro: "Incorrecto."
    retro: "Un equipo de salud supera la suma individual gracias a la complementariedad de roles y la cohesión."

  - tipo: opcion_multiple
    enunciado: "Durante una cirugía compleja, la instrumentadora advierte que un insumo presenta una falla de esterilización y alerta de inmediato en voz clara al cirujano jefe, quien detiene la maniobra, agradece la advertencia y reemplaza el material. ¿Qué dinámica se observa en esta escena?"
    opciones:
      - texto: "Un equipo de trabajo cohesivo donde las jerarquías formales se dinamizan en favor del rol experto de cada miembro y la seguridad del paciente."
        correcta: true
        retro: "Correcto. En un verdadero equipo quirúrgico cada integrante domina su faceta y la meta común prima sobre la rigidez jerárquica."
      - texto: "Una falta grave a la cadena de mando que debería sancionarse administrativamente."
        retro: "Incorrecto."
      - texto: "Una cultura de tipo Mercado basada en la competencia interna."
        retro: "Incorrecto."
      - texto: "Un grupo social formado por afinidad recreativa."
        retro: "Incorrecto."
    retro: "En el equipo interdependiente la decisión técnica oportuna es respaldada por todo el colectivo."

  - tipo: opcion_multiple
    enunciado: "Una médica residente debe explicar un diagnóstico complejo y el tratamiento al alta a un paciente rural de 78 años que se encuentra ansioso y con dificultades auditivas. Si aplica el esquema comunicacional de la Lic. Carla Nani, ¿cómo debe proceder?"
    opciones:
      - texto: "Asumir su responsabilidad como emisora, reconocer los condicionantes etarios, culturales y emocionales de su perceptor, y codificar el mensaje con lenguaje claro, pausado y empático."
        correcta: true
        retro: "Correcto. El emisor especialista es quien debe adecuarse a las características de su perceptor para que la comunicación sea eficaz."
      - texto: "Entregarle un folleto impreso en jerga médica técnica, ya que como profesional siempre explica todo de la misma manera."
        retro: "Incorrecto. Dar el mismo mensaje estandarizado sin contemplar al perceptor impide la comunicación eficaz."
      - texto: "Culpar al paciente si no comprende los tecnicismos biomédicos."
        retro: "Incorrecto."
      - texto: "Evitar el contacto visual y limitarse a cargar los datos en la computadora."
        retro: "Incorrecto. Descuida tanto la adaptación al perceptor como la comunicación no verbal."
    retro: "En salud no existen receptores mecánicos pasivos; cada paciente y familiar es un perceptor activo."

  - tipo: opcion_multiple
    enunciado: "Un hospital público cuenta con su Misión, Visión y Principios Rectores publicados por Resolución Ministerial (el SER). Sin embargo, en el Servicio de Clínica Médica predomina el maltrato verbal en los pases de guardia, el ocultamiento de errores por miedo y una alta rotación de residentes. ¿Cuál es el diagnóstico institucional correcto?"
    opciones:
      - texto: "Existe una fractura entre el SER formal declarado y el ESTAR cotidiano, manifestada en un clima laboral tóxico que deteriora el bienestar y la productividad asistencial."
        correcta: true
        retro: "Correcto. Un clima negativo y hostil en el ESTAR contradice los principios rectores y compromete la calidad de atención."
      - texto: "El hospital no necesita gestionar su clima laboral porque ya tiene su Misión escrita en el Boletín Oficial."
        retro: "Incorrecto. La declaración formal no basta si no se vive en la cultura y el clima diario."
      - texto: "El servicio presenta una cultura tipo Clan altamente saludable."
        retro: "Incorrecto."
      - texto: "Es un problema exclusivamente contable de las funciones de apoyo."
        retro: "Incorrecto."
    retro: "La gestión estratégica debe alinear el SER, el HACER y el ESTAR promoviendo un clima ético y saludable."

  - tipo: opcion_multiple
    enunciado: "En la clasificación funcional del vector del HACER (Dra. Susana Salomón), ¿cómo se articula el Servicio de Laboratorio Central y Mantenimiento con el Servicio de Internación Pediátrica?"
    opciones:
      - texto: "Internación Pediátrica cumple una función final (asistencial directa) y Laboratorio/Mantenimiento cumplen funciones intermedias o de apoyo indispensables para que aquella se realice."
        correcta: true
        retro: "Correcto. Las funciones de apoyo proveen el soporte técnico y diagnóstico necesario para las funciones finales."
      - texto: "Ambos servicios cumplen exclusivamente funciones administrativas de control horario."
        retro: "Incorrecto."
      - texto: "Laboratorio es una función final externa y Pediatría es una función de apoyo."
        retro: "Incorrecto."
      - texto: "No tienen ninguna relación funcional dentro de la estructura hospitalaria."
        retro: "Incorrecto. Las organizaciones de salud integran múltiples dominios técnicos y sociales interconectados."
    retro: "Reconocer el valor de las funciones de apoyo fortalece la integración interdisciplinaria en el hospital."

  - tipo: opcion_multiple
    enunciado: "Un nuevo Jefe de Servicio intenta implementar un protocolo innovador de telemedicina, pero fracasa porque solo se apoyó en el organigrama impreso sin consultar a los médicos de planta y enfermeros referentes a quienes todo el equipo escucha y respeta desde hace veinte años. ¿Qué elemento del vector del ESTAR ignoró?"
    opciones:
      - texto: "La cadena de mando real y los líderes naturales que sostienen la cultura del servicio."
        correcta: true
        retro: "Correcto. En toda organización coexiste la estructura formal con la cadena de mando real y las redes de influencia."
      - texto: "El control administrativo de licencias anuales."
        retro: "Incorrecto."
      - texto: "La liquidación de haberes del servicio de personal."
        retro: "Incorrecto."
      - texto: "El diseño arquitectónico de la fachada del hospital."
        retro: "Incorrecto."
    retro: "Analizar la estructura en el ESTAR exige comprender tanto el organigrama formal como los liderazgos reales del equipo."

  - tipo: opcion_multiple
    enunciado: "Un centro privado de diagnóstico por imágenes evalúa a sus profesionales exclusivamente por la cantidad de estudios facturados por hora, generando rivalidad entre colegas, falta de cooperación en casos dudosos y agotamiento emocional. ¿Qué tipología cultural predomina y cuál es su límite?"
    opciones:
      - texto: "Predomina la cultura de Mercado; su beneficio es el foco en resultados y rentabilidad, pero su límite es la competencia interna, la desmotivación y el desgaste del compromiso."
        correcta: true
        retro: "Correcto. La cultura de Mercado prioriza objetivos cuantitativos y competitividad, con alto riesgo de desgaste interpersonal."
      - texto: "Predomina la cultura tipo Clan familiar y colaborativa."
        retro: "Incorrecto."
      - texto: "Predomina la cultura Jerárquica sin metas de rentabilidad."
        retro: "Incorrecto."
      - texto: "Predomina la cultura de Adhocracia filantrópica."
        retro: "Incorrecto."
    retro: "Conocer los límites de cada tipología cultural permite equilibrar la eficiencia con el cuidado del talento humano."

  - tipo: opcion_multiple
    enunciado: "Durante una guardia nocturna ocurre una caída brusca del suministro eléctrico en un sector de internación y, simultáneamente, ingresa un politraumatismo grave. El equipo reconfigura de inmediato las camas y los roles sin esperar órdenes burocráticas. ¿Qué principio de la Unidad 2 explica esta situación?"
    opciones:
      - texto: "En salud «dos más dos nunca es cuatro»: los imponderables existen permanentemente y exigen adaptabilidad rápida, trabajo en equipo y liderazgo situacional."
        correcta: true
        retro: "Correcto. La presencia de imponderables obliga a contar con equipos flexibles capaces de reorganizarse en tiempo real."
      - texto: "Las organizaciones de salud son sistemas mecánicos exactos donde nunca ocurre nada fuera de lo programado."
        retro: "Incorrecto."
      - texto: "Ante un imponderable cada profesional debe actuar de forma aislada e individual."
        retro: "Incorrecto."
      - texto: "Solo la administración normativa de expedientes resuelve una emergencia clínica."
        retro: "Incorrecto."
    retro: "La adaptabilidad frente a los imponderables es una competencia central en la gestión de personas en salud."

  - tipo: opcion_multiple
    enunciado: "Una residente de tercer año nota que su compañero de primer año está cometiendo errores de concentración porque atraviesa la internación grave de su hijo. Decide cubrirle la realización de un procedimiento complejo hoy, dialoga con él en privado y acuerda cómo reorganizar sus tareas de la semana sin exponerlo ni humillarlo, manteniendo la calidad del servicio. ¿Qué competencia ejerció?"
    opciones:
      - texto: "Empatía genuina y liderazgo situacional positivo, comprendiendo el momento humano del colega para cuidar tanto al equipo como al paciente sin caer en permisividad."
        correcta: true
        retro: "Correcto. La empatía genuina se pone en el lugar del otro y reacomoda transitoriamente el trabajo con honestidad y responsabilidad."
      - texto: "Permisividad destructiva que arruina la disciplina hospitalaria."
        retro: "Incorrecto. La permisividad es ceder a todo sin criterio; aquí hubo una decisión consciente y temporal ante una crisis real."
      - texto: "Liderazgo autocrático y coercitivo."
        retro: "Incorrecto."
      - texto: "Desinterés por los objetivos asistenciales del servicio."
        retro: "Incorrecto."
    retro: "La Lic. Carla Nani destaca que correr temporalmente a un compañero que atraviesa un mal momento, acompañándolo hasta que se acomode, es propio de un gran líder."

  - tipo: opcion_multiple
    enunciado: "Un referente médico pretende que su equipo cumpla las nuevas guías clínicas mediante amenazas y gritos, se niega a escuchar las dificultades operativas que le plantean las enfermeras, toma decisiones impulsivas y nunca delega porque afirma que «nadie hace las cosas como yo». ¿Cuál es el pronóstico de su conducción?"
    opciones:
      - texto: "Fracasará como líder, ya que reúne las causas clásicas de fracaso: uso de coerción en vez de persuasión, falta de escucha, impulsividad e incapacidad para delegar."
        correcta: true
        retro: "Correcto. El liderazgo genuino se basa en la persuasión, la escucha activa, el diálogo y el empoderamiento del equipo."
      - texto: "Tendrá éxito duradero porque el estilo autocrático es el único válido en salud."
        retro: "Incorrecto."
      - texto: "Logrará empoderar a su equipo satisfaciendo las necesidades superiores de Maslow."
        retro: "Incorrecto. Su conducta frustra las necesidades de estima, pertenencia y autorrealización."
      - texto: "Fomentará una cultura de innovación y adhocracia participativa."
        retro: "Incorrecto."
    retro: "El líder que no escucha, no delega y no se adapta al contexto termina siendo superado y perdiendo el respaldo del equipo."

  - tipo: opcion_multiple
    enunciado: "En los hospitales coexisten profesionales de múltiples especialidades, técnicos, administrativos, personal de limpieza, mantenimiento y seguridad. ¿Cómo define la Dra. Susana Salomón a las instituciones de salud en función de esta característica?"
    opciones:
      - texto: "Organizaciones complejas con múltiples dominios sociales y técnicos donde coexisten diversos saberes, metas e identidades orientados a dar valor agregado a la salud."
        correcta: true
        retro: "Correcto. Esa multiplicidad de dominios exige desarrollar interdisciplinariedad y transdisciplinariedad."
      - texto: "Organizaciones simples y homogéneas con un único dominio técnico."
        retro: "Incorrecto."
      - texto: "Empresas exclusivamente financieras ajenas al contexto social."
        retro: "Incorrecto."
      - texto: "Estructuras estáticas inmunes a la innovación tecnológica."
        retro: "Incorrecto."
    retro: "Comprender los múltiples dominios sociales y técnicos del hospital es esencial para integrar a todo el personal en una cultura compartida."

  - tipo: opcion_multiple
    enunciado: "En el Servicio de Cirugía General los pases de guardia son breves, verticales y ejecutivos, mientras que en el Servicio de Medicina Interna del mismo hospital se realizan extensos ateneos deliberativos horizontales. ¿Cómo se denomina este fenómeno cultural?"
    opciones:
      - texto: "Coexistencia de subculturas hospitalarias (quirúrgica vs. clínica) dentro de una misma cultura organizacional, cada una con sus rituales, ritmos y códigos propios."
        correcta: true
        retro: "Correcto. Los grupos y especialidades desarrollan subculturas acorde a las exigencias específicas de su práctica."
      - texto: "Ausencia total de identidad institucional en el hospital."
        retro: "Incorrecto."
      - texto: "Falla administrativa del departamento de contaduría."
        retro: "Incorrecto."
      - texto: "Recepción mecánica pasiva del mensaje."
        retro: "Incorrecto."
    retro: "Las subculturas enriquecen a la institución siempre que permanezcan alineadas con la Misión y los Principios Rectores comunes."

  - tipo: opcion_multiple
    enunciado: "Según la aplicación de la **Pirámide de Maslow** en la gestión del talento humano (Lic. Carla Nani), ¿qué ocurre cuando un jefe de servicio reconoce públicamente el excelente desempeño de sus residentes y les delega responsabilidades acordes a su crecimiento?"
    opciones:
      - texto: "Satisface necesidades superiores de pertenencia, reconocimiento, estima y desarrollo profesional, empoderando e inspirando al equipo."
        correcta: true
        retro: "Correcto. El reconocimiento genuino y la delegación constructiva fortalecen la motivación intrínseca y el compromiso."
      - texto: "Pierde autoridad frente al equipo y fomenta la indisciplina."
        retro: "Incorrecto. El líder positivo no es egoísta: impulsa a los demás para que crezcan."
      - texto: "Actúa únicamente sobre el escalón fisiológico básico."
        retro: "Incorrecto."
      - texto: "Genera un clima laboral tóxico de competencia agresiva."
        retro: "Incorrecto."
    retro: "Un buen líder jamás esconde información ni teme que sus colaboradores brillen; los empodera en pos del equipo."

  - tipo: opcion_multiple
    enunciado: "Uno de los desafíos contemporáneos del contexto sanitario señalados en la Unidad 1 es la «pulverización por especialidades y subespecialidades». ¿Qué problema genera este fenómeno y cómo debe responder la gestión?"
    opciones:
      - texto: "Dificulta el abordaje integral e integrado del paciente; la gestión debe responder articulando el trabajo inter y transdisciplinario centrado en la persona."
        correcta: true
        retro: "Correcto. Frente a la hiperfragmentación del saber médico, la gestión y el trabajo en equipo reconstruyen la mirada integral del paciente."
      - texto: "Mejora automáticamente la comunicación sin necesidad de coordinar equipos."
        retro: "Incorrecto."
      - texto: "Se resuelve eliminando todas las especialidades médicas del hospital."
        retro: "Incorrecto."
      - texto: "Solo afecta a las áreas de mantenimiento edilicio."
        retro: "Incorrecto."
    retro: "Integrar saberes diversos en equipos cohesivos es la respuesta estratégica ante la fragmentación asistencial."

  - tipo: opcion_multiple
    enunciado: "De acuerdo con la **Circular N° 5** que regula este curso en el Campus Virtual ESALUD, ¿cómo opera el **Sistema de Doble Candado Automatizado** para obtener el Certificado Oficial de 30 Horas Reloj?"
    opciones:
      - texto: "Exige cumplir dos condiciones encadenadas: 1) Aprobar este Examen Final Integrador con calificación mayor o igual al 70%, y 2) Completar la Encuesta de Calidad Educativa."
        correcta: true
        retro: "¡Correcto! Cumplidas ambas condiciones, el campus habilita automáticamente la descarga del Certificado Oficial de 30 horas."
      - texto: "El certificado se emite solo con matricularse en el aula sin rendir evaluaciones."
        retro: "Incorrecto."
      - texto: "Requiere presentar un expediente impreso en papel en la oficina de personal."
        retro: "Incorrecto. Todo el proceso es 100% virtual y automatizado en Moodle."
      - texto: "Solo exige ver el primer video sin realizar las prácticas ni el examen final."
        retro: "Incorrecto."
    retro: "¡Felicitaciones por completar el Examen Final Integrador! Recordá completar a continuación la Encuesta de Calidad Educativa para desbloquear tu certificado."
---

**Evaluación Sumativa Final Integradora** del curso *Gestión de Personas y Talento Humano en Salud*. Consta de **16 casos integradores** sobre las Unidades 1 y 2. Se aprueba con el **70% o más** de respuestas correctas y disponés de **2 intentos**.
"""

for fname, text in files.items():
    (BASE_DIR / fname).write_text(text.strip() + "\n", encoding="utf-8")
    print(f"Created Moodle/Tiza file: {fname}")

# ==============================================================================
# GENERACIÓN DE PODCASTS EDUCATIVOS RIOPLATENSES (CLAUDEMY ENGINE + EDGE-TTS)
# ==============================================================================
print("\n" + "=" * 60)
print("  Generando Podcasts Pedagógicos de Unidad (Claudemy Engine)")
print("=" * 60)

MEDIA_DIR = BASE_DIR / "media"
SCORM_DIR = BASE_DIR / "scorm"
MEDIA_DIR.mkdir(parents=True, exist_ok=True)
SCORM_DIR.mkdir(parents=True, exist_ok=True)

# Guion Unidad 1: Cultura Organizacional y Gestión (Rioplatense, ~300 palabras)
U1_PODCAST_SCRIPT = """
A: Hola, te damos la bienvenida al podcast de la Unidad 1. Hoy nos metemos de lleno en una pregunta que incomoda: ¿por qué gestionar un hospital no tiene nada que ver con administrar papeles?
B: Tal cual, Elena. En la residencia o en la guardia médica muchas veces creemos que conducir es firmar planillas o controlar horarios, cuando en realidad estamos lidiando con personas en contextos críticos.
A: Exacto, Tomás. Y ahí entra lo que la doctora Susana Salomón define como los tres vectores de la identidad: el SER, el HACER y el ESTAR. Fijate que muchas instituciones tienen una Misión hermosa colgada en un cuadro, pero en el día a día las prioridades van por otro carril.
B: Claro, la famosa disociación entre el organigrama oficial y lo que pasa a las tres de la mañana en la urgencia. El organigrama formal dice una cosa, pero el equipo acude al referente real en el que confía.
A: Eso es el ESTAR cotidiano. Y por eso la regla de oro de esta unidad es innegociable: el SER, los valores éticos de la salud pública, no se negocian en un expediente burocrático; se defienden y se construyen en el ESTAR de cada guardia.
B: Fundamental para no perder el rumbo ético ni el compromiso con nuestros pacientes.
"""

# Guion Unidad 2: Comunicación y Liderazgo (Rioplatense, ~310 palabras)
U2_PODCAST_SCRIPT = """
A: Bienvenidos al podcast de la Unidad 2. Hoy analizamos con la licenciada Carla Nani por qué en salud dos más dos casi nunca es cuatro.
B: Es que en el hospital los imponderables son la regla, Elena. Te cambia una guardia en un segundo por un ingreso imprevisto y todo lo planificado se cae.
A: Totalmente. Y frente a esos imponderables, la herramienta central es la comunicación. Ojo con esto: el paciente, la familia y el colega nunca son receptores mecánicos; son perceptores activos atravesados por el miedo, la incertidumbre y su historia social.
B: Por eso el modelo del quirófano es tan potente. En quirófano nadie se corta solo; hay una interdependencia absoluta donde la instrumentadora, el anestesiólogo y el cirujano comparten una sola meta: la seguridad del paciente.
A: Ni más ni menos. El cirujano no puede cerrarse en un liderazgo autoritario. Un líder positivo escucha, persuade y tiene empatía genuina sin caer en la permisividad destructiva.
B: Y la regla de oro que nos deja Carla Nani es contundente: en salud no comunicás lo que decís, sino lo que tu perceptor comprendió y puede ejecutar de forma segura.
"""

u1_audio_path = MEDIA_DIR / "u1_podcast_cultura.mp3"
u2_audio_path = MEDIA_DIR / "u2_podcast_liderazgo.mp3"

print("-> Renderizando audio Unidad 1 (es-AR-ElenaNeural / es-AR-TomasNeural)...")
generate_podcast_sync(U1_PODCAST_SCRIPT, u1_audio_path)
print(f"   [OK] Audio U1 generado: {u1_audio_path.name} ({u1_audio_path.stat().st_size / 1024:.1f} KB)")

print("-> Renderizando audio Unidad 2 (es-AR-ElenaNeural / es-AR-TomasNeural)...")
generate_podcast_sync(U2_PODCAST_SCRIPT, u2_audio_path)
print(f"   [OK] Audio U2 generado: {u2_audio_path.name} ({u2_audio_path.stat().st_size / 1024:.1f} KB)")

# Generar paquetes SCORM para los audios
print("\n-> Empaquetando SCORMs de audio para Moodle...")
import os
import shutil

orig_cwd = os.getcwd()
try:
    os.chdir(str(SCORM_DIR))
    create_audio_scorm(
        str(u1_audio_path),
        "Podcast Unidad 1: Cultura Organizacional y Gestión",
        "Microlearning en audio de dos voces sobre los vectores SER, HACER y ESTAR en salud.",
        "u1_podcast_SCORM.zip"
    )
    create_audio_scorm(
        str(u2_audio_path),
        "Podcast Unidad 2: Comunicación y Liderazgo",
        "Microlearning en audio de dos voces sobre el paradigma del quirófano y el perceptor en salud.",
        "u2_podcast_SCORM.zip"
    )
finally:
    os.chdir(orig_cwd)

print("\n[OK] Generación completa de aula virtual Moodle con podcasts finalizada exitosamente.")
