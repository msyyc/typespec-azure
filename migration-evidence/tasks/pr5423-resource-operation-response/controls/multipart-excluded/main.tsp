
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

@armResourceOperations interface Widgets {
@put @armResourceCreateOrUpdate(Widget) create(...ResourceInstanceParameters<Widget>, @header contentType: "multipart/form-data", @multipartBody body: { part: HttpPart<string> }): ArmResponse<Widget>;
}
