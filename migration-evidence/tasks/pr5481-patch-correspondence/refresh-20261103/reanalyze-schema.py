"""Join unchanged Swagger replay classifications to fresh project counts."""
import copy
import hashlib
import json
import pathlib

root = pathlib.Path(__file__).parent
source = root.parent / "staging-comparison/schema-investigation.json"
old = json.loads(source.read_text(encoding="utf-8"))
rows = json.loads((root / "staging-comparison/projects.json").read_text(encoding="utf-8"))
affected = {row["project"]: row for row in rows if row["swaggerReportedDiagnostics"] or row["typeSpecReportedDiagnostics"]}
assert set(affected) == {row["project"] for row in old["projects"]}
assert len(affected) == 336
projects = []
for previous in old["projects"]:
    row = copy.deepcopy(previous)
    current = affected[row["project"]]
    assert row["swaggerReportedDiagnostics"] == current["swaggerReportedDiagnostics"]
    row["typeSpecReportedDiagnostics"] = current["typeSpecReportedDiagnostics"]
    row["swaggerOnly"] = current["swaggerOnly"]
    row["typeSpecOnly"] = current["typeSpecOnly"]
    projects.append(row)
result = {
    "assessment": "Unchanged saved Swagger schema replay, exact project-key join to fresh native counts; no source diagnostic pairing or new Swagger execution.",
    "source": "../staging-comparison/schema-investigation.json",
    "sourceSha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "swaggerInputsPreviouslyReplayed": len(old["inputs"]),
    "affectedProjects": len(projects),
    "projects": projects,
}
(root / "staging-comparison/schema-current-projects.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
one_sided = sorted((row for row in projects if row["swaggerOnly"] or row["typeSpecOnly"]), key=lambda row: row["project"])
schema_only = [row for row in one_sided if row["swaggerOnly"] and row["sameNameDifferentSchemaFindings"] == row["swaggerReportedDiagnostics"]]
lines = [
    "# Fresh one-sided projects and retained Swagger classifications", "",
    "All affected projects are the same 336 projects whose 497 Swagger inputs",
    "were previously replayed. Only native project counts/one-sided flags are",
    "updated here by exact project identity; Swagger evidence is unchanged.",
    "The source replay and hash are recorded in [schema-current-projects.json](schema-current-projects.json).",
    "These are emitted-side reasons, not paired source defects.", "",
    f"Swagger-only projects: {sum(row['swaggerOnly'] for row in one_sided)}; "
    f"TypeSpec-only projects: {sum(row['typeSpecOnly'] for row in one_sided)}.",
    f"Of the Swagger-only projects, {len(schema_only)} have only matching-name schema inequalities.", "",
    "| Project | Swagger | TypeSpec | Same name, unequal schema | Absent leaf name | Absent PATCH body |",
    "| --- | ---: | ---: | ---: | ---: | ---: |",
]
for row in one_sided:
    assert row["sameNameDifferentSchemaFindings"] + row["leafNameAbsentFindings"] + row["missingPatchBodyFindings"] + row["missingPutBodyFindings"] == row["swaggerReportedDiagnostics"]
    lines.append(f"| {row['project']} | {row['swaggerReportedDiagnostics']} | {row['typeSpecReportedDiagnostics']} | {row['sameNameDifferentSchemaFindings']} | {row['leafNameAbsentFindings']} | {row['missingPatchBodyFindings']} |")
(root / "staging-comparison/one-sided-projects.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"affectedProjects": len(projects), "reusedSwaggerInputs": len(old["inputs"]), "swaggerOnlySchemaOnlyProjects": len(schema_only), "schemaOnlyFindings": sum(row["swaggerReportedDiagnostics"] for row in schema_only)}))
