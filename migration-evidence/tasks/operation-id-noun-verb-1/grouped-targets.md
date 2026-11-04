# Complete target accounting for differing projects

Counts are retained raw findings, not normalized actionable defects. Source ownership and HTTP metadata are captured independently. The original automatic joins remain unchanged; two Resources bridges use explicit authored rename annotations.

## Billing

Project: `specification/billing/resource-manager/Microsoft.Billing/Billing`; API version: `2024-04-01`.

Raw Swagger / TypeSpec: **5 / 4**. Signed TypeSpec minus Swagger: -1; absolute gap: 1; relative gap: 0.2.

| Exact HTTP target                                                                                                                           | Common owner / method; source                                      | Swagger | TypeSpec | Identity                                |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------- | -------- | --------------------------------------- |
| `GET /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoices/{invoiceName}/transactionSummary`                           | `Transactions.getTransactionSummaryByInvoice`; `Invoice.tsp:254:3` | 1       | 1        | Exact route/verb and source coordinates |
| `POST /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoices/{invoiceName}/transactionsDownload`                        | `Transactions.transactionsDownloadByInvoice`; `Invoice.tsp:240:3`  | 1       | 0        | Exact route/verb and source coordinates |
| `GET /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/reservationOrders/{reservationOrderId}/reservations`                 | `Reservations.listByReservationOrder`; `Reservation.tsp:86:3`      | 1       | 1        | Exact route/verb and source coordinates |
| `GET /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/reservationOrders/{reservationOrderId}/reservations/{reservationId}` | `Reservations.getByReservationOrder`; `Reservation.tsp:55:3`       | 1       | 1        | Exact route/verb and source coordinates |
| `GET /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/savingsPlanOrders/{savingsPlanOrderId}/savingsPlans`                 | `SavingsPlans.listBySavingsPlanOrder`; `SavingsPlanModel.tsp:78:3` | 1       | 1        | Exact route/verb and source coordinates |

Disposition: No TypeSpec rule update required for the approved common-SDK contract; not serialized-ID equivalence.

## DesktopVirtualization

Project: `specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/DesktopVirtualization`; API version: `2026-04-01-preview`.

Raw Swagger / TypeSpec: **0 / 1**. Signed TypeSpec minus Swagger: 1; absolute gap: 1; relative gap: 1.

| Exact HTTP target                                                                                                                                                                                                   | Common owner / method; source                                                   | Swagger | TypeSpec | Identity                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------- | -------- | --------------------------------------- |
| `POST /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools/{hostPoolName}/sessionHosts/{sessionHostName}/listSingleSessionHostRegistrationTokens` | `SessionHosts.listSingleSessionHostRegistrationTokens`; `SessionHost.tsp:128:3` | 0       | 1        | Exact route/verb and source coordinates |

Disposition: No TypeSpec rule update required for the approved common-SDK contract; not serialized-ID equivalence.

## FileShares

Project: `specification/fileshares/resource-manager/Microsoft.FileShares/FileShares`; API version: `2026-06-01`.

Raw Swagger / TypeSpec: **0 / 4**. Signed TypeSpec minus Swagger: 4; absolute gap: 4; relative gap: 1.

| Exact HTTP target                                                                                                                                              | Common owner / method; source                                                | Swagger | TypeSpec | Identity                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------- | -------- | --------------------------------------- |
| `GET /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FileShares/fileShares/{resourceName}/fileShareSnapshots/{name}`    | `FileShareSnapshots.getFileShareSnapshot`; `fileshares.tsp:346:3`            | 0       | 1        | Exact route/verb and source coordinates |
| `PUT /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FileShares/fileShares/{resourceName}/fileShareSnapshots/{name}`    | `FileShareSnapshots.createOrUpdateFileShareSnapshot`; `fileshares.tsp:354:3` | 0       | 1        | Exact route/verb and source coordinates |
| `PATCH /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FileShares/fileShares/{resourceName}/fileShareSnapshots/{name}`  | `FileShareSnapshots.updateFileShareSnapshot`; `fileshares.tsp:364:3`         | 0       | 1        | Exact route/verb and source coordinates |
| `DELETE /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FileShares/fileShares/{resourceName}/fileShareSnapshots/{name}` | `FileShareSnapshots.deleteFileShareSnapshot`; `fileshares.tsp:377:3`         | 0       | 1        | Exact route/verb and source coordinates |

