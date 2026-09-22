# card-creator-skill

[简体中文](README.md) | [English](README_EN.md)

[![skills.sh](https://skills.sh/b/juju-w/card-creator-skill)](https://skills.sh/juju-w/card-creator-skill)

A Codex Skill for creating print-ready AirCard, NFC-card, and transit-card faces. AI creates the
artwork; the Skill handles dimensions, trim, layout, transparent stickers, and 300 DPI exports.
This repository does not include an online editor.

## Start here: nine card styles and one-line prompts

Dimensions, bleed, layout, rounded-display behavior, and export rules already live in the Skill.
Paste one sentence into ChatGPT or Gemini; upload a reference in the same message when applicable.

| Minimal character card · Magikarp × ICOCA | Purple tech · Gengar × Octopus |
|---|---|
| <img src="examples/gemini-magikarp-icoca.jpeg" width="420" alt="Minimal Magikarp and ICOCA card"> | <img src="examples/gemini-gengar-octopus.jpeg" width="420" alt="Purple Gengar and Octopus card"> |
| `Using the card-creator Skill, create a simple Magikarp × ICOCA card with ICOCA at lower right.` | `Using the card-creator Skill, create a Gengar × Octopus card and recolor the Octopus logo purple to match the artwork.` |

| High art · Vienna Secession × Diners Club |
|---|
| <img src="examples/vienna-secession-diners.png" width="420" alt="Vienna Secession black-and-gold portrait with Diners Club"> |
| `Using the card-creator Skill, create a black-and-gold Vienna Secession card with matte-gold Diners Club at lower right.` |

| Fresh watercolor · Chiikawa × Suica | Post-impressionist · swirling night × Visa |
|---|---|
| <img src="examples/chiikawa-suica.png" width="420" alt="Fresh watercolor Chiikawa and Suica card"> | <img src="examples/post-impressionist-visa.png" width="420" alt="Post-impressionist swirling-night card with matte-gold Visa"> |
| `Using the card-creator Skill, create a fresh watercolor Chiikawa × Suica card with Suica at lower right.` | `Using the card-creator Skill, create a post-impressionist card with a deep-blue swirling night and matte-gold Visa at lower right.` |

| Beijing ink wash · transit marks | Ultra-minimal line art · Mastercard |
|---|---|
| <img src="examples/beijing-ink-transit-background.png" width="420" alt="Beijing ink-wash transit card"> | <img src="examples/minimal-mastercard.png" width="420" alt="Ultra-minimal line-art Mastercard card"> |
| `Using the card-creator Skill, create a Beijing ink-wash transit card with the Temple of Heaven, Great Wall, Beijing Transit Card, and China T-Union.` | `Using the card-creator Skill, create a warm-ivory minimal line-art card with Mastercard at lower right.` |

| Palace collection · mica clouds and cranes | Shanghai Art Deco · night skyline × UnionPay |
|---|---|
| <img src="examples/palace-museum-cranes-unionpay.png" width="420" alt="Palace collection card with mica clouds and cranes"> | <img src="examples/shanghai-art-deco-unionpay.png" width="420" alt="Shanghai Art Deco night card with matte-gold UnionPay"> |
| `Using the card-creator Skill, create a Palace collection card with mica clouds, cranes, architecture, and style-matched antique-gold marks.` | `Using the card-creator Skill, create a deep-jade and antique-gold Shanghai Art Deco card with compact UnionPay at lower right.` |

The Magikarp and Gengar images are user-supplied Gemini outputs published with permission. Their generated
ICOCA, JR-West, and purple Octopus marks are non-official stylized interpretations and are not added to the
exact `ready` sticker pack. The Beijing and Palace examples also use disclosed non-official stylized marks;
other payment and transit overlays use exact transparent assets whose manifest status is `ready`. All
examples are personal, non-commercial demonstrations and do not imply authorization or endorsement. The
two Gemini images keep their original display ratio; production exports still use the Skill's
`1011 × 638 px` specification.

## Install

Use Vercel's open-source `skills` CLI:

```bash
npx skills add juju-w/card-creator-skill
```

Or install manually:

```bash
cp -R skills/card-creator ~/.codex/skills/
python3 -m pip install -r skills/card-creator/scripts/requirements.txt
```

The localized SkillHub / WorkBuddy package is maintained under
[`packaging/skillhub-zh-CN`](packaging/skillhub-zh-CN/README.md). After approval, install it with:

```bash
skillhub install card-creator
```

## Use

Do not repeat dimensions and layout mechanics in every prompt:

```text
Using the card-creator Skill and the reference image above, create a [theme] card with [stickers] in a [style]. Add no contactless mark or unrelated text.
```

Mobile-wallet screenshots work as references. The Skill isolates the card face, ignores balances,
reader instructions, interface corners, shadows, and watermarks, and transfers design grammar into a
new composition instead of copying the original. See
[reference-card remix](skills/card-creator/references/reference-remix.md).

## Output specification

- Trim: `1011 × 638 px` at 300 DPI, representing `85.60 × 53.98 mm`.
- Full bleed: `1081 × 708 px`, with `35 px` bleed on every edge.
- The `59 px` blue guide is advisory for small functional information; it does not constrain marks,
  illustration, or full-face compositions.
- Exports include `bleed`, `trim`, and `guides` PNG files. Physical or wallet-display corner rounding is
  never baked into source artwork.
- A complete 3 × 3 anchor grid supports deliberate multi-mark collage layouts.

[card-rules.md](skills/card-creator/references/card-rules.md) is the single source of truth for dimensions
and coordinates.

## Assets and boundaries

- Ready overlays include Visa, Mastercard, American Express, UnionPay, JCB, Discover, Diners Club,
  RuPay, MIR, and Japanese transit marks including Suica, PASMO, and ICOCA.
- The manifest keeps only repository-backed `ready` and `reference-only` files; unavailable brands no
  longer create empty `blocked` rows. Missing city, bank, wallet, or payment marks are researched and
  alpha-extracted on demand, or rendered as one-off non-official interpretations when the user explicitly
  selects stylized mode. See the [sticker catalog](skills/card-creator/references/sticker-catalog.md),
  [research workflow](skills/card-creator/references/sticker-research.md), and
  [manifest](skills/card-creator/assets/stickers/manifest.json).
- `unionpay-compact` is the conventional card-corner default; Diners Club similarly uses its compact mark
  unless a full lockup is requested. Marks may dominate a corner or the full face and are not forced inside
  the advisory blue guide.
- Contactless marks are opt-in. The exact EMVCo four-wave indicator requires the applicable permission,
  and the generic Material icon is not a substitute.
- The MIT License covers original code and documentation only; it does not relicense third-party marks,
  characters, music, or example artwork.

## Validate

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/card-creator
python3 skills/card-creator/scripts/validate_stickers.py
python3 -m unittest discover -s tests -v
```

Start with [SKILL.md](skills/card-creator/SKILL.md).
