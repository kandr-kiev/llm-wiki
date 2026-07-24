---
source_url: https://dev.to/sarvar_04/sentrys-span-hierarchy-exposed-a-silent-retry-in-my-5-agent-pipeline-one-agent-took-226s-the-fb4
ingested: 2026-07-24
sha256: 868de7a20a77fa4e013d6ee7767b9c1a1484161c7701056d4532bef5e4f81ec3
blog_source: Dev Community
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Sentry&#39;s Span Hierarchy Exposed a Silent Retry in My 5-Agent Pipeline. One Agent Took 22.6s, the Others Took 5. - DEV Community</title>
    
    <link rel="preload" href="/reactions?article_id=4220414" as="fetch" crossorigin="same-origin">
    <link rel="canonical" href="https://dev.to/sarvar_04/sentrys-span-hierarchy-exposed-a-silent-retry-in-my-5-agent-pipeline-one-agent-took-226s-the-fb4" />
    <meta name="description" content="How gen_ai.invoke_agent spans revealed one tool was dumping 7x more output than its siblings. The fix: pagination + a token budget guard. 42% output reduction, 21% faster agent. Tagged with devchallenge, bugsmash, ai, aws.">
    <meta name="keywords" content="devchallenge, bugsmash, ai, aws, software, coding, development, engineering, inclusive, community">

    <meta property="og:type" content="article" />
    <meta property="og:url" content="https://dev.to/sarvar_04/sentrys-span-hierarchy-exposed-a-silent-retry-in-my-5-agent-pipeline-one-agent-took-226s-the-fb4" />
    <meta property="og:title" content="Sentry&#39;s Span Hierarchy Exposed a Silent Retry in My 5-Agent Pipeline. One Agent Took 22.6s, the Others Took 5." />
    <meta property="og:description" content="How gen_ai.invoke_agent spans revealed one tool was dumping 7x more output than its siblings. The fix: pagination + a token budget guard. 42% output reduction, 21% faster agent." />
    <meta property="og:site_name" content="DEV Community" />
    <meta name="twitter:site" content="@thepracticaldev">
    <meta name="twitter:creator" content="@">
    <meta name="author-trust" content="0">
    <meta name="twitter:title" content="Sentry&#39;s Span Hierarchy Exposed a Silent Retry in My 5-Agent Pipeline. One Agent Took 22.6s, the Others Took 5.">
    <meta name="twitter:description" content="How gen_ai.invoke_agent spans revealed one tool was dumping 7x more output than its siblings. The fix: pagination + a token budget guard. 42% output reduction, 21% faster agent.">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:widgets:new-embed-design" content="on">
    <meta name="robots" content="max-snippet:-1, max-image-preview:large, max-video-preview:-1">
      <meta property="og:image" content="https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fqk0xs1de40d6us98fre1.png" />
      <meta name="twitter:image:src" content="https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fqk0xs1de40d6us98fre1.png">
      <meta name="robots" content="noindex">
      <meta name="robots" content="nofollow">

      <meta name="last-updated" content="2026-07-24 05:49:42 UTC">
      <meta name="user-signed-in" content="false">
      <meta name="head-cached-at" content="1784872182">
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
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" aria-labelledby="alm0rmz9a68q3yfmucegp2yfp3seczqy" class="crayons-icon"><title id="alm0rmz9a68q3yfmucegp2yfp3seczqy">Navigation menu</title>
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
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" aria-labelledby="af0y9eatzrkn99adm6876xyd32zwioiu" aria-hidden="true" class="crayons-icon"><title id="af0y9eatzrkn99adm6876xyd32zwioiu">Search</title>
    <path d="M18.031 16.617l4.283 4.282-1.415 1.415-4.282-4.283A8.96 8.96 0 0111 20c-4.968 0-9-4.032-9-9s4.032-9 9-9 9 4.032 9 9a8.96 8.96 0 01-1.969 5.617zm-2.006-.742A6.977 6.977 0 0018 11c0-3.868-3.133-7-7-7-3.868 0-7 3.132-7 7 0 3.867 3.132 7 7 7a6.977 6.977 0 004.875-1.975l.15-.15z"></path>
