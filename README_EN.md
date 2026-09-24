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

| Art · swirling night | Art · floral Art Nouveau |
|:---:|:---:|
| [<img src="examples/post-impressionist-visa.png" width="320" alt="Swirling blue night Visa card face">](https://juju-w.github.io/card-creator-skill/) <br> `Post-Impressionist night · muted-gold Visa` | [<img src="examples/mucha-art-nouveau-octopus.png" width="320" alt="Floral Art Nouveau Octopus card face">](https://juju-w.github.io/card-creator-skill/) <br> `Floral portrait · bronze Octopus` |
| Pokémon · Psychic pink | City · Greater Bay bridge |
| [<img src="examples/chatgpt-gardevoir-cmb-unionpay.png" width="320" alt="Gardevoir with CMB and UnionPay">](https://juju-w.github.io/card-creator-skill/) <br> `Gardevoir · CMB × UnionPay` | [<img src="examples/greater-bay-sea-bridge-concept.png" width="320" alt="Conceptual Greater Bay bridge card face">](https://juju-w.github.io/card-creator-skill/) <br> `Sea bridge at dawn · fictional Bay Pass` |
| Parody · Niu Lai | Modern · crystal cat |
| [<img src="examples/niu-lai-amex-parody.png" width="320" alt="Niu Lai on an Amex-inspired parody card">](https://juju-w.github.io/card-creator-skill/) <br> `Classic Amex layout · centered Niu Lai` | [<img src="examples/hsbc-crystal-cat.png" width="320" alt="Blue crystalline cat on an HSBC-inspired card">](https://juju-w.github.io/card-creator-skill/) <br> `Blue crystal facets · cat × HSBC` |

> The Gardevoir example was shared by a user from ChatGPT on the web; whether the Skill was loaded is unknown. The Bay Pass mark is fictional. Character and brand depictions are unofficial fan art. See [SOURCES.md](SOURCES.md).

## Get started in 30 seconds

Install in a client that supports both **Agent Skills** and **image generation**. The Skill does not include an image model.

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

Change the brief to explore something else: `Palace Museum cranes and mica clouds × UnionPay`, `springtime London impasto × Oyster`, or attach a card you like as a composition reference. Card numbers, chips, QR codes, and contactless symbols are omitted unless requested.

### Using a web image-generation interface

Select the interface's **Create image** tool, then try:

```text
Refer to the card-creator Skill at https://github.com/juju-w/card-creator-skill and use image generation to create a Pokémon Gardevoir card face with China Merchants Bank and UnionPay branding: minimalist, Psychic-type pink, no chip.
```

Pasting a repository link **does not install the Skill** or guarantee that its files were read. If the site cannot access the repository, provide [SKILL.md](skills/card-creator/SKILL.md), the short [card rules](skills/card-creator/references/card-rules.md), and any relevant [reference pictures](skills/card-creator/references/logo-reference-index.md). There is no need to scan the entire library. `@创建图像` is a tool picker in some interfaces, not universal prompt syntax.

## How it works

1. Interpret the subject, style, and placement; open only the relevant PNG reference when a mark is requested.
2. Use image generation to paint the **whole card face**, including style-matched marks. No SVG drawing, scripted rendering, or logo compositing.
3. Check readability and balance. Return the generator's original image; do not claim print DPI or bleed files that were not produced.

The reference library covers transit cards in China and abroad, major banks, payment networks, and fintech brands such as Wise and Apple Cash. Browse the [picture index](skills/card-creator/references/logo-reference-index.md) as needed; the [aspect-ratio and layout rules](skills/card-creator/references/card-rules.md) stay deliberately short. Logos may become foil, monochrome, or line art, but the outputs are **unofficial stylized interpretations**, not functioning bank or transit cards.

## About the project

Card Creator is a free, non-commercial project for creative exchange and reference sharing. It sells no card faces or assets and claims no brand endorsement. Third-party marks, characters, and art belong to their respective owners; **non-profit use and attribution do not automatically grant permission**. The repository's MIT License does not cover third-party material. See [DISCLAIMER.md](DISCLAIMER.md) for rights and removal requests, and [SOURCES.md](SOURCES.md) for provenance.

<details>
<summary>Manual installation and maintainer checks</summary>

From the repository root, install manually into Codex:

```bash
cp -R skills/card-creator ~/.codex/skills/
```

The Chinese SkillHub package is documented in [`packaging/skillhub-zh-CN`](packaging/skillhub-zh-CN/README.md). Before contributing, run:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/card-creator
python3 -m unittest discover -s tests -v
```

</details>
