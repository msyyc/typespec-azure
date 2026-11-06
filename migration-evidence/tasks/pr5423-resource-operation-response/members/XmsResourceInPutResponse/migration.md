# XmsResourceInPutResponse migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` is assessed against [`XmsResourceInPutResponse`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/xms-resource-in-put-response.md). **Native resource-response validation, not extension parity. Declared resources remain resources despite emission flags or OpenAPI overrides. Exact native violations, intentional representation differences and resolver/authoring residuals are accounted for separately.**

## 2. Actual coverage

All 487 frozen projects succeeded; none failed or was unassessed. Reported diagnostics are individual findings. The TypeSpec raw total is the responsible rule's full output, shared with other members where applicable; it is not this member's credited coverage.

| Count                                                                       | Swagger linter | TypeSpec linter |
| --------------------------------------------------------------------------- | -------------- | --------------- |
| Reported diagnostics (member / responsible rule)                            | 155            | 283             |
| Affected project/routes (member / responsible rule, not equivalent defects) | 57             | 273             |

**Assessed coverage:** 38 of 57 original member-check contexts are diagnosed: 38 by corresponding configured warnings. Remaining: 9 intentional native-resource/serialized-marker differences; 10 resolver-enumeration gaps. Captured selected-rule and owning diagnostics count despite suppression; configured raw totals are unchanged. Contexts are not equivalent-defect counts; universal violation percentages remain unassessed.

See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the decisions, including broader shared-rule checks.

## 3. Function-level coverage

| Behavior                                                     | Result                              | Rationale                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------ | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Resolver-exposed ARM PUT, body-bearing 200 then 201 fallback | Native resource policy              | The existing enabled rule accepts registered resources, native resource-base ancestry and explicit custom declarations. Arrays, scalars and lookalike DTOs fail. A canonical response warning replaces, rather than duplicates, a resource-identity warning. [Evidence](../../gap-analysis.md#member-xms-resource-in-put-response). |
| Extension overrides and custom emission options              | Intentional difference              | They neither create nor erase native resource identity. The linter does not inspect extensions or simulate emitted Swagger. [Evidence](../../gap-analysis.md#member-xms-resource-in-put-response).                                                                                                                                  |
| Absent/void body, non-PUT and resolver omissions             | Separate owners / explicit boundary | Body/status rules own absent bodies. Added PUT enumeration uses only resolveArmResources; unsupported authoring and API omissions are reported, not bypassed. [Evidence](../../gap-analysis.md#member-xms-resource-in-put-response).                                                                                                |

## 4. Why diagnostic counts differ

`Raw / grouped` means reported Swagger diagnostics / distinct (member, project, resolved document, exact route, compared schema context) checks. The TypeSpec column is configured / captured-before-suppression diagnostics for the same check, including responsible existing owners. Suppression does not remove diagnostic coverage. Callbacks can cover several member contexts, so these rows are not additive defect counts.

| Difference (with evidence)                                                                                            | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics (configured / before suppression) | Decision and rationale                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Native resource identity differs from emitted marker presence](../../gap-analysis.md#native-resource-representation) | 9 / 9                               | 0 / 0                                                  | The selected body is a native resource. Marker/emission differences do not make it invalid; intentionally do not reproduce extension-level parity.                                           |
| [Marked PUTs on non-ARM targets are omitted by the resolver](../../gap-analysis.md#resolver-operation-gap)            | 108 / 10                            | 0 / 0                                                  | Ten marked Network PUTs target models without ARM declarations. Reported in #5995; resolve the API/modeling prerequisite, not by fallback enumeration.                                       |
| [Other responsible-rule checks](../../gap-analysis.md#typespec-only-checks)                                           | 0 / 0                               | 245 configured                                         | 145 diagnose other members; 100 are additional/different policy or population checks. Keep their individual source/body/canonical dispositions separate; none receives this member's credit. |

## NOTES

Assessed source `779b3c409`; source-program versus latest-version Swagger, not universal version-aligned equivalence. The existing response rule is enabled in the shared ARM profile; its expanded native PUT guidance is intentionally enabled too. The worker explicitly enables the selected rule for comparison. Authored suppressions affect reported totals, not assessed diagnostic coverage; selected-rule and owning callbacks are credited without double-counting contexts.

[Pinned Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/with-xms-resource.ts). [Shared provenance, controls, recovery and replay](../../evidence-details.md). [Exact targets](../../instance-correspondence.md).
