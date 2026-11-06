# PutGetPatchResponseSchema migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` is assessed against [`PutGetPatchResponseSchema`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-get-patch-response-schema.md). **Not equivalent. Existing response-body diagnostics cover empty 200 responses, but SyncJob's PUT/GET shape difference is not covered by its wrong-parent read registration. No-content and same-item collection comparisons are recommended exclusions, not approved retirements.**

## 2. Actual coverage

All 487 frozen projects succeeded; none failed or was unassessed. Reported diagnostics are individual findings. The TypeSpec raw total is the responsible rule's full output, shared with other members where applicable; it is not this member's credited coverage.

| Count                                                                       | Swagger linter | TypeSpec linter |
| --------------------------------------------------------------------------- | -------------- | --------------- |
| Reported diagnostics (member / responsible rule)                            | 50             | 283             |
| Affected project/routes (member / responsible rule, not equivalent defects) | 36             | 273             |

**Assessed coverage:** 16 of 36 original member-check contexts are diagnosed: 16 additional contexts by captured owning diagnostics before authored suppression. Remaining: 19 recommended comparison exclusions awaiting approval; 1 unresolved/modeling or deferred contract contexts. Captured selected-rule and owning diagnostics count despite suppression; configured raw totals are unchanged. Contexts are not equivalent-defect counts; universal violation percentages remain unassessed.

See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the decisions, including broader shared-rule checks.

## 3. Function-level coverage

| Behavior                                                     | Result                                 | Rationale                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------ | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Registered lifecycle actual success responses and list items | Covered canonical-resource policy      | Read/create/update/list aliases are traversed. Per-response arrays/value envelopes are extracted for list associations, and discriminated response ancestry is preserved. [Evidence](../../gap-analysis.md#member-put-get-patch-response-schema).                             |
| Empty 200 compared with a resource                           | Covered by existing owning diagnostics | Captured no-response-body callbacks remain diagnostic evidence despite authored suppression; schema equality must not replace body-existence policy. [Evidence](../../gap-analysis.md#member-put-get-patch-response-schema).                                                  |
| No-content / same-item collection roles                      | Recommended intentional difference     | Comparing absent schemas or wrapper names does not establish a different resource item. Exclusions remain recommendations awaiting approval. [Evidence](../../gap-analysis.md#member-put-get-patch-response-schema).                                                          |
| SyncJob PUT/GET shape difference                             | Missing / deferred                     | The borrowed SourceControl read association diagnoses another comparison. Confirm owner intent before sharing models; one route does not justify a recursive version/visibility-aware schema matcher. [Evidence](../../gap-analysis.md#member-put-get-patch-response-schema). |

## 4. Why diagnostic counts differ

`Raw / grouped` means reported Swagger diagnostics / distinct (member, project, resolved document, exact route, compared schema context) checks. The TypeSpec column is configured / captured-before-suppression diagnostics for the same check, including responsible existing owners. Suppression does not remove diagnostic coverage. Callbacks can cover several member contexts, so these rows are not additive defect counts.

| Difference (with evidence)                                                                                         | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics (configured / before suppression) | Decision and rationale                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Empty 200: real response-body issue, not two unequal payload models](../../gap-analysis.md#body-policy-owner)     | 30 / 16                             | 0 / 16                                                 | Covered by 16 captured owning diagnostic callbacks over 16 contexts before suppression. Diagnosed by the existing body owner before suppression; review the suppression/wire contract, not duplicate schema equality. |
| [Swagger schema-comparison false positive / policy overreach](../../gap-analysis.md#bodyless-comparator-overreach) | 15 / 15                             | 0 / 0                                                  | Recommend excluding absent-body comparisons, not inventing bodies. Status-code compliance is a separate policy; approval is pending.                                                                                  |
| [Swagger collection-shape comparison false positive](../../gap-analysis.md#collection-comparator-overreach)        | 4 / 4                               | 0 / 0                                                  | Recommend excluding wrapper-versus-item reference equality: actual resource items agree. Approval is pending.                                                                                                         |
| [Genuine PUT/GET resource-shape difference](../../gap-analysis.md#cross-method-entity-contract)                    | 1 / 1                               | 0 / 0                                                  | Genuine uncovered contract difference. Confirm service intent before sharing models; defer a broad structural matcher.                                                                                                |
| [Other responsible-rule checks](../../gap-analysis.md#typespec-only-checks)                                        | 0 / 0                               | 283 configured                                         | 183 diagnose other members; 100 are additional/different policy or population checks. Keep their individual source/body/canonical dispositions separate; none receives this member's credit.                          |

## NOTES

Assessed source `779b3c409`; source-program versus latest-version Swagger, not universal version-aligned equivalence. The existing response rule is enabled in the shared ARM profile; its expanded native PUT guidance is intentionally enabled too. The worker explicitly enables the selected rule for comparison. Authored suppressions affect reported totals, not assessed diagnostic coverage; selected-rule and owning callbacks are credited without double-counting contexts.

[Pinned Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/put-get-patch-schema.ts). [Shared provenance, controls, recovery and replay](../../evidence-details.md). [Exact targets](../../instance-correspondence.md).
