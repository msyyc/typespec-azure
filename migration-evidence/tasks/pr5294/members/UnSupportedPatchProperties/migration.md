# UnSupportedPatchProperties migration

## 1. Conclusion and scope

The TypeSpec linter `no-unsafe-patch-body-properties` includes
[UnSupportedPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/un-supported-patch-properties.md).
**Not blanket Swagger equivalence:** the native policy rejects exposed immutable
PATCH input rather than accepting emitted no-Update annotations. Fresh group
execution completed; member-specific native parity remains unassessed.

## 2. Actual coverage

Fresh corpus: 487/487 assessable projects; zero compilation/worker failures.
Diagnostics are individual findings, not project counts.

| Count                                        | Swagger linter | TypeSpec linter |
| -------------------------------------------- | -------------: | --------------: |
| Fresh member-attributed reported diagnostics |            110 |      Unassessed |
| Projects with this Swagger member's findings |             45 |      Unassessed |

The shared TypeSpec rule has 1,337 group findings, counted once. Its projects
must not be presented as this member's native coverage without attribution.
Historical 107/59 findings and historical member project sets remain historical.

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
effective PATCH input excludes them. The exact internal Swagger resolver-loss
point is not instrumented. Historical readonly-reference fixture: 1/0.
Historical explicit Create-only
immutable fixture: 0/2, including one separate visibility finding from the
combined rule. [Evidence and examples](../../evidence-details.md#visibility-and-immutable-input).
These fixture counts are not fresh production observations or per-member parity.

## NOTES

Shared candidate, specs, runtime, fresh 758-test suite, 20 injected PATCH
controls, generic-control failures and limits:
[group report](../../migration.md).
The old [standalone equivalence conclusion and report reconciliation](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/migration.md)
must not be applied to the combined rule's changed native policy.
No source repair was performed; unresolved current corpus questions remain open.
