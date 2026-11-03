# PR 5481: semantic comparison appendix

The observations below describe historical candidate `7baca4db3d7824c24c30961c50c3f47a6df8d958`.
The [corrected candidate and current validation](fix-validation.md) supersede
the inherited-traversal and missing-PUT results; [fresh full-corpus results](fix-results.md)
are separate. Historical versioning remains deferred under #5875.

## Scope and evidence

**This task reports differences. It does not authorize changes to rule semantics. Broader equivalence requires an explicit policy decision.**

The candidate extends the existing `@azure-tools/typespec-azure-resource-manager/arm-resource-patch` rule. It is not a literal port of the Swagger validator's whole-schema comparison. Neither functional equivalence nor diagnostic-count equivalence is established.

Pinned sources:

- **Original validator:** [`6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f`][original-function].
- **Candidate:** [`7baca4db3d7824c24c30961c50c3f47a6df8d958`][candidate-rule].
- **Shared-baseline producer tooling:** [`8cbd8d8348d5b614afb8bf60d74477de6caaab1a`][producer].

The original implementation/documentation/registration URLs were verified against immutable GitHub blobs. The candidate and producer GitHub commit identities were also verified.

Evidence labels used below:

| Label                           | Meaning                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Executed: native helper**     | Compiled minimal source in the compiler's virtual filesystem, then invoked the existing compiled paired-body helper with a collecting context. Listed controls had no compiler diagnostics. The candidate artifact was not rebuilt. These controls do not exercise normal lint activation, suppression, or the older operation listener. |
| **Executed: Swagger predicate** | Transpiled the unchanged original function/helper in memory and called them with miniature already-resolved schema objects, using installed Lodash 4.18.1. Not a full Spectral/AutoRest run, reference-resolution test, or verification against the original pinned dependency installation.                                             |
| **Source inspection**           | Conclusion follows from the linked pinned implementation. Not an additional executed control.                                                                                                                                                                                                                                            |
| **Existing focused test**       | The candidate test and its assertion were independently inspected. Existing tests were not rerun for this appendix.                                                                                                                                                                                                                      |
| **Retained execution logs**     | Observation from the already-produced shared production baseline, not a new corpus execution.                                                                                                                                                                                                                                            |

**Original control boundary:** no real Swagger staging validation was executed
for these miniature controls. They do not establish staging corpus totals or
emitted-schema parity. The subsequent validator-only corpus evaluation is
reported separately in [the staging comparison](staging-comparison/summary.json)
and [gap investigation](gap-investigation.md); it does not turn these controls
into emitter or full native reruns.

## Original contract and activation

The [original documentation][original-doc] describes ARM PATCH property presence and a nonempty PATCH body. The [actual registration][original-registration] is:

```text
ID: PatchPropertiesCorrespondToPutProperties
Guideline: RPC-Patch-V1-01
severity: error
stagingOnly: true
resolved: true
formats: [oas2]
given: ["$[paths,'x-ms-paths'].*"]
then.function: patchPropertiesCorrespondToPutProperties
functionOptions: none
```

The function ignores `_opts`. There is no per-rule `openapiType` or TypeSpec-disablement flag in this registration. The caller selects the ARM ruleset; this is **not an RPaaS-only registration**.

The original function requires both verbs on the selected path-item and reads operation-level `parameters` whose `in` is `"body"`. It compares only the first body parameter. Its `"empty"` checks count body parameters, not properties. It compares retained `{name: schema}` objects using Lodash deep equality. See [function][original-function] and [traversal helper][original-helper].

The candidate retains the existing rule's **warning** severity and [ARM `all` enablement][candidate-linter]. Its paired listener accepts project HTTP services without requiring provider-namespace metadata; the [ARM ruleset also enables the existing rule][candidate-profile]. Thus activation differs from the original staging-only predicate.

## Behavior matrix

