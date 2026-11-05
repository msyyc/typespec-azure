# PutRequestResponseSchemeArm migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` is assessed against [`PutRequestResponseSchemeArm`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/put-request-response-scheme-arm.md). **Partial migration: registered createOrUpdate PUT traversal includes legacy and overwritten aliases; custom request/response contracts and response-body exceptions still prevent equivalence.**

## 2. Actual coverage

All 487 projects compiled successfully; none failed or was unassessed. Reported diagnostics are individual findings. The TypeSpec column contains only observed warnings attributed to this member's comparison, not the shared rule's entire output.

| Count                                                             | Swagger linter | TypeSpec linter |
| ----------------------------------------------------------------- | -------------- | --------------- |
| Reported diagnostics (member / corresponding TypeSpec)            | 212            | 144             |
| PUT comparison contexts, grouped by project/document/route/schema | 168            | 144             |

The grouped row counts checks, not equivalent defects. See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the causes and decisions.

## 3. Function-level coverage

| Behavior                                                   | Result                                                                                                                                 |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Registered createOrUpdate PUT request / canonical resource | Covered by effective payload identity; not universal emitted-schema structural equality.                                               |
| Legacy or overwritten registered PUTs                      | Included through the existing operation Set, deduplicated per resource/Operation.                                                      |
| Custom request / actual selected response                  | Not generally compared; body-policy exceptions and legacy modeling need separate treatment.                                            |
| Shared-rule controls                                       | [Exact-candidate controls](../../evidence-details.md#controls-and-validation) verify existing behavior, not coverage of absent checks. |

## 4. Why diagnostic counts differ

Only unpaired groups are listed. The TypeSpec count is for the same comparison; other rules' pre-suppression results and unrelated same-operation warnings are excluded.

| Difference / evidence                                                       | Swagger findings / checks | TypeSpec corresponding warnings | Gap analysis and decision                                                                 |
| --------------------------------------------------------------------------- | ------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------- |
| [Empty 200 responses](../../gap-analysis.md#existing-policy-exceptions)     | 23 / 9                    | 0                               | Review existing no-response-body suppressions/specs; do not duplicate that check.         |
| [Legacy request/response contracts](../../gap-analysis.md#legacy-contracts) | 45 / 15                   | 0                               | Review registration, DTOs and parent/child modeling; do not broaden blindly to every PUT. |

Zero does not mean that other TypeSpec policies are absent or that the APIs are compliant. Proposed fixes are not observed coverage; recommended exclusions are not approved retirements. [Exact targets and both engines' results](../../instance-correspondence.md#differing-projects) retain the evidence.

## NOTES

The [group report](../../migration.md#notes) records shared source/projection, suppression and corpus policies. [Controls and reproduction](../../evidence-details.md#controls-and-validation) and [all TypeSpec finding dispositions](../../instance-correspondence.md#typespec-finding-accounting) are retained.

[Original implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/put-request-response-scheme.ts). Reconstruct these reports with `python render-instances.py` from the group directory.
