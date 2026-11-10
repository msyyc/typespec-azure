# Diagnostic differences at the synchronized review-fix head

All 487 projects were assessed successfully at `ad01897b347c00a353dbb3791671253f1916361d` against the unchanged frozen Swagger population. Current shared-rule totals are Swagger 0 / TypeSpec 1, entirely attributable to `systemData`; `billingData` contributes zero. The [full observations](runs/fix5892-20261110/observations.json) and [independent recount](runs/fix5892-20261110/summary.json) retain every project, including zero and failure states. [Exact comparison](runs/fix5892-20261110/comparison.json) confirms no target/message, aligned-warning or default-warning change in any project from the preceding consolidated run.

| Current differing project                       | Swagger diagnostics | TypeSpec diagnostics for the same check | Coverage and recommended action                                                                     |
| ----------------------------------------------- | ------------------: | --------------------------------------: | --------------------------------------------------------------------------------------------------- |
| [DataBoxEdge](#databoxedge-direct-bag-metadata) |                   0 |                                       1 | Covered direct bag violation. Retain the linter check; a separate consumer suppression preserves the existing API without changing these frozen counts. |

Every other project remains 0/0. No count adjustment, deduplication or fuzzy correspondence is used. AzureDataTransfer below is an approved historical scope correction and current matching control, not a current one-sided diagnostic group.

## AzureDataTransfer embedded connection envelope

- Project: `specification/azuredatatransfer/resource-manager/Microsoft.AzureDataTransfer/AzureDataTransfer`.
- Selected API version: `2026-02-06-preview`.
- Historical target: `models.tsp:1644:3`, `ReadPipelineConnection.systemData`.
- Frozen [model declaration](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/azuredatatransfer/resource-manager/Microsoft.AzureDataTransfer/AzureDataTransfer/models.tsp#L1613-L1649).
- [Original source/schema hashes and reference edges](azuredatatransfer-witness.json).

```text
Pipelines_Get -> Pipeline -> PipelineProperties
  -> connections[] -> ReadPipelineConnection.systemData
```

The connection object has its own `id`, `name`, `type`, `systemData` and `properties`. The saved schema proves it is selected-version HTTP payload, not a version/reachability artifact. That proof does not establish that metadata in this embedded envelope is incorrectly placed.

The prior recursive checker emitted one warning. The current TypeSpec check only visits immediate/inherited members of the recognized resource's properties model, and therefore emits none here. The selected policy does not adjudicate arbitrary nested metadata.

**Coverage status: approved retirement of the recursive warning; current counts are Swagger 0 / TypeSpec 0. Recommended action: keep the narrower check.** The user approved shallow existing-rule consolidation under [ARM envelope guidance](https://github.com/Azure/azure-resource-manager-rpc/blob/8231d7df51aec87e6ccb5bcc04478136758b0a4c/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources). Canonical test `accepts envelope metadata, embedded resource envelopes and nearby names` reproduces an array of envelope-shaped connection objects, contrasting with `rejects the immediate resource property %s` in the [exact-head suite](https://github.com/Azure/typespec-azure/blob/ad01897b347c00a353dbb3791671253f1916361d/packages/typespec-azure-resource-manager/test/rules/no-reserved-resource-property.test.ts). The current actual-package [embedded-envelope control](runs/fix5892-20261110/controls.json) passes. These are scoped semantic controls, not exhaustive Swagger-equivalence proof.

Historical raw 0/1 is preserved in [checkpoint A observations](runs/checkpointA-round1/observations.json); current raw 0/0 is preserved in [current observations](runs/fix5892-20261110/observations.json).

## DataBoxEdge direct bag metadata

- Project: `specification/databoxedge/resource-manager/Microsoft.DataBoxEdge/DataBoxEdge`.
- Selected API version: `2023-12-01`.
- Exact current target: `models.tsp:1447:3`, `DataBoxEdgeDeviceProperties.systemData`.
- Frozen [bag declaration](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/databoxedge/resource-manager/Microsoft.DataBoxEdge/DataBoxEdge/models.tsp#L1438-L1453) and [standard tracked resource](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/databoxedge/resource-manager/Microsoft.DataBoxEdge/DataBoxEdge/DataBoxEdgeDevice.tsp#L16).
- [Original source/schema hashes and reference edges](databoxedge-witness.json).

```text
Devices_Get -> DataBoxEdgeDevice -> DataBoxEdgeDeviceProperties.systemData
```

`DataBoxEdgeDevice` is a `TrackedResource<DataBoxEdgeDeviceProperties>`. The offending member is in its properties bag, not the valid system-data member of its outer resource envelope. The saved response references common-types `v3` system metadata.

The current warning is:

```text
@azure-tools/typespec-azure-resource-manager/no-reserved-resource-property
Property "systemData" is not allowed in the resource property bag. This property name is reserved for resource system metadata.
```

The pinned [Swagger helper](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/packages/rulesets/src/spectral/functions/utils.ts#L293-L308) returns `[]` for a nonmatching child and tests that truthy result before continuing. The saved bag schema starts with scalar `type` before payload `properties`, illustrating the short-circuit limitation. Saved production logs establish zero Swagger findings; this is a code-backed explanation, not a new Swagger execution trace.

**Coverage status: retained direct-bag violation, not strict output equivalence. Recommended action: retain the TypeSpec check and do not port the upstream false-negative bug.** Canonical direct-member cases in the [exact-head suite](https://github.com/Azure/typespec-azure/blob/ad01897b347c00a353dbb3791671253f1916361d/packages/typespec-azure-resource-manager/test/rules/no-reserved-resource-property.test.ts) and assessed [incorrect/correct actual-package controls](runs/fix5892-20261110/controls.json) distinguish this violation from valid standard envelope metadata. Frozen source suppressions do not suppress the target; its assessed default configuration also reports it. Source-scope versus latest-version populations differ generally, but this exact finding is verified in the selected emitted schema.

The later [CI-attributed consumer proposal](companion-suppressions-20261110.md), [Azure/azure-rest-api-specs#48080](https://github.com/Azure/azure-rest-api-specs/pull/48080), adds one property-level suppression to preserve the published DataBoxEdge contract. This is an explicit compatibility exception, not a false-positive finding, linter change or adjustment to the frozen 0/1 score. Its separate 605-project CI population, missing tested-consumer SHA and intentionally unrun local validation are disclosed in the attribution report.

## Limits

Zero saved Swagger findings means no observed Swagger-positive finding was lost in this population. It does not establish exhaustive equivalence or a coverage percentage. The TypeSpec rule intentionally does not cover recursive searches, arbitrary non-resource bags or JSON aliases; it retains the existing authored-name, case-insensitive and type-independent policy. Comparable violation totals remain unassessed. See the complete current [migration report](migration.md).
