#!/usr/bin/env python3
"""
graphify_query.py — Концептуальний пошук через graph-from-wiki.json

Алгоритм:
1. Завантажити graph-from-wiki.json
2. Знайти найближчі вузли до запиту (fuzzy match)
3. BFS depth=N від знайдених вузлів
4. Завантажити топ-5 wiki-сторінок
5. Повернути контекст для LLM

Usage:
  python3 tools/graphify_query.py "RAG"                    # default depth=2
  python3 tools/graphify_query.py "transformers architecture" --depth 3
  python3 tools/graphify_query.py "agent workflow" --json   # JSON output
"""

import json
import sys
import argparse
from pathlib import Path
from collections import deque
from difflib import SequenceMatcher

# === Configuration ===
PROJECT_ROOT = Path(__file__).resolve().parent.parent
GRAPH_JSON = PROJECT_ROOT.parent / "graphify-out" / "graph-from-wiki.json"
WIKI_DIR = PROJECT_ROOT / "wiki"

# BFS parameters
DEFAULT_DEPTH = 2
DEFAULT_TOP_K = 5


def fuzzy_match(query: str, target: str) -> float:
    """Calculate similarity between query and target.
    Uses word-level matching: each query word checked against target.
    """
    q_words = query.lower().strip().split()
    t_lower = target.lower()
    
    if not q_words:
        return 0.0
    
    # Score: fraction of query words found as substrings
    found = 0
    for word in q_words:
        if word in t_lower:
            found += 1
    
    word_score = found / len(q_words)
    
    # Also do character-level for partial matches
    char_score = SequenceMatcher(None, q_words[0], t_lower).ratio()
    
    # Combined: word-level is primary, char-level is fallback
    return 0.8 * word_score + 0.2 * char_score


def find_relevant_nodes(graph: dict, query: str, top_k: int = 5) -> list:
    """Find nodes most relevant to the query."""
    scores = []
    for node in graph.get("nodes", []):
        label = node.get("label", "")
        slug = node.get("id", "")
        
        # Score by label similarity
        label_score = fuzzy_match(query, label)
        
        # Score by slug similarity
        slug_score = fuzzy_match(query, slug)
        
        # Boost if query contains slug or vice versa
        if slug.lower() in label.lower() or label.lower() in slug.lower():
            label_score = max(label_score, 0.85)
        
        # Combined score (label is more important)
        combined = 0.7 * label_score + 0.3 * slug_score
        
        if combined > 0.3:  # Threshold
            scores.append({
                "node": node,
                "label": label,
                "slug": slug,
                "score": round(combined, 3)
            })
    
    # Sort by score descending, but prioritize "concept" and "playbook" types
    # Filter out obvious noise: composer packages, vendor files
    type_priority = {"concept": 0, "playbook": 1, "comparison": 2, "entity": 3, "research": 4}
    for item in scores:
        node_type = item["node"].get("type", "unknown")
        item["type_priority"] = type_priority.get(node_type, 5)
    
    scores.sort(key=lambda x: (-x["score"], x["type_priority"]))
    
    # Filter out noise: vendor/composer files
    filtered = []
    for item in scores:
        label = item["label"].lower()
        if any(skip in label for skip in ["vendor/", "node_modules/", "phpunit/", "composer/"]):
            continue
        filtered.append(item)
    
    return filtered[:top_k]


def bfs_from_nodes(graph: dict, start_nodes: list, max_depth: int) -> dict:
    """BFS from multiple start nodes, return visited nodes and edges."""
    visited = {}  # slug -> {node, depth, distance_from_query}
    queue = deque()
    
    # Initialize with start nodes
    for item in start_nodes:
        slug = item["slug"]
        if slug not in visited:
            visited[slug] = {
                "node": item["node"],
                "depth": 0,
                "distance_from_query": item["score"]
            }
            queue.append((slug, 0))
    
    # Build adjacency list AND a slug->node lookup
    slug_to_node = {}
    for i, node in enumerate(graph.get("nodes", [])):
        slug_to_node[node.get("id", "")] = node
    
    adj = {}
    for edge in graph.get("edges", []):
        src = edge.get("source", "")
        tgt = edge.get("target", "")
        if src not in adj:
            adj[src] = []
        if tgt not in adj:
            adj[tgt] = []
        adj[src].append(tgt)
        adj[tgt].append(src)  # undirected
    
    # BFS
    while queue:
        current_slug, current_depth = queue.popleft()
        
        if current_depth >= max_depth:
            continue
        
        for neighbor in adj.get(current_slug, []):
            if neighbor not in visited:
                node_data = slug_to_node.get(neighbor)
                visited[neighbor] = {
                    "node": node_data,
                    "depth": current_depth + 1,
                    "distance_from_query": visited[current_slug]["distance_from_query"] * 0.8
                }
                queue.append((neighbor, current_depth + 1))
    
    return visited


