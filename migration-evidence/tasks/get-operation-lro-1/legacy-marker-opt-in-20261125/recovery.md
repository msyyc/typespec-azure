# Recover the frozen client-SDK opt-in assessment

## Separate roles

| Role               | Repository / revision                                                            |
| ------------------ | -------------------------------------------------------------------------------- |
| Assessed candidate | `Azure/typespec-azure`, `c67b521bc0166f11f492afb3366da29793ebbac9`               |
| Core submodule     | `microsoft/typespec`, `123e997958ced3b632caa0a4486e306d1487ca82`                 |
| Tooling            | `msyyc/typespec-azure`, `702ac1601ec62a1273872d4a12e6fd05b9ebda60`               |
| Specs              | `msyyc/azure-rest-api-specs`, `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`         |
| Evidence           | `msyyc/typespec-azure`, branch `evidence/get-operation-must-not-be-long-running` |

The evidence branch is not the source candidate. Published source `4c1a337a01268c504b28508efaf4e0b4a7f29190` subsequently merges only nine unrelated documentation-agent/spelling files. All twenty assessed tarballs and 3,341 payload files also match that later head; the corpus remains attributed to `c67b521`.

Frozen specs are retained at `evidence/long-running-operations-options-validator-20261022-source`. Baseline discovery metadata is `msyyc/azure-rest-api-specs@2c35e1f6a7139768b03234983ad201d8fefa4d0b`, descriptor `.lintdiff-baselines/swagger-arm-20261026-2cd3c5dd/baseline.json`.

## Unchanged Swagger baseline

[baseline-descriptor.json](baseline-descriptor.json) identifies:

```text
Repository: msyyc/azure-rest-api-specs
Release: swagger-lint-baseline-20261026-2cd3c5dd
Asset: swagger-arm-20261026-2cd3c5dd.tar.gz
Bytes: 51932501
SHA256: 0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0
Identity: aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995
```

Recover and verify it with the pinned tooling's supported shared-baseline helper, including all inventory/shards. The historical 487-project population is intentionally preserved. No Swagger regeneration or silent population replacement.

## Published assets

[assets.json](assets.json) lists three checksummed archives on `msyyc/typespec-azure` release `lintdiff-get-operation-lro-legacy-marker-opt-in-20261125`.

```powershell
gh release download lintdiff-get-operation-lro-legacy-marker-opt-in-20261125 `
  --repo msyyc/typespec-azure --dir C:\recovery\downloads
```

Verify each asset's byte length and SHA-256, exact member set and every `publication-mapping.json` member hash. Text sanitizes known machine/session/registry roots to roles and UTF-8/LF. All twenty tarballs are byte-identical to the assessed originals. The separately sealed Swagger baseline is unchanged.

The packages archive retains source audits, later-head applicability audit, builds and packing evidence. The observations archive retains all 487 worker receipts and raw comparison metadata. The controls archive retains public fixtures, local checks, inspection and reproduction helpers. The unrelated Python-hook TLS failure and successful filtered TypeSpec restore are retained rather than counted as an unrestricted all-workspace installation success.

## Saved-observation replay

```powershell
python C:\recovery\evidence\replay.py `
  --evidence-dir C:\recovery\evidence `
  --native-archive C:\recovery\downloads\get-operation-lro-legacy-marker-opt-in-20261125-native.tar.gz
```

Replay independently regroups all 487 successful receipts and verifies scoped totals, four matched targets and eight historical absent targets. It does not compile TypeSpec, regenerate Swagger, capture suppressed callbacks or decide equivalence.

## Fresh TypeSpec reproduction

Use recorded Node `26.5.0`, candidate/Core pnpm `11.10.0` and specs pnpm `12.6.0`. Keep registry/tool configuration process-local.

1. Recover clean, exclusively owned candidate/Core, tooling and frozen specs; restore the verified baseline and twenty original tarballs.
2. Substitute local roles into archived helpers. Pass the assessed candidate explicitly to the coordinator's `-CandidateRevision`; do not reuse a private session ID or a historical portable-control receipt.
3. Acquire the shared cooperating-session machine corpus lock before injection, controls and compilation. Inject the exact candidate/Core packages with the archived `tsp-integration` patch/install command; verify clean restored specs source and payload hashes.
4. Run all 37 applicable portable controls and 50 selected executions; six unrelated resource-group fixtures are excluded upfront. Client-SDK defaults must remain inactive, while explicit target enablement and SDK `all` activate the rule.
5. Run pinned `test\harness\native-coverage.ts` with candidate/specs/tarballs/baseline/output roles, `--validator-rule GetOperationMustNotBeLongRunning --tsp-rule @azure-tools/typespec-client-generator-core/no-get-lro --scope source --native-mode target-only --baseline-policy frozen-reference --native-budget-seconds 7200 --concurrency 2`. No filter/limit; use a fresh output.
6. Inspect exact source/HTTP/saved-Swagger correspondence and every worker entrypoint against the audited closure. Preserve all failed/unassessed projects and unexpected differences.

The full run explicitly enables the rule; full-population default activation is unassessed. Selected-version HTTP membership is a separate bounded inspection, not a claim that the source run is version-projected.

## Limits and validation

The worker honors suppressions without capturing suppressed diagnostics. Four observed matches are unsuppressed; exhaustive substitute/suppression-inclusive coverage remains unassessed. Raw-only LRO extensions are missing from this predicate; GET LRO metadata without a Legacy marker is outside the selected check.

[validation.json](validation.json) records 2,074 SDK passes/two skips, 22 ruleset passes, 24 builds, root lint/format/spelling, regeneration, Chronus, whitespace and three exact published examples. Root build/test/regeneration skips have separate supplements. The later head passed its own PR validation and unchanged-payload audit. CI remains separate.
