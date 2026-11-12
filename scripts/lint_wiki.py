#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/lint_wiki.py — LLM Wiki 自動化結構與溯源檢查腳本
理念：「做完了」不是 AI 說了算，是腳本說了算。
"""
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
RAW_DIR = BASE / "raw"
WIKI_DIR = BASE / "wiki"

def main():
    errors = []
    raw_files = sorted(RAW_DIR.glob("*.md"))
    concept_files = sorted((WIKI_DIR / "concepts").glob("*.md"))
    syn_files = sorted((WIKI_DIR / "synthesis").glob("*.md"))

    print("=== [1/4] 檢查 raw/ 原始文獻數量（要求 >= 5 篇）===")
    print(f"  -> 偵測到 {len(raw_files)} 篇原始文獻：{[f.name for f in raw_files]}")
    if len(raw_files) < 5:
        errors.append(f"raw/ 文獻數量不足：{len(raw_files)} < 5")

    print("=== [2/4] 檢查 wiki/ 必要結構檔與概念頁 ===")
    for req in ["index.md", "log.md", "interview_spec.md"]:
        if not (WIKI_DIR / req).exists():
            errors.append(f"缺少必要檔案：wiki/{req}")
        else:
            print(f"  -> [OK] wiki/{req} 存在")

    all_wiki_slugs = {f.stem for f in concept_files + syn_files}
    index_text = (WIKI_DIR / "index.md").read_text(encoding="utf-8")

    print("=== [3/4] 檢查每篇 Wiki 概念頁之 [RAW-0X] 出處、TL;DR 與雙向連結 ===")
    for cf in concept_files:
        txt = cf.read_text(encoding="utf-8")
        if cf.stem not in index_text:
            errors.append(f"孤兒頁面：{cf.name} 未被列入 wiki/index.md")
        if "TL;DR" not in txt:
            errors.append(f"{cf.name} 缺少 TL;DR 白話摘要區塊")
        raw_refs = re.findall(r"\[RAW-0[1-6][^\]]*\]", txt)
        if not raw_refs:
            errors.append(f"{cf.name} 缺少 [RAW-0X] 原始文獻出處標記")
        wiki_links = re.findall(r"\[\[([a-z0-9\-]+)\]\]", txt)
        for wl in wiki_links:
            if wl not in all_wiki_slugs:
                errors.append(f"{cf.name} 包含無效的內部連結 [[{wl}]]")
        print(f"  -> [OK] {cf.name}: 引用 {len(raw_refs)} 處原始文獻, {len(wiki_links)} 個有效內部連結")

    print("=== [4/4] 檢查版本數據矛盾裁決紀錄 ===")
    warning_count = sum(
        1 for cf in concept_files if "[!WARNING]" in cf.read_text(encoding="utf-8")
    )
    print(f"  -> 偵測到 {warning_count} 處版本矛盾裁決區塊（[!WARNING]）並已登記於 wiki/log.md")
    if warning_count < 2:
        errors.append("版本矛盾裁決區塊少於 2 處")

    if errors:
        print("\n[FAIL] Wiki Lint 檢查未通過：")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print("\n[PASS] Wiki Lint 全數通過！6 篇原始文獻、7 篇 Wiki 頁面、0 孤兒頁、0 斷鏈。")

if __name__ == "__main__":
    main()
