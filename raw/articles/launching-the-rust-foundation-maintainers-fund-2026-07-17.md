---
source_url: https://blog.rust-lang.org/2026/06/02/launching-the-rust-foundation-maintainers-fund/
ingested: 2026-07-17
sha256: ea82222c16ac3138e98fd5a0907ef89596bc4db8e5c8e390d8f63de3251d3983
blog_source: Rust Blog
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Launching the Rust Foundation Maintainers Fund | Rust Blog</title>
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Empowering everyone to build reliable and efficient software.">
     <!-- Twitter card -->
     <meta name="twitter:card" content="summary">
     <meta name="twitter:site" content="@rustlang">
     <meta name="twitter:creator" content="@rustlang">
     <meta name="twitter:title" content="Launching the Rust Foundation Maintainers Fund | Rust Blog">
     <meta name="twitter:description" content="Empowering everyone to build reliable and efficient software.">
    <meta name="twitter:image" content="https://www.rust-lang.org/static/images/rust-social.jpg">
    
    <!-- Facebook OpenGraph -->
    <meta property="og:title" content="Launching the Rust Foundation Maintainers Fund | Rust Blog" />
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
    </nav><section id="Launching the Rust Foundation Maintainers Fund" class="white">
  <div class="w-100 mw-none ph3 mw8-m mw8-l center f3">
    <header>
      <h2>Launching the Rust Foundation Maintainers Fund</h2>
      <div class="highlight mt2 mb3"></div>
    </header>

    <div class="publish-date-author">June 2, 2026 &middot; Funding team
     on behalf of <a href="https://www.rust-lang.org/governance/teams/leadership-council">Leadership Council</a> 
    </div>

    <div class="post">
      <blockquote>
