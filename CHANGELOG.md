# Changelog

Versions apply to the shared Card Creator Skill, its web guide and both distribution packages. Gallery-only additions do not require a Skill version bump. Historical Git commits remain available; no older GitHub releases are implied.

## [0.5.0] — 2026-10-22

- Establish a single version in the canonical Skill's `metadata.version`; generate the SkillHub version from it.
- Add release validation, committed-snapshot ZIP packages and SHA-256 checksums. Local drafts and uncommitted changes are excluded.
- Publish the current image-generation-only workflow, shared web guide and logo reference library as the first tagged GitHub release.
- Provide a full package with local reference pictures and a smaller Chinese package with commit-pinned remote pictures. Neither installed Skill contains scripts.

## Legacy packaging

The Chinese distribution template previously declared `0.4.0` independently. The main Skill had no declared version, Git tag or GitHub release. This section records that legacy value, not a reconstructed release history or confirmation of the version currently served by SkillHub.
