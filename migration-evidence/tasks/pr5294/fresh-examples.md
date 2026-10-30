# Fresh cause examples and remaining uncertainty

The [complete difference inventory](fresh-differences.md) preserves every unequal
project and exact target. Counts below are raw observations, not a normalization.
Sources are the frozen specs commit
`2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`; Swagger excerpts come from the verified
shared baseline. The TypeSpec linter is the unchanged PR head `94b316787`.

## Read-only reference siblings

**Classification:** Swagger-linter-only. **Observed counts:** 9 / 0 across
Dynatrace (1), Elastic (1), Help (1), ServiceGroups (1), NewRelic (1), and
SecurityConnectorsDevOpsAPI (4).

For example,
[Dynatrace models.tsp:421](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/dynatrace/resource-manager/Dynatrace.Observability/DynatraceObservability/models.tsp#L421):

```typespec
@visibility(Lifecycle.Read)
provisioningState?: ProvisioningState;
```

The saved `MonitoredSubscriptionProperties` request reaches a property with:

```json
{
  "provisioningState": {
    "$ref": "#/definitions/ProvisioningState",
    "description": "Provisioning State of the resource",
    "readOnly": true
  }
}
```

The referenced enum has no `readOnly` or `x-ms-mutability`. The same reference
sibling pattern was checked for all nine findings, including the four distinct
Security paths. The Swagger linter reports immutable provisioning state despite
the raw property's `readOnly: true`; its rule uses resolved properties. The
TypeSpec linter excludes the Read-only property from effective PATCH input.

**Disposition: No TypeSpec rule update required** for these exclusions.
The precise internal point at which the Swagger execution loses or disregards
the reference sibling was not instrumented; this is not a claim that the saved
Swagger execution has been repaired or exactly reproduced.

## Excluded input

**Classification:** Swagger-linter-only. **Observed counts:** ConfidentialLedger
1 / 0; SAPDiscoverySites 1 / 0.

ConfidentialLedger uses
`ConfidentialLedger.tsp:43`:

```typespec
@patch(#{ implicitOptionality: false })
update is ArmCustomPatchAsync<
  ConfidentialLedger,
  PatchModel = ConfidentialLedger,
```

The saved request references the full resource and inherited common
`TrackedResource.location`:

```json
{
  "type": "string",
  "description": "The geo-location where the resource lives",
  "x-ms-mutability": ["read", "create"]
}
```

The inherited required list leads the Swagger linter to require `location`.
The TypeSpec linter excludes Read/Create-only location from ordinary PATCH.

SAPDiscoverySites `models.tsp:344` and `:447`:

```typespec
@visibility(Lifecycle.Read)
performanceData?: PerformanceData;
```

```typespec
@discriminator("dataSource")
model PerformanceData {
  /** The data source of the performance data. */
  dataSource: DataSource;
}
```

The Swagger linter reports required `dataSource` inside the saved resource
schema. This is an authored discriminator, not a synthesized-property example.
The TypeSpec linter never traverses its Read-only parent as PATCH input.
The original reported JSON path is retained even where resolving that location
does not identify the final nested property; no exact location correspondence
is invented.

**Disposition: No TypeSpec rule update required** for excluding these inputs.

## Version populations

**Classification:** TypeSpec-linter-only. **Observed counts:** ManagedNetworkFabric
0 / 29; ProgrammableConnectivity 0 / 6. These findings do not establish a
same-version semantic gap.

ManagedNetworkFabric selects Swagger version `2025-07-15`. Every native target
was inspected: it is a removed/renamed declaration or a descendant of one.
For example, `models/AccessControlList.tsp:367`:

```typespec
@removed(Versions.v2025_07_15)
@renamedFrom(Versions.v2025_07_15, "icmpTypes")
icmpTypesDeprecated?: string[];
```

The unprojected request retains the old name, while current resource metadata
and latest-version Swagger do not provide that same name. The 29 findings are
not 29 proven current-version defects.

ProgrammableConnectivity selects `2025-03-30-preview`.
`OperatorApiConnection.tsp:54`:

```typespec
@TypeSpec.Versioning.removed(Versions.v2025_03_30_preview)
@visibility(Lifecycle.Read, Lifecycle.Create, Lifecycle.Update)
configuredApplication?: ApplicationProperties;
```

Its referenced `Gateway.tsp:166` includes:

```typespec
@TypeSpec.Versioning.madeRequired(Versions.v2025_03_30_preview)
name: string;
```

An inspection of actual compiled PATCH operations established that these six
findings come from the **OperatorApiConnection** update body, not the tag-only
Gateway operation. Unprojected source combines the removed enclosing property
with newly required descendants. Saved `OperatorApiConnectionUpdate` has no
`configuredApplication`; the Gateway request is independently tag-only.
There is no meaningful latest-version emitted excerpt for that removed input.

**Disposition: No TypeSpec rule update required to explain this comparison
artifact.** Same-version assessment requires a supported projected evaluation;
it was not performed, and these source findings are not credited as parity.

## Native-only projects

The other thirteen TypeSpec-only projects have **0 / 61** findings:

| Project                    | Swagger linter | TypeSpec linter | Verified cause                                                    |
| -------------------------- | -------------: | --------------: | ----------------------------------------------------------------- |
| ApiCenter                  |              0 |               1 | `restore = false`                                                 |
| AzureDataTransfer          |              0 |               4 | Zero defaults and defaults beneath arrays                         |
| ComputeSchedule            |              0 |               2 | False defaults, including an array item                           |
| Discovery.Management       |              0 |               1 | Zero default in imported source                                   |
| Edge configurationmanager  |              0 |               4 | Two array-item defaults encountered through two source uses       |
| ElasticSan                 |              0 |               1 | Array-item default                                                |
| ImageBuilder               |              0 |               3 | Empty-string and zero defaults                                    |
| Informatica                |              0 |              24 | Recursive update layout; Swagger absence unresolved               |
| fluxConfigurations         |              0 |               2 | False defaults                                                    |
| ScheduledQueryRuleApi      |              0 |               2 | Defaults beneath array items                                      |
| PipelineGroups             |              0 |              13 | Array defaults; source also includes removed-version declarations |
| DBforPostgreSQL.Management |              0 |               3 | Empty-string and zero defaults                                    |
| hcpopenshiftclusters       |              0 |               1 | Array-item default                                                |

### Falsy defaults

AzureDataTransfer `models.flowprofile.tsp:218`:

```typespec
@minValue(0)
minimumSizeForExpansion?: int64 = 0;
```

ImageBuilder `models.tsp:652` and `:660`:

```typespec
vmSize?: string = "";
```

```typespec
osDiskSizeGB?: int32 = 0;
```

The Swagger implementation checks `if (properties[prop].default)`, whereas the
TypeSpec implementation checks whether a default exists. Thus `false`, `0`,
and `""` are intentional additional checks, not missing Swagger observations
that should be fabricated.

**Disposition: No TypeSpec rule update required** under the current authored
contract; reproducing Swagger's truthiness behavior would remove coverage.

### Array traversal

Edge `WorkflowVersion.tsp:51`:

```typespec
concurrency?: int32 = 1;
```

The actual native paths include
`properties.stageSpec[].taskOption.concurrency` and
`properties.stageSpec[].taskOption.errorAction.mode`, each twice.
The Swagger implementation recurses into object properties but not `items`;
the TypeSpec linter deliberately traverses array items. The same boundary was
checked in ElasticSan, ScheduledQueryRuleApi, PipelineGroups and
hcpopenshiftclusters. Required replacement-item fields remain allowed by the
canonical tests; this extension must not be described as historical Swagger
coverage.

**Disposition: No TypeSpec rule update required** under the current array policy.
Versioned source findings in PipelineGroups remain subject to the source-scope
limitation, not a same-version correspondence claim.

### Recursive Informatica layout

**Status:** Native layout is evidenced; Swagger omission mechanism unresolved.
Selected API version: `2025-11-27`.
`main.tsp:737`:

```typespec
model OrganizationPropertiesCustomUpdate {
  @doc("Informatica Organization properties")
  informaticaOrganizationProperties?: InformaticaOrganizationResourceUpdate;
}
```

The resource's `OrganizationProperties` instead declares:

```typespec
@doc("Informatica Organization properties.")
informaticaProperties?: InformaticaProperties;
```

The saved Swagger retains the same mismatch:

```json
{
  "OrganizationPropertiesCustomUpdate": {
    "properties": {
      "informaticaOrganizationProperties": {
        "$ref": "#/definitions/InformaticaOrganizationResourceUpdate"
      }
    }
  },
  "OrganizationProperties": {
    "properties": {
      "informaticaProperties": {
        "$ref": "#/definitions/InformaticaProperties"
      }
    }
  }
}
```

The update type recursively reaches itself. The TypeSpec linter reports 24
missing descendant paths while terminating that recursion. The baseline reports
zero selected findings. Saved validator output confirms the selected rules were
configured and the command returned normally; its stderr is empty. This does
not explain why the resolved Swagger comparison omitted the mismatch.

**Disposition: No TypeSpec rule update is demonstrated for the missing keys.**
The Swagger omission and exact parent/leaf correspondence remain unresolved;
do not normalize 24 findings to one defect or certify equivalence.

## Parent and leaf counting

EdgeOrder has **8 / 29** findings: Swagger layout 3 plus required 5; TypeSpec
layout 23, required 5 and default 1.
Swagger reports absent `properties.forwardAddress`, `properties.preferences`
and `properties.notificationEmailList`. TypeSpec reports leaf paths including
`properties.forwardAddress.shippingAddress.streetAddress1`.

The saved source includes `models.tsp:1969`:

```typespec
@minValue(0)
quantity?: int32 = 0;
```

Family-level parent/leaf fanout explains 20 additional layout occurrences and
the zero default explains one additional check. Equal required-family totals
do not, by themselves, prove exact pairing.

**Disposition: No TypeSpec rule update required for the documented leaf and
falsy-default policies.** No common actionable count is asserted.

## Outliers

| Project            | Swagger / TypeSpec | Evidence and remaining limit                                                                                                                                                                                                                    |
| ------------------ | -----------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EventGrid          |          117 / 200 | Swagger: safety 62, layout 55. TypeSpec: required 49, default 24, layout 127. Source reuse and layout fanout are material; full correspondence is unassessed.                                                                                   |
| NetApp             |             6 / 42 | TypeSpec includes 26 defaults, including array-item defaults, and a removed-version layout target. Residual correspondence is unassessed.                                                                                                       |
| Search             |             6 / 39 | TypeSpec has layout 27, default 8, required 4. Source/version/resource-selection boundaries need further correspondence analysis.                                                                                                               |
| SQL                |            47 / 17 | Swagger includes Create-only mutability and required fields retained in shared schemas; TypeSpec excludes ineffective PATCH input. It still reports four layout findings and thirteen required findings. Residual correspondence is unassessed. |
| DomainRegistration |             16 / 1 | Create-only contacts and Read-only subtrees are excluded. Native retains the `autoRenew = true` default.                                                                                                                                        |

Concrete source examples:

```typespec
// EventGrid models.tsp:3281
endpointType: EndpointType;
```

```typespec
// NetApp NetAppAccount.tsp:627
organizationalUnit?: string = "CN=Computers";
```

```typespec
// NetApp Volume.tsp:1357
@removed(Versions.v2026_06_15_preview)
@renamedFrom(Versions.v2026_06_15_preview, "usageThreshold")
@maxValue(2638827906662400)
@minValue(53687091200)
usageThreshold20250901?: int64;
```

```typespec
// DomainRegistration models.tsp:795
@visibility(Lifecycle.Create)
contactAdmin: Contact;
```

EventGrid demonstrates why location deduplication is not normalization:
117 / 200 raw findings become 45 Swagger paths / 27 TypeSpec source locations,
reversing the direction. Distinct checks share locations; repeated source uses
and operations are still separate raw occurrences.

**Disposition:** No repair follows merely from these raw counts. The known
array, effective-input and counting policies explain material categories.
For unresolved layout/correspondence residuals, whether a TypeSpec update is
required remains **unassessed**, not approved or silently waived.
All 60 unequal-count projects with findings on both sides remain individually
enumerated, even where only representative causes have been investigated.
This analysis does not claim that every within-project residual is explained.

## Mapping and semantic controls

| Original Swagger linter    | Material checks                                                                              | Native evidence and conclusion                                                                                                                                                                                                                  |
| -------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PatchBodyParametersSchema  | Required/default/Create-only body properties; top-level identity exemption; object recursion | Violating required/default/exposed-Create cases, compliant optional input, excluded Create-only input, identity exemption and suppression pass through injected packages. Falsy defaults, effective visibility and arrays intentionally differ. |
| ConsistentPatchProperties  | Encoded resource/request layout; response or GET selection                                   | Injected missing-key and compliant partial-shape controls pass; canonical tests cover association, status/GET selection, unions, inheritance and overrides. Source/Swagger layout parity is not established.                                    |
| UnSupportedPatchProperties | Immutable root paths and writable provisioning state                                         | Injected immutable and compliant controls pass; canonical tests cover all configured paths and effective visibility. Read-only saved-reference differences remain explicit.                                                                     |

Each member's Swagger observations remain separate. The native rule runs once.
Native message families are not a deterministic attribution of individual
findings to a Swagger member. There is no group-equivalence or source-regression
claim based only on equal totals, overlap, test counts or location deduplication.
