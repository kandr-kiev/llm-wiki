#!/usr/bin/env python3
"""
graphify_bridge.py — Bridge між graphify-out/graph.json та wiki/

Алгоритм:
1. Завантажити graph.json → extract nodes + edges
2. Завантажити wiki/index.md → extract all wiki slugs
3. Fuzzy match: graph node labels ↔ wiki slugs
4. Для кожного match:
   - Додати wikilink [[slug]] до wiki сторінки якщо не існує
   - Додати graph node як "related_structure" у frontmatter
5. Знайти orphan graph nodes → запропонувати нові wiki сторінки
6. Report: {matched, orphan_nodes, new_links_added}

Usage:
  python3 tools/graphify_bridge.py [--dry-run] [--auto-fix]
"""

import json
import os
import re
import sys
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher

# === Configuration ===
PROJECT_ROOT = Path(__file__).resolve().parent.parent
GRAPH_JSON = PROJECT_ROOT / "graphify-out" / "graph.json"
WIKI_DIR = PROJECT_ROOT / "wiki"
WIKI_INDEX = WIKI_DIR / "index.md"
SLUGS_FILE = PROJECT_ROOT / "wiki" / ".slug_cache.json"

# Fuzzy match threshold (0.0-1.0)
FUZZY_THRESHOLD = 0.65


# === Helpers ===

def fuzzy_match(a: str, b: str) -> float:
    """Calculate similarity between two strings."""
    a_norm = a.lower().strip().replace("-", " ").replace("_", " ")
    b_norm = b.lower().strip().replace("-", " ").replace("_", " ")
    return SequenceMatcher(None, a_norm, b_norm).ratio()


def extract_slugs_from_index(index_content: str) -> dict:
    """Extract all wiki slugs from index.md.
    Returns: {slug: title}
    
    Format: ### [title](wiki/path/to/file.md)
    Also handles: - [[slug]] — Title
    """
    slugs = {}
    
    # Pattern: ### [title](wiki/path/to/file.md)
    for match in re.finditer(r"###\s+\[([^\]]+)\]\s*\(\s*wiki/([^\)]+)\s*\)", index_content):
        title = match.group(1).strip()
        path = match.group(2).strip()
        # Extract slug from path: wiki/comparisons/slug.md → slug
        slug = Path(path).stem
        slugs[slug] = title
    
    # Pattern: - [[slug]] — Title (legacy format)
    for match in re.finditer(r"-\s+\[\[([^\]]+)\]\]\s*[—-]\s*(.+)", index_content):
        slug = match.group(1).strip()
        title = match.group(2).strip()
        if slug not in slugs:
            slugs[slug] = title
    
    # Pattern: [[slug]] (bare wikilinks)
    for match in re.finditer(r"\[\[([^\]]+)\]\]", index_content):
        slug = match.group(1).strip()
        if slug not in slugs:
            slugs[slug] = slug
    
    return slugs


def extract_slugs_from_files(wiki_dir: Path) -> dict:
    """Extract slugs from all wiki .md files frontmatter."""
    slugs = {}
    for md_file in wiki_dir.rglob("*.md"):
        if md_file.name == "index.md":
            continue
        try:
            content = md_file.read_text(encoding="utf-8")
            # Read frontmatter slug
            slug_match = re.search(r"^---\s*\n.*?^slug:\s*(.+?)\s*\n---", content, re.DOTALL)
            if slug_match:
                slug = slug_match.group(1).strip()
                slugs[slug] = slug
        except Exception:
            pass
    return slugs


def load_graph() -> dict:
    """Load graph.json and return parsed graph."""
    if not GRAPH_JSON.exists():
        print(f"ERROR: {GRAPH_JSON} not found. Run: graphify .")
        sys.exit(1)
    with open(GRAPH_JSON) as f:
        return json.load(f)


def load_slugs() -> dict:
    """Load wiki slugs from index.md and files."""
    slugs = {}
    if WIKI_INDEX.exists():
        slugs.update(extract_slugs_from_index(WIKI_INDEX.read_text(encoding="utf-8")))
    slugs.update(extract_slugs_from_files(WIKI_DIR))
    return slugs


def match_graph_to_slugs(graph: dict, slugs: dict) -> list:
    """Fuzzy match graph nodes to wiki slugs.
    Returns: [{graph_node, matched_slug, score, type}]
    """
    matches = []
    matched_slugs = set()

    for node in graph.get("nodes", []):
        label = node.get("label", "")
        node_type = node.get("file_type", "unknown")
        source_file = node.get("source_file", "")

        # Skip non-content nodes (config, cache, etc.)
        if source_file and any(skip in source_file for skip in [
            ".obsidian/", "node_modules/", ".git/", "cache/",
            "graphify-out/", "tools/", "utils.py", "requirements"
        ]):
            continue

        # Find best match
        best_slug = None
        best_score = 0.0

        for slug in slugs:
            score = fuzzy_match(label, slug)
            # Boost for exact substring match
            if slug.lower() in label.lower() or label.lower() in slug.lower():
                score = max(score, 0.85)
            # Boost for type match
            if node_type == slug.split("-")[0].lower() if "-" in slug else False:
                score = min(score + 0.1, 1.0)

            if score > best_score and score >= FUZZY_THRESHOLD:
                best_score = score
                best_slug = slug

        if best_slug:
            matches.append({
                "graph_node": node,
                "matched_slug": best_slug,
                "score": round(best_score, 3),
                "type": node_type,
            })
            matched_slugs.add(best_slug)

    return matches


