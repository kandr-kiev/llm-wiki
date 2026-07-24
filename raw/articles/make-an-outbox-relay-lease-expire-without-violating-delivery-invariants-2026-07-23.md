---
source_url: https://dev.to/robinzzz/make-an-outbox-relay-lease-expire-without-violating-delivery-invariants-30dh
ingested: 2026-07-23
sha256: d121bb33c0e8b54d2b937f70c72dd0d4f3ee9e70bb74bea602dbacbf14b4869b
blog_source: Dev Community
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Make an Outbox Relay Lease Expire Without Violating Delivery Invariants - DEV Community</title>
    
    <link rel="preload" href="/reactions?article_id=4214983" as="fetch" crossorigin="same-origin">
    <link rel="canonical" href="https://dev.to/robinzzz/make-an-outbox-relay-lease-expire-without-violating-delivery-invariants-30dh" />
    <meta name="description" content="Model the duplicate delivery created by an expired relay lease and define the invariants consumers must preserve. Tagged with distributedsystems, backend, architecture, testing.">
    <meta name="keywords" content="distributedsystems, backend, architecture, testing, software, coding, development, engineering, inclusive, community">

    <meta property="og:type" content="article" />
    <meta property="og:url" content="https://dev.to/robinzzz/make-an-outbox-relay-lease-expire-without-violating-delivery-invariants-30dh" />
    <meta property="og:title" content="Make an Outbox Relay Lease Expire Without Violating Delivery Invariants" />
    <meta property="og:description" content="Model the duplicate delivery created by an expired relay lease and define the invariants consumers must preserve." />
    <meta property="og:site_name" content="DEV Community" />
    <meta name="twitter:site" content="@thepracticaldev">
    <meta name="twitter:creator" content="@">
    <meta name="author-trust" content="0">
    <meta name="twitter:title" content="Make an Outbox Relay Lease Expire Without Violating Delivery Invariants">
    <meta name="twitter:description" content="Model the duplicate delivery created by an expired relay lease and define the invariants consumers must preserve.">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:widgets:new-embed-design" content="on">
    <meta name="robots" content="max-snippet:-1, max-image-preview:large, max-video-preview:-1">
      <meta property="og:image" content="https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Floq25o5nhbj4v6acvpog.png" />
      <meta name="twitter:image:src" content="https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Floq25o5nhbj4v6acvpog.png">

      <meta name="last-updated" content="2026-07-23 11:57:20 UTC">
      <meta name="user-signed-in" content="false">
      <meta name="head-cached-at" content="1784807840">
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
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" aria-labelledby="akw5rs4cs0zovi178pzt8xkiwdnpgd78" class="crayons-icon"><title id="akw5rs4cs0zovi178pzt8xkiwdnpgd78">Navigation menu</title>
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
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" aria-labelledby="aehbfqorfkqscfos8sp2xqg9eiltbjxm" aria-hidden="true" class="crayons-icon"><title id="aehbfqorfkqscfos8sp2xqg9eiltbjxm">Search</title>
    <path d="M18.031 16.617l4.283 4.282-1.415 1.415-4.282-4.283A8.96 8.96 0 0111 20c-4.968 0-9-4.032-9-9s4.032-9 9-9 9 4.032 9 9a8.96 8.96 0 01-1.969 5.617zm-2.006-.742A6.977 6.977 0 0018 11c0-3.868-3.133-7-7-7-3.868 0-7 3.132-7 7 0 3.867 3.132 7 7 7a6.977 6.977 0 004.875-1.975l.15-.15z"></path>
