#!/usr/bin/env python3
"""Fix broken wikilinks by matching normalized stems (spaces->dashes)."""
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path("/workspace/llm-wiki/wiki")

def normalize(s):
    """Normalize a string for comparison: lowercase, remove non-alnum."""
    return re.sub(r'[^a-z0-9]', '', s.lower())

# Build stem map: normalized -> list of actual stems
pages = list(ROOT.rglob("*.md"))
stem_map = defaultdict(list)
for p in pages:
    stem = p.stem
    norm = normalize(stem)
    stem_map[norm].append(stem)

# External links that should NOT be in wikilink format
EXTERNAL_PATTERNS = [
    r'^view\s*email$',
    r'^moving\s*to\s*substack$',
    r'^arxiv[:\s]',
    r'^arXiv[:\s]',
    r'^https?://',
]

def is_external(wikilink):
    for pat in EXTERNAL_PATTERNS:
        if re.match(pat, wikilink, re.IGNORECASE):
            return True
    return False

# Collect all broken wikilinks
all_broken = defaultdict(lambda: {"count": 0, "pages": set()})
total_fixed = 0

for p in pages:
    content = p.read_text(encoding="utf-8")
    
    # Strip HTML
    clean_body = re.sub(r'<astro-island\b.*', ' ', content, flags=re.DOTALL)
    clean_body = re.sub(r'<[^>]+>', ' ', clean_body)
    
    # Find all wikilinks
    wikilinks = re.findall(r'\[\[([^\]|#]+)\]', clean_body)
    
    fixed_content = content
    changes = 0
    
    for wl in wikilinks:
        # Skip if already exists
        if wl in stem_map:
            continue
        
        # Skip external
        if is_external(wl):
            continue
        
        # Try to match: normalize and find candidates
        norm_wl = normalize(wl)
        candidates = stem_map.get(norm_wl, [])
        
        if candidates:
            # Pick the most likely (shortest stem, or latest date)
            target = candidates[0]
            old = f'[[{wl}]]'
            new = f'[[{target}]]'
            fixed_content = fixed_content.replace(old, new)
            changes += 1
        else:
            # Partial match: try with spaces replaced by dashes
            alt_wl = re.sub(r'\s+', '-', wl).strip('-')
            alt_norm = normalize(alt_wl)
            alt_candidates = stem_map.get(alt_norm, [])
            if alt_candidates:
                target = alt_candidates[0]
                old = f'[[{wl}]]'
                new = f'[[{target}]]'
                fixed_content = fixed_content.replace(old, new)
                changes += 1
            else:
                all_broken[f'[[{wl}]]']["count"] += 1
                all_broken[f'[[{wl}]]']["pages"].add(p.name)
    
    if changes > 0:
        p.write_text(fixed_content, encoding="utf-8")
        total_fixed += changes
        print(f"FIXED {changes} wikilinks in {p.name}")

print(f"\nTotal wikilinks fixed: {total_fixed}")

# Report remaining
if all_broken:
    print(f"\nRemaining unresolvable broken wikilinks ({len(all_broken)} unique):")
    for wl, info in sorted(all_broken.items(), key=lambda x: -x[1]["count"])[:30]:
        print(f"  {wl} ({info['count']} occurrences in {len(info['pages'])} files)")
