# Recovery and replay

## Status

These are prepared recovery instructions, not a publication receipt.
No native task commit, evidence commit, release asset upload, download round trip
or fresh published-checkout recovery has occurred. Retained final local acceptance
must precede publication. Record verified publication identities before following
the published recovery path.

The local candidate envelope has all 15 original artifact-set-1 members. Each
embedded archive was read back and checked against its recorded byte length and
SHA-256. See [candidate-envelope.json](candidate-envelope.json). This local check
is not an independent download.

All four prepared assets passed local verification: 15 candidate packages,
1,469 sanitized run members and 79,756 exact committed tooling files.
[Publication preparation](publication-preparation.json) records their byte
lengths and hashes. [Local replay receipt](local-replay.json) distinguishes
these checks from the pending published-checkout recovery.

## Read saved evidence

Recover the verified `msyyc/typespec-azure` evidence commit on
`evidence/operation-id-noun-verb`, then read this task directory.
Use the immutable commit recorded by the later publication receipt, not a newly
resolved moving head. Recover source from the recorded native publication commit
only after its tree is verified against `source-snapshot.json`.

The shared Swagger baseline is already published:

- Repository: `msyyc/azure-rest-api-specs`.
- Metadata commit: `1c9d2b0e6a596754af1aa793b1906ff3c4ef2bd6`.
- Release: `swagger-lint-baseline-20261026-2cd3c5dd`.
- Asset: `swagger-arm-20261026-2cd3c5dd.tar.gz`.
- SHA-256: `0904cbd17e24ce076e7969837b85b1f5b3682e5ae25b8805b048fb506e77c1d0`.
- Bytes: `51932501`.
- Baseline identity: `aceebb4ebf1ae78205105a94337046d18e583472bd1ebf782effca1e24a75995`.

Verify downloaded bytes before extracting. Preserve the complete sealed
`manifest.json`, `baseline.json` and `dataset` inventory. A subset containing
only this rule's observations cannot replace a sealed CLI baseline.
Never generate Swagger to fill missing baseline files.

### Recover the four task assets

The planned destination is release
`lint-migration-operation-id-noun-verb-cycle0-1` in `msyyc/typespec-azure`.
It is **not published yet**. After publication, use the actual release and
immutable evidence commit recorded in the publication receipt. Do not infer
successful upload from these planned names:

1. `candidate-packages-1.tar.gz`: all 15 exact candidate package archives.
2. `native-run-results-1.tar.gz`: sanitized original run manifest, complete
   coverage report, all 487 worker inputs/results/logs, integration log and
   runtime installation receipts, plus an inner checksum inventory.
3. `comparison-tooling-inputs-1.tar.gz`: the exact committed comparison package
   and root package/tool/lock manifests, including original tracked fixtures.
4. `comparison-tooling-inventory-1.json.gz`: complete checksums for the tooling
   subset. The large uncompressed inventory does not belong in Git.

From the recovered task directory, set `$Assets` to the downloaded asset
directory. With Python from the pinned mise configuration, run:

```powershell
python .\verify-assets.py `
  (Join-Path $Assets "candidate-packages-1.tar.gz") `
  (Join-Path $Assets "native-run-results-1.tar.gz") `
  (Join-Path $Assets "comparison-tooling-inputs-1.tar.gz") `
  (Join-Path $Assets "comparison-tooling-inventory-1.json.gz")
```

The verifier checks all four outer identities and every embedded file before
any extraction. It accepts the candidate archive's recorded `./` root prefix,
rejects duplicate or unexpected files, and never extracts untrusted paths.
Do not treat successful verification of local assets as a download round trip.

The sanitized run asset is **not** a reusable sealed Swagger baseline. The
separately published baseline retains `baseline.json` and the complete dataset.
Sanitized copies replace known machine-local role prefixes and use UTF-8/LF.
Their inventory records original and sanitized hashes separately. Do not feed
symbolic `<specs>` or `<candidate>` paths directly to the analyzer.

## Reanalyze saved observations

From the recovered task directory, with Node 26.5.0:

```powershell
node .\reanalyze.mjs
```

The dependency-free helper checks the full selected receipt population, rejects
duplicate or out-of-population projects, preserves failures as unassessed and
reconstructs every project count and directional difference in `counts.json`.
It does not execute either linter or decide functional equivalence.

The conservative identities are:

1. Swagger occurrence key: rule, project, recorded Swagger file and exact JSON path.
2. Swagger file-independent key: rule, project and exact JSON path.
3. TypeSpec source key: rule, project, source file, line and column.

These identities are not interchangeable. In particular, a fallback Swagger
input filename does not establish a diagnostic's defining source document.
Raw occurrences remain intact even when location keys coincide.
Relative differences use `abs(Swagger - TypeSpec) / max(Swagger, TypeSpec, 1)`.

## Regenerate coverage

This full rerun is distinct from the count audit and has not been repeated as a
recovery test. It requires recovered source, artifacts and installed tool/runtime
closures. Version strings alone do not prove all transitive dependency identities.

1. Create isolated temporary recovery checkouts strictly under `C:\dev\worktrees`.
   Do not reset another task's checkout or create a fourth persistent replay role.
