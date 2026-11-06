"""Apply explicit, evidence-backed policy decisions without changing correspondence credit."""

import argparse
import collections
import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parent
COLLECTION_COMPARISONS = {
    "a4753c8793120f98", "932685760e4abb70", "96597104b5cfbfbf", "2d6708f576319f69",
}
REQUEST_COLLECTIONS = {"43582b9e61743914", "e44a5097b4b0fd88"}
REQUEST_COMMANDS = {"7375fbc9fd2cdf33", "4f6894b5bb1a95e3"}
PARENT_COMPARISONS = {"9eca5628f4dd299e", "e7c4ffbd689792f0", "86cde2d203ba3710"}
SYNC_JOB = "e3d27963b9f80e88"
POLYMORPHIC_REQUEST = "4de3358332155e13"

DECISIONS = {
    "corroborated": (
        "Corresponding implemented check", "Keep",
        "No rule change for this observed pairing; retain compliant and violating controls.",
    ),
    "recover-registered-put": (
        "Worthwhile request traversal gap", "P1: small native change",
        "Enumerate getArmResourceOperationList for each already-registered resource; select createOrUpdate PUTs, "
        "reuse the existing request predicate and deduplicate Operation targets. This avoids a broad PUT listener "
        "and shared registry redesign. The probe verifies reachability and the canonical selected response, not post-fix warning counts.",
    ),
    "custom-lifecycle-registration": (
        "Custom lifecycle registration/modeling gap", "P2: spec/template triage",
        "The PUT is absent from every registered resource's operation Set, despite a registered selected response. "
        "Review the low-level/custom template or its resource argument before adding explicit lifecycle registration. "
        "Verify emitted paths, operation IDs and wire schemas do not change; do not infer a canonical model from HTTP PUT alone. "
        "The separate three-decorator follow-up is Azure/azure-rest-api-specs#47952; its modified specs are not frozen-corpus coverage.",
    ),
    "upstream-identity-bug": (
        "Confirmed Swagger false positive", "Do not port",
        "Identical 200/201 references were compared by resolved JavaScript object identity. "
        "Do not reproduce this bug or count its absence as a missing useful diagnostic.",
    ),
    "existing-success-schema-owner": (
        "Genuine schema difference with an existing native owner", "P2: owner/suppression review",
        "Quota deliberately models a quota resource at 200 and a submission-status envelope at 201. "
        "Azure Core response-schema-problem already compares non-error success payload identities; the source explicitly suppresses it. "
        "Use that owner and review the legacy-contract exception instead of adding a duplicate ARM warning. "
        "The final LRO result is separately modeled as the quota resource; initial-envelope and final-result policies are different.",
    ),
    "response-resource-policy": (
        "Unpaired native response-resource comparison", "P2: inspect exact native correspondence",
        "The consolidated native resource-response check has no proven corresponding diagnostic here. "
        "Inspect resolver exposure, selected status, native declaration metadata, source/latest-version body identity "
        "and actual callbacks before suppression. Do not infer native resource identity from emitted extensions "
        "or invent credit from an unrelated warning.",
    ),
    "native-resource-representation": (
        "Native resource identity differs from emitted marker presence", "Keep native semantics",
        "The exact selected source body is a declared native resource, while frozen Swagger lacks its marker. "
        "Native ARM registration, resource-base ancestry and explicit custom declarations establish identity; "
        "custom emission flags and OpenAPI overrides do not change it. This is an intentional representation "
        "difference, not a diagnosed native violation or proof of marker-level equivalence.",
    ),
    "resolver-operation-gap": (
        "Marked PUTs on non-ARM targets are omitted by the resolver", "API/modeling prerequisite; no fallback",
        "Ten Microsoft.Network interface PUTs have non-resource selected bodies and action metadata targeting models "
        "without ARM resource declarations. They are project-owned in an ARM namespace, but appear in neither resolved "
        "resources nor providerOperations: the resource scan cannot discover their targets, while provider enumeration "
        "excludes marked operations. Exact-head and three minimal marked/unmarked controls confirm the mechanism. "
        "Azure/typespec-azure#5995 requests explicit prerequisite diagnostics or an unresolved-operation representation; "
        "do not promote DTOs into resources or bypass the resolver. This differs from #5994's registered-model "
        "LIST/PATCH-only omission and #5899's split identities.",
    ),
    "standalone-operation-prerequisite": (
        "Standalone PUT is outside required ARM interface authoring", "Fix authoring prerequisite",
        "The selected non-resource body belongs to a standalone operation. resolveArmResources does not expose it, "
        "and use-interface owns the interface requirement. That prerequisite is not credited as a diagnostic of the "
        "response-body predicate. Move the operation into compliant ARM authoring before assessing that predicate; "
        "do not add a direct HTTP-enumeration fallback.",
    ),
    "body-policy-owner": (
        "Empty 200: real response-body issue, not two unequal payload models", "P2: existing owner/spec fix",
        "Keep schema consistency separate from response existence. Review no-response-body and authored suppressions, "
        "and repair the spec only against the actual wire contract. Its current implementation checks the first ordinary response "
        "and skips some template operations; source ownership alone is not measured coverage. "
        "The focused owner-predicate results are linked in gap-analysis.md.",
    ),
    "bodyless-comparator-overreach": (
        "Swagger schema-comparison false positive / policy overreach", "Recommend not porting",
        "The comparison treats a correctly bodyless 202 or 204 as an unequal resource schema. "
        "Do not invent a response body or add a resource-schema warning merely to match that result. "
        "This does not establish that the operation's status set is ARM-compliant: arm-put-response-codes owns that separate question. "
        "This is a recommended intentional difference, not approved retirement or existing migration credit.",
    ),
    "collection-comparator-overreach": (
        "Swagger collection-shape comparison false positive", "Recommend not porting",
        "The compared payloads are an entity/array/list-envelope role difference, not evidence of different resource item models. "
        "The saved schemas show matching item identity. Keep list envelope/item validation separate; "
        "do not compare wrapper reference names across collection and item-like methods. "
        "This recommendation is not approved retirement or existing migration credit.",
    ),
    "custom-collection-request": (
        "Bulk/collection request contract, not ordinary resource replacement", "Defer blanket equality",
        "Annotations creates an item but returns an array; FirewallRules_Replace supplies a list to a collection operation. "
        "These shapes are not automatically equivalent, but HTTP PUT alone does not establish a single-resource replacement contract. "
        "Require spec-owner intent before extending the canonical-resource rule; do not claim these are confirmed compliant APIs.",
    ),
    "custom-command-request": (
        "Action-like PUT contract", "Defer blanket equality",
        "Gateway API association and storage migration use command/association inputs rather than the parent resource model. "
        "GatewayApi is registered as action, has a different ApiContract response and explicitly suppresses the current ARM rule. "
        "Do not compare its input to the Gateway parent simply because its verb is PUT. "
        "Review API design and justified exceptions separately rather than widening this resource listener.",
    ),
    "unregistered-entity-request": (
        "Unregistered body-bearing request/response mismatch", "P2: contract/modeling investigation",
        "The differing request and response are observable, but no registered canonical resource is established. "
        "ExportConfiguration, TestJob, ConnectionMonitor and PacketCapture need owner review of read-only fields, "
        "visibility and actual contract before a modeling repair. These are four checked PUTs, not their repeated raw finding total. "
        "Do not add a generic recursive schema comparator for these legacy DTOs.",
    ),
    "parent-canonical-association": (
        "Canonical parent differs from the actual child/result response", "P2: spec/template modeling review",
        "ApiManagement PrivateEndpointConnection uses ApiManagementServiceResource as the legacy resource argument; "
        "RecoveryServices certificate uses Vault but returns VaultCertificateResponse. "
        "The complete registered-alias graph also exposes SyncJob.create as a read association of SourceControl, "
        "not an eligible create/update association for the SyncJob result. Existing canonical warnings compare to "
        "the parent, not the original request/result or SyncJob PUT/GET pair. "
        "Review child-resource/custom-operation modeling and preserve wire behavior; an extra equality warning is not the first fix.",
    ),
    "cross-method-entity-contract": (
        "Genuine PUT/GET resource-shape difference", "P3: spec-owner follow-up; defer broad matcher",
        "SyncJob's PUT response has read-only name/type/id; GET has writable id, omits name/type, and adds nested exception. "
        "These are not merely differently named aliases. Establish whether the wire contract should share a model; "
        "do not rewrite the spec if the service intentionally returns a summary versus detail. "
        "One observed route does not justify a general recursive, version/visibility-aware cross-operation structural comparator.",
    ),
    "supported-polymorphism": (
        "Deliberate polymorphism with unresolved canonical request association", "Preserve hierarchy; assess registration",
        "ThreatIntelligenceIndicatorModel derives from the kind-discriminated ThreatIntelligenceInformation response base. "
        "The generic response predicate accepts discriminated ancestor/descendant resources, but the request predicate "
        "still requires effective identity with the declared canonical resource. The frozen PUT is unassociated, "
        "so its absent request warning is not observed request-polymorphism acceptance. Preserve the intended hierarchy "
        "and establish the canonical resource before changing registration; do not claim corresponding warning parity "
        "or rewrite the DTOs merely to satisfy strict identity.",
    ),
}


