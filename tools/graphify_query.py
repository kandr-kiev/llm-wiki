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
from collections import deque, defaultdict
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
    
    # If preprocessing stripped everything, return empty (not original)
    # so the caller knows the query has no meaningful terms
    if not result:
        result = ""
    
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
    Normalizes hyphens/underscores to spaces for consistent matching.
    """
    # Normalize: hyphens and underscores → spaces
    q_norm = query.lower().strip().replace("-", " ").replace("_", " ")
    t_norm = target.lower().replace("-", " ").replace("_", " ")
    
    q_words = [w for w in q_norm.split() if len(w) >= 2]
    t_lower = t_norm
    
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


# Type priority multipliers — concept/playbook pages are higher quality
TYPE_BONUS = {
    "concept": 1.2,
    "playbook": 1.1,
    "entity": 1.0,
    "comparison": 1.0,
    "research": 0.9,
}

# Noise patterns to exclude from results
NOISE_PATTERNS = ["vendor/", "node_modules/", "phpunit/", "composer/", "issue #", "release notes"]


def calculate_score(query: str, label: str, slug: str, node_type: str,
                    inbound_count: int = 0) -> float:
    """Calculate relevance score for a node given a query.
    
    Multi-factor scoring:
    1. Word match (70%) — PRIMARY signal, WORD-BOUNDARY match in label
    2. Slug match (20%) — WORD-BOUNDARY match in slug
    3. Both-words bonus (10%) — if ALL query words present
    
    Uses regex word boundaries to avoid substring false-positives
    (e.g. "rag" inside "coverage").
    
    Returns: float score (0.0 to 1.0)
    """
    q_words = [w for w in query.lower().split() if len(w) >= 2]
    l_lower = label.lower().replace("-", " ").replace("_", " ")
    s_lower = slug.lower().replace("-", " ").replace("_", " ")
    
    if not q_words:
        return 0.0
    
    # Word match with WORD BOUNDARIES — prevents "rag" matching inside "coverage"
    word_matches = sum(
        1 for w in q_words 
        if re.search(r'\b' + re.escape(w) + r'\b', l_lower)
    )
    word_score = word_matches / len(q_words)
    
    # Slug match with word boundaries
    slug_matches = sum(
        1 for w in q_words 
        if re.search(r'\b' + re.escape(w) + r'\b', s_lower)
    )
    slug_score = slug_matches / len(q_words)
    
    # Both-words bonus (10%) — if ALL query words in label
    all_match = all(
        re.search(r'\b' + re.escape(w) + r'\b', l_lower) 
        for w in q_words
    )
    
    # Base score — word match is primary
    score = (
        0.70 * word_score +
        0.20 * slug_score +
        0.10 * all_match
    )
    
    # Package/version penalty (×0.1)
    if re.search(r'==\d+\.\d+', l_lower) or re.search(r'~=?\d+\.\d+', l_lower):
        score *= 0.1
    
    return round(score, 3)


def find_relevant_nodes(graph: dict, query: str, top_k: int = 5, min_score: float = 0.3) -> list:
    """Find nodes most relevant to the query using multi-factor scoring.
    
    Replaces old fuzzy_match with calculate_score for better relevance.
    Uses inbound link counts as a quality signal.
    """
    scores = []
    
    # Build slug→node lookup + inbound count
    slug_to_node = {}
    inbound_counts = defaultdict(int)
    for edge in graph.get("edges", []):
        inbound_counts[edge.get("target", "")] += 1
    
    for node in graph.get("nodes", []):
        slug_to_node[node.get("id", "")] = node
    
    for node in graph.get("nodes", []):
        label = node.get("label", "")
        slug = node.get("id", "")
        node_type = node.get("type", "unknown")
        
        # Filter out package-version nodes
        label_lower = label.lower()
        if re.search(r'==\d+\.\d+', label_lower):
            continue
        if re.search(r'~=?\d+\.\d+', label_lower):
            continue
        if re.search(r'\d+\.x\.x', label_lower):
            continue
        
        # Get inbound link count for quality signal
        inbound = inbound_counts.get(slug, 0)
        
        # Calculate multi-factor score
        score = calculate_score(query, label, slug, node_type, inbound)
        
        if score > min_score:
            scores.append({
                "node": node,
                "label": label,
                "slug": slug,
                "score": score,
                "type": node_type,
                "inbound": inbound,
            })
    
    # Sort by score descending
    scores.sort(key=lambda x: -x["score"])
    
    # Filter noise
    filtered = []
    for item in scores:
        label = item["label"].lower()
        if any(skip in label for skip in NOISE_PATTERNS):
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


def _read_wiki_content(wiki_path: Path, limit: int = 3000) -> str:
    """Read wiki content, strip frontmatter, limit length.
    
    Args:
        wiki_path: Path to the wiki markdown file
        limit: Max characters (default 3000, can be 500 for summaries)
    """
    content = wiki_path.read_text(encoding="utf-8")
    if content.startswith("---"):
        end_fm = content.find("---", 3)
        if end_fm > 0:
            content = content[end_fm+3:].strip()
    return content[:limit]


def _estimate_tokens(text: str) -> int:
    """Estimate token count: ~4 chars per token."""
    return len(text) // 4


def enforce_token_budget(context: str, budget_chars: int = 3000) -> str:
    """Ensure context fits within token budget.
    
    Budget: ~3000 chars = ~750 tokens (default budget)
    """
    if _estimate_tokens(context) <= budget_chars // 4:
        return context
    return context[:budget_chars] + "\n\n[TRUNCATED — context exceeded budget]"


def query(graph: dict, query_text: str, depth: int = DEFAULT_DEPTH, top_k: int = DEFAULT_TOP_K) -> dict:
    """Main query function with summary-first token optimization.
    
    Strategy:
    1. Load 500-char summaries for ALL top_k nodes
    2. Load full content (3000 chars) only for top-2 most relevant
    3. Enforce total token budget (~750 tokens = ~3000 chars)
    """
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
    
    # 4. Load 500-char summaries for ALL top nodes (cheap scan)
    summaries = {}
    for slug, info in sorted_nodes[:top_k]:
        for dir_name in ["", "comparisons/", "entities/", "concepts/", "research/", "playbooks/"]:
            wiki_path = WIKI_DIR / f"{slug}.md" if not dir_name else WIKI_DIR / f"{dir_name}{slug}.md"
            if wiki_path.exists():
                summaries[slug] = _read_wiki_content(wiki_path, limit=500)
                break
        else:
            # Fallback: partial match
            for md_file in WIKI_DIR.rglob("*.md"):
                if md_file.name == "index.md":
                    continue
                file_slug = md_file.stem.lower().replace("-", "")
                target_slug = slug.lower().replace("-", "")
                if target_slug in file_slug or file_slug in target_slug:
                    summaries[slug] = _read_wiki_content(md_file, limit=500)
                    break
    
    # 5. Load full content (3000 chars) only for top-2 most relevant
    #    — saves tokens when relevance is clear from summary
    full_pages = {}
    pages_to_load_full = sorted_nodes[:min(2, len(sorted_nodes))]
    for slug, info in pages_to_load_full:
        # Try to find the file through standard paths
        found = False
        for dir_name in ["", "comparisons/", "entities/", "concepts/", "research/", "playbooks/"]:
            wiki_path = WIKI_DIR / f"{dir_name}{slug}.md" if dir_name else WIKI_DIR / f"{slug}.md"
            if wiki_path.exists():
                full_pages[slug] = _read_wiki_content(wiki_path, limit=3000)
                found = True
                break
        # Fallback: partial match search
        if not found:
            for md_file in WIKI_DIR.rglob("*.md"):
                if md_file.name == "index.md":
                    continue
                file_slug = md_file.stem.lower().replace("-", "")
                target_slug = slug.lower().replace("-", "")
                if target_slug in file_slug or file_slug in target_slug:
                    full_pages[slug] = _read_wiki_content(md_file, limit=3000)
                    break
    
    # 6. Build context: full content for top-2, summaries for rest
    pages = []
    for slug, info in sorted_nodes[:top_k]:
        title = info["node"].get("label", slug) if info["node"] else slug
        depth_val = info["depth"]
        score = round(info["distance_from_query"], 3)
        
        # Use full content if available, otherwise summary
        if slug in full_pages:
            content = full_pages[slug]
            mode = "full"
        elif slug in summaries:
            content = summaries[slug]
            mode = "summary"
        else:
            continue
        
        pages.append({
            "slug": slug,
            "title": title,
            "depth": depth_val,
            "score": score,
            "content": content,
            "mode": mode,
        })
    
    # 7. Build context with token budget enforcement
    context_lines = []
    for p in pages:
        mode_label = " [FULL]" if p["mode"] == "full" else " [SUMMARY]"
        context_lines.append(f"\n## {p['title']}{mode_label} (slug: {p['slug']}, depth: {p['depth']}, score: {p['score']})")
        context_lines.append(p["content"])
    
    context = "\n".join(context_lines)
    
    # Enforce token budget — cap at ~3000 chars
    context = enforce_token_budget(context, budget_chars=3000)
    
    # 8. Report token usage
    total_chars = len(context)
    estimated_tokens = _estimate_tokens(context)
    
    return {
        "query": query_text,
        "found_nodes": len(relevant),
        "relevant_nodes": [{"label": r["label"], "slug": r["slug"], "score": r["score"]} for r in relevant],
        "bfs_nodes": len(visited),
        "pages": pages,
        "context": context,
        "token_stats": {
            "total_chars": total_chars,
            "estimated_tokens": estimated_tokens,
            "budget_chars": 3000,
            "budget_tokens": 750,
            "mode": "summary-first"
        }
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
                mode_label = "[FULL]" if p["mode"] == "full" else "[SUMMARY]"
                print(f"  [{p['depth']}] {p['title']:50s} (score={p['score']}) {mode_label}")
        
        # Token stats
        stats = result.get("token_stats", {})
        if stats:
            print(f"\n📊 Token usage: {stats['total_chars']} chars, ~{stats['estimated_tokens']} tokens")
            print(f"   Mode: {stats['mode']} (budget: {stats['budget_chars']} chars / {stats['budget_tokens']} tokens)")
        
        print("\n" + "=" * 60)
        print("CONTEXT:")
        print("=" * 60)
        print(result["context"])


if __name__ == "__main__":
    main()
