#!/usr/bin/env python3
"""Verify all hashes are correct and check raw-to-wiki mapping.

Uses check_raw_integrity() from utils.py — single source of truth.
"""
import os, sys
from pathlib import Path

_tools_dir = Path(__file__).resolve().parent
if str(_tools_dir) not in sys.path:
    sys.path.insert(0, str(_tools_dir))

from utils import check_raw_integrity, check_dir_exists

print("=== SHA256 Verification ===")
integrity = check_raw_integrity(Path('raw'))

print(f"\nAll hashes correct: {integrity['mismatch'] == 0}")
print(f"Total checked: {integrity['ok']}")
print(f"MISMATCH: {integrity['mismatch']}")
print(f"No SHA256 in frontmatter: {integrity['no_hash']}")

if integrity['mismatch_files']:
    for f in sorted(integrity['mismatch_files']):
        print(f"  MISMATCH: {f[0]} (stored={f[1]}... computed={f[2]}...)")

# Check raw-to-wiki mapping
print("\n=== Raw-to-Wiki Mapping ===")
wiki_sources_dir = 'wiki/sources'
raw_files = set()
wiki_files = set()

if check_dir_exists(Path('raw')):
    for fn in os.listdir('raw'):
        fp = os.path.join('raw', fn)
        if os.path.isfile(fp) and fn.endswith('.md') and fn != 'README.md':
            raw_files.add(fn)

if check_dir_exists(Path(wiki_sources_dir)):
    for fn in os.listdir(wiki_sources_dir):
        fp = os.path.join(wiki_sources_dir, fn)
        if os.path.isfile(fp) and fn.endswith('.md') and fn != 'README.md':
            wiki_files.add(fn)

print(f'Raw source files: {len(raw_files)}')
print(f'Wiki source-note files: {len(wiki_files)}')

missing_in_wiki = raw_files - wiki_files
extra_in_wiki = wiki_files - raw_files

if missing_in_wiki:
    print(f'\nRaw files WITHOUT wiki source-note: {len(missing_in_wiki)}')
if extra_in_wiki:
    print(f'\nWiki source-notes WITHOUT raw file: {len(extra_in_wiki)}')
if not missing_in_wiki and not extra_in_wiki:
    print('\nAll raw files have corresponding wiki source-notes. OK')
