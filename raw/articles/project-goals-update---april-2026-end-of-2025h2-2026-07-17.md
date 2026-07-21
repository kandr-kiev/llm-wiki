---
source_url: https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/
ingested: 2026-07-17
sha256: 3ed19b01b5f03eb605b0f9992536a9e93097ed4c0986dbd29399192810747324
blog_source: Rust Blog
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Project goals update — April 2026 (end of 2025H2) | Rust Blog</title>
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Empowering everyone to build reliable and efficient software.">
     <!-- Twitter card -->
     <meta name="twitter:card" content="summary">
     <meta name="twitter:site" content="@rustlang">
     <meta name="twitter:creator" content="@rustlang">
     <meta name="twitter:title" content="Project goals update — April 2026 (end of 2025H2) | Rust Blog">
     <meta name="twitter:description" content="Empowering everyone to build reliable and efficient software.">
    <meta name="twitter:image" content="https://www.rust-lang.org/static/images/rust-social.jpg">
    
    <!-- Facebook OpenGraph -->
    <meta property="og:title" content="Project goals update — April 2026 (end of 2025H2) | Rust Blog" />
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
    </nav><section id="Project goals update — April 2026 (end of 2025H2)" class="white">
  <div class="w-100 mw-none ph3 mw8-m mw8-l center f3">
    <header>
      <h2>Project goals update — April 2026 (end of 2025H2)</h2>
      <div class="highlight mt2 mb3"></div>
    </header>

    <div class="publish-date-author">May 18, 2026 &middot; Nurzhan Saken
     on behalf of <a href="https://www.rust-lang.org/governance/teams/launching-pad#team-goals">the Goals team</a> 
    </div>

    <div class="post">
      <p>The 2025H2 Project Goal period has now concluded. Over these months, the Rust Project pursued <a rel="external" href="https://rust-lang.github.io/rust-project-goals/2025h2/goals.html">41 Project Goals</a>, 13 of which were designated as <a rel="external" href="https://rust-lang.github.io/rust-project-goals/2025h2/goals.html#flagship-goals">Flagship Goals</a>. This post contains curated updates on our progress since the <a rel="external" href="https://blog.rust-lang.org/2026/01/05/project-goals-2025-december-update/">last post</a> and the final status for each of the goals (many of which continue as part of the 2026 period). Full details for any particular goal are available in its <a rel="external" href="https://github.com/rust-lang/rust-project-goals/issues?q=is%3Aissue%20label%3Aex-2025h2">tracking issue</a>.</p>
