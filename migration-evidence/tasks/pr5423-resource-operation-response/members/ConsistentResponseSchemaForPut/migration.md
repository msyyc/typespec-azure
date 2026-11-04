# ConsistentResponseSchemaForPut migration

## 1. Conclusion and scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` consolidates [`ConsistentResponseSchemaForPut`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-response-schema-for-put.md).
**Not equivalent: exact 200/201 comparison is absent, including a genuine Quota plain-response mismatch.** Per-member TypeSpec finding attribution is unassessed.

## 2. Actual coverage

All 487 projects succeeded, zero failed/unassessed.
Reported diagnostics are individual findings, not projects.

| Count                                             | Swagger linter | TypeSpec linter       |
| ------------------------------------------------- | -------------- | --------------------- |
| Reported diagnostics                              | 16             | Unassessed per member |
| Affected projects (member / shared TypeSpec rule) | 10             | 34                    |

The shared TypeSpec rule reports 104 raw findings across the entire admitted
group, not 104 findings attributable to this member.
Project grouping is assessed: 3 projects have findings from both, 7 from this Swagger member
only and 31 from the shared TypeSpec rule only. The 34-project TypeSpec set is shared with every
member comparison, not additive or member-attributed. [Method and sets](../../project-differences.md#assessed-project-grouping).
See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ).

## 3. Function-level coverage

| Behavior                         | Result                                                                                                 |
| -------------------------------- | ------------------------------------------------------------------------------------------------------ |
| ConsistentResponseSchemaForPut   | Not equivalent: exact 200/201 comparison is absent, including a genuine Quota plain-response mismatch. |
| Compliant and violation controls | [Linked shared controls](../../evidence-details.md#controls-and-validation)                            |

## 4. Why diagnostic counts differ

The upstream implementation uses JavaScript object identity. Fifteen saved findings have identical raw schema references; avoiding that bug is desirable but does not implement the genuine equality requirement.
Swagger linter reports 16 findings in 10 projects;
the TypeSpec count for this member is unassessed, not zero.
[All member observations](observations.json), [exact targets](../../diagnostic-inventory.md),
[directional project groups](../../project-differences.md), and
[code-backed causes](../../evidence-details.md) preserve the findings and unresolved pairings.

## NOTES

This member shares the frozen population, artifacts, configured mode and source scope of the
[group report](../../migration.md); no duplicate corpus or independent TypeSpec attribution was run.
[Original implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/consistent-response-schema-for-put.ts).
Mode: `stagingOnly`; original audience ARM.
