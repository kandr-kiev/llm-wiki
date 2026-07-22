#!/usr/bin/env python3
"""
Shared utilities for LLM Wiki tools.

Centralizes:
  - SHA256 body hashing (NO .strip() — matches fix_sha256.py canonical)
  - Frontmatter splitting (find-based, matches fix_sha256.py canonical)
  - YAML frontmatter parsing
  - Slug generation
  - Log appending
  - Approved tags list (single source of truth)
  - File existence checks
"""

import hashlib
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Canonical frontmatter splitting — matches fix_sha256.py, check_new_raw.py
# ---------------------------------------------------------------------------

def split_frontmatter(text: str):
    """Split markdown into (frontmatter, body).
    
    Canonical logic: find '\\n---\\n' boundary after initial '---\\n'.
    Returns (fm_string, body_string). If no frontmatter, returns (None, text).
    """
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end+5:]


# ---------------------------------------------------------------------------
# SHA256 — NO .strip() on body (canonical, matches fix_sha256.py)
# ---------------------------------------------------------------------------

def compute_sha256(content: str) -> str:
    """Compute SHA256 of content body. NO .strip() — canonical."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def compute_body_sha256(filepath: Path) -> str:
    """Compute SHA256 of a file's body (after frontmatter)."""
    text = filepath.read_text(encoding='utf-8')
    fm, body = split_frontmatter(text)
    if fm is None:
        return None
    return compute_sha256(body)


# ---------------------------------------------------------------------------
# YAML frontmatter parsing (simple key: value / key: [a, b])
# ---------------------------------------------------------------------------

def parse_simple_yaml(fm: str):
    """Parse simple YAML frontmatter into dict.
    
    Supports:
      - key: value
      - key: [item1, item2]
      - key: (multiline list with - item)
      - key: true/false
    """
    data = {}
    lines = fm.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.strip()
        i += 1
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            data[key] = [x.strip().strip('"\'') for x in inner.split(",") if x.strip()]
        elif value.lower() in {"true", "false"}:
            data[key] = value.lower() == "true"
        elif value == "":
            # Multi-line YAML list
            items = []
            while i < len(lines):
                child = lines[i].strip()
                i += 1
                if not child:
                    continue
                if child.startswith("- "):
                    items.append(child[2:].strip().strip('"\''))
                elif ":" in child and not child.startswith("-"):
                    i -= 1
                    break
            data[key] = items if items else value
        else:
            data[key] = value.strip('"\'')
    return data


# ---------------------------------------------------------------------------
# Slug generation (canonical, used by all monitors)
# ---------------------------------------------------------------------------

def slugify(title: str) -> str:
    """Generate slug from title — canonical logic."""
    slug = title.lower().replace(' ', '-').replace('.', '').replace(',', '').replace(':', '').replace('—', '-')
    slug = ''.join(c for c in slug if c.isalnum() or c in '-_')
    slug = slug[:100]
    return slug


# ---------------------------------------------------------------------------
# Approved tags — SINGLE SOURCE OF TRUTH
# ---------------------------------------------------------------------------

