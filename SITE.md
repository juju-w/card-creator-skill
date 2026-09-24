# Gallery maintenance

GitHub Pages publishes this repository's `main` branch from its root. The site is plain HTML/CSS/JavaScript with no build step or backend. `examples/` contains the same downloadable original files shown by GitHub; do not duplicate or recompress them for the site.

To add a work:

1. Put its original image in `examples/` with a descriptive filename.
2. Add one entry to `gallery-data.js`: unique `id`, title, subtitle, one primary `series` key, image filename, `publishedAt`, a standalone `brief` without URLs/tool invocation, original `prompt`, and provenance when user-supplied. Do not rewrite historical user prompts when curating a reusable brief. Categories are mutually exclusive: ukiyo-e belongs under art; `city` is for a named city as the main subject.
3. Record its source and rights context in `SOURCES.md`, and preserve the full generation prompt outside the installed Skill (see `examples/PROMPTS.md`). Check the image before publishing. Keep generated, style-matched logos labelled as non-official.
4. Run a local static server (`python3 -m http.server 8765`), inspect desktop and mobile layouts, then push to `main`. Pages updates from the branch automatically.

The `meme` filter is for selected, reviewed examples only. Do not add placeholder art or imply that unofficial character/brand fan art is authorized. Rights concerns can be raised through the linked GitHub issue form; see `DISCLAIMER.md`.

## Interaction and ordering

`gallery-prompts.js` adds the Web guide URL or installed-Skill invocation around the same brief. Web is the default; a local-storage preference remembers the user's choice without an account. Reference creation downloads the original and supplies an edit prompt; the user must attach the image themselves. Original prompts remain folded separately.

Newest ordering uses the later Git timestamp of the work's first gallery inclusion and its displayed image's most recent update; ties retain curated order. Updating copy alone must not make old artwork look newly published.

## Maintainer checks

Use a Python environment with `pip install -r requirements-dev.txt`; Pillow is only for inspecting image pixels, not rendering or editing cards. Run `python -m unittest discover -s tests -v`, `node --test tests/gallery-prompts.test.mjs`, and the Web/Skill checks from the README. Installed Skill users need none of these dependencies.

For browser QA, exercise both prompt channels, reload persistence, blocked storage/clipboard, current-image reference download, and rapid close/reopen while an image is loading. Check desktop and mobile. Keep screenshots, browser scripts and generated QA drafts outside the repository.
