# card-creator-skill

[简体中文](README.md) | [English](README_EN.md)

[![skills.sh](https://skills.sh/b/juju-w/card-creator-skill)](https://skills.sh/juju-w/card-creator-skill)

An Agent Skill for creating print-ready AirCard, NFC-card, and transit-card face artwork. It keeps
three concerns separate:

- exact card dimensions, bleed, and safe-area rules;
- traceable transparent payment and transit sticker assets;
- deterministic scripts that crop AI-generated backgrounds and composite approved stickers.

The repository does not contain an online editor. Image models generate background artwork only;
they never redraw protected brand marks.

## Install from GitHub / skills.sh

Use Vercel's open-source `skills` CLI:

```bash
npx skills add juju-w/card-creator-skill
```

Or copy `skills/card-creator` into the Skill directory used by your Agent. Install the script
dependencies when you want deterministic exports:

```bash
python3 -m pip install -r skills/card-creator/scripts/requirements.txt
```

Ordinary cropping and PNG sticker compositing require Pillow only. Maintainers who regenerate PNG
derivatives from SVG sources should install `requirements-render.txt` and the native Cairo library.

Example request:

```text
Use $card-creator to create a quiet Guangzhou morning card face,
reserve the upper-right for the China T-Union sticker, and export print-ready PNGs.
```

The SkillHub/WorkBuddy distribution has a maintained Simplified Chinese entry point and localized
references. Its reproducible source and build instructions live in
[`packaging/skillhub-zh-CN`](packaging/skillhub-zh-CN/README.md). Both distributions copy the same
scripts, card rules, manifest, and sticker files from the canonical Skill directory.

## Output specification

- Trim: `1011 × 638 px` at 300 DPI, representing `85.60 × 53.98 mm`.
- Full bleed: `1081 × 708 px`, with `35 px` bleed on every edge.
- Safe inset: `59 px` inside the trim edge.
- Exports: `bleed`, `trim`, and `guides` PNG files.

## Examples

### Chiikawa × Suica

<p align="center">
  <img src="examples/chiikawa-suica.png" width="600" alt="Unofficial Chiikawa and Suica card-face example">
</p>

The Suica mark in the lower-right is a deterministic `ready` sticker overlay. This is an
unofficial, non-commercial fan example and does not imply authorization, sponsorship, or approval.

### Minimal line art × Mastercard

<p align="center">
  <img src="examples/minimal-mastercard.png" width="600" alt="Minimal line-art Mastercard card-face example">
</p>

The red/orange Mastercard symbol in the lower-right is a deterministic `ready` sticker overlay.

### Beijing ink-wash background — stickers pending

<p align="center">
  <img src="examples/beijing-ink-transit-background.png" width="600" alt="Beijing ink-wash background awaiting verified stickers">
</p>

This is intentionally a background-only example. It reserves two areas for China T-Union and
Beijing Yikatong marks, but both manifest entries remain `pending`. The Skill reports the missing
assets instead of generating or approximating either logo.

The complete background prompts are documented in the [Chinese README](README.md).

## Sticker policy

Only manifest entries with `status: ready` may be composited. Every ready asset records its file,
source URL, license note, and usage note. Research assets and observed URLs remain unavailable to
the compositor until their exact source and usage status are resolved.

Brand and character rights remain with their respective owners. The repository's MIT license
covers original code and documentation only; it does not relicense third-party marks or artwork.

## Validate

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/card-creator

python3 skills/card-creator/scripts/render_stickers.py
python3 skills/card-creator/scripts/validate_stickers.py
```

`render_stickers.py` is a maintainer command and uses the optional render requirements; ordinary
card creation does not.

Start with [SKILL.md](skills/card-creator/SKILL.md).
