# PATCH staging/native gap investigation

**Historical TypeSpec counts:** this investigation retains the original
214-finding candidate and unchanged Swagger replay. See
[fresh candidate results](fix-results.md) and the
[current migration assessment](migration.md) for corrected traversal,
112 fresh findings and the superseding BillingTrust disposition.

## What was measured

The completed supplement evaluates all 649 retained Swagger inputs from all
487 frozen ARM projects, with no failed inputs or regeneration. The native
side is the unchanged saved candidate execution: 487 successful projects,
214 findings, 42 affected projects. This follow-up did not rerun native lint.

The independent Python analysis and native-coverage harness agree on every
project row: 1,314 Swagger findings in 335 projects, 214 native findings in 42,
41 overlapping projects, 294 Swagger-only projects and one native-only project.
Swagger excess summed per project is 1,183; native excess is 83. The absolute
sum is 1,266, not the net 1,100. There are 325 Swagger-higher, three native-higher
and 159 equal-count projects; 151 equal-count projects have no findings.

The [complete difference inventory](staging-comparison/differences.md) preserves
every exact raw diagnostic in both engines' separate identity domains. Relative
gaps use `abs(TypeSpec - Swagger) / max(TypeSpec, Swagger, 1)`.

## Exact emitted-side accounting

The focused replay inspected **all 497 retained Swagger inputs for all 336
projects with findings on either side**, including **every one-sided project**.
It checked the actual rulesets/Spectral content identities and verified every
replayed selected-rule diagnostic against the sealed supplement. It used the
unchanged installed traversal helper and Lodash comparison, not a rewritten
approximation. Full details are in
[schema-investigation.json](staging-comparison/schema-investigation.json).

| Original Swagger predicate's reported failure                                 |  Findings |
| ----------------------------------------------------------------------------- | --------: |
| A matching emitted leaf name exists in PUT, but no whole leaf schema is equal |     1,263 |
| No matching emitted leaf name exists in the helper's PUT leaf inventory       |        49 |
| PATCH has no operation-level body parameter                                   |         2 |
| PATCH has a body parameter but PUT has none                                   |         0 |
| **Total actually reported**                                                   | **1,314** |

These are classifications of Swagger observations, not native attribution.
The first category can include description, mutability, defaults, types, enum
metadata, array items and other schema differences. It must not be relabeled
as 1,263 type defects or 1,263 missing native warnings.

The helper returns 1,339 unequal leaf occurrences, but Spectral reports 1,312
leaf diagnostics: **27 repeated identical operation-target messages collapse
inside Spectral**. The two missing-body findings bring the reported total to
1,314. Repeated helper returns are retained under `predicateOccurrences` in the
investigation JSON, and exact replay verifies the final reported records.
This describes the actual engine's aggregation, not a new deduplication policy.
It does not merge unrelated Swagger or native defects.

The Swagger helper traverses `allOf` at a schema root, but decides whether to
recurse into an individual property from that property's own `properties`
member. It does not apply the native payload-visibility policy. The native
helper applies source visibility and its direct-payload-property recursion
gate. Both schema comparison and extraction can therefore differ.

## Swagger-only projects

The [complete one-sided inventory](staging-comparison/one-sided-projects.md)
lists all 295 one-sided projects, with counts and classification columns.
Each Swagger-only project's retained Swagger was actually replayed, not
classified from its project name or a coverage percentage.

Of the **294 Swagger-only projects**, **292 have only matching-name,
unequal-schema findings**. This establishes the original predicate's
emitted-side reason for reporting; the native rule checks JSON leaf names,
not whole leaf schemas. It does not prove that every source declaration has
been semantically paired or that every policy difference is intentional.
The two mixed cases have additional source-backed explanations:

### EdgeActions: 4 Swagger / 0 native

`specification/cdn/resource-manager/Microsoft.Cdn/EdgeActions` has three
matching-name schema inequalities and one `properties` leaf absent from the
Swagger helper's PUT leaf list. The latter is not proof of a missing wire
property.

