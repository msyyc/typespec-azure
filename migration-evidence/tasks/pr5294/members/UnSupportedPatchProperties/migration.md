# UnSupportedPatchProperties migration

## 1. Conclusion and scope

The TypeSpec linter `no-unsafe-patch-body-properties` includes
[UnSupportedPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/un-supported-patch-properties.md).
**Not blanket Swagger equivalence:** the native policy rejects exposed immutable
PATCH input rather than accepting emitted no-Update annotations. Fresh group
execution completed; direct branch attribution does not certify per-defect parity.

## 2. Actual coverage

Fresh corpus: 487/487 assessable projects; zero compilation/worker failures.
Diagnostics are individual findings, not project counts.

| Count                                                        | Swagger linter | TypeSpec linter |
| ------------------------------------------------------------ | -------------: | --------------: |
| Reported diagnostics, explicit implementation-family mapping |            110 |              62 |

The shared TypeSpec rule has 1,337 group findings, counted once. Its projects
must not be presented as this member's native coverage without attribution.
The 62 immutable observations were directly observed at `94b316787` through the
`immutable` callback branch; they are not guessed from message/property names
or asserted to match 62 original Swagger defects.
Historical 107/59 findings and historical member project sets remain historical.

The November 2 run at `8a92389c9` reproduced every raw and aligned diagnostic
exactly in all 487 projects. This retains the earlier branch attribution,
not freshly rerun callback instrumentation. No corpus immutable findings changed.

## 3. Function-level coverage

| Behavior                                                              | Result                                              |
| --------------------------------------------------------------------- | --------------------------------------------------- |
| Root `id`, `name`, `type`, `location`; `properties.provisioningState` | Covered                                             |
| Encoded/inherited names; unrelated nested names                       | Covered with compliant controls                     |
| Ordinary Read/Create input                                            | Excluded under native request policy                |
| Exposed immutable field even with Update visibility                   | Rejected                                            |
| Explicit Create-only override                                         | Intentional extra immutable and visibility findings |

## 4. Why diagnostic counts differ

Fresh [Read-only reference siblings](../../fresh-examples.md#read-only-reference-siblings)
explain nine Swagger-only provisioning-state findings across six projects;
effective PATCH input excludes them. The actual Dynatrace callback now confirms
reference-sibling loss, and annotation-preserving inlining changes its immutable
count from 1 to 0.
[Captured resolution boundary](../../detailed-analysis.md#recursive-reference-boundary).
All fifty unmatched Swagger immutable checks have an excluded-input source
chain; the two unmatched TypeSpec immutable checks are explicit source/reference
population differences. Historical readonly-reference fixture: 1/0.
Historical explicit Create-only
immutable fixture: 0/2, including one separate visibility finding from the
combined rule. [Evidence and examples](../../evidence-details.md#visibility-and-immutable-input).
These fixture counts are not fresh production observations or per-member parity.

## NOTES

Shared candidate, specs, runtime, 757 validated ARM tests (112 canonical PATCH),
20 injected PATCH controls, 37 applicable portable controls and limits:
[group report](../../migration.md).
The old [standalone equivalence conclusion and report reconciliation](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/migration.md)
must not be applied to the combined rule's changed native policy.
No original lintdiff-source repair was performed; documented parity boundaries remain open.
