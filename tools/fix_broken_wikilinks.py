#!/usr/bin/env python3
"""Fix broken wikilinks: normalize slug format in wiki pages."""
import re
from pathlib import Path

ROOT = Path("/workspace/llm-wiki/wiki")

def slug_for(stem):
    """Reproduce the linter's slug_for() logic."""
    stem = re.sub(r'_\d{4}-\d{2}-\d{2}$', '', stem)
    stem = re.sub(r'_\d+$', '', stem)
    stem = re.sub(r'[_]+', '-', stem)
    stem = stem.lower()
    stem = re.sub(r'[^a-z0-9\-]', '', stem)
    stem = re.sub(r'-+', '-', stem)
    return stem

# Build slug -> page map
pages = list(ROOT.rglob("*.md"))
slugs = {}
for p in pages:
    s = slug_for(p.stem)
    if s:
        slugs[s] = p

# External links that should NOT be in wikilink format
EXTERNAL_PATTERNS = [
    r'^view\s*email$',
    r'^moving\s*to\s*substack$',
    r'^arxiv[:\s]',
    r'^arXiv[:\s]',
    r'^https?://',
]

def is_external(wikilink):
    """Check if a wikilink refers to external content."""
    for pat in EXTERNAL_PATTERNS:
        if re.match(pat, wikilink, re.IGNORECASE):
            return True
    return False

# Collect all broken wikilinks across all pages
all_broken = {}
total_fixed = 0

for p in pages:
    content = p.read_text(encoding="utf-8")
    
    # Strip HTML before checking wikilinks
    clean_body = re.sub(r'<astro-island\b.*', ' ', content, flags=re.DOTALL)
    clean_body = re.sub(r'<[^>]+>', ' ', clean_body)
    
    # Find all wikilinks
    wikilinks = re.findall(r'\[\[([^\]|#]+)\]', clean_body)
    
    fixed_content = content
    changes = 0
    
    for wl in wikilinks:
        # Skip if already correct (exists as-is)
        if wl in slugs:
            continue
        
        # Skip external links
        if is_external(wl):
            continue
        
        # Try to normalize: convert to slug format
        normalized = slug_for(wl)
        
        if normalized and normalized in slugs:
            # Replace all occurrences of [[wl]] with [[normalized]]
            old = f'[[{wl}]]'
            new = f'[[{normalized}]]'
            fixed_content = fixed_content.replace(old, new)
            changes += 1
        else:
            # Track but don't fix
            key = f'[[{wl}]]'
            all_broken[key] = all_broken.get(key, 0) + 1
    
    if changes > 0:
        p.write_text(fixed_content, encoding="utf-8")
        total_fixed += changes
        print(f"FIXED {changes} wikilinks in {p.name}")

print(f"\nTotal wikilinks fixed: {total_fixed}")

# Report remaining broken
if all_broken:
    print(f"\nRemaining unresolvable broken wikilinks ({len(all_broken)} unique):")
    for wl, count in sorted(all_broken.items(), key=lambda x: -x[1])[:30]:
        print(f"  {wl} ({count} occurrences)")