| Concern                          | Original Swagger implementation                                                                                         | Candidate paired-body helper                                                                                                                                               | Evidence                                                                                                                   |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Endpoint selection               | Both verbs in one resolved `paths` or `x-ms-paths` item.                                                                | Exact current HTTP path, per service and resolved version; project operations only; same-endpoint overloads excluded. Last encountered operation retained for a verb/path. | [Original][original-function]; [native pairing][native-pairing].                                                           |
| Property identity                | Whole retained one-key schema object, not just its name.                                                                | Effective JSON leaf name only.                                                                                                                                             | [Deep equality][original-comparison]; [name set][native-comparison].                                                       |
| Scalar types and constraints     | Differences in retained type, format, enum, constraints, or extensions can diagnose.                                    | Same-name leaves are accepted regardless of these differences.                                                                                                             | **Executed controls** for scalar type; other listed fields: **source inspection**.                                         |
| Description/client-name metadata | Unequal leaf metadata can diagnose despite matching wire name and type.                                                 | Metadata is not compared.                                                                                                                                                  | **Executed description control**; [encoded-name compliant test][tests-leaf-controls].                                      |
| Requiredness                     | Parent `required` lists are not part of separately collected leaf schemas.                                              | Property optionality is not compared.                                                                                                                                      | **Executed Swagger predicate** required-list control; native **source inspection**.                                        |
| Ordinary nesting                 | Direct property objects are flattened; ancestor names do not identify their leaves.                                     | Flattens when the nested type has direct effective payload properties; ancestor names do not identify flattened leaves.                                                    | [Original helper][original-helper]; [native traversal][native-traversal]; [tests][tests-leaf-controls].                    |
| Inherited-only nested wrappers   | A property with only `allOf`, without direct `properties`, remains an opaque wrapper.                                   | A nested model with only inherited properties remains a wrapper leaf under the direct-property gate.                                                                       | **Executed wrapper controls**; [focused test][tests-basic]. This does not prove all composition shapes equivalent.         |
| Inheritance and overrides        | Traverses entered `allOf` schemas, potentially retaining duplicate occurrences.                                         | Enumerates inherited properties with overrides; excludes `never`; resolves JSON names.                                                                                     | [Original helper][original-helper]; [model utilities][native-utils]; [native filtering][native-traversal].                 |
| Missing/void PATCH               | No body parameter produces one body error.                                                                              | Missing/void body produces one `missingPatchBody` per PATCH operation across versions.                                                                                     | [Original body checks][original-function]; [native body checks][native-bodies]; [tests][tests-bodies].                     |
| Empty PATCH object               | An existing body parameter with zero schema leaves is accepted when PUT has a body.                                     | Supported object with zero effective input leaves produces `emptyPatchBody`.                                                                                               | **Executed controls**.                                                                                                     |
| Missing PUT body                 | Existing PATCH body parameter with no PUT body parameter produces a body-level error.                                   | Skips correspondence after independently checking PATCH absence/emptiness.                                                                                                 | **Executed controls**; [tests][tests-bodies].                                                                              |
| Empty PUT object                 | Nonempty PATCH produces per-unmatched-leaf errors.                                                                      | Nonempty PATCH produces per-missing-name errors.                                                                                                                           | **Executed controls**. Units can still differ.                                                                             |
| Arrays/dictionaries/unions       | Retained leaves include item/value/union schema information. Top-level shapes without properties may collect no leaves. | Top-level arrays, dictionaries, ambiguous unions and nonsingle bodies are skipped. Property-level arrays, dictionaries and ambiguous unions are opaque named leaves.       | **Executed array/value-type and selected unsupported-body controls**; [object gate][native-object]; [tests][tests-unions]. |
| Nullable models                  | No native union-unwrapping algorithm; behavior depends on emitted schema.                                               | Unwraps exactly one non-null member. Nullable model properties can flatten.                                                                                                | [Utility][native-utils]; **executed nullable-extra-leaf control**; [tests][tests-leaf-controls].                           |
| Discriminators                   | Compares actual resolved emitted properties, including a synthesized property if present.                               | Does not synthesize unauthored discriminator properties. Authored discriminator properties are compared.                                                                   | **Source inspection**; [focused tests][tests-discriminator], [authored discriminator test][tests-input].                   |
| Visibility/HTTP membership       | No intrinsic read-only, mutability, or HTTP metadata filtering; consumes its input schema.                              | Per-operation request visibility and payload membership; explicit `@body` and `@bodyRoot` differ.                                                                          | [Native traversal][native-traversal]; [visibility tests][tests-visibility], [membership tests][tests-input].               |
| Versions                         | Uses the shapes in each selected Swagger file.                                                                          | Evaluates added/removed availability with service/dependency resolution; does not reconstruct historical names, types, routes, or body shapes.                             | [Availability code][native-versions]; **executed historical controls** below.                                              |
| Recursion                        | No explicit helper cycle guard.                                                                                         | Branch-local model visitation prevents infinite recursion; cyclic traversal can fall back to a named leaf.                                                                 | [Traversal][native-traversal]; [recursive test][tests-leaf-controls]. Not a full Spectral cycle comparison.                |
| Deduplication                    | One result per unmatched retained schema occurrence, per selected Swagger path/file.                                    | Missing-name result deduplicated by diagnostic target plus JSON name across services, versions and endpoint pairs.                                                         | [Original reporting][original-comparison]; [native reporting][native-comparison]; [dedup tests][tests-dedup].              |

