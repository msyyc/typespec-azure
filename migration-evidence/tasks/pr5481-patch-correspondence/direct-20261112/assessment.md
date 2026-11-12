# Direct-constraint policy and assessed diagnostic effect

## Policy and complexity

The approved trade-off is a small direct-constraint check, not a general
PATCH-value subset solver. The compatibility helper is **132 lines instead
of 374**. It uses existing compiler metadata getters for format, string length,
item count and numeric bounds, including inherited constraints, inclusive and
exclusive integer bounds, tighter PATCH limits and nullable/reset values.

The rule still owns request visibility, operation pairing, encoded names,
correct-position opaque containers, missing properties and absent/empty bodies.
The comparator does **not** solve general scalar-type assignability, enum value
sets, encodings, array element types or dictionary contents. These are explicit
scope limits, not claims that all accepted values are compatible.

Compiler assignability is not a replacement: it does not enforce an omitted
property constraint and can reject legitimate partial PATCH objects or
separately declared wire-compatible enums. Reintroducing those concerns would
recreate the solver this change deliberately removes.

## Actual diagnostic effect

The final candidate is
[`f2079b23690d816ecc92a858fab2c1572e9448b5`](https://github.com/Azure/typespec-azure/commit/f2079b23690d816ecc92a858fab2c1572e9448b5).
A clean CLI run assessed **all 487 frozen ARM projects**, with **104 warnings
and no failed/unassessed projects**. The unchanged Swagger staging observations
contain **1,314 diagnostics**. No Swagger was regenerated.

The current warnings are **83 missing-name**, **19 direct-constraint**,
**1 empty-body** and **1 missing-body** findings.
All **19 straightforward findings** from the preceding checker remain:

| Direct check           | Warnings | Projects                                 |
| ---------------------- | -------: | ---------------------------------------- |
| String length          |        6 | API Management, Automation, NetworkCloud |
| Minimum item count     |       10 | ManagedNetworkFabric                     |
| Numeric bounds         |        1 | RegistryTasks                            |
| ARM resource-ID format |        2 | AppService                               |

The [raw complete-record delta](../refresh-20261112-direct/candidate-delta.json)
contains **23 removals and 19 additions** because the diagnostic wording
changed. This is not 23 lost behaviors and 19 new defects. The
[explicit wording-normalized comparison](reconciliation.json) changes only the
old compatibility-message suffix; every other diagnostic field and duplicate
occurrence is preserved. Its behavioral delta is **4 removed, 0 added**.

## Deliberately omitted deep checks

These are observed findings, not hypothetical gaps. They require collection or
nested-value comparisons beyond the approved direct-constraint policy:

| Project                 | Source target                  | Location                             |
| ----------------------- | ------------------------------ | ------------------------------------ |
| MachineLearningServices | `userAssignedIdentities`       | `models.tsp:5735:3`                  |
| ManagedNetworkFabric    | `matchConfigurations`          | `models/AccessControlList.tsp:255:3` |
| ManagedNetworkFabric    | `controlPlaneAclConfiguration` | `models/AccessControlList.tsp:265:3` |
| ManagedNetworkFabric    | `matchConfigurations`          | `models/NetworkTapRule.tsp:218:3`    |

The exact records, including project paths and full messages, are in
[the reconciliation](reconciliation.json).
They correspond to **six retained Swagger records**: MachineLearningServices
indices **7, 13, 18**, and ManagedNetworkFabric indices **2, 4, 82**.
Several emitted records can witness one source warning; do not collapse
different checks merely because they share a source location.

**Decision: accept the narrower policy**, preserving the 19 direct findings
without the recursive solver. Those six records are **not migrated**, not
proven compatible, not confirmed Swagger false positives, and not deferred to
#5875. Restoring them would be a separate policy expansion with its own
complexity/noise justification. The migration is therefore explicitly partial.

## Record-to-warning bridge

The immutable Swagger assessment excludes **1,132 confirmed overchecks**.
The other **182 records** are all assessed:

| Disposition                                    | Retained records | Meaning                                                       |
| ---------------------------------------------- | ---------------: | ------------------------------------------------------------- |
| Reporting checks                               |               83 | Precise configured warning witnesses                          |
| Authored suppression                           |                1 | Implemented absent-body check, intentionally suppressed       |
| Compatible inputs or non-input leaves/wrappers |               92 | No additional current-source warning required                 |
| Outside the approved direct-constraint policy  |                6 | Four omitted deep targets, not compatibility acceptance       |
| Total                                          |              182 | 84 check-covered; 92 require no extra warning; 6 not migrated |

The reporting records make **85 associations to 73 distinct warnings**:
**12** associations reuse a warning across records, while **2** are additional
checks within one record. Another **31 configured warnings** have no
established retained-record counterpart:

| Outside-join group                          | Warnings | Decision                                                             |
| ------------------------------------------- | -------: | -------------------------------------------------------------------- |
| Historical names/availability               |       13 | Defer shared versioning work to #5875                                |
| Writable PATCH inputs absent from PUT input |       17 | Keep the check; request model/API-owner corrections where unintended |
| Empty PATCH body                            |        1 | Keep the check; Swagger's existing-parameter test misses it          |

Thus **182 - 104 = 92 + 6 + 1 + 12 - 2 - 31 = 78**.
This closes the arithmetic, not historical API-version equivalence.
The [deterministic checker](reconcile.py) verifies every occurrence, all
**51 exact ordered capture arrays**, all six changed record dispositions,
the four omitted targets and the 19 retained direct findings.
The [per-project bridge](reconciliation.json) preserves both difference
directions instead of treating opposite gaps as cancellation.
Retained-record excesses are **95 Swagger-higher / 17 TypeSpec-higher**,
absolute **112**, net **78**. Raw full-population excesses are
**1,212 Swagger-higher / 2 TypeSpec-higher**, absolute **1,214**; the
[complete comparison](../refresh-20261112-direct/staging-comparison/summary.json)
retains all per-project differences.

## Validation and provenance

- **Production:** 91 canonical PATCH tests pass, including the updated policy
  boundaries. The null-only reset regression also passed its focused run.
  ARM dependency build, root formatting, syntax/type-aware linting, Chronus and
  PR-owned whitespace checks passed.
- **Conflict:** both the intentional bodyless-PATCH suppression and
  `@armResourceUpdate` annotation are retained. The resolved legacy
  private-endpoints sample compiles successfully.
- **CI:** all six exact-head Build jobs passed on Ubuntu/Windows with
  Node 22/24/26. The source branch is mergeable. The external Azure REST API
  Specs failure remains outside the user-requested repair scope.
- **Packaged controls:** 17 semantic/activation/suppression controls,
  37 applicable portable harness controls, and 12 extraction controls passed.
  Six fixtures requiring the unrelated unmerged resource-group rule were
  explicitly excluded, not counted as passes.
- **Authored examples:** both actual published Incorrect/Correct ARM template
  snippets were extracted with the existing website Markdown AST and executed
  unchanged. The receipts show one expected warning and no warnings,
  respectively, with no ambient errors. See
  [documentation receipts](../refresh-20261112-direct/controls/documentation-examples.json).
- **Fresh population:** the CLI completed cleanly from
  **2026-11-12 03:35:24 to 04:14:33 UTC**, within its recorded budget. This is
  separate from the previous observation's finalization recovery.
- **Closure:** current main was merged to resolve an actual conflict. This
  also upgraded the compiler/library closure; fresh results were not relabeled
  from the old run. The current compiler is **1.18.0**, core commit
  `e06f6b34fdad9d7f49bfc084a598b03c60684e9a`; actual generator/replay tooling is
  `4dda34822b8877d997b6b5ab6525b70e8379ba0d`. Runtime is Node **26.13.0** and
  the frozen specs' package manager is pnpm **12.6.0**.

[Current metadata](../refresh-20261112-direct/task.json),
[build/package/runtime provenance](../refresh-20261112-direct/provenance/artifact-provenance.json)
and [replay instructions](../replay.md) retain the exact identities and
verification paths. The original prepared plan is preserved: its inherited
`toolingRevisionVerification` and historical estimates are not new execution
proof, and its bare-shell pnpm version is not the integration package-manager
version. Use the actual manifest and integration log for current runtime facts.

Historical body-shape investigations and separately enabled existing-rule
probes remain in the
[dated appendix](../gap-investigation.md). The responsible
`@azure-tools/typespec-azure-resource-manager/use-model-request-body` source is
unchanged from that assessed candidate; its separately scoped findings are
not included in the target-only total of 104. Synthetic unobserved gaps are
not added to the main diagnostic-driven gap table.
