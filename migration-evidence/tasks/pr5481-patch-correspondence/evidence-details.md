# PATCH correspondence: assessment details

This document retains the original candidate's execution/provenance and the
unchanged shared Swagger inputs. The [current assessment](migration.md) and
[final candidate evidence](fix-results.md) supersede its old TypeSpec counts
and pre-fix dispositions; original receipts remain available for audit.

## What this assessment can and cannot establish

The current TypeSpec linter is **not functionally equivalent** to the original
Swagger linter. The [semantic analysis](semantic-evidence.md) distinguishes
source-inspected predicates from executed controls. It includes substantive
differences, not just diagnostic formatting: same-name properties with different
types, empty PATCH models, missing PUT bodies, effective JSON leaf extraction,
version history, and diagnostic identity.

The shared production Swagger baseline did **not evaluate**
`PatchPropertiesCorrespondToPutProperties`: it is staging-only. Every one of the
649 retained Swagger execution logs explicitly disables it. An absent rule shard
is therefore **not zero findings**. The unchanged analyzer's numerical zero for an
absent shard must not be used as evidence of parity, TypeSpec-only findings,
Swagger false negatives, or a measurable cross-engine count gap.

The original TypeSpec execution uses the complete frozen ARM project population,
with no filter or limit. Its results describe current source-rule observations,
not an aligned Swagger/TypeSpec comparison. The source profile considers source
versions; the historical Swagger baseline reflects emitted-version selection.
The subsequent staging supplement evaluates those retained Swagger files
separately. No new Swagger was generated, no native corpus execution was
repeated, and neither production rule was changed to equalize counts.

## Difference-group accounting

The [staging summary](staging-comparison/summary.json) and
[complete per-project difference inventory](staging-comparison/differences.md)
record actual raw findings, both one-sided sets, project overlap,
signed/absolute/relative gaps, and both directional excesses. The
[gap investigation](gap-investigation.md) retains the schema-side causes and
limits for every one-sided project and outliers in both directions.
Common-operation counts and exact cross-engine diagnostic correspondence
remain **unassessed**: source programs across versions and latest-emitted
Swagger do not share an established normalization unit.

The saved TypeSpec project receipts and derived inventory account separately for
every selected project, successful compilation, failure/unassessed project, and
reported diagnostic. Message-family grouping is an accounting convenience, not
proof that each finding corresponds to this particular original Swagger rule:
`arm-resource-patch` also retains older resource-subset, tags, and body checks.
Do not attribute its whole diagnostic total to paired PUT/PATCH correspondence.
The [complete grouped diagnostic inventory](diagnostic-inventory.md) records
all 214 exact source targets/messages, grouped under all 42 affected projects;
the selected messages in this run are the paired-helper families.

The semantic appendix provides minimal code-backed controls for material
predicate differences. Those are controlled examples, not measured prevalence
in the service corpus. [Real-service examples and outliers](corpus-examples.md)
are documented alongside the final saved-observation inventory.

