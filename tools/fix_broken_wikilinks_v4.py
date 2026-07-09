#!/usr/bin/env python3
"""Fix broken wikilinks by finding best matching existing page."""
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path("/workspace/llm-wiki/wiki")

def normalize_wikilink(wl):
    """Normalize a wikilink text to match page stem format."""
    s = wl.strip()
    s = re.sub(r'[^a-zA-Z0-9\u0400-\u04FF\u0600-\u06FF]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    s = s.lower()
    s = re.sub(r' ', '-', s)
    s = s.strip('-')
    return s

def get_stem_base(stem):
    """Get the base stem without date/version suffixes."""
    s = re.sub(r'_[0-9]{4}-[0-9]{2}-[0-9]{2}$', '', stem)
    s = re.sub(r'_[0-9]+$', '', s)
    return s

# Build stem map: normalized base -> list of actual stems
pages = list(ROOT.rglob("*.md"))
stem_map = defaultdict(list)
for p in pages:
    base = get_stem_base(p.stem)
    norm = normalize_wikilink(base)
    if norm:
        stem_map[norm].append(p.stem)

# Also build a fuzzy map: for stems that don't match exactly
# e.g. "explainable-ai-07" should match "explainable-ai"
fuzzy_map = {}
for norm, stems in stem_map.items():
    # Also try without trailing -XX
    parts = norm.rsplit('-', 1)
    if len(parts) == 2 and parts[1].isdigit():
        partial = parts[0]
        if partial not in fuzzy_map:
            fuzzy_map[partial] = stems

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

def find_best_match(wl):
    """Find the best matching page stem for a wikilink."""
    norm = normalize_wikilink(wl)
    
    # Exact match
    if norm in stem_map:
        stems = stem_map[norm]
        # Prefer non-suffixed files first
        for s in stems:
            if not re.search(r'_\d+$', s):
                return s
        return stems[0]
    
    # Fuzzy match (without trailing -XX)
    if norm in fuzzy_map:
        stems = fuzzy_map[norm]
        for s in stems:
            if not re.search(r'_\d+$', s):
                return s
        return stems[0]
    
    # Try partial: remove trailing words
    parts = norm.split('-')
    for i in range(len(parts) - 1, 0, -1):
        partial = '-'.join(parts[:i])
        if partial in stem_map:
            stems = stem_map[partial]
            for s in stems:
                if not re.search(r'_\d+$', s):
                    return s
            return stems[0]
    
    return None

# Debug: show what each remaining wikilink matches
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

print("=== Fix resolution ===")
for wl in remaining:
    match = find_best_match(wl)
    norm = normalize_wikilink(wl)
    print(f"  '{wl}' -> '{norm}' -> match: {match}")
