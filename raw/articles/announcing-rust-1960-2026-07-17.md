---
source_url: https://blog.rust-lang.org/2026/05/28/Rust-1.96.0/
ingested: 2026-07-17
sha256: 1bfd335cb29c38f50d0240648b3b4cd023a3626530e886217f5e33c97f3d7e7e
blog_source: Rust Blog
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Announcing Rust 1.96.0 | Rust Blog</title>
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Empowering everyone to build reliable and efficient software.">
     <!-- Twitter card -->
     <meta name="twitter:card" content="summary">
     <meta name="twitter:site" content="@rustlang">
     <meta name="twitter:creator" content="@rustlang">
     <meta name="twitter:title" content="Announcing Rust 1.96.0 | Rust Blog">
     <meta name="twitter:description" content="Empowering everyone to build reliable and efficient software.">
    <meta name="twitter:image" content="https://www.rust-lang.org/static/images/rust-social.jpg">
    
    <!-- Facebook OpenGraph -->
    <meta property="og:title" content="Announcing Rust 1.96.0 | Rust Blog" />
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
    </nav><section id="Announcing Rust 1.96.0" class="white">
  <div class="w-100 mw-none ph3 mw8-m mw8-l center f3">
    <header>
      <h2>Announcing Rust 1.96.0</h2>
      <div class="highlight mt2 mb3"></div>
    </header>

    <div class="publish-date-author">May 28, 2026 &middot; The Rust Release Team
    
    </div>

    <div class="post">
      <p>The Rust team is happy to announce a new version of Rust, 1.96.0. Rust is a programming language empowering everyone to build reliable and efficient software.</p>
