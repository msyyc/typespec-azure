# Source population and explicit path correspondence

The initial exact-path reader retained 130 scoped diagnostics without a saved
path/method candidate. All 130 remain in the reported TypeSpec total.
Source-only abstract syntax tree (AST) inspection then read each exact authored
declaration, its ancestors, SDK override statements and 21 project version enums.
It did not compile or project a program.

| Source-backed cause                          | Diagnostics | Saved counterpart                                                                    |
| -------------------------------------------- | ----------: | ------------------------------------------------------------------------------------ |
| SDK overrides outside the service HTTP graph |          46 | Not selected service operations                                                      |
| Unavailable in the retained API version      |          67 | Excluded by authored availability                                                    |
| Explicit legacy path-parameter rename        |          13 | Exact saved path after the authored substitution; required properties exist          |
| Explicit ARM provider namespace              |           4 | Exact saved path after replacing the template placeholder; required properties exist |
| Unexplained                                  |           0 | No numerical balancing category                                                      |

These are not equivalent-defect or normalized counts. The 17 path
correspondences supplement the 4,231 directly matched property-presence-valid
defaults: `4,231 + 17 = 4,248`. The other 113 are source/latest-version population
differences: `46 + 67 = 113`.

## Complete residual project index

The [full 490-project inventory](project-accounting.csv) preserves exact project
identities. Each row below names the service and its retained version. The
observations asset retains every full source symbol, file, line, column, source
hash, annotation and saved reference chain.

| Project                        | Selected API version | SDK override | Version-unavailable | Legacy rename | Provider namespace |
| ------------------------------ | -------------------- | -----------: | ------------------: | ------------: | -----------------: |
| Advisor                        | 2026-10-01           |            0 |                   5 |             0 |                  0 |
| ContainerApps                  | 2026-07-01           |            0 |                  14 |             0 |                  0 |
| Batch                          | 2025-06-01           |            0 |                   6 |             0 |                  0 |
| BotService                     | 2023-09-15-preview   |            2 |                   0 |             0 |                  0 |
| CertificateRegistration        | 2024-11-01           |            0 |                   0 |             2 |                  0 |
| ContainerInstance              | 2026-09-01-preview   |            0 |                   7 |             0 |                  0 |
| DocumentDB                     | 2026-07-15           |            0 |                  32 |             0 |                  0 |
| DataBox                        | 2025-07-01           |            2 |                   0 |             0 |                  0 |
| DataBoxEdge                    | 2023-12-01           |            1 |                   0 |             0 |                  0 |
| DataProtection                 | 2026-08-31-preview   |            0 |                   1 |             0 |                  0 |
| Education                      | 2021-12-01-preview   |            0 |                   0 |             0 |                  1 |
| GuestConfiguration/Assignments | 2024-04-05           |           10 |                   0 |             0 |                  0 |
| IoTHub                         | 2026-11-01           |            3 |                   0 |             0 |                  0 |
| ResourceGraph/ResourceChanges  | 2020-09-01-preview   |            0 |                   0 |             0 |                  2 |
| ResourceGraph/ResourceHistory  | 2021-06-01-preview   |            0 |                   0 |             0 |                  1 |
| Microsoft.Resources/resources  | 2025-04-01           |            0 |                   0 |             2 |                  0 |
| Search                         | 2026-11-01           |           24 |                   2 |             0 |                  0 |
| SecurityInsights               | 2025-10-01-preview   |            0 |                   0 |             1 |                  0 |
| Storage                        | 2026-09-01           |            2 |                   0 |             0 |                  0 |
| TrafficManager                 | 2026-09-01           |            1 |                   0 |             0 |                  0 |
| AppService                     | 2026-09-01           |            1 |                   0 |             8 |                  0 |
| **Total**                      |                      |       **46** |              **67** |        **13** |              **4** |

## SDK overrides

- **Classification:** source/Swagger population difference.
- **Coverage status:** existing source check executes; no corresponding selected
  service operation is asserted.
- **Evidence:** all 46 targets have exact authored `@@override` statements and
  are absent from the captured service HTTP graph.

