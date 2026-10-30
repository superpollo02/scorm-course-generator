# SCORM Course Generator

Sistema profesional para la generación de contenidos didácticos en formato SCORM 1.2, compatible con cualquier LMS (Learning Management System).

[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![SCORM 1.2](https://img.shields.io/badge/SCORM-1.2-green.svg)](https://scorm.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Índice

- [Descripción General](#descripción-general)
- [Características Principales](#características-principales)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalación](#instalación)
- [Inicio Rápido](#inicio-rápido)
- [Arquitectura Multi-Agente](#arquitectura-multi-agente)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Guía Completa de Scripts](#guía-completa-de-scripts)
- [Integración Multimedia](#integración-multimedia)
- [Centro de Ayuda y Guías Ilustradas](#centro-de-ayuda-y-guías-ilustradas)
- [Importación en LMS](#importación-en-lms)
- [Estándares de Calidad](#estándares-de-calidad)
- [Resolución de Problemas](#resolución-de-problemas)
- [Ejemplos de Cursos](#ejemplos-de-cursos)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## Descripción General

Este proyecto utiliza una **arquitectura multi-agente basada en IA** para crear contenidos didácticos de alta calidad en formato SCORM 1.2. El sistema divide el proceso de creación en fases especializadas, cada una gestionada por un agente dedicado con competencias específicas.

### ¿Por qué SCORM 1.2?

SCORM 1.2 es el estándar de e-learning más confiable y universalmente compatible:

| Ventaja | Descripción |
|-----------|-------------|
| **Compatibilidad Universal** | Funciona en cualquier LMS moderno |
| **Fiabilidad** | Estándar maduro y estable desde 2001 |
| **Seguimiento** | Soporta el estado de finalización y el progreso del usuario |
| **Portabilidad** | Un único paquete funciona en cualquier parte |
| **Listo para modo local** | Se puede visualizar localmente sin necesidad de un LMS |

### LMS Soportados

- **Moodle** (todas las versiones)
- **Canvas** (Instructure)
- **Blackboard Learn**
- **Google Classroom**
- **TalentLMS**
- **Schoology**
- **D2L Brightspace**
- **SAP Litmos**
- **Docebo**
- **iSpring Learn**
- Y cualquier otro LMS compatible con SCORM 1.2

---

## Características Principales

### Generación de Contenidos
- **Creación Automática**: Desde un simple esquema hasta un curso completo
- **Calidad Profesional**: Contenidos pedagógicamente válidos y gramaticalmente correctos
- **Optimización en Español**: Soporte completo para acentos, caracteres especiales y tono formal/informal

### Formateo
- **Markdown → HTML**: Conversión automática con estilos profesionales
- **Tablas Responsivas**: Visualización perfecta tanto en escritorio como en dispositivos móviles
- **Navegación Integrada**: Botones de Anterior/Siguiente/Índice

### Multimedia
- **SCORM de Audio**: Reproductor HTML5 con seguimiento de finalización
- **SCORM de Video**: Reproductor con barra de progreso y finalización automática al 90% visto
- **Compresión Inteligente**: Optimización automática para archivos multimedia grandes

### Seguimiento
- **API SCORM**: Comunicación completa con el LMS
- **Estado de Finalización**: de `incomplete` a `completed`
- **Puntuaciones**: Soporte para el reporte de calificaciones (`score raw`)

---

## Requisitos del Sistema

### Obligatorios

| Requisito | Versión | Notas |
|-----------|----------|------|
| **Python** | 3.8+ | Probado en 3.9, 3.10, 3.11, 3.14 |
| **Claude Code / Antigravity** | Última | Para el uso de agentes de IA |

### Opcionales

| Requisito | Versión | Uso |
|-----------|----------|----------|
| **ffmpeg** | 4.0+ | Compresión de video/audio |
| **Git** | 2.0+ | Control de versiones |

### Instalación de ffmpeg

**Windows (con Chocolatey):**
```powershell
choco install ffmpeg
```

**Windows (manual):**
1. Descarga desde https://ffmpeg.org/download.html
2. Extrae los archivos en `C:\ffmpeg`
3. Añade `C:\ffmpeg\bin` al PATH del sistema

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update && sudo apt install ffmpeg
```

---

## Instalación

### 1. Clona el Repositorio

```bash
git clone https://github.com/tuusername/scorm-course-generator.git
cd scorm-course-generator
```

### 2. Verifica Python

```bash
python --version  # Debe ser 3.8+
```

### 3. Crea el Entorno Virtual (Opcional)

```bash
python -m venv venv

# Windows
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process; .\venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate
```

### 4. Verifica la Instalación

```bash
python scripts/scorm_generators/create_scorm_package.py --help
```

---

## Inicio Rápido

### Método 1: Usando los Agentes de IA (Recomendado)

La forma más sencilla de crear un curso completo es utilizar los agentes de IA integrados:

```
1. Abre tu terminal de IA en el directorio del proyecto.
2. Solicita: "Quiero crear un curso sobre [TEMA]"
3. El agente de estructura de cursos te entrevistará para definir los requisitos.
4. Los agentes de creación, edición y empaquetado generarán automáticamente el archivo SCORM final.
```

### Método 2: Usando los Scripts Directamente

#### Paso 1: Prepara el Contenido

Crea un archivo markdown con la siguiente estructura:

```markdown
# Módulo 1: Introducción

## Objetivos de Aprendizaje
- Comprender los conceptos básicos
- Aplicar las técnicas fundamentales

## Contenido
Texto del módulo...

# Módulo 2: Profundización

## Objetivos de Aprendizaje
...
```

#### Paso 2: Genera el Paquete SCORM

```bash
python scripts/scorm_generators/create_scorm_package.py
```

#### Paso 3: Importa en tu LMS

Sube el archivo `.zip` generado a tu LMS como "Paquete SCORM".

---

## Arquitectura Multi-Agente

El sistema utiliza **cinco agentes especializados**, cada uno con competencias específicas:

```
┌─────────────────────────────────────────────────────────────────┐
│                        FLUJO DE TRABAJO                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐       │
│  │   COURSE     │    │   CONTENT    │    │   SENIOR     │       │
│  │   OUTLINER   │───▶│   CREATOR    │───▶│   EDITOR     │       │
│  │  (Naranja)   │    │   (Azul)     │    │   (Rojo)     │       │
│  └──────────────┘    └──────────────┘    └──────────────┘       │
│         │                                        │               │
│         │              Esquema                   │ Contenido     │
│         │              Estructurado              │ Pulido        │
│         ▼                                        ▼               │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    SCORM PACKAGER                         │   │
│  │                       (Verde)                             │   │
│  └──────────────────────────────────────────────────────────┐   │
│                              │                                   │
│                              ▼                                   │
│                    ┌──────────────────┐                         │
│                    │  Paquete SCORM   │                         │
│                    │     (.zip)       │                         │
│                    └──────────────────┘                         │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              MULTIMEDIA INTEGRATOR (Morado)               │   │
│  │       Audio/Video → Paquetes SCORM Independientes          │   │
│  └──────────────────────────────────────────────────────────┐   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Detalle de los Agentes

#### 1. Course Outliner (Naranja)
**Objetivo**: Diseña estructuras de cursos pedagógicamente sólidas.

| Aspecto | Detalle |
|---------|-----------|
| **Entrada** | Entrevista sobre objetivos, público, duración y nivel |
| **Salida** | Esquema completo con módulos, temas y actividades |
| **Metodología** | Taxonomía de Bloom, complejidad progresiva |
| **Invocación** | `subagent_type="course-outliner"` |

**Ejemplo de salida:**
```markdown
# Curso: Introducción a la Inteligencia Artificial

## Módulo 1: Fundamentos (2 horas)
### Objetivos
- Definir la inteligencia artificial
- Distinguir entre IA débil y fuerte

### Temas
1.1 Historia de la IA
1.2 Tipos de IA
1.3 Aplicaciones cotidianas

### Actividades
- Quiz de autoevaluación
- Debate: "La IA en tu vida diaria"
```

#### 2. Content Creator (Azul)
**Objetivo**: Genera contenidos de texto detallados.

| Aspecto | Detalle |
|---------|-----------|
| **Entrada** | Esquema estructurado del curso |
| **Salida** | Contenidos completos en formato markdown |
| **Estilo** | Tono de "tú", ejemplos prácticos, español neutro |
| **Invocación** | `subagent_type="content-creator"` |

#### 3. Senior Editor (Rojo)
**Objetivo**: Revisa, pule y perfecciona los contenidos escritos.

| Aspecto | Detalle |
|---------|-----------|
| **Entrada** | Borrador de los contenidos |
| **Salida** | Contenidos finales listos para publicar |
| **Modelo** | Diseñado para trabajar con modelos avanzados (ej. Sonnet) |
| **Invocación** | `subagent_type="senior-editor"` |

**Proceso de edición en 6 pasos:**
1. **Mecánica**: Corrección de gramática, ortografía y puntuación.
2. **Claridad**: Simplificación de oraciones complejas.
3. **Concisión**: Eliminación de redundancias.
4. **Consistencia**: Unificación de términos técnicos y tono.
5. **E-learning**: Adaptación a formatos de lectura digital ágiles.
6. **Fluidez**: Coherencia y transición narrativa óptima.

#### 4. SCORM Packager (Verde)
**Objetivo**: Convierte los contenidos markdown a formato SCORM.

| Aspecto | Detalle |
|---------|-----------|
| **Entrada** | Contenidos markdown aprobados |
| **Salida** | Archivo .zip compatible con el estándar SCORM 1.2 |
| **Componentes** | HTML estructurado, estilos, navegación y manifest XML |
| **Invocación** | `subagent_type="moodle-xml-formatter"` |

#### 5. Multimedia Integrator (Morado)
**Objetivo**: Crea paquetes SCORM dedicados a archivos de audio o video.

| Aspecto | Detalle |
|---------|-----------|
| **Entrada** | Archivo de audio (MP3, WAV...) o de video (MP4, WEBM...) |
| **Salida** | Paquete SCORM independiente con reproductor HTML5 integrado |
| **Funciones** | Análisis de integridad, compresión y optimización |
| **Invocación** | `subagent_type="multimedia-integrator"` |

---

## Estructura del Proyecto

```
scorm-course-generator/
│
├── .claude/                          # Configuración del agente
│   ├── agents/                       # Definiciones de los agentes
│   │   ├── course-outliner.md       # Agente de estructura del curso
│   │   ├── content-creator.md       # Agente de creación de contenido
│   │   ├── senior-editor.md         # Agente de edición
│   │   ├── moodle-xml-formatter.md  # Agente de empaquetado SCORM
│   │   └── multimedia-integrator.md # Agente multimedia
│   └── settings.local.json          # Ajustes locales
│
├── scripts/                          # Scripts de Python
│   ├── scorm_generators/            # Creadores de SCORM
│   │   ├── create_scorm_package.py  # Genera paquete de texto
│   │   ├── create_audio_scorm.py    # Genera paquete de audio
│   │   ├── create_video_scorm.py    # Genera paquete de video
│   │   └── create_sicurezza_scorm.py # Generador específico de seguridad
│   ├── content_generation/          # Scripts de procesamiento
│   │   ├── create_html_pages.py     # Conversión HTML
│   │   └── edit_course_correct.py   # Edición y corrección automática
│   └── legacy/                      # Scripts antiguos (referencia)
│       └── ...
│
├── content/                         # Contenidos de los cursos
│   ├── ai-principianti/            # Ejemplo: Curso de IA
│   │   ├── course-outline.md
│   │   ├── course-content-edited.md
│   │   └── modules/
│   ├── sicurezza-lavoro/           # Ejemplo: Seguridad Laboral
│   │   ├── modulo1-content.md
│   │   ├── modulo2-content.md
│   │   └── ...
│   └── eu-ai-act-pmi/              # Ejemplo: Ley de IA de la UE
│       ├── course-outline.md
│       └── modulo*.md
│
├── media/                           # Archivos multimedia fuente
│   ├── audio/
│   └── video/
│
├── output/                          # Salidas generadas
│   └── scorm/                      # Paquetes SCORM .zip finales
│
├── docs/                            # Documentación de soporte
│   ├── GUIA_IMPORTAR_MOODLE.md      # Guida de importación en Moodle
│   ├── GUIA_AUMENTAR_LIMITE_UPLOAD_MOODLE.md
│   ├── GUIA_COMPATIBILIDAD_LMS.md   # Matriz de compatibilidad
│   └── INSTRUCCIONES_*.md
│
├── temp/                            # Directorio temporal (ignorado)
│
├── CLAUDE.md                        # Guía de desarrollo para agentes
├── README.md                        # Este archivo
└── .gitignore
```

---

## Guía Completa de Scripts

### create_scorm_package.py

**Objetivo**: Genera un paquete SCORM a partir de un archivo markdown.

**Uso**:
```bash
python scripts/scorm_generators/create_scorm_package.py
```

**Requisitos**:
- Archivo `course-content-edited.md` en el directorio de ejecución.
- Estructura con encabezados `# Módulo X: Título`.

**Salida**:
- Directorio de desarrollo `scorm_package/` con los archivos HTML.
- Archivo empaquetado final `[nombre-del-curso]-SCORM.zip`.

---

### create_scorm_modern_package.py

**Objetivo**: Genera un paquete SCORM moderno compuesto por **1 Clase o Lectura + 1 Evaluación (cuestionario interactivo) + N Actividades**, con soporte de bloques de apoyo (`:::apoyo:::`) con video embebido de YouTube/Drive, y una lista de enlaces externos (`ENLACES.md`).

**Uso**:
```bash
# Validar configuración + contenido, sin generar nada
python scripts/scorm_generators/create_scorm_modern_package.py validate mi-curso/config.yaml

# Listar los objetos parseados (clase/lectura/evaluación/actividades/enlaces)
python scripts/scorm_generators/create_scorm_modern_package.py list mi-curso/config.yaml

# Construir el paquete SCORM (.zip)
python scripts/scorm_generators/create_scorm_modern_package.py build mi-curso/config.yaml
```

**Guía de Creación del Archivo de Configuración (`config.yaml`)**:
El archivo `config.yaml` orquesta las propiedades del curso. Debes crear un archivo de texto con extensión `.yaml` siguiendo esta estructura:
```yaml
identificador: mi-curso-id         # ID único para el paquete (sin espacios ni acentos)
titulo: "Mi Curso SCORM Moderno"   # Título del curso que aparecerá en el LMS
contenido_md: curso.md             # Ruta relativa al archivo markdown con el contenido
salida_dir: output                 # Carpeta donde se generará el paquete final
puntaje_minimo: 80                 # Puntaje mínimo para aprobar la evaluación (0 a 100)

enlaces:                           # (Opcional) Listado de enlaces de interés
  - titulo: "Sitio Oficial"
    url: "https://ejemplo.com"
    descripcion: "Documentación y recursos del tema."
```

**Guía de Creación del Archivo de Contenido (`.md`)**:
El archivo markdown referenciado (por ejemplo, `curso.md`) debe estructurarse usando títulos de nivel 1 (`# `) que definen los componentes. 

> [!NOTE]
> Se utiliza **`# Clase:`** o **`# Lectura:`** (o `# Lecturas:`) en lugar de `# Lección:` para estructurar la unidad de estudio del curso, reflejando el propósito de clases académicas y lecturas sugeridas.

```markdown
# Clase: Introducción al Tema
Aquí va el contenido teórico de la clase o lectura.

:::apoyo
Este es un bloque de apoyo destacado para tips o notas adicionales.
VIDEO: https://www.youtube.com/watch?v=EjemploVideoId
:::

# Actividad: Práctica Guiada
Descripción de la actividad o ejercicio práctico que el estudiante debe realizar.

# Evaluación: Cuestionario del Módulo
Breve introducción al quiz.

## Pregunta 1
¿Cuál es la respuesta correcta?
A) Opción incorrecta 1
B) Opción correcta
C) Opción incorrecta 2
D) Opción incorrecta 3

**Respuesta correcta: B**
**Explicación:** Opcional. Aquí se detalla la justificación de la respuesta correcta.

# Enlaces
- [Recurso Adicional](https://recurso.com) — Descripción opcional del recurso.
```

**Salida**:
- Directorio `<salida_dir>/<identificador>/` con `index.html`, `leccion.html` (o el nombre correspondiente a Clase/Lectura), `evaluacion.html`, `actividad_NN.html`, `imsmanifest.xml` y `ENLACES.md`.
- Archivo empaquetado final `<identificador>-SCORM.zip`.

**Cuándo usarlo en lugar de `create_scorm_package.py`**: cuando el curso necesita una clase o lectura con un quiz autocorregido con seguimiento SCORM de aprobado/reprobado, actividades separadas de la lección, o una lista curada de enlaces externos.

---

### create_audio_scorm.py

**Objetivo**: Crea un paquete SCORM con un reproductor de audio integrado.

**Uso**:
```bash
# Básico
python scripts/scorm_generators/create_audio_scorm.py leccion.mp3

# Con título
python scripts/scorm_generators/create_audio_scorm.py leccion.mp3 "Lección 1"

# Completo
python scripts/scorm_generators/create_audio_scorm.py leccion.mp3 "Lección 1" "Introducción general"
```

**Formatos**: MP3, WAV, OGG, M4A, AAC.

---

### create_video_scorm.py

**Objetivo**: Crea un paquete SCORM con un reproductor de video interactivo.

**Uso**:
```bash
# Básico
python scripts/scorm_generators/create_video_scorm.py video.mp4

# Con título y descripción
python scripts/scorm_generators/create_video_scorm.py video.mp4 "Video Lección 1" "Vista general"
```

**Formatos**: MP4, WEBM, MOV, AVI, MKV.

---

## Integración Multimedia

### Guía de Tamaños Recomendados

| Tamaño | Recomendación | Acción sugerida |
|------------|-----------------|--------|
| < 10 MB | Ideal | Usar directamente |
| 10-25 MB | Aceptable | Compresión opcional |
| 25-50 MB | Grande | Compresión recomendada |
| 50-100 MB | Muy grande | Compresión obligatoria |
| > 100 MB | Excesivo | Alojamiento externo (YouTube/Vimeo) |

### Compresión de Video con ffmpeg

**Alta Calidad (Recomendado)**:
```bash
ffmpeg -i input.mp4 -vcodec libx264 -crf 23 -preset medium -acodec aac -b:a 128k output.mp4
```

**Calidad Media (Tamaño reducido)**:
```bash
ffmpeg -i input.mp4 -vcodec libx264 -crf 28 -preset fast -acodec aac -b:a 96k output.mp4
```

---

---

## Centro de Ayuda y Guías Ilustradas

El proyecto incluye un centro de documentación y guías paso a paso ilustradas con capturas de pantalla, generadas bajo el estándar Schema v2 en `output/articles/`:

| Guía / Flujo | Descripción Pedagógica y Técnica | Tipo | Video MP4 |
| :--- | :--- | :---: | :---: |
| [**Instructivo: Instalación del repositorio y prompts de línea de comandos**](output/articles/guia-instalacion-prompts-linea-comandos/article.json) | Flujo guiado: clonación, entorno virtual, prompts para agentes IA y comandos de despliegue en Moodle. | how-to | [Ver Video](output/articles/guia-instalacion-prompts-linea-comandos/videotutorial.mp4) |
| [**Cómo usar Aula Lista para crear actividades del curso y conectarse a Moodle**](output/articles/guia-aula-lista-moodle/article.json) | Ejecución del pipeline de ensamblado de aula, previsualización local y conexión autenticada mediante la CLI `tiza`. | `how-to` [Ver Video](output/articles/guia-aula-lista-moodle/videotutorial.mp4) |
| [**Cómo diseñar una unidad didáctica bajo la estructura tripartita en Moodle**](output/articles/disenar-unidad-tripartita-moodle/article.json) | Metodología de la Circular N° 5: integración de **1. La Clase** (cápsulas 20-30 min), **2. La Lectura** (glosario y 20 FAQs) y **3. La Práctica** (gamificación). | `how-to` [Ver Video](output/articles/disenar-unidad-tripartita-moodle/videotutorial.mp4) |
| [**Cómo crear trivias gamificadas y desafíos Conecta Bloques en SCORM**](output/articles/crear-trivias-scorm-conecta-bloques/article.json) | Formulación de ítems de autoevaluación sin numeración fija para mezcla aleatoria y exportación a SCORM 1.2 interactivo. | `how-to` [Ver Video](output/articles/crear-trivias-scorm-conecta-bloques/videotutorial.mp4) |
| [**Cómo generar podcasts pedagógicos de dos voces con acento rioplatense**](output/articles/generar-podcasts-pedagogicos-dos-voces/article.json) | Redacción de guiones dialógicos (A/B), síntesis con `edge-tts` (Elena y Tomás) y masterización con filtros `ffmpeg` de calidad cálida. | `how-to` [Ver Video](output/articles/generar-podcasts-pedagogicos-dos-voces/videotutorial.mp4) |
| [**Cómo comprimir y empaquetar videos pedagógicos en formato SCORM**](output/articles/empaquetar-videos-comprimir-scorm/article.json) | Compresión optimizada para LMS (`crf 23`, `libx264`) y configuración de rastreo de lección al 90% visto. | `how-to` [Ver Video](output/articles/empaquetar-videos-comprimir-scorm/videotutorial.mp4) |
| [**Cómo configurar el sistema de Doble Candado para emitir certificados en Moodle**](output/articles/configurar-doble-candado-certificacion/article.json) | Encadenamiento condicional: aprobación del Examen Final Sumativo (≥ 70%) y envío de la Encuesta de Calidad obligatoria. | `how-to` [Ver Video](output/articles/configurar-doble-candado-certificacion/videotutorial.mp4) |
| [**Cómo auditar la integridad técnica de un curso con la CLI tiza**](output/articles/auditar-integridad-tecnica-tiza/article.json) | Auditoría offline de HTML peligroso, validación de dependencias entre lecciones y control de calidad institucional. | `troubleshooting` [Ver Video](output/articles/auditar-integridad-tecnica-tiza/videotutorial.mp4) |
| [**Cómo aumentar el límite de subida de archivos para paquetes SCORM en Moodle**](output/articles/aumentar-limite-subida-archivos-moodle/article.json) | Ajuste coordinado en `php.ini`, servidores web (Apache / Nginx) y políticas de administración del campus. | `troubleshooting` [Ver Video](output/articles/aumentar-limite-subida-archivos-moodle/videotutorial.mp4) |

## Importación en LMS

### Moodle

1. **Accede a tu curso** en Moodle.
2. **Activa la edición** en la esquina superior derecha.
3. Haz clic en **"Añadir una actividad o recurso"**.
4. Selecciona **"Paquete SCORM"**.
5. Sube tu archivo `.zip` generado.
6. Ajusta los parámetros de visualización (se recomienda "Nueva ventana" y tamaño responsivo) y haz clic en **"Guardar cambios"**.

---

## Estándares de Calidad

- **Pedagogía**: Contenido estructurado según la taxonomía de Bloom con dificultad incremental.
- **Formato**: Markdown a HTML responsivo. Tablas bien estructuradas con separadores estándar.
- **Idioma**: Tono cercano "tú" consistente, acentuación perfecta en español y ejemplos relevantes.
- **SCORM**: Cumplimiento estricto del esquema XML 1.2 verificado mediante validaciones de estructura.

---

## Contribuciones

1. Realiza un **Fork** del repositorio.
2. Crea una rama para tu característica: `git checkout -b feature/nueva-funcion`.
3. Haz commit de tus cambios: `git commit -m "Añade nueva función"`.
4. Envía la rama: `git push origin feature/nueva-funcion`.
5. Abre una **Pull Request**.

---

## Licencia

Este proyecto está liberado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más información.

---

*Desarrollado de forma profesional para la creación y gestión ágil de contenidos e-learning.*
