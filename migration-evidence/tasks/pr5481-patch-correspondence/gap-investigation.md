# PATCH correspondence: current gap analysis

This appendix interprets the same current assessment as [migration.md](migration.md):
1,314 Swagger linter findings and 94 TypeSpec linter findings, over 487 successful
projects. It separates **coverage**, **cause/evidence** and **recommended action**.
Historical investigations and raw receipts remain linked; their previous
TypeSpec counts are not current conclusions. The
[preceding 214-finding narrative](https://github.com/msyyc/typespec-azure/blob/348c7e318cf1c2ada04ea6cefb082d971183e8dc/migration-evidence/tasks/pr5481-patch-correspondence/gap-investigation.md)
remains available as an immutable audit record.

## Difference groups and decisions

Only differing groups appear below. Counts are raw unless stated otherwise;
rows overlap and must not be added. In particular, a project total is not an
attributed counterpart count for a highlighted semantic cause.

| Difference group                                                                | Swagger / TypeSpec observations                                                                                         | Coverage status                                                                          | Recommended action and rationale                                                                                                                                                                                                |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Same-name schema inequalities](#exact-emitted-side-accounting)                 | 1,263 Swagger findings; attributed TypeSpec subset unassessed. The 301 schema-only Swagger-only projects total 876 / 0. | Presence checks exist; metadata equality and general type compatibility are not checked. | Do not port metadata overchecks or equate every unequal schema with a missing property. Type incompatibility is a separate unchecked behavior; broad type validation needs its own policy/design, not a count-equalizing patch. |
| [EdgeActions](#edgeactions-4-swagger--0-typespec)                               | 4 / 0, including 3 schema inequalities and 1 opaque wrapper                                                             | Source/emitted payload extraction differs; missing wire property unestablished.          | No justified TypeSpec fix yet. Inspect effective membership/shape before altering traversal or spec models.                                                                                                                     |
| [Quota](#quota-2-swagger--0-typespec)                                           | 2 / 0, including 1 schema inequality and 1 suppressed missing body                                                      | Missing-body check covered but authored suppression prevents a configured warning.       | Preserve source suppression; do not duplicate or bypass the owning check.                                                                                                                                                       |
| [BillingTrust](#billingtrust-0-swagger--1-typespec)                             | 0 / 1, the sole TypeSpec-only project                                                                                   | Source input-membership warning retained.                                                | Reject read-only/discriminator relaxation. A different intended input contract needs a spec-owner decision, not inferred schema presence.                                                                                       |
| [NetApp](#netapp-49-swagger--2-typespec)                                        | 49 / 2: 49 schema inequalities; 1 empty-body and 1 source-name warning                                                  | Empty-body policy covered; version-aware names missing/deferred.                         | Keep the body check; defer shared version handling. Do not treat either project total as matched violations.                                                                                                                    |
| [Source/API-version scope](simplification.md#corpus-differences)                | Nine changed projects total 182 / 14; 18 TypeSpec warnings removed, none added                                          | Historical evaluation intentionally absent; version-specific gaps remain missing.        | Follow the authorized source-only scope and shared #5875. The nine-project table dispositions each removal; it does not explain all current project findings.                                                                   |
| [Residual correspondence/shapes](#swagger-higher-outliers-and-remaining-limits) | 49 absent-name Swagger findings across 18 projects; attributed TypeSpec subset unassessed                               | Required cross-engine correspondence and unsupported-body coverage remain unassessed.    | Investigate exact operation/version/source/payload identities before choosing a rule, spec, emitter or comparison repair. No production fix is justified by totals alone.                                                       |

## Exact emitted-side accounting

The unchanged replay inspected **all 497 retained Swagger inputs for the same
336 projects with findings on either side**. It used the actual installed
traversal helper and Lodash comparison, and verified every reported record
against the sealed staging supplement. The
[saved replay](staging-comparison/schema-investigation.json) is not a fresh
TypeSpec execution or an inferred match by property name. The
[current join](refresh-20261104/staging-comparison/schema-current-projects.json)
updates only TypeSpec project counts and one-sided flags.

| Swagger predicate's actual reported result                                  |  Findings |
| --------------------------------------------------------------------------- | --------: |
| Matching emitted leaf name exists in PUT, but no whole leaf schema is equal |     1,263 |
| No matching name exists in the helper's PUT leaf inventory                  |        49 |
| PATCH has no operation-level body parameter                                 |         2 |
| PATCH has a body parameter but PUT has none                                 |         0 |
| **Total**                                                                   | **1,314** |

The [pinned Swagger function][swagger-function] uses
`_.differenceWith(patchBodyProperties[0], putBodyProperties[0], _.isEqual)`.
Consequently, a description or mutability difference can be reported as a
missing property even when its name exists: that is an overchecking bug for
the documented presence policy. However, the 1,263 category also includes
type/constraint differences. **It is not a count of 1,263 proven harmless
false positives or missing TypeSpec warnings.**

The helper returns 1,339 unequal leaves; Spectral reports 1,312 leaf findings
after collapsing 27 repeated identical operation-target messages. The two
body findings yield 1,314. The saved `predicateOccurrences` preserve those
helper returns. This is measured engine aggregation, not permission to
deduplicate distinct source findings or invent common operation identities.

### Gap example: metadata-only inequality in CodeSigning

- **Classification/status:** Swagger-linter-only; whole-schema comparison not ported.
- **Project/API version:** `specification/codesigning/resource-manager/Microsoft.CodeSigning/CodeSigning` / `2026-05-15-preview`.
- **Target:** `CodeSigningAccounts_Update`, `tags`, under the account resource path.

The [authored PATCH model](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/codesigning/resource-manager/Microsoft.CodeSigning/CodeSigning/models.tsp#L148-L156)
contains:

```typespec
model CodeSigningAccountPatch {
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-no-record" "existing API"
  @doc("Resource tags.")
  tags?: Record<string>;
  // Other member omitted.
}
```

The retained Swagger replay records a same-named PUT candidate, with only
`x-ms-mutability` differing; this is a trace excerpt, not newly emitted JSON:

```json
{
  "name": "tags",
  "classification": "same-name-different-schema",
  "sameNamedPutCandidates": 1,
  "differingSchemaKeys": [["x-ms-mutability"]]
}
```

| Engine          | Observed project result                                          |
| --------------- | ---------------------------------------------------------------- |
| Swagger linter  | 1 finding: `tags` schemas are unequal despite the matching name. |
| TypeSpec linter | 0 configured findings in the current receipt.                    |

**Coverage:** name presence is the current policy; metadata equality is not.
**Action:** do not add whole-schema equality. It would create metadata noise
without finding an absent wire property. The 301 schema-only Swagger-only
projects are accounted for in the
[complete current inventory](refresh-20261104/staging-comparison/one-sided-projects.md).

**Separate type-compatibility gap:** the executed
[same-name unequal-type control](semantic-evidence.md#same-name-unequal-scalar-type)
produced 1 Swagger predicate finding and 0 TypeSpec helper findings for
`value?: string` versus `value?: int32`; array/dictionary value-type controls
also differ. The current source still checks names only, and the final
registered [same-name-type control](refresh-20261104/controls/injected-controls.json)
retains this policy with no configured warning. This is missing original predicate
behavior, not proved harmless metadata noise. No corpus prevalence or exact
counterpart subset is established.
**Action:** keep the authorized presence policy for this PR; do not substitute
deep equality for a separately designed compatibility policy. A broader
type-compatibility requirement needs explicit policy ownership and appropriate
violating/compliant controls. Full Swagger-predicate equivalence is not claimed.

## Swagger-only projects

There are now **303 Swagger-only projects**; **301** contain only the
same-name/schema-inequality category, totaling **876 Swagger / 0 TypeSpec**
findings. The remaining two are EdgeActions and Quota. Every one's emitted-side
predicate was replayed; this is not an exact semantic pairing to source targets.
The [current project inventory](refresh-20261104/staging-comparison/projects.json)
and [complete grouped targets](refresh-20261104/staging-comparison/differences.md)
retain each project's counts and all exact records.

<a id="edgeactions-4-swagger--0-native"></a>

### EdgeActions: 4 Swagger / 0 TypeSpec

- **Classification/status:** Swagger-linter-only; extraction difference, not a confirmed missing TypeSpec check.
- **Project/API version:** `specification/cdn/resource-manager/Microsoft.Cdn/EdgeActions` / `2026-10-01`.
- **Target:** `EdgeActions_Update`, PATCH `properties`.

The [frozen source](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cdn/resource-manager/Microsoft.Cdn/EdgeActions/edgeactionsbasemodels.tsp#L156-L201)
declares:

```typespec
model EdgeActionProperties {
  @visibility(Lifecycle.Read)
  provisioningState?: ProvisioningState;

  @visibility(Lifecycle.Read)
  attachments: EdgeActionAttachment[];
}
model EdgeActionPropertiesUpdate {}
```

The replay finds the opaque PATCH name `properties`; PUT instead has
`provisioningState` and `attachments` among its leaves. The same operation also
reports a `tags` inequality. The other two project findings are `tags`
inequalities on `EdgeActionExecutionFilters_Update` and
`EdgeActionVersions_Update`: **3 schema inequalities
plus 1 wrapper**, not four absent wire properties.

**Coverage:** the TypeSpec linter filters source request visibility and can
retain the same opaque wrapper on both sides; Swagger flattens the read-only
PUT members. This cause follows pinned source inspection and saved results,
not a fresh control proving all runtime payloads.
**Action:** do not add a missing-property check or change this spec solely to
match four Swagger warnings. Whether that wrapper represents a real missing
request property remains unestablished; inspect effective payloads first.

<a id="quota-2-swagger--0-native"></a>

### Quota: 2 Swagger / 0 TypeSpec

- **Classification/status:** Swagger-linter-only; authored suppression explains missing configured warning.
- **Project/API version:** `specification/quota/resource-manager/Microsoft.Quota/Quota` / `2026-09-01-preview`.
- **Target:** `GroupQuotaSubscriptions_Update`.

The [frozen source](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/quota/resource-manager/Microsoft.Quota/Quota/GroupQuotaSubscriptionId.tsp#L80-L106)
selects PUT `Request = void`, and PATCH:

```typespec
#suppress "@azure-tools/typespec-azure-resource-manager/arm-resource-patch" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
@patch(#{ implicitOptionality: false })
update is GroupQuotaSubscriptionIdsOps.CustomPatchAsync<
  GroupQuotaSubscriptionId,
  PatchModel = void,
  // Response argument omitted.
>;
```

The retained replay has `patchBodyParameters: 0`, `putBodyParameters: 0`,
and one missing-PATCH-body finding for this operation. The other project
finding is a same-name `properties` schema inequality (`allOf`).

**Coverage:** the owning TypeSpec missing-body check exists; the authored
operation suppression explains its configured silence. No unsuppressed
real-project execution is claimed here.
**Action:** preserve suppression semantics. A second check or bypass would
duplicate existing behavior. Reviewing this compatibility exception belongs
to the spec owner and is not required by this count difference.

## TypeSpec-higher projects

### BillingTrust: 0 Swagger / 1 TypeSpec

- **Classification/status:** TypeSpec-linter-only; retained source input-membership policy.
- **Project/API version:** `specification/billingtrust/resource-manager/Microsoft.BillingTrust/BillingTrust` / retained Swagger `2026-03-17-preview`, unprojected TypeSpec.
- **Target:** `Rules_Update`, `main.tsp:324:3`, `kind`.

The actual [PUT](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/billingtrust/resource-manager/Microsoft.BillingTrust/BillingTrust/main.tsp#L222-L259)
and [PATCH](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/billingtrust/resource-manager/Microsoft.BillingTrust/BillingTrust/main.tsp#L320-L324)
declarations differ:

```typespec
// PUT: RuleProperties
@visibility(Lifecycle.Read)
kind: RuleKind;
// PATCH: RulePatchProperties
kind: RuleKind;
```

The retained shared Swagger PUT schema includes:

```json
{
  "kind": {
    "$ref": "#/definitions/RuleKind",
    "description": "The kind of rule. Acts as a discriminator for kind-specific properties.",
    "readOnly": true
  }
}
```

The Swagger linter finds `kind` on both sides and reports 0. The TypeSpec
linter excludes read-only PUT input and reports 1 missing-property warning.
Its final registered discriminator control confirms that source policy.

**Coverage:** shared-schema presence does not prove PUT request membership.
**Action:** **reject a TypeSpec visibility/discriminator relaxation** for this
case. If request-visible `kind` is intended, the spec owner must make that
contract consistent or justify an applicable suppression; no spec, service or
emitter defect is established merely from this warning. The existing suppression
on the PATCH operation does not cover the separately targeted model property.
This keeps the [superseding disposition](fix-results.md#billingtrust-request-membership),
not the earlier proposed mandatory source fix.

## NetApp: 49 Swagger / 2 TypeSpec

The entire project difference must not be attributed to the empty-body example.
All **49 Swagger findings are same-name schema inequalities**. The two TypeSpec
findings are independently identified in the current receipt:

| Source target                                 | Swagger result for that semantic cause                   | TypeSpec finding           | Coverage/action                                                              |
| --------------------------------------------- | -------------------------------------------------------- | -------------------------- | ---------------------------------------------------------------------------- |
| `Snapshot.tsp:116:3`, `Snapshots_Update`      | 0 for the existing empty PATCH object                    | 1 `emptyPatchBody`         | Covered policy; keep the check, do not port the Swagger false negative.      |
| `Volume.tsp:1361:3`, `usageThreshold20250901` | Corresponding historical source-warning count unassessed | 1 missing-property finding | Source names/history differ; defer version-aware reconstruction under #5875. |

### Gap example: existing empty PATCH is not an absent body parameter

- **Classification/status:** TypeSpec-linter-only cause inside a Swagger-higher project; Swagger bug intentionally avoided.
- **Project/API version:** `specification/netapp/resource-manager/Microsoft.NetApp/NetApp` / `2026-06-15-preview`.
- **Target:** `Snapshots_Update`.

The [frozen declaration](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/Snapshot.tsp#L85-L116)
contains:

```typespec
#suppress "@azure-tools/typespec-azure-resource-manager/no-empty-model" "For backward compatibility"
model SnapshotPatch {}
// Inside the resource operations interface:
@patch(#{ implicitOptionality: false })
update is ArmCustomPatchAsync<Snapshot, PatchModel = SnapshotPatch>;
```

The saved Swagger replay for this exact operation records:

```json
{
  "operationId": "Snapshots_Update",
  "patchBodyParameters": 1,
  "putBodyParameters": 1,
  "patchLeafNames": [],
  "swaggerReportedDiagnostics": 0
}
```

**Coverage:** the TypeSpec linter reports one empty-body warning. The Swagger
linter's `.length < 1` checks count body parameters, not their properties, and
therefore miss this existing empty body. The other rule's compatibility
suppression does not suppress `arm-resource-patch`.
**Action:** retain the TypeSpec check. Do not copy the false negative or
automatically change an intentionally compatible service model.

### Gap example: source names are not historical wire names

The pinned PUT property is
[`usageThresholdOld`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/Volume.tsp#L70-L112);
PATCH uses
[`usageThreshold20250901`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/Volume.tsp#L1340-L1381).
Both have `@renamedFrom(..., "usageThreshold")` at the same series of
version boundaries, while later declarations are named `usageThreshold`.
The observed missing-property warning compares current source names, not
reconstructed wire names for those historical versions.

**Coverage:** version-aware historical-name comparison is missing. This
source inspection identifies the mechanism; no new per-version projection or
exact emitted-warning pairing was executed.
**Action:** retain the authorized temporary deferral to #5875 rather than
special-case these aliases. The existing
[source-history examples and changed-target dispositions](simplification.md#corpus-differences)
show both disappearing warnings and lost availability checks; disappearance
is not proof of repaired versioning.

## Swagger-higher outliers and remaining limits

The [complete difference inventory](refresh-20261104/staging-comparison/differences.md)
groups all exact records by differing project/target, with signed, absolute and
relative gaps. It retains all 330 Swagger-higher projects and BillingTrust in
the opposite direction; totals do not cancel. Representative current outliers:

| Project                | Swagger | TypeSpec | Cause established; remaining scope                                                                                |
| ---------------------- | ------: | -------: | ----------------------------------------------------------------------------------------------------------------- |
| Managed Network Fabric |      93 |       12 | All 93 Swagger findings are schema inequalities; exact counterparts for the 12 source warnings remain unassessed. |
| AppService             |      53 |        1 | Exact per-operation schema-key comparisons retained; not 52 proved missing TypeSpec checks.                       |
| NetApp                 |      49 |        2 | Two distinct TypeSpec causes described above; not a 47-operation gap.                                             |
| API Management         |      41 |        2 | 37 schema inequalities and 4 absent-name Swagger records; exact source correspondence unassessed.                 |
| ComputeGallery         |      36 |        0 | All same-name schema inequalities; included in the complete one-sided inventory.                                  |
| EventGrid              |      34 |        0 | All same-name schema inequalities; included in the complete one-sided inventory.                                  |

**Coverage:** all **49 absent-name Swagger findings across 18 projects** are
retained, including the EdgeActions wrapper. The remaining records are not
classified as Swagger bugs by subtraction. Unsupported top-level bodies are
skipped by the TypeSpec object gate; shared source targets, visibility,
suppression and API-version scope also prevent automatic operation matching.
Their exact corresponding TypeSpec counts and equivalent coverage remain
unassessed. Equal-count projects are not a proof of semantic correspondence.

The [historical Automation source-target example](corpus-examples.md#writable-source-metadata-automation)
also shows why distinct leaf messages can share one containing-model target.
Keep those messages separate; neither that example nor the 84 current source
positions establishes how many Swagger operations correspond to them.

**Action:** use saved source/schema/operation evidence to establish the exact
request payload and target identity before recommending an owning-rule fix,
spec correction or comparison repair. A confirmed missing TypeSpec predicate
would need an authorable violating fixture and a compliant control in the
owning suite. No such additional production fix, emitter repair or safe
normalization is established from the remaining counts. Further compilation
would need a specific unresolved question and a justified cost/budget.

The intended source-presence checks are implemented for the documented
supported scope. **Full functional equivalence is not established and the
migration is not fully equivalent:** known type/version boundaries and
unassessed shape/correspondence coverage remain. No immediate-code-change
recommendations above should be read as a parity or completeness pass.

[swagger-function]: https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-properties-correspond-to-put-properties.ts#L15-L70
