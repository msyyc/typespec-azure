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
It intentionally avoids Swagger overchecking of documentation, defaults,
method-appropriate mutability and read-only PATCH fields. It also detects empty
PATCH objects that the Swagger linter incorrectly accepts.

## 2. Actual coverage

The assessment covers **487 ARM projects, with 0 TypeSpec failures**, and
**649 retained Swagger inputs, with 0 staging-evaluation failures**.
Reported diagnostics are total individual findings across that population,
not project counts.

| Count                                                | Swagger linter | TypeSpec linter |
| ---------------------------------------------------- | -------------: | --------------: |
| Reported diagnostics                                 |      **1,314** |          **94** |
| Retained records after verified overcheck exclusions |        **182** |          **94** |

The second row filters Swagger overchecks only; **94 is unchanged reported
TypeSpec output, not 94 independently validated service defects**.

**Assessed coverage: partial, not equivalent.** The
[record-level assessment](gap-investigation.md#assessed-diagnostic-records)
excludes **1,132 Swagger overchecks**, not merely the previously identified
336 description/title-only reports. The exclusions are **339 documentation,
144 default-value, 612 input-compatible mutability, and 37 additional
read-only PATCH reports**. They do not establish missing names or incompatible
request types. Raw observations are preserved.

**What does TypeSpec still not check?** Of the **182 remaining Swagger records**:

- **131 concern unequal same-name schemas.** TypeSpec stores leaf names, not
  their type/constraint contracts, so it has **no general compatibility check**
  for these differences. They are investigation candidates, **not 131 proved
  valid violations**: some still concern visibility, extensions or legitimate
  PATCH shapes.
- **49 concern absent emitted leaf names.** TypeSpec already implements
  missing-name checking; these are **not 49 automatically ignored findings**.
  Their exact correspondence to the 92 reported TypeSpec presence warnings
  remains unassessed.
- **2 concern absent PATCH bodies. Both are covered:** ProviderHub has
  **1 reported** warning; Quota has **1 verified valid-but-suppressed** finding.
  Quota receives coverage credit, without changing its raw reported zero.

**The total number of valid violations missed by TypeSpec is not yet
established.** In particular, **182 - 94 = 88 is not a missed-diagnostic count**.
Swagger reports emitted-operation records; TypeSpec reports source targets,
including an empty-body warning and a historical-name warning with separate
causes. The remaining records still need semantic validation and matching by
API version, operation and source target. Coverage percentages remain
unassessed rather than invented.

The concrete fixes are to **add wire-type/constraint compatibility**, **evaluate
versioned names/types/operations through #5875**, and **resolve the 49
name/shape correspondences before changing traversal**. See
[Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the counts,
reasons and recommended fixes.

## 3. Function-level coverage

| Behavior                                                                            | Result                              | Rationale                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Extra PATCH JSON leaf; compliant subset                                             | Covered in supported scope          | [Violating/compliant controls](simplification.md#claim-to-test-mapping) establish missing-name reporting and subset acceptance for supported paired source bodies.                                                                                                                 |
| Absent or empty PATCH body                                                          | Covered                             | The [empty-body example](gap-investigation.md#gap-example-existing-empty-patch-is-not-an-absent-body-parameter) reports an existing object with no effective input leaves, unlike the Swagger linter's body-parameter-count bug.                                                   |
| Nonempty PATCH with absent/void PUT input                                           | Covered                             | [Body controls and validation](simplification.md#local-validation) retain reporting of effective PATCH leaves when PUT has no input.                                                                                                                                               |
| Nested/inherited writable leaves, encoded names and request visibility              | Covered in supported scope          | [Focused controls](simplification.md#claim-to-test-mapping) retain source traversal; [BillingTrust](gap-investigation.md#billingtrust-0-swagger--1-typespec) demonstrates why PUT read-only fields do not satisfy request membership.                                              |
| Same-name metadata differences                                                      | Intentionally not enforced          | The [CodeSigning replay](gap-investigation.md#gap-example-metadata-only-inequality-in-codesigning) proves that metadata inequality can falsely report a missing name. Presence policy does not require whole-schema equality.                                                      |
| Same-name incompatible types                                                        | Missing; real rule gap              | The [unequal-type control and fix](gap-investigation.md#remaining-candidates-and-fixes) show that `string` versus `int32` passes name-only comparison. Preserve property/type contracts and compare wire compatibility; do not copy whole-schema equality.                         |
| Individual API-version availability, historical names/types and operation selection | Missing/deferred                    | The [source-only controls and corrected case classification](simplification.md#corpus-differences) show unchecked availability and operation history. KeyVault/DNS have renamed predecessors, not proven historical absences. Shared version resolution remains deferred to #5875. |
| Unsupported/ambiguous top-level bodies                                              | Unassessed                          | The [object-body gate](gap-investigation.md#swagger-higher-outliers-and-remaining-limits) skips these shapes; equivalent behavior is not established or compiler-prevented.                                                                                                        |
| Authored suppressions and shared source targets                                     | Retained; correspondence unassessed | [Quota's authored suppression](gap-investigation.md#quota-2-swagger--0-typespec) explains configured silence. [Source-target accounting](gap-investigation.md#swagger-higher-outliers-and-remaining-limits) does not establish emitted-operation correspondence.                   |

[Current semantic boundaries and controls](simplification.md#claim-to-test-mapping)
support these scoped statements; they do not prove exhaustive policy parity.

## 4. Why diagnostic counts differ

The following rows are **disjoint and account for all 1,314 Swagger records**:
**1,132 excluded + 131 schema candidates + 49 name candidates + 2 body checks**.
No grouping or cross-engine deduplication is applied. For schema-comparison
rows, `0` means TypeSpec does not implement that comparison, not zero unrelated
presence warnings on the same operation. The body row explicitly includes the
verified suppressed finding; all other observed counts remain configured output.

| Difference (with evidence)                                                                                               | Swagger diagnostics | TypeSpec diagnostics for the same check | Recommended action and rationale                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------: | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Documentation-only overchecks](gap-investigation.md#assessed-diagnostic-records)                                        |                 339 | 0                                       | **Exclude; no TypeSpec fix.** The same name/type/constraints exist; only description, title or external documentation differs.                                                                                                                                                                                                             |
| [Default-only overchecks](gap-investigation.md#gap-example-default-is-not-a-different-type)                              |                 144 | 0                                       | **Exclude; no TypeSpec fix.** PUT `enabled?: boolean = true` and PATCH `enabled?: boolean` have the same type. Defaults need not be identical across methods.                                                                                                                                                                              |
| [Input-compatible mutability overchecks](gap-investigation.md#gap-example-mutability-metadata-is-not-a-missing-property) |                 612 | 0                                       | **Exclude; preserve visibility checks.** Every occurrence has an otherwise equivalent PUT candidate allowing create/update and PATCH allowing update. Metadata order/omission or method differences do not imply an absent property or incompatible type.                                                                                  |
| [Additional read-only PATCH overchecks](gap-investigation.md#gap-example-read-only-patch-leaves-are-not-input)           |                  37 | 0                                       | **Exclude; keep TypeSpec request filtering.** Every contributing PATCH leaf is explicitly read-only, hence outside PATCH input. Do not add a type warning for a field clients cannot send.                                                                                                                                                 |
| [Remaining same-name schema differences](gap-investigation.md#remaining-candidates-and-fixes)                            |                 131 | 0                                       | **Compatibility checking is missing.** The current helper accepts a matching name without comparing types/constraints. Add a request-aware wire-compatibility check, allowing PATCH optionality and ignoring annotations/defaults. Validate these candidates before calling them valid missed violations or predicting new warning totals. |
| [Absent emitted leaf names](gap-investigation.md#swagger-higher-outliers-and-remaining-limits)                           |                  49 | unassessed                              | **Check implemented; exact gap unresolved.** Match operation/version/source/writable leaf identities. Repair demonstrated extraction or unsupported-body gaps only; do not infer 49 misses from the Swagger count.                                                                                                                         |
| [Absent PATCH bodies](gap-investigation.md#missing-body-correspondence)                                                  |                   2 | 1 reported + 1 suppressed               | **Covered; no new rule needed.** ProviderHub reports; Quota has a valid suppressed finding. Preserve suppression and give it assessment credit.                                                                                                                                                                                            |

**Version handling is a separate real gap, not an extra row to add to 1,314.**
Source-only evaluation can miss older-operation violations or miscompare
historical names/types. Resolve active operations, availability and historical
wire contracts through [#5875](https://github.com/Azure/typespec-azure/issues/5875).
The [18 removed source warnings](simplification.md#corpus-differences) are not
18 proved lost violations; KeyVault/DNS have renamed predecessors.

The 94 TypeSpec warnings also have separate causes:
[NetApp's empty PATCH](gap-investigation.md#gap-example-existing-empty-patch-is-not-an-absent-body-parameter)
correctly reports what Swagger misses;
[BillingTrust's request membership](gap-investigation.md#billingtrust-0-swagger--1-typespec)
must not be relaxed just to equalize counts; and
[NetApp's historical-name warning](gap-investigation.md#gap-example-source-names-are-not-historical-wire-names)
needs shared version resolution. Subtracting these source totals from emitted
Swagger totals cannot identify missed defects.

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
  retain the immutable Swagger observations. This refresh generated no Swagger
  and ran no new TypeSpec corpus; the pinned Swagger resolver/ruleset was
  replayed only to inspect saved values, not replace the baseline or supplement.
- **Counting limits:** all 94 configured TypeSpec warnings are paired-body
  message families: 92 missing-property, 1 empty body, 1 absent body; older
  tags/resource-subset messages contribute none in this run.
  There are 94 full diagnostic records but 84 source positions. Swagger has
  740 project/file/path identities, also 740 dropping the file. Neither is a
  common violation unit. The [complete project/target inventory](refresh-20261104/staging-comparison/differences.md)
  and [grouped investigation](gap-investigation.md) retain raw findings and
  aggregation/attribution limits. The
  [assessment receipt](assessment-20261105/results.json) accounts for
  every original diagnostic and pins both saved inputs by hash. Its
  [tested offline replay](gap-investigation.md#assessed-diagnostic-records)
  now removes documentation/default/input-compatible-mutability and additional
  read-only PATCH overchecks. The [schema-value trace](assessment-20261105/schema-values.json)
  supplies actual type, mutability, read-only and default values, rather than
  inferring them from differing-key names. It is not a new TypeSpec run or
  general cross-engine normalization.
- **Population and directional gaps:** 335 Swagger-affected projects, 33
  TypeSpec-affected, 32 overlapping, 303 Swagger-only and 1 TypeSpec-only.
  Swagger counts are higher in 330 projects, TypeSpec in 1; 156 have equal
  counts, including 151 with neither reporting. Directional excesses are
  1,221 and 1; the absolute per-project gap is 1,222, not the net 1,220.
  Relative gap is `abs(TypeSpec - Swagger) / max(TypeSpec, Swagger, 1)`.
  [Independent accounting](refresh-20261104/provenance/harness-crosscheck.json)
  agrees with the [saved summary](refresh-20261104/staging-comparison/summary.json)
  on all 487 projects. After the broader overcheck filter, directional excesses
  are 105 Swagger / 17 TypeSpec, with absolute per-project gap 122, not net 88;
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
  This report refresh adds tested offline classification, not new production
  results: the [extractor](assessment-20261105/inspect_gap.mjs) inspected 341
  hash-verified saved Swagger inputs in 192.7 seconds, checking all 1,263
  original schema-difference records against the pinned replay and runtime.
  All 14 focused assessment tests passed.
  [Commands, claim-to-test mapping, runtime and recovery](simplification.md)
  distinguish full execution, saved-data replay and historical controls.
  Fully transitive locked regeneration is not claimed.
