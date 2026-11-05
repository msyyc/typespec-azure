import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REPLAY = ROOT / "staging-comparison" / "schema-investigation.json"
PROJECTS = ROOT / "refresh-20261104" / "staging-comparison" / "projects.json"
OUTPUT = Path(__file__).with_name("results.json")
SCHEMA_VALUES = Path(__file__).with_name("schema-values.json")
SCHEMA_EXTRACTOR = Path(__file__).with_name("inspect_gap.mjs")
ANNOTATIONS = {"description", "title"}
DOCUMENTATION = ANNOTATIONS | {"externalDocs"}
OVERCHECKS = {
    "documentation-only-overcheck",
    "default-only-overcheck",
    "input-allowed-mutability-overcheck",
    "read-only-patch-overcheck",
}


def annotation_category(occurrences):
    if not occurrences:
        raise ValueError("A reported schema finding needs every predicate occurrence.")
    flags = []
    for occurrence in occurrences:
        differences = occurrence["differingSchemaKeys"]
        if (
            occurrence["classification"] != "same-name-different-schema"
            or not differences
            or len(differences) != occurrence["sameNamedPutCandidates"]
            or any(not keys for keys in differences)
        ):
            raise ValueError("Incomplete or inconsistent same-name comparison evidence.")
        flags.append(any(set(keys) <= ANNOTATIONS for keys in differences))
    if all(flags):
        return "all-occurrences-annotation-only"
    if any(flags):
        return "mixed-occurrences"
    return "no-annotation-only-candidate"


def schema_gap_category(occurrences):
    if not occurrences:
        raise ValueError("A reported schema finding needs every predicate occurrence.")
    ranks = []
    incompatible_kind = False
    for occurrence in occurrences:
        patch = occurrence["patch"]
        candidates = occurrence["candidates"]
        if not candidates or any(not item["differingKeys"] for item in candidates):
            raise ValueError("Missing or incomplete same-name candidate evidence.")
        candidate_ranks = []
        for candidate in candidates:
            keys = set(candidate["differingKeys"])
            put = candidate["put"]
            if keys <= DOCUMENTATION:
                rank = 1
            elif keys <= DOCUMENTATION | {"default"}:
                rank = 2
            elif keys <= DOCUMENTATION | {"default", "x-ms-mutability"}:
                put_modes = put["mutability"]
                patch_modes = patch["mutability"]
                if put_modes is None:
                    put_modes = ["read", "create", "update"]
                if patch_modes is None:
                    patch_modes = ["read", "create", "update"]
                rank = 3 if (
                    not put["readOnly"] and not patch["readOnly"]
                    and {"create", "update"} <= set(put_modes)
                    and "update" in patch_modes
                ) else 4
            else:
                rank = 4
            candidate_ranks.append(rank)
        ranks.append(min(candidate_ranks))
        incompatible_kind |= bool(patch["type"]) and all(
            item["put"]["type"] and item["put"]["type"] != patch["type"]
            for item in candidates
        )
    rank = max(ranks)
    if rank == 1:
        return "documentation-only-overcheck"
    if rank == 2:
        return "default-only-overcheck"
    if rank == 3:
        return "input-allowed-mutability-overcheck"
    if all(occurrence["patch"]["readOnly"] for occurrence in occurrences):
        return "read-only-patch-overcheck"
    if incompatible_kind:
        return "incompatible-json-kind"
    return "remaining-schema-difference"


def native_family(message):
    if re.fullmatch(
        r"The property '.*' in the PATCH body does not correspond to a property in the PUT body\.",
        message,
    ):
        return "absent-leaf-name"
    if message == "The PATCH request body must contain at least one property.":
        return "empty-patch-body"
    if message == "The PATCH operation must have a request body.":
        return "missing-patch-body"
    raise ValueError(f"Unclassified TypeSpec message: {message!r}")


def key(project, swagger_file, path, message):
    return project, swagger_file, tuple(path), message