APPROVED_TAGS = {    "active-learning",
    "adoption",
    "advanced-rag",
    "agent",
    "agent-skills",
    "agent-workflow",
    "agentic-tasks",
    "ai",
    "ai-agents",
    "ai-benchmark",
    "ai-coding",
    "ai-education",
    "ai-infrastructure",
    "ai-integration",
    "ai-safety",
    "ai-workforce",
    "alignment",
    "analysis",
    "analytics",
    "application",
    "architecture",
    "architecture-design",
    "arxiv",
    "assembly",
    "async",
    "audit",
    "auto-ml",
    "automation",
    "awq",
    "benchmark",
    "best-practice",
    "bias-mitigation",
    "bioinformatics",
    "broadcom",
    "business-process",
    "chatgpt",
    "ci-cd",
    "clarification",
    "claude",
    "clinical",
    "clinical-decision-support",
    "closed-source",
    "cloud",
    "cloudflare",
    "code-architecture",
    "code-quality",
    "coding-agents",
    "company",
    "comparison",
    "computer-vision",
    "concept",
    "conditional-generation",
    "configuration",
    "consistency-regularization",
    "constitutional-ai",
    "context-window",
    "contrastive-loss",
    "controllability",
    "cost",
    "cost-economics",
    "cot",
    "critical-analysis",
    "cron",
    "data",
    "data-efficiency",
    "data-engineering",
    "data-parallelism",
    "data-quality",
    "decision",
    "deepseek",
    "deployment",
    "design-pattern",
    "diffusion",
    "digest",
    "distributed",
    "distributed-training",
    "dpo",
    "dqn",
    "drug-discovery",
    "duplicates",
    "edge",
    "efficiency",
    "embedding",
    "embeddings",
    "embodied-ai",
    "enterprise",
    "enterprise-ai",
    "entity",
    "environment-modeling",
    "europe",
    "evaluation",
    "event",
    "explainable-ai",
    "exploration",
    "faq",
    "feature-attribution",
    "few-shot",
    "fine-tuning",
    "foundation-model",
    "framework",
    "gemini",
    "gemma",
    "genebench-pro",
    "generative-models",
    "genomics",
    "gguf",
    "glm",
    "governance",
    "gpt",
    "gptq",
    "gpu",
    "graph-neural-networks",
    "guide",
    "hardware",
    "health-check",
    "healthcare",
    "helk",
    "hermes",
    "hermes-agent",
    "hp",
    "iFLYTEK",
    "image-generation",
    "in-context-learning",
    "indexer",
    "inference",
    "inference-chip",
    "ingest",
    "instruction-tuning",
    "integration",
    "integrator",
    "integrity",
    "interpretability",
    "knowledge-base",
    "knowledge-storage",
    "labor-market",
    "language-action",
    "language-model",
    "library",
    "lint",
    "llama",
    "llm",
    "llm-agents",
    "llm-assistance",
    "llm-benchmarks",
    "llm-wiki",
    "local",
    "local-llm-hardware",
    "lora",
    "machine-learning",
    "manufacturing",
    "mcp",
    "medical-calculation",
    "meeting",
    "milestone",
    "mistral",
    "mixed-precision",
    "ml",
    "ml-infrastructure",
    "mmlu",
    "mobile",
    "model",
    "model-auditing",
    "model-parallelism",
    "moe",
    "monitors",
    "mt-bench",
    "multi-agent",
    "multimodal",
    "nas",
    "news",
    "next-gen",
    "nlp",
    "object-centric",
    "obsidian",
    "okf",
    "online",
    "open-domain",
    "open-source",
    "open-source-llm",
    "openai",
    "optimization",
    "orchestration",
    "pairwise-comparison",
    "parallel",
    "partial-observability",
    "partnership",
    "peft",
    "performance",
    "pipeline",
    "planning",
    "playbook",
    "pluralism",
    "policy",
    "policy-gradient",
    "process-improvement",
    "productivity",
    "prompt-engineering",
    "prompt-tuning",
    "qa",
    "qlora",
    "quantization",
    "query",
    "query-strategy",
    "qwen",
    "rag",
    "real-time",
    "reference",
    "reinforcement-learning",
    "reliability",
    "replication",
    "representation-learning",
    "reproducibility",
    "research",
    "retrieval",
    "rlhf",
    "robotics",
    "robustness",
    "rtx-5070-ti",
    "safety",
    "scalability",
    "scheduling",
    "schema",
    "scientific-ai",
    "scientific-research",
    "scripts",
    "search",
    "security",
    "self-consistency",
    "self-supervised",
    "self-training",
    "semi-supervised",
    "serverless",
    "serving",
    "setup",
    "sft",
    "skills-gap",
    "software-engineering",
    "sol",
    "source",
    "source-management",
    "stable-diffusion",
    "storage",
    "style-transfer",
    "supervised",
    "swarm-intelligence",
    "swrl",
    "synthesis",
    "system-audit",
    "system-design",
    "system-integrity",
    "tdd",
    "text-generation",
    "tools",
    "tot",
    "toxicity",
    "toxicity-reduction",
    "training",
    "transfer-learning",
    "trends",
    "trust",
    "truthfulqa",
    "tutorial",
    "uncertainty",
    "use-case",
    "user-metrics",
    "vector-database",
    "verification",
    "visualization",
    "vllm",
    "web",
    "wiki",
    "wiki-maintenance",
    "wikilinks",
    "workflow",
    "xai",
    "zero-shot",
}


# ---------------------------------------------------------------------------
# Log appending (canonical)
# ---------------------------------------------------------------------------

def append_to_log(log_file: Path, component: str, entry: str):
    """Append entry to log.md with timestamp."""
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"\n## [{timestamp}] {component} | {entry}\n")


# ---------------------------------------------------------------------------
# File existence checks (resilient)
# ---------------------------------------------------------------------------

def check_dir_exists(path: Path) -> bool:
    """Check if directory exists (resilient to missing paths)."""
    return path.exists() and path.is_dir()


def check_file_exists(path: Path) -> bool:
    """Check if file exists."""
    return path.exists() and path.is_file()


# ---------------------------------------------------------------------------
# Status line output (canonical format)
# ---------------------------------------------------------------------------

def print_status(has_new: bool, label: str, count: int, source_count: int):
    """Print canonical status line."""
    if has_new:
        print(f"Статус: [ACTIVE] — сканування {source_count} {label}, знайдено {count} нових")
    else:
        print(f"Статус: [SILENT] — немає нових даних для сканування")


# ---------------------------------------------------------------------------
# Raw file slug from title (canonical for monitors)
# ---------------------------------------------------------------------------

def raw_filename_from_title(title: str, suffix: str = '') -> str:
    """Generate raw filename from title with date suffix.
    
    Args:
        title: Article title
        suffix: Optional prefix (e.g. 'gh-' for GitHub)
    """
    slug = slugify(title)
    date_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    return f"{suffix}{slug}-{date_str}.md"


# ---------------------------------------------------------------------------
# Frontmatter template for new raw files (canonical)
# ---------------------------------------------------------------------------

