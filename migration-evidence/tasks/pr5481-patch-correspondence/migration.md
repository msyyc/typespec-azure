# PatchPropertiesCorrespondToPutProperties migration

## 1. Conclusion and scope

The TypeSpec rule `@azure-tools/typespec-azure-resource-manager/arm-resource-patch`
migrates Swagger linter rule
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
**Inherited writable-property traversal and nonempty PATCH with absent/void PUT
input are corrected. Full functional equivalence remains unestablished.**
Historical-name/type false positives are accepted temporarily under
[#5875](https://github.com/Azure/typespec-azure/issues/5875), not fixed.
The Swagger linter's whole-schema equality bug overchecks property presence,
and its body-parameter-count bug misses existing empty PATCH objects; the
TypeSpec linter intentionally avoids both bugs. The assessed policy is object-body
property presence and nonempty PATCH input, not general type compatibility.
Source/latest-emitted version scopes remain unaligned, and unsupported shapes
and residual source-to-emission correspondence remain unassessed.

## 2. Actual coverage

Fresh TypeSpec execution completed for **487 ARM projects, with 0 failures**.
The unchanged, separately evaluated staging supplement covers all **649 retained
Swagger inputs, with 0 failed inputs**. Reported diagnostics are individual
findings across this population, not project counts.

| Count                | Swagger linter | TypeSpec linter |
| -------------------- | -------------: | --------------: |
| Reported diagnostics |      **1,314** |         **112** |

The remaining difference includes Swagger schema-equality overchecks, request
visibility, suppressions, source/version differences and unresolved attribution.
No justified common-operation counting unit is available; comparison in that
unit remains **unassessed**. See
[Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the breakdown
and remaining limitations.

## 3. Function-level coverage

| Behavior                                                                           | Result                                                                                                                                                 |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Extra PATCH JSON leaf; compliant subset                                            | Covered by violating/compliant rule tests and injected-package controls.                                                                               |
| Missing or empty PATCH body                                                        | Covered. An existing empty object is rejected despite the Swagger linter's body-parameter-count bug.                                                   |
| Nonempty PATCH with absent/void PUT input                                          | **Fixed:** each effective PATCH leaf reports the existing missing-property diagnostic. Unsupported actual PUT shapes remain skipped.                   |
| Inherited writable leaves behind read-only direct members; inherited-only wrappers | **Fixed:** recursion and leaf collection use the same inherited-property traversal and payload filters. Genuine missing inherited leaves still report. |
| Historical property renames and nested type changes                                | **Known false positives, accepted temporarily** under #5875. No rule-local snapshot solution is implemented.                                           |
| Same leaf name with unequal description/type/schema metadata                       | No whole-schema equality check is required by this presence policy. General type compatibility is outside scope.                                       |
| Encoded JSON names and operation request visibility                                | Retained. BillingTrust's read-only PUT discriminator is not made request-visible merely because it appears in a shared Swagger schema.                 |
| Unsupported/ambiguous top-level bodies                                             | Remain skipped; full migration coverage is unassessed, not compiler-prevented or proven equivalent.                                                    |
| Source targets, authored suppression and reporting multiplicity                    | Existing behavior retained; exact cross-engine diagnostic correspondence is not claimed.                                                               |

[Fix validation](fix-validation.md) maps the corrections to regression tests
and registered-linter controls. The [earlier semantic evidence](semantic-evidence.md)
retains pre-fix observations; it is not validation of the corrected candidate.

## 4. Why diagnostic counts differ

The [fresh complete difference inventory](refresh-20261103/staging-comparison/differences.md)
retains both engines' exact records for every differing project. Counts below
are separate observation groups, not matched defects.

| Differing project or diagnostic group                                                                          | Swagger / TypeSpec findings                                                                          | Cause and disposition                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Same-name schema inequalities](gap-investigation.md#exact-emitted-side-accounting)                            | 1,263 Swagger findings; matching TypeSpec attribution unassessed                                     | The original [whole-schema comparison][swagger-function] can claim a property is absent when its name exists but metadata differs. Do not copy this Swagger bug. Of 297 current Swagger-only projects, 295 have only these schema inequalities, totaling 815 Swagger / 0 TypeSpec findings; see the [fresh one-sided inventory](refresh-20261103/staging-comparison/one-sided-projects.md). |
| [DevCenter and CDN inheritance](fix-results.md#inherited-leaf-corrections)                                     | DevCenter 13 / 0; CDN 4 / 0                                                                          | Their 90 and 9 prior TypeSpec findings are no longer emitted after the inherited traversal fix. The Swagger findings are unchanged schema inequalities. Fresh results replace the earlier source-only inference about the correction.                                                                                                                                                       |
| [Power BI Dedicated and Machine Learning inheritance](fix-results.md#inherited-leaf-corrections)               | Power BI Dedicated 2 / 0; Machine Learning 21 / 3                                                    | Two inherited Power BI leaves and the Machine Learning `identity` wrapper finding disappear. The remaining three Machine Learning leaf warnings are unchanged; their cross-engine identity remains unassessed.                                                                                                                                                                              |
| [BillingTrust request visibility](fix-results.md#billingtrust-request-membership)                              | 0 / 1                                                                                                | PUT's `kind` is source-read-only; PATCH's is request-visible. Shared-schema presence does not establish PUT request membership. **Reject a TypeSpec visibility/discriminator correction for this case; keep the warning for the authored contract.**                                                                                                                                        |
| [Managed Network Fabric historical names](corpus-examples.md#historical-property-names-managed-network-fabric) | 93 / 13                                                                                              | All 93 Swagger findings are schema inequalities. The `primaryIpv6Prefix` warning exhibits the demonstrated historical-name false-positive mechanism. Accept that limitation temporarily under #5875; this does not classify all 13 warnings as false positives.                                                                                                                             |
| [EdgeActions](gap-investigation.md#edgeactions-4-swagger--0-native)                                            | 4 / 0                                                                                                | Three schema inequalities and one opaque-wrapper/read-only extraction difference. The wrapper finding alone does not establish a missing wire property or required TypeSpec fix.                                                                                                                                                                                                            |
| [Quota](gap-investigation.md#quota-2-swagger--0-native)                                                        | 2 / 0                                                                                                | One schema inequality; one missing PATCH body is explicitly suppressed in TypeSpec source. Suppression explains the silence, not a missing body check.                                                                                                                                                                                                                                      |
| [NetApp empty PATCH](corpus-examples.md#effective-empty-patch-netapp-snapshot)                                 | 49 / 2 project totals                                                                                | The 49 Swagger findings are schema inequalities. A separate existing-empty PATCH object passes Swagger's parameter-count check but is correctly rejected by TypeSpec. Project totals are not paired violations.                                                                                                                                                                             |
| [Remaining absent-name/body findings](gap-investigation.md#swagger-higher-outliers-and-remaining-limits)       | 49 absent-name and 2 absent-PATCH Swagger findings overall; corresponding TypeSpec counts unassessed | Complete source-target correspondence is unresolved. Preserve all records; do not classify the residual as Swagger bugs or TypeSpec omissions from names/counts alone.                                                                                                                                                                                                                      |

Across the same frozen specs, the candidate changes **214 to 112 TypeSpec
findings: 102 removed, 0 added**, in four projects. The
[exact multiset delta](refresh-20261103/candidate-delta.json) preserves every
removed record; no distinct messages sharing a location were collapsed.
The absent/void PUT correction is proven by focused and injected controls;
this corpus adds no findings for it. The saved Swagger supplement contains
0 missing-PUT-body findings, which does not negate the controlled policy gap.

The current 112 TypeSpec findings comprise 110 missing-leaf findings, one
empty PATCH body and one absent PATCH body, not 112 confirmed API defects.
The historical-shape controls remain false positives and are explicitly
deferred. These limits prevent a full functional-equivalence claim even
though the two adopted corrections are implemented and validated.

## NOTES

- Candidate [`60a56b11d149b5960783e0c18da675d6cceb902e`](https://github.com/Azure/typespec-azure/commit/60a56b11d149b5960783e0c18da675d6cceb902e)
  is pushed to [PR #5481](https://github.com/Azure/typespec-azure/pull/5481).
  [Fresh execution metadata](refresh-20261103/task.json),
  [all project receipts](refresh-20261103/runs/full-corpus/manifest.json),
  [build/package provenance](refresh-20261103/provenance/artifact-provenance.json)
  and [validation](fix-validation.md) identify the actual final candidate.
- Frozen specs: `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`; core gitlink:
  `780c2c6a944d2f6be276b60f890854f7a18b2955`; tooling:
  `662e7f405fda22e1d9c8c9c1d7664d171f80b60d`.
  The existing public compiler/library closure was built and packed; all
  15 tarballs and installation receipts are retained under the fresh evidence.
  Selected rule JavaScript was verified equal in built, packed and installed bytes.
- Shared baseline identity:
  `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`.
  Staging supplement identity:
  `e0a2c22b857b13fa8ccf318bff1c8a6beaf367e1a1210cbc71cf7161fd86d482`.
  Production still did **not evaluate** this staging-only rule; 1,314 is the
  separate evaluated staging total, not a reinterpretation of that absence.
  [Frozen sources and supplement recovery](evidence-details.md) remain available.
- TypeSpec profile: `source`, `target-only`, authored suppressions retained;
  baseline policy `frozen-reference`, no filter/limit, concurrency 2.
  This is not a projected comparison aligned with latest-emitted Swagger.
  The native stage ran 09:10:04-09:33:47 UTC on 2026-11-03 within its
  10,800-second budget; the complete run, including integrity checks, ran
  08:37:03-09:50:47 UTC. No Swagger was regenerated or staging rule rerun.
- [Fresh summary](refresh-20261103/staging-comparison/summary.json):
  335 Swagger-affected projects, 39 TypeSpec-affected, 38 overlapping,
  297 Swagger-only and 1 TypeSpec-only. Swagger is higher in 328 projects,
  TypeSpec in 1; 158 have equal counts, including 151 with neither reporting.
  Project-wise Swagger excess is 1,203, TypeSpec excess 1, absolute gap 1,204;
  the net 1,202 must not cancel opposite-direction differences.
  Relative gap is `abs(TypeSpec - Swagger) / max(TypeSpec, Swagger, 1)`.
  Independent Python and [native-harness accounting](refresh-20261103/provenance/harness-crosscheck.json)
  agree on all 487 project rows.
- There are 112 distinct source/location/message records but 102 source
  positions. Swagger has 740 distinct project/file/JSON-path identities,
  also 740 dropping the file. These are different identity domains, not
  normalized operation counts.
- Existing Swagger schema-replay evidence is reused, not rerun: the affected
  union remains exactly the same 336 projects whose 497 inputs were replayed.
  [Reanalysis](refresh-20261103/reanalyze-schema.py) verifies the exact project
  set and unchanged Swagger totals before joining fresh native project counts.
- Validation: 59 focused rule tests, 40 sample tests and 14 injected controls
  passed; portable harness 37 passed / 6 unrelated absent-rule fixtures excluded.
  Builds, lint, formatting and Chronus checks passed; independent code review
  found no significant issues. The original 214-finding receipts remain
  historical evidence; they were not overwritten.
- Historical shapes remain deferred under
  [#5875](https://github.com/Azure/typespec-azure/issues/5875#issuecomment-6597627686).
  No discriminator exception, visibility relaxation or bespoke versioning
  machinery was added. [Fresh recovery instructions](fix-results.md#recovery)
  distinguish saved-data replay from a new native execution and fully locked
  transitive regeneration, which is not claimed.

[swagger-function]: https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-properties-correspond-to-put-properties.ts#L15-L70