</svg>

            </button>

            <a class="crayons-header--search-brand-indicator" href="https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral" target="_blank" rel="noopener noreferrer">
                Powered by Algolia
                <svg xmlns="http://www.w3.org/2000/svg" id="Layer_1" width="24" height="24" viewBox="0 0 500 500.34" role="img" aria-labelledby="ao9bpyr0rtusegvhl9qq84ca3kefovrp" aria-hidden="true" class="crayons-icon"><title id="ao9bpyr0rtusegvhl9qq84ca3kefovrp">Search</title>
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
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" aria-labelledby="ag888fcrz08gztyrj2zupuzkanuy9jai" aria-hidden="true" class="crayons-icon c-btn__icon"><title id="ag888fcrz08gztyrj2zupuzkanuy9jai">Close</title><path d="M12 10.586l4.95-4.95 1.414 1.414-4.95 4.95 4.95 4.95-1.414 1.414-4.95-4.95-4.95 4.95-1.414-1.414 4.95-4.95-4.95-4.95L7.05 5.636l4.95 4.95z"></path></svg>

      </button>
    </header>

    <div class="p-2 js-navigation-links-container" id="authentication-hamburger-actions">
    </div>
  </div>
  <div class="hamburger__overlay js-hamburger-trigger"></div>
</div>


      <div id="active-broadcast" class="broadcast-wrapper"></div>
