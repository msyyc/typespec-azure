# Exact reported diagnostic inventory

Every selected Swagger and raw TypeSpec finding is retained below, without deduplicating
distinct violations at one location. These are individual reported findings, not equivalent defects.
Raw/aligned/default compilations remain separately available in [observations.json](observations.json).
The [instance assessment](instance-correspondence.md) resolves exact operations and comparisons;
original reported/input documents and fallback attribution are not rewritten.

## specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement

Swagger raw: 22; TypeSpec raw: 26; source-aligned: 26; default: 26.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Api_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2936,
        "column": 12
      },
      "end": {
        "line": 3102,
        "column": 43
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ApiTagDescription_CreateOrUpdate' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/tagDescriptions/{tagDescriptionId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/tagDescriptions/{tagDescriptionId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 9456,
        "column": 12
      },
      "end": {
        "line": 9558,
        "column": 74
      }
    }
  }
}
```

### Swagger 3: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Certificate_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/certificates/{certificateId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/certificates/{certificateId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14137,
        "column": 12
      },
      "end": {
        "line": 14231,
        "column": 80
      }
    }
  }
}
```

### Swagger 4: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'GatewayApi_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/gateways/{gatewayId}/apis/{apiId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/gateways/{gatewayId}/apis/{apiId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 17239,
        "column": 12
      },
      "end": {
        "line": 17315,
        "column": 67
      }
    }
  }
}
```

### Swagger 5: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Group_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/groups/{groupId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/groups/{groupId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 18835,
        "column": 12
      },
      "end": {
        "line": 18929,
        "column": 70
      }
    }
  }
}
```

### Swagger 6: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'IdentityProvider_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/identityProviders/{identityProviderName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/identityProviders/{identityProviderName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 19583,
        "column": 12
      },
      "end": {
        "line": 19711,
        "column": 73
      }
    }
  }
}
```

### Swagger 7: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'NamedValue_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/namedValues/{namedValueId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/namedValues/{namedValueId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 21014,
        "column": 12
      },
      "end": {
        "line": 21128,
        "column": 43
      }
    }
  }
}
```

### Swagger 8: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PrivateEndpointConnection_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/privateEndpointConnections/{privateEndpointConnectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/privateEndpointConnections/{privateEndpointConnectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 26250,
        "column": 12
      },
      "end": {
        "line": 26330,
        "column": 43
      }
    }
  }
}
```

### Swagger 9: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Subscription_CreateOrUpdate' Request Model: 'parameters[8].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/subscriptions/{sid}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/subscriptions/{sid}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 31416,
        "column": 12
      },
      "end": {
        "line": 31536,
        "column": 69
      }
    }
  }
}
```

### Swagger 10: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Tag_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tags/{tagId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tags/{tagId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 32174,
        "column": 12
      },
      "end": {
        "line": 32261,
        "column": 60
      }
    }
  }
}
```

### Swagger 11: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'EmailTemplate_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/templates/{templateName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/templates/{templateName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 33618,
        "column": 12
      },
      "end": {
        "line": 33768,
        "column": 65
      }
    }
  }
}
```

### Swagger 12: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'TenantAccess_Create' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tenant/{accessName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tenant/{accessName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 34342,
        "column": 12
      },
      "end": {
        "line": 34432,
        "column": 69
      }
    }
  }
}
```

### Swagger 13: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'User_CreateOrUpdate' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/users/{userId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/users/{userId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 35475,
        "column": 12
      },
      "end": {
        "line": 35573,
        "column": 61
      }
    }
  }
}
```

### Swagger 14: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'WorkspaceApi_CreateOrUpdate' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/apis/{apiId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/apis/{apiId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 37655,
        "column": 12
      },
      "end": {
        "line": 37777,
        "column": 43
      }
    }
  }
}
```

### Swagger 15: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'WorkspaceCertificate_CreateOrUpdate' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/certificates/{certificateId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/certificates/{certificateId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 42002,
        "column": 12
      },
      "end": {
        "line": 42106,
        "column": 89
      }
    }
  }
}
```

### Swagger 16: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'WorkspaceGroup_CreateOrUpdate' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/groups/{groupId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/groups/{groupId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 42997,
        "column": 12
      },
      "end": {
        "line": 43096,
        "column": 79
      }
    }
  }
}
```

### Swagger 17: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'WorkspaceNamedValue_CreateOrUpdate' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/namedValues/{namedValueId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/namedValues/{namedValueId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 44350,
        "column": 12
      },
      "end": {
        "line": 44479,
        "column": 43
      }
    }
  }
}
```

### Swagger 18: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'WorkspaceSubscription_CreateOrUpdate' Request Model: 'parameters[9].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/subscriptions/{sid}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/subscriptions/{sid}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 49491,
        "column": 12
      },
      "end": {
        "line": 49621,
        "column": 78
      }
    }
  }
}
```

### Swagger 19: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'WorkspaceTag_CreateOrUpdate' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/tags/{tagId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/workspaces/{workspaceId}/tags/{tagId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 50262,
        "column": 12
      },
      "end": {
        "line": 50359,
        "column": 69
      }
    }
  }
}
```

### Swagger 20: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/delegation has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/delegation"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/delegation"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 25401,
        "column": 155
      },
      "end": {
        "line": 25628,
        "column": 73
      }
    }
  }
}
```

### Swagger 21: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signin has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signin"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signin"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 25683,
        "column": 151
      },
      "end": {
        "line": 25910,
        "column": 69
      }
    }
  }
}
```

### Swagger 22: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement",
  "swaggerFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/apimanagement/resource-manager/Microsoft.ApiManagement/ApiManagement/swagger/preview/2025-09-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signup has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signup"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/portalsettings/signup"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 25915,
        "column": 151
      },
      "end": {
        "line": 26142,
        "column": 69
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.ApiContract. Found Microsoft.ApiManagement.ApiCreateOrUpdateParameter.",
  "sourceFile": "ApiContract.tsp",
  "line": 93,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.ApiContract. Found Microsoft.ApiManagement.ApiCreateOrUpdateParameter.",
  "sourceFile": "ApiContract.tsp",
  "line": 395,
  "column": 3
}
```

### TypeSpec 3

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.ApiManagementServiceResource. Found Microsoft.ApiManagement.PrivateEndpointConnectionRequest.",
  "sourceFile": "PrivateEndpointConnection.tsp",
  "line": 29,
  "column": 3
}
```

### TypeSpec 4

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "TagContract.tsp",
  "line": 223,
  "column": 3
}
```

### TypeSpec 5

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "TagContract.tsp",
  "line": 110,
  "column": 3
}
```

### TypeSpec 6

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "TagContract.tsp",
  "line": 350,
  "column": 3
}
```

### TypeSpec 7

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.TagContract. Found Microsoft.ApiManagement.TagCreateUpdateParameters.",
  "sourceFile": "TagContract.tsp",
  "line": 453,
  "column": 3
}
```

### TypeSpec 8

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.TagContract. Found Microsoft.ApiManagement.TagCreateUpdateParameters.",
  "sourceFile": "TagContract.tsp",
  "line": 628,
  "column": 3
}
```

### TypeSpec 9

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.TagDescriptionContract. Found Microsoft.ApiManagement.TagDescriptionCreateParameters.",
  "sourceFile": "TagDescriptionContract.tsp",
  "line": 102,
  "column": 3
}
```

### TypeSpec 10

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.CertificateContract. Found Microsoft.ApiManagement.CertificateCreateOrUpdateParameters.",
  "sourceFile": "CertificateContract.tsp",
  "line": 97,
  "column": 3
}
```

### TypeSpec 11

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.CertificateContract. Found Microsoft.ApiManagement.CertificateCreateOrUpdateParameters.",
  "sourceFile": "CertificateContract.tsp",
  "line": 273,
  "column": 3
}
```

### TypeSpec 12

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.EmailTemplateContract. Found Microsoft.ApiManagement.EmailTemplateUpdateParameters.",
  "sourceFile": "EmailTemplateContract.tsp",
  "line": 89,
  "column": 3
}
```

### TypeSpec 13

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.GroupContract. Found Microsoft.ApiManagement.GroupCreateParameters.",
  "sourceFile": "GroupContract.tsp",
  "line": 188,
  "column": 3
}
```

### TypeSpec 14

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "GroupContract.tsp",
  "line": 334,
  "column": 3
}
```

### TypeSpec 15

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.GroupContract. Found Microsoft.ApiManagement.GroupCreateParameters.",
  "sourceFile": "GroupContract.tsp",
  "line": 438,
  "column": 3
}
```

### TypeSpec 16

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.UserContract. Found Microsoft.ApiManagement.UserCreateParameters.",
  "sourceFile": "UserContract.tsp",
  "line": 61,
  "column": 3
}
```

### TypeSpec 17

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.IdentityProviderContract. Found Microsoft.ApiManagement.IdentityProviderCreateContract.",
  "sourceFile": "IdentityProviderContract.tsp",
  "line": 62,
  "column": 3
}
```

### TypeSpec 18

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.NamedValueContract. Found Microsoft.ApiManagement.NamedValueCreateContract.",
  "sourceFile": "NamedValueContract.tsp",
  "line": 91,
  "column": 3
}
```

### TypeSpec 19

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.NamedValueContract. Found Microsoft.ApiManagement.NamedValueCreateContract.",
  "sourceFile": "NamedValueContract.tsp",
  "line": 306,
  "column": 3
}
```

### TypeSpec 20

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "NotificationContract.tsp",
  "line": 233,
  "column": 3
}
```

### TypeSpec 21

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "NotificationContract.tsp",
  "line": 424,
  "column": 3
}
```

### TypeSpec 22

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "NotificationContract.tsp",
  "line": 485,
  "column": 3
}
```

### TypeSpec 23

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "NotificationContract.tsp",
  "line": 538,
  "column": 3
}
```

### TypeSpec 24

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.SubscriptionContract. Found Microsoft.ApiManagement.SubscriptionCreateParameters.",
  "sourceFile": "SubscriptionContract.tsp",
  "line": 91,
  "column": 3
}
```

### TypeSpec 25

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.SubscriptionContract. Found Microsoft.ApiManagement.SubscriptionCreateParameters.",
  "sourceFile": "SubscriptionContract.tsp",
  "line": 403,
  "column": 3
}
```

### TypeSpec 26

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ApiManagement.AccessInformationContract. Found Microsoft.ApiManagement.AccessInformationCreateParameters.",
  "sourceFile": "AccessInformationContract.tsp",
  "line": 91,
  "column": 3
}
```

## specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/AnalyticsItems

Swagger raw: 1; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/AnalyticsItems",
  "swaggerFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/AnalyticsItems/swagger/stable/2015-05-01/analyticsItems_API.json",
  "validatorInputFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/AnalyticsItems/swagger/stable/2015-05-01/analyticsItems_API.json",
  "sourceDocuments": [
    "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/AnalyticsItems/swagger/stable/2015-05-01/analyticsItems_API.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: AnalyticsItems_Put",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 268,
        "column": 12
      },
      "end": {
        "line": 342,
        "column": 54
      }
    }
  }
}
```

## specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs

Swagger raw: 7; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs",
  "swaggerFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json",
  "validatorInputFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json",
  "sourceDocuments": [
    "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Annotations_Create' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/Annotations",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/Annotations",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 188,
        "column": 12
      },
      "end": {
        "line": 237,
        "column": 55
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs",
  "swaggerFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json",
  "validatorInputFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json",
  "sourceDocuments": [
    "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ExportConfigurations_Update' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/exportconfiguration/{exportId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/exportconfiguration/{exportId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1025,
        "column": 12
      },
      "end": {
        "line": 1072,
        "column": 63
      }
    }
  }
}
```

### Swagger 3: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs",
  "swaggerFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json",
  "validatorInputFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json",
  "sourceDocuments": [
    "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: Annotations_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/Annotations",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/Annotations",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 188,
        "column": 12
      },
      "end": {
        "line": 237,
        "column": 55
      }
    }
  }
}
```

### Swagger 4: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs",
  "swaggerFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json",
  "validatorInputFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json",
  "sourceDocuments": [
    "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ProactiveDetectionConfigurations_Update",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/ProactiveDetectionConfigs/{ConfigurationId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/ProactiveDetectionConfigs/{ConfigurationId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 538,
        "column": 12
      },
      "end": {
        "line": 585,
        "column": 75
      }
    }
  }
}
```

### Swagger 5: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs",
  "swaggerFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json",
  "validatorInputFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json",
  "sourceDocuments": [
    "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ComponentCurrentBillingFeatures_Update",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/currentbillingfeatures",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/currentbillingfeatures",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 850,
        "column": 12
      },
      "end": {
        "line": 890,
        "column": 66
      }
    }
  }
}
```

### Swagger 6: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs",
  "swaggerFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json",
  "validatorInputFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json",
  "sourceDocuments": [
    "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExportConfigurations_Update",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/exportconfiguration/{exportId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/exportconfiguration/{exportId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1025,
        "column": 12
      },
      "end": {
        "line": 1072,
        "column": 63
      }
    }
  }
}
```

### Swagger 7: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs",
  "swaggerFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json",
  "validatorInputFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json",
  "sourceDocuments": [
    "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/ComponentAPIs/swagger/stable/2015-05-01/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/Annotations has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/Annotations"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/Annotations"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 129,
        "column": 140
      },
      "end": {
        "line": 237,
        "column": 55
      }
    }
  }
}
```

## specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/Favorites

Swagger raw: 1; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/Favorites",
  "swaggerFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/Favorites/swagger/stable/2015-05-01/favorites_API.json",
  "validatorInputFile": "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/Favorites/swagger/stable/2015-05-01/favorites_API.json",
  "sourceDocuments": [
    "projects/specification/applicationinsights/resource-manager/Microsoft.Insights/ApplicationInsights/Favorites/swagger/stable/2015-05-01/favorites_API.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: Favorites_Add",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 235,
        "column": 12
      },
      "end": {
        "line": 282,
        "column": 49
      }
    }
  }
}
```

## specification/attestation/resource-manager/Microsoft.Attestation/Attestation

Swagger raw: 1; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/attestation/resource-manager/Microsoft.Attestation/Attestation",
  "swaggerFile": "projects/specification/attestation/resource-manager/Microsoft.Attestation/Attestation/swagger/stable/2021-06-01/attestation.json",
  "validatorInputFile": "projects/specification/attestation/resource-manager/Microsoft.Attestation/Attestation/swagger/stable/2021-06-01/attestation.json",
  "sourceDocuments": [
    "projects/specification/attestation/resource-manager/Microsoft.Attestation/Attestation/swagger/stable/2021-06-01/attestation.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'AttestationProviders_Create' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Attestation/attestationProviders/{providerName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Attestation/attestationProviders/{providerName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 276,
        "column": 12
      },
      "end": {
        "line": 332,
        "column": 64
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Attestation.AttestationProvider. Found Microsoft.Attestation.AttestationServiceCreationParams.",
  "sourceFile": "AttestationProvider.tsp",
  "line": 61,
  "column": 3
}
```

## specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview

Swagger raw: 8; TypeSpec raw: 8; source-aligned: 8; default: 8.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview",
  "swaggerFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json",
  "validatorInputFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json",
  "sourceDocuments": [
    "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ScopeAccessReviewHistoryDefinition_Create' Request Model: 'parameters[3].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/{scope}/providers/Microsoft.Authorization/accessReviewHistoryDefinitions/{historyDefinitionId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/{scope}/providers/Microsoft.Authorization/accessReviewHistoryDefinitions/{historyDefinitionId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 238,
        "column": 12
      },
      "end": {
        "line": 289,
        "column": 70
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview",
  "swaggerFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json",
  "validatorInputFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json",
  "sourceDocuments": [
    "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ScopeAccessReviewScheduleDefinitions_CreateOrUpdateById' Request Model: 'parameters[3].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/{scope}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/{scope}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 544,
        "column": 12
      },
      "end": {
        "line": 595,
        "column": 71
      }
    }
  }
}
```

### Swagger 3: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview",
  "swaggerFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json",
  "validatorInputFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json",
  "sourceDocuments": [
    "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ScopeAccessReviewInstances_Create' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/{scope}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/instances/{id}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/{scope}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/instances/{id}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 758,
        "column": 12
      },
      "end": {
        "line": 816,
        "column": 61
      }
    }
  }
}
```

### Swagger 4: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview",
  "swaggerFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json",
  "validatorInputFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json",
  "sourceDocuments": [
    "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ScopeAccessReviewDefaultSettings_Put' Request Model: 'parameters[2].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/{scope}/providers/Microsoft.Authorization/accessReviewScheduleSettings/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/{scope}/providers/Microsoft.Authorization/accessReviewScheduleSettings/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1298,
        "column": 12
      },
      "end": {
        "line": 1342,
        "column": 68
      }
    }
  }
}
```

### Swagger 5: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview",
  "swaggerFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json",
  "validatorInputFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json",
  "sourceDocuments": [
    "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'AccessReviewHistoryDefinition_Create' Request Model: 'parameters[3].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewHistoryDefinitions/{historyDefinitionId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewHistoryDefinitions/{historyDefinitionId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1862,
        "column": 12
      },
      "end": {
        "line": 1902,
        "column": 53
      }
    }
  }
}
```

### Swagger 6: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview",
  "swaggerFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json",
  "validatorInputFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json",
  "sourceDocuments": [
    "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'AccessReviewScheduleDefinitions_CreateOrUpdateById' Request Model: 'parameters[3].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2108,
        "column": 12
      },
      "end": {
        "line": 2148,
        "column": 53
      }
    }
  }
}
```

### Swagger 7: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview",
  "swaggerFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json",
  "validatorInputFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json",
  "sourceDocuments": [
    "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'AccessReviewInstances_Create' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/instances/{id}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/instances/{id}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2282,
        "column": 12
      },
      "end": {
        "line": 2329,
        "column": 53
      }
    }
  }
}
```

### Swagger 8: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview",
  "swaggerFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json",
  "validatorInputFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json",
  "sourceDocuments": [
    "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/AccessReview/swagger/preview/2021-12-01-preview/authorization-AccessReviewCalls.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'AccessReviewDefaultSettings_Put' Request Model: 'parameters[2].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleSettings/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleSettings/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2671,
        "column": 12
      },
      "end": {
        "line": 2704,
        "column": 53
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.AttributeNamespaces.AccessReviewInstance. Found Microsoft.AttributeNamespaces.AccessReviewInstanceProperties.",
  "sourceFile": "AccessReviewInstance.tsp",
  "line": 72,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.AttributeNamespaces.AccessReviewInstance. Found Microsoft.AttributeNamespaces.AccessReviewInstanceProperties.",
  "sourceFile": "AccessReviewInstance.tsp",
  "line": 224,
  "column": 3
}
```

### TypeSpec 3

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.AttributeNamespaces.AccessReviewScheduleDefinition. Found Microsoft.AttributeNamespaces.AccessReviewScheduleDefinitionProperties.",
  "sourceFile": "AccessReviewScheduleDefinition.tsp",
  "line": 84,
  "column": 3
}
```

### TypeSpec 4

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.AttributeNamespaces.AccessReviewScheduleDefinition. Found Microsoft.AttributeNamespaces.AccessReviewScheduleDefinitionProperties.",
  "sourceFile": "AccessReviewScheduleDefinition.tsp",
  "line": 169,
  "column": 3
}
```

### TypeSpec 5

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.AttributeNamespaces.AccessReviewHistoryDefinition. Found Microsoft.AttributeNamespaces.AccessReviewHistoryDefinitionProperties.",
  "sourceFile": "AccessReviewHistoryDefinition.tsp",
  "line": 65,
  "column": 3
}
```

### TypeSpec 6

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.AttributeNamespaces.AccessReviewHistoryDefinition. Found Microsoft.AttributeNamespaces.AccessReviewHistoryDefinitionProperties.",
  "sourceFile": "AccessReviewHistoryDefinition.tsp",
  "line": 173,
  "column": 3
}
```

### TypeSpec 7

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.AttributeNamespaces.AccessReviewDefaultSettings. Found Microsoft.AttributeNamespaces.AccessReviewScheduleSettings.",
  "sourceFile": "AccessReviewDefaultSettings.tsp",
  "line": 62,
  "column": 3
}
```

### TypeSpec 8

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.AttributeNamespaces.AccessReviewDefaultSettings. Found Microsoft.AttributeNamespaces.AccessReviewScheduleSettings.",
  "sourceFile": "AccessReviewDefaultSettings.tsp",
  "line": 107,
  "column": 3
}
```

## specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment

Swagger raw: 2; TypeSpec raw: 2; source-aligned: 2; default: 2.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment",
  "swaggerFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment/swagger/stable/2022-04-01/authorization-RoleAssignmentsCalls.json",
  "validatorInputFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment/swagger/stable/2022-04-01/authorization-RoleAssignmentsCalls.json",
  "sourceDocuments": [
    "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment/swagger/stable/2022-04-01/authorization-RoleAssignmentsCalls.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'RoleAssignments_CreateById' Request Model: 'parameters[2].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/{roleAssignmentId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/{roleAssignmentId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 94,
        "column": 12
      },
      "end": {
        "line": 144,
        "column": 64
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment",
  "swaggerFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment/swagger/stable/2022-04-01/authorization-RoleAssignmentsCalls.json",
  "validatorInputFile": "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment/swagger/stable/2022-04-01/authorization-RoleAssignmentsCalls.json",
  "sourceDocuments": [
    "projects/specification/authorization/resource-manager/Microsoft.Authorization/Authorization/RoleAssignment/swagger/stable/2022-04-01/authorization-RoleAssignmentsCalls.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'RoleAssignments_Create' Request Model: 'parameters[3].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 318,
        "column": 12
      },
      "end": {
        "line": 382,
        "column": 75
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RoleAssignment.RoleAssignment. Found Microsoft.RoleAssignment.RoleAssignmentCreateParameters.",
  "sourceFile": "RoleAssignment.tsp",
  "line": 161,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RoleAssignment.RoleAssignment. Found Microsoft.RoleAssignment.RoleAssignmentCreateParameters.",
  "sourceFile": "RoleAssignment.tsp",
  "line": 309,
  "column": 3
}
```

