---
title: "textures"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - compliance
  - distributed
  - edge
  - nlp
  - software
  - system-design
  - use-case
---
# textures

> **Source:** self-organising-textures-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://distill.pub/selforg/2021/textures ingested: 2026-07-10 sha256: 09183f79a81dd370e26df8eeab39b224c4be779395e2b28adaef1dd292c43422 blog_source: Distill AI --- -  -  -  Self-Organi...
> **Sources:**
>   - self-organising-textures-2026-07-10.md
> **Links:**
- [[adversarial]]
- [[full-stack-ai-explainer]]
- [[google-finance-updates-june]]
- [[expanding-managed-agents-gemini-api]]
- [[nyc-ai-summit]]

## Key Findings

---
source_url: https://distill.pub/selforg/2021/textures
ingested: 2026-07-10
sha256: 09183f79a81dd370e26df8eeab39b224c4be779395e2b28adaef1dd292c43422
blog_source: Distill AI
---
- 
- 
- 
Self-Organising Textures
- 
[
Distill
](/)
[About](/about/)
[Prize](/prize/)
[Submit](/journal/)
# Self-Organising Textures
Neural Cellular Automata Model of Pattern Formation
#demo {
font-size: 14px;
user-select: none;
grid-template-columns: auto;
grid-template-rows: auto auto;
grid-auto-flow: column;
row-gap: 10px;
}
.hint a {
color: inherit;
}
@media (min-width: 1180px) {
#demo {
grid-template-columns: 512px 1fr;
grid-template-rows: auto;
}
#pattern-controls {
grid-row: 1;
}
}
#demo-canvas {
border: 1px solid lightgrey;
image-rendering: pixelated;
touch-action: none;
width: 100%;
}
#pattern-controls {
display: grid;
grid-template-columns: 1fr;
grid-template-rows: min-content minmax(0, 0.3fr) min-content minmax(0, 0.3fr) minmax(0, 0.32fr) minmax(0, 0.1fr);
/*row-gap: 20px;*/
overflow: hidden;
}
@media (max-width: 1180px) {
#pattern-controls {
grid-template-rows: min-content minmax(0, 0.4fr) min-content minmax(0, 0.4fr) min-content minmax(0, 0.1fr);
}
}
.pattern-selector::-webkit-scrollbar {
display: none;
}
#demo-tip{
display: grid;
grid-template-columns: 40px auto;
align-items: center;
column-gap: 10px;
margin-bottom: 20px;
}
#pointer {
width: 40px;
}
#status {
font-size: 12px;
color: rgba(0, 0, 0, 0.6);
font-family: monospace;
}
#model-hints {
color: rgba(0, 0, 0, 0.6);
grid-column: 1/3;
}
#model-hints span {
display: none;
}
.hint {
color: rgba(0, 0, 0, 0.6);
line-height: 1.4em;
user-select: text;
}
input[type=range] {
-webkit-appearance: none; /* Hides the slider so that custom slider can be made */
width: 95%; /* Specific width is required for Firefox. */
background: transparent; /* Otherwise white in Chrome */
margin-bottom: 8px;
}
.hint a {
font-size: 90%;
}
@media (max-width: 350px) {
.hint a {
font-size: 75%;
}
}
input[type=range]::-webkit-slider-thumb {
-webkit-appearance: none;
}
input[type=range]:focus {
outline: none; /* Removes the blue border. You should probably do some kind of focus styling for accessibility reasons though. */
}
input[type=range]::-ms-track {
width: 100%;
cursor: pointer;
/* Hides the slider so custom styles can be added */
background: transparent;
border-color: transparent;
color: transparent;
}
/* Thumb */
/* Special styling for WebKit/Blink */
input[type=range]::-webkit-slider-thumb {
-webkit-appearance: none;
height: 14px;
width: 14px;
border-radius: 50%;
background: steelblue;
cursor: pointer;
margin-top: -6px; /* You need to specify a margin in Chrome, but in Firefox and IE it is automatic */
}
/* All the same stuff for Firefox */
input[type=range]::-moz-range-thumb {
height: 14px;
width: 14px;
border-radius: 50%;
background: steelblue;
cursor: pointer;
border: none;
}
/* All the same stuff for IE */
input[type=range]::-ms-thumb {
height: 14px;
width: 14px;
border-radius: 50%;
background: grey;
cursor: pointer;
}
/* Tra

## Summary

See Key Findings for full content.

## Related Articles

- [[adversarial]]
- [[full-stack-ai-explainer]]
- [[google-finance-updates-june]]
- [[expanding-managed-agents-gemini-api]]
- [[nyc-ai-summit]]
