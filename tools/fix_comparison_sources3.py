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
    
    # Check if sources line exists (not just sources: [])
    sources_match = re.search(r'^sources:\s*\[.*\]', fm_text, re.MULTILINE)
    has_sources = bool(sources_match)
    
    if not has_sources:
        # Find the last closing --- line in frontmatter
        # Insert sources: [] before the closing ---
        lines = fm_text.split('\n')
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if line.strip() == '' and not any(l.startswith('sources:') for l in new_lines):
                new_lines.append('sources: []')
        
        new_fm = '\n'.join(new_lines)
        new_content = f'---\n{new_fm}\n---\n{body}'
        fpath.write_text(new_content, encoding="utf-8")
        fixed_count += 1
        print(f"ADDED sources: []: {fpath.name}")

print(f"\nDone: {fixed_count} fixed")
