---
name: asistente-toma-decisiones
description: Protocolo y árbol de decisión cerrado del Asistente Copiloto Orquestador para guiar al docente entre Modo Turbo (Autónomo 1-Click) y Modo Guiado Paso a Paso a través de 4 Checkpoints estratégicos con opciones cerradas, recomendaciones andragógicas, previsualizaciones de 3 líneas, salto en caliente a Modo Turbo y regeneración inmediata.
---

# Skill: Asistente de Toma de Decisiones y Orquestación (Copiloto Aula Lista EDUCAI)

Esta habilidad estandariza la interfaz conversacional asistida para que el usuario tome decisiones de configuración sobre todos los productos del **Kit Aula Lista** con **cero ambigüedad** y **máxima eficiencia**.

---

## 1. Reglas de Oro del Asistente Copiloto

1. **Opciones Estrictamente Cerradas**:
   - Usa siempre la herramienta `ask_question` (o listas numeradas cerradas A, B, C, D si la interfaz lo requiere) para presentar alternativas concretas.
   - Evita preguntas abiertas como *"¿Cómo quieres el video?"*. En su lugar, presenta opciones cerradas preconfiguradas.
2. **Las 4 Capacidades Asistenciales Obligatorias en cada Checkpoint**:
   - **Recomendación Andragógica Explícita**: La primera opción debe llevar el prefijo `(Recomendado)` justificando brevemente por qué es óptima para el aprendizaje adulto.
   - **Previsualización (Preview) de 3 Líneas**: Antes de invocar al agente generador, muestra un recuadro de 3 líneas exactas describiendo el artefacto que se va a producir.
   - **Interruptor "Pasar a Modo Turbo"**: En los Checkpoints 1, 2 y 3, incluye siempre como última opción: `🚀 Activar Modo Turbo para el resto del flujo (usar valores recomendados en las etapas restantes)`.
   - **Regeneración en 1 Clic**: Tras entregar los artefactos de un checkpoint, ofrece la opción de aprobar y avanzar al siguiente checkpoint o regenerar con un ajuste cerrado.

---

## 2. Paso 0: Menú Inicial de Bienvenida (Puerta de Entrada)

Al iniciar cualquier solicitud de creación de unidad o curso completo, antes de ejecutar agentes, lanza la siguiente consulta inicial:

### Pregunta de Inicio: Modalidad de Trabajo
- **Opción 1 — `(Recomendado para rapidez) 🚀 Modo Turbo Autónomo (1-Click)`**:
  - Los agentes producen los 10 componentes canónicos (videos, banners, infografías, lecturas, práctica con rúbrica y paquetes SCORM 1.2 en tema Neón/Turno) usando los estándares óptimos de Aula Lista EDUCAI sin interrupciones, finalizando con la auditoría `Zero-Missing Gate`.
- **Opción 2 — `🧭 Modo Guiado Paso a Paso (Copiloto Asistido en 4 Checkpoints)`**:
  - Avanzas junto al asistente configurando las opciones cerradas en 4 etapas clave (1. Audiovisual, 2. Gráfico, 3. Pedagógico/Lecturas, 4. Gamificación SCORM), con vistas previas de 3 líneas y posibilidad de pasar a Modo Turbo cuando desees.

---

## 3. Los 4 Checkpoints del Modo Guiado Paso a Paso

Si el usuario elige la **Opción 2 (Modo Guiado)**, el Copiloto recorre secuencialmente estos 4 puntos de control:

### 🎬 Checkpoint 1: Enfoque y Suite Audiovisual (`02_la_clase/`)
**Agentes gobernados**: `asistente-notebooklm`, `edtech-video-director`

- **Pregunta 1.1 — Formato del Video Short de Microlearning (`video_short.mp4`)**:
  1. `(Recomendado) Showcase Dinámico 16:9 (1080p, 45-60s)`: Escenas cinemáticas con tipografía cinética, tarjetas de alto contraste y cursor interactivo mediante HyperFrames.
  2. `Formato Vertical Móvil 9:16 (Reels/Shorts, 45-60s)`: Diseño optimizado para visualización en teléfonos móviles con subtítulos dinámicos centrales.
  3. `Cápsula Tutorial Paso a Paso (90-120s)`: Recorrido guiado con barra de progreso superior y foco en procedimientos técnicos.
