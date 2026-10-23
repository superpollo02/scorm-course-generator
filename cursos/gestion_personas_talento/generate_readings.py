import subprocess
from pathlib import Path

BASE_DIR = Path(r"c:\Users\mfischer\Documents\antigravitiy proyectos\aula nueva con moodle\cursos\gestion_personas_talento")
U1_DIR = BASE_DIR / "lecturas" / "unidad_1"
U2_DIR = BASE_DIR / "lecturas" / "unidad_2"
U1_DIR.mkdir(parents=True, exist_ok=True)
U2_DIR.mkdir(parents=True, exist_ok=True)

readings = [
    (U1_DIR / "lectura_1_1_gestion_vs_administracion_y_contexto.md", """# Lectura 1.1: Gestión vs. Administración en Salud y Complejidad del Contexto Sanitario

**Curso:** Gestión de Personas y Talento Humano en Salud  
**Unidad 1:** Cultura Organizacional y los Desafíos de la Gestión Institucional  
**Docente:** Dra. Susana Salomón  

---

## 1. Diferenciación Conceptual: Administración vs. Gestión

En el ámbito de las instituciones sanitarias coexisten dos enfoques complementarios pero sustancialmente diferentes para la conducción institucional:

- **Administración Tradicional:** Constituye un enfoque esencialmente **normativo, estructurado y ordenador**. Se centra en el cumplimiento de reglamentos, la regularidad procedimental y la calidad técnica operativa. Su objetivo principal es disponer y organizar racionalmente los recursos materiales, económicos y normativos para asegurar un funcionamiento predecible. En un efector de salud, la función administrativa se ejemplifica en la oficina de personal, encargada de fiscalizar el cumplimiento de horarios, la contabilización de licencias y el trámite de expedientes reglamentarios.
- **Gestión Estratégica:** Representa un enfoque dinámico orientado a **resultados asistenciales, la conducción del talento humano y la sincronización de voluntades**. Mientras la administración norma procesos, la gestión orienta las acciones coordinadas hacia el logro eficaz y eficiente de objetivos institucionales compartidos. La gestión prioriza al capital humano y entiende que en el comportamiento social de las organizaciones de salud **"dos más dos nunca es cuatro"**, debido a la interferencia constante de imponderables, factores emocionales y la complejidad subjetiva del equipo de salud. En la práctica, el departamento de gestión del talento humano planifica la capacitación continua, el desarrollo profesional y la motivación del personal.

| Dimensión | Administración Tradicional | Gestión Estratégica en Salud |
| :--- | :--- | :--- |
| **Enfoque principal** | Normativo, procedimental y de control. | Estratégico, orientado a resultados y personas. |
| **Objeto de acción** | Procesos, recursos físicos y regularidad formal. | Talento humano, sincronización de voluntades e imponderables. |
| **Criterio de éxito** | Orden, cumplimiento normativo y precisión técnica. | Eficiencia, eficacia asistencial y clima laboral saludable. |
| **Ejemplo hospitalario** | Control de presentismo y otorgamiento de licencias. | Desarrollo de competencias, formación y liderazgo de equipos. |

---

## 2. La Complejidad del Contexto Sanitario Contemporáneo

Las instituciones de salud se definen como **organizaciones complejas con múltiples dominios sociales y técnicos**. En ellas convergen saberes interconectados pero heterogéneos: profesionales médicos de diversas especialidades, enfermeros, bioquímicos, farmacéuticos, técnicos, trabajadores sociales, así como personal administrativo, de mantenimiento, seguridad y servicios generales. Cada uno de estos estamentos posee sus propios lenguajes, metas e identidades profesionales.

Los centros asistenciales enfrentan hoy un entorno caracterizado por alta incertidumbre y transformación permanente:

1. **Innovación Tecnológica e Inteligencia Artificial:** La rápida penetración de tecnologías sanitarias y herramientas de Inteligencia Artificial genera una obsolescencia acelerada de equipamientos y procesos, exigiendo una reconversión continua de las competencias del personal.
2. **Pulverización por Especialidades:** La hiperespecialización biomédica dicotomiza y fragmenta la atención asistencial, tornando complejo el abordaje integral e integrado del paciente como persona.
3. **Incertidumbre y Sobregeneración de Información:** El volumen de evidencia científica crece de forma exponencial, configurando un escenario donde la toma de decisiones clínicas y de gestión debe realizarse bajo presión e incertidumbre constante.
4. **Dinámicas Socioeconómicas y Ambientales:** Las tensiones presupuestarias, la complejidad de los mercados sanitarios y la preocupación ambiental demandan un uso ético, equitativo y eficiente de cada recurso asignado.
"""),
    (U1_DIR / "lectura_1_2_vectores_identidad_ser_hacer_estar.md", """# Lectura 1.2: Los Tres Vectores de la Identidad Institucional (EL SER, EL HACER y EL ESTAR)

**Curso:** Gestión de Personas y Talento Humano en Salud  
**Unidad 1:** Cultura Organizacional y los Desafíos de la Gestión Institucional  
**Docente:** Dra. Susana Salomón  

---

## 1. Vector EL SER: Identidad Sustancial y Propósito

El vector del **SER** representa la esencia sustancial, el alma y el marco deontológico de la institución. Define los cimientos estratégicos y **no es un bien transable ni negociable** bajo presiones coyunturales:

- **Misión (*¿Qué somos?*):** Expresa el propósito primordial, la razón de ser y la contribución directa que la institución brinda a la sociedad en el presente. Define la dirección estratégica; sin una misión clara, los esfuerzos colectivos no pueden sincronizarse. La pedagogía institucional recomienda enunciados claros y concisos que identifiquen al usuario (paciente/comunidad) y el valor asistencial aportado.
- **Visión (*¿Qué queremos ser?*):** Constituye el horizonte estratégico a largo plazo, la aspiración futura e imagen objetivo que motiva y guía el desarrollo institucional.
- **Valores Estratégicos (*¿Cómo hacemos lo que hacemos?*):** Convicciones éticas y operativas que sustentan la misión y la visión, estableciendo el parámetro de conducta de los colaboradores y guiando la selección de prioridades.
- **Principios Rectores y Valores Éticos:** Ubicados en la base de la pirámide de la identidad, son las creencias y convicciones sustanciales e innegociables (calidad, seguridad del paciente, transparencia, equidad, honestidad, puntualidad, cordialidad) que deben formalizarse mediante actos administrativos oficiales (como resoluciones ministeriales publicadas en el Boletín Oficial) para ser conocidos y respetados por todos los integrantes al ingresar a la institución.

---

## 2. Vector EL HACER: Dimensión Operativa y Funcional

El vector del **HACER** traduce el propósito ético en acciones concretas y ejecutables dentro del sistema asistencial:

- **Prioridades:** Selección consciente de caminos operativos tras evaluar riesgos e impacto sanitario, alineando las metas de cada servicio con la misión y visión colectivas.
- **Funciones:** Modelos de división del trabajo articulados en unidades organizativas (departamentos, servicios, divisiones) indispensables para cumplir la misión. Se dividen en:
  - **Funciones Finales:** Actividades sustantivas directas orientadas al paciente (servicios de urgencias, quirófanos, salas de internación, consultorios externos).
  - **Funciones Intermedias o de Apoyo:** Unidades de diagnóstico por imágenes, laboratorio, farmacia, mantenimiento, esterilización, limpieza y administración que garantizan la viabilidad de las funciones finales.
- **Actividades:** Tareas estandarizadas desempeñadas cotidianamente por las personas; representan a nivel individual lo que las funciones representan a nivel departamental.

---

## 3. Vector EL ESTAR: Dimensión Relacional, Estructural y Contextual

El vector del **ESTAR** comprende las condiciones estructurales, ambientales y vinculares en las que se despliega la vida institucional cotidiana:

- **Ambiente:** Red de intercambio dinámico con el entorno socioeconómico, epidemiológico y comunitario.
- **Estructura Organizativa:** Esquema de división del trabajo e integración de responsabilidades. Distingue entre la **cadena de mando formal** (el organigrama jerárquico reglamentario) y la **cadena de mando real** (las redes informales de autoridad técnica y moral reconocidas de facto por los profesionales en la práctica asistencial).
- **Cultura:** El entramado sociocultural implícito y explícito que modela la convivencia diaria.
"""),
    (U1_DIR / "lectura_1_3_cultura_tipologias_y_clima_laboral.md", """# Lectura 1.3: Cultura Organizacional, Tipologías Culturales y Clima Laboral

**Curso:** Gestión de Personas y Talento Humano en Salud  
**Unidad 1:** Cultura Organizacional y los Desafíos de la Gestión Institucional  
**Docente:** Dra. Susana Salomón  

---

## 1. Concepto, Transmisión y Niveles de la Cultura Organizacional

La cultura organizacional se define como el **"alma" o la "personalidad" de la institución**. Es un sistema de significados compartidos, códigos, normas implícitas, tradiciones y valores que determinan cómo se hacen las cosas y cómo se resuelven los problemas.

### Mecanismos de Transmisión Cultural
1. **Historias y Narrativas:** Relatos sobre los fundadores, momentos críticos superados y maestros formadores que ejemplifican los valores del hospital.
2. **Ritos y Rituales:** Secuencias repetitivas que refuerzan la identidad (pases de sala, ateneos clínicos, actos de bienvenida a residentes, festejos de fin de año integradores).
3. **Símbolos Materiales:** Infraestructura, indumentaria distintiva, casacas por servicio y credenciales que comunican pertenencia.
4. **Lenguaje y Jerga:** Siglas clínicas, modismos técnicos y códigos comunicacionales propios de cada servicio.

### Niveles de la Cultura y Subculturas Hospitalarias
- **Nivel 1 (Artefactos visibles):** Arquitectura, vestimenta, protocolos escritos y rutinas observables.
- **Nivel 2 (Valores de comportamiento):** Normas aprendidas por observación e interacción entre pares.
- **Nivel 3 (Supuestos inconscientes):** Creencias profundas y automáticas que conforman el ADN institucional.
- **Subculturas Clínicas vs. Quirúrgicas:** Dentro del mismo hospital coexisten subculturas diferenciadas. Los servicios clínicos suelen operar bajo tiempos deliberativos de discusión diagnóstica, mientras que los servicios quirúrgicos requieren jerarquías operativas inmediatas y alta sincronización física en el quirófano.

---

## 2. Las 4 Tipologías Culturales en Salud

| Tipología Cultural | Características Nucleares | Beneficios Principales | Límites y Riesgos |
| :--- | :--- | :--- | :--- |
| **1. Cultura Clan** | Familiar, colaborativa, horizontal y centrada en las personas. | Alta cohesión, lealtad, sentido de pertenencia y clima amigable. | Dificultad para mantener el orden y control cuando la organización crece a gran escala. |
| **2. Cultura Adhocracia** | Flexible, innovadora, creativa y dispuesta a asumir riesgos. | Dinamismo constante, aprendizaje rápido e innovación médica. | Riesgo de errores por baja estandarización y presión por el cambio continuo. |
| **3. Cultura de Mercado** | Orientada a la competitividad, metas cuantitativas y rentabilidad. | Objetivos claros, alta productividad y foco en resultados medibles. | Competencia interna excesiva, desgaste emocional (*burnout*) y menor compromiso afectivo. |
| **4. Cultura Jerárquica** | Tradicional, formal, centrada en la cadena de mando y normas estrictas. | Estabilidad, predictibilidad, orden normativo y dirección clara. | Rigidez, lentitud ante imprevistos, baja creatividad y escaso feedback ascendente. |

---

## 3. Clima Laboral vs. Cultura Organizacional y Glosario

- **Cultura vs. Clima:** La cultura es estructural, histórica y profunda; el **clima laboral** es la percepción subjetiva coyuntural que tienen los trabajadores sobre su entorno cotidiano. Un clima tóxico o violento destruye la productividad, provoca fuga de talentos y aumenta el riesgo de error asistencial; un clima saludable potencia el compromiso, la salud ocupacional y la excelencia en el cuidado del paciente.

### Glosario Esencial de la Unidad 1
1. **Administración:** Proceso normativo de ordenar y disponer recursos garantizando regularidad técnica.
2. **Cadena de Mando Real:** Red de liderazgo y consulta efectiva que opera en la práctica más allá del organigrama impreso.
3. **Clima Laboral:** Percepción subjetiva compartida sobre el bienestar y las relaciones cotidianas en el trabajo.
4. **Cultura Organizacional:** Personalidad o alma de la institución integrada por valores, ritos y supuestos compartidos.
5. **Funciones Finales:** Servicios asistenciales directos que cumplen la misión sustantiva con el paciente.
6. **Funciones de Apoyo:** Servicios intermedios (laboratorio, farmacia, mantenimiento) indispensables para sostener la atención.
7. **Gestión:** Conducción estratégica del talento humano sincronizando voluntades hacia resultados.
8. **Misión:** Propósito presente y razón de ser de la organización sanitaria.
9. **Principios Rectores:** Convicciones éticas innegociables que rigen la conducta institucional.
10. **Visión:** Horizonte estratégico e imagen futura que la institución aspira a alcanzar.
"""),
    (U2_DIR / "lectura_2_1_talento_humano_imponderables_y_comunicacion.md", """# Lectura 2.1: Gestión del Talento Humano, Imponderables y el Proceso de Comunicación en Salud

**Curso:** Gestión de Personas y Talento Humano en Salud  
**Unidad 2:** Comunicación, Trabajo en Equipo y Liderazgo Situacional en Salud  
**Docente:** Lic. Carla Nani  

---

## 1. La Premisa del Factor Humano: Por qué en Salud "2 + 2 nunca es 4"

En la conducción de personas dentro de las organizaciones sanitarias, las ecuaciones deterministas no funcionan: **dos más dos nunca es cuatro**. A diferencia del manejo de insumos inertes, los profesionales y los pacientes son sujetos atravesados por emociones, historias de vida, miedos y contingencias.

En el hospital existen **imponderables permanentes**: urgencias no programadas, reacciones inesperadas ante el dolor o el duelo, y tensiones interpersonales que alteran cualquier planificación rígida. Por ello, la primera competencia transversal del profesional de salud es la **flexibilidad y adaptabilidad rápida** para recalibrar decisiones sin perder el objetivo asistencial.

---

## 2. El Proceso de Comunicación: Del Receptor Pasivo al Perceptor Activo

La comunicación humana es un proceso relacional entre dos o más personas que interactúan mediante dimensiones **verbales** (palabra oral o escrita) y **no verbales** (gestos, mirada, tono de voz, postura corporal). En salud, la dimensión no verbal es determinante porque transmite contención, seguridad o rechazo antes de pronunciar la primera palabra.

### Actores y Operaciones del Esquema Comunicacional
- **El Emisor:** Es el profesional que inicia el proceso realizando un trabajo mental consciente de **codificación** (pensar, seleccionar el código y estructurar el mensaje según el canal).
- **Por qué NO hablamos de Receptor:** Un *receptor* es un aparato mecánico (como un buzón de voz telefónico) que se limita a reproducir literalmente la señal recibida sin otorgarle sentido propio.
- **El Perceptor:** En la comunicación humana el interlocutor es siempre un **perceptor**, porque percibe y **decodifica** el mensaje interpretándolo desde su propio punto de vista.

### Condicionantes del Perceptor y Responsabilidad del Emisor
El perceptor filtra el mensaje a través de sus **condicionantes**:
1. Edad y etapa vital (no decodifica igual un joven de 20 años que un adulto mayor de 75).
2. Nivel socioeconómico, educativo y entorno cultural.
3. Vivencias previas, prejuicios y estado emocional agudo (angustia, miedo, negación).

**Regla de Oro de la Comunicación Eficaz:** El mensaje es eficaz únicamente cuando el perceptor lo comprende con la misma intención con que lo emitió el emisor. La **responsabilidad primaria recae siempre en el profesional emisor**, quien como especialista debe diagnosticar quién es su perceptor (paciente, familiar o colega) y adecuar su lenguaje dejando de lado los tecnicismos inaccesibles.
"""),
    (U2_DIR / "lectura_2_2_trabajo_en_equipo_vs_grupo_y_quirofano.md", """# Lectura 2.2: Trabajo en Equipo vs. Grupo de Trabajo y el Paradigma del Quirófano

**Curso:** Gestión de Personas y Talento Humano en Salud  
**Unidad 2:** Comunicación, Trabajo en Equipo y Liderazgo Situacional en Salud  
**Docente:** Lic. Carla Nani  

---

## 1. Diferencias Estructurales entre Grupo y Equipo de Trabajo

En la vida cotidiana del hospital suelen confundirse los grupos sociales con los verdaderos equipos asistenciales:

| Dimensión de Análisis | Grupo de Trabajo | Equipo de Trabajo en Salud |
| :--- | :--- | :--- |
| **Origen y Formación** | Surge por afinidades personales, simpatías espontáneas o proximidad social. | Se conforma en el ámbito laboral para alcanzar un objetivo asistencial común. |
| **Perfil de los Miembros** | Formación homogénea o similar; realizan el mismo tipo de tarea en paralelo. | **Habilidades complementarias** y multidisciplinarias (médicos, enfermeros, técnicos). |
| **Responsabilidad** | Estricto carácter **individual**: cada uno responde solo por su fracción. | **Responsabilidad individual y colectiva**: las decisiones son sostenidas por todo el equipo. |
| **Jerarquía Operativa** | Niveles jerárquicos rígidos y marcados. | Las jerarquías formales se dinamizan porque cada especialista domina su rol técnico. |
| **Cohesión y Sinergia** | La cohesión es opcional; suma lineal de esfuerzos. | Cohesión estrecha indispensable; genera soluciones creativas e innovadoras. |

---

## 2. El Quirófano como Modelo Paradigmático de Equipo Interdependiente

Incluso fuera de las ciencias médicas, la disciplina de Recursos Humanos estudia al **quirófano** como el ejemplo más acabado de un equipo de trabajo de alto rendimiento:

1. **Diversidad Complementaria:** En el quirófano convergen el cirujano, el anestesiólogo, el instrumentador quirúrgico, el enfermero circulante y el personal de limpieza y bioseguridad. Ninguno puede reemplazar el saber específico del otro, pero todos se necesitan mutuamente.
2. **Distribución Natural y Sincronizada de Roles:** Cada integrante conoce con precisión qué debe hacer y en qué instante intervenir sin necesidad de órdenes burocráticas constantes.
3. **Meta Común Innegociable:** Todos los esfuerzos, la comunicación verbal y las miradas (comunicación no verbal) están alineados tras un único propósito compartido: sacar adelante al paciente con seguridad y calidad.
4. **Respaldo Colectivo:** Cuando surge una complicación intraoperatoria (un imponderable), la solución innovadora emerge de la sinergia del conjunto y es respaldada solidariamente por todo el equipo quirúrgico.
"""),
    (U2_DIR / "lectura_2_3_liderazgo_situacional_empatia_y_maslow.md", """# Lectura 2.3: Liderazgo Situacional, Empatía Genuina y Prevención del Fracaso Directivo

**Curso:** Gestión de Personas y Talento Humano en Salud  
**Unidad 2:** Comunicación, Trabajo en Equipo y Liderazgo Situacional en Salud  
**Docente:** Lic. Carla Nani  

---

## 1. Liderazgo Situacional y Persuasión Sin Coerción

El **liderazgo** es la capacidad de guiar, motivar e influir en un equipo de trabajo para alcanzar metas institucionales. Influir es sinónimo de **persuadir**: lograr que el colaborador adhiera y actúe por convicción propia y respeto profesional, **nunca mediante la fuerza bruta, el miedo, la coerción ni la manipulación**.

### ¿Por qué el Liderazgo en Salud es Situacional?
No existe un único molde de líder para todo momento. En las instituciones de salud los líderes son **situacionales**:
- Durante una emergencia vital en guardia o quirófano, se requiere una determinación rápida, precisa y directiva.
- Durante la planificación de un servicio, un pase de sala académico o la resolución de un conflicto crónico, se requiere escucha activa, consenso y participación horizontal.
El líder efectivo no es egoísta ni oculta información para sentirse indispensable; por el contrario, **inspira y empodera** a sus residentes y colegas para que crezcan profesionalmente.

---

## 2. Empatía Genuina vs. Permisividad y Pirámide de Maslow

- **Empatía Genuina vs. Permisividad:** Ser un líder empático significa ponerse en el lugar del otro para comprender qué situación personal o emocional atraviesa (por ejemplo, reubicar temporalmente a un profesional que vive una crisis familiar sin desplazarlo ni humillarlo). Sin embargo, **empatía no es permisividad**: el líder permisivo dice que sí a todo, incumple las normas y termina destruyendo la autoridad y el orden del equipo.
- **Reconocimiento de Necesidades (Pirámide de Maslow):** El talento humano no se motiva únicamente con el salario básico (necesidades fisiológicas y de seguridad). El líder sanitario debe satisfacer las necesidades superiores de **pertenencia al equipo**, **reconocimiento explícito del trabajo bien hecho** y **autorrealización profesional** mediante la delegación con confianza.

---

## 3. Las Causas Comunes del Fracaso del Líder y Glosario

Un referente asistencial fracasa cuando incurre en:
1. **Falta de escucha activa:** No oír las alertas ni propuestas del equipo.
2. **Impulsividad:** Tomar decisiones apresuradas sin reflexionar.
3. **Incapacidad para delegar:** Querer absorber todas las tareas por desconfianza.
4. **Mal manejo de conflictos y falta de ética:** Mentir, incumplir la palabra o carecer de transparencia.
5. **Estancamiento profesional ("líder chato"):** Perder el respeto técnico de sus pares por falta de actualización.
6. **Rigidez autocrática:** No adaptarse a los cambios del contexto ni practicar la empatía.

### Glosario Esencial de la Unidad 2
1. **Codificación:** Elaboración mental consciente del mensaje por parte del emisor antes de transmitirlo.
2. **Condicionantes:** Factores de edad, cultura, nivel socioeconómico y emociones que filtran la percepción.
3. **Decodificación:** Interpretación subjetiva que realiza el perceptor sobre el mensaje recibido.
4. **Empatía Genuina:** Comprender la realidad emocional del colaborador manteniendo los objetivos del servicio.
5. **Empoderamiento:** Impulsar el crecimiento, la autonomía y el reconocimiento de los miembros del equipo.
6. **Equipo de Trabajo:** Conjunto de profesionales con habilidades complementarias y responsabilidad colectiva.
7. **Imponderables:** Situaciones imprevistas propias del factor humano en salud ($2+2 \\neq 4$).
8. **Liderazgo Situacional:** Conducción flexible que se adapta a las necesidades del equipo y del contexto clínico.
9. **Perceptor:** Sujeto humano activo que interpreta los mensajes según su marco de referencia.
10. **Persuasión:** Influencia positiva basada en la convicción y la palabra, libre de coerción.
""")
]

for md_path, content in readings:
    md_path.write_text(content, encoding="utf-8")
    docx_path = md_path.with_suffix(".docx")
    if docx_path.exists():
        docx_path.unlink()
    subprocess.run(["tiza", "documento", str(md_path), "--salida", str(docx_path)], check=True)
    print(f"Created MD and DOCX: {docx_path.name}")
