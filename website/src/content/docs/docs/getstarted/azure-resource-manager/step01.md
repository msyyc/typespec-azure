---
title: 2. Defining the Service
description: Defining the ARM service
llmstxt: true
---

To define an Azure Resource Manager service, the first thing you will need to do is define the service namespace and decorate it with the `service` and `armProviderNamespace` decorators:

```typespec tryit="{"emit": ["@azure-tools/typespec-autorest"]}"
@armProviderNamespace
@service(#{ title: "<service name>" })
namespace <mynamespace>;
```

For example:

```typespec
@armProviderNamespace
@service(#{ title: "Contoso User Service" })
@armCommonTypesVersion(Azure.ResourceManager.CommonTypes.Versions.v6)
@versioned(Versions)
namespace Contoso.Users;

/** Contoso User Service API versions */
enum Versions {
  /** 2025-01-01 version */
  `2025-01-01`,
}
```

Apply `@armCommonTypesVersion` to the service namespace when all API versions use the same ARM
`common-types` version. If the required `common-types` version varies by API version, apply the
decorator to each member of the service's version enum instead.

## The `using` keyword

Just after the `namespace` declaration, you will also need to include a few `using` statements to pull in symbols from the namespaces of libraries you will for your specification.

For example, these lines pull in symbols from the `@typespec/rest` and `@azure-tools/typespec-azure-resource-manager`:

```
using Http;
using Rest;
using Azure.ResourceManager;
```

## The `operations` interface

All Resource Providers are required to provide operations that list the available operations for their resources. If you are using ProviderHub (RPaaS: RP as a Service), this functionality can be provided for you, but you will still need to include these operations in your api description. You can include these operations in your API description automatically using the following code:

```typespec
interface Operations extends Azure.ResourceManager.Operations {}
```
