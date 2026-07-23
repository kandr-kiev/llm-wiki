---
source_url: https://dev.to/dr_data/agentscaffold-memory-peer-review-and-continuous-improvement-for-ai-coding-agents-43fb
ingested: 2026-07-23
sha256: 9f46793d1f0bc8bb5f064596e669f8fef4cf6e8c3ec42b593a11b40e4593af16
blog_source: Dev Community
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>AgentScaffold: Memory, Peer Review, and Continuous Improvement for AI Coding Agents - DEV Community</title>
    
    <link rel="preload" href="/reactions?article_id=4202748" as="fetch" crossorigin="same-origin">
    <link rel="canonical" href="https://dev.to/dr_data/agentscaffold-memory-peer-review-and-continuous-improvement-for-ai-coding-agents-43fb" />
    <meta name="description" content="A knowledge graph and governed plan lifecycle for Cursor, Claude Code, and any MCP agent — built by a data scientist who spent two decades keeping production systems and ML pipelines from drifting quietly wrong. Tagged with python, devtools, ai, agentskills.">
    <meta name="keywords" content="python, devtools, ai, agentskills, software, coding, development, engineering, inclusive, community">

    <meta property="og:type" content="article" />
    <meta property="og:url" content="https://dev.to/dr_data/agentscaffold-memory-peer-review-and-continuous-improvement-for-ai-coding-agents-43fb" />
    <meta property="og:title" content="AgentScaffold: Memory, Peer Review, and Continuous Improvement for AI Coding Agents" />
    <meta property="og:description" content="A knowledge graph and governed plan lifecycle for Cursor, Claude Code, and any MCP agent — built by a data scientist who spent two decades keeping production systems and ML pipelines from drifting quietly wrong." />
    <meta property="og:site_name" content="DEV Community" />
    <meta name="twitter:site" content="@thepracticaldev">
    <meta name="twitter:creator" content="@">
    <meta name="author-trust" content="0">
    <meta name="twitter:title" content="AgentScaffold: Memory, Peer Review, and Continuous Improvement for AI Coding Agents">
    <meta name="twitter:description" content="A knowledge graph and governed plan lifecycle for Cursor, Claude Code, and any MCP agent — built by a data scientist who spent two decades keeping production systems and ML pipelines from drifting quietly wrong.">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:widgets:new-embed-design" content="on">
    <meta name="robots" content="max-snippet:-1, max-image-preview:large, max-video-preview:-1">
      <meta property="og:image" content="https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F61aneq87hz3zabi50agk.png" />
      <meta name="twitter:image:src" content="https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F61aneq87hz3zabi50agk.png">

      <meta name="last-updated" content="2026-07-23 06:02:09 UTC">
      <meta name="user-signed-in" content="false">
      <meta name="head-cached-at" content="1784786529">
      <meta name="environment" content="production">
      <link rel="stylesheet" href="https://assets.dev.to/assets/minimal-b74fc990bceac4211a1cd56dba292c86ef404899478f400db08e0ee6bb2fe52f.css" media="all" id="main-minimal-stylesheet" />
<link rel="stylesheet" href="https://assets.dev.to/assets/views-53fd5c62260337fdcc0cd283567529e2d0145374447ef4eee282979766a5d6d3.css" media="all" id="main-views-stylesheet" />
<link rel="stylesheet" href="https://assets.dev.to/assets/crayons-cd641458c515ed65f655e4222ec89a7e0394593a544555029c4b64da2bc7c722.css" media="all" id="main-crayons-stylesheet" />

      <script src="https://assets.dev.to/assets/base-21243ecb87ec81f8bff00e691ca88aa1ea79183b8e90e9111f1970a832afea13.js" defer="defer"></script>
<script src="https://assets.dev.to/assets/application-9ee88e198a0d2b64238c8557b5225d20e2c18ff5b877f1159ee5a31f6e3174f9.js" defer="defer"></script>
<script src="https://assets.dev.to/assets/baseInitializers-a14e91b5761bba84afd44af9613781f2308746c8b242cf84b4f4338f4328c5d5.js" defer="defer"></script>
<script src="https://assets.dev.to/assets/baseTracking-cb478131fb1b41bc25e80ebcee996318777e081c9aa87367fabc1c118461a2d3.js" defer="defer"></script>
<script src="https://assets.dev.to/assets/followButtons-e3595664847e9f43945a9b8a0445b32cda9a149f1f169f78b8fcc7714ccab45a.js" defer="defer"></script>
<script src="https://assets.dev.to/assets/eventSignupButtons-a2b5da712a1b8eeb0eda4d63fafc54973138a70b88503a2163806c27fc1e4c39.js" defer="defer"></script>

        <meta name="search-script" content="https://assets.dev.to/assets/Search-a570c3428c9b6cb070d3f18817c957f80d0dbdf36a0f4a1d6e23a990305fbc12.js">
      <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
      <link rel="icon" type="image/x-icon" href="https://media2.dev.to/dynamic/image/width=32,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png" />
      <link rel="apple-touch-icon" href="https://media2.dev.to/dynamic/image/width=180,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png">
      <link rel="apple-touch-icon" sizes="152x152" href="https://media2.dev.to/dynamic/image/width=152,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png">
      <link rel="apple-touch-icon" sizes="180x180" href="https://media2.dev.to/dynamic/image/width=180,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png">
      <link rel="apple-touch-icon" sizes="167x167" href="https://media2.dev.to/dynamic/image/width=167,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png">
      <link href="https://media2.dev.to/dynamic/image/width=192,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png" rel="icon" sizes="192x192" />
      <link href="https://media2.dev.to/dynamic/image/width=128,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png" rel="icon" sizes="128x128" />
      <meta name="apple-mobile-web-app-title" content="dev.to">
      <meta name="application-name" content="dev.to">
      <meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
      <meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">
      <link rel="search" href="https://dev.to/open-search.xml" type="application/opensearchdescription+xml" title="DEV Community" />

      <meta property="forem:name" content="DEV Community" />
      <meta property="forem:logo" content="https://media2.dev.to/dynamic/image/width=512,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png" />
      <meta property="forem:domain" content="dev.to" />
    <style>
body:has(.pageslug-aie) #topbar {
    display: none !important;
}

