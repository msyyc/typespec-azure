
import "@typespec/http";
import "@typespec/rest";
import "@typespec/openapi";
import "@azure-tools/typespec-azure-core";
import "@azure-tools/typespec-azure-resource-manager";
using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.OpenAPI;
using Azure.ResourceManager;
@service @armProviderNamespace namespace Microsoft.Coverage;
model Widget is ProxyResource<{}> { ...ResourceNameParameter<Widget>; }
model Other is ProxyResource<{}> { ...ResourceNameParameter<Other>; }
model Input { value?: string; }
model Lookalike { ...Widget; }
@armResourceOperations interface Widgets { @get @armResourceList(Widget) list(...Foundations.SubscriptionScope<Widget>): ArmResponse<ResourceListResult<Other>>; }