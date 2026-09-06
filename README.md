<div align="center">

<img src="img/learn.png" alt="English Learning" width="110">

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
| ⚖️ **易混词辨析 Similar Words** | 5 组对比卡 · 30 词 | 把 remarkable / incredible / reasonable、scalable / maintainable 这类形近意近词并列对比，不同色彩主题区分。 |
| 📘 **雅思核心词汇 IELTS** | 2000+ 词 | 每词含美式音标、中文释义（词性自动上色）、常用词组、中英双语例句。顶部 A–Z 字母导航 + 关键词搜索。 |

## 🎯 亮点功能

- **👁 自测模式**：点击右上角「小眼睛」隐藏所有释义 / 对话 / 例句，只留单词或场景标题；逐张点击卡片揭示答案，适合自我检测。四个模块通用。
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
│   └── learn.png              # Logo / favicon
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

**`similarword/similar_words.json`** —— 数组，每个元素是一组对比卡。`theme` 可选 `theme-blue` / `theme-green` / `theme-purple` / `theme-orange`。

```json
{
  "theme": "theme-blue",
  "words": [
    { "en": "Scalable", "phonetic": "/ˈskeɪləbl/", "cn": "可扩展的" },
    { "en": "Maintainable", "phonetic": "/meɪnˈteɪnəbl/", "cn": "可维护的（代码清晰、易于修改）" }
  ]
}
```

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
