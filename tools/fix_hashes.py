#!/usr/bin/env python3
"""Fix SHA256 hashes in raw source files."""
import hashlib
import os
import re

def compute_correct_sha256(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    first_dash = content.index('---')
    rest = content[first_dash+3:]
    second_dash = rest.index('---')
    body = rest[second_dash+3:].strip()
    return hashlib.sha256(body.encode()).hexdigest()

wiki_root = '/workspace/llm-wiki'
for root, dirs, files in os.walk(os.path.join(wiki_root, 'raw')):
    for fn in sorted(files):
        if fn == 'README.md':
            continue
        fp = os.path.join(root, fn)
        if not fp.endswith('.md'):
            continue
        
        with open(fp, 'r') as f:
            content = f.read()
        
        new_hash = compute_correct_sha256(fp)
        
        new_content = re.sub(
            r'(sha256:\s*)[a-f0-9]{64}',
            r'\g<1>' + new_hash,
            content
        )
        
        if new_content != content:
            with open(fp, 'w') as f:
                f.write(new_content)
            print(f'UPDATED: {fp} -> {new_hash}')
        else:
            print(f'NO CHANGE: {fp}')

print('\nDone.')
