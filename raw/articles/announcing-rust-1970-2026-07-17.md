---
source_url: https://blog.rust-lang.org/2026/07/09/Rust-1.97.0/
ingested: 2026-07-17
sha256: 17cafa268e4c72d5d4946fe3af779eefca5736ece7600cb9db08adf47327a166
blog_source: Rust Blog
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Announcing Rust 1.97.0 | Rust Blog</title>
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Empowering everyone to build reliable and efficient software.">
     <!-- Twitter card -->
     <meta name="twitter:card" content="summary">
     <meta name="twitter:site" content="@rustlang">
     <meta name="twitter:creator" content="@rustlang">
     <meta name="twitter:title" content="Announcing Rust 1.97.0 | Rust Blog">
     <meta name="twitter:description" content="Empowering everyone to build reliable and efficient software.">
    <meta name="twitter:image" content="https://www.rust-lang.org/static/images/rust-social.jpg">
    
    <!-- Facebook OpenGraph -->
    <meta property="og:title" content="Announcing Rust 1.97.0 | Rust Blog" />
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
    </nav><section id="Announcing Rust 1.97.0" class="white">
  <div class="w-100 mw-none ph3 mw8-m mw8-l center f3">
    <header>
      <h2>Announcing Rust 1.97.0</h2>
      <div class="highlight mt2 mb3"></div>
    </header>

    <div class="publish-date-author">July 9, 2026 &middot; The Rust Release Team
    
    </div>

    <div class="post">
      <p>The Rust team is happy to announce a new version of Rust, 1.97.0. Rust is a programming language empowering everyone to build reliable and efficient software.</p>
