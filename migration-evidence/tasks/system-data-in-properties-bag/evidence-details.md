# SystemDataInPropertiesBag evidence details

This appendix retains semantic evidence independently of numerical agreement. Final artifact, coverage, published evidence, and fresh input recovery receipts are available. Native implementation remains unpublished pending the required independent local review; migration is not complete.

## Frozen member contract

| Field                | Decision                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Member               | `SystemDataInPropertiesBag` only; membership revision 1, cycle 0                                                                |
| Destination          | `@azure-tools/typespec-azure-resource-manager`                                                                                  |
| Public TypeSpec rule | `no-nested-system-data`                                                                                                         |
| Guideline            | System data belongs in the resource envelope, not in or below its properties bag.                                               |
| Applicability        | Models with a JSON property named `properties` in an explicitly ARM-selected program; no resource-marker prerequisite.          |
| Predicate            | Find JSON properties named exactly `systemData` or `SystemData` in the bag's type graph.                                        |
| Traversal            | Inherited model properties, nested models, array/dictionary indexer values, and union variants; visited types terminate cycles. |
| Diagnostic unit      | Each distinct original authored offending property once, including reuse or spreads into several bags.                          |
| Severity/default     | Warning; disabled in ARM `all` and the general `resource-manager` ruleset.                                                      |
| Exemptions           | Envelope-level system data, non-bag models, substrings and other casing. Uninstantiated templates are skipped.                  |
| Suppression          | Fully qualified rule ID on the original offending property declaration.                                                         |

This is an ARM resource-shape policy, not an SDK-name policy. Azure Core must not acquire an ARM dependency, and TCGC metadata is not needed.

### Existing coverage and separate-rule decision

At canonical base `2160a1a6b0e7827aff13f01a2fd296e534945411`:

- `no-reserved-resource-property` checks only `billingData`, case-insensitively and only in direct registered resource bags. It is already generally enabled. Adding recursive system-data checks to that released rule would silently change default diagnostics and the established scope.
- `arm-resource-invalid-envelope-property` validates the envelope, not nested bag contents. Standard envelope `systemData` is valid.

The separate rule preserves both released contracts and supplies opt-in recursion without introducing output-schema parsing into production.

## Original Swagger linter

- [Guideline](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/docs/system-data-in-properties-bag.md)
- [Registration](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/packages/rulesets/src/spectral/az-arm.ts)
- [Function](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/packages/rulesets/src/spectral/functions/system-data-in-properties-bag.ts)
- [Helpers](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/packages/rulesets/src/spectral/functions/utils.ts)
- [Six upstream tests](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/packages/rulesets/src/spectral/test/system-data-in-properties-bag.test.ts)

The frozen installed producer uses `@microsoft.azure/openapi-validator-rulesets` 2.2.6 and `@microsoft.azure/openapi-validator` 2.2.4. The newer source revision above is explanatory provenance, not a substitute for the frozen producer's installed identity and saved execution receipts.

### Selection and every material check

1. Production ARM Spectral registration, severity error, resolved OAS2; neither staging-only nor RPaaS-specific.
2. Select definition property bags with `$.definitions.*.properties[?(@property === 'properties')]^`. No `x-ms-azure-resource` prerequisite is imposed.
3. Collect the selected schema's properties through `getProperties`, merging `allOf` and direct properties.
4. Search recursively for the exact key `systemData`; only if absent, search for `SystemData`.
5. Return at most one finding per selected definition. The diagnostic path appends `properties` and the first segment of the found path, not necessarily the actual offending property.

No named model identity, common-type identity, property type, read-only constraint, or required-property condition is part of this predicate.

### Observed upstream limitations not copied into production

`deepFindObjectKeyPath` returns an empty array when a child has no match. Its caller tests the returned array for truthiness, so the first child's empty result still ends the traversal. A later sibling can be missed. The recursive search also scans arbitrary schema-object keys, including metadata, rather than only payload property declarations.

