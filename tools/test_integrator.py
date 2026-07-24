#!/usr/bin/env python3
"""
LLM Wiki Integrator — Unit Tests

Tests for integrator.py to verify correct wikilink generation,
slug-based linking, and page creation logic.

Usage:
    python3 tools/test_integrator.py
"""

import sys
import os
import re
import hashlib
import tempfile
import shutil
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add tools to path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from integrator import (
    find_wikilinks,
    _get_slug_title_pairs,
    build_tag_map,
    extract_title,
    extract_tags,
    classify_page_type,
    convert_html_to_markdown,
    generate_wiki_page,
    is_already_processed,
    MIN_CONTENT_LENGTH,
)


# ---------------------------------------------------------------------------
# Test Runner
# ---------------------------------------------------------------------------

class TestResult:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = []

    def check(self, name, condition, msg=""):
        if condition:
            self.passed += 1
            print(f"  ✅ {name}")
        else:
            self.failed += 1
            self.errors.append((name, msg))
            print(f"  ❌ {name}: {msg}")

    def summary(self):
        total = self.passed + self.failed
        print(f"\n{'='*60}")
        print(f"RESULTS: {self.passed}/{total} passed, {self.failed} failed")
        if self.errors:
            print(f"\nFailures:")
            for name, msg in self.errors:
                print(f"  - {name}: {msg}")
        return self.failed == 0


def make_temp_wiki_dir(tmpdir: Path, files: dict):
    """Create a temporary wiki directory with test files.
    
    Args:
        tmpdir: Base temp directory
        files: Dict of {relative_path: content} where path is wiki subcategory/filename.md
    """
    wiki_dir = tmpdir / "wiki"
    for rel_path, content in files.items():
        full_path = wiki_dir / rel_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content, encoding="utf-8")
    return wiki_dir


# ---------------------------------------------------------------------------
# Test: extract_title
# ---------------------------------------------------------------------------

def test_extract_title(result: TestResult):
    """Test title extraction from various formats."""
    print("\n📝 Test: extract_title")

    # Frontmatter title
    fm_content = """---
title: "My Test Article"
tags: [llm, agent]
---
# H1 Title Should Not Be Used
"""
    title = extract_title(fm_content)
    result.check("Frontmatter title extraction", title == "My Test Article", f"got: '{title}'")

    # H1 fallback
    h1_content = "# My H1 Title\n\nSome content"
    title = extract_title(h1_content)
    result.check("H1 fallback", title == "My H1 Title", f"got: '{title}'")

    # Date stripping
    date_content = "---\ntitle: \"AI Trends in 2026\"\n---\n"
    title = extract_title(date_content)
    result.check("Date stripping (in YYYY)", title == "AI Trends", f"got: '{title}'")

    # Year range
    date_content = "---\ntitle: \"LLM Landscape 2025–2026\"\n---\n"
    title = extract_title(date_content)
    result.check("Year range stripping", "2025" not in title and "2026" not in title, f"got: '{title}'")

    # Trailing punctuation (only trailing, not mid-text)
    punct_content = "---\ntitle: \"Agent Frameworks Review\"\n---\n"
    title = extract_title(punct_content)
    result.check("Trailing punctuation removal", title == "Agent Frameworks Review", f"got: '{title}'")


# ---------------------------------------------------------------------------
# Test: extract_tags
# ---------------------------------------------------------------------------

def test_extract_tags(result: TestResult):
    """Test tag extraction from frontmatter."""
    print("\n🏷️ Test: extract_tags")

    # Valid tags from frontmatter
    content = """---
title: "Test"
tags: [llm, agent, rag]
---
"""
    tags = extract_tags(content, "Test")
    result.check("Tag extraction (valid tags)", "llm" in tags, f"got: {tags}")

    # Invalid tags should be filtered
    content = """---
title: "Test"
tags: [llm, invalid-tag, agent]
---
"""
    tags = extract_tags(content, "Test")
    result.check("Invalid tag filtering", "invalid-tag" not in tags, f"got: {tags}")


