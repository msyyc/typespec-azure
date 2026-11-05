"""Render all migration narratives from one assessed, independently scoped inventory."""

import argparse
import collections
import hashlib
import json
import pathlib
import posixpath
import re
import urllib.parse


ROOT = pathlib.Path(__file__).resolve().parent
REVISION = "2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9"
UPSTREAM = "https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/"
ARM = "@azure-tools/typespec-azure-resource-manager/"
RESPONSE = ARM + "arm-resource-operation-response"
MARKER = ARM + "arm-put-response-resource"
MEMBERS = {
    "PutRequestResponseSchemeArm": (
        "put-request-response-scheme-arm", "put-request-response-scheme",
        "Partial coverage. Registered createOrUpdate requests are checked, but unassociated legacy contracts and wrong canonical-resource associations remain; emitted structural equality is not generally reproduced.",
    ),
    "ConsistentResponseSchemaForPut": (
        "consistent-response-schema-for-put", "consistent-response-schema-for-put",
        "The observed genuine success-body difference is diagnosed. The TypeSpec linter intentionally avoids the Swagger linter's resolved-object-identity false positives; this is not bug-for-bug equivalence or universal structural-equivalence proof.",
    ),
    "XmsResourceInPutResponse": (
        "xms-resource-in-put-response", "with-xms-resource",
        "Complete observed correspondence for the selected PUT response-marker checks. This policy diagnoses missing resource markers, not proven service defects; custom/action contracts still need owner decisions. Source versus latest-version comparison does not establish universal equivalence.",
    ),
    "PutGetPatchResponseSchema": (
        "put-get-patch-response-schema", "put-get-patch-schema",
        "Not equivalent. Existing response-body diagnostics cover empty 200 responses, but SyncJob's PUT/GET shape difference is not covered by its wrong-parent read registration. No-content and same-item collection comparisons are recommended exclusions, not approved retirements.",
    ),
}
NATIVE_ACTIONS = {
    "additional-resource-marker-policy": "Retain the source marker policy; inspect selected-version/status correspondence before claiming a frozen Swagger counterpart.",
    "additional-canonical-response-policy": "Review the authored canonical resource and actual success body. Parent/child, command, polling-result and collection-role associations are not automatically original cross-method comparisons; prefer wire-compatible spec fixes over weakening the rule.",
    "additional-missing-request-policy": "Additional body-existence policy; the Swagger selector skips missing bodies. Review the wire contract rather than inventing a request for count parity.",
    "same-operation-different-comparison": "Review the canonical association or selected status/body. A real warning on the route receives no credit for a different comparison.",
    "source-only-operation-not-in-selected-version": "Retain source diagnostics and use supported version alignment for selected-version parity; do not suppress them to equalize totals.",
    "additional-request-check-outside-swagger-200-201-selector": "Keep broader registered-request enforcement separate from the Swagger 200/201 selector.",
    "native-only-request-policy-or-schema-identity-unresolved": "Unresolved source/schema identity; establish the actual contract before a source change or equivalence claim.",
}
SHORT_DECISIONS = {
    "body-policy-owner": "Diagnosed by the existing body owner before suppression; review the suppression/wire contract, not duplicate schema equality.",
    "bodyless-comparator-overreach": "Recommend excluding absent-body comparisons, not inventing bodies. Status-code compliance is a separate policy; approval is pending.",
    "collection-comparator-overreach": "Recommend excluding wrapper-versus-item reference equality: actual resource items agree. Approval is pending.",
    "cross-method-entity-contract": "Genuine uncovered contract difference. Confirm service intent before sharing models; defer a broad structural matcher.",
    "custom-collection-request": "Unresolved bulk/item semantics. Require owner intent before enforcing ordinary resource replacement.",
    "custom-command-request": "Unresolved command/association contracts; do not infer canonical replacement solely from PUT.",
    "custom-lifecycle-registration": "Missing associations; three compatibility-checked repairs are in separate draft #47952, not frozen-corpus credit.",
    "parent-canonical-association": "Wrong parent/operation-kind association; repair modeling only after proving wire/client compatibility.",
    "supported-polymorphism": "Preserve the hierarchy; establish canonical request registration. Response ancestry support does not prove derived-request acceptance.",
    "unregistered-entity-request": "Four legacy DTO contracts lack canonical registration; review visibility/wire models rather than add recursive schema equality.",
    "upstream-identity-bug": "Confirmed resolved-object-identity bug; intentionally do not port its false positives.",
}
SHORT_MEMBER = {
    "PutRequestResponseSchemeArm": "Partial: legacy associations/contracts remain.",
    "ConsistentResponseSchemaForPut": "Observed genuine difference diagnosed; identity bug intentionally avoided.",
    "XmsResourceInPutResponse": "All observed marker comparisons correspond.",
    "PutGetPatchResponseSchema": "Partial: body owner covers empty 200s; SyncJob remains.",
}