@media screen and (max-width: 768px) and (pointer: coarse) {
  /* Target WebKit/Blink specific behaviors */
  @supports (-webkit-app-region: none) {
    body:has(.pageslug-aie) .dc-page {
      padding-top: 56px !important;
    }
  }
}

body:not(.hidden-shell) .pageslug-aie {
    margin-top: -56px !important;
}

/* ==========================================================================
   THE 418 CHALLENGE: THEME-AWARE RETRO EDITION
   ========================================================================== */
.articletag-418challenge {
  font-family: "Comic Sans MS", "Chalkboard SE", "Marker Felt", sans-serif !important;
  cursor: crosshair !important;
}

/* Destroy modern rounded corners and add brutal borders */
.articletag-418challenge .crayons-card,
.articletag-418challenge .crayons-article__main,
.articletag-418challenge .crayons-article__header {
  border-radius: 0 !important;
  margin-bottom: 2rem !important;
}

/* Typography specifics */
.articletag-418challenge h1,
.articletag-418challenge h2,
.articletag-418challenge h3 {
  text-transform: uppercase !important;
}

/* Fake <marquee> effect for the main article title */
.articletag-418challenge h1.fs-3xl {
  animation: retro-slide 5s linear infinite alternate;
  overflow: visible;
}

/* Spin those avatars */
.articletag-418challenge .crayons-article__header__meta img {
  border-radius: 0 !important; 
  animation: retro-spin 5s linear infinite;
}

/* Obnoxious tags */
.articletag-418challenge .crayons-tag {
  border-radius: 0 !important;
  font-weight: 900 !important;
  transform: rotate(-3deg);
  display: inline-block;
}
.articletag-418challenge .crayons-tag:nth-child(even) {
  transform: rotate(3deg);
}

/* --------------------------------------------------------------------------
   2. LIGHT THEME (Windows 95 / Office 97 Vibes)
   -------------------------------------------------------------------------- */
body:not(.dark-theme) .articletag-418challenge {
  background-color: #008080 !important; /* Win95 Teal Desktop */
}

body:not(.dark-theme) .articletag-418challenge .crayons-card,
body:not(.dark-theme) .articletag-418challenge .crayons-article__main,
body:not(.dark-theme) .articletag-418challenge .crayons-article__header {
  background-color: #c0c0c0 !important; /* Classic dialog gray */
  color: #000000 !important;
  border: 4px outset #ffffff !important;
  box-shadow: 8px 8px 0px #000000 !important;
}

body:not(.dark-theme) .articletag-418challenge h1,
body:not(.dark-theme) .articletag-418challenge h2,
body:not(.dark-theme) .articletag-418challenge h3 {
  color: #ff0000 !important;
  text-shadow: 2px 2px 0px #ffff00 !important;
  border-bottom: 3px dashed #0000ff !important;
}

body:not(.dark-theme) .articletag-418challenge a,
body:not(.dark-theme) .articletag-418challenge .crayons-link {
  color: #0000ff !important; /* Standard unvisited blue */
  text-decoration: underline !important;
  font-weight: bold !important;
}

body:not(.dark-theme) .articletag-418challenge a:hover,
body:not(.dark-theme) .articletag-418challenge .crayons-link:hover {
  background-color: #ffff00 !important;
  color: #ff0000 !important;
}

body:not(.dark-theme) .articletag-418challenge .crayons-tag {
  background: #ffff00 !important;
  color: #ff0000 !important;
  border: 2px dotted #0000ff !important;
}

/* --------------------------------------------------------------------------
   3. DARK THEME (1999 Hacker / Deep GeoCities Vibes)
   -------------------------------------------------------------------------- */
body.dark-theme .articletag-418challenge {
  background-color: #000000 !important;
  /* Dumb CSS: A scrolling, eye-bleeding neon green hacker grid with CRT scanlines */
  background-image: 
    linear-gradient(transparent 50%, rgba(0, 255, 0, 0.25) 50%), 
    linear-gradient(90deg, rgba(0, 255, 0, 0.5) 1px, transparent 1px), 
    linear-gradient(rgba(0, 255, 0, 0.5) 1px, transparent 1px) !important;
  background-size: 100% 4px, 20px 20px, 20px 20px !important;
  animation: retro-pan 60s linear infinite !important;
}

body.dark-theme .articletag-418challenge .crayons-card,
body.dark-theme .articletag-418challenge .crayons-article__main,
body.dark-theme .articletag-418challenge .crayons-article__header {
  background-color: #111111 !important;
  color: #00ff00 !important; /* Terminal Green */
  border: 4px outset #555555 !important;
  box-shadow: 8px 8px 0px #ff00ff !important; /* Hot pink shadow */
}

body.dark-theme .articletag-418challenge h1,
body.dark-theme .articletag-418challenge h2,
body.dark-theme .articletag-418challenge h3 {
  color: #ff00ff !important; /* Magenta headers */
  text-shadow: 2px 2px 0px #00ffff !important; /* Cyan shadow */
  border-bottom: 3px dashed #00ff00 !important;
}

body.dark-theme .articletag-418challenge a,
body.dark-theme .articletag-418challenge .crayons-link {
  color: #00ffff !important; /* Cyan links */
  text-decoration: underline !important;
  font-weight: bold !important;
}

body.dark-theme .articletag-418challenge a:hover,
body.dark-theme .articletag-418challenge .crayons-link:hover {
  background-color: #ff00ff !important;
  color: #ffffff !important;
}

body.dark-theme .articletag-418challenge .crayons-tag {
  background: #000000 !important;
  color: #00ff00 !important;
  border: 2px dotted #ff00ff !important;
}

/* --------------------------------------------------------------------------
   4. ANIMATIONS
   -------------------------------------------------------------------------- */
@keyframes retro-spin {
  100% { transform: rotate(360deg); }
}

@keyframes retro-slide {
  0% { transform: translateX(-2%); }
  100% { transform: translateX(2%); }
}

@keyframes retro-pan {
  0% { background-position: 0 0, 0 0, 0 0; }
  /* Numbers must be multiples of the background-size (4px and 20px) to loop perfectly */
  100% { background-position: 0 100px, 40px 40px, 40px 40px; }
}

