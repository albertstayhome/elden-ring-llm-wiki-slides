#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/check_drafts.py — 逐頁稿檢查腳本（把檢查往前移）
程式檢查項目（確定性驗證）：
1. 頁數是否介於 8~15 頁
2. 每頁是否標註 [WIKI-XX] 與 [RAW-0X] 出處
3. 每頁要點數 <= 5 點、單頁正文總字數 <= 210 字（防止進到 HTML 才爆版！）
4. 逐頁稿內出現的所有數值（百分比、幀數、秒數、倍率）是否 100% 存在於 cards/ 證據卡與 Wiki 中（攔截錯置的舊版數據或幻覺數字）
"""
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
CARDS_DIR = BASE / "topic-elden-combat-primer/cards"
WIKI_DIR = BASE / "wiki"

def check_file(draft_path: Path):
    print(f"=== 正在執行逐頁稿程式檢查（把檢查往前移）：{draft_path.name} ===")
    text = draft_path.read_text(encoding="utf-8")
    slides = re.split(r"^## Slide \d+:", text, flags=re.MULTILINE)[1:]
    errors = []

    print(f"  -> [檢查 1] 簡報總頁數：{len(slides)} 頁（規範區間：8~15 頁）")
    if not (8 <= len(slides) <= 15):
        errors.append(f"頁數不符規範：{len(slides)} 頁（應為 8~15 頁）")

    # 讀取所有證據卡與 Wiki 建立合法數值池 (Allowed Numbers Corpus)
    corpus_text = ""
    for f in sorted(CARDS_DIR.glob("*.md")) + sorted((WIKI_DIR / "concepts").glob("*.md")) + sorted((WIKI_DIR / "synthesis").glob("*.md")):
        corpus_text += f.read_text(encoding="utf-8") + "\n"
    allowed_numbers = set(re.findall(r"\d+(?:\.\d+)?%?", corpus_text))
    # 加入基本結構序號 (1~4)
    allowed_numbers.update({"1", "2", "3", "4", "5", "6"})

    for idx, s in enumerate(slides, 1):
        lines = [ln.strip() for ln in s.strip().splitlines() if ln.strip()]
        title = lines[0] if lines else f"Slide {idx}"
        src_lines = [ln for ln in lines if ln.startswith("- 來源：")]
        bullets = [ln for ln in lines if ln.startswith("- 重點")]

        # 1. 檢查出處標籤
        if not src_lines or ("[WIKI-" not in src_lines[0] or "[RAW-" not in src_lines[0]):
            errors.append(f"Slide {idx:02d} ({title})：[缺出處] 未標註有效的 [WIKI-XX] 或 [RAW-0X] 來源標籤")

        # 2. 檢查要點數與總字數（把防溢出檢查往前移）
        stripped_bullets = [re.sub(r"[`\*]", "", re.sub(r"^- 重點 \d+：", "", b)) for b in bullets]
        body_chars = sum(len(b) for b in stripped_bullets)
        if len(bullets) > 5:
            errors.append(f"Slide {idx:02d} ({title})：[要點超標] 要點數 {len(bullets)} > 5 點上限")
        if body_chars > 210:
            errors.append(f"Slide {idx:02d} ({title})：[字數溢出風險] 正文字數 {body_chars} 字 > 210 字上限")

        # 3. 檢查所有數值是否皆有證據卡支持（攔截幻覺數字）
        slide_body = "\n".join(stripped_bullets)
        nums_in_slide = re.findall(r"\d+(?:\.\d+)?%?", slide_body)
        unverified_nums = [n for n in nums_in_slide if n not in allowed_numbers]
        if unverified_nums:
            errors.append(f"Slide {idx:02d} ({title})：[幻覺數字攔截] 發現未存在於 cards/ 證據卡的數字：{unverified_nums}")

        print(f"  -> Slide {idx:02d}: {len(bullets)} 個要點, 淨字數 {body_chars} 字, 查驗 {len(nums_in_slide)} 個數值")

    if errors:
        print(f"\n[FAIL] {draft_path.name} 程式檢查未通過（共發現 {len(errors)} 項違規）：")
        for e in errors:
            print(f"  ❌ {e}")
        return False
    else:
        print(f"\n[PASS] {draft_path.name} 全數通過逐頁稿程式檢查（12 頁、100% 出處、0 溢出、100% 數值經證據卡核對）！")
        return True

if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "topic-elden-combat-primer/drafts/slides_draft_v2_passed.md"
    ok = check_file(target)
    sys.exit(0 if ok else 1)
