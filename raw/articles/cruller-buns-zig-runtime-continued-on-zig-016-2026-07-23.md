---
source_url: https://ziggit.dev/t/cruller-buns-zig-runtime-continued-on-zig-0-16/16734
ingested: 2026-07-23
sha256: bbf0b2fa8f86b837c14d0a8b1e6b38c6b600c126ee40dc818ab12f6f2f0b6523
blog_source: Hacker News
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Cruller: Bun&#39;s Zig Runtime, Continued on Zig 0.16 - Showcase - Ziggit</title>
    <meta name="description" content="Cruller: a production-focused Bun runtime ported to Zig 0.16
Cruller is a fork of the last Zig-based Bun release, reduced to the parts needed to run already-built production JavaScript servers and ported to vanilla Zig 0&amp;hellip;">
    <meta name="generator" content="Discourse 2026.2.0-latest - https://github.com/discourse/discourse version 780e1c6f0fc5e945d6d8db59e4a3bfdf4777b104">
<link rel="icon" type="image/png" href="https://ziggit.dev/uploads/default/optimized/1X/3417db0e8abaf83a355700b91efd528025492487_2_32x32.png">
<link rel="apple-touch-icon" type="image/png" href="https://ziggit.dev/uploads/default/optimized/1X/3417db0e8abaf83a355700b91efd528025492487_2_180x180.png">
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#ffffff">
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#111111">

<meta name="color-scheme" content="light dark">

<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, viewport-fit=cover">
<link rel="canonical" href="https://ziggit.dev/t/cruller-buns-zig-runtime-continued-on-zig-0-16/16734" />


<link rel="search" type="application/opensearchdescription+xml" href="https://ziggit.dev/opensearch.xml" title="Ziggit Search">

    
    <link href="/stylesheets/color_definitions_light_4_1_4ca60d8e38641be617e5427ded7c39447496d8a7.css?__ws=ziggit.dev" media="(prefers-color-scheme: light)" rel="stylesheet" class="light-scheme" data-scheme-id="4"/><link href="/stylesheets/color_definitions_dark_1_1_0c12d3073d043a8cbc3ac244cf2dc2ab758ae4d1.css?__ws=ziggit.dev" media="(prefers-color-scheme: dark)" rel="stylesheet" class="dark-scheme" data-scheme-id="1"/>

<link href="/stylesheets/common_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="common"  />

  <link href="/stylesheets/mobile_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="(max-width: 39.99999rem)" rel="stylesheet" data-target="mobile"  />
  <link href="/stylesheets/desktop_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="(min-width: 40rem)" rel="stylesheet" data-target="desktop"  />



    <link href="/stylesheets/chat_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="chat"  />
    <link href="/stylesheets/checklist_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="checklist"  />
    <link href="/stylesheets/discourse-data-explorer_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="discourse-data-explorer"  />
    <link href="/stylesheets/discourse-details_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="discourse-details"  />
    <link href="/stylesheets/discourse-docs_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="discourse-docs"  />
    <link href="/stylesheets/discourse-graphviz_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="discourse-graphviz"  />
    <link href="/stylesheets/discourse-lazy-videos_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="discourse-lazy-videos"  />
    <link href="/stylesheets/discourse-local-dates_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="discourse-local-dates"  />
    <link href="/stylesheets/discourse-narrative-bot_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="discourse-narrative-bot"  />
    <link href="/stylesheets/discourse-post-voting_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="discourse-post-voting"  />
    <link href="/stylesheets/discourse-presence_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="discourse-presence"  />
    <link href="/stylesheets/discourse-solved_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="discourse-solved"  />
    <link href="/stylesheets/discourse-templates_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="discourse-templates"  />
    <link href="/stylesheets/discourse-topic-voting_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="discourse-topic-voting"  />
    <link href="/stylesheets/docker_manager_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="docker_manager"  />
    <link href="/stylesheets/footnote_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="footnote"  />
    <link href="/stylesheets/poll_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="poll"  />
    <link href="/stylesheets/spoiler-alert_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="spoiler-alert"  />
    <link href="/stylesheets/chat_mobile_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="(max-width: 39.99999rem)" rel="stylesheet" data-target="chat_mobile"  />
    <link href="/stylesheets/discourse-post-voting_mobile_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="(max-width: 39.99999rem)" rel="stylesheet" data-target="discourse-post-voting_mobile"  />
    <link href="/stylesheets/discourse-solved_mobile_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="(max-width: 39.99999rem)" rel="stylesheet" data-target="discourse-solved_mobile"  />
    <link href="/stylesheets/discourse-topic-voting_mobile_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="(max-width: 39.99999rem)" rel="stylesheet" data-target="discourse-topic-voting_mobile"  />
    <link href="/stylesheets/chat_desktop_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="(min-width: 40rem)" rel="stylesheet" data-target="chat_desktop"  />
    <link href="/stylesheets/discourse-post-voting_desktop_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="(min-width: 40rem)" rel="stylesheet" data-target="discourse-post-voting_desktop"  />
    <link href="/stylesheets/discourse-topic-voting_desktop_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="(min-width: 40rem)" rel="stylesheet" data-target="discourse-topic-voting_desktop"  />
    <link href="/stylesheets/poll_desktop_cb4f48f1647bda6ed9a1b6fabde8222d4562dcb7.css?__ws=ziggit.dev" media="(min-width: 40rem)" rel="stylesheet" data-target="poll_desktop"  />

  <link href="/stylesheets/common_theme_3_ee69bc8deed3edbf6165c6b0907f8b1a40a6937a.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="common_theme" data-theme-id="3" data-theme-name="discotoc"/>
