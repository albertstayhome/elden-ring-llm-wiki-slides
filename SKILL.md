---
name: topic-slides-generator
description: 從 LLM Wiki 檢索知識，透過 Graph 節點與內迴圈（Loop）驗證，生成零幻覺、無溢出的教學型 HTML 簡報。
---

# SKILL.md — 主題教學簡報 Loop / Graph 規格書

## 🎯 目標（Goal）
只使用 `wiki/` 知識庫與抽取出的 `cards/` 證據卡內容，針對指定教學主題產出一份讓完全新手也能看懂的 **教學型 HTML 簡報（`deck.html`）**。

## 🚧 限制（Constraints）
1. **零外部腦補**：所有出現在簡報上的數字（幀數、百分比、秒數、倍率）必須 100% 存在於 `topic-elden-combat-primer/cards/*.md` 中。
2. **職責分離（Separation of Concerns）**：渲染 HTML 節點（Node 5）只能負責視覺排版與互動元件，**嚴禁修改逐頁稿（Node 4）已審核通過的文字與數據**。

## ✅ 完成標準與雙重驗證（Verification Gates）
### 1. 🧮 程式檢查（Executable Scripts）
- `python scripts/lint_wiki.py`：確認 Wiki 知識庫 6 篇原始文獻皆已 Ingest、雙向連結完整、矛盾裁決已記錄。
- `python scripts/check_drafts.py`（**把檢查往前移**）：
  - 檢查頁數是否介於 `8–15` 頁之間（本簡報定為 12 頁）。
  - 檢查每一頁是否皆標註 `[WIKI-0X]` 與 `[RAW-0X]` 出處。
  - 檢查每一頁要點數是否 `≤ 5` 點、單頁正文總字數是否 `≤ 210` 字（防止渲染階段發生版面溢出）。
  - 自動比對簡報中的所有數值是否皆可在對應 `cards/` 證據卡中找到。
- `python scripts/check_slides.py`（**最終 HTML 渲染檢查**）：
  - 檢查 `deck.html` 內含完整 `<section class="slide">` 結構、出處連結有效、無高度溢出風險。

### 2. 🧑‍⚖️ AI 審查（Independent Context Audit）
- 開啟獨立審查視角（只給成品與對應 `cards/` 證據卡），檢查：
  1. **忠實度（Faithfulness）**：說法有沒有講反？（例如：把「負重 ≥ 70% 會變成重負荷慢滾」講反成「≤ 70%」）。
  2. **覆蓋率（Coverage）**：6 篇核心 Wiki 概念頁與版本矛盾裁決是否都有被納入簡報對應章節？

## 🔁 每一輪修正規則（Loop Policy）
- **局部修復原則**：只修正檢查報告（`report.md`）列出的特定錯誤頁面（例如第 5 頁字太多、第 6 頁缺出處，就只修第 5、6 頁，其餘頁面鎖定不動）。

## 🛑 停止條件（Brakes & Stop Conditions）
1. **前置剎車**：若 `sources.md` 檢索到的相關 Wiki 頁面少於 3 頁，立即停止生成並報錯（不硬湊）。
2. **硬上限剎車**：單一節點小圈 Loop 最多修正 **2 輪**，整體流程最多 **3 輪**；全數通過檢查腳本後立即交件並輸出 `report.md`。
