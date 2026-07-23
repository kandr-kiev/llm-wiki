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
import re
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

# Stop words to strip from natural-language queries (EN + UA)
STOP_WORDS = {
    # English
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "shall", "can", "need", "dare", "ought",
    "used", "to", "of", "in", "for", "on", "with", "at", "by", "from",
    "as", "into", "through", "during", "before", "after", "above", "below",
    "between", "out", "off", "over", "under", "again", "further", "then",
    "once", "here", "there", "when", "where", "why", "how", "all", "both",
    "each", "few", "more", "most", "other", "some", "such", "no", "nor",
    "not", "only", "own", "same", "so", "than", "too", "very", "just",
    "about", "up", "down", "and", "but", "or", "if", "while", "that",
    "this", "these", "those", "it", "its", "what", "which", "who", "whom",
    "because", "although", "though", "since", "until", "unless",
    # Common non-technical filler words
    "work", "works", "working", "thing", "things", "make", "made",
    "get", "got", "give", "given", "take", "took", "let", "use", "used",
    "know", "knows", "think", "see", "look", "tell", "says", "said",
    "help", "like", "much", "many", "well", "back", "even", "still",
    "also", "new", "way", "ways", "lot", "part", "place", "case",
    "week", "company", "system", "program", "project", "home",
    "page", "hand", "part", "point", "game", "end", "good", "top",
    "vs", "versus", "comparison", "compare", "compared",
    # Ukrainian
    "як", "що", "де", "коли", "чому", "про", "з", "по", "на", "в", "і",
    "та", "або", "але", "який", "яка", "які", "це", "той", "такий",
    "розкажи", "поясни", "знайди", "шукай", "мені", "мені потрібно",
    "як працює", "що таке", "що означає", "який", "про що",
    # Ukrainian filler
    "архітектуру", "порівняння", "яке", "мені", "щодо", "з",
}

# Common question patterns to strip
QUESTION_PATTERNS = [
    r"(?:how|what|when|where|why|which|who)\s+(?:does?|is|are|was|were|can|could|would|should|does?|has|have|did|do|works?|function[s]?)\s*",
    r"(?:як|що|де|коли|чому|який)\s+(?:працює|таке|означає|є|робить|виконує)\s*",
    r"(?:tell|explain|describe|find|search|look up|show me)\s+(?:me\s+)?(?:about\s+)?",
    r"(?:розкажи|поясни|описуй|знайди|шукай|покажи)\s+(?:мені\s+)?(?:про|щодо|з)\s*",
    r"information\s+about\s+",
    r"info\s+on\s+",
]


def preprocess_query(raw_query: str, graph: dict = None) -> tuple:
    """Extract technical keywords from natural language query.
    
    Strips question patterns, stop words, and generic words.
    Works with English, Ukrainian, and mixed input.
    
    Returns: (processed_query, debug_info)
    """
    q = raw_query.strip()
    
    # Step 1: Strip common question patterns
    for pattern in QUESTION_PATTERNS:
        q = re.sub(pattern, "", q, flags=re.IGNORECASE)
    
    # Step 2: Remove question marks
    q = re.sub(r'\?', '', q)
    
    # Step 3: Split into words/tokens (handle hyphens, underscores, spaces)
    tokens = re.split(r'[\s\-_]+', q.lower())
    
    # Step 4: Filter stop words
    keywords = []
    removed_generic = []
    for token in tokens:
        token = token.strip()
        if not token:
            continue
        if len(token) < 2:
            continue
        if token in STOP_WORDS:
            continue
        keywords.append(token)
    
    # Step 5: If graph provided, filter frequency-based generic words
    if graph:
        generic_words = _build_generic_stoplist(graph)
        filtered = []
        for kw in keywords:
            if kw in generic_words:
                removed_generic.append(kw)
            else:
                filtered.append(kw)
        keywords = filtered
    else:
        removed_generic = []
    
    # Step 6: Remove duplicates, preserve order
    seen = set()
    unique_keywords = []
    for kw in keywords:
        if kw not in seen:
            seen.add(kw)
            unique_keywords.append(kw)
    
    result = " ".join(unique_keywords)
    
    # If preprocessing stripped everything, return original
    if not result:
        result = raw_query.strip()
    
    debug_info = {
        "original": raw_query,
        "processed": result,
        "words_kept": unique_keywords,
        "stopwords_removed": [w for w in re.split(r'[\s\-_]+', raw_query.lower()) if w in STOP_WORDS and len(w) >= 2],
        "generic_removed": removed_generic,
    }
    
    return result, debug_info


