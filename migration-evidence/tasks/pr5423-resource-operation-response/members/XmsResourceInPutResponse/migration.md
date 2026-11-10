# XmsResourceInPutResponse migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` is assessed against [`XmsResourceInPutResponse`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/xms-resource-in-put-response.md). **Not equivalent to extension-presence checking. TypeSpec resource declarations determine response identity, regardless of emission flags or OpenAPI overrides. PUTs omitted by resolveArmResources remain undiagnosed.**

## 2. Actual coverage

All 487 frozen projects succeeded; none failed or was unassessed. Counts are individual diagnostics, not projects. The TypeSpec total is the shared rule's full output across all four Swagger members, not this member's matched findings.

| Count                                                                 | Swagger linter | TypeSpec linter |
| --------------------------------------------------------------------- | -------------- | --------------- |
| Reported diagnostics (member / responsible rule)                      | 155            | 283             |
| Affected HTTP routes (grouped by project/route; member / shared rule) | 57             | 273             |

**Assessed coverage:** 38 of 57 original Swagger check contexts are diagnosed: 38 by corresponding configured diagnostics. Remaining: 9 intentional TypeSpec-resource/Swagger-marker differences; 10 checks missed because the resolver omits the PUT. Suppressed diagnostics count toward this assessment, not the configured raw total. Check contexts are not confirmed service defects; equivalent-defect coverage remains unassessed.

See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the decisions, including broader shared-rule checks.

## 3. Function-level coverage

| Behavior                                                     | Result                 | Rationale                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------ | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Resolver-exposed ARM PUT, body-bearing 200 then 201 fallback | Covered                | The existing enabled rule accepts registered resources, native resource-base ancestry and explicit custom declarations. Arrays, scalars and lookalike DTOs fail. A canonical response warning replaces, rather than duplicates, a resource-identity warning. [Evidence](../../gap-analysis.md#member-xms-resource-in-put-response). |
| Extension overrides and custom emission options              | Intentional difference | They neither create nor erase native resource identity. The linter does not inspect extensions or simulate emitted Swagger. [Evidence](../../gap-analysis.md#member-xms-resource-in-put-response).                                                                                                                                  |
| Absent/void body and non-PUT operations                      | Outside this check     | Body/status rules own absent bodies; the added resource-identity check applies only to PUT. [Evidence](../../gap-analysis.md#member-xms-resource-in-put-response).                                                                                                                                                                  |
| PUTs omitted by resolveArmResources                          | Missing                | Ten marked Network PUTs are absent from both resolver collections. Issue #5995 tracks the prerequisite; there is no fallback enumeration. [Evidence](../../gap-analysis.md#member-xms-resource-in-put-response).                                                                                                                    |

## 4. Why diagnostic counts differ

`Raw / grouped` means individual Swagger findings / distinct check contexts (Swagger member, project, resolved document, route and schema comparison). The TypeSpec column counts configured diagnostics attributed to that same check, not unrelated warnings on the route. Captured diagnostics before suppression are stated separately in the rationale and still count as diagnosed coverage. A diagnostic can cover several check contexts.

| Difference (with evidence)                                                                                            | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | Recommended action and rationale                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Native resource identity differs from emitted marker presence](../../gap-analysis.md#native-resource-representation) | 9 / 9                               | 0                                       | The selected body is a native resource. Marker/emission differences do not make it invalid; intentionally do not reproduce extension-level parity.                                           |
| [Marked PUTs on non-ARM targets are omitted by the resolver](../../gap-analysis.md#resolver-operation-gap)            | 108 / 10                            | 0                                       | Ten marked Network PUTs target models without ARM declarations. Reported in #5995; resolve the API/modeling prerequisite, not by fallback enumeration.                                       |
| [Other checks from the shared TypeSpec rule](../../gap-analysis.md#typespec-only-checks)                              | 0 / 0                               | 245                                     | 145 diagnose other members; 100 are additional/different policy or population checks. Keep their individual source/body/canonical dispositions separate; none receives this member's credit. |

## NOTES

Assessed source `779b3c409`. The TypeSpec linter is enabled in the shared ARM profile and explicitly selected for this comparison. Counts compare the source program with latest-version Swagger, not universally version-aligned defects. Each diagnosed check receives credit once, including captured diagnostics hidden by authored suppression.

[Pinned Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/with-xms-resource.ts). [Shared provenance, controls, recovery and replay](../../evidence-details.md). [Exact targets](../../instance-correspondence.md).
