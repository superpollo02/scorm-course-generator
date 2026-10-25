---
name: hyperframes-render
description: Metodología y pipeline de producción para renderizar videos programáticos deterministas en MP4 mediante HyperFrames (Chrome Headless + ffmpeg) con sincronización de audio diegético y layouts 1080p y 9:16 vertical.
---

# Renderizado Programático de Video con HyperFrames

Esta habilidad rige la producción, verificación y renderizado headless a MP4 del video short microlearning (`video_short.mp4`) dentro del protocolo **Kit Aula Lista**.

## 1. Comandos del Pipeline de Renderizado

```bash
# 1. Previsualizar composición en tiempo real (navegador con hot reload)
npx hyperframes preview templates/moodle-showcase-60s.html

# 2. Validación de tiempos, oclusiones de capa y contraste WCAG AA
npx hyperframes check templates/moodle-showcase-60s.html

# 3. Renderizar headless a video MP4 final (1080p determinista a 30fps)
npx hyperframes render templates/moodle-showcase-60s.html --output output/unidad1_kit_aula_lista/02_la_clase/video_short.mp4
```

## 2. Invariantes de Ingeniería HyperFrames

1. **Determinismo Absoluto**:
   - Todo el avance temporal está controlado por la timeline de GSAP pausada (`window.__timelines["main"]`).
   - Jamás utilizar `Date.now()`, `Math.random()` sin semilla o transiciones CSS basadas en reloj del navegador (`transition:`).
2. **Capas y Oclusión (`data-layout-allow-*`)**:
   - Para sellos animados, tarjetas flotantes o el cursor virtual (`#virtual-cursor`), declarar siempre:
     ```html
     <div class="floating-badge" data-layout-allow-overlap="true" data-layout-allow-occlusion="true">
     ```
3. **Diseño Sonoro y Balance Estéreo**:
   - La música de fondo (`assets/audio/bgm*.mp3`) se calibra al 12% - 15% de volumen (`data-volume="0.12"`).
   - Efectos diegéticos en puntos clave de inflexión visual (`whoosh` en cambios de escena, `click` en botones, `chime` en aciertos, `impact` en títulos principales).
4. **Entrega Física Obligatoria**:
   - El renderizado debe producir el archivo físico en `02_la_clase/video_short.mp4` (o `.webm`).
