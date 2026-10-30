# PatchBodyParametersSchema migration

## 1. Conclusion and scope

The TypeSpec linter `no-unsafe-patch-body-properties` includes
[PatchBodyParametersSchema](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-body-parameters-schema.md).
**Not fully equivalent:** effective PATCH visibility, authored discriminators,
falsy defaults and array traversal intentionally differ. The fresh current-head
group run completed; member-attributed TypeSpec counts and residual parity
remain unassessed.

## 2. Actual coverage

Fresh corpus: 487/487 assessable projects; zero compilation/worker failures.
Diagnostics are individual findings, not project counts.

| Count                                        | Swagger linter | TypeSpec linter |
| -------------------------------------------- | -------------: | --------------: |
| Fresh member-attributed reported diagnostics |            715 |      Unassessed |
| Projects with this Swagger member's findings |             97 |      Unassessed |

The shared TypeSpec rule has 1,337 group findings, counted once across the three
members. They are not this member's native count. Message families do not prove
individual attribution; no common actionable count has been established.
Historical 703/897 observations remain accessible in the historical appendix.

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

Fresh examples show native input selection, falsy defaults, arrays and
versioned-source differences.
[Excluded input](../../fresh-examples.md#excluded-input),
[defaults and arrays](../../fresh-examples.md#native-only-projects), and
[ProgrammableConnectivity's now-identified operation/version artifact](../../fresh-examples.md#version-populations)
explain material categories. Exact full correspondence remains unassessed.
Saved fixture counts can include other combined-rule categories and must not
be treated as member-attributed native coverage.

## NOTES

Shared candidate, specs, runtime, fresh 758-test suite, 20 injected PATCH
controls, generic-control failures and limits:
[group report](../../migration.md).
Earlier [standalone evidence and old-report reconciliation](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/migration.md)
is historical, not the current combined-rule result.
No source repair was performed or full equivalence certified.
