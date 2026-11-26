import "@typespec/http";
import "@azure-tools/typespec-client-generator-core";
using TypeSpec.Http;
using Azure.ClientGenerator.Core;
@service namespace NativeControls;
model Widget { @clientName(exact("same")) same: string; @clientName(exact("other"), "python") @clientName(exact("other")) second: string; }
