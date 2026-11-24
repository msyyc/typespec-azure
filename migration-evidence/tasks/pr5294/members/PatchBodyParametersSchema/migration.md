# PatchBodyParametersSchema migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/no-unsafe-patch-body-properties`
is assessed against the Swagger linter
[PatchBodyParametersSchema](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-body-parameters-schema.md).
Original migration linter PR: [Azure/typespec-azure#5294](https://github.com/Azure/typespec-azure/pull/5294).

## 2. Coverage

The final source-fix run completed all 487 frozen projects with no failed or
unassessed projects. Its required/default/visibility diagnostics reproduce the
historical per-project target/message multisets exactly: 914 configured, minus
33 evidenced population exclusions, gives 881. The new generic lifecycle
findings belong to neither this member nor this table.
Other owning-rule warnings and suppressed findings were not captured; their
additional diagnostic count is unknown, not zero.
[Group scope](../../scoped-assessment.md#exclusion-and-population-ledger).

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |            715 |             881 |

**Analysis:** The 166-diagnostic excess is unchanged by the source fixes.
It is a diagnostic-count difference, not 166 additional equivalent defects.
The table separates final reports from pre-report callback multiplicity.
[Member accounting](../../scoped-assessment.md#count-reconciliation).

**Assessed coverage:** Required/default checks cover tested authored input.
Five emitted-only discriminator callbacks and one optionality difference lack
the same authored check. Version alignment and per-defect correspondence are not established.

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

The current TypeSpec results preserve every original-policy observation, so the
saved callback-to-report attribution remains applicable without rerunning Swagger.
Groups use project, exact PATCH route, check family and encoded property-path text,
not equivalent-defect identities. Zeros describe additional selected-rule findings,
not unmeasured owning warnings.
[Attribution and mixed report](../../scoped-assessment.md#reported-diagnostic-attribution).

| Difference (with evidence)                                                                              | Swagger diagnostics | TypeSpec diagnostics for the same check | analysis                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------- | ------------------: | --------------------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Effective input](../../detailed-analysis.md#effective-input-and-synthetic-fields)                      |                  79 |                                       0 | The 106 callbacks become 79 reports. TypeSpec excludes Read/Create-only input or an ancestor; the intended input policy remains a review decision.        |
| [Synthetic discriminator or optional input](../../scoped-assessment.md#reported-diagnostic-attribution) |                   3 |                                       0 | Two reports concern emitted-only fields; one concerns effectively optional input. Three more emitted-only callbacks contribute to the mixed report below. |
| [Falsy and array defaults](../../scoped-assessment.md#count-reconciliation)                             |                   0 |                                     185 | TypeSpec checks 128 falsy defaults and 57 other array defaults, beyond Swagger's truthiness/traversal policy.                                             |
| [Source/operation scope](../../scoped-assessment.md#count-reconciliation)                               |                   0 |                                       2 | Two diagnostics lack an identical saved PATCH route; selected-version/operation alignment remains pending.                                                |
| [NetApp representation](../../detailed-analysis.md#representation-policy-boundaries)                    |                   0 |                                       9 | The saved emitted PATCH fields are optional or default-free; the cause needs aligned-emission review.                                                     |
| [Mixed authored/synthetic report](../../scoped-assessment.md#reported-diagnostic-attribution)           |                   1 |                                       1 | One report combines three emitted-only checks with one shared authored check. Count the report once without hiding either behavior.                       |

**Count-only difference:** Outside the mixed report, shared accounting keys contain 684 TypeSpec diagnostics and 632 Swagger reports after reporting collapse: `632 - 684 = -52`. Equal text keys are not proof of equivalent defects.

**Raw-count reconciliation:** `715 - 881 = 79 + 3 - 185 - 2 - 9 + (1 - 1) - 52 = -166`.
The original 82-callback reduction comprises 27 excluded-input, 52 shared-key and three mixed-report callbacks; no TypeSpec diagnostic is removed by this attribution.
[Scoped accounting](../../scoped-accounting.json).

## 4. Function-level coverage

| Behavior                                             | Result                                | analysis                                                                                                                                                                                                                        |
| ---------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Required/default input and compliant optional fields | Covered for supported authored input  | Required, falsy-default and compliant cases passed in the [injected controls](../../runs/20261102-8a92389c9/controls.json).                                                                                                     |
| Falsy defaults and array-item defaults               | Extended TypeSpec behavior            | [Source examples](../../fresh-examples.md#native-only-projects) show the Swagger truthiness and traversal boundaries.                                                                                                           |
| Ordinary Read/Create-only input                      | Excluded by TypeSpec policy           | An explicit visibility override is checked separately. [Evidence](../../evidence-details.md#visibility-and-immutable-input).                                                                                                    |
| Default versus explicit Update visibility            | Message and controls clarified        | Default visibility is valid; exposed non-Update input is checked, while effective Read/Query-only input is filtered before traversal. [Current regressions](../../runs/20261124-qualified/assessment.md#canonical-regressions). |
| Synthesized emitted discriminators                   | Missing from the authored-field check | Five callbacks concern fields without an authored property; the required emitted policy remains undecided. [Evidence](../../detailed-analysis.md#effective-input-and-synthetic-fields).                                         |

## NOTES

- **Inputs and validation:** Current source `9e413f4725`, core `ce2f9bcdb494`,
  frozen specs `2cd3c5dd6d00`. The new full run reproduces this member's saved
  observations; the semantic trace remains historical, not newly instrumented.
  [Current receipts](../../runs/20261124-qualified/assessment.md);
  [shared attribution and limits](../../scoped-assessment.md).
- **Historical evidence:** The earlier [standalone report](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/PatchBodyParametersSchema/migration.md)
  uses a different population and is not the current group result.
