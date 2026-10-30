import hashlib
import json
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1]).resolve()
bindings = json.loads((root / "replay" / "assessment-inputs.json").read_text(encoding="utf-8"))
for file, expected in bindings.items():
    if hashlib.sha256((root / file).read_bytes()).hexdigest() != expected:
        raise RuntimeError(f"Saved assessment input changed; renewed analysis/review required: {file}")
coverage = json.loads((root / "coverage.json").read_text(encoding="utf-8"))
comparison = json.loads((root / "receipts" / "combined-operation-comparison.json").read_text(encoding="utf-8"))
if coverage["unassessedProjects"] or comparison["comparable"]["missing"] or comparison["comparable"]["extra"]:
    raise RuntimeError("The saved assessment does not apply to unexplained gaps")
if coverage["selectedProjectCount"] != coverage["assessableProjectCount"]:
    raise RuntimeError("The saved assessment requires the complete population")
rows = comparison["rows"]
data_migration = next(row for row in rows if row["project"].endswith("/DataMigration"))
network = next(row for row in rows if row["project"].endswith("/Network/Network"))
values = {
    "selected": coverage["selectedProjectCount"],
    "rawSwagger": coverage["validatorRawCount"],
    "rawNative": coverage["nativeAlignedCount"],
    "comparableSwagger": comparison["comparable"]["swagger"],
    "comparableNative": comparison["comparable"]["native"],
    "swaggerHigher": comparison["swaggerHigherExcess"],
    "nativeHigher": comparison["nativeHigherExcess"],
    "absolute": comparison["totalAbsoluteDifference"],
    "equalProjects": comparison["equalRawCountProjects"],
    "dataMigrationSwagger": data_migration["validatorRawCount"],
    "dataMigrationNative": data_migration["nativeAlignedCount"],
    "networkSwagger": network["validatorRawCount"],
}
template = (root / "replay" / "migration-template.md").read_text(encoding="utf-8")
result = re.sub(r"\{\{(\w+)\}\}", lambda match: str(values[match[1]]), template)
if "{{" in result or "}}" in result:
    raise RuntimeError("Unresolved assessment-template token")
output = pathlib.Path(sys.argv[2])
output.write_bytes(result.encode("utf-8"))
print(json.dumps({"output": str(output), "sha256": hashlib.sha256(output.read_bytes()).hexdigest()}))
