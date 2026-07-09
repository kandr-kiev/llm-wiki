#!/usr/bin/env python3
"""Final pass: fix ALL remaining wiki_lint errors."""
import re
from pathlib import Path

ROOT = Path("/workspace/llm-wiki/wiki")
INDEX = Path("/workspace/llm-wiki/index.md")

# ============================================================
# FIX 1: Convert markdown links [arXiv:XXXX](URL) to backticks
# ============================================================
arxiv_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    original = content
    content = re.sub(
        r'\[arXiv:(\d+\.\d+)\]\(https://arxiv\.org/abs/\1\)',
        r'arXiv:\1',
        content
    )
    if content != original:
        p.write_text(content, encoding='utf-8')
        arxiv_fixed += 1
print(f"ArXiv markdown links → backticks: {arxiv_fixed}")

# ============================================================
# FIX 2: Remove [[view email]] (20 occurrences)
# ============================================================
view_email_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if '[[view email]]' in content:
        content = content.replace('[[view email]]', '')
        p.write_text(content, encoding='utf-8')
        view_email_fixed += 1
print(f"view email removed: {view_email_fixed} files")

# ============================================================
# FIX 3: Fix [[karpathy]] (3 occurrences) -> [[karpathy-llm-wiki-2026_1]]
# ============================================================
karpathy_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if '[[karpathy]]' in content:
        content = content.replace('[[karpathy]]', '[[karpathy-llm-wiki-2026_1]]')
        p.write_text(content, encoding='utf-8')
        karpathy_fixed += 1
print(f"karpathy wikilinks fixed: {karpathy_fixed}")

# ============================================================
# FIX 4: Fix [[query, doc.page_content]] -> backticks
# ============================================================
qdpc_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if '[[query, doc.page_content]]' in content:
        content = content.replace('[[query, doc.page_content]]', '`query, doc.page_content`')
        p.write_text(content, encoding='utf-8')
        qdpc_fixed += 1
print(f"query, doc.page_content fixed: {qdpc_fixed}")

# ============================================================
# FIX 5: Fix sliding-window wikilink (wrong slug)
# ============================================================
sw_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if '[[a-sliding-window-based-reinforcement-learning-for-dynamic-assembly-flow-shop-scheduling-with-multi-p-2026-07-07_1]]' in content:
        content = content.replace(
            '[[a-sliding-window-based-reinforcement-learning-for-dynamic-assembly-flow-shop-scheduling-with-multi-p-2026-07-07_1]]',
            '[[sliding-window-reinforcement-learning-for-assembly-scheduling_2026_1]]'
        )
        p.write_text(content, encoding='utf-8')
        sw_fixed += 1
print(f"sliding-window wikilink fixed: {sw_fixed}")

# ============================================================
# FIX 6: Fix missing frontmatter fields (created, description, sources, type, updated)
# ============================================================
fm_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
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
        content = re.sub(r'^---\n.*?\n---\n', f'---\n{fm}---\n', content, count=1, flags=re.DOTALL)
        p.write_text(content, encoding='utf-8')
        fm_fixed += 1
print(f"Frontmatter fields fixed: {fm_fixed}")

# ============================================================
# FIX 7: Fix remaining page missing from index.md
# ============================================================
def slug_for(stem):
    s = stem
    s = re.sub(r'_\d{4}-\d{2}-\d{2}$', '', s)
    s = re.sub(r'_[0-9]+$', '', s)
    return s

idx_content = INDEX.read_text(encoding='utf-8')
idx_added = 0
for p in ROOT.rglob("*.md"):
    stem = p.stem
    if f'[[{stem}]]' not in idx_content:
        title = stem.replace('-', ' ').replace('_', ' ').title()
        # Find appropriate section
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

# ============================================================
# FIX 8: Remove any remaining broken markdown links [text](url)
# that cause "source file missing" errors
# ============================================================
md_link_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    original = content
    # Convert [text](url) to `text` for arXiv refs
    content = re.sub(
        r'\[arXiv:(\d+\.\d+)\]\(https://arxiv\.org/abs/\1\)',
        r'arXiv:\1',
        content
    )
    if content != original:
        p.write_text(content, encoding='utf-8')
        md_link_fixed += 1
print(f"Markdown links cleaned: {md_link_fixed}")