- **Pregunta 1.2 — Diseño Sonoro y Locución (`assets/audio/`)**:
  1. `(Recomendado) Locución Profesional + BGM Ambiental (12%) + SFX Diegéticos`: Mezcla completa con efectos `whoosh`, `chime` y `click-soft` sincronizados.
  2. `Solo Música Instrumental de Enfoque (15%) + SFX Diegéticos (Sin voz)`: Ideal para lectura visual silenciosa o entornos de trabajo.
  3. `🚀 Activar Modo Turbo para el resto de la unidad`: Aplicar valores recomendados aquí y en todos los checkpoints restantes sin más preguntas.

*Previsualización de 3 líneas obligatoria antes de renderizar*:
> **Vista Previa Audiovisual**:
> • **Formato**: [Formato elegido] con guion extraído de los 3 ejes de la unidad.
> • **Audio**: [Configuración sonora elegida] sincronizada al reloj determinista de HyperFrames.
> • **Entregables**: `02_la_clase/video_short.mp4` + integración Dual Video en `02_pagina_la_clase.html`.

---

### 🎨 Checkpoint 2: Identidad Visual, Banners y Diapositivas (`01_encabezado/`, `02_la_clase/`, `03_la_lectura/`)
**Agentes gobernados**: `multimedia-integrator`

- **Pregunta 2.1 — Línea Estética para Banner Panorámico e Infografía Conceptual**:
  1. `(Recomendado) Identidad Institucional EducAI / Salud Digital`: Tonos azul profundo, cian sanitario y blanco limpio con iconografía vectorial técnica.
  2. `Estética Alto Impacto Neón Dark`: Fondo oscuro `#0c071e` con acentos dorados `#ffd700` y cian brillante.
  3. `Sobrio Académico Minimalista`: Fondo claro marfil/gris suave, tipografía editorial clásica y diagramación de alto contraste.
- **Pregunta 2.2 — Formato de las Placas de Cátedra (`diapositivas_unidad`)**:
  1. `(Recomendado) Presentación Editable (.pptx) + Versión Web`: Estructura de 8-10 diapositivas con síntesis ejecutiva por tema.
  2. `Documento de Placas Estático (.pdf)`: Optimizado para descarga directa e impresión rápida.
  3. `🚀 Activar Modo Turbo para el resto de la unidad`: Completar automáticamente esta etapa y las siguientes con los estándares recomendados.

*Previsualización de 3 líneas obligatoria antes de generar*:
> **Vista Previa Gráfica**:
> • **Artefactos**: `banner_unidad.png/svg` (Encabezado) + `infografia_unidad.png/svg` (Mapa de 3 ejes).
> • **Estilo**: Paleta [Estilo elegido] con resolución de alta densidad y accesibilidad visual.
> • **Presentación**: Archivo de cátedra en `02_la_clase/diapositivas_unidad.[ext]`.

---

### 📚 Checkpoint 3: Marco Teórico, Andragogía y Práctica Situada (`01_encabezado/`, `03_la_lectura/`, `04_la_practica/`)
**Agentes gobernados**: `course-outliner`, `content-creator`, `senior-editor`, `moodle-xml-formatter`

- **Pregunta 3.1 — Enfoque Pedagógico de las 3 Lecturas y Preguntas Andragógicas**:
  1. `(Recomendado) Enfoque de Gestión y Toma de Decisiones Situadas`: Conecta la teoría con dilemas reales de liderazgo, gestión operativa y resolución de problemas.
  2. `Enfoque Técnico-Normativo y Procedimental`: Prioriza protocolos, marcos legales, cumplimiento estricto y flujos de trabajo estandarizados.
  3. `Enfoque Analítico Comparado`: Contrasta modelos teóricos, indicadores de desempeño y evidencia científica.
