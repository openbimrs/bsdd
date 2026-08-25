#!/usr/bin/env bash
# Complete standalone verification gate for openbimrs/bsdd.
set -euo pipefail

cd "$(dirname "$0")/.."

cargo fmt --all -- --check
cargo build --workspace --all-targets
cargo test --workspace --all-features
cargo clippy --workspace --all-targets --all-features -- -D warnings
RUSTDOCFLAGS="-D warnings" cargo doc --workspace --all-features --no-deps
scripts/check-alias-purity.sh
scripts/test-alias-purity.sh
# Verify Cargo's full source preparation and build for the canonical crate.
cargo package --locked -p openbim-bsdd
# Full alias verification requires openbim-bsdd = 0.1.0 in crates.io after the
# canonical release. Listing still validates the alias package file boundary.
cargo package --locked --list -p bsdd