def build_frontmatter(source_url: str, blog_source: str, sha256: str = 'PLACEHOLDER') -> str:
    """Build canonical frontmatter for new raw files."""
    ingested = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    return f"---\nsource_url: {source_url}\ningested: {ingested}\nsha256: {sha256}\nblog_source: {blog_source}\n---\n"


# ---------------------------------------------------------------------------
# Hash verification — SINGLE SOURCE OF TRUTH for all tools
# ---------------------------------------------------------------------------

def verify_file_hash(filepath: Path) -> dict:
    """Verify SHA256 of a raw file.
    
    Returns dict with:
      - status: 'ok' | 'mismatch' | 'no_hash' | 'no_fm'
      - stored: str | None  (stored sha256 from frontmatter)
      - computed: str | None  (computed sha256 of body)
      - has_frontmatter: bool
    """
    content = filepath.read_text(encoding='utf-8')
    fm, body = split_frontmatter(content)
    
    if fm is None:
        return {'status': 'no_fm', 'stored': None, 'computed': None, 'has_frontmatter': False}
    
    m = re.search(r'sha256:\s*([a-f0-9]{64})', fm)
    if m is None:
        return {'status': 'no_hash', 'stored': None, 'computed': compute_sha256(body), 'has_frontmatter': True}
    
    stored = m.group(1)
    computed = compute_sha256(body)
    
    if stored == computed:
        return {'status': 'ok', 'stored': stored, 'computed': computed, 'has_frontmatter': True}
    else:
        return {'status': 'mismatch', 'stored': stored, 'computed': computed, 'has_frontmatter': True}


def check_raw_integrity(raw_dir: Path) -> dict:
    """Scan all raw files and return integrity report.
    
    Returns dict with:
      - total: int
      - no_fm: int
      - no_hash: int
      - ok: int
      - mismatch: int
      - mismatch_files: list of (filename, stored[:12], computed[:12])
    """
    result = {'total': 0, 'no_fm': 0, 'no_hash': 0, 'ok': 0, 'mismatch': 0, 'mismatch_files': []}
    
    if not raw_dir.exists() or not raw_dir.is_dir():
        return result
    
    for fn in sorted(raw_dir.rglob('*.md')):
        if fn.name == 'README.md':
            continue
        result['total'] += 1
        v = verify_file_hash(fn)
        status = v['status']
        if status == 'no_fm':
            result['no_fm'] += 1
        elif status == 'no_hash':
            result['no_hash'] += 1
        elif status == 'ok':
            result['ok'] += 1
        elif status == 'mismatch':
            result['mismatch'] += 1
            result['mismatch_files'].append((fn.name, v['stored'][:12], v['computed'][:12]))
    
    return result


def fix_file_hash(filepath: Path) -> bool:
    """Fix SHA256 in a file's frontmatter. Returns True if file was updated."""
    content = filepath.read_text(encoding='utf-8')
    fm, body = split_frontmatter(content)

    if fm is None:
        return False

    # Try to find a valid 64-char hex hash first
    m = re.search(r'sha256:\s*([a-f0-9]{64})', fm)
    if m is not None:
        stored = m.group(1)
        computed = compute_sha256(body.lstrip("\n"))
        if stored == computed:
            return False  # Already correct
        new_fm = fm.replace(f'sha256: {stored}', f'sha256: {computed}')
        new_content = f"---\n{new_fm}\n---\n{body}"
        filepath.write_text(new_content, encoding='utf-8')
        return True

    # No valid hex hash found — check for non-hex placeholders (e.g. "auto", "PLACEHOLDER")
    m2 = re.search(r'sha256:\s*(\S+)', fm)
    if m2 is not None:
        non_hex_val = m2.group(1)
        if not re.match(r'^[a-f0-9]{64}$', non_hex_val):
            # Replace non-hex value with computed hash
            computed = compute_sha256(body.lstrip("\n"))
            new_fm = re.sub(r'sha256:\s*\S+', f'sha256: {computed}', fm)
            new_content = f"---\n{new_fm}\n---\n{body}"
            filepath.write_text(new_content, encoding='utf-8')
            return True

    return False


def retry_for_status(url: str, headers: dict, max_retries: int = 3,
                     backoff: float = 2.0, status: int = 200):
    """Retry GET request on non-target status codes.
    
    Args:
        url: URL to fetch
        headers: Request headers
        max_retries: Max number of retries
        backoff: Initial backoff in seconds (exponential)
        status: Target status code to return
    
    Returns:
        requests.Response (200 on success, or last error response)
    """
    import requests
    
    last_resp = None
    for attempt in range(max_retries):
        try:
            resp = requests.get(url, timeout=10, headers=headers)
            if resp.status_code == status:
                return resp
            last_resp = resp
            if attempt < max_retries - 1:
                wait = backoff * (2 ** attempt)
                time.sleep(wait)
        except requests.exceptions.RequestException:
            last_resp = None
            if attempt < max_retries - 1:
                time.sleep(backoff * (2 ** attempt))
    
    return last_resp or requests.Response()