def _build_generic_stoplist(graph: dict) -> set:
    """Build stoplist from graph: words appearing in >20% of node labels are too generic."""
    labels = []
    for node in graph.get("nodes", []):
        label = node.get("label", "").lower()
        words = re.split(r'[\s\-_]+', label)
        words.extend(re.findall(r'[A-Z][a-z]+', label))
        labels.extend(words)
    
    total = len(graph.get("nodes", []))
    if total == 0:
        return set()
    
    word_counts = {}
    for w in labels:
        w = w.lower().strip()
        if len(w) >= 2:
            word_counts[w] = word_counts.get(w, 0) + 1
    
    threshold = total * 0.20
    return {w for w, c in word_counts.items() if c > threshold}


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


def find_relevant_nodes(graph: dict, query: str, top_k: int = 5, min_score: float = 0.3) -> list:
    """Find nodes most relevant to the query."""
    scores = []
    
    # Build slug->node lookup for type info
    slug_to_type = {}
    for node in graph.get("nodes", []):
        slug_to_type[node.get("id", "")] = node.get("type", "unknown")
    
    for node in graph.get("nodes", []):
        label = node.get("label", "")
        slug = node.get("id", "")
        node_type = slug_to_type.get(slug, "unknown")
        
        # Filter out package-version nodes (e.g. langchain-core==1.4.9)
        label_lower = label.lower()
        if re.search(r'==\d+\.\d+', label_lower):
            continue
        if re.search(r'~=\d+\.\d+', label_lower):
            continue
        if re.search(r'\d+\.x\.x', label_lower):
            continue
        
        # Score by label similarity
        label_score = fuzzy_match(query, label)
        
        # Score by slug similarity
        slug_score = fuzzy_match(query, slug)
        
        # Boost if ALL query words appear in label (exact match of all terms)
        q_words = query.lower().strip().split()
        if q_words and all(w in label_lower for w in q_words):
            label_score = max(label_score, 0.85)
        
        # Combined score (label is more important)
        combined = 0.7 * label_score + 0.3 * slug_score
        
        if combined > min_score:  # Threshold
            scores.append({
                "node": node,
                "label": label,
                "slug": slug,
                "score": round(combined, 3),
                "type": node_type
            })
    
    # Sort by score descending, but prioritize "concept" and "playbook" types
    # Filter out obvious noise: composer packages, vendor files
    type_priority = {"concept": 0, "playbook": 1, "comparison": 2, "entity": 3, "research": 4}
    for item in scores:
        item["type_priority"] = type_priority.get(item["type"], 5)
    
    scores.sort(key=lambda x: (-x["score"], x["type_priority"]))
    
    # Filter out noise: vendor/composer files, package comparisons
    filtered = []
    for item in scores:
        label = item["label"].lower()
        if any(skip in label for skip in ["vendor/", "node_modules/", "phpunit/", "composer/"]):
            continue
        # Lower priority for package-version comparisons
        if item["type"] == "comparison" and re.search(r'==\d+', item["label"]):
            item["type_priority"] = 9  # Push to very end
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
    # Preprocess: extract keywords from natural language
    processed, debug_info = preprocess_query(query_text, graph=graph)
    
    # 1. Find relevant nodes
    relevant = find_relevant_nodes(graph, processed, top_k=top_k)
    
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
    parser.add_argument("--debug", action="store_true", help="Show query preprocessing details")
    
    args = parser.parse_args()
    
    # Load graph
    if not GRAPH_JSON.exists():
        print(f"ERROR: {GRAPH_JSON} not found. Run wiki_graph_generator.py first.", file=sys.stderr)
        sys.exit(1)
    
    with open(GRAPH_JSON) as f:
        graph = json.load(f)
    
    print(f"Graph loaded: {len(graph.get('nodes', []))} nodes, {len(graph.get('edges', []))} edges", file=sys.stderr)
    
    # Preprocess and show debug info
    processed, debug_info = preprocess_query(args.query, graph=graph)
    if args.debug:
        print(f"\n📝 Preprocessing:", file=sys.stderr)
        print(f"   Original:         '{debug_info['original']}'", file=sys.stderr)
        print(f"   Processed:        '{debug_info['processed']}'", file=sys.stderr)
        print(f"   Words kept:       {debug_info['words_kept']}", file=sys.stderr)
        if debug_info['stopwords_removed']:
            print(f"   Stopwords removed:{debug_info['stopwords_removed']}", file=sys.stderr)
        if debug_info['generic_removed']:
            print(f"   Generic removed:  {debug_info['generic_removed']}", file=sys.stderr)
    
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
