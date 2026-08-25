# OpenBIM.rs bSDD

[![CI](https://github.com/openbimrs/bsdd/actions/workflows/ci.yml/badge.svg)](https://github.com/openbimrs/bsdd/actions/workflows/ci.yml)
[![crates.io](https://img.shields.io/crates/v/openbim-bsdd.svg)](https://crates.io/crates/openbim-bsdd)
[![docs.rs](https://docs.rs/openbim-bsdd/badge.svg)](https://docs.rs/openbim-bsdd)
[![MSRV](https://img.shields.io/badge/MSRV-1.85.0-blue)](https://www.rust-lang.org)

A standalone Rust workspace reserving the OpenBIM.rs package names for a
possible future integration with the buildingSMART Data Dictionary (bSDD).

> [!IMPORTANT]
> Version `0.1.0` is a **reserved scaffold only**. It does not provide a bSDD
> API client, request or response models, authentication, data validation, or
> conformance guarantees. Package-name ownership must not be read as a claim of
> bSDD functionality.

## Capability status

| Capability | Status |
| --- | --- |
| Standalone Rust 2021 package-name scaffold | Present |
| Lockstep canonical and pure-alias package layout | Present and structurally gated |
| bSDD API HTTP client | Not implemented |
| bSDD request/response data model | Not implemented |
| Authentication or dictionary publishing | Not implemented |
| Validation or conformance checking | Not implemented |
| Offline cache or vendored dictionary data | Not implemented |

## Package architecture

| Package | Role |
| --- | --- |
| [`openbim-bsdd`](openbim-bsdd/) | Canonical reserved scaffold; the only package in which future implementation may live |
| [`bsdd`](bsdd/) | Exact-version pure re-export alias; defines no independent API or types |

```text
bsdd  -- exact =0.1.0 dependency -->  openbim-bsdd
(alias; no implementation)           (canonical reserved scaffold)
```

Cargo permits dependency renaming but crates.io has no publisher-side package
alias. The two package records reserve both names while `bsdd` re-exports the
canonical crate, preserving one source for any future API.

## Install

After the corresponding version has been published to crates.io, choose one
package name (do not add both directly):

```bash
cargo add openbim-bsdd@0.1.0
# or
cargo add bsdd@0.1.0
```

For this unpublished local candidate, use a path dependency instead:

```toml
openbim-bsdd = { path = "path/to/bsdd/openbim-bsdd" }
```

The only current item is a status marker:

```rust
assert!(openbim_bsdd::PACKAGE_STATUS.contains("reserved scaffold"));
```

## Official bSDD resources

This project is independent of buildingSMART International. Authoritative bSDD
product and API information belongs to buildingSMART:

- [buildingSMART Data Dictionary service](https://www.buildingsmart.org/users/services/buildingsmart-data-dictionary/)
- [Official bSDD repository and developer documentation](https://github.com/buildingSMART/bSDD)
- [Official bSDD API documentation](https://app.swaggerhub.com/apis-docs/buildingSMART/Dictionaries/v1)

No standards text, API snapshots, schemas, or dictionary exports are vendored
in this repository.

## Development

Rust `1.85.0` is the minimum supported version. Python `3.10` or newer is used
by the semantic alias-purity gate.

```bash
git clone https://github.com/openbimrs/bsdd.git
cd bsdd
./scripts/gate.sh
```

The gate checks formatting, build, tests, Clippy, rustdoc, alias purity, and the
package contents. The canonical crate is fully packaged and verified. Until
`openbim-bsdd = 0.1.0` exists in the registry, the alias is checked with
`cargo package --list` because crates.io package verification cannot resolve
its exact registry dependency before the canonical package is released.

See [the architecture notes](docs/architecture.md) and
[contribution guide](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE).
