# ConsistentResponseSchemaForPut migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` is assessed against [`ConsistentResponseSchemaForPut`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-response-schema-for-put.md). **The observed genuine success-body difference is diagnosed. The TypeSpec linter intentionally avoids the Swagger linter's resolved-object-identity false positives; this is not bug-for-bug equivalence or universal structural-equivalence proof.**

## 2. Actual coverage

All 487 frozen projects succeeded; none failed or was unassessed. Reported diagnostics are individual findings. The TypeSpec raw total is the responsible rule's full output, shared with other members where applicable; it is not this member's credited coverage.

| Count                                                                       | Swagger linter | TypeSpec linter |
| --------------------------------------------------------------------------- | -------------- | --------------- |
| Reported diagnostics (member / responsible rule)                            | 16             | 248             |
| Affected project/routes (member / responsible rule, not equivalent defects) | 16             | 238             |

**Assessed coverage:** 1 of 16 original member-check contexts are diagnosed: 1 by corresponding configured warnings. Remaining: 15 confirmed Swagger false-positive contexts. 1 mapped context(s) also have captured owning diagnostics; coverage counts each once. Captured owning diagnostics receive credit despite suppression, without changing configured raw totals. Contexts are not equivalent-defect counts; universal violation percentages remain unassessed.

See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the decisions, including broader shared-rule checks.

## 3. Function-level coverage

| Behavior                                                       | Result                                  | Rationale                                                                                                                                                                                                                         |
| -------------------------------------------------------------- | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Actual body-bearing 200/201 responses for registered resources | Covered for observed genuine difference | Canonical consistency now inspects actual HTTP success bodies, including plain nonresource models; Quota also has an existing Azure Core diagnostic. [Evidence](../../gap-analysis.md#member-consistent-response-schema-for-put). |
| Equal success schemas; absent or explicit-void bodies          | Covered compliant behavior              | No resolved-object-identity comparison or spurious void/resource mismatch is introduced. [Evidence](../../gap-analysis.md#member-consistent-response-schema-for-put).                                                             |

## 4. Why diagnostic counts differ

`Raw / grouped` means reported Swagger diagnostics / distinct (member, project, resolved document, exact route, compared schema context) checks. The TypeSpec column counts only configured diagnostics attributed to that same comparison, not unrelated warnings on the route or callbacks hidden by authored suppression. Captured owning diagnostics are nevertheless credited in Assessed coverage and identified below.

| Difference (with evidence)                                                      | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | Recommended action and rationale                                                                                                                                                             |
| ------------------------------------------------------------------------------- | ----------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Confirmed Swagger false positive](../../gap-analysis.md#upstream-identity-bug) | 15 / 15                             | 0                                       | Confirmed resolved-object-identity bug; intentionally do not port its false positives.                                                                                                       |
| [Other responsible-rule checks](../../gap-analysis.md#typespec-only-checks)     | 0 / 0                               | 247                                     | 144 diagnose other members; 103 are additional/different policy or population checks. Keep their individual source/body/canonical dispositions separate; none receives this member's credit. |

## NOTES

Assessed source `3b0603ab8`; source-program versus latest-version Swagger, not universal version-aligned equivalence. The marker rule is opt-in in the shared ARM ruleset and explicitly activated for assessment; authored suppressions remain in configured raw totals. Owning-rule callbacks are counted separately without double-counting covered contexts.

[Pinned Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/consistent-response-schema-for-put.ts). [Shared provenance, controls, recovery and replay](../../evidence-details.md). [Exact targets](../../instance-correspondence.md).
