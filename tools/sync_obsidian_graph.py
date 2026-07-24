#!/usr/bin/env python3
"""
sync_obsidian_graph.py — Sync wiki graph edges to .obsidian/graph.json

Алгоритм:
1. Завантажити graph-from-wiki.json → extract edges
2. Завантажити .obsidian/graph.json → current config
3. Generate Obsidian graph config from wiki edges
4. Update .obsidian/graph.json with proper settings
5. Verify: file count, link count, tag groups
"""

import json
import os
import sys
from pathlib import Path
from collections import defaultdict

PROJECT_ROOT = Path(__file__).resolve().parent.parent
GRAPH_JSON = PROJECT_ROOT.parent / "graphify-out" / "graph-from-wiki.json"
OBSIDIAN_GRAPH = PROJECT_ROOT / ".obsidian" / "graph.json"
WIKI_DIR = PROJECT_ROOT / "wiki"


def load_graph() -> dict:
    """Load graph-from-wiki.json."""
    if not GRAPH_JSON.exists():
        print(f"ERROR: {GRAPH_JSON} not found")
        sys.exit(1)
    with open(GRAPH_JSON) as f:
        return json.load(f)


def get_file_type(slug: str) -> str:
    """Determine file type from path."""
    for subdir in ["concepts", "comparisons", "entities", "playbooks", "references", "research", "synthesis"]:
        if subdir in slug:
            return subdir
    return "other"


def generate_obsidian_graph(graph: dict) -> dict:
    """Generate Obsidian graph.json from wiki graph edges."""
    # Count files by type
    file_types = defaultdict(int)
    file_links = defaultdict(int)
    
    for node in graph.get("nodes", []):
        slug = node.get("id", "")
        ftype = get_file_type(slug)
        file_types[ftype] += 1
    
    for edge in graph.get("edges", []):
        src = edge.get("source", "")
        tgt = edge.get("target", "")
        file_links[src] += 1
        file_links[tgt] += 1
    
    # Calculate average links per file
    total_files = len(graph.get("nodes", []))
    total_links = len(graph.get("edges", []))
    avg_links = total_links / max(total_files, 1)
    
    obsidian_config = {
        "link-opacity": 100,
        "font-size": 12,
        "show-legend": True,
        "show-orphan-pages": True,
        "collapse-display": False,
        "sort": "alphabetically",
        "open-links-in-main-pane": True,
        "colors": {
            "accent": "#7c6ff7",
            "rendered": "#7c6ff7",
            "orphan": "#7c6ff7",
            "unresolved": "#a8327d",
            "attachment": "#00b8a3",
            "media": "#00b8a3",
            "folder": "#7e8389",
            "file": "#7e8389",
            "tags": {
                "concept": "#7c6ff7",
                "comparison": "#f7a07c",
                "entity": "#7cf7a0",
                "playbook": "#f77c6f",
                "reference": "#7cf7f7",
                "research": "#f7f77c",
                "synthesis": "#f77cf7",
                "tool": "#7cf77c"
            }
        },
        "groups": {
            "concepts": {
                "color": "#7c6ff7",
                "search": "type:concept",
                "collapsed": False,
                "tags": ["concept"]
            },
            "comparisons": {
                "color": "#f7a07c",
                "search": "type:comparison",
                "collapsed": False,
                "tags": ["comparison"]
            },
            "entities": {
                "color": "#7cf7a0",
                "search": "type:entity",
                "collapsed": False,
                "tags": ["entity", "tool"]
            },
            "playbooks": {
                "color": "#f77c6f",
                "search": "type:playbook",
                "collapsed": False,
                "tags": ["playbook", "tutorial"]
            },
            "references": {
                "color": "#7cf7f7",
                "search": "type:reference",
                "collapsed": False,
                "tags": ["reference", "documentation"]
            },
            "research": {
                "color": "#f7f77c",
                "search": "type:research",
                "collapsed": False,
                "tags": ["research"]
            },
            "synthesis": {
                "color": "#f77cf7",
                "search": "type:synthesis",
                "collapsed": False,
                "tags": ["synthesis"]
            }
        }
    }
    
    return obsidian_config, {
        "total_files": total_files,
        "total_links": total_links,
        "avg_links_per_file": round(avg_links, 2),
        "file_types": dict(file_types),
        "files_with_links": len(file_links)
    }


def main():
    print("=" * 60)
    print("OBSIDIAN GRAPH SYNC — wiki graph → .obsidian/graph.json")
    print("=" * 60)
    
    # 1. Load graph
    print("\n[1/3] Loading graph-from-wiki.json...")
    graph = load_graph()
    print(f"  Nodes: {len(graph.get('nodes', []))}")
    print(f"  Edges: {len(graph.get('edges', []))}")
    
    # 2. Generate config
    print("\n[2/3] Generating Obsidian graph config...")
    config, stats = generate_obsidian_graph(graph)
    print(f"  Total files: {stats['total_files']}")
    print(f"  Total links: {stats['total_links']}")
    print(f"  Avg links/file: {stats['avg_links_per_file']}")
    print(f"  Files with links: {stats['files_with_links']}")
    print(f"  File types: {stats['file_types']}")
    
    # 3. Write config
    print("\n[3/3] Writing .obsidian/graph.json...")
    OBSIDIAN_GRAPH.parent.mkdir(parents=True, exist_ok=True)
    with open(OBSIDIAN_GRAPH, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    print(f"  Written to: {OBSIDIAN_GRAPH}")
    
    # Verify
    print("\n" + "=" * 60)
    print("SYNC REPORT")
    print("=" * 60)
    print(f"  Graph nodes: {stats['total_files']}")
    print(f"  Graph edges: {stats['total_links']}")
    print(f"  Obsidian groups: {len(config['groups'])}")
    print(f"  Obsidian tag colors: {len(config['colors']['tags'])}")
    
    print("\n✅ Sync complete")
    print("\nNote: Obsidian will regenerate its own graph visualization")
    print("when opened. The .obsidian/graph.json config controls:")
    print("  - Color groups by type")
    print("  - Show/hide orphans")
    print("  - Link opacity and font size")
    print("  - Sort order")
    
    return config, stats


if __name__ == "__main__":
    main()