<link href="/stylesheets/common_theme_6_82687937adc0c88911548d974734be098a1c3acb.css?__ws=ziggit.dev" media="all" rel="stylesheet" data-target="common_theme" data-theme-id="6" data-theme-name="zig syntax highlighting for discourse"/>
    
    

    
    
        <link rel="alternate nofollow" type="application/rss+xml" title="RSS feed of &#39;Cruller: Bun&#39;s Zig Runtime, Continued on Zig 0.16&#39;" href="https://ziggit.dev/t/cruller-buns-zig-runtime-continued-on-zig-0-16/16734.rss" />
    <meta property="og:site_name" content="Ziggit" />
<meta property="og:type" content="website" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:image" content="https://ziggit.dev/uploads/default/original/1X/3417db0e8abaf83a355700b91efd528025492487.png" />
<meta property="og:image" content="https://ziggit.dev/uploads/default/original/1X/3417db0e8abaf83a355700b91efd528025492487.png" />
<meta property="og:url" content="https://ziggit.dev/t/cruller-buns-zig-runtime-continued-on-zig-0-16/16734" />
<meta name="twitter:url" content="https://ziggit.dev/t/cruller-buns-zig-runtime-continued-on-zig-0-16/16734" />
<meta property="og:title" content="Cruller: Bun&#39;s Zig Runtime, Continued on Zig 0.16" />
<meta name="twitter:title" content="Cruller: Bun&#39;s Zig Runtime, Continued on Zig 0.16" />
<meta property="og:description" content="Cruller: a production-focused Bun runtime ported to Zig 0.16 Cruller is a fork of the last Zig-based Bun release, reduced to the parts needed to run already-built production JavaScript servers and ported to vanilla Zig 0.16.  Repository: GitHub - solenopsys/cruller: fork of Bun · GitHub  The project keeps JavaScriptCore, Bun.serve, HTTP/1-3, WebSockets, fetch, streams, Blob, Request/Response, static serving, and the module resolver for pre-built JavaScript. It removes the package manager, bundle..." />
<meta name="twitter:description" content="Cruller: a production-focused Bun runtime ported to Zig 0.16 Cruller is a fork of the last Zig-based Bun release, reduced to the parts needed to run already-built production JavaScript servers and ported to vanilla Zig 0.16.  Repository: GitHub - solenopsys/cruller: fork of Bun · GitHub  The project keeps JavaScriptCore, Bun.serve, HTTP/1-3, WebSockets, fetch, streams, Blob, Request/Response, static serving, and the module resolver for pre-built JavaScript. It removes the package manager, bundle..." />
<meta property="og:article:section" content="Showcase" />
<meta property="og:article:section:color" content="F7941D" />
<meta property="og:article:tag" content="llm-deps" />
<meta property="og:article:tag" content="llm" />
<meta name="twitter:label1" value="Reading time" />
<meta name="twitter:data1" value="6 mins 🕑" />
<meta name="twitter:label2" value="Likes" />
<meta name="twitter:data2" value="85 ❤" />
<meta property="article:published_time" content="2026-07-16T08:01:11+00:00" />
<meta property="og:ignore_canonical" content="true" />

        <link rel="next" href="/t/cruller-buns-zig-runtime-continued-on-zig-0-16/16734?page=2">

    
  </head>
  <body class="crawler ">
    
    <header>
  <a href="/">Ziggit</a>
