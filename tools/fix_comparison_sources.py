#!/usr/bin/env python3
"""Fix comparison files: remove invalid source references."""
from pathlib import Path

WIKI_DIR = Path("/workspace/llm-wiki/wiki/comparisons")
RAW_DIR = Path("/workspace/llm-wiki/raw/articles")

fixed_count = 0
no_sources_count = 0

for fpath in sorted(WIKI_DIR.glob("*.md")):
    content = fpath.read_text(encoding="utf-8")
    
    import re
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not fm_match:
        continue
    
    fm_text = fm_match.group(1)
    body = fm_match.group(2)
    
    # Find sources line
    sources_match = re.search(r'^sources:\s*\[(.*?)\]', fm_text, re.MULTILINE)
    if not sources_match:
        continue
    
    sources_content = sources_match.group(1)
    # Parse source filenames
    source_refs = re.findall(r'raw/articles/([^,\]]+)', sources_content)
    
    # Check which sources exist
    valid_sources = []
    invalid_sources = []
    for src in source_refs:
        src_path = RAW_DIR / src
        if src_path.exists():
            valid_sources.append(f"raw/articles/{src}")
        else:
            invalid_sources.append(src)
    
    if invalid_sources:
        if valid_sources:
            new_sources = ', '.join(valid_sources)
            new_fm = fm_text.replace(sources_match.group(0), f'sources: [{new_sources}]')
        else:
            # No valid sources - remove sources line entirely
            new_fm = fm_text.replace(sources_match.group(0), '')
            new_sources = 'none'
        
        new_content = f'---\n{new_fm}\n---\n{body}'
        fpath.write_text(new_content, encoding="utf-8")
        
        if valid_sources:
            print(f"FIXED sources: {fpath.name} ({invalid_sources}) -> {new_sources}")
        else:
            print(f"REMOVED sources: {fpath.name} (no valid raw articles)")
            no_sources_count += 1
        fixed_count += 1

print(f"\nDone: {fixed_count} fixed, {no_sources_count} with no sources")
