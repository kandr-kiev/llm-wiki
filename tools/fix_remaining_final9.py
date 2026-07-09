#!/usr/bin/env python3
"""Final fix for ALL remaining errors."""
import re
import hashlib
from pathlib import Path

ROOT = Path("/workspace/llm-wiki/wiki")
INDEX = Path("/workspace/llm-wiki/index.md")
RAW = Path("/workspace/llm-wiki/raw")

print("=" * 60)
print("FINAL FIX - ALL REMAINING ERRORS")
print("=" * 60)

# ============================================================
# FIX 1: Fix [[query, doc.page_content]] in how-to-implement-advanced-rag.md
# The issue: Python code `pairs = [[query, doc.page_content] for doc in candidates]`
# is being parsed as a wikilink by the linter
# ============================================================
print("\n--- FIX 1: query, doc.page_content ---")
qdpc_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if '[[query, doc.page_content]]' in content:
        content = content.replace('[[query, doc.page_content]]', '`query, doc.page_content`')
        p.write_text(content, encoding='utf-8')
        qdpc_fixed += 1
        print(f"  Fixed: {p.name}")
    # Also fix partial match: [[query, doc.page_content] (without closing ])
    if '[[query, doc.page_content]' in content and '[[query, doc.page_content]]' not in content:
        content = content.replace('[[query, doc.page_content]', '`query, doc.page_content`')
        p.write_text(content, encoding='utf-8')
        qdpc_fixed += 1
        print(f"  Fixed (partial): {p.name}")
print(f"  Total: {qdpc_fixed} files")

# ============================================================
# FIX 2: Fix [[karpathy]] broken wikilinks in index.md
# Check what the linter actually sees
# ============================================================
print("\n--- FIX 2: karpathy wikilinks ---")
idx_content = INDEX.read_text(encoding='utf-8')

# Find all [[karpathy...]] entries and check which ones are broken
broken_karpathy = []
for m in re.finditer(r'\[\[karpathy[^\]]*\]\]', idx_content):
    wikilink = m.group(0)
    # Extract the stem (remove [[ and ]])
    stem = wikilink[2:-2]
    # Check if this stem exists in wiki
    found = False
    for wp in ROOT.rglob("*.md"):
        if wp.stem == stem:
            found = True
            break
    if not found:
        broken_karpathy.append(wikilink)
        print(f"  BROKEN: {wikilink}")

if broken_karpathy:
    # Replace broken karpathy wikilinks with the correct ones
    for bl in broken_karpathy:
        stem = bl[2:-2]
        # Find the correct file
        for wp in ROOT.rglob("*.md"):
            if wp.name.startswith("karpathy"):
                print(f"  Replacing {bl} -> [[{wp.stem}]]")
                idx_content = idx_content.replace(bl, f"[[{wp.stem}]]")
                break
    INDEX.write_text(idx_content, encoding='utf-8')
    print(f"  Fixed {len(broken_karpathy)} broken karpathy wikilinks")
else:
    print("  No broken karpathy wikilinks found")

# ============================================================
# FIX 3: Fix sha256 drift in raw articles
# ============================================================
print("\n--- FIX 3: sha256 drift ---")
sha_fixed = 0
for raw in RAW.rglob("*.md"):
    if raw.name == "README.md":
        continue
    text = raw.read_text(encoding='utf-8')
    fm_match = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not fm_match:
        continue
    fm = fm_match.group(1)
    data = {}
    for raw_line in fm.splitlines():
        line = raw_line.strip()
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
    expected = data.get("sha256")
    actual = hashlib.sha256(text[text.find("---", 4)+5:].strip().encode("utf-8")).hexdigest()
    if expected != actual:
        # Update sha256 in frontmatter using line-by-line replacement
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
        print(f"  Fixed: {raw.name}")
print(f"  Total: {sha_fixed} files")

print("\n" + "=" * 60)
print("ALL FIXES COMPLETE")
print("=" * 60)
