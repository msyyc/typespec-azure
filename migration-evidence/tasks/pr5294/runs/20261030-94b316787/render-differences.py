"""Render saved raw-target differences without asserting semantic matching."""

import collections
import json
from pathlib import Path
import posixpath
import sys
from urllib.parse import quote

root, output = map(Path, sys.argv[1:3])
coverage = json.loads((root / "coverage.json").read_text())
native = {x["project"]: x for x in json.loads((root / "native-results.json").read_text())}
swagger = json.loads((root / "swagger-observations.json").read_text())
rows = [x for x in coverage["projects"] if x["rawDifference"] != 0]
rows.sort(key=lambda x: x["project"])
assert len(rows) == 83


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def anchor(project):
    return "project-" + str(next(i for i, row in enumerate(rows, 1)
                                 if row["project"] == project))


def explanation(project):
    causes = {
        "/confidentialledger/": "Read/Create-only inherited location is excluded from effective PATCH input.",
        "/dynatrace/": "Read-only provisioningState; saved Swagger diagnoses a readOnly sibling of a reference.",
        "/elastic/": "Read-only provisioningState; saved Swagger diagnoses a readOnly sibling of a reference.",
        "/help/": "Read-only provisioningState; saved Swagger diagnoses a readOnly sibling of a reference.",
        "/ServiceGroups": "Read-only provisioningState; saved Swagger diagnoses a readOnly sibling of a reference.",
        "/newrelic/": "Read-only provisioningState; saved Swagger diagnoses a readOnly sibling of a reference.",
        "/SecurityConnectorsDevOpsAPI": "Four Read-only provisioningState uses; saved Swagger diagnoses readOnly reference siblings.",
        "/SAPDiscoverySites": "Required dataSource lies inside Read-only performanceData and is excluded from PATCH input.",
        "/apicenter/": "False default is checked natively but skipped by the Swagger truthiness test.",
        "/azuredatatransfer/": "Zero defaults and array-item defaults are native extensions.",
        "/computeschedule/": "False defaults, including an array item, are native extensions.",
        "/discovery/": "Zero default in imported source is retained by source-scope traversal.",
        "/configurationmanager": "Array-item defaults; repeated source uses remain separate raw findings.",
        "/elasticsan/": "Array-item default is outside Swagger traversal.",
        "/imagebuilder/": "Empty-string and zero defaults are skipped by Swagger truthiness.",
        "/informatica/": "Recursive update shape has missing resource keys; saved Swagger absence remains unresolved.",
        "/fluxConfigurations": "False defaults are skipped by Swagger truthiness.",
        "/managednetworkfabric/": "Unprojected removed/renamed properties versus latest-version Swagger; no version-aligned comparison.",
        "/ScheduledQueryRuleApi": "Defaults below array items are outside Swagger traversal.",
        "/PipelineGroups": "Defaults below arrays, including removed-version declarations; source and latest-version populations differ.",
        "/postgresql/": "Empty-string and zero defaults are skipped by Swagger truthiness.",
        "/programmableconnectivity/": "Removed operator connection property combines with newer required application fields in unprojected source.",
        "/hcpopenshiftclusters": "Array-item default is outside Swagger traversal.",
        "/edgeorder/": "Parent-versus-leaf layout fanout plus an additional zero default; no common-unit normalization.",
        "/domainregistration/": "Create-only contacts and Read-only subtrees are excluded; shared default remains checked.",
        "/sql/": "Create-only/Read-only input exclusions and repeated operations explain material parts; residual correspondence unassessed.",
        "/eventgrid/": "Layout fanout, source reuse and version/visibility policies; full target correspondence remains unassessed.",
        "/netapp/": "Array defaults and removed-version source coexist; residual correspondence unassessed.",
        "/search/": "Source/version and layout-selection differences; residual layout correspondence unassessed.",
    }
    matches = [text for key, text in causes.items() if key in project]
    return matches[0] if matches else (
        "Different raw targets retained. Complete target correspondence and any remaining "
        "within-project residual are unassessed; this row is not accepted as parity."
    )


