---
source_url: https://blog.rust-lang.org/2026/07/16/Rust-1.97.1/
ingested: 2026-07-17
sha256: 5c25fd9652937a993779d611ab5b384fa5c26ff0b8a7028e5bd0a1993ed5715a
blog_source: Rust Blog
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Announcing Rust 1.97.1 | Rust Blog</title>
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Empowering everyone to build reliable and efficient software.">
     <!-- Twitter card -->
     <meta name="twitter:card" content="summary">
     <meta name="twitter:site" content="@rustlang">
     <meta name="twitter:creator" content="@rustlang">
     <meta name="twitter:title" content="Announcing Rust 1.97.1 | Rust Blog">
     <meta name="twitter:description" content="Empowering everyone to build reliable and efficient software.">
    <meta name="twitter:image" content="https://www.rust-lang.org/static/images/rust-social.jpg">
    
    <!-- Facebook OpenGraph -->
    <meta property="og:title" content="Announcing Rust 1.97.1 | Rust Blog" />
    <meta property="og:description" content="Empowering everyone to build reliable and efficient software.">
    <meta property="og:image" content="https://www.rust-lang.org/static/images/rust-social-wide.jpg" />
    <meta property="og:type" content="website" />
    <meta property="og:locale" content="en_US" />
    
    <!-- styles -->
    <link rel="stylesheet" href="https://blog.rust-lang.org/styles/skeleton.css"/>
    <link rel="stylesheet" href="https://blog.rust-lang.org/styles/tachyons.css"/>
    <link rel="stylesheet" href="https://blog.rust-lang.org/styles/fonts.css"/>
    <link rel="stylesheet" href="https://blog.rust-lang.org/styles/app.css"/>
    <link rel="stylesheet" type="text/css" id="syntax-theme" />
    
    <!-- stylesheet for user agents without js -->
    <noscript>
        <link rel="stylesheet" href="https://blog.rust-lang.org/styles/noscript.css">
        <link rel="stylesheet" type="text/css" href="/giallo-dark.css" media="(prefers-color-scheme: dark)" />
        <link rel="stylesheet" type="text/css" href="/giallo-light.css" media="(prefers-color-scheme: light)" />
    </noscript>
    
    <!-- favicon -->
    <link rel="apple-touch-icon" sizes="180x180" href="https://blog.rust-lang.org/images/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="16x16" href="https://blog.rust-lang.org/images/favicon-16x16.png">
    <link rel="icon" type="image/png" sizes="32x32" href="https://blog.rust-lang.org/images/favicon-32x32.png">
    <link rel="icon" type="image/svg+xml" href="https://blog.rust-lang.org/images/favicon.svg">
    <link rel="manifest" href="https://blog.rust-lang.org/images/site.webmanifest">
    <link rel="mask-icon" href="https://blog.rust-lang.org/images/safari-pinned-tab.svg" color="#5bbad5">
    <meta name="msapplication-TileColor" content="#00aba9">
    <meta name="theme-color" content="#ffffff">
    
     <!-- atom -->
     <link type="application/atom+xml" rel="alternate" href="https://blog.rust-lang.org/feed.xml" title="Rust Blog" />
    
    <!-- theme switcher -->
    <script src="https://blog.rust-lang.org/scripts/theme-switch.js"></script>
  </head>
  <body>
    <nav class="flex flex-row justify-center justify-end-l items-center flex-wrap ph2 pl3-ns pr4-ns">
      <div class="brand flex-auto w-100 w-auto-l self-start tc tl-l">
        <a href="https://blog.rust-lang.org/">
          <img class="v-mid ml0-l rust-logo" alt="" src="https://blog.rust-lang.org/images/rust-logo-blk.svg">
          <span class="dib ml1 ml0-l">Rust Blog</span>
        </a>
      </div>
    
      <ul class="nav list w-100 w-auto-l flex flex-none flex-row flex-wrap justify-center justify-end-l items-center pv2 ph0 ph4-ns">
        <li class="tc pv2 ph2 ph4-ns flex-20-s"><a href="https://www.rust-lang.org">Rust</a></li>
        <li class="tc pv2 ph2 ph4-ns flex-20-s"><a href="https://www.rust-lang.org/tools/install">Install</a></li>
        <li class="tc pv2 ph2 ph4-ns flex-20-s"><a href="https://www.rust-lang.org/learn">Learn</a></li>
        <li class="tc pv2 ph2 ph4-ns flex-20-s"><a href="https://www.rust-lang.org/tools">Tools</a></li>
        <li class="tc pv2 ph2 ph4-ns flex-20-s"><a href="https://www.rust-lang.org/governance">Governance</a></li>
        <li class="tc pv2 ph2 ph4-ns flex-20-s"><a href="https://www.rust-lang.org/community">Community</a></li>
        <button class="theme-icon" onclick="dropdown();">🖌
          <ul id="theme-choice">
            <li class="theme-item" onclick="changeThemeTo('light');">Light</li>
            <li class="theme-item" onclick="changeThemeTo('dark');">Dark</li>
            <li class="theme-item" onclick="changeThemeTo('system');">System</li>
          </ul>
        </button>
        <script src="https://blog.rust-lang.org/scripts/theme-switch-post.js"></script>
      </ul>
    </nav><section id="Announcing Rust 1.97.1" class="white">
  <div class="w-100 mw-none ph3 mw8-m mw8-l center f3">
    <header>
      <h2>Announcing Rust 1.97.1</h2>
      <div class="highlight mt2 mb3"></div>
    </header>

    <div class="publish-date-author">July 16, 2026 &middot; The Rust Release Team
    
    </div>

    <div class="post">
      <p>The Rust team has published a new point release of Rust, 1.97.1. Rust is a programming language that is empowering everyone to build reliable and efficient software.</p>
