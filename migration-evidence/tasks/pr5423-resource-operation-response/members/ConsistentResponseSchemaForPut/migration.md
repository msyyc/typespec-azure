# ConsistentResponseSchemaForPut migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` is assessed against [`ConsistentResponseSchemaForPut`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-response-schema-for-put.md). **The observed genuine success-body difference is diagnosed. The TypeSpec linter intentionally avoids the Swagger linter bug that compares resolved objects by identity and reports identical 200/201 schema references as different. This establishes coverage of the observed valid check, not universal structural equivalence.**

## 2. Actual coverage

All 487 frozen projects succeeded; none failed or was unassessed. Counts are individual diagnostics, not projects. The TypeSpec total is the shared rule's full output across all four Swagger members, not this member's matched findings.

| Count                                                                 | Swagger linter | TypeSpec linter |
| --------------------------------------------------------------------- | -------------- | --------------- |
| Reported diagnostics (member / responsible rule)                      | 16             | 283             |
| Affected HTTP routes (grouped by project/route; member / shared rule) | 16             | 273             |

**Assessed coverage:** 1 of 16 original Swagger check contexts is diagnosed: 1 by corresponding configured diagnostics. Remaining: 15 confirmed Swagger linter false positives. Suppressed diagnostics count toward this assessment, not the configured raw total. Check contexts are not confirmed service defects; equivalent-defect coverage remains unassessed.

See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the decisions, including broader shared-rule checks.

## 3. Function-level coverage

| Behavior                                                       | Result                                  | Rationale                                                                                                                                                                                                                         |
| -------------------------------------------------------------- | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Actual body-bearing 200/201 responses for registered resources | Covered for observed genuine difference | Canonical consistency now inspects actual HTTP success bodies, including plain nonresource models; Quota also has an existing Azure Core diagnostic. [Evidence](../../gap-analysis.md#member-consistent-response-schema-for-put). |
| Equal success schemas; absent or explicit-void bodies          | Covered / scoped exemptions             | Equal schemas do not get an object-identity false positive. This check skips absent/void bodies; separate response-body/status rules still apply. [Evidence](../../gap-analysis.md#member-consistent-response-schema-for-put).    |

## 4. Why diagnostic counts differ

`Raw / grouped` means individual Swagger findings / distinct check contexts (Swagger member, project, resolved document, route and schema comparison). The TypeSpec column counts configured diagnostics attributed to that same check, not unrelated warnings on the route. Captured diagnostics before suppression are stated separately in the rationale and still count as diagnosed coverage. A diagnostic can cover several check contexts.

| Difference (with evidence)                                                               | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | Recommended action and rationale                                                                                                                                                             |
| ---------------------------------------------------------------------------------------- | ----------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Confirmed Swagger false positive](../../gap-analysis.md#upstream-identity-bug)          | 15 / 15                             | 0                                       | Confirmed resolved-object-identity bug; intentionally do not port its false positives.                                                                                                       |
| [Other checks from the shared TypeSpec rule](../../gap-analysis.md#typespec-only-checks) | 0 / 0                               | 282                                     | 182 diagnose other members; 100 are additional/different policy or population checks. Keep their individual source/body/canonical dispositions separate; none receives this member's credit. |

## NOTES

Assessed source `779b3c409`. The TypeSpec linter is enabled in the shared ARM profile and explicitly selected for this comparison. Counts compare the source program with latest-version Swagger, not universally version-aligned defects. Each diagnosed check receives credit once, including captured diagnostics hidden by authored suppression.

[Pinned Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/consistent-response-schema-for-put.ts). [Shared provenance, controls, recovery and replay](../../evidence-details.md). [Exact targets](../../instance-correspondence.md).
