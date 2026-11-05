# XmsResourceInPutResponse migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-put-response-resource` is assessed against [`XmsResourceInPutResponse`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/xms-resource-in-put-response.md). **Complete observed correspondence for the selected PUT response-marker checks. This policy diagnoses missing resource markers, not proven service defects; custom/action contracts still need owner decisions. Source versus latest-version comparison does not establish universal equivalence.**

## 2. Actual coverage

All 487 frozen projects succeeded; none failed or was unassessed. Reported diagnostics are individual findings. The TypeSpec raw total is the responsible rule's full output, shared with other members where applicable; it is not this member's credited coverage.

| Count                                                                       | Swagger linter | TypeSpec linter |
| --------------------------------------------------------------------------- | -------------- | --------------- |
| Reported diagnostics (member / responsible rule)                            | 155            | 57              |
| Affected project/routes (member / responsible rule, not equivalent defects) | 57             | 57              |

**Assessed coverage:** 57 of 57 original member-check contexts are diagnosed: 57 by corresponding configured warnings. Captured owning diagnostics receive credit despite suppression, without changing configured raw totals. Contexts are not equivalent-defect counts; universal violation percentages remain unassessed.

See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the decisions, including broader shared-rule checks.

## 3. Function-level coverage

| Behavior                                                | Result                           | Rationale                                                                                                                                                                                                                      |
| ------------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| PUT response marker, 200 then body-bearing 201 fallback | Observed correspondence complete | Dedicated opt-in rule checks selected actual response metadata independently of canonical registration, including inherited/explicit extension markers. [Evidence](../../gap-analysis.md#member-xms-resource-in-put-response). |
| Absent/void body, non-PUT and marked response           | Covered compliant behavior       | No body is not a missing marker; explicit void is skipped. Custom payloads can opt out only through explicit configuration/suppression. [Evidence](../../gap-analysis.md#member-xms-resource-in-put-response).                 |

## 4. Why diagnostic counts differ

`Raw / grouped` means reported Swagger diagnostics / distinct (member, project, resolved document, exact route, compared schema context) checks. The TypeSpec column counts only configured diagnostics attributed to that same comparison, not unrelated warnings on the route or callbacks hidden by authored suppression. Captured owning diagnostics are nevertheless credited in Assessed coverage and identified below.

| Difference (with evidence)                                                                        | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | Recommended action and rationale                                                                                                 |
| ------------------------------------------------------------------------------------------------- | ----------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| [Repeated reference invocations: put-resource-marker](../../gap-analysis.md#repeated-invocations) | 108 / 10                            | 10                                      | Count-only difference: preserve all invocations, but compare each exact member/schema context once. No production fix is needed. |

## NOTES

Assessed source `3b0603ab8`; source-program versus latest-version Swagger, not universal version-aligned equivalence. The marker rule is opt-in in the shared ARM ruleset and explicitly activated for assessment; authored suppressions remain in configured raw totals. Owning-rule callbacks are counted separately without double-counting covered contexts.

[Pinned Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/with-xms-resource.ts). [Shared provenance, controls, recovery and replay](../../evidence-details.md). [Exact targets](../../instance-correspondence.md).
