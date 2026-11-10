# CI-attributed DataBoxEdge suppression proposal

This is a consumer compatibility proposal for [Azure/typespec-azure#5892](https://github.com/Azure/typespec-azure/pull/5892), not a linter change or a green-CI claim. One observed diagnostic maps to one authored property and one proposed suppression.

**Publication status:** the consumer branch is published; the draft PR will be linked after creation. See the [machine-readable attribution](companion-suppressions-20261110.json).

## Pinned evidence and source identities

- Linter head: [`ad01897b347c00a353dbb3791671253f1916361d`](https://github.com/Azure/typespec-azure/commit/ad01897b347c00a353dbb3791671253f1916361d).
- Failed CI: [External Integration run 42753183246, job 129621347031](https://github.com/Azure/typespec-azure/actions/runs/42753183246/job/129621347031). Its completed validation reports **604 passed / 1 failed, 605 projects**. This population is separate from the migration report's frozen 487-project comparison.
- Consumer branch point: canonical `Azure/azure-rest-api-specs:typespec-next`, fetched at [`06472951865696fb06a0e36ece718d62bf4edc33`](https://github.com/Azure/azure-rest-api-specs/commit/06472951865696fb06a0e36ece718d62bf4edc33).
- Proposed consumer commit: [`afcbd3a0fd73c1fcf41d1b6fc5467ead292f8b2b`](https://github.com/Azure/azure-rest-api-specs/commit/afcbd3a0fd73c1fcf41d1b6fc5467ead292f8b2b), branch `suppress/pr5892-system-data-in-properties-bag`.
- **Provenance limitation:** CI records checkout of `typespec-next` at 04:11-04:12 UTC on November 10, but does not print the consumer SHA or retain a source-provenance artifact. Its exact consumer commit is therefore **unknown**, not assumed to be the later fetched branch point. The logged declaration and location are reconciled directly with that fetched source; this is not proof of an identical whole CI checkout.

The original complete job log is retained privately with its SHA-256 in the JSON report. Only the relevant sanitized diagnostic is published here; build logs, environment data and machine paths are not copied.

## Attribution and authored edit

| Project / entrypoint | Actual diagnostic target | Raw occurrences | Unique edits | Disposition |
| --- | --- | ---: | ---: | --- |
| `specification/databoxedge/resource-manager/Microsoft.DataBoxEdge/DataBoxEdge`; `client.tsp` | `models.tsp:1447:3`, `DataBoxEdgeDeviceProperties.systemData` | 1 | 1 | Confirmed PR-caused compatibility diagnostic; add a property-level suppression preserving the existing response contract. |

```text
error @azure-tools/typespec-azure-resource-manager/no-reserved-resource-property:
Property "systemData" is not allowed in the resource property bag. This property name is reserved for resource system metadata.
> 1447 |   systemData?: SystemData;
```

Entrypoint provenance is derived from the exact [suite configuration](https://github.com/Azure/typespec-azure/blob/ad01897b347c00a353dbb3791671253f1916361d/.typespec-integration/config.yaml#L2-L12) and pinned runner, rather than a literal entrypoint label in the diagnostic. `client.tsp` exists and is tried first with `--no-emit`. The runner [returns at the first failing entrypoint](https://github.com/microsoft/typespec/blob/8574d5453f7bf9a07dc09bd41edac579af71d94b/packages/tsp-integration/src/validate.ts#L239-L276), so no separate `main.tsp` occurrence is inferred. The compiler command includes [`--warn-as-error`](https://github.com/microsoft/typespec/blob/8574d5453f7bf9a07dc09bd41edac579af71d94b/packages/tsp-integration/src/package-manager.ts#L68-L84): the linter remains warning-severity even though CI prints an error.

## Why this is caused by the PR, not an unrelated same-code warning

The [pre-change rule](https://github.com/Azure/typespec-azure/blob/3f6b4c0518ee1ca9da38571e6a4e7febc7ac0920/packages/typespec-azure-resource-manager/src/rules/no-reserved-resource-property.ts) reserves only `billingData`. The [tested PR rule](https://github.com/Azure/typespec-azure/blob/ad01897b347c00a353dbb3791671253f1916361d/packages/typespec-azure-resource-manager/src/rules/no-reserved-resource-property.ts) adds the `systemData` / `resource system metadata` map entry while retaining the existing reporting path and rule ID. This exact message therefore comes from the added check, not the unchanged billing restriction.

The consumer [configuration](https://github.com/Azure/azure-rest-api-specs/blob/06472951865696fb06a0e36ece718d62bf4edc33/specification/databoxedge/resource-manager/Microsoft.DataBoxEdge/DataBoxEdge/tspconfig.yaml#L45-L48) extends the ARM resource-manager ruleset. [`DataBoxEdgeDevice`](https://github.com/Azure/azure-rest-api-specs/blob/06472951865696fb06a0e36ece718d62bf4edc33/specification/databoxedge/resource-manager/Microsoft.DataBoxEdge/DataBoxEdge/DataBoxEdgeDevice.tsp#L16-L17) uses `TrackedResource<DataBoxEdgeDeviceProperties>`; the diagnosed member is directly in that bag. The warning is consistent with the accepted policy, not a native false positive requiring a linter repair.

The [committed 2023-12-01 schema](https://github.com/Azure/azure-rest-api-specs/blob/06472951865696fb06a0e36ece718d62bf4edc33/specification/databoxedge/resource-manager/Microsoft.DataBoxEdge/DataBoxEdge/stable/2023-12-01/databoxedge.json) already includes read-only `DataBoxEdgeDeviceProperties.systemData`. Removing or relocating that wire property would change an existing API. The proposal instead adds exactly this directive to the diagnosed property:

```typespec
#suppress "@azure-tools/typespec-azure-resource-manager/no-reserved-resource-property" "Existing API exposes systemData in the device properties bag; preserve the published response contract."
```

The [directive documentation](https://typespec.io/docs/language-basics/directives/#suppress) supports a full diagnostic code and an explicit justification. Existing model-level baseline annotations, the visibility decorator and every original source byte remain unchanged.

## Exclusions and limits

- No `billingData` annotation: that is an unchanged reporting path and is not the observed failure.
- No recursive/embedded-envelope suppression or AzureDataTransfer edit: neither is diagnosed by this CI run under the approved narrower policy.
- No namespace-wide suppression, historical-version blanket edits, API changes, common-types changes, generated Swagger, dependency/lock changes or CI-setting changes.
- One raw occurrence deduplicates by source target, full rule code and exact message to one authored edit. There are no unresolved diagnostic targets. The missing whole-checkout SHA remains a disclosed provenance limitation.
- A suppressed client entrypoint could expose later failures, including the previously unreached `main.tsp`; this proposal does not claim all CI will pass.

## Validation and proposal boundary

**Local compilation, builds, tests, lint, formatting, integration, emission and dependency setup were intentionally not run**, as required by the suppression-only proposal contract. Only existing CI, source/schema inspection, the complete one-line diff and publication identities were inspected. No new CI was requested or awaited, and no merge or landing coordination is part of this proposal.