/* --------------------------------------------------------------------------
   5. BONUS: CAUTION TAPE REACTION BAR
   -------------------------------------------------------------------------- */
.articletag-418challenge .crayons-article-actions {
  background: repeating-linear-gradient(
    45deg,
    #ffff00,
    #ffff00 10px,
    #000000 10px,
    #000000 20px
  ) !important;
  border: 4px solid #ff0000 !important;
  border-radius: 0 !important;
}

.articletag-418challenge .crayons-article-actions button {
  background:black;
  color: #ff00ff !important;
}

.articletag-418challenge .crayons-article-actions .crayons-reaction__count {
    color: #ff00ff !important;
    font-weight: bold !important;
}

.articletag-418challenge .crayons-icon:not(.crayons-icon--default) * {
    fill: #ffff00 !important;
}

.articletag-418challenge .c-embed .crayons-btn--primary {
  color: #00ff00 !important;
}

.articletag-418challenge .popover-billboard {
margin-bottom: 0 !important;
}

.crayons-story__contentpreview .ltag__link--embedded {
margin-top: 0 !important;
}

.subscription-icon {
    max-height: 16px !important;
    display: inline-block !important;
}

@media screen and (min-width: 950px) {
    .event-show-layout {
        margin-top: 24px !important;
    }
}

@media screen and (max-width: 949px) {
    .event-show-layout {
        padding: 11px !important;
    }
}


</style>
  </head>
    <body
      class="sans-serif-article-body default-header"
      data-user-status="logged-out"
      data-is-root-subforem="false"
        data-subforem-id="1"
      data-side-nav-visible="true"
      data-community-name="DEV Community"
      data-subscription-icon="https://assets.dev.to/assets/subscription-icon-805dfa7ac7dd660f07ed8d654877270825b07a92a03841aa99a1093bd00431b2.png"
      data-locale="en"
      data-honeybadger-key="hbp_nqu4Y66HuEKlD6YRGssZuRQnPOjDm50J8Zkr"
      data-deployed-at="2026-07-21T18:53:07Z"
      data-latest-commit-id="0178bfe3d62984121c07921b3ed6c78d22003471"
      data-ga-tracking="UA-71991109-1"
      data-cookie-banner-user-context="logged_out_only"
      data-cookie-banner-platform-context="off"
      data-algolia-id="PRSOBFP46H"
      data-algolia-search-key="9aa7d31610cba78851c9b1f63776a9dd"
      data-algolia-display="true"
      data-dynamic-url-component="bmar11"
      data-ga4-tracking-id="G-TYEM8Y3JN3"
      data-global-feature-flags-enabled="data_update_scripts onboarding_newsletter_content schedule_articles moderator_role display_ad_tags replace_unicorn_with_jump_to_comments article_id_adjusted_weight cloudflare_preferred_for_hosted_images multiple_reactions subscriber_icon ab_experiment_feed_strategy use_stories_endpoint digest_subject_testing digest_results_count_testing consistent_rendering discover_and_following_tabs hero_billboard onboarding_drip_emails algolia_frontend gemini_onboarding optimize_article_tag_query onboarding_custom_cta_slide dev_core_user_sync personalized_email_digests">
      
      <script>
        if (navigator.userAgent === 'ForemWebView/1' || window.frameElement) {
          document.body.classList.add("hidden-shell");
        }
          if (new Date() > new Date("2026-02-04T09:00:00-05:00")) {
            document.body.dataset.sideNavVisible = "false";
          } 
      </script>

      <link rel="stylesheet" href="https://assets.dev.to/assets/minimal-b74fc990bceac4211a1cd56dba292c86ef404899478f400db08e0ee6bb2fe52f.css" media="all" id="secondary-minimal-stylesheet" />
<link rel="stylesheet" href="https://assets.dev.to/assets/views-53fd5c62260337fdcc0cd283567529e2d0145374447ef4eee282979766a5d6d3.css" media="all" id="secondary-views-stylesheet" />
<link rel="stylesheet" href="https://assets.dev.to/assets/crayons-cd641458c515ed65f655e4222ec89a7e0394593a544555029c4b64da2bc7c722.css" media="all" id="secondary-crayons-stylesheet" />

      <div id="body-styles">
        <style>
          :root {
            --accent-brand-lighter-rgb: 86, 105, 285;
            --accent-brand-rgb: 64, 78, 211;
            --accent-brand-darker-rgb: 51, 62, 169;
          }
        </style>
      </div>
      <div id="audiocontent" data-podcast="">
        
      </div>
      <div class="navigation-progress" id="navigation-progress"></div>

<header id="topbar" class="crayons-header topbar print-hidden">
  <span id="route-change-target" tabindex="-1"></span>
  <a href="#main-content" class="skip-content-link">Skip to content</a>
  <div class="crayons-header__container">
    <span class="inline-block m:hidden ">
      <button class="c-btn c-btn--icon-alone js-hamburger-trigger mx-2">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" aria-labelledby="aeof11spegfxs3xqnd3nq7gm1k7tgscf" class="crayons-icon"><title id="aeof11spegfxs3xqnd3nq7gm1k7tgscf">Navigation menu</title>
    <path d="M3 4h18v2H3V4zm0 7h18v2H3v-2zm0 7h18v2H3v-2z"></path>
</svg>

      </button>
    </span>
    <a href="/" class="site-logo" aria-label="DEV Community Home" >
    <img class="site-logo__img"
         src="https://media2.dev.to/dynamic/image/quality=100/https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png"
         style="aspect-ratio: 10 / 8"
         alt="DEV Community">
