#!/usr/bin/env python3
"""
graphify_bridge.py — Bridge між graph-from-wiki.json та wiki/

Алгоритм:
1. Завантажити graph-from-wiki.json → extract nodes + edges (wikilinks)
2. Завантажити wiki/index.md → extract all wiki slugs
3. Verify: graph edges match actual [[wikilinks]] in wiki files
4. For each node:
   - Check if file contains backlinks section
   - Add [[wikilink]] for each graph edge target
   - Add Dataview query for backlinks
5. Find orphan nodes → confirm if artifacts
6. Report: {matched, orphans, missing_links, dataview_added}

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
# Use graph-from-wiki.json (wiki content) instead of graph.json (code AST)
GRAPH_JSON = PROJECT_ROOT.parent / "graphify-out" / "graph-from-wiki.json"
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
    """
    slugs = {}
    
    # Pattern: ### [title](wiki/path/to/file.md)
    for match in re.finditer(r"###\s+\[([^\]]+)\]\s*\(\s*wiki/([^\)]+)\s*\)", index_content):
        title = match.group(1).strip()
        path = match.group(2).strip()
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
            slug_match = re.search(r"^---\s*\n.*?^slug:\s*(.+?)\s*\n---", content, re.DOTALL)
            if slug_match:
                slug = slug_match.group(1).strip()
                slugs[slug] = slug
        except Exception:
            pass
    return slugs


def load_graph() -> dict:
    """Load graph-from-wiki.json and return parsed graph."""
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


def extract_wikilinks_from_file(wiki_path: Path) -> set:
    """Extract all [[wikilink]] references from a wiki file.
    Returns: set of slug strings
    """
    if not wiki_path.exists():
        return set()
    
    try:
        content = wiki_path.read_text(encoding="utf-8")
        links = set()
        
        # Pattern: [[slug]] or [[slug|alias]]
        for match in re.finditer(r"\[\[([^\]|]+?)(?:\|([^\]]+))?\]\]", content):
            slug = match.group(1).strip()
            links.add(slug)
        
        return links
    except Exception:
        return set()


def verify_graph_edges_against_wikilinks(graph: dict, wiki_slugs: dict) -> dict:
    """Verify graph edges match actual [[wikilinks]] in wiki files.
    Returns: {verified, mismatched, missing_files}
    """
    # Build wiki content cache - search all subdirs
    wiki_content = {}
    for root, dirs, files in os.walk(WIKI_DIR):
        for f in files:
            if f.endswith('.md'):
                slug = os.path.splitext(f)[0]
                path = os.path.join(root, f)
                wiki_content[slug] = {
                    'path': path,
                    'content': open(path).read()
                }
    
    # Pre-index edges by source node (O(edges) instead of O(nodes × edges))
    edges_by_source = defaultdict(set)
    for edge in graph.get("edges", []):
        src = edge.get("source", "")
        tgt = edge.get("target", "")
        edges_by_source[src].add(tgt)
    
    verified = 0
    mismatched = 0
    missing_files = 0
    
    for node in graph.get("nodes", []):
        node_id = node.get("id", "")
        
        # Find file by slug (may be in subdirs)
        if node_id not in wiki_content:
            missing_files += 1
            continue
        
        file_data = wiki_content[node_id]
        file_links = extract_wikilinks_from_file(Path(file_data['path']))
        
        # Get graph targets from pre-indexed dict (O(1) instead of O(edges))
        graph_targets = edges_by_source.get(node_id, set())
        
        # Verify: graph targets should be in file links
        if graph_targets and file_links:
            matched = graph_targets & file_links
            if len(matched) >= len(graph_targets) * 0.8:  # 80% threshold
                verified += 1
            else:
                mismatched += 1
    
    return {
        "verified": verified,
        "mismatched": mismatched,
        "missing_files": missing_files,
        "total_nodes": len(graph.get("nodes", []))
    }


