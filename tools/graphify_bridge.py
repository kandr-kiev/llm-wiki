#!/usr/bin/env python3
"""
Graphify Bridge — connects graphify-out/graph.json with wiki/ directory.

Functions:
- Orphan detection (graph nodes not in wiki, wiki pages not in graph)
- Fuzzy cross-link suggestions
- Graph validation against SCHEMA.md
- Bridge report generation

Usage:
    python3 tools/graphify_bridge.py --mode full
    python3 tools/graphify_bridge.py --mode orphans
    python3 tools/graphify_bridge.py --mode suggestions
    python3 tools/graphify_bridge.py --mode validate
"""

import argparse
import difflib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
WIKI_ROOT = SCRIPT_DIR.parent  # /workspace/llm-wiki
GRAPH_FILE = WIKI_ROOT / "graphify-out" / "graph.json"
WIKI_DIR = WIKI_ROOT / "wiki"
SCHEMA_FILE = WIKI_ROOT / "SCHEMA.md"
OUTPUT_DIR = WIKI_ROOT / "graphify-out"

# Fuzzy matching config
FUZZY_THRESHOLD = 0.75
STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
    "being", "have", "has", "had", "do", "does", "did", "will", "would",
    "could", "should", "may", "might", "can", "shall", "it", "its", "this",
    "that", "these", "those", "i", "you", "he", "she", "we", "they", "me",
    "him", "her", "us", "them", "my", "your", "his", "our", "their",
    "not", "no", "nor", "so", "if", "then", "than", "too", "very",
    "just", "about", "above", "after", "again", "all", "also", "am",
    "any", "as", "because", "before", "between", "both", "each", "few",
    "more", "most", "other", "out", "over", "own", "same", "some",
    "such", "up", "what", "when", "where", "which", "while", "who",
    "whom", "why", "how", "into", "through", "during", "only", "down",
    "even", "get", "got", "make", "made", "like", "well", "back",
    "new", "now", "way", "use", "used", "using", "one", "two",
}


def normalize_text(text: str) -> str:
    """Normalize text for fuzzy comparison."""
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r"[_\-\.]", " ", text)
    words = [w for w in text.split() if w not in STOP_WORDS and w.isalnum()]
    return " ".join(words)


def fuzzy_match(query: str, candidates: list[str], threshold: float = FUZZY_THRESHOLD) -> list[tuple[str, float]]:
    """Fuzzy match query against candidates. Returns list of (candidate, score)."""
    normalized_query = normalize_text(query)
    if not normalized_query:
        return []
    
    results = []
    for candidate in candidates:
        normalized_candidate = normalize_text(candidate)
        if not normalized_candidate:
            continue
        ratio = difflib.SequenceMatcher(None, normalized_query, normalized_candidate).ratio()
        if ratio >= threshold:
            results.append((candidate, ratio))
    
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:3]  # Top 3 matches


def load_graph() -> dict | None:
    """Load graph.json. Returns None if file doesn't exist."""
    if not GRAPH_FILE.exists():
        return None
    try:
        with open(GRAPH_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"ERROR: Failed to load {GRAPH_FILE}: {e}", file=sys.stderr)
        return None


def get_wiki_slugs() -> dict[str, str]:
    """Get all wiki slugs -> title mappings."""
    slugs = {}
    if not WIKI_DIR.exists():
        return slugs
    
    for md_file in WIKI_DIR.rglob("*.md"):
        slug = md_file.stem
        # Try to read title from frontmatter
        title = slug.replace("-", " ").title()
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read(1000)  # Read first 1KB for frontmatter
                if content.startswith("---"):
                    lines = content.split("\n")
                    for i, line in enumerate(lines[1:], 1):
                        if line.startswith("title:"):
                            title = line.split(":", 1)[1].strip()
                            break
        except IOError:
            pass
        slugs[slug] = title
    
    return slugs


def get_graph_node_ids(graph: dict) -> set[str]:
    """Extract all node IDs from graph.json."""
    nodes = graph.get("nodes", [])
    return {node.get("id", "") for node in nodes if node.get("id")}


