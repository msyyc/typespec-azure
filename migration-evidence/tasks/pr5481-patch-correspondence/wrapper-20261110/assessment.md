# Opaque-container coverage and current correspondence

The assessed source is
[`ade5040b62c25c8cd4eb8a0e99593f5f739c23f2`](https://github.com/Azure/typespec-azure/commit/ade5040b62c25c8cd4eb8a0e99593f5f739c23f2).
The fresh 487-project evaluation reports **108 warnings, 9 removed and 0 added**
against the preceding candidate on identical frozen specs. All projects succeeded.
This supports the diagnostic-driven current-source conclusion in
[migration.md](../migration.md), not exhaustive cross-version equivalence.

## Opaque object containers

**Coverage: Covered.** A writable object can have no Update-visible children
while still existing in both request bodies. Previously, PUT's collector could
flatten that object into Create-visible children, leaving no container candidate
for PATCH's opaque object and causing a false missing-property warning.

This executed, unversioned control reproduces the relevant shape
([full source and result](../refresh-20261110-wrapper/controls/injected-controls.json),
`opaque-matching-container`):

```typespec
model Properties {
  @visibility(Lifecycle.Read, Lifecycle.Create)
  value?: string;
}
model PutBody {
  properties?: Properties;
  tags?: string;
}
model PatchBody {
  properties?: Properties;
  tags?: string;
}
```

The PUT has a Create-visible `properties.value`; PATCH has no Update-visible
child inside `properties`. The container itself is valid input in both.
The current check emits **0 warnings**, without using version decorators.

The production change records encoded JSON path segments and resolves only
nonrecursive opaque object leaves against the actual PUT body at that finite
path. It preserves inherited/nullable models, encoded names, request visibility,
explicit-body metadata policy and compatibility. Missing/read-only/wrong-position
containers still warn; a compatible object elsewhere does not hide an incompatible
correct-position property. Finite path traversal also handles recursive PUT
ancestors. Ordinary leaves retain the existing global encoded-leaf-name policy.

| Packaged control                                                     | Configured warnings |
| -------------------------------------------------------------------- | ------------------: |
| Matching container                                                   |                   0 |
| Absent container                                                     |                   1 |
| Read-only container                                                  |                   1 |
| Same name at the wrong position                                      |                   1 |
| Incompatible correct-position container, compatible object elsewhere |                   1 |
| Matching finite path through recursive PUT ancestors                 |                   0 |

Nine canonical regression cases cover these distinctions and inherited,
nullable, encoded, dotted-name and read-only-ancestor behavior. The final
**98 rule tests**, owning ARM build/lint, changed-file formatting, Chronus and
whitespace checks passed. All **31 injected controls**, **37 applicable portable
controls** and **16 extraction controls** passed. Six portable cases requiring
the unrelated unmerged `resource-group-path-parameter` rule were excluded,
not counted as passes. See [injected receipts](../refresh-20261110-wrapper/controls/injected-controls.json),
[portable results](../refresh-20261110-wrapper/provenance/portable-applicable-controls.log)
and [extraction results](../refresh-20261110-wrapper/source-attribution/controls/summary.json).

## Actual full-corpus effect

The [exact diagnostic multiset delta](../refresh-20261110-wrapper/candidate-delta.json)
preserves every occurrence, including distinct findings at the same location.
The fix removes these **9 warnings across 8 projects**, not just the previously
identified seven outside-join warnings:

| Project              | Former target                | Source location                    |
| -------------------- | ---------------------------- | ---------------------------------- |
| ContainerApps        | `networking`                 | `models.tsp:7037:3`                |
| ContainerApps        | `vnetConfiguration`          | `models.tsp:2711:3`                |
| ContainerStorage     | `elasticSan`                 | `pool.tsp:106:3`                   |
| DatabaseFleetManager | `properties`                 | `models.tsp:340:3`                 |
| DeviceRegistry       | `bringYourOwnRoot`           | `ns_policy.tsp:94:3`               |
| Discovery            | `properties`                 | `storageContainer.tsp:114:3`       |
| GitHubNetwork        | `properties`                 | `NetworkSettingsResource.tsp:37:3` |
| SQL                  | `properties`                 | `models.tsp:11853:3`               |
| AppService           | `containerAppsConfiguration` | `models.tsp:6560:3`                |

The original seven have [pinned source excerpts and version-free controls](../count-gap-20261106/analysis.md#empty-wrapper-overcheck-to-fix).
The two additional removals belonged to retained absent-name records, so their
current dispositions change to accepted containers; they cannot simply be
subtracted from the old outside-join count.

### Additional retained container contexts

**ContainerStorage `Pools_Update/elasticSan`:** the
[pinned source](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/containerstorage/resource-manager/Microsoft.ContainerStorage/ContainerStorage/pool.tsp#L99-L145)
contains, omitting documentation:

```typespec
model PoolType {
  azureDisk?: AzureDisk;
  elasticSan?: ElasticSan;
  ephemeralDisk?: EphemeralDisk;
}
model ProvisionedPoolProperties<SkuType> {
  @visibility(Lifecycle.Read)
  resourceGroup?: string;

  @visibility(Lifecycle.Read, Lifecycle.Create)
  skuName?: SkuType;

  @visibility(Lifecycle.Read, Lifecycle.Create)
  encryption?: Encryption;
}
```

[`ElasticSan`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/containerstorage/resource-manager/Microsoft.ContainerStorage/ContainerStorage/pool.tsp#L198-L201)
spreads `ProvisionedPoolProperties<ElasticSanSkuName>`.
Its children have no Update visibility. The
[current source capture](../refresh-20261110-wrapper/source-attribution/source-14.json)
proves that PATCH and PUT both use `Microsoft.ContainerStorage.ElasticSan` at
**`properties / poolType / elasticSan`**, with a compatible candidate and no
configured warning. This is retained Swagger record index 1.

**Discovery `StorageContainers_Update/properties`:** the
[pinned source](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/discovery/Discovery.Management/storageContainer.tsp#L97-L108)
contains, omitting documentation and the model's availability decorator:

```typespec
model StorageContainerProperties {
  @visibility(Lifecycle.Read)
  provisioningState?: ProvisioningState;

  @visibility(Lifecycle.Read, Lifecycle.Create)
  storageStore: StorageStore;
}
```

The [current source capture](../refresh-20261110-wrapper/source-attribution/source-19.json)
proves that both bodies have `Microsoft.Discovery.StorageContainerProperties`
at **`properties`**, with a compatible candidate and no warning. This is retained
Swagger record index 2. Although the service is versioned, this current-source
container/visibility mechanism is not solely a #5875 gap.

The third changed retained predicate context is **EdgeActions record 0**:
it remains accepted. Its PUT candidate's diagnostic-target metadata now points
to the actual library property rather than the operation fallback; property
identity, type, compatibility, suppression and configured result are unchanged.
All **81 previously reviewed accepted schema predicates** are unchanged after
the documented warning-index/path-tracing/store-prefix canonicalization.
The [reconciliation](reconciliation.json) retains all three before/after contexts.

**Gap analysis and decision:** preserve the correct-position container check
and its negative controls. These are valid current-source objects, not a reason
to weaken visibility, suppress genuine incompatible values or reconstruct
historical types. The assessed container behavior is covered.

## Record-to-warning bridge

The immutable Swagger assessment still excludes **1,132** confirmed overchecks
from **1,314** raw records. Every one of the remaining **182 records** is
re-inspected using the installed final candidate.

| Retained family             | Records | Current-source disposition                             | Distinct configured witnesses |
| --------------------------- | ------: | ------------------------------------------------------ | ----------------------------: |
| Same-name schema inequality |     131 | 42 reporting, 81 compatible, 6 non-input, 2 mixed-name |                            34 |
| Absent emitted leaf name    |      49 | 44 reporting, 3 accepted containers, 2 non-leaf        |                            42 |
| Missing PATCH body          |       2 | 1 reporting, 1 suppressed                              |                             1 |

The **90 check-covered records** contain **89 reporting records and 1
suppression**. Another **92 records** are accepted/non-input. Reporting records
have **91 associations to 77 distinct configured warnings**: two records each
witness two prefix-limit checks, while reused warnings create 14 associations
across records. These are source-check incidences, not normalized defects.

**182 - 108 = 92 + 1 + 14 - 2 - 31 = 74.**

The [tested checker](reconcile.py) independently sums every project. Retained
record directional excesses are **94 Swagger-higher and 20 TypeSpec-higher**,
absolute **114**, net **74**. Raw full-population excesses remain **1,208
Swagger-higher / 2 TypeSpec-higher**, absolute **1,210**, net **1,206**.
The [raw comparison](../refresh-20261110-wrapper/staging-comparison/summary.json)
retains 331 Swagger-higher, 2 TypeSpec-higher and 154 equal-count projects;
opposite directions are never cancelled to claim parity.

The [route index](retained-route-contexts.md) groups all 182 records into
**97 project + exact PATCH-route inspections**. All 97 have source contexts,
but equal inspection counts are not equal defect counts. All 51 captured
diagnostic arrays match their full-run arrays exactly, including order.
The **98 distinct source positions** are a conservative location summary,
not a replacement for the **108 diagnostic occurrences**.

## Remaining configured warnings

The **31 warnings outside the retained-record join** are remapped from the
previous reviewed classification by **project + complete diagnostic record**,
preserving duplicate occurrences and rejecting new or ambiguous matches.
No stale warning-index matching or fuzzy name matching is used.

| Current warning group                               | Warnings | Coverage and decision                                                                                                                                                                    |
| --------------------------------------------------- | -------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Historical names/availability                       |       13 | Deferred to #5875; retain the [verified historical examples](../count-gap-20261106/analysis.md#historical-versioning).                                                                   |
| Writable PATCH inputs absent from PUT request input |       17 | Valid checks; retain [visibility/input-membership enforcement](../count-gap-20261106/analysis.md#valid-source-checks-to-retain), request spec-owner correction or contract confirmation. |
| Empty PATCH body                                    |        1 | Valid check; retain NetApp empty-body detection and request a model/API-owner correction.                                                                                                |

The [current inventory](reconciliation.json) records each current warning,
old index, source evidence and decision. It proves that exactly seven former
outside-join overchecks disappeared; the complete candidate delta additionally
contains the two reviewed retained-context removals. No new warning was added.
There is no observed non-versioning rule gap left in these groups. This does
not fix the two synthetic-only body-policy gaps or establish historical
cross-engine violation identity.

## Execution, closure and recovery limits

The [task metadata](../refresh-20261110-wrapper/task.json),
[artifact provenance](../refresh-20261110-wrapper/provenance/artifact-provenance.json)
and [closure delta](../refresh-20261110-wrapper/closure-delta.json) bind the
final source, frozen specs/core, all 15 archives and installed entrypoints.
The only changed executable archive member is `arm-resource-patch-body.js`;
other changes are its maps and formatting-only package manifests whose parsed
JSON is unchanged. ARM library members, compatibility/model utilities and
the existing body-policy owner modules remain unchanged.

Native execution ran **2026-11-10 06:35:13.591-07:03:25.884 UTC** within
the original 10,800-second budget. All 487 projects succeeded. The CLI then
exited **-1** after writing every receipt and coverage report, before sealing
its manifest. The exact Node executable was observed missing afterward;
neither its disappearance nor the process-exit cause is established.

Independent checks subsequently verified **all 93,496 dataset-file hashes**,
exact path-set equality, source/core/spec snapshots, artifacts, immutable
baseline/supplement identities and exact reconstruction of every original
official report field. The [strict recovery receipt](../refresh-20261110-wrapper/provenance/integrity-reconciliation.json)
binds the unchanged original manifest/report, records **zero native reruns**
and preserves the original `running` manifest status. **No clean CLI pass
is claimed.**

The [tooling receipt](tooling-identity.json) records actual generator commit
`d0a802b0...`, planned replay commit `8345f684...` and later observed HEAD
`4dda3482...`. Their entire lintdiff package tree, root dependency lock/manifest
and execution-file hashes are identical; use the actual manifest identity,
not a silently relabeled run. Exact Node 26.5.0 was recovered using the
existing tool manager in task-owned storage without changing shared settings.
See [replay.md](../replay.md) for offline verification versus genuinely new execution.
