# XmsClientName supporting evidence

## Assessment boundary

The user selected a native SDK naming requirement: report an explicit
`@clientName` application only when removing that application changes neither
effective SDK spelling nor relevant exact-name policy in any affected scope.
This is not a request to recreate extension-text equality.
The [claim map](claim-map.json) records the singleton mapping, excluded warning
registrations, tests, controls and execution limits.

The source is the temporary immutable candidate
`d065102fa52bf69b680f08016fc049d7185b7c22`, above canonical base
`9024f28739650a92c05465c8318fc08bc17a48cc`, with core
`41e2a4e70f0ea49ee52fa9d0d6d3d9c698c6ac08`.
Canonical native commit `c06d3a4a7ed1bb2cb417c76c6348624472c0c3ad` is pushed.
Its complete tree equals the assessed snapshot tree, including all 16 reviewed
task-file bytes. The local snapshot remains the assessment/recovery identity.

No blanket functional equivalence is supported. Strict Swagger extension
equality and SDK no-effect analysis are different predicates and use different
diagnostic units. The measured ARM population does not establish full SDK
customization or data-plane coverage.

## Original Swagger linter

The combined
[`XmsClientName` implementation](https://github.com/Azure/azure-openapi-validator/blob/405e6f094fa8280e05af23327845f6202a8edc65/packages/rulesets/src/spectral/functions/Extensions/xms-client-name.ts)
uses strict case-sensitive equality. Under a path containing `parameters`, it
compares `x-ms-client-name` with the object's `name`. Otherwise it compares with
the final resolved property key.

The actual common registration selects descendants of `paths` and `x-ms-paths`,
runs on resolved objects, and reports errors. It is not RPaaS-only.
The separate `XmsClientNameParameter` and `XmsClientNameProperty` warnings are
not migration members. See the retained
[production registration](receipts/production-rule-registration.json).
Function-valued registration fields cannot be represented by plain JSON;
the pinned implementation link is the code authority.

The sealed baseline's selected rule shard is absent. This is reconciled as
**zero observed production findings**, not unevaluated staging behavior:
the rule is registered in the production common ruleset, both TypeSpec disable
flags are false in the pinned catalog, and all 490 producer projects compiled
and validated successfully. The producer used openapi-validator 2.2.4 and
rulesets 2.2.6. See
[selected baseline observations](receipts/baseline-selected-observation.json).
No Swagger was regenerated for this task.

## Native semantic checks

### SDK fallback, scopes and exact policy

The rule uses the same scoped decorator storage, scope parser and SDK name
resolver as TCGC. It counterfactually omits one semantic decorator application;
it does not mutate the Program, infer a scope grammar, inspect emitted Swagger
or simulate AutoRest.

The comparison preserves real and case-only renames, meaningful scoped resets,
and meaningful exact-name markers. An encoded wire-name difference does not
make an ineffective SDK override useful. Canonical rule tests cover parameter
and property targets, multi-scope effects, negation, scope-option objects,
template arguments and independently authored augmentations.

The actual packed controls are
[property](controls/redundant-property/output.json),
[parameter](controls/redundant-parameter/output.json),
[compliance and real/case-only renames](controls/compliant-and-real-case-renames/output.json),
[wire independence](controls/wire-name-independence/output.json),
[scope replay](controls/scoped-repeat-and-reset/output.json), and
[exact policy](controls/exact-policy-effect-and-repeat/output.json).
Their inputs and full ambient diagnostics are retained beside the outputs.

### Friendly fallback and dependent naming

An independent source reviewer found that checking only the decorated
property's final name was insufficient. A direct `@friendlyName` consumer
substitutes the source property's client override, not its final friendly name.

The new discriminating regression uses this supported authored source:

```typespec
model Source {
  @clientName("renamed")
  @friendlyName("renamed")
  original: string;
}
model Result {
  @friendlyName("{name}", Source.original)
  value: string;
}
```

Without `@clientName`, `Source.original` still has the friendly name `renamed`,
but `Result.value` changes from `renamed` to `original`. The override must remain.
The correction inspects actual direct friendly-template consumers during the
same semantic traversal. It does not add a speculative dependency graph.

The public resolver tests cover default source-client-name substitution,
`use-client-name-for-friendly-name-source=false`, context isolation, other
placeholders, and copied friendly-name metadata. The emitter-independent lint
uses the default TCGC naming context; it cannot represent every emitter option
at once. Existing SDK contexts keep their supported option behavior.

The actual packed
[dependent-name control](controls/dependent-friendly-effect/output.json)
reports zero target warnings. The
[fallback control](controls/friendly-fallback/output.json) reports the two
ineffective non-exact overrides while preserving the meaningful exact policy.
The retained reviewer verified the corrected 16-file source manifest and found
no significant remaining source issue. The retained independent artifact/report
review also passed after correcting the payload-file accounting below.

### Authored targets and suppression

A decorator shared through inheritance, spread or template instantiation has
one removable authored target only when every evaluated use is unaffected.
An independently authored redundant application remains a separate warning.
The [packed copy control](controls/authored-copy-count/output.json) reports two
warnings, not one warning per copy.

The registered rule honors authored suppressions.
The [packed suppression control](controls/authored-suppression/output.json)
reports zero target warnings for its intentionally suppressed violation.
This focused control is not an exhaustive corpus-wide pre-suppression capture.

## Activation and actual artifacts

The three central presets keep the rule disabled:
[data-plane](controls/preset-data-plane/output.json),
[resource-manager](controls/preset-resource-manager/output.json), and
[client-sdk](controls/preset-client-sdk/output.json).
Each original configured compilation reports zero target warnings; each
explicitly activated comparison reports one. Ambient warnings remain in the
receipts. The TCGC C# best-practices ruleset does not add the new rule.

The compiler-synthesized
[library all preset](controls/library-all-activation/output.json) reports one
target warning in both the original and explicitly activated compilations.
No custom per-rule all exclusion was added.
The target-only
[positive](controls/target-only-positive/output.json) and
[compliant](controls/target-only-compliant/output.json) controls report one and
zero warnings and explicitly mark default activation unassessed.

The package closure contains six Azure packages and nine core packages.
[The artifact inventory](receipts/candidate-artifact-inventory.json)
binds all 15 tarballs. Their 2,919 total payload files comprise 2,904 non-manifest
files that match the clean snapshot bytes and 15 separately verified package
manifests with intentional publish-time transformations. The manifests are
excluded from source-byte equality. The inventory's `files` arrays include those
manifests; `nonManifestPayloadBytesMatchSnapshot` applies only to the 2,904
non-manifest files. Publish-time manifest dependency substitutions are recorded
separately.
[The snapshot receipt](receipts/candidate-snapshot-2.json) binds all 16 reviewed
working files and committed blobs, 3,618 reused prepared build files, and 43
dependency junctions. Reused build output was checksummed, not silently rebuilt
or relabeled as an unmodified base build.

[Actual injected identities](receipts/injected-loaded-identities.json) verify
all 15 public entrypoints, artifact membership and shared compiler identity.
Worker receipts also retain their actual loaded package paths, versions and
entrypoint hashes. The published copies replace machine-specific path prefixes,
not diagnostic targets or counts.

## Validation and recovery history

The required profile is the user's explicit **changed test files only** scope:
all cases in the three changed TCGC files and the one changed rulesets file.
TCGC passed 63/63 with the specifically approved `--maxWorkers=1` profile;
rulesets passed 22/22. Neither run skipped cases.
The ordinary test and hook limits stayed 10000 ms.
See the [profile](receipts/changed-test-validation-profile.json),
[passing diagnostic receipt](receipts/user-approved-test-diagnostic-1.json),
[TCGC output](receipts/changed-test-tcgc-user-diagnostic-1.txt), and
[rulesets output](receipts/changed-test-rulesets.txt).

The earlier five-file 118-case mixed-timeout run and the later default-concurrency
63-case mixed-timeout run remain **failed historical attempts**:
[original output](receipts/early-focused-final-corrected.txt) and
[changed-file output](receipts/changed-test-tcgc.txt).
The timeout cause remains unproven. A later pass is not a diagnosis of the
earlier failures. Unchanged sibling and full owning-package suites were omitted
under the superseding user scope, not reported as passing.

Package/root type-aware lint, formatting, spelling, affected builds and required
documentation generation passed at unchanged source hashes. Root lint first
failed because playground `vite/client` types were missing. A frozen filtered
ignore-scripts restore repaired that prerequisite; the same full root lint then
passed. See [the passed lint receipt](receipts/static-root-lint-2.txt).
Final documentation example source hashes exactly match the actual compiled
ARM snippets with expected one/zero target warnings:
[example reuse proof](receipts/static-doc-example-reuse.json).

The portable injected suite passed 37 applicable controls. Six controls for
an unrelated absent `resource-group-path-parameter` rule were declared
inapplicable before execution and skipped with the documented selector.
They are not passes. See
[portable output](receipts/portable-injected-controls.txt).
All 16 selected-rule controls passed without skips:
[manifest](controls/controls.json) and [summary](controls/summary.json).

The first snapshot checkout failed before source overlay because inherited
`submodule.recurse=true` reached an uninitialized `core`. The partial snapshot
was preserved. The original helper lost Git's child stderr; it remains lost.
Read-only object/path/space and checkout-boundary evidence supported the
coordinator-approved sequencing correction. A distinct snapshot disables root
checkout recursion, then initializes the verified local core in the right order.
The corrected helper saves output and exit metadata before raising.
See [failed output](receipts/snapshot-preparation.txt) and
[corrected output](receipts/snapshot-preparation-corrected-2.txt).

Current inherited counters are ordinary corrections **10/10**, coordinator
reserve **8/10**, replacement worker **1/1**, and explicit user diagnostic
**1/1**. Automatic timeout and hook diagnostics remain zero.
No allowance was reset by a phase or scope change.

## Population and diagnostic differences

The fresh full comparison completed successfully for all 490 frozen ARM projects
and 652 retained Swagger inputs, with no compile, worker or unassessed failures.
It observed zero Swagger linter findings and 141 TypeSpec linter findings
across 32 projects. All 141 raw source locations are classified
exactly once in the complete [grouped differences](grouped-differences.md).
The representative examples below supplement, but do not replace, that full
project/target inventory.

The independent [saved-observation recount](receipts/saved-observation-reanalysis.json)
agrees with the original report on selected/assessable populations, all raw and
aligned counts, conservative source keys and both directional excess sums.
The declared source profile filters no captured target warnings; emitted
latest-version and unprojected source populations remain different.
Configured corpus diagnostics are not an exhaustive pre-suppression total.
The full target-only run does not assess default activation.
All worker-recorded candidate package entrypoint hashes and versions match
the payload-verified injected identities; compiler and TCGC are present in
every project receipt. Ambient diagnostics are retained, not silently filtered.

### Grouped difference evidence

The groups below use exact authored targets, not matching names alone.
Counts remain individual warnings. Grouping does not establish equivalent
defects. The saved [source facts](receipts/one-sided-source-facts-final.json) retain
source-file hashes, complete excerpts and exact retained Swagger pointers.
The historical gist and legacy coverage report are not inputs to this fresh
artifact assessment; their populations and row reconciliation are not applicable.

#### Advisor: older-version source

- **Classification:** TypeSpec-linter-only.
- **Status:** population mismatch; retained in the declared source profile.
- **Project/API version:** `Microsoft.Advisor/Advisor` / `2026-10-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 3.

The three exact source applications are:

| Source in `client.tsp` | Target                                                              | Version boundary                           |
| ---------------------- | ------------------------------------------------------------------- | ------------------------------------------ |
| 21–24                  | `ResourceRecommendationBases.patch::parameters.properties`          | `patch` removed at `v2026_02_01_preview`   |
| 32                     | `AssessmentResults.put::parameters.resource`                        | interface removed at `v2026_10_01`         |
| 33–36                  | `TriageRecommendations.rejectTriageRecommendation::parameters.body` | interface removed at `v2026_03_01_preview` |

For example, the pinned
[operation source](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/ResourceRecommendationBase.tsp#L41-L50)
contains:

```typespec
@added(Versions.v2025_05_01_preview)
@removed(Versions.v2026_02_01_preview)
@patch(#{ implicitOptionality: false })
patch is ArmCustomPatchSync<
  ResourceRecommendationBase,
  PatchModel = TrackedRecommendationPropertiesPayload,
  BaseParameters = Azure.ResourceManager.Foundations.ExtensionBaseParameters,
  Error = ArmDefaultErrorResponse
>;
```

Its source override repeats `trackedProperties` already applied with `!csharp`.
The other two targets similarly repeat `assessmentContract` and
`recommendationRejectBody`. All three warnings were captured from the
unprojected source. None of these authored operations belongs to the selected
latest-version Swagger. A newer `update` operation reuses the first route but
has a different authored operation and payload; that route is not correspondence.

**Coverage status:** the source no-effect check is exercised; same-version
Swagger correspondence is absent for these targets. There is no meaningful
selected-version Swagger object to quote for a removed operation.

**Gap analysis and decision:** retain all three raw source observations.
Do not filter warnings by source filename or equate them with a missing Swagger
check. Service owners can assess source cleanup separately. A same-version
semantic comparison would need a supported projected-program profile, not
count normalization; none is claimed here.

#### Advisor: body-name application collapse

- **Classification:** TypeSpec-linter-only.
- **Status:** source/emission representation difference.
- **Project/API version:** `Microsoft.Advisor/Advisor` / `2026-10-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 1.

The pinned [source application](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/client.tsp#L28-L31)
is:

```typespec
@@clientName(
  SuppressionContracts.create::parameters.resource,
  "suppressionContract"
);
```

`back-compatible.tsp:68–72` already applies the same name with `!csharp`.
TCGC's existing `applyScopedDecoratorData` preserves negated-scope state when
an unscoped entry is applied. Thus this common repeat does not restore a C#
name that would otherwise change. The rule uses that actual resolver behavior.

The retained exact operation is
`PUT /{resourceUri}/providers/Microsoft.Advisor/recommendations/{recommendationId}/suppressions/{name}`,
operation ID `Suppressions_Create`. Its body parameter is:

```json
{
  "name": "suppressionContract",
  "in": "body",
  "description": "The snoozed or dismissed attribute; for example, the snooze duration.",
  "required": true,
  "schema": { "$ref": "#/definitions/SuppressionContract" }
}
```

**Explanation:** the emitted name contains no `x-ms-client-name`. The Swagger
linter therefore does not select this object. One body name cannot preserve
the redundant source application.

**Coverage status:** observed source redundancy, not a missing implementation
of strict extension equality.

**Gap analysis and decision:** a service-owner cleanup may remove the redundant
common repeat while retaining effective scoped naming. Do not change the
TypeSpec predicate merely to obtain equal counts.

#### API Management: two applications, one emitted body name

- **Classification:** TypeSpec-linter-only.
- **Status:** source/emission representation difference.
- **Project/API version:** `Microsoft.ApiManagement/ApiManagement` /
  `2025-09-01-preview`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 2.

The exact same application appears independently at
[`back-compatible.tsp:966–969`](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/back-compatible.tsp#L966-L969)
and
[`1931–1934`](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/back-compatible.tsp#L1931-L1934):

```typespec
@@clientName(
  ApiManagementServiceResources.quotaByCounterKeysUpdate::parameters.body,
  "parameters"
);
```

The retained exact operation is
`PATCH /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/quotas/{quotaCounterKey}`,
operation ID `QuotaByCounterKeys_Update`. Its body parameter is:

```json
{
  "name": "parameters",
  "in": "body",
  "description": "The value of the quota counter to be applied to all quota counter periods.",
  "required": true,
  "schema": { "$ref": "#/definitions/QuotaCounterValueUpdateContract" }
}
```

**Explanation:** each source application is independently removable while the
other remains. Both raw warnings are retained. The emitted body name lacks
`x-ms-client-name`, so the Swagger linter reports none.

**Coverage status:** two captured no-effect applications; no asserted
two-defect correspondence or duplicate-pair normalization.

**Gap analysis and decision:** remove at most one duplicate, then reassess.
The remaining rename is meaningful. Deleting both applications at once would
change the SDK name and is not the proposed cleanup. The service owner must
approve any source edit; this task leaves frozen specs unchanged.

#### ContainerApps: scoped repeat of a meaningful case-only rename

- **Classification:** TypeSpec-linter-only.
- **Status:** SDK-scope versus emitted-extension policy difference.
- **Project/API version:** `Microsoft.App/ContainerApps` / `2026-07-01`.
- **Observed counts:** Swagger linter 0; TypeSpec linter 1.

The pinned [source application](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/app/resource-manager/Microsoft.App/ContainerApps/client.tsp#L1189)
is:

```typespec
@@clientName(ScheduledEntries.scheduledEntries, "ScheduledEntries", "csharp");
```

`back-compatible.tsp:334` already applies `"ScheduledEntries"` without a
language scope. The retained exact Swagger object
`definitions.ScheduledEntries.properties.scheduledEntries` is:

```json
{
  "type": "array",
  "description": "List of maintenance schedules for a managed environment.",
  "items": { "$ref": "#/definitions/ScheduledEntry" },
  "x-ms-client-name": "ScheduledEntries",
  "x-ms-identifiers": []
}
```

**Explanation:** `scheduledEntries` is not strictly equal to `ScheduledEntries`.
The Swagger linter correctly reports no extension-equality finding. It cannot
observe the extra C# source application. The TypeSpec linter reports that scoped
repeat, not the meaningful common case-only rename.

**Coverage status:** observed scoped no-effect check with a preserved real
rename; this is not literal Swagger parity.

**Gap analysis and decision:** the service owner may remove only the scoped
repeat. Preserve the common case-only rename. No TypeSpec rule edit is proposed
for this difference.

## Publication and replay boundary

The native source is committed and pushed at
`c06d3a4a7ed1bb2cb417c76c6348624472c0c3ad`; staged and committed bytes
matched the reviewed source and complete assessed snapshot tree.
The independent source and artifact/report reviews passed.
The candidate package/source archive was prepared after full-run completion.
Durable evidence and release publication, verified download round trip, fresh
published evidence recovery, native PR, separate A/B review checkpoints,
integration and CI remain subsequent gates.
See [recovery instructions](recovery.md). Saved-count reanalysis is not a full
native rerun or migration acceptance.
