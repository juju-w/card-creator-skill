# Repository Instructions

This repository is intentionally limited to the `card-creator` Codex skill.

- Do not add a web application, online editor, database, auth system, or deployment runtime unless the user explicitly reopens platform work.
- Keep card dimensions and coordinate rules in `references/card-rules.md` as the single source of truth.
- Never generate or hand-redraw payment, transit, or city-card logos. Add a logo only from a traceable source and record its file, source URL, license note, usage note, and status in the manifest.
- Only `status: ready` sticker assets may be composited by the skill.
- Preserve original transparent SVG sources and generated transparent PNG derivatives.
- Test changed scripts with real local assets and validate the skill with `quick_validate.py` before handoff.
