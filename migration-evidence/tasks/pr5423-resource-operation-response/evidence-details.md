# Supporting evidence and recovery

## Assessment boundary

Final assessed source: `3b0603ab8d062af3c2ee54769db30cbf009aa133`; core:
`f87a4e2d51c5cc0b3d995d4c7542578d55799804`. Tooling:
`8345f684fad330568e55e40181c3d17cd8d8db7f`; frozen specs:
`2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`.

Two independent mappings use the same source, 15 immutable archives and complete
487-project population, with `scope: source`, `baseline-policy: frozen-reference`,
no filter/limit and concurrency two:

| Mapping              | Swagger members                                                                        | TypeSpec rule                   | Raw Swagger / TypeSpec |
| -------------------- | -------------------------------------------------------------------------------------- | ------------------------------- | ---------------------- |
| Resource consistency | PutRequestResponseSchemeArm, ConsistentResponseSchemaForPut, PutGetPatchResponseSchema | arm-resource-operation-response | 278 / 248              |
| PUT resource marker  | XmsResourceInPutResponse                                                               | arm-put-response-resource       | 155 / 57               |

These are not a general many-to-many comparison or a combined coverage percentage.
Configured and source-aligned TypeSpec totals agree in each mapping. Default
activation produces 248 consistency warnings and zero marker warnings; the new
marker rule is opt-in in the shared ARM ruleset and explicitly enabled for its
assessment. Authored suppressions remain in the configured observations. Captured
existing-owner diagnostics before suppression are credited separately as diagnostic
coverage, not added to configured raw totals.

Swagger represents the producer's latest emitted version; TypeSpec evaluates the
source program. Selected-version HTTP metadata supports individual correspondence,
not universal version-aligned equivalence or emitted structural equality.
`ConsistentResponseSchemaForPut` is explicitly evaluated through the pinned ARM
staging Spectral supplement, not treated as an absent production zero.
Historical `coverage_old.md`/`coverage-breakdown.md` reconciliation is not applicable
to this fresh official-package comparison.

## Final-source execution and recovery

Both mappings assessed all **487 projects successfully**, with zero failed or
unassessed projects. Swagger was neither regenerated nor revalidated.

The original consistency CLI terminated with exit 255 after 433 successful workers.
It did not record an application error; the pinned Node executable was subsequently
absent. The deletion/termination cause remains **unknown**; no antivirus attribution
is established. The original manifest, logs and receipts remain unchanged in the
immutable asset.

The supported official Node **26.5.0** runtime was restored using mise without
changing security settings or runtime version. Its restored executable SHA-256 is
`119d6fa70e6ae1b15b90688ab6bcc8e3a2819acea021af196895cab1843645af`.
An original executable digest was not captured: recorded version and absolute worker
launch paths are evidence of the original version/path, not byte-identical executable
attestation.

One recovery preflight incorrectly required identical package-probe arrays across
different projects. Legitimate duplicate inherited ruleset probes violated that
assumption; **no workers executed** in that rejected attempt. The corrected recovery
checks each entrypoint's version/hash and installed archive payload, preserving
duplicate probes. It retained the 433 original receipt bytes, reproduced two semantic
smokes and ran only the remaining **54** projects.

The pinned official `buildNativeCoverageReport` finalized the complete recovered
population after all **93,496 dataset files** passed inventory and SHA-256 validation.
This is a recovered full-population measurement, **not a clean original CLI exit**.
The marker mapping then completed as an ordinary uninterrupted full CLI run.

[Consistency manifest](runs/20261105-3b0603ab8-resource-consistency/manifest.json),
[consistency coverage](runs/20261105-3b0603ab8-resource-consistency/coverage.json),
[marker manifest](runs/20261105-3b0603ab8-put-resource-marker/manifest.json),
[marker coverage](runs/20261105-3b0603ab8-put-resource-marker/coverage.json).
Original/rejected attempts, successful recovery, worker completion, dataset
verification and complete logs are preserved by [the immutable asset](native-asset.json).

