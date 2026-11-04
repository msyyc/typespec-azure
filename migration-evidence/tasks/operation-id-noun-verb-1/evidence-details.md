# OperationIdNounVerb supporting evidence

This is unpublished final-review evidence. The full 487-project run is complete.
Retained final local acceptance, native publication, asset round trips and
independent published recovery remain separate gates. Early source review does
not certify this appendix.

## Difference summary

Only six projects have different raw counts:

| Project                                                                                   | Swagger / TypeSpec raw | Swagger exact file-independent keys / TypeSpec source keys | Cause / grouped evidence                               |
| ----------------------------------------------------------------------------------------- | ---------------------- | ---------------------------------------------------------- | ------------------------------------------------------ |
| [Billing](#gap-example-method-casing-introduced-by-serialization)                         | 5 / 4                  | 5 / 4                                                      | Common versus serialized casing                        |
| [DesktopVirtualization](#gap-example-explicit-operation-id-hides-a-common-sdk-repetition) | 0 / 1                  | 0 / 1                                                      | Explicit operation ID hides repetition                 |
| [FileShares](#same-cause-fileshares-explicit-operation-ids)                               | 0 / 4                  | 0 / 4                                                      | Four explicit operation IDs hide repetitions           |
| [Network](#network-reference-and-attribution-evidence)                                    | 154 / 11               | 11 / 11                                                    | Repeated observations; callback attribution incomplete |
| [Network/Vmss](#gap-example-autorest-only-operation-group-relocation)                     | 5 / 3                  | 5 / 3                                                      | AutoRest-only group relocation                         |
| [Resources](#gap-example-resources-casing-and-explicit-route-bridges)                     | 4 / 3                  | 4 / 3                                                      | Common versus serialized casing                        |

The location-key columns use different identities; they are not normalized
actionable counts. [Complete grouped targets](grouped-targets.md) show both
linters' counts for every target in these projects, including matching groups
needed to account for each project's total. [Machine-readable groups](difference-groups.json)
retain exact route/verb/source identities and the two explicit Resources bridges.
All six groups have the disposition **no TypeSpec rule update required for the
approved common-SDK contract**, not serialized-ID equivalence.

Across all 487 assessable projects, Swagger/TypeSpec raw findings are 265/123.
Swagger excess is 147, TypeSpec excess is 5, and absolute difference is 152.
The signed TypeSpec-minus-Swagger difference is -142; opposite gaps do not cancel
in the directional accounting. Six projects differ and 481 have equal raw counts.
[counts.json](counts.json) retains signed (`rawDifference` uses Swagger minus
TypeSpec), absolute and relative differences for every project.

## Policy and comparison boundaries

- Swagger linter: [OperationIdNounVerb implementation](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/packages/rulesets/src/spectral/functions/operation-id-noun-verb.ts).
  It reads underscore-separated serialized operation-ID segments and uses a dynamic
  regular expression, with an optional terminal `s`. The pinned upstream source
  was inspected; this is not a claim that the newer upstream source was executed.
- TypeSpec linter:
  `@azure-tools/typespec-client-generator-core/no-redundant-operation-group-name`.
  It reads the actual immediate common SDK owning subclient and common method name.
  It compares literal text, case-sensitively, after removing one terminal lowercase
  `s` from the group. Root clients and unowned operations are exempt.
- The frozen comparison assesses ARM source programs against saved latest-version
  Swagger. It does not project TypeSpec to that API version or assess a real
  data-plane corpus. Data-plane standard-template tests are separate evidence.
- The analyzer explicitly activates only the mapped rule, preserves authored
  suppressions and target options, and overrides configuration disablement.
  Corpus default activation is not assessed; installed controls verify it separately.
- Historical `coverage_old.md` and `coverage-breakdown.md` reconciliation is not
  applicable. Neither historical report underpins this fresh artifact comparison.
  The compared reports are the pinned saved member shard and this run's fresh
  `coverage.json`, with their identities retained in `inputs.json`.

## Gap example: method casing introduced by serialization

- **Classification:** count-only.
- **Status:** intentional common-SDK naming boundary.
- **Project/API version:** `specification/billing/resource-manager/Microsoft.Billing/Billing` / `2024-04-01`.
- **Source:** [`Invoice.tsp`](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/billing/resource-manager/Microsoft.Billing/Billing/Invoice.tsp#L240)
  and [`back-compatible.tsp`](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/billing/resource-manager/Microsoft.Billing/Billing/back-compatible.tsp#L473).

```typespec
@action("transactionsDownload")
transactionsDownloadByInvoice is InvoiceOps.ActionAsync<
  Invoice,
  void,
  DocumentDownloadResult
>;
```

```typespec
@@clientLocation(Invoices.transactionsDownloadByInvoice, "Transactions");
```

The saved POST operation at
`/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoices/{invoiceName}/transactionsDownload`
contains:

```json
{ "operationId": "Transactions_TransactionsDownloadByInvoice" }
```

| Engine          | Observed result                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------- |
| Swagger linter  | One finding: serialized `TransactionsDownloadByInvoice` contains `Transaction`.                                     |
| TypeSpec linter | No finding on this operation: common `transactionsDownloadByInvoice` does not contain case-sensitive `Transaction`. |

**Explanation:** serialization changes the first character's case. The production
TypeSpec rule intentionally does not reconstruct that casing. Its close
case-sensitive compliant controls cover this boundary.

**Disposition:** no TypeSpec rule update required for the approved common-SDK
contract. This is not exact serialized-ID equivalence.

## Gap example: explicit operation ID hides a common SDK repetition

- **Classification:** TypeSpec-linter-only.
- **Status:** intentional common-SDK naming boundary.
- **Project/API version:** `specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization` / `2026-04-01-preview`.
- **Source:** [`SessionHost.tsp`](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization/SessionHost.tsp#L125).

```typespec
@operationId("SessionHosts_ListSingleRegistrationTokens")
@added(Versions.vLatestPreview)
listSingleSessionHostRegistrationTokens is ArmResourceActionSync<
  SessionHost,
  ScopedRegistrationTokenProperties,
  RegistrationTokenList
>;
```

The saved POST operation at
`/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools/{hostPoolName}/sessionHosts/{sessionHostName}/listSingleSessionHostRegistrationTokens`
contains:

```json
{ "operationId": "SessionHosts_ListSingleRegistrationTokens" }
```

| Engine          | Observed result                                                                                               |
| --------------- | ------------------------------------------------------------------------------------------------------------- |
| Swagger linter  | No target finding: explicit `ListSingleRegistrationTokens` does not repeat `SessionHost`.                     |
| TypeSpec linter | One finding at `SessionHost.tsp:128:3`: the common SDK method contains its owning group's `SessionHost` noun. |

**Explanation:** the explicit serialized ID removes text that remains in the
common SDK method. The operation exists in the saved selected API version, so
this example is not explained by an absent version or an unassessed compilation.

**Disposition:** no TypeSpec rule update required for the approved common-SDK
contract. The native tests also prove independence from explicit operation IDs.

### Same cause: FileShares explicit operation IDs

The selected FileShares API version is `2026-06-01`. The exact saved operations
and source overrides establish the same difference, not a missing version:

| Authored common method            | Explicit saved operation ID        | Swagger / TypeSpec findings |
| --------------------------------- | ---------------------------------- | --------------------------- |
| `getFileShareSnapshot`            | `FileShareSnapshot_Get`            | 0 / 1                       |
| `createOrUpdateFileShareSnapshot` | `FileShareSnapshot_CreateOrUpdate` | 0 / 1                       |
| `updateFileShareSnapshot`         | `FileShareSnapshot_Update`         | 0 / 1                       |
| `deleteFileShareSnapshot`         | `FileShareSnapshot_Delete`         | 0 / 1                       |

These are methods on the actual `FileShareSnapshots` interface in
[`fileshares.tsp:344-380`](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/fileshares/resource-manager/Microsoft.FileShares/FileShares/fileshares.tsp#L344).
The following exact source fragment shows the mechanism:

```typespec
@armResourceOperations
interface FileShareSnapshots {
  @operationId("FileShareSnapshot_Get")
  getFileShareSnapshot is ArmResourceRead<FileShareSnapshot, BaseParameters<FileShareSnapshot>>;
}
```

The saved GET on
`/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FileShares/fileShares/{resourceName}/fileShareSnapshots/{name}`
has `"operationId": "FileShareSnapshot_Get"`. PUT, PATCH and DELETE on that same
route carry the other three explicit IDs. The fifth, compliant list operation has
`FileShareSnapshot_List` and common method `listByFileShare`; neither linter reports it.

All four additional findings enforce the approved common-SDK contract.
**Disposition:** no TypeSpec rule update required; exact wire equivalence is not claimed.

## Gap example: AutoRest-only operation-group relocation

- **Classification:** count-only.
- **Status:** intentional common-SDK ownership boundary.
- **Project/API version:** `specification/network/resource-manager/Microsoft.Network/Network/Vmss` / `2018-10-01`.
- **Source:** [`routes.tsp`](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/network/resource-manager/Microsoft.Network/Network/Vmss/routes.tsp#L42)
  and [`back-compatible.tsp:118-128`](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/network/resource-manager/Microsoft.Network/Network/Vmss/back-compatible.tsp#L118).

```typespec
interface NetworkInterfacesOperationGroup {}
```

Its authored method is `listVirtualMachineScaleSetNetworkInterfaces`. The source
relocates it only for the AutoRest emitter:

```typespec
@@clientLocation(
  Microsoft.Compute.NetworkInterfacesOperationGroup.listVirtualMachineScaleSetNetworkInterfaces,
  Microsoft.Compute.NetworkInterfaces,
  "autorest"
);
```

The saved GET on
`/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/networkInterfaces`
has:

```json
{ "operationId": "NetworkInterfaces_ListVirtualMachineScaleSetNetworkInterfaces" }
```

| Exact differing target                 | Swagger / TypeSpec findings | Cause                                                                                            |
| -------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------ |
| Scale-set-level network-interface list | 1 / 0                       | AutoRest group is `NetworkInterfaces`; common source group is `NetworkInterfacesOperationGroup`. |
| Scale-set-level public-IP-address list | 1 / 0                       | AutoRest group is `PublicIPAddresses`; common source group is `PublicIPAddressesOperationGroup`. |

The second method is `listVirtualMachineScaleSetPublicIPAddresses`, on
`PublicIPAddressesOperationGroup`, with the same `"autorest"`-scoped relocation.
Its exact saved GET route replaces the final `networkInterfaces` segment above
with `publicipaddresses` and carries
`PublicIPAddresses_ListVirtualMachineScaleSetPublicIPAddresses`.

The other three saved observations correspond to the virtual-machine-level
methods listed in the native receipt; both linters report those three.
Thus the project's 5 / 3 raw difference is not repeated-input multiplicity.
Source inspection, the scoped decorator, captured findings and the actual
common-owner metadata establish the boundary. The saved
[semantic metadata](semantic-operation-metadata.json) independently records both
`OperationGroup` owners and the three shorter common owners. This is not a trace
of the historical AutoRest emitter's internal execution.

**Disposition:** no TypeSpec rule update required. The common policy does not
apply AutoRest-only relocation or remove arbitrary `OperationGroup` suffixes.

## Network reference and attribution evidence

The saved Network shard has 154 individual occurrences at 11 distinct exact
JSON paths. The selected project has 19 Swagger files. Nine validator input
files produced these findings. Per-path repetition ranges from 9 to 15.

Eleven observations retain reported source documents. The other 143 have
`sourceAttribution: input-fallback` and empty `sourceDocuments`. Their
`swaggerFile` is the input fallback, not proof of the defining source document.
Exact JSON-pointer lookup across the 19 inventoried documents finds one candidate
definition for every target. This locates saved targets but does not restore
missing callback source attribution.

The deterministic extraction preserves all occurrences, per-input multiplicities,
11 candidate definitions and the actual cross-document `$ref` edges. Repeated
JSON paths are conservative location summaries, not independently established
actionable defects. No repeat is silently removed from the raw scorecard.

The completed TypeSpec run reports exactly 11 findings. Independent semantic
metadata captures one source operation for each exact path/verb target, with
zero HTTP metadata diagnostics. All 11 map to individual source diagnostics.
Per-target raw Swagger multiplicities are 10, 9 and nine groups of 15, versus
one TypeSpec finding each: `10 + 9 + 9 * 15 = 154`; excess is 143.
All 154 observations remain in the published member shard.

The 143 fallback observations and the raw excess happen to have the same total;
this is not proof that each excess occurrence has restored callback attribution.
The extraction retains nine input counts, the 19-file inventory, exact defining
candidates and reference edges. Actual callback provenance for those 143
observations remains unavailable.

### Gap example: repeated Network operation observations

- **Classification:** count-only.
- **Status:** explained saved-observation multiplicity; callback attribution remains limited.
- **Project/API version:** Network / `2026-03-01`.
- **Source:** [`VirtualHub.tsp:164-166`](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/network/resource-manager/Microsoft.Network/Network/Network/VirtualHub.tsp#L164).

```typespec
@action("effectiveRoutes")
@autoRoute
getEffectiveVirtualHubRoutes is ArmResourceActionAsync<
```

The exact saved POST target ends with
`/providers/Microsoft.Network/virtualHubs/{virtualHubName}/effectiveRoutes`.
Its unique exact-pointer definition in `virtualWan.json` contains:

```json
{ "operationId": "VirtualHubs_GetEffectiveVirtualHubRoutes" }
```

| Engine          | Observed result                                                                                          |
| --------------- | -------------------------------------------------------------------------------------------------------- |
| Swagger linter  | 10 retained observations at that exact operation-ID JSON path                                            |
| TypeSpec linter | One finding on `VirtualHub.tsp:166:3`, common owner `VirtualHubs`, method `getEffectiveVirtualHubRoutes` |

**Explanation:** repeated validator-input observations describe the same saved
route/verb target; source lint reports the authored operation once. The exact
semantic HTTP join independently identifies that source operation. This does
not establish a new full-corpus actionable identity or reconstruct callback
source attribution.

**Disposition:** no TypeSpec rule update required. Retain all raw observations,
the exact route/verb grouping and attribution limitation separately.

## Gap example: Resources casing and explicit route bridges

- **Classification:** count-only.
- **Status:** intentional common-SDK naming boundary; bridge spelling differences explained.
- **Project/API version:** Resources / `2025-04-01`.
- **Source:** [`routes.tsp:68-71`](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/resources/resource-manager/Microsoft.Resources/resources/routes.tsp#L68).

```typespec
@tag("Providers")
@route("/subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}/providerPermissions")
@get
providerPermissions(
```

The exact saved GET operation contains:

```json
{ "operationId": "Providers_ProviderPermissions" }
```

| Exact operation         | Swagger / TypeSpec findings | Evidence                                                                                     |
| ----------------------- | --------------------------- | -------------------------------------------------------------------------------------------- |
| `providerPermissions`   | 1 / 0                       | Actual owner `Providers`; lowercase common method does not contain case-sensitive `Provider` |
| `listByResourceGroup`   | 1 / 1                       | Exact route/verb and authored source-coordinate join                                         |
| `moveResources`         | 1 / 1                       | Explicit legacy parameter-rename bridge                                                      |
| `validateMoveResources` | 1 / 1                       | Explicit legacy parameter-rename bridge                                                      |
| **Total**               | **4 / 3**                   | Complete accounting                                                                          |

**Explanation:** serialized casing accounts for the one excess finding.
The two other route spelling differences do not represent missing findings.
Saved Swagger uses `{sourceResourceGroupName}`, while captured HTTP metadata
uses `{resourceGroupName}`. The source explicitly annotates each operation:

```typespec
@Azure.ResourceManager.Legacy.renamePathParameter(
  "resourceGroupName",
  "sourceResourceGroupName"
)
moveResources is ArmResourceActionAsync<
```

The same annotation precedes `validateMoveResources`. Both source coordinates,
the exact saved POST paths and each individual source diagnostic are retained in
[semantic-route-bridges.json](semantic-route-bridges.json). The original
[automatic correspondence](semantic-correspondence.json) remains unchanged,
including its unresolved automatic spellings. Only these two explicitly
annotated operations are bridged; no generic placeholder normalization is used.

**Disposition:** no TypeSpec rule update required. The group-name comparison is
common-SDK policy, not exact serialized-ID parity.

## Semantic conclusion and member coverage

The singleton mapping is `OperationIdNounVerb` to
`@azure-tools/typespec-client-generator-core/no-redundant-operation-group-name`.
The original policy audience is common ARM/data-plane SDK naming; this run
assesses only the frozen ARM corpus. All 487 projects compiled and were assessed;
no source/projection/worker failures were discarded.

| Material upstream behavior / native boundary                                   | Evidence and result                                                                                                                       |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Repeated noun after group / method separation, optional terminal lowercase `s` | Singular/plural violating fixtures and compliant `list` controls; covered through actual common SDK ownership                             |
| Case-sensitive matching                                                        | Close compliant controls plus Billing and Resources real-service examples                                                                 |
| One finding per operation-ID occurrence                                        | Native unit intentionally becomes one authored operation; repeated matches emit one warning                                               |
| Empty/nonstring/no-underscore serialized IDs                                   | Not a native input shape: the rule does not parse serialized IDs; root/unowned and empty-normalized-group exemptions have direct controls |
| Dynamic regex and underscore-segment interpretation                            | Intentionally replaced with literal full-name matching; punctuation and underscore controls discriminate the policies                     |
| Explicit IDs and language-specific names                                       | Comparison-only explicit-ID fixture and language-scoped override controls prove independence                                              |
| Actual group ownership and common name overrides                               | Interface/namespace, immediate owner, relocation, virtual group, inheritance, alias and friendly-name controls                            |
| ARM/data-plane authoring                                                       | Standard-template violating/compliant cases; real data-plane corpus remains unassessed                                                    |

No production rule or directly related fixture change is required by these
investigations. The approved common-SDK rule is supported; exact functional
equality with the serialized-ID Swagger rule is **not** claimed. The harness
correctly retains `equivalence: not-determined`; this manual conclusion does
not rewrite the immutable run.

The native test file contains the canonical behavior suite. Focused
rule/registration checks passed 29 cases; registration/ruleset tests separately
cover automatic library `all`, recommended disablement and preset wiring.
These fixture counts are not production prevalence or an exhaustive percentage.
See [claim mapping](claim-map.json) and [validation](validation.json).

## Validation and finite recovery

See [validation.json](validation.json) and its sanitized receipt views.
The current full TCGC run passed 1,888 tests with the same two skips across
109 files, using the authorized single-worker profile and unchanged timeouts.
The original four-timeout attempt is preserved; its cause remains **UNPROVEN**.
Rulesets tests passed 12 tests. Five exact published documentation controls,
five actual installed selected-rule controls and 37 applicable portable controls
passed. Six predeclared unrelated portable cases were excluded, not passed.

The 15-package artifact set preserves 14 original archives. Only TCGC was
repacked after validated runtime reconciliation. All 2,836 nonmanifest payload
files and independently resolved packed manifests were checked; the only three
authorized changed payloads match the current validated build exactly.
Installed resolution follows actual dependency owners and loader export
conditions; `manifest.main` is not used as a universal entrypoint.

Ordinary development corrections, coordinator reserve and the native timeout
diagnostic are exhausted. The separately authorized YAML, artifact and installed
helper corrections remain distinct, each used once. Historical failures were
preserved and did not reset task-wide counters.

The separately authorized saved-count/receipt correction passed once. It
preserved the four original total checks, checked directional totals using
`rawValidatorExcess` / `rawNativeExcess`, and bound the original completed-run
log at its verified native-root location. The failing JS, both failure receipts
and exact route-bridge bytes remain preserved locally; sanitized correction
provenance is in [count-audit.json](count-audit.json). No linter, build, install
or package operation was repeated for this correction.

## Recovery boundaries

`reanalyze.mjs` reproduces the prepared numerical results from compact saved
observations without dependencies. That count audit does not execute either
linter, restore a sealed baseline, regenerate Swagger or decide equivalence.

The local four-asset/member verification passed, retaining 15 candidate package
archives, 1,469 sanitized run members and 79,756 exact committed tooling files.
The large tooling member inventory is compressed in a separate asset, not Git.
See [local-replay.json](local-replay.json) for exact executed scopes and receipt
hashes. The one authorized asset-launch parser correction changed only
`$code:` to `${code}:`; offline whole-script parsing passed before invocation.
The original parser failure and all earlier failed receipts remain preserved.

Publication text uses UTF-8/LF with Git whitespace checks enabled.
[Publication normalization](publication-normalization.json) distinguishes
reading copies from exact executed inputs. All five original control-source
hashes were checked against the installed receipts; complete source/configuration
bytes remain recoverable from [control-source-originals.json](control-source-originals.json).
Raw receipts, immutable archives, the sealed baseline and the 13 native source
files were not changed.

Published-asset round trips and a fresh checkout of the published evidence commit
remain pending. A populated local worktree is not durable publication or proof of
independent recovery. Full coverage regeneration must recover the exact frozen
specs source, candidate artifacts, tooling identities and baseline, then rerun
controls, native diagnostics and semantic investigation. It must not regenerate
Swagger or infer a new conclusion from count equality.
