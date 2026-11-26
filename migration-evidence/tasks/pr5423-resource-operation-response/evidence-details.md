# Supporting evidence and recovery

## Assessment boundary

The frozen assessment uses the resolver implementation at
`d40a080ddf7e504a40e0eaf3aa4c8aeede40b9f4`, actual core
`683031f809a3394a374c21ed587979277f6dd5c7`, tooling
`402e3fb202e9a16f0a8c7dfc1b799098cfba879d`, and frozen specs
`2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`.

The sealed Swagger baseline is
`aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`;
its ARM staging supplement is
`e0a2c22b857b13fa8ccf318bff1c8a6beaf367e1a1210cbc71cf7161fd86d482`.
Both remain read-only. Swagger generation and Swagger linter execution are
not rerun. One explicit four-member/one-TypeSpec-linter mapping runs against all
487 frozen projects with source scope, frozen-reference policy, no filter/limit,
and concurrency two. Supplemental owning callbacks are not additional selected
mapping IDs.

Actual execution uses Node 26.13.0 and the frozen specs' pnpm 12.6.0, retaining
the approved registry. This current closure is not the baseline producer's
historical runtime. The source-versus-latest-version comparison does not prove
universal version-aligned or structural equivalence.

The [plan](receipts/resolver-20261125-plan.json),
[source/build/archive attestation](receipts/resolver-20261125-artifacts.json),
[baseline verification](receipts/resolver-20261125-baseline.json), and
[run manifest](runs/20261125-d40a080ddf-native-resource-contract/manifest.json)
record the frozen inputs. [Coverage](runs/20261125-d40a080ddf-native-resource-contract/coverage.json)
preserves the unfiltered observations.

## Native policy and resolver boundary

The rule calls `resolveArmResources` once at global namespace exit. Each
resolved occurrence supplies its resource model, HTTP operations and scope.
Canonical requests, lifecycle responses and list items are checked through
those associations; occurrences are not collapsed by model. Requests deduplicate
the operation/model pair, and response warnings deduplicate offending operations.

The separate PUT identity pass uses resolved lifecycle/list/action/associated
and provider operations. Every body-bearing 200 and 201 response must use a
resolved resource, native resource-base ancestry, virtual resource or existing
custom-resource identity. Emission options and extension overrides do not define
identity. The separate custom-marker option policy is unchanged. Canonical
response failures avoid duplicate resource-identity warnings.

