# UnSupportedPatchProperties migration

## 1. Conclusion and scope

The TypeSpec linter `no-unsafe-patch-body-properties` includes
[UnSupportedPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/un-supported-patch-properties.md).
**Not blanket Swagger equivalence:** the native policy rejects exposed immutable
PATCH input rather than accepting emitted no-Update annotations. Current-head
corpus coverage remains unassessed.

## 2. Actual coverage

Historical corpus: 462/468 compiled projects; six failures excluded.
Diagnostics are individual findings, not project counts.

| Count                                             | Swagger linter |                TypeSpec linter |
| ------------------------------------------------- | -------------: | -----------------------------: |
| Historical reported diagnostics                   |            107 | 59 immutable-category findings |
| Current-head member-attributed corpus diagnostics |     Unassessed |                     Unassessed |

Historical project sets: 45 Swagger projects, 21 TypeSpec projects, 21 overlap,
24 Swagger-only and zero TypeSpec-only. Equal or lower counts alone would not
prove that every immutable input is handled.

## 3. Function-level coverage

| Behavior                                                              | Result                                              |
| --------------------------------------------------------------------- | --------------------------------------------------- |
| Root `id`, `name`, `type`, `location`; `properties.provisioningState` | Covered                                             |
| Encoded/inherited names; unrelated nested names                       | Covered with compliant controls                     |
| Ordinary Read/Create input                                            | Excluded under native request policy                |
| Exposed immutable field even with Update visibility                   | Rejected                                            |
| Explicit Create-only override                                         | Intentional extra immutable and visibility findings |

## 4. Why diagnostic counts differ

Historical 107/59 reflects effective input and emitted annotation/reference
differences. Saved readonly-reference fixture: 1/0. Saved explicit Create-only
immutable fixture: 0/2, including one separate visibility finding from the
combined rule. [Evidence and examples](../../evidence-details.md#visibility-and-immutable-input).
This is not proof of fresh current-head project coverage or per-member parity.

## NOTES

Shared candidate, specs, runtime, fresh 113-test inventory and limits:
[group report](../../migration.md).
The old [standalone equivalence conclusion and report reconciliation](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/migration.md)
must not be applied to the combined rule's changed native policy.
No source repair was performed; unresolved current corpus questions remain open.
