# Aula Lista EDUCAI

Sistema profesional para la generación de contenidos didácticos en formato SCORM 1.2, compatible con cualquier LMS (Learning Management System).

[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![SCORM 1.2](https://img.shields.io/badge/SCORM-1.2-green.svg)](https://scorm.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Índice

- [Descripción General](#descripción-general)
- [Flujo Autónomo «Genera la Unidad X» (Kit Aula Lista & HyperFrames)](#️-flujo-autónomo-genera-la-unidad-x-protocolo-kit-aula-lista--hyperframes)
- [Características Principales](#características-principales)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalación](#instalación)
- [Inicio Rápido](#inicio-rápido)
- [Arquitectura Multi-Agente](#arquitectura-multi-agente)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Guía Completa de Scripts](#guía-completa-de-scripts)
- [Integración Multimedia](#integración-multimedia)
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

## 🏛️ Flujo Autónomo «Genera la Unidad X» (Protocolo Kit Aula Lista & HyperFrames)

El sistema integra un flujo de trabajo autónomo de punta a punta. Cuando el docente o usuario solicita **«Genera la Unidad X»**, el agente detona automáticamente una cadena de 4 fases que produce todos los contenidos organizados en un **único directorio estructurado**, ejecuta una auto-auditoría (*Zero-Missing Gate*) y corrige cualquier elemento faltante antes de finalizar:

```text
Usuario: «Genera la Unidad X»
  │
  ├── 1. INGESTA COGNITIVA (NotebookLM con CLI nlm)
  │      Conexión al cuaderno correspondiente (ej. Unidad 1 SSC, 39 fuentes).
  │      Extracción de citas textuales, transcripciones docentes, diapositivas y papers.
  │
  ├── 2. PRODUCCIÓN MULTIMEDIA REAL (HyperFrames + SVG/Chrome)
  │      • Video Short Microlearning (1920x1080, 30fps): Composición HTML/GSAP renderizada
  │        headless a MP4 mediante el motor HyperFrames (captura chromium + encoding ffmpeg).
  │      • Banners Visuales Panorámicos: Generación SVG y renderizado PNG con tipografía limpia.
  │      • Infografías de Síntesis: Diagramas conceptuales de alta resolución.
  │      • Diapositivas: Archivo de placas oficiales descargables (.pptx).
  │
  ├── 3. MAQUETACIÓN AULA TRIPARTITA (Moodle 4.5 / Bootstrap 4.6.2)
  │      • Encabezado: Banner + frase de encuadre (2 oraciones) + 3 preguntas andragógicas (Circular 5).
  │      • 1. La Clase: Dual Video (Short HyperFrames + Videoclase magistral 20-30m target="_blank").
  │      • 2. La Lectura: 3 lecturas didácticas, infografía incrustada, glosario, FAQs y bibliografía.
  │      • 3. La Práctica: Consigna orientadora obligatoria («se resuelve con los videos...»),
  │        ficha de desafíos interactivos y caso situado de gestión con rúbrica.
  │
  └── 4. DIRECTORIO ÚNICO, EMPAQUETADO SCORM & AUTO-AUDITORÍA (Zero-Missing Gate)
         • Empaquetado SCORM: Conectabloques (8 pares) + Trivia (sin numeración rígida).
         • Examen Final Sumativo: Si es la unidad de cierre, genera examen integrador con candado Moodle.
         • Consolidación en directorio único jerarquizado y validación con tiza comprobar.
```

### 🗣️ Consulta Obligatoria de Modo de Trivia y Examen al Usuario

Al momento de generar la **Gran Trivia SCORM** de cada unidad o el **Examen Final Sumativo**, el agente de IA **debe pausar y preguntar expresamente al usuario qué modo prefiere utilizar**, describiéndole las características y configuraciones de cada uno:

1. **🚀 Modo Turbo 1 (Automático 1-Click)**:
   - *Configuración*: 10 preguntas de dificultad intermedia, 60% de aprobación, 30 minutos de tiempo límite, orden aleatorio (shuffle), estilo Neón accesible de alto contraste y retroalimentación inmediata. Empaquetado directo sin pasos intermedios.
2. **🎮 Modo Turno Estándar (Interactivo con Navegación por Pasos)**:
   - *Configuración*: Navegación bidireccional (`← Anterior` y `Siguiente →`), barra interactiva superior de turnos para saltar libremente y revisar preguntas antes de entregar, 70% de aprobación, sin límite de tiempo estricto y retroalimentación pedagógica contextual inmediata.
3. **⚡ Modo Turbo 2 (Generación Masiva por Lotes / Batch)**:
   - *Configuración*: Procesa automáticamente todas las unidades o cuestionarios existentes en el directorio y genera todos los paquetes SCORM 1.2 correspondientes en una sola pasada.
4. **🎨 Personalización Total**:
   - *Configuración a medida del docente*: Selección libre de Tema visual (`neon`, `corporate`, `minimal`, `high-contrast`, `sunset`, `forest`, `cosmic`), paleta de colores hexadecimales (`--neon-primary`, `--neon-accent`), tiempo límite en minutos, momento del feedback (`immediate` o `end`), puntaje de aprobación (ej. 75%, 80%) y exportación paralela a formato GIFT para el banco nativo de Moodle.

---

### 🎯 Detalle de Actividades Formativas, Consignas y Examen Final

| Componente | Fase de Creación | Ubicación y Archivo | Regla Técnica & Pedagógica (Kit Aula Lista) |
| :--- | :---: | :--- | :--- |
| **Consignas de la Práctica** | **Fase 3** | `04_la_practica/04_tarea_la_practica.html` | Incluye la **consigna orientadora obligatoria**: *«Esta práctica se resuelve con lo visto en los videos docentes; no necesitás repasar toda la bibliografía obligatoria para completarla»*. Detalla los dos desafíos SCORM y el caso situado con su rúbrica. |
| **Conectabloques SCORM** | **Fases 1, 3 y 4** | `scorm/conectabloques_unidad-SCORM.zip` | 8 pares conceptuales clave extraídos de las fuentes de cátedra. Compilado con Web Audio, temporizador, interfaz synthwave responsiva y reporte de score al libro de calificaciones de Moodle. |
| **Gran Trivia SCORM** | **Fases 1, 3 y 4** | `scorm/trivia_unidad-SCORM.zip` | Banco de preguntas formativas **sin numeración rígida en los enunciados** (sin "Pregunta 1") para permitir la aleatorización anti-trampa en Moodle. Incluye retroalimentación pedagógica inmediata por opción. |
| **Examen Final Sumativo** | **Fases 1, 3 y 4** *(Unidad Final)* | `examen_final/` o `scorm/modulo_completo-SCORM.zip` | Se activa cuando la instrucción solicita la **última unidad del programa** (o el cierre de cursado). Incluye `banner_examen_final.png`, consigna formal de acreditación (duración 45-50 min, nota mínima 70%), banco aleatorizado global y **restricción de acceso condicionada (candado de Moodle)** hasta completar las prácticas previas. |

### Estructura Canónica de Directorio Único

Todos los artefactos se generan en una sola carpeta por unidad, respetando la siguiente jerarquía:

```text
output/<unidad>_kit_aula_lista/
├── 01_encabezado/
│   ├── banner_unidad.png                       # Banner visual panorámico
│   ├── banner_unidad.svg                       # Fuente vectorial
│   └── 01_etiqueta_encabezado_y_banner.html    # Etiqueta Moodle (área de texto y medios)
│
├── 02_la_clase/
│   ├── video_short_hyperframes.mp4             # Video MP4 renderizado por HyperFrames
│   ├── hyperframes_short/                      # Proyecto fuente HyperFrames (index.html, GSAP)
│   ├── diapositivas_unidad.pptx                # Presentación de placas docentes
│   └── 02_pagina_la_clase.html                 # Página Moodle con Dual Video
│
├── 03_la_lectura/
│   ├── infografia_unidad.png                   # Infografía conceptual de síntesis
│   ├── infografia_unidad.svg                   # Vectorial editable
│   └── 03_pagina_la_lectura.html               # Página Moodle con marco teórico y glosario
│
├── 04_la_practica/
│   └── 04_tarea_la_practica.html               # Tarea Moodle con consigna orientadora y caso
│
└── scorm/
    ├── conectabloques_unidad-SCORM.zip         # 8 pares conceptuales, temporizador, audio
    ├── trivia_unidad-SCORM.zip                 # Preguntas aleatorizables sin numeración rígida
    └── modulo_completo-SCORM.zip               # Paquete SCORM integrador de la asignatura
```

### Checklist Obligatorio de Autoverificación (Zero-Missing Gate)

Antes de responder al usuario, el agente auto-audita 10 puntos canónicos:
1. `banner_unidad.png`: Banner visual de cabecera creado y enlazado.
2. `01_etiqueta_...`: Contiene el banner, la síntesis de 2 oraciones y las 3 preguntas andragógicas.
3. `video_short_hyperframes.mp4`: Video short de microlearning renderizado con HyperFrames.
4. `02_pagina_...`: Integra Dual Video (Short + Clase magistral docente de 20-30 min con `target="_blank"`).
5. `diapositivas.*`: Archivo de placas de la clase presente y enlazado.
6. `03_pagina_...`: Módulo teórico estructurado con Glosario de términos clave y bloque FAQ.
7. `infografia_unidad.png`: Infografía conceptual de síntesis creada e incrustada en la lectura.
8. `04_tarea_...`: Incluye la consigna obligatoria (*«Esta práctica se resuelve con lo visto en los videos docentes...»*) y caso con rúbrica.
9. `conectabloques-SCORM.zip` y `trivia-SCORM.zip`: Paquetes SCORM 1.2 interactivos compilados.
10. `tiza comprobar *.html`: Auditoría ejecutada con éxito (`Paso COMPROBAR: ok`) en todos los ficheros HTML.

> **Directiva de Cierre Obligatorio y Autocorrección (Zero-Missing Gate & Self-Healing):**
> Una vez creados todos los contenidos solicitados, el agente DEBE realizar una **revisión exhaustiva de verificación física en disco** de todos y cada uno de los 10 componentes y el examen final.
> Si se detecta que **falta cualquiera de ellos**, está terminantemente prohibido dar por concluida la tarea o consultar al usuario: el sistema debe auto-repararse inmediatamente (*Self-Healing*), invocando al agente o script especializado hasta satisfacer el 100% de la lista antes de cerrar la respuesta.

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

### Multimedia y Suite Audiovisual HyperFrames
- **Renderizado Headless de Video (HyperFrames)**: Generación programática de videos en Chrome Headless (1080p y 9:16 vertical) con animaciones GSAP deterministas.
- **Plantillas Maestras Verificadas**: Showcases de cursos de 60s, adaptaciones para reels/shorts 9:16, tutoriales paso a paso de 120s con cursor interactivo y renovaciones de aula de 90s.
- **Banco Sonoro Multicapa Portable (`assets/audio/`)**: 10 efectos sonoros diegéticos calibrados (whoosh, chime, sparkle, pop, impact), BGMs ambientales e institucionales al 12-15% y pistas VoiceOver de locución profesional.
- **SCORM de Audio**: Reproductor HTML5 con seguimiento de finalización
- **SCORM de Video**: Reproductor con barra de progreso y finalización automática al 90% visto
- **Compresión Inteligente**: Optimización automática con ffmpeg (CRF 23)

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
git clone https://github.com/superpollo02/scorm-course-generator.git "aula lista EDUCAI"
cd "aula lista EDUCAI"
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

#### 4. SCORM Architect (Amarillo)
**Objetivo**: Compila interactivos gamificados SCORM 1.2 (Trivias Turbo/Turno, Conectabloques de pares y Exámenes Sumativos) optimizados con `scorm_core`.

| Aspecto | Detalle |
|---------|-----------|
| **Entrada** | Cuestionarios markdown, pares conceptuales o checkpoints |
| **Salida** | Paquetes `.zip` SCORM 1.2 (`cmi.core.score.raw`), GIFT de Moodle y caché IA en disco |
| **Capacidades** | Modo Turbo 1 y 2, Modo Turno, 7 temas visuales Neón/WCAG, Web Audio API y consulta previa interactiva |
| **Invocación** | `subagent_type="scorm-architect"` |

#### 5. Moodle Formatter & Tiza Auditor (Verde)
**Objetivo**: Maqueta el HTML responsivo de las unidades para Moodle 4.5 y valida con el linter de Tiza.

| Aspecto | Detalle |
|---------|-----------|
| **Entrada** | Textos instruccionales, infografías y enlaces a videos/SCORM |
| **Salida** | Archivos HTML canónicos (`01_etiqueta...`, `02_pagina...`, `03_pagina...`, `04_tarea...`) |
| **Filtro** | Bootstrap 4.6.2, Font Awesome 6 y aprobación estricta `tiza comprobar` |
| **Invocación** | `subagent_type="moodle-xml-formatter"` |

#### 6. Multimedia Integrator (Morado)
**Objetivo**: Diseña activos gráficos vectoriales (banners panorámicos, infografías conceptuales) y diapositivas de clase.

| Aspecto | Detalle |
|---------|-----------|
| **Entrada** | Insumos de la cátedra y especificaciones de marca |
| **Salida** | Banners PNG/SVG, Infografías teóricas de síntesis y presentaciones PPTX/PDF |
| **Invocación** | `subagent_type="multimedia-integrator"` |

---

## Estructura del Proyecto

```
aula lista EDUCAI/
│
├── templates/                        # Plantillas maestras de video programático HyperFrames
│   ├── moodle-showcase-60s.html      # Showcase promocional de alto impacto (1080p, 60s)
│   ├── moodle-vertical-9-16.html     # Adaptación vertical (1080x1920) para Shorts y Reels
│   ├── moodle-makeover-90s.html      # Renovación de aula en 8 escenas (90s)
│   ├── moodle-tutorial-120s.html     # Tutorial técnico con cursor reactivo animado (120s)
│   └── unidad*-*.html                # Plantillas curriculares sincronizadas (Unidades 2 a 8)
│
├── assets/                           # Activos multimedia portables
│   └── audio/                        # Banco sonoro multicapa (SFX diegéticos, BGMs, VoiceOvers)
│
├── scorm_core/                                  # Motor unificado de empaquetado y optimización
│   ├── manifest.py                              # Generador canónico de imsmanifest.xml con escape XML
│   └── ai_cache.py                              # Caché de IA en disco SHA-256 (0 tokens en repeticiones)
│
├── skills/                                      # Habilidades ejecutables de Antigravity
│   ├── edtech-moodle-video/                     # Metodología y captura de recorridos Moodle y SCORM
│   ├── notebooklm-video-shorts/                 # Ingesta con NotebookLM (CLI nlm) para guiones de shorts
│   ├── hyperframes-render/                      # Renderizado programático en MP4 con HyperFrames en Chrome Headless
│   ├── diseno-instruccional-aula-tripartita/    # Redacción de intro (2 oraciones + 3 preguntas) y consignas
│   └── scorm-gamification/                      # Compilación y personalización SCORM 1.2 (Turbo 1/2, Turno, Neón)
│
├── agents/ y .claude/agents/                    # Agentes y subagentes especializados
│   ├── asistente-notebooklm.md                  # Ingesta de fuentes y guiones de microlearning con NotebookLM
│   ├── course-outliner.md                       # Arquitectura curricular Kit Aula Lista y Aula Tripartita
│   ├── content-creator.md                       # Redacción de marcos teóricos, intro, consignas y rúbricas
│   ├── senior-editor.md                         # Auditoría editorial, consigna obligatoria y anti-trampa
│   ├── multimedia-integrator.md                 # Diseño de banners panorámicos, infografías vectoriales y PPTX
│   ├── edtech-video-director.md                 # Director audiovisual HyperFrames (renders MP4 a 1080p y 9:16)
│   ├── scorm-architect.md                       # Compilación SCORM 1.2 (Trivias Turbo/Turno, Conectabloques, GIFT)
│   ├── moodle-xml-formatter.md                  # Maquetación HTML responsiva (Bootstrap 4.6.2) y auditoría Tiza
│   └── auditor-calidad-aula-lista.md            # Auto-auditoría exhaustiva Zero-Missing Gate y Self-Healing
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

### build_trivia_scorm.py (Gran Trivia SCORM con Modo Turno, Temas Neón y Modo Turbo)

**Objetivo**: Genera paquetes SCORM 1.2 interactivos de autoevaluación y trivia gamificada con navegación por turnos, temporizador, barra de accesibilidad WCAG para el estudiante y sincronización de puntaje con Moodle (`cmi.core.score.raw`).

**Ejemplos de Uso**:
```bash
# 1. Modo Turbo 1 (1-Click Automático: 10 preguntas, 60% aprobación, 30 min, aleatorio, Neón)
python scripts/scorm_generators/build_trivia_scorm.py cuestionario.md --turbo 1

# 2. Modo Turbo 2 (Por lotes / Batch: procesa carpetas completas y empaqueta todo en SCORM 1.2)
python scripts/scorm_generators/build_trivia_scorm.py content/unidades/ --turbo 2

# 3. Personalización de Temas Visuales (neon, corporate, minimal, high-contrast, sunset, forest, cosmic)
python scripts/scorm_generators/build_trivia_scorm.py cuestionario.md --tema cosmic --tiempo 20 --barajar

# 4. Personalización Fina Neón y Exportación simultánea a formato GIFT de Moodle
python scripts/scorm_generators/build_trivia_scorm.py cuestionario.md --tema neon --neon-accent "#00f3ff" --exportar-gift
```

---

### build_conectabloques_scorm.py (Conectabloques SCORM con Web Audio)

**Objetivo**: Genera un paquete SCORM 1.2 interactivo de emparejamiento conceptual de 8 pares extraídos de las lecturas, con síntesis de sonido procedural vía Web Audio API, temporizador dinámico y reporte directo al libro de calificaciones de Moodle.

**Ejemplos de Uso**:
```bash
# Empaquetado estándar de Conectabloques desde markdown de pares conceptuales
python scripts/scorm_generators/build_conectabloques_scorm.py content/conectabloques_unidad1.md

# Con ruta de salida personalizada
python scripts/scorm_generators/build_conectabloques_scorm.py content/conectabloques_unidad1.md -o output/scorm/conectabloques_u1.zip
```

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