Disposition: No TypeSpec rule update required for the approved common-SDK contract; not serialized-ID equivalence.

## Network

Project: `specification/network/resource-manager/Microsoft.Network/Network/Network`; API version: `2026-03-01`.

Raw Swagger / TypeSpec: **154 / 11**. Signed TypeSpec minus Swagger: -143; absolute gap: 143; relative gap: 0.9285714285714286.

| Exact HTTP target                                                                                                                                                                                                                                                        | Common owner / method; source                                                                             | Swagger | TypeSpec | Identity                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- | ------- | -------- | --------------------------------------- |
| `POST /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/effectiveRoutes`                                                                                                                       | `VirtualHubs.getEffectiveVirtualHubRoutes`; `VirtualHub.tsp:166:3`                                        | 10      | 1        | Exact route/verb and source coordinates |
| `POST /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/disconnectVirtualNetworkGatewayVpnConnections`                                                                   | `VirtualNetworkGateways.disconnectVirtualNetworkGatewayVpnConnections`; `VirtualNetworkGateway.tsp:496:3` | 9       | 1        | Exact route/verb and source coordinates |
| `GET /subscriptions/{subscriptionId}/providers/Microsoft.Network/locations/{location}/autoApprovedPrivateLinkServices`                                                                                                                                                   | `PrivateLinkServices.listAutoApprovedPrivateLinkServices`; `routes.tsp:484:3`                             | 15      | 1        | Exact route/verb and source coordinates |
| `POST /subscriptions/{subscriptionId}/providers/Microsoft.Network/locations/{location}/checkPrivateLinkServiceVisibility`                                                                                                                                                | `PrivateLinkServices.checkPrivateLinkServiceVisibility`; `routes.tsp:456:3`                               | 15      | 1        | Exact route/verb and source coordinates |
| `GET /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/locations/{location}/autoApprovedPrivateLinkServices`                                                                                                                | `PrivateLinkServices.listAutoApprovedPrivateLinkServicesByResourceGroup`; `routes.tsp:498:3`              | 15      | 1        | Exact route/verb and source coordinates |
| `POST /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/locations/{location}/checkPrivateLinkServiceVisibility`                                                                                                             | `PrivateLinkServices.checkPrivateLinkServiceVisibilityByResourceGroup`; `routes.tsp:469:3`                | 15      | 1        | Exact route/verb and source coordinates |
| `GET /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.Compute/cloudServices/{cloudServiceName}/networkInterfaces`                                                                                                                  | `NetworkInterfaces.listCloudServiceNetworkInterfaces`; `routes.tsp:259:3`                                 | 15      | 1        | Exact route/verb and source coordinates |
| `GET /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.Compute/cloudServices/{cloudServiceName}/publicipaddresses`                                                                                                                  | `PublicIPAddresses.listCloudServicePublicIPAddresses`; `routes.tsp:277:3`                                 | 15      | 1        | Exact route/verb and source coordinates |
| `GET /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.Compute/cloudServices/{cloudServiceName}/roleInstances/{roleInstanceName}/networkInterfaces`                                                                                 | `NetworkInterfaces.listCloudServiceRoleInstanceNetworkInterfaces`; `NetworkInterface.tsp:70:3`            | 15      | 1        | Exact route/verb and source coordinates |
| `GET /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.Compute/cloudServices/{cloudServiceName}/roleInstances/{roleInstanceName}/networkInterfaces/{networkInterfaceName}`                                                          | `NetworkInterfaces.getCloudServiceNetworkInterface`; `NetworkInterface.tsp:55:3`                          | 15      | 1        | Exact route/verb and source coordinates |
| `GET /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.Compute/cloudServices/{cloudServiceName}/roleInstances/{roleInstanceName}/networkInterfaces/{networkInterfaceName}/ipconfigurations/{ipConfigurationName}/publicipaddresses` | `PublicIPAddresses.listCloudServiceRoleInstancePublicIPAddresses`; `PublicIPAddress.tsp:102:3`            | 15      | 1        | Exact route/verb and source coordinates |

