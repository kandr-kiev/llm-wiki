#!/usr/bin/env python3
"""Fix broken wikilinks with fuzzy matching."""
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path("/workspace/llm-wiki/wiki")

def normalize_wikilink(wl):
    s = re.sub(r'[^a-zA-Z0-9\u0400-\u04FF\u0600-\u06FF]', ' ', wl.strip())
    s = re.sub(r'\s+', ' ', s).strip().lower()
    s = re.sub(r' ', '-', s).strip('-')
    return s

def get_stem_base(stem):
    s = re.sub(r'_[0-9]{4}-[0-9]{2}-[0-9]{2}$', '', stem)
    s = re.sub(r'_[0-9]+$', '', s)
    return s

def stem_to_norm(stem):
    base = get_stem_base(stem)
    return normalize_wikilink(base)

# Build maps
pages = list(ROOT.rglob("*.md"))

# Direct: norm -> stem (prefer non-suffixed)
direct_map = {}
for p in pages:
    norm = stem_to_norm(p.stem)
    if norm and norm not in direct_map:
        direct_map[norm] = p.stem

# Fuzzy: try stripping trailing -XX from normalized form
fuzzy_map = {}
for norm, stem in direct_map.items():
    # Strip trailing -number patterns
    m = re.match(r'^(.+?)-(\d{1,3})$', norm)
    if m:
        partial = m.group(1)
        if partial not in fuzzy_map:
            fuzzy_map[partial] = stem
    # Strip multiple trailing -XX
    curr = norm
    while True:
        m = re.match(r'^(.+?)-(\d{1,3})$', curr)
        if not m:
            break
        partial = m.group(1)
        if partial not in fuzzy_map:
            fuzzy_map[partial] = stem
        curr = partial

# Also try without the first word (for long wikilinks)
word_map = {}
for norm, stem in direct_map.items():
    parts = norm.split('-')
    for i in range(1, len(parts)):
        partial = '-'.join(parts[i:])
        if partial not in word_map:
            word_map[partial] = stem

def find_best_match(wl):
    norm = normalize_wikilink(wl)
    
    # 1. Exact match
    if norm in direct_map:
        return direct_map[norm]
    
    # 2. Fuzzy (strip trailing -XX)
    if norm in fuzzy_map:
        return fuzzy_map[norm]
    
    # 3. Strip first word
    parts = norm.split('-')
    for i in range(1, len(parts)):
        partial = '-'.join(parts[i:])
        if partial in word_map:
            return word_map[partial]
    
    return None

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

# Debug all remaining
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

print("=== Resolution debug ===")
for wl in remaining:
    match = find_best_match(wl)
    norm = normalize_wikilink(wl)
    print(f"  '{wl}' -> '{norm}' -> {match}")
