---
type: synthesis
title: Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots
description: Auto-generated wiki page
created: 2026-07-08
updated: 2026-07-08
tags: [llm-wiki, synthesis]
sources: [raw/articles/sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07.md]
confidence: high
contested: false
links: [advanced-rag-techniques]
---
# Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots

> **Source:** [sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07.md](https://sitedex.dev/insights/robots-txt-2023-war-memorial)
> **Relevance:** high
> **Type:** synthesis

---

← InsightsData StudyYour robots.txt is a 2023 war memorialWe read the robots.txt of the top 10,000 sites. 38% of the GPTBot rules we could date were written in a single quarter of 2023 — right after GPTBot launched and the Times sued. Then every AI company quietly added a second bot, the one that answers questions in real time, and almost nobody wrote a rule for it.July 4, 2026

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
the robots.txt of the top 10,000 sites and read what each one declares —
not what its servers actually serve, not what its edge quietly blocks, because from the outside
nobody can see that. Just the rulebook every site publishes at its own front door. 5,577 of
them had one we could read. This is a study of what that rulebook says about the answer era.
Short version: it was written for a different war.

The rules are a war memorial

The first thing you notice is the dates. When you line up the AI rules in these files against
when they were first written, they don't spread out across the AI era. They pile up at the
beginning of it. Of the 861 sites whose GPTBot rule we could date, 38% wrote it in a single
quarter — the last three months of 2023 (323 sites, three times the next-tallest
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
that followed booked just 3% to 23% of its rules in its first two quarters, a slow drip against
2023's flood. The panic was a one-time event. Everything after is muscle memory.

So the file is a war memorial — just not the abandoned kind. It's the kind people keep coming
back to, and every name they cut into it is another training crawler from the same war. That
isn't neglect. It's a blind spot, and you don't fix a blind spot by tending the file harder.

 
 
 When the AI rules were first written, by quarter
 Training crawler (GPTBot)Answer-time bots — first rule per site (OAI-SearchBot, Claude-User, Claude-SearchBot, Perplexity-User)first quarter a rule for the bot was observed · all 1,197 blockers
 0100200300sites
 
 323 — the panic quarter81
 2023202420252026
 
 Each site counted once, in the quarter its rule first appeared. Across all 1,197
 blockers, 861 ever wrote a dated GPTBot rule and only about half as many (406) ever wrote an
 answer-time one — the low band that never rises to meet the 2023 spike. Dated from the Internet
 Archive by first appearance. See method.

Every AI company runs two bots. Most rules only know about one.

Here is the part the 2023 rulebook missed.

Each of the big AI vendors doesn't send one bot to your site. It sends two, and they do
different jobs. One is the training crawler — it reads the web in bulk to build the
model. The other is the answer-time fetcher — it shows up later, when a real person has
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
bot that answers with Claude. And the number who deliberately did the interesting thing — block
the training, keep the answering, the one posture that would actually make sense for a publisher
who wants the referral traffic without feeding the model — is tiny. Under two percent for
Anthropic. Four percent for OpenAI. The "no training, yes answers" stance that everyone
theorizes about barely exists in the wild.

One caution before you read intent into that silence: it's an upper bound on the blind spot,
not a measurement of it. From outside, a site that never met OAI-SearchBot looks identical to one
that met it, shrugged, and saw no reason to write a redundant Allow — nobody writes
rules for bots they're happy to let in. What we can see is intent when someone acts on it, and
that's the table's last column: the few percent who block the training crawler and deliberately
wave the answer-time one through. Forbes is one — GPTBot disallowed, OpenAI's search fetcher
explicitly allowed. The stance is real. It's just rare.

The gap is easier to see in a file that clearly tried. The Economist, as its robots.txt read on
our 2026-07-03 scan and re-checked on 2026-07-04, turns two OpenAI bots away by name — GPTBot and
ChatGPT-User both draw a flat Disallow: /. The third, OAI-SearchBot, the fetcher that
pulls a page into a live search answer, isn't in the file at all. The Economist plainly paid
attention here; it named bots on purpose and made a defensible call. OpenAI just runs more than the
two it governed, and the one it left out is the search fetcher. You can check any site the same way
in about ten seconds: open its robots.txt and look for the answer-time names.

The rulebook the governed aren't allowed to read

There's a quieter failure, too. On 883 of the 7,627 sites that answered us at all, an
honestly-identified bot asking for /robots.txt got a challenge or a refusal — the
rulebook whose whole job is to state the rules, handed to the visitor face-down. GoDaddy is one.
We can't tell a deliberate anti-AI stance from a security vendor challenging every datacenter IP,
ours included, and we don't pretend to. But a rulebook the governed can't read is its own kind of
answer.

Meanwhile, 144 sites already made the call

It would be easy to read all this as "the web is closing." It isn't, and the same 5,577 files
prove it. Only 351 of them disallow every answer-time bot; the front door to answering
is open on the overwhelming majority of the readable top 10,000. And 144 sites went further than
open-by-default — they wrote an explicit Allow line naming an answer-time bot and
invited it in on purpose.

 
 
 
 598
 sites blocked Anthropic's training crawler and said nothing about the bot that answers
 of 840 ClaudeBot-blockers
 
 
 144
 sites wrote an explicit rule inviting an answer-time bot in
 of 5,577 readable robots.txt files
 
 
 Silence versus choice. The left figure is the size of the vacuum — sites that never
 addressed the answering bot. The right figure is how many, across the entire readable sample,
 made an on-the-record decision to allow it. One of these numbers is a posture.

144 out of 5,577 is not a movement. But it's proof the opt-in economy isn't hypothetical and
isn't waiting on anyone. A few sites already treat the answer-time fetch as something to court
rather than tolerate, and a list this short means no one has missed it yet.

Diligence is not a decision

Put the findings next to each other and the shape is clear. These files are maintained —
diligently, for years — and nearly all of that upkeep re-fights a single war. The posture toward
the moment the web is now learning to charge for, the answer-time fetch, is the one line the
maintenance never gets around to writing. Not refused. Just never reached.

There are three coherent things to do about that, and this piece is an argument for none of
them in particular. You can seal: block the training crawlers and the
answer-time fetchers alike, and accept you won't be in the answers. You can sell:
keep the fetchers out until the pay-per-answer toll arrives, then charge for coming in. Or you can
open: let the answer-time bots in, because being in the answer is worth more to
you than the page view. All three are defensible. What isn't a posture is the fourth thing, the
one most sites are actually doing — tending the file for years and never once deciding what
happens when the answer arrives. Whatever you'd choose, choose it on purpose. The file is already
open; it's the decision that's missing.

Opening the door is the easy half

Say you make the call the file never did, and open the door to the answer-time fetch on
purpose. There's a harder question waiting behind it — the one all that maintenance never thinks
to ask.

Those 144 sites made a real decision and opened the door. What none of the files can show is
whether anyone checked the next thing — the one the whole toll booth is premised on: when the
answer-time bot fetches the page, can the page answer the question? Opening the door is
not the same as the room being worth walking into. Whether you sell software or publish articles,
the failure looks the same: an AI arrives at your pricing page and can't find the price, or reads
your reporting and can't tell what you concluded, and it doesn't bill you and move on. It answers
the buyer anyway — from somewhere else, or from a guess.

And this was never a resourcing problem. Diligence barely changes down the rank list; sight
does. A rule for the answer-time category shows up on 64% of top-thousand blockers and just 41% by
rank ten thousand — the teams whose whole job this is miss the new category a third of the time,
and below the top 10,000, where our data runs out, the slope only points down. Most small teams
have no one tending the file at all, and it wouldn't save them if they did: the people who do tend
it still miss what counts. The training war is the visible half. Whether your pages can answer what
a buyer's AI actually asks is the half no file reveals — at any size — and it's the half that
decides whether being in the answer was ever worth anything. You don't get there with more upkeep;
you get there by looking, one page and one question at a time, starting with your own.

Find out which buyer questions your pages can't answer
→

Method

What this is and isn't. We fetched /robots.txt for the Tranco top 10,000 domains
on 2026-07-03 and classified each site's declared policy toward 15 AI bots. This is a
study of stated policy only. We did not crawl any site's pages, we can't see edge or WAF
enforcement, and we never claim a site "blocks AI" — only what its published file does and doesn't
say. Every figure below names its denominator.

 Sample. 10,000 domains. 7,627 returned any HTTP response; 5,577 had a
 readable robots.txt (the denominator for every policy rate); 1,197 fully block at least one
 major AI crawler. The Tranco frame skews toward large, commercial sites.

 The two-bots silence figures. Among sites that issue an explicit full block
 to a training crawler, the share whose robots.txt contains no stanza at all for that
 vendor's answer-time bot(s): Anthropic 598/840 (71%), OpenAI 493/932 (53%), Perplexity 229/461
 (50%). "Explicitly let it in" = at least one answer-time sibling with an explicit
 Allow: OpenAI 37/932 (4.0%), Anthropic 16/840 (1.9%), Perplexity 4/461 (0.9%). The
 silence rates are upper bounds on the blind spot — an absent stanza can't be told apart from a
 deliberate choice to leave the default in place, and few sites write a redundant Allow.

 Opt-ins. 144 of 5,577 sites carry an explicit Allow for at
 least one of OAI-SearchBot, ChatGPT-User, Claude-User, Claude-SearchBot, or Perplexity-User,
 deduped by site.

 When the rules were written. First-observed dates from Internet Archive
 snapshots of each blocker's robots.txt, taken at the actual snapshot timestamp across all 1,197
 full-blockers. These are upper bounds on age (first time a token was seen archived), and the
 archive favors popular sites. Its snapshot cadence can also rise with a site's news attention, so
 part of the 2023Q4 cluster may reflect denser archiving that quarter, not only denser editing.
 323 of 861 datable GPTBot rules (38%) first appear in 2023Q4 —
 three times the next-tallest quarter — and half (430 of 861) within roughly six months of the
 crawler's launch. The same-unit answer-time series counts each site once at its first
 answer-time rule: 406 of 1,197 blockers ever wrote one, about half as many as wrote a GPTBot
 rule, on a low plateau of 50–80 a quarter from late 2024 that never approaches the 2023 spike.

 Maintained, not abandoned. Of 430 panic-era GPTBot-blockers (GPTBot rule
 first seen 2023Q3–2024Q1), 87% later added at least one new tracked-bot rule; only 57 did not.
 This is a lower bound — we register a return only when it adds one of the 15 tracked bots. The
 additions skew to training crawlers (ClaudeBot 671 sites, PerplexityBot 540, Applebot-Extended
 476, meta-externalagent 493) over answer-time bots (167–354). Return rates barely move by rank
 (91% at top-1k, 86% at 5k–10k); the presence of any answer-time stanza decays with it (64% of
 top-1k blockers, 79/124, to 41%, 263/640, at 5k–10k). Sample floor is the top 10,000; the true
 long tail is unmeasured.

 Unreadable rulebooks. 883 of 7,627 responding sites returned a challenge or
 refusal to an honestly-identified client requesting robots.txt from a datacenter IP, after a
 www-fallback and one polite retry. We cannot distinguish an anti-bot policy from a blanket
 datacenter challenge, so these sites are excluded from all rate denominators — which likely makes
 our block rates underestimates, since the most restrictive sites are the ones we couldn't read.

 Carve-outs. 926 of 8,599 full-block verdicts (10.8%) pair
 Disallow: / with path-level Allows. We count these as blocks
 (default-deny posture). 86 sites run curated GPTBot carve-outs.

 Answer-time reachability. Of 5,577 readable files, only 351 effectively
 disallow every answer-time bot; 263 wildcard-block everything.

 An open answer-time sibling, down-rank. Among full-blockers, a training bot
 blocked while an answer-time sibling is left effectively open — mostly by omission, not by
 explicit allow — rises with rank: 8% of top-1,000 (10/125), 22% at 1k–5k (97/433), 29% at 5k–10k
 (187/639). This is the gap widening, not deliberate opening. (Distinct from the deliberate allows
 above, at 0.9–4.0%.)

 Validation. Our classifier agreed with the reference
 robots-parser on 99.24% of 16,740 verdicts across ~1,116 real bodies; the
 disagreements are the carve-out pattern, where we classify stanza posture and the reference tests
 the literal root URL. A re-scan of a 500-domain subsample hours later showed 0.00% verdict churn
 (0 of 4,125).

Download the full
dataset — every domain and its per-bot verdicts (matrix.jsonl), the
first-observed dates (wayback.jsonl), and the
full numbers memo — and check any row yourself. CC BY 4.0.

---

## Related Articles

- [[advanced-rag-techniques]]

---

> **Generated by:** LLM Wiki Integrator
> **Created:** 2026-07-08
