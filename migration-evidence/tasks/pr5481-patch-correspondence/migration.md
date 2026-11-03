# PatchPropertiesCorrespondToPutProperties migration

## 1. Conclusion and scope

The TypeSpec linter
`@azure-tools/typespec-azure-resource-manager/arm-resource-patch` migrates Swagger linter
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
**It covers the basic documented property-presence and nonempty-PATCH checks,
but full functional equivalence to that policy is not yet established: confirmed
TypeSpec missing-PUT, inherited-property and historical-shape gaps remain.**
The historical-shape false positives are accepted temporarily for this migration
under the shared [version-aware linting issue #5875](https://github.com/Azure/typespec-azure/issues/5875),
not fixed or counted as equivalent behavior.
The Swagger linter has two implementation bugs relative to its documentation:
whole-schema equality overchecks property presence, and counting body parameters
misses existing empty PATCH models. The TypeSpec linter does not reproduce those
bugs; schema inequality alone is not a migration defect.
This assessment covers ARM object-body correspondence, not general type
compatibility. Source-version and emitted-version scopes are not aligned, and
remaining visibility/traversal cases prevent a full corpus-parity claim.

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

The Swagger linter's schema-equality bug explains the schema-only findings;
its empty-body bug also hides a documented violation detected by TypeSpec.
Genuine TypeSpec defects and source-version, visibility and suppression
differences remain separate. Exact cross-engine correspondence and a justified
common counting unit remain **unassessed**. See
[Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the grouped
evidence and remaining limitations.

## 3. Function-level coverage

| Behavior                                                          | Result against the documented policy                                                                                                                                                                          |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Extra PATCH JSON leaf; compliant subset                           | **Covered:** executed violating and compliant TypeSpec controls.                                                                                                                                              |
| Same name, unequal type, description or other schema metadata     | **No TypeSpec equality check required by this rule:** property presence does not require identical schemas. General type compatibility is outside this assessment.                                            |
| Absent PATCH body                                                 | **Covered:** both predicates reject it.                                                                                                                                                                       |
| Existing empty PATCH object                                       | **TypeSpec is correct; Swagger bug:** an existing body parameter is not proof of at least one property.                                                                                                       |
| Nonempty PATCH with a bodyless paired PUT                         | **TypeSpec fix required:** it silently skips correspondence; the authored control violates documented presence.                                                                                               |
| Inherited writable PUT properties behind read-only direct members | **TypeSpec fix required:** an executed control reports a shared, present property as missing.                                                                                                                 |
| Historical property renames and nested type shapes                | **Known false positives; accepted temporarily:** defer version-specific shape evaluation to [#5875](https://github.com/Azure/typespec-azure/issues/5875). Executed controls still demonstrate the limitation. |
| Encoded names, request visibility and synthesized discriminators  | Encoded-name controls exist; **wire/request-shape parity remains incomplete**, including the source-backed BillingTrust discrepancy below.                                                                    |
| Unsupported top-level bodies                                      | **Unassessed:** skipped arrays, dictionaries and ambiguous unions are not proven compiler-prevented or approved exclusions.                                                                                   |
| Source-target deduplication, suppressions and activation          | Explain some reporting differences, not missing-property semantics; no one-to-one diagnostic count is claimed.                                                                                                |

[Semantic examples and evidence labels](semantic-evidence.md) distinguish
executed controls, existing tests, and source inspection. They do not establish
production prevalence.

## 4. Why diagnostic counts differ

The [complete differing-project inventory](staging-comparison/differences.md)
retains exact targets and both linters' counts. The following groups overlap;
they are explanations, not additive matched-defect totals.

**Swagger schema-equality bug, not missing TypeSpec coverage.**
The documentation requires PATCH properties to be present in PUT.
The [pinned implementation][swagger-function] instead calls
`_.differenceWith(..., _.isEqual)` on whole leaf-schema objects. It can therefore
say a property is absent when that name exists but its description, mutability
or type differs. The [executed controls](semantic-evidence.md#same-nametype-unequal-description)
produce **1 Swagger / 0 TypeSpec** finding for different descriptions; a
[separate type control](semantic-evidence.md#same-name-unequal-scalar-type)
has the same result. Neither difference alone violates documented presence.
The TypeSpec rule must not acquire whole-schema equality merely to match this bug.

The [saved-schema replay](gap-investigation.md#exact-emitted-side-accounting)
classifies **1,263 of 1,314 Swagger findings** as matching-name schema inequalities.
Of these, **796 occur in the 292 schema-only Swagger-only projects**, with
**0 TypeSpec findings**; the [complete member inventory](staging-comparison/one-sided-projects.md)
and [replay details](staging-comparison/schema-investigation.json) retain each case.
A real example is `AgriService_Update` in AgriculturePlatform.Management:
**4 / 0** findings concern `userAssignedIdentities`, `name`, `size` and `tags`;
the saved replay records a description-only difference for `size` and
`x-ms-mutability` for `tags`, despite those names being present in PUT.
These schema-comparison findings are overvalidation under the documented
presence-only policy. This does not certify every project's API correctness:
flattened-name collisions and exact source-to-emission identity remain unassessed.

**Swagger empty-body bug; TypeSpec implements the documented check.**
The [original function][swagger-function] tests the number of body parameters,
not the number of collected properties. An existing empty PATCH object passes
when PUT has a body: **0 / 1** in the
[executed control](semantic-evidence.md#empty-patch-model-versus-absent-patch-body).
The [NetApp Snapshot source and saved TypeSpec warning](corpus-examples.md#effective-empty-patch-netapp-snapshot)
show the same empty-model shape; the retained schema replay independently
records one existing-empty PATCH body in NetApp.
The **49 / 2** total NetApp findings concern several checks, not 47 missing
TypeSpec defects. Keep the TypeSpec empty-body check.

| Other differing project or group                                                                                                     | Swagger / TypeSpec findings                                                                          | Evidence-backed cause and disposition                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [EdgeActions](gap-investigation.md#edgeactions-4-swagger--0-native)                                                                  | 4 / 0                                                                                                | Three schema-equality overchecks plus one opaque `properties` versus read-only-leaf extraction difference. The wrapper finding does not prove a missing wire property; no TypeSpec fix is established by this case alone.                                                                                                                                           |
| [Quota](gap-investigation.md#quota-2-swagger--0-native)                                                                              | 2 / 0                                                                                                | One schema-equality overcheck and one bodyless PATCH with an explicit TypeSpec suppression. Retaining an authored suppression explains silence; it is not a missing TypeSpec body check.                                                                                                                                                                            |
| [DevCenter](gap-investigation.md#devcenter-13-swagger--90-native)                                                                    | 13 / 90                                                                                              | All Swagger findings are schema inequalities. A minimal executed control proves a TypeSpec inherited-property traversal false positive; fix the recursion gate. The source supports this mechanism, but not a blanket classification of all 90 warnings.                                                                                                            |
| [CDN](gap-investigation.md#cdn-4-swagger--9-native)                                                                                  | 4 / 9                                                                                                | Four Swagger `tags` schema overchecks; nine TypeSpec warnings concern inherited writable leaves. Pinned source has the demonstrated recursion-gate shape. Add real-case regressions with the traversal fix; this service inference is not a fresh TypeSpec replay.                                                                                                  |
| [BillingTrust](gap-investigation.md#billingtrust-0-swagger--1-native-the-only-native-only-project)                                   | 0 / 1                                                                                                | The emitted helper finds `kind` in both bodies, while TypeSpec excludes the PUT source property as read-only. Source comments explain its continued wire presence. This is a credible TypeSpec false-positive case, not an evidenced Swagger bug: request-shape regression and a targeted visibility/discriminator correction are required before accepting parity. |
| [Managed Network Fabric](corpus-examples.md#historical-property-names-managed-network-fabric)                                        | 93 / 13                                                                                              | All 93 Swagger findings are schema inequalities. The TypeSpec `primaryIpv6Prefix` warning has the historical-rename pattern reproduced by executed controls. Accept this known limitation temporarily under [#5875](https://github.com/Azure/typespec-azure/issues/5875); validity of all 13 warnings remains unassessed.                                           |
| [Remaining absent-name/body findings and Swagger-higher outliers](gap-investigation.md#swagger-higher-outliers-and-remaining-limits) | 49 absent-name and 2 absent-PATCH Swagger findings overall; corresponding TypeSpec counts unassessed | EdgeActions explains one absent-name record; Quota explains one body record by suppression. Do not label the remaining absent-name records Swagger bugs or TypeSpec omissions without aligned request-shape evidence. Complete correspondence remains an unresolved acceptance gate.                                                                                |

The [missing-PUT control](semantic-evidence.md#missing-put-body) exposes an
additional **1 / 0** semantic gap: a nonempty PATCH with no PUT body cannot
satisfy documented presence, but TypeSpec silently skips it. This requires a
TypeSpec fix even though the corpus replay records **0** Swagger missing-PUT
findings. Lack of a corpus occurrence does not excuse a demonstrated rule defect.
The [historical controls](semantic-evidence.md#historical-renamed-and-type-shape-properties)
likewise establish TypeSpec false positives independently of any unproven
per-project diagnostic pairing. Their expected historical shapes follow from
`@renamedFrom` and `@typeChangedFrom`; no historical Swagger emission was
captured for those controls.
The migration owner approved accepting these historical-shape false positives
temporarily while [#5875](https://github.com/Azure/typespec-azure/issues/5875)
defines shared version-aware evaluation, reporting and suppression.
That issue demonstrates a missing historical violation; these controls
demonstrate extra historical violations from the same source-versus-versioned-shape
problem. It does not yet prescribe the rename/type-shape implementation.
No rule-local historical-shape fix is required for this PR under that deferral.
Keep all findings and counts unchanged; this does not accept inherited-property
false positives or establish full functional equivalence.

The TypeSpec corpus comprises 212 missing-leaf findings, one empty PATCH body
and one absent PATCH body; it must not be relabeled as 214 confirmed defects.
Spectral's collapse of 27 identical operation-target messages and TypeSpec's
shared-source deduplication explain reporting multiplicity, not functional parity.
**The schema-equality gap is justified by an original Swagger bug; the remaining
demonstrated TypeSpec defects still block full documented-policy equivalence.
The approved historical-shape deferral does not remove that limitation.**

## NOTES

- Assessed candidate: `7baca4db3d7824c24c30961c50c3f47a6df8d958`
  from [Azure/typespec-azure#5481](https://github.com/Azure/typespec-azure/pull/5481).
  This report refresh changes the policy interpretation and dispositions only,
  not source code, fixtures or observations. No linter execution was repeated.
- Acceptance policy is the original documentation's property presence plus at
  least one PATCH property, not bug-for-bug equivalence to the implementation.
  The linked appendices predate this policy decision: their observations,
  execution labels and limitations remain evidence, while this note supersedes
  their open-policy/no-authorized-fix dispositions. Historical coverage-report
  reconciliation is not applicable to this pinned baseline comparison.
- Required production corrections belong in
  [`packages/typespec-azure-resource-manager/src/rules/arm-resource-patch-body.ts`][typespec-body]:
  diagnose nonempty PATCH with a bodyless paired PUT; make
  `hasDirectPayloadProperties` consistent with inherited writable traversal;
  and resolve the BillingTrust request-visible discriminator case
  without indiscriminately including read-only properties.
  Add focused violating/compliant regressions in
  [`test/rules/patch-operations.test.ts`][typespec-tests]: absent PUT body versus
  a valid paired body; inherited present versus genuinely absent leaves;
  and wire-present discriminator versus a genuinely absent discriminator.
  These fixes are identified, **not implemented or validated by this update**.
  Relevant changes require fresh candidate validation; saved counts cannot
  certify future fixes. Version alignment and residual diagnostic attribution
  are comparison work, not permission to change rule behavior to equalize totals.
- Historical name/type-shape correction is deferred from this PR to
  [Azure/typespec-azure#5875](https://github.com/Azure/typespec-azure/issues/5875)
  with the migration owner's approval. Its shared detection, diagnostic-target,
  deduplication and suppression contract applies to this limitation, although
  its current reproduction concerns operation availability rather than renames
  or nested types. Preserve the [historical controls](semantic-evidence.md#historical-renamed-and-type-shape-properties)
  and later validate historical correspondence versus genuine versioned
  mismatches when implementing the shared solution. This is a known-defect
  deferral, not evidence that the present rule evaluates historical shapes correctly.
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
- Eight previously recorded injected real-linter controls passed. Applicable portable harness
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

[swagger-function]: https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-properties-correspond-to-put-properties.ts#L15-L70
[typespec-body]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/src/rules/arm-resource-patch-body.ts
[typespec-tests]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/test/rules/patch-operations.test.ts
