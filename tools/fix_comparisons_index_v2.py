#!/usr/bin/env python3
"""Correctly add [[page.stem]] entries for all wiki/comparisons pages to root index.md."""
import re
from pathlib import Path

ROOT = Path("/workspace/llm-wiki")
INDEX = ROOT / "index.md"

index_text = INDEX.read_text(encoding="utf-8")
comparisons_dir = ROOT / "wiki" / "comparisons"

# Find Comparisons section
comp_match = re.search(r'(## Comparisons\n)', index_text)
if comp_match:
    insert_pos = comp_match.end()
else:
    concepts_match = re.search(r'(## Concepts\n)', index_text)
    insert_pos = concepts_match.end() if concepts_match else len(index_text)

# Collect comparison pages missing from index
missing = []
for p in sorted(comparisons_dir.glob("*.md")):
    stem = p.stem
    wikilink = f"[[{stem}]]"
    if wikilink not in index_text:
        missing.append((p, stem, wikilink))

print(f"Found {len(missing)} comparison pages missing from index.md")

# Add entries — compute wikilink inside loop!
new_entries = []
for p, stem, wikilink in missing:
    new_entries.append(f"- {wikilink} — {p.name.replace('.md', '')}")

if new_entries:
    insert_text = '\n'.join(new_entries) + '\n'
    index_text = index_text[:insert_pos] + insert_text + index_text[insert_pos:]
    INDEX.write_text(index_text, encoding="utf-8")
    print(f"Added {len(new_entries)} entries to index.md")
    # Verify
    for p, stem, wikilink in missing[:5]:
        found = wikilink in index_text
        print(f"  VERIFY {stem}: {'OK' if found else 'MISSING'}")
else:
    print("No entries to add")