def read(root, name):
    return json.loads((root / name).read_text(encoding="utf-8"))


def code(value):
    return "`" + str(value).replace("|", "\\|").replace("`", "'") + "`"


def project_anchor(project):
    return "p-" + hashlib.sha256(project.encode()).hexdigest()[:12]


def source_link(project, operation):
    file = posixpath.normpath(project + "/" + operation["sourceFile"])
    url = f"https://github.com/msyyc/azure-rest-api-specs/blob/{REVISION}/{urllib.parse.quote(file)}#L{operation['line']}"
    return f"[{operation['operation']}]({url})"


def distinct_callbacks(rows):
    return len({
        json.dumps(report, sort_keys=True)
        for row in rows for report in row["ownerReports"]
    })


def difference_rows(assessment, rule=None):
    grouped = collections.defaultdict(list)
    for row in assessment["checks"]:
        if row["decision"] != "corroborated" and (rule is None or row["member"] == rule):
            grouped[row["decision"]].append(row)
    return [
        {"decision": decision, "checks": len(rows), "raw": sum(row["rawObservations"] for row in rows)}
        for decision, rows in sorted(grouped.items())
    ]


def operation_evidence(operation):
    return {
        key: operation[key] for key in (
            "operation", "sourceFile", "line", "verb", "path", "request", "associations", "responses",
        ) if key in operation
    }


