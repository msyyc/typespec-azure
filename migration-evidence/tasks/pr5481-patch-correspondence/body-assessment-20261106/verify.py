import collections
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REPO = ROOT.parents[2]
PREFIX = "@azure-tools/typespec-azure-resource-manager/"
RULES = ["arm-resource-patch", "use-model-request-body", "use-application-json-content-type"]


def read(file):
    return json.loads(Path(file).read_text(encoding="utf-8-sig"))


def digest(file):
    return hashlib.sha256(Path(file).read_bytes()).hexdigest()


def write(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def sanitize(value):
    if isinstance(value, dict):
        return {key: sanitize(item) for key, item in value.items()}
    if isinstance(value, list):
        return [sanitize(item) for item in value]
    if isinstance(value, str):
        return value.replace(str(REPO), "<evidence>").replace(
            r"C:\dev\worktrees\specs-pr5481-native-coverage", "<specs>"
        )
    return value


def multiset(rows):
    return sorted(json.dumps(row, sort_keys=True) for row in rows)


def check_source_identity(data):
    task = read(ROOT / "refresh-20261105-inherited" / "task.json")
    assert data["candidateCommit"] == task["candidateCommit"]
    assert data["specsCommit"] == task["specsCommit"]
    provenance = read(
        ROOT / "refresh-20261105-inherited" / "provenance" / "artifact-provenance.json"
    )
    arm = next(item for item in provenance["artifacts"]
               if "azure-tools-typespec-azure-resource-manager-" in item["file"])
    return next(item["sha256"] for item in arm["files"]
                if item["file"] == "package/dist/src/rules/arm-resource-patch-body.js")


def check_fixtures(data):
    collector_sha = check_source_identity(data)
    expected = {}
    for shape in ["scalar", "array", "dictionary", "union"]:
        for verb in ["put", "patch"]:
            expected[f"{verb}-{shape}"] = (
                f"unsupported{verb.title()}Body",
                0, 1, int(shape == "scalar"), int(verb == "put"),
            )
    for verb in ["put", "patch"]:
        expected[f"{verb}-inherited-dictionary"] = (
            f"unsupported{verb.title()}Body", 0, 0, 0, int(verb == "put")
        )
        expected[f"{verb}-multipart"] = (
            f"unsupported{verb.title()}Body", 0, 0, 1, 1
        )
    expected.update({
        "plain-compatible": ("supported", 0, 0, 0, 0),
        "plain-extra": ("supported", 1, 0, 0, 1),
        "nullable-extra": ("supported", 1, 1, 0, 1),
        "property-reference-extra": ("unsupportedPutBody", 0, 0, 0, 1),
        "patch-property-reference-extra": ("unsupportedPatchBody", 0, 0, 0, 1),
        "property-reference-compatible": ("unsupportedPatchBody", 0, 0, 0, 0),
        "plain-inherited-compatible": ("supported", 0, 0, 0, 0),
        "nested-collection-compatible": ("supported", 0, 0, 0, 0),
        "nested-collection-incompatible": ("supported", 1, 0, 0, 1),
    })
    assert len(data["results"]) == len(expected) == 21
    assert {item["name"] for item in data["results"]} == set(expected)
    for item in data["results"]:
        native, body = item["native"], item["bodies"]
        assert body["bodyCollectorSha256"] == collector_sha, item["name"]
        assert native["status"] == "success", item["name"]
        assert len(body["pairs"]) == 1
        counts = collections.Counter(row["rule"] for row in native["rawDiagnostics"])
        observed = (
            body["pairs"][0]["bodyCheck"],
            *(counts[PREFIX + rule] for rule in RULES),
            sum(len(row["diagnostics"]) for row in body["swagger"]),
        )
        assert observed == expected[item["name"]], (item["name"], observed)
        assert not [
            row for row in body["emitterDiagnostics"] if row["severity"] == "error"
        ]
        if "union" in item["name"]:
            assert any(row["code"].endswith("/union-unsupported")
                       for row in body["emitterDiagnostics"])
        if body["pairs"][0]["bodyCheck"].startswith("unsupported"):
            predicted = [{
                key: value for key, value in row.items()
                if key in ["rule", "sourceFile", "line", "column"]
            } for row in body["pairs"][0].get("ownerPredicates", [])]
            observed_owners = [{
                key: value for key, value in row.items()
                if key in ["rule", "sourceFile", "line", "column"]
            } for row in native["rawDiagnostics"] if row["rule"] != PREFIX + RULES[0]]
            assert multiset(predicted) == multiset(observed_owners), item["name"]
    return {"cases": len(expected), "status": "passed"}


def check_inventory(data):
    collector_sha = check_source_identity(data)
    projects = data["results"]
    assert data["projects"] == len(projects) == 487
    assert len({item["project"] for item in projects}) == 487
    statuses = collections.Counter()
    root_kinds = collections.Counter()
    excluded_roots = []
    reference_roots = 0
    inherited_only_indexers = 0
    warnings = 0
    for item in projects:
        assert item["bodyCollectorSha256"] == collector_sha, item["project"]
        original = HERE.joinpath(*item["originalReceipt"].split("/")).resolve()
        assert original.is_relative_to(REPO)
        assert digest(original) == item["originalReceiptSha256"], original
        receipt = read(original)
        assert receipt["project"] == item["project"]
        assert receipt["status"] == "success"
        assert multiset(receipt["rawDiagnostics"]) == multiset(item["rawDiagnostics"])
        assert item["diagnosticMultisetMatches"] is True
        assert item["configuredWarnings"] == len(item["rawDiagnostics"])
        warnings += len(item["rawDiagnostics"])
        statuses.update(pair["bodyCheck"] for pair in item["pairs"])
        for index, pair in enumerate(item["pairs"]):
            for verb in ["put", "patch"]:
                body = pair[verb]
                if body.get("state") == "absent":
                    root_kinds["absent"] += 1
                    continue
                root_kinds[f'{body["kind"]}/{body["bodyKind"]}'] += 1
                reference_roots += body["kind"] == "ModelProperty"
                inherited_only_indexers += bool(
                    body["indexers"] and body["type"] not in body["indexers"]
                )
                if body["type"] != "void" and (
                    body["bodyKind"] != "single" or not body["objectBody"]
                ):
                    excluded_roots.append({
                        "project": item["project"], "pairIndex": index,
                        "route": pair["route"], "verb": verb, **body,
                    })
    assert warnings == 117
    assert dict(statuses) == data["bodyChecks"]
    assert data["elapsedSeconds"] < data["budgetSeconds"] == 2700
    return {
        "projects": len(projects),
        "projectsWithPairs": sum(bool(item["pairs"]) for item in projects),
        "pairedRouteContexts": sum(statuses.values()),
        "bodyChecks": dict(statuses),
        "requestBodyKinds": dict(root_kinds),
        "guardExcludedRoots": excluded_roots,
        "modelPropertyReferenceRoots": reference_roots,
        "inheritedOnlyIndexerRoots": inherited_only_indexers,
        "configuredPatchWarnings": warnings,
        "unsupportedRouteContexts": sum(
            value for key, value in statuses.items() if key.startswith("unsupported")
        ),
        "diagnosticMultisetsEqualFrozenRun": True,
    }


def check_owners(data):
    collector_sha = check_source_identity(data)
    inventory = read(HERE / "inventory.json")
    expected_projects = {
        item["project"] for item in inventory["summary"]["guardExcludedRoots"]
    }
    assert {item["project"] for item in data["results"]} == expected_projects
    assert len(data["results"]) == 2
    assert data["explicitRuleProfile"] == [PREFIX + rule for rule in RULES]
    assert data["elapsedSeconds"] < data["budgetSeconds"] == 240
    events = 0
    for item in data["results"]:
        original = HERE.joinpath(*item["originalReceipt"].split("/")).resolve()
        assert original.is_relative_to(REPO)
        assert digest(original) == item["originalReceiptSha256"]
        native, body = item["native"], item["bodies"]
        assert native["status"] == "success"
        assert body["bodyCollectorSha256"] == collector_sha
        assert multiset(native["rawDiagnostics"]) == multiset(body["rawDiagnostics"])
        patch = [row for row in native["rawDiagnostics"]
                 if row["rule"] == PREFIX + RULES[0]]
        assert multiset(patch) == multiset(read(original)["rawDiagnostics"])
        assert len(item["expectedOwnerEvents"]) == 1
        for event in item["expectedOwnerEvents"]:
            assert event["rule"] == PREFIX + "use-model-request-body"
            assert any(all(row.get(key) == event.get(key) for key in
                           ["rule", "sourceFile", "line", "column"])
                       for row in native["rawDiagnostics"]), event
            events += 1
    return {"projects": 2, "skippedContextOwnerWarnings": events,
            "patchWarningMultisetsUnchanged": True}


if __name__ == "__main__":
    mode, *arguments = sys.argv[1:]
    if mode == "publish-fixtures":
        runs = [read(Path(directory) / "results.json") for directory in arguments]
        results = [item for run in runs for item in run["results"]]
        for item in results:
            source = Path(item["native"]["project"]) / "main.tsp"
            assert source.read_text(encoding="utf-8") == item["source"]
        data = {
            "scope": "Synthetic unversioned ARM-provider pairs; not production prevalence or corpus gains.",
            "candidateCommit": runs[0]["candidateCommit"],
            "specsCommit": runs[0]["specsCommit"],
            "explicitFixtureRuleProfile": [PREFIX + rule for rule in RULES],
            "countBoundary": "Owner warnings are separate from the117-warningPATCH-only corpus.",
            "swaggerBoundary": "Actual resolved fixture emission and pinned predicate returns, not Spectral-reported real-service counts. Union emission warns and falls back to{}; do not claim union-schema equivalence.",
            "runs": [{key: value for key, value in run.items() if key != "results"}
                     for run in runs],
            "results": results,
        }
        check_fixtures(data)
        write("fixtures.json", sanitize(data))
        print(json.dumps(check_fixtures(read(HERE / "fixtures.json"))))
    elif mode == "publish-inventory":
        data = read(Path(arguments[0]) / "results.json")
        for item in data["results"]:
            item["localOriginalReceiptSha256"] = item["originalReceiptSha256"]
            original = HERE.joinpath(*item["originalReceipt"].split("/")).resolve()
            item["originalReceiptSha256"] = digest(original)
            item["localNativeReceiptSha256"] = item.pop("nativeReceiptSha256")
        summary = check_inventory(data)
        data["summary"] = summary
        data["hashBoundary"] = (
            "originalReceiptSha256 identifies the linked published frozen receipt; "
            "local* hashes preserve the unsanitized execution receipt identities."
        )
        write("inventory.json", sanitize(data))
        print(json.dumps(check_inventory(read(HERE / "inventory.json"))))
    elif mode == "publish-owners":
        data = read(Path(arguments[0]) / "results.json")
        check_owners(data)
        write("owner-probes.json", sanitize(data))
        print(json.dumps(check_owners(read(HERE / "owner-probes.json"))))
    elif mode == "check":
        fixtures = check_fixtures(read(HERE / "fixtures.json"))
        inventory_data = read(HERE / "inventory.json")
        inventory = check_inventory(inventory_data)
        assert inventory_data["summary"] == inventory
        owners = check_owners(read(HERE / "owner-probes.json"))
        print(json.dumps({"fixtures": fixtures, "inventory": inventory,
                          "owners": owners}, indent=2))
    else:
        raise ValueError(f"Unknown mode: {mode}")
