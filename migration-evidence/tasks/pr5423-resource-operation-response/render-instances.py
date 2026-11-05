"""Render assessed targets; semantic conclusions are explicit, not inferred from totals."""

import argparse
import hashlib
import json
import pathlib
import posixpath
import re
import urllib.parse


ROOT = pathlib.Path(__file__).resolve().parent
REVISION = "2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9"
UPSTREAM = "https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/"
MEMBERS = {
    "PutRequestResponseSchemeArm": (
        "put-request-response-scheme-arm", "put-request-response-scheme",
        "Partial migration: registered createOrUpdate PUT traversal includes legacy and overwritten aliases; custom request/response contracts and response-body exceptions still prevent equivalence.",
        "PUT comparison contexts",
    ),
    "ConsistentResponseSchemaForPut": (
        "consistent-response-schema-for-put", "consistent-response-schema-for-put",
        "Not a complete mapping to this ARM rule. Azure Core already detects the genuine success-schema difference before suppression; the Swagger object-identity bug should not be reproduced.",
        "PUT comparison contexts",
    ),
    "XmsResourceInPutResponse": (
        "xms-resource-in-put-response", "with-xms-resource",
        "Not covered: canonical resource registration does not enforce the selected response's resource marker. Custom/action policy boundaries remain unresolved.",
        "PUT comparison contexts",
    ),
    "PutGetPatchResponseSchema": (
        "put-get-patch-response-schema", "put-get-patch-schema",
        "Not equivalent: registered-resource traversal is narrower than payload consistency. No-content and collection-role comparisons should not be copied literally; the genuine legacy shape difference remains unresolved.",
        "Route comparison contexts",
    ),
}
NATIVE_DIFFERENCES = {
    "additional-missing-request-policy": (
        "Missing-request policy",
        "Additional body-existence check, skipped by the Swagger selector. Review the wire contract/exception; do not invent a body to equalize counts.",
    ),
    "same-operation-different-comparison": (
        "Same operation, different comparison",
        "Canonical parent or selected success body differs from the original comparator. Review resource association/contract; route co-occurrence receives no migration credit.",
    ),
    "source-only-operation-not-in-selected-version": (
        "Source-only version population",
        "Retain the source warning; use supported version-aligned comparison for selected-version parity, not a rule suppression.",
    ),
    "additional-request-check-outside-swagger-200-201-selector": (
        "Outside Swagger 200/201 selector",
        "The registered request policy is broader. Keep this finding separate from migrated 200/201 comparisons; review the independent status-set contract.",
    ),
    "native-only-request-policy-or-schema-identity-unresolved": (
        "Unresolved source/schema comparison",
        "Investigate the exact emitted request/response and canonical identity before deciding whether this is stricter authoring policy or an incorrect warning; do not claim equivalence.",
    ),
}
DIFFERENCES = [
    (
        {"recover-registered-put"}, "Registered PUT traversal", "registered-put-traversal",
        "Small rule change: enumerate existing registered createOrUpdate PUTs; validate before claiming new warnings.",
    ),
    (
        {"body-policy-owner"}, "Empty 200 responses", "existing-policy-exceptions",
        "Review existing no-response-body suppressions/specs; do not duplicate that check.",
    ),
    (
        {"existing-success-schema-owner"}, "Quota success-schema difference", "existing-policy-exceptions",
        "Review the existing Azure Core rule's suppression/legacy exception; do not duplicate it in ARM.",
    ),
    (
        {"upstream-identity-bug"}, "Swagger object-identity bug", "swagger-comparison-artifacts",
        "Confirmed false positives: do not reproduce the bug.",
    ),
    (
        {"bodyless-comparator-overreach", "collection-comparator-overreach"},
        "No-content / collection-role comparisons", "swagger-comparison-artifacts",
        "Recommend not porting misleading schema comparisons; this is not approved retirement or whole-API compliance.",
    ),
    (
        {"response-resource-policy"}, "Independent response-resource policy", "response-resource-policy",
        "Design a focused check with custom/action boundaries; the policy remains unresolved.",
    ),
    (
        {"custom-lifecycle-registration", "custom-collection-request", "custom-command-request",
         "unregistered-entity-request", "parent-canonical-association"},
        "Legacy request/response contracts", "legacy-contracts",
        "Review registration, DTOs and parent/child modeling; do not broaden blindly to every PUT.",
    ),
    (
        {"cross-method-entity-contract"}, "SyncJob PUT/GET shape difference", "legacy-contracts",
        "Confirm the wire contract; prefer a targeted fix and defer a broad structural matcher.",
    ),
]