</header>

    <div id="main-outlet" class="wrap" role="main">
        <div id="topic-title">
    <h1>
      <a href="/t/cruller-buns-zig-runtime-continued-on-zig-0-16/16734">Cruller: Bun&#39;s Zig Runtime, Continued on Zig 0.16</a>
    </h1>

      <div class="topic-category" itemscope itemtype="http://schema.org/BreadcrumbList">
          <span itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem">
            <a href="/c/showcase/7" class="badge-wrapper bullet" itemprop="item">
              <span class='badge-category-bg' style='background-color: #F7941D'></span>
              <span class='badge-category clear-badge'>
                <span class='category-name' itemprop='name'>Showcase</span>
              </span>
            </a>
            <meta itemprop="position" content="1" />
          </span>
      </div>

      <div class="topic-category">
        <div class='discourse-tags list-tags'>
            <a href='https://ziggit.dev/tag/llm-deps' class='discourse-tag' rel="tag">llm-deps</a>, 
            <a href='https://ziggit.dev/tag/llm' class='discourse-tag' rel="tag">llm</a>
        </div>
      </div>
  </div>

  

    <div itemscope itemtype='http://schema.org/DiscussionForumPosting'>
      <meta itemprop='headline' content='Cruller: Bun&#39;s Zig Runtime, Continued on Zig 0.16'>
      <link itemprop='url' href='https://ziggit.dev/t/cruller-buns-zig-runtime-continued-on-zig-0-16/16734'>
      <meta itemprop='datePublished' content='2026-07-16T08:01:11Z'>
        <meta itemprop='articleSection' content='Showcase'>
      <meta itemprop='keywords' content='llm-deps, llm'>
      <div itemprop='publisher' itemscope itemtype="http://schema.org/Organization">
        <meta itemprop='name' content='calder-ty'>
          <div itemprop='logo' itemscope itemtype="http://schema.org/ImageObject">
            <meta itemprop='url' content='https://ziggit.dev/uploads/default/original/2X/a/a65087dbc73e8fc2751c8ff1eebb91d0922b6b27.png'>
          </div>
      </div>


          <div id='post_1'  class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/solenopsys'><span itemprop='name'>solenopsys</span></a>
                
              </span>

                <link itemprop="mainEntityOfPage" href="https://ziggit.dev/t/cruller-buns-zig-runtime-continued-on-zig-0-16/16734">


              <span class="crawler-post-infos">
                  <time  datetime='2026-07-16T08:01:11Z' class='post-time'>
                    July 16, 2026,  8:01am
                  </time>
                  <meta itemprop='dateModified' content='2026-07-16T08:03:02Z'>
              <span itemprop='position'>1</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <h1><a name="p-73493-cruller-a-production-focused-bun-runtime-ported-to-zig-016-1" class="anchor" href="#p-73493-cruller-a-production-focused-bun-runtime-ported-to-zig-016-1" aria-label="Heading link"></a>Cruller: a production-focused Bun runtime ported to Zig 0.16</h1>
