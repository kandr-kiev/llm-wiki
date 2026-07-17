#!/usr/bin/env python3
"""Central GitHub repository list for all monitors.

Single source of truth — edit here, all monitors inherit.
Replacements for 404/archived repos are listed inline.
"""

REPOS = [
    # Core AI/ML Frameworks
    "pytorch/pytorch",
    "tensorflow/tensorflow",
    "microsoft/DeepSpeed",
    # Hugging Face ecosystem
    "huggingface/transformers",
    "huggingface/diffusers",
    "huggingface/optimum",
    "huggingface/accelerate",
    "huggingface/peft",
    "huggingface/trl",
    "huggingface/tokenizers",        # Fast tokenizer library (Rust)
    "huggingface/datasets",          # Dataset hub & loaders
    "huggingface/safetensors",       # Safe tensor serialization format
    "huggingface/sentence-transformers", # Sentence embeddings
    "huggingface/optimum-habana",    # Intel Gaudi accelerator support
    # Inference & serving engines
    "vllm-project/vllm",             # High-throughput LLM serving
    "ollama/ollama",                 # Local model runner (172K+ stars)
    "ggml-org/llama.cpp",            # C/C++ local inference (100K+ stars, GGUF)
    # Model families
    "google-deepmind/gemma",         # Google Gemma series
    "meta-llama/llama-models",       # Meta Llama (replaces: meta-llama/llama 404)
    # QwenLM/Qwen3.6 removed — no releases (repo exists but empty)
    "mistralai/mistral-src",         # Mistral models
    # Fine-tuning & training tools
    "unslothai/unsloth",             # Fast fine-tuning
    "axolotl-ai-cloud/axolotl",      # Training configuration framework
    "microsoft/autogen",             # Multi-agent framework
    # Computer vision / other
    "facebookresearch/faiss",        # Vector similarity search
    # LangChain ecosystem
    "langchain-ai/langchain",
    # AI Agents — Open Source
    "NousResearch/hermes-agent",       # Hermes Agent: persistent self-hosted agent (175K+ stars)
    "opencode-ai/opencode",            # OpenCode: terminal-native agent, model-agnostic (180K+ stars)
    "cline/cline",                     # Cline: VS Code + CLI agent, MCP (64K+ stars)
    "earendil-works/pi",               # Pi: minimal open-source coding agent CLI (46K+ stars)
    "kilocode/kilo-code",              # Kilo Code: VS Code/JetBrains/CLI, 0% markup gateway (19K+ stars)
    "Aider-AI/aider",                  # Aider: terminal coding agent, open-source
    # Chinese AI Labs — DeepSeek
    "deepseek-ai/DeepSeek-V4",       # DeepSeek-V4-Pro/Flash (1.6T MoE)
    "deepseek-ai/DeepGEMM",          # Efficient BLAS kernel library (7.5K+ stars)
    "deepseek-ai/FlashMLA",          # Multi-head latent attention kernel (12.7K+ stars)
    "deepseek-ai/DeepEP",            # Expert-parallel communication library
    "deepseek-ai/3FS",               # Three-way fast storage (10K+ stars)
    # Chinese AI Labs — Zhipu AI (Z.ai)
    "zai-org/GLM-5",                 # GLM-5 series (744B MoE, MIT license)
    "zai-org/GLM-Image",             # GLM image generation
    "zai-org/SCAIL-2",               # Scientific AI agent framework
    "zai-org/z-ai-sdk-python",       # Official Python SDK
    "zai-org/z-ai-sdk-java",         # Official Java SDK
    # Chinese AI Labs — Moonshot AI (Kimi)
    "MoonshotAI/Kimi-K2.5",          # Kimi K2.5 multimodal agentic model
    "MoonshotAI/Kimi-K2.6",          # Kimi K2.6 native multimodal coding
    "MoonshotAI/Kimi-K2.7-Code",     # Kimi K2.7-Code coding-focused (GitHub Copilot)
    "moonshotai/kimi-code",          # Kimi Code — AI coding agent
    "moonshotai/kimi-agent-sdk",     # Kimi Agent SDK
    # Chinese AI Labs — Alibaba (Qwen)
    "QwenLM/Qwen3.6",                # Qwen3.6 model family
    "QwenLM/Qwen3-VL",               # Qwen3 vision-language models
    "QwenLM/qwen-code",              # Qwen Code — AI coding assistant
    # Legacy (active but older releases)
    "openai/whisper",                # ASR model (last: 2025-06)
    "huggingface/text-generation-inference", # TGI (maintenance mode)
    "facebookresearch/llama-recipes",    # Llama recipes (last: 2025-01)
    "ericlbuehler/mistral.rs",       # Rust Mistral inference (replaces: mistralai/mistral.rs 404)
    "bitsandbytes-foundation/bitsandbytes", # Quantization (replaces: huggingface/bitsandbytes 404)
    "google/re2",                    # Regex library (replaces: google-research/re2 404)
]
