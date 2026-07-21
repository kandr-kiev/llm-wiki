---
source_url: https://dev.to/lettstartdesign-official/bootstrap-5-grid-system-the-complete-guide-for-2026-17jj
ingested: 2026-07-21
sha256: a2899d98160a97454813951fd3b7616fc12d8a04a5b7a52682367c54509d5be3
blog_source: Dev Community
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Bootstrap 5 Grid System: The Complete Guide for 2026 - DEV Community</title>
    
    <link rel="preload" href="/reactions?article_id=4192846" as="fetch" crossorigin="same-origin">
    <link rel="canonical" href="https://dev.to/lettstartdesign-official/bootstrap-5-grid-system-the-complete-guide-for-2026-17jj" />
    <meta name="description" content="I&#39;ve been using Bootstrap&#39;s grid system since version 3. Watched it evolve from a 12-column... Tagged with bootstrap, css, webdev, frontend.">
    <meta name="keywords" content="bootstrap, css, webdev, frontend, software, coding, development, engineering, inclusive, community">

    <meta property="og:type" content="article" />
    <meta property="og:url" content="https://dev.to/lettstartdesign-official/bootstrap-5-grid-system-the-complete-guide-for-2026-17jj" />
    <meta property="og:title" content="Bootstrap 5 Grid System: The Complete Guide for 2026" />
    <meta property="og:description" content="I&#39;ve been using Bootstrap&#39;s grid system since version 3. Watched it evolve from a 12-column..." />
    <meta property="og:site_name" content="DEV Community" />
    <meta name="twitter:site" content="@thepracticaldev">
    <meta name="twitter:creator" content="@">
    <meta name="author-trust" content="0">
    <meta name="twitter:title" content="Bootstrap 5 Grid System: The Complete Guide for 2026">
    <meta name="twitter:description" content="I&#39;ve been using Bootstrap&#39;s grid system since version 3. Watched it evolve from a 12-column...">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:widgets:new-embed-design" content="on">
    <meta name="robots" content="max-snippet:-1, max-image-preview:large, max-video-preview:-1">
      <meta property="og:image" content="https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Ftm0e6r5t5uau8ehmjl75.png" />
      <meta name="twitter:image:src" content="https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Ftm0e6r5t5uau8ehmjl75.png">

      <meta name="last-updated" content="2026-07-21 05:22:45 UTC">
      <meta name="user-signed-in" content="false">
      <meta name="head-cached-at" content="1784611365">
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
      data-deployed-at="2026-07-20T20:34:47Z"
      data-latest-commit-id="ae359ff41b2a1a4b0918bb18012f1d9160a15765"
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
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" aria-labelledby="ahewspb5tkxa4be5r8jizujder15hk4n" class="crayons-icon"><title id="ahewspb5tkxa4be5r8jizujder15hk4n">Navigation menu</title>
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
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" aria-labelledby="aa3x8eocmznw7erg7hot4q2zlixx6pxr" aria-hidden="true" class="crayons-icon"><title id="aa3x8eocmznw7erg7hot4q2zlixx6pxr">Search</title>
    <path d="M18.031 16.617l4.283 4.282-1.415 1.415-4.282-4.283A8.96 8.96 0 0111 20c-4.968 0-9-4.032-9-9s4.032-9 9-9 9 4.032 9 9a8.96 8.96 0 01-1.969 5.617zm-2.006-.742A6.977 6.977 0 0018 11c0-3.868-3.133-7-7-7-3.868 0-7 3.132-7 7 0 3.867 3.132 7 7 7a6.977 6.977 0 004.875-1.975l.15-.15z"></path>
