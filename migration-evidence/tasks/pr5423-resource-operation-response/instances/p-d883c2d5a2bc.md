# specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices

[All project differences](../instance-correspondence.md#differing-projects).

**Project totals:** Swagger 1 raw / 1 member checks; TypeSpec 0 raw; 0 findings credited to the same comparison. Common project/route unit: 1 Swagger / 0 TypeSpec. Counts repeated across different members at the same operation are non-additive.

<a id="s-147374c72a96fb47"></a>

### PutGetPatchResponseSchema: Computes_CreateOrUpdate

**Identity:** `147374c72a96fb47`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/computes/{computeName}`.
**Swagger document:** `projects/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices/swagger/preview/2026-09-15-preview/cognitiveservices.json`.
**Cause:** Cross-operation comparison includes an absent selected response reference.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation      | Request schema          | Success response schemas     |
| ------------------------------- | ----------------------- | ---------------------------- |
| `put` `Computes_CreateOrUpdate` | `#/definitions/Compute` | `202: (no schema)`           |
| `get` `Computes_Get`            | `(no schema)`           | `200: #/definitions/Compute` |

| TypeSpec operation                                                                                                                                                                                                                                                | Effective request                     | Canonical association / request checked                                       | Registered return candidates          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------- |
| [Microsoft.CognitiveServices.Computes.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices/Compute.tsp#L91) | `Microsoft.CognitiveServices.Compute` | `Microsoft.CognitiveServices.Compute: lifecycle.createOrUpdate; request=True` | `Microsoft.CognitiveServices.Compute` |
| [Microsoft.CognitiveServices.Computes.get](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices/Compute.tsp#L84)            | `(no single request)`                 | `Microsoft.CognitiveServices.Compute: lifecycle.read; request=False`          | `Microsoft.CognitiveServices.Compute` |

**Explanation:** The original picks the first existing 200/201/202 response and reads schema.$ref. It can obtain undefined for an empty response, an inline schema, or an operation without those statuses. The resource traversal does not compare this value across methods.

**Disposition:** TypeSpec rule update required for exact original-policy parity: add selected-status/body and inline-schema controls. A different intended policy requires explicit approval; no retirement is inferred.

**Raw observation IDs:** `PutGetPatchResponseSchema:6`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).
