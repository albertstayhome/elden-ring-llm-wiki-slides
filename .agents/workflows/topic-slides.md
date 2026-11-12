---
description: 從 LLM Wiki 執行 Graph + Loop 工作流，產出教學型 HTML 簡報與檢查報告 (/topic-slides)
---

# `/topic-slides` — 教學 HTML 簡報 Graph 工作流

1. **Node 1（檢索 Wiki 並過覆蓋率關卡）**
   - 讀取 `wiki/index.md` 與 `wiki/concepts/*.md`。
   - 輸出 `topic-elden-combat-primer/sources.md`。
   - **關卡檢查**：若命中相關頁面 `< 3` 篇則立即中止；確認命中 6 篇核心概念頁 + 1 篇綜合頁後進入下一關。

2. **Node 2（平行抽取證據卡 Evidence Cards）**
   - 針對每篇命中的 Wiki 頁面，單獨建立 `topic-elden-combat-primer/cards/card_0X_*.md`。
   - 每張證據卡僅能看單一篇 Wiki 頁面，提取：`核心定義`、`新手白話比喻`、`精確數值表`、`版本矛盾備註`。

3. **Node 3（建立教學大綱與結構確認）**
   - 根據 `sources.md` 與 `cards/*.md` 產出 12 頁教學簡報大綱 `topic-elden-combat-primer/outline.md`。
   - **關卡檢查**：確認教學順序符合「新手破冰 → 防守生存（無敵幀）→ 進攻破防（失衡與韌性）→ 傷害放大（倍率與異常狀態）→ 高階實戰（Boss 讀指令與 Buff 疊加）→ 實戰總結」。

4. **Node 4（撰寫逐頁稿 + 小圈把檢查往前移）**
   - 依據 `outline.md` 與對應 `cards/*.md` 撰寫 `topic-elden-combat-primer/drafts/slides_draft_v2_passed.md`。
   - **執行腳本檢查**：`python scripts/check_drafts.py`
   - 若發現某頁字數超標（> 210 字）或漏標 `[WIKI-0X]` 出處，**小圈退回只修該頁**（最多 2 輪），直到腳本回傳 `PASS`。

5. **Node 5（渲染 HTML 簡報 + 渲染檢查）**
   - 將通過檢查的逐頁稿一字不改地渲染為互動式教學簡報 `deck.html`。
   - **執行腳本檢查**：`python scripts/check_slides.py`
   - 若發生版面溢出則退回 Node 4 縮短逐頁稿；全數通過後產出最終 `topic-elden-combat-primer/report.md` 交件。