</a>


    <div class="crayons-header--search js-search-form" id="header-search">
      <form accept-charset="UTF-8" method="get" action="/search" role="search">
        <div class="crayons-fields crayons-fields--horizontal">
          <div class="crayons-field flex-1 relative">
            <input id="search-input" class="crayons-header--search-input crayons-textfield js-search-input" type="text" id="nav-search" name="q" placeholder="Find related posts..." autocomplete="off" />
            <button type="submit" aria-label="Search" class="c-btn c-btn--icon-alone absolute inset-px right-auto mt-0 py-0">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" aria-labelledby="ahuzsl3a85v690dvzk8glfo76xntrai3" aria-hidden="true" class="crayons-icon"><title id="ahuzsl3a85v690dvzk8glfo76xntrai3">Search</title>
    <path d="M18.031 16.617l4.283 4.282-1.415 1.415-4.282-4.283A8.96 8.96 0 0111 20c-4.968 0-9-4.032-9-9s4.032-9 9-9 9 4.032 9 9a8.96 8.96 0 01-1.969 5.617zm-2.006-.742A6.977 6.977 0 0018 11c0-3.868-3.133-7-7-7-3.868 0-7 3.132-7 7 0 3.867 3.132 7 7 7a6.977 6.977 0 004.875-1.975l.15-.15z"></path>
</svg>

            </button>

            <a class="crayons-header--search-brand-indicator" href="https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral" target="_blank" rel="noopener noreferrer">
                Powered by Algolia
                <svg xmlns="http://www.w3.org/2000/svg" id="Layer_1" width="24" height="24" viewBox="0 0 500 500.34" role="img" aria-labelledby="ajwu2r37omaknoflwvho2kivun1n0uk7" aria-hidden="true" class="crayons-icon"><title id="ajwu2r37omaknoflwvho2kivun1n0uk7">Search</title>
  <defs></defs><path class="cls-1" d="M250,0C113.38,0,2,110.16,.03,246.32c-2,138.29,110.19,252.87,248.49,253.67,42.71,.25,83.85-10.2,120.38-30.05,3.56-1.93,4.11-6.83,1.08-9.52l-23.39-20.74c-4.75-4.22-11.52-5.41-17.37-2.92-25.5,10.85-53.21,16.39-81.76,16.04-111.75-1.37-202.04-94.35-200.26-206.1,1.76-110.33,92.06-199.55,202.8-199.55h202.83V407.68l-115.08-102.25c-3.72-3.31-9.43-2.66-12.43,1.31-18.47,24.46-48.56,39.67-81.98,37.36-46.36-3.2-83.92-40.52-87.4-86.86-4.15-55.28,39.65-101.58,94.07-101.58,49.21,0,89.74,37.88,93.97,86.01,.38,4.28,2.31,8.28,5.53,11.13l29.97,26.57c3.4,3.01,8.8,1.17,9.63-3.3,2.16-11.55,2.92-23.6,2.07-35.95-4.83-70.39-61.84-127.01-132.26-131.35-80.73-4.98-148.23,58.18-150.37,137.35-2.09,77.15,61.12,143.66,138.28,145.36,32.21,.71,62.07-9.42,86.2-26.97l150.36,133.29c6.45,5.71,16.62,1.14,16.62-7.48V9.49C500,4.25,495.75,0,490.51,0H250Z"></path>
</svg>

            </a>
          </div>
        </div>
      </form>
    </div>

    <div class="flex items-center h-100 ml-auto">
        <div class="flex" id="authentication-top-nav-actions">
          <span class="hidden m:block">
            <a href="https://dev.to/enter?signup_subforem=1" class="c-link c-link--block mr-2 whitespace-nowrap ml-auto" data-no-instant>
              Log in
            </a>
          </span>

          <a href="https://dev.to/enter?signup_subforem=1&amp;state=new-user" data-tracking-id="ca_top_nav" data-tracking-source="top_navbar" class="c-cta c-cta--branded whitespace-nowrap mr-2" data-no-instant>
            Create account
          </a>
        </div>
    </div>
  </div>
</header>

<div class="hamburger">
  <div class="hamburger__content">
    <header class="hamburger__content__header">
      <h2 class="fs-l fw-bold flex-1 break-word lh-tight">DEV Community</h2>

      <button class="c-btn c-btn--icon-alone js-hamburger-trigger shrink-0" aria-label="Close">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" aria-labelledby="af3992b80k25tf5m59rfmdkxig6m4pna" aria-hidden="true" class="crayons-icon c-btn__icon"><title id="af3992b80k25tf5m59rfmdkxig6m4pna">Close</title><path d="M12 10.586l4.95-4.95 1.414 1.414-4.95 4.95 4.95 4.95-1.414 1.414-4.95-4.95-4.95 4.95-1.414-1.414 4.95-4.95-4.95-4.95L7.05 5.636l4.95 4.95z"></path></svg>

      </button>
    </header>

    <div class="p-2 js-navigation-links-container" id="authentication-hamburger-actions">
    </div>
  </div>
  <div class="hamburger__overlay js-hamburger-trigger"></div>
</div>


      <div id="active-broadcast" class="broadcast-wrapper"></div>
<div id="page-content" class="wrapper stories stories-show articletag-python articletag-devtools articletag-ai articletag-agentskills articleuser-3817477" data-current-page="stories-show">
  <div id="page-content-inner" data-internal-nav="false" data-viewable-id="4202748" data-viewable-type="Article">
    <div id="page-route-change" class="screen-reader-only" aria-live="polite" aria-atomic="true"></div>

    
<style>
  .html-variant-wrapper { display: none}
</style>



<script src="https://unpkg.com/@webcomponents/webcomponentsjs@2.2.10/webcomponents-loader.js"
        integrity="sha384-3HK5hxQbkFqOIxMbpROlRmRtYl2LBZ52t+tqcjzsmr9NJuOWQxl8RgQSyFvq2lhy"
        crossorigin="anonymous" defer></script>

  <script src="https://assets.dev.to/assets/webShare-0686f0b9ac40589694ef6ae6a6202c44119bc781c254f6cf6d52d8a008461156.js" defer="defer"></script>
