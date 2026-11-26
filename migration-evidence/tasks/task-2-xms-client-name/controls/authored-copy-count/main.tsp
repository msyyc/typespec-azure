import "@typespec/http";
import "@azure-tools/typespec-client-generator-core";
using TypeSpec.Http;
using Azure.ClientGenerator.Core;
@service namespace NativeControls;
model Base { @clientName("name") name: string; } model Derived extends Base {} model Copy { ...Base; } model Independent { @clientName("name") name: string; }
