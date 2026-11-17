"""Recount saved observations and their explicit, reviewed scope ledger."""

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def recount(root):
    projects = {}
    observations = {}
    for path in sorted((root / "native-results").glob("native-*.json")):
        result = load(path)
        project = result["project"]
        if project in projects:
            raise ValueError(f"Duplicate project: {project}")
        if result["status"] != "success":
            raise ValueError(f"Unassessed project: {project}")
        projects[project] = result
        for index, diagnostic in enumerate(result["rawDiagnostics"]):
            observations[f"typespec:{project}:{index}"] = ("TypeSpec", project, diagnostic)
    if not projects:
        raise ValueError("No completed project receipts")

    swagger = load(root / "swagger-observations.json")["results"]
    for index, diagnostic in enumerate(swagger):
        project = diagnostic["project"]
        if project not in projects:
            raise ValueError(f"Swagger project is unassessed: {project}")
        observations[f"swagger:{index}"] = ("Swagger", project, diagnostic)

    ledger = load(root / "scope-ledger.json")
    if ledger["assessedProjects"] != len(projects):
        raise ValueError("Project population mismatch")
    rows = ledger["observations"]
    ids = [row["id"] for row in rows]
    if len(set(ids)) != len(ids) or set(ids) != set(observations):
        raise ValueError("Every raw observation needs exactly one scope decision")

    groups = defaultdict(Counter)
    exclusions = Counter()
    counts = defaultdict(Counter)
    for row in rows:
        engine, project, _ = observations[row["id"]]
        if type(row["included"]) is not bool or not row["reason"].strip():
            raise ValueError("Missing explicit inclusion decision or rationale")
        if row["included"]:
            groups[row["group"]][engine] += 1
            counts[project][engine] += 1
        else:
            exclusions[f"{engine}: {row['group']}"] += 1

    totals = Counter()
    for values in counts.values():
        totals.update(values)
    differences = [
        {"project": project, "swagger": counts[project]["Swagger"],
         "typespec": counts[project]["TypeSpec"],
         "swaggerMinusTypeSpec": counts[project]["Swagger"] - counts[project]["TypeSpec"]}
        for project in sorted(projects)
        if counts[project]["Swagger"] != counts[project]["TypeSpec"]
    ]
    return {
        "assessedProjects": len(projects),
        "rawSwagger": len(swagger),
        "rawTypeSpec": sum(len(result["rawDiagnostics"]) for result in projects.values()),
        "includedSwagger": totals["Swagger"],
        "includedTypeSpec": totals["TypeSpec"],
        "swaggerMinusTypeSpec": totals["Swagger"] - totals["TypeSpec"],
        "groups": {
            group: {"swagger": value["Swagger"], "typespec": value["TypeSpec"]}
            for group, value in sorted(groups.items())
        },
        "exclusions": dict(sorted(exclusions.items())),
        "opposingProjectExcess": {
            "swagger": sum(max(0, row["swaggerMinusTypeSpec"]) for row in differences),
            "typespec": sum(max(0, -row["swaggerMinusTypeSpec"]) for row in differences),
        },
        "projectDifferences": differences,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_directory", type=Path)
    args = parser.parse_args()
    print(json.dumps(recount(args.run_directory), ensure_ascii=True, indent=2))
