# Current semantic and validation evidence

This document describes the consolidated `no-reserved-resource-property` outcome. The prior recursive rule's detailed contract and acceptance history remain available at [immutable evidence commit `810d5c9`](https://github.com/msyyc/typespec-azure/blob/810d5c9565db742ce370544dea42633c5fa7c687/migration-evidence/tasks/system-data-in-properties-bag/evidence-details.md); they are not current coverage claims.

## Mapping and accepted native policy

| Field                | Current decision                                                                                                |
| -------------------- | --------------------------------------------------------------------------------------------------------------- |
| Swagger member       | `SystemDataInPropertiesBag`, production ARM, resolved OAS2                                                      |
| Official destination | `@azure-tools/typespec-azure-resource-manager/no-reserved-resource-property`                                    |
| Relationship         | Partial guideline coverage through an existing rule, not full functional equivalence                            |
| Applicability        | Immediate/inherited members of recognized ARM resource properties models                                        |
| Predicate            | Existing case-insensitive authored TypeSpec names; add reserved `systemData`, preserve `billingData`            |
| Diagnostic           | Existing warning ID, message format and authored property target; no added global deduplication                 |
| Activation           | Existing ARM `all` and recommended `resource-manager` enablement retained                                       |
| Out of scope         | Recursive descendants, arbitrary non-resource bags, JSON alias resolution and serialization-specific exemptions |

The user's accepted revision replaces the proposed standalone rule and recursive policy. The source change is one reserved-map entry and its description, plus removal of the rejected rule's source/tests/registration. Existing billing behavior remains untouched. ARM guidance permits each resource's own envelope metadata; the real AzureDataTransfer embedded envelope is not established to be a violation merely because it is nested.

## Upstream comparison

The pinned [registration](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/packages/rulesets/src/spectral/az-arm.ts) selects definition properties bags without a recognized-resource prerequisite. Its [function](https://github.com/Azure/azure-openapi-validator/blob/e1b8b207a196cf2fc288593efec22e6e38ab98d5/packages/rulesets/src/spectral/functions/system-data-in-properties-bag.ts) searches recursively for exact `systemData`, then `SystemData`, reporting at most one path per selected definition. The helper also scans schema metadata and can stop on the first nonmatching child because an empty array is truthy.

The frozen installed producer is rulesets 2.2.6 / validator 2.2.4. The newer explanatory source revision does not replace that producer identity. The unchanged [649-file producer audit](producer-audit.json) establishes production ARM selection, enabled error registration, completed Spectral execution and zero target findings in every retained raw log. No Swagger emission or linter execution was repeated.

## Canonical regression mapping

All rule behavior lives in the existing public rule's `test/rules/no-reserved-resource-property.test.ts`; no parallel migration suite or private authoring API was introduced.

| Behavior / corpus link                                             | Canonical test or executed control                                                                                |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| Direct bag metadata, including retained DataBoxEdge target         | `rejects the immediate resource property %s`, parameterized for three casings; actual published incorrect snippet |
| Inherited metadata                                                 | `checks inherited system data in the resource properties model`; actual-package inherited control                 |
| Valid envelope and retired AzureDataTransfer array-element warning | `accepts envelope metadata, embedded resource envelopes and nearby names`; actual-package nested/embedded control |
| Existing billing policy                                            | All existing billing tests retained; published incorrect/correct snippets give two/zero total warnings            |
| Authored names versus JSON aliases                                 | Actual-package alias control; no new emitted-name semantics promised                                              |
| Existing rule activation and suppression                           | Actual-package ARM `all`, recommended preset and property-level suppression controls                              |

The new violating cases failed before the `systemData` map entry was added. The direct/embedded contrast distinguishes the accepted policy from the rejected recursive architecture.

## Executed local checks

- ARM focused rule/linter suites: 20 passed. Central ruleset validation suite: 14 passed.
- ARM and central rulesets builds passed. The required compiler, Azure and emitter package closure builds passed.
- Full `pnpm lint`, `pnpm format:check`, Chronus status and whitespace checks passed. The first lint attempt raced generated Azure Core extern files during a parallel build; retry after generation completed passed without source repair.
- Eight selected-rule actual-package controls passed, including literal verification and compilation of the actual published documentation snippets with a standard ARM wrapper. This is one-time evidence, not continuous documentation coverage or a bespoke Markdown parser.
- Thirty-seven applicable portable injected-package controls passed. Six resource-group-path-parameter migration cases were explicitly excluded before execution because their unrelated unmerged target is absent; they are not counted as passes. The exact selector is documented in [recovery.md](recovery.md).
- One full 487-project corpus run passed under exclusive shared ownership. Complete baseline/source/artifact integrity and natural completion were accepted; all observations and an independent per-project recount are published under `runs/fix5892-20261106`.

The 17 candidate/core-built archives' 3,023 `lib`/`dist` files were compared byte-for-byte with the selected built trees. Three external frozen registry archives retained their original hashes. Current core and runtime differ from the historical recursive run; frozen-reference compatibility is assumed and actual failures investigated, not treated as identical emission.

The [input recovery](fresh-recovery.json) independently downloaded the new public archive and reconstructed all source changes/deletions and all 20 packages from remote source plus the downloaded overlay. It did not borrow unpublished source, rerun the native corpus a second time or prove a fully portable transitive dependency lock.

## Current versus historical gates

Current gates are recorded in [final-gates.json](final-gates.json). Historical independent reviews, A/B checkpoints and CI results belong to their exact historical commits and are not relabeled as reviews of this fix. The fix workflow requires local validation and a single final-head CI observation, not waiting for CI. Thread flags are left unchanged; addressing feedback is not reviewer approval or merge readiness.
