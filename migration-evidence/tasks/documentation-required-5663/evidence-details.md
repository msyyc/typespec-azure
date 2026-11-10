# Documentation quality evidence details

## Frozen identities

| Role                                          | Identity                                                                                                                                                                               |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Official implementation                       | [Azure/typespec-azure#5663](https://github.com/Azure/typespec-azure/pull/5663), inspected at `2c6596126f281d78ca06fb23afc9ef8ab37684b8`                                                |
| Official source                               | [require-docs.ts](https://github.com/Azure/typespec-azure/blob/2c6596126f281d78ca06fb23afc9ef8ab37684b8/packages/typespec-azure-core/src/rules/require-docs.ts)                        |
| Canonical public-rule tests                   | [require-docs.test.ts](https://github.com/Azure/typespec-azure/blob/2c6596126f281d78ca06fb23afc9ef8ab37684b8/packages/typespec-azure-core/test/rules/require-docs.test.ts)             |
| Compiler/HTTP closure                         | `core` at `8574d5453f7bf9a07dc09bd41edac579af71d94b`; dependencies from the inspected official commit                                                                                  |
| Name-check source and detailed investigation  | [3753a319](https://github.com/Azure/typespec-azure/blob/3753a319f32f3926005536029f9ff32b94f3c905/packages/typespec-lintdiff/test/fixtures/DescriptionMustNotBeNodeName/migration.md)   |
| Blank-check source and detailed investigation | [72ab2239](https://github.com/Azure/typespec-azure/blob/72ab22394704fce1a1555c879ff7335da8debf42/packages/typespec-lintdiff/test/fixtures/DescriptiveDescriptionRequired/migration.md) |
| Historical specs                              | [Azure/azure-rest-api-specs at f6b53f10](https://github.com/Azure/azure-rest-api-specs/tree/f6b53f105b95da05276530a0754a1c71b4f16397)                                                  |

The original source PRs are merged, and their source branch refs no longer resolve. Their commit-pinned files were verified readable through GitHub. This new combined report branch provides a stable, branch-based description link; the original immutable investigations remain audit evidence, not current-policy instructions.

## Swagger selector evidence

The [historical installed-rule execution matrix](https://github.com/Azure/typespec-azure/blob/72ab22394704fce1a1555c879ff7335da8debf42/packages/typespec-lintdiff/test/fixtures/DescriptiveDescriptionRequired/migration.md#source-and-comparison-population) confirms that missing, empty, null, and numeric descriptions produce zero findings, whitespace/tab descriptions produce one, and meaningful text produces zero. The [pinned selector source](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/packages/rulesets/src/spectral/az-common.ts) retains `$..[?(@object() && @.description)].description`: a truthy precondition skips the empty string before the function can reject it. This is the false-negative bug the TypeSpec linter intentionally avoids.

The November 10 upstream source read verifies that selector text, not a new Spectral execution. This upstream source pin is not a recovered historical runtime identity; the original report remains the authority for the captured installed-rule behavior.

## Authorized policy adaptations

The combined official rule has three messages: `default` for existing missing documentation, `empty` for explicitly blank documentation, and `uninformative` for repeated names/placeholder text. The quality checks run through semantic callbacks, including the compiler's emitted `enumMember` callback. No new public rule ID or emitter dependency is introduced.

The official ordinary-property policy intentionally differs from the original source's JSON-name resolver: authored `sourceName` remains the comparison name under `@encodedName("application/json", "wire-name")`. Reviewer-requested simplification was implemented in [b3b1a184d](https://github.com/Azure/typespec-azure/commit/b3b1a184d0641f3c1617e885c99e3d43685f0fee). The current report does not call the old source's JSON-name outcomes current coverage.

HTTP path/query/header names and authored multipart names remain distinct metadata-based policies. Operations compare both authored names and effective HTTP verbs. Status-code properties skip name comparison, not explicit blank checks. Existing missing-documentation scopes and version/discriminator exemptions remain.

The existing presets already enable `documentation-required`. The combined change intentionally strengthens quality for current users; it is not an opt-in-only migration. A feature changeset summarizes the author-visible change; a separate samples entry covers corrected descriptions and snapshots. No new release note is needed for this report-only publication.

The original lintdiff implementations remain immutable. A future confirmed defect in those pinned sources requires the owning source-repair process, not a silent promotion-only semantic repair. New official-policy changes require explicit review and corresponding tests/evidence; this publication authorizes neither.

## Historical populations and exclusions

Both member notes use 468 attempted ARM projects and 462 successful compilations at the frozen specs revision. The six excluded project suffixes under `specification/` are:

- `deviceprovisioningservices/resource-manager/Microsoft.Devices/DeviceProvisioningServices`
- `monitor/resource-manager/Microsoft.Insights/Insights/TenantActionGroups`
- `network/resource-manager/Microsoft.Network/Network/Network`
- `quota/resource-manager/Microsoft.Quota/Quota`
- `resources/resource-manager/Microsoft.Resources/deployments`
- `servicelinker/resource-manager/Microsoft.ServiceLinker/ServiceLinker`

Failures are HTTP `duplicate-body` or `missing-uri-param`, not successful rule-only programs. The name-check excluded population contains 15,449 Swagger and 976 TypeSpec raw findings; the blank-check raw shard retains 27 additional Network warnings. Historical Swagger generation was recorded August 6, 2026; no fresh Swagger baseline was produced here.

Historical TypeSpec compilation used source suppressions and unprojected source programs, while Swagger used dataset-selected files and production rule registration without readme suppressions. The name-check selected-version extraction was a separate investigation, reused only after archived diagnostic multisets matched. It is not a common source/emission identity.

Original raw corpus artifacts were retained outside the source PRs. Their complete downloadable archive/publication binding is not established by this refresh. Commit-pinned human-readable investigations are available, but this report does not claim independent full replay or fresh raw-dataset integrity verification.

## Historical name-check differences

The original name-check report preserves all 38 unprojected one-sided projects and witnesses. Their causes are unused/imported source declarations, client compatibility types, removed/later-version declarations, namespace-qualified schema names, template-renamed keys, and constant parameters erased during emission. Selected-version attribution removes Advisor, leaving 37 TypeSpec-only projects. No Swagger-only successful project remains.

The original cardinalities are:

| Historical unit                                  | Swagger linter             | TypeSpec linter           |
| ------------------------------------------------ | -------------------------- | ------------------------- |
| Entire raw shards, including failures            | 86,264 across 109 projects | 8,499 across 147 projects |
| Successful-project raw diagnostics               | 70,815                     | 7,523                     |
| Successful project plus JSON path, ignoring file | 6,941                      | Not comparable            |
| Successful project plus source file/line/column  | Not comparable             | 7,519                     |
| Selected-version-attributed diagnostics          | 70,815                     | 7,501                     |

Raw/path/location counts cannot be divided to obtain precision or recall. SQL has 64,724 raw findings, including 3,740 ColumnDataType reference-root occurrences across 110 files for 34 file-independent member paths. The original source contains 34 authored members. AlertsManagement has 76 definition and 124 inline-parameter copies versus 76 source targets. ContainerApps and Advisor illustrate source/version scope; Fleet illustrates qualified emitted names; Manufacturing illustrates template-renamed keys; RecoveryServicesBackup illustrates erased constant parameters and multiple semantic instances sharing locations.

See the [complete original examples and project tables](https://github.com/Azure/typespec-azure/blob/3753a319f32f3926005536029f9ff32b94f3c905/packages/typespec-lintdiff/test/fixtures/DescriptionMustNotBeNodeName/migration.md). Those witnesses explain historical populations; current corpus gains/losses after authored-name adaptation are unassessed.

## Implementation and fixture mapping

Azure Core owns the public rule because documentation quality applies across data-plane and ARM authoring and needs compiler/HTTP metadata, not ARM resource identity or SDK naming. Its canonical suite is `packages/typespec-azure-core/test/rules/require-docs.test.ts`; no parallel legacy quality-rule suites remain.

| Original fixture/behavior family                                                         | Current canonical evidence                                                                                                          |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Repeated model/property names, literal `description`, normalization, meaningful controls | Parameterized repeated-name/placeholder cases, doc comments, meaningful text/punctuation controls, exact model/key-property targets |
| Enum and union members versus literal values                                             | Named/unnamed variant and enum-member controls, exact authored targets                                                              |
| Explicit/inferred HTTP verbs                                                             | Mixed missing/blank/punctuation/source-name/verb deduplication and inferred GET/POST/explicit-verb precedence                       |
| Path/query/header wire names                                                             | Combined parameter-name violation/compliance checks                                                                                 |
| JSON-encoded property/source-name controls                                               | Old JSON-precedence matrix deliberately replaced by one authored-name regression; not equivalent legacy fixture outcomes            |
| Multipart authored/source fallback/repeated parts                                        | Named-part, placeholder, unnamed fallback, and outer-array tests                                                                    |
| Empty property/parameter/member docs                                                     | Mixed blank controls, exact property/member targets, inline/instance and exempt-declaration cases                                   |
| Missing vs explicitly supplied docs                                                      | Existing missing-target tests and exemptions, combined no-duplicate regression                                                      |

The name-check's 15 original strict fixtures and 47 predicate tests and the blank-check's four strict fixtures and 22 predicate tests describe their source phases. They are not added together as current coverage. The official canonical suite was condensed to 32 cases, retaining distinct authoring branches rather than every cross-product.

### Actual published examples

The authored rule guide at the inspected commit is [documentation-required.md](https://github.com/Azure/typespec-azure/blob/2c6596126f281d78ca06fb23afc9ef8ab37684b8/packages/typespec-azure-core/src/rules/documentation-required.md). A recorded October 22 one-time execution used compiler `createTester` with `libraries: []`, no injected imports/usings/wrappers, and the real linter. The three incorrect snippets produced 2, 2, and 1 diagnostics; the correct snippet produced zero. Document SHA-256 was `e6405852d08b4128d365c582840dbbd3e923b31200e25539ba91969e488534d6`.

This is a historical one-time receipt, not continuous Markdown-driven coverage or a rerun under the current compiler. No bespoke per-rule Markdown parser was introduced. The literal semantic examples and canonical behavior tests remain.

## Validation and release readiness

At official head `2c6596126f281d78ca06fb23afc9ef8ab37684b8`, the conflict-resolution task recorded:

```text
mise exec -- pnpm -r --filter "@azure-tools/typespec-azure-rulesets..." build
mise exec -- pnpm exec vitest run --config vitest.config.fast.ts --pool=threads --maxWorkers=1 --project=@azure-tools/typespec-azure-core --project=@azure-tools/typespec-azure-rulesets require-docs.test.ts validate-rules-defined.test.ts
mise exec -- pnpm format
mise exec -- pnpm lint
```

The build and 50 tests across two files passed; root format/lint passed. The merge retains both documentation enablement and upstream client-name opt-in tests. This is not a full package-suite or corpus result. Inherited main-only whitespace warnings were left unchanged; the PR delta passed whitespace validation.

Earlier October 22 full Azure Core/ruleset validation reported 522 passing tests and two existing skips across 60 files. Earlier whole-test-project type checking had unrelated failures in casing-style tests, a type-only import, and Vitest project boundaries; focused changed-test strict checking passed. These are historical receipts, not proof the current entire test project is clean.

No linter implementation changes occur in this publication, so no additional corpus run is required for the report edit. The separately published consumer patch contains only compatibility annotations and intentionally receives no local consumer validation. It does not repair or waive existing acceptance gaps or convert historical runs into a new-head assessment. Independent prior source/promotion reviews are recorded in the original investigations and PR history; no new development/release-readiness review loop was run for this proposal task.

## Consumer compatibility and companion status

The current-head [failed job 129697292505](https://github.com/Azure/typespec-azure/actions/runs/42776863168/job/129697292505), in run `42776863168`, tested linter `2c6596126f281d78ca06fb23afc9ef8ab37684b8` with compiler `8574d5453f7bf9a07dc09bd41edac579af71d94b`. Its 10,697 `uninformative` occurrences span 208 project log groups and 7,901 diagnostic tuples in 219 files. Existing missing-doc, blank-doc and other-rule messages are outside the extraction.

All 7,901 tuples independently reconcile to 7,901 authored targets in canonical consumer base `06472951865696fb06a0e36ece718d62bf4edc33`. Exact location, direct documentation and authored/explicit HTTP names establish the intended changed predicate for every target. There are zero unresolved, stale or native-false-positive targets in this extracted population. The [complete causal report](companion/causality.md) documents the base/head source comparison, matching policy, unnamed variants, HTTP headers, raw project provenance, exclusions and machine-readable mappings.

The full CI checkout log still does not identify its tested consumer commit, and the run has zero downloadable artifacts. **Tested consumer SHA remains unknown**; the proposal base is independently frozen, not presented as the tested SHA. The verifier also omits which entrypoint first failed where both `client.tsp` and `main.tsp` are available. Machine evidence preserves actual project groups and current-base candidate entrypoints without guessing.

The source branch `Azure/azure-rest-api-specs:suppress/documentation-required-pr5663-20261110` is published at `369d77dcf0db154c6c71c39a6f6d166aee3bab9b`; initial draft publication follows. Complete diff inspection confirms only 7,901 rule-specific annotations in 219 `.tsp` files, with no deleted lines or other source changes. The justification preserves existing published descriptions for backward compatibility.

Local consumer compilation, build, tests, lint, formatting, integration, dependency setup and emission were intentionally not run. Syntax-only source/diff inspection is not compiler or emitted-output proof. No CI was requested, rerun or awaited; this proposal neither establishes green CI nor waives the linter PR's failed acceptance gate.
