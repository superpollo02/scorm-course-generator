# {{PROJECT_NAME}} — Universal AI Workflow (Updated 26/08/2026)

This file is the single, canonical entry point for all AI agents (Gemini, Antigravity, Claude, GPT/Codex, Cursor, Copilot, etc.). The workflow is 100% agent-agnostic and tool-independent.

---

## 🤖 Universal Agent Self-Adaptation

Every AI agent executing in this repository MUST:
1. **Self-Detect Environment**: Inspect your active tools, IDE capabilities, available skills, and shell environment.
2. **Execute Workflow Core**: Enforce the exact same lane selection, zero-grep traversal (`traverse.ps1`), 30-line handoff limit (`.ai/HANDOFF.md`), and phase gates — regardless of whether you are Gemini, Antigravity, Claude, GPT/Codex, Cursor, Copilot, Cline, or a custom LLM agent.
3. **Graceful Skill Scaling**:
   - **With optional skills** (`ponytail`, `caveman`, `rtk`): Use them automatically for maximum token savings and lean code generation.
   - **Without optional skills**: The workflow operates at 100% functionality using native terminal commands (`powershell`/`bash`) and standard file edits. Zero required external dependencies.

---

## ⚡ Recommended Token-Saving Skills & Tools

To achieve maximum performance and save up to 70% context tokens, the following skills/tools are highly recommended:
- **`ponytail` skill**: Enables ultra-lean coding mode — cuts over-engineering, unrequested abstractions, and boilerplate.
- **`caveman` skill**: Enables direct output mode — eliminates conversational filler tokens.
- **`rtk` (Rust Token Killer)** / **Output Filters**: Filters noisy CLI output (`git diff`, `test`, `build`, `lint`) before returning it to the LLM context.

---

## 🚦 1. Choose Workflow Lane

- **Answer Lane**: Question or architectural explanation only → Read-only lookup, respond directly. No workflow files modified.
- **Small Lane**: Simple bug fix or feature modifying ≤2 product files at a known edit site with no API/schema/database/security/payment/concurrency risks → Run `brain-recall.ps1`, edit files, run focused test, call `complete-task.ps1`.
- **Full Lane**: Multi-step features, refactors, complex bug fixes, or structural changes → Follow full lifecycle: **Plan → Build → Review**.

---

## 🔍 2. Full-Lane Startup & Zero-Grep Traversal

Read `.ai/HANDOFF.md`, then run session startup once:
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ai-workspace/scripts/brief.ps1 -Role <planner|builder|reviewer> -Query "<task keywords>"
```

> [!IMPORTANT]
> **Zero-Grep Traversal Rule**: Never run a wide `grep` or `rg` without querying index tables first.
> ```powershell
> powershell -File ai-workspace/scripts/traverse.ps1 -Symbol <name>      # Query symbol_index.md
> powershell -File ai-workspace/scripts/traverse.ps1 -Endpoint <route>    # Query endpoint_index.md
> powershell -File ai-workspace/scripts/traverse.ps1 -Err <text>          # Query incident/error cache
> powershell -File ai-workspace/scripts/traverse.ps1 -Module <keyword>    # Query domain-manifest.yaml
> powershell -File ai-workspace/scripts/traverse.ps1 -Brain <keywords>   # Query brain memory
> ```
> Only fall back to `rg` if `traverse.ps1` returns `TRAVERSE_MISS`.

---

## 🔄 3. Full-Lane Lifecycle Phases

1. **Plan Phase**:
   - Inspect routed source files (from `brief.ps1` output).
   - Write/update `.ai/HANDOFF.md` with: Goal, Non-goals, Exact paths+symbols, Ordered edits (max 8 bullets), Invariants, Focused checks, Dirty-file boundaries.
   - Do NOT modify product code during planning.
2. **Plan-Readiness Gate**:
   - Proceed to Build if `.ai/HANDOFF.md` has exact edit sites, clear scope, invariants, and no open blockers.
   - If blocked or ambiguous, refine plan first.
3. **Build Phase**:
   - Run `validate-handoff.ps1` pre-build gate before starting edits.
   - Implement minimal changes within named scope (use `ponytail` mindset — no unrequested abstractions).
   - Run named verification checks. Update `.ai/HANDOFF.md` changed files list at phase end.
4. **Review Phase**:
   - Inspect git diff. Verify correctness, contracts, security, regressions, and tests.
   - Report findings as `path:line`.
   - After clean verification, run `complete-task.ps1` once to record reusable lessons and update brain cache.

---

## 💰 4. Context Budget & Token Savings

- Keep `.ai/HANDOFF.md` under **30 lines**.
- Open only brief-routed files. Do not flood context with unreferenced codebase files.
- Raw output is disposable — save reusable facts to `ai-workspace/agents/research.md` and novel bug cause/fix to `ai-workspace/agents/lessons-learned.md`.
- `brief.ps1` metrics record classification/cache hits — do not report fake token metrics.

---

## ⚡ 5. Output Compression (Optional Enhancement)

If your agent supports CLI output filtering (e.g. `rtk` on Gemini/Antigravity, `--compact` / `head` on Claude, or PowerShell pipeline filters on Codex):
- Prefix noisy output commands (`git status`, `git diff`, test suites, lint runs) with output filter.
- Keep short single-file reads (`Get-Content`, targeted 3-line search) direct.



---

## 🎥 6. Mediación Audiovisual Dual y Publicación Moodle con Tiza

Para los cursos organizados bajo la metodología **Aula Tripartita** (`1. La Clase`, `2. La Lectura`, `3. La Práctica`):

1. **Sección «# Clase:» con Video Adicional en `scorm_modern`**:
   - En `modulo_scorm.md` o checkpoints, la sección `# Clase:` admite video principal (`VIDEO: <url>`) y múltiples videos adicionales:
     ```markdown
     :::apoyo
     VIDEO: https://youtu.be/<id>
     VIDEO_ADICIONAL: https://vimeo.com/<id> | Video-Lección Magistral
     VIDEO_ADICIONAL: media/microlearning.mp4 | Cápsula Corta MP4
     :::
     ```
   - Plataformas soportadas: YouTube (`youtube-nocookie.com`), Vimeo (`player.vimeo.com`), Google Drive y videos locales (`.mp4`, `.webm`).

