"""Reproduce the manually reviewed current-source acceptance groups at 150e59ee."""
import collections
import hashlib
import json
from pathlib import Path
import sys

task = Path(__file__).resolve().parent.parent
observations = task / "refresh-20261105" / "source-attribution" / "observations.json"
data = json.loads(observations.read_text(encoding="utf-8"))
groups = {
    "narrower-bounds": {
        "ApiManagement": [12, 18, 28, 33],
    },
    "compatible-serialized-enums": {
        "WorkbooksApi": [0], "StackHCIVM": [8], "BillingBenefits": [11],
        "DynatraceObservability": [3], "HybridCompute": [3, 6], "NetApp": [41],
        "DBforPostgreSQL.Management": [12], "DataReplication": [5], "StorageCache": [4],
    },
    "partial-null-reset-or-secrecy-annotation": {
        "WorkbooksApi": [2], "CognitiveServices": [0, 2, 3], "HDInsight": [0],
        "extensions": [1], "fluxConfigurations": [5, 6, 7, 10, 11],
        "MachineLearningServices": [3, 6, 8, 12, 14, 17], "ManagementGroups": [0],
        "NetApp": [35],
    },
    "request-compatible-mutability-or-identifiers": {
        "ContainerApps": [3], "Kusto": [1], "DesktopVirtualization": [3, 4],
        "ElasticSan": [0, 1, 2, 3, 4, 6, 7], "HybridConnectivity": [1, 2],
        "NetworkCloud": [19, 21], "NetApp": [19, 28, 44],
        "DBforPostgreSQL.Management": [11, 13], "RecoveryServices": [0],
        "ServiceBus": [0], "StorageCache": [2, 7],
    },
    "compatible-partial-collections": {
        "Compute": [22], "RegistryTasks": [3, 4], "fleet": [3],
        "DesktopVirtualization": [1], "DeviceRegistry": [6, 7, 8, 12, 13],
        "HybridCompute": [7], "ManagedNetworkFabric": [3, 88, 92],
        "Mission": [5, 20], "NetworkCloud": [6, 7, 9], "ScVmm": [0, 1],
        "StorageDiscovery": [2],
    },
}
membership = {}
for group, projects in groups.items():
    for project, indices in projects.items():
        for index in indices:
            assert (project, index) not in membership
            membership[project, index] = group
records = []
for record in data["records"]:
    if record["swaggerFamily"] != "same-name-schema-inequality" or record["observation"] != "source-accepts":
        continue
    identity = (record["project"].split("/")[-1], record["diagnosticIndex"])
    group = membership.pop(identity)
    records.append({
        **{key: record[key] for key in ("project", "diagnosticIndex", "replayInputIndex", "replayOperationIndex", "replayReasonIndex", "sourceFile", "operationId", "name")},
        "reviewedCurrentSourceDisposition": group,
    })
assert not membership
assert len(records) == 79
result = {
    "candidateCommit": "150e59ee31e1043863d6316b9a3564743c0ca1a1",
    "boundary": "Manual semantic review grouped79 accepted current-source contracts. The script only verifies membership and aggregates preserved records. These are not79 matched harmless Swagger defects, historical-version dispositions or cross-engine normalized counts.",
    "observationsSha256": hashlib.sha256(observations.read_bytes()).hexdigest(),
    "groups": dict(sorted(collections.Counter(record["reviewedCurrentSourceDisposition"] for record in records).items())),
    "records": records,
}
output = Path(__file__).with_name("accepted-contracts.json")
encoded = json.dumps(result, indent=2) + "\n"
if "--check" in sys.argv:
    assert output.read_text(encoding="utf-8") == encoded
else:
    assert not output.exists()
    output.write_text(encoded, encoding="utf-8", newline="\n")
print(json.dumps(result["groups"], indent=2))
