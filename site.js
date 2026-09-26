import { works, seriesNames } from "./gallery-data.js";
import { CHANNEL_STORAGE_KEY, createPrompt, normalizeChannel } from "./gallery-prompts.js";

const grid = document.querySelector("#gallery-grid");
const count = document.querySelector("#work-count");
const empty = document.querySelector("#empty-state");
const sort = document.querySelector("#sort-order");
const filters = [...document.querySelectorAll(".filter")];
const dialog = document.querySelector("#artwork-dialog");
let activeSeries = "all";
let imageRequestId = 0;
let currentWork = null;
let promptRevision = 0;
const copyTimers = new Map();
let promptChannel = "web";
try {
  promptChannel = normalizeChannel(localStorage.getItem(CHANNEL_STORAGE_KEY));
} catch {
  // Privacy modes may block storage; the in-memory choice still works.
}

function resetCopyState() {
  promptRevision += 1;
  for (const timer of copyTimers.values()) clearTimeout(timer);
  copyTimers.clear();
  document.querySelector("#copy-status").textContent = "";
  document.querySelector("#reference-copy-status").textContent = "";
}

function updatePrompts() {
  resetCopyState();
  if (!currentWork) return;
  document.querySelector("#dialog-prompt-text").textContent = createPrompt(currentWork.brief, promptChannel);
  document.querySelector("#reference-prompt-text").textContent = createPrompt(currentWork.brief, promptChannel, true);
  document.querySelectorAll('input[name="prompt-channel"]').forEach((input) => {
    input.checked = input.value === promptChannel;
  });
  document.querySelector("#prompt-channel-help").textContent = promptChannel === "web"
    ? "无需安装 Skill。复制提示词，在 ChatGPT、Gemini 等网页中选择图片生成功能后发送；链接读不到时，可下载指南并上传。"
    : "适合已安装 card-creator 的 Codex 等工具。复制提示词，在已识别该 Skill 且支持图片生成或编辑的对话中发送。";
  document.querySelector("#guide-download").hidden = promptChannel !== "web";
}

async function copyPrompt(textId, statusId) {
  const revision = promptRevision;
  const text = document.querySelector(textId);
  const status = document.querySelector(statusId);
  clearTimeout(copyTimers.get(statusId));
  try {
    await navigator.clipboard.writeText(text.textContent);
    if (revision !== promptRevision || !dialog.open) return;
    status.textContent = "已复制 ✓";
    copyTimers.set(statusId, setTimeout(() => {
      if (revision === promptRevision) status.textContent = "";
    }, 1800));
  } catch {
    if (revision !== promptRevision || !dialog.open) return;
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(text);
    selection?.removeAllRanges();
    selection?.addRange(range);
    status.textContent = "复制失败，已选中提示，请手动复制";
  }
}

function imageUrl(work, alternate = false) {
  return `./examples/${alternate ? work.alternate : work.image}`;
}

function render() {
  const visible = works.filter((work) => activeSeries === "all" || work.series === activeSeries);
  if (sort.value === "newest") visible.sort((a, b) => Date.parse(b.publishedAt) - Date.parse(a.publishedAt));
  if (sort.value === "title") visible.sort((a, b) => a.title.localeCompare(b.title, "zh-CN"));
  count.textContent = `${visible.length} 件作品`;
  empty.hidden = visible.length !== 0;
  grid.replaceChildren(...visible.map(createCard));
}

function createCard(work) {
  const card = document.createElement("article");
  card.className = "work-card";
  const preview = document.createElement("button");
  preview.type = "button";
  preview.className = "work-preview";
  preview.classList.toggle("is-portrait", work.orientation === "portrait");
  preview.setAttribute("aria-label", `查看${work.title}卡面`);
  preview.addEventListener("click", () => openWork(work));
  const picture = document.createElement("img");
  picture.src = imageUrl(work);
  picture.alt = `${work.title}，${work.subtitle}`;
  picture.loading = "lazy";
  picture.decoding = "async";
  preview.append(picture);
  const info = document.createElement("div");
  info.className = "work-info";
  const labels = document.createElement("div");
  const title = document.createElement("h3");
  title.textContent = work.title;
  const subtitle = document.createElement("p");
  subtitle.textContent = work.subtitle;
  labels.append(title, subtitle);
  const download = document.createElement("a");
  download.className = "card-download";
  download.href = imageUrl(work);
  download.download = work.image;
  download.title = `下载${work.title}原图`;
  download.setAttribute("aria-label", `下载${work.title}原图`);
  download.textContent = "↓";
  info.append(labels, download);
  card.append(preview, info);
  return card;
}

