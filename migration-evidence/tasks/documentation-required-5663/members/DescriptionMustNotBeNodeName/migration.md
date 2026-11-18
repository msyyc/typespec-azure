# DescriptionMustNotBeNodeName migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-azure-core/documentation-required` is assessed against [DescriptionMustNotBeNodeName](https://github.com/Azure/azure-openapi-validator/blob/main/docs/description-must-not-be-node-name.md). Original migration linter PR: [Azure/typespec-azure#5663](https://github.com/Azure/typespec-azure/pull/5663).

## 2. Coverage

The November 18 official-rule run assessed **490/490 frozen ARM projects**, with **zero failures or exclusions**.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------- | --------------- |
| Reported diagnostics | 88,500         | 8,355           |

TypeSpec includes **7,852 configured + 503 captured suppressed** `uninformative` diagnostics. Suppression observation covers every successful program. The sibling's 32 blank findings and 11,260 existing missing-documentation findings are excluded, not treated as missing attribution. [Scoped totals](../../runs/native-20261118/scoped-summary.json) and [individual diagnostic identities](../../runs/native-20261118/native-quality.jsonl) preserve the breakdown.

**Assessed coverage:** All 107 Swagger-affected projects have native name-check findings; TypeSpec affects 149 projects, including 42 TypeSpec-only projects. The configured-only analyzer had two Swagger-only projects, Commerce and PolicyTrackedResourcesApi; captured suppressed findings account for both. [Every one-sided project and source witness](../../runs/native-20261118/investigation.json) is retained.

**Analysis:** The official authored-name adaptation is exercised by discriminating injected controls and the fresh corpus. This establishes execution and project-level overlap, not equivalent diagnostic targets. Source/emission/version scope and reference multiplicity differ; comparable-defect coverage remains unassessed. See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

The following complete project partition retains the saved production Swagger observations and includes configured plus captured suppressed TypeSpec findings.

| Difference (with evidence)                                                                     | Swagger diagnostics | TypeSpec diagnostics for the same check | analysis                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------- | ------------------- | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SQL reference/input contexts](../../evidence-details.md#current-count-investigation)          | 65,199              | 613                                     | ColumnDataType has 3,774 validator occurrences at 34 member paths and 34 captured source diagnostics. Only 34 occurrences explicitly identify the reported document; the remaining input-fallback observations cannot be assigned exact source files. Repetition is evidenced, but not a full causal partition of SQL's 64,586 gap. |
| [Network source/emission differences](../../evidence-details.md#current-count-investigation)   | 17,221              | 936                                     | All programs compile, unlike the historical excluded Network run. Raw emitted/reference contexts and source semantic instances differ; exact allocation of 16,285 remains unresolved.                                                                                                                                               |
| [Other projects, both directions retained](../../runs/native-20261118/per-project-counts.json) | 6,080               | 6,806                                   | ContainerApps is 192/255 and Reservations 138/185. Source-only/client/common declarations, removed versions and emitted names have witnesses, not exhaustive normalized matching. The other-project net is -726.                                                                                                                    |

**Raw-count reconciliation:** **`88,500 - 8,355 = 64,586 + 16,285 - 726 = 80,145`**. Across individual projects, **22 have more Swagger findings (81,167 excess)**, **108 have more TypeSpec findings (1,022 excess)** and **360 are equal**. The full 80,145 net remains incompletely allocated by cause; do not call it 80,145 missing native checks.

There are **88,491 enum-metadata occurrences and nine other definition occurrences**. Conservative grouping gives 7,841 project-plus-JSON-path keys and 8,351 native source-location keys, but neither grouping establishes equivalent defects. The Swagger dataset records **80,659 input-fallback** and **7,841 reported-document** observations; input filenames must not be relabeled as proven diagnostic source documents. Four repeated native source identities are retained as individual semantic diagnostic occurrences.

The [source witness inventory](../../runs/native-20261118/investigation.json) includes all 42 one-sided projects. Directly inspected examples include Advisor's removed PriorityName declaration, ApiManagement/EventHub/KeyVault/Storage client compatibility types, imported common declarations, IoTOperations version members, Fleet's qualified model names, Manufacturing's resource-key naming, and RecoveryServicesBackup's constant path parameters. These are representative source-policy explanations, not a complete per-finding emitted correspondence. Preserve the reviewed policy; further exact correspondence is a follow-up, not justification to equalize raw counts.

## 4. Function-level coverage

| Behavior                                                                          | Result                                                      | analysis                                                                                                                                                                                                                  |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Trimming, period removal, case-insensitive equality and placeholder `description` | Verified by canonical/injected controls                     | Violating and meaningful controls exercise the actual official linter. [Current validation](../../evidence-details.md#current-run-validation).                                                                            |
| Enum members, named/unnamed string union variants and authored keys               | Verified tests and corpus targets                           | Exact source locations are retained; semantic instances sharing locations are not silently deduplicated.                                                                                                                  |
| Authored operation names/effective HTTP verbs; HTTP and multipart names           | Covered by canonical tests                                  | Public metadata policies remain separate from ordinary-property JSON naming. [Fixture mapping](../../evidence-details.md#implementation-and-fixture-mapping).                                                             |
| JSON-renamed ordinary properties                                                  | Verified policy adaptation                                  | Injected wire-name compliance and authored-name violation controls pass. Historical JSON-name outcomes are not current parity claims. [Injected controls](../../runs/native-20261118/documentation-control-results.json). |
| Status-code name repetition                                                       | Exempt by reviewed policy                                   | Blank checks remain independently applicable.                                                                                                                                                                             |
| Source suppression and project defaults                                           | Suppressions captured; default activation separately tested | Direct and ancestor controls pass in both modes. Target-only corpus execution does not assess each project's default activation.                                                                                          |
| Generated names and universal emitted reachability                                | Outside source policy / correspondence unresolved           | No emitter reconstruction or source-to-output equivalence percentage is claimed.                                                                                                                                          |

## NOTES

- **Inputs and replay:** Official head `2c6596126f281d78ca06fb23afc9ef8ab37684b8`, core `8574d5453f7bf9a07dc09bd41edac579af71d94b`, specs `6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc`; [new-run inputs, archives and replay](../../runs/native-20261118/README.md). Swagger is reused, not regenerated.
- **Historical evidence:** [Original investigation at 3753a319](https://github.com/Azure/typespec-azure/blob/3753a319f32f3926005536029f9ff32b94f3c905/packages/typespec-lintdiff/test/fixtures/DescriptionMustNotBeNodeName/migration.md) and [historical appendix](../../evidence-details.md#historical-populations-and-exclusions) retain the earlier 462-successful-project configured snapshot. It is superseded for current counts, not summed with this run.
- **Validation and CI:** [Current controls and limits](../../evidence-details.md#current-run-validation) are separate from CI compatibility. [Suppression draft #48090](https://github.com/Azure/azure-rest-api-specs/pull/48090) is unchanged and its proposed annotations are not included in this corpus.