<p>If you have a previous version of Rust installed via <code>rustup</code>, you can get 1.97.0 with:</p>
<pre class="giallo z-code"><code data-lang="shellsession"><span class="giallo-l"><span>$</span><span> rustup update stable</span></span></code></pre>
<p>If you don't have it already, you can get <a rel="external" href="https://www.rust-lang.org/install.html"><code>rustup</code></a> from the appropriate page on our website, and check out the <a rel="external" href="https://doc.rust-lang.org/stable/releases.html#version-1970-2026-07-09">detailed release notes for 1.97.0</a>.</p>
<p>If you'd like to help us out by testing future releases, you might consider updating locally to use the beta channel (<code>rustup default beta</code>) or the nightly channel (<code>rustup default nightly</code>). Please <a rel="external" href="https://github.com/rust-lang/rust/issues/new/choose">report</a> any bugs you might come across!</p>
<h2 id="what-s-in-1-97-0-stable"><a class="anchor" href="#what-s-in-1-97-0-stable" aria-hidden="true"></a>
What's in 1.97.0 stable</h2>
<h3 id="symbol-mangling-v0-enabled-by-default"><a class="anchor" href="#symbol-mangling-v0-enabled-by-default" aria-hidden="true"></a>
Symbol mangling v0 enabled by default</h3>
<p>When Rust is compiled into object files and binaries, each item (functions,
statics, etc) must have a globally unique "symbol" identifying it. To avoid
conflicts when linking together different Rust programs, Rust mangles the
original name of items to include additional context such as the module path,
defining crate, generics, and more. Historically, this mangling was based on
the <a rel="external" href="https://refspecs.linuxbase.org/cxxabi-1.86.html#mangling">Itanium ABI</a>,
also (sometimes) used by C++.</p>
<p>The new mangling scheme resolves a number of drawbacks from the previous one:</p>
<ul>
<li>Generic parameter instantiations preserve their values, rather than being tracked solely behind a hash</li>
<li>Inconsistencies: not all parts used the Itanium ABI, meaning that custom demangling was still necessary</li>
</ul>
<p>Since Rust 1.59, the compiler has supported opting into a Rust-specific
mangling scheme via <code>-Csymbol-mangling-version=v0</code>. Since November 2025, this
scheme has been enabled by default on nightly, and 1.97 is now enabling it on
stable Rust. The legacy mangling scheme can only be enabled on nightly, and the
current plan is to fully remove it.</p>
<p>See the previous <a rel="external" href="https://blog.rust-lang.org/2025/11/20/switching-to-v0-mangling-on-nightly/">blog post</a> for more details.</p>
<h3 id="cargo-support-for-denying-warnings"><a class="anchor" href="#cargo-support-for-denying-warnings" aria-hidden="true"></a>
Cargo support for denying warnings</h3>
<p>It's common practice to deny warnings in CI. Historically, doing so is
typically done through <code>RUSTFLAGS=-Dwarnings</code>. With Rust 1.97, Cargo controls
how warnings interact with build success: either silencing them (via <code>allow</code>
level), rendering without failing (default, <code>warn</code>), or denying them (via <code>deny</code>).</p>
<p>As a  result of Cargo configuration determining the behavior, using this
feature doesn't invalidate the underlying build cache, meaning that it's easy
to temporarily opt-in. For example, if warnings are adding unwanted noise while
working through fixing errors after a refactor, you can run
<code>CARGO_BUILD_WARNINGS=allow cargo check</code>, temporarily silencing them.</p>
<p>In CI, jobs can instead set <code>CARGO_BUILD_WARNINGS=deny</code> to deny warnings. This
can be combined with <code>--keep-going</code> to collect all errors and warnings rather
than stopping on the first failing package.</p>
<p>See the <a rel="external" href="https://doc.rust-lang.org/cargo/reference/config.html#buildwarnings">documentation</a> for more details.</p>
<h3 id="linker-output-no-longer-hidden-by-default"><a class="anchor" href="#linker-output-no-longer-hidden-by-default" aria-hidden="true"></a>
Linker output no longer hidden by default</h3>
<p>rustc invokes a linker on behalf of users. Historically, rustc has silenced
linker output by default if the link completes successfully. This can mask real
problems, though, so in Rust 1.97 we are enabling linker messages by default.
These are emitted as a warning lint, for example:</p>
<pre class="giallo z-code"><code data-lang="plain"><span class="giallo-l"><span>warning: linker stderr: ignoring deprecated linker optimization setting &#39;1&#39;</span></span>
<span class="giallo-l"><span>  |</span></span>
<span class="giallo-l"><span>  = note: `#[warn(linker_messages)]` on by default</span></span></code></pre>
<p>Common linker messages that have been diagnosed as false positives or intentional behavior
are filtered out by rustc. Several defects have already been fixed as a result
of no longer hiding this output on nightly.</p>
<p>Note that currently, <code>linker_messages</code> is a special lint that is <em>not</em> affected
by the <code>warnings</code> lint group. This is intentional as rustc generally doesn't
control linker output as precisely, and it's not uncommon for output to only
appear on some platforms. If you are seeing what you think is a false positive
output from the linker, please <a rel="external" href="https://github.com/rust-lang/rust/issues/new/choose">file an issue</a>.</p>
<p>To silence the warning in the mean time, you can configure the lint level to
allow. This can be done through <code>Cargo.toml</code> by adding a <a rel="external" href="https://doc.rust-lang.org/nightly/cargo/reference/manifest.html#the-lints-section">lints section</a> like this:</p>
<pre class="giallo z-code"><code data-lang="toml"><span class="giallo-l"><span>[</span><span>lints</span><span>.</span><span>rust</span><span>]</span></span>
<span class="giallo-l"><span class="z-variable">linker_messages</span><span> =</span><span class="z-punctuation z-definition z-string z-string"> &quot;</span><span class="z-string z-quoted z-string">allow</span><span class="z-punctuation z-definition z-string z-string">&quot;</span></span></code></pre><h3 id="stabilized-apis"><a class="anchor" href="#stabilized-apis" aria-hidden="true"></a>
Stabilized APIs</h3>
<ul>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/iter/struct.RepeatN.html#impl-Default-for-RepeatN%3CA%3E"><code>Default for RepeatN</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/ffi/struct.FromBytesUntilNulError.html#impl-Copy-for-FromBytesUntilNulError"><code>Copy for ffi::FromBytesUntilNulError</code></a></li>
<li><a rel="external" href="https://github.com/rust-lang/rust/pull/154003"><code>Send for std::fs::File</code> on UEFI</a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/primitive.u32.html#method.isolate_highest_one"><code>&lt;{integer}&gt;::isolate_highest_one</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/primitive.u32.html#method.isolate_lowest_one"><code>&lt;{integer}&gt;::isolate_lowest_one</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/primitive.u32.html#method.highest_one"><code>&lt;{integer}&gt;::highest_one</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/primitive.u32.html#method.lowest_one"><code>&lt;{integer}&gt;::lowest_one</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/primitive.u32.html#method.bit_width"><code>&lt;{uN}&gt;::bit_width</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/num/struct.NonZero.html#method.isolate_highest_one"><code>NonZero&lt;{integer}&gt;::isolate_highest_one</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/num/struct.NonZero.html#method.isolate_lowest_one"><code>NonZero&lt;{integer}&gt;::isolate_lowest_one</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/num/struct.NonZero.html#method.highest_one"><code>NonZero&lt;{integer}&gt;::highest_one</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/num/struct.NonZero.html#method.lowest_one"><code>NonZero&lt;{integer}&gt;::lowest_one</code></a></li>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/num/struct.NonZero.html#method.bit_width"><code>NonZero&lt;{uN}&gt;::bit_width</code></a></li>
</ul>
<p>These previously stable APIs are now stable in const contexts:</p>
<ul>
<li><a rel="external" href="https://doc.rust-lang.org/stable/std/primitive.char.html#method.is_control"><code>char::is_control</code></a></li>
</ul>
<h3 id="other-changes"><a class="anchor" href="#other-changes" aria-hidden="true"></a>
Other changes</h3>
<p>Check out everything that changed in <a rel="external" href="https://github.com/rust-lang/rust/releases/tag/1.97.0">Rust</a>, <a rel="external" href="https://doc.rust-lang.org/nightly/cargo/CHANGELOG.html#cargo-197-2026-07-09">Cargo</a>, and <a rel="external" href="https://github.com/rust-lang/rust-clippy/blob/master/CHANGELOG.md#rust-197">Clippy</a>.</p>
<h2 id="contributors-to-1-97-0"><a class="anchor" href="#contributors-to-1-97-0" aria-hidden="true"></a>
Contributors to 1.97.0</h2>
<p>Many people came together to create Rust 1.97.0. We couldn't have done it without all of you. <a rel="external" href="https://thanks.rust-lang.org/rust/1.97.0/">Thanks!</a></p>

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
          <a href="https://github.com/rust-lang/blog.rust-lang.org/edit/main/content/Rust-1.97.0.md" target="_blank" rel="noopener">Send a fix here</a>!
        </div>
      </div>
    </footer>
  </body>
</html>