</svg>

            </button>

            <a class="crayons-header--search-brand-indicator" href="https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral" target="_blank" rel="noopener noreferrer">
                Powered by Algolia
                <svg xmlns="http://www.w3.org/2000/svg" id="Layer_1" width="24" height="24" viewBox="0 0 500 500.34" role="img" aria-labelledby="a8gixusrfeq77col8o66c1lalh4sdcp9" aria-hidden="true" class="crayons-icon"><title id="a8gixusrfeq77col8o66c1lalh4sdcp9">Search</title>
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
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" aria-labelledby="am8sgd2y6tgwoc5paeoa6q0bgiqsnlv5" aria-hidden="true" class="crayons-icon c-btn__icon"><title id="am8sgd2y6tgwoc5paeoa6q0bgiqsnlv5">Close</title><path d="M12 10.586l4.95-4.95 1.414 1.414-4.95 4.95 4.95 4.95-1.414 1.414-4.95-4.95-4.95 4.95-1.414-1.414 4.95-4.95-4.95-4.95L7.05 5.636l4.95 4.95z"></path></svg>

      </button>
    </header>

    <div class="p-2 js-navigation-links-container" id="authentication-hamburger-actions">
    </div>
  </div>
  <div class="hamburger__overlay js-hamburger-trigger"></div>
</div>


      <div id="active-broadcast" class="broadcast-wrapper"></div>
<div id="page-content" class="wrapper stories stories-show articletag-distributedsystems articletag-backend articletag-architecture articletag-testing articleuser-4022699" data-current-page="stories-show">
  <div id="page-content-inner" data-internal-nav="false" data-viewable-id="4214983" data-viewable-type="Article">
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
    {"@context":"http://schema.org","@type":"Article","mainEntityOfPage":{"@type":"WebPage","@id":"https://dev.to/robinzzz/make-an-outbox-relay-lease-expire-without-violating-delivery-invariants-30dh"},"url":"https://dev.to/robinzzz/make-an-outbox-relay-lease-expire-without-violating-delivery-invariants-30dh","image":["https://media2.dev.to/dynamic/image/width=1080,height=1080,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Floq25o5nhbj4v6acvpog.png","https://media2.dev.to/dynamic/image/width=1280,height=720,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Floq25o5nhbj4v6acvpog.png","https://media2.dev.to/dynamic/image/width=1600,height=900,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Floq25o5nhbj4v6acvpog.png"],"publisher":{"@context":"http://schema.org","@type":"Organization","name":"DEV Community","logo":{"@context":"http://schema.org","@type":"ImageObject","url":"https://media2.dev.to/dynamic/image/width=192,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png","width":"192","height":"192"}},"headline":"Make an Outbox Relay Lease Expire Without Violating Delivery Invariants","author":{"@context":"http://schema.org","@type":"Person","url":"https://dev.to/robinzzz","name":"Robin"},"datePublished":"2026-07-23T11:55:13Z","dateModified":"2026-07-23T11:55:13Z"}
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
      <img aria_hidden="true" height="32" width="32" src="https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg" />
    </span>
    <span class="crayons-reaction__count" id="reaction-number-raised_hands"><span class="bg-base-40 opacity-25 p-2 inline-block radius-default"></span></span>

    <span data-testid="tooltip" class="crayons-tooltip__content">
      Raised Hands
    </span>
</button>

        <button
  id="reaction-butt-fire"
  name="Fire"
  aria-label="Fire"
  aria-pressed="false"
  class="crayons-reaction crayons-tooltip__activator relative pt-2 pr-2 pb-1 pl-2"
  data-category="fire">
    <span class="crayons-reaction__icon crayons-reaction__icon--inactive p-0">
      <img aria_hidden="true" height="32" width="32" src="https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg" />
    </span>
    <span class="crayons-reaction__count" id="reaction-number-fire"><span class="bg-base-40 opacity-25 p-2 inline-block radius-default"></span></span>

    <span data-testid="tooltip" class="crayons-tooltip__content">
      Fire
    </span>
</button>

    </div>
  </div>
</div>

