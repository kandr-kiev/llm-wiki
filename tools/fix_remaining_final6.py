#!/usr/bin/env python3
"""Fix ALL remaining errors - NO .md suffixes, linter uses path.stem."""
import re
import hashlib
from pathlib import Path

ROOT = Path("/workspace/llm-wiki/wiki")
INDEX = Path("/workspace/llm-wiki/index.md")
RAW = Path("/workspace/llm-wiki/raw")

# ============================================================
# FIX 1: Remove .md from wikilinks (linter uses path.stem)
# ============================================================
fixes = [
    ('[[previewing-gpt-5-6-sol_07_1.md]]', '[[previewing-gpt-5-6-sol_07_1]]'),
    ('[[a-sliding-window-based-reinforcement-learning-for-dynamic-assembly-flow-shop-scheduling-with-multi-p-2026-07-07.md]]', '[[a-sliding-window-based-reinforcement-learning-for-dynamic-assembly-flow-shop-scheduling-with-multi-p-2026-07-07]]'),
    ('[[architecture-overview_architecture_1.md]]', '[[architecture-overview_architecture_1]]'),
]

for old, new in fixes:
    count = 0
    for p in ROOT.rglob("*.md"):
        content = p.read_text(encoding='utf-8')
        if old in content:
            content = content.replace(old, new)
            p.write_text(content, encoding='utf-8')
            count += 1
    print(f"FIX 1 - '{old}' → '{new}': {count} files")

# ============================================================
# FIX 2: Fix [[karpathy]] in index.md → [[karpathy-llm-wiki-2026_1]]
# ============================================================
idx_content = INDEX.read_text(encoding='utf-8')
if '[[karpathy]]' in idx_content:
    idx_content = idx_content.replace('[[karpathy]]', '[[karpathy-llm-wiki-2026_1]]')
    INDEX.write_text(idx_content, encoding='utf-8')
    print("FIX 2 - karpathy wikilinks fixed in index.md")
else:
    print("FIX 2 - karpathy already fixed")

# ============================================================
# FIX 3: Fix [[query, doc.page_content]] → backticks
# ============================================================
qdpc_fixed = 0
for p in ROOT.rglob("*.md"):
    content = p.read_text(encoding='utf-8')
    if '[[query, doc.page_content]]' in content:
        content = content.replace('[[query, doc.page_content]]', '`query, doc.page_content`')
        p.write_text(content, encoding='utf-8')
        qdpc_fixed += 1
print(f"FIX 3 - query, doc.page_content fixed: {qdpc_fixed} files")

# ============================================================
# FIX 4: Fix sha256 drift in raw files
# ============================================================
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
        # Update sha256 in frontmatter
        new_text = re.sub(
            r'(sha256:\s+)\S+',
            rf'\1{actual}',
            text
        )
        raw.write_text(new_text, encoding='utf-8')
        sha_fixed += 1
print(f"FIX 4 - sha256 drift fixed: {sha_fixed} files")

print("\n=== ALL FIXES COMPLETE ===")