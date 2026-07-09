#!/usr/bin/env python3
"""
Fix broken wikilinks after promote_fallback_to_base.py.
After promotion, files contain [[base_1]] links that should be [[base]].
"""
import re
import sys
from pathlib import Path

WIKI_DIR = Path("/workspace/llm-wiki/wiki")
DRY_RUN = "--apply" not in sys.argv

def get_existing_slugs():
    """Get all existing .md filenames (without .md) as a set."""
    slugs = set()
    for md_file in WIKI_DIR.rglob("*.md"):
        slugs.add(md_file.stem)
    return slugs

def fix_wikilinks(content, existing_slugs):
    """Replace [[slug_N]] -> [[slug]] when slug_N doesn't exist but slug does."""
    total_fixes = 0
    
    # Find all [[...]] wikilinks
    pattern = re.compile(r'\[\[([^\]]+)\]\]')
    
    def replacer(match):
        nonlocal total_fixes
        link = match.group(1)
        # Check if this is a suffixed link: slug_N
        parts = link.rsplit("_", 1)
        if len(parts) == 2 and parts[1].isdigit():
            base = parts[0]
            # If base exists in slugs, fix the link
            if base in existing_slugs:
                total_fixes += 1
                return f"[[{base}]]"
        return match.group(0)  # No change
    
    new_content = pattern.sub(replacer, content)
    return new_content, total_fixes

def main():
    existing_slugs = get_existing_slugs()
    print(f"Found {len(existing_slugs)} existing slugs.\n")
    
    total_fixes = 0
    files_modified = 0
    
    for md_file in WIKI_DIR.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8", errors="replace")
            new_content, fixes = fix_wikilinks(content, existing_slugs)
            if fixes > 0:
                total_fixes += fixes
                files_modified += 1
                if DRY_RUN:
                    print(f"[DRY-RUN] {md_file.relative_to(WIKI_DIR)}: {fixes} fixes")
                else:
                    md_file.write_text(new_content, encoding="utf-8")
                    print(f"[FIXED] {md_file.relative_to(WIKI_DIR)}: {fixes} fixes")
        except Exception as e:
            print(f"[ERROR] {md_file.relative_to(WIKI_DIR)}: {e}")
    
    print(f"\n{'[DRY-RUN] ' if DRY_RUN else ''}Total: {files_modified} files, {total_fixes} wikilink fixes")
    if not DRY_RUN:
        print(f"[COMPLETE] Fixed {total_fixes} broken wikilinks in {files_modified} files.")

if __name__ == "__main__":
    main()