2. Recover the exact native published source tree, verified against
   `source-snapshot.json`, and core commit
   `05b9bad7c57b9b58e8fb5390f9bab081a1a9ac31`.
3. Recover the 15 packed artifacts from the later verified candidate-envelope
   asset. Check every member against `candidate-artifacts.json`. Do not substitute
   current registry packages or rebuild passing artifacts without new evidence.
4. Recover specs commit `2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9`.
   Its verified preservation ref is
   `msyyc/azure-rest-api-specs:evidence/long-running-operations-options-validator-20261022-source`.
   Check its SHA and clean source/lock state before injection.
5. Recover tooling repository `Azure/typespec-azure` at commit
   `662e7f405fda22e1d9c8c9c1d7664d171f80b60d`. Verify the analyzer and worker
   against [tooling-inputs.json](tooling-inputs.json), the run manifest and the
   complete compressed member inventory. The tooling asset retains the recorded
   package and root dependency lock; it is a subset, not a standalone installed
   repository or offline dependency cache. Recover the full repository at that
   commit before using the retained subset. Recover core from
   `microsoft/typespec` at the candidate's exact gitlink; do not resolve latest.
6. Use Node 26.5.0 and pnpm 12.6.0 for the specs runner. Set both variables for the
   runner and every pnpm child process:

   ```powershell
   $env:PNPM_CONFIG_VERIFY_DEPS_BEFORE_RUN = "false"
   $env:PNPM_CONFIG_REGISTRY = "https://packagefeedproxy.microsoft.io/npm/"
   ```

   Put the pinned Node and pnpm executables on child `PATH`.
   Do not let `pnpm exec` silently auto-install a workspace.
   The owning-package validation used pnpm 11.10.0, while the specs runtime
   used pnpm 12.6.0; do not substitute one for the other.

7. Reestablish actual owner-relative installed package resolution and loader export
   conditions against exact packed members. Run the five retained selected-rule
   controls through the actual coverage worker. `control-sources` contains
   whitespace-normalized reading copies. Restore exact executed bytes from
   [control-source-originals.json](control-source-originals.json) into a new
   `$Controls` directory before byte-exact replay:

   ```powershell
   $originals = Get-Content ".\control-source-originals.json" -Raw | ConvertFrom-Json
   foreach ($file in $originals.files) {
     $destination = Join-Path $Controls $file.file
     [System.IO.Directory]::CreateDirectory((Split-Path $destination -Parent)) | Out-Null
     [System.IO.File]::WriteAllBytes($destination, [Convert]::FromBase64String($file.base64))
   }
   ```

   Verify each restored SHA-256 against its retained entry. The five `main.tsp`
   hashes also match the actual installed-control receipts.
   Preserve the 37 applicable portable controls and the six predeclared unrelated
   exclusions. Do not count skips as passing runtime controls.
   [Installed identities](installed-controls.json) retain the declared owner,
   actual loader conditions and exact corresponding packed member. A transitive
   dependency need not resolve from the specs root, and `manifest.main` is not
   a universal expected entrypoint.

8. Use a new empty output directory, exclusive writable specs runtime and the
   complete integrity-verified shared baseline. From the recovered tooling
   `packages\typespec-lintdiff` directory, use these exact supported options.
   Variables denote the recovered absolute role paths:

   ```powershell
   node --import tsx/esm .\test\harness\native-coverage.ts `
     --candidate-repo $CandidateRepo `
     --specs-repo $SpecsRepo `
     --tgz-dir $Artifacts `
     --validator-rule OperationIdNounVerb `
     --tsp-rule @azure-tools/typespec-client-generator-core/no-redundant-operation-group-name `
     --scope source `
     --baseline-run $Baseline `
     --baseline-policy frozen-reference `
     --output $Output `
     --concurrency 2 `
     --native-mode target-only `
     --native-budget-seconds 7200
   ```

   Do not add a filter or limit. The analyzer runs candidate integration
   patch/install, not checkout. Retain its installation/source-restoration receipts.

9. Verify all 487 results and actual installed artifact identities. Preserve every
   compile, worker or projection failure as unassessed. Investigate every one-sided
   project and all count-difference groups using exact source and saved Swagger.
10. Regenerate numerical evidence, then reassess the semantic conclusion and write
    the four-section migration note. Counts alone cannot regenerate its conclusion.
    Never promise identical future counts or prose without a captured rerun.

The candidate package manifests, source snapshot and retained runtime locks
document the observed closure. They do not prove a complete offline cache or
attest every transitive runtime byte from version strings alone. The prepared
assets retain recorded locks without claiming that a future install or full
native rerun was exercised during recovery.

## Independent publication recovery gate

After authorized publication, download the exact assets into a **fresh temporary
checkout of the published evidence commit**. Do not seed that checkout from the
populated local evidence directory or Copilot session files.
Verify committed blob bytes, asset hashes, all inner archive identities and the
dependency-free count audit. Preserve the verified receipt in the persistent
evidence role, then remove only that temporary checkout after stopping its work.

The final publication receipt must distinguish reading evidence, saved-observation
reanalyzing, sealed-baseline recovery and a full native rerun. None is implied by
another, and no pending gate is a success.
