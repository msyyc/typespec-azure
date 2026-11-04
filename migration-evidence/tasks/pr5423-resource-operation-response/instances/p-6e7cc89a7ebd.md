# specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement

[All project differences](../instance-correspondence.md#differing-projects).

**Project totals:** Swagger 22 raw / 22 member checks; TypeSpec 4 raw; 3 findings credited to the same comparison. Common project/route unit: 22 Swagger / 4 TypeSpec. Counts repeated across different members at the same operation are non-additive. TypeSpec counts refer only to arm-resource-operation-response, not the entire linter suite.

<a id="s-d6c6d92c9a0f4dc9"></a>

### PutRequestResponseSchemeArm: Api_CreateOrUpdate

**Identity:** `d6c6d92c9a0f4dc9`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** Registered response, but PUT absent from retained operation map.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation | Request schema                             | Success response schemas                                         |
| -------------------------- | ------------------------------------------ | ---------------------------------------------------------------- |
| `put` `Api_CreateOrUpdate` | `#/definitions/ApiCreateOrUpdateParameter` | `200: #/definitions/ApiContract; 201: #/definitions/ApiContract` |

| TypeSpec operation                                                                                                                                                                                                                                        | Effective request                                    | Canonical association / request checked | Registered return candidates |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | --------------------------------------- | ---------------------------- |
| [Microsoft.ApiManagement.ApiContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/ApiContract.tsp#L93) | `Microsoft.ApiManagement.ApiCreateOrUpdateParameter` | `(none)`                                | `(none)`                     |

**Explanation:** The response body is registered, but this operation has no retained resource association. The listener therefore never reaches its request. ApiManagement demonstrates same-name registration overwrite; absence from the map is proven for every target, not an assertion that every absence has the same decorator cause.

**Decision:** Small rule change: enumerate existing registered createOrUpdate PUTs; validate before claiming new warnings. [Registered PUT traversal: evidence and tradeoff](../gap-analysis.md#registered-put-traversal).

**Raw observation IDs:** `PutRequestResponseSchemeArm:0`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-a0043bfa2f35690b"></a>

### PutRequestResponseSchemeArm: ApiTagDescription_CreateOrUpdate

**Identity:** `a0043bfa2f35690b`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/tagDescriptions/{tagDescriptionId}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** PUT stored under lists rather than lifecycle.createOrUpdate.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation               | Request schema                                 | Success response schemas                                                               |
| ---------------------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------- |
| `put` `ApiTagDescription_CreateOrUpdate` | `#/definitions/TagDescriptionCreateParameters` | `200: #/definitions/TagDescriptionContract; 201: #/definitions/TagDescriptionContract` |

| TypeSpec operation                                                                                                                                                                                                                                                               | Effective request                                        | Canonical association / request checked                                               | Registered return candidates |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------- | ---------------------------- |
| [Microsoft.ApiManagement.TagDescriptionContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagDescriptionContract.tsp#L102) | `Microsoft.ApiManagement.TagDescriptionCreateParameters` | `Microsoft.ApiManagement.TagDescriptionContract: lists.createOrUpdate; request=False` | `(none)`                     |

**Explanation:** The operation is associated through lists. Existing response traversal visits it, but the new request branch does not.

**Decision:** Small rule change: enumerate existing registered createOrUpdate PUTs; validate before claiming new warnings. [Registered PUT traversal: evidence and tradeoff](../gap-analysis.md#registered-put-traversal).

**Raw observation IDs:** `PutRequestResponseSchemeArm:1`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-07a4fba5ab458883"></a>

### PutRequestResponseSchemeArm: Certificate_CreateOrUpdate

**Identity:** `07a4fba5ab458883`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/certificates/{certificateId}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** Registered response, but PUT absent from retained operation map.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation         | Request schema                                      | Success response schemas                                                         |
| ---------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------- |
| `put` `Certificate_CreateOrUpdate` | `#/definitions/CertificateCreateOrUpdateParameters` | `200: #/definitions/CertificateContract; 201: #/definitions/CertificateContract` |

| TypeSpec operation                                                                                                                                                                                                                                                        | Effective request                                             | Canonical association / request checked | Registered return candidates |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------- | ---------------------------- |
| [Microsoft.ApiManagement.CertificateContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/CertificateContract.tsp#L97) | `Microsoft.ApiManagement.CertificateCreateOrUpdateParameters` | `(none)`                                | `(none)`                     |

**Explanation:** The response body is registered, but this operation has no retained resource association. The listener therefore never reaches its request. ApiManagement demonstrates same-name registration overwrite; absence from the map is proven for every target, not an assertion that every absence has the same decorator cause.

**Decision:** Small rule change: enumerate existing registered createOrUpdate PUTs; validate before claiming new warnings. [Registered PUT traversal: evidence and tradeoff](../gap-analysis.md#registered-put-traversal).

**Raw observation IDs:** `PutRequestResponseSchemeArm:2`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-4f6894b5bb1a95e3"></a>

### PutRequestResponseSchemeArm: GatewayApi_CreateOrUpdate

**Identity:** `4f6894b5bb1a95e3`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/gateways/{gatewayId}/apis/{apiId}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** PUT stored under lists rather than lifecycle.createOrUpdate.

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

**Explanation:** The operation is associated through lists. Existing response traversal visits it, but the new request branch does not.

**Decision:** Review registration, DTOs and parent/child modeling; do not broaden blindly to every PUT. [Legacy request/response contracts: evidence and tradeoff](../gap-analysis.md#legacy-contracts).

**Raw observation IDs:** `PutRequestResponseSchemeArm:3`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-a24e9f05205ca77e"></a>

### PutRequestResponseSchemeArm: Group_CreateOrUpdate

**Identity:** `a24e9f05205ca77e`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/groups/{groupId}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** Registered response, but PUT absent from retained operation map.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation   | Request schema                        | Success response schemas                                             |
| ---------------------------- | ------------------------------------- | -------------------------------------------------------------------- |
| `put` `Group_CreateOrUpdate` | `#/definitions/GroupCreateParameters` | `200: #/definitions/GroupContract; 201: #/definitions/GroupContract` |

| TypeSpec operation                                                                                                                                                                                                                                             | Effective request                               | Canonical association / request checked | Registered return candidates |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | --------------------------------------- | ---------------------------- |
| [Microsoft.ApiManagement.GroupContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/GroupContract.tsp#L188) | `Microsoft.ApiManagement.GroupCreateParameters` | `(none)`                                | `(none)`                     |

**Explanation:** The response body is registered, but this operation has no retained resource association. The listener therefore never reaches its request. ApiManagement demonstrates same-name registration overwrite; absence from the map is proven for every target, not an assertion that every absence has the same decorator cause.

**Decision:** Small rule change: enumerate existing registered createOrUpdate PUTs; validate before claiming new warnings. [Registered PUT traversal: evidence and tradeoff](../gap-analysis.md#registered-put-traversal).

**Raw observation IDs:** `PutRequestResponseSchemeArm:4`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-4074356758b8b55a"></a>

### PutRequestResponseSchemeArm: NamedValue_CreateOrUpdate

**Identity:** `4074356758b8b55a`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/namedValues/{namedValueId}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** Registered response, but PUT absent from retained operation map.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation        | Request schema                           | Success response schemas                                                       |
| --------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------ |
| `put` `NamedValue_CreateOrUpdate` | `#/definitions/NamedValueCreateContract` | `200: #/definitions/NamedValueContract; 201: #/definitions/NamedValueContract` |

| TypeSpec operation                                                                                                                                                                                                                                                      | Effective request                                  | Canonical association / request checked | Registered return candidates |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | --------------------------------------- | ---------------------------- |
| [Microsoft.ApiManagement.NamedValueContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NamedValueContract.tsp#L91) | `Microsoft.ApiManagement.NamedValueCreateContract` | `(none)`                                | `(none)`                     |

**Explanation:** The response body is registered, but this operation has no retained resource association. The listener therefore never reaches its request. ApiManagement demonstrates same-name registration overwrite; absence from the map is proven for every target, not an assertion that every absence has the same decorator cause.

**Decision:** Small rule change: enumerate existing registered createOrUpdate PUTs; validate before claiming new warnings. [Registered PUT traversal: evidence and tradeoff](../gap-analysis.md#registered-put-traversal).

**Raw observation IDs:** `PutRequestResponseSchemeArm:6`.
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

<a id="s-9bd66fb3b423b668"></a>

### PutRequestResponseSchemeArm: Subscription_CreateOrUpdate

**Identity:** `9bd66fb3b423b668`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/subscriptions/{sid}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** Registered response, but PUT absent from retained operation map.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation          | Request schema                               | Success response schemas                                                           |
| ----------------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------- |
| `put` `Subscription_CreateOrUpdate` | `#/definitions/SubscriptionCreateParameters` | `200: #/definitions/SubscriptionContract; 201: #/definitions/SubscriptionContract` |

| TypeSpec operation                                                                                                                                                                                                                                                          | Effective request                                      | Canonical association / request checked | Registered return candidates |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | --------------------------------------- | ---------------------------- |
| [Microsoft.ApiManagement.SubscriptionContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/SubscriptionContract.tsp#L91) | `Microsoft.ApiManagement.SubscriptionCreateParameters` | `(none)`                                | `(none)`                     |

**Explanation:** The response body is registered, but this operation has no retained resource association. The listener therefore never reaches its request. ApiManagement demonstrates same-name registration overwrite; absence from the map is proven for every target, not an assertion that every absence has the same decorator cause.

**Decision:** Small rule change: enumerate existing registered createOrUpdate PUTs; validate before claiming new warnings. [Registered PUT traversal: evidence and tradeoff](../gap-analysis.md#registered-put-traversal).

**Raw observation IDs:** `PutRequestResponseSchemeArm:8`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-c24f5593e4c0444c"></a>

### PutRequestResponseSchemeArm: Tag_CreateOrUpdate

**Identity:** `c24f5593e4c0444c`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tags/{tagId}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** Registered response, but PUT absent from retained operation map.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation | Request schema                            | Success response schemas                                         |
| -------------------------- | ----------------------------------------- | ---------------------------------------------------------------- |
| `put` `Tag_CreateOrUpdate` | `#/definitions/TagCreateUpdateParameters` | `200: #/definitions/TagContract; 201: #/definitions/TagContract` |

| TypeSpec operation                                                                                                                                                                                                                                                      | Effective request                                   | Canonical association / request checked | Registered return candidates |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | --------------------------------------- | ---------------------------- |
| [Microsoft.ApiManagement.TagContractOperationGroup.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagContract.tsp#L453) | `Microsoft.ApiManagement.TagCreateUpdateParameters` | `(none)`                                | `(none)`                     |

**Explanation:** The response body is registered, but this operation has no retained resource association. The listener therefore never reaches its request. ApiManagement demonstrates same-name registration overwrite; absence from the map is proven for every target, not an assertion that every absence has the same decorator cause.

**Decision:** Small rule change: enumerate existing registered createOrUpdate PUTs; validate before claiming new warnings. [Registered PUT traversal: evidence and tradeoff](../gap-analysis.md#registered-put-traversal).

**Raw observation IDs:** `PutRequestResponseSchemeArm:9`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-5bc868e33cb12f58"></a>

### PutRequestResponseSchemeArm: EmailTemplate_CreateOrUpdate

**Identity:** `5bc868e33cb12f58`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/templates/{templateName}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** PUT stored under lists rather than lifecycle.createOrUpdate.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation           | Request schema                                | Success response schemas                                                             |
| ------------------------------------ | --------------------------------------------- | ------------------------------------------------------------------------------------ |
| `put` `EmailTemplate_CreateOrUpdate` | `#/definitions/EmailTemplateUpdateParameters` | `200: #/definitions/EmailTemplateContract; 201: #/definitions/EmailTemplateContract` |

| TypeSpec operation                                                                                                                                                                                                                                                            | Effective request                                       | Canonical association / request checked                                              | Registered return candidates                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------- |
| [Microsoft.ApiManagement.EmailTemplateContracts.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/EmailTemplateContract.tsp#L89) | `Microsoft.ApiManagement.EmailTemplateUpdateParameters` | `Microsoft.ApiManagement.EmailTemplateContract: lists.createOrUpdate; request=False` | `Microsoft.ApiManagement.EmailTemplateContract` |

**Explanation:** The operation is associated through lists. Existing response traversal visits it, but the new request branch does not.

**Decision:** Small rule change: enumerate existing registered createOrUpdate PUTs; validate before claiming new warnings. [Registered PUT traversal: evidence and tradeoff](../gap-analysis.md#registered-put-traversal).

**Raw observation IDs:** `PutRequestResponseSchemeArm:10`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-f480a1873a8a46d6"></a>

### PutRequestResponseSchemeArm: WorkspaceApi_CreateOrUpdate

**Identity:** `f480a1873a8a46d6`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/apis/{apiId}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** PUT stored under lists rather than lifecycle.createOrUpdate.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation          | Request schema                             | Success response schemas                                         |
| ----------------------------------- | ------------------------------------------ | ---------------------------------------------------------------- |
| `put` `WorkspaceApi_CreateOrUpdate` | `#/definitions/ApiCreateOrUpdateParameter` | `200: #/definitions/ApiContract; 201: #/definitions/ApiContract` |

| TypeSpec operation                                                                                                                                                                                                                                         | Effective request                                    | Canonical association / request checked                                    | Registered return candidates |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------- | ---------------------------- |
| [Microsoft.ApiManagement.WorkspaceApi.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/ApiContract.tsp#L395) | `Microsoft.ApiManagement.ApiCreateOrUpdateParameter` | `Microsoft.ApiManagement.ApiContract: lists.createOrUpdate; request=False` | `(none)`                     |

**Explanation:** The operation is associated through lists. Existing response traversal visits it, but the new request branch does not.

**Decision:** Small rule change: enumerate existing registered createOrUpdate PUTs; validate before claiming new warnings. [Registered PUT traversal: evidence and tradeoff](../gap-analysis.md#registered-put-traversal).

**Raw observation IDs:** `PutRequestResponseSchemeArm:13`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-4fe374080228c379"></a>

### PutRequestResponseSchemeArm: WorkspaceCertificate_CreateOrUpdate

**Identity:** `4fe374080228c379`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/certificates/{certificateId}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** PUT stored under lists rather than lifecycle.createOrUpdate.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation                  | Request schema                                      | Success response schemas                                                         |
| ------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------- |
| `put` `WorkspaceCertificate_CreateOrUpdate` | `#/definitions/CertificateCreateOrUpdateParameters` | `200: #/definitions/CertificateContract; 201: #/definitions/CertificateContract` |

| TypeSpec operation                                                                                                                                                                                                                                                         | Effective request                                             | Canonical association / request checked                                            | Registered return candidates |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------- |
| [Microsoft.ApiManagement.WorkspaceCertificate.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/CertificateContract.tsp#L273) | `Microsoft.ApiManagement.CertificateCreateOrUpdateParameters` | `Microsoft.ApiManagement.CertificateContract: lists.createOrUpdate; request=False` | `(none)`                     |

**Explanation:** The operation is associated through lists. Existing response traversal visits it, but the new request branch does not.

**Decision:** Small rule change: enumerate existing registered createOrUpdate PUTs; validate before claiming new warnings. [Registered PUT traversal: evidence and tradeoff](../gap-analysis.md#registered-put-traversal).

**Raw observation IDs:** `PutRequestResponseSchemeArm:14`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-aab9a5c4285f75fb"></a>

### PutRequestResponseSchemeArm: WorkspaceGroup_CreateOrUpdate

**Identity:** `aab9a5c4285f75fb`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/groups/{groupId}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** PUT stored under lists rather than lifecycle.createOrUpdate.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation            | Request schema                        | Success response schemas                                             |
| ------------------------------------- | ------------------------------------- | -------------------------------------------------------------------- |
| `put` `WorkspaceGroup_CreateOrUpdate` | `#/definitions/GroupCreateParameters` | `200: #/definitions/GroupContract; 201: #/definitions/GroupContract` |

| TypeSpec operation                                                                                                                                                                                                                                             | Effective request                               | Canonical association / request checked                                      | Registered return candidates |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------- |
| [Microsoft.ApiManagement.WorkspaceGroup.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/GroupContract.tsp#L438) | `Microsoft.ApiManagement.GroupCreateParameters` | `Microsoft.ApiManagement.GroupContract: lists.createOrUpdate; request=False` | `(none)`                     |

**Explanation:** The operation is associated through lists. Existing response traversal visits it, but the new request branch does not.

**Decision:** Small rule change: enumerate existing registered createOrUpdate PUTs; validate before claiming new warnings. [Registered PUT traversal: evidence and tradeoff](../gap-analysis.md#registered-put-traversal).

**Raw observation IDs:** `PutRequestResponseSchemeArm:15`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-e76bb208f825a268"></a>

### PutRequestResponseSchemeArm: WorkspaceNamedValue_CreateOrUpdate

**Identity:** `e76bb208f825a268`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/namedValues/{namedValueId}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** PUT stored under lists rather than lifecycle.createOrUpdate.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation                 | Request schema                           | Success response schemas                                                       |
| ------------------------------------------ | ---------------------------------------- | ------------------------------------------------------------------------------ |
| `put` `WorkspaceNamedValue_CreateOrUpdate` | `#/definitions/NamedValueCreateContract` | `200: #/definitions/NamedValueContract; 201: #/definitions/NamedValueContract` |

| TypeSpec operation                                                                                                                                                                                                                                                       | Effective request                                  | Canonical association / request checked                                           | Registered return candidates |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- | --------------------------------------------------------------------------------- | ---------------------------- |
| [Microsoft.ApiManagement.WorkspaceNamedValue.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/NamedValueContract.tsp#L306) | `Microsoft.ApiManagement.NamedValueCreateContract` | `Microsoft.ApiManagement.NamedValueContract: lists.createOrUpdate; request=False` | `(none)`                     |

**Explanation:** The operation is associated through lists. Existing response traversal visits it, but the new request branch does not.

**Decision:** Small rule change: enumerate existing registered createOrUpdate PUTs; validate before claiming new warnings. [Registered PUT traversal: evidence and tradeoff](../gap-analysis.md#registered-put-traversal).

**Raw observation IDs:** `PutRequestResponseSchemeArm:16`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-ddf45b716631a01b"></a>

### PutRequestResponseSchemeArm: WorkspaceSubscription_CreateOrUpdate

**Identity:** `ddf45b716631a01b`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/subscriptions/{sid}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** PUT stored under lists rather than lifecycle.createOrUpdate.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation                   | Request schema                               | Success response schemas                                                           |
| -------------------------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------- |
| `put` `WorkspaceSubscription_CreateOrUpdate` | `#/definitions/SubscriptionCreateParameters` | `200: #/definitions/SubscriptionContract; 201: #/definitions/SubscriptionContract` |

| TypeSpec operation                                                                                                                                                                                                                                                           | Effective request                                      | Canonical association / request checked                                             | Registered return candidates |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------- | ---------------------------- |
| [Microsoft.ApiManagement.WorkspaceSubscription.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/SubscriptionContract.tsp#L403) | `Microsoft.ApiManagement.SubscriptionCreateParameters` | `Microsoft.ApiManagement.SubscriptionContract: lists.createOrUpdate; request=False` | `(none)`                     |

**Explanation:** The operation is associated through lists. Existing response traversal visits it, but the new request branch does not.

**Decision:** Small rule change: enumerate existing registered createOrUpdate PUTs; validate before claiming new warnings. [Registered PUT traversal: evidence and tradeoff](../gap-analysis.md#registered-put-traversal).

**Raw observation IDs:** `PutRequestResponseSchemeArm:17`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

<a id="s-ea5b75fffe317a54"></a>

### PutRequestResponseSchemeArm: WorkspaceTag_CreateOrUpdate

**Identity:** `ea5b75fffe317a54`; `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/tags/{tagId}`.
**Swagger document:** `projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json`.
**Observed comparison:** PUT stored under lists rather than lifecycle.createOrUpdate.

| Engine          | Observed findings on this target                         |
| --------------- | -------------------------------------------------------- |
| Swagger linter  | 1 raw observations; one member check                     |
| TypeSpec linter | 0 same-operation findings; 0 credited to this comparison |

| Method / Swagger operation          | Request schema                            | Success response schemas                                         |
| ----------------------------------- | ----------------------------------------- | ---------------------------------------------------------------- |
| `put` `WorkspaceTag_CreateOrUpdate` | `#/definitions/TagCreateUpdateParameters` | `200: #/definitions/TagContract; 201: #/definitions/TagContract` |

| TypeSpec operation                                                                                                                                                                                                                                         | Effective request                                   | Canonical association / request checked                                    | Registered return candidates |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------- | ---------------------------- |
| [Microsoft.ApiManagement.WorkspaceTag.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/TagContract.tsp#L628) | `Microsoft.ApiManagement.TagCreateUpdateParameters` | `Microsoft.ApiManagement.TagContract: lists.createOrUpdate; request=False` | `(none)`                     |

**Explanation:** The operation is associated through lists. Existing response traversal visits it, but the new request branch does not.

**Decision:** Small rule change: enumerate existing registered createOrUpdate PUTs; validate before claiming new warnings. [Registered PUT traversal: evidence and tradeoff](../gap-analysis.md#registered-put-traversal).

**Raw observation IDs:** `PutRequestResponseSchemeArm:18`.
Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages are retained in [instance-mapping.json](../instance-mapping.json).

## Matching request checks

- [`16bb019f51c54666`](../instance-correspondence.md#s-16bb019f51c54666): `IdentityProvider_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.
- [`6d6f81e97257180a`](../instance-correspondence.md#s-6d6f81e97257180a): `TenantAccess_Create`; one Swagger finding and one matching TypeSpec warning.
- [`abb6d8ec653be75b`](../instance-correspondence.md#s-abb6d8ec653be75b): `User_CreateOrUpdate`; one Swagger finding and one matching TypeSpec warning.

## Additional or different TypeSpec checks

- [Microsoft.ApiManagement.PrivateEndpointConnections.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/PrivateEndpointConnection.tsp#L29): **same-operation-different-comparison**; `PUT request body must use resource model Microsoft.ApiManagement.ApiManagementServiceResource. Found Microsoft.ApiManagement.PrivateEndpointConnectionRequest.`; route `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/privateEndpointConnections/{privateEndpointConnectionName}`.
