# On-Demand Sticker Research and Alpha Extraction

Use this workflow only when a requested exact mark is absent from the ready sticker pack. Do not keep
an exhaustive backlog of unavailable brands in the manifest.

## Source order

Prefer, in order:

1. an operator, issuer, or network's official transparent download;
2. an official vector, brand guide, production PDF, or press kit;
3. an official flat card-face artwork or high-resolution straight-on card image;
4. a traceable user-supplied image;
5. another high-resolution source whose origin and usage note can be recorded.

Avoid thumbnails, perspective photos, heavily compressed memes, and reconstructed logos when a better
source is available.

## Creating an alpha candidate

AI or image tools may crop a mark, create a foreground mask, and remove a uniform or visually separable
background. Preserve visible pixels, proportions, lettering, and colors. Do not repair missing strokes,
invent hidden geometry, or use generative upscaling while presenting the result as exact.

Inspect the candidate over light, dark, and checkerboard backgrounds at 100% and 400%. Reject exact-mode
candidates whose source is too small, distorted, occluded, or changed by the mask.

## Storage and promotion

- Keep unresolved sources and alpha candidates under ignored `output/research-cache/`, with source URL,
  retrieval date, SHA-256, dimensions, crop rectangle, and extraction method.
- Add a public `reference-only` item only when an actual traceable source or research file is preserved
  in the repository. Record source, source asset, license/usage note, SHA-256, and transparency.
- Promote to `ready` only when the source is traceable, the transparent derivative matches the mark,
  redistribution/use notes support the repository, and validation passes.
- If those requirements cannot be met, keep the candidate local or delete it. Do not add a `blocked`
  placeholder row merely to remember that the search failed.

## Stylized fallback

When the user explicitly requests style matching or reinterpretation, ImageGen may transform a found
reference, a user-provided image, or model prior knowledge into a one-off artistic mark as part of the
card face. Record the source decision—use the URL or file when available, otherwise explicitly write
`model-prior / no external asset`—and retain the final prompt. Label the result as a non-official
stylized interpretation. Never extract that generated mark into the exact `ready` sticker pack or claim
brand-guideline accuracy, authorization, interoperability, or endorsement.
