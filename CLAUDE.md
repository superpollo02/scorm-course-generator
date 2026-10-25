# CLAUDE.md

Este archivo proporciona pautas para Claude Code / Antigravity cuando trabaja con código en este repositorio.

## Descripción General del Proyecto

Aula Lista EDUCAI: Sistema integral de ingeniería instruccional y producción automatizada de contenidos didácticos para LMS (Moodle / Arquitectura Tripartita, Protocolo Kit Aula Lista, Microlearning, Infografías y paquetes SCORM 1.2 interactivos). Crea contenido de e-learning universalmente compatible con todas las plataformas LMS principales (Moodle, Canvas, Blackboard, Google Classroom, TalentLMS, Schoology, D2L Brightspace, etc.).

## Comandos Comunes

```bash
# Generar paquete SCORM a partir de contenido markdown (formato "# Módulo X: Título")
python scripts/scorm_generators/create_scorm_package.py

# Generar paquete SCORM moderno: 1 Lección + 1 Evaluación (quiz) + N Actividades + enlaces
python scripts/scorm_generators/create_scorm_modern_package.py validate <config.yaml>
python scripts/scorm_generators/create_scorm_modern_package.py build <config.yaml>
python scripts/scorm_generators/create_scorm_modern_package.py list <config.yaml>

# Actividades gamificadas SCORM interactivas (Conectabloques & Trivia con Modo Turno)
python scripts/scorm_generators/build_conectabloques_scorm.py
python scripts/scorm_generators/build_trivia_scorm.py <archivo.md> --tema neon|cosmic|corporate|high-contrast

# Modo Turbo en Trivia (1: 1-Click Automático, 2: Por Lotes / Batch)
python scripts/scorm_generators/build_trivia_scorm.py <archivo.md> --turbo 1
python scripts/scorm_generators/build_trivia_scorm.py <directorio> --turbo 2

# Renderizado de video educativo programático con HyperFrames
npx hyperframes preview templates/moodle-showcase-60s.html
npx hyperframes check templates/moodle-showcase-60s.html
npx hyperframes render templates/moodle-showcase-60s.html

# Crear paquete SCORM de audio / video legacy
python scripts/scorm_generators/create_audio_scorm.py <archivo_de_audio> [titulo] [descripcion]
python scripts/scorm_generators/create_video_scorm.py <archivo_de_video> [titulo] [descripcion]

# Comprimir archivos de video grandes (CRF recomendado: 23)
ffmpeg -i input.mp4 -vcodec libx264 -crf 23 -preset medium -acodec aac -b:a 128k output.mp4
```

## Estructura de Directorios

```
templates/                    # Plantillas maestras de video programático HyperFrames
├── moodle-showcase-60s.html  # Showcase promocional de alto impacto (1080p, 60s)
├── moodle-vertical-9-16.html # Formato móvil vertical (Reels, TikTok, Shorts)
├── moodle-makeover-90s.html  # Kit Makeover / Renovación de aula en 8 escenas
├── moodle-tutorial-120s.html # Tutorial técnico con cursor reactivo animado y step bar
└── unidad*-*.html            # Plantillas curriculares sincronizadas (Unidades 2 a 8)

assets/audio/                 # Banco sonoro multicapa portable para videos y microlearning
├── manifest.json             # Catálogo de pistas, duraciones y volúmenes
├── bgm*.wav / *.mp3          # Música de fondo ambiental e institucional (calibrada 12-15%)
├── vo-*.mp3                  # Pistas maestras de locución profesional (Elena, etc.)
└── *.mp3 (SFX)               # 10 efectos diegéticos (whoosh, chime, sparkle, click, impact...)

skills/                                      # Habilidades ejecutables de Antigravity
├── edtech-moodle-video/                     # Metodología y captura de recorridos Moodle y SCORM
├── notebooklm-video-shorts/                 # Ingesta con NotebookLM (CLI nlm) para guiones de shorts
├── hyperframes-render/                      # Renderizado programático en MP4 con HyperFrames (Chrome Headless)
└── diseno-instruccional-aula-tripartita/    # Enfoque andragógico: intro (2 oraciones + 3 preguntas) y consignas

agents/                       # Definiciones de agentes especializados
└── edtech-video-director.md  # Director audiovisual EdTech / HyperFrames

scripts/
├── scorm_generators/        # Creadores de paquetes SCORM (texto, audio, video, moderno, trivia, conectabloques)
├── content_generation/      # Generación de páginas HTML, IA con Gemini, edición de contenido
└── legacy/                  # Scripts de referencia histórica

scorm_modern/                 # Generador moderno: Lección + Evaluación + N Actividades + enlaces
├── scorm_modern/             # Paquete Python (config, parser, renderer, manifest, builder, cli)
├── tests/                    # pytest (30 tests)
├── ejemplo/                  # config.yaml + markdown de ejemplo funcional
└── README.md                 # Formato de config.yaml y del markdown fuente

content/                     # Contenido de los cursos organizado por curso
.claude/agents/              # Definiciones de agentes para Claude Code / Antigravity
output/                      # Paquetes SCORM generados (.zip) y kits de aula lista
renders/                     # Renders MP4 de video exportados
docs/                        # Guías de importación, LMS y resolución de problemas
```

