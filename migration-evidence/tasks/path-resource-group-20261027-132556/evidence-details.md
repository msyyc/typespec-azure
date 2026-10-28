# Evidence details

## Frozen inputs

| Input                   | Identity                                                                                                                                                                                               |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Mapping                 | `PathContainsResourceGroup` to `@azure-tools/typespec-azure-resource-manager/resource-group-path-parameter`                                                                                            |
| Task / flow             | `path-resource-group-20261027-132556` / `native-first`                                                                                                                                                 |
| Candidate base          | `Azure/typespec-azure@0f0bd39898526be39e145beb770f771aaaa84653`                                                                                                                                        |
| Tested source           | Twelve changed files in the [run manifest](runs/full-native-01/manifest.json); exact bytes retained as standalone assets                                                                               |
| Candidate core          | `fbb44a7037e1eda84fd108a96aaaffc8a7dc045a`                                                                                                                                                             |
| Specs                   | `Azure/azure-rest-api-specs@2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`                                                                                                                                  |
| Preserved specs         | `msyyc/azure-rest-api-specs:evidence/long-running-operations-options-validator-20261022-source` at the same exact specs SHA; reused read-only                                                          |
| Swagger producer / core | `726862b537be9fdb24d7e6a4ca868eb9104025dd` / `88e5bd18b07d0cbd3bbe92946aff36beaf707b54`                                                                                                                |
| Baseline identity       | `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`                                                                                                                                     |
| Baseline asset          | [swagger-arm-20261026-2cd3c5dd.tar.gz](https://github.com/msyyc/azure-rest-api-specs/releases/download/swagger-lint-baseline-20261026-2cd3c5dd/swagger-arm-20261026-2cd3c5dd.tar.gz), 51,932,501 bytes |
| Baseline asset SHA-256  | `0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0`                                                                                                                                     |
| Tooling base            | `Azure/typespec-azure@729b948037d6c2d71284c929ec2f2d96d2a7793f` plus the six exact source assets                                                                                                       |
| Runtime                 | Node 26.5.0; candidate pnpm 11.10.0; specs pnpm 12.6.0                                                                                                                                                 |
| Actual key packages     | Compiler 1.17.0; ARM 0.73.0; AutoRest emitter 0.73.2; validator 2.2.4; validator core 1.0.7; validator rulesets 2.2.6                                                                                  |

The [publication manifest](publication-inputs.json) records individual package and
source asset hashes, restore paths, the final native commit, and verified upload
status. [Installed-artifact auditing](receipts/step6-installed-artifact-audit.json)
compared 2,907 installed files across 18 reachable packages against candidate
tarballs. Three packed packages were outside the installed runtime closure:
`tmlanguage-generator`, `@typespec/json-schema`, and `@typespec/tspd`. They receive
no runtime-loading credit.

This run uses explicit `frozen-reference` comparison, not strict unchanged-runtime
baseline reuse. The candidate compiler/library/emitter differ from the producer.
Compatibility is a working assumption supported here by successful compilation
and targeted path evidence, not proof of byte-identical Swagger. No Swagger was
regenerated. The source population, inventory, retained files, and hashes were
verified; 487 projects, 649 Swagger files, and 222,905 baseline observations were
retained, with no producer failures. The new native run selected no filter/limit.

The source rule is registered for production ARM/OAS2. Its
[selector](https://github.com/Azure/azure-openapi-validator/blob/18a7944e7fc3155e8ef1498665465ed5f455f54a/packages/rulesets/src/spectral/az-arm.ts)
is `$[paths,'x-ms-paths'].*[get,patch,put,delete]^~`. Its
[predicate](https://github.com/Azure/azure-openapi-validator/blob/18a7944e7fc3155e8ef1498665465ed5f455f54a/packages/rulesets/src/spectral/functions/arm-path-validation.ts)
lowercases the full key and checks for `/resourcegroups/` without
`/resourcegroups/{resourcegroupname}`. This is not a full ARM URI grammar.
Canonical occurrence anywhere satisfies the original condition. There is no
RPaaS-only restriction for this rule. Data-plane policies are not evaluated.

## Comparison method

The generator's [raw report](runs/full-native-01/coverage.md) and
[structured report](runs/full-native-01/coverage.json) describe this fresh native
run against the shared frozen Swagger reference. Unrelated historical coverage
reports are not inputs; historical-report reconciliation is not applicable.

Raw Swagger units are validator observations, with 15 exact file-independent
project/JSON-path identities. Raw native units are 31 authored-operation
diagnostics/source targets. These identities are not interchangeable. The
separate [operation-unit report](receipts/step8-operation-comparison-full.json)
preserves each project's raw counts, signed/absolute/relative gaps, and exact
method-unit comparison.

Normalization is specific to this one rule:

1. Retain all 43 [original observations](receipts/step6-swagger-member-observations.json).
   Verify their complete multiset against the independently grouped audit.
2. Require one exact owning Swagger document for each diagnosed full JSON path.
   Re-read the actual frozen document and verify its selected API version and
   eligible methods.
3. Keep repeated validation inputs and original reported/fallback attribution.
   For derived owners, check every local `$ref` edge in the retained reference
   chain; do not relabel fallback input names as reported source files.
4. Expand the diagnosed path into eligible GET/PUT/PATCH/DELETE method slots.
   Compare exact project/path/method identities, retaining full case/query keys.
5. In an independent instrumented copy of the exact native worker, bind every
   native diagnostic to its HTTP operation object. Audit the selected-version
   HTTP graph separately and require the same operation-unit set.
6. Bind the three project probes back to the full run's diagnostic multisets.
   Check every other successful native receipt contains zero target findings.
   Missing/failed receipts are unassessed, never compliant.

The [auditor](replay/audit-native-operations.mjs) records original and instrumented
worker hashes. It does not modify production sources or rerun the linter on a
projected program. The [comparator](replay/compare-operation-units.mjs) and its
[eight controls](replay/compare-operation-units.test.mjs) reject equal totals with
different operations, a missing method, distinct-project/path collisions,
ambiguous method owners, duplicate native operations, and changed query suffixes.
There is no fuzzy name or property matching.

| Project       | Swagger raw | Native raw | N-S | Absolute | Relative | Method units S/N |
| ------------- | ----------: | ---------: | --: | -------: | -------: | ---------------: |
| Advisor       |           2 |          2 |   0 |        0 |        0 |            2 / 2 |
| DataMigration |          11 |         26 |  15 |       15 |   57.69% |          26 / 26 |
| Network       |          30 |          3 | -27 |       27 |      90% |            3 / 3 |
| Other 484     |           0 |          0 |   0 |        0 |        0 |            0 / 0 |

Relative difference is `abs(N-S)/max(N,S)`, or zero when both are zero. Raw
directional excesses are 27 and 15; absolute total is 42. File-independent
Swagger-path count is 15, not a comparable denominator for 31 native operations.
The report's location-based excess fields are separate conservative summaries.
They must not replace raw counts or this tested operation-unit audit.

### Advisor: direct route

**Classification:** count agreement. **Status:** matching behavior.
**Version:** `2026-08-01-preview`.
[Pinned source](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/routes.tsp#L61-L96).

The actual source uses:

```typespec
@route("/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Advisor/configurations")
```

The GET operation has `@path resourceGroup: string`. The PUT item route uses
the same wrong group parameter. Swagger reports two path findings; native
reports `listByResourceGroup` and `createInResourceGroup`, at source lines 64 and 82. Both selected-version HTTP paths match exactly. No rule change is needed.

### DataMigration: method multiplicity

**Classification:** count-only. **Status:** explained multiplicity, not a missing
check. **Version:** `2025-09-01-preview`.
[Pinned source](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/DataMigrationService.tsp#L53-L130).

The legacy base contains:

```typespec
@path
@segment("resourceGroups")
@key
groupName: string;
```

`DataMigrationServices.get`, `createOrUpdate`, `update`, and `delete` share this
exact emitted path:

```text
/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}
```

| Engine  | Observed result for this item path                      |
| ------- | ------------------------------------------------------- |
| Swagger | One path-level diagnostic covering GET/PUT/PATCH/DELETE |
| Native  | Four operation diagnostics at lines 86, 96, 116, 129    |

Across the project, five item paths each have four eligible methods; six other
paths have one each: `5*4+6=26`. Swagger has 11 diagnosed paths. The selected-version
HTTP audit confirms all 26 native units. No production rule change is needed.

### Network: reference multiplicity

**Classification:** count-only. **Status:** explained reference-linked/repeated
observations; 28 lack reported file attribution and two retain it.
**Version:** `2026-03-01`.
[Pinned source](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/network/resource-manager/Microsoft.Network/Network/Network/SwapResource.tsp#L53-L151).

Both `CloudServiceOps` and `SwapResourceListOps` use
`@path @segment("resourceGroups") groupName: string`. The two exact paths are:

```text
/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}
/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots
```

The retained `swagger/stable/2026-03-01/virtualNetwork.json` is the unique document
containing those exact paths. Every relevant validator input reaches it through
verified local references. Each path has 15 raw observations across nine input
files. Twenty-eight records retain empty `sourceDocuments` and
`sourceAttribution: input-fallback`; two retain reported attribution. Reference-chain
ownership inferred for fallback records is separate evidence, not recovered
reported provenance.

| Engine  | Observed result                                                      |
| ------- | -------------------------------------------------------------------- |
| Swagger | 30 raw records describing two path-level defects                     |
| Native  | GET/PUT item operations and GET collection operation: three warnings |

Native targets are `SwapResources.get`, `create`, and `list`, lines 121, 129, 146.
Both source and selected-version HTTP metadata contain the same three units.
The source path policy has one material check, not 30 independent checks.
The full [reference/path audit](receipts/step6-swagger-cardinality-audit.json)
retains every observation and chain. No production rule change is needed.

## Validation

Required package builds, library validation, generated documentation, actual
incorrect/correct example compilation, formatting, standard/type-aware lint,
spelling, Chronus, ruleset checks, source/artifact drift checks, and whitespace
checks passed on the unchanged tested native content.

| Check                              | Result                                                    |
| ---------------------------------- | --------------------------------------------------------- |
| Focused native rule / registration | 25 / 5 tests; scoped rule coverage 100%                   |
| Whole ARM package                  | 671 tests in 81 files; 541.73 seconds; one initial worker |
| Azure rulesets                     | 9 tests                                                   |
| Injected real-package controls     | 37 tests                                                  |
| Coverage harness regressions       | 75 tests                                                  |
| Operation comparator               | 8 tests                                                   |
| Real-spec native population        | 487 successes; no failures or unassessed projects         |

Default test/hook timeouts were unchanged. The injected suite covers actual
package loading, explicit versus configured activation, inherited short options,
source suppression, compliance, missing-rule failures, and existing HTTP/boolean
alignment controls. Direct Spectral controls preserve the original selector and
function, removing only unsupported Azure `rpcGuidelineCode` metadata: one/four
eligible methods yield one diagnostic; POST-only and canonical controls yield
none. This is not a fresh AutoRest production-pipeline run.

The broad tooling-package typecheck has **32 unchanged unrelated diagnostics**;
it is not claimed as a full typecheck pass. Task-owned errors were corrected and
are zero. The first injected controls had six fixture import-order failures;
the corrected final run passed all 37. Earlier failed native drafts and original
typecheck/import logs remain under [validation](validation). No counters were
reset. An optional aggregate-archive preflight rejected the distinct candidate
integration generator record before creating an archive. That helper was not
retried; original package archives and exact standalone source assets preserve
the required inputs instead.

The full run lasted **80m 12s**: baseline preparation/integrity/copy **48m 20s**,
six-worker target-only native execution **12m 54s**, and final integrity/report
completion **18m 58s**. Native execution stayed below its 3,600-second limit;
the full wall-clock run did not finish within one hour. All processes stopped.
No setup/final integrity step is omitted from this total.

## Recovery and replay

Download assets from the dedicated
[input release](https://github.com/msyyc/typespec-azure/releases/tag/lint-migration-path-contains-resource-group-20261027).
Verify every filename, size, and SHA-256 against `publication-inputs.json` before
use. The manifest maps each asset to its restore path. Standalone source assets
preserve the tested working-tree bytes independently of Git line-ending changes.
The preserved source ref is separate from runtime injection/generated outputs.

**Read saved evidence:** retrieve this committed report, structured/native
receipts, and the linked baseline descriptor/asset. Published receipts replace
host paths and strip terminal control sequences. Their original and published
hashes are distinct; sanitized native receipts are not a reusable CLI baseline.
Never pass them as a fabricated sealed baseline.

**Reanalyze saved observations:** use the dependency-free comparator and its
tests from `replay`. Recover the baseline's actual `_meta.json` and referenced
Swagger documents, the committed original-observation/cardinality receipts,
operation-audit receipts, and all 487 native receipts. Numerical replay checks
the exact reference edges and regenerates raw/comparable counts. It does not
execute either linter or regenerate the semantic conclusion.

```powershell
node --test .\replay\compare-operation-units.test.mjs
node .\replay\compare-operation-units.mjs `
  C:\replay\baseline\dataset `
  .\receipts\step6-swagger-member-observations.json `
  .\receipts\step6-swagger-cardinality-audit.json `
  .\receipts\operation-audit `
  C:\replay\operation-comparison.json `
  C:\replay\native-receipts
```

The last directory must contain the retained `native-N.json` receipts at its
root. The committed `native-results` directory already has that layout.

**Regenerate the comparison:** recover the recorded candidate base and its exact
core gitlink, overlay all twelve tested source assets, and recover the frozen
specs commit from the preservation ref. Recover the tooling base and overlay
all six tooling source assets. Use Node 26.5.0 and each repository's recorded
package manager; build the required integration closure. Restore the 21 package
assets and the complete unmodified baseline archive. Configure only the
machine-approved registry process-locally; do not publish registry credentials.

From `packages\typespec-lintdiff`, with specs pnpm 12.6.0 on PATH:

```powershell
node --import tsx/esm test\harness\native-coverage.ts `
  --candidate-repo C:\replay\candidate `
  --specs-repo C:\replay\specs `
  --tgz-dir C:\replay\candidate-packages `
  --validator-rule PathContainsResourceGroup `
  --tsp-rule @azure-tools/typespec-azure-resource-manager/resource-group-path-parameter `
  --scope source --baseline-run C:\replay\baseline `
  --baseline-policy frozen-reference --candidate-working-tree true `
  --native-mode target-only --concurrency 6 --native-budget-seconds 3600 `
  --output C:\replay\new-run
```

Run the retained injected-package controls before an expensive rerun. Never
overwrite the baseline or old output. Installation paths and private registry
availability can differ; recorded locks and packages are not a claim that every
transitive registry dependency is vendored. Full dependency installation/build
and a second complete compiler/emitter execution have not been claimed merely
from downloading assets or replaying counts. Publication/replay verification
receipts state which recovery paths were actually exercised.
