# specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota

[All project differences](../instance-correspondence.md#differing-projects).

**Project totals:** Swagger 1 raw / 1 member checks; TypeSpec 0 raw; 0 findings credited to the same comparison. Common project/route unit: 1 Swagger / 0 TypeSpec. Counts repeated across different members at the same operation are non-additive.

<a id="s-272fe9a097875b9c"></a>

### ConsistentResponseSchemaForPut: Quota_CreateOrUpdate

**Identity:** `272fe9a097875b9c`; `/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/resourceProviders/{providerId}/locations/{location}/serviceLimits/{resourceName}`.
**Swagger document:** `projects/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/swagger/stable/2020-10-25/quota.json`.
**Cause:** Genuine plain-response 200/201 mismatch.

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

**Assessment:** Genuine schema difference with an existing native owner. **Recommendation:** P2: owner/suppression review.

**Disposition / tradeoff:** Quota deliberately models a quota resource at 200 and a submission-status envelope at 201. Azure Core response-schema-problem already compares non-error success payload identities; the source explicitly suppresses it. Use that owner and review the legacy-contract exception instead of adding a duplicate ARM warning. The final LRO result is separately modeled as the quota resource; initial-envelope and final-result policies are different. [Decision evidence and alternatives](../gap-analysis.md).

**Raw observation IDs:** `ConsistentResponseSchemaForPut:8`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).
