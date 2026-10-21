import "@typespec/http";
import "@typespec/rest";
import "@typespec/openapi";
import "@typespec/versioning";
import "@azure-tools/typespec-autorest";
import "@azure-tools/typespec-azure-core";

using TypeSpec.Http;
using TypeSpec.Versioning;

@useAuth(ApiKeyAuth<ApiKeyLocation.header, "api-key">)
@service(#{ title: "Boolean coverage controls" })
@versioned(Versions)
namespace BooleanCoverageControls;

enum Versions {
  v2026_01_01: "2026-01-01",
}

scalar DerivedFlag extends boolean;

union WidgetState {
  Enabled: "Enabled",
  Disabled: "Disabled",
  string,
}

model Widget {
  plain: boolean;
  @visibility(Lifecycle.Delete)
  omitted: boolean;
  constant: true;
  nullable: boolean | null;
  items: boolean[];
  dictionary: Record<boolean>;
  derived: DerivedFlag;
  state: WidgetState;
}

@route("/widgets/{name}")
@get
op getWidget(@path name: string, @query("api-version") apiVersion: string): Widget;
