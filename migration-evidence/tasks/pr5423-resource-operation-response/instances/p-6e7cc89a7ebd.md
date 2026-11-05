# specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement

[All project differences](../instance-correspondence.md#differing-projects).

**Project totals:** Swagger 22 raw / 22 member checks; TypeSpec 26 raw; 17 findings credited to the same comparison. Common project/route unit: 22 Swagger / 26 TypeSpec. Counts repeated across different members at the same operation are non-additive. TypeSpec counts refer only to arm-resource-operation-response, not the entire linter suite.

<a id="s-4f6894b5bb1a95e3"></a>

### PutRequestResponseSchemeArm: GatewayApi_CreateOrUpdate

**Identity:** `4f6894b5bb1a95e3`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/gateways/{gatewayId}/apis/{apiId}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** PUT lacks eligible createOrUpdate registration.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation        | Request schema                      | Success response schemas                                         |
| --------------------------------- | ----------------------------------- | ---------------------------------------------------------------- |
| `put` `GatewayApi_CreateOrUpdate` | `#/definitions/AssociationContract` | `200: #/definitions/ApiContract; 201: #/definitions/ApiContract` |

| TypeSpec operation                                                                                                                                                                                                                                                           | Effective request                             | Canonical association / request checked                                                  | Registered return candidates          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------- |
| [Microsoft.ApiManagement.GatewayContracts.gatewayApiCreateOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/GatewayContract.tsp#L320) | `Microsoft.ApiManagement.AssociationContract` | `Microsoft.ApiManagement.GatewayContract: lists.gatewayApiCreateOrUpdate; request=False` | `Microsoft.ApiManagement.ApiContract` |

**Explanation:** A name-keyed list association does not establish semantic createOrUpdate registration. The fixed request branch selects the actual operation identifier kind, not its retained map key.

**Decision:** Review registration, DTOs and parent/child modeling; do not broaden blindly to every PUT. [Legacy request/response contracts: evidence and tradeoff](../gap-analysis.md#legacy-contracts).

**Raw observation IDs:** `PutRequestResponseSchemeArm:3`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-e7a795042777d9cf"></a>

### PutGetPatchResponseSchema: DelegationSettings_CreateOrUpdate

**Identity:** `e7a795042777d9cf`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/delegation`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** Cross-operation comparison includes an absent selected response reference.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation                | Request schema                           | Success response schemas                      |
| ----------------------------------------- | ---------------------------------------- | --------------------------------------------- |
| `put` `DelegationSettings_CreateOrUpdate` | `#/definitions/PortalDelegationSettings` | `200: #/definitions/PortalDelegationSettings` |
| `get` `DelegationSettings_Get`            | `(no schema)`                            | `200: #/definitions/PortalDelegationSettings` |
| `patch` `DelegationSettings_Update`       | `#/definitions/PortalDelegationSettings` | `(no selected status)`                        |

| TypeSpec operation                                                                                                                                                                                                                                                           | Effective request                                  | Canonical association / request checked                                                    | Registered return candidates                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| [Microsoft.ApiManagement.DelegationSettings.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PortalDelegationSettings.tsp#L67) | `Microsoft.ApiManagement.PortalDelegationSettings` | `Microsoft.ApiManagement.PortalDelegationSettings: lifecycle.createOrUpdate; request=True` | `Microsoft.ApiManagement.PortalDelegationSettings` |
| [Microsoft.ApiManagement.DelegationSettings.get](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PortalDelegationSettings.tsp#L36)            | `(no single request)`                              | `Microsoft.ApiManagement.PortalDelegationSettings: lifecycle.read; request=False`          | `(none)`                                           |
| [Microsoft.ApiManagement.DelegationSettings.update](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PortalDelegationSettings.tsp#L85)         | `Microsoft.ApiManagement.PortalDelegationSettings` | `Microsoft.ApiManagement.PortalDelegationSettings: lifecycle.update; request=False`        | `(none)`                                           |

**Explanation:** The original picks the first existing 200/201/202 response and reads schema.$ref. It can obtain undefined for an empty response, an inline schema, or an operation without those statuses. The resource traversal does not compare this value across methods.

**Decision:** Recommend not porting misleading schema comparisons; this is not approved retirement or whole-API compliance. [No-content / collection-role comparisons: evidence and tradeoff](../gap-analysis.md#swagger-comparison-artifacts).

**Raw observation IDs:** `PutGetPatchResponseSchema:0`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-e0504c2667af2c28"></a>

### PutGetPatchResponseSchema: SignInSettings_CreateOrUpdate

**Identity:** `e0504c2667af2c28`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signin`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** Cross-operation comparison includes an absent selected response reference.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation            | Request schema                       | Success response schemas                  |
| ------------------------------------- | ------------------------------------ | ----------------------------------------- |
| `put` `SignInSettings_CreateOrUpdate` | `#/definitions/PortalSigninSettings` | `200: #/definitions/PortalSigninSettings` |
| `get` `SignInSettings_Get`            | `(no schema)`                        | `200: #/definitions/PortalSigninSettings` |
| `patch` `SignInSettings_Update`       | `#/definitions/PortalSigninSettings` | `(no selected status)`                    |

| TypeSpec operation                                                                                                                                                                                                                                                   | Effective request                              | Canonical association / request checked                                                | Registered return candidates                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------- |
| [Microsoft.ApiManagement.SignInSettings.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PortalSigninSettings.tsp#L67) | `Microsoft.ApiManagement.PortalSigninSettings` | `Microsoft.ApiManagement.PortalSigninSettings: lifecycle.createOrUpdate; request=True` | `Microsoft.ApiManagement.PortalSigninSettings` |
| [Microsoft.ApiManagement.SignInSettings.get](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PortalSigninSettings.tsp#L36)            | `(no single request)`                          | `Microsoft.ApiManagement.PortalSigninSettings: lifecycle.read; request=False`          | `(none)`                                       |
| [Microsoft.ApiManagement.SignInSettings.update](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PortalSigninSettings.tsp#L85)         | `Microsoft.ApiManagement.PortalSigninSettings` | `Microsoft.ApiManagement.PortalSigninSettings: lifecycle.update; request=False`        | `(none)`                                       |

**Explanation:** The original picks the first existing 200/201/202 response and reads schema.$ref. It can obtain undefined for an empty response, an inline schema, or an operation without those statuses. The resource traversal does not compare this value across methods.

**Decision:** Recommend not porting misleading schema comparisons; this is not approved retirement or whole-API compliance. [No-content / collection-role comparisons: evidence and tradeoff](../gap-analysis.md#swagger-comparison-artifacts).

**Raw observation IDs:** `PutGetPatchResponseSchema:1`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-86196a233810a562"></a>

### PutGetPatchResponseSchema: SignUpSettings_CreateOrUpdate

**Identity:** `86196a233810a562`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signup`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** Cross-operation comparison includes an absent selected response reference.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation            | Request schema                       | Success response schemas                  |
| ------------------------------------- | ------------------------------------ | ----------------------------------------- |
| `put` `SignUpSettings_CreateOrUpdate` | `#/definitions/PortalSignupSettings` | `200: #/definitions/PortalSignupSettings` |
| `get` `SignUpSettings_Get`            | `(no schema)`                        | `200: #/definitions/PortalSignupSettings` |
| `patch` `SignUpSettings_Update`       | `#/definitions/PortalSignupSettings` | `(no selected status)`                    |

| TypeSpec operation                                                                                                                                                                                                                                                   | Effective request                              | Canonical association / request checked                                                | Registered return candidates                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------- |
| [Microsoft.ApiManagement.SignUpSettings.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PortalSignupSettings.tsp#L67) | `Microsoft.ApiManagement.PortalSignupSettings` | `Microsoft.ApiManagement.PortalSignupSettings: lifecycle.createOrUpdate; request=True` | `Microsoft.ApiManagement.PortalSignupSettings` |
| [Microsoft.ApiManagement.SignUpSettings.get](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PortalSignupSettings.tsp#L36)            | `(no single request)`                          | `Microsoft.ApiManagement.PortalSignupSettings: lifecycle.read; request=False`          | `(none)`                                       |
| [Microsoft.ApiManagement.SignUpSettings.update](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PortalSignupSettings.tsp#L85)         | `Microsoft.ApiManagement.PortalSignupSettings` | `Microsoft.ApiManagement.PortalSignupSettings: lifecycle.update; request=False`        | `(none)`                                       |

**Explanation:** The original picks the first existing 200/201/202 response and reads schema.$ref. It can obtain undefined for an empty response, an inline schema, or an operation without those statuses. The resource traversal does not compare this value across methods.

**Decision:** Recommend not porting misleading schema comparisons; this is not approved retirement or whole-API compliance. [No-content / collection-role comparisons: evidence and tradeoff](../gap-analysis.md#swagger-comparison-artifacts).

**Raw observation IDs:** `PutGetPatchResponseSchema:2`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-9eca5628f4dd299e"></a>

### PutRequestResponseSchemeArm: PrivateEndpointConnection_CreateOrUpdate

**Identity:** `9eca5628f4dd299e`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/privateEndpointConnections/{privateEndpointConnectionName}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** Warning on the same operation compares a different contract.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 1 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation                       | Request schema                                   | Success response schemas                                                                                                                         |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `put` `PrivateEndpointConnection_CreateOrUpdate` | `#/definitions/PrivateEndpointConnectionRequest` | `200: ../../../../../../../../../common-types/resource-management/v5/privatelinks.json#/definitions/PrivateEndpointConnection; 202: (no schema)` |

| TypeSpec operation                                                                                                                                                                                                                                                                    | Effective request                                          | Canonical association / request checked                                                        | Registered return candidates |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------- |
| [Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PrivateEndpointConnection.tsp#L29) | `Microsoft.ApiManagement.PrivateEndpointConnectionRequest` | `Microsoft.ApiManagement.ApiManagementServiceResource: lifecycle.createOrUpdate; request=True` | `(none)`                     |

Observed TypeSpec `requestMismatch`: `PUT request body must use resource model Microsoft.ApiManagement.ApiManagementServiceResource. Found Microsoft.ApiManagement.PrivateEndpointConnectionRequest.`

**Explanation:** The TypeSpec request warning is real, but its canonical resource or selected response status/body differs from the original comparison. It is not credited merely because the HTTP operation is identical.

**Decision:** Review registration, DTOs and parent/child modeling; do not broaden blindly to every PUT. [Legacy request/response contracts: evidence and tradeoff](../gap-analysis.md#legacy-contracts).

**Raw observation IDs:** `PutRequestResponseSchemeArm:7`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

## Matching request checks

- [`d6c6d92c9a0f4dc9`](../instance-correspondence.md#s-d6c6d92c9a0f4dc9): `Api_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.
- [`a0043bfa2f35690b`](../instance-correspondence.md#s-a0043bfa2f35690b): `ApiTagDescription_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.
- [`07a4fba5ab458883`](../instance-correspondence.md#s-07a4fba5ab458883): `Certificate_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.
- [`a24e9f05205ca77e`](../instance-correspondence.md#s-a24e9f05205ca77e): `Group_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.
- [`16bb019f51c54666`](../instance-correspondence.md#s-16bb019f51c54666): `IdentityProvider_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.
- [`4074356758b8b55a`](../instance-correspondence.md#s-4074356758b8b55a): `NamedValue_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.
- [`9bd66fb3b423b668`](../instance-correspondence.md#s-9bd66fb3b423b668): `Subscription_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.
- [`c24f5593e4c0444c`](../instance-correspondence.md#s-c24f5593e4c0444c): `Tag_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.
- [`5bc868e33cb12f58`](../instance-correspondence.md#s-5bc868e33cb12f58): `EmailTemplate_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.
- [`6d6f81e97257180a`](../instance-correspondence.md#s-6d6f81e97257180a): `TenantAccess_Create`; one Swagger finding and one matching TypeSpec warning.
- [`abb6d8ec653be75b`](../instance-correspondence.md#s-abb6d8ec653be75b): `User_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.
- [`f480a1873a8a46d6`](../instance-correspondence.md#s-f480a1873a8a46d6): `WorkspaceApi_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.
- [`4fe374080228c379`](../instance-correspondence.md#s-4fe374080228c379): `WorkspaceCertificate_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.
- [`aab9a5c4285f75fb`](../instance-correspondence.md#s-aab9a5c4285f75fb): `WorkspaceGroup_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.
- [`e76bb208f825a268`](../instance-correspondence.md#s-e76bb208f825a268): `WorkspaceNamedValue_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.
- [`ddf45b716631a01b`](../instance-correspondence.md#s-ddf45b716631a01b): `WorkspaceSubscription_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.
- [`ea5b75fffe317a54`](../instance-correspondence.md#s-ea5b75fffe317a54): `WorkspaceTag_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.

## Additional or different TypeSpec checks

- [Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PrivateEndpointConnection.tsp#L29): **same-operation-different-comparison**; `PUT request body must use resource model Microsoft.ApiManagement.ApiManagementServiceResource. Found Microsoft.ApiManagement.PrivateEndpointConnectionRequest.`; route `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/privateEndpointConnections/{privateEndpointConnectionName}`.
- [Microsoft.ApiManagement.Tag.assignToApi](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagContract.tsp#L223): **additional-missing-request-policy**; `ARM PUT operations must have a request body.`; route `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/tags/{tagId}`.
- [Microsoft.ApiManagement.TagContracts.assignToOperation](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagContract.tsp#L110): **additional-missing-request-policy**; `ARM PUT operations must have a request body.`; route `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/tags/{tagId}`.
- [Microsoft.ApiManagement.TagContractOperation.assignToProduct](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagContract.tsp#L350): **additional-missing-request-policy**; `ARM PUT operations must have a request body.`; route `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/tags/{tagId}`.
- [Microsoft.ApiManagement.GroupContracts.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/GroupContract.tsp#L334): **additional-missing-request-policy**; `ARM PUT operations must have a request body.`; route `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/groups/{groupId}/users/{userId}`.
- [Microsoft.ApiManagement.NotificationContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NotificationContract.tsp#L233): **additional-missing-request-policy**; `ARM PUT operations must have a request body.`; route `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/notifications/{notificationName}`.
- [Microsoft.ApiManagement.WorkspaceNotification.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NotificationContract.tsp#L424): **additional-missing-request-policy**; `ARM PUT operations must have a request body.`; route `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}`.
- [Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientUserCreateOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NotificationContract.tsp#L485): **additional-missing-request-policy**; `ARM PUT operations must have a request body.`; route `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}/recipientUsers/{userId}`.
- [Microsoft.ApiManagement.WorkspaceNotification.workspaceNotificationRecipientEmailCreateOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NotificationContract.tsp#L538): **additional-missing-request-policy**; `ARM PUT operations must have a request body.`; route `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/notifications/{notificationName}/recipientEmails/{email}`.