The native type/schema-equality omission is not limited to harmless descriptions: **a same-name incompatible type can pass the native helper.** This is a real omission of the original comparison, not universally a Swagger bug. Whether correspondence should require type compatibility, exact schema equality, or name presence alone is a policy question; this appendix does not resolve it.

## Minimal discriminating examples

Unless stated otherwise, source fragments substitute `PutBody` and `PatchBody` into this endpoint pair:

```typespec
@service
namespace Example;

// PutBody and PatchBody declarations go here.
@route("/widgets")
@put
op put(@body body: PutBody): void;
@route("/widgets")
@patch
op patch(@body body: PatchBody): void;
```

Imports/usings for HTTP and versioning are omitted for brevity. Swagger snippets are **predicate inputs**, not claims of newly generated emitter output.

### Same name, unequal scalar type

```typespec
model PutBody {
  value?: string;
}
model PatchBody {
  value?: int32;
}
```

```json
{
  "put": {
    "parameters": [
      {
        "in": "body",
        "schema": {
          "type": "object",
          "properties": { "value": { "type": "string" } }
        }
      }
    ]
  },
  "patch": {
    "parameters": [
      {
        "in": "body",
        "schema": {
          "type": "object",
          "properties": { "value": { "type": "integer", "format": "int32" } }
        }
      }
    ]
  }
}
```

- **Executed: Swagger predicate:** one `value` finding.
- **Executed: native helper:** no finding.
- Interpretation: actual type disagreement is accepted by the name-only comparison. Do not classify it automatically as harmless metadata noise.
- Additional **executed controls:** `string[]` versus `int32[]`, and `Record<string>` versus `Record<int32>`, each produced one Swagger predicate finding and no native helper finding.

### Same name/type, unequal description

```typespec
model PutBody {
  @doc("PUT description") value?: string;
}
model PatchBody {
  @doc("PATCH description") value?: string;
}
```

```json
{
  "putLeaf": { "value": { "type": "string", "description": "PUT description" } },
  "patchLeaf": { "value": { "type": "string", "description": "PATCH description" } }
}
```

The two `value` schemas are inserted into ordinary object body schemas as above.

- **Executed: Swagger predicate:** one `value` finding.
- **Executed: native helper:** no finding.
- This isolates metadata inequality without a type mismatch. The [original focused schema-value test][original-value-test] also expects unequal property schemas to diagnose.
- The same-name type example must remain separate; this description control cannot explain every Swagger-only report.

### Empty PATCH model versus absent PATCH body

```typespec
model PutBody {
  value?: string;
}
model PatchBody {}
```

```json
{
  "put": {
    "parameters": [
      {
        "in": "body",
        "schema": {
          "type": "object",
          "properties": { "value": { "type": "string" } }
        }
      }
    ]
  },
  "patch": {
    "parameters": [
      {
        "in": "body",
        "schema": {
          "type": "object",
          "properties": {}
        }
      }
    ]
  }
}
```

- **Executed: Swagger predicate:** no finding. Its collected PATCH value is `[[]]`; the outer body-parameter count is one.
- **Executed: native helper:** one `emptyPatchBody`.
- In contrast, `patch.parameters: []` produced the original `"Patch operations body cannot be empty."` predicate finding. Existing native tests independently cover absent/void bodies and effective-empty models.

### Missing PUT body

```typespec
model PatchBody {
  value?: string;
}
@route("/widgets") @put op put(): void;
@route("/widgets") @patch op patch(@body body: PatchBody): void;
```

```json
{
  "put": { "parameters": [] },
  "patch": {
    "parameters": [
      {
        "in": "body",
        "schema": {
          "type": "object",
          "properties": { "value": { "type": "string" } }
        }
      }
    ]
  }
}
```