def selected_empty_200(group):
    for operation in group["swaggerOperations"]:
        status = next((s for s in ("200", "201", "202") if s in operation["responses"]), None)
        if status == "200" and operation["responses"][status] is None:
            return True
    return False


def has_bodyless_selection(group):
    for operation in group["swaggerOperations"]:
        status = next((s for s in ("200", "201", "202") if s in operation["responses"]), None)
        if status == "202" and operation["responses"][status] is None:
            return True
        if status is None and operation["responses"].get("204", False) is None:
            return True
        if status is None:
            for binding in group.get("typeSpecSelectedBindings", []):
                for selected in binding["operations"]:
                    if selected["verb"] != operation["verb"]:
                        continue
                    if any(
                        response["statusCodes"] == 204 and not any(response["bodies"])
                        for response in selected["responses"]
                    ):
                        return True
    return False


def decision_for(group, registry):
    classification = group["classification"]
    identity = group["id"]
    if group.get("mappedNativePredicateIds") or classification in (
        "mapped-request-mismatch", "mapped-response-mismatch", "mapped-resource-marker", "mapped-resource-response",
    ):
        return "corroborated"
    if identity == POLYMORPHIC_REQUEST:
        return "supported-polymorphism"
    if classification == "upstream-identity-false-positive":
        return "upstream-identity-bug"
    if classification == "missed-200-201-response-equality":
        return "existing-success-schema-owner"
    if classification == "native-resource-without-emitted-marker":
        return "native-resource-representation"
    if classification == "nonresource-response-not-exposed-by-resolver":
        source = [
            operation for binding in group["typeSpecSourceBindings"] for operation in binding["operations"]
        ]
        return (
            "standalone-operation-prerequisite"
            if len(source) == 1 and source[0].get("inInterface") is False
            else "resolver-operation-gap"
        )
    if classification in (
        "missed-emitted-resource-extension-check", "unpaired-native-resource-response-check",
        "native-resource-response-suppressed-or-unresolved",
    ):
        return "response-resource-policy"
    if group["rule"] == "PutGetPatchResponseSchema":
        if identity in COLLECTION_COMPARISONS:
            return "collection-comparator-overreach"
        if identity == SYNC_JOB:
            return "cross-method-entity-contract"
        if selected_empty_200(group):
            return "body-policy-owner"
        assert has_bodyless_selection(group), f"Unassessed cross-method semantics: {identity}"
        return "bodyless-comparator-overreach"
    if selected_empty_200(group):
        return "body-policy-owner"
    if identity in REQUEST_COLLECTIONS:
        return "custom-collection-request"
    if identity in REQUEST_COMMANDS:
        return "custom-command-request"
    if identity in PARENT_COMPARISONS:
        return "parent-canonical-association"
    if identity in registry:
        return "recover-registered-put" if registry[identity]["selectedCanonicalComparison"] else "custom-lifecycle-registration"
    if classification == "missed-request-unregistered-response-operation":
        return "unregistered-entity-request"
    raise AssertionError(f"Unassessed decision: {identity}: {classification}")


