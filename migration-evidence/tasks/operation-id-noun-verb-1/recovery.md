# Recovery and replay

## Status

This directory records published and independently recovered cycle0-3 evidence. Historical
evidence commit `d467753cc057c8320d768ca59660709baae70963` and release
`lint-migration-operation-id-noun-verb-cycle0-1` remain immutable and
independently recovered. Native C2
`54cc4d9ddb386ee4d7ce1f09d25ea13963d6150a` now publishes exact tree T3.
Evidence E2 `3ad00cb9872c586bf9fe11c9c848ee3ccf8ec5d7`, release
`lint-migration-operation-id-noun-verb-cycle0-3`, mixed-release download
recovery, checkpoint A2 and checkpoint B are complete. Closing metadata E3
remains unpublished. All C2 checks completed. ExternalIntegration
completed 211 passed and 394 failed of 605; all failures are classified as the
unrelated ARM common-types-version v6 versus v5 requirement, with no target
naming-rule mentions. This is a disclosed non-green limitation, not
matching-base proof. PackageSize separately failed on an unrelated Maven
Central HTTP 429.

## Recover immutable inputs

- Candidate snapshot: `79a4247adc0e09e1c2b0f5e411b53410780d5f41`, tree `56f36f10a9c0f8c189796833dc3d79de213beee9`, parents `ac8c02e7bb5564a0cd49b1a831a13947f9916b2c` and `471dffac285f90e0bf892ac80a37a0a21cf8879b`.
- Published native source: fetch C2 `54cc4d9ddb386ee4d7ce1f09d25ea13963d6150a`
  from `Azure/typespec-azure:native/operation-id-noun-verb`; its tree is exactly
  T3. S3 is the tested local snapshot and is not claimed as a GitHub recovery
  ref.
- Core gitlink: `a43d2ca6f2ddd4c1a1d05f2e63cd4c8a40a71b76`.
- Frozen specs: `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`.
- Tooling: `662e7f405fda22e1d9c8c9c1d7664d171f80b60d`.
- Shared baseline metadata commit: `1c9d2b0e6a596754af1aa793b1906ff3c4ef2bd6`.
- Shared baseline identity: `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`.
- Shared baseline asset: `swagger-arm-20261026-2cd3c5dd.tar.gz`,
  SHA-256 `0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0`.

The baseline is separate and sealed. `native-run-results-3.tar.gz` excludes
`baseline.json` and `dataset/**`; never use it as a reusable Swagger baseline.

## Recover the mixed-release task assets

Download the two published cycle0-3 assets from release
`lint-migration-operation-id-noun-verb-cycle0-3` (release ID `434755280`,
target E2):

1. [candidate-packages-3.tar.gz](https://github.com/msyyc/typespec-azure/releases/download/lint-migration-operation-id-noun-verb-cycle0-3/candidate-packages-3.tar.gz),
   asset ID `711938908`, SHA-256
   `990ad34e590fe6c692e794c5129381e0348186b72ee01bb315d053c1cd34aa63`.
2. [native-run-results-3.tar.gz](https://github.com/msyyc/typespec-azure/releases/download/lint-migration-operation-id-noun-verb-cycle0-3/native-run-results-3.tar.gz),
   asset ID `711938907`, SHA-256
   `351ba6c2d2e78ccc47ab0dfc5a4d608680970575793e2a2d60c9656ffc2d3cfe`.

Reuse these exact already-published release1 tooling assets:

3. [comparison-tooling-inputs-1.tar.gz](https://github.com/msyyc/typespec-azure/releases/download/lint-migration-operation-id-noun-verb-cycle0-1/comparison-tooling-inputs-1.tar.gz),
   SHA-256 `d11c91d1118094561575d54fa39c4c3d6d100e6f6a7d8d6096d6babdcfddfd73`.
4. [comparison-tooling-inventory-1.json.gz](https://github.com/msyyc/typespec-azure/releases/download/lint-migration-operation-id-noun-verb-cycle0-1/comparison-tooling-inventory-1.json.gz),
   SHA-256 `852f4e2ffba8882bd65481c9deb4a5795375fe45d1e73daae3360e6767e75d04`.

Do not imply all four assets belong to release3. Run `verify-assets.py` with the
four explicit downloaded paths. It verifies all outer identities and every
embedded member without extracting them.

The completed fresh recovery verified 113 E2 task members, 15 candidate
packages, 1,488 run members and 79,756 tooling members. It also verified
C2/T3/core-a43, frozen specs `2cd3c5dd`, the descriptor, helper and all 93,496
sealed baseline dataset files. Dependency-free saved reanalysis reproduced
487/487 selected and assessable projects, 265 Swagger diagnostics and 123
native diagnostics. Neither linter ran, and Swagger was not regenerated.

## Reanalyze saved observations

Run `node .\reanalyze.mjs` with Node 26.5.0. The dependency-free helper checks
all 487 selected receipts and regenerates the count tuple from
`project-inventory.json`, `swagger-findings.json` and `native-results.json`.
It does not execute either linter or decide functional equivalence.

The fresh run3 diagnostics exactly reproduce the accepted saved native tuple.
The six correspondence groups, examples and bridges therefore remain applicable.
Network's 143 input-fallback observations retain their attribution limitation;
count equality or repeated paths do not restore callback provenance.

## Fully rerun native coverage

Recover the exact candidate/core/specs/tooling identities and all 15 candidate
archives. Use Node 26.5.0, pnpm 12.6.0 on child `PATH`,
`PNPM_CONFIG_VERIFY_DEPS_BEFORE_RUN=false` and the approved
`PNPM_CONFIG_REGISTRY`. Run the analyzer from tooling
`packages\typespec-lintdiff` with the exact command saved in
`native-run-results-3.tar.gz:support/full-native-coverage-command-3.txt`.

The supported policy is full population, `scope=source`, `concurrency=2`,
`baseline-policy=frozen-reference`, `native-mode=target-only`, no filter/limit,
no Swagger generation and a 7200-second native budget. Use a new empty output
directory and a separately writable specs runtime. Preserve failures as
unassessed; do not promise identical future counts without a captured rerun.

Restore exact seven installed-control source/config bytes from
`control-source-originals.json` for byte-exact control replay. Six unrelated
resource-group portable fixtures remain predeclared nonapplicable skips, not
passes.