<button
  id="reaction-butt-comment"
  aria-label="Jump to Comments"
  aria-pressed="false"
  class="crayons-reaction crayons-reaction--comment crayons-tooltip__activator relative"
  data-category="comment">
    <span class="crayons-reaction__icon crayons-reaction__icon--borderless crayons-reaction__icon--inactive">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" aria-hidden="true" class="crayons-icon">
    <path d="M10 3h4a8 8 0 010 16v3.5c-5-2-12-5-12-11.5a8 8 0 018-8zm2 14h2a6 6 0 000-12h-4a6 6 0 00-6 6c0 3.61 2.462 5.966 8 8.48V17z"></path>
</svg>

    </span>
    <span class="crayons-reaction__count" id="reaction-number-comment" data-count="0">
      <span class="bg-base-40 opacity-25 p-2 inline-block radius-default"></span>
    </span>

    <span data-testid="tooltip" class="crayons-tooltip__content">
      Jump to Comments
    </span>
</button>

<button
  id="reaction-butt-readinglist"
  aria-label="Add to reading list"
  aria-pressed="false"
  class="crayons-reaction crayons-reaction--readinglist crayons-tooltip__activator relative"
  data-category="readinglist">
    <span class="crayons-reaction__icon crayons-reaction__icon--borderless crayons-reaction__icon--inactive">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" aria-hidden="true" class="crayons-icon">
    <path d="M5 2h14a1 1 0 011 1v19.143a.5.5 0 01-.766.424L12 18.03l-7.234 4.536A.5.5 0 014 22.143V3a1 1 0 011-1zm13 2H6v15.432l6-3.761 6 3.761V4z"></path>
</svg>

    </span>
    <span class="crayons-reaction__count" id="reaction-number-readinglist"><span class="bg-base-40 opacity-25 p-2 inline-block radius-default"></span></span>

    <span data-testid="tooltip" class="crayons-tooltip__content">
      Save
    </span>
</button>


<button
  id="reaction-butt-boost"
  aria-label="Boost"
  aria-pressed="false"
  class="crayons-reaction crayons-reaction--boost crayons-tooltip__activator relative">
    <span class="crayons-reaction__icon crayons-reaction__icon--borderless crayons-reaction__icon--inactive">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img" aria-hidden="true" class="crayons-icon" width="24" height="24">
  <path transform="translate(24,0) scale(-1,1)" d="M6 4H21C21.5523 4 22 4.44772 22 5V12H20V6H6V9L1 5L6 1V4ZM18 20H3C2.44772 20 2 19.5523 2 19V12H4V18H18V15L23 19L18 23V20Z"></path>
</svg>

    </span>
    <span data-testid="tooltip" class="crayons-tooltip__content">
      Boost
    </span>
</button>


      <div class="only-sidebar-menu-item">
        <div id="mod-actions-menu-btn-area" class="print-hidden trusted-visible-block align-center">
        </div>
      </div>
      <div class="align-center m:relative">
        <button id="article-show-more-button" aria-controls="article-show-more-dropdown" aria-expanded="false" aria-haspopup="true" class="dropbtn crayons-btn crayons-btn--ghost-dimmed crayons-btn--icon-rounded" aria-label="Share post options">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" role="img" aria-labelledby="ahpagj7by7khc2z41mz0yfqdal5q7hgm" aria-hidden="true" class="crayons-icon dropdown-icon"><title id="ahpagj7by7khc2z41mz0yfqdal5q7hgm">More...</title><path fill-rule="evenodd" clip-rule="evenodd" d="M7 12a2 2 0 11-4 0 2 2 0 014 0zm7 0a2 2 0 11-4 0 2 2 0 014 0zm5 2a2 2 0 100-4 2 2 0 000 4z"></path></svg>

        </button>

        <div id="article-show-more-dropdown" class="crayons-dropdown side-bar left-2 right-2 m:right-auto m:left-100 s:left-auto mb-1 m:mb-0 top-unset bottom-100 m:top-0 m:bottom-unset">
          <div>
            <button
              id="copy-post-url-button"
              class="flex justify-between crayons-link crayons-link--block w-100 bg-transparent border-0"
              data-postUrl="https://dev.to/robinzzz/make-an-outbox-relay-lease-expire-without-violating-delivery-invariants-30dh">
              <span class="fw-bold">Copy link</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" id="article-copy-icon" role="img" aria-labelledby="aairnto3k9zdl7gr4wyrx1wfm6jkmoa2" aria-hidden="true" class="crayons-icon mx-2 shrink-0"><title id="aairnto3k9zdl7gr4wyrx1wfm6jkmoa2">Copy link</title>
    <path d="M7 6V3a1 1 0 011-1h12a1 1 0 011 1v14a1 1 0 01-1 1h-3v3c0 .552-.45 1-1.007 1H4.007A1 1 0 013 21l.003-14c0-.552.45-1 1.007-1H7zm2 0h8v10h2V4H9v2zm-2 5v2h6v-2H7zm0 4v2h6v-2H7z"></path>
