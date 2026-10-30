# PatchBodyParametersSchema migration

## 1. Conclusion and scope

The TypeSpec linter `no-unsafe-patch-body-properties` includes
[PatchBodyParametersSchema](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-body-parameters-schema.md).
**Not fully equivalent:** effective PATCH visibility, authored discriminators,
falsy defaults and array traversal intentionally differ. Current-head corpus
coverage and unresolved historical residuals remain unassessed.

## 2. Actual coverage

Historical corpus: 462/468 compiled projects; six failures excluded.
Diagnostics are individual findings, not project counts.

| Count                                             | Swagger linter |              TypeSpec linter |
| ------------------------------------------------- | -------------: | ---------------------------: |
| Historical reported diagnostics                   |            703 | 897 safety-category findings |
| Current-head member-attributed corpus diagnostics |     Unassessed |                   Unassessed |

The 897 historical observations comprise 472 required, 425 default and zero
exposed non-Update findings. They do not prove exact member attribution or a
common normalized identity. Do not substitute the combined rule's 1,258 total.

## 3. Function-level coverage

| Behavior                                             | Result                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Required/default input; optional default-free input  | Covered                                                 |
| Falsy defaults                                       | Intentional extra coverage                              |
| Ordinary excluded Read/Create input                  | Not traversed under native policy                       |
| Explicitly exposed non-Update input                  | Covered native extension                                |
| Identity safety boundary and authored discriminators | Covered with intentional emitted-shape differences      |
| Arrays                                               | Extended; required replacement-item descendants allowed |

## 4. Why diagnostic counts differ

Historical 703/897 differs through native input selection, falsy defaults,
arrays and emitted discriminator behavior. ProgrammableConnectivity attribution
and within-project residuals remain unresolved.
[Grouped evidence and examples](../../evidence-details.md#safety-and-counting).
Saved fixture counts can include other combined-rule categories and must not
be treated as member-attributed native coverage.

## NOTES

Shared candidate, specs, runtime, fresh 113-test inventory, failures and limits:
[group report](../../migration.md).
Earlier [standalone evidence and old-report reconciliation](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/migration.md)
is historical, not the current combined-rule result.
No source repair was performed or full equivalence certified.