## specification/automation/resource-manager/Microsoft.Automation/Automation

Swagger raw: 26; TypeSpec raw: 20; source-aligned: 20; default: 20.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'AutomationAccount_CreateOrUpdate' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 393,
        "column": 12
      },
      "end": {
        "line": 451,
        "column": 69
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Certificate_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/certificates/{certificateName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/certificates/{certificateName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 773,
        "column": 12
      },
      "end": {
        "line": 838,
        "column": 63
      }
    }
  }
}
```

### Swagger 3: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'DscConfiguration_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/configurations/{configurationName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/configurations/{configurationName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1100,
        "column": 12
      },
      "end": {
        "line": 1165,
        "column": 68
      }
    }
  }
}
```

### Swagger 4: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionType_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/connectionTypes/{connectionTypeName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/connectionTypes/{connectionTypeName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1457,
        "column": 12
      },
      "end": {
        "line": 1516,
        "column": 66
      }
    }
  }
}
```

### Swagger 5: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Connection_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/connections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/connections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1685,
        "column": 12
      },
      "end": {
        "line": 1750,
        "column": 62
      }
    }
  }
}
```

### Swagger 6: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Credential_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/credentials/{credentialName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/credentials/{credentialName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2040,
        "column": 12
      },
      "end": {
        "line": 2105,
        "column": 62
      }
    }
  }
}
```

### Swagger 7: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'HybridRunbookWorkerGroup_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups/{hybridRunbookWorkerGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups/{hybridRunbookWorkerGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2338,
        "column": 12
      },
      "end": {
        "line": 2403,
        "column": 65
      }
    }
  }
}
```

### Swagger 8: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'HybridRunbookWorkers_Create' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups/{hybridRunbookWorkerGroupName}/hybridRunbookWorkers/{hybridRunbookWorkerId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups/{hybridRunbookWorkerGroupName}/hybridRunbookWorkers/{hybridRunbookWorkerId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2650,
        "column": 12
      },
      "end": {
        "line": 2722,
        "column": 60
      }
    }
  }
}
```

### Swagger 9: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'JobSchedule_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/jobSchedules/{jobScheduleId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/jobSchedules/{jobScheduleId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 3042,
        "column": 12
      },
      "end": {
        "line": 3102,
        "column": 55
      }
    }
  }
}
```

### Swagger 10: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Job_Create' Request Model: 'parameters[6].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/jobs/{jobName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/jobs/{jobName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 3287,
        "column": 12
      },
      "end": {
        "line": 3353,
        "column": 51
      }
    }
  }
}
```

### Swagger 11: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Module_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/modules/{moduleName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/modules/{moduleName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 4066,
        "column": 12
      },
      "end": {
        "line": 4131,
        "column": 58
      }
    }
  }
}
```

### Swagger 12: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'DscNodeConfiguration_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodeConfigurations/{nodeConfigurationName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodeConfigurations/{nodeConfigurationName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 4647,
        "column": 12
      },
      "end": {
        "line": 4727,
        "column": 43
      }
    }
  }
}
```

### Swagger 13: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Python2Package_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/python2Packages/{packageName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/python2Packages/{packageName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 5794,
        "column": 12
      },
      "end": {
        "line": 5859,
        "column": 66
      }
    }
  }
}
```

### Swagger 14: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Python3Package_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/python3Packages/{packageName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/python3Packages/{packageName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 6085,
        "column": 12
      },
      "end": {
        "line": 6150,
        "column": 66
      }
    }
  }
}
```

### Swagger 15: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Runbook_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 6380,
        "column": 12
      },
      "end": {
        "line": 6449,
        "column": 66
      }
    }
  }
}
```

### Swagger 16: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'TestJob_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}/draft/testJob",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}/draft/testJob",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 6890,
        "column": 12
      },
      "end": {
        "line": 6950,
        "column": 59
      }
    }
  }
}
```

### Swagger 17: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Package_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runtimeEnvironments/{runtimeEnvironmentName}/packages/{packageName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runtimeEnvironments/{runtimeEnvironmentName}/packages/{packageName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 7795,
        "column": 12
      },
      "end": {
        "line": 7868,
        "column": 67
      }
    }
  }
}
```

### Swagger 18: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Schedule_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/schedules/{scheduleName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/schedules/{scheduleName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 8116,
        "column": 12
      },
      "end": {
        "line": 8184,
        "column": 60
      }
    }
  }
}
```

### Swagger 19: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SourceControl_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 8971,
        "column": 12
      },
      "end": {
        "line": 9036,
        "column": 79
      }
    }
  }
}
```

### Swagger 20: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SourceControlSyncJob_Create' Request Model: 'parameters[6].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 9284,
        "column": 12
      },
      "end": {
        "line": 9351,
        "column": 85
      }
    }
  }
}
```

### Swagger 21: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Variable_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/variables/{variableName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/variables/{variableName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 9722,
        "column": 12
      },
      "end": {
        "line": 9787,
        "column": 60
      }
    }
  }
}
```

### Swagger 22: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Webhook_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/webhooks/{webhookName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/webhooks/{webhookName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 10424,
        "column": 12
      },
      "end": {
        "line": 10489,
        "column": 59
      }
    }
  }
}
```

### Swagger 23: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: TestJob_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}/draft/testJob",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}/draft/testJob",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 6890,
        "column": 12
      },
      "end": {
        "line": 6950,
        "column": 59
      }
    }
  }
}
```

### Swagger 24: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: SourceControlSyncJob_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 9284,
        "column": 12
      },
      "end": {
        "line": 9351,
        "column": 85
      }
    }
  }
}
```

### Swagger 25: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodeConfigurations/{nodeConfigurationName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodeConfigurations/{nodeConfigurationName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodeConfigurations/{nodeConfigurationName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 4592,
        "column": 190
      },
      "end": {
        "line": 4776,
        "column": 64
      }
    }
  }
}
```

### Swagger 26: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/automation/resource-manager/Microsoft.Automation/Automation",
  "swaggerFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "validatorInputFile": "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json",
  "sourceDocuments": [
    "projects/specification/automation/resource-manager/Microsoft.Automation/Automation/swagger/stable/2024-10-23/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 9221,
        "column": 229
      },
      "end": {
        "line": 9351,
        "column": 85
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.AutomationAccount. Found Microsoft.Automation.AutomationAccountCreateOrUpdateParameters.",
  "sourceFile": "AutomationAccount.tsp",
  "line": 76,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.DscConfiguration. Found Microsoft.Automation.DscConfigurationCreateOrUpdateParameters.",
  "sourceFile": "DscConfiguration.tsp",
  "line": 49,
  "column": 3
}
```

### TypeSpec 3

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.DscNodeConfiguration. Found Microsoft.Automation.DscNodeConfigurationCreateOrUpdateParameters.",
  "sourceFile": "DscNodeConfiguration.tsp",
  "line": 45,
  "column": 3
}
```

### TypeSpec 4

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.HybridRunbookWorker. Found Microsoft.Automation.HybridRunbookWorkerCreateParameters.",
  "sourceFile": "HybridRunbookWorker.tsp",
  "line": 43,
  "column": 3
}
```

### TypeSpec 5

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.HybridRunbookWorkerGroup. Found Microsoft.Automation.HybridRunbookWorkerGroupCreateOrUpdateParameters.",
  "sourceFile": "HybridRunbookWorkerGroup.tsp",
  "line": 44,
  "column": 3
}
```

### TypeSpec 6

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.Certificate. Found Microsoft.Automation.CertificateCreateOrUpdateParameters.",
  "sourceFile": "Certificate.tsp",
  "line": 43,
  "column": 3
}
```

### TypeSpec 7

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.Connection. Found Microsoft.Automation.ConnectionCreateOrUpdateParameters.",
  "sourceFile": "Connection.tsp",
  "line": 42,
  "column": 3
}
```

### TypeSpec 8

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.ConnectionType. Found Microsoft.Automation.ConnectionTypeCreateOrUpdateParameters.",
  "sourceFile": "ConnectionType.tsp",
  "line": 44,
  "column": 3
}
```

### TypeSpec 9

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.Credential. Found Microsoft.Automation.CredentialCreateOrUpdateParameters.",
  "sourceFile": "Credential.tsp",
  "line": 42,
  "column": 3
}
```

### TypeSpec 10

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.Job. Found Microsoft.Automation.JobCreateParameters.",
  "sourceFile": "Job.tsp",
  "line": 54,
  "column": 3
}
```

### TypeSpec 11

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.JobSchedule. Found Microsoft.Automation.JobScheduleCreateParameters.",
  "sourceFile": "JobSchedule.tsp",
  "line": 44,
  "column": 3
}
```

### TypeSpec 12

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.Module. Found Microsoft.Automation.ModuleCreateOrUpdateParameters.",
  "sourceFile": "Module.tsp",
  "line": 71,
  "column": 3
}
```

### TypeSpec 13

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.Module. Found Microsoft.Automation.PythonPackageCreateParameters.",
  "sourceFile": "Module.tsp",
  "line": 223,
  "column": 3
}
```

### TypeSpec 14

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.Module. Found Microsoft.Automation.PythonPackageCreateParameters.",
  "sourceFile": "Module.tsp",
  "line": 291,
  "column": 3
}
```

### TypeSpec 15

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.Package. Found Microsoft.Automation.PackageCreateOrUpdateParameters.",
  "sourceFile": "Package.tsp",
  "line": 42,
  "column": 3
}
```

### TypeSpec 16

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.Runbook. Found Microsoft.Automation.RunbookCreateOrUpdateParameters.",
  "sourceFile": "Runbook.tsp",
  "line": 65,
  "column": 3
}
```

### TypeSpec 17

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.Schedule. Found Microsoft.Automation.ScheduleCreateOrUpdateParameters.",
  "sourceFile": "Schedule.tsp",
  "line": 43,
  "column": 3
}
```

### TypeSpec 18

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.SourceControl. Found Microsoft.Automation.SourceControlCreateOrUpdateParameters.",
  "sourceFile": "SourceControl.tsp",
  "line": 55,
  "column": 3
}
```

### TypeSpec 19

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.Variable. Found Microsoft.Automation.VariableCreateOrUpdateParameters.",
  "sourceFile": "Variable.tsp",
  "line": 42,
  "column": 3
}
```

### TypeSpec 20

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Automation.Webhook. Found Microsoft.Automation.WebhookCreateOrUpdateParameters.",
  "sourceFile": "Webhook.tsp",
  "line": 42,
  "column": 3
}
```

## specification/batch/resource-manager/Microsoft.Batch/Batch

Swagger raw: 1; TypeSpec raw: 2; source-aligned: 2; default: 2.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/batch/resource-manager/Microsoft.Batch/Batch",
  "swaggerFile": "projects/specification/batch/resource-manager/Microsoft.Batch/Batch/swagger/stable/2025-06-01/openapi.json",
  "validatorInputFile": "projects/specification/batch/resource-manager/Microsoft.Batch/Batch/swagger/stable/2025-06-01/openapi.json",
  "sourceDocuments": [
    "projects/specification/batch/resource-manager/Microsoft.Batch/Batch/swagger/stable/2025-06-01/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'BatchAccount_Create' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 401,
        "column": 12
      },
      "end": {
        "line": 486,
        "column": 43
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Batch.BatchAccount. Found Microsoft.Batch.BatchAccountCreateParameters.",
  "sourceFile": "BatchAccount.tsp",
  "line": 44,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Batch.Certificate. Found Microsoft.Batch.CertificateCreateOrUpdateParameters.",
  "sourceFile": "Certificate.tsp",
  "line": 69,
  "column": 3
}
```

## specification/billing/resource-manager/Microsoft.Billing/Billing

Swagger raw: 2; TypeSpec raw: 2; source-aligned: 2; default: 2.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/billing/resource-manager/Microsoft.Billing/Billing",
  "swaggerFile": "projects/specification/billing/resource-manager/Microsoft.Billing/Billing/swagger/stable/2024-04-01/openapi.json",
  "validatorInputFile": "projects/specification/billing/resource-manager/Microsoft.Billing/Billing/swagger/stable/2024-04-01/openapi.json",
  "sourceDocuments": [
    "projects/specification/billing/resource-manager/Microsoft.Billing/Billing/swagger/stable/2024-04-01/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PartnerTransfers_Initiate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/customers/{customerName}/transfers/{transferName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/customers/{customerName}/transfers/{transferName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 3632,
        "column": 12
      },
      "end": {
        "line": 3706,
        "column": 62
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/billing/resource-manager/Microsoft.Billing/Billing",
  "swaggerFile": "projects/specification/billing/resource-manager/Microsoft.Billing/Billing/swagger/stable/2024-04-01/openapi.json",
  "validatorInputFile": "projects/specification/billing/resource-manager/Microsoft.Billing/Billing/swagger/stable/2024-04-01/openapi.json",
  "sourceDocuments": [
    "projects/specification/billing/resource-manager/Microsoft.Billing/Billing/swagger/stable/2024-04-01/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Transfers_Initiate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/transfers/{transferName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/transfers/{transferName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 5400,
        "column": 12
      },
      "end": {
        "line": 5474,
        "column": 55
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Billing.PartnerTransferDetails. Found Microsoft.Billing.PartnerInitiateTransferRequest.",
  "sourceFile": "PartnerTransferDetails.tsp",
  "line": 52,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Billing.TransferDetails. Found Microsoft.Billing.InitiateTransferRequest.",
  "sourceFile": "TransferDetails.tsp",
  "line": 50,
  "column": 3
}
```

## specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits

Swagger raw: 1; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits",
  "swaggerFile": "projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json",
  "validatorInputFile": "projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json",
  "sourceDocuments": [
    "projects/specification/billingbenefits/resource-manager/Microsoft.BillingBenefits/BillingBenefits/swagger/stable/2026-06-01/billingbenefits.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ReservationOrderAlias_Create' Request Model: 'parameters[2].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/providers/Microsoft.BillingBenefits/reservationOrderAliases/{reservationOrderAliasName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/providers/Microsoft.BillingBenefits/reservationOrderAliases/{reservationOrderAliasName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 562,
        "column": 12
      },
      "end": {
        "line": 633,
        "column": 43
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.BillingBenefits.ReservationOrderAliasResponse. Found Microsoft.BillingBenefits.ReservationOrderAliasRequest.",
  "sourceFile": "ReservationOrderAliasResponse.tsp",
  "line": 54,
  "column": 3
}
```

## specification/cdn/resource-manager/Microsoft.Cdn/Cdn

Swagger raw: 1; TypeSpec raw: 2; source-aligned: 2; default: 2.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cdn/resource-manager/Microsoft.Cdn/Cdn",
  "swaggerFile": "projects/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/swagger/preview/2026-08-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/swagger/preview/2026-08-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cdn/resource-manager/Microsoft.Cdn/Cdn/swagger/preview/2026-08-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'CustomDomains_Create' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 3429,
        "column": 12
      },
      "end": {
        "line": 3531,
        "column": 43
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "RuleSet.tsp",
  "line": 43,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Cdn.CustomDomain. Found Microsoft.Cdn.CustomDomainParameters.",
  "sourceFile": "CustomDomain.tsp",
  "line": 41,
  "column": 3
}
```

## specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices

Swagger raw: 1; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices",
  "swaggerFile": "projects/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices/swagger/preview/2026-09-15-preview/cognitiveservices.json",
  "validatorInputFile": "projects/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices/swagger/preview/2026-09-15-preview/cognitiveservices.json",
  "sourceDocuments": [
    "projects/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/CognitiveServices/swagger/preview/2026-09-15-preview/cognitiveservices.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/computes/{computeName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/computes/{computeName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/computes/{computeName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3279,
        "column": 157
      },
      "end": {
        "line": 3492,
        "column": 43
      }
    }
  }
}
```

## specification/compute/resource-manager/Microsoft.Compute/Compute/Compute

Swagger raw: 2; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/compute/resource-manager/Microsoft.Compute/Compute/Compute",
  "swaggerFile": "projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json",
  "validatorInputFile": "projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json",
  "sourceDocuments": [
    "projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualMachineScaleSetExtensions_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 6803,
        "column": 12
      },
      "end": {
        "line": 6886,
        "column": 43
      }
    }
  }
}
```

### Swagger 2: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/compute/resource-manager/Microsoft.Compute/Compute/Compute",
  "swaggerFile": "projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json",
  "validatorInputFile": "projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json",
  "sourceDocuments": [
    "projects/specification/compute/resource-manager/Microsoft.Compute/Compute/Compute/swagger/stable/2026-04-01/ComputeRP.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualMachineScaleSetVMExtensions_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 9530,
        "column": 12
      },
      "end": {
        "line": 9617,
        "column": 43
      }
    }
  }
}
```

## specification/confluent/resource-manager/Microsoft.Confluent/Confluent

Swagger raw: 1; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/confluent/resource-manager/Microsoft.Confluent/Confluent",
  "swaggerFile": "projects/specification/confluent/resource-manager/Microsoft.Confluent/Confluent/swagger/preview/2026-06-02-preview/confluent.json",
  "validatorInputFile": "projects/specification/confluent/resource-manager/Microsoft.Confluent/Confluent/swagger/preview/2026-06-02-preview/confluent.json",
  "sourceDocuments": [
    "projects/specification/confluent/resource-manager/Microsoft.Confluent/Confluent/swagger/preview/2026-06-02-preview/confluent.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: MarketplaceAgreements_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/providers/Microsoft.Confluent/agreements/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/providers/Microsoft.Confluent/agreements/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 210,
        "column": 12
      },
      "end": {
        "line": 250,
        "column": 81
      }
    }
  }
}
```

## specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry

Swagger raw: 1; TypeSpec raw: 2; source-aligned: 2; default: 2.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry",
  "swaggerFile": "projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json",
  "validatorInputFile": "projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json",
  "sourceDocuments": [
    "projects/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/swagger/preview/2026-09-01-preview/containerregistry.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Webhooks_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/webhooks/{webhookName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/webhooks/{webhookName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 5206,
        "column": 12
      },
      "end": {
        "line": 5292,
        "column": 43
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "ArchiveVersion.tsp",
  "line": 84,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.ContainerRegistry.Webhook. Found Microsoft.ContainerRegistry.WebhookCreateParameters.",
  "sourceFile": "Webhook.tsp",
  "line": 36,
  "column": 3
}
```

## specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB

Swagger raw: 33; TypeSpec raw: 31; source-aligned: 31; default: 31.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'DatabaseAccounts_CreateOrUpdate' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2508,
        "column": 12
      },
      "end": {
        "line": 2576,
        "column": 43
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'CassandraResources_CreateUpdateCassandraKeyspace' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2803,
        "column": 12
      },
      "end": {
        "line": 2885,
        "column": 43
      }
    }
  }
}
```

### Swagger 3: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'CassandraResources_CreateUpdateCassandraTable' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/tables/{tableName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/tables/{tableName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 3069,
        "column": 12
      },
      "end": {
        "line": 3158,
        "column": 43
      }
    }
  }
}
```

### Swagger 4: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'CassandraResources_UpdateCassandraTableThroughput' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/tables/{tableName}/throughputSettings/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/tables/{tableName}/throughputSettings/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 3293,
        "column": 12
      },
      "end": {
        "line": 3382,
        "column": 43
      }
    }
  }
}
```

### Swagger 5: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'CassandraResources_UpdateCassandraKeyspaceThroughput' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/throughputSettings/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/throughputSettings/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 3605,
        "column": 12
      },
      "end": {
        "line": 3687,
        "column": 43
      }
    }
  }
}
```

### Swagger 6: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'CassandraResources_CreateUpdateCassandraView' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/views/{viewName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/views/{viewName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 3959,
        "column": 12
      },
      "end": {
        "line": 4048,
        "column": 43
      }
    }
  }
}
```

### Swagger 7: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'CassandraResources_UpdateCassandraViewThroughput' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/views/{viewName}/throughputSettings/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/views/{viewName}/throughputSettings/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 4191,
        "column": 12
      },
      "end": {
        "line": 4280,
        "column": 43
      }
    }
  }
}
```

### Swagger 8: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'DataTransferJobs_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/dataTransferJobs/{jobName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/dataTransferJobs/{jobName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 5633,
        "column": 12
      },
      "end": {
        "line": 5690,
        "column": 89
      }
    }
  }
}
```

### Swagger 9: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'GraphResources_CreateUpdateGraph' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/graphs/{graphName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/graphs/{graphName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 6689,
        "column": 12
      },
      "end": {
        "line": 6771,
        "column": 43
      }
    }
  }
}
```