The full TypeSpec result is **214 diagnostics across 42 of 487 successfully
compiled projects**: 212 missing JSON-leaf names, one empty PATCH body, and one
absent PATCH body. There are 214 distinct project/location/message records but
192 source positions. The analyzer's `sourceIdentity` omits the message and
property name, so it can merge distinct leaf findings at one containing-model
target. The 192 positions are not unique HTTP operations or a cross-engine
normalization. In particular, its zero Swagger member count, `nativeOnlyProjects`,
and 445 equal-zero project counts must not be interpreted as measured parity.
The [source identity implementation](https://github.com/Azure/typespec-azure/blob/52eeec48b136f97addc10d90dcba4457a04f83a7/packages/typespec-lintdiff/test/harness/native-coverage.ts#L220-L225)
and complete original machine report are retained for audit.

## Original Swagger policy and frozen evidence

- Original implementation and documentation are pinned to
  [`6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f`](https://github.com/Azure/azure-openapi-validator/tree/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f).
- [ARM registration](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/az-arm.ts#L475-L489):
  staging-only, error severity, resolved OAS2, path and `x-ms-paths` selection;
  not restricted to RPaaS.
- Shared baseline: `swagger-arm-20261026-2cd3c5dd`; identity
  `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`.
- [Pinned descriptor](https://github.com/msyyc/azure-rest-api-specs/blob/317e703b3e380d3b64e0dacb3a2c6fc0651de253/.lintdiff-baselines/swagger-arm-20261026-2cd3c5dd/baseline.json);
  descriptor SHA-256
  `ac511e7ff4b519619f30af811107b7f770a92a5bb56b199dfca983262dc8fd31`.
- [Immutable baseline archive](https://github.com/msyyc/azure-rest-api-specs/releases/download/swagger-lint-baseline-20261026-2cd3c5dd/swagger-arm-20261026-2cd3c5dd.tar.gz):
  51,932,501 bytes; SHA-256
  `0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0`.
- Baseline verification checked all 93,496 retained dataset files and the exact
  487-project population. Historical totals across all enabled Swagger rules
  are not observations for the selected staging-only rule.
- Baseline runtime: openapi-validator 2.2.4, core 1.0.7, rulesets 2.2.6.
- Concrete disabled-rule evidence after extracting the archive:
  `dataset\projects\specification\advisor\resource-manager\Microsoft.Advisor\Advisor\raw\preview\2026-08-01-preview\openapi.jsonl`,
  lines 61 and 182 (production staging exclusion), 132 and 253 (disabled in
  manual and TypeSpec-generated Swagger evaluation). The complete scan found
  649 disabling logs, no staging executions, and no enablements.

## Candidate and runtime provenance

- Assessed PR head:
  [`7baca4db3d7824c24c30961c50c3f47a6df8d958`](https://github.com/Azure/typespec-azure/commit/7baca4db3d7824c24c30961c50c3f47a6df8d958).
- Core gitlink: `780c2c6a944d2f6be276b60f890854f7a18b2955`.
- Analysis tooling:
  [`52eeec48b136f97addc10d90dcba4457a04f83a7`](https://github.com/Azure/typespec-azure/commit/52eeec48b136f97addc10d90dcba4457a04f83a7).
- Frozen specs source:
  [`2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`](https://github.com/Azure/azure-rest-api-specs/tree/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9).
  Verified source preservation:
  [`msyyc/azure-rest-api-specs:evidence/long-running-operations-options-validator-20261022-source`](https://github.com/msyyc/azure-rest-api-specs/tree/evidence/long-running-operations-options-validator-20261022-source),
  pointing to that exact source commit.
- All 15 public dependency/peer-closure packages were built and packed from the
  selected candidate/core, totaling 1,982,104 bytes. The selected compiled rule,
  body helper, and model helper were byte-compared with their packed contents.
  At approximately 2 MB total, these small tarballs are retained directly in
  `artifacts/packages`, not as an expiring external job artifact. Their byte
  hashes are recorded in `provenance/artifact-provenance.json`.
- The frozen specs runtime received those tarballs through the supported
  patch/install stages, not checkout/reset. The analyzer records actual loaded
  package entrypoint hashes. The specs package manager is pnpm 12.6.0; the
  candidate/tooling package manager is pnpm 11.10.0.
- Source manifests/locks and injected installation receipts are distinct.
  Other dependency ranges resolved during installation (including OpenAPI3
  1.18.0-dev.7). This is **not** a claim of fully locked transitive regeneration.

## Separate staging supplement

The tooling is published independently in
[Azure/typespec-azure#5932](https://github.com/Azure/typespec-azure/pull/5932).
The validator-only producer source is pinned to
`9795fc4bec723e56716c0c110e392972e3de45e8`; its source-file and lockfile hashes,
actual package content identities, complete selected-rule list, input receipts,
and data inventory are in the
[supplement manifest](staging-comparison/supplement-manifest.json).

The profile is explicitly `arm-staging-spectral`: direct evaluation of the
installed ARM/common `stagingOnly: true` registrations, preserving selectors,
functions, options and error severity. The runtime uses rulesets 2.2.6 and
Spectral core 1.23.1. Matching the historical rulesets version is not a claim of
an identical transitive installation, an AutoRest staging pipeline, or
data-plane/RPaaS/native-engine coverage. Successfully evaluated zero-finding
rules have explicit shards; absent, failed and evaluated-zero are distinct.

The original production archive, descriptor and baseline identity remain
unchanged. The supplement is separately parent-bound and reusable.
[Publication and recovery provenance](provenance/staging-publication.json)
pins immutable Git data/discovery commits and byte hashes. The compact
[attempt inventory](provenance/staging-attempts.json) preserves cancelled
attempt boundaries; the
[real-corpus regression receipt](provenance/staging-cache-regression.json)
demonstrates why per-input resolver isolation is required. No failing project
was excluded from the final population.

The combined report is **saved-observation reanalysis**. The previously
verified native receipts, candidate source, 15 tarballs and original controls
are unchanged. Independent Python and
[native-coverage harness accounting](staging-comparison/harness-crosscheck.json)
cross-check all project rows and summary fields without a native rerun.

## Validation and controls

Eight fresh injected real-linter controls passed: extra PATCH leaf (1 finding),
compliant subset (0), same-name different type (0), empty PATCH model (1),
authored property suppression (0), configured-disabled comparison opt-in
(comparison 1/default 0), ARM `all` activation (1/1), and Azure resource-manager
ruleset activation (1/1).

The selected-rule corpus uses `target-only` mode, so it does not measure default
activation. The separate controls above do. The TypeSpec linter is a warning;
the original Swagger linter is an error disabled in production by staging
selection. This activation difference is material.

Portable harness validation initially produced 37 passing and 6 failing tests;
the six required an absent, unrelated unmerged `resource-group-path-parameter`
rule. After explicitly excluding that group, 37 applicable tests passed and
6 were skipped. This is not a claim that all 43 tests passed.

Some additional semantic controls invoke the rule's helper context directly,
not the complete linter/suppression pipeline; those controls are labeled
separately in the semantic appendix. Current-head focused source tests/build
from the preceding merge validation remain separate from this corpus refresh.

## Rule-change disposition

No TypeSpec rule or test-fixture change is included in this evidence-only task.
The differences are reported, not silently approved or repaired. If exact
Swagger predicate parity is required, the same-name schema/type comparison,
empty-body and missing-PUT policies, effective-property extraction, historical
version shapes, and occurrence/deduplication units need explicit design
decisions and focused regression tests. The separately authorized staging
evaluation adds missing observations without regenerating or rewriting the
shared production baseline; it does not resolve these semantic policy choices.

Do not infer that a difference is rare, intended, a Swagger bug, or a required
TypeSpec bug fix merely from the aggregate findings. Full policy parity remains
unassessed even though specific non-equivalent predicates are established.

## Reading, reanalysis, and regeneration

See [replay.md](replay.md) for the distinct saved-evidence, saved-observation
reanalysis, and new-execution paths. Saved-data recovery does not prove a full
native rerun or an exactly reproducible transitive installation. The frozen
Swagger baseline stays shared by reference; it is never rewritten by this task.
