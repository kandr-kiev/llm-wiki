---
title: "Issue #2844: Add avian magnetoreception quantum co-scientist example"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - data
  - foundation-model
  - gpt
  - hardware
  - open-source
  - real-time
  - tool
  - use-case
---
# Issue #2844: Add avian magnetoreception quantum co-scientist example

> **Source:** gh-openaiopenai-cookbook-issue-2844-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/openai/openai-cookbook/issues/2844 ingested: 2026-07-11 sha256: 53e5a706c2fa88f636d0a10e7f0dfcdbc94a6b22476bec0540f598e60a071724 blog_source: github:openai/openai-co...
> **Sources:**
>   - gh-openaiopenai-cookbook-issue-2844-2026-07-11.md
> **Links:**
- [[issue-6359-truncate-gold-on-policy-prompts-before-generation-keeping-the-prompt-end]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[issue-6358-add-trlenvironments-submodule-with-sandboxenvironment]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-3419-fix-bug-in-forgetting-metric-in-metamathqa]]

## Key Findings

---
source_url: https://github.com/openai/openai-cookbook/issues/2844
ingested: 2026-07-11
sha256: 53e5a706c2fa88f636d0a10e7f0dfcdbc94a6b22476bec0540f598e60a071724
blog_source: github:openai/openai-cookbook
---
# Issue #2844: Add avian magnetoreception quantum co-scientist example
**State:** open | **Author:** steps-re | **Created:** 2026-07-09T00:25:05Z
### Summary
A community example that casts the model as a hands-on scientific collaborator on a real physics problem: the radical-pair "quantum compass" thought to underlie avian magnetoreception.
GPT does the actual work across the notebook:
- **Designs** a Trotterized circuit for the 3-qubit radical-pair Hamiltonian, choosing the gate decomposition and singlet preparation/readout.
- **Runs** it on a simulator and compares against pre-recorded runs on real IBM quantum hardware (`ibm_kingston`), sweeping the compass-survival probability vs field angle.
- **Interprets** the sweep and the hardware-vs-simulator gap.
- **Judges**, honestly, whether a quantum computer is even the right tool here. The verdict is no for this observable: a classical typicality estimator matches it on a laptop. The notebook makes that case rather than overselling quantum.
### Notes
- Runs end-to-end on a laptop from bundled pre-recorded data (`data/`), so no quantum-hardware account or long queue is needed to reproduce it.
- Uses the Responses API. API key is read from `OPENAI_API_KEY`; no secrets in the notebook.
- Executed outputs are kept so the reasoning is visible on the rendered page.
- Adds `registry.yaml` and `authors.yaml` entries.

## Summary

See Key Findings for full content.

## Related Articles

- [[issue-6359-truncate-gold-on-policy-prompts-before-generation-keeping-the-prompt-end]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[issue-6358-add-trlenvironments-submodule-with-sandboxenvironment]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[issue-3419-fix-bug-in-forgetting-metric-in-metamathqa]]
