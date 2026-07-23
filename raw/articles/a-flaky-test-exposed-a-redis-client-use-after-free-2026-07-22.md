---
source_url: https://buildkite.engineering/how-a-flaky-test-exposed-a-redis-use-after-free/
ingested: 2026-07-22
sha256: fa213f13b2bbc838fa354d5ce4399de7110f8e406342c4d396144c0438d043c4
blog_source: Hacker News
---
<!DOCTYPE html><html lang="en"> <head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>How a flaky test exposed a Redis use-after-free | Buildkite</title><meta name="description" content="A handful of flaky tests turned out to be a use-after-free in the Redis client's C extension. Here's how we tracked it down."><meta name="author" content="Patrick Robinson"><meta name="keywords" content="debugging, memory-safety, redis, ruby, testing, asan"><link rel="sitemap" href="/sitemap-index.xml"><!-- Visitors --><script src="https://cdn.visitors.now/v.js" data-token="52b0f6fa-945b-4f0e-bcc7-a44e6b438ba0"></script><meta name="theme-color" content="#0d0d0d" media="(prefers-color-scheme: dark)"><meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)"><link rel="canonical" href="https://buildkite.engineering/how-a-flaky-test-exposed-a-redis-use-after-free/"><!-- Open Graph --><meta property="og:title" content="How a flaky test exposed a Redis use-after-free"><meta property="og:locale" content="en_US"><meta property="og:site_name" content="Buildkite"><meta property="og:type" content="article"><meta property="og:logo" content="https://buildkite.engineering/favicon.svg"><meta property="og:description" content="A handful of flaky tests turned out to be a use-after-free in the Redis client's C extension. Here's how we tracked it down."><meta property="og:image" content="https://buildkite.engineering/api/og/how-a-flaky-test-exposed-a-redis-use-after-free.png"><meta property="og:url" content="https://buildkite.engineering/how-a-flaky-test-exposed-a-redis-use-after-free/"><meta property="article:published_time" content="2026-07-03T00:00:00.000Z"><meta property="article:modified_time" content="2026-07-03T00:00:00.000Z"><meta name="twitter:image" content="https://buildkite.engineering/api/og/how-a-flaky-test-exposed-a-redis-use-after-free.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@buildkite"><!-- Favicons --><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png"><link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png"><link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png"><link rel="manifest" href="/manifest.json"><meta name="generator" content="Astro v6.4.8"><!-- Atom feed autodiscovery --><link rel="alternate" type="application/atom+xml" href="/engineering-blog.atom" title="Buildkite Engineering Blog"><link rel="preload" href="/_site/assets/fonts/Aeonik-Medium.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/_site/assets/fonts/Aeonik-Bold.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/_site/assets/fonts/DepartureMono-Regular.woff2" as="font" type="font/woff2" crossorigin><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600&display=swap" rel="stylesheet"><!-- Additional head content (JSON-LD, etc.) --><script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"How a flaky test exposed a Redis use-after-free","description":"A handful of flaky tests turned out to be a use-after-free in the Redis client's C extension. Here's how we tracked it down.","author":{"@type":"Person","name":"Patrick Robinson"},"publisher":{"@type":"Organization","name":"Buildkite","logo":{"@type":"ImageObject","url":"https://buildkite.engineering/favicon.svg"}},"datePublished":"2026-07-03T00:00:00.000Z","dateModified":"2026-07-03T00:00:00.000Z","mainEntityOfPage":{"@type":"WebPage","@id":"https://buildkite.engineering/how-a-flaky-test-exposed-a-redis-use-after-free/"},"keywords":"debugging, memory-safety, redis, ruby, testing, asan","articleSection":"debugging","wordCount":1686}</script><!-- Post-specific favicon (overrides the site default) --><link rel="icon" type="image/svg+xml" href="/api/favicon/how-a-flaky-test-exposed-a-redis-use-after-free.svg"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.BUui_hpL.js?dpl=dpl_GUsYzL9AtA14GPmsoXvU9E3xKmM4"></script><link rel="stylesheet" href="/_astro/particle-figure.Cn5l4_ZQ.css"><script type="module" src="/_astro/page.CEOVVaB0.js"></script><style>[data-astro-transition-scope="astro-2rpjnfor-1"] { view-transition-name: buildkite-logo; }@layer astro { ::view-transition-old(buildkite-logo) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(buildkite-logo) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(buildkite-logo) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(buildkite-logo) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; } }[data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-2rpjnfor-1"],
			[data-astro-transition-fallback="old"][data-astro-transition-scope="astro-2rpjnfor-1"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-2rpjnfor-1"],
			[data-astro-transition-fallback="new"][data-astro-transition-scope="astro-2rpjnfor-1"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back][data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-2rpjnfor-1"],
			[data-astro-transition=back][data-astro-transition-fallback="old"][data-astro-transition-scope="astro-2rpjnfor-1"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back][data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-2rpjnfor-1"],
			[data-astro-transition=back][data-astro-transition-fallback="new"][data-astro-transition-scope="astro-2rpjnfor-1"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-4iwcmdxz-2"] { view-transition-name: buildkite-logo; }@layer astro { ::view-transition-old(buildkite-logo) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(buildkite-logo) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(buildkite-logo) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(buildkite-logo) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; } }[data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-4iwcmdxz-2"],
			[data-astro-transition-fallback="old"][data-astro-transition-scope="astro-4iwcmdxz-2"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-4iwcmdxz-2"],
			[data-astro-transition-fallback="new"][data-astro-transition-scope="astro-4iwcmdxz-2"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back][data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-4iwcmdxz-2"],
			[data-astro-transition=back][data-astro-transition-fallback="old"][data-astro-transition-scope="astro-4iwcmdxz-2"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back][data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-4iwcmdxz-2"],
			[data-astro-transition=back][data-astro-transition-fallback="new"][data-astro-transition-scope="astro-4iwcmdxz-2"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }</style><style>@media(min-width:768px){div[data-astro-cid-liaill72]>p:has(img){width:var(--media-img-w)}}
</style></head> <body class="engineering-blog-page flex min-h-screen flex-col bg-eng-blog-background text-eng-blog-foreground">     <div class="lg:hidden"> <header class="mb-6 flex max-w-267 items-center w-full justify-between px-6 pt-6 min-[1600px]:mx-auto"> <div class="flex items-center"> <a href="/" aria-label="Buildkite Engineering — home" class="group flex items-center gap-3 font-sans text-lg tracking-normal transition-colors text-white"> <div class="mx-auto size-18 items-center justify-center group-hover:text-eng-blog-accent" data-astro-transition-scope="astro-4iwcmdxz-2"> <svg xmlns="http://www.w3.org/2000/svg" class="size-18 self-center" viewBox="0 0 28 19" fill="none"> <path fill-rule="evenodd" clip-rule="evenodd" d="M9.332 4.71 0 0v9.499l9.332 4.713L18.74 9.5V19L28 14.212V4.711L18.74 0 9.332 4.71Z" fill="#30F2A2"></path> <path d="M18.74 0 9.332 4.71v9.502L18.74 9.5V0ZM28 4.71 18.74 9.5V19L28 14.212" fill="#14CC80"></path> </svg> </div> </a> </div> <div class="flex items-center gap-8"> <div class="flex items-center gap-2 text-[10px] text-eng-blog-muted-foreground"> <a href="/engineering-blog.atom" class="group relative flex cursor-pointer items-baseline gap-2 font-sans text-xs tracking-[0.2em] text-eng-blog-muted-foreground no-underline"> <span class="relative z-10 text-[13px] leading-none text-eng-blog-foreground/30 transition-all duration-200 group-hover:translate-x-0.5 group-hover:text-white" style="transition-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1);">
[
</span> <span class="relative text-[14px] z-10 translate-y-px leading-none tracking-widest transition-colors duration-200 text-eng-blog-foreground/90 group-hover:text-white">
RSS
</span> <span class="relative z-10 text-[13px] leading-none text-eng-blog-foreground/30 transition-all duration-200 group-hover:-translate-x-0.5 group-hover:text-white" style="transition-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1);">
]
</span> </a> </div> </div> </header> </div> <div class="eng-blog-post-grid"> <!-- Full-width header: logo + title --> <div class="eng-blog-post-header group/hdr"> <header class="mb-6 items-center justify-between px-8 hidden lg:flex w-full"> <div class="flex items-center"> <a href="/" aria-label="Buildkite Engineering — home" class="logo-link group flex items-center gap-3 font-sans text-lg tracking-normal transition-colors text-white"> <div class="mx-auto size-18 items-center justify-start group-hover:text-eng-blog-accent" data-astro-transition-scope="astro-2rpjnfor-1"> <svg xmlns="http://www.w3.org/2000/svg" class="logo-animated size-18" viewBox="0 0 28 19" fill="none"> <path class="chevron-piece-1" d="M9.332 4.71 0 0v9.499l9.332 4.713V4.71Z" fill="#30F2A2"></path> <path class="chevron-piece-2" d="M9.332 4.71v9.502L18.74 9.5V0L9.332 4.71Z" fill="#14CC80"></path> <g class="right-box"> <path d="M18.74 0v9.5L28 4.711 18.74 0Z" fill="#30F2A2"></path> <path d="M18.74 9.5V19L28 14.212V4.71L18.74 9.5Z" fill="#30F2A2"></path> <path d="M28 4.71 18.74 9.5V19L28 14.212V4.71Z" fill="#14CC80"></path> </g> </svg> </div> </a> </div> <div class="flex items-center gap-8"> <div class="flex items-center gap-2 text-[10px] text-eng-blog-muted-foreground"> <a href="/engineering-blog.atom" class="group relative flex cursor-pointer items-baseline gap-2 font-sans text-xs tracking-[0.2em] text-eng-blog-muted-foreground no-underline"> <span class="relative z-10 text-[13px] leading-none text-eng-blog-foreground/30 transition-all duration-200 group-hover:translate-x-0.5 group-hover:text-white" style="transition-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1);">
[
</span> <span class="relative text-[14px] z-10 translate-y-px leading-none tracking-widest transition-colors duration-200 text-eng-blog-foreground/90 group-hover:text-white">
RSS
</span> <span class="relative z-10 text-[13px] leading-none text-eng-blog-foreground/30 transition-all duration-200 group-hover:-translate-x-0.5 group-hover:text-white" style="transition-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1);">
]
</span> </a> </div> </div> </header> <div class="group relative mb-12 rounded-none border border-eng-blog-border bg-eng-blog-card ring-1 ring-black/5"> <hr class="absolute left-0 -top-px w-24 md:w-32 bg-linear-to-r h-px border-0 from-emerald-300/0 via-emerald-300/60 to-emerald-300/0 transition-[width] duration-200 group-has-[.logo-link:hover]/hdr:w-18 group-has-[.logo-link:hover]/hdr:left-4"> <div class="flex items-center justify-between border-b border-eng-blog-border px-2 py-2 bg-[radial-gradient(15%_90%_at_8%_0%,rgba(0,247,156,0.05)_0%,rgba(0,247,156,0)_100%)]"> <span class="font-mono-pixel text-[10px] tracking-wider bg-clip-text bg-linear-to-b from-emerald-500 from-0% to-70% to-eng-blog-muted-foreground text-transparent uppercase">/vibe_check</span> <div class="flex items-center gap-0.5"> <span class="inline-flex gap-1 items-center font-mono-pixel text-[10px] rounded-xs px-1 bg-sky-300/15 text-code-blue">
Opinion
</span> <span class="inline-flex gap-1 items-center font-mono-pixel text-[10px] rounded-xs px-1 bg-amber-300/15 text-code-orange">
Story
</span>  <span class="inline-flex gap-1 items-center font-mono-pixel text-[10px] rounded-xs px-1 bg-red-300/15 text-code-red">
Lessons
</span> <span class="inline-flex gap-1 items-center font-mono-pixel text-[10px] rounded-xs px-1 bg-indigo-300/15 text-code-purple">
Craft
</span> <span class="inline-flex gap-1 items-center font-mono-pixel text-[10px] rounded-xs px-1 bg-emerald-300/15 text-code-green">
Code
</span> </div> </div> <p class="sr-only">Article composition: Story 30%, Craft 23%, Lessons 22%, Code 13%, Opinion 12%</p> <div class="not-prose overflow-hidden bg-eng-blog-card/80 rounded-none h-[200px] md:h-[300px]"> <canvas data-particle-figure data-mode="pour" data-word="REDIS" data-gridpx="9" data-cursor-radius="170" data-max-particles="10000" data-weights="{&quot;Story&quot;:90,&quot;Craft&quot;:70,&quot;Lessons&quot;:65,&quot;Code&quot;:40,&quot;Opinion&quot;:35}" class="block h-full w-full " aria-hidden="true"></canvas> <script type="module" src="/_astro/particle-figure.astro_astro_type_script_index_0_lang.Ds8zxMuO.js?dpl=dpl_GUsYzL9AtA14GPmsoXvU9E3xKmM4"></script> </div> </div> <h1 class="eng-blog-h1 font-eng-blog-heading font-normal text-pretty"> How a flaky test exposed a Redis use-after-free </h1> </div> <!-- Left Sidebar: metadata + TOC --> <aside class="eng-blog-post-sidebar"> <div class="eng-blog-post-sidebar-sticky pb-0 lg:pb-12"> <!-- Metadata --> <dl class="eng-blog-meta"> <div class="eng-blog-meta-row"> <dt class="eng-blog-meta-dt">Date</dt> <dd class="eng-blog-meta-dd"> <time datetime="2026-07-03">Jul 3, 2026</time> </dd> </div> <div class="eng-blog-meta-row"> <dt class="eng-blog-meta-dt">Author</dt> <dd class="eng-blog-meta-dd">Patrick Robinson</dd> </div> <div class="eng-blog-meta-row"> <dt class="eng-blog-meta-dt">Read time</dt> <dd class="eng-blog-meta-dd">9 min read</dd> </div>  <div class="eng-blog-meta-row"> <dt class="eng-blog-meta-dt">Agents</dt> <dd class="eng-blog-meta-dd"> <div class="eng-blog-meta-actions"> <button type="button" class="eng-blog-meta-action" data-copy-md="/how-a-flaky-test-exposed-a-redis-use-after-free.md">
Copy for LLMs
</button> <a class="eng-blog-meta-action" href="/how-a-flaky-test-exposed-a-redis-use-after-free.md" target="_blank" rel="noopener">
View as markdown
</a> </div> </dd> </div> <div class="eng-blog-meta-row"> <dt class="eng-blog-meta-dt">Share</dt> <dd class="eng-blog-meta-dd"> <div class="eng-blog-meta-actions"> <a href="https://twitter.com/share?url=https%3A%2F%2Fbuildkite.engineering%2Fhow-a-flaky-test-exposed-a-redis-use-after-free%2F%3Futm_source%3Dreferral%26utm_medium%3DTwitter&amp;text=Read%20How%20a%20flaky%20test%20exposed%20a%20Redis%20use-after-free%20on%20%40buildkite%20blog" target="_blank" rel="noopener noreferrer" class="eng-blog-meta-action">
Twitter/X
</a> <a href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A%2F%2Fbuildkite.engineering%2Fhow-a-flaky-test-exposed-a-redis-use-after-free%2F%3Futm_source%3Dreferral%26utm_medium%3DLinkedIn" target="_blank" rel="noopener noreferrer" class="eng-blog-meta-action">
LinkedIn
</a> </div> </dd> </div> </dl> <!-- TOC (fades in on scroll) --> <div class="eng-blog-post-toc mt-10"> <div class="eng-blog-sidebar"> <!-- CONTENTS (conditional) --> <div class="eng-blog-sidebar-section" data-toc-visible="false"> <!-- <div class='eng-blog-sidebar-section-label'>
    <span>{label}</span>
  </div> --> <div>  <nav aria-label="Table of contents"><a href="#chapter-1-bounce" class="eng-blog-sidebar-toc-item" style="--indent: 0" data-heading-slug="chapter-1-bounce">Chapter 1: Bounce</a><a href="#chapter-2fade-to-black" class="eng-blog-sidebar-toc-item" style="--indent: 0" data-heading-slug="chapter-2fade-to-black">Chapter 2: Fade to Black</a><a href="#chapter-3-everlong" class="eng-blog-sidebar-toc-item" style="--indent: 0" data-heading-slug="chapter-3-everlong">Chapter 3: Everlong</a><a href="#epilogue-in-the-end" class="eng-blog-sidebar-toc-item" style="--indent: 0" data-heading-slug="epilogue-in-the-end">Epilogue: In the End</a></nav><script type="module">function l(){const r=document.querySelectorAll(".eng-blog-sidebar-toc-item");if(r.length===0)return;const i=Array.from(document.querySelectorAll(".eng-blog-prose h2, .eng-blog-prose h3, .eng-blog-prose h4")),o=new IntersectionObserver(e=>{e.forEach(t=>{const c=t.target.getAttribute("id"),n=document.querySelector(`.eng-blog-sidebar-toc-item[data-heading-slug="${c}"]`);t.isIntersecting&&(r.forEach(a=>a.removeAttribute("data-active")),n&&n.setAttribute("data-active","true"))})},{rootMargin:"-100px 0px -66%",threshold:1});i.forEach(e=>{o.observe(e)}),r.forEach(e=>{e.addEventListener("click",t=>{t.preventDefault();const c=e.getAttribute("href");if(c){const n=document.querySelector(c);n&&n.scrollIntoView({behavior:"smooth",block:"start"})}})})}function d(){const r=document.querySelector(".eng-blog-sidebar-section"),i=document.querySelector(".eng-blog-post-sidebar-sticky");if(!r)return;let o=null;const e=()=>{o&&cancelAnimationFrame(o),o=requestAnimationFrame(()=>{const t=window.scrollY>0;r.setAttribute("data-toc-visible",t?"true":"false"),i&&(i.setAttribute("data-has-scrolled",t?"true":"false"),i.setAttribute("data-header-hidden",t?"true":"false"))})};e(),window.addEventListener("scroll",e,{passive:!0}),document.addEventListener("astro:before-preparation",()=>{window.removeEventListener("scroll",e),o&&cancelAnimationFrame(o)})}function s(){l(),d()}s();document.addEventListener("astro:page-load",s);
//# sourceMappingURL=sidebar-toc.astro_astro_type_script_index_0_lang.5hs9WJqp.js.map</script>  </div>  </div> </div> </div> </div> </aside> <!-- Main Content --> <main class="eng-blog-post-content pt-0 pb-20"> <!-- Article --> <article class="eng-blog-prose">  <div class="eng-blog-content"> <p>It can be hard to fix a bug even when it happens deterministically; replicating the circumstances that trigger it is often the hardest step. When a bug is non-deterministic this becomes harder: we need to execute the code that reproduces it many times in order to observe the behaviour, which adds significant time to our feedback loop. Harder still is when the cause of the bug happens prior to its manifestation —when data is corrupted but we don’t immediately notice it. Our usual tools focus on capturing the state of the system at the time a crash happens, which doesn’t tell us why the corruption happened in the first place, just that it happened.</p>
<p>This is the tale of a memory corruption bug we found in the <a href="https://github.com/redis-rb/redis-client">redis-client library</a> and what helped us get there.</p>
<h2 id="chapter-1-bounce">Chapter 1: <strong>Bounce</strong></h2>
<p><a href="https://genius.com/2817913/System-of-a-down-bounce/Jump-bounce-down-up"><em>Jump! Bounce! Down! Up!</em></a></p>
<div class="flex flex-col md:flex-row gap-6 md:items-start my-8 [&amp;>p]:my-0 [&amp;>p>img]:my-0 [&amp;>p>img]:w-full md:[&amp;>p:not(:has(img))]:flex-1 md:[&amp;>p:has(img)]:shrink-0 " style="--media-img-w:170px" data-astro-cid-liaill72> <p>Our story starts with David, an engineering manager on our Scalability team. One idle Tuesday, David saw a build of his had failed due to what appeared to be a number of flaky tests. He started a thread in Slack to alert others and included a screenshot from the <a href="https://buildkite.com/docs/pipelines/configure/tests">Test Engine</a> dashboard.</p><p><img src="/_astro/1-david.BAMM5Om7_1Tb5Oq.webp?dpl=dpl_GUsYzL9AtA14GPmsoXvU9E3xKmM4" alt="David, an engineering manager on our Scalability team." loading="lazy" decoding="async" width="512" height="512"></p> </div>
<p><img src="/_astro/2-test-suite-trend.DpcIJqZa_YgAFY.webp?dpl=dpl_GUsYzL9AtA14GPmsoXvU9E3xKmM4" alt="Test Engine reliability trend showing the tests dropping from ~100% reliable." loading="lazy" decoding="async" width="1584" height="672"></p>
<p>As a continuous integration company, we are intimately familiar with flaky tests —they are an inevitable part of any large codebase. Within 15 minutes, the team pulled the Andon Cord; these tests were so flaky they were preventing us deploying code to production. As David summarised it, “[the] priority is getting main unblocked”, so we worked to exclude the tests from our suite temporarily.</p>
<p>With the urgency reduced, David and the many other developers blocked by this hiccup were free to go back to their original tasks. David, though, decided to take a slightly deeper look by inspecting the reliability of these tests using Buildkite’s Test Engine reliability score, to see if he could correlate when they suddenly became unstable.</p>
<blockquote>
<p>It seems the three worst flakeys went from ~100% reliable to… not around [2-4 days prior]. I’ve had a look through merged PRs to see if I can spot what might have contributed to that change, but can’t see anything obvious…
Only thing that jumps out is the redis upgrade?</p>
</blockquote>
<div class="flex flex-col md:flex-row gap-6 md:items-start my-8 [&amp;>p]:my-0 [&amp;>p>img]:my-0 [&amp;>p>img]:w-full md:[&amp;>p:not(:has(img))]:flex-1 md:[&amp;>p:has(img)]:shrink-0 " style="--media-img-w:170px" data-astro-cid-liaill72> <p><img src="/_astro/3-patrick.C0iyQ3dZ_5Q5s.webp?dpl=dpl_GUsYzL9AtA14GPmsoXvU9E3xKmM4" alt="Patrick Robinson, staff engineer and part-time blog post narrator." loading="lazy" decoding="async" width="512" height="512"></p><p>That Redis upgrade was done on the prior Friday afternoon by a staff engineer, and part time blog post narrator, Patrick Robinson. Patrick loves few things more than talking about himself in the third person; one of those things is getting deep into gnarly bugs.</p> </div>
<p>Here’s our first clue: the Redis gem upgrade had gone smoothly with no hint of any production issues. At this point, though, a second hypothesis appeared: the tests were flaky because they depended on a certain sequence of events. See, the flaky tests were part of our feature test suite; they utilised not just RSpec but also a Selenium headless browser and a test environment comprising of a web/API server, database and Redis server. In these situations, race conditions between the different components are a common cause of flaky tests. Unfortunately, this would lead our investigators off track.</p>
<aside role="note" aria-label="Tip" class="relative my-8 overflow-hidden border-l-[3px] bg-eng-blog-accent/[0.06] border-l-eng-blog-accent"><div class="relative flex gap-4 px-5 py-4"><div class="shrink-0 pt-0.5 text-eng-blog-accent"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon" class="size-5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 18v-5.25m0 0a6.01 6.01 0 0 0 1.5-.189m-1.5.189a6.01 6.01 0 0 1-1.5-.189m3.75 7.478a12.06 12.06 0 0 1-4.5 0m3.75 2.383a14.406 14.406 0 0 1-3 0M14.25 18v-.192c0-.983.658-1.823 1.508-2.316a7.5 7.5 0 1 0-7.517 0c.85.493 1.509 1.333 1.509 2.316V18"></path></svg></div><div class="flex-1 space-y-2"><div class="font-eng-blog-mono text-sm font-medium leading-tight tracking-tight text-eng-blog-accent">Occam’s Razor</div><div class="text-[15px] leading-relaxed text-eng-blog-muted-foreground [&amp;&gt;p]:mb-2 [&amp;&gt;p:last-child]:mb-0 [&amp;&gt;code]:rounded [&amp;&gt;code]:bg-eng-blog-card [&amp;&gt;code]:px-1.5 [&amp;&gt;code]:py-0.5 [&amp;&gt;code]:text-[13px] [&amp;&gt;code]:font-eng-blog-mono [&amp;&gt;code]:text-eng-blog-accent [&amp;&gt;code]:border [&amp;&gt;code]:border-eng-blog-border/50"><p>When faced with competing explanations, the simplest is the most likely correct.</p></div></div></div></aside>
<p>So the suggestion was to slap a sleep in between the test setup and assertions to see if it made the problem go away. This wasn’t a solution, but a way of establishing if the flakiness was the result of a WebSocket message taking slightly too long to arrive.</p>
<h2 id="chapter-2fade-to-black">Chapter 2: <strong>Fade to Black</strong></h2>
<p><a href="https://open.spotify.com/track/12oSzrBIyirNs0aCwk6elL"><em>Life, it seems, will fade away<br/>
Drifting further every day<br/>
Getting lost within myself<br/>
Nothing matters, no one else</em></a></p>
<p>The following Monday, more tests were failing sporadically in the same file as those that had been skipped. Patrick worked with another of our staff engineers who could, unlike Patrick, write actual frontend code. Together they managed to build a reliable reproduction of the bug, although it took up to 30 minutes to produce a failure. After eliminating the possibility of a race condition where messages were delivered after the test suite had run, the team narrowed in on the interactions between ActionCable and Redis.</p>
<aside role="note" aria-label="Note" class="relative my-8 overflow-hidden border-l-[3px] bg-eng-blog-card/60 border-l-eng-blog-border"><div class="relative flex gap-4 px-5 py-4"><div class="shrink-0 pt-0.5 text-eng-blog-muted-foreground"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon" class="size-5"><path stroke-linecap="round" stroke-linejoin="round" d="m11.25 11.25.041-.02a.75.75 0 0 1 1.063.852l-.708 2.836a.75.75 0 0 0 1.063.853l.041-.021M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9-3.75h.008v.008H12V8.25Z"></path></svg></div><div class="flex-1 space-y-2"><div class="text-[15px] leading-relaxed text-eng-blog-muted-foreground [&amp;&gt;p]:mb-2 [&amp;&gt;p:last-child]:mb-0 [&amp;&gt;code]:rounded [&amp;&gt;code]:bg-eng-blog-card [&amp;&gt;code]:px-1.5 [&amp;&gt;code]:py-0.5 [&amp;&gt;code]:text-[13px] [&amp;&gt;code]:font-eng-blog-mono [&amp;&gt;code]:text-eng-blog-accent [&amp;&gt;code]:border [&amp;&gt;code]:border-eng-blog-border/50"><p><a href="https://guides.rubyonrails.org/action_cable_overview.html">ActionCable</a> is the Ruby on Rails framework for WebSockets. It requires a PubSub queue, such as Redis, to support delivering messages to connected clients. This supports features such as updating the icon of a Build when it changes state.</p></div></div></div></aside>
<p>By adding additional logging, they found the <code>subscribe</code> command was being delivered to ActionCable but wasn’t being received by Redis. Other developers also reported WebSockets often failing in development, indicating it was not only the test environment that was impacted.</p>
<p>At the end of the third day of debugging, seemingly getting nowhere, Patrick got a very unusual error message, which he posted to Slack with the departing words “I think it’s time to give up for the night…”:</p>
<div class="group relative my-6 rounded-none bg-eng-blog-card/0 px-1 pb-1 shadow-[inset_0_0_0_1px_rgba(255,255,255,.09),0_12px_28px_-8px_rgba(0,0,0,.05)] ring-1 ring-black/5"><div class="flex items-center justify-between border-eng-blog-border/50 px-2 pt-2 pb-1 md:px-2"><div class="flex items-center gap-3"><span class="font-mono-pixel text-[10px] tracking-wider text-eng-blog-muted-foreground/70 uppercase">text</span></div></div><div class="relative"><div class="CodeBlock not-prose overflow-x-auto bg-eng-blog-card/80 p-2 text-sm md:px-4 rounded-none border border-eng-blog-border/60"><pre class="shiki github-dark" style="background-color:#24292e;color:#e1e4e8" tabindex="0"><code><span class="line"><span>ruby(29632,0x2a9f1f000) malloc: Double free of object 0x2a9bb6740</span></span>
<span class="line"><span>ruby(29632,0x2a9f1f000) malloc: *** set a breakpoint in malloc_error_break to debug</span></span></code></pre></div><button class="absolute top-2.5 right-2.5 flex h-7 w-7 items-center justify-center rounded transition-all bg-eng-blog-background/80 text-eng-blog-muted-foreground hover:text-eng-blog-foreground opacity-0 group-hover:opacity-100 focus:opacity-100" aria-label="Copy code" title="Copy code"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-copy h-3.5 w-3.5"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"></rect><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path></svg></button></div></div>
<p>This kind of exception is quite unusual and hints at how deep this bug goes. But the team hadn’t quite gathered enough information to recognise how or even if it related to the failure. Like an installment of the blockbuster movie series Knives Out, even with all the information, it still didn’t make sense.</p>
<blockquote>
<p>And yet, with all the pieces on the table, this crime still truly appears impossible.
<em>~ Benoit Blanc</em></p>
</blockquote>
<h2 id="chapter-3-everlong">Chapter 3: Everlong</h2>
<p><a href="https://open.spotify.com/track/5UWwZ5lm5PKu6eKsHAGxOk"><em>Hello<br/>
I’ve waited here for you<br/>
Everlong</em></a></p>
<p>Successful debugging requires a good dose of skill and a pinch of luck. Late on the following Thursday afternoon, a message was posted in our engineering Slack channel that a build had triggered a segmentation fault. Attached to the build was a core dump.</p>
<aside role="note" aria-label="Note" class="relative my-8 overflow-hidden border-l-[3px] bg-eng-blog-card/60 border-l-eng-blog-border"><div class="relative flex gap-4 px-5 py-4"><div class="shrink-0 pt-0.5 text-eng-blog-muted-foreground"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon" class="size-5"><path stroke-linecap="round" stroke-linejoin="round" d="m11.25 11.25.041-.02a.75.75 0 0 1 1.063.852l-.708 2.836a.75.75 0 0 0 1.063.853l.041-.021M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9-3.75h.008v.008H12V8.25Z"></path></svg></div><div class="flex-1 space-y-2"><div class="text-[15px] leading-relaxed text-eng-blog-muted-foreground [&amp;&gt;p]:mb-2 [&amp;&gt;p:last-child]:mb-0 [&amp;&gt;code]:rounded [&amp;&gt;code]:bg-eng-blog-card [&amp;&gt;code]:px-1.5 [&amp;&gt;code]:py-0.5 [&amp;&gt;code]:text-[13px] [&amp;&gt;code]:font-eng-blog-mono [&amp;&gt;code]:text-eng-blog-accent [&amp;&gt;code]:border [&amp;&gt;code]:border-eng-blog-border/50"><p>A <a href="https://en.wikipedia.org/wiki/Segmentation_fault">segmentation fault</a> (segfault) is an error condition raised by the CPU when a program attempts to access memory outside its permitted range. Typically this results in the operating system sending a signal to the process that causes it to crash.</p><p>A core dump is a snapshot of the program memory and registers at the time it crashed and is often generated in response to an unrecoverable error such as a segfault.</p></div></div></div></aside>
<p>The core dump was attached because one of our developers was previously trying to debug a crash in the test suite, and had written a plugin to look for the presence of a core dump and, if one was found, upload it to the relevant build as an artifact.</p>
<div class="flex flex-col md:flex-row gap-6 md:items-start my-8 [&amp;>p]:my-0 [&amp;>p>img]:my-0 [&amp;>p>img]:w-full md:[&amp;>p:not(:has(img))]:flex-1 md:[&amp;>p:has(img)]:shrink-0 " style="--media-img-w:170px" data-astro-cid-liaill72> <p>That means it’s time to introduce our third character, Rian, who during his tenure at Buildkite developed a reputation for finding and fixing incredibly obscure bugs (along with the infamous <a href="https://buildkite.com/platform/pipelines/doom/">Doom pipeline</a>). The stories are so great that despite Rian’s departure we tell them to new hires, who retell them to others and so on and so forth.</p><p><img src="/_astro/4-rian.BH3NhkJ4_Z13kl3K.webp?dpl=dpl_GUsYzL9AtA14GPmsoXvU9E3xKmM4" alt="Rian, our third character, renowned for hunting down obscure bugs." loading="lazy" decoding="async" width="192" height="192"></p> </div>
<p>The core dump enabled Rian to inspect the state of the process at the time it crashed, akin to a black box in an aircraft crash investigation. The crash message itself indicated it happened inside the hiredis code, which is a C extension bundled into the redis-client gem. From this, he ascertained that the exception was triggered by a call to the C function <code>memmove</code>. While the source and destination addresses for this call looked sane, the size field was set to <code>0x00a0ffffffffffb6</code> , which is about 45 petabytes. Based on this and the fact we’d been seeing other unexpected behaviour since upgrading the Redis gem, it was logical to conclude a memory corruption bug was present in the newest version.</p>
<p>By another stroke of luck, Rian had attended a conference talk earlier in the year called <a href="https://www.youtube.com/watch?v=yM1us32z-9I">Finding and fixing memory safety bugs in C with ASAN</a>.</p>
<aside role="note" aria-label="Note" class="relative my-8 overflow-hidden border-l-[3px] bg-eng-blog-card/60 border-l-eng-blog-border"><div class="relative flex gap-4 px-5 py-4"><div class="shrink-0 pt-0.5 text-eng-blog-muted-foreground"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon" class="size-5"><path stroke-linecap="round" stroke-linejoin="round" d="m11.25 11.25.041-.02a.75.75 0 0 1 1.063.852l-.708 2.836a.75.75 0 0 0 1.063.853l.041-.021M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9-3.75h.008v.008H12V8.25Z"></path></svg></div><div class="flex-1 space-y-2"><div class="text-[15px] leading-relaxed text-eng-blog-muted-foreground [&amp;&gt;p]:mb-2 [&amp;&gt;p:last-child]:mb-0 [&amp;&gt;code]:rounded [&amp;&gt;code]:bg-eng-blog-card [&amp;&gt;code]:px-1.5 [&amp;&gt;code]:py-0.5 [&amp;&gt;code]:text-[13px] [&amp;&gt;code]:font-eng-blog-mono [&amp;&gt;code]:text-eng-blog-accent [&amp;&gt;code]:border [&amp;&gt;code]:border-eng-blog-border/50"><p><a href="https://www.osc.edu/resources/getting_started/howto/howto_use_address_sanitizer">Address Sanitiser</a> (ASAN) is an open source tool, developed by Google, that enables detection of memory safety bugs including use-after-free. Because C is not garbage collected and, unlike Rust, doesn’t provide guardrails to prevent memory safety errors, it’s relatively easy to accidentally write code that reads a page of memory that was already freed. This results in unexpected consequences, from segmentation faults to data corruption.</p></div></div></div></aside>
<p>With this information, Rian set to work getting the reproducible code running in a version of Ruby compiled with ASAN. It only took a couple of hours to get this running, and within 30 minutes ASAN reported a heap use-after-free. In order to provide concurrent execution, hiredis has two threads for each connection, one for reading and one for writing. The use-after-free was happening because in some scenarios <a href="https://github.com/redis-rb/redis-client/blob/6d55f61cac62af91aebbd5a1d00eae7a8d940b9e/hiredis-client/ext/redis_client/hiredis/hiredis_connection.c#L741-L761">the reader thread would free the writer buffer</a>.</p>
<h2 id="epilogue-in-the-end">Epilogue: <strong>In the End</strong></h2>
<p><a href="https://open.spotify.com/track/60a0Rd6pjrkxjPbaKzXjfq"><em>I’m surprised it got so far<br/>
Things aren’t the way they were before<br/>
You wouldn’t even recognize me anymore<br/>
Not that you knew me back then, but it all comes back to me in the end</em></a></p>
<p>Once we knew that there was memory corruption and, more importantly, where it was coming from, fixing it was relatively straightforward. Rian disabled using the C extension for Redis connections in test, development and production, and developed a reproducible test case that was <a href="https://github.com/redis-rb/redis-client/issues/208">reported upstream</a>.</p>
<p>What enabled us to find it in the first place is the interesting part. A combination of deliberate application of our skills in building the necessary tooling, teamwork, and just the right amount of luck. Our tools, such as <a href="https://buildkite.com/docs/pipelines/configure/tests">Test Engine</a> and our <a href="https://github.com/buildkite-plugins/coredump-artifact-buildkite-plugin">coredump-artifact</a> plugin, enabled us to identify the nature of the bug and, combined with using ASAN, where it manifested. Memory corruption bugs such as these can often <a href="https://web.archive.org/web/20211129172859/https://webuild.envato.com/blog/tracking-down-ruby-heap-corruption/">take months</a> to fix, because having a core dump generated by a segfault only tells you that memory was corrupted at some point in the past, but gives you few clues as to how it became corrupt.</p>
<p><em>No production data was harmed in the making of this story.</em></p> </div> </article> <footer class="mt-auto border-t border-eng-blog-border pt-12"> <p class="font-eng-blog-mono text-[11px] tracking-widest text-eng-blog-muted-foreground uppercase">
© 2026 Buildkite
</p> </footer> </main> </div> <script type="module">function o(){document.querySelectorAll("[data-copy-md]").forEach(t=>{t.dataset.bound||(t.dataset.bound="true",t.addEventListener("click",async()=>{const a=t.dataset.copyMd;if(!a)return;const r=t.textContent;try{const e=await fetch(a);if(!e.ok)throw new Error(`HTTP ${e.status}`);await navigator.clipboard.writeText(await e.text()),t.textContent="Copied!"}catch{t.textContent="Copy failed"}setTimeout(()=>{t.textContent=r},1500)}))})}o();document.addEventListener("astro:page-load",o);
//# sourceMappingURL=_slug_.astro_astro_type_script_index_0_lang.DSMyqAqU.js.map</script>  <script>
      // Use the site's existing theme system (window.theme with 'dark' class)
      // This matches the behavior of theme-toggle.tsx and theme-provider
      ;(function () {
        // Migrate legacy theme key for existing users
        if (typeof localStorage !== 'undefined') {
          const legacyTheme = localStorage.getItem('eng-blog-theme')
          if (legacyTheme && !localStorage.getItem('theme')) {
            localStorage.setItem('theme', legacyTheme)
            localStorage.removeItem('eng-blog-theme')
          }
        }

        const getThemePreference = () => {
          if (typeof localStorage !== 'undefined') {
            return localStorage.getItem('theme') || 'system'
          }
          return 'system'
        }

        const applyTheme = (theme) => {
          const isDark =
            theme === 'dark' ||
            (theme === 'system' &&
              window.matchMedia('(prefers-color-scheme: dark)').matches)

          document.documentElement.classList.toggle('dark', isDark)

          // Store the theme globally for compatibility with theme-toggle.tsx
          if (typeof window !== 'undefined') {
            window.theme = theme
          }
        }

        const theme = getThemePreference()
        applyTheme(theme)

        // Listen for theme changes from other parts of the app
        window.addEventListener('storage', (e) => {
          if (e.key === 'theme' && e.newValue) {
            applyTheme(e.newValue)
          }
        })

        // Listen for system theme changes
        window
          .matchMedia('(prefers-color-scheme: dark)')
          .addEventListener('change', () => {
            const currentTheme = getThemePreference()
            if (currentTheme === 'system') {
              applyTheme('system')
            }
          })
      })()
    </script> <!-- View Transition: Disable logo animation when header is scrolled out of view --> <script type="module">const n=new Map;function i(){const t=document.querySelector("header");if(!t||!t.querySelector("[data-astro-transition-scope]"))return!0;const o=t.getBoundingClientRect();return o.top<window.innerHeight&&o.bottom>0}function r(){document.querySelectorAll("[data-astro-transition-scope]").forEach(e=>{const o=e.getAttribute("data-astro-transition-scope");n.has(e)||n.set(e,o),e.removeAttribute("data-astro-transition-scope")})}function a(){n.forEach((t,e)=>{t&&e.setAttribute("data-astro-transition-scope",t)}),n.clear()}document.addEventListener("astro:before-preparation",()=>{if(!(window.location.pathname==="/"||window.location.pathname==="/engineering-blog/"))return;i()||r()});document.addEventListener("astro:page-load",()=>{a()});
//# sourceMappingURL=engineering-blog-layout.astro_astro_type_script_index_0_lang.DZNLT9nZ.js.map</script> </body> </html>