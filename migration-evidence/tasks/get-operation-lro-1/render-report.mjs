export default function renderReport(context) {
  const c = context.counts;
  return `# GetOperationMustNotBeLongRunning → ARM no-get-lro

## 1. Conclusion and scope

The ARM-owned TypeSpec rule \`no-get-lro\` migrates Swagger linter rule
[\`GetOperationMustNotBeLongRunning\`](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/docs/get-operation-must-not-be-long-running.md).
The explicit-declaration contract is supported by focused controls and exact correspondence for the assessed corpus.
General emission equivalence remains undetermined. Independent local source/proof reviews found no precommit blockers. Native C and four immutable assets are published. [Publication/recovery status](publication.json) records the remaining gates; GitHub checkpoints A/B remain pending.

## 2. Actual coverage

Fresh frozen-reference comparison: **${c.assessableProjectCount}/${c.selectedProjectCount} projects assessed; 0 failed; 0 unassessed**.
Reported diagnostics are individual findings, not project counts.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics | ${String(c.validatorRawCount).padStart(14)} | ${String(c.nativeRawCount).padStart(15)} |

## 3. Function-level coverage

| Behavior                                               | Result                                                                                          |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| Effective explicit GET declaration                     | Covered by accepted SDK declarations and exact-true raw flags                                   |
| Raw flag precedence and truthy options                 | Covered; false flag overrides SDK, options remain independent                                   |
| Legitimate 202 polling and nonservice helpers          | Compliant; protocol metadata alone is not affirmative                                           |
| SDK scope, rejected markers and selected-version state | Covered by native tests, injected controls and real-target inspection                           |
| Both flags/options on one operation                    | Intentional one-operation warning; Swagger may report twice                                     |
| \`paths\` versus \`x-ms-paths\`                            | Shared source semantics; container completeness is not independently established by this corpus |

## 4. Why diagnostic counts differ

No current one-sided project or count difference remains. Both directional raw excess sums are zero.
[Exact correspondence](proof/gap-correspondence.json) binds every finding to its path, verb, authored location and accepted source/selected-version state.
The [historical rejected 4-versus-19 comparison](evidence-details.md#observed-correspondence-and-historical-rejection) remains separate history, not current acceptance evidence.

## NOTES

- No project filter, limit or Swagger regeneration. Source/target-only mode compares source findings with saved selected-version emission; these populations are not generally interchangeable. Equal totals alone do not prove general equivalence; the analyzer retains \`not-determined\`.
- Both finding-project sets contain ${context.validatorProjects} projects. All ${context.matched} saved occurrences map exactly to ${context.mapped} current source operations. The four current targets are accepted unscoped Legacy markers; all are present in selected-version HTTP graphs.
- The historical eight polling GETs and eleven SDK helpers have no accepted AutoRest declaration or current warning. Four historical pollers are removed in the selected version; none is subtracted from source counts.
- All four corpus violations are true flags under \`paths\`. Options/\`x-ms-paths\` completeness is not established by those four findings. Injected controls cover the field predicates; unchanged emitter/Swagger-linter code supplies the container rationale.
- Affected validation: 2,944 passes/four existing skips, 54 focused tests and six actual published examples. Injected packages passed 17 declaration controls and 37 portable controls; six foreign resource-group controls were not selected.
- The small Core operation evaluator bridge has one current SDK producer. ARM imports Core, never TCGC. SDK validation, scope and ignored-marker behavior remain SDK-owned.
- An explicit raw flag overrides the accepted designation; only exact \`true\` violates. Truthy options independently violate. Polling metadata alone is never affirmative.
- Warning and disabled-by-default registration are deliberate. Existing broader Core Legacy/raw-extension bans remain separate; the four real targets waive the Legacy ban.
- Candidate tree: \`${context.candidateTree}\`. Core: \`${context.coreCommit}\`. Frozen specs: \`${context.specsCommit}\`. Native [C](https://github.com/Azure/typespec-azure/commit/03238b8a39e7cc85f8e493667c848d544ba46678) is published. [Four immutable assets](https://github.com/msyyc/typespec-azure/releases/tag/lintdiff-get-operation-lro-c0-d8953d78e779) passed upload/download verification. The containing evidence commit supplies E without a circular self-hash.
- [Full details](evidence-details.md), [population](project-inventory.json), [receipts](receipts.json), [controls](proof/injected-controls.json), [replay](replay.mjs). These are proposed local evidence, not publication or independent recovery proof.
`;
}
