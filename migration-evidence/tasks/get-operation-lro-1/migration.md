# GetOperationMustNotBeLongRunning migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-client-generator-core/no-get-lro` is assessed against Swagger linter [`GetOperationMustNotBeLongRunning`](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/docs/get-operation-must-not-be-long-running.md). Original migration linter PR: [Azure/typespec-azure#5889](https://github.com/Azure/typespec-azure/pull/5889).

## 2. Coverage

The assessment completed **487/487 frozen projects**, with **zero failed or unassessed projects**. It explicitly enables the TypeSpec rule in source/target-only mode and reuses the saved production ARM Swagger observations.

Reported diagnostics are individual occurrences for this check: four configured TypeSpec warnings, zero excluded current warnings and zero additional captured suppressed findings. All four matching targets actually report an unsuppressed warning. The worker honors suppressions but does not capture suppressed diagnostics; exhaustive suppression-inclusive totals for other owning checks remain unassessed. [Counting evidence](legacy-marker-opt-in-20261125/analysis.md#counting-and-suppression).

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |              4 |               4 |

**Analysis:** All four observed Swagger findings have an individually matched TypeSpec warning on an accepted Legacy-marked GET. Raw LRO flag/options properties without an accepted marker remain missing from this predicate. Native-only GET LRO metadata is outside the selected check. Equal totals do not establish complete property-check coverage or an equivalent-defect percentage.

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).

## 3. Why diagnostic counts differ

There are no differing projects or unmatched current diagnostic groups under section 2's inclusion policy. Each included source warning corresponds to one distinct saved Swagger occurrence; no normalization or deduplication is applied. Both directional project excesses are zero. [Exact correspondence](legacy-marker-opt-in-20261125/analysis.md#current-correspondence).

**Raw-count reconciliation:** **4 - 4 = 0**, with zero unexplained residual and no count-only adjustment. Historical native-only warnings are not current excluded diagnostics and do not enter either total; their [separate ledger](legacy-marker-opt-in-20261125/analysis.md#native-only-boundary) preserves that boundary.

The [raw-extension limitation](legacy-marker-opt-in-20261125/analysis.md#raw-extension-boundary) is evidenced missing behavior, not an observed one-sided corpus occurrence or an approved retirement of the Swagger property check.

## 4. Function-level coverage

| Behavior                                                             | Result                                              | analysis                                                                                                                                                                                                                                                                           |
| -------------------------------------------------------------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accepted common Legacy marker on GET                                 | Covered in the observed corpus                      | Four exact matches in the selected-version HTTP graph, with saved LRO flags and no source-authored raw flag/options. [Evidence](legacy-marker-opt-in-20261125/analysis.md#current-correspondence).                                                                                 |
| Positive/negative/options scopes and repeated markers                | Covered by TypeSpec controls                        | Any effective accepted scope can warn without its emitter selected; one warning per operation. Empty scope keys do not trigger the rule. Real matching projects use common scope. [Controls](legacy-marker-opt-in-20261125/analysis.md#controls-and-activation).                   |
| Raw LRO flag/options without an accepted marker                      | Missing from this predicate                         | The Swagger property check is broader. Raw-only controls have no target warning; substitute owning-check coverage is not credited without captured attributed evidence. [Analysis](legacy-marker-opt-in-20261125/analysis.md#raw-extension-boundary).                              |
| Native-only GET LRO metadata                                         | Outside the user-selected check                     | Eight historical source findings are absent, not replacements for the four Swagger findings. No native-only detector or follow-up issue is introduced. [Boundary](legacy-marker-opt-in-20261125/analysis.md#native-only-boundary).                                                 |
| Invalid/ineffective marker; unmarked GET; accepted non-GET marker    | Existing validation or compliant behavior preserved | Rejected markers retain their existing warning/error and do not produce this lint. Accepted POST/PUT/PATCH/DELETE markers remain allowed. [Controls](legacy-marker-opt-in-20261125/analysis.md#controls-and-activation).                                                           |
| Authored suppression, SDK generation and service/template boundaries | Covered by canonical/injected controls              | Suppression of this rule preserves the approved SDK LRO; another Legacy suppression does not suppress it. Authored operation identity and helper/service isolation remain tested. [Evidence](legacy-marker-opt-in-20261125/analysis.md#counting-and-suppression).                  |
| Client-SDK default and explicit activation                           | Opt-in behavior verified by controls                | Client-SDK registers `false`; SDK `all` and explicit enablement still activate the rule. The corpus explicitly enables it and does not assess full-population default activation. [Controls and authorization](legacy-marker-opt-in-20261125/analysis.md#controls-and-activation). |

## NOTES

- **Inputs:** Assessed source [`c67b521`](https://github.com/Azure/typespec-azure/commit/c67b521bc0166f11f492afb3366da29793ebbac9), Core `123e997958ced3b632caa0a4486e306d1487ca82`, tooling `702ac1601ec62a1273872d4a12e6fd05b9ebda60`, specs `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`. This is a fresh TypeSpec run against unchanged historical Swagger, not current-emission equality. Later head `4c1a337a01268c504b28508efaf4e0b4a7f29190` adds unrelated documentation tooling only; the assessed payloads are unchanged. [Manifest](legacy-marker-opt-in-20261125/manifest.json), [applicability](legacy-marker-opt-in-20261125/assessment.json).
- **Counting:** Source/target-only/frozen-reference, no filter or limit. [Configured observations](legacy-marker-opt-in-20261125/coverage-summary.json), [scoped accounting/exclusion ledger](legacy-marker-opt-in-20261125/assessment.json), [complete project inventory](legacy-marker-opt-in-20261125/project-inventory.json).
- **Validation:** Required local checks and the full comparison passed; the root validation's build/test/regeneration skips have separate executed supplements. CI at head `4c1a337` was pending when inspected, not awaited or inferred from local results. [Detailed receipt](legacy-marker-opt-in-20261125/validation.json), [CI snapshot](legacy-marker-opt-in-20261125/ci.json), [recovery/assets/replay](legacy-marker-opt-in-20261125/recovery.md).
