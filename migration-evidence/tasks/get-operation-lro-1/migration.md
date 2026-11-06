# GetOperationMustNotBeLongRunning migration

## 1. Conclusion and scope

The TypeSpec linter is intentionally narrower than the Swagger linter. The retained rule, `@azure-tools/typespec-azure-resource-manager/no-get-lro`, reports HTTP GET operations recognized by Azure Core `getLroMetadata`. The proposed TCGC `no-get-lro` rule has been removed.

Accepted `Legacy.markAsLro` declarations without native LRO metadata are outside this rule. This adopts the compatibility-policy suggestion in [the review](https://github.com/Azure/typespec-azure/pull/5889#discussion_r4480977041), not an assertion that the two linters detect the same problems. Existing Legacy validation and SDK LRO generation remain unchanged.

The frozen corpus contains **four Swagger warnings that are no longer reported**: two CostManagement and two AppService Legacy-only GETs. All eight native-protocol ARM warnings remain unchanged. Consequently, this is **not a functionally equivalent migration** of the Swagger rule.

## 2. Actual coverage

The fresh final-candidate execution assessed **487/487 projects**, with **zero failed or unassessed projects**. Saved Swagger observations were integrity-verified and reused; Swagger was not regenerated.

| Observation                                                     | Swagger linter | TypeSpec linter |
| --------------------------------------------------------------- | -------------: | --------------: |
| Raw diagnostics, source scope                                   |              4 |               8 |
| Projects with diagnostics                                       |              2 |               4 |
| Diagnostics represented in the selected-version HTTP graph      |              4 |               4 |
| Original Swagger violations still detected by the retained rule |              4 |               0 |

The selected-version row is an inspected membership view, not a second compilation or a claim that the findings correspond. Its four TypeSpec findings concern different operations from the four Swagger violations. The other four native findings belong to source versions outside the selected Swagger version.

**Assessed coverage:** zero of the four observed Swagger warnings remain covered. Their retirement is intentional under the accepted Legacy exception. Eight native-protocol warnings are retained; all eight identities, authored targets and metadata checks match the previous joint-rule run. Equal selected-version totals do not establish parity.

See the [complete project inventory](arm-only-20261106/project-inventory.json), [coverage summary](arm-only-20261106/coverage-summary.json), and [operation-level analysis](arm-only-20261106/analysis.md).

## 3. Function-level comparison

| Behavior                                                                     | Result                      | Rationale                                                                                                                                                                          |
| ---------------------------------------------------------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HTTP GET with native LRO metadata, including customized/polling GETs         | Reported by the ARM rule    | Uses the existing Azure Core semantic API, not a separate response-status or decorator-pattern detector.                                                                           |
| Accepted common or language-scoped Legacy-only GET                           | Intentionally not reported  | Legacy compatibility exceptions do not require another GET-LRO warning/suppression. SDK generation still honors the accepted decorator.                                            |
| Authored raw `x-ms-long-running-operation` extension without native metadata | Not covered by the ARM rule | A raw extension is not proof of a native TypeSpec LRO protocol. No replacement detector was introduced.                                                                            |
| Synchronous GET or non-GET operation                                         | Not reported by this rule   | Preserves the rule's method and native-metadata prerequisites.                                                                                                                     |
| Explicit/implicit service boundary and authored suppression                  | Preserved                   | The unchanged ARM implementation resolves the operation directly and retains the existing service/suppression behavior.                                                            |
| Activation and ownership                                                     | One ARM rule; no SDK rule   | Registration, rulesets, references and release notes consistently remove the proposed SDK rule. The comparison explicitly enables the ARM rule.                                    |
| Existing Legacy validation and SDK LRO generation                            | Preserved                   | The focused regression compiles an accepted Legacy-only GET under SDK `all`, produces an SDK LRO, and has no Core LRO metadata. It fails on the removed warning before the change. |

## 4. Differences and disposition

The comparable unit below is an investigated operation/check, not a project-total coincidence.

| Project / semantic group                     | Swagger linter | TypeSpec linter | Disposition                                                                      |
| -------------------------------------------- | -------------: | --------------: | -------------------------------------------------------------------------------- |
| CostManagement: accepted Legacy-only GETs    |              2 |               0 | Intentional retirement of both original Swagger violations.                      |
| AppService: accepted Legacy-only GETs        |              2 |               0 | Intentional retirement of both original Swagger violations.                      |
| AppService: separate native-protocol GET     |              0 |               1 | Retained native guidance; not coverage of either retired AppService violation.   |
| BotService: native-protocol GET              |              0 |               1 | Retained native guidance.                                                        |
| Maps: native-protocol GET                    |              0 |               1 | Retained native guidance.                                                        |
| RecoveryServicesBackup: native-protocol GETs |              0 |               5 | One selected-version operation and four source-only/version-excluded operations. |

All differences are attributed in the [grouped appendix](arm-only-20261106/analysis.md), including exact source identities and saved Swagger input/document/path/verb attribution. There are no unexplained runtime differences.

## NOTES

- **Tested source:** Azure/typespec-azure [`75b9be3c28af0f36763b9511f25c193bde11675d`](https://github.com/Azure/typespec-azure/commit/75b9be3c28af0f36763b9511f25c193bde11675d), Core gitlink `3a87c089009146e1ce1201659c00f1179411a81f`. Tooling `402e3fb202e9a16f0a8c7dfc1b799098cfba879d`; specs `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`. The manifest records the actual loaded package versions and hashes. Native execution used Node `v26.13.0` and the specs' pnpm `12.6.0`.
- **Mapping:** one production ARM Swagger validator, `GetOperationMustNotBeLongRunning`, to one native ARM rule, `@azure-tools/typespec-azure-resource-manager/no-get-lro`. This establishes neither data-plane coverage nor coverage of every emitted-extension pattern.
- **Policy:** `scope: source`, `native-mode: target-only`, `baseline-policy: frozen-reference`, no filter/limit, concurrency 2. Source and selected Swagger version populations differ. The analyzer's `equivalence: not-determined` is unchanged; the reviewed conclusion is intentionally narrower/non-equivalent.
- **Directional differences:** project-total excess sums are Swagger 3 / TypeSpec 7. After operation/check attribution, unmatched observations are Swagger 4 / TypeSpec 8. AppService project overlap cannot cancel differences between unrelated operations. No count normalization or deduplication was used to claim parity.
- **Frozen baseline:** metadata commit `1c9d2b0e6a596754af1aa793b1906ff3c4ef2bd6`; baseline identity `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`. [Descriptor](arm-only-20261106/baseline-descriptor.json) and [recovery instructions](arm-only-20261106/recovery.md) identify the separately retained 51,932,501-byte Swagger archive and its SHA-256. Both standalone baseline verification and analyzer reuse/final integrity verification passed.
- **Controls:** 37 applicable portable harness controls passed; six fixtures requiring an unrelated resource-group rule were explicitly inapplicable, not passes. All 34 ARM-only injected semantic controls passed, including intentionally compliant common/language-scoped Legacy GETs, raw-extension boundaries, native GET positives, non-GET/synchronous contrasts, suppression and activation.
- **Local validation:** 13 canonical ARM cases, eight SDK Legacy cases and 15 central-ruleset cases passed (36 total). The 23-package build closure, root formatting, lint, Chronus verification and whitespace checks passed. [Validation receipt](arm-only-20261106/validation.json).
- **Provenance:** 15 source-audited tarballs, 2,875 packed files; all 487 worker entrypoint receipts verified against the selected artifacts. Separately verified all 180 installed SDK package files and the absence of the removed rule/registration. [Runtime verification](arm-only-20261106/runtime-verification.json).
- **Execution:** the analyzer completed at `2026-11-06T08:36:51.574Z`; its native execution interval was `08:06:38.915Z` to `08:34:31.995Z` (27 minutes 53 seconds), within the 7,200-second budget. Preparation and integrity verification are additional work, not native execution time.
- **Recovery/publication:** [asset inventory](arm-only-20261106/assets.json) identifies the packages, native observations and controls archives. Text publication replaces machine roots with role tokens and records original/published hashes; tarballs and the sealed baseline are unchanged. [Saved-observation replay](arm-only-20261106/replay.py) audits counts and correspondence; it is not fresh native execution. [Recovery](arm-only-20261106/recovery.md) separately describes full regeneration of the frozen comparison and reviewed report.
- **Recovered preparation failures:** the first ARM-only control adapter incorrectly expected an SDK entrypoint receipt; the corrected adapter passed without changing the rule. A resume guard was corrected to ignore ANSI formatting. Runtime verification distinguishes absent authored extensions from true emitted Swagger flags. An initial publication sanitizer failure was corrected by replacing the verified Node installation root; the partial archive was retained locally and excluded from publication. These were preparation/verification issues, not failed corpus projects.
- **Historical evidence:** the [previous joint-rule report](https://github.com/msyyc/typespec-azure/blob/611e4e7dbcd9698ff8bd6999c2aa7eda792a7790/migration-evidence/tasks/get-operation-lro-1/migration.md) and [operation findings](review-http-20261104/findings.json) remain available for the 8 ARM + 4 SDK comparison. Their joint-coverage conclusion is superseded by this report.
