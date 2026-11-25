"""Render the native many-to-one assessment and its exact per-member evidence."""

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
MEMBERS = {
    "PutRequestResponseSchemeArm": (
        "put-request-response-scheme-arm", "put-request-response-scheme",
        "Not fully equivalent. Registered create/update requests are checked against their canonical resource, but unassociated PUTs and incorrect resource associations leave request-contract gaps.",
    ),
    "ConsistentResponseSchemaForPut": (
        "consistent-response-schema-for-put", "consistent-response-schema-for-put",
        "The observed genuine success-body difference is diagnosed. The TypeSpec linter intentionally avoids the Swagger linter bug that compares resolved objects by identity and reports identical 200/201 schema references as different. This establishes coverage of the observed valid check, not universal structural equivalence.",
    ),
    "XmsResourceInPutResponse": (
        "xms-resource-in-put-response", "with-xms-resource",
        "Not equivalent to extension-presence checking. TypeSpec resource declarations determine response identity, regardless of emission flags or OpenAPI overrides. PUTs omitted by resolveArmResources remain undiagnosed.",
    ),
    "PutGetPatchResponseSchema": (
        "put-get-patch-response-schema", "put-get-patch-schema",
        "Not equivalent. Existing response-body diagnostics cover empty 200 responses, including authored suppressions, but SyncJob's PUT/GET shape difference remains undiagnosed. Excluding no-content and collection/item comparisons is recommended, not approved.",
    ),
}
NATIVE_ACTIONS = {
    "additional-native-resource-response-policy": "A resolver-exposed PUT returns a non-resource body without a corresponding frozen marker warning. Inspect source/latest-version identity and explicit extension overrides; do not make those overrides define native identity.",
    "additional-canonical-response-policy": "Review the authored canonical resource and actual success body. Parent/child, command, polling-result and collection-role associations are not automatically original cross-method comparisons; prefer wire-compatible spec fixes over weakening the rule.",
    "additional-missing-request-policy": "Additional body-existence policy; the Swagger selector skips missing bodies. Review the wire contract rather than inventing a request for count parity.",
    "same-operation-different-comparison": "Review the canonical association or selected status/body. A real warning on the route receives no credit for a different comparison.",
    "source-only-operation-not-in-selected-version": "Retain source diagnostics and use supported version alignment for selected-version parity; do not suppress them to equalize totals.",
    "additional-request-check-outside-swagger-200-201-selector": "Keep broader registered-request enforcement separate from the Swagger 200/201 selector.",
    "native-only-request-policy-or-schema-identity-unresolved": "Unresolved source/schema identity; establish the actual contract before a source change or equivalence claim.",
}
SHORT_DECISIONS = {
    "recover-registered-put": "Missing resolved occurrence/association. Follow the resolver API decision; investigate that prerequisite without a legacy discovery fallback.",
    "body-policy-owner": "Review the authored suppression and wire contract; do not duplicate the existing response-body check.",
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
    "native-resource-representation": "The selected body is a native resource. Marker/emission differences do not make it invalid; intentionally do not reproduce extension-level parity.",
    "resolver-operation-gap": "Ten marked Network PUTs target models without ARM declarations. Reported in #5995; resolve the API/modeling prerequisite, not by fallback enumeration.",
    "standalone-operation-prerequisite": "Standalone operations violate required interface authoring. The prerequisite is not credited as a body diagnostic.",
    "response-resource-policy": "Inspect the exact selected native body, resolver exposure and callbacks; no extension-based inference or unrelated-warning credit.",
}
CONTRACT_DECISIONS = (
    "custom-lifecycle-registration", "custom-collection-request", "custom-command-request",
    "unregistered-entity-request", "parent-canonical-association",
    "supported-polymorphism", "cross-method-entity-contract",
)


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


def diagnostic_counts(rows):
    configured = len({identity for row in rows for identity in row["mappedWarningIds"]})
    configured += len({
        json.dumps(report, sort_keys=True)
        for row in rows for report in row.get("ownerConfiguredReports", [])
    })
    selected = {identity for row in rows for identity in row.get("mappedPredicateIds", [])}
    before_suppression = len(selected) + distinct_callbacks(rows)
    return configured, before_suppression


