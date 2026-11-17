# Concrete response naming evidence

This appendix describes the November 17 candidate. The [older appendix](evidence-details.md) retains historical measurements, not the current response naming policy.

## Assessed implementation

- Candidate: `a00f22c7592f5ecfb009b783c4e367ee34a39959`.
- Compiler gitlink: `8574d5453f7bf9a07dc09bd41edac579af71d94b`.
- Official rule: `@azure-tools/typespec-azure-core/no-unnamed-types`; no separate response rule or new suppression identity.
- Source rule SHA-256: `4a1b999db693f4c5c94632dfd36b6327c4bc7ff34dd33178abf6392525e3d387`.
- Built and injected rule SHA-256: `b9dc0046f2c1afbe7efea9ad0c70f90876ec7236e8c16b74a558c98aa2e6cae9`.

The candidate was committed after focused validation and independent local review. All JavaScript files in the fifteen packed runtime packages matched their corresponding built files. The installed rule was independently hash-checked against the candidate build before corpus execution.

## Response naming contract

The rule examines the actual HTTP body, not the outer response envelope. Material generic payloads need either a concrete model declaration or an explicit resolved nonempty `@friendlyName`. A template's declaration name does not name every concrete instantiation, and an alias does not introduce a model declaration.

| Declaration and response                                              | Expected result | Basis                                      |
| --------------------------------------------------------------------- | --------------- | ------------------------------------------ |
| `model Settings is Record<string>;` then return `Settings`            | Accept          | Concrete model declaration                 |
| `model StringResult is Result<string>;` then return `StringResult`    | Accept          | Concrete model declaration                 |
| Return `Record<string>` directly                                      | Warn            | Unnamed concrete dictionary instantiation  |
| `alias Settings = Record<string>;` then return `Settings`             | Warn            | Alias preserves the generic instance       |
| Declare `model Result<T> { value: T; }`, then return `Result<string>` | Warn            | Named template, but no concrete model name |
| `alias StringResult = Result<string>;` then return `StringResult`     | Warn            | Alias does not name the concrete model     |
| Instantiate a template with a nonempty resolved `@friendlyName`       | Accept          | Explicit instance naming evidence          |

For example:

```typespec
model Result<T> {
  value: T;
}
model StringResult is Result<string>;

op unnamed(): Result<string>; // Warning
op named(): StringResult; // Accepted

@friendlyName("ResultOf{name}", T)
model FriendlyResult<T> {
  value: T;
}
model Widget {
  value: string;
}
op friendly(): FriendlyResult<Widget>; // Accepted
```

Core `Page<Widget>` and ARM `ResourceListResult<Widget>` have explicit friendly names and remain accepted. `ArmResponse<Widget>` exposes the concrete `Widget` body; the generic HTTP envelope is not itself a violation. Conversely, `ArmResponse<Record<string>>` does not hide an unnamed dictionary body.

Friendly names are source-level naming evidence, not a guarantee of a named schema under every emitter or configuration. Concrete declarations may also emit inline composition. Neither exemption establishes exact Swagger equivalence.

## Scope and diagnostic identity

The new concrete-instance requirement applies to response payloads only. Existing property, request-body and union checks retain their prior generic behavior. In particular, accepting a nested dictionary-valued property is not evidence that the new response check covers Swagger's recursive schema selector.

Empty and metadata-only generics, scalars and arrays remain compliant. Indexers inherited through a base model are inspected without confusing dictionary bodies with arrays. Concrete declarations containing HTTP metadata remain concrete even when HTTP normalization maps their effective payload to a generic base.

Generic response diagnostics are attached to a project-authored operation identifier, or the concrete inheriting interface identifier when that is the authored location. Repeated status/content representations are deduplicated per operation and generic payload instance. Two operations returning the same unnamed generic can each warn and can be suppressed independently.

Existing anonymous-expression diagnostics keep their original authored-model targets and shared original-model deduplication. Anonymous expressions instantiated inside generic interfaces do not become generic-instance diagnostics merely because the compiler carries template metadata.

## Focused validation and independent review

At the candidate revision:

