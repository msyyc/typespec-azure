# Previous candidate: 2026-11-03 evidence and differences

**Preceding candidate:** these are the 2026-11-03 results, preserved unchanged.
The [source-only simplification](simplification.md) and
[current migration assessment](migration.md) supersede their TypeSpec counts
and versioning scope; the shared Swagger observations remain unchanged.

The preceding candidate is `60a56b11d149b5960783e0c18da675d6cceb902e`.
[Execution metadata](refresh-20261103/task.json) and the
[sealed manifest](refresh-20261103/runs/full-corpus/manifest.json) record a
fresh full native run: **487 successful projects, 0 failures, 112 findings
in 39 projects**. The unchanged Swagger staging observations remain
**1,314 findings in 335 projects**.

The [complete difference inventory](refresh-20261103/staging-comparison/differences.md)
accounts for both engines separately for every differing project.
The [earlier emitted-side investigation](gap-investigation.md) retains the
verified Swagger predicate causes. Its old TypeSpec counts are historical;
the fresh comparison supersedes them. No source-to-Swagger diagnostic pairing
is inferred from leaf names, project overlap or matching totals.

## Inherited-leaf corrections

The exact old/new source-diagnostic multiset comparison removes **102 findings**
and adds **0**, on identical frozen specs:

| Project                   | Swagger, unchanged | TypeSpec before | TypeSpec after | Removed source findings                |
| ------------------------- | -----------------: | --------------: | -------------: | -------------------------------------- |
| DevCenter                 |                 13 |              90 |              0 | All 90 previous missing-leaf records   |
| CDN                       |                  4 |               9 |              0 | All nine previous missing-leaf records |
| Power BI Dedicated        |                  2 |               2 |              0 | `members`, `mode`                      |
| Machine Learning Services |                 21 |               4 |              3 | `identity`                             |

All other projects' exact diagnostic multisets are unchanged. The
[delta JSON](refresh-20261103/candidate-delta.json) retains every removed
target/message and both candidate identities. Removal is a measured behavior
change, not a count-based classification of all prior warnings as API defects.
The remaining Machine Learning warnings concern `maxNodeCount`, `minNodeCount`
and `nodeIdleTimeBeforeScaleDown`; cross-engine correspondence remains unassessed.

### Representative source: inherited writable members

