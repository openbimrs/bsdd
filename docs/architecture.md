# Architecture

## Repository role

`openbimrs/bsdd` is a standalone OpenBIM.rs repository reserving package names
for a possible future buildingSMART Data Dictionary integration. It is not the
official bSDD service or documentation repository and currently contains no API
client, domain model, authentication, or validation implementation.

Every published-package field is explicit in each package manifest. The child
repository can therefore build, test, document, and package without inheriting
configuration from an integration workspace.

## Package identity

```text
bsdd  -- path + exact =0.1.0 dependency -->  openbim-bsdd
(alias; re-export only)                      (canonical scaffold)
```

Cargo dependency renaming is consumer-local and does not reserve another
crates.io package name. Two package records are therefore needed. All public
items originate in `openbim-bsdd`; `bsdd` contains only:

```rust
pub use openbim_bsdd::*;
```

The exact version requirement prevents alias and canonical releases from
silently drifting. The local path allows workspace verification before release;
Cargo removes that path from the published manifest and retains `=0.1.0`.

## Current boundary

`openbim-bsdd` deliberately has no dependencies and exposes only
`PACKAGE_STATUS`. A future implementation must begin with an independently
reviewed contract and executable evidence. A package name, README roadmap, or
link to buildingSMART documentation does not establish capability.

## Packaging and release sequence

1. Run `./scripts/gate.sh` on Rust 1.85.0.
2. Inspect and publish `openbim-bsdd` through an explicit maintainer action.
3. Confirm `openbim-bsdd` at the exact version is available from crates.io.
4. Replace the alias list-only gate with full alias package verification.
5. Inspect and publish the matching `bsdd` package explicitly.

The repository CI never publishes. Before step 3, `cargo package --list -p bsdd`
is intentional: full verification resolves the alias's registry-normalized exact
dependency, which cannot succeed until the canonical package exists there.

## External material

The official bSDD service, API documentation, and developer resources remain
external buildingSMART resources. This repository vendors no standards, API
snapshots, schemas, or dictionary data. Locally consulted files belong under the
ignored `references/` path and must not enter a package.
