---
title: "pointer events"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - image-generation
  - machine-learning
  - optimization
  - search
  - use-case
  - video-generation
---

# pointer events

> **Source:** pointer-events-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://css-tricks.com/almanac/properties/p/pointer-events/ ingested: 2026-07-17 sha256: cc1137030c1dbdc9c0bf6329b2ff8911bd072eafb46830ac915d20881cc32006 blog_source: CSS Tricks --- po...
> **Sources:**
>   - pointer-events-2026-07-17.md
> **Links:**
- [Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning](http[Issue #8330: Dataset Studio and Viewer down](https://github.com/pytorch/pytorch/issues/8330)[Issue #8330: Dataset Studio and Viewer down]]
- [[The Illustrated Retrieval Transformer 2026 07 07]]
- [[5 Agent Skills I Use Every Day]]
- [[Release v0.25.1]]

## Key Findings

---
source_url: https://css-tricks.com/almanac/properties/p/pointer-events/
ingested: 2026-07-17
sha256: cc1137030c1dbdc9c0bf6329b2ff8911bd072eafb46830ac915d20881cc32006
blog_source: CSS Tricks
---
pointer-events | CSS-Tricks
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
- - - 
- 
- 
- 
- 
- 
- 
Skip to main content 
[
CSS-Tricks
](/)
Since 2007
- [Articles](https://css-tricks.com/category/articles/)
- [Guides](/guides)
- [Almanac](/almanac)
- [Links](https://css-tricks.com/category/links/)
- [Picks](https://css-tricks.com/picks/)
- [Newsletter](https://css-tricks.com/newsletters/)
- [Search
](https://www.google.com/search?q=site:css-tricks.com%20layout)
[pointer-events](https://css-tricks.com/tag/pointer-events/) 
CSS Almanac → Properties → P → pointer-events 
# pointer-events
![](https://secure.gravatar.com/avatar/4526d37720aa1e3389c64d28339da0ca1cbf4f7e6d47ff155f71a565a4db3093?s=80&d=retro&r=pg)
[
Mojtaba Seyedi ](https://css-tricks.com/author/seyedi/)
on
Jul 15, 2026 
The `pointer-events` property controls whether an element can become the target of pointer events like clicks, hover states, and other pointer-based events. In other words, it lets you decide whether the browser should treat an element as interactive when the pointer is over it.
.no-pointer-events {
pointer-events: none;
}
CodePen Embed Fallback
To understand how the property works, it helps to know what the browser does before it fires a pointer event. First, it has to determine which element is under the pointer. This process is known as hit-testing.
Normally, the browser chooses the topmost element under the pointer. But if that element has `pointer-events` set to `none`, the browser skips it and continues looking for the next eligible element underneath.
Once you think about `pointer-events` this way, most of its behavior starts to make sense. Rather than disabling events, it simply changes which element (or, in the case of SVG, which part of an element) becomes the event target in the first place.
<svg aria-hidden="true" height="16" version="1.1" viewBox[Issue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning](http[Issue #8330: Dataset Studio and Viewer down](https://github.com/pytorch/pytorch/issues/8330)ssue #2455: fix #2432: support transformers>=5.0.0 and fix torch.load security warning]]
- [Issue #8330: Dataset Studio and Viewer down](https://github.com/pytorch/pytorch/issues/8330)
- [[The Illustrated Retrieval Transformer 2026 07 07]]
- [[5 Agent Skills I Use Every Day]]
- [[Release v0.25.1]]
