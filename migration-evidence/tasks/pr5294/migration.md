# ARM PATCH property migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/no-unsafe-patch-body-properties`
is assessed against the Swagger linters
[PatchBodyParametersSchema](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-body-parameters-schema.md),
[ConsistentPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/consistent-patch-properties.md),
and [UnSupportedPatchProperties](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/un-supported-patch-properties.md).
Original migration linter PR: [Azure/typespec-azure#5294](https://github.com/Azure/typespec-azure/pull/5294).

## 2. Coverage

The final source-fix run assessed all 487 frozen projects successfully: no failed
or unassessed projects. Swagger reuses the selected-version baseline; TypeSpec
uses the unprojected source program with this rule explicitly enabled.

The configured TypeSpec total is **1,413**. This comparison excludes 91 evidenced
client-only/other-version observations and 76 generic resource-lifecycle findings
outside the original Swagger immutable-field selector: `1,413 - 91 - 76 = 1,246`.
These exclusions are disjoint. All 1,337 historical original-policy diagnostics
were reproduced exactly, including their source targets and multiplicity; the
91 population exclusions were therefore revalidated, not blindly reapplied.
[Current accounting](runs/20261124-qualified/accepted-assessment.json).

The table counts individual reported diagnostics, not equivalent defects.
Other owning rules' suppressed and unsuppressed warnings were not captured;
their additional count is unknown, not zero. Existing suppression directives
do not establish replacement coverage.
[Scope and limits](scoped-assessment.md#suppression-and-runtime-limits).

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |            975 |           1,246 |

**Analysis:** Original-policy observations remain 975 / 1,246; the 76 new
lifecycle findings are not credited as improved Swagger coverage. A lifecycle-only
replacement initially lost 52 reserved-field warnings. The final implementation
restores all 52 while retaining the broader lifecycle check. Five emitted-only
discriminator checks and one optionality difference still lack the same authored
check; 21 representation findings and seven route/version findings remain policy
or alignment limits. Neither the unchanged scoped total nor the larger raw total
establishes parity. [Corpus-driven decision](runs/20261124-qualified/assessment.md).

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

The table uses section 2's original-policy scope. Exact per-project diagnostic
preservation permits reuse of the saved semantic investigations, not relabeling
an old run as current. Swagger's 1,057 callbacks still map to 975 final reports
by exact project, document, rule, message and reported-path ancestry.
[Attribution](scoped-assessment.md#reported-diagnostic-attribution).

Groups use project, exact PATCH route, check family and encoded property-path
text, not equivalent-defect identities. A zero means no additional captured
selected-rule diagnostic in that category; other owning diagnostics remain
unmeasured. The 76 broader lifecycle findings are excluded here and retained in
the [current check-exclusion ledger](runs/20261124-qualified/accepted-assessment.json).

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
All scoped reported diagnostics are accounted for. The 82-callback reporting
reduction comprises 27 excluded-input, 52 shared-key and three mixed-report
callbacks. The separate 52 warnings restored after the rejected redesign are
not this reporting reduction and must not be added to the reconciliation.
The accounting does not settle policy, version alignment or unmeasured warnings.
[Project directions and exact targets](scoped-project-differences.md).

## 4. Function-level coverage

| Behavior                                                        | Result                                      | analysis                                                                                                                                                                                                                                                                    |
| --------------------------------------------------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Required/default PATCH input and optional default-free controls | Covered for supported authored input        | Falsy and array defaults extend Swagger behavior; emitted optionality is not aligned. [Injected controls](runs/20261102-8a92389c9/controls.json)                                                                                                                            |
| Read/Create-only input and explicit visibility overrides        | Covered under the TypeSpec input policy     | The Swagger linter can inspect fields excluded from effective PATCH input. [Examples](fresh-examples.md#excluded-input)                                                                                                                                                     |
| Root immutable fields and unrelated nested names                | Reserved-field safeguard retained           | Missing/default/incorrect lifecycle annotations cannot retire the ARM restriction. All 52 warnings lost by the first candidate are restored; unrelated nested names remain allowed. [Decision and regressions](runs/20261124-qualified/assessment.md#reserved-field-policy) |
| Generic resource lifecycle restrictions                         | Broader tested TypeSpec policy              | 76 new findings concern other matched resource properties lacking Update. They indicate modeled-contract conflicts, not 76 proven service defects or original-member coverage. [Examples and limits](runs/20261124-qualified/assessment.md#generic-lifecycle-policy)        |
| Partial encoded layout, inheritance and supported nested models | Covered for tested shapes                   | Parent/leaf counts differ; associated-resource name policy is unresolved. [Evidence](scoped-assessment.md#count-reconciliation)                                                                                                                                             |
| Synthesized emitted discriminator properties                    | Missing from the authored-field check       | Five Swagger callbacks concern emitted fields with no authored property. The required emitted policy remains a reviewer decision. [Evidence](detailed-analysis.md#effective-input-and-synthetic-fields)                                                                     |
| Unions, tuples, transport models and ambiguous resource layouts | Full emitted-shape coverage not established | The TypeSpec linter declines or limits traversal in these cases. Supported sibling safety checks remain separate. [Fixture evidence](evidence-details.md#layout-and-emission)                                                                                               |
| Existing owning rules and authored suppressions                 | Diagnostic counts not captured              | The `arm-resource-patch` layout branch may overlap; saved target-only diagnostics do not capture its warnings. [Evidence](scoped-assessment.md#suppression-and-runtime-limits)                                                                                              |
| Recursive Record values and inferred response filtering         | Explicit traversal boundaries tested        | Record values are not expanded; named siblings remain checked. HTTP-inferred responses can already omit Query-only properties. [Canonical gap controls](runs/20261124-qualified/assessment.md#canonical-regressions)                                                        |

## NOTES

- **Inputs:** Published source `9e413f4725`, core `ce2f9bcdb494`,
  specs `2cd3c5dd6d00`; the new final run is bound to the four working-tree
  file hashes and reconciled with that commit. The pinned Swagger baseline
  is unchanged. [Run and closure](runs/20261124-qualified/manifest.json);
  [commit reconciliation](runs/20261124-qualified/source-commit-reconciliation.json).
- **Counting:** [Current raw/scoped/exclusion ledger](runs/20261124-qualified/accepted-assessment.json),
  [historical population ledger](scoped-accounting.json),
  [reported-diagnostic attribution](reporting-accounting.json),
  [unfiltered analysis](detailed-analysis.md), and member notes for
  [safety](members/PatchBodyParametersSchema/migration.md),
  [layout](members/ConsistentPatchProperties/migration.md), and
  [immutable input](members/UnSupportedPatchProperties/migration.md).
- **Validation:** The final candidate passed 112 canonical rule tests,
  ARM build, root format/lint, 36 injected PATCH controls, 37 applicable portable
  controls, 18 before/rejected/final gap assertions and the actual guide snippets
  (five warnings / zero warnings). Six unrelated portable fixtures were
  inapplicable. Configured whole-corpus activation and other owning warnings
  were not assessed. [Receipts and retained failures](runs/20261124-qualified/assessment.md#validation-and-recovery).
- **Publication:** The [historical manifest](publication-manifest.json)
  applies to an earlier evidence commit; the
  [current receipt](current-publication-manifest.json) covers this refresh.
