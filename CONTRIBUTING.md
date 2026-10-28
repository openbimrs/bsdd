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
version exists on crates.io may the matching `bsdd` alias be released.
`./scripts/gate.sh` checks the alias against the candidate canonical package;
`cargo publish` (canonical first) does the registry check. Publishing is always
an explicit maintainer action; the CI workflow does not publish.

## Commits

Use focused commits with imperative Conventional Commit subjects where
practical. Never weaken the alias-purity gate to place implementation in the
alias package.

## Licensing contributions

OpenBIM.rs is dual-licensed: `AGPL-3.0-or-later OR LicenseRef-Commercial`
(see [`LICENSING.md`](LICENSING.md)). To keep the commercial option
possible, every contribution is accepted on the following terms, which you
agree to by submitting it (a pull request, patch, issue attachment or any
other material intended for inclusion):

1. **Licence to the project.** Your contribution is licensed under
   `AGPL-3.0-or-later`.
2. **Licence to the copyright holder.** You also grant the copyright holder
   named in [`NOTICE`](NOTICE) a perpetual, worldwide, non-exclusive,
   royalty-free, irrevocable licence to use, reproduce, modify, distribute,
   sublicense and relicense your contribution, including under proprietary
   or commercial terms, as part of OpenBIM.rs or works derived from it.
3. **You keep your copyright.** These terms grant a licence; they do not
   transfer ownership.
4. **You have the right to grant this.** The contribution is your own work,
   or you have permission to submit it on these terms (for example from
   your employer). Identify third-party material, keep its licence,
   attribution and provenance, and do not submit third-party material whose
   licence does not allow these terms.
5. **Patents.** You grant the same parties a licence under any patent claims
   you can license that your contribution necessarily infringes, on the terms
   of section 11 of the AGPL.

If you cannot agree to these terms, say so in the issue or pull request
before submitting; the contribution can then not be merged.
