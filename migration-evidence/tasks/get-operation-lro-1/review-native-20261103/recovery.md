# Current native-only GET LRO evidence and recovery

<!-- cspell:ignore msyyc -->

## Immutable inputs

| Role                                            | Commit                                     |
| ----------------------------------------------- | ------------------------------------------ |
| Candidate, `Azure/typespec-azure`               | `8a1c96bef8aeb3edf01e3a54d3c484ff49a44fd8` |
| Candidate Core gitlink                          | `780c2c6a944d2f6be276b60f890854f7a18b2955` |
| Tooling, `Azure/typespec-azure`                 | `ec5e2c81c7fcb78e715313a34734e2590238cf94` |
| Frozen specs                                    | `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9` |
| Baseline metadata, `msyyc/azure-rest-api-specs` | `317e703b3e380d3b64e0dacb3a2c6fc0651de253` |

The specs preservation branch
`msyyc/azure-rest-api-specs:evidence/long-running-operations-options-validator-20261022-source`
was verified at the exact frozen SHA. Neither the metadata commit nor today's
`typespec-next` is the tested source.

The [descriptor](baseline-descriptor.json) identifies the shared Swagger release
`swagger-lint-baseline-20261026-2cd3c5dd`, asset
`swagger-arm-20261026-2cd3c5dd.tar.gz`, SHA-256
`0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0`,
51,932,501 bytes. The cached archive, sealed completion, all 93,496 retained file
hashes, full project inventory and validator shards were verified before reuse.
The full analyzer independently checked reuse and final integrity.

## Recover published results

The dedicated release is
[lintdiff-get-operation-lro-native-8a1c96be](https://github.com/msyyc/typespec-azure/releases/tag/lintdiff-get-operation-lro-native-8a1c96be).
Download the three exact assets listed in [assets.json](assets.json) with
`gh release download --repo msyyc/typespec-azure --pattern <asset>`.
Verify every byte count and SHA-256 before extraction into new directories.

The packages archive contains all seventeen tarballs, the 2,951-file source audit
and successful build/pack logs. The native archive contains all 487 worker
receipts, coverage and installation/runtime evidence, but excludes `dataset`.
Recover that dataset from the separate descriptor-bound shared Swagger asset.
The controls archive contains 37 portable passes, 34 current-policy controls and
fresh operation-level inspection. Six foreign resource-group controls are not
applicable because that unrelated rule is absent.

Published text copies replace machine-specific path prefixes with role tokens.
Each archive contains original-to-published SHA-256 mappings. Package tarballs
and sealed baseline content are not rewritten. Raw local observations remain
unchanged. [Publication verification](https://github.com/msyyc/typespec-azure/blob/evidence/get-operation-must-not-be-long-running/migration-evidence/tasks/get-operation-lro-1/review-native-20261103/publication.json) separately records the
upload/download hash round trip and count audit; it is not a second cold rebuild.

From the containing task directory:

```powershell
node .\review-native-20261103\replay.mjs
```

This audits saved observations. It does not compile specs or prove equivalence.

## Rerun the frozen comparison

Use the exact candidate and tooling commits above and initialize the candidate's
Core submodule at its gitlink. Use their pinned mise tools. Recover the exact
published tarballs, or rebuild the recorded 23-package closure and pack the six
Azure and eleven Core packages with repeated Chronus `--only` selectors.
The existing [artifact auditor](../split-20261102/audit-artifacts.py) checks this
closure. Install prerequisites only when missing.

Prepare a clean, exclusive specs runtime at the frozen source SHA. Recover the
shared baseline through the tooling's `shared_baseline.py fetch`, using the
selected descriptor and a new output directory. Never regenerate Swagger as
cache recovery. Preserve the approved registry with pnpm 12's
`PNPM_CONFIG_REGISTRY` setting.

Run the integration CLI from the candidate root with suite `azure-specs`,
`--stage patch --stage install`, `--repo` and `--tgz-dir`. Do not run its checkout
stage. Then run all applicable portable controls using
`NATIVE_COVERAGE_SPECS_REPO` and the selection documented in [run-plan.json](run-plan.json).
Run `injected-controls.mjs SPECS TOOLING NEW_CONTROL_OUTPUT` for current-policy
activation, compliance, scopes, suppression and raw-extension controls.

From `TOOLING\packages\typespec-lintdiff`, replacing these example directories:

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
compilation for all 487 projects while reusing saved Swagger observations.
Actual native execution took 27m24s; preparation and final integrity checks are
additional and can be substantial on this 93,496-file dataset.

Run the existing `inspect-findings.mjs SPECS TOOLING NEW_NATIVE_RUN NEW_INSPECTION`
from the sibling `split-20261102` folder. It checks every target against current
helpers, actual HTTP paths and selected-version membership.
Regenerate the four-section `migration.md` from the new coverage and inspection
receipts, preserving raw counts and every differing group. The prose is reviewed
analysis, not automatically certified by the count-audit script.