<script src="https://assets.dev.to/assets/articlePage-f48756b4b900540521c06f3c4a38fc6bdbcb80065eb4c4e960d3f0dde6dbc8e2.js" defer="defer"></script>
<script src="https://assets.dev.to/assets/commentDropdowns-7a28d130e5b78d38b30a9495a964003a66bd64fa455fc70b766d69cf06b9ba24.js" defer="defer"></script>


  <script type="application/ld+json">
    {"@context":"http://schema.org","@type":"Article","mainEntityOfPage":{"@type":"WebPage","@id":"https://dev.to/dr_data/agentscaffold-memory-peer-review-and-continuous-improvement-for-ai-coding-agents-43fb"},"url":"https://dev.to/dr_data/agentscaffold-memory-peer-review-and-continuous-improvement-for-ai-coding-agents-43fb","image":["https://media2.dev.to/dynamic/image/width=1080,height=1080,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F61aneq87hz3zabi50agk.png","https://media2.dev.to/dynamic/image/width=1280,height=720,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F61aneq87hz3zabi50agk.png","https://media2.dev.to/dynamic/image/width=1600,height=900,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F61aneq87hz3zabi50agk.png"],"publisher":{"@context":"http://schema.org","@type":"Organization","name":"DEV Community","logo":{"@context":"http://schema.org","@type":"ImageObject","url":"https://media2.dev.to/dynamic/image/width=192,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png","width":"192","height":"192"}},"headline":"AgentScaffold: Memory, Peer Review, and Continuous Improvement for AI Coding Agents","author":{"@context":"http://schema.org","@type":"Person","url":"https://dev.to/dr_data","name":"Dave"},"datePublished":"2026-07-23T05:38:36Z","dateModified":"2026-07-23T05:41:40Z","mainEntity":{"@type":"DiscussionForumPosting","@id":"#article-discussion-4202748","headline":"AgentScaffold: Memory, Peer Review, and Continuous Improvement for AI Coding Agents","text":"\u003cp\u003eAn AI coding agent will never tell you it's guessing. It doesn't hedge before a wrong answer, doesn't slow down when it's about to break something three modules away, doesn't leave a nervous comment admitting it isn't sure about this part. Right or catastrophically wrong, it hands you the same clean, confident, well-commented code at the same steady cadence — because in a language model, confidence tracks how plausible the next token looks, not whether the design actually holds up. There's no tell. That single property — fluent output with nothing calibrated underneath it — is what makes a capable agent genuinely dangerous on a real codebase, and it's the problem I built AgentScaffold to manage.\u003c/p\u003e\n\n\u003cp\u003eThree structural gaps make that dangerous in practice. First, an agent has no durable memory across the boundaries that matter: a new session, a compacted context window, a teammate's agent picking up the same repo tomorrow. Inside a single conversation it holds context fine; cross one of those seams and it starts over, cheerfully re-deriving everything it worked out yesterday. Second, left to its own devices it approaches each plan a little differently, with none of the consistent rigor a seasoned engineer brings — not out of laziness, but because nothing in the loop requires it. Third, it doesn't learn: catch a mistake on plan 12 and the same class of mistake turns up, refreshed and just as confident, on plan 40. Nothing carries the lesson forward.\u003c/p\u003e\n\n\u003cp\u003eMy career spans thirteen years as an industrial engineer at Boeing and the last eight-plus years as a data scientist in capacity engineering at Salesforce and Dropbox. A mindset that I learned as an industrial engineer that has persisted across the arc of my career is a systems-level mindset — the habit of spotting poorly designed processes and the toll they take on a system's time and resources, how the absence of standards lets variation creep in, and how, without a governance framework, mistakes accumulate both visibly and invisibly until they erode the outcome the original design was meant to deliver. Building software with an AI agent is just another process, and today's agentic tools run it without standards or a governance framework — failing in all three of those ways at once. AgentScaffold is a governance framework built to solve for them: memory so the agent stops losing state, peer review so mistakes are caught before they ship, and a continuous improvement loop so the standards tighten over time instead of slipping.\u003c/p\u003e\n\n\u003cp\u003eConcretely, it's a Python package (\u003ccode\u003epip install agentscaffold\u003c/code\u003e). It runs as an MCP server, so it works with Cursor, Claude Code, Windsurf, or anything else that speaks the protocol, and it ships a CLI for the parts that should be deterministic and boring.\u003c/p\u003e\n\n\u003ch3\u003e\n  \u003ca name=\"layer-1-memory-a-knowledge-graph-not-a-scrollback-buffer\" href=\"#layer-1-memory-a-knowledge-graph-not-a-scrollback-buffer\"\u003e\n  \u003c/a\u003e\n  Layer 1: Memory — a knowledge graph, not a scrollback buffer\n\u003c/h3\u003e\n\n\u003cp\u003e\u003ccode\u003escaffold index\u003c/code\u003e parses your repository into a DuckDB + DuckPGQ property graph. Tree-sitter handles eight languages — Python, TypeScript, JavaScript, Go, Rust, Java, C, and C++ — pulling out functions, classes, methods, and interfaces along with the IMPORTS and CALLS edges between them. It's a real graph, not a glorified tag file: on the order of twenty node types and forty edge types, because it doesn't stop at code.\u003c/p\u003e\n\n\u003cp\u003eWhat makes it more than a fancy ctags is that the same index ingests your governance artifacts — plans, interface contracts, ADRs, spikes, studies, review findings, backlog items — and wires them to the code they describe. A review finding isn't a sentence buried in a chat log nobody will scroll back to; it's a node attached to the exact file and function it concerns. Ask \"where did we leave off, and what's blocked?\" and the agent pulls recent plans, open findings, and next steps in a single MCP call — instead of reading three dozen files to reconstruct the state it had yesterday and then lost.\u003c/p\u003e\n\n\u003cp\u003eA few graph engineering details:\u003c/p\u003e\n\n\u003cul\u003e\n\u003cli\u003eIncremental indexing is honest about cost. Every file carries a SHA-256 content hash, and a (mtime, size) prefilter skips unchanged files without bothering to re-hash them. Edge re-resolution is scoped to the files that changed plus their direct importers — not a full-repo rebuild every time you hit save.\u003c/li\u003e\n\u003cli\u003eSearch degrades gracefully. Hybrid search fuses structural matches with semantic ones (all-MiniLM-L6-v2, 384-dim, merged by reciprocal rank fusion). Skip the embeddings extra and it falls back to keyword search — and says so, rather than quietly handing you worse results and letting you assume they're good.\u003c/li\u003e\n\u003cli\u003eIt refuses to confuse \"unknown\" with \"no.\" Call and import edges exist only for the parsed languages, so Markdown, YAML, and shell are structurally invisible. When an impact query comes back empty, the tools label it unconfirmed, not unused, and hand you a grep fallback. Zero callers means \"I didn't find any,\" not \"there are none.\" A product that exists because agents are overconfident does not get to be overconfident about what's safe to delete.\u003c/li\u003e\n\u003c/ul\u003e\n\n\u003cp\u003eModule structure comes from the Leiden algorithm (via graspologic), which clusters tightly-coupled files so you can see where your real boundaries are instead of guessing at them from the directory tree.\u003c/p\u003e\n\n\u003ch3\u003e\n  \u003ca name=\"layer-2-peer-review-your-digital-sprint-team-ready-to-call-bs-before-the-code-exists\" href=\"#layer-2-peer-review-your-digital-sprint-team-ready-to-call-bs-before-the-code-exists\"\u003e\n  \u003c/a\u003e\n  Layer 2: Peer review — your digital sprint team ready to call BS, before the code exists\n\u003c/h3\u003e\n\n\u003cp\u003eHere's the part people skip when they run agents without any governance around them. An agent reviewing its own plan isn't a review — it's the same model grading its own homework, with the exact blind spots that wrote the homework, and it awards itself full marks every time. What a plan needs before implementation is what any decent design review needs: someone else in the room poking at the assumptions, the edge cases, the error paths, and the integration points — not to win an argument, but to catch the thing you can't see precisely because you're the one who wrote it.\u003c/p\u003e\n\n\u003cp\u003eAgentScaffold runs that review before a line of code exists. A devil's-advocate pass goes after the riskiest assumptions and the ways the plan could fail quietly. An expansion review hunts the missing edge cases, the undocumented error paths, and the consumers the file-impact map conveniently forgot. Install a domain pack — there are ten: trading, mlops, data-engineering, infrastructure, api-services, webapp, mobile, embedded, game-dev, research — and a specialist reviewer shows up with standards and prompts tuned to the field. The trading pack's quant architect catches the look-ahead bias in a backtest that trains on data the strategy wouldn't have had at trade time; the webapp reviewer flags the accessibility and performance problems everyone plans to fix later. And because the reviews are grounded in the graph, a challenge reads \"src/data/router.py has 5 importers not in your impact map,\" not \"consider possible downstream effects.\"\u003c/p\u003e\n\n\u003cp\u003eThen the findings stick around. Record one and it becomes a ReviewFinding node linked to the plan and the file, ranked by severity, resurfacing in every future review of that plan until someone actually resolves it. The next session — different agent, fresh window, no memory of this morning — starts from \"this risk is known and open\" instead of rediscovering it the hard way. A caught risk should only cost you once.\u003c/p\u003e\n\n\u003ch3\u003e\n  \u003ca name=\"layer-3-continuous-improvement-the-loop-that-sharpens-the-reviewer\" href=\"#layer-3-continuous-improvement-the-loop-that-sharpens-the-reviewer\"\u003e\n  \u003c/a\u003e\n  Layer 3: Continuous improvement — the loop that sharpens the reviewer\n\u003c/h3\u003e\n\n\u003cp\u003eThis is the layer I'd keep if I had to throw out the other two, and it comes straight out of the industrial-engineering playbook: you don't just fix the defect, you fix the process that let the defect through, so the same class of mistake can't walk in the same way twice.\u003c/p\u003e\n\n\u003cp\u003eAfter implementation, a post-implementation review compares what got built against what was planned — an actual diff, not a satisfied nod. A retrospective records what worked, what took longer than the plan assumed, and what nobody saw coming, into a learnings_tracker. Then the part that actually matters: those learnings get folded back into the artifacts the next plan's review runs against. A recurring process mistake becomes a line in AGENTS.md. A structural gap becomes a change to the plan template. A risk pattern that keeps reappearing becomes a new question in the devil's-advocate prompt itself. A coding mistake becomes a line in an implementation standard.\u003c/p\u003e\n\n\u003cp\u003eIn full transparency, the loop is process-driven, not a magic self-rewriter. The lifecycle tools own the graph state — they write the findings, stamp the plan as reviewed, hand back a structured retro — and the agent, with you in the loop, updates the files. The framework supplies the ratchet and the checklist; it does not quietly rewrite your rulebook behind your back. Plan, do, check, act — where \"act\" lands as a concrete diff against the agent's own operating rules instead of a good intention nobody revisits. You do have to build the habit: read the learnings tracker every week and actually integrate what's in it. It's a process, but it works.\u003c/p\u003e\n\n\u003ch3\u003e\n  \u003ca name=\"what-actually-lands-in-your-repo\" href=\"#what-actually-lands-in-your-repo\"\u003e\n  \u003c/a\u003e\n  What actually lands in your repo\n\u003c/h3\u003e\n\n\u003cp\u003e\"Governance framework\" sounds like a binder nobody opens. In practice it's a set of templates, standards, and the rules that tell an agent how to use them. A template does for knowledge work exactly what a standard does on a production line: it removes variation. When every plan, decision, and experiment is captured the same way, the agent can't quietly skip the step it finds inconvenient, and the next person — or the next session — always knows where to look and what \"done\" means. \u003ccode\u003escaffold init\u003c/code\u003e writes into your project:\u003c/p\u003e\n\n\u003cul\u003e\n\u003cli\u003e\n\u003cstrong\u003ePlan templates\u003c/strong\u003e (feature, bugfix, refactor) — a plan can't leave draft without a file-impact map, a test plan, execution steps, and a rollback plan. This is the standard that quietly ends \"I'll figure out testing later.\"\u003c/li\u003e\n\u003cli\u003e\n\u003cstrong\u003eA spike template\u003c/strong\u003e — for high-uncertainty work: a time-boxed investigation that pressure-tests the risky assumption before you commit to a full plan, and forces an explicit proceed / pivot / defer call instead of a hopeful \"seems fine.\"\u003c/li\u003e\n\u003cli\u003e\n\u003cstrong\u003eA study template\u003c/strong\u003e — for experiments, A/B tests, and ablations: hypothesis, variants, metrics, conclusion. The result becomes a durable Study in the graph instead of a number that scrolls out of a notebook and is never seen again.\u003c/li\u003e\n\u003cli\u003e\n\u003cstrong\u003eAn ADR template\u003c/strong\u003e — architecture decision records that capture the decision, the alternatives you weighed, and why. Six months later, when someone asks \"why on earth did we build it this way,\" there's an answer — and the graph can trace which ADR governs which plan.\u003c/li\u003e\n\u003cli\u003e\n\u003cstrong\u003eReview prompts\u003c/strong\u003e — the devil's-advocate, expansion, and retrospective scripts the reviewers work from, and the same files the improvement loop sharpens over time.\u003c/li\u003e\n\u003cli\u003e\n\u003cstrong\u003eImplementation standards\u003c/strong\u003e for errors, logging, config, and testing, so the agent five sessions from now isn't reinventing your logging convention from scratch.\u003c/li\u003e\n\u003cli\u003e\n\u003cstrong\u003eAgent rules and state\u003c/strong\u003e — AGENTS.md plus platform-specific .cursor/rules, CLAUDE.md, and .windsurfrules, so Cursor, Claude Code, and Windsurf all read one operating manual; plus workflow_state.md, backlog.md, and learnings_tracker.md, so context survives a session boundary the same way the code graph does.\u003c/li\u003e\n\u003c/ul\u003e\n\n\u003cp\u003eNone of this clobbers what you've already written: generated content lives in managed blocks, existing files get appended to, and the graph's runtime artifacts are added to .gitignore for you.\u003c/p\u003e\n\n\u003cp\u003eIf you'd rather see it than read a file tree, here's a short tour of a freshly initialized project — the folders and files \u003ccode\u003escaffold init\u003c/code\u003e creates, and how the governance layer and the graph backend actually fit together:\u003c/p\u003e\n\n\n\u003cdiv style=\"position: relative; padding-bottom: 56.25%; height: 0;\"\u003e\n  \u003ciframe src=\"https://loom.com/embed/4209184f1bb84c259990cdc43f81df5c\" frameborder=\"0\" webkitallowfullscreen mozallowfullscreen allowfullscreen style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%;\"\u003e\n  \u003c/iframe\u003e\n\u003c/div\u003e\n\n\n\u003ch3\u003e\n  \u003ca name=\"the-honest-numbers-and-when-this-package-isnt-for-you\" href=\"#the-honest-numbers-and-when-this-package-isnt-for-you\"\u003e\n  \u003c/a\u003e\n  The honest numbers, and when this package isn’t for you\n\u003c/h3\u003e\n\n\u003cp\u003eThe efficiency case is real, with caveats. In the eval harness, when the agent routes through the tools the way it's supposed to, the raw reduction is about 46% fewer tokens and 84% fewer tool calls on tasks like orientation, impact analysis, and full plan review. Adjust for the fact that agents don't always take the paved road — sometimes they grep around a tool that would've answered in one call — and the replay-behavioral view is closer to 37% / 68%. Quality-adjusted, it lands around 33% / 61%. Those lower numbers are the honest ones, and they're the first thing I'd check if someone else were selling me this.\u003c/p\u003e\n\n\u003cp\u003eAnd it isn't magic. The savings come from the agent reading one structured answer instead of re-grepping and re-reading files to rebuild state it already had — which also means less context burned, and less of the window pressure that triggers the compaction-and-amnesia cycle this whole thing exists to prevent.\u003c/p\u003e\n\n\u003cp\u003eYou also might not need it. Solo, on a small, short-lived project, a well-written rules file gets you most of the way there, and the indexing and lifecycle overhead won't pay for itself. The value compounds with scale (impact analysis past the point where grep stops being trustworthy), with time (memory that accumulates instead of resetting), and with teams (shared contracts and findings that per-developer rules can't give you). It's alpha, and it's opinionated about process. If your preferred workflow is \"figure it out as we go,\" the gates will feel like friction — which is the point, not a bug I haven't gotten around to fixing.\u003c/p\u003e\n\n\u003ch3\u003e\n  \u003ca name=\"try-it\" href=\"#try-it\"\u003e\n  \u003c/a\u003e\n  Try it\n\u003c/h3\u003e\n\n\n\n\u003cp\u003e\u003ccode\u003ebash pip install \"agentscaffold[all]\" cd my-project scaffold init # templates, standards, agent rules, MCP wiring scaffold index --embeddings # build the knowledge graph (with semantic search) scaffold mcp # start the MCP server (or use the generated mcp.json)\u003c/code\u003e\u003cbr\u003e\n\u003c/p\u003e\n\n\u003cp\u003eCommands only tell you so much. Here's a hands-on tour on a fictional app called Appalicious — orientation, impact analysis, a pre-implementation review that records a finding, decision history, and the first implementation step. A quick walkthrough of the core tools and the collaboration protocol that governs the development workflow:\u003c/p\u003e\n\n\n\u003cdiv style=\"position: relative; padding-bottom: 56.25%; height: 0;\"\u003e\n  \u003ciframe src=\"https://loom.com/embed/7b7a5dca86164d818e5517ed6e0114a5\" frameborder=\"0\" webkitallowfullscreen mozallowfullscreen allowfullscreen style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%;\"\u003e\n  \u003c/iframe\u003e\n\u003c/div\u003e\n\n\n\u003cp\u003eOne parting thought: AgentScaffold is designed to be a governance framework that grows with you. If you leverage it correctly, your dev patterns can be learned and the standards and rules can be adapted to your preferences as you use it.\u003c/p\u003e\n\n\u003cp\u003eThe repo, with full docs, is at \u003ca href=\"https://github.com/drobbster/agentscaffold\" target=\"_blank\" rel=\"noopener noreferrer\"\u003ehttps://github.com/drobbster/agentscaffold\u003c/a\u003e. If you have any design suggestions reach out, start a conversation.\u003c/p\u003e\n\n","author":{"@type":"Person","name":"Dave","url":"https://dev.to/dr_data"},"datePublished":"2026-07-23T05:38:36Z","dateModified":"2026-07-23T05:41:40Z","url":"https://dev.to/dr_data/agentscaffold-memory-peer-review-and-continuous-improvement-for-ai-coding-agents-43fb","interactionStatistic":[{"@type":"InteractionCounter","interactionType":"https://schema.org/CommentAction","userInteractionCount":1},{"@type":"InteractionCounter","interactionType":"https://schema.org/LikeAction","userInteractionCount":1}],"comment":[{"@type":"Comment","@id":"#comment-1578817","text":"\u003cp\u003eWhat stood out to me is that you’re not treating memory as chat history, but as durable engineering knowledge tied to code, decisions, and review findings.\u003c/p\u003e\n\n\u003cp\u003eThe line about a caught risk only costing once really captures the value. That’s where agent tooling starts to feel like process improvement rather than just faster code generation.\u003c/p\u003e\n\n","author":{"@type":"Person","name":"Mustafa ERBAY","url":"https://dev.to/merbayerp"},"datePublished":"2026-07-23T06:02:05Z","dateModified":"2026-07-23T06:02:05Z","url":"https://dev.to/merbayerp/comment/3bldj","interactionStatistic":[{"@type":"InteractionCounter","interactionType":"https://schema.org/LikeAction","userInteractionCount":1}]}]}}
  </script>

  
  <div class="crayons-layout crayons-layout--3-cols crayons-layout--article">
    <aside class="crayons-layout__sidebar-left" aria-label="Article actions">
      <script>
  if (/Twitter for (iPhone|iPad|Android)/i.test(navigator.userAgent)) {
    document.documentElement.classList.add('is-twitter-in-app');
  }