## Flujo de Trabajo de Agentes

El sistema utiliza agentes especializados invocados con `subagent_type`:

| Agente | subagent_type | Propósito |
|-------|---------------|-----------|
| NotebookLM Assistant | `asistente-notebooklm` | Ingesta de fuentes con NotebookLM (CLI nlm), transcripciones y guiones de video |
| Course Outliner | `course-outliner` | Estructurar la unidad bajo Kit Aula Lista y Arquitectura Tripartita |
| Content Creator | `content-creator` | Redactar sección introductoria, lecturas, consignas obligatorias y rúbricas |
| Senior Editor | `senior-editor` | Auditar coherencia pedagógica, consignas obligatorias y anti-trampa |
| Multimedia Integrator | `multimedia-integrator` | Crear banners panorámicos, infografías vectoriales y diapositivas PPTX |
| EdTech Video Director | `edtech-video-director` | Renderizar videos programáticos MP4 con HyperFrames (Short 1-2 min) |
| SCORM Packager | `moodle-xml-formatter` | Maquetar HTML Moodle (Tiza) y compilar SCORM 1.2 (Conectabloques / Trivia) |
| Quality Auditor | `auditor-calidad-aula-lista` | Auto-auditoría exhaustiva Zero-Missing Gate y autocorrección Self-Healing |

**Flujo estándar:**
1. `course-outliner` → Planificación pedagógica bajo la Arquitectura Tripartita y Circular 5.
2. `content-creator` → Redacción de textos, 3 preguntas andragógicas, lecturas, consigna obligatoria y rúbrica.
3. `senior-editor` → Auditoría editorial y verificación de banco de preguntas aleatorizables.
4. `multimedia-integrator` & `edtech-video-director` → Creación de banners, infografías, diapositivas y video short MP4.
5. `moodle-xml-formatter` → Consulta de modo de trivia al usuario (Turbo 1/Turno/Turbo 2/Personalizado), empaquetado SCORM y maquetación HTML.
6. `auditor-calidad-aula-lista` → **Revisión exhaustiva de los 10 componentes obligatorios**. Si falta alguno, ejecuta inmediatamente la autocorrección autónoma (Self-Healing) antes de entregar la tarea al usuario.

## Generación de Paquetes SCORM

Hay **dos generadores de texto** disponibles; elegir según la estructura del contenido:

| Generador | Estructura de origen | Cuándo usarlo |
|---|---|---|
| `create_scorm_package.py` | `# Módulo X: Título` (secuencia simple de módulos) | Cursos lineales sin quiz interactivo ni enlaces estructurados. |
| `create_scorm_modern_package.py` (→ paquete `scorm_modern/`) | `# Lección:` + `# Evaluación:` + `# Actividad:`/`# Ejercicio:` + `# Enlaces` | Cursos que necesitan un quiz corregido en el navegador (con seguimiento SCORM de aprobado/reprobado), actividades separadas de la lección, bloques de apoyo (`:::apoyo:::`) con video embebido de YouTube/Drive, y una lista de enlaces (`ENLACES.md`). |

