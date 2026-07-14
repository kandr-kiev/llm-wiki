---
source_url: https://sleuth-io.github.io/sx/2026/07/10/your-dropbox-is-now-a-skill-server.html
ingested: 2026-07-14
sha256: b1a9a7da7715eb0330cdea65d5becad9a3d5dd9cd662fb3b346b823aeb959cb6
blog_source: Hacker News AI
---
<!DOCTYPE html>
<html lang="en"><head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1"><!-- Begin Jekyll SEO tag v2.8.0 -->
<title>Your Dropbox is now a skill server | sx blog</title>
<meta name="generator" content="Jekyll v3.10.0" />
<meta property="og:title" content="Your Dropbox is now a skill server" />
<meta name="author" content="Dylan Etkin" />
<meta property="og:locale" content="en_US" />
<meta name="description" content="sx 2.0 is out: a native app for Mac, Windows, and Linux that lets anyone share AI skills with their team, no git and no terminal required." />
<meta property="og:description" content="sx 2.0 is out: a native app for Mac, Windows, and Linux that lets anyone share AI skills with their team, no git and no terminal required." />
<link rel="canonical" href="https://sleuth-io.github.io/sx/2026/07/10/your-dropbox-is-now-a-skill-server.html" />
<meta property="og:url" content="https://sleuth-io.github.io/sx/2026/07/10/your-dropbox-is-now-a-skill-server.html" />
<meta property="og:site_name" content="sx blog" />
<meta property="og:image" content="https://sleuth-io.github.io/sx/sx/assets/skill-server-hero.png" />
<meta property="og:type" content="article" />
<meta property="article:published_time" content="2026-07-10T00:00:00+00:00" />
<meta name="twitter:card" content="summary_large_image" />
<meta property="twitter:image" content="https://sleuth-io.github.io/sx/sx/assets/skill-server-hero.png" />
<meta property="twitter:title" content="Your Dropbox is now a skill server" />
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Dylan Etkin"},"dateModified":"2026-07-10T00:00:00+00:00","datePublished":"2026-07-10T00:00:00+00:00","description":"sx 2.0 is out: a native app for Mac, Windows, and Linux that lets anyone share AI skills with their team, no git and no terminal required.","headline":"Your Dropbox is now a skill server","image":"https://sleuth-io.github.io/sx/sx/assets/skill-server-hero.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://sleuth-io.github.io/sx/2026/07/10/your-dropbox-is-now-a-skill-server.html"},"url":"https://sleuth-io.github.io/sx/2026/07/10/your-dropbox-is-now-a-skill-server.html"}</script>
<!-- End Jekyll SEO tag -->
<link rel="stylesheet" href="/sx/assets/main.css"><link type="application/atom+xml" rel="alternate" href="https://sleuth-io.github.io/sx/feed.xml" title="sx blog" /></head>
<body><header class="site-header" role="banner">

  <div class="wrapper"><a class="site-title" rel="author" href="/sx/">sx blog</a><nav class="site-nav">
        <input type="checkbox" id="nav-trigger" class="nav-trigger" />
        <label for="nav-trigger">
          <span class="menu-icon">
            <svg viewBox="0 0 18 15" width="18px" height="15px">
              <path d="M18,1.484c0,0.82-0.665,1.484-1.484,1.484H1.484C0.665,2.969,0,2.304,0,1.484l0,0C0,0.665,0.665,0,1.484,0 h15.032C17.335,0,18,0.665,18,1.484L18,1.484z M18,7.516C18,8.335,17.335,9,16.516,9H1.484C0.665,9,0,8.335,0,7.516l0,0 c0-0.82,0.665-1.484,1.484-1.484h15.032C17.335,6.031,18,6.696,18,7.516L18,7.516z M18,13.516C18,14.335,17.335,15,16.516,15H1.484 C0.665,15,0,14.335,0,13.516l0,0c0-0.82,0.665-1.483,1.484-1.483h15.032C17.335,12.031,18,12.695,18,13.516L18,13.516z"/>
            </svg>
          </span>
        </label>

        <div class="trigger"><a class="page-link" href="/sx/">sx blog</a></div>
      </nav></div>
