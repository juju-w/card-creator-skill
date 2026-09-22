# Prompt Guide

Keep user-facing prompts short. The Skill supplies dimensions, export rules, and ordinary exclusions.

## Default fast mode

Use one sentence containing the subject, style, and mark placement:

```text
Use the card-creator Skill to create a simple Magikarp × ICOCA card with ICOCA at lower right.
```

Internally add only the minimum production direction needed by ImageGen: flat landscape card artwork,
no mockup or functional card data, and no contactless symbol unless requested. Generate requested marks
inside the artwork and disclose them as non-official stylized interpretations.

## Exact-overlay mode

When the user explicitly requests an exact local sticker, generate the background with a clean placement
zone and no logo, then add the `ready` asset with `prepare_card.py`. Do not search for missing assets unless
the user explicitly asks for research.
