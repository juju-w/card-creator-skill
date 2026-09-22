# card-creator-skill

[简体中文](README.md) | [English](README_EN.md)

[![skills.sh](https://skills.sh/b/juju-w/card-creator-skill)](https://skills.sh/juju-w/card-creator-skill)

A one-sentence Skill for AirCard, bank-card and transit-card artwork. Image generation creates the whole
composition, including style-matched logos. Reference pictures guide their appearance; foil, monochrome
and line-art interpretations are welcome. No Python dependency or online editor.

## Start here: ten card styles and one-line prompts

These one-line prompts assume the **Skill is already loaded**. For a ChatGPT / Gemini web conversation
without an installed Skill, see [web usage](#web-usage-links-and-reference-pictures) below. Attach references when applicable.

| Minimal character card · Magikarp × ICOCA | Purple tech · Gengar × Octopus |
|---|---|
| <img src="examples/gemini-magikarp-icoca.jpeg" width="420" alt="Minimal Magikarp and ICOCA card"> | <img src="examples/gemini-gengar-octopus.jpeg" width="420" alt="Purple Gengar and Octopus card"> |
| `Using the card-creator Skill, create a simple Magikarp × ICOCA card with ICOCA at lower right.` | `Using the card-creator Skill, create a Gengar × Octopus card and recolor the Octopus logo purple to match the artwork.` |

| Hua Shan ink wash · China T-Union | Guangzhou minimal line art · Lingnan Tong × China T-Union |
|---|---|
| <img src="examples/huashan-ink-tunion.png" width="420" alt="Hua Shan ink-wash card with China T-Union"> | <img src="examples/guangzhou-minimal-lingnantong-tunion.png" width="420" alt="Guangzhou minimal line-art card with Lingnan Tong and China T-Union"> |
| `Using the card-creator Skill, create a Hua Shan ink-wash transit card with China T-Union at lower right.` | `Using the card-creator Skill, create a minimalist Guangzhou line-art card with Lingnan Tong and China T-Union.` |

| High art · Vienna Secession × Diners Club | Post-impressionist · swirling night × Visa |
|---|---|
| <img src="examples/vienna-secession-diners.png" width="420" alt="Vienna Secession black-and-gold portrait with Diners Club"> | <img src="examples/post-impressionist-visa.png" width="420" alt="Post-impressionist swirling-night card with matte-gold Visa"> |
| `Using the card-creator Skill, create a black-and-gold Vienna Secession card with matte-gold Diners Club at lower right.` | `Using the card-creator Skill, create a post-impressionist card with a deep-blue swirling night and matte-gold Visa at lower right.` |

| Fresh watercolor · Chiikawa × Suica | Ultra-minimal line art · Mastercard |
|---|---|
| <img src="examples/chiikawa-suica.png" width="420" alt="Fresh watercolor Chiikawa and Suica card"> | <img src="examples/minimal-mastercard.png" width="420" alt="Ultra-minimal line-art Mastercard card"> |
| `Using the card-creator Skill, create a fresh watercolor Chiikawa × Suica card with Suica at lower right.` | `Using the card-creator Skill, create a warm-ivory minimal line-art card with Mastercard at lower right.` |

| Palace collection · mica clouds and cranes | Shanghai Art Deco · night skyline × UnionPay |
|---|---|
| <img src="examples/palace-museum-cranes-unionpay.png" width="420" alt="Palace collection card with mica clouds and cranes"> | <img src="examples/shanghai-art-deco-unionpay.png" width="420" alt="Shanghai Art Deco night card with matte-gold UnionPay"> |
| `Using the card-creator Skill, create a Palace collection card with mica clouds, cranes, architecture, and style-matched antique-gold marks.` | `Using the card-creator Skill, create a deep-jade and antique-gold Shanghai Art Deco card with compact UnionPay at lower right.` |

The Magikarp and Gengar images are user-supplied Gemini outputs published with permission. Their generated
ICOCA, JR-West, and purple Octopus marks are non-official stylized interpretations. The Hua Shan, Guangzhou,
and Palace examples likewise use AI-generated marks guided by visual references. All
examples are personal, non-commercial demonstrations and do not imply authorization or endorsement. The
gallery images retain their original dimensions and aspect ratios.

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
