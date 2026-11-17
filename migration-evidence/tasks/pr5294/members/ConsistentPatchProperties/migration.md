# ConsistentPatchProperties migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/no-unsafe-patch-body-properties`
is assessed against the Swagger linter
[ConsistentPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-patch-properties.md).
Original migration linter PR: [Azure/typespec-azure#5294](https://github.com/Azure/typespec-azure/pull/5294).

## 2. Coverage

The saved run covered 487 selected projects with no compilation or worker
failures. The TypeSpec column contains the selected rule's observed `missing`
callback family, after 57 identified out-of-population findings were excluded
from 361. It is not a count of matched Swagger defects.

The existing `arm-resource-patch` rule can report overlapping layout checks,
but its unsuppressed and suppressed diagnostics were not captured. The
suppression-inclusive total is unassessed.
[Suppression evidence](../../scoped-assessment.md#suppression-and-runtime-limits).

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |            150 |             304 |

**Analysis:** The trace has 61 unmatched Swagger callbacks and 215 unmatched
TypeSpec diagnostics. [Member accounting](../../scoped-assessment.md#count-reconciliation).

**Assessed coverage:** Supported authored layouts are covered for tested
shapes. Twelve TypeSpec resource-name findings need a policy decision.
Unsupported shapes, owning-rule overlap and version alignment remain
unassessed.

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

Groups use project, exact PATCH route, check family and encoded property-path
text. The layout callbacks have no reporting-stage collapse in this run.
Unmatched keys are not proven corresponding defects.

| Difference (with evidence)                                                              | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | analysis                                                                                                    |
| --------------------------------------------------------------------------------------- | ----------------------------------: | --------------------------------------: | ----------------------------------------------------------------------------------------------------------- |
| [Excluded input](../../detailed-analysis.md#effective-input-and-synthetic-fields)       |                               9 / 9 |                             0 unmatched | The TypeSpec linter excludes the effective input or ancestor; other owning-rule diagnostics are unassessed. |
| [Missing parents and leaves](../../detailed-analysis.md#parent-and-leaf-accounting)     |                             52 / 52 |                                     175 | Swagger stops at a parent and TypeSpec reports supported leaves. Do not equate the counts with defects.     |
| [Recursive request](../../detailed-analysis.md#recursive-reference-boundary)            |                     0 / 0 unmatched |                                      24 | The Swagger callback receives an unresolved recursive reference without inspectable children.               |
| [Associated-resource name](../../detailed-analysis.md#representation-policy-boundaries) |                     0 / 0 unmatched |                                      12 | The payload filter causes these findings; whether they are desirable requires policy review.                |
| [Unmatched saved routes](../../scoped-assessment.md#count-reconciliation)               |                     0 / 0 unmatched |                                       4 | Source-to-selected-version alignment remains unassessed.                                                    |

**Raw-count reconciliation:** `150 - 304 = 9 + 52 - 175 - 24 - 12 - 4 = -154`.
Suppressed and other owning-rule warnings are not measured by this equation.
[Scoped accounting](../../scoped-accounting.json).

## 4. Function-level coverage

| Behavior                                                        | Result                                      | analysis                                                                                                                                                                                     |
| --------------------------------------------------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Partial layout, inherited and encoded names, compliant controls | Covered for tested authored shapes          | The TypeSpec linter compares supported encoded partial layouts. [Injected controls](../../runs/20261102-8a92389c9/controls.json); [examples](../../evidence-details.md#layout-and-emission). |
| Explicit resource association and response/GET selection        | Covered for tested cases                    | Ambiguous preferred responses decline layout rather than choosing an unrelated fallback. [Validation](../../runs/20261102-8a92389c9/local-validation.json).                                  |
| Synthetic fields and unsupported union/transport shapes         | Unassessed for full emitted-layout coverage | Authored and emitted models differ; traversal is deliberately limited. [Examples](../../evidence-details.md#layout-and-emission).                                                            |
| Existing `arm-resource-patch` layout checks                     | Unassessed                                  | The `modelSuperset` branch can overlap, but directives alone do not establish suppressed findings. [Evidence](../../scoped-assessment.md#suppression-and-runtime-limits).                    |

## NOTES

- **Inputs and validation:** The trace used `94b316787`; exact diagnostics
  were reproduced at `8a92389c9` without rerunning callback instrumentation.
  [Shared provenance and validation](../../scoped-assessment.md).
- **Historical evidence:** The earlier [standalone report](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/ConsistentPatchProperties/migration.md)
  uses a different population and is not the current group result.
