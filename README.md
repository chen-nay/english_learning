<div align="center">

<img src="img/learn-v3-soft-book.png" alt="English Learning" width="110">

# English Learning · 英语学习助手 💻🚀

一个面向开发者的**纯静态**英语学习工具：掌握软件专业术语、练习真实出国场景对话、辨析形近意近词汇、突破雅思核心词汇。

**[👉 在线体验 · Live Demo](https://chen-nay.github.io/english_learning)**

[![Live Demo](https://img.shields.io/badge/demo-online-brightgreen)](https://chen-nay.github.io/english_learning)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![No Build](https://img.shields.io/badge/build-none-lightgrey)
![Dependencies](https://img.shields.io/badge/dependencies-0-success)

</div>

---

> **关于内容来源**
> 1. 除「场景对话（Dialogue）」中的部分对话取材自书籍《English Conversation Premium》外，其余英语内容均由 AI 生成。
> 2. 本项目所有代码（包括本篇 README）均由 AI 生成。

## ✨ 项目简介

- **零依赖**：单个 `index.html` 承载全部 HTML / CSS / JS，无框架、无构建、无后端。
- **数据即文件**：所有词汇与对话都是静态 `.json`，可自由增删、二次分发。
- **开箱即用**：已部署在 GitHub Pages，打开即用；也可一条命令在本地跑起来。
- **响应式**：桌面 / 平板 / 手机自适应，窄屏自动收起侧边栏。

## 📚 功能模块

| 模块 | 内容量 | 说明 |
| --- | --- | --- |
| 💾 **专业词汇 Software Words** | 8 大分类 · 约 620 词 | 架构设计、前后端、代码逻辑、测试调试、版本控制、流程方法、职场动词短语等。每张卡片含音标、中文释义、同义词、中英双语例句。 |
| 💬 **场景对话 Dialogue** | 4 个场景 · 34 组对话 | 机场（值机 / 转机 / 安检…）、酒店、订餐、日常社交。聊天气泡式排版，`**加粗**` 短语高亮，右侧「Key Structures」讲解重点句型。 |
| ⚖️ **易混词辨析 Similar Words** | 53 组对比卡 · 122 个不同单词 | 按拼写接近、工作用词、专业概念、同词根和相似词缀分组；每组 2–4 词，含音标、词性、双语用法和辨析提示。 |
| 📘 **雅思核心词汇 IELTS** | 2000+ 词 | 每词含美式音标、中文释义（词性自动上色）、常用词组、中英双语例句。顶部 A–Z 字母导航 + 关键词搜索。 |
| 📒 **Word Notebook** | 37 个条目 · 持续追加 | 统一保存单词、短语和句型。每条一张紧凑卡片，默认显示美式音标、中文释义、搭配或结构和一条例句；点击 More details 在弹窗查看完整用法。 |

## 🎯 亮点功能

- **👁 自测模式**：专业词汇、对话和雅思模块通过右上角「小眼睛」隐藏详情，点击卡片或场景标题揭示。Similar Words 使用「逐词自测」按钮，保留英文、词性和音标，点击单词逐个显示或收起释义及用法；也可显示或收起整组，整组全部揭示后显示辨析提示。退出自测后显示全部内容，再次进入时重新隐藏。
- **🔊 真人发音**：基于浏览器原生 **Web Speech API**，点击 🔊 朗读单词或整句例句，优先选用 `en-US` 音色。
- **⭐ 学习进度（IELTS）**：支持「收藏」与「已掌握」标记，配合「全部 / 收藏 / 已掌握 / 未掌握」筛选与分页浏览。进度、当前页码、乱序开关全部保存在浏览器 `localStorage`。
- **🔀 固定乱序复习（IELTS）**：使用写死的种子（mulberry32）洗牌，**任何设备、任何浏览器打开顺序都一致**，可按页码接着上次继续学。
- **↔️ 可折叠侧边栏**：点击 Logo 旁箭头收起菜单，最大化学习区域。

## 📂 项目结构

```text
english_learning/
├── index.html                 # 唯一入口：全部 HTML/CSS/JS
├── source.json                # 数据源清单：登记 wordbook/ 与 dialogue/ 下的文件
├── img/
│   └── learn-v3-soft-book.png # Logo / favicon
├── wordbook/                  # 专业词汇（每个分类一个 .json）
│   ├── Architecture & Design.json
│   ├── Backend, Database & DevOps.json
│   └── ...
├── dialogue/                  # 场景对话
│   ├── airport.json
│   ├── conversation.json
│   ├── hotel.json
│   └── order.json
├── similarword/
│   └── similar_words.json     # 易混词分组
├── notebook/
│   ├── ADDING_ENTRIES.md       # 添加单词、短语和句型的约定
│   └── words.json             # 个人单词本，新条目放在数组最前面
├── ielts/
│   └── words.json             # 雅思词库（单文件，紧凑键名）
├── LICENSE
└── README.md
```

## 🚀 本地运行

项目是纯静态的。因浏览器安全策略会拦截本地 `file://` 下的 `fetch`，请用任意静态服务器打开：

```bash
# 方式一：Python（推荐，无需安装）
python3 -m http.server 9001
# 打开 http://localhost:9001

# 方式二：Node
npx serve .
```

## 🌐 部署

已托管于 **GitHub Pages**：<https://chen-nay.github.io/english_learning>

自行部署也很简单——由于是纯静态站点，把整个仓库根目录扔到任何静态托管（GitHub Pages / Vercel / Netlify / Nginx）即可，无需任何构建步骤。GitHub Pages 方式：仓库 `Settings → Pages → Build and deployment → Source: Deploy from a branch`，选择 `main` 分支、`/ (root)` 目录。

## ⚙️ 数据扩展

### 新增专业词汇 / 场景对话

1. 在 `wordbook/` 或 `dialogue/` 下新建 `.json`（格式见下）。
2. 把文件名登记到根目录 `source.json` 对应的数组里。
3. 刷新页面，顶部自动出现新分类。

**`wordbook/*.json`** —— 数组，每个元素：

```json
{
  "id": 1,
  "term": "Variable",
  "phonetic": "/ˈveriəbl/",
  "definition": "变量",
  "synonyms": "placeholder, identifier",
  "exampleEn": "You need to declare a global variable to store the user's session.",
  "exampleCn": "你需要声明一个全局变量来存储用户的会话信息。"
}
```

**`dialogue/*.json`** —— 数组，每个元素是一个场景。对话按索引奇偶左右分栏；`text` 里的 `**...**` 会渲染成高亮短语。`key_structures` 可选。

```json
{
  "scenario": "办理入住 (Check-in)，确认预定信息并提出房间偏好",
  "dialogue": [
    { "speaker": "Traveler", "text": "I have a **reservation under the name** Li Ming." },
    { "speaker": "Front Desk", "text": "Welcome. May I see your passport?" }
  ],
  "key_structures": [
    {
      "pattern": "...under the name [Name]",
      "example": "I have a reservation under the name Li Ming.",
      "explanation": "固定的预定话术，比 My name is... 更地道，适用于酒店、餐厅。"
    }
  ]
}
```

### 新增易混词 / 雅思词汇

这两个模块**不经过 `source.json`**，直接编辑对应单文件即可。

**`similarword/similar_words.json`** —— 数组，每个元素是一组对比卡。`category` 为 `spelling`（拼写）、`meaning`（工作用词）、`concept`（专业概念）、`family`（同词根）或 `suffix`（词缀），同类卡片使用相同的顶部色线。`title` 为组标题，`note` 为辨析提示。每组建议 2–5 词；同一单词可在不同的比较关系中重复出现，页面词数按不同单词统计。

```json
{
  "category": "spelling",
  "title": "adapt / adopt",
  "note": "adapt 强调调整以适应；adopt 强调开始采用，或收养。",
  "words": [
    { "en": "adapt", "phonetic": "/əˈdæpt/", "pos": "v.", "cn": "适应；改编；调整", "example": "adapt to a new environment", "exampleCn": "适应新环境" },
    { "en": "adopt", "phonetic": "/əˈdɑːpt/", "pos": "v.", "cn": "采用；收养", "example": "adopt a new approach", "exampleCn": "采用一种新方法" }
  ]
}
```

专业概念中的异步、序列化和幂等性说明参考 MDN 的 [Asynchronous](https://developer.mozilla.org/en-US/docs/Glossary/Asynchronous)、[Serialization](https://developer.mozilla.org/en-US/docs/Glossary/Serialization) 和 [Idempotent](https://developer.mozilla.org/en-US/docs/Glossary/Idempotent)；词卡中的双语用法为学习示例。

**`ielts/words.json`** —— 数组，紧凑键名：`w` 单词、`p` 音标、`m` 释义、`ph` 词组、`s` 例句。

```json
{
  "w": "abandon",
  "p": "əˈbændən",
  "m": "v. 放弃;抛弃;放纵",
  "ph": [{ "en": "abandon a plan", "cn": "放弃计划" }],
  "s": [{ "en": "The sailors had to abandon the sinking ship.", "cn": "水手们不得不弃船逃生。" }]
}
```

### 追加 Word Notebook

后续添加内容时，参考 [notebook/ADDING_ENTRIES.md](notebook/ADDING_ENTRIES.md)。

用户后续提供的重点摘抄词，放到 `notebook/words.json` 数组最前面，保留之前所有词条。同一批内容按用户提供的顺序排列；已存在的条目直接从原位置移到本批对应位置，不复制，也不默认修改原内容。同批重复项按首次出现保留一次，其余旧条目的相对顺序保持不变。页面直接按数组顺序展示，无需时间字段或额外排序逻辑。无需登记 `source.json`，刷新页面后显示更新。

短语和句型也添加到同一数组最前面，分别设置 `type: "phrase"` 或 `type: "pattern"`，单词默认视为 `word`。表达类卡片显示英文类型标记，计数统一使用 entries。它们的每个义项提供 `structure`（可替换结构）、`phrases`（双语常见用法）、`sentence`（双语例句）和 `usageNotes`（语法及易错提示），可选 `relatedExpressions` 和 `relatedNote` 用于有价值的近义、反向表达或结构对比，不要求 `synonyms`、`antonyms`，页面也不显示固定的近反义词栏目。原有单词的近反义词栏目继续保留。

`sth` 等占位符只用于展示结构；必要时提供 `pronunciationText` 指定可自然朗读的文本，例如将 `be capable of doing sth` 读作 `be capable of doing something`。

以 `oversight` 的完整词条为模板，每个词提供 `word`、`phoneticUs`（美式 IPA）、`pos`、`summary`、`note`、`senses` 和 `sources`。每个义项分别提供中文含义 `meaning`、语法说明 `grammar`、解释 `definition`、双语词组 `phrases`、双语例句 `sentence`、双语近义词 `synonyms` 和反义表达 `antonyms`。`synonymNote`、`antonymNote` 用于解释替换限制。若不同词性读音不同，可在对应义项增加 `phoneticUs`，如 recall 的名词读音。

多义词的词组、例句和近反义表达必须对应各自义项。没有自然、直接的反义词时，明确写出语境对照的限制，或使用空数组和说明，不强行凑词。音标和词义核对词典，在 `sources` 中保存来源链接；双语例句可以原创。卡片按数组顺序呈现，单词和例句可使用浏览器美式语音朗读。

频道名称和界面标签使用英文，学习内容保留中文释义与翻译。卡片采用自适应网格，单词默认展示 `senses[0]` 的第一个词组和例句，短语及句型默认展示第一个义项的结构和例句。点击 More details 在原生 `dialog` 弹窗中查看完整内容，原卡片大小保持不变；按 Esc 或点击 Close 关闭，焦点返回原按钮。

## 🛠 技术栈

- 原生 HTML + CSS + JavaScript（单文件 `index.html`，约 990 行）
- CSS Grid 自适应卡片布局
- Web Speech API（`speechSynthesis`）语音合成
- `localStorage` 持久化学习进度
- `fetch` 加载静态 JSON 数据
- 无框架 · 无打包 · 无后端

## 📄 License

[MIT](LICENSE) © 2025 Chenyan

---

<div align="center"><em>Enjoy learning English for Developers! 🌟</em></div>
