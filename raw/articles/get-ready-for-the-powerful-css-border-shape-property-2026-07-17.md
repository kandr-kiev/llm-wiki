---
source_url: https://css-tricks.com/get-ready-for-the-powerful-css-border-shape-property/
ingested: 2026-07-17
sha256: 967e02ebc3b74c96a53db217a744b3268a3997cdc0c7d69d31cb15a1c1f2c71d
blog_source: CSS Tricks
---
<!doctype html>
<html lang="en" id="top-of-site" class="js">

<head>
<title>Get Ready For the Powerful CSS border-shape Property! | CSS-Tricks</title>

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
<meta name="description" content="We recently got the shape() function and corner-shape property. What else could we possibly need as far as making shapes in CSS? Let me tell you: the border-shape property!"/>
<meta name="robots" content="follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large"/>
<link rel="canonical" href="https://css-tricks.com/get-ready-for-the-powerful-css-border-shape-property/" />
<meta property="og:locale" content="en_US" />
<meta property="og:type" content="article" />
<meta property="og:title" content="Get Ready For the Powerful CSS border-shape Property! | CSS-Tricks" />
<meta property="og:description" content="We recently got the shape() function and corner-shape property. What else could we possibly need as far as making shapes in CSS? Let me tell you: the border-shape property!" />
<meta property="og:url" content="https://css-tricks.com/get-ready-for-the-powerful-css-border-shape-property/" />
<meta property="og:site_name" content="CSS-Tricks" />
<meta property="article:publisher" content="https://www.facebook.com/CSSTricks" />
<meta property="article:tag" content="border-shape" />
<meta property="article:tag" content="borders" />
<meta property="article:tag" content="css shapes" />
<meta property="article:section" content="Articles" />
<meta property="og:updated_time" content="2026-07-07T09:14:05-06:00" />
<meta property="og:image" content="https://i0.wp.com/css-tricks.com/wp-content/uploads/2026/06/css-border-shape-examples.jpg" />
<meta property="og:image:secure_url" content="https://i0.wp.com/css-tricks.com/wp-content/uploads/2026/06/css-border-shape-examples.jpg" />
<meta property="og:image:width" content="1150" />
<meta property="og:image:height" content="552" />
<meta property="og:image:alt" content="Eight examples of CSS shapes, including two red hearts, two yellow sunbursts, two floors, and two blue jagged rectangles, the latter of each is a cutout against a solid background." />
<meta property="og:image:type" content="image/jpeg" />
<meta property="article:published_time" content="2026-07-07T09:14:00-06:00" />
<meta property="article:modified_time" content="2026-07-07T09:14:05-06:00" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Get Ready For the Powerful CSS border-shape Property! | CSS-Tricks" />
<meta name="twitter:description" content="We recently got the shape() function and corner-shape property. What else could we possibly need as far as making shapes in CSS? Let me tell you: the border-shape property!" />
<meta name="twitter:site" content="@CSS" />
<meta name="twitter:creator" content="@ChallengesCss" />
<meta name="twitter:image" content="https://i0.wp.com/css-tricks.com/wp-content/uploads/2026/06/css-border-shape-examples.jpg" />
<meta name="twitter:label1" content="Written by" />
<meta name="twitter:data1" content="Temani Afif" />
<meta name="twitter:label2" content="Time to read" />
<meta name="twitter:data2" content="9 minutes" />
<script type="application/ld+json" class="rank-math-schema">{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://css-tricks.com/#organization","name":"CSS-Tricks","url":"https://css-tricks.com","sameAs":["https://www.facebook.com/CSSTricks","https://twitter.com/CSS","https://bsky.app/profile/css-tricks.com","https://mastodon.social/csstricks"],"email":"geoff@css-tricks.com","logo":{"@type":"ImageObject","@id":"https://css-tricks.com/#logo","url":"https://css-tricks.com/wp-content/uploads/2026/07/css-tricks-star-logo.svg","contentUrl":"https://css-tricks.com/wp-content/uploads/2026/07/css-tricks-star-logo.svg","caption":"CSS-Tricks","inLanguage":"en-US","width":"116","height":"124"},"description":"A learning community for front-end design and development"},{"@type":"WebSite","@id":"https://css-tricks.com/#website","url":"https://css-tricks.com","name":"CSS-Tricks","publisher":{"@id":"https://css-tricks.com/#organization"},"inLanguage":"en-US"},{"@type":"ImageObject","@id":"https://i0.wp.com/css-tricks.com/wp-content/uploads/2026/06/css-border-shape-examples.jpg?fit=1150%2C552&amp;ssl=1","url":"https://i0.wp.com/css-tricks.com/wp-content/uploads/2026/06/css-border-shape-examples.jpg?fit=1150%2C552&amp;ssl=1","width":"1150","height":"552","caption":"Eight examples of CSS shapes, including two red hearts, two yellow sunbursts, two floors, and two blue jagged rectangles, the latter of each is a cutout against a solid background.","inLanguage":"en-US"},{"@type":"WebPage","@id":"https://css-tricks.com/get-ready-for-the-powerful-css-border-shape-property/#webpage","url":"https://css-tricks.com/get-ready-for-the-powerful-css-border-shape-property/","name":"Get Ready For the Powerful CSS border-shape Property! | CSS-Tricks","datePublished":"2026-07-07T09:14:00-06:00","dateModified":"2026-07-07T09:14:05-06:00","isPartOf":{"@id":"https://css-tricks.com/#website"},"primaryImageOfPage":{"@id":"https://i0.wp.com/css-tricks.com/wp-content/uploads/2026/06/css-border-shape-examples.jpg?fit=1150%2C552&amp;ssl=1"},"inLanguage":"en-US"},{"@type":"Person","@id":"https://css-tricks.com/author/afiftemani/","name":"Temani Afif","url":"https://css-tricks.com/author/afiftemani/","image":{"@type":"ImageObject","@id":"https://secure.gravatar.com/avatar/c16ca31febf1ccf880613914aa584da7cac990d02a585c1d6c9aff416ce8e28f?s=96&amp;d=retro&amp;r=pg","url":"https://secure.gravatar.com/avatar/c16ca31febf1ccf880613914aa584da7cac990d02a585c1d6c9aff416ce8e28f?s=96&amp;d=retro&amp;r=pg","caption":"Temani Afif","inLanguage":"en-US"},"sameAs":["https://support.temani-afif.com","https://twitter.com/ChallengesCss","https://css-challenges.com/","https://css-generators.com/","https://css-tip.com/","https://css-pattern.com/","https://css-loaders.com/","https://css-shape.com/"],"worksFor":{"@id":"https://css-tricks.com/#organization"}},{"@type":"BlogPosting","headline":"Get Ready For the Powerful CSS border-shape Property! | CSS-Tricks","datePublished":"2026-07-07T09:14:00-06:00","dateModified":"2026-07-07T09:14:05-06:00","articleSection":"Articles","author":{"@id":"https://css-tricks.com/author/afiftemani/","name":"Temani Afif"},"publisher":{"@id":"https://css-tricks.com/#organization"},"description":"We recently got the shape() function and corner-shape property. What else could we possibly need as far as making shapes in CSS? Let me tell you: the border-shape property!","name":"Get Ready For the Powerful CSS border-shape Property! | CSS-Tricks","@id":"https://css-tricks.com/get-ready-for-the-powerful-css-border-shape-property/#richSnippet","isPartOf":{"@id":"https://css-tricks.com/get-ready-for-the-powerful-css-border-shape-property/#webpage"},"image":{"@id":"https://i0.wp.com/css-tricks.com/wp-content/uploads/2026/06/css-border-shape-examples.jpg?fit=1150%2C552&amp;ssl=1"},"inLanguage":"en-US","mainEntityOfPage":{"@id":"https://css-tricks.com/get-ready-for-the-powerful-css-border-shape-property/#webpage"}}]}</script>
<!-- /Rank Math WordPress SEO plugin -->

<link rel='preconnect' href='//i0.wp.com' />
<link rel='preconnect' href='//c0.wp.com' />
<link rel="alternate" type="application/rss+xml" title="CSS-Tricks &raquo; Get Ready For the Powerful CSS border-shape Property! Comments Feed" href="https://css-tricks.com/get-ready-for-the-powerful-css-border-shape-property/feed/" />
<link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://css-tricks.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fcss-tricks.com%2Fget-ready-for-the-powerful-css-border-shape-property%2F" />
<link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://css-tricks.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fcss-tricks.com%2Fget-ready-for-the-powerful-css-border-shape-property%2F&#038;format=xml" />
<style id="wp-img-auto-sizes-contain-inline-css">
img:is([sizes=auto i],[sizes^="auto," i]){contain-intrinsic-size:3000px 1500px}
/*# sourceURL=wp-img-auto-sizes-contain-inline-css */
</style>
<style id="classic-theme-styles-inline-css">
/*! This file is auto-generated */
.wp-block-button__link{color:#fff;background-color:#32373c;border-radius:9999px;box-shadow:none;text-decoration:none;padding:calc(.667em + 2px) calc(1.333em + 2px);font-size:1.125em}.wp-block-file__button{background:#32373c;color:#fff;text-decoration:none}
/*# sourceURL=/wp-includes/css/classic-themes.min.css */
</style>

<style id="css-tricks-baseline-status-style-inline-css">
/*!***************************************************************************************************************************************************************************************************************************************!*\
  !*** css ./node_modules/css-loader/dist/cjs.js??ruleSet[1].rules[4].use[1]!./node_modules/postcss-loader/dist/cjs.js??ruleSet[1].rules[4].use[2]!./node_modules/sass-loader/dist/cjs.js??ruleSet[1].rules[4].use[3]!./src/style.scss ***!
  \***************************************************************************************************************************************************************************************************************************************/
/**
 * The following styles get applied both on the front of your site
 * and in the editor.
 *
 * Replace them with your own styles or remove the file completely.
 */
baseline-status {
  --color-text: #fff;
  --color-outline: var(--orange);
  background: #000;
  border: solid 5px var(--color-outline);
  border-radius: 8px;
  color: var(--color-text);
  display: block;
  margin-block-end: var(--gap);
  padding: calc(var(--gap) / 4);
}
@media (prefers-color-scheme: dark) {
  baseline-status {
    --color-text: #fff;
    --color-link: var(--orange);
  }
}

/*# sourceMappingURL=style-index.css.map*/
/*# sourceURL=https://css-tricks.com/wp-content/plugins/baseline-status/build/style-index.css */
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
<link rel="https://api.w.org/" href="https://css-tricks.com/wp-json/" /><link rel="alternate" title="JSON" type="application/json" href="https://css-tricks.com/wp-json/wp/v2/posts/395508" /><link rel='shortlink' href='https://css-tricks.com/?p=395508' />
<!-- Better Art Direction Styles -->


	<style>img#wpstats{display:none}</style>
		<link rel="site.standard.document" href="at://did:plc:ffm3o4vz473f6q7idxz4pmz7/site.standard.document/3mq2vftqm4vy6" />
<link rel="site.standard.publication" href="at://did:plc:ffm3o4vz473f6q7idxz4pmz7/site.standard.publication/3moisllyxvlob" />
<link rel="icon" href="https://i0.wp.com/css-tricks.com/wp-content/uploads/2021/07/star.png?fit=32%2C32&#038;ssl=1" sizes="32x32" />
<link rel="icon" href="https://i0.wp.com/css-tricks.com/wp-content/uploads/2021/07/star.png?fit=180%2C180&#038;ssl=1" sizes="192x192" />
<link rel="apple-touch-icon" href="https://i0.wp.com/css-tricks.com/wp-content/uploads/2021/07/star.png?fit=180%2C180&#038;ssl=1" />
<meta name="msapplication-TileImage" content="https://i0.wp.com/css-tricks.com/wp-content/uploads/2021/07/star.png?fit=180%2C180&#038;ssl=1" />

<style id="wp-block-heading-inline-css">
h1:where(.wp-block-heading).has-background,h2:where(.wp-block-heading).has-background,h3:where(.wp-block-heading).has-background,h4:where(.wp-block-heading).has-background,h5:where(.wp-block-heading).has-background,h6:where(.wp-block-heading).has-background{padding:1.25em 2.375em}h1.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h1.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h2.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h2.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h3.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h3.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h4.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h4.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h5.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h5.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h6.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h6.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]){rotate:180deg}
/*# sourceURL=https://c0.wp.com/c/7.0.1/wp-includes/blocks/heading/style.min.css */
</style>
<style id="wp-block-image-inline-css">
.wp-block-image>a,.wp-block-image>figure>a{display:inline-block}.wp-block-image img{box-sizing:border-box;height:auto;max-width:100%;vertical-align:bottom}@media not (prefers-reduced-motion){.wp-block-image img.hide{visibility:hidden}.wp-block-image img.show{animation:show-content-image .4s}}.wp-block-image[style*=border-radius] img,.wp-block-image[style*=border-radius]>a{border-radius:inherit}.wp-block-image.has-custom-border img{box-sizing:border-box}.wp-block-image.aligncenter{text-align:center}.wp-block-image.alignfull>a,.wp-block-image.alignwide>a{width:100%}.wp-block-image.alignfull img,.wp-block-image.alignwide img{height:auto;width:100%}.wp-block-image .aligncenter,.wp-block-image .alignleft,.wp-block-image .alignright,.wp-block-image.aligncenter,.wp-block-image.alignleft,.wp-block-image.alignright{display:table}.wp-block-image .aligncenter>figcaption,.wp-block-image .alignleft>figcaption,.wp-block-image .alignright>figcaption,.wp-block-image.aligncenter>figcaption,.wp-block-image.alignleft>figcaption,.wp-block-image.alignright>figcaption{caption-side:bottom;display:table-caption}.wp-block-image .alignleft{float:left;margin:.5em 1em .5em 0}.wp-block-image .alignright{float:right;margin:.5em 0 .5em 1em}.wp-block-image .aligncenter{margin-left:auto;margin-right:auto}.wp-block-image :where(figcaption){margin-bottom:1em;margin-top:.5em}.wp-block-image.is-style-circle-mask img{border-radius:9999px}@supports ((-webkit-mask-image:none) or (mask-image:none)) or (-webkit-mask-image:none){.wp-block-image.is-style-circle-mask img{border-radius:0;-webkit-mask-image:url('data:image/svg+xml;utf8,<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="50"/></svg>');mask-image:url('data:image/svg+xml;utf8,<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="50"/></svg>');mask-mode:alpha;-webkit-mask-position:center;mask-position:center;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;-webkit-mask-size:contain;mask-size:contain}}:root :where(.wp-block-image.is-style-rounded img,.wp-block-image .is-style-rounded img){border-radius:9999px}.wp-block-image figure{margin:0}.wp-lightbox-container{display:flex;flex-direction:column;position:relative}.wp-lightbox-container img{cursor:zoom-in}.wp-lightbox-container img:hover+button{opacity:1}.wp-lightbox-container button{align-items:center;backdrop-filter:blur(16px) saturate(180%);background-color:#5a5a5a40;border:none;border-radius:4px;cursor:zoom-in;display:flex;height:20px;justify-content:center;opacity:0;padding:0;position:absolute;right:16px;text-align:center;top:16px;width:20px;z-index:100}@media not (prefers-reduced-motion){.wp-lightbox-container button{transition:opacity .2s ease}}.wp-lightbox-container button:focus-visible{outline:3px auto #5a5a5a40;outline:3px auto -webkit-focus-ring-color;outline-offset:3px}.wp-lightbox-container button:hover{cursor:pointer;opacity:1}.wp-lightbox-container button:focus{opacity:1}.wp-lightbox-container button:focus,.wp-lightbox-container button:hover,.wp-lightbox-container button:not(:hover):not(:active):not(.has-background){background-color:#5a5a5a40;border:none}.wp-lightbox-overlay{box-sizing:border-box;cursor:zoom-out;height:100vh;left:0;overflow:hidden;position:fixed;top:0;visibility:hidden;width:100%;z-index:100000}.wp-lightbox-overlay .wp-lightbox-close-button{align-items:center;cursor:pointer;display:flex;font-family:inherit;gap:8px;justify-content:center;line-height:1;min-height:40px;min-width:40px;padding:0 4px;position:absolute;right:calc(env(safe-area-inset-right) + 16px);top:calc(env(safe-area-inset-top) + 16px);z-index:5000000}.wp-lightbox-overlay .wp-lightbox-close-button:focus,.wp-lightbox-overlay .wp-lightbox-close-button:hover,.wp-lightbox-overlay .wp-lightbox-close-button:not(:hover):not(:active):not(.has-background){background:none;border:none}.wp-lightbox-overlay .wp-lightbox-close-button:has(.wp-lightbox-close-text:not([hidden])) .wp-lightbox-close-icon svg{height:1em;width:1em}.wp-lightbox-overlay .wp-lightbox-close-icon svg{display:block}.wp-lightbox-overlay .wp-lightbox-navigation-button-next,.wp-lightbox-overlay .wp-lightbox-navigation-button-prev{align-items:center;bottom:16px;cursor:pointer;display:flex;font-family:inherit;gap:4px;justify-content:center;line-height:1;min-height:40px;min-width:40px;padding:0 8px;position:absolute;z-index:2000002}.wp-lightbox-overlay .wp-lightbox-navigation-button-next[hidden],.wp-lightbox-overlay .wp-lightbox-navigation-button-prev[hidden]{display:none}@media (min-width:960px){.wp-lightbox-overlay .wp-lightbox-navigation-button-next,.wp-lightbox-overlay .wp-lightbox-navigation-button-prev{bottom:50%;transform:translateY(-50%)}}.wp-lightbox-overlay .wp-lightbox-navigation-button-next:focus,.wp-lightbox-overlay .wp-lightbox-navigation-button-next:hover,.wp-lightbox-overlay .wp-lightbox-navigation-button-next:not(:hover):not(:active):not(.has-background),.wp-lightbox-overlay .wp-lightbox-navigation-button-prev:focus,.wp-lightbox-overlay .wp-lightbox-navigation-button-prev:hover,.wp-lightbox-overlay .wp-lightbox-navigation-button-prev:not(:hover):not(:active):not(.has-background){background:none;border:none;padding:0 8px}.wp-lightbox-overlay .wp-lightbox-navigation-button-next:has(.wp-lightbox-navigation-text:not([hidden])) .wp-lightbox-navigation-icon svg,.wp-lightbox-overlay .wp-lightbox-navigation-button-prev:has(.wp-lightbox-navigation-text:not([hidden])) .wp-lightbox-navigation-icon svg{display:block;height:1.5em;width:1.5em}.wp-lightbox-overlay .wp-lightbox-navigation-button-prev{left:calc(env(safe-area-inset-left) + 16px)}.wp-lightbox-overlay .wp-lightbox-navigation-button-next{right:calc(env(safe-area-inset-right) + 16px)}.wp-lightbox-overlay .wp-lightbox-navigation-icon svg{vertical-align:middle}.wp-lightbox-overlay .lightbox-image-container{height:var(--wp--lightbox-container-height);left:50%;overflow:hidden;position:absolute;top:50%;transform:translate(-50%,-50%);transform-origin:top left;width:var(--wp--lightbox-container-width);z-index:2000001}.wp-lightbox-overlay .wp-block-image{align-items:center;box-sizing:border-box;display:flex;height:100%;justify-content:center;margin:0;position:relative;transform-origin:0 0;width:100%;z-index:3000000}.wp-lightbox-overlay .wp-block-image img{height:var(--wp--lightbox-image-height);min-height:var(--wp--lightbox-image-height);min-width:var(--wp--lightbox-image-width);width:var(--wp--lightbox-image-width)}.wp-lightbox-overlay .wp-block-image figcaption{display:none}.wp-lightbox-overlay button{background:none;border:none}.wp-lightbox-overlay .scrim{background-color:#fff;height:100%;opacity:.9;position:absolute;width:100%;z-index:2000000}.wp-lightbox-overlay.active{visibility:visible}@media not (prefers-reduced-motion){.wp-lightbox-overlay.active{animation:turn-on-visibility .25s both}.wp-lightbox-overlay.active img{animation:turn-on-visibility .35s both}.wp-lightbox-overlay.show-closing-animation:not(.active){animation:turn-off-visibility .35s both}.wp-lightbox-overlay.show-closing-animation:not(.active) img{animation:turn-off-visibility .25s both}.wp-lightbox-overlay.zoom.active{animation:none;opacity:1;visibility:visible}.wp-lightbox-overlay.zoom.active .lightbox-image-container{animation:lightbox-zoom-in .4s}.wp-lightbox-overlay.zoom.active .lightbox-image-container img{animation:none}.wp-lightbox-overlay.zoom.active .scrim{animation:turn-on-visibility .4s forwards}.wp-lightbox-overlay.zoom.show-closing-animation:not(.active){animation:none}.wp-lightbox-overlay.zoom.show-closing-animation:not(.active) .lightbox-image-container{animation:lightbox-zoom-out .4s}.wp-lightbox-overlay.zoom.show-closing-animation:not(.active) .lightbox-image-container img{animation:none}.wp-lightbox-overlay.zoom.show-closing-animation:not(.active) .scrim{animation:turn-off-visibility .4s forwards}}@keyframes show-content-image{0%{visibility:hidden}99%{visibility:hidden}to{visibility:visible}}@keyframes turn-on-visibility{0%{opacity:0}to{opacity:1}}@keyframes turn-off-visibility{0%{opacity:1;visibility:visible}99%{opacity:0;visibility:visible}to{opacity:0;visibility:hidden}}@keyframes lightbox-zoom-in{0%{transform:translate(calc((-100vw + var(--wp--lightbox-scrollbar-width))/2 + var(--wp--lightbox-initial-left-position)),calc(-50vh + var(--wp--lightbox-initial-top-position))) scale(var(--wp--lightbox-scale))}to{transform:translate(-50%,-50%) scale(1)}}@keyframes lightbox-zoom-out{0%{transform:translate(-50%,-50%) scale(1);visibility:visible}99%{visibility:visible}to{transform:translate(calc((-100vw + var(--wp--lightbox-scrollbar-width))/2 + var(--wp--lightbox-initial-left-position)),calc(-50vh + var(--wp--lightbox-initial-top-position))) scale(var(--wp--lightbox-scale));visibility:hidden}}
/*# sourceURL=https://c0.wp.com/c/7.0.1/wp-includes/blocks/image/style.min.css */
</style>
<style id="wp-block-paragraph-inline-css">
.is-small-text{font-size:.875em}.is-regular-text{font-size:1em}.is-large-text{font-size:2.25em}.is-larger-text{font-size:3em}.has-drop-cap:not(:focus):first-letter{float:left;font-size:8.4em;font-style:normal;font-weight:100;line-height:.68;margin:.05em .1em 0 0;text-transform:uppercase}body.rtl .has-drop-cap:not(:focus):first-letter{float:none;margin-left:.1em}p.has-drop-cap.has-background{overflow:hidden}:root :where(p.has-background){padding:1.25em 2.375em}:where(p.has-text-color:not(.has-link-color)) a{color:inherit}p.has-text-align-left[style*="writing-mode:vertical-lr"],p.has-text-align-right[style*="writing-mode:vertical-rl"]{rotate:180deg}
/*# sourceURL=https://c0.wp.com/c/7.0.1/wp-includes/blocks/paragraph/style.min.css */
</style>
<style id="wp-block-quote-inline-css">
.wp-block-quote{box-sizing:border-box;overflow-wrap:break-word}.wp-block-quote.is-large:where(:not(.is-style-plain)),.wp-block-quote.is-style-large:where(:not(.is-style-plain)){margin-bottom:1em;padding:0 1em}.wp-block-quote.is-large:where(:not(.is-style-plain)) p,.wp-block-quote.is-style-large:where(:not(.is-style-plain)) p{font-size:1.5em;font-style:italic;line-height:1.6}.wp-block-quote.is-large:where(:not(.is-style-plain)) cite,.wp-block-quote.is-large:where(:not(.is-style-plain)) footer,.wp-block-quote.is-style-large:where(:not(.is-style-plain)) cite,.wp-block-quote.is-style-large:where(:not(.is-style-plain)) footer{font-size:1.125em;text-align:right}.wp-block-quote>cite{display:block}
/*# sourceURL=https://c0.wp.com/c/7.0.1/wp-includes/blocks/quote/style.min.css */
</style>
<link rel='stylesheet' id='student-notes-style-css' href='https://css-tricks.com/wp-content/plugins/learndash-notes/dist/css/styles.css?ver=2.0.1' media='all' />
<link rel='stylesheet' id='jquery-ui-smoothness-css' href='https://ajax.googleapis.com/ajax/libs/jqueryui//themes/smoothness/jquery-ui.min.css' media='all' />
<link rel='stylesheet' id='font-awesome-css' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css?ver=4.7.0' media='all' />

</head>

<body class="wp-singular post-template-default single single-post postid-395508 single-format-standard wp-theme-CSS-Tricks-19 jps-theme-CSS-Tricks-19 category-articles">

  <div id="top-of-site-pixel-anchor"></div>

  <header class="site-header" id="site-header">

  <a id="skip-nav" class="skip-nav screen-reader-text" href="#maincontent">Skip to main content</a> 

  <div class="logo">
    <a href="/">
      <div class="screen-reader-text">CSS-Tricks</div>

      <svg class="icon-logo-star" width="35px" height="35px" viewBox="0 0 362.62 388.52" data-spin-me="false">
  <path d="M156.58,239l-88.3,64.75c-10.59,7.06-18.84,11.77-29.43,11.77-21.19,0-38.85-18.84-38.85-40C0,257.83,14.13,244.88,27.08,239l103.6-44.74L27.08,148.34C13,142.46,0,129.51,0,111.85,0,90.66,18.84,73,40,73c10.6,0,17.66,3.53,28.25,11.77l88.3,64.75L144.81,44.74C141.28,20,157.76,0,181.31,0s40,18.84,36.5,43.56L206,149.52l88.3-64.75C304.93,76.53,313.17,73,323.77,73a39.2,39.2,0,0,1,38.85,38.85c0,18.84-12.95,30.61-27.08,36.5L231.93,194.26,335.54,239c14.13,5.88,27.08,18.83,27.08,37.67,0,21.19-18.84,38.85-40,38.85-9.42,0-17.66-4.71-28.26-11.77L206,239l11.77,104.78c3.53,24.72-12.95,44.74-36.5,44.74s-40-18.84-36.5-43.56Z" />
</svg>
            <svg id="Layer_1" class="icon-logo-text" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 974.89 117.95"><g id="CSS-Tricks" style="isolation:isolate"><g style="isolation:isolate"><path d="M66.18,66.2v-.33c0-32.42,24.27-59,58.81-59,17.6,0,29.16,5.21,39.1,12.87a10,10,0,0,1,3.91,8,10,10,0,0,1-16,7.82c-7.82-6.35-16.29-10.26-27.21-10.26-21.67,0-37.63,17.92-37.63,40.24v.33c0,22.32,15.8,40.4,37.63,40.4,12.06,0,20.2-3.91,28.51-10.92a9.12,9.12,0,0,1,6-2.28,9.53,9.53,0,0,1,9.45,9.29,9.63,9.63,0,0,1-