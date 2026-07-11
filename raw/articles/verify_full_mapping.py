#!/usr/bin/env python3
"""Full raw-to-wiki mapping with recursive raw/ scan."""
import os

wiki_sources_dir = 'wiki/sources'
raw_files = set()
wiki_files = set()

for root, dirs, files in os.walk('raw'):
    for fn in files:
        fp = os.path.join(root, fn)
        if os.path.isfile(fp) and fn.endswith('.md') and fn != 'README.md':
            raw_files.add(fn)

for fn in os.listdir(wiki_sources_dir):
    fp = os.path.join(wiki_sources_dir, fn)
    if os.path.isfile(fp) and fn.endswith('.md') and fn != 'README.md':
        wiki_files.add(fn)

print(f'Raw source files: {len(raw_files)}')
for f in sorted(raw_files):
    print(f'  {f}')
print(f'\nWiki source-note files: {len(wiki_files)}')
for f in sorted(wiki_files):
    print(f'  {f}')

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