def build():
    replay = json.loads(REPLAY.read_text(encoding="utf-8"))
    projects = json.loads(PROJECTS.read_text(encoding="utf-8"))
    values = json.loads(SCHEMA_VALUES.read_text(encoding="utf-8"))
    if (
        values["replaySha256"] != hashlib.sha256(REPLAY.read_bytes()).hexdigest()
        or values["extractorSha256"] != hashlib.sha256(SCHEMA_EXTRACTOR.read_bytes()).hexdigest()
        or values["supplementIdentity"] != replay["supplementIdentity"]
        or values["packages"] != replay["packages"]
        or values["lodashVersion"] != replay["lodashVersion"]
    ):
        raise ValueError("Additional schema-value evidence is not bound to this replay/extractor.")
    value_index = {}
    for record in values["records"]:
        identity = tuple(record[name] for name in (
            "replayInputIndex", "replayOperationIndex", "replayReasonIndex",
        ))
        if identity in value_index:
            raise ValueError("Duplicate schema-value record.")
        value_index[identity] = record["occurrences"]
    used_values = set()
    index = {}
    for input_index, item in enumerate(replay["inputs"]):
        for operation_index, operation in enumerate(item["operations"]):
            entries = []
            if operation["patchBodyParameters"] == 0:
                entries.append(("Patch operations body cannot be empty.", {
                    "family": "missing-patch-body",
                    "annotationCategory": "not-applicable",
                    "gapCategory": "missing-patch-body",
                    "replayReasonIndex": None,
                }))
            elif operation["putBodyParameters"] == 0:
                raise ValueError("Unexpected missing PUT body; inspect its actual message first.")
            for reason_index, reason in enumerate(operation["reasons"]):
                classification = reason["classification"]
                if classification == "same-name-different-schema":
                    family = "same-name-schema-inequality"
                    category = annotation_category(reason["predicateOccurrences"])
                    value_key = input_index, operation_index, reason_index
                    occurrences = value_index[value_key]
                    if [
                        [item["differingKeys"] for item in occurrence["candidates"]]
                        for occurrence in occurrences
                    ] != [
                        occurrence["differingSchemaKeys"]
                        for occurrence in reason["predicateOccurrences"]
                    ]:
                        raise ValueError("Schema values do not match the saved candidate comparisons.")
                    used_values.add(value_key)
                    gap_category = schema_gap_category(occurrences)
                elif classification == "leaf-name-absent-from-put":
                    family = "absent-leaf-name"
                    category = "not-applicable"
                    gap_category = "absent-leaf-name"
                else:
                    raise ValueError(f"Unknown replay classification: {classification}")
                entries.append((reason["message"], {
                    "family": family,
                    "annotationCategory": category,
                    "gapCategory": gap_category,
                    "replayReasonIndex": reason_index,
                }))
            if len(entries) != operation["swaggerReportedDiagnostics"]:
                raise ValueError("Replay classification does not account for every report.")
            for message, entry in entries:
                identity = key(
                    item["project"], item["swaggerFile"],
                    operation["path"] + ["patch", "parameters"], message,
                )
                if identity in index:
                    raise ValueError("Duplicate replay identity; do not silently deduplicate.")
                index[identity] = {
                    **entry,
                    "replayInputIndex": input_index,
                    "replayOperationIndex": operation_index,
                }
    if used_values != set(value_index):
        raise ValueError("Extra or missing schema-value records.")

    seen = Counter()
    swagger_families = Counter()
    native_families = Counter()
    annotations = Counter()
    gap_categories = Counter()
    remaining_keys = Counter()
    rows = []
    for project in projects:
        swagger_records = []
        native_records = []
        for diagnostic_index, diagnostic in enumerate(project["swaggerDiagnostics"]):
            if diagnostic["rule"] != "PatchPropertiesCorrespondToPutProperties":
                raise ValueError("Unexpected Swagger rule.")
            identity = key(
                project["project"], diagnostic["swaggerFile"],
                diagnostic["path"], diagnostic["message"],
            )
            seen[identity] += 1
            entry = index[identity]
            gap_categories[entry["gapCategory"]] += 1
            if entry["gapCategory"] == "remaining-schema-difference":
                occurrences = value_index[(
                    entry["replayInputIndex"], entry["replayOperationIndex"],
                    entry["replayReasonIndex"],
                )]
                remaining_keys[tuple(sorted({
                    field for occurrence in occurrences for candidate in occurrence["candidates"]
                    for field in candidate["differingKeys"]
                }))] += 1
            swagger_families[entry["family"]] += 1
            if entry["family"] == "same-name-schema-inequality":
                annotations[entry["annotationCategory"]] += 1
            swagger_records.append({
                "diagnosticIndex": diagnostic_index,
                **entry,
                "retained": entry["annotationCategory"] != "all-occurrences-annotation-only",
                "retainedAfterMetadataAssessment": entry["gapCategory"] not in OVERCHECKS,
            })
        for diagnostic_index, diagnostic in enumerate(project["typeSpecDiagnostics"]):
            if diagnostic["rule"] != "@azure-tools/typespec-azure-resource-manager/arm-resource-patch":
                raise ValueError("Unexpected TypeSpec rule.")
            family = native_family(diagnostic["message"])
            native_families[family] += 1
            native_records.append({
                "diagnosticIndex": diagnostic_index,
                "family": family,
                "retained": True,
            })
        if (
            len(swagger_records) != project["swaggerReportedDiagnostics"]
            or len(native_records) != project["typeSpecReportedDiagnostics"]
        ):
            raise ValueError("Raw project totals do not match the saved diagnostic arrays.")
        retained = sum(record["retained"] for record in swagger_records)
        metadata_retained = sum(record["retainedAfterMetadataAssessment"] for record in swagger_records)
        rows.append({
            "project": project["project"],
            "swaggerRaw": len(swagger_records),
            "swaggerExcludedAnnotationOnly": len(swagger_records) - retained,
            "swaggerRetained": retained,
            "swaggerExcludedOverchecks": len(swagger_records) - metadata_retained,
            "swaggerAfterMetadataAssessment": metadata_retained,
            "typeSpecRaw": len(native_records),
            "typeSpecRetained": len(native_records),
            "swaggerAssessments": swagger_records,
            "typeSpecAssessments": native_records,
        })
    if seen != Counter({identity: 1 for identity in index}):
        raise ValueError("Replay and raw records do not correspond exactly one-to-one.")
    expected_families = {
        "same-name-schema-inequality": sum(p["sameNameDifferentSchemaFindings"] for p in replay["projects"]),
        "absent-leaf-name": sum(p["leafNameAbsentFindings"] for p in replay["projects"]),
        "missing-patch-body": sum(p["missingPatchBodyFindings"] for p in replay["projects"]),
    }
    if dict(swagger_families) != expected_families:
        raise ValueError("Independent replay project totals disagree with the record-level join.")
    if len({row["project"] for row in rows}) != len(rows):
        raise ValueError("Duplicate project identity.")

    def summary(swagger_field, native_field):
        deltas = [row[native_field] - row[swagger_field] for row in rows]
        return {
            "swagger": sum(row[swagger_field] for row in rows),
            "typeSpec": sum(row[native_field] for row in rows),
            "swaggerHigherProjects": sum(delta < 0 for delta in deltas),
            "typeSpecHigherProjects": sum(delta > 0 for delta in deltas),
            "equalCountProjects": sum(delta == 0 for delta in deltas),
            "swaggerExcess": sum(-delta for delta in deltas if delta < 0),
            "typeSpecExcess": sum(delta for delta in deltas if delta > 0),
            "absoluteProjectGap": sum(abs(delta) for delta in deltas),
        }

    inputs = []
    for path in (REPLAY, PROJECTS, SCHEMA_VALUES, SCHEMA_EXTRACTOR, Path(__file__).resolve()):
        inputs.append({
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        })
    return {
        "inputs": inputs,
        "assessment": (
            "Broader false-positive assessment of original reported records, not a native rerun, "
            "matched service-defect counts, approved behavior retirement or coverage percentage. "
            "Every contributing helper occurrence must have a same-name PUT candidate differing "
            "only in documentation, defaults, or method-appropriate mutability. For mutability "
            "exclusions, neither candidate is read-only, PUT explicitly/default allows create AND "
            "update, and PATCH allows update. All other schema fields must be equal. "
            "Also exclude remaining records only when EVERY contributing PATCH leaf is "
            "explicitly read-only, hence outside PATCH request input. "
            "Retain a mixed record if any occurrence fails. The original description/title-only "
            "assessment is preserved separately as historical narrow accounting. TypeSpec raw "
            "presence/body records remain unchanged; verified suppression credit is reported "
            "separately, not invented as a new configured diagnostic."
        ),
        "identity": (
            "Swagger join: exact project + Swagger file + operation diagnostic path + full message; "
            "every original record occurs once. Published diagnosticIndex is zero-based in the pinned "
            "project diagnostic array; replay indices are zero-based in the pinned replay. "
            "No new target grouping, source-location deduplication or cross-engine pairing."
        ),
        "projectPopulation": len(rows),
        "raw": summary("swaggerRaw", "typeSpecRaw"),
        "retainedAfterAnnotationAssessment": summary("swaggerRetained", "typeSpecRetained"),
        "retainedAfterMetadataAssessment": summary("swaggerAfterMetadataAssessment", "typeSpecRetained"),
        "gapCategories": dict(sorted(gap_categories.items())),
        "remainingSchemaKeyGroups": [
            {"differingKeys": list(keys), "records": count}
            for keys, count in sorted(remaining_keys.items())
        ],
        "swaggerFamilies": dict(sorted(swagger_families.items())),
        "typeSpecFamilies": dict(sorted(native_families.items())),
        "swaggerSchemaAnnotationCategories": dict(sorted(annotations.items())),
        "projectsWithAnnotationOnlyExclusions": sum(row["swaggerExcludedAnnotationOnly"] > 0 for row in rows),
        "projects": rows,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.check:
        if json.loads(OUTPUT.read_text(encoding="utf-8")) != result:
            raise ValueError("Published assessment differs from recomputed results.")
    else:
        OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({name: value for name, value in result.items() if name != "projects"}, indent=2))
