# Source-only PATCH/PUT correspondence

## Scope and review admission

The migration owner authorized removing rule-local version handling while
retaining effective source-program PATCH/PUT comparison. This is not deletion
of the paired-body checker or an assertion that resource identity makes
writable-input comparison redundant.

Report **01** admits [the simplification comment](https://github.com/Azure/typespec-azure/pull/5481#discussion_r4455090553),
created `2026-11-03T13:09:10Z`, against head
`60a56b11d149b5960783e0c18da675d6cceb902e` committed
`2026-11-03T08:28:23Z`. Its versioning-import location and the migration owner's
explicit source-only direction determine this cycle's scope; reviewer agreement
with the resulting implementation is not assumed. Older comments were excluded
from fix/reply targets. No thread resolution was changed.

## Implementation and behavioral boundary

Candidate `51cc68db6897b286b10ad6a23266e9c62a4f422d` removes
`resolveVersions`, `getAddedOnVersions`, `getRemovedOnVersions`, the hand-written
availability evaluator and body-at-version helper. Each HTTP service's resolved
source operations are grouped by path once, rather than separately per version.
Per-version missing/empty-body reporting sets are no longer necessary.
Per-source-target/property-name deduplication remains.

Nested and inherited JSON leaves, request visibility, encoded names, nullable
single-model handling, cycle protection, authored targets and unsupported-body
boundaries remain. Missing/empty PATCH and absent/void PUT behavior remain.
Rule identity, registration, activation and suppression behavior are unchanged.

This deliberately removes availability-sensitive coverage: a source property
can satisfy correspondence even if absent in a particular API version. Source
operations whose lifetimes do not overlap can also be compared. Renames/type
changes are not reconstructed. All these version-dependent false-negative and
false-positive risks belong to the shared work in
[#5875](https://github.com/Azure/typespec-azure/issues/5875), not a claim that
source-only evaluation fixes versioning.

## Claim-to-test mapping

The owning public rule retains its canonical `patch-operations.test.ts` suite
and shared tester setup; no private authoring APIs or new test harness is added.

| Claim                                                                           | Existing canonical regression                                                                                                    |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Source declarations, not each version's availability, determine comparison      | `compares source properties without applying historical availability`                                                            |
| Inherited/spread source members remain present despite removal decorators       | `compares source %s properties in nested namespaces`                                                                             |
| Dependency source properties are not projected to a selected dependency version | `compares dependency source models without applying selected dependency versions`                                                |
| Nonconcurrent operation/interface declarations can pair in source mode          | `pairs source %s declarations without historical availability filtering`                                                         |
| Explicit source body remains present despite version removal                    | `uses source explicit %s body parameters despite historical removal`                                                             |
| Added nested source models do not collapse into opaque wrapper properties       | `compares source nested types without filtering newly added models`                                                              |
| A shared-path source lookup does not select historical PATCH variants           | `uses the last resolved source PATCH at a shared path without historical selection`                                              |
| Effective input still differs despite shared resource identity                  | `compares effective input of a standard PUT with Create visibility (unrelated property: %s)`                                     |
| Inheritance correction remains intact                                           | `finds inherited writable PUT leaves behind read-only direct members`; `reports genuinely missing inherited nested PATCH leaves` |

These are intentional changes to the proposed versioning architecture, not
claims of preserving each historical-version check. The documented TypeSpec
source-presence policy is retained; bug-for-bug Swagger parity is not required.

## Local validation

Executed from the candidate's existing checkout:

```powershell
# packages\typespec-azure-resource-manager
pnpm exec vitest run test\rules\patch-operations.test.ts --reporter=dot --maxWorkers=1
pnpm run build
pnpm run lint

# packages\samples
pnpm exec vitest run test\samples.test.ts --reporter=dot --maxWorkers=1

# Repository root
pnpm exec chronus verify
pnpm exec prettier --check packages\typespec-azure-resource-manager\src\rules\arm-resource-patch-body.ts packages\typespec-azure-resource-manager\test\rules\patch-operations.test.ts packages\typespec-azure-resource-manager\src\rules\arm-resource-patch.md .chronus\changes\arm-resource-patch-input-consistency.md
pnpm -r --filter '@azure-tools/typespec-autorest...' --filter '@azure-tools/typespec-azure-rulesets...' --filter '@typespec/integration-tester...' build
git diff --check
```

All **61 focused rule tests**, **40 sample tests**, builds, ARM lint, formatting,
Chronus and whitespace checks passed. Independent read-only source review found
no significant issues. The adequate existing feature entry was updated; no
extra review-history changeset was created.

The final closure contains the same 15 public packages and unchanged core
gitlink as the preceding candidate. New tarballs, build logs, artifact hashes,
installed-runtime provenance and the full comparison are retained separately in
`refresh-20261104`. Original and preceding receipts are not overwritten.

## Corpus differences

The [complete fresh comparison](refresh-20261104/staging-comparison/differences.md)
retains all differing projects, including unchanged gaps. The
[exact source-record delta](refresh-20261104/candidate-delta.json) records
**18 removals and 0 additions**. Every changed source target is listed below;
all other project multisets are unchanged.

**Coverage:** source-level presence remains checked, but individual API-version
membership, names, nested types and operation selection are missing. The
migration owner explicitly authorized this narrower scope; that does not make
the missing functionality implemented or establish full equivalence.

**Recommended action and rationale:** retain the simplified comparison and
defer version-aware evaluation to shared #5875 rather than restore a bespoke
availability/history implementation in this rule. Historical coverage has value,
but partial per-rule reconstruction also produced the wrapper/name noise below
and increases maintenance. The missing coverage remains visible; the removed
warnings are not all corrections, and no new source fix is recommended merely
to restore their count.

| Project                | Swagger, unchanged | TypeSpec before / after | Removed properties and source lines                                                                                                                                                                                                                                                                                                                                                             | Disposition                                                                                                                                                                                                                                                                                    |
| ---------------------- | -----------------: | ----------------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AppLink                |                  3 |                   2 / 0 | `metadata` (`applinkmember.tsp:29`), `privateConnect` (`:118`)                                                                                                                                                                                                                                                                                                                                  | Intended source-path selection change. The later custom PATCH omits both; the preceding checker also visited the older PATCH. Not proof that all historical inputs are valid.                                                                                                                  |
| CodeSigning            |                  1 |                   1 / 0 | `sku` (`models.tsp:162`)                                                                                                                                                                                                                                                                                                                                                                        | Intended removal of availability-filtered opaque-wrapper warning. The source `AccountSkuPatch` has matching `name`; the old check hid its children before the model's addition without restoring the previous type.                                                                            |
| DeviceRegistry         |                 18 |                   2 / 1 | `certificateAuthorityConfiguration` (`ns_policy.tsp:66`)                                                                                                                                                                                                                                                                                                                                        | Intended source-only nested-shape change. Added `bringYourOwnRoot` gives a source child on both sides; old availability filtering could leave a wrapper on PATCH but PUT's `keyType` leaf. The remaining project finding is preserved.                                                         |
| Discovery              |                 10 |                   2 / 1 | `properties` (`../Discovery.Workspace.Management/ChatModelDeployments.tsp:63`)                                                                                                                                                                                                                                                                                                                  | Intended source-only change. The shared properties type gains Update-visible `capacity`; before its addition PATCH has no writable child and becomes an opaque wrapper while PUT has Create-visible leaves. No claim of historical correctness.                                                |
| DNS Resolver           |                 12 |                   1 / 0 | `dnsResolverDomainLists` (`models.tsp:612`)                                                                                                                                                                                                                                                                                                                                                     | Intended loss of availability-sensitive membership checking: PUT's source member is added later than the PATCH member. Source presence now passes without evaluating earlier versions.                                                                                                         |
| KeyVault               |                  9 |                   1 / 0 | `enableRbacAuthorization` (`models.tsp:1463`)                                                                                                                                                                                                                                                                                                                                                   | Same availability-sensitive boundary: PUT's member has `@added(v2026_02_01)`, PATCH's has no corresponding addition. No longer checked version by version.                                                                                                                                     |
| Managed Network Fabric |                 93 |                 13 / 12 | `primaryIpv6Prefix` (`models/NetworkFabric.tsp:403`)                                                                                                                                                                                                                                                                                                                                            | Demonstrated historical-name warning disappears because the newer source member is always available to comparison, not because `@renamedFrom` is reconstructed. The other 12 findings remain.                                                                                                  |
| ManagedOps             |                  2 |                   2 / 0 | `defenderForServers`, `defenderCspm` (`managedOps.tsp:348`, `:352`)                                                                                                                                                                                                                                                                                                                             | Source contains the newer matching names; the former availability walk selected old declarations with current `oldDefender...` names without historical rename application. Intended removal of those warnings.                                                                                |
| NetworkCloud           |                 34 |                   8 / 0 | `aggregatorOrSingleRackDefinition`, `clusterServicePrincipal`, `computeDeploymentThreshold`, `runtimeProtectionConfiguration`, `secretArchive`, `updateStrategy` (`clusters/Cluster_models.tsp:1580`, `:1596`, `:1607`, `:1620`, `:1626`, `:1637`); `vmImageRepositoryCredentials` (`virtualmachines/VirtualMachine_models.tsp:439`); `sshPublicKey` (`virtualmachines/Console_models.tsp:182`) | All eight PATCH nested types are added at `v2026_07_01` and paired with `@typeChangedFrom`. Source traversal sees their current matching leaves instead of filtering all children and comparing wrapper names in older versions. Intended source-only changes, not full historical validation. |

These are accepted consequences of the migration owner's explicit source-only
direction. In particular, availability-sensitive losses are not mislabeled as
false positives repaired. Removing version handling can cause additional
warnings too (the nonconcurrent-operation control proves that possibility);
this frozen corpus has **no newly added findings**.

### Example: availability-sensitive membership is no longer enforced

The pinned [KeyVault source](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/models.tsp#L1122-L1126)
and [PATCH declaration](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/models.tsp#L1460-L1463)
contain:

```typespec
// PUT: VaultProperties
@Versioning.added(KeyVault.Versions.v2026_02_01)
enableRbacAuthorization?: boolean = true;

// PATCH: VaultPatchProperties
enableRbacAuthorization?: boolean;
```

The old checker could report a mismatch in versions preceding the PUT member's
addition. The source-only checker sees both names and no longer reports it.
This intentionally narrows version-specific enforcement. The unchanged nine
Swagger project findings are schema inequalities; no common per-operation
pairing with this removed source warning is established.
The canonical source-availability test distinguishes the old/new policy.

### Example: partial version evaluation produced an opaque nested wrapper

The pinned [CodeSigning declarations](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/codesigning/resource-manager/Microsoft.CodeSigning/CodeSigning/models.tsp#L143-L169)
contain:

```typespec
model AccountSku {
  name: SkuName;
}
model CodeSigningAccountPatchProperties {
  @typeChangedFrom(Versions.v2024_09_30_preview, AccountSku)
  sku?: AccountSkuPatch;
}
@added(Versions.v2024_09_30_preview)
model AccountSkuPatch {
  name?: SkuName;
}
```

The preceding checker filters the current nested model's children out before
its addition, but does not restore `AccountSku` from `@typeChangedFrom`.
It then compares opaque PATCH `sku` against PUT leaf `name`. Source-only
traversal compares `name` with `name` and is silent. The retained Swagger
project count remains one schema-inequality finding. This is not a new
Swagger run or proof that all historical shapes were repaired.
The extracted test `compares source nested types without filtering newly added models`
protects the new behavior; NetworkCloud shares this mechanism.
The existing historical-rename example on #5875 explains the separate
Managed Network Fabric/ManagedOps name mechanism.

### Example: same-path historical operation selection is removed

The pinned [AppLink operations](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/applink/AppLink.Management/applinkmember.tsp#L220-L253)
contain an earlier `updateLegacy` and a later `update`, both `@sharedRoute` PATCH:

```typespec
@removed(Versions.v2026_08_01_preview)
@renamedFrom(Versions.v2026_08_01_preview, "update")
@sharedRoute
// Other LRO decorators/arguments omitted.
updateLegacy is ArmResourcePatchAsync<AppLinkMember, AppLinkMemberProperties>;

@added(Versions.v2026_08_01_preview)
@sharedRoute
// Other LRO decorators/arguments omitted.
update is ArmCustomPatchAsync<AppLinkMember, AppLinkMemberUpdate>;
```

The later source PATCH replaces the earlier entry in the per-path lookup.
Its update body excludes `metadata` and `privateConnect`; the preceding
version loop also evaluated the legacy body. Both prior source warnings
disappear; Swagger's three project findings remain schema inequalities.
The extracted `uses the last resolved source PATCH at a shared path without historical selection`
test records this limitation. A source-order choice is not a latest-version
projection or a guarantee of checking every historical operation.

## Final validation and comparison

The final production candidate passed **487/487 projects with no failures**:
**94 findings across 33 projects**, comprising 92 missing-property findings,
one empty PATCH and one missing PATCH. There are 94 distinct full records and
84 distinct source positions. BillingTrust remains **0 Swagger / 1 TypeSpec**;
its source request-visibility policy is unchanged.

The immutable Swagger staging observations remain **1,314 findings across
335 projects**. There are 32 overlapping projects, 303 Swagger-only and one
TypeSpec-only. The net gap grows **1,202 to 1,220**; absolute per-project gap
grows **1,204 to 1,222**. These different diagnostic units do not measure
matched defects or prove equivalence. The narrower source-only policy does not provide full functional equivalence;
historical coverage is missing and other correspondence remains unassessed.

The subsequent report-only
[annotation assessment](gap-investigation.md#assessed-diagnostic-records)
excludes 336 description/title-only Swagger overchecks, retaining 978 / 94
diagnostic records. It changes neither these raw execution totals nor the
18-removal source-code delta and does not establish matched defect counts.

Fourteen actual registered-linter controls passed. The portable harness passed
37 cases; six fixtures requiring an unrelated absent resource-group rule were
explicitly excluded, not counted as passes. Built, packed and installed selected
JavaScript matched. Independent Python and native-harness aggregation agree on
every project and summary field.

Two corpus-derived tests were added afterward, yielding 61 passing focused
tests. Final source head is `4f62f17ff8a4d3afcbc7fd548112c5fb42402464`;
only test source differs from the corpus-tested production revision
`51cc68db6897b286b10ad6a23266e9c62a4f422d`. No new corpus run is required
for those test-only additions.

## Recovery

Recover the same immutable parent and staging supplement as described in
[the original replay instructions](replay.md). Saved-data replay from this task
directory uses:

```powershell
python -B .\refresh-20261104\compare-staging.py `
  .\refresh-20261104\runs\full-corpus $recoveredSupplement $newEmptyComparison
python -B .\refresh-20261104\reanalyze-schema.py
```

The schema replay is reused only after proving the affected union is exactly
the same 336 projects whose 497 Swagger inputs were previously investigated.
Current TypeSpec counts are joined by exact project identity; no source/schema
diagnostic matching is inferred. Comparison and artifact provenance identify
the actual tested revision and preserved package closure.

For fresh execution, use the existing replay command with this candidate,
`refresh-20261104/artifacts/packages`, the exact selected supplement, a new empty
output directory, and source/target-only/frozen-reference, no filter/limit,
concurrency 2 and the recorded 10,800-second native budget. Acquire the shared
machine-wide corpus gate before artifact injection or running any workers.
Reading downloaded receipts and replaying comparison are not fresh native
execution or fully transitive locked regeneration.