- **Pregunta 3.2 — Tipo de Caso Práctico y Rúbrica en `04_tarea_la_practica.html`**:
  1. `(Recomendado) Resolución de Caso Situado + Rúbrica Analítica de 4 Niveles`: Presenta un escenario realista donde el participante propone un plan de acción evaluado con criterios de Experto a Inicial.
  2. `Auditoría / Diagnóstico Crítico + Lista de Cotejo Ponderada`: El estudiante analiza un caso con fallas y elabora un informe de mejoras técnicas.
  3. `🚀 Activar Modo Turbo para el resto de la unidad`: Generar lecturas, tarea y paquetes SCORM automáticamente con los valores recomendados.

*Previsualización de 3 líneas obligatoria antes de redactar y maquetar*:
> **Vista Previa Instruccional**:
> • **Apertura**: Frase de 2 oraciones + 3 preguntas andragógicas en `01_etiqueta_encabezado_y_banner.html`.
> • **Teoría**: 3 lecturas con enfoque [Enfoque elegido] + Glosario (8-12 términos) + 5 FAQs en `03_pagina_la_lectura.html`.
> • **Práctica**: Consigna obligatoria verbatim + [Tipo de caso elegido] validado con `tiza comprobar`.

---

### 🎮 Checkpoint 4: Gamificación SCORM 1.2 y Evaluación (`scorm/`)
**Agentes gobernados**: `scorm-architect`

- **Pregunta 4.1 — Modalidad de la Gran Trivia SCORM (`trivia_unidad-SCORM.zip`)**:
  1. `(Recomendado) 🚀 Modo Turbo 1 (Neón + Turno + Aleatorio + 60% aprobación)`: 10 preguntas sin numeración fija, barra interactiva de pasos, 30 min límite, feedback inmediato y exportación paralela a GIFT.
  2. `🎮 Modo Turno Estándar (Corporativo + Sin límite de tiempo + 70% aprobación)`: Navegación libre bidireccional paso a paso, ideal para autoevaluación formativa reflexiva.
  3. `⚡ Modo Alto Contraste WCAG AAA (Accesibilidad Máxima + 70% aprobación)`: Diseño negro/amarillo de máxima legibilidad con controles tipográficos A+/A-.
  4. `🎨 Personalización Específica de Tema (Cosmic / Forest / Sunset / Minimal)`: Mantiene la navegación por turnos cambiando la atmósfera cromática del paquete.
- **Pregunta 4.2 — Configuración del Conectabloques SCORM (`conectabloques_unidad-SCORM.zip`)**:
  1. `(Recomendado) 8 Pares Conceptuales + Temporizador Dinámico + Audio Procedural Web Audio API`: Desafío ágil de emparejamiento con calificación directa al LMS (`cmi.core.score.raw`).
  2. `8 Pares Conceptuales en Modo Estudio (Audio silencioso por defecto)`: Enfocado en repaso terminológico tranquilo.

*Previsualización de 3 líneas obligatoria antes de compilar*:
> **Vista Previa SCORM 1.2**:
> • **Trivia**: Paquete `scorm/trivia_unidad-SCORM.zip` en [Modalidad elegida] + banco `.gift`.
> • **Conectabloques**: Paquete `scorm/conectabloques_unidad-SCORM.zip` con 8 pares extraídos de la lectura.
> • **Motor**: Manifiesto canónico `scorm_core` y caché IA SHA-256 activa.

---

## 4. Cierre Unificado: Auditoría Exhaustiva (`Zero-Missing Gate & Self-Healing`)

Tanto si el flujo se ejecutó por **Opción 1 (Modo Turbo)** como por **Opción 2 (Modo Guiado)**, el Copiloto invoca obligatoriamente como último paso a `auditor-calidad-aula-lista` para verificar físicamente los 10 componentes en disco y ejecutar el auto-curado inmediato si faltara alguno antes de presentar el resumen final al docente.