def detect_orphans(graph: dict, wiki_slugs: dict[str, str]) -> tuple[set[str], set[str]]:
    """
    Detect orphans:
    - Graph nodes not found in wiki
    - Wiki pages not found in graph
    Returns: (graph_orphans, wiki_orphans)
    """
    graph_ids = get_graph_node_ids(graph)
    wiki_slug_set = set(wiki_slugs.keys())
    
    # Normalize for comparison
    normalized_graph = {normalize_text(nid): nid for nid in graph_ids}
    normalized_wiki = {normalize_text(slug): slug for slug in wiki_slug_set}
    
    graph_orphans = set()
    wiki_orphans = set()
    
    for nid in graph_ids:
        norm = normalize_text(nid)
        if not fuzzy_match(nid, list(wiki_slug_set)):
            graph_orphans.add(nid)
    
    for slug in wiki_slug_set:
        norm = normalize_text(slug)
        if not fuzzy_match(slug, list(graph_ids)):
            wiki_orphans.add(slug)
    
    return graph_orphans, wiki_orphans


def suggest_crosslinks(graph: dict, wiki_slugs: dict[str, str], max_suggestions: int = 50) -> list[dict]:
    """
    Suggest cross-links between graph nodes and wiki pages based on fuzzy matching.
    Returns list of {node, wiki_slug, score, reason}.
    """
    graph_ids = list(get_graph_node_ids(graph))
    suggestions = []
    
    for slug, title in wiki_slugs.items():
        # Skip already-matched pages (approximate check)
        if fuzzy_match(slug, graph_ids, threshold=0.85):
            continue
        
        # Find best graph match
        matches = fuzzy_match(slug, graph_ids, threshold=0.65)
        if matches:
            best_match, score = matches[0]
            suggestions.append({
                "wiki_slug": slug,
                "wiki_title": title,
                "graph_node": best_match,
                "score": round(score, 3),
                "reason": f"Fuzzy match score {score:.2f}"
            })
    
    suggestions.sort(key=lambda x: x["score"], reverse=True)
    return suggestions[:max_suggestions]


def validate_graph_against_schema(graph: dict) -> list[str]:
    """Validate graph.json nodes against SCHEMA.md tag taxonomy."""
    errors = []
    
    # Load approved tags from SCHEMA.md
    approved_tags = set()
    if SCHEMA_FILE.exists():
        with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            # Look for tag taxonomy section
            in_taxonomy = False
            for line in content.split("\n"):
                if "## Tag Taxonomy" in line or "### Tag Taxonomy" in line:
                    in_taxonomy = True
                    continue
                if in_taxonomy and line.startswith("## "):
                    break
                if in_taxonomy and line.strip().startswith("- "):
                    tag = line.strip().lstrip("- ").split(" ")[0].strip()
                    if tag:
                        approved_tags.add(tag.lower())
    
    # Check node tags
    nodes = graph.get("nodes", [])
    for node in nodes:
        tags = node.get("tags", [])
        for tag in tags:
            if approved_tags and tag.lower() not in approved_tags:
                errors.append(f"Node '{node.get('id', 'unknown')}' has unapproved tag: {tag}")
    
    return errors