- **Executed: Swagger predicate:** one `"Non empty patch body with an empty put body is not valid."` finding.
- **Executed: native helper:** no finding.
- A supported but empty PUT object is different: both executed controls produced one missing-`value` finding.
- Native still rejects an empty PATCH model when PUT has no body; that separate ordering is covered by an existing focused test.

### Synthesized discriminator

```typespec
model PutBody {
  name?: string;
}
@discriminator("kind")
model PatchBody {
  name?: string;
}
model ConcretePatch extends PatchBody {
  kind: "concrete";
}
```

Conditional schema-level distinction:

```json
{
  "putProperties": { "name": { "type": "string" } },
  "patchPropertiesAfterSynthesis": {
    "name": { "type": "string" },
    "kind": { "type": "string" }
  }
}
```

- **Source inspection:** if emission supplies the additional `kind` schema shown, the original predicate compares that emitted leaf and diagnoses it.
- **Existing focused tests:** native accepts direct and inherited unauthored discriminators; it does not manufacture `kind`. A separately authored `kind` property is diagnosed when absent from PUT.
- **Not executed here:** an emitter run or real Swagger staging validation for this discriminator example. The conditional schema is explanatory, not newly observed emitted output.

### Historical renamed and type-shape properties

Both controls used an actual two-version service and same-path explicit bodies:

```typespec
@service
@versioned(Versions)
namespace Example;
enum Versions {
  v1,
  v2,
}

model PutBody {
  common?: string;

  @renamedFrom(Versions.v2, "oldName")
  currentName?: string;
}
model PatchBody {
  common?: string;

  @removed(Versions.v2)
  oldName?: string;
}
```

- Expected from historical wire names: both expose `oldName` in v1; PATCH removes it in v2. No missing-name violation is expected from those projected shapes.
- **Executed: native helper:** one missing-`oldName` finding. The current PUT name is used while checking v1.
- **Not observed here:** emitted historical Swagger or its validator result.

Type-shape variant:

```typespec
model Old {
  oldLeaf?: string;
}
model Current {
  currentLeaf?: string;
}
model PutBody {
  common?: string;

  @typeChangedFrom(Versions.v2, Old)
  detail?: Current;
}
model PatchBody {
  common?: string;

  @removed(Versions.v2)
  detail?: Old;
}
```

- Expected historical shapes: both expose `detail.oldLeaf` in v1; PATCH removes `detail` in v2.
- **Executed: native helper:** one missing-`oldLeaf` finding, because it traverses PUT's current `detail` type while checking v1.
- This is a historical shape-reconstruction limitation, distinct from intentionally comparing scalar leaf names without scalar types.
- Existing availability tests do not establish historical projection equivalence.

