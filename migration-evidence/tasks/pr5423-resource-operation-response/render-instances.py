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
        "Not equivalent: only a subset of the original request/selected-response comparisons is covered.",
        "PUT operations",
    ),
    "ConsistentResponseSchemaForPut": (
        "consistent-response-schema-for-put", "consistent-response-schema-for-put",
        "Not equivalent: the genuine plain 201 response mismatch is missed; the upstream object-identity bug should not be reproduced.",
        "PUT operations",
    ),
    "XmsResourceInPutResponse": (
        "xms-resource-in-put-response", "with-xms-resource",
        "Not equivalent: canonical resource registration does not independently enforce the selected emitted response extension.",
        "PUT operations",
    ),
    "PutGetPatchResponseSchema": (
        "put-get-patch-response-schema", "put-get-patch-schema",
        "Not equivalent: registered-resource return traversal does not implement the original status-specific response-reference comparison.",
        "route comparisons",
    ),
}
CAUSES = {
    "missed-request-registered-response-operation-absent-from-map": (
        "Registered response, but PUT absent from retained operation map",
        "The response body is registered, but this operation has no retained resource association. "
        "The listener therefore never reaches its request. ApiManagement demonstrates same-name registration overwrite; "
        "absence from the map is proven for every target, not an assertion that every absence has the same decorator cause.",
        "TypeSpec rule update required: cover the actual PUT operation rather than relying solely on a singular retained registration slot; add overwritten-alias controls.",
    ),
    "missed-request-outside-lifecycle-map": (
        "PUT stored under lists rather than lifecycle.createOrUpdate",
        "The operation is associated through lists. Existing response traversal visits it, but the new request branch does not.",
        "TypeSpec rule update required: cover PUT request comparisons stored by legacy/list registration; add violating and compliant legacy-template fixtures.",
    ),
    "missed-request-unregistered-response-operation": (
        "Unassociated PUT with no registered response model",
        "The source HTTP graph contains the PUT, but it has no retained resource association and no registered response body. "
        "Inherited ARM-shaped models alone do not satisfy getArmResource.",
        "TypeSpec rule update required: support authorable custom/unregistered PUT request-response comparisons, or obtain approval for a narrower policy before claiming migration.",
    ),
    "same-operation-different-comparison": (
        "Warning on the same operation compares a different contract",
        "The TypeSpec request warning is real, but its canonical resource or selected response status/body differs from the original comparison. "
        "It is not credited merely because the HTTP operation is identical.",
        "TypeSpec rule update required for the original request/actual-response predicate; incorrect source registration may independently need a spec fix. Preserve a same-route/different-model regression.",
    ),
    "source-canonical-request-agrees-emitted-schemas-differ": (
        "Canonical request is accepted while selected 200 has no schema",
        "The request is exactly the registered resource, so TypeSpec accepts it. The original chooses the existing 200 response even without a schema, "
        "then compares the request against an empty schema instead of falling back to 201.",
        "TypeSpec rule update required for the original selected-status/body predicate; add empty-200 controls. This policy difference is not an approved retirement.",
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
        "TypeSpec rule update required: compare status-specific success payloads, including nonresource models; add the Quota-shaped violation and equal-schema control.",
    ),
    "missed-emitted-resource-extension-check": (
        "Selected PUT response lacks resource extension",
        "Every selected response here has xmsResourceInHierarchy=false after reference/allOf traversal. "
        "The TypeSpec rule has no independent extension or equivalent response-resource check; an incidental request warning is not coverage.",
        "TypeSpec rule update required: enforce the source concept that guarantees the selected response resource extension, with unregistered-response and inherited-extension controls.",
    ),
    "missed-cross-operation-selected-ref-absent": (
        "Cross-operation comparison includes an absent selected response reference",
        "The original picks the first existing 200/201/202 response and reads schema.$ref. It can obtain undefined for an empty response, "
        "an inline schema, or an operation without those statuses. The resource traversal does not compare this value across methods.",
        "TypeSpec rule update required for exact original-policy parity: add selected-status/body and inline-schema controls. A different intended policy requires explicit approval; no retirement is inferred.",
    ),
    "missed-cross-operation-distinct-response-refs": (
        "Cross-operation comparison has distinct selected references",
        "The original compares reference names, including resource-versus-list-wrapper responses at collection routes. "
        "The retained TypeSpec rule instead checks supported registered resource candidates. Wrapper/list-item equivalence is not reference-name equality.",
        "TypeSpec rule update required for original-policy parity: cover explicit cross-method response comparison and collection/list fixtures. These policy differences are not silently accepted as equivalent.",
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


def render_group(lines, group, native):
    cause = CAUSES[group["classification"]]
    lines.extend([
        f'<a id="s-{group["id"]}"></a>',
        f'### {group["rule"]}: {group["swaggerOperations"][0].get("operationId", group["id"])}',
        "",
        f'**Identity:** {code(group["id"])}; {code(group["route"])}.',
        f'**Swagger document:** {code(group["document"])}.',
        f'**Cause:** {cause[0]}.',
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
        "", f"**Explanation:** {cause[1]}", "", f"**Disposition:** {cause[2]}",
        "", "**Raw observation IDs:** " + ", ".join(code(i) for i in group["rawObservationIds"]) + ".",
        "Full reported/input document attribution, JSON paths, source/selected-version response bodies and messages "
        "are retained in [instance-mapping.json](../instance-mapping.json).", "",
    ])


def render(root):
    data = json.loads((root / "instance-mapping.json").read_text(encoding="utf-8"))
    groups = data["swaggerGroups"]
    native = {item["id"]: item for item in data["nativeFindings"]}
    differing = [g for g in groups if not g["mappedNativeFindingIds"]]
    lines = [
        "# Exact operation/model correspondence", "",
        "## Differing projects", "",
        "This appendix accounts for **433 Swagger observations, 277 member checks and all 104 TypeSpec findings**. "
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
        "**168 distinct PUT checks:** 87 corroborated request mismatches, 39 PUTs stored under lists, "
        "23 registered-response PUTs absent from the retained map, 12 unassociated/unregistered-response PUTs, "
        "five same-operation/different comparisons and two canonical requests with empty selected 200 schemas. "
        "The last five plus two are not credited as matching checks.", "",
        "## Response comparison differences", "",
        "**16 status-equality checks:** 15 upstream identity-bug false positives and one genuine Quota mismatch. "
        "**57 extension checks:** all selected response hierarchies lack the extension; none is independently checked. "
        "**36 cross-method route checks:** 33 have at least one absent selected `$ref`; three compare distinct references. "
        "Their traversal context is: 28 with retained registered candidates, seven with no retained association, "
        "and one with no registered return candidate. No response-family warning fired.", "",
        "## Identity and attribution", "",
        "Each raw observation is resolved against the immutable Swagger dataset by exact route and explicit operation ID, "
        "or by exact referenced schema document and JSON pointer for staging schema targets. All 433 have one candidate. "
        "Grouping retains `(member, project, resolved document, exact route, request/response schema context)`; "
        "it never merges different member checks or distinct schema contexts. PUT/GET/PATCH is one path-level method bundle, "
        "not three invented violations.", "",
        "The result is 168 + 16 + 57 + 36 = **277** member checks. Network's 170 raw observations resolve to 14 checks "
        "(three request, ten extension, one cross-method), accounting for all 156 repeated observations. "
        "The earlier 275 file-independent JSON-path keys are not this identity: schema-target locations can identify "
        "different invoking operations, so they must not be relabeled operation counts.", "",
        "These checks reference 256 distinct project/routes and 307 participating method/route identities. "
        "All 328 source bindings across the member checks, and all 328 selected-version bindings, are unique exact method/route matches. "
        "No fuzzy matching or parameter normalization was needed. Original fallback documents and validator inputs remain unchanged; "
        "the separately resolved document is explicit in every group.", "",
        "All 87 credited cases use the same operation, a different effective request model and the canonical resource as the "
        "original selected response body. Their source and selected-version request/response metadata agree. "
        "**This corroborates these observed request-resource mismatches; it does not prove structural schema equality and "
        "source-model identity are universally equivalent, or that correcting the source will necessarily eliminate every emitted-schema difference.**", "",
        "Routes overlap at 95 (161 Swagger-only, nine TypeSpec-only), but only 87 findings receive comparison credit. "
        "Route co-occurrence is explicitly not coverage. The complete raw IDs and full schema contexts are in "
        "[Swagger bindings](swagger-bindings.json), [native-to-Swagger bindings](native-swagger-bindings.json) and "
        "[assessment](instance-mapping.json).", "",
        "Per-project route-grouped excesses are 156 Swagger-higher and four TypeSpec-higher, absolute difference 160. "
        "This is distinct from the original raw-finding excesses of 333 and four. "
        "Opposing project differences do not cancel in either unit.", "",
        "## TypeSpec finding accounting", "",
        "The shared linter reports **96 requestMismatch + eight missingRequest + zero response-family findings**. "
        "Of the 96: 87 map to the original request comparison, seven occur on routes with original findings but compare a different contract, "
        "one is Batch Certificate removed from the selected version, and one is PostgreSQL DbAgent with only a 202 response. "
        "The original request rule's registration selects existing 200/201 responses, so it never invokes its function for that 202-only PUT. "
        "This selector restriction is separate from the function's 200-otherwise-201 fallback.", "",
        "The eight missing requests are DnssecConfig, EventGrid DomainTopic, ManagementGroups subscription association, "
        "MySQL ServerBackup, PostgreSQL BackupAutomaticAndOnDemand, Security ApiCollection, SQL OutboundFirewallRule "
        "and SQL ServerDnsAlias. They are additional policy, not covered findings of the four original members. "
        "Missing-request and 202-only extras require no TypeSpec change merely to explain these counts; "
        "Batch requires comparable projection for a latest-version comparison, not a production-rule change.", "",
        "The seven coincident request mismatches are ApiManagement PrivateEndpointConnection, Automation DscNodeConfiguration, "
        "HDInsight Extension, PostgreSQL AdministratorMicrosoftEntra and Configuration, RecoveryServices certificate, "
        "and RecoveryServicesBackup encryption configuration. Five share an original request-rule finding; "
        "the two PostgreSQL operations share only response-comparison findings. None is automatically credited to those response rules.", "",
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
            "Counts repeated across different members at the same operation are non-additive.", "",
        ]
        project_groups = [g for g in differing if g["project"] == project]
        for group in sorted(project_groups, key=lambda g: (g["route"], g["rule"])):
            render_group(project_lines, group, native)
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
        "These 87 controls are listed separately from differences. Each has one original raw finding and one "
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
        "The metadata-only inspection recompiled the 59-project union affected by either engine, concurrency two. "
        "All 59 succeeded, every saved finding was reproduced byte-for-field, and HTTP metadata produced zero diagnostics. "
        "No spec or linter was modified and Swagger was not emitted. The 428 no-finding projects remain in the original successful 487-project corpus; "
        "they did not need another metadata compilation.", "",
        "[Execution receipt](receipts/instance-inspection-20261104.json) retains timings, full-graph hashes/counts and equality checks. "
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
        "**Decision:** the migrated linter is not functionally equal to the four-rule group. "
        "175 original member checks remain unpaired through semantic/scope differences, plus 15 upstream false positives that should not be reproduced. "
        "Target attribution is assessed, not unresolved; original-policy coverage still requires the rule/fixture changes specified above, "
        "or an explicitly approved narrower policy. No such approval or production changes are claimed.", "",
    ])
    outputs["instance-correspondence.md"] = "\n".join(lines)
    for member in data["summary"]["members"]:
        rule = member["rule"]
        slug, function, conclusion, unit = MEMBERS[rule]
        member_groups = [g for g in groups if g["rule"] == rule]
        body = [
            f"# {rule} migration", "", "## 1. Conclusion and scope", "",
            "The TypeSpec linter `@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response` "
            f"consolidates [`{rule}`]({UPSTREAM}docs/{slug}.md). **{conclusion}**",
            "", "## 2. Actual coverage", "",
            "All 487 frozen projects succeeded, zero failed/unassessed. Reported diagnostics are individual findings. "
            "The TypeSpec column is now deterministically attributed to this member by exact operation and relevant comparison; "
            "it is not the entire shared 104-finding rule count.", "",
            "| Count | Swagger linter | TypeSpec linter |", "| --- | --- | --- |",
            f'| Reported findings (member / mapped TypeSpec) | {member["raw"]} | {member["mappedNativeFindings"]} |',
            f'| Distinct checked targets ({unit}) | {member["groups"]} | {member["mappedNativeFindings"]} |', "",
            f'{member["sameOperationNativeFindings"]} shared-rule warnings occur on participating operations, but only '
            f'{member["mappedNativeFindings"]} check the corresponding contract. Coincident messages receive no migration credit. '
            "See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ).",
            "", "## 3. Function-level coverage", "",
            "| Behavior | Result |", "| --- | --- |",
            *{
                "PutRequestResponseSchemeArm": [
                    "| Registered lifecycle request versus canonical selected response | 87 corroborated instances; structural equality and source identity remain different policies. |",
                    "| PUT stored under lists / absent from the retained map | Missing: 39 list-map operations and 35 unassociated operations. |",
                    "| Actual selected response/status differs from canonical comparison | Five coincident warnings and two accepted canonical requests are not equivalent checks. |",
                ],
                "ConsistentResponseSchemaForPut": [
                    "| Different 200/201 bodies, including a nonresource 201 | Missing: Quota's genuine mismatch. |",
                    "| Identical 200/201 references | No TypeSpec warning; correctly avoids 15 upstream object-identity false positives. |",
                ],
                "XmsResourceInPutResponse": [
                    "| Selected PUT response lacks resource extension in its hierarchy | Missing: 57 distinct checks; registration/request warnings do not enforce this predicate. |",
                    "| Extension inherited through allOf / references | Extraction resolves the hierarchy; TypeSpec still has no independent extension predicate. |",
                ],
                "PutGetPatchResponseSchema": [
                    "| First selected 200/201/202 has no $ref | 33 route comparisons are not reproduced by canonical resource traversal. |",
                    "| Selected references differ, including list wrappers | Three route comparisons are not reproduced; wrapper names and list-item identity differ. |",
                    "| Registered-resource return identity | Retained narrower check; zero response-family findings in this corpus. |",
                ],
            }[rule],
            "| Compliant/violation controls | [Exact-candidate shared controls](../../evidence-details.md#controls-and-validation) |",
            "", "## 4. Why diagnostic counts differ", "",
            "| Original check group | Swagger raw | Distinct checks | Corresponding TypeSpec findings |",
            "| --- | --- | --- | --- |",
        ]
        for classification, count in member["classifications"].items():
            if classification == "mapped-request-mismatch":
                continue
            group = next(g for g in member_groups if g["classification"] == classification)
            body.append(
                f'| [{CAUSES[classification][0]}](../../instances/{project_anchor(group["project"])}.md#s-{group["id"]}) | '
                f'{member["classificationRawCounts"][classification]} | {count} | 0 |'
            )
        body.extend([
            "", "Every target, original schema/reference, matching TypeSpec operation/model and diagnostic family is listed in the "
            "[per-project inventory](../../instance-correspondence.md#per-project-target-differences). "
            "The [shared TypeSpec accounting](../../instance-correspondence.md#typespec-finding-accounting) retains all 17 uncredited warnings. "
            "Zero means no corresponding finding was observed and the relevant predicate is absent/different, not that this member's "
            "operations are necessarily compliant.",
            "", "## NOTES", "",
            "Shared frozen inputs, configured source scope, selected Swagger-version policy and execution provenance are in the "
            "[group report](../../migration.md). The 59 affected projects' metadata-only recompilations exactly reproduced all "
            "104 shared findings; all source/selected-version route bindings were unique and exact. No production linter changes "
            "or additional full corpus run were made.", "",
            f"[Original implementation]({UPSTREAM}packages/rulesets/src/spectral/functions/{function}.ts). "
            "Saved-data reconstruction: `python analyze-instances.py --root .` from the group directory.", "",
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