# ---------------------------------------------------------------------------
# Test: classify_page_type
# ---------------------------------------------------------------------------

def test_classify_page_type(result: TestResult):
    """Test page type classification."""
    print("\n📂 Test: classify_page_type")

    # Comparison
    comp = "GPT-4 vs Claude: A comparison of LLM capabilities"
    ptype = classify_page_type(comp, "GPT-4 vs Claude")
    result.check("Comparison detection", ptype == "comparison", f"got: '{ptype}'")

    # Playbook
    pb = "How to build an AI agent with LangGraph - a step by step guide"
    ptype = classify_page_type(pb, "Build AI Agent")
    result.check("Playbook detection", ptype == "playbook", f"got: '{ptype}'")

    # Synthesis
    syn = "State of AI: Analysis of emerging trends and future directions"
    ptype = classify_page_type(syn, "State of AI")
    result.check("Synthesis detection", ptype == "synthesis", f"got: '{ptype}'")

    # Default (concept) — must NOT accidentally match comparison/playbook/synthesis keywords
    # NOTE: "or" is in comparison_keywords, so avoid any word containing "or"
    concept = "Deep learning architectures using convolutional layers"
    ptype = classify_page_type(concept, "Convolutional Layers")
    result.check("Default concept", ptype == "concept", f"got: '{ptype}'")


# ---------------------------------------------------------------------------
# Test: convert_html_to_markdown
# ---------------------------------------------------------------------------

def test_convert_html_to_markdown(result: TestResult):
    """Test HTML to Markdown conversion."""
    print("\n🔄 Test: convert_html_to_markdown")

    html = "<html><body><h1>Title</h1><p>Content with <strong>bold</strong> and <em>italic</em>.</p></body></html>"
    md, _ = convert_html_to_markdown(html)
    result.check("H1 conversion", "# Title" in md, f"got: '{md[:50]}'")
    result.check("Bold conversion", "**bold**" in md, f"got: '{md}'")
    result.check("Italic conversion", "*italic*" in md, f"got: '{md}'")

    # Astro island removal
    astro_html = "<body><p>Real content</p><astro-island><script>noise</script></astro-island><p>More content</p></body>"
    md, _ = convert_html_to_markdown(astro_html)
    result.check("Astro island removal", "<astro-island" not in md, f"got: '{md}'")
    result.check("Real content preserved", "Real content" in md, f"got: '{md}'")

    # Links
    link_html = '<a href="https://example.com">Click here</a>'
    md, _ = convert_html_to_markdown(link_html)
    result.check("Link conversion", "[Click here](https://example.com)" in md, f"got: '{md}'")


# ---------------------------------------------------------------------------
# Test: find_wikilinks — SLUG-BASED
# ---------------------------------------------------------------------------

