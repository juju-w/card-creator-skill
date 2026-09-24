// One creative brief, two invocation surfaces. Historical prompts stay untouched.
export const WEB_GUIDE_URL = "https://raw.githubusercontent.com/juju-w/card-creator-skill/main/web/card-creator.md";
export const CHANNEL_STORAGE_KEY = "card-creator.prompt-channel";

export function normalizeChannel(value) {
  return value === "installed" ? "installed" : "web";
}

export function createPrompt(brief, channel, reference = false) {
  const request = reference
    ? "参考我上传的卡面，保留版式和质感，把主体改成【你的主题】；未提到的部分保持。"
    : brief;
  return normalizeChannel(channel) === "installed"
    ? `使用 card-creator Skill，${request}`
    : `请先读取并遵循 ${WEB_GUIDE_URL} ，然后用图片生成功能${reference ? "修改" : "创作"}卡面：${request}`;
}
