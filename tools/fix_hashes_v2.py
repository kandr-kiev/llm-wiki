#!/usr/bin/env python3
"""Fix SHA256 hashes in raw source files — v2 with proper frontmatter parsing."""
import hashlib
import os
import re

def compute_correct_sha256(filepath):
    """Compute SHA256 of body: everything after the first complete raw frontmatter block.
    
    Raw frontmatter is always at the very beginning of the file:
    ---
    source_url: ...
    ingested: ...
    sha256: ...
    ---
    
    Body = everything after the closing --- of this first block.
    Handles files with embedded second frontmatter and markdown tables containing ---.
    """
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Match the first frontmatter block at the start of the file
    # Pattern: line starting with '---', then YAML content, then '---' on its own line
    fm_pattern = r'^---\s*\n(.*?)^---\s*\n?'
    m = re.match(fm_pattern, content, re.DOTALL | re.MULTILINE)
    
    if m:
        # Body is everything after the first frontmatter closing ---
        body = content[m.end():].strip()
    else:
        # No frontmatter found — whole file is body
        body = content.strip()
    
    return hashlib.sha256(body.encode()).hexdigest(), body[:80]

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
        
        new_hash, preview = compute_correct_sha256(fp)
        
        # Replace the sha256 line in the FIRST frontmatter block only
        fm_pattern = r'^(---\s*\n.*?sha256:\s*)[a-f0-9]{64}'
        new_content = re.sub(fm_pattern, r'\g<1>' + new_hash, content, count=1, flags=re.MULTILINE)
        
        if new_content != content:
            with open(fp, 'w') as f:
                f.write(new_content)
            print(f'UPDATED: {os.path.relpath(fp, wiki_root)}')
            print(f'  hash: {new_hash}')
            print(f'  body preview: {repr(preview)}')
            print(f'  body len: {len(new_hash)}')
        else:
            print(f'NO CHANGE: {os.path.relpath(fp, wiki_root)}')

print('\nDone.')
