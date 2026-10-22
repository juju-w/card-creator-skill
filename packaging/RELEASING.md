# Versioning and releases

The only maintained version is `metadata.version` in `skills/card-creator/SKILL.md`.
Use a quoted stable `MAJOR.MINOR.PATCH`. The Chinese package inherits it at build time;
do not put another version in `entry.md`. Keep release history here in the repository,
not inside the installed Skill.

- **PATCH**: compatible corrections to instructions, reference links or packaging.
- **MINOR**: new capabilities or reference-library expansions.
- **MAJOR**: incompatible changes to supported workflows or package layout.
- Gallery-only additions do not require a Skill release. `main` is development/latest;
  `vX.Y.Z` tags and their ZIPs are stable snapshots. Do not move published tags or replace
  an existing version's assets; publish a new version instead.

## Prepare

1. Update the canonical version and add a dated section to root `CHANGELOG.md`.
2. Run the README's validation/tests, plus `python3 packaging/release.py check --tag vX.Y.Z`.
3. Commit only release-ready changes and push the commit. The small Chinese package's
   picture URLs point to that exact commit, which must be available on GitHub.

## Build and publish

```bash
git tag -a vX.Y.Z -m "Card Creator vX.Y.Z"
python3 packaging/release.py build --ref vX.Y.Z /tmp/card-creator-vX.Y.Z
git push origin vX.Y.Z
```

The build reads **committed files only**, not local modifications or untracked drafts.
It checks the snapshot's version, tag, changelog and shared web guide. It produces:

- `card-creator-X.Y.Z-full.zip`: the installable `card-creator/` folder with local pictures.
- `card-creator-X.Y.Z-zh-CN.zip`: Chinese entry and commit-pinned remote picture links.
- `release.json`: version, source commit and package hashes.
- `SHA256SUMS`: checksums for both ZIPs and the manifest.

Both ZIPs keep attribution, disclaimer, license and changelog **beside**, not inside,
the installable folder. Build tools are never shipped in that folder. The web guide's
frozen version is also readable at `https://raw.githubusercontent.com/juju-w/card-creator-skill/vX.Y.Z/web/card-creator.md`.

Create a GitHub Release for the existing tag and attach all four files. To install a
specific version manually, download its ZIP, extract it and copy only `card-creator/`
to the client's Skill directory. Restart/reload the session, then inspect the installed
`SKILL.md` version. Do not assume `skills add` or `skillhub install` pins a version.

## Tencent SkillHub is a separate publication

Extract the released Chinese ZIP to a new directory and publish its `card-creator/`
folder with the existing [CLI workflow](skillhub-zh-CN/README.md). After publication,
install into a fresh directory and check version, source commit and reference links.
A GitHub release does **not** mean Tencent has updated or re-evaluated the package.
