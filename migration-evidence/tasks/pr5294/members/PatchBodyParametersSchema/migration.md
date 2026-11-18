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
matched Swagger defects. Other owning-rule warnings and suppressed findings were not captured; their additional diagnostic count is unknown.
[Group scope](../../scoped-assessment.md#exclusion-and-population-ledger).

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |            715 |             881 |

**Analysis:** The TypeSpec linter reports 166 more diagnostics in these families. The table below separates final reports from callback multiplicity rather than treating each callback as a reported diagnostic.
[Member accounting](../../scoped-assessment.md#count-reconciliation).

**Assessed coverage:** Required/default checks cover tested authored input.
Five emitted-only discriminator callbacks and one optionality difference lack
the same authored check. Version alignment and per-defect correspondence are not established.

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

Counts below are final reported diagnostics, attributed from the saved callbacks without running either linter. Groups use exact project, PATCH route, check family and encoded property-path text, not equivalent-defect identities. Zeros apply only to additional selected-rule diagnostics in each category; other owning-rule warnings were not measured. [Attribution and mixed-report evidence](../../scoped-assessment.md#reported-diagnostic-attribution).

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
