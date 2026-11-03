# GetOperationMustNotBeLongRunning → ARM and SDK no-get-lro

## 1. Conclusion and scope

The ARM and TCGC TypeSpec rules `no-get-lro` provide native guidance related to Swagger linter rule
[`GetOperationMustNotBeLongRunning`](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/docs/get-operation-must-not-be-long-running.md).
**The native policy is an adaptation, not functional equivalence:** ARM checks recognized protocol LROs, including polling/result GETs; TCGC checks accepted Legacy SDK declarations. Raw OpenAPI extensions alone are not checked.

Current source is [`580a32ccf77c5121d8ba15908d30c968e0481b56`](https://github.com/Azure/typespec-azure/commit/580a32ccf77c5121d8ba15908d30c968e0481b56). It addresses review IDs 01–03 by removing the extension fallback and the ARM `all` exclusion. The central resource-manager and client-sdk presets remain disabled independently.

## 2. Actual coverage

The saved frozen-reference comparison at predecessor `7e6def9b` assessed **487/487 ARM projects; 0 failed; 0 unassessed**. It is not a fresh full-corpus run of `580a32ccf`. Reported diagnostics are individual findings, not project counts.

| Count                                              | Swagger linter | TypeSpec linter |
| -------------------------------------------------- | -------------: | --------------: |
| Reported diagnostics                               |              4 |              12 |
| At selected-version HTTP locations, alignment only |              4 |               8 |

The TypeSpec total is **8 ARM + 4 TCGC** findings on 12 distinct checked HTTP operations. All four Swagger findings correspond exactly to TCGC findings. Four additional ARM findings target operations absent from the selected Swagger version; four target emitted polling/result GETs without LRO extensions.

All eight saved ARM findings have native LRO metadata, with no raw extensions; none depends on the removed fallback. The SDK predicate is unchanged. Current-head evidence is **40 focused tests, ten actual documentation examples and five standalone probes**, not a new 487-project execution. [Current validation](review-fix-20261103/validation.json).

## 3. Function-level coverage

| Behavior                                  | Result                                                                                         |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Customized GET LRO template               | Existing Core helper recognizes the real customized read; ARM warns                            |
| Recognized polling/result GET             | ARM warns intentionally; ordinary status-only GET remains compliant                            |
| Accepted SDK Legacy declaration           | TCGC warns in common and language-specific scopes; rejected markers retain existing validation |
| Raw flag/options alone                    | Not checked; current standalone probes confirm a synchronous flagged GET remains compliant     |
| Diagnostic multiplicity                   | One ARM finding per recognized operation; accepted SDK scopes report once                      |
| Service boundary, suppression and non-GET | Nonservice helpers and non-GETs remain compliant; authored suppressions work                   |
| Activation and dependency isolation       | ARM `all` includes the rule; central presets remain disabled; ARM uses Core, not TCGC          |
| `paths` / `x-ms-paths`                    | Source HTTP semantics are shared; this corpus independently demonstrates only `paths` findings |

## 4. Why diagnostic counts differ

| Differing project      | Swagger / TypeSpec findings | Explanation                                                                                                                                       |
| ---------------------- | --------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| BotService             |                       0 / 1 | Recognized result GET; saved Swagger has no LRO extensions. [Evidence](split-20261102/analysis.md#botservice)                                     |
| Maps                   |                       0 / 1 | Recognized result GET with accepted response/location metadata. [Evidence](split-20261102/analysis.md#maps)                                       |
| RecoveryServicesBackup |                       0 / 5 | One emitted result GET plus four source operations removed in the selected version. [Evidence](split-20261102/analysis.md#recoveryservicesbackup) |
| AppService             |                       2 / 3 | Two matched SDK declarations plus one additional recognized result GET. [Evidence](split-20261102/analysis.md#appservice)                         |

All eight saved excess TypeSpec findings follow the approved native policy. They do not justify retaining the removed raw-extension fallback. Both saved directional excess sums are retained: Swagger **0**, TypeSpec **8**.

## NOTES

- Current source: `580a32ccf77c5121d8ba15908d30c968e0481b56`. Saved full-comparison candidate: [`7e6def9b192f04147a6fb8b0929a24f5d978ab9e`](https://github.com/Azure/typespec-azure/commit/7e6def9b192f04147a6fb8b0929a24f5d978ab9e). Both use Core `780c2c6a944d2f6be276b60f890854f7a18b2955`; historical tooling is `52eeec48b136f97addc10d90dcba4457a04f83a7`, and frozen specs are `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`.
- One Swagger rule maps to `@azure-tools/typespec-azure-resource-manager/no-get-lro` and `@azure-tools/typespec-client-generator-core/no-get-lro`. Both are warnings. The task-added Core declaration bridge is removed; Core source matches canonical main.
- The saved full run used no filter, limit or Swagger regeneration: `source`, `target-only`, `frozen-reference`, concurrency 2 and a 7,200-second native budget. Native execution took 28m25s; setup/integrity verification is additional. The analyzer retains `equivalence: not-determined`. This bounded review fix did not rerun or relabel that full execution.
- Swagger finding projects / TypeSpec finding projects / overlap: 2 / 5 / 2. Three TypeSpec-only projects are fully explained above. No Swagger-only project remains. [Counts and population](split-20261102/coverage-summary.json), [exact operation evidence](split-20261102/findings.json).
- The alignment row filters source findings by selected-version HTTP membership; it does not rerun version-sensitive predicates on projected programs or replace the 12 source findings.
- Current-head validation: ARM build/library lint, both package lints, changed-code type-aware lint, formatting, spelling and Chronus verification passed. Forty focused tests passed: ten ARM rule cases, three ARM registration cases, fourteen SDK rule cases and thirteen central-ruleset cases. [Documentation receipts](review-fix-20261103/documentation-examples.json) record ten actual snippets; this one-time execution is not continuous documentation coverage.
- [Standalone probes](review-fix-20261103/native-probes.json) verify native customized GET recognition, the synchronous control, ignored flag-only/options-only GETs, and registered ARM `all` execution. The canonical [constructed GET LRO test](https://github.com/Azure/typespec-azure/blob/580a32ccf77c5121d8ba15908d30c968e0481b56/packages/typespec-azure-resource-manager/test/rules/no-get-lro.test.ts#L29-L37) directly asserts HTTP `get` and `getLroMetadata(program, read)?.operation === read`.
- Historical validation only: 3,151 package tests, 32 canonical cases, 37 portable controls, thirty injected split controls, 23-package build closure, and all 17 archives / 2,951 packed files were verified at `7e6def9b`. Six foreign controls were not applicable. Old extension/overlap and ARM `all` opt-out controls describe the superseded policy, not current acceptance.
- Historical [external integration](https://github.com/Azure/typespec-azure/actions/runs/41402813520) failed in 64 folders with 841 diagnostics. The [pre-split run](https://github.com/Azure/typespec-azure/actions/runs/41386057187) has the exact same diagnostic multiset; neither had a `no-get-lro` diagnostic. [Comparison](split-20261102/integration-comparison.json). These old failures are not current-head CI results or a passing gate; current checks are observed separately in the PR.
- [Historical recovery, reproducible commands and evidence assets](split-20261102/recovery.md) retain the exact `7e6def9b` tuple. Saved-observation replay is a count audit, not fresh compilation. The older declaration-only report and independent reviews remain [historical evidence](https://github.com/msyyc/typespec-azure/blob/1e4992afdc52b9d43d424402b129d28e7bd71a88/migration-evidence/tasks/get-operation-lro-1/migration.md), not validation of the current rule.
