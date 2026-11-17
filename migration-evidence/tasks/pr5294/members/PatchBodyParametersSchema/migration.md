# PatchBodyParametersSchema migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/no-unsafe-patch-body-properties`
is assessed against the Swagger linter
[PatchBodyParametersSchema](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-body-parameters-schema.md).
Original migration linter PR: [Azure/typespec-azure#5294](https://github.com/Azure/typespec-azure/pull/5294).

## 2. Coverage

The saved run covered 487 selected projects with no compilation or worker
failures. The TypeSpec column contains the selected rule's observed
required/default/visibility callback families, after 33 identified
out-of-population findings were excluded from 914. It is not a count of
matched Swagger defects. Other owning-rule warnings and suppressed findings
were not captured; the suppression-inclusive total is unassessed.
[Group scope](../../scoped-assessment.md#exclusion-and-population-ledger).

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |            715 |             881 |

**Analysis:** The saved trace has 112 unmatched Swagger callbacks and 196
unmatched TypeSpec diagnostics in these families.
[Member accounting](../../scoped-assessment.md#count-reconciliation).

**Assessed coverage:** Required/default checks cover tested authored input.
Five emitted-only discriminator callbacks and one optionality difference lack
the same authored check. Version alignment and per-defect correspondence remain
unassessed.

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

Groups use exact project, PATCH route, check family and encoded property-path
text. Swagger raw reports cannot be attributed uniquely to groups after the
82-result reporting collapse. Values marked unmatched do not establish
corresponding defects.

| Difference (with evidence)                                                                                   | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | analysis                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------: | --------------------------------------: | ------------------------------------------------------------------------------------------------------------------------------- |
| [Effective input](../../detailed-analysis.md#effective-input-and-synthetic-fields)                           |                    Unassessed / 106 |                             0 unmatched | The TypeSpec check excludes Read/Create-only input or an ancestor. Review the intended policy.                                  |
| [Synthetic discriminator or optional input](../../detailed-analysis.md#effective-input-and-synthetic-fields) |                      Unassessed / 6 |                             0 unmatched | Five emitted-only discriminator fields and one optional field have no matching authored required check.                         |
| [Falsy and array defaults](../../scoped-assessment.md#count-reconciliation)                                  |                     0 / 0 unmatched |                                     185 | TypeSpec checks 128 falsy defaults and 57 other array defaults. This is broader than Swagger's traversal and truthiness checks. |
| [Source/operation scope](../../scoped-assessment.md#count-reconciliation)                                    |                     0 / 0 unmatched |                                       2 | Two unmatched-route findings remain; their alignment is unassessed.                                                             |
| [NetApp representation](../../detailed-analysis.md#representation-policy-boundaries)                         |                     0 / 0 unmatched |                                       9 | The saved emitted PATCH fields are optional or default-free; the cause needs aligned-emission review.                           |

**Raw-count reconciliation:** `715 - 881 = 106 + 6 - 185 - 2 - 9 - 82 = -166`.
The 82 are reporting-stage collapsed callbacks, not removed TypeSpec findings.
[Scoped accounting](../../scoped-accounting.json).

## 4. Function-level coverage

| Behavior                                             | Result                                | analysis                                                                                                                                                                                |
| ---------------------------------------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Required/default input and compliant optional fields | Covered for supported authored input  | Required, falsy-default and compliant cases passed in the [injected controls](../../runs/20261102-8a92389c9/controls.json).                                                             |
| Falsy defaults and array-item defaults               | Extended TypeSpec behavior            | [Source examples](../../fresh-examples.md#native-only-projects) show the Swagger truthiness and traversal boundaries.                                                                   |
| Ordinary Read/Create-only input                      | Excluded by TypeSpec policy           | An explicit visibility override is checked separately. [Evidence](../../evidence-details.md#visibility-and-immutable-input).                                                            |
| Synthesized emitted discriminators                   | Missing from the authored-field check | Five callbacks concern fields without an authored property; the required emitted policy remains undecided. [Evidence](../../detailed-analysis.md#effective-input-and-synthetic-fields). |

## NOTES

- **Inputs and validation:** The trace used `94b316787`; exact diagnostics
  were reproduced at `8a92389c9` without rerunning callback instrumentation.
  [Shared provenance, suppression limits and validation](../../scoped-assessment.md).
- **Historical evidence:** The earlier [standalone report](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/migration.md)
  uses a different population and is not the current group result.
