---
source_url: https://blog.rust-lang.org/2026/07/13/crates-io-development-update/
ingested: 2026-07-17
sha256: 580da46c3c3539102df8a7f962331bef179ef204d6f0efaca07332cfc6aaa9c9
blog_source: Rust Blog
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>crates.io: development update | Rust Blog</title>
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Empowering everyone to build reliable and efficient software.">
     <!-- Twitter card -->
     <meta name="twitter:card" content="summary">
     <meta name="twitter:site" content="@rustlang">
     <meta name="twitter:creator" content="@rustlang">
     <meta name="twitter:title" content="crates.io: development update | Rust Blog">
     <meta name="twitter:description" content="Empowering everyone to build reliable and efficient software.">
    <meta name="twitter:image" content="https://www.rust-lang.org/static/images/rust-social.jpg">
    
    <!-- Facebook OpenGraph -->
    <meta property="og:title" content="crates.io: development update | Rust Blog" />
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
    </nav><section id="crates.io: development update" class="white">
  <div class="w-100 mw-none ph3 mw8-m mw8-l center f3">
    <header>
      <h2>crates.io: development update</h2>
      <div class="highlight mt2 mb3"></div>
    </header>

    <div class="publish-date-author">July 13, 2026 &middot; Tobias Bieniek
     on behalf of <a href="https://www.rust-lang.org/governance/teams/crates-io">the crates.io team</a> 
    </div>

    <div class="post">
      <p>Another six months have passed since our <a rel="external" href="https://blog.rust-lang.org/2026/01/21/crates-io-development-update/">last development update</a>, and the crates.io team has been busy. Here's a summary of the most notable changes and improvements made to <a rel="external" href="https://crates.io/">crates.io</a> since then.</p>
