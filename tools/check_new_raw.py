#!/usr/bin/env python3
"""Check for new raw files not yet in wiki, and print report."""
import os, hashlib, re

def compute_correct_sha256(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    first_dash = content.index('---')
    rest = content[first_dash+3:]
    second_dash = rest.index('---')
    body = rest[second_dash+3:].strip()
    return hashlib.sha256(body.encode()).hexdigest()

wiki_sources_dir = 'wiki/sources'
raw_files = set()
wiki_files = set()

for root, dirs, files in os.walk('raw'):
    for fn in files:
        if fn.endswith('.md') and fn != 'README.md':
            raw_files.add(fn)

for fn in os.listdir(wiki_sources_dir):
    if fn.endswith('.md') and fn != 'README.md':
        wiki_files.add(fn)

new_raw = raw_files - wiki_files
hash_mismatches = []

for fn in sorted(raw_files):
    # find the file
    fp = None
    for root, dirs, files in os.walk('raw'):
        if fn in files:
            fp = os.path.join(root, fn)
            break
    if fp:
        computed = compute_correct_sha256(fp)
        with open(fp, 'r') as f:
            first_lines = f.read(300)
        m = re.search(r'sha256:\s*([a-f0-9]{64})', first_lines)
        stored = m.group(1) if m else 'NONE'
        if computed != stored:
            hash_mismatches.append(fn)

print(f"Total raw files: {len(raw_files)}")
print(f"Total wiki source-notes: {len(wiki_files)}")
print(f"New raw (not in wiki): {len(new_raw)}")
for f in sorted(new_raw):
    print(f"  NEW: {f}")
print(f"Hash mismatches: {len(hash_mismatches)}")
for f in sorted(hash_mismatches):
    print(f"  MISMATCH: {f}")
if not new_raw and not hash_mismatches:
    print("Status: ALL OK — no new files, all hashes correct.")
