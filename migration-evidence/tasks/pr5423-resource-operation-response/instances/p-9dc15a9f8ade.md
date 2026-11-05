# specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry

[All project differences](../instance-correspondence.md#differing-projects).

**Project totals:** Swagger 1 raw / 1 member checks; TypeSpec 2 raw; 1 findings credited to the same comparison. Common project/route unit: 1 Swagger / 2 TypeSpec. Counts repeated across different members at the same operation are non-additive. TypeSpec counts refer only to arm-resource-operation-response, not the entire linter suite.

## Matching request checks

- [`32e3c2def02f5a05`](../instance-correspondence.md#s-32e3c2def02f5a05): `Webhooks_Create`; one Swagger finding and one matching TypeSpec warning.

## Additional or different TypeSpec checks

- [Microsoft.ContainerRegistry.ArchiveVersions.create](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/Registry/ArchiveVersion.tsp#L84): **additional-missing-request-policy**; `ARM PUT operations must have a request body.`; route `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/packages/{packageType}/archives/{archiveName}/versions/{archiveVersionName}`.
