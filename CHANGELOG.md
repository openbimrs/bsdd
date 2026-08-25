# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Changed

- The steady-state release gate now fully packages the published `bsdd` alias.
- Alias purity now fails closed over Cargo dependency, feature, target, build,
  and source shape, with 19 mutation probes and exact package allowlists.
- CI now pins its runner and action revisions.
- Replaced the retired SwaggerHub documentation URL with buildingSMART's
  maintained bSDD API documentation page.

## [0.1.0] - 2026-08-25

### Added

- Reserved the `openbim-bsdd` canonical package name with an explicitly
  non-functional scaffold.
- Added `bsdd` as an exact-version pure re-export alias.
- Added standalone documentation, CI, packaging checks, and a mutation-verified
  semantic alias-purity gate.

[Unreleased]: https://github.com/openbimrs/bsdd/commits/main
[0.1.0]: https://crates.io/crates/openbim-bsdd/0.1.0
