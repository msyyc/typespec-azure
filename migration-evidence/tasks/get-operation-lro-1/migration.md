# GetOperationMustNotBeLongRunning → ARM and SDK no-get-lro

## 1. Conclusion and scope

The ARM and SDK TypeSpec linter rules `no-get-lro` adapt Swagger linter rule
[`GetOperationMustNotBeLongRunning`](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/docs/get-operation-must-not-be-long-running.md).
**The policies are not functionally equivalent:** ARM checks recognized protocol LROs, including polling/result GETs; SDK checks accepted Legacy declarations. Raw OpenAPI extensions alone are not checked. The assessed corpus covers ARM projects, not SDK policies outside that audience.

## 2. Actual coverage

The comparison assessed **487/487 ARM projects; 0 failed; 0 unassessed**. Reported diagnostics are total individual findings across that population, not project counts.

| Count                                                                      | Swagger linter | TypeSpec linter |
| -------------------------------------------------------------------------- | -------------: | --------------: |
| Reported diagnostics                                                       |              4 |              12 |
| Affected selected-version HTTP operations (grouped by project/path/method) |              4 |               8 |

The excess TypeSpec findings come from recognized polling/result GETs without LRO extensions and source operations absent from the selected Swagger version. The second row aligns HTTP membership only; it does not establish semantic equivalence. See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the breakdown and evidence.

## 3. Function-level coverage

| Behavior                                  | Result                                                                                         |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Customized GET LRO template               | Existing Core helper recognizes the real customized read; ARM warns                            |
| Recognized polling/result GET             | ARM warns intentionally; ordinary status-only GET remains compliant                            |
| Accepted SDK Legacy declaration           | TCGC warns in common and language-specific scopes; rejected markers retain existing validation |
| Raw flag/options alone                    | Not checked by the TypeSpec linters; current standalone probes confirm no warning              |
| Diagnostic multiplicity                   | One ARM finding per recognized operation; accepted SDK scopes report once                      |
| Service boundary, suppression and non-GET | Nonservice helpers and non-GETs remain compliant; authored suppressions work                   |
| Activation and dependency isolation       | ARM `all` includes the rule; central presets remain disabled; ARM uses Core, not TCGC          |
| `paths` / `x-ms-paths`                    | Source HTTP semantics are shared; this corpus independently demonstrates only `paths` findings |

## 4. Why diagnostic counts differ

