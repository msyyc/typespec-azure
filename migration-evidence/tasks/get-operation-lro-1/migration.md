# GetOperationMustNotBeLongRunning migration

## 1. Scope

The TypeSpec linter `@azure-tools/typespec-client-generator-core/no-get-lro` is assessed against Swagger linter rule [`GetOperationMustNotBeLongRunning`](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/docs/get-operation-must-not-be-long-running.md). Original migration linter PR: [Azure/typespec-azure#5889](https://github.com/Azure/typespec-azure/pull/5889).

## 2. Coverage

The final execution assessed **487/487 frozen projects**, with **zero failed or unassessed projects**. The comparison explicitly enables the TypeSpec rule in source mode and reuses the original production ARM Swagger observations.

These are individual reported diagnostic occurrences: four configured TypeSpec warnings, zero excluded current warnings, and no additional captured suppressed diagnostics. All four Swagger-matching targets have an observed unsuppressed TypeSpec warning. The worker honors authored suppressions but does not capture suppressed diagnostics; an exhaustive suppression-inclusive total for other owning checks remains unassessed.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |              4 |               4 |

**Analysis:** The four observations correspond to four accepted Legacy-marked GET operations in CostManagement and AppService. Exact source operation, HTTP path/verb and saved Swagger document/JSON-path evidence establishes these matches, not equal totals alone. The rule does **not** cover raw LRO extension/options declarations without an accepted Legacy marker. Native-only GET LRO enforcement is outside this implementation.

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ) and the [scoped assessment](legacy-marker-20261125/assessment.json).

## 3. Why diagnostic counts differ

There are no differing projects or unmatched current diagnostic groups in this observed comparison. Each of the four TypeSpec warnings maps to one saved Swagger occurrence; no deduplication or count normalization is used. Both directional project excesses are zero.

**Raw-count reconciliation:** **4 - 4 = 0**, with zero unexplained residual. The [operation-level appendix](legacy-marker-20261125/analysis.md#current-correspondence) accounts for all four findings.

The previous eight ARM warnings concerned native-only GET operations, not these Swagger violations. They are intentionally absent from the new predicate and are not subtracted from its four configured warnings or credited as Swagger coverage. Their [historical-target ledger](legacy-marker-20261125/analysis.md#native-only-boundary) preserves this distinction.

Matching observed counts do not establish complete property-level coverage: the [raw-extension boundary](legacy-marker-20261125/analysis.md#raw-extension-boundary) remains visible, and current Swagger emission was not regenerated.

## 4. Function-level coverage

| Behavior                                                         | Result                                              | analysis                                                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accepted common Legacy marker on GET                             | Covered in the observed corpus                      | Four exact matches, all in the selected-version HTTP graph; saved emitted LRO flags are true and authored raw flags/options absent. [Evidence](legacy-marker-20261125/analysis.md#current-correspondence).                                                                              |
| Positive/negative/options language scopes; repeated declarations | Covered by TypeSpec controls                        | Uses existing accepted scoped state, warns without a selected emitter and reports once per authored operation. Empty, ineffective scope data is ignored. The four real matches use common scope. [Controls](legacy-marker-20261125/analysis.md#controls-and-regressions).               |
| Native-only GET LRO metadata                                     | Outside the agreed predicate                        | Eight former ARM findings are absent; no SDK-context, Core metadata or response-pattern classifier is added. [Boundary](legacy-marker-20261125/analysis.md#native-only-boundary).                                                                                                       |
| Raw LRO flag/options without an accepted marker                  | Missing from the new check                          | Property-level Swagger coverage is broader; injected controls return no target warning. This PR implements the explicitly selected marker-only guideline, not full extension parity. [Analysis](legacy-marker-20261125/analysis.md#raw-extension-boundary).                             |
| Invalid/ineffective marker; synchronous/unmarked GET; non-GET    | Existing validation or compliant behavior preserved | Invalid markers retain the existing SDK warning, native-ineffective markers retain the existing error, and neither becomes accepted state. Accepted POST/PUT/PATCH/DELETE markers do not trigger the GET rule. [Evidence](legacy-marker-20261125/analysis.md#controls-and-regressions). |
| Authored suppression and SDK generation                          | Preserved                                           | New-rule suppression removes its warning and preserves the SDK LRO; unrelated Legacy suppression does not erase the new warning. This is behavior evidence, not exhaustive suppressed corpus capture. [Evidence](legacy-marker-20261125/analysis.md#suppression-accounting).            |
| Service/template targets and activation                          | Covered by canonical/injected controls              | Explicit services recurse; implicit global services do not sweep helper namespaces. Concrete template-derived operations are checked. Client-SDK and TCGC `all` enable the rule; ARM/data-plane/C# presets do not. [Validation](legacy-marker-20261125/validation.json).                |

## NOTES

- **Inputs:** Assessed source [`65c1ca5e`](https://github.com/Azure/typespec-azure/commit/65c1ca5e24d9bc72d768f4c5d3e437507b0764b9), Core `a1664df866494abea6d51767c60ea9b627903abd`, tooling `702ac1601ec62a1273872d4a12e6fd05b9ebda60`, specs `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`. Later source commit `50dace214e7de8473c75d441db71eced78ccb15a` only clarifies the changeset; assessed payloads are unchanged. This is a fresh TypeSpec run against unchanged historical Swagger, not a current-emission comparison. [Manifest](legacy-marker-20261125/manifest.json).
- **Counting:** Source/target-only/frozen-reference, no filter or limit; full-population default activation is not assessed. Suppression limits and zero exclusions are in [assessment](legacy-marker-20261125/assessment.json), [configured observations](legacy-marker-20261125/coverage-summary.json) and [project inventory](legacy-marker-20261125/project-inventory.json).
- **Validation:** 1,971 SDK cases passed across the full suite and isolated retry of one startup timeout; two intentional skips. Rulesets: 20 passed. Portable controls: 37 passed, six unrelated fixtures excluded upfront; selected controls: 50 passed. Builds, regeneration, formatting/lint/spelling, Chronus, whitespace and three exact documentation examples passed. `validate:pr` used skip-build/skip-test with recorded supplements, not an unrestricted root run. [Receipt](legacy-marker-20261125/validation.json).
- **Recovery:** Twenty source-audited tarballs/3,332 payload files and all 487 successful worker receipts verified. [Assets](legacy-marker-20261125/assets.json), [recovery and replay](legacy-marker-20261125/recovery.md). Prior [ARM-only evidence](arm-only-20261106/analysis.md) and [joint-rule findings](review-http-20261104/findings.json) remain historical, not current conclusions.
