"""Recount the saved PATCH observations without running either linter."""

import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RUN = ROOT / "runs" / "20261030-94b316787"
TRACE = ROOT / "runs" / "20261102-semantic-analysis"
NETWORK_PROJECT = (
    "specification/managednetworkfabric/resource-manager/"
    "Microsoft.ManagedNetworkFabric/ManagedNetworkFabric"
)
NETAPP_PROJECT = "specification/netapp/resource-manager/Microsoft.NetApp/NetApp"
PIPELINE_PROJECT = (
    "specification/monitoringservice/resource-manager/Microsoft.Monitor/PipelineGroups"
)
REMOVED_PIPELINE_PATHS = {
    "properties.exporters[].azureMonitorWorkspaceLogs.concurrency.batchQueueSize",
    "properties.exporters[].azureMonitorWorkspaceLogs.concurrency.workerCount",
    "properties.processors[].batch.timeoutv20241001preview",
    "properties.receivers[].syslog.protocol",
    "properties.receivers[].udp.encoding",
    "properties.receivers[].udp.jsonArrayMapper.destinationField.destination",
    "properties.receivers[].udp.readQueueLength",
}
EXCLUDED_CATEGORIES = {
    "client-only-source-operation",
    "known-version-population",
    "removed-source-field-or-ancestor",
    "removed-netapp-source",
    "multiple-source-operations",
    "additional-version-scoped-source",
}


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def exclusion(row):
    remaining = row.get("typespecRemaining") or {}
    category = remaining.get("category")
    count = remaining.get("count", 0)
    if category in EXCLUDED_CATEGORIES or (
        category == "array-missing" and row["project"] == NETWORK_PROJECT
    ):
        return count, category
    if (
        row["project"] == NETAPP_PROJECT
        and row["propertyPath"] == "properties.activeDirectories[].organizationalUnit"
    ):
        assert category == "array-default" and count == 2
        return 1, "removed-netapp-same-route-operation"
    if row["project"] == PIPELINE_PROJECT and row["propertyPath"] in REMOVED_PIPELINE_PATHS:
        assert category == "array-default" and count == 1
        return 1, "removed-pipeline-field-or-ancestor"
    return 0, None


def family(kind):
    if kind in {"required", "default", "visibility"}:
        return "safety"
    if kind == "missing":
        return "layout"
    if kind == "immutable":
        return "immutable"
    raise ValueError(f"Unknown check kind: {kind}")


