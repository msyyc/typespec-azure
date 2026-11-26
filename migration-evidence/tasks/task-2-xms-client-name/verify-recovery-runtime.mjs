import { createHash } from "node:crypto";
import fs from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";
const [runtime, output] = process.argv.slice(2);
const closure = JSON.parse(
  fs.readFileSync(new URL("./recovery-runtime-closure.json", import.meta.url)),
);
const require = createRequire(path.join(runtime, "package.json"));
const hash = (data) => createHash("sha256").update(data).digest("hex");
const verified = [];
for (const item of closure.packages) {
  const names = require.resolve.paths(item.name) ?? [];
  const manifests = names.map((base) => path.join(base, item.name, "package.json"));
  let directory;
  for (const manifest of manifests) {
    if (fs.existsSync(manifest) && JSON.parse(fs.readFileSync(manifest)).version === item.version) {
      directory = path.dirname(manifest);
      break;
    }
  }
  if (!directory) {
    const store = path.join(runtime, "node_modules", ".pnpm");
    for (const entry of fs.readdirSync(store)) {
      const manifest = path.join(store, entry, "node_modules", item.name, "package.json");
      if (
        fs.existsSync(manifest) &&
        JSON.parse(fs.readFileSync(manifest)).version === item.version
      ) {
        directory = path.dirname(manifest);
        break;
      }
    }
  }
  if (!directory) throw Error(`Missing exact recorded package ${item.name}@${item.version}`);
  for (const file of item.files) {
    const actual = fs.readFileSync(path.join(directory, file.file));
    if (actual.length !== file.bytes || hash(actual) !== file.sha256) {
      throw Error(`Changed recovered bytes: ${item.name}@${item.version}/${file.file}`);
    }
  }
  verified.push({ name: item.name, version: item.version, files: item.files.length });
}
fs.writeFileSync(
  output,
  JSON.stringify({ status: "passed", packages: verified, candidateRoots: closure.roots }, null, 2) +
    "\n",
);
console.log(JSON.stringify({ status: "passed", packages: verified.length }));
