# specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis

[All project differences](../instance-correspondence.md#differing-projects).

**Project totals:** Swagger 1 raw / 1 member checks; TypeSpec 0 raw; 0 findings credited to the same comparison. Common project/route unit: 1 Swagger / 0 TypeSpec. Counts repeated across different members at the same operation are non-additive. TypeSpec counts refer only to arm-resource-operation-response, not the entire linter suite.

<a id="s-1eade2d50db1582c"></a>

### PutRequestResponseSchemeArm: PrivateEndpointConnections_CreateOrUpdate

**Identity:** `1eade2d50db1582c`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName}/privateEndpointConnections/{privateEndpointConnectionName}`.
**Swagger document:** `projects/specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis/swagger/preview/2025-04-01-preview/healthcare-apis.json`.
**Observed comparison:** Registered response, but PUT absent from retained operation map.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation                        | Request schema                                                                                                            | Success response schemas                                  |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| `put` `PrivateEndpointConnections_CreateOrUpdate` | `../../../../../../../../../common-types/resource-management/v3/privatelinks.json#/definitions/PrivateEndpointConnection` | `200: #/definitions/PrivateEndpointConnectionDescription` |

| TypeSpec operation                                                                                                                                                                                                                                                                                              | Effective request                                             | Canonical association / request checked | Registered return candidates |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------- | ---------------------------- |
| [Microsoft.HealthcareApis.PrivateEndpointConnectionDescriptions.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis/PrivateEndpointConnectionDescription.tsp#L69) | `Azure.ResourceManager.CommonTypes.PrivateEndpointConnection` | `(none)`                                | `(none)`                     |

**Explanation:** The response body is registered, but this operation has no retained resource association. The listener therefore never reaches its request. ApiManagement demonstrates same-name registration overwrite; absence from the map is proven for every target, not an assertion that every absence has the same decorator cause.

**Decision:** Small rule change: enumerate existing registered createOrUpdate PUTs; validate before claiming new warnings. [Registered PUT traversal: evidence and tradeoff](../gap-analysis.md#registered-put-traversal).

**Raw observation IDs:** `PutRequestResponseSchemeArm:100`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).
