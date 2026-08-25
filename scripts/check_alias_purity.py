#!/usr/bin/env python3
"""Fail closed unless `bsdd` is a semantic pure alias of `openbim-bsdd`."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import NoReturn

ROOT = Path(__file__).resolve().parent.parent


def fail(message: str) -> NoReturn:
    print(f"alias purity: {message}", file=sys.stderr)
    raise SystemExit(1)


def package(packages: list[dict], name: str) -> dict:
    matches = [candidate for candidate in packages if candidate["name"] == name]
    if len(matches) != 1:
        fail(f"expected exactly one {name!r} package, found {len(matches)}")
    return matches[0]


def normalized(path: str | Path) -> Path:
    return Path(path).resolve()


metadata = json.loads(
    subprocess.run(
        ["cargo", "metadata", "--no-deps", "--format-version", "1"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout
)
packages = metadata["packages"]
canonical = package(packages, "openbim-bsdd")
alias = package(packages, "bsdd")

canonical_version = canonical["version"]
alias_version = alias["version"]
if alias_version != canonical_version:
    fail(
        f"package versions differ: bsdd={alias_version}, "
        f"openbim-bsdd={canonical_version}"
    )

expected_alias_manifest = normalized(ROOT / "bsdd/Cargo.toml")
if normalized(alias["manifest_path"]) != expected_alias_manifest:
    fail(f"bsdd manifest moved outside {expected_alias_manifest}")

if alias.get("features"):
    fail("bsdd must not define features")
if alias.get("links") is not None:
    fail("bsdd must not define a native links contract")
if len(alias["targets"]) != 1:
    fail("bsdd must contain exactly one Cargo target")

target = alias["targets"][0]
if target["kind"] != ["lib"] or target["crate_types"] != ["lib"]:
    fail("bsdd's only target must be a normal library")
if target["name"] != "bsdd":
    fail(f"bsdd library target has unexpected name {target['name']!r}")

source_path = normalized(target["src_path"])
expected_source_path = normalized(ROOT / "bsdd/src/lib.rs")
if source_path != expected_source_path:
    fail(f"bsdd library target must be {expected_source_path}, got {source_path}")

meaningful_lines = [
    line.strip()
    for line in source_path.read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.lstrip().startswith("//")
]
if meaningful_lines != ["pub use openbim_bsdd::*;"]:
    fail("bsdd library must contain only `pub use openbim_bsdd::*;` apart from comments")

dependencies = alias["dependencies"]
if len(dependencies) != 1:
    fail("bsdd must depend only on openbim-bsdd")
dependency = dependencies[0]
if dependency["name"] != "openbim-bsdd" or dependency.get("rename") is not None:
    fail("bsdd's sole dependency must be the unrenamed openbim-bsdd package")
if dependency.get("kind") is not None or dependency.get("optional"):
    fail("openbim-bsdd must be a required normal dependency")
expected_requirement = f"={canonical_version}"
if dependency["req"] != expected_requirement:
    fail(
        f"openbim-bsdd requirement must be {expected_requirement}, "
        f"got {dependency['req']}"
    )
expected_dependency_path = normalized(ROOT / "openbim-bsdd")
if dependency.get("path") is None:
    fail("openbim-bsdd must be a local path dependency for workspace validation")
if normalized(dependency["path"]) != expected_dependency_path:
    fail(
        f"openbim-bsdd path must resolve to {expected_dependency_path}, "
        f"got {dependency['path']}"
    )

extra_rust_sources = sorted(
    path.relative_to(ROOT) for path in (ROOT / "bsdd").rglob("*.rs") if path != source_path
)
if extra_rust_sources:
    fail(f"bsdd contains unexpected Rust sources: {extra_rust_sources}")

print("alias purity: ok")