For `EdgeActions_Update`, the resolved PATCH leaf inventory contains the opaque
`properties` wrapper; PUT's inventory instead contains `provisioningState` and
`attachments`. The
[frozen declarations](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cdn/resource-manager/Microsoft.Cdn/EdgeActions/edgeactionsbasemodels.tsp#L156-L201)
show a PATCH `properties` model with no members, versus a PUT properties model
whose direct members are read-only. Swagger flattens those read-only members;
the native direct-payload gate does not flatten them and can retain the same
opaque wrapper name on both sides. This is a source-inspected
visibility/traversal difference supported by the saved zero native result,
not a fresh native control or a proposed production fix.

The other three Swagger records concern `tags` schemas. The exact candidate
comparisons differ in `x-ms-mutability`, and one also in `description`.

### Quota: 2 Swagger / 0 native

`specification/quota/resource-manager/Microsoft.Quota/Quota` has one
same-name `properties` schema inequality (`allOf`) and one missing PATCH body.
The latter is `GroupQuotaSubscriptions_Update`; both retained PUT and PATCH
have no body parameter.

The
[frozen source](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/quota/resource-manager/Microsoft.Quota/Quota/GroupQuotaSubscriptionId.tsp#L80-L106)
explicitly uses `Request = void`, `PatchModel = void`, and an authored
`arm-resource-patch` suppression on the PATCH operation. The native comparison
retains that suppression; Swagger has no equivalent source-suppression
application. The native missing-body diagnostic targets the operation, so
this is an evidenced suppression-policy difference, not a compile failure or
an unevaluated native rule.

## Native-higher projects

### BillingTrust: 0 Swagger / 1 native; the only native-only project

`specification/billingtrust/resource-manager/Microsoft.BillingTrust/BillingTrust`
reports missing `kind` at `main.tsp:324:3`. The retained Swagger has exactly one
paired operation, `Rules_Update`, at
`/{resourceUri}/providers/Microsoft.BillingTrust/assessments/default/rules/{ruleName}`.
Its PATCH leaf list is `["kind"]`; PUT also contains `kind`, and the actual
whole-schema predicate reports zero.

The
[PUT declaration](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/billingtrust/resource-manager/Microsoft.BillingTrust/BillingTrust/main.tsp#L222-L259)
marks `RuleProperties.kind` read-only, whereas
[PATCH's discriminator property](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/billingtrust/resource-manager/Microsoft.BillingTrust/BillingTrust/main.tsp#L320-L324)
is writable. The native helper filters source payload visibility before
comparing names. The source comments explicitly describe the discriminator's
continued wire presence despite source mutability; the resolved Swagger
observation above confirms that emitted-side presence. This is a concrete
source-visibility/discriminator difference, not a missing staging evaluation.

An authored suppression exists on the
[PATCH operation](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/billingtrust/resource-manager/Microsoft.BillingTrust/BillingTrust/main.tsp#L698-L709),
but the saved warning targets the separate property declaration. Retaining
authored suppressions does not mean an operation suppression covers a referenced
model property. This follow-up did not change suppression placement or native
behavior.

### DevCenter: 13 Swagger / 90 native

All 13 Swagger records are matching-name schema inequalities. The 90 native
records are missing JSON-leaf names. They are not 77 proven additional defects.
The [original source investigation](corpus-examples.md#inherited-writable-traversal-devcenter-outlier)
and [executed minimal control](semantic-evidence.md#executed-follow-up-inherited-writable-put-properties-behind-read-only-direct-members)
establish a native traversal false-positive mechanism: a PUT derived model with
only read-only direct members can hide inherited writable leaves, while PATCH
flattens the base. The fresh emitted-side replay supplies the previously missing
Swagger count, but does not classify the validity of all 90 source warnings.

### CDN: 4 Swagger / 9 native

All four Swagger findings concern `tags` whole-schema inequalities on the WAF
policy, profile and endpoint paths. The nine native warnings instead concern
health-probe, origin and response-error-detection leaves.

The
[frozen model](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/models.tsp#L4966-L5007)
has `OriginGroupProperties extends OriginGroupUpdatePropertiesParameters` with
only read-only direct `resourceState` and `provisioningState` members.
Its inherited writable members contain the nine reported names, directly or
through `HealthProbeParameters` and
`ResponseBasedOriginErrorDetectionParameters`. This exhibits the same
direct-member recursion-gate asymmetry as the executed minimal control.
The emitted helper finds no absent leaf name in this project. The observed
four and nine diagnostics therefore describe different groups; a net five
must not be treated as five matched or unmatched operations.

## Swagger-higher outliers and remaining limits

| Project                | Swagger | TypeSpec | Emitted-side classification                                                                               |
| ---------------------- | ------: | -------: | --------------------------------------------------------------------------------------------------------- |
| Managed Network Fabric |      93 |       13 | All 93 matching-name, unequal-schema records; 108 helper returns before identical-record collapse         |
| AppService             |      53 |        1 | See exact per-operation schema-key comparisons in the investigation JSON                                  |
| NetApp                 |      49 |        2 | All 49 matching-name schema inequalities; one separate existing-empty PATCH body in the inspected schemas |
| API Management         |      41 |        2 | 37 matching-name inequalities and four absent-name records                                                |
| ComputeGallery         |      36 |        0 | All matching-name schema inequalities; included in the complete one-sided inventory                       |
| EventGrid              |      34 |        0 | All matching-name schema inequalities; included in the complete one-sided inventory                       |

All 49 absent-name Swagger findings across 18 projects are retained explicitly;
they are not folded into the schema-equality category. Names and JSON paths
alone do not establish which native warning, if any, corresponds to them.
For example, the original
[Automation investigation](corpus-examples.md) describes shared source-target
aggregation, and the Managed Network Fabric source contains
[historical property-name changes](corpus-examples.md#historical-property-names-managed-network-fabric).
Those source effects are distinct from the 93 current emitted-schema records.

The second missing-body Swagger finding is ProviderHub, with 1 Swagger and
1 native observation. The original source example explicitly chooses
`PatchModel = void`. Conversely, the existing-empty NetApp Snapshot PATCH body
passes the original body-parameter-count check but is rejected by native.
Neither example establishes general one-to-one diagnostic correspondence.

The complete raw-count gap is accounted for numerically and the emitted-side
predicate causes are verified. **Exact cross-engine correspondence and a
common-operation normalization remain unassessed.** Native considers source
versions and source suppression/visibility; Swagger uses retained latest
emissions. The controlled same-name schema/type, historical shape and traversal
differences still establish non-equivalence. This report does not declare every
warning valid, every difference intended, or a full policy-parity pass.
