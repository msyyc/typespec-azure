# PatchPropertiesCorrespondToPutProperties migration

## 1. Conclusion and scope

The TypeSpec linter
`@azure-tools/typespec-azure-resource-manager/arm-resource-patch` is **not
functionally equivalent** to Swagger linter
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
It compares writable JSON leaf **names**, not whole leaf schemas, so incompatible
same-name types can pass. Empty PATCH/missing PUT behavior, historical shape
handling, traversal, activation, and diagnostic identity also differ; inheritance
and historical-shape handling can produce false positives.
The assessment covers frozen ARM source programs and retained latest-emitted
Swagger under separate version policies; exact diagnostic correspondence remains
**unassessed**.

## 2. Actual coverage

The assessment covers **487 ARM projects**: all **649 retained Swagger inputs**
were evaluated with **0 failed inputs**, and TypeSpec compilation succeeded for
**487 projects, with 0 failed or unassessed projects**. Diagnostic correspondence,
not project execution, remains unassessed.
Reported diagnostics are total individual findings across this population,
not project counts.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |      **1,314** |         **214** |

Whole-schema versus leaf-name checks, body policy, source traversal,
visibility and suppression explain evidenced differences. Source-version scope
also differs; exact cross-engine correspondence and a justified common counting
unit remain **unassessed**. See
[Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the grouped
evidence and remaining limitations.

## 3. Function-level coverage

| Behavior                                                | Result                                                                                                             |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Extra PATCH JSON leaf; compliant subset                 | Covered by executed TypeSpec violating and compliant controls.                                                     |
| Same name, incompatible type or unequal schema metadata | **Different:** TypeSpec accepts it; Swagger's schema-equality predicate can report it.                             |
| Absent PATCH body                                       | Covered; both predicates reject it.                                                                                |
| Existing empty PATCH object                             | **Different:** TypeSpec rejects it; Swagger's body-parameter count check accepts it when PUT has a body.           |
| Missing PUT body                                        | **Different:** Swagger reports it; TypeSpec skips correspondence after checking PATCH.                             |
| Nested/inherited writable properties                    | **Partial:** a controlled derived-read-only/inherited-writable shape produces a TypeSpec traversal false positive. |
| Version availability versus historical names/types      | **Partial:** added/removed availability is handled; historical rename/type-shape controls produce false positives. |
| Encoded names, visibility, unauthored discriminators    | Source-aware TypeSpec policy differs from comparing emitted schemas; not full emission parity.                     |
| Unsupported top-level bodies                            | TypeSpec skips arrays, dictionaries, ambiguous unions, and other unsupported shapes.                               |
| Occurrence identity and activation                      | Different source-target deduplication and broader warning activation versus staging-only Swagger errors.           |

[Semantic examples and evidence labels](semantic-evidence.md) distinguish
executed controls, existing tests, and source inspection. They do not establish
production prevalence.

## 4. Why diagnostic counts differ

The [complete differing-project inventory](staging-comparison/differences.md)
retains both linters' exact diagnostic groups and counts. The following entries
summarize the evidenced causes, not matched defects; counts are Swagger / TypeSpec.

| Differing project or diagnostic group                                                                                         | Reported counts                                                          | Cause and disposition                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [292 Swagger-only projects](gap-investigation.md#swagger-only-projects)                                                       | 796 / 0                                                                  | Matching-name, unequal-schema findings: the TypeSpec linter compares names only. Semantic non-equivalence; source-target correspondence remains unassessed.                           |
| [EdgeActions](gap-investigation.md#edgeactions-4-swagger--0-native)                                                           | 4 / 0                                                                    | Three `tags` schema inequalities and one opaque `properties` traversal/visibility difference. Evidenced policy differences, not four proven missing TypeSpec defects.                 |
| [Quota](gap-investigation.md#quota-2-swagger--0-native)                                                                       | 2 / 0                                                                    | One same-name schema inequality and one absent PATCH body with an authored TypeSpec suppression. Distinct predicate and suppression policies.                                         |
| [DevCenter](gap-investigation.md#devcenter-13-swagger--90-native)                                                             | 13 / 90                                                                  | Schema inequalities versus missing leaf-name warnings; an executed control establishes an inherited-writable traversal false-positive mechanism, not the validity of all 90 warnings. |
| [CDN](gap-investigation.md#cdn-4-swagger--9-native)                                                                           | 4 / 9                                                                    | Swagger `tags` schema inequalities and separate TypeSpec inherited-leaf warnings; source inspection supports the traversal asymmetry. No five-defect net interpretation.              |
| [BillingTrust](gap-investigation.md#billingtrust-0-swagger--1-native-the-only-native-only-project)                            | 0 / 1                                                                    | Writable PATCH discriminator versus read-only PUT source property, despite emitted `kind` on both sides. Source visibility differs from emitted-schema policy.                        |
| [Managed Network Fabric and other Swagger-higher outliers](gap-investigation.md#swagger-higher-outliers-and-remaining-limits) | Managed Network Fabric 93 / 13; other project counts in the linked table | Whole-schema comparison, historical source shapes and body policy describe different checks. Exact cross-engine correspondence remains unassessed.                                    |

[Emitted-side accounting](gap-investigation.md#exact-emitted-side-accounting)
classifies all 1,314 Swagger findings as 1,263 matching-name schema inequalities,
49 absent leaf names and 2 absent PATCH bodies. The TypeSpec findings comprise
212 missing leaf names, one empty PATCH body and one absent PATCH body.
These are separate predicate families, not attributed diagnostic pairs.
Spectral collapses 27 identical operation-target messages from repeated helper
returns; that captured engine behavior is not a new semantic deduplication.
The linked [source examples](corpus-examples.md) and
[semantic controls](semantic-evidence.md) retain historical-shape, body-policy
and traversal evidence. Full correspondence and policy parity remain unassessed;
the established semantic differences preclude functional equivalence.

## NOTES

- Assessed candidate: `7baca4db3d7824c24c30961c50c3f47a6df8d958`
  from [Azure/typespec-azure#5481](https://github.com/Azure/typespec-azure/pull/5481).
  This report refresh changes presentation only, not rule behavior or observations.
  [Rule-change disposition and limitations](evidence-details.md#rule-change-disposition).
- Frozen specs: `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`;
  shared baseline `swagger-arm-20261026-2cd3c5dd`, metadata commit
  `317e703b3e380d3b64e0dacb3a2c6fc0651de253`.
  All 649 retained Swagger logs explicitly disable the original staging-only
  rule. New staging data is separate, not an edit to those observations.
  [Pinned sources, supplement identities and runtime provenance](evidence-details.md).
- The separately sealed staging supplement supplies the selected Swagger rule's
  observations; its production shard remains absent, meaning **not evaluated**,
  not zero. This is saved-observation reanalysis, not a new TypeSpec run or
  Swagger regeneration.
- [Project inventory](staging-comparison/projects.json) and
  [independently cross-checked summary](staging-comparison/summary.json):
  335 Swagger-affected projects, 42 TypeSpec-affected, 41 overlapping,
  294 Swagger-only and 1 TypeSpec-only. These are project sets, not matches.
  Swagger counts are higher in 325 projects, TypeSpec in 3; 159 have equal
  counts, including 151 with neither linter reporting.
  Summed project-wise Swagger excess is 1,183, TypeSpec excess 83 and absolute
  gaps 1,266; the net 1,100 must not cancel opposing gaps.
  Relative gaps use `abs(TypeSpec - Swagger) / max(TypeSpec, Swagger, 1)`.
- TypeSpec policy: all-source versions, selected rule explicitly enabled in
  `target-only` mode, authored suppressions retained. This is not a projection
  aligned with the historical latest-emitted Swagger selection.
  Separate controls verify suppression and actual ruleset activation.
- Raw TypeSpec diagnostics: 214; distinct project/location/message records: 214.
  The analyzer's 192 source positions merge different leaf messages and are
  **not** 192 equivalent operations or a normalized Swagger comparison.
  Older resource-subset/tags/body checks coexist under this TypeSpec rule code;
  the observed full-corpus messages here are the paired-helper families.
- Swagger has 740 distinct project/file/JSON-path identities, also 740 after
  dropping the file. These location summaries and the 192 native source
  positions are different units, not normalized actionable checks.
- [Independent tooling PR #5932](https://github.com/Azure/typespec-azure/pull/5932)
  supplies reusable immutable staging data for all seven installed ARM/common
  staging-only Spectral rules. This report's mapping remains the single
  original rule to `arm-resource-patch`. The profile is direct Spectral
  evaluation, not the AutoRest staging pipeline or data-plane/RPaaS coverage.
- Eight fresh injected real-linter controls passed. Applicable portable harness
  controls: 37 passed / 6 unrelated absent-rule cases explicitly skipped;
  the initial six failures remain disclosed. Additional semantic controls use
  the helper directly and do not test the entire suppression pipeline.
  Extra-leaf/compliant-subset controls report 1 / 0 TypeSpec findings.
- [Evidence details](evidence-details.md),
  [real-service examples](corpus-examples.md), and
  [recovery/reanalysis instructions](replay.md) retain provenance, complete
  observations, validation boundaries, and source retention. Saved-data
  recovery is distinct from a full rerun; fully locked transitive regeneration
  is not claimed.
- The original [independent local review](provenance/local-review.json) found no blocking
  publication issues. Original [fresh-checkout recovery](provenance/recovery-verification.json)
  verified saved-data reanalysis, package bytes, and the shared-baseline asset;
  it did not repeat the corpus execution.
  [Supplement publication/recovery](provenance/staging-publication.json) and
  [staging evidence review](provenance/staging-evidence-review.json) record the
  separate follow-up checks.
