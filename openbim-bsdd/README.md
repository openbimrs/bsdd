# openbim-bsdd

Canonical OpenBIM.rs package-name reservation for a possible future
buildingSMART Data Dictionary (bSDD) integration.

## Status

**Reserved scaffold only.** Version `0.1.0` does not implement an API client,
request or response model, authentication, dictionary publishing, validation,
or conformance checking. It currently exposes only `PACKAGE_STATUS`.

See the repository [capability table](https://github.com/openbimrs/bsdd#capability-status)
and [architecture notes](https://github.com/openbimrs/bsdd/blob/main/docs/architecture.md).

The sibling [`bsdd`](https://crates.io/crates/bsdd) package is an exact-version
pure re-export. Choose one package name rather than depending on both directly.

## External documentation

For the actual service and API, use buildingSMART's
[official bSDD resources](https://www.buildingsmart.org/users/services/buildingsmart-data-dictionary/).
No API specification or dictionary data is included here.

## License

MIT
