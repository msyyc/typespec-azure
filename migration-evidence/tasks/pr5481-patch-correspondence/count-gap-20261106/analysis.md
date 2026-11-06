# Reconciling 182 Swagger records and 117 TypeSpec warnings

**The net 65 is fully accounted for. It is not 65 missing checks. There is,
however, a real TypeSpec overchecking bug affecting seven observed warning
targets, which should be fixed rather than deferred to #5875.**

This supplement reuses the unchanged 487-project run. "Outside the join" means
not witnessed by a retained Swagger record's exact reviewed source context;
it does not mean the project's Swagger total is zero. No one-to-one historical
defect identity is invented.

## Record-to-warning bridge

The [reconciliation and individual identities](reconciliation.json) establish:

| Conversion                                             | Change | Running count |
| ------------------------------------------------------ | -----: | ------------: |
| Retained Swagger records                               |        |           182 |
| Remove 82 compatible and 8 non-input contexts          |    -90 |            92 |
| Remove Quota's suppressed check from the warning count |     -1 |            91 |
| Two records each witness two distinct checks           |     +2 |            93 |
| Count shared source-warning witnesses once             |    -14 |            79 |
| Include the remaining configured TypeSpec warnings     |    +38 |           117 |

Therefore **65 = 90 + 1 + 14 - 2 - 38**. The 13 difference between 92
check-covered records and 79 configured witnesses is **1 suppression + 14
repeated associations - 2 additional checks**, not thirteen duplicated defects.

The repeated associations belong to eleven source warnings:

| Project                 | Source warnings shared across records | Additional associations |
| ----------------------- | ------------------------------------: | ----------------------: |
| ApiManagement           |                                     4 |                       4 |
| MachineLearningServices |                                     1 |                       2 |
| ManagedNetworkFabric    |                                     3 |                       3 |
| Support                 |                                     1 |                       1 |
| AppService              |                                     2 |                       4 |
| **Total**               |                                **11** |                  **14** |

For example, one ApiManagement `description` warning covers both Logger and
WorkspaceLogger routes. Conversely, ManagedNetworkFabric's
`ExternalNetworks_Update/prefixLimits` and `InternalNetworks_Update/prefixLimits`
records each witness **two** warnings, on IPv4 and IPv6 declarations at
`models/common.tsp:1090/1115`. Neither warning is discarded merely because the
encoded name is identical.

Identity is `(project, original Swagger diagnostic-array index)` for records
and `(project, full-run diagnostic-array index)` for warnings. Each record's
warning-index set removes only repeated references to the same diagnostic
occurrence within that record. Distinct diagnostic occurrences, including
different checks at one source position, remain separate. All **51 capture
arrays equal the corresponding full-run arrays in order**, not only as
multisets. The 51-project capture filenames are not used as full-run indices.

The independently summed per-project retained-record differences are **+89
Swagger-higher, -24 TypeSpec-higher, absolute 113, net 65**. The machine-readable
project rows preserve opposing differences rather than cancelling them away.

## All 38 warnings outside the join

The following rows partition every outside-join diagnostic. Indices below are
the project's original full-run diagnostic-array indices, not global indices.
The [complete target inventory](reconciliation.json) preserves each message,
source location, original receipt, classification and rationale.

| Project / diagnostic indices                                      | Warnings | Coverage decision                                                              |
| ----------------------------------------------------------------- | -------: | ------------------------------------------------------------------------------ |
| ContainerApps / 0, 1                                              |        2 | Fix empty-wrapper overcheck                                                    |
| DatabaseFleetManager / 0                                          |        1 | Fix empty-wrapper overcheck                                                    |
| DeviceRegistry / 0                                                |        1 | Fix empty-wrapper overcheck                                                    |
| GitHubNetwork / 0                                                 |        1 | Fix empty-wrapper overcheck                                                    |
| SQL / 0                                                           |        1 | Fix empty-wrapper overcheck                                                    |
| AppService / 2                                                    |        1 | Fix empty-wrapper overcheck                                                    |
| ManagedNetworkFabric / 2, 4, 7, 9, 11, 13, 15, 17, 18, 20, 21, 23 |       12 | Defer historical reconstruction to #5875                                       |
| NetApp / 0                                                        |        1 | Defer historical reconstruction to #5875                                       |
| Automation / 0-5                                                  |        6 | Retain input-membership checks; review writable `systemData` model             |
| ServiceFabric / 0-5                                               |        6 | Retain input-membership checks; review writable `systemData` model             |
| BillingTrust / 0                                                  |        1 | Retain source input-membership check; owner decision on discriminator contract |
| DataBoxEdge / 0                                                   |        1 | Retain input-membership check; review PATCH of read-only `edgeProfile`         |
| Informatica / 0, 1                                                |        2 | Retain precise inner-property checks; correct unintended PATCH shape           |
| OffAzure / 0                                                      |        1 | Retain input-membership check; review writable `provisioningState`             |
| NetApp / 1                                                        |        1 | Retain empty-body check; correct empty update model/contract                   |
| **Total**                                                         |   **38** | **13 deferred + 7 overchecks to fix + 18 checks to retain**                    |