The [IoTHub example](evidence-details.md#source-program-sdk-overrides-are-not-emitted-service-operations)
shows the three structural-default cases. The other 43 warnings have custom
source defaults with encoded `error.code` and `error.message` properties.
They still violate standard-model identity.

**analysis:** retain these source-scope diagnostics. Do not remove SDK
customizations or infer API-version removal merely to align counts. A different
reachability policy needs separate approval and a supported comparison profile.

## Version availability

- **Classification:** source/latest-version population difference.
- **Project/API version:** Batch / `2025-06-01`.
- **Coverage status:** source check executes; the selected Swagger excludes the
  unavailable declarations.

The [authored certificate operation](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/batch/resource-manager/Microsoft.Batch/Batch/Certificate.tsp#L43-L63)
contains this interface-member excerpt; documentation comments are omitted:

```text
#deprecated "Removal of feature"
@removed(Versions.v2025_06_01)
get is ArmResourceRead<
  Certificate,
  Response = ArmResponse<Certificate> & {
    @header("ETag")
    etag?: string;
  },
  Error = CloudError
>;
```

The retained API version is `2025-06-01`. The exact authored `Versions` enum
binds `v2025_06_01` to that value. All six certificate operations are marked
removed at that version. The unprojected program still contains them; the saved
Swagger has no matching path/method candidates.

| Engine          | Observed result                                                     |
| --------------- | ------------------------------------------------------------------- |
| Swagger linter  | No finding for these six excluded selected-version operations       |
| TypeSpec linter | Six default-payload warnings on the unprojected source declarations |

For all 67 version cases, the retained source receipts show an unavailable
operation or ancestor at the selected version. The helper uses the actual enum
order and the last applicable added/removed event, including re-addition.
It does not infer exclusion from a name containing `Preview`.

**analysis:** do not change production lint behavior to erase this declared
source-profile difference. These receipts are not a version-projected TypeSpec
run or evidence that arbitrary version-sensitive predicates were reevaluated.

## Explicit path representations

These 17 diagnostics are not source-population exclusions. Exact authored
annotations explain the path spelling difference. Applying only their literal
substitutions finds saved defaults with the required properties. Each warning is
counted once within the 4,248 stricter defaults.

### Legacy parameter names

- **Classification:** correspondence representation difference.
- **Project/API version:** CertificateRegistration / `2024-11-01`.
- **Coverage status:** stricter model-identity warning; saved property-presence
  check is compliant.

The [authored operation](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/certificateregistration/resource-manager/Microsoft.CertificateRegistration/CertificateRegistration/AppServiceCertificateOrder.tsp#L152-L166)
contains:

```text
@Azure.ResourceManager.Legacy.renamePathParameter(
  "certificateOrderName",
  "name"
)
retrieveCertificateActions is ArmResourceActionSync<
  AppServiceCertificateOrder,
  void,
  ArmResponse<CertificateOrderAction[]>,
  Error = DefaultErrorResponse
>;
```

Captured HTTP metadata uses
`/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/retrieveCertificateActions`.
The authored substitution yields the retained exact path with `{name}` instead.
Its `POST` operation ID is
`AppServiceCertificateOrders_RetrieveCertificateActions`.
The saved default schema is:

```json
{
  "$ref": "#/definitions/DefaultErrorResponse"
}
```

Reference resolution finds outer `error`, then `code`, `details`, `innererror`,
`message` and `target`.

| Engine          | Observed result                                                 |
| --------------- | --------------------------------------------------------------- |
| Swagger linter  | No diagnostic; required properties exist                        |
| TypeSpec linter | One warning; the custom default model is not the standard model |

The same explicit-annotation procedure accounts for 13 warnings across
CertificateRegistration, Microsoft.Resources/resources, SecurityInsights and
AppService. No case-insensitive, approximate-name or guessed parameter mapping
is used.

### Provider namespace placeholders

- **Classification:** correspondence representation difference.
- **Project/API version:** Education / `2021-12-01-preview`.
- **Coverage status:** stricter model-identity warning; saved property-presence
  check is compliant.

The [provider declaration](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/education/resource-manager/Microsoft.Education/Education/main.tsp#L33-L37)
uses `@armProviderNamespace` on `namespace Microsoft.Education`.
The [operation](https://github.com/Azure/azure-rest-api-specs/blob/6eeeaa99a3a7dea8eef4592a6a238fe2c6c129cc/specification/education/resource-manager/Microsoft.Education/Education/routes.tsp#L24-L30)
uses:

```typespec
@autoRoute
op redeemInvitationCode is ArmProviderActionSync<
  Request = RedeemRequest,
  Response = RedeemCodeResponse,
  Error = DefaultErrorResponse
>;
```

The captured path is
`/providers/Microsoft.ThisWillBeReplaced/redeemInvitationCode`.
The explicit provider declaration identifies `Microsoft.Education`; substituting
that literal yields the retained `POST /providers/Microsoft.Education/redeemInvitationCode`,
operation ID `RedeemInvitationCode`. Its saved default schema references
`#/definitions/ErrorResponseBody`, with nested `error.code` and `error.message`.

| Engine          | Observed result                          |
| --------------- | ---------------------------------------- |
| Swagger linter  | No diagnostic; required properties exist |
| TypeSpec linter | One warning on the custom default model  |

Three ResourceGraph operations use the same template placeholder and explicit
`@armProviderNamespace("Microsoft.ResourceGraph")` declarations. Together they
account for four diagnostics.

**analysis:** use these exact source-backed correspondences for this assessment.
They are not production enforcement, generic path normalization, proof of
identical current emission, or approval to alter either rule. Original captured
paths and both byte identities remain retained.

## Reanalysis

With the same recovered variables described in
[the main appendix](evidence-details.md#reanalyze-saved-data-without-running-either-linter):

```powershell
python "$Task\trace-source-population.py" `
  --baseline "$Baseline\dataset" `
  --source "$Observations\inspection\residual-source-evidence.json" `
  --projects "$Observations\inspection\residual-project-evidence.json" `
  --output "$Replay\residual-population"
```

Compare its `summary.json` and `residual-population.json` with the retained
`source-population` directory. Four availability controls check boundary removal,
re-addition, later removal and future addition. AST inspection used the
candidate compiler's separately payload-verified `dist/src/ast/index.js`
entrypoint, SHA-256
`8434fa440eb08e69bf19b3c1d638e2314ecd332c5afdfb0be48867bc2091553a`.
No compiler, emitter or Swagger linter runs during this saved-data reanalysis.