<p>Thanks to everyone who contributed! &lt;3</p>
<h2 id="table-of-contents"><a class="anchor" href="#table-of-contents" aria-hidden="true"></a>
Table of contents</h2>
<ul>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#flagship-beyond-the">Flagship: Beyond the <code>&amp;</code></a>
<ul>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#continue-experimentation-with-pin-ergonomics">Continue Experimentation with Pin Ergonomics</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#design-a-language-feature-to-solve-field-projections">Design a language feature to solve Field Projections</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#reborrow-traits">Reborrow traits</a></li>
</ul>
</li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#flagship-flexible-fast-er-compilation">Flagship: Flexible, fast(er) compilation</a>
<ul>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#build-std">build-std</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#production-ready-cranelift-backend">Production-ready cranelift backend</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#promoting-parallel-front-end">Promoting Parallel Front End</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#relink-don-t-rebuild">Relink don't Rebuild</a></li>
</ul>
</li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#flagship-higher-level-rust">Flagship: Higher-level Rust</a>
<ul>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#ergonomic-ref-counting-rfc-decision-and-preview">Ergonomic ref-counting: RFC decision and preview</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#stabilize-cargo-script">Stabilize cargo-script</a></li>
</ul>
</li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#flagship-unblocking-dormant-traits">Flagship: Unblocking dormant traits</a>
<ul>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#evolving-trait-hierarchies">Evolving trait hierarchies</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#in-place-initialization">In-place initialization</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#next-generation-trait-solver">Next-generation trait solver</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#stabilizable-polonius-support-on-nightly">Stabilizable Polonius support on nightly</a></li>
</ul>
</li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#other-goal-updates">Other goal updates</a>
<ul>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#add-a-team-charter-for-rustdoc-team">Add a team charter for rustdoc team</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#borrow-checking-in-a-mir-formality">Borrow checking in a-mir-formality</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#c-rust-interop-problem-space-mapping">C++/Rust Interop Problem Space Mapping</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#comprehensive-niche-checks-for-rust">Comprehensive niche checks for Rust</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#const-generics">Const Generics</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#continue-resolving-cargo-semver-checks-blockers-for-merging-into-cargo">Continue resolving <code>cargo-semver-checks</code> blockers for merging into cargo</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#develop-the-capabilities-to-keep-the-fls-up-to-date">Develop the capabilities to keep the FLS up to date</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#emit-retags-in-codegen">Emit Retags in Codegen</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#expand-the-rust-reference-to-specify-more-aspects-of-the-rust-language">Expand the Rust Reference to specify more aspects of the Rust language</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#finish-the-libtest-json-output-experiment">Finish the libtest json output experiment</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#finish-the-std-offload-module">Finish the std::offload module</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#getting-rust-for-linux-into-stable-rust-compiler-features">Getting Rust for Linux into stable Rust: compiler features</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#getting-rust-for-linux-into-stable-rust-language-features">Getting Rust for Linux into stable Rust: language features</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#implement-open-api-namespace-support">Implement Open API Namespace Support</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#mir-move-elimination">MIR move elimination</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#prototype-a-new-set-of-cargo-plumbing-commands">Prototype a new set of Cargo "plumbing" commands</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#prototype-cargo-build-analysis">Prototype Cargo build analysis</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#reflection-and-comptime">reflection and comptime</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#rework-cargo-build-dir-layout">Rework Cargo Build Dir Layout</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#run-more-tests-for-gcc-backend-in-the-rust-s-ci">Run more tests for GCC backend in the Rust's CI</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#rust-stabilization-of-memorysanitizer-and-threadsanitizer-support">Rust Stabilization of MemorySanitizer and ThreadSanitizer Support</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#rust-vision-document">Rust Vision Document</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#rustc-perf-improvements">rustc-perf improvements</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#stabilize-public-private-dependencies">Stabilize public/private dependencies</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#stabilize-rustdoc-doc-cfg-feature">Stabilize rustdoc <code>doc_cfg</code> feature</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#sve-and-sme-on-aarch64">SVE and SME on AArch64</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#type-system-documentation">Type System Documentation</a></li>
<li><a href="https://blog.rust-lang.org/2026/05/18/project-goals-2026-04/#unsafe-fields">Unsafe Fields</a></li>
</ul>
</li>
</ul>
<hr />
<h2 id="flagship-beyond-the"><a class="anchor" href="#flagship-beyond-the" aria-hidden="true"></a>
Flagship: Beyond the <code>&amp;</code></h2>
<h3 id="continue-experimentation-with-pin-ergonomics"><a class="anchor" href="#continue-experimentation-with-pin-ergonomics" aria-hidden="true"></a>
<a rel="external" href="https://github.com/rust-lang/rust-project-goals/issues/389">Continue Experimentation with Pin Ergonomics</a></h3>
<ul>
<li><strong>People involved:</strong> <strong><a rel="external" href="https://github.com/frank-king">Frank King</a></strong></li>
<li><strong>Champions:</strong> <a rel="external" href="http://github.com/rust-lang/compiler-team">compiler</a> (<a rel="external" href="https://github.com/oli-obk">Oliver Scherer</a>), <a rel="external" href="http://github.com/rust-lang/lang-team">lang</a> (<a rel="external" href="https://github.com/traviscross">TC</a>)</li>
<li><strong>Status:</strong> <a rel="external" href="https://rust-lang.github.io/rust-project-goals/2026/pin-ergonomics.html">Continued</a></li>
</ul>
<details>
<summary>3 detailed updates available.</summary>
<ul>
<li>
<p><strong><a rel="external" href="https://github.com/frank-king">Frank King</a></strong> — <a rel="external" href="https://github.com/rust-lang/rust-project-goals/issues/389#issuecomment-3963321984">comment from 2026-02-26</a></p>
<blockquote>
<p>(Just come back from the Spring Festival)</p>
<ul>
<li>(locally, no PR yet): design and implement the borrow checking algorithms of <code>&amp;pin</code></li>
<li>Reviewed <a rel="external" href="https://github.com/rust-lang/rust/pull/144537">Add <code>Drop::pin_drop</code> for pinned drops</a>, to update the submodule <code>book</code></li>
<li>Reviewed <a rel="external" href="https://github.com/rust-lang/rust/pull/149130">Implement coercions between <code>&amp;pin (mut|const) T</code> and <code>&amp;(mut) T</code> when <code>T: Unpin</code></a>, to do some refactors according to the reviewed messages.</li>
</ul>
</blockquote>
</li>
<li>
<p><strong><a rel="external" href="https://github.com/frank-king">Frank King</a></strong> — <a rel="external" href="https://github.com/rust-lang/rust-project-goals/issues/389#issuecomment-4064499322">comment from 2026-03-16</a></p>
<blockquote>
<ul>
<li>Merged <a rel="external" href="https://github.com/rust-lang/rust/pull/149130">Implement coercions between <code>&amp;pin (mut|const) T</code> and <code>&amp;(mut) T</code> when <code>T: Unpin</code></a>.</li>
<li>Opened draft PR <a rel="external" href="https://github.com/rust-lang/rust/pull/153693">Implement borrowck for <code>&amp;pin mut|const $place</code></a>. The implementation needs to be refined and self-reviewed before the community reviews.</li>
</ul>
</blockquote>
</li>
<li>
<p><strong><a rel="external" href="https://github.com/frank-king">Frank King</a></strong> — <a rel="external" href="https://github.com/rust-lang/rust-project-goals/issues/389#issuecomment-4258655696">comment from 2026-04-16</a></p>
<blockquote>
<p>Self-reviewed <a rel="external" href="https://github.com/rust-lang/rust/pull/153693">Implement borrowck for <code>&amp;pin mut|const $place</code></a>. Found that the current approach of handling pinned borrows may be incorrect, as it failed to distinguish a pinned borrow from a coercion of a normal-to-pinned reference. The latter doesn't prevent a <code>T: Unpin</code> type from being moved, but the former does, which breaks the pin coercion test.</p>
</blockquote>
</li>
</ul>
</details>
<h3 id="design-a-language-feature-to-solve-field-projections"><a class="anchor" href="#design-a-language-feature-to-solve-field-projections" aria-hidden="true"></a>
<a rel="external" href="https://github.com/rust-lang/rust-project-goals/issues/390">Design a language feature to solve Field Projections</a></h3>
<ul>
<li><strong>People involved:</strong> <strong><a rel="external" href="https://github.com/BennoLossin">Benno Lossin</a></strong></li>
<li><strong>Champions:</strong> <a rel="external" href="http://github.com/rust-lang/lang-team">lang</a> (<a rel="external" href="https://github.com/tmandry">Tyler Mandry</a>)</li>
<li><strong>Status:</strong> <a rel="external" href="https://rust-lang.github.io/rust-project-goals/2026/field-projections.html">Continued</a></li>
</ul>
<details>
<summary>5 detailed updates available.</summary>
<ul>
<li>
<p><strong><a rel="external" href="https://github.com/BennoLossin">Benno Lossin</a></strong> — <a rel="external" href="https://github.com/rust-lang/rust-project-goals/issues/390#issuecomment-3703190328">comment from 2026-01-01</a></p>
<blockquote>
<ul>
<li>At the beginning of December, we set out to <a rel="external" href="https://github.com/rust-lang/rust-project-goals/issues/390#issuecomment-3621913656">answer five important questions</a> regarding the virtual places approach. We discussed four questions and arrived at answers for three.
<ul>
<li>The first question we looked at was question 3 <a rel="external" href="https://github.com/rust-lang/rust-project-goals/issues/390#issuecomment-3644702112">Canonical Projections</a>.</li>
<li>Next we looked at question 4 <a rel="external" href="https://github.com/rust-lang/rust-project-goals/issues/390#issuecomment-3659055067">Non-Indirected Containers</a>.</li>
<li>As the final question we answered, we looked at question 1 <a rel="external" href="https://github.com/rust-lang/rust-project-goals/issues/390#issuecomment-3677624396">Field-by-Field Projections vs One-Shot Projections</a>.</li>
<li>At the moment, we are investigating question 2 and I wrote a <a rel="external" href="https://bennolossin.github.io/blog/field-projections/virtual-places-and-borrowck.html">blog post</a> with a potential solution that still needs feedback.</li>
</ul>
</li>
<li>We started a <a rel="external" href="https://github.com/rust-lang/rust-project-goals/issues/390#issuecomment-3690808729">Wiki Project</a> to consolidate our knowledge in one place.
<ul>
<li>We <a rel="external" href="https://github.com/rust-lang/beyond-refs/pull/9">implemented an algorithm</a> to determine the type of a place expression.</li>
</ul>
</li>
<li>Our plan is to continue this project goal in the next goal period.</li>
</ul>
</blockquote>
</li>
<li>
<p><strong><a rel="external" href="https://github.com/BennoLossin">Benno Lossin</a></strong> — <a rel="external" href="https://github.com/rust-lang/rust-project-goals/issues/390#issuecomment-3796971577">comment from 2026-01-25</a></p>
<blockquote>
<p>Earlier this month, <a rel="external" href="https://github.com/Nadrieril">Nadrieril</a> <a rel="external" href="https://github.com/dingxiangfei2009">Ding Xiang Fei</a> and I held a meeting on autoref and method resolution in a world with field projections. This meeting resulted in a new page for the wiki on <a rel="external" href="https://rust-lang.github.io/beyond-refs/autoref.html">autoref</a>.</p>
</blockquote>
</li>
<li>
<p><strong><a rel="external" href="https://github.com/BennoLossin">Benno Lossin</a></strong> — <a rel="external" href="https://github.com/rust-lang/rust-project-goals/issues/390#issuecomment-3977436014">comment from 2026-02-28</a></p>
<blockquote>
<p>The first pull request of the lang experiment has just been merged: rust-lang/rust#152730</p>
<p>This PR enables the use of the <code>field_of!</code> macro to obtain a unique type for each field of a struct, enum variant, tuple, or union. We call these types field representing types (FRTs). When the base type is a struct that is not <code>repr(packed)</code>, only contains <code>Sized</code> fields, this type automatically implements the <code>Field</code> trait that exposes some information about the field to the type system. The offset in bytes from the start of the struct, the type of the field and the type of the base type.</p>
<p>The feature is still incomplete and highly experimental. We also want to tackle the limitations in future PRs. For the moment this is enough to give us the ability to experiment with library versions of field projections and write functions that are generic over the fields of structs. For example one can write code like this:</p>
<pre class="giallo z-code"><code data-lang="rust"><span class="giallo-l"><span>#</span><span>!</span><span>[</span><span>feature</span><span>(</span><span>field_projections</span><span>)</span><span>]</span></span>
<span class="giallo-l"></span>
<span class="giallo-l"><span class="z-keyword">use</span><span class="z-entity z-name z-namespace"> std</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-namespace">field</span><span class="z-keyword z-operator">::</span><span>{</span><span class="z-entity z-name z-type">Field</span><span>,</span><span> field_of</span><span>}</span><span>;</span></span>
<span class="giallo-l"><span class="z-keyword">use</span><span class="z-entity z-name z-namespace"> std</span><span class="z-keyword z-operator">::</span><span>ptr</span><span>;</span></span>
<span class="giallo-l"></span>
<span class="giallo-l"><span class="z-keyword">fn</span><span class="z-entity z-name z-function"> project_ref</span><span>&lt;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span>,</span><span class="z-entity z-name z-type"> T</span><span>,</span><span class="z-entity z-name z-type"> F</span><span class="z-keyword z-operator">:</span><span class="z-entity z-name z-type"> Field</span><span>&lt;</span><span class="z-entity z-name z-type">Base</span><span class="z-keyword z-operator z-assignment z-keyword z-operator"> =</span><span class="z-entity z-name z-type"> T</span><span>&gt;</span><span>&gt;</span><span>(</span><span class="z-variable">r</span><span class="z-keyword z-operator">:</span><span class="z-keyword z-operator"> &amp;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span class="z-entity z-name z-type"> T</span><span>)</span><span class="z-keyword z-operator"> -&gt;</span><span class="z-keyword z-operator"> &amp;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span class="z-entity z-name z-namespace"> F</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">Type</span><span> {</span></span>
<span class="giallo-l"><span class="z-punctuation z-definition z-comment z-comment">    //</span><span class="z-comment z-line z-double-slash z-comment"> SAFETY: the `Field` trait guarantees that this is sound.</span></span>
<span class="giallo-l"><span class="z-keyword">    unsafe</span><span> {</span><span class="z-keyword z-operator"> &amp;</span><span class="z-keyword z-operator">*</span><span class="z-entity z-name z-namespace">ptr</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-function">from_ref</span><span>(</span><span class="z-variable">r</span><span>)</span><span class="z-keyword z-operator">.</span><span class="z-entity z-name z-function">byte_add</span><span>(</span><span class="z-entity z-name z-namespace">F</span><span class="z-keyword z-operator">::</span><span class="z-constant z-other">OFFSET</span><span>)</span><span class="z-keyword z-operator">.</span><span class="z-entity z-name z-function">cast</span><span>(</span><span>)</span><span> }</span></span>
<span class="giallo-l"><span>}</span></span>
<span class="giallo-l"></span>
<span class="giallo-l"><span class="z-storage z-type">struct</span><span class="z-entity z-name z-type"> Struct</span><span> {</span></span>
<span class="giallo-l"><span class="z-variable">    field</span><span class="z-keyword z-operator">:</span><span class="z-entity z-name z-type"> i32</span><span>,</span></span>
<span class="giallo-l"><span class="z-variable">    other</span><span class="z-keyword z-operator">:</span><span class="z-entity z-name z-type"> u32</span><span>,</span></span>
<span class="giallo-l"><span>}</span></span>
<span class="giallo-l"></span>
<span class="giallo-l"><span class="z-keyword">fn</span><span class="z-entity z-name z-function"> main</span><span>(</span><span>)</span><span> {</span></span>
<span class="giallo-l"><span class="z-storage z-type">    let</span><span class="z-variable"> s</span><span class="z-keyword z-operator z-assignment z-keyword z-operator"> =</span><span class="z-entity z-name z-type"> Struct</span><span> {</span><span class="z-variable"> field</span><span class="z-keyword z-operator">:</span><span class="z-constant z-numeric"> 42</span><span>,</span><span class="z-variable"> other</span><span class="z-keyword z-operator">:</span><span class="z-constant z-numeric"> 24</span><span> }</span><span>;</span></span>
<span class="giallo-l"><span class="z-storage z-type">    let</span><span class="z-variable"> r</span><span class="z-keyword z-operator z-assignment z-keyword z-operator"> =</span><span class="z-keyword z-operator"> &amp;</span><span class="z-variable">s</span><span>;</span></span>
<span class="giallo-l"><span class="z-storage z-type">    let</span><span class="z-variable"> field</span><span class="z-keyword z-operator z-assignment z-keyword z-operator"> =</span><span class="z-entity z-name z-function"> project_ref</span><span class="z-keyword z-operator">::</span><span>&lt;</span><span class="z-variable">_</span><span>,</span><span class="z-entity z-name z-function"> field_of!</span><span>(</span><span class="z-entity z-name z-type">Struct</span><span>,</span><span class="z-variable"> field</span><span>)</span><span>&gt;</span><span>(</span><span class="z-variable">r</span><span>)</span><span>;</span></span>
<span class="giallo-l"><span class="z-storage z-type">    let</span><span class="z-variable"> other</span><span class="z-keyword z-operator z-assignment z-keyword z-operator"> =</span><span class="z-entity z-name z-function"> project_ref</span><span class="z-keyword z-operator">::</span><span>&lt;</span><span class="z-variable">_</span><span>,</span><span class="z-entity z-name z-function"> field_of!</span><span>(</span><span class="z-entity z-name z-type">Struct</span><span>,</span><span class="z-variable"> other</span><span>)</span><span>&gt;</span><span>(</span><span class="z-variable">r</span><span>)</span><span>;</span></span>
<span class="giallo-l"><span class="z-entity z-name z-function">    println!</span><span>(</span><span class="z-punctuation z-definition z-string z-string">&quot;</span><span class="z-string z-quoted z-string">field: </span><span class="z-string z-quoted z-string">{</span><span class="z-string z-quoted z-string">field</span><span class="z-string z-quoted z-string">}</span><span class="z-punctuation z-definition z-string z-string">&quot;</span><span>)</span><span>;</span><span class="z-punctuation z-definition z-comment z-comment"> //</span><span class="z-comment z-line z-double-slash z-comment"> prints 42</span></span>
<span class="giallo-l"><span class="z-entity z-name z-function">    println!</span><span>(</span><span class="z-punctuation z-definition z-string z-string">&quot;</span><span class="z-string z-quoted z-string">other: </span><span class="z-string z-quoted z-string">{</span><span class="z-string z-quoted z-string">other</span><span class="z-string z-quoted z-string">}</span><span class="z-punctuation z-definition z-string z-string">&quot;</span><span>)</span><span>;</span><span class="z-punctuation z-definition z-comment z-comment"> //</span><span class="z-comment z-line z-double-slash z-comment"> prints 24</span></span>
<span class="giallo-l"><span>}</span></span></code></pre>
<p>A very important feature of the types returned by <code>field_of!</code> is that you can implement traits for them if you own the base type. This allows anointing fields with information by extending the <code>Field</code> trait. For example, this allows encoding the property of being a structurally pinned field:</p>
<pre class="giallo z-code"><code data-lang="rust"><span class="giallo-l"><span class="z-keyword">use</span><span class="z-entity z-name z-namespace"> std</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-namespace">pin</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">Pin</span><span>;</span></span>
<span class="giallo-l"></span>
<span class="giallo-l"><span class="z-keyword">unsafe</span><span class="z-storage z-type"> trait</span><span class="z-entity z-name z-type"> PinnableField</span><span class="z-keyword z-operator">:</span><span class="z-entity z-name z-type"> Field</span><span> {</span></span>
<span class="giallo-l"><span class="z-storage z-type">    type</span><span class="z-entity z-name z-type"> StructuralRefMut</span><span>&lt;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span>&gt;</span></span>
<span class="giallo-l"><span class="z-keyword">    where</span></span>
<span class="giallo-l"><span class="z-variable z-language">        Self</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">Type</span><span class="z-keyword z-operator">:</span><span> &#39;</span><span class="z-entity z-name z-type">a</span><span>,</span></span>
<span class="giallo-l"><span class="z-variable z-language">        Self</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">Base</span><span class="z-keyword z-operator">:</span><span> &#39;</span><span class="z-entity z-name z-type">a</span><span>;</span></span>
<span class="giallo-l"></span>
<span class="giallo-l"><span class="z-keyword">    fn</span><span class="z-entity z-name z-function"> project_mut</span><span>&lt;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span>&gt;</span><span>(</span><span class="z-variable">base</span><span class="z-keyword z-operator">:</span><span class="z-entity z-name z-type"> Pin</span><span>&lt;</span><span class="z-keyword z-operator">&amp;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span class="z-storage z-storage z-modifier"> mut</span><span class="z-variable z-language"> Self</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">Base</span><span>&gt;</span><span>)</span><span class="z-keyword z-operator"> -&gt;</span><span class="z-variable z-language"> Self</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">StructuralRefMut</span><span>&lt;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span>&gt;</span></span>
<span class="giallo-l"><span class="z-keyword">    where</span></span>
<span class="giallo-l"><span class="z-variable z-language">        Self</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">Type</span><span class="z-keyword z-operator">:</span><span> &#39;</span><span class="z-entity z-name z-type">a</span><span>,</span></span>
<span class="giallo-l"><span class="z-variable z-language">        Self</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">Base</span><span class="z-keyword z-operator">:</span><span> &#39;</span><span class="z-entity z-name z-type">a</span><span>;</span></span>
<span class="giallo-l"><span>}</span></span>
<span class="giallo-l"></span>
<span class="giallo-l"><span class="z-keyword">fn</span><span class="z-entity z-name z-function"> project_pinned</span><span>&lt;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span>,</span><span class="z-entity z-name z-type"> T</span><span>,</span><span class="z-entity z-name z-type"> F</span><span>&gt;</span><span>(</span><span class="z-variable">r</span><span class="z-keyword z-operator">:</span><span class="z-entity z-name z-type"> Pin</span><span>&lt;</span><span class="z-keyword z-operator">&amp;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span class="z-storage z-storage z-modifier"> mut</span><span class="z-entity z-name z-type"> T</span><span>&gt;</span><span>)</span><span class="z-keyword z-operator"> -&gt;</span><span> &lt;</span><span class="z-entity z-name z-type">F</span><span class="z-keyword"> as</span><span class="z-entity z-name z-type"> PinnableField</span><span>&gt;</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">StructuralRefMut</span><span>&lt;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span>&gt;</span></span>
<span class="giallo-l"><span class="z-keyword">where</span></span>
<span class="giallo-l"><span class="z-entity z-name z-type">    F</span><span class="z-keyword z-operator">:</span><span class="z-entity z-name z-type"> PinnableField</span><span>&lt;</span><span class="z-entity z-name z-type">Base</span><span class="z-keyword z-operator z-assignment z-keyword z-operator"> =</span><span class="z-entity z-name z-type"> T</span><span>&gt;</span><span>,</span></span>
<span class="giallo-l"><span>{</span></span>
<span class="giallo-l"><span class="z-entity z-name z-type">    F</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-function">project_mut</span><span>(</span><span class="z-variable">r</span><span>)</span></span>
<span class="giallo-l"><span>}</span></span></code></pre>
<p>We can then implement this extra trait for all of the fields of our struct (and automate that with a proc-macro):</p>
<pre class="giallo z-code"><code data-lang="rust"><span class="giallo-l"><span class="z-keyword">unsafe</span><span class="z-keyword"> impl</span><span class="z-entity z-name z-type"> PinnableField</span><span class="z-keyword z-control"> for</span><span class="z-entity z-name z-function"> field_of!</span><span>(</span><span class="z-entity z-name z-type">Struct</span><span>,</span><span class="z-variable"> field</span><span>)</span><span> {</span></span>
<span class="giallo-l"><span class="z-storage z-type">    type</span><span class="z-entity z-name z-type"> StructuralRefMut</span><span>&lt;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span>&gt;</span><span class="z-keyword z-operator z-assignment z-keyword z-operator"> =</span><span class="z-keyword z-operator"> &amp;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span class="z-storage z-storage z-modifier"> mut</span><span class="z-entity z-name z-type"> i32</span><span>;</span></span>
<span class="giallo-l"></span>
<span class="giallo-l"><span class="z-keyword">    fn</span><span class="z-entity z-name z-function"> project_mut</span><span>&lt;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span>&gt;</span><span>(</span><span class="z-variable">base</span><span class="z-keyword z-operator">:</span><span class="z-entity z-name z-type"> Pin</span><span>&lt;</span><span class="z-keyword z-operator">&amp;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span class="z-storage z-storage z-modifier"> mut</span><span class="z-variable z-language"> Self</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">Base</span><span>&gt;</span><span>)</span><span class="z-keyword z-operator"> -&gt;</span><span class="z-variable z-language"> Self</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">StructuralRefMut</span><span>&lt;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span>&gt;</span></span>
<span class="giallo-l"><span class="z-keyword">    where</span></span>
<span class="giallo-l"><span class="z-variable z-language">        Self</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">Type</span><span class="z-keyword z-operator">:</span><span> &#39;</span><span class="z-entity z-name z-type">a</span><span>,</span></span>
<span class="giallo-l"><span class="z-variable z-language">        Self</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">Base</span><span class="z-keyword z-operator">:</span><span> &#39;</span><span class="z-entity z-name z-type">a</span><span>,</span></span>
<span class="giallo-l"><span>    {</span></span>
<span class="giallo-l"><span class="z-storage z-type">        let</span><span class="z-variable"> base</span><span class="z-keyword z-operator z-assignment z-keyword z-operator"> =</span><span class="z-keyword"> unsafe</span><span> {</span><span class="z-entity z-name z-type"> Pin</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-function">into_inner_unchecked</span><span>(</span><span class="z-variable">base</span><span>)</span><span> }</span><span>;</span></span>
<span class="giallo-l"><span class="z-keyword z-operator">        &amp;</span><span class="z-storage z-storage z-modifier">mut</span><span class="z-variable"> base</span><span class="z-keyword z-operator">.</span><span>field</span></span>
<span class="giallo-l"><span>    }</span></span>
<span class="giallo-l"><span>}</span></span>
<span class="giallo-l"></span>
<span class="giallo-l"><span class="z-keyword">unsafe</span><span class="z-keyword"> impl</span><span class="z-entity z-name z-type"> PinnableField</span><span class="z-keyword z-control"> for</span><span class="z-entity z-name z-function"> field_of!</span><span>(</span><span class="z-entity z-name z-type">Struct</span><span>,</span><span class="z-variable"> other</span><span>)</span><span> {</span></span>
<span class="giallo-l"><span class="z-storage z-type">    type</span><span class="z-entity z-name z-type"> StructuralRefMut</span><span>&lt;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span>&gt;</span><span class="z-keyword z-operator z-assignment z-keyword z-operator"> =</span><span class="z-entity z-name z-type"> Pin</span><span>&lt;</span><span class="z-keyword z-operator">&amp;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span class="z-storage z-storage z-modifier"> mut</span><span class="z-entity z-name z-type"> u32</span><span>&gt;</span><span>;</span></span>
<span class="giallo-l"><span class="z-punctuation z-definition z-comment z-comment">    //</span><span class="z-comment z-line z-double-slash z-comment"> u32 is `Unpin`, so this isn&#39;t doing anything special, but it highlights the pattern.</span></span>
<span class="giallo-l"></span>
<span class="giallo-l"><span class="z-keyword">    fn</span><span class="z-entity z-name z-function"> project_mut</span><span>&lt;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span>&gt;</span><span>(</span><span class="z-variable">base</span><span class="z-keyword z-operator">:</span><span class="z-entity z-name z-type"> Pin</span><span>&lt;</span><span class="z-keyword z-operator">&amp;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span class="z-storage z-storage z-modifier"> mut</span><span class="z-variable z-language"> Self</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">Base</span><span>&gt;</span><span>)</span><span class="z-keyword z-operator"> -&gt;</span><span class="z-variable z-language"> Self</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">StructuralRefMut</span><span>&lt;</span><span>&#39;</span><span class="z-entity z-name z-type">a</span><span>&gt;</span></span>
<span class="giallo-l"><span class="z-keyword">    where</span></span>
<span class="giallo-l"><span class="z-variable z-language">        Self</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">Type</span><span class="z-keyword z-operator">:</span><span> &#39;</span><span class="z-entity z-name z-type">a</span><span>,</span></span>
<span class="giallo-l"><span class="z-variable z-language">        Self</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-type">Base</span><span class="z-keyword z-operator">:</span><span> &#39;</span><span class="z-entity z-name z-type">a</span><span>,</span></span>
<span class="giallo-l"><span>    {</span></span>
<span class="giallo-l"><span class="z-storage z-type">        let</span><span class="z-variable"> base</span><span class="z-keyword z-operator z-assignment z-keyword z-operator"> =</span><span class="z-keyword"> unsafe</span><span> {</span><span class="z-entity z-name z-type"> Pin</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-function">into_inner_unchecked</span><span>(</span><span class="z-variable">base</span><span>)</span><span> }</span><span>;</span></span>
<span class="giallo-l"><span class="z-keyword">        unsafe</span><span> {</span><span class="z-entity z-name z-type"> Pin</span><span class="z-keyword z-operator">::</span><span class="z-entity z-name z-function">new_unchecked</span><span>(</span><span class="z-keyword z-operator">&amp;</span><span class="z-storage z-storage z-modifier">mut</span><span class="z-variable"> base</span><span class="z-keyword z-operator">.</span><span>other</span><span>)</span><span> }</span></span>
<span class="giallo-l"><span>    }</span></span>
<span class="giallo-l"><span>}</span></span></code></pre>
<p>Now you can safely obtain a pinned mutable reference to <code>other</code> and a normal mutable reference to <code>field</code> by calling the <code>project_pinned</code> function and supplying the correct FRT.</p>
<p>(<a rel="external" href="https://play.rust-lang.org/?version=nightly&amp;mode=debug&amp;edition=2024&amp;gist=5b9494bd8f88aa4adf054f70abe16d9d">playground link</a>)</p>
</blockquote>
</li>
<li>
<p><strong><a rel="external" href="https://github.com/BennoLossin">Benno Lossin</a></strong> — <a rel="external" href="https://github.com/rust-lang/rust-project-goals/issues/390#issuecomment-4099385451">comment from 2026-03-20</a></p>
<blockquote>
<h3 id="plan-for-2026"><a class="anchor" href="#plan-for-2026" aria-hidden="true"></a>
Plan for 2026</h3>
<p>We have an updated plan for this goal in 2026 consisting of three major steps:</p>
<ul>
<li><code>a-mir-formality</code>,</li>
<li>Implementation,</li>
<li>Experimentation.</li>
</ul>
<p>Some of their subtasks depend on other subtasks for other steps. You can find the details in the <a rel="external" href="https://github.com/rust-lang/rust/issues/145383">updated tracking issue</a>. Here is a short rundown of each:</p>
<p><strong><code>a-mir-formality</code>:</strong> we want to create a formal model of the borrow checker changes we're proposing to ensure correctness. We also want to create a document explaining our model in a more human-friendly language. To really get started with this, we're blocked on the new expression based syntax in development by Niko.</p>
<p><strong>Implementation:</strong> at the same time, we can start implementing more parts in the compiler. We will continue to improve FRTs, while keeping in mind that we might remove them if they end up being unnecessary. They still pose for a useful feature, but they might be orthogonal to field projections. We plan to make small and incremental changes, starting with library additions. We also want to begin exploring potential desugarings, for which we will add some manual and low level macros. When we have that figured out, we can fast-track syntax changes. When we have a sufficiently mature formal model of the borrow checker integration, we will port it to the compiler. After further evaluation, we can think about removing the <code>incomplete_feature</code> flag.</p>
<p><strong>Experimentation:</strong> after each compiler or standard library change, we look to several projects to stress-test our ideas in real code. I will take care of experimentation in the Linux kernel, while <a rel="external" href="https://github.com/tmandry">Tyler Mandry</a> will be taking a look at testing field projections with <code>crubit</code>. <a rel="external" href="https://github.com/joshtriplett">Josh Triplett</a> also has expressed eagerness of introducing them in the standard library; I will coordinate with him and the rest of t-libs-api to experiment there.</p>
</blockquote>
</li>
<li>
<p><strong><a rel="external" href="https://github.com/BennoLossin">Benno Lossin</a></strong> — <a rel="external" href="https://github.com/rust-lang/rust-project-goals/issues/390#issuecomment-4178384770">comment from 2026-04-02</a></p>
<blockquote>
<p>Yesterday, we held a t-lang design meeting on our current approach. <a rel="external" href="https://github.com/Nadrieril">Nadrieril</a> and I authored a <a rel="external" href="https://hackmd.io/H5d2-83ER2ymNPZVIWCYWg">design document</a> with the feedback of <a rel="external" href="https://github.com/tmandry">Tyler Mandry</a>, <a rel="external" href="https://github.com/dingxiangfei2009">Ding Xiang Fei</a>, <a rel="external" href="https://github.com/Darksonn">Alice Ryhl</a>, and <a rel="external" href="https://github.com/nbdd0121">Gary Guo</a>. In this document, we provided the motivation for this feature, what the look and feel of a solution fitting into the existing features of Rust is, and a comprehensive + compact introduction to our current approach based on virtual places.</p>
<p>The general reception was extremely positive. To give some concrete quotes from the meeting:</p>
<ul>
<li>Josh:
<blockquote>
<p>I adore this! I love how orthogonal it is, and how impactful and universal it is. I anticipate this becoming a beloved, <em>pervasive</em> feature of Rust.</p>
<p>Places and projection seem important enough to me that they're worth giving one of our precious remaining ASCII sigils to, and <code>@</code> is nicely evocative of a place (something is <em>at</em> a place). So to the extent the final syntax benefits from a sigil, :+1: for giving this <code>@</code>. (See some feedback below on the details, though.)</p>
</blockquote>
</li>
<li>TC:
<blockquote>
<p>Love it. High concept. As I said in the last meeting:</p>
<blockquote>
<p>I particularly like language features that reduce the need for library surface area, and this is one of those.</p>
</blockquote>
<p>There are, of course, many details to resolve and understand further, e.g., with respect to migration issues, interaction with <code>const</code>, <code>async</code>, and other effect-like things, etc. I'm looking forward to seeing the formalization work.</p>
</blockquote>
</li>
<li>tmandry:
<blockquote>
<p>What I love about this direction is how effectively it builds on what Rust already has. I love to see designs that reinforce our existing concepts while pushing them in directions that make them more expressive.</p>
</blockquote>
</li>
<li>Jack:
<blockquote>
<p>Whoo boy. This is great. There's so much here that I'm not exactly sure where to begin and what to comment on. I think this is the type of thing that we will only <em>really</em> be able to figure out the nitty gritty details and ergonomics only after some amount of experimentation.</p>
</blockquote>
</li>
</ul>
<p>There are a few takeaways from this meeting:</p>
<ul>
<li>Mark <a rel="external" href="https://hackmd.io/H5d2-83ER2ymNPZVIWCYWg?view#From-author-Concerns-about-moving-forward">raised the concern</a> that t-libs should be more involved in reviewing the experimental traits that we intend to add. Ensuring that we don't accidentally stabilize or expose some behavior, have sufficient documentation on our experimental traits, and that t-libs is in the loop of this feature in general.
<ul>
<li>Mark offered to review PRs and I will be tagging him in those.</li>
</ul>
</li>
<li>Jack <a rel="external" href="https://hackmd.io/H5d2-83ER2ymNPZVIWCYWg?view#Jack">raised the concern</a> that increasing the cognitive load for the 95% use-case should be avoided. Making the right choice between <code>@</code> and <code>&amp;</code> might be challenging for users.
<ul>
<li>We <a rel="external" href="https://hackmd.io/H5d2-83ER2ymNPZVIWCYWg?view#From-author-Ergonomics-of-raw-pointers">discussed this point more in the meeting</a> and concluded with that we need to do some experimentation, possibly utilizing the user research team. We will of course keep this in mind and revisit it later when we have a partially working implementation.</li>
</ul>
</li>
<li>TC requested that we publish our fine-grained design axioms, essentially the list of things we go through when considering a modification of our proposal.
<ul>
<li>I will write an update on this issue explaining exactly those.</li>
</ul>
</li>
</ul>
<p>Aside from the concerns and directly actionable items, the meeting also covered design questions/comments that we want to take a look at in the coming weeks/months:</p>
<ul>
<li><a rel="external" href="https