</script>

  <div class="crayons-article-actions print-hidden">
    <div class="crayons-article-actions__inner">

      
<div class="reaction-drawer__outer hoverdown" style="">
  <button
    id="reaction-drawer-trigger"
    aria-label="reaction-drawer-trigger"
    aria-pressed="false"
    class="hoverdown-trigger crayons-reaction pseudo-reaction crayons-tooltip__activator relative">
      <span class="crayons-reaction__icon crayons-reaction__icon--borderless crayons-reaction--like crayons-reaction__icon--inactive" style="width: 40px; height: 40px">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" role="img" aria-hidden="true" class="crayons-icon">
    <g clip-path="url(#clip0_988_3276)">
        <path d="M19 14V17H22V19H18.999L19 22H17L16.999 19H14V17H17V14H19ZM20.243 4.75698C22.505 7.02498 22.583 10.637 20.479 12.992L19.059 11.574C20.39 10.05 20.32 7.65998 18.827 6.16998C17.324 4.67098 14.907 4.60698 13.337 6.01698L12.002 7.21498L10.666 6.01798C9.09103 4.60598 6.67503 4.66798 5.17203 6.17198C3.68203 7.66198 3.60703 10.047 4.98003 11.623L13.412 20.069L12 21.485L3.52003 12.993C1.41603 10.637 1.49503 7.01898 3.75603 4.75698C6.02103 2.49298 9.64403 2.41698 12 4.52898C14.349 2.41998 17.979 2.48998 20.242 4.75698H20.243Z" fill="#525252"></path>
    </g>
    <defs>
        <clipPath id="clip0_988_3276">
        <rect width="24" height="24" fill="white"></rect>
        </clipPath>
    </defs>
