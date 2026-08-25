# Contributing

Contributions are welcome, but this repository currently reserves package names
rather than claiming a working buildingSMART Data Dictionary integration.

## Before opening a pull request

1. Read `AGENTS.md` and the affected directory's nested instructions.
2. Put all future implementation in `openbim-bsdd`; keep `bsdd` a pure re-export.
3. Add executable tests before changing any capability from "Not implemented".
4. Keep README, rustdoc, architecture notes, and `CHANGELOG.md` synchronized.
5. Link to buildingSMART's current official documentation rather than vendoring
   API or data snapshots.
6. Do not commit standards documents, API snapshots, credentials, tokens, or
   dictionary exports.
7. Run the complete gate:

   ```bash
   ./scripts/gate.sh
   ```

## Release order

Release the canonical `openbim-bsdd` package first. Only after that exact
version exists on crates.io may the matching `bsdd` alias be packaged with
registry dependency verification and released. Publishing is always an
explicit maintainer action; the CI workflow does not publish.

## Commits

Use focused commits with imperative Conventional Commit subjects where
practical. Never weaken the alias-purity gate to place implementation in the
alias package.