def find_wiki_file(slug: str) -> str | None:
    """Find wiki file by slug, searching all subdirectories.
    Returns: absolute path or None.
    """
    for root, dirs, files in os.walk(WIKI_DIR):
        if slug + '.md' in files:
            return os.path.join(root, slug + '.md')
    return None


def add_backlinks_to_file(wiki_path: str, graph_node_id: str, graph_node_label: str, dry_run: bool = True) -> bool:
    """Add backlink to frontmatter if not exists.
    Returns: True if added, False if already exists or error.
    """
    if not os.path.exists(wiki_path):
        return False
    
    try:
        content = open(wiki_path, 'r', encoding='utf-8').read()
        
        # Check if backlink already exists in frontmatter
        if f"backlinks:\n" in content and graph_node_id in content[:500]:
            return False  # Already has backlink
        
        # Find frontmatter end
        fm_end = content.find("---", 3)
        if fm_end < 0:
            return False  # No frontmatter
        
        # Extract frontmatter
        frontmatter = content[:fm_end + 3]
        body = content[fm_end + 3:]
        
        # Add backlinks section if not exists
        if "backlinks:" not in frontmatter:
            new_frontmatter = frontmatter.rstrip() + "\nbacklinks:\n  - " + graph_node_id + "\n---\n"
            new_content = new_frontmatter + body
        else:
            # Append to existing backlinks
            bm = re.search(r"(backlinks:\s*\n)(.*)", frontmatter, re.DOTALL)
            if bm:
                existing = bm.group(2).strip()
                if graph_node_id not in existing:
                    new_backlinks = existing + "\n  - " + graph_node_id
                    new_frontmatter = frontmatter.replace(bm.group(0), bm.group(1) + new_backlinks)
                    new_content = new_frontmatter + body
                else:
                    return False  # Already exists
            else:
                return False  # Can't parse backlinks
        
        if not dry_run:
            with open(wiki_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
        return True
        
    except Exception as e:
        print(f"  WARNING: Could not update backlinks in {wiki_path}: {e}")
        return False


def add_dataview_query(wiki_path: str, graph_node_id: str, graph_node_label: str, dry_run: bool = True) -> bool:
    """Add Dataview query for backlinks if not exists.
    Returns: True if added, False if already exists or error.
    """
    if not os.path.exists(wiki_path):
        return False
    
    try:
        content = open(wiki_path, 'r', encoding='utf-8').read()
        
        # Check if Dataview query already exists
        if "dataview" in content.lower() and "backlinks" in content.lower():
            return False  # Already has Dataview query
        
        # Add Dataview query at end of file
        dataview_query = f"""
## Backlinks

```dataview
LIST FROM ""
WHERE contains(backlinks, "{graph_node_id}")
```
"""
        if not dry_run:
            with open(wiki_path, 'w', encoding='utf-8') as f:
                f.write(content.rstrip() + dataview_query)
        return True
        
    except Exception as e:
        print(f"  WARNING: Could not add Dataview query to {wiki_path}: {e}")
        return False


def match_graph_to_slugs(graph: dict, slugs: dict) -> list:
    """Fuzzy match graph nodes to wiki slugs.
    Returns: [{graph_node, matched_slug, score, type}]
    """
    matches = []
    matched_slugs = set()

    for node in graph.get("nodes", []):
        label = node.get("label", "")
        node_type = node.get("type", "unknown")
        node_id = node.get("id", "")

        # Skip non-content nodes (config, cache, etc.)
        if any(skip in node_id for skip in [
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
        node_id = node.get("id", "")

        # Skip non-content nodes
        if any(skip in node_id for skip in [
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


def generate_report(matches: list, orphans: list, new_links: int, missing_links: int, dataview_added: int, edge_verification: dict) -> dict:
    """Generate bridge report."""
    report = {
        "total_graph_nodes": len(matches) + len(orphans),
        "matched_nodes": len(matches),
        "orphan_nodes": len(orphans),
        "match_rate": round(len(matches) / max(len(matches) + len(orphans), 1) * 100, 1),
        "new_links_added": new_links,
        "missing_links": missing_links,
        "dataview_added": dataview_added,
        "edge_verification": edge_verification,
        "matched_pairs": [
            {"graph_label": m["graph_node"]["label"], "wiki_slug": m["matched_slug"], "score": m["score"]}
            for m in sorted(matches, key=lambda x: x["score"], reverse=True)[:20]
        ],
        "orphan_suggestions": [
            {"label": o.get("label", ""), "type": o.get("type", "")}
            for o in orphans[:20]
        ],
    }
    return report


def main():
    dry_run = "--dry-run" in sys.argv
    auto_fix = "--auto-fix" in sys.argv

    print("=" * 60)
    print("GRAPHIFY BRIDGE — graph-from-wiki.json ↔ wiki/ cross-references")
    print("=" * 60)

    # 1. Load graph
    print("\n[1/6] Loading graph-from-wiki.json...")
    graph = load_graph()
    print(f"  Nodes: {len(graph.get('nodes', []))}")
    print(f"  Edges: {len(graph.get('edges', []))}")

    # 2. Load wiki slugs
    print("\n[2/6] Loading wiki slugs...")
    slugs = load_slugs()
    print(f"  Wiki slugs: {len(slugs)}")

    # 3. Fuzzy match
    print("\n[3/6] Fuzzy matching graph nodes to wiki slugs...")
    matches = match_graph_to_slugs(graph, slugs)
    print(f"  Matches: {len(matches)}")

    # 4. Detect orphans
    print("\n[4/6] Detecting orphan graph nodes...")
    matched_slugs = {m["matched_slug"] for m in matches}
    orphans = detect_orphan_nodes(graph, matched_slugs)
    print(f"  Orphans: {len(orphans)}")

    # 5. Verify graph edges against actual wikilinks
    print("\n[5/6] Verifying graph edges against wiki wikilinks...")
    edge_verification = verify_graph_edges_against_wikilinks(graph, slugs)
    print(f"  Verified: {edge_verification['verified']}")
    print(f"  Mismatched: {edge_verification['mismatched']}")
    print(f"  Missing files: {edge_verification['missing_files']}")

    # 6. Add backlinks & Dataview for ALL matched files
    print("\n[6/6] Adding backlinks and Dataview queries...")
    new_links = 0
    dataview_added = 0
    errors = []
    
    for i, match in enumerate(matches):
        slug = match["matched_slug"]
        wiki_path = find_wiki_file(slug)
        if not wiki_path:
            errors.append(f"File not found for slug '{slug}'")
            continue
        graph_node = match["graph_node"]
        
        # Add backlink
        if add_backlinks_to_file(wiki_path, graph_node.get("id", ""), graph_node.get("label", ""), dry_run=dry_run):
            new_links += 1
        
        # Add Dataview query
        if add_dataview_query(wiki_path, graph_node.get("id", ""), graph_node.get("label", ""), dry_run=dry_run):
            dataview_added += 1
        
        # Progress indicator for large batches
        if dry_run and (i + 1) % 100 == 0:
            print(f"  Processing... {i+1}/{len(matches)}")
    
    if errors:
        print(f"  Errors: {len(errors)}")
        for e in errors[:5]:
            print(f"    - {e}")
    
    print(f"  New backlinks: {new_links}")
    print(f"  Dataview queries: {dataview_added}")

    # Report
    report = generate_report(matches, orphans, new_links, 0, dataview_added, edge_verification)
    print("\n" + "=" * 60)
    print("BRIDGE REPORT")
    print("=" * 60)
    print(f"  Graph nodes: {report['total_graph_nodes']}")
    print(f"  Matched:     {report['matched_nodes']} ({report['match_rate']}%)")
    print(f"  Orphans:     {report['orphan_nodes']}")
    print(f"  New links:   {report['new_links_added']}")
    print(f"  Dataview:    {report['dataview_added']}")

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
    report_path = PROJECT_ROOT.parent / "graphify-out" / "bridge_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"  Report saved to: {report_path}")

    return report


if __name__ == "__main__":
    main()
