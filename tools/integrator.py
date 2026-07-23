#!/usr/bin/env python3
"""
LLM Wiki Integrator — scans raw articles and generates structured wiki pages.

Usage:
    python3 tools/integrator.py [--dry-run] [--limit N]

Environment:
    LLM_WIKI_ROOT  — optional override for the wiki root directory
"""

import re
import html
import sys
import hashlib
import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ROOT = Path(
    __import__("os").environ.get(
        "LLM_WIKI_ROOT", str(Path(__file__).resolve().parent.parent)
    )
)
RAW_DIR = ROOT / "raw" / "articles"
WIKI_DIR = ROOT / "wiki"
INDEX_FILE = ROOT / "wiki" / "index.md"
PROCESSED_DB = ROOT / ".processed" / "processed_hashes.db"
RAW_PROCESSED_DIR = ROOT / ".processed"  # Track processed raw files

MIN_CONTENT_LENGTH = 500  # minimum clean content length


# ---------------------------------------------------------------------------
# Processed file tracking
# ---------------------------------------------------------------------------


def is_already_processed(raw_path: Path) -> bool:
    """Check if a raw file has already been processed (wiki page exists)."""
    # Read title from raw file
    try:
        content = raw_path.read_text(encoding="utf-8")
        title = extract_title(content)
        if not title:
            return False
        # Check if any wiki page with this title already exists
        safe_title = re.sub(r"[^\w\s-]", "", title.lower())
        safe_title = re.sub(r"\s+", "-", safe_title).strip("-")
        # Check base path
        for page_type_dir in WIKI_DIR.glob("*"):
            if page_type_dir.is_dir():
                if (page_type_dir / f"{safe_title}.md").exists():
                    return True
                if (page_type_dir / f"{safe_title}_*.md").exists():
                    return True
    except Exception:
        pass
    return False


def mark_processed(raw_path: Path):
    """Mark a raw file as processed."""
    RAW_PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    marker = RAW_PROCESSED_DIR / raw_path.name
    marker.write_text(datetime.now(timezone.utc).isoformat(), encoding="utf-8")


# Approved page types
VALID_TYPES = {"concept", "comparison", "playbook", "synthesis", "entity"}

# Map page types to wiki directory names
TYPE_DIR_MAP = {
    "concept": "concepts",
    "comparison": "comparisons",
    "playbook": "playbooks",
    "synthesis": "synthesis",
    "entity": "entities",
}

# Approved tags from SCHEMA.md (single source of truth)
# Loaded from tools/approved_tags.json — DO NOT EDIT THIS BLOCK MANUALLY
# Run: python3 tools/tag_sync.py --apply to sync
import json
_APPROVED_TAGS_PATH = Path(__file__).resolve().parent / 'approved_tags.json'
if _APPROVED_TAGS_PATH.exists():
    APPROVED_TAGS = set(json.loads(_APPROVED_TAGS_PATH.read_text(encoding='utf-8')))
else:
    APPROVED_TAGS = set()


# ---------------------------------------------------------------------------
# HTML → Markdown converter (aggressive, deterministic)
# ---------------------------------------------------------------------------