<p>If you want to financially support the development of Rust, please consider <a rel="external" href="https://github.com/sponsors/rustfoundation">donating</a> to the Rust Foundation Maintainers Fund.</p>
</blockquote>
<p>A few months ago, the Rust Foundation announced the <a rel="external" href="https://rustfoundation.org/media/announcing-the-rust-foundation-maintainers-fund/">Rust Foundation Maintainers Fund</a> (RFMF). Since then, the Rust Project has been closely cooperating with the Rust Foundation to determine how exactly this fund will be used to support Rust maintainers. This resulted in the acceptance of <a rel="external" href="https://rust-lang.github.io/rfcs/3931-rfmf-rust-foundation-maintainer-fund.html">RFC #3931</a>, which established the <a rel="external" href="https://rust-lang.org/governance/teams/launching-pad/#team-funding">Funding team</a> and the <a rel="external" href="https://rust-lang.github.io/rfcs/3931-rfmf-rust-foundation-maintainer-fund.html#expectations-placed-on-maintainers-in-residence">Maintainer in Residence</a> program.</p>
<p>The primary goal of the Funding team is to ensure that maintainers who work on Rust and its toolchain will be properly supported. We will talk to Rust Project members to figure out their funding situation, meet Rust team leads to learn about their maintenance needs, approach companies to find opportunities for them to invest into Rust by supporting Rust maintainers, coordinate various funding efforts and ensure that the beneficial effects of funded maintenance are visibly promoted, with the help of the <a rel="external" href="https://rust-lang.org/governance/teams/launching-pad/#team-content">Content team</a>.</p>
<p><a rel="external" href="https://rust-lang.github.io/rfcs/3931-rfmf-rust-foundation-maintainer-fund.html#expectations-placed-on-maintainers-in-residence">Maintainer in Residence</a> is a new program dedicated to financially supporting existing Rust Project maintainers<sup class="footnote-reference" id="fr-dir-1"><a href="#fn-dir">1</a></sup>. Each Maintainer in Residence will be funded to <a rel="external" href="https://blog.rust-lang.org/inside-rust/2026/01/12/what-is-maintenance-anyway/">maintain</a> one or more critical parts of Rust, such as the compiler, the standard library, Cargo, Clippy or one of many other projects that the Rust Project develops and maintains. The funded work will include activities such as performing large-scale refactorings, code reviews, unblocking new features, issue triaging, mentoring other contributors and more, and will be split between priorities guided by the teams they are supporting and priorities of their own choosing within the Project. Where applicable, Maintainers in Residence are also encouraged to propose, champion, and drive forward <a rel="external" href="https://rust-lang.github.io/rust-project-goals/">Rust Project Goals</a>.</p>
<p>The goal of this program is to provide stable and long-term funding so that maintainers can focus on important work that ensures the long-term health of Rust. The funding team will select Maintainers in Residence based on funding availability and maintenance needs within the Rust Project, and help ensure that they are successful. We expect that this will usually be a (near) full-time position, but that will depend on the nature of the work and the area of maintenance.</p>
<p>This program extends our existing support for Rust maintainers, such as the <a rel="external" href="https://blog.rust-lang.org/inside-rust/2026/04/09/program-management-update-2026-03/">program management program</a> and the <a rel="external" href="https://blog.rust-lang.org/inside-rust/2025/06/05/a-glance-at-the-team-compiler-operations">compiler-ops program</a>. An important development is that we now have a centralized <a rel="external" href="https://github.com/sponsors/rustfoundation">mechanism</a> for gathering donations from both individuals and companies, and a dedicated team that will help direct those funds to specific maintainers. You can find more details about the funding team and the Maintainer in Residence program in the <a rel="external" href="https://rust-lang.github.io/rfcs/3931-rfmf-rust-foundation-maintainer-fund.html">RFC</a>.</p>
<p>We expect to hire the first Maintainer in Residence in the upcoming months and announce it on this blog, so stay tuned!</p>
<h2 id="how-to-contribute-funds"><a class="anchor" href="#how-to-contribute-funds" aria-hidden="true"></a>
How to contribute funds</h2>
<p>If you are an individual who wants to help Rust succeed and thrive, you can donate to the RFMF through <a rel="external" href="https://github.com/sponsors/rustfoundation">GitHub Sponsors</a><sup class="footnote-reference" id="fr-sponsors-1"><a href="#fn-sponsors">2</a></sup>. Companies who would like to invest in better maintenance of Rust can also donate through GitHub Sponsors or they can contact the Rust Foundation <a href="mailto:contact@rustfoundation.org">directly</a>.</p>
<p>The important thing is that <strong>all proceeds from this fund will be directly used to support Rust Project maintainers</strong>. We currently expect that to happen primarily through the Maintainer in Residence program, but it can also be done in the form of smaller-scale grants or other mechanisms, as determined by the Funding team. We will figure this out on the go, as this is also quite new for us.</p>
<p>We really appreciate each donation, however small, because with more money we can hire more maintainers to ensure that we can continue to develop Rust and that important improvements are not blocked on maintenance tasks. This is especially important at this time, where Rust is starting to get used more and more in the industry in various application areas, which increases the need for sustained maintenance. The importance of multiple funding sources is underscored by an unfortunate trend we currently observe, where key Rust maintainers are losing their funding for Rust work due to budget shifts. The Rust Foundation Maintainers Fund is designed to provide stable funding for Rust maintainers that is less dependent on sudden shifts in the job market and the IT industry.</p>
<p>As with most things, there is no one-size-fits-all solution, so there are multiple ways to support Rust financially. The <a rel="external" href="https://rustnl.org/maintainers">RustNL Maintainers Team</a> recently hired several Rust Project maintainers. Previously, we <a rel="external" href="https://blog.rust-lang.org/2025/12/08/making-it-easier-to-sponsor-rust-contributors/">wrote</a> about how you can support specific individuals working on Rust. And there are also Rust Project Goals <a rel="external" href="https://rust-lang.github.io/rust-project-goals/2026/funding.html">in search of funding</a>. We welcome all efforts that can help support Rust Project maintainers, who often do work that is near invisible and thankless, while at the same time incredibly important and necessary, on a volunteer basis.</p>
<p>Thank you for considering sponsoring the development and maintenance of Rust! You can find more information about funding Rust on our <a rel="external" href="https://rust-lang.org/funding/">Funding page</a>.</p>
<section class="footnotes">
<ol class="footnotes-list">
<li id="fn-dir">
<p>This program was inspired by the <a rel="external" href="https://www.python.org/psf/developersinresidence/">Developer in Residence</a> concept used by the Python Software Foundation (PSF), with which we led several helpful discussions. Thank you, PSF! <a href="#fr-dir-1">↩</a></p>
</li>
<li id="fn-sponsors">
<p>Note that the fact that GitHub Sponsors is currently enabled on the <code>rustfoundation</code> GitHub organization, and not the <code>rust-lang</code> organization, is an implementation detail that might change in the future. All donations raised on this Sponsors page will be routed to the Rust Foundation Maintainers Fund and will be spent on directly supporting Rust Project maintainers. <a href="#fr-sponsors-1">↩</a></p>
</li>
</ol>
</section>

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
          <a href="https://github.com/rust-lang/blog.rust-lang.org/edit/main/content/launching-the-rust-foundation-maintainers-fund.md" target="_blank" rel="noopener">Send a fix here</a>!
        </div>
      </div>
    </footer>
  </body>
</html>
