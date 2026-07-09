#!/usr/bin/env python3
"""Fix comparison files: add empty sources field where it's missing entirely."""
import re
from pathlib import Path

WIKI_DIR = Path("/workspace/llm-wiki/wiki/comparisons")

fixed_count = 0

for fpath in sorted(WIKI_DIR.glob("*.md")):
    content = fpath.read_text(encoding="utf-8")
    
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not fm_match:
        continue
    
    fm_text = fm_match.group(1)
    body = fm_match.group(2)
    
    has_sources = bool(re.search(r'^sources:', fm_text, re.MULTILINE))
    
    if not has_sources:
        # Add empty sources after tags
        lines = fm_text.split('\n')
        new_lines = []
        added = False
        for line in lines:
            new_lines.append(line)
            if not added and line.strip() == '':
                new_lines.append('sources: []')
                added = True
        
        if not added:
            new_lines.append('sources: []')
        
        new_fm = '\n'.join(new_lines)
        new_content = f'---\n{new_fm}\n---\n{body}'
        fpath.write_text(new_content, encoding="utf-8")
        fixed_count += 1
        print(f"ADDED sources: []: {fpath.name}")

print(f"\nDone: {fixed_count} fixed")