- Core rule tests: **108 passed**.
- ARM rule controls: **6 passed**.
- Ruleset registration tests: **19 passed**.
- Total focused tests: **133 passed**.
- Core build and the complete AutoRest/rulesets/integration dependency closure build passed.
- Repository formatting, lint, Chronus verification and whitespace checks passed.
- All four actual ARM guide examples compiled through the registered rule: each incorrect example produced one warning and each corresponding correction produced none. The implicit-response correction preserves the extra `etag` payload.
- Registered-rule suppression was verified with two operations sharing one generic instance: the suppressed operation was silent while the other warned.

Independent local review identified regressions involving concrete payload normalization, filtered and inherited dictionary indexers, generic provenance and inherited arrays. Each was corrected with a focused regression before the final test/build/artifact checkpoint. The final independent review reported no significant issues.

## Injected-package controls

The selected-rule controls used the actual installed official packages and the same coverage worker as the corpus comparison. Four control groups passed:

| Control group                                                          | Captured target diagnostics | Default-configuration target diagnostics |
| ---------------------------------------------------------------------- | --------------------------: | ---------------------------------------: |
| Six-case contract with configuration-level disablement                 |                           4 |                                        0 |
| Friendly names, Core/ARM pagination, named envelope payload and arrays |                           0 |                                        0 |
| Operation suppression and an implicit anonymous body                   |                           2 |                                        0 |
| Existing Core all-ruleset activation                                   |                           1 |                                        1 |

The first scratch fixture used the reserved operation name `array`; its compiler failure was retained. Renaming only that operation to `readArray` produced the passing four-group rerun. No production source, compiler option or assertion was changed to obtain that result.

The complete portable-worker invocation recorded **37 passing controls and six failing migration-specific fixtures**, not a passing 43-test suite. All six failures requested the unrelated, unregistered `resource-group-path-parameter` rule. They are outside this candidate's applicable controls; that rule was not added to the candidate. The complete failed invocation is retained alongside the passing portable controls. Its applicability should have been inspected before invoking the entire file.

The 37 portable controls include official-package loading, explicit activation, source suppression, missing-rule failure, options, selected-version alignment, unreachable-schema policy, referenced bases, named unions, parameters, headers and shared schemas. The selected response-policy controls above are separate from those portable harness checks.

## Frozen comparison inputs

The full comparison uses all **487 ARM projects** from source `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`, with source scope, no filter or limit, target-only execution and concurrency two.

Swagger observations are reused read-only from shared baseline `swagger-arm-20261026-2cd3c5dd`, identity `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`. Metadata is pinned at `1c9d2b0e6a596754af1aa793b1906ff3c4ef2bd6`. Full descriptor, inventory and hash verification passed before the run. The baseline has 649 Swagger files and zero producer project failures.

Tooling is pinned at `688486d1e9a1701c34fc912c01705d098625c2a3`. The supported `frozen-reference` policy keeps the older producer context distinct from the current candidate closure. No Swagger generation or validator execution is performed for this update.

The saved `AvoidAnonymousTypes` shard contains 32 occurrences across nine projects. Its Network observations include input-fallback source attribution; input filenames must not be relabeled as confirmed originating documents. Raw findings, source correspondence and any justified grouping remain distinct.

## Historical compatibility evidence