### Swagger 10: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'GremlinResources_CreateUpdateGremlinDatabase' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 6944,
        "column": 12
      },
      "end": {
        "line": 7026,
        "column": 43
      }
    }
  }
}
```

### Swagger 11: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'GremlinResources_CreateUpdateGremlinGraph' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/graphs/{graphName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/graphs/{graphName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 7210,
        "column": 12
      },
      "end": {
        "line": 7299,
        "column": 43
      }
    }
  }
}
```

### Swagger 12: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'GremlinResources_UpdateGremlinGraphThroughput' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/graphs/{graphName}/throughputSettings/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/graphs/{graphName}/throughputSettings/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 7522,
        "column": 12
      },
      "end": {
        "line": 7611,
        "column": 43
      }
    }
  }
}
```

### Swagger 13: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'GremlinResources_UpdateGremlinDatabaseThroughput' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/throughputSettings/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/throughputSettings/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 7834,
        "column": 12
      },
      "end": {
        "line": 7916,
        "column": 43
      }
    }
  }
}
```

### Swagger 14: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'MongoDBResources_CreateUpdateMongoDBDatabase' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 9394,
        "column": 12
      },
      "end": {
        "line": 9479,
        "column": 43
      }
    }
  }
}
```

### Swagger 15: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'MongoDBResources_CreateUpdateMongoDBCollection' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/collections/{collectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/collections/{collectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 9663,
        "column": 12
      },
      "end": {
        "line": 9755,
        "column": 43
      }
    }
  }
}
```

### Swagger 16: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'MongoDBResources_UpdateMongoDBCollectionThroughput' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/collections/{collectionName}/throughputSettings/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/collections/{collectionName}/throughputSettings/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 10071,
        "column": 12
      },
      "end": {
        "line": 10160,
        "column": 43
      }
    }
  }
}
```

### Swagger 17: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'MongoDBResources_UpdateMongoDBDatabaseThroughput' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/throughputSettings/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/throughputSettings/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 10655,
        "column": 12
      },
      "end": {
        "line": 10737,
        "column": 43
      }
    }
  }
}
```

### Swagger 18: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'MongoDBResources_CreateUpdateMongoRoleDefinition' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbRoleDefinitions/{mongoRoleDefinitionId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbRoleDefinitions/{mongoRoleDefinitionId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 11167,
        "column": 12
      },
      "end": {
        "line": 11244,
        "column": 43
      }
    }
  }
}
```

### Swagger 19: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'MongoDBResources_CreateUpdateMongoUserDefinition' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbUserDefinitions/{mongoUserDefinitionId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbUserDefinitions/{mongoUserDefinitionId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 11417,
        "column": 12
      },
      "end": {
        "line": 11494,
        "column": 43
      }
    }
  }
}
```

### Swagger 20: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'NotebookWorkspaces_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/notebookWorkspaces/{notebookWorkspaceName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/notebookWorkspaces/{notebookWorkspaceName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 11864,
        "column": 12
      },
      "end": {
        "line": 11949,
        "column": 43
      }
    }
  }
}
```

### Swagger 21: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Service_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/services/{serviceName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/services/{serviceName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 13428,
        "column": 12
      },
      "end": {
        "line": 13522,
        "column": 43
      }
    }
  }
}
```

### Swagger 22: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SqlResources_CreateUpdateSqlDatabase' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 13782,
        "column": 12
      },
      "end": {
        "line": 13867,
        "column": 43
      }
    }
  }
}
```

### Swagger 23: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SqlResources_CreateUpdateClientEncryptionKey' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/clientEncryptionKeys/{clientEncryptionKeyName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/clientEncryptionKeys/{clientEncryptionKeyName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14051,
        "column": 12
      },
      "end": {
        "line": 14140,
        "column": 43
      }
    }
  }
}
```

### Swagger 24: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SqlResources_CreateUpdateSqlContainer' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14258,
        "column": 12
      },
      "end": {
        "line": 14353,
        "column": 43
      }
    }
  }
}
```

### Swagger 25: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SqlResources_CreateUpdateSqlStoredProcedure' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/storedProcedures/{storedProcedureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/storedProcedures/{storedProcedureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14734,
        "column": 12
      },
      "end": {
        "line": 14830,
        "column": 43
      }
    }
  }
}
```

### Swagger 26: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SqlResources_UpdateSqlContainerThroughput' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/throughputSettings/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/throughputSettings/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14972,
        "column": 12
      },
      "end": {
        "line": 15061,
        "column": 43
      }
    }
  }
}
```

### Swagger 27: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SqlResources_CreateUpdateSqlTrigger' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/triggers/{triggerName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/triggers/{triggerName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 15527,
        "column": 12
      },
      "end": {
        "line": 15623,
        "column": 43
      }
    }
  }
}
```

### Swagger 28: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SqlResources_CreateUpdateSqlUserDefinedFunction' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/userDefinedFunctions/{userDefinedFunctionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/userDefinedFunctions/{userDefinedFunctionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 15835,
        "column": 12
      },
      "end": {
        "line": 15931,
        "column": 43
      }
    }
  }
}
```

### Swagger 29: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SqlResources_UpdateSqlDatabaseThroughput' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/throughputSettings/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/throughputSettings/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 16152,
        "column": 12
      },
      "end": {
        "line": 16234,
        "column": 43
      }
    }
  }
}
```

### Swagger 30: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SqlResources_CreateUpdateSqlRoleAssignment' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlRoleAssignments/{roleAssignmentId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlRoleAssignments/{roleAssignmentId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 16664,
        "column": 12
      },
      "end": {
        "line": 16741,
        "column": 43
      }
    }
  }
}
```

### Swagger 31: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SqlResources_CreateUpdateSqlRoleDefinition' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlRoleDefinitions/{roleDefinitionId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlRoleDefinitions/{roleDefinitionId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 16914,
        "column": 12
      },
      "end": {
        "line": 16991,
        "column": 43
      }
    }
  }
}
```

### Swagger 32: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'TableResources_CreateUpdateTable' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/tables/{tableName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/tables/{tableName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 17669,
        "column": 12
      },
      "end": {
        "line": 17751,
        "column": 43
      }
    }
  }
}
```

### Swagger 33: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB",
  "swaggerFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/cosmos-db/resource-manager/Microsoft.DocumentDB/DocumentDB/swagger/preview/2026-04-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'TableResources_UpdateTableThroughput' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/tables/{tableName}/throughputSettings/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/tables/{tableName}/throughputSettings/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 17953,
        "column": 12
      },
      "end": {
        "line": 18035,
        "column": 43
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.GraphResourceGetResults. Found Microsoft.DocumentDB.GraphResourceCreateUpdateParameters.",
  "sourceFile": "GraphResourceGetResults.tsp",
  "line": 58,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.SqlDatabaseGetResults. Found Microsoft.DocumentDB.SqlDatabaseCreateUpdateParameters.",
  "sourceFile": "SqlDatabaseGetResults.tsp",
  "line": 56,
  "column": 3
}
```

### TypeSpec 3

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.ClientEncryptionKeyGetResults. Found Microsoft.DocumentDB.ClientEncryptionKeyCreateUpdateParameters.",
  "sourceFile": "ClientEncryptionKeyGetResults.tsp",
  "line": 40,
  "column": 3
}
```

### TypeSpec 4

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.SqlContainerGetResults. Found Microsoft.DocumentDB.SqlContainerCreateUpdateParameters.",
  "sourceFile": "SqlContainerGetResults.tsp",
  "line": 56,
  "column": 3
}
```

### TypeSpec 5

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.SqlStoredProcedureGetResults. Found Microsoft.DocumentDB.SqlStoredProcedureCreateUpdateParameters.",
  "sourceFile": "SqlStoredProcedureGetResults.tsp",
  "line": 55,
  "column": 3
}
```

### TypeSpec 6

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.SqlUserDefinedFunctionGetResults. Found Microsoft.DocumentDB.SqlUserDefinedFunctionCreateUpdateParameters.",
  "sourceFile": "SqlUserDefinedFunctionGetResults.tsp",
  "line": 55,
  "column": 3
}
```

### TypeSpec 7

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.SqlTriggerGetResults. Found Microsoft.DocumentDB.SqlTriggerCreateUpdateParameters.",
  "sourceFile": "SqlTriggerGetResults.tsp",
  "line": 55,
  "column": 3
}
```

### TypeSpec 8

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.MongoDBDatabaseGetResults. Found Microsoft.DocumentDB.MongoDBDatabaseCreateUpdateParameters.",
  "sourceFile": "MongoDBDatabaseGetResults.tsp",
  "line": 59,
  "column": 3
}
```

### TypeSpec 9

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.MongoDBCollectionGetResults. Found Microsoft.DocumentDB.MongoDBCollectionCreateUpdateParameters.",
  "sourceFile": "MongoDBCollectionGetResults.tsp",
  "line": 58,
  "column": 3
}
```

### TypeSpec 10

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.TableGetResults. Found Microsoft.DocumentDB.TableCreateUpdateParameters.",
  "sourceFile": "TableGetResults.tsp",
  "line": 54,
  "column": 3
}
```

### TypeSpec 11

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.CassandraKeyspaceGetResults. Found Microsoft.DocumentDB.CassandraKeyspaceCreateUpdateParameters.",
  "sourceFile": "CassandraKeyspaceGetResults.tsp",
  "line": 54,
  "column": 3
}
```

### TypeSpec 12

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.CassandraTableGetResults. Found Microsoft.DocumentDB.CassandraTableCreateUpdateParameters.",
  "sourceFile": "CassandraTableGetResults.tsp",
  "line": 54,
  "column": 3
}
```

### TypeSpec 13

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.GremlinDatabaseGetResults. Found Microsoft.DocumentDB.GremlinDatabaseCreateUpdateParameters.",
  "sourceFile": "GremlinDatabaseGetResults.tsp",
  "line": 54,
  "column": 3
}
```

### TypeSpec 14

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.GremlinGraphGetResults. Found Microsoft.DocumentDB.GremlinGraphCreateUpdateParameters.",
  "sourceFile": "GremlinGraphGetResults.tsp",
  "line": 54,
  "column": 3
}
```

### TypeSpec 15

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.CassandraViewGetResults. Found Microsoft.DocumentDB.CassandraViewCreateUpdateParameters.",
  "sourceFile": "CassandraViewGetResults.tsp",
  "line": 58,
  "column": 3
}
```

### TypeSpec 16

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.DataTransferJobGetResults. Found Microsoft.DocumentDB.CreateJobRequest.",
  "sourceFile": "DataTransferJobGetResults.tsp",
  "line": 44,
  "column": 3
}
```

### TypeSpec 17

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.MongoRoleDefinitionGetResults. Found Microsoft.DocumentDB.MongoRoleDefinitionCreateUpdateParameters.",
  "sourceFile": "MongoRoleDefinitionGetResults.tsp",
  "line": 42,
  "column": 3
}
```

### TypeSpec 18

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.MongoUserDefinitionGetResults. Found Microsoft.DocumentDB.MongoUserDefinitionCreateUpdateParameters.",
  "sourceFile": "MongoUserDefinitionGetResults.tsp",
  "line": 42,
  "column": 3
}
```

### TypeSpec 19

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.SqlRoleDefinitionGetResults. Found Microsoft.DocumentDB.SqlRoleDefinitionCreateUpdateParameters.",
  "sourceFile": "SqlRoleDefinitionGetResults.tsp",
  "line": 42,
  "column": 3
}
```

### TypeSpec 20

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.SqlRoleAssignmentGetResults. Found Microsoft.DocumentDB.SqlRoleAssignmentCreateUpdateParameters.",
  "sourceFile": "SqlRoleAssignmentGetResults.tsp",
  "line": 42,
  "column": 3
}
```

### TypeSpec 21

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.ServiceResource. Found Microsoft.DocumentDB.ServiceResourceCreateUpdateParameters.",
  "sourceFile": "ServiceResource.tsp",
  "line": 47,
  "column": 3
}
```

### TypeSpec 22

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.ThroughputSettingsGetResults. Found Microsoft.DocumentDB.ThroughputSettingsUpdateParameters.",
  "sourceFile": "ThroughputSettingsGetResults.tsp",
  "line": 90,
  "column": 3
}
```

### TypeSpec 23

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.ThroughputSettingsGetResults. Found Microsoft.DocumentDB.ThroughputSettingsUpdateParameters.",
  "sourceFile": "ThroughputSettingsGetResults.tsp",
  "line": 211,
  "column": 3
}
```

### TypeSpec 24

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.ThroughputSettingsGetResults. Found Microsoft.DocumentDB.ThroughputSettingsUpdateParameters.",
  "sourceFile": "ThroughputSettingsGetResults.tsp",
  "line": 323,
  "column": 3
}
```

### TypeSpec 25

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.ThroughputSettingsGetResults. Found Microsoft.DocumentDB.ThroughputSettingsUpdateParameters.",
  "sourceFile": "ThroughputSettingsGetResults.tsp",
  "line": 449,
  "column": 3
}
```

### TypeSpec 26

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.ThroughputSettingsGetResults. Found Microsoft.DocumentDB.ThroughputSettingsUpdateParameters.",
  "sourceFile": "ThroughputSettingsGetResults.tsp",
  "line": 566,
  "column": 3
}
```

### TypeSpec 27

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.ThroughputSettingsGetResults. Found Microsoft.DocumentDB.ThroughputSettingsUpdateParameters.",
  "sourceFile": "ThroughputSettingsGetResults.tsp",
  "line": 649,
  "column": 3
}
```

### TypeSpec 28

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.ThroughputSettingsGetResults. Found Microsoft.DocumentDB.ThroughputSettingsUpdateParameters.",
  "sourceFile": "ThroughputSettingsGetResults.tsp",
  "line": 739,
  "column": 3
}
```

### TypeSpec 29

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.ThroughputSettingsGetResults. Found Microsoft.DocumentDB.ThroughputSettingsUpdateParameters.",
  "sourceFile": "ThroughputSettingsGetResults.tsp",
  "line": 829,
  "column": 3
}
```

### TypeSpec 30

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.ThroughputSettingsGetResults. Found Microsoft.DocumentDB.ThroughputSettingsUpdateParameters.",
  "sourceFile": "ThroughputSettingsGetResults.tsp",
  "line": 912,
  "column": 3
}
```

### TypeSpec 31

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DocumentDB.ThroughputSettingsGetResults. Found Microsoft.DocumentDB.ThroughputSettingsUpdateParameters.",
  "sourceFile": "ThroughputSettingsGetResults.tsp",
  "line": 1002,
  "column": 3
}
```

## specification/datadog/resource-manager/Microsoft.Datadog/Datadog

Swagger raw: 1; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/datadog/resource-manager/Microsoft.Datadog/Datadog",
  "swaggerFile": "projects/specification/datadog/resource-manager/Microsoft.Datadog/Datadog/swagger/preview/2025-12-26-preview/datadog.json",
  "validatorInputFile": "projects/specification/datadog/resource-manager/Microsoft.Datadog/Datadog/swagger/preview/2025-12-26-preview/datadog.json",
  "sourceDocuments": [
    "projects/specification/datadog/resource-manager/Microsoft.Datadog/Datadog/swagger/preview/2025-12-26-preview/datadog.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: MarketplaceAgreements_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/providers/Microsoft.Datadog/agreements/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/providers/Microsoft.Datadog/agreements/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 175,
        "column": 12
      },
      "end": {
        "line": 212,
        "column": 66
      }
    }
  }
}
```

## specification/datafactory/resource-manager/Microsoft.DataFactory/DataFactory

Swagger raw: 1; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/datafactory/resource-manager/Microsoft.DataFactory/DataFactory",
  "swaggerFile": "projects/specification/datafactory/resource-manager/Microsoft.DataFactory/DataFactory/swagger/stable/2018-06-01/openapi.json",
  "validatorInputFile": "projects/specification/datafactory/resource-manager/Microsoft.DataFactory/DataFactory/swagger/stable/2018-06-01/openapi.json",
  "sourceDocuments": [
    "projects/specification/datafactory/resource-manager/Microsoft.DataFactory/DataFactory/swagger/stable/2018-06-01/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PrivateEndpointConnection_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/privateEndpointConnections/{privateEndpointConnectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/privateEndpointConnections/{privateEndpointConnectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 5491,
        "column": 12
      },
      "end": {
        "line": 5558,
        "column": 76
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DataFactory.PrivateEndpointConnectionResource. Found Microsoft.DataFactory.PrivateLinkConnectionApprovalRequestResource.",
  "sourceFile": "PrivateEndpointConnectionResource.tsp",
  "line": 54,
  "column": 3
}
```

## specification/dns/resource-manager/Microsoft.Network/Dns

Swagger raw: 0; TypeSpec raw: 1; source-aligned: 1; default: 1.

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "DnssecConfig.tsp",
  "line": 45,
  "column": 3
}
```

## specification/domainservices/resource-manager/Microsoft.AAD/DomainServices

Swagger raw: 1; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/domainservices/resource-manager/Microsoft.AAD/DomainServices",
  "swaggerFile": "projects/specification/domainservices/resource-manager/Microsoft.AAD/DomainServices/swagger/preview/2026-08-31-preview/openapi.json",
  "validatorInputFile": "projects/specification/domainservices/resource-manager/Microsoft.AAD/DomainServices/swagger/preview/2026-08-31-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/domainservices/resource-manager/Microsoft.AAD/DomainServices/swagger/preview/2026-08-31-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'OuContainer_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AAD/domainServices/{domainServiceName}/ouContainer/{ouContainerName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AAD/domainServices/{domainServiceName}/ouContainer/{ouContainerName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 563,
        "column": 12
      },
      "end": {
        "line": 667,
        "column": 43
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.AAD.OuContainer. Found Microsoft.AAD.ContainerAccount.",
  "sourceFile": "OuContainer.tsp",
  "line": 58,
  "column": 3
}
```

## specification/durabletask/resource-manager/Microsoft.DurableTask/DurableTask

Swagger raw: 1; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: ConsistentResponseSchemaForPut

```json
{
  "rule": "ConsistentResponseSchemaForPut",
  "level": "error",
  "project": "specification/durabletask/resource-manager/Microsoft.DurableTask/DurableTask",
  "swaggerFile": "common-types/resource-management/v6/privatelinks.json",
  "validatorInputFile": "projects/specification/durabletask/resource-manager/Microsoft.DurableTask/DurableTask/swagger/preview/2026-05-01-preview/durabletask.json",
  "sourceDocuments": [
    "common-types/resource-management/v6/privatelinks.json"
  ],
  "sourceAttribution": "reported",
  "message": "200 response schema does not match 201 response schema. A PUT API must always return the same response schema for both the 200 and 201 status codes.",
  "path": [
    "definitions",
    "PrivateEndpointConnection"
  ]
}
```

## specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid

Swagger raw: 6; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid",
  "swaggerFile": "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json",
  "validatorInputFile": "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json",
  "sourceDocuments": [
    "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2647,
        "column": 124
      },
      "end": {
        "line": 2897,
        "column": 43
      }
    }
  }
}
```

### Swagger 2: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid",
  "swaggerFile": "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json",
  "validatorInputFile": "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json",
  "sourceDocuments": [
    "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 8411,
        "column": 144
      },
      "end": {
        "line": 8661,
        "column": 43
      }
    }
  }
}
```

### Swagger 3: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid",
  "swaggerFile": "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json",
  "validatorInputFile": "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json",
  "sourceDocuments": [
    "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName}/channels/{channelName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName}/channels/{channelName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName}/channels/{channelName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 8729,
        "column": 167
      },
      "end": {
        "line": 8975,
        "column": 43
      }
    }
  }
}
```

### Swagger 4: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid",
  "swaggerFile": "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json",
  "validatorInputFile": "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json",
  "sourceDocuments": [
    "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerRegistrations/{partnerRegistrationName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerRegistrations/{partnerRegistrationName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerRegistrations/{partnerRegistrationName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 9193,
        "column": 150
      },
      "end": {
        "line": 9449,
        "column": 43
      }
    }
  }
}
```

### Swagger 5: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid",
  "swaggerFile": "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json",
  "validatorInputFile": "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json",
  "sourceDocuments": [
    "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerTopics/{partnerTopicName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerTopics/{partnerTopicName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerTopics/{partnerTopicName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 9510,
        "column": 136
      },
      "end": {
        "line": 9734,
        "column": 43
      }
    }
  }
}
```

