# PutGetPatchResponseSchema migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` is assessed against [`PutGetPatchResponseSchema`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-get-patch-response-schema.md). **Not equivalent: registered-resource traversal is narrower than payload consistency. No-content and collection-role comparisons should not be copied literally; the genuine legacy shape difference remains unresolved.**

## 2. Actual coverage

All 487 projects compiled successfully; none failed or was unassessed. Reported diagnostics are individual findings. The TypeSpec column contains only observed warnings attributed to this member's comparison, not the shared rule's entire output.

| Count                                                               | Swagger linter | TypeSpec linter |
| ------------------------------------------------------------------- | -------------- | --------------- |
| Reported diagnostics (member / corresponding TypeSpec)              | 50             | 0               |
| Distinct route comparisons, grouped by project/route/schema context | 36             | 0               |

The grouped row counts checks, not equivalent defects. See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the causes and decisions.

## 3. Function-level coverage

| Behavior                              | Result                                                                                                                                 |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Registered-resource return identity   | Retained narrower traversal, not general cross-method payload equality.                                                                |
| Empty ordinary-success response       | Existing no-response-body policy, explicitly suppressed on the observed targets.                                                       |
| No-content / collection-wrapper roles | Literal reference equality is misleading; recommend excluding these comparisons.                                                       |
| Different non-bodyless entity shapes  | SyncJob contract remains unresolved.                                                                                                   |
| Shared-rule controls                  | [Exact-candidate controls](../../evidence-details.md#controls-and-validation) verify existing behavior, not coverage of absent checks. |

## 4. Why diagnostic counts differ

Only unpaired groups are listed. The TypeSpec count is for the same comparison; other rules' pre-suppression results and unrelated same-operation warnings are excluded.

| Difference / evidence                                                                          | Swagger findings / checks | TypeSpec corresponding warnings | Decision                                                                                                      |
| ---------------------------------------------------------------------------------------------- | ------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [Empty 200 responses](../../gap-analysis.md#existing-policy-exceptions)                        | 30 / 16                   | 0                               | Review existing no-response-body suppressions/specs; do not duplicate that check.                             |
| [No-content / collection-role comparisons](../../gap-analysis.md#swagger-comparison-artifacts) | 19 / 19                   | 0                               | Recommend not porting misleading schema comparisons; this is not approved retirement or whole-API compliance. |
| [SyncJob PUT/GET shape difference](../../gap-analysis.md#legacy-contracts)                     | 1 / 1                     | 0                               | Confirm the wire contract; prefer a targeted fix and defer a broad structural matcher.                        |

Zero does not mean that other TypeSpec policies are absent or that the APIs are compliant. Proposed fixes are not observed coverage; recommended exclusions are not approved retirements. [Exact targets and both engines' results](../../instance-correspondence.md#differing-projects) retain the evidence.

## NOTES

The [group report](../../migration.md#notes) records shared source/projection, suppression and corpus policies. [Controls and reproduction](../../evidence-details.md#controls-and-validation) and [all TypeSpec finding dispositions](../../instance-correspondence.md#typespec-finding-accounting) are retained.

[Original implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/put-get-patch-schema.ts). Reconstruct these reports with `python render-instances.py` from the group directory.