<p>Cruller is a fork of the last Zig-based Bun release, reduced to the parts needed to run already-built production JavaScript servers and ported to vanilla Zig 0.16.</p>
<p>Repository: <a href="https://github.com/solenopsys/cruller" class="inline-onebox" rel="noopener nofollow ugc">GitHub - solenopsys/cruller: fork of Bun · GitHub</a></p>
<p>The project keeps JavaScriptCore, <code>Bun.serve</code>, HTTP/1-3, WebSockets, <code>fetch</code>, streams, <code>Blob</code>, <code>Request</code>/<code>Response</code>, static serving, and the module resolver for pre-built JavaScript. It removes the package manager, bundler/transpiler, shell, test runner, most CLI dispatch, N-API, SQL clients, archive support, and other development-oriented subsystems.</p>
<p>The interesting part of the port was separating the runtime from Bun’s old patched Zig build integration. Cruller now has a vanilla Zig 0.16 build graph, compatibility shims for APIs changed since Zig 0.15, and a generated-code embedding module so release builds remain portable instead of loading generated JS from the build directory at runtime.</p>
<p>The main design decision is to treat this as a runtime, not a general-purpose Bun replacement. A minimal launcher loads a pre-built entrypoint; features that require package installation, bundling, TypeScript transformation, or <code>bun test</code> are intentionally outside the scope.</p>
<p>Current measurements on Linux x64, compared with the official Bun 1.3.14 binary:</p>
<ul>
<li>Cruller <code>ReleaseFast</code> stripped runtime: 73.0 MiB</li>
<li>Official Bun runtime: 88.5 MiB</li>
<li>Size reduction: about 18%</li>
<li>V8 Crypto pure-JS benchmark: performance parity; Cruller’s median was about 2% higher, within normal run-to-run variance</li>
</ul>
<p>The runtime is still work in progress, but Zig semantic checks, release builds, CJS/ESM entrypoints, Node path tests, and an HTTP <code>Bun.serve</code> plus built-in <code>fetch()</code> smoke test currently pass.</p>
<h3><a name="p-73493-supported-zig-versions-2" class="anchor" href="#p-73493-supported-zig-versions-2" aria-label="Heading link"></a>Supported Zig versions</h3>
<ul>
<li>Zig 0.16.0</li>
<li>Linux x64 is the currently supported build target</li>
</ul>
<p>Suggested topic tags: <code>showcase</code>, <code>zig-0-16</code>, <code>llm</code></p>
<h3><a name="p-73493-ai-llm-usage-disclosure-3" class="anchor" href="#p-73493-ai-llm-usage-disclosure-3" aria-label="Heading link"></a>AI / LLM usage disclosure</h3>
<p>AI was used as an engineering assistant for parts of the Zig 0.16 migration, build/debug investigation, and focused test work. The project scope, architecture decisions, review of changes, and build/test verification remain maintainer-directed. This is not a purely AI-generated project.</p>
            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="23" />
              <span class='post-likes'>23 Likes</span>
            </div>


            
          </div>
          <div id='post_2' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/xsawyerx'><span itemprop='name'>xsawyerx</span></a>
                
              </span>



              <span class="crawler-post-infos">
                  <time itemprop='datePublished' datetime='2026-07-16T08:08:18Z' class='post-time'>
                    July 16, 2026,  8:08am
                  </time>
                  <meta itemprop='dateModified' content='2026-07-16T08:08:18Z'>
              <span itemprop='position'>2</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <p>Do you aim to address the critique of the code? I.e., cull the bad design decisions, etc.?</p>
            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="4" />
              <span class='post-likes'>4 Likes</span>
            </div>


            
          </div>
          <div id='post_3' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/solenopsys'><span itemprop='name'>solenopsys</span></a>
                
              </span>



              <span class="crawler-post-infos">
                  <time itemprop='datePublished' datetime='2026-07-16T08:19:00Z' class='post-time'>
                    July 16, 2026,  8:19am
                  </time>
                  <meta itemprop='dateModified' content='2026-07-16T08:30:40Z'>
              <span itemprop='position'>3</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <p>My idea is to strip the system down as much as possible and leave only what is required for production.</p>
<p>Development would be done using the full Bun runtime, while production would use its lightweight fork, Cruller. I do not have the resources of the Oven team to develop and maintain a massive general-purpose runtime, so I want to focus on specific production requirements.</p>
<p>The main goals are:</p>
<ul>
<li>strengthen HTTP/2 and HTTP/3 support;</li>
<li>add native ZMQ plugins;</li>
<li>implement a dynamic memory controller through a separate QuickJS-based control plane, allowing complex memory-management policies and configurations.</li>
<li>package the engine as a simple dynamic library with a clean <code>.zig</code> interface, so it can be embedded into other applications with minimal effort.</li>
</ul>
<p>Cruller is not intended to replace Bun for development. It is a minimal, specialized runtime for executing production code.</p>
<p>In any case, I do not want to throw away such a large codebase that has taken several years to build. It makes more sense to turn it into a convenient embeddable library that can be used throughout the Zig ecosystem.</p>
            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="17" />
              <span class='post-likes'>17 Likes</span>
            </div>


            
          </div>
          <div id='post_4' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/WeeBull'><span itemprop='name'>WeeBull</span></a>
                
              </span>



              <span class="crawler-post-infos">
                  <time itemprop='datePublished' datetime='2026-07-16T19:12:59Z' class='post-time'>
                    July 16, 2026,  7:12pm
                  </time>
                  <meta itemprop='dateModified' content='2026-07-16T19:12:59Z'>
              <span itemprop='position'>4</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <p>I wondered if someone would do this.</p>
