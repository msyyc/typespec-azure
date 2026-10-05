---
title: Unified examples
order: 0
---

Azure service examples can be stored in the unified `examples.yaml` format instead of
versioned `x-ms-examples` JSON files. The format stores all versions of an operation's
request and response examples together, using `since` to identify variants introduced
in later API versions.

## Validate examples

Install the `@azure-tools/typespec-azure-examples` package, then run the validator from
the service directory:

```bash
tsp-examples validate <service-dir>
```

The validator discovers `examples.yaml` and `examples/<Interface>.yaml` files, reads
version metadata from the adjacent `service.yaml`, and exits with a non-zero status
when it finds an error. Use `--warn-as-error` to also fail on warnings.

The format requires response status keys to be integers, quoted `since` values to
refer to versions in `service.yaml`, and all examples for an operation to be kept in
one file. The only supported placeholder for an embedded API version is
`{api-version}`.

## Migrate existing examples

The migration command converts versioned Swagger `x-ms-examples` files to the unified
format:

```bash
tsp-examples-migrate <spec-dir> --out <service-dir>
```

The input directory uses the `stable/<version>/` and `preview/<version>/` layout.
The command follows each operation's `x-ms-examples` references and writes one
`examples.yaml`, or one file per interface when `--split-by-interface` is specified.
Generated output is validated before it is written.

If the input contains a `service.yaml`, or one is supplied with `--service`, its
version list controls the migration. Swagger versions not listed there are ignored.
Use `--namespace` when the namespace cannot be detected from the provider path.
Other supported options include `--dry-run` and `--warn-as-error`.

The migration normalizes API-version values embedded in headers and URLs, groups
identical examples across versions, and emits a base example plus `since` variants
when an example changes. Because the format has no `until` marker, examples removed
in a later version produce an `example-removed-before-latest` warning and must be
reviewed manually.

> **Note:** `tsp-examples-migrate` is a transitional tool for bulk conversion. It is
> intended to be removed once services author `examples.yaml` directly.
