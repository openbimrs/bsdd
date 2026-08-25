# bsdd alias instructions

Purpose: short crates.io package-name alias for `openbim-bsdd`.
Follow `../AGENTS.md` and read `PLAN.md` for release coordination.

## Invariant

Apart from comments, `src/lib.rs` must contain exactly:

```rust
pub use openbim_bsdd::*;
```

Defining any item or behavior here is a defect. Keep the sole dependency pinned
to the exact canonical version. `scripts/check-alias-purity.sh` enforces these
rules semantically from Cargo metadata and the active library source.