text = [
    "# Fresh diagnostic differences", "",
    "All 83 unequal-count projects are retained below. Each project has both raw totals, "
    "signed/absolute/relative gaps and every exact diagnostic target. Counts at a common "
    "Swagger path or source location are not collapsed into actionable defects. "
    "The 404 equal-count projects remain in the population/coverage receipts; equality "
    "does not establish target correspondence.", "",
    "See [verified cause examples and limits](fresh-examples.md). A stated cause can explain "
    "a family without proving exact cross-engine correspondence for the entire project. "
    "Unresolved residuals remain visible; no source changes or invented normalization were applied.", "",
    "| Project | Swagger linter | TypeSpec linter | TypeSpec minus Swagger |",
    "| --- | ---: | ---: | ---: |",
]
for row in rows:
    text.append(f"| [{row['project']}](#{anchor(row['project'])}) | "
                f"{row['validatorRawCount']} | {row['nativeAlignedCount']} | "
                f"{-row['rawDifference']:+} |")
for row in rows:
    project = row["project"]
    sw = [d for d in swagger if d["project"] == project]
    ns = native[project]["diagnostics"]
    assert len(sw) == row["validatorRawCount"] and len(ns) == row["nativeAlignedCount"]
    relative = abs(row["rawDifference"]) / max(len(sw), len(ns), 1)
    text.extend([
        "", f'<a id="{anchor(project)}"></a>', f"## {project}", "",
        f"API version: `{row['apiVersion']}`. Swagger linter **{len(sw)}**; "
        f"TypeSpec linter **{len(ns)}**. Signed TypeSpec-minus-Swagger gap "
        f"**{-row['rawDifference']:+}**, absolute **{abs(row['rawDifference'])}**, "
        f"relative `absolute / max(Swagger, TypeSpec, 1)` **{relative:.2%}**.", "",
        explanation(project), "",
        "**After-analysis common actionable count:** unassessed. "
        "Per-member TypeSpec attribution is unavailable. See the cause appendix for "
        "verified dispositions; unresolved correspondence blocks equivalence, not publication "
        "of the observations.", "",
        "<details>", "<summary>Every exact target and its raw multiplicity</summary>", "",
        "### Swagger linter targets", "",
    ])
    if not sw:
        text.extend(["No selected Swagger-linter findings.", ""])
    else:
        grouped = collections.Counter(
            (d["rule"], d["swaggerFile"], json.dumps(d["path"], separators=(",", ":")),
             d["message"]) for d in sw)
        text.extend(["| Occurrences | Rule | Exact document and JSON path | Diagnostic |",
                     "| ---: | --- | --- | --- |"])
        for (rule, file, pointer, message), count in sorted(grouped.items()):
            text.append(f"| {count} | `{rule}` | `{cell(file)}`<br>`{cell(pointer)}` | {cell(message)} |")
        text.extend(["", "Invoked input, reported documents and source-attribution status are "
                     "retained unchanged in `runs/20261030-94b316787/swagger-observations.json`.", ""])
    text.extend(["### TypeSpec linter targets", ""])
    if not ns:
        text.extend(["No target TypeSpec-linter findings.", ""])
    else:
        grouped = collections.Counter(
            (d.get("sourceFile"), d.get("line"), d.get("column"), d["message"]) for d in ns)
        text.extend(["| Occurrences | Exact project-relative source target | Diagnostic |",
                     "| ---: | --- | --- |"])
        for (file, line, column, message), count in sorted(grouped.items()):
            target = f"`{cell(file)}:{line}:{column}`"
            source = posixpath.normpath(project + "/" + file.replace("\\", "/")) if file else ""
            if source.startswith("specification/") and line:
                url = ("https://github.com/msyyc/azure-rest-api-specs/blob/"
                       "2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/"
                       + quote(source, safe="/") + f"#L{line}")
                target = f"[{target}]({url})"
            text.append(f"| {count} | {target} | {cell(message)} |")
        text.extend(["", "Each row preserves repeated use multiplicity; source locations are not "
                     "a common actionable unit with Swagger paths.", ""])
    text.extend(["</details>", ""])
output.write_text("\n".join(text), encoding="utf-8")
print(json.dumps({"differingProjects": len(rows), "bytes": output.stat().st_size,
                  "anchors": {row["project"]: anchor(row["project"]) for row in rows}}, indent=2))
