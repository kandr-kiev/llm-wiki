#!/usr/bin/env python3
"""Fix all remaining broken wikilinks in wiki pages."""
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
direct_map = {}
for p in pages:
    norm = stem_to_norm(p.stem)
    if norm and norm not in direct_map:
        direct_map[norm] = p.stem

fuzzy_map = {}
for norm, stem in direct_map.items():
    curr = norm
    while True:
        m = re.match(r'^(.+?)-(\d{1,3})$', curr)
        if not m:
            break
        partial = m.group(1)
        if partial not in fuzzy_map:
            fuzzy_map[partial] = stem
        curr = partial

word_map = {}
for norm, stem in direct_map.items():
    parts = norm.split('-')
    for i in range(1, len(parts)):
        partial = '-'.join(parts[i:])
        if partial not in word_map:
            word_map[partial] = stem

prefix_map = {}
for norm, stem in direct_map.items():
    parts = norm.split('-')
    for i in range(1, len(parts) - 1):
        prefix = '-'.join(parts[:i])
        if prefix not in prefix_map:
            prefix_map[prefix] = stem

def find_best_match(wl):
    norm = normalize_wikilink(wl)
    if norm in direct_map:
        return direct_map[norm]
    if norm in fuzzy_map:
        return fuzzy_map[norm]
    parts = norm.split('-')
    for i in range(1, len(parts)):
        partial = '-'.join(parts[i:])
        if partial in word_map:
            return word_map[partial]
    for i in range(1, len(parts) - 1):
        prefix = '-'.join(parts[:i])
        if prefix in prefix_map:
            return prefix_map[prefix]
    return None

# Wikilinks to fix: (original, replacement)
# Manual overrides for tricky cases
WIKILINK_FIXES = {
    # Direct mappings from debug output
    'generative ai and ai product moats': 'generative-ai-and-ai-product-moats_07_1',
    'applying large language models cohere': 'applying-large-language-models-cohere_07_1',
    'explainable ai': 'explainable-ai_07_1',
    'llm-fine-tuning-lora-qlora-dpo': 'llm-fine-tuning-lora-qlora-dpo-2026',
    'LLM Deployment Q&A — Common Questions': 'llm-deployment-qa',
    'Advanced Prompt Engineering Techniques': 'advanced-prompt-engineering-techniques_2026_1',
    'Automating Ai Away': 'automating-ai-away-2026-07-07_1',
    'Automating Ai Away 2026 07 07': 'automating-ai-away-2026-07-07_1',
    'Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots': 'sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07_4',
    'How to Use Cloudflare Workers AI REST API': 'how-to-use-cloudflare-workers-ai',
    'Open Source LLM Landscape Llama vs Mistral vs Qwen': 'llama-vs-mistral-vs-qwen',
    'How to Engineer Prompts — Step-by-Step': 'how-to-engineer-prompts',
    'AI Coding Assistants Landscape': 'ai-coding-assistants',
    'Applying Massive Language Models In The Real World With Cohere 2026 07 07': 'applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07_1',
    'away': 'away_07_1',
    'hidden states': 'hidden-states_07_1',
    'open-source-llm-landscape': 'open-source-llm-landscape-2026',
    'Llama vs Mistral vs Qwen — Open Source LLM Comparison': 'llama-vs-mistral-vs-qwen',
    'AI Agent Frameworks LangGraph vs CrewAI vs AutoGen Compared': 'ai-agent-frameworks-langgraph-vs-crewai-vs-autogen-compared_2026_1',
    'Generative Ai And Ai Product Moats': 'generative-ai-and-ai-product-moats_07_1',
    'robots txt 2023 war memorial': 'robots-txt-2023-war-memorial_07_1',
    'Object Centric Environment Modeling For Agentic Tasks': 'object-centric-environment-modeling-for-agentic-tasks-2026-07-07_1',
    'Medcalc Pro Solving Complex Medical Calculations With Llm Agents': 'medcalc-pro-solving-complex-medical-calculations-with-llm-agents-2026-07-07_1',
    'Best AI Coding Assistants as of March 2026': 'best-ai-coding-assistants-as-of-march_2026_1',
    'Open Source LLM Landscape 2026: Llama vs Mistral vs Qwen': 'llama-vs-mistral-vs-qwen',
    'LLM Landscape 2026 — Multi-Source Synthesis': 'ai-agents-2026-synthesis',
    '12 Advanced RAG Techniques Beyond Naive Retrieval': '12-advanced-rag-techniques-beyond-naive-retrieval_2026_1',
    # Unresolvable - remove these
    'wikilinks': None,
    'wiki-links': None,
    'karpathy': None,
}

# External links to skip
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

# Collect all broken wikilinks from all files
broken_count = 0
fixed_count = 0
removed_count = 0

for p in pages:
    content = p.read_text(encoding='utf-8')
    original = content
    
    # Find all [[wikilinks]]
    for m in re.finditer(r'\[\[([^\]]+)\]\]', content):
        wl_text = m.group(1)
        
        # Skip external links
        if is_external(wl_text):
            continue
        
        # Check if it's in our fix list
        if wl_text in WIKILINK_FIXES:
            replacement = WIKILINK_FIXES[wl_text]
            if replacement is None:
                # Remove unresolvable wikilink
                content = content.replace(f'[[{wl_text}]]', '')
                removed_count += 1
            else:
                content = content.replace(f'[[{wl_text}]]', f'[[{replacement}]]')
                fixed_count += 1
        else:
            # Try fuzzy match
            match = find_best_match(wl_text)
            if match:
                content = content.replace(f'[[{wl_text}]]', f'[[{match}]]')
                fixed_count += 1
            else:
                broken_count += 1
    
    if content != original:
        p.write_text(content, encoding='utf-8')

print(f"Fixed: {fixed_count}")
print(f"Removed (unresolvable): {removed_count}")
print(f"Still broken: {broken_count}")