## Exact correspondence and accounting

All 433 Swagger findings resolve to 277 member checks. Identity retains
`(member, project, resolved document, exact route, compared schema context)`;
different members and different comparisons at one location are never deduplicated.
Reported/input documents and fallback attribution remain unchanged.

Each final mapping has its own affected-union metadata pass, with the original
selected rule/configuration and exact saved-diagnostic reproduction. Overlapping
source/selected-version graphs must agree before findings are combined into the
inventory. HTTP metadata diagnostics must remain empty.
[Execution and graph-compaction receipt](receipts/instance-inspection-20261105.json).

Attribution checks the diagnostic family, actual status/body, effective model,
canonical resource and exact source/selected-version correspondence. Response
polymorphism and list-item rules remain distinct from request identity. Wrong-parent
warnings and collection wrappers containing the same resource item are not credited
as different-resource cross-method comparisons. Marker attribution independently
requires matching selected status/body and absence of the emitted resource marker.
Route/message co-occurrence alone is never coverage.

Existing-owner visitor callbacks are actually captured, not inferred from source
ownership. Callback `reportIndex` preserves distinct reports at one location.
A callback may cover several original member contexts; a context covered by both
ARM and Azure Core is counted once in the covered union.
[Coverage accounting](gap-assessment.json), [owner probes](gap-probes.json),
[exact comparison inventory](instance-correspondence.md),
[source/selected metadata](instance-inputs.json),
[Swagger bindings](swagger-bindings.json),
[TypeSpec-to-Swagger bindings](native-swagger-bindings.json).

Every one-sided project and every additional TypeSpec diagnostic has an individual
source/status/canonical disposition. [Directional/project differences](project-differences.md)
retain opposing excesses, absolute/relative differences and independent mapping
project sets. [Raw diagnostic inventory](diagnostic-inventory.md) preserves all
selected findings. Location summaries and project overlap are not functional
coverage percentages. Exact checked subsets are assessed; universal equivalent
violation totals remain unassessed.

## Production policies and controls

The resource-driven rule enumerates registered operation aliases, rather than
globally inferring resources from every PUT. Requests use effective payload identity;
responses inspect actual HTTP success bodies and allow discriminated ancestry.
Raw arrays and ordinary `value` envelopes are interpreted per response for **list**
associations, not arbitrary read/command associations. Absent and explicit-void bodies
do not create response-resource mismatches.

The dedicated marker rule checks PUT 200, falling back to body-bearing 201, and
honors inherited resource metadata and explicit extension overrides. It does not
silently convert custom command payloads into canonical resources.

All **923 tests in 88 files** passed, together with the affected package closure
build, type-aware lint, formatting, spelling, changeset/whitespace checks and compiled
documentation examples. **34 selected injected controls** verify the final packed
implementation, including marker status precedence/fallback/void/inheritance,
registered aliases, plain response mismatch, independent request/response behavior,
list arrays/envelopes, compliance, multipart, explicit configuration disablement,
default activation and authored suppression.
[Exact control results](receipts/injected-controls-3b0603.json).