</svg>

            </button>
            <div id="article-copy-link-announcer" aria-live="polite" class="crayons-notice crayons-notice--success my-2 p-1" aria-live="polite" hidden>Copied to Clipboard</div>
          </div>

          <div class="Desktop-only">
            <a
              target="_blank"
              class="crayons-link crayons-link--block"
              rel="noopener"
              href='https://twitter.com/intent/tweet?text=%22Make%20an%20Outbox%20Relay%20Lease%20Expire%20Without%20Violating%20Delivery%20Invariants%22%20by%20Robin%20%23DEVCommunity%20https%3A%2F%2Fdev.to%2Frobinzzz%2Fmake-an-outbox-relay-lease-expire-without-violating-delivery-invariants-30dh'>
              Share to X
            </a>
            <a
              target="_blank"
              class="crayons-link crayons-link--block"
              rel="noopener"
              href="https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fdev.to%2Frobinzzz%2Fmake-an-outbox-relay-lease-expire-without-violating-delivery-invariants-30dh&title=Make%20an%20Outbox%20Relay%20Lease%20Expire%20Without%20Violating%20Delivery%20Invariants&summary=Model%20the%20duplicate%20delivery%20created%20by%20an%20expired%20relay%20lease%20and%20define%20the%20invariants%20consumers%20must%20preserve.&source=DEV%20Community">
              Share to LinkedIn
            </a>
            <a
              target="_blank"
              class="crayons-link crayons-link--block"
              rel="noopener"
              href="https://www.facebook.com/sharer.php?u=https%3A%2F%2Fdev.to%2Frobinzzz%2Fmake-an-outbox-relay-lease-expire-without-violating-delivery-invariants-30dh">
              Share to Facebook
            </a>
            <a
              target="_blank"
              class="crayons-link crayons-link--block"
              rel="noopener"
              href="https://s2f.kytta.dev/?text=https%3A%2F%2Fdev.to%2Frobinzzz%2Fmake-an-outbox-relay-lease-expire-without-violating-delivery-invariants-30dh">
              Share to Mastodon
            </a>
          </div>

          <web-share-wrapper shareurl="https://dev.to/robinzzz/make-an-outbox-relay-lease-expire-without-violating-delivery-invariants-30dh" sharetitle="Make an Outbox Relay Lease Expire Without Violating Delivery Invariants" sharetext="Model the duplicate delivery created by an expired relay lease and define the invariants consumers must preserve." template="web-share-button">
          </web-share-wrapper>
          <template id="web-share-button">
            <a href="#" class="dropdown-link-row crayons-link crayons-link--block">Share Post via...</a>
          </template>

          <a href="/report-abuse" class="crayons-link crayons-link--block" id="ReportButtonAuthor">Report Abuse</a>
        </div>
      </div>
    </div>
  </div>

    </aside>

    <main id="main-content" class="crayons-layout__content grid gap-4">
      <div class="article-wrapper">


        <article class="crayons-card crayons-article mb-4"
          id="article-show-container"
          data-article-id="4214983"
          data-article-slug="make-an-outbox-relay-lease-expire-without-violating-delivery-invariants-30dh"
          data-author-id="4022699"
          data-author-name="Robin"
          data-author-username="robinzzz"
          data-co-author-ids=""
          data-path="/robinzzz/make-an-outbox-relay-lease-expire-without-violating-delivery-invariants-30dh"
          data-pin-path="/stories/feed/pinned_article"
          data-pinned-article-id=""
          data-published="true"
          data-scheduled="false"
          lang=en
           >
          <script>
            try {
              if(localStorage) {
                let currentUser = localStorage.getItem('current_user');

                if (currentUser) {
                  currentUser = JSON.parse(currentUser);
                  if (currentUser.id === 4022699) {
                    document.getElementById('article-show-container').classList.add('current-user-is-article-author');
                  }
                }
              }
            } catch (e) {
              console.error(e);
            }
          </script>
          <header class="crayons-article__header" id="main-title">

            <div class="crayons-article__header__meta">
              <div class="flex s:items-start flex-col s:flex-row">
                <div id="action-space" class="crayons-article__actions mb-4 s:mb-0 s:order-last"></div>
                <div class="flex flex-1 mb-5 items-start">
                  <div class="relative">
                      <a href="/robinzzz"><img class="radius-full align-middle" src="https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F4022699%2F18662e47-418f-402e-badd-5dea93f6cf78.jpg" width="40" height="40" alt="Robin" /></a>
                  </div>
                  <div class="pl-3 flex-1">
                    <a href="/robinzzz" class="crayons-link fw-bold">Robin</a>
                    
                    <p class="fs-xs color-base-60">
                        Posted on <time datetime="2026-07-23T11:55:13Z" class="date-no-year">Jul 23</time>


                    </p>
                  </div>
                </div>
              </div>

              

              <h1 class=" fs-3xl m:fs-4xl l:fs-5xl fw-bold s:fw-heavy lh-tight mb-2 long">
                Make an Outbox Relay Lease Expire Without Violating Delivery Invariants
              </h1>
              
                  <div class="spec__tags flex flex-wrap">
                      <a class="crayons-tag   " style="
        --tag-bg: rgba(235, 223, 55, 0.10);
        --tag-prefix: #ebdf37;
        --tag-bg-hover: rgba(235, 223, 55, 0.10);
        --tag-prefix-hover: #ebdf37;
      " href="/t/architecture"><span class="crayons-tag__prefix">#</span>architecture</a>
                      <a class="crayons-tag   " style="
        --tag-bg: rgba(64, 78, 211, 0.10);
        --tag-prefix: #404ED3;
        --tag-bg-hover: rgba(64, 78, 211, 0.10);
        --tag-prefix-hover: #404ED3;
      " href="/t/backend"><span class="crayons-tag__prefix">#</span>backend</a>
                      <a class="crayons-tag   " style="
        --tag-bg: rgba(0, 102, 102, 0.10);
        --tag-prefix: #006666;
        --tag-bg-hover: rgba(0, 102, 102, 0.10);
        --tag-prefix-hover: #006666;
      " href="/t/distributedsystems"><span class="crayons-tag__prefix">#</span>distributedsystems</a>
                      <a class="crayons-tag   " style="
        --tag-bg: rgba(1, 155, 101, 0.10);
        --tag-prefix: #019b65;
        --tag-bg-hover: rgba(1, 155, 101, 0.10);
        --tag-prefix-hover: #019b65;
      " href="/t/testing"><span class="crayons-tag__prefix">#</span>testing</a>
                  </div>
            </div>
          </header>

          <div class="crayons-article__main ">
            <div class="crayons-article__body text-styles spec__body" data-article-id="4214983"
              id="article-body">
                <p>Relay A claims outbox row 42 and publishes its message. Before A records completion, its lease expires. Relay B claims row 42 and publishes it again. Both relays behaved according to their local state; the broker received a duplicate.</p>

