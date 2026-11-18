# Supporting evidence and recovery

## Assessment boundary

These are the historical attribution inputs. The separate
[review-fix validation](#review-fix-validation-2026-11-18) records the current
candidate without relabeling historical suppression capture as current.

| Input                  | Pinned identity                                                    |
| ---------------------- | ------------------------------------------------------------------ |
| Candidate              | `779b3c409a5c4c7fede806ff552787ba706eb215`                         |
| Candidate core         | `f87a4e2d51c5cc0b3d995d4c7542578d55799804`                         |
| Tooling                | `402e3fb202e9a16f0a8c7dfc1b799098cfba879d`                         |
| Frozen specs           | `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`                         |
| Swagger baseline       | `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995` |
| ARM staging supplement | `e0a2c22b857b13fa8ccf318bff1c8a6beaf367e1a1210cbc71cf7161fd86d482` |

One explicit mapping compares **PutRequestResponseSchemeArm,
ConsistentResponseSchemaForPut, PutGetPatchResponseSchema and
XmsResourceInPutResponse** with the existing enabled
`@azure-tools/typespec-azure-resource-manager/arm-resource-operation-response`.
Native executes once and is counted once. Body/Core owners are supplemental
correspondence evidence, not additional selected mapping IDs.

The final run covers all **487** frozen projects with `scope: source`,
`baseline-policy: frozen-reference`, no filter/limit and concurrency two.
Swagger generation and validator execution are **not run**: the pinned baseline
and supplement are verified and reused. The staging member is not interpreted as
a missing production zero. Actual runtime is **Node 26.13.0**, specs **pnpm
12.6.0**, Python **3.13.17**; this is not the historical producer's runtime.
Mise was checked, but its Node selector still resolved the actual global binary.
The historical-reference policy does not require identical runtime versions.

[Run manifest](runs/20261106-779b3c409-native-resource-contract/manifest.json),
[coverage](runs/20261106-779b3c409-native-resource-contract/coverage.json),
[pinned plan](receipts/final-plan-779b3c.json) and
[source/build/archive attestation](receipts/artifact-provenance-779b3c.json)
retain the selection and provenance. The main report's raw totals come from
this run, not the rejected extension-oriented implementation. Its previous
source, two mappings and results remain historical evidence only.

## Native policy and resolver boundary

Canonical request/response checks still use complete resource registrations.
The added PUT identity pass uses **only `resolveArmResources()`**: resource
lifecycle arrays, lists, actions, associated operations and provider operations.
It selects actual HTTP PUTs owned by the project in an ARM namespace, deduplicates
operations, and, at this historical source, chooses body-bearing 200 before 201.
The review correction below checks both statuses. Void/bodyless responses remain
with their existing owners.

A resource is established by ARM registration, native resource-base ancestry or
an explicit custom-resource declaration. Emission options and OpenAPI overrides
neither create nor erase identity. There is no extension read, emitted-Swagger
simulation or field-shape heuristic. A canonical response failure prevents a
second resource-identity warning on that operation.

Replacing all existing traversal with the resolver would lose LIST/PATCH-only
checks: those registrations need not establish a read/create resource identity.
Existing traversal is therefore preserved, **not used as fallback enumeration
for the added PUT check**. Minimal LIST/PATCH reproductions are reported in
[#5994](https://github.com/Azure/typespec-azure/issues/5994).
[#5899](https://github.com/Azure/typespec-azure/issues/5899) instead concerns
splitting read/create identities and attaching a list to only one.
The operation-derived resource list is not a universal model inventory.

The remaining **10 non-resource PUT contexts / 108 repeated Swagger findings**
are all Microsoft.Network interface operations marked as actions on targets
without ARM resource declarations. They fall between registered-model scanning
and provider-operation filtering. Three minimal controls and an exact-head
probe of all ten establish this distinct mechanism, reported in
[#5995](https://github.com/Azure/typespec-azure/issues/5995).
The API must expose an unresolved operation or diagnose the modeling
prerequisite; the linter does not fabricate resources or bypass the resolver.
[Probe receipt](receipts/resolver-omissions-779b3c.json).

## Exact correspondence and suppression

All **433** frozen Swagger observations retain their original member,
validator-input/reported document and JSON path. They resolve to **277**
member-check contexts: `(member, project, resolved document, exact route,
compared schema context)`. Different members or comparisons sharing a location
are not deduplicated; repeated reference invocations remain raw observations.

One metadata pass covers the union of Swagger-affected and configured
native-affected projects. Every project must reproduce its fresh saved
configured diagnostics exactly and have no HTTP metadata diagnostics.
[Execution and graph hashes](receipts/instance-inspection-20261106.json).
Compaction retains every finding/callback target and original comparison route
in both source and selected-version graphs; full graphs remain in the asset.

Attribution checks the actual predicate, canonical effective model, status,
body kind/declaration and source/selected-version identity. A canonical warning
receives resource-response credit only for the corresponding **non-resource**
selected body; a wrong genuine resource is a different canonical comparison.
Native-valid but unmarked Swagger is an intentional representation difference,
not a diagnosed native violation. Route or message co-occurrence is insufficient.

Actual selected-rule and existing-owner listeners are executed before authored
suppression; captured diagnostic callbacks **count as diagnostics**. Configured
raw totals remain unchanged. One callback can cover several member contexts,
and overlapping owner/selected coverage counts each context once. This
affected-union inspection does **not** establish a whole-corpus
suppression-adjusted raw total. Source-versus-latest-version comparison is not
universal version-aligned or structural equivalence.

[Coverage decisions](gap-assessment.json), [owner/registry probes](gap-probes.json),
[exact inventory](instance-correspondence.md), [source/selected metadata](instance-inputs.json),
[Swagger bindings](swagger-bindings.json) and [directional/project differences](project-differences.md)
retain both matching and one-sided evidence. All additional native findings
have individual dispositions. No universal equivalent-defect percentage is claimed.

## Validation and CI

**922 distinct package tests are verified.** The initial 87-file invocation
passed 86 files; the added virtual-resource fixture lacked `@path`, causing 23
failures in the remaining file. After fixing that fixture, all **73** tests in
that file passed. This is not a claim that the initial full invocation was green.

Final ARM/rulesets builds, type-aware lint, formatting, spelling, Chronus and
whitespace checks passed. Exact authored/generated incorrect and correct
documentation snippets compiled with their expected diagnostics.
**33 selected injected controls** verify the final packed rule, native identities,
invalid bodies, status selection, canonical deduplication, default activation
and authored suppression. **37 portable controls passed**; six fixtures requiring
an unrelated absent migration are explicitly non-applicable, not passes.
Six inspector controls verify callback capture and configured equality; two
versioned metadata controls verify resource-base and virtual-resource identity
and declaration correspondence through an actual versioned property removal.
The three resolver controls above are additional API probes, not added to the
33 selected controls or silently treated as full-corpus coverage.

[Validation record](validation.json), [selected controls](receipts/injected-controls-779b3c.json),
[metadata controls](receipts/inspector-preflight-779b3c.json) and
[versioned controls](receipts/projected-resource-controls-779b3c.json).
All 15 archives have source-to-payload lineage; obsolete marker-rule output is absent.

Frozen-corpus completion is **not a green PR CI claim**. At the assessed head,
**41 checks succeeded, one was neutral and only Azure REST API Specs failed**.
The moving check assessed 605 projects: 193 passed and 412 failed, with 845
common-types-version diagnostics and 306 response-rule diagnostics (168 request
mismatches, 73 canonical-response mismatches, 29 absent requests and 36 native
resource-response findings). These are different sources/dependencies, not
frozen-corpus counts or a universal classification of service defects.
[Exact failures](receipts/ci-rest-api-specs-779b3c.json);
[all checks and mergeability](receipts/ci-final-779b3c.json).
Valid new diagnostics are not disabled or silently suppressed to manufacture a
pass. The PR is mergeable; being behind `main` is not a content conflict.

Separate draft [spec PR #47952](https://github.com/Azure/azure-rest-api-specs/pull/47952)
adds three missing create/update registrations. Five all-version OpenAPI outputs
are byte-identical; ten public TCGC outputs differ only in the source-version
fingerprint. Full SDK generation was not performed, and omitted internal
`__raw` prevents claiming specialized ARM SDK neutrality. These modified specs
are **not used or credited** in the frozen comparison.
[Compatibility receipt](receipts/spec-followup-compatibility-20261105.json).

## Read, recount and regenerate

[native-asset.json](native-asset.json) identifies the new immutable fork release,
checksum and download URL. It retains all 15 package archives, original worker
inputs/results/logs, full metadata graphs, controls, build/source provenance,
orchestration scripts and a saved-analysis snapshot. Its index records original
and published hashes. Text paths are sanitized; package archives are unchanged.
Report control copies trim trailing blank-line whitespace without moving lines;
the asset retains the original executed inputs.
Prior assets are preserved. Installed dependencies and the separately published
shared Swagger corpus are not duplicated.

Recover the baseline from the
[pinned descriptor commit](https://github.com/msyyc/typespec-azure/tree/1c9d2b0e6a596754af1aa793b1906ff3c4ef2bd6)
and the supplement from its
[pinned descriptor commit](https://github.com/msyyc/typespec-azure/tree/feec4bab366c373380fbe1b5528faa12e7233cfe).
[Frozen specs](https://github.com/msyyc/azure-rest-api-specs/tree/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9)
remain independently fetchable, separate from authored follow-ups.

From the published report directory, saved-input verification requires no compilation:

```powershell
python -B analyze-instances.py --root .
python -B assess-gaps.py --verify
python -B -m unittest test_instance_analysis.py test_reanalyze.py
python -B reanalyze.py --verify-inventory
python -B render-instances.py --verify
```

Independent [remote recovery](receipts/remote-recovery-779b3c.json) downloads the
new asset, verifies its checksum and every indexed file, and repeats attribution,
suppression credit, gap decisions, directional recount, rendering and tests.
It is **saved-input recovery and reanalysis, not a fresh whole-corpus execution**.
The immutable snapshot predates that post-publication recovery receipt; the
branch retains the final validation and recovery records.
Later report-only wording changes reuse the same observations. The asset's
recovery receipt verifies its measurement snapshot, not the refreshed wording;
the branch's renderer reproduces the current reports from the unchanged JSON.

For a full native rerun, recover and verify both baseline assets, frozen specs,
the exact tooling/candidate/core commits and all package archives. Use the
recorded actual runtime/package manager/registry, not arbitrary latest
dependencies. Restore sanitized path tokens to explicit verified local roots.
Run `native-coverage.ts` once with all four `--validator-rule` selectors and
exactly one `--tsp-rule`, the baseline and staging supplement, a new empty
output directory, `--baseline-policy frozen-reference`, `--scope source`, no
filter/limit and concurrency two. Do not regenerate Swagger or run validators.
The asset's `orchestration\run-full.ps1` retains the exact command and gate.

Then run the retained finishing script's `export`, `inspect` and `assess`
stages. Require full-population success and exact configured-diagnostic
reproduction before attribution. Regenerate reports with the committed
renderer and run the saved-data tests/integrity checks. Failed or incomplete
attempts must be preserved, not overwritten or called completed coverage.

## Review-fix validation (2026-11-18)

The final review-fix source is
[`6981ba45ae8b00fa2849b24b7aca8e11544df9de`](https://github.com/Azure/typespec-azure/commit/6981ba45ae8b00fa2849b24b7aca8e11544df9de),
with core `683031f809a3394a374c21ed587979277f6dd5c7`. The frozen specs,
tooling, Swagger baseline and staging supplement in the historical input table
are unchanged. The final gate used the same four-to-one mapping, source scope,
concurrency two, frozen-reference policy and no filter/limit. Its coordinator
held the machine/user-wide exclusive corpus lock through the runner and children.
There was **no Swagger generation or validator execution**.

All **487 projects succeeded**, with zero failed or unassessed. The selected
rule's **283 raw, default and aligned diagnostics** are exactly unchanged,
including each project's code, full message, authored path/line/column and
multiplicity. All recorded loaded candidate entrypoints match the new package
archive payloads. Equal totals alone were not the acceptance test.
[Manifest](runs/20261118-6981ba45a-native-resource-contract/manifest.json),
[coverage](runs/20261118-6981ba45a-native-resource-contract/coverage.json),
[accepted exact comparison](receipts/review-fix-20261118-comparison.json),
[plan](receipts/review-fix-20261118-plan.json) and
[post-run source/artifact attestation](receipts/review-fix-20261118-attestation.json).

Ambient diagnostics changed in 387 projects. Every change belongs to an upstream
rule change already present at admission head `751d9f098`, not this cycle:

| Ambient rule                    | Removed / added | Upstream explanation                                                                                                                                      |
| ------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `arm-common-types-version`      | 737 / 0         | [#6000](https://github.com/Azure/typespec-azure/commit/d59eb4736) reverted the latest-version requirement; all removed messages compare v6 with v3/v4/v5. |
| `no-generic-numeric`            | 0 / 3           | [#5975](https://github.com/Azure/typespec-azure/commit/70315a314) expanded property and array/record checks; the new findings concern decimal types.      |
| `no-reserved-resource-property` | 0 / 1           | [#5892](https://github.com/Azure/typespec-azure/commit/af1fb8415) added the exact reported reserved property, `systemData`.                               |
| `unsupported-scope`             | 0 / 5           | [#5997](https://github.com/Azure/typespec-azure/commit/0afb2ab5b) introduced this rule; four findings name `js`, one names `parameters`.                  |

This is a current-closure comparison with a frozen native reference, **not an
isolated causal comparison of otherwise identical historical dependencies**.
The full comparison retains every ambient target, not just these code totals.
No sibling-rule production code was modified by this review fix.

The correction for [R5423-11](https://github.com/Azure/typespec-azure/pull/5423#discussion_r4608390423)
requires both body-bearing 200 and 201 responses to be native resources, with
one diagnostic per operation. The corpus contains no observed selected-rule
change exercising this distinction. Instead, the canonical unit case
`requires resource bodies for both 200 and 201, reporting once: %s`
fails against the original code when 200 is a resource and 201 is a DTO, and
passes with the fix. Its reverse/both-invalid cases and
`accepts resource bodies at both 200 and 201` provide contrasting controls.
Resolver-only enumeration and native resource-identity predicates are unchanged.

Final local validation: **86 focused ARM/ruleset tests**, native dependency
closure/final ARM builds, `pnpm format`, `pnpm lint`, targeted type-aware lint,
spelling, Chronus and whitespace checks passed. **36 injected selected controls**
and **37 portable controls** passed; six unrelated fixtures remain explicitly
non-applicable. The actual published incorrect/correct snippets were checked as
literal document content at SHA-256
`7b9407a6f3488d729613afa636bcc335318d823ca49d9c743afad1316ae60a32`,
using `ArmResourceCreateOrReplaceSync<Widget>` and an explicit selected-rule
activation: one diagnostic versus zero, without compiler errors. This is a
one-time receipt, not continuous documentation testing or a Markdown parser.

[The new immutable asset](review-validation-asset.json) retains all 15
byte-identical archives, all worker receipts/inputs/logs, controls, exact
comparison, orchestration and local validation logs/helpers. Downloaded recovery
verified **1,690 indexed files**, all 15 archives and the prior published inputs,
then recomputed the exact selected and ambient comparison.
[Recovery receipt](receipts/review-fix-20261118-recovery.json).
Recovery replays saved evidence; it does not rerun the corpus.

The historical **433/200 attributed comparison**, including 17 captured
suppressed owning diagnostics, remains unchanged and is not remeasured by this
run. The pre-existing main-report/renderer mismatch was reconciled while
preserving the authored four-section layout and attribution arithmetic; the
obsolete raw-283 main-report layout was not restored. The companion suppression
PR remains pinned to its earlier CI/head and was not refreshed. None of these
local results establishes green current PR CI or merge readiness.
