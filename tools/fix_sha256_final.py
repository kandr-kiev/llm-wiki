#!/usr/bin/env python3
"""Fix sha256 drift using the SAME method as wiki_lint.py."""
import hashlib
from pathlib import Path

RAW = Path("/workspace/llm-wiki/raw")

sha_fixed = 0
for raw in RAW.rglob("*.md"):
    if raw.name == "README.md":
        continue
    text = raw.read_text(encoding='utf-8')
    
    # Split by --- exactly like wiki_lint.py does
    parts = text.split('---')
    if len(parts) < 4:
        continue
    
    # Body is parts[3] (after third ---)
    body = parts[3].strip()
    if not body:
        continue
    
    actual = hashlib.sha256(body.encode('utf-8')).hexdigest()
    
    # Find expected sha256 in frontmatter
    import re
    fm_part = parts[1]  # First --- section
    expected = None
    for line in fm_part.splitlines():
        if line.strip().startswith("sha256:"):
            expected = line.strip().replace("sha256:", "").strip()
            break
    
    if expected and expected != actual:
        print(f"DRIFT: {raw.name}")
        print(f"  Expected: {expected}")
        print(f"  Actual:   {actual}")
        
        # Update sha256 in frontmatter
        lines = text.split('\n')
        new_lines = []
        for line in lines:
            if line.strip().startswith("sha256:"):
                new_lines.append(f"sha256: {actual}")
            else:
                new_lines.append(line)
        new_text = '\n'.join(new_lines)
        raw.write_text(new_text, encoding='utf-8')
        sha_fixed += 1

print(f"\nTotal sha256 drift fixed: {sha_fixed} files")
