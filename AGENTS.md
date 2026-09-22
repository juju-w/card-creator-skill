# Repository Instructions

This repository is intentionally limited to the `card-creator` Codex skill.

- Do not add a web application, online editor, database, auth system, or deployment runtime unless the user explicitly reopens platform work.
- Keep card dimensions and coordinate rules in `references/card-rules.md` as the single source of truth.
- Default exact-logo mode must use a traceable source and record its file, source URL, license note, usage note, and status in the manifest. Only `status: ready` assets may be composited as exact logos.
- When the user explicitly requests style matching or reinterpretation, AI may transform or redraw a payment, transit, bank, or city-card logo as part of an artistic card-face composition. Label the result as a non-official stylized interpretation, keep the reference source and final prompt, and never promote the generated mark into the exact `ready` sticker pack or claim brand-guideline accuracy, authorization, interoperability, or endorsement.
- Contactless/payment indicators are opt-in only. Do not add one unless the user explicitly requests it, and distinguish generic decorative NFC motifs from exact licensed acceptance marks.
- Preserve original transparent SVG sources and generated transparent PNG derivatives.
- Test changed scripts with real local assets and validate the skill with `quick_validate.py` before handoff.
