#!/usr/bin/env python3
"""Structural lint for Local LLM Wiki."""
from pathlib import Path
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"type", "title", "description", "created", "updated", "tags", "sources", "confidence", "links"}
APPROVED_TAGS = {
    "active-learning", "adoption", "agent-workflow", "agentic-tasks", "ai-agents", "ai-benchmark", "ai-education", "ai-infrastructure",
    "ai-integration", "ai-safety", "ai-workforce", "alignment", "analytics", "architecture", "architecture-design", "arxiv",
    "assembly", "auto-ml", "automation", "benchmark", "bias-mitigation", "bioinformatics", "broadcom", "business-process",
    "chatgpt", "clarification", "clinical-decision-support", "cloudflare", "coding-agents", "company", "comparison", "concept",
    "conditional-generation", "configuration", "consistency-regularization", "contrastive-loss", "controllability", "cost-economics", "cot", "data-efficiency",
    "data-engineering", "data-parallelism", "data-quality", "decision", "deepseek", "deployment", "diffusion", "digest",
    "distributed-training", "dpo", "dqn", "drug-discovery", "efficiency", "embeddings", "embodied-ai", "enterprise",
    "enterprise-ai", "entity", "environment-modeling", "europe", "evaluation", "event", "explainable-ai", "exploration",
    "faq", "feature-attribution", "few-shot", "fine-tuning", "gemma", "genebench-pro", "generative-models", "genomics",
    "glm", "gpt", "graph-neural-networks", "hardware", "health-check", "healthcare", "helk", "hermes",
    "hp", "iFLYTEK", "image-generation", "in-context-learning", "indexer", "inference", "inference-chip", "ingest", "interpretability",
    "constitutional-ai",
    "vllm",
    "advanced-rag",
    "knowledge-base", "labor-market", "language-action", "language-model", "lint", "llama", "llm-agents", "llm-assistance",
    "llm-benchmarks", "llm-wiki", "local", "local-llm-hardware", "lora", "manufacturing", "mcp", "medical-calculation",
    "meeting", "milestone", "mistral", "mixed-precision", "ml", "ml-infrastructure", "mmlu", "model",
    "model-auditing", "model-parallelism", "mt-bench", "multi-agent", "multimodal", "nas", "next-gen", "nlp",
    "object-centric", "obsidian", "okf", "open-domain", "open-source-llm", "openai", "orchestration", "pairwise-comparison",
    "partial-observability", "partnership", "peft", "planning", "playbook", "pluralism", "policy", "policy-gradient",
    "productivity", "prompt-engineering", "qa", "quantization", "qlora", "query", "query-strategy", "qwen", "rag",
    "reference", "reinforcement-learning", "reliability", "replication", "representation-learning", "reproducibility", "retrieval", "rlhf",
    "robotics", "robustness", "rtx-5070-ti", "safety", "scheduling", "schema", "scientific-ai", "scientific-research",
    "self-consistency", "self-supervised", "self-training", "semi-supervised", "serverless", "serving", "sft", "skills-gap", "software-engineering",
    "sol", "source", "source-management", "stable-diffusion", "storage", "style-transfer", "swarm-intelligence", "swrl",
    "synthesis", "text-generation", "tot", "toxicity", "toxicity-reduction", "trust", "truthfulqa", "uncertainty", "user-metrics",
    "verification", "visualization", "wiki", "workflow", "xai", "zero-shot"
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
    for raw in fm.splitlines():
        line = raw.strip()
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
        else:
            data[key] = value.strip('"\'')
    return data


def slug_for(path):
    return path.stem


def main():
    issues = []
    wiki_pages = [p for p in (ROOT / "wiki").rglob("*.md") if p.name not in RESERVED_NAMES and p.parent.name != "templates"]
    slugs = {slug_for(p): p for p in wiki_pages}
    index_text = (ROOT / "index.md").read_text(encoding="utf-8") if (ROOT / "index.md").exists() else ""

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
        if f"[[{page.stem}]]" not in index_text:
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
        for src in data.get("sources", []):
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
