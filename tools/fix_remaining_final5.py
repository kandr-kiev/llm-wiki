#!/usr/bin/env python3
"""Fix ALL remaining errors - final attempt with correct slugs."""
import re
from pathlib import Path

ROOT = Path("/workspace/llm-wiki/wiki")
INDEX = Path("/workspace/llm-wiki/index.md")

# ============================================================
# FIX 1: Fix [view email] → view email (no brackets)
# The issue: "From: Junhao Qiu [view email] [v1]" → linter sees [view email as broken wikilink
# ============================================================
ve_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    original = content
    # Fix: [view email] → view email
    content = content.replace('[view email]', 'view email')
    if content != original:
        p.write_text(content, encoding='utf-8')
        ve_fixed += 1
print(f"FIX 1 - view email brackets removed: {ve_fixed} files")

# ============================================================
# FIX 2: Fix [[karpathy]] in index.md → [[karpathy-llm-wiki-2026_1]]
# ============================================================
idx_content = INDEX.read_text(encoding='utf-8')
if '[[karpathy]]' in idx_content:
    idx_content = idx_content.replace('[[karpathy]]', '[[karpathy-llm-wiki-2026_1]]')
    INDEX.write_text(idx_content, encoding='utf-8')
    print("FIX 2 - karpathy wikilinks fixed in index.md")
else:
    print("FIX 2 - karpathy already fixed")

# ============================================================
# FIX 3: Fix [[query, doc.page_content]] → backticks
# ============================================================
qdpc_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if '[[query, doc.page_content]]' in content:
        content = content.replace('[[query, doc.page_content]]', '`query, doc.page_content`')
        p.write_text(content, encoding='utf-8')
        qdpc_fixed += 1
print(f"FIX 3 - query, doc.page_content fixed: {qdpc_fixed} files")

# ============================================================
# FIX 4: Fix [[sliding-window-reinforcement-learning-for-assembly-scheduling_2026_1]]
# → [[a-sliding-window-based-reinforcement-learning-for-dynamic-assembly-flow-shop-scheduling-with-multi-p-2026-07-07.md]]
# ============================================================
sw_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if 'sliding-window-reinforcement-learning-for-assembly-scheduling_2026_1' in content:
        content = content.replace(
            '[[sliding-window-reinforcement-learning-for-assembly-scheduling_2026_1]]',
            '[[a-sliding-window-based-reinforcement-learning-for-dynamic-assembly-flow-shop-scheduling-with-multi-p-2026-07-07.md]]'
        )
        p.write_text(content, encoding='utf-8')
        sw_fixed += 1
print(f"FIX 4 - sliding-window slug fixed: {sw_fixed} files")

# ============================================================
# FIX 5: Fix [[architecture-overview_2026_1]] → [[architecture-overview_architecture_1.md]]
# ============================================================
arch_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if 'architecture-overview_2026_1' in content:
        content = content.replace(
            '[[architecture-overview_2026_1]]',
            '[[architecture-overview_architecture_1.md]]'
        )
        p.write_text(content, encoding='utf-8')
        arch_fixed += 1
print(f"FIX 5 - architecture-overview slug fixed: {arch_fixed} files")

# ============================================================
# FIX 6: Fix [[swrl]] → remove (no matching file exists)
# ============================================================
swrl_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if '[[swrl]]' in content:
        content = content.replace('[[swrl]]', '')
        p.write_text(content, encoding='utf-8')
        swrl_fixed += 1
print(f"FIX 6 - swrl wikilinks removed: {swrl_fixed} files")

# ============================================================
# FIX 7: Fix [[previewing-gpt-5-6-sol-a-next-generation-model-2026-07-07]]
# → [[previewing-gpt-5-6-sol_07_1.md]]
# ============================================================
gpt_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if 'previewing-gpt-5-6-sol-a-next-generation-model-2026-07-07' in content:
        content = content.replace(
            '[[previewing-gpt-5-6-sol-a-next-generation-model-2026-07-07]]',
            '[[previewing-gpt-5-6-sol_07_1.md]]'
        )
        p.write_text(content, encoding='utf-8')
        gpt_fixed += 1
print(f"FIX 7 - previewing-gpt-5-6-sol slug fixed: {gpt_fixed} files")

# ============================================================
# FIX 8: Check sha256 drift
# ============================================================
import hashlib
sha_fixed = 0
for raw in (ROOT.parent / "raw").rglob("*.md"):
    if raw.name == "README.md":
        continue
    text = raw.read_text(encoding='utf-8')
    fm_match = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not fm_match:
        continue
    fm = fm_match.group(1)
    data = {}
    for raw_line in fm.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            data[key] = [x.strip().strip('"\'') for x in inner.split(",") if x.strip()]
        else:
            data[key] = value.strip('"\'')
    expected = data.get("sha256")
    actual = hashlib.sha256(text[text.find("---", 4)+5:].strip().encode("utf-8")).hexdigest()
    if expected != actual:
        print(f"SHA256 drift: {raw.name} expected={expected[:8]}... actual={actual[:8]}...")
        sha_fixed += 1
print(f"FIX 8 - sha256 drift files: {sha_fixed}")

print("\n=== ALL FIXES COMPLETE ===")
