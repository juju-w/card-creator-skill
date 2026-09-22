# Sticker Research and Card-Face Extraction

Use this workflow only when a requested mark is missing from the ready sticker pack. It produces a
review candidate, not an automatically approved sticker.

## Source order

Prefer sources in this order:

1. an operator or network's official transparent download;
2. an official vector, brand guide, production PDF, or press kit;
3. an official flat card-face artwork or high-resolution straight-on card image;
4. a user-supplied card image whose origin the user can identify.

Do not extract from search thumbnails, marketplace listings, social-media reposts, perspective
photos, compressed memes, or another person's reconstructed logo when a traceable primary source is
available.

## Pixel-extraction boundary

AI may create a foreground mask or remove a uniform background from a card-face source. It must not
invent missing strokes, redraw letters, correct geometry, recolor the mark, vector-trace an uncertain
edge, upscale by hallucinating detail, or replace the extracted pixels with a generated imitation.

Compare the candidate over light, dark, and checkerboard backgrounds at 100% and 400%. Reject it when
the source is too small, perspective-distorted, partly occluded, or the mask changes visible logo
pixels. Record the crop rectangle and extraction method so another maintainer can reproduce the
result.

## Storage and provenance

- If redistribution or mark usage is not verified, keep the source and extracted candidate under
  `output/research-cache/`; this path is local and ignored by Git. Record the public source URL,
  retrieval date, source SHA-256, dimensions, crop rectangle, and extraction method in working notes.
- Add a file under `assets/stickers/research/` only when keeping that exact source or derivative in the
  public repository is supportable. Add a manifest entry with `status: pending`, `research_file`,
  `source`, `source_asset`, `license`, `usage`, `sha256`, `transparency`, and an explicit blocker.
- Do not use a public image host as a substitute for provenance or permission. If the user explicitly
  requires their own object storage, retain an immutable source URL and SHA-256 in the manifest, but
  prefer repository-local approved assets for deterministic builds.

Only promote a candidate to `ready` after its source is traceable, its pixels match the identified
mark, its transparent derivative has passed validation, and the usage note supports the intended
distribution. Until then, reserve space in the background and report that the sticker is pending.