The TypeSpec linter follows the guideline with a complete semantic graph traversal and actionable property targets. It deliberately does not preserve the first-child miss, arbitrary metadata-key matches, camel-case-first single-result selection, or emitted-definition multiplicity. Therefore identical implementation predicates and raw diagnostic counts are not assumed, even if a corpus has zero findings.

The authored rule documentation explains native authoring independently; historical mechanics remain in its dedicated `LintDiff Equivalent` section and this appendix.

## Saved producer execution proof

The baseline `swagger-arm-20261026-2cd3c5dd` contains 487 successfully compiled and validated projects and 649 Swagger files. Read-only inspection of **every one of the 649 saved raw JSONL logs** establishes:

- production execution was selected;
- the ARM Spectral ruleset was selected;
- `SystemDataInPropertiesBag` was registered with severity `Error` in both manual and TypeSpec-generated configurations;
- Spectral execution returned normally;
- there are zero target diagnostics, corroborating the absent aggregate-index entry.

No Swagger was generated and no Swagger linter was rerun for this migration. The audit helper records each raw file's hash and the complete execution-proof population. The saved CLI settings select ARM type and subtype, not RPaaS; README suppressions were not applied.

The frozen lock records rulesets 2.2.6 integrity `sha512-WUManjLzzEJpcCrhvJc4YyFANIzBHLY6N1YwVQFXFMcWW88WfDWMpSNWR6AqUXl1C/cq/wgOe/N4qGb9wfY3pw==`. Installed registration/function/helper hashes are retained separately. This establishes frozen execution, not equivalence to the current candidate.

## Fixture and acceptance-claim mapping

