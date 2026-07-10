#!/usr/bin/env python3
"""Structural lint for Local LLM Wiki."""
from pathlib import Path
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"type", "title", "description", "created", "updated", "tags", "sources", "confidence", "links"}
APPROVED_TAGS = {
    "active-learning", "adoption", "agent", "agent-workflow", "agentic-tasks", "ai", "ai-agents", "ai-benchmark", "ai-education", "ai-infrastructure",
    "ai-integration", "ai-safety", "ai-workforce", "alignment", "analytics", "analysis", "application", "architecture", "architecture-design", "arxiv",
    "assembly", "async", "auto-ml", "automation", "awq", "benchmark", "bias-mitigation", "bioinformatics", "best-practice", "broadcom", "business-process",
    "chatgpt", "ci-cd", "clarification", "claude", "clinical", "clinical-decision-support", "closed-source", "cloud", "cloudflare", "coding-agents", "company", "comparison", "concept",
    "computer-vision", "conditional-generation", "configuration", "consistency-regularization", "contrastive-loss", "controllability", "cost", "cost-economics", "cot", "data", "data-efficiency",
    "data-engineering", "data-parallelism", "data-quality", "decision", "deepseek", "deployment", "design-pattern", "diffusion", "digest",
    "distributed", "distributed-training", "dpo", "dqn", "drug-discovery", "duplicates", "efficiency", "embedding", "embeddings", "embodied-ai", "edge", "enterprise",
    "enterprise-ai", "entity", "environment-modeling", "europe", "evaluation", "event", "explainable-ai", "exploration",
    "faq", "feature-attribution", "few-shot", "fine-tuning", "framework", "foundation-model", "gemma", "genebench-pro", "generative-models", "genomics",
    "gemini", "gguf", "glm", "gpt", "gptq", "graph-neural-networks", "gpu", "guide", "governance", "hardware", "health-check", "healthcare", "helk", "hermes",
    "hp", "iFLYTEK", "image-generation", "in-context-learning", "indexer", "inference", "inference-chip", "ingest", "instruction-tuning", "integration", "integrity", "interpretability",
    "constitutional-ai",
    "vllm",
    "advanced-rag",
    "knowledge-base", "labor-market", "language-action", "language-model", "library", "lint", "llama", "llm", "llm-agents", "llm-assistance",
    "llm-benchmarks", "llm-wiki", "local", "local-llm-hardware", "lora", "machine-learning", "manufacturing", "mcp", "medical-calculation",
    "meeting", "milestone", "mistral", "mixed-precision", "ml", "ml-infrastructure", "mmlu", "model",
    "model-auditing", "model-parallelism", "mobile", "mt-bench", "multi-agent", "multimodal", "nas", "next-gen", "news", "nlp",
    "object-centric", "obsidian", "okf", "online", "open-domain", "open-source", "open-source-llm", "openai", "optimization", "orchestration", "pairwise-comparison",
    "partial-observability", "partnership", "parallel", "peft", "performance", "pipeline", "planning", "playbook", "pluralism", "policy", "policy-gradient",
    "productivity", "prompt-engineering", "prompt-tuning", "qa", "quantization", "qlora", "query", "query-strategy", "qwen", "rag",
    "real-time", "reference", "reinforcement-learning", "reliability", "replication", "representation-learning", "reproducibility", "retrieval", "research", "rlhf",
    "robotics", "robustness", "rtx-5070-ti", "safety", "scalability", "search", "scheduling", "schema", "scientific-ai", "scientific-research",
    "security", "self-consistency", "self-supervised", "self-training", "semi-supervised", "serverless", "serving", "sft", "skills-gap", "software-engineering",
    "sol", "source", "source-management", "stable-diffusion", "storage", "style-transfer", "supervised", "swarm-intelligence", "swrl",
    "synthesis", "system-design", "text-generation", "tools", "tot", "toxicity", "toxicity-reduction", "training", "transfer-learning", "trust", "truthfulqa", "uncertainty", "use-case", "user-metrics",
    "vector-database", "verification", "visualization", "web", "wikilinks", "wiki", "wiki-maintenance", "workflow", "xai", "zero-shot"
}
RESERVED_NAMES = {"README.md"}