def difference_rows(assessment, rule=None):
    rows = []
    for identities, title, anchor, action in DIFFERENCES:
        checks = [
            row for row in assessment["checks"]
            if row["decision"] in identities and (rule is None or row["member"] == rule)
        ]
        if checks:
            rows.append({
                "title": title, "anchor": anchor, "action": action,
                "checks": len(checks), "raw": sum(row["rawObservations"] for row in checks),
            })
    return rows
CAUSES = {
    "missed-request-registered-response-operation-absent-from-map": (
        "Registered response without a canonical createOrUpdate association",
        "The response body is registered, but this PUT has no retained map or eligible operation-Set association. "
        "The fixed request traversal cannot infer a canonical resource from the response alone.",
        "Review custom lifecycle registration and resource arguments rather than adding a global PUT scan.",
    ),
    "missed-request-outside-lifecycle-map": (
        "PUT lacks eligible createOrUpdate registration",
        "A name-keyed list association does not establish semantic createOrUpdate registration. "
        "The fixed request branch selects the actual operation identifier kind, not its retained map key.",
        "Do not treat action registrations as resource replacement; investigate the intended operation/resource contract.",
    ),
    "missed-request-unregistered-response-operation": (
        "Unassociated PUT with no registered response model",
        "The source HTTP graph contains the PUT, but it has no retained resource association and no registered response body. "
        "Inherited ARM-shaped models alone do not satisfy getArmResource.",
        "Separate legacy entity contracts, collections, commands and empty-body issues before recommending any source change.",
    ),
    "same-operation-different-comparison": (
        "Warning on the same operation compares a different contract",
        "The TypeSpec request warning is real, but its canonical resource or selected response status/body differs from the original comparison. "
        "It is not credited merely because the HTTP operation is identical.",
        "Review parent/child modeling or the response-body owner; a warning on the route is not equivalent coverage.",
    ),
    "source-canonical-request-agrees-emitted-schemas-differ": (
        "Canonical request is accepted while selected 200 has no schema",
        "The request is exactly the registered resource, so TypeSpec accepts it. The original chooses the existing 200 response even without a schema, "
        "then compares the request against an empty schema instead of falling back to 201.",
        "Use the existing response-body owner and review its authored suppression instead of duplicating an empty-body schema warning.",
    ),
    "upstream-identity-false-positive": (
        "Upstream staging object-identity false positive",
        "Raw 200 and 201 references are identical in the same invoking document. The original uses !== on resolved JavaScript objects, not structural equality. "
        "This classification uses saved references and pinned code, not a newly captured resolver-object execution trace.",
        "No TypeSpec rule update required: intentionally do not reproduce the upstream identity bug.",
    ),
    "missed-200-201-response-equality": (
        "Genuine plain-response 200/201 mismatch",
        "Quota returns CurrentQuotaLimitBase for 200 and QuotaRequestSubmitResponse201 for 201. Only the canonical registered resource is a response candidate; "
        "the plain nonresource 201 body is ignored.",
        "Azure Core response-schema-problem already detects this difference before the authored suppression; do not add a duplicate ARM check.",
    ),
    "missed-emitted-resource-extension-check": (
        "Selected PUT response lacks resource extension",
        "Every selected response here has xmsResourceInHierarchy=false after reference/allOf traversal. "
        "The TypeSpec rule has no independent extension or equivalent response-resource check; an incidental request warning is not coverage.",
        "Design a focused source-level response-resource policy with explicit custom/action boundaries; no emitted-JSON equality or automatic false-positive classification.",
    ),
    "missed-cross-operation-selected-ref-absent": (
        "Cross-operation comparison includes an absent selected response reference",
        "The original picks the first existing 200/201/202 response and reads schema.$ref. It can obtain undefined for an empty response, "
        "an inline schema, or an operation without those statuses. The resource traversal does not compare this value across methods.",
        "Distinguish correct no-content responses, inline collections and genuinely missing 200 bodies; their recommendations differ.",
    ),
    "missed-cross-operation-distinct-response-refs": (
        "Cross-operation comparison has distinct selected references",
        "The original compares reference names, including resource-versus-list-wrapper responses at collection routes. "
        "The retained TypeSpec rule instead checks supported registered resource candidates. Wrapper/list-item equivalence is not reference-name equality.",
        "Distinguish equivalent collection items from the genuine SyncJob shape difference before deciding whether a new comparator is worthwhile.",
    ),
}