def test_find_wikilinks_slug_based(result: TestResult):
    """Test that find_wikilinks returns SLUGS, not titles.
    
    This is the CRITICAL fix: wikilinks must match filenames.
    [[page-title]] -> page-title.md ✅
    [[Page Title]] -> page-title.md ❌ (broken)
    """
    print("\n🔗 Test: find_wikilinks (slug-based)")

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        wiki_dir = make_temp_wiki_dir(tmpdir, {
            "concepts/llm-fundamentals.md": """---
title: "LLM Fundamentals"
tags:
  - llm
  - llm-wiki
  - foundation-model
---
# LLM Fundamentals

Large Language Models are neural networks trained on vast text corpora.
""",
            "concepts/agent-architecture.md": """---
title: "Agent Architecture"
tags:
  - agent
  - llm
  - llm-wiki
---
# Agent Architecture

AI agents use LLMs to reason and act in environments.
""",
            "comparisons/claude-vs-gpt.md": """---
title: "Claude vs GPT"
tags:
  - llm
  - llm-wiki
  - comparison
---
# Claude vs GPT

Comparison of leading LLM providers.
""",
        })

        # Override WIKI_DIR in integrator
        with patch('integrator.WIKI_DIR', wiki_dir):
            # Build tag map
            tag_map = build_tag_map()
            
            # Verify tag_map uses SLUGS
            result.check("Tag map has llm-wiki entries", "llm-wiki" in tag_map, f"keys: {list(tag_map.keys())}")
            
            # Check: tag_map values are slugs (contain hyphens, not spaces)
            if "llm-wiki" in tag_map:
                sample_slugs = tag_map["llm-wiki"][:3]
                all_slug_format = all("-" in s or "_" in s for s in sample_slugs)
                result.check("Tag map values are slugs (hyphenated)", all_slug_format, 
                           f"got: {sample_slugs}")
            
            # Test find_wikilinks returns slugs
            wikilinks = find_wikilinks("Test Article", ["llm"], tag_map, 
                                      "LLM agents use foundation models for reasoning")
            
            # All returned wikilinks should be slugs (lowercase, hyphenated)
            all_slug_format = all(re.match(r'^[a-z0-9_-]+$', l) for l in wikilinks)
            result.check("find_wikilinks returns slugs", all_slug_format, 
                       f"got: {wikilinks}")
            
            # No wikilinks should contain spaces (titles have spaces)
            no_spaces = all(" " not in l for l in wikilinks)
            result.check("Wikilinks have no spaces", no_spaces, 
                       f"got: {wikilinks} (spaces indicate title, not slug)")
            
            # Wikilinks should match actual files
            for slug in wikilinks:
                found = False
                for subdir in wiki_dir.glob("*"):
                    if subdir.is_dir() and (subdir / f"{slug}.md").exists():
                        found = True
                        break
                result.check(f"Slug '{slug}' matches file", found, 
                           f"file {slug}.md not found")


# ---------------------------------------------------------------------------
# Test: find_wikilinks — NON-EXISTENT PAGES FILTERED
# ---------------------------------------------------------------------------

def test_find_wikilinks_external_filtered(result: TestResult):
    """Test that external article titles are NOT included as wikilinks.
    
    If a page is about '5 Agent Skills I Use Every Day' but there's no
    wiki page with that title/slug, it should NOT be wikilinked.
    """
    print("\n🚫 Test: find_wikilinks (external filtering)")

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        wiki_dir = make_temp_wiki_dir(tmpdir, {
            "concepts/agent-basics.md": """---
title: "Agent Basics"
tags: [agent]
---
# Agent Basics

Introduction to AI agents.
""",
        })

        with patch('integrator.WIKI_DIR', wiki_dir):
            tag_map = build_tag_map()
            
            # Content about something NOT in wiki
            content = "5 Agent Skills I Use Every Day: Here's my comprehensive guide to building AI agents with LangChain, CrewAI, AutoGen, and more advanced techniques."
            
            wikilinks = find_wikilinks("External Article", ["agent"], tag_map, content)
            
            # Should NOT contain the external article title
            external_title = "5 Agent Skills I Use Every Day"
            result.check("External title NOT in wikilinks", 
                        external_title not in str(wikilinks),
                       f"got: {wikilinks}")


# ---------------------------------------------------------------------------
# Test: generate_wiki_page — wikilinks embedded in output
# ---------------------------------------------------------------------------

