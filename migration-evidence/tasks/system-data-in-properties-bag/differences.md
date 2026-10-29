# Grouped diagnostic differences

This appendix accounts for every difference in the completed 487-project comparison. All projects are assessable; no worker failed. The complete population has 485 equal-zero projects, zero Swagger-linter-only projects, and the two TypeSpec-linter-only projects below. Both raw and conservative location totals are 0/2, with no count adjustment.

The helper explanations are code-backed inferences from the pinned installed producer and saved schemas, not newly executed Swagger traces. The separate witnesses prove both targets are real selected-version HTTP payload fields regardless of the exact resolved-object iteration order.

| Group                                                                                         | Swagger linter | TypeSpec linter | Cause and disposition                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------- | -------------: | --------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [AzureDataTransfer nested connection metadata](#azuredatatransfer-nested-connection-metadata) |              0 |               1 | Selected-version emitted payload contains the target. Complete semantic recursion intentionally exceeds the original helper's first-child traversal. No TypeSpec rule update required for the frozen intended policy.                                         |
| [DataBoxEdge direct bag metadata](#databoxedge-direct-bag-metadata)                           |              0 |               1 | Selected-version emitted payload contains direct bag `systemData`. Its saved schema's first key is scalar `type`, illustrating the original helper's short-circuit before later payload properties. No TypeSpec rule update required for the intended policy. |

## AzureDataTransfer nested connection metadata

- **Classification:** TypeSpec-linter-only.
- **Status:** intentional semantic difference; not functional/output equivalence.
- **Project:** `specification/azuredatatransfer/resource-manager/Microsoft.AzureDataTransfer/AzureDataTransfer`.
- **Selected API version:** `2026-02-06-preview`.
- **Target:** `models.tsp:1644:3`, `ReadPipelineConnection.systemData`.
- **Source:** [frozen models](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/azuredatatransfer/resource-manager/Microsoft.AzureDataTransfer/AzureDataTransfer/models.tsp#L1613-L1649) and [Pipeline resource](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/azuredatatransfer/resource-manager/Microsoft.AzureDataTransfer/AzureDataTransfer/Pipeline.tsp#L20).
- **Exact source/schema hashes and reference edges:** [machine-readable witness](azuredatatransfer-witness.json).

### TypeSpec source

Relevant declarations, excerpted from the frozen source:

```typespec
model Pipeline is Azure.ResourceManager.TrackedResource<PipelineProperties> {
  // ResourceNameParameter customization omitted from this excerpt.
}

model PipelineProperties {
  remoteCloud: string;
  displayName?: string;

  @visibility(Lifecycle.Read)
  @identifiers(#["id"])
  connections?: ReadPipelineConnection[];
  // Other properties omitted.
}

model ReadPipelineConnection {
  ...Record<unknown>;
  id: string;

  // name, type, location and etag omitted.
  systemData?: SystemData;

  properties?: PipelineConnectionProperties;
}
```

The envelope is a standard tracked ARM resource. The reported property is in an array element below its `properties` bag, not the standard system-data envelope of `Pipeline`.

### Saved Swagger and HTTP reachability

The baseline-relative document is:

`projects/specification/azuredatatransfer/resource-manager/Microsoft.AzureDataTransfer/AzureDataTransfer/swagger/preview/2026-02-06-preview/azuredatatransfer.json`.

It contains these actual reference edges:

```text
GET /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureDataTransfer/pipelines/{pipelineName}
  operationId: Pipelines_Get
  200 schema -> #/definitions/Pipeline
  Pipeline.properties.properties -> #/definitions/PipelineProperties
  PipelineProperties.properties.connections.items -> #/definitions/ReadPipelineConnection
  ReadPipelineConnection.properties.systemData -> common-types/resource-management/v6/types.json#/definitions/systemData
```

Relevant saved schema excerpts:

```json
{
  "PipelineProperties": {
    "type": "object",
    "description": "Properties of pipeline",
    "properties": {
      "remoteCloud": { "type": "string" },
      "displayName": { "type": "string" },
      "connections": {
        "type": "array",
        "items": { "$ref": "#/definitions/ReadPipelineConnection" },
        "readOnly": true,
        "x-ms-identifiers": ["id"]
      }
    }
  },
  "ReadPipelineConnection": {
    "type": "object",
    "properties": {
      "systemData": {
        "$ref": "../../../../../../../../../common-types/resource-management/v6/types.json#/definitions/systemData",
        "description": "Metadata pertaining to creation and last modification of the resource."
      },
      "properties": {
        "$ref": "#/definitions/PipelineConnectionProperties"
      }
    }
  }
}
```

Unrelated schema properties/descriptions are omitted. The witness retains the actual complete selected edges and schema key order. No Swagger was regenerated or validated.

### Cause, units, and disposition

| Engine          | Observed result                                                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Swagger linter  | 0 saved findings in this project; production ARM rule registration and completed execution are established by the saved-log audit. |
| TypeSpec linter | 1 fresh finding at the original authored `ReadPipelineConnection.systemData` declaration.                                          |

This target is present in the selected version's emitted GET response graph. Its difference is therefore **not** explained away as an older-version, source-only, unreachable, unresolved-reference, or missing-project artifact.

The pinned Swagger helper returns `[]` for a child without a match and then treats that array as truthy:

```javascript
for (const [key, value] of Object.entries(object)) {
  const result = deepFindObjectKeyPath(value, keyName, lodash_1.default.concat(path, key));
  if (result) {
    return result;
  }
}
return [];
```

Consequently it cannot continue to later siblings after the first child's no-match result. The saved `PipelineProperties` schema starts with scalar `type` and `description` keys before its payload `properties`; its payload also begins with compliant `remoteCloud` and `displayName` before `connections`. The original function scans schema-object keys and reports only a first path. The native contract instead traverses all model properties, array items, dictionary values and union variants and reports distinct offending authored declarations.

This is a code-backed explanation using the saved output and installed helper, not a new execution trace of the Swagger linter. The original implementation and diagnostic units are intentionally not reproduced. There is no justified count normalization turning the native 1 into 0.

**Disposition: No TypeSpec rule update required** for the frozen intended recursive payload policy. Preserve the observed 0/1 and state that strict functional equivalence to the defective original traversal is not established. The focused later-sibling/container tests and actual injected complete-graph control provide discriminating native regression evidence.

## DataBoxEdge direct bag metadata

- **Classification:** TypeSpec-linter-only.
- **Status:** intentional semantic difference; not functional/output equivalence.
- **Project:** `specification/databoxedge/resource-manager/Microsoft.DataBoxEdge/DataBoxEdge`.
- **Selected API version:** `2023-12-01`.
- **Target:** `models.tsp:1447:3`, `DataBoxEdgeDeviceProperties.systemData`.
- **Source:** [frozen bag declaration](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/databoxedge/resource-manager/Microsoft.DataBoxEdge/DataBoxEdge/models.tsp#L1438-L1453) and [standard tracked resource](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/databoxedge/resource-manager/Microsoft.DataBoxEdge/DataBoxEdge/DataBoxEdgeDevice.tsp#L16).
- **Exact source/schema hashes and reference edges:** [machine-readable witness](databoxedge-witness.json).

### TypeSpec source

The relevant authored bag excerpt is:

```typespec
model DataBoxEdgeDeviceProperties {
  /**
   * DataBoxEdge Device Properties
   */
  @visibility(Lifecycle.Read)
  systemData?: SystemData;
  // Remaining properties omitted.
}
```

`DataBoxEdgeDevice` is a standard `TrackedResource<DataBoxEdgeDeviceProperties>`. The new finding concerns the additional bag member, not the valid system-data field inherited in the outer resource envelope. The existing source suppressions address unrelated rules and do not suppress this new opt-in policy.

### Saved Swagger and HTTP reachability

The selected saved document is:

`projects/specification/databoxedge/resource-manager/Microsoft.DataBoxEdge/DataBoxEdge/swagger/stable/2023-12-01/databoxedge.json`.

The exact emitted reference path is:

```text
GET /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}
  operationId: Devices_Get
  200 schema -> #/definitions/DataBoxEdgeDevice
  DataBoxEdgeDevice.properties.properties -> #/definitions/DataBoxEdgeDeviceProperties
  DataBoxEdgeDeviceProperties.properties.systemData -> common-types/resource-management/v3/types.json#/definitions/systemData
```

Relevant schema excerpt, with unrelated fields omitted:

```json
{
  "DataBoxEdgeDeviceProperties": {
    "type": "object",
    "description": "The properties of the Data Box Edge/Gateway device.",
    "properties": {
      "systemData": {
        "$ref": "../../../../../../../../../common-types/resource-management/v3/types.json#/definitions/systemData",
        "description": "DataBoxEdge Device Properties",
        "readOnly": true
      }
    }
  }
}
```

| Engine          | Observed result                                                                       |
| --------------- | ------------------------------------------------------------------------------------- |
| Swagger linter  | 0 saved findings in this project, with registered production ARM execution completed. |
| TypeSpec linter | 1 fresh finding at the original direct bag property `models.tsp:1447:3`.              |

This is not a source-only or different-version declaration: it is present in the selected version's emitted GET response. The saved schema has scalar `type` before nested payload `properties`; code inspection shows how the helper returns an empty-array result on a nonmatching first child instead of searching later children. This explains the class of missed policy without claiming a newly captured resolved-object execution trace. Unlike the preceding array case, this direct member needs no array/union traversal to demonstrate the missed policy.

SDK-specific `clientName` metadata does not change the JSON property, rule identity, or count. The TypeSpec linter uses JSON wire names and has no TCGC dependency. Both reported counts and this concrete reference path remain unchanged; no fuzzy name matching or after-analysis count adjustment is used.

**Disposition: No TypeSpec rule update required** for the frozen intended policy. Retain the intentional 0/1 difference and the non-equivalence limitation rather than reproducing the upstream false negative.
