---
title: "Wiki Schema — OKF v0.1"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - alignment
  - architecture
  - automation
  - benchmark
  - cloud
  - comparison
  - compliance
  - cost
  - data
  - deep-learning
  - deployment
  - distributed
  - dpo
  - efficiency
  - evaluation
  - few-shot
  - fine-tuning
  - foundation-model
  - gpt
  - hardware
  - image-generation
  - integration
  - llama
  - llm
  - lora
  - machine-learning
  - mistral
  - multi-agent
  - multimodal
  - nlp
  - open-source
  - playbook
  - policy
  - prompt-engineering
  - prompt-tuning
  - qlora
  - quantization
  - rag
  - reinforcement-learning
  - research
  - retrieval
  - review
  - rlhf
  - self-supervised
  - semi-supervised
  - serverless
  - sft
  - stable-diffusion
  - standards
  - supervised
  - synthesis
  - training
  - transfer-learning
  - transformers
  - use-case
  - workflow
  - zero-shot
---
# Wiki Schema — OKF v0.1

> **Source:** schema-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: local:///workspace/llm-wiki/SCHEMA.md ingested: 2026-07-10 sha256: 9f9c36e0d6061f708ec3d70e41e94eed31fc5597eb60630ab6b87af5ff4e7771 blog_source: local --- --- type: reference title: LL...
> **Sources:**
>   - schema-2026-07-10.md
> **Links:**
- [[wiki-log]]
- [[local-llm-wiki-algorithm]]
- [[llm-wiki-index]]
- [[llm-wiki]]
- [[llm-fine-tuning]]

## Key Findings

---
source_url: local:///workspace/llm-wiki/SCHEMA.md
ingested: 2026-07-10
sha256: 9f9c36e0d6061f708ec3d70e41e94eed31fc5597eb60630ab6b87af5ff4e7771
blog_source: local
---

# Wiki Schema — OKF v0.1
## OKF v0.1 Compliance
This wiki conforms to the [Open Knowledge Format v0.1](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing):
| OKF Field | Required? | Coverage |
|-----------|:---------:|----------|
| `type` | ✅ required | 219/219 (100%) |
| `title` | optional | 219/219 (100%) |
| `description` | optional | 209/219 (95%) |
| `tags` | optional | 117/219 (53%) |
| `resource` | optional | 0/219 (0%) |
| `timestamp` | optional | 0/219 (0%) |
### OKF Field Mapping
| OKF Spec | Our Field | Notes |
|----------|-----------|-------|
| `type` | `type` | Direct mapping |
| `title` | `title` | Direct mapping |
| `description` | `description` | Direct mapping |
| `tags` | `tags` | Direct mapping |
| `timestamp` | `created` + `updated` | Split into creation/update dates |
| `resource` | (not used) | Reserved for external resources |
### OKF Extensions (Non-Standard Fields)
OKF is minimally opinionated — additional fields are allowed:
| Field | Purpose |
|-------|---------|
| `category` | Wiki section (entities, concepts, comparisons, etc.) |
| `confidence` | Quality signal: high/medium/low |
| `contested` | Boolean — unresolved contradictions |
| `links` | Markdown links to related pages |
| `sources` | Raw source file references |
| `status` | Workflow status (draft, completed, archived) |
## Conventions
- **File names:** lowercase, hyphens, no spaces (e.g., `transformer-architecture.md`)
- **Frontmatter:** Every wiki page starts with YAML frontmatter (see below)
- **Wikilinks:** Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- **Updates:** When updating a page, always bump the `updated` date
- **Index:** Every new page must be added to `index.md` under the correct section
- **Log:** Every action must be appended to `log.md`
- **Provenance:** On pages synthesizing 3+ sources, append `^[raw/articles/source-file.md]` at end of paragraphs with source-specific claims
## Frontmatter
```yaml

```
## Tag Taxonomy — 184 Tags
### AI/ML Core (48 tags)
| Tag | Tag | Tag | 

