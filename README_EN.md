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

Install the localized package from SkillHub after its listing is approved:

```bash
skillhub install card-creator
```

## Output specification

- Trim: `1011 × 638 px` at 300 DPI, representing `85.60 × 53.98 mm`.
- Full bleed: `1081 × 708 px`, with `35 px` bleed on every edge.
- Safe inset: `59 px` inside the trim edge.
- Exports: `bleed`, `trim`, and `guides` PNG files.

## Use directly in ChatGPT or Gemini

Upload your visual reference to the current conversation, then copy this prompt and replace the
bracketed fields. It includes the essential constraints in case the model cannot open GitHub:

```text
Follow the card-face rules in https://github.com/juju-w/card-creator-skill and use the reference image I uploaded in this conversation (reference image above) to create a [theme] card face.

Create flat, straight-on landscape artwork at a 1.58577:1 aspect ratio, targeting a 1011 × 638 px trim at 300 DPI. Extend the background to every edge and keep all people, architecture, and important details comfortably inside the central safe area. Output artwork only: no hand, physical card mockup, perspective, rounded-corner mask, border, or shadow. Do not add card numbers, QR codes, barcodes, watermarks, or unrequested text.

Reserve clean negative space at [position] for [sticker name]. If I also uploaded its transparent PNG, treat it as an immutable overlay: preserve its proportions, colors, lettering, and transparency; do not redraw or approximate the logo. If no verified sticker file is available, leave the space empty and tell me which asset is missing.

Generate one complete card-face preview and include the final prompt you actually used.
```

### Create a style variation from an existing card

The reference can be a mobile-wallet screenshot. This prompt preserves the design character without
copying the original card literally:

```text
Follow the card-face rules in https://github.com/juju-w/card-creator-skill and use the reference image I uploaded above. The reference may be a mobile-wallet screenshot: analyze only the card artwork and ignore the balance, currency, reader instructions, interface, mockup corners, shadows, and watermark.

Do not copy the card literally. First extract its design grammar—palette relationships, whitespace, composition zones, line weight, motif density, and mood—then create a clearly new [target theme] variation using those relationships. You may echo a brand color in one garment, translate a heritage motif into new line art, or preserve the balance between a large quiet field and one small narrative scene, but do not copy proprietary illustration from the reference.

Create flat landscape artwork at 1.58577:1, targeting a 1011 × 638 px trim at 300 DPI, with all important content in the central safe area. Do not reproduce card numbers, masked digits, names, chips, balances, QR codes, barcodes, issuer text, or unavailable logos.

Reserve clean zones for [requested stickers]. If I uploaded verified transparent sticker files, preserve their proportions, colors, lettering, and transparency as immutable overlays; otherwise leave those zones empty. Output artwork only, with no hand, device, card mockup, perspective, rounded-corner mask, border, or shadow. Generate one complete preview and include the final prompt you used.
```

See [reference-card remix](skills/card-creator/references/reference-remix.md) for the full decision rules.

## Examples

### Chiikawa × Suica

<p align="center">
  <img src="examples/chiikawa-suica.png" width="600" alt="Unofficial Chiikawa and Suica card-face example">
</p>

The Suica mark in the lower-right is a deterministic `ready` sticker overlay. This is an
unofficial, non-commercial fan example and does not imply authorization, sponsorship, or approval.

Copy into ChatGPT or Gemini after uploading a composition reference and, for an exact mark, the
repository's `suica.png`:

```text
Follow the dimensions and safe-area rules in https://github.com/juju-w/card-creator-skill and use my uploaded reference image (reference image above) to create an unofficial, non-commercial Chiikawa × Suica fan card face. Paint a fresh spring meadow in pale mint green beneath a powder-blue sky, with rounded white clouds and a soft watercolor-and-gouache texture. Place Chiikawa alone slightly left of center, smiling and holding a four-leaf clover. Keep the lower-right clean.

Create flat landscape artwork at 1.58577:1, targeting a 1011 × 638 px trim at 300 DPI. Keep the character and important details inside the central safe area. No card mockup, hand, perspective, rounded-corner mask, border, shadow, card number, QR code, barcode, watermark, or unrequested text.

If I uploaded a transparent Suica PNG, place it unchanged in the lower-right safe area and preserve its proportions, colors, lettering, and transparency. Otherwise leave the space empty; do not generate an approximate Suica logo. Generate one complete preview and include the final prompt you used.
```

### Minimal line art × Mastercard