def main():
    coverage = load(RUN / "coverage.json")
    native = load(RUN / "native-results.json")
    analysis = load(TRACE / "analysis.json")
    ledger = load(TRACE / "difference-ledger.json")["differences"]
    comparison = load(
        ROOT / "runs" / "20261102-8a92389c9" / "diagnostic-differences.json"
    )
    assert comparison["changedProjects"] == 0 and not comparison["differences"]
    assert comparison["projects"] == 487
    assert len(coverage["projects"]) == len(native) == 487
    assert all(project["status"] == "success" for project in native)
    assert sum(project["validatorRawCount"] for project in coverage["projects"]) == 975
    assert sum(project["nativeRawCount"] for project in coverage["projects"]) == 1337
    assert sum(len(project["rawDiagnostics"]) for project in native) == 1337

    exclusions = []
    by_project = Counter()
    by_family = Counter()
    by_reason = Counter()
    residuals = defaultdict(lambda: {"swagger": Counter(), "typespec": Counter()})
    project_residuals = defaultdict(lambda: {"swagger": Counter(), "typespec": Counter()})
    for index, row in enumerate(ledger, start=1):
        project = row["project"]
        check_family = family(row["kind"])
        swagger = row.get("swaggerRemaining") or {}
        typespec = row.get("typespecRemaining") or {}
        sw_count = swagger.get("count", 0)
        ts_count = typespec.get("count", 0)
        removed, reason = exclusion(row)
        if removed:
            assert removed <= row["typespec"] - row["sharedKeyOccurrences"]
            by_project[project] += removed
            by_family[check_family] += removed
            by_reason[reason] += removed
            exclusions.append(
                {
                    "ledgerRow": index,
                    "project": project,
                    "route": row["route"],
                    "check": row["kind"],
                    "propertyPath": row["propertyPath"],
                    "count": removed,
                    "reason": reason,
                    "originalLedgerCategory": typespec["category"],
                    "swaggerCallbacksAtKey": row["swagger"],
                    "typespecDiagnosticsAtKey": row["typespec"],
                    "sharedTextKeyOccurrences": row["sharedKeyOccurrences"],
                }
            )
        if sw_count:
            residuals[check_family]["swagger"][swagger["category"]] += sw_count
            project_residuals[project]["swagger"][swagger["category"]] += sw_count
        if ts_count - removed:
            residuals[check_family]["typespec"][typespec["category"]] += ts_count - removed
            project_residuals[project]["typespec"][typespec["category"]] += ts_count - removed

    assert sum(by_project.values()) == 91
    assert dict(by_family) == {"safety": 33, "layout": 57, "immutable": 1}
    assert analysis["checkPathAccounting"]["commonOccurrences"] == 834
    assert sum(sum(x["swagger"].values()) for x in residuals.values()) == 223
    assert sum(sum(x["typespec"].values()) for x in residuals.values()) == 412
    assert 834 + 223 == 1057
    assert 834 + 412 == 1337 - sum(by_project.values())
    assert 975 - 1246 == 165 + 6 + 52 - 175 - 185 - 24 - 7 - 21 - 82

    anchors = dict(
        (project, anchor)
        for anchor, project in re.findall(
            r'<a id="(project-\d+)"></a>\s*\n\s*## (specification/\S+)',
            (ROOT / "detailed-differences.md").read_text(encoding="utf-8"),
        )
    )
    projects = []
    for project in coverage["projects"]:
        name = project["project"]
        swagger = project["validatorRawCount"]
        configured = project["nativeRawCount"]
        removed = by_project[name]
        scoped = configured - removed
        assert scoped >= 0
        remainder = project_residuals[name]
        projects.append(
            {
                "project": name,
                "apiVersion": project["apiVersion"],
                "swaggerReported": swagger,
                "typespecConfiguredTargetOnly": configured,
                "typespecExcluded": removed,
                "typespecScopedObserved": scoped,
                "swaggerMinusTypespec": swagger - scoped,
                "absoluteDifference": abs(swagger - scoped),
                "relativeDifference": round(abs(swagger - scoped) / max(swagger, scoped, 1), 6),
                "unsharedSwaggerCallbacks": dict(sorted(remainder["swagger"].items())),
                "unsharedTypespecDiagnostics": dict(sorted(remainder["typespec"].items())),
                "detailAnchor": anchors.get(name),
            }
        )

    assert sum(p["typespecScopedObserved"] for p in projects) == 1246
    unequal = [p for p in projects if p["swaggerMinusTypespec"]]
    different = [
        p
        for p in projects
        if p["swaggerMinusTypespec"]
        or p["unsharedSwaggerCallbacks"]
        or p["unsharedTypespecDiagnostics"]
    ]
    assert all(p["detailAnchor"] for p in different)
    swagger_excess = sum(max(p["swaggerMinusTypespec"], 0) for p in projects)
    typespec_excess = sum(max(-p["swaggerMinusTypespec"], 0) for p in projects)
    assert swagger_excess - typespec_excess == -271

    output = {
        "schemaVersion": 1,
        "scope": {
            "projects": 487,
            "candidateCommit": "8a92389c9f9488035ab65c6ed3e08a49cc822f25",
            "attributionTraceCommit": "94b316787e2a19847c26986412ce254ca4da33b4",
            "specsCommit": "2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9",
            "swagger": "selected-version saved reports",
            "typespec": "unprojected source, target-only; subtract only identified out-of-population occurrences",
            "suppressedOwningDiagnostics": "unassessed, not zero",
            "limitation": "Text-key accounting does not prove defect identity or version alignment.",
        },
        "totals": {
            "swaggerReported": 975,
            "typespecConfiguredTargetOnly": 1337,
            "typespecExcluded": sum(by_project.values()),
            "typespecScopedObserved": 1246,
            "swaggerFunctionChecks": 1057,
            "spectralReportingReduction": 82,
            "sharedTextKeyOccurrences": 834,
            "unsharedSwaggerCallbacks": 223,
            "unsharedTypespecDiagnostics": 412,
            "swaggerHigherProjects": sum(p["swaggerMinusTypespec"] > 0 for p in projects),
            "typespecHigherProjects": sum(p["swaggerMinusTypespec"] < 0 for p in projects),
            "equalCountProjects": sum(p["swaggerMinusTypespec"] == 0 for p in projects),
            "unequalCountProjects": len(unequal),
            "differentCheckOrCountProjects": len(different),
            "swaggerExcess": swagger_excess,
            "typespecExcess": typespec_excess,
            "absoluteDifference": swagger_excess + typespec_excess,
            "netDifference": swagger_excess - typespec_excess,
        },
        "excludedByFamily": dict(sorted(by_family.items())),
        "excludedByReason": dict(sorted(by_reason.items())),
        "excludedByProject": dict(sorted(by_project.items())),
        "excludedOccurrences": exclusions,
        "unsharedByFamily": {
            name: {
                side: dict(sorted(counts.items()))
                for side, counts in sides.items()
            }
            for name, sides in sorted(residuals.items())
        },
        "projects": projects,
    }
    (ROOT / "scoped-accounting.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n"
    )

    lines = [
        "# Scoped differing-project inventory",
        "",
        "Only projects with unequal scoped counts or unshared check/path keys are shown.",
        "Counts are saved reported diagnostics; the TypeSpec column subtracts only the",
        "identified source-population exclusions. Suppressed owning-rule findings and",
        "same-version correspondence remain unassessed. Relative difference is",
        "`abs(Swagger - scoped TypeSpec) / max(Swagger, scoped TypeSpec, 1)`.",
        "In category cells, `S` counts pre-report Swagger callbacks and `T` counts",
        "unshared TypeSpec diagnostics; neither proves corresponding defects.",
        "The linked project entries retain original route, target and cause evidence.",
        "",
        f"Swagger-higher / TypeSpec-higher / equal: **{output['totals']['swaggerHigherProjects']} / "
        f"{output['totals']['typespecHigherProjects']} / {output['totals']['equalCountProjects']}** projects.",
        f"Directional excesses: **{swagger_excess} / {typespec_excess}**; absolute difference "
        f"**{swagger_excess + typespec_excess}**, net Swagger minus TypeSpec **-271**.",
        "",
        "| Project | Swagger | TypeSpec configured | Excluded | TypeSpec scoped | Signed / relative | Remaining unshared check categories |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for p in sorted(different, key=lambda x: (-x["absoluteDifference"], x["project"])):
        categories = []
        for side, key in (
            ("S", "unsharedSwaggerCallbacks"),
            ("T", "unsharedTypespecDiagnostics"),
        ):
            categories.extend(f"{side}: {k} {v}" for k, v in p[key].items())
        description = "; ".join(categories) if categories else "reporting-stage count difference"
        lines.append(
            f"| [{p['project']}](detailed-differences.md#{p['detailAnchor']}) | "
            f"{p['swaggerReported']} | {p['typespecConfiguredTargetOnly']} | "
            f"{p['typespecExcluded']} | {p['typespecScopedObserved']} | "
            f"{p['swaggerMinusTypespec']:+d} / {p['relativeDifference']:.2%} | {description} |"
        )
    lines.extend(
        [
            "",
            "Equal totals do not establish corresponding checks. Excluded-project records,",
            "all 487 project counts and the exact excluded keys are in",
            "[scoped accounting](scoped-accounting.json). The original unfiltered",
            "[difference inventory](detailed-differences.md) preserves every source",
            "target, including projects with only excluded differences.",
            "",
        ]
    )
    (ROOT / "scoped-project-differences.md").write_text(
        "\n".join(lines), encoding="utf-8", newline="\n"
    )
    print(json.dumps(output["totals"], indent=2))


if __name__ == "__main__":
    main()
