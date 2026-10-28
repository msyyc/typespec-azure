# DeleteResponseBodyEmpty supporting evidence

## Difference summary

These are all seven projects whose reported counts differ. Unchanged projects
remain in the complete machine-readable population, not in this difference table.

| Project suffix             | Swagger | TypeSpec | Signed difference | Absolute difference | Relative difference |
| -------------------------- | ------: | -------: | ----------------: | ------------------: | ------------------: |
| DeviceProvisioningServices |       1 |        0 |                 1 |                   1 |                100% |
| IoTHub                     |       2 |        0 |                 2 |                   2 |                100% |
| SecurityInsights           |       2 |        0 |                 2 |                   2 |                100% |
| AppService                 |      10 |        0 |                10 |                  10 |                100% |
| aks                        |       0 |        1 |                -1 |                   1 |                100% |
| policy                     |       1 |        2 |                -1 |                   1 |                 50% |
| Search                     |       1 |        2 |                -1 |                   1 |                 50% |

The denominator for relative difference is `max(Swagger, TypeSpec)`.
There are 30 exact matching operation/status groups, 15 Swagger-only groups
with explicit source suppression, two native DELETE-only client groups, and
one native POST `202` finding outside the mapping. Multiplicities are retained.
The comparison did not match diagnostic messages or fuzzy operation names.

All source citations below use frozen specs commit
`2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`. JSON excerpts were read from the
verified saved baseline, not regenerated output.

## Device Provisioning Services