<p>A lease prevents unlimited concurrent ownership. It cannot create exactly-once delivery across a database and broker without a shared transaction.</p>

<p>The honest contract is:</p>

<blockquote>
<p>Every committed outbox event is eventually offered at least once; consumers preserve business invariants under duplicate offers.</p>
</blockquote>

<h2>
  <a name="state-model" href="#state-model">
  </a>
  State model
</h2>



<div class="highlight js-code-highlight">
<pre class="highlight plaintext"><code>pending
  -&gt; leased(owner, token, expires_at)
  -&gt; published

leased --expiry--&gt; claimable
leased --failure--&gt; claimable
</code></pre>
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>



<p>A fencing token increments on every claim:<br>
</p>

<div class="highlight js-code-highlight">
<pre class="highlight sql"><code><span class="k">UPDATE</span> <span class="n">outbox</span>
<span class="k">SET</span> <span class="n">lease_owner</span> <span class="o">=</span> <span class="p">:</span><span class="n">worker</span><span class="p">,</span>
    <span class="n">lease_token</span> <span class="o">=</span> <span class="n">lease_token</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span>
    <span class="n">lease_expires_at</span> <span class="o">=</span> <span class="n">now</span><span class="p">()</span> <span class="o">+</span> <span class="n">interval</span> <span class="s1">'30 seconds'</span>
