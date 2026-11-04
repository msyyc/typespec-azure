# specification/dns/resource-manager/Microsoft.Network/Dns

[All project differences](../instance-correspondence.md#differing-projects).

**Project totals:** Swagger 0 raw / 0 member checks; TypeSpec 1 raw; 0 findings credited to the same comparison. Common project/route unit: 0 Swagger / 1 TypeSpec. Counts repeated across different members at the same operation are non-additive. TypeSpec counts refer only to arm-resource-operation-response, not the entire linter suite.

## Additional or different TypeSpec checks

- [Microsoft.Network.DnssecConfigs.createOrUpdate](https://github.com/msyyc/azure-rest-api-specs/blob/2cd3c5dd6d00a5f53214fe594afd2aef3f44d3f9/specification/dns/resource-manager/Microsoft.Network/Dns/DnssecConfig.tsp#L45): **additional-missing-request-policy**; `ARM PUT operations must have a request body.`; route `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/dnssecConfigs/default`.