def code(value):
    return "`" + str(value).replace("|", "\\|").replace("`", "'") + "`"


def project_anchor(project):
    return "p-" + hashlib.sha256(project.encode()).hexdigest()[:12]


def source_link(project, operation):
    file = posixpath.normpath(project + "/" + operation["sourceFile"])
    url = f"https://github.com/msyyc/azure-rest-api-specs/blob/{REVISION}/{urllib.parse.quote(file)}#L{operation['line']}"
    return f"[{operation['operation']}]({url})"


def schema_name(schema):
    if schema is None:
        return "(no schema)"
    return schema["raw"].get("$ref") or json.dumps(schema["raw"], sort_keys=True)


def source_operations(group):
    return [op for binding in group["typeSpecSourceBindings"] for op in binding["operations"]]


def render_group(lines, group, native, assessments):
    cause = CAUSES[group["classification"]]
    decision_id = assessments[group["id"]]["decision"]
    _, title, anchor, action = next(row for row in DIFFERENCES if decision_id in row[0])
    lines.extend([
        f'<a id="s-{group["id"]}"></a>',
        f'### {group["rule"]}: {group["swaggerOperations"][0].get("operationId", group["id"])}',
        "",
        f'**Identity:** {code(group["id"])}; {code(group["route"])}.',
        f'**Swagger document:** {code(group["document"])}.',
        f'**Observed comparison:** {cause[0]}.',
        "",
        "| Engine | Observed findings on this target |",
        "| --- | --- |",
        f'| Swagger linter | {len(group["rawObservationIds"])} raw observations; one member check |',
        f'| TypeSpec linter | {len(group["sameOperationNativeFindingIds"])} same-operation findings; '
        f'{len(group["mappedNativeFindingIds"])} credited to this comparison |',
        "",
        "| Method / Swagger operation | Request schema | Success response schemas |",
        "| --- | --- | --- |",
    ])
    for operation in group["swaggerOperations"]:
        responses = "; ".join(f"{status}: {schema_name(schema)}" for status, schema in operation["responses"].items())
        lines.append(
            f'| {code(operation["verb"])} {code(operation.get("operationId"))} | '
            f'{code(schema_name(operation.get("request")))} | {code(responses or "(no selected status)")} |'
        )
    lines.extend(["", "| TypeSpec operation | Effective request | Canonical association / request checked | Registered return candidates |",
                  "| --- | --- | --- | --- |"])
    for operation in source_operations(group):
        request = operation.get("request")
        request_name = request and request.get("effectiveType") and request["effectiveType"]["name"]
        associations = "; ".join(
            f'{a["resource"]}: {a["group"]}.{a["kind"]}; request={a["checkedPutRequest"]}'
            for a in operation["associations"]
        )
        lines.append(
            f'| {source_link(group["project"], operation)} | {code(request_name or "(no single request)")} | '
            f'{code(associations or "(none)")} | {code(", ".join(operation["responseCandidates"]) or "(none)")} |'
        )
    if group["sameOperationNativeFindingIds"]:
        lines.append("")
        for identity in group["sameOperationNativeFindingIds"]:
            finding = native[identity]
            lines.append(f'Observed TypeSpec {code(finding["family"])}: {code(finding["finding"]["message"])}')
    lines.extend([
        "", f"**Explanation:** {cause[1]}",
        "", f"**Decision:** {action} "
        f"[{title}: evidence and tradeoff](../gap-analysis.md#{anchor}).",
        "", "**Raw observation IDs:** " + ", ".join(code(i) for i in group["rawObservationIds"]) + ".",
        "Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages "
        "are retained in [instance-mapping.json](../instance-mapping.json).", "",
    ])