<div id="page-content" class="wrapper stories stories-show articletag-devchallenge articletag-bugsmash articletag-ai articletag-aws articleuser-1163149" data-current-page="stories-show">
  <div id="page-content-inner" data-internal-nav="false" data-viewable-id="4220414" data-viewable-type="Article">
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
    {"@context":"http://schema.org","@type":"Article","mainEntityOfPage":{"@type":"WebPage","@id":"https://dev.to/sarvar_04/sentrys-span-hierarchy-exposed-a-silent-retry-in-my-5-agent-pipeline-one-agent-took-226s-the-fb4"},"url":"https://dev.to/sarvar_04/sentrys-span-hierarchy-exposed-a-silent-retry-in-my-5-agent-pipeline-one-agent-took-226s-the-fb4","image":["https://media2.dev.to/dynamic/image/width=1080,height=1080,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fqk0xs1de40d6us98fre1.png","https://media2.dev.to/dynamic/image/width=1280,height=720,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fqk0xs1de40d6us98fre1.png","https://media2.dev.to/dynamic/image/width=1600,height=900,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fqk0xs1de40d6us98fre1.png"],"publisher":{"@context":"http://schema.org","@type":"Organization","name":"DEV Community","logo":{"@context":"http://schema.org","@type":"ImageObject","url":"https://media2.dev.to/dynamic/image/width=192,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png","width":"192","height":"192"}},"headline":"Sentry's Span Hierarchy Exposed a Silent Retry in My 5-Agent Pipeline. One Agent Took 22.6s, the Others Took 5.","author":{"@context":"http://schema.org","@type":"Person","url":"https://dev.to/sarvar_04","name":"Sarvar Nadaf"},"datePublished":"2026-07-24T05:48:09Z","dateModified":"2026-07-24T05:48:09Z","mainEntity":{"@type":"DiscussionForumPosting","@id":"#article-discussion-4220414","headline":"Sentry's Span Hierarchy Exposed a Silent Retry in My 5-Agent Pipeline. One Agent Took 22.6s, the Others Took 5.","text":"\u003cp\u003e\u003cem\u003eThis is a submission for \u003ca href=\"https://dev.to/bugsmash\"\u003eDEV's Summer Bug Smash: Clear the Lineup\u003c/a\u003e powered by \u003ca href=\"https://sentry.io/\" target=\"_blank\" rel=\"noopener noreferrer\"\u003eSentry\u003c/a\u003e.\u003c/em\u003e\u003c/p\u003e\n\n\n\u003chr\u003e\n\n\u003ch2\u003e\n  \u003ca name=\"project-overview\" href=\"#project-overview\"\u003e\n  \u003c/a\u003e\n  Project Overview\n\u003c/h2\u003e\n\n\u003cp\u003eI built an \u003cstrong\u003eAWS Security Posture Agent\u003c/strong\u003e: five specialist AI agents that scan your AWS account for security misconfigurations, map findings to CIS benchmarks, score risk, and generate copy-paste fix commands.\u003c/p\u003e\n\n\u003cp\u003eThe agents run sequentially on CrewAI with Amazon Bedrock Nova Pro as the LLM:\u003cbr\u003e\n\u003c/p\u003e\n\n\u003cdiv class=\"highlight js-code-highlight\"\u003e\n\u003cpre class=\"highlight plaintext\"\u003e\u003ccode\u003e1. ResourceDiscovery    → inventories EC2, S3, Lambda, IAM, SGs, API GW, DynamoDB\n2. SecurityScanner      → finds open ports, public buckets, admin roles, insecure configs\n3. ComplianceChecker    → maps to CIS AWS Foundations Benchmark\n4. RiskScorer           → severity × blast radius × exploitability\n5. RemediationPlanner   → generates AWS CLI fix commands\n\u003c/code\u003e\u003c/pre\u003e\n\u003cdiv class=\"highlight__panel js-actions-panel\"\u003e\n\u003cdiv class=\"highlight__panel-action js-fullscreen-code-action\"\u003e\n    \u003csvg xmlns=\"http://www.w3.org/2000/svg\" width=\"20px\" height=\"20px\" viewbox=\"0 0 24 24\" class=\"highlight-action crayons-icon highlight-action--fullscreen-on\"\u003e\u003ctitle\u003eEnter fullscreen mode\u003c/title\u003e\n    \u003cpath d=\"M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z\"\u003e\u003c/path\u003e\n\u003c/svg\u003e\n\n    \u003csvg xmlns=\"http://www.w3.org/2000/svg\" width=\"20px\" height=\"20px\" viewbox=\"0 0 24 24\" class=\"highlight-action crayons-icon highlight-action--fullscreen-off\"\u003e\u003ctitle\u003eExit fullscreen mode\u003c/title\u003e\n    \u003cpath d=\"M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z\"\u003e\u003c/path\u003e\n\u003c/svg\u003e\n\n\u003c/div\u003e\n\u003c/div\u003e\n\u003c/div\u003e\n\n\n\u003cp\u003eEach agent has custom boto3 tools that make real AWS API calls against a live account with 90 IAM roles, 14 S3 buckets, 9 security groups, and 7 Lambda functions. Not test data. Real findings.\u003c/p\u003e\n\n\u003chr\u003e\n\n\n\u003cdiv class=\"ltag-github-readme-tag\"\u003e\n  \u003cdiv class=\"readme-overview\"\u003e\n    \u003ch2\u003e\n      \u003cimg src=\"https://assets.dev.to/assets/github-logo-5a155e1f9a670af7944dd5e12375bc76ed542ea80224905ecaf878b9157cdefc.svg\" alt=\"GitHub logo\"\u003e\n      \u003ca href=\"https://github.com/simplynadaf\" target=\"_blank\" rel=\"noopener noreferrer\"\u003e\n        simplynadaf\n      \u003c/a\u003e / \u003ca style=\"font-weight: 600;\" href=\"https://github.com/simplynadaf/aws-security-posture-agent\" target=\"_blank\" rel=\"noopener noreferrer\"\u003e\n        aws-security-posture-agent\n      \u003c/a\u003e\n    \u003c/h2\u003e\n    \u003ch3\u003e\n      Multi-agent AI system that scans AWS accounts for security misconfigurations using CrewAI + Amazon Bedrock, instrumented with Sentry AI Agent Monitoring.  5 specialist agents discover resources, analyze security, map to CIS benchmarks, score risk, and generate fix commands.\n    \u003c/h3\u003e\n  \u003c/div\u003e\n  \u003cdiv class=\"ltag-github-body\"\u003e\n    \n\u003cdiv id=\"readme\" class=\"md\" data-path=\"README.md\"\u003e\u003carticle class=\"markdown-body entry-content container-lg\" itemprop=\"text\"\u003e\u003cdiv align=\"center\" dir=\"auto\"\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\n\u003ch1 class=\"heading-element\" dir=\"auto\"\u003eAWS Security Posture Agent\u003c/h1\u003e\n\u003c/div\u003e\n\n\u003cp dir=\"auto\"\u003e\u003cstrong\u003eFive AI agents scan your AWS account. Find misconfigurations. Score risk. Get fix commands.\u003c/strong\u003e\u003c/p\u003e\n\n\u003cp dir=\"auto\"\u003e\u003ca href=\"https://python.org\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"\u003e\u003cimg src=\"https://camo.githubusercontent.com/66fb2689aaa25f80a8be6cff6a545571d5570f8000dd1970752b4b964ba02689/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e31322b2d626c75653f7374796c653d666f722d7468652d6261646765\" alt=\"Python\" data-canonical-src=\"https://img.shields.io/badge/python-3.12+-blue?style=for-the-badge\" style=\"max-width: 100%;\"\u003e\u003c/a\u003e\n\u003ca href=\"https://crewai.com\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"\u003e\u003cimg src=\"https://camo.githubusercontent.com/440c0080ea4c75ac2e62ae575be4c3daaa2d05a78cdd27ac2e1efa02a4da2a29/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6372657761692d312e31352d677265656e3f7374796c653d666f722d7468652d6261646765\" alt=\"CrewAI\" data-canonical-src=\"https://img.shields.io/badge/crewai-1.15-green?style=for-the-badge\" style=\"max-width: 100%;\"\u003e\u003c/a\u003e\n\u003ca href=\"https://sentry.io\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"\u003e\u003cimg src=\"https://camo.githubusercontent.com/d03ce15ed42502b6eb3930cd74ca03f89b591bcce6c0b12ed75a4bbe54b47a84/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73656e7472792d41492532304d6f6e69746f72696e672d707572706c653f7374796c653d666f722d7468652d6261646765\" alt=\"Sentry\" data-canonical-src=\"https://img.shields.io/badge/sentry-AI%20Monitoring-purple?style=for-the-badge\" style=\"max-width: 100%;\"\u003e\u003c/a\u003e\n\u003ca href=\"https://aws.amazon.com/bedrock/\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"\u003e\u003cimg src=\"https://camo.githubusercontent.com/b80c525f9b228dd9a6d73a1f0b83995d6c106f49cabc5dff20ee8a8eafcdfa1a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4157532d426564726f636b2532304e6f766125323050726f2d6f72616e67653f7374796c653d666f722d7468652d6261646765\" alt=\"Bedrock\" data-canonical-src=\"https://img.shields.io/badge/AWS-Bedrock%20Nova%20Pro-orange?style=for-the-badge\" style=\"max-width: 100%;\"\u003e\u003c/a\u003e\n\u003ca href=\"https://github.com/simplynadaf/aws-security-posture-agent/LICENSE\" target=\"_blank\" rel=\"noopener noreferrer\"\u003e\u003cimg src=\"https://camo.githubusercontent.com/daa52099573be5a50c320c4387496400f2f722e49f86a42db8d5778130d3582d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d677265656e3f7374796c653d666f722d7468652d6261646765\" alt=\"License\" data-canonical-src=\"https://img.shields.io/badge/license-MIT-green?style=for-the-badge\" style=\"max-width: 100%;\"\u003e\u003c/a\u003e\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003ca href=\"https://github.com/simplynadaf/aws-security-posture-agent#quick-start\" target=\"_blank\" rel=\"noopener noreferrer\"\u003eQuick Start\u003c/a\u003e | \u003ca href=\"https://github.com/simplynadaf/aws-security-posture-agent#architecture\" target=\"_blank\" rel=\"noopener noreferrer\"\u003eArchitecture\u003c/a\u003e | \u003ca href=\"https://github.com/simplynadaf/aws-security-posture-agent#screenshots\" target=\"_blank\" rel=\"noopener noreferrer\"\u003eScreenshots\u003c/a\u003e | \u003ca href=\"https://github.com/simplynadaf/aws-security-posture-agent#performance-bug-fix\" target=\"_blank\" rel=\"noopener noreferrer\"\u003ePerformance Fix\u003c/a\u003e\u003c/p\u003e\n\u003c/div\u003e\n\u003chr\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\n\u003ch2 class=\"heading-element\" dir=\"auto\"\u003eThe Problem\u003c/h2\u003e\n\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eMost AWS accounts accumulate security debt silently. Open SSH ports from testing. S3 buckets without encryption. IAM roles with full admin access that nobody remembers creating. Manual audits miss things. AWS Config rules cost money. SecurityHub is noisy.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eThis agent scans your account in 60 seconds, finds real issues, maps them to CIS benchmarks, scores risk, and gives you the exact AWS CLI command to fix each one.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\n\u003ch2 class=\"heading-element\" dir=\"auto\"\u003eWhat It Finds\u003c/h2\u003e\n\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eOn a real AWS account (90 IAM roles, 14 S3 buckets, 9 security groups, 7 Lambda functions):\u003c/p\u003e\n\u003cdiv class=\"snippet-clipboard-content notranslate position-relative overflow-auto\" data-snippet-clipboard-copy-content=\"97 security findings\n├── CRITICAL: open SSH/RDP from 0.0.0.0/0, IAM users without MFA\n├── HIGH:     admin roles, unencrypted EBS, missing public access blocks  \n├── MEDIUM:   deprecated Lambda runtimes, missing versioning, stale SGs\n└── LOW:      direct user policies, missing DLQ on Lambda\"\u003e\n\u003cpre class=\"notranslate\"\u003e\u003ccode\u003e97 security findings\n├── CRITICAL: open SSH/RDP from 0.0.0.0/0, IAM users without MFA\n├── HIGH:     admin roles, unencrypted EBS, missing public access blocks\n├── MEDIUM:   deprecated Lambda runtimes, missing versioning, stale SGs\n└──\u003c/code\u003e\u003c/pre\u003e…\u003c/div\u003e\u003c/article\u003e\u003c/div\u003e\n  \u003c/div\u003e\n  \u003cdiv class=\"gh-btn-container\"\u003e\u003ca class=\"gh-btn\" href=\"https://github.com/simplynadaf/aws-security-posture-agent\" target=\"_blank\" rel=\"noopener noreferrer\"\u003eView on GitHub\u003c/a\u003e\u003c/div\u003e\n\u003c/div\u003e\n\n\n\n\u003chr\u003e\n\n\u003ch3\u003e\n  \u003ca name=\"demo\" href=\"#demo\"\u003e\n  \u003c/a\u003e\n  Demo\n\u003c/h3\u003e\n\n\u003cp\u003eHere's the full scan running against my AWS account. The scan portion is sped up 4x, results walkthrough is at normal speed:\u003c/p\u003e\n\n\u003cp\u003e  \u003ciframe src=\"https://www.youtube.com/embed/UuOvKcdtYLs\" style=\"width: 100%; aspect-ratio: 16 / 9;\" allowfullscreen loading=\"lazy\"\u003e\n  \u003c/iframe\u003e\n\u003c/p\u003e\n\n\n\u003chr\u003e\n\n\u003ch2\u003e\n  \u003ca name=\"bug-fix-or-performance-improvement\" href=\"#bug-fix-or-performance-improvement\"\u003e\n  \u003c/a\u003e\n  Bug Fix or Performance Improvement\n\u003c/h2\u003e\n\n\u003cp\u003eMy first instinct was to blame Bedrock latency. Every time something is slow you blame the LLM, right?\u003c/p\u003e\n\n\u003cp\u003eThe \u003cstrong\u003eSecurityScanner agent\u003c/strong\u003e was taking 22.6 seconds while every other agent averaged 5-10 seconds. Without visibility into what was happening inside each agent's execution, I would have added \u003ccode\u003etime.time()\u003c/code\u003e calls and guessed.\u003c/p\u003e\n\n\u003cp\u003eSentry's trace waterfall told a different story. The real problem wasn't Python execution time or network latency. It was the LLM getting a context payload it couldn't process cleanly on the first attempt.\u003c/p\u003e\n\n\u003cp\u003eThe root cause: my \u003ccode\u003eIAMAnalyzer\u003c/code\u003e tool was fetching all 90 IAM roles from the account (59 after filtering service-linked roles), serializing them into a 27KB JSON blob, and handing that entire payload to the LLM as tool output. The context window got overwhelmed. CrewAI's internal retry logic kicked in, burning tokens on a second attempt with even more context.\u003c/p\u003e\n\n\u003cp\u003eOne tool. Wrong default. The entire pipeline suffered.\u003c/p\u003e\n\n\n\u003chr\u003e\n\n\u003ch2\u003e\n  \u003ca name=\"code\" href=\"#code\"\u003e\n  \u003c/a\u003e\n  Code\n\u003c/h2\u003e\n\n\u003cp\u003ePR with the fix:\u003c/p\u003e\n\n\n\u003cdiv class=\"ltag_github-liquid-tag\"\u003e\n  \u003ch1\u003e\n    \u003ca href=\"https://github.com/simplynadaf/aws-security-posture-agent/pull/1\" target=\"_blank\" rel=\"noopener noreferrer\"\u003e\n      \u003cimg class=\"github-logo\" alt=\"GitHub logo\" src=\"https://assets.dev.to/assets/github-logo-5a155e1f9a670af7944dd5e12375bc76ed542ea80224905ecaf878b9157cdefc.svg\"\u003e\n      \u003cspan class=\"issue-title\"\u003e\n        fix: paginate IAM analysis and add token budget guard\n      \u003c/span\u003e\n      \u003cspan class=\"issue-number\"\u003e#1\u003c/span\u003e\n    \u003c/a\u003e\n  \u003c/h1\u003e\n  \u003cdiv class=\"github-thread\"\u003e\n    \u003cdiv class=\"timeline-comment-header\"\u003e\n      \u003ca href=\"https://github.com/simplynadaf\" target=\"_blank\" rel=\"noopener noreferrer\"\u003e\n        \u003cimg class=\"github-liquid-tag-img\" src=\"https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F107028874%3Fv%3D4\" alt=\"simplynadaf avatar\" loading=\"lazy\"\u003e\n      \u003c/a\u003e\n      \u003cdiv class=\"timeline-comment-header-text\"\u003e\n        \u003cstrong\u003e\n          \u003ca href=\"https://github.com/simplynadaf\" target=\"_blank\" rel=\"noopener noreferrer\"\u003esimplynadaf\u003c/a\u003e\n        \u003c/strong\u003e posted on \u003ca href=\"https://github.com/simplynadaf/aws-security-posture-agent/pull/1\" target=\"_blank\" rel=\"noopener noreferrer\"\u003e\u003ctime datetime=\"2026-07-20T11:40:51Z\"\u003eJul 20, 2026\u003c/time\u003e\u003c/a\u003e\n      \u003c/div\u003e\n    \u003c/div\u003e\n    \u003cdiv class=\"ltag-github-body\"\u003e\n      \u003cdiv class=\"markdown-heading\"\u003e\n\u003ch2 class=\"heading-element\"\u003eWhat\u003c/h2\u003e\n\u003ca id=\"user-content-what\" class=\"anchor\" aria-label=\"Permalink: What\" href=\"#what\"\u003e\u003cspan aria-hidden=\"true\" class=\"octicon octicon-link\"\u003e\u003c/span\u003e\u003c/a\u003e\n\u003c/div\u003e\n\u003cp\u003eThe IAMAnalyzer tool was fetching every single role in the account (90 of them, 59 after filtering service-linked ones) and dumping the full details into a single JSON blob. That blob hit 26,980 characters. The LLM choked on it, CrewAI retried the task, and the SecurityScanner agent ended up taking 22.6s while every other agent finished in 5-10s.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\"\u003e\n\u003ch2 class=\"heading-element\"\u003eHow I found it\u003c/h2\u003e\n\u003ca id=\"user-content-how-i-found-it\" class=\"anchor\" aria-label=\"Permalink: How I found it\" href=\"#how-i-found-it\"\u003e\u003cspan aria-hidden=\"true\" class=\"octicon octicon-link\"\u003e\u003c/span\u003e\u003c/a\u003e\n\u003c/div\u003e\n\u003cp\u003eAdded Sentry spans to each agent and tool. The trace waterfall made it obvious: SecurityScanner was twice as wide as everything else. Drilled into the tool spans and saw \u003ccode\u003eresult_length_chars: 26980\u003c/code\u003e on \u003ccode\u003eiam_analyzer\u003c/code\u003e vs ~4000 on the other tools.\u003c/p\u003e\n\u003cp\u003e7x output disproportion. That was the problem.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\"\u003e\n\u003ch2 class=\"heading-element\"\u003eWhat I changed\u003c/h2\u003e\n\u003ca id=\"user-content-what-i-changed\" class=\"anchor\" aria-label=\"Permalink: What I changed\" href=\"#what-i-changed\"\u003e\u003cspan aria-hidden=\"true\" class=\"octicon octicon-link\"\u003e\u003c/span\u003e\u003c/a\u003e\n\u003c/div\u003e\n\u003cp\u003eThree things in \u003ccode\u003eiam_analyzer.py\u003c/code\u003e:\u003c/p\u003e\n\u003col\u003e\n\u003cli\u003ePaginate and sort roles by \u003ccode\u003eRoleLastUsed\u003c/code\u003e date, only analyze the top 20 most active ones. The rest are stale roles nobody has touched in months.\u003c/li\u003e\n\u003cli\u003eSkip 31 service-linked roles upfront (you cannot modify them anyway, auditing them is noise).\u003c/li\u003e\n\u003cli\u003eToken budget guard at the end: if the JSON output exceeds 4000 chars, trim the role_summary down to just names and policy lists.\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\"\u003e\n\u003ch2 class=\"heading-element\"\u003eNumbers\u003c/h2\u003e\n\u003ca id=\"user-content-numbers\" class=\"anchor\" aria-label=\"Permalink: Numbers\" href=\"#numbers\"\u003e\u003cspan aria-hidden=\"true\" class=\"octicon octicon-link\"\u003e\u003c/span\u003e\u003c/a\u003e\n\u003c/div\u003e\n\u003cul\u003e\n\u003cli\u003eTool output: 26,980 chars down to 15,532 (42% smaller)\u003c/li\u003e\n\u003cli\u003eSecurityScanner: 22.6s down to 17.8s (21% faster, no more LLM retry)\u003c/li\u003e\n\u003cli\u003eAPI calls to IAM: 59 down to 20\u003c/li\u003e\n\u003cli\u003eTotal pipeline: 62s down to 57.7s\u003c/li\u003e\n\u003cli\u003eFindings: still 27. No coverage loss because the top-20 most active roles contain all the problematic ones (AdminRole, Bedrock-Lambda-Role, etc are all heavily used).\u003c/li\u003e\n\u003c/ul\u003e\n\n    \u003c/div\u003e\n    \u003cdiv class=\"gh-btn-container\"\u003e\u003ca class=\"gh-btn\" href=\"https://github.com/simplynadaf/aws-security-posture-agent/pull/1\" target=\"_blank\" rel=\"noopener noreferrer\"\u003eView on GitHub\u003c/a\u003e\u003c/div\u003e\n  \u003c/div\u003e\n\u003c/div\u003e\n\n\n\u003cp\u003eThe core change lives in \u003ccode\u003esrc/security_posture/tools/iam_analyzer.py\u003c/code\u003e. Here's the before and after:\u003c/p\u003e\n\n\u003cp\u003e\u003cstrong\u003eBefore (the bug):\u003c/strong\u003e\u003cbr\u003e\n\u003c/p\u003e\n\n\u003cdiv class=\"highlight js-code-highlight\"\u003e\n\u003cpre class=\"highlight python\"\u003e\u003ccode\u003e\u003cspan class=\"c1\"\u003e# Fetches ALL roles without pagination limit\n\u003c/span\u003e\u003cspan class=\"n\"\u003eroles\u003c/span\u003e \u003cspan class=\"o\"\u003e=\u003c/span\u003e \u003cspan class=\"n\"\u003eiam\u003c/span\u003e\u003cspan class=\"p\"\u003e.\u003c/span\u003e\u003cspan class=\"nf\"\u003elist_roles\u003c/span\u003e\u003cspan class=\"p\"\u003e(\u003c/span\u003e\u003cspan class=\"n\"\u003eMaxItems\u003c/span\u003e\u003cspan class=\"o\"\u003e=\u003c/span\u003e\u003cspan class=\"mi\"\u003e100\u003c/span\u003e\u003cspan class=\"p\"\u003e)\u003c/span\u003e\n\u003cspan class=\"n\"\u003erole_details\u003c/span\u003e \u003cspan class=\"o\"\u003e=\u003c/span\u003e \u003cspan class=\"p\"\u003e[]\u003c/span\u003e\n\n\u003cspan class=\"k\"\u003efor\u003c/span\u003e \u003cspan class=\"n\"\u003erole\u003c/span\u003e \u003cspan class=\"ow\"\u003ein\u003c/span\u003e \u003cspan class=\"n\"\u003eroles\u003c/span\u003e\u003cspan class=\"p\"\u003e[\u003c/span\u003e\u003cspan class=\"sh\"\u003e\"\u003c/span\u003e\u003cspan class=\"s\"\u003eRoles\u003c/span\u003e\u003cspan class=\"sh\"\u003e\"\u003c/span\u003e\u003cspan class=\"p\"\u003e]:\u003c/span\u003e\n    \u003cspan class=\"n\"\u003erole_name\u003c/span\u003e \u003cspan class=\"o\"\u003e=\u003c/span\u003e \u003cspan class=\"n\"\u003erole\u003c/span\u003e\u003cspan class=\"p\"\u003e[\u003c/span\u003e\u003cspan class=\"sh\"\u003e\"\u003c/span\u003e\u003cspan class=\"s\"\u003eRoleName\u003c/span\u003e\u003cspan class=\"sh\"\u003e\"\u003c/span\u003e\u003cspan class=\"p\"\u003e]\u003c/span\u003e\n    \u003cspan class=\"k\"\u003eif\u003c/span\u003e \u003cspan class=\"n\"\u003erole\u003c/span\u003e\u003cspan class=\"p\"\u003e.\u003c/span\u003e\u003cspan class=\"nf\"\u003eget\u003c/span\u003e\u003cspan class=\"p\"\u003e(\u003c/span\u003e\u003cspan class=\"sh\"\u003e\"\u003c/span\u003e\u003cspan class=\"s\"\u003ePath\u003c/span\u003e\u003cspan class=\"sh\"\u003e\"\u003c/span\u003e\u003cspan class=\"p\"\u003e,\u003c/span\u003e \u003cspan class=\"sh\"\u003e\"\"\u003c/span\u003e\u003cspan class=\"p\"\u003e).\u003c/span\u003e\u003cspan class=\"nf\"\u003estartswith\u003c/span\u003e\u003cspan class=\"p\"\u003e(\u003c/span\u003e\u003cspan class=\"sh\"\u003e\"\u003c/span\u003e\u003cspan class=\"s\"\u003e/aws-service-role/\u003c/span\u003e\u003cspan class=\"sh\"\u003e\"\u003c/span\u003e\u003cspan class=\"p\"\u003e):\u003c/span\u003e\n        \u003cspan class=\"k\"\u003econtinue\u003c/span\u003e\n    \u003cspan class=\"c1\"\u003e# Analyzes every single role...\n\u003c/span\u003e    \u003cspan class=\"n\"\u003eattached\u003c/span\u003e \u003cspan class=\"o\"\u003e=\u003c/span\u003e \u003cspan class=\"n\"\u003eiam\u003c/span\u003e\u003cspan class=\"p\"\u003e.\u003c/span\u003e\u003cspan class=\"nf\"\u003elist_attached_role_policies\u003c/span\u003e\u003cspan class=\"p\"\u003e(\u003c/span\u003e\u003cspan class=\"n\"\u003eRoleName\u003c/span\u003e\u003cspan class=\"o\"\u003e=\u003c/span\u003e\u003cspan class=\"n\"\u003erole_name\u003c/span\u003e\u003cspan class=\"p\"\u003e)\u003c/span\u003e\n    \u003cspan class=\"c1\"\u003e# ...builds massive JSON output\n\u003c/span\u003e\u003c/code\u003e\u003c/pre\u003e\n\u003cdiv class=\"highlight__panel js-actions-panel\"\u003e\n\u003cdiv class=\"highlight__panel-action js-fullscreen-code-action\"\u003e\n    \u003csvg xmlns=\"http://www.w3.org/2000/svg\" width=\"20px\" height=\"20px\" viewbox=\"0 0 24 24\" class=\"highlight-action crayons-icon highlight-action--fullscreen-on\"\u003e\u003ctitle\u003eEnter fullscreen mode\u003c/title\u003e\n    \u003cpath d=\"M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z\"\u003e\u003c/path\u003e\n\u003c/svg\u003e\n\n    \u003csvg xmlns=\"http://www.w3.org/2000/svg\" width=\"20px\" height=\"20px\" viewbox=\"0 0 24 24\" class=\"highlight-action crayons-icon highlight-action--fullscreen-off\"\u003e\u003ctitle\u003eExit fullscreen mode\u003c/title\u003e\n    \u003cpath d=\"M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z\"\u003e\u003c/path\u003e\n\u003c/svg\u003e\n\n\u003c/div\u003e\n\u003c/div\u003e\n\u003c/div\u003e\n\n\n\n\u003cp\u003eThis produces 26,980 characters of JSON for an account with 90 roles. The LLM chokes on it.\u003c/p\u003e\n\n\u003cp\u003e\u003cstrong\u003eAfter (the fix):\u003c/strong\u003e\u003cbr\u003e\n\u003c/p\u003e\n\n\u003cdiv class=\"highlight js-code-highlight\"\u003e\n\u003cpre class=\"highlight python\"\u003e\u003ccode\u003e\u003cspan class=\"c1\"\u003e# FIX: Paginate and sort by relevance\n\u003c/span\u003e\u003cspan class=\"n\"\u003eall_roles\u003c/span\u003e \u003cspan class=\"o\"\u003e=\u003c/span\u003e \u003cspan class=\"p\"\u003e[]\u003c/span\u003e\n\u003cspan class=\"n\"\u003epaginator\u003c/span\u003e \u003cspan class=\"o\"\u003e=\u003c/span\u003e \u003cspan class=\"n\"\u003eiam\u003c/span\u003e\u003cspan class=\"p\"\u003e.\u003c/span\u003e\u003cspan class=\"nf\"\u003eget_paginator\u003c/span\u003e\u003cspan class=\"p\"\u003e(\u003c/span\u003e\u003cspan class=\"sh\"\u003e\"\u003c/span\u003e\u003cspan class=\"s\"\u003elist_roles\u003c/span\u003e\u003cspan class=\"sh\"\u003e\"\u003c/span\u003e\u003cspan class=\"p\"\u003e)\u003c/span\u003e\n\u003cspan class=\"k\"\u003efor\u003c/span\u003e \u003cspan class=\"n\"\u003epage\u003c/span\u003e \u003cspan class=\"ow\"\u003ein\u003c/span\u003e \u003cspan class=\"n\"\u003epaginator\u003c/span\u003e\u003cspan class=\"p\"\u003e.\u003c/span\u003e\u003cspan class=\"nf\"\u003epaginate\u003c/span\u003e\u003cspan class=\"p\"\u003e():\u003c/span\u003e\n    \u003cspan class=\"n\"\u003eall_roles\u003c/span\u003e\u003cspan class=\"p\"\u003e.\u003c/span\u003e\u003cspan class=\"nf\"\u003eextend\u003c/span\u003e\u003cspan class=\"p\"\u003e(\u003c/span\u003e\u003cspan class=\"n\"\u003epage\u003c/span\u003e\u003cspan class=\"p\"\u003e[\u003c/span\u003e\u003cspan class=\"sh\"\u003e\"\u003c/span\u003e\u003cspan class=\"s\"\u003eRoles\u003c/span\u003e\u003cspan class=\"sh\"\u003e\"\u003c/span\u003e\u003cspan class=\"p\"\u003e])\u003c/span\u003e\n\n\u003cspan class=\"c1\"\u003e# Filter service-linked roles (31 roles, can't modify anyway)\n\u003c/span\u003e\u003cspan class=\"n\"\u003eauditable_roles\u003c/span\u003e \u003cspan class=\"o\"\u003e=\u003c/span\u003e \u003cspan class=\"p\"\u003e[\u003c/span\u003e\n    \u003cspan class=\"n\"\u003er\u003c/span\u003e \u003cspan class=\"k\"\u003efor\u003c/span\u003e \u003cspan class=\"n\"\u003er\u003c/sp