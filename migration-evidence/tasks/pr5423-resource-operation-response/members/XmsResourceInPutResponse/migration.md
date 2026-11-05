# XmsResourceInPutResponse migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` is assessed against [`XmsResourceInPutResponse`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/xms-resource-in-put-response.md). **Not covered: canonical resource registration does not enforce the selected response's resource marker. Custom/action policy boundaries remain unresolved.**

## 2. Actual coverage

All 487 projects compiled successfully; none failed or was unassessed. Reported diagnostics are individual findings. The TypeSpec column contains only observed warnings attributed to this member's comparison, not the shared rule's entire output.

| Count                                                             | Swagger linter | TypeSpec linter |
| ----------------------------------------------------------------- | -------------- | --------------- |
| Reported diagnostics (member / corresponding TypeSpec)            | 155            | 0               |
| PUT comparison contexts, grouped by project/document/route/schema | 57             | 0               |

The grouped row counts checks, not equivalent defects. See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the causes and decisions.

## 3. Function-level coverage

| Behavior                                                                 | Result                                                                                                                                 |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| Selected response resource marker, including inherited/reference markers | Missing independent policy; canonical registration/request warnings do not enforce it.                                                 |
| Custom/action response payloads                                          | Required resource semantics remain unresolved; not every missing marker is a proven defect.                                            |
| Shared-rule controls                                                     | [Exact-candidate controls](../../evidence-details.md#controls-and-validation) verify existing behavior, not coverage of absent checks. |

## 4. Why diagnostic counts differ

Only unpaired groups are listed. The TypeSpec count is for the same comparison; other rules' pre-suppression results and unrelated same-operation warnings are excluded.

| Difference / evidence                                                                  | Swagger findings / checks | TypeSpec corresponding warnings | Gap analysis and decision                                                            |
| -------------------------------------------------------------------------------------- | ------------------------- | ------------------------------- | ------------------------------------------------------------------------------------ |
| [Independent response-resource policy](../../gap-analysis.md#response-resource-policy) | 155 / 57                  | 0                               | Design a focused check with custom/action boundaries; the policy remains unresolved. |

Zero does not mean that other TypeSpec policies are absent or that the APIs are compliant. Proposed fixes are not observed coverage; recommended exclusions are not approved retirements. [Exact targets and both engines' results](../../instance-correspondence.md#differing-projects) retain the evidence.

## NOTES

The [group report](../../migration.md#notes) records shared source/projection, suppression and corpus policies. [Controls and reproduction](../../evidence-details.md#controls-and-validation) and [all TypeSpec finding dispositions](../../instance-correspondence.md#typespec-finding-accounting) are retained.

[Original implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/with-xms-resource.ts). Reconstruct these reports with `python render-instances.py` from the group directory.
