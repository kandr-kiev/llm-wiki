---
title: "stop prompting llms to do legal math its broken 27e0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - application
  - deep-learning
  - image-generation
  - mobile
  - open-source
  - prompt-engineering
  - search
  - software
  - video-generation
  - web
---

# stop prompting llms to do legal math its broken 27e0

> **Source:** stop-prompting-llms-to-do-legal-math-its-broken-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/renato_marinho/stop-prompting-llms-to-do-legal-math-its-broken-27e0 ingested: 2026-07-17 sha256: e5ead69ecbb7f2ee930e0b0449effe93342078d2a1c492cec0a25f5222d52342 blog_so...
> **Sources:**
>   - stop-prompting-llms-to-do-legal-math-its-broken-2026-07-17.md
> **Links:**
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[5-agent-skills-i-use-every-day]]
- [[deadstop-2025-vs-crossfit-games-2024-1okg]]
- [[i-gave-my-agent-the-right-memory-and-it-ignored-it-anyway-li7]]
- [[away]]

## Key Findings

---
source_url: https://dev.to/renato_marinho/stop-prompting-llms-to-do-legal-math-its-broken-27e0
ingested: 2026-07-17
sha256: e5ead69ecbb7f2ee930e0b0449effe93342078d2a1c492cec0a25f5222d52342
blog_source: Dev Community
---
Stop Prompting LLMs to do Legal Math. It's Broken. - DEV Community
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
[Skip to content](#main-content)
Navigation menu
[
![DEV Community](https://media2.dev.to/dynamic/image/quality=100/https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png)
](/)
Search
[
Powered by Algolia
Search
](https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral)
[
Log in
](https://dev.to/enter?signup_subforem=1)
[
Create account
](https://dev.to/enter?signup_subforem=1&state=new-user)
## DEV Community
Close
![](https://assets.dev.to/assets/heart-plus-active-9ea3b22f2bc311281db911d416166c5f430636e76b15cd5df6b3b841d830eefa.svg)
Add reaction
![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)
Like
![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)
Unicorn
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
Exploding Head
![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)
Raised Hands
![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)
Fire
Jump to Comments
Save
Boost
More...
Copy link
Copy link
Copied to Clipboard
Share to X
Share to LinkedIn
Share to Facebook
Share to Mastodon
[Share Post via...](#)
[Report Abuse](/report-abuse)
[![Renato Marinho](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2813362%2Fd2e79a59-7332-4297-b05d-7252876f6e5d.png)](/renato_marinho)
[Renato Marinho](/renato_marinho)
Posted on Jul 17
# 
Stop Prompting LLMs to do Legal Math. It's Broken.
[#ai](/t/ai)
[#mcp](/t/mcp)
[#finance](/t/finance)
[#programming](/t/programming)
I've seen developers try to build "Financial AI Agents" by simply feeding them a PDF of Treasury rates and telling the LLM, "good luck."
It fails every single time.
The problem isn't the model's reasoning capability; it's the fundamental nature of how LLMs process tokens. When you ask Claude or GPT to calculate interest accrual based on a semi-structured text about Treasury Bill rates, you aren't performing math—you are performing pattern matching. The moment the context window gets crowded or the decimal points get complex, the hallucination begins. In a legal context involving 28 U.S.C. § 1961, "approximately" is legally useless.
You don't need better prompts. You need a deterministic execution layer that moves the math out of the LLM's reasoning engine and into a spec

## Summary

ialized, verifiable tool.
### 
The Problem with Post-Judgment Interest
Calculating US Federal post-judgment interest isn't just about multiplying a rate by time. It is strictly governed by 28 U.S.C. § 1961, which mandates using weekly Treasury Bill rates. This introduces a high degree of volatility and granular complexity that an LLM cannot reliably manage via text alone.
If you are building an agent to assist in legal audits or settlement calculations, your agent needs access to three distinct logical steps:
- 
**Data Retrieval**: Finding the exact annual rate for a specific week.
- 
**Computation**: Applying that rate across multiple date ranges where the rate might have changed mid-period.
- 
**Comparative Analysis**: Evaluating how different payment timelines affect the total liability.
If you try to handle this via prompts, your agent is essentially guessing based on cached knowledge. If you use an MCP (Model Context Protocol) server, the agent is executing code.
### 
The Tooling: Moving from Reasoning to Execution
I recently integrated the US Post-Judgment Interest Calculator into a workflow designed for automated legal document review. Here is how the tools within this MCP server actually function in a real production chain.
#### 
1. The Source of Truth: `rate_lookup`
An agent cannot be trusted to remember what the Treasury Bill rate was on February 15, 2024. By using `rate_lookup`, the agent performs a directed query. It provides a reference date and receives the precise annual interest rate active during that specific week. This eliminates the "stale context" problem where an LLM relies on training data that might be months out of date.
#### 
2. The Engine: `interest_accrual_calc`
Once the agent has the rates, it needs to compute the actual burden. `interest_accrual_calc` takes a judgment amount and a timeframe and returns both the total interest accumulated and the updated balance. This is where we bridge the gap between raw data and actionable financial updates. The logic for handling day-counts and rate transitions is handled by the server, not the prompt.
#### 
3. The Decision Layer: `interest_scenario_comparison`
This is where most developers miss the point of MCP. An agent shouldn't just tell you what happened; it should help you decide what to do next. By using `interest_scenario_comparison`, an agent can evaluate two different payment dates (e.g., paying today vs. paying in three months) and output the exact difference in interest costs. This enables a higher level of agency—moving from simple information retrieval to actual financial strategy support.
### 
Why this belongs in MCP, not a Python script
You might be thinking: "I can just write a Python script for this."
You could. But then you have to manage the integration, handle the API/interface between your script and Claude Desktop or Cursor, and deal with the orchestration of how the LLM knows when to call it.
The MCP pattern wraps that logic in a standard protocol that any 

## Related Articles

- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[5-agent-skills-i-use-every-day]]
- [[deadstop-2025-vs-crossfit-games-2024-1okg]]
- [[i-gave-my-agent-the-right-memory-and-it-ignored-it-anyway-li7]]
- [[away]]
