# OpenBIM.rs bSDD

Canonical repository: <https://github.com/openbimrs/bsdd>
Integration ecosystem: <https://github.com/openbimrs/openbim>

Read `AGENTS.md` before changing the repository and each nested `AGENTS.md`
before editing a package or documentation. This repository is standalone and
must not rely on a parent workspace.

## Verification

Run `./scripts/gate.sh`. It is the authoritative local and CI gate.

## Conventions

- Rust 2021 with MSRV 1.85.0; MIT; authors `point-grey`.
- `openbim-bsdd` is the canonical reserved scaffold.
- `bsdd` is an exact-version pure re-export and defines nothing.
- Do not claim any bSDD API, model, authentication, or validation capability.
- Do not commit or package standards material, API snapshots, or dictionary
  exports. Link to buildingSMART's official resources instead.
- Publishing to GitHub or crates.io requires a separate explicit maintainer act.