<p>Honestly, I wish you the best of luck. If you do continue this project seriously I’m sure the community will be interested in what you learn. I did start exploring the bun repo myself from the same point (the last Zig release) and I think you’re absolutely correct to slim it down. Looks like you’ve taken about 290k lines of Zig out of the project (712k down to 425k).</p>
<p>Just getting it to the point where the build is <code>zig build</code> looks like it will be a significant milestone to me. I’m currently failing with…</p>
<pre data-code-wrap="sh"><code class="lang-sh">zig 0.16.0 build --build-file build016.zig check                                                             
anyzig: build file 'build016.zig'
anyzig: appdata '/home/pauls/.local/share/anyzig'
anyzig: zig '0.16.0' already exists at '/home/pauls/.cache/zig/p/N-V-__8AAFFSVRWqblwBIcA-Yqv-u7sbjsJoww8K0mWaHbmJ'
check
└─ compile obj bzrt-check Debug native 1 errors
error: failed to check cache: 'build/codegen/ZigGeneratedClasses.zig' file_hash FileNotFound
error: 1 compilation errors
</code></pre>
            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="2" />
              <span class='post-likes'>2 Likes</span>
            </div>


            
          </div>
          <div id='post_5' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/shimekukuri'><span itemprop='name'>shimekukuri</span></a>
                
              </span>



              <span class="crawler-post-infos">
                  <time itemprop='datePublished' datetime='2026-07-16T19:51:54Z' class='post-time'>
                    July 16, 2026,  7:51pm
                  </time>
                  <meta itemprop='dateModified' content='2026-07-16T19:51:54Z'>
              <span itemprop='position'>5</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <aside class="quote no-group" data-username="solenopsys" data-post="3" data-topic="16734">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://ziggit.dev/user_avatar/ziggit.dev/solenopsys/48/9589_2.png" class="avatar"> solenopsys:</div>
<blockquote>
<p>It makes more sense to turn it into a convenient embeddable library that can be used throughout the Zig ecosystem.</p>
</blockquote>
</aside>
<p>I’m highly interested in where this possibly goes, migrating from a DX perspective to a performance I think more aligns with the capabilities and design philosophies of zig. It would be interesting to get some input of the larger zig community on working with this, but I do have some caution when it comes to supporting in specifically Bun.serve and these others here.</p>
            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="0" />
              <span class='post-likes'></span>
            </div>


            
          </div>
          <div id='post_6' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/kristoff'><span itemprop='name'>kristoff</span></a>
                
              </span>



              <span class="crawler-post-infos">
                  <time itemprop='datePublished' datetime='2026-07-16T20:37:51Z' class='post-time'>
                    July 16, 2026,  8:37pm
                  </time>
                  <meta itemprop='dateModified' content='2026-07-16T20:37:51Z'>
              <span itemprop='position'>6</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <p>That is kind of a crazy undertaking, good luck.</p>
<p>One thing about this whole Bun thing that I find particularly dissatisfying is how Zig compilation speed has been misrepresented. It would be cool if this project were to do whatever work is necessary to be able to make use of incremental compilation and showed the world that Bun could have enjoyed instant rebuilds all along.</p>
            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="18" />
              <span class='post-likes'>18 Likes</span>
            </div>


            
          </div>
          <div id='post_7' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/solenopsys'><span itemprop='name'>solenopsys</span></a>
                
              </span>



              <span class="crawler-post-infos">
                  <time itemprop='datePublished' datetime='2026-07-17T02:13:38Z' class='post-time'>
                    July 17, 2026,  2:13am
                  </time>
                  <meta itemprop='dateModified' content='2026-07-17T02:13:38Z'>
              <span itemprop='position'>7</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <p>Thanks, you found a real clean-checkout bootstrap bug.</p>
