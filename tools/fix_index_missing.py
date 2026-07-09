#!/usr/bin/env python3
"""Add missing [[page.stem]] entries to root index.md for all wiki pages."""
import re
from pathlib import Path

ROOT = Path("/workspace/llm-wiki")
INDEX = ROOT / "index.md"

# Read index
index_text = INDEX.read_text(encoding="utf-8")

# Find all wiki pages
wiki_pages = list((ROOT / "wiki").rglob("*.md"))

# Find Comparisons section
comp_match = re.search(r'(## Comparisons\n)', index_text)
if comp_match:
    insert_pos = comp_match.end()
else:
    # Find Concepts section
    concepts_match = re.search(r'(## Concepts\n)', index_text)
    if concepts_match:
        insert_pos = concepts_match.end()
    else:
        insert_pos = len(index_text)

# Collect all pages missing from index
missing = []
for p in wiki_pages:
    stem = p.stem
    wikilink = f"[[{stem}]]"
    if wikilink not in index_text:
        missing.append((p, stem))

print(f"Found {len(missing)} pages missing from index.md")

# Add entries
new_entries = []
for p, stem in missing:
    rel = p.relative_to(ROOT)
    # Use filename as description
    desc = p.name.replace('.md', '')
    new_entries.append(f"- {wikilink} — {desc}")

if new_entries:
    insert_text = '\n'.join(new_entries) + '\n'
    index_text = index_text[:insert_pos] + insert_text + index_text[insert_pos:]
    INDEX.write_text(index_text, encoding="utf-8")
    print(f"Added {len(new_entries)} entries to index.md")
else:
    print("No entries to add")
