#!/usr/bin/env python3
"""
wiki_graph_generator.py — Generate graph.json from wiki wikilinks

Цей скрипт конвертує wiki/ з його [[wikilinks]] у graphify-сумісний graph.json формат.
Не потребує LLM — використовує існуючі wikilinks як edges.

Алгоритм:
1. Scan всі wiki .md файли
2. Extract [[wikilink]] посилання з контенту
3. Створити nodes (кожна wiki сторінка) + edges (wikilinks)
4. Output: graphify-out/graph.json (NetworkX-сумісний формат)

Usage:
  python3 tools/wiki_graph_generator.py [--dry-run] [--output path]
"""

import json
import re
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime


# === Configuration ===
PROJECT_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = PROJECT_ROOT / "wiki"
OUTPUT_DIR = PROJECT_ROOT / "graphify-out"


def extract_wikilinks(content: str) -> list:
    """Extract all [[wikilink]] references from markdown content."""
    links = []
    for match in re.finditer(r"\[\[([^\]|]+?)(?:\|([^\]]+))?\]\]", content):
        target = match.group(1).strip()
        alias = match.group(2).strip() if match.group(2) else None
        links.append((target, alias))
    return links


def extract_frontmatter(content: str) -> dict:
    """Extract frontmatter from markdown content."""
    fm = {}
    match = re.match(r"^---\s*\n(.*?)\n---\s*", content, re.DOTALL)
    if match:
        fm_text = match.group(1)
        for line in fm_text.split("\n"):
            if ":" in line:
                key, _, value = line.partition(":")
                fm[key.strip()] = value.strip().strip('"').strip("'")
    return fm


def extract_tags(frontmatter: dict) -> list:
    """Extract tags from frontmatter.
    Handles both YAML formats:
      tags: tag1, tag2, tag3
      tags: [tag1, tag2, tag3]
    """
    tags_raw = frontmatter.get("tags", "")
    if not tags_raw:
        return []
    
    tags_str = str(tags_raw).strip()
    
    # Handle YAML inline list: [tag1, tag2, tag3]
    if tags_str.startswith("[") and tags_str.endswith("]"):
        inner = tags_str[1:-1]
        return [t.strip().strip("'\"") for t in inner.split(",") if t.strip().strip("'\"")]
    
    # Handle comma-separated: tag1, tag2, tag3
    return [t.strip().strip("'\"") for t in tags_str.split(",") if t.strip().strip("'\"")]


def extract_type(frontmatter: dict) -> str:
    """Extract page type from frontmatter."""
    return frontmatter.get("type", "concept")


def extract_confidence(frontmatter: dict) -> float:
    """Extract confidence score from frontmatter."""
    try:
        return float(frontmatter.get("confidence", 0.7))
    except (ValueError, TypeError):
        return 0.7


def scan_wiki_files(wiki_dir: Path) -> list:
    """Scan all wiki .md files and extract metadata."""
    pages = []
    
    for md_file in wiki_dir.rglob("*.md"):
        if md_file.name == "index.md":
            continue
        
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception:
            continue
        
        # Skip if no meaningful content at all
        if len(content) < 50:
            continue
        
        frontmatter = extract_frontmatter(content)
        slug = frontmatter.get("slug", md_file.stem)
        wikilinks = extract_wikilinks(content)
        tags = extract_tags(frontmatter)
        page_type = extract_type(frontmatter)
        confidence = extract_confidence(frontmatter)
        
        # Extract title from frontmatter or first heading
        title = frontmatter.get("title", "")
        if not title:
            title_match = re.search(r"^#\s+(.+)", content, re.MULTILINE)
            title = title_match.group(1).strip() if title_match else slug
        
        pages.append({
            "path": str(md_file.relative_to(PROJECT_ROOT)),
            "slug": slug,
            "title": title,
            "type": page_type,
            "tags": tags,
            "confidence": confidence,
            "outbound_links": [link[0] for link in wikilinks],
            "source_file": str(md_file),
        })
    
    return pages


def build_graph(pages: list) -> dict:
    """Build graph.json from wiki pages and their wikilinks."""
    
    # Create slug → page mapping
    slug_map = {p["slug"]: p for p in pages}
    
    # Build nodes
    nodes = []
    for page in pages:
        node = {
            "id": page["slug"],
            "label": page["title"],
            "type": page["type"],
            "file_type": "document",
            "source_file": page["path"],
            "source_location": None,
            "source_url": None,
            "captured_at": datetime.utcnow().isoformat() + "Z",
            "author": None,
            "contributor": None,
            "tags": page["tags"],
            "confidence": page["confidence"],
        }
        nodes.append(node)
    
    # Build edges from wikilinks
    edges = []
    edge_set = set()
    for page in pages:
        for link_target in page["outbound_links"]:
            # Normalize: if target exists as slug, use it; otherwise use as-is
            target_slug = link_target if link_target in slug_map else link_target
            edge_key = (page["slug"], target_slug)
            if edge_key not in edge_set:
                edge_set.add(edge_key)
                edge = {
                    "source": page["slug"],
                    "target": target_slug,
                    "type": "wikilink",
                    "weight": 1,
                }
                edges.append(edge)
    
    # Detect communities based on tags (simple co-occurrence)
    tag_to_pages = defaultdict(list)
    for page in pages:
        for tag in page["tags"]:
            tag_to_pages[tag].append(page["slug"])
    
    # Build communities: tags with ≥2 pages
    communities = []
    for tag, page_list in sorted(tag_to_pages.items()):
        if len(page_list) >= 2:
            communities.append({
                "id": f"community_{tag}",
                "label": tag,
                "nodes": sorted(page_list),
                "size": len(page_list),
            })
    
    # Sort communities by size
    communities.sort(key=lambda c: c["size"], reverse=True)
    
    return {
        "metadata": {
            "generator": "wiki_graph_generator.py",
            "version": "1.0.0",
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "source": "wiki/ (wikilinks)",
            "total_pages": len(pages),
        },
        "nodes": nodes,
        "edges": edges,
        "communities": communities[:50],  # Top 50 communities
    }


