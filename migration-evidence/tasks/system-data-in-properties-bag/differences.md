# Diagnostic differences after the review fixes

All 487 projects were assessed successfully against the unchanged frozen Swagger population. Current shared-rule totals are Swagger 0 / TypeSpec 1, entirely attributable to `systemData`; `billingData` contributes zero. The [full observations](runs/fix5892-20261106/observations.json) and [independent recount](runs/fix5892-20261106/summary.json) retain every project, including zero and failure states.

| Project           | Historical recursive native | Current native | Swagger | Disposition                                                                                   |
| ----------------- | --------------------------: | -------------: | ------: | --------------------------------------------------------------------------------------------- |
| AzureDataTransfer |                           1 |              0 |       0 | Authorized narrowing: do not infer invalid metadata from a nested embedded resource envelope. |
| DataBoxEdge       |                           1 |              1 |       0 | Retained direct bag violation; pinned Swagger helper false-negative limitation.               |

Every other project remains 0/0. No count adjustment, deduplication or fuzzy correspondence is used.

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

The prior recursive checker emitted one warning. The current native check only visits immediate/inherited members of the recognized resource's properties model, and therefore emits none here. The selected native policy does not adjudicate arbitrary nested metadata.

**Disposition: intended correction of the proposed native scope.** The user approved shallow existing-rule consolidation. Canonical test `accepts envelope metadata, embedded resource envelopes and nearby names` reproduces an array of envelope-shaped connection objects, with a contrasting direct-bag violation in `rejects the immediate resource property %s`. The actual-package `embedded-resource-and-nested-object` control also passes. These are native semantic controls, not proof of exhaustive Swagger equivalence.

Historical raw 0/1 is preserved in [checkpoint A observations](runs/checkpointA-round1/observations.json); current raw 0/0 is preserved in [current observations](runs/fix5892-20261106/observations.json).

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

**Disposition: retained direct-bag native violation, not strict output equivalence.** Canonical direct-member cases and the published incorrect/correct actual-package controls distinguish the violation from valid standard envelope metadata. Existing source suppressions do not suppress this target; the current default configuration also reports it. Source-scope versus latest-version populations differ generally, but this exact finding is verified in the selected emitted schema.

## Limits

Zero saved Swagger findings means no observed Swagger-positive finding was lost in this population. It does not establish exhaustive equivalence. The native rule intentionally does not cover recursive searches, arbitrary non-resource bags or JSON aliases; it retains the existing authored-name, case-insensitive and type-independent policy. See the complete current [migration report](migration.md).