<span class="k">WHERE</span> <span class="n">id</span> <span class="o">=</span> <span class="p">:</span><span class="n">id</span>
  <span class="k">AND</span> <span class="n">published_at</span> <span class="k">IS</span> <span class="k">NULL</span>
  <span class="k">AND</span> <span class="p">(</span><span class="n">lease_expires_at</span> <span class="k">IS</span> <span class="k">NULL</span> <span class="k">OR</span> <span class="n">lease_expires_at</span> <span class="o">&lt;</span> <span class="n">now</span><span class="p">())</span>
<span class="n">RETURNING</span> <span class="n">id</span><span class="p">,</span> <span class="n">event_id</span><span class="p">,</span> <span class="n">payload</span><span class="p">,</span> <span class="n">lease_token</span><span class="p">;</span>
</code></pre>
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>



<p>Completion is conditional:<br>
</p>

<div class="highlight js-code-highlight">
<pre class="highlight sql"><code><span class="k">UPDATE</span> <span class="n">outbox</span>
<span class="k">SET</span> <span class="n">published_at</span> <span class="o">=</span> <span class="n">now</span><span class="p">()</span>
<span class="k">WHERE</span> <span class="n">id</span> <span class="o">=</span> <span class="p">:</span><span class="n">id</span>
  <span class="k">AND</span> <span class="n">lease_owner</span> <span class="o">=</span> <span class="p">:</span><span class="n">worker</span>
  <span class="k">AND</span> <span class="n">lease_token</span> <span class="o">=</span> <span class="p">:</span><span class="n">token</span>
  <span class="k">AND</span> <span class="n">published_at</span> <span class="k">IS</span> <span class="k">NULL</span><span class="p">;</span>
</code></pre>
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>



<p>The token stops stale relay A from marking B's newer lease complete. It does not retract A's already published message.</p>

<h2>
  <a name="minimal-eventorder-simulator" href="#minimal-eventorder-simulator">
  </a>
  Minimal event-order simulator
</h2>

<p>Model actions instead of threads:<br>
</p>

<div class="highlight js-code-highlight">
<pre class="highlight python"><code><span class="n">state</span> <span class="o">=</span> <span class="p">{</span>
    <span class="sh">"</span><span class="s">token</span><span class="sh">"</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">lease</span><span class="sh">"</span><span class="p">:</span> <span class="bp">None</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">published</span><span class="sh">"</span><span class="p">:</span> <span class="bp">False</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">broker</span><span class="sh">"</span><span class="p">:</span> <span class="p">[],</span>
<span class="p">}</span>


<span class="k">def</span> <span class="nf">claim</span><span c