def assess(mapping, probes):
    registry = {row["checkId"]: row for row in probes["registry"]["checks"]}
    checks = [
        {
            "checkId": group["id"], "member": group["rule"], "project": group["project"],
            "route": group["route"], "rawObservations": len(group["rawObservationIds"]),
            "decision": decision_for(group, registry),
        }
        for group in mapping["swaggerGroups"]
    ]
    owner_reports = {}
    for group, check in zip(mapping["swaggerGroups"], checks):
        check["mappedWarningIds"] = group.get("mappedNativeFindingIds", [])
        check["mappedPredicateIds"] = group.get("mappedNativePredicateIds", [])
        check["ownerReports"] = []
        check["ownerConfiguredReports"] = []
        owner_rule = {
            "body-policy-owner": "no-response-body",
            "existing-success-schema-owner": "response-schema-problem",
        }.get(check["decision"])
        if not owner_rule:
            owner_rule = next((
                probe["ownerRule"] for probe in probes.get("owners", {}).get("checks", [])
                if probe["checkId"] == check["checkId"]
            ), None)
        if owner_rule:
            keys = {
                operation["operationKey"]
                for binding in group.get("typeSpecSourceBindings", [])
                for operation in binding["operations"]
            }
            reports = {}
            configured_reports = {}
            for probe in probes.get("owners", {}).get("checks", []):
                if probe["project"] != group["project"] or probe["ownerRule"] != owner_rule:
                    continue
                for report in probe["predicateFindingsIgnoringSuppressions"]:
                    if report["operationKey"] not in keys:
                        continue
                    value = {"project": group["project"], **report}
                    identity = json.dumps(value, sort_keys=True)
                    reports[identity] = value
                    owner_reports[identity] = value
                for report in probe.get("configuredFindings", []):
                    if report.get("operationKey") in keys:
                        value = {"project": group["project"], **report}
                        configured_reports[json.dumps(value, sort_keys=True)] = value
            check["ownerReports"] = [reports[key] for key in sorted(reports)]
            check["ownerConfiguredReports"] = [
                configured_reports[key] for key in sorted(configured_reports)
            ]
        check["coverageStatus"] = (
            "corresponding-mapped-warning" if check["mappedWarningIds"]
            else "selected-diagnostic-before-suppression" if check["mappedPredicateIds"]
            else "existing-owner-diagnostic-before-suppression" if check["ownerReports"]
            else "polymorphic-contract-with-unassessed-request-association" if check["decision"] == "supported-polymorphism"
            else "confirmed-upstream-false-positive" if check["decision"] == "upstream-identity-bug"
            else "recommended-non-porting-not-approved" if check["decision"] in (
                "bodyless-comparator-overreach", "collection-comparator-overreach",
            )
            else "intentional-native-serialization-difference" if check["decision"] == "native-resource-representation"
            else "unsupported-standalone-authoring" if check["decision"] == "standalone-operation-prerequisite"
            else "resolver-enumeration-gap" if check["decision"] == "resolver-operation-gap"
            else "unpaired-required-investigation-or-modeling"
        )
    summary = []
    for key, (title, priority, action) in DECISIONS.items():
        rows = [row for row in checks if row["decision"] == key]
        summary.append({
            "decision": key, "title": title, "priority": priority, "recommendation": action,
            "memberChecks": len(rows), "rawObservations": sum(r["rawObservations"] for r in rows),
            "distinctProjectRoutes": len({(r["project"], r["route"]) for r in rows}),
            "members": dict(collections.Counter(r["member"] for r in rows)),
        })
    return {
        "scope": "Evidence-backed dispositions over the measured instance mapping; recommendations do not create correspondence credit or approve unresolved policy changes",
        "memberChecks": len(checks), "rawObservations": sum(r["rawObservations"] for r in checks),
        "decisions": summary, "checks": checks,
        "coverageAccounting": {
            "mappedWarningContexts": sum(bool(check["mappedWarningIds"]) for check in checks),
            "selectedPredicateContexts": sum(bool(check["mappedPredicateIds"]) for check in checks),
            "suppressedSelectedContexts": sum(
                bool(check["mappedPredicateIds"]) and not check["mappedWarningIds"] for check in checks
            ),
            "distinctSelectedDiagnosticCallbacks": len({
                identity for check in checks for identity in check["mappedPredicateIds"]
            }),
            "existingOwnerContexts": sum(bool(check["ownerReports"]) for check in checks),
            "ownerOnlyContexts": sum(
                bool(check["ownerReports"]) and not (check["mappedWarningIds"] or check["mappedPredicateIds"])
                for check in checks
            ),
            "overlappingMappedAndOwnerContexts": sum(bool(check["ownerReports"] and check["mappedWarningIds"]) for check in checks),
            "coveredDiagnosticContexts": sum(
                bool(check["mappedWarningIds"] or check["mappedPredicateIds"] or check["ownerReports"])
                for check in checks
            ),
            "distinctOwnerDiagnosticCallbacks": len(owner_reports),
            "ownerDiagnosticCallbacksByRule": dict(collections.Counter(
                report["rule"] for report in owner_reports.values()
            )),
            "statuses": dict(collections.Counter(check["coverageStatus"] for check in checks)),
            "byMember": {
                member: {
                    "contexts": len(rows),
                    "mappedWarningContexts": sum(bool(row["mappedWarningIds"]) for row in rows),
                    "mappedWarnings": len({identity for row in rows for identity in row["mappedWarningIds"]}),
                    "selectedPredicateContexts": sum(bool(row["mappedPredicateIds"]) for row in rows),
                    "suppressedSelectedContexts": sum(
                        bool(row["mappedPredicateIds"]) and not row["mappedWarningIds"] for row in rows
                    ),
                    "existingOwnerContexts": sum(bool(row["ownerReports"]) for row in rows),
                    "statuses": dict(collections.Counter(row["coverageStatus"] for row in rows)),
                }
                for member in sorted({check["member"] for check in checks})
                for rows in [[check for check in checks if check["member"] == member]]
            },
            "unit": "Original member check contexts, not equivalent defects or raw diagnostic totals. Captured selected-rule and owner callbacks count as diagnostics despite authored suppression; a callback can cover several contexts. Configured raw totals are unchanged.",
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=ROOT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = assess(
        json.loads((args.root / "instance-mapping.json").read_text(encoding="utf-8")),
        json.loads((args.root / "gap-probes.json").read_text(encoding="utf-8")),
    )
    output = args.root / "gap-assessment.json"
    if args.verify:
        assert json.loads(output.read_text(encoding="utf-8")) == result
    else:
        output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"memberChecks": result["memberChecks"], "rawObservations": result["rawObservations"]}))
