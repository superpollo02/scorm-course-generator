---
name: edtech-moodle-video
description: Author, animate, and render high-fidelity EdTech and Moodle LMS video compositions using HyperFrames. Covers step-by-step tutorials, course showcases, tripartite structures, SCORM gamification demos, and responsive 16:9 / 9:16 video generation.
---

# EdTech & Moodle Video Production with HyperFrames

Use this skill when asked to create, structure, or render educational technology videos, Moodle tutorials, SCORM demonstrations, or online course promos.

## Key Invariants
1. **Pacing & Navigation**:
   - Provide a persistent Step Progress Bar in tutorials (`.step-bar` with active and completed states).
   - Use an animated virtual cursor (`#virtual-cursor`) with expanding click tap rings to direct viewer focus.
2. **Layout & Occlusion Directives**:
   - For simulated drag-and-drop or stamp overlays, always add `data-layout-allow-overlap="true"` and `data-layout-allow-occlusion="true"` to prevent headless layout check rejections.
3. **Sound Mixing**:
   - Background music bed must be ducked or set to low volume (`data-volume="0.15"` to `"0.25"`) to preserve headroom for voiceover.
   - Synchronize tactile audio effects: clicks on buttons, swoosh on scene transitions, chime on correct answers/feedback, and notification on gradebook sync.
4. **Zero-Missing Verification & Render Gate**:
   - Every composition must pass headless verification (`npx hyperframes check <template.html>`).
   - The final microlearning video (`video_short.mp4` / `video_short_hyperframes.mp4`) must be rendered physically to disk (`02_la_clase/`).
   - If missing or unrendered, trigger `npx hyperframes render` immediately (Self-Healing) before reporting completion.
