# Supporting evidence for PR #5294

## Differing groups

| Group                         |             Swagger / TypeSpec | Status                                                             | Disposition                                                            |
| ----------------------------- | -----------------------------: | ------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| Historical layout corpus      |                      151 / 302 | Partially explained; unresolved residuals                          | Record, do not repair source                                           |
| Historical immutable corpus   |                       107 / 59 | Different effective input/reference policy                         | Preserve native policy; current corpus unassessed                      |
| Historical safety corpus      |                      703 / 897 | Extensions plus unresolved attribution/residuals                   | Record, do not force count equality                                    |
| 24 unequal saved fixtures     | 44 / 57 across all 51 fixtures | Different member/combined selectors; 27 fixtures have equal counts | Preserve each occurrence and exact target; no cross-rule normalization |
| Latest review simplifications |         Unassessed post-change | Not implemented                                                    | Retain current code; explain diagnostic-loss risk                      |

The [fixture difference inventory](fixture-differences.md) accounts for all
unequal saved fixture groups. It retains both directions: eight Swagger-higher
groups contribute 12 excess findings; 16 TypeSpec-higher groups contribute 25.
Absolute difference is 37, net TypeSpec excess 13. These are fixture aggregates,
not per-project corpus gaps. Equal-count fixtures may still have different
categories and targets.

## Historical corpus

The immutable
[consolidation report](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/docs/patch-body-consolidation.md)
records the following selected-version, HTTP-reachable ARM run:

| Swagger member             | Swagger findings / projects | Corresponding TypeSpec categories / projects | Overlap projects | Swagger-only / TypeSpec-only projects |
| -------------------------- | --------------------------: | -------------------------------------------: | ---------------: | ------------------------------------: |
| ConsistentPatchProperties  |                    151 / 27 |                                     302 / 29 |               27 |                                 0 / 2 |
| UnSupportedPatchProperties |                    107 / 45 |                                      59 / 21 |               21 |                                24 / 0 |
| PatchBodyParametersSchema  |                    703 / 93 |                                    897 / 105 |               90 |                                3 / 15 |

The TypeSpec category totals are missing layout 302, immutable 59, required 472,
default 425 and exposed non-Update zero: 1,258 in 122 successful projects.
Swagger members sum to 961. Do not sum project counts, duplicate the shared
TypeSpec population per member, or interpret category partitioning as exact
Swagger-to-source attribution.

All 468 projects were attempted; 462 compiled. Failed identities were
DeviceProvisioningServices, TenantActionGroups, Microsoft.Network/Network,
Microsoft.Quota/Quota, Microsoft.Resources/deployments and ServiceLinker.
The report records the same six failures as its baseline. Its specs commit is
`f6b53f105b95da05276530a0754a1c71b4f16397`, not the newer shared Swagger
baseline's frozen specs. Full run time was 1,340,352 ms.

The old external disposition report and old observed report are linked and
reconciled in each historical member note. They have different populations
(450 versus 462 compiled projects), credit definitions and generator snapshots.
Their rows cannot be subtracted to reconstruct current missing projects.
This task is not a new comparison of those reports.

Raw per-project corpus data was not republished with this task. Consequently,
current-head project sets, occurrence/source-location deduplicated totals,
per-project positive/negative/absolute/relative gaps and exact outlier attribution
are **unassessed**, not zero. The historical aggregate net difference is
297 / 961 = approximately 30.9%; that number does not describe the current head.
No normalized operation count or complete target-level correspondence is
supported. A fresh native run over a pinned shared baseline would be needed
before a current corpus claim; historical data cannot supply that result.

## Layout and emission

The original
[Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/consistent-patch-properties.ts)
selects a PATCH body and PATCH 200/201 or same-path GET response schema.
The TypeSpec implementation prefers an explicit resource association, then
response/GET fallbacks. It compares effective authored encoded layout, not
assignability, synthetic discriminators, or an SDK emitter's scoped output.

