# AvoidAnonymousTypes evidence appendix

This appendix supports the [migration report](migration.md). Historical measurements retain their assessed source and execution scope; none is a new run against the November 10 PR head.

## Assessed inputs and counting

| Evidence                               | Frozen identity and scope                                                                                                                                                                                                                                                                                                               | What it establishes                                                                                                                         |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Historical Swagger/TypeSpec comparison | Specs [`f6b53f105b95da05276530a0754a1c71b4f16397`](https://github.com/Azure/azure-rest-api-specs/tree/f6b53f105b95da05276530a0754a1c71b4f16397); response-only implementation published at [`02430e4a75c3c9eff17b0d2d908bec7f0b482967`](https://github.com/Azure/typespec-azure/commit/02430e4a75c3c9eff17b0d2d908bec7f0b482967)        | Ten Swagger occurrences versus one response-only TypeSpec diagnostic over 462 successful ARM projects; six failures excluded symmetrically. |
| Installed Core warning comparison      | Same specs commit; 468 ARM projects plus WidgetAnalytics; baseline includes request-body fix at [`88d691bb51be944df0ff60171059e437d7f2db27`](https://github.com/Azure/typespec-azure/commit/88d691bb51be944df0ff60171059e437d7f2db27); candidate loaded rule SHA-256 `b04ae191f8ca0ab68491412f9ed3bd5bc31aa78655c179f1f014a55d090d21a5` | All 469 source compiles succeed; complete naming-rule warnings increase 21 to 22; only CustomLocations is added.                            |
| November 10 focused checks             | PR source [`3a08c00ff9daca0ed6eb44ce043d424a90d78ab9`](https://github.com/Azure/typespec-azure/commit/3a08c00ff9daca0ed6eb44ce043d424a90d78ab9); compiler [`8574d5453f7bf9a07dc09bd41edac579af71d94b`](https://github.com/microsoft/typespec/commit/8574d5453f7bf9a07dc09bd41edac579af71d94b)                                           | Current focused regression/build/format/lint evidence, not current corpus or whole-PR readiness.                                            |

The historical run used latest-selected-version Swagger, production common Spectral rules, retained Swagger generated August 6, 2026, and a TypeSpec source program rather than emitter/SDK-projected endpoints. Readme suppressions were not applied to that Swagger comparison. Swagger severity was error; the consolidated TypeSpec rule is a warning. Failed TypeSpec projects were not counted as compliant.

The final historical TypeSpec report records `2026-09-23T07:43:21.622Z` and duration `1332102 ms` at concurrency six. The [immutable report](https://github.com/Azure/typespec-azure/blob/02430e4a75c3c9eff17b0d2d908bec7f0b482967/packages/typespec-lintdiff/test/fixtures/AvoidAnonymousTypes/migration.md#final-corpus-evidence) retains source/base context, project inventory, commands and limitations.

Raw Swagger findings across all projects were 32. Excluding 22 occurrences in six failed projects leaves 10. Both project + file + JSON-path and file-independent project + JSON-path summaries remain 10. The one TypeSpec source-location summary remains one. There is no supported cross-domain matching or deduplication into common defects.

Across the 462 successful projects, 454 have equal counts (all unaffected), seven are Swagger-higher by a total of 10, and one is TypeSpec-higher by one. No affected project overlaps. The SDK-override finding belongs to the service's sole `2021-08-31-preview` version; zero findings were excluded as older versions. This does not establish general version-projected parity.

An older aggregate snapshot reported 450 compiled projects and 210 rules, whereas the retained observed report reported 462/468 and 215 rules. The aggregate lacks reproducible specs/generator revisions and per-project identities. It cannot identify unmatched services or validate a coverage percentage; its discrepancy is not attributed to a newly discovered rule defect.

## Dictionary representation differences

Every positive Swagger row below is part of the complete seven-project Swagger-only set. Counts are occurrences, not source-model defects. The original captured snippets and paths are in the [historical gap examples](https://github.com/Azure/typespec-azure/blob/02430e4a75c3c9eff17b0d2d908bec7f0b482967/packages/typespec-lintdiff/test/fixtures/AvoidAnonymousTypes/migration.md#code-backed-gap-examples).

| Project                                                                                       | Selected API version | Swagger findings | Response-only TypeSpec findings | Source-backed explanation                                                                                    |
| --------------------------------------------------------------------------------------------- | -------------------- | ---------------: | ------------------------------: | ------------------------------------------------------------------------------------------------------------ |
| `specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement`          | `2025-09-01-preview` |                1 |                               0 | `GatewayContracts.listTrace` returns `ArmResponse<Record<unknown>>`.                                         |
| `specification/developerhub/resource-manager/Microsoft.DevHub/DeveloperHub`                   | `2025-03-01-preview` |                1 |                               0 | `generatePreviewArtifacts` returns `ArmResponse<Record<string>>`.                                            |
| `specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight`                      | `2025-01-15-preview` |                2 |                               0 | One response dictionary (`ClusterConfiguration`) and one nested dictionary (`Record<ClusterConfiguration>`). |
| `specification/datafactory/resource-manager/Microsoft.DataFactory/DataFactory`                | `2018-06-01`         |                2 |                               0 | `projectConnectionManagers` and `packageConnectionManagers` are `Record<Record<SSISExecutionParameter>>`.    |
| `specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration`          | `2025-09-01-preview` |                1 |                               0 | `NodeMonitoringData` has a property named `additionalProperties` containing `Record<unknown>`.               |
| `specification/impact/Impact.Management`                                                      | `2026-01-01-preview` |                1 |                               0 | `WorkloadImpactProperties` has the same dictionary-valued property shape.                                    |
| `specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights` | `2025-10-01-preview` |                2 |                               0 | `RecommendationProperties` and `RecommendedSuggestion` have `additionalProperties?: Record<string> \| null`. |

For example:

```typespec
op generatePreviewArtifacts(
  ...ApiVersionParameter,
  ...SubscriptionIdParameter,
  ...LocationResourceParameter,
  @body parameters: ArtifactGenerationProperties,
): ArmResponse<Record<string>> | ErrorResponse;
```

Its emitted response schema is:

```json
{ "type": "object", "additionalProperties": { "type": "string" } }
```

The Swagger predicate diagnoses that representation. `Record<string>` is a named semantic dictionary, not an authored anonymous TypeSpec model. Nested `Record<Record<T>>` similarly creates an inline inner dictionary. A source property literally named `additionalProperties` can be reached by the recursive definition selector, but that does not make its named dictionary type anonymous.

Recommendation: keep this naming rule semantic and preserve supported dictionaries. Exact Swagger parity would require a separately agreed emission/dictionary policy. The evidence does not establish that these ten Swagger checks are upstream bugs or ten service defects.

## Composition-and-extension boundary

The [Swagger selector](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/az-common.ts#L462-L478) checks response schemas plus object-valued `additionalProperties` and `allOf` entries below definitions. Its [predicate](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/avoid-anonymous-schema.ts) accepts null, any schema containing `x-ms-client-name`, and schemas without nonempty properties, additional properties or composition. The rule is OpenAPI 2, `resolved: false`, severity error.

The TypeSpec rule does not predict emitter references or read schema extensions. A named model with a generic dictionary base can produce an inline object inside `allOf` while still being named in TypeSpec. A schema override can insert an inline object without creating an anonymous semantic model. Conversely, an emitted `x-ms-client-name` exemption is not itself a source-naming exemption. These are source-inspected non-equivalence boundaries, not measured current-corpus frequencies or captured execution of every emitter path.

AutoRest representation also limits historical controls: plain anonymous object unions can produce `union-unsupported`, and multiple distinct same-status JSON/XML payloads can produce `duplicate-body-types`. Supported compiler/HTTP authoring shapes still need correct TypeSpec diagnostics even when that emitter cannot represent them. An emitter error was not suppressed to manufacture a parity result.

## SDK override and compatibility

The only TypeSpec-only historical project was:

`specification/extendedlocation/resource-manager/Microsoft.ExtendedLocation/CustomLocations`

At [the pinned specs source](https://github.com/Azure/azure-rest-api-specs/blob/f6b53f105b95da05276530a0754a1c71b4f16397/specification/extendedlocation/resource-manager/Microsoft.ExtendedLocation/CustomLocations/client.tsp#L154-L159), `resourceSyncRulesUpdate` is a JavaScript SDK override:

```typespec
@@override(ResourceSyncRules.update, resourceSyncRulesUpdate, "javascript");
```

Its return union includes:

```typespec
{
  statusCode: 200;
  body: Microsoft.ExtendedLocation.resourceSyncRule;
  azureAsyncOperation: string;
  retryAfter: int32;
}
```

These properties lack `@statusCode`, `@body` and `@header`; HTTP semantics see an implicit anonymous payload. The emitted ARM operation uses a named resource response instead. The rule deliberately uses compiler/HTTP semantics, not SDK projection or override filtering.

The installed-package comparison has 469 successful compiles in both profiles, zero errors/crashes, 21 baseline and 22 candidate naming warnings, exactly this added warning, and no removed diagnostics. It hash-verified 8,652 source/config files. The shared installed cohort was compiler/HTTP 1.17.0, REST/versioning 0.87.0 and Azure 0.73.0. Emitters were disabled; this is source-warning impact, not emitted-Swagger equivalence. Positive canaries had two existing baseline warnings and four candidate warnings; plain/metadata-bearing implicit responses were added while suppression, named/spread controls and shared-model deduplication remained valid.

The [historical external CI failure](https://github.com/Azure/typespec-azure/actions/runs/39196989244/job/117881773984) recorded 601 passing projects and one failure: CustomLocations `client.tsp:158`, where warning promotion made the same naming diagnostic an error. This is related compatibility evidence, not an unrelated green-CI exception.

A later [November 5 run](https://github.com/Azure/typespec-azure/actions/runs/41824032647/job/126554077335) recorded 205 passes / 400 failures: 845 `arm-common-types-version` error occurrences across 394 projects, 42 `no-response-body` occurrences across 21, and one naming occurrence in CustomLocations. Project sets overlap; raw occurrences are not unique failing projects. Other rules' failures do not erase the naming failure, and a matched baseline would be needed to establish causality for those other rules.

Recommended action remains a named service response or an approved compatibility suppression. No consumer contract edit, annotation or approved suppression decision is made by this report. At refresh inspection, the current-head [external job](https://github.com/Azure/typespec-azure/actions/runs/42774292159/job/129689064694) was still in progress. No companion URL was verified; an initial companion proposal and an explicit refresh are separate operations, not outcomes claimed here.

## Response semantics and controls

The [current rule](https://github.com/Azure/typespec-azure/blob/3a08c00ff9daca0ed6eb44ce043d424a90d78ab9/packages/typespec-azure-core/src/rules/no-unnamed-types.ts) resolves HTTP once for request/response inspection. It enumerates original return-model constituents, inspects every actual content body, recognizes named payload reuse with `getEffectiveModelType` and header/status filtering, and follows `Model.sourceModels` back to original return constituents. The existing model set deduplicates property/request/response uses. No emitter, OpenAPI/TCGC API, private state or version mutation is introduced.

The [canonical response tests](https://github.com/Azure/typespec-azure/blob/3a08c00ff9daca0ed6eb44ce043d424a90d78ab9/packages/typespec-azure-core/test/rules/no-unnamed-types.test.ts#L101-L463) cover:

- Direct anonymous responses, aliases and anonymous intersections, with header/status combinations.
- All 13 original-constituent ordering cases: plain/reversed unions, named-first/last, two envelopes in either order, spread-first/last, explicit-body-first/last, nested/shared unions, shared aliases and non-model alternatives.
- One diagnostic per original declaration across operations/statuses and exact imported source targets.
- Named direct/spread controls, combined and split inside/outside metadata, plus shared imported spreads with and without added payload.
- Empty/metadata-only bodies, void, scalars, arrays, dictionaries, and explicit-body/property/request deduplication.

The historical source repair added 13 constituent regressions: before the repair nine failed and 64 passed; afterwards all 73 source tests passed. Wrong first-body identity and filtered/unfiltered named-model comparisons caused missing or misdirected diagnostics. Those regressions, not unchanged corpus totals, demonstrated the repair.

The historical `audit:noise` implementation omitted its local-linter activation argument and returned zero local findings. That zero was not coverage evidence; strict fixture snapshots and emitter-free semantic tests supplied the controls. The harness was not changed by this migration.

## Template boundary

The [concrete-inheritance correction](https://github.com/Azure/typespec-azure/commit/a6b7c2e9a3fd2b7d31cbb401280a5b00225e7d10) changed production behavior after the historical cohort measurements. A concrete inherited endpoint must be checked even when declared through a generic interface; generic operation/interface declarations remain exempt. Its canonical regression failed before the guard fix and then passed at the original authored model target.

The [imported-template tests](https://github.com/Azure/typespec-azure/blob/3a08c00ff9daca0ed6eb44ce043d424a90d78ab9/packages/typespec-azure-core/test/rules/no-unnamed-types.test.ts#L147-L218), added in [`2889105d`](https://github.com/Azure/typespec-azure/commit/2889105d5624c6d071d84e40f38243d442f35bc0), pass against the existing implementation:

- A named library `Result<string>` returned through a library operation template is accepted. Its semantic model name is `Result`; angle brackets belong to display formatting.
- A project-authored anonymous argument returned through that template produces one diagnostic at the authored expression.

This does not prove that every anonymous declaration authored inside library source will warn. The operation guard excludes library declarations, and compiler lint reporting filters library-source targets. No blanket angle-bracket/name-string filter was adopted.

## Ownership and fixture mapping

Azure Core owns the rule because its naming policy applies to both ARM and data-plane HTTP services. The current implementation consolidates responses into existing `no-unnamed-types`, rather than retaining the earlier supplemental response-only rule. Existing property checks own explicit `@body` / `@bodyRoot`; request-template checks remain intact. Severity, message, enabled presets and suppression identity are unchanged.

The [ruleset tests](https://github.com/Azure/typespec-azure/blob/3a08c00ff9daca0ed6eb44ce043d424a90d78ab9/packages/typespec-azure-rulesets/test/validate-rules-defined.test.ts) retain the enabled existing rule in both presets and reject a separate `no-unnamed-response-bodies` registration.

| Original response-only fixture   | Retained canonical evidence                             |
| -------------------------------- | ------------------------------------------------------- |
| `compliant`                      | Named-response controls                                 |
| `implicit-response`              | Anonymous-response cases with authored targets          |
| `metadata-response`              | Header/status anonymous response case                   |
| `intersection-response`          | Anonymous intersection cases                            |
| `spread-response`                | Complete named-spread control                           |
| `metadata-spread-response`       | Complete spread containing header/status metadata       |
| `split-metadata-spread-response` | Both split header/status directions                     |
| `shared-multi-status-response`   | One original declaration across operations and statuses |

The [historical fixtures](https://github.com/Azure/typespec-azure/tree/02430e4a75c3c9eff17b0d2d908bec7f0b482967/packages/typespec-lintdiff/test/fixtures/AvoidAnonymousTypes) include eight comparison fixtures (four direct violations and four controls). Current explicit-body expectations correctly assert the existing property diagnostic instead of the former response-only exclusion. Literal ARM controls remain in the canonical ARM suite; the bespoke Markdown-parsing integration file was removed, not replaced with a new documentation-testing system.

The [current guide](https://github.com/Azure/typespec-azure/blob/3a08c00ff9daca0ed6eb44ce043d424a90d78ab9/packages/typespec-azure-core/src/rules/no-unnamed-types.md) uses one Incorrect/Correct pair with property, request and implicit-response categories. ARM examples use the supported `ArmResourceRead` template, including `get is ArmResourceRead<Widget>;`. They are excerpts requiring the stated imports/provider/resource context, not standalone programs. November 5 one-time validation of the actual response excerpts produced one naming warning versus zero diagnostics. The later heading-only change retained all eight code blocks unchanged; no continuous snippet-coverage claim is made.

## Validation and performance

### November 10 merge checks

The merged PR parent identities were `7f7d22e3a3a8fc78ec029c3727240cb392a218d5` and main `4184cf254ea0420446ebe9bc3b978b2da342ca76`; the resulting head is `3a08c00ff9daca0ed6eb44ce043d424a90d78ab9`. Production naming-rule source is unchanged from the concrete-inheritance fix. The only text conflict was independent ruleset test additions; all three test blocks were preserved.

The initial test attempt used stale compiled compiler output after the submodule update and failed on reserved `typeref` / missing implementation diagnostics. A normal dependency-closure rebuild succeeded (21 tasks), after which all **106 focused tests passed** in 32.54 seconds: 83 Core, four ARM and 19 ruleset tests. Root `pnpm format`, `pnpm lint`, and the PR delta's whitespace check passed. The compiler checkout matches the merged pin. No stale-output failure is represented as a successful run.

Commands from the prepared source checkout:

```powershell
mise exec -- pnpm run-all build --filter=@azure-tools/typespec-azure-rulesets...
mise exec -- pnpm exec vitest run --config vitest.config.fast.ts packages\typespec-azure-rulesets\test\validate-rules-defined.test.ts packages\typespec-azure-core\test\rules\no-unnamed-types.test.ts packages\typespec-azure-resource-manager\test\rules\no-unnamed-types.test.ts --pool=threads --maxWorkers=1
mise exec -- pnpm format
mise exec -- pnpm lint
```

This is not a full monorepo build/test, fresh corpus run, completed current-head external CI check or independent review of a new source change. This report refresh changes evidence text only.

### Historical broad validation and limitations

At October 16's `4396863afa58f9e22f56addbc89113d35f5cc8ba`, the recorded full Core/rulesets run passed 61 files, 580 tests and two unchanged skips, with focused 126/126 tests and 11 passing GitHub checks. These are historical outcomes, not current-head gates.

Subsequent test/doc cleanup retained the constituent/metadata/imported-target acceptance boundaries. October 19 reported 116 focused tests and eight ruleset tests passing. Broader TypeScript test configurations retained eight Core and 25 ARM baseline diagnostics, not passing type checks. October 21's two combined runs each had 82 passes and one 10-second ARM setup/integration test timeout; independently selected canonical Core/ARM tests and the registered Sync/Async request integration passed later without changing timeout/retry settings. Neither failed combined run was relabeled green. A prior optional broad `validate:pr` attempt expired at five minutes; a Python prepare TLS error did not become a successful full dependency-install claim.

The source repair's historical strict comparison ran eight AvoidAnonymousTypes fixtures plus unchanged 23 ConsistentPatchProperties, 19 PatchBodyParametersSchema, 13 ConsistentResponseSchemaForPut and six LroErrorContent fixtures. That is not current-source fixture validation. The imported-library follow-up later passed 87 canonical Core/ARM cases without a production change or new corpus claim.

### Bounded historical performance

The October 21 measurement compared baseline `88d691bb51be944df0ff60171059e437d7f2db27` (already including request-body naming) with candidate production `984152c923a1d26e5d95fb036cbe91e375185790`. Loaded Core runtime emission was checked against the exact Git objects for all 89 JavaScript files per profile, normalizing only source-map comments. Baseline/head loaded naming-rule SHA-256 values were `05b4b00c1bc229a8ac7fce683cdee578a9c1730a0d3201ae140ffeee067e0087` / `b04ae191f8ca0ab68491412f9ed3bd5bc31aa78655c179f1f014a55d090d21a5`. Non-Core compiler/HTTP/REST/versioning/ARM/rulesets/TCGC package trees matched across profiles.

The shared non-dedicated Windows machine used Node 26.5.0, 16 logical CPUs and 64 GiB RAM. Between `2026-10-21T03:56:50.211Z` and `2026-10-21T03:59:27.197Z`, 48 serial fresh subprocesses covered three services, two profiles and two variants, each with a discarded warm-up and three measured iterations. Baseline/head order alternated. Emitters, compiler reuse and worker parallelism were disabled; no timeout/retry settings changed. A preliminary run with an outdated registry was excluded rather than presented as final measurement.

Values below are median [minimum, maximum] milliseconds, except whole-process peak RSS in MiB. `enabled` means the applicable standard Azure preset, not all optional rules. `isolated` means only the existing naming rule.

| Service / profile          | Variant   |              Compile ms |          All lint ms |         Naming ms |         Peak RSS MiB |
| -------------------------- | --------- | ----------------------: | -------------------: | ----------------: | -------------------: |
| WidgetAnalytics / enabled  | Baseline  | 1448.3 [1356.2, 1674.8] |    37.2 [32.4, 37.3] |    5.3 [4.7, 5.4] | 161.6 [160.7, 167.5] |
| WidgetAnalytics / enabled  | Candidate | 1439.7 [1358.2, 1526.3] |    33.7 [32.8, 34.6] |    5.2 [5.1, 5.7] | 161.8 [161.4, 166.2] |
| CustomLocations / enabled  | Baseline  | 2746.0 [2553.2, 2820.1] |    93.7 [90.2, 99.4] | 10.9 [10.4, 11.2] | 208.4 [204.7, 209.2] |
| CustomLocations / enabled  | Candidate | 2840.2 [2702.1, 3025.5] |   91.9 [87.4, 101.7] | 11.7 [11.0, 12.3] | 201.2 [201.0, 206.4] |
| Advisor / enabled          | Baseline  | 3178.7 [3038.8, 3526.5] | 136.5 [132.1, 143.9] | 14.3 [14.1, 14.8] | 208.8 [208.4, 209.6] |
| Advisor / enabled          | Candidate | 3186.2 [3118.4, 3505.7] | 140.6 [134.8, 143.4] | 15.9 [15.1, 18.2] | 209.5 [207.9, 211.1] |
| WidgetAnalytics / isolated | Baseline  | 1327.2 [1294.5, 1764.4] |       7.4 [7.3, 7.6] |    5.9 [5.8, 5.9] | 161.6 [160.9, 164.4] |
| WidgetAnalytics / isolated | Candidate | 1349.0 [1329.1, 1659.9] |     10.3 [8.8, 11.1] |    8.4 [7.2, 9.1] | 167.1 [161.0, 168.2] |
| CustomLocations / isolated | Baseline  | 2522.9 [2407.1, 2550.7] |    25.7 [19.1, 26.2] | 21.4 [15.6, 21.8] | 201.6 [197.9, 201.9] |
| CustomLocations / isolated | Candidate | 2507.4 [2474.5, 2697.5] |    21.7 [20.6, 22.4] | 18.2 [17.2, 19.0] | 202.0 [201.5, 202.5] |
| Advisor / isolated         | Baseline  | 2978.1 [2865.5, 3023.5] |    33.3 [30.1, 38.5] | 28.6 [25.8, 31.8] | 210.7 [206.3, 216.3] |
| Advisor / isolated         | Candidate | 2944.1 [2718.8, 3007.0] |    33.4 [32.4, 39.2] | 28.8 [28.0, 33.4] | 207.5 [205.9, 218.1] |

Isolated naming medians changed +2.5 / -3.2 / +0.2 ms. Mixed noisy three-process samples do not prove negative cost, no regression or a whole-corpus upper bound. Compile timing surrounds public `compile`, including source loading/checking/linting; module import/config resolution and process startup are outside it. Lint/naming timers use `program.stats.runtime.linter`; peak RSS uses the whole process's `resourceUsage().maxRSS`, not separately attributed linter allocations. All measured compiles had zero errors/crashes, with warnings not promoted.

Reproduction uses the frozen specs source, identical compatible installed cohorts from the preceding section, hash-verified source copies and Core built from the two exact revisions. For each service/profile/variant, run fresh serial processes with no emitters and `warningAsError: false`; enable the appropriate Azure preset or only `no-unnamed-types`. Measure public `compile` with `performance.now()`, retain linter runtime statistics and peak RSS, discard iteration zero, then report median/min/max for iterations one to three. Today's unpinned packages are not replacements for the measured closure. Raw local samples are not claimed to be a newly published replay bundle.

## Limits and readiness

The six failed historical projects remain outside behavioral coverage:

| Project                     | Error                                                                 | Excluded Swagger findings |
| --------------------------- | --------------------------------------------------------------------- | ------------------------: |
| DeviceProvisioningServices  | HTTP duplicate body in `client.tsp`                                   |                         0 |
| Insights/TenantActionGroups | HTTP missing URI parameter in a legacy operation                      |                         0 |
| Network/Network             | HTTP missing URI parameter for `applicationGatewayAvailableSslOption` |                        21 |
| Quota                       | HTTP missing subscription/resource-group URI parameters               |                         0 |
| Resources/deployments       | HTTP duplicate body in a legacy operation                             |                         1 |
| ServiceLinker               | HTTP duplicate body in `client.tsp`                                   |                         0 |

The [full paths and errors](https://github.com/Azure/typespec-azure/blob/02430e4a75c3c9eff17b0d2d908bec7f0b482967/packages/typespec-lintdiff/test/fixtures/AvoidAnonymousTypes/migration.md#compile-failures-and-limits) are pinned. A retained Network JSON path could not be reconciled with its attributed Swagger file; Network is excluded, and no correspondence claim relies on that inconsistency.

The current compiler pin and concrete-inheritance production fix differ from historical measured inputs. This description/report refresh does not run coverage, refresh a shared Swagger baseline, start a new review/development cycle, or claim replay/checkpoint completion. The known CustomLocations compatibility issue and current-head rollout uncertainty remain visible in the report's conclusion, not just this appendix. A later semantic or rollout claim must satisfy its own fresh relevant coverage and review gates.

No new companion suppression PR was created, no existing companion was refreshed, and no thread was resolved. The PR source/title remain unchanged. The refreshed report replaces stale supplemental-rule/append-only claims while preserving historical evidence under its real scope.
