# 家豪的交界地戰鬥底層機制 LLM Wiki ＆ 教學 HTML 簡報 (`elden-ring-llm-wiki-slides`)

> **TAICA 生成式 AI：文字與圖像生成的原理與實務 — 第 10 週作業**
> - **作者**：中央大學 電機二A 林鑫吾 (`11450101010`)
> - **線上教學 HTML 簡報 (`deck.html`)**：https://albertstayhome.github.io/elden-ring-llm-wiki-slides/deck.html
> - **LLM Wiki 與 Graph 工作流主控台 (`index.html`)**：https://albertstayhome.github.io/elden-ring-llm-wiki-slides/

## 專案亮點
1. **步驟一（先討論、後生成 LLM Wiki）**：
   - 先完成 8 題需求訪談（[`wiki/interview_spec.md`](wiki/interview_spec.md)），再生成 [`AGENTS.md`](AGENTS.md) 與 `CLAUDE.md`（`@AGENTS.md`）。
   - Ingest **6 篇原始文獻**（[`raw/`](raw/)，超過作業至少 5 篇要求）至結構化 [`wiki/`](wiki/)，並記錄 2 處版本數據矛盾裁決（Patch 1.07 vs 1.10+）。
2. **步驟二（12 頁教學型 HTML 簡報）**：
   - [`deck.html`](deck.html) 將硬核底層數據轉化為完全新手也能秒懂的四階段互動簡報，每頁底部皆標註 `[WIKI-0X]` 與 `[RAW-0X]` 溯源標籤。
3. **步驟三 & 四（Loop / Graph 設計與把檢查往前移反思）**：
   - 完整保留 [`topic-elden-combat-primer/`](topic-elden-combat-primer/) 各節點狀態檔（`sources.md`、`cards/`、`outline.md`、`drafts/`、`report.md`）與 3 支可執行 Python 檢查腳本（[`scripts/`](scripts/)）。
