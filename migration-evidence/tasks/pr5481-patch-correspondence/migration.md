# PatchPropertiesCorrespondToPutProperties migration

## 1. Conclusion and scope

The TypeSpec rule `@azure-tools/typespec-azure-resource-manager/arm-resource-patch`
migrates Swagger linter rule
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
**The migration is not fully functionally equivalent.** The TypeSpec linter
checks property presence and nonempty input for supported source-model bodies,
not each API version or general type compatibility. Version-specific coverage
is missing and deferred to [#5875](https://github.com/Azure/typespec-azure/issues/5875);
unsupported shapes and remaining source-to-Swagger correspondence are unassessed.
It intentionally avoids two Swagger linter bugs: metadata-only schema
differences reported as missing properties, and existing empty PATCH objects
accepted because the implementation counts body parameters rather than properties.

## 2. Actual coverage

The assessment covers **487 ARM projects, with 0 TypeSpec failures**, and
**649 retained Swagger inputs, with 0 staging-evaluation failures**.
Reported diagnostics are total individual findings across that population,
not project counts.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |      **1,314** |          **94** |

The gap includes schema-comparison differences, request visibility, authored
suppression and source/API-version scope. Exact cross-engine attribution remains
unresolved; comparison in a common operation/violation unit is **unassessed**,
not normalized to matching counts. See
[Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the causes,
decisions and remaining limits.

## 3. Function-level coverage

| Behavior                                                                            | Coverage                                                                                                                                                           |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Extra PATCH JSON leaf; compliant subset                                             | Covered for supported paired source bodies: missing names report; a matching subset passes.                                                                        |
| Absent or empty PATCH body                                                          | Covered. An existing object with no effective input leaves reports, unlike the Swagger linter's empty-body bug.                                                    |
| Nonempty PATCH with absent/void PUT input                                           | Covered: each effective PATCH leaf reports as absent from PUT.                                                                                                     |
| Nested/inherited writable leaves, encoded names and request visibility              | Covered by focused violating/compliant controls. PUT read-only fields do not satisfy request-input membership.                                                     |
| Same-name metadata/type differences                                                 | Names pass. Metadata equality is not required by the presence policy; incompatible types are also **not checked**, so this is not full Swagger-predicate coverage. |
| Individual API-version availability, historical names/types and operation selection | **Missing/deferred:** source-only comparison can miss version-specific mismatches or report historical declarations.                                               |
| Unsupported/ambiguous top-level bodies                                              | Skipped; equivalent coverage is **unassessed**, not compiler-prevented.                                                                                            |
| Authored suppressions and shared source targets                                     | Retained. Suppressed warnings and source-target deduplication are not evidence of equivalent emitted-operation coverage.                                           |

[Current semantic boundaries and controls](simplification.md#claim-to-test-mapping)
support these scoped statements; they do not prove exhaustive policy parity.

## 4. Why diagnostic counts differ

These are **overlapping explanation groups, not numbers to add together**.
Project totals include findings outside the highlighted cause. Unassessed
counterpart counts are not zero. Each link gives the separate coverage,
cause and recommended-action assessment.

| Difference group                                                                                                     | Swagger / TypeSpec findings                                                                                                | Coverage and decision                                                                                                                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Same-name schema inequalities](gap-investigation.md#exact-emitted-side-accounting)                                  | 1,263 Swagger findings; corresponding TypeSpec subset unassessed. The 301 schema-only Swagger-only projects total 876 / 0. | Do **not** port whole-schema equality merely to match counts: metadata-only mismatches are false missing-property reports. Actual type incompatibility is a distinct, unchecked behavior, not automatically a Swagger false positive; broad type checking is outside this PR's presence policy. |
| [EdgeActions: opaque wrapper](gap-investigation.md#edgeactions-4-swagger--0-typespec)                                | 4 / 0 project total: 3 schema inequalities and 1 wrapper-name finding                                                      | Request visibility and leaf extraction differ. No missing wire property or required TypeSpec fix is established; retain the boundary and investigate effective source/emitted membership before proposing one.                                                                                  |
| [Quota: authored suppression](gap-investigation.md#quota-2-swagger--0-typespec)                                      | 2 / 0 project total: 1 schema inequality and 1 absent-PATCH-body finding                                                   | The missing-body check exists but is suppressed in source. Preserve the authored suppression; no duplicate check or linter fix is warranted.                                                                                                                                                    |
| [BillingTrust: request membership](gap-investigation.md#billingtrust-0-swagger--1-typespec)                          | 0 / 1                                                                                                                      | PUT's `kind` is read-only while PATCH's is request-visible. **Reject a TypeSpec visibility/discriminator relaxation**: shared Swagger schema presence does not establish PUT input membership.                                                                                                  |
| [NetApp: empty body and historical name](gap-investigation.md#netapp-49-swagger--2-typespec)                         | 49 / 2 project total: 49 Swagger schema inequalities; TypeSpec reports 1 empty body and 1 source-name mismatch             | Keep the empty-body check rather than copy the Swagger bug. The historical-name mismatch is a source/version limitation; defer version-aware handling, not the valid empty-body check.                                                                                                          |
| [Source/API-version scope](simplification.md#corpus-differences)                                                     | Nine changed projects total 182 / 14; the source-only change removed 18 TypeSpec findings and added 0                      | Source-only scope was explicitly authorized, including loss of historical assessment. **Missing version-specific coverage remains deferred**, not repaired; use shared #5875 rather than restore bespoke version logic. This does not explain every finding in those projects.                  |
| [Remaining correspondence and unsupported shapes](gap-investigation.md#swagger-higher-outliers-and-remaining-limits) | 49 absent-leaf Swagger findings across 18 projects; corresponding TypeSpec subset unassessed                               | Do not declare these all Swagger bugs or all missing TypeSpec checks. Trace exact operation/version/source identities and effective payloads before recommending an owning-rule, spec or comparison fix. No additional production fix is established by these counts alone.                     |

Fewer warnings do **not** establish better coverage. The 18 removals include
intentional coverage losses, not 18 proven false positives. A no-change/defer
recommendation does not close the missing coverage or establish equivalence.

## NOTES

- **Assessed source and validation:** the corpus tested production commit
  [`51cc68db`](https://github.com/Azure/typespec-azure/commit/51cc68db6897b286b10ad6a23266e9c62a4f422d).
  [PR #5481](https://github.com/Azure/typespec-azure/pull/5481) head
  [`4f62f17f`](https://github.com/Azure/typespec-azure/commit/4f62f17ff8a4d3afcbc7fd548112c5fb42402464)
  adds only two tests; production source is unchanged. This report refresh
  reuses that verified assessment and changes no rule code or corpus inputs.
  [Execution metadata](refresh-20261104/task.json),
  [all project receipts](refresh-20261104/runs/full-corpus/manifest.json) and
  [package/runtime provenance](refresh-20261104/provenance/artifact-provenance.json)
  pin specs, compiler/library closure, tooling and all 15 package artifacts.
- **Audience and execution:** ARM, not RPaaS-only. The Swagger linter is an
  error-severity OAS2 staging rule; the production baseline **did not evaluate
  it**. The 1,314 findings come from the separate, parent-bound staging
  supplement over unchanged retained Swagger, not a reinterpreted production
  zero. The TypeSpec linter retains the existing rule's warning severity and
  activation; this comparison explicitly selects it and retains authored
  suppressions. [Original registration and activation evidence](semantic-evidence.md#original-contract-and-activation).
- **Scope and inputs:** frozen specs `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`;
  TypeSpec `source`/`target-only`, `frozen-reference`, no filter/limit,
  concurrency 2. This is not a projection aligned with latest-emitted Swagger.
  [Baseline/supplement identities and recovery](evidence-details.md#original-swagger-policy-and-frozen-evidence)
  retain the immutable Swagger evidence; neither Swagger generation nor
  staging evaluation was repeated for this refresh.
- **Counting limits:** all 94 configured TypeSpec warnings are paired-body
  message families: 92 missing-property, 1 empty body, 1 absent body; older
  tags/resource-subset messages contribute none in this run.
  There are 94 full diagnostic records but 84 source positions. Swagger has
  740 project/file/path identities, also 740 dropping the file. Neither is a
  common violation unit. The [complete project/target inventory](refresh-20261104/staging-comparison/differences.md)
  and [grouped investigation](gap-investigation.md) retain raw findings and
  aggregation/attribution limits.
- **Population and directional gaps:** 335 Swagger-affected projects, 33
  TypeSpec-affected, 32 overlapping, 303 Swagger-only and 1 TypeSpec-only.
  Swagger counts are higher in 330 projects, TypeSpec in 1; 156 have equal
  counts, including 151 with neither reporting. Directional excesses are
  1,221 and 1; the absolute per-project gap is 1,222, not the net 1,220.
  Relative gap is `abs(TypeSpec - Swagger) / max(TypeSpec, Swagger, 1)`.
  [Independent accounting](refresh-20261104/provenance/harness-crosscheck.json)
  agrees with the [saved summary](refresh-20261104/staging-comparison/summary.json)
  on all 487 projects. Equal-count projects are not automatically semantic matches.
- **Evidence continuity:** current findings are 112 -> 94, with 18 removals
  and no additions. [Source-only differences, examples and policy decisions](simplification.md#corpus-differences)
  retain every changed target; the earlier 214 -> 112 inheritance/body
  corrections remain [historical validation](fix-results.md), not competing
  current totals. The affected union is the same 336 projects whose 497
  Swagger inputs were replayed; [reanalysis](refresh-20261104/reanalyze-schema.py)
  joins unchanged classifications to current project counts without
  claiming source-diagnostic matches.
- **Executed checks and recovery:** 61 focused rule tests, 40 sample tests,
  14 registered-linter controls and 37 portable controls passed; 6 unrelated
  absent-rule fixtures were explicitly excluded. Builds, lint, formatting
  and Chronus passed. The native stage ran 07:09:08-07:33:09 UTC on
  2026-11-04 within a 10,800-second budget, under the shared corpus gate.
  [Commands, claim-to-test mapping, runtime and recovery](simplification.md)
  distinguish full execution, saved-data replay and historical controls.
  Fully transitive locked regeneration is not claimed.
