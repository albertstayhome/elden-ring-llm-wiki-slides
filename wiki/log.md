# LLM Wiki 建置、Ingest 與矛盾裁決日誌 (`log.md`)

## [Batch 0] 需求訪談與規格建立（Discuss First, Then Generate）
- **執行動作**：完成 8 題需求訪談（讀者、頁面類型、語言、出處細度、矛盾處理、Ingest 方式、下游產出、Lint 規則），經確認後建立 `wiki/interview_spec.md`、`AGENTS.md` 與 `CLAUDE.md`。

## [Batch 1] 首批文獻 Ingest（First Ingest: RAW-01 ~ RAW-02）
- **Ingest 來源**：`raw/01_stance_and_poise_frames.md`、`raw/02_dodge_roll_iframes_equip_load.md`
- **產出頁面**：`wiki/concepts/stance-and-poise.md` (`[WIKI-01]`)、`wiki/concepts/iframes-and-equip-load.md` (`[WIKI-02]`)
- **版本矛盾裁決 #1**：`[RAW-01 §1.3]` 記載 Patch 1.07 與 Patch 1.10+ 之霸體調整差異，已依 `AGENTS.md` 第 3 條規則，於 `[WIKI-01]` 標註 `> [!WARNING] 版本數據矛盾與裁決` 區塊，統一採用 Patch 1.10+ 之 PvE 被動韌性門檻（`51` 點／`101` 點）。
- **版本控制**：執行 `git commit -m "first ingest"`。

## [Batch 2] 第二批文獻 Ingest 與綜合頁建立（RAW-03 ~ RAW-06）
- **Ingest 來源**：`raw/03_status_effects_hemorrhage_frostbite.md`、`raw/04_damage_negation_and_motion_values.md`、`raw/05_boss_input_reading_and_aggro.md`、`raw/06_ash_of_war_buff_stacking_rules.md`
- **產出頁面**：`[WIKI-03]`、`[WIKI-04]`、`[WIKI-05]`、`[WIKI-06]` 及跨文獻綜合頁 `wiki/synthesis/beginner-combat-roadmap.md` (`[WIKI-SYN-01]`)。
- **版本矛盾裁決 #2**：`[RAW-03 §3.3]` 記載雙持武器跳劈 4 連擊異常狀態倍率於 Patch 1.06 前為 `90%`（共 `360%`），Patch 1.07+ 下修為 **`65%`（共 `260%`）**。已於 `[WIKI-03]` 標註警告區塊並以最新 `65% / 260%` 作為教學標準數據。
- **Lint 檢查狀態**：執行 `python scripts/lint_wiki.py` 通過（6 篇原始文獻 100% 覆蓋、0 斷鏈、0 孤兒頁）。
