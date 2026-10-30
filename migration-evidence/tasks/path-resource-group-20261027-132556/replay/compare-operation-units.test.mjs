import assert from "node:assert/strict";
import { test } from "node:test";
import { compareUnits, expandMethods } from "./compare-operation-units.mjs";

test("one diagnosed path covers all four eligible operations, not POST or HEAD", () => {
  assert.equal(
    expandMethods("p", "/resourceGroups/{g}", [
      "get",
      "put",
      "patch",
      "delete",
      "post",
      "head",
    ]).length,
    4,
  );
});

test("exact operation agreement has no missing or extra units", () => {
  const units = expandMethods("p", "/resourceGroups/{g}", ["get", "put"]);
  assert.deepEqual(compareUnits(units, [...units]), {
    swagger: 2,
    native: 2,
    missing: [],
    extra: [],
  });
});

test("equal totals cannot hide a missing operation and an extra operation", () => {
  const left = expandMethods("p", "/resourceGroups/{g}/a", ["get", "put"]);
  const right = [
    ...expandMethods("p", "/resourceGroups/{g}/a", ["get"]),
    ...expandMethods("p", "/resourceGroups/{g}/b", ["put"]),
  ];
  const result = compareUnits(left, right);
  assert.equal(result.swagger, result.native);
  assert.equal(result.missing.length, 1);
  assert.equal(result.extra.length, 1);
});

test("missing eligible method remains a missing check", () => {
  const result = compareUnits(
    expandMethods("p", "/a", ["get", "put"]),
    expandMethods("p", "/a", ["get"]),
  );
  assert.equal(result.missing.length, 1);
  assert.equal(result.extra.length, 0);
});

test("project and full case-preserved path prevent name collisions", () => {
  const left = [
    ...expandMethods("p", "/a/{groupName}", ["get"]),
    ...expandMethods("q", "/a/{groupName}", ["get"]),
  ];
  const right = [
    ...expandMethods("p", "/a/{groupName}", ["get"]),
    ...expandMethods("q", "/A/{groupName}", ["get"]),
  ];
  assert.equal(compareUnits(left, right).missing.length, 1);
});

test("native aliases sharing one path and verb must not be silently deduplicated", () => {
  const units = expandMethods("p", "/a", ["get"]);
  assert.throws(
    () => compareUnits(units, [...units, ...units]),
    /Distinct native operations collide/,
  );
});

test("ambiguous Swagger path and method owners must not be silently deduplicated", () => {
  const units = expandMethods("p", "/a", ["get"]);
  assert.throws(
    () => compareUnits([...units, ...units], units),
    /Ambiguous Swagger/,
  );
});

test("full query-suffixed route identity is retained", () => {
  const left = expandMethods("p", "/a?mode=one", ["get"]);
  const right = expandMethods("p", "/a?mode=two", ["get"]);
  assert.equal(compareUnits(left, right).missing.length, 1);
  assert.equal(compareUnits(left, right).extra.length, 1);
});
