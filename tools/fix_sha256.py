#!/usr/bin/env python3
"""Fix SHA256 drift in raw files — recompute body hash using split_frontmatter logic."""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw" / "articles"

def split_frontmatter(text):
    """Same logic as wiki_lint.py — find '\\n---\\n' boundary."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end+5:]

def compute_sha256(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def fix_file(filepath):
    """Recompute sha256 for a single file."""
    content = filepath.read_text(encoding='utf-8')
    fm, body = split_frontmatter(content)
    if fm is None:
        return False  # no frontmatter
    
    new_sha = compute_sha256(body)
    
    # Find PLACEHOLDER or existing sha256 in frontmatter
    sha_line = None
    for line in fm.split('\n'):
        if line.startswith('sha256:'):
            sha_line = line
            break
    
    if sha_line is None:
        # No sha256 in frontmatter — add it
        new_fm = fm + f'\nsha256: {new_sha}'
        new_content = '---\n' + new_fm + '\n---\n' + body
        print(f"  ADDED: {filepath.name} ({new_sha[:12]}...)")
        return True
    else:
        # Replace existing sha256 line
        old_sha = sha_line.split(':', 1)[1].strip()
        if old_sha == new_sha:
            return False  # no change needed
        new_fm = fm.replace(sha_line, f'sha256: {new_sha}')
        new_content = '---\n' + new_fm + '\n---\n' + body
        print(f"  FIXED: {filepath.name} ({old_sha[:12]}... → {new_sha[:12]}...)")
    
    filepath.write_text(new_content, encoding='utf-8')
    return True

if __name__ == '__main__':
    files = sorted(RAW_DIR.glob('*.md'))
    print(f"Scanning {len(files)} files in {RAW_DIR}")
    
    fixed = 0
    for f in files:
        if fix_file(f):
            fixed += 1
    
    print(f"\nTotal: {len(files)}, Fixed: {fixed}")