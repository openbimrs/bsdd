//! Reserved OpenBIM.rs bSDD package scaffold.
//!
//! This crate does **not** implement a buildingSMART Data Dictionary API client,
//! request or response models, authentication, validation, or conformance
//! behavior. Its current release exists only to reserve the canonical package
//! name and establish a standalone repository boundary.

#![forbid(unsafe_code)]

/// Machine-readable statement of the package's current capability level.
pub const PACKAGE_STATUS: &str =
    "reserved scaffold; no bSDD API client, model, or validation is implemented";
