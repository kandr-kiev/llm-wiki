#!/usr/bin/env python3
"""Final step: append missing tags to SCHEMA.md."""
import json
import re
from pathlib import Path

SCHEMA_PATH = Path('/workspace/llm-wiki/SCHEMA.md')

BT = chr(96)  # backtick

# Read schema
content = SCHEMA_PATH.read_text(encoding='utf-8')
lines = content.split('\n')
taxonomy_lines = []
in_taxonomy = False
for line in lines:
    if line.startswith('## Tag Taxonomy'):
        in_taxonomy = True
        continue
    if in_taxonomy:
        if line.startswith('## '):
            break
        taxonomy_lines.append(line)

# Find last table row
last_idx = None
for i in range(len(taxonomy_lines)-1, -1, -1):
    line = taxonomy_lines[i]
    if line.startswith('|') and BT in line and not line.startswith('|---'):
        last_idx = i
        break

prefix = '\n'.join(taxonomy_lines[:last_idx + 1])
insert_pos = content.find(prefix) + len(prefix)

# Missing tags from utils.py
missing = ['api', 'dataset', 'interoperability', 'knowledge-storage',
           'monitoring', 'review', 'setup', 'software', 'standards',
           'streaming', 'tensorflow', 'tool', 'tutorial', 'video-generation']

# Build new rows
new_rows = []
for i in range(0, len(missing), 4):
    row_tags = missing[i:i+4]
    cells = ' | '.join(BT + t + BT for t in row_tags)
    while len(row_tags) < 4:
        cells += ' | '
    new_rows.append('| ' + cells + ' |')

new_section = '\n' + '\n'.join(new_rows) + '\n'
out = content[:insert_pos] + new_section + content[insert_pos:]
SCHEMA_PATH.write_text(out, encoding='utf-8')
print(f'SCHEMA.md updated: {len(out)} bytes, +{len(missing)} tags', flush=True)

# Verify
content2 = SCHEMA_PATH.read_text(encoding='utf-8')
lines2 = content2.split('\n')
tax2 = []
in2 = False
for line in lines2:
    if line.startswith('## Tag Taxonomy'):
        in2 = True
        continue
    if in2:
        if line.startswith('## '):
            break
        tax2.append(line)

_SKIP = {'type','title','description','tags','timestamp','resource',
         'category','confidence','contested','links','sources','status',
         'from taxonomy below','Тег','Tag'}
schema_tags2 = set()
for line in tax2:
    for m in re.finditer(BT + r'([^' + BT + r']+)' + BT, line):
        tag = m.group(1).strip()
        if tag not in _SKIP and tag:
            schema_tags2.add(tag)

# Read approved_tags.json
approved_path = Path('/workspace/llm-wiki/tools/approved_tags.json')
utils_tags = set(json.loads(approved_path.read_text(encoding='utf-8')))

print(f'Schema tags: {len(schema_tags2)}', flush=True)
print(f'Utils tags: {len(utils_tags)}', flush=True)
print(f'Match: {schema_tags2 == utils_tags}', flush=True)
if schema_tags2 != utils_tags:
    print(f'Only in schema: {sorted(schema_tags2 - utils_tags)}', flush=True)
    print(f'Only in utils: {sorted(utils_tags - schema_tags2)}', flush=True)
print('DONE', flush=True)
