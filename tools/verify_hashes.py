#!/usr/bin/env python3
"""Verify all hashes are now correct and check raw-to-wiki mapping."""
import hashlib, os, re

def compute_correct_sha256(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    first_dash = content.index('---')
    rest = content[first_dash+3:]
    second_dash = rest.index('---')
    body = rest[second_dash+3:].strip()
    return hashlib.sha256(body.encode()).hexdigest()

print("=== SHA256 Verification ===")
all_ok = True
for root, dirs, files in os.walk('raw'):
    for fn in sorted(files):
        if fn == 'README.md': continue
        fp = os.path.join(root, fn)
        if not fp.endswith('.md'): continue
        computed = compute_correct_sha256(fp)
        with open(fp, 'r') as f:
            first_lines = f.read(300)
        m = re.search(r'sha256:\s*([a-f0-9]{64})', first_lines)
        stored = m.group(1) if m else 'NONE'
        match = 'OK' if computed == stored else 'MISMATCH'
        if match != 'OK': all_ok = False
        print(f'  {match} | {fp}')

print(f'\nAll hashes correct: {all_ok}')

# Check raw-to-wiki mapping
print("\n=== Raw-to-Wiki Mapping ===")
wiki_sources_dir = 'wiki/sources'
raw_files = set()
wiki_files = set()

for fn in os.listdir('raw'):
    fp = os.path.join('raw', fn)
    if os.path.isfile(fp) and fn.endswith('.md') and fn != 'README.md':
        raw_files.add(fn)

for fn in os.listdir(wiki_sources_dir):
    fp = os.path.join(wiki_sources_dir, fn)
    if os.path.isfile(fp) and fn.endswith('.md') and fn != 'README.md':
        wiki_files.add(fn)

print(f'Raw source files: {len(raw_files)}')
print(f'Wiki source-note files: {len(wiki_files)}')

missing_in_wiki = raw_files - wiki_files
extra_in_wiki = wiki_files - raw_files

if missing_in_wiki:
    print(f'\nRaw files WITHOUT wiki source-note:')
    for f in sorted(missing_in_wiki):
        print(f'  MISSING: {f}')
if extra_in_wiki:
    print(f'\nWiki source-notes WITHOUT raw file:')
    for f in sorted(extra_in_wiki):
        print(f'  EXTRA: {f}')
if not missing_in_wiki and not extra_in_wiki:
    print('\nAll raw files have corresponding wiki source-notes. OK')
