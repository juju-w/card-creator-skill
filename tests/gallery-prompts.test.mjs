import assert from "node:assert/strict";
import test from "node:test";
import { createPrompt, normalizeChannel, WEB_GUIDE_URL } from "../gallery-prompts.js";
import { works } from "../gallery-data.js";

test("each public work has a standalone brief and its original prompt", () => {
  assert.equal(new Set(works.map(w => w.id)).size, works.length);
  for (const work of works) {
    assert.ok(work.brief?.trim(), work.id);
    assert.ok(work.prompt?.trim(), work.id);
    assert.doesNotMatch(work.brief, /https?:|@创建|card-creator Skill/);
    const web = createPrompt(work.brief, "web");
    const installed = createPrompt(work.brief, "installed");
    assert.ok(web.includes(WEB_GUIDE_URL));
    assert.ok(web.endsWith(work.brief));
    assert.equal(installed, `使用 card-creator Skill，${work.brief}`);
    assert.doesNotMatch(installed, /https?:/);
  }
});

test("reference prompts require an uploaded image and share the selected entry", () => {
  for (const channel of ["web", "installed"]) {
    const text = createPrompt("unused creative brief", channel, true);
    assert.ok(text.includes("我上传的卡面"));
    assert.ok(text.includes("【你的主题】"));
    assert.ok(text.includes("未提到的部分保持"));
    assert.equal(text.includes(WEB_GUIDE_URL), channel === "web");
    assert.ok(!text.includes("unused creative brief"));
  }
});

test("invalid or missing stored preferences default to Web", () => {
  for (const value of [null, undefined, "", "broken"]) assert.equal(normalizeChannel(value), "web");
  assert.equal(normalizeChannel("installed"), "installed");
});

test("curated briefs do not rewrite the user's historical spelling", () => {
  const work = works.find(w => w.id === "chatgpt-metagross-icbc-mastercard-world");
  assert.ok(work.prompt.includes("万事达 word"));
  assert.ok(work.brief.includes("Mastercard World"));
});
