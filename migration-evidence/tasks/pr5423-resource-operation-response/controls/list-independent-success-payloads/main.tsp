
import "@typespec/http";
import "@typespec/rest";
import "@azure-tools/typespec-azure-core";
import "@azure-tools/typespec-azure-resource-manager";
import "@typespec/openapi";
using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.OpenAPI;
using Azure.ResourceManager;
@service @armProviderNamespace namespace Microsoft.Coverage;
model Widget is ProxyResource<{}> { ...ResourceNameParameter<Widget>; }
model Input { value?: string; }

        @armResourceOperations interface Widgets {
          @get @armResourceList(Widget)
          list(...Foundations.SubscriptionScope<Widget>): ArmResponse<ResourceListResult<Widget>> | ArmCreatedResponse<Input>;
        }
        