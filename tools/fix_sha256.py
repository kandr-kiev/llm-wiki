#!/usr/bin/env python3
"""Fix SHA256 hashes in all raw article files — handles PLACEHOLDER and actual hashes."""
import hashlib, os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
raw_dir = ROOT / "raw" / "articles"

fixed = 0
skipped = 0

for fname in sorted(os.listdir(raw_dir)):
    fpath = raw_dir / fname
    text = fpath.read_text(encoding="utf-8")

    parts = text.split('---')
    if len(parts) >= 3:
        body = '---'.join(parts[2:]).strip()
    else:
        body = text.strip()
    sha = hashlib.sha256(body.encode("utf-8")).hexdigest()

    # Match sha256 line — either PLACEHOLDER or actual hash
    sha_pattern = r'^(sha256:\s*)([A-Za-z0-9_]+)'
    match = re.search(sha_pattern, text, re.MULTILINE)
    if match:
        old_val = match.group(2)
        if old_val != sha:
            new_content = text.replace(match.group(0), f'{match.group(1)}{sha}')
            fpath.write_text(new_content, encoding="utf-8")
            fixed += 1
            print(f'  FIXED: {fname} ({old_val} -> {sha[:12]}...)')
        else:
            skipped += 1
    else:
        skipped += 1

print(f'\nDone: {fixed} fixed, {skipped} skipped')