def load_wiki_page(slug: str) -> str:
    """Load wiki page content by slug — search by partial filename match."""
    # First try exact match
    for dir_name in ["", "comparisons/", "entities/", "concepts/", "research/", "playbooks/"]:
        wiki_path = WIKI_DIR / f"{slug}.md" if not dir_name else WIKI_DIR / f"{dir_name}{slug}.md"
        if wiki_path.exists():
            return _read_wiki_content(wiki_path)
    
    # Fallback: search by partial match
    for root_dir in [WIKI_DIR]:
        for md_file in root_dir.rglob("*.md"):
            if md_file.name == "index.md":
                continue
            file_slug = md_file.stem.lower().replace("-", "")
            target_slug = slug.lower().replace("-", "")
            if target_slug in file_slug or file_slug in target_slug:
                return _read_wiki_content(md_file)
    
    return None


def _read_wiki_content(wiki_path: Path) -> str:
    """Read wiki content, strip frontmatter, limit length."""
    content = wiki_path.read_text(encoding="utf-8")
    if content.startswith("---"):
        end_fm = content.find("---", 3)
        if end_fm > 0:
            content = content[end_fm+3:].strip()
    return content[:1500]


def query(graph: dict, query_text: str, depth: int = DEFAULT_DEPTH, top_k: int = DEFAULT_TOP_K) -> dict:
    """Main query function."""
    # 1. Find relevant nodes
    relevant = find_relevant_nodes(graph, query_text, top_k=top_k)
    
    if not relevant:
        return {
            "query": query_text,
            "found_nodes": 0,
            "bfs_nodes": 0,
            "pages": [],
            "context": f"No relevant nodes found for: {query_text}"
        }
    
    # 2. BFS from relevant nodes
    visited = bfs_from_nodes(graph, relevant, max_depth=depth)
    
    # 3. Sort visited nodes by relevance
    sorted_nodes = sorted(visited.items(), key=lambda x: x[1]["distance_from_query"], reverse=True)
    
    # 4. Load wiki pages for top nodes
    pages = []
    for slug, info in sorted_nodes[:top_k]:
        page_content = load_wiki_page(slug)
        if page_content:
            pages.append({
                "slug": slug,
                "title": info["node"].get("label", slug) if info["node"] else slug,
                "depth": info["depth"],
                "score": round(info["distance_from_query"], 3),
                "content": page_content
            })
    
    # 5. Build context
    context_lines = []
    for p in pages:
        context_lines.append(f"\n## {p['title']} (slug: {p['slug']}, depth: {p['depth']}, score: {p['score']})")
        context_lines.append(p["content"])
    
    return {
        "query": query_text,
        "found_nodes": len(relevant),
        "relevant_nodes": [{"label": r["label"], "slug": r["slug"], "score": r["score"]} for r in relevant],
        "bfs_nodes": len(visited),
        "pages": pages,
        "context": "\n".join(context_lines) if context_lines else "No wiki pages found"
    }


def main():
    parser = argparse.ArgumentParser(description="Query graph-from-wiki.json for conceptual context")
    parser.add_argument("query", help="Query text (e.g., 'RAG', 'transformers architecture')")
    parser.add_argument("--depth", type=int, default=DEFAULT_DEPTH, help=f"BFS depth (default: {DEFAULT_DEPTH})")
    parser.add_argument("--top-k", type=int, default=DEFAULT_TOP_K, help=f"Top K results (default: {DEFAULT_TOP_K})")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    # Load graph
    if not GRAPH_JSON.exists():
        print(f"ERROR: {GRAPH_JSON} not found. Run wiki_graph_generator.py first.", file=sys.stderr)
        sys.exit(1)
    
    with open(GRAPH_JSON) as f:
        graph = json.load(f)
    
    print(f"Graph loaded: {len(graph.get('nodes', []))} nodes, {len(graph.get('edges', []))} edges", file=sys.stderr)
    
    # Execute query
    result = query(graph, args.query, depth=args.depth, top_k=args.top_k)
    
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("=" * 60)
        print(f"QUERY: {args.query}")
        print("=" * 60)
        print(f"\nFound {result['found_nodes']} relevant nodes")
        print(f"Visited {result['bfs_nodes']} nodes via BFS (depth={args.depth})")
        
        if result.get("relevant_nodes"):
            print("\nTop relevant nodes:")
            for r in result["relevant_nodes"][:5]:
                print(f"  {r['label']:50s} ({r['slug']}) score={r['score']}")
        
        if result.get("pages"):
            print(f"\nTop {len(result['pages'])} wiki pages loaded:")
            for p in result["pages"]:
                print(f"  [{p['depth']}] {p['title']:50s} (score={p['score']})")
        
        print("\n" + "=" * 60)
        print("CONTEXT:")
        print("=" * 60)
        print(result["context"])


if __name__ == "__main__":
    main()
