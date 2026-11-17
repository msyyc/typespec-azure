# Scoped PATCH assessment

This assessment reuses saved observations. It does not execute either linter,
change the implementation, or regenerate Swagger. The [project inventory](scoped-project-differences.md)
starts with the unequal scoped counts and unshared check groups. Each project
links to its original route, property and source evidence.

## Membership and observed diagnostics

| Swagger linter               | Material check                               | Assessed TypeSpec callback family           | Swagger reported | TypeSpec observed after exclusions | Status and member evidence                                                                                                                                                                     |
| ---------------------------- | -------------------------------------------- | ------------------------------------------- | ---------------: | ---------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PatchBodyParametersSchema`  | Required/default input and update visibility | `required`, `default`, `visibility`         |              715 |                                881 | Authored input and compliant controls are covered; emitted-only fields and broader TypeSpec checks differ. [Member](members/PatchBodyParametersSchema/migration.md)                            |
| `ConsistentPatchProperties`  | Request versus resource layout               | `missing`                                   |              150 |                                304 | Supported authored layouts are covered; emitted representation, unsupported shapes and overlapping owning warnings remain unassessed. [Member](members/ConsistentPatchProperties/migration.md) |
| `UnSupportedPatchProperties` | Immutable properties                         | `immutable`                                 |              110 |                                 61 | Exposed immutable input and compliant controls are covered; excluded input and reference resolution differ. [Member](members/UnSupportedPatchProperties/migration.md)                          |
| Combined                     | All three                                    | Distinct target-rule findings, counted once |              975 |                              1,246 | The family partition is not per-defect correspondence.                                                                                                                                         |

The callback-family trace was made at `94b316787`; the later
[`8a92389c9` comparison](runs/20261102-8a92389c9/diagnostic-differences.json)
reproduced the exact per-project diagnostic multisets, not the instrumentation.
Some independent checks can share a target. Do not deduplicate them or assume
that a family finding is the same defect as a Swagger report.

## Exclusion and population ledger

The retained Swagger reports cover the selected version of 487 successful
projects. The TypeSpec linter was explicitly enabled in an unprojected source
program. Of 1,337 target-only diagnostics, this assessment removes only these
91 identified observations outside the selected service/version population:

| Project                  | Excluded | Evidence                                                                                                                                                                                                                         |
| ------------------------ | -------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Search                   |       34 | Client-only override, not the service PATCH operation. [Source](detailed-analysis.md#source-and-operation-populations)                                                                                                           |
| ManagedNetworkFabric     |       29 | Removed or renamed input, including 14 array-layout findings. [Version evidence](fresh-examples.md#version-populations)                                                                                                          |
| ProgrammableConnectivity |        6 | Removed enclosing input and newly required descendants in an unprojected operation. [Version evidence](fresh-examples.md#version-populations)                                                                                    |
| NetApp                   |        6 | Two removed source inputs and four extra occurrences from the older same-route operation. The individual same-location duplicate is not separately identifiable. [Source](detailed-analysis.md#source-and-operation-populations) |
| PipelineGroups           |        7 | Defaults under removed fields or ancestors. [Selected-version source](#additional-version-evidence)                                                                                                                              |
| CognitiveServices        |        4 | Findings from the removed Workbench update operation. [Selected-version source](#additional-version-evidence)                                                                                                                    |
| StandbyPool              |        2 | Removed capacity properties. [Selected-version source](#additional-version-evidence)                                                                                                                                             |
| AzureFleet               |        1 | Removed allocation-policy model. [Selected-version source](#additional-version-evidence)                                                                                                                                         |
| DesktopVirtualization    |        1 | Removed input. [Source](detailed-analysis.md#source-and-operation-populations)                                                                                                                                                   |
| DeviceRegistry           |        1 | Removed ancestor. [Source](detailed-analysis.md#source-and-operation-populations)                                                                                                                                                |

The [machine-readable ledger](scoped-accounting.json) records each excluded
project, route, check, property-path text, multiplicity and original ledger row.
It preserves the 1,337 unfiltered observations. Other version-scoped or
unmatched-route findings remain in the scoped count when attribution is
uncertain. This partial filter is not a projected, aligned comparison.

The scoped project sets are 121 Swagger projects, 126 TypeSpec projects,
113 shared, eight Swagger-only and 13 TypeSpec-only. Equal project presence
does not establish matching checks. The [scoped inventory](scoped-project-differences.md)
retains both directional differences: 103 Swagger excess versus 374 TypeSpec
excess, absolute 477. Raw, unfiltered project and location counts remain in
the [original analysis](detailed-analysis.md#counting-levels).

## Additional version evidence

These are source-population differences, not diagnosed defects in the selected
Swagger versions. The [ledger](scoped-accounting.json) retains each exact
route, path and occurrence. No selected-version Swagger excerpt exists for an
input that was removed from that version.

**AzureFleet**, selected `2026-08-01`: the reported
`properties.zoneAllocationPolicy.distributionStrategy` is under a
[removed model](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/azurefleet/resource-manager/Microsoft.AzureFleet/AzureFleet/fleet.tsp#L569-L578):

```typespec
@removed(Versions.v2026_08_01)
model ZoneAllocationPolicy {
  /** Distribution strategy used for zone allocation policy. */
  distributionStrategy: ZoneDistributionStrategy;

  /** Zone preferences, required when zone distribution strategy is Prioritized. */
  @identifiers(#[])
  zonePreferences?: Array<ZonePreference>;
}
```

**CognitiveServices**, selected `2026-09-15-preview`: four required findings
come from the
[removed legacy Workbench operation](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices/Workbench.tsp#L159-L174).
The selected operation uses
[`WorkbenchUpdate`](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices/Workbench.tsp#L83-L92),
whose properties are optional. The unprojected legacy operation instead uses
the full `Workbench` body, mixing declarations from different versions.

```typespec
@removed(Versions.v2026_09_01)
@renamedFrom(Versions.v2026_09_15_preview, "update")
@tag("Workbenches")
@patch(#{ implicitOptionality: false })
updateLegacy is ArmCustomPatchAsync<Workbench, PatchModel = Workbench>;
```

**StandbyPool**, selected `2026-04-01`: the container and VM pool findings
both target `oldMaxReadyCapacity`, which was
[removed in `2025-10-01`](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/standbypool/resource-manager/Microsoft.StandbyPool/StandbyPool/standbyContainerGroupPool.tsp#L55-L60).

```typespec
@removed(Microsoft.StandbyPool.Versions.`2025-10-01`)
@renamedFrom(Microsoft.StandbyPool.Versions.`2025-10-01`, "maxReadyCapacity")
oldMaxReadyCapacity: int64;
```

**PipelineGroups**, selected `2026-04-01`: seven defaults occur under removed
inputs: three UDP descendants, two exporter concurrency descendants, the old
batch timeout and the old syslog protocol. For example, the
[UDP ancestor](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/monitoringservice/resource-manager/Microsoft.Monitor/PipelineGroups/typespec/pipelineGroup.tsp#L106-L109)
is removed at the selected version:

```typespec
@removed(Microsoft.Monitor.Versions.v2026_04_01)
udp?: UdpReceiver;
```

The other removed declarations are
[concurrency](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/monitoringservice/resource-manager/Microsoft.Monitor/PipelineGroups/typespec/exporters/AzureMonitorWorkspaceLogs.tsp#L14-L16),
[old timeout](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/monitoringservice/resource-manager/Microsoft.Monitor/PipelineGroups/typespec/processors/BatchProcessor.tsp#L16-L21),
and [protocol](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/monitoringservice/resource-manager/Microsoft.Monitor/PipelineGroups/typespec/receivers/SyslogReceiver.tsp#L15-L17).
Six other PipelineGroups defaults remain in the scoped count.

**NetApp**, selected `2026-06-15-preview`: `updatePrevious` and `update` share
a route in unprojected source. The
[previous operation](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/NetAppAccount.tsp#L929-L933)
is removed at the selected version. Four excess observations come from the
two operations, including one of two same-key array-default observations.
The saved source location does not distinguish the individual duplicate.

```typespec
@removed(Versions.v2026_06_15_preview)
@renamedFrom(Versions.v2026_06_15_preview, "update")
@sharedRoute
updatePrevious is ArmCustomPatchAsync<
```

## Count reconciliation

Before reporting, the Swagger functions returned 1,057 observations. Spectral
reported 975, collapsing 82 observations by its reporting fingerprint.
The [captured control](detailed-analysis.md#reporting-stage-collapse) retains
the distinct callbacks. They must not be presented as 82 removed defects.

The accounting key is project, exact PATCH route, check family and encoded
property-path text. It has 834 shared-key occurrences, 223 unmatched Swagger
callbacks and 412 unmatched TypeSpec diagnostics after the exclusions.
The shared key is not proof of a shared defect. Raw Swagger reports cannot be
assigned uniquely to each callback category after Spectral's collapse.

| Difference                                                                                             | Swagger unmatched callbacks | TypeSpec unmatched diagnostics | Coverage and proposed action                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------ | --------------------------: | -----------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Effective input](detailed-analysis.md#effective-input-and-synthetic-fields)                           |                         165 |       0 from the selected rule | Read/Create-only fields or ancestors are excluded by the TypeSpec input policy. Retain the observed distinction; reviewers must decide the intended policy. Overlapping owning-rule diagnostics were not captured. |
| [Synthetic discriminator or optional input](detailed-analysis.md#effective-input-and-synthetic-fields) |                           6 |       0 from the selected rule | Five emitted discriminators have no authored field; one candidate input is optional. Whether emitted-only behavior is required remains a policy decision.                                                          |
| [Missing parents versus leaves](detailed-analysis.md#parent-and-leaf-accounting)                       |                          52 |                            175 | Swagger stops at parents while TypeSpec reports supported descendant paths. These counts do not identify equivalent defects.                                                                                       |
| [Falsy defaults and arrays](detailed-analysis.md#defaults-and-arrays)                                  |                           0 |                            185 | TypeSpec reports 128 falsy defaults and 57 additional array defaults. Removed-version array findings were excluded separately. Review the intended extension; do not remove checks only to equalize totals.        |
| [Recursive reference](detailed-analysis.md#recursive-reference-boundary)                               |                           0 |                             24 | The saved callback has no inspectable recursive request children. A counterfactual control explains the boundary, not production equivalence.                                                                      |
| [Remaining source/operation differences](detailed-analysis.md#source-and-operation-populations)        |                           0 |                              7 | Seven no-identical-route findings remain observed, but their selected-version attribution is unassessed. Resolve with an aligned comparison before changing code.                                                  |
| [Representation policy](detailed-analysis.md#representation-policy-boundaries)                         |                           0 |                             21 | Twelve associated-resource name findings and nine optional/default-free NetApp findings need policy or aligned-emission review; neither is an approved parity decision.                                            |

The complete observed arithmetic is:

`975 - 1,246 = 165 + 6 + 52 - 175 - 185 - 24 - 7 - 21 - 82 = -271`.

This reconciles counts, not one-to-one correspondence. Suppressed and other
overlapping owning-rule warnings were not measured, so their contribution and
any resulting semantic residual are unassessed, not zero. The
[recount script](scope-recount.py) reproduces the scoped ledger and inventory
from the saved inputs without running either linter:

```powershell
mise exec -- python migration-evidence\tasks\pr5294\scope-recount.py
```

## Suppression and runtime limits

The saved corpus enabled only the selected TypeSpec rule; it did not capture
the configured or suppressed diagnostics of other owning rules. The
[assessed `arm-resource-patch` source](https://github.com/msyyc/typespec-azure/blob/8a92389c9f9488035ab65c6ed3e08a49cc822f25/packages/typespec-azure-resource-manager/src/rules/arm-resource-patch.ts)
and ARM artifact show that the rule has a
`modelSuperset` branch that can overlap the layout check. Its other messages
do not establish the same check. A distinct owning diagnostic and a
target-rule diagnostic must both be retained if each is actually captured.

The [directive inventory](suppression-inventory.json) found 47 authored
`arm-resource-patch` directives in 44 tracked files across 22 selected project
roots, and no directives naming the target rule in those roots. A directive
does not prove a warning was suppressed. Imports outside these roots, other
owning rules, and the number and attribution of suppressed warnings remain
unassessed. Reproduce the source scan against the clean frozen specs checkout:

```powershell
mise exec -- python migration-evidence\tasks\pr5294\scan-suppressions.py <FROZEN_SPECS>
```

The published candidate archive was independently downloaded and matched its
recorded 2,466,985 bytes and SHA-256
`2b6ee7ef151d0d1f659060bd948ba328e556f12a3fc2f74d14fc940da1ff270e`.
Comparing every packaged file with the currently installed shared runtime found
57 differences in 411 ARM files and 21 differences in 1,070 compiler files.
Matching entrypoints alone do not prove the closure. No supplementary compile
was run against that runtime and no suppressed-warning count is inferred.
[Archive and original worker receipts](fresh-evidence.md#november-2-final-review-fix-run)
remain the evidence for the historical run.

## Assessed revision and validation

The assessed implementation is `8a92389c9f9488035ab65c6ed3e08a49cc822f25`,
with core `cefb035e7721a6fdcb6de605b5f469b93055a880`, specs
`2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`, and the retained
[`frozen-reference` baseline](fresh-evidence.md#frozen-inputs-and-result).
The saved baseline and candidate have different producer/runtime closures.
Selected-version Swagger and source-scoped TypeSpec are not proven equivalent.

The assessed review fixes decline ambiguous selected response layouts without
substituting a lower-priority response, remove namespace-local GET discovery,
exclude whole derived `File` models, and compare resources using all-visibility
metadata. An encoded-name ambiguity guard prevents a Query member from masking
an inherited Read member while retaining independent safety and sibling checks.
These changes narrow some synthetic cases; unchanged corpus diagnostics do not
prove that every supported case is unchanged. The
[case-to-review mapping](runs/20261102-8a92389c9/local-validation.json)
retains the focused controls.

At that assessed revision, 487 projects completed; 757 distinct ARM tests,
112 canonical PATCH tests, 20 injected PATCH controls and 37 applicable portable
controls passed. Two initial test timeouts passed focused retries; six unrelated
portable controls were excluded before that run. Historical failures and
recovery steps remain in the [validation receipt](runs/20261102-8a92389c9/local-validation.json)
and [provenance](fresh-evidence.md#november-2-final-review-fix-run).
Default/configured corpus activation and suppressed owning diagnostics were
not assessed.

The PR later moved to a different compiler gitlink. The saved run does not
validate that later source/closure; current-head corpus coverage is unassessed.
Any acceptance decision needs the applicable current-head checks, aligned
coverage and review gates. This report does not authorize or approve a source
change, policy retirement or migration acceptance.

The older [publication manifest](publication-manifest.json) is a historical
receipt for evidence commit `dc4132bca`; its hashes must not be interpreted
as the current report's hashes. The current report has a separate publication
receipt.
