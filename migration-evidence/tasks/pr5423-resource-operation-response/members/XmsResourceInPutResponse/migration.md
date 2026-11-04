# XmsResourceInPutResponse migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` consolidates [`XmsResourceInPutResponse`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/xms-resource-in-put-response.md).
**Partial source-policy overlap, not equivalent to checking x-ms-azure-resource on every emitted PUT response.** Per-member TypeSpec finding attribution is unassessed.

## 2. Actual coverage

All 487 projects succeeded, zero failed/unassessed.
Reported diagnostics are individual findings, not projects.

| Count                | Swagger linter | TypeSpec linter       |
| -------------------- | -------------- | --------------------- |
| Reported diagnostics | 155            | Unassessed per member |

The shared TypeSpec rule reports 104 raw findings across the entire admitted
group, not 104 findings attributable to this member.
See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ).

## 3. Function-level coverage

| Behavior                         | Result                                                                                                       |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| XmsResourceInPutResponse         | Partial source-policy overlap, not equivalent to checking x-ms-azure-resource on every emitted PUT response. |
| Compliant and violation controls | [Linked shared controls](../../evidence-details.md#controls-and-validation)                                  |

## 4. Why diagnostic counts differ

The registered-resource listener is not an emitted extension validator; custom/unregistered PUT responses are outside its audience.
Swagger linter reports 155 findings in 14 projects;
the TypeSpec count for this member is unassessed, not zero.
[All member observations](observations.json), [exact targets](../../diagnostic-inventory.md),
[directional project groups](../../project-differences.md), and
[code-backed causes](../../evidence-details.md) preserve the findings and unresolved pairings.

## NOTES

This member shares the frozen population, artifacts, configured mode and source scope of the
[group report](../../migration.md); no duplicate corpus or independent TypeSpec attribution was run.
[Original implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/with-xms-resource.ts).
Mode: `production`; original audience ARM.