| Differing project      | Swagger / TypeSpec findings | Explanation                                                                                                                                               |
| ---------------------- | --------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BotService             |                       0 / 1 | Recognized result GET; saved Swagger has no LRO extensions. [Evidence](review-native-20261103/analysis.md#botservice)                                     |
| Maps                   |                       0 / 1 | Recognized result GET with accepted response/location metadata. [Evidence](review-native-20261103/analysis.md#maps)                                       |
| RecoveryServicesBackup |                       0 / 5 | One emitted result GET plus four source operations removed in the selected version. [Evidence](review-native-20261103/analysis.md#recoveryservicesbackup) |
| AppService             |                       2 / 3 | Two matched SDK declarations plus one additional recognized result GET. [Evidence](review-native-20261103/analysis.md#appservice)                         |

The TypeSpec total is **8 ARM + 4 TCGC** findings on 12 distinct HTTP operations, with no ARM/SDK overlap. All four Swagger findings correspond exactly to TCGC findings. Four excess ARM findings target operations absent from the selected Swagger version; four target emitted polling/result GETs without LRO extensions. All eight ARM findings have recognized LRO metadata and no raw LRO extensions.

All eight excess TypeSpec findings follow the approved TypeSpec policy. No TypeSpec rule change is required to explain these differences; they do not justify restoring the removed raw-extension fallback. Both directional excess sums are retained: Swagger **0**, TypeSpec **8**.

## NOTES

- Current source: [`8a1c96bef8aeb3edf01e3a54d3c484ff49a44fd8`](https://github.com/Azure/typespec-azure/commit/8a1c96bef8aeb3edf01e3a54d3c484ff49a44fd8); Core: `780c2c6a944d2f6be276b60f890854f7a18b2955`; tooling: `ec5e2c81c7fcb78e715313a34734e2590238cf94`; frozen specs: `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`. The producer's older runtime remains separately recorded in the [baseline descriptor](review-native-20261103/baseline-descriptor.json).
- One Swagger rule maps to `@azure-tools/typespec-azure-resource-manager/no-get-lro` and `@azure-tools/typespec-client-generator-core/no-get-lro` (TCGC). Both are warnings. ARM uses only `getLroMetadata`; TCGC uses accepted Legacy declarations. ARM `all` includes its rule; the central resource-manager and client-sdk presets remain disabled independently. The task-added Core declaration bridge is removed; Core source matches canonical main.
- The completed comparison reran TypeSpec compilation across the full population using the same sealed Swagger baseline. No Swagger generation or Swagger-linter rerun occurred. Exact diagnostic identities, operation metadata and Swagger attribution match the predecessor's investigation; totals are unchanged. This is fresh TypeSpec execution at the recorded candidate, not a replay of saved TypeSpec findings. [Current counts](review-native-20261103/coverage-summary.json), [current operation evidence](review-native-20261103/findings.json), [identity comparison](review-native-20261103/historical-identity-comparison.json). This report-format update reuses those observations; it does not claim another corpus run.
- Review IDs 04–05 restored the original registration-test title and removed the obsolete OpenAPI library from the shared ARM tester. Both comments were valid, fixed, replied to and resolved at the user's explicit request. These test-only changes do not change production behavior.
- The fresh full run used no filter or limit: `source`, `target-only`, `frozen-reference`, concurrency 2 and a 7,200-second native budget. Native execution took 27m24s; preparation and final integrity verification are additional. The analyzer retains `equivalence: not-determined`. [Execution plan](review-native-20261103/run-plan.json).
- The two test cleanups alone did not require a corpus rerun. The earlier native-only predicate change invalidated the historical final-native gate, so this run supplies current-code data while reusing saved Swagger observations.
- Swagger finding projects / TypeSpec finding projects / overlap: 2 / 5 / 2. Three TypeSpec-only projects are fully explained above. No Swagger-only project remains. All 487 fresh worker receipts succeeded, and loaded candidate entrypoints and actual installed rule files match the source-audited artifacts. [Preflight and runtime verification](review-native-20261103/preflight-summary.json).
- The alignment row filters source findings by selected-version HTTP membership; it does not rerun version-sensitive predicates on projected programs or replace the 12 source findings.
- Current-head validation: all **769 ARM tests in 84 files** passed after removing the shared tester import. Package lint, scoped formatting, Chronus verification and whitespace checks passed. The 23-package build closure succeeded; all **17 archives / 2,951 packed files** match the selected source. All **37 portable controls** and **34 current-policy injected controls** passed. Six foreign resource-group controls are not applicable because their rule is absent, not passing tests. [Commands and review outcomes](review-native-20261103/validation.json).
- The current [constructed GET LRO test](https://github.com/Azure/typespec-azure/blob/8a1c96bef8aeb3edf01e3a54d3c484ff49a44fd8/packages/typespec-azure-resource-manager/test/rules/no-get-lro.test.ts#L29-L37) directly asserts HTTP `get` and `getLroMetadata(program, read)?.operation === read`. Fresh injected controls verify native recognition, synchronous reads, ignored flag-only/options-only reads, SDK scopes, suppression and registered ARM `all` execution. A raw true extension plus an accepted Legacy marker now produces only the SDK warning, not an ARM/SDK overlap.
- Prior [documentation receipts](review-fix-20261103/documentation-examples.json), forty focused tests and five standalone probes retain their original `580a32ccf` scope. The authored rule documents did not change in this test-only cycle; those receipts were not rerun or relabeled. One-time snippet execution is not continuous documentation coverage.
- Historical validation only: 3,151 package tests, 32 canonical cases, 37 portable controls, thirty injected split controls, 23-package build closure, and all 17 archives / 2,951 packed files were verified at `7e6def9b`. Six foreign controls were not applicable. Old extension/overlap and ARM `all` opt-out controls describe the superseded policy, not current acceptance.
- Historical [external integration](https://github.com/Azure/typespec-azure/actions/runs/41402813520) failed in 64 folders with 841 diagnostics. The [pre-split run](https://github.com/Azure/typespec-azure/actions/runs/41386057187) has the exact same diagnostic multiset; neither had a `no-get-lro` diagnostic. [Comparison](split-20261102/integration-comparison.json). These old failures are not current-head CI results or a passing gate; current checks are observed separately in the PR.
- [Current recovery commands and evidence assets](review-native-20261103/recovery.md) bind the exact current tuple. The frozen specs preservation ref was verified. Release archives preserve packages, source/build provenance, all native receipts and current controls; they exclude the separately retained shared Swagger dataset. [Archive checksums](review-native-20261103/assets.json). Download verification and saved-observation count replay are separate from the actual fresh compilation.
- [Historical recovery](split-20261102/recovery.md) retains the `7e6def9b` tuple. Its thirty split controls include obsolete extension/overlap and ARM `all` opt-out expectations and are not current acceptance. Older declaration-only evidence is also historical, not validation of this rule.
