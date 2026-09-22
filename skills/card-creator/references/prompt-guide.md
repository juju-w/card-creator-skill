# Prompt Guide

Keep user-facing prompts short. The Skill supplies dimensions, export rules, and ordinary exclusions.

## One-pass ImageGen workflow

Use one sentence containing the subject, style, and mark placement:

```text
Use the card-creator Skill to create a simple Magikarp × ICOCA card with ICOCA at lower right.
```

This prompt must lead directly to one ImageGen call. Do not research the logo, inspect SVG, construct the
artwork in code, or split the job into “background generation + logo compositing.” Internally add only the
minimum production direction: flat landscape card artwork, no mockup or functional card data, and no
contactless symbol unless requested.

When a matching repository PNG or user attachment is available, always provide it to ImageGen as a visual
reference while still generating the complete card in one pass. Do not redraw a referenced mark from memory.
Generated marks are non-official stylized
interpretations.
