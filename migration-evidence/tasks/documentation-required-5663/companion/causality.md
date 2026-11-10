# CI-derived documentation compatibility proposal

## Outcome and scope

The completed [external integration job](https://github.com/Azure/typespec-azure/actions/runs/42776863168/job/129697292505) for [linter PR #5663](https://github.com/Azure/typespec-azure/pull/5663) contains **10,697 occurrences**, representing **7,901 distinct diagnostic tuples and authored targets across 219 files** in **208 project log groups**. Every target was reconciled against a separately frozen current consumer checkout. There are zero unresolved, stale or false-positive targets in this extracted population. The consumer patch adds exactly 7,901 declaration-specific suppressions and deletes no lines.

The suppression-only draft is [Azure/azure-rest-api-specs#48090](https://github.com/Azure/azure-rest-api-specs/pull/48090). This is a compatibility proposal, not successful consumer compilation, green CI, full-corpus equivalence or merge readiness. The [group assessment](../migration.md) retains its separate historical coverage limitations.

## Frozen identities and provenance limitation

| Role                                | Identity                                                                                                                                                               |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Failed run/job                      | [42776863168 / 129697292505](https://github.com/Azure/typespec-azure/actions/runs/42776863168/job/129697292505)                                                        |
| Tested linter                       | `2c6596126f281d78ca06fb23afc9ef8ab37684b8`                                                                                                                             |
| Linter comparison base              | `4184cf254ea0420446ebe9bc3b978b2da342ca76`                                                                                                                             |
| Compiler/HTTP closure               | `8574d5453f7bf9a07dc09bd41edac579af71d94b`                                                                                                                             |
| Original complete job log SHA-256   | `c2bb7a4ad5ac1f8e2db42c08863eb15dfbbaba5659e2cad50f4461c6a6b5d0cd`                                                                                                     |
| Exact consumer commit tested by CI  | **Unknown**: the full checkout log names `typespec-next` but omits its commit, and the run has no downloadable artifacts                                               |
| Independently fetched proposal base | [06472951865696fb06a0e36ece718d62bf4edc33](https://github.com/Azure/azure-rest-api-specs/commit/06472951865696fb06a0e36ece718d62bf4edc33) on canonical `typespec-next` |
| Published consumer source           | [369d77dcf0db154c6c71c39a6f6d166aee3bab9b](https://github.com/Azure/azure-rest-api-specs/commit/369d77dcf0db154c6c71c39a6f6d166aee3bab9b)                              |
| Consumer head/base                  | `Azure/azure-rest-api-specs:suppress/documentation-required-pr5663-20261110` -> `Azure/azure-rest-api-specs:typespec-next`                                             |

The proposal base is **not substituted for the unknown tested commit**. Instead, every proposed declaration independently satisfies the exact CI location, documentation and changed predicate in the frozen proposal source. This supports a current source-compatible proposal without falsely claiming a complete tested-source attestation. The original full log remains locally retained; only sanitized diagnostic/project evidence is published.

## Why these findings are caused by #5663

The [pre-change rule](https://github.com/Azure/typespec-azure/blob/4184cf254ea0420446ebe9bc3b978b2da342ca76/packages/typespec-azure-core/src/rules/require-docs.ts) lacks the `uninformative` reporting path. The [tested rule](https://github.com/Azure/typespec-azure/blob/2c6596126f281d78ca06fb23afc9ef8ab37684b8/packages/typespec-azure-core/src/rules/require-docs.ts) introduces the supplied-description name/placeholder check. Its normalization trims, removes periods and ignores case.

Only the exact new message was extracted: `Description must not match the name of the node it describes.` Existing missing-documentation `default` findings, blank-content `empty` findings and other rules are outside this extraction. Sharing a rule code alone was not used as causal evidence.

Each included source target has an exact direct `@doc` string or documentation comment matching the logged description. Its authored name or explicit HTTP wire name matches the logged comparison name, or its normalized text is the placeholder `description`. Status-code name exemptions, existing target suppressions, ambiguous direct docs and inline insertion hazards were checked. No unresolved case was extrapolated into an annotation.

| Authored target kind | Unique annotations |
| -------------------- | -----------------: |
| Union variant        |              7,192 |
| Enum member          |                522 |
| Model property       |                138 |
| Model                |                 38 |
| Union                |                 10 |
| Operation            |                  1 |
| **Total**            |          **7,901** |

Named declarations match the compiler syntax identifier's exact start. Seventy-six unnamed string variants instead match their exact variant-node start, including the leading doc/decorator span; the string literal and direct documentation independently confirm identity. Three HTTP properties use an explicit `@header("Content-Type")`, rather than the authored `contentType`, as the confirmed comparison name. No fuzzy location search or inferred source drift was accepted.

Representative frozen-base witnesses include [DocumentTranslation's `format`](https://github.com/Azure/azure-rest-api-specs/blob/06472951865696fb06a0e36ece718d62bf4edc33/specification/translation/data-plane/DocumentTranslation/models.tsp#L243-L244), [Maps Route's explicit header](https://github.com/Azure/azure-rest-api-specs/blob/06472951865696fb06a0e36ece718d62bf4edc33/specification/maps/data-plane/Route/routes.tsp#L10-L14), and [EventGrid's unnamed string variants](https://github.com/Azure/azure-rest-api-specs/blob/06472951865696fb06a0e36ece718d62bf4edc33/specification/eventgrid/data-plane/EventGridSystemEvents/Microsoft.EventGrid/EventGrid.tsp#L6-L12).

## Project and entrypoint attribution

The [tested suite configuration](https://github.com/Azure/typespec-azure/blob/2c6596126f281d78ca06fb23afc9ef8ab37684b8/.typespec-integration/config.yaml) selects `specification/**/tspconfig.yaml`, excluding `specification/ai-foundry/data-plane/Foundry/**`. It tries available `client.tsp` with `--no-emit`, then `main.tsp`; the [compile command](https://github.com/microsoft/typespec/blob/8574d5453f7bf9a07dc09bd41edac579af71d94b/packages/tsp-integration/src/package-manager.ts) appends `--warn-as-error`. These warnings therefore appear with error severity in the captured output.

The [project verifier](https://github.com/microsoft/typespec/blob/8574d5453f7bf9a07dc09bd41edac579af71d94b/packages/tsp-integration/src/validate.ts) stops at the first failing entrypoint and returns that output without naming the failed entrypoint. All 10,697 occurrences retain the actual CI project group and full-log line. Available entrypoint candidates in the frozen proposal base are recorded separately; where both exist, this evidence does not guess which one failed or claim both ran. Repeated project imports/semantic instances remain separate raw occurrences, not additional authored edits.

## Suppression-only change and inspection

Each confirmed declaration receives only:

```tsp
#suppress "@azure-tools/typespec-azure-core/documentation-required" "Preserve the existing published API description for backward compatibility."
```

The fully qualified code and justification follow the [TypeSpec directive documentation](https://typespec.io/docs/language-basics/directives/). The directive is attached to the diagnosed declaration, before its existing docs/decorators, not to an enclosing namespace as a blanket opt-out.

Complete diff inspection verified 219 `.tsp` files, exactly 7,901 added annotation lines and zero deleted lines. Removing only those exact annotations restores the original source content. Syntax-only parsing inspected directive attachment at all targets; this is source reconciliation, **not compilation, lint execution or proof of emitted-output equality**. Existing descriptions, declarations, API names, baseline suppressions, dependencies, lockfiles, generated Swagger and CI settings are unchanged.

Remote readback verified the draft's same-repository head/base, exact description, complete changed-file inventory and all 219 source blob identities. GitHub omits patches and reports zero per-file changes for six files; their blob hashes match the completely inspected local commit, and PR-wide counts are 7,901 additions with no deletions. The machine manifest retains that display/API limitation rather than treating omitted patches as empty edits.

**Local consumer compilation, build, tests, lint, formatting, integration, dependency setup and emission were intentionally not run.** No CI run was requested, rerun or awaited. Ordinary publication-triggered checks may run independently; their success is not claimed.

## Machine evidence and recovery

- [manifest.json](manifest.json): identities, counts, suite/entrypoint limitations, inspection result and artifact hashes.
- [occurrences.jsonl](occurrences.jsonl): all 10,697 original occurrence IDs, full-log lines, project groups and diagnostic IDs.
- [diagnostics.jsonl](diagnostics.jsonl): 7,901 exact diagnostic tuples, causal classifications, occurrence/project provenance and target IDs.
- [targets.jsonl](targets.jsonl): 7,901 authored identities, direct docs, original positions, frozen working-source hashes, UTF-16 insertion offsets and diagnostic mappings.
- [projects.jsonl](projects.jsonl): 208 observed project groups and separately inspected current-base entrypoint candidates.
- [exclusions.jsonl](exclusions.jsonl): empty; all extracted diagnostics were independently reconciled.

Artifact checksums protect published evidence bytes, not the missing CI consumer identity. Source hashes describe the frozen UTF-8 working-source content used for matching; Git commits above independently identify canonical source and the actual patch. Recovery needs the published evidence plus the pinned public source, not a local report path or regenerated Swagger.
