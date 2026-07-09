#!/usr/bin/env python3
"""Fix ALL remaining errors - final attempt."""
import re
from pathlib import Path

ROOT = Path("/workspace/llm-wiki/wiki")
INDEX = Path("/workspace/llm-wiki/index.md")

# ============================================================
# FIX 1: Remove [[view email]] from ALL wiki files
# ============================================================
ve_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if '[[view email]]' in content:
        content = content.replace('[[view email]]', '')
        p.write_text(content, encoding='utf-8')
        ve_fixed += 1
print(f"FIX 1 - view email removed: {ve_fixed} files")

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
# FIX 4: Fix [[a-sliding-window-based-reinforcement-learning-for-dynamic-assembly-flow-shop-scheduling-with-multi-p-2026-07-07_2]]
# → [[sliding-window-reinforcement-learning-for-assembly-scheduling_2026_1]]
# ============================================================
sw_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if 'a-sliding-window-based-reinforcement-learning-for-dynamic-assembly-flow-shop-scheduling-with-multi-p-2026-07-07_2' in content:
        content = content.replace(
            '[[a-sliding-window-based-reinforcement-learning-for-dynamic-assembly-flow-shop-scheduling-with-multi-p-2026-07-07_2]]',
            '[[sliding-window-reinforcement-learning-for-assembly-scheduling_2026_1]]'
        )
        p.write_text(content, encoding='utf-8')
        sw_fixed += 1
print(f"FIX 4 - sliding-window long slug fixed: {sw_fixed} files")

# ============================================================
# FIX 5: Fix [[architecture-overview_architecture_1]] → correct slug
# ============================================================
arch_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if 'architecture-overview_architecture_1' in content:
        content = content.replace(
            '[[architecture-overview_architecture_1]]',
            '[[architecture-overview_2026_1]]'
        )
        p.write_text(content, encoding='utf-8')
        arch_fixed += 1
print(f"FIX 5 - architecture-overview slug fixed: {arch_fixed} files")

# ============================================================
# FIX 6: Fix [[previewing-gpt-5-6-sol_07_1]] → correct slug
# ============================================================
gpt_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if 'previewing-gpt-5-6-sol_07_1' in content:
        content = content.replace(
            '[[previewing-gpt-5-6-sol_07_1]]',
            '[[previewing-gpt-5-6-sol-a-next-generation-model-2026-07-07]]'
        )
        p.write_text(content, encoding='utf-8')
        gpt_fixed += 1
print(f"FIX 6 - previewing-gpt-5-6-sol slug fixed: {gpt_fixed} files")

# ============================================================
# FIX 7: Fix [[previewing-gpt-56-sol-a-next-generation-model-2026-07-07]]
# → [[previewing-gpt-5-6-sol-a-next-generation-model-2026-07-07]]
# ============================================================
gpt2_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if 'previewing-gpt-56-sol-a-next-generation-model-2026-07-07' in content:
        content = content.replace(
            '[[previewing-gpt-56-sol-a-next-generation-model-2026-07-07]]',
            '[[previewing-gpt-5-6-sol-a-next-generation-model-2026-07-07]]'
        )
        p.write_text(content, encoding='utf-8')
        gpt2_fixed += 1
print(f"FIX 7 - previewing-gpt-56 slug fixed: {gpt2_fixed} files")

# ============================================================
# FIX 8: Fix [[SWRL — [[sliding-window... (double bracket issue)
# ============================================================
sw2_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if '[[SWRL — [[sliding-window-reinforcement-learning-for-assembly-scheduling_2026_1]]' in content:
        content = content.replace(
            '[[SWRL — [[sliding-window-reinforcement-learning-for-assembly-scheduling_2026_1]]',
            '[[swrl]] — [[sliding-window-reinforcement-learning-for-assembly-scheduling_2026_1]]'
        )
        p.write_text(content, encoding='utf-8')
        sw2_fixed += 1
print(f"FIX 8 - double bracket fixed: {sw2_fixed} files")

print("\n=== ALL FIXES COMPLETE ===")
