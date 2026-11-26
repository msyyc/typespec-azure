import argparse
import collections
import csv
import hashlib
import json
import pathlib
import re

RULE = "@azure-tools/typespec-azure-resource-manager/use-standard-error"
IN_SCOPE = {"structural-default", "strict-identity-default"}


def read(file):
    return json.loads(file.read_text(encoding="utf-8-sig"))


def diagnostic_key(row):
    return (row["rule"], row.get("sourceFile"), row.get("line"), row.get("column"), row["message"])


def source_location_key(row):
    return diagnostic_key(row)[:-1]


def directional_metrics(swagger, native):
    delta = native - swagger
    denominator = max(swagger, native)
    return {
        "signedGapNativeMinusSwagger": delta,
        "absoluteRelativeDifference": abs(delta) / denominator if denominator else 0,
    }


def classify(callback):
    if callback["messageId"] == "missingErrorResponse":
        return "missing-marked-response"
    assert callback["messageId"] == "default", callback
    operation = callback["operation"]
    assert operation, callback
    bad_default = []
    bad_explicit = []
    for variant in operation["variants"]:
        if not variant["markedError"]:
            continue
        for response in variant["responses"]:
            bad = [body for body in response["bodies"] if body["bodyKind"] != "single" or not body["standard"]]
            (bad_default if response["statusCodes"] == "*" else bad_explicit).extend(bad)
    if bad_default:
        return (
            "strict-identity-default"
            if all(body.get("nestedPropertyPresence") for body in bad_default)
            else "structural-default"
        )
    assert bad_explicit, callback
    return "explicit-only-payload"


def tests():
    def item(status, nested=False, standard=False):
        return {"statusCodes": status, "bodies": [{"bodyKind": "single", "standard": standard, "nestedPropertyPresence": nested}]}

    def callback(responses):
        return {"messageId": "default", "operation": {"variants": [{"markedError": True, "responses": responses}]}}

    assert classify({"messageId": "missingErrorResponse"}) == "missing-marked-response"
    assert classify(callback([item("*")])) == "structural-default"
    assert classify(callback([item("*", True)])) == "strict-identity-default"
    assert classify(callback([item(400)])) == "explicit-only-payload"
    assert classify(callback([item("*", True, True), item(400)])) == "explicit-only-payload"
    assert classify(callback([item("*", True), item("*")])) == "structural-default"
    assert diagnostic_key({"rule": RULE, "sourceFile": "a.tsp", "line": 1, "column": 1, "message": "a"}) != diagnostic_key(
        {"rule": RULE, "sourceFile": "a.tsp", "line": 1, "column": 1, "message": "b"}
    )
    assert source_location_key({"rule": RULE, "sourceFile": "a.tsp", "line": 1, "column": 1, "message": "a"}) == source_location_key(
        {"rule": RULE, "sourceFile": "a.tsp", "line": 1, "column": 1, "message": "b"}
    )
    assert [
        directional_metrics(swagger, native)
        for swagger, native in [(0, 0), (0, 2), (4, 1), (1, 4)]
    ] == [
        {"signedGapNativeMinusSwagger": 0, "absoluteRelativeDifference": 0},
        {"signedGapNativeMinusSwagger": 2, "absoluteRelativeDifference": 1},
        {"signedGapNativeMinusSwagger": -3, "absoluteRelativeDifference": 0.75},
        {"signedGapNativeMinusSwagger": 3, "absoluteRelativeDifference": 0.75},
    ]
    print("Nine deterministic accounting controls passed.")


