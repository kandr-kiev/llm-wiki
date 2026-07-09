#!/usr/bin/env python3
"""Fix SHA256 hashes in raw source files — v3 with line-by-line parsing."""
import hashlib
import os
import re

def compute_correct_sha256(filepath):
    """Compute SHA256 of body: everything after the first raw frontmatter block.
    
    The raw frontmatter is always the FIRST block at the very start of the file:
    ---
    source_url: ...
    ingested: YYYY-MM-DD
    sha256: <hex>
    ---
    
    Body = everything after the second '---' line (closing of first frontmatter).
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Find first --- (opening of frontmatter)
    first_dash_line = None
    second_dash_line = None
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == '---':
            if first_dash_line is None:
                first_dash_line = i
            elif second_dash_line is None:
                second_dash_line = i
                break
    
    if second_dash_line is not None:
        # Body starts after the second --- line
        body_lines = lines[second_dash_line + 1:]
    else:
        # No frontmatter found
        body_lines = lines
    
    body = ''.join(body_lines).strip()
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
        
        # Replace the sha256 line in the first frontmatter block only
        # Use line-by-line replacement to be precise
        lines = content.split('\n')
        first_dash = None
        second_dash = None
        for i, line in enumerate(lines):
            if line.strip() == '---':
                if first_dash is None:
                    first_dash = i
                elif second_dash is None:
                    second_dash = i
                    break
        
        if second_dash is not None:
            # Find sha256 line between first and second dash
            sha_line = None
            for i in range(first_dash, second_dash + 1):
                if 'sha256:' in lines[i]:
                    sha_line = i
                    break
            
            if sha_line is not None:
                old_line = lines[sha_line]
                new_line = re.sub(
                    r'(sha256:\s*)[a-f0-9]{64}',
                    r'\g<1>' + new_hash,
                    old_line
                )
                lines[sha_line] = new_line
                new_content = '\n'.join(lines)
                
                if new_content != content:
                    with open(fp, 'w') as f:
                        f.write(new_content)
                    print(f'UPDATED: {os.path.relpath(fp, wiki_root)}')
                    print(f'  hash: {new_hash}')
                    print(f'  body preview: {repr(preview)}')
                    print(f'  body len: {len(body)}')
                else:
                    print(f'NO CHANGE: {os.path.relpath(fp, wiki_root)}')
            else:
                print(f'NO SHA256 LINE: {os.path.relpath(fp, wiki_root)}')
        else:
            print(f'NO FRONTMATTER: {os.path.relpath(fp, wiki_root)}')

print('\nDone.')
