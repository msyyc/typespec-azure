import assert from "node:assert/strict";
import { test } from "node:test";
import { compareUnits, expand } from "./compare-member-operation-units.mjs";
const project = "specification/example/resource-manager/Example/Service";
const route = "/subscriptions/{subId}/resourceGroups/{groupName}/widgets";
const group = "PathContainsResourceGroup";
const subscription = "PathContainsSubscriptionId";
test("expands eligible methods and keeps two independent policies at a shared operation", () => {
  const units = expand(project, route, ["get", "put", "post", "head"], [group, subscription]);
  assert.equal(units.length, 4);
  assert.deepEqual(compareUnits(units, units), { swagger: 4, native: 4, missing: [], extra: [] });
});
test("rejects wrong-but-equal member counts at the exact same path and method", () => {
  const comparison = compareUnits(expand(project, route, ["get"], [group]), expand(project, route, ["get"], [subscription]));
  assert.equal(comparison.swagger, comparison.native);
  assert.equal(comparison.missing.length, 1);
  assert.equal(comparison.extra.length, 1);
});
test("detects one missing member instead of collapsing a shared source target", () => {
  const comparison = compareUnits(expand(project, route, ["get"], [group, subscription]), expand(project, route, ["get"], [group]));
  assert.equal(comparison.missing.length, 1);
  assert.ok(comparison.missing[0].includes(subscription));
});
test("does not fuzz case-preserved full paths or silently collapse duplicate units", () => {
  const units = expand(project, route, ["get"], [group]);
  assert.equal(compareUnits(units, expand(project, route.toLowerCase(), ["get"], [group])).missing.length, 1);
  assert.throws(() => compareUnits([...units, ...units], units), /Duplicate actionable/);
});
