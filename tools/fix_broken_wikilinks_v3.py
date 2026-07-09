#!/usr/bin/env python3
"""Fix broken wikilinks with correct normalization."""
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path("/workspace/llm-wiki/wiki")

def normalize_wikilink(wl):
    """Normalize a wikilink text to match page stem format."""
    s = wl.strip()
    # Replace all non-alphanumeric with spaces first
    s = re.sub(r'[^a-zA-Z0-9\u0400-\u04FF\u0600-\u06FF]', ' ', s)
    # Collapse spaces
    s = re.sub(r'\s+', ' ', s).strip()
    # Lowercase
    s = s.lower()
    # Replace spaces with dashes
    s = re.sub(r' ', '-', s)
    # Remove leading/trailing dashes
    s = s.strip('-')
    return s

def get_stem_base(stem):
    """Get the base stem without date/version suffixes."""
    s = re.sub(r'_[0-9]{4}-[0-9]{2}-[0-9]{2}$', '', stem)
    s = re.sub(r'_[0-9]+$', '', s)
    return s

# Build stem map: normalized -> list of actual stems
pages = list(ROOT.rglob("*.md"))
stem_map = defaultdict(list)
for p in pages:
    base = get_stem_base(p.stem)
    norm = normalize_wikilink(base)
    if norm:
        stem_map[norm].append(p.stem)

# External links
EXTERNAL_PATTERNS = [
    r'^view\s*email$',
    r'^moving\s*to\s*substack$',
    r'^arxiv[:\s]',
    r'^arXiv[:\s]',
    r'^https?://',
]

def is_external(wl):
    for pat in EXTERNAL_PATTERNS:
        if re.match(pat, wl, re.IGNORECASE):
            return True
    return False

# Debug: show what each remaining wikilink normalizes to
remaining = [
    'generative ai and ai product moats',
    'applying large language models cohere',
    'explainable ai',
    'llm-fine-tuning-lora-qlora-dpo',
    'LLM Deployment Q&A — Common Questions',
    'Advanced Prompt Engineering Techniques',
    'Automating Ai Away',
    'Automating Ai Away 2026 07 07',
    'Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots',
    'How to Use Cloudflare Workers AI REST API',
    'Open Source LLM Landscape Llama vs Mistral vs Qwen',
    'How to Engineer Prompts — Step-by-Step',
    'AI Coding Assistants Landscape',
    'Applying Massive Language Models In The Real World With Cohere 2026 07 07',
    'away',
    'hidden states',
    'open-source-llm-landscape',
    'Llama vs Mistral vs Qwen — Open Source LLM Comparison',
    'AI Agent Frameworks LangGraph vs CrewAI vs AutoGen Compared',
    'Generative Ai And Ai Product Moats',
    'robots txt 2023 war memorial',
    'Object Centric Environment Modeling For Agentic Tasks',
    'Medcalc Pro Solving Complex Medical Calculations With Llm Agents',
    'Best AI Coding Assistants as of March 2026',
    'Open Source LLM Landscape 2026: Llama vs Mistral vs Qwen',
    'LLM Landscape 2026 — Multi-Source Synthesis',
    'wikilinks',
    'wiki-links',
    'karpathy',
    '12 Advanced RAG Techniques Beyond Naive Retrieval',
]

print("=== Normalization debug ===")
for wl in remaining:
    norm = normalize_wikilink(wl)
    matches = stem_map.get(norm, [])
    print(f"  '{wl}' -> '{norm}' -> matches: {matches[:3]}")

# Check all existing stems
print("\n=== All normalized stems (sample) ===")
for norm, stems in sorted(stem_map.items()):
    if 'generative' in norm or 'explainable' in norm or 'llm-fine' in norm:
        print(f"  '{norm}' -> {stems[:2]}")
