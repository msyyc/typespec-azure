# ARM PATCH property migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/no-unsafe-patch-body-properties`
is assessed against the Swagger linters
[PatchBodyParametersSchema](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-body-parameters-schema.md),
[ConsistentPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-patch-properties.md),
and [UnSupportedPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/un-supported-patch-properties.md).
Original migration linter PR: [Azure/typespec-azure#5294](https://github.com/Azure/typespec-azure/pull/5294).

## 2. Coverage

The saved run assessed 487 selected projects, with no compilation or worker
failures. Swagger used the saved selected-version output; TypeSpec used an
unprojected source program with the selected rule explicitly enabled. The
TypeSpec count excludes 91 identified client-only or other-version observations
from the original 1,337. Other uncertain version and route attribution remains
in the count.

These are individual reported diagnostics from the selected rule, not
equivalent defects. Corresponding suppressed or unsuppressed diagnostics from
other owning rules were not captured. The suppression-inclusive corpus total
is therefore unassessed. A source scan found 47 directives for one potentially
overlapping rule; directives are not diagnostic counts.
[Scope and suppression evidence](scoped-assessment.md#suppression-and-runtime-limits).

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |            975 |           1,246 |

**Analysis:** The saved trace has 834 shared check/path text occurrences,
223 unmatched Swagger callbacks and 412 unmatched TypeSpec diagnostics.
Those keys do not establish corresponding defects.

**Assessed coverage:** Required/default input, supported layouts and immutable
input are covered for tested authored shapes. Five emitted-only discriminator
callbacks and one optionality difference lack the same authored-input check.
Twelve associated-resource name findings and nine NetApp representation findings
need policy or aligned-emission review. Suppression, remaining version alignment
and current-head coverage are unassessed.
[Assessment and member status](scoped-assessment.md).

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

The accounting key is project, exact PATCH route, check family and encoded
property-path text. Table groups contain unmatched keys, not proven equivalent
defects. The second number in the Swagger column counts pre-report callbacks;
the raw reports cannot be assigned uniquely to those groups after reporting
collapse. TypeSpec values count selected-rule diagnostics in the section 2
scope. Other owning-rule counts remain unassessed.

| Difference (with evidence)                                                                 | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | analysis                                                                                                                                           |
| ------------------------------------------------------------------------------------------ | ----------------------------------: | --------------------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Effective input](scoped-assessment.md#count-reconciliation)                               |                    Unassessed / 165 |                             0 unmatched | Read/Create-only input or an ancestor is excluded. Keep the distinction visible for policy review; owning-rule findings were not captured.         |
| [Synthetic discriminator and optional input](scoped-assessment.md#count-reconciliation)    |                      Unassessed / 6 |                             0 unmatched | Five emitted-only discriminators and one optional input lack the same authored check. Review the required policy rather than assuming equivalence. |
| [Missing parents and leaves](detailed-analysis.md#parent-and-leaf-accounting)              |                     Unassessed / 52 |                                     175 | Swagger stops at a missing parent; TypeSpec reports supported leaves. The counts are not normalized into common defects.                           |
| [Falsy defaults and arrays](scoped-assessment.md#count-reconciliation)                     |                     0 / 0 unmatched |                                     185 | TypeSpec checks falsy defaults and array-item defaults that Swagger misses. The intended extension remains a review decision.                      |
| [Recursive reference](detailed-analysis.md#recursive-reference-boundary)                   |                     0 / 0 unmatched |                                      24 | The saved Swagger callback cannot inspect the recursive request children. A counterfactual control explains the boundary, not parity.              |
| [Source and operation scope](scoped-assessment.md#count-reconciliation)                    |                     0 / 0 unmatched |                                       7 | Findings without an identical saved PATCH route remain in the count; their alignment is unassessed.                                                |
| [Resource and PATCH representation](detailed-analysis.md#representation-policy-boundaries) |                     0 / 0 unmatched |                                      21 | Twelve resource-name and nine optional/default-free findings need policy or aligned-emission review.                                               |

**Raw-count reconciliation:** `975 - 1,246 = 165 + 6 + 52 - 175 - 185 - 24 - 7 - 21 - 82 = -271`.
The final 82 are callbacks collapsed during Swagger reporting. Distinct checks
and distinct owning diagnostics are not deduplicated. The arithmetic does not
resolve unmeasured suppressed warnings or semantic correspondence.
[Project directions and exact targets](scoped-project-differences.md).

## 4. Function-level coverage

| Behavior                                                        | Result                                  | analysis                                                                                                                                                                                                |
| --------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Required/default PATCH input and optional default-free controls | Covered for supported authored input    | Falsy and array defaults extend Swagger behavior; emitted optionality is not aligned. [Injected controls](runs/20261102-8a92389c9/controls.json)                                                        |
| Read/Create-only input and explicit visibility overrides        | Covered under the TypeSpec input policy | The Swagger linter can inspect fields excluded from effective PATCH input. [Examples](fresh-examples.md#excluded-input)                                                                                 |
| Root immutable fields and unrelated nested names                | Covered for tested authored input       | Read-only reference siblings can produce different Swagger findings. [Evidence](fresh-examples.md#read-only-reference-siblings)                                                                         |
| Partial encoded layout, inheritance and supported nested models | Covered for tested shapes               | Parent/leaf counts differ; associated-resource name policy is unresolved. [Evidence](scoped-assessment.md#count-reconciliation)                                                                         |
| Synthesized emitted discriminator properties                    | Missing from the authored-field check   | Five Swagger callbacks concern emitted fields with no authored property. The required emitted policy remains a reviewer decision. [Evidence](detailed-analysis.md#effective-input-and-synthetic-fields) |
| Unions, tuples, transport models and ambiguous resource layouts | Unassessed for full Swagger coverage    | The TypeSpec linter declines or limits traversal in these cases. Supported sibling safety checks remain separate. [Fixture evidence](evidence-details.md#layout-and-emission)                           |
| Existing owning rules and authored suppressions                 | Unassessed                              | The `arm-resource-patch` layout branch may overlap; saved target-only diagnostics do not capture its warnings. [Evidence](scoped-assessment.md#suppression-and-runtime-limits)                          |

## NOTES

- **Inputs:** Assessed implementation `8a92389c9`, core `cefb035e7721`,
  specs `2cd3c5dd6d00`; this is a report-only reuse of saved observations.
  The later PR head has a different compiler gitlink and has not been assessed
  by this corpus. [Provenance](fresh-evidence.md#november-2-final-review-fix-run).
- **Counting:** [Scoped ledger](scoped-accounting.json),
  [unfiltered analysis](detailed-analysis.md), and member notes for
  [safety](members/PatchBodyParametersSchema/migration.md),
  [layout](members/ConsistentPatchProperties/migration.md), and
  [immutable input](members/UnSupportedPatchProperties/migration.md).
- **Validation:** The assessed revision passed 757 distinct ARM tests,
  including 112 PATCH tests, and 20 injected PATCH controls. Two initial
  timeouts passed focused retries; six unrelated portable controls were
  excluded. Configured corpus activation was not assessed.
  [Validation receipt](runs/20261102-8a92389c9/local-validation.json).
- **Publication:** The [historical manifest](publication-manifest.json)
  applies to an earlier evidence commit; the
  [current receipt](current-publication-manifest.json) covers this refresh.