def generate_bridge_report(graph: dict, wiki_slugs: dict[str, str],
                           graph_orphans: set[str], wiki_orphans: set[str],
                           suggestions: list[dict], validation_errors: list[str]) -> str:
    """Generate markdown bridge report."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    
    lines = [
        f"# Graphify Bridge Report",
        f"",
        f"**Generated:** {now}",
        f"**Graph file:** {GRAPH_FILE}",
        f"**Wiki root:** {WIKI_DIR}",
        f"",
        f"---",
        f"",
        f"## Summary",
        f"",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Graph nodes | {len(get_graph_node_ids(graph))} |",
        f"| Wiki pages | {len(wiki_slugs)} |",
        f"| Graph orphans | {len(graph_orphans)} |",
        f"| Wiki orphans | {len(wiki_orphans)} |",
        f"| Cross-link suggestions | {len(suggestions)} |",
        f"| Validation errors | {len(validation_errors)} |",
        f"",
        f"---",
        f"",
    ]
    
    # Graph orphans
    if graph_orphans:
        lines.extend([
            f"## Graph Orphans ({len(graph_orphans)} nodes)",
            f"",
            f"Nodes in graph.json that don't match any wiki page:",
            f"",
        ])
        for orphan in sorted(graph_orphans)[:50]:
            lines.append(f"- `{orphan}`")
        if len(graph_orphans) > 50:
            lines.append(f"\n*... and {len(graph_orphans) - 50} more*")
        lines.append("")
    
    # Wiki orphans
    if wiki_orphans:
        lines.extend([
            f"## Wiki Orphans ({len(wiki_orphans)} pages)",
            f"",
            f"Wiki pages that don't match any graph node:",
            f"",
        ])
        for orphan in sorted(wiki_orphans)[:50]:
            title = wiki_slugs.get(orphan, orphan.replace("-", " ").title())
            lines.append(f"- `{orphan}` — {title}")
        if len(wiki_orphans) > 50:
            lines.append(f"\n*... and {len(wiki_orphans) - 50} more*")
        lines.append("")
    
    # Cross-link suggestions
    if suggestions:
        lines.extend([
            f"## Cross-Link Suggestions ({len(suggestions)} suggestions)",
            f"",
            f"Wiki pages that could be linked to graph nodes:",
            f"",
            f"| Wiki Slug | Score | Graph Node |",
            f"|-----------|-------|------------|",
        ])
        for s in suggestions[:30]:
            lines.append(f"| `{s['wiki_slug']}` | {s['score']:.2f} | `{s['graph_node']}` |")
        if len(suggestions) > 30:
            lines.append(f"\n*... and {len(suggestions) - 30} more*")
        lines.append("")
    
    # Validation errors
    if validation_errors:
        lines.extend([
            f"## Validation Errors ({len(validation_errors)} errors)",
            f"",
        ])
        for error in validation_errors[:20]:
            lines.append(f"- {error}")
        if len(validation_errors) > 20:
            lines.append(f"\n*... and {len(validation_errors) - 20} more*")
        lines.append("")
    
    # Recommendations
    lines.extend([
        f"---",
        f"",
        f"## Recommendations",
        f"",
    ])
    
    if graph_orphans:
        lines.append(f"- **Review graph orphans**: These nodes may be stale or from sources not yet ingested into wiki/")
    if wiki_orphans:
        lines.append(f"- **Review wiki orphans**: These pages could benefit from graph edges or should be added to graph")
    if suggestions:
        lines.append(f"- **Apply cross-links**: {min(len(suggestions), 10)} high-confidence suggestions available")
    if validation_errors:
        lines.append(f"- **Fix tags**: {len(validation_errors)} nodes have unapproved tags")
    
    if not any([graph_orphans, wiki_orphans, suggestions, validation_errors]):
        lines.append("- **All clear**: No issues detected!")
    
    lines.append("")
    return "\n".join(lines)


def save_text_file(path: Path, content: str):
    """Save content to file, creating parent dirs."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def mode_full():
    """Run full analysis."""
    print(f"[bridge] Loading graph from {GRAPH_FILE}...")
    graph = load_graph()
    if not graph:
        print("[bridge] ERROR: graph.json not found. Run 'graphify extract' first.", file=sys.stderr)
        sys.exit(1)
    
    print(f"[bridge] Loading wiki slugs...")
    wiki_slugs = get_wiki_slugs()
    
    print(f"[bridge] Detecting orphans...")
    graph_orphans, wiki_orphans = detect_orphans(graph, wiki_slugs)
    
    print(f"[bridge] Suggesting cross-links...")
    suggestions = suggest_crosslinks(graph, wiki_slugs)
    
    print(f"[bridge] Validating against SCHEMA.md...")
    validation_errors = validate_graph_against_schema(graph)
    
    print(f"[bridge] Generating report...")
    report = generate_bridge_report(graph, wiki_slugs, graph_orphans, wiki_orphans, suggestions, validation_errors)
    
    # Save files
    save_text_file(OUTPUT_DIR / "bridge_report.md", report)
    save_text_file(OUTPUT_DIR / "orphans_graph.txt", "\n".join(sorted(graph_orphans)) + "\n")
    save_text_file(OUTPUT_DIR / "orphans_wiki.txt", "\n".join(sorted(wiki_orphans)) + "\n")
    
    suggestions_data = json.dumps(suggestions, indent=2, ensure_ascii=False)
    save_text_file(OUTPUT_DIR / "orphans_suggestions.json", suggestions_data)
    
    # Print summary
    print(f"\n[bridge] === Summary ===")
    print(f"[bridge] Graph nodes: {len(get_graph_node_ids(graph))}")
    print(f"[bridge] Wiki pages: {len(wiki_slugs)}")
    print(f"[bridge] Graph orphans: {len(graph_orphans)}")
    print(f"[bridge] Wiki orphans: {len(wiki_orphans)}")
    print(f"[bridge] Cross-link suggestions: {len(suggestions)}")
    print(f"[bridge] Validation errors: {len(validation_errors)}")
    print(f"\n[bridge] Files saved to {OUTPUT_DIR}/")
    print(f"[bridge]   - bridge_report.md")
    print(f"[bridge]   - orphans_graph.txt")
    print(f"[bridge]   - orphans_wiki.txt")
    print(f"[bridge]   - orphans_suggestions.json")