async function openWork(work) {
  const requestId = ++imageRequestId;
  const image = document.querySelector("#dialog-image");
  const imageStatus = document.querySelector("#dialog-image-status");
  image.hidden = true;
  imageStatus.textContent = "正在加载图片…";
  imageStatus.hidden = false;
  document.querySelector("#dialog-title").textContent = work.title;
  document.querySelector("#dialog-subtitle").textContent = work.subtitle;
  document.querySelector("#dialog-series").textContent = seriesNames[work.series];
  currentWork = work;
  updatePrompts();
  document.querySelector("#original-prompt-text").textContent = work.prompt;
  document.querySelector("#original-prompt").open = false;
  document.querySelector("#reference-creation").open = false;
  const reference = document.querySelector("#reference-download");
  reference.href = imageUrl(work);
  reference.download = work.image;
  document.querySelector("#dialog-origin").textContent = work.origin || "AI 风格化创作示例；标志并非官方制图或授权版本。";
  const download = document.querySelector("#dialog-download");
  download.href = imageUrl(work);
  download.download = work.image;
  const alternate = document.querySelector("#dialog-alternate");
  alternate.hidden = !work.alternate;
  if (work.alternate) {
    alternate.href = imageUrl(work, true);
    alternate.download = work.alternate;
  }
  dialog.showModal();

  const nextImage = new Image();
  nextImage.id = "dialog-image";
  nextImage.dataset.orientation = work.orientation || "landscape";
  nextImage.alt = `${work.title}，${work.subtitle}`;
  nextImage.src = imageUrl(work);
  try {
    await nextImage.decode();
    if (requestId !== imageRequestId || !dialog.open) return;
    image.replaceWith(nextImage);
    imageStatus.hidden = true;
  } catch {
    if (requestId === imageRequestId && dialog.open) imageStatus.textContent = "图片加载失败，请关闭后重试";
  }
}

filters.forEach((button) => button.addEventListener("click", () => {
  activeSeries = button.dataset.series;
  filters.forEach((filter) => {
    const selected = filter === button;
    filter.classList.toggle("is-active", selected);
    filter.setAttribute("aria-pressed", String(selected));
  });
  render();
}));
sort.addEventListener("change", render);
document.querySelector("#show-all").addEventListener("click", () => filters[0].click());
document.querySelector("#dialog-close").addEventListener("click", () => dialog.close());
dialog.addEventListener("close", () => {
  imageRequestId += 1;
  resetCopyState();
  currentWork = null;
  document.querySelector("#dialog-image").hidden = true;
  document.querySelector("#dialog-image-status").hidden = true;
});
dialog.addEventListener("click", (event) => { if (event.target === dialog) dialog.close(); });
document.querySelectorAll('input[name="prompt-channel"]').forEach((input) => {
  input.addEventListener("change", () => {
    promptChannel = normalizeChannel(input.value);
    try { localStorage.setItem(CHANNEL_STORAGE_KEY, promptChannel); } catch { /* session-only */ }
    updatePrompts();
  });
});
document.querySelector("#copy-prompt").addEventListener("click", () => copyPrompt("#dialog-prompt-text", "#copy-status"));
document.querySelector("#copy-reference-prompt").addEventListener("click", () => copyPrompt("#reference-prompt-text", "#reference-copy-status"));
document.querySelector(".hero-preview").addEventListener("click", (event) => {
  const work = works.find((item) => item.id === event.currentTarget.dataset.open);
  if (work) openWork(work);
});
render();
