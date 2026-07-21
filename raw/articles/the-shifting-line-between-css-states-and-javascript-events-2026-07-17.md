---
source_url: https://css-tricks.com/css-states-and-javascript-events/
ingested: 2026-07-17
sha256: 599baf74e83e5168cf9ef37ba9781aaf0752a92f2e27a02389723178bec8aa35
blog_source: CSS Tricks
---
<!doctype html>
<html lang="en" id="top-of-site" class="js">

<head>
<title>The Shifting Line Between CSS States and JavaScript Events | CSS-Tricks</title>

  <meta charset="utf-8">

  <meta name="viewport" content="width=device-width">

  
  


  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="manifest" href="/manifest.json">
  <meta name="theme-color" content="#ff7a18">

  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="CSS-Tricks Search">

  <link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="https://css-tricks.com/feed/">

  <link rel="preconnect" href="https://s3.buysellads.com">
  <link rel="dns-prefetch" href="https://s3.buysellads.com">
  <link rel="preconnect" href="https://srv.buysellads.com">
  <link rel="dns-prefetch" href="https://srv.buysellads.com">
  <link rel="preconnect" href="https://static.codepen.io">
  <link rel="dns-prefetch" href="https://static.codepen.io">

  
  
<!-- Search Engine Optimization by Rank Math - https://rankmath.com/ -->
<meta name="description" content="CSS has always had pseudo-classes that style things based on user interactions. Recent features, however, are blurring the line between what CSS &quot;listens&quot; for and how they are alternatives to what Javascript typically listens for."/>
<meta name="robots" content="follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large"/>
<link rel="canonical" href="https://css-tricks.com/css-states-and-javascript-events/" />
<meta property="og:locale" content="en_US" />
<meta property="og:type" content="article" />
<meta property="og:title" content="The Shifting Line Between CSS States and JavaScript Events | CSS-Tricks" />
<meta property="og:description" content="CSS has always had pseudo-classes that style things based on user interactions. Recent features, however, are blurring the line between what CSS &quot;listens&quot; for and how they are alternatives to what Javascript typically listens for." />
<meta property="og:url" content="https://css-tricks.com/css-states-and-javascript-events/" />
<meta property="og:site_name" content="CSS-Tricks" />
<meta property="article:publisher" content="https://www.facebook.com/CSSTricks" />
<meta property="article:tag" content="pseudo elements" />
<meta property="article:tag" content="state" />
<meta property="article:section" content="Articles" />
<meta property="og:updated_time" content="2026-06-30T19:44:13-06:00" />
<meta property="og:image" content="https://i0.wp.com/css-tricks.com/wp-content/uploads/2018/07/state-management.jpg" />
<meta property="og:image:secure_url" content="https://i0.wp.com/css-tricks.com/wp-content/uploads/2018/07/state-management.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="600" />
<meta property="og:image:alt" content="The Shifting Line Between CSS States and JavaScript Events" />
<meta property="og:image:type" content="image/jpeg" />
<meta property="article:published_time" content="2026-06-29T07:03:32-06:00" />
<meta property="article:modified_time" content="2026-06-30T19:44:13-06:00" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="The Shifting Line Between CSS States and JavaScript Events | CSS-Tricks" />
<meta name="twitter:description" content="CSS has always had pseudo-classes that style things based on user interactions. Recent features, however, are blurring the line between what CSS &quot;listens&quot; for and how they are alternatives to what Javascript typically listens for." />
<meta name="twitter:site" content="@CSS" />
<meta name="twitter:creator" content="@dxnnydotfun" />
<meta name="twitter:image" content="https://i0.wp.com/css-tricks.com/wp-content/uploads/2018/07/state-management.jpg" />
<meta name="twitter:label1" content="Written by" />
<meta name="twitter:data1" content="Daniel Schwarz" />
<meta name="twitter:label2" content="Time to read" />
<meta name="twitter:data2" content="9 minutes" />
<script type="application/ld+json" class="rank-math-schema">{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://css-tricks.com/#organization","name":"CSS-Tricks","url":"https://css-tricks.com","sameAs":["https://www.facebook.com/CSSTricks","https://twitter.com/CSS","https://bsky.app/profile/css-tricks.com","https://mastodon.social/csstricks"],"email":"geoff@css-tricks.com","logo":{"@type":"ImageObject","@id":"https://css-tricks.com/#logo","url":"https://css-tricks.com/wp-content/uploads/2026/07/css-tricks-star-logo.svg","contentUrl":"https://css-tricks.com/wp-content/uploads/2026/07/css-tricks-star-logo.svg","caption":"CSS-Tricks","inLanguage":"en-US","width":"116","height":"124"},"description":"A learning community for front-end design and development"},{"@type":"WebSite","@id":"https://css-tricks.com/#website","url":"https://css-tricks.com","name":"CSS-Tricks","publisher":{"@id":"https://css-tricks.com/#organization"},"inLanguage":"en-US"},{"@type":"ImageObject","@id":"https://i0.wp.com/css-tricks.com/wp-content/uploads/2018/07/state-management.jpg?fit=1200%2C600&amp;ssl=1","url":"https://i0.wp.com/css-tricks.com/wp-content/uploads/2018/07/state-management.jpg?fit=1200%2C600&amp;ssl=1","width":"1200","height":"600","inLanguage":"en-US"},{"@type":"WebPage","@id":"https://css-tricks.com/css-states-and-javascript-events/#webpage","url":"https://css-tricks.com/css-states-and-javascript-events/","name":"The Shifting Line Between CSS States and JavaScript Events | CSS-Tricks","datePublished":"2026-06-29T07:03:32-06:00","dateModified":"2026-06-30T19:44:13-06:00","isPartOf":{"@id":"https://css-tricks.com/#website"},"primaryImageOfPage":{"@id":"https://i0.wp.com/css-tricks.com/wp-content/uploads/2018/07/state-management.jpg?fit=1200%2C600&amp;ssl=1"},"inLanguage":"en-US"},{"@type":"Person","@id":"https://css-tricks.com/author/danielschwarz/","name":"Daniel Schwarz","url":"https://css-tricks.com/author/danielschwarz/","image":{"@type":"ImageObject","@id":"https://secure.gravatar.com/avatar/b6c928ce1b901c34f86f3856b5a3bcefe9a4fb94698b9778fb3df5802d66e25d?s=96&amp;d=retro&amp;r=pg","url":"https://secure.gravatar.com/avatar/b6c928ce1b901c34f86f3856b5a3bcefe9a4fb94698b9778fb3df5802d66e25d?s=96&amp;d=retro&amp;r=pg","caption":"Daniel Schwarz","inLanguage":"en-US"},"sameAs":["https://dxnny.fun/","https://twitter.com/dxnnydotfun","https://bsky.app/profile/dxnny.fun"],"worksFor":{"@id":"https://css-tricks.com/#organization"}},{"@type":"BlogPosting","headline":"The Shifting Line Between CSS States and JavaScript Events | CSS-Tricks","datePublished":"2026-06-29T07:03:32-06:00","dateModified":"2026-06-30T19:44:13-06:00","articleSection":"Articles","author":{"@id":"https://css-tricks.com/author/danielschwarz/","name":"Daniel Schwarz"},"publisher":{"@id":"https://css-tricks.com/#organization"},"description":"CSS has always had pseudo-classes that style things based on user interactions. Recent features, however, are blurring the line between what CSS &quot;listens&quot; for and how they are alternatives to what Javascript typically listens for.","name":"The Shifting Line Between CSS States and JavaScript Events | CSS-Tricks","@id":"https://css-tricks.com/css-states-and-javascript-events/#richSnippet","isPartOf":{"@id":"https://css-tricks.com/css-states-and-javascript-events/#webpage"},"image":{"@id":"https://i0.wp.com/css-tricks.com/wp-content/uploads/2018/07/state-management.jpg?fit=1200%2C600&amp;ssl=1"},"inLanguage":"en-US","mainEntityOfPage":{"@id":"https://css-tricks.com/css-states-and-javascript-events/#webpage"}}]}</script>
<!-- /Rank Math WordPress SEO plugin -->

<link rel='preconnect' href='//i0.wp.com' />
<link rel='preconnect' href='//c0.wp.com' />
<link rel="alternate" type="application/rss+xml" title="CSS-Tricks &raquo; The Shifting Line Between CSS States and JavaScript Events Comments Feed" href="https://css-tricks.com/css-states-and-javascript-events/feed/" />
<link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://css-tricks.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fcss-tricks.com%2Fcss-states-and-javascript-events%2F" />
<link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://css-tricks.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fcss-tricks.com%2Fcss-states-and-javascript-events%2F&#038;format=xml" />
<style id="wp-img-auto-sizes-contain-inline-css">
img:is([sizes=auto i],[sizes^="auto," i]){contain-intrinsic-size:3000px 1500px}
/*# sourceURL=wp-img-auto-sizes-contain-inline-css */
</style>
<style id="classic-theme-styles-inline-css">
/*! This file is auto-generated */
.wp-block-button__link{color:#fff;background-color:#32373c;border-radius:9999px;box-shadow:none;text-decoration:none;padding:calc(.667em + 2px) calc(1.333em + 2px);font-size:1.125em}.wp-block-file__button{background:#32373c;color:#fff;text-decoration:none}
/*# sourceURL=/wp-includes/css/classic-themes.min.css */
</style>

<style id="global-styles-inline-css">
:root{--wp--preset--aspect-ratio--square: 1;--wp--preset--aspect-ratio--4-3: 4/3;--wp--preset--aspect-ratio--3-4: 3/4;--wp--preset--aspect-ratio--3-2: 3/2;--wp--preset--aspect-ratio--2-3: 2/3;--wp--preset--aspect-ratio--16-9: 16/9;--wp--preset--aspect-ratio--9-16: 9/16;--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgb(6,147,227) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgb(252,185,0) 0%,rgb(255,105,0) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgb(255,105,0) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgb(255, 255, 255), 6px 6px rgb(0, 0, 0);--wp--preset--shadow--crisp: 6px 6px 0px rgb(0, 0, 0);}:where(body) { margin: 0; }:where(.is-layout-flex){gap: 0.5em;}:where(.is-layout-grid){gap: 0.5em;}body .is-layout-flex{display: flex;}.is-layout-flex{flex-wrap: wrap;align-items: center;}.is-layout-flex > :is(*, div){margin: 0;}body .is-layout-grid{display: grid;}.is-layout-grid > :is(*, div){margin: 0;}body{padding-top: 0px;padding-right: 0px;padding-bottom: 0px;padding-left: 0px;}:root :where(.wp-element-button, .wp-block-button__link){background-color: #32373c;border-width: 0;color: #fff;font-family: inherit;font-size: inherit;font-style: inherit;font-weight: inherit;letter-spacing: inherit;line-height: inherit;padding-top: calc(0.667em + 2px);padding-right: calc(1.333em + 2px);padding-bottom: calc(0.667em + 2px);padding-left: calc(1.333em + 2px);text-decoration: none;text-transform: inherit;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
/*# sourceURL=global-styles-inline-css */
</style>

<link rel='stylesheet' id='learndash_quiz_front_css-css' href='//css-tricks.com/wp-content/plugins/sfwd-lms/themes/legacy/templates/learndash_quiz_front.min.css?ver=5.1.7' media='all' />
<link rel='stylesheet' id='dashicons-css' href='https://c0.wp.com/c/7.0.1/wp-includes/css/dashicons.min.css' media='all' />
<link rel='stylesheet' id='learndash-css' href='//css-tricks.com/wp-content/plugins/sfwd-lms/src/assets/dist/css/styles.css?ver=5.1.7' media='all' />
<link rel='stylesheet' id='jquery-dropdown-css-css' href='//css-tricks.com/wp-content/plugins/sfwd-lms/assets/css/jquery.dropdown.min.css?ver=5.1.7' media='all' />
<link rel='stylesheet' id='learndash_lesson_video-css' href='//css-tricks.com/wp-content/plugins/sfwd-lms/themes/legacy/templates/learndash_lesson_video.min.css?ver=5.1.7' media='all' />
<link rel='stylesheet' id='learndash-admin-bar-css' href='https://css-tricks.com/wp-content/plugins/sfwd-lms/src/assets/dist/css/admin-bar/styles.css?ver=5.1.7' media='all' />
<link rel='stylesheet' id='jetpack-instant-search-css' href='https://css-tricks.com/wp-content/plugins/jetpack/jetpack_vendor/automattic/jetpack-search/build/instant-search/jp-search.chunk-main-payload.css?minify=false&#038;ver=9de017be31cb883a04fb' media='all' />
<link rel='stylesheet' id='learndash-course-grid-skin-grid-css' href='https://css-tricks.com/wp-content/plugins/sfwd-lms/includes/course-grid/templates/skins/grid/style.css?ver=5.1.7' media='all' />
<link rel='stylesheet' id='learndash-course-grid-pagination-css' href='https://css-tricks.com/wp-content/plugins/sfwd-lms/includes/course-grid/templates/pagination/style.css?ver=5.1.7' media='all' />
<link rel='stylesheet' id='learndash-course-grid-filter-css' href='https://css-tricks.com/wp-content/plugins/sfwd-lms/includes/course-grid/templates/filter/style.css?ver=5.1.7' media='all' />
<link rel='stylesheet' id='learndash-course-grid-card-grid-1-css' href='https://css-tricks.com/wp-content/plugins/sfwd-lms/includes/course-grid/templates/cards/grid-1/style.css?ver=5.1.7' media='all' />
<link rel='stylesheet' id='css-tricks-style-css' href='https://css-tricks.com/wp-content/themes/CSS-Tricks-19/style.css?ver=17360904070019' media='all' />
<link rel='stylesheet' id='learndash-front-css' href='//css-tricks.com/wp-content/plugins/sfwd-lms/themes/ld30/assets/css/learndash.min.css?ver=5.1.7' media='all' />
<style id="learndash-front-inline-css">
		.learndash-wrapper .ld-item-list .ld-item-list-item.ld-is-next,
		.learndash-wrapper .wpProQuiz_content .wpProQuiz_questionListItem label:focus-within {
			border-color: #ff7a18;
		}

		/*
		.learndash-wrapper a:not(.ld-button):not(#quiz_continue_link):not(.ld-focus-menu-link):not(.btn-blue):not(#quiz_continue_link):not(.ld-js-register-account):not(#ld-focus-mode-course-heading):not(#btn-join):not(.ld-item-name):not(.ld-table-list-item-preview):not(.ld-lesson-item-preview-heading),
		 */

		.learndash-wrapper .ld-breadcrumbs a,
		.learndash-wrapper .ld-lesson-item.ld-is-current-lesson .ld-lesson-item-preview-heading,
		.learndash-wrapper .ld-lesson-item.ld-is-current-lesson .ld-lesson-title,
		.learndash-wrapper .ld-primary-color-hover:hover,
		.learndash-wrapper .ld-primary-color,
		.learndash-wrapper .ld-primary-color-hover:hover,
		.learndash-wrapper .ld-primary-color,
		.learndash-wrapper .ld-tabs .ld-tabs-navigation .ld-tab.ld-active,
		.learndash-wrapper .ld-button.ld-button-transparent,
		.learndash-wrapper .ld-button.ld-button-reverse,
		.learndash-wrapper .ld-icon-certificate,
		.learndash-wrapper .ld-login-modal .ld-login-modal-login .ld-modal-heading,
		#wpProQuiz_user_content a,
		.learndash-wrapper .ld-item-list .ld-item-list-item a.ld-item-name:hover,
		.learndash-wrapper .ld-focus-comments__heading-actions .ld-expand-button,
		.learndash-wrapper .ld-focus-comments__heading a,
		.learndash-wrapper .ld-focus-comments .comment-respond a,
		.learndash-wrapper .ld-focus-comment .ld-comment-reply a.comment-reply-link:hover,
		.learndash-wrapper .ld-expand-button.ld-button-alternate {
			color: #ff7a18 !important;
		}

		.learndash-wrapper .ld-focus-comment.bypostauthor>.ld-comment-wrapper,
		.learndash-wrapper .ld-focus-comment.role-group_leader>.ld-comment-wrapper,
		.learndash-wrapper .ld-focus-comment.role-administrator>.ld-comment-wrapper {
			background-color:rgba(255, 122, 24, 0.03) !important;
		}


		.learndash-wrapper .ld-primary-background,
		.learndash-wrapper .ld-tabs .ld-tabs-navigation .ld-tab.ld-active:after {
			background: #ff7a18 !important;
		}



		.learndash-wrapper .ld-course-navigation .ld-lesson-item.ld-is-current-lesson .ld-status-incomplete,
		.learndash-wrapper .ld-focus-comment.bypostauthor:not(.ptype-sfwd-assignment) >.ld-comment-wrapper>.ld-comment-avatar img,
		.learndash-wrapper .ld-focus-comment.role-group_leader>.ld-comment-wrapper>.ld-comment-avatar img,
		.learndash-wrapper .ld-focus-comment.role-administrator>.ld-comment-wrapper>.ld-comment-avatar img {
			border-color: #ff7a18 !important;
		}



		.learndash-wrapper .ld-loading::before {
			border-top:3px solid #ff7a18 !important;
		}

		.learndash-wrapper .ld-button:hover:not([disabled]):not(.ld-button-transparent):not(.ld--ignore-inline-css),
		#learndash-tooltips .ld-tooltip:after,
		#learndash-tooltips .ld-tooltip,
		.ld-tooltip:not(.ld-tooltip--modern) [role="tooltip"],
		.learndash-wrapper .ld-primary-background,
		.learndash-wrapper .btn-join:not(.ld--ignore-inline-css),
		.learndash-wrapper #btn-join:not(.ld--ignore-inline-css),
		.learndash-wrapper .ld-button:not([disabled]):not(.ld-button-reverse):not(.ld-button-transparent):not(.ld--ignore-inline-css),
		.learndash-wrapper .ld-expand-button:not([disabled]),
		.learndash-wrapper .wpProQuiz_content .wpProQuiz_button:not([disabled]):not(.wpProQuiz_button_reShowQuestion):not(.wpProQuiz_button_restartQuiz),
		.learndash-wrapper .wpProQuiz_content .wpProQuiz_button2:not([disabled]),
		.learndash-wrapper .ld-focus .ld-focus-sidebar .ld-course-navigation-heading,
		.learndash-wrapper .ld-focus-comments .form-submit #submit,
		.learndash-wrapper .ld-login-modal input[type='submit']:not([disabled]),
		.learndash-wrapper .ld-login-modal .ld-login-modal-register:not([disabled]),
		.learndash-wrapper .wpProQuiz_content .wpProQuiz_certificate a.btn-blue:not([disabled]),
		.learndash-wrapper .ld-focus .ld-focus-header .ld-user-menu .ld-user-menu-items a:not([disabled]),
		#wpProQuiz_user_content table.wp-list-table thead th,
		#wpProQuiz_overlay_close:not([disabled]),
		.learndash-wrapper .ld-expand-button.ld-button-alternate:not([disabled]) .ld-icon {
			background-color: #ff7a18 !important;
			color: #000000;
		}

		.learndash-wrapper .ld-focus .ld-focus-sidebar .ld-focus-sidebar-trigger:not([disabled]):not(:hover):not(:focus) .ld-icon {
			background-color: #ff7a18;
		}

		.learndash-wrapper .ld-focus .ld-focus-sidebar .ld-focus-sidebar-trigger:hover .ld-icon,
		.learndash-wrapper .ld-focus .ld-focus-sidebar .ld-focus-sidebar-trigger:focus .ld-icon {
			border-color: #ff7a18;
			color: #ff7a18;
		}

		.learndash-wrapper .ld-button:focus:not(.ld-button-transparent):not(.ld--ignore-inline-css),
		.learndash-wrapper .btn-join:focus:not(.ld--ignore-inline-css),
		.learndash-wrapper #btn-join:focus:not(.ld--ignore-inline-css),
		.learndash-wrapper .ld-expand-button:focus,
		.learndash-wrapper .wpProQuiz_content .wpProQuiz_button:not(.wpProQuiz_button_reShowQuestion):focus:not(.wpProQuiz_button_restartQuiz),
		.learndash-wrapper .wpProQuiz_content .wpProQuiz_button2:focus,
		.learndash-wrapper .ld-focus-comments .form-submit #submit,
		.learndash-wrapper .ld-login-modal input[type='submit']:focus,
		.learndash-wrapper .ld-login-modal .ld-login-modal-register:focus,
		.learndash-wrapper .wpProQuiz_content .wpProQuiz_certificate a.btn-blue:focus {
			opacity: 0.75; /* Replicates the hover/focus states pre-4.21.3. */
			outline-color: #ff7a18;
		}

		.learndash-wrapper .ld-button:hover:not(.ld-button-transparent):not(.ld--ignore-inline-css),
		.learndash-wrapper .btn-join:hover:not(.ld--ignore-inline-css),
		.learndash-wrapper #btn-join:hover:not(.ld--ignore-inline-css),
		.learndash-wrapper .ld-expand-button:hover,
		.learndash-wrapper .wpProQuiz_content .wpProQuiz_button:not(.wpProQuiz_button_reShowQuestion):hover:not(.wpProQuiz_button_restartQuiz),
		.learndash-wrapper .wpProQuiz_content .wpProQuiz_button2:hover,
		.learndash-wrapper .ld-focus-comments .form-submit #submit,
		.learndash-wrapper .ld-login-modal input[type='submit']:hover,
		.learndash-wrapper .ld-login-modal .ld-login-modal-register:hover,
		.learndash-wrapper .wpProQuiz_content .wpProQuiz_certificate a.btn-blue:hover {
			background-color: #ff7a18; /* Replicates the hover/focus states pre-4.21.3. */
			opacity: 0.85; /* Replicates the hover/focus states pre-4.21.3. */
		}

		.learndash-wrapper .ld-item-list .ld-item-search .ld-closer:focus {
			border-color: #ff7a18;
		}

		.learndash-wrapper .ld-focus .ld-focus-header .ld-user-menu .ld-user-menu-items:before {
			border-bottom-color: #ff7a18 !important;
		}

		.learndash-wrapper .ld-button.ld-button-transparent:hover {
			background: transparent !important;
		}

		.learndash-wrapper .ld-button.ld-button-transparent:focus {
			outline-color: #ff7a18;
		}

		.learndash-wrapper .ld-focus .ld-focus-header .sfwd-mark-complete .learndash_mark_complete_button:not(.ld--ignore-inline-css),
		.learndash-wrapper .ld-focus .ld-focus-header #sfwd-mark-complete #learndash_mark_complete_button,
		.learndash-wrapper .ld-button.ld-button-transparent,
		.learndash-wrapper .ld-button.ld-button-alternate,
		.learndash-wrapper .ld-expand-button.ld-button-alternate {
			background-color:transparent !important;
		}

		.learndash-wrapper .ld-focus-header .ld-user-menu .ld-user-menu-items a,
		.learndash-wrapper .ld-button.ld-button-reverse:hover,
		.learndash-wrapper .ld-alert-success .ld-alert-icon.ld-icon-certificate,
		.learndash-wrapper .ld-alert-warning .ld-button,
		.learndash-wrapper .ld-primary-background.ld-status {
			color:white !important;
		}

		.learndash-wrapper .ld-status.ld-status-unlocked {
			background-color: rgba(255,122,24,0.2) !important;
			color: #ff7a18 !important;
		}

		.learndash-wrapper .wpProQuiz_content .wpProQuiz_addToplist {
			background-color: rgba(255,122,24,0.1) !important;
			border: 1px solid #ff7a18 !important;
		}

		.learndash-wrapper .wpProQuiz_content .wpProQuiz_toplistTable th {
			background: #ff7a18 !important;
		}

		.learndash-wrapper .wpProQuiz_content .wpProQuiz_toplistTrOdd {
			background-color: rgba(255,122,24,0.1) !important;
		}


		.learndash-wrapper .wpProQuiz_content .wpProQuiz_time_limit .wpProQuiz_progress {
			background-color: #ff7a18 !important;
		}
		
		.learndash-wrapper #quiz_continue_link,
		.learndash-wrapper .ld-secondary-background,
		.learndash-wrapper .learndash_mark_complete_button:not(.ld--ignore-inline-css),
		.learndash-wrapper #learndash_mark_complete_button,
		.learndash-wrapper .ld-status-complete,
		.learndash-wrapper .ld-alert-success .ld-button,
		.learndash-wrapper .ld-alert-success .ld-alert-icon {
			background-color: #e52e71 !important;
		}

		.learndash-wrapper #quiz_continue_link:focus,
		.learndash-wrapper .learndash_mark_complete_button:focus:not(.ld--ignore-inline-css),
		.learndash-wrapper #learndash_mark_complete_button:focus,
		.learndash-wrapper .ld-alert-success .ld-button:focus {
			outline-color: #e52e71;
		}

		.learndash-wrapper .wpProQuiz_content a#quiz_continue_link {
			background-color: #e52e71 !important;
		}

		.learndash-wrapper .wpProQuiz_content a#quiz_continue_link:focus {
			outline-color: #e52e71;
		}

		.learndash-wrapper .course_progress .sending_progress_bar {
			background: #e52e71 !important;
		}

		.learndash-wrapper .wpProQuiz_content .wpProQuiz_button_reShowQuestion:hover, .learndash-wrapper .wpProQuiz_content .wpProQuiz_button_restartQuiz:hover {
			background-color: #e52e71 !important;
			opacity: 0.75;
		}

		.learndash-wrapper .wpProQuiz_content .wpProQuiz_button_reShowQuestion:focus,
		.learndash-wrapper .wpProQuiz_content .wpProQuiz_button_restartQuiz:focus {
			outline-color: #e52e71;
		}

		.learndash-wrapper .ld-secondary-color-hover:hover,
		.learndash-wrapper .ld-secondary-color,
		.learndash-wrapper .ld-focus .ld-focus-header .sfwd-mark-complete .learndash_mark_complete_button:not(.ld--ignore-inline-css),
		.learndash-wrapper .ld-focus .ld-focus-header #sfwd-mark-complete #learndash_mark_complete_button,
		.learndash-wrapper .ld-focus .ld-focus-header .sfwd-mark-complete:after {
			color: #e52e71 !important;
		}

		.learndash-wrapper .ld-secondary-in-progress-icon {
			border-left-color: #e52e71 !important;
			border-top-color: #e52e71 !important;
		}

		.learndash-wrapper .ld-alert-success {
			border-color: #e52e71;
			background-color: transparent !important;
			color: #e52e71;
		}

		
		.learndash-wrapper .ld-alert-warning {
			background-color:transparent;
		}

		.learndash-wrapper .ld-status-waiting,
		.learndash-wrapper .ld-alert-warning .ld-alert-icon {
			background-color: #000000 !important;
		}

		.learndash-wrapper .ld-tertiary-color-hover:hover,
		.learndash-wrapper .ld-tertiary-color,
		.learndash-wrapper .ld-alert-warning {
			color: #000000 !important;
		}

		.learndash-wrapper .ld-tertiary-background {
			background-color: #000000 !important;
		}

		.learndash-wrapper .ld-alert-warning {
			border-color: #000000 !important;
		}

		.learndash-wrapper .ld-tertiary-background,
		.learndash-wrapper .ld-alert-warning .ld-alert-icon {
			color:white !important;
		}

		.learndash-wrapper .wpProQuiz_content .wpProQuiz_reviewQuestion li.wpProQuiz_reviewQuestionReview,
		.learndash-wrapper .wpProQuiz_content .wpProQuiz_box li.wpProQuiz_reviewQuestionReview {
			background-color: #000000 !important;
		}

		
/*# sourceURL=learndash-front-inline-css */
</style>
<script id="jetpack_related-posts-js-extra">
var related_posts_js_options = {"post_heading":"h4"};
//# sourceURL=jetpack_related-posts-js-extra
</script>
<script id="jetpack_related-posts-js" src="https://c0.wp.com/p/jetpack/16.0/_inc/build/related-posts/related-posts.min.js"></script>
<script id="breeze-prefetch-js-extra">
var breeze_prefetch = {"local_url":"https://css-tricks.com","ignore_remote_prefetch":"1","ignore_list":["wp-admin","wp-login.php"]};
//# sourceURL=breeze-prefetch-js-extra
</script>
<script id="breeze-prefetch-js" src="https://css-tricks.com/wp-content/plugins/breeze/assets/js/js-front-end/breeze-prefetch-links.min.js?ver=2.5.9"></script>
<link rel="https://api.w.org/" href="https://css-tricks.com/wp-json/" /><link rel="alternate" title="JSON" type="application/json" href="https://css-tricks.com/wp-json/wp/v2/posts/395223" /><link rel='shortlink' href='https://css-tricks.com/?p=395223' />
<!-- Better Art Direction Styles -->


	<style>img#wpstats{display:none}</style>
		<link rel="site.standard.document" href="at://did:plc:ffm3o4vz473f6q7idxz4pmz7/site.standard.document/3mpgkfvjjyqdg" />
<link rel="site.standard.publication" href="at://did:plc:ffm3o4vz473f6q7idxz4pmz7/site.standard.publication/3moisllyxvlob" />
<link rel="icon" href="https://i0.wp.com/css-tricks.com/wp-content/uploads/2021/07/star.png?fit=32%2C32&#038;ssl=1" sizes="32x32" />
<link rel="icon" href="https://i0.wp.com/css-tricks.com/wp-content/uploads/2021/07/star.png?fit=180%2C180&#038;ssl=1" sizes="192x192" />
<link rel="apple-touch-icon" href="https://i0.wp.com/css-tricks.com/wp-content/uploads/2021/07/star.png?fit=180%2C180&#038;ssl=1" />
<meta name="msapplication-TileImage" content="https://i0.wp.com/css-tricks.com/wp-content/uploads/2021/07/star.png?fit=180%2C180&#038;ssl=1" />

<style id="wp-block-heading-inline-css">
h1:where(.wp-block-heading).has-background,h2:where(.wp-block-heading).has-background,h3:where(.wp-block-heading).has-background,h4:where(.wp-block-heading).has-background,h5:where(.wp-block-heading).has-background,h6:where(.wp-block-heading).has-background{padding:1.25em 2.375em}h1.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h1.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h2.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h2.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h3.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h3.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h4.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h4.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h5.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h5.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h6.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h6.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]){rotate:180deg}
/*# sourceURL=https://c0.wp.com/c/7.0.1/wp-includes/blocks/heading/style.min.css */
</style>
<style id="wp-block-list-inline-css">
ol,ul{box-sizing:border-box}:root :where(.wp-block-list.has-background){padding:1.25em 2.375em}
/*# sourceURL=https://c0.wp.com/c/7.0.1/wp-includes/blocks/list/style.min.css */
</style>
<style id="wp-block-paragraph-inline-css">
.is-small-text{font-size:.875em}.is-regular-text{font-size:1em}.is-large-text{font-size:2.25em}.is-larger-text{font-size:3em}.has-drop-cap:not(:focus):first-letter{float:left;font-size:8.4em;font-style:normal;font-weight:100;line-height:.68;margin:.05em .1em 0 0;text-transform:uppercase}body.rtl .has-drop-cap:not(:focus):first-letter{float:none;margin-left:.1em}p.has-drop-cap.has-background{overflow:hidden}:root :where(p.has-background){padding:1.25em 2.375em}:where(p.has-text-color:not(.has-link-color)) a{color:inherit}p.has-text-align-left[style*="writing-mode:vertical-lr"],p.has-text-align-right[style*="writing-mode:vertical-rl"]{rotate:180deg}
/*# sourceURL=https://c0.wp.com/c/7.0.1/wp-includes/blocks/paragraph/style.min.css */
</style>
<style id="wp-block-table-inline-css">
.wp-block-table{overflow-x:auto}.wp-block-table table{border-collapse:collapse;width:100%}.wp-block-table thead{border-bottom:3px solid}.wp-block-table tfoot{border-top:3px solid}.wp-block-table td,.wp-block-table th{border:1px solid;padding:.5em}.wp-block-table .has-fixed-layout{table-layout:fixed;width:100%}.wp-block-table .has-fixed-layout td,.wp-block-table .has-fixed-layout th{word-break:break-word}.wp-block-table.aligncenter,.wp-block-table.alignleft,.wp-block-table.alignright{display:table;width:auto}.wp-block-table.aligncenter td,.wp-block-table.aligncenter th,.wp-block-table.alignleft td,.wp-block-table.alignleft th,.wp-block-table.alignright td,.wp-block-table.alignright th{word-break:break-word}.wp-block-table .has-subtle-light-gray-background-color{background-color:#f3f4f5}.wp-block-table .has-subtle-pale-green-background-color{background-color:#e9fbe5}.wp-block-table .has-subtle-pale-blue-background-color{background-color:#e7f5fe}.wp-block-table .has-subtle-pale-pink-background-color{background-color:#fcf0ef}.wp-block-table.is-style-stripes{background-color:initial;border-collapse:inherit;border-spacing:0}.wp-block-table.is-style-stripes tbody tr:nth-child(odd){background-color:#f0f0f0}.wp-block-table.is-style-stripes.has-subtle-light-gray-background-color tbody tr:nth-child(odd){background-color:#f3f4f5}.wp-block-table.is-style-stripes.has-subtle-pale-green-background-color tbody tr:nth-child(odd){background-color:#e9fbe5}.wp-block-table.is-style-stripes.has-subtle-pale-blue-background-color tbody tr:nth-child(odd){background-color:#e7f5fe}.wp-block-table.is-style-stripes.has-subtle-pale-pink-background-color tbody tr:nth-child(odd){background-color:#fcf0ef}.wp-block-table.is-style-stripes td,.wp-block-table.is-style-stripes th{border-color:#0000}.wp-block-table.is-style-stripes{border-bottom:1px solid #f0f0f0}.wp-block-table .has-border-color td,.wp-block-table .has-border-color th,.wp-block-table .has-border-color tr,.wp-block-table .has-border-color>*{border-color:inherit}.wp-block-table table[style*=border-top-color] tr:first-child,.wp-block-table table[style*=border-top-color] tr:first-child td,.wp-block-table table[style*=border-top-color] tr:first-child th,.wp-block-table table[style*=border-top-color]>*,.wp-block-table table[style*=border-top-color]>* td,.wp-block-table table[style*=border-top-color]>* th{border-top-color:inherit}.wp-block-table table[style*=border-top-color] tr:not(:first-child){border-top-color:initial}.wp-block-table table[style*=border-right-color] td:last-child,.wp-block-table table[style*=border-right-color] th,.wp-block-table table[style*=border-right-color] tr,.wp-block-table table[style*=border-right-color]>*{border-right-color:inherit}.wp-block-table table[style*=border-bottom-color] tr:last-child,.wp-block-table table[style*=border-bottom-color] tr:last-child td,.wp-block-table table[style*=border-bottom-color] tr:last-child th,.wp-block-table table[style*=border-bottom-color]>*,.wp-block-table table[style*=border-bottom-color]>* td,.wp-block-table table[style*=border-bottom-color]>* th{border-bottom-color:inherit}.wp-block-table table[style*=border-bottom-color] tr:not(:last-child){border-bottom-color:initial}.wp-block-table table[style*=border-left-color] td:first-child,.wp-block-table table[style*=border-left-color] th,.wp-block-table table[style*=border-left-color] tr,.wp-block-table table[style*=border-left-color]>*{border-left-color:inherit}.wp-block-table table[style*=border-style] td,.wp-block-table table[style*=border-style] th,.wp-block-table table[style*=border-style] tr,.wp-block-table table[style*=border-style]>*{border-style:inherit}.wp-block-table table[style*=border-width] td,.wp-block-table table[style*=border-width] th,.wp-block-table table[style*=border-width] tr,.wp-block-table table[style*=border-width]>*{border-style:inherit;border-width:inherit}
/*# sourceURL=https://c0.wp.com/c/7.0.1/wp-includes/blocks/table/style.min.css */
</style>
<link rel='stylesheet' id='student-notes-style-css' href='https://css-tricks.com/wp-content/plugins/learndash-notes/dist/css/styles.css?ver=2.0.1' media='all' />
<link rel='stylesheet' id='jquery-ui-smoothness-css' href='https://ajax.googleapis.com/ajax/libs/jqueryui//themes/smoothness/jquery-ui.min.css' media='all' />
<link rel='stylesheet' id='font-awesome-css' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css?ver=4.7.0' media='all' />

</head>

<body class="wp-singular post-template-default single single-post postid-395223 single-format-standard wp-theme-CSS-Tricks-19 jps-theme-CSS-Tricks-19 category-articles">

  <div id="top-of-site-pixel-anchor"></div>

  <header class="site-header" id="site-header">

  <a id="skip-nav" class="skip-nav screen-reader-text" href="#maincontent">Skip to main content</a> 

  <div class="logo">
    <a href="/">
      <div class="screen-reader-text">CSS-Tricks</div>

      <svg class="icon-logo-star" width="35px" height="35px" viewBox="0 0 362.62 388.52" data-spin-me="false">
  <path d="M156.58,239l-88.3,64.75c-10.59,7.06-18.84,11.77-29.43,11.77-21.19,0-38.85-18.84-38.85-40C0,257.83,14.13,244.88,27.08,239l103.6-44.74L27.08,148.34C13,142.46,0,129.51,0,111.85,0,90.66,18.84,73,40,73c10.6,0,17.66,3.53,28.25,11.77l88.3,64.75L144.81,44.74C141.28,20,157.76,0,181.31,0s40,18.84,36.5,43.56L206,149.52l88.3-64.75C304.93,76.53,313.17,73,323.77,73a39.2,39.2,0,0,1,38.85,38.85c0,18.84-12.95,30.61-27.08,36.5L231.93,194.26,335.54,239c14.13,5.88,27.08,18.83,27.08,37.67,0,21.19-18.84,38.85-40,38.85-9.42,0-17.66-4.71-28.26-11.77L206,239l11.77,104.78c3.53,24.72-12.95,44.74-36.5,44.74s-40-18.84-36.5-43.56Z" />
</svg>
            <svg id="Layer_1" class="icon-logo-text" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 974.89 117.95"><g id="CSS-Tricks" style="isolation:isolate"><g style="isolation:isolate"><path d="M66.18,66.2v-.33c0-32.42,24.27-59,58.81-59,17.6,0,29.16,5.21,39.1,12.87a10,10,0,0,1,3.91,8,10,10,0,0,1-16,7.82c-7.82-6.35-16.29-10.26-27.21-10.26-21.67,0-37.63,17.92-37.63,40.24v.33c0,22.32,15.8,40.4,37.63,40.4,12.06,0,20.2-3.91,28.51-10.92a9.12,9.12,0,0,1,6-2.28,9.53,9.53,0,0,1,9.45,9.29,9.63,9.63,0,0,1-3.26,7.17c-10.75,9.45-23,15.31-41.38,15.31C90.94,124.85,66.18,98.95,66.18,66.2Z" transform="translate(-66.18 -6.9)" /><path d="M188.53,110.19a9.34,9.34,0,0,1,5.54-16.94A9.29,9.29,0,0,1,199.93,95c9.45,7.49,19.55,11.73,31.93,11.73s20.2-5.87,20.2-14.34V92.1c0-8.15-4.56-12.54-25.74-17.43-24.27-5.87-38-13-38-34V40.3c0-19.55,16.29-33.07,38.94-33.07,14.34,0,25.9,3.75,36.17,10.59a9,9,0,0,1,4.4,8,9.32,9.32,0,0,1-9.45,9.29,9.69,9.69,0,0,1-5.21-1.47C244.41,27.91,235.94,25,227,25c-11.73,0-18.57,6-18.57,13.52v.33c0,8.8,5.21,12.71,27.21,17.92,24.11,5.86,36.49,14.5,36.49,33.4v.33c0,21.34-16.78,34.05-40.73,34.05A71,71,0,0,1,188.53,110.19Z" transform="translate(-66.18 -6.9)" /><path d="M291.17,110.19a9.34,9.34,0,0,1,5.54-16.94A9.29,9.29,0,0,1,302.57,95c9.45,7.49,19.55,11.73,31.93,11.73s20.2-5.87,20.2-14.34V92.1c0-8.15-4.56-12.54-25.74-17.43-24.27-5.87-38-13-38-34V40.3c0-19.55,16.29-33.07,38.94-33.07,14.34,0,25.9,3.75,36.17,10.59a9,9,0,0,1,4.4,8,9.32,9.32,0,0,1-9.45,9.29,9.69,9.69,0,0,1-5.21-1.47C347,27.91,338.57,25,329.61,25,317.88,25,311,31,311,38.5v.33c0,8.8,5.21,12.71,27.21,17.92,24.11,5.86,36.49,14.5,36.49,33.4v.33c0,21.34-16.78,34.05-40.73,34.05A71,71,0,0,1,291.17,110.19Z" transform="translate(-66.18 -6.9)" /><path d="M392,73a9.77,9.77,0,0,1,9.61-9.77h30.63a9.69,9.69,0,0,1,0,19.39H401.62A9.74,9.74,0,0,1,392,73Z" transform="translate(-66.18 -6.9)" /><path d="M478.19,27.43H450.5a9.29,9.29,0,0,1,0-18.57h75.76a9.29,9.29,0,0,1,0,18.57H498.4v86.35a10.1,10.1,0,0,1-20.2,0Z" transform="translate(-66.18 -6.9)" /><path d="M555.74,19a10,10,0,0,1,10.1-10.1h40.73c14.34,0,25.58,4.24,32.91,11.4,6,6.19,9.45,14.66,9.45,24.6v.33c0,18.25-10.59,29.33-25.9,34.05l21.83,27.53c2,2.44,3.26,4.56,3.26,7.66a9.45,9.45,0,0,1-9.61,9.29c-4.56,0-7.49-2.12-9.77-5.21L601,83.14H575.78v30.63a10,10,0,0,1-20,0Zm49.36,46.43c14.34,0,23.46-7.49,23.46-19.06V46c0-12.22-8.8-18.9-23.62-18.9H575.78V65.39Z" transform="translate(-66.18 -6.9)" /><path d="M674.67,18a10,10,0,0,1,20,0v95.8a10,10,0,0,1-20,0Z" transform="translate(-66.18 -6.9)" /><path d="M720.12,66.2v-.33c0-32.42,24.27-59,58.81-59,17.59,0,29.16,5.21,39.1,12.87a10,10,0,0,1,3.91,8,10,10,0,0,1-16,7.82c-7.82-6.35-16.29-10.26-27.21-10.26-21.67,0-37.63,17.92-37.63,40.24v.33c0,22.32,15.8,40.4,37.63,40.4,12.06,0,20.2-3.91,28.51-10.92a9.12,9.12,0,0,1,6-2.28,9.53,9.53,0,0,1,9.45,9.29,9.63,9.63,0,0,1-3.26,7.17c-10.75,9.45-23,15.31-41.38,15.31C744.89,124.85,720.12,98.95,720.12,66.2Z" transform="translate(-66.18 -6.9)" /><path d="M845.41,18a10,10,0,0,1,20,0V66.2l54.09-54.42A10.54,10.54,0,0,1,927.84,8a9.18,9.18,0,0,1,9.29,9.29,9.74,9.74,0,0,1-3.58,7.49L898,59l38.45,47.74a10.85,10.85,0,0,1,2.77,7.17,9.78,9.78,0,0,1-10.1,9.78c-3.91,0-6.35-2-8.47-4.72L884,72.23,865.44,90.15v23.62a10,10,0,0,1-20,0Z" transform="translate(-66.18 -6.9)" /><path d="M957.49,110.19A9.34,9.34,0,0,1,963,93.25,9.29,9.29,0,0,1,968.9,95c9.45,7.49,19.55,11.73,31.93,11.73s20.2-5.87,20.2-14.34V92.1c0-8.15-4.56-12.54-25.74-17.43-24.28-5.87-38-13-38-34V40.3c0-19.55,16.29-33.07,38.94-33.07,14.34,0,25.9,3.75,36.17,10.59a9,9,0,0,1,4.4,8,9.32,9.32,0,0,1-9.45,9.29,9.69,9.69,0,0,1-5.21-1.47c-8.8-5.7-17.27-8.63-26.23-8.63-11.73,0-18.57,6-18.57,13.52v.33c0,8.8,5.21,12.71,27.21,17.92,24.11,5.86,36.49,14.5,36.49,33.4v.33c0,21.34-16.78,34.05-40.73,34.05A71,71,0,0,1,957.49,110.19Z" transform="translate(-66.18 -6.9)" /></g></g></svg>    </a>

    <span>Since 2007</span>
  </div>

  <div class="header-middle-area">

    <nav id="main-nav" class="main-nav" role="navigation">
	<ul id="menu-primary" class="menu"><li id="menu-item-379211" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-379211"><a href="https://css-tricks.com/category/articles/"><span>Articles</span></a></li>
<li id="menu-item-377808" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-377808"><a href="/guides"><span>Guides</span></a></li>
<li id="menu-item-377809" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-377809"><a href="/almanac"><span>Almanac</span></a></li>
<li id="menu-item-379154" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-379154"><a href="https://css-tricks.com/category/links/"><span>Links</span></a></li>
<li id="menu-item-382690" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-382690"><a href="https://css-tricks.com/picks/"><span>Picks</span></a></li>
<li id="menu-item-394345" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-394345"><a href="https://css-tricks.com/newsletters/"><span>Newsletter</span></a></li>
<li class="search-item"><a href="https://www.google.com/search?q=site:css-tricks.com%20layout" class="jetpack-search-filter__link"><span class="screen-reader-text">Search</span><svg width="24" height="24" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M15.0726 10.4326C12.4801 10.4326 10.4 12.5451 10.4 15.1053C10.4 17.6978 12.5125 19.7779 15.0726 19.7779C17.6651 19.7779 19.7453 17.6654 19.7453 15.1053C19.744 12.544 17.664 10.4326 15.0726 10.4326Z" fill="white"/>
<path d="M16.0327 0.447479C7.42401 0.447479 0.447693 7.4238 0.447693 16.0324C0.447693 24.6398 7.42401 31.6161 16.0314 31.6161C24.64 31.6161 31.6163 24.6398 31.6163 16.0324C31.6163 7.4238 24.64 0.447479 16.0327 0.447479ZM23.6163 24.0324C23.3926 24.2562 23.0401 24.385 22.6563 24.385C22.2726 24.385 21.9526 24.2575 21.6963 24.0324L18.7526 21.0887L18.4651 21.2487C17.4088 21.825 16.2576 22.145 15.0724 22.145C11.1998 22.145 8.06509 19.0087 8.06509 15.1376C8.06509 11.265 11.2013 8.13023 15.0724 8.13023C18.9451 8.13023 22.0798 11.2665 22.0798 15.1376C22.0798 16.5138 21.6961 17.8251 20.9273 18.9776L20.7348 19.2976L23.6473 22.2101C23.8711 22.4664 24.0311 22.7864 24.0311 23.1376C23.9998 23.4563 23.8723 23.7763 23.616 24.0326L23.6163 24.0324Z" fill="white"/>
</svg>
</a></li></ul></nav>
  </div>
  
</header>

  <div class="page-wrap">
<script>
  var articleID = 395223;
  var articleYear = 2026;
  var articleAuthor = "288677";
  var articleType = "post";
</script>

<div class="articles-and-sidebar ">

  <main id="post-395223">

    <article>

      <header class="mega-header">

    <style>
    html {
      --featured-img: url(https://css-tricks.com/wp-content/uploads/2018/07/state-management.jpg);
      --bg-blend-mode: multiply;
      background-size: 120% 2000px, 100% auto;
    }
  </style>
  
    <div class="tags">
    <a href="https://css-tricks.com/tag/pseudo-elements/" rel="tag">pseudo elements</a> <a href="https://css-tricks.com/tag/state/" rel="tag">state</a>  </div>

  <h1 class="article-title">
          The Shifting Line Between CSS States and JavaScript&nbsp;Events      </h1>

      <div class="author-row">

    
          <img style="border-radius: 50%;" src="https://secure.gravatar.com/avatar/b6c928ce1b901c34f86f3856b5a3bcefe9a4fb94698b9778fb3df5802d66e25d?s=80&d=retro&r=pg"/>
    
    <div>
      
              
        <a class="author-name" href="https://css-tricks.com/author/danielschwarz/">
          Daniel Schwarz        </a>
      
        on
              <time datetime="">
          Jun 29, 2026        </time> 

    </div>

  
</div>
  
</header>
        <div class="article-sponsor">

  
      <div id="bsa-custom-01"></div>
<script src="//m.servedby-buysellads.com/monetization.custom.js" type="text/javascript"
></script>

<script>
	(function () {
		if 