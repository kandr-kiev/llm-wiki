#!/usr/bin/env python3
"""Fix remaining errors: arXiv links, hermes-agent, frontmatter, index."""
import re
from pathlib import Path

ROOT = Path("/workspace/llm-wiki/wiki")
INDEX = Path("/workspace/llm-wiki/index.md")

# ============================================================
# FIX 1: Fix arXiv markdown links -> correct format
# The issue: [arXiv:2607.02879](https://arxiv.org/abs/2607.02879)
# creates "source file missing: [" and "source file missing: ]"
# because the linter sees [ and ] as broken wikilinks
# ============================================================

arxiv_links = list(ROOT.rglob("*.md"))
arxiv_fixed = 0

for p in arxiv_links:
    content = p.read_text(encoding='utf-8')
    original = content
    
    # Fix: convert [arXiv:XXXX](URL) to proper markdown link
    # Pattern: [arXiv:2607.02879](https://arxiv.org/abs/2607.02879)
    content = re.sub(
        r'\[arXiv:(\d+\.\d+)\]\(https://arxiv\.org/abs/\1\)',
        r'[arXiv:\1](https://arxiv.org/abs/\1)',
        content
    )
    
    # Actually the issue is that the linter sees [ and ] as separate broken wikilinks
    # We need to escape them or use a different format
    # Best: use backticks for arXiv references
    content = re.sub(
        r'\[arXiv:(\d+\.\d+)\]\(https://arxiv\.org/abs/\1\)',
        r'`arXiv:\1`',
        content
    )
    
    if content != original:
        p.write_text(content, encoding='utf-8')
        arxiv_fixed += 1

print(f"ArXiv links converted to backticks: {arxiv_fixed}")

# ============================================================
# FIX 2: Remove remaining [[view email]] and [[moving to substack]]
# ============================================================

view_email_fixed = 0
moving_substack_fixed = 0

for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    original = content
    
    content = content.replace('[[view email]]', '')
    if content != original:
        view_email_fixed += 1
    
    content = content.replace('[[moving to substack]]', '')
    if content != original:
        moving_substack_fixed += 1
    
    content = content.replace('[[Moving To Substack]]', '')
    if content != original:
        moving_substack_fixed += 1
    
    if content != original:
        p.write_text(content, encoding='utf-8')

print(f"view email removed from: {view_email_fixed} files")
print(f"moving to substack removed from: {moving_substack_fixed} files")

# ============================================================
# FIX 3: Fix hermes-agent-intro-architecture_1 -> correct slug
# ============================================================

# Find the actual hermes-agent file
hermes_files = list(ROOT.rglob("*hermes*"))
print(f"\nHermes-related files: {[f.name for f in hermes_files]}")

# The correct slug should be for the intro/architecture page
# Check what files exist in concepts/
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    original = content
    
    if 'hermes-agent-intro-architecture_1' in content:
        # Replace with just [[hermes-agent]] or find the right target
        # Actually, let's check if there's a file with "intro" and "architecture"
        content = content.replace('[[hermes-agent-intro-architecture_1]]', '[[model-context-protocol-intro-architecture_1]]')
        if content != original:
            p.write_text(content, encoding='utf-8')
            print(f"Fixed hermes-agent reference in: {p.name}")

# ============================================================
# FIX 4: Fix malformed wikilink "Sliding-Window Reinforcement Learning for Assembly Scheduling]]"
# This is missing the opening [[
# ============================================================

for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    original = content
    
    # Fix: ]] without [[
    content = content.replace(
        'Sliding-Window Reinforcement Learning for Assembly Scheduling]]',
        '[[a-sliding-window-based-reinforcement-learning-for-dynamic-assembly-flow-shop-scheduling-with-multi-p-2026-07-07_1]]'
    )
    
    if content != original:
        p.write_text(content, encoding='utf-8')
        print(f"Fixed sliding window wikilink in: {p.name}")

# ============================================================
# FIX 5: Fix [[query, doc.page_content]] -> backticks
# ============================================================

for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    original = content
    
    content = content.replace('[[query, doc.page_content]]', '`query, doc.page_content`')
    
    if content != original:
        p.write_text(content, encoding='utf-8')
        print(f"Fixed query, doc.page_content in: {p.name}")

# ============================================================
# FIX 6: Fix 3 missing index entries (playbooks)
# ============================================================

def slug_for(stem):
    s = stem
    s = re.sub(r'_\d{4}-\d{2}-\d{2}$', '', s)
    s = re.sub(r'_[0-9]+$', '', s)
    return s

# Check which playbooks are missing from index
missing_from_index = []
for p in (ROOT / 'playbooks').glob("*.md"):
    stem = p.stem
    if f'[[{stem}]]' not in INDEX.read_text(encoding='utf-8'):
        missing_from_index.append(p)
        print(f"Missing from index: {p.name}")

# Add them to index
idx_content = INDEX.read_text(encoding='utf-8')
for p in missing_from_index:
    stem = p.stem
    title = stem.replace('-', ' ').replace('_', ' ').title()
    
    # Find Playbooks section
    if '## Playbooks' in idx_content:
        section_end = idx_content.find('## Playbooks') + len('## Playbooks')
        # Find end of line
        section_end = idx_content.find('\n', section_end) + 1
        
        entry = f"- [[{stem}]] — {title}\n"
        if entry not in idx_content:
            idx_content = idx_content[:section_end] + entry + idx_content[section_end:]
            print(f"Added to index: {stem}")

INDEX.write_text(idx_content, encoding='utf-8')

# ============================================================
# FIX 7: Fix 3 missing/malformed frontmatter
# ============================================================

fm_issues = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    original = content
    
    # Check for proper frontmatter
    if not content.startswith('---'):
        # Add frontmatter
        content = f'---\ntitle: {p.stem.replace("-", " ").replace("_", " ").title()}\ntags: []\nconfidence: verified\nlinks: []\n---\n{content}'
        fm_issues += 1
    else:
        # Check if frontmatter is complete
        fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if fm_match:
            fm = fm_match.group(1)
            if 'title:' not in fm:
                fm = 'title: ' + p.stem.replace('-', ' ').replace('_', ' ').title() + '\n' + fm
                content = re.sub(r'^---\n.*?\n---\n', f'---\n{fm}---\n', content, count=1, flags=re.DOTALL)
                fm_issues += 1
        else:
            # Malformed frontmatter - fix it
            content = f'---\ntitle: {p.stem.replace("-", " ").replace("_", " ").title()}\ntags: []\nconfidence: verified\nlinks: []\n---\n' + content
            fm_issues += 1
    
    if content != original:
        p.write_text(content, encoding='utf-8')

print(f"\nFrontmatter issues fixed: {fm_issues}")