Disposition: No TypeSpec rule update required for the approved common-SDK contract; not serialized-ID equivalence.

## Vmss

Project: `specification/network/resource-manager/Microsoft.Network/Network/Vmss`; API version: `2018-10-01`.

Raw Swagger / TypeSpec: **5 / 3**. Signed TypeSpec minus Swagger: -2; absolute gap: 2; relative gap: 0.4.

| Exact HTTP target                                                                                                                                                                                                                                                                                 | Common owner / method; source                                                                    | Swagger | TypeSpec | Identity                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------- | -------- | --------------------------------------- |
| `GET /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/networkInterfaces`                                                                                                                       | `NetworkInterfacesOperationGroup.listVirtualMachineScaleSetNetworkInterfaces`; `routes.tsp:50:3` | 1       | 0        | Exact route/verb and source coordinates |
| `GET /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/publicipaddresses`                                                                                                                       | `PublicIPAddressesOperationGroup.listVirtualMachineScaleSetPublicIPAddresses`; `routes.tsp:76:3` | 1       | 0        | Exact route/verb and source coordinates |
| `GET /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines/{virtualmachineIndex}/networkInterfaces`                                                                                 | `NetworkInterfaces.listVirtualMachineScaleSetVMNetworkInterfaces`; `NetworkInterface.tsp:71:3`   | 1       | 1        | Exact route/verb and source coordinates |
| `GET /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines/{virtualmachineIndex}/networkInterfaces/{networkInterfaceName}`                                                          | `NetworkInterfaces.getVirtualMachineScaleSetNetworkInterface`; `NetworkInterface.tsp:35:3`       | 1       | 1        | Exact route/verb and source coordinates |
| `GET /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines/{virtualmachineIndex}/networkInterfaces/{networkInterfaceName}/ipconfigurations/{ipConfigurationName}/publicipaddresses` | `PublicIPAddresses.listVirtualMachineScaleSetVMPublicIPAddresses`; `PublicIPAddress.tsp:83:3`    | 1       | 1        | Exact route/verb and source coordinates |

Disposition: No TypeSpec rule update required for the approved common-SDK contract; not serialized-ID equivalence.

## resources

Project: `specification/resources/resource-manager/Microsoft.Resources/resources`; API version: `2025-04-01`.

Raw Swagger / TypeSpec: **4 / 3**. Signed TypeSpec minus Swagger: -1; absolute gap: 1; relative gap: 0.25.

| Exact HTTP target                                                                                     | Common owner / method; source                                | Swagger | TypeSpec | Identity                                |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ------- | -------- | --------------------------------------- |
| `GET /subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}/providerPermissions`       | `Providers.providerPermissions`; `routes.tsp:71:3`           | 1       | 0        | Exact route/verb and source coordinates |
| `POST /subscriptions/{subscriptionId}/resourcegroups/{sourceResourceGroupName}/moveResources`         | `Resources.moveResources`; `ResourceGroup.tsp:163:3`         | 1       | 1        | Explicit source-backed rename bridge    |
| `GET /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/resources`                    | `Resources.listByResourceGroup`; `ResourceGroup.tsp:125:3`   | 1       | 1        | Exact route/verb and source coordinates |
| `POST /subscriptions/{subscriptionId}/resourcegroups/{sourceResourceGroupName}/validateMoveResources` | `Resources.validateMoveResources`; `ResourceGroup.tsp:183:3` | 1       | 1        | Explicit source-backed rename bridge    |

Disposition: No TypeSpec rule update required for the approved common-SDK contract; not serialized-ID equivalence.
