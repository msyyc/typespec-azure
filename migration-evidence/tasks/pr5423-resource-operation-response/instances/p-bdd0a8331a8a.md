# specification/subscription/resource-manager/Microsoft.Subscription/Subscription

[All project differences](../instance-correspondence.md#differing-projects).

<a id="s-e61cca263ccff3b7"></a>

## PutRequestResponseSchemeArm: e61cca263ccff3b7

**Route/document:** `/providers/Microsoft.Subscription/aliases/{aliasName}`; `projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/providers/Microsoft.Subscription/aliases/{aliasName}",
      "operationId": "Alias_Create",
      "request": {
        "raw": {
          "$ref": "#/definitions/PutAliasRequest"
        },
        "reference": {
          "document": "projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json",
          "pointer": ["definitions", "PutAliasRequest"]
        },
        "topLevelResolvedSchemaSha256": "b8d2a9b53529adc42ee84581decdc7a8c14cfb6224789df5c5ee2c47120f956c",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/SubscriptionAliasResponse"
          },
          "reference": {
            "document": "projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json",
            "pointer": ["definitions", "SubscriptionAliasResponse"]
          },
          "topLevelResolvedSchemaSha256": "58aa7a017733718d3de4281da89c7670b80d58bd05fdd3b4ce2bd01d3923da22",
          "xmsResourceInHierarchy": true
        },
        "201": {
          "raw": {
            "$ref": "#/definitions/SubscriptionAliasResponse"
          },
          "reference": {
            "document": "projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json",
            "pointer": ["definitions", "SubscriptionAliasResponse"]
          },
          "topLevelResolvedSchemaSha256": "58aa7a017733718d3de4281da89c7670b80d58bd05fdd3b4ce2bd01d3923da22",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.Subscription.SubscriptionAliasResponses.create",
      "sourceFile": "SubscriptionAliasResponse.tsp",
      "line": 40,
      "verb": "put",
      "path": "/providers/Microsoft.Subscription/aliases/{aliasName}",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.Subscription.PutAliasRequest",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.Subscription.PutAliasRequest",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.Subscription.PutAliasRequest",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.Subscription.PutAliasRequest",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.Subscription.SubscriptionAliasResponse",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.Subscription.SubscriptionAliasResponses.create\",{\"sourceFile\":\"SubscriptionAliasResponse.tsp\",\"line\":40,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.Subscription.SubscriptionAliasResponse>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.Subscription.SubscriptionAliasResponse>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.Subscription.SubscriptionAliasResponse",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.Subscription.SubscriptionAliasResponse",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.ProxyResource",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.Resource",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.Subscription.SubscriptionAliasResponse"
            }
          ]
        },
        {
          "statusCodes": 201,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceCreatedResponse<Microsoft.Subscription.SubscriptionAliasResponse, { location: string, retryAfter: int32 }>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceCreatedResponse<Microsoft.Subscription.SubscriptionAliasResponse, { location: string, retryAfter: int32 }>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.Subscription.SubscriptionAliasResponse",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.Subscription.SubscriptionAliasResponse",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.ProxyResource",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.Resource",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.Subscription.SubscriptionAliasResponse"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
              "kind": "Model",
              "registeredResource": false,
              "void": false,
              "lineage": [
                {
                  "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Azure.ResourceManager.CommonTypes.ErrorResponse"
            }
          ]
        }
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.Subscription.SubscriptionAliasResponses.create\",{\"sourceFile\":\"SubscriptionAliasResponse.tsp\",\"line\":40,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/subscription/resource-manager/Microsoft.Subscription/Subscription:0"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:203"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-9fb05cc3244469f8"></a>

## PutRequestResponseSchemeArm: 9fb05cc3244469f8

**Route/document:** `/providers/Microsoft.Subscription/policies/default`; `projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/providers/Microsoft.Subscription/policies/default",
      "operationId": "SubscriptionPolicy_AddUpdatePolicyForTenant",
      "request": {
        "raw": {
          "$ref": "#/definitions/PutTenantPolicyRequestProperties"
        },
        "reference": {
          "document": "projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json",
          "pointer": ["definitions", "PutTenantPolicyRequestProperties"]
        },
        "topLevelResolvedSchemaSha256": "bc569a7acb6a802f2ffd48aee2a22ed383f85acef9696d5e2ecc4fc79e57c5d5",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/GetTenantPolicyResponse"
          },
          "reference": {
            "document": "projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json",
            "pointer": ["definitions", "GetTenantPolicyResponse"]
          },
          "topLevelResolvedSchemaSha256": "3cc3cc20c22e159a32067ba15f4c31be13aaa9e6f08d9fceb92e59ddf7ba56e2",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.Subscription.GetTenantPolicyResponses.addUpdatePolicyForTenant",
      "sourceFile": "GetTenantPolicyResponse.tsp",
      "line": 43,
      "verb": "put",
      "path": "/providers/Microsoft.Subscription/policies/default",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.Subscription.PutTenantPolicyRequestProperties",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.Subscription.PutTenantPolicyRequestProperties",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.Subscription.PutTenantPolicyRequestProperties",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.Subscription.PutTenantPolicyRequestProperties",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.Subscription.GetTenantPolicyResponse",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.Subscription.GetTenantPolicyResponses.addUpdatePolicyForTenant\",{\"sourceFile\":\"GetTenantPolicyResponse.tsp\",\"line\":43,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.Subscription.GetTenantPolicyResponse>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.Subscription.GetTenantPolicyResponse>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.Subscription.GetTenantPolicyResponse",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.Subscription.GetTenantPolicyResponse",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.ProxyResource",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.Resource",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.Subscription.GetTenantPolicyResponse"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
              "kind": "Model",
              "registeredResource": false,
              "void": false,
              "lineage": [
                {
                  "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Azure.ResourceManager.CommonTypes.ErrorResponse"
            }
          ]
        }
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.Subscription.GetTenantPolicyResponses.addUpdatePolicyForTenant\",{\"sourceFile\":\"GetTenantPolicyResponse.tsp\",\"line\":43,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/subscription/resource-manager/Microsoft.Subscription/Subscription:2"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:204"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.