<p><code>build016.zig</code> imported generated modules from <code>build/codegen</code>, but those files<br>
are ignored by git. I fixed and pushed this: <code>zig build --build-file build016.zig check</code><br>
now runs the codegen target first, then performs the Zig semantic check.</p>
<p>It still requires an installed Bun for that bootstrap because the remaining<br>
generators are TypeScript. Making codegen Zig-native is a separate milestone.</p>
<p>The reduction is intentional: Bun remains the development toolchain; Cruller is<br>
for running pre-built production JavaScript without carrying the package<br>
manager, TypeScript transpiler, bundler, shell, or test runner.</p>
            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="3" />
              <span class='post-likes'>3 Likes</span>
            </div>


            
          </div>
          <div id='post_8' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/skdishansachin'><span itemprop='name'>skdishansachin</span></a>
                
              </span>



              <span class="crawler-post-infos">
                  <time itemprop='datePublished' datetime='2026-07-17T03:49:55Z' class='post-time'>
                    July 17, 2026,  3:49am
                  </time>
                  <meta itemprop='dateModified' content='2026-07-17T04:15:22Z'>
              <span itemprop='position'>8</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <p>First of all, Best of luck!</p>
<p>One thing I’ve been thinking about, the memory issues seem to come from JSC and Zig not playing nice together (GC vs manual memory), not from Zig being bad. Rust doesn’t really fix that either (I still haven’t done much research so I might be wrong), it just the rewrite still has thousand of unsafe blocks (which the bun team will cleanup eventually) at those same issues, because Rust’s type system can’t reason about a garbage collector it doesn’t own. So it seems like the language change helps with bugs in the runtime’s own code, but doesn’t really solve the core JSC/Zig issue problem…</p>
<p>How are you thinking about that issues in Cruller? You mentioned a QuickJS-based memory controller is that related to this?</p>
            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="2" />
              <span class='post-likes'>2 Likes</span>
            </div>


            
          </div>
          <div id='post_9' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/solenopsys'><span itemprop='name'>solenopsys</span></a>
                
              </span>



              <span class="crawler-post-infos">
                  <time itemprop='datePublished' datetime='2026-07-17T06:00:56Z' class='post-time'>
                    July 17, 2026,  6:00am
                  </time>
                  <meta itemprop='dateModified' content='2026-07-17T06:00:56Z'>
              <span itemprop='position'>9</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <p>I initially thought the move to Rust was just a marketing stunt by Claude to show off how “powerful” their AI is. Turns out they hit serious roadblocks — the migration was supposed to take a couple of days, but there’s still no release after three months. There are actually 13,000 <code>unsafe</code> blocks there, not just “thousands,” so the move didn’t seem to provide much real benefit.</p>
<p>If Claude is truly as powerful as they claim, why not migrate JSC itself to Zig instead of switching to Rust? That would have been a real demonstration of capability. Besides, similar memory protection mechanisms to those in Rust could have been implemented selectively for business logic within Zig.</p>
<p>Regarding the memory controller I’m planning to build: it’s not exactly rocket science. I just want to manage JSC’s parameters so that the runtime doesn’t eat 200–300 MB while idling. I doubt I’ll be diving into major engine modifications right now. My current goal is to get it working stably for both business logic and React-based SSR; performance and memory optimization will follow as targeted improvements later on.</p>
            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="2" />
              <span class='post-likes'>2 Likes</span>
            </div>


            
          </div>
          <div id='post_10' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/WeeBull'><span itemprop='name'>WeeBull</span></a>
                
              </span>



              <span class="crawler-post-infos">
                  <time itemprop='datePublished' datetime='2026-07-17T08:38:49Z' class='post-time'>
                    July 17, 2026,  8:38am
                  </time>
                  <meta itemprop='dateModified' content='2026-07-17T08:38:49Z'>
              <span itemprop='position'>10</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <aside class="quote no-group" data-username="skdishansachin" data-post="8" data-topic="16734">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://ziggit.dev/letter_avatar_proxy/v4/letter/s/779978/48.png" class="avatar"> skdishansachin:</div>
