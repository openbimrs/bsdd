# bSDD repository instructions

This repository owns an OpenBIM.rs package-name reservation for a possible
future buildingSMART Data Dictionary integration. The packages are reserved
scaffolds; never describe an API client, model, authentication flow, validation,
or conformance behavior as implemented without executable evidence.

## Map

- `openbim-bsdd/` — canonical package and sole home of future implementation
- `bsdd/` — exact-version pure re-export alias; no implementation or types
- `docs/` — maintained architecture documentation
- `scripts/gate.sh` — authoritative standalone verification gate
- `references/` — ignored local material; never package or commit

## Commands

```bash
./scripts/gate.sh
cargo test --workspace
scripts/check-alias-purity.sh
```

Trust command exit codes. Do not hide failures in pipelines or summarize an
unrun command as passing.

## Boundaries

- `openbim-bsdd` currently exposes only an honest package status marker.
- `bsdd/src/lib.rs` may contain comments plus exactly
  `pub use openbim_bsdd::*;`.
- The alias dependency must stay pinned to the exact canonical version.
- No vendored standards, API specifications, schemas, or bSDD data snapshots.
- External buildingSMART links do not imply affiliation or endorsement.
- Capability claims must distinguish a reserved package from implemented and
  conformance-tested behavior.
