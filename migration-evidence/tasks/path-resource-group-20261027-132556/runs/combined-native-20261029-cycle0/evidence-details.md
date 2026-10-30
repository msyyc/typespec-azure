# Combined scope-path naming evidence

## Differences grouped by project

Only DataMigration and Network differ. Advisor is a matching positive control,
and 484 remaining projects have zero selected findings on both sides.
The [complete operation comparison](receipts/combined-operation-comparison.json)
and [automatic report](coverage.json) preserve every selected project.

| Project | Swagger raw | TypeSpec raw | Swagger operation/member checks | TypeSpec operation/member checks | Disposition |
| --- | ---: | ---: | ---: | ---: | --- |
| DataMigration | 11 | 26 | 26 | 26 | No rule update: path-to-method multiplicity |
| Network | 30 | 3 | 3 | 3 | No rule update: referenced-input repetition |

## DataMigration method multiplicity

- **Classification:** count-only; fully explained.
- **Project/API version:** `specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration` / `2025-09-01-preview`.
- **Observed:** Swagger 11, TypeSpec 26; comparable 26/26.
- **Raw gap:** TypeSpec minus Swagger +15; absolute 15; relative 57.69% using the larger raw count as denominator. No opposite-direction cancellation.
- **Source:** [`DataMigrationService.tsp`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/DataMigrationService.tsp).

**Verified TypeSpec source excerpts**

Lines 54–65:

```tsp
alias DataMigrationServiceOps = Azure.ResourceManager.Legacy.LegacyOperations<
  {
    ...ApiVersionParameter;
    ...SubscriptionIdParameter;

    /** Name of the resource group */
    @path
    @segment("resourceGroups")
    @key
    groupName: string;

    ...Azure.ResourceManager.Legacy.Provider;
```

Lines 78–89:

```tsp
interface DataMigrationServices {
  /**
   * The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The GET method retrieves information about a service instance.
   */
  @summary("Get DMS (classic) Service Instance")
  @tag("Service resource")
  @tag("Standard operation")
  @tag("GET")
  get is DataMigrationServiceOps.Read<DataMigrationService>;

  /**
   * The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The PUT method creates a new service or updates an existing one. When a service is updated, existing child resources (i.e. tasks) are unaffected. Services currently support a single kind, "vm", which refers to a VM-based service, although other kinds may be added in the future. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request ("ServiceIsBusy"). The provider will reply when successful with 200 OK or 201 Created. Long-running operations use the provisioningState property.
```

Lines 91–100:

```tsp
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-put-operation-response-codes" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  @summary("Create or update DMS (classic) Instance")
  @tag("Service resource")
  @tag("Standard operation")
  @tag("PUT")
  createOrUpdate is DataMigrationServiceOps.CreateOrUpdateAsync<
    DataMigrationService,
    Response =
      | ArmResourceUpdatedResponse<DataMigrationService>
      | ArmResourceCreatedResponse<
```