def mode_orphans():
    """Run orphan detection only."""
    print(f"[bridge] Loading graph from {GRAPH_FILE}...")
    graph = load_graph()
    if not graph:
        print("[bridge] ERROR: graph.json not found.", file=sys.stderr)
        sys.exit(1)
    
    wiki_slugs = get_wiki_slugs()
    graph_orphans, wiki_orphans = detect_orphans(graph, wiki_slugs)
    
    save_text_file(OUTPUT_DIR / "orphans_graph.txt", "\n".join(sorted(graph_orphans)) + "\n")
    save_text_file(OUTPUT_DIR / "orphans_wiki.txt", "\n".join(sorted(wiki_orphans)) + "\n")
    
    print(f"[bridge] Graph orphans: {len(graph_orphans)}")
    print(f"[bridge] Wiki orphans: {len(wiki_orphans)}")


def mode_suggestions():
    """Run cross-link suggestions only."""
    print(f"[bridge] Loading graph from {GRAPH_FILE}...")
    graph = load_graph()
    if not graph:
        print("[bridge] ERROR: graph.json not found.", file=sys.stderr)
        sys.exit(1)
    
    wiki_slugs = get_wiki_slugs()
    suggestions = suggest_crosslinks(graph, wiki_slugs)
    
    suggestions_data = json.dumps(suggestions, indent=2, ensure_ascii=False)
    save_text_file(OUTPUT_DIR / "orphans_suggestions.json", suggestions_data)
    
    print(f"[bridge] Suggestions: {len(suggestions)}")
    for s in suggestions[:10]:
        print(f"  [{s['score']:.2f}] {s['wiki_slug']} -> {s['graph_node']}")


def mode_validate():
    """Validate graph against SCHEMA.md only."""
    print(f"[bridge] Loading graph from {GRAPH_FILE}...")
    graph = load_graph()
    if not graph:
        print("[bridge] ERROR: graph.json not found.", file=sys.stderr)
        sys.exit(1)
    
    errors = validate_graph_against_schema(graph)
    
    if errors:
        print(f"[bridge] Validation errors: {len(errors)}")
        for e in errors[:20]:
            print(f"  - {e}")
    else:
        print(f"[bridge] Validation: PASSED (no errors)")


def main():
    parser = argparse.ArgumentParser(description="Graphify Bridge — connect graph.json with wiki/")
    parser.add_argument("--mode", choices=["full", "orphans", "suggestions", "validate"],
                        default="full", help="Operation mode (default: full)")
    args = parser.parse_args()
    
    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Run selected mode
    match args.mode:
        case "full":
            mode_full()
        case "orphans":
            mode_orphans()
        case "suggestions":
            mode_suggestions()
        case "validate":
            mode_validate()


if __name__ == "__main__":
    main()