def split_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end+5:]


def parse_simple_yaml(fm):
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
            # Multi-line YAML list (tags:, sources:)
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


def slug_for(path):
    return path.stem


def main():
    issues = []
    wiki_pages = [p for p in (ROOT / "wiki").rglob("*.md") if p.name not in RESERVED_NAMES and p.parent.name != "templates"]
    slugs = {slug_for(p): p for p in wiki_pages}
    index_text = (ROOT / "wiki" / "index.md").read_text(encoding="utf-8") if (ROOT / "wiki" / "index.md").exists() else ""

    for page in wiki_pages:
        text = page.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        rel = page.relative_to(ROOT)
        if fm is None:
            issues.append(("ERROR", str(rel), "missing or malformed frontmatter"))
            continue
        data = parse_simple_yaml(fm)
        missing = sorted(REQUIRED - set(data))
        if missing:
            issues.append(("ERROR", str(rel), "missing fields: " + ", ".join(missing)))
        for tag in data.get("tags", []):
            if tag not in APPROVED_TAGS:
                issues.append(("WARN", str(rel), f"unapproved tag: {tag}"))
        if str(rel) not in index_text and rel != Path("wiki/index.md"):
            issues.append(("ERROR", str(rel), "page missing from index.md"))
        if len(text.splitlines()) > 200:
            issues.append(("WARN", str(rel), "page over 200 lines"))
        if str(data.get("confidence", "")).lower() == "low":
            issues.append(("INFO", str(rel), "low confidence page"))
        if data.get("contested") is True:
            issues.append(("INFO", str(rel), "contested page"))
        # Strip HTML before checking wikilinks (prevents false positives from Astro JSON props)
        # NOTE: integrator may produce truncated files where astro-island tags are never closed.
        # Handle both complete tags (astro-island ... />) and truncated tags (astro-island ... EOF).
        # Strategy: remove everything from <astro-island to end of body, since it's never valid markdown.
        clean_body = re.sub(r'<astro-island\b.*', ' ', body, flags=re.DOTALL)
        # Then strip remaining HTML tags
        clean_body = re.sub(r'<[^>]+>', ' ', clean_body)
        for link in re.findall(r"\[\[([^\]|#]+)", clean_body):
            if link not in slugs:
                issues.append(("ERROR", str(rel), f"broken wikilink: [[{link}]]"))
        # Check that source files actually exist
        sources = data.get("sources", [])
        if isinstance(sources, str):
            sources = [sources]
        for src in sources:
            src_path = ROOT / src
            if not src_path.is_file():
                issues.append(("ERROR", str(rel), f"source file missing: {src}"))

    for raw in (ROOT / "raw").rglob("*.md"):
        if raw.name == "README.md":
            continue
        text = raw.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        rel = raw.relative_to(ROOT)
        if fm is None:
            issues.append(("ERROR", str(rel), "raw source missing frontmatter"))
            continue
        data = parse_simple_yaml(fm)
        expected = data.get("sha256")
        actual = hashlib.sha256(body.strip().encode("utf-8")).hexdigest()
        if expected != actual:
            issues.append(("ERROR", str(rel), "sha256 drift"))

    out = ROOT / "outputs" / "lint-report.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Local LLM Wiki Lint Report", "", f"Pages checked: {len(wiki_pages)}", f"Issues: {len(issues)}", ""]
    if issues:
        for severity, path, msg in issues:
            lines.append(f"- **{severity}** `{path}` — {msg}")
    else:
        lines.append("No structural issues found.")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    if any(sev == "ERROR" for sev, _, _ in issues):
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
