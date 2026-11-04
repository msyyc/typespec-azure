# specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota

[All project differences](../instance-correspondence.md#differing-projects).

**Project totals:** Swagger 1 raw / 1 member checks; TypeSpec 0 raw; 0 findings credited to the same comparison. Common project/route unit: 1 Swagger / 0 TypeSpec. Counts repeated across different members at the same operation are non-additive. TypeSpec counts refer only to arm-resource-operation-response, not the entire linter suite.

<a id="s-272fe9a097875b9c"></a>

### ConsistentResponseSchemaForPut: Quota_CreateOrUpdate

**Identity:** `272fe9a097875b9c`; `/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/resourceProviders/{providerId}/locations/{location}/serviceLimits/{resourceName}`.
**Swagger document:** `projects/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/swagger/stable/2020-10-25/quota.json`.
**Observed comparison:** Genuine plain-response 200/201 mismatch.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation   | Request schema                        | Success response schemas                                                                     |
| ---------------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------- |
| `put` `Quota_CreateOrUpdate` | `#/definitions/CurrentQuotaLimitBase` | `200: #/definitions/CurrentQuotaLimitBase; 201: #/definitions/QuotaRequestSubmitResponse201` |

| TypeSpec operation                                                                                                                                                                                                                                         | Effective request             | Canonical association / request checked                               | Registered return candidates  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | --------------------------------------------------------------------- | ----------------------------- |
| [Quota.CurrentQuotaLimitBases.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/CurrentQuotaLimitBase.tsp#L71) | `Quota.CurrentQuotaLimitBase` | `Quota.CurrentQuotaLimitBase: lifecycle.createOrUpdate; request=True` | `Quota.CurrentQuotaLimitBase` |

**Explanation:** Quota returns CurrentQuotaLimitBase for 200 and QuotaRequestSubmitResponse201 for 201. Only the canonical registered resource is a response candidate; the plain nonresource 201 body is ignored.

**Decision:** Review the existing Azure Core rule's suppression/legacy exception; do not duplicate it in ARM. [Quota success-schema difference: evidence and tradeoff](../gap-analysis.md#existing-policy-exceptions).

**Raw observation IDs:** `ConsistentResponseSchemaForPut:8`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).