def diagnostic_components(rows):
    """Keep shared callbacks together without merging distinct reports."""
    parents = {row["checkId"]: row["checkId"] for row in rows}
    tokens = {}
    owners = {}

    def find(key):
        while parents[key] != key:
            parents[key] = parents[parents[key]]
            key = parents[key]
        return key

    for row in rows:
        identity = row["checkId"]
        assert not row.get("mappedWarningIds") or row.get("mappedPredicateIds"), identity
        tokens[identity] = {"selected:" + item for item in row.get("mappedPredicateIds", [])}
        tokens[identity].update(
            "owner:" + hashlib.sha256(json.dumps(report, sort_keys=True).encode()).hexdigest()
            for report in row.get("ownerReports", [])
        )
        for token in tokens[identity]:
            if token in owners:
                parents[find(identity)] = find(owners[token])
            else:
                owners[token] = identity
    components = collections.defaultdict(list)
    for row in rows:
        components[find(row["checkId"])].append(row)
    result = []
    for component in components.values():
        selected = set().union(*(tokens[row["checkId"]] for row in component))
        raw = sum(row["rawObservations"] for row in component)
        result.append({
            "checkIds": sorted(row["checkId"] for row in component),
            "decisions": sorted({row["decision"] for row in component}),
            "diagnosticIds": sorted(selected),
            "swaggerRaw": raw, "typeSpecReported": len(selected),
            "swaggerMinusTypeSpec": raw - len(selected),
            "project": component[0]["project"],
        })
        assert len({row["project"] for row in component}) == 1
    return sorted(result, key=lambda row: row["checkIds"])


def operation_evidence(operation):
    return {
        key: operation[key] for key in (
            "operation", "sourceFile", "line", "verb", "path", "request", "associations", "responses",
            "resolverExposed", "projectOwned", "inInterface", "armNamespace",
        ) if key in operation
    }