</svg>

            </button>

            <a class="crayons-header--search-brand-indicator" href="https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral" target="_blank" rel="noopener noreferrer">
                Powered by Algolia
                <svg xmlns="http://www.w3.org/2000/svg" id="Layer_1" width="24" height="24" viewBox="0 0 500 500.34" role="img" aria-labelledby="adhkx9qre9xcyqiaccnz6dk3dn3p33o3" aria-hidden="true" class="crayons-icon"><title id="adhkx9qre9xcyqiaccnz6dk3dn3p33o3">Search</title>
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
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" aria-labelledby="a4rlhkemh93a2sbm96nxlyit5mzok0r4" aria-hidden="true" class="crayons-icon c-btn__icon"><title id="a4rlhkemh93a2sbm96nxlyit5mzok0r4">Close</title><path d="M12 10.586l4.95-4.95 1.414 1.414-4.95 4.95 4.95 4.95-1.414 1.414-4.95-4.95-4.95 4.95-1.414-1.414 4.95-4.95-4.95-4.95L7.05 5.636l4.95 4.95z"></path></svg>

      </button>
    </header>

    <div class="p-2 js-navigation-links-container" id="authentication-hamburger-actions">
    </div>
  </div>
  <div class="hamburger__overlay js-hamburger-trigger"></div>
</div>


      <div id="active-broadcast" class="broadcast-wrapper"></div>
