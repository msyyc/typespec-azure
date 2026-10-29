# Evidence detail

## Contract and ownership

`no-get-lro` is ARM-owned. It queries concrete GETs in the actual HTTP service graph, including global fallback.
Core stores one side-effect-free per-operation evaluator. TCGC installs it only after accepting the Legacy marker.
The evaluator uses the queried Program/Operation and SDK scope reader. Core contains no SDK grammar; ARM has no SDK dependency.
Scope queries use the full AutoRest package name. Raw flag presence overrides the SDK designation; truthy options remain independent.

## Observed correspondence and historical rejection

The exact four current operation mappings and every historical location are in [gap correspondence](proof/gap-correspondence.json).
The fresh [accepted-state inspection](proof/accepted-declaration-runtime-proof.json) queried real Core/SDK getters for AutoRest, CSharp and Java.
It inspected source and selected-version graphs for seven projects, four saved targets and all nineteen historical rejected locations.
This proves accepted state, not actual server-side initiation or regenerated emission.
All current project/count differences are fully enumerated in the [487-project audit](proof/full487-audit.json).

## Validation and release compatibility

The reviewed20-file tree is unchanged. Current source validation is 2,944 passes/four existing skips over all four affected packages,
54 focused tests, normal builds/lint/type-aware/format/docs/ruleset checks and six actual authored/generated documentation examples.
The new immutable export has19,664 source files. Core/ARM/TCGC/rulesets were rebuilt in isolation; eight changed runtime outputs equal the tested native output bytes.
Seventeen fresh archives have2,914 verified non-manifest files plus17 verified manifests, close52 workspace dependencies and pass the full2,883-file manifest-pattern audit.
The generated Examples JSON exception is checked against its actual packed module import and equivalent compiled JSON, not waived.
Existing Chronus lockstep minor/workspace-peer rules select the new API consumers together at0.74.0; local unreleased pack versions remain0.73.x.

The [17 injected controls](proof/injected-controls.json) include actual SDK production, scopes, raw precedence/options, valid202 polling,
helper exclusion, registered activation/defaults and authored suppression. The portable suite passed37, with six foreign resource-group cases explicitly N/A.
Original43-suite failures, original5 metadata-only controls, failed helper126, failed optional wrapper178 and failed whitespace163 remain history, not new passes.

## Publication and recovery

Independent retained source/design and final proof reviews found no precommit blockers.
Native [C](https://github.com/Azure/typespec-azure/commit/03238b8a39e7cc85f8e493667c848d544ba46678) retains the reviewed tree.
All four [immutable release assets](https://github.com/msyyc/typespec-azure/releases/tag/lintdiff-get-operation-lro-c0-d8953d78e779) passed upload and download/hash verification.
See [current publication/recovery status](publication.json), [pinned recovery plan](recovery-plan.json) and [cold recovery helper](recover.mjs).
The portable saved-observation replay rebuilds counts and exact formatted report bytes; it is not fresh native execution.
Separate outer-owned GitHub checkpoints A and B both completed clean on unchanged C, one Balanced round each, with no fixes.
[Portable review receipts](proof/review-summary.json) link both requests and reviews. Each final parent inspection found zero numeric REST review comments and zero unresolved Copilot threads after full pagination.
The separate checkpoint-B local readiness reviewer found no native or substantive evidence blockers; final metadata follow-up and publication approval remain coordinator-owned.

Independent cold recovery restored the published E1 inputs and verified19,664 source files,17 package archives,2,914 packed files plus17 manifests,93,496 baseline files and1,481 runtime files.
The clean remote E2 checkout then verified all30 publication files/Git blobs and exact saved-observation report/count replay.
[Cold receipt](proof/cold-recovery.json) and [E2 reconciliation](proof/evidence-E2-reconciliation.json) retain the historical report SHA256 `de74fc3af6589f9eefe68f7126ef39941e474fc89996750f36b2b51b7f5e76d6`.
The final metadata report has a [new identity](proof/final-report-identity.json); it does not rewrite either historical recovery receipt or claim another full native run.

The original staged seven blob identities and local backup remain preserved; only authorized publication copies replace them.
Known LF correction1/1 was debited before this coherent formatter/replay/whitespace correction. Semantic supplement3/3 remains exhausted.
Capture-time states in immutable raw receipts are historical, not rewritten publication claims.
In particular, `proof/native-draft-pr.json` preserves the creation-time pending checkpoints; current completed results are in `proof/review-summary.json` and `publication.json`.
Failed helper126, wrappers151/178, whitespace163 and optional summary207 remain retained history.
No failed external operation was retried and no source semantic edit occurred after admission.
