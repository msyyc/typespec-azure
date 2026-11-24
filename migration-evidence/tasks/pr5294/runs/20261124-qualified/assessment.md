# Source-impact assessment and corpus-driven qualification

## Source comment dispositions

This cycle addresses only the seven admitted source-impact comments on
[PR #5294](https://github.com/Azure/typespec-azure/pull/5294), not the ten
other eligible non-source findings. Admission was frozen at `81ed0f8ff2`.
All comments are human contributions by `markcowl`; no thread resolution is changed.
Published source: [`9e413f4725`](https://github.com/msyyc/typespec-azure/commit/9e413f47259b4a58b60c2aa05f48791916899f6d).

| Finding                                                                                 | Original recommendation                                          | Final action and evidence                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [MARK5294-19](https://github.com/Azure/typespec-azure/pull/5294#discussion_r4637006553) | Accept default-visibility wording                                | Implemented; default visibility is valid, explicit non-Update input remains checked.                                                                                                                             |
| [MARK5294-21](https://github.com/Azure/typespec-azure/pull/5294#discussion_r4637057026) | Defer scalar equivalence                                         | Retained layout-only semantics: equality versus assignability and derived scalar/union policy are not specified by these three Swagger checks. No scalar policy added or parity claimed.                         |
| [MARK5294-22](https://github.com/Azure/typespec-azure/pull/5294#discussion_r4637090865) | Qualified resource lifecycle check                               | Implemented for unambiguous counterparts lacking Update. Effective input filtering and HTTP-inferred response boundaries remain; ordinary Read/Query-only input is not automatically an exposed PATCH violation. |
| [MARK5294-27](https://github.com/Azure/typespec-azure/pull/5294#discussion_r4637196916) | Remove provisioning-state name policy with lifecycle replacement | Revised after corpus: retain the narrow ARM policy. Unannotated provisioning state and a suppressed owning rule do not provide replacement coverage.                                                             |
| [MARK5294-28](https://github.com/Azure/typespec-azure/pull/5294#discussion_r4637210127) | Replace reserved names with resource lifecycle                   | Partially adopted: add generic lifecycle checks, but retain reserved fields after the blanket replacement lost 52 warnings. One OR predicate avoids duplicate immutable reports.                                 |
| [MARK5294-29](https://github.com/Azure/typespec-azure/pull/5294#discussion_r4637410981) | Type-kind dispatch                                               | Implemented Union/Model/default switch with model handling separated; existing traversal boundaries retained.                                                                                                    |
| [MARK5294-30](https://github.com/Azure/typespec-azure/pull/5294#discussion_r4637425963) | Recursive Record control                                         | Added recursive indexer-value boundary plus a named sibling that must still be checked.                                                                                                                          |

## Reserved-field policy

**Coverage status:** The final candidate retains every historical original-policy
diagnostic. The first, lifecycle-only candidate did not: it removed 52 reserved-field
warnings and added 76 generic lifecycle warnings. Net +24 concealed the loss.

**Cause and evidence:** Exact counterpart traces cover all 128 changed occurrences
in 39 projects. Removed warnings comprise 38 default/all-lifecycle counterparts,
two explicit Create/Read/Update counterparts and 12 missing counterparts.
The latter all retain a distinct exact-target layout diagnostic; they are not
12 wholly undetected defects, but the independent immutable policy was lost.
[`first-attempt-delta.json`](first-attempt-delta.json) and
[`predicate-traces.json`](predicate-traces.json) preserve source targets, exact
operation routes and annotations. Each trace event is one operation/property
occurrence; its `changes.count` is an aggregate source-diagnostic annotation,
not a per-event multiplier.

### Gap example: missing lifecycle metadata

- **Classification:** Regression introduced by the rejected redesign.
- **Project/source:** TrafficManager / `2026-09-01`, selected Swagger population at frozen
  specs `2cd3c5dd6d00`, `models.tsp:311,316,321`.

```typespec
id?: armResourceIdentifier;
name?: string;
type?: string;
```

These are actual members of its custom `Resource`, without lifecycle annotations.
They appear in two PATCH operations, yielding six removed warnings.
Default visibility includes Update; it does not establish that ARM permits
PATCHing the resource identity.

The pinned [Swagger guideline RPC-Patch-V1-02](https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/un-supported-patch-properties.md)
independently prohibits writable root id/name/type/location and
properties.provisioningState. Its predicate is not conditional on a correct
resource-model annotation. Final observations reproduce the original six warnings.

### Gap example: suppressed provisioning-state owner

CustomLocations / `2021-08-31-preview`, `models.tsp:187-188`:

```typespec
#suppress "@azure-tools/typespec-azure-resource-manager/arm-resource-provisioning-state" "FIXME: Update justification, follow aka.ms/tsp/conversion-fix for details"
provisioningState?: string;
```

The resource and PATCH use this same unannotated declaration. The first candidate
lost its immutable warning. The owning rule only checks recognized resource
models and its warning is explicitly suppressed here; no replacement diagnostic
was captured. The final rule retains the PATCH safeguard.

### Gap example: explicitly Update-visible reserved field

Cosmos DB `DatabaseAccountGetResults.tsp:27` and `ClusterResource.tsp:29`
declare resource `location` with Create/Read/Update visibility. Two warnings
were lost by trusting that annotation. Incorrect Update metadata cannot override
the independent ARM location restriction; the final rule restores both.

### Gap example: no resource counterpart

Automation / `2024-10-23`, `AutomationAccountUpdateParameters.name`, `models.tsp:2334`, is
exposed input but absent from the comparison resource's effective property map.
Eleven Automation names and one Resources resource-group name have this shape.
Layout warnings survive, but the lifecycle-only implementation has no
resource-property fact on which to enforce immutability. The corrected predicate
retains the independent reserved-name warning without treating arbitrary
unmatched properties as immutable.

**Analysis and action:** Qualify, rather than force adoption of, the blanket
review suggestion. Keep the small name-based ARM safeguard and OR it with the
resource-lifecycle predicate; report immutable once if both apply. This is
required-policy preservation, not a repair to equalize raw totals. Any retirement
of this reserved-field policy requires an explicit policy decision and evidenced
replacement coverage.

## Generic lifecycle policy

**Coverage status:** Broader TypeSpec policy, outside the three Swagger members'
immutable selector. All 76 added diagnostics across 25 projects have exact
counterpart evidence: 43 Create/Read and 33 Read-only resource members.
These are modeled resource/PATCH contract conflicts, not 76 established service
defects. Check the service contract before correcting annotations or excluding
input; legacy suppressions do not prove the service is immutable.

### Gap example: Create/Read resource, explicit Update PATCH

ElasticSan / `2026-05-01-preview`, `models.tsp:457-459` versus `706-707`:

```typespec
@madeOptional(Versions.v2026_05_01_preview)
@visibility(Lifecycle.Read, Lifecycle.Create)
baseSizeTiB?: int64;
```

```typespec
@visibility(Lifecycle.Update)
baseSizeTiB?: int64;
```

These are different models, `ElasticSanProperties` and
`ElasticSanUpdateProperties`, for the same encoded property.
The new warning identifies this contradictory modeled update contract; it does
not prove which annotation reflects the service. This includes eight ElasticSan
findings, all with exact source/counterpart traces.

### Gap example: Read-only resource, writable PATCH

KeyVault / `2026-06-01-preview`, `Secret.tsp:38-39` declares:

```typespec
@visibility(Lifecycle.Read)
tags?: Record<string>;
```

Its `SecretPatchParameters`, `models.tsp:2365`, instead contains:

```typespec
tags?: Record<string>;
```

The new warning compares those exact counterparts. ContainerApps likewise has
Read-only outbound IP/event-stream fields and a Create/Read environment ID
exposed by its PATCH model. These cases are not evidence that every same-named
field or every response property should be rejected.

**Analysis and action:** Retain the qualified modeled-resource lifecycle check,
with default/Update ordinary controls, effective request filtering, ambiguity
handling and the existing identity exemption. Do not credit these broader
warnings to `UnSupportedPatchProperties` or infer migration improvement from them.
They remain in the raw receipts and check-exclusion ledger, even when also outside
the selected API-version population; exclusions are not double-counted.

## Current diagnostic accounting

The final 487-project run has zero failed/unassessed projects:

| Check                    | Historical configured | Final configured |            Original-policy scoped |
| ------------------------ | --------------------: | ---------------: | --------------------------------: |
| Required                 |                   478 |              478 |   Included in 881 safety findings |
| Default                  |                   436 |              436 |   Included in 881 safety findings |
| Visibility               |                     0 |                0 |          Included in safety scope |
| Layout                   |                   361 |              361 |                               304 |
| Reserved immutable       |                    62 |               62 |                                61 |
| Other resource lifecycle |                     0 |               76 | Excluded by original check policy |
| Total                    |                 1,337 |            1,413 |                             1,246 |

The final original-policy multiset is identical in all 487 projects. The final
76 additions match the first candidate's additions exactly. All 52 first-candidate
removals are restored. The [accepted assessment](accepted-assessment.json)
contains exact per-project additions, all 167 check/population exclusions, scoped
totals, both project-count directions and source-target identity validation.
It preserves 103 Swagger excess / 374 TypeSpec excess, absolute 477, net -271,
not just the net. The [main report](../../migration.md) and all three member notes
use this one scope and the unchanged complete signed reconciliation.

The [complete broader-finding inventory](lifecycle-differences.md) groups every
excluded generic warning by project, exact PATCH route, source target and
counterpart. It preserves all 76 occurrences, including shared declarations
used by distinct operations, rather than listing only representative examples.

## Canonical regressions

The owning suite is
`packages/typespec-azure-resource-manager/test/rules/no-unsafe-patch-body-properties.test.ts`.
Reuse these cases in later reviews before requesting another corpus:

| Corpus/source boundary                                       | Canonical case or control                                                               | Disposition protected                                             |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Default reserved lifecycle                                   | `does not trust missing resource lifecycle annotations for reserved %s`                 | Blanket name removal rejected                                     |
| Explicit Update on reserved field                            | `does not let explicit Update visibility override ARM reserved-field policy`            | Metadata does not retire ARM restriction                          |
| Missing comparison resource                                  | `preserves ARM reserved-field checks without a resource counterpart`                    | Preserve reserved policy, not arbitrary name matching             |
| Unannotated/suppressed provisioning owner                    | `does not trust unannotated provisioning state even when its owning rule is suppressed` | No assumed replacement coverage                                   |
| Matched Read/Create/Query resource                           | `checks resource members with %s visibility`                                            | Generic lifecycle restriction                                     |
| Both predicates match                                        | `checks encoded resource visibility and reports reserved fields only once`              | No duplicated immutable diagnostic                                |
| No resource restriction                                      | `accepts resource properties that allow Update: %s`                                     | Default/Update ordinary compliant controls                        |
| Inferred response has no readable body or filters root Query | Query-response boundary tests                                                           | Do not fabricate missing resource lifecycle facts                 |
| Recursive Record value with named sibling                    | Recursive Record canonical case                                                         | Do not expand arbitrary indexer values or stop sibling validation |

The [18 exact comparisons](gap-controls.json) exercise six minimized public-API
fixtures against admitted, rejected and corrected predicates on one identical
current fixture closure. Reserved default/Update/no-counterpart/provisioning
cases are `warning / none / warning`; generic lifecycle is `none / warning /
warning`; ordinary default visibility is valid in all three. This is not a
replay of the historical compiler closure. Canonical controls remain the cheap
future regression mechanism; the corpus evidence remains the integration gate.

## Validation and recovery

- [Structured validation receipt](local-validation.json) records commands,
  actual results and limits; [CI snapshot](ci.json) records available checks
  once at the published head. Pending CI is not a pass and was not awaited.
- Final candidate: 112 canonical tests; ARM build; root `pnpm format` and
  `pnpm lint`; 36 injected PATCH controls in two activation modes; 37 applicable
  portable controls; all 487 real-spec projects passed. Six unrelated,
  unregistered resource-group fixtures were inapplicable before execution.
- [Published guide snippets](snippet-validation.json) were executed through the
  existing public Tester: incorrect example exactly five warnings, correct
  example none. This is one-time evidence, not continuous documentation testing.
- The initial unchanged baseline failed from stale built libraries and passed
  104 tests after rebuilding the dependency closure. Two preflight Query fixtures
  had invalid HTTP response assumptions and were corrected; the discovered
  boundaries became canonical tests. Failed logs/fixtures are retained.
- The first full run completed successfully but its lifecycle-only design
  failed the semantic assessment. Its 487 receipts, rejected artifact, all
  128 trace occurrences, exact 12-target layout check, and 18-assertion gap
  replay are retained alongside the corrected final run.
- No Swagger generation or Swagger validation was rerun. Both full runs used
  the same shared baseline and exclusive machine-wide corpus lock.

Download the unique [evidence asset](archive.json), verify its SHA-256, then
extract it into a new directory. Its `archive-manifest.json` independently
hashes every portable payload. `first-attempt/` and `final-attempt/` preserve
all project receipts; `artifacts/` preserves all 20 final packages plus the
rejected ARM package. The unchanged 19 dependency artifacts are identified
by their hashes. `published-source/` preserves exact assessed file bytes.

`replay-and-local-validation/` retains the extraction, controls, runner and
assessment scripts. Local absolute paths are replaced with explicit placeholders;
configure them to isolated checkouts rather than using a shared mutable checkout.
Use saved JSON receipts for recounting: no compiler or corpus is required to
reproduce the accounting. A new compile requires the exact pinned specs,
baseline, source/core/artifact closure and the existing exclusive runner gate.

The original emitted-field, version/route, associated-resource representation
and unmeasured owning/suppression gaps remain. This source-fix assessment neither
declares full Swagger equivalence nor authorizes policy retirement or asserts
that unrelated PR feedback is complete.
