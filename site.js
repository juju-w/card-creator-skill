import { works, seriesNames } from "./gallery-data.js";

const grid = document.querySelector("#gallery-grid");
const count = document.querySelector("#work-count");
const empty = document.querySelector("#empty-state");
const sort = document.querySelector("#sort-order");
const filters = [...document.querySelectorAll(".filter")];
const dialog = document.querySelector("#artwork-dialog");
let activeSeries = "all";

function imageUrl(work, alternate = false) {
  return `./examples/${alternate ? work.alternate : work.image}`;
}

function render() {
  const visible = works.filter((work) => activeSeries === "all" || work.series.includes(activeSeries));
  if (sort.value === "newest") visible.reverse();
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

function openWork(work) {
  const image = document.querySelector("#dialog-image");
  image.src = imageUrl(work);
  image.alt = `${work.title}，${work.subtitle}`;
  document.querySelector("#dialog-title").textContent = work.title;
  document.querySelector("#dialog-subtitle").textContent = work.subtitle;
  document.querySelector("#dialog-series").textContent = work.series.map((key) => seriesNames[key]).join(" / ");
  document.querySelector("#dialog-prompt-text").textContent = work.prompt;
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
dialog.addEventListener("click", (event) => { if (event.target === dialog) dialog.close(); });
document.querySelector("#copy-prompt").addEventListener("click", async (event) => {
  try {
    await navigator.clipboard.writeText(document.querySelector("#dialog-prompt-text").textContent);
    event.currentTarget.textContent = "已复制 ✓";
    setTimeout(() => { event.currentTarget.textContent = "复制 Prompt"; }, 1800);
  } catch {
    event.currentTarget.textContent = "复制失败，请手动选择";
  }
});
document.querySelector(".hero-preview").addEventListener("click", () => openWork(works[0]));
render();
