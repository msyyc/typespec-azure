# GetOperationMustNotBeLongRunning → ARM and SDK no-get-lro

## 1. Conclusion and scope

For the assessed ARM corpus and supported TypeSpec LRO declarations, Swagger linter rule
[`GetOperationMustNotBeLongRunning`](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/docs/get-operation-must-not-be-long-running.md)
is **fully covered jointly by two TypeSpec linter rules**:
`@azure-tools/typespec-client-generator-core/no-get-lro` (TCGC) and
`@azure-tools/typespec-azure-resource-manager/no-get-lro` (ARM).
Raw OpenAPI extension-only declarations and SDK policies outside the ARM audience are outside this coverage claim.

## 2. Actual coverage

The comparison assessed **487/487 ARM projects; 0 failed; 0 unassessed**. Reported diagnostics are total individual findings across that population, not project counts.

| Count                                                                      | Swagger linter | TypeSpec linter |
| -------------------------------------------------------------------------- | -------------: | --------------: |
| Reported diagnostics                                                       |              4 |              12 |
| Affected selected-version HTTP operations (grouped by project/path/method) |              4 |               8 |

The TypeSpec linter rules apply a stricter semantic LRO policy by design, reporting recognized polling/result GETs even without LRO extensions. Source-wide checking also includes operations absent from the selected Swagger version. These intentional checks and scope differences explain the additional diagnostics. The second row aligns HTTP membership only; it does not establish identical rule behavior. See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the breakdown and evidence.

## 3. Function-level coverage

| Behavior                                  | Result                                                                                         |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Customized GET LRO template               | Existing Core helper recognizes the real customized read; ARM warns                            |
| Recognized polling/result GET             | By design, ARM warns without LRO extensions; ordinary status-only GET remains compliant        |
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

The additional diagnostics are **by design**, not missing Swagger coverage: the ARM rule uses stricter semantic recognition rather than requiring emitted LRO extensions, and the source-wide run retains operations excluded from the selected Swagger version. No TypeSpec rule change is required to explain these differences; the stricter checks should not be weakened to match Swagger diagnostic totals. Both directional excess sums are retained: Swagger **0**, TypeSpec **8**.

## NOTES

### Current review fix: 2026-11-04

- Current source: [`a78104288669f33aa23ac2f78c7c0410dc312040`](https://github.com/Azure/typespec-azure/commit/a78104288669f33aa23ac2f78c7c0410dc312040); Core: `05b9bad7c57b9b58e8fb5390f9bab081a1a9ac31`; tooling: `662e7f405fda22e1d9c8c9c1d7664d171f80b60d`; frozen specs: `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`. Baseline discovery metadata was pinned at `1c9d2b0e6a596754af1aa793b1906ff3c4ef2bd6`; its immutable descriptor retains baseline identity `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`.
- Only review finding **01** was selected: the ARM rule now calls `getHttpOperation` directly and retains the same explicit/implicit HTTP-service boundary using compiler operation enumeration. Rule IDs, SDK behavior, registration and suppression policy are unchanged. Findings 02-03 were not acted on.
- A fresh, exclusive-lock-protected native run assessed **487/487 projects, with zero failures or unassessed projects**. Swagger was neither regenerated nor revalidated. Counts remain **4 Swagger / 12 native**, split **8 ARM + 4 TCGC**; selected-version HTTP membership remains **4 / 8**. All **12 diagnostic identities, messages, authored targets, operation metadata, selected-version memberships and saved Swagger attributions are unchanged**, with no added or removed finding. [Counts](review-http-20261104/coverage-summary.json), [operation evidence](review-http-20261104/findings.json), [exact comparison](review-http-20261104/identity-comparison.json).
- The run used `source`, `target-only`, `frozen-reference`, no filter/limit, concurrency 2 and a 7,200-second native budget. Native execution took **29m02s**, excluding preparation/final integrity checks. The analyzer still reports `equivalence: not-determined`; matching this refactor's results does not erase the existing intentional Swagger/native policy differences.
- Validation passed: **13 canonical rule tests**, the **23-package build closure**, root `pnpm format`, root `pnpm lint`, Chronus verification and whitespace checks. Three canonical regressions protect nested explicit-service operations, nonrecursive implicit-global handling and exclusion of global operations when explicit services exist. No corpus behavior changed, so no additional corpus-derived fixture was necessary. The first lint attempt exposed missing playground types; the minimal dependency closure was restored and root lint then passed. [Commands and dispositions](review-http-20261104/validation.json).
- All **37 portable controls** and **34 current-policy injected controls** passed. Six foreign resource-group fixtures remain explicitly inapplicable, not passes. **15 archives / 2,855 packed files** match the candidate source/build; all 487 fresh worker entrypoint receipts and both actual installed rule files match the artifacts. The fifteen archives form the complete required runtime workspace closure; two historical extra archives are not required. [Runtime verification](review-http-20261104/runtime-verification.json).
- The analyzer tested the recorded working-tree content on `e8486a1b922242a8893e7d092f5ca9750296a74d`, diff SHA-256 `d5ca7ad00f4391175f3dcc69e53f8ea1d0065a07b01cc17e237fa92849584bee`. Both published commit blobs match the tested file hashes exactly. The later commit introduces no untested source change. [Manifest](review-http-20261104/manifest.json).
- [Recovery instructions](review-http-20261104/recovery.md) and [checksummed assets](review-http-20261104/assets.json) retain the candidate packages, build/pack provenance, all native observations and current controls. The frozen specs preservation ref was reverified at the exact source SHA. Download/hash verification and saved-observation replay are separate from the actual fresh compilation. Published text copies use role tokens and UTF-8/LF; the sealed baseline and package tarballs are unchanged.
- Final-head CI was queried once after publication: no checks were reported yet. CI was not awaited and is not claimed to have passed. Overall PR readiness was not reassessed beyond the user-selected finding 01.

### Historical receipts

These notes retain the preceding cycles' scope and terminology. Their "current" labels refer to those historical snapshots, not the current review-fix head above.

- Prior source: [`8a1c96bef8aeb3edf01e3a54d3c484ff49a44fd8`](https://github.com/Azure/typespec-azure/commit/8a1c96bef8aeb3edf01e3a54d3c484ff49a44fd8); Core: `780c2c6a944d2f6be276b60f890854f7a18b2955`; tooling: `ec5e2c81c7fcb78e715313a34734e2590238cf94`; frozen specs: `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`. The producer's older runtime remains separately recorded in the [baseline descriptor](review-native-20261103/baseline-descriptor.json).
- One Swagger rule maps to `@azure-tools/typespec-azure-resource-manager/no-get-lro` and `@azure-tools/typespec-client-generator-core/no-get-lro` (TCGC). Both are warnings. ARM uses only `getLroMetadata`; TCGC uses accepted Legacy declarations. ARM `all` includes its rule; the central resource-manager and client-sdk presets remain disabled independently. The task-added Core declaration bridge is removed; Core source matches canonical main.
- Full coverage here means all observed Swagger findings are covered under the assessed TypeSpec semantic policy. It does not mean identical behavior or a strict superset of every raw OpenAPI check: extension-only declarations remain unchecked, as documented in section 3 and the linked controls.
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