The two historical TypeSpec-only layout projects are Informatica and
ManagedNetworkFabric. The former's Swagger omission mechanism is unresolved.
Authored/emitted inheritance and SDK selection explain fixture differences but
do not establish the cause of every within-project production difference.
**Disposition: unresolved full equivalence; no source update is authorized by
this reporting task.** Revisit the rule only if aligned target-level evidence
demonstrates an incorrect supported semantic check.

### Authored versus synthesized discriminator

Classification: Swagger-only in this fixture; intentional authored-shape policy.
The saved `ConsistentPatchProperties/synthesized-discriminator` fixture uses
standard ARM operations and API version `2024-01-01`:

```typespec
@doc("PATCH details whose discriminator property is synthesized by AutoRest.")
@discriminator("kind")
model PatchDetails {}
```

Its PATCH path is
`/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestService/widgets/{widgetName}`.
The saved Swagger reports missing `properties.details.kind` at
`paths.<that path>.patch.parameters.4.schema`; the TypeSpec rule reports none.
There is no authored `kind` property for the TypeSpec rule to require or compare.
The actual emitted schema and full authored context are retained in
[historical-fixtures.json](historical-fixtures.json) under that fixture, alongside
the exact diagnostic and source-blob hashes.

Inherited encoded discriminator fixtures have the opposite outcomes in opposite
directions: request fixture 0/1 and response fixture 1/0 at `details.kind.extra`.
The emitted derived synthetic string masks a base authored object through
`allOf`; the TypeSpec rule retains the effective authored object.
`never-resource-override` is 0/1 at `extra`, because the emitted base reference
cannot represent the authored `never` removal. These are not missing native
layout checks to be repaired by imitating emission.

### SDK-scope selection

Saved scoped request, property and GET fixtures each report 0/1; the scoped
response fixture reports 1/0 at `description`. They use SDK/client-generator
scope decorators in source fixtures, while the TypeSpec linter deliberately
uses the native HTTP program. Source excerpts, generated schemas and exact
targets are retained per fixture. No official-package SDK integration is claimed.
The source report maps these to native partial-layout and GET-selection tests;
it does not port the SDK dependency into ARM.

## Safety and counting

The original
[Swagger safety function](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-body-parameters.ts)
checks required membership, truthy defaults and exact `["create"]` mutability,
recursing through objects but not array elements. The TypeSpec linter checks
effective PATCH input and every defined default, with a top-level identity
safety exemption and separate layout/immutable findings.

Historical Swagger-only safety projects are AccessReview, ConfidentialLedger
and SAPDiscoverySite. The earlier standalone note attributes four findings to
excluded Read/Create input or descendants. The consolidation has 15 TypeSpec-only
safety projects, and 79 array default findings in 21 projects. ProgrammableConnectivity's
six required fields have unresolved source-to-recorded-Swagger attribution;
that uncertainty must not be relabeled an API-version explanation. Remaining
within-project differences are not fully classified.
**Disposition: partial coverage with intentional extensions and unresolved
comparison evidence; do not repair the rule solely to equalize totals.**

### Array extension

Classification: TypeSpec-only; intentional extension. Saved fixture:
`PatchBodyParametersSchema/array-replacement-elements`, `PATCH /widgets`,
API version `0000-00-00`.

```typespec
model Element {
  id: string;
  enabled?: boolean = false;
  extra?: string;
}
```

The request contains `items?: Element[]`; the response item has `id` and
`enabled`, but no `extra`. The actual saved definition includes:

```json
{
  "Element": {
    "type": "object",
    "properties": {
      "id": { "type": "string" },
      "enabled": { "type": "boolean", "default": false },
      "extra": { "type": "string" }
    },
    "required": ["id"]
  }
}
```

| Engine                                 | Observed saved result                                 |
| -------------------------------------- | ----------------------------------------------------- |
| Swagger linter, selected safety member | 0                                                     |
| Combined TypeSpec linter               | 2: default `items[].enabled`, missing `items[].extra` |

