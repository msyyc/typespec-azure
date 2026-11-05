# PATCH correspondence: assessed differences and decisions

This appendix supports [migration.md](migration.md): **1,314 Swagger / 117
TypeSpec reported diagnostics**, 487 successful ARM projects. Its central
answer is: **the demonstrated type/constraint and inherited-operation gaps
are fixed; none of the 182 retained records now exposes another confirmed
missing non-versioning check in the investigated supported source contexts.**
That scoped result is not full API-version-aware Swagger equivalence or a
count of matched service defects.

## Difference groups and decisions

The first three rows partition the 182 records remaining after 1,132 verified
Swagger overchecks. Project-only rows below them overlap and must not be added.
Source-check witnesses mean distinct configured diagnostic indices verified
against the full run, not cross-engine violation matches.

| Difference group                                       |                      Swagger observations | TypeSpec observations                                                                                                                  | Coverage, cause and recommended action                                                                                                                       |
| ------------------------------------------------------ | ----------------------------------------: | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Same-name schemas](#schema-contexts)                  |                      131 retained records | 42 reporting contexts; 81 compatible contracts; 6 not writable source leaves; 2 mixed-name contexts. 34 distinct configured witnesses. | Compatibility gap fixed. Accept legitimate partial/compatible values; do not require deep schema equality. Mixed names remain explicit, not guessed matches. |
| [Absent emitted names](#name-contexts)                 |                       49 retained records | 46 reporting contexts; 1 accepted opaque wrapper; 2 flattened/non-leaf names. 44 distinct configured witnesses.                        | Name check exists. Keep precise inner-leaf warnings; no additional demonstrated traversal fix remains.                                                       |
| [Absent bodies](#missing-body-correspondence)          |                                 2 records | 1 reported; 1 valid-but-suppressed                                                                                                     | Covered. Credit suppression without changing configured totals.                                                                                              |
| [Overchecks](#assessed-diagnostic-records)             |                    1,132 excluded records | 0 metadata-equality checks                                                                                                             | Swagger bug; do not port. Preserve raw records and actual request filtering.                                                                                 |
| [Inherited operations](#inherited-operation-fix)       | 2 Oracle records, already included in 131 | 2 recovered compatible source contexts; 0 warnings                                                                                     | Origin-filter bug fixed. Pair inherited project operations without warning about compliant bodies.                                                           |
| [BillingTrust / Automation](#typespec-higher-projects) |                   0 / 11 project findings | 1 / 12 project findings                                                                                                                | Preserve input-membership and compatibility checks. Project count excess is not a defect correspondence.                                                     |
| [NetApp](#netapp-49-swagger--2-typespec)               |      49 raw / 5 retained project findings | 2 project warnings                                                                                                                     | Keep empty-body detection; historical names remain under #5875.                                                                                              |

The [complete raw difference inventory](refresh-20261105-inherited/staging-comparison/differences.md)
accounts for every differing project and diagnostic target, with both engines'
counts and signed/absolute/relative gaps. The
[retained-record route index](inherited-20261105/retained-route-contexts.md)
then groups the investigated subset by project and exact PATCH route, showing
retained Swagger records and witnessed source warnings. Matching projects
remain in [the complete population](refresh-20261105-inherited/staging-comparison/projects.json),
not in the difference summary.

## Assessment method

The [saved Swagger replay](staging-comparison/schema-investigation.json)
used the actual pinned resolver/helper and compared every reported record
against the sealed staging supplement. All 1,314 records retain project,
Swagger file, full diagnostic path/message and original diagnostic-array index.
The actual predicate classified 1,263 same-name schema inequalities,
49 absent emitted leaf names and 2 absent bodies. It returned 1,339 unequal
leaves; Spectral collapsed 27 repeated identical operation-target messages
into 1,312 leaf reports, plus the 2 bodies. This measured engine behavior is
not permission to collapse distinct source checks at one position.

The [new source captures](refresh-20261105-inherited/source-attribution/inventory.json)
cover all 51 projects containing retained records. They invoke the installed
production collector/comparator, retain exact HTTP route, operation, property,
candidate, request-visibility, target and check-family evidence, and compare
each capture's complete configured diagnostic multiset to its corresponding
full-run receipt. **All 51 match.** Ten independently executed
[extraction/suppression/collision controls](refresh-20261105-inherited/source-attribution/controls/summary.json)
test those distinctions, including two families sharing one source position.

The [182-record join](refresh-20261105-inherited/source-attribution/observations.json)
contains **82 accepted contexts, 88 reporting contexts, 8 names that are not
source leaves, 2 mixed-name contexts, 1 reported body and 1 suppressed body**.
The [assessment checker](inherited-20261105/assess-contexts.py) reproduces these
aggregates and the manually reviewed acceptance membership; it does not make
the semantic decisions. The preceding 79 accepted schema contexts are unchanged
except for installed package-store prefixes, canonicalized only after verifying
all **52 ARM library members** have identical content hashes. Two Oracle
contracts were reviewed separately.

This is stronger evidence than matching a property name somewhere in a
project: the owning predicate, candidate and source target must agree.
Nevertheless, no complete per-API-version source-to-emission identity was
reconstructed. **Context counts are not normalized service-defect counts.**

## Assessed diagnostic records

The immutable [assessment receipt](assessment-20261105/results.json),
[actual schema values](assessment-20261105/schema-values.json) and
[14 tested offline controls](assessment-20261105/test_assess_diagnostics.py)
preserve the following disjoint exclusions. Every contributing helper
occurrence must have a qualifying candidate; one harmless occurrence cannot
hide another incompatible occurrence.

| Swagger bug category               |   Records | Proven condition / action                                                                                                                                               |
| ---------------------------------- | --------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Documentation only                 |       339 | Otherwise-equal schemas differ only in description/title/external documentation. Do not port.                                                                           |
| Defaults, optionally documentation |       144 | Otherwise-equal request value schemas. Creation defaults need not equal PATCH metadata. Do not port.                                                                    |
| Input-compatible mutability        |       612 | Otherwise-equal, non-read-only leaves: PUT permits create/update and PATCH permits update, despite metadata order/omission. Preserve visibility, not metadata equality. |
| Additional read-only PATCH leaves  |        37 | Every contributing PATCH leaf is explicitly read-only, hence not PATCH input. Preserve request filtering.                                                               |
| **Total excluded**                 | **1,132** | **1,314 - 1,132 = 182 retained records, not 182 valid defects.**                                                                                                        |

The [pinned Swagger implementation][swagger-function] calls
`_.differenceWith(..., _.isEqual)` on whole leaf schemas, so metadata inequality
can become a misleading "property ... is not present" report. This is a
confirmed overchecking bug, not just different count aggregation.
The schema-value extractor inspected 341 hash-verified retained inputs in
192.7 seconds; no Swagger was regenerated.

### Gap example: documentation and defaults

Agriculture's `AgriService_Update/userAssignedIdentities` has a same-name
candidate differing only in description/title: **1 Swagger report / 0
annotation-equality TypeSpec reports**. Its verified source/schema excerpts
remain in the [pinned example][historical-documentation].
For AlertProcessingRules `2021-08-08`, the actual
[PUT declaration](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/AlertProcessingRules/models.tsp#L249-L253)
and [PATCH declaration](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/AlertProcessingRules/models.tsp#L434-L438)
are, omitting documentation:

```typespec
// PUT
enabled?: boolean = true;
// PATCH
enabled?: boolean;
```

The saved schemas are `{"type":"boolean","default":true}` versus
`{"type":"boolean"}`: **1 Swagger report / 0 type/default-equality TypeSpec
reports**. **Status/action:** excluded Swagger false positive; no TypeSpec
change. Defaults do not change the boolean wire type.

<a id="gap-example-default-is-not-a-different-type"></a>
<a id="gap-example-metadata-only-inequality-in-codesigning"></a>
<a id="gap-example-mutability-metadata-is-not-a-missing-property"></a>
<a id="gap-example-read-only-patch-leaves-are-not-input"></a>

### Gap example: request metadata is not missing input

CodeSigning `CodeSigningAccounts_Update/tags` is `Record<string>` on both
sides. PATCH omits `x-ms-mutability` (default read/create/update); PUT explicitly
lists the same permissions. The verified [source/schema example][historical-mutability]
has **1 Swagger report / 0 TypeSpec project reports**: excluded metadata
overcheck, not a missing type check.

API Management `ApiGateway_Update/id` is explicitly read-only on both sides;
the saved trace differs in description/format. The verified
[source/schema example][historical-readonly] explains **1 Swagger report /
0 TypeSpec checks of that non-input leaf**. **Status/action:** exclude this
read-only PATCH overcheck; do not manufacture a warning for a value clients
cannot send.

## Schema contexts

Of the **131 retained schema records**, **42** have reporting source contexts,
**81** have compatible source contracts, **6** do not identify writable
source leaves, and **2** expose both compatible and incompatible same-named
leaves. The 42 reporting records witness **34 distinct configured diagnostics**
across their owning checks, including the compatibility fixes. This is not
a 131-to-34 defect matching.

<a id="remaining-candidates-and-fixes"></a>

### Compatibility fix

**Classification/status:** demonstrated non-versioning TypeSpec gap, fixed.
The previous implementation compared only names; violating scalar,
array/dictionary and bound controls passed incorrectly.
The existing owning rule now retains source properties and tests compatible
wire types, serialized enum values, encoding, recursive collections/partial
objects, and relevant string/item/numeric bounds. PATCH property/dictionary
null reset is allowed; null array items remain ordinary values. Bounds are
directional: PATCH must not accept values rejected by the corresponding PUT
contract. Documentation, defaults and SDK enum names are not value constraints.

**Example: API Management Logger description.** The pinned
[PUT and PATCH source](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/models.tsp#L7634-L7686)
contains:

```typespec
// LoggerContractProperties (PUT)
@maxLength(256)
description?: string;
// LoggerUpdateParameters (PATCH)
description?: string;
```

The [saved schemas](compatibility-20261105/retained-schemas.json) are
`{"type":"string","maxLength":256}` versus `{"type":"string"}`.
Logger and WorkspaceLogger yield **2 Swagger records but share 1 configured
TypeSpec compatibility warning** at `models.tsp:7686:3`; the
[exact source capture](refresh-20261105-inherited/source-attribution/source-0.json)
proves both contexts use that target. The check is no longer ignored.

**Example: RegistryTasks timeout.** The pinned PUT
[bounds](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/RegistryTasks/models.tsp#L991-L996)
are `@minValue(300) @maxValue(28800) timeout?: int32 = 3600`;
[PATCH](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/RegistryTasks/models.tsp#L1366-L1369)
is `timeout?: int32`. Saved Swagger agrees on those bounds.
This yields **1 Swagger record / 1 configured TypeSpec compatibility warning**,
verified in [the source capture](refresh-20261105-inherited/source-attribution/source-12.json).
The missing bound, not the creation default, is incompatible.

**Coverage/action:** keep the owning-rule fix and its compliant controls.
The [exact diagnostic delta](refresh-20261105/candidate-delta.json) adds
**23 configured warnings, removes none**, compared with the 94-warning
implementation. No prediction is substituted for observed output.

### Why 81 schema contexts correctly accept

These manually reviewed current-source categories are disjoint; their
[complete membership and verified aggregate](inherited-20261105/assessed-contexts.json)
are published. They are **not 81 proved harmless historical Swagger defects**.

| Compatible source contract                           | Records | Example / reason not to add a warning                                                                                                                            |
| ---------------------------------------------------- | ------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Narrower PATCH bounds                                |       4 | API Management `serviceUrl`: PATCH minLength 1 / PUT 0, both maxLength 2000. Every accepted PATCH value satisfies the PUT bound.                                 |
| Compatible serialized enums/literals                 |      11 | Workbooks `kind` has compatible wire values despite different SDK enum declarations; Oracle `source` is the same `"None"` literal in both current-source bodies. |
| Partial/null-reset/secrecy differences               |      19 | Kubernetes extensions `configurationProtectedSettings` is `Record<string> \| null` on both sides; PATCH adds `@secret`, not a different value type.              |
| Request-compatible mutability/identifier annotations |      24 | ElasticSan `baseSizeTiB` is int64 on both sides; PUT allows Create and PATCH Update. PUT request membership does not require identical lifecycle annotations.    |
| Compatible partial collections                       |      23 | Oracle's scheduled-operation list contains partial update items with the same child contracts; optional child fields need not equal PUT required lists.          |

The [saved resolved Swagger schemas](compatibility-20261105/retained-schemas.json)
and [source record index](refresh-20261105-inherited/source-attribution/observations.json)
provide both sides for every row. Representative verified declarations:
[API bounds](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/models.tsp#L2458-L2464),
[secret PATCH](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/extensions/models.tsp#L398-L406),
[secret PUT](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/kubernetesconfiguration/resource-manager/Microsoft.KubernetesConfiguration/extensions/models.tsp#L161-L167),
[ElasticSan PUT](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/elasticsan/resource-manager/Microsoft.ElasticSan/ElasticSan/models.tsp#L454-L459)
and [PATCH](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/elasticsan/resource-manager/Microsoft.ElasticSan/ElasticSan/models.tsp#L703-L707).
**Action:** accept these supported current-source contracts; deep schema
equality would recreate noise rather than fix a demonstrated value mismatch.

### Inherited-operation fix

**Classification/status:** non-versioning operation-selection bug, fixed.
The old origin guard rejected library-declared operations inherited into a
project interface. New violating controls failed before the fix; compatible
inherited pairs remain silent. Operations authored in the project keep their
original target/suppression behavior; inherited operations use their project
interface when a diagnostic needs a fallback target.

Oracle's [actual interface](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/operations/autonomousdatabase/autonomousDatabaseOperations.tsp#L9-L15)
extends `ResourceCreateAsync<AutonomousDatabase>` and authors
`update is ArmCustomPatchAsync<AutonomousDatabase, AutonomousDatabaseUpdate>`.
The original capture had **no source pair** for its
`scheduledOperationsList` Swagger record. The final
[capture](refresh-20261105-inherited/source-attribution/source-35.json)
now pairs it and accepts the compatible partial list.
The source item declarations have `dayOfWeek: DayOfWeek` for PUT and
`dayOfWeek?: DayOfWeekUpdate` for PATCH; both optional scheduled-time strings
retain minLength 1 / maxLength 50
([pinned source](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/models/autonomousdatabase/autonomousDatabase.tsp#L573-L601)).
Saved Swagger differs in nested `required` lists, not incompatible child types.

The second recovered record, `DbSystems_Update/source`, has the identical
current-source literal `"None"` on both sides
([declaration](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/oracle/resource-manager/Oracle.Database/OracleDatabase/models/basedb/dbSystem.tsp#L34-L38)).
Saved Swagger also has `"None"`, but differs in enum metadata/default/mutability.
**Observed results:** 2 retained Swagger records / 0 configured TypeSpec
warnings, with **2 compatible pairs actually evaluated**, not 2 skipped checks.
The final exact 117 -> 117 diagnostic delta is therefore expected.
**Action:** retain the origin/target fix, not warnings for compliant pairs;
historical emitted/source reconstruction remains separately scoped.

### Non-input/flattened and mixed schema names

The six schema names that are not writable source leaves are four
ManagedNetworkFabric `administrativeState` records inside read-only BFD patch
configuration, PostgreSQL's read-only PATCH `geoRedundantBackup`, and Quota's
flattened `properties` wrapper whose effective `displayName` child is compatible.
Their exact routes and source predicates are in the
[route index](inherited-20261105/retained-route-contexts.md).
**Coverage/action:** preserve effective input traversal; do not add a warning
merely because the emitted helper traverses a different leaf/wrapper.

ManagedNetworkFabric `L3IsolationDomains_Update/ipv4Routes` and `ipv6Routes`
each have **two same-named PATCH leaves**, one compatible and one incompatible.
The incompatible leaves produce **2 configured compatibility warnings** at
`L3IsolationDomain.tsp:105/117`; see
[the exact capture](refresh-20261105-inherited/source-attribution/source-30.json).
**Status/action:** checks covered; emitted one-to-one pairing remains
unassessed. Do not match or deduplicate by name alone.

## Name contexts

Of 49 emitted absent-name records, **46 have reporting source-check contexts**,
witnessing **44 distinct configured diagnostics**. The other three are:

| Exact emitted target                          | Observed source behavior                                                                                                 | Coverage / action                                                        |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| EdgeActions `EdgeActions_Update/properties`   | 0 warnings for the accepted opaque empty wrapper; PUT's emitted read-only children are flattened differently.            | Not a demonstrated absent input leaf. Preserve source request filtering. |
| Informatica `Organizations_Update/properties` | No source leaf called `properties`; 2 precise missing-name warnings on effective inner properties at `main.tsp:739/751`. | Covered inner checks, not an ignored wrapper. Do not duplicate them.     |
| MLRegistries `Registries_Update/identity`     | No corresponding source leaf name; `allOf`/direct wrappers differ while effective children agree.                        | Emission/traversal identity difference; no demonstrated name-check fix.  |

<a id="edgeactions-4-swagger--0-native"></a>
<a id="edgeactions-4-swagger--0-typespec"></a>
<a id="swagger-only-projects"></a>

The [EdgeActions source/schema example][historical-edgeactions] records
`model EdgeActionPropertiesUpdate {}` while PUT's `provisioningState` and
`attachments` are read-only. Its project totals remain **4 raw / 1 retained
Swagger / 0 TypeSpec**; the other 3 Swagger records are excluded `tags`
overchecks. The final source predicate capture establishes acceptance, replacing
the earlier unresolved wrapper explanation. All three cases have exact source
captures in the [record join](refresh-20261105-inherited/source-attribution/observations.json).

## Missing-body correspondence

| Exact operation                              | Swagger records | Configured TypeSpec warnings | Assessment / action                                                                                                            |
| -------------------------------------------- | --------------: | ---------------------------: | ------------------------------------------------------------------------------------------------------------------------------ |
| ProviderHub `ProviderMonitorSettings_Update` |               1 |                            1 | `PatchModel = void`; missing-body warning at `ProviderMonitorSetting.tsp:42:3`. Covered.                                       |
| Quota `GroupQuotaSubscriptions_Update`       |               1 |                            0 | `PatchModel = void`; applicable authored suppression. **1 valid-but-suppressed finding credited**, not an unimplemented check. |

<a id="quota-2-swagger--0-native"></a>
<a id="quota-2-swagger--0-typespec"></a>

Quota's [actual declaration](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/quota/resource-manager/Microsoft.Quota/Quota/GroupQuotaSubscriptionId.tsp#L80-L106)
places `#suppress ".../arm-resource-patch" ...` directly on the void PATCH.
The [source probe](refresh-20261105-inherited/source-attribution/source-38.json)
verifies `compilerSuppressed: true` and `configuredWarning: false`.
The Swagger replay records zero PATCH body parameters.
**Status/action:** both body cases are covered; preserve Quota's suppression.
This is pre-suppression predicate evidence, not an unsuppressed real-service
rerun or an invented 118th configured warning.

## TypeSpec-higher projects

The raw TypeSpec-higher projects are **BillingTrust 0 / 1** and
**Automation 11 / 12**. Automation's three new compatibility findings concern
`branch`, `folderPath` and `description`; its whole-project excess must not be
mistaken for one extra defect. Exact added targets are in the
[23-warning delta](refresh-20261105/candidate-delta.json).

<a id="billingtrust-0-swagger--1-typespec"></a>

**BillingTrust request-membership example:** PUT `RuleProperties.kind` is
`@visibility(Lifecycle.Read) kind: RuleKind`; PATCH's `kind: RuleKind` is writable.
The shared Swagger PUT schema includes read-only `kind`, so Swagger reports 0.
TypeSpec reports 1 because it is not PUT request input. The verified
[source/schema example][historical-billingtrust] retains exact versions/targets.
**Coverage/action:** preserve the input-membership check. A different intended
contract needs a spec-owner decision or applicable suppression, not a visibility
relaxation merely to equalize totals.

## NetApp: 49 Swagger / 2 TypeSpec

All 49 Swagger records are schema inequalities; **5 remain after exclusions**.
The two TypeSpec warnings have separate causes:

<a id="gap-example-existing-empty-patch-is-not-an-absent-body-parameter"></a>

- `Snapshots_Update`: an existing `model SnapshotPatch {}` produces **0
  Swagger / 1 TypeSpec empty-body warning**. The Swagger predicate counts body
  parameters, not input leaves, and falsely accepts the empty body.
  [Pinned source/schema trace][historical-empty] proves this false negative.
  **Action:** retain the TypeSpec check; do not port that bug.
- `Volume.tsp:1361:3`, `usageThreshold20250901`: **1 source missing-name warning**,
  with exact historical emitted counterpart unassessed. PUT and PATCH have
  separate `@renamedFrom(..., "usageThreshold")` declarations.
  **Action:** defer historical-name reconstruction to #5875.

<a id="gap-example-source-names-are-not-historical-wire-names"></a>

## Versioning boundary

The user explicitly excluded gaps belonging to
[#5875](https://github.com/Azure/typespec-azure/issues/5875).
This includes active-version operations, property availability, historical names
and historical types; it does not exclude every check in a versioned service.
The [18-removal assessment](simplification.md#corpus-differences) and
[verified issue follow-up](https://github.com/Azure/typespec-azure/issues/5875#issuecomment-6652676528)
retain each historical case. KeyVault/DNS have renamed predecessors; historical
absence was not proved. Those removals are not 18 established lost violations.
**Status/action:** genuine historical functionality remains missing/deferred;
do not restore bespoke reconstruction in this rule. This is why the scoped
source-policy result is not full Swagger equivalence.

<a id="swagger-higher-outliers-and-remaining-limits"></a>

## Remaining comparison limits and reproducibility

The context join witnesses **79 distinct configured warnings**: 23 compatibility,
55 missing-name and 1 absent-body warning. It does not account for all 117
warnings as emitted counterparts. The other 38 are preserved in the complete
raw project/target inventory; neither their absence from this retained-record
join nor opposite count directions establishes missed or extra service defects.
Unsupported/ambiguous top-level bodies remain unassessed, and supported
constraint checks are not a general regex/schema-subset solver.

The old [94-warning investigation][historical-report] preserves its full
examples and earlier conclusions as history. The current report replaces,
not appends corrections to, its name-only and unresolved-Oracle conclusions.
For current recovery and independent saved-data checks, use [replay.md](replay.md).
All raw inputs, membership, configured findings, suppression probes and both
gap directions remain available.

**Final decision:** retain the demonstrated owning-rule fixes and compatible
current-source behavior. No further non-versioning production change is
justified by these investigated contexts. Historical projection and complete
cross-engine violation totals remain outside the established result.

[swagger-function]: https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-properties-correspond-to-put-properties.ts#L15-L70
[historical-report]: https://github.com/msyyc/typespec-azure/blob/4752fb8c73c226ee0e53edf2d776c62a5f08a7b2/migration-evidence/tasks/pr5481-patch-correspondence/gap-investigation.md
[historical-documentation]: https://github.com/msyyc/typespec-azure/blob/4752fb8c73c226ee0e53edf2d776c62a5f08a7b2/migration-evidence/tasks/pr5481-patch-correspondence/gap-investigation.md#gap-example-descriptiontitle-only-agriculture-identity-report
[historical-mutability]: https://github.com/msyyc/typespec-azure/blob/4752fb8c73c226ee0e53edf2d776c62a5f08a7b2/migration-evidence/tasks/pr5481-patch-correspondence/gap-investigation.md#gap-example-mutability-metadata-is-not-a-missing-property
[historical-readonly]: https://github.com/msyyc/typespec-azure/blob/4752fb8c73c226ee0e53edf2d776c62a5f08a7b2/migration-evidence/tasks/pr5481-patch-correspondence/gap-investigation.md#gap-example-read-only-patch-leaves-are-not-input
[historical-edgeactions]: https://github.com/msyyc/typespec-azure/blob/4752fb8c73c226ee0e53edf2d776c62a5f08a7b2/migration-evidence/tasks/pr5481-patch-correspondence/gap-investigation.md#edgeactions-4-swagger--0-typespec
[historical-billingtrust]: https://github.com/msyyc/typespec-azure/blob/4752fb8c73c226ee0e53edf2d776c62a5f08a7b2/migration-evidence/tasks/pr5481-patch-correspondence/gap-investigation.md#billingtrust-0-swagger--1-typespec
[historical-empty]: https://github.com/msyyc/typespec-azure/blob/4752fb8c73c226ee0e53edf2d776c62a5f08a7b2/migration-evidence/tasks/pr5481-patch-correspondence/gap-investigation.md#gap-example-existing-empty-patch-is-not-an-absent-body-parameter