| Original lintdiff fixture                                     | Native vitest case                                                                              | Coverage note                                                                                                                                                                                                                                           |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SystemDataInPropertiesBag/systemdata-in-properties/main.tsp` | `it("checks standard ARM resource property bags", ...)`                                         | Authorable `TrackedResource` with custom nested system data produces the new property warning directly. The historical fixture's unresolved common-types reference and empty Swagger diagnostics were not treated as compliance or copied as snapshots. |
| N/A (native compliant control)                                | `it("accepts standard ARM envelope system data", ...)`                                          | Standard template's envelope remains valid; correction stays in the same ARM resource audience.                                                                                                                                                         |
| N/A (upstream missed-sibling regression)                      | `it("finds violations after a compliant sibling and targets every offending declaration", ...)` | Two distinct offending nested declarations after a compliant first branch; exact authored spans.                                                                                                                                                        |
| N/A (native recursion)                                        | `it("traverses inherited bags and inherited nested properties", ...)`                           | Custom inherited lookup and shared-root deduplication, not merely framework inheritance.                                                                                                                                                                |
| N/A (native containers)                                       | `it("traverses arrays, dictionary values and union variants", ...)`                             | Three independent graph branches; null/scalar variants do not manufacture findings.                                                                                                                                                                     |
| N/A (native graph termination)                                | `it("terminates cycles and reports shared offending properties only once", ...)`                | Cycles, shared siblings and two root bags; exact single offending target.                                                                                                                                                                               |
| N/A (wire names)                                              | `it("uses JSON encoded names for both bags and nested properties", ...)`                        | Encoded violation and separately renamed compliant envelope; compiler-forbidden name swaps were removed, not suppressed.                                                                                                                                |
| N/A (authored target deduplication)                           | `it("does not multiply findings when a declaration is spread into several bags", ...)`          | Two spreads of one source declaration yield one actionable warning.                                                                                                                                                                                     |

The same canonical behavior suite also checks both exact casing branches and compliant envelope/substring/other-casing controls. There is one rule suite, plus the existing package/rulesets registration suites; no per-rule Markdown parser, emitter fixture suite, or import-inspection test was added.

### Documentation and actual-package controls

The published incorrect/correct snippets use `TrackedResource`, `ResourceNameParameter`, and `ArmResourceRead`. They differ only by removing nested custom `systemData`; the standard envelope remains present. The one-time control helper requires each full literal snippet to be present in the authored document, then compiles those exact snippets against the injected packages with the target explicitly enabled. This is not continuous documentation testing.

The helper additionally checks compliant nearby names, recursive array/dictionary/union traversal, authored suppression, and default inactivity through ARM `all` and the general resource-manager ruleset. All seven actual injected controls passed: published incorrect 1/correct 0, suppression 0, complete graph 3, compliant nearby names 0, and both rulesets default 0/explicit 1. Both documentation snippets compiled without unrelated errors. The full literal document hash and loaded package/entrypoint hashes are retained in the controls receipt.

## Validation and recovery history

Passing local gates to date:

- Eleven focused behavior tests; initial empty-scaffold TDD failure is retained.
- ARM package build, library lint and oxlint.
- Bound documentation generation, actual generated page inspection, manual ARM matrix update, scoped source/docs formatting and explicit empty-ignore generated-doc checking.
- Rulesets build and nine tests.
- Separate LF Chronus feature/internal descriptions and `chronus status`.

The initial full ARM suite had 718 passing tests and one failing existing exhaustive `all` registration assertion. Coordinator reserve attempt 1 authorized the exact missing opt-in exception and test-title correction, with no production/default changes. The next original-scope run passed that assertion but had 717 passing tests and two per-test 10,000 ms timeouts in unrelated existing tests. The coordinator granted the single task-wide reduced-concurrency diagnostic, preserving the original 719-test/83-file population, zero skips, pool, assertions, dependencies, and timeouts. That diagnostic passed all 719 tests in 83 files, with zero skips, in 429.68 seconds. This is a recovered timeout with unproven cause, not proof of contention.

A separate clean immutable candidate at `9dcf4cb3cf1be3d8b050bfb65c404573fe2981a3` (tree `e710df8841fd1312953da137588f172449473c84`) contains the exact unpublished source. Both changed-package builds pass. The original pack invocation failed because Chronus 1.5.1 uses non-greedy array arguments. Coordinator reserve 2 authorized only repeating `--only` for the second selector. That correction passed: 20 unique package archives, the 18 existing archive hashes unchanged, and packaged rule/linter/ruleset bytes matching the clean snapshot build outputs. Fifteen unchanged archives retain candidate-base build provenance, two are newly snapshot-built, and three are explicitly external frozen-lock pins, not candidate-built outputs.

Final artifact injection passed using the supported patch/install stages and specs pnpm 12.6.0. Original specs lockfile/workspace bytes were restored and source stayed clean. The first full-coverage launch failed before importing the analyzer: `tsx` is installed in the lintdiff package, not the repository root used by that invocation. A read-only resolution probe from the skill-prescribed package directory succeeded. That failed invocation created no coverage output, worker, second injection or Swagger execution.

The coordinator granted final reserve 3 for only that cwd correction. The actual analyzer started from the package directory with unchanged flags and completed its normal exact-artifact injection. The single full comparison completed naturally with exit 0 and final manifest `complete`, including final input/dataset integrity. All 487 projects are assessable with successful native receipts, zero unassessed projects, zero ambient compiler errors, and zero default target findings. Raw Swagger/TypeSpec findings are 0/2, with two distinct authored source locations. Both differing projects are fully investigated in [the grouped appendix](differences.md). The dependency-free recount matched every aggregate and every project row against the original analyzer report.

The command ran from `2026-10-29T14:10:20.967Z` to `2026-10-29T15:36:17.566Z`, 85.94 minutes including baseline preparation and final integrity. Its native-phase deadline stayed 3,600 seconds at concurrency 2, source scope, configured mode, all 487 projects, no filter or limit. The earlier failed bootstrap receipt is retained separately. The [sanitized final manifest](runs/cycle0/manifest.json), [complete observations](runs/cycle0/observations.json), [original numerical report](runs/cycle0/coverage.json), and [independent summary](runs/cycle0/summary.json) preserve the successful population and actual directional counts without asserting strict functional equivalence.

Initial evidence formatting stopped before formatting because the untouched evidence checkout's relative core formatter plugin was not built there. A separate lint invocation stopped before source analysis because that checkout's configuration could not resolve its `oxlint` dependency. Both original failures remain retained. The coordinator's read-only reconciliation established genuinely missing first-time prerequisites, not a task draft defect or corrective retry.

The evidence role's exact `cefb035e7721a6fdcb6de605b5f469b93055a880` core gitlink was initialized. Its initial root/core-root/`@typespec/prettier-plugin-typespec...` filtered frozen offline ignore-scripts installation selected six workspace projects and reused 486 cached packages, with zero downloads. Only the missing four-package formatter build closure ran: internal-build-utils, tmlanguage-generator, compiler, and prettier-plugin-typespec. Original configurations, manifests, lockfile, core gitlink, and all 18 existing evidence files were verified unchanged by setup. No alternate-config route, unrelated package build, artifact build, corpus rerun, or correction-budget debit occurred.

An additional optional direct-import smoke probe rejected a raw Windows drive path as an ESM URL before loading the module. That probe was not corrected or retried and is not reported as passing. The original scoped formatter/linter, rather than a substituted configuration or standalone probe, supply the required evidence-tool runtime validation.

The first staged evidence whitespace check rejected a task-owned nine-byte CRLF `.gitattributes` whose `* -text` setting preserved the carriage return. No commit or push occurred on that failure. A separately authorized single supplemental local correction normalized only that file to eight LF bytes and refreshed its dependent size/checksum metadata. Original whitespace, format, lint, and recount checks then passed. This did not consume or reset the PR-creation-only publication allowance.

Failed commands and raw receipts remain retained; none are relabeled as passing. Ordinary development draft corrections remain 3/3, reserve 3/3, timeout diagnosis 1/1 debited, baseline comparison 0/1, and the separate supplemental LF correction 1/1. Neither a new phase nor a resumed worker resets counters.

## Reproducibility and remaining gates

The shared baseline is pinned through metadata commit `317e703b3e380d3b64e0dacb3a2c6fc0651de253`, descriptor SHA-256 `ac511e7ff4b519619f30af811107b7f770a92a5bb56b199dfca983262dc8fd31`, baseline identity `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`, and specs source `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`.

The specs source preservation tuple is `msyyc/azure-rest-api-specs`, ref `evidence/long-running-operations-options-validator-20261022-source`, at that exact source commit. The frozen shared archive remains on that repository's `swagger-lint-baseline-20261026-2cd3c5dd` release; it is not replaced per rule.

Initial evidence commit `b45d7c3a54f05bda2f7552e4ca4501d5316d8322` was pushed to the stable evidence branch and its exact remote head verified. A new recursive GitHub clone independently verified all 20 initial published files, downloaded both immutable assets, reconstructed the exact candidate/core and 20 package identities, and recovered the frozen specs source's complete 363,518-file Git object closure with connectivity and critical witness checks. The archived supported baseline helper then completed naturally with exit 0, verifying the complete 93,496-file sealed inventory, 487 successful projects, 649 Swagger files, and 222,905 saved observations in 121 rule shards. A fresh dependency-free recount matched every project row and aggregate. [Recovery receipt and explicit claim boundaries](fresh-recovery.json) and [tested recovery operations](recovery.md) retain these results.

This is input recovery and saved-observation reanalysis without unpublished development inputs, not an installed fresh specs runtime, full transitive dependency lock, second native corpus, or Swagger execution. Remaining gates are independent local precommit review, one canonical native draft PR, external integration, and independent A/B local/GitHub review checkpoints. The native source remains uncommitted and unpublished pending the outer-owned retained local review and supplied approval.