[Companion suppression PR #48088](https://github.com/Azure/azure-rest-api-specs/pull/48088) remains the original one-operation draft for linter head `3a08c00ff9daca0ed6eb44ce043d424a90d78ab9`. It has not been refreshed for this candidate. Historical CI and companion identities remain in [compatibility.json](compatibility.json) and [compatibility.md](compatibility.md); they are not current-head CI or coverage proof.

The historical 462/468 comparison, 469-project warning-impact experiment and 605-project CI run are different populations. Their totals are not combined with the new 487-project frozen comparison.

## Completed frozen comparison

The official-package comparison completed with **487 successful projects and zero failures**. Preparation began at `2026-11-17T08:44:37.311Z`; native execution ran from `08:55:39.687Z` through `09:33:43.141Z`; final aggregation completed at `09:36:37.905Z`.

The original source-scope output contains **32 Swagger occurrences and ten TypeSpec diagnostics**. All ten TypeSpec diagnostics remain in the 487 [project receipts](runs/20261117-a00f22c75/native-results). Applying the explicit [scope ledger](runs/20261117-a00f22c75/scope-ledger.json) gives **32 versus seven** for the selected Swagger operation population. The dependency-free [recount helper](recount.py) checks that every raw occurrence has exactly one inclusion decision, rejects failed/missing/duplicate projects, and computes both the signed difference and opposing project excesses.

The [sanitized manifest](runs/20261117-a00f22c75/manifest.json), [original aggregate output](runs/20261117-a00f22c75/coverage.json) and [coverage summary](runs/20261117-a00f22c75/coverage.md) retain the original run profile and ten-diagnostic total. The manual scope ledger does not relabel the CLI run as projected or change its 487-project population. Sanitized copies are publication evidence, not replacements for the sealed reusable baseline.

### Direct dictionary response correspondence

Five contexts were matched by exact project, HTTP route/verb, source operation, actual body and saved Swagger material schema. These are check contexts, not a normalized count replacing the raw observations.

| Project       | Source target                                                  | Actual dictionary payload                     |
| ------------- | -------------------------------------------------------------- | --------------------------------------------- |
| APIManagement | `GatewayContract.tsp:255`, `GatewayContracts.listTrace`        | `Record<unknown>`                             |
| DeveloperHub  | `routes.tsp:24`, `generatePreviewArtifacts`                    | `Record<string>`                              |
| HDInsight     | `routes.tsp:135`, `Configurations.get`                         | Alias `ClusterConfiguration = Record<string>` |
| Network       | `BgpConnection.tsp:108`, `BgpConnections.listLearnedRoutes`    | `Record<PeerRoute[]>`                         |
| Network       | `BgpConnection.tsp:123`, `BgpConnections.listAdvertisedRoutes` | `Record<PeerRoute[]>`                         |

The [response correspondence receipt](runs/20261117-a00f22c75/response-correspondence.json) includes the saved schema and actual body types. The first three contexts have three Swagger occurrences and three TypeSpec diagnostics. Network's two contexts have the multiplicity described below. Direct or aliased `Record<T>` is no longer treated as exempt merely because `Record` is a named template.

### Network response multiplicity

The saved Swagger shard contains **20 response observations** for the learned/advertised route JSON paths. Two observations identify `virtualWan.json` and match the actual source operations above. The other **18** retain `sourceDocuments: []` and `sourceAttribution: "input-fallback"` under different input filenames, while repeating the two response JSON paths.

This explains the visible **20 Swagger / two TypeSpec** occurrence difference, not 20 independently established defects. The original source documents of the 18 fallback observations were not recorded. Input filenames are not relabeled as originating documents, and the observations are not discarded as proven duplicates. Grouping by project + JSON path yields two contexts solely for transparent accounting. A producer-attribution investigation is needed before stronger deduplication claims.

### Remaining dictionary property checks

These are **nine captured Swagger occurrences with no diagnostic from the selected TypeSpec rule**, not nine newly reported or inferred owning-rule diagnostics.

| Category                             | Frozen source model and property                                                                                                                                 | Count |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----: |
| Nested dictionary                    | DataFactory `ExecuteSSISPackageActivityTypeProperties.projectConnectionManagers` and `.packageConnectionManagers`, each `Record<Record<SSISExecutionParameter>>` |     2 |
| Nested dictionary                    | HDInsight `ClusterConfigurations.configurations: Record<ClusterConfiguration>`                                                                                   |     1 |
| Nested dictionary                    | Deployments `DeploymentProperties.extensionConfigs: Record<Record<DeploymentExtensionConfigItem>>`                                                               |     1 |
| Literal `additionalProperties` field | DataMigration `NodeMonitoringData`, `Record<unknown>`                                                                                                            |     1 |
| Literal `additionalProperties` field | Impact `WorkloadImpactProperties`, `Record<unknown>`                                                                                                             |     1 |
| Literal `additionalProperties` field | Network `AzureFirewallPropertiesFormat`, `Record<string>`                                                                                                        |     1 |
| Literal `additionalProperties` field | SecurityInsights `RecommendationProperties` and `RecommendedSuggestion`, each `Record<string>                                                                    | null` | 2   |

The [source correspondence receipt](runs/20261117-a00f22c75/definition-correspondence.json) records exact frozen file/line, property declaration, surrounding suppression and source hash. The Swagger recursive schema selector observes the nested dictionary or literal named property. The new concrete-instance requirement inspects response payloads, not every dictionary-valued property, so these checks remain outside this PR's added behavior.

All nine inspected source properties carry existing `@azure-tools/typespec-azure-resource-manager/arm-no-record` suppressions. The run deliberately captured only `no-unnamed-types`; it did not capture that owning rule's emitted and suppressed diagnostics. Consequently, alternate-owner correspondence, cross-rule deduplication and an exhaustive suppression-inclusive total are **unassessed**. Do not equate selected-rule zero with absent production coverage, infer an exact suppressed count, or describe the remaining checks as approved retirements.

The proposed next analysis is to capture the existing owner's corresponding diagnostics, including suppressions, and determine whether any recursive anonymous-schema obligation still lacks an owner. Extending property/request semantics is a separate policy change, not part of this response refinement.

### HorizonDB concrete response naming

Three raw source findings target the direct `PrivateEndpointConnectionResource<"A private endpoint connection resource">` response at `routes.tsp:136`, `:149` and `:156`. The selected `2026-05-01-preview` service retains `get` and `updateStatus`; the intermediate `update` operation was removed and is excluded separately below.

The two included responses use a generic without `@friendlyName` or a service-defined concrete model declaration. They therefore warn under the approved source policy. Saved Swagger instead references common-types v6 `PrivateEndpointConnection`, producing zero `AvoidAnonymousTypes` occurrences. The [outlier receipt](runs/20261117-a00f22c75/outlier-correspondence.json) retains exact selected HTTP operations and response references.

This is not evidence that every standard generic is exempt or that the new rule misclassified an HTTP envelope. The ARM library [explicitly requires providers to declare their own private-endpoint connection resource type](https://github.com/Azure/typespec-azure/blob/a00f22c7592f5ecfb009b783c4e367ee34a39959/packages/typespec-azure-resource-manager/lib/private-endpoints.tsp#L8-L34), for example:

```typespec
model PrivateEndpointConnection is PrivateEndpointConnectionResource;
```

By comparison, standard `ResourceListResult<T>` and `Page<T>` explicitly supply friendly names and remain accepted. Adding a concrete declaration can affect emitted/SDK naming; any consumer correction must preserve the contract. Suppression targets must come from actual current CI, not extrapolation from this frozen corpus. No standard-library exemption was broadened to equalize the counts.

### Source-only observations

All ten raw diagnostics were investigated. Three are excluded from the selected Swagger operation population, not suppressed or treated as successful source corrections:

| Source finding                                                           | Selected-population evidence                                                                                                | Disposition                                                         |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| HorizonDB `routes.tsp:149`, private-endpoint `update`                    | Removed before selected `2026-05-01-preview`; absent from selected HTTP graph and saved Swagger                             | Exclude one from the seven-diagnostic scorecard; retain raw receipt |
| CustomLocations `client.tsp:158`, `resourceSyncRulesUpdate`              | SDK-only override; absent from selected `2021-08-31-preview` service HTTP graph and saved Swagger operation population      | Exclude one; retain original anonymous-expression warning           |
| Search `client.tsp:702`, `SharedPrivateLinkResourcesDeleteCustomization` | SDK-only customization; absent from selected `2026-09-01-preview` service HTTP graph and saved Swagger operation population | Exclude one; retain generic-response warning                        |

Search's actual payload is `ArmAcceptedLroResponse<"Resource operation accepted.", { azureAsyncOperation: string, retryAfter: int32 }>`: the header-like fields lack `@header`, so HTTP sees material payload. Its exclusion is based on operation population, not the assumption that all accepted-response envelopes are bodyless.

Attribution uses a separately compiled program and the supported versioning snapshot API to recover selected-version HTTP path/verb correspondence, then inspects the saved Swagger. It does **not** rerun the lint rule on projected types or prove all version-sensitive predicates equivalent. Included HorizonDB-only findings remain included despite Swagger reporting zero. No unrelated request/property/union findings were captured among these ten.

### Source and emitted policy boundaries

The Swagger linter predicate checks material object structure and exemptions, not simply the absence of `$ref`. Source declarations, aliases, generic instances, `allOf`, overrides and `x-ms-client-name` can therefore differ from emitted-schema naming. The [historical predicate analysis](evidence-details.md#composition-and-extension-boundary) remains applicable to that conceptual boundary, but its old blanket exemption for generic dictionaries is superseded by this appendix.

The raw difference is fully accounted for: `32 - 7 = 18 + 4 + 5 - 2 = 25`. The remaining response dictionary group is `3 - 3 = 0`. Per-project excesses of 27 and two are both preserved; opposing directions do not establish correspondence through cancellation. Equivalent-defect totals and percentages remain unassessed.

## Current-head review and CI

The first Balanced [Copilot review](https://github.com/Azure/typespec-azure/pull/5551#pullrequestreview-5936194099) completed on candidate `a00f22c75` with three mapped, unresolved comments. [Independent parent collection](runs/20261117-a00f22c75/review-current-head.json) verified the numeric REST endpoint and GraphQL thread state. Two comments concern rollout compatibility; the third [identifies an anonymous template-argument body gap](https://github.com/Azure/typespec-azure/pull/5551#discussion_r4597845503).

A focused regression confirmed that `Envelope<{ value: string }>` can escape the current check when `Envelope<T>` exposes `T` through `@body` or `@bodyRoot`. The property visitor excludes template arguments while the response visitor assumes an explicit body property is already covered. A corrective source/test draft now passes 109 Core, six ARM and 19 ruleset tests locally, but is **unpublished** and is **not the source assessed by this frozen run**. Its final validation must include fresh full official-package coverage before publication.

Current-head [Ubuntu24 CI](https://github.com/Azure/typespec-azure/actions/runs/44057497362/job/133950511671) independently failed **ten tests in two files**, with **5,350 passing and four skipped tests**. Five sample specs now warn on standard generic operation-status payloads:

- Data-plane `widget-manager`, `api-path-parameter`, `custom-error-type` and `trait-versioning`: `ResourceOperationStatus<...>` and related status models.
- ARM `operations/operation-status`: `ArmOperationStatus<never, ResourceProvisioningState>`.

The [sanitized CI receipt](runs/20261117-a00f22c75/ci-current-head.json) retains all 17 distinct source-location warning lines in that completed job. The sample and playground checks consume the same examples, so both fail; ungenerated-snapshot suite errors follow the compilation failures. These are current-head compatibility failures, not the historical single CustomLocations result. The concrete/friendly naming policy remains unchanged. The unpublished compatibility approach uses narrowly scoped operation suppressions where adding model declarations could rename emitted/SDK contracts; the initial sample-validation batch still has unresolved diagnostics and a timeout, so neither the draft nor CI is presented as green.

[External Integration run 44057497369](https://github.com/Azure/typespec-azure/actions/runs/44057497369/job/133950511423) completed at the exact same source head: **587 projects passed and 18 failed out of 605**. All 18 failed execution groups reconcile to **37 captured `no-unnamed-types` errors at 32 distinct authored file/line/column targets**. [The complete receipt](runs/20261117-a00f22c75/external-ci-current-head.json) retains each diagnostic, execution group and compiler error total. This is neither the frozen ARM comparison nor a count of equivalent defects.

Execution-group attribution matters: Network's parent and nested entrypoints diagnose imported `Network/Network` operations, and Discovery Combined diagnoses Workspace source. Mapping only by longest source-file prefix would incorrectly leave two failing execution groups unexplained. Every group is retained; source sharing does not discard raw diagnostics. The consumer's complete checkout SHA has not been established, so this is not a pinned consumer-source replay claim.

The CI population includes data-plane consumers and generic operation-status/pagination payloads absent from the frozen ARM comparison. These diagnostics require contract-aware consumer migration analysis, not a blanket generic exemption. Existing suppression PR #48088 remains an unchanged one-operation proposal for the older head; it does not cover this expanded current-head result. No suppression refresh or local consumer validation was performed.

## Recovery and reproduction

The [run plan](runs/20261117-a00f22c75/plan.json), [artifact provenance](runs/20261117-a00f22c75/artifact-provenance.json), [validation receipt](runs/20261117-a00f22c75/validation.json) and [baseline descriptor](runs/20261117-a00f22c75/baseline-descriptor.json) retain the candidate, closure, runtime and source-retention identities.

Candidate artifacts and sanitized validation logs belong to the immutable task-specific release [pr5551-concrete-responses-20261117-a00f22c75](https://github.com/msyyc/typespec-azure/releases/tag/pr5551-concrete-responses-20261117-a00f22c75). [Archive metadata](runs/20261117-a00f22c75/archive.json) gives the asset name, size and SHA-256; package-level and packed-file hashes remain in artifact provenance. No raw execution `log.txt`, dependency directory or machine-specific checkout path is published.

The shared baseline is independently recoverable from [`msyyc/azure-rest-api-specs`](https://github.com/msyyc/azure-rest-api-specs/releases/tag/swagger-lint-baseline-20261026-2cd3c5dd), asset `swagger-arm-20261026-2cd3c5dd.tar.gz`, **51,932,501 bytes**, SHA-256 `0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0`. Its exact TypeSpec source is retained by `evidence/long-running-operations-options-validator-20261022-source` at `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`, separately from metadata commit `1c9d2b0e6a596754af1aa793b1906ff3c4ef2bd6`.

From a fresh evidence checkout, numerical recovery needs only Python:

```powershell
python -X utf8 -B .\migration-evidence\tasks\avoid-anonymous-types\recount.py `
  .\migration-evidence\tasks\avoid-anonymous-types\runs\20261117-a00f22c75
```

Expected output: 487 assessed projects; raw Swagger 32 / TypeSpec ten; included Swagger 32 / TypeSpec seven; signed difference 25; excluded one removed-version operation and two SDK-only customizations. Asset recovery and hash validation are separate from this recount. Neither operation constitutes a second full TypeSpec execution.

The [independent recovery receipt](runs/20261117-a00f22c75/recovery.json) records a fresh clean checkout of published evidence commit `da7824f182d7d767d6f5ba8cc71ffe7f4293c6eb`, separate release downloads of both archives, exact hashes for all fifteen packages and 2,903 packed files, and remote verification of the frozen source retention ref. The published recount helper reproduced the complete saved result, not only its headline totals. All 528 cataloged Git blobs were independently byte-verified from that checkout. Recovery does not validate the held corrective source draft or establish a hermetic native rerun.

For a complete native regeneration, recover the pinned candidate/compiler, frozen specs, tooling, shared baseline and fifteen package artifacts into isolated directories. Verify the baseline with the official analyzer before use. Apply the candidate's integration runner **patch/install-only** stages to the frozen specs runtime using the recovered package directory; do not generate Swagger. The captured sanitized dependency manifest/lock are under [runtime-installation](runs/20261117-a00f22c75/runtime-installation); path tokens need rebinding, and their presence does not claim hermetic transitive dependency recovery.

The full comparison command, from tooling `packages\typespec-lintdiff`, was:

```powershell
$env:PNPM_CONFIG_VERIFY_DEPS_BEFORE_RUN = "false"
$env:PNPM_CONFIG_REGISTRY = "https://packagefeedproxy.microsoft.io/npm/"
node --import tsx/esm test\harness\native-coverage.ts `
  --candidate-repo $candidate --specs-repo $specs --tgz-dir $packages `
  --validator-rule AvoidAnonymousTypes `
  --tsp-rule "@azure-tools/typespec-azure-core/no-unnamed-types" `
  --scope source --baseline-run $baseline --baseline-policy frozen-reference `
  --native-mode target-only --concurrency 2 --output $newEmptyOutput
```

Use the recorded Node `26.13.0`, specs/tooling pnpm `12.6.0` and candidate pnpm `11.10.0` contexts. The frozen-reference policy intentionally distinguishes baseline producer compiler/libraries from this candidate closure. A future full rerun must recheck compatibility and independently complete its controls and full population; numerical replay alone proves none of those execution claims.