def convert_html_to_markdown(html_content: str) -> Tuple[str, bool]:
    """Convert raw HTML to clean Markdown.

    Returns:
        (cleaned_text, was_truncated)
    """
    content = html_content

    # Extract body content
    body_start = content.find("<body")
    body_end = content.find("</body>")

    if body_start >= 0 and body_end > body_start:
        body_content = content[body_start:body_end]
    else:
        # Fallback: extract between <main> or <article>
        for tag in ["<main", "<article"]:
            body_start = content.find(tag)
            end_tag = tag.replace("<", "</")
            body_end = content.find(end_tag)
            if body_start >= 0 and body_end > body_start:
                body_content = content[body_start:body_end]
                break
        else:
            body_content = content

    # Remove astro-island blocks (framework noise)
    body_content = re.sub(
        r"<astro-island[^>]*>.*?</astro-island>",
        "",
        body_content,
        flags=re.DOTALL,
    )

    # Remove script and style blocks
    body_content = re.sub(r"<script[^>]*>.*?</script>", "", body_content, flags=re.DOTALL)
    body_content = re.sub(r"<style[^>]*>.*?</style>", "", body_content, flags=re.DOTALL)

    # Remove HTML comments
    body_content = re.sub(r"<!--.*?-->", "", body_content, flags=re.DOTALL)

    # Remove inline styles and classes
    body_content = re.sub(r'\s*class="[^"]*"', "", body_content)
    body_content = re.sub(r'\s*style="[^"]*"', "", body_content)

    # Convert common HTML to Markdown
    # Headings
    for i in range(6, 0, -1):
        body_content = re.sub(
            rf"<h{i}[^>]*>(.*?)</h{i}>",
            rf"{'#' * i} \1\n\n",
            body_content,
            flags=re.DOTALL,
        )

    # Bold and italic
    body_content = re.sub(r"<strong>(.*?)</strong>", r"**\1**", body_content, flags=re.DOTALL)
    body_content = re.sub(r"<b>(.*?)</b>", r"**\1**", body_content, flags=re.DOTALL)
    body_content = re.sub(r"<em>(.*?)</em>", r"*\1*", body_content, flags=re.DOTALL)
    body_content = re.sub(r"<i>(.*?)</i>", r"*\1*", body_content, flags=re.DOTALL)

    # Links
    body_content = re.sub(
        r'<a\s+href="([^"]*)"[^>]*>(.*?)</a>',
        r"[\2](\1)",
        body_content,
        flags=re.DOTALL,
    )

    # Images
    body_content = re.sub(
        r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*/?>',
        r"![\2](\1)",
        body_content,
    )
    body_content = re.sub(
        r'<img[^>]*alt="([^"]*)"[^>]*src="([^"]*)"[^>]*/?>',
        r"![\1](\2)",
        body_content,
    )
    body_content = re.sub(
        r'<img[^>]*src="([^"]*)"[^>]*\/?>',
        r"![](\1)",
        body_content,
    )

    # Lists
    body_content = re.sub(r"<li>(.*?)</li>", r"- \1\n", body_content, flags=re.DOTALL)
    body_content = re.sub(r"<ul[^>]*>", "\n", body_content)
    body_content = re.sub(r"</ul>", "\n", body_content)
    body_content = re.sub(r"<ol[^>]*>", "\n", body_content)
    body_content = re.sub(r"</ol>", "\n", body_content)
    body_content = re.sub(r"<li[^>]*>", "- ", body_content)

    # Code blocks
    body_content = re.sub(
        r"<pre><code[^>]*>(.*?)</code></pre>",
        r"```\n\1\n```\n",
        body_content,
        flags=re.DOTALL,
    )
    body_content = re.sub(r"<code>(.*?)</code>", r"`\1`", body_content, flags=re.DOTALL)

    # Blockquotes
    body_content = re.sub(
        r"<blockquote[^>]*>(.*?)</blockquote>",
        r">\1\n",
        body_content,
        flags=re.DOTALL,
    )

    # Horizontal rules
    body_content = re.sub(r"<hr[^>]*\/?>", "\n---\n", body_content)

    # Paragraphs
    body_content = re.sub(r"<p[^>]*>(.*?)</p>", r"\1\n\n", body_content, flags=re.DOTALL)

    # Line breaks
    body_content = re.sub(r"<br\s*\/?>", "\n", body_content)

    # Remove remaining HTML tags
    body_content = re.sub(r"<[^>]+>", "", body_content)

    # Clean up whitespace
    body_content = re.sub(r"\n{3,}", "\n\n", body_content)
    body_content = re.sub(r"[ \t]+", " ", body_content)
    body_content = re.sub(r"^\s+", "", body_content, flags=re.MULTILINE)
    body_content = body_content.strip()

    # Final cleanup: unescape any remaining HTML entities
    body_content = html.unescape(body_content)

    return body_content, False


# ---------------------------------------------------------------------------
# Wikilink finder
# ---------------------------------------------------------------------------


def find_wikilinks(
    title: str,
    tags: List[str],
    tag_map: Dict[str, List[str]],
    content: str = "",
    max_links: int = 5,
) -> List[str]:
    """Find relevant wiki pages for internal linking.

    Strategy:
    1. Content-based: semantic similarity via title overlap
    2. Tag-based: shared tags from tag_map
    3. Title-based: substring matches
    """
    candidates = []

    # 1. Content-based: check title overlap with existing pages
    if content:
        words = set(re.findall(r"\b\w+\b", content.lower()))
        for page_title, page_content in _get_title_content_pairs().items():
            page_words = set(re.findall(r"\b\w+\b", page_content.lower()))
            overlap = len(words & page_words)
            if overlap > 3:  # meaningful overlap
                candidates.append((page_title, overlap, "content"))

    # 2. Tag-based: shared tags
    for tag in tags:
        if tag in tag_map:
            for page_title in tag_map[tag]:
                if page_title != title:
                    candidates.append((page_title, 2, "tag"))

    # 3. Title-based: substring matches
    title_words = set(title.lower().split())
    for page_title in tag_map.get("llm-wiki", []):
        if page_title != title:
            page_words = set(page_title.lower().split())
            overlap = len(title_words & page_words)
            if overlap > 1:
                candidates.append((page_title, overlap * 3, "title"))

    # Sort by score and return top N
    candidates.sort(key=lambda x: x[1], reverse=True)
    seen = set()
    result = []
    for page_title, score, source in candidates:
        if page_title not in seen:
            seen.add(page_title)
            result.append(page_title)
            if len(result) >= max_links:
                break

    return result


def _get_title_content_pairs() -> Dict[str, str]:
    """Get title-content pairs from existing wiki pages for content matching."""
    pairs = {}
    for subdir in WIKI_DIR.glob("*"):
        if subdir.is_dir():
            for f in subdir.glob("*.md"):
                try:
                    with open(f, "r", encoding="utf-8") as fh:
                        content = fh.read(2000)  # First 2000 chars for matching
                    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                    if title_match:
                        pairs[title_match.group(1).strip()] = content
                except Exception:
                    continue
    return pairs


