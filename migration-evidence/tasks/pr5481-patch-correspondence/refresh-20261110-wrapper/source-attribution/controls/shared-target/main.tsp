
import "@typespec/http";
import "@azure-tools/typespec-azure-resource-manager";
using TypeSpec.Http;
@service namespace Context;
model PatchBody { value?: string; }
model Accepted { value?: string; }
model Incompatible { value?: int32; }
model Missing { other?: string; }
@route("/accepted") @put op putAccepted(@body body: Accepted): void;
@route("/accepted") @patch op patchAccepted(@body body: PatchBody): void;
@route("/incompatible") @put op putIncompatible(@body body: Incompatible): void;
@route("/incompatible") @patch op patchIncompatible(@body body: PatchBody): void;
@route("/missing") @put op putMissing(@body body: Missing): void;
@route("/missing") @patch op patchMissing(@body body: PatchBody): void;
@route("/no-body") @put op putNoBody(@body body: Accepted): void;
#suppress "@azure-tools/typespec-azure-resource-manager/arm-resource-patch" "Approved body exception."
@route("/no-body") @patch op patchNoBody(): void;
@route("/empty-body") @put op putEmpty(@body body: Accepted): void;
@route("/empty-body") @patch op patchEmpty(@body body: {}): void;
