#!/usr/bin/env python3
"""
test_bridge.py — Verification tests for graphify_bridge.py

Test scenarios:
1. Bridge loads graph-from-wiki.json correctly
2. Bridge matches graph nodes to wiki slugs
3. Bridge verifies edges against actual wikilinks
4. Bridge adds backlinks to files
5. Bridge adds Dataview queries to files
6. Bridge reports correct statistics
"""

import json
import os
import re
import sys
import tempfile
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
from graphify_bridge import (
    load_graph,
    load_slugs,
    extract_wikilinks_from_file,
    verify_graph_edges_against_wikilinks,
    match_graph_to_slugs,
    find_wiki_file,
    add_backlinks_to_file,
    add_dataview_query,
    generate_report,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
GRAPH_JSON = PROJECT_ROOT.parent / "graphify-out" / "graph-from-wiki.json"
WIKI_DIR = PROJECT_ROOT / "wiki"


def test_load_graph():
    """Test that graph-from-wiki.json loads correctly."""
    print("Test 1: Load graph-from-wiki.json...")
    graph = load_graph()
    
    assert "nodes" in graph, "Graph must have 'nodes' key"
    assert "edges" in graph, "Graph must have 'edges' key"
    assert len(graph["nodes"]) > 0, "Graph must have at least 1 node"
    assert len(graph["edges"]) > 0, "Graph must have at least 1 edge"
    
    print(f"  ✅ Graph loaded: {len(graph['nodes'])} nodes, {len(graph['edges'])} edges")
    return graph


def test_load_slugs():
    """Test that wiki slugs are extracted correctly."""
    print("\nTest 2: Load wiki slugs...")
    slugs = load_slugs()
    
    assert len(slugs) > 0, "Must have at least 1 wiki slug"
    
    # Verify slugs are valid (no empty strings, no special chars)
    for slug in slugs:
        assert slug.strip(), f"Slug must not be empty: '{slug}'"
        assert not slug.startswith("."), f"Slug must not start with '.': '{slug}'"
    
    print(f"  ✅ Loaded {len(slugs)} wiki slugs")
    return slugs


def test_verify_graph_edges(graph, slugs):
    """Test that graph edges match actual wikilinks in wiki files."""
    print("\nTest 3: Verify graph edges against wiki wikilinks...")
    verification = verify_graph_edges_against_wikilinks(graph, slugs)
    
    # Verify a sample (full verification is expensive)
    assert verification["verified"] > 0, "Must have at least 1 verified edge"
    assert verification["missing_files"] == 0, f"Must have 0 missing files, got {verification['missing_files']}"
    
    print(f"  ✅ Verified: {verification['verified']}")
    print(f"  ✅ Mismatched: {verification['mismatched']}")
    print(f"  ✅ Missing files: {verification['missing_files']}")
    
    # Verify match rate is high
    total = verification["verified"] + verification["mismatched"] + verification["missing_files"]
    if total > 0:
        rate = verification["verified"] / total
        assert rate > 0.9, f"Verification rate must be > 90%, got {rate*100:.1f}%"
    
    return verification


def test_extract_wikilinks():
    """Test wikilink extraction from wiki files."""
    print("\nTest 4: Extract wikilinks from wiki files...")
    
    # Find a file with wikilinks
    test_file = None
    for root, dirs, files in os.walk(WIKI_DIR):
        for f in files:
            if f.endswith(".md"):
                path = os.path.join(root, f)
                content = open(path).read()
                if "[[" in content:
                    test_file = path
                    break
        if test_file:
            break
    
    assert test_file is not None, "Must find at least 1 file with wikilinks"
    links = extract_wikilinks_from_file(Path(test_file))
    
    assert len(links) > 0, f"File must have at least 1 wikilink: {test_file}"
    
    print(f"  ✅ Extracted {len(links)} wikilinks from {test_file}")
    return links


def test_match_graph_to_slugs(graph, slugs):
    """Test fuzzy matching of graph nodes to wiki slugs."""
    print("\nTest 5: Match graph nodes to wiki slugs...")
    matches = match_graph_to_slugs(graph, slugs)
    
    assert len(matches) > 0, "Must have at least 1 match"
    
    # Verify match scores are reasonable
    for match in matches:
        assert "graph_node" in match, "Match must have 'graph_node'"
        assert "matched_slug" in match, "Match must have 'matched_slug'"
        assert "score" in match, "Match must have 'score'"
        assert match["score"] >= 0.65, f"Match score must be >= 0.65, got {match['score']}"
    
    print(f"  ✅ Matched {len(matches)} graph nodes to wiki slugs")
    print(f"  ✅ Top match score: {max(m['score'] for m in matches)}")
    return matches


def test_find_wiki_file():
    """Test finding wiki files by slug in subdirectories."""
    print("\nTest 6: Find wiki files by slug...")
    
    # Test with known slug
    test_slug = "llm-wiki"
    path = find_wiki_file(test_slug)
    
    assert path is not None, f"Must find file for slug '{test_slug}'"
    assert os.path.exists(path), f"File must exist: {path}"
    
    print(f"  ✅ Found '{test_slug}' → {path}")
    
    # Test with non-existent slug
    path = find_wiki_file("non-existent-slug-12345")
    assert path is None, "Must return None for non-existent slug"
    
    print(f"  ✅ Returns None for non-existent slug")


def test_add_backlinks_to_file():
    """Test adding backlinks to wiki file frontmatter."""
    print("\nTest 7: Add backlinks to wiki file...")
    
    # Create temp file with frontmatter
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write("---\n")
        f.write("title: Test Page\n")
        f.write("type: concept\n")
        f.write("---\n")
        f.write("\n")
        f.write("This is test content.\n")
        f.write("\n")
        f.write("## See Also\n")
        f.write("- [[other-page]]\n")
        temp_path = f.name
    
    try:
        # Add backlink
        result = add_backlinks_to_file(temp_path, "test-node-id", "Test Node", dry_run=False)
        
        assert result is True, "Must return True when backlink added"
        
        # Verify backlink was added
        content = open(temp_path).read()
        assert "test-node-id" in content, "Backlink must be in file"
        assert "backlinks:" in content, "backlinks: section must exist"
        
        print(f"  ✅ Added backlink to {temp_path}")
        
        # Test idempotency (second add should return False)
        result = add_backlinks_to_file(temp_path, "test-node-id", "Test Node", dry_run=False)
        assert result is False, "Must return False when backlink already exists"
        
        print(f"  ✅ Idempotency check passed")
        
    finally:
        os.unlink(temp_path)


def test_add_dataview_query():
    """Test adding Dataview query to wiki file."""
    print("\nTest 8: Add Dataview query to wiki file...")
    
    # Create temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write("---\n")
        f.write("title: Test Page\n")
        f.write("---\n")
        f.write("\n")
        f.write("Test content.\n")
        temp_path = f.name
    
    try:
        # Add Dataview query
        result = add_dataview_query(temp_path, "test-node-id", "Test Node", dry_run=False)
        
        assert result is True, "Must return True when Dataview query added"
        
        # Verify Dataview query was added
        content = open(temp_path).read()
        assert "dataview" in content.lower(), "Dataview query must be in file"
        assert "backlinks" in content.lower(), "backlinks reference must be in query"
        
        print(f"  ✅ Added Dataview query to {temp_path}")
        
        # Test idempotency
        result = add_dataview_query(temp_path, "test-node-id", "Test Node", dry_run=False)
        assert result is False, "Must return False when Dataview query already exists"
        
        print(f"  ✅ Idempotency check passed")
        
    finally:
        os.unlink(temp_path)


def test_generate_report():
    """Test report generation."""
    print("\nTest 9: Generate bridge report...")
    
    sample_matches = [
        {"graph_node": {"label": "Test Page", "id": "test-page"}, "matched_slug": "test-page", "score": 1.0, "type": "concept"},
        {"graph_node": {"label": "Other Page", "id": "other-page"}, "matched_slug": "other-page", "score": 0.8, "type": "comparison"},
    ]
    
    sample_orphans = [
        {"label": "Orphan Node", "type": "unknown"},
    ]
    
    report = generate_report(
        matches=sample_matches,
        orphans=sample_orphans,
        new_links=5,
        missing_links=0,
        dataview_added=3,
        edge_verification={"verified": 100, "mismatched": 0, "missing_files": 0, "total_nodes": 200}
    )
    
    assert "total_graph_nodes" in report, "Report must have 'total_graph_nodes'"
    assert report["total_graph_nodes"] == 3, f"Must have 3 total nodes, got {report['total_graph_nodes']}"
    assert report["matched_nodes"] == 2, f"Must have 2 matched, got {report['matched_nodes']}"
    assert report["orphan_nodes"] == 1, f"Must have 1 orphan, got {report['orphan_nodes']}"
    assert report["match_rate"] == 66.7, f"Match rate must be 66.7%, got {report['match_rate']}"
    assert "matched_pairs" in report, "Report must have 'matched_pairs'"
    assert "orphan_suggestions" in report, "Report must have 'orphan_suggestions'"
    
    print(f"  ✅ Report generated: {report['total_graph_nodes']} nodes, {report['match_rate']}% match rate")


def main():
    print("=" * 60)
    print("BRIDGE VERIFICATION TESTS")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    try:
        graph = test_load_graph()
        passed += 1
    except Exception as e:
        print(f"  ❌ FAILED: {e}")
        failed += 1
        return False
    
    try:
        slugs = test_load_slugs()
        passed += 1
    except Exception as e:
        print(f"  ❌ FAILED: {e}")
        failed += 1
    
    try:
        test_verify_graph_edges(graph, slugs)
        passed += 1
    except Exception as e:
        print(f"  ❌ FAILED: {e}")
        failed += 1
    
    try:
        test_extract_wikilinks()
        passed += 1
    except Exception as e:
        print(f"  ❌ FAILED: {e}")
        failed += 1
    
    try:
        test_match_graph_to_slugs(graph, slugs)
        passed += 1
    except Exception as e:
        print(f"  ❌ FAILED: {e}")
        failed += 1
    
    try:
        test_find_wiki_file()
        passed += 1
    except Exception as e:
        print(f"  ❌ FAILED: {e}")
        failed += 1
    
    try:
        test_add_backlinks_to_file()
        passed += 1
    except Exception as e:
        print(f"  ❌ FAILED: {e}")
        failed += 1
    
    try:
        test_add_dataview_query()
        passed += 1
    except Exception as e:
        print(f"  ❌ FAILED: {e}")
        failed += 1
    
    try:
        test_generate_report()
        passed += 1
    except Exception as e:
        print(f"  ❌ FAILED: {e}")
        failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
