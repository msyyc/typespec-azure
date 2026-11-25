# Recover the frozen Legacy-marker assessment

## Roles and immutable inputs

The evidence branch is not the candidate source checkout. Recover these separate roles:

| Role           | Repository / revision                                                            |
| -------------- | -------------------------------------------------------------------------------- |
| Candidate      | `Azure/typespec-azure`, `65c1ca5e24d9bc72d768f4c5d3e437507b0764b9`               |
| Core submodule | `microsoft/typespec`, `a1664df866494abea6d51767c60ea9b627903abd`                 |
| Tooling        | `msyyc/typespec-azure`, `702ac1601ec62a1273872d4a12e6fd05b9ebda60`               |
| Specs          | `msyyc/azure-rest-api-specs`, `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`         |
| Evidence       | `msyyc/typespec-azure`, branch `evidence/get-operation-must-not-be-long-running` |

Specs are retained at `evidence/long-running-operations-options-validator-20261022-source`; its head was independently verified as the exact frozen commit. Tooling commit accessibility was verified in the fork. Later candidate commit `50dace214e7de8473c75d441db71eced78ccb15a` changes only the release note, not the tested lint or artifacts.

Baseline discovery metadata is `msyyc/azure-rest-api-specs@2c35e1f6a7139768b03234983ad201d8fefa4d0b`, descriptor `.lintdiff-baselines/swagger-arm-20261026-2cd3c5dd/baseline.json`. The historical 487-project population was explicitly retained rather than replaced by the newer monthly descriptor.

The [baseline descriptor](baseline-descriptor.json) identifies the unchanged asset:

```text
Repository: msyyc/azure-rest-api-specs
Release: swagger-lint-baseline-20261026-2cd3c5dd
Asset: swagger-arm-20261026-2cd3c5dd.tar.gz
Bytes: 51932501
SHA256: 0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0
Identity: aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995
```

Use the supported shared-baseline helper at the pinned tooling revision to download and verify the descriptor/archive, all inventory and validation shards. The successful receipt is archived; Swagger generation was **not run**. Do not regenerate Swagger or silently use a moving source/version population.

## Published assets and byte verification

[assets.json](assets.json) lists three immutable archives on release `lintdiff-get-operation-lro-legacy-marker-20261125` in `msyyc/typespec-azure`.

```powershell
gh release download lintdiff-get-operation-lro-legacy-marker-20261125 `
  --repo msyyc/typespec-azure --dir C:\recovery\downloads
```

Verify each declared asset's SHA-256 and byte length before reading it. Each archive's `publication-mapping.json` enumerates every ordinary member's original and published SHA-256. Require exact member sets and verify every published member. Text replaces known machine roots/private session identity/registry address with role tokens and uses UTF-8/LF; **all twenty original tarballs are byte-identical**, and the independently retained Swagger asset is unchanged.

The packages archive contains the complete source-audited 20-package runtime closure and build/pack/audit evidence. The observations archive contains all 487 worker results, raw coverage and execution/provenance files. The controls archive contains all public fixtures, validation/inspection receipts, helpers and preserved failed preparation outputs.

## Saved-observation replay

```powershell
python C:\recovery\evidence\replay.py `
  --evidence-dir C:\recovery\evidence `
  --native-archive C:\recovery\downloads\get-operation-lro-legacy-marker-20261125-native.tar.gz
```

This independently regroups project counts and checks all 487 downloaded successful worker receipts against the compact inventory, four restored exact matches, eight retired targets, directional differences and source identities. It **does not compile TypeSpec**, regenerate Swagger, capture all suppressed diagnostics or decide semantic equivalence.

## Fresh TypeSpec reproduction

Use Node `26.5.0`, candidate/Core pnpm `11.10.0`, and specs pnpm `12.6.0` as recorded in the execution manifest. Preserve local/global configuration; use an authorized registry only in the process environment if required. The frozen workspace's required `next` overrides are supplied by the 20 pinned tarballs, not resolved from an unavailable moving tag.

1. Recover clean, exclusively owned candidate/Core, tooling and frozen specs checkouts; restore the verified sealed baseline and original package tarballs.
2. Replace role tokens in archived coordinator/verification helpers with those local roles. Do not reuse an old private session identity. Acquire the shared cooperating-session machine corpus lock exclusively before injection, controls and full compilation.
3. Inject the packed candidate/Core closure using the archived `tsp-integration` patch/install command. Verify restored clean specs source and payload hashes. Run the 37 applicable portable controls and all 50 selected controls; the six foreign resource-group fixtures are explicitly inapplicable.
4. Run `test\harness\native-coverage.ts` from the pinned tooling package with specs pnpm `12.6.0` on PATH: `--validator-rule GetOperationMustNotBeLongRunning --tsp-rule @azure-tools/typespec-client-generator-core/no-get-lro --scope source --native-mode target-only --baseline-policy frozen-reference --native-budget-seconds 7200 --concurrency 2`, passing candidate/specs/tarball/baseline/output roles. Use no filter or limit and a fresh output directory.
5. Inspect exact operation correspondence with the archived helper and validate every worker/package entrypoint against the source-audited payloads. Retain failed/unassessed projects and every unexpected difference; do not force a 4/4 result or equate equality with complete semantics.

This is a fresh final-source TypeSpec comparison against saved Swagger. API-version membership is an additional bounded HTTP-graph inspection, not a claim that all source diagnostics were generated from a selected-version projected program. Full-population default activation is unassessed in target-only mode; separate controls prove the selected presets.

## Limits and historical material

The worker does not collect suppressed diagnostics. The four observed matches are unsuppressed, while exhaustive suppression-inclusive totals for other owning checks remain unassessed. Raw-extension-only GETs remain outside this predicate; native-only enforcement is not implemented.

The source changeset-only follow-up, full-suite timeout retry, dependency recovery and control-driver repairs are explicitly distinguished in [assessment](assessment.json), [validation](validation.json) and [analysis](analysis.md). Original joint and ARM-only directories remain historical. No CI outcome is inferred from the archived local validation.