2. **Skill de Tiza para Moodle**:
   - La skill `tiza` (`.agents/skills/tiza/SKILL.md`) permite validar offline con `tiza comprobar` y publicar en Moodle páginas y etiquetas con estilo responsivo Bootstrap 4.6.2, siguiendo la guía especializada `guias/clase-video-scorm.md`.

---

## 🏛️ 7. Protocolo Obligatorio Kit Aula Lista (Arquitectura Tripartita & Zero-Missing Gate)

Siempre que se solicite crear o actualizar los contenidos de una unidad temática o curso completo:

### A. Estructura de Directorio Único y Organizado
Todos los contenidos de la unidad deben generarse en **un mismo directorio** estructurado con sus subdirectorios:
```text
<directorio_unidad>/
├── 01_encabezado/
│   ├── banner_unidad.png
│   └── 01_etiqueta_encabezado_y_banner.html (Banner + Frase 2 oraciones + 3 preguntas andragógicas)
├── 02_la_clase/
│   ├── video_short.mp4 (Microlearning 1-2 min)
│   ├── diapositivas.pptx (o .pdf)
│   └── 02_pagina_la_clase.html (Dual Video: Short + Videoclase magistral docente 20-30m + Diapositivas)
├── 03_la_lectura/
│   ├── infografia_unidad.png (y .svg)
│   └── 03_pagina_la_lectura.html (Marco teórico, Infografía incrustada, Glosario, FAQs, Bibliografía)
├── 04_la_practica/
│   └── 04_tarea_la_practica.html (Consigna orientadora obligatoria + Caso situado con rúbrica)
└── scorm/
    ├── conectabloques_unidad-SCORM.zip (8 pares conceptuales, temporizador, audio)
    └── trivia_unidad-SCORM.zip (sin numeración rígida en enunciados para aleatorización anti-trampa)
```

### B. Checklist Obligatorio de Autoverificación (Zero-Missing Gate)
Antes de responder al usuario, el agente DEBE autoauditar la existencia de los 10 elementos canónicos:
1. `banner_unidad.png`: Banner visual de cabecera creado y referenciado en la etiqueta.
2. `01_etiqueta_...`: Contiene el banner, la síntesis pedagógica de 2 oraciones y las 3 preguntas andragógicas (Circular 5).
3. `video_short.mp4`: Video short de microlearning creado (con HyperFrames, NotebookLM o recursos locales).
4. `02_pagina_...`: Integra Dual Video (Short + Clase magistral docente de 20-30 min con `target="_blank"`).
5. `diapositivas.*`: Archivo de placas de la clase presente y enlazado.
6. `03_pagina_...`: Módulo teórico estructurado con Glosario de términos clave y bloque FAQ.
7. `infografia_unidad.png`: Infografía conceptual de síntesis creada e incrustada en la lectura.
8. `04_tarea_...`: Incluye la consigna obligatoria (*«Esta práctica se resuelve con lo visto en los videos docentes...»*) y el caso de gestión con rúbrica.
9. `conectabloques-SCORM.zip` y `trivia-SCORM.zip`: Paquetes SCORM 1.2 interactivos compilados (preguntas de trivia sin numeración fija como «Pregunta 1» para permitir aleatorización anti-trampa).
10. `tiza comprobar *.html`: Auditoría ejecutada con éxito (`Paso COMPROBAR: ok`) en todos los ficheros HTML.

### C. Regla de Autocorrección (Self-Healing)
Si durante la autoauditoría se detecta que **falta cualquiera de estos 10 componentes**, el agente **NO debe pedir confirmación ni dejarlo pendiente en su respuesta**: debe proceder inmediatamente a generarlo o compilarlo hasta satisfacer el 100% del checklist.