</svg>

      </span>
      <span class="crayons-reaction__icon crayons-reaction__icon--borderless crayons-reaction__icon--active" style="width: 40px; height: 40px">
        <img aria_hidden="true" height="24" width="24" src="https://assets.dev.to/assets/heart-plus-active-9ea3b22f2bc311281db911d416166c5f430636e76b15cd5df6b3b841d830eefa.svg" />
      </span>
      <span class="crayons-reaction__count" id="reaction_total_count">
        <span class="bg-base-40 opacity-25 p-2 inline-block radius-default"></span>
      </span>
      <span class="crayons-tooltip__content">
        Add reaction
      </span>
  </button>

  <div class="reaction-drawer" aria-expanded="false">
    <div class="reaction-drawer__container">
        <button
  id="reaction-butt-like"
  name="Like"
  aria-label="Like"
  aria-pressed="false"
  class="crayons-reaction crayons-tooltip__activator relative pt-2 pr-2 pb-1 pl-2"
  data-category="like">
    <span class="crayons-reaction__icon crayons-reaction__icon--inactive p-0">
      <img aria_hidden="true" height="32" width="32" src="https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg" />
    </span>
    <span class="crayons-reaction__count" id="reaction-number-like"><span class="bg-base-40 opacity-25 p-2 inline-block radius-default"></span></span>

    <span data-testid="tooltip" class="crayons-tooltip__content">
      Like
    </span>
