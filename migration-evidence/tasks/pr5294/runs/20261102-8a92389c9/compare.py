import collections
import json
import pathlib
import sys

before_path, after_path, output_path = map(pathlib.Path, sys.argv[1:4])
before = {p["project"]: p for p in json.loads(before_path.read_text())}
after = {p["project"]: p for p in json.loads(after_path.read_text())}
assert set(before) == set(after), "Project populations differ."
differences = []
for project in sorted(before):
    assert before[project]["status"] == after[project]["status"] == "success", project
    for field in ["rawDiagnostics", "diagnostics"]:
        original = collections.Counter(json.dumps(d, sort_keys=True) for d in before[project][field])
        current = collections.Counter(json.dumps(d, sort_keys=True) for d in after[project][field])
        if original != current:
            differences.append({
                "project": project,
                "field": field,
                "removed": [{"diagnostic": json.loads(key), "occurrences": count} for key, count in (original - current).items()],
                "added": [{"diagnostic": json.loads(key), "occurrences": count} for key, count in (current - original).items()],
            })
result = {
    "comparisonUnit": "per-project exact diagnostic JSON multiset, including rule/message/sourceFile/line/column and duplicate multiplicity; no fuzzy matching",
    "projects": len(before),
    "beforeRaw": sum(len(p["rawDiagnostics"]) for p in before.values()),
    "afterRaw": sum(len(p["rawDiagnostics"]) for p in after.values()),
    "beforeAligned": sum(len(p["diagnostics"]) for p in before.values()),
    "afterAligned": sum(len(p["diagnostics"]) for p in after.values()),
    "changedProjects": len({d["project"] for d in differences}),
    "differences": differences,
}
output_path.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
