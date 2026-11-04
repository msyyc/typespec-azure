# specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace

[All project differences](../instance-correspondence.md#differing-projects).

**Project totals:** Swagger 2 raw / 2 member checks; TypeSpec 0 raw; 0 findings credited to the same comparison. Common project/route unit: 1 Swagger / 0 TypeSpec. Counts repeated across different members at the same operation are non-additive. TypeSpec counts refer only to arm-resource-operation-response, not the entire linter suite.

<a id="s-dcb16038cea11cc9"></a>

### PutGetPatchResponseSchema: PrivateStore_CreateOrUpdate

**Identity:** `dcb16038cea11cc9`; `/providers/Microsoft.Marketplace/privateStores/{privateStoreId}`.
**Swagger document:** `projects/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/swagger/stable/2025-01-01/Marketplace.json`.
**Observed comparison:** Cross-operation comparison includes an absent selected response reference.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation          | Request schema               | Success response schemas          |
| ----------------------------------- | ---------------------------- | --------------------------------- |
| `put` `PrivateStore_CreateOrUpdate` | `#/definitions/PrivateStore` | `200: (no schema)`                |
| `get` `PrivateStore_Get`            | `(no schema)`                | `200: #/definitions/PrivateStore` |

| TypeSpec operation                                                                                                                                                                                                                                  | Effective request                    | Canonical association / request checked                                      | Registered return candidates         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------- | ------------------------------------ |
| [Microsoft.Marketplace.PrivateStores.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/PrivateStore.tsp#L43) | `Microsoft.Marketplace.PrivateStore` | `Microsoft.Marketplace.PrivateStore: lifecycle.createOrUpdate; request=True` | `(none)`                             |
| [Microsoft.Marketplace.PrivateStores.get](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/PrivateStore.tsp#L32)            | `(no single request)`                | `Microsoft.Marketplace.PrivateStore: lifecycle.read; request=False`          | `Microsoft.Marketplace.PrivateStore` |

**Explanation:** The original picks the first existing 200/201/202 response and reads schema.$ref. It can obtain undefined for an empty response, an inline schema, or an operation without those statuses. The resource traversal does not compare this value across methods.

**Decision:** Review existing no-response-body suppressions/specs; do not duplicate that check. [Empty 200 responses: evidence and tradeoff](../gap-analysis.md#existing-policy-exceptions).

**Raw observation IDs:** `PutGetPatchResponseSchema:18`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-e6c42278fc611fee"></a>

### PutRequestResponseSchemeArm: PrivateStore_CreateOrUpdate

**Identity:** `e6c42278fc611fee`; `/providers/Microsoft.Marketplace/privateStores/{privateStoreId}`.
**Swagger document:** `projects/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/swagger/stable/2025-01-01/Marketplace.json`.
**Observed comparison:** Canonical request is accepted while selected 200 has no schema.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation          | Request schema               | Success response schemas |
| ----------------------------------- | ---------------------------- | ------------------------ |
| `put` `PrivateStore_CreateOrUpdate` | `#/definitions/PrivateStore` | `200: (no schema)`       |

| TypeSpec operation                                                                                                                                                                                                                                  | Effective request                    | Canonical association / request checked                                      | Registered return candidates |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------- | ---------------------------- |
| [Microsoft.Marketplace.PrivateStores.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/PrivateStore.tsp#L43) | `Microsoft.Marketplace.PrivateStore` | `Microsoft.Marketplace.PrivateStore: lifecycle.createOrUpdate; request=True` | `(none)`                     |

**Explanation:** The request is exactly the registered resource, so TypeSpec accepts it. The original chooses the existing 200 response even without a schema, then compares the request against an empty schema instead of falling back to 201.

**Decision:** Review existing no-response-body suppressions/specs; do not duplicate that check. [Empty 200 responses: evidence and tradeoff](../gap-analysis.md#existing-policy-exceptions).

**Raw observation IDs:** `PutRequestResponseSchemeArm:109`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).