<div id="page-content" class="wrapper stories stories-show articletag-bootstrap articletag-css articletag-webdev articletag-frontend articleuser-4012143" data-current-page="stories-show">
  <div id="page-content-inner" data-internal-nav="false" data-viewable-id="4192846" data-viewable-type="Article">
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
    {"@context":"http://schema.org","@type":"Article","mainEntityOfPage":{"@type":"WebPage","@id":"https://dev.to/lettstartdesign-official/bootstrap-5-grid-system-the-complete-guide-for-2026-17jj"},"url":"https://dev.to/lettstartdesign-official/bootstrap-5-grid-system-the-complete-guide-for-2026-17jj","image":["https://media2.dev.to/dynamic/image/width=1080,height=1080,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Ftm0e6r5t5uau8ehmjl75.png","https://media2.dev.to/dynamic/image/width=1280,height=720,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Ftm0e6r5t5uau8ehmjl75.png","https://media2.dev.to/dynamic/image/width=1600,height=900,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Ftm0e6r5t5uau8ehmjl75.png"],"publisher":{"@context":"http://schema.org","@type":"Organization","name":"DEV Community","logo":{"@context":"http://schema.org","@type":"ImageObject","url":"https://media2.dev.to/dynamic/image/width=192,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png","width":"192","height":"192"}},"headline":"Bootstrap 5 Grid System: The Complete Guide for 2026","author":{"@context":"http://schema.org","@type":"Person","url":"https://dev.to/lettstartdesign-official","name":"Sakshi"},"datePublished":"2026-07-21T05:08:54Z","dateModified":"2026-07-21T05:08:54Z","mainEntity":{"@type":"DiscussionForumPosting","@id":"#article-discussion-4192846","headline":"Bootstrap 5 Grid System: The Complete Guide for 2026","text":"\u003cp\u003eI've been using Bootstrap's grid system since version 3. Watched it evolve from a 12-column float-based layout to a proper CSS Grid-powered system in Bootstrap 5. Most tutorials cover the basics — \u003ccode\u003ecol-md-6\u003c/code\u003e, \u003ccode\u003econtainer\u003c/code\u003e, \u003ccode\u003erow\u003c/code\u003e. This one covers the parts developers actually get wrong and the features most people don't know exist.\u003c/p\u003e\n\n\u003ch2\u003e\n  \u003ca name=\"the-container-options-nobody-explains-properly\" href=\"#the-container-options-nobody-explains-properly\"\u003e\n  \u003c/a\u003e\n  The Container Options Nobody Explains Properly\n\u003c/h2\u003e\n\n\u003cp\u003eBootstrap 5 has three container types and the difference matters for layout.\u003cbr\u003e\n\u003ccode\u003e.container\u003c/code\u003e — fixed max-width at each breakpoint. Your content has a maximum width and centers itself. Most common. Use for general page layouts.\u003c/p\u003e\n\n\u003cp\u003e\u003ccode\u003e.container-fluid\u003c/code\u003e — 100% width at all breakpoints. Full-width layouts. Use for dashboards where you want content to fill the screen.\u003c/p\u003e\n\n\u003cp\u003e\u003ccode\u003e.container-{breakpoint}\u003c/code\u003e — 100% width below the specified breakpoint, fixed max-width above it. This is the underused one.\u003cbr\u003e\n\u003c/p\u003e\n\n\u003cdiv class=\"highlight js-code-highlight\"\u003e\n\u003cpre class=\"highlight html\"\u003e\u003ccode\u003e\u003cspan class=\"c\"\u003e\u0026lt;!-- Full width on mobile, fixed width on desktop --\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"container-md\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"c\"\u003e\u0026lt;!-- 100% width on xs and sm, fixed max-width on md and above --\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\n\u003cspan class=\"c\"\u003e\u0026lt;!-- Full width until large screens --\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"container-lg\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"c\"\u003e\u0026lt;!-- Useful for dashboards that should fill tablet screens --\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\u003c/code\u003e\u003c/pre\u003e\n\u003cdiv class=\"highlight__panel js-actions-panel\"\u003e\n\u003cdiv class=\"highlight__panel-action js-fullscreen-code-action\"\u003e\n    \u003csvg xmlns=\"http://www.w3.org/2000/svg\" width=\"20px\" height=\"20px\" viewbox=\"0 0 24 24\" class=\"highlight-action crayons-icon highlight-action--fullscreen-on\"\u003e\u003ctitle\u003eEnter fullscreen mode\u003c/title\u003e\n    \u003cpath d=\"M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z\"\u003e\u003c/path\u003e\n\u003c/svg\u003e\n\n    \u003csvg xmlns=\"http://www.w3.org/2000/svg\" width=\"20px\" height=\"20px\" viewbox=\"0 0 24 24\" class=\"highlight-action crayons-icon highlight-action--fullscreen-off\"\u003e\u003ctitle\u003eExit fullscreen mode\u003c/title\u003e\n    \u003cpath d=\"M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z\"\u003e\u003c/path\u003e\n\u003c/svg\u003e\n\n\u003c/div\u003e\n\u003c/div\u003e\n\u003c/div\u003e\n\n\n\n\u003cp\u003eFor admin dashboards — \u003ccode\u003econtainer-fluid\u003c/code\u003e inside the main content area. For landing pages — \u003ccode\u003econtainer\u003c/code\u003e or \u003ccode\u003econtainer-lg\u003c/code\u003e. For hybrid layouts — \u003ccode\u003econtainer-{breakpoint}\u003c/code\u003e where the content transitions from full-width mobile to contained desktop.\u003c/p\u003e\n\n\u003ch2\u003e\n  \u003ca name=\"column-sizing-beyond-the-basics\" href=\"#column-sizing-beyond-the-basics\"\u003e\n  \u003c/a\u003e\n  Column Sizing — Beyond the Basics\n\u003c/h2\u003e\n\n\u003cp\u003eEvery developer knows \u003ccode\u003ecol-md-6\u003c/code\u003e. Few know all the sizing options.\u003cbr\u003e\n\u003c/p\u003e\n\n\u003cdiv class=\"highlight js-code-highlight\"\u003e\n\u003cpre class=\"highlight html\"\u003e\u003ccode\u003e\u003cspan class=\"c\"\u003e\u0026lt;!-- Auto-width — takes up as much space as content needs --\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"row\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col-auto\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003eAuto width\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003eFills remaining space\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\n\u003cspan class=\"c\"\u003e\u0026lt;!-- Equal width columns — no number needed --\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"row\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003eEqual\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003eEqual\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003eEqual\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\n\u003cspan class=\"c\"\u003e\u0026lt;!-- Mixed — auto + fill --\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"row align-items-center\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col-auto\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n    \u003cspan class=\"nt\"\u003e\u0026lt;img\u003c/span\u003e \u003cspan class=\"na\"\u003esrc=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"avatar.jpg\"\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"rounded-circle\"\u003c/span\u003e \u003cspan class=\"na\"\u003ewidth=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"40\"\u003c/span\u003e \u003cspan class=\"na\"\u003eheight=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"40\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n    \u003cspan class=\"nt\"\u003e\u0026lt;h6\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"mb-0\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003eUser Name\u003cspan class=\"nt\"\u003e\u0026lt;/h6\u0026gt;\u003c/span\u003e\n    \u003cspan class=\"nt\"\u003e\u0026lt;small\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"text-muted\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003euser@email.com\u003cspan class=\"nt\"\u003e\u0026lt;/small\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col-auto\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n    \u003cspan class=\"nt\"\u003e\u0026lt;span\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"badge bg-success\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003eActive\u003cspan class=\"nt\"\u003e\u0026lt;/span\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\u003c/code\u003e\u003c/pre\u003e\n\u003cdiv class=\"highlight__panel js-actions-panel\"\u003e\n\u003cdiv class=\"highlight__panel-action js-fullscreen-code-action\"\u003e\n    \u003csvg xmlns=\"http://www.w3.org/2000/svg\" width=\"20px\" height=\"20px\" viewbox=\"0 0 24 24\" class=\"highlight-action crayons-icon highlight-action--fullscreen-on\"\u003e\u003ctitle\u003eEnter fullscreen mode\u003c/title\u003e\n    \u003cpath d=\"M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z\"\u003e\u003c/path\u003e\n\u003c/svg\u003e\n\n    \u003csvg xmlns=\"http://www.w3.org/2000/svg\" width=\"20px\" height=\"20px\" viewbox=\"0 0 24 24\" class=\"highlight-action crayons-icon highlight-action--fullscreen-off\"\u003e\u003ctitle\u003eExit fullscreen mode\u003c/title\u003e\n    \u003cpath d=\"M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z\"\u003e\u003c/path\u003e\n\u003c/svg\u003e\n\n\u003c/div\u003e\n\u003c/div\u003e\n\u003c/div\u003e\n\n\n\n\u003cp\u003eThe \u003ccode\u003ecol-auto\u003c/code\u003e + \u003ccode\u003ecol\u003c/code\u003e pattern is the most useful for dashboard UI — avatar with auto width, name with fill, status badge with auto width. Eliminates manual width calculation for this common pattern.\u003c/p\u003e\n\n\u003ch2\u003e\n  \u003ca name=\"responsive-breakpoints-the-full-picture\" href=\"#responsive-breakpoints-the-full-picture\"\u003e\n  \u003c/a\u003e\n  Responsive Breakpoints — The Full Picture\n\u003c/h2\u003e\n\n\u003cp\u003eBootstrap 5 breakpoints:\u003cbr\u003e\n| Breakpoint | Class infix | Width |\u003cbr\u003e\n|---|---|---|\u003cbr\u003e\n| Extra small | None (xs) | \u0026lt; 576px |\u003cbr\u003e\n| Small | sm | ≥ 576px |\u003cbr\u003e\n| Medium | md | ≥ 768px |\u003cbr\u003e\n| Large | lg | ≥ 992px |\u003cbr\u003e\n| Extra large | xl | ≥ 1200px |\u003cbr\u003e\n| Extra extra large | xxl | ≥ 1400px |\u003c/p\u003e\n\n\u003cp\u003eThe one developers miss — \u003ccode\u003exxl\u003c/code\u003e. For large monitor dashboard layouts where you want a different column count above 1400px:\u003cbr\u003e\n\u003c/p\u003e\n\n\u003cdiv class=\"highlight js-code-highlight\"\u003e\n\u003cpre class=\"highlight html\"\u003e\u003ccode\u003e\u003cspan class=\"c\"\u003e\u0026lt;!-- 1 col mobile, 2 col tablet, 3 col desktop, 4 col large desktop --\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"row g-4\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col-12 col-md-6 col-lg-4 col-xxl-3\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n    \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"stat-card card\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e...\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\u003c/code\u003e\u003c/pre\u003e\n\u003cdiv class=\"highlight__panel js-actions-panel\"\u003e\n\u003cdiv class=\"highlight__panel-action js-fullscreen-code-action\"\u003e\n    \u003csvg xmlns=\"http://www.w3.org/2000/svg\" width=\"20px\" height=\"20px\" viewbox=\"0 0 24 24\" class=\"highlight-action crayons-icon highlight-action--fullscreen-on\"\u003e\u003ctitle\u003eEnter fullscreen mode\u003c/title\u003e\n    \u003cpath d=\"M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z\"\u003e\u003c/path\u003e\n\u003c/svg\u003e\n\n    \u003csvg xmlns=\"http://www.w3.org/2000/svg\" width=\"20px\" height=\"20px\" viewbox=\"0 0 24 24\" class=\"highlight-action crayons-icon highlight-action--fullscreen-off\"\u003e\u003ctitle\u003eExit fullscreen mode\u003c/title\u003e\n    \u003cpath d=\"M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z\"\u003e\u003c/path\u003e\n\u003c/svg\u003e\n\n\u003c/div\u003e\n\u003c/div\u003e\n\u003c/div\u003e\n\n\n\n\u003cp\u003eFor admin dashboards displayed on large monitors — \u003ccode\u003ecol-xxl\u003c/code\u003e prevents wide cards that look wrong on 1440px+ screens.\u003c/p\u003e\n\n\u003ch2\u003e\n  \u003ca name=\"gutters-the-bootstrap-5-improvement\" href=\"#gutters-the-bootstrap-5-improvement\"\u003e\n  \u003c/a\u003e\n  Gutters — The Bootstrap 5 Improvement\n\u003c/h2\u003e\n\n\u003cp\u003eBootstrap 5 replaced padding-based gutters with the \u003ccode\u003eg-*\u003c/code\u003e utility. Most developers know \u003ccode\u003eg-4\u003c/code\u003e but miss the directional variants.\u003cbr\u003e\n\u003c/p\u003e\n\n\u003cdiv class=\"highlight js-code-highlight\"\u003e\n\u003cpre class=\"highlight html\"\u003e\u003ccode\u003e\u003cspan class=\"c\"\u003e\u0026lt;!-- Horizontal gutters only — useful for tight vertical layouts --\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"row gx-4\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col-md-6\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e...\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col-md-6\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e...\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\n\u003cspan class=\"c\"\u003e\u0026lt;!-- Vertical gutters only — when columns wrap and you need row spacing --\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"row gy-3\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col-md-4\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e...\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col-md-4\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e...\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col-md-4\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e...\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\n\u003cspan class=\"c\"\u003e\u0026lt;!-- Both directions — most common for card grids --\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"row g-4\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col-md-4\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e...\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\u003c/code\u003e\u003c/pre\u003e\n\u003cdiv class=\"highlight__panel js-actions-panel\"\u003e\n\u003cdiv class=\"highlight__panel-action js-fullscreen-code-action\"\u003e\n    \u003csvg xmlns=\"http://www.w3.org/2000/svg\" width=\"20px\" height=\"20px\" viewbox=\"0 0 24 24\" class=\"highlight-action crayons-icon highlight-action--fullscreen-on\"\u003e\u003ctitle\u003eEnter fullscreen mode\u003c/title\u003e\n    \u003cpath d=\"M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z\"\u003e\u003c/path\u003e\n\u003c/svg\u003e\n\n    \u003csvg xmlns=\"http://www.w3.org/2000/svg\" width=\"20px\" height=\"20px\" viewbox=\"0 0 24 24\" class=\"highlight-action crayons-icon highlight-action--fullscreen-off\"\u003e\u003ctitle\u003eExit fullscreen mode\u003c/title\u003e\n    \u003cpath d=\"M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z\"\u003e\u003c/path\u003e\n\u003c/svg\u003e\n\n\u003c/div\u003e\n\u003c/div\u003e\n\u003c/div\u003e\n\n\n\n\u003cp\u003eFor stat card grids — \u003ccode\u003eg-4\u003c/code\u003e (1.5rem gap both directions). For form layouts — \u003ccode\u003egx-3 gy-2\u003c/code\u003e (tighter vertical, comfortable horizontal). For full-width dashboard sections — \u003ccode\u003egx-0\u003c/code\u003e (no horizontal gap between edge-to-edge panels).\u003c/p\u003e\n\n\u003ch2\u003e\n  \u003ca name=\"offset-and-order-when-you-need-them\" href=\"#offset-and-order-when-you-need-them\"\u003e\n  \u003c/a\u003e\n  Offset and Order — When You Need Them\n\u003c/h2\u003e\n\n\u003cp\u003eOffsets push columns to the right. Useful for centering a single column or creating asymmetric layouts.\u003cbr\u003e\n\u003c/p\u003e\n\n\u003cdiv class=\"highlight js-code-highlight\"\u003e\n\u003cpre class=\"highlight html\"\u003e\u003ccode\u003e\u003cspan class=\"c\"\u003e\u0026lt;!-- Centered single column — login page pattern --\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"row justify-content-center\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col-md-6 col-lg-4\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n    \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"card\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n      \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"card-body\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n        \u003cspan class=\"c\"\u003e\u0026lt;!-- Login form --\u0026gt;\u003c/span\u003e\n      \u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n    \u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\n\u003cspan class=\"c\"\u003e\u0026lt;!-- Offset — push column right --\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"row\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col-md-4 offset-md-4\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n    \u003cspan class=\"c\"\u003e\u0026lt;!-- Centered on md+ --\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\u003c/code\u003e\u003c/pre\u003e\n\u003cdiv class=\"highlight__panel js-actions-panel\"\u003e\n\u003cdiv class=\"highlight__panel-action js-fullscreen-code-action\"\u003e\n    \u003csvg xmlns=\"http://www.w3.org/2000/svg\" width=\"20px\" height=\"20px\" viewbox=\"0 0 24 24\" class=\"highlight-action crayons-icon highlight-action--fullscreen-on\"\u003e\u003ctitle\u003eEnter fullscreen mode\u003c/title\u003e\n    \u003cpath d=\"M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z\"\u003e\u003c/path\u003e\n\u003c/svg\u003e\n\n    \u003csvg xmlns=\"http://www.w3.org/2000/svg\" width=\"20px\" height=\"20px\" viewbox=\"0 0 24 24\" class=\"highlight-action crayons-icon highlight-action--fullscreen-off\"\u003e\u003ctitle\u003eExit fullscreen mode\u003c/title\u003e\n    \u003cpath d=\"M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z\"\u003e\u003c/path\u003e\n\u003c/svg\u003e\n\n\u003c/div\u003e\n\u003c/div\u003e\n\u003c/div\u003e\n\n\n\n\u003cp\u003eOrder utilities reorder columns visually without changing HTML order — important for accessibility where logical reading order matters:\u003cbr\u003e\n\u003c/p\u003e\n\n\u003cdiv class=\"highlight js-code-highlight\"\u003e\n\u003cpre class=\"highlight html\"\u003e\u003ccode\u003e\u003cspan class=\"c\"\u003e\u0026lt;!-- On mobile: image first, text second --\u0026gt;\u003c/span\u003e\n\u003cspan class=\"c\"\u003e\u0026lt;!-- On desktop: text first, image second --\u0026gt;\u003c/span\u003e\n\u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"row align-items-center\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col-12 col-md-6 order-2 order-md-1\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n    \u003cspan class=\"nt\"\u003e\u0026lt;h2\u0026gt;\u003c/span\u003eHeadline\u003cspan class=\"nt\"\u003e\u0026lt;/h2\u0026gt;\u003c/span\u003e\n    \u003cspan class=\"nt\"\u003e\u0026lt;p\u0026gt;\u003c/span\u003eDescription text\u003cspan class=\"nt\"\u003e\u0026lt;/p\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;div\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"col-12 col-md-6 order-1 order-md-2\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n    \u003cspan class=\"nt\"\u003e\u0026lt;img\u003c/span\u003e \u003cspan class=\"na\"\u003esrc=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"illustration.svg\"\u003c/span\u003e \u003cspan class=\"na\"\u003eclass=\u003c/span\u003e\u003cspan class=\"s\"\u003e\"img-fluid\"\u003c/span\u003e\u003cspan class=\"nt\"\u003e\u0026gt;\u003c/span\u003e\n  \u003cspan class=\"nt\"\u003e\u0026lt;/div\u0026gt;\u003c/span\u003e\n\