<p>If you have a previous version of Rust installed via <code>rustup</code>, you can get 1.96.0 with:</p>
<pre class="giallo z-code"><code data-lang="shellsession"><span class="giallo-l"><span>$</span><span> rustup update stable</span></span></code></pre>
<p>If you don't have it already, you can <a rel="external" href="https://www.rust-lang.org/install.html">get <code>rustup</code></a> from the appropriate page on our website, and check out the <a rel="external" href="https://doc.rust-lang.org/stable/releases.html#version-1960-2026-05-28">detailed release notes for 1.96.0</a>.</p>
<p>If you'd like to help us out by testing future releases, you might consider updating locally to use the beta channel (<code>rustup default beta</code>) or the nightly channel (<code>rustup default nightly</code>). Please <a rel="external" href="https://github.com/rust-lang/rust/issues/new/choose">report</a> any bugs you might come across!</p>
<h2 id="what-s-in-1-96-0-stable"><a class="anchor" href="#what-s-in-1-96-0-stable" aria-hidden="true"></a>
What's in 1.96.0 stable</h2>
<h3 id="new-range-types"><a class="anchor" href="#new-range-types" aria-hidden="true"></a>
New <code>Range*</code> types</h3>
<p>Many users expect <code>Range</code> and related <code>core::ops</code> types to be <code>Copy</code>, but this is not the case: they implement <code>Iterator</code> directly, and <a rel="external" href="https://rust-lang.github.io/rust-clippy/rust-1.95.0/index.html#copy_iterator">it is a footgun to implement both <code>Iterator</code> and <code>Copy</code> on the same type</a> so this has been avoided. <a rel="external" href="https://rust-lang.github.io/rfcs/3550-new-range.html">RFC3550</a> proposed a set of replacement range types that implement <code>IntoIterator</code> rather than <code>Iterator</code>, meaning they can also be <code>Copy</code>. The standard library portion of that RFC is now stable, introducing:</p>
<ul>
<li><code>core::range::Range</code></li>
<li><code>core::range::RangeFrom</code></li>
<li><code>core::range::RangeInclusive</code></li>
<li>Associated iterators</li>
</ul>
<p>A Rust version in the near future will also add <code>core::range::RangeFull</code> and <code>core::range::RangeTo</code> as re-exports from <code>core::ops</code> (these do not implement <code>Iterator</code> and already implement <code>Copy</code>), and <code>core::range::legacy::*</code> as the new home for the current ranges. Range syntax like <code>0..1</code> still produces the legacy types for now, but will be updated to <code>core::range</code> types in a future edition.</p>
<p>With these stabilizations, it is now possible to store slice accessors in <code>Copy</code> types without splitting <code>start</code> and <code>end</code>:</p>
<pre class="giallo z-code"><code data-lang="rust"><span class="giallo-l"><span class="z-keyword">use</span><span class="z-entity z-name z-namespace"> core</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-namespace">range</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">Range</span><span>;</span></span>
<span class="giallo-l"></span>
<span class="giallo-l"><span>#</span><span>[</span><span>derive</span><span>(</span><span class="z-entity z-name z-type">Clone</span><span>,</span><span class="z-entity z-name z-type"> Copy</span><span>)</span><span>]</span></span>
<span class="giallo-l"><span class="z-keyword">pub</span><span class="z-storage z-type"> struct</span><span class="z-entity z-name z-type"> Span</span><span>(</span><span class="z-entity z-name z-type">Range</span><span>&lt;</span><span class="z-entity z-name z-type">usize</span><span>&gt;</span><span>)</span><span>;</span></span>
<span class="giallo-l"></span>
<span class="giallo-l"><span class="z-keyword">impl</span><span class="z-entity z-name z-type"> Span</span><span> {</span></span>
<span class="giallo-l"><span class="z-keyword">    pub</span><span class="z-keyword"> fn</span><span class="z-entity z-name z-function"> of</span><span>(</span><span class="z-variable z-language">self</span><span>,</span><span class="z-variable"> s</span><span class="z-keyword z-operator">:</span><span class="z-keyword z-operator"> &amp;</span><span class="z-entity z-name z-type">str</span><span>)</span><span class="z-keyword z-operator"> -&gt;</span><span class="z-keyword z-operator"> &amp;</span><span class="z-entity z-name z-type">str</span><span> {</span></span>
<span class="giallo-l"><span class="z-keyword z-operator">        &amp;</span><span class="z-variable">s</span><span>[</span><span class="z-variable z-language">self</span><span class="z-keyword z-operator">.</span><span class="z-constant z-numeric">0</span><span>]</span></span>
<span class="giallo-l"><span>    }</span></span>
<span class="giallo-l"><span>}</span></span></code></pre>
<p>The new <code>RangeInclusive</code> also makes its fields public, unlike the legacy version which avoided exposing the exhausted iterator state. This isn't a concern with the new type since it must be converted to begin iteration.</p>
<p>Library authors should consider making use of <code>impl RangeBounds</code> in public API, which accepts both legacy and new range types. If a concrete type is needed, prefer using new ranges as this will eventually become the default.</p>
<h3 id="assert-matching-patterns"><a class="anchor" href="#assert-matching-patterns" aria-hidden="true"></a>
Assert matching patterns</h3>
<p>The new macros <code>assert_matches!</code> and <code>debug_assert_matches!</code> check that a value matches a given pattern, panicking with a <code>Debug</code> representation of the value otherwise. These are essentially the same as <code>assert!(matches!(..))</code> and <code>debug_assert!(matches!(..))</code>, but the printed value improves the possibility of diagnosing the failure.</p>
<p>These new macros have not been added to the standard prelude, because they would collide with popular third-party crates that provide macros with the same name. Instead, they should be manually imported from <code>core</code> or <code>std</code> before use.</p>
<pre class="giallo z-code"><code data-lang="rust"><span class="giallo-l"><span class="z-keyword">use</span><span class="z-entity z-name z-namespace"> core</span><span class="z-keyword z-operator">::</span><span>assert_matches</span><span>;</span></span>
<span class="giallo-l"></span>
<span class="giallo-l"><span class="z-punctuation z-definition z-comment z-comment">///</span><span class="z-comment"> [Random Number](https://xkcd.com/221/)</span></span>
<span class="giallo-l"><span class="z-keyword">fn</span><span class="z-entity z-name z-function"> get_random_number</span><span>(</span><span>)</span><span class="z-keyword z-operator"> -&gt;</span><span class="z-entity z-name z-type"> u32</span><span> {</span></span>
<span class="giallo-l"><span class="z-punctuation z-definition z-comment z-comment">    //</span><span class="z-comment z-line z-double-slash z-comment"> chosen by a fair dice roll.</span></span>
<span class="giallo-l"><span class="z-punctuation z-definition z-comment z-comment">    //</span><span class="z-comment z-line z-double-slash z-comment"> guaranteed to be random.</span></span>
<span class="giallo-l"><span class="z-constant z-numeric">    4</span></span>
<span class="giallo-l"><span>}</span></span>
<span class="giallo-l"></span>
<span class="giallo-l"><span class="z-keyword">fn</span><span class="z-entity z-name z-function"> main</span><span>(</span><span>)</span><span> {</span></span>
<span class="giallo-l"><span class="z-entity z-name z-function">    assert_matches!</span><span>(</span><span class="z-entity z-name z-function">get_random_number</span><span>(</span><span>)</span><span>,</span><span class="z-constant z-numeric"> 1</span><span class="z-keyword z-operator">..=</span><span class="z-constant z-numeric">6</span><span>)</span><span>;</span></span>
<span class="giallo-l"><span>}</span></span></code></pre><h3 id="changes-to-webassembly-targets"><a class="anchor" href="#changes-to-webassembly-targets" aria-hidden="true"></a>
Changes to WebAssembly targets</h3>
<p>WebAssembly targets no longer pass <code>--allow-undefined</code> to the linker which means that undefined symbols when linking are now a linker error instead of being converted to WebAssembly imports from the <code>"env"</code> module. This change prevents modules from linking unless all linking-related symbols are defined to catch bugs earlier and prevent accidental issues with symbol naming or similar.</p>
<p>Undefined linking-related symbols are often indicative of build-time related bugs or misconfiguration. If, however, the old behavior is intended then it can be re-enabled with <code>RUSTFLAGS=-Clink-arg=--allow-undefined</code> or by editing the source code and using <code>#[link(wasm_import_module = "env")]</code> on the block defining the symbol.</p>
<p>This change was <a rel="external" href="https://blog.rust-lang.org/2026/04/04/changes-to-webassembly-targets-and-handling-undefined-symbols/">previously announced</a> on this blog, and now takes effect in Rust 1.96.</p>
<h3 id="stabilized-apis"><a class="anchor" href="#stabilized-apis" aria-hidden="true"></a>
Stabilized APIs</h3>
<ul>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/macro.assert_matches.html"><code>assert_matches!</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/macro.debug_assert_matches.html"><code>debug_assert_matches!</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/panic/struct.AssertUnwindSafe.html#impl-From%3CT%3E-for-AssertUnwindSafe%3CT%3E"><code>From&lt;T&gt; for AssertUnwindSafe&lt;T&gt;</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/cell/struct.LazyCell.html#impl-From%3CT%3E-for-LazyCell%3CT,+F%3E"><code>From&lt;T&gt; for LazyCell&lt;T, F&gt;</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/sync/struct.LazyLock.html#impl-From%3CT%3E-for-LazyLock%3CT,+F%3E"><code>From&lt;T&gt; for LazyLock&lt;T, F&gt;</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/core/range/struct.RangeToInclusive.html"><code>core::range::RangeToInclusive</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/core/range/struct.RangeFrom.html"><code>core::range::RangeFrom</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/core/range/struct.RangeFromIter.html"><code>core::range::RangeFromIter</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/core/range/struct.Range.html"><code>core::range::Range</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/core/range/struct.RangeIter.html"><code>core::range::RangeIter</code></a></li>
</ul>
<h3 id="two-cargo-advisories"><a class="anchor" href="#two-cargo-advisories" aria-hidden="true"></a>
Two Cargo advisories</h3>
<p>Rust 1.96 contains fixes for two vulnerabilities for users of third-party registries.</p>
<ul>
<li>
<p><a rel="external" href="https://blog.rust-lang.org/2026/05/25/cve-2026-5223/">CVE-2026-5223</a> is a <strong>medium</strong> severity vulnerability regarding extraction of crate tarballs with symlinks.</p>
</li>
<li>
<p><a rel="external" href="https://blog.rust-lang.org/2026/05/25/cve-2026-5222/">CVE-2026-5222</a> is a <strong>low</strong> severity vulnerability regarding authentication with normalized URLs.</p>
</li>
</ul>
<p>Users of crates.io are <strong>not affected</strong> by either vulnerability.</p>
<h3 id="other-changes"><a class="anchor" href="#other-changes" aria-hidden="true"></a>
Other changes</h3>
<p>Check out everything that changed in <a rel="external" href="https://github.com/rust-lang/rust/releases/tag/1.96.0">Rust</a>, <a rel="external" href="https://doc.rust-lang.org/nightly/cargo/CHANGELOG.html#cargo-196-2026-05-28">Cargo</a>, and <a rel="external" href="https://github.com/rust-lang/rust-clippy/blob/master/CHANGELOG.md#rust-196">Clippy</a>.</p>
<h2 id="contributors-to-1-96-0"><a class="anchor" href="#contributors-to-1-96-0" aria-hidden="true"></a>
Contributors to 1.96.0</h2>
<p>Many people came together to create Rust 1.96.0. We couldn't have done it without all of you. <a rel="external" href="https://thanks.rust-lang.org/rust/1.96.0/">Thanks!</a></p>

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
          <a href="https://github.com/rust-lang/blog.rust-lang.org/edit/main/content/Rust-1.96.0.md" target="_blank" rel="noopener">Send a fix here</a>!
        </div>
      </div>
    </footer>
  </body>
</html>
