#!/usr/bin/env python3
"""Fix broken wikilinks where ] appears inside [[Issue #...]] titles.

Converts [[Issue #123: some text with ] inside]] to [Issue #123: some text with ] inside](url).
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"

def fix_file(filepath):
    """Fix broken wikilinks in a single file."""
    content = filepath.read_text(encoding="utf-8")
    original = content
    
    # Pattern: [[Issue #DIGIT: text with ] possibly more text]]
    # We need to find the LAST ]]] to handle nested brackets
    # Match [[Issue #\d+: ... ]] where ... may contain ]
    pattern = r'\[\[(Issue #\d+: [^\]]*(?:\[[^\]]*\])?[^\]]*)\]\]'
    
    # Also handle simpler case: [[Issue #DIGIT: text without ]]]
    pattern2 = r'\[\[(Issue #\d+: [^\]]+)\]\]'
    
    count = 0
    # First pass: handle cases with nested [[
    for m in re.finditer(r'\[\[(Issue #\d+: [^\]]*(?:\[[^\]]*\])?[^\]]*)\]\]', content):
        issue_text = m.group(1)
        # Extract issue number
        num_match = re.match(r'Issue #(\d+)', issue_text)
        if num_match:
            issue_num = num_match.group(1)
            # Convert to markdown link
            markdown_link = f"[{issue_text}](https://github.com/pytorch/pytorch/issues/{issue_num})"
            content = content[:m.start()] + markdown_link + content[m.end():]
            count += 1
    
    # Second pass: handle simpler cases without nested brackets
    for m in re.finditer(pattern2, content):
        issue_text = m.group(1)
        num_match = re.match(r'Issue #(\d+)', issue_text)
        if num_match:
            issue_num = num_match.group(1)
            markdown_link = f"[{issue_text}](https://github.com/pytorch/pytorch/issues/{issue_num})"
            content = content[:m.start()] + markdown_link + content[m.end():]
            count += 1
    
    if content != original:
        filepath.write_text(content, encoding="utf-8")
        return count
    return 0

def main():
    total = 0
    for md_file in WIKI_DIR.rglob("*.md"):
        c = fix_file(md_file)
        if c > 0:
            print(f"  Fixed {md_file.name}: {c} occurrences")
            total += c
    
    print(f"\nTotal files fixed: {total}")

if __name__ == "__main__":
    main()