### Swagger 6: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid",
  "swaggerFile": "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json",
  "validatorInputFile": "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json",
  "sourceDocuments": [
    "projects/specification/eventgrid/resource-manager/Microsoft.EventGrid/EventGrid/swagger/preview/2026-06-15-preview/EventGrid.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 11179,
        "column": 122
      },
      "end": {
        "line": 11429,
        "column": 43
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "DomainTopic.tsp",
  "line": 41,
  "column": 3
}
```

## specification/fileshares/resource-manager/Microsoft.FileShares/FileShares

Swagger raw: 1; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/fileshares/resource-manager/Microsoft.FileShares/FileShares",
  "swaggerFile": "projects/specification/fileshares/resource-manager/Microsoft.FileShares/FileShares/swagger/stable/2026-06-01/fileshares.json",
  "validatorInputFile": "projects/specification/fileshares/resource-manager/Microsoft.FileShares/FileShares/swagger/stable/2026-06-01/fileshares.json",
  "sourceDocuments": [
    "projects/specification/fileshares/resource-manager/Microsoft.FileShares/FileShares/swagger/stable/2026-06-01/fileshares.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FileShares/fileShares/{resourceName}/fileShareSnapshots/{name} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FileShares/fileShares/{resourceName}/fileShareSnapshots/{name}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FileShares/fileShares/{resourceName}/fileShareSnapshots/{name}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 681,
        "column": 156
      },
      "end": {
        "line": 963,
        "column": 43
      }
    }
  }
}
```

## specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments

Swagger raw: 4; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments",
  "swaggerFile": "projects/specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments/swagger/stable/2024-04-05/guestconfiguration.json",
  "validatorInputFile": "projects/specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments/swagger/stable/2024-04-05/guestconfiguration.json",
  "sourceDocuments": [
    "projects/specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments/swagger/stable/2024-04-05/guestconfiguration.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: GuestConfigurationAssignmentsVMSS_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmssName}/providers/Microsoft.GuestConfiguration/guestConfigurationAssignments/{name}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmssName}/providers/Microsoft.GuestConfiguration/guestConfigurationAssignments/{name}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 228,
        "column": 12
      },
      "end": {
        "line": 287,
        "column": 84
      }
    }
  }
}
```

### Swagger 2: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments",
  "swaggerFile": "projects/specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments/swagger/stable/2024-04-05/guestconfiguration.json",
  "validatorInputFile": "projects/specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments/swagger/stable/2024-04-05/guestconfiguration.json",
  "sourceDocuments": [
    "projects/specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments/swagger/stable/2024-04-05/guestconfiguration.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: GuestConfigurationAssignments_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/providers/Microsoft.GuestConfiguration/guestConfigurationAssignments/{guestConfigurationAssignmentName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/providers/Microsoft.GuestConfiguration/guestConfigurationAssignments/{guestConfigurationAssignmentName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 556,
        "column": 12
      },
      "end": {
        "line": 619,
        "column": 80
      }
    }
  }
}
```

### Swagger 3: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments",
  "swaggerFile": "projects/specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments/swagger/stable/2024-04-05/guestconfiguration.json",
  "validatorInputFile": "projects/specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments/swagger/stable/2024-04-05/guestconfiguration.json",
  "sourceDocuments": [
    "projects/specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments/swagger/stable/2024-04-05/guestconfiguration.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: GuestConfigurationConnectedVMwarevSphereAssignments_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ConnectedVMwarevSphere/virtualmachines/{vmName}/providers/Microsoft.GuestConfiguration/guestConfigurationAssignments/{guestConfigurationAssignmentName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ConnectedVMwarevSphere/virtualmachines/{vmName}/providers/Microsoft.GuestConfiguration/guestConfigurationAssignments/{guestConfigurationAssignmentName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 892,
        "column": 12
      },
      "end": {
        "line": 956,
        "column": 102
      }
    }
  }
}
```

### Swagger 4: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments",
  "swaggerFile": "projects/specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments/swagger/stable/2024-04-05/guestconfiguration.json",
  "validatorInputFile": "projects/specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments/swagger/stable/2024-04-05/guestconfiguration.json",
  "sourceDocuments": [
    "projects/specification/guestconfiguration/resource-manager/Microsoft.GuestConfiguration/Assignments/swagger/stable/2024-04-05/guestconfiguration.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: GuestConfigurationHCRPAssignments_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{machineName}/providers/Microsoft.GuestConfiguration/guestConfigurationAssignments/{guestConfigurationAssignmentName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{machineName}/providers/Microsoft.GuestConfiguration/guestConfigurationAssignments/{guestConfigurationAssignmentName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1274,
        "column": 12
      },
      "end": {
        "line": 1336,
        "column": 84
      }
    }
  }
}
```

## specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight

Swagger raw: 9; TypeSpec raw: 2; source-aligned: 2; default: 2.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight",
  "swaggerFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "validatorInputFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Clusters_Create' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 504,
        "column": 12
      },
      "end": {
        "line": 616,
        "column": 43
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight",
  "swaggerFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "validatorInputFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Extensions_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/{extensionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/{extensionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1466,
        "column": 12
      },
      "end": {
        "line": 1539,
        "column": 43
      }
    }
  }
}
```

### Swagger 3: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight",
  "swaggerFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "validatorInputFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Extensions_EnableAzureMonitor' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/azureMonitor",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/azureMonitor",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1716,
        "column": 12
      },
      "end": {
        "line": 1782,
        "column": 43
      }
    }
  }
}
```

### Swagger 4: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight",
  "swaggerFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "validatorInputFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Extensions_EnableAzureMonitorAgent' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/azureMonitorAgent",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/azureMonitorAgent",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1892,
        "column": 12
      },
      "end": {
        "line": 1958,
        "column": 43
      }
    }
  }
}
```

### Swagger 5: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight",
  "swaggerFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "validatorInputFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Extensions_EnableMonitoring' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/clustermonitoring",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/clustermonitoring",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2068,
        "column": 12
      },
      "end": {
        "line": 2134,
        "column": 43
      }
    }
  }
}
```

### Swagger 6: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight",
  "swaggerFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "validatorInputFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/{extensionName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/{extensionName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/{extensionName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1414,
        "column": 153
      },
      "end": {
        "line": 1608,
        "column": 43
      }
    }
  }
}
```

### Swagger 7: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight",
  "swaggerFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "validatorInputFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/azureMonitor has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/azureMonitor"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/azureMonitor"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1671,
        "column": 150
      },
      "end": {
        "line": 1844,
        "column": 43
      }
    }
  }
}
```

### Swagger 8: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight",
  "swaggerFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "validatorInputFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/azureMonitorAgent has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/azureMonitorAgent"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/azureMonitorAgent"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1847,
        "column": 155
      },
      "end": {
        "line": 2020,
        "column": 43
      }
    }
  }
}
```

### Swagger 9: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight",
  "swaggerFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "validatorInputFile": "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsight/swagger/preview/2025-01-15-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/clustermonitoring has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/clustermonitoring"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/extensions/clustermonitoring"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2023,
        "column": 155
      },
      "end": {
        "line": 2196,
        "column": 43
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.HDInsight.Cluster. Found Microsoft.HDInsight.ClusterCreateParametersExtended.",
  "sourceFile": "Cluster.tsp",
  "line": 50,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.HDInsight.Cluster. Found Microsoft.HDInsight.Extension.",
  "sourceFile": "routes.tsp",
  "line": 278,
  "column": 3
}
```

## specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis

Swagger raw: 1; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis",
  "swaggerFile": "projects/specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis/swagger/preview/2025-04-01-preview/healthcare-apis.json",
  "validatorInputFile": "projects/specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis/swagger/preview/2025-04-01-preview/healthcare-apis.json",
  "sourceDocuments": [
    "projects/specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/HealthcareApis/swagger/preview/2025-04-01-preview/healthcare-apis.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PrivateEndpointConnections_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName}/privateEndpointConnections/{privateEndpointConnectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName}/privateEndpointConnections/{privateEndpointConnectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 699,
        "column": 12
      },
      "end": {
        "line": 775,
        "column": 43
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.HealthcareApis.PrivateEndpointConnectionDescription. Found Azure.ResourceManager.CommonTypes.PrivateEndpointConnection.",
  "sourceFile": "PrivateEndpointConnectionDescription.tsp",
  "line": 69,
  "column": 3
}
```

## specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb

Swagger raw: 2; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb",
  "swaggerFile": "projects/specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb/swagger/preview/2026-05-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb/swagger/preview/2026-05-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb/swagger/preview/2026-05-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'HorizonDbAdministrators_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HorizonDb/clusters/{clusterName}/administrators/{objectId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HorizonDb/clusters/{clusterName}/administrators/{objectId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 604,
        "column": 12
      },
      "end": {
        "line": 688,
        "column": 43
      }
    }
  }
}
```

### Swagger 2: ConsistentResponseSchemaForPut

```json
{
  "rule": "ConsistentResponseSchemaForPut",
  "level": "error",
  "project": "specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb",
  "swaggerFile": "common-types/resource-management/v6/privatelinks.json",
  "validatorInputFile": "projects/specification/horizondb/resource-manager/Microsoft.HorizonDb/HorizonDb/swagger/preview/2026-05-01-preview/openapi.json",
  "sourceDocuments": [
    "common-types/resource-management/v6/privatelinks.json"
  ],
  "sourceAttribution": "reported",
  "message": "200 response schema does not match 201 response schema. A PUT API must always return the same response schema for both the 200 and 201 status codes.",
  "path": [
    "definitions",
    "PrivateEndpointConnection"
  ]
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.HorizonDb.HorizonDbAdministrator. Found Microsoft.HorizonDb.HorizonDbAdministratorAdd.",
  "sourceFile": "routes.tsp",
  "line": 245,
  "column": 3
}
```

## specification/iothub/resource-manager/Microsoft.Devices/IoTHub

Swagger raw: 1; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/iothub/resource-manager/Microsoft.Devices/IoTHub",
  "swaggerFile": "projects/specification/iothub/resource-manager/Microsoft.Devices/IoTHub/swagger/preview/2026-10-01-preview/iothub.json",
  "validatorInputFile": "projects/specification/iothub/resource-manager/Microsoft.Devices/IoTHub/swagger/preview/2026-10-01-preview/iothub.json",
  "sourceDocuments": [
    "projects/specification/iothub/resource-manager/Microsoft.Devices/IoTHub/swagger/preview/2026-10-01-preview/iothub.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'IotHubResource_CreateEventHubConsumerGroup' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/eventHubEndpoints/{eventHubEndpointName}/ConsumerGroups/{name}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/eventHubEndpoints/{eventHubEndpointName}/ConsumerGroups/{name}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1149,
        "column": 12
      },
      "end": {
        "line": 1213,
        "column": 64
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Devices.EventHubConsumerGroupInfo. Found Microsoft.Devices.EventHubConsumerGroupBodyDescription.",
  "sourceFile": "EventHubConsumerGroupInfo.tsp",
  "line": 69,
  "column": 3
}
```

## specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault

Swagger raw: 5; TypeSpec raw: 4; source-aligned: 4; default: 4.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault",
  "swaggerFile": "projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ManagedHsmKeys_CreateIfNotExist' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/managedHSMs/{name}/keys/{keyName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/managedHSMs/{name}/keys/{keyName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 996,
        "column": 12
      },
      "end": {
        "line": 1056,
        "column": 57
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault",
  "swaggerFile": "projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Vaults_CreateOrUpdate' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1622,
        "column": 12
      },
      "end": {
        "line": 1698,
        "column": 43
      }
    }
  }
}
```

### Swagger 3: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault",
  "swaggerFile": "projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Keys_CreateIfNotExist' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/keys/{keyName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/keys/{keyName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1986,
        "column": 12
      },
      "end": {
        "line": 2044,
        "column": 47
      }
    }
  }
}
```

### Swagger 4: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault",
  "swaggerFile": "projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Secrets_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/secrets/{secretName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/secrets/{secretName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2574,
        "column": 12
      },
      "end": {
        "line": 2636,
        "column": 50
      }
    }
  }
}
```

### Swagger 5: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault",
  "swaggerFile": "projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/keyvault/resource-manager/Microsoft.KeyVault/KeyVault/swagger/preview/2026-06-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: Vaults_UpdateAccessPolicy",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/accessPolicies/{operationKind}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/accessPolicies/{operationKind}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1805,
        "column": 12
      },
      "end": {
        "line": 1877,
        "column": 61
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.KeyVault.Vault. Found Microsoft.KeyVault.VaultCreateOrUpdateParameters.",
  "sourceFile": "Vault.tsp",
  "line": 77,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.KeyVault.Secret. Found Microsoft.KeyVault.SecretCreateOrUpdateParameters.",
  "sourceFile": "Secret.tsp",
  "line": 54,
  "column": 3
}
```

### TypeSpec 3

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.KeyVault.Key. Found Microsoft.KeyVault.KeyCreateParameters.",
  "sourceFile": "Key.tsp",
  "line": 79,
  "column": 3
}
```

### TypeSpec 4

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.KeyVault.ManagedHsmKey. Found Microsoft.KeyVault.ManagedHsmKeyCreateParameters.",
  "sourceFile": "ManagedHsmKey.tsp",
  "line": 77,
  "column": 3
}
```

## specification/management/resource-manager/Microsoft.Management/ManagementGroups

Swagger raw: 2; TypeSpec raw: 3; source-aligned: 3; default: 3.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/management/resource-manager/Microsoft.Management/ManagementGroups",
  "swaggerFile": "projects/specification/management/resource-manager/Microsoft.Management/ManagementGroups/swagger/stable/2023-04-01/management.json",
  "validatorInputFile": "projects/specification/management/resource-manager/Microsoft.Management/ManagementGroups/swagger/stable/2023-04-01/management.json",
  "sourceDocuments": [
    "projects/specification/management/resource-manager/Microsoft.Management/ManagementGroups/swagger/stable/2023-04-01/management.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ManagementGroups_CreateOrUpdate' Request Model: 'parameters[3].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/providers/Microsoft.Management/managementGroups/{groupId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/providers/Microsoft.Management/managementGroups/{groupId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 418,
        "column": 12
      },
      "end": {
        "line": 493,
        "column": 43
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/management/resource-manager/Microsoft.Management/ManagementGroups",
  "swaggerFile": "projects/specification/management/resource-manager/Microsoft.Management/ManagementGroups/swagger/stable/2023-04-01/management.json",
  "validatorInputFile": "projects/specification/management/resource-manager/Microsoft.Management/ManagementGroups/swagger/stable/2023-04-01/management.json",
  "sourceDocuments": [
    "projects/specification/management/resource-manager/Microsoft.Management/ManagementGroups/swagger/stable/2023-04-01/management.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'HierarchySettings_CreateOrUpdate' Request Model: 'parameters[2].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/providers/Microsoft.Management/managementGroups/{groupId}/settings/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/providers/Microsoft.Management/managementGroups/{groupId}/settings/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 757,
        "column": 12
      },
      "end": {
        "line": 800,
        "column": 58
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "SubscriptionUnderManagementGroup.tsp",
  "line": 53,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Management.ManagementGroup. Found Microsoft.Management.CreateManagementGroupRequest.",
  "sourceFile": "ManagementGroup.tsp",
  "line": 81,
  "column": 3
}
```

### TypeSpec 3

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Management.HierarchySettings. Found Microsoft.Management.CreateOrUpdateSettingsRequest.",
  "sourceFile": "HierarchySettings.tsp",
  "line": 42,
  "column": 3
}
```

## specification/maps/resource-manager/Microsoft.Maps/Maps

Swagger raw: 1; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: ConsistentResponseSchemaForPut

```json
{
  "rule": "ConsistentResponseSchemaForPut",
  "level": "error",
  "project": "specification/maps/resource-manager/Microsoft.Maps/Maps",
  "swaggerFile": "common-types/resource-management/v6/privatelinks.json",
  "validatorInputFile": "projects/specification/maps/resource-manager/Microsoft.Maps/Maps/swagger/preview/2025-10-01-preview/maps-management.json",
  "sourceDocuments": [
    "common-types/resource-management/v6/privatelinks.json"
  ],
  "sourceAttribution": "reported",
  "message": "200 response schema does not match 201 response schema. A PUT API must always return the same response schema for both the 200 and 201 status codes.",
  "path": [
    "definitions",
    "PrivateEndpointConnection"
  ]
}
```

## specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace

Swagger raw: 2; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace",
  "swaggerFile": "projects/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/swagger/stable/2025-01-01/Marketplace.json",
  "validatorInputFile": "projects/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/swagger/stable/2025-01-01/Marketplace.json",
  "sourceDocuments": [
    "projects/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/swagger/stable/2025-01-01/Marketplace.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PrivateStore_CreateOrUpdate' Request Model: 'parameters[2].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/providers/Microsoft.Marketplace/privateStores/{privateStoreId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/providers/Microsoft.Marketplace/privateStores/{privateStoreId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 180,
        "column": 12
      },
      "end": {
        "line": 220,
        "column": 58
      }
    }
  }
}
```

### Swagger 2: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace",
  "swaggerFile": "projects/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/swagger/stable/2025-01-01/Marketplace.json",
  "validatorInputFile": "projects/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/swagger/stable/2025-01-01/Marketplace.json",
  "sourceDocuments": [
    "projects/specification/marketplace/resource-manager/Microsoft.Marketplace/Marketplace/swagger/stable/2025-01-01/Marketplace.json"
  ],
  "sourceAttribution": "reported",
  "message": "/providers/Microsoft.Marketplace/privateStores/{privateStoreId} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/providers/Microsoft.Marketplace/privateStores/{privateStoreId}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/providers/Microsoft.Marketplace/privateStores/{privateStoreId}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 141,
        "column": 70
      },
      "end": {
        "line": 258,
        "column": 56
      }
    }
  }
}
```

## specification/mysql/resource-manager/Microsoft.DBforMySQL/FlexibleServers

Swagger raw: 1; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: ConsistentResponseSchemaForPut

```json
{
  "rule": "ConsistentResponseSchemaForPut",
  "level": "error",
  "project": "specification/mysql/resource-manager/Microsoft.DBforMySQL/FlexibleServers",
  "swaggerFile": "common-types/resource-management/v5/privatelinks.json",
  "validatorInputFile": "projects/specification/mysql/resource-manager/Microsoft.DBforMySQL/FlexibleServers/swagger/preview/2025-12-01-preview/openapi.json",
  "sourceDocuments": [
    "common-types/resource-management/v5/privatelinks.json"
  ],
  "sourceAttribution": "reported",
  "message": "200 response schema does not match 201 response schema. A PUT API must always return the same response schema for both the 200 and 201 status codes.",
  "path": [
    "definitions",
    "PrivateEndpointConnection"
  ]
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "ServerBackup.tsp",
  "line": 43,
  "column": 3
}
```

## specification/network/resource-manager/Microsoft.Network/Network/Network

Swagger raw: 170; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionMonitors_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1090,
        "column": 12
      },
      "end": {
        "line": 1183,
        "column": 43
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PacketCaptures_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 3: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionMonitors_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1090,
        "column": 12
      },
      "end": {
        "line": 1183,
        "column": 43
      }
    }
  }
}
```

### Swagger 4: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PacketCaptures_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 5: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'VipSwap_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14382,
        "column": 12
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 6: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'VipSwap_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14382,
        "column": 12
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 7: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionMonitors_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1090,
        "column": 12
      },
      "end": {
        "line": 1183,
        "column": 43
      }
    }
  }
}
```

### Swagger 8: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PacketCaptures_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 9: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'VipSwap_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14382,
        "column": 12
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 10: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionMonitors_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1090,
        "column": 12
      },
      "end": {
        "line": 1183,
        "column": 43
      }
    }
  }
}
```

### Swagger 11: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PacketCaptures_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 12: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'VipSwap_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14382,
        "column": 12
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 13: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'VipSwap_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14382,
        "column": 12
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 14: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionMonitors_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1090,
        "column": 12
      },
      "end": {
        "line": 1183,
        "column": 43
      }
    }
  }
}
```

### Swagger 15: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PacketCaptures_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 16: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionMonitors_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1090,
        "column": 12
      },
      "end": {
        "line": 1183,
        "column": 43
      }
    }
  }
}
```

### Swagger 17: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PacketCaptures_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 18: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'VipSwap_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14382,
        "column": 12
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 19: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'VipSwap_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14382,
        "column": 12
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 20: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionMonitors_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1090,
        "column": 12
      },
      "end": {
        "line": 1183,
        "column": 43
      }
    }
  }
}
```

### Swagger 21: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PacketCaptures_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 22: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'VipSwap_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14382,
        "column": 12
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 23: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "sourceDocuments": [
    "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionMonitors_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1090,
        "column": 12
      },
      "end": {
        "line": 1183,
        "column": 43
      }
    }
  }
}
```

### Swagger 24: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "sourceDocuments": [
    "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PacketCaptures_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 25: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'VipSwap_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14382,
        "column": 12
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 26: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionMonitors_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1090,
        "column": 12
      },
      "end": {
        "line": 1183,
        "column": 43
      }
    }
  }
}
```

### Swagger 27: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PacketCaptures_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 28: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionMonitors_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1090,
        "column": 12
      },
      "end": {
        "line": 1183,
        "column": 43
      }
    }
  }
}
```

### Swagger 29: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PacketCaptures_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 30: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'VipSwap_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14382,
        "column": 12
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 31: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [
    "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'VipSwap_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14382,
        "column": 12
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 32: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionMonitors_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1090,
        "column": 12
      },
      "end": {
        "line": 1183,
        "column": 43
      }
    }
  }
}
```

### Swagger 33: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PacketCaptures_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 34: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionMonitors_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1090,
        "column": 12
      },
      "end": {
        "line": 1183,
        "column": 43
      }
    }
  }
}
```

