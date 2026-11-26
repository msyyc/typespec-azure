# DefaultErrorResponseSchema supporting evidence

## Assessment boundaries

This assessment reuses `use-standard-error`. It adds guidance and provenance, not
a new rule, production predicate, default enablement change, or Swagger-linter
retirement decision. Existing `LroErrorContent` provenance remains intact.

The recommended disposition is **partial existing coverage**. Functional
equivalence is not established. HEAD exemptions, unmarked defaults and inherited
library operations remain material limits. Reviewers retain policy and acceptance
decisions.

- [Pinned inputs and comparison policy](inputs.json).
- [Candidate source snapshots and 15-package closure](candidate.json).
- [Semantic, injected and default-activation controls](controls.json).
- [Validation, including the failed broad run and authorized scope change](validation.json).
- [Representative saved schemas](representative-schemas.json).

Historical aggregate coverage reports are not inputs to this assessment. This is
a fresh source-program comparison against the frozen production ARM baseline.
Source programs and latest-version Swagger are not version/reachability-aligned.

## Predicate and member matrix

The [Swagger implementation](https://github.com/Azure/azure-openapi-validator/blob/405e6f094fa8280e05af23327845f6202a8edc65/packages/rulesets/src/native/legacyRules/DefaultErrorResponseSchema.ts)
selects existing `paths.*.*.responses.default` entries. It requires a schema and
the properties `error`, `error.code` and `error.message`. It does not require
string scalars, required properties or `readOnly`. A missing default response does
not trigger this rule.

The [TypeSpec implementation](https://github.com/Azure/typespec-azure/blob/9024f28739650a92c05465c8318fc08bc17a48cc/packages/typespec-azure-resource-manager/src/rules/use-standard-error.ts)
requires an `@error` response on a linted non-HEAD operation. Every marked payload
must use the standard `Azure.ResourceManager.CommonTypes.ErrorResponse` model.
It checks marked union members separately and reports once per authored
operation. It skips compiler-classified template declarations/instances,
operations on uninstantiated templated interfaces, and library-origin targets.
Authored uses of standard ARM operation templates remain lintable, as the
positive control demonstrates.

| Original behavior or control                                | Result                                  | Evidence and limit                                                                                                                                 |
| ----------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Existing default has no schema/body                         | Covered for linted marked defaults      | Separate injected bodyless-default control: one emitted diagnostic, one callback, native `*` response has no body. No new Swagger execution.       |
| Nested `error` missing                                      | Covered for linted marked defaults      | Source controls and 756 saved Swagger findings; real counterpart and library-origin limits are separated below.                                    |
| `error.code` or `error.message` missing                     | Covered for linted marked defaults      | Separate discriminating controls; six saved findings lack both properties.                                                                         |
| Standard error model                                        | Compliant                               | Canonical tests, injected ARM-template control and actual final authored correct example.                                                          |
| Custom model has all three properties                       | Stricter TypeSpec requirement           | Custom shapes still warn. All 798 such warnings in the 19 Swagger-bearing projects have a retained property-presence-valid default schema.         |
| Properties have other scalar types or are optional          | Different requirements                  | Swagger checks presence only. TypeSpec still requires standard model identity. Scalar-type control does not establish corpus prevalence.           |
| Aliases/nullable standard model                             | Compliant within existing rule contract | Existing 49-test suite. Copies, spreads and derived custom models are not aliases.                                                                 |
| Missing default/error response                              | Outside original check                  | `missingErrorResponse` checks missing marked errors, not an existing default schema. Exclude that diagnostic family from member-attributed totals. |
| Explicit/ranged marked error, no invalid default            | Outside original check                  | Broader TypeSpec payload policy. Exclude only the proven explicit-only check, not unmatched default warnings.                                      |
| HEAD with malformed marked default                          | Missing Swagger scope                   | TypeSpec exemption is verified by controls. Swagger selector has no HEAD exemption. No removal or retirement is approved here.                     |
| Unmarked malformed default with valid explicit marked error | Missing payload coverage                | Injected control emits no target diagnostic. A missing-marked-error warning on a different fixture is not coverage of this payload check.          |
| Inherited library operation with custom marked default      | Missing coverage                        | Five real provider `/operations` endpoints; effective operation location is the ARM library, although custom error models are project-authored.    |
| Authored suppression                                        | Honored                                 | Positive fixture: emitted/callback `1/1`; compliant `0/0`; suppressed positive `0/1`. Captured suppressed evidence is not an emitted warning.      |

Production enforcement does not import OpenAPI decorators or inspect emitter
extensions. Legacy `OpenAPI.defaultResponse` occurs only in discriminating
fixtures. HTTP metadata exposes its default status without a production OpenAPI
dependency.

## Difference investigations

Start with the [complete differing project/model index](difference-groups.md).
It contains 153 differing diagnostic groups in 119 projects. The
[490-project inventory](project-accounting.csv) retains matching projects,
opposing gaps and excluded mixed-rule checks. The
[source population/path trace](residual-evidence.md) explains every initially
unmatched context without changing raw counts.

### Repeated input-associated Swagger observations

- **Classification:** count-only observation multiplicity.
- **Project/API version:** Network/Network, `2026-03-01`.
- **Status:** raw observations preserved; exact source attribution is limited.

Network has 528 raw observations, 351 input-file/path occurrence keys and 39
file-independent path/method contexts. The additional observations comprise 312
cross-input keys and 177 additional field-identical records at repeated keys.
The same-key repetitions occur in 90 groups. No records are removed.

For example, `GET /subscriptions/{subscriptionId}/providers/Microsoft.Network/ipGroups`
has 15 observations across nine validator inputs. `expressRoute.json` contributes
four, `networkGateway.json` two, `virtualWan.json` three, and six other inputs one
each. Only one observation in each Network context has reported source
attribution; 489 Network observations use input-fallback attribution.

The retained application-gateway request-header default illustrates the malformed
shape behind these contexts:

```json
{
  "description": "An unexpected error response.",
  "schema": {
    "$ref": "#/definitions/Error"
  }
}
```

Its resolved properties are `code`, `details`, `innerError`, `message` and
`target`, not nested `error`. The source custom error model is
[`Microsoft.Network.Error`](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/network/resource-manager/Microsoft.Network/Network/Network/models.tsp#L9335-L9361).
The selected request-header context has nine saved observations and one
corresponding TypeSpec payload diagnostic.

**Coverage status:** all 39 contexts have a structural-default source diagnostic.
Exact project/path/method plus independently inspected schema and source
predicates establishes this scoped observation. It is not proof that all
input-fallback observations identify the same originating file or actionable
defect.

**analysis:** keep raw counts, occurrence keys and context counts separate.
Do not change either rule merely to equalize counts. Repeated serialized records
are evidence about the saved observation stream, not approval to normalize
distinct defects or retire the Swagger rule.

### Standard-model identity is stricter than property presence

- **Classification:** TypeSpec-linter-only default-payload requirement.
- **Project/API version:** Network/Network, `2026-03-01`.
- **Source:** `ApplicationGateways.get`, `ApplicationGateway.tsp:58`.
- **Status:** existing stricter policy; not a new implementation.

The [authored operation](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/network/resource-manager/Microsoft.Network/Network/Network/ApplicationGateway.tsp#L52-L58)
uses this interface-member excerpt:

```text
get is ArmResourceRead<ApplicationGateway, Error = CloudError>;
```

The [custom model](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/network/resource-manager/Microsoft.Network/Network/Common/main.tsp#L2491-L2517)
has `error?: CloudErrorBody`, with optional string `code` and `message` properties
on `CloudErrorBody`. Documentation comments are omitted here:

```typespec
@Azure.ResourceManager.Legacy.armExternalType
@error
model CloudError {
  error?: CloudErrorBody;
}
```

The saved response is:

```json
{
  "description": "An unexpected error response.",
  "schema": {
    "$ref": "./common.json#/definitions/CloudError"
  }
}
```

Reference resolution confirms `error.code` and `error.message`.

| Engine          | Observed result                                                     |
| --------------- | ------------------------------------------------------------------- |
| Swagger linter  | No finding for this context; all required property names exist.     |
| TypeSpec linter | One payload warning; `Common.CloudError` is not the standard model. |

All 793 Network warnings in this check family have property-presence-valid saved
defaults. The same investigation finds one such warning in Commerce, one in
FrontDoor and three in MetricsApi: 798 across the 19 Swagger-bearing projects.
These are not discarded from the default-payload scope.

**Coverage status:** a stricter existing TypeSpec policy, not structural parity.

**analysis:** prefer the standard model when API compatibility permits. Do not
silently change existing wire contracts or generated client types to remove
warnings. A justified existing-API suppression may be needed. No independent
structural-only competing rule is proposed.

### Inherited library operations are not lint targets

- **Classification:** Swagger-linter-only behavior.
- **Project/API version:** WorkBookOperations, `2021-03-08`.
- **Status:** confirmed missing coverage; no policy retirement approved.

The [authored interface](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/WorkBookOperations/main.tsp#L43-L47)
is:

```typespec
interface Operations
  extends Azure.ResourceManager.Legacy.Operations<OperationListResult, ErrorResponse> {}
```

Its project-authored `@error model ErrorResponse` has top-level `code`, `message`
and `details`, not an `error` wrapper. The saved
`GET /providers/Microsoft.Insights/operations` default references that model.

| Engine          | Observed result                     |
| --------------- | ----------------------------------- |
| Swagger linter  | One missing-nested-`error` finding. |
| TypeSpec linter | No target diagnostic.               |

The native HTTP service graph resolves the effective operation to
`Azure.ResourceManager.Legacy.Operations.list`. Its location context is `library`
and its source library is `@azure-tools/typespec-azure-resource-manager`.
Its actual marked `*` response body is `WorkBookOperations.ErrorResponse`, with
no nested `error`.

The same cause is independently confirmed for provider operation endpoints in
DeviceProvisioningServices, HDInsight, IoTHub and subscriptions. Each contributes
one saved finding without a TypeSpec counterpart. WorkBookOperations has no other
authored operations and no raw target diagnostics.

**Coverage status:** five confirmed inherited-operation gaps, not compiler
prevention or evidence that custom error overrides are impossible.

**analysis:** an owning-rule follow-up could inspect project-authored inherited
interface instantiations and report at a project-owned declaration. It needs a
negative `Legacy.Operations<..., CustomError>` case, a compliant standard-error
case, and correct once-per-authored-target behavior. It must not report library
declarations merely because a project imports them. That policy/implementation
extension requires separate owner approval; it is not implemented here.

### A common-type wrapper can add an extra `error` level

- **Classification:** covered structural issue plus a separate inherited-target gap.
- **Project/API version:** subscriptions, `2022-12-01`.
- **Source:** project `CloudError`, illustrated by authored `checkResourceName`.

The [source model](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/resources/resource-manager/Microsoft.Resources/subscriptions/models.tsp#L225-L233)
contains:

```typespec
@error
@Azure.ResourceManager.Legacy.armExternalType
model CloudError {
  error?: Azure.ResourceManager.CommonTypes.ErrorResponse;
}
```

`ErrorResponse` already has an `error` wrapper. The saved schema's outer `error`
therefore resolves to a model whose property is another `error`, not `code` and
`message`. This is not a missing-schema or scalar-type issue.

| Engine          | Observed result                                                                            |
| --------------- | ------------------------------------------------------------------------------------------ |
| Swagger linter  | Six existing defaults lack `error.code` and `error.message`.                               |
| TypeSpec linter | Five project-authored payload diagnostics; the inherited provider operation is not linted. |

**Coverage status:** the five authored cases are recognized. The remaining case
is the inherited-operation gap described above, not a second counting allowance.

**analysis:** use the canonical response model directly when compatible. Review
existing API compatibility before changing the error envelope. A partial custom
shape repair alone does not satisfy the TypeSpec linter's model-identity policy.

### Source-program SDK overrides are not emitted service operations

- **Classification:** source/Swagger population difference.
- **Project:** IoTHub.
- **Source:** `client.tsp:365`, `:394` and `:418`.
- **Status:** confirmed source-only customization operations in this comparison.

The [source](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/iothub/resource-manager/Microsoft.Devices/IoTHub/client.tsp#L365-L435)
declares `replaceManualFailover`, `replaceTestAllRoutes` and `replaceTestRoute`.
Each uses `Microsoft.Devices.ErrorDetails` and is bound by an SDK `@@override`,
for example:

```typespec
@@override(IotHubDescriptions.manualFailover, replaceManualFailover);
```

The source HTTP metadata gives all three the path
`/{subscriptionId}/{iotHubName}/{resourceGroupName}/{provider}`. None occurs in the
unprojected service HTTP graph or selected saved Swagger. These are not inferred
API-version removals.

| Engine          | Observed result                                                       |
| --------------- | --------------------------------------------------------------------- |
| Swagger linter  | No corresponding emitted operation.                                   |
| TypeSpec linter | Three default-payload diagnostics on source customization operations. |

**Coverage status:** a source-population difference, not three extra emitted API
defects. The declared source comparison retains these individual diagnostics.

**analysis:** do not change production policy to equalize these totals. A
version/reachability-aligned comparison would need its own supported profile and
must not silently relabel this source run.

Across the full corpus, 46 captured warnings target SDK override declarations
outside the service HTTP graph. The three IoTHub warnings above have malformed
source defaults. The other 43 use property-presence-valid custom source models.
All remain in the declared source-scope total. Exact source override statements
and per-project counts are retained in the linked source-population evidence.

## Full-population accounting

The fresh run selected and assessed all 490 projects. All 490 worker receipts
succeeded, and the analyzer's final copied-dataset integrity check passed.
The native stage took 6,307.557 seconds within its original 7,200-second budget.
No Swagger was generated and no Swagger linter was rerun.

| Observation                                                      | Count |
| ---------------------------------------------------------------- | ----: |
| Saved Swagger diagnostics                                        |   762 |
| Swagger occurrence keys (rule/project/input file/JSON path)      |   585 |
| Swagger file-independent keys and path/method contexts           |   273 |
| Selected TypeSpec rule diagnostics, before check attribution     | 5,119 |
| Conservative TypeSpec source-location keys                       | 5,119 |
| Excluded missing-marked-response checks                          |   450 |
| Excluded explicit-only payload checks                            |    40 |
| Scoped emitted default-payload diagnostics                       | 4,629 |
| Scoped captured suppressed diagnostics in 144 inspected projects |     0 |

The scoped total is `5,119 - 450 - 40 + 0 = 4,629`. The source check families are
271 structural defaults and 4,358 property-presence-valid custom defaults. These
are source predicate families, not equivalent Swagger defects.

Saved-schema investigation initially found 4,231 property-presence-valid
defaults, 263 missing-`error` defaults, five defaults missing both `code` and
`message`, and 130 diagnostics without an exact raw source-path candidate.
The source-backed follow-up accounts for all 130: 46 SDK overrides, 67
version-unavailable declarations, and 17 exact authored path representations
(13 legacy parameter renames and four provider namespace substitutions).
All 17 corresponding retained defaults have the required properties.
Thus 4,248 warnings enforce stricter model identity against
property-presence-valid retained defaults. No unexplained numerical residual is
hidden in a balancing category.

The 19 Swagger-bearing projects contribute 1,069 scoped diagnostics. Their
breakdown remains 271 structural defaults and 798 stricter defaults. Other
projects contribute 3,560 scoped diagnostics. Every one was attributed from
captured operations and response bodies, not selected by message or unmatched
status alone.

There are 19 Swagger-bearing projects and 128 scoped TypeSpec-bearing projects:
18 overlap, one is Swagger-only and 110 are TypeSpec-only. The sole Swagger-only
project is WorkBookOperations. The unfiltered target rule warns in 143 projects;
15 of those have only checks excluded from this member's diagnostic scope.

Four projects have a positive Swagger-minus-TypeSpec gap; 115 have a negative
gap and 371 are equal. Positive excess sums to 4, negative excess to 3,871;
the signed difference is `4 - 3,871 = -3,867`, and the absolute sum is 3,875.
Per-project evidence retains both `S - N` and `N - S`, absolute gaps,
`abs(N - S) / max(N, S)` (zero when both are zero), and the separately labeled
relative-to-S metric.

The complete reconciliation is
`762 - 4,629 = 489 + 5 - 4,248 - 46 - 67 = -3,867`.
The 489 term preserves Network input/repeated-record multiplicity; five are
inherited-operation gaps; 4,248 are stricter defaults; 46 are source-only SDK
operations; 67 are unavailable in the selected Swagger version. The other
229 authored contexts contribute `229 - 229 = 0`.

All 144 named inspected projects have exact captured/emitted diagnostic
multisets matching the original full run. Five enriched captures repeat
projects for library-origin investigation; the 149 capture receipts are not
149 distinct projects. Zero captured suppressions here does not establish zero
suppressed warnings in the other 346 projects.

**Coverage status:** partial existing coverage with five real inherited-target
gaps and control-proven HEAD/unmarked-default limits. Stricter model identity
and source/latest-version differences are explained, not policy retirement.
No equivalent-defect total, full emission parity or blanket acceptance is claimed.

**analysis:** keep this change documentation-only. Preserve the existing
`LroErrorContent` mapping and rule enablement. Owners must decide whether to
extend inherited-target/unmarked-default coverage or change HEAD policy.
Existing API wire contracts must not change merely to remove warnings.

## Validation and controls

The unchanged owning-rule suite passes all 49 tests at the checked-in 10,000 ms
test/default hook limits. Twelve source semantic/documentation controls pass,
including the actual incorrect/correct snippets selected from the final authored
documentation.

Injected controls pass 11 initial cases plus the separate bodyless-default case.
They establish standard ARM-template compliance, a violating custom error,
explicit activation despite configuration disablement, authored suppression,
HEAD/unmarked-default limits, and target-only behavior.

`@azure-tools/typespec-azure-resource-manager/all` activates the rule.
`@azure-tools/typespec-azure-rulesets/resource-manager` explicitly disables it.
The target-only corpus run does not assess per-project default activation; the
separate activation controls are not corpus-wide default findings.

The portable harness passes 37 applicable controls. Six parameterized fixtures
for an unrelated absent `resource-group-path-parameter` rule were excluded
before execution. They are not passes and did not justify adding another rule.

The broad ARM run remains failed: 999 tests passed, seven timed out individually
and nine failed in setup hooks. No environmental cause is proven. The user
subsequently replaced that broad required gate with focused affected tests and
documentation checks for this unchanged two-Markdown-only change. No broad
rerun, timeout increase or instrumentation was used.

ARM build/lint, documentation regeneration, changed-file formatting and the native
whitespace check pass. Existing documentation-missing warnings are disclosed in
the validation receipt. Chronus reported no eligible package changes because
Markdown is excluded.

### Tested fixture bytes and publication derivatives

The 12 injected controls executed the original fixture bytes. Of the 24 source
and configuration files, 22 remain byte-exact in this publication. Only
`fixtures/injected/9/main.tsp` and `fixtures/injected/10/main.tsp` are display
derivatives. Each removes its final two space bytes and retains the existing
terminal LF. No TypeSpec token, diagnostic location or tested original changed.
The display derivatives were not executed.

The exact original bytes are recoverable from
`controls.json` → `publicationFixtureSources.entries`. Each entry records base64,
encoding, byte length, original SHA-256 and display SHA-256. Original SHA-256:

- Fixture 9: `6ca44f21248ca52b24a9948c12503024e433dd9e7e1d0faf9b82415501ce83b1`.
- Fixture 10: `909b88076e715c4cf29b47fce5e73d0d769078462c9ed65e04012afd5dafa280`.

The original raw control inputs and receipts remain immutable. All four reviewed
archive checksums remain unchanged; no archive was repacked. The original source
bytes were reconstructed from public JSON and compared byte-for-byte with both
immutable tested inputs. This is publication normalization, not another native,
unit-test or corpus run.

To restore the executed sources, set `$RestoredTask` to a new writable copy of
this task directory, not the immutable inputs. Use this before rerunning fixtures:

```powershell
$Controls = Get-Content "$RestoredTask\controls.json" -Raw -Encoding utf8 | ConvertFrom-Json
foreach ($Entry in $Controls.publicationFixtureSources.entries) {
  $Path = Join-Path $RestoredTask ($Entry.path.Replace('/', '\'))
  [IO.File]::WriteAllBytes($Path, [Convert]::FromBase64String($Entry.executedOriginalBase64))
  if ((Get-FileHash $Path -Algorithm SHA256).Hash.ToLowerInvariant() -cne $Entry.executedOriginalSha256) {
    throw "Restored fixture hash mismatch"
  }
}
```

Keep the display-copy hash distinct from the original input hash. Do not describe
the derivatives as executed fixtures or disable Git whitespace checks.

## Provenance and recovery boundaries

The candidate is based on `9024f28739650a92c05465c8318fc08bc17a48cc`, with core
`41e2a4e70f0ea49ee52fa9d0d6d3d9c698c6ac08`. Its reviewed content snapshot has tree
`899e080cc92c485e32a6fa5bac28b37f75ca3dd5`. No production or canonical-test source
changed. Task commit `438371583f18256bac617148633654f43dc6a4ca` has that exact tested tree; its canonical source branch is published. This binds the commit to the assessed content, not a new native run.

The 15 tarballs contain six Azure packages and nine core packages, derived from
published dependencies and peers rather than development dependencies. Every
non-manifest payload byte was checked against the built workspace. Rewritten
package manifests and package-manager-added shared LICENSE files are handled
explicitly in the payload proof. Core packages were packed separately because
the Azure Chronus configuration excludes `@typespec/*`.

Producer and candidate use the same package version numbers but different source,
core and artifact identities. `frozen-reference` assumes compatibility; it does
not prove identical emission. Actual analyzer Node is `v26.5.0`; supplemental
specs controls use `v26.5.1`. Candidate pnpm is `11.10.0`; the specs package
manager is `12.6.0`. Integration uses patch/install only, never checkout/reset.
The no-lockfile runtime installation changed incidental transitive tool versions;
full transitive freezing is not claimed.

Reading published evidence, reanalyzing saved observations and fully rerunning
the comparison are separate recovery paths. Count replay does not rerun either
linter or by itself restore a sealed CLI baseline. A complete new run must use
the pinned specs source, compatible closure, original mapping/settings, required
controls and full population. It must not generate Swagger as a missing-cache
fallback or infer a semantic conclusion from counts alone.

## Reading, reanalysis and full regeneration

These are different operations. Download/upload round trips and fresh-context
recovery must be verified separately; preparing a local archive does not establish
durable publication.

### Recover inputs and read observations

Use the repositories, exact commits and archive checksums in [inputs.json](inputs.json)
and [candidate.json](candidate.json). Recover the shared baseline from its
original release, not a regenerated Swagger dataset. Verify archive size and
SHA-256 before extraction. Keep the recovered baseline read-only.

The candidate package archive contains the 15 original tarballs and
`artifact-source-proof.json`. Candidate/core source ZIPs preserve the assessed
content. Recover the actual pinned Git commits and submodules when a command
requires Git metadata; extracting a source ZIP alone does not create that
metadata. Tooling has a different core gitlink from the candidate and is recovered
from its separately pinned canonical commit.

The observations archive retains the full run's actual receipt filenames,
selected Swagger observations, semantic captures, scoped accounting and
saved-schema inspection. Its `retention.json` records original and portable byte
hashes. Physical checkout prefixes become named role aliases. Native diagnostic
projects, source targets and counts remain unchanged. No raw execution logs,
dependencies or duplicate Swagger dataset belong in that archive.

### Reanalyze saved data without running either linter

Set `$Task` to this task directory, `$Observations` to the recovered observations
archive root, and `$Baseline` to the recovered sealed baseline root. Set `$Replay`
to a new empty directory outside those inputs. Use Python 3.12 or newer.

```powershell
python "$Task\extract-saved-swagger.py" `
  --baseline "$Baseline\dataset" `
  --output "$Replay\saved-swagger-details.json"

python "$Task\account-analysis.py" `
  --run "$Observations\full" `
  --swagger "$Replay\saved-swagger-details.json" `
  --captures "$Observations\captures\swagger-projects" `
    "$Observations\captures\library-origin" `
    "$Observations\captures\additional" `
  --output "$Replay\account"

python "$Task\compare-saved-defaults.py" `
  --baseline "$Baseline\dataset" `
  --account "$Replay\account" `
  --captures "$Observations\captures\swagger-projects" `
    "$Observations\captures\library-origin" `
    "$Observations\captures\additional" `
  --output "$Replay\saved-defaults"
```

The parameterized Swagger reader reproduces all 762 retained findings
byte-for-byte. Its six extraction functions and complete aggregation have the
same syntax trees as the original reader. Accounting preserves diagnostic
multiplicity; its nine controls distinguish exact diagnostic matching from the
conservative source-location summary and cover both gap directions and a zero
denominator. Source keys exclude message text, while exact matching retains it.
Per-project accounting includes `N - S` and `abs(N - S) / max(N, S)` (zero when
both counts are zero). The separately labeled relative-to-S metric is not a
substitute for that symmetric relative difference.

Compare reanalyzed counts, project rows and classifications with the saved
accounting. A portable copy's coverage-file byte hash can differ from the original
because physical paths were replaced; `retention.json` preserves both hashes.
That difference is not a changed diagnostic or evidence of equivalent defects.

### Rerun the frozen TypeSpec comparison

This requires a prepared tooling checkout, the pinned candidate/core checkout,
an exclusively owned writable specs runtime at the frozen source commit, the
original candidate tarballs and a new empty output directory. Restore only missing
prerequisites. Preserve the approved registry process-locally; do not change global
package-manager configuration or reset an existing runtime.

Set `$Tooling`, `$Candidate`, `$Specs`, `$Tarballs`, `$Baseline`, `$Run` and
`$ApprovedRegistry` to those verified roles. `$Tarballs` names the recovered
archive's `packages` directory. From the tooling checkout:

```powershell
Set-Location $Tooling
$env:PNPM_CONFIG_VERIFY_DEPS_BEFORE_RUN = "false"
$env:PNPM_CONFIG_REGISTRY = $ApprovedRegistry
mise exec node@26.5.0 pnpm@12.6.0 -- node --import tsx/esm `
  packages\typespec-lintdiff\test\harness\native-coverage.ts `
  --candidate-repo $Candidate `
  --specs-repo $Specs `
  --tgz-dir $Tarballs `
  --validator-rule DefaultErrorResponseSchema `
  --tsp-rule @azure-tools/typespec-azure-resource-manager/use-standard-error `
  --scope source `
  --native-mode target-only `
  --native-budget-seconds 7200 `
  --baseline-run $Baseline `
  --baseline-policy frozen-reference `
  --output $Run `
  --concurrency 2
```

Do not add a filter/limit, invoke Swagger generation, or use integration's
checkout/reset stage. The original run explicitly allowed its reviewed
two-Markdown working-tree snapshot; a recovered clean task commit instead uses
the default clean-checkout mode. Verify the same expected source tree and keep
the original assessed identity separate from any new run's commit identity.

Repeat applicable runtime controls and verify actual loaded entrypoint hashes.
New installs can resolve incidental transitive tools differently; matching
package version numbers alone do not prove an identical closure.

Also rerun `trace-source-population.py` against the recovered residual source and
project annotation receipts to reproduce the 46/67/17 partition. Its four
availability controls cover removal boundaries, re-addition and future addition.
This operates on retained source annotations and saved schemas, not a projected
program or fresh emission. The exact command is in
[the source-path/population evidence](residual-evidence.md#reanalysis).
