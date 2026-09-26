<p align="center"><img src="brand/icon.png" width="88" alt="Card Creator icon"></p>

<h1 align="center">Card Creator</h1>

<p align="center"><strong>One sentence. A card face worth keeping.</strong><br>An image-generation Skill for AirCard, bank-card, and transit-card artwork.<br>Give it a subject, a style, and the marks you want to see.</p>

<p align="center"><a href="https://juju-w.github.io/card-creator-skill/">Explore the gallery</a> · <a href="#get-started-in-30-seconds">Get started</a> · <a href="README.md">简体中文</a></p>

<p align="center">
  <a href="https://skills.sh/juju-w/card-creator-skill"><img src="https://skills.sh/b/juju-w/card-creator-skill" alt="skills.sh"></a>
  <a href="https://github.com/juju-w/card-creator-skill/stargazers"><img src="https://img.shields.io/github/stars/juju-w/card-creator-skill?style=flat-square&logo=github" alt="GitHub Stars"></a>
  <a href="https://github.com/juju-w/card-creator-skill/forks"><img src="https://img.shields.io/github/forks/juju-w/card-creator-skill?style=flat-square&logo=github" alt="GitHub Forks"></a>
  <a href="https://aiagentslisting.com/mcp/card-creator-skill"><img src="https://aiagentslisting.com/card-creator-skill/badge.svg?claim=1080f8ea087cc1881566e4ed826f8708" alt="Card Creator Skill on AI Agents Listing"></a>
</p>

## See the work first