LIST/PATCH-only registrations need not establish a resolved resource occurrence
([#5994](https://github.com/Azure/typespec-azure/issues/5994)). Such omitted
occurrences are not checked; no `getArmResource` or direct HTTP-enumeration
fallback is added. Marked PUTs targeting models without ARM declarations can
also escape both resource and provider collections
([#5995](https://github.com/Azure/typespec-azure/issues/5995)).
The [resolver discussion](https://github.com/Azure/typespec-azure/issues/6053#issuecomment-6927770475)
chooses this supported API, not perfect legacy parity.

The [complete target delta](resolver-analysis.md) explains all 16 removed
canonical comparisons (15 GET and one POST). These findings were already
outside the four original Swagger checks. Fresh attributed diagnostic counts,
owning callbacks and the scoped gap remain unchanged; absent warnings do not
establish that the underlying models are compliant.

## Exact correspondence and suppression

The frozen Swagger observations keep their member, invoking/reported document,
JSON path and repeated occurrence identities. Check contexts retain the member,
project, resolved document, exact route and compared schema context.

The fresh metadata pass inspects the union of Swagger-affected, currently
TypeSpec-affected and previously TypeSpec-affected projects. Historical affected
operations remain in the compact graph even when their warnings disappear.
Every inspected project must reproduce its saved configured diagnostics exactly
and have no HTTP metadata errors. Source and selected-version body/declaration,
canonical association, actual status and predicate evidence establish
correspondence; route or message coincidence alone does not.

Actual selected and existing owning callbacks are captured before authored
suppression. Distinct report indexes remain distinct diagnostics. Shared
callbacks count once across members, without merging different diagnostics of
the same check. [Count components](diagnostic-count-components.json) explain
the full signed difference, including repeated emission and overlapping owners.
This affected-union pass is not exhaustive corpus-wide suppression enumeration.

[Original configured observations](observations.json),
[exact comparisons and exclusions](instance-correspondence.md),
[source/selected graph](instance-inputs.json),
[decisions and scoped accounting](gap-assessment.json), and
[directional project differences](project-differences.md) retain the audit trail.
Absent correspondence is not automatically compliance or an excluded policy.

## Validation and CI

The assessed resolver source passes 200 focused tests across four files, including 68
canonical rule cases, required dependency builds, engineering type checking,
ordinary/type-aware lint, formatting, spelling, Chronus and whitespace checks.
Four added multi-scope controls also passed on the previous implementation;
they are regression guards, not proof that those examples were previously missed.
Exact authored documentation examples produce the intended one/zero findings
without compiler errors.

Preflight includes 40 selected injected controls, 37 applicable portable controls,
six metadata controls and two versioned metadata controls. Six portable fixtures
require an unrelated absent migration and are explicitly non-applicable.
Unannotated collection-item controls supply a genuine read occurrence and public
route decorators because standard paged templates reject unannotated items.
The LIST-only omission control uses the public standard template.

The first injection failed because `@typespec/openapi3@next` no longer resolved
in the approved registry. The bounded recovery adds OpenAPI3, asset-emitter and
formatter archives from the same pinned core, bringing the complete inventory
to 18; it does not substitute arbitrary latest dependencies or alter specs.
An injected-control assertion then expected one message for two offending
operations. Its multiplicity assertion was corrected. Passing receipts were
reused only after checking source/config/input, saved receipt hashes and actual
loaded package payloads; changed or missing controls were executed.
All failed attempts and the final receipts are retained separately.
The retained injected `main.tsp` files preserve their executed bytes, including
template-generated blank-line indentation. Their narrowly scoped Git whitespace
attribute limits whitespace-check exemptions to those byte-preserved captures;
it does not exempt production code or report scripts.

The fresh full run succeeds for all 487 projects. All 73 affected-union metadata
inspections reproduce the saved configured findings exactly, with no metadata
errors. The saved-data assessment initially rejected a new resolver classification:
TestJob is associated with a Runbook action, not its own create/update contract.
The [tested classifier repair](receipts/resolver-20261125-assessment-repair.json)
preserves the unresolved DTO-contract conclusion without rerunning either
expensive stage. All 35 saved-data tests pass.

[Validation](validation.json) records final run, analysis, recovery and exact-head
CI status. Full frozen-corpus completion is not a green moving external-specs
CI claim. The independent source reviewer found no actionable bugs.
The [companion suppression proposal](companion-suppressions.md) was subsequently
reopened and rebuilt from current `typespec-next` using the completed exact-head
external specs CI at `d40a080dd`: 262 annotations in 170 files. The November 26
refresh retains that historical diagnostic evidence, rebuilds from consumer
base `6ce3a7672`, and places directives before decorators at proposal
`d73194243`. It does not claim an exact-current-runtime rerun or repair of the
consumer workflow's separate automatic-main-merge compiler failures.
Neither it nor the separate
registration proposal is credited in frozen counts.

The later selected review fixes at `b730bce2b` modify only canonical tests:
the data-plane case is removed and seven mismatch cases are consolidated into
two compilations with exact authored diagnostic targets. All 62 canonical
cases, full repository formatting and ordinary/type-aware lint pass. The ARM
production implementation is unchanged, so this cleanup requires no fresh
corpus. The intervening maintainer merge updates core to `41e2a4e70`; the
frozen coverage and older external CI remain explicitly pinned to their actual
runtime rather than relabeled as a current-core execution.

At the published resolver head, formatting, lint, spelling and the Java build/test
check pass. [Package-size CI](https://github.com/Azure/typespec-azure/actions/runs/45550910115/job/138991582698)
fails in **Build (base)**, after the workflow checks out target-base
`42a033215c7512522f4117a71b02dc60b8aff060`. Java's `sse-utils.ts` cannot find
`SchemaContext.Sse` or `ModelOptions.sseMetadata`. This is not a resolver-source
failure; no unrelated Java/base repair is bundled here. Other external checks
are retained at their actual captured status, not represented as passed.

The [external specs job](https://github.com/Azure/typespec-azure/actions/runs/45550909839/job/138991581750)
subsequently completed with **543 passed / 62 failed / 605 projects** and
289 selected-rule diagnostics, at the same resolver head and core. Its fresh
source reconciliation supports the companion proposal, not a green-CI claim;
no local consumer validation or CI rerun/wait was performed.

Final verification also inspected the already-completed
[current-head external job](https://github.com/Azure/typespec-azure/actions/runs/45800499846/job/139842326361).
At `b730bce2b` and core `41e2a4e70`, it reports the same 543 passed / 62 failed /
605 projects and 289 selected-rule occurrences. All 269 target/rule/message
checks and 262 authored targets match the proposal, with exact diagnosed-source
line correspondence and no other parsed diagnostic codes. The
[current receipt](receipts/companion-20261126-b730-public-external.json)
does not invent an immutable consumer SHA: the job logs moving `typespec-next`.
The linter's format, lint, build, unit and package-size checks pass at this head.
No suppression CI was awaited, and no proposed consumer edit is claimed validated.

## Read, recount and regenerate

Saved-input verification needs no compilation:

```powershell
python -B analyze-instances.py --root .
python -B assess-gaps.py --verify
python -B -m unittest test_instance_analysis test_reanalyze
python -B reanalyze.py --verify-inventory
python -B render-instances.py --verify
```

Publication and downloaded recovery passed: the [immutable asset descriptor](resolver-validation-asset.json)
and [recovery receipt](receipts/resolver-20261125-recovery.json) record its
SHA-256, 2,802 verified indexed files, 487 original receipt links and 18 unchanged
archives. Attribution, summary and assessment hashes are identical after
downloaded reanalysis. The sealed asset is a pre-publication snapshot; subsequent
provenance-link corrections, recovery results and exact-head CI status are
recorded in this Git evidence, not retroactively added to that immutable snapshot.
The asset retains the 18 untouched package archives, worker
inputs/results/logs, full affected-union graphs, controls, failed attempts,
source/build lineage, finishing scripts and saved-analysis snapshot. Installed
dependencies and the separately published shared Swagger dataset are excluded.
Paths are sanitized without changing package payloads.

Recover the baseline and supplement through their
[pinned baseline descriptor](https://github.com/msyyc/typespec-azure/tree/1c9d2b0e6a596754af1aa793b1906ff3c4ef2bd6)
and [pinned supplement descriptor](https://github.com/msyyc/typespec-azure/tree/feec4bab366c373380fbe1b5528faa12e7233cfe).
[Frozen specs](https://github.com/msyyc/azure-rest-api-specs/tree/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9)
remain independently fetchable, separate from authored follow-ups.

A full rerun requires the exact candidate/core/tooling commits, verified baseline
assets, all candidate archives and recorded specs runtime/registry. Restore
sanitized path tokens to verified local roots. Run the retained serialized
orchestration with a new empty output directory and all four Swagger selectors
plus the single TypeSpec selector. Hold the exclusive corpus lock, preserve failed
attempts, and do not regenerate Swagger.

Then execute finishing `export`, `inspect` and `assess`, retaining the historical
affected union and exact configured-diagnostic equality. Run the renderer,
saved-data tests and integrity checks. Downloaded saved-input recovery/reanalysis
is not a fresh full native regeneration.

## Review-fix validation (2026-11-18)

[Historical evidence](historical-assessment.md#review-fix-validation-2026-11-18)
preserves the earlier 6981ba45a/283-diagnostic comparison, prior suppression
assessment, immutable assets and CI context. None is relabeled as a current
resolver result.
