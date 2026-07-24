#!/usr/bin/env python3
"""
Migrate wiki pages from title-based wikilinks to slug-based wikilinks.

Before: [[Page Title]] → broken (file is page-title.md)
After:  [[page-title]] → valid (matches page-title.md)

Usage:
    python3 tools/fix_wikilinks.py [--dry-run] [--limit N]

This script:
1. Builds a complete slug->title map from ALL wiki pages
2. Scans every wiki page for [[Title]] patterns
3. Replaces them with [[slug]] where slug exists
4. Only modifies title-based wikilinks (not already-slug-based ones)
"""

import re
import sys
from pathlib import Path
from typing import Dict, Tuple

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"


def build_title_to_slug_map() -> Dict[str, str]:
    """Build title -> slug mapping from all wiki pages.
    
    Returns: {normalized_title: slug}
    E.g. {"5 agent skills i use every day": "5-agent-skills-i-use-every-day"}
    """
    map = {}
    for subdir in WIKI_DIR.glob("*"):
        if not subdir.is_dir():
            continue
        for f in subdir.glob("*.md"):
            if f.name == "README.md":
                continue
            try:
                content = f.read_text(encoding="utf-8", errors="ignore")
                # Extract H1 title
                h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                if h1_match:
                    title = h1_match.group(1).strip()
                    # Normalize: lowercase, hyphens instead of spaces
                    slug = f.stem.lower()
                    # Skip empty/invalid slugs
                    if not slug or slug == "readme":
                        continue
                    normalized = re.sub(r"\s+", " ", title.lower()).strip()
                    # Skip empty titles
                    if not normalized:
                        continue
                    map[normalized] = slug
                    # Also add with hyphens (some titles get hyphenated)
                    hyphenated = re.sub(r"\s+", "-", title.lower()).strip()
                    if hyphenated != normalized:
                        map[hyphenated] = slug
            except Exception:
                continue
    return map


def fix_wikilinks_in_content(content: str, title_to_slug: Dict[str, str]) -> Tuple[str, int]:
    """Replace title-based wikilinks with slug-based ones.
    
    Returns: (fixed_content, replacements_made)
    """
    replacements = 0
    fixed = content
    
    # Find all [[wikilinks]]
    # Pattern: [[text]] where text is NOT already slug-like (contains spaces or uppercase)
    # Slug-like: all lowercase, hyphens instead of spaces
    def replacer(match):
        nonlocal replacements
        inner = match.group(1)
        
        # Skip if already slug-like (no spaces, all lowercase)
        if " " not in inner and inner == inner.lower():
            return match.group(0)
        
        # Skip special patterns: [[#tag]], [[Category:]], etc.
        if inner.startswith("#") or ":" in inner:
            return match.group(0)
        
        # Try to find matching slug
        normalized = re.sub(r"\s+", " ", inner.lower()).strip()
        
        # Also try with hyphens
        hyphenated = re.sub(r"\s+", "-", inner.lower()).strip()
        
        slug = title_to_slug.get(normalized) or title_to_slug.get(hyphenated)
        
        if slug:
            replacements += 1
            return f"[[{slug}]]"
        
        return match.group(0)  # No match, leave as-is
    
    fixed = re.sub(r"\[\[([^\]]+?)\]\]", replacer, fixed)
    return fixed, replacements


def main():
    dry_run = "--dry-run" in sys.argv
    limit = None
    if "--limit" in sys.argv:
        idx = sys.argv.index("--limit")
        if idx + 1 < len(sys.argv):
            limit = int(sys.argv[idx + 1])
    
    print("=" * 60)
    print("Wiki Wikilink Migrator")
    print("Converting title-based links to slug-based links")
    print("=" * 60)
    
    # Build map
    print("\nBuilding title->slug map...")
    title_to_slug = build_title_to_slug_map()
    print(f"  Mapped {len(title_to_slug)} titles to slugs")
    
    # Scan pages
    print("\nScanning wiki pages...")
    pages = list(WIKI_DIR.glob("*/*.md"))
    if limit:
        pages = pages[:limit]
    
    total_replacements = 0
    modified_pages = 0
    skipped_pages = 0
    
    for page in pages:
        try:
            content = page.read_text(encoding="utf-8", errors="ignore")
            fixed, count = fix_wikilinks_in_content(content, title_to_slug)
            
            if count > 0:
                total_replacements += count
                modified_pages += 1
                
                if dry_run:
                    print(f"  [DRY-RUN] {page.relative_to(WIKI_DIR)}: {count} replacements")
                else:
                    page.write_text(fixed, encoding="utf-8")
                    print(f"  [FIXED] {page.relative_to(WIKI_DIR)}: {count} replacements")
            else:
                skipped_pages += 1
        except Exception as e:
            print(f"  [ERROR] {page.relative_to(WIKI_DIR)}: {e}")
    
    print("\n" + "=" * 60)
    print("RESULTS:")
    print(f"  Total pages scanned: {len(pages)}")
    print(f"  Modified: {modified_pages}")
    print(f"  Skipped (no changes): {skipped_pages}")
    print(f"  Total replacements: {total_replacements}")
    print(f"  Mode: {'DRY-RUN' if dry_run else 'LIVE'}")
    print("=" * 60)
    
    return modified_pages, total_replacements


if __name__ == "__main__":
    main()
