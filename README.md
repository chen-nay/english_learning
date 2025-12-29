# English Learning - 英语学习助手 💻🚀

```
Note:
1 除了场景对话(Dialogue)中的conversation内容来自书本《English Conversation Premium》外，其余英语内容由AI生成
2 本项目所有代码，均由AI生成(包括本篇READEME)
```

本项目是一个辅助英语学习工具，旨在帮助掌握软件专业术语、提升职场交流能力（如机场、酒店等真实场景），并清晰辨析形近意近词汇。

项目为**纯静态 Web 应用**，无需复杂的后端环境即可运行。

## ✨ 功能特点

*   **💾 专业词汇 (Software Words)**：
    *   按技术领域分类（架构、前端、后端、版本控制等）。
    *   包含音标、精准释义、同义词及中英双语例句。
    *   **自测模式**：点击右上角“小眼睛”隐藏所有详情，仅留单词进行自我测试。
    *   **语音支持**：点击喇叭图标，支持 Web Speech API 实时发音。

*   **💬 场景对话 (Dialogue)**：
    *   模拟机场、酒店、订餐等真实出国交流场景。
    *   包含重点句型 (Key Structures) 解析。
    *   同样支持自测模式，隐藏对话详情进行盲听或口语练习。

*   **⚖️ 易混词辨析 (Similar Words)**：
    *   将容易混淆的词汇进行对比展示。
    *   使用不同的颜色主题进行视觉区分。

*   **🛠 交互优化**：
    *   **可折叠侧边栏**：点击 Logo 旁的箭头可收起菜单，最大化学习区域。
    *   **完全静态化**：基于 `source.json` 管理数据源，无需运行 Python 服务。

## 📂 项目结构

```text
vocabulary_learn/
├── index.html          # 核心程序入口 (HTML/CSS/JS)
├── source.json         # 数据源配置文件，管理所有 JSON 文件列表
├── img/                # 图片资源目录 (favicon, logo)
├── wordbook/           # 存放专业词汇数据的目录 (.json)
├── dialogue/           # 存放场景对话数据的目录 (.json)
└── similarword/        # 存放易混词数据的目录 (.json)
```

## 🚀 快速开始

由于本项目是纯静态的，你可以直接用浏览器打开 `index.html`（部分浏览器可能因安全限制无法读取本地 JSON），推荐使用简单的静态文件服务器：

**使用 Python (推荐):**
```bash
# 在项目根目录下运行
python3 -m http.server 9001
```
然后访问：`http://localhost:9001`

**使用 Node.js (npx):**
```bash
npx serve .
```

## ⚙️ 数据扩展

如果你想添加自己的单词书或对话：

1.  **添加文件**：在 `wordbook/` 或 `dialogue/` 目录下创建新的 `.json` 文件（参考现有文件格式）。
2.  **更新配置**：在根目录的 `source.json` 中，将你的新文件名添加到对应的数组中。
3.  **刷新页面**：应用会自动加载并显示新的分类。

---

*Enjoy learning English for Developers!* 🌟