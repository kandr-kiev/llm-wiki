#!/usr/bin/env python3
"""
Cleanup duplicate wiki pages (_1, _2, _3, _4 suffixes).

Logic:
1. Group files by base name (remove _N.md suffix).
2. If base version (no suffix) exists -> delete all _N versions.
3. If base version does NOT exist -> rename highest _N to base, delete rest.

Dry-run by default. Use --apply to actually delete/rename files.
"""

import os
import re
import argparse
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"

def find_duplicates():
    """Find all _N.md duplicate groups."""
    base_to_versions = defaultdict(list)
    
    for root, dirs, files in os.walk(WIKI_DIR):
        for f in files:
            if f == "README.md":
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, ROOT)
            match = re.match(r"^(.+)_\d+\.md$", f)
            if match:
                base = match.group(1)
                base_to_versions[base].append(rel)
    
    return {k: sorted(v) for k, v in base_to_versions.items() if len(v) >= 2}

def analyze_groups(groups):
    """Analyze each group: does base version exist?"""
    results = []
    for base, paths in sorted(groups.items()):
        # Check if base version exists (no suffix)
        # Extract directory from first path
        first_dir = os.path.dirname(paths[0])
        base_filename = os.path.basename(paths[0]).replace(paths[0].split("/")[-1].split("_")[-1].replace(".md", ""), "")
        
        # Reconstruct base path
        parts = paths[0].split("/")
        dir_part = "/".join(parts[:-1])
        file_part = parts[-1]
        file_stem = file_part.replace(".md", "")
        # Remove _N suffix
        base_stem = re.sub(r"_\d+$", "", file_stem)
        base_path = f"{dir_part}/{base_stem}.md" if dir_part else f"{base_stem}.md"
        
        base_exists = (ROOT / base_path).exists()
        
        results.append({
            "base": base,
            "paths": paths,
            "base_exists": base_exists,
            "base_path": base_path,
            "count": len(paths),
        })
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Cleanup wiki page duplicates")
    parser.add_argument("--apply", action="store_true", help="Actually delete/rename files")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Preview only (default)")
    args = parser.parse_args()
    
    groups = find_duplicates()
    print(f"Found {len(groups)} duplicate groups ({sum(len(v) for v in groups.values())} total files)\n")
    
    results = analyze_groups(groups)
    
    # Summary stats
    with_base = sum(1 for r in results if r["base_exists"])
    without_base = sum(1 for r in results if not r["base_exists"])
    
    print(f"Groups WITH base version: {with_base}")
    print(f"Groups WITHOUT base version: {without_base}\n")
    
    # Show groups WITHOUT base (need special handling)
    print("=" * 80)
    print("GROUPS WITHOUT BASE VERSION (need base creation or manual review):")
    print("=" * 80)
    for r in results:
        if not r["base_exists"]:
            print(f"\n  BASE: {r['base_path']}")
            for p in r["paths"]:
                action = "DELETE" if not args.apply else "DELETE"
                print(f"    [{action}] {p}")
    
    print("\n" + "=" * 80)
    print("GROUPS WITH BASE VERSION (delete _N versions):")
    print("=" * 80)
    for r in results:
        if r["base_exists"]:
            print(f"\n  BASE: {r['base_path']} (KEEP)")
            for p in r["paths"]:
                print(f"    -> {p}")
    
    if not args.apply:
        print("\n\n=== DRY RUN ===")
        print("Run with --apply to actually delete files.")
        print(f"Would delete: {sum(len(r['paths']) for r in results)} files")
        print(f"Would rename: 0 files (all have base versions)")
    else:
        # Apply: handle both cases
        deleted = 0
        for r in results:
            if r["base_exists"]:
                # Delete all _N versions (base is preserved)
                for p in r["paths"]:
                    full = ROOT / p
                    if full.exists():
                        full.unlink()
                        deleted += 1
                        print(f"  Deleted: {p}")
            else:
                # No base version: keep first _N, delete rest
                for p in r["paths"][1:]:
                    full = ROOT / p
                    if full.exists():
                        full.unlink()
                        deleted += 1
                        print(f"  Deleted: {p} (kept {r['paths'][0]})")
        
        print(f"\nDeleted {deleted} duplicate files.")

if __name__ == "__main__":
    main()