**`create_scorm_package.py`**: convierte markdown a HTML con estilo y botones de navegación, crea `imsmanifest.xml` compatible con SCORM 1.2, y empaqueta todo en un .zip listo para importar en el LMS.

**`create_scorm_modern_package.py`** (`validate` / `build` / `list`): lee un `config.yaml` (con `identificador`, `titulo`, `contenido_md`, `puntaje_minimo`, `enlaces`) y el markdown que referencia, valida ambos, y genera 1 página de lección + 1 de evaluación (quiz autoevaluable) + N páginas de actividad + `ENLACES.md` + `imsmanifest.xml` con título real por objeto, todo empaquetado en `<identificador>-SCORM.zip`. Ver `scorm_modern/README.md` para el formato completo del config y del markdown.

**SCORM de Audio:** Se marca como completado cuando el audio termina. Soporta MP3, WAV, OGG, M4A, AAC.

**SCORM de Video:** Se marca como completado al visualizar el 90%. Soporta MP4, WEBM, MOV, AVI, MKV.

## Pautas de Tamaño de Archivos Multimedia

| Tamaño | Acción |
|------|--------|
| < 10 MB | Usar directamente |
| 10-25 MB | Compresión opcional |
| 25-50 MB | Compresión recomendada |
| 50-100 MB | Compresión obligatoria |
| > 100 MB | Alojamiento externo (YouTube/Vimeo) |

## Directrices para el Idioma Español

- Utilizar de forma consistente el tono informal "tú".
- Acentuación y caracteres correctos: á, é, í, ó, ú, ñ, ü, ¡, ¿.
- Ejemplos adaptados a contextos culturalmente relevantes de habla hispana.

## Estándares de Calidad

- **Pedagógico**: Taxonomía de Bloom, complejidad progresiva.
- **Tablas**: Tablas markdown con separadores `|`, fila de encabezado y separador `|---|---|`.
- **SCORM**: Archivo `imsmanifest.xml` válido en la raíz del zip.
- **Responsivo**: Salida HTML compatible con dispositivos móviles.

## Resolución de Problemas

**Fallo al importar SCORM:** Comprobar que `imsmanifest.xml` esté en la raíz del archivo zip.

**Tablas rotas:** Asegurar fila de cabecera + fila separadora (`|---|---|`) + número consistente de columnas.

**Carga demasiado grande:** Para Moodle/XAMPP, editar php.ini: `upload_max_filesize=100M`, `post_max_size=100M`.

**Los medios no se reproducen:** Volver a codificar a formato H.264/AAC.

Ver `docs/` para guías detalladas: `GUIA_IMPORTAR_MOODLE.md`, `GUIA_AUMENTAR_LIMITE_UPLOAD_MOODLE.md`


## Protocolo del Copiloto Orquestador: Menú Inicial (Modo Turbo vs. Modo Guiado)

Al iniciar la creación de cualquier unidad o curso completo, el agente (`agents/copiloto-orquestador.md` apoyado en `skills/asistente-toma-decisiones/SKILL.md`) presenta al docente **2 opciones cerradas**:

1. **`(Recomendado para rapidez) 🚀 Opción 1: Modo Turbo Autónomo (1-Click)`**:
   - Ejecución 100% autónoma sin pedir instrucciones intermedias. Todos los textos, imágenes, videos HyperFrames y paquetes SCORM 1.2 se generan con la configuración institucional óptima.