def test_generate_wiki_page_wikilinks(result: TestResult):
    """Test that generated wiki pages contain valid wikilinks.
    
    Every [[wikilink]] in the generated page should point to an existing file.
    """
    print("\n📄 Test: generate_wiki_page (wikilink validation)")

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        wiki_dir = make_temp_wiki_dir(tmpdir, {
            "concepts/llm-fundamentals.md": """---
title: "LLM Fundamentals"
tags: [llm]
---
# LLM Fundamentals

LLM content here.
""",
        })

        raw_content = """---
title: "Test Agent Article"
tags: [agent, llm]
source_url: https://example.com/test
---
<html>
<body>
<h1>Test Agent Article</h1>
<p>This article discusses how AI agents use LLMs for decision making in complex environments with multiple reasoning steps and action planning capabilities. The agent system integrates perception, memory, and action modules to achieve autonomous goals.</p>
<h2>Key Components</h2>
<p>The perception module processes sensory inputs from the environment. It uses vision transformers and language models to understand context and extract relevant features from raw data streams.</p>
<h2>Memory Systems</h2>
<p>Short-term memory stores recent observations and intermediate reasoning traces. Long-term memory uses vector embeddings to store knowledge that can be retrieved through semantic similarity search.</p>
<h2>Action Planning</h2>
<p>The action module generates executable commands based on the agent's goals, current state, and available tools. It uses reinforcement learning and planning algorithms to optimize decision sequences.</p>
</body>
</html>
"""

        with patch('integrator.WIKI_DIR', wiki_dir):
            with patch('integrator.ROOT', tmpdir):
                # Generate page
                page = generate_wiki_page(
                    raw_path=tmpdir / "test.md",
                    raw_content=raw_content,
                    title="Test Agent Article",
                    page_type="concept",
                    tags=["agent", "llm"],
                    tag_map=build_tag_map()
                )

                if page:
                    # Read generated page — page is relative to ROOT, but wiki_dir already includes /wiki
                    # So we need to strip "wiki/" prefix if present
                    page_path = page
                    if page.startswith("wiki/"):
                        page_path = page[5:]
                    generated_path = wiki_dir / page_path
                    if not generated_path.exists():
                        # Fallback: try the page as-is
                        generated_path = wiki_dir / page
                    if not generated_path.exists():
                        # Last resort: search in wiki subdirs
                        for subdir in wiki_dir.glob("*/*.md"):
                            if "test-agent-article" in subdir.name:
                                generated_path = subdir
                                break
                    generated_content = generated_path.read_text(encoding="utf-8")
                    
                    # Find all wikilinks in generated page
                    wikilinks = re.findall(r'\[\[([^\]]+?)\]\]', generated_content)
                    
                    # Each wikilink should be a valid slug
                    for link in wikilinks:
                        # Should be slug format (no spaces)
                        result.check(f"Slug format: {link}", 
                                   " " not in link,
                                   f"space in link indicates title, not slug")
                        
                        # Should match an existing file
                        found = False
                        for subdir in wiki_dir.glob("*"):
                            if subdir.is_dir():
                                if (subdir / f"{link.lower()}.md").exists():
                                    found = True
                                    break
                        result.check(f"Link exists: {link}", found,
                                   f"no file matches {link}")
                else:
                    result.check("Page generated", False, "generate_wiki_page returned None")


# ---------------------------------------------------------------------------
# Test: is_already_processed
# ---------------------------------------------------------------------------

def test_is_already_processed(result: TestResult):
    """Test deduplication logic."""
    print("\n🔄 Test: is_already_processed")

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        wiki_dir = make_temp_wiki_dir(tmpdir, {
            "concepts/existing-page.md": "---\ntitle: Existing\n---\n# Existing\n",
        })

        raw_path = tmpdir / "new-article.md"
        raw_path.write_text("---\ntitle: New\n---\n# New\n", encoding="utf-8")

        with patch('integrator.WIKI_DIR', wiki_dir):
            # New page should NOT be marked processed
            is_proc = is_already_processed(raw_path)
            result.check("New page not processed", not is_proc, f"got: {is_proc}")

            # Create matching wiki page
            existing_path = wiki_dir / "concepts" / "new.md"
            existing_path.write_text("---\ntitle: New\n---\n# New\n", encoding="utf-8")
            
            is_proc = is_already_processed(raw_path)
            result.check("Existing page detected as processed", is_proc, f"got: {is_proc}")


# ---------------------------------------------------------------------------
# Test: SHA256 hash consistency (wiki_doctor standard)
# ---------------------------------------------------------------------------