def render(root):
    data = read(root, "instance-mapping.json")
    assessment = read(root, "gap-assessment.json")
    summary = read(root, "summary.json")
    task = read(root, "task.json")
    validation = read(root, "validation.json")
    groups = data["swaggerGroups"]
    findings = data["nativeFindings"]
    excluded_policies = {
        "source-only-operation-not-in-selected-version",
        "additional-missing-request-policy",
        "additional-canonical-response-policy",
        "same-operation-different-comparison",
        "additional-request-check-outside-swagger-200-201-selector",
    }
    assert all(
        finding["mappedSwaggerGroups"] or finding["classification"] in excluded_policies
        for finding in findings
    ), "Investigate in-scope or unassessed TypeSpec-only findings before assigning an excluded count"
    checks = {row["checkId"]: row for row in assessment["checks"]}
    decisions = {row["decision"]: row for row in assessment["decisions"]}
    accounting = assessment["coverageAccounting"]
    components = diagnostic_components(assessment["checks"])
    mappings = summary["mappingAssessments"]
    outputs = {}

    def scoped_mapping(rule):
        return next(row for row in mappings if rule in row["mapping"]["validatorRules"])

    def group_link(group, prefix=""):
        return f'{prefix}instances/{project_anchor(group["project"])}.md#s-{group["id"]}'

    def coverage_sentence(rows):
        mapped = sum(bool(row["mappedWarningIds"]) for row in rows)
        hidden = sum(bool(row.get("mappedPredicateIds")) and not row["mappedWarningIds"] for row in rows)
        owner = sum(
            bool(row["ownerReports"]) and not (row["mappedWarningIds"] or row.get("mappedPredicateIds"))
            for row in rows
        )
        residual = [
            row for row in rows
            if not (row["mappedWarningIds"] or row.get("mappedPredicateIds") or row["ownerReports"])
        ]
        false = sum(row["decision"] == "upstream-identity-bug" for row in residual)
        excluded = sum(row["decision"] in ("bodyless-comparator-overreach", "collection-comparator-overreach") for row in residual)
        native = sum(row["decision"] == "native-resource-representation" for row in residual)
        standalone = sum(row["decision"] == "standalone-operation-prerequisite" for row in residual)
        resolver = sum(row["decision"] == "resolver-operation-gap" for row in residual)
        remaining = len(residual) - false - excluded - native - standalone - resolver
        sources = []
        if mapped:
            sources.append(f"{mapped} by corresponding configured diagnostics")
        if hidden:
            sources.append(f"{hidden} additional contexts by the selected rule's captured diagnostics before suppression")
        if owner:
            sources.append(f"{owner} additional checks by existing owning diagnostics captured before authored suppression")
        residuals = []
        if false:
            residuals.append(f"{false} confirmed Swagger linter false positives")
        if excluded:
            residuals.append(f"{excluded} proposed no-content/collection exclusions awaiting approval")
        if native:
            residuals.append(f"{native} intentional TypeSpec-resource/Swagger-marker differences")
        if standalone:
            residuals.append(f"{standalone} unsupported standalone-operation contexts")
        if resolver:
            residuals.append(f"{resolver} checks missed because the resolver omits the PUT")
        if remaining:
            noun = "check" if remaining == 1 else "checks"
            residuals.append(f"{remaining} modeling or contract {noun} still unresolved/deferred")
        diagnosed = mapped + hidden + owner
        verb = "is" if diagnosed == 1 else "are"
        text = f"{diagnosed} of {len(rows)} original Swagger check contexts {verb} diagnosed"
        text += ": " + "; ".join(sources) + ". " if sources else ". "
        if residuals:
            text += "Remaining: " + "; ".join(residuals) + ". "
        return text + (
            "Suppressed diagnostics count toward this assessment, not the configured raw total. "
            "Check contexts are not confirmed service defects; equivalent-defect coverage remains unassessed."
        )

    def difference_table(rule=None, prefix=""):
        rows = [row for row in assessment["checks"] if rule is None or row["member"] == rule]
        selected = diagnostic_components(rows)
        buckets = collections.defaultdict(list)
        for component in selected:
            if component["swaggerMinusTypeSpec"]:
                buckets[tuple(component["decisions"])].append(component)
        lines = [
            "`Raw / grouped` means individual Swagger findings / distinct check contexts "
            "(Swagger member, project, resolved document, route and schema comparison). "
            "The TypeSpec column includes corresponding captured suppressed diagnostics. "
            "Check contexts sharing a diagnostic are kept in one connected component; distinct callbacks "
            "remain distinct. This makes source/emission multiplicity and overlapping owning diagnostics "
            "countable without treating contexts as equivalent defects.", "",
            "| Difference (with evidence) | Swagger diagnostics (raw / grouped) | TypeSpec diagnostics for the same check | analysis |",
            "| --- | --- | --- | --- |",
        ]
        contributions = []
        for category, bucket in sorted(buckets.items()):
            evidence = []
            actions = []
            for decision in category:
                if decision == "corroborated":
                    evidence.append(f"[Already-diagnosed count differences]({prefix}gap-analysis.md#corroborated-count-only)")
                    actions.append("Count-only difference: repeated emitted occurrences or several distinct owning diagnostics support the same check; do not change production semantics to equalize counts.")
                else:
                    evidence.append(f'[{decisions[decision]["title"]}]({prefix}gap-analysis.md#{decision})')
                    actions.append(SHORT_DECISIONS.get(decision, decisions[decision]["recommendation"]))
            raw = sum(row["swaggerRaw"] for row in bucket)
            reported = sum(row["typeSpecReported"] for row in bucket)
            context_count = sum(len(row["checkIds"]) for row in bucket)
            contributions.append(raw - reported)
            lines.append(
                f'| {"; ".join(evidence)} | {raw} / {context_count} | {reported} | {" ".join(actions)} |'
            )
        raw = sum(row["swaggerRaw"] for row in selected)
        reported = sum(row["typeSpecReported"] for row in selected)
        matching = sum(row["swaggerRaw"] for row in selected if not row["swaggerMinusTypeSpec"])
        assert raw - reported == sum(contributions)
        expression = " + ".join(f"({value:+d})" for value in contributions) or "0"
        lines.extend([
            "", f"**Raw-count reconciliation:** `{raw} - {reported} = {raw - reported} = {expression}`. "
            f"The other {matching} Swagger / {matching} TypeSpec diagnostics belong to balanced components. "
            "Balanced totals are not an equivalence claim; opposing component/project differences remain in "
            f"[the exact accounting]({prefix}diagnostic-count-components.json) and "
            f"[directional project evidence]({prefix}project-differences.md).",
        ])
        return lines + [""]

    behaviors = {
        "PutRequestResponseSchemeArm": [
            ("Resolved createOrUpdate PUT at each resource scope", "Covered",
             "Each resolved occurrence supplies the canonical model and HTTP operation; effective request identity is checked once per operation/resource pair."),
            ("Missing/void request; compliant and multipart bodies", "Covered / intentional exception",
             "Body existence is additional policy; compliant identity and multipart exemptions are controlled explicitly."),
            ("Unregistered, command, collection or wrong-parent contracts", "Partial / unresolved",
             "HTTP PUT alone does not establish a canonical resource. Separate compatibility-gated spec fixes are safer than a global structural comparator."),
        ],
        "ConsistentResponseSchemaForPut": [
            ("Actual body-bearing 200/201 responses for registered resources", "Covered for observed genuine difference",
             "Canonical consistency now inspects actual HTTP success bodies, including plain nonresource models; Quota also has an existing Azure Core diagnostic."),
            ("Equal success schemas; absent or explicit-void bodies", "Covered / scoped exemptions",
             "Equal schemas do not get an object-identity false positive. This check skips absent/void bodies; separate response-body/status rules still apply."),
        ],
        "XmsResourceInPutResponse": [
            ("Resolver-exposed ARM PUT, every body-bearing 200 and 201", "Covered",
             "Resolved resources, native resource-base ancestry, virtual and existing custom declarations are accepted. Arrays, scalars and lookalike DTOs fail. A canonical response warning avoids a duplicate resource-identity warning."),
            ("Extension overrides and custom emission options", "Intentional difference",
             "They neither create nor erase native resource identity. The linter does not inspect extensions or simulate emitted Swagger."),
            ("Absent/void body and non-PUT operations", "Outside this check",
             "Body/status rules own absent bodies; the added resource-identity check applies only to PUT."),
            ("PUTs omitted by resolveArmResources", "Missing",
             "Ten marked Network PUTs are absent from both resolver collections. Issue #5995 tracks the prerequisite; there is no fallback enumeration."),
        ],
        "PutGetPatchResponseSchema": [
            ("Resolved lifecycle actual success responses and list items", "Covered canonical-resource policy",
             "Read/create/update/list associations are traversed at each resolved scope. Arrays/value envelopes supply list items; discriminated response ancestry is preserved. Unresolved LIST/PATCH-only occurrences are not checked."),
            ("Empty 200 compared with a resource", "Covered by existing owning diagnostics",
             "Captured no-response-body callbacks remain diagnostic evidence despite authored suppression; schema equality must not replace body-existence policy."),
            ("No-content / same-item collection roles", "Recommended intentional difference",
             "Comparing absent schemas or wrapper names does not establish a different resource item. Exclusions remain recommendations awaiting approval."),
            ("SyncJob PUT/GET shape difference", "Missing / deferred",
             "The borrowed SourceControl read association diagnoses another comparison. Confirm owner intent before sharing models; one route does not justify a recursive version/visibility-aware schema matcher."),
        ],
    }

    def behavior_table(rules, prefix=""):
        lines = ["| Behavior | Result | analysis |", "| --- | --- | --- |"]
        for rule in rules:
            for behavior, result, rationale in behaviors[rule]:
                lines.append(
                    f"| {behavior} | {result} | {rationale} "
                    f"[Evidence]({prefix}gap-analysis.md#member-{MEMBERS[rule][0]}). |"
                )
        return lines + [""]

    for rule, (slug, function, _) in MEMBERS.items():
        mapping = scoped_mapping(rule)
        rows = [row for row in assessment["checks"] if row["member"] == rule]
        member = next(row for row in data["summary"]["members"] if row["rule"] == rule)
        responsible = mapping["mapping"]["nativeRules"][0]
        member_configured, member_reported = diagnostic_counts(rows)
        lines = [
            f"# {rule} migration", "", "## 1. Scope", "",
            f"The TypeSpec linter {code(responsible)} is assessed against "
            f"[`{rule}`]({UPSTREAM}docs/{slug}.md). "
            "Original migration linter PR: [Azure/typespec-azure#5423](https://github.com/Azure/typespec-azure/pull/5423).", "",
            "## 2. Coverage", "",
            f"All {summary['selectedProjects']} frozen projects succeeded; none failed or was unassessed. "
            "Counts are individual diagnostics attributed to this member's actual comparison, not the shared "
            "rule's full output. Captured suppressed findings are included only in the inspected affected union.", "",
            "| Count | Swagger linter | TypeSpec linter |", "| --- | --- | --- |",
            f'| Reported diagnostics | {member["raw"]} | {member_reported} |', "",
            f"The TypeSpec total comprises {member_configured} corresponding configured diagnostics and "
            f"{member_reported - member_configured} corresponding captured suppressed diagnostics. "
            "Other members and different canonical/source-version policies are not credited to this member. "
            "[Inclusion, exclusions and original callbacks](../../instance-correspondence.md).", "",
            "**Analysis:** " + coverage_sentence(rows), "",
            "See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ).", "",
            "## 3. Why diagnostic counts differ", "", *difference_table(rule, "../../"),
            "## 4. Function-level coverage", "", *behavior_table([rule], "../../"),
            "## NOTES", "",
            f"- **Inputs:** Assessed source `{task['candidateCommit'][:9]}`, core `{task['coreCommit'][:9]}`, "
            f"specs `{task['specsCommit'][:9]}`. Fresh source-program execution against retained latest-version Swagger; "
            "not universally version-aligned defects. [Provenance and recovery](../../evidence-details.md).",
            "- **Counting:** Distinct callbacks are retained; shared diagnostics can contribute to several member notes "
            "and must not be summed. Suppression capture is not an exhaustive corpus scan. "
            "[Component accounting](../../diagnostic-count-components.json).",
            "- **Validation:** [Assessed source and runtime gates](../../validation.json); "
            "[current head CI, separate from historical results](../../evidence-details.md#validation-and-ci).", "",
            f"[Pinned Swagger implementation]({UPSTREAM}packages/rulesets/src/spectral/functions/{function}.ts). "
            "[Shared provenance, controls, recovery and replay](../../evidence-details.md). "
            "[Exact targets](../../instance-correspondence.md).",
        ]
        outputs[f"members/{rule}/migration.md"] = "\n".join(lines) + "\n"

    links = ", ".join(
        f"[`{rule}`]({UPSTREAM}docs/{info[0]}.md)" for rule, info in MEMBERS.items()
    )
    configured, attributed = diagnostic_counts(assessment["checks"])
    selected_configured = len({identity for row in assessment["checks"] for identity in row["mappedWarningIds"]})
    owner_configured = configured - selected_configured
    additional = summary["nativeRaw"] - selected_configured
    captured = attributed - configured
    diagnosed = accounting["coveredDiagnosticContexts"]
    contexts = len(assessment["checks"])
    assert sum(row["swaggerRaw"] for row in components) == summary["swaggerRaw"]
    assert sum(row["typeSpecReported"] for row in components) == attributed
    outputs["diagnostic-count-components.json"] = json.dumps({
        "unit": "Individual diagnostic callbacks and raw Swagger occurrences. Connected components only keep shared callbacks together; they are not equivalent-defect normalization.",
        "candidateCommit": task["candidateCommit"],
        "swaggerRaw": summary["swaggerRaw"], "typeSpecReported": attributed,
        "swaggerMinusTypeSpec": summary["swaggerRaw"] - attributed,
        "components": components,
        "excludedConfiguredDiagnostics": [
            {"id": finding["id"], "project": finding["project"],
             "classification": finding["classification"], "diagnostic": finding["finding"],
             "operationKey": finding["operation"]["operationKey"],
             "emittedBindings": finding["emittedBindings"]}
            for finding in findings if not finding["mappedSwaggerGroups"]
        ],
        "byMember": {
            member: diagnostic_components([row for row in assessment["checks"] if row["member"] == member])
            for member in MEMBERS
        },
    }, indent=2) + "\n"
    outputs["migration.md"] = f"""# ARM PUT and resource-response migration

## 1. Scope

The TypeSpec linter {code(RESPONSE)} is assessed against {links}. Original migration linter PR: [Azure/typespec-azure#5423](https://github.com/Azure/typespec-azure/pull/5423).

## 2. Coverage

Fresh TypeSpec linter execution at `{task['candidateCommit'][:9]}` succeeded for all **{summary['selectedProjects']} frozen projects**, with no failed or unassessed projects. The table counts individual findings within the four Swagger linters' assessed comparisons, not all diagnostics from the mixed TypeSpec rule. Corresponding suppressed diagnostics captured in the affected-union inspection are included; this is not an exhaustive suppression-inclusive corpus count.

| Count | Swagger linter | TypeSpec linter |
| --- | --- | --- |
| Reported diagnostics | {summary['swaggerRaw']} | {attributed} |

**Counting:** The selected rule emitted {summary['nativeRaw']} configured diagnostics: {selected_configured} are attributed to the original comparisons and {additional} concern different canonical, missing-body or source-version policies. The scoped total also includes {owner_configured} configured owning diagnostics and {captured} corresponding captured suppressed diagnostics. Thus **`{attributed} = ({summary['nativeRaw']} - {additional}) + {owner_configured} + {captured}`**. Distinct diagnostics remain distinct even when they concern the same check. [Full inclusion/exclusion and callback inventory](instance-correspondence.md), [scoped count components](diagnostic-count-components.json).

**Analysis:** Corresponding diagnostics cover **{diagnosed} of {contexts} original check contexts**. A context identifies the Swagger rule, frozen project, resolved document, route and exact schema comparison; it is neither a diagnostic nor a confirmed service defect. The {contexts - diagnosed} contexts without corresponding findings include confirmed Swagger false positives, resource-marker policy differences, resolver omissions and unresolved resource/contract associations. Resolver-omitted LIST/PATCH-only occurrences are explicitly outside the implementation's traversal, not evidence of compliance. Canonical resource consistency does not implement arbitrary cross-method structural equality.

See [Why diagnostic counts differ](#3-why-diagnostic-counts-differ) for the complete signed reconciliation. All four [member assessments](gap-analysis.md) retain their own semantic limits; equal totals or project overlap cannot establish equivalent-defect coverage.

**Resolver tradeoff:** Configured findings decreased by 16: 15 GET and one POST canonical comparisons previously outside the four Swagger checks. Fresh attributed counts and the scoped gap are unchanged. [Every removed target, resolver classification and code-backed examples](resolver-analysis.md).

## 3. Why diagnostic counts differ

{chr(10).join(difference_table()).rstrip()}

## 4. Function-level coverage

| Behavior | Result | analysis |
| --- | --- | --- |
| Resolved create/update request at each scope | Covered within resolved occurrences | Effective request identity is compared with that occurrence's resource model. Several scopes are traversed without collapsing them by model. [Request checks](members/PutRequestResponseSchemeArm/migration.md). |
| Resolved lifecycle success bodies and list items | Covered canonical policy | Actual HTTP bodies and collection items use the resolved association; a warning is reported once per offending operation. This is not a generic structural cross-method matcher. [Success checks](members/ConsistentResponseSchemaForPut/migration.md), [lifecycle/list checks](members/PutGetPatchResponseSchema/migration.md). |
| Body-bearing PUT 200 and 201 resource identity | Covered for resolver-exposed ARM operations | Every body-bearing success payload is checked. Scalars, arrays and lookalike DTOs fail; canonical response failures avoid duplicate identity warnings. [Resource identity](members/XmsResourceInPutResponse/migration.md). |
| Same model at several scopes; equal bodies; resource ancestry | Covered controls | Four scope regressions also passed on the previous implementation, so they do not prove a historical miss. Multipart requests remain exempt; bodyless success responses stay with body/status policies. [Validation](validation.json). |
| Marker/emission options versus resource declarations | Intentional policy difference | Resolved/native/custom/virtual identity is retained. This change does not tighten the separate custom-marker option policy or simulate extension presence. [Evidence](gap-analysis.md#native-resource-representation). |
| Unresolved resources and legacy operation/parent contracts | Missing / unresolved | LIST/PATCH-only resource occurrences and marked non-resource PUTs can be omitted by the resolver; no legacy discovery fallback is added. Genuine uncovered comparisons and modeling decisions remain visible. [Resolver gap](gap-analysis.md#resolver-operation-gap), [contract gaps](gap-analysis.md#unresolved-contracts). |

## NOTES

- **Inputs:** Source `{task['candidateCommit'][:9]}`, actual core `{task['coreCommit'][:9]}`, frozen specs `{task['specsCommit'][:9]}`. Fresh source-program analysis reuses sealed latest-version Swagger and its staging supplement; no Swagger regeneration or version-aligned equivalence claim. [Provenance and recovery](evidence-details.md#assessment-boundary).
- **Counting:** Original configured observations, exclusions, fresh suppressed callbacks and all member scopes are retained in [exact correspondence](instance-correspondence.md), [coverage accounting](gap-assessment.json) and [count components](diagnostic-count-components.json). Suppression capture covers the inspected affected union, including previously diagnosed projects, not every suppressed declaration.
- **Validation:** Assessed unit/build/lint/docs, selected/injected controls and full-corpus results: [validation receipt](validation.json). Pending or historical external CI is not a current pass. [CI and recovery limits](evidence-details.md#validation-and-ci).
- **Separate follow-ups:** [Closed compatibility suppression proposal #48087](https://github.com/Azure/azure-rest-api-specs/pull/48087) and [draft registration PR #47952](https://github.com/Azure/azure-rest-api-specs/pull/47952) are not refreshed or credited in frozen counts. [Companion limits](companion-suppressions.md), [registration compatibility evidence](gap-analysis.md#compatibility-gated-spec-follow-ups).
"""

    lines = [
        "# Gap analysis and decision", "",
        "This appendix separates measured diagnostic coverage, semantic cause and recommended action. "
        "Recommendations are not approved policy retirements. [Migration assessment](migration.md).", "",
        "## Difference groups", "", *difference_table(),
        '<a id="corroborated-count-only"></a>', "## Already-diagnosed count differences", "",
        "The following connected components have corresponding diagnostics but different raw cardinalities. "
        "Shared selected/owning callbacks are counted once, and distinct owning reports remain distinct. "
        "These are counting differences, not missing coverage or approved policy retirements.", "",
        "| Project / exact check components | Swagger raw | TypeSpec reported | Swagger - TypeSpec |",
        "| --- | --- | --- | --- |",
    ]
    for component in components:
        if component["decisions"] == ["corroborated"] and component["swaggerMinusTypeSpec"]:
            linked = ", ".join(
                f'[{identity}]({group_link(next(group for group in groups if group["id"] == identity))})'
                for identity in component["checkIds"]
            )
            lines.append(
                f'| {code(component["project"])} / {linked} | {component["swaggerRaw"]} | '
                f'{component["typeSpecReported"]} | {component["swaggerMinusTypeSpec"]:+d} |'
            )
    lines.extend(["", "[Complete components, including balanced comparisons](diagnostic-count-components.json).", ""])
    for anchor, title, members in (
        ("proposed-comparison-exclusions", "Proposed comparison exclusions",
         ("bodyless-comparator-overreach", "collection-comparator-overreach")),
        ("unresolved-contracts", "Unresolved modeling and contract checks", CONTRACT_DECISIONS),
    ):
        lines.extend([
            f'<a id="{anchor}"></a>', f"## {title}", "",
            "This groups the main report's decision row without merging distinct member checks. "
            "The linked entries retain exact targets, coverage status and the required owner decision.", "",
            "| Difference | Swagger raw / check contexts | Recommended action and rationale |",
            "| --- | --- | --- |",
        ])
        for decision in members:
            info = decisions[decision]
            lines.append(
                f'| [{info["title"]}](#{decision}) | {info["rawObservations"]} / {info["memberChecks"]} | '
                f'{SHORT_DECISIONS[decision]} |'
            )
        lines.append("")
    for decision, info in decisions.items():
        rows = [group for group in groups if checks[group["id"]]["decision"] == decision]
        if not rows or decision == "corroborated":
            continue
        records = [checks[group["id"]] for group in rows]
        configured, before = diagnostic_counts(records)
        lines.extend([
            f'<a id="{decision}"></a>', f'## {info["title"]}', "",
            f'**Observed counts:** {sum(len(group["rawObservationIds"]) for group in rows)} Swagger raw / '
            f'{len(rows)} member checks; {configured} corresponding configured / {before} captured-before-suppression diagnostics. '
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
        "| Member / project | Swagger raw | Grouped diagnosed contexts | TypeSpec configured / before suppression |",
        "| --- | --- | --- | --- |",
    ])
    repeats = collections.defaultdict(list)
    for group in groups:
        if (group["mappedNativeFindingIds"] or group.get("mappedNativePredicateIds")) and len(group["rawObservationIds"]) > 1:
            repeats[(group["rule"], group["project"])].append(group)
    for (member, project), bucket in sorted(repeats.items()):
        configured, before = diagnostic_counts([checks[group["id"]] for group in bucket])
        lines.append(
            f'| {member} / [{code(project)}](instances/{project_anchor(project)}.md) | '
            f'{sum(len(group["rawObservationIds"]) for group in bucket)} | {len(bucket)} | '
            f'{configured} / {before} |'
        )
    lines.append("")
    for rule, (slug, _, _) in MEMBERS.items():
        member_checks = [row for row in assessment["checks"] if row["member"] == rule]
        lines.extend([
            f'<a id="member-{slug}"></a>', f"## {rule}: implemented policy and remaining boundary", "",
            coverage_sentence(member_checks), "",
            f"**Semantic assessment:** {MEMBERS[rule][2]} "
            "The resolver-only boundary and pending modeling/policy decisions remain explicit; "
            "reviewers retain the acceptance decision.", "",
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
        "The single selected native rule is counted once; per-member attribution does not imply equivalence.", "",
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
        "Selected-rule and owning diagnostic callbacks retain `reportIndex`, preserving distinct reports at one location. "
        "One callback can cover multiple member contexts; overlapping mapped/owner coverage counts a context once. "
        "[Machine-readable coverage accounting](gap-assessment.json), [exact bindings](swagger-bindings.json), "
        "[all comparisons](instance-mapping.json), [directional/project recount](summary.json).", "",
        "## All original member checks", "",
        "| Member / check | Route | Raw Swagger | Configured selected warnings | Selected callbacks before suppression | Owning callbacks | Disposition |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ])
    for group in sorted(groups, key=lambda group: (group["project"], group["route"], group["rule"])):
        check = checks[group["id"]]
        inventory.append(
            f'| [{group["rule"]}: {group["id"]}]({group_link(group)}) | {code(group["route"])} | '
            f'{len(group["rawObservationIds"])} | {len(group["mappedNativeFindingIds"])} | '
            f'{len(group.get("mappedNativePredicateIds", []))} | '
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
        "", "## Selected diagnostics absent from configured output", "",
        "These actual selected-rule callbacks still count as diagnostics. Capture covers the union of projects with "
        "original Swagger findings or configured native findings, not a new whole-corpus suppression-adjusted raw total.", "",
        "| Source operation | Diagnostic | Original member checks |",
        "| --- | --- | --- |",
    ])
    for predicate in data.get("nativePredicates", []):
        if not predicate["configuredFindingIds"]:
            inventory.append(
                f'| {source_link(predicate["project"], predicate["operation"])} | '
                f'{code(predicate["finding"]["message"])} | '
                f'{", ".join(predicate["mappedSwaggerGroups"]) or "(no attributed selected check)"} |'
            )
    inventory.extend([
        "", "[Metadata execution receipt](receipts/resolver-20261125-attestation.json) records the one mapping "
        "pass, exact saved-diagnostic reproduction, full-graph hashes and relevant-target compaction. "
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
                f'{len(group.get("mappedNativePredicateIds", []))} corresponding selected callbacks before suppression; '
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
                    "mappedNativePredicateIds": group.get("mappedNativePredicateIds", []),
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
        "# Project and directional differences", "",
        "Project overlap is a population guard, not member-check coverage. This is one many-to-one mapping; "
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
        "suppression are separate evidence in [gap-probes.json](gap-probes.json) and selected predicates in "
        "[instance-mapping.json](instance-mapping.json), credited by [gap-assessment.json](gap-assessment.json). "
        "The selected rule's full output is counted once across the four Swagger members.", "",
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
