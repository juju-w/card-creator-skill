# Sticker Catalog

Use `../assets/stickers/manifest.json` as the authority for exact compositing. The manifest contains
only repository-backed assets:

- `ready` — exact transparent source and derivative are present and may be composited;
- `reference-only` — a traceable research/source file is present but may not be composited.

Missing brands are researched only when a user actually requests them. Do not add empty `blocked`
placeholder rows to the manifest.

## Ready payment schemes and networks

- `visa` — Visa
- `mastercard` — Mastercard red/orange symbol
- `american-express` — American Express
- `unionpay-compact` — compact UnionPay card-corner mark; conventional default
- `unionpay` — full UnionPay wordmark; use when explicitly requested
- `jcb` — JCB
- `discover` — Discover
- `diners-club-symbol` — compact Diners Club symbol; conventional default
- `diners-club` — full Diners Club International wordmark
- `rupay` — RuPay
- `mir` — MIR; retain the manifest attribution and ShareAlike notice

## Ready Japanese transit IC marks

- `suica`, `pasmo`, `icoca`, `toica`, `manaca`
- `sugoca`, `nimoca`, `hayakaken`, `pitapa`

These marks are decorative assets only. Do not claim that a custom card is issued, accepted, or
interoperable with an operator.

## Preserved reference files

The manifest keeps source-backed `reference-only` records for Beijing, Hangzhou, Xi'an, Guangzhou,
Lingnan Pass, Shenzhen, Tianjin, Chengdu, and Chongqing research images, plus the opaque-background
Kitaca source and the generic Material contactless icon. They are evidence, not compositable stickers.

## Missing mark behavior

When a requested payment, transit, bank, wallet, or city-card mark is absent:

1. Read [sticker research](sticker-research.md) for exact-mode discovery or alpha extraction.
2. If an exact reusable asset cannot be established, do not create a manifest placeholder. Exact mode
   leaves the zone empty and reports the missing asset.
3. If the user explicitly requests style matching or reinterpretation, ImageGen may search for a
   visual reference or use model prior knowledge to create a one-off non-official artistic mark inside
   the card composition. Record the reference decision and final prompt; never promote it to `ready`.

Keep bank issuers, payment schemes, wallets, transit products, and acceptance indicators conceptually
separate even when a parody collage intentionally combines them.

## Contactless marks

Contactless/NFC indicators are opt-in only. `generic-contactless-material` is `reference-only` and is
not the standard card-side indicator. An exact licensed acceptance mark must come from a traceable,
permitted source; do not substitute the generic icon. Missing licensed marks are handled on demand and
are not represented by empty manifest rows.
