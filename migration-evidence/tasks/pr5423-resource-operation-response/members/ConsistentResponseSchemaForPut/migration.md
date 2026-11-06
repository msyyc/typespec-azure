# ConsistentResponseSchemaForPut migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` is assessed against [`ConsistentResponseSchemaForPut`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-response-schema-for-put.md). **The observed genuine success-body difference is diagnosed. The TypeSpec linter intentionally avoids the Swagger linter's resolved-object-identity false positives; this is not bug-for-bug equivalence or universal structural-equivalence proof.**

## 2. Actual coverage

All 487 frozen projects succeeded; none failed or was unassessed. Reported diagnostics are individual findings. The TypeSpec raw total is the responsible rule's full output, shared with other members where applicable; it is not this member's credited coverage.

| Count                                                                       | Swagger linter | TypeSpec linter |
| --------------------------------------------------------------------------- | -------------- | --------------- |
| Reported diagnostics (member / responsible rule)                            | 16             | 283             |
| Affected project/routes (member / responsible rule, not equivalent defects) | 16             | 273             |

**Assessed coverage:** 1 of 16 original member-check contexts are diagnosed: 1 by corresponding configured warnings. Remaining: 15 confirmed Swagger false-positive contexts. 1 mapped context(s) also have captured owning diagnostics; coverage counts each once. Captured selected-rule and owning diagnostics count despite suppression; configured raw totals are unchanged. Contexts are not equivalent-defect counts; universal violation percentages remain unassessed.

See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the decisions, including broader shared-rule checks.

## 3. Function-level coverage

| Behavior                                                       | Result                                  | Rationale                                                                                                                                                                                                                         |
| -------------------------------------------------------------- | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Actual body-bearing 200/201 responses for registered resources | Covered for observed genuine difference | Canonical consistency now inspects actual HTTP success bodies, including plain nonresource models; Quota also has an existing Azure Core diagnostic. [Evidence](../../gap-analysis.md#member-consistent-response-schema-for-put). |
| Equal success schemas; absent or explicit-void bodies          | Covered compliant behavior              | No resolved-object-identity comparison or spurious void/resource mismatch is introduced. [Evidence](../../gap-analysis.md#member-consistent-response-schema-for-put).                                                             |

## 4. Why diagnostic counts differ

`Raw / grouped` means reported Swagger diagnostics / distinct (member, project, resolved document, exact route, compared schema context) checks. The TypeSpec column is configured / captured-before-suppression diagnostics for the same check, including responsible existing owners. Suppression does not remove diagnostic coverage. Callbacks can cover several member contexts, so these rows are not additive defect counts.

| Difference (with evidence)                                                      | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics (configured / before suppression) | Decision and rationale                                                                                                                                                                       |
| ------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Confirmed Swagger false positive](../../gap-analysis.md#upstream-identity-bug) | 15 / 15                             | 0 / 0                                                  | Confirmed resolved-object-identity bug; intentionally do not port its false positives.                                                                                                       |
| [Other responsible-rule checks](../../gap-analysis.md#typespec-only-checks)     | 0 / 0                               | 282 configured                                         | 182 diagnose other members; 100 are additional/different policy or population checks. Keep their individual source/body/canonical dispositions separate; none receives this member's credit. |

## NOTES

Assessed source `779b3c409`; source-program versus latest-version Swagger, not universal version-aligned equivalence. The existing response rule is enabled in the shared ARM profile; its expanded native PUT guidance is intentionally enabled too. The worker explicitly enables the selected rule for comparison. Authored suppressions affect reported totals, not assessed diagnostic coverage; selected-rule and owning callbacks are credited without double-counting contexts.

[Pinned Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/consistent-response-schema-for-put.ts). [Shared provenance, controls, recovery and replay](../../evidence-details.md). [Exact targets](../../instance-correspondence.md).