def render(root):
    data = json.loads((root / "instance-mapping.json").read_text(encoding="utf-8"))
    groups = data["swaggerGroups"]
    native = {item["id"]: item for item in data["nativeFindings"]}
    assessment = json.loads((root / "gap-assessment.json").read_text(encoding="utf-8"))
    assessments = {item["checkId"]: item for item in assessment["checks"]}
    differing = [g for g in groups if not g["mappedNativeFindingIds"]]
    summary = data["summary"]
    routes = summary["routeGrouping"]
    matched = [g for g in groups if g["mappedNativeFindingIds"]]
    matched_findings = sum(bool(f["mappedSwaggerGroups"]) for f in native.values())
    extra_findings = len(native) - matched_findings
    request_member = next(m for m in summary["members"] if m["rule"] == "PutRequestResponseSchemeArm")
    raw_summary = json.loads((root / "summary.json").read_text(encoding="utf-8"))
    lines = [
        "# Exact operation/model correspondence", "",
        "This is the target-level inventory supporting the [migration decision](migration.md) and "
        "[difference analysis](gap-analysis.md). It retains raw findings, exact comparisons and source/schema examples.", "",
        "## Differing projects", "",
        f"This appendix accounts for **{summary['rawSwagger']} Swagger observations, "
        f"{summary['checkedSwaggerInstanceGroups']} member checks and all {len(native)} TypeSpec findings**. "
        "The summary below contains only projects with unpaired checks or additional/different TypeSpec findings, "
        "including equal-total projects with different checks. Counts on shared targets across members are non-additive.", "",
        "| Project | Swagger raw | Member checks | TypeSpec raw | Routes Swagger / TypeSpec | Credited same comparison |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    difference_projects = {
        g["project"] for g in differing
    } | {f["project"] for f in native.values() if not f["mappedSwaggerGroups"]}
    for row in data["summary"]["projects"]:
        if row["project"] in difference_projects:
            lines.append(
                f'| [{code(row["project"])}](instances/{project_anchor(row["project"])}.md) | {row["swaggerRaw"]} | '
                f'{row["swaggerCheckGroups"]} | {row["nativeFindings"]} | '
                f'{row["swaggerRoutes"]} / {row["nativeRoutes"]} | {row["mappedFindings"]} |'
            )
    lines.extend([
        "", "## Request comparison differences", "",
        f"Of {request_member['groups']} request checks, {request_member['mappedNativeFindings']} have corresponding "
        "TypeSpec warnings. The difference groups below preserve every remaining comparison; "
        "the previous traversal gap is assessed separately against the final-source results. "
        "See [registered traversal](gap-analysis.md#registered-put-traversal), "
        "[existing policy exceptions](gap-analysis.md#existing-policy-exceptions) and "
        "[legacy contracts](gap-analysis.md#legacy-contracts).", "",
        "## Response comparison differences", "",
        "**16 success-schema checks:** 15 Swagger identity-bug false positives and Quota's genuine difference, "
        "which the existing Azure Core rule detects before suppression. "
        "**57 resource-marker checks:** independent policy is absent. "
        "**36 cross-method checks:** 15 no-content comparisons, four matching-item collection comparisons, "
        "16 empty-200 cases detected by the existing body rule before suppression, and one genuine SyncJob shape difference. "
        "The shared ARM rule emits no corresponding response-family warning. "
        "[Evidence and decisions](gap-analysis.md#difference-groups).", "",
        "## Identity and attribution", "",
        "Each raw observation is resolved against the immutable Swagger dataset by exact route and explicit operation ID, "
        "or by exact referenced schema document and JSON pointer for staging schema targets. All 433 have one candidate. "
        "Grouping retains `(member, project, resolved document, exact route, request/response schema context)`; "
        "it never merges different member checks or distinct schema contexts. PUT/GET/PATCH is one path-level method bundle, "
        "not three invented violations.", "",
        "The result is 168 + 16 + 57 + 36 = **277** member checks. Network's 170 raw observations resolve to 14 checks "
        "(three request, ten extension, one cross-method), accounting for all 156 repeated observations. "
        "Location-only JSON-path keys are not operation identities: schema-target locations can identify "
        "different invoking operations. The separate location summaries remain in [summary.json](summary.json).", "",
        "These checks reference 256 distinct project/routes and 307 participating method/route identities. "
        "All 328 source bindings across the member checks, and all 328 selected-version bindings, are unique exact method/route matches. "
        "No fuzzy matching or parameter normalization was needed. Original fallback documents and validator inputs remain unchanged; "
        "the separately resolved document is explicit in every group.", "",
        f"All {len(matched)} credited cases use the same operation, a different effective request model and the canonical resource as the "
        "original selected response body. Their source and selected-version request/response metadata agree. "
        "**This corroborates these observed request-resource mismatches; it does not prove structural schema equality and "
        "source-model identity are universally equivalent, or that correcting the source will necessarily eliminate every emitted-schema difference.**", "",
        f"Routes overlap at {routes['both']} ({routes['swaggerOnly']} Swagger-only, {routes['nativeOnly']} TypeSpec-only), "
        f"but only {matched_findings} findings receive comparison credit. "
        "Route co-occurrence is explicitly not coverage. The complete raw IDs and full schema contexts are in "
        "[Swagger bindings](swagger-bindings.json), [native-to-Swagger bindings](native-swagger-bindings.json) and "
        "[assessment](instance-mapping.json).", "",
        f"Per-project route-grouped excesses are {summary['routeCountDifferences']['swaggerHigherExcess']} Swagger-higher "
        f"and {summary['routeCountDifferences']['nativeHigherExcess']} TypeSpec-higher, absolute difference "
        f"{summary['routeCountDifferences']['absoluteDifference']}. "
        f"This is distinct from raw-finding excesses of {raw_summary['swaggerHigherExcess']} and "
        f"{raw_summary['nativeHigherExcess']}. "
        "Opposing project differences do not cancel in either unit.", "",
        "## TypeSpec finding accounting", "",
        f"The shared linter reports **{summary['nativeFamilies'].get('requestMismatch', 0)} requestMismatch + "
        f"{summary['nativeFamilies'].get('missingRequest', 0)} missingRequest + "
        f"{summary['nativeFamilies'].get('responseMismatch', 0)} response-family findings**. "
        f"{matched_findings} findings correspond to selected Swagger comparisons; all {extra_findings} additional "
        "or different findings appear individually below.", "",
        "Missing-request warnings enforce an additional body-existence policy. A source-only operation absent in the "
        "selected version is a population difference, not a new selected-version defect. A PUT without 200/201 is outside "
        "the original request rule's registration selector. Same-operation warnings comparing another canonical resource "
        "or selected body do not receive comparison credit. Any unresolved schema-identity classification remains "
        "unresolved until its linked source/schema evidence explains it; totals alone are never correspondence.", "",
        "| Additional comparison / cause | Swagger corresponding findings | TypeSpec findings | Gap analysis and decision |",
        "| --- | --- | --- | --- |",
    ])
    for classification, (title, action) in NATIVE_DIFFERENCES.items():
        count = summary["nativeClassifications"].get(classification, 0)
        if count:
            lines.append(f"| {title} | 0 | {count} | {action} |")
    lines.extend([
        "",
        "The zero column means no selected Swagger finding for that same comparison, not no Swagger warning on the route.", "",
        "| TypeSpec operation / source | Family | Disposition | Credited Swagger check IDs |",
        "| --- | --- | --- | --- |",
    ])
    for finding in sorted(native.values(), key=lambda f: (f["project"], f["operation"]["operation"])):
        lines.append(
            f'| {source_link(finding["project"], finding["operation"])} | {code(finding["family"])} | '
            f'{code(finding["classification"])} | '
            + (", ".join(f'[`{identity}`](#s-{identity})' for identity in finding["mappedSwaggerGroups"]) or "(none)") + " |"
        )
    outputs = {}
    lines.extend([
        "", "## Per-project target differences", "",
        "Use the project links in [Differing projects](#differing-projects) for every original target, "
        "corresponding TypeSpec operation/model and disposition. Project pages keep the evidence small enough "
        "to render on GitHub. All 277 check groups remain in the machine-readable assessment.", "",
    ])
    for project in sorted(difference_projects):
        row = next(item for item in data["summary"]["projects"] if item["project"] == project)
        project_lines = [
            f"# {project}", "", "[All project differences](../instance-correspondence.md#differing-projects).", "",
            f'**Project totals:** Swagger {row["swaggerRaw"]} raw / {row["swaggerCheckGroups"]} member checks; '
            f'TypeSpec {row["nativeFindings"]} raw; {row["mappedFindings"]} findings credited to the same comparison. '
            f'Common project/route unit: {row["swaggerRoutes"]} Swagger / {row["nativeRoutes"]} TypeSpec. '
            "Counts repeated across different members at the same operation are non-additive. "
            "TypeSpec counts refer only to arm-resource-operation-response, not the entire linter suite.", "",
        ]
        project_groups = [g for g in differing if g["project"] == project]
        for group in sorted(project_groups, key=lambda g: (g["route"], g["rule"])):
            render_group(project_lines, group, native, assessments)
        matching = [g for g in groups if g["project"] == project and g["mappedNativeFindingIds"]]
        if matching:
            project_lines.extend(["## Matching request checks", ""])
            for group in matching:
                project_lines.append(
                    f'- [{code(group["id"])}](../instance-correspondence.md#s-{group["id"]}): '
                    f'{code(group["swaggerOperations"][0]["operationId"])}; one Swagger finding and one matching TypeSpec warning.'
                )
            project_lines.append("")
        residuals = [f for f in native.values() if f["project"] == project and not f["mappedSwaggerGroups"]]
        if residuals:
            project_lines.extend(["## Additional or different TypeSpec checks", ""])
            for finding in residuals:
                operation = finding["operation"]
                project_lines.extend([
                    f'- {source_link(project, operation)}: **{finding["classification"]}**; '
                    f'{code(finding["finding"]["message"])}; route {code(operation["path"])}.',
                ])
            project_lines.append("")
        outputs[f"instances/{project_anchor(project)}.md"] = "\n".join(project_lines)
    lines.extend([
        "## Matching request targets", "",
        f"These {len(matched)} controls are listed separately from differences. Each has one original raw finding and one "
        "TypeSpec requestMismatch on the same PUT, with the selected source response equal to the canonical resource. "
        "The full output retains the exact request, resource, status-specific bodies, source line and diagnostic.", "",
        "| Check ID / source | Swagger operation / request | Canonical selected response |",
        "| --- | --- | --- |",
    ])
    for group in sorted((g for g in groups if g["mappedNativeFindingIds"]), key=lambda g: (g["project"], g["route"])):
        operation = source_operations(group)[0]
        resource = next(a["resource"] for a in operation["associations"] if a["checkedPutRequest"])
        lines.append(
            f'| <a id="s-{group["id"]}"></a>{code(group["id"])} {source_link(group["project"], operation)} | '
            f'{code(group["swaggerOperations"][0]["operationId"])} / {code(operation["request"]["effectiveType"]["name"])} | {code(resource)} |'
        )
    examples = json.loads((root / "instance-examples.json").read_text(encoding="utf-8"))
    lines.extend(["", "## Code-backed representatives", "",
                  "These are verbatim excerpts of the pinned authored source, not invented or standalone compiling fixtures. "
                  "The per-target entries above retain all other instances; existing broader controls and examples remain in "
                  "[evidence-details.md](evidence-details.md#exact-source-examples).", ""])
    for example in examples:
        lines.extend([
            f'### {example["title"]}', "",
            f'**Project/API version:** {code(example["project"])} / {code(example["apiVersion"])}.',
            f'**Source:** {example["sourceLink"]}, lines {example["startLine"]}-{example["endLine"]}.', "",
            "**TypeSpec source**", "", "```typespec", example["source"].rstrip(), "```", "",
            "**Emitted Swagger schema excerpt / version-scope evidence**", "", "```json",
            json.dumps(example["swagger"], indent=2), "```", "",
            f'**Observed comparison / disposition:** {example["explanation"]}', "",
        ])
    lines.extend([
        "## Reproduction and limits", "",
        f"The metadata-only inspection recompiled the {summary['traceProjects']}-project union affected by either engine, concurrency two. "
        f"All {summary['traceProjects']} succeeded, every saved finding was reproduced byte-for-field, and HTTP metadata produced zero diagnostics. "
        f"The inspection did not modify specs or linter source and did not emit Swagger. The {487 - summary['traceProjects']} no-finding projects remain in the successful 487-project corpus; "
        "they did not need another metadata compilation.", "",
        "[Execution receipt](receipts/instance-inspection-20261105.json) retains timings, full-graph hashes/counts and equality checks. "
        "[Compact metadata](instance-inputs.json) retains every relevant operation and version counterpart without duplicating unrelated HTTP graphs. "
        "The [inspector](analysis/inspect-instance-targets.mjs) copies the candidate's actual response traversal, "
        "and the [runner](analysis/run-instance-inspection.py) injects it into the pinned worker without changing diagnostic selection.", "",
        "Saved-evidence verification: `python analyze-instances.py --root .`, "
        "`python -m unittest test_instance_analysis.py test_reanalyze.py`, and `python reanalyze.py --verify-inventory`. "
        "`python render-instances.py --verify` checks the generated appendix/member prose, ignoring formatter whitespace; "
        "integrity.json verifies exact saved bytes. "
        "Fresh metadata reproduction additionally requires the pinned runtime/artifacts and original worker inputs documented in "
        "[evidence-details.md](evidence-details.md#read-recount-and-regenerate). "
        "The resolver accepts `--observations`, `--dataset`, `--output` and optional `--traces`; no CLI invocation regenerates Swagger.", "",
        "The [migration report](migration.md) states the conclusion; [gap-analysis.md](gap-analysis.md) "
        "explains the recommended fixes, policy exceptions and unresolved contracts. "
        "This inventory does not turn unpaired findings into proven defects or prospective fixes into observed coverage.", "",
    ])
    outputs["instance-correspondence.md"] = "\n".join(lines)
    for member in data["summary"]["members"]:
        rule = member["rule"]
        slug, function, conclusion, unit = MEMBERS[rule]
        body = [
            f"# {rule} migration", "", "## 1. Conclusion and scope", "",
            "The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` "
            f"is assessed against [`{rule}`]({UPSTREAM}docs/{slug}.md). **{conclusion}**",
            "", "## 2. Actual coverage", "",
            "All 487 projects compiled successfully; none failed or was unassessed. "
            "Reported diagnostics are individual findings. The TypeSpec column contains only observed warnings "
            "attributed to this member's comparison, not the shared rule's entire output.", "",
            "| Count | Swagger linter | TypeSpec linter |", "| --- | --- | --- |",
            f'| Reported diagnostics (member / corresponding TypeSpec) | {member["raw"]} | {member["mappedNativeFindings"]} |',
            f'| {unit}, grouped by project/document/route/schema | {member["groups"]} | {member["mappedNativeFindings"]} |', "",
            "The grouped row counts checks, not equivalent defects. "
            "See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the causes and decisions.",
            "", "## 3. Function-level coverage", "",
            "| Behavior | Result |", "| --- | --- |",
            *{
                "PutRequestResponseSchemeArm": [
                    "| Registered createOrUpdate PUT request / canonical resource | Covered by effective payload identity; not universal emitted-schema structural equality. |",
                    "| Legacy or overwritten registered PUTs | Included through the existing operation Set, deduplicated per resource/Operation. |",
                    "| Custom request / actual selected response | Not generally compared; body-policy exceptions and legacy modeling need separate treatment. |",
                ],
                "ConsistentResponseSchemaForPut": [
                    "| Different 200/201 success bodies | Azure Core response-schema-problem detects the observed Quota case before suppression; this ARM rule does not independently compare it. |",
                    "| Identical 200/201 schemas | Correctly avoids the Swagger object-identity bug. |",
                ],
                "XmsResourceInPutResponse": [
                    "| Selected response resource marker, including inherited/reference markers | Missing independent policy; canonical registration/request warnings do not enforce it. |",
                    "| Custom/action response payloads | Required resource semantics remain unresolved; not every missing marker is a proven defect. |",
                ],
                "PutGetPatchResponseSchema": [
                    "| Registered-resource return identity | Retained narrower traversal, not general cross-method payload equality. |",
                    "| Empty ordinary-success response | Existing no-response-body policy, explicitly suppressed on the observed targets. |",
                    "| No-content / collection-wrapper roles | Literal reference equality is misleading; recommend excluding these comparisons. |",
                    "| Different non-bodyless entity shapes | SyncJob contract remains unresolved. |",
                ],
            }[rule],
            "| Shared-rule controls | [Exact-candidate controls](../../evidence-details.md#controls-and-validation) verify existing behavior, not coverage of absent checks. |",
            "", "## 4. Why diagnostic counts differ", "",
            "Only unpaired groups are listed. The TypeSpec count is for the same comparison; "
            "other rules' pre-suppression results and unrelated same-operation warnings are excluded.", "",
            "| Difference / evidence | Swagger findings / checks | TypeSpec corresponding warnings | Gap analysis and decision |",
            "| --- | --- | --- | --- |",
        ]
        for row in difference_rows(assessment, rule):
            body.append(
                f'| [{row["title"]}](../../gap-analysis.md#{row["anchor"]}) | '
                f'{row["raw"]} / {row["checks"]} | 0 | {row["action"]} |'
            )
        body.extend([
            "", "Zero does not mean that other TypeSpec policies are absent or that the APIs are compliant. "
            "Proposed fixes are not observed coverage; recommended exclusions are not approved retirements. "
            "[Exact targets and both engines' results](../../instance-correspondence.md#differing-projects) retain the evidence.",
            "", "## NOTES", "",
            "The [group report](../../migration.md#notes) records shared source/projection, suppression and corpus policies. "
            "[Controls and reproduction](../../evidence-details.md#controls-and-validation) and "
            "[all TypeSpec finding dispositions](../../instance-correspondence.md#typespec-finding-accounting) are retained.", "",
            f"[Original implementation]({UPSTREAM}packages/rulesets/src/spectral/functions/{function}.ts). "
            "Reconstruct these reports with `python render-instances.py` from the group directory.", "",
        ])
        outputs[f"members/{rule}/migration.md"] = "\n".join(body)
    return outputs


def canonical_markdown(text):
    lines = []
    for line in text.splitlines():
        if line.startswith("|"):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if all(re.fullmatch(r":?-+:?", cell) for cell in cells):
                line = "|".join("---" for _ in cells)
            else:
                line = "|".join(cells)
        lines.append(line)
    return " ".join("\n".join(lines).split())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=ROOT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    for name, text in render(args.root).items():
        file = args.root / name
        if args.verify:
            assert canonical_markdown(file.read_text(encoding="utf-8")) == canonical_markdown(text), name
        else:
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text(text, encoding="utf-8", newline="\n")