# ---------------------------------------------------------------------------
# Page type classifier
# ---------------------------------------------------------------------------


def classify_page_type(raw_content: str, title: str) -> str:
    """Classify raw article into wiki page type."""
    title_lower = title.lower()
    content_lower = raw_content[:5000].lower()

    # Comparison indicators
    comparison_keywords = [
        "vs", "versus", "compared", "comparison", "compare",
        "difference", "differences", "pros and cons", "pro vs con",
        "alternative", "alternatives", "vs.", "or",
    ]
    for kw in comparison_keywords:
        if kw in title_lower or kw in content_lower:
            return "comparison"

    # Playbook indicators
    playbook_keywords = [
        "guide", "how to", "tutorial", "step by step", "workflow",
        "implementation", "setup", "configuration", "best practices",
        "practices", "strategy", "strategies", "approach",
    ]
    for kw in playbook_keywords:
        if kw in title_lower or kw in content_lower:
            return "playbook"

    # Synthesis indicators
    synthesis_keywords = [
        "analysis", "overview", "landscape", "state of",
        "trends", "future", "emerging", "review",
    ]
    for kw in synthesis_keywords:
        if kw in title_lower or kw in content_lower:
            return "synthesis"

    return "concept"


# ---------------------------------------------------------------------------
# Title extractor and cleaner
# ---------------------------------------------------------------------------


def extract_title(raw_content: str) -> str:
    """Extract and clean the title from raw content."""
    # Try frontmatter title: first
    title = ""
    if raw_content.startswith("---"):
        fm_end = raw_content.find("---", 3)
        if fm_end > 0:
            fm = raw_content[3:fm_end]
            for line in fm.split("\n"):
                line = line.strip()
                if line.lower().startswith("title:"):
                    title = line.split(":", 1)[1].strip().strip('"').strip("'")
                    break

    # Fallback: first h1
    if not title:
        h1_match = re.search(r"^#\s+(.+)$", raw_content, re.MULTILINE)
        if h1_match:
            title = h1_match.group(1).strip()

    # Fallback: extract from source_url
    if not title and raw_content.startswith("---"):
        fm_end = raw_content.find("---", 3)
        if fm_end > 0:
            fm = raw_content[3:fm_end]
            for line in fm.split("\n"):
                line = line.strip()
                if line.lower().startswith("source_url:"):
                    url = line.split(":", 1)[1].strip()
                    try:
                        parsed = urlparse(url)
                        path_parts = [p for p in parsed.path.split("/") if p]

                        # arXiv: extract paper ID
                        if "arxiv.org" in url:
                            for part in path_parts:
                                if re.match(r"\d{4}\.\d+", part):
                                    title = f"arXiv:{part}"
                                    break
                            if not title:
                                title = "arXiv Paper"
                        else:
                            last_part = path_parts[-1] if path_parts else url
                            # Clean up URL slug
                            title = re.sub(r"[-_]", " ", last_part)
                            title = re.sub(r"\.(html|md|htm)$", "", title).strip()
                            title = re.sub(r"\s+", " ", title).strip()
                    except Exception:
                        pass
                    break

    if not title:
        return ""

    # === Date stripping (most specific first) ===

    # 1. "in YYYY" or "in YYYY–anything" at end (before anything else!)
    title = re.sub(r"\s+in\s+\d{4}\s*[-–—\d]*\s*$", "", title, flags=re.IGNORECASE).strip()

    # 2. Year ranges anywhere: "2025–2026" or "2026–2027"
    title = re.sub(r"\s+\d{4}\s*[-–—]\s*\d{4}\s*[:，,.]?\s*", " ", title, flags=re.IGNORECASE).strip()

    # 3. Single-char preposition before year range: "в 2026–2027:"
    title = re.sub(r"\s+\w\s+\d{4}\s*[-–—]\s*\d{4}\s*[:，,.]?\s*", " ", title, flags=re.IGNORECASE).strip()

    # 4. Trailing "[2026]" or "[2026-07]"
    title = re.sub(r"\s*\[\d{4}[-\d]*\]\s*$", "", title).strip()

    # 5. "YYYY -" or "YYYY –" mid-text (year as separator): "Frameworks 2026 - LangGraph"
    title = re.sub(r"\s+\d{4}\s*[-–—]\s+", " ", title, flags=re.IGNORECASE).strip()

    # 6. "as of MONTH YYYY" or "as of YYYY"
    title = re.sub(r"\s+as of\s+\w+\s+\d{4}\s*$", "", title, flags=re.IGNORECASE).strip()
    title = re.sub(r"\s+as of\s+\d{4}\s*$", "", title, flags=re.IGNORECASE).strip()

    # 7. Trailing YYYY-MM-DD
    title = re.sub(r"\s*\d{4}\s*[-/]\s*\d{1,2}\s*[-/]\s*\d{1,2}\s*$", "", title, flags=re.IGNORECASE).strip()
    title = re.sub(r"\s*\d{8}$", "", title, flags=re.IGNORECASE).strip()

    # 8. Trailing standalone year
    title = re.sub(r"\s+\d{4}\s*$", "", title).strip()

    # 9. Trailing comma+year
    title = re.sub(r",\s*\d{4}\s*$", "", title).strip()

    # Clean up multiple spaces
    title = re.sub(r"\s+", " ", title).strip()

    # Remove trailing punctuation
    title = re.sub(r"\s*[:，,.!?]+\s*$", "", title).strip()

    return title

