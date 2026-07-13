---
title: "Release v5.12.0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ci-cd
  - computer-vision
  - data
  - deep-learning
  - deployment
  - docker
  - edge
  - embedding
  - foundation-model
  - image-generation
  - library
  - multimodal
  - nlp
  - optimization
  - real-time
  - security
  - standards
  - system-design
---
# Release v5.12.0

> **Source:** release-v5120-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/transformers/releases/tag/v5.12.0 ingested: 2026-07-10 sha256: edd37bd756853070b34d9775fc6884aad35de91ba4f83b48f36ce228d53ebffd blog_source: github --- #...
> **Sources:**
>   - release-v5120-2026-07-10.md
> **Links:**
- [[release-v5110]]
- [[release-v0390]]
- [[patch-release-v5104]]
- [[release-notes-hugging-face-transformers-vv5130]]
- [[release-v1140]]

## Key Findings

---
source_url: https://github.com/huggingface/transformers/releases/tag/v5.12.0
ingested: 2026-07-10
sha256: edd37bd756853070b34d9775fc6884aad35de91ba4f83b48f36ce228d53ebffd
blog_source: github
---
# Release v5.12.0
## Release Notes
# Release v5.12.0
## New Model additions
### MiniMax-M3-VL
![image](https://github.com/user-attachments/assets/ae9dd96f-6877-4531-a06b-a756686f24e5)
MiniMax-M3-VL is the vision-language member of the MiniMax-M3 family that pairs a CLIP-style vision tower with 3D rotary position embeddings with the MiniMax-M3 text backbone. It uses a mixed dense/sparse Mixture-of-Experts decoder with SwiGLU-OAI gated experts and a lightning indexer for block-sparse attention. The model processes images through a Conv3d patch embedding system and includes specialized components for efficient multimodal understanding and generation.
**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/minimax_m3_vl)
* Add minimax m3vl (#46600) by @ArthurZucker in [#46600](https://github.com/huggingface/transformers/pull/46600)
### PP-OCRv6: update documentation and slow tests (#46576)
![image](https://github.com/user-attachments/assets/e62284ec-78bf-49cb-8aa2-deccc665372f)
The official weights for PP-OCRv6 are out: PP-OCRv6 is a lightweight OCR system that combines architectural innovation with data-centric optimization. It redesigns the backbone, detection neck, and recognition neck around a unified MetaFormer-style building block with structural reparameterization. Three model tiers (medium, small, tiny) share the same block primitives, covering deployment scenarios from server to edge.
* PP-OCRv6: update documentation and slow tests (#46576) by @ zhang-prog
### Add Parakeet-RNNT (#46331)
ParakeetForRNNT: a Fast Conformer Encoder + an RNN-T (RNN Transducer) decoder
- RNN-T Decoder: Standard neural transducer:
- LSTM prediction network maintains language context across token predictions.
- Joint network combines encoder and decoder outputs.
- Greedy transducer decoding for inference: a blank emission advances the encoder frame by one, a non-blank emission stays on the same frame.
* Add Parakeet-RNNT (#46331) by @eustlb
## Bugfixes and improvements
* [CI] don't export OTELs within the tests (#46602) by @tarekziade in [#46602]
* [CI] capture checkers output in OTEL (#46601) by @tarekziade in [#46601]
* Lfm2: thread `seq_idx` through ShortConv for packed/varlen inputs (#46588) by @ChangyiYang in [#46588]
* put output_hidden_states into filter_output_hidden_states (#46422) by @molbap in [#46422]
* a11 for checkers (#46599) by @tarekziade in [#46599]
* Fix stop string matching for byte-fragment tokens (#46530) by @Incheonkirin in [#46530]
* [DiffusionGemma] better docs and links (#46569) by @gante in [#46569]
* Require `trust_remote_code` to run a local-directory `custom_generate` (#46483) by @LinZiyuu in [#46483]
* Fix torchaudio version not tied to torch version in docker file (#46594) by @ydshieh in [#46594]
* [CI] Enable

## Summary

See Key Findings for full content.

## Related Articles

- [[release-v5110]]
- [[release-v0390]]
- [[patch-release-v5104]]
- [[release-notes-hugging-face-transformers-vv5130]]
- [[release-v1140]]
