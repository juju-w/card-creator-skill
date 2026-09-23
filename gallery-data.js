// One primary series per featured card face; images remain in examples/ for Pages and GitHub.
export const seriesNames = {
  art: "艺术风格",
  modern: "现代设计",
  pokemon: "宝可梦",
  city: "城市",
  anime: "二次元",
  meme: "玩梗",
};

export const works = [
  { id: "monet-water-lilies-visa", title: "睡莲印象派", subtitle: "珠光水面 × Visa", series: "art", image: "monet-water-lilies-visa.png", prompt: "使用 card-creator Skill，生成一张睡莲印象派卡面：蓝紫水面、少量珠光，右下角银白 Visa。" },
  { id: "klimt-gold-mastercard", title: "金箔装饰画", subtitle: "旋涡枝蔓 × Mastercard", series: "art", image: "klimt-gold-mastercard.png", prompt: "使用 card-creator Skill，生成一张金箔装饰画卡面：旋涡枝蔓、宝石色点缀，右下角金线 Mastercard。" },
  { id: "morandi-still-life-wise", title: "莫兰迪静物", subtitle: "灰粉陶器 × WISE", series: "modern", image: "morandi-still-life-wise.png", alternate: "morandi-still-life.png", prompt: "使用 card-creator Skill，生成一张莫兰迪风格的三件陶器静物卡面：灰粉、燕麦与鼠尾草绿，右下角加低调的 WISE 字标。" },
  { id: "hsbc-geometric-hong-kong", title: "折面之城", subtitle: "红白几何 × 汇丰", series: "modern", image: "hsbc-geometric-hong-kong.png", prompt: "使用 card-creator Skill，生成一张汇丰风格的红白几何卡面：折纸般的三角切面与香港天际线，右上角汇丰标志，不要角色、芯片或多余文字。" },
  { id: "apple-cash-iridescent-ribbon", title: "虹彩流线", subtitle: "黑曜石 × Apple Cash", series: "modern", image: "apple-cash-iridescent-ribbon-opaque.png", prompt: "使用 card-creator Skill，生成一张 Apple Cash 风格卡面：黑曜石底色、一条薄荷银紫色虹彩丝带，右下角白色 Apple Cash 标志，极简且不要芯片。" },
  { id: "mucha-art-nouveau-octopus", title: "新艺术花卉", subtitle: "复古纸感 × 八达通", series: "art", image: "mucha-art-nouveau-octopus.png", prompt: "使用 card-creator Skill，生成一张穆夏新艺术风格卡面：花卉人物、复古纸感，右下角古铜色八达通。" },
  { id: "hokusai-wave-suica", title: "浮世绘海浪", subtitle: "远山与浪 × Suica", series: "art", image: "hokusai-wave-suica.png", prompt: "使用 card-creator Skill，生成一张浮世绘海浪与远处富士山的卡面，右下角深蓝 Suica。" },
  { id: "song-blue-green-unionpay", title: "青绿山水", subtitle: "矿物色与云母 × 银联", series: "art", image: "song-blue-green-unionpay.png", prompt: "使用 card-creator Skill，生成一张宋画青绿山水卡面：矿物颜料、云母云雾，右下角金蓝风格化银联。" },
  { id: "vienna-secession-diners", title: "维也纳分离派", subtitle: "黑金人物 × Diners Club", series: "art", image: "vienna-secession-diners.png", prompt: "使用 card-creator Skill，生成一张维也纳分离派风格的黑金高级艺术卡面，右下角哑金 Diners Club。" },
  { id: "post-impressionist-visa", title: "旋涡夜景", subtitle: "后印象派 × Visa", series: "art", image: "post-impressionist-visa.png", prompt: "使用 card-creator Skill，生成一张深蓝旋涡夜空的后印象派卡面，右下角哑金 Visa。" },
  { id: "chatgpt-gardevoir-cmb-unionpay", title: "超能系粉色", subtitle: "沙奈朵 × 招商银行 × 银联", series: "pokemon", image: "chatgpt-gardevoir-cmb-unionpay.png", origin: "用户分享的 ChatGPT 网页成图；无法确认当时是否加载了 Skill。", prompt: "使用 [juju-w/card-creator-skill](https://github.com/juju-w/card-creator-skill) card-creator Skill @创建图像 ，生成一张宝可梦里沙奈朵的卡面，简洁，超能系粉色， 招商银行银联信用卡，不要芯片" },
  { id: "chatgpt-metagross-icbc-mastercard-world", title: "青色云母金属", subtitle: "巨金怪 × 工商银行 × Mastercard", series: "pokemon", image: "chatgpt-metagross-icbc-mastercard-world.png", origin: "用户分享的 ChatGPT 网页成图；原始 Prompt 中的 word 保持原样，无法确认当时是否加载了 Skill。", prompt: "@创建图像 使用 [juju-w/card-creator-skill](https://github.com/juju-w/card-creator-skill) card-creator Skill  ，生成一张宝可梦里巨金怪的万事达 word 卡面，工商银行，不要芯片，万事达logo 不要颜色只保留线条，整体有云母/金属光泽，保持青色系" },
  { id: "gemini-magikarp-icoca", title: "水边的鲤鱼王", subtitle: "简洁海蓝 × ICOCA", series: "pokemon", image: "gemini-magikarp-icoca.jpeg", origin: "用户分享的 Gemini 成图；标志为生成图里的非官方诠释。", prompt: "使用 card-creator Skill，生成一张鲤鱼王 × ICOCA 卡面：简洁，右下角 ICOCA。" },
  { id: "gemini-gengar-octopus", title: "紫色耿鬼", subtitle: "夜色科技 × 八达通", series: "pokemon", image: "gemini-gengar-octopus.jpeg", origin: "用户分享的 Gemini 成图；紫色标志为生成图里的非官方诠释。", prompt: "使用 card-creator Skill，生成一张耿鬼 × 八达通卡面，让八达通 Logo 变成与画面匹配的紫色。" },
  { id: "chiikawa-suica", title: "四叶草草地", subtitle: "清新水彩 × Suica", series: "anime", image: "chiikawa-suica.png", prompt: "使用 card-creator Skill，生成一张清新水彩风 Chiikawa × Suica 卡面，右下角 Suica。" },
  { id: "huashan-ink-tunion", title: "华山水墨", subtitle: "山水留白 × 交通联合", series: "art", image: "huashan-ink-tunion.png", prompt: "使用 card-creator Skill，生成一张华山水墨画风格的交通卡面，右下角交通联合。" },
  { id: "guangzhou-minimal-lingnantong-tunion", title: "广州极简线条", subtitle: "珠江曲线 × 岭南通 × 交通联合", series: "city", image: "guangzhou-minimal-lingnantong-tunion-v2.png", prompt: "使用 card-creator Skill，生成一张广州极简线条卡面：暖白纸底，广州塔、珠江曲线与木棉花，包含岭南通和交通联合。" },
  { id: "palace-museum-cranes-unionpay", title: "北京 · 故宫典藏", subtitle: "云母祥云与仙鹤", series: "city", image: "palace-museum-cranes-unionpay.png", prompt: "使用 card-creator Skill，生成一张北京故宫典藏风卡面，使用云母祥云、仙鹤、宫殿和哑金风格化标志。" },
  { id: "shanghai-art-deco-unionpay", title: "上海装饰艺术", subtitle: "外滩扇面 × 深翡翠银联", series: "city", image: "shanghai-art-deco-unionpay-v2.png", prompt: "使用 card-creator Skill，生成一张上海装饰艺术卡面：深翡翠底、古金扇面、外滩钟楼与江面倒影，右下角哑金短款银联。" },
  { id: "minimal-mastercard", title: "一笔成线", subtitle: "暖象牙白 × Mastercard", series: "modern", image: "minimal-mastercard.png", prompt: "使用 card-creator Skill，生成一张暖象牙白的极简线条 Mastercard 卡面，右下角 Mastercard。" },
];
