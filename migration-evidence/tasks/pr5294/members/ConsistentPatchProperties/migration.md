# ConsistentPatchProperties migration

## 1. Conclusion and scope

The TypeSpec linter `no-unsafe-patch-body-properties` includes
[ConsistentPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-patch-properties.md).
**Not fully equivalent:** it compares authored encoded partial layouts,
including explicit resource associations, rather than reproducing emitted
synthetic properties and SDK filtering. Current-head corpus parity is unknown.

## 2. Actual coverage

Historical corpus: 462/468 compiled projects; six failures excluded.
Diagnostics are individual findings, not project counts.

| Count                                             | Swagger linter |              TypeSpec linter |
| ------------------------------------------------- | -------------: | ---------------------------: |
| Historical reported diagnostics                   |            151 | 302 layout-category findings |
| Current-head member-attributed corpus diagnostics |     Unassessed |                   Unassessed |

All 27 historical Swagger projects overlap; the layout category fires in 29.
This does not establish exact correspondence or explain every extra finding.

## 3. Function-level coverage

| Behavior                                                    | Result                               |
| ----------------------------------------------------------- | ------------------------------------ |
| Missing/misnested properties; valid partial layout          | Covered                              |
| Encoded names, inherited overrides and nullable models      | Covered                              |
| Explicit association, response and same-path GET precedence | Covered                              |
| Authored discriminator versus emitted synthetic field       | Intentional difference               |
| Resource unions and open records                            | Conservative supported-layout policy |
| Unsupported request unions/indexers/tuples                  | Outside expansion scope              |

## 4. Why diagnostic counts differ

Historical 151/302 differs through native shape, emission/scope and collection
behavior. Informatica's omission mechanism and within-project residuals remain
unresolved. [Grouped evidence](../../evidence-details.md#layout-and-emission)
retains opposing inherited-discriminator outcomes, `never` and SDK-scope cases.
Latest ambiguity/fallback proposals are not implemented or measured corpus deltas.

## NOTES

Shared candidate, specs, runtime, fresh 113-test inventory and limits:
[group report](../../migration.md).
[Standalone evidence and old-report reconciliation](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/migration.md)
is historical and superseded by the consolidation.
No source repair or current full-corpus equivalence certification was performed.