Required replacement-item `id` is accepted. The missing finding belongs to the
combined layout check, not the selected Swagger safety member; these counts
have no common normalized unit.

### Falsy defaults and independent categories

`PatchBodyParametersSchema/default-patch-property` records 1/8: Swagger's
selected safety check reports truthy `mode`; the combined TypeSpec rule reports
four defaults (`properties.mode`, `enabled`, `count`, `label`) and four separate
missing-layout findings. The source and emitted schemas preserve the falsy
defaults; the Swagger implementation's `if (properties[prop].default)` explains
their omission. Four default violations and four layout violations must not
be deduplicated merely because they target the same properties.

Other count-only/mixed-category examples are the nullable fixtures (1/2 each,
required plus layout), encoded immutable fixture (3/5, immutable plus layout),
`patch-with-id-name` (3/4) and `patch-with-location-provisioning-state` (2/3).
`encoded-identity-compliant` has 0/1 layout finding despite the safety exemption.
These preserve the separate responsibilities of the three-member consolidation;
the word "compliant" in a member fixture is not group-wide compliance.

## Visibility and immutable input

The original
[Swagger immutable function](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/validate-patch-body-param-properties.ts)
accepts immutable/read-only emitted properties. The TypeSpec linter instead
rejects exposed immutable PATCH input even when a request visibility override
makes a Create-only field writable. Ordinary Read/Create-only input is excluded.

### Explicit visibility override

Classification: TypeSpec-only; intentional native policy.
Saved fixture `UnSupportedPatchProperties/explicit-create-immutable-input`,
`PATCH /widgets`, API version `0000-00-00`:

```typespec
@parameterVisibility(Lifecycle.Create)
@patch
@route("/widgets")
op update(
  @body body: {
    @visibility(Lifecycle.Create) location?: string;
  },
): void;
```

Its saved Swagger request property is:

```json
{ "location": { "type": "string", "x-ms-mutability": ["create"] } }
```

The selected Swagger immutable member reports zero, accepting no `"update"`
mutability. The combined TypeSpec rule reports two: immutable `location` and
missing `Lifecycle.Update`. This fixture's saved Swagger diagnostics belong to
the selected immutable member; it does **not** prove that the separate Swagger
safety member would also be silent.

### Excluded inputs and reference resolution

`native-visibility-compliant` records 4/3. Its source contains Read-only `id`,
Create-only `createdBy`, and optional writable root `name`. Swagger safety
reports required/default `id` and Create-only `createdBy`; TypeSpec excludes
those fields, but emits three immutable `name` findings across the three
operations. This is a semantic and selector difference, not a net one-warning
loss of the same violation.

`readonly-ref-validator-discrepancy` records 1/0 at
`properties.provisioningState`. The authored property has
`@visibility(Lifecycle.Read)` and the historical investigation traces the
Swagger finding to resolved-reference annotation loss. The saved source,
emission and diagnostic remain available; the TypeSpec linter deliberately
does not recreate that artifact.

**Disposition: preserve the declared input policy; full current-head immutable
equivalence is unassessed.** Restoring emitted-shape behavior would be a separate
semantic decision, not a reporting repair.

## Latest review and regression boundary

