
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

alias StandardAlias = Azure.Core.Foundations.OperationStatus<Widget>;
model LocalStatus<T> is Azure.Core.Foundations.OperationStatus<T>;
model BodyEnvelope<T> { @body body: T; }
model RootEnvelope<T> { @bodyRoot body: T; }
@get @route("/core") op core(): Azure.Core.Foundations.OperationStatus<Widget>;
@get @route("/resource") op resource(): ResourceOperationStatus<Widget>;
@get @route("/arm") op arm(): ArmOperationStatus;
@get @route("/alias") op aliasResult(): StandardAlias;
@get @route("/local") op readLocalStatus(): LocalStatus<Widget>;
@get @route("/dictionary") op dictionary(): ArmResponse<Record<string>>;
@get @route("/body") op anonymousBody(): BodyEnvelope<{ value: string }>;
@get @route("/body-root") op anonymousBodyRoot(): RootEnvelope<{ value: string }>;