**37 portable harness controls passed**; six fixtures requiring an unrelated
resource-group-rule migration were explicitly non-applicable, not passes or silent
skips. The complete frozen population was not reduced.
[Selection and commands](receipts/final-plan-3b0603.json).
Source/build/payload lineage for all 15 archives is retained in
[artifact provenance](receipts/artifact-provenance-3b0603.json).
Source examples and retained emitted snippets are under
[Code-backed representatives](gap-analysis.md#code-backed-representatives).

## Validation and CI

The successful frozen assessment is not a green PR CI claim. The separate moving
external-specs check assessed **605** projects: **193 passed, 412 failed**. Its log
contains 845 `arm-common-types-version` diagnostics and 270
`arm-resource-operation-response` diagnostics, including 73 RPC008 response-family
findings. These are a different corpus and include existing dependency-policy
failures and newly detected canonical-contract issues.
[Extracted diagnostics](receipts/ci-rest-api-specs-3b0603.json).

An AppService function-secret command returns KeyInfo while its legacy registration
names FunctionEnvelope; a VnetRoute read returns an array; a security scan-result
read is associated with its settings resource. These are concrete association/role
differences, not evidence that arbitrary read results should be treated as list
operations. They require owner/spec triage; valid warnings were not disabled,
silently suppressed or reclassified as passes. No universal classification of all
moving-CI warnings as service defects is claimed.

[Draft spec PR #47952](https://github.com/Azure/azure-rest-api-specs/pull/47952)
adds exactly three missing create/update registrations. Five all-version OpenAPI
outputs are byte-identical; ten public TCGC outputs differ only in the source-version
fingerprint. Full SDK generation was not performed, and omitted internal `__raw`
prevents claiming specialized ARM SDK neutrality. These modified specs were never
used or credited in the frozen comparison.
[Compatibility receipt](receipts/spec-followup-compatibility-20261105.json).

## Read, recount and regenerate

The stable branch report links to [native-asset.json](native-asset.json), whose
immutable release asset preserves exact archives, raw run/input receipts, full
metadata graphs, controls, recovery attempts and publication scripts. Its internal
index records original and published hashes; machine/user paths are sanitized in
text, never inside package archives.

The shared frozen Swagger baseline remains independently available from the
[pinned descriptor commit](https://github.com/msyyc/typespec-azure/tree/1c9d2b0e6a596754af1aa793b1906ff3c4ef2bd6)
with identity
`aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`.
The matching
[staging descriptor](https://github.com/msyyc/typespec-azure/tree/feec4bab366c373380fbe1b5528faa12e7233cfe)
has identity
`e0a2c22b857b13fa8ccf318bff1c8a6beaf367e1a1210cbc71cf7161fd86d482`.
The [retained frozen specs](https://github.com/msyyc/azure-rest-api-specs/tree/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9)
are separate from authored follow-up changes.

From this report directory, saved-input verification requires no compilation:

```powershell
python -B analyze-instances.py --root . --output instance-mapping.json
python -B assess-gaps.py --verify
python -B -m unittest test_instance_analysis.py test_reanalyze.py
python -B reanalyze.py --verify-inventory
python -B render-instances.py --verify
```

Independent remote recovery verifies the downloaded asset checksum/index,
reconstructs the published saved observations/graphs and repeats attribution,
owning-diagnostic accounting and directional recount. It is **saved-input recovery
and reanalysis, not a new whole-corpus execution**.

To fully rerun, recover and verify both pinned baseline descriptors/assets and
frozen specs, the tooling SHA, final candidate/core source and 15 package archives.
Use specs pnpm **12.6.0**, Node **26.5.0**, Python **3.13.17** (the final analysis runtime) and the recorded registry;
do not install arbitrary latest libraries or regenerate Swagger. Run the official
`native-coverage.ts` once for the three consistency members and once for the marker
member, each with its single mapped rule, a new empty output directory,
`--baseline-run`, `--baseline-policy frozen-reference`, `--scope source`, no filter/limit,
and the pinned staging supplement where needed. Keep writable specs injection serial.
Exact selectors, artifact inventory, launcher/runtime policy, source identities and
control selections are in [the plan](receipts/final-plan-3b0603.json); the immutable
asset retains the original commands, original worker inputs and finishing scripts.
Restore sanitized path tokens to explicit verified local roots before using those
orchestration scripts. Retain all failed attempts rather than overwriting them.

Re-run per-mapping metadata inspection with unchanged selectors; require exact
saved-diagnostic equality before merging graphs and resolving saved Swagger targets.
The committed resolver/analyzer/probe/assessment/recount/renderer scripts reconstruct
the current evidence from those inputs. Full regeneration was not repeated for
publication. Runtime identities and package hashes alone do not prove complete
transitive dependency locking.
