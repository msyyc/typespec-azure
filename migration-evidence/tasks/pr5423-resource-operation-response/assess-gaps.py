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
PARENT_COMPARISONS = {"9eca5628f4dd299e", "e7c4ffbd689792f0"}
SYNC_JOB = "e3d27963b9f80e88"

DECISIONS = {
    "corroborated": (
        "Existing corresponding check", "Keep",
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
        "Verify emitted paths, operation IDs and wire schemas do not change; do not infer a canonical model from HTTP PUT alone.",
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
        "Missing independent response-resource policy", "P2: separate focused rule/design",
        "The selected emitted hierarchy lacks x-ms-azure-resource, and its source payload is not a registered ARM resource. "
        "This is unimplemented policy, not proof that all instances are legitimate resource-contract bugs. "
        "Prefer a focused source-level response-resource check after defining custom/action exceptions; "
        "account for emitter marker state, custom-resource options, explicit extensions and external references. "
        "Do not overload canonical-resource identity or add emitted-JSON equality.",
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
        "ExportConfiguration, TestJob, SyncJob, ConnectionMonitor and PacketCapture need owner review of read-only fields, "
        "visibility and actual contract before a modeling repair. These are five checked PUTs, not their repeated raw finding total. "
        "Do not add a generic recursive schema comparator for these legacy DTOs.",
    ),
    "parent-canonical-association": (
        "Canonical parent differs from the actual child response", "P2: spec/template modeling review",
        "ApiManagement PrivateEndpointConnection uses ApiManagementServiceResource as the legacy resource argument; "
        "RecoveryServices certificate uses Vault but returns VaultCertificateResponse. "
        "Existing request warnings compare to the parent, not the original selected child response. "
        "Review child-resource/custom-operation modeling and preserve wire behavior; an extra equality warning is not the first fix.",
    ),
    "cross-method-entity-contract": (
        "Genuine PUT/GET resource-shape difference", "P3: spec-owner follow-up; defer broad matcher",
        "SyncJob's PUT response has read-only name/type/id; GET has writable id, omits name/type, and adds nested exception. "
        "These are not merely differently named aliases. Establish whether the wire contract should share a model; "
        "do not rewrite the spec if the service intentionally returns a summary versus detail. "
        "One observed route does not justify a general recursive, version/visibility-aware cross-operation structural comparator.",
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
    if classification == "mapped-request-mismatch":
        return "corroborated"
    if classification == "upstream-identity-false-positive":
        return "upstream-identity-bug"
    if classification == "missed-200-201-response-equality":
        return "existing-success-schema-owner"
    if classification == "missed-emitted-resource-extension-check":
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
