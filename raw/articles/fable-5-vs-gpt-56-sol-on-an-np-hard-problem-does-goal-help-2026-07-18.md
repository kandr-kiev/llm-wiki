---
source_url: https://charlesazam.com/blog/fable-5-gpt-5-6-sol-goal/
ingested: 2026-07-18
sha256: 16698840ba02aef7068e677c1c5d49fb1574142318e4b87913e1c4e7fa1c4527
blog_source: Hacker News
---
<!DOCTYPE html><html lang="en"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Fable 5 vs. GPT-5.6 Sol on an NP-Hard Problem: Does /goal Help? - Charles AZAM</title><meta name="description" content="I gave Claude Fable 5 and GPT-5.6 Sol the same unpublished NP-hard optimization problem, with and without their native /goal mode. Fable 5 is a beast; /goal is not a game changer."><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://charles-azam.github.io/blog/fable-5-gpt-5-6-sol-goal/"><link rel="alternate" hreflang="en" href="https://charles-azam.github.io/blog/fable-5-gpt-5-6-sol-goal/"><link rel="alternate" hreflang="fr" href="https://charles-azam.github.io/fr/blog/fable-5-gpt-5-6-sol-goal/"><!-- Open Graph --><meta property="og:type" content="website"><meta property="og:title" content="Fable 5 vs. GPT-5.6 Sol on an NP-Hard Problem: Does /goal Help? - Charles AZAM"><meta property="og:description" content="I gave Claude Fable 5 and GPT-5.6 Sol the same unpublished NP-hard optimization problem, with and without their native /goal mode. Fable 5 is a beast; /goal is not a game changer."><meta property="og:url" content="https://charles-azam.github.io/blog/fable-5-gpt-5-6-sol-goal/"><meta property="og:image" content="https://charles-azam.github.io/headshot.jpg"><meta property="og:locale" content="en_US"><!-- Twitter Card --><meta name="twitter:card" content="summary"><meta name="twitter:title" content="Fable 5 vs. GPT-5.6 Sol on an NP-Hard Problem: Does /goal Help? - Charles AZAM"><meta name="twitter:description" content="I gave Claude Fable 5 and GPT-5.6 Sol the same unpublished NP-hard optimization problem, with and without their native /goal mode. Fable 5 is a beast; /goal is not a game changer."><meta name="twitter:image" content="https://charles-azam.github.io/headshot.jpg"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Manrope:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet"><link rel="stylesheet" href="/_astro/_slug_.DCwbNy1U.css">
<style>pre code.hljs{display:block;overflow-x:auto;padding:1em}code.hljs{padding:3px 5px}/*!
  Theme: GitHub Dark Dimmed
  Description: Dark dimmed theme as seen on github.com
  Author: github.com
  Maintainer: @Hirse
  Updated: 2021-05-15

  Colors taken from GitHub's CSS
*/.hljs{color:#adbac7;background:#22272e}.hljs-doctag,.hljs-keyword,.hljs-meta .hljs-keyword,.hljs-template-tag,.hljs-template-variable,.hljs-type,.hljs-variable.language_{color:#f47067}.hljs-title,.hljs-title.class_,.hljs-title.class_.inherited__,.hljs-title.function_{color:#dcbdfb}.hljs-attr,.hljs-attribute,.hljs-literal,.hljs-meta,.hljs-number,.hljs-operator,.hljs-variable,.hljs-selector-attr,.hljs-selector-class,.hljs-selector-id{color:#6cb6ff}.hljs-regexp,.hljs-string,.hljs-meta .hljs-string{color:#96d0ff}.hljs-built_in,.hljs-symbol{color:#f69d50}.hljs-comment,.hljs-code,.hljs-formula{color:#768390}.hljs-name,.hljs-quote,.hljs-selector-tag,.hljs-selector-pseudo{color:#8ddb8c}.hljs-subst{color:#adbac7}.hljs-section{color:#316dca;font-weight:700}.hljs-bullet{color:#eac55f}.hljs-emphasis{color:#adbac7;font-style:italic}.hljs-strong{color:#adbac7;font-weight:700}.hljs-addition{color:#b4f1b4;background-color:#1b4721}.hljs-deletion{color:#ffd8d3;background-color:#78191b}
</style></head> <body> <div class="flex flex-col min-h-screen"> <header class="bg-[var(--color-bg-secondary)] border-b border-[var(--color-border)]"> <div class="mx-auto max-w-5xl px-6 py-3 flex items-center justify-between"> <a href="/" class="group flex items-center gap-2 transition-colors"> <span class="inline-flex items-center justify-center w-7 h-7 rounded bg-[var(--color-accent)] text-white text-xs font-bold font-mono leading-none">
CA
</span> <span class="text-sm font-medium text-[var(--color-text-muted)] group-hover:text-[var(--color-text)] transition-colors hidden sm:inline">
Charles Azam
</span> </a> <!-- Desktop nav --> <div class="hidden md:flex items-center gap-4"> <nav class="flex gap-1"> <a href="/" class="px-3 py-1.5 rounded text-sm transition-colors text-[var(--color-text-muted)] hover:text-[var(--color-text)] hover:bg-[var(--color-bg)]"> Home </a><a href="/projects" class="px-3 py-1.5 rounded text-sm transition-colors text-[var(--color-text-muted)] hover:text-[var(--color-text)] hover:bg-[var(--color-bg)]"> Projects </a><a href="/blog" class="px-3 py-1.5 rounded text-sm transition-colors text-[var(--color-accent)] bg-[var(--color-accent-light)] font-medium"> Blog </a><a href="/consulting" class="px-3 py-1.5 rounded text-sm transition-colors text-[var(--color-text-muted)] hover:text-[var(--color-text)] hover:bg-[var(--color-bg)]"> Consulting </a><a href="/books" class="px-3 py-1.5 rounded text-sm transition-colors text-[var(--color-text-muted)] hover:text-[var(--color-text)] hover:bg-[var(--color-bg)]"> Books </a> </nav> <div class="w-px h-4 bg-[var(--color-border)]"></div> <a href="/fr/blog/fable-5-gpt-5-6-sol-goal/" class="text-xs font-mono font-medium px-2 py-1 rounded border border-[var(--color-border)] text-[var(--color-text-muted)] hover:text-[var(--color-accent)] hover:border-[var(--color-accent)] transition-all uppercase"> fr </a> </div> <!-- Mobile header right --> <div class="flex items-center gap-3 md:hidden"> <a href="/fr/blog/fable-5-gpt-5-6-sol-goal/" class="text-xs font-mono font-medium px-2 py-1 rounded border border-[var(--color-border)] text-[var(--color-text-muted)] hover:text-[var(--color-accent)] hover:border-[var(--color-accent)] transition-all uppercase"> fr </a> <button id="menu-toggle" class="text-[var(--color-text-muted)] hover:text-[var(--color-text)] transition-colors p-1" aria-label="Toggle menu"> <svg id="menu-icon-open" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"> <path d="M4 7h16M4 12h16M4 17h16"></path> </svg> <svg id="menu-icon-close" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" class="hidden"> <path d="M6 6l12 12M6 18L18 6"></path> </svg> </button> </div> </div> <!-- Mobile menu --> <nav id="mobile-menu" class="md:hidden border-t border-[var(--color-border)] px-6 py-3 space-y-1 bg-[var(--color-bg-secondary)] hidden"> <a href="/" class="block px-3 py-2 rounded text-sm transition-colors text-[var(--color-text-muted)] hover:text-[var(--color-text)] hover:bg-[var(--color-bg)]"> Home </a><a href="/projects" class="block px-3 py-2 rounded text-sm transition-colors text-[var(--color-text-muted)] hover:text-[var(--color-text)] hover:bg-[var(--color-bg)]"> Projects </a><a href="/blog" class="block px-3 py-2 rounded text-sm transition-colors text-[var(--color-accent)] bg-[var(--color-accent-light)] font-medium"> Blog </a><a href="/consulting" class="block px-3 py-2 rounded text-sm transition-colors text-[var(--color-text-muted)] hover:text-[var(--color-text)] hover:bg-[var(--color-bg)]"> Consulting </a><a href="/books" class="block px-3 py-2 rounded text-sm transition-colors text-[var(--color-text-muted)] hover:text-[var(--color-text)] hover:bg-[var(--color-bg)]"> Books </a> </nav> </header> <script type="module">const e=document.getElementById("menu-toggle"),n=document.getElementById("mobile-menu"),o=document.getElementById("menu-icon-open"),s=document.getElementById("menu-icon-close");e.addEventListener("click",()=>{const t=!n.classList.contains("hidden");n.classList.toggle("hidden"),o.classList.toggle("hidden"),s.classList.toggle("hidden"),e.setAttribute("aria-expanded",String(!t))});</script> <main class="flex-1">  <div class="mx-auto flex max-w-7xl gap-16 px-6 py-12 animate-page-in"> <aside class="hidden xl:block w-60 shrink-0"> <div class="sticky top-24 max-h-[calc(100vh-8rem)] overflow-y-auto"> <nav class="toc text-sm" aria-label="On this page"><p class="mb-3 font-mono text-xs uppercase tracking-wider text-[var(--color-text-muted)]">On this page</p><ul class="space-y-1 border-l border-[var(--color-border)]"><li><a href="#the-problem" data-toc-link="the-problem" class="block border-l -ml-px py-1 leading-snug border-transparent text-[var(--color-text-muted)] hover:text-[var(--color-accent)] transition-colors pl-4">The problem</a></li><li><a href="#how-large-is-the-search-space" data-toc-link="how-large-is-the-search-space" class="block border-l -ml-px py-1 leading-snug border-transparent text-[var(--color-text-muted)] hover:text-[var(--color-accent)] transition-colors pl-8 text-[0.8125rem]">How large is the search space?</a></li><li><a href="#what-i-tested" data-toc-link="what-i-tested" class="block border-l -ml-px py-1 leading-snug border-transparent text-[var(--color-text-muted)] hover:text-[var(--color-accent)] transition-colors pl-4">What I tested</a></li><li><a href="#results" data-toc-link="results" class="block border-l -ml-px py-1 leading-snug border-transparent text-[var(--color-text-muted)] hover:text-[var(--color-accent)] transition-colors pl-4">Results</a></li><li><a href="#deep-dive-into-the-goal-command" data-toc-link="deep-dive-into-the-goal-command" class="block border-l -ml-px py-1 leading-snug border-transparent text-[var(--color-text-muted)] hover:text-[var(--color-accent)] transition-colors pl-4">Deep dive into the goal command</a></li><li><a href="#the-same-command-hides-two-different-systems" data-toc-link="the-same-command-hides-two-different-systems" class="block border-l -ml-px py-1 leading-snug border-transparent text-[var(--color-text-muted)] hover:text-[var(--color-accent)] transition-colors pl-4">The same command hides two different systems</a></li><li><a href="#claude-code-a-separate-evaluator" data-toc-link="claude-code-a-separate-evaluator" class="block border-l -ml-px py-1 leading-snug border-transparent text-[var(--color-text-muted)] hover:text-[var(--color-accent)] transition-colors pl-8 text-[0.8125rem]">Claude Code: a separate evaluator</a></li><li><a href="#codex-persisted-state-and-lifecycle-tools" data-toc-link="codex-persisted-state-and-lifecycle-tools" class="block border-l -ml-px py-1 leading-snug border-transparent text-[var(--color-text-muted)] hover:text-[var(--color-accent)] transition-colors pl-8 text-[0.8125rem]">Codex: persisted state and lifecycle tools</a></li><li><a href="#why-goal-can-win-most-runs-and-still-be-a-bad-default" data-toc-link="why-goal-can-win-most-runs-and-still-be-a-bad-default" class="block border-l -ml-px py-1 leading-snug border-transparent text-[var(--color-text-muted)] hover:text-[var(--color-accent)] transition-colors pl-4">Why /goal can win most runs and still be a bad default</a></li><li><a href="#limitations" data-toc-link="limitations" class="block border-l -ml-px py-1 leading-snug border-transparent text-[var(--color-text-muted)] hover:text-[var(--color-accent)] transition-colors pl-4">Limitations</a></li><li><a href="#reproducing-this" data-toc-link="reproducing-this" class="block border-l -ml-px py-1 leading-snug border-transparent text-[var(--color-text-muted)] hover:text-[var(--color-accent)] transition-colors pl-4">Reproducing this</a></li></ul></nav><script type="module">const o=Array.from(document.querySelectorAll("[data-toc-link]"));if(o.length>0){const a=new Map(o.map(e=>[e.dataset.tocLink,e])),r=["!border-[var(--color-accent)]","!text-[var(--color-accent)]","font-medium"],i=e=>{o.forEach(n=>n.classList.remove(...r)),e&&a.get(e)?.classList.add(...r)},s=new Set,c=o.map(e=>document.getElementById(e.dataset.tocLink)).filter(e=>e!==null),d=new IntersectionObserver(e=>{for(const t of e)t.isIntersecting?s.add(t.target.id):s.delete(t.target.id);const n=c.find(t=>s.has(t.id));n&&i(n.id)},{rootMargin:"-80px 0px -66% 0px",threshold:0});c.forEach(e=>d.observe(e))}</script> </div> </aside> <article class="mx-auto w-full max-w-3xl min-w-0"> <a href="/blog" class="inline-flex items-center gap-1 text-sm text-[var(--color-text-muted)] hover:text-[var(--color-accent)] transition-colors mb-8"> <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"> <path d="M10 12L6 8l4-4"></path> </svg>
Blog
</a> <header class="mb-10"> <h1 class="font-[var(--font-display)] text-4xl lg:text-[2.75rem] leading-tight text-[var(--color-text)] mb-4"> Fable 5 vs. GPT-5.6 Sol on an NP-Hard Problem: Does /goal Help? </h1> <div class="flex items-center gap-3 text-sm font-mono text-[var(--color-text-muted)]"> <time> July 17, 2026 </time> <span class="text-[var(--color-border)]">/</span> <span>6 min read</span> </div> </header> <div class="prose prose-lg max-w-none"> <p><strong>TL;DR:</strong> I gave Claude Fable 5 and GPT-5.6 Sol the same unpublished NP-hard
optimization problem, with and without their native <code>/goal</code> mode. Fable 5 is an absolute beast;
<code>/goal</code> is not a game changer.</p>
<p><img alt="Clean score distributions" loading="lazy" decoding="async" fetchpriority="auto" width="1789" height="1164" src="/_astro/fig3_clean_distributions.Ct-GZQ3W_2lndA9.webp" ></p>
<p><strong>Context:</strong> This is an operations research problem originally submitted to students at a
hackathon. I spent a week years
ago writing C++ to solve it, so I have a useful human baseline.</p>
<p>Fable 5 was an absolute beast on this benchmark. It produced the best solution overall, and its
consistency is unlike anything I have seen from a model on this problem. This is pure raw
intelligence. Incredible.</p>
<p>The other result is that <code>/goal</code> is not a generic “try harder” switch. It changes the control
loop and the search path. Sometimes that finds a better basin. Sometimes it gives a bad idea
more time to mature.</p>
<p>All code, prompts, result tables, exclusions, and trajectory notes are in
<a href="https://github.com/charles-azam/CLIArena">CLIArena</a>. This is a follow-up to my
<a href="https://charlesazam.com/blog/kiro-benchmark/">first article about this benchmark</a>.</p>
<hr>
<h2 id="the-problem">The problem</h2>
<p>KIRO is a fiber-network design problem I worked on as an engineering student in 2018. Given
directed distance matrices for Grenoble, Nice, and Paris, the solver has to connect distribution
points and terminals using loops and short chains while respecting several structural
constraints. The objective is total cable length. Lower is better.</p>
<p><img alt="KIRO network structure: a directed loop rooted at a hub with a short branch" loading="lazy" decoding="async" fetchpriority="auto" width="2365" height="1234" src="/_astro/fig0_kiro_problem.CYvcjsCU_Z1X0vi6.webp" ></p>
<p>A valid network consists of redundant loops rooted at distribution hubs, with short branches
hanging from towers on those loops. Every tower must appear exactly once, and reversing a cable
segment can change its cost.</p>
<h3 id="how-large-is-the-search-space">How large is the search space?</h3>
<p>There is no single closed-form count because a solution can use any number of loops, variable
loop sizes, and differently anchored and ordered branches. But Paris alone gives a useful lower
bound.</p>
<p>Even if we ignore ordering and branches and only assign each of the 532 terminals to one of
11 distribution hubs, there are <code>11^532</code> possible assignments.</p>
<p>A stronger lower bound comes from one deliberately restricted family of valid solutions:
exactly 19 loops of 28 terminals each, with no branches. This covers all 532 terminals because
<code>19 x 28 = 532</code>, while staying below the 30-terminal limit for a loop. Order the 532 terminals,
split that ordering into 19 consecutive groups, divide by <code>19!</code> because the set of loops is
unordered, and choose one of the 11 hubs for each loop:</p>
<p><code>(532! / 19!) x 11^19 ~= 10^1223</code></p>
<h2 id="what-i-tested">What I tested</h2>
<p>The primary experiment was intentionally narrow:</p>

































<table><thead><tr><th>Setting</th><th>Value</th></tr></thead><tbody><tr><td>Models</td><td>Claude Fable 5, Opus 4.8, Sonnet 5; GPT-5.6 Sol, Terra, Luna</td></tr><tr><td>Modes</td><td>Plain; native <code>/goal</code></td></tr><tr><td>Optimization budget</td><td>30 minutes</td></tr><tr><td>Outer agent timeout</td><td>1,900 seconds</td></tr><tr><td>Reasoning</td><td>Maximum available setting for every model</td></tr><tr><td>Execution</td><td>Harbor 0.1.43, Docker, subscription authentication</td></tr></tbody></table>
<h2 id="results">Results</h2>
<p>Before concentrating repetitions on the flagship pair, I ran one matched 30-minute no-hint
pair for every model in the sweep. For Fable and Sol, the chart uses Pair 1 from the replicated
headline set; the other four models have one pair each.</p>
<p><img alt="All six models in one matched 30-minute no-hint pair" loading="lazy" decoding="async" fetchpriority="auto" width="2294" height="1244" src="/_astro/fig6_all_models_30min.Cp2VuCKx_Z2jLU4Y.webp" ></p>
<p>I then repeated the flagship comparison until I had three matched runs for Fable 5 and three
for Sol.</p>
<p><img alt="Clean score distributions" loading="lazy" decoding="async" fetchpriority="auto" width="1789" height="1164" src="/_astro/fig3_clean_distributions.Ct-GZQ3W_2lndA9.webp" ></p>






















































<table><thead><tr><th>Model</th><th align="right">Run</th><th align="right">Plain</th><th align="right"><code>/goal</code></th><th align="right">Goal minus plain</th></tr></thead><tbody><tr><td>Fable 5</td><td align="right">1</td><td align="right">32,197</td><td align="right"><strong>31,934</strong></td><td align="right">-263</td></tr><tr><td>Fable 5</td><td align="right">2</td><td align="right">32,516</td><td align="right"><strong>32,324</strong></td><td align="right">-192</td></tr><tr><td>Fable 5</td><td align="right">3</td><td align="right"><strong>32,446</strong></td><td align="right">35,178</td><td align="right">+2,732</td></tr><tr><td>GPT-5.6 Sol</td><td align="right">1</td><td align="right"><strong>33,581</strong></td><td align="right">39,371</td><td align="right">+5,790</td></tr><tr><td>GPT-5.6 Sol</td><td align="right">2</td><td align="right">35,539</td><td align="right"><strong>32,703</strong></td><td align="right">-2,836</td></tr><tr><td>GPT-5.6 Sol</td><td align="right">3</td><td align="right">33,663</td><td align="right"><strong>33,313</strong></td><td align="right">-350</td></tr></tbody></table>
<p>Negative means <code>/goal</code> was better. Goal won four of six trials, so win rate alone makes the
feature look useful. The means tell the other half:</p>


























<table><thead><tr><th>Model</th><th align="right">Plain mean</th><th align="right"><code>/goal</code> mean</th><th align="right">Mean effect</th><th align="right">Median effect</th></tr></thead><tbody><tr><td>Fable 5</td><td align="right"><strong>32,386</strong></td><td align="right">33,145</td><td align="right">+759 worse</td><td align="right">-192 better</td></tr><tr><td>GPT-5.6 Sol</td><td align="right"><strong>34,261</strong></td><td align="right">35,129</td><td align="right">+868 worse</td><td align="right">-350 better</td></tr></tbody></table>
<p>Both models usually got a small benefit and occasionally suffered a large regression. That is
why <code>/goal</code> won most runs but made both means worse.</p>
<p>Fable was also clearly stronger. Its plain mean beat Sol’s by 1,875 points, and its goal mean
beat Sol’s by 1,984. More importantly, Fable plain stayed inside a tiny 319-point range while
Sol plain spanned 1,958 points. Fable goal produced the best clean score, 31,934; Fable plain
was the safest configuration.</p>
<h2 id="deep-dive-into-the-goal-command">Deep dive into the goal command</h2>
<h2 id="the-same-command-hides-two-different-systems">The same command hides two different systems</h2>
<p>Claude Code and Codex both expose <code>/goal</code>, but the implementations are fundamentally different.</p>
<p><img alt="Claude Code and Codex goal architecture" loading="lazy" decoding="async" fetchpriority="auto" width="2574" height="1421" src="/_astro/fig4_goal_architecture.CUL-v7ck_ZQOPcm.webp" ></p>
<h3 id="claude-code-a-separate-evaluator">Claude Code: a separate evaluator</h3>
<p>Claude Code implements <code>/goal</code> as a session-scoped Stop hook. After each main-model turn, a
small evaluator model, Haiku by default, reads the condition and conversation. It returns yes
or no with a reason. A no starts another turn; a yes clears the goal.</p>
<p>The evaluator cannot use tools or inspect files. It can only judge evidence that appeared in
the transcript. That can catch an early exit, but it cannot know whether another ten million
solver iterations are worthwhile. <a href="https://code.claude.com/docs/en/goal">Anthropic’s goal documentation</a></p>
<p>Keep in mind that claude code is not open source, so we rely solely on what Anthropic tells us.</p>
<h3 id="codex-persisted-state-and-lifecycle-tools">Codex: persisted state and lifecycle tools</h3>
<p>I also read the source for the benchmarked release,
<a href="https://github.com/openai/codex/tree/rust-v0.144.4">Codex CLI 0.144.4</a>. Codex treats a goal as
persisted thread state:</p>
<ol>
<li>The TUI saves the objective for the active thread, and SQLite stores its status and budget
accounting. <a href="https://github.com/openai/codex/blob/rust-v0.144.4/codex-rs/tui/src/app/thread_goal_actions.rs#L128-L227">TUI</a>,
<a href="https://github.com/openai/codex/blob/rust-v0.144.4/codex-rs/state/goals_migrations/0001_thread_goals.sql">schema</a></li>
<li>The working model receives <code>create_goal</code>, <code>get_goal</code>, and <code>update_goal</code> tools.
<a href="https://github.com/openai/codex/blob/rust-v0.144.4/codex-rs/ext/goal/src/spec.rs">Tool specification</a></li>
<li>If the thread becomes idle while the goal is active, Codex injects a continuation turn with
the objective and a completion audit. <a href="https://github.com/openai/codex/blob/rust-v0.144.4/codex-rs/ext/goal/src/runtime.rs#L359-L414">Runtime</a>,
<a href="https://github.com/openai/codex/blob/rust-v0.144.4/codex-rs/ext/goal/templates/goals/continuation.md">prompt</a></li>
</ol>
<p>Claude delegates completion to another model. Codex lets the working model declare completion,
then resumes it while the persisted goal remains active. Claude’s evaluator is independent but
sees only the transcript; Codex sees the files and tools but effectively grades its own work.</p>
<h2 id="why-goal-can-win-most-runs-and-still-be-a-bad-default">Why <code>/goal</code> can win most runs and still be a bad default</h2>
<p>On a normal coding task, progress is often legible: another turn can fix a test or complete a
migration. Optimization is different. Once an agent chooses a solver, extra time can amplify
either a good decision or a bad one.</p>
<p>That is exactly what happened here. Goal helped when it sustained Fable’s fast compiled
portfolio or Sol’s successful chain repartition. It hurt when Fable built a slow solver or Sol
committed to an exhaustive anchor sweep. The median moved slightly in the right direction; the
bad tail moved much farther in the wrong one.</p>
<h2 id="limitations">Limitations</h2>
<p>This is one unpublished NP-hard task, not a general coding leaderboard. Only Fable and Sol have
three clean matched pairs. Other comparisons mix prompts, wrapper versions, and time limits,
and the trials ran sequentially through subscription services that may have drifted.</p>
<p>The containers exposed eight CPUs despite task metadata declaring one, which favored Fable’s
parallel portfolios. Every scored Fable and Sol output was valid, partly because the wrapper
required early checkpoints and final verification. The benchmark measures the complete system:
model, CLI, prompt, subscription service, and harness.</p>
<h2 id="reproducing-this">Reproducing this</h2>
<p>The benchmark task, wrappers, analysis scripts, figure generator, and full evidence memo are in
<a href="https://github.com/charles-azam/CLIArena">CLIArena</a>. Raw job directories are excluded from Git
because of their size, but the memo records every publishable score, city breakdown, elapsed
time, strategy, exclusion, and run ID.</p>
<p>The primary commands are:</p>
<pre class="astro-code github-dark" style="background-color:#24292e;color:#e1e4e8; overflow-x: auto;" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#E1E4E8">RUN_ID</span><span style="color:#F97583">=</span><span style="color:#9ECBFF">article-kiro-YYYYMMDD-clean</span><span style="color:#B392F0"> \</span></span>
<span class="line"><span style="color:#E1E4E8">PHASE=nohint-all </span><span style="color:#79B8FF">\</span></span>
<span class="line"><span style="color:#E1E4E8">./scripts/run_subscription_article_matrix.sh</span></span>
<span class="line"></span>
<span class="line"><span style="color:#B392F0">uv</span><span style="color:#9ECBFF"> run</span><span style="color:#9ECBFF"> python</span><span style="color:#9ECBFF"> scripts/summarize_subscription_article_results.py</span><span style="color:#9ECBFF"> RUN_ID...</span></span>
<span class="line"><span style="color:#B392F0">uv</span><span style="color:#9ECBFF"> run</span><span style="color:#9ECBFF"> python</span><span style="color:#9ECBFF"> scripts/analyze_subscription_article_results.py</span><span style="color:#9ECBFF"> RUN_ID...</span></span></code></pre>
<p>The result I would put in the headline is not that goal helps or hurts. It is that a persistence
feature can win most individual trials while making observed average performance worse. On a hard
optimization problem, the quality of the loop matters less than the quality of what the loop
keeps doing.</p> </div> </article> <div class="hidden xl:block w-60 shrink-0" aria-hidden="true"></div> </div>  </main> <footer class="mt-auto bg-[var(--color-bg-secondary)] border-t border-[var(--color-border)]"> <div class="mx-auto max-w-5xl px-6 py-6 flex flex-col sm:flex-row items-center justify-between gap-4"> <p class="text-xs text-[var(--color-text-muted)]">
Charles Azam
</p> <div class="flex gap-5"> <a href="https://www.linkedin.com/in/charles-azam-a4223b135/" target="_blank" rel="noopener noreferrer" class="text-xs font-mono text-[var(--color-text-muted)] hover:text-[var(--color-accent)] transition-colors"> LinkedIn </a><a href="https://github.com/charles-azam" target="_blank" rel="noopener noreferrer" class="text-xs font-mono text-[var(--color-text-muted)] hover:text-[var(--color-accent)] transition-colors"> GitHub </a><a href="https://huggingface.co/charles-azam" target="_blank" rel="noopener noreferrer" class="text-xs font-mono text-[var(--color-text-muted)] hover:text-[var(--color-accent)] transition-colors"> HuggingFace </a><a href="/cdn-cgi/l/email-protection#b6d5d9d8c2d7d5c2f6d7ccd7dbc2d3d5ded8d9dad9d1dfd3c598d5d9db" class="text-xs font-mono text-[var(--color-text-muted)] hover:text-[var(--color-accent)] transition-colors"> Email </a> </div> </div> </footer> </div> <script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script></body></html>