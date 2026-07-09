#!/usr/bin/env python3
"""Fix sha256 drift using the EXACT same logic as wiki_lint.py."""
import hashlib
from pathlib import Path

RAW = Path("/workspace/llm-wiki/raw")

def split_frontmatter(text):
    """Same as wiki_lint.py."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end+5:]

def parse_simple_yaml(fm):
    """Same as wiki_lint.py."""
    data = {}
    for raw in fm.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            data[key] = [x.strip().strip('"\'') for x in inner.split(",") if x.strip()]
        else:
            data[key] = value.strip('"\'')
    return data

sha_fixed = 0
for raw in RAW.rglob("*.md"):
    if raw.name == "README.md":
        continue
    text = raw.read_text(encoding='utf-8')
    fm, body = split_frontmatter(text)
    if fm is None:
        continue
    
    data = parse_simple_yaml(fm)
    expected = data.get("sha256")
    if not expected:
        continue
    
    actual = hashlib.sha256(body.strip().encode("utf-8")).hexdigest()
    
    if expected != actual:
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
