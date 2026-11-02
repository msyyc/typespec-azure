# Detailed PATCH migration analysis

This November 2 analysis uses the unchanged PR implementation and October 30
observations. It explains count mechanisms; it does not convert an intentional
native policy into Swagger equivalence. No Swagger was regenerated and no
production source, ruleset, test expectation or PR implementation was repaired.

The [difference-only inventory](detailed-differences.md) starts with all
**87 differing projects** and groups their evidence by exact PATCH route.
The [machine-readable assessment](runs/20261102-semantic-analysis/difference-ledger.json)
retains every unmatched check/path and source inspection. Matching observations
remain in the complete trace archive, not in the difference inventory.

## Counting levels

| Level                                                | Swagger linter | TypeSpec linter | Meaning                                                                                            |
| ---------------------------------------------------- | -------------: | --------------: | -------------------------------------------------------------------------------------------------- |
| Original reported diagnostics                        |            975 |           1,337 | Preserve the full-population observations                                                          |
| Function/check observations before reporting         |          1,057 |           1,337 | Spectral suppresses 82 returned occurrences; the TypeSpec observer forwards all findings unchanged |
| Distinct project/route/check/property-path-text keys |          1,057 |           1,333 | Four additional TypeSpec occurrences come from different NetApp source operations; retain all four |
| Affected exact PATCH routes                          |            304 |             321 | Shared coarse unit; 277 shared, 27 Swagger-only, 44 TypeSpec-only                                  |

The route identity includes project, exact case-sensitive route and parameter
names; the method is always PATCH. Parameter renaming is not canonicalized.
One route can contain many independent violations, so this is not a count of
defects or authoring actions. Both the original reported Swagger findings and
the full callback observations independently produce the same 304-route set.

Check/path accounting uses project, exact route, intrinsic check family and
encoded property-path **text**, retaining multiplicity. It is not a semantic
join: emitted parent paths, source leaves, literal dotted names such as
`@odata.type`, API versions and declaration identities can differ. The
834-occurrence intersection therefore means equal accounting keys, **not
834 proven equivalent defects**. No arbitrary callback is selected to represent
a collapsed reported finding.

| Check family      | Swagger reported | Swagger function checks | TypeSpec reported | Equal-key occurrences | Swagger remainder | TypeSpec remainder |
| ----------------- | ---------------: | ----------------------: | ----------------: | --------------------: | ----------------: | -----------------: |
| Required          |              456 |                     531 |               478 |                   451 |                80 |                 27 |
| Default           |              231 |                     238 |               436 |                   234 |                 4 |                202 |
| Update visibility |               28 |                      28 |                 0 |                     0 |                28 |                  0 |
| Missing/layout    |              150 |                     150 |               361 |                    89 |                61 |                272 |
| Immutable         |              110 |                     110 |                62 |                    60 |                50 |                  2 |
| Total             |              975 |                   1,057 |             1,337 |                   834 |               223 |                503 |

TypeSpec attribution observes the unchanged rule's actual `messageId` callback,
producing 914 safety, 361 layout and 62 immutable implementation-family findings.
It is not inferred from displayed text and does not create original Swagger
rule IDs in production diagnostics. The original three Swagger members remain
715 / 150 / 110 reported findings, counted separately.

Raw per-project direction remains 27 Swagger-higher / 56 TypeSpec-higher:
102 / 464 excesses, absolute difference 566, net TypeSpec +362. At the separate
function-observation level it is 29 / 52 projects, 134 / 414 excesses, absolute
548, net +280. Neither analysis cancels opposing project gaps. Spectral's
82-occurrence reporting reduction accounts for the difference between the two
net deltas; it does not explain the underlying semantic differences.

## Reporting-stage collapse

**Classification:** count-only reporting difference. The original three
functions return 1,057 occurrences with distinct full check/path keys.
Spectral reports 975, losing 75 required and seven default occurrences in
13 projects. The original 975 reports reproduce the retained baseline's
project/document/rule/message multiset exactly.

The safety function returns parent-oriented error paths. Spectral associates
those with document locations, then deduplicates by rule, reported path, source
and message. Different nested properties can acquire the same fingerprint.
The observer on Spectral's actual unchanged `prepareResults` confirms
**43 incoming results become 16** in DomainRegistration.

For example, four separate callback paths:

```text
properties.contactAdmin.addressMailing.address1
properties.contactBilling.addressMailing.address1
properties.contactRegistrant.addressMailing.address1
properties.contactTech.addressMailing.address1
```

