---
source_url: https://blog.exe.dev/claude-is-not-a-compiler
ingested: 2026-07-21
sha256: ea66c342db699fa454210f615d2f375c23d5b8ae0351df0c3f0623d15fb27dfd
blog_source: Hacker News
---
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="icon" href="/favicon.ico">
    <title>Claude Is Not a Compiler - exe.dev blog</title>
    <meta name="description" content="">
    <link rel="canonical" href="https://blog.exe.dev/claude-is-not-a-compiler">
    <meta property="og:title" content="Claude Is Not a Compiler - exe.dev blog">
    <meta property="og:description" content="">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://blog.exe.dev/claude-is-not-a-compiler">
    <meta property="og:site_name" content="exe.dev">
    <meta property="og:image" content="https://blog.exe.dev/static/og-card.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="exe.dev blog">
    <meta property="article:published_time" content="2026-07-20">
    <meta property="article:author" content="Josh Bleecher Snyder">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Claude Is Not a Compiler - exe.dev blog">
    <meta name="twitter:description" content="">
    <meta name="twitter:image" content="https://blog.exe.dev/static/og-card.png">
    <link rel="stylesheet" href="/static/exe.css" />
    <link rel="alternate" type="application/atom+xml" title="exe.dev blog" href="https://blog.exe.dev/atom.xml" />
    <link rel="alternate" type="application/rss+xml" title="exe.dev blog" href="https://blog.exe.dev/rss.xml" />
    <script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Josh Bleecher Snyder"},"dateModified":"2026-07-20T00:00:00Z","datePublished":"2026-07-20T00:00:00Z","description":"","headline":"Claude Is Not a Compiler","image":"https://blog.exe.dev/static/og-card.png","mainEntityOfPage":"https://blog.exe.dev/claude-is-not-a-compiler","publisher":{"@type":"Organization","logo":{"@type":"ImageObject","url":"https://blog.exe.dev/apple-touch-icon.png"},"name":"exe.dev"},"url":"https://blog.exe.dev/claude-is-not-a-compiler"}</script>
    