<a id="s-09326584113e2a3a"></a>

## PutRequestResponseSchemeArm: 09326584113e2a3a

**Route/document:** `/subscriptions/{subscriptionId}/providers/Microsoft.Subscription/changeTenantRequest/default`; `projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json`.

**Observed:** 1 Swagger raw / 1 member check; 1 corresponding configured TypeSpec warnings; 1 same-operation findings (not automatically credited); 0 captured owning callbacks before suppression.

**Coverage status:** corresponding-mapped-warning. **Classification:** mapped-request-mismatch.

```json
{
  "swaggerOperations": [
    {
      "verb": "put",
      "route": "/subscriptions/{subscriptionId}/providers/Microsoft.Subscription/changeTenantRequest/default",
      "operationId": "Subscriptions_PutTargetDirectory",
      "request": {
        "raw": {
          "$ref": "#/definitions/TargetDirectoryRequest"
        },
        "reference": {
          "document": "projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json",
          "pointer": ["definitions", "TargetDirectoryRequest"]
        },
        "topLevelResolvedSchemaSha256": "9d0f43fead06e883fb35f55f1956a1a610c7c8db1710b8b8e1b08a507825373a",
        "xmsResourceInHierarchy": false
      },
      "responses": {
        "200": {
          "raw": {
            "$ref": "#/definitions/TargetDirectoryResult"
          },
          "reference": {
            "document": "projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json",
            "pointer": ["definitions", "TargetDirectoryResult"]
          },
          "topLevelResolvedSchemaSha256": "95b1cefcc7c0f97d77c833d6f1af81401d718cd686cf9fcefbe8ea9cbb90869a",
          "xmsResourceInHierarchy": true
        }
      }
    }
  ],
  "typeSpecSourceBindings": [
    {
      "operation": "Microsoft.Subscription.TargetDirectoryResults.putTargetDirectory",
      "sourceFile": "TargetDirectoryResult.tsp",
      "line": 51,
      "verb": "put",
      "path": "/subscriptions/{subscriptionId}/providers/Microsoft.Subscription/changeTenantRequest/default",
      "request": {
        "bodyKind": "single",
        "type": {
          "name": "Microsoft.Subscription.TargetDirectoryRequest",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.Subscription.TargetDirectoryRequest",
              "discriminated": false
            }
          ]
        },
        "effectiveType": {
          "name": "Microsoft.Subscription.TargetDirectoryRequest",
          "kind": "Model",
          "registeredResource": false,
          "void": false,
          "lineage": [
            {
              "name": "Microsoft.Subscription.TargetDirectoryRequest",
              "discriminated": false
            }
          ]
        },
        "void": false
      },
      "associations": [
        {
          "resource": "Microsoft.Subscription.TargetDirectoryResult",
          "group": "lifecycle",
          "kind": "createOrUpdate",
          "operationKey": "[\"Microsoft.Subscription.TargetDirectoryResults.putTargetDirectory\",{\"sourceFile\":\"TargetDirectoryResult.tsp\",\"line\":51,\"column\":3}]",
          "internal": false,
          "checkedResponseKind": "createOrUpdate",
          "checkedPutRequest": true
        }
      ],
      "responses": [
        {
          "statusCodes": 200,
          "type": {
            "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.Subscription.TargetDirectoryResult>",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.ArmResourceUpdatedResponse<Microsoft.Subscription.TargetDirectoryResult>",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Microsoft.Subscription.TargetDirectoryResult",
              "kind": "Model",
              "registeredResource": true,
              "void": false,
              "lineage": [
                {
                  "name": "Microsoft.Subscription.TargetDirectoryResult",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.ProxyResource",
                  "discriminated": false
                },
                {
                  "name": "Azure.ResourceManager.CommonTypes.Resource",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Microsoft.Subscription.TargetDirectoryResult"
            }
          ]
        },
        {
          "statusCodes": "*",
          "type": {
            "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
            "kind": "Model",
            "registeredResource": false,
            "void": false,
            "lineage": [
              {
                "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
                "discriminated": false
              }
            ]
          },
          "bodies": [
            {
              "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
              "kind": "Model",
              "registeredResource": false,
              "void": false,
              "lineage": [
                {
                  "name": "Azure.ResourceManager.CommonTypes.ErrorResponse",
                  "discriminated": false
                }
              ],
              "effectiveModel": "Azure.ResourceManager.CommonTypes.ErrorResponse"
            }
          ]
        }
      ]
    }
  ],
  "selectedVersionOperationIdentities": [
    "[\"Microsoft.Subscription.TargetDirectoryResults.putTargetDirectory\",{\"sourceFile\":\"TargetDirectoryResult.tsp\",\"line\":51,\"column\":3}]"
  ],
  "mappedNativeFindingIds": [
    "specification/subscription/resource-manager/Microsoft.Subscription/Subscription:1"
  ],
  "ownerReports": [],
  "rawObservationIds": ["PutRequestResponseSchemeArm:205"]
}
```

**Gap analysis and decision:** No rule change for this observed pairing; retain compliant and violating controls.