def detect_orphan_nodes(graph: dict, matched_slugs: set) -> list:
    """Find graph nodes with no matching wiki slug."""
    orphans = []
    for node in graph.get("nodes", []):
        label = node.get("label", "")
        source_file = node.get("source_file", "")

        # Skip non-content nodes
        if source_file and any(skip in source_file for skip in [
            ".obsidian/", "node_modules/", ".git/", "cache/",
            "graphify-out/", "tools/", "utils.py", "requirements"
        ]):
            continue

        if label not in matched_slugs:
            orphans.append(node)

    return orphans


def add_wikilinks_to_wiki(matches: list, dry_run: bool = True) -> int:
    """Add [[wikilink]] references to wiki pages based on graph matches.
    Returns: count of new links added.
    """
    new_links = 0

    for match in matches:
        slug = match["matched_slug"]
        graph_node = match["graph_node"]

        # Build wiki path
        wiki_path = WIKI_DIR / f"{slug}.md"
        if not wiki_path.exists():
            continue

        try:
            content = wiki_path.read_text(encoding="utf-8")
            slug = match["matched_slug"]

            # Check if wikilink already exists (both slug and graph_label)
            graph_label = graph_node.get("label", "")
            if f"[[{slug}]]" in content or f"[[{graph_label}]]" in content:
                continue

            # Add to "See also" section or at end
            see_also_match = re.search(r"\n##\s*See\s*also", content, re.IGNORECASE)
            if see_also_match:
                insert_pos = see_also_match.end()
                new_content = content[:insert_pos] + f"\n- [[{slug}]]\n" + content[insert_pos:]
            else:
                new_content = content.rstrip() + f"\n\nSee also: [[{slug}]]\n"

            if not dry_run:
                wiki_path.write_text(new_content, encoding="utf-8")
            new_links += 1

        except Exception as e:
            print(f"  WARNING: Could not update {wiki_path}: {e}")

    return new_links


def generate_report(matches: list, orphans: list, new_links: int) -> dict:
    """Generate bridge report."""
    report = {
        "total_graph_nodes": len(matches) + len(orphans),
        "matched_nodes": len(matches),
        "orphan_nodes": len(orphans),
        "match_rate": round(len(matches) / max(len(matches) + len(orphans), 1) * 100, 1),
        "new_links_added": new_links,
        "matched_pairs": [
            {"graph_label": m["graph_node"]["label"], "wiki_slug": m["matched_slug"], "score": m["score"]}
            for m in sorted(matches, key=lambda x: x["score"], reverse=True)[:20]
        ],
        "orphan_suggestions": [
            {"label": o.get("label", ""), "type": o.get("file_type", "")}
            for o in orphans[:20]
        ],
    }
    return report


def main():
    dry_run = "--dry-run" in sys.argv
    auto_fix = "--auto-fix" in sys.argv

    print("=" * 60)
    print("GRAPHIFY BRIDGE — graph.json ↔ wiki/ cross-references")
    print("=" * 60)

    # 1. Load graph
    print("\n[1/5] Loading graph.json...")
    graph = load_graph()
    print(f"  Nodes: {len(graph.get('nodes', []))}")
    print(f"  Edges: {len(graph.get('edges', []))}")

    # 2. Load wiki slugs
    print("\n[2/5] Loading wiki slugs...")
    slugs = load_slugs()
    print(f"  Wiki slugs: {len(slugs)}")

    # 3. Fuzzy match
    print("\n[3/5] Fuzzy matching graph nodes to wiki slugs...")
    matches = match_graph_to_slugs(graph, slugs)
    print(f"  Matches: {len(matches)}")

    # 4. Detect orphans
    print("\n[4/5] Detecting orphan graph nodes...")
    matched_slugs = {m["matched_slug"] for m in matches}
    orphans = detect_orphan_nodes(graph, matched_slugs)
    print(f"  Orphans: {len(orphans)}")

    # 5. Add wikilinks
    print("\n[5/5] Adding wikilinks to wiki pages...")
    new_links = add_wikilinks_to_wiki(matches, dry_run=dry_run)
    print(f"  New links: {new_links} ({'DRY RUN' if dry_run else 'APPLIED'})")

    # Report
    report = generate_report(matches, orphans, new_links)
    print("\n" + "=" * 60)
    print("BRIDGE REPORT")
    print("=" * 60)
    print(f"  Graph nodes: {report['total_graph_nodes']}")
    print(f"  Matched:     {report['matched_nodes']} ({report['match_rate']}%)")
    print(f"  Orphans:     {report['orphan_nodes']}")
    print(f"  New links:   {report['new_links_added']}")

    if report["matched_pairs"]:
        print("\nTop matches:")
        for m in report["matched_pairs"][:10]:
            print(f"  {m['graph_label']:40s} → [[{m['wiki_slug']}]]) ({m['score']})")

    if report["orphan_suggestions"]:
        print(f"\nOrphan suggestions (top {min(10, len(orphans))}):")
        for o in report["orphan_suggestions"][:10]:
            print(f"  {o['label']:40s} ({o['type']})")

    if dry_run:
        print("\n⚠️  Dry run — use --auto-fix to apply changes")
    else:
        print("\n✅ Changes applied")

    # Save report
    report_path = PROJECT_ROOT / "graphify-out" / "bridge_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"  Report saved to: {report_path}")

    return report


if __name__ == "__main__":
    main()