| Exact path | Eligible methods | Swagger raw | Comparable Swagger/TypeSpec | Actual TypeSpec operation targets |
| --- | --- | ---: | ---: | --- |
| `/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services` | get | 1 | 1/1 | [GET `Microsoft.DataMigration.DataMigrationServices.listByResourceGroup`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/DataMigrationService.tsp#L151) |
| `/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}` | delete, get, patch, put | 1 | 4/4 | [GET `Microsoft.DataMigration.DataMigrationServices.get`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/DataMigrationService.tsp#L86); [PUT `Microsoft.DataMigration.DataMigrationServices.createOrUpdate`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/DataMigrationService.tsp#L96); [PATCH `Microsoft.DataMigration.DataMigrationServices.update`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/DataMigrationService.tsp#L116); [DELETE `Microsoft.DataMigration.DataMigrationServices.delete`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/DataMigrationService.tsp#L129) |
| `/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects` | get | 1 | 1/1 | [GET `Microsoft.DataMigration.Projects.list`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/Project.tsp#L127) |
| `/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}` | delete, get, patch, put | 1 | 4/4 | [GET `Microsoft.DataMigration.Projects.get`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/Project.tsp#L81); [PUT `Microsoft.DataMigration.Projects.createOrUpdate`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/Project.tsp#L90); [PATCH `Microsoft.DataMigration.Projects.update`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/Project.tsp#L100); [DELETE `Microsoft.DataMigration.Projects.delete`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/Project.tsp#L109) |
| `/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/files` | get | 1 | 1/1 | [GET `Microsoft.DataMigration.ProjectFiles.list`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/ProjectFile.tsp#L118) |
| `/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/files/{fileName}` | delete, get, patch, put | 1 | 4/4 | [GET `Microsoft.DataMigration.ProjectFiles.get`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/ProjectFile.tsp#L78); [PUT `Microsoft.DataMigration.ProjectFiles.createOrUpdate`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/ProjectFile.tsp#L87); [PATCH `Microsoft.DataMigration.ProjectFiles.update`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/ProjectFile.tsp#L97); [DELETE `Microsoft.DataMigration.ProjectFiles.delete`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/ProjectFile.tsp#L109) |
| `/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks` | get | 1 | 1/1 | [GET `Microsoft.DataMigration.ProjectTasks.list`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/ProjectTask.tsp#L137) |
| `/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName}` | delete, get, patch, put | 1 | 4/4 | [GET `Microsoft.DataMigration.ProjectTasks.get`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/ProjectTask.tsp#L79); [PUT `Microsoft.DataMigration.ProjectTasks.createOrUpdate`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/ProjectTask.tsp#L97); [PATCH `Microsoft.DataMigration.ProjectTasks.update`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/ProjectTask.tsp#L107); [DELETE `Microsoft.DataMigration.ProjectTasks.delete`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/ProjectTask.tsp#L119) |
| `/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/serviceTasks` | get | 1 | 1/1 | [GET `Microsoft.DataMigration.ServiceTasks.list`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/ProjectTask.tsp#L272) |
| `/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/serviceTasks/{taskName}` | delete, get, patch, put | 1 | 4/4 | [GET `Microsoft.DataMigration.ServiceTasks.get`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/ProjectTask.tsp#L214); [PUT `Microsoft.DataMigration.ServiceTasks.createOrUpdate`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/ProjectTask.tsp#L232); [PATCH `Microsoft.DataMigration.ServiceTasks.update`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/ProjectTask.tsp#L242); [DELETE `Microsoft.DataMigration.ServiceTasks.delete`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/ProjectTask.tsp#L254) |
| `/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/skus` | get | 1 | 1/1 | [GET `Microsoft.DataMigration.DataMigrationServices.listSkus`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/DataMigrationService.tsp#L220) |

**Verified owning documents and reference chains:** `projects/specification/datamigration/resource-manager/Microsoft.DataMigration/DataMigration/swagger/preview/2025-09-01-preview/openapi.json`. Every group retains its unique document, original attribution mode, input occurrences and exact checked local-reference edges in [the complete grouping receipt](receipts/combined-operation-comparison.json).


**Verified frozen Swagger path/method excerpt**

```json
{
  "paths": {
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services": {
      "get": {
        "operationId": "Services_ListByResourceGroup"
      }
    }
  }
}
```

**Explanation:** The Swagger linter reports an invalid path once when eligible methods exist. The TypeSpec linter reports each concrete operation; expanding the 11 exact owning paths gives the same 26 operations. POST actions are not counted. **Disposition:** no TypeSpec rule update required.

## Network reference multiplicity

- **Classification:** count-only; fully explained.
- **Project/API version:** `specification/network/resource-manager/Microsoft.Network/Network/Network` / `2026-03-01`.
- **Observed:** Swagger 30, TypeSpec 3; comparable 3/3.
- **Raw gap:** TypeSpec minus Swagger -27; absolute 27; relative 90.00% using the larger raw count as denominator. No opposite-direction cancellation.
- **Source:** [`SwapResource.tsp`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/network/resource-manager/Microsoft.Network/Network/Network/SwapResource.tsp).

**Verified TypeSpec source excerpts**

Lines 53–63:

```tsp
alias CloudServiceOps = Legacy.ExtensionOperations<
  {
    ...ApiVersionParameter;
    ...SubscriptionIdParameter;

    #suppress "@azure-tools/typespec-azure-core/documentation-required" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
    @path
    @segment("resourceGroups")
    groupName: string;

    #suppress "@azure-tools/typespec-azure-core/documentation-required" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
```

Lines 117–129:

```tsp
  /**
   * Gets the SwapResource which identifies the slot type for the specified cloud service. The slot type on a cloud service can either be Staging or Production
   */
  @tag("VipSwap")
  get is CloudServiceOps.Read<SwapResource, ErrorType = CloudError>;

  /**
   * Performs vip swap operation on swappable cloud services.
   */
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-put-operation-response-codes" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  #suppress "@azure-tools/typespec-azure-resource-manager/no-response-body" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
  @tag("VipSwap")
  create is CloudServiceOps.CreateOrUpdateAsync<
```

| Exact path | Eligible methods | Swagger raw | Comparable Swagger/TypeSpec | Actual TypeSpec operation targets |
| --- | --- | ---: | ---: | --- |
| `/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots` | get | 15 | 1/1 | [GET `Microsoft.Network.SwapResources.list`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/network/resource-manager/Microsoft.Network/Network/Network/SwapResource.tsp#L146) |
| `/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots/{singletonResource}` | get, put | 15 | 2/2 | [GET `Microsoft.Network.SwapResources.get`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/network/resource-manager/Microsoft.Network/Network/Network/SwapResource.tsp#L121); [PUT `Microsoft.Network.SwapResources.create`](https://github.com/msyyc/azure-rest-api-specs/blob/evidence/long-running-operations-options-validator-20261022-source/specification/network/resource-manager/Microsoft.Network/Network/Network/SwapResource.tsp#L129) |

**Verified owning documents and reference chains:** `projects/specification/network/resource-manager/Microsoft.Network/Network/Network/swagger/stable/2026-03-01/virtualNetwork.json`. Every group retains its unique document, original attribution mode, input occurrences and exact checked local-reference edges in [the complete grouping receipt](receipts/combined-operation-comparison.json).


**Verified frozen Swagger path/method excerpt**

```json
{
  "paths": {
    "/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/microsoft.Compute/cloudServices/{resourceName}/providers/Microsoft.Network/cloudServiceSlots": {
      "get": {
        "operationId": "VipSwap_List"
      }
    }
  }
}
```

**Explanation:** The same two invalid owning paths are encountered through multiple validator inputs. The original source attribution includes input-fallback cases and is not relabeled exact. A unique owner and every local `$ref` edge are independently rechecked against the immutable dataset. Collapsing only those proven repetitions and expanding eligible methods gives the same three operations. **Disposition:** no TypeSpec rule update required.

## Conservative location summaries

The automatic report retains **15
member-preserving file-independent Swagger paths**, **31
TypeSpec source locations**, and **0**
locationless TypeSpec diagnostics. These are conservative summaries, not matched
actionable checks; both failures at one operation remain separate raw findings.
The [independent saved-count receipt](receipts/saved-reanalysis.json) also derives
reported-file occurrences directly from all selected member observations.

## Matching controls and member evidence

Advisor's two exact paths bind to the same two operations. The independent
A-only/B-only/both/neither installed-package controls distinguish the two policies.
Four normalization controls reject equal-but-wrong member totals, a missing
member at a shared operation, fuzzy route matches and duplicate unit collapse.
No raw member diagnostic is assigned by message text.

Conservative file-independent Swagger paths and TypeSpec source locations are
retained separately in the automatic report; these different identity domains
do not establish correspondence. The dependency-free saved reanalysis derives
reported-file occurrences, member-preserving file-independent paths, native
source locations and locationless counts independently, while leaving every raw
diagnostic intact.

The subscription shard is absent from the complete saved index. The actual
injected production ARM ruleset registers `PathContainsSubscriptionId` as an
unresolved OAS2 error on GET/PATCH/PUT/DELETE paths with subscriptionIdParam
options; the [registration receipt](receipts/injected-controls.json) retains it.
This is a zero historical observation, not an omitted native check.

## Candidate integration and source identity

The actual candidate `tsp-integration` patch/install stages succeeded with the
15 retained artifacts, direct Node26.5 and specs pnpm12.6. Source package.json,
workspace and bootstrap lock bytes were restored and verified. Nine real
injected controls verify the loaded compiler, ARM and AutoRest entrypoint hashes
against packed contents before full native execution.

The full worker compiles with emit=[] and noEmit=true. The checked-in conditional
external-integration workflow's normal main.tsp validation can emit Swagger;
it was not run locally because Swagger generation is forbidden in this task.
Local required candidate integration is supported artifact patch/install,
registered/default-activation controls and all 487 real no-emit native compiles,
not a claim that the optional labeled CI emission job was reproduced.

The exact pre/post-build working-tree content snapshot and full packed file
inventories are in [artifact provenance](receipts/artifact-provenance.json).
Native commit `991c7ec6bd093ab253ab4a4af27e3425525c99d2` has [verified source equality](receipts/native-committed-source-equality.json) with this tested snapshot. [Independent local development review](receipts/local-development-review.json) is clean. Artifacts remain bound to the tested precommit working-tree identity; no rebuild from a future commit is claimed.

## Recovery and replay

Both immutable assets are **published and download-hash verified**. Exact URLs, candidate commit, hashes and the separate shared baseline are recorded in [assets-publication.json](receipts/assets-publication.json). The original [prepared-assets receipt](receipts/assets-prepared.json) is historical.

1. **Read saved evidence:** recover the eventual evidence commit and the compact
   reports/receipts. Current publication and A/B reviews remain pending.
2. **Reanalyze saved observations:** run
   `python replay\reanalyze-saved-counts.py <this-run> <output.json>`.
   It independently recomputes all 487 project counts and directional gaps from
   retained member observations and native receipts, with no compiler or network.
   Then run `python replay\render-migration.py <this-run> <migration-output.md>`
   to regenerate the four-section report from the retained authored template and
   actual saved counts. Content-bound input hashes prevent reusing this scoped
   assessment when inputs differ and renewed analysis/review is required.
3. **Regenerate coverage:** recover the exact tooling bundle, candidate source
   (eventual native commit, or retained base plus binary patch/untracked files),
   exact core gitlink and preserved specs commit. Verify every asset hash before
   extracting. Install/build only the recorded compatible closures. Recover the
   separate immutable shared baseline using `baseline-descriptor.json`: run
   `python -X utf8 -B <tooling>\.github\skills\analyze-native-lint-coverage\shared_baseline.py fetch --descriptor <this-run>\baseline-descriptor.json --output <fresh-baseline>`.
   Add `--archive <verified-archive>` only when that exact hash/size-bound archive
   already exists; output must be new. This fetch/verification path never emits
   Swagger. Then rerun the
   direct-Node analyzer with both --validator-rule selectors, one --tsp-rule,
   --scope source, --baseline-policy frozen-reference, --native-mode target-only,
   --candidate-working-tree true for the retained working-tree lane, native
   budget7200, concurrency2, and no filter/limit. Never regenerate Swagger.
   Recreate semantic controls against the injected artifacts before expensive
   native compilation: copy `replay\injected-controls.mjs` beside a copy of
   `receipts\artifact-provenance.json` in a fresh writable replay directory.
   Resolve the explicit `$SPECS` and `$TOOLING` placeholders in that script to
   recovered roots, then run it with pinned Node26. It refuses to overwrite a
   controls directory and checks all nine expectations, registered activation,
   suppression, production validator registrations and loaded-package hashes.
   The retained original fixture inputs also use explicit path placeholders;
   they are evidence, not runnable without that root binding.
4. **Investigate counts:** run the metadata audit helper with explicit run root
   and pinned worker path after the full run. Then run the comparison helper
   with run root and immutable Swagger grouping receipt. This validates current
   owner documents, reference edges, operation targets and selected-version
   metadata. It is not fuzzy correspondence or a projected lint rerun.

Native source-commit equality, independent local development review and asset upload/download hashes passed. Actual Git-blob bytes are checked before every evidence push. [Temporary fresh-checkout recovery](receipts/fresh-checkout-recovery.json) passed against the [initial evidence publication](receipts/evidence-initial-publication.json). Both distinct current GitHub checkpoints and the separate independent local readiness review are now clean; see [final review evidence](reviews/final-review-summary.json). Recovery verified source/packages/tooling/full sealed baseline and saved-data replay; it did not rerun native compiles or claim a full specs checkout.

## Validation and retained failures

38 canonical rule cases, 682 full ARM tests, nine ruleset tests, nine installed
controls, four comparison controls and four final documentation snippets passed.
Builds, generated rule/reference docs, explicit NUL formatting, package/root lint
and Chronus status passed. The original missing vite/client prerequisite and
non-greedy Chronus selector failures are retained beside successful authorized
recovery receipts; no failure was demoted or erased. Coordinator reserve used:
3/3; ordinary development draft corrections remain 3/3. No semantic repair cycle
or review budget was spent.

The exact runtime source/package receipts and automatic coverage results are
authoritative for this historical evaluation; transitive future package
resolution and unchanged emission are not claimed. Existing historical
resource-group-only A/B reviews do not review this combined source.

## Portable publication recovery

The earlier saved report roundtrip belongs to the [exact reviewed prepublication report](receipts/migration-reviewed-prepublication.md), before publication-status updates. Saved counts and assessment inputs remain unchanged; only the bound report template's publication metadata is updated.

Run `python replay\recover-published-inputs.py --evidence-root <fresh-evidence-checkout> --run-relative migration-evidence\tasks\path-resource-group-20261027-132556\runs\combined-native-20261029-cycle0 --recovery-root <new-recovery-directory> --node <pinned-Node26>` after checking out the recorded evidence commit. This downloads immutable assets, verifies every packed file, recovers exact native/core/tooling commits and frozen specs Git inputs, verifies the complete shared baseline with the recovered pinned helper, and replays saved counts/report/normalization controls. It performs no dependency installation, Swagger generation or full native compile rerun. The full specs working tree is not materialized; the receipt explicitly distinguishes commit/tree retention plus representative input recovery from a fresh full compilation.

## Final independent review applicability

[Summary](reviews/final-review-summary.json), [local readiness](reviews/scope-local-readiness-review-result.json), [full readiness checklist](reviews/scope-cycle0-readiness-checklist.json), [A parent exact collection](reviews/scope-A-parent-final/result.json), [B parent exact collection](reviews/scope-B-parent-final/result.json), and [API/input byte map](reviews/audit-byte-map.json) retain the separate four review gates and all original-hash/published-hash relationships. Collector request/poll/final-refetch API payloads and parent independent raw API responses are retained under `reviews/`; the manifests were verified against original private bytes before sanitizing known machine roots. Diagnostics, coordinates, target identities and counts were not rewritten.

A and B each consumed one of their own five-round budgets on native `991c7ec6bd093ab253ab4a4af27e3425525c99d2`, with zero findings, no fixes and no semantic repair cycle. Both numeric reviews are `COMMENTED` with Approval recommended, not formal GitHub approval. Independent local readiness reviewed evidence `eefbb2b927c0c502245352abf32a377d35c690c8`; this append adds only review/status metadata and updates the report-template hash binding. All pre-existing diagnostic and artifact inputs remain byte-identical. The final evidence commit/remote and Git blobs are recorded in the external terminal receipt after push, avoiding circular commit claims. Original draft3/3 and reserve3/3 remain exhausted; semantic repairs0/3 and all other counters are preserved. No new builds, installs, package tests, metadata audit or full native compilation were performed. The historical corpus, attribution, severity/activation and fresh-specs-recovery limitations remain applicable.