all yield the same `property:address1` message and reported path ending in
`patch.parameters[4].schema.properties.properties`. They collapse to one
reported occurrence. This is not permission for this analysis to discard
distinct violations; all four callbacks remain in the archive and ledger.

Pinned implementation:
[safety function](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-body-parameters.ts).
The loaded Spectral core is `1.24.0`; its `runner/utils/results.js` computes the
fingerprint and filters duplicate fingerprints. The
[reporting receipt](runs/20261102-semantic-analysis/reporting-control.json)
contains the actual pre/post results.

**Disposition: No TypeSpec rule update required** for Spectral's reporting
collapse. Do not repair TypeSpec to imitate lost Swagger reports.

## Effective input and synthetic fields

All **223** Swagger-side unmatched function checks were inspected against their
exact compiled source route and encoded property chain, in **48 projects**:

| Count | Captured cause                                                                                  |
| ----: | ----------------------------------------------------------------------------------------------- |
|   165 | Excluded PATCH input or ancestor: required 74, default 4, visibility 28, layout 9, immutable 50 |
|    52 | Missing parent paths with TypeSpec missing descendants                                          |
|     5 | Emitted required discriminator absent as an authored source property                            |
|     1 | Candidate effective PATCH field is optional                                                     |

These inspections cover all 27 Swagger-only affected routes, not only the eight
Swagger-only projects. See the [Read-only](fresh-examples.md#read-only-reference-siblings)
and [excluded-input](fresh-examples.md#excluded-input) examples. In Authorization,
the direct configuration's authored `alertConfigurationType` is diagnosed;
the same discriminator under Read-only `properties.alertConfiguration` is not
PATCH input. It is not a missing discriminator implementation.

The five emitted-only discriminator checks are three DevOpsInfrastructure
`kind` fields and two DataReplication `instanceType` fields. The latter includes
this verified source at
[models.tsp:2099](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/recoveryservicesdatareplication/resource-manager/Microsoft.DataReplication/DataReplication/models.tsp#L2099):

```typespec
@discriminator("instanceType")
model ProtectedItemModelCustomPropertiesUpdate {}
```

The emitted schema has required `instanceType`; source `walkJsonProperties`
finds no such property and records the model's discriminator metadata.
Authored required discriminator properties are independently covered.

CommunityTraining's `sku.name` is the remaining required finding. The candidate
effective PATCH metadata reports `isOptional: true`, while the saved Swagger
schema lists `name` as required. Its originating common `Sku` declaration
contains `name: string`; originating syntax alone is not the effective PATCH
model. No authored `name?: string` is fabricated.

**Disposition: No TypeSpec rule update required** to diagnose excluded input,
synthesized source properties or an effectively optional property as authored
required PATCH fields. These differences prevent bug-for-bug equivalence.

## Parent and leaf accounting

The 52 unmatched Swagger parent findings have TypeSpec missing descendants.
There are **175 unmatched TypeSpec leaf observations below Swagger missing
parent paths**, after the disjoint accounting priorities below. These are
related structural regions, not 52 proven identical fixes.

[EdgeOrder](fresh-examples.md#parent-and-leaf-counting) is the smallest
representative: its three missing parent branches become 23 missing leaves.
The original [diffSchema](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/utils.ts#L140)
stops at a missing parent; the TypeSpec visitor continues into supported
children. Required/default checks at those children remain independent checks.

**Disposition: No TypeSpec rule update required** for the documented leaf
reporting policy. Do not deduplicate distinct leaf problems to force parity.

## Defaults and arrays

TypeSpec reports **128 falsy defaults**: 96 false, 26 numeric zero and six empty
strings. It also reports **88 defaults beneath arrays**, of which **23 are
already in the falsy set**. Thus the union is 128 + 88 - 23 = **193 defaults**,
not 216. Add 14 array-layout findings for **207 disjoint observations**.

The corresponding Swagger implementations test default truthiness and recurse
through object properties, not array `items`. The verified
[default and array source examples](fresh-examples.md#native-only-projects)
and canonical replacement-item controls establish the boundary: required
array-item descendants remain allowed, while defaults/layout are checked.

**Disposition: No TypeSpec rule update required** under the current authored
default/array policy; matching Swagger would intentionally remove coverage.

## Recursive reference boundary

Informatica contributes **0 reported Swagger / 24 TypeSpec layout findings**.
The actual unchanged Swagger callback receives:

```json
{ "$ref": "#/definitions/OrganizationPropertiesCustomUpdate" }
```

as request `properties`, with zero inspectable keys. The response properties are
resolved and include `informaticaProperties`. Original `getProperties` merges
`allOf` and properties but does not follow this remaining recursive `$ref`;
`diffSchema` therefore sees no request children.

An analysis-only in-memory control replaces the recursive
`informaticaOrganizationProperties` child with a scalar without changing its
absent name. The same Swagger function then produces **two** missing branches:
`properties.informaticaOrganizationProperties` and `properties.existingResourceId`.
This is a causal control, not new emitted Swagger or a replacement baseline.
The [authored and emitted snippets](fresh-examples.md#recursive-informatica-layout)
remain unchanged.

The same observer establishes the reference-sibling boundary in Dynatrace:
raw `SubscriptionList.provisioningState` has `$ref` and `readOnly: true`;
the resolved enum delivered to the immutable function lacks `readOnly`.
Annotation-preserving inlining changes its result **1 to 0**. This observation
does not independently decide whether emitted `$ref` siblings or resolver
interpretation should change.

The [resolver controls](runs/20261102-semantic-analysis/resolver-controls.json)
retain original/counterfactual counts **0, 2, 1, 0**, messages and callback inputs.

**Disposition: No TypeSpec rule update required** to reproduce these resolution
boundaries. The recursive request omission is explained; 24 leaf findings are
not normalized to one defect or to the two counterfactual branches.

## Source and operation populations

The ordered disjoint ledger assigns **76** additional TypeSpec observations to
source/operation population differences:

| Category                                                                                                   | Observations |
| ---------------------------------------------------------------------------------------------------------- | -----------: |
| ManagedNetworkFabric / ProgrammableConnectivity version populations after higher-priority array accounting |           21 |
| Search client-only override                                                                                |           34 |
| Additional version-scoped CognitiveServices / AzureFleet / StandbyPool source                              |            7 |
| Removed NetApp field/model                                                                                 |            2 |
| Additional same-route NetApp source-operation occurrences                                                  |            3 |
| No identical saved PATCH route                                                                             |            7 |
| Removed DesktopVirtualization field / DeviceRegistry ancestor                                              |            2 |

The 21 first-row observations are not a revised total for those projects:
their complete **0 / 35** raw findings remain intact; fourteen additional
ManagedNetworkFabric array-layout observations were assigned earlier.
See the [versioning source excerpts](fresh-examples.md#version-populations).

Search has **6 / 39 raw findings**. All **34** unmatched TypeSpec findings come
from `Customizations.searchUpdateCustomization`, not the ARM service operation.
Its [client.tsp:220](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/search/resource-manager/Microsoft.Search/Search/client.tsp#L220)
explicitly calls it a client-only override:

```typespec
@autoRoute
@patch(#{ implicitOptionality: false })
@action("searchUpdateCustomization")
op searchUpdateCustomization(
```

The override's body has a `properties: SearchServiceUpdate` wrapper and optional
request-options parameter. Those declarations are linted under source scope
but are not an emitted ARM route. The ordinary service update has five native
findings matching five Swagger check/path keys; the sixth Swagger finding is
an excluded immutable field.

NetApp's `updatePrevious` and `update` coexist in unprojected source on the same
route. Four diagnostic keys occur twice; all occurrences are retained. Three
excess occurrences are assigned here; the fourth is already an array default.
`updatePrevious` is explicitly removed for selected `2026-06-15-preview`.

The seven no-identical-PATCH observations are Batch certificate input (three),
Cdn key group (one), DeviceRegistry discovered asset (one), RecoveryServicesBackup
recovery point (one), and policy-assignment-by-ID (one). Exact saved route
inspection finds six observations at absent routes and one at a GET-only route. This is an exact
route/method result, not a claim that URI-template renaming or API projection
has been semantically aligned.

Two additional examples:

```typespec
// DesktopVirtualization/models.tsp:1707
@removed(Versions.vLatestPreview)
type: VirtualMachineDiskType;
```

```typespec
// DeviceRegistry/assetEndpointProfiles.tsp:49
@removed(Versions.v2024_09_01_preview)
userAuthentication?: Authentication;
```

Their corresponding callback request chains omit those fields; the source
observer still sees the unprojected declarations. Complete exact routes,
version annotations and target citations are retained in the ledger/archive.

**Disposition: No TypeSpec rule update required** to explain unprojected
source/client populations. A same-version/service-only assessment would require
an explicitly changed comparison policy; it is not fabricated here.

## Representation policy boundaries

These **21** findings are not left as unexplained arithmetic. Their mechanisms
are captured, but they must not be approved as exact emitted-layout parity.

### Associated-resource name: 12 findings

Automation contributes eleven extra missing-`name` layout findings and Resources
one. Saved request and response schemas both contain `name`; response `name`
is Read-only. The candidate's associated resource inherits
[ResourceNameParameter](https://github.com/msyyc/typespec-azure/blob/94b316787e2a19847c26986412ce254ca4da33b4/packages/typespec-azure-resource-manager/lib/models.tsp#L35):

```typespec
@path
name: Type;
```

The actual metadata probes establish:

```text
isPathParam(name) = true
isPayloadProperty(name, Visibility.All, false) = false
isPayloadProperty(name, Visibility.All, true) = true
```

The rule prioritizes associated resources with `isExplicit: false`. Its layout
property filter consequently excludes this `name` and reports it as missing.
The Swagger linter sees the emitted JSON response `name`, so does not report
the missing-layout check. Immutable-name checks are independent and are not
removed or deduplicated.

**Disposition: No TypeSpec source update is made for this reporting task.**
The existing associated-resource payload policy fully explains the count;
whether that extra missing-layout warning is desirable for the JSON-resource
contract remains a policy/correctness boundary. Exact emitted-layout parity
would require revisiting this filter and an immutable-versus-layout control,
not deleting twelve observations from the report.

### NetApp optional/default-free PATCH fields: nine findings

Seven source required checks and two default checks have no corresponding
Swagger findings. The actual resolved saved request fields exist but are
optional/default-free; corresponding response fields remain required/defaulted.
Representative authored source:

```typespec
// NetAppAccount.tsp:328
applicationId: string;
```

```typespec
// NetAppAccount.tsp:490
bindAuthenticationLevel?: BindAuthenticationLevel = BindAuthenticationLevel.Anonymous;
```

| Field                                                  | Candidate effective input | Saved resolved PATCH | Saved response      |
| ------------------------------------------------------ | ------------------------- | -------------------- | ------------------- |
| `properties.entraIdConfig.applicationId`               | Required                  | Not required         | Required            |
| `properties.ldapConfiguration.bindAuthenticationLevel` | Default `Anonymous`       | No default           | Default `Anonymous` |

The inspection covers all seven required fields and both defaults, not only
these representatives. The baseline was produced with a different library/
emitter closure, so the trace does not establish whether source transformation,
API projection or producer/runtime evolution accounts for every representation
change. No new emission was run to settle that separate question.

**Disposition: No TypeSpec source update is justified from this unaligned
reference alone.** The current authored-input checks are reproducible; their
nine findings are not equivalent to the saved emitted PATCH shape.

## Equal counts with different checks

CommunityTraining, ContainerInstance, DevOpsInfrastructure and SiteRecovery have
equal raw totals but different check/path observations. For example, an excluded
or synthesized required check can be offset by a newly checked falsy/array
default. Their differences appear in the same project/route ledger as unequal
projects; equal totals are not treated as passing correspondence.

## Reproducibility

- Candidate `94b316787e2a19847c26986412ce254ca4da33b4`, core
  `cefb035e7721a6fdcb6de605b5f469b93055a880`, frozen specs
  `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`; original baseline identity and
  [October recovery](fresh-evidence.md) remain unchanged.
- Node `26.5.0`, selected rulesets `2.2.6`, Spectral core `1.24.0`.
  The original producer creates a new resolver per document; this replay does
  the same and confines reference reads to the retained dataset.
- All 136 active projects reproduce 1,337 native source/message occurrences;
  selected Spectral replay reproduces 975 baseline reports. Zero worker,
  compilation or replay failures. The 351 projects without selected findings
  on either side retain their October observations.
- All 223 unmatched Swagger checks have successful source applicability probes;
  final native remainder probes cover 23 exact request chains, seven exact
  route-presence inspections and twelve resource-name metadata checks.
- [Analysis summary](runs/20261102-semantic-analysis/analysis.json),
  [difference ledger](runs/20261102-semantic-analysis/difference-ledger.json),
  [archive receipt](runs/20261102-semantic-analysis/archive.json), and
  [recovery/recount instructions](runs/20261102-semantic-analysis/README.md)
  preserve checks, provenance and boundaries. The archive retains all callbacks,
  actual operations, matched controls, original paths, source chains and
  analysis-only control inputs.
- No dependencies were installed. This documentation/evidence update does not
  rerun the unchanged 758-test suite or alter its 20 passing injected PATCH
  controls. The previously disclosed six unrelated generic-control failures
  remain failures; no full migration-readiness conclusion is claimed.

**Final assessment:** count mechanisms are substantially established and the
coarse common unit is now numerical. The TypeSpec linter is **not functionally
equal to the original Swagger group** under this source-versus-reference policy;
intentional extensions and the explicit representation-policy boundaries must
not be mistaken for regression-free one-to-one diagnostic parity.