### Swagger 35: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PacketCaptures_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 36: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionMonitors_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1090,
        "column": 12
      },
      "end": {
        "line": 1183,
        "column": 43
      }
    }
  }
}
```

### Swagger 37: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PacketCaptures_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 38: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionMonitors_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1090,
        "column": 12
      },
      "end": {
        "line": 1183,
        "column": 43
      }
    }
  }
}
```

### Swagger 39: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PacketCaptures_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 40: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'VipSwap_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14382,
        "column": 12
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 41: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'VipSwap_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14382,
        "column": 12
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 42: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionMonitors_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1090,
        "column": 12
      },
      "end": {
        "line": 1183,
        "column": 43
      }
    }
  }
}
```

### Swagger 43: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PacketCaptures_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 44: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'VipSwap_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14382,
        "column": 12
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 45: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ConnectionMonitors_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1090,
        "column": 12
      },
      "end": {
        "line": 1183,
        "column": 43
      }
    }
  }
}
```

### Swagger 46: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'PacketCaptures_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 47: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'VipSwap_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 14382,
        "column": 12
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 48: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PacketCaptures_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 49: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 712,
        "column": 12
      },
      "end": {
        "line": 792,
        "column": 43
      }
    }
  }
}
```

### Swagger 50: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: NetworkVirtualApplianceConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1412,
        "column": 12
      },
      "end": {
        "line": 1488,
        "column": 43
      }
    }
  }
}
```

### Swagger 51: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: HubVirtualNetworkConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3494,
        "column": 12
      },
      "end": {
        "line": 3570,
        "column": 43
      }
    }
  }
}
```

### Swagger 52: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualHubRouteTableV2s_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 4357,
        "column": 12
      },
      "end": {
        "line": 4434,
        "column": 43
      }
    }
  }
}
```

### Swagger 53: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VpnConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 6097,
        "column": 12
      },
      "end": {
        "line": 6174,
        "column": 43
      }
    }
  }
}
```

### Swagger 54: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualNetworkGatewayConnections_SetSharedKey",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 563,
        "column": 12
      },
      "end": {
        "line": 636,
        "column": 43
      }
    }
  }
}
```

### Swagger 55: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PacketCaptures_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 56: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteCrossConnectionPeerings_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3507,
        "column": 12
      },
      "end": {
        "line": 3587,
        "column": 43
      }
    }
  }
}
```

### Swagger 57: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: RouteFilterRules_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 5909,
        "column": 12
      },
      "end": {
        "line": 5989,
        "column": 43
      }
    }
  }
}
```

### Swagger 58: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PrivateDnsZoneGroups_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10066,
        "column": 12
      },
      "end": {
        "line": 10146,
        "column": 43
      }
    }
  }
}
```

### Swagger 59: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [
    "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteCrossConnectionPeerings_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3507,
        "column": 12
      },
      "end": {
        "line": 3587,
        "column": 43
      }
    }
  }
}
```

### Swagger 60: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [
    "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: RouteFilterRules_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 5909,
        "column": 12
      },
      "end": {
        "line": 5989,
        "column": 43
      }
    }
  }
}
```

### Swagger 61: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PrivateDnsZoneGroups_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10066,
        "column": 12
      },
      "end": {
        "line": 10146,
        "column": 43
      }
    }
  }
}
```

### Swagger 62: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PacketCaptures_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 63: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PrivateDnsZoneGroups_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10066,
        "column": 12
      },
      "end": {
        "line": 10146,
        "column": 43
      }
    }
  }
}
```

### Swagger 64: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualNetworkGatewayConnections_SetSharedKey",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 563,
        "column": 12
      },
      "end": {
        "line": 636,
        "column": 43
      }
    }
  }
}
```

### Swagger 65: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PacketCaptures_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 66: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PrivateDnsZoneGroups_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10066,
        "column": 12
      },
      "end": {
        "line": 10146,
        "column": 43
      }
    }
  }
}
```

### Swagger 67: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 712,
        "column": 12
      },
      "end": {
        "line": 792,
        "column": 43
      }
    }
  }
}
```

### Swagger 68: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: NetworkVirtualApplianceConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1412,
        "column": 12
      },
      "end": {
        "line": 1488,
        "column": 43
      }
    }
  }
}
```

### Swagger 69: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: HubVirtualNetworkConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3494,
        "column": 12
      },
      "end": {
        "line": 3570,
        "column": 43
      }
    }
  }
}
```

### Swagger 70: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualHubRouteTableV2s_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 4357,
        "column": 12
      },
      "end": {
        "line": 4434,
        "column": 43
      }
    }
  }
}
```

### Swagger 71: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VpnConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 6097,
        "column": 12
      },
      "end": {
        "line": 6174,
        "column": 43
      }
    }
  }
}
```

### Swagger 72: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PrivateDnsZoneGroups_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10066,
        "column": 12
      },
      "end": {
        "line": 10146,
        "column": 43
      }
    }
  }
}
```

### Swagger 73: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PacketCaptures_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 74: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 712,
        "column": 12
      },
      "end": {
        "line": 792,
        "column": 43
      }
    }
  }
}
```

### Swagger 75: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: NetworkVirtualApplianceConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1412,
        "column": 12
      },
      "end": {
        "line": 1488,
        "column": 43
      }
    }
  }
}
```

### Swagger 76: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: HubVirtualNetworkConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3494,
        "column": 12
      },
      "end": {
        "line": 3570,
        "column": 43
      }
    }
  }
}
```

### Swagger 77: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualHubRouteTableV2s_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 4357,
        "column": 12
      },
      "end": {
        "line": 4434,
        "column": 43
      }
    }
  }
}
```

### Swagger 78: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VpnConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 6097,
        "column": 12
      },
      "end": {
        "line": 6174,
        "column": 43
      }
    }
  }
}
```

### Swagger 79: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualNetworkGatewayConnections_SetSharedKey",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 563,
        "column": 12
      },
      "end": {
        "line": 636,
        "column": 43
      }
    }
  }
}
```

### Swagger 80: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PacketCaptures_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 81: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteCrossConnectionPeerings_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3507,
        "column": 12
      },
      "end": {
        "line": 3587,
        "column": 43
      }
    }
  }
}
```

### Swagger 82: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: RouteFilterRules_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 5909,
        "column": 12
      },
      "end": {
        "line": 5989,
        "column": 43
      }
    }
  }
}
```

### Swagger 83: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PrivateDnsZoneGroups_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10066,
        "column": 12
      },
      "end": {
        "line": 10146,
        "column": 43
      }
    }
  }
}
```

### Swagger 84: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [
    "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualNetworkGatewayConnections_SetSharedKey",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 563,
        "column": 12
      },
      "end": {
        "line": 636,
        "column": 43
      }
    }
  }
}
```

### Swagger 85: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 712,
        "column": 12
      },
      "end": {
        "line": 792,
        "column": 43
      }
    }
  }
}
```

### Swagger 86: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: NetworkVirtualApplianceConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1412,
        "column": 12
      },
      "end": {
        "line": 1488,
        "column": 43
      }
    }
  }
}
```

### Swagger 87: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: HubVirtualNetworkConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3494,
        "column": 12
      },
      "end": {
        "line": 3570,
        "column": 43
      }
    }
  }
}
```

### Swagger 88: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualHubRouteTableV2s_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 4357,
        "column": 12
      },
      "end": {
        "line": 4434,
        "column": 43
      }
    }
  }
}
```

### Swagger 89: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VpnConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 6097,
        "column": 12
      },
      "end": {
        "line": 6174,
        "column": 43
      }
    }
  }
}
```

### Swagger 90: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteCrossConnectionPeerings_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3507,
        "column": 12
      },
      "end": {
        "line": 3587,
        "column": 43
      }
    }
  }
}
```

### Swagger 91: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: RouteFilterRules_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 5909,
        "column": 12
      },
      "end": {
        "line": 5989,
        "column": 43
      }
    }
  }
}
```

### Swagger 92: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PrivateDnsZoneGroups_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10066,
        "column": 12
      },
      "end": {
        "line": 10146,
        "column": 43
      }
    }
  }
}
```

### Swagger 93: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PacketCaptures_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 94: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 712,
        "column": 12
      },
      "end": {
        "line": 792,
        "column": 43
      }
    }
  }
}
```

### Swagger 95: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: NetworkVirtualApplianceConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1412,
        "column": 12
      },
      "end": {
        "line": 1488,
        "column": 43
      }
    }
  }
}
```

### Swagger 96: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: HubVirtualNetworkConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3494,
        "column": 12
      },
      "end": {
        "line": 3570,
        "column": 43
      }
    }
  }
}
```

### Swagger 97: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualHubRouteTableV2s_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 4357,
        "column": 12
      },
      "end": {
        "line": 4434,
        "column": 43
      }
    }
  }
}
```

### Swagger 98: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VpnConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 6097,
        "column": 12
      },
      "end": {
        "line": 6174,
        "column": 43
      }
    }
  }
}
```

### Swagger 99: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PrivateDnsZoneGroups_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10066,
        "column": 12
      },
      "end": {
        "line": 10146,
        "column": 43
      }
    }
  }
}
```

### Swagger 100: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "sourceDocuments": [
    "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PacketCaptures_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 101: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 712,
        "column": 12
      },
      "end": {
        "line": 792,
        "column": 43
      }
    }
  }
}
```

### Swagger 102: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: NetworkVirtualApplianceConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1412,
        "column": 12
      },
      "end": {
        "line": 1488,
        "column": 43
      }
    }
  }
}
```

### Swagger 103: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: HubVirtualNetworkConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3494,
        "column": 12
      },
      "end": {
        "line": 3570,
        "column": 43
      }
    }
  }
}
```

### Swagger 104: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualHubRouteTableV2s_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 4357,
        "column": 12
      },
      "end": {
        "line": 4434,
        "column": 43
      }
    }
  }
}
```

### Swagger 105: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VpnConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 6097,
        "column": 12
      },
      "end": {
        "line": 6174,
        "column": 43
      }
    }
  }
}
```

### Swagger 106: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualNetworkGatewayConnections_SetSharedKey",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 563,
        "column": 12
      },
      "end": {
        "line": 636,
        "column": 43
      }
    }
  }
}
```

### Swagger 107: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteCrossConnectionPeerings_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3507,
        "column": 12
      },
      "end": {
        "line": 3587,
        "column": 43
      }
    }
  }
}
```

### Swagger 108: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: RouteFilterRules_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 5909,
        "column": 12
      },
      "end": {
        "line": 5989,
        "column": 43
      }
    }
  }
}
```

### Swagger 109: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PrivateDnsZoneGroups_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10066,
        "column": 12
      },
      "end": {
        "line": 10146,
        "column": 43
      }
    }
  }
}
```

### Swagger 110: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PacketCaptures_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 111: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 712,
        "column": 12
      },
      "end": {
        "line": 792,
        "column": 43
      }
    }
  }
}
```

### Swagger 112: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: NetworkVirtualApplianceConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1412,
        "column": 12
      },
      "end": {
        "line": 1488,
        "column": 43
      }
    }
  }
}
```

### Swagger 113: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: HubVirtualNetworkConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3494,
        "column": 12
      },
      "end": {
        "line": 3570,
        "column": 43
      }
    }
  }
}
```

### Swagger 114: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualHubRouteTableV2s_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 4357,
        "column": 12
      },
      "end": {
        "line": 4434,
        "column": 43
      }
    }
  }
}
```

### Swagger 115: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VpnConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 6097,
        "column": 12
      },
      "end": {
        "line": 6174,
        "column": 43
      }
    }
  }
}
```

### Swagger 116: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualNetworkGatewayConnections_SetSharedKey",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 563,
        "column": 12
      },
      "end": {
        "line": 636,
        "column": 43
      }
    }
  }
}
```

### Swagger 117: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PacketCaptures_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 118: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteCrossConnectionPeerings_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3507,
        "column": 12
      },
      "end": {
        "line": 3587,
        "column": 43
      }
    }
  }
}
```

### Swagger 119: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: RouteFilterRules_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 5909,
        "column": 12
      },
      "end": {
        "line": 5989,
        "column": 43
      }
    }
  }
}
```

### Swagger 120: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PrivateDnsZoneGroups_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10066,
        "column": 12
      },
      "end": {
        "line": 10146,
        "column": 43
      }
    }
  }
}
```

### Swagger 121: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [
    "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PrivateDnsZoneGroups_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10066,
        "column": 12
      },
      "end": {
        "line": 10146,
        "column": 43
      }
    }
  }
}
```

### Swagger 122: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PacketCaptures_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 123: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 712,
        "column": 12
      },
      "end": {
        "line": 792,
        "column": 43
      }
    }
  }
}
```

### Swagger 124: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: NetworkVirtualApplianceConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1412,
        "column": 12
      },
      "end": {
        "line": 1488,
        "column": 43
      }
    }
  }
}
```

### Swagger 125: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: HubVirtualNetworkConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3494,
        "column": 12
      },
      "end": {
        "line": 3570,
        "column": 43
      }
    }
  }
}
```

### Swagger 126: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualHubRouteTableV2s_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 4357,
        "column": 12
      },
      "end": {
        "line": 4434,
        "column": 43
      }
    }
  }
}
```

### Swagger 127: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VpnConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 6097,
        "column": 12
      },
      "end": {
        "line": 6174,
        "column": 43
      }
    }
  }
}
```

### Swagger 128: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualNetworkGatewayConnections_SetSharedKey",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 563,
        "column": 12
      },
      "end": {
        "line": 636,
        "column": 43
      }
    }
  }
}
```

### Swagger 129: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PacketCaptures_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 130: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteCrossConnectionPeerings_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3507,
        "column": 12
      },
      "end": {
        "line": 3587,
        "column": 43
      }
    }
  }
}
```

### Swagger 131: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: RouteFilterRules_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 5909,
        "column": 12
      },
      "end": {
        "line": 5989,
        "column": 43
      }
    }
  }
}
```

### Swagger 132: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PacketCaptures_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 133: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 712,
        "column": 12
      },
      "end": {
        "line": 792,
        "column": 43
      }
    }
  }
}
```

### Swagger 134: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: NetworkVirtualApplianceConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1412,
        "column": 12
      },
      "end": {
        "line": 1488,
        "column": 43
      }
    }
  }
}
```

### Swagger 135: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: HubVirtualNetworkConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3494,
        "column": 12
      },
      "end": {
        "line": 3570,
        "column": 43
      }
    }
  }
}
```

### Swagger 136: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualHubRouteTableV2s_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 4357,
        "column": 12
      },
      "end": {
        "line": 4434,
        "column": 43
      }
    }
  }
}
```

### Swagger 137: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VpnConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 6097,
        "column": 12
      },
      "end": {
        "line": 6174,
        "column": 43
      }
    }
  }
}
```

### Swagger 138: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualNetworkGatewayConnections_SetSharedKey",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 563,
        "column": 12
      },
      "end": {
        "line": 636,
        "column": 43
      }
    }
  }
}
```

### Swagger 139: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PacketCaptures_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 140: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteCrossConnectionPeerings_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3507,
        "column": 12
      },
      "end": {
        "line": 3587,
        "column": 43
      }
    }
  }
}
```

### Swagger 141: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: RouteFilterRules_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 5909,
        "column": 12
      },
      "end": {
        "line": 5989,
        "column": 43
      }
    }
  }
}
```

### Swagger 142: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PrivateDnsZoneGroups_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10066,
        "column": 12
      },
      "end": {
        "line": 10146,
        "column": 43
      }
    }
  }
}
```

### Swagger 143: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [
    "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 712,
        "column": 12
      },
      "end": {
        "line": 792,
        "column": 43
      }
    }
  }
}
```

### Swagger 144: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [
    "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: NetworkVirtualApplianceConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1412,
        "column": 12
      },
      "end": {
        "line": 1488,
        "column": 43
      }
    }
  }
}
```

### Swagger 145: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [
    "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: HubVirtualNetworkConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3494,
        "column": 12
      },
      "end": {
        "line": 3570,
        "column": 43
      }
    }
  }
}
```

### Swagger 146: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [
    "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualHubRouteTableV2s_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeTables/{routeTableName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 4357,
        "column": 12
      },
      "end": {
        "line": 4434,
        "column": 43
      }
    }
  }
}
```

### Swagger 147: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [
    "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VpnConnections_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 6097,
        "column": 12
      },
      "end": {
        "line": 6174,
        "column": 43
      }
    }
  }
}
```

### Swagger 148: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: ExpressRouteCrossConnectionPeerings_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3507,
        "column": 12
      },
      "end": {
        "line": 3587,
        "column": 43
      }
    }
  }
}
```

### Swagger 149: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: RouteFilterRules_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 5909,
        "column": 12
      },
      "end": {
        "line": 5989,
        "column": 43
      }
    }
  }
}
```

### Swagger 150: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PrivateDnsZoneGroups_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10066,
        "column": 12
      },
      "end": {
        "line": 10146,
        "column": 43
      }
    }
  }
}
```

### Swagger 151: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PacketCaptures_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 152: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PrivateDnsZoneGroups_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10066,
        "column": 12
      },
      "end": {
        "line": 10146,
        "column": 43
      }
    }
  }
}
```

### Swagger 153: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VirtualNetworkGatewayConnections_SetSharedKey",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 563,
        "column": 12
      },
      "end": {
        "line": 636,
        "column": 43
      }
    }
  }
}
```

### Swagger 154: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PacketCaptures_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2099,
        "column": 12
      },
      "end": {
        "line": 2173,
        "column": 43
      }
    }
  }
}
```

### Swagger 155: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: PrivateDnsZoneGroups_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10066,
        "column": 12
      },
      "end": {
        "line": 10146,
        "column": 43
      }
    }
  }
}
```

### Swagger 156: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/applicationGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 14320,
        "column": 188
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 157: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 14320,
        "column": 188
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 158: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 14320,
        "column": 188
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 159: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 14320,
        "column": 188
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 160: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/expressRoute.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 14320,
        "column": 188
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 161: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/loadBalancer.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 14320,
        "column": 188
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 162: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 14320,
        "column": 188
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 163: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 14320,
        "column": 188
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 164: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/networkWatcher.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 14320,
        "column": 188
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 165: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/serviceGateway.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 14320,
        "column": 188
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 166: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json",
  "sourceDocuments": [
    "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 14320,
        "column": 188
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 167: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetworkAppliance.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 14320,
        "column": 188
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 168: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 14320,
        "column": 188
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 169: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 14320,
        "column": 188
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

### Swagger 170: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/network/resource-manager/Microsoft.Network/Network/Network",
  "swaggerFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "validatorInputFile": "projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualWan.json",
  "sourceDocuments": [],
  "sourceAttribution": "input-fallback",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 14320,
        "column": 188
      },
      "end": {
        "line": 14465,
        "column": 43
      }
    }
  }
}
```

## specification/nginx/resource-manager/Nginx.NginxPlus/NginxPlus

