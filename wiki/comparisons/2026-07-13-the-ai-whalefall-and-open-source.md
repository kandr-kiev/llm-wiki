---
title: "2026 07 13 the ai whalefall and open source"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - application
  - container
  - data
  - image-generation
  - mobile
  - news
  - nlp
  - open-source
  - tool
  - web
---

# 2026 07 13 the ai whalefall and open source

> **Source:** the-ai-whale-fall-and-open-source-2026-07-14.md
> **Type:** comparison
> **Created:** 2026-07-14
> **Updated:** 2026-07-14
> **Confidence:** high
> **Description:** #  [ Minor Gripe ](https://minor.gripe/) -  [Posts](/posts/) -  Recent -  [The AI Whale Fall and Open Source](https://minor.gripe/posts/2026-07-13-the_ai_whalefall_and_open_source/) -  [Against Open S...
> **Sources:**
>   - the-ai-whale-fall-and-open-source-2026-07-14.md
> **Links:**
- [[automating-ai-away-2026-07-07]]
- [[away]]
- [[5-agent-skills-i-use-every-day]]
- [[the-illustrated-stable-diffusion-2026-07-07]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]

## Key Findings

# 
[
Minor Gripe
](https://minor.gripe/)
- 
[Posts](/posts/)
- 
Recent
- 
[The AI Whale Fall and Open Source](https://minor.gripe/posts/2026-07-13-the_ai_whalefall_and_open_source/)
- 
[Against Open Source's Anthropocentrism](https://minor.gripe/posts/2026-03-23-against_open_sources_anthropocentrism/)
- 
[Millwright: Smarter Tool Selection From Agent Experience](https://minor.gripe/posts/2026-03-13-millwright_smarter_tool_selection_with_adaptive_toolsheds/)
- 
[My Friend Ellem](https://minor.gripe/posts/2026-03-11-my_friend_ellem/)
- 
[Gremlins: Ideas for Cogitation and Actuation](https://minor.gripe/posts/2026-03-09-gremlins_ideas_for_cogitation_and_actuation/)
- 
[Series](/series/)
- 
[Tags](/tags/)
powered by Hugo | themed with poison
© 2026 . All rights reserved.
# 
[The AI Whale Fall and Open Source](https://minor.gripe/posts/2026-07-13-the_ai_whalefall_and_open_source/)
July 13, 2026
- 
5 mins read
- 
[ai](https://minor.gripe/tags/ai)
- 
[genai](https://minor.gripe/tags/genai)
- 
[practices](https://minor.gripe/tags/practices)
- 
[policy](https://minor.gripe/tags/policy)
- 
[rant](https://minor.gripe/tags/rant)
Frontier labs are subsidizing AI usage, and we’d be fools not to use it to improve the state of open source while that holds out.
## How are whales like frontier labs?
**Aside**
Arguably, whales are more like the *institutional investors* in frontier labs, but that’s neither here nor there.
A [whale fall](https://en.wikipedia.org/wiki/Whale_fall) is the bloom of an ecosystem when the carcass of a whale sinks and lands on the ocean floor, providing food and spurring the creation of new life.
Right now, critics of AI as currently being commercialized will tell you that labs like Anthropic and OpenAI cannot possibly last given the huge sums of money (hundreds of billions in some cases) that somehow must be paid back. They will say that the financial engineering underpinning these orgs has temporarily given a reprieve from market forces, and that is the *only* reason you can waste time making slop without paying through the nose for the privilege. I’m not entirely sure that that is the case, but let’s take it as true.
From personal experience as well as that of many [experienced](https://github.com/macton/differentiable-collisions-optc) [developers](https://antirez.com/news/158), AI can be a useful tool when writing or maintaining code. I’ll write more on this some other time, but there is very clearly a there there and anybody saying otherwise is living in some different reality.
So, we get two things:
- AI is a useful tool.
- AI is a tool that will only be available for a limited time.
**Aside**
Now, *personally*, the limited-time thing I think is bullshit–but, I’ll allow it for rhetorical reasons here.
Most-all of the people I’ve talked to that are strongly anti-LLM and anti-AI are oddly silent on the subject of models like GLM 5.2 and other modern open-weight models that are “good enough” for assistance now, and in another year will 

## Summary

likely be as good as Fable or 5.6 today. I suspect this is because they are *larpers* and aren’t actually keeping track of the technology.
These same people seem to believe that AI/LLMs, if the bubble bursts, will all just spontaneously disappear and delete themselves from the collective storage of the universe, to presumably be followed by the expensive graphics cards and CPUs and FPGAs that can run them.
As a friend wryly observed:
>
Ah yes, it is well-known that after the 2008 sub-prime collapse everybody stopped living in houses.
The whale carcass will not last forever on the ocean floor, nor too shall the over-leveraged frontier lab. But, in the meantime, there’s a chance for the rest of us to pick those tokens clean.
## A feast of tokens, if we but choose to eat
You’ve probably seen some version of the [classic XKCD image](https://imgs.xkcd.com/comics/dependency_2x.png), where there’s a tower of babel of software and the critical jenga piece it all happens to be supported by is maintained by some quiet developer in the middle of nowhere. There are a *lot* of those projects, and honestly, we ain’t getting any younger.
Even in theoretically “young” (flagrantly false in this case, but bear with me) projects like NixOS, you can end up with open PRs (not to mention *issues*!) numbering in the low [tens of thousands](https://github.com/NixOS/nixpkgs/pulls). These same projects will also then frequently complain about the lack of available manpower.
There are things that I wouldn’t trust to an AI right now. I don’t think, for example, that large architectural rewrites or feature additions for projects that are meant to be building blocks for other projects are best left to the vibes.
For mechanical work–things like bumping versions, fixing failing tests, checking documentation for inconsistencies–the clankers have proven their worth (even before LLMs, anybody remember dependabot?)! **A *large part* of the technical debt (and debt in developer ergonomics) for these projects is something that could be remediated using these models.**
In projects like NixOS’ nixpkgs, we already make heavy use of automation (`r-ryantm` and friends) and mechanical verification and CI. Those deterministic systems make improving tests and suggesting minor PR refactors and things *even safer*. It makes it *even easier* to trust the contributions of clankers.
**We should all be making hay while the sun shines.**
**Aside**
Another community I’ve long been a member of–the Elixir community–has been somewhat at the forefront here.
If you look at work done by Jose Valim (in marked contrast to, say, Andrew Kelley and how he’s handling Zig) and other folks in the Elixir community (Chris McCord, Isaac Yonemoto, Zach Daniels, myself, others), there’s a clear embrace of these tools.
It isn’t done uncritically–[Valim himself commented on this during a conference](https://x.com/josevalim/status/2048698752077025743)–but that it is being done *at all* has yielded and will yield dividend

## Related Articles

- [[automating-ai-away-2026-07-07]]
- [[away]]
- [[5-agent-skills-i-use-every-day]]
- [[the-illustrated-stable-diffusion-2026-07-07]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