### Empty-wrapper overcheck to fix

**Classification:** extra TypeSpec warnings; **status:** confirmed owning-rule
defect, recommended fix not implemented.

| Observed target                         | Source location                    |
| --------------------------------------- | ---------------------------------- |
| ContainerApps `networking`              | `models.tsp:7037:3`                |
| ContainerApps `vnetConfiguration`       | `models.tsp:2711:3`                |
| DatabaseFleetManager `properties`       | `models.tsp:340:3`                 |
| DeviceRegistry `bringYourOwnRoot`       | `ns_policy.tsp:94:3`               |
| GitHubNetwork `properties`              | `NetworkSettingsResource.tsp:37:3` |
| SQL `properties`                        | `models.tsp:11853:3`               |
| AppService `containerAppsConfiguration` | `models.tsp:6560:3`                |

The [pinned source excerpts](source-evidence.json) show the common shape:
the object container exists in PUT and PATCH, but its children are
Create/Read-only rather than Update-visible. For example, both Fleet request
models use `FleetProperties`; its `description` is Create/Read-visible and
`provisioningState` is Read-only. The PATCH body also has valid `tags`, so this
is not an empty top-level PATCH.

The [production collector](https://github.com/Azure/typespec-azure/blob/0121903975ab45cde7d7aca37cf50ffd7f3855d3/packages/typespec-azure-resource-manager/src/rules/arm-resource-patch-body.ts#L172-L265)
keeps PATCH's container as an opaque leaf when no child is Update-visible.
It flattens the PUT container into Create-visible children instead, then
compares only leaf names. The PUT container candidate has been lost, so an
existing matching object is falsely called absent.

**Executed reproducer:** the [captured fixture](fixtures.json) uses the same
body shape on PUT and PATCH:

```typespec
model P {
  @visibility(Lifecycle.Read, Lifecycle.Create) value?: string;
}
@route("/widgets") @put op put(
  @body body: {
    properties?: P;
    tags?: string;
  },
): void;
@route("/widgets") @patch op patch(
  @body body: {
    properties?: P;
    tags?: string;
  },
): void;
```

| Engine / control                                        | Observed result                                                                              |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| TypeSpec linter, identical bodies above                 | **1 false missing-`properties` warning**; exact captured PUT/PATCH body type names are equal |
| TypeSpec linter, same wrapper with Update-visible child | 0 warnings                                                                                   |
| TypeSpec linter, genuinely extra leaf                   | 1 missing-property warning                                                                   |
| TypeSpec linter, genuinely absent wrapper               | 1 missing-property warning                                                                   |
| Swagger linter, these new controls                      | Not run; no emitted correspondence is claimed                                                |

The fixture has **no version decorators**. Merely placing one observed case
in a versioned service does not make this a #5875 gap.

**Coverage status:** all seven are observed configured warnings with
source-inspected instances of the reproduced container/leaf asymmetry. This
is not seven newly compiled service traces or seven missed Swagger violations.

**Recommended action and rationale:** fix `arm-resource-patch-body.ts` so an
opaque PATCH object can be compared with the corresponding PUT object
container at the correct payload position, preserving visibility and type/
constraint checks. Retain container/path information rather than globally
matching a common name or blindly skipping empty wrappers. Turn the first
control into a zero-warning regression; retain both genuinely absent-input
controls and add a same-container incompatible-value control for the chosen
implementation. Run owning tests and fresh relevant final coverage on that
changed candidate. The existing 117 warnings cannot validate a future fix.

This improves correctness rather than reducing a raw count for its own sake.
The exact post-fix warning gain is a prediction until that candidate is run;
the current evidence and total stay **117**.

### Historical versioning

**Classification:** source-only historical discrepancies; **status:** deferred
under the user's explicit #5875 policy.

ManagedNetworkFabric has eleven `*Deprecated` warning targets carrying
`@renamedFrom`/`@removed` metadata and one `NetworkInterface.description`
warning. The latter is not simply a missing current input: its PUT predecessor
is `descriptionDeprecated` renamed from `"description"`, while the newer PUT
`description` is Read-only and the old PATCH declaration is removed.
For example, the pinned source contains:

```typespec
@removed(Versions.v2025_07_15)
@renamedFrom(Versions.v2025_07_15, "description")
@doc("Description of the interface.")
descriptionDeprecated?: string;
```

NetApp's `usageThreshold20250901` supplies the thirteenth warning, with repeated
added/removed boundaries and historical wire name `"usageThreshold"`.
The [saved source predicates](../refresh-20261105-inherited/source-attribution/inventory.json)
and [exact decorators/source excerpts](source-evidence.json) preserve the
declarations; raw current source names are not historical wire names.

**Swagger comparison:** exact per-version counterparts for these thirteen
source warnings remain unassessed, not thirteen proven API defects.
**Recommended action:** defer names, availability and operation projection to
[#5875](https://github.com/Azure/typespec-azure/issues/5875), not a bespoke
history implementation in this rule. Do not count this deferral as implemented
historical functionality or reclassify the seven visibility-wrapper cases
above as historical.

### Valid source checks to retain

**Classification:** checks not represented by the retained-record join;
**coverage:** covered for the assessed source-input policy.

**Seventeen warnings check actual PUT request membership:**

- **Automation 6 + ServiceFabric 6:** custom PATCH models expose
  `systemData` without Read-only visibility. Its six library members are
  unannotated, while the standard resource's `systemData` container is
  `@visibility(Lifecycle.Read)`. The response schema's existence does not make
  those members PUT input. Different member messages at one source position
  remain six checks, not one.
- **BillingTrust 1 + DataBoxEdge 1 + OffAzure 1:** respectively writable PATCH
  `kind`, nested `edgeProfile.subscription.id`, and `provisioningState`
  correspond to Read-only PUT source inputs/ancestors.
- **Informatica 2:** the existing organization-route capture has no PUT
  candidates for `informaticaOrganizationProperties` or `existingResourceId`.
  Swagger's retained outer `properties` report is not an exact source leaf;
  the two precise inner findings are therefore outside that record join,
  not missing TypeSpec warnings.

The [source evidence](source-evidence.json) preserves all relevant excerpts,
including the library's Read-only `systemData` container and unannotated members.
For example, the actual OffAzure PUT declaration has:

```typespec
@visibility(Lifecycle.Read)
provisioningState?: ProvisioningState;
```

Its PATCH `VmwareSiteUpdateProperties.provisioningState` has no such visibility.
The [BillingTrust source/schema explanation](../gap-investigation.md#typespec-higher-projects)
shows why Swagger's response-schema membership incorrectly accepts the
Read-only property as input. The same source-input distinction explains the
Read-only ancestor/member cases, without claiming new Swagger execution.

**One further warning is NetApp's empty `SnapshotPatch`:** the
[existing source/schema trace](../gap-investigation.md#netapp-49-swagger--2-typespec)
proves that Swagger counts the body parameter and misses the empty payload.
TypeSpec checks the payload itself and reports it.

**Recommended action and rationale:** retain all eighteen checks. Model/API
owners should mark unintended PATCH metadata Read-only or remove it, correct
unintended PATCH property shapes, and provide a meaningful update body where
required. If the intended contract is genuinely asymmetric, confirm it and
document an appropriate policy exception/suppression; BillingTrust's
discriminator especially needs its owner's contract decision. These are
model/policy follow-ups, not justification to weaken the linter or fabricate
matched Swagger defects. No spec edits are made by this report.

## Validation and limits

[reconcile.py](reconcile.py) checks all 487 frozen successful receipts,
all 182 unique retained identities and the exact diagnostic-array mapping for
51 captures. It computes the incidence graph, verifies the 38-case manual
decision inventory and independently sums per-project results.
[Seven focused tests](test_reconcile.py) exercise shared checks, multiple checks
per record, repeated references within a record, suppression, separate
diagnostic occurrences/projects and invalid identities.

[capture.mjs](capture.mjs) ran four isolated controls with the same Node
`v26.5.0`, candidate/spec revisions and body/comparator/extractor hashes as
the frozen run. It is a characterization of the existing bug, not a claim
that production is fixed. [fixtures.json](fixtures.json) retains authored
source, configured diagnostics and exact production predicate captures.
The executable path/hash is unchanged from the existing runtime receipt.

The attempted shared bulk-capture gate was busy with another session, so no
new real-service extraction was started or claimed. An initial fixture-helper
preparation error occurred before compilation; its corrected, fully preserved
final four-control run passed. Real-service classifications use the frozen
configured receipts and **35 exact excerpts from the clean pinned specs
checkout**, not a new coverage run. This does not block the observed-data
count reconciliation or the isolated non-versioning defect reproducer.

Offline replay, with no dependency installation or spec compilation:

```powershell
python -B -m unittest discover -s .\count-gap-20261106 -p test_reconcile.py
python -B .\count-gap-20261106\reconcile.py check
```

The [manual decisions](decisions.json) are semantic assessments, not decisions
made by the aggregation script. [Byte hashes](reconciliation.json) cover every
input the reconciliation loads; the old whole-tree seal is not relabelled as
covering this supplement. Historical cross-engine violation totals remain
unassessed, and the seven-warning overcheck remains unfixed. There is **no
unexplained arithmetic residual**, but there is also **no full-equivalence
or completed-migration claim**.
