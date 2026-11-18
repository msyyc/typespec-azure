# Response naming: implementation and evidence

<a id="response-naming-contract"></a>

## Assessed implementation and contract

The proposed implementation is [Azure/typespec-azure@af1c08da26fdbd4c9932b56124de0e11e896dccc](https://github.com/Azure/typespec-azure/commit/af1c08da26fdbd4c9932b56124de0e11e896dccc), following `a00f22c7592f5ecfb009b783c4e367ee34a39959`. It checks actual HTTP response payloads with the existing Core `no-unnamed-types` rule; it does not introduce a separate opt-in rule or alter request/property naming checks.

The tested five-file diff SHA-256 is `ae058cb9ee6cc18d61a3362a08c8d9546ec2939cdc54ba22e472337bc6aaea98`. Publication verified the committed diff and every raw file against the tested snapshot. Source rule SHA-256 is `7c173b49ed4769eb152c1324e59f37e877715ce961f15bbb2e6d4cb8b502dab1`; built and installed rule SHA-256 is `27648c370ca01abd95dfa849180b7643fc06e5c825b882a8088214dc4b16a9e4`. The compiler is pinned to `8574d5453f7bf9a07dc09bd41edac579af71d94b`.

| Declaration/use                                                                                         | Result                                                            |
| ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `model Settings is Record<string>;` then return `Settings`                                              | Accept: explicit concrete model declaration.                      |
| `model StringResult is Result<string>;` then return `StringResult`                                      | Accept: explicit concrete model declaration.                      |
| Direct `Record<string>` or `alias Settings = Record<string>`                                            | Warn: neither creates a concrete model declaration.               |
| `model Result<T> { value: T; }` then direct or aliased `Result<string>`                                 | Warn unless a resolved nonempty friendly name names the instance. |
| Named generic model whose declaration belongs to the verified Azure Core or ARM package                 | Accept: the standard-library declaration-ownership exception.     |
| Project generic derived from a trusted standard model, or a project model in an Azure-looking namespace | Still check: neither inherits package trust.                      |
| Named envelope with an actual dictionary, anonymous, or unnamed project-generic body                    | Check the actual body, not the envelope's name.                   |
| Explicit `@body`/`@bodyRoot` containing an anonymous template argument                                  | Warn; focused regressions cover both paths.                       |

The standard-library exception uses compiler library location metadata and the exact declaring package name, either `@azure-tools/typespec-azure-core` or `@azure-tools/typespec-azure-resource-manager`. It is not a namespace allowlist, a base-model exemption, or a blanket exemption for all library generics. Core does not import ARM to implement it.

Checked-in sample snapshots confirm that standard operation-status outer response objects can still be emitted inline; their named nested properties do not make the outer schema a `$ref`. The exception is a source-policy decision for standard declarations, not evidence that every accepted instance emits a named schema.

## Complete comparison and counting

Current receipts are in [runs/20261118-standard-models-af1c08da26](runs/20261118-standard-models-af1c08da26/). The full supported native comparison completed successfully on 487 projects with zero worker failures, using the unchanged frozen Swagger population. Source, copied, and final retained inventories were checked by the analyzer.

| Population                 | Swagger | TypeSpec |
| -------------------------- | ------: | -------: |
| Raw captured observations  |      32 |        6 |
| Included comparison scope  |      32 |        5 |
| Excluded SDK-only override |       0 |        1 |

The only excluded current diagnostic is CustomLocations `client.tsp:158`, an SDK override absent from the selected Swagger service graph. The five included TypeSpec diagnostics are API Management `GatewayContract.tsp:255`, Developer Hub `routes.tsp:24`, HDInsight `routes.tsp:135`, and Network `BgpConnection.tsp:108` and `:123`.

Compared with the preceding snapshot, three raw HorizonDB ARM-generic findings and one raw Search ARM-generic finding are intentionally removed by the standard-library exception. Two of those HorizonDB findings were included in the old scorecard; the removed-version HorizonDB operation and Search were already excluded. They are not subtracted a second time. No additional frozen-corpus warning was introduced by the anonymous-envelope correction.

The 32 unchanged Swagger observations reconcile as 3 ordinary dictionary responses, 20 Network response observations for 2 directly verified contexts, 4 nested dictionary properties, and 5 literal properties named `additionalProperties`. Thus `32 - 5 = (20 - 2) + 4 + 5 = 27`. This is diagnostic accounting, not an assertion that 27 distinct defects are missed.

### Network response observations

One verified source context is Network `BgpConnection.tsp:123`, `listAdvertisedRoutes`; the other is its learned-routes counterpart at line 108. Source excerpt:

```typespec
@action("advertisedRoutes")
listAdvertisedRoutes is VirtualHubBgpConnectionOps.ActionAsync<
  BgpConnection,
  void,
  void,
  Response =
    | Record<PeerRoute[]>
    | ArmAcceptedLroResponse<
        LroHeaders = ArmLroLocationHeader<FinalResult = PeerRouteList> &
          Azure.Core.Foundations.RetryAfterHeader
      >,
  OverrideErrorType = CloudError
>;
```

In the frozen `2026-03-01` `virtualWan.json`, the advertised-routes POST 200 response has this schema:

```json
{
  "type": "object",
  "additionalProperties": {
    "items": { "$ref": "#/definitions/PeerRoute" },
    "type": "array"
  }
}
```

Both actual dictionary response contexts still warn. The total is 20 Swagger observations versus 2 TypeSpec diagnostics. Eighteen observations have `input-fallback` attribution and no original source-document identity. Their original emission/input origins remain unknown; do not label them verified duplicate defects. The next investigation is producer attribution, not suppressing the two real dictionary warnings. Exact schema and pointer evidence: [gap-example-schemas.json](runs/20261118-standard-models-af1c08da26/gap-example-schemas.json).

### Nested dictionary-valued properties

Data Factory `models.tsp:25724`, in `ExecuteSSISPackageActivityTypeProperties`, contains:

```typespec
projectConnectionManagers?: Record<Record<SSISExecutionParameter>>;
```

The frozen stable `2018-06-01` schema at `definitions/ExecuteSSISPackageActivityTypeProperties/properties/projectConnectionManagers/additionalProperties` is:

```json
{
  "additionalProperties": {
    "$ref": "#/definitions/SSISExecutionParameter"
  },
  "type": "object"
}
```

That observation contributes 1 Swagger and 0 selected-rule diagnostics. There are four observations in this category overall. They concern property structure inside a declared model, not an unnamed concrete response-body model instance. All four corresponding source declarations already suppress `arm-no-record`. This migration does not establish that the responsible property rule captured, suppressed, or fully replaces these Swagger checks; that coverage remains unassessed.

### Literal properties named additionalProperties

Data Migration `models.tsp:3223`, `NodeMonitoringData`, contains a real declared property:

```typespec
@visibility(Lifecycle.Read)
additionalProperties?: Record<unknown>;
```

Its frozen preview `2025-09-01-preview` schema is:

```json
{
  "type": "object",
  "description": "Unmatched properties from the message are deserialized in this collection.",
  "additionalProperties": {},
  "readOnly": true
}
```

This contributes 1 Swagger and 0 selected-rule diagnostics; five observations belong to this category overall. A literal property with that name must not be conflated with an indexer's emitted `additionalProperties` keyword. All five source declarations already suppress `arm-no-record`; owning-rule diagnostic and suppression counts remain unassessed. The copied definition-correspondence receipt preserves all nine property declarations, source hashes, and existing suppressions.

### Resolved standard-library findings

HorizonDB's selected API version is `2026-05-01-preview`. Its source `routes.tsp:135` includes:

```typespec
@doc("Gets a private endpoint connection.")
get is HorizonDbPrivateEndpointOperations.Read<
  HorizonDbCluster,
  PrivateEndpointConnectionResource
>;
```

The saved GET 200 schema references `common-types/resource-management/v6/privatelinks.json#/definitions/PrivateEndpointConnection`. The ARM-declared generic model is now accepted by declaring-package identity. The update at line 149 is removed from this selected version; the status update at line 156 is added in it. The saved source/version and schema evidence distinguishes these cases.

This removes a previous TypeSpec-only difference; it does not demonstrate that every generic has a friendly name, or that all standard outer schemas are references. Search's `ArmAcceptedLroResponse` is accepted for the same declaration-ownership reason.

### Source-only CustomLocations observation

The SDK override at `client.tsp:158` includes an authored anonymous return alternative:

```typespec
| {
    statusCode: 200;
    body: Microsoft.ExtendedLocation.resourceSyncRule;
    azureAsyncOperation: string;
    retryAfter: int32;
  }
| Azure.ResourceManager.CommonTypes.ErrorResponse;
```

The raw TypeSpec warning remains. The override is absent from the selected Swagger service graph, so it is excluded from that comparison, not erased, suppressed, or described as fixed. The prior-outlier correspondence receipt preserves the source and graph attribution.

## Validation and preserved failures

Required local gates passed: 116 Core rule tests, 7 ARM companion tests, and 19 ruleset tests; five unchanged sample snapshots; five playground compilations; Core, ARM, and rulesets builds; formatting, lint, Chronus; four actual ARM guide examples and the suppression control. No sample suppressions were added, and all five sample sources/snapshots remain unchanged.

Five installed selected-rule contract/activation/suppression groups passed. The portable worker suite passed 37 cases; six cases requiring the unrelated, unregistered `resource-group-path-parameter` rule were excluded by a selector recorded before execution. These exclusions are not silent selected-rule failures.

Preserved earlier attempts include two newly authored expectation-message mistakes before Core reached 116/116; an ARM failure caused by stale Core `dist`, resolved by rebuilding Core before the unchanged test passed; an incorrect sample selector, corrected to the actual `operations/operation-status` case; a playground timeout with unproven cause followed by one explicitly authorized unchanged five-case rerun that passed; and an installed-control fixture using reserved identifier `local`, corrected to `readLocalStatus` before all five groups passed. The receipts retain failures rather than presenting only successful retries.

Artifact compatibility inspection found only key-order changes in the fresh Core archive's `peerDependencies` and `devDependencies` maps, in addition to the selected rule JS/maps. All dependency names/values, versions, other metadata, and conditional-export ordering are unchanged. The guard normalizes only those two dependency maps for comparison. Fourteen other package archives are byte-identical to the preceding run. No artifact was rewritten to pass the guard.

All 487 installed Core entrypoint hashes matched the packed artifact. Runtime provenance records Node `26.5.0`, the exact analyzer/tooling revision, installed packages, controls, and source binding. The installed specs environment also contains frozen OpenAPI 3/portal dependencies; this is not represented as a hermetic 15-package dependency closure.

### Final-head CI and review

Final-head workflows are [CI 44258427999](https://github.com/Azure/typespec-azure/actions/runs/44258427999) and [External Integration 44258427992](https://github.com/Azure/typespec-azure/actions/runs/44258427992), for source `af1c08da26fdbd4c9932b56124de0e11e896dccc`. Their completed results must be assessed separately; local gates and frozen selected-rule workers do not prove downstream CI is green.

The existing Balanced review's anonymous-body envelope finding is implemented with `@body` and `@bodyRoot` regressions. Its two rollout/compatibility concerns are not automatically resolved by accepting standard-library models or by changing release-note classification. No new review is requested while admitted valid requirements remain undisposed.

The PR remains draft. Existing [suppression proposal #48088](https://github.com/Azure/azure-rest-api-specs/pull/48088) is historical and has not been refreshed for this head. Neither release readiness nor permission to merge is asserted.

## Recovery and reproduction

The public candidate asset is published in release [`pr5551-standard-models-20261118-af1c08da26`](https://github.com/msyyc/typespec-azure/releases/tag/pr5551-standard-models-20261118-af1c08da26), asset `pr5551-standard-models-af1c08da26-artifacts.zip`: 2,209,899 bytes, SHA-256 `d5d1539156f337f84e6ea789f1202e5ff773616de2c45c939faed393c4b67da6`. Its [archive receipt](runs/20261118-standard-models-af1c08da26/archive.json) verifies an independent public download against the prepared bytes. Fresh-checkout recovery is recorded separately.

The unchanged shared Swagger baseline is `swagger-arm-20261026-2cd3c5dd`, identity `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`, source `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`, metadata commit `1c9d2b0e6a596754af1aa793b1906ff3c4ef2bd6`. Its [release asset](https://github.com/msyyc/azure-rest-api-specs/releases/download/swagger-lint-baseline-20261026-2cd3c5dd/swagger-arm-20261026-2cd3c5dd.tar.gz) is 51,932,501 bytes with SHA-256 `0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0`. It retains 487 projects, 649 Swagger files, 93,496 inventory files, and zero producer failures. The source-retention branch is `msyyc/azure-rest-api-specs:evidence/long-running-operations-options-validator-20261022-source`.

For saved-observation recovery, check out the published evidence commit in a fresh temporary directory, download the candidate and baseline assets, verify their exact sizes/hashes, and verify all candidate package/file inventories. Then run the published dependency-free `recount.py` against this run using its documented CLI. Expected totals are 487 successful workers, 32/6 raw observations, and 32/5 included observations. Verify the complete emitted result, not only those headline totals. This recount and artifact recovery do not execute the native compiler again.

A new native execution requires the pinned baseline, source/compiler and analyzer identities, package injection and installed controls, matching comparison scope, and the supported analyzer's frozen-baseline mode. Preserve the final source/package hashes and all mandatory source/copy/final inventories. Do not regenerate Swagger, substitute a different project population, or treat changed installed dependency metadata as equivalent without inspection. The recorded execution used 15 package artifacts and target-only native coverage; reproduction limits and exact arguments are preserved in the run's provenance and plan.

Current functional evidence supports the stated response source-naming policy. It does not establish complete Swagger-predicate equivalence, distinct-defect cardinality for unattributed Network observations, property-owner coverage, or data-plane corpus coverage.