def extract_tags(raw_content: str, title: str) -> List[str]:
    """Extract tags from raw content and title."""
    tags = set()

    # Try frontmatter tags
    if raw_content.startswith("---"):
        fm_end = raw_content.find("---", 3)
        if fm_end > 0:
            fm = raw_content[3:fm_end]
            for line in fm.split("\n"):
                line = line.strip()
                if line.lower().startswith("tags:"):
                    tag_str = line.split(":", 1)[1].strip()
                    # Handle both "tags: a, b, c" and "tags: [a, b, c]"
                    tag_str = tag_str.strip("[]")
                    for tag in tag_str.split(","):
                        tag = tag.strip().lower()
                        if tag and tag in APPROVED_TAGS:
                            tags.add(tag)

    # Extract keywords from title and content
    title_words = set(re.findall(r"\b\w+\b", title.lower()))
    content_words = set(re.findall(r"\b\w+\b", raw_content[:10000].lower()))

    # Map common words to approved tags
    word_to_tag = {
        "llm": "llm",
        "language": "language-model",
        "model": "foundation-model",
        "training": "training",
        "fine": "fine-tuning",
        "tuning": "fine-tuning",
        "lora": "lora",
        "qlora": "qlora",
        "dpo": "dpo",
        "rlhf": "rlhf",
        "sft": "sft",
        "quantization": "quantization",
        "gguf": "gguf",
        "gptq": "gptq",
        "awq": "awq",
        "rag": "rag",
        "retrieval": "retrieval",
        "prompt": "prompt-engineering",
        "engineering": "prompt-engineering",
        "agent": "agent",
        "agents": "agent",
        "multi": "multi-agent",
        "agent": "agent",
        "security": "security",
        "privacy": "privacy",
        "ethics": "ethics",
        "governance": "governance",
        "ai": "ai",
        "machine": "machine-learning",
        "learning": "machine-learning",
        "deep": "deep-learning",
        "neural": "deep-learning",
        "transformer": "transformers",
        "nlp": "nlp",
        "natural": "nlp",
        "language": "nlp",
        "processing": "nlp",
        "vision": "computer-vision",
        "image": "computer-vision",
        "cv": "computer-vision",
        "reinforcement": "reinforcement-learning",
        "rl": "reinforcement-learning",
        "evaluation": "evaluation",
        "benchmark": "benchmark",
        "eval": "evaluation",
        "architecture": "architecture",
        "research": "research",
        "tutorial": "tutorial",
        "guide": "guide",
        "comparison": "comparison",
        "playbook": "playbook",
        "synthesis": "synthesis",
        "news": "news",
        "analysis": "analysis",
        "review": "review",
        "tool": "tool",
        "framework": "framework",
        "library": "library",
        "api": "api",
        "deployment": "deployment",
        "optimization": "optimization",
        "data": "data",
        "dataset": "dataset",
        "preprocessing": "preprocessing",
        "postprocessing": "postprocessing",
        "open": "open-source",
        "source": "open-source",
        "closed": "closed-source",
        "proprietary": "proprietary",
        "commercial": "commercial",
        "academic": "academic",
        "industry": "industry",
        "application": "application",
        "use": "use-case",
        "case": "use-case",
        "study": "use-case",
        "best": "best-practice",
        "practice": "best-practice",
        "pattern": "design-pattern",
        "system": "system-design",
        "scalable": "scalability",
        "performance": "performance",
        "cost": "cost",
        "efficiency": "efficiency",
        "energy": "energy",
        "compliance": "compliance",
        "regulation": "regulation",
        "policy": "policy",
        "standard": "standards",
        "interoperability": "interoperability",
        "integration": "integration",
        "automation": "automation",
        "workflow": "workflow",
        "pipeline": "pipeline",
        "ci": "ci-cd",
        "cd": "ci-cd",
        "mlops": "mlops",
        "devops": "devops",
        "cloud": "cloud",
        "edge": "edge",
        "serverless": "serverless",
        "container": "container",
        "kubernetes": "kubernetes",
        "docker": "docker",
        "microservice": "microservice",
        "distributed": "distributed",
        "parallel": "parallel",
        "async": "async",
        "real": "real-time",
        "time": "real-time",
        "batch": "batch",
        "streaming": "streaming",
        "offline": "offline",
        "online": "online",
        "supervised": "supervised",
        "unsupervised": "unsupervised",
        "semi": "semi-supervised",
        "self": "self-supervised",
        "transfer": "transfer-learning",
        "few": "few-shot",
        "zero": "zero-shot",
        "prompt": "prompt-tuning",
        "instruction": "instruction-tuning",
        "alignment": "alignment",
        "pytorch": "pytorch",
        "tensorflow": "tensorflow",
        "jax": "jax",
        "onnx": "onnx",
        "cuda": "cuda",
        "gpu": "gpu",
        "hardware": "hardware",
        "software": "software",
        "frontend": "frontend",
        "backend": "backend",
        "mobile": "mobile",
        "web": "web",
        "api": "api",
        "database": "vector-database",
        "search": "search",
        "retrieval": "retrieval",
        "embedding": "embedding",
        "vector": "vector-database",
        "gpt": "gpt",
        "claude": "claude",
        "gemini": "gemini",
        "llama": "llama",
        "mistral": "mistral",
        "diffusion": "stable-diffusion",
        "whisper": "whisper",
        "speech": "speech-to-text",
        "audio": "audio-generation",
        "image": "image-generation",
        "video": "video-generation",
        "multimodal": "multimodal",
        "foundation": "foundation-model",
        "open": "open-source",
        "open": "open-source",
    }

    for word in title_words | content_words:
        if word in word_to_tag:
            tags.add(word_to_tag[word])

    # Always include base tags
    tags.add("llm-wiki")
    tags.add("knowledge-base")

    return sorted(tags)


