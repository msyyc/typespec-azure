# PutRequestResponseSchemeArm migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` consolidates [`PutRequestResponseSchemeArm`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-request-response-scheme-arm.md). **Not equivalent: only a subset of the original request/selected-response comparisons is covered.**

## 2. Actual coverage

All 487 frozen projects succeeded, zero failed/unassessed. Reported diagnostics are individual findings. The TypeSpec column is now deterministically attributed to this member by exact operation and relevant comparison; it is not the entire shared 104-finding rule count.

| Count                                        | Swagger linter | TypeSpec linter |
| -------------------------------------------- | -------------- | --------------- |
| Reported findings (member / mapped TypeSpec) | 212            | 87              |
| Distinct checked targets (PUT operations)    | 168            | 87              |

92 shared-rule warnings occur on participating operations, but only 87 check the corresponding contract. Coincident messages receive no migration credit. See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ).

## 3. Function-level coverage

| Behavior                                                          | Result                                                                                        |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Registered lifecycle request versus canonical selected response   | 87 corroborated instances; structural equality and source identity remain different policies. |
| PUT stored under lists / absent from the retained map             | Missing: 39 list-map operations and 35 unassociated operations.                               |
| Actual selected response/status differs from canonical comparison | Five coincident warnings and two accepted canonical requests are not equivalent checks.       |
| Compliant/violation controls                                      | [Exact-candidate shared controls](../../evidence-details.md#controls-and-validation)          |

## 4. Why diagnostic counts differ

| Original check group                                                                                                    | Swagger raw | Distinct checks | Corresponding TypeSpec findings |
| ----------------------------------------------------------------------------------------------------------------------- | ----------- | --------------- | ------------------------------- |
| [Registered response, but PUT absent from retained operation map](../../instances/p-6e7cc89a7ebd.md#s-d6c6d92c9a0f4dc9) | 23          | 23              | 0                               |
| [PUT stored under lists rather than lifecycle.createOrUpdate](../../instances/p-6e7cc89a7ebd.md#s-a0043bfa2f35690b)     | 39          | 39              | 0                               |
| [Warning on the same operation compares a different contract](../../instances/p-6e7cc89a7ebd.md#s-9eca5628f4dd299e)     | 5           | 5               | 0                               |
| [Unassociated PUT with no registered response model](../../instances/p-560dd8313baf.md#s-43582b9e61743914)              | 56          | 12              | 0                               |
| [Canonical request is accepted while selected 200 has no schema](../../instances/p-f43db0dc1fd6.md#s-e6c42278fc611fee)  | 2           | 2               | 0                               |

Every target, original schema/reference, matching TypeSpec operation/model and diagnostic family is listed in the [per-project inventory](../../instance-correspondence.md#per-project-target-differences). The [shared TypeSpec accounting](../../instance-correspondence.md#typespec-finding-accounting) retains all 17 uncredited warnings. Zero means no corresponding finding was observed and the relevant predicate is absent/different, not that this member's operations are necessarily compliant.

## NOTES

Shared frozen inputs, configured source scope, selected Swagger-version policy and execution provenance are in the [group report](../../migration.md). The 59 affected projects' metadata-only recompilations exactly reproduced all 104 shared findings; all source/selected-version route bindings were unique and exact. No production linter changes or additional full corpus run were made.

[Original implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/put-request-response-scheme.ts). Saved-data reconstruction: `python analyze-instances.py --root .` from the group directory.