</header>
<main class="page-content" aria-label="Content">
      <div class="wrapper">
        <article class="post h-entry" itemscope itemtype="http://schema.org/BlogPosting">

  <header class="post-header">
    <h1 class="post-title p-name" itemprop="name headline">Your Dropbox is now a skill server</h1>
    <p class="post-meta">
      <time class="dt-published" datetime="2026-07-10T00:00:00+00:00" itemprop="datePublished">Jul 10, 2026
      </time>• <span itemprop="author" itemscope itemtype="http://schema.org/Person"><span class="p-author h-card" itemprop="name">Dylan Etkin</span></span></p>
  </header>

  <div class="post-content e-content" itemprop="articleBody">
    <p><img src="/sx/assets/skill-server-hero.png" alt="sx 2.0" /></p>

<p><em>sx 2.0 is out: a native app for Mac, Windows, and Linux that lets anyone share AI skills with their team, no git and no terminal required.</em></p>

<p>A few months ago I wrote that there’s an <a href="/2026/06/05/a-package-manager-for-ai-assets.html">npm-shaped hole in the AI tooling stack</a>. Your best AI users build up skills, MCP configs, and commands that multiply their output, and that knowledge stays trapped on their machines because there’s no clean way to distribute it. We built sx, an open source package manager for AI assets, to fill that hole. It worked. Developers use it to version skills in git vaults and install them across Claude Code, Cursor, Copilot, Codex, Gemini, Cline, and Kiro with a lock file and deterministic installs.</p>

<p>Then I made a mistake I should have seen coming, because I’ve watched Atlassian make it twice. I built the sharing layer for developers and assumed everyone else would eventually meet us at the command line. They won’t. In the sixty or so discovery interviews we’ve run this year, the people getting the most out of skills are increasingly in marketing, legal, sales, and ops. They write great skills. They have no git, no terminal, and no interest in acquiring either. Asking a marketing team to <code class="language-plaintext highlighter-rouge">sx init --type git</code> is asking them to not share skills.</p>

<p>sx 2.0 is the fix. It’s a real desktop app, and the distribution model it leans on is one every team already has: a shared folder.</p>

<h2 id="a-shared-dropbox-folder-is-the-whole-backend">A shared Dropbox folder is the whole backend</h2>

<p>Here’s the workflow for a non-technical team. You open the app, point your library at a folder in Dropbox, Google Drive, OneDrive, or iCloud, and drag your skills in. Markdown goes in, skills come out. Your teammates point the app at the same folder and everything you publish shows up for them. There’s no server and no accounts. The file sync product your company already pays for does the replication.</p>

<p>This works because of the other big change in 2.0: vault format v2. The latest version of every asset now lives directly on disk at <code class="language-plaintext highlighter-rouge">assets/&lt;name&gt;/</code> as plain, readable markdown. Version history lives in <code class="language-plaintext highlighter-rouge">.sx/versions/</code> next to it. You can grep the vault. You can open it in Obsidian. You can point <code class="language-plaintext highlighter-rouge">.claude/skills</code> straight at it and it just works, because there’s nothing to unpack.</p>

<p>The obvious comparison is exactly that Obsidian setup, a markdown vault in a synced folder, and plenty of teams do run their skills that way today. The difference is what happens after the files sync. sx knows about the AI clients natively. When you hit Sync in the app, it runs an <code class="language-plaintext highlighter-rouge">sx install</code> in the background: it resolves what should be installed for you, translates each asset into every client’s format (Claude Code skills, Cursor rules, Copilot instructions, and so on), and writes it to the right place on your machine. Your teammate drops a skill in the shared folder, you click one button, and it’s live in your AI client. That translation layer is the part a folder full of markdown can’t do for you.</p>

