# Gallery maintenance

GitHub Pages publishes this repository's `main` branch from its root. The site is plain HTML/CSS/JavaScript with no build step or backend. `examples/` contains the same downloadable original files shown by GitHub; do not duplicate or recompress them for the site.

To add a work:

1. Put its original image in `examples/` with a descriptive filename.
2. Add one entry to `gallery-data.js`: unique `id`, title, subtitle, series, image filename, concise reproducible prompt, and provenance note when user-supplied.
3. Record its source and rights context in `SOURCES.md` and check the image before publishing. Keep generated, style-matched logos labelled as non-official.
4. Run a local static server (`python3 -m http.server 8765`), inspect desktop and mobile layouts, then push to `main`. Pages updates from the branch automatically.

The existing `meme` filter is intentionally empty until a genuinely good example is reviewed. Do not add placeholder art or imply that unofficial character/brand fan art is authorized. Rights concerns can be raised through the linked GitHub issue form; see `DISCLAIMER.md`.
