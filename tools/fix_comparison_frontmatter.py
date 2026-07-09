#!/usr/bin/env python3
"""Fix comparison files: add missing frontmatter fields and register in root index.md."""
import re, os, glob
from pathlib import Path

WIKI_DIR = Path("/workspace/llm-wiki/wiki/comparisons")
ROOT_INDEX = Path("/workspace/llm-wiki/index.md")
TODAY = "2026-07-08"

# Read root index
root_index_text = ROOT_INDEX.read_text(encoding="utf-8")

# Find where comparisons section starts
comp_section_match = re.search(r'(## Comparisons\n)', root_index_text)
if not comp_section_match:
    # Find Concepts section and insert Comparisons after it
    concepts_match = re.search(r'(## Concepts\n)', root_index_text)
    if concepts_match:
        insert_pos = concepts_match.end()
        comp_marker = '\n## Comparisons\n\n'
    else:
        insert_pos = len(root_index_text)
        comp_marker = '\n## Comparisons\n\n'
else:
    insert_pos = comp_section_match.end()
    comp_marker = ""

new_entries = []
fixed_count = 0
skipped_count = 0

for fpath in sorted(WIKI_DIR.glob("*.md")):
    content = fpath.read_text(encoding="utf-8")
    
    # Extract existing frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not fm_match:
        print(f"SKIP (no frontmatter): {fpath.name}")
        skipped_count += 1
        continue
    
    fm_text = fm_match.group(1)
    body = fm_match.group(2)
    
    # Check what's missing
    has_type = bool(re.search(r'^type:', fm_text, re.MULTILINE))
    has_title = bool(re.search(r'^title:', fm_text, re.MULTILINE))
    has_confidence = bool(re.search(r'^confidence:', fm_text, re.MULTILINE))
    has_created = bool(re.search(r'^created:', fm_text, re.MULTILINE))
    has_updated = bool(re.search(r'^updated:', fm_text, re.MULTILINE))
    has_description = bool(re.search(r'^description:', fm_text, re.MULTILINE))
    has_sources = bool(re.search(r'^sources:', fm_text, re.MULTILINE))
    has_links = bool(re.search(r'^links:', fm_text, re.MULTILINE))
    
    # Extract title for slug
    title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm_text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else fpath.stem
    
    # Generate slug from title
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    
    # Fix: add missing fields
    lines = fm_text.split('\n')
    new_lines = []
    for line in lines:
        new_lines.append(line)
        if line.startswith('tags:') or line.startswith('tags: ['):
            # Insert after tags
            if not has_type:
                new_lines.append('type: comparison')
            if not has_description:
                new_lines.append(f'description: Comparison page for {title}')
            if not has_sources:
                new_lines.append(f'sources: [raw/articles/{fpath.stem}.md]')
            if not has_links:
                new_lines.append('links: []')
            break
        elif line.strip() == '' and not has_type:
            new_lines.append('type: comparison')
    
    # Add missing fields at end if not added in loop
    if not has_type:
        new_lines.append('type: comparison')
    if not has_description:
        new_lines.append(f'description: Comparison page for {title}')
    if not has_sources:
        new_lines.append(f'sources: [raw/articles/{fpath.stem}.md]')
    if not has_links:
        new_lines.append('links: []')
    if not has_confidence:
        new_lines.append('confidence: medium')
    if not has_created:
        new_lines.append('created: ' + TODAY)
    if not has_updated:
        new_lines.append('updated: ' + TODAY)
    
    new_fm = '\n'.join(new_lines)
    new_content = f'---\n{new_fm}\n---\n{body}'
    
    # Write back
    fpath.write_text(new_content, encoding="utf-8")
    fixed_count += 1
    
    # Build index entry
    entry = f"- [[{slug}]] — {title}"
    new_entries.append(entry)
    print(f"FIXED: {fpath.name} (slug={slug})")

# Write new entries to root index
if new_entries:
    insert_text = comp_marker + '\n'.join(new_entries) + '\n'
    root_index_text = root_index_text[:insert_pos] + insert_text + root_index_text[insert_pos:]
    ROOT_INDEX.write_text(root_index_text, encoding="utf-8")
    print(f"\nWrote {len(new_entries)} entries to root index.md")

print(f"\nDone: {fixed_count} fixed, {skipped_count} skipped")
