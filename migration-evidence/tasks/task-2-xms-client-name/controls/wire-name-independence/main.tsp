import "@typespec/http";
import "@azure-tools/typespec-client-generator-core";
using TypeSpec.Http;
using Azure.ClientGenerator.Core;
@service namespace NativeControls;
model Widget { @encodedName("application/json", "wire_name") @clientName("name") name: string; } @get op read(@query("wire_filter") @clientName("filter") filter: string): Widget;
