---
name: scorm-gamification
description: Guía canónica para la compilación, configuración y personalización de paquetes interactivos SCORM 1.2 gamificados (Trivias por Turnos/Turbo, Conectabloques de pares y Exámenes Sumativos) usando el motor scorm_core y scripts de generación de Aula Lista EDUCAI.
---

# Skill: SCORM Gamification & Interactive Packager (Aula Lista EDUCAI)

Esta habilidad proporciona el estándar técnico y operativo para compilar y empaquetar actividades interactivas compatibles con SCORM 1.2 y Moodle 4.5.

## 1. Módulo Central `scorm_core`

Todos los generadores utilizan el módulo unificado `scorm_core`:
- `scorm_core.manifest.generar_manifest_scorm_unificado(...)`: Garantiza un `imsmanifest.xml` canónico con escape XML riguroso, evitando inyecciones y errores de parseo en LMS.
- `scorm_core.ai_cache.cache_ai_call(...)`: Almacena en disco (`.cache/ai/<sha256>.json`) las extracciones de IA para que ejecuciones repetidas tarden 0 segundos y consuman 0 tokens.
  - Para invalidar forzosamente la caché, exportar la variable de entorno: `EDUCAI_NO_CACHE=1`.

## 2. Generador de Trivias SCORM (`build_trivia_scorm.py`)

Ubicación: `scripts/scorm_generators/build_trivia_scorm.py`

### Modos Operativos Principales

| Modo | Comando CLI | Descripción |
| :--- | :--- | :--- |
| **Turbo 1** (1-Click) | `python scripts/scorm_generators/build_trivia_scorm.py <archivo.md> --turbo 1` | Compilación instantánea con parámetros canónicos de Aula Lista EDUCAI (Tema Neón, Modo Turno, feedback inmediato, accesibilidad WCAG y exportación a GIFT). |
| **Turbo 2** (Batch) | `python scripts/scorm_generators/build_trivia_scorm.py <directorio_o_md> --turbo 2` | Procesa en lote todos los archivos `.md` de cuestionario de un directorio o curso completo. |
| **Modo Turno** (Por pasos) | `python scripts/scorm_generators/build_trivia_scorm.py <archivo.md> --modo-turno` | Barra de navegación paso a paso con conmutación de clases CSS de alto rendimiento (sin re-renderizado DOM completo). |
| **Personalización Total** | Ver opciones abajo | Ajuste completo de tema, colores, feedback y temporizador. |

### Catálogo de Temas Visuales (`--tema`)
1. `neon` (Predeterminado): Fondo ultra-oscuro `#0c071e`, acentos dorados `#ffd700` y púrpuras.
2. `corporate`: Azul institucional marino con acentos blancos/grises.
3. `minimal`: Fondo blanco limpio, tipografía neutra, ideal para lectura sobria.
4. `high-contrast`: Contraste máximo negro/amarillo conforme a WCAG AAA.
5. `sunset`: Tonos cálidos rojizos y naranjas.
6. `forest`: Gama esmeralda y verde naturaleza.
7. `cosmic`: Violetas profundos y acentos cian espaciales.

### Opciones de Personalización Avanzada
```bash
python scripts/scorm_generators/build_trivia_scorm.py entrada.md \
  -o scorm/trivia_unidad-SCORM.zip \
  --tema neon \
  --tiempo 15 \
  --feedback end \
  --barajar \
  --exportar-gift \
  --nota-minima 70
```

## 3. Generador de Conectabloques SCORM (`build_conectabloques_scorm.py`)

Ubicación: `scripts/scorm_generators/build_conectabloques_scorm.py`

- Extrae o genera 8 pares conceptuales (Término + Definición) a partir del checkpoint de la clase.
- Genera tablero interactivo accesible con sintetizador Web Audio API libre de fugas de memoria (desconexión explícita de osciladores en `onended`).
- Compilación:
  ```bash
  python scripts/scorm_generators/build_conectabloques_scorm.py <checkpoint.md> -o scorm/conectabloques_unidad-SCORM.zip
  ```

## 4. Consulta Previa Obligatoria al Usuario

Antes de compilar la trivia interactiva de una unidad temática o examen, el agente DEBE consultar al usuario cuál es su modo preferido:
1. **Modo Turbo 1** *(Recomendado)*: 1 solo clic, tema Neón oficial, Modo Turno interactivo, feedback inmediato y exportación GIFT lista para Moodle.
2. **Modo Turno Estándar**: Navegación por pasos con tema neutro corporativo o minimalista.
3. **Modo Turbo 2**: Procesamiento por lotes si se están generando múltiples unidades a la vez.
4. **Personalización Total**: Elección detallada de tema (`neon`, `corporate`, `minimal`, etc.), límite de tiempo en minutos y momento del feedback.
