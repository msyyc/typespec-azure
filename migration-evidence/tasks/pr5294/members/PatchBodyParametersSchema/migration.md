# PatchBodyParametersSchema migration

## 1. Conclusion and scope

The TypeSpec linter `no-unsafe-patch-body-properties` includes
[PatchBodyParametersSchema](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-body-parameters-schema.md).
**Not fully equivalent:** effective PATCH visibility, authored discriminators,
falsy defaults and array traversal intentionally differ. The fresh current-head
group run completed. Prior callback observation attributes the native
implementation family; it does not establish per-defect parity.

## 2. Actual coverage

Fresh corpus: 487/487 assessable projects; zero compilation/worker failures.
Diagnostics are individual findings, not project counts.

| Count                                                        | Swagger linter | TypeSpec linter |
| ------------------------------------------------------------ | -------------: | --------------: |
| Reported diagnostics, explicit implementation-family mapping |            715 |             914 |

The shared TypeSpec rule has 1,337 group findings, counted once across the three
members. The 914 mapped safety observations are the actual required (478),
default (436) and visibility (0) callback branches observed at `94b316787`, not guesses from displayed
messages or 914 proven counterparts to 715 Swagger defects. The Swagger
functions returned 797 safety checks before Spectral reporting collapsed 82.
The justified shared route unit and complete accounting are in the
[detailed group analysis](../../detailed-analysis.md#counting-levels).
Historical 703/897 observations remain accessible in the historical appendix.

The November 2 run at `8a92389c9` reproduced every raw and aligned diagnostic
exactly in all 487 projects. This retains the earlier attribution, not a claim
that callback instrumentation was rerun. Whole derived-File exclusion
intentionally drops synthetic override warnings outside the supported scope;
no corpus safety findings changed.

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
explain material categories. The
[complete assessment](../../detailed-analysis.md) additionally identifies
five synthesized discriminator findings, candidate PATCH optionality, reporting
collapse and nine optional/default-free NetApp representation differences.
Exact same-version parity is not certified.
Saved fixture counts can include other combined-rule categories and must not
be treated as member-attributed native coverage.

## NOTES

Shared candidate, specs, runtime, 757 validated ARM tests (112 canonical PATCH),
20 injected PATCH controls, 37 applicable portable controls and limits:
[group report](../../migration.md).
Earlier [standalone evidence and old-report reconciliation](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/migration.md)
is historical, not the current combined-rule result.
No original lintdiff-source repair was performed or full equivalence certified.