- Project: `specification/deviceprovisioningservices/resource-manager/Microsoft.Devices/DeviceProvisioningServices`.
- Selected API version: `2026-11-01`.
- Group: DELETE `.../provisioningServices/{resourceName}/privateEndpointConnections/{privateEndpointConnectionName}`, status `200`.
- Counts: Swagger 1; TypeSpec 0.
- Source: [PrivateEndpointConnection.tsp, lines 74-88](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/deviceprovisioningservices/resource-manager/Microsoft.Devices/DeviceProvisioningServices/PrivateEndpointConnection.tsp#L74-L88).

```typespec
#suppress "@azure-tools/typespec-azure-resource-manager/no-response-body" "The existing API returns the PrivateEndpointConnection resource in the 200 and 202 delete response bodies. Keeping for backward compatibility."
deletePrivateEndpointConnection is PrivateEndpointConnectionsOps.DeleteWithoutOkAsync<
  PrivateEndpointConnection,
  Response =
    | ArmResponse<PrivateEndpointConnection>
    | (ArmDeleteAcceptedLroResponse<LroHeaders = ArmLroLocationHeader<FinalResult = PrivateEndpointConnection> &
        Azure.Core.Foundations.RetryAfterHeader> & {
        @bodyRoot
        _: PrivateEndpointConnection;
      })
    | ArmDeletedNoContentResponse
>;
```

The saved `IotDpsResource_DeletePrivateEndpointConnection` operation contains:

```json
{
  "200": {
    "description": "Azure operation completed successfully.",
    "schema": { "$ref": "#/definitions/PrivateEndpointConnection" }
  }
}
```

Swagger reports the body; TypeSpec honors the explicit operation suppression.
**Disposition: No TypeSpec rule update required.** Do not remove source
suppression or claim that the existing API became compliant.

## IoT Hub

- Project: `specification/iothub/resource-manager/Microsoft.Devices/IoTHub`.
- Selected API version: `2026-10-01-preview`.
- Counts: Swagger 2; TypeSpec 0.

| DELETE path suffix                                                                  | Status | Swagger | TypeSpec | Frozen source                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------- | ------ | ------: | -------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `IotHubs/{resourceName}`                                                            | 200    |       1 |        0 | [IotHubDescription.tsp:111-125](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/iothub/resource-manager/Microsoft.Devices/IoTHub/IotHubDescription.tsp#L111-L125)             |
| `iotHubs/{resourceName}/privateEndpointConnections/{privateEndpointConnectionName}` | 200    |       1 |        0 | [PrivateEndpointConnection.tsp:80-96](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/iothub/resource-manager/Microsoft.Devices/IoTHub/PrivateEndpointConnection.tsp#L80-L96) |

Both operations explicitly suppress `no-response-body` with backward-compatibility
justifications. Both customize the response with `ArmResponse<Resource>`.
The saved Swagger reports the corresponding two `200.schema` nodes.
Case differences in the actual HTTP paths are preserved, not normalized.
**Disposition: No TypeSpec rule update required.**

## Security Insights

- Project: `specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights`.
- Selected API version: `2025-10-01-preview`.
- Group: DELETE `.../providers/Microsoft.SecurityInsights/automationRules/{automationRuleId}`, statuses `200` and `204`.
- Counts: Swagger 2; TypeSpec 0.
- Source: [AutomationRule.tsp:98-114](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/AutomationRule.tsp#L98-L114).

```typespec
#suppress "@azure-tools/typespec-azure-resource-manager/no-response-body" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
#suppress "@azure-tools/typespec-azure-core/response-schema-problem" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
@tag("automationRules")
delete is Extension.DeleteSync<
  OperationalInsights,
  AutomationRule,
  Response =
    | ArmResponse<unknown>
    | (NoContentResponse & {
        #suppress "@azure-tools/typespec-azure-core/no-unknown" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
        @body body: unknown;
      }),
  Error = CloudError
>;
```

Saved operation `AutomationRules_Delete` has `"schema": {}` on both responses.
An empty schema object is truthy for the Swagger rule's `falsy` predicate;
it does not mean that no response body exists. One source suppression covers
the two status-specific TypeSpec findings.
**Disposition: No TypeSpec rule update required.**

## App Service

- Project: `specification/web/resource-manager/Microsoft.Web/AppService`.
- Selected API version: `2026-07-15`.
- Counts: Swagger 10; TypeSpec 0.
- Every row below has two Swagger findings, one for `200` and one for `204`.
  All five operations explicitly suppress the mapped TypeSpec rule.

| DELETE path suffix below `providers/Microsoft.Web/`                                     | Swagger | TypeSpec | Frozen source                                                                                                                                                                                                                                                              |
| --------------------------------------------------------------------------------------- | ------: | -------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hostingEnvironments/{name}/configurations/customdnssuffix`                             |       2 |        0 | [CustomDnsSuffixConfiguration.tsp:61-73](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/CustomDnsSuffixConfiguration.tsp#L61-L73)                                 |
| `hostingEnvironments/{name}/privateEndpointConnections/{privateEndpointConnectionName}` |       2 |        0 | [RemotePrivateEndpointConnectionARMResource.tsp:94-111](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/RemotePrivateEndpointConnectionARMResource.tsp#L94-L111)   |
| `sites/{name}/privateEndpointConnections/{privateEndpointConnectionName}`               |       2 |        0 | [RemotePrivateEndpointConnectionARMResource.tsp:268-285](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/RemotePrivateEndpointConnectionARMResource.tsp#L268-L285) |
| `sites/{name}/slots/{slot}/privateEndpointConnections/{privateEndpointConnectionName}`  |       2 |        0 | [RemotePrivateEndpointConnectionARMResource.tsp:362-379](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/RemotePrivateEndpointConnectionARMResource.tsp#L362-L379) |
| `staticSites/{name}/privateEndpointConnections/{privateEndpointConnectionName}`         |       2 |        0 | [RemotePrivateEndpointConnectionARMResource.tsp:180-197](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/web/resource-manager/Microsoft.Web/AppService/RemotePrivateEndpointConnectionARMResource.tsp#L180-L197) |

The custom DNS operation uses `ArmResponse<unknown>` and
`ArmDeletedNoContentResponse & { @body _: unknown; }`; the other four have the
same material `200`/`204` body shapes and explicit operation-level suppression.
The exact HTTP metadata confirms both slots on each operation.
**Disposition: No TypeSpec rule update required.**

## AKS

- Project: `specification/containerservice/resource-manager/Microsoft.ContainerService/aks`.
- Selected API version: `2026-07-02-preview`.
- Counts: Swagger 0; TypeSpec 1.
- Source: [AgentPool.tsp:125-138](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/AgentPool.tsp#L125-L138).

```typespec
@summary("Upgrades the node image version of an agent pool to the latest.")
upgradeNodeImageVersion is ArmResourceActionAsyncBase<
  AgentPool,
  void,
  | {
      ...AcceptedResponse;
      ...ArmCombinedLroHeaders<FinalResult = void>;
      ...Azure.Core.Foundations.RetryAfterHeader;

      @body
      body: AgentPool;
    }
  | OkResponse,
  Foundations.DefaultBaseParameters<AgentPool>
>;
```

Native HTTP metadata identifies a POST operation with a body-bearing `202`.
The existing TypeSpec policy reports it. The Swagger rule selects only DELETE
`200`/`204` schemas, so it cannot report this group. The metadata join, rather
than diagnostic-message text, establishes this exclusion.
**Disposition: No TypeSpec rule update required.** Keep the broader existing check.

## Policy

- Project: `specification/resources/resource-manager/Microsoft.Authorization/policy`.
- Counts: Swagger 1; TypeSpec 2.
- Matching group: DELETE `/{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}`, status `200`, one finding per linter.
- Extra group: DELETE `/{policyAssignmentId}`, status `200`, Swagger 0 / TypeSpec 1.
- Sources: [PolicyAssignment.tsp:146-150](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/resources/resource-manager/Microsoft.Authorization/policy/PolicyAssignment.tsp#L146-L150)
  and [client.tsp:93-102](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/resources/resource-manager/Microsoft.Authorization/policy/client.tsp#L93-L102).

```typespec
@summary("Deletes a policy assignment.")
@scope("java,csharp,go,python")
@clientLocation(PolicyAssignments)
@delete
@route("/{+policyAssignmentId}")
op deleteById(
  ...PolicyAssignmentIdParameter,
  ...Azure.Core.Foundations.ApiVersionParameter,
): PolicyAssignment | ArmDeletedNoContentResponse | ErrorResponse;
```

The source-mode program includes this client customization in addition to the
service operation. Saved Swagger contains `PolicyAssignments_Delete` on the
service path with `200.schema.$ref = "#/definitions/PolicyAssignment"`; it has
no corresponding DELETE on `/{policyAssignmentId}`.
**Disposition: No TypeSpec rule update required.** This is a source/emission
population difference, not two Swagger occurrences collapsed into one.

## Search

- Project: `specification/search/resource-manager/Microsoft.Search/Search`.
- Counts: Swagger 1; TypeSpec 2.
- Matching group: DELETE `.../searchServices/{searchServiceName}/privateEndpointConnections/{privateEndpointConnectionName}`, status `200`.
- Extra group: DELETE `.../searchServices/{searchServiceName}/{privateEndpointConnectionName}`, status `200`, Swagger 0 / TypeSpec 1.
- Sources: [PrivateEndpointConnection.tsp:78-94](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/search/resource-manager/Microsoft.Search/Search/PrivateEndpointConnection.tsp#L78-L94)
  and [client.tsp:498-524](https://github.com/Azure/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/search/resource-manager/Microsoft.Search/Search/client.tsp#L498-L524).

The client operation is explicitly documented as a client-only override. Its
`@autoRoute @delete` operation `privateEndpointConnectionsDeleteCustomization`
returns `ArmResponse<Microsoft.Search.PrivateEndpointConnection>`. Native HTTP
metadata proves the extra path above; the missing `privateEndpointConnections`
segment must not be silently normalized away.

Saved Swagger contains `PrivateEndpointConnections_Delete` on the service path
with `200.schema.$ref = "#/definitions/PrivateEndpointConnection"` and no
corresponding DELETE on the customization path.
**Disposition: No TypeSpec rule update required.**

## Reproduction and limits

The complete source-mode run used the pinned shared Swagger baseline with
`--baseline-policy frozen-reference --scope source`, no filter or limit, and
the immutable candidate's 17 package artifacts. It executed native diagnostics
only; no Swagger was regenerated.

The focused HTTP metadata helper joins each saved native diagnostic to an
operation by exact source file, line, and column. It then uses native HTTP
method/path/status information. All 33 diagnostics were attributable:
32 are DELETE `200`/`204` findings and one is an unrelated `202` finding.
Exact wire keys produce 30 matching groups and the 17 DELETE-only differences
listed in the machine-readable reconciliation. Source suppressions account for
15 of those; client-only declarations account for the other two.

This investigation does not authorize removal of author suppressions, claim
every suppressed API is compliant, or infer one-to-one diagnostic correspondence
from aggregate equality. Historical aggregate coverage reports are not inputs
to this pinned native-baseline comparison.

The semantic investigation and
[independent fresh-checkout recovery](runs/native-full487-run1/recovery-receipt.json)
are complete. Both independent local and GitHub review checkpoints passed at
native commit `8ccd925220ca8a92cdbc4c7ec06bb656c4f831ab`, with one Balanced
GitHub round per checkpoint and no review comments or unresolved threads.
The [review receipts](runs/native-full487-run1/review-checkpoints.json) preserve
the distinct request/review IDs, parent verification, local readiness reviewer,
and all ten passing required CI checks. The
[validation summary](runs/native-full487-run1/validation.json) preserves
exact-source test/documentation results and the original failures; these
receipts do not relabel supplemental limitations as passing checks.

### Portable inputs

The [provenance](runs/native-full487-run1/provenance.json) records the exact
candidate/core/specs/tooling commits, shared-baseline descriptor, artifact
checksums, and actual loaded package entrypoint hashes. The committed
[observations](runs/native-full487-run1/observations.json) retain the complete
487-project population, all 45 Swagger findings, all 33 native diagnostics,
and deterministic HTTP attribution. Suppressed operations are retained
[separately](runs/native-full487-run1/suppressed-http-operations.json).

From `runs\native-full487-run1` in a fresh evidence checkout:

```powershell
node .\reanalyze-observations.mjs .\observations.json .\replayed-reconciliation.json
```

Compare its parsed JSON with `reconciliation.json`. The original deterministic
reanalysis bytes have SHA-256
`41b7de72b8c8d9874c291e728bd0f89118daf82e2f91552d4fe0fde93b9c9995`.
This command reanalyzes observations; it does not rerun native diagnostics.

Recover the 17 candidate artifacts and frozen shared-baseline archive into new,
separate directories:

```powershell
gh release download lintdiff-delete-response-body-empty-20261028 --repo msyyc/typespec-azure --dir <new-artifact-directory>
gh release download swagger-lint-baseline-20261026-2cd3c5dd --repo msyyc/azure-rest-api-specs --pattern swagger-arm-20261026-2cd3c5dd.tar.gz --dir <new-baseline-directory>
```

Verify every SHA-256 and byte count against the provenance before use. Source
recovery uses `msyyc/azure-rest-api-specs` ref
`evidence/long-running-operations-options-validator-20261022-source`, which must
resolve to `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`, not the baseline metadata
commit. The [recovery configuration](runs/native-full487-run1/reproduction.json)
records the full native coverage invocation, selection and runtime policies.
Do not resolve latest packages or regenerate Swagger. A new native execution
requires recovered runtime checks and positive/compliant controls; the retained
package entrypoint identities do not claim a sealed transitive dependency lock.
