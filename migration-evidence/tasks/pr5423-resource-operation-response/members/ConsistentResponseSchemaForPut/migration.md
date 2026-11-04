# ConsistentResponseSchemaForPut migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` consolidates [`ConsistentResponseSchemaForPut`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-response-schema-for-put.md). **Not equivalent: the genuine plain 201 response mismatch is missed; the upstream object-identity bug should not be reproduced.**

## 2. Actual coverage

All 487 frozen projects succeeded, zero failed/unassessed. Reported diagnostics are individual findings. The TypeSpec column is now deterministically attributed to this member by exact operation and relevant comparison; it is not the entire shared 104-finding rule count.

| Count                                        | Swagger linter | TypeSpec linter |
| -------------------------------------------- | -------------- | --------------- |
| Reported findings (member / mapped TypeSpec) | 16             | 0               |
| Distinct checked targets (PUT operations)    | 16             | 0               |

0 shared-rule warnings occur on participating operations, but only 0 check the corresponding contract. Coincident messages receive no migration credit. See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ).

## 3. Function-level coverage

| Behavior                                              | Result                                                                               |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Different 200/201 bodies, including a nonresource 201 | Missing: Quota's genuine mismatch.                                                   |
| Identical 200/201 references                          | No TypeSpec warning; correctly avoids 15 upstream object-identity false positives.   |
| Compliant/violation controls                          | [Exact-candidate shared controls](../../evidence-details.md#controls-and-validation) |

## 4. Why diagnostic counts differ

| Original check group                                                                                    | Swagger raw | Distinct checks | Corresponding TypeSpec findings |
| ------------------------------------------------------------------------------------------------------- | ----------- | --------------- | ------------------------------- |
| [Upstream staging object-identity false positive](../../instances/p-7c23914bec5d.md#s-b303b55475326bb1) | 15          | 15              | 0                               |
| [Genuine plain-response 200/201 mismatch](../../instances/p-e87fcbcb098a.md#s-272fe9a097875b9c)         | 1           | 1               | 0                               |

Every target, original schema/reference, matching TypeSpec operation/model and diagnostic family is listed in the [per-project inventory](../../instance-correspondence.md#per-project-target-differences). The [shared TypeSpec accounting](../../instance-correspondence.md#typespec-finding-accounting) retains all 17 uncredited warnings. Zero means no corresponding finding was observed and the relevant predicate is absent/different, not that this member's operations are necessarily compliant.

## NOTES

Shared frozen inputs, configured source scope, selected Swagger-version policy and execution provenance are in the [group report](../../migration.md). The 59 affected projects' metadata-only recompilations exactly reproduced all 104 shared findings; all source/selected-version route bindings were unique and exact. No production linter changes or additional full corpus run were made.

[Original implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/consistent-response-schema-for-put.ts). Saved-data reconstruction: `python analyze-instances.py --root .` from the group directory.
