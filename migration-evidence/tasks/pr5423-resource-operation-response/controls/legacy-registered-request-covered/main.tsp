
import "@typespec/http";
import "@typespec/rest";
import "@typespec/versioning";
import "@azure-tools/typespec-azure-core";
import "@azure-tools/typespec-azure-resource-manager";
using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.ResourceManager;
@service @armProviderNamespace namespace Microsoft.Coverage;
model Widget is TrackedResource<{ value?: string }> { ...ResourceNameParameter<Widget>; }
model Other is ProxyResource<{}> { ...ResourceNameParameter<Other>; }
model Input { value?: string; }

@armResourceOperations interface LegacyOps extends Azure.ResourceManager.Legacy.LegacyOperations<
  {...ApiVersionParameter, ...SubscriptionIdParameter, ...ResourceGroupParameter, ...Azure.ResourceManager.Legacy.Provider},
  {@path @segment("widgets") @key widgetName: string;}
> {}

@armResourceOperations interface Widgets {
create is LegacyOps.CreateOrUpdateAsync<Widget, Request = Input>;
}
