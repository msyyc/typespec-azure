# XmsClientName migration

## 1. Scope

The TypeSpec linter
`@azure-tools/typespec-client-generator-core/no-redundant-client-name`
is assessed against Swagger linter rule
[`XmsClientName`](https://github.com/Azure/azure-openapi-validator/blob/405e6f094fa8280e05af23327845f6202a8edc65/packages/rulesets/src/spectral/functions/Extensions/xms-client-name.ts).

## 2. Coverage

All 490 frozen ARM projects were assessable, with 652 retained Swagger inputs.
No project failed or remained unassessed. The comparison uses unprojected
TypeSpec source and the baseline's selected latest-version Swagger.
Counts are individual configured findings: no mixed-rule exclusions or count
normalization apply. Authored suppressions remain honored; no exhaustive
pre-suppression corpus capture was made. The focused suppressed control is not
added to corpus totals.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |              0 |             141 |

**Assessed coverage:** the TypeSpec linter reported 141 no-effect applications in
32 projects. The Swagger linter had zero observed production
findings after confirmed registration and successful baseline execution.
All observed differences are source-version or SDK-application representation
differences, detailed below. Strict extension equality and SDK no-effect naming
are different predicates; exact equivalent-defect counts and coverage percentages
remain unassessed. This ARM run is not complete SDK or data-plane validation.

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

The table partitions every captured TypeSpec diagnostic once by evidenced cause.
The columns retain raw occurrences for the mapped naming intent, not asserted
one-to-one identical predicates. Every project and exact target is listed in
[grouped evidence](grouped-differences.md).

| Difference (with evidence)                                                                  | Swagger diagnostics | TypeSpec diagnostics for the same check | analysis                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------- | ------------------: | --------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Repeated body-name applications](grouped-differences.md#advisor-body-repeat)               |                   0 |                                      38 | The retained exact body objects have one name and no x-ms-client-name. Source application multiplicity and SDK scopes are not emitted. Preserve meaningful remaining names when cleaning duplicates. |
| [Copied-property SDK repeats](grouped-differences.md#cdn-copy-source-repeats)               |                   0 |                                      30 | The reported copy-target applications add no naming effect beyond source-property applications. Preserve effective source names and independent scopes.                                              |
| [Duplicate scoped applications](grouped-differences.md#aks-duplicate-enabled)               |                   0 |                                      35 | Each application is independently removable while another meaningful rename remains. Do not delete all warned copies together.                                                                       |
| [Identity SDK name without an extension](grouped-differences.md#dns-identity-name)          |                   0 |                                       1 | The common override equals the source spelling; a separate meaningful C# override remains. The retained Swagger has no matching extension.                                                           |
| [Inherited-property SDK repeats](grouped-differences.md#consumption-inherited-scope-repeat) |                   0 |                                      12 | Derived references address inherited properties, not independent authored property declarations. Retain every raw removable-application warning.                                                     |
| [Older-version source](grouped-differences.md#advisor-removed-assessment)                   |                   0 |                                      13 | Source contains removed targets that are absent from selected latest-version Swagger. Retain the source-profile observations; a same-version assessment remains unassessed.                          |
| [Scoped repeat of a case-only rename](grouped-differences.md#containerapps-scoped-repeat)   |                   0 |                                       1 | Only the extra language-scoped application is ineffective. The meaningful common case-only rename does not satisfy strict Swagger equality.                                                          |
| [Shadowed SDK applications](grouped-differences.md#billing-shadowed-inherited-overrides)    |                   0 |                                      11 | A later effective application makes an earlier application ineffective, even when their text differs. Cleanup must retain the intended winning name.                                                 |

**Raw-count reconciliation:** Swagger total - TypeSpec total =
0 - 141 = - 38 - 30 - 35 - 1 - 12 - 13 - 1 - 11 = -141. The terms follow table order.
The unresolved count residual is zero. There are no opposing project differences
to cancel. [The recount](receipts/saved-observation-reanalysis.json) retains all
project sets, raw/source-key counts, signed/absolute gaps and undefined relative
gaps when the Swagger denominator is zero. Cleanup proposals are not approved
spec changes; deleting every independently removable duplicate at once can
change a meaningful SDK name.

## 4. Function-level coverage

| Behavior                                                           | Result                                                          | analysis                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------ | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No-effect property and operation-parameter overrides               | Covered by native-contract controls                             | Actual packed [property](controls/redundant-property/output.json) and [parameter](controls/redundant-parameter/output.json) controls fire; [compliance](controls/compliant-and-real-case-renames/output.json) preserves real/case-only renames.                                                                |
| Scoped fallback, exact naming and wire independence                | Covered by native-contract controls                             | [Scope](controls/scoped-repeat-and-reset/output.json), [exact](controls/exact-policy-effect-and-repeat/output.json) and [wire](controls/wire-name-independence/output.json) controls retain meaningful effects.                                                                                                |
| Friendly and dependent naming                                      | Covered in the declared default TCGC context                    | [Dependent-name](controls/dependent-friendly-effect/output.json) and [fallback](controls/friendly-fallback/output.json) controls preserve real naming effects. Emitter-option limits and the corrected source review are in [supporting evidence](evidence-details.md#friendly-fallback-and-dependent-naming). |
| Authored application identity and suppression                      | Covered by focused controls; corpus suppression capture limited | [Copied applications](controls/authored-copy-count/output.json) and [suppression](controls/authored-suppression/output.json) are tested through the registered packed rule.                                                                                                                                    |
| Default versus library-all activation                              | Assessed separately from the full run                           | Three central presets remain disabled; library all remains active. See [activation evidence](evidence-details.md#activation-and-actual-artifacts).                                                                                                                                                             |
| Literal extension equality and same-version Swagger correspondence | Not claimed as the native policy                                | The user-directed SDK no-effect contract intentionally differs. [All real-spec differences](grouped-differences.md) retain source/version and predicate limits.                                                                                                                                                |
| Complete SDK/data-plane and every emitter configuration            | Unassessed                                                      | The full corpus is ARM; discriminating SDK controls do not establish exhaustive production prevalence.                                                                                                                                                                                                         |

## NOTES

- **Inputs:** snapshot `d065102fa52bf69b680f08016fc049d7185b7c22`,
  core `41e2a4e70f0ea49ee52fa9d0d6d3d9c698c6ac08`, specs
  `6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc`; fresh target-only source run
  against frozen Swagger. [Manifest](runs/full-native-coverage/manifest.json),
  [claim map](claim-map.json), [identities and recovery](recovery.md).
- **Validation:** required changed-file tests 85/85; target injected controls
  16/16; portable controls 37 passed and six predeclared inapplicable skips.
  Earlier timeout attempts remain failed, with unproven cause.
  [Detailed validation](evidence-details.md#validation-and-recovery-history).
- **Source publication:** canonical native commit
  `c06d3a4a7ed1bb2cb417c76c6348624472c0c3ad` is pushed. Its complete tree equals
  the assessed snapshot tree. Independent source and artifact/report reviews
  passed. The native commit contains exactly the 16 reviewed task files.
- **Remaining gates:** durable evidence/assets, verified published-checkout
  recovery, native PR, separate A/B review, integration and CI remain pending.
  Source publication alone does not establish migration acceptance.
