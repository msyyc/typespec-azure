# ConsistentPatchProperties migration

## 1. Conclusion and scope

The TypeSpec linter `no-unsafe-patch-body-properties` includes
[ConsistentPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-patch-properties.md).
**Not fully equivalent:** it compares authored encoded partial layouts,
including explicit resource associations, rather than reproducing emitted
synthetic properties and SDK filtering. Fresh group execution completed;
current-head emitted-layout parity is not established.

## 2. Actual coverage

Fresh corpus: 487/487 assessable projects; zero compilation/worker failures.
Diagnostics are individual findings, not project counts.

| Count                                                        | Swagger linter | TypeSpec linter |
| ------------------------------------------------------------ | -------------: | --------------: |
| Reported diagnostics, explicit implementation-family mapping |            150 |             361 |

The shared TypeSpec rule has 1,337 group findings, counted once, not as this
member's attributed count. The 361 layout observations were attributed at `94b316787` by
the actual `missing` callback branch, not displayed-message guesses
or a claim of 361 counterparts to 150 Swagger defects.
[Counting and route-unit limits](../../detailed-analysis.md#counting-levels).
Historical 151/302 data remains historical.

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

Fresh differences include
[removed/renamed versioned source](../../fresh-examples.md#version-populations),
[parent-versus-leaf counting](../../fresh-examples.md#parent-and-leaf-counting),
and [recursive Informatica layout](../../fresh-examples.md#recursive-informatica-layout).
Informatica's omission mechanism is now captured: an unresolved recursive
request reference exposes no children to `getProperties`. The
[detailed assessment](../../detailed-analysis.md#representation-policy-boundaries)
also identifies twelve extra associated-resource-name layout findings and
34 Search client-only findings across the combined rule.
These are not blanket emitted-layout equivalences.
The November 2 review fixes at `8a92389c9` decline ambiguous response layouts,
remove namespace-local GET discovery, exclude whole derived-File models and
use native all-visibility resource comparison with conservative encoded-name
ambiguity handling. These intentionally narrow synthetic cases; the final
487-project run reproduced every prior diagnostic exactly, so no corpus
layout findings changed. The 361-family attribution is retained prior analysis,
not freshly rerun callback instrumentation.

## NOTES

Shared candidate, specs, runtime, 757 validated ARM tests (112 canonical PATCH),
20 injected PATCH controls, 37 applicable portable controls and limits:
[group report](../../migration.md).
[Standalone evidence and old-report reconciliation](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/migration.md)
is historical and superseded by the consolidation.
No original lintdiff-source repair or full-corpus equivalence certification was performed.