Swagger raw: 2; TypeSpec raw: 2; source-aligned: 2; default: 2.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/nginx/resource-manager/Nginx.NginxPlus/NginxPlus",
  "swaggerFile": "projects/specification/nginx/resource-manager/Nginx.NginxPlus/NginxPlus/swagger/stable/2025-11-01/swagger.json",
  "validatorInputFile": "projects/specification/nginx/resource-manager/Nginx.NginxPlus/NginxPlus/swagger/stable/2025-11-01/swagger.json",
  "sourceDocuments": [
    "projects/specification/nginx/resource-manager/Nginx.NginxPlus/NginxPlus/swagger/stable/2025-11-01/swagger.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ApiKeys_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Nginx.NginxPlus/nginxDeployments/{deploymentName}/apiKeys/{apiKeyName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Nginx.NginxPlus/nginxDeployments/{deploymentName}/apiKeys/{apiKeyName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 544,
        "column": 12
      },
      "end": {
        "line": 608,
        "column": 60
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/nginx/resource-manager/Nginx.NginxPlus/NginxPlus",
  "swaggerFile": "projects/specification/nginx/resource-manager/Nginx.NginxPlus/NginxPlus/swagger/stable/2025-11-01/swagger.json",
  "validatorInputFile": "projects/specification/nginx/resource-manager/Nginx.NginxPlus/NginxPlus/swagger/stable/2025-11-01/swagger.json",
  "sourceDocuments": [
    "projects/specification/nginx/resource-manager/Nginx.NginxPlus/NginxPlus/swagger/stable/2025-11-01/swagger.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Configurations_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Nginx.NginxPlus/nginxDeployments/{deploymentName}/configurations/{configurationName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Nginx.NginxPlus/nginxDeployments/{deploymentName}/configurations/{configurationName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1027,
        "column": 12
      },
      "end": {
        "line": 1109,
        "column": 43
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Nginx.NginxPlus.NginxDeploymentApiKeyResponse. Found Nginx.NginxPlus.NginxDeploymentApiKeyRequest.",
  "sourceFile": "NginxDeploymentApiKeyResponse.tsp",
  "line": 38,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Nginx.NginxPlus.NginxConfigurationResponse. Found Nginx.NginxPlus.NginxConfigurationRequest.",
  "sourceFile": "NginxConfigurationResponse.tsp",
  "line": 38,
  "column": 3
}
```

## specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights

Swagger raw: 1; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights",
  "swaggerFile": "projects/specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights/swagger/stable/2026-03-01/openapi.json",
  "validatorInputFile": "projects/specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights/swagger/stable/2026-03-01/openapi.json",
  "sourceDocuments": [
    "projects/specification/operationalinsights/resource-manager/Microsoft.OperationalInsights/OperationalInsights/swagger/stable/2026-03-01/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 742,
        "column": 124
      },
      "end": {
        "line": 822,
        "column": 59
      }
    }
  }
}
```

## specification/portal/resource-manager/Microsoft.Portal/Portal

Swagger raw: 2; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: ConsistentResponseSchemaForPut

```json
{
  "rule": "ConsistentResponseSchemaForPut",
  "level": "error",
  "project": "specification/portal/resource-manager/Microsoft.Portal/Portal",
  "swaggerFile": "projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/common.json",
  "validatorInputFile": "projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/portal.json",
  "sourceDocuments": [
    "projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/common.json"
  ],
  "sourceAttribution": "reported",
  "message": "200 response schema does not match 201 response schema. A PUT API must always return the same response schema for both the 200 and 201 status codes.",
  "path": [
    "definitions",
    "Dashboard"
  ]
}
```

### Swagger 2: ConsistentResponseSchemaForPut

```json
{
  "rule": "ConsistentResponseSchemaForPut",
  "level": "error",
  "project": "specification/portal/resource-manager/Microsoft.Portal/Portal",
  "swaggerFile": "projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/common.json",
  "validatorInputFile": "projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/tenantConfiguration.json",
  "sourceDocuments": [
    "projects/specification/portal/resource-manager/Microsoft.Portal/Portal/swagger/stable/2026-04-01/common.json"
  ],
  "sourceAttribution": "reported",
  "message": "200 response schema does not match 201 response schema. A PUT API must always return the same response schema for both the 200 and 201 status codes.",
  "path": [
    "definitions",
    "Configuration"
  ]
}
```

## specification/postgresql/DBforPostgreSQL.Management

Swagger raw: 9; TypeSpec raw: 4; source-aligned: 4; default: 4.

### Swagger 1: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/postgresql/DBforPostgreSQL.Management",
  "swaggerFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 476,
        "column": 138
      },
      "end": {
        "line": 803,
        "column": 43
      }
    }
  }
}
```

### Swagger 2: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/postgresql/DBforPostgreSQL.Management",
  "swaggerFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/administrators/{objectId} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/administrators/{objectId}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/administrators/{objectId}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 858,
        "column": 164
      },
      "end": {
        "line": 1066,
        "column": 43
      }
    }
  }
}
```

### Swagger 3: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/postgresql/DBforPostgreSQL.Management",
  "swaggerFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/advancedThreatProtectionSettings/{threatProtectionName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/advancedThreatProtectionSettings/{threatProtectionName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/advancedThreatProtectionSettings/{threatProtectionName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1121,
        "column": 194
      },
      "end": {
        "line": 1283,
        "column": 43
      }
    }
  }
}
```

### Swagger 4: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/postgresql/DBforPostgreSQL.Management",
  "swaggerFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/backups/{backupName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/backups/{backupName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/backups/{backupName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1338,
        "column": 159
      },
      "end": {
        "line": 1546,
        "column": 43
      }
    }
  }
}
```

### Swagger 5: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/postgresql/DBforPostgreSQL.Management",
  "swaggerFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/configurations/{configurationName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/configurations/{configurationName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/configurations/{configurationName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1712,
        "column": 173
      },
      "end": {
        "line": 1936,
        "column": 43
      }
    }
  }
}
```

### Swagger 6: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/postgresql/DBforPostgreSQL.Management",
  "swaggerFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/databases/{databaseName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/databases/{databaseName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/databases/{databaseName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 1991,
        "column": 163
      },
      "end": {
        "line": 2208,
        "column": 43
      }
    }
  }
}
```

### Swagger 7: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/postgresql/DBforPostgreSQL.Management",
  "swaggerFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/firewallRules/{firewallRuleName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/firewallRules/{firewallRuleName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/firewallRules/{firewallRuleName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2444,
        "column": 171
      },
      "end": {
        "line": 2661,
        "column": 43
      }
    }
  }
}
```

### Swagger 8: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/postgresql/DBforPostgreSQL.Management",
  "swaggerFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/privateEndpointConnections/{privateEndpointConnectionName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/privateEndpointConnections/{privateEndpointConnectionName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/privateEndpointConnections/{privateEndpointConnectionName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 3813,
        "column": 197
      },
      "end": {
        "line": 4009,
        "column": 43
      }
    }
  }
}
```

### Swagger 9: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/postgresql/DBforPostgreSQL.Management",
  "swaggerFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/postgresql/DBforPostgreSQL.Management/swagger/resource-manager/Microsoft.DBforPostgreSQL/preview/2026-07-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/virtualendpoints/{virtualEndpointName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/virtualendpoints/{virtualEndpointName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{serverName}/virtualendpoints/{virtualEndpointName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 4886,
        "column": 177
      },
      "end": {
        "line": 5187,
        "column": 43
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DBforPostgreSQL.AdministratorMicrosoftEntra. Found Microsoft.DBforPostgreSQL.AdministratorMicrosoftEntraAdd.",
  "sourceFile": "AdministratorMicrosoftEntra.tsp",
  "line": 43,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "BackupAutomaticAndOnDemand.tsp",
  "line": 41,
  "column": 3
}
```

### TypeSpec 3

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DBforPostgreSQL.Configuration. Found Microsoft.DBforPostgreSQL.ConfigurationForUpdate.",
  "sourceFile": "Configuration.tsp",
  "line": 43,
  "column": 3
}
```

### TypeSpec 4

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.DBforPostgreSQL.DbAgent. Found Microsoft.DBforPostgreSQL.DbAgentForUpdate.",
  "sourceFile": "routes.tsp",
  "line": 184,
  "column": 3
}
```

## specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc

Swagger raw: 1; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: ConsistentResponseSchemaForPut

```json
{
  "rule": "ConsistentResponseSchemaForPut",
  "level": "error",
  "project": "specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc",
  "swaggerFile": "common-types/resource-management/v4/privatelinks.json",
  "validatorInputFile": "projects/specification/postgresqlhsc/resource-manager/Microsoft.DBforPostgreSQL/PostgresqlHsc/swagger/preview/2023-03-02-preview/postgresqlhsc.json",
  "sourceDocuments": [
    "common-types/resource-management/v4/privatelinks.json"
  ],
  "sourceAttribution": "reported",
  "message": "200 response schema does not match 201 response schema. A PUT API must always return the same response schema for both the 200 and 201 status codes.",
  "path": [
    "definitions",
    "PrivateEndpointConnection"
  ]
}
```

## specification/quota/resource-manager/Microsoft.Quota/Quota

Swagger raw: 0; TypeSpec raw: 1; source-aligned: 1; default: 1.

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "GroupQuotaSubscriptionId.tsp",
  "line": 81,
  "column": 3
}
```

## specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices

Swagger raw: 2; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices",
  "swaggerFile": "projects/specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices/swagger/preview/2026-08-31-preview/openapi.json",
  "validatorInputFile": "projects/specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices/swagger/preview/2026-08-31-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices/swagger/preview/2026-08-31-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'VaultCertificates_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/certificates/{certificateName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/certificates/{certificateName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 810,
        "column": 12
      },
      "end": {
        "line": 866,
        "column": 50
      }
    }
  }
}
```

### Swagger 2: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices",
  "swaggerFile": "projects/specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices/swagger/preview/2026-08-31-preview/openapi.json",
  "validatorInputFile": "projects/specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices/swagger/preview/2026-08-31-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/RecoveryServices/swagger/preview/2026-08-31-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: VaultCertificates_Create",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/certificates/{certificateName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/certificates/{certificateName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 810,
        "column": 12
      },
      "end": {
        "line": 866,
        "column": 50
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RecoveryServices.Vault. Found Microsoft.RecoveryServices.CertificateRequest.",
  "sourceFile": "Vault.tsp",
  "line": 215,
  "column": 3
}
```

## specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup

Swagger raw: 3; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup",
  "swaggerFile": "projects/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/swagger/stable/2026-10-01/bms.json",
  "validatorInputFile": "projects/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/swagger/stable/2026-10-01/bms.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/swagger/stable/2026-10-01/bms.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'BackupResourceEncryptionConfigs_Update' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupEncryptionConfigs/backupResourceEncryptionConfig",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupEncryptionConfigs/backupResourceEncryptionConfig",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 508,
        "column": 12
      },
      "end": {
        "line": 554,
        "column": 72
      }
    }
  }
}
```

### Swagger 2: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup",
  "swaggerFile": "projects/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/swagger/stable/2026-10-01/bms.json",
  "validatorInputFile": "projects/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/swagger/stable/2026-10-01/bms.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/swagger/stable/2026-10-01/bms.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupEncryptionConfigs/backupResourceEncryptionConfig has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupEncryptionConfigs/backupResourceEncryptionConfig"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupEncryptionConfigs/backupResourceEncryptionConfig"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 463,
        "column": 184
      },
      "end": {
        "line": 554,
        "column": 72
      }
    }
  }
}
```

### Swagger 3: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup",
  "swaggerFile": "projects/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/swagger/stable/2026-10-01/bms.json",
  "validatorInputFile": "projects/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/swagger/stable/2026-10-01/bms.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/RecoveryServicesBackup/swagger/stable/2026-10-01/bms.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupstorageconfig/vaultstorageconfig has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupstorageconfig/vaultstorageconfig"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupstorageconfig/vaultstorageconfig"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 5070,
        "column": 168
      },
      "end": {
        "line": 5214,
        "column": 70
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RecoveryServices.BackupResourceEncryptionConfigExtendedResource. Found Microsoft.RecoveryServices.BackupResourceEncryptionConfigResource.",
  "sourceFile": "BackupResourceEncryptionConfigExtendedResource.tsp",
  "line": 74,
  "column": 3
}
```

## specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery

Swagger raw: 14; TypeSpec raw: 14; source-aligned: 14; default: 14.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery",
  "swaggerFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "validatorInputFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ReplicationAlertSettings_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationAlertSettings/{alertSettingName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationAlertSettings/{alertSettingName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 339,
        "column": 12
      },
      "end": {
        "line": 390,
        "column": 69
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery",
  "swaggerFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "validatorInputFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ReplicationFabrics_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 643,
        "column": 12
      },
      "end": {
        "line": 715,
        "column": 43
      }
    }
  }
}
```

### Swagger 3: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery",
  "swaggerFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "validatorInputFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ReplicationNetworkMappings_Create' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationNetworks/{networkName}/replicationNetworkMappings/{networkMappingName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationNetworks/{networkName}/replicationNetworkMappings/{networkMappingName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1523,
        "column": 12
      },
      "end": {
        "line": 1609,
        "column": 43
      }
    }
  }
}
```

### Swagger 4: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery",
  "swaggerFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "validatorInputFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ReplicationProtectionContainers_Create' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1880,
        "column": 12
      },
      "end": {
        "line": 1959,
        "column": 43
      }
    }
  }
}
```

### Swagger 5: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery",
  "swaggerFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "validatorInputFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ReplicationMigrationItems_Create' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationMigrationItems/{migrationItemName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationMigrationItems/{migrationItemName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2255,
        "column": 12
      },
      "end": {
        "line": 2341,
        "column": 43
      }
    }
  }
}
```

### Swagger 6: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery",
  "swaggerFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "validatorInputFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ReplicationProtectedItems_Create' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 3448,
        "column": 12
      },
      "end": {
        "line": 3534,
        "column": 43
      }
    }
  }
}
```

### Swagger 7: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery",
  "swaggerFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "validatorInputFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ReplicationProtectionContainerMappings_Create' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectionContainerMappings/{mappingName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectionContainerMappings/{mappingName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 6698,
        "column": 12
      },
      "end": {
        "line": 6784,
        "column": 43
      }
    }
  }
}
```

### Swagger 8: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery",
  "swaggerFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "validatorInputFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ReplicationRecoveryServicesProviders_Create' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationRecoveryServicesProviders/{providerName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationRecoveryServicesProviders/{providerName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 7324,
        "column": 12
      },
      "end": {
        "line": 7403,
        "column": 43
      }
    }
  }
}
```

### Swagger 9: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery",
  "swaggerFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "validatorInputFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ReplicationStorageClassificationMappings_Create' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationStorageClassifications/{storageClassificationName}/replicationStorageClassificationMappings/{storageClassificationMappingName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationStorageClassifications/{storageClassificationName}/replicationStorageClassificationMappings/{storageClassificationMappingName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 7843,
        "column": 12
      },
      "end": {
        "line": 7929,
        "column": 43
      }
    }
  }
}
```

### Swagger 10: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery",
  "swaggerFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "validatorInputFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ReplicationvCenters_Create' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationvCenters/{vcenterName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationvCenters/{vcenterName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 8112,
        "column": 12
      },
      "end": {
        "line": 8191,
        "column": 43
      }
    }
  }
}
```

### Swagger 11: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery",
  "swaggerFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "validatorInputFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ReplicationPolicies_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationPolicies/{policyName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationPolicies/{policyName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 8965,
        "column": 12
      },
      "end": {
        "line": 9037,
        "column": 43
      }
    }
  }
}
```

### Swagger 12: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery",
  "swaggerFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "validatorInputFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ReplicationProtectionIntents_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationProtectionIntents/{intentObjectName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationProtectionIntents/{intentObjectName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 9491,
        "column": 12
      },
      "end": {
        "line": 9542,
        "column": 73
      }
    }
  }
}
```

### Swagger 13: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery",
  "swaggerFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "validatorInputFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ReplicationRecoveryPlans_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 9638,
        "column": 12
      },
      "end": {
        "line": 9710,
        "column": 43
      }
    }
  }
}
```

### Swagger 14: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery",
  "swaggerFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "validatorInputFile": "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json",
  "sourceDocuments": [
    "projects/specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/SiteRecovery/swagger/preview/2026-08-31-preview/service.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ReplicationVaultSetting_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationVaultSettings/{vaultSettingName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationVaultSettings/{vaultSettingName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 10725,
        "column": 12
      },
      "end": {
        "line": 10794,
        "column": 43
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RecoveryServices.Alert. Found Microsoft.RecoveryServices.ConfigureAlertRequest.",
  "sourceFile": "Alert.tsp",
  "line": 47,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RecoveryServices.Fabric. Found Microsoft.RecoveryServices.FabricCreationInput.",
  "sourceFile": "Fabric.tsp",
  "line": 87,
  "column": 3
}
```

### TypeSpec 3

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RecoveryServices.NetworkMapping. Found Microsoft.RecoveryServices.CreateNetworkMappingInput.",
  "sourceFile": "NetworkMapping.tsp",
  "line": 48,
  "column": 3
}
```

### TypeSpec 4

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RecoveryServices.ProtectionContainer. Found Microsoft.RecoveryServices.CreateProtectionContainerInput.",
  "sourceFile": "ProtectionContainer.tsp",
  "line": 90,
  "column": 3
}
```

### TypeSpec 5

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RecoveryServices.MigrationItem. Found Microsoft.RecoveryServices.EnableMigrationInput.",
  "sourceFile": "MigrationItem.tsp",
  "line": 51,
  "column": 3
}
```

### TypeSpec 6

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RecoveryServices.ReplicationProtectedItem. Found Microsoft.RecoveryServices.EnableProtectionInput.",
  "sourceFile": "ReplicationProtectedItem.tsp",
  "line": 95,
  "column": 3
}
```

### TypeSpec 7

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RecoveryServices.ProtectionContainerMapping. Found Microsoft.RecoveryServices.CreateProtectionContainerMappingInput.",
  "sourceFile": "ProtectionContainerMapping.tsp",
  "line": 48,
  "column": 3
}
```

### TypeSpec 8

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RecoveryServices.RecoveryServicesProvider. Found Microsoft.RecoveryServices.AddRecoveryServicesProviderInput.",
  "sourceFile": "RecoveryServicesProvider.tsp",
  "line": 58,
  "column": 3
}
```

### TypeSpec 9

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RecoveryServices.StorageClassificationMapping. Found Microsoft.RecoveryServices.StorageClassificationMappingInput.",
  "sourceFile": "StorageClassificationMapping.tsp",
  "line": 48,
  "column": 3
}
```

### TypeSpec 10

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RecoveryServices.VCenter. Found Microsoft.RecoveryServices.AddVCenterRequest.",
  "sourceFile": "VCenter.tsp",
  "line": 49,
  "column": 3
}
```

### TypeSpec 11

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RecoveryServices.Policy. Found Microsoft.RecoveryServices.CreatePolicyInput.",
  "sourceFile": "Policy.tsp",
  "line": 46,
  "column": 3
}
```

### TypeSpec 12

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RecoveryServices.ReplicationProtectionIntent. Found Microsoft.RecoveryServices.CreateProtectionIntentInput.",
  "sourceFile": "ReplicationProtectionIntent.tsp",
  "line": 47,
  "column": 3
}
```

### TypeSpec 13

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RecoveryServices.RecoveryPlan. Found Microsoft.RecoveryServices.CreateRecoveryPlanInput.",
  "sourceFile": "RecoveryPlan.tsp",
  "line": 50,
  "column": 3
}
```

### TypeSpec 14

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.RecoveryServices.VaultSetting. Found Microsoft.RecoveryServices.VaultSettingCreationInput.",
  "sourceFile": "VaultSetting.tsp",
  "line": 65,
  "column": 3
}
```

## specification/redis/resource-manager/Microsoft.Cache/Redis

Swagger raw: 3; TypeSpec raw: 2; source-aligned: 2; default: 2.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/redis/resource-manager/Microsoft.Cache/Redis",
  "swaggerFile": "projects/specification/redis/resource-manager/Microsoft.Cache/Redis/swagger/preview/2025-08-01-preview/redis.json",
  "validatorInputFile": "projects/specification/redis/resource-manager/Microsoft.Cache/Redis/swagger/preview/2025-08-01-preview/redis.json",
  "sourceDocuments": [
    "projects/specification/redis/resource-manager/Microsoft.Cache/Redis/swagger/preview/2025-08-01-preview/redis.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Redis_Create' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/redis/{name}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/redis/{name}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 316,
        "column": 12
      },
      "end": {
        "line": 399,
        "column": 43
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/redis/resource-manager/Microsoft.Cache/Redis",
  "swaggerFile": "projects/specification/redis/resource-manager/Microsoft.Cache/Redis/swagger/preview/2025-08-01-preview/redis.json",
  "validatorInputFile": "projects/specification/redis/resource-manager/Microsoft.Cache/Redis/swagger/preview/2025-08-01-preview/redis.json",
  "sourceDocuments": [
    "projects/specification/redis/resource-manager/Microsoft.Cache/Redis/swagger/preview/2025-08-01-preview/redis.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'LinkedServer_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/redis/{name}/linkedServers/{linkedServerName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/redis/{name}/linkedServers/{linkedServerName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1668,
        "column": 12
      },
      "end": {
        "line": 1743,
        "column": 43
      }
    }
  }
}
```

### Swagger 3: ConsistentResponseSchemaForPut

```json
{
  "rule": "ConsistentResponseSchemaForPut",
  "level": "error",
  "project": "specification/redis/resource-manager/Microsoft.Cache/Redis",
  "swaggerFile": "common-types/resource-management/v4/privatelinks.json",
  "validatorInputFile": "projects/specification/redis/resource-manager/Microsoft.Cache/Redis/swagger/preview/2025-08-01-preview/redis.json",
  "sourceDocuments": [
    "common-types/resource-management/v4/privatelinks.json"
  ],
  "sourceAttribution": "reported",
  "message": "200 response schema does not match 201 response schema. A PUT API must always return the same response schema for both the 200 and 201 status codes.",
  "path": [
    "definitions",
    "PrivateEndpointConnection"
  ]
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Cache.RedisResource. Found Microsoft.Cache.RedisCreateParameters.",
  "sourceFile": "RedisResource.tsp",
  "line": 60,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Cache.RedisLinkedServerWithProperties. Found Microsoft.Cache.RedisLinkedServerCreateParameters.",
  "sourceFile": "RedisLinkedServerWithProperties.tsp",
  "line": 63,
  "column": 3
}
```

## specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota

Swagger raw: 1; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: ConsistentResponseSchemaForPut

```json
{
  "rule": "ConsistentResponseSchemaForPut",
  "level": "error",
  "project": "specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota",
  "swaggerFile": "projects/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/swagger/stable/2020-10-25/quota.json",
  "validatorInputFile": "projects/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/swagger/stable/2020-10-25/quota.json",
  "sourceDocuments": [
    "projects/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Quota/swagger/stable/2020-10-25/quota.json"
  ],
  "sourceAttribution": "reported",
  "message": "200 response schema does not match 201 response schema. A PUT API must always return the same response schema for both the 200 and 201 status codes.",
  "path": [
    "definitions",
    "CurrentQuotaLimitBase"
  ]
}
```

## specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Reservations

Swagger raw: 1; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Reservations",
  "swaggerFile": "projects/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Reservations/swagger/stable/2022-11-01/reservations.json",
  "validatorInputFile": "projects/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Reservations/swagger/stable/2022-11-01/reservations.json",
  "sourceDocuments": [
    "projects/specification/reservations/resource-manager/Microsoft.Capacity/Reservations/Reservations/swagger/stable/2022-11-01/reservations.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ReservationOrder_Purchase' Request Model: 'parameters[2].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 393,
        "column": 12
      },
      "end": {
        "line": 461,
        "column": 43
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Reservations.ReservationOrderResponse. Found Reservations.PurchaseRequest.",
  "sourceFile": "ReservationOrderResponse.tsp",
  "line": 58,
  "column": 3
}
```

