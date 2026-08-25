# bsdd alias plan

Status: published pure re-export alias.
Last updated: 2026-08-25

## Invariant

`src/lib.rs` contains comments plus only:

```rust
pub use openbim_bsdd::*;
```

The sole dependency remains pinned to the exact canonical version.

## Work queue

- [x] `ALIAS-RELEASE` — fully package and release after matching
  `openbim-bsdd` exists on crates.io

No feature implementation belongs in this package.
