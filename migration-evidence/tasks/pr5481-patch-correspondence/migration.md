# PatchPropertiesCorrespondToPutProperties migration

## 1. Conclusion and scope

The TypeSpec rule `@azure-tools/typespec-azure-resource-manager/arm-resource-patch`
migrates Swagger linter rule
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
**The demonstrated non-versioning gaps are fixed for supported current-source
PUT/PATCH bodies; full Swagger equivalence is not established.** The TypeSpec
linter checks writable names, compatible wire types and supported constraints,
including operations inherited onto project interfaces. It intentionally avoids
the Swagger linter's whole-schema-equality overchecking bug and detects empty
PATCH objects that the Swagger linter misses. Historical names/types,
availability and operation selection remain outside this repair under the
authorized [#5875](https://github.com/Azure/typespec-azure/issues/5875) deferral.
Unsupported/ambiguous top-level bodies and complete cross-engine defect
correspondence remain unassessed.

## 2. Actual coverage

The assessment covers **487 ARM projects, with 0 failed/unassessed projects**,
and **649 retained Swagger inputs, with 0 staging-evaluation failures**.
Reported diagnostics are total individual findings, not project counts.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |      **1,314** |         **117** |

**Assessed coverage:** **1,132 Swagger overchecks are excluded**: 339
documentation, 144 defaults, 612 input-compatible mutability and 37 additional
read-only PATCH reports. All **182 remaining emitted records** were investigated
against exact source route/body predicates:

- **131 same-name schema records:** 42 have reported source-check witnesses;
  81 have reviewed compatible current-source contracts; 6 do not identify
  writable source leaves; 2 have both compatible and incompatible same-named
  source leaves, with the incompatible checks reporting.
- **49 absent emitted names:** 46 have reported source-check witnesses;
  1 is an accepted opaque wrapper; 2 are flattening/wrapper differences,
  not absent source leaf checks.
- **2 absent bodies:** 1 reported and **1 valid-but-suppressed** finding.
  Both receive coverage credit; suppression does not inflate the raw total.

**No remaining confirmed missing non-versioning check was found in these
investigated supported source contexts.** The fixes add **23 configured
compatibility warnings** versus the preceding 94-warning implementation.
The inherited-operation repair recovers two previously unchecked Oracle
contexts; both have compatible source contracts, so neither needs a warning.

These are assessed **context/contract observations**, not 182 matched defects
or 182 independently expected TypeSpec warnings. The 81 compatible schema
contexts comprise **23 partial collections, 11 serialized enum/literal
contracts, 4 narrower bounds, 19 partial/null-reset/secrecy differences and
24 request-compatible mutability/identifier differences**. They establish why
those current-source checks accept, not that every historical Swagger record
is a harmless false positive. Comparable violation totals and coverage
percentages remain **unassessed** because a complete API-version-aware
source-to-emission identity is unavailable. Neither `1,314 - 117` nor
`182 - 117` counts missed violations.

See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the
remaining differences, actions and limits.

## 3. Function-level coverage

| Behavior                                                              | Result                                      | Rationale                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Extra PATCH JSON leaf; compliant subset                               | Covered in supported scope                  | Exact encoded names and effective request membership are checked; [registered controls](refresh-20261105-inherited/controls/injected-controls.json) include violations and compliant subsets.                                                                             |
| Same-name incompatible wire types/constraints                         | Fixed; covered for implemented predicates   | [Compatibility evidence](gap-investigation.md#compatibility-fix) covers scalar/encoding, serialized enum values, recursive arrays/dictionaries/partial objects, string/item lengths and numeric bounds. It is not a universal regular-expression or schema-subset solver. |
| Inherited ARM operations instantiated in project interfaces           | Fixed                                       | [Inherited-operation evidence](gap-investigation.md#inherited-operation-fix) proves the previous origin-filter bug with failing regressions, preserves project targets and checks the recovered Oracle pairs.                                                             |
| Absent/empty PATCH, or writable PATCH with absent PUT input           | Covered                                     | [Body evidence](gap-investigation.md#missing-body-correspondence) distinguishes absent input from an existing empty object and preserves the Quota suppression.                                                                                                           |
| Nested/inherited writable leaves, encoded names, shared targets       | Covered in supported scope                  | [Controls and source captures](gap-investigation.md#assessment-method) retain visibility, distinct check families and source-target deduplication without collapsing different warnings at one position.                                                                  |
| Documentation/defaults/method-appropriate mutability                  | Intentionally not compared for equality     | [Overcheck evidence](gap-investigation.md#assessed-diagnostic-records) demonstrates why metadata equality is not request compatibility.                                                                                                                                   |
| Individual API-version names/types, availability, operation selection | Missing/deferred; excluded from this repair | [Historical dispositions](gap-investigation.md#versioning-boundary) belong to shared #5875, not new per-rule reconstruction.                                                                                                                                              |
| Unsupported/ambiguous top-level bodies                                | Unassessed                                  | The object-body gate does not establish parity for these shapes; they are not classified as compiler-prevented.                                                                                                                                                           |

## 4. Why diagnostic counts differ

The Swagger rows below are disjoint and account for **all 1,314 records**.
The TypeSpec column counts only established same-check findings; contextual
witnesses are identified separately and are not asserted to be matched emitted
violations. **Unassessed attribution is not an unimplemented check.**

| Difference (with evidence)                                                                                | Swagger diagnostics | TypeSpec diagnostics for the same check                                                          | Recommended action and rationale                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------- | ------------------: | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Documentation/default/mutability/read-only overchecks](gap-investigation.md#assessed-diagnostic-records) |               1,132 | 0 metadata-equality checks                                                                       | **Do not port the bug.** Retain request visibility and compatible value checking, not whole-schema equality.                                                                                                                                            |
| [Same-name schema differences](gap-investigation.md#schema-contexts)                                      |                 131 | Unassessed emitted counterparts; 34 distinct configured source-check witnesses in these contexts | **Confirmed compatibility gap fixed.** Keep warnings for incompatible contracts; accept the 81 reviewed source contracts, exclude 6 non-input/flattened names and retain the 2 mixed-name cases explicitly. Do not equate 131 records with 131 defects. |
| [Absent emitted names](gap-investigation.md#name-contexts)                                                |                  49 | Unassessed emitted counterparts; 44 distinct configured source-check witnesses in these contexts | **No further demonstrated name-check gap.** 46 records have reporting contexts; explain the remaining 3 wrappers rather than adding duplicate name checks.                                                                                              |
| [Absent bodies](gap-investigation.md#missing-body-correspondence)                                         |                   2 | 1 reported                                                                                       | **Covered.** Also credit Quota's 1 verified suppressed finding; preserve the authored exception.                                                                                                                                                        |

The **117 TypeSpec warnings are not all counterparts of those 182 records**.
The context join witnesses 79 distinct configured warnings: 23 compatibility,
55 missing-name and 1 absent-body warning. The other 38 remain in the full
diagnostic inventory, not silently discarded or labeled matched defects.
[Source-only differences](gap-investigation.md#typespec-higher-projects)
include BillingTrust's request-membership warning and NetApp's empty-body
check; NetApp's historical-name warning remains deferred to #5875.
Swagger emits repeated operation/version records while TypeSpec can reuse
one source target. These identities and scope differences preclude subtraction
as a defect count.

## NOTES

- **Assessed implementation:** [PR #5481](https://github.com/Azure/typespec-azure/pull/5481),
  candidate [`012190397`](https://github.com/Azure/typespec-azure/commit/0121903975ab45cde7d7aca37cf50ffd7f3855d3).
  [Execution/mapping](refresh-20261105-inherited/task.json),
  [all project receipts](refresh-20261105-inherited/runs/full-corpus/manifest.json),
  [15-package provenance](refresh-20261105-inherited/provenance/artifact-provenance.json)
  and [local validation](inherited-20261105/validation.json) identify the actual
  source, compiler/library closure and installed artifacts.
- **Execution and recovery:** all 487 projects succeeded. The original CLI
  exited 255 after 134 completed projects; the remaining 353 ran through the
  same official workers under the original 10,800-second deadline, without
  rerunning a completed project. All 93,496 dataset files, source snapshots,
  artifacts, supplements and the reconstructed official report passed the
  original integrity checks. The original running manifest is preserved;
  this is **not a clean CLI pass**. [Recovery](refresh-20261105-inherited/provenance/integrity-reconciliation.json)
  and [runtime repair](refresh-20261105-inherited/provenance/pinned-node-recovery.json)
  retain the failures and exact Node version, without claiming an established
  cause for exit 255.
- **Assessed methods:** [182 context observations](refresh-20261105-inherited/source-attribution/observations.json),
  [51 exact-multiset capture checks](refresh-20261105-inherited/source-attribution/inventory.json),
  [reviewed acceptance groups](inherited-20261105/assessed-contexts.json)
  and [per-project/route index](inherited-20261105/retained-route-contexts.md)
  distinguish source checks, configured warnings and suppression probes.
  The immutable [Swagger assessment](assessment-20261105/results.json) supplies
  the 1,132/182 split; its embedded 94-warning TypeSpec counts are historical,
  not current results.
- **Population/policy:** frozen specs `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`;
  ARM, `source`, `target-only`, `frozen-reference`, no filter/limit,
  concurrency 2. The separate `arm-staging-spectral` supplement evaluated this
  staging-only Swagger rule; production's absent shard is **not evaluated**,
  not a compliant zero. No Swagger was regenerated. Source-program evaluation
  is not historical-version projection. Existing warning severity,
  registration/activation and authored suppressions are unchanged.
- **Accounting:** 740 Swagger path identities versus 107 TypeSpec positions,
  not a common defect unit. There are 335 Swagger-affected / 34 TypeSpec-affected
  projects, 33 overlapping, 302 Swagger-only and 1 TypeSpec-only. Raw counts
  are higher for Swagger in 329 projects and TypeSpec in 2; 156 are equal.
  Directional excesses are 1,199 / 2, absolute per-project gap 1,201.
  [Complete signed/absolute/relative project and target inventory](refresh-20261105-inherited/staging-comparison/differences.md)
  preserves both directions; equal totals do not prove semantic agreement.
- **Validation/continuity:** 89 canonical tests, 32 relevant ARM sample tests,
  25 injected controls, 37 applicable portable controls and 10 extraction
  controls passed. Six unrelated portable fixtures were explicitly inapplicable;
  eight unaffected data-plane sample cases were not rerun after the incremental
  ARM fix. Build/public typecheck, lint, formatting, Chronus and documentation
  generation passed (preexisting missing-documentation warnings retained).
  [94 -> 117 compatibility delta](refresh-20261105/candidate-delta.json)
  and [117 -> 117 inherited-operation delta](refresh-20261105-inherited/candidate-delta.json)
  keep both frozen candidates distinct. Earlier 94/112/214 findings and
  controls are historical, not competing current conclusions.
  [Independent final local readiness review](inherited-20261105/readiness.json)
  found no significant issues; it is not a new formal GitHub A/B review.
  [Replay and publication verification](replay.md) distinguish saved-data checks
  from fresh execution; fully transitive locked regeneration is not claimed.