## specification/resources/resource-manager/Microsoft.Resources/deployments

Swagger raw: 5; TypeSpec raw: 5; source-aligned: 5; default: 5.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/resources/resource-manager/Microsoft.Resources/deployments",
  "swaggerFile": "projects/specification/resources/resource-manager/Microsoft.Resources/deployments/swagger/stable/2026-06-01/deployments.json",
  "validatorInputFile": "projects/specification/resources/resource-manager/Microsoft.Resources/deployments/swagger/stable/2026-06-01/deployments.json",
  "sourceDocuments": [
    "projects/specification/resources/resource-manager/Microsoft.Resources/deployments/swagger/stable/2026-06-01/deployments.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Deployments_CreateOrUpdateAtScope' Request Model: 'parameters[3].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/{scope}/providers/Microsoft.Resources/deployments/{deploymentName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/{scope}/providers/Microsoft.Resources/deployments/{deploymentName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 149,
        "column": 12
      },
      "end": {
        "line": 228,
        "column": 43
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/resources/resource-manager/Microsoft.Resources/deployments",
  "swaggerFile": "projects/specification/resources/resource-manager/Microsoft.Resources/deployments/swagger/stable/2026-06-01/deployments.json",
  "validatorInputFile": "projects/specification/resources/resource-manager/Microsoft.Resources/deployments/swagger/stable/2026-06-01/deployments.json",
  "sourceDocuments": [
    "projects/specification/resources/resource-manager/Microsoft.Resources/deployments/swagger/stable/2026-06-01/deployments.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Deployments_CreateOrUpdateAtManagementGroupScope' Request Model: 'parameters[3].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 721,
        "column": 12
      },
      "end": {
        "line": 801,
        "column": 43
      }
    }
  }
}
```

### Swagger 3: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/resources/resource-manager/Microsoft.Resources/deployments",
  "swaggerFile": "projects/specification/resources/resource-manager/Microsoft.Resources/deployments/swagger/stable/2026-06-01/deployments.json",
  "validatorInputFile": "projects/specification/resources/resource-manager/Microsoft.Resources/deployments/swagger/stable/2026-06-01/deployments.json",
  "sourceDocuments": [
    "projects/specification/resources/resource-manager/Microsoft.Resources/deployments/swagger/stable/2026-06-01/deployments.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Deployments_CreateOrUpdateAtTenantScope' Request Model: 'parameters[2].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/providers/Microsoft.Resources/deployments/{deploymentName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/providers/Microsoft.Resources/deployments/{deploymentName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1403,
        "column": 12
      },
      "end": {
        "line": 1474,
        "column": 43
      }
    }
  }
}
```

### Swagger 4: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/resources/resource-manager/Microsoft.Resources/deployments",
  "swaggerFile": "projects/specification/resources/resource-manager/Microsoft.Resources/deployments/swagger/stable/2026-06-01/deployments.json",
  "validatorInputFile": "projects/specification/resources/resource-manager/Microsoft.Resources/deployments/swagger/stable/2026-06-01/deployments.json",
  "sourceDocuments": [
    "projects/specification/resources/resource-manager/Microsoft.Resources/deployments/swagger/stable/2026-06-01/deployments.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Deployments_CreateOrUpdateAtSubscriptionScope' Request Model: 'parameters[3].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1970,
        "column": 12
      },
      "end": {
        "line": 2044,
        "column": 43
      }
    }
  }
}
```

### Swagger 5: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/resources/resource-manager/Microsoft.Resources/deployments",
  "swaggerFile": "projects/specification/resources/resource-manager/Microsoft.Resources/deployments/swagger/stable/2026-06-01/deployments.json",
  "validatorInputFile": "projects/specification/resources/resource-manager/Microsoft.Resources/deployments/swagger/stable/2026-06-01/deployments.json",
  "sourceDocuments": [
    "projects/specification/resources/resource-manager/Microsoft.Resources/deployments/swagger/stable/2026-06-01/deployments.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Deployments_CreateOrUpdate' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 2684,
        "column": 12
      },
      "end": {
        "line": 2777,
        "column": 43
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Resources.DeploymentExtended. Found Microsoft.Resources.Deployment.",
  "sourceFile": "DeploymentExtended.tsp",
  "line": 85,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Resources.DeploymentExtended. Found Microsoft.Resources.ScopedDeployment.",
  "sourceFile": "DeploymentExtended.tsp",
  "line": 264,
  "column": 3
}
```

### TypeSpec 3

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Resources.DeploymentExtended. Found Microsoft.Resources.ScopedDeployment.",
  "sourceFile": "DeploymentExtended.tsp",
  "line": 462,
  "column": 3
}
```

### TypeSpec 4

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Resources.DeploymentExtended. Found Microsoft.Resources.Deployment.",
  "sourceFile": "DeploymentExtended.tsp",
  "line": 654,
  "column": 3
}
```

### TypeSpec 5

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Resources.DeploymentExtended. Found Microsoft.Resources.Deployment.",
  "sourceFile": "DeploymentExtended.tsp",
  "line": 846,
  "column": 3
}
```

## specification/resources/resource-manager/Microsoft.Resources/resources

Swagger raw: 2; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/resources/resource-manager/Microsoft.Resources/resources",
  "swaggerFile": "projects/specification/resources/resource-manager/Microsoft.Resources/resources/swagger/stable/2025-04-01/resources.json",
  "validatorInputFile": "projects/specification/resources/resource-manager/Microsoft.Resources/resources/swagger/stable/2025-04-01/resources.json",
  "sourceDocuments": [
    "projects/specification/resources/resource-manager/Microsoft.Resources/resources/swagger/stable/2025-04-01/resources.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: Tags_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/tagNames/{tagName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/tagNames/{tagName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2139,
        "column": 12
      },
      "end": {
        "line": 2177,
        "column": 48
      }
    }
  }
}
```

### Swagger 2: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/resources/resource-manager/Microsoft.Resources/resources",
  "swaggerFile": "projects/specification/resources/resource-manager/Microsoft.Resources/resources/swagger/stable/2025-04-01/resources.json",
  "validatorInputFile": "projects/specification/resources/resource-manager/Microsoft.Resources/resources/swagger/stable/2025-04-01/resources.json",
  "sourceDocuments": [
    "projects/specification/resources/resource-manager/Microsoft.Resources/resources/swagger/stable/2025-04-01/resources.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: Tags_CreateOrUpdateValue",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/tagNames/{tagName}/tagValues/{tagValue}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/tagNames/{tagName}/tagValues/{tagValue}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 2221,
        "column": 12
      },
      "end": {
        "line": 2266,
        "column": 48
      }
    }
  }
}
```

## specification/security/resource-manager/Microsoft.Security/Security/ApiCollectionsAPI

Swagger raw: 0; TypeSpec raw: 1; source-aligned: 1; default: 1.

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "ApiCollection.tsp",
  "line": 61,
  "column": 3
}
```

## specification/security/resource-manager/Microsoft.Security/Security/AssessmentAPI

Swagger raw: 1; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/security/resource-manager/Microsoft.Security/Security/AssessmentAPI",
  "swaggerFile": "projects/specification/security/resource-manager/Microsoft.Security/Security/AssessmentAPI/swagger/stable/2025-05-04/security-Assessment.json",
  "validatorInputFile": "projects/specification/security/resource-manager/Microsoft.Security/Security/AssessmentAPI/swagger/stable/2025-05-04/security-Assessment.json",
  "sourceDocuments": [
    "projects/specification/security/resource-manager/Microsoft.Security/Security/AssessmentAPI/swagger/stable/2025-05-04/security-Assessment.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Assessments_CreateOrUpdate' Request Model: 'parameters[3].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/{resourceId}/providers/Microsoft.Security/assessments/{assessmentName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/{resourceId}/providers/Microsoft.Security/assessments/{assessmentName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 171,
        "column": 12
      },
      "end": {
        "line": 228,
        "column": 71
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model AssessmentAPI.SecurityAssessmentResponse. Found AssessmentAPI.SecurityAssessment.",
  "sourceFile": "SecurityAssessmentResponse.tsp",
  "line": 56,
  "column": 3
}
```

## specification/security/resource-manager/Microsoft.Security/Security/PrivateLinksAPI

Swagger raw: 1; TypeSpec raw: 0; source-aligned: 0; default: 0.

### Swagger 1: ConsistentResponseSchemaForPut

```json
{
  "rule": "ConsistentResponseSchemaForPut",
  "level": "error",
  "project": "specification/security/resource-manager/Microsoft.Security/Security/PrivateLinksAPI",
  "swaggerFile": "common-types/resource-management/v5/privatelinks.json",
  "validatorInputFile": "projects/specification/security/resource-manager/Microsoft.Security/Security/PrivateLinksAPI/swagger/stable/2026-01-01/privateLinks.json",
  "sourceDocuments": [
    "common-types/resource-management/v5/privatelinks.json"
  ],
  "sourceAttribution": "reported",
  "message": "200 response schema does not match 201 response schema. A PUT API must always return the same response schema for both the 200 and 201 status codes.",
  "path": [
    "definitions",
    "PrivateEndpointConnection"
  ]
}
```

## specification/security/resource-manager/Microsoft.Security/Security/SecurityOperatorsAPI

Swagger raw: 0; TypeSpec raw: 1; source-aligned: 1; default: 1.

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "SecurityOperator.tsp",
  "line": 78,
  "column": 3
}
```

## specification/security/resource-manager/Microsoft.Security/Security/SecuritySolutionsAPI

Swagger raw: 0; TypeSpec raw: 1; source-aligned: 1; default: 1.

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "ServerVulnerabilityAssessment.tsp",
  "line": 93,
  "column": 3
}
```

## specification/security/resource-manager/Microsoft.Security/Security/SensitivitySettingsAPI

Swagger raw: 1; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/security/resource-manager/Microsoft.Security/Security/SensitivitySettingsAPI",
  "swaggerFile": "projects/specification/security/resource-manager/Microsoft.Security/Security/SensitivitySettingsAPI/swagger/preview/2023-02-15-preview/sensitivitySettings.json",
  "validatorInputFile": "projects/specification/security/resource-manager/Microsoft.Security/Security/SensitivitySettingsAPI/swagger/preview/2023-02-15-preview/sensitivitySettings.json",
  "sourceDocuments": [
    "projects/specification/security/resource-manager/Microsoft.Security/Security/SensitivitySettingsAPI/swagger/preview/2023-02-15-preview/sensitivitySettings.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SensitivitySettings_CreateOrUpdate' Request Model: 'parameters[1].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/providers/Microsoft.Security/sensitivitySettings/current",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/providers/Microsoft.Security/sensitivitySettings/current",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 109,
        "column": 12
      },
      "end": {
        "line": 145,
        "column": 88
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model SensitivitySettingsAPI.GetSensitivitySettingsResponse. Found SensitivitySettingsAPI.UpdateSensitivitySettingsRequest.",
  "sourceFile": "GetSensitivitySettingsResponse.tsp",
  "line": 48,
  "column": 3
}
```

## specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI

Swagger raw: 1; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI",
  "swaggerFile": "projects/specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI/swagger/preview/2026-04-01-preview/security-SqlVulnerabilityAssessments.json",
  "validatorInputFile": "projects/specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI/swagger/preview/2026-04-01-preview/security-SqlVulnerabilityAssessments.json",
  "sourceDocuments": [
    "projects/specification/security/resource-manager/Microsoft.Security/Security/SqlVulnerabilityAssessmentsAPI/swagger/preview/2026-04-01-preview/security-SqlVulnerabilityAssessments.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SqlVulnerabilityAssessmentBaselineRules_CreateOrUpdate' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/{resourceId}/providers/Microsoft.Security/sqlVulnerabilityAssessments/default/baselineRules/{ruleId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/{resourceId}/providers/Microsoft.Security/sqlVulnerabilityAssessments/default/baselineRules/{ruleId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 437,
        "column": 12
      },
      "end": {
        "line": 523,
        "column": 119
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model SqlVulnerabilityAssessmentsAPI.RuleResults. Found SqlVulnerabilityAssessmentsAPI.RuleResultsInput.",
  "sourceFile": "RuleResults.tsp",
  "line": 87,
  "column": 3
}
```

## specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights

Swagger raw: 3; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights",
  "swaggerFile": "projects/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/swagger/preview/2025-10-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/swagger/preview/2025-10-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/swagger/preview/2025-10-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Actions_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/alertRules/{ruleId}/actions/{actionId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/alertRules/{ruleId}/actions/{actionId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 717,
        "column": 12
      },
      "end": {
        "line": 789,
        "column": 69
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights",
  "swaggerFile": "projects/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/swagger/preview/2025-10-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/swagger/preview/2025-10-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/swagger/preview/2025-10-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'EntityQueries_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/entityQueries/{entityQueryId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/entityQueries/{entityQueryId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 4543,
        "column": 12
      },
      "end": {
        "line": 4608,
        "column": 77
      }
    }
  }
}
```

### Swagger 3: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights",
  "swaggerFile": "projects/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/swagger/preview/2025-10-01-preview/openapi.json",
  "validatorInputFile": "projects/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/swagger/preview/2025-10-01-preview/openapi.json",
  "sourceDocuments": [
    "projects/specification/securityinsights/resource-manager/Microsoft.SecurityInsights/SecurityInsights/swagger/preview/2025-10-01-preview/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ThreatIntelligenceIndicator_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/threatIntelligence/main/indicators/{name}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/threatIntelligence/main/indicators/{name}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 9361,
        "column": 12
      },
      "end": {
        "line": 9426,
        "column": 81
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.SecurityInsights.EntityQuery. Found Microsoft.SecurityInsights.CustomEntityQuery.",
  "sourceFile": "EntityQuery.tsp",
  "line": 88,
  "column": 3
}
```

## specification/sql/resource-manager/Microsoft.Sql/SQL

Swagger raw: 20; TypeSpec raw: 9; source-aligned: 9; default: 9.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/databaseExtensions.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/databaseExtensions.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/databaseExtensions.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'DatabaseExtensions_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/extensions/{extensionName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/extensions/{extensionName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 159,
        "column": 12
      },
      "end": {
        "line": 252,
        "column": 43
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/databaseSqlVulnerabilityAssessmentBaselines.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/databaseSqlVulnerabilityAssessmentBaselines.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/databaseSqlVulnerabilityAssessmentBaselines.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'DatabaseSqlVulnerabilityAssessmentBaselines_CreateOrUpdate' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/sqlVulnerabilityAssessments/{vulnerabilityAssessmentName}/baselines/{baselineName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/sqlVulnerabilityAssessments/{vulnerabilityAssessmentName}/baselines/{baselineName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 217,
        "column": 12
      },
      "end": {
        "line": 317,
        "column": 83
      }
    }
  }
}
```

### Swagger 3: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/databaseSqlVulnerabilityAssessmentRuleBaselines.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/databaseSqlVulnerabilityAssessmentRuleBaselines.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/databaseSqlVulnerabilityAssessmentRuleBaselines.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'DatabaseSqlVulnerabilityAssessmentRuleBaselines_CreateOrUpdate' Request Model: 'parameters[8].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/sqlVulnerabilityAssessments/{vulnerabilityAssessmentName}/baselines/{baselineName}/rules/{ruleId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/sqlVulnerabilityAssessments/{vulnerabilityAssessmentName}/baselines/{baselineName}/rules/{ruleId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 244,
        "column": 12
      },
      "end": {
        "line": 348,
        "column": 90
      }
    }
  }
}
```

### Swagger 4: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/firewallRules.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/firewallRules.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/firewallRules.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'FirewallRules_Replace' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/firewallRules",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/firewallRules",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 95,
        "column": 12
      },
      "end": {
        "line": 147,
        "column": 57
      }
    }
  }
}
```

### Swagger 5: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/maintenanceWindows.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/maintenanceWindows.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/maintenanceWindows.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'MaintenanceWindows_CreateOrUpdate' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/maintenanceWindows/current",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/maintenanceWindows/current",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 106,
        "column": 12
      },
      "end": {
        "line": 166,
        "column": 70
      }
    }
  }
}
```

### Swagger 6: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/managedServerDnsAliases.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/managedServerDnsAliases.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/managedServerDnsAliases.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ManagedServerDnsAliases_CreateOrUpdate' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/dnsAliases/{dnsAliasName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/dnsAliases/{dnsAliasName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 148,
        "column": 12
      },
      "end": {
        "line": 242,
        "column": 43
      }
    }
  }
}
```

### Swagger 7: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/sqlVulnerabilityAssessmentBaseline.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/sqlVulnerabilityAssessmentBaseline.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/sqlVulnerabilityAssessmentBaseline.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SqlVulnerabilityAssessmentBaselines_CreateOrUpdate' Request Model: 'parameters[7].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/sqlVulnerabilityAssessments/{vulnerabilityAssessmentName}/baselines/{baselineName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/sqlVulnerabilityAssessments/{vulnerabilityAssessmentName}/baselines/{baselineName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 245,
        "column": 12
      },
      "end": {
        "line": 359,
        "column": 75
      }
    }
  }
}
```

### Swagger 8: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/sqlVulnerabilityAssessmentRuleBaseline.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/sqlVulnerabilityAssessmentRuleBaseline.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/sqlVulnerabilityAssessmentRuleBaseline.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SqlVulnerabilityAssessmentRuleBaseline_CreateOrUpdate' Request Model: 'parameters[8].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/sqlVulnerabilityAssessments/{vulnerabilityAssessmentName}/baselines/{baselineName}/rules/{ruleId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/sqlVulnerabilityAssessments/{vulnerabilityAssessmentName}/baselines/{baselineName}/rules/{ruleId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 272,
        "column": 12
      },
      "end": {
        "line": 390,
        "column": 82
      }
    }
  }
}
```

### Swagger 9: ConsistentResponseSchemaForPut

```json
{
  "rule": "ConsistentResponseSchemaForPut",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/common.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/databaseVulnerabilityAssessments.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/common.json"
  ],
  "sourceAttribution": "reported",
  "message": "200 response schema does not match 201 response schema. A PUT API must always return the same response schema for both the 200 and 201 status codes.",
  "path": [
    "definitions",
    "DatabaseVulnerabilityAssessment"
  ]
}
```

### Swagger 10: ConsistentResponseSchemaForPut

```json
{
  "rule": "ConsistentResponseSchemaForPut",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/common.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/jobExecutions.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/common.json"
  ],
  "sourceAttribution": "reported",
  "message": "200 response schema does not match 201 response schema. A PUT API must always return the same response schema for both the 200 and 201 status codes.",
  "path": [
    "definitions",
    "JobExecution"
  ]
}
```

### Swagger 11: ConsistentResponseSchemaForPut

```json
{
  "rule": "ConsistentResponseSchemaForPut",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/common.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/managedDatabaseSensitivityLabels.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/common.json"
  ],
  "sourceAttribution": "reported",
  "message": "200 response schema does not match 201 response schema. A PUT API must always return the same response schema for both the 200 and 201 status codes.",
  "path": [
    "definitions",
    "SensitivityLabel"
  ]
}
```

### Swagger 12: ConsistentResponseSchemaForPut

```json
{
  "rule": "ConsistentResponseSchemaForPut",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/common.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/managedDatabaseVulnerabilityAssessments.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/common.json"
  ],
  "sourceAttribution": "reported",
  "message": "200 response schema does not match 201 response schema. A PUT API must always return the same response schema for both the 200 and 201 status codes.",
  "path": [
    "definitions",
    "DatabaseVulnerabilityAssessment"
  ]
}
```

### Swagger 13: ConsistentResponseSchemaForPut

```json
{
  "rule": "ConsistentResponseSchemaForPut",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/common.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/sensitivityLabels.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/common.json"
  ],
  "sourceAttribution": "reported",
  "message": "200 response schema does not match 201 response schema. A PUT API must always return the same response schema for both the 200 and 201 status codes.",
  "path": [
    "definitions",
    "SensitivityLabel"
  ]
}
```

### Swagger 14: ConsistentResponseSchemaForPut

```json
{
  "rule": "ConsistentResponseSchemaForPut",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/common.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/sqlVulnerabilityAssessmentsSettings.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/common.json"
  ],
  "sourceAttribution": "reported",
  "message": "200 response schema does not match 201 response schema. A PUT API must always return the same response schema for both the 200 and 201 status codes.",
  "path": [
    "definitions",
    "SqlVulnerabilityAssessment"
  ]
}
```

