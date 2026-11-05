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

| Count                                                                        | Swagger linter | TypeSpec linter |
| ---------------------------------------------------------------------------- | -------------: | --------------: |
| Reported diagnostics                                                         |      **1,314** |          **94** |
| Retained diagnostic records after description/title-only overchecks excluded |        **978** |          **94** |

**Assessed coverage: partial coverage, not functional equivalence.** The
[record-level assessment](gap-investigation.md#assessed-diagnostic-records)
excludes **336 confirmed description/title-only overchecks** from Swagger.
Every contributing helper occurrence must have a same-name PUT candidate
equivalent except for those annotations. Both rows count original reported
records, without regrouping or source-target deduplication. The TypeSpec linter
has no annotation-equality predicate, so this filter excludes none of its
94 findings.

The **978 retained Swagger records** comprise **927 other schema inequalities,
49 absent leaf names and 2 absent PATCH bodies**. The **94 TypeSpec records**
comprise **92 property-presence and 2 body warnings**. These numbers establish
one measured false-positive exclusion and the remaining check families, **not
confirmed service-defect totals or matched violations**. Type compatibility and
individual API-version coverage remain missing; unsupported shapes remain
unassessed.

**Complete comparable violation totals and a coverage percentage remain
unassessed:** the remaining records lack complete cross-engine pairing by
project, API version, operation, check and semantic target. They are not all
false positives or missing TypeSpec checks. Request visibility, authored
suppression and source/emitted shape also affect the results.
See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the
quantified exclusions, retained groups and unresolved limits.

## 3. Function-level coverage

| Behavior                                                                            | Result                              | Rationale                                                                                                                                                                                                                                                        |
| ----------------------------------------------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Extra PATCH JSON leaf; compliant subset                                             | Covered in supported scope          | [Violating/compliant controls](simplification.md#claim-to-test-mapping) establish missing-name reporting and subset acceptance for supported paired source bodies.                                                                                               |
| Absent or empty PATCH body                                                          | Covered                             | The [empty-body example](gap-investigation.md#gap-example-existing-empty-patch-is-not-an-absent-body-parameter) reports an existing object with no effective input leaves, unlike the Swagger linter's body-parameter-count bug.                                 |
| Nonempty PATCH with absent/void PUT input                                           | Covered                             | [Body controls and validation](simplification.md#local-validation) retain reporting of effective PATCH leaves when PUT has no input.                                                                                                                             |
| Nested/inherited writable leaves, encoded names and request visibility              | Covered in supported scope          | [Focused controls](simplification.md#claim-to-test-mapping) retain source traversal; [BillingTrust](gap-investigation.md#billingtrust-0-swagger--1-typespec) demonstrates why PUT read-only fields do not satisfy request membership.                            |
| Same-name metadata differences                                                      | Intentionally not enforced          | The [CodeSigning replay](gap-investigation.md#gap-example-metadata-only-inequality-in-codesigning) proves that metadata inequality can falsely report a missing name. Presence policy does not require whole-schema equality.                                    |
| Same-name incompatible types                                                        | Missing                             | The [unequal-type control](gap-investigation.md#exact-emitted-side-accounting) confirms that name matching also accepts incompatible types; avoiding metadata noise does not implement type compatibility.                                                       |
| Individual API-version availability, historical names/types and operation selection | Missing/deferred                    | The [source-only differences](simplification.md#corpus-differences) show lost historical checks and unreconstructed names/types; the authorized narrower policy defers shared handling to #5875.                                                                 |
| Unsupported/ambiguous top-level bodies                                              | Unassessed                          | The [object-body gate](gap-investigation.md#swagger-higher-outliers-and-remaining-limits) skips these shapes; equivalent behavior is not established or compiler-prevented.                                                                                      |
| Authored suppressions and shared source targets                                     | Retained; correspondence unassessed | [Quota's authored suppression](gap-investigation.md#quota-2-swagger--0-typespec) explains configured silence. [Source-target accounting](gap-investigation.md#swagger-higher-outliers-and-remaining-limits) does not establish emitted-operation correspondence. |

[Current semantic boundaries and controls](simplification.md#claim-to-test-mapping)
support these scoped statements; they do not prove exhaustive policy parity.

## 4. Why diagnostic counts differ

These are **overlapping explanation groups, not numbers to add together**.
Counts below are raw diagnostics for the named check/context, not grouped
operations or matched defects. The TypeSpec column excludes unrelated warnings
in the same project and counts configured warnings, not predictions before
suppression. **Unassessed** means attribution is unsupported, not zero.
For annotation equality, `0` means that predicate is absent from the TypeSpec
linter; it does not assert zero presence warnings on corresponding source targets.
Each link gives the separate coverage, cause and recommended-action assessment.

| Difference (with evidence)                                                                                                   | Swagger diagnostics | TypeSpec diagnostics for the same check | Recommended action and rationale                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------: | --------------------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Description/title-only overchecks](gap-investigation.md#assessed-diagnostic-records)                                        |                 336 |                                       0 | Confirmed annotation-only false missing-property reports; exclude these records from the assessed row, not the raw observations. Retain the TypeSpec policy of not comparing annotations. This exclusion requires an annotation-only candidate for **every** helper occurrence.                                      |
| [Remaining same-name schema inequalities](gap-investigation.md#assessed-diagnostic-records)                                  |                 927 |                              unassessed | Retain **925** records without an annotation-only candidate and **2** mixed-occurrence records. Their semantic disposition is not established by this filter. Actual type compatibility remains missing; do not replace its separate policy/design with whole-schema equality or declare these 927 records harmless. |
| [EdgeActions: opaque wrapper](gap-investigation.md#edgeactions-4-swagger--0-typespec)                                        |                   1 |                                       0 | Request visibility and leaf extraction differ. A missing wire property is unestablished; investigate effective membership before proposing a rule/spec fix. The project's other 3 Swagger findings are schema inequalities, not wrapper findings.                                                                    |
| [Quota: suppressed absent PATCH body](gap-investigation.md#quota-2-swagger--0-typespec)                                      |                   1 |                                       0 | The missing-body check is covered but authored suppression prevents a configured warning. Preserve suppression; no duplicate check is warranted. The project's other Swagger finding is a schema inequality.                                                                                                         |
| [BillingTrust: request membership](gap-investigation.md#billingtrust-0-swagger--1-typespec)                                  |                   0 |                                       1 | Source request-membership policy is retained: PUT's `kind` is read-only while PATCH's is request-visible. **Reject a visibility/discriminator relaxation** based on shared-schema presence; any changed input contract needs a spec-owner decision.                                                                  |
| [NetApp: existing empty PATCH object](gap-investigation.md#gap-example-existing-empty-patch-is-not-an-absent-body-parameter) |                   0 |                                       1 | Covered by TypeSpec; retain the empty-body check rather than copy the Swagger bug that counts body parameters instead of properties. The project's 49 Swagger schema inequalities are a separate cause.                                                                                                              |
| [NetApp: historical source name](gap-investigation.md#gap-example-source-names-are-not-historical-wire-names)                |          unassessed |                                       1 | Historical-name handling is missing/deferred; no exact emitted counterpart is established. Use shared #5875, not a local alias special case.                                                                                                                                                                         |
| [Source/API-version scope](simplification.md#corpus-differences)                                                             |          unassessed |                              unassessed | Missing version-specific coverage remains deferred, not repaired. The authorized source-only change removed 18 warnings and added 0 across nine projects; those deltas are not attributed counterpart counts. Prefer shared #5875 over bespoke version logic.                                                        |
| [Remaining correspondence and unsupported shapes](gap-investigation.md#swagger-higher-outliers-and-remaining-limits)         |                  49 |                              unassessed | These absent-leaf findings span 18 projects and include the EdgeActions wrapper. Do not classify all as Swagger bugs or missing TypeSpec checks: exact operation/version/source/payload attribution and unsupported-body coverage remain unassessed. No additional production fix follows from totals alone.         |

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
  aggregation/attribution limits. The
  [new assessment receipt](assessment-20261105/results.json) accounts for
  every original diagnostic and pins both saved inputs by hash. Its
  [tested offline replay](gap-investigation.md#assessed-diagnostic-records)
  removes only proven annotation-only overchecks; it is not a new lint run
  or general cross-engine normalization.
- **Population and directional gaps:** 335 Swagger-affected projects, 33
  TypeSpec-affected, 32 overlapping, 303 Swagger-only and 1 TypeSpec-only.
  Swagger counts are higher in 330 projects, TypeSpec in 1; 156 have equal
  counts, including 151 with neither reporting. Directional excesses are
  1,221 and 1; the absolute per-project gap is 1,222, not the net 1,220.
  Relative gap is `abs(TypeSpec - Swagger) / max(TypeSpec, Swagger, 1)`.
  [Independent accounting](refresh-20261104/provenance/harness-crosscheck.json)
  agrees with the [saved summary](refresh-20261104/staging-comparison/summary.json)
  on all 487 projects. After the narrow annotation filter, directional excesses
  are 891 Swagger / 7 TypeSpec, with absolute per-project gap 898, not net 884;
  [the assessed breakdown](gap-investigation.md#assessed-diagnostic-records)
  retains both directions. Equal-count projects are not automatically semantic matches.
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