2. **`🧭 Opción 2: Modo Guiado Paso a Paso (4 Checkpoints con Opciones Cerradas)`**:
   - Acompaña al usuario a través de 4 puntos de decisión cerrados:
     - **Checkpoint 1 (Audiovisual)**: Formato de video short (16:9, 9:16 o Tutorial) y mezcla de audio.
     - **Checkpoint 2 (Gráfico)**: Paleta de banner/infografía y formato de diapositivas (PPTX/PDF).
     - **Checkpoint 3 (Pedagógico)**: Enfoque de las 3 lecturas y tipo de caso práctico con rúbrica.
     - **Checkpoint 4 (Gamificación SCORM)**: Modo de Trivia (Turbo 1, Turno, WCAG AAA o Temas) y Conectabloques.
   - Incluye siempre: opción `(Recomendado)`, vista previa de 3 líneas, botón para saltar a **Modo Turbo** en cualquier momento y regeneración en 1 clic.

## Protocolo Obligatorio: Consulta de Modo de Trivia y Examen

Al momento de generar la **Gran Trivia SCORM** de cada unidad o el **Examen Final Sumativo**, el agente **DEBE pausar y preguntar al usuario qué modo prefiere utilizar**, describiéndole las características de cada uno:

1. **🚀 Modo Turbo 1 (Automático 1-Click)**:
   - 10 preguntas intermedias, 60% de aprobación, 30 minutos de tiempo límite, orden aleatorio (shuffle), estilo Neón accesible de alto contraste y retroalimentación inmediata. Empaquetado directo automático a SCORM 1.2 ZIP.
2. **🎮 Modo Turno Estándar (Interactivo con Navegación por Pasos)**:
   - Navegación bidireccional (`← Anterior` y `Siguiente →`), barra interactiva superior de turnos para saltar libremente y revisar preguntas antes de entregar, 70% de aprobación, sin límite de tiempo estricto y retroalimentación contextual inmediata.
3. **⚡ Modo Turbo 2 (Generación Masiva por Lotes / Batch)**:
   - Procesa automáticamente todas las unidades o cuestionarios existentes en el directorio y genera todos los paquetes SCORM 1.2 correspondientes en una sola pasada.
4. **🎨 Personalización Total**:
   - Selección libre del tema visual (`neon`, `corporate`, `minimal`, `high-contrast`, `sunset`, `forest`, `cosmic`), paleta de colores (`--neon-primary`, `--neon-accent`), tiempo límite, momento del feedback (`immediate` o `end`), puntaje mínimo y exportación a GIFT para el banco de Moodle.

## Directiva Obligatoria de Cierre y Verificación Exhaustiva (Zero-Missing Gate)

Una vez que se hayan generado todos los contenidos solicitados para una unidad didáctica o curso completo, el agente **DEBE realizar una revisión exhaustiva para comprobar si alguno de los componentes no ha sido creado**.
- **Checklist obligatorio en disco**:
  1. `01_encabezado/banner_unidad.png` (y `.svg`)
  2. `01_encabezado/01_etiqueta_encabezado_y_banner.html` (con frase de 2 oraciones y 3 preguntas andragógicas)
  3. `02_la_clase/video_short.mp4` (microlearning renderizado con HyperFrames/NotebookLM)
  4. `02_la_clase/02_pagina_la_clase.html` (Dual Video responsivo + enlace a diapositivas)
  5. `02_la_clase/diapositivas_unidad.pptx` (o `.pdf`)
  6. `03_la_lectura/03_pagina_la_lectura.html` (teoría, Glosario y FAQs)
  7. `03_la_lectura/infografia_unidad.png` (y `.svg`)
  8. `04_la_practica/04_tarea_la_practica.html` (consigna orientadora obligatoria, desafíos y rúbrica)
  9. `scorm/conectabloques_unidad-SCORM.zip` (8 pares conceptuales con Web Audio)
  10. `scorm/trivia_unidad-SCORM.zip` (trivia gamificada con modo elegido y exportación GIFT)
  11. `Examen Final Sumativo` con candado en Moodle (si es unidad de cierre)
  12. Auditoría `tiza comprobar` en todos los archivos HTML (`Paso COMPROBAR: ok`)
- **Regla de Autocorrección (Self-Healing)**: Si falta cualquier elemento, el agente no debe detenerse ni solicitar confirmación: debe generarlo de inmediato hasta tener el 100% verificado.
