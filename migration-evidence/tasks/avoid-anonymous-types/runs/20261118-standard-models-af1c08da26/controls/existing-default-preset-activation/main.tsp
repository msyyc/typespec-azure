
import "@typespec/http";
import "@typespec/rest";
import "@typespec/versioning";
import "@azure-tools/typespec-azure-core";
import "@azure-tools/typespec-azure-resource-manager";
using TypeSpec.Http;
using Azure.Core;
using Azure.ResourceManager;
@service namespace Contoso;
model Widget { value: string; }
model Result<T> { value: T; }
@get @route("/dictionary") op dictionary(): Record<string>;