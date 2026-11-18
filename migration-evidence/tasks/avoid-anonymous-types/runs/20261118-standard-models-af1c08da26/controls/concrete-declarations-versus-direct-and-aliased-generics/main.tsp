
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

model Settings is Record<string>;
model StringResult is Result<string>;
alias SettingsAlias = Record<string>;
alias StringResultAlias = Result<string>;
@get @route("/settings") op settings(): Settings;
@get @route("/result") op result(): StringResult;
@get @route("/dictionary") op dictionary(): Record<string>;
@get @route("/dictionary-alias") op dictionaryAlias(): SettingsAlias;
@get @route("/generic") op generic(): Result<string>;
@get @route("/generic-alias") op genericAlias(): StringResultAlias;
