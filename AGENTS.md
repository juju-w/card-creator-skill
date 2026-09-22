# Repository Instructions

This repository is intentionally limited to the `card-creator` Codex skill.

- Do not add a web application, online editor, database, auth system, or deployment runtime unless the user explicitly reopens platform work.
- Keep card dimensions and coordinate rules in `references/card-rules.md` as the single source of truth.
- Image generation is the default and only card-art creation path. Do not draw card artwork with SVG, HTML, Canvas, or deterministic logo compositing.
- PNG logo files are visual references for ImageGen, not stickers to paste onto the finished card. Open only references relevant to the requested card.
- AI may transform or redraw a payment, transit, bank, or city-card logo as part of an artistic card-face composition. Label the result as a non-official stylized interpretation and never claim brand-guideline accuracy, authorization, interoperability, or endorsement.
- Contactless/payment indicators are opt-in only. Do not add one unless the user explicitly requests it, and distinguish generic decorative NFC motifs from exact licensed acceptance marks.
- Test changed scripts with real local artwork and validate the skill with `quick_validate.py` before handoff.
