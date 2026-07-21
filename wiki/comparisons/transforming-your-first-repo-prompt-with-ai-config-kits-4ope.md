---
title: "transforming your first repo prompt with ai config kits 4ope"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - application
  - claude
  - image-generation
  - llm
  - mobile
  - open-source
  - prompt-engineering
  - prompt-tuning
  - search
  - software
  - standards
  - video-generation
  - web
---

# transforming your first repo prompt with ai config kits 4ope

> **Source:** transforming-your-first-repo-prompt-with-ai-config-kits-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-20
> **Updated:** 2026-07-20
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/davekurian/transforming-your-first-repo-prompt-with-ai-config-kits-4ope ingested: 2026-07-18 sha256: 728b69e8f49283f626d315d45821139cb0bc4a475e585b640542c2d1abbf0112 blo...
> **Sources:**
>   - transforming-your-first-repo-prompt-with-ai-config-kits-2026-07-18.md
> **Links:**
- [[the gitbook migration trap 4gp2]]
- [[17 none of it was for me a year of building with ai 32kf]]
- [[5 things i learned doing ai evaluation for 2 years 3kgh]]
- [[adding an ai chatbot to echostats 290m]]
- [[stop hand translating between sql and your erd 4ohm]]

## Key Findings

---
source_url: https://dev.to/davekurian/transforming-your-first-repo-prompt-with-ai-config-kits-4ope
ingested: 2026-07-18
sha256: 728b69e8f49283f626d315d45821139cb0bc4a475e585b640542c2d1abbf0112
blog_source: Dev Community
---
Transforming Your First Repo Prompt with AI Config Kits - DEV Community
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
[
![Cover image for Transforming Your First Repo Prompt with AI Config Kits](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fcdn.otf-kit.dev%2Fthumbnails%2Fthe-first-prompt-in-a-new-repo.png)
](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fcdn.otf-kit.dev%2Fthumbnails%2Fthe-first-prompt-in-a-new-repo.png)
[![Dave Kurian](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3962819%2F50b558da-9a83-43ee-a473-5381fe6bb0d4.png)](/davekurian)
[Dave Kurian](/davekurian)
Posted on Jul 18
• Originally published at [otf-kit.dev](https://otf-kit.dev/blog/the-first-prompt-in-a-new-repo) 
# 
Transforming Your First Repo Prompt with AI Config Kits
[#agents](/t/agents)
[#ai](/t/ai)
[#llm](/t/llm)
[#programming](/t/programming)
The first prompt in a brand-new repo is the hardest one you'll ever send a coding agent. Not because the task is complex — usually it's something modest, like "add a settings page" or "wire up Stripe checkout." It's hard because the agent has nothing to anch

## Summary

or on. No conventions. No examples. No answer to the question that quietly determines everything: what does "done" mean here?
This is genuinely one of the sharper edges of agentic coding right now, and the engineers shipping real apps know it. The first prompt sets the trajectory for every prompt that follows. Get it wrong and you spend the next month fighting the ghost of a generic scaffold the agent invented on day one. So let's talk about what a kit's AI config actually changes about that first prompt — concretely, with a before/after.
## 
The cold-start problem, made specific
Imagine a fresh `pnpm init` repo. No `package.json` beyond the default, no `src/`, no `README`. You hand it to an agent and type:
>
"Add a settings page where I can toggle email notifications."
Here's what a high-quality agent does in that situation — and here's what makes it quietly expensive:
- It picks a file structure. `app/settings/page.tsx`, or `src/pages/Settings.tsx`, or `pages/settings/index.tsx`. Which one? A guess weighted by training data, not by your repo, because your repo has no opinion.
- It picks a component library. Some prior, whichever it picks, it imports the way *that* library wants to be imported — not the way your future code will want it.
- It writes a server action. Or a route handler. Or a tRPC procedure. Or bakes the mutation client-side. Three valid choices, all with different downstream consequences.
- It adds a form library. A safe default is fine. So is nothing.
- It guesses at "done." No loading state. No error boundary. No disabled-while-saving. No toast on success. The page *renders*, which is technically shipping.
Five prompts later you're four thousand lines deep, the agent is confidently extending its own scaffold, and you're trying to refactor *out* of conventions it invented. The ghost in the machine isn't the agent's intelligence. It's the absence of priors.
## 
Why this happens — and why it isn't the model's fault
It's tempting to blame the model. It isn't the model's fault.
Mechanistically, an LLM is a next-token predictor over its context window. In an empty repo, that context contains: the prompt, the file tree, the contents of any files you've opened. That is the entire evidence base for "what does done mean here." When the evidence is thin, the model falls back to its training distribution — the median of every well-structured open-source repo it ever saw. That's a reasonable default for a demo. It's a real liability for a project that needs to ship, because your project will diverge from the median within a week, and now the agent is reinforcing patterns you've already abandoned.
The first prompt isn't really one prompt. It's the seed for a trajectory.
[[COMPARE: empty repo cold start vs kit repo with AI config]]
## 
What the kit's AI config actually does
A kit ships three things that change the math on that first prompt:
- 
**`CLAUDE.md` at the repo root.** A short, opinionated document stating the house style: where pages

## Related Articles

- [[the gitbook migration trap 4gp2]]
- [[17 none of it was for me a year of building with ai 32kf]]
- [[5 things i learned doing ai evaluation for 2 years 3kgh]]
- [[adding an ai chatbot to echostats 290m]]
- [[stop hand translating between sql and your erd 4ohm]]
