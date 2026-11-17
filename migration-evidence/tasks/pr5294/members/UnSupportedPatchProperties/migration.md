# UnSupportedPatchProperties migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/no-unsafe-patch-body-properties`
is assessed against the Swagger linter
[UnSupportedPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/un-supported-patch-properties.md).
Original migration linter PR: [Azure/typespec-azure#5294](https://github.com/Azure/typespec-azure/pull/5294).

## 2. Coverage

The saved run covered 487 selected projects with no compilation or worker
failures. The TypeSpec column contains the selected rule's observed
`immutable` callback family, after one identified out-of-version finding was
excluded from 62. It is not a count of matched Swagger defects. Other owning
rules and suppressed diagnostics were not captured; the suppression-inclusive
total is unassessed. [Group scope](../../scoped-assessment.md#exclusion-and-population-ledger).

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |            110 |              61 |

**Analysis:** The saved trace has 50 unmatched Swagger callbacks and one
unmatched TypeSpec diagnostic. [Member accounting](../../scoped-assessment.md#count-reconciliation).

**Assessed coverage:** Exposed immutable input and compliant controls are
covered for tested authored shapes. Nine of the 50 unmatched Swagger callbacks
involve read-only reference siblings; the remaining version and defect
correspondence is unassessed.

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

Groups use project, exact PATCH route, check family and encoded property-path
text. The immutable callbacks have no reporting-stage collapse in this run.
Unmatched keys are not proven corresponding defects.

| Difference (with evidence)                                                                    | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | analysis                                                                                                                                             |
| --------------------------------------------------------------------------------------------- | ----------------------------------: | --------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Excluded input and reference siblings](../../fresh-examples.md#read-only-reference-siblings) |                             50 / 50 |                             0 unmatched | TypeSpec excludes the input or an ancestor. Nine findings involve read-only reference siblings; the captured control explains the resolver boundary. |
| [Unmatched saved route](../../scoped-assessment.md#count-reconciliation)                      |                     0 / 0 unmatched |                                       1 | The selected-version relationship is unassessed; retain the observed finding.                                                                        |

**Raw-count reconciliation:** `110 - 61 = 50 - 1 = 49`.
Other owning-rule or suppressed warnings remain unmeasured.
[Scoped accounting](../../scoped-accounting.json).

## 4. Function-level coverage

| Behavior                                                                 | Result                                  | analysis                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Root `id`, `name`, `type`, `location` and `properties.provisioningState` | Covered for tested authored input       | Exposed immutable fields are diagnosed, including supported visibility overrides. [Injected controls](../../runs/20261102-8a92389c9/controls.json); [examples](../../evidence-details.md#visibility-and-immutable-input). |
| Unrelated nested names and ordinary Read/Create input                    | Covered under the TypeSpec input policy | Compliant nested names are accepted and excluded inputs are not treated as PATCH input. [Evidence](../../fresh-examples.md#excluded-input).                                                                               |
| Emitted read-only reference siblings                                     | Different observed behavior             | The Swagger callback can lose the raw sibling annotation at resolution. Policy and exact correspondence remain review decisions. [Evidence](../../detailed-analysis.md#recursive-reference-boundary).                     |

## NOTES

- **Inputs and validation:** The trace used `94b316787`; exact diagnostics
  were reproduced at `8a92389c9` without rerunning callback instrumentation.
  [Shared provenance, suppression limits and validation](../../scoped-assessment.md).
- **Historical evidence:** The earlier [standalone report](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/test/fixtures/UnSupportedPatchProperties/migration.md)
  uses a different population and is not the current group result.
