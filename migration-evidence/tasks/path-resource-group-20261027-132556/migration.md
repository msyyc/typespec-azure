# ARM scope-path standard name migration

## 1. Conclusion and scope

The TypeSpec rule `@azure-tools/typespec-azure-resource-manager/use-scope-path-standard-name` combines Swagger linter
[`PathContainsResourceGroup`](https://github.com/Azure/azure-openapi-validator/blob/18a7944e7fc3155e8ef1498665465ed5f455f54a/docs/path-contains-resource-group.md) and
[`PathContainsSubscriptionId`](https://github.com/Azure/azure-openapi-validator/blob/18a7944e7fc3155e8ef1498665465ed5f455f54a/docs/path-contains-subscription-id.md).
**The admitted ARM scope-path naming checks are functionally equivalent for the
assessed policy**, with different severity and diagnostic units. Subscription
behavior is established by discriminating controls; the frozen historical corpus
contains no subscription findings. This is not a claim of unchanged emission.
Native source, immutable inputs and fresh-checkout recovery are verified. Independent local development and local readiness reviews are clean; both distinct Balanced GitHub checkpoints are clean on the unchanged native commit.

## 2. Actual coverage

All **487 production ARM projects** were assessed by fresh TypeSpec compilation,
with **no failures or unassessed projects**. Reported diagnostics are individual
findings, not project counts.

| Count | Swagger linter | TypeSpec linter |
| --- | ---: | ---: |
| Reported diagnostics | 43 | 31 |
| After analysis: affected HTTP operation/member checks | 31 | 31 |

The after-analysis row uses independently checked member policy + exact project +
case-preserved full path + HTTP method, not renamed raw counts. It preserves two
independently actionable naming failures at one operation.

## 3. Function-level coverage

| Behavior | Result |
| --- | --- |
| Resource-group naming | Missing, wrong, and literal values detected; canonical or absent segment accepted |
| Subscription naming | Independently detected; canonical or absent segment accepted, including supported template customizations |
| Both naming failures | Two distinguishable warnings on the same authored operation under one public ID |
| Full-path and serialized names | Case-insensitive canonical-occurrence exception preserved; serialized `@path` overrides checked in both directions |
| Applicability | Concrete ARM provider GET/PUT/PATCH/DELETE operations; POST/HEAD, non-ARM services and generic declarations excluded |
| Registered activation | ARM `all` enabled; Azure resource-manager ruleset disabled; one suppression covers both checks |

## 4. Why diagnostic counts differ

Only two projects differ; there are no one-sided projects.

- **[DataMigration](runs/combined-native-20261029-cycle0/evidence-details.md#datamigration-method-multiplicity):**
  11 Swagger linter path findings cover 26 eligible operations, each reported by
  the TypeSpec linter.
- **[Network](runs/combined-native-20261029-cycle0/evidence-details.md#network-reference-multiplicity):**
  30 Swagger linter observations repeat two owning paths through verified
  reference chains; those paths contain the three reported TypeSpec operations.

Every differing path/method group is accounted for in the linked appendix.

## NOTES

- **Historical comparison:** shared baseline `swagger-arm-20261026-2cd3c5dd`,
  source `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`, frozen-reference policy,
  source-program scope, no filter or limit. Backward compatibility is an explicit
  assumption, not byte-identical Swagger or dependency equivalence. A separate
  selected-version HTTP metadata audit verifies every affected operation; it is
  not a projected lint rerun. No Swagger was generated or revalidated.
- **Counting:** raw Swagger-higher excess **27**, TypeSpec-higher excess **15**,
  total absolute discrepancy **42**; 485 projects have equal raw counts.
  Comparable operation/member checks agree in all 487 projects. TypeSpec raw
  per-member attribution remains **unassessed**; no member percentage is inferred
  from diagnostic messages. Metadata-based semantic controls distinguish members.
- **Validation:** 38 focused rule cases, 682 full ARM tests, nine ruleset tests,
  nine actual injected controls, four normalization controls, four actual final
  documentation snippets, builds, package/root lint, explicit generated-doc
  formatting, and Chronus status passed. Earlier expected TDD failures,
  missing-prerequisite lint failure and Chronus parser failure are preserved.
- **Activation:** Swagger errors become TypeSpec warnings. ARM `all` activation
  is preserved; Azure resource-manager ruleset activation remains disabled.
  Opting into this one public ID controls both checks.
- **Members:** [resource group](members/PathContainsResourceGroup/migration.md)
  and [subscription](members/PathContainsSubscriptionId/migration.md) retain
  independent semantic evidence and the zero-observation limitation.

  | Member | Swagger raw | Material semantics | TypeSpec member raw |
  | --- | ---: | --- | --- |
  | PathContainsResourceGroup | 43 | Covered by corpus and discriminating controls | Unassessed |
  | PathContainsSubscriptionId | 0 | Covered by discriminating controls; no corpus-positive example | Unassessed |

- **Evidence/recovery:** [current appendix](runs/combined-native-20261029-cycle0/evidence-details.md),
  [automatic report](runs/combined-native-20261029-cycle0/coverage.md),
  [claim map](runs/combined-native-20261029-cycle0/claim-map.json), and
  [published assets](runs/combined-native-20261029-cycle0/receipts/assets-publication.json).
  Native commit `991c7ec6bd093ab253ab4a4af27e3425525c99d2` has [verified source equality](runs/combined-native-20261029-cycle0/receipts/native-committed-source-equality.json); immutable asset downloads and [independent local development review](runs/combined-native-20261029-cycle0/receipts/local-development-review.json) passed. [Fresh-checkout recovery](runs/combined-native-20261029-cycle0/receipts/fresh-checkout-recovery.json) passed, including sealed baseline, exact package files, source commits and saved-data replay. Both [applicable review checkpoints and local readiness](https://github.com/msyyc/typespec-azure/blob/evidence/path-contains-resource-group-20261027/migration-evidence/tasks/path-resource-group-20261027-132556/runs/combined-native-20261029-cycle0/reviews/final-review-summary.json) are **clean**, with retained raw API collections and pre/post-sanitization hashes.
  The [earlier resource-group-only report](migration-resource-group-only-before-combination-20261029.md),
  runs and their review/recovery receipts remain
  historical evidence, not reviews of this combined candidate.

- **Final reviews:** A request `34556224237` / review `5693922620`; B request `34557402613` / review `5694070332`, each Balanced and 1/5 rounds. Both actual states are `COMMENTED` with Approval recommended, zero REST comments and zero unresolved Copilot threads. Local readiness is separate from local development. Reviews apply to native `991c7ec6bd093ab253ab4a4af27e3425525c99d2` and reviewed evidence `eefbb2b927c0c502245352abf32a377d35c690c8`; this final evidence append changes review/status metadata only. Ordinary draft corrections **3/3**, coordinator reserve **3/3 exhausted**, semantic repairs **0/3**; all other counters preserved in the linked receipt. The human combination-request thread remains open with the existing friendly reply. Final evidence identity/readback is recorded externally after publication, not claimed circularly here.

- **Final evidence authoring:** two existing release-readiness draft corrections (2/3) restored original UTF-8 appendix labels, made newly added review links location-independent, and enforced explicit LF for final JSON metadata; no production, diagnostics, package, baseline or native-document content changed. Publication-configuration correction remains 0/1. The original ad-hoc run/task report comparison mismatch is separately retained, not counted as a failed required renderer gate.
