# specification/portal/resource-manager/Microsoft.Portal/Portal

[All project differences](../instance-correspondence.md#differing-projects).

**Project totals:** Swagger 2 raw / 2 member checks; TypeSpec 0 raw; 0 findings credited to the same comparison. Common project/route unit: 2 Swagger / 0 TypeSpec. Counts repeated across different members at the same operation are non-additive.

<a id="s-84a4cb24142840d5"></a>

### ConsistentResponseSchemaForPut: TenantConfigurations_Create

**Identity:** `84a4cb24142840d5`; `/providers/Microsoft.Portal/tenantConfigurations/{configurationName}`.
**Swagger document:** `projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/tenantConfiguration.json`.
**Cause:** Upstream staging object-identity false positive.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation          | Request schema                             | Success response schemas                                                                       |
| ----------------------------------- | ------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| `put` `TenantConfigurations_Create` | `./common.json#/definitions/Configuration` | `200: ./common.json#/definitions/Configuration; 201: ./common.json#/definitions/Configuration` |

| TypeSpec operation                                                                                                                                                                                                                    | Effective request                | Canonical association / request checked                                  | Registered return candidates     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------ | -------------------------------- |
| [Microsoft.Portal.TenantConfigurations.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/portal/resource-manager/Microsoft.Portal/Portal/TenantConfiguration.tsp#L48) | `Microsoft.Portal.Configuration` | `Microsoft.Portal.Configuration: lifecycle.createOrUpdate; request=True` | `Microsoft.Portal.Configuration` |

**Explanation:** Raw 200 and 201 references are identical in the same invoking document. The original uses !== on resolved JavaScript objects, not structural equality. This classification uses saved references and pinned code, not a newly captured resolver-object execution trace.

**Assessment:** Confirmed Swagger false positive. **Recommendation:** Do not port.

**Disposition / tradeoff:** Identical 200/201 references were compared by resolved JavaScript object identity. Do not reproduce this bug or count its absence as a missing useful diagnostic. [Decision evidence and alternatives](../gap-analysis.md).

**Raw observation IDs:** `ConsistentResponseSchemaForPut:5`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-20e9f2df566de610"></a>

### ConsistentResponseSchemaForPut: Dashboards_CreateOrUpdate

**Identity:** `20e9f2df566de610`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName}`.
**Swagger document:** `projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/portal.json`.
**Cause:** Upstream staging object-identity false positive.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation        | Request schema                         | Success response schemas                                                               |
| --------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------- |
| `put` `Dashboards_CreateOrUpdate` | `./common.json#/definitions/Dashboard` | `200: ./common.json#/definitions/Dashboard; 201: ./common.json#/definitions/Dashboard` |

| TypeSpec operation                                                                                                                                                                                                        | Effective request            | Canonical association / request checked                              | Registered return candidates |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | -------------------------------------------------------------------- | ---------------------------- |
| [Microsoft.Portal.Dashboards.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/portal/resource-manager/Microsoft.Portal/Portal/Dashboard.tsp#L35) | `Microsoft.Portal.Dashboard` | `Microsoft.Portal.Dashboard: lifecycle.createOrUpdate; request=True` | `Microsoft.Portal.Dashboard` |

**Explanation:** Raw 200 and 201 references are identical in the same invoking document. The original uses !== on resolved JavaScript objects, not structural equality. This classification uses saved references and pinned code, not a newly captured resolver-object execution trace.

**Assessment:** Confirmed Swagger false positive. **Recommendation:** Do not port.

**Disposition / tradeoff:** Identical 200/201 references were compared by resolved JavaScript object identity. Do not reproduce this bug or count its absence as a missing useful diagnostic. [Decision evidence and alternatives](../gap-analysis.md).

**Raw observation IDs:** `ConsistentResponseSchemaForPut:4`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).
