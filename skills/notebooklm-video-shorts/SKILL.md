---
name: notebooklm-video-shorts
description: Conexión con Google NotebookLM mediante CLI (nlm) para ingerir fuentes de cátedra, transcripciones de clases y papers, y estructurar guiones andragógicos optimizados para videos shorts de microlearning con HyperFrames.
---

# Ingesta Cognitiva con NotebookLM para Videos Shorts

Utiliza esta habilidad para conectar `aula lista EDUCAI` con los cuadernos de Google NotebookLM de la cátedra a través de la CLI `nlm`, extrayendo citas, transcripciones docentes y conceptos clave para crear el guion del video short microlearning (1 a 2 minutos).

## 1. Comandos de la CLI NotebookLM (`nlm`)

```bash
# Verificar autenticación activa
nlm login --check

# Listar cuadernos disponibles
nlm list

# Consultar el contenido o transcripción de una unidad temática
nlm query <notebook_id> "Sintetiza los 3 conceptos fundamentales y el dilema profesional central para un video de 90 segundos"

# Extraer citas textuales y definiciones de cátedra
nlm query <notebook_id> "Extrae citas textuales del docente y la transcripción de la clase sobre este tema"
```

## 2. Estructuración del Guion para Video Short (60 - 120 segundos)

A partir de las respuestas de NotebookLM, el guion debe organizarse en 4 fases de ritmo andragógico:

| Bloque | Tiempo | Propósito Pedagógico | Efecto Sonoro (`assets/audio/`) |
| :--- | :---: | :--- | :--- |
| **01. Hook / Gancho** | 0 - 12s | Pregunta andragógica o situación problemática real de gestión | `whoosh.mp3` + `impact-bass-1.mp3` |
| **02. Núcleo Teórico** | 12 - 45s | Los 2 o 3 conceptos indispensables extraídos de la cátedra | `click-soft.mp3` + `pop.mp3` |
| **03. Demostración Situada** | 45 - 80s | Ejemplo práctico o contraste de modelos en acción | `sparkle.mp3` + `chime.mp3` |
| **04. Cierre y Puente** | 80 - 100s | Llamada a la acción hacia la videoclase magistral y la práctica | `notification.mp3` + `riser.mp3` |

## 3. Salida del Guion
El guion generado se traslada directamente a `edtech-video-director` para montarlo en una plantilla HTML de HyperFrames y renderizarlo a MP4.