Each card starts with a short idea. Click an image to [browse the gallery](https://juju-w.github.io/card-creator-skill/), read its prompt, and download the original.
Browse curated picks or newest works. Open a card and choose “Use on the web” or “Use an installed Skill” to copy the appropriate prompt. Historical prompts remain available separately.

| Art · swirling night | Art · floral Art Nouveau |
|:---:|:---:|
| [<img src="examples/post-impressionist-visa.png" width="320" alt="Swirling blue night Visa card face">](https://juju-w.github.io/card-creator-skill/) <br> `Post-Impressionist night · muted-gold Visa` | [<img src="examples/mucha-art-nouveau-octopus.png" width="320" alt="Floral Art Nouveau Octopus card face">](https://juju-w.github.io/card-creator-skill/) <br> `Floral portrait · bronze Octopus` |
| Pokémon · Psychic pink | City · Greater Bay bridge |
| [<img src="examples/chatgpt-gardevoir-cmb-unionpay.png" width="320" alt="Gardevoir with CMB and UnionPay">](https://juju-w.github.io/card-creator-skill/) <br> `Gardevoir · CMB × UnionPay` | [<img src="examples/greater-bay-sea-bridge-concept.png" width="320" alt="Conceptual Greater Bay bridge card face">](https://juju-w.github.io/card-creator-skill/) <br> `Sea bridge at dawn · fictional Bay Pass` |
| Parody · Niu Lai | Modern · crystal cat |
| [<img src="examples/niu-lai-amex-parody.png" width="320" alt="Niu Lai on an Amex-inspired parody card">](https://juju-w.github.io/card-creator-skill/) <br> `Classic Amex layout · centered Niu Lai` | [<img src="examples/hsbc-crystal-cat.png" width="320" alt="Blue crystalline cat on an HSBC-inspired card">](https://juju-w.github.io/card-creator-skill/) <br> `Blue crystal facets · cat × HSBC` |

> The Gardevoir example was shared by a user from ChatGPT on the web; whether the Skill was loaded is unknown. The Bay Pass mark is fictional. Character and brand depictions are unofficial fan art. See [SOURCES.md](SOURCES.md).

## Get started in 30 seconds

### Use a web image interface

Choose **Create image** in a supported chat interface, then paste:

```text
Read and follow https://raw.githubusercontent.com/juju-w/card-creator-skill/main/web/card-creator.md first. Then use image generation to create a Pokémon Gardevoir card face with China Merchants Bank and UnionPay branding: minimalist, Psychic-type pink, no chip.
```

Or choose a work in the [gallery](https://juju-w.github.io/card-creator-skill/) and copy its “Use on the web” prompt. The single-file guide contains the complete workflow; no multi-file browsing is needed.

A link **does not install the Skill** or guarantee it was read. If access fails, download [card-creator.md](https://juju-w.github.io/card-creator-skill/web/card-creator.md) and attach it. `@创建图像` is not universal prompt syntax; select your interface's image tool instead.

### Install the Skill

Install in a client supporting **Agent Skills** and **image generation/editing**. The Skill does not include an image model.

```bash
npx skills add juju-w/card-creator-skill
```

The Simplified Chinese edition is also on Tencent SkillHub:

```bash
skillhub install card-creator --namespace indiv-juju-w
```

Once `card-creator` is recognized in your current session, ask for a card:

```text
Using the card-creator Skill, create a Pokémon Gardevoir card face with China Merchants Bank and UnionPay branding: minimalist, Psychic-type pink, no chip.
```

Try `Palace Museum cranes and mica clouds × UnionPay` or `springtime London impasto transit card`. When unspecified, a suitable mark is selected automatically; say “no logo” for pure artwork. Card numbers, chips, QR codes, and contactless indicators are omitted unless requested.

### Use a reference or change one detail

In the gallery, choose “Create from this reference,” download the image, upload it to your image conversation, and copy the editing prompt. For an image already in the conversation, simply continue:

```text
Only change the Octopus logo to purple; keep the character and background.
```

Attach a reference for a specific character or mark variant. Copying text does not attach the image automatically, and generative edits cannot guarantee pixel-identical preservation elsewhere.

## How it works

1. Interpret the subject and edit scope; choose a suitable mark if unspecified. Open only relevant reference pictures.
2. Generate or edit the **whole card face**, including style-matched marks, with the host's image tool. No SVG drawing or scripted compositing.
3. Check subjects, marks, unwanted transparency and borders. Landscape is the default; simply request a “portrait card” for an upright composition, not a rotated or cropped landscape image. See the [card rules](skills/card-creator/references/card-rules.md) for ratios and preferred dimensions; return actual output without unsupported pixel, DPI or bleed claims.

The reference library covers transit cards in China and abroad, major banks, payment networks, and fintech brands such as Wise and Apple Cash. Browse the [picture index](skills/card-creator/references/logo-reference-index.md) as needed; the [aspect-ratio and layout rules](skills/card-creator/references/card-rules.md) stay deliberately short. Logos may become foil, monochrome, or line art, but the outputs are **unofficial stylized interpretations**, not functioning bank or transit cards.

## About the project

Card Creator is a free, non-commercial project for creative exchange and reference sharing. It sells no card faces or assets and claims no brand endorsement. Third-party marks, characters, and art belong to their respective owners; **non-profit use and attribution do not automatically grant permission**. The repository's MIT License does not cover third-party material. See [DISCLAIMER.md](DISCLAIMER.md) for rights and removal requests, and [SOURCES.md](SOURCES.md) for provenance.

<details>
<summary>Manual installation and maintainer checks</summary>

From the repository root, install manually into Codex:

```bash
cp -R skills/card-creator ~/.codex/skills/
```

The Chinese SkillHub package is documented in [`packaging/skillhub-zh-CN`](packaging/skillhub-zh-CN/README.md). It uses a Chinese introduction, shared execution rules and remote image links; the GitHub package includes local reference images. The web guide is generated from those same rules; do not edit it directly. Before contributing, run:

```bash
python3 -m pip install -r requirements-dev.txt  # Maintainers only: pixel opacity checks
python3 packaging/build_web_md.py --check
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/card-creator
python3 -m unittest discover -s tests -v
node --test tests/gallery-prompts.test.mjs
```

Use a virtual environment for maintainer dependencies. Skill users need neither Python nor Node. Live image-generation scenarios are in [tests/skill-scenarios.md](tests/skill-scenarios.md).

</details>
