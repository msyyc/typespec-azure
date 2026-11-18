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

These are individual reported diagnostics, not equivalent defects. The TypeSpec total contains only the selected rule. Corresponding suppressed or unsuppressed diagnostics from other owning rules were not captured, so their additional count is unknown. A source scan found 47 directives for one potentially overlapping rule; directives are not diagnostic counts.
[Scope and suppression evidence](scoped-assessment.md#suppression-and-runtime-limits).

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |            975 |           1,246 |

**Analysis:** The TypeSpec linter reports 271 more diagnostics, not 271 more defects. Five emitted-only discriminator checks and one optionality difference lack the same authored-input check; 21 representation findings need policy or aligned-emission review, and seven findings need route/version alignment. The count mechanisms are explained below; tested behavior and remaining coverage limits are in section 4.
[Assessment and member status](scoped-assessment.md).

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

The table counts **reported diagnostics**, using the same scope as section 2. Saved callbacks are linked to reports by exact project, document, rule, message and reported-path ancestry. All 1,057 callbacks have exactly one compatible saved report; their reporting collapse produces the known 975 diagnostics. No linter was rerun. [Attribution and reproduction](scoped-assessment.md#reported-diagnostic-attribution).

Differences are classified using project, exact PATCH route, check family and encoded property-path text. Equal keys are not proof of equivalent defects. A zero means no additional captured selected-rule diagnostic in that category, not that other owning rules or suppressed warnings are absent.

| Difference (with evidence)                                                                                | Swagger diagnostics | TypeSpec diagnostics for the same check | analysis                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------- | ------------------: | --------------------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Effective input](scoped-assessment.md#reported-diagnostic-attribution)                                   |                 138 |                                       0 | Read/Create-only input or an ancestor is excluded. The 165 Swagger callbacks become 138 reports; the intended input policy remains a review decision.                                                              |
| [Synthetic discriminator and optional input](scoped-assessment.md#reported-diagnostic-attribution)        |                   3 |                                       0 | Two reports concern emitted-only discriminators and one concerns effectively optional input. Three more discriminator callbacks contribute to the mixed report below. Review the required emitted-field policy.    |
| [Missing parents and leaves](detailed-analysis.md#parent-and-leaf-accounting)                             |                  52 |                                     175 | Swagger stops at missing parents; TypeSpec reports supported descendants. These are diagnostic counts, not counts of equivalent fixes.                                                                             |
| [Falsy defaults and arrays](scoped-assessment.md#count-reconciliation)                                    |                   0 |                                     185 | TypeSpec reports 128 falsy defaults and 57 additional array defaults. The broader policy remains a review decision.                                                                                                |
| [Recursive reference](detailed-analysis.md#recursive-reference-boundary)                                  |                   0 |                                      24 | The saved Swagger callback cannot inspect the recursive request children. The counterfactual control explains the boundary, not parity.                                                                            |
| [Source and operation scope](scoped-assessment.md#count-reconciliation)                                   |                   0 |                                       7 | These seven diagnostics have no identical saved PATCH route. Keep them counted; selected-version/operation alignment remains pending.                                                                              |
| [Resource and PATCH representation](detailed-analysis.md#representation-policy-boundaries)                |                   0 |                                      21 | Twelve resource-name findings need policy review; nine optional/default-free NetApp findings need aligned-emission review.                                                                                         |
| [Mixed authored and synthetic discriminator report](scoped-assessment.md#reported-diagnostic-attribution) |                   1 |                                       1 | One Swagger report combines three emitted-only checks with one shared authored check. Count the report once and retain the TypeSpec authored-field diagnostic; do not assign the whole report to missing coverage. |

**Count-only difference:** Outside the mixed report, 833 shared-key checks produce 781 Swagger reports versus 833 TypeSpec diagnostics: a further difference of `781 - 833 = -52`. This is reporting multiplicity for already-diagnosed checks, not 52 missing defects.

**Raw-count reconciliation:** `975 - 1,246 = 138 + 3 + (52 - 175) - 185 - 24 - 7 - 21 + (1 - 1) - 52 = -271`.
All reported diagnostics are accounted for. The original 82-callback reporting reduction comprises 27 excluded-input callbacks, 52 shared-key callbacks and three callbacks in the mixed report. This arithmetic does not settle the identified policy questions, version alignment or the unmeasured owning-rule/suppression count.
[Project directions and exact targets](scoped-project-differences.md).

## 4. Function-level coverage

| Behavior                                                        | Result                                      | analysis                                                                                                                                                                                                |
| --------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Required/default PATCH input and optional default-free controls | Covered for supported authored input        | Falsy and array defaults extend Swagger behavior; emitted optionality is not aligned. [Injected controls](runs/20261102-8a92389c9/controls.json)                                                        |
| Read/Create-only input and explicit visibility overrides        | Covered under the TypeSpec input policy     | The Swagger linter can inspect fields excluded from effective PATCH input. [Examples](fresh-examples.md#excluded-input)                                                                                 |
| Root immutable fields and unrelated nested names                | Covered for tested authored input           | Read-only reference siblings can produce different Swagger findings. [Evidence](fresh-examples.md#read-only-reference-siblings)                                                                         |
| Partial encoded layout, inheritance and supported nested models | Covered for tested shapes                   | Parent/leaf counts differ; associated-resource name policy is unresolved. [Evidence](scoped-assessment.md#count-reconciliation)                                                                         |
| Synthesized emitted discriminator properties                    | Missing from the authored-field check       | Five Swagger callbacks concern emitted fields with no authored property. The required emitted policy remains a reviewer decision. [Evidence](detailed-analysis.md#effective-input-and-synthetic-fields) |
| Unions, tuples, transport models and ambiguous resource layouts | Full emitted-shape coverage not established | The TypeSpec linter declines or limits traversal in these cases. Supported sibling safety checks remain separate. [Fixture evidence](evidence-details.md#layout-and-emission)                           |
| Existing owning rules and authored suppressions                 | Diagnostic counts not captured              | The `arm-resource-patch` layout branch may overlap; saved target-only diagnostics do not capture its warnings. [Evidence](scoped-assessment.md#suppression-and-runtime-limits)                          |

## NOTES

- **Inputs:** Assessed implementation `8a92389c9`, core `cefb035e7721`,
  specs `2cd3c5dd6d00`; this is a report-only reuse of saved observations.
  The later PR head has a different compiler gitlink and has not been assessed
  by this corpus. [Provenance](fresh-evidence.md#november-2-final-review-fix-run).
- **Counting:** [Scoped ledger](scoped-accounting.json),
  [reported-diagnostic attribution](reporting-accounting.json),
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
