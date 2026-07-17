---
source_url: https://github.com/kandr-kiev/llm-wiki/wiki/entities
ingested: 2026-07-18
sha256: a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2
summary: "Chinese AI Labs Overview — DeepSeek, Kimi (Moonshot AI), Z.ai (Zhipu AI), Qwen (Alibaba): the four major Chinese open-weight model providers challenging US dominance"
---
# 🇨🇳 Chinese AI Labs Overview — DeepSeek, Kimi, Z.ai, Qwen

> **Last updated:** 2026-07-18 | **Type:** Company overview / competitive landscape

## The Four Giants of Chinese Open-Source AI

Four Chinese AI companies are leading the global open-weight revolution, each with distinct strengths and architectures:

### 1. DeepSeek (深度求索) — Cost Innovation Leader

- **Founded:** January 2023 by Liang Wenfeng (High-Flyer Quantitative)
- **Flagship:** DeepSeek-V4-Pro (1.6T MoE, 49B active, 1M context)
- **Key Innovation:** MoE with deep sparse routing, MLA, MPO
- **Compute:** Domestic GPUs (Huawei Ascend) under US Entity List
- **Pricing:** ~$0.14/M input tokens — orders of magnitude cheaper than US competitors
- **GitHub:** `deepseek-ai/DeepSeek-V4`, `deepseek-ai/DeepGEMM`, `deepseek-ai/FlashMLA`
- **HuggingFace:** `deepseek-ai/DeepSeek-V4-Pro`, `deepseek-ai/DeepSeek-V4-Flash`
- **Entity:** [[deepseek]]

### 2. Kimi / Moonshot AI (月之暗面) — Agentic & Coding Leader

- **Founded:** 2023 by Yang Zhilin (Tsinghua professor, ex-Google Brain)
- **Flagship:** Kimi K2.7-Code (1T MoE, coding-focused, +21.8% on Code Bench v2)
- **Key Innovation:** Native multimodal, agentic capabilities, Muon optimizer
- **Breakthrough:** First open-weight model in GitHub Copilot (July 2026)
- **GitHub:** `MoonshotAI/Kimi-K2.6`, `MoonshotAI/Kimi-K2.7-Code`
- **HuggingFace:** `moonshotai/Kimi-K2.6`, `moonshotai/Kimi-K2.7-Code`
- **Entity:** [[kimi]]

### 3. Z.ai / Zhipu AI (智谱AI) — Academic Excellence

- **Founded:** 2021 by Tsinghua KEG Lab professors
- **Flagship:** GLM-5.2 (744B MoE, 40B active, 1M context, SWE-bench Pro: 81.0)
- **Key Innovation:** #1 open-weight on Artificial Analysis, MIT license
- **Public:** Listed on HKEX as "Knowledge Atlas Technology"
- **GitHub:** `zai-org/GLM-5`, `zai-org/SCAIL-2`, `zai-org/Vision2Web`
- **HuggingFace:** `zai-org/GLM-5.2`, `zai-org/GLM-5.1`
- **Entity:** [[glm]]

### 4. Qwen / Alibaba — Ecosystem Scale Leader

- **Company:** Alibaba Cloud Intelligence
- **Flagship:** Qwen3.6-35B-A3B (35B MoE, 3B active) — most popular size
- **Scale:** 100M+ downloads on HuggingFace, 29+ languages
- **GitHub:** `QwenLM/Qwen3.6`, `QwenLM/Qwen3-VL`, `QwenLM/qwen-code`
- **HuggingFace:** `Qwen/Qwen3.6-35B-A3B`, `Qwen/Qwen3.5-397B-A17B`
- **Entity:** [[qwen]]

## Competitive Landscape

| Company | Flagship | Architecture | Key Differentiator |
|---|---|---|---|
| DeepSeek | V4-Pro (1.6T) | MoE deep sparse routing | Cost efficiency, pricing |
| Kimi | K2.7-Code (1T) | MoE + Muon | Agentic, GitHub Copilot integration |
| Z.ai | GLM-5.2 (744B) | MoE (40B active) | Academic pedigree, SWE-bench Pro |
| Qwen | 3.6-35B-A3B | MoE (3B active) | Ecosystem scale, downloads |

## Common Challenges

- **US Entity List** (Jan 2025): All four restricted from NVIDIA H100/H200 GPUs
- **Training Hardware:** All rely on domestic Chinese GPUs (Huawei Ascend 910B)
- **Data Scraping:** Training on copyrighted content — subject to legal challenges
- **Open-Weight Safety:** Global debate on open-weight model implications

## Cross-References

- [[deepseek]]
- [[kimi]]
- [[glm]]
- [[qwen]]
- [[openai]]
- [[anthropic]]
- [[hugging-face]]
