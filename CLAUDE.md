# CLAUDE.md

Este archivo proporciona pautas para Claude Code / Antigravity cuando trabaja con código en este repositorio.

## Descripción General del Proyecto

Sistema de generación de contenidos de cursos SCORM 1.2 utilizando un flujo de trabajo multi-agente. Crea contenido de e-learning universalmente compatible con todas las plataformas LMS principales (Moodle, Canvas, Blackboard, Google Classroom, TalentLMS, Schoology, D2L Brightspace, etc.).

## Comandos Comunes

```bash
# Generar paquete SCORM a partir de contenido markdown
python scripts/scorm_generators/create_scorm_package.py

# Crear paquete SCORM de audio
python scripts/scorm_generators/create_audio_scorm.py <archivo_de_audio> [titulo] [descripcion]

# Crear paquete SCORM de video
python scripts/scorm_generators/create_video_scorm.py <archivo_de_video> [titulo] [descripcion]

# Comprimir archivos de video grandes (CRF recomendado: 23)
ffmpeg -i input.mp4 -vcodec libx264 -crf 23 -preset medium -acodec aac -b:a 128k output.mp4
```

## Estructura de Directorios

```
scripts/
├── scorm_generators/        # Creadores de paquetes SCORM (texto, audio, video)
├── content_generation/      # Generación de páginas HTML, edición de contenido
└── legacy/                  # Scripts obsoletos (solo referencia)

content/                     # Contenido de los cursos organizado por curso
├── ai-principianti/         # Ejemplo: Curso de IA para principiantes
└── sicurezza-lavoro/        # Ejemplo: Curso de seguridad laboral

.claude/agents/              # Archivos de definición de agentes
output/                      # Paquetes SCORM generados (.zip)
docs/                        # Guías de importación y resolución de problemas
```

## Flujo de Trabajo de Agentes

El sistema utiliza cinco agentes especializados invocados con `subagent_type`:

| Agente | subagent_type | Propósito |
|-------|---------------|-----------|
| Course Outliner | `course-outliner` | Entrevistar al usuario → crear una estructura pedagógica del curso |
| Content Creator | `content-creator` | Generar contenido textual a partir de la estructura |
| Senior Editor | `senior-editor` | Refinar y pulir el contenido escrito |
| SCORM Packager | `moodle-xml-formatter` | Convertir markdown → paquete SCORM .zip |
| Multimedia Integrator | `multimedia-integrator` | Crear paquetes SCORM de audio/video |

**Flujo estándar:**
1. `course-outliner` → Entrevista y creación de la estructura.
2. `content-creator` → Escribir contenido a partir de la estructura.
3. `senior-editor` → Pulir y editar.
4. `moodle-xml-formatter` → Empaquetar como SCORM .zip.

## Generación de Paquetes SCORM

El script `create_scorm_package.py` espera un archivo markdown con módulos prefijados por `# Módulo` o `# Modulo`. El script:
- Convierte markdown a HTML con estilo y botones de navegación.
- Crea `imsmanifest.xml` compatible con SCORM 1.2.
- Empaqueta todo en un archivo .zip listo para importar en el LMS.

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