The [latest reassessment](https://github.com/Azure/typespec-azure/pull/5294#pullrequestreview-5699317637)
explicitly identifies itself as Copilot-generated despite posting through a
human account. It is a scope/complexity critique, not independently established
evidence of required production behavior. The four inline suggestions are
still unresolved; none is adopted by this task.

| Suggestion                                                                                                                         | Current tested result                                                                                                             | Consequence of the proposed simplification                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| [Single response selector; skip ambiguous layout](https://github.com/Azure/typespec-azure/pull/5294#discussion_r4413546384)        | Shared GET fixture emits missing `extra` and default `enabled`; literal/singleton-status fixture retains definite missing `extra` | A blanket ambiguity skip could lose the common missing finding while retaining safety. No post-change run or corpus delta is claimed    |
| [Remove namespace-local no-service GET discovery](https://github.com/Azure/typespec-azure/pull/5294#discussion_r4413546410)        | No-service `PATCH /widgets` plus same-namespace GET emits missing `extra`                                                         | Removing discovery would lose this fallback diagnostic; standard associated ARM templates do not need that fallback                     |
| [Exclude every File descendant](https://github.com/Azure/typespec-azure/pull/5294#discussion_r4413546420)                          | Legal authored `contents` override emits required and default findings; inherited native File members are excluded                | Whole-model exclusion would retire these authored JSON checks. Arbitrary extra File members are compiler-invalid, not coverage evidence |
| [Compare resource model without response Read filtering](https://github.com/Azure/typespec-azure/pull/5294#discussion_r4413546436) | Read and Update members accepted; Query-only counterpart reports missing `details.value`                                          | An All-visibility comparison would accept the Query-only named member, intentionally removing that tested layout warning                |

These are source-based consequences of proposals, **not observed results for
an implemented alternative**. The fresh suite verifies only the current head.
No count for real ARM services or performance regression follows from synthetic
tests. The reviewer's 400-endpoint timing is not reproduced here.

The standard synchronous/asynchronous ARM PATCH templates carry
`@armResourceUpdate(Resource)`; the decorator calls `$updatesResource`.
Thus explicit resource association bypasses response reconciliation and GET
discovery in those templates. This supports evaluating whether fallback policy
belongs in this migration, but does not prove that removing it preserves every
currently diagnosed custom operation. A narrower supported policy needs explicit
acceptance; it is not an already approved retirement.

The current implementation traverses once **per comparison candidate**, buffers
findings, intersects missing-layout keys and deduplicates independent safety
findings. Earlier descriptions of one traversal are therefore not literally
accurate for multiple candidates. The review's complexity concern is valid;
passing synthetic controls establish the behavior, not its necessity within the
supported ARM migration scope.

## Member evidence

| Original Swagger member                                                       | TypeSpec behavior evidence                                        | Status                                                                |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------- |
| [PatchBodyParametersSchema](members/PatchBodyParametersSchema/migration.md)   | Required/default/visibility, identity, arrays, nullable input     | Intentional differences; corpus residuals unresolved                  |
| [ConsistentPatchProperties](members/ConsistentPatchProperties/migration.md)   | Encoded partial layout, association/fallbacks, inheritance/unions | Intentional differences; Informatica and corpus residuals unresolved  |
| [UnSupportedPatchProperties](members/UnSupportedPatchProperties/migration.md) | Five immutable paths, nested-name controls, visibility overrides  | Implemented native policy; not blanket emitted-mutability equivalence |

The historical [51-fixture-to-test mapping](https://github.com/msyyc/typespec-azure/blob/0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3/packages/typespec-lintdiff/docs/patch-body-consolidation.md#fixture-to-native-test-mapping)
is retained with the original snapshot, not presented as an exact current title
inventory. Current tests renamed "misnested" to "incorrectly nested", removed
redundant standalone examples/framework checks, retained meaningful controls,
and added the 22 October 29 cases. The current [113 test names and results](focused-tests.json)
provide the exact executed inventory. Do not infer semantic completeness from a
test-count percentage.

## Recovery and validation

Current code: `94b316787e2a19847c26986412ce254ca4da33b4` from the existing
`msyyc/typespec-azure:promote-lintdiff-patch-body-parameters-schema-to-arm` head.
Base is `Azure/typespec-azure:main`; this reporting branch is separate.
The destination remains `@azure-tools/typespec-azure-resource-manager`.
The rule registers with warning severity, is disabled in shared rulesets, and
does not replace `arm-resource-patch`, `patch-envelope` or PATCH-to-PUT checks.

Historical provenance: consolidated source `0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3`
from [#5540](https://github.com/Azure/typespec-azure/pull/5540), followed by
the union repair `19a9d339ad4cdaf6f777bd44f78c61e2def6e118` from
[#5820](https://github.com/Azure/typespec-azure/pull/5820).
The direct destination fixes at the current head intentionally were not
backported to source, as requested. Superseding [#5384](https://github.com/Azure/typespec-azure/pull/5384)
and [#5456](https://github.com/Azure/typespec-azure/pull/5456) remains a reviewer
decision; this task closes no PR.

Fresh execution uses Node v26.5.0, pnpm 11.10.0, the candidate's existing built
dependency closure, and core `cefb035e7721a6fdcb6de605b5f469b93055a880`:

```powershell
mise exec -- pnpm --filter @azure-tools/typespec-azure-resource-manager exec vitest run test\rules\no-unsafe-patch-body-properties.test.ts --maxWorkers=4 --hookTimeout=30000 --testTimeout=30000
```

Result: 113 passed, zero failed/skipped. No tests, production files, dependencies,
source pins, public examples or enablement were changed for this task.
The October 29 758-test ARM run, dependency builds, typecheck, documentation
generation and lint are historical validations, not a newly executed corpus.

To read saved evidence, fetch this report branch and open `historical-fixtures.json`
and `focused-tests.json`; neither requires installing repository dependencies.
The fixture file retains all 51 source excerpts, complete emitted Swagger,
selected diagnostics, and SHA-256 identities of their original Git blobs at the
immutable source pin. It is a deterministic extraction of saved observations,
not a new linter execution. The fresh test receipt preserves names/status/duration
and excludes machine-specific absolute paths.

To regenerate fixture observations, read each `main.tsp`, `output.json`,
`validator-diagnostics.json` and `tsp-diagnostics.json` under the three source
fixture families at `0cc1c2d73f30d0d0e57d1b1a7dc64bb932040da3` using `git show`.
Filter Swagger diagnostics by the three original IDs and TypeSpec diagnostics
by `tsp-lintdiff-local-linter/no-unsafe-patch-body-properties`, retaining every
occurrence. Each file's original bytes can be checked against `sourceBlobSha256`.
To recompute fixture differences, count each retained array, not distinct paths,
then group by `fixture`. This reproduces the saved fixture counts, not a corpus.

For example, from this report's directory, this dependency-free command
recalculates the raw totals and both directional excesses:

```powershell
python -c "import json; f=json.load(open('historical-fixtures.json', encoding='utf-8'))['fixtures']; s=[len(x['swaggerDiagnostics']) for x in f]; t=[len(x['typeSpecDiagnostics']) for x in f]; print(dict(fixtures=len(f), swagger=sum(s), typespec=sum(t), swaggerExcess=sum(max(0,a-b) for a,b in zip(s,t)), typespecExcess=sum(max(0,b-a) for a,b in zip(s,t))))"
```

Expected output: 51 fixtures, 44 Swagger findings, 57 TypeSpec findings,
Swagger excess 12 and TypeSpec excess 25. This reanalyzes saved observations;
it does not execute either linter.

Full current-head regeneration has **not** been performed. It requires the
current shared-baseline consumer procedure, a pinned compatible descriptor and
its frozen specs source, isolated runtime, candidate build/package injection,
fresh full native execution and target-level gap investigation. It must not
substitute this old 468-project snapshot for a newer 487-project shared baseline
or regenerate Swagger without separate producer authorization.

There is no full portable corpus replay or completed migration-readiness
certification in this report. Source/compiler/emitter changes are not proposed
to conceal these limits. **The current TypeSpec linter is not fully functionally
equal to the original Swagger linters; current corpus parity remains unknown.**

For the evidenced intentional fixture policies, **no TypeSpec rule update is
required to preserve the declared native contract**. Unresolved corpus groups
do not establish either a required rule fix or its absence; that decision remains
unassessed pending aligned target-level evidence. A requirement for exact
Swagger equivalence would require a separately agreed policy change, not a
count-normalization or source-repair action hidden in this report.
