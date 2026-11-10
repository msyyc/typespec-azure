# Recovery and replay contract

This draft describes the retained inputs and proposed publication. **Remote asset round-trip and fresh published-checkout recovery are not yet verified.** Local preparation is not durable publication. Those checks follow the retained reviewer's initial artifact/evidence acceptance and coordinator publication approval.

## 1. Read saved evidence

Retrieve the evidence branch `msyyc/typespec-azure:evidence/arm-common-types-latest-api-version`, then read the root `migration.md`, this directory's supporting notes, and the publication inventory. Verify the actual evidence commit and every declared asset's byte size and SHA-256. Do not treat a moving branch name alone as an immutable receipt.

The shared Swagger input is separately retained in:

- Metadata: `msyyc/azure-rest-api-specs:evidence/shared-swagger-baseline`, pinned commit `1c9d2b0e6a596754af1aa793b1906ff3c4ef2bd6`.
- Selected descriptor SHA-256: `ac511e7ff4b519619f30af811107b7f770a92a5bb56b199dfca983262dc8fd31`.
- Release: `swagger-lint-baseline-20261026-2cd3c5dd`; asset `swagger-arm-20261026-2cd3c5dd.tar.gz`, **51,932,501 bytes**, SHA-256 `0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0`.
- Baseline identity: `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`.

The descriptor's frozen specs source is **not** the metadata commit. Preserve all baseline `manifest.json`, `baseline.json`, and `dataset` files; the sealed inventory covers 93,496 dataset files. Reading compact results does not reconstruct that baseline.

The task archive can be verified and recovered using only Python's standard library:

```powershell
python .\verify-asset.py <downloaded-task-archive> .\asset-proposal.json .\asset-files.json <new-recovered-directory>
```

This verifies the complete archive size/hash, exact member inventory, individual file sizes/hashes, and regular-file-only containment before writing a new recovery directory. The inventory and proposal must themselves come from the verified evidence commit.

## 2. Reanalyze saved observations

The proposed task asset retains `observations.json.gz`, containing the selected project's original Swagger findings and sanitized fresh TypeSpec receipts, plus the complete project population. It also retains source annotations, reference-origin investigations, candidate packages, a source overlay, and runtime/provenance receipts.

The dependency-free helper uses Python's standard library:

```powershell
python .\reanalyze.py <recovered-observations.json.gz> <new-output-directory> --verify .\numerical-replay.json
```

The output directory must be new. This independently recomputes project sets, failed population, raw and conservative location counts, signed/absolute/relative project gaps, and both directional excesses. Relative gaps use `absolute gap / max(1, project Swagger raw findings)` solely for investigation priority. It does **not** execute either linter, infer diagnostic correspondence, or establish semantic equivalence.

The report's reference investigation performs exact JSON-path lookups, retaining original `validatorInputFile`, `sourceDocuments`, and `sourceAttribution`. A unique candidate document for a missing-origin finding is not silently rewritten into original reported attribution.

## 3. Regenerate coverage and reassess the report

Recover these immutable source identities:

| Input                     | Identity                                   |
| ------------------------- | ------------------------------------------ |
| Azure base                | `895c7b84c16cc8ab4d834381886bc727fa564c20` |
| Assessed snapshot         | `6252789175001c7f1cdd36b7e083af2eb72447d6` |
| Assessed source tree      | `50cb60159e75c2ac4e9dafe4418803f0fbf991ac` |
| Core gitlink              | `837b5a769414f853fd22eeed0a123c953425b1d8` |
| Frozen specs              | `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9` |
| Tooling                   | `402e3fb202e9a16f0a8c7dfc1b799098cfba879d` |
| Node                      | `26.13.0`                                  |
| Candidate package manager | `pnpm@11.10.0`                             |
| Specs package manager     | `pnpm@12.6.0`                              |

The unchanged frozen specs source is preserved at `msyyc/azure-rest-api-specs:evidence/long-running-operations-options-validator-20261022-source`. Verify the fetched SHA rather than updating this preservation ref. It remains separate from dependency injection and generated data.

The candidate source overlay contains exactly the 19 reviewed changed files. Fetch the canonical Azure base, restore the pinned core, apply only the inventoried overlay, stage those paths, and compare `git write-tree` with the recorded source tree. Its per-file hashes bind source contents without exposing local commit-author metadata. A reconstructed commit can differ from the validation-only snapshot commit while retaining the exact tree; record both identities honestly. The eventual native task commit must likewise match this tested tree.

Use the recorded 20 tarballs for exact artifact replay. The full payload attestation matches 3,318 packed files to the immutable source/build output; it is stronger than package-version equality. Artifact regeneration follows `artifact-plan.json`:

1. Select the candidate's declared toolchain and pinned core. Install only missing selected package/tool closures with `--frozen-lockfile --ignore-scripts`.
2. Build the 17 recorded seed dependency closures and `@typespec/integration-tester`. Do not copy stale output from the development worktree.
3. Pack the eight Azure packages using the Azure Chronus configuration, and the 12 core packages separately from the core workspace. Repeat `--only=<package>` for each package: the installed parser's arrays are nongreedy, and the Azure configuration ignores core packages.
4. Verify source/tree identity and the complete expected package inventory. Preserve changed artifact identities instead of relabeling them as the original tarballs.

Use a dedicated writable specs checkout and a new output directory outside every input checkout. The analyzer invokes candidate `tsp-integration` **patch/install stages only**, never its checkout/reset stage. Put the **specs** package-manager version on the child `PATH` and retain the approved registry process-locally; do not modify global configuration or disable TLS.

After verifying the recovered baseline and task asset, run the applicable original portable suite and the eight selected controls against the injected packages. The selected-control helper creates and verifies the fixture `node_modules` junction; its output root must be new.

From the pinned tooling checkout's `packages\typespec-lintdiff` directory, the original comparison command is:

```powershell
mise exec pnpm@12.6.0 -- node --import tsx/esm test\harness\native-coverage.ts `
  --candidate-repo <clean-candidate> `
  --specs-repo <dedicated-frozen-specs> `
  --tgz-dir <recovered-candidate-artifacts> `
  --validator-rule LatestVersionOfCommonTypesMustBeUsed `
  --tsp-rule @azure-tools/typespec-azure-resource-manager/arm-common-types-version `
  --scope source `
  --baseline-run <verified-sealed-baseline> `
  --baseline-policy frozen-reference `
  --native-mode configured `
  --concurrency 2 `
  --output <new-empty-output>
```

No filter, limit, Swagger regeneration, or artificial native deadline was used. Record a cost estimate and applicable authorization before a new full run.

The recorded source locks, installed runtime metadata/hashes, package entrypoint identities, and artifact inventories identify the actual closure. Sanitized runtime paths must be rebound to recovered locations; original and portable byte hashes are kept separate. This does not claim that every external transitive dependency is forever recoverable or that a future installation resolves identically. A fresh full rerun is distinct from a numerical replay and is not yet a verified recovery path.

Finally, investigate every one-sided project, both count directions, source suppressions, API selection, and reference-attribution limits again. Re-run relevant semantic controls and rewrite all four report sections and NOTES from one coherent assessment. Numerical reproduction alone cannot regenerate the semantic conclusion.
