
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

alias SubscriptionOps = Azure.ResourceManager.Legacy.LegacyOperations<
  {...ApiVersionParameter, ...SubscriptionIdParameter, ...Azure.ResourceManager.Legacy.Provider},
  {@path @key @segment("widgets") widgetName: string;}, ResourceName = "Widgets"
>;
alias TenantOps = Azure.ResourceManager.Legacy.LegacyOperations<
  {...ApiVersionParameter, ...Azure.ResourceManager.Legacy.Provider},
  {@path @key @segment("widgets") widgetName: string;}, ResourceName = "Widgets"
>;

    @armResourceOperations interface Subscriptions {
      read is SubscriptionOps.Read<Widget>;
      list is SubscriptionOps.List<Widget, Response = ArmResponse<ResourceListResult<Other>>>;
    }
    @armResourceOperations interface Tenants {
      read is TenantOps.Read<Widget>;
      list is TenantOps.List<Widget, Response = ArmResponse<ResourceListResult<Other>>>;
    }
    