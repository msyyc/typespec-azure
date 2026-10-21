import "@typespec/http";
import "@azure-tools/typespec-autorest";
using TypeSpec.Http;

@service namespace Contoso;
model Unused { enabled: boolean; }
model Query {
  @Autorest.useRef("./common.json#/parameters/Flag")
  @query flag: boolean;
}
@Autorest.useRef("./common.json#/definitions/Base")
model Base { name: string; }
model Child extends Base { enabled: boolean; }
union Choice { value: { enabled: boolean; }, absent: null }
@get @route("/base") op read(...Query): Base;
