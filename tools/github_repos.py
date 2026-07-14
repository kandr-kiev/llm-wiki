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
    "QwenLM/Qwen3.6",                # Qwen 3.6 series
    "mistralai/mistral-src",         # Mistral models
    # Fine-tuning & training tools
    "unslothai/unsloth",             # Fast fine-tuning
    "axolotl-ai-cloud/axolotl",      # Training configuration framework
    "microsoft/autogen",             # Multi-agent framework
    # Computer vision / other
    "facebookresearch/faiss",        # Vector similarity search
    # LangChain ecosystem
    "langchain-ai/langchain",
    # Legacy (active but older releases)
    "openai/whisper",                # ASR model (last: 2025-06)
    "huggingface/text-generation-inference", # TGI (maintenance mode)
    "facebookresearch/llama-recipes",    # Llama recipes (last: 2025-01)
    "ericlbuehler/mistral.rs",       # Rust Mistral inference (replaces: mistralai/mistral.rs 404)
    "bitsandbytes-foundation/bitsandbytes", # Quantization (replaces: huggingface/bitsandbytes 404)
    "google/re2",                    # Regex library (replaces: google-research/re2 404)
]