<blockquote>
<p>the memory issues seem to come from JSC and Zig not playing nice together (GC vs manual memory), not from Zig being bad. Rust doesn’t really fix that either (I still haven’t done much research so I might be wrong)</p>
</blockquote>
</aside>
<p>I’ve thought exactly the same thing. It strikes me that to support a language with garbage collected semantics, you probably need to write an allocator with automated releasing of memory. That might be garbage collection or some other scheme.</p>
            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="1" />
              <span class='post-likes'>1 Like</span>
            </div>


            
          </div>
          <div id='post_11' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/WeeBull'><span itemprop='name'>WeeBull</span></a>
                
              </span>



              <span class="crawler-post-infos">
                  <time itemprop='datePublished' datetime='2026-07-17T08:48:01Z' class='post-time'>
                    July 17, 2026,  8:48am
                  </time>
                  <meta itemprop='dateModified' content='2026-07-17T08:48:01Z'>
              <span itemprop='position'>11</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <aside class="quote no-group" data-username="kristoff" data-post="6" data-topic="16734">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://ziggit.dev/user_avatar/ziggit.dev/kristoff/48/9_2.png" class="avatar"> kristoff:</div>
<blockquote>
<p>One thing about this whole Bun thing that I find particularly dissatisfying is how Zig compilation speed has been misrepresented.</p>
</blockquote>
</aside>
<p>Is that because the build process was controlled by a high level Typescript process, with the Zig build only being part of that?</p>
            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="1" />
              <span class='post-likes'>1 Like</span>
            </div>


            
          </div>
          <div id='post_12' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/alanza'><span itemprop='name'>alanza</span></a>
                
              </span>



              <span class="crawler-post-infos">
                  <time itemprop='datePublished' datetime='2026-07-17T12:52:55Z' class='post-time'>
                    July 17, 2026, 12:52pm
                  </time>
                  <meta itemprop='dateModified' content='2026-07-17T12:52:55Z'>
              <span itemprop='position'>12</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <p>no, I think there were structural issues. I’m only repeating third-hand what I heard before, but iirc Bun in Zig used comptime in suboptimal ways that impacted compilation speed, they used <code>usingnamespace</code> (which was a source of slowdowns iirc) well after its deprecation, for a while they depended on a forked version of the compiler for reasons I didn’t understand, etc.</p>
            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="0" />
              <span class='post-likes'></span>
            </div>


            
          </div>
          <div id='post_13' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/kristoff'><span itemprop='name'>kristoff</span></a>
                
              </span>



              <span class="crawler-post-infos">
                  <time itemprop='datePublished' datetime='2026-07-17T13:12:50Z' class='post-time'>
                    July 17, 2026,  1:12pm
                  </time>
                  <meta itemprop='dateModified' content='2026-07-17T13:12:50Z'>
              <span itemprop='position'>13</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <p>I believe all usage of usingnamespace was cleaned up, but for example the forked compiler AFAIK was there till the end, it added <code>#</code> prefixes to struct fields meant to be private, but undoing this change is trivial (just remove the pound sign), at which point you should be able to switch back to the normal compiler. That would be an example of something that should be removed to upgrade to a newer version of Zig.</p>
<p>Then there’s the 0.15.0 Reader/Writer switch to runtime interfaces, that also is a big chunk of work I’d imagine, and lastly the async Io stuff in 0.16.0, which is trivial to get working but a lot of edits at that scale.</p>
<p>If for some miracle Bun were to be upgraded all the way to 0.17.0, which contains more important improvements to incremental, then we would be truly be able to see how long it would take for Bun to rebuild.</p>
<p>As a reminder, this is the last compilation times report we saw as the public (post written by somebody working at Bun):</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://zackoverflow.dev/writing/i-spent-181-minutes-waiting-for-the-zig-compiler-this-week">
  <header class="source">
      

      <a href="https://zackoverflow.dev/writing/i-spent-181-minutes-waiting-for-the-zig-compiler-this-week" target="_blank" rel="noopener">zackoverflow.dev</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://zackoverflow.dev/writing/i-spent-181-minutes-waiting-for-the-zig-compiler-this-week" target="_blank" rel="noopener">I spent 181 minutes waiting for the Zig compiler this week</a></h3>

  <p>TLDR; The Zig compiler takes about 1 minute and 30 seconds to compile debug builds of Bun. Zig's language server doesn't do basic things like type-checking, so often have to run the compiler to see if my code works.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="2" />
              <span class='post-likes'>2 Likes</span>
            </div>


            
          </div>
          <div id='post_14' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/hkupty'><span itemprop='name'>hkupty</span></a>
                
              </span>



              <span class="crawler-post-infos">
                  <time itemprop='datePublished' datetime='2026-07-17T13:19:08Z' class='post-time'>
                    July 17, 2026,  1:19pm
                  </time>
                  <meta itemprop='dateModified' content='2026-07-17T13:19:08Z'>
              <span itemprop='position'>14</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <p>Really nice initiative, good luck! I truly wish you are able to persevere and harvest good results from this effort!</p>
