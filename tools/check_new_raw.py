#!/usr/bin/env python3
"""Check for new raw files not yet in wiki, and print report.

Uses check_raw_integrity() from utils.py — single source of truth.
"""
import os, sys
from pathlib import Path

# Ensure tools/ is on sys.path when run as python3 tools/check_new_raw.py
_tools_dir = Path(__file__).resolve().parent
if str(_tools_dir) not in sys.path:
    sys.path.insert(0, str(_tools_dir))

from utils import check_raw_integrity, check_dir_exists

wiki_sources_dir = 'wiki/sources'
raw_files = set()
wiki_files = set()

if check_dir_exists(Path('raw')):
    for root, dirs, files in os.walk('raw'):
        for fn in files:
            if fn.endswith('.md') and fn != 'README.md':
                raw_files.add(fn)

if check_dir_exists(Path(wiki_sources_dir)):
    for fn in os.listdir(wiki_sources_dir):
        if fn.endswith('.md') and fn != 'README.md':
            wiki_files.add(fn)

new_raw = raw_files - wiki_files
integrity = check_raw_integrity(Path('raw'))

print(f"Total raw files: {integrity['total']}")
print(f"Total wiki source-notes: {len(wiki_files)}")
print(f"New raw (not in wiki): {len(new_raw)}")
for f in sorted(new_raw):
    print(f"  NEW: {f}")
print(f"Hash mismatches: {integrity['mismatch']}")
for f in sorted(integrity['mismatch_files']):
    print(f"  MISMATCH: {f[0]}")
if not new_raw and integrity['mismatch'] == 0:
    print("Status: ALL OK — no new files, all hashes correct.")