<p align="center">
  <img src="examples/minimal-mastercard.png" width="600" alt="Minimal line-art Mastercard card-face example">
</p>

The red/orange Mastercard symbol in the lower-right is a deterministic `ready` sticker overlay.

Copy into ChatGPT or Gemini after uploading a reference and, for an exact mark, the repository's
`mastercard.png`:

```text
Follow the dimensions and safe-area rules in https://github.com/juju-w/card-creator-skill and use my uploaded reference image (reference image above) to create an ultra-minimal line-art card face for a later Mastercard sticker. Use an opaque warm-ivory background and a few precise charcoal, coral-red, and amber-orange monoline arcs. Keep the composition quiet, modern, and restrained, with clean space in the lower-right.

Create flat landscape artwork at 1.58577:1, targeting a 1011 × 638 px trim at 300 DPI. No chip, card number, QR code, barcode, watermark, unrequested text, card mockup, hand, perspective, rounded-corner mask, border, or shadow. Do not use background circles that imitate the Mastercard mark.

If I uploaded a transparent Mastercard PNG, place it unchanged in the lower-right safe area and preserve its red/orange colors, proportions, and transparency. Otherwise leave the space empty. Generate one complete preview and include the final prompt you used.
```

### Beijing ink-wash background — stickers pending

<p align="center">
  <img src="examples/beijing-ink-transit-background.png" width="600" alt="Beijing ink-wash background awaiting verified stickers">
</p>

This is intentionally a background-only example. It reserves two areas for China T-Union and
Beijing Yikatong marks, but both manifest entries remain `pending`. The Skill reports the missing
assets instead of generating or approximating either logo.

Copy into ChatGPT or Gemini after uploading a reference and any verified transparent marks you own:

```text
Follow the dimensions and safe-area rules in https://github.com/juju-w/card-creator-skill and use my uploaded reference image (reference image above) to create a contemporary Beijing ink-wash transit-card face. Fill the canvas with warm ivory rice paper, paint a complete Temple of Heaven on the left, and place a misty Great Wall across the distant mountains. Keep the composition spacious and editorial, with two clean sticker areas stacked on the right.

Create flat landscape artwork at 1.58577:1, targeting a 1011 × 638 px trim at 300 DPI. Keep the complete architecture inside the central safe area. No card mockup, hand, perspective, rounded-corner mask, border, shadow, card number, QR code, barcode, watermark, Chinese characters, or unrequested text.

If I uploaded transparent China T-Union and Beijing Yikatong stickers, place them unchanged in the two right-side safe areas and preserve their proportions, colors, lettering, and transparency. If either file is missing, generate the background only and keep its position empty; do not approximate either logo. Generate one complete preview and include the final prompt you used.
```

The complete background prompts are documented in the [Chinese README](README.md).

## Sticker policy

Only manifest entries with `status: ready` may be composited. Every ready asset records its file,
source URL, license note, and usage note. Research assets and observed URLs remain unavailable to
the compositor until their exact source and usage status are resolved.

The pack includes a ready Apache-2.0 Google Material contactless icon as a generic decorative NFC
cue. It is not the EMV Contactless Indicator. The exact four-semicircle card mark is recorded as
`emv-contactless-indicator`, but remains `pending` because EMVCo requires a written trademark
license and supplies the official artwork after the agreement is executed. The generic icon must
not be substituted when the user specifically requests the EMV mark.

Bank issuers are tracked separately from payment networks. The initial issuer reference set covers
major mainland Chinese banks—ICBC, ABC, Bank of China, CCB, Bank of Communications, PSBC, China
Merchants Bank, CITIC, Everbright, Minsheng, Industrial Bank, SPD Bank, Ping An, and Guangfa—and
commonly requested Hong Kong or international issuers including BOCHK, HSBC, Standard Chartered,
Hang Seng, BEA, Dah Sing, CMB Wing Lung, DBS, OCBC, UOB, and Citi. See the
[bank issuer reference catalog](skills/card-creator/references/bank-issuer-catalog.md). All issuer
entries are currently `pending`: the Skill may reserve space for an exact lockup, but may not draw,
approximate, or substitute it.

When no official transparent asset can be found, an official card face or a traceable user-supplied
card image may be used as a last-resort research source. AI may produce a mask and remove the
background, but it may not redraw, recolor, or reconstruct the mark. Candidates with unresolved
usage terms stay in the local `output/research-cache/` and are not uploaded to a public image host or
used by the compositor. See [sticker research](skills/card-creator/references/sticker-research.md).

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
