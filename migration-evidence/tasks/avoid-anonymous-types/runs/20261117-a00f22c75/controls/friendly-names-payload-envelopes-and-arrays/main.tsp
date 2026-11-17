import "@typespec/http";
import "@typespec/rest";
import "@typespec/versioning";
import "@azure-tools/typespec-azure-core";
import "@azure-tools/typespec-azure-resource-manager";
using TypeSpec.Http;
using Azure.Core;
using Azure.ResourceManager;
@service
namespace Contoso;
model Widget {
  value: string;
}
model Result<T> {
  value: T;
}

@friendlyName("ResultOf{name}", T)
model Friendly<T> {
  value: T;
}
alias FriendlyAlias = Friendly<Widget>;
@get @route("/friendly") op friendly(): Friendly<Widget>;
@get @route("/alias") op aliasResult(): FriendlyAlias;
@get @route("/page") op page(): Page<Widget>;
@get @route("/arm-page") op armPage(): ResourceListResult<Widget>;
@get @route("/envelope") op envelope(): ArmResponse<Widget>;
@get @route("/array") op readArray(): Widget[];
