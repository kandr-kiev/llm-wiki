#!/usr/bin/env python3
"""
Promote _1 (and _2, _3, _4) files to base versions when no base exists.
These groups have NO canonical page — the first _N is the best content available.
"""
import sys
from pathlib import Path

WIKI_DIR = Path("/workspace/llm-wiki/wiki")
DRY_RUN = "--apply" not in sys.argv

def get_base_name(filepath):
    stem = filepath.stem
    parts = stem.rsplit("_", 1)
    if len(parts) == 2 and parts[1].isdigit():
        return parts[0] + ".md"
    return None

def find_groups():
    groups = {}
    for md_file in WIKI_DIR.rglob("*.md"):
        base = get_base_name(md_file)
        if base:
            groups.setdefault(base, []).append(md_file)
    return groups

def main():
    groups = find_groups()
    
    to_promote = []
    for base_name, members in sorted(groups.items()):
        base_path = WIKI_DIR / base_name
        if not base_path.exists():
            # No base — promote the highest _N (first fallback = best content)
            members_sorted = sorted(members, key=lambda f: int(f.stem.rsplit("_", 1)[1]), reverse=True)
            to_promote.append((members_sorted[0], base_name))
    
    print(f"Found {len(to_promote)} groups to promote:\n")
    
    for src, base_name in to_promote:
        print(f"[{base_name}]")
        if DRY_RUN:
            print(f"  [DRY-RUN] {src.name} -> {base_name}")
        else:
            src.rename(WIKI_DIR / base_name)
            print(f"  [PROMOTED] {src.name} -> {base_name}")
    
    print(f"\n{'[DRY-RUN] ' if DRY_RUN else ''}Total: {len(to_promote)} files to promote")
    if not DRY_RUN:
        print(f"[COMPLETE] Promoted {len(to_promote)} fallback files to base versions.")

if __name__ == "__main__":
    main()
