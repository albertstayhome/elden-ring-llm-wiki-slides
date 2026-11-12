# 家豪的交界地戰鬥底層機制 LLM Wiki — 知識庫總目錄 (`index.md`)

> 本知識庫依照 [`AGENTS.md`](../AGENTS.md) 與 [`interview_spec.md`](interview_spec.md) 規範，自 `raw/` 目錄下 **6 篇原始筆記** 整理編譯而成，作為下游「教學 HTML 簡報（`deck.html`）」的核心資料來源。

---

## 一、原始資料層（唯讀原始筆記，`raw/`）
1. `[RAW-01]` [`01_stance_and_poise_frames.md`](../raw/01_stance_and_poise_frames.md) — 失衡系統（Stance）與玩家韌性（Poise）底層數據
2. `[RAW-02]` [`02_dodge_roll_iframes_equip_load.md`](../raw/02_dodge_roll_iframes_equip_load.md) — 翻滾無敵幀（i-Frames）與四階段負重門檻（60 FPS）
3. `[RAW-03]` [`03_status_effects_hemorrhage_frostbite.md`](../raw/03_status_effects_hemorrhage_frostbite.md) — 異常狀態累積：出血與凍傷數學公式與雙持倍率修正
4. `[RAW-04]` [`04_damage_negation_and_motion_values.md`](../raw/04_damage_negation_and_motion_values.md) — 攻擊動作倍率（MV）與雙層減傷公式（Split Damage 懲罰）
5. `[RAW-05]` [`05_boss_input_reading_and_aggro.md`](../raw/05_boss_input_reading_and_aggro.md) — Boss AI 讀指令（Input Reading）偵測條件與安全喝水視窗
6. `[RAW-06]` [`06_ash_of_war_buff_stacking_rules.md`](../raw/06_ash_of_war_buff_stacking_rules.md) — 戰灰與增益魔法五大分類桶（Buff Buckets）疊加規則

---

## 二、核心概念頁（Compiled Concept Pages，`wiki/concepts/`）
| 頁面編號 | 頁面連結 | 核心主題 | 對應原始文獻 | 關鍵數據摘要 |
| :--- | :--- | :--- | :--- | :--- |
| **`[WIKI-01]`** | [[stance-and-poise]] | 失衡值與韌性機制 | `[RAW-01]` | Boss 失衡 `80/120/150` 點、5 秒恢復倒數、玩家 `51/101` 韌性門檻 |
| **`[WIKI-02]`** | [[iframes-and-equip-load]] | 翻滾無敵幀與負重 | `[RAW-02]` | 輕/中負荷 `13` 幀無敵幀 + `8` 幀硬直；重負荷（`≥70%`）`12` 幀 + `16` 幀硬直 |
| **`[WIKI-03]`** | [[status-buildup-math]] | 出血與凍傷異常數學 | `[RAW-03]` | 出血扣血 `10.5%+100`；凍傷扣血 `10%+30` 並降減傷 `20%` 達 30 秒；雙持倍率 `65%` |
| **`[WIKI-04]`** | [[damage-formula-mv]] | 動作倍率與雙層減傷 | `[RAW-04]` | 第一層固定防禦力（複合屬性雙重扣減）+ 第二層減傷率；輕擊 MV `100%` vs 戰技 `210%~240%` |
| **`[WIKI-05]`** | [[boss-ai-input-reading]] | Boss 讀指令與喝水視窗 | `[RAW-05]` | `8~20m` 中立待機下 `0.2` 秒（`12` 幀）觸發懲罰；喝水需 `52` 幀，應卡收招 `1.5~2.5` 秒硬直 |
| **`[WIKI-06]`** | [[buff-stacking-buckets]] | 五大增益分類桶疊加 | `[RAW-06]` | 武器、軀幹、光環、精力、特殊共 5 桶；同桶互蓋、異桶相乘（最高示範 `+58.7%`） |

---

## 三、跨文獻綜合應用頁（Synthesis Pages，`wiki/synthesis/`）
- **`[WIKI-SYN-01]`** [[beginner-combat-roadmap]] — 跨文獻整合：交界地新手生存與輸出最佳化全流程藍圖

---

## 四、管理與稽核紀錄
- [`interview_spec.md`](interview_spec.md) — 「先討論、後生成」8 題需求訪談與規格確認單
- [`log.md`](log.md) — Ingest 批次紀錄、版本矛盾裁決與 `lint_wiki.py` 檢查日誌