def generate_report(graph: dict) -> dict:
    """Generate a summary report."""
    nodes = graph["nodes"]
    edges = graph["edges"]
    communities = graph["communities"]
    
    # Type distribution
    type_dist = defaultdict(int)
    for n in nodes:
        type_dist[n.get("type", "unknown")] += 1
    
    # Tag distribution
    tag_counts = defaultdict(int)
    for n in nodes:
        for tag in n.get("tags", []):
            tag_counts[tag] += 1
    
    # Top tags
    top_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:20]
    
    # Top nodes by inbound links
    inbound_counts = defaultdict(int)
    for e in edges:
        inbound_counts[e["target"]] += 1
    top_inbound = sorted(inbound_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    
    return {
        "generated_at": graph["metadata"]["generated_at"],
        "total_nodes": len(nodes),
        "total_edges": len(edges),
        "total_communities": len(communities),
        "type_distribution": dict(type_dist),
        "top_tags": [{"tag": t, "count": c} for t, c in top_tags],
        "top_inbound": [{"node": n, "inbound_links": c} for n, c in top_inbound],
        "top_communities": [{"id": c["id"], "label": c["label"], "size": c["size"]} for c in communities[:10]],
    }


def main():
    dry_run = "--dry-run" in sys.argv
    output_path = None
    for i, arg in enumerate(sys.argv):
        if arg == "--output" and i + 1 < len(sys.argv):
            output_path = sys.argv[i + 1]
    
    print("=" * 60)
    print("WIKI GRAPH GENERATOR — wiki/ → graph.json")
    print("=" * 60)
    
    # 1. Scan wiki
    print(f"\n[1/4] Scanning wiki files in {WIKI_DIR}...")
    if not WIKI_DIR.exists():
        print(f"  ERROR: {WIKI_DIR} not found")
        sys.exit(1)
    
    pages = scan_wiki_files(WIKI_DIR)
    print(f"  Pages scanned: {len(pages)}")
    
    if not pages:
        print("  ERROR: No wiki pages found")
        sys.exit(1)
    
    # 2. Build graph
    print("\n[2/4] Building graph from wikilinks...")
    graph = build_graph(pages)
    print(f"  Nodes: {len(graph['nodes'])}")
    print(f"  Edges: {len(graph['edges'])}")
    print(f"  Communities: {len(graph['communities'])}")
    
    # 3. Generate report
    print("\n[3/4] Generating report...")
    report = generate_report(graph)
    print(f"  Top type: {max(report['type_distribution'].items(), key=lambda x: x[1])}")
    print(f"  Top tag: {report['top_tags'][0] if report['top_tags'] else 'N/A'}")
    print(f"  Top inbound: {report['top_inbound'][0] if report['top_inbound'] else 'N/A'}")
    
    # 4. Save
    print("\n[4/4] Saving graph.json...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    graph_path = output_path or OUTPUT_DIR / "graph.json"
    with open(graph_path, "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)
    print(f"  Saved to: {graph_path}")
    
    # Save report
    report_path = OUTPUT_DIR / "wiki_graph_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"  Report saved to: {report_path}")
    
    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Total pages:       {report['total_nodes']}")
    print(f"  Total wikilinks:   {report['total_edges']}")
    print(f"  Communities:       {report['total_communities']}")
    print(f"  Avg edges/page:    {report['total_edges']/max(report['total_nodes'],1):.2f}")
    
    if report["top_tags"]:
        print(f"\n  Top 5 tags:")
        for t in report["top_tags"][:5]:
            print(f"    {t['tag']:30s} ({t['count']})")
    
    if report["top_inbound"]:
        print(f"\n  Top 5 most-linked pages:")
        for t in report["top_inbound"][:5]:
            print(f"    {t['node']:40s} ({t['inbound_links']} inbound)")
    
    if dry_run:
        print("\n⚠️  Dry run — file already saved (dry-run flag is informational)")
    else:
        print("\n✅ Graph generated successfully")
    
    return graph


if __name__ == "__main__":
    main()
