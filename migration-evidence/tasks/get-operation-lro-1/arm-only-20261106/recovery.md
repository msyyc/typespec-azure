# Recovering the ARM-only comparison

The fresh run, operation comparison and runtime verification passed. Download verification and publication identities are recorded separately in `publication-verification.json`.

## Frozen identities

| Input                                        | Commit                                     |
| -------------------------------------------- | ------------------------------------------ |
| Azure/typespec-azure candidate               | `75b9be3c28af0f36763b9511f25c193bde11675d` |
| Candidate Core gitlink                       | `3a87c089009146e1ce1201659c00f1179411a81f` |
| Azure/typespec-azure tooling                 | `402e3fb202e9a16f0a8c7dfc1b799098cfba879d` |
| Frozen specs source                          | `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9` |
| msyyc/azure-rest-api-specs baseline metadata | `1c9d2b0e6a596754af1aa793b1906ff3c4ef2bd6` |

Recover the candidate from its organization repository and initialize its exact Core gitlink. Recover the tooling at its recorded commit. The frozen specs are preserved at `msyyc/azure-rest-api-specs:evidence/long-running-operations-options-validator-20261022-source`; verify the source SHA rather than using a metadata commit or moving branch.

## Download and verify saved inputs

Use [baseline-descriptor.json](baseline-descriptor.json) and the tooling `shared_baseline.py` fetch helper to download, verify and extract the shared Swagger archive into a new directory. Its repository is `msyyc/azure-rest-api-specs`, release `swagger-lint-baseline-20261026-2cd3c5dd`, asset `swagger-arm-20261026-2cd3c5dd.tar.gz`: **51,932,501 bytes**, SHA-256 `0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0`. Baseline identity: `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`. Never regenerate Swagger as missing-cache recovery.

Download the exact three assets in [assets.json](assets.json) from `msyyc/typespec-azure`, release `lintdiff-get-operation-lro-arm-only-20261106`. Verify each byte count and SHA-256 before extracting into new directories.

The packages archive contains the complete 15-package runtime closure, its source audit and build/pack logs. The native archive contains all fresh worker results/requests and coverage/installation receipts, but not the separately retained shared Swagger dataset. The controls archive preserves literal fixtures, output receipts, scripts and focused test results.

Published text replaces absolute machine roots with role tokens and uses UTF-8/LF. Tarballs and the sealed baseline are unchanged. Each archive has a `publication-mapping.json` with original and published hashes. Hash verification, saved-observation replay and fresh compilation are separate operations.

Run `python replay.py` beside the compact receipts to audit the saved 487-project population, 4/8 counts and correspondence. This does not execute the TypeSpec linter.

## Fully rerun the frozen comparison

1. Prepare clean, exclusive candidate/specs checkouts at the exact SHAs above. Use the recorded toolchains; native execution used Node `v26.13.0`, and the specs package manager is pnpm `12.6.0`.
2. Recover the complete tarball set, or build the candidate AutoRest/rulesets/integration-tester dependency closures, then pack the six Azure and nine Core packages listed in `manifest.json`. Pack Azure and Core under their respective Chronus configurations, repeating `--only` for each package. Run `audit-artifacts.py CANDIDATE ARTIFACTS NEW_AUDIT_JSON`.
3. Acquire the shared machine/user `corpus.lock` atomically and exclusively. Hold it through injection, controls, coverage, inspection and all children. Do not bypass another owner.
4. From the candidate, run its `tsp-integration azure-specs` command with only `--stage patch --stage install`, `--repo SPECS` and `--tgz-dir ARTIFACTS`. Do not invoke the checkout stage.
5. From tooling, set `NATIVE_COVERAGE_SPECS_REPO` to the runtime and run the portable `native-coverage-worker.test.ts` suite, excluding only the six foreign `evaluates injected resource-group rule` fixtures. Run `current-injected-controls.mjs SPECS TOOLING NEW_CONTROLS --arm-only`. The Legacy fixtures intentionally expect no target diagnostic.
6. From `TOOLING\packages\typespec-lintdiff`, execute the following command using fresh output directories and no filter or limit:

```powershell
mise exec pnpm@12.6.0 -- node --import tsx/esm test\harness\native-coverage.ts `
  --candidate-repo CANDIDATE --specs-repo SPECS --tgz-dir ARTIFACTS `
  --validator-rule GetOperationMustNotBeLongRunning `
  --tsp-rule @azure-tools/typespec-azure-resource-manager/no-get-lro `
  --scope source --native-mode target-only `
  --baseline-run BASELINE --baseline-policy frozen-reference `
  --native-budget-seconds 7200 --concurrency 2 --output NEW_RUN
```

7. Run `inspect-findings.mjs SPECS TOOLING NEW_RUN NEW_INSPECTION OLD_FINDINGS`, where `OLD_FINDINGS` is the historical `review-http-20261104/findings.json`. This recomputes metadata and saved Swagger correspondence for retained findings and intentionally retired Legacy-only operations. A removed diagnostic's selected-version graph field is `null`, not a claim that the operation disappeared.
8. Reconcile all operation identities, diagnostics, metadata, source locations, selected-version memberships and saved Swagger attribution. Verify injected entrypoints/rule files against source-audited tarballs. In particular, the SDK package must contain neither the removed rule nor its registration. Do not accept equal totals as semantic proof.
9. Refresh all four sections and NOTES of `migration.md` from the run, semantic controls and operation-level dispositions. Preserve the accepted narrower Legacy policy explicitly. The report is reviewed policy analysis, not a conclusion automatically certified by count replay.

The published run executed the full frozen population once. Subsequent publication download/hash/member checks and saved-data replay are recovery checks, not a second full corpus execution.