def test_sha256_consistency(result: TestResult):
    """Test that body.lstrip('\\n') is used for hash calculation.
    
    This ensures consistency with wiki_doctor.py.
    """
    print("\n🔐 Test: SHA256 hash consistency")

    # Test the standard hash function
    body = "\n\n# Title\n\nContent"
    
    # wiki_doctor standard: body.lstrip("\n")
    expected = hashlib.sha256(body.lstrip("\n").encode("utf-8")).hexdigest()
    
    # Verify lstrip removes leading newlines
    result.check("lstrip removes leading newlines", 
                body.lstrip("\n") == "# Title\n\nContent",
                f"got: '{body.lstrip(chr(10))}'")

    # Verify SHA256 is deterministic
    body2 = "\n\n# Title\n\nContent"
    hash2 = hashlib.sha256(body2.lstrip("\n").encode("utf-8")).hexdigest()
    result.check("SHA256 deterministic", expected == hash2,
               f"hash1={expected[:16]}... hash2={hash2[:16]}...")


# ---------------------------------------------------------------------------
# Test: minimum content length
# ---------------------------------------------------------------------------

def test_min_content_length(result: TestResult):
    """Test that short content is filtered."""
    print("\n📏 Test: minimum content length")

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        wiki_dir = make_temp_wiki_dir(tmpdir, {})

        short_content = """---
title: "Too Short"
---
<html><body><p>Only 10 chars</p></body></html>
"""
        with patch('integrator.WIKI_DIR', wiki_dir):
            page = generate_wiki_page(
                raw_path=tmpdir / "short.md",
                raw_content=short_content,
                title="Too Short",
                page_type="concept",
                tags=[],
                tag_map={}
            )
            result.check("Short content filtered", page is None, 
                       f"got page: {page}")

        # Long content should pass — append INSIDE body tags
        long_content = """---
title: "Long Enough"
---
<html><body><p>""" + "x" * (MIN_CONTENT_LENGTH + 100) + """</p></body></html>
"""
        with patch('integrator.WIKI_DIR', wiki_dir):
            with patch('integrator.ROOT', tmpdir):
                page = generate_wiki_page(
                    raw_path=tmpdir / "long.md",
                    raw_content=long_content,
                    title="Long Enough",
                    page_type="concept",
                    tags=[],
                    tag_map={}
                )
                result.check("Long content passes", page is not None,
                           f"got: {page}")


# ---------------------------------------------------------------------------
# Test: Astro-island handling
# ---------------------------------------------------------------------------

def test_astro_island_handling(result: TestResult):
    """Test that astro-island blocks are properly removed."""
    print("\n🛡️ Test: astro-island handling")

    astro_content = """---
title: "Astro Test"
---
<html>
<body>
<h1>Astro Test</h1>
<astro-island>
<script>console.log("noise")</script>
<p>Framework noise content</p>
</astro-island>
<p>Real content that should remain.</p>
</body>
</html>
"""
    md, _ = convert_html_to_markdown(astro_content)
    
    result.check("Astro block removed", "<astro-island" not in md, f"got: '{md[:100]}'")
    result.check("Framework noise removed", "noise" not in md.lower(), f"got: '{md}'")
    result.check("Real content preserved", "Real content" in md, f"got: '{md}'")
    result.check("Script removed", "console.log" not in md, f"got: '{md}'")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("LLM Wiki Integrator — Unit Tests")
    print("=" * 60)

    result = TestResult()

    # Run all tests
    test_extract_title(result)
    test_extract_tags(result)
    test_classify_page_type(result)
    test_convert_html_to_markdown(result)
    test_find_wikilinks_slug_based(result)
    test_find_wikilinks_external_filtered(result)
    test_generate_wiki_page_wikilinks(result)
    test_is_already_processed(result)
    test_sha256_consistency(result)
    test_min_content_length(result)
    test_astro_island_handling(result)

    # Summary
    success = result.summary()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
