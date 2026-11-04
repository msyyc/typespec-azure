# GET LRO review finding 01: recovery

<!-- cspell:ignore msyyc -->

## Frozen inputs

| Role                                            | Identity                                   |
| ----------------------------------------------- | ------------------------------------------ |
| Candidate, `Azure/typespec-azure`               | `a78104288669f33aa23ac2f78c7c0410dc312040` |
| Candidate Core gitlink                          | `05b9bad7c57b9b58e8fb5390f9bab081a1a9ac31` |
| Tooling, `Azure/typespec-azure`                 | `662e7f405fda22e1d9c8c9c1d7664d171f80b60d` |
| Frozen specs                                    | `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9` |
| Baseline metadata, `msyyc/azure-rest-api-specs` | `1c9d2b0e6a596754af1aa793b1906ff3c4ef2bd6` |

The specs preservation branch
`msyyc/azure-rest-api-specs:evidence/long-running-operations-options-validator-20261022-source`
was reverified at the exact frozen SHA. Neither the metadata commit nor a moving
`typespec-next` branch is the tested source.

The [descriptor](baseline-descriptor.json) identifies the separate shared release
`msyyc/azure-rest-api-specs:swagger-lint-baseline-20261026-2cd3c5dd`, asset
`swagger-arm-20261026-2cd3c5dd.tar.gz`, SHA-256
`0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0`,
51,932,501 bytes. The sealed baseline identity is
`aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`.
Completion, all 93,496 retained file hashes, full project inventory and validator
shards were verified. The analyzer independently verified reuse/final integrity.
No Swagger generation or Swagger validator execution occurred.

## Download saved observations

Download the three exact [assets](assets.json) from
[the dedicated release](https://github.com/msyyc/typespec-azure/releases/tag/lintdiff-get-operation-lro-fix01-20261104):

```powershell
gh release download lintdiff-get-operation-lro-fix01-20261104 `
  --repo msyyc/typespec-azure --dir C:\work\download
```

Verify every asset's byte count and SHA-256 before extraction into new directories.
The packages archive contains fifteen tarballs, the 2,855-file source audit and
successful build/pack logs. The native archive contains all 487 fresh worker
receipts, requests, coverage, installation receipts and logs, but excludes the
separately preserved Swagger dataset. The controls archive contains current
scripts, operation evidence, 37 portable passes, 34 selected controls and focused
validation logs. Six foreign resource-group fixtures are not applicable.

Each archive includes original-to-published SHA-256 mappings. Absolute machine
roots are replaced with role tokens in text copies; raw local observations,
tarballs and sealed baseline content are unchanged. Compact Git copies may also
be formatted with the repository's equivalent Prettier configuration; their
actual blob hashes are recorded separately in `publication.json`.

Run the adjacent `replay.py` to audit the saved compact observations. This does
not compile specs, reexecute validators or establish semantic equivalence.
Publication verification records the fresh download/hash round trip separately.

## Rerun native compilation

Use the exact candidate and tooling commits above, initialize the candidate's
Core submodule at its gitlink and use their pinned mise tools. Recover the exact
published tarballs, or rebuild the recorded 23-package closure and pack the six
Azure and nine Core packages listed in the [manifest](manifest.json).
The portable `audit-artifacts.py` in the packages archive accepts
`CANDIDATE ARTIFACTS NEW_OUTPUT_JSON` and verifies the complete runtime closure.
Install prerequisites only if missing.

Prepare a clean, exclusive specs runtime at the frozen source SHA. Fetch and
verify the descriptor-bound shared baseline with the tooling's
`shared_baseline.py fetch`. Do not regenerate Swagger for cache recovery.
Preserve the approved registry using pnpm 12's `PNPM_CONFIG_REGISTRY`.

Acquire the shared machine/user corpus gate
`$env:LOCALAPPDATA\Copilot\lint-migration\corpus.lock` atomically and exclusively.
Hold it through injection, the entire run and all child processes; never bypass
an active owner. From the candidate, run its integration CLI with suite
`azure-specs`, `--stage patch --stage install`, `--repo` and `--tgz-dir`.
Do not invoke the checkout stage.

Run the tooling's portable worker controls with
`NATIVE_COVERAGE_SPECS_REPO` set and test selection
`^(?!.*evaluates injected resource-group rule)`: 37 applicable passes, six
explicitly inapplicable foreign fixtures. Run
`current-injected-controls.mjs SPECS TOOLING NEW_CONTROL_OUTPUT` from the controls
archive for all 34 selected-policy checks.

From `TOOLING\packages\typespec-lintdiff`, replacing the example paths:

```powershell
mise exec pnpm@12.6.0 -- node --import tsx/esm test\harness\native-coverage.ts `
  --candidate-repo C:\work\candidate `
  --specs-repo C:\work\specs `
  --tgz-dir C:\work\artifacts `
  --validator-rule GetOperationMustNotBeLongRunning `
  --tsp-rule "@azure-tools/typespec-azure-resource-manager/no-get-lro" `
  --tsp-rule "@azure-tools/typespec-client-generator-core/no-get-lro" `
  --scope source --native-mode target-only `
  --baseline-run C:\work\baseline --baseline-policy frozen-reference `
  --native-budget-seconds 7200 --concurrency 2 `
  --output C:\work\new-native-run
```

Use a new empty output directory, no filter and no limit. This reruns native
compilation for all 487 projects while retaining historical Swagger observations.
The original run used `--candidate-working-tree true` on the recorded base and
diff; [runtime verification](runtime-verification.json) proves that the published
commit has those exact tested source bytes. A clean replay at that commit does
not need the working-tree option.

Run `inspect-findings.mjs SPECS TOOLING NEW_NATIVE_RUN NEW_INSPECTION` from the
controls archive. Compare all diagnostic codes/messages/authored targets,
operation metadata, selected-version HTTP membership and saved Swagger
attribution with [findings.json](findings.json), not totals alone. The current
[comparison](identity-comparison.json) has twelve unchanged identities and no
additions/removals relative to the preceding native evidence.

The checked-in report is reviewed analysis, not a conclusion automatically
certified by `replay.py`. Recovering saved observations, replaying their counts
and actually rerunning the frozen comparison are three different operations.
