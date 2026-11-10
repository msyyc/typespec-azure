# Grouped difference analysis

## Difference index

All **398 finding projects** are accounted for below. The other 89 both-zero projects are matching population controls, not differences. [Complete project accounting](project-accounting.md) links the per-project numbers; [assessment.json](assessment.json) retains each project's source diagnostic target, exact reference-filename subgroup and representative saved schema path/value. Recoverable observations retain every original finding.

These are observed Swagger / TypeSpec counts in the same project group, **not counts attributed to the same underlying check**. Comparable violation counts are unassessed throughout: the reference checker and source-selection/configuration checker lack a verified common semantic identity.

| Difference                                                                                        | Projects | Swagger findings | TypeSpec findings |
| ------------------------------------------------------------------------------------------------- | -------: | ---------------: | ----------------: |
| [Outdated selection versus reference occurrences](#reference-occurrences-versus-source-selection) |      381 |           64,960 |               381 |
| [Existing configuration check](#existing-configuration-check)                                     |        7 |              709 |                 7 |
| [Filename-map policy](#filename-map-policy)                                                       |        5 |                7 |                 0 |
| [Deprecated location parameter](#deprecated-location-parameter)                                   |        3 |                7 |                 0 |
| [Explicit legacy identity](#explicit-legacy-identity)                                             |        1 |                2 |                 0 |
| [Authored suppression](#authored-suppression-and-configuration-precedence)                        |        1 |              101 |                 0 |
| **Total**                                                                                         |  **398** |       **65,786** |           **388** |

The index is exhaustive even where raw counts happen to equal one: equality does not erase the difference in semantic unit. No TypeSpec-only project was observed. Recommended actions below are recommendations, not authorization to change frozen specs, expand this rule, retire unapproved behavior, or fix the Swagger linter.

## Rule and report reconciliation

| Dimension                        | Historical Swagger baseline                                                                          | Fresh TypeSpec comparison                                                                                                                                     |
| -------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mapping                          | `LatestVersionOfCommonTypesMustBeUsed`                                                               | Existing `arm-common-types-version`, including distinct `outdated` and default configuration messages                                                         |
| Registration / audience          | ARM Spectral warning; unresolved OpenAPI 2; `$..['$ref']`; no RPaaS/staging-only selection indicated | Warning; ARM provider service guard; existing enabled library preset                                                                                          |
| Predicate                        | Common-types reference regex, then exact filename/version lookup                                     | Registry newest selection, effective member-over-namespace selection, last API member in declaration order; configuration predicate still checks every member |
| Finding unit                     | Emitted reference occurrence, including reused references and input associations                     | Source selection or service namespace                                                                                                                         |
| Source                           | Frozen specs `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`                                              | Same frozen specs commit                                                                                                                                      |
| Population                       | 487 successful ARM projects / 649 Swagger documents                                                  | All 487 selected/assessable projects; zero failed/unassessed                                                                                                  |
| API policy                       | Historical selected emitted API per project, retained in observations                                | Unprojected source; latest member for outdated guidance, all members for explicit configuration                                                               |
| Activation                       | Production ARM registration                                                                          | Explicit comparison activation; authored source suppression retained                                                                                          |
| Actual defaults                  | Not a TypeSpec default-policy observation                                                            | 379 warnings versus 388 explicit comparison warnings; all nine differences are recorded authored config disables                                              |
| Raw findings / finding projects  | 65,786 / 398                                                                                         | 388 / 388                                                                                                                                                     |
| Same-project overlap / one-sided | 388 overlap / 10 Swagger-only                                                                        | 388 overlap / zero TypeSpec-only                                                                                                                              |

Pinned original [implementation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/latest-version-of-common-types-must-be-used.ts), [filename map](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/utils.ts#L3-L14), [registration](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/az-arm.ts#L1105-L1118) and [documentation](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/latest-version-of-common-types-must-be-used.md) establish the upstream contract. Its regex admits `/common-types/resource-management/v\d+/\w+.json#`; it does not inspect a source service's selected default.

The current comparison does not reproduce an unrelated historical gist or `coverage_old.md` claim. Those reports are **not applicable** to this frozen-baseline recovery; their population/category/coverage percentages are not used. The required concrete reports here are the retained baseline rule shard and the fresh run's `coverage.json` / `coverage.md`; their numerical contents are preserved in portable observations, [run.json](run.json), [raw receipt identities](raw-receipts.json) and the independently checked [numerical report](numerical-replay.json).

The historical producer used a different Azure/core/compiler/emitter closure. [run.json](run.json) retains its artifact hashes and current identities; the descriptor pins the historical producer. Current compilation success across 487 projects establishes the recorded compatibility check, not identical historical/current emitter behavior. No Swagger was regenerated. The baseline represents its historical evaluation time, not a claim about a newly executed Swagger linter.

## Reference occurrences versus source selection

**Classification:** count-only and semantic-unit difference across 381 projects. **Observed:** 64,960 Swagger reference findings versus 381 TypeSpec `outdated` warnings. Every project has one saved TypeSpec warning; [assessment.json](assessment.json) preserves its exact source file, line, column and message and every independently observed reference-file subgroup. No reference subgroup is assigned that one warning as a fabricated per-file native count.

The saved TypeSpec messages select registry `v6` instead of `v5`, `v3` or `v4`; the registry supplies this version, not a production constant. Updating a latest source selection can affect many emitted schema/property/parameter references. Conversely, an individual explicit legacy reference can survive a compliant service selection. Repeated source/model names, shared message strings, or numeric equality are therefore not sufficient correspondence.

**Coverage status:** the latest-selection predicate is covered by focused/injected controls and observed diagnostics; full reference-check coverage remains outside the approved policy. Exact counterpart totals are unassessed.

**Recommended action and rationale:** service owners should evaluate upgrading the latest effective selection, including member overrides and compatibility impact. Do not modify historical API selections or add payload/reference traversal solely to match historical reference counts. That would expand issue 6007's approved scope and introduce noise/maintenance unrelated to this recovery.

### Source-backed outlier example: Network and SQL

The pinned Network service [selects namespace `v5`](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/network/resource-manager/Microsoft.Network/Network/Network/main.tsp#L159-L163):

```typespec
@armProviderNamespace
@service(#{ title: "WebApplicationFirewallManagement" })
@versioned(Versions)
@armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v5)
namespace Microsoft.Network;
```

Its last member is `v2026_03_01: "2026-03-01"`; the TypeSpec warning targets `main.tsp:197:3`: `Use the latest ARM common-types version 'v6' instead of 'v5'.` SQL likewise selects namespace `v5`; its last member is `v2026_08_01_preview: "2026-08-01-preview"`, with the same warning at `main.tsp:454:3`. See the exact source neighborhoods in recovered `source-footprints.json.gz`.

The saved Network `common.json` contains this exact `definitions.CommonResource.properties.systemData.$ref` value:

```json
{
  "$ref": "../../../../../../../../../../common-types/resource-management/v5/types.json#/definitions/systemData"
}
```

The Swagger linter reports that path across **19 input associations**: one reported origin and 18 `input-fallback` associations. SQL's `definitions.Advisor.allOf[0].$ref` similarly appears across **111 input associations**, one reported and 110 input-fallback, with its exact candidate document `databaseAdvisors.json`. These are reference observations, not 19 or 111 proven independent source-selection defects.

| Project | Swagger raw |                 File-independent paths | TypeSpec selection warnings |
| ------- | ----------: | -------------------------------------: | --------------------------: |
| Network |      23,619 | See exact per-project numerical report |                           1 |
| SQL     |       4,837 | See exact per-project numerical report |                           1 |

Both linters' findings are retained. The source selection and these emitted values support the multiplicity mechanism; they do not prove a complete source-to-emission defect map or attribute every emitted reference to that warning.

## Existing configuration check

**Classification:** distinct predicate, not matched reference warnings. **Observed:** seven TypeSpec namespace warnings in projects with 709 Swagger reference findings:

| Project           | Swagger findings | Configuration warnings |
| ----------------- | ---------------: | ---------------------: |
| CommunityTraining |               29 |                      1 |
| Fleet             |              183 |                      1 |
| ContainerStorage  |               66 |                      1 |
| IoTDataProcessor  |               69 |                      1 |
| IoTMQ             |              258 |                      1 |
| IoTOrchestrator   |               75 |                      1 |
| Astronomer        |               29 |                      1 |

For example, the pinned Community service [declares a versioned namespace without explicit common-types configuration](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/communitytraining/resource-manager/Microsoft.Community/Community/main.tsp#L15-L24):

```typespec
@armProviderNamespace("Microsoft.Community")
@service(#{ title: "Microsoft.Community" })
@versioned(Versions)
namespace Microsoft.Community;
```

The observed TypeSpec warning targets `main.tsp:18:21`: `Specify the ARM common-types version using the @armCommonTypesVersion decorator on the service namespace or on each version of the service version enum.` The saved Swagger finds references to default-emitted `v5` common types, not the absence of the decorator. [assessment.json](assessment.json) retains exact reference values and paths for each project.

**Coverage status:** unchanged explicit-configuration behavior is covered, including a historical member gap; the rule returns before outdated guidance when this predicate fails. These seven warnings are **not** migrated-reference counterpart credit. All seven have authored project config disables; their actual-default target count is zero. [default-activation.json](default-activation.json) retains exact config sections and source hashes.

**Recommended action and rationale:** service owners should explicitly configure the namespace or every API member, then separately assess latest selection. Preserve the existing missing-configuration message, target and precedence; adding a second implicit-default outdated warning would be noisy and contrary to the approved requirement.

## All ten Swagger-only projects

Each project below has **zero observed TypeSpec target warnings**, after source suppression. [One-sided examples](one-sided-examples.md) provide the exact frozen source excerpts, selected emitted API, every reference-file subgroup, diagnostic path, and emitted `$ref` value. No unsuppressed real-service result is inferred.

### Filename-map policy

| Project            | Swagger findings | TypeSpec warnings | Saved reference filename                |
| ------------------ | ---------------: | ----------------: | --------------------------------------- |
| Communication      |                2 |                 0 | `v6/networksecurityperimeter.json`      |
| AKS                |                1 |                 0 | `v6/managedidentitywithdelegation.json` |
| Cosmos DB          |                1 |                 0 | `v6/networksecurityperimeter.json`      |
| PlatformValidation |                1 |                 0 | `v6/mobo.json`                          |
| Search             |                2 |                 0 | `v6/networksecurityperimeter.json`      |

**Cause:** all five select common types `v6` effectively. The pinned Swagger map requires **`v5`** for these three filenames and compares exact version equality, so it warns on their actual emitted `v6` references. The TypeSpec linter instead accepts the registry's newest selection.

**Coverage status:** approved registry-selection boundary, not a missing latest-selection check. The implementation and saved diagnostics establish the mechanism, but do not by themselves establish that the Swagger policy is a bug or authorize its retirement.

**Recommended action and rationale:** seek an upstream filename-policy decision before changing that map or downgrading services. Do not hardcode a filename/version exception into this TypeSpec rule; no additional production check is justified by these observations.

### Deprecated location parameter

| Project                   | Swagger findings | TypeSpec warnings |
| ------------------------- | ---------------: | ----------------: |
| AzureResilienceManagement |                1 |                 0 |
| EventGrid                 |                4 |                 0 |
| HybridCompute             |                2 |                 0 |

**Cause:** each latest API effectively selects `v6`, but the emitted `LocationParameter` references `v5/types.json#/parameters/LocationParameter`. AzureResilienceManagement demonstrates member `v6` overriding a namespace `v5` default. HybridCompute has historical `v3` members followed by latest stable `v6`; its older declarations do not justify a latest-selection warning.

The candidate's unchanged deprecated `CommonTypes.LocationParameter` registers only through `v5`:

```text
  @armCommonParameter("LocationParameter", Azure.ResourceManager.CommonTypes.Versions.v3)
  @armCommonParameter("LocationParameter", Azure.ResourceManager.CommonTypes.Versions.v4)
  @armCommonParameter("LocationParameter", Azure.ResourceManager.CommonTypes.Versions.v5)
```

Source: `packages/typespec-azure-resource-manager/lib/parameters.tsp:35-37` in the assessed source overlay/base tree. The supported `LocationResourceParameter.location` registration includes `v6` in `lib/common-types/types-ref.tsp:549-569`. The original Swagger linter correctly observes the older reference according to its filename policy; a compliant service selection alone does not remove every legacy reference.

**Coverage status:** approved selection-versus-reference boundary, with the member-overrides-default behavior independently tested. **Recommended action and rationale:** separately evaluate supported location-parameter authoring and API compatibility. Do not extend the linter into deprecated payload/reference traversal or silently alter service contracts in this recovery.

### Explicit legacy identity

RedisEnterprise has **2 / 0** findings. Its namespace selects `v6`, while two authored model spreads explicitly use `Azure.ResourceManager.Legacy.ManagedServiceIdentityV4Property`, each with an existing `no-legacy-usage` suppression. The legacy model binds `ManagedServiceIdentity` to `v4/managedidentity.json`; both saved references retain that version.

**Coverage status:** approved source-selection boundary; the existing owning legacy-usage policy, rather than a new common-types payload checker, addresses this authoring surface. **Recommended action and rationale:** service owners should evaluate legacy identity compatibility and its suppressions separately. Do not claim two missing latest-selection warnings or change frozen contracts to satisfy counts. [Both exact model excerpts and references](one-sided-examples.md#redisenterprise).

### Authored suppression and configuration precedence

DatabaseWatcher has **101 / 0** findings. The namespace carries an authored `arm-common-types-version` suppression. Its historical `2023-09-01-preview` member lacks explicit configuration, while later members explicitly select `v5`. The unchanged all-version predicate therefore reaches the missing-configuration branch and returns before outdated guidance; the namespace suppression applies there. Its reference subgroups include `v5/types.json` and explicit `v4/managedidentity.json`; exact subgroup counts are in [the source/schema example](one-sided-examples.md#databasewatcher).

**Coverage status:** existing suppression/configuration behavior, not an absent owning check. The observed real service result is zero. No unsuppressed real-service compilation was performed or claimed; the missing-gap and suppression predicates are verified independently by the injected controls.

**Recommended action and rationale:** service owners should review explicit configuration and compatibility suppressions independently. Do not remove suppression in the comparison, attribute a predicted warning as an observed result, or weaken historical-gap precedence.

## Outliers and originating-document limits

Every saved finding underwent exact JSON-path lookup. **42,054** values resolved in the recorded source/input document; **23,732** lookups lacked an exact originating-document/path value and were investigated across only the project's recorded emitted documents:

| Project       | Missing-origin raw associations | Distinct exact paths |
| ------------- | ------------------------------: | -------------------: |
| Network       |                          21,187 |                1,866 |
| SQL           |                           2,530 |                   23 |
| Portal        |                              10 |                    5 |
| BatchPricings |                               5 |                    5 |

Every missing-origin group has exactly one candidate among its project's recorded emitted documents, all pointing to `v5/types.json`. This source-backed candidate search explains the available value and repeated-input mechanism; it **does not recover the original originating-document attribution**. Original `sourceAttribution`, `validatorInputFile` and `sourceDocuments` remain untouched. Candidate documents, values and all input associations are retained in recovered `ambiguous-reference-inspection.json.gz`.

The two conservative Swagger identities are `(rule, project, Swagger file, JSON path)` and `(rule, project, JSON path)`; the TypeSpec identity is `(rule, project, source file, line, column)`. Their totals are 59,546 / 42,052 versus 388. Raw occurrence multiplicity is not silently discarded, and these different domains cannot be normalized into equivalent defects.

**Coverage status:** all project/reference observations and missing-origin groups are accounted for; exact reference-to-source violation correspondence remains unassessed. **Recommended action and rationale:** retain these honest attribution limits. A future requirement for exact per-reference counterparts needs independently tested source/emission identity, not fuzzy names, guessed origins, or another unbounded corpus rerun.

## Actual activation versus explicit comparison

Nine project configs disable this rule with reason `"New rule"`: CommunityTraining, Fleet, ContainerStorage, IoTDataProcessor, IoTMQ, IoTOrchestrator, Astronomer, PlaywrightTesting and ServiceNetworking. The explicit comparison produces 388 warnings; their actual-default compilation produces 379. [default-activation.json](default-activation.json) retains all nine exact configuration sections, file hashes, messages and per-mode counts.

This is not evidence that the official preset disables the rule: the original policy remains enabled, and an injected resource-manager preset control produces its warning. The comparison removes config disables in memory only, retaining authored source suppressions; no source config was rewritten. Recommendations to service owners are separate from observed diagnostics under their current configuration.

## Scoped decision

The evidence supports the approved latest-selection/configuration recovery, **not full functional equivalence to the Swagger reference checker**. There is no unexplained project-count residual. Source/emission defect correspondence and comparable coverage percentages remain unassessed; broader reference checks are deliberately outside the approved scope, not silently reported as migrated. No additional production rule change is recommended by this assessment.
