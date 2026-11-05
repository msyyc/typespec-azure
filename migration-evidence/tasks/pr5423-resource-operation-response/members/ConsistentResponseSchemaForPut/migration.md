# ConsistentResponseSchemaForPut migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` is assessed against [`ConsistentResponseSchemaForPut`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-response-schema-for-put.md). **Not a complete mapping to this ARM rule. Azure Core already detects the genuine success-schema difference before suppression; the Swagger object-identity bug should not be reproduced.**

## 2. Actual coverage

All 487 projects compiled successfully; none failed or was unassessed. Reported diagnostics are individual findings. The TypeSpec column contains only observed warnings attributed to this member's comparison, not the shared rule's entire output.

| Count                                                             | Swagger linter | TypeSpec linter |
| ----------------------------------------------------------------- | -------------- | --------------- |
| Reported diagnostics (member / corresponding TypeSpec)            | 16             | 0               |
| PUT comparison contexts, grouped by project/document/route/schema | 16             | 0               |

The grouped row counts checks, not equivalent defects. See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the causes and decisions.

## 3. Function-level coverage

| Behavior                         | Result                                                                                                                                  |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Different 200/201 success bodies | Azure Core response-schema-problem detects the observed Quota case before suppression; this ARM rule does not independently compare it. |
| Identical 200/201 schemas        | Correctly avoids the Swagger object-identity bug.                                                                                       |
| Shared-rule controls             | [Exact-candidate controls](../../evidence-details.md#controls-and-validation) verify existing behavior, not coverage of absent checks.  |

## 4. Why diagnostic counts differ

Only unpaired groups are listed. The TypeSpec count is for the same comparison; other rules' pre-suppression results and unrelated same-operation warnings are excluded.

| Difference / evidence                                                               | Swagger findings / checks | TypeSpec corresponding warnings | Gap analysis and decision                                                                       |
| ----------------------------------------------------------------------------------- | ------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------- |
| [Quota success-schema difference](../../gap-analysis.md#existing-policy-exceptions) | 1 / 1                     | 0                               | Review the existing Azure Core rule's suppression/legacy exception; do not duplicate it in ARM. |
| [Swagger object-identity bug](../../gap-analysis.md#swagger-comparison-artifacts)   | 15 / 15                   | 0                               | Confirmed false positives: do not reproduce the bug.                                            |

Zero does not mean that other TypeSpec policies are absent or that the APIs are compliant. Proposed fixes are not observed coverage; recommended exclusions are not approved retirements. [Exact targets and both engines' results](../../instance-correspondence.md#differing-projects) retain the evidence.

## NOTES

The [group report](../../migration.md#notes) records shared source/projection, suppression and corpus policies. [Controls and reproduction](../../evidence-details.md#controls-and-validation) and [all TypeSpec finding dispositions](../../instance-correspondence.md#typespec-finding-accounting) are retained.

[Original implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/consistent-response-schema-for-put.ts). Reconstruct these reports with `python render-instances.py` from the group directory.
