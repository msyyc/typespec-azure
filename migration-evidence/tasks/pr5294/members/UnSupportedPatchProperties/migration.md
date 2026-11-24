# UnSupportedPatchProperties migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/no-unsafe-patch-body-properties`
is assessed against the Swagger linter
[UnSupportedPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/un-supported-patch-properties.md).
Original migration linter PR: [Azure/typespec-azure#5294](https://github.com/Azure/typespec-azure/pull/5294).

## 2. Coverage

The final source-fix run completed all 487 frozen projects with no failed or
unassessed projects. Its `immutable` family contains 138 findings: 62 for this
member's reserved fields plus 76 for other resource-lifecycle restrictions.
The latter are outside this Swagger rule's name-based selector and excluded,
not credited as member coverage. Removing one evidenced out-of-version reserved
finding leaves **61**. All 62 original reserved-field observations were
reproduced exactly, including repeated source targets.

Other owning and suppressed diagnostics were not captured; their additional
count is unknown, not zero. An owning-rule suppression is not replacement
coverage. [Current check/population ledger](../../runs/20261124-qualified/accepted-assessment.json).

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |            110 |              61 |

**Analysis:** Original-policy observations remain 110 / 61: 50 excluded-input
Swagger reports versus one additional TypeSpec route finding, with 60 shared
accounting-key occurrences on each side. A lifecycle-only replacement lost 52
reserved-field warnings; the final implementation restores them while adding
the separate generic check. Neither the 76 broader warnings nor the restored
warnings are an additional row in this member's reconciliation.
[Corpus-driven qualification](../../runs/20261124-qualified/assessment.md#reserved-field-policy).

**Assessed coverage:** Exposed immutable input and compliant controls are
covered for tested authored shapes. Nine of the 50 excluded-input Swagger reports involve read-only reference siblings. Version alignment and per-defect correspondence are not established.

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

Groups use project, exact PATCH route, check family and encoded property-path
text. Reserved-field findings have no reporting-stage collapse; every historical
occurrence is present in the final run. Equal keys are not proof of equivalent
defects. Zeros describe additional captured selected-rule findings, not
unmeasured owning diagnostics. The broader generic lifecycle warnings remain
outside this table. [Attribution](../../scoped-assessment.md#reported-diagnostic-attribution).

| Difference (with evidence)                                                                    | Swagger diagnostics | TypeSpec diagnostics for the same check | analysis                                                                                                                                            |
| --------------------------------------------------------------------------------------------- | ------------------: | --------------------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Excluded input and reference siblings](../../fresh-examples.md#read-only-reference-siblings) |                  50 |                                       0 | TypeSpec excludes the input or an ancestor. Nine reports involve read-only reference siblings; the captured control explains the resolver boundary. |
| [Source/operation alignment](../../scoped-assessment.md#count-reconciliation)                 |                   0 |                                       1 | One diagnostic has no identical saved PATCH route; selected-version/operation alignment remains pending. Retain the finding.                        |

**Raw-count reconciliation:** `110 - 61 = 50 - 1 = 49`.
Other owning-rule or suppressed warnings remain unmeasured.
[Scoped accounting](../../scoped-accounting.json).

## 4. Function-level coverage

| Behavior                                                                 | Result                                  | analysis                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Root `id`, `name`, `type`, `location` and `properties.provisioningState` | Reserved-field safeguard retained       | The ARM guideline does not become optional when resource annotations are missing, incorrectly Update-visible, or no counterpart exists. Reduced corpus cases protect this boundary. [Evidence](../../runs/20261124-qualified/assessment.md#reserved-field-policy). |
| Unrelated nested names and ordinary Read/Create input                    | Covered under the TypeSpec input policy | Compliant nested names are accepted and excluded inputs are not treated as PATCH input. [Evidence](../../fresh-examples.md#excluded-input).                                                                                                                        |
| Emitted read-only reference siblings                                     | Different observed behavior             | The Swagger callback can lose the raw sibling annotation at resolution. Policy and exact correspondence remain review decisions. [Evidence](../../detailed-analysis.md#recursive-reference-boundary).                                                              |
| Other resource properties lacking Update visibility                      | Broader TypeSpec policy, excluded here  | The 76 new warnings concern modeled resource/PATCH contract conflicts, not this Swagger selector or 76 established service defects. [Examples and action](../../runs/20261124-qualified/assessment.md#generic-lifecycle-policy).                                   |

## NOTES

- **Inputs and validation:** Current source `9e413f4725`, core `ce2f9bcdb494`,
  frozen specs `2cd3c5dd6d00`. The final full run and 112 canonical tests passed;
  18 exact assertions compare original, rejected and corrected predicates.
  [Current receipts](../../runs/20261124-qualified/assessment.md);
  [shared attribution and limits](../../scoped-assessment.md).
- **Historical evidence:** The earlier [standalone report](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/migration.md)
  uses a different population and is not the current group result.
