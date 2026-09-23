# card-creator-skill

[简体中文](README.md) | [English](README_EN.md)

[![skills.sh](https://skills.sh/b/juju-w/card-creator-skill)](https://skills.sh/juju-w/card-creator-skill)

A one-sentence Skill for AirCard, bank-card and transit-card artwork. Image generation creates the whole
composition, including style-matched logos. Reference pictures guide their appearance; foil, monochrome
and line-art interpretations are welcome. No Python dependency or online editor.

## Explore the gallery

[Browse and download the card gallery](https://juju-w.github.io/card-creator-skill/) by art style, Pokémon, city, anime, and more. Each work has one primary category. The gallery contains each original image, a short prompt, and provenance notes; new examples are primarily maintained there. The meme category will fill as curated work becomes available.

| Impressionist water lilies × Visa | Gilded decorative art × Mastercard |
|---|---|
| [<img src="examples/monet-water-lilies-visa.png" width="420" alt="Blue-violet water-lily card">](https://juju-w.github.io/card-creator-skill/) | [<img src="examples/klimt-gold-mastercard.png" width="420" alt="Gold-leaf decorative card">](https://juju-w.github.io/card-creator-skill/) |

| Gardevoir × CMB / UnionPay | Morandi still life × Wise |
|---|---|
| [<img src="examples/chatgpt-gardevoir-cmb-unionpay.png" width="420" alt="Pink Gardevoir card">](https://juju-w.github.io/card-creator-skill/) | [<img src="examples/morandi-still-life-wise.png" width="420" alt="Morandi still-life card with WISE lettering">](https://juju-w.github.io/card-creator-skill/) |

The Gardevoir and Metagross cards were shared by the user from ChatGPT on the web; **Skill loading was not verified**. Their original prompts and provenance remain in the gallery and [SOURCES.md](SOURCES.md). The Wise lettering is an unofficial stylized interpretation; the [unmarked Morandi version](examples/morandi-still-life.png) is also available. See [DISCLAIMER.md](DISCLAIMER.md) for rights notes.

## How to use

### Installed Skill: Codex or a compatible app

The client needs both **Skill loading** and **image generation**. This repository supplies instructions and
reference pictures, not an image model. A local app or a successful installation alone does not ensure
that the current session can generate images. Do not substitute code-drawn artwork when it cannot.

Install with Vercel's open-source `skills` CLI and select your compatible client:

```bash
npx skills add juju-w/card-creator-skill
```

Or download this repository and run the following from its root to install into Codex manually:

```bash
cp -R skills/card-creator ~/.codex/skills/
```

The localized SkillHub / WorkBuddy package is maintained under
[`packaging/skillhub-zh-CN`](packaging/skillhub-zh-CN/README.md). After approval, install it with:

```bash
skillhub install card-creator
```

Once the client recognizes `card-creator`, use a short prompt:

```text
Using the card-creator Skill, create a Pokémon Gardevoir card face with China Merchants Bank and UnionPay branding: minimalist, Psychic-type pink, no chip.
```

### Web usage: links and reference pictures

**Pasting a GitHub link does not install a Skill or guarantee that its instructions and PNGs were read.**
Without installation through a platform's Skill interface, treat the repository as reference material.
Link and image access depend on the capabilities of the current conversation.

Select the image-generation tool in the interface, then send the sentence below. If your interface shows
`@创建图像` or “Create image,” select that tool; this is not a universal text command to copy into every app.
See the [official ChatGPT image instructions](https://help.openai.com/en/articles/11084440).

```text
Refer to the card-creator instructions at https://github.com/juju-w/card-creator-skill and use image generation to create a Pokémon Gardevoir card face with China Merchants Bank and UnionPay branding: minimalist, Psychic-type pink, no chip.
```

If the repository cannot be read, paste [SKILL.md](skills/card-creator/SKILL.md) and the short
[card rules](skills/card-creator/references/card-rules.md), then attach the relevant logo or character images.
There is no need to scan the repository. For this example, attach
[China Merchants Bank](skills/card-creator/assets/logo-references/banks/china/cmb.png) and
[compact UnionPay](skills/card-creator/assets/logo-references/payment/unionpay-compact.png), and add “Use the attached references.”

If your platform or workspace provides Skill installation, install it and use the previous section instead;
Skill loading is not inherently limited to local apps. For ChatGPT, consult the
[official Skill guide](https://openai.com/academy/skills/) and the controls available to your account.

Both methods use image generation for the entire card. PNGs are visual references, not layers for scripts
to draw or paste onto the finished artwork.

## Images and references

Default to landscape card proportions and return the image generator's original output. There is no
automatic cropping or print-export pipeline. See the short [card rules](skills/card-creator/references/card-rules.md).

- Transit references are grouped by mainland China, Hong Kong, Japan, USA, UK, Germany and Australia.
  Suica is in the Japan directory alongside ICOCA and the other Japanese cards.
- 30 bank references cover China's Big Four and common commercial banks, Hong Kong, the USA, the UK,
  Singapore, Germany and Australia.
- Digital wallets and fintech: Wise, Bybit, Apple Cash and X Money, including brand marks and an official X Card reference. Designs can explore typography, abstraction, cities or materials—not only anime characters.
- The [picture index](skills/card-creator/references/logo-reference-index.md) links to actual files.
  [Sources and attribution](SOURCES.md) stay at the repository root, outside the installed Skill.
- Contactless indicators are opt-in. The repository's MIT License does not relicense third-party logos,
  characters or example artwork.

## Disclaimer

This free, non-commercial project shares references and creative experiments; it does not sell assets or
claim brand authorization. Third-party rights remain with their owners. Non-profit use is not a guarantee
against infringement. Rights holders may request removal or correction; see the [full notice](DISCLAIMER.md).

## Validate

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/card-creator
python3 -m unittest discover -s tests -v
```

Start with [SKILL.md](skills/card-creator/SKILL.md).
