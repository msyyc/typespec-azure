# EnumInsteadOfBoolean -> Azure Core no-boolean

## Conclusion

**The current official rule is not fully functionally equivalent to the Swagger
validator.** Ordinary boolean properties, parameters and direct bodies are
covered. Compiled controls expose five authorable boolean shapes that the
validator flags but the native rule does not: boolean literals, nullable booleans,
derived boolean scalars, array items and dictionary values.

This analysis does not change the official rule or enable it in production.
Matching project sets or conservative source-location counts do not override
these predicate differences. A warning count is not automatically a count of
distinct authorable defects.

## Mapping and frozen inputs

| Field                  | Recorded value                                                                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Original validator     | `EnumInsteadOfBoolean`                                                                                                                            |
| Official native rule   | `@azure-tools/typespec-azure-core/no-boolean`                                                                                                     |
| Original native PR     | [Azure/typespec-azure#5265](https://github.com/Azure/typespec-azure/pull/5265), merged but disabled in the production ARM and data-plane rulesets |
| Candidate policy       | Resolve canonical `main` once, then freeze                                                                                                        |
| Candidate commit       | `03f2dc50e5da5e0da7109fed00ffabfbfcd1da47`                                                                                                        |
| Candidate core gitlink | `50240c7db77895b261ab2a511f7f79e5650db59b`                                                                                                        |
| Specs policy           | Resolve canonical `typespec-next` once, then freeze                                                                                               |
| Specs commit           | `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`                                                                                                        |
| Comparison tooling     | `5e590b8bcb87adf33567911f19778623e18a4c45`, in [Azure/typespec-azure#5775](https://github.com/Azure/typespec-azure/pull/5775)                     |
| Native alignment       | `boolean-http`; selected-version HTTP metadata plus default-emitted service schemas, not emitted-name matching                                    |
| Audience               | Production ARM Swagger validator selection; native rule explicitly enabled only for analysis                                                      |
| Options                | Native rule enabled with its configured options; authored source suppressions retained                                                            |
| Version policy         | Latest emitted API version per discovered project                                                                                                 |
| Swagger suppressions   | Readme suppressions are not applied                                                                                                               |
| Discovery              | `main.tsp` plus `tspconfig.yaml` whose text contains `typespec-azure-rulesets/resource-manager`                                                   |
| Runtime                | Node `26.5.0`; candidate pnpm `11.10.0`; specs pnpm `12.6.0`                                                                                      |

The selected candidate contains the merged #5265 implementation. The matching
compiler, libraries, emitter and official lint packages were built from this
candidate and its actual core gitlink, not independently chosen registry
versions. Package versions alone are not source identities: retained tarball
hashes and loaded-entrypoint hashes identify the actual artifacts.

Both official rulesets explicitly set `no-boolean` to `false`. The comparison
worker removes only conflicting configuration-level disables and explicitly
activates the mapped rule. Source suppressions remain effective. This separates
native capability from default production activation.

## Final full-corpus results

The final run completed successfully: all 487 discovered ARM projects compiled,
completed validator execution and completed native analysis. It emitted 649
Swagger files. No filter, limit or failure exclusion reduced the population.
The [full report](runs/full-4/coverage.md), [machine-readable report](runs/full-4/coverage.json)
and [independent count audit](runs/full-4/audit/count-audit.json) retain the
complete project inventory.

| Measure                                                 | Final observation |
| ------------------------------------------------------- | ----------------: |
| Selected / assessable / unassessed projects             |     487 / 487 / 0 |
| Swagger / native / overlapping affected projects        |   313 / 312 / 312 |
| Swagger-only / native-only projects                     |             1 / 0 |
| Swagger raw events                                      |             8,338 |
| Native raw / aligned findings                           |     4,823 / 4,680 |
| Swagger file-independent JSON paths                     |             4,269 |
| Native source-coordinate keys                           |             4,174 |
| Native findings under project defaults                  |                 0 |
| Projects with equal raw counts                          |               428 |
| Projects with Swagger-higher / native-higher raw counts |           21 / 38 |
| Sum of Swagger-higher / native-higher raw excess        |       4,037 / 379 |
| Sum of absolute per-project raw differences             |             4,416 |
| Projects with equal conservative location counts        |               450 |
| Conservative location excess, Swagger / native          |            95 / 0 |

The signed aggregate raw difference is 3,658, but it must not hide the
opposite-direction excesses. The [487-row CSV](runs/full-4/audit/project-counts.csv)
retains signed, absolute and relative differences per project. Relative
difference is `abs(SwaggerRaw - nativeAligned) / max(SwaggerRaw, nativeAligned)`;
both zero means zero. No numerical tolerance is used to accept a semantic gap.

The only one-sided project is the external-JSON `BatchPricingsAPI` example below.
All four previously false Migrate gaps now report Swagger 2 / native aligned 2.
There are no native-only projects. This is 99.68% observed affected-project
overlap, **not** 99.68% semantic equivalence.

The [exact-schema audit](runs/full-4/validator-schema-audit.json) verifies every
explicitly attributed event against its actual dataset document and JSON path:
4,269 Boolean schemas across 367 documents, with zero mismatches. The other
4,069 events lack usable source attribution and remain unassigned. The
attributed schemas include 46 nullable Boolean occurrences and one Boolean
dictionary-value occurrence. These shape signals overlap and are not an
invented count of native misses.

The 95-key conservative location deficit spans 37 projects. It is not a count
of 95 proven missing checks: JSON paths and source coordinates are different
domains. The report and CSV preserve every residual. Exact cross-engine
correspondence remains unestablished; no blanket per-project semantic
normalization or acceptance is claimed. The independent controls and real
nullable example already disprove strict equivalence, without guessing that
correspondence.

The final full baseline identity is:

```text
841c5181e93fb7be2444077e0e25165d49df73c06f456c1fa9171e33c2cb7365
```

## Semantic and activation evidence

The selected native package's five existing tests pass. They cover boolean
model properties, path parameters, request bodies, response bodies and compliant
extensible string unions. All 28 injected-runtime controls also pass. They
exercise the actually installed official packages, not the tooling checkout's
compiler.

The [frozen native implementation](https://github.com/Azure/typespec-azure/blob/03f2dc50e5da5e0da7109fed00ffabfbfcd1da47/packages/typespec-azure-core/src/rules/no-boolean.ts)
uses an exact standard-Boolean predicate. The
[validator implementation receipt](controls/validator-source.json) records the
actual installed production selector, function source and file hashes.

The additional [compiled source](controls/main.tsp) and
[configuration](controls/tspconfig.yaml) run through the selected AutoRest
emitter, the production ARM validator engine and the native worker. Compilation
and validator execution both succeed.

| Source shape                          | Emitted OpenAPI                               | Swagger target findings | Native aligned target findings |
| ------------------------------------- | --------------------------------------------- | ----------------------: | -----------------------------: |
| `plain: boolean`                      | `Widget.properties.plain.type: boolean`       |                       1 |                              1 |
| Delete-only `omitted: boolean` on GET | Property absent                               |                       0 |                              0 |
| `constant: true`                      | Boolean schema with `enum: [true]`            |                       1 |                              0 |
| `nullable: boolean \| null`           | Boolean schema with `x-nullable: true`        |                       1 |                              0 |
| `items: boolean[]`                    | Boolean `items` schema                        |                       1 |                              0 |
| `dictionary: Record<boolean>`         | Boolean `additionalProperties` schema         |                       1 |                              0 |
| `derived: DerivedFlag`                | Reference to boolean `DerivedFlag` definition |                       1 |                              0 |
| Extensible string `WidgetState`       | String schema                                 |                       0 |                              0 |
| **Total**                             |                                               |                   **6** |                          **1** |

The native raw receipt has two findings: `plain` and the non-emitted `omitted`
property. Alignment retains only `plain`; neither raw diagnostic is erased.
The default native target count is zero.

These are separate semantic checks, not a fuzzy matching of common property
names. The authored declarations, exact emitted schemas and validator JSON
paths are retained together.

The semantic controls were rerun with the final tooling commit, not only with
the first repair. To reproduce emission after preparing the injected specs
checkout, copy the two control source/configuration files into a new scratch
directory and link that directory's `node_modules` to the prepared specs
checkout. From the tooling checkout, run:

```powershell
mise exec -- <specs>\node_modules\.bin\tsp.cmd compile <scratch>\main.tsp `
  --config <scratch>\tspconfig.yaml `
  --option "@azure-tools/typespec-autorest.emitter-output-dir=<scratch>\swagger" `
  --warn-as-error=false

mise exec -- <specs>\node_modules\.bin\autorest.cmd --v3 --spectral `
  --azure-validator --semantic-validator=false --model-validator=false `
  --message-format=json --openapi-type=arm --openapi-subtype=arm `
  --use=<validator-extension-file-URI> `
  --input-file=<scratch>\swagger\2026-01-01.json
```

Resolve the extension file URI from
`<specs>\node_modules\@microsoft.azure\openapi-validator\`, not a newly fetched
validator version. The observation archive retains `controls/input.json` and
`controls/native.json`. Replace the input's scratch/specs roots with the local
paths, then run the worker:

```powershell
mise exec -- node packages\typespec-lintdiff\test\harness\native-coverage-worker.mjs `
  <input.json> <new-native-receipt.json>
```

### Gap example: boolean literal

- **Classification:** Swagger-only semantic check.
- **Status:** Unresolved production-rule difference.
- **Source/API version:** `controls/main.tsp`, `2026-01-01`.

```typespec
constant: true;
```

```json
{ "type": "boolean", "enum": [true] }
```

Swagger flags `definitions.Widget.properties.constant`. The native property type
is a Boolean literal, not the standard Boolean scalar.

### Gap example: nullable boolean

- **Classification:** Swagger-only semantic check.
- **Status:** Unresolved production-rule difference.
- **Source/API version:** `controls/main.tsp`, `2026-01-01`.

```typespec
nullable: boolean | null;
```

```json
{ "type": "boolean", "x-nullable": true }
```

Swagger flags `definitions.Widget.properties.nullable`. The native property type
is a union; the current rule does not unwrap it.

### Gap example: array item

- **Classification:** Swagger-only semantic check.
- **Status:** Unresolved production-rule difference.
- **Source/API version:** `controls/main.tsp`, `2026-01-01`.

```typespec
items: boolean[];
```

```json
{ "type": "array", "items": { "type": "boolean" } }
```

Swagger flags `definitions.Widget.properties.items.items`. The native rule
does not inspect model indexer values representing array items.

### Gap example: dictionary value

- **Classification:** Swagger-only semantic check.
- **Status:** Unresolved production-rule difference.
- **Source/API version:** `controls/main.tsp`, `2026-01-01`.

```typespec
dictionary: Record<boolean>;
```

```json
{ "type": "object", "additionalProperties": { "type": "boolean" } }
```

Swagger flags `definitions.Widget.properties.dictionary.additionalProperties`.
The native rule does not inspect dictionary indexer values.

### Gap example: derived boolean scalar

- **Classification:** Swagger-only semantic check.
- **Status:** Unresolved production-rule difference.
- **Source/API version:** `controls/main.tsp`, `2026-01-01`.

```typespec
scalar DerivedFlag extends boolean;
model Widget {
  derived: DerivedFlag;
}
```

```json
{
  "DerivedFlag": { "type": "boolean" },
  "Widget": {
    "properties": { "derived": { "$ref": "#/definitions/DerivedFlag" } }
  }
}
```

Swagger flags `definitions.DerivedFlag`. The native rule uses
`tk.scalar.isBoolean`, documented as checking exactly the standard Boolean
scalar, rather than the separate `extendsBoolean` predicate.

## Required TypeSpec rule changes

**A production rule update is required for complete Swagger-predicate parity.**
That update belongs in
`packages/typespec-azure-core/src/rules/no-boolean.ts`, with directly related
regressions in `test/rules/no-boolean.test.ts`.

The rule would need supported native handling for boolean literals, nullable
boolean unions, derived boolean scalars, array items and dictionary values.
Tests must include each violating shape and compliant string/enum equivalents.
Diagnostic targets and repeated use of shared types need an explicit native
contract; do not add duplicate diagnostics merely to equalize emitted counts.

Alternatively, the official rule can retain an intentionally narrower guideline,
but that is not full functional equivalence to the validator's blanket selector.
This analysis does not authorize or perform either production-policy change.

## Comparison-tool repair

Before the repair, a GET response containing a Delete-only boolean property
produced a native aligned finding even though the emitter omitted that property.
Reference-only parameters also need separate treatment from named parameter
models emitted as unused schemas.

Three negative runtime controls failed before the fix. Commit
`dcc3188a0643e9c8ba1018f486abe2f5d8d7ee44` fixes payload visibility/body-ignore
filtering and reference-only parameters. Positive controls retain ordinary
parameters, response headers, canonical shared schemas and explicit-body
metadata. All 23 runtime controls, 56 coverage unit tests, scoped strict
TypeScript, lint and formatting pass.

The first full-corpus attempt was deliberately stopped during compilation once
the independent control proved the alignment defect. Its incomplete data is
retained as aborted evidence, not counted as a completed run or reused baseline.
The frozen candidate and specs commits were not refreshed for the retry.

The next full run exposed two more comparison defects. It selected all 487
projects, but one validator invocation failed because a copied external
`pricings.json` referenced common types outside the project's output directory.
Four Migrate projects also appeared Swagger-only because the HTTP-only filter
dropped named schemas that AutoRest emits by default.

Commit `112ab7124800b620031626820421ad6dff8c8e49` preserves the bounded reference
closure and follows `omit-unreachable-types`. Two regression tests failed
before repair. Actual emitter controls then established that `Unused`, `Child`,
`Choice`, and `Query` schemas are emitted with the option off and omitted with
it on. The negative referenced-parameter control now explicitly uses the
omit mode; the default mode correctly retains the named `Query.flag` schema.
See [source](controls/emission-policy/main.tsp) and
[actual emitted definitions](controls/emission-policy/results.json).

Commit `5e590b8bcb87adf33567911f19778623e18a4c45` records validator source
attribution separately from invocation inputs. The validator can diagnose a
referenced document or omit its source attribution. Neither case permits
treating the invocation filename as an exact diagnostic target.
Five new provenance controls and all 56 existing coverage unit tests pass;
dataset tests total 13. Together with the 28 injected controls, the final
validation set has 97 passing tests. Scoped strict TypeScript, lint and
formatting also pass.

The stopped `full-3` attempt reached preparation only and is recorded as
aborted, not reused. The earlier completed-but-incomplete `full-2` remains
pre-repair evidence, not the final assessable population.

## Retained baseline reuse

The repaired eight-project pilot and its explicit baseline reuse both complete
successfully. They retain this same baseline identity:

```text
78499eec48bcce203bd45326002add358e100ea4a6257a8401918336a0d0dae0
```

The reuse run has no Swagger-generation/validation stage. It reruns installation
and native workers, and its complete coverage report text matches the original
pilot. This proves same-input local reuse for that scoped baseline, not
cross-machine cache compatibility or full-corpus reuse.

## Historical report reconciliation

Historical temporary-library reports are not inputs to this fresh
official-package comparison. This note does not import their populations,
projection policies or equivalence conclusions.

The earlier official eight-project pilot at candidate `d212c494...` and core
`cf8712b...` is also a different candidate closure. Its 20 Swagger findings,
26 raw native findings, 25 aligned findings and 20 native source locations are
scoped observations. Repeating those counts is not proof of the missing
literal, union, scalar-derivation or collection checks.

No aggregate-only historical gist is used as the source of the new project
inventory, failures or count totals.

## Real-service cardinality and projection examples

The largest raw-count outliers and the real nullable example retain these final
observations:

| Project                 | Swagger raw | Explicit source / unassigned | Native aligned | JSON paths / native coordinates |
| ----------------------- | ----------: | ---------------------------: | -------------: | ------------------------------: |
| SQL                     |       2,224 |                  134 / 2,090 |            157 |                       134 / 134 |
| Network                 |       2,190 |                  214 / 1,976 |            258 |                       214 / 211 |
| Billing                 |          75 |                       75 / 0 |            145 |                         75 / 75 |
| MachineLearningServices |          63 |                       63 / 0 |             60 |                         63 / 50 |

SQL and Network account for 4,066 of the 4,069 unattributed events. Their large
raw totals cannot be assigned to exact target files from invocation filenames.
The reference witness below demonstrates that failure mode. Billing's separate
compiler-object audit establishes native target multiplicity. Machine Learning
demonstrates a real missed nullable predicate even though its raw gap is only
three. These causes must not be collapsed into one count-equality test.

### Gap example: the largest native-higher outlier has distinct semantic targets

- **Classification:** Count-only; native semantic-target multiplicity.
- **Status:** Explained target cardinality; no production rule update required
  merely to reduce the warning total.
- **Project/API version:** `specification/billing/resource-manager/Microsoft.Billing/Billing`
  / `2024-04-01`.
- **Source:** `BillingAccount.tsp:392`, `BillingAccountsListParameters`.

```typespec
alias BillingAccountsListParameters = {
  @query("includeAll")
  includeAll?: boolean = false;
};
```

The emitted parameter at
`paths["/providers/Microsoft.Billing/billingAccounts"].get.parameters[1]`
includes:

```json
{
  "name": "includeAll",
  "in": "query",
  "required": false,
  "type": "boolean",
  "default": false
}
```

Billing has 75 raw Swagger findings and 145 raw/aligned native findings at
75 source locations. A separate compiler traversal verifies 145 distinct
property objects across 101 models. Their entire per-location multiplicity
map exactly matches all 145 native warnings. For example, `includeAll` occurs
in three distinct anonymous template-instance models at one authored location.
See [the complete target-object receipt](controls/billing-source-targets.json).

These are distinct semantic targets, not evidence that the native rule ran
three times on one object. The equal count of 75 JSON paths and source locations
still does not establish a cross-engine bijection or an actionable-defect
normalization.

### Gap example: reference traversal multiplies validator observations

- **Classification:** Count-only with missing per-event source attribution.
- **Status:** Preserve raw events; do not manufacture exact file-level identities.
- **Project/API version:** `specification/network/resource-manager/Microsoft.Network/Network/Network`
  / `2026-03-01`.

One validator invocation uses `applicationGateway.json`, but emits a finding at
`definitions.ConnectionMonitorHttpConfiguration.properties.preferHTTPS`.
That JSON path does not exist in the invocation input. A retained
[reference witness](controls/reference-witness.json) follows these exact edges:

```text
applicationGateway.json
  -> ./virtualNetwork.json#/definitions/PrivateLinkServiceConnectionState
  -> ./networkWatcher.json#/definitions/FlowLog
```

The reachable `networkWatcher.json` document contains:

```json
{
  "type": "boolean",
  "description": "Value indicating whether HTTPS is preferred over HTTP in cases where the choice is not explicit."
}
```

The engine supplies no source-document metadata for this event. The witness
explains reference-file evaluation, but is not used to assign every source-less
event or deduplicate actionable defects by property name.

This matters especially for SQL's 142 emitted files and Network's 19 files.
The pre-repair raw-file audit preserves all 8,336 events: 4,268 have an explicit
reported document and were verified against an actual Boolean schema at the
exact JSON path; 4,068 lack source attribution. The final run separately
records its own attribution totals. Invocation-plus-path counts must not be
called exact target-file counts, and equal file-independent paths do not
resolve this uncertainty.

### Gap example: template parameter targets share authored locations

- **Classification:** Count-only; native raw excess.
- **Status:** Explained semantic-target multiplicity; no production rule update
  required for this count difference.
- **Project/API version:** `specification/alertsmanagement/resource-manager/Microsoft.AlertsManagement/AlertsManagement`
  / `2025-05-25-preview`.
- **Source:** `Alert.tsp:195`, `Alert.tsp:201`, `Alert.tsp:319`,
  `Alert.tsp:325`, `routes.tsp:55`, `models.tsp:656`.

One parameter declaration is:

```typespec
@query("includeContext")
includeContext?: boolean;
```

The scoped operation emits one corresponding query-parameter occurrence:

```json
{
  "name": "includeContext",
  "in": "query",
  "required": false,
  "type": "boolean"
}
```

The full emitted parameter also retains its authored description. The exact
validator path is
`paths["/{scope}/providers/Microsoft.AlertsManagement/alerts"].get.parameters[11]`.

The project has six emitted Boolean occurrences: five query parameters and
`ActionStatus.isSuppressed`. Native reports eleven aligned semantic targets at
six authored locations. A separate compiler traversal verifies eleven distinct
property objects: ten template-instance parameters and the ordinary
`ActionStatus` property, across seven model objects. Each of the five parameter locations has two
native findings; the ordinary property has one. See
[the target-object receipt](controls/alerts-source-targets.json).

This explains the five-count native excess without property-name matching.
The six source coordinates remain a conservative summary, not proof that
eleven distinct semantic checks can always be normalized to six actionable
defects.

### Gap example: an older-version boolean is not emitted

- **Classification:** Raw source versus selected-version population.
- **Status:** Correctly excluded by alignment; no production rule update
  required for this difference.
- **Project/API version:** `specification/advisor/resource-manager/Microsoft.Advisor/Advisor`
  / `2026-08-01-preview`.
- **Source:** `models.tsp:749`.

```typespec
@removed(Versions.v2026_02_01_preview)
tracked?: boolean;
```

Native raw linting sees the historical declaration. The selected version is
after the removal, so the selected-version HTTP graph excludes it. The receipt
retains three raw findings and two aligned findings; Swagger has two Boolean
occurrences. No emitted `tracked` schema exists for the removed property in
this selected-version comparison.

### Gap example: unused schemas are emitted by default

- **Classification:** Comparison-filter defect, not a missing native predicate.
- **Status:** Fixed in `112ab7124800b620031626820421ad6dff8c8e49`.
- **Projects/API version:** `Microsoft.Migrate/{AKSAssessments,HeterogenousAssessments,MachineAssessments,WebAppCompoundAssessments}`
  / `2024-03-03-preview`.
- **Source:** `Common/StandardizedContracts/CommonModels.tsp:138,144`;
  MachineAssessments uses `Normalized Contract/StandardizedContracts/CommonModels.tsp`.

```typespec
model AppSvcNativeSettings {
  @doc("Gets or sets the isolation required.")
  isolationRequired: boolean;
}
```

```json
{
  "type": "boolean",
  "description": "Gets or sets the isolation required."
}
```

Every project emits Boolean properties at
`definitions.AppSvcNativeSettings.properties.isolationRequired` and
`definitions.AppSvcContainerSettings.properties.isolationRequired`. A compiler
probe verifies that both are ordinary project-defined standard Boolean
properties. Native raw linting already reported them. The old HTTP filter
incorrectly removed both because the models were not operation-reachable.

Default AutoRest emission still includes these named service schemas. The
repaired boolean profile follows that policy, while explicit
`omit-unreachable-types: true` retains the narrower graph. No production rule
change is required for this cause.

### Gap example: a real nullable Boolean is missed

- **Classification:** Swagger-only authorable semantic check.
- **Status:** Production rule update required for strict predicate parity.
- **Project:** `specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/MachineLearningServices`.
- **Selected API version:** `2026-09-01`.
- **Source:** `models.tsp:4415`, `Docker.privileged`.

```typespec
model Docker {
  ...Record<unknown>;
  #suppress "@azure-tools/typespec-azure-core/no-nullable" "Existing API contract allows null values"
  privileged?: boolean | null;
}
```

The emitted schema at `definitions.Docker.properties.privileged` is:

```json
{
  "type": "boolean",
  "description": "Indicate whether container shall run in privileged or non-privileged mode.",
  "x-nullable": true
}
```

The authored suppression targets `no-nullable`, not `no-boolean`. The current
native Boolean rule rejects this union at its exact-standard-scalar predicate.
The compiled nullable control independently reproduces the difference. This is
not explained by count deduplication or namespace reachability.

### Gap example: a real Boolean dictionary value is missed

- **Classification:** Swagger-only authorable semantic check.
- **Status:** Production rule update required for strict predicate parity.
- **Project/API version:** `specification/purview/resource-manager/Microsoft.Purview/Purview`
  / `2024-04-01-preview`.
- **Source:** `models.tsp:1219-1225`, `BatchFeatureStatus.features`.

```typespec
#suppress "@azure-tools/typespec-azure-resource-manager/arm-no-record" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
@visibility(Lifecycle.Read)
features?: Record<boolean>;
```

The emitted `definitions.BatchFeatureStatus.properties.features` schema is:

```json
{
  "type": "object",
  "description": "Features with enabled status",
  "additionalProperties": { "type": "boolean" },
  "readOnly": true
}
```

Swagger flags the exact `additionalProperties` path. The source suppression
targets `arm-no-record`, not `no-boolean`. Native reports four ordinary Boolean
properties elsewhere in `models.tsp`, but none at the dictionary property on
line 1225. Both raw and aligned native totals are four; Swagger has five events.
The property's native type is a record model, not the standard Boolean scalar.
The dictionary control independently reproduces the missing indexer check.

### Gap example: an opaque external Swagger model has no native property

- **Classification:** External-schema coverage boundary.
- **Status:** Explained; no TypeSpec Boolean rule update required for this
  opaque reference. Swagger validation is still needed for the external schema.
- **Project/API version:** `specification/security/resource-manager/Microsoft.Security/Security/BatchPricingsAPI`
  / `2026-07-01`.
- **Source:** `models.tsp:18`, `PricingPropertiesReference`.

```typespec
@useRef("./pricings.json#/definitions/PricingProperties")
model PricingPropertiesReference {}
```

The referenced JSON, not a native model property, contains:

```json
{
  "type": "boolean",
  "description": "Optional. True if the plan is deprecated. If there are replacing plans they will appear in `replacedBy` property",
  "readOnly": true
}
```

The exact path is `definitions.PricingProperties.properties.deprecated` in
`pricings.json`. Two validator invocation events share that JSON path; only the
direct invocation supplies an explicit source document. Native raw and aligned
counts are both zero because the placeholder model has no declared properties.
Do not invent a native warning or borrow another project's diagnostics to
equalize counts. A fully native coverage claim requires representing this
external shape in TypeSpec or explicitly retaining validation at the JSON
boundary.

## Reproduce the recorded comparison

Use separate clean candidate and specs checkouts. For this historical run,
check out the exact candidate/specs commits above and initialize the candidate's
`core` submodule at its recorded gitlink. Do not resolve current branch tips when
reproducing this run. A new baseline, in contrast, selects current references
once and records their new identities.

Use the tools pinned in each checkout. The candidate build used this scoped
restore after the first build exposed missing dependencies:

```powershell
mise exec -- pnpm install --filter . --filter ./core `
  --filter '@azure-tools/typespec-azure-rulesets...' `
  --filter '@azure-tools/typespec-autorest...' `
  --filter '@typespec/integration-tester...' `
  --filter '@typespec/events...' --filter '@typespec/sse...' `
  --filter '@typespec/streams...' --filter '@typespec/json-schema...' `
  --filter '@typespec/xml...' --frozen-lockfile --ignore-scripts

mise exec -- pnpm exec turbo run build `
  --filter '@azure-tools/typespec-azure-rulesets...' `
  --filter '@azure-tools/typespec-autorest...' `
  --filter '@typespec/integration-tester...' `
  --filter '@typespec/events...' --filter '@typespec/sse...' `
  --filter '@typespec/streams...' --filter '@typespec/json-schema...' `
  --filter '@typespec/xml...' --output-logs=errors-only
```

All 23 required package builds succeeded without cache hits. A broader restore
had triggered an unrelated Python preparation failure; that failed attempt is
retained separately and is not presented as a passing build.

Pack into a new artifact directory using `chronus pack --pack-destination
<artifacts>` and one `--only <package>` selector for each package. Run Azure
packing from the candidate root and core packing from its initialized `core`
workspace. The retained inventory contains six Azure packages and eleven core
packages. Restore artifacts by their recorded hashes, not by installing the
same version strings from the registry.

From the tooling checkout's `packages\typespec-lintdiff` directory, run the
following with the recorded specs package manager on `PATH`. Replace the four
placeholder paths with absolute local paths. The example uses the registry
approved on the original machine; preserve the approved registry on the replay
machine rather than changing shared global configuration.

```powershell
$env:PNPM_CONFIG_REGISTRY='https://packagefeedproxy.microsoft.io/npm/'
mise exec pnpm@12.6.0 -- node --import tsx/esm test\harness\native-coverage.ts `
  --candidate-repo <candidate> --specs-repo <specs> --tgz-dir <artifacts> `
  --validator-rule EnumInsteadOfBoolean `
  --tsp-rule @azure-tools/typespec-azure-core/no-boolean `
  --scope boolean-http --concurrency 4 --output <new-empty-run>
```

The scoped pilot adds `--limit 8`. Its second run adds
`--baseline-run <original-completed-pilot>` and uses another new output
directory. Neither `--filter` nor `--limit` is present in the full-corpus command.
Never run two writable comparisons concurrently against the same specs
checkout.

## Limits of the evidence

This run evaluates production ARM validation, not data-plane, RPaaS or staging
rules. It selects the latest emitted API version rather than all versions or a
readme tag. Authored native suppressions remain active; Swagger readme
suppressions are not applied.

`boolean-http` aligns source diagnostic locations with selected-version HTTP
metadata. It does not rerun every possible predicate on a projected program,
nor establish an exact cross-engine actionable identity. Raw, aligned,
file-aware JSON-path and source-location counts remain separate.

Default-emitted unused service schemas are included by the Boolean profile.
The general `http-reachable` profile remains HTTP-only.

The AutoRest launcher and validator packages have runtime versions and
entrypoint hashes in the retained receipts. The launcher requests the existing
v3 core resolution; its raw log records the configuration range `^3.2.0`.
This analysis does not claim a fully locked transitive AutoRest engine or an
automatic source-to-build attestation from package versions.

The successful scoped baseline reuse is local. Public observation copies
replace machine-specific roots and therefore are not the byte-identical sealed
CLI baseline. Original hashes identify the local originals; a separate
derivation inventory identifies published bytes. Downloading these observation
copies must not be presented as passing cross-machine `--baseline-run` replay.
Portable baseline replay remains unverified.

## Publication and observation replay

Publication verification is pending. The compact reports and native target
receipts belong in this evidence branch. The approximately 961 MB full-run
directory and 17 candidate tarballs belong in durable fork release assets,
not Git. The asset inventory and original-to-published derivation hashes
distinguish original inputs from sanitized public copies.

The observation bundle retains emitted Swagger, all validator shards and raw
output, native receipts, build/validation logs and the final semantic controls.
Machine-specific roots are replaced. Fictional `c:\users\contosoUser` strings
in the public security-alert example payloads remain unchanged; those strings
are sample data, not paths from the execution machine.

After downloading and verifying the recorded asset hashes, extract the
observation archive into a new directory. From a fresh evidence checkout,
recompute the count audit without the original development worktrees:

```powershell
node migration-evidence\tasks\EnumInsteadOfBoolean\audit-counts.mjs `
  <extracted>\observations\full-4 <new-audit-directory>
```

Compare the result with
`runs\full-4\audit\count-audit.json` and `project-counts.csv`.
This replays observation analysis, not the sealed CLI baseline or a new native
execution. Rebuilding/rerunning the comparison needs the frozen source checkouts,
recorded toolchain and unchanged package assets described above.
