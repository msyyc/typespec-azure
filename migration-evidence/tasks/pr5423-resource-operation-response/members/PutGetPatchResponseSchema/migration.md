# PutGetPatchResponseSchema migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` consolidates [`PutGetPatchResponseSchema`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-get-patch-response-schema.md). **Not equivalent: registered-resource return traversal does not implement the original status-specific response-reference comparison.**

## 2. Actual coverage

All 487 frozen projects succeeded, zero failed/unassessed. Reported diagnostics are individual findings. The TypeSpec column is now deterministically attributed to this member by exact operation and relevant comparison; it is not the entire shared 104-finding rule count.

| Count                                        | Swagger linter | TypeSpec linter |
| -------------------------------------------- | -------------- | --------------- |
| Reported findings (member / mapped TypeSpec) | 50             | 0               |
| Distinct checked targets (route comparisons) | 36             | 0               |

7 shared-rule warnings occur on participating operations, but only 0 check the corresponding contract. Coincident messages receive no migration credit. See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ).

## 3. Function-level coverage

| Behavior                                            | Result                                                                                                                                                                                                                               |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| First selected 200/201/202 has no $ref              | 33 route comparisons are not reproduced by canonical resource traversal.                                                                                                                                                             |
| Selected references differ, including list wrappers | Three route comparisons are not reproduced; wrapper names and list-item identity differ.                                                                                                                                             |
| Registered-resource return identity                 | Retained narrower check; zero response-family findings in this corpus.                                                                                                                                                               |
| Decision-relevant partition                         | 15 correctly bodyless comparisons; four matching collection-item comparisons; 16 empty-200 body-policy cases; one genuine SyncJob shape difference. The existing body-owner predicate diagnoses all 16 before authored suppressions. |
| Compliant/violation controls                        | [Exact-candidate shared controls](../../evidence-details.md#controls-and-validation)                                                                                                                                                 |

## 4. Why diagnostic counts differ

| Original check group                                                                                                              | Swagger raw | Distinct checks | Corresponding TypeSpec findings |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------- | ------------------------------- |
| [Cross-operation comparison includes an absent selected response reference](../../instances/p-6e7cc89a7ebd.md#s-e7a795042777d9cf) | 47          | 33              | 0                               |
| [Cross-operation comparison has distinct selected references](../../instances/p-49581f50dce3.md#s-e3d27963b9f80e88)               | 3           | 3               | 0                               |

### Assessed decisions

These recommendations classify every member check without adding correspondence credit or predicting post-fix warning counts.

| Decision / next action                                                                       | Member checks | Priority                                      |
| -------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------- |
| [Empty 200: real response-body issue, not two unequal payload models](../../gap-analysis.md) | 16            | P2: existing owner/spec fix                   |
| [Swagger schema-comparison false positive / policy overreach](../../gap-analysis.md)         | 15            | Recommend not porting                         |
| [Swagger collection-shape comparison false positive](../../gap-analysis.md)                  | 4             | Recommend not porting                         |
| [Genuine PUT/GET resource-shape difference](../../gap-analysis.md)                           | 1             | P3: spec-owner follow-up; defer broad matcher |

Every target, original schema/reference, matching TypeSpec operation/model and diagnostic family is listed in the [per-project inventory](../../instance-correspondence.md#per-project-target-differences). The [shared TypeSpec accounting](../../instance-correspondence.md#typespec-finding-accounting) retains all 17 uncredited warnings. Zero means no corresponding finding was observed and the relevant predicate is absent/different, not that this member's operations are necessarily compliant. The [decision/tradeoff analysis](../../gap-analysis.md) and [per-check dispositions](../../gap-assessment.json) separate false positives, existing suppressed owners and worthwhile functional gaps; unpaired totals are not required new warnings.

## NOTES

Shared frozen inputs, configured source scope, selected Swagger-version policy and execution provenance are in the [group report](../../migration.md). The 59 affected projects' metadata-only recompilations exactly reproduced all 104 shared findings; all source/selected-version route bindings were unique and exact. No production linter changes or additional full corpus run were made.

[Original implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/put-get-patch-schema.ts). Saved-data reconstruction: `python analyze-instances.py --root .` from the group directory.