### Swagger 15: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/firewallRules.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/firewallRules.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/firewallRules.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: FirewallRules_Replace",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/firewallRules",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/firewallRules",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 95,
        "column": 12
      },
      "end": {
        "line": 147,
        "column": 57
      }
    }
  }
}
```

### Swagger 16: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/firewallRules.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/firewallRules.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/firewallRules.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: FirewallRules_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/firewallRules/{firewallRuleName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/firewallRules/{firewallRuleName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 204,
        "column": 12
      },
      "end": {
        "line": 269,
        "column": 56
      }
    }
  }
}
```

### Swagger 17: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/iPv6FirewallRules.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/iPv6FirewallRules.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/iPv6FirewallRules.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: IPv6FirewallRules_CreateOrUpdate",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/ipv6FirewallRules/{firewallRuleName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/ipv6FirewallRules/{firewallRuleName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 148,
        "column": 12
      },
      "end": {
        "line": 213,
        "column": 60
      }
    }
  }
}
```

### Swagger 18: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/databaseExtensions.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/databaseExtensions.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/databaseExtensions.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/extensions/{extensionName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/extensions/{extensionName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/extensions/{extensionName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 103,
        "column": 170
      },
      "end": {
        "line": 252,
        "column": 43
      }
    }
  }
}
```

### Swagger 19: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/firewallRules.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/firewallRules.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/firewallRules.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/firewallRules has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/firewallRules"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/firewallRules"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 47,
        "column": 132
      },
      "end": {
        "line": 147,
        "column": 57
      }
    }
  }
}
```

### Swagger 20: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/sql/resource-manager/Microsoft.Sql/SQL",
  "swaggerFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/maintenanceWindows.json",
  "validatorInputFile": "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/maintenanceWindows.json",
  "sourceDocuments": [
    "projects/specification/sql/resource-manager/Microsoft.Sql/SQL/swagger/preview/2026-08-01-preview/maintenanceWindows.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/maintenanceWindows/current has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/maintenanceWindows/current"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/maintenanceWindows/current"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 47,
        "column": 170
      },
      "end": {
        "line": 166,
        "column": 70
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Sql.ImportExportExtensionsOperationResult. Found Microsoft.Sql.DatabaseExtensions.",
  "sourceFile": "ImportExportExtensionsOperationResult.tsp",
  "line": 50,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentBaselineSet. Found Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentRuleBaselineListInput.",
  "sourceFile": "DatabaseSqlVulnerabilityAssessmentBaselineSet.tsp",
  "line": 81,
  "column": 3
}
```

### TypeSpec 3

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentBaselineSet. Found Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentRuleBaselineListInput.",
  "sourceFile": "DatabaseSqlVulnerabilityAssessmentBaselineSet.tsp",
  "line": 146,
  "column": 3
}
```

### TypeSpec 4

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentRuleBaseline. Found Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentRuleBaselineInput.",
  "sourceFile": "DatabaseSqlVulnerabilityAssessmentRuleBaseline.tsp",
  "line": 84,
  "column": 3
}
```

### TypeSpec 5

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentRuleBaseline. Found Microsoft.Sql.DatabaseSqlVulnerabilityAssessmentRuleBaselineInput.",
  "sourceFile": "DatabaseSqlVulnerabilityAssessmentRuleBaseline.tsp",
  "line": 159,
  "column": 3
}
```

### TypeSpec 6

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "JobExecution.tsp",
  "line": 76,
  "column": 3
}
```

### TypeSpec 7

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Sql.ManagedServerDnsAlias. Found Microsoft.Sql.ManagedServerDnsAliasCreation.",
  "sourceFile": "ManagedServerDnsAlias.tsp",
  "line": 43,
  "column": 3
}
```

### TypeSpec 8

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "OutboundFirewallRule.tsp",
  "line": 43,
  "column": 3
}
```

### TypeSpec 9

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "ServerDnsAlias.tsp",
  "line": 43,
  "column": 3
}
```

## specification/storage/resource-manager/Microsoft.Storage/Storage

Swagger raw: 1; TypeSpec raw: 1; source-aligned: 1; default: 1.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/storage/resource-manager/Microsoft.Storage/Storage",
  "swaggerFile": "projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json",
  "validatorInputFile": "projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json",
  "sourceDocuments": [
    "projects/specification/storage/resource-manager/Microsoft.Storage/Storage/swagger/stable/2026-09-01/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'StorageAccounts_Create' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1268,
        "column": 12
      },
      "end": {
        "line": 1389,
        "column": 43
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Storage.StorageAccount. Found Microsoft.Storage.StorageAccountCreateParameters.",
  "sourceFile": "StorageAccount.tsp",
  "line": 111,
  "column": 3
}
```

## specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync

Swagger raw: 5; TypeSpec raw: 5; source-aligned: 5; default: 5.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync",
  "swaggerFile": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
  "validatorInputFile": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
  "sourceDocuments": [
    "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'StorageSyncServices_Create' Request Model: 'parameters[4].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 446,
        "column": 12
      },
      "end": {
        "line": 529,
        "column": 43
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync",
  "swaggerFile": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
  "validatorInputFile": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
  "sourceDocuments": [
    "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'RegisteredServers_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/registeredServers/{serverId}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/registeredServers/{serverId}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1154,
        "column": 12
      },
      "end": {
        "line": 1255,
        "column": 43
      }
    }
  }
}
```

### Swagger 3: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync",
  "swaggerFile": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
  "validatorInputFile": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
  "sourceDocuments": [
    "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SyncGroups_Create' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1666,
        "column": 12
      },
      "end": {
        "line": 1732,
        "column": 55
      }
    }
  }
}
```

### Swagger 4: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync",
  "swaggerFile": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
  "validatorInputFile": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
  "sourceDocuments": [
    "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'CloudEndpoints_Create' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 1933,
        "column": 12
      },
      "end": {
        "line": 2040,
        "column": 43
      }
    }
  }
}
```

### Swagger 5: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync",
  "swaggerFile": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
  "validatorInputFile": "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json",
  "sourceDocuments": [
    "projects/specification/storagesync/resource-manager/Microsoft.StorageSync/StorageSync/swagger/stable/2025-12-01/storagesync.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'ServerEndpoints_Create' Request Model: 'parameters[6].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/serverEndpoints/{serverEndpointName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/serverEndpoints/{serverEndpointName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 3019,
        "column": 12
      },
      "end": {
        "line": 3126,
        "column": 43
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.StorageSync.StorageSyncService. Found Microsoft.StorageSync.StorageSyncServiceCreateParameters.",
  "sourceFile": "StorageSyncService.tsp",
  "line": 52,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.StorageSync.SyncGroup. Found Microsoft.StorageSync.SyncGroupCreateParameters.",
  "sourceFile": "SyncGroup.tsp",
  "line": 51,
  "column": 3
}
```

### TypeSpec 3

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.StorageSync.CloudEndpoint. Found Microsoft.StorageSync.CloudEndpointCreateParameters.",
  "sourceFile": "CloudEndpoint.tsp",
  "line": 55,
  "column": 3
}
```

### TypeSpec 4

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.StorageSync.ServerEndpoint. Found Microsoft.StorageSync.ServerEndpointCreateParameters.",
  "sourceFile": "ServerEndpoint.tsp",
  "line": 53,
  "column": 3
}
```

### TypeSpec 5

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.StorageSync.RegisteredServer. Found Microsoft.StorageSync.RegisteredServerCreateParameters.",
  "sourceFile": "RegisteredServer.tsp",
  "line": 54,
  "column": 3
}
```

## specification/subscription/resource-manager/Microsoft.Subscription/Subscription

Swagger raw: 3; TypeSpec raw: 3; source-aligned: 3; default: 3.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/subscription/resource-manager/Microsoft.Subscription/Subscription",
  "swaggerFile": "projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json",
  "validatorInputFile": "projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json",
  "sourceDocuments": [
    "projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Alias_Create' Request Model: 'parameters[2].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/providers/Microsoft.Subscription/aliases/{aliasName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/providers/Microsoft.Subscription/aliases/{aliasName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 153,
        "column": 12
      },
      "end": {
        "line": 217,
        "column": 43
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/subscription/resource-manager/Microsoft.Subscription/Subscription",
  "swaggerFile": "projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json",
  "validatorInputFile": "projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json",
  "sourceDocuments": [
    "projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'SubscriptionPolicy_AddUpdatePolicyForTenant' Request Model: 'parameters[1].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/providers/Microsoft.Subscription/policies/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/providers/Microsoft.Subscription/policies/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 353,
        "column": 12
      },
      "end": {
        "line": 386,
        "column": 56
      }
    }
  }
}
```

### Swagger 3: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/subscription/resource-manager/Microsoft.Subscription/Subscription",
  "swaggerFile": "projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json",
  "validatorInputFile": "projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json",
  "sourceDocuments": [
    "projects/specification/subscription/resource-manager/Microsoft.Subscription/Subscription/swagger/preview/2025-11-01-preview/subscriptions.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'Subscriptions_PutTargetDirectory' Request Model: 'parameters[2].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/providers/Microsoft.Subscription/changeTenantRequest/default",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/providers/Microsoft.Subscription/changeTenantRequest/default",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 693,
        "column": 12
      },
      "end": {
        "line": 729,
        "column": 56
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Subscription.SubscriptionAliasResponse. Found Microsoft.Subscription.PutAliasRequest.",
  "sourceFile": "SubscriptionAliasResponse.tsp",
  "line": 40,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Subscription.TargetDirectoryResult. Found Microsoft.Subscription.TargetDirectoryRequest.",
  "sourceFile": "TargetDirectoryResult.tsp",
  "line": 51,
  "column": 3
}
```

### TypeSpec 3

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Subscription.GetTenantPolicyResponse. Found Microsoft.Subscription.PutTenantPolicyRequestProperties.",
  "sourceFile": "GetTenantPolicyResponse.tsp",
  "line": 43,
  "column": 3
}
```

## specification/support/resource-manager/Microsoft.Support/Support

Swagger raw: 0; TypeSpec raw: 2; source-aligned: 2; default: 2.

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "FileWorkspaceDetails.tsp",
  "line": 54,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "FileWorkspaceDetails.tsp",
  "line": 87,
  "column": 3
}
```

## specification/web/resource-manager/Microsoft.Web/AppService

Swagger raw: 31; TypeSpec raw: 8; source-aligned: 8; default: 8.

### Swagger 1: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'WebApps_CreateMSDeployOperation' Request Model: 'parameters[4].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/extensions/MSDeploy",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/extensions/MSDeploy",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 12494,
        "column": 12
      },
      "end": {
        "line": 12561,
        "column": 43
      }
    }
  }
}
```

### Swagger 2: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'WebApps_CreateInstanceMSDeployOperation' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/extensions/MSDeploy",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/extensions/MSDeploy",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 16009,
        "column": 12
      },
      "end": {
        "line": 16083,
        "column": 43
      }
    }
  }
}
```

### Swagger 3: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'WebApps_MigrateStorage' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/migrate",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/migrate",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 16749,
        "column": 12
      },
      "end": {
        "line": 16814,
        "column": 43
      }
    }
  }
}
```

### Swagger 4: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'WebApps_CreateMSDeployOperationSlot' Request Model: 'parameters[5].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/extensions/MSDeploy",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/extensions/MSDeploy",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 25346,
        "column": 12
      },
      "end": {
        "line": 25420,
        "column": 43
      }
    }
  }
}
```

### Swagger 5: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'WebApps_CreateInstanceMSDeployOperationSlot' Request Model: 'parameters[6].schema' Response Model: 'responses[201].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/extensions/MSDeploy",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/extensions/MSDeploy",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 27289,
        "column": 12
      },
      "end": {
        "line": 27370,
        "column": 43
      }
    }
  }
}
```

### Swagger 6: PutRequestResponseSchemeArm

```json
{
  "rule": "PutRequestResponseSchemeArm",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "A PUT operation request body schema should be the same as its 200 response schema, to allow reusing the same entity between GET and PUT. If the schema of the PUT request body is a superset of the GET response body, make sure you have a PATCH operation to make the resource updatable. Operation: 'StaticSites_CreateOrUpdateStaticSiteCustomDomain' Request Model: 'parameters[5].schema' Response Model: 'responses[200].schema'",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/staticSites/{name}/customDomains/{domainName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/staticSites/{name}/customDomains/{domainName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-25",
    "range": {
      "start": {
        "line": 37800,
        "column": 12
      },
      "end": {
        "line": 37876,
        "column": 43
      }
    }
  }
}
```

### Swagger 7: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_UpdateApplicationSettings",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/appsettings",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/appsettings",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 9136,
        "column": 12
      },
      "end": {
        "line": 9186,
        "column": 55
      }
    }
  }
}
```

### Swagger 8: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_UpdateAuthSettings",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/authsettings",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/authsettings",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 9239,
        "column": 12
      },
      "end": {
        "line": 9289,
        "column": 56
      }
    }
  }
}
```

### Swagger 9: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_UpdateAzureStorageAccounts",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/azurestorageaccounts",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/azurestorageaccounts",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 9490,
        "column": 12
      },
      "end": {
        "line": 9540,
        "column": 64
      }
    }
  }
}
```

### Swagger 10: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_UpdateBackupConfiguration",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/backup",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/backup",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 9588,
        "column": 12
      },
      "end": {
        "line": 9632,
        "column": 58
      }
    }
  }
}
```

### Swagger 11: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_UpdateConnectionStrings",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/connectionstrings",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/connectionstrings",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 9915,
        "column": 12
      },
      "end": {
        "line": 9959,
        "column": 58
      }
    }
  }
}
```

### Swagger 12: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_UpdateMetadata",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/metadata",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/metadata",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10099,
        "column": 12
      },
      "end": {
        "line": 10143,
        "column": 58
      }
    }
  }
}
```

### Swagger 13: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_UpdateSitePushSettings",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/pushsettings",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/pushsettings",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 10245,
        "column": 12
      },
      "end": {
        "line": 10289,
        "column": 58
      }
    }
  }
}
```

### Swagger 14: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_CreateOneDeployOperation",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/extensions/onedeploy",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/extensions/onedeploy",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 12649,
        "column": 12
      },
      "end": {
        "line": 12682,
        "column": 58
      }
    }
  }
}
```

### Swagger 15: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_CreateOrUpdateFunctionSecret",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/functions/{functionName}/keys/{keyName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/functions/{functionName}/keys/{keyName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 12911,
        "column": 12
      },
      "end": {
        "line": 12972,
        "column": 58
      }
    }
  }
}
```

### Swagger 16: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_CreateOrUpdateHostSecret",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/host/default/{keyType}/{keyName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/host/default/{keyType}/{keyName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 13171,
        "column": 12
      },
      "end": {
        "line": 13235,
        "column": 58
      }
    }
  }
}
```

### Swagger 17: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_MigrateStorage",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/migrate",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/migrate",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 16749,
        "column": 12
      },
      "end": {
        "line": 16814,
        "column": 43
      }
    }
  }
}
```

### Swagger 18: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_UpdateApplicationSettingsSlot",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/appsettings",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/appsettings",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 21695,
        "column": 12
      },
      "end": {
        "line": 21746,
        "column": 58
      }
    }
  }
}
```

### Swagger 19: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_UpdateAuthSettingsSlot",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/authsettings",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/authsettings",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 21802,
        "column": 12
      },
      "end": {
        "line": 21853,
        "column": 58
      }
    }
  }
}
```

### Swagger 20: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_UpdateAzureStorageAccountsSlot",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/azurestorageaccounts",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/azurestorageaccounts",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 22063,
        "column": 12
      },
      "end": {
        "line": 22114,
        "column": 58
      }
    }
  }
}
```

### Swagger 21: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_UpdateBackupConfigurationSlot",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/backup",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/backup",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 22170,
        "column": 12
      },
      "end": {
        "line": 22221,
        "column": 58
      }
    }
  }
}
```

### Swagger 22: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_UpdateConnectionStringsSlot",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/connectionstrings",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/connectionstrings",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 22542,
        "column": 12
      },
      "end": {
        "line": 22593,
        "column": 58
      }
    }
  }
}
```

### Swagger 23: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_UpdateMetadataSlot",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/metadata",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/metadata",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 22754,
        "column": 12
      },
      "end": {
        "line": 22805,
        "column": 58
      }
    }
  }
}
```

### Swagger 24: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_UpdateSitePushSettingsSlot",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/pushsettings",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/pushsettings",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 22921,
        "column": 12
      },
      "end": {
        "line": 22972,
        "column": 58
      }
    }
  }
}
```

### Swagger 25: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_CreateOrUpdateFunctionSecretSlot",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions/{functionName}/keys/{keyName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions/{functionName}/keys/{keyName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 25727,
        "column": 12
      },
      "end": {
        "line": 25794,
        "column": 58
      }
    }
  }
}
```

### Swagger 26: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: WebApps_CreateOrUpdateHostSecretSlot",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/host/default/{keyType}/{keyName}",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/host/default/{keyType}/{keyName}",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 26017,
        "column": 12
      },
      "end": {
        "line": 26088,
        "column": 58
      }
    }
  }
}
```

### Swagger 27: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: StaticSites_CreateOrUpdateStaticSiteBuildAppSettings",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/staticSites/{name}/builds/{environmentName}/config/appsettings",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/staticSites/{name}/builds/{environmentName}/config/appsettings",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 36095,
        "column": 12
      },
      "end": {
        "line": 36153,
        "column": 78
      }
    }
  }
}
```

### Swagger 28: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: StaticSites_CreateOrUpdateStaticSiteBuildFunctionAppSettings",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/staticSites/{name}/builds/{environmentName}/config/functionappsettings",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/staticSites/{name}/builds/{environmentName}/config/functionappsettings",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 36159,
        "column": 12
      },
      "end": {
        "line": 36217,
        "column": 86
      }
    }
  }
}
```

### Swagger 29: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: StaticSites_CreateOrUpdateStaticSiteAppSettings",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/staticSites/{name}/config/appsettings",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/staticSites/{name}/config/appsettings",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 37530,
        "column": 12
      },
      "end": {
        "line": 37580,
        "column": 73
      }
    }
  }
}
```

### Swagger 30: XmsResourceInPutResponse

```json
{
  "rule": "XmsResourceInPutResponse",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "The 200 response model for an ARM PUT operation must have x-ms-azure-resource extension set to true in its hierarchy.Operation: StaticSites_CreateOrUpdateStaticSiteFunctionAppSettings",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/staticSites/{name}/config/functionappsettings",
    "put"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/staticSites/{name}/config/functionappsettings",
      "put"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 37586,
        "column": 12
      },
      "end": {
        "line": 37636,
        "column": 81
      }
    }
  }
}
```

### Swagger 31: PutGetPatchResponseSchema

```json
{
  "rule": "PutGetPatchResponseSchema",
  "level": "error",
  "project": "specification/web/resource-manager/Microsoft.Web/AppService",
  "swaggerFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "validatorInputFile": "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json",
  "sourceDocuments": [
    "projects/specification/web/resource-manager/Microsoft.Web/AppService/swagger/stable/2026-07-15/openapi.json"
  ],
  "sourceAttribution": "reported",
  "message": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} has different responses for PUT/GET/PATCH operations. The PUT/GET/PATCH operations must have same schema response.",
  "path": [
    "paths",
    "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName}"
  ],
  "details": {
    "jsonpath": [
      "paths",
      "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName}"
    ],
    "validationCategory": "",
    "providerNamespace": false,
    "resourceType": false,
    "rpcGuidelineCode": "RPC-Put-V1-12",
    "range": {
      "start": {
        "line": 7419,
        "column": 172
      },
      "end": {
        "line": 7673,
        "column": 58
      }
    }
  }
}
```

### TypeSpec 1

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Web.StaticSiteCustomDomainOverviewARMResource. Found Microsoft.Web.StaticSiteCustomDomainRequestPropertiesARMResource.",
  "sourceFile": "StaticSiteCustomDomainOverviewARMResource.tsp",
  "line": 54,
  "column": 3
}
```

### TypeSpec 2

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Web.FunctionEnvelope. Found Microsoft.Web.KeyInfo.",
  "sourceFile": "FunctionEnvelope.tsp",
  "line": 350,
  "column": 3
}
```

### TypeSpec 3

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "SiteExtensionInfo.tsp",
  "line": 77,
  "column": 3
}
```

### TypeSpec 4

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "ARM PUT operations must have a request body.",
  "sourceFile": "SiteExtensionInfo.tsp",
  "line": 165,
  "column": 3
}
```

### TypeSpec 5

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Web.MSDeployStatus. Found Microsoft.Web.MSDeploy.",
  "sourceFile": "MSDeployStatus.tsp",
  "line": 82,
  "column": 3
}
```

### TypeSpec 6

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Web.MSDeployStatus. Found Microsoft.Web.MSDeploy.",
  "sourceFile": "MSDeployStatus.tsp",
  "line": 161,
  "column": 3
}
```

### TypeSpec 7

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Web.MSDeployStatus. Found Microsoft.Web.MSDeploy.",
  "sourceFile": "MSDeployStatus.tsp",
  "line": 239,
  "column": 3
}
```

### TypeSpec 8

```json
{
  "rule": "@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response",
  "message": "PUT request body must use resource model Microsoft.Web.MSDeployStatus. Found Microsoft.Web.MSDeploy.",
  "sourceFile": "MSDeployStatus.tsp",
  "line": 324,
  "column": 3
}
```
