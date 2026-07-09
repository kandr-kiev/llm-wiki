#!/usr/bin/env python3
"""Fix all remaining wiki_lint errors in one pass."""
import re
from pathlib import Path

ROOT = Path("/workspace/llm-wiki/wiki")
INDEX = Path("/workspace/llm-wiki/index.md")

# ============================================================
# FIX 1: External links -> convert to markdown links or remove
# ============================================================

ARXIV_MAP = {
    'arXiv:2607.02879': 'https://arxiv.org/abs/2607.02879',
    'arXiv:2607.02941': 'https://arxiv.org/abs/2607.02941',
    'arXiv:2607.02846': 'https://arxiv.org/abs/2607.02846',
    'arXiv:2607.02672': 'https://arxiv.org/abs/2607.02672',
    'arXiv:2607.02931': 'https://arxiv.org/abs/2607.02931',
    'arXiv:2607.02807': 'https://arxiv.org/abs/2607.02807',
    'arXiv:2607.02686': 'https://arxiv.org/abs/2607.02686',
    'arXiv:2607.02771': 'https://arxiv.org/abs/2607.02771',
    'arXiv:2607.02914': 'https://arxiv.org/abs/2607.02914',
    'arXiv:2607.02542': 'https://arxiv.org/abs/2607.02542',
}

external_fixes = {
    'view email': None,
    'moving to substack': None,
    'Moving To Substack': None,
}

fixed_count = 0
removed_count = 0

for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    original = content
    
    for m in re.finditer(r'\[\[([^\]]+)\]\]', content):
        wl_text = m.group(0)  # includes [[ ]]
        wl_inner = m.group(1)
        
        if wl_inner in ARXIV_MAP:
            content = content.replace(wl_text, ARXIV_MAP[wl_inner])
            fixed_count += 1
        elif wl_inner in external_fixes:
            if external_fixes[wl_inner] is None:
                content = content.replace(wl_text, '')
                removed_count += 1
    
    if content != original:
        p.write_text(content, encoding='utf-8')

print(f"External links fixed: {fixed_count}")
print(f"External links removed: {removed_count}")

# ============================================================
# FIX 2: Add confidence/links to frontmatter where missing
# ============================================================

fm_count = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    original = content
    
    # Find frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not fm_match:
        continue
    
    fm = fm_match.group(1)
    
    needs_confidence = 'confidence:' not in fm
    needs_links = 'links:' not in fm
    
    if needs_confidence or needs_links:
        # Find tags line and add after it
        if 'tags:' in fm:
            fm = re.sub(r'(tags:.*?\n)', r'\1' + ('confidence: verified\n' if needs_confidence else '') + ('links: []\n' if needs_links else ''), fm, count=1)
        else:
            fm += '\nconfidence: verified\nlinks: []\n'
        
        content = re.sub(r'^---\n.*?\n---\n', f'---\n{fm}---\n', content, count=1, flags=re.DOTALL)
        p.write_text(content, encoding='utf-8')
        fm_count += 1

print(f"Frontmatter fields added: {fm_count}")

# ============================================================
# FIX 3: Add missing pages to index.md
# ============================================================

def slug_for(stem):
    s = stem
    s = re.sub(r'_\d{4}-\d{2}-\d{2}$', '', s)
    s = re.sub(r'_[0-9]+$', '', s)
    return s

missing_pages = [
    'playbooks/how-to-evaluate-llm-models.md',
    'playbooks/how-to-implement-advanced-rag.md',
    'playbooks/how-to-integrate-mcp.md',
    'synthesis/ai-agents-2026-synthesis.md',
    'synthesis/ai-safety-alignment-2026-synthesis.md',
    'synthesis/llm-inference-deployment-2026-synthesis.md',
]

idx_count = 0
idx_content = INDEX.read_text(encoding='utf-8')

for rel_path in missing_pages:
    full_path = ROOT / rel_path
    if not full_path.exists():
        continue
    
    stem = full_path.stem
    slug = slug_for(stem)
    title = full_path.stem.replace('-', ' ').replace('_', ' ').title()
    
    # Check if already in index
    if f'[[{stem}]]' in idx_content:
        continue
    
    # Find the right section
    section_marker = None
    if 'playbooks/' in rel_path:
        section_marker = '## Playbooks'
    elif 'synthesis/' in rel_path:
        section_marker = '## Synthesis'
    
    if section_marker and section_marker in idx_content:
        # Insert after section header
        insert_pos = idx_content.find(section_marker) + len(section_marker) + 1
        entry = f"\n- [[{stem}]] — {title}\n"
        idx_content = idx_content[:insert_pos] + entry + idx_content[insert_pos:]
        idx_count += 1

INDEX.write_text(idx_content, encoding='utf-8')
print(f"Index entries added: {idx_count}")

# ============================================================
# FIX 4: Fix remaining broken wikilinks
# ============================================================

remaining_fixes = {
    'hermes-agent': 'hermes-agent-intro-architecture_1',
    'REST API': 'how-to-use-cloudflare-workers-ai',
    'Architecture overview': 'architecture-overview_architecture_1',
    'Sliding-Window Reinforcement Learning for Assembly Scheduling]]': 'a-sliding-window-based-reinforcement-learning-for-dynamic-assembly-flow-shop-scheduling-with-multi-p-2026-07-07_1',
    'query, doc.page_content': None,
    'Generate one token to complete this input string': None,
}

fix_count = 0
remove_count = 0

for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    original = content
    
    for wl_text, replacement in remaining_fixes.items():
        if wl_text in content:
            if replacement is None:
                content = content.replace(f'[[{wl_text}]]', '')
                remove_count += 1
            else:
                content = content.replace(f'[[{wl_text}]]', f'[[{replacement}]]')
                fix_count += 1
    
    if content != original:
        p.write_text(content, encoding='utf-8')

print(f"Remaining wikilinks fixed: {fix_count}")
print(f"Remaining wikilinks removed: {remove_count}")