def render(root):
    data = read(root, "instance-mapping.json")
    assessment = read(root, "gap-assessment.json")
    summary = read(root, "summary.json")
    task = read(root, "task.json")
    groups = data["swaggerGroups"]
    findings = data["nativeFindings"]
    checks = {row["checkId"]: row for row in assessment["checks"]}
    decisions = {row["decision"]: row for row in assessment["decisions"]}
    accounting = assessment["coverageAccounting"]
    mappings = summary["mappingAssessments"]
    outputs = {}

    def scoped_mapping(rule):
        return next(row for row in mappings if rule in row["mapping"]["validatorRules"])

    def group_link(group, prefix=""):
        return f'{prefix}instances/{project_anchor(group["project"])}.md#s-{group["id"]}'

    def coverage_sentence(rows):
        mapped = sum(bool(row["mappedWarningIds"]) for row in rows)
        owner = sum(bool(row["ownerReports"]) and not row["mappedWarningIds"] for row in rows)
        residual = [row for row in rows if not row["mappedWarningIds"] and not row["ownerReports"]]
        false = sum(row["decision"] == "upstream-identity-bug" for row in residual)
        excluded = sum(row["decision"] in ("bodyless-comparator-overreach", "collection-comparator-overreach") for row in residual)
        remaining = len(residual) - false - excluded
        sources = []
        if mapped:
            sources.append(f"{mapped} by corresponding configured warnings")
        if owner:
            sources.append(f"{owner} additional contexts by captured owning diagnostics before authored suppression")
        residuals = []
        if false:
            residuals.append(f"{false} confirmed Swagger false-positive contexts")
        if excluded:
            residuals.append(f"{excluded} recommended comparison exclusions awaiting approval")
        if remaining:
            residuals.append(f"{remaining} unresolved/modeling or deferred contract contexts")
        text = f"{mapped + owner} of {len(rows)} original member-check contexts are diagnosed: " + "; ".join(sources) + ". "
        if residuals:
            text += "Remaining: " + "; ".join(residuals) + ". "
        overlap = sum(bool(row["ownerReports"] and row["mappedWarningIds"]) for row in rows)
        if overlap:
            text += f"{overlap} mapped context(s) also have captured owning diagnostics; coverage counts each once. "
        return text + (
            "Captured owning diagnostics receive credit despite suppression, without changing configured raw totals. "
            "Contexts are not equivalent-defect counts; universal violation percentages remain unassessed."
        )

    def difference_table(rule=None, prefix=""):
        selected = [
            group for group in groups
            if not group["mappedNativeFindingIds"] and (rule is None or group["rule"] == rule)
        ]
        lines = [
            "`Raw / grouped` means reported Swagger diagnostics / distinct "
            "(member, project, resolved document, exact route, compared schema context) checks. "
            "The TypeSpec column counts only configured diagnostics attributed to that same comparison, "
            "not unrelated warnings on the route or callbacks hidden by authored suppression. "
            "Captured owning diagnostics are nevertheless credited in Assessed coverage and identified below.", "",
            "| Difference (with evidence) | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | Recommended action and rationale |",
            "| --- | --- | --- | --- |",
        ]
        for count in difference_rows(assessment, rule):
            decision = count["decision"]
            info = decisions[decision]
            rows = [group for group in selected if checks[group["id"]]["decision"] == decision]
            if not rows:
                continue
            owner_rows = [checks[group["id"]] for group in rows]
            owner_contexts = sum(bool(row["ownerReports"]) for row in owner_rows)
            detail = (
                f"Covered by {distinct_callbacks(owner_rows)} captured owning diagnostic callbacks over "
                f"{owner_contexts} contexts before suppression. "
            ) if owner_contexts else ""
            lines.append(
                f'| [{info["title"]}]({prefix}gap-analysis.md#{decision}) | '
                f'{sum(len(group["rawObservationIds"]) for group in rows)} / {len(rows)} | 0 | '
                f'{detail}{SHORT_DECISIONS[decision]} |'
            )
        selected_rules = set(scoped_mapping(rule)["mapping"]["nativeRules"]) if rule else {RESPONSE, MARKER}
        repeated = [
            group for group in groups if group["mappedNativeFindingIds"]
            and len(group["rawObservationIds"]) > 1 and (rule is None or group["rule"] == rule)
        ]
        for mapping in mappings:
            bucket = [group for group in repeated if group["rule"] in mapping["mapping"]["validatorRules"]]
            if bucket:
                raw = sum(len(group["rawObservationIds"]) for group in bucket)
                warnings = len({identity for group in bucket for identity in group["mappedNativeFindingIds"]})
                lines.append(
                    f'| [Repeated reference invocations: {mapping["mapping"]["name"]}]({prefix}gap-analysis.md#repeated-invocations) | '
                    f'{raw} / {len(bucket)} | {warnings} | Count-only difference: preserve all invocations, '
                    "but compare each exact member/schema context once. No production fix is needed. |"
                )
        extra = [
            finding for finding in findings
            if finding["finding"]["rule"] in selected_rules
            and not any(
                group["id"] in finding["mappedSwaggerGroups"] and (rule is None or group["rule"] == rule)
                for group in groups
            )
        ]
        extra_counts = collections.Counter(
            finding["classification"] if not finding["mappedSwaggerGroups"] else "other-member-comparison"
            for finding in extra
        )
        if rule and extra_counts:
            other = extra_counts.get("other-member-comparison", 0)
            lines.append(
                f'| [Other responsible-rule checks]({prefix}gap-analysis.md#typespec-only-checks) | 0 / 0 | {len(extra)} | '
                f'{other} diagnose other members; {len(extra) - other} are additional/different policy or population checks. '
                "Keep their individual source/body/canonical dispositions separate; none receives this member's credit. |"
            )
        for classification, count in sorted(extra_counts.items()) if rule is None else []:
            action = NATIVE_ACTIONS.get(
                classification,
                "The shared rule diagnoses another member's comparison. Retain its own attribution; do not credit it to this member.",
            )
            lines.append(
                f'| [{classification}]({prefix}gap-analysis.md#typespec-only-checks) | 0 / 0 | {count} | {action} |'
            )
        if not selected and not extra and not repeated:
            return ["No differing checks in the assessed correspondence.", ""]
        return lines + [""]

    behaviors = {
        "PutRequestResponseSchemeArm": [
            ("Registered createOrUpdate PUT, including retained/overwritten aliases", "Covered",
             "Existing resource operation registrations select the canonical model; effective request identity is checked once per operation/resource."),
            ("Missing/void request; compliant and multipart bodies", "Covered / intentional exception",
             "Body existence is additional policy; compliant identity and multipart exemptions are controlled explicitly."),
            ("Unregistered, command, collection or wrong-parent contracts", "Partial / unresolved",
             "HTTP PUT alone does not establish a canonical resource. Separate compatibility-gated spec fixes are safer than a global structural comparator."),
        ],
        "ConsistentResponseSchemaForPut": [
            ("Actual body-bearing 200/201 responses for registered resources", "Covered for observed genuine difference",
             "Canonical consistency now inspects actual HTTP success bodies, including plain nonresource models; Quota also has an existing Azure Core diagnostic."),
            ("Equal success schemas; absent or explicit-void bodies", "Covered compliant behavior",
             "No resolved-object-identity comparison or spurious void/resource mismatch is introduced."),
        ],
        "XmsResourceInPutResponse": [
            ("PUT response marker, 200 then body-bearing 201 fallback", "Observed correspondence complete",
             "Dedicated opt-in rule checks selected actual response metadata independently of canonical registration, including inherited/explicit extension markers."),
            ("Absent/void body, non-PUT and marked response", "Covered compliant behavior",
             "No body is not a missing marker; explicit void is skipped. Custom payloads can opt out only through explicit configuration/suppression."),
        ],
        "PutGetPatchResponseSchema": [
            ("Registered lifecycle actual success responses and list items", "Covered canonical-resource policy",
             "Read/create/update/list aliases are traversed. Per-response arrays/value envelopes are extracted for list associations, and discriminated response ancestry is preserved."),
            ("Empty 200 compared with a resource", "Covered by existing owning diagnostics",
             "Captured no-response-body callbacks remain diagnostic evidence despite authored suppression; schema equality must not replace body-existence policy."),
            ("No-content / same-item collection roles", "Recommended intentional difference",
             "Comparing absent schemas or wrapper names does not establish a different resource item. Exclusions remain recommendations awaiting approval."),
            ("SyncJob PUT/GET shape difference", "Missing / deferred",
             "The borrowed SourceControl read association diagnoses another comparison. Confirm owner intent before sharing models; one route does not justify a recursive version/visibility-aware schema matcher."),
        ],
    }

    def behavior_table(rules, prefix=""):
        lines = ["| Behavior | Result | Rationale |", "| --- | --- | --- |"]
        for rule in rules:
            for behavior, result, rationale in behaviors[rule]:
                lines.append(
                    f"| {behavior} | {result} | {rationale} "
                    f"[Evidence]({prefix}gap-analysis.md#member-{MEMBERS[rule][0]}). |"
                )
        return lines + [""]

    for rule, (slug, function, conclusion) in MEMBERS.items():
        mapping = scoped_mapping(rule)
        scoped = mapping["assessment"]
        rows = [row for row in assessment["checks"] if row["member"] == rule]
        member = next(row for row in data["summary"]["members"] if row["rule"] == rule)
        responsible = mapping["mapping"]["nativeRules"][0]
        lines = [
            f"# {rule} migration", "", "## 1. Conclusion and scope", "",
            f"The TypeSpec linter {code(responsible)} is assessed against "
            f"[`{rule}`]({UPSTREAM}docs/{slug}.md). **{conclusion}**", "",
            "## 2. Actual coverage", "",
            "All 487 frozen projects succeeded; none failed or was unassessed. Reported diagnostics are individual findings. "
            "The TypeSpec raw total is the responsible rule's full output, shared with other members where applicable; "
            "it is not this member's credited coverage.", "",
            "| Count | Swagger linter | TypeSpec linter |", "| --- | --- | --- |",
            f'| Reported diagnostics (member / responsible rule) | {member["raw"]} | {scoped["nativeAligned"]} |',
            f'| Affected project/routes (member / responsible rule, not equivalent defects) | '
            f'{len({(group["project"], group["route"]) for group in groups if group["rule"] == rule})} | '
            f'{scoped["instanceMapping"]["routeGrouping"]["native"]} |', "",
            "**Assessed coverage:** " + coverage_sentence(rows), "",
            "See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ) for the decisions, including broader shared-rule checks.", "",
            "## 3. Function-level coverage", "", *behavior_table([rule], "../../"),
            "## 4. Why diagnostic counts differ", "", *difference_table(rule, "../../"),
            "## NOTES", "",
            f"Assessed source `{task['candidateCommit'][:9]}`; source-program versus latest-version Swagger, "
            "not universal version-aligned equivalence. The marker rule is opt-in in the shared ARM ruleset and "
            "explicitly activated for assessment; authored suppressions remain in configured raw totals. "
            "Owning-rule callbacks are counted separately without double-counting covered contexts.", "",
            f"[Pinned Swagger implementation]({UPSTREAM}packages/rulesets/src/spectral/functions/{function}.ts). "
            "[Shared provenance, controls, recovery and replay](../../evidence-details.md). "
            "[Exact targets](../../instance-correspondence.md).",
        ]
        outputs[f"members/{rule}/migration.md"] = "\n".join(lines) + "\n"

    links = ", ".join(
        f"[`{rule}`]({UPSTREAM}docs/{info[0]}.md)" for rule, info in MEMBERS.items()
    )
    lines = [
        "# ARM PUT and resource-response migration", "", "## 1. Conclusion and scope", "",
        f"The TypeSpec linters {code(RESPONSE)} and {code(MARKER)} are assessed against {links}. "
        "**Not fully equivalent:** marker checks now have complete observed correspondence, and registered-resource "
        "request/actual-response checks are implemented, but legacy resource associations and the genuine SyncJob PUT/GET "
        "contract gap remain. The TypeSpec linter intentionally avoids the Swagger resolved-object-identity bug; "
        "recommended no-content/collection exclusions are not approved retirements.", "",
        "## 2. Actual coverage", "",
        "Each of two independently admitted mappings assessed all **487** frozen projects: **0 failed, 0 unassessed**. "
        "Reported diagnostics are individual findings, not projects. The consistency mapping is three Swagger members "
        "to one TypeSpec rule; marker is a separate one-to-one mapping. Their union is an inventory, not a general "
        "many-to-many coverage percentage.", "",
        "| Count | Swagger linter | TypeSpec linter |", "| --- | --- | --- |",
    ]
    for mapping in mappings:
        scope = mapping["assessment"]
        label = mapping["mapping"]["name"]
        lines.extend([
            f'| Reported diagnostics: {label} | {scope["swaggerRaw"]} | {scope["nativeAligned"]} |',
            f'| Affected project/routes: {label} (not equivalent defects) | '
            f'{scope["instanceMapping"]["routeGrouping"]["swagger"]} | '
            f'{scope["instanceMapping"]["routeGrouping"]["native"]} |',
        ])
    lines.extend([
        "", "**Assessed coverage:** " + coverage_sentence(assessment["checks"]), "",
        "The selected marker mapping is assessed independently; canonical-resource warnings on the same operation "
        "are not automatically marker, request/response or cross-method coverage. "
        "See [Why diagnostic counts differ](#4-why-diagnostic-counts-differ).", "",
        "## 3. Function-level coverage", "", *behavior_table(MEMBERS),
        "## 4. Why diagnostic counts differ", "", *difference_table(),
        "## NOTES", "",
        f"Assessed source `{task['candidateCommit'][:9]}`, core `{task['coreCommit'][:9]}`, frozen specs "
        f"`{task['specsCommit'][:9]}`. Source-program diagnostics are compared with latest-version Swagger, not universal "
        "version-aligned equivalence. Existing source suppressions remain; captured owning diagnostics still receive "
        "coverage credit. The new marker rule is opt-in in the shared ARM ruleset and explicitly enabled in its assessment.", "",
        "| Swagger member | Checks | Corresponding configured-warning contexts | Existing-owner contexts (overlap possible) | Member conclusion |",
        "| --- | --- | --- | --- | --- |",
    ])
    for rule, row in accounting["byMember"].items():
        lines.append(
            f'| [{rule}](members/{rule}/migration.md) | {row["contexts"]} | '
            f'{row["mappedWarningContexts"]} | {row["existingOwnerContexts"]} | {SHORT_MEMBER[rule]} |'
        )
    lines.extend([
        "", f"{accounting['distinctOwnerDiagnosticCallbacks']} distinct captured owning diagnostic callbacks cover "
        f"{accounting['existingOwnerContexts']} member contexts; {accounting['overlappingMappedAndOwnerContexts']} "
        "also has a mapped configured warning. Coverage is the union, not the sum of warning counts.", "",
        "Validation: **923 package tests**, **34 selected injected controls**, **37 portable controls** passed "
        "(6 unrelated fixtures non-applicable). The separate moving external-specs CI still fails; it is not the "
        "successful frozen 487-project assessment. Valid diagnostics are not disabled to manufacture green CI. "
        "[CI and validation limits](evidence-details.md#validation-and-ci).", "",
        "Separate draft [spec-association follow-up #47952](https://github.com/Azure/azure-rest-api-specs/pull/47952) "
        "adds three compatibility-checked registrations; it is **not credited in the frozen corpus**. "
        "Parent/child association and SyncJob decisions remain owner follow-ups. "
        "[Gap analysis and decision](gap-analysis.md); [all exact comparisons](instance-correspondence.md); "
        "[provenance and recovery](evidence-details.md).",
    ])
    outputs["migration.md"] = "\n".join(lines) + "\n"

    lines = [
        "# Gap analysis and decision", "",
        "This appendix separates measured diagnostic coverage, semantic cause and recommended action. "
        "Recommendations are not approved policy retirements. [Migration conclusion](migration.md).", "",
        "## Difference groups", "", *difference_table(),
    ]
    for decision, info in decisions.items():
        rows = [group for group in groups if checks[group["id"]]["decision"] == decision]
        if not rows or decision == "corroborated":
            continue
        records = [checks[group["id"]] for group in rows]
        lines.extend([
            f'<a id="{decision}"></a>', f'## {info["title"]}', "",
            f'**Observed counts:** {sum(len(group["rawObservationIds"]) for group in rows)} Swagger raw / '
            f'{len(rows)} member checks; 0 corresponding configured TypeSpec warnings. '
            f'{distinct_callbacks(records)} captured owning diagnostic callbacks across '
            f'{sum(bool(row["ownerReports"]) for row in records)} contexts before suppression.', "",
            f'**Coverage status:** {", ".join(sorted({row["coverageStatus"] for row in records}))}.', "",
            f'**Cause, tradeoff and recommendation:** {info["recommendation"]}', "",
            "**Exact targets:** " + ", ".join(
                f'[{group["id"]}]({group_link(group)})' for group in rows
            ) + ".", "",
        ])
        if decision == "upstream-identity-bug":
            lines.extend([
                f"[Pinned implementation]({UPSTREAM}packages/rulesets/src/spectral/functions/consistent-response-schema-for-put.ts): "
                "the result uses `!==` on resolved objects. Saved 200/201 references are identical in the same invoking "
                "document; no new resolver-object execution trace or newer upstream version was tested.", "",
            ])
    lines.extend([
        '<a id="repeated-invocations"></a>', "## Repeated reference invocations", "",
        "The same referenced operation/schema can be diagnosed while validating different invoking documents. "
        "All raw input/reported-document identities are retained; only exact same-member/schema contexts are grouped. "
        "This is counting multiplicity, not a production-rule defect or normalization of different violations.", "",
        "| Member / project | Swagger raw | Grouped mapped contexts | TypeSpec corresponding warnings |",
        "| --- | --- | --- | --- |",
    ])
    repeats = collections.defaultdict(list)
    for group in groups:
        if group["mappedNativeFindingIds"] and len(group["rawObservationIds"]) > 1:
            repeats[(group["rule"], group["project"])].append(group)
    for (member, project), bucket in sorted(repeats.items()):
        lines.append(
            f'| {member} / [{code(project)}](instances/{project_anchor(project)}.md) | '
            f'{sum(len(group["rawObservationIds"]) for group in bucket)} | {len(bucket)} | '
            f'{len({identity for group in bucket for identity in group["mappedNativeFindingIds"]})} |'
        )
    lines.append("")
    for rule, (slug, _, _) in MEMBERS.items():
        member_checks = [row for row in assessment["checks"] if row["member"] == rule]
        lines.extend([
            f'<a id="member-{slug}"></a>', f"## {rule}: implemented policy and remaining boundary", "",
            coverage_sentence(member_checks), "",
            f"[Member assessment](members/{rule}/migration.md). "
            "Exact source/body/status/canonical metadata and warning IDs are retained for both matching and differing targets.", "",
        ])
    lines.extend([
        "## TypeSpec-only checks", "",
        "These counts have no attributed selected Swagger finding for the same comparison. A route may still have "
        "an unrelated Swagger warning. Canonical response policy compares against the authored resource, not necessarily "
        "another method's body. This explains additional diagnostics but does not prove every association is correct.", "",
        "| Classification | TypeSpec raw | Gap analysis and decision |", "| --- | --- | --- |",
    ])
    extras = [finding for finding in findings if not finding["mappedSwaggerGroups"]]
    for classification, count in sorted(collections.Counter(row["classification"] for row in extras).items()):
        lines.append(f"| {classification} | {count} | {NATIVE_ACTIONS[classification]} |")
    lines.extend([
        "", "Every extra diagnostic is listed with its message, actual response and canonical association in "
        "[the exact inventory](instance-correspondence.md#typespec-finding-accounting), including one-sided projects.", "",
        "## Compatibility-gated spec follow-ups", "",
        "[Draft #47952](https://github.com/Azure/azure-rest-api-specs/pull/47952) adds only three missing create/update "
        "associations. Registry probes changed as intended; five all-version OpenAPI outputs are byte-identical. "
        "Ten public TCGC outputs differ only in the source-version fingerprint. Full SDK generation was not run and "
        "public TCGC omits internal `__raw`, so specialized ARM SDK neutrality is not proven. "
        "[Receipt](receipts/spec-followup-compatibility-20261105.json).", "",
        "API Management's parent-resource argument also controls paths; a simple argument swap is not wire-neutral. "
        "The RecoveryServices certificate contract has no established canonical child resource. SyncJob has an actual "
        "PUT/GET difference (read-only name/type/id versus writable id, missing name/type and added exception). "
        "ThreatIntel's response ancestry is supported, but its frozen PUT is unassociated and request identity remains "
        "strict: absence of a warning is not evidence that a registered derived request is accepted. "
        "These remain explicit owner/modeling decisions, not broad-linter special cases.", "",
        "## Code-backed representatives", "",
        "Excerpts are verbatim pinned authored source and saved Swagger, not invented compiling examples. "
        "Resolved gaps retain their original example and current observed disposition.", "",
    ])
    for index, example in enumerate(read(root, "instance-examples.json")):
        lines.extend([
            f'<a id="example-{index}"></a>', f'### {example["title"]}', "",
            f'**Project/API version:** {code(example["project"])} / {code(example["apiVersion"])}. '
            f'**Source:** {example["sourceLink"]}, lines {example["startLine"]}-{example["endLine"]}.', "",
            "```typespec", example["source"].rstrip(), "```", "",
            "```json", json.dumps(example["swagger"], indent=2), "```", "",
            "**Observed comparison / gap analysis and decision:** " + example["explanation"], "",
        ])
    outputs["gap-analysis.md"] = "\n".join(lines) + "\n"

    inventory = [
        "# Exact operation/model correspondence", "",
        f'Accounts for all {len(groups)} original member-check contexts, '
        f'{summary["swaggerRaw"]} raw Swagger findings and {len(findings)} configured TypeSpec findings. '
        "Separate mapping membership is retained; counts do not imply a cross-product of rule equivalences.", "",
        "## Differing projects", "",
        "| Project | Swagger raw / checks | TypeSpec raw | Credited findings |",
        "| --- | --- | --- | --- |",
    ]
    differing_projects = {
        group["project"] for group in groups if not group["mappedNativeFindingIds"]
    } | {finding["project"] for finding in extras}
    for row in data["summary"]["projects"]:
        if row["project"] in differing_projects:
            inventory.append(
                f'| [{code(row["project"])}](instances/{project_anchor(row["project"])}.md) | '
                f'{row["swaggerRaw"]} / {row["swaggerCheckGroups"]} | {row["nativeFindings"]} | {row["mappedFindings"]} |'
            )
    inventory.extend([
        "", "## Identity and attribution", "",
        "All raw observations resolve against the immutable dataset using exact reported/input document attribution, "
        "route/operation or referenced schema JSON pointer. Group identity retains member, project, resolved document, "
        "route and complete compared schema context; repeated reference invocations are retained as raw IDs. "
        "A cross-method path comparison is one member check, not one invented violation per method. "
        "Native findings are matched only after checking the relevant family, effective model, canonical resource, "
        "actual selected status/body and source/latest-version agreement. Wrong-parent co-occurrence and collection "
        "wrappers containing the same canonical item receive no different-resource-item credit.", "",
        "Owning diagnostic callbacks retain `reportIndex`, preserving distinct reports at one location. "
        "One callback can cover multiple member contexts; overlapping mapped/owner coverage counts a context once. "
        "[Machine-readable coverage accounting](gap-assessment.json), [exact bindings](swagger-bindings.json), "
        "[all comparisons](instance-mapping.json), [directional/project recount](summary.json).", "",
        "## All original member checks", "",
        "| Member / check | Route | Raw Swagger | Corresponding TypeSpec warnings | Owning diagnostic callbacks | Disposition |",
        "| --- | --- | --- | --- | --- | --- |",
    ])
    for group in sorted(groups, key=lambda group: (group["project"], group["route"], group["rule"])):
        check = checks[group["id"]]
        inventory.append(
            f'| [{group["rule"]}: {group["id"]}]({group_link(group)}) | {code(group["route"])} | '
            f'{len(group["rawObservationIds"])} | {len(group["mappedNativeFindingIds"])} | '
            f'{distinct_callbacks([check])} | {check["coverageStatus"]} |'
        )
    inventory.extend([
        "", "## TypeSpec finding accounting", "",
        "| Source operation | Family | Disposition | Credited original check IDs |",
        "| --- | --- | --- | --- |",
    ])
    for finding in sorted(findings, key=lambda row: (row["project"], row["operation"]["operation"], row["id"])):
        inventory.append(
            f'| {source_link(finding["project"], finding["operation"])} | {finding["family"]} | '
            f'{finding["classification"]} | {", ".join(finding["mappedSwaggerGroups"]) or "(none)"} |'
        )
    inventory.extend([
        "", "[Metadata execution receipt](receipts/instance-inspection-20261105.json) records the separate mapping "
        "passes, exact saved-diagnostic reproduction, full-graph hashes and lossless relevant-target compaction. "
        "[Reproduction and limitations](evidence-details.md#read-recount-and-regenerate).",
    ])
    outputs["instance-correspondence.md"] = "\n".join(inventory) + "\n"
    projects = sorted({group["project"] for group in groups} | {finding["project"] for finding in findings})
    for project in projects:
        lines = [f"# {project}", "", "[All project differences](../instance-correspondence.md#differing-projects).", ""]
        for group in sorted((row for row in groups if row["project"] == project), key=lambda row: (row["route"], row["rule"])):
            check = checks[group["id"]]
            lines.extend([
                f'<a id="s-{group["id"]}"></a>', f'## {group["rule"]}: {group["id"]}', "",
                f'**Route/document:** {code(group["route"])}; {code(group["document"])}.', "",
                f'**Observed:** {len(group["rawObservationIds"])} Swagger raw / 1 member check; '
                f'{len(group["mappedNativeFindingIds"])} corresponding configured TypeSpec warnings; '
                f'{len(group["sameOperationNativeFindingIds"])} same-operation findings (not automatically credited); '
                f'{distinct_callbacks([check])} captured owning callbacks before suppression.', "",
                f'**Coverage status:** {check["coverageStatus"]}. **Classification:** {group["classification"]}.', "",
                "```json",
                json.dumps({
                    "swaggerOperations": group["swaggerOperations"],
                    "typeSpecSourceBindings": [
                        operation_evidence(operation)
                        for binding in group["typeSpecSourceBindings"] for operation in binding["operations"]
                    ],
                    "selectedVersionOperationIdentities": [
                        operation["operationKey"]
                        for binding in group["typeSpecSelectedBindings"] for operation in binding["operations"]
                    ],
                    "mappedNativeFindingIds": group["mappedNativeFindingIds"],
                    "ownerReports": check["ownerReports"],
                    "rawObservationIds": group["rawObservationIds"],
                }, indent=2), "```", "",
                "**Gap analysis and decision:** " + decisions[check["decision"]]["recommendation"], "",
            ])
        for finding in (row for row in findings if row["project"] == project and not row["mappedSwaggerGroups"]):
            lines.extend([
                f'## Additional comparison: {finding["operation"]["operation"]}', "",
                f'{source_link(project, finding["operation"])}; **{finding["classification"]}**.', "",
                "```json", json.dumps({
                    "diagnostic": finding["finding"], "operation": operation_evidence(finding["operation"]),
                    "selectedVersionOperationIdentities": [
                        operation["operationKey"] for operation in finding["selectedVersionOperations"]
                    ],
                    "emittedBindings": finding["emittedBindings"],
                }, indent=2), "```", "",
                "**Gap analysis and decision:** " + NATIVE_ACTIONS[finding["classification"]], "",
            ])
        outputs[f"instances/{project_anchor(project)}.md"] = "\n".join(lines) + "\n"
    lines = [
        "# Independent mapping project and directional differences", "",
        "Project overlap is a population guard, not member-check coverage. The two mappings are reported separately; "
        "opposing project gaps never cancel. All exact comparison dispositions are in "
        "[the target inventory](instance-correspondence.md).", "",
    ]
    for mapping in mappings:
        scope = mapping["assessment"]
        sets = scope["projectGrouping"]
        lines.extend([
            f'## {mapping["mapping"]["name"]}', "",
            f'All {scope["selectedProjects"]} projects succeeded. Swagger projects: {sets["swagger"]}; '
            f'TypeSpec: {sets["native"]}; both: {sets["both"]}; Swagger-only: {sets["swaggerOnly"]}; '
            f'TypeSpec-only: {sets["nativeOnly"]}.', "",
            f'Raw directional excess: Swagger-higher {scope["swaggerHigherExcess"]}; '
            f'TypeSpec-higher {scope["nativeHigherExcess"]}; absolute difference {scope["absoluteDifference"]}. '
            "Source-location and JSON-path summaries are conservative identities, not equivalent violations.", "",
            "| Project | Swagger raw | TypeSpec raw | TypeSpec minus Swagger | Absolute difference | Relative difference |",
            "| --- | --- | --- | --- | --- | --- |",
        ])
        for row in scope["projects"]:
            if not row["swagger"] and not row["native"]:
                continue
            lines.append(
                f'| [{code(row["project"])}](instances/{project_anchor(row["project"])}.md) | '
                f'{row["swagger"]} | {row["native"]} | {row["nativeMinusSwagger"]} | '
                f'{row["absoluteDifference"]} | {row["relativeDifference"]:.6f} |'
            )
        lines.append("")
    lines.extend([
        "Complete population, unchanged zeros, member-responsible project sets, raw/location/route identities and "
        "all signed/absolute/relative differences are retained in [summary.json](summary.json).",
    ])
    outputs["project-differences.md"] = "\n".join(lines) + "\n"
    lines = [
        "# Diagnostic inventory", "",
        "Configured findings are preserved without suppression adjustment. Owning diagnostic callbacks before "
        "suppression are separate evidence in [gap-probes.json](gap-probes.json), credited by "
        "[gap-assessment.json](gap-assessment.json). The combined list is an inventory of two independent "
        "mappings, not a general many-to-many comparison.", "",
        "| Swagger member | Raw | Grouped original member checks | Corresponding configured-warning contexts |",
        "| --- | --- | --- | --- |",
    ]
    for member in data["summary"]["members"]:
        lines.append(
            f'| {member["rule"]} | {member["raw"]} | {member["groups"]} | '
            f'{accounting["byMember"][member["rule"]]["mappedWarningContexts"]} |'
        )
    lines.extend([
        "", "## Every configured TypeSpec diagnostic", "",
        "| Project / source | Rule | Family | Diagnostic |",
        "| --- | --- | --- | --- |",
    ])
    for finding in findings:
        lines.append(
            f'| {code(finding["project"])} {source_link(finding["project"], finding["operation"])} | '
            f'{code(finding["finding"]["rule"])} | {finding["family"]} | {code(finding["finding"]["message"])} |'
        )
    lines.extend([
        "", "Every raw Swagger occurrence, validator input/reported document, JSON path and source attribution remains "
        "in [observations.json](observations.json) and [swagger-bindings.json](swagger-bindings.json). "
        "All raw-to-check IDs and exact bodies are in [instance-mapping.json](instance-mapping.json).",
    ])
    outputs["diagnostic-inventory.md"] = "\n".join(lines) + "\n"
    return outputs


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=ROOT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    for name, text in render(args.root).items():
        target = args.root / name
        if args.verify:
            def normalized(value):
                value = re.sub(
                    r"^\|[-:|\s]+\|$",
                    lambda match: re.sub(r"-{3,}", "---", match.group()),
                    value, flags=re.MULTILINE,
                )
                return re.sub(r"\s+", "", value)

            assert normalized(target.read_text(encoding="utf-8")) == normalized(text), name
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8", newline="\n")
