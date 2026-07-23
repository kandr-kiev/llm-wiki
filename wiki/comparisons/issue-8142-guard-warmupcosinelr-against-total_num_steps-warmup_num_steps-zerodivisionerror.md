---
title: "Issue #8142: Guard WarmupCosineLR against total_num_steps == warmup_num_steps (ZeroDivisionError)"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - open-source
  - self-supervised
  - use-case
  - zero-shot
---

# Issue #8142: Guard WarmupCosineLR against total_num_steps == warmup_num_steps (ZeroDivisionError)

> **Source:** gh-microsoftdeepspeed-issue-8142-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-15
> **Updated:** 2026-07-15
> **Confidence:** high
> **Description:** --- source_url: https://github.com/microsoft/DeepSpeed/issues/8142 ingested: 2026-07-14 sha256: bdb452492539369823e25510614ec8cfded66f3635b0b79af1c998fc35f53ba2 blog_source: github:microsoft/DeepSpeed...
> **Sources:**
>   - gh-microsoftdeepspeed-issue-8142-2026-07-14.md
> **Links:**
- [Issue #47325: `return_assistant_tokens_mask` masks the rest of the sequence when a `{% generation %}` span ends at token index 0 or on whitespace stripped by the pre-tokenizer]
- [[Release v1.8.0]]
- [Issue #8333: Support batched=True in Dataset.to_dict]
- [Issue #14167: FlashPack support for transformers pipeline components]
- [Issue #3425: FIX Accept layers_to_transform=0 together with layers_pattern]

## Key Findings

---
source_url: https://github.com/microsoft/DeepSpeed/issues/8142
ingested: 2026-07-14
sha256: bdb452492539369823e25510614ec8cfded66f3635b0b79af1c998fc35f53ba2
blog_source: github:microsoft/DeepSpeed
---
# Issue #8142: Guard WarmupCosineLR against total_num_steps == warmup_num_steps (ZeroDivisionError)
**State:** open | **Author:** vineethsaivs | **Created:** 2026-07-14T16:07:39Z
`WarmupCosineLR.get_lr_ratio` computes the cosine denominator as:
```python
real_total_steps = self.total_num_steps - self.warmup_num_steps
...
ratio = (1 + math.cos(math.pi * real_last_step / real_total_steps)) / 2
```
with no guard against `real_total_steps == 0`. When `total_num_steps == warmup_num_steps` (or `total_num_steps real_total_steps == 0
sched.get_lr_ratio() # ZeroDivisionError: float division by zero
```
The sibling `WarmupDecayLR._get_gamma` already floors this exact denominator with `max(1.0, self.total_num_steps - self.warmup_num_steps)`. This mirrors that guard:
```python
real_total_steps = max(1, self.total_num_steps - self.warmup_num_steps)
```
There is no behavior change in the normal case (`total_num_steps > warmup_num_steps` leaves the value unchanged). In the degenerate case the ratio now floors to `cos_min_ratio` via the existing `max(0.0, ...)` clamp, instead of crashing.
Added a CPU-only regression test `test_warmup_cosine_lr_total_num_steps_equals_warmup_num_steps` next to the existing plain `WarmupCosineLR` tests; it raises `ZeroDivisionError` before this change and passes after. yapf and flake8 clean; DCO signed off.

## Summary

See Key Findings for full content.

## Related Articles

- [Issue #47325: `return_assistant_tokens_mask` masks the rest of the sequence when a `{% generation %}` span ends at token index 0 or on whitespace stripped by the pre-tokenizer]
- [[Release v1.8.0]]
- [Issue #8333: Support batched=True in Dataset.to_dict]
- [Issue #14167: FlashPack support for transformers pipeline components]
- [Issue #3425: FIX Accept layers_to_transform=0 together with layers_pattern]