<p>Developers lose nothing here. The CLI is still the same Go binary, the git and skills.new vault types still work, and the app and CLI read the same vaults. 2.0 adds collections, which group related skills and install as a unit resolved at read time, so a skill added to a shared collection next month reaches the whole team automatically without anyone re-running anything.</p>

<h2 id="extensions-because-your-teams-problems-arent-my-roadmap">Extensions, because your team’s problems aren’t my roadmap</h2>

<p>The second half of this release line is an extension system for the app. I’ve spent enough years around plugin ecosystems (I was at Atlassian when my co-founder Don built theirs) to believe that the interesting problems in a team tool are always specific to the team, and that cramming every team’s answer into core is how products get bloated and slow.</p>

<p>So the app is now pluggable. An extension is a folder with a manifest and one ES module, no build step until you want one. Extensions can add dashboard widgets, publish-time checks, editor commands, and whole new views. There’s a marketplace that ships with fifteen of them, and the ones people reach for first are the team-health ones:</p>

<ul>
  <li><strong>Collection Doctor</strong> scores a collection 0 to 100 and names the problems: thin descriptions, stale assets that should be retired, near-duplicate skills, oversized skills eating context. Each finding is one click from the asset it names.</li>
  <li>The <strong>adoption widgets</strong> show who on the team is actually using which skills, so you can see whether that skill someone spent a week on is earning its keep.</li>
  <li><strong>Review Rota</strong> gives every asset a review due date that adapts to how heavily it’s used, and rotates reviews fairly across the team.</li>
  <li><strong>Collection Export</strong> compiles a collection into a Claude Code, Codex, or Gemini plugin, or a plain zip, for sharing outside your vault.</li>
</ul>

<p>Two design decisions I’ll defend if you push on them in the comments. First, extensions are permission-gated: no filesystem, no Node, no network beyond hosts an extension explicitly declares, and enabling one shows you a plain-language list of exactly what it can touch, re-prompted whenever an update changes that list. Second, extensions are just sx assets. They publish, version, scope to teams, pin, and audit through the same pipeline as a skill, which means an extension update can never sneak past review the way it can in ecosystems where plugins auto-update out-of-band. Org admins can allowlist or disable third-party extensions vault-wide. The marketplace itself is just another sx vault, so pointing the app at your own repo gives you a private one.</p>

<h2 id="where-this-is-going">Where this is going</h2>

<p>The premise behind sx hasn’t changed since the first release: AI gains are trapped in individuals, and the missing layer is distribution. What changed is my picture of who needs it. The 2.0 line is a bet that the next wave of skill authors won’t be developers, and that meeting them means a native app, a folder they already share, and one sync button that hides a package manager underneath.</p>

<p>Everything is Apache-2.0 and on GitHub: <a href="https://github.com/sleuth-io/sx">github.com/sleuth-io/sx</a>. The app is in the <a href="https://github.com/sleuth-io/sx/releases">release assets</a> for all three platforms, and <code class="language-plaintext highlighter-rouge">brew install sx</code> still gets you the CLI. If you try the shared-folder setup with your team, I want to hear where it breaks. That’s the part of this release I’m least sure survives contact with real Dropbox latency.</p>

  </div><a class="u-url" href="/sx/2026/07/10/your-dropbox-is-now-a-skill-server.html" hidden></a>
</article>

      </div>
    </main><footer class="site-footer h-card">
  <data class="u-url" href="/sx/"></data>

  <div class="wrapper">

    <h2 class="footer-heading">sx blog</h2>

    <div class="footer-col-wrapper">
      <div class="footer-col footer-col-1">
        <ul class="contact-list">
          <li class="p-name">Sleuth</li></ul>
      </div>

      <div class="footer-col footer-col-2"><ul class="social-media-list"></ul>
</div>

      <div class="footer-col footer-col-3">
        <p>Notes from building sx — a package manager for AI assets (skills, rules, MCP configs, commands).</p>
      </div>
    </div>

  </div>

</footer>
</body>

</html>
