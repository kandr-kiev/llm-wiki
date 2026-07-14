---
type: reference
title: LLM Wiki Schema
description: OKF v0.1 compliant schema defining conventions, structure rules, and tag taxonomy for the LLM Wiki knowledge base
created: 2026-07-10
updated: 2026-07-10
tags: [schema, okf, llm-wiki, knowledge-base]
sources: []
confidence: high
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
---
title: Page Title
type: entity | concept | comparison | query | reference | playbook | synthesis
category: entities | concepts | comparisons | queries | references | playbooks | synthesis
tags: [from taxonomy below]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [raw/articles/source-name.md]
# Optional quality signals:
confidence: high | medium | low
contested: true
links: [related-page]
status: draft | completed | archived
---
```

## Tag Taxonomy — 184 Tags

### AI/ML Core (48 tags)

| Tag | Tag | Tag | Tag |
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
| `llm-agents` | `context-window` | `moe` | `hermes-agent` |
| `interpretability` | `model-auditing` | `agent-skills` | `ai-coding` |
| `code-architecture` | `process-improvement` | `tdd` | `code-quality` |
| `critical-analysis` | | | |

### Infrastructure & Systems (19 tags)

| Tag | Tag | Tag | Tag |
|-----|-----|-----|-----|
| `assembly` | `cloudflare` | `configuration` | `data-engineering` |
| `data-parallelism` | `hardware` | `helk` | `inference-chip` |
| `knowledge-base` | `local-llm-hardware` | `mcp` | `model-parallelism` |
| `object-centric` | `orchestration` | `rtx-5070-ti` | `serverless` |
| `vllm` | `ml-infrastructure` | | |

### Methods & Techniques (20 tags)

| Tag | Tag | Tag | Tag |
|-----|-----|-----|-----|
| `active-learning` | `advanced-rag` | `agent-workflow` | `agentic-tasks` |
| `auto-ml` | `configuration` | `duplicates` | `feature-attribution` |
| `language-action` | `mixed-precision` | `nas` | `next-gen` |
| `partial-observability` | `style-transfer` | `swrl` | `tot` |
| `xai` | `scheduling` | | |

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
| `toxicity` | `toxicity-reduction` | `visualization` | `robotics` |
| `software-engineering` | | | |

### Companies & Products (10 tags)

| Tag | Tag | Tag | Tag |
|-----|-----|-----|-----|
| `broadcom` | `chatgpt` | `gemma` | `hp` |
| `iFLYTEK` | `mistral` | `openai` | `qwen` |
| `sol` | `stable-diffusion` | | |

### Research & Meta (15 tags)

| Tag | Tag | Tag | Tag |
|-----|-----|-----|-----|
| `arxiv` | `hermes` | `ingest` | `integrity` |
| `llm-assistance` | `llm-benchmarks` | `llm-wiki` | `ml` |
| `okf` | `reference` | `schema` | `source` |
| `synthesis` | `tools` | `wiki-maintenance` | `trends` |

### Wiki Operations (14 tags)

| Tag | Tag | Tag | Tag |
|-----|-----|-----|-----|
| `adoption` | `europe` | `local` | `partnership` |
| `playbook` | `pluralism` | `productivity` | `query-strategy` |
| `skills-gap` | `swrl` | `trust` | `user-metrics` |
| `wikilinks` | `workflow` | | |
| `indexer` | `audit` | `cron` | `integrator` |
| `monitors` | `scripts` | `system-audit` | `system-integrity` |
| `obsidian` | `wiki` | | |

### Extended Tags (from wiki usage)

| Tag | Tag | Tag | Tag |
|-----|-----|-----|-----|
| `agent` | `ai` | `analysis` | `application` |
| `async` | `awq` | `best-practice` | `business-process` |
| `ci-cd` | `claude` | `clinical` | `closed-source` |
| `cloud` | `company` | `computer-vision` | `cost` |
| `data` | `decision` | `design-pattern` | `digest` |
| `distributed` | `edge` | `embedding` | `event` |
| `foundation-model` | `framework` | `gemini` | `gguf` |
| `governance` | `gptq` | `gpu` | `guide` |
| `health-check` | `instruction-tuning` | `integration` | `library` |
| `lint` | `llm` | `machine-learning` | `meeting` |
| `milestone` | `mobile` | `news` | `online` |
| `open-source` | `optimization` | `parallel` | `performance` |
| `pipeline` | `prompt-tuning` | `query` | `real-time` |
| `research` | `scalability` | `search` | `security` |
| `source-management` | `storage` | `supervised` | `system-design` |
| `training` | `transfer-learning` | `use-case` | `vector-database` |
| `web` | | | |

### Page Thresholds

- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

### Update Policy

When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contested: true`
4. Flag for user review