## Summary

Tag |
|-----|-----|-----|-----|
| `ai-agents` | `ai-benchmark` | `ai-education` | `ai-infrastructure` |
| `ai-integration` | `ai-safety` | `ai-workforce` | `alignment` |
| `architecture` | `architecture-design` | `auto-ml` | `automation` |
| `benchmark` | `bias-mitigation` | `clarification` | `comparison` |
| `concept` | `conditional-generation` | `consistency-regularization` | `constitutional-ai` |
| `contrastive-loss` | `controllability` | `cost-economics` | `cot` |
| `data-efficiency` | `data-quality` | `deepseek` | `deployment` |
| `diffusion` | `distributed-training` | `dpo` | `dqn` |
| `efficiency` | `embeddings` | `embodied-ai` | `evaluation` |
| `explainable-ai` | `exploration` | `few-shot` | `fine-tuning` |
| `generative-models` | `glm` | `gpt` | `graph-neural-networks` |
| `in-context-learning` | `inference` | `language-model` | `llama` |
| `lora` | `model` | `multimodal` | `nlp` |
| `open-source-llm` | `peft` | `planning` | `policy` |
| `policy-gradient` | `prompt-engineering` | `qa` | `qlora` |
| `quantization` | `rag` | `reinforcement-learning` | `representation-learning` |
| `reproducibility` | `retrieval` | `rlhf` | `serving` |
| `self-consistency` | `self-supervised` | `self-training` | `semi-supervised` |
| `sft` | `text-generation` | `zero-shot` | |
### Infrastructure & Systems (19 tags)
| Tag | Tag | Tag | Tag |
|-----|-----|-----|-----|
| `assembly` | `cloudflare` | `configuration` | `data-engineering` |
| `data-parallelism` | `hardware` | `helk` | `inference-chip` |
| `knowledge-base` | `local-llm-hardware` | `mcp` | `model-parallelism` |
| `object-centric` | `orchestration` | `rtx-5070-ti` | `serverless` |
| `vllm` | | | |
### Methods & Techniques (20 tags)
| Tag | Tag | Tag | Tag |
|-----|-----|-----|-----|
| `active-learning` | `advanced-rag` | `agent-workflow` | `agentic-tasks` |
| `auto-ml` | `configuration` | `duplicates` | `feature-attribution` |
| `language-action` | `mixed-precision` | `nas` | `next-gen` |
| `partial-observability` | `style-transfer` | `swrl` | `tot` |
| `xai` | | | |
### Evaluation & Benchmarks (12 tags)
| Tag | Tag | Tag | Tag |
|-----|-----|-----|-----|
| `entity` | `mmlu` | `mt-bench` | `open-domain` |
| `pairwise-comparison` | `reliability` | `replication` | `robustness` |
| `safety` | `truthfulqa` | `uncertainty` | `verification` |
### Applications & Domains (18 tags)
| Tag | Tag | Tag | Tag |
|-----|-----|-----|-----|
| `analytics` | `bioinformatics` | `clinical-decision-support` | `coding-agents` |
| `drug-discovery` | `enterprise` | `enterprise-ai` | `environment-modeling` |
| `faq` | `genebench-pro` | `genomics` | `healthcare` |
| `image-generation` | `labor-market` | `manufacturing` | `medical-calculation` |
| `multi-agent` | `scientific-ai` | `scientific-research` | `swarm-intelligence` |
| `toxicity` | `toxicity-reduction` | `visualization` | |
### Companies & Products (10 tags)
| Tag | Tag | Tag | Tag |
|-----|-----|-----|-----|
| `broadcom` | `chatgpt` | `gemma` | `hp` |
| `iFLYTEK` | 

## Related Articles

- [[wiki-log]]
- [[local-llm-wiki-algorithm]]
- [[llm-wiki-index]]
- [[llm-wiki]]
- [[llm-fine-tuning]]
