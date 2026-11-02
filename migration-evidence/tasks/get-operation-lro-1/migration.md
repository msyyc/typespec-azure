# GetOperationMustNotBeLongRunning → ARM and SDK no-get-lro

## 1. Conclusion and scope

The ARM and TCGC TypeSpec rules `no-get-lro` jointly cover Swagger linter rule
[`GetOperationMustNotBeLongRunning`](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/docs/get-operation-must-not-be-long-running.md).
**The approved native policy is intentionally broader, not functionally identical:** ARM checks recognized protocol LROs, including polling/result GETs; TCGC checks accepted Legacy SDK declarations.
External integration remains red with the exact same pre-split diagnostics; it is not a green acceptance gate.

## 2. Actual coverage

Fresh frozen-reference comparison: **487/487 ARM projects assessed; 0 failed; 0 unassessed**.
Reported diagnostics are individual findings, not project counts.

| Count                                              | Swagger linter | TypeSpec linter |
| -------------------------------------------------- | -------------: | --------------: |
| Reported diagnostics                               |              4 |              12 |
| At selected-version HTTP locations, alignment only |              4 |               8 |

The TypeSpec total is **8 ARM + 4 TCGC** findings on 12 distinct checked HTTP operations. All four Swagger findings correspond exactly to TCGC findings. Four additional ARM findings target operations absent from the selected Swagger version; four target emitted polling/result GETs without LRO extensions.

## 3. Function-level coverage

| Behavior                                  | Result                                                                                                    |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Customized GET LRO template               | Existing Core helper recognizes the real customized read; ARM warns                                       |
| Recognized polling/result GET             | ARM warns intentionally; ordinary status-only GET remains compliant                                       |
| Accepted SDK Legacy declaration           | TCGC warns in common and language-specific scopes; rejected markers retain existing validation            |
| Explicit flag/options                     | ARM checks exact `true` and independently truthy options; false flags do not hide native or SDK LRO state |
| Multiplicity and overlap                  | One ARM finding per operation; independently applicable ARM and TCGC checks can both warn                 |
| Service boundary, suppression and non-GET | Nonservice helpers and non-GETs remain compliant; authored suppressions work                              |
| Activation and dependency isolation       | Both production presets keep the checks opt-in; ARM uses Core, not TCGC                                   |
| `paths` / `x-ms-paths`                    | Source HTTP semantics are shared; this corpus independently demonstrates only `paths` findings            |

## 4. Why diagnostic counts differ

| Differing project      | Swagger / TypeSpec findings | Explanation                                                                                                                                       |
| ---------------------- | --------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| BotService             |                       0 / 1 | Recognized result GET; saved Swagger has no LRO extensions. [Evidence](split-20261102/analysis.md#botservice)                                     |
| Maps                   |                       0 / 1 | Recognized result GET with accepted response/location metadata. [Evidence](split-20261102/analysis.md#maps)                                       |
| RecoveryServicesBackup |                       0 / 5 | One emitted result GET plus four source operations removed in the selected version. [Evidence](split-20261102/analysis.md#recoveryservicesbackup) |
| AppService             |                       2 / 3 | Two matched SDK declarations plus one additional recognized result GET. [Evidence](split-20261102/analysis.md#appservice)                         |

All eight excess TypeSpec findings follow the approved policy. No TypeSpec rule update is required to force Swagger-count equality. Both directional excess sums are retained: Swagger **0**, TypeSpec **8**.

## NOTES

- Candidate: [`7e6def9b192f04147a6fb8b0929a24f5d978ab9e`](https://github.com/Azure/typespec-azure/commit/7e6def9b192f04147a6fb8b0929a24f5d978ab9e); Core `780c2c6a944d2f6be276b60f890854f7a18b2955`; tooling `52eeec48b136f97addc10d90dcba4457a04f83a7`; frozen specs `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`.
- One Swagger rule maps to `@azure-tools/typespec-azure-resource-manager/no-get-lro` and `@azure-tools/typespec-client-generator-core/no-get-lro`. Both are warnings. The task-added Core declaration bridge is removed; Core source matches canonical main.
- No filter, limit or Swagger regeneration. The full run uses `source`, `target-only`, `frozen-reference`, concurrency 2 and a 7,200-second native budget. Native execution took 28m25s; setup/integrity verification is additional. The analyzer retains `equivalence: not-determined`.
- Swagger finding projects / TypeSpec finding projects / overlap: 2 / 5 / 2. Three TypeSpec-only projects are fully explained above. No Swagger-only project remains. [Counts and population](split-20261102/coverage-summary.json), [exact operation evidence](split-20261102/findings.json).
- The alignment row filters source findings by selected-version HTTP membership; it does not rerun version-sensitive predicates on projected programs or replace the 12 source findings.
- Local validation: 3,151 package tests passed, four pre-existing skips; final canonical suites passed 32 cases; affected lint, formatting, spelling, Chronus verification and the 23-package build closure passed. All 17 archives / 2,951 packed files passed source/content auditing.
- Injected validation: 37 portable controls passed; six foreign resource-group fixtures were declared not applicable before execution. Thirty split controls passed in configured and target-only modes. Ten actual authored/generated documentation examples passed. Default activation is not assessed by the corpus run; production-preset activation and suppression were verified separately.
- [External integration](https://github.com/Azure/typespec-azure/actions/runs/41402813520) fails in 64 folders with 841 diagnostics from existing rules. The [pre-split run](https://github.com/Azure/typespec-azure/actions/runs/41386057187) has the exact same diagnostic multiset; neither run has a `no-get-lro` diagnostic. [Comparison](split-20261102/integration-comparison.json). This unrelated baseline failure is not presented as a passing gate.
- [Recovery, reproducible commands and evidence assets](split-20261102/recovery.md). Saved-observation replay is a count audit, not fresh compilation. The previous declaration-only report, recovery and independent reviews remain [historical evidence](https://github.com/msyyc/typespec-azure/blob/1e4992afdc52b9d43d424402b129d28e7bd71a88/migration-evidence/tasks/get-operation-lro-1/migration.md), not validation of this split.