def main(args):
    coverage = read(args.run / "coverage.json")
    assert coverage["selectedProjectCount"] == 490
    assert coverage["assessableProjectCount"] == 490
    assert coverage["unassessedProjects"] == []
    results = {}
    for file in args.run.glob("native-*.json"):
        if re.fullmatch(r"native-\d+\.json", file.name):
            receipt = read(file)
            assert receipt["status"] == "success", file
            assert receipt["project"] not in results
            results[receipt["project"]] = receipt
    assert len(results) == 490
    captures = {}
    for directory in args.captures:
        for file in directory.glob("*.json"):
            if not re.fullmatch(r"\d+\.json", file.name):
                continue
            receipt = read(file)
            assert receipt["status"] == "success", file
            if receipt["project"] in captures:
                previous = captures[receipt["project"]]
                assert collections.Counter(map(diagnostic_key, previous["emitted"])) == collections.Counter(map(diagnostic_key, receipt["emitted"]))
            captures[receipt["project"]] = receipt
    saved_swagger = read(args.swagger)["findings"]
    swagger_by_project = collections.defaultdict(list)
    for finding in saved_swagger:
        swagger_by_project[finding["project"]].append(finding)
    missing_captures = sorted(
        project for project, receipt in results.items()
        if (receipt["rawDiagnostics"] or swagger_by_project[project]) and project not in captures
    )
    if missing_captures:
        print(json.dumps({"missingSupplementalCaptures": missing_captures}, indent=2))
        raise SystemExit(2)
    args.output.mkdir(parents=True, exist_ok=False)
    rows = []
    diagnostic_ledger = []
    correspondence = []
    for project, receipt in sorted(results.items()):
        assert collections.Counter(map(diagnostic_key, receipt["rawDiagnostics"])) == collections.Counter(map(diagnostic_key, receipt["diagnostics"])), project
        families = collections.Counter()
        suppressed = collections.Counter()
        scoped_callbacks = []
        capture = captures.get(project)
        if capture:
            assert collections.Counter(map(diagnostic_key, receipt["rawDiagnostics"])) == collections.Counter(map(diagnostic_key, capture["emitted"])), project
            for callback in capture["captured"]:
                family = classify(callback)
                emitted = callback["emitted"]
                (families if emitted else suppressed)[family] += 1
                operation = callback.get("operation")
                row = {
                    "project": project,
                    **{key: callback.get(key) for key in ["rule", "sourceFile", "line", "column", "message", "messageId"]},
                    "family": family,
                    "inScope": family in IN_SCOPE,
                    "emitted": emitted,
                    "operation": operation,
                    "suppressionDirectives": callback.get("suppressionDirectives", []),
                }
                diagnostic_ledger.append(row)
                if family in IN_SCOPE:
                    scoped_callbacks.append(row)
            assert sum(families.values()) == len(receipt["rawDiagnostics"]), project
        swagger = swagger_by_project[project]
        contexts = collections.defaultdict(list)
        for finding in swagger:
            contexts[(finding["path"][1], finding["path"][2])].append(finding)
        for context, findings in sorted(contexts.items()):
            matching = [
                callback for callback in scoped_callbacks
                if (callback["operation"]["path"], callback["operation"]["verb"]) == context
            ]
            candidates = [] if not capture else [
                operation for operation in capture.get("serviceOperations", capture["operations"])
                if (operation["path"], operation["verb"]) == context
            ]
            source_has_structural_error = any(
                callback["family"] == "structural-default" for callback in matching
            )
            library_gap = not matching and any(
                operation.get("sourceContext") == "library"
                and any(
                    variant["markedError"] and any(
                        response["statusCodes"] == "*" and any(
                            not body.get("nestedPropertyPresence") for body in response["bodies"]
                        ) for response in variant["responses"]
                    ) for variant in operation["variants"]
                ) for operation in candidates
            )
            cause = (
                "saved-and-source-structural-default"
                if source_has_structural_error
                else "library-origin-inherited-operation-gap" if library_gap else "unassessed"
            )
            correspondence.append({
                "project": project,
                "path": context[0],
                "verb": context[1],
                "swaggerRaw": len(findings),
                "swaggerCauses": sorted({finding["observedSchemaCause"] for finding in findings}),
                "sourceAttributions": sorted({finding["sourceAttribution"] for finding in findings}),
                "matchingNativeDiagnostics": [
                    {key: callback[key] for key in ["sourceFile", "line", "column", "family", "emitted"]}
                    for callback in matching
                ],
                "sourceOperationCandidates": candidates,
                "cause": cause,
                "identityLimit": "Exact project/path/verb context plus separately inspected schema and source predicates; not an equivalent-defect or exact originating-file identity.",
            })
        scoped_emitted = sum(families[family] for family in IN_SCOPE)
        scoped_suppressed = sum(suppressed[family] for family in IN_SCOPE)
        scoped = scoped_emitted + scoped_suppressed
        delta = len(swagger) - scoped
        rows.append({
            "project": project,
            "apiVersion": next(item.get("apiVersion") for item in coverage["projects"] if item["project"] == project),
            "swaggerRaw": len(swagger),
            "swaggerOccurrenceKeys": len({
                (finding["swaggerFile"], json.dumps(finding["path"])) for finding in swagger
            }),
            "swaggerFileIndependentKeys": len({json.dumps(finding["path"]) for finding in swagger}),
            "swaggerContextKeys": len(contexts),
            "nativeConfiguredRaw": len(receipt["rawDiagnostics"]),
            "nativeSourceKeys": len({source_location_key(finding) for finding in receipt["rawDiagnostics"]}),
            "nativeScopedEmitted": scoped_emitted,
            "nativeScopedCapturedSuppressed": scoped_suppressed,
            "nativeScopedObserved": scoped,
            "nativeStructuralDefault": families["structural-default"] + suppressed["structural-default"],
            "nativeStrictIdentityDefault": families["strict-identity-default"] + suppressed["strict-identity-default"],
            "excludedMissingMarkedResponse": families["missing-marked-response"],
            "excludedExplicitOnlyPayload": families["explicit-only-payload"],
            "suppressionInspected": capture is not None,
            "signedGapSwaggerMinusNative": delta,
            **directional_metrics(len(swagger), scoped),
            "absoluteGap": abs(delta),
            "relativeGapToSwagger": delta / len(swagger) if swagger else None,
            "relativeGapZeroDenominator": bool(not swagger and scoped),
        })
    sums = {
        key: sum(row[key] for row in rows)
        for key in [
            "swaggerRaw", "swaggerOccurrenceKeys", "swaggerFileIndependentKeys", "swaggerContextKeys",
            "nativeConfiguredRaw", "nativeSourceKeys", "nativeScopedEmitted", "nativeScopedCapturedSuppressed",
            "nativeScopedObserved", "nativeStructuralDefault", "nativeStrictIdentityDefault",
            "excludedMissingMarkedResponse", "excludedExplicitOnlyPayload",
        ]
    }
    assert sums["swaggerRaw"] == coverage["validatorRawCount"] == 762
    assert sums["nativeConfiguredRaw"] == coverage["nativeRawCount"]
    assert sums["nativeSourceKeys"] == coverage["nativeSourceCount"]
    assert sums["nativeConfiguredRaw"] == sums["nativeScopedEmitted"] + sums["excludedMissingMarkedResponse"] + sums["excludedExplicitOnlyPayload"]
    assert sums["nativeScopedObserved"] == sums["nativeStructuralDefault"] + sums["nativeStrictIdentityDefault"]
    assert len(correspondence) == sums["swaggerContextKeys"]
    aggregate = {
        "scope": "Full490 source-program emitted diagnostics, mixed-check semantic attribution; captured suppression restricted to named inspected projects.",
        "totals": sums,
        "selectedProjects": 490,
        "suppressionInspectedProjects": sorted(captures),
        "swaggerProjects": sum(row["swaggerRaw"] > 0 for row in rows),
        "nativeRawProjects": sum(row["nativeConfiguredRaw"] > 0 for row in rows),
        "nativeScopedProjects": sum(row["nativeScopedObserved"] > 0 for row in rows),
        "scopedOverlapProjects": sum(row["swaggerRaw"] > 0 and row["nativeScopedObserved"] > 0 for row in rows),
        "swaggerOnlyScopedProjects": [row["project"] for row in rows if row["swaggerRaw"] > 0 and row["nativeScopedObserved"] == 0],
        "nativeOnlyScopedProjects": [row["project"] for row in rows if row["swaggerRaw"] == 0 and row["nativeScopedObserved"] > 0],
        "projectsSwaggerHigher": sum(row["signedGapSwaggerMinusNative"] > 0 for row in rows),
        "projectsNativeHigher": sum(row["signedGapSwaggerMinusNative"] < 0 for row in rows),
        "projectsEqual": sum(row["signedGapSwaggerMinusNative"] == 0 for row in rows),
        "swaggerDirectionalExcess": sum(max(0, row["signedGapSwaggerMinusNative"]) for row in rows),
        "nativeDirectionalExcess": sum(max(0, -row["signedGapSwaggerMinusNative"]) for row in rows),
        "absoluteGapSum": sum(row["absoluteGap"] for row in rows),
        "signedGap": sums["swaggerRaw"] - sums["nativeScopedObserved"],
        "signedGapNativeMinusSwagger": sums["nativeScopedObserved"] - sums["swaggerRaw"],
        "correspondenceCauses": dict(collections.Counter(row["cause"] for row in correspondence)),
        "sourceIntegrity": {
            "coverageSha256": hashlib.sha256((args.run / "coverage.json").read_bytes()).hexdigest(),
            "swaggerDetailsSha256": hashlib.sha256(args.swagger.read_bytes()).hexdigest(),
        },
    }
    assert aggregate["signedGap"] == aggregate["swaggerDirectionalExcess"] - aggregate["nativeDirectionalExcess"]
    for name, value in [
        ("assessment.json", aggregate),
        ("project-accounting.json", rows),
        ("diagnostic-ledger.json", diagnostic_ledger),
        ("swagger-correspondence.json", correspondence),
    ]:
        (args.output / name).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8", newline="\n")
    with (args.output / "project-accounting.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps(aggregate, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--run", type=pathlib.Path)
    parser.add_argument("--swagger", type=pathlib.Path)
    parser.add_argument("--captures", type=pathlib.Path, nargs="+")
    parser.add_argument("--output", type=pathlib.Path)
    arguments = parser.parse_args()
    tests()
    if not arguments.self_test:
        main(arguments)
