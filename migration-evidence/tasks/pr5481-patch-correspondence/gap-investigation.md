# PATCH correspondence: current gap analysis

This appendix interprets the same current assessment as [migration.md](migration.md):
1,314 Swagger linter findings and 94 TypeSpec linter findings, over 487 successful
projects. The broader [record-level assessment](#assessed-diagnostic-records)
excludes **1,132 Swagger overchecks**, leaving **182 / 94 reported records**,
not matched service defects. The remaining Swagger records are **131 schema
differences, 49 absent names and 2 absent bodies**. The first is not generally
checked by TypeSpec; the second is checked but not completely matched; both
body cases are covered, counting Quota's verified suppression.
It separates **coverage**, **cause/evidence** and **recommended action**.
Historical investigations and raw receipts remain linked; their previous
TypeSpec counts are not current conclusions. The
[preceding 214-finding narrative](https://github.com/msyyc/typespec-azure/blob/348c7e318cf1c2ada04ea6cefb082d971183e8dc/migration-evidence/tasks/pr5481-patch-correspondence/gap-investigation.md)
remains available as an immutable audit record.

## Difference groups and decisions

Only differing groups appear below. Counts are raw unless stated otherwise;
rows overlap and must not be added. In particular, a project total is not an
attributed counterpart count for a highlighted semantic cause.

| Difference group                                                                | Swagger / TypeSpec observations                                                                                                 | Coverage status                                                                                   | Recommended action and rationale                                                                                                                                          |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Verified overchecks](#assessed-diagnostic-records)                             | 1,132 Swagger records excluded: 339 documentation, 144 defaults, 612 input-compatible mutability, 37 additional read-only PATCH | These reports do not establish missing names or incompatible request types.                       | Preserve raw observations and request visibility; do not port whole-schema equality. Every contributing helper occurrence must satisfy the exclusion.                     |
| [Remaining same-name schema differences](#remaining-candidates-and-fixes)       | 131 retained Swagger records; 0 general TypeSpec type/constraint-comparison diagnostics                                         | Name-only comparison does not implement compatibility. Not all 131 are established valid defects. | Add a request-aware wire-type/constraint check; validate source/version correspondence and legitimate PATCH differences before predicting new warning totals.             |
| [EdgeActions](#edgeactions-4-swagger--0-typespec)                               | 4 / 0, including 3 schema inequalities and 1 opaque wrapper                                                                     | Source/emitted payload extraction differs; missing wire property unestablished.                   | No justified TypeSpec fix yet. Inspect effective membership/shape before altering traversal or spec models.                                                               |
| [Quota](#quota-2-swagger--0-typespec)                                           | 2 / 0 raw; 1 valid suppressed missing-body finding credited in assessment                                                       | Missing-body behavior is covered, not ignored. The other schema difference remains.               | Preserve suppression and give coverage credit; do not duplicate or bypass the owning check.                                                                               |
| [BillingTrust](#billingtrust-0-swagger--1-typespec)                             | 0 / 1, the sole TypeSpec-only project                                                                                           | Source input-membership warning retained.                                                         | Reject read-only/discriminator relaxation. A different intended input contract needs a spec-owner decision, not inferred schema presence.                                 |
| [NetApp](#netapp-49-swagger--2-typespec)                                        | 49 / 2: 49 schema inequalities; 1 empty-body and 1 source-name warning                                                          | Empty-body policy covered; version-aware names missing/deferred.                                  | Keep the body check; defer shared version handling. Do not treat either project total as matched violations.                                                              |
| [Source/API-version scope](simplification.md#corpus-differences)                | Nine changed projects total 182 / 14; 18 TypeSpec warnings removed, none added                                                  | Historical evaluation intentionally absent; version-specific gaps remain missing.                 | Follow the authorized source-only scope and shared #5875. The nine-project table dispositions each removal; it does not explain all current project findings.             |
| [Residual correspondence/shapes](#swagger-higher-outliers-and-remaining-limits) | 49 absent-name Swagger findings across 18 projects; attributed TypeSpec subset unassessed                                       | Required cross-engine correspondence and unsupported-body coverage remain unassessed.             | Investigate exact operation/version/source/payload identities before choosing a rule, spec, emitter or comparison repair. No production fix is justified by totals alone. |

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

### Assessed diagnostic records

The [assessment receipt](assessment-20261105/results.json) and
[deterministic extractor](assessment-20261105/assess_diagnostics.py) assess
individual **already reported diagnostic records**. The counting unit remains
the original report, not a grouped operation or matched service defect. Each
Swagger record is joined to its saved replay by exact project, Swagger file,
full diagnostic path and full message. Every record must match once; no
property-name-only matching, input omission or further deduplication is allowed.
The receipt references every original record by its project and zero-based
diagnostic-array index, and its exact replay input/operation/reason indices.

The [additional value trace](assessment-20261105/schema-values.json) contains
the actual type, read-only flag, mutability and default for every same-name
candidate of all **1,263 schema-difference records**. Its
[extractor](assessment-20261105/inspect_gap.mjs) checked 341 retained Swagger
inputs against their immutable baseline hashes, the original replay's exact
candidate/key comparisons and the original ruleset/helper/resolver package
content identities. Runtime was **192.7 seconds**, within a 540-second budget.
This is saved-Swagger inspection, not source compilation, Swagger generation
or new TypeSpec observations.

For each schema record, inspect **all** helper occurrences, not just its union
of differing keys. Apply these disjoint categories in order:

| Category                                                        |   Records | Required evidence and disposition                                                                                                                                                                                                                                         |
| --------------------------------------------------------------- | --------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Documentation only                                              |       339 | Every occurrence has a same-name PUT candidate differing only in `description`, `title` or `externalDocs`. Exclude.                                                                                                                                                       |
| Default only, possibly with documentation                       |       144 | Every occurrence has a same-name candidate equal in every other field. A different/omitted default is not an incompatible type. Exclude.                                                                                                                                  |
| Input-compatible mutability, possibly with the preceding fields |       612 | Every occurrence has an otherwise equivalent candidate. Neither leaf is read-only; PUT allows **both create and update**, PATCH allows update. Missing `x-ms-mutability` means the default `read/create/update`. Exclude metadata inequality, not visibility enforcement. |
| Additional read-only PATCH reports                              |        37 | Every contributing PATCH leaf is explicitly `readOnly: true`, so none is PATCH request input. Exclude; keep TypeSpec's input filtering.                                                                                                                                   |
| Remaining schema differences                                    |       131 | Retain. Type/constraint, visibility, extension and nested-shape differences require semantic assessment; not 131 confirmed missed valid warnings.                                                                                                                         |
| **All schema-difference records**                               | **1,263** | **1,132 excluded + 131 retained**, with no collapse of distinct reported records.                                                                                                                                                                                         |

Thus **1,314 - 1,132 = 182 Swagger records remain**:
**131 schema differences + 49 absent names + 2 absent bodies**.
The receipt references every original record by its project/diagnostic index
and exact replay input/operation/reason indices. No record can be excluded
because just one collapsed helper occurrence has a qualifying candidate.
Read-only/create-only PUT differences that fail the mutability guard remain;
constraints, formats, enums, nested schemas and unknown extensions are not
silently treated as documentation.

The earlier description/title-only filter excluded 336 and retained 978. That
**historical narrow result**, including its two mixed-occurrence controls,
remains in `retainedAfterAnnotationAssessment` for audit. The current scorecard
uses `retainedAfterMetadataAssessment`; 978 is no longer the current assessed
Swagger remainder.

All **94 TypeSpec records remain**: 92 missing-property, one empty PATCH and one
absent PATCH. The
[assessed checker](https://github.com/Azure/typespec-azure/blob/51cc68db6897b286b10ad6a23266e9c62a4f422d/packages/typespec-azure-resource-manager/src/rules/arm-resource-patch-body.ts#L56-L103)
compares names and body presence, not `description` or `title`, so there are
**0 annotation-equality warnings** to exclude. This zero does not infer a
source-target counterpart or exclude any potentially unrelated presence
warning at that target. The retained row is a **partial false-positive assessment**, not a new
TypeSpec run, predicted modified-linter output, complete actionable-defect
count or coverage percentage. The **one verified suppressed Quota finding**
is separately credited as covered; it is not fabricated as a 95th raw warning.

The current per-project receipt preserves count directions rather than
subtracting totals: **36 Swagger-higher, 10 TypeSpec-higher and 441 equal-count
projects**. Directional excesses are **105 / 17**; absolute per-project gap is
**122**, not net 88. None is a missed-valid-diagnostic total.
Representative current filtered project totals are:

| Project       | Swagger raw / retained | TypeSpec project total |
| ------------- | ---------------------: | ---------------------: |
| Automation    |                 11 / 6 |                      9 |
| BillingTrust  |                  0 / 0 |                      1 |
| ServiceFabric |                 13 / 0 |                      6 |

These are current filtered **project totals**, not attributed same-check
findings. All 13 ServiceFabric reports are now excluded; that does not make
its six source warnings automatically true positives or new findings.
BillingTrust's independently evidenced membership cause remains below.
All original project totals and the 18-warning source-code delta stay unchanged.

#### Gap example: description/title-only Agriculture identity report

- **Classification/status:** Swagger-linter-only annotation overcheck; excluded from the assessed row, preserved in raw counts.
- **Project/API version:** `specification/agricultureplatform/AgriculturePlatform.Management` / `2024-06-01-preview`.
- **Target:** `AgriService_Update`, `userAssignedIdentities`.

The [PUT resource](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/agricultureplatform/AgriculturePlatform.Management/main.tsp#L28-L41)
spreads `ManagedServiceIdentityProperty`. Its
[authored PATCH](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/agricultureplatform/AgriculturePlatform.Management/main.tsp#L240-L253)
uses the corresponding resource-update model:

```typespec
update is ArmCustomPatchAsync<
  AgriServiceResource,
  Azure.ResourceManager.Foundations.ResourceUpdateModel<
    AgriServiceResource,
    AgriServiceResourceProperties
  >
>;
```

The actual saved Swagger predicate occurrence for this reported record is:

```json
{
  "name": "userAssignedIdentities",
  "classification": "same-name-different-schema",
  "sameNamedPutCandidates": 1,
  "differingSchemaKeys": [["description", "title"]]
}
```

| Engine          | Observed result                                                                                                   |
| --------------- | ----------------------------------------------------------------------------------------------------------------- |
| Swagger linter  | 1 missing-property report for this leaf; the PUT candidate has the same name and all non-annotation fields equal. |
| TypeSpec linter | 0 configured project findings; no annotation-equality predicate.                                                  |

**Coverage/cause:** the saved occurrence proves an annotation-only false
missing-property report, not an absent PUT name or incompatible type.
**Recommended action:** exclude this report and retain the TypeSpec policy of
not comparing annotations. Agriculture has **4 raw / 0 retained Swagger**
and 0 TypeSpec findings: three documentation reports and one input-compatible
`tags` mutability report are excluded.

**Mixed-occurrence control from real evidence:** Workbooks API
`2023-06-01`, `Workbooks_Update`, `tags`, has two helper returns collapsed into
one reported record. The first has no annotation-only candidate: its two
candidate differences are `["x-ms-mutability"]` and
`["additionalProperties", "description", "items", "type", "x-ms-mutability"]`.
The second has a candidate differing only in `["description"]`. The record
could not be excluded by the old description-only filter. The new value trace
shows a write-compatible mutability candidate for the first occurrence and
the documentation candidate for the second, so it now qualifies. Workbooks
has **4 raw / 3 retained Swagger / 1 TypeSpec** project findings.
The other mixed record is DataReplication `2026-05-01`, `Vault_Update`, `type`;
one occurrence includes enum/read-only differences, while another has a
description-only candidate. Both exact records and every candidate comparison
remain in the pinned replay referenced by the receipt.

Reproduce the numeric assessment offline from this task directory:

```powershell
python -B -m unittest discover -s .\assessment-20261105 -p test_assess_diagnostics.py -v
python -B .\assessment-20261105\assess_diagnostics.py --check
```

All **14 focused tests** passed, covering multiple candidates, all versus mixed
helper occurrences, default/documentation differences, mutability eligibility,
read-only PATCH input, incompatible kinds and fail-closed missing evidence.
Record-level totals independently agree with the saved Swagger project
classifications. Input hashes and the extractor hash are in the receipt.
The Python assessment reuses immutable observations and the value trace; it
installs nothing and does not compile specs or regenerate Swagger. Regenerating
the value trace separately invokes the pinned Swagger resolver/ruleset over
saved inputs, not TypeSpec compilation.

To recover the additional values, run from the tooling package directory
using the same verified parent/supplement variables described in [replay.md](replay.md):

```powershell
mise exec -- node --import tsx/esm $task\assessment-20261105\inspect_gap.mjs `
  $tooling $verifiedSharedBaseline $recoveredSupplement $newSchemaValues
```

Use a new output file and compare it with the committed value trace; the
extractor refuses to overwrite an existing capture.

### Gap example: default is not a different type

- **Classification/status:** Swagger-linter-only default overcheck; excluded.
- **Project/API version:** AlertProcessingRules / `2021-08-08`.
- **Target:** `AlertProcessingRules_Update`, `enabled`.

The actual [PUT declaration](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/AlertProcessingRules/models.tsp#L249-L253)
and [PATCH declaration](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/AlertProcessingRules/models.tsp#L434-L438)
are, with documentation omitted:

```typespec
// PUT
enabled?: boolean = true;
// PATCH
enabled?: boolean;
```

The saved value trace has PATCH `{ "type": "boolean" }` and PUT
`{ "type": "boolean", "default": true }`; the only differing schema key is
`default`. Swagger reports one missing-property warning; TypeSpec reports no
type warning. There is neither an absent name nor a changed boolean type.
A creation default and PATCH's leave-unchanged behavior need not use identical
default metadata.
The same criterion accounts for **144 default-only records**, allowing
documentation differences but no changed constraints or wire shape.

**Coverage/action:** do not require equal PUT/PATCH defaults. Add genuine
type/constraint checking separately; copying this equality test would add noise.

<a id="gap-example-metadata-only-inequality-in-codesigning"></a>

### Gap example: mutability metadata is not a missing property

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
The additional value trace confirms PATCH mutability is absent (the default
read/create/update) and PUT is explicitly `["read", "create", "update"]`;
both leaves are writable and otherwise equivalent. The reported difference
therefore qualifies for the current exclusion. CodeSigning is **1 raw /
0 retained Swagger**, not a missing TypeSpec warning.
**Action:** do not add whole-schema equality. It would create metadata noise
without finding an absent wire property. The raw schema-only Swagger-only
projects are accounted for in the
[complete current inventory](refresh-20261104/staging-comparison/one-sided-projects.md).

### Gap example: read-only PATCH leaves are not input

- **Classification/status:** Swagger-linter-only request-input overcheck; excluded.
- **Project/target:** ApiManagement, `ApiGateway_Update`, `id`.

The actual [value trace](assessment-20261105/schema-values.json), replay
input 7 / operation 0 / reason 0, records both leaves as
`{ "type": "string", "readOnly": true }`; their differing keys are
`["description", "format"]`. The Swagger helper compares them despite PATCH's
read-only flag. The TypeSpec
[source traversal](https://github.com/Azure/typespec-azure/blob/51cc68db6897b286b10ad6a23266e9c62a4f422d/packages/typespec-azure-resource-manager/src/rules/arm-resource-patch-body.ts#L181-L198)
filters effective request payload properties before comparing their names.

**Coverage/action:** a field clients cannot send is not a missing PATCH input
property. The exclusion requires **every** contributing PATCH occurrence to be
explicitly read-only, not just one same-name candidate. It removes 37 additional
records after the preceding exclusions. Preserve TypeSpec's request filtering;
do not manufacture type warnings to match these Swagger reports.

## Remaining candidates and fixes

The **131 retained schema records are not a measured total of valid missing
TypeSpec diagnostics**. They still include `format`, scalar constraints,
array/dictionary schemas, nullability, read-only/mutability differences that
failed the exclusions, and other extensions. The receipt's
`remainingSchemaKeyGroups` inventories every such group. Key inequality alone
cannot establish incompatible request contracts.

**Confirmed missing behavior:** the executed
[same-name unequal-type control](semantic-evidence.md#same-name-unequal-scalar-type)
produced 1 Swagger predicate finding and 0 TypeSpec helper findings for
`value?: string` versus `value?: int32`; array/dictionary value-type controls
also differ. The current source still checks names only, and the final
registered [same-name-type control](refresh-20261104/controls/injected-controls.json)
has no configured warning. This is a **real compatibility-checking gap**, not
an accepted reason to call the migration complete. The controls prove missing
behavior, not its frequency in the corpus.

**Owning-rule fix:** in
`packages/typespec-azure-resource-manager/src/rules/arm-resource-patch-body.ts`,
`LeafProperty` retains only `jsonName` and `target`; `putPropertyNames` is a
`Set<string>`. Preserve the source property, effective wire type and relevant
property-level constraints, then compare corresponding writable PATCH/PUT
contracts rather than just names. Cover scalar kind, array items, dictionary
values and nullability; allow PATCH optionality. Documentation, defaults and
method-appropriate mutability must not cause type warnings. Keep visibility,
inheritance, encoded-name and source-target deduplication behavior.

Add focused failing controls to `test/rules/patch-operations.test.ts` for an
incompatible scalar, array/dictionary value mismatch and a missing relevant
constraint; compliant controls must accept documentation-only changes and
partial PATCH objects. The exact compatibility direction and constraint policy
need owner review; deep schema equality is not that design. No production
implementation or predicted number of new source warnings is claimed here.

**Version fix:** separately implement shared #5875 evaluation of active
operations, availability, historical names and historical types. A correct
type comparator on the wrong version's model is still incorrect. The
[18-removal analysis](simplification.md#corpus-differences) and
[issue follow-up](https://github.com/Azure/typespec-azure/issues/5875#issuecomment-6652676528)
explain why those removals are not a count of lost valid findings.

**Unresolved 49 name records:** the name check already exists, so do not add
a duplicate check. Establish `(project, API version, route/method, writable
model/leaf)` correspondence to the actual TypeSpec source target; resolve
wrappers, unsupported bodies, visibility and suppression. Only then identify
concrete extraction fixes and count valid unmatched violations. Source-target
deduplication and emitted-operation multiplicity mean even that count is not
automatically the number of new TypeSpec warnings. This is the remaining work
needed for a defensible total, not a license to label all 182 retained records
missed.

## Swagger-only projects

This section preserves **raw observations before the overcheck exclusions**.
Its project totals are not the current 182-record remainder.

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

After the broader exclusion the project is **4 raw / 1 retained Swagger /
0 TypeSpec**: all three `tags` metadata reports are excluded, but the
`properties` wrapper remains unresolved.

**Coverage:** the TypeSpec linter filters source request visibility and can
retain the same opaque wrapper on both sides; Swagger flattens the read-only
PUT members. This cause follows pinned source inspection and saved results,
not a fresh control proving all runtime payloads.
**Action:** do not add a missing-property check or change this spec solely to
match four Swagger warnings. Whether that wrapper represents a real missing
request property remains unestablished; inspect effective payloads first.

## Missing-body correspondence

The two Swagger missing-body records can be attributed without guessing from
project totals:

| Exact operation                              | Swagger missing-body records | TypeSpec assessment                                     | Why / action                                                                                                                               |
| -------------------------------------------- | ---------------------------: | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| ProviderHub `ProviderMonitorSettings_Update` |                            1 | 1 reported warning at `ProviderMonitorSetting.tsp:42:3` | Source PATCH explicitly has `PatchModel = void`; the existing missing-body check reports. Covered.                                         |
| Quota `GroupQuotaSubscriptions_Update`       |                            1 | 1 valid-but-suppressed finding; 0 raw reported          | Source PATCH explicitly has `PatchModel = void` and applicable `arm-resource-patch` suppression. Credit coverage and preserve suppression. |
| **Total**                                    |                        **2** | **2 covered: 1 reported + 1 suppressed**                | **Not a missing-check gap.**                                                                                                               |

The [ProviderHub declaration](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/providerhub/resource-manager/Microsoft.ProviderHub/ProviderHub/ProviderMonitorSetting.tsp#L36-L45)
and the saved raw diagnostic agree on the operation/body. ProviderHub's other
suppression is for `patch-envelope`, not this missing-body warning.
Quota is detailed below. This is source/predicate evidence before suppression,
not a newly observed unsuppressed Quota run or a global survey of suppressions.

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

**Coverage:** the owning TypeSpec missing-body check exists and its predicate
is satisfied. **Credit one valid-but-suppressed finding** in the assessment,
while keeping Quota's raw reported zero. No unsuppressed real-project execution
is claimed.
**Action:** preserve suppression semantics. A second check or bypass would
duplicate existing behavior. The spec owner can review the exception, but
silence caused by this suppression is not an unimplemented TypeSpec check.

## TypeSpec-higher projects

This section uses **raw project counts**. The additional count-direction
changes after the broader overcheck filter are
accounted for [above](#assessed-diagnostic-records), without inferring
same-check correspondence.

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
All **49 raw Swagger findings are same-name schema inequalities**; only **5
remain after the current overcheck exclusions**. The two TypeSpec
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

| Project                | Swagger raw / retained | TypeSpec raw | Cause established; remaining scope                                                                                                  |
| ---------------------- | ---------------------: | -----------: | ----------------------------------------------------------------------------------------------------------------------------------- |
| Managed Network Fabric |                93 / 21 |           12 | All raw Swagger reports are schema inequalities; the 21 retained records are not automatically counterparts of the source warnings. |
| AppService             |                 53 / 6 |            1 | Most raw reports are excluded overchecks; the six remaining schema records still need semantic/source matching.                     |
| NetApp                 |                 49 / 5 |            2 | Five schema records remain; the two source warnings have separate empty-body/history causes, not a three-defect subtraction.        |
| API Management         |                41 / 12 |            2 | Eight schema and four absent-name records remain; exact source correspondence is unassessed.                                        |
| ComputeGallery         |                 36 / 0 |            0 | Every captured Swagger report satisfies an overcheck exclusion, not 36 missing TypeSpec warnings.                                   |
| EventGrid              |                 34 / 0 |            0 | Every captured Swagger report satisfies an overcheck exclusion, not 34 missing TypeSpec warnings.                                   |

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
owning suite. No additional extraction fix for these 49 records, emitter
repair or general cross-engine normalization is established by their counts.
The separately demonstrated compatibility-checking gap and proposed owning-rule
fix are [above](#remaining-candidates-and-fixes). The
1,132-record overcheck exclusion does not resolve them. Further compilation
would need a specific unresolved question and a justified cost/budget.

The intended source-presence checks are implemented for the documented
supported scope. **Full functional equivalence is not established and the
migration is not fully equivalent:** known type/version boundaries and
unassessed shape/correspondence coverage remain. No immediate-code-change
recommendations above should be read as a parity or completeness pass.

[swagger-function]: https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-properties-correspond-to-put-properties.ts#L15-L70
