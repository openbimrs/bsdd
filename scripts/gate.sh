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
python3 scripts/check-package-contents.py
# Package both crates together: cargo verifies the alias against the packaged
# canonical crate through its temporary registry.
cargo package --locked -p openbim-bsdd -p bsdd