<link rel="stylesheet" href="/static/topbar.css" />

    <style>
      body {
        font-family:
          "Charter", "Charter Roman", "ITC Charter", "STIX Two Text", "Hoefler Text",
          "Iowan Old Style", "Palatino", "Palatino Linotype", "URW Palladio L",
          Georgia, "Times New Roman", serif;
        font-size: 16px;
        font-size-adjust: 0.48;
        -webkit-text-size-adjust: 100%;
        text-size-adjust: 100%;
        background: #fff;
        color: #1f1f1f;
        margin: 0;
      }

      main {
        max-width: 720px;
        margin: 64px auto 120px;
        padding: 0 24px;
      }

      .post-header {
        margin-bottom: 48px;
      }

      .post-title {
        font-size: 40px;
        font-weight: 400;
        letter-spacing: -0.01em;
        margin-bottom: 12px;
      }

      .post-meta {
        font-size: 13px;
        color: rgba(0, 0, 0, 0.6);
        display: flex;
        flex-wrap: wrap;
        gap: 16px;
      }

      .post-meta span {
        display: flex;
        align-items: center;
        gap: 6px;
      }

      .unpublished-note {
        font-size: 11px;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: rgba(0, 0, 0, 0.55);
        margin-left: 8px;
      }

      .post-content {
        font-size: 17px;
        line-height: 1.75;
        color: #2c2c2c;
      }

      .post-content h1,
      .post-content h2,
      .post-content h3,
      .post-content h4 {
        margin: 48px 0 16px 0;
        font-weight: 600;
        line-height: 1.3;
        color: #111;
      }

       
      .post-content h1 { font-size: 32px; }
      .post-content h2 { font-size: 26px; }
      .post-content h3 { font-size: 22px; }
      .post-content h4 { font-size: 18px; }

      .post-content p {
        margin-bottom: 22px;
      }

      .post-content ul,
      .post-content ol {
        padding-left: 28px;
        margin-bottom: 22px;
      }

      .post-content a {
        color: #0054d1;
        text-decoration: underline;
      }

      .post-content blockquote {
        margin: 32px 0;
        padding: 20px 24px;
        border-left: 4px solid rgba(0, 0, 0, 0.08);
        background: #f6f6f0;
        border-radius: 14px;
        font-style: italic;
        font-size: 18px;
        white-space: normal;
        overflow-x: visible;
      }

      .post-content blockquote p {
        margin: 0 0 16px;
      }

      .post-content blockquote p:last-child {
        margin-bottom: 0;
      }

       
      .post-content pre.code {
        background: #f6f6f0;
        padding: 20px;
        border-radius: 8px;
        overflow-x: auto;
        font-size: 15px;
        line-height: 1.6;
      }

       
      .post-content pre.indented {
        background: transparent;
        padding: 12px 0;
        border-radius: 0;
        overflow-x: visible;
        white-space: pre-wrap;
        word-break: break-word;
        font-size: 17px;
        line-height: 1.75;
      }
      .post-content pre.indented code { font-family: inherit; }

       
      .post-content img {
        max-width: 100%;
        height: auto;
      }
      .post-content p > img,
      .post-content > img {
        display: block;
        margin-left: auto;
        margin-right: auto;
      }

       
      .post-content .img-row {
        display: flex;
        gap: 14px;
        align-items: flex-start;
        justify-content: center;
        margin: 28px 0;
      }
      .post-content .img-row img {
        flex: 1 1 0;
        min-width: 0;
        width: 100%;
        height: auto;
      }
      @media (max-width: 560px) {
        .post-content .img-row { flex-direction: column; align-items: center; }
      }

       
      .post-content .asciinema-embed {
        margin: 28px 0 8px;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
        max-width: 100%;
      }

      .post-content p.asciinema-caption {
        margin: 0 0 28px;
        font-size: 14px;
        color: rgba(0, 0, 0, 0.6);
        text-align: center;
      }

      .post-content kbd {
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
        font-size: 12px;
        padding: 2px 6px;
        border: 1px solid rgba(0, 0, 0, 0.18);
        border-bottom-width: 2px;
        border-radius: 4px;
        background: #fafaf3;
        color: #111;
        white-space: nowrap;
      }

       
      .post-content table.sharing-matrix {
        width: 100%;
        margin: 28px 0;
        border-collapse: separate;
        border-spacing: 0;
        font-size: 15px;
        line-height: 1.5;
        background: #fff;
        border: 1px solid rgba(0, 0, 0, 0.1);
        border-radius: 10px;
        overflow: hidden;
      }
      .post-content table.sharing-matrix th,
      .post-content table.sharing-matrix td {
        padding: 12px 16px;
        text-align: left;
        vertical-align: top;
        border-bottom: 1px solid rgba(0, 0, 0, 0.08);
        border-right: 1px solid rgba(0, 0, 0, 0.06);
      }
      .post-content table.sharing-matrix th:last-child,
      .post-content table.sharing-matrix td:last-child {
        border-right: none;
      }
      .post-content table.sharing-matrix tbody tr:last-child th,
      .post-content table.sharing-matrix tbody tr:last-child td {
        border-bottom: none;
      }
      .post-content table.sharing-matrix thead th {
        background: #f6f6f0;
        font-weight: 600;
        color: #111;
      }
      .post-content table.sharing-matrix tbody th[scope="row"] {
        background: #fafaf3;
        font-weight: 600;
        color: #111;
        width: 28%;
      }
      .post-content table.sharing-matrix .hint {
        display: inline-block;
        margin-top: 2px;
        font-weight: 400;
        font-size: 13px;
        color: rgba(0, 0, 0, 0.55);
      }

      .post-footer {
        margin-top: 64px;
        padding-top: 32px;
        border-top: 1px solid rgba(0, 0, 0, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 16px;
      }

      .post-footer a {
        color: #0054d1;
        text-decoration: none;
      }

      .post-feeds {
        display: flex;
        align-items: center;
        gap: 0;
        font-size: 12px;
        letter-spacing: 0.15em;
        text-transform: uppercase;
      }
      .post-feeds a { color: rgba(0, 0, 0, 0.5); }
      .post-feeds a:hover { color: #101010; }
      .post-feeds .sep { color: rgba(0, 0, 0, 0.35); padding: 0 8px; }

      @media (max-width: 768px) {
        main {
          margin: 32px auto 80px;
          padding: 0 16px;
        }

        .post-title {
          font-size: 32px;
        }

        .post-content h1 { font-size: 28px; }
        .post-content h2 { font-size: 24px; }
        .post-content h3 { font-size: 20px; }
        .post-content h4 { font-size: 18px; }

        .post-meta {
          flex-direction: column;
          gap: 8px;
        }
      }

       
      @media (prefers-color-scheme: dark) {
        body {
          background: #111;
          color: #e5e5e5;
        }

        .post-title {
          color: #f3f4f6;
        }

        .post-meta {
          color: rgba(255, 255, 255, 0.6);
        }

        .unpublished-note {
          color: rgba(255, 255, 255, 0.55);
        }

        .post-content {
          color: #d1d5db;
        }

        .post-content h1,
        .post-content h2,
        .post-content h3,
        .post-content h4 {
          color: #f3f4f6;
        }

        .post-content a {
          color: #60a5fa;
        }

        .post-content blockquote {
          border-left-color: rgba(255, 255, 255, 0.15);
          background: #1a1a1a;
        }

        .post-content pre.code {
          background: #1a1a1a;
        }

        .post-content img[src$=".svg"] {
          filter: invert(1) hue-rotate(180deg);
        }

        .post-footer {
          border-top-color: rgba(255, 255, 255, 0.1);
        }

        .post-footer a {
          color: #60a5fa;
        }

        .post-feeds a { color: rgba(255, 255, 255, 0.55); }
        .post-feeds a:hover { color: #f3f4f6; }
        .post-feeds .sep { color: rgba(255, 255, 255, 0.35); }
      }
    </style>
  </head>
  <body>
    
<header>
  <div class="nav-container">
    <div class="nav-left">
      <a href="https://exe.dev" class="nav-logo-img"><img src="/static/exy.webp" alt="exe.dev logo" /></a>
      <a href="https://exe.dev" class="nav-logo-text">exe.dev</a>
      <a href="https://exe.dev/docs" class="nav-link">docs</a>
      <a href="/" class="nav-link active">blog</a>
      <a href="https://exe.dev/pricing" class="nav-link">pricing</a>
      <div class="nav-dropdown">
        <button type="button" class="nav-link nav-dropdown-trigger" aria-haspopup="true" aria-expanded="false">uses<svg class="nav-dropdown-caret" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M5.22 8.22a.75.75 0 0 1 1.06 0L10 11.94l3.72-3.72a.75.75 0 1 1 1.06 1.06l-4.25 4.25a.75.75 0 0 1-1.06 0L5.22 9.28a.75.75 0 0 1 0-1.06Z" clip-rule="evenodd"/></svg></button>
        <div class="nav-dropdown-menu" role="menu">
          <a href="https://exe.dev/sandbox" class="nav-dropdown-item" role="menuitem"><span class="nav-dropdown-title">Sandbox</span><span class="nav-dropdown-desc">Disposable VMs for AI agents, by the second.</span></a>
          <a href="https://exe.dev/vps" class="nav-dropdown-item" role="menuitem"><span class="nav-dropdown-title">VPS</span><span class="nav-dropdown-desc">Persistent Linux VMs with HTTPS and SSH.</span></a>
          <a href="https://exe.dev/devbox" class="nav-dropdown-item" role="menuitem"><span class="nav-dropdown-title">Devbox</span><span class="nav-dropdown-desc">Cloud dev environment for you and your agents.</span></a>
        </div>
      </div>
    </div>
    <div class="nav-right">
      <a href="https://exe.dev/auth" class="btn btn-primary">Dashboard</a>
    </div>
  </div>
</header>

    
    <main>
      <header class="post-header">
        <h1 class="post-title">Claude Is Not a Compiler</h1>
        <div class="post-meta">
          <span>2026-07-20</span>
          <span>
            Josh Bleecher Snyder
            
          </span>
        </div>
      </header>
      <article class="post-content"><p>In early 2025, I wrote <a href="https://commaok.xyz/ai/is-claude-a-compiler/">Is Claude a Compiler</a>? At the time, my answer was: I don’t know.</p>
<p>I’m now pretty sure the answer is “no, that’s a category error, it’s <em>better</em> than a compiler.” But this requires a bit of unpacking.</p>
<p>Computer programs are notoriously intricate and finicky. A program operates at an extreme level of precision. There is no “wave hands” CPU instruction. High-level goals, meanwhile, are deeply underspecified.</p>
<p>In a highly stylized view of the world, software gets built in layers, each one adding specification and hiding “unnecessary” detail. Vision becomes strategy, product plans become coding plans, code becomes binaries. Each step is handled by a different role: executive, VP, PM, architect, engineer, compiler. </p>
<p>Critically, every step involves making lots of decisions. That’s what it <em>means</em> to increase the level of specification. (This is why one of my two key metrics for hiring engineers is judgment. The other is comity.)</p>
<p>The bottom layer, from source code to binary, is what a compiler does. Compilers make lots of decisions! Inlining, register allocation, whether to emit warnings or reject a program outright. And these decisions matter: They drive performance, system stability, predictability, and failure modes. A compiler engineer’s job is to arrange for the compiler to make consistently good decisions.</p>
<p>A good, trusted compiler frees a software engineer from having to make these decisions. Most engineers have little idea how compilers work; they don’t need to in order to be effective. </p>
<p>In 2025, we operated in a world where we used LLMs to generate smallish chunks of code. In this mental model, a coding agent might slot in as a new layer between a software engineer and a traditional compiler. It “compiles” natural language to code, making decisions so the engineer doesn’t have to. Its value is proportional to its reliability and the scale of the decisions it can make.</p>
<p>The thing is, this highly stylized view of the world is false. Abstractions leak and <a href="https://www.dbreunig.com/2026/07/03/ai-ecosytem-pace-layers.html">layers rub</a>. And even if they didn’t, we’d poke holes in them anyway.</p>
<p>Working across layers is extremely valuable; mechanical sympathy matters.</p>
<p>Part of how the <a href="https://www.construction-physics.com/p/building-fast-and-slow-the-empire">Empire State Building was constructed</a> in under a year and under budget (!!) was by systematically working across layers. For example, when deciding about the exterior chrome-nickel steel cladding:</p>
<blockquote>
<p>Neither architects, builders nor subcontractors felt competent to deal with this complicated technical problem of construction without full consultation. Accordingly, after full preliminary discussion, an all-inclusive meeting was called which was attended by representatives of the owner, the architects and builders, the subcontractors rolling the material, the metal workers who were to fabricate and those who were to erect it, and the inspectors who were to test all sheets at the several stages of preparation.</p>
</blockquote>
<p>This sounds really obvious when you say it out loud.</p>
<p>And yet we systematically fail at this in practice. I can only imagine the delight of the metal workers who had an opportunity to guide the design toward something that wasn’t slow and miserable to work on.</p>
<p>Part of the reason we fail is ignorance of what is even worth asking about. There’s a reason that <a href="https://daringfireball.net/linked/2022/10/11/ceos-as-nerds">the best executives have deep knowledge of their industry</a>. I also suspect that some of it is dismissiveness (“What could a line metalworker have to tell <em>me</em>?”). But a big chunk is also communication and organizational overhead. Layers exist for a reason—information hiding enables organizational scaling.</p>
<p>Claude is better than a compiler because it can work vertically across the stack. LLMs now talk strategy, product, architecture, code, and machine code. It can’t (yet?) do most individual tasks as well as an experienced, dedicated human, but it can do all of them, without having to schedule meetings or ask permission.</p>
<p>Here’s a concrete example.</p>
<p><a href="http://exe.dev">exe.dev</a> VMs have nice domain names: <a href="http://vm-name.exe.xyz">vm-name.exe.xyz</a>. When we start a new VM, we add a CNAME entry or three. Easy, right?</p>
<p>But our VMs start fast, so fast that even if we created the DNS entries before creating the VM, our users still had to sit around waiting for DNS to propagate, which occasionally took minutes, not seconds.</p>
<p>We did the obvious thing: We wrote our own DNS server, so that DNS always immediately matched the source of truth. And life was good.</p>
<p>But <a href="https://blog.exe.dev/regions">latency matters</a>, so we added regions. And just like that, DNS became the long pole again, because all DNS was served out of Oregon. Also, deployments caused tiny DNS outages. To fix this, all we needed now was a geographically distributed but fully consistent DNS server.</p>
<p>We did what a sensible engineer does when faced with a hard problem: cheat. We vibe-engineered a distributed DNS server tuned to our specific needs.</p>
<p>The goals were clear: Reduce latency for users far from Oregon and increase uptime resiliency. But the rest was not. We had to figure out everything from the exact behavior we wanted (particularly under various failure conditions), to how it fit into our overall company plans, to the architecture that could best achieve those goals, straight through down to the fine implementation details.</p>
<p>We hashed out the highest level strategic and architectural decisions in person. We’d make a fairly general-purpose DNS server and layer on our particular behavioral tweaks, use a hub-and-spoke model, use an append-only replication strategy, and have persistence at the edges.</p>
<p>All that was left was to actually build it.</p>
<p>I had LLMs research standard designs for distributed DNS systems, teach me about the guts and quirks of DNS, point out historic security failings, explore alternative implementation strategies (AXFR/IXFR? no thanks), research open source offerings, game out failure modes, and plan testing strategies.</p>
<p>Once I had an initial sketch of a design that seemed promising, I prompted multiple concurrent agent loops into building <em>the entire thing</em>, including tests and adversarial code review. They raised a bunch of questions—at every level of detail, from major structural approaches down to line-level code concerns. As I answered them (or reverted answers that generated regret), I slowly converted what I had learned into very terse written guidance, codifying decisions that proved to be important.</p>
<p>Then I asked new agents to compare the completed implementations and look for interesting deviations. It was shocking how many important decisions the agents never asked about but simply made—and made differently.</p>
<p>Here’s an example. Replication uses the fairly obvious approach: Catch up by asking for everything since the last known entry, and then long poll for new entries. There’s one ugly twist: database rollbacks. Rare, but they do happen, and they break the “append-only” contract.</p>
<p>The agents noticed this, and they solved it in wildly different ways. The design I ultimately settled on was to give every row a “timeline” field, as in “which timeline are you living in?” These are randomly generated, and every sync request for “entries since row N” includes the edge server’s timeline value for row N. If there’s a timeline mismatch, we know that history has been altered and fall back to a full clean re-sync.</p>
<p>There were also obvious style differences between the systems built by different agents. Claude and Codex both agreed that Claude created a more elegant system but that Codex was more thorough.</p>
<p>I worked through the list of major identified divergences, experimented, and then added more written guidance.</p>
<p>Then I repeated that <em>entire</em> <a href="https://commaok.xyz/ai/differential-spec/">differential spec analysis</a> process, twice. I know my <a href="https://en.wikipedia.org/wiki/Second-system_effect">aphorisms</a>.</p>
<blockquote>
<p>Plan to throw one away; you will, anyhow.</p>
<p>— Fred Brooks</p>
<p>If you plan to throw one away, you will throw away two.</p>
<p>— Craig Zerouni</p>
</blockquote>
<p>By the time I was ready to build a keeper, I had accumulated a scar-tissue document that was empirically sufficient to guide an agent through most of the important decisions, at every layer, ranging from high level goals through architecture down to the occasional low level detail, such as the exact shape of the data type for load-bearing concurrent caches.</p>
<p>The final system included unit tests, end-to-end tests, a shadow-mode for de-risking prod rollout, and a terse written-by-and-for-agents doc suite.</p>
<p>This cumulatively took about a week of my attention. I read a vanishingly small amount of the actual code.</p>
<p>At the end of that, I presented the solution to the team. I planned to launch the server and then go on vacation. As my colleagues peppered me with questions—&quot;How does X work? What happens in condition Y?&quot;—I found I could answer all of them confidently. (And I did go on that vacation. Number of DNS incidents a month later: 0.)</p>
<p>Claude wasn’t just a compiler here. I never handed off a task and let an agent make a bunch of decisions in order to reduce it to practice. That’s vibe-coding.</p>
<p>Rather, Claude was a vertically integrated resource, a multi-compiler. Its ability to work across the stack accelerated and augmented my ability to make a bunch of decisions at different levels, including about which decisions were important. (Most individual lines of code don’t make that cut.) That’s vibe-engineering.</p>
<p>I’d say that, in all the ways that matter, I understand the code. Sure, if I had to hand-edit it now, there’d be a serious learning curve. But I won't have to. And more importantly, I can reason about the system, share perspectives with my colleagues, and guide agents on future work. And there’s an enduring artifact that encapsulates the central, intentional aspects of the design that were important enough to record, across all layers, and should thus survive bug fixes and code churn.</p>
<p>One of the questions of this era is: What do software engineers need to understand about the systems they work on?</p>
<p>Well-chosen layers provide <em>understanding</em>. Fundamental laws of physics appear all-encompassing, but they’re inferior to classical mechanics for <em>explaining</em> why it’s better to be in a bus than a car in an accident.</p>
<p>Some software layers are dying, because they provide convenience, but not extra insight. (Sorry, Tailwind. I loved you.) But software layers that enable us to express important decisions in a comprehensible way? Those will stay.</p>
<p>We are shifting more of our attention up the stack, but without fully relinquishing the lower layers. Agents are not a free pass to hand off all understanding of the deeper layers of a system. Most of the Go standard library is written in Go, but a few key routines are written in assembly. You can’t rely on the compiler there.</p>
<p>Software engineers are being stretched. It’s exhilarating and exhausting. What’s becoming clear, though, is that in the near future, vibe-engineering is just…engineering.</p>
</article>
      <footer class="post-footer">
        <a href="/">&larr; All posts</a>
        <nav class="post-feeds">
          <a href="/rss.xml">RSS</a>
          <span class="sep">&middot;</span>
          <a href="/atom.xml">Atom</a>
        </nav>
      </footer>
    </main>
  </body>
</html>
