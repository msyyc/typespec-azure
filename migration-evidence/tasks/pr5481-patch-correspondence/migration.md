# PatchPropertiesCorrespondToPutProperties migration

## 1. Conclusion and scope

The TypeSpec linter
`@azure-tools/typespec-azure-resource-manager/arm-resource-patch` is **not
functionally equivalent** to Swagger linter
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
It compares writable JSON leaf **names**, not whole leaf schemas, so incompatible
same-name types can pass. Empty PATCH/missing PUT behavior, historical shape
handling, traversal, activation, and diagnostic identity also differ. Controlled
examples demonstrate inheritance and historical-shape false-positive mechanisms.
The previously missing Swagger observations are now supplied by a separately
sealed staging supplement over the **unchanged** production baseline.
The measured comparison is complete for the frozen population, but source and
emitted-version policies are not aligned; counts do not establish parity.

## 2. Actual coverage

The staging evaluation assessed all **649 retained Swagger inputs from 487 ARM
projects**, with **0 failed inputs** and no Swagger regeneration. It is combined
with the unchanged, content-verified native execution: **487 successful
projects, 0 failed or unassessed**. This is saved-observation reanalysis, not a
new native run.

| Count                  | Swagger linter | TypeSpec linter |
| ---------------------- | -------------: | --------------: |
| Reported diagnostics   |      **1,314** |         **214** |
| Projects with findings |        **335** |          **42** |

There are **41 overlapping projects, 294 Swagger-only projects, and 1
TypeSpec-only project**. These are observed project sets, not diagnostic matches.
No justified cross-engine common-unit count is available. See the
[complete staging/native project inventory](staging-comparison/projects.json),
[all differing diagnostic groups](staging-comparison/differences.md), and
[independently cross-checked summary](staging-comparison/summary.json).
The original production shard remains absent, meaning not evaluated, not zero.

## 3. Function-level coverage

| Behavior                                                | Result                                                                                                             |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Extra PATCH JSON leaf; compliant subset                 | Covered by executed TypeSpec controls: 1 / 0 findings.                                                             |
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

Swagger reports more findings in **325 projects**, TypeSpec in **3**, and **159**
have equal raw counts, including 151 with no findings on either side. Summed
project-wise Swagger excess is **1,183**, TypeSpec excess **83**, and absolute
gaps **1,266**. The net 1,100 difference must not cancel opposing gaps or be
called 1,100 missed native defects. Per-project signed, absolute and relative
gaps use `abs(TypeSpec - Swagger) / max(TypeSpec, Swagger, 1)`.

The [complete gap investigation](gap-investigation.md) inspects every one-sided
project and outliers in both directions. It classifies actual Swagger
whole-schema/body-policy findings separately from native leaf-name warnings,
and preserves Spectral's identical-record deduplication rather than counting
every repeated helper return as a reported diagnostic.
The Swagger records comprise **1,263 matching-name schema inequalities,
49 absent leaf names, and 2 absent PATCH bodies**. These are Swagger-side
predicate categories, not counts attributed to native findings.

The three native-higher projects are DevCenter (**13 / 90** Swagger/TypeSpec),
CDN (**4 / 9**) and BillingTrust (**0 / 1**). The
[source-backed examples](gap-investigation.md#native-higher-projects) investigate
inherited-writable traversal and source visibility/discriminator behavior.
Managed Network Fabric (**93 / 13**) is the largest Swagger-higher gap.
The unchanged native findings comprise 212 missing JSON-leaf names, one empty
PATCH body and one absent PATCH body. The
[original corpus examples](corpus-examples.md) and
[semantic controls](semantic-evidence.md) remain separate evidence; neither
equal counts nor leaf-name coincidence proves exact correspondence or validity
of every finding.

## NOTES

- Assessed current PR head: `7baca4db3d7824c24c30961c50c3f47a6df8d958`.
  This task updates evidence and the PR description, not rule behavior.
  [Rule-change disposition and limitations](evidence-details.md#rule-change-disposition).
- Frozen specs: `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`;
  shared baseline `swagger-arm-20261026-2cd3c5dd`, metadata commit
  `317e703b3e380d3b64e0dacb3a2c6fc0651de253`.
  All 649 retained Swagger logs explicitly disable the original staging-only
  rule. New staging data is separate, not an edit to those observations.
  [Pinned sources, supplement identities and runtime provenance](evidence-details.md).
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