</button>

        <button
  id="reaction-butt-unicorn"
  name="Unicorn"
  aria-label="Unicorn"
  aria-pressed="false"
  class="crayons-reaction crayons-tooltip__activator relative pt-2 pr-2 pb-1 pl-2"
  data-category="unicorn">
    <span class="crayons-reaction__icon crayons-reaction__icon--inactive p-0">
      <img aria_hidden="true" height="32" width="32" src="https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg" />
    </span>
    <span class="crayons-reaction__count" id="reaction-number-unicorn"><span class="bg-base-40 opacity-25 p-2 inline-block radius-default"></span></span>

    <span data-testid="tooltip" class="crayons-tooltip__content">
      Unicorn
    </span>
</button>

        <button
  id="reaction-butt-exploding_head"
  name="Exploding Head"
  aria-label="Exploding Head"
  aria-pressed="false"
  class="crayons-reaction crayons-tooltip__activator relative pt-2 pr-2 pb-1 pl-2"
  data-category="exploding_head">
    <span class="crayons-reaction__icon crayons-reaction__icon--inactive p-0">
      <img aria_hidden="true" height="32" width="32" src="https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg" />
    </span>
    <span class="crayons-reaction__count" id="reaction-number-exploding_head"><span class="bg-base-40 opacity-25 p-2 inline-block radius-default"></span></span>

    <span data-testid="tooltip" class="crayons-tooltip__content">
      Exploding Head
    </span>
</button>

        <button
  id="reaction-butt-raised_hands"
  name="Raised Hands"
  aria-label="Raised Hands"
  aria-pressed="false"
  class="crayons-reaction crayons-tooltip__activator relative pt-2 pr-2 pb-1 pl-2"
  data-category="raised_hands">
    <span class="crayons-reaction__icon crayons-reaction__icon--inactive p-0">
      <img aria_hidden="true" height="32" width="32" src="https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b