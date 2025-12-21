# DevEnglish - 程序员单词本

DevEnglish 是一个为程序员设计的英语词汇学习工具。它帮助你通过简洁的界面记忆和管理专业词汇，支持“认识/不认识”的状态标记，并提供相似词汇的分组记忆功能。

## 功能特点

*   **单词本管理**：
    *   动态加载 `wordbook/` 目录下的所有 JSON 单词书。
    *   支持按 "全部"、"未标记"、"认识"、"不认识" 筛选单词。
    *   实时保存单词状态到 JSON 文件。
    *   **记忆模式**：一键隐藏音标、释义、例句，仅显示单词，用于自我测试。
    *   **详细查看**：在记忆模式下，可单独点击卡片上的“眼睛”按钮查看特定单词的详情。
    *   支持 TTS 语音朗读。

*   **相似词分组 (Similar Words)**：
    *   将形近词、意近词或同根词分组展示，提高记忆效率。
    *   数据驱动：从 `similarword/similar_words.json` 动态加载数据。
    *   **记忆模式**：同样支持一键隐藏中文释义和音标，仅显示英文单词。
    *   支持单独查看某个卡片的隐藏内容。

## 项目结构

```
vocabulary_learn/
├── index.html          # 主程序入口，包含所有前端逻辑
├── similar.html        # 独立的相似词展示页面（组件化）
├── server.py           # Python HTTP 服务器，处理 JSON 读写
├── wordbook/           # 存放单词书数据的目录 (.json)
│   ├── Architecture & Design.json
│   └── ...
└── similarword/        # 存放相似词数据的目录
    └── similar_words.json
```

## 快速开始

1.  **启动服务器**：
    确保你安装了 Python 3，然后在终端运行：
    ```bash
    python3 server.py
    ```

2.  **访问应用**：
    打开浏览器访问 `http://localhost:9001`。

3.  **使用**：
    *   左侧侧边栏切换 "Software Words" (单词本) 和 "Similar Words" (相似词)。
    *   在 "Software Words" 模式下，顶部栏可切换不同的单词书。
    *   点击右上角的“眼睛”图标切换显示/隐藏模式。

## 数据格式说明

### 单词本 (`wordbook/*.json`)
```json
[
    {
        "id": 1,
        "term": "Algorithm",
        "phonetic": "/ˈælɡərɪðəm/",
        "definition": "算法",
        "synonyms": "Procedure, Routine",
        "exampleEn": "The sorting algorithm is very efficient.",
        "exampleCn": "这个排序算法非常高效。",
        "status": 0  // 0:未标记, 1:认识, 2:不认识
    }
]
```

### 相似词 (`similarword/similar_words.json`)
```json
[
    {
        "theme": "theme-blue", // 卡片颜色主题
        "words": [
            {
                "en": "Remarkable",
                "cn": "卓越的",
                "phonetic": "/rɪˈmɑːkəbl/"
            }
        ]
    }
]
```