<h2 id="source-code-viewer"><a class="anchor" href="#source-code-viewer" aria-hidden="true"></a>
Source Code Viewer</h2>
<p>Crate pages now have a "Code" tab that lets you browse the contents of published crate versions directly on crates.io. This shows you the exact files that <code>cargo</code> downloads when you add a crate as a dependency, which might differ from the linked repository. This makes it much easier to audit your dependencies, including files that never appear in the repository, like the normalized <code>Cargo.toml</code> files that <code>cargo</code> generates.</p>
<p><img src="https://blog.rust-lang.org/2026/07/13/crates-io-development-update/code-tab.png" alt="Source code viewer showing the &quot;Code&quot; tab of the serde crate" /></p>
<p>The viewer comes with a file tree sidebar with search functionality, syntax highlighting, and GitHub-style line selection, where clicking or dragging line numbers produces shareable <code>#L10-L20</code> URLs.</p>
<p>Under the hood, the server now builds a zip file for every published version. Since the <code>.crate</code> files that <code>cargo</code> consumes are gzipped tarballs without random access support, a background job re-packs each of them into a seekable zip archive plus a JSON manifest describing the contained files. Both are served from our static CDN. The frontend then fetches only the manifest and loads each file on demand with an HTTP range request. Because of this architecture, browsing crate sources essentially adds no load on the crates.io API servers. Existing crate versions have been backfilled, so this works for old releases too.</p>
<p>The rendering library behind the code viewer is a diff renderer at heart, and that's no accident: a version-to-version diff viewer built on the same infrastructure is currently in the works. This will allow you to review exactly what changed between two published versions, right on crates.io. Stay tuned!</p>
<h2 id="untangling-crates-io-accounts-from-github"><a class="anchor" href="#untangling-crates-io-accounts-from-github" aria-hidden="true"></a>
Untangling crates.io Accounts from GitHub</h2>
<p>At the end of May, the crates.io team accepted <a rel="external" href="https://github.com/rust-lang/rfcs/pull/3946">RFC #3946</a>. Crates.io accounts always have been tightly coupled to GitHub: signing in means "Log in with GitHub", and your crates.io identity is your GitHub username. The RFC changes that. It introduces usernames that are native to crates.io and independent of linked GitHub accounts, as a prerequisite for eventually supporting login via other identity providers.</p>
<p>The implementation of crates.io usernames has started, but there is still a lot left to do, most visibly the ability to change your crates.io username. After that is complete, there will be future RFCs and implementation for signing in with identity providers other than GitHub. Since all of this touches authentication and account security, we are deliberately taking it slow and rolling these changes out in small, carefully reviewed steps.</p>
<h2 id="advisories-and-suggestions"><a class="anchor" href="#advisories-and-suggestions" aria-hidden="true"></a>
Advisories and Suggestions</h2>
<p>In our <a rel="external" href="https://blog.rust-lang.org/2026/01/21/crates-io-development-update/">January update</a> we introduced the "Security" tab, which shows security advisories from the <a rel="external" href="https://rustsec.org/">RustSec</a> database. We have since taken this integration one step further: crates that RustSec has flagged as unmaintained now show a warning banner directly on their crate pages, linking to the corresponding advisory for details and possible alternatives. Thanks to <a rel="external" href="https://github.com/djc">Dirkjan Ochtman</a> for implementing this feature!</p>
<p><img src="https://blog.rust-lang.org/2026/07/13/crates-io-development-update/unmaintained-banner.png" alt="Unmaintained warning banner on the ansi_term crate page" /></p>
<p>Related to this, some popular crates have been largely absorbed into the Rust standard library over the years, like <code>lazy_static</code>, which has been superseded by <code>std::sync::LazyLock</code> since Rust 1.80. Crate pages of such crates now show a friendly "You might not need this dependency" banner describing the standard library replacement, and superseded crates in dependency lists get a small light bulb icon with a similar hint.</p>
<p><img src="https://blog.rust-lang.org/2026/07/13/crates-io-development-update/std-replacement-banner.png" alt="&quot;You might not need this dependency&quot; banner on the lazy_static crate page" /></p>
<p>The dataset behind this feature lives in the new <a rel="external" href="https://github.com/rust-lang/std-replacement-data">rust-lang/std-replacement-data</a> repository, together with a documented inclusion policy: standard library replacements only, every entry must cite the stable <code>std</code>, <code>core</code>, or <code>alloc</code> API and Rust version, and crate maintainers get a notice-and-comment window before an entry is added. New entries can be proposed upstream and can benefit other tools too.</p>
<h2 id="ferris"><a class="anchor" href="#ferris" aria-hidden="true"></a>
Ferris</h2>
<p>The most delightful change of this cycle: the Ferris on our error pages now follows your mouse cursor with its eyes:</p>
<p><img src="https://blog.rust-lang.org/2026/07/13/crates-io-development-update/ferris.gif" alt="Ferris&#39; eyes following the mouse cursor on the error page" /></p>
<p>Getting a 404 error on crates.io is now slightly less sad.</p>
<h2 id="svelte-frontend-migration-completed"><a class="anchor" href="#svelte-frontend-migration-completed" aria-hidden="true"></a>
Svelte Frontend Migration Completed</h2>
<p>In our <a rel="external" href="https://blog.rust-lang.org/2026/01/21/crates-io-development-update/">January update</a>, we announced that we were experimenting with porting the crates.io frontend from Ember.js to <a rel="external" href="https://svelte.dev/">Svelte</a>. This experiment has concluded successfully: the new frontend reached feature parity, went through a <a rel="external" href="https://blog.rust-lang.org/inside-rust/2026/04/17/crates-io-svelte-public-testing/">public testing phase</a> in April, became the default at the beginning of May, and the Ember.js app has been removed from our repository.</p>
<p>We designed this change to be invisible for our users, since the new frontend is a 1:1 port of the previous design and functionality. For the team and our contributors, however, it is a big deal: the frontend is now built on a more modern framework, which should make it easier for new contributors to get started. It also allows us to iterate faster, as the source code viewer above demonstrates.</p>
<p>We want to thank the <a rel="external" href="https://emberjs.com/teams/">Ember.js team</a> for a framework that served crates.io well for many years, and the Svelte team for making the transition so enjoyable.</p>
<h2 id="miscellaneous"><a class="anchor" href="#miscellaneous" aria-hidden="true"></a>
Miscellaneous</h2>
<p>These were some of the more visible changes to crates.io over the past six months, but a lot has happened "under the hood" as well:</p>
<ul>
<li>
<p><strong>Search performance</strong>: Relevance-sorted search queries previously ranked every crate matching the query, which could take 1-2 seconds for short or common search terms. Ranking is now bounded to the 1,000 matching crates with the highest recent download counts.</p>
</li>
<li>
<p><strong>Reverse dependencies performance</strong>: The reverse dependencies endpoint no longer recomputes the full dependent set on every request. It is now served from a precomputed table kept in sync by database triggers, turning an expensive join into a bounded index scan and greatly reducing the chance of getting a timeout error.</p>
</li>
<li>
<p><strong>New ARCHITECTURE.md</strong>: If you've ever wondered how crates.io actually works, our <a rel="external" href="https://github.com/rust-lang/crates.io/blob/main/docs/ARCHITECTURE.md"><code>ARCHITECTURE.md</code></a> document got a complete rewrite. It is now organized around the high-level systems that make up crates.io and how they fit together, and includes walkthroughs of what happens when you run <code>cargo publish</code>, why a typical crate download never touches our API servers, and how download counts are derived from CDN access logs.</p>
</li>
<li>
<p><strong>Definition lists</strong>: READMEs now render Markdown <a rel="external" href="https://github.com/rust-lang/crates.io/pull/13950">definition lists</a>, a widely used Markdown extension. Our markdown renderer <a rel="external" href="https://crates.io/crates/comrak">comrak</a> already supported them, the extension just wasn't enabled yet. Thanks to <a rel="external" href="https://github.com/mistaste">@mistaste</a> for this contribution!</p>
</li>
<li>
<p><strong>CDN cache tags</strong>: Files uploaded to our static CDN now carry cache-tag metadata, allowing us to invalidate all cached files of a crate or a specific release in a single operation, instead of issuing one invalidation per file URL.</p>
</li>
<li>
<p><strong>Caching improvements</strong>: We removed a global <code>Vary: Cookie</code> response header that was preventing our CDNs from caching public API responses and frontend assets effectively. Per-user responses now use <code>Cache-Control: no-store</code> instead, resulting in better cache hit rates at the CDN edge.</p>
</li>
<li>
<p><strong>Accessibility</strong>: We have made crates.io friendlier to screen readers: decorative icons are now hidden from the accessibility tree, heading hierarchies have been fixed, and lists are marked up as proper lists. ARIA snapshot tests now ensure that regressions can't slip in unnoticed. We plan to continue to improve crates.io accessibility over the coming months.</p>
</li>
<li>
<p><strong>Git index performance</strong>: The background worker's local clone of the git index is now a bare and shallow repository, eliminating roughly 250,000 checked-out files and the full commit history from its disk, improving its performance as we see increased rates of crate publication. The periodic index squashing now goes through the GitHub API instead of generating large git packs locally, which had previously caused out-of-memory failures on the production worker.</p>
</li>
</ul>
<h2 id="feedback"><a class="anchor" href="#feedback" aria-hidden="true"></a>
Feedback</h2>
<p>We hope you enjoyed this update on the development of crates.io. If you have any feedback or questions, please let us know on <a rel="external" href="https://rust-lang.zulipchat.com/#narrow/stream/318791-t-crates-io">Zulip</a> or <a rel="external" href="https://github.com/rust-lang/crates.io/discussions">GitHub</a>. We are always happy to hear from you and are looking forward to your feedback!</p>

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
          <a href="https://github.com/rust-lang/blog.rust-lang.org/edit/main/content/crates-io-development-update-2026-07&#x2F;index.md" target="_blank" rel="noopener">Send a fix here</a>!
        </div>
      </div>
    </footer>
  </body>
</html>
