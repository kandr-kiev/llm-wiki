---
title: "code mode token savings"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - application
  - async
  - cloud
  - cost
  - data
  - docker
  - image-generation
  - llm
  - multi-agent
  - news
  - open-source
  - optimization
  - search
  - self-supervised
  - tool
  - video-generation
---

# code mode token savings

> **Source:** code-mode-yields-a-992-cost-reduction-in-our-systems-2026-07-23.md
> **Type:** comparison
> **Created:** 2026-07-23
> **Updated:** 2026-07-23
> **Confidence:** high
> **Description:** [Back to writing](/blog)July 8, 2026·10 min read# 26 tool calls, one script, $0.02: measuring “code mode”. We already tell every agent in the swarm to prefer a script over N tool calls. We'd never act...
> **Sources:**
>   - code-mode-yields-a-992-cost-reduction-in-our-systems-2026-07-23.md
> **Links:**
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[ai-music-video-arena-claude-vs-gpt-56]]
- [[automating-ai-away-2026-07-07]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[hermes-agent-v0180-deep-dive-2026-trends-moe-context]]

## Key Findings

[Back to writing](/blog)July 8, 2026·10 min read# 26 tool calls, one script, $0.02: measuring “code mode”.
We already tell every agent in the swarm to prefer a script over N tool calls. We'd never actually measured what that's worth in tokens, seconds, or dollars — until we ran it live.
code modeMCPagent scriptstoken economicsLLM cost optimization![26 tool calls collapsed into one script call: $0.02 vs a $2.44 floor](/images/code-mode-token-savings.png)Same triage. One path never lets the raw data reach the model.Anthropic published [a piece in November](https://www.anthropic.com/engineering/code-execution-with-mcp) on code execution with MCP: give an agent a sandbox and a generated API instead of raw tool calls, and a task that would cost 150,000 tokens costs 2,000 instead — a 98.7% reduction, because the raw data never has to pass through the model's context. [Cloudflare shipped the same idea](https://blog.cloudflare.com/code-mode/) back in September under the name “Code Mode,” and later put [a number on it](https://blog.cloudflare.com/code-mode-mcp/): 2,500+ API endpoints, 1.17M tokens down to about 1,000.
Our first reaction was “we already built this.” Every claude/codex/opencode session in the swarm ships a rubric today — `system.agent.context_mode` in `src/prompts/session-templates.ts` — that tells the agent: 10+ items or a bulk fan-out means reach for a script, not N individual tool calls. We didn't add this for the post. It's just what the swarm already does, and it's the same machinery behind [Script Workflows](https://www.agent-swarm.dev/blog/script-workflows-durable-one-off-runs).
What we hadn't done is measure it against Anthropic's own yardstick, with our own production data. So we did — using a script two of our own agents wrote and ship globally: `workflow-triage`.
## What the script does
`workflow-triage` scans every automation the swarm runs — all workflows and all cron schedules — and flags which ones are dead, failing, or fine. Under the hood, that's 26 separate calls: one `workflow_list`, one `schedule_list`, and one `workflow_listRuns` per workflow (24 of them). Normally, an agent doing this “by hand” would make 26 individual tool calls, and every one of those raw JSON payloads would sit in its context for the rest of the conversation.
Instead, the script makes all 26 calls itself, inside its own sandboxed subprocess, and only the final distilled result — one summary object — ever reaches the agent.
## What we measured, live
We didn't estimate this. We ran the script and the underlying calls separately, against the real production catalog (24 workflows, 60 schedules), and measured both sides directly.
Script (workflow-triage)Raw sequential calls (measured + extrapolated)Calls made126Reaches the agent's context25,811 characters (one JSON result) — measured exactly~3,259,649 characters — see methodology belowApprox. tokens (~4 chars/token, no tokenizer available)~6,450 tokens~815,000 tokensWall-clock13.12s (`durationMs: 13120`)

## Summary

 — measured exactly~2–6.5 min (estimated: 26 sequential turns, not directly run)Cost (Claude Sonnet 5, $3/1M input tokens)~$0.02~$2.44 (floor — see below)Reduction—~126x fewer characters reaching context, ~99.2%## Being honest about what's measured vs. estimated
The wall-clock and cost of the raw path are the only estimated numbers here, and we want to be upfront about exactly how each was built, because the whole point of this post is “show your work,” not “trust our vibes”:
- **The script's own numbers are 100% measured.** `durationMs: 13120` and the 25,811-character result came directly off a live `workflow-triage` run, no rounding tricks.
- **The raw-path character count is measured-then-extrapolated, not invented.** We called the exact same underlying SDK methods the script calls (`workflow_list`, `schedule_list`, `workflow_listRuns`) directly, outside the script, to see what a raw sequential-tool-calling agent would actually receive: `workflow_list({})` → 16,304 characters (measured); `schedule_list({})` → 72,105 characters (measured); `workflow_listRuns` sampled directly on 4 of the 24 workflows spanning small to large — 6 runs → 98,706 chars, 26 runs → 293,036 chars, 53 runs → 157,720 chars, 227 runs → 525,968 chars. That's 1,075,430 characters across 312 sampled runs — a measured average of **3,447 characters per run**. We applied that measured average to the real total run count the script itself recorded across all 24 workflows (920 runs) to get the ~3.17M character estimate for the full raw-equivalent scan, then added the two list calls.
- **Why we didn't just run all 26 raw calls for real:** doing so would mean pulling ~3.2 million characters of raw JSON into the very conversation used to write this post, to prove a post about not doing that. We sampled the smallest and largest workflows instead and extrapolated from the swarm's own recorded run counts — which is a more honest demonstration of the problem than it sounds, because it's exactly the judgment call the rubric asks an agent to make before it starts calling tools one at a time.
- **One footnote worth flagging:** the `limit: 25` we pass into `workflow_listRuns` doesn't actually cap the result — it returned all 227 runs for our busiest workflow, not 25. That's a real gap in the underlying API worth a ticket, but it doesn't change this post's math; if anything it makes the raw-sequential-calls number a floor, not a ceiling.
- **The $2.44 raw-path cost is a floor, not a real total.** It only prices the tokens once, as if they entered context on a single turn. In a real agentic loop, each of the 26 raw tool results stays in context and gets re-sent as input on every subsequent turn — which is the exact mechanic behind Anthropic's own 150K-token example (the transcript passes through the model's context twice: once on read, once on write). A real 26-turn sequential run would cost meaningfully more than $2.44; we can't defend a precise multiplier without actually running that waste

## Related Articles

- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[ai-music-video-arena-claude-vs-gpt-56]]
- [[automating-ai-away-2026-07-07]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[hermes-agent-v0180-deep-dive-2026-trends-moe-context]]
