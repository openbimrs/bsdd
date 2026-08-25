# openbim-bsdd implementation plan

Status: package name reserved; implementation not started.
Last updated: 2026-08-25

This file records future work, not current capability.

## Established boundary

The canonical crate is the only package where implementation may be added. The
`bsdd` sibling remains a pure re-export at every version.

## Open work

- [ ] `BSDD-CONTRACT` — research and review a minimal, versioned client contract
- [ ] `BSDD-MODEL` — design loss-aware response models against current official documentation
- [ ] `BSDD-CLIENT` — implement an HTTP client with explicit authentication and error behavior
- [ ] `BSDD-EVIDENCE` — add redistributable fixtures and executable integration evidence

Nothing above is implemented or promised by version `0.1.0`.
