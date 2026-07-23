---
source_url: https://runtimewire.com/article/jack-dorsey-block-buzz-team-chat-ai-agents-git
ingested: 2026-07-21
sha256: 2322a145b91643b90ab6d5e9ac7c4273f5f72a8cad28ed59420c53e5d1123419
blog_source: Hacker News AI
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="color-scheme" content="dark" />
    <meta name="theme-color" content="#0a0a0f" />
    <meta name="format-detection" content="telephone=no" />

    <!-- Pre-paint the persisted color theme onto <html> so there's no flash
         of the wrong palette before React hydrates. Mirrors the useTheme hook
         (storage key "rw-theme"; classes rw-theme-dark|light|ascii). -->
    <script>
      (function () {
        try {
          var t = null;
          try { t = localStorage.getItem("rw-theme"); } catch (e) {}
          if (t !== "dark" && t !== "light" && t !== "ascii") {
            var m2 = document.cookie.match(/(?:^|;\s*)rw-theme=([^;]+)/);
            t = m2 ? decodeURIComponent(m2[1]) : null;
          }
          if (t !== "dark" && t !== "light" && t !== "ascii") {
            var prefersDark = true;
            try {
              if (window.matchMedia) {
                prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
              }
            } catch (e2) {}
            t = prefersDark ? "dark" : "light";
          }
          document.documentElement.classList.add("rw-theme-" + t);
          var c = { dark: "#0a0a0f", light: "#f5f7fa", ascii: "#050705" }[t];
          var m = document.querySelector('meta[name="theme-color"]');
          if (m && c) m.setAttribute("content", c);
        } catch (e) {}
      })();
    </script>

    
    
    <meta name="keywords" content="ai startups, ai funding, ai news, startup news, founders, venture capital, ai infrastructure, model launches, ai economy, runtimewire" />
    <meta name="author" content="RuntimeWire" />
    <meta name="publisher" content="RuntimeWire" />
    <meta name="application-name" content="RuntimeWire" />
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
    <meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large" />
    <meta name="referrer" content="strict-origin-when-cross-origin" />
    

    
    <link rel="alternate" type="application/rss+xml" title="RuntimeWire" href="https://runtimewire.com/rss" />

    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png?v=3" />
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png?v=3" />
    <link rel="icon" type="image/png" sizes="192x192" href="/rw-icon-192.png?v=3" />
    <link rel="icon" type="image/png" sizes="512x512" href="/rw-icon.png?v=3" />
    <link rel="apple-touch-icon" sizes="180x180" href="/rw-icon-192.png?v=3" />
    <link rel="shortcut icon" href="/favicon-32.png?v=3" />

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "Organization",
          "@id": "https://runtimewire.com/#organization",
          "name": "RuntimeWire",
          "alternateName": "RW",
          "url": "https://runtimewire.com/",
          "logo": {
            "@type": "ImageObject",
            "url": "https://runtimewire.com/runtimewire-wordmark.png",
            "contentUrl": "https://runtimewire.com/runtimewire-wordmark.png",
            "width": 576,
            "height": 106
          },
          "image": "https://runtimewire.com/og-card.png",
          "description": "Real-time startup intelligence for the AI economy. Funding rounds, model launches, infra shifts, and founder moves.",
          "sameAs": [
            "https://x.com/runtimewire",
            "https://www.youtube.com/@runtimewire",
            "https://podcasts.apple.com/us/podcast/id1896845816",
            "https://open.spotify.com/show/033ponGGZ51S8UMgMzhcgH"
          ]
        },
        {
          "@type": "WebSite",
          "@id": "https://runtimewire.com/#website",
          "url": "https://runtimewire.com/",
          "name": "RuntimeWire",
          "description": "Real-time startup intelligence for the AI economy.",
          "publisher": { "@id": "https://runtimewire.com/#organization" },
          "inLanguage": "en-US"
        }
      ]
    }
    </script>

    <!-- X conversion tracking is a non-essential tracker and is NOT loaded
         here. It is injected on demand by src/lib/twitterPixel.ts only after
         the reader grants analytics consent (see the cookie consent banner). -->

    <script type="module" crossorigin src="/assets/index-BD_u5w9n.js"></script>
    <link rel="stylesheet" crossorigin href="/assets/index-DUVqNEO3.css">
      <title>Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting - RuntimeWire</title>
    <meta name="description" content="Block&#39;s Buzz combines team chat, AI agents, workflows and Git hosting in a self-hostable workspace built on signed Nostr events." />
    <meta property="og:type" content="article" />
    <meta property="og:site_name" content="RuntimeWire" />
    <meta property="og:title" content="Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting" />
    <meta property="og:description" content="Block&#39;s Buzz combines team chat, AI agents, workflows and Git hosting in a self-hostable workspace built on signed Nostr events." />
    <meta property="og:url" content="https://runtimewire.com/article/jack-dorsey-block-buzz-team-chat-ai-agents-git" />
    <meta property="og:locale" content="en_US" />
    <meta property="og:image" content="https://runtimewire.com/og/jack-dorsey-block-buzz-team-chat-ai-agents-git.jpg" />
    <meta property="og:image:secure_url" content="https://runtimewire.com/og/jack-dorsey-block-buzz-team-chat-ai-agents-git.jpg" />
    <meta property="og:image:type" content="image/jpeg" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:image:alt" content="Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting — Block&#39;s self-hostable workspace uses signed Nostr events, while its current relay architecture remains centralized within each deployment." />
    <meta property="article:published_time" content="2026-07-21T17:13:16.588Z" />
    <meta property="article:modified_time" content="2026-07-21T17:13:16.588Z" />
    <meta property="article:section" content="ai" />
    <meta property="article:author" content="Ryan Merket" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:site" content="@runtimewire" />
    <meta name="twitter:creator" content="@runtimewire" />
    <meta name="twitter:domain" content="runtimewire.com" />
    <meta name="twitter:title" content="Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting" />
    <meta name="twitter:description" content="Block&#39;s Buzz combines team chat, AI agents, workflows and Git hosting in a self-hostable workspace built on signed Nostr events." />
    <meta name="twitter:image" content="https://runtimewire.com/og/jack-dorsey-block-buzz-team-chat-ai-agents-git.jpg" />
    <meta name="twitter:image:alt" content="Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting — Block&#39;s self-hostable workspace uses signed Nostr events, while its current relay architecture remains centralized within each deployment." />
    <meta property="article:tag" content="block" />
    <meta property="article:tag" content="buzz" />
    <meta property="article:tag" content="ai agents" />
    <meta property="article:tag" content="developer tools" />
    <meta property="article:tag" content="open source" />
    <link rel="canonical" href="https://runtimewire.com/article/jack-dorsey-block-buzz-team-chat-ai-agents-git" />
    <script type="application/ld+json">{"@context":"https://schema.org","@type":"NewsArticle","mainEntityOfPage":{"@type":"WebPage","@id":"https://runtimewire.com/article/jack-dorsey-block-buzz-team-chat-ai-agents-git"},"headline":"Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting","description":"Block's Buzz combines team chat, AI agents, workflows and Git hosting in a self-hostable workspace built on signed Nostr events.","image":[{"@type":"ImageObject","url":"https://runtimewire.com/og/jack-dorsey-block-buzz-team-chat-ai-agents-git.jpg","width":1200,"height":630,"encodingFormat":"image/jpeg","caption":"Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting — Block's self-hostable workspace uses signed Nostr events, while its current relay architecture remains centralized within each deployment."}],"datePublished":"2026-07-21T17:13:16.588Z","dateModified":"2026-07-21T17:13:16.588Z","author":[{"@type":"Person","name":"Ryan Merket","url":"https://runtimewire.com/author/ryan-merket","jobTitle":"Editor in Chief","sameAs":["https://x.com/ryanmerket","https://www.linkedin.com/in/ryanmerket/","https://www.facebook.com/merket","https://ryanmerket.com","https://www.threads.com/@merket","https://www.instagram.com/merket","https://www.crunchbase.com/person/ryan-merket"]}],"publisher":{"@id":"https://runtimewire.com/#organization"},"isPartOf":{"@id":"https://runtimewire.com/#website"},"articleSection":"ai","keywords":"block, buzz, ai agents, developer tools, open source","articleBody":"Jack Dorsey (@jack) said in an announcement on X on July 21st that Block is launching Buzz, an open source workspace designed to put employees, AI agents, conversations and software repositories behind one identity system. Dorsey, Block's cofounder and Block Head, is pitching Buzz as a way to reduce Block's dependence on Slack and GitHub. The move takes his preference for open protocols into the daily machinery of software development, where teams typically spread discussions, source code, au...","inLanguage":"en-US"}</script>
    <script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://runtimewire.com/"},{"@type":"ListItem","position":2,"name":"AI","item":"https://runtimewire.com/category/ai"},{"@type":"ListItem","position":3,"name":"Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting","item":"https://runtimewire.com/article/jack-dorsey-block-buzz-team-chat-ai-agents-git"}]}</script>
  </head>
  <body>
    <noscript>
      <style>
        body { background: #06080c; color: #e5e9f0; margin: 0; }
        .rw-nojs-bar { max-width: 880px; margin: 0 auto; padding: 18px 16px 14px; }
        .rw-nojs-bar .rw-nojs-brand { font: 700 20px/1 Inter, system-ui, sans-serif; color: #e5e9f0; text-decoration: none; }
        .rw-nojs-nav { max-width: 880px; margin: 0 auto; padding: 0 16px 14px; border-bottom: 1px solid #1c2230; font: 500 14px/1.4 Inter, system-ui, sans-serif; }
        .rw-nojs-nav a { color: #6f9bff; margin: 0 14px 6px 0; text-decoration: none; display: inline-block; }
        .rw-nojs-nav a:hover { text-decoration: underline; }
        .rw-nojs-note { max-width: 880px; margin: 12px auto 0; padding: 0 16px; font: 400 13px/1.5 Inter, system-ui, sans-serif; color: #8a93a6; }
        #root [data-rw-crawler] { max-width: 880px; margin: 0 auto; padding: 8px 16px 48px; font: 400 16px/1.65 Inter, system-ui, sans-serif; color: #e5e9f0; }
        #root [data-rw-crawler] a { color: #6f9bff; }
        #root [data-rw-crawler] h1 { font-size: 28px; line-height: 1.2; }
        #root [data-rw-crawler] h2 { font-size: 20px; margin-top: 28px; }
        #root [data-rw-crawler] img { max-width: 100%; height: auto; }
        #root [data-rw-crawler] ul { padding-left: 0; list-style: none; }
        #root [data-rw-crawler] li { margin: 0 0 18px; }
        #root [data-rw-crawler] .rw-pagination { margin: 28px 0 0; display: flex; flex-wrap: wrap; gap: 12px; align-items: baseline; }
        #root [data-rw-crawler] .rw-pagination strong { color: #e5e9f0; }
        .rw-nojs-footer { max-width: 880px; margin: 40px auto 0; padding: 22px 16px 44px; border-top: 1px solid #1c2230; font: 400 13px/1.6 Inter, system-ui, sans-serif; color: #8a93a6; }
        .rw-nojs-footer .rw-nojs-fcols { display: flex; flex-wrap: wrap; gap: 28px 40px; margin-bottom: 20px; }
        .rw-nojs-footer h2 { font-size: 11px; letter-spacing: 0.05em; text-transform: uppercase; color: #b7c0d3; margin: 0 0 8px; }
        .rw-nojs-footer a { color: #6f9bff; text-decoration: none; display: block; margin: 0 0 5px; }
        .rw-nojs-footer a:hover { text-decoration: underline; }
        .rw-nojs-footer .rw-nojs-legal { font: 400 12px/1.6 Inter, system-ui, sans-serif; color: #6b7384; margin: 0; }
        .rw-nojs-footer .rw-nojs-legal a { display: inline; }
      </style>
      <div class="rw-nojs-bar"><a class="rw-nojs-brand" href="/">RuntimeWire</a></div>
      <nav class="rw-nojs-nav" aria-label="Primary">
        <a href="/category/ai">AI</a>
        <a href="/category/startups">Startups</a>
        <a href="/category/venture">Venture</a>
        <a href="/category/products">Products</a>
        <a href="/category/funding">Funding</a>
        <a href="/category/exits">Exits</a>
        <a href="/models">Models</a>
        <a href="/head-to-head">Head-to-Head</a>
        <a href="/about">About</a>
      </nav>
      <p class="rw-nojs-note">
        You're browsing RuntimeWire with JavaScript disabled. Articles and
        navigation work fully. Interactive features &mdash; search, comments,
        and newsletter signup &mdash; require JavaScript.
      </p>
    </noscript>
    <div id="root"><noscript><main id="rw-crawler-main" data-rw-crawler="1">
  <nav aria-label="Section" data-rw-block="section-nav">
    <a href="/category/ai">ai</a>
  </nav>
  <article>
    <header>
      <h1>Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting</h1>
      <p data-rw-block="dek"><strong>Block&#39;s self-hostable workspace uses signed Nostr events, while its current relay architecture remains centralized within each deployment.</strong></p>
      <p data-rw-block="byline">
        By <a href="/author/ryan-merket" itemprop="author">Ryan Merket</a>
        · Published <time datetime="2026-07-21T17:13:16.588Z">Jul 21, 2026, 12:13pm CT</time>
        
      </p>
    </header>
    
    <section aria-label="Why it matters" data-rw-block="why-it-matters">
        <h2>Why it matters</h2>
        <p>Buzz turns Dorsey&#39;s agent-centered operating thesis into an open-source product. Its key bet is that shared identity and signed events can make agents accountable participants in software work.</p>
      </section>
    <figure><img src="https://runtimewire.com/api/storage/uploads/source-images/jack-dorsey-block-buzz-team-chat-ai-agents-git-f562a21f.jpg" alt="Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting — Block&#39;s self-hostable workspace uses signed Nostr events, while its current relay architecture remains centralized within each deployment." /></figure>
    <section data-rw-block="body"><p><a rel="noopener noreferrer" target="_blank" href="https://x.com/jack">Jack Dorsey (@jack)</a> said in an <a rel="noopener noreferrer" target="_blank" href="https://x.com/jack/status/2079605800998146171">announcement on X</a> on July 21st that Block is launching <a rel="noopener noreferrer" target="_blank" href="https://buzz.xyz">Buzz</a>, an open-source workspace designed to put employees, AI agents, conversations and software repositories behind one identity system.</p>
<p>Dorsey, <a rel="noopener noreferrer" target="_blank" href="https://investors.block.xyz/governance/leadership/default.aspx">Block&#39;s cofounder and Block Head</a>, is pitching Buzz as a way to reduce Block&#39;s dependence on Slack and GitHub. The move takes his preference for open protocols into the daily machinery of software development, where teams typically spread discussions, source code, automated workflows and agent activity across several vendors.</p>
<p>Buzz also fits the operating model Dorsey has been building inside Block. In an essay with Sequoia Capital&#39;s Roelof Botha, Dorsey argued that AI should change how organizations coordinate rather than serve only as a productivity add-on. Buzz supplies an infrastructure layer for that thesis: Block&#39;s <a rel="noopener noreferrer" target="_blank" href="https://github.com/block/buzz">public repository</a> documents a separate internal build configured for Block&#39;s relay and agent provider.</p>
<h3>One workspace for humans and agents</h3>
<p>Buzz is built around a self-hostable Nostr relay. Every message, reaction, workflow step, code event and approval is stored as a cryptographically signed event. Human employees and agents receive the same basic identity structure, including their own key pairs, channel memberships and audit trails.</p>
<p>That design lets agents participate as members rather than conventional chat bots. According to Block&#39;s documentation, agents can search prior discussions, open repositories, submit patches, review code, run workflows, edit shared canvases and create channels. Buzz includes an agent-oriented command-line interface and harnesses for Goose, Codex and Claude Code, keeping the underlying model choice separate from the workspace.</p>
<p>Buzz&#39;s Git ambitions go well beyond posting repository notifications into chat. The <a rel="noopener noreferrer" target="_blank" href="https://github.com/block/buzz/blob/main/VISION_PROJECTS.md">project specification</a> describes a built-in software forge using standard Git Smart HTTP. A feature branch can become its own channel, with patches, continuous-integration results, review comments and the merge decision preserved in the same record. Repositories, discussions and workflow history then share one search index.</p>
<p>The currently working feature set includes channels, threads, direct messages, shared canvases, media, search, an audit log, a desktop application and YAML-based workflows. Packaged builds are available for macOS, Windows and Linux. The repository is licensed under Apache 2.0.</p>
<h3>Decentralized control, centralized relays</h3>
<p>Dorsey described Buzz as decentralized and self-sovereign, but Block&#39;s <a rel="noopener noreferrer" target="_blank" href="https://github.com/block/buzz/blob/main/ARCHITECTURE.md">architecture document</a> draws a more specific boundary. Buzz currently has no peer-to-peer event exchange, gossip layer or replication between relays. All reads and writes in a workspace pass through a single relay, which authenticates users, verifies signatures, stores events and distributes updates.</p>
<p>Buzz&#39;s decentralization therefore comes from deployment and ownership. An organization can run its own relay, retain its domain and data, and use portable Nostr key pairs instead of depending on a single hosted service. A hosted operator can also run multiple isolated communities on shared infrastructure. Within each community, however, the relay remains the authoritative server.</p>
<p>That distinction matters for teams evaluating Buzz as a Slack or GitHub substitute. Self-hosting gives an operator control over infrastructure and data location, but it also transfers responsibility for availability, backups, security and upgrades. The signed event model provides attribution and an audit trail; it does not remove the operational risks attached to the server hosting the workspace.</p>
<h3>An early product with a wide scope</h3>
<p>Buzz is available for testing and development, though Block&#39;s own documentation repeatedly labels it unfinished. Mobile clients remain in development, push notifications are pending, and workflow approval gates have database, API and interface components without a completed execution path. The latest desktop release, <a rel="noopener noreferrer" target="_blank" href="https://github.com/block/buzz/releases/tag/v0.4.21">version 0.4.21</a>, shipped on July 21st with fixes and additions covering agent controls, authentication and workspace onboarding.</p>
<p>Block has given Buzz a broad assignment: replace portions of chat, code hosting, workflow automation, project search and agent orchestration with one event system. Combining those surfaces may reduce the integration work required to give agents useful context and tightly scoped access. It also puts Buzz against mature products whose separate roles let customers replace one tool without migrating the rest of their development stack.</p>
<p>Dorsey&#39;s launch makes Block the first customer reference embedded in Buzz&#39;s documentation, but Block has not published adoption, pricing or external customer figures. For now, Buzz is an open-source build and an invitation to contribute. Its first test will be whether engineers outside Block want one relay to carry this much of their work.</p>
</section>
  </article>
  <aside aria-label="Sources" data-rw-block="sources">
        <h2>Sources</h2>
        <ul>
          <li><a href="https://x.com/jack/status/2079605800998146171" rel="noopener noreferrer" target="_blank">Jack Dorsey announces Buzz</a> <small>X</small></li>
          <li><a href="https://buzz.xyz" rel="noopener noreferrer" target="_blank">Buzz</a> <small>Buzz</small></li>
          <li><a href="https://github.com/block/buzz" rel="noopener noreferrer" target="_blank">block/buzz: A hive mind communication platform</a> <small>GitHub</small></li>
          <li><a href="https://github.com/block/buzz/blob/main/ARCHITECTURE.md" rel="noopener noreferrer" target="_blank">Buzz Architecture</a> <small>GitHub</small></li>
          <li><a href="https://github.com/block/buzz/blob/main/VISION_PROJECTS.md" rel="noopener noreferrer" target="_blank">Buzz Projects - A Nostr-Native Forge</a> <small>GitHub</small></li>
          <li><a href="https://github.com/block/buzz/releases/tag/v0.4.21" rel="noopener noreferrer" target="_blank">Buzz Desktop v0.4.21</a> <small>GitHub</small></li>
          <li><a href="https://investors.block.xyz/governance/leadership/default.aspx" rel="noopener noreferrer" target="_blank">Block leadership</a> <small>Block</small></li>
          <li><a href="https://block.xyz/inside/from-hierarchy-to-intelligence" rel="noopener noreferrer" target="_blank">From Hierarchy to Intelligence</a> <small>Block</small></li>
        </ul>
      </aside>
  <section aria-label="Comments" data-rw-block="comments">
    <h2>Reader comments</h2>
    <p>Conversation for this story loads after sign-in.</p>
  </section>
</main>
<nav aria-label="More from AI" data-rw-block="related">
  <h2>More from AI</h2>
  <ul>
      <li><a href="/article/gizmo-generates-editable-3d-environments-for-robot-training-from-text-and-images">Gizmo generates editable 3D environments for robot training from text and images</a></li>
      <li><a href="/article/twelvelabs-launches-jockey-research-preview">TwelveLabs opens research preview of Jockey, an AI agent that searches entire video libraries via Claude</a></li>
      <li><a href="/article/head-to-head-animatediff-turbo-vs-marey-realism-v1-5-2">Head to head: AnimateDiff Turbo vs Marey Realism V1.5</a></li>
      <li><a href="/article/turingcom-simulated-company-platform-cirrus-sleep-pilot">Turing.com launches platform that builds a complete synthetic company, demoed with Cirrus Sleep</a></li>
      <li><a href="/article/nick-khami-launches-scribe-multiplayer-markdown-editor-ai-agents">Nick Khami launches Scribe for multiplayer Markdown editing with AI agents</a></li>
      <li><a href="/article/digits-cla-firm-specific-accounting-ai">Digits and CLA will train firm-specific accounting AI for thousands of clients</a></li>
  </ul>
  <p><a href="/category/ai">See all AI</a></p>
</nav></noscript></div>
    <noscript>
      <footer class="rw-nojs-footer">
        <div class="rw-nojs-fcols">
          <div>
            <h2>Sections</h2>
            <a href="/category/ai">AI</a>
            <a href="/category/startups">Startups</a>
            <a href="/category/venture">Venture</a>
            <a href="/category/products">Products</a>
            <a href="/category/funding">Funding</a>
            <a href="/category/exits">Exits</a>
          </div>
          <div>
            <h2>Publication</h2>
            <a href="/about">About</a>
            <a href="/faq">FAQ</a>
            <a href="/contact">Contact</a>
            <a href="/editorial-policy">Editorial Policy</a>
            <a href="/corrections-policy">Corrections Policy</a>
            <a href="/ethics">Ethics</a>
          </div>
          <div>
            <h2>Tools</h2>
            <a href="/models">AI Model Pricing</a>
            <a href="/head-to-head">Head-to-Head</a>
            <a href="/tools/synthid-watermark-remover">SynthID Remover</a>
          </div>
          <div>
            <h2>Legal</h2>
            <a href="/privacy">Privacy</a>
            <a href="/terms">Terms</a>
          </div>
        </div>
        <p class="rw-nojs-legal">
          &copy; 2026 RuntimeWire, Inc. All rights reserved. &middot;
          <a href="https://gradientnoise.com" rel="noopener noreferrer">Gradient Noise, Inc.</a><br />
          An independent startup and technology publication based in Austin, Texas
          and San Francisco, California. Send tips to
          <a href="mailto:tips@runtimewire.com">tips@runtimewire.com</a>.
        </p>
      </footer>
    </noscript>
  </body>
</html>