<aside class="quote no-group" data-username="solenopsys" data-post="7" data-topic="16734">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://ziggit.dev/user_avatar/ziggit.dev/solenopsys/48/9589_2.png" class="avatar"> solenopsys:</div>
<blockquote>
<p>Bun remains the development toolchain; Cruller is<br>
for running pre-built production JavaScript without carrying the package<br>
manager, TypeScript transpiler, bundler, shell, or test runner</p>
</blockquote>
</aside>
<p>To me this is the absolutely right mindset. Bun tries to do everything you need for development, which is “unnecessary” (and likely a security hazard) in production. This also makes it more maintainable/sustainable for a single developer. <img src="https://ziggit.dev/images/emoji/twitter/bullseye.png?v=15" title=":bullseye:" class="emoji" alt=":bullseye:" loading="lazy" width="20" height="20"></p>
            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="2" />
              <span class='post-likes'>2 Likes</span>
            </div>


            
          </div>
          <div id='post_15' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/solenopsys'><span itemprop='name'>solenopsys</span></a>
                
              </span>



              <span class="crawler-post-infos">
                  <time itemprop='datePublished' datetime='2026-07-17T13:22:03Z' class='post-time'>
                    July 17, 2026,  1:22pm
                  </time>
                  <meta itemprop='dateModified' content='2026-07-17T13:22:03Z'>
              <span itemprop='position'>15</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <p>I spent 4-6 hours on the migration from 15.2 to version 16; of course, some of the code was removed, but still, the build takes 20 minutes at most, and as far as I remember, there was nothing like 180 minutes there. As for the compiler fork in Bun, it only differs by something like 30 lines of code.</p>
<p>I spent about $5 on the migration. It took a couple of hours with Claude + Python, then DeepSeek (free version) fixed a lot of compilation errors—about 50 of them—then I used Codex a bit more, and overall, there was nothing terrible about it. I definitely didn’t spend $165,000 on tokens, like the Oven team did during their migration to Rust.</p>
            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="3" />
              <span class='post-likes'>3 Likes</span>
            </div>


            
          </div>
          <div id='post_16' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/solenopsys'><span itemprop='name'>solenopsys</span></a>
                
              </span>



              <span class="crawler-post-infos">
                  <time itemprop='datePublished' datetime='2026-07-17T13:37:57Z' class='post-time'>
                    July 17, 2026,  1:37pm
                  </time>
                  <meta itemprop='dateModified' content='2026-07-17T13:37:57Z'>
              <span itemprop='position'>16</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <p>Thanks for the feedback and interest in Cruller, everyone. If you have specific ideas or issues, please feel free to share them.</p>
            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="1" />
              <span class='post-likes'>1 Like</span>
            </div>


            
          </div>
          <div id='post_17' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/kristoff'><span itemprop='name'>kristoff</span></a>
                
              </span>



              <span class="crawler-post-infos">
                  <time itemprop='datePublished' datetime='2026-07-17T13:40:52Z' class='post-time'>
                    July 17, 2026,  1:40pm
                  </time>
                  <meta itemprop='dateModified' content='2026-07-17T13:40:52Z'>
              <span itemprop='position'>17</span>
              </span>
            </div>
            <div class='post' itemprop='text'>
              <p>I think the post is talking about cumulative time.</p>
<p>The benchmark is whether you can run <code>zig build --watch -fincremental</code> on a Linux x64 machine and have the compiler stay on between edits. That will show you exactly how much time it takes for an incremental rebuild of the Zig code. If then the linking is orchestrated externally, this won’t get you all the way to an updated executable, but at least we’ll be able to see how much of that time could have been shaved off by incremental.</p>
            </div>

            <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
              <meta itemprop="interactionType" content="http://schema.org/LikeAction"/>
              <meta itemprop="userInteractionCount" content="0" />
              <span class='post-likes'></span>
            </div>


            
          </div>
          <div id='post_18' itemprop='comment' itemscope itemtype='http://schema.org/Comment' class='topic-body crawler-post'>
            <div class='crawler-post-meta'>
              <span class="creator" itemprop="author" itemscope itemtype="http://schema.org/Person">
                <a itemprop="url" rel='nofollow' href='https://ziggit.dev/u/so