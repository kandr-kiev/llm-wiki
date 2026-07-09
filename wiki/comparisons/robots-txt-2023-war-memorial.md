---
title: "robots txt 2023 war memorial"
type: comparison
tags:
description: Comparison page for robots txt 2023 war memorial

sources: []
links: []
description: Comparison page for robots txt 2023 war memorial

links: []
confidence: medium
created: 2026-07-08
updated: 2026-07-08
---

# robots txt 2023 war memorial

> **Source:** sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07.md
> **Type:** comparison
> **Created:** 2026-07-08

## Key Findings

[← Insights](/insights)Data Study
# Your robots.txt is a 2023 war memorial
We read the robots.txt of the top 10,000 sites. 38% of the GPTBot rules we could date were written in a single quarter of 2023 — right after GPTBot launched and the Times sued. Then every AI company quietly added a second bot, the one that answers questions in real time, and almost nobody wrote a rule for it.
July 4, 2026
On July 1, Cloudflare announced a way for site owners to start charging AI
companies at the exact
moment one of their bots fetches a page to answer someone's question — not to train a model months
from now, but to answer, live, right then. It's early and experimental, and it isn't alone: open
payment rails like x402 are being built for the same idea. The web has
long had a way to block that fetch. It's starting to build a way to bill for it. Answering is turning into a
transaction.
Which is a strange thing to build a toll booth for, because the web's rulebook for AI barely
admits that moment exists.
We wanted to check that with data rather than vibes, so we did the boring thing. We fetched
the `robots.txt` of the top 10,000 sites and read what each one *declares* —
not what its servers actually serve, not what its edge quietly blocks, because from the outside
nobody can see that. Just the rulebook every site publishes at its own front door. 5,577 of
them had one we could read. This is a study of what that rulebook says about the answer era.
Short version: it was written for a different war.
## The rules are a war memorial
The first thing you notice is the dates. When you line up the AI rules in these files against
when they were first written, they don't spread out across the AI era. They pile up at the
beginning of it. Of the 861 sites whose GPTBot rule we could date, **38% wrote it in a single
quarter — the last three months of 2023** (323 sites, three times the next-tallest
quarter). Half were written within roughly six months of the crawler's launch (430 of 861).
That quarter was not a coincidence. OpenAI shipped GPTBot in August 2023; the New York Times
sued OpenAI eight weeks later. If you ran a website that autumn, you got a real shock and you
reacted to it, rationally, by pasting four lines into a text file to keep the training crawler
out. That was a reasonable thing to do in 2023. It might still be the right call today.
You would expect files this old to be stale. Most aren't. Of the 430 sites that wrote their
GPTBot rule in the panic window, 87% came back and added new bot rules later; only 57 never
returned. Someone keeps opening these files.
Look at what they add, though, and the diligence curdles. The new lines are almost all more
training crawlers — ClaudeBot now sits on 671 of these sites, PerplexityBot on 540, still climbing
through 2026 — while the answer-time bots, the ones that fetch a page to write a live answer, draw
a fraction of that attention. And nothing since GPTBot has moved at panic speed: every crawler
that followed booked ju

## Summary

st 3% to 23% of its rules in its first two quarters, a slow drip against
2023's flood. The panic was a one-time event. Everything after is muscle memory.
So the file is a war memorial — just not the abandoned kind. It's the kind people keep coming
back to, and every name they cut into it is another training crawler from the same war. That
isn't neglect. It's a blind spot, and you don't fix a blind spot by tending the file harder.
When the AI rules were first written, by quarter
Training crawler (GPTBot)Answer-time bots — first rule per site (OAI-SearchBot, Claude-User, Claude-SearchBot, Perplexity-User)first quarter a rule for the bot was observed · all 1,197 blockers
0- 100- 200- 300- sites
323 — the panic quarter81
- - - - - - - - - - - - - - - 2023202420252026
Each site counted once, in the quarter its rule first appeared. Across all 1,197
blockers, 861 ever wrote a dated GPTBot rule and only about half as many (406) ever wrote an
answer-time one — the low band that never rises to meet the 2023 spike. Dated from the Internet
Archive by first appearance. See method.
## Every AI company runs two bots. Most rules only know about one.
Here is the part the 2023 rulebook missed.
Each of the big AI vendors doesn't send one bot to your site. It sends two, and they do
different jobs. One is the *training crawler* — it reads the web in bulk to build the
model. The other is the *answer-time fetcher* — it shows up later, when a real person has
asked a real question, to pull your page into the answer being written in front of them. The
first is the one everyone was angry at in 2023. The second is the one that matters now, because
it's the one any pay-per-answer toll would meter.
Every AI vendor runs two bots; most rules only name the training crawler.
TRAINING CRAWLERreads the web to build the modelANSWER-TIME FETCHERarrives when someone asks a questionGPTBotOpenAIOAI-SearchBot + ChatGPT-UserOpenAIClaudeBotAnthropicClaude-User + Claude-SearchBotAnthropicPerplexityBotPerplexityPerplexity-UserPerplexity
The split. Blocking the training crawler on the left says nothing about the
answer-time fetcher on the right.
So we asked, for every site that fully blocked a vendor's training crawler: did it say
anything at all about that vendor's answer-time bot? Mostly, no.
Among sites that fully block each training crawler (readable robots.txt, top 10,000)
Vendor
Training crawler they blocked
Answer-time bot(s) in question
Said nothing at all about the answer-time bot
Explicitly let it in
Anthropic
ClaudeBot
Claude-User, Claude-SearchBot
71% (598 of 840)
1.9% (16 of 840)
OpenAI
GPTBot
OAI-SearchBot, ChatGPT-User
53% (493 of 932)
4.0% (37 of 932)
Perplexity
PerplexityBot
Perplexity-User
50% (229 of 461)
0.9% (4 of 461)
Read the two right-hand columns together, because the gap between them is the finding.
Seven in ten sites that shut Anthropic's training crawler out have no rule of any kind for the
bot that answers with Claude. And the number who deliberately did the inter

## Related Articles

- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- 
- [[automating-ai-away-2026-07-07]]
- [[automating-ai-away-2026-07-07]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