The [Power BI source](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/powerbidedicated/resource-manager/Microsoft.PowerBIdedicated/PowerBIDedicated/models.tsp#L155-L208)
has the same structural problem as the recorded DevCenter/CDN examples:

```typespec
model DedicatedCapacityProperties extends DedicatedCapacityMutableProperties {
  @visibility(Lifecycle.Read)
  state?: State;

  @visibility(Lifecycle.Read)
  provisioningState?: CapacityProvisioningState;
}
model DedicatedCapacityMutableProperties {
  administration?: DedicatedCapacityAdministrators;
  mode?: Mode;
  // Other read-only members omitted.
}
model DedicatedCapacityAdministrators {
  members?: string[];
}
```

The old gate saw only read-only direct properties and failed to descend into
the PUT's inherited writable leaves. The corrected gate uses the same inherited
property iterator as leaf collection. Swagger's two findings are unchanged
schema inequalities, not evidence that the two removed source warnings were
the same Swagger defects.

### Representative source: inherited-only wrapper

The [Machine Learning source](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices/models.tsp#L8075-L8102)
contains:

```typespec
model PartialRegistryPartialTrackedResource {
  identity?: RegistryPartialManagedServiceIdentity;
  // Other members omitted.
}
model RegistryPartialManagedServiceIdentity
  extends Azure.ResourceManager.CommonTypes.ManagedServiceIdentity {}
```

The old gate treated the inherited-only identity model as an opaque `identity`
leaf. The corrected traversal descends into its effective inherited properties,
as it already did for direct members. The saved source warning at
`models.tsp:8082:3` is absent from the fresh receipt. This is the second important
effect of making recursion and leaf collection agree; the focused inherited-only
wrapper test protects it.

## Absent or void PUT input

Both original missing-PUT controls failed before the correction and now pass
their missing-property assertions. Registered-linter controls independently
confirm one finding for a nonempty PATCH paired with either absent or explicit
void PUT input; an unsupported actual string PUT still produces no target-rule
finding. The existing removed-body-parameter test now also expects the missing
property in versions where the PUT body was removed.

No new corpus finding was added. The zero corpus occurrence is not the reason
for accepting the fix; the documented presence policy and discriminating
controls establish it. Empty/missing PATCH checks and property-level diagnostic
targeting remain unchanged.

## BillingTrust request membership

Disposition: **no TypeSpec visibility/discriminator correction for this case.**
The warning remains **0 Swagger / 1 TypeSpec**:

```typespec
// PUT: RuleProperties
@visibility(Lifecycle.Read)
kind: RuleKind;

// PATCH: RulePatchProperties
kind: RuleKind;
```

See the actual [PUT](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/billingtrust/resource-manager/Microsoft.BillingTrust/BillingTrust/main.tsp#L222-L259)
and [PATCH](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/billingtrust/resource-manager/Microsoft.BillingTrust/BillingTrust/main.tsp#L320-L324)
declarations. The retained shared Swagger PUT schema includes:

```json
{
  "kind": {
    "$ref": "#/definitions/RuleKind",
    "description": "The kind of rule. Acts as a discriminator for kind-specific properties.",
    "readOnly": true
  }
}
```

Swagger's helper compares retained leaf schemas without applying the TypeSpec
request-visibility policy. The emitter can share a canonical read schema with
read-only members; schema presence is not proof of request membership.
Discriminator metadata and comments about an internal back-PUT carrying or
tolerating the field do not override the source lifecycle contract.
Do not include read-only PUT properties merely to remove this warning.
An intended request-visible discriminator needs a consistent source contract
or a separately justified exception/suppression. This assessment does not
declare the runtime service broken or require an emitter change.

The final registered-linter discriminator control still reports missing `kind`.
This supersedes the earlier report's required-source-fix judgment, not its raw
Swagger or TypeSpec observation.

## Historical versioning and remaining correspondence

Historical rename/type-shape false positives remain, with the migration owner's
approved temporary deferral to [#5875](https://github.com/Azure/typespec-azure/issues/5875#issuecomment-6597627686).
Managed Network Fabric remains **93 Swagger / 13 TypeSpec**; the reproduced
`primaryIpv6Prefix` warning explains one historical-name pattern, not all 13.
There is no new rule-local versioning machinery or full-parity claim.

The remaining 49 absent-name Swagger findings, unsupported/ambiguous bodies
and exact source-to-latest-emission identity remain subject to the original
comparison limitations. Counts and opposing project gaps are preserved, not
equalized through new production behavior.

## Recovery

The original receipts and package closure remain under their existing paths.
The final candidate's complete portable evidence is separate:

- `refresh-20261103/runs/full-corpus`: all 487 fresh project receipts, sealed
  manifest and native harness coverage.
- `refresh-20261103/artifacts/packages`: 15 final-candidate tarballs.
- `refresh-20261103/provenance`: build/package hashes, installed runtime
  snapshots, raw-to-published transformations and independent count cross-check.
- `refresh-20261103/controls`: 14 registered-linter control sources and receipts.
- `refresh-20261103/staging-comparison`: raw project counts, exact findings,
  both one-sided sets and unchanged Swagger schema classifications.

Recover the same immutable parent and supplement using the existing
[replay instructions](replay.md). Then, from the recovered task directory:

```powershell
python -B .\refresh-20261103\compare-staging.py `
  .\refresh-20261103\runs\full-corpus $recoveredSupplement $newEmptyComparison
python -B .\refresh-20261103\reanalyze-schema.py
```

The first command verifies candidate/specs/baseline identities, every supplement
data hash, the complete 487-project population and all successful receipts before
reconstructing the comparison. The second verifies that the affected-project
union is exactly the same 336 projects whose 497 Swagger inputs were previously
replayed, then joins only current project counts by exact project identity.
It does not rerun Swagger or pair source diagnostics with schema properties.

For a new native execution, use the existing full-run command in `replay.md`
with this final candidate/package closure, the selected supplement via
`--staging-supplement`, and a new empty run directory. Keep source/target-only,
frozen-reference, no filters or limits, concurrency 2 and the recorded budget.
Saved-data recovery is not a fresh native execution. Runtime installation locks
are provenance; fully transitive locked regeneration is not claimed.
