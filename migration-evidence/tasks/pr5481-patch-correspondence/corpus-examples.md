# Real-service observations

These original TypeSpec source investigations are **not exact cross-engine
diagnostic matches**. The shared production baseline did not evaluate the
staging-only rule. The subsequent [staging comparison](staging-comparison/summary.json)
and [gap investigation](gap-investigation.md) supply actual Swagger observations
separately. Complete original native project/target/message accounting is
retained unchanged in `project-inventory.json`, `coverage-summary.json`, and
`runs/full-corpus`.

## Inherited-writable traversal: DevCenter outlier

Project: `specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter`.

This is the largest project total: **90 missing-name findings**. Representative
messages name `identityType`, `userAssignedIdentityResourceId`, and
`federatedClientId` at `models.tsp:688:3`. No conclusion that all 90 are false
positives is supported by this investigation.

[Frozen model declarations](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/devcenter/resource-manager/Microsoft.DevCenter/DevCenter/models.tsp#L655-L688)
include this inheritance structure:

```typespec
model DevCenterProperties extends DevCenterUpdateProperties {
  @visibility(Lifecycle.Read)
  provisioningState?: ProvisioningState;

  @visibility(Lifecycle.Read)
  devCenterUri?: string;
}

model DevCenterUpdateProperties {
  encryption?: Encryption;
  // Other writable properties omitted.
}
```

The PUT resource uses `DevCenterProperties`; PATCH uses
`DevCenterUpdateProperties`. A fresh
[minimal helper control](semantic-evidence.md#executed-follow-up-inherited-writable-put-properties-behind-read-only-direct-members)
confirmed one spurious missing-`identityType` diagnostic with this shape and
zero compiler diagnostics. The direct-property recursion gate sees no writable
direct member on the derived PUT model, retains an opaque wrapper, but flattens
PATCH's base model. The inherited writable declaration is shared, so the control
demonstrates a traversal false positive, not an actual missing wire property.

Disposition: report a confirmed mechanism and its relevant real-service
structure. The complete 90-finding validity classification, historical projected
schemas, and original Swagger correspondence remain unassessed; no source fix
is included.

## Effective-empty PATCH: NetApp Snapshot

Project: `specification/netapp/resource-manager/Microsoft.NetApp/NetApp`.

The saved TypeSpec observation is one `emptyPatchBody` diagnostic at
`Snapshot.tsp:116:3`:

> The PATCH request body must contain at least one property.

[Frozen source](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/netapp/resource-manager/Microsoft.NetApp/NetApp/Snapshot.tsp#L85-L116):

```typespec
#suppress "@azure-tools/typespec-azure-resource-manager/no-empty-model" "For backward compatibility"
model SnapshotPatch {}

@armResourceOperations
interface Snapshots {
  // Other operations omitted.
  @patch(#{ implicitOptionality: false })
  update is ArmCustomPatchAsync<Snapshot, PatchModel = SnapshotPatch>;
}
```

The suppression is for a different rule; it does not suppress `arm-resource-patch`.
The original Swagger predicate's body-parameter count check does not reject an
existing object body with zero collected leaves when PUT has a body. The
[executed minimal control](semantic-evidence.md#empty-patch-model-versus-absent-patch-body)
demonstrates that predicate difference. This original source-control
investigation did not emit schemas or execute Swagger staging. The subsequent
retained-Swagger evaluation is separate evidence, not a replay of this control.

Disposition: report the current TypeSpec finding and semantic difference;
neither change this service nor declare its compatibility exception erroneous.

## Absent PATCH body: ProviderHub

Project:
`specification/providerhub/resource-manager/Microsoft.ProviderHub/ProviderHub`.

One saved TypeSpec diagnostic at `ProviderMonitorSetting.tsp:42:3` states:

> The PATCH operation must have a request body.

[Frozen source](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/providerhub/resource-manager/Microsoft.ProviderHub/ProviderHub/ProviderMonitorSetting.tsp#L31-L45):

```typespec
create is ArmResourceCreateOrReplaceAsync<ProviderMonitorSetting>;

@patch(#{ implicitOptionality: false })
update is Azure.ResourceManager.Legacy.CustomPatchSync<
  ProviderMonitorSetting,
  PatchModel = void
>;
```

The actual source intentionally selects a bodyless legacy template. Both
predicates' missing-PATCH checks are covered by semantic evidence, but the
original Swagger linter did not execute for this service in the production baseline.
The subsequent staging inventory records its actual emitted-side observation.
Disposition: retain the TypeSpec observation; do not silently suppress it or
count it as a measured cross-engine match.

## Historical property names: Managed Network Fabric

Project:
`specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric`.

The project reports 13 TypeSpec missing-name diagnostics. The complete receipt
retains all 13; the example below explains one concrete historical-name pattern,
not a blanket attribution of all 13.

The saved diagnostic for `primaryIpv6Prefix` targets
`models/NetworkFabric.tsp:403:3`. Compare the
[PUT declaration](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/NetworkFabric.tsp#L175-L205)
with the
[PATCH declaration](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/NetworkFabric.tsp#L385-L409):

```typespec
model TerminalServerConfiguration {
  // Other members omitted.
  @removed(Versions.v2024_06_15_preview)
  @renamedFrom(Versions.v2024_06_15_preview, "primaryIpv6Prefix")
  primaryIpv6PrefixDeprecated?: string;

  @added(Versions.v2024_06_15_preview)
  primaryIpv6Prefix?: string;
}

model TerminalServerPatchConfiguration {
  // Other members omitted.
  primaryIpv6Prefix?: string;
}
```

Before that boundary the intended historical PUT wire name is
`primaryIpv6Prefix`; the paired helper instead uses current property identity
while filtering availability. The
[executed historical rename control](semantic-evidence.md#historical-renamed-and-type-shape-properties)
isolates this failure to reconstruct historical names. This is different from
the name-only comparison accepting incompatible scalar types.

The same project also contains deprecated/renamed PATCH members such as
[`connectedIPv4SubnetsDeprecated`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/ManagedNetworkFabric/models/InternalNetwork.tsp#L310-L338).
Their exact diagnostic targets remain in the inventory. No per-finding
projected-schema replay was performed, so no complete 13-finding false-positive
classification or Swagger correspondence is claimed.

Disposition: preserve the findings and source-history limitation; do not treat
all-source corpus diagnostics as an emitted-version parity result.
The migration owner accepts demonstrated historical-shape false positives
temporarily for PR #5481, deferring their correction to the shared
[version-aware linting issue #5875](https://github.com/Azure/typespec-azure/issues/5875).
This does not classify all 13 findings as false positives or alter their counts.

## Writable source metadata: Automation

Project:
`specification/automation/resource-manager/Microsoft.Automation/Automation`.

The project reports nine TypeSpec missing-name diagnostics. Observed names
include `createdBy`, `createdByType`, and `createdAt` at `models.tsp:5200:3`.
The diagnostic target is the containing model property, not necessarily a
separately authored leaf declaration at that location.

[Frozen PATCH model](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/models.tsp#L5187-L5201):

```typespec
model RuntimeEnvironmentUpdateParameters {
  properties?: RuntimeEnvironmentUpdateProperties;
  systemData?: SystemData;
}
```

[Frozen operations](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/automation/resource-manager/Microsoft.Automation/Automation/RuntimeEnvironment.tsp#L30-L54)
pair standard `ArmResourceCreateOrReplaceSync<RuntimeEnvironment>` with
`ArmCustomPatchSync<RuntimeEnvironment, PatchModel = RuntimeEnvironmentUpdateParameters>`.

This illustrates why an exact source target can own multiple distinct leaf-name
findings and why counting lines is not counting diagnostics. The full receipt,
not this excerpt, accounts for all nine. Emission, other visibility rules, and
the disabled Swagger linter were not independently replayed for this service.

Disposition: retain the observed source-rule findings without inferring an
actual Swagger count or classifying all nine as valid/invalid.
