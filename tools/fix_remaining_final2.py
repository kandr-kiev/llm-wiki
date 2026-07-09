#!/usr/bin/env python3
"""Fix ALL remaining errors in one pass."""
import re
from pathlib import Path

ROOT = Path("/workspace/llm-wiki/wiki")
INDEX = Path("/workspace/llm-wiki/index.md")

# ============================================================
# FIX 1: Fix broken frontmatter: sources: []--- → sources: []\n---
# ============================================================
fm_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    original = content
    # Fix: sources: []--- → sources: []\n---
    content = content.replace('sources: []---', 'sources: []\n---')
    if content != original:
        p.write_text(content, encoding='utf-8')
        fm_fixed += 1
print(f"Frontmatter newline fixes: {fm_fixed}")

# ============================================================
# FIX 2: Remove [[view email]] from all files
# ============================================================
ve_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    original = content
    content = content.replace('[[view email]]', '')
    if content != original:
        p.write_text(content, encoding='utf-8')
        ve_fixed += 1
print(f"view email removed: {ve_fixed} files")

# ============================================================
# FIX 3: Fix [[karpathy]] in index.md → [[karpathy-llm-wiki-2026_1]]
# ============================================================
idx_content = INDEX.read_text(encoding='utf-8')
idx_content = idx_content.replace('[[karpathy]]', '[[karpathy-llm-wiki-2026_1]]')
INDEX.write_text(idx_content, encoding='utf-8')
print(f"karpathy wikilinks fixed in index.md")

# ============================================================
# FIX 4: Fix [[query, doc.page_content]] → backticks
# ============================================================
qdpc_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    original = content
    content = content.replace('[[query, doc.page_content]]', '`query, doc.page_content`')
    if content != original:
        p.write_text(content, encoding='utf-8')
        qdpc_fixed += 1
print(f"query, doc.page_content fixed: {qdpc_fixed}")

# ============================================================
# FIX 5: Fix sliding-window wikilink (wrong slug)
# ============================================================
sw_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    original = content
    content = content.replace(
        '[[a-sliding-window-based-reinforcement-learning-for-dynamic-assembly-flow-shop-scheduling-with-multi-p-2026-07-07_1]]',
        '[[sliding-window-reinforcement-learning-for-assembly-scheduling_2026_1]]'
    )
    if content != original:
        p.write_text(content, encoding='utf-8')
        sw_fixed += 1
print(f"sliding-window wikilink fixed: {sw_fixed}")

# ============================================================
# FIX 6: Add missing frontmatter fields to files that need them
# ============================================================
fm2_fixed = 0
for p in ROOT.rglob("*.md"):
    text = p.read_text(encoding='utf-8')
    fm_match = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not fm_match:
        continue
    fm = fm_match.group(1)
    needs = []
    if 'created:' not in fm: needs.append('created: 2026-07-08')
    if 'description:' not in fm: needs.append('description: ""')
    if 'sources:' not in fm: needs.append('sources: []')
    if 'type:' not in fm: needs.append('type: concept')
    if 'updated:' not in fm: needs.append('updated: 2026-07-08')
    if needs:
        fm += '\n' + '\n'.join(needs) + '\n'
        text = re.sub(r'^---\n.*?\n---\n', f'---\n{fm}---\n', text, count=1, flags=re.DOTALL)
        p.write_text(text, encoding='utf-8')
        fm2_fixed += 1
print(f"Frontmatter fields added: {fm2_fixed}")

# ============================================================
# FIX 7: Add missing pages to index.md
# ============================================================
idx_content = INDEX.read_text(encoding='utf-8')
idx_added = 0
for p in ROOT.rglob("*.md"):
    stem = p.stem
    if f'[[{stem}]]' not in idx_content:
        title = stem.replace('-', ' ').replace('_', ' ').title()
        if 'playbooks/' in str(p):
            marker = '## Playbooks'
        elif 'synthesis/' in str(p):
            marker = '## Synthesis'
        elif 'raw/' in str(p):
            marker = '## Raw'
        elif 'schema/' in str(p):
            marker = '## Schema'
        else:
            marker = '## Concepts'
        if marker in idx_content:
            pos = idx_content.find(marker) + len(marker) + 1
            pos = idx_content.find('\n', pos) + 1
            entry = f"- [[{stem}]] — {title}\n"
            if entry not in idx_content:
                idx_content = idx_content[:pos] + entry + idx_content[pos:]
                idx_added += 1
INDEX.write_text(idx_content, encoding='utf-8')
print(f"Index entries added: {idx_added}")

print("\n=== ALL FIXES COMPLETE ===")