**Disposition:** known TypeSpec false positives, accepted temporarily for
[migration PR #5481](https://github.com/Azure/typespec-azure/pull/5481) with the
migration owner's approval; defer the correction to the shared
[version-aware linting issue #5875](https://github.com/Azure/typespec-azure/issues/5875).
That issue's current example is an availability false negative, while these
controls demonstrate rename/type-shape false positives. Both require evaluating
the API shape for each version, with consistent reporting and suppression.
No rule-local versioning correction is required for this PR under the deferral.
The observations above remain unchanged; acceptance is not a fix or a
functional-equivalence claim and does not cover inherited-property false positives.

### Source-target deduplication

```typespec
model PutBody {
  common?: string;
}
model PatchBody {
  missing?: string;
}

@route("/first") @put op firstPut(@body body: PutBody): void;
@route("/first") @patch op firstPatch(@body body: PatchBody): void;
@route("/second") @put op secondPut(@body body: PutBody): void;
@route("/second") @patch op secondPatch(@body body: PatchBody): void;
```

- **Existing focused test / source inspection:** one native helper finding for the shared `missing` property, not one per endpoint.
- Original schema-level unit: the equivalent unmatched leaf occurs separately in each selected path-item. Its predicate has no cross-path deduplication.
- Distinct authored properties sharing the same JSON name can still produce separate native findings.
- Original findings at one endpoint share `...patch.parameters`; JSON path alone does not uniquely identify individual findings. Preserve property/message evidence and multiplicity.
- Native missing-name identity is target plus JSON name, not merely file/line. Body errors have operation-level identity.

### Existing tags/subset checks coexist

The [older operation listener][candidate-old-checks] remains alongside the paired-body helper under the same rule code:

```typespec
model WidgetPatch {
  tags?: Record<string>;
  properties?: {
    displayName?: string;
  };
  extra?: string;
}
```

For a discovered ARM resource whose properties do not include `extra`, the old subset branch can diagnose `extra` independently of a corresponding PUT. If the resource has a direct `tags` property, a PATCH without a model-valued `tags` property can instead trigger the old tags branch.

These are **source-inspection conclusions**, not newly executed full-rule controls. The existing focused tests cover old reference/spread subset checks and the old missing-body warning; no dedicated tags-branch test was found in the inspected native file.

The old resource discovery requires suitable successful model variants in a union return and can examine template arguments. It is not a general direct-return-type detector. ARM-origin source properties can bypass the old name-subset branch. Do not simplify this listener into an unconditional check over every PATCH model.

The old checks report operation-level default/tags/subset warnings; the new helper often reports property-level missing-name warnings. They can coexist, so **all `arm-resource-patch` findings are not automatically attributable to this one migrated Swagger rule**.

### Executed follow-up: inherited writable PUT properties behind read-only direct members

**One focused native raw-helper control was executed.** It confirms that the direct-property recursion gate can make PUT/PATCH traversal asymmetric even when their writable leaf is the same declaration.

```typespec
@service
namespace Example;
model CustomerManagedKeyEncryption {
  identityType?: string;
}
model Encryption {
  customerManagedKeyEncryption?: CustomerManagedKeyEncryption;
}
model UpdateProperties {
  encryption?: Encryption;
}
model PutProperties extends UpdateProperties {
  @visibility(Lifecycle.Read) provisioningState?: string;
  @visibility(Lifecycle.Read) devCenterUri?: string;
}
model PutBody {
  properties?: PutProperties;
}
model PatchBody {
  properties?: UpdateProperties;
}
@route("/widgets") @put op put(@body body: PutBody): void;
@route("/widgets") @patch op patch(@body body: PatchBody): void;
```

HTTP/lifecycle imports and usings were supplied by the existing virtual test harness.

**Observed:** zero compiler diagnostics; one raw-helper report:

```text
messageId: missingProperty
propertyName: identityType
target: CustomerManagedKeyEncryption.identityType
message: The property 'identityType' in the PATCH body does not correspond to a property in the PUT body.
```

**Mechanism:** [`hasDirectPayloadProperties`][native-traversal] tests `type.properties`, not inherited properties. `PutProperties` has only read-only direct members, so its writable inherited `encryption` does not open the recursion gate. PUT retains the outer name `properties` as an opaque leaf. PATCH's `UpdateProperties` has a direct writable `encryption`, so it recursively reaches `identityType`. The collected names therefore differ despite the shared inherited writable declaration. Once recursion starts, `collectTypeLeaves` itself uses inherited-property enumeration; that does not repair the earlier gate.

**Interpretation:** this is a demonstrated traversal false positive in the minimal control, not a deliberate same-name schema-equality difference. It supports the proposed explanation for the reported DevCenter inheritance pattern. It does **not** establish that all 90 DevCenter findings have this cause or are false positives: no DevCenter project replay, emitted-schema comparison, actual leaf inventory assessment, or Swagger staging validation was performed for this follow-up. The control invokes only the paired-body helper, not the complete rule's older tags/subset listener or normal suppression pipeline. No semantics change is authorized by this evidence.

## Focused test mapping

Current native files are `patch-operations.test.ts` and `model-utils.test.ts`. References below map actual assertions; they are not stale fixture counts or a claim that the tests were rerun.

| Native test evidence                                      | Material behavior                                                                                                                                                                                          |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`patch-operations.test.ts:23–179`][tests-old]            | Existing resource subset checks for model references/spreads; old missing-body behavior.                                                                                                                   |
| [`patch-operations.test.ts:195–329`][tests-examples]      | Incorrect/correct ARM template examples; shared versus distinct property targets across services.                                                                                                          |
| [`patch-operations.test.ts:331–368`][tests-basic]         | Nested missing leaf without provider metadata; encoded-name mismatch; inherited-only wrapper mismatch.                                                                                                     |
| [`patch-operations.test.ts:371–445`][tests-bodies]        | Missing/void/empty PATCH; missing/void PUT accepted; unauthored discriminator not synthesized.                                                                                                             |
| [`patch-operations.test.ts:448–537`][tests-visibility]    | Standard ARM PUT with Create visibility; explicit visibility controls; empty effective PATCH input, including absent PUT.                                                                                  |
| [`patch-operations.test.ts:543–650`][tests-input]         | PATCH/PUT `@body` versus `@bodyRoot`; unsupported PUT shapes; authored discriminator; inherited visibility; `never` override; operation-specific visibility on shared models.                              |
| [`patch-operations.test.ts:653–757`][tests-leaf-controls] | Nullable body, recursion/distinct siblings, subset, nesting changes, equal encoded names, discriminator controls, matching scalar/array and other property families.                                       |
| [`patch-operations.test.ts:760–830`][tests-dedup]         | No paired PUT; shared-source dedup across endpoint pairs; same-endpoint overload handling.                                                                                                                 |
| [`patch-operations.test.ts:849–1046`][tests-versions]     | Added/removed properties, inheritance/spreads and nested namespaces, dependency version mapping, nonconcurrent operation/interface declarations, synchronized additions, removed explicit body parameters. |
| [`model-utils.test.ts:6–45`][tests-model-utils]           | Unambiguous non-null member selection; inheritance overrides and encoded names without helper-level payload filtering.                                                                                     |

Important unestablished boundaries:

- Matching type-family controls do not test negative same-name type/constraint equality.
- Existing added/removed tests do not cover historical renames, type changes, routes or body-shape projection.
- Unsupported PUT coverage is not coverage of every unsupported PATCH top-level shape, null-only body or multipart body.
- The inherited-only wrapper test does not establish every mixed direct/inherited `allOf` composition.
- Library-origin fallback diagnostic targets, target-rule suppression placement, and old/new combined diagnostic cardinality lack focused evidence here.
- Multiple same-verb operations at one path, alternate-path/query representation, path-level Swagger body parameters, duplicate schema occurrences and full Spectral cyclic-reference behavior remain limitations.
- The old tags branch is not independently covered by a dedicated test in the inspected native file.
- Native missing-property diagnostics target declarations, not automatically the PATCH operation using them. Standard source suppression placement and shared-target dedup affect final user-visible results; raw-helper controls bypass that pipeline.
- Older tests suppress unrelated deprecation warnings. Explicit `@body` metadata controls suppress `@typespec/http/metadata-ignored`; they are not evidence that the underlying prerequisite warning is absent.
- Full source-schema/emitter equivalence, compliant real-service behavior, and corpus outliers are not established by this appendix.

## Shared production baseline: not evaluated

Baseline identity: `swagger-arm-20261026-2cd3c5dd`.

**`PatchPropertiesCorrespondToPutProperties` was not evaluated in this production baseline because it is staging-only. Its absent shard/index entry is not an evaluated zero.**

Evidence chain:

1. The frozen runtime lock records validator **2.2.4**, core **1.0.7**, and rulesets **2.2.6** at `dataset/_baseline-runtime/1-pnpm-lock.yaml:230–238`; the validator dependency on rulesets 2.2.6 appears at `:5072–5076`.
2. The matching installed registration used the exact ID and selector shown above, with `stagingOnly: true`; no renamed ID was discovered.
3. The [frozen producer][producer] resolves the installed validator at lines **875–878**, then invokes production ARM validation at **924–940** without `--is-staging-run`. `dataset/_meta.json:8` preserves that command.
4. The [validator's staging gate][original-staging-gate] disables staging-only rules in production. More importantly, the retained execution logs directly record exclusion.

Concrete relative raw-log receipt:

```text
dataset/projects/specification/advisor/resource-manager/Microsoft.Advisor/Advisor/raw/preview/2026-08-01-preview/openapi.jsonl
```

| Line | Retained observation                                                                                                            |
| ---- | ------------------------------------------------------------------------------------------------------------------------------- |
| 61   | `Detected production run` and `PatchPropertiesCorrespondToPutProperties` listed among rules being disabled.                     |
| 132  | `DISABLED Spectral rule for manually written OpenAPI specs, severity 'DISABLED': 'PatchPropertiesCorrespondToPutProperties'`.   |
| 182  | Production staging-rule exclusion repeated for the second ruleset.                                                              |
| 253  | `DISABLED Spectral rule for TypeSpec-generated OpenAPI specs, severity 'DISABLED': 'PatchPropertiesCorrespondToPutProperties'`. |

A read-only scan of every retained `dataset/projects/**/*.jsonl` actually observed:

| Observation                                   | Files |
| --------------------------------------------- | ----: |
| Raw log files inspected                       |   649 |
| Explicitly disable the exact rule ID          |   649 |
| Log production exclusion of the exact rule ID |   649 |
| Log staging execution                         |     0 |
| Log the exact rule ID enabled                 |     0 |

The scan searched for `DISABLED Spectral rule` plus the exact quoted ID, `Detected production run` plus the exact ID, `Detected staging run`, and `ENABLED Spectral rule` plus the exact quoted ID. This was retained-log inspection, **not a validator rerun**.

`dataset/_meta.json:42–50` records 487 validated projects, 649 Swagger files and zero validation failures. These execution totals do not change this member's disabled status.

For this original production run, reader-facing reporting must preserve
**“not evaluated (staging-only)”**, even if a machine report fills an absent
mapped member with numeric `0`. Keep the original mapping for provenance, but
do not use that placeholder as a parity denominator, clean result, or
justification for dismissing native-only findings. The separately sealed staging
supplement does not rewrite these original production observations.

The original fresh full native run is separate evidence. Inspecting its
production baseline did not regenerate Swagger, modify a production rule, or
execute staging. The subsequent staging evaluation supplies actual emitted-side
counts, but an equivalence conclusion still requires an explicit semantic
policy decision and aligned source/emission evidence, not reinterpretation of
this disabled production member as zero.

## Immutable references

[original-function]: https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-properties-correspond-to-put-properties.ts#L15-L70
[original-doc]: https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/docs/patch-properties-correspond-to-put-properties.md#L3-L25
[original-registration]: https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/az-arm.ts#L475-L489
[original-helper]: https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/utils.ts#L47-L69
[original-comparison]: https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/functions/patch-properties-correspond-to-put-properties.ts#L56-L67
[original-value-test]: https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/rulesets/src/spectral/test/patch-properties-correspond-to-put-properties.test.ts#L583-L713
[original-staging-gate]: https://github.com/Azure/azure-openapi-validator/blob/6243cb01c16c7535cd3b8df6f45fbeb3c095ed7f/packages/azure-openapi-validator/autorest/src/spectral-plugin-utils.ts#L10-L50
[candidate-rule]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/src/rules/arm-resource-patch.ts#L29-L55
[candidate-old-checks]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/src/rules/arm-resource-patch.ts#L59-L150
[candidate-linter]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/src/linter.ts#L111-L140
[candidate-profile]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-rulesets/src/rulesets/resource-manager.ts#L110-L110
[native-pairing]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/src/rules/arm-resource-patch-body.ts#L37-L72
[native-bodies]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/src/rules/arm-resource-patch-body.ts#L75-L114
[native-comparison]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/src/rules/arm-resource-patch-body.ts#L115-L135
[native-object]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/src/rules/arm-resource-patch-body.ts#L180-L190
[native-traversal]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/src/rules/arm-resource-patch-body.ts#L159-L285
[native-versions]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/src/rules/arm-resource-patch-body.ts#L288-L319
[native-utils]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/src/rules/model-utils.ts#L12-L29
[tests-old]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/test/rules/patch-operations.test.ts#L23-L179
[tests-examples]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/test/rules/patch-operations.test.ts#L195-L329
[tests-basic]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/test/rules/patch-operations.test.ts#L331-L368
[tests-bodies]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/test/rules/patch-operations.test.ts#L371-L445
[tests-discriminator]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/test/rules/patch-operations.test.ts#L423-L445
[tests-visibility]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/test/rules/patch-operations.test.ts#L448-L537
[tests-input]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/test/rules/patch-operations.test.ts#L543-L650
[tests-unions]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/test/rules/patch-operations.test.ts#L562-L576
[tests-leaf-controls]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/test/rules/patch-operations.test.ts#L653-L757
[tests-dedup]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/test/rules/patch-operations.test.ts#L760-L830
[tests-versions]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/test/rules/patch-operations.test.ts#L849-L1046
[tests-model-utils]: https://github.com/Azure/typespec-azure/blob/7baca4db3d7824c24c30961c50c3f47a6df8d958/packages/typespec-azure-resource-manager/test/rules/model-utils.test.ts#L6-L45
[producer]: https://github.com/Azure/typespec-azure/blob/8cbd8d8348d5b614afb8bf60d74477de6caaab1a/packages/typespec-lintdiff/test/harness/spec-dataset.ts#L875-L946
