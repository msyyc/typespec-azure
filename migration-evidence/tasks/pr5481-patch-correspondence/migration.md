# PatchPropertiesCorrespondToPutProperties migration

## 1. Conclusion and scope

The TypeSpec rule `@azure-tools/typespec-azure-resource-manager/arm-resource-patch`
migrates Swagger linter rule
[`PatchPropertiesCorrespondToPutProperties`](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md).
**Source-model property presence is checked; full functional equivalence remains
unestablished.** Individual API-version shapes are not evaluated.
Version-specific availability, renames and type changes can cause missed
violations or false positives; shared version-aware evaluation is deferred to
[#5875](https://github.com/Azure/typespec-azure/issues/5875).
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
| Reported diagnostics |      **1,314** |          **94** |

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
| API-version availability, historical names and nested type changes                 | **Not evaluated.** Both missed version-specific mismatches and false positives are possible; deferred to #5875.                                        |
| Same leaf name with unequal description/type/schema metadata                       | No whole-schema equality check is required by this presence policy. General type compatibility is outside scope.                                       |
| Encoded JSON names and operation request visibility                                | Retained. BillingTrust's read-only PUT discriminator is not made request-visible merely because it appears in a shared Swagger schema.                 |
| Unsupported/ambiguous top-level bodies                                             | Remain skipped; full migration coverage is unassessed, not compiler-prevented or proven equivalent.                                                    |
| Source targets, authored suppression and reporting multiplicity                    | Existing behavior retained; exact cross-engine diagnostic correspondence is not claimed.                                                               |

[Simplification validation](simplification.md) maps source-only semantics,
corpus differences and retained checks to regression and registered-linter controls.
The [earlier fix validation](fix-validation.md) and
[semantic evidence](semantic-evidence.md) retain historical observations.

## 4. Why diagnostic counts differ

The [fresh complete difference inventory](refresh-20261104/staging-comparison/differences.md)
retains both engines' exact records for every differing project. Counts below
are separate observation groups, not matched defects.

| Differing project or diagnostic group                                                                    | Swagger / TypeSpec findings                                                                          | Cause and disposition                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Same-name schema inequalities](gap-investigation.md#exact-emitted-side-accounting)                      | 1,263 Swagger findings; matching TypeSpec attribution unassessed                                     | The original [whole-schema comparison][swagger-function] can claim a property is absent when its name exists but metadata differs. Do not copy this Swagger bug. Of 303 current Swagger-only projects, 301 have only these schema inequalities, totaling 876 Swagger / 0 TypeSpec findings; see the [fresh one-sided inventory](refresh-20261104/staging-comparison/one-sided-projects.md).                                    |
| [DevCenter and CDN inheritance](fix-results.md#inherited-leaf-corrections)                               | DevCenter 13 / 0; CDN 4 / 0                                                                          | Their 90 and 9 prior TypeSpec findings are no longer emitted after the inherited traversal fix. The Swagger findings are unchanged schema inequalities. Fresh results replace the earlier source-only inference about the correction.                                                                                                                                                                                          |
| [Power BI Dedicated and Machine Learning inheritance](fix-results.md#inherited-leaf-corrections)         | Power BI Dedicated 2 / 0; Machine Learning 21 / 3                                                    | Two inherited Power BI leaves and the Machine Learning `identity` wrapper finding disappear. The remaining three Machine Learning leaf warnings are unchanged; their cross-engine identity remains unassessed.                                                                                                                                                                                                                 |
| [BillingTrust request visibility](fix-results.md#billingtrust-request-membership)                        | 0 / 1                                                                                                | PUT's `kind` is source-read-only; PATCH's is request-visible. Shared-schema presence does not establish PUT request membership. **Reject a TypeSpec visibility/discriminator correction for this case; keep the warning for the authored contract.**                                                                                                                                                                           |
| [Source-only evaluation changes](simplification.md#corpus-differences)                                   | Nine changed projects; 182 Swagger / 14 current TypeSpec findings across those projects              | 18 former TypeSpec findings disappear, none are added. This includes the Managed Network Fabric `primaryIpv6Prefix` warning (project now 93 / 12). Removing availability filtering avoids some historical-shape warnings and also stops checking version-specific membership gaps. Each changed project/target and its disposition is retained; disappearance is not proof of equivalence or that every old warning was false. |
| [EdgeActions](gap-investigation.md#edgeactions-4-swagger--0-native)                                      | 4 / 0                                                                                                | Three schema inequalities and one opaque-wrapper/read-only extraction difference. The wrapper finding alone does not establish a missing wire property or required TypeSpec fix.                                                                                                                                                                                                                                               |
| [Quota](gap-investigation.md#quota-2-swagger--0-native)                                                  | 2 / 0                                                                                                | One schema inequality; one missing PATCH body is explicitly suppressed in TypeSpec source. Suppression explains the silence, not a missing body check.                                                                                                                                                                                                                                                                         |
| [NetApp empty PATCH](corpus-examples.md#effective-empty-patch-netapp-snapshot)                           | 49 / 2 project totals                                                                                | The 49 Swagger findings are schema inequalities. A separate existing-empty PATCH object passes Swagger's parameter-count check but is correctly rejected by TypeSpec. Project totals are not paired violations.                                                                                                                                                                                                                |
| [Remaining absent-name/body findings](gap-investigation.md#swagger-higher-outliers-and-remaining-limits) | 49 absent-name and 2 absent-PATCH Swagger findings overall; corresponding TypeSpec counts unassessed | Complete source-target correspondence is unresolved. Preserve all records; do not classify the residual as Swagger bugs or TypeSpec omissions from names/counts alone.                                                                                                                                                                                                                                                         |

The [exact current delta](refresh-20261104/candidate-delta.json) is
**112 to 94 findings: 18 removed, 0 added**, in nine projects. Its effects are
accepted under the explicitly authorized source-only scope, not classified as
18 API defects repaired. The prior [214 to 112 correction](refresh-20261103/candidate-delta.json)
remains separate historical evidence. Distinct messages sharing a location
are not collapsed.

The current 94 TypeSpec findings comprise 92 missing-leaf findings, one
empty PATCH body and one absent PATCH body, not 94 confirmed API defects.
The absent/void PUT and inherited traversal corrections remain covered;
version-specific guarantees are not preserved. These boundaries prevent a
full functional-equivalence claim.

## NOTES

- Production candidate [`51cc68db6897b286b10ad6a23266e9c62a4f422d`](https://github.com/Azure/typespec-azure/commit/51cc68db6897b286b10ad6a23266e9c62a4f422d)
  underlies final head [`4f62f17ff8a4d3afcbc7fd548112c5fb42402464`](https://github.com/Azure/typespec-azure/commit/4f62f17ff8a4d3afcbc7fd548112c5fb42402464)
  of [PR #5481](https://github.com/Azure/typespec-azure/pull/5481).
  The follow-up adds two corpus-derived tests only; production source is unchanged.
  [Fresh execution metadata](refresh-20261104/task.json),
  [all project receipts](refresh-20261104/runs/full-corpus/manifest.json),
  [build/package provenance](refresh-20261104/provenance/artifact-provenance.json)
  and [validation](simplification.md) identify the tested candidate.
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
  The native stage ran 07:09:08-07:33:09 UTC on 2026-11-04 within its
  10,800-second budget; the complete run, including integrity checks, ran
  06:28:34-07:51:08 UTC, after the separate injected controls. No Swagger was
  regenerated or staging rule rerun. The coordinator held the shared machine
  corpus lock through injection, controls, the runner and all its children.
- [Fresh summary](refresh-20261104/staging-comparison/summary.json):
  335 Swagger-affected projects, 33 TypeSpec-affected, 32 overlapping,
  303 Swagger-only and 1 TypeSpec-only. Swagger is higher in 330 projects,
  TypeSpec in 1; 156 have equal counts, including 151 with neither reporting.
  Project-wise Swagger excess is 1,221, TypeSpec excess 1, absolute gap 1,222;
  the net 1,220 must not cancel opposite-direction differences.
  Relative gap is `abs(TypeSpec - Swagger) / max(TypeSpec, Swagger, 1)`.
  Independent Python and [native-harness accounting](refresh-20261104/provenance/harness-crosscheck.json)
  agree on all 487 project rows.
- There are 94 distinct source/location/message records but 84 source
  positions. Swagger has 740 distinct project/file/JSON-path identities,
  also 740 dropping the file. These are different identity domains, not
  normalized operation counts.
- Existing Swagger schema-replay evidence is reused, not rerun: the affected
  union remains exactly the same 336 projects whose 497 inputs were replayed.
  [Reanalysis](refresh-20261104/reanalyze-schema.py) verifies the exact project
  set and unchanged Swagger totals before joining fresh native project counts.
- Validation: 61 focused rule tests (including two corpus-extracted tests),
  40 sample tests and 14 injected controls
  passed; portable harness 37 passed / 6 unrelated absent-rule fixtures excluded.
  Builds, lint, formatting and Chronus checks passed; independent code review
  found no significant issues. The original 214- and preceding 112-finding receipts remain
  historical evidence; they were not overwritten.
- Version-specific evaluation remains deferred under
  [#5875](https://github.com/Azure/typespec-azure/issues/5875#issuecomment-6597627686).
  No discriminator exception or visibility relaxation was added. Rule-local
  versioning machinery was removed. [Fresh recovery instructions](simplification.md#recovery)
  distinguish saved-data replay from a new native execution and fully locked
  transitive regeneration, which is not claimed.

[swagger-function]: https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-properties-correspond-to-put-properties.ts#L15-L70