# ---------------------------------------------------------------------------
# Content relevance scorer
# ---------------------------------------------------------------------------


def _structural_depth(content: str) -> int:
    """Score how structurally rich the content is."""
    score = 0
    # Headings indicate structure
    h_count = len(re.findall(r"^#{1,3}\s+", content, re.MULTILINE))
    score += min(h_count // 3, 5)

    # Lists indicate organized information
    list_count = len(re.findall(r"^\s*[-*•]\s+", content, re.MULTILINE))
    score += min(list_count // 5, 3)

    # Code blocks indicate technical depth
    code_count = len(re.findall(r"```", content))
    score += min(code_count // 2, 3)

    # Tables indicate structured data
    table_count = len(re.findall(r"^\|", content, re.MULTILINE))
    score += min(table_count // 3, 3)

    # References/sources
    ref_count = len(re.findall(r"https?://|arxiv\.org|github\.com", content))
    score += min(ref_count, 2)

    # Citations
    cite_count = len(re.findall(r"\[\d+\]|\(Author.*?\)", content))
    score += min(cite_count, 2)

    return min(score, 18)


def _semantic_density(content: str, title: str) -> int:
    """Score how information-dense the content is."""
    score = 0
    words = re.findall(r"\b\w+\b", content.lower())
    if not words:
        return 0

    # Content-word ratio (vs filler)
    fillers = {"the", "a", "an", "is", "are", "was", "were", "be", "been",
               "being", "have", "has", "had", "do", "does", "did", "will",
               "would", "could", "should", "may", "might", "can", "shall",
               "to", "of", "in", "for", "on", "with", "at", "by", "from",
               "as", "into", "through", "during", "before", "after", "above",
               "below", "between", "out", "off", "over", "under", "again",
               "further", "then", "once", "and", "but", "or", "nor", "not",
               "so", "yet", "both", "either", "neither", "each", "every",
               "all", "any", "few", "more", "most", "other", "some", "such",
               "no", "only", "own", "same", "than", "too", "very", "just",
               "because", "if", "when", "where", "how", "what", "which",
               "who", "whom", "this", "that", "these", "those", "it", "its"}
    content_words = [w for w in words if w not in fillers]
    density = len(content_words) / max(len(words), 1)
    score += int(density * 10)  # up to 10 points for density

    # Unique word ratio (lexical diversity)
    unique_ratio = len(set(content_words)) / max(len(content_words), 1)
    score += int(unique_ratio * 5)  # up to 5 points for diversity

    return min(score, 15)


def _tag_precision(content: str, title: str, extracted_tags: List[str]) -> int:
    """Score how well extracted tags match the actual content."""
    if not extracted_tags:
        return 0

    score = 0
    content_lower = (content + " " + title).lower()

    # Map tags back to expected content signals
    tag_signal_map = {
        "llm": {"language model", "large language", "llm", "gpt", "claude", "gemini"},
        "rag": {"retrieval augmented", "retrieval-augmented", "vector store", "vector database", "knowledge base"},
        "fine-tuning": {"fine-tun", "finetun", "lora", "qlora", "adapter", "sft", "instruction tun"},
        "transformers": {"transformer", "attention mechanism", "self-attention", "multi-head attention", "encoder", "decoder"},
        "computer-vision": {"image", "vision", "conv", "cnn", "resnet", "detection", "segmentation", "classification"},
        "nlp": {"natural language", "token", "tokenization", "nlp", "text processing", "sentiment"},
        "deep-learning": {"neural network", "backpropagation", "gradient", "loss function", "activation function"},
        "security": {"security", "privacy", "adversarial", "vulnerability", "attack", "defense", "encryption", "authentication"},
        "deployment": {"deploy", "inference", "serving", "latency", "throughput", "production", "api", "endpoint"},
    }

    for tag, signals in tag_signal_map.items():
        if tag in extracted_tags:
            matches = sum(1 for s in signals if s in content_lower)
            if matches >= 2:
                score += 2  # strong confirmation
            elif matches >= 1:
                score += 1  # weak confirmation

    return min(score, 10)


def _content_type_markers(content: str) -> Dict[str, float]:
    """Analyze content structure to determine type probabilities."""
    content_lower = content.lower()
    title_lower = (content.split("---")[0] if "---" in content else content).lower()
    full_lower = content_lower + " " + title_lower

    markers = {
        "comparison": 0.0,
        "playbook": 0.0,
        "synthesis": 0.0,
        "concept": 0.0,
    }

    # Comparison signals
    comparison_patterns = [
        r"\b(vs\.?|versus)\b",
        r"\bcompared?\s+(?:to|with|against)\b",
        r"\b(?:(?:pros|cons|advantages?|disadvantages?|trade\s*offs?)\b.*?(?:vs|versus|compared))",
        r"\bwhich.*?(?:is|are|should)\b.*?(?:better|worse|preferred)\b",
        r"\bdifferen(?:t|ces?)\s+(?:between|in\s+(?:\w+\s+and|\w+\s+/))",
        r"\balternatives?\s*(?:to|for)\b",
        r"\bside\s*[-_]?by\s*[-_]?side\b",
        r"\bhead\s*[-_]?to\s*[-_]?head\b",
    ]
    markers["comparison"] += sum(1 for p in comparison_patterns if re.search(p, full_lower))

    # Playbook signals
    playbook_patterns = [
        r"\bhow\s+to\b",
        r"\bstep\s*[-_]?by\s*[-_]?step\b",
        r"\bguide\b",
        r"\btutorial\b",
        r"\bwant\s+to\b",
        r"\bimplement(?:ing|ation)?\b",
        r"\bsetup\b",
        r"\bconfig(?:uration)?\b",
        r"\bbest\s+practices?\b",
        r"\bworkflow\b",
        r"\bprocedure\b",
        r"\brecipe\b",
        r"\bplaybook\b",
    ]
    markers["playbook"] += sum(1 for p in playbook_patterns if re.search(p, full_lower))

    # Synthesis signals
    synthesis_patterns = [
        r"\boverview\b",
        r"\bstate\s+of\b",
        r"\btrends?\b",
        r"\blandscape\b",
        r"\bsurvey\b",
        r"\breview\b",
        r"\banalysis\b",
        r"\bfuture\b",
        r"\bemerging\b",
        r"\bcomprehensive\b",
        r"\bcomplete\s+guide\b",
        r"\bultimate\b",
        r"\bdefinitive\b",
        r"\broadmap\b",
    ]
    markers["synthesis"] += sum(1 for p in synthesis_patterns if re.search(p, full_lower))

    # Concept signals (default — present if no strong other signals)
    concept_patterns = [
        r"\bconcept\b",
        r"\bdef(?:inition|ine)\b",
        r"\bwhat\s+is\b",
        r"\bexplain\b",
        r"\bintroduc(?:e|tion)\b",
        r"\bbasic\b",
        r"\bfundamental\b",
        r"\bcore\b",
    ]
    markers["concept"] += sum(1 for p in concept_patterns if re.search(p, full_lower))

    # Boost concept if it's a technical term (no action verbs)
    # Short, noun-heavy titles with no how-to/compare/survey markers
    if markers["playbook"] < 2 and markers["comparison"] < 2 and markers["synthesis"] < 2:
        markers["concept"] += 2

    return markers


def score_relevance(raw_content: str, title: str = "") -> Tuple[int, str]:
    """Score content relevance using semantic-aware analysis.

    Returns:
        (score, page_type)
    """
    score = 0
    content_lower = raw_content.lower()
    title_lower = title.lower()

    # === Structural Depth (0-18) ===
    score += _structural_depth(raw_content)

    # === Semantic Density (0-15) ===
    score += _semantic_density(raw_content, title)

    # Extract tags for precision scoring
    tags = extract_tags(raw_content, title)
    score += _tag_precision(raw_content, title, tags)

    # === Content Type Analysis ===
    type_markers = _content_type_markers(raw_content)
    page_type = max(type_markers, key=type_markers.get)

    # Type confirmation bonus: if content type aligns with title signals
    # e.g., "vs" in title → comparison confirmed
    title_type_boost = 0
    if "vs" in title_lower or "versus" in title_lower:
        title_type_boost = type_markers["comparison"]
    elif "how to" in title_lower or "guide" in title_lower:
        title_type_boost = type_markers["playbook"]
    elif "overview" in title_lower or "landscape" in title_lower:
        title_type_boost = type_markers["synthesis"]
    score += min(title_type_boost, 3)

    # === Length bonus (diminishing returns) ===
    length = len(raw_content)
    if length > 10000:
        score += 3
    elif length > 5000:
        score += 2
    elif length > 2000:
        score += 1

    # === Source quality bonus ===
    source_indicators = [
        "arxiv.org", "research", "paper", "study", "experiment",
        "benchmark", "evaluation", "results", "methodology",
    ]
    source_score = sum(1 for s in source_indicators if s in content_lower)
    score += min(source_score, 3)

    return score, page_type


# ---------------------------------------------------------------------------
# Wiki page generator
# ---------------------------------------------------------------------------


def generate_wiki_page(
    raw_path: Path,
    raw_content: str,
    title: str,
    page_type: str,
    tags: List[str],
    tag_map: Dict[str, List[str]],
) -> Optional[str]:
    """Generate a wiki page from raw content.

    Returns:
        Relative path to generated wiki page, or None if skipped.
    """
    # Convert HTML to Markdown
    cleaned_content, was_truncated = convert_html_to_markdown(raw_content)

    # Check minimum length
    if len(cleaned_content) < MIN_CONTENT_LENGTH:
        print(f"  Skipped: content too short ({len(cleaned_content)} chars)")
        return None

    # Find wikilinks (content-based)
    wikilinks = find_wikilinks(title, tags, tag_map, content=cleaned_content)

    # Generate wiki filename
    safe_title = re.sub(r"[^\w\s-]", "", title.lower())
    safe_title = re.sub(r"\s+", "-", safe_title).strip("-")

    # Map page type to directory name
    dir_name = TYPE_DIR_MAP.get(page_type, page_type)
    page_type_dir = WIKI_DIR / dir_name

    # Check 1: if base version (no suffix, no date) already exists, skip duplicate
    base_path = page_type_dir / f"{safe_title}.md"
    if base_path.exists():
        print(f"  Skipped: base page already exists ({safe_title}.md)")
        return None

    # Check 2: if any suffixed version exists, skip (prevent duplicate creation)
    for existing in page_type_dir.glob(f"{safe_title}_*.md"):
        print(f"  Skipped: suffixed page already exists ({existing.name})")
        return None

    # Check 3: if a date-stamped version exists, skip
    date_str = raw_path.stem.split("-")[-1] if "-" in raw_path.stem else datetime.now().strftime("%Y-%m-%d")
    # Validate date format: must be YYYY-MM-DD pattern
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
        date_str = ""
    if date_str:
        date_path = page_type_dir / f"{safe_title}_{date_str}.md"
        if date_path.exists():
            print(f"  Skipped: date-stamped page already exists ({safe_title}_{date_str}.md)")
            return None

    # Use clean base name (no suffix, no date) — first valid ingest wins
    filename = f"{safe_title}.md"
    wiki_path = page_type_dir / filename

    # Build wiki content
    related_links = []
    for link in wikilinks[:5]:
        related_links.append(f"- [[{link}]]")

    # Generate description from first 200 chars of content
    description = cleaned_content[:200].strip().replace('\n', ' ')
    if len(cleaned_content) > 200:
        description += "..."

    wiki_content = f"""---
title: "{title}"
type: {page_type}
tags:
  - llm-wiki
  - knowledge-base
  """
    for tag in tags:
        if tag not in ("llm-wiki", "knowledge-base"):
            wiki_content += f"  - {tag}\n"
    wiki_content += f"""---

# {title}

> **Source:** {raw_path.name}
> **Type:** {page_type}
> **Created:** {datetime.now(timezone.utc).strftime('%Y-%m-%d')}
> **Updated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d')}
> **Confidence:** high
> **Description:** {description}
> **Sources:**
>   - {raw_path.name}
> **Links:**
"""
    if related_links:
        wiki_content += '\n'.join(related_links) + "\n"
    else:
        wiki_content += "  - No related articles found.\n"

    wiki_content += f"""
## Key Findings

{cleaned_content[:3000]}

## Summary

{cleaned_content[3000:6000] if len(cleaned_content) > 6000 else 'See Key Findings for full content.'}

## Related Articles

"""
    if related_links:
        wiki_content += '\n'.join(related_links)
    else:
        wiki_content += "No related articles found."

    wiki_content += "\n"

    # Ensure wiki subdirectory exists
    wiki_path.parent.mkdir(parents=True, exist_ok=True)

    with open(wiki_path, "w", encoding="utf-8") as f:
        # Final cleanup: unescape any remaining HTML entities
        wiki_content = html.unescape(wiki_content)
        # Remove any trailing whitespace
        wiki_content = wiki_content.strip() + "\n"
        f.write(wiki_content)

    return str(wiki_path.relative_to(ROOT))


# ---------------------------------------------------------------------------
# Index updater
# ---------------------------------------------------------------------------


def update_index(wiki_path: str, content_type: str, title: str):
    """Update index.md with new wiki page. Only adds if not already present."""
    # Read existing index
    if INDEX_FILE.exists():
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            index_content = f.read()
    else:
        index_content = ""

    # Check if this page is already in index — avoid duplicates
    if wiki_path in index_content:
        print(f"    Index: entry already exists ({wiki_path})")
        return

    # Add new entry at the top (after frontmatter if exists)
    new_entry = f"### [{title}]({wiki_path})\n"

    if "---" in index_content:
        fm_end = index_content.find("---", 3)
        if fm_end > 0:
            index_content = (
                index_content[: fm_end + 3]
                + "\n\n"
                + new_entry
                + index_content[fm_end + 3 :]
            )
        else:
            index_content = new_entry + "\n" + index_content
    else:
        index_content = new_entry + "\n" + index_content

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(index_content)


# ---------------------------------------------------------------------------
# Tag map builder
# ---------------------------------------------------------------------------


def build_tag_map() -> Dict[str, List[str]]:
    """Build tag-to-page-title mapping from existing wiki pages."""
    tag_map: Dict[str, List[str]] = {}

    for subdir in WIKI_DIR.glob("*"):
        if subdir.is_dir():
            for f in subdir.glob("*.md"):
                try:
                    with open(f, "r", encoding="utf-8") as fh:
                        content = fh.read(500)  # Just frontmatter
                    # Extract tags
                    tags = []
                    if content.startswith("---"):
                        fm_end = content.find("---", 3)
                        if fm_end > 0:
                            fm = content[3:fm_end]
                            in_tags = False
                            for line in fm.split("\n"):
                                line = line.strip()
                                if line == "tags:":
                                    in_tags = True
                                    continue
                                if in_tags:
                                    if line.startswith("- "):
                                        tag = line[2:].strip().lower()
                                        tags.append(tag)
                                    else:
                                        break

                    # Extract title
                    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                    title = title_match.group(1).strip() if title_match else f.name

                    # Add to tag map
                    for tag in tags:
                        if tag not in tag_map:
                            tag_map[tag] = []
                        if title not in tag_map[tag]:
                            tag_map[tag].append(title)
                except Exception:
                    continue

    return tag_map


# ---------------------------------------------------------------------------
# Process raw files
# ---------------------------------------------------------------------------


def process_raw_files(
    raw_dir: Path, limit: Optional[int] = None
) -> Dict[str, int]:
    """Process raw article files and generate wiki pages.

    Returns:
        Statistics dict with counts.
    """
    stats = {
        "new_pages": 0,
        "html_conversions": 0,
        "truncations": 0,
        "skipped": 0,
    }

    # Build tag map from existing wiki pages
    print("Scanning existing wiki pages for cross-references...")
    tag_map = build_tag_map()
    print(f"   Found {sum(len(v) for v in tag_map.values())} tag->page mappings")

    # Get raw files
    raw_files = sorted(raw_dir.glob("*.md"))
    if limit:
        raw_files = raw_files[:limit]

    print(f"\nProcessing {len(raw_files)} raw files...\n")

    for raw_path in raw_files:
        try:
            with open(raw_path, "r", encoding="utf-8") as f:
                raw_content = f.read()
        except Exception as e:
            print(f"  Error reading {raw_path.name}: {e}")
            stats["skipped"] += 1
            continue

        # Skip if already processed (wiki page exists)
        if is_already_processed(raw_path):
            print(f"  {raw_path.name}:")
            print(f"    Skipped: already processed (wiki page exists)")
            stats["skipped"] += 1
            continue

        # Extract title
        title = extract_title(raw_content)
        if not title:
            print(f"  Skipped {raw_path.name}: no title found")
            stats["skipped"] += 1
            continue

        # Score relevance
        score, page_type = score_relevance(raw_content, title)

        # Determine if we should process this file
        if score < 3:
            print(f"  {raw_path.name}:")
            print(f"    Relevance: low (score: {score})")
            print(f"    Type: {page_type}")
            print(f"    Skipped: low relevance")
            stats["skipped"] += 1
            continue

        print(f"  {raw_path.name}:")
        print(f"    Relevance: {'high' if score >= 10 else 'medium'} (score: {score})")
        print(f"    Type: {page_type}")

        # Extract tags
        tags = extract_tags(raw_content, title)

        # Generate wiki page
        wiki_path = generate_wiki_page(
            raw_path, raw_content, title, page_type, tags, tag_map
        )

        if wiki_path:
            print(f"    Generated: {wiki_path}")
            stats["new_pages"] += 1

            # Mark raw file as processed
            mark_processed(raw_path)

            # Update index
            update_index(wiki_path, page_type, title)
        else:
            stats["skipped"] += 1

    return stats


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="LLM Wiki Integrator")
    parser.add_argument("--dry-run", action="store_true", help="Don't write files")
    parser.add_argument("--limit", type=int, help="Process only N files")
    args = parser.parse_args()

    print("LLM Wiki Integrator - Starting...")
    print(f"Raw directory: {RAW_DIR}")
    print(f"Wiki directory: {WIKI_DIR}")

    stats = process_raw_files(RAW_DIR, limit=args.limit)

    print(f"\nIntegration complete:")
    print(f"  New wiki pages: {stats['new_pages']}")
    print(f"  HTML conversions: {stats['html_conversions']}")
    print(f"  Truncation warnings: {stats['truncations']}")
    print(f"  Skipped (already processed): {stats['skipped']}")

    # Status line
    if stats['new_pages'] > 0:
        print(f"Статус: [ACTIVE] — інтеграція завершена, створено {stats['new_pages']} wiki-сторінок")
    else:
        print(f"Статус: [SILENT] — немає нових даних для інгесту")


if __name__ == "__main__":
    main()