<p>If you have a previous version of Rust installed via rustup, getting Rust 1.97.1 is as easy as:</p>
<pre class="giallo z-code"><code data-lang="plain"><span class="giallo-l"><span>rustup update stable</span></span></code></pre>
<p>If you don't have it already, you can <a rel="external" href="https://www.rust-lang.org/install.html">get <code>rustup</code></a> from the appropriate page on our website.</p>
<h2 id="what-s-in-1-97-1"><a class="anchor" href="#what-s-in-1-97-1" aria-hidden="true"></a>
What's in 1.97.1</h2>
<p>Rust 1.97.1 fixes a <a rel="external" href="https://github.com/rust-lang/rust/issues/159035">miscompilation in an LLVM optimization</a>.</p>
<p>We have backported both an LLVM fix and a disable of the underlying change in Rust 1.97.0 of
Rust's generated IR that increased the likelihood of this happening. However,
note that the underlying miscompilation has been present since at least Rust
1.87.</p>
<p>If you'd like to help us out by testing future releases, you might consider
running your code's CI or locally using the beta channel (<code>rustup default beta</code>) or the nightly
channel (<code>rustup default nightly</code>). Please
<a rel="external" href="https://github.com/rust-lang/rust/issues/new/choose">report</a> any bugs you
might come across!</p>
<h3 id="contributors-to-1-97-1"><a class="anchor" href="#contributors-to-1-97-1" aria-hidden="true"></a>
Contributors to 1.97.1</h3>
<p>Many people came together to create Rust 1.97.1. We couldn't have done it without all of you. <a rel="external" href="https://thanks.rust-lang.org/rust/1.97.1/">Thanks!</a></p>

    </div>
  </div>
</section>
    <footer class="footer">
      <div class="w-100 mw-none ph3 mw8-m mw9-l center f3">
        <div class="row">
          <div class="four columns mt3 mt0-l" id="get-help">
            <h4>Get help!</h4>
            <ul>
              <li><a href="https://doc.rust-lang.org" target="_blank" rel="noopener">Documentation</a></li>
              <li><a href="mailto:core-team@rust-lang.org">Contact the Rust Team</a></li>
            </ul>
          </div>
          <div class="four columns mt3 mt0-l">
            <h4>Terms and policies</h4>
            <ul>
              <li><a href="https://www.rust-lang.org/policies/code-of-conduct">Code of Conduct</a></li>
              <li><a href="https://www.rust-lang.org/policies/licenses">Licenses</a></li>
              <li><a href="https://rustfoundation.org/policy/rust-trademark-policy">Logo Policy and Media Guide</a></li>
              <li><a href="https://www.rust-lang.org/policies/security">Security Disclosures</a></li>
              <li><a href="https://www.rust-lang.org/policies">All Policies</a></li>
            </ul>
          </div>
          <div class="four columns mt3 mt0-l">
            <h4>Social</h4>
            <div class="flex flex-row flex-wrap">
              <a rel="me" href="https://social.rust-lang.org/@rust" target="_blank" rel="noopener"><img src="https://blog.rust-lang.org/images/mastodon.svg" alt="Mastodon"/></a>
              <a rel="me" href="https://bsky.app/profile/rust-lang.org" target="_blank" rel="noopener"><img src="https://blog.rust-lang.org/images/bluesky.svg" alt="Bluesky"/></a>
              <a href="https://www.youtube.com/channel/UCaYhcUwRBNscFNUKTjgPFiA" target="_blank" rel="noopener"><img style="padding-top: 6px; padding-bottom:6px" src="https://blog.rust-lang.org/images/youtube.svg" alt="YouTube"/></a>
              <a href="https://discord.gg/rust-lang" target="_blank" rel="noopener"><img src="https://blog.rust-lang.org/images/discord.svg" alt="Discord"/></a>
              <a href="https://github.com/rust-lang" target="_blank" rel="noopener"><img src="https://blog.rust-lang.org/images/github.svg" alt="GitHub"/></a>
            </div>
            <h4 class="mt4 mb3">RSS</h4>
            <ul>
              <li><a href="https://blog.rust-lang.org/feed.xml">Main Blog</a></li>
              <li><a href="https://blog.rust-lang.org/inside-rust/feed.xml">"Inside Rust" Blog</a></li>
            </ul>
          </div>
    
        </div>
        <div class="attribution">
          Maintained by the Rust Team. See a typo?
          <a href="https://github.com/rust-lang/blog.rust-lang.org/edit/main/content/Rust-1.97.1.md" target="_blank" rel="noopener">Send a fix here</a>!
        </div>
      </div>
    </footer>
  </body>
</html>
