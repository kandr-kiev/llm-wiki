---
source_url: https://webkit.org/blog/18162/release-notes-for-safari-technology-preview-248/
ingested: 2026-07-22
sha256: db011083144dc45500433e765eac5dc66d72c2132bd362567c4b6ed1fb879ebe
blog_source: Hacker News
---
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
    <meta name="robots" content="noodp">

    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes, viewport-fit=cover">
    <meta name="theme-color" content="hsl(203.6, 100%, 12%)">

    <title>  Release Notes for Safari Technology Preview 248 | WebKit</title>

    <meta name="application-name" content="WebKit">

    <link rel="stylesheet" type="text/css" href="https://webkit.org/wp-content/themes/webkit/style.css?2022100501" media="all">
    <link rel="stylesheet" href="https://www.apple.com/wss/fonts?families=SF+Pro,v1" type="text/css">
    <link rel="stylesheet" href="https://www.apple.com/wss/fonts?families=SF+Mono,v2" type="text/css">
    <meta name="supported-color-schemes" content="light dark">

    <noscript>
        <img src="https://shynet.webkit.org/ingress/561b9e53-fb8c-4297-ae4d-bde05e8daa59/pixel.gif">
    </noscript>
    <script defer src="https://shynet.webkit.org/ingress/561b9e53-fb8c-4297-ae4d-bde05e8daa59/script.js"></script>

    <link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="https://webkit.org/feed/">
    <link rel="alternate" type="text/xml" title="RSS .92" href="https://webkit.org/feed/rss/">
    <link rel="alternate" type="application/atom+xml" title="Atom 0.3" href="https://webkit.org/feed/atom/">
    <link rel="pingback" href="https://webkit.org/wp/xmlrpc.php">

    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="shortcut icon" sizes="any" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon.png">

    <meta name='robots' content='max-image-preview:large' />
<link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://webkit.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwebkit.org%2Fblog%2F18162%2Frelease-notes-for-safari-technology-preview-248%2F" />
<link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://webkit.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwebkit.org%2Fblog%2F18162%2Frelease-notes-for-safari-technology-preview-248%2F&#038;format=xml" />
<style id="wp-img-auto-sizes-contain-inline-css">
img:is([sizes=auto i],[sizes^="auto," i]){contain-intrinsic-size:3000px 1500px}
/*# sourceURL=wp-img-auto-sizes-contain-inline-css */
</style>
<style id="wp-block-library-inline-css">
:root{--wp-block-synced-color:#7a00df;--wp-block-synced-color--rgb:122,0,223;--wp-bound-block-color:var(--wp-block-synced-color);--wp-editor-canvas-background:#ddd;--wp-admin-theme-color:#007cba;--wp-admin-theme-color--rgb:0,124,186;--wp-admin-theme-color-darker-10:#006ba1;--wp-admin-theme-color-darker-10--rgb:0,107,160.5;--wp-admin-theme-color-darker-20:#005a87;--wp-admin-theme-color-darker-20--rgb:0,90,135;--wp-admin-border-width-focus:2px}@media (min-resolution:192dpi){:root{--wp-admin-border-width-focus:1.5px}}.wp-element-button{cursor:pointer}:root .has-very-light-gray-background-color{background-color:#eee}:root .has-very-dark-gray-background-color{background-color:#313131}:root .has-very-light-gray-color{color:#eee}:root .has-very-dark-gray-color{color:#313131}:root .has-vivid-green-cyan-to-vivid-cyan-blue-gradient-background{background:linear-gradient(135deg,#00d084,#0693e3)}:root .has-purple-crush-gradient-background{background:linear-gradient(135deg,#34e2e4,#4721fb 50%,#ab1dfe)}:root .has-hazy-dawn-gradient-background{background:linear-gradient(135deg,#faaca8,#dad0ec)}:root .has-subdued-olive-gradient-background{background:linear-gradient(135deg,#fafae1,#67a671)}:root .has-atomic-cream-gradient-background{background:linear-gradient(135deg,#fdd79a,#004a59)}:root .has-nightshade-gradient-background{background:linear-gradient(135deg,#330968,#31cdcf)}:root .has-midnight-gradient-background{background:linear-gradient(135deg,#020381,#2874fc)}:root{--wp--preset--font-size--normal:16px;--wp--preset--font-size--huge:42px}.has-regular-font-size{font-size:1em}.has-larger-font-size{font-size:2.625em}.has-normal-font-size{font-size:var(--wp--preset--font-size--normal)}.has-huge-font-size{font-size:var(--wp--preset--font-size--huge)}:root .has-text-align-center{text-align:center}:root .has-text-align-left{text-align:left}:root .has-text-align-right{text-align:right}.has-fit-text{white-space:nowrap!important}#end-resizable-editor-section{display:none}.aligncenter{clear:both}.items-justified-left{justify-content:flex-start}.items-justified-center{justify-content:center}.items-justified-right{justify-content:flex-end}.items-justified-space-between{justify-content:space-between}.screen-reader-text{word-wrap:normal!important;border:0;clip-path:inset(50%);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}.screen-reader-text:focus{background-color:#ddd;clip-path:none;color:#444;display:block;font-size:1em;height:auto;left:5px;line-height:normal;padding:15px 23px 14px;text-decoration:none;top:5px;width:auto;z-index:100000}html :where(.has-border-color){border-style:solid}html :where([style*=border-color]){border-style:solid}html :where([style*=border-top-color]){border-top-style:solid}html :where([style*=border-right-color]){border-right-style:solid}html :where([style*=border-bottom-color]){border-bottom-style:solid}html :where([style*=border-left-color]){border-left-style:solid}html :where([style*=border-width]){border-style:solid}html :where([style*=border-top-width]){border-top-style:solid}html :where([style*=border-right-width]){border-right-style:solid}html :where([style*=border-bottom-width]){border-bottom-style:solid}html :where([style*=border-left-width]){border-left-style:solid}html :where(img[class*=wp-image-]){height:auto;max-width:100%}:where(figure){margin:0 0 1em}html :where(.is-position-sticky){--wp-admin--admin-bar--position-offset:var(--wp-admin--admin-bar--height,0px)}@media screen and (max-width:600px){html :where(.is-position-sticky){--wp-admin--admin-bar--position-offset:0px}}

/*# sourceURL=/wp-includes/css/dist/block-library/common.min.css */
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

<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://webkit.org/wp/xmlrpc.php?rsd" />
<meta name="generator" content="WordPress 7.0.2" />
<link rel="canonical" href="https://webkit.org/blog/18162/release-notes-for-safari-technology-preview-248/" />
<link rel='shortlink' href='https://webkit.org/?p=18162' />

    <!-- Schema.org markup -->
    <meta itemprop="name" content="Release Notes for Safari Technology Preview 248">
    <meta itemprop="description" content="Safari Technology Preview Release 248 is now available for download for macOS Golden Gate and macOS Tahoe.">
    <meta itemprop="image" content="https://webkit.org/wp-content/themes/webkit/images/preview-card.jpg">

    <!-- Twitter Card data -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image:src" content="https://webkit.org/wp-content/themes/webkit/images/preview-card.jpg">
    <meta name="twitter:site" content="@webkit">
    <meta name="twitter:title" content="Release Notes for Safari Technology Preview 248">
    <meta name="twitter:description" content="Safari Technology Preview Release 248 is now available for download for macOS Golden Gate and macOS Tahoe.">

    <!-- Open Graph data -->
    <meta property="og:title" content="Release Notes for Safari Technology Preview 248">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://webkit.org/blog/18162/release-notes-for-safari-technology-preview-248/">
    <meta property="og:image" content="https://webkit.org/wp-content/themes/webkit/images/preview-card.jpg">
    <meta property="og:description" content="Safari Technology Preview Release 248 is now available for download for macOS Golden Gate and macOS Tahoe.">
    <meta property="og:site_name" content="WebKit">
    <meta property="article:published_time" content="2026-07-22T11:58:31-07:00">
    <meta property="article:modified_time" content="2026-07-22T11:58:31-07:00">
    <meta property="article:section" content="Safari Technology Preview">
</head>
<body class="wp-singular post-template-default single single-post postid-18162 single-format-standard wp-theme-webkit">
    <!-- Copyright © 2020 Apple Inc. All rights reserved. -->
<svg xmlns="http://www.w3.org/2000/svg">
	<style> svg { display: block; width: 0; height: 0; } </style>
    <filter id="invertLightness" x="0" y="0" style="color-interpolation-filters: sRGB">
        <feColorMatrix type="matrix" in="SourceGraphic" result="red" values="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 1" />
        <feColorMatrix type="matrix" in="SourceGraphic" result="green" values="0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 1" />
        <feColorMatrix type="matrix" in="SourceGraphic" result="blue" values="0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1" />
        <feBlend in="red" in2="green" mode="lighten" result="maxyellow" />
        <feBlend in="maxyellow" in2="blue" mode="lighten" result="max" />
        <feBlend in="red" in2="green" mode="darken" result="minyellow" />
        <feBlend in="minyellow" in2="blue" mode="darken" result="min" />
        <feComponentTransfer result="adjustment" in="min">
            <feFuncR type="linear" intercept="1" slope="-1" />
            <feFuncG type="linear" intercept="1" slope="-1" />
            <feFuncB type="linear" intercept="1" slope="-1" />
        </feComponentTransfer>
        <feComposite operator="arithmetic" in="SourceGraphic" in2="adjustment" k1="0" k2="1" k3="1" k4="-1" result="channelAdjustment" />
        <feComposite operator="arithmetic" in="channelAdjustment" in2="max" k1="0" k2="1" k3="-1" k4="1" result="finalColors" />
        <feComposite operator="in" in="finalColors" in2="SourceAlpha" />
    </filter>
</svg>    <header aria-label="WebKit.org Header" id="header">
        <div class="page-width">
        <a href="/"><div id="logo" class="site-logo">WebKit</div></a>
        <nav id="site-nav" aria-label="Site Menu">
<div class="menu-main-menu-container"><input type="checkbox" id="menu-main-menu-toggle" class="menu-toggle" /><label for="menu-main-menu-toggle" class="label-toggle main-menu" data-open="Main Menu" data-close="Close Menu"></label><ul id="menu-main-menu" class="menu" role="menubar"><li id="menu-item-6091" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6091"><a href="https://webkit.org/downloads/" role="menuitem">Downloads</a></li>
<li id="menu-item-4272" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-4272"><input type="checkbox" id="toggle-4272" class="menu-toggle" /><a href="#nav-sub-menu" role="menuitem" aria-haspopup="true" aria-owns="sub-menu-for-4272" aria-controls="sub-menu-for-4272" aria-expanded="true"><label for="toggle-4272" class="label-toggle">Feature Status</label></a>
<ul class="sub-menu sub-menu-layer" role="menu" id="sub-menu-for-4272">
	<li id="menu-item-13052" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-13052"><a href="https://webkit.org/css-status/" role="menuitem">CSS Features</a></li>
	<li id="menu-item-14388" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14388"><a href="https://webkit.org/standards-positions/" role="menuitem">Standards Positions</a></li>
</ul>
</li>
<li id="menu-item-9988" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-9988"><input type="checkbox" id="toggle-9988" class="menu-toggle" /><a href="#nav-sub-menu" role="menuitem" aria-haspopup="true" aria-owns="sub-menu-for-9988" aria-controls="sub-menu-for-9988" aria-expanded="true"><label for="toggle-9988" class="label-toggle">Documentation</label></a>
<ul class="sub-menu sub-menu-layer" role="menu" id="sub-menu-for-9988">
	<li id="menu-item-9989" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9989"><a href="/web-inspector" role="menuitem">Web Inspector</a></li>
	<li id="menu-item-10868" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-10868"><a href="https://webkit.org/tracking-prevention/" role="menuitem">Tracking Prevention</a></li>
</ul>
</li>
<li id="menu-item-4282" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-4282"><input type="checkbox" id="toggle-4282" class="menu-toggle" /><a href="#nav-sub-menu" role="menuitem" aria-haspopup="true" aria-owns="sub-menu-for-4282" aria-controls="sub-menu-for-4282" aria-expanded="true"><label for="toggle-4282" class="label-toggle">Policies</label></a>
<ul class="sub-menu sub-menu-layer" role="menu" id="sub-menu-for-4282">
	<li id="menu-item-10037" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-10037"><a href="https://webkit.org/project/" role="menuitem">Project Goals</a></li>
	<li id="menu-item-13077" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-13077"><a href="https://webkit.org/bug-prioritization/" role="menuitem">Bug Prioritization</a></li>
	<li id="menu-item-13076" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-13076"><a href="https://webkit.org/bug-report-guidelines/" role="menuitem">Bug Report Guidelines</a></li>
	<li id="menu-item-13075" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-13075"><a href="https://webkit.org/code-style-guidelines/" role="menuitem">Code Style Guidelines</a></li>
	<li id="menu-item-13074" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-13074"><a href="https://webkit.org/commit-and-review-policy/" role="menuitem">Commit and Review Policy</a></li>
	<li id="menu-item-13073" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-13073"><a href="https://webkit.org/feature-policy/" role="menuitem">Feature Policy</a></li>
	<li id="menu-item-13072" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-13072"><a href="https://webkit.org/security-policy/" role="menuitem">Security Policy</a></li>
	<li id="menu-item-13071" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-13071"><a href="https://webkit.org/tracking-prevention-policy/" role="menuitem">Tracking Prevention Policy</a></li>
</ul>
</li>
<li id="menu-item-4274" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-4274"><input type="checkbox" id="toggle-4274" class="menu-toggle" /><a href="#nav-sub-menu" role="menuitem" aria-haspopup="true" aria-owns="sub-menu-for-4274" aria-controls="sub-menu-for-4274" aria-expanded="true"><label for="toggle-4274" class="label-toggle">Contribute</label></a>
<ul class="sub-menu sub-menu-layer" role="menu" id="sub-menu-for-4274">
	<li id="menu-item-4277" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4277"><a href="https://webkit.org/getting-started/" role="menuitem">Getting Started</a></li>
	<li id="menu-item-4284" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4284"><a href="https://webkit.org/contributing-code/" role="menuitem">Contributing Code</a></li>
	<li id="menu-item-4281" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4281"><a href="https://webkit.org/testing-contributions/" role="menuitem">Testing Contributions</a></li>
	<li id="menu-item-4273" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4273"><a href="https://webkit.org/reporting-bugs/" role="menuitem">How to Report Bugs</a></li>
	<li id="menu-item-4278" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4278"><a href="https://github.com/WebKit/WebKit" role="menuitem">GitHub Repository</a></li>
</ul>
</li>
<li id="menu-item-4270" class="menu-item menu-item-type-post_type menu-item-object-page current_page_parent menu-item-has-children menu-item-4270"><input type="checkbox" id="toggle-4270" class="menu-toggle" /><a href="#nav-sub-menu" role="menuitem" aria-haspopup="true" aria-owns="sub-menu-for-4270" aria-controls="sub-menu-for-4270" aria-expanded="true"><label for="toggle-4270" class="label-toggle">Blog</label></a>
<ul class="sub-menu sub-menu-layer" role="menu" id="sub-menu-for-4270">
	<li id="menu-item-13057" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-13057"><a href="https://webkit.org/blog/category/news/" role="menuitem">News Posts</a></li>
	<li id="menu-item-13058" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-13058"><a href="https://webkit.org/blog/category/css/" role="menuitem">CSS Posts</a></li>
	<li id="menu-item-13063" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-13063"><a href="https://webkit.org/blog/category/contributing/" role="menuitem">Contributing Posts</a></li>
	<li id="menu-item-13062" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-13062"><a href="https://webkit.org/blog/category/privacy/" role="menuitem">Privacy Posts</a></li>
	<li id="menu-item-13060" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-13060"><a href="https://webkit.org/blog/category/performance/" role="menuitem">Performance Posts</a></li>
	<li id="menu-item-13061" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-13061"><a href="https://webkit.org/blog/category/javascript/" role="menuitem">JavaScript Posts</a></li>
	<li id="menu-item-13056" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-13056"><a href="https://webkit.org/blog/category/standards/" role="menuitem">Standards Posts</a></li>
	<li id="menu-item-13059" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-13059"><a href="https://webkit.org/blog/category/web-inspector/" role="menuitem">Web Inspector Posts</a></li>
	<li id="menu-item-13055" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-13055"><a href="https://webkit.org/blog/category/safari-technology-preview/" role="menuitem">Safari Technology Preview Posts</a></li>
</ul>
</li>
<li><form action="/" method="get"><input type="search" name="s" class="search-input" value=""></form></li></ul></div></nav>
        </div>
    </header>

<main id="content">
    <div class="page-width">
    
        <article class="post-18162 post type-post status-publish format-standard hentry category-safari-technology-preview" id="post-18162">
            <h1><a href="https://webkit.org/blog/18162/release-notes-for-safari-technology-preview-248/" rel="bookmark" title="Permanent Link: Release Notes for Safari Technology Preview 248">Release Notes for Safari Technology Preview 248</a></h1>
            <div class="byline">
                <p class="date">Jul 22, 2026</p>
                <p class="author">by <span>Jon Davis</span></p>
                            </div>

            <div class="bodycopy">
                                
                <p><a href="https://webkit.org/blog/6017/introducing-safari-technology-preview/">Safari Technology Preview</a> Release 248 is now <a href="https://developer.apple.com/safari/resources/">available for download</a> for macOS Golden Gate and macOS Tahoe. If you already have Safari Technology Preview installed, you can update it in System Settings under General → Software Update.</p>
<p>This release includes WebKit changes between: <a href="https://github.com/WebKit/WebKit/compare/666fd351d376a96584c357fee973f74f701800be...84565916779faa5f54b09bc075add03a779723c1">315567@main&#8230;316817@main</a>.</p>
<h3>Accessibility</h3>
<h4>Resolved Issues</h4>
<ul>
<li>Fixed VoiceOver on Safari unable to navigate to content revealed by disclosure widgets using <code>hidden="until-found"</code>. (<a href="https://commits.webkit.org/315964@main">315964@main</a>)  (173228707)</li>
<li>Fixed stale <code>aria-labelledby</code> when the referenced element dynamically changes its <code>aria-label</code>. (<a href="https://commits.webkit.org/316316@main">316316@main</a>)  (180319221)</li>
</ul>
<h3>CSS</h3>
<h4>New Features</h4>
<ul>
<li>Added support for forwarding missing color components when interpolating between analogous color spaces. (<a href="https://commits.webkit.org/315569@main">315569@main</a>)  (180239320)</li>
<li>Added support for the <code>no-clamp</code> option on the CSS <code>progress()</code> function. (<a href="https://commits.webkit.org/315977@main">315977@main</a>)  (180473472)</li>
</ul>
<h4>Resolved Issues</h4>
<ul>
<li>Fixed serialization of various CSS at-rules not escaping identifiers. (<a href="https://commits.webkit.org/315795@main">315795@main</a>)  (178750383)</li>
<li>Fixed <code>:last-child</code> and related selectors incorrectly gating on parser state outside of style resolution. (<a href="https://commits.webkit.org/316495@main">316495@main</a>)  (178879939)</li>
<li>Fixed changing the <code>color-scheme</code> of an <code>&lt;iframe&gt;</code> not invalidating the appearance of the embedded document. (<a href="https://commits.webkit.org/316467@main">316467@main</a>)  (179177141)</li>
<li>Fixed CSS scroll snap re-snap to prefer the fragment-targeted (<code>:target</code>) snap area over other aligned snap targets. (<a href="https://commits.webkit.org/315880@main">315880@main</a>)  (180108825)</li>
<li>Fixed the CSS preload scanner failing to preload <code>@import</code> rules that follow an <code>@layer</code> statement rule. (<a href="https://commits.webkit.org/315576@main">315576@main</a>)  (180170656)</li>
<li>Fixed serialization of <code>CSSViewTransitionRule</code>. (<a href="https://commits.webkit.org/315614@main">315614@main</a>)  (180170814)</li>
<li>Fixed <code>MediaList.deleteMedium()</code> to parse its argument as a media query and remove all matching queries. (<a href="https://commits.webkit.org/315579@main">315579@main</a>)  (180270019)</li>
<li>Fixed <code>MediaList.appendMedium()</code> to parse its argument as a single media query and suppress duplicates. (<a href="https://commits.webkit.org/315594@main">315594@main</a>)  (180291283)</li>
<li>Fixed grid items with <code>stretch</code> or <code>fit-content</code> preferred sizes computing incorrect minimum-content contributions when sizing tracks. (<a href="https://commits.webkit.org/316296@main">316296@main</a>)  (180748205)</li>
<li>Fixed inserting a CSS rule while a view transition is active causing the group animation to snap to its final state. (<a href="https://commits.webkit.org/316436@main">316436@main</a>)  (181100818)</li>
<li>Fixed CSS <code>var()</code> to only resolve its fallback when the first argument resolves to the guaranteed-invalid value. (<a href="https://commits.webkit.org/316280@main">316280@main</a>)  (181114298)</li>
<li>Fixed navigating away from a render-blocked document before its first rendering opportunity incorrectly firing <code>pagereveal</code> and starting an outbound cross-document view transition. (<a href="https://commits.webkit.org/316446@main">316446@main</a>)  (181191512)</li>
</ul>
<h3>Editing</h3>
<h4>Resolved Issues</h4>
<ul>
<li>Fixed drag images of DOM elements with CSS transforms not rendering correctly. (<a href="https://commits.webkit.org/316077@main">316077@main</a>)  (99614217)</li>
<li>Fixed opaque DOM mutations coming from dictation on iOS. (<a href="https://commits.webkit.org/316049@main">316049@main</a>)  (163454428)</li>
<li>Fixed deletion in an editable table leaving an empty trailing table row behind. (<a href="https://commits.webkit.org/315990@main">315990@main</a>)  (180877315)</li>
<li>Fixed vertical caret movement in editable content ignoring the requested editable-type parameter. (<a href="https://commits.webkit.org/316241@main">316241@main</a>)  (181000174)</li>
</ul>
<h3>Forms</h3>
<h4>Resolved Issues</h4>
<ul>
<li>Fixed the concentric inner-button corner radius on horizontal text form controls incorrectly ignoring the bottom inset. (<a href="https://commits.webkit.org/316022@main">316022@main</a>)  (180869927)</li>
</ul>
<h3>Images</h3>
<h4>Resolved Issues</h4>
<ul>
<li>Fixed a regression where RGB gain map images were decoded to 8 bits per channel, causing a color shift and incorrect brightness. (<a href="https://commits.webkit.org/316069@main">316069@main</a>)  (179152566)</li>
<li>Fixed handling of the gain-map target pixel format when decoding HDR images to fall back safely when the format cannot be parsed. (<a href="https://commits.webkit.org/316405@main">316405@main</a>)  (181180757)</li>
</ul>
<h3>JavaScript</h3>
<h4>New Features</h4>
<ul>
<li>Added support for the TC39 BigInt Math proposal, exposing <code>Math</code>-equivalent methods on <code>BigInt</code> such as <code>BigInt.pow</code> and <code>BigInt.sqrt</code>. (<a href="https://commits.webkit.org/315974@main">315974@main</a>)  (152472996)</li>
</ul>
<h3>Media</h3>
<h4>Resolved Issues</h4>
<ul>
<li>Fixed <code>&lt;audio&gt;</code> and <code>&lt;video&gt;</code> controls rendering incorrectly when rotated via CSS transform. (<a href="https://commits.webkit.org/315718@main">315718@main</a>)  (37516619)</li>
<li>Fixed subtitles and closed captions not appearing in fullscreen video on iPhone. (<a href="https://commits.webkit.org/315789@main">315789@main</a>)  (175298523)</li>
<li>Fixed ArrayBuffer-backed YUV <code>VideoFrame</code> with a <code>visibleRect</code> rendering with offset chroma channels. (<a href="https://commits.webkit.org/315742@main">315742@main</a>)  (180202939)</li>
<li>Fixed video playback of streams from certain sources such as security cameras not working. (<a href="https://commits.webkit.org/315774@main">315774@main</a>)  (180411019)</li>
<li>Fixed transient device rotation resulting in captured video frames having the wrong orientation. (<a href="https://commits.webkit.org/315821@main">315821@main</a>)  (180429147)</li>
<li>Fixed Media Source Extensions playback and seek by loosening the gap tolerance between buffered ranges. (<a href="https://commits.webkit.org/316146@main">316146@main</a>)  (180439090)</li>
</ul>
<h3>Navigation</h3>
<h4>Resolved Issues</h4>
<ul>
<li>Fixed a <code>&lt;meta http-equiv="refresh"&gt;</code> to a URL differing only in fragment identifier being incorrectly treated as a page reload. (<a href="https://commits.webkit.org/316001@main">316001@main</a>)  (176933795)</li>
</ul>
<h3>Networking</h3>
<h4>Resolved Issues</h4>
<ul>
<li>Fixed URL path separators being encoded as <code>%2F</code> following a percent-encoded Armenian path segment. (<a href="https://commits.webkit.org/315627@main">315627@main</a>)  (180067095)</li>
</ul>
<h3>Rendering</h3>
<h4>Resolved Issues</h4>
<ul>
<li>Fixed the background of a composited <code>&lt;html&gt;</code> element not being repainted when the <code>&lt;body&gt;</code> background changed. (<a href="https://commits.webkit.org/316415@main">316415@main</a>)  (177975964)</li>
<li>Fixed a regression where block-axis padding on a <code>flex</code> column container with <code>overflow: auto</code> was excluded from <code>scrollHeight</code>. (<a href="https://commits.webkit.org/315813@main">315813@main</a>)  (179376053)</li>
<li>Fixed an issue where an <code>&lt;img&gt;</code> embedding an SVG with a near-integral intrinsic width rendered one device pixel narrower than expected. (<a href="https://commits.webkit.org/315807@main">315807@main</a>)  (180490343)</li>
<li>Fixed elements with <code>filter: drop-shadow()</code> not being fully repainted when a child is resized. (<a href="https://commits.webkit.org/316450@main">316450@main</a>)  (181284741)</li>
</ul>
<h3>SVG</h3>
<h4>Resolved Issues</h4>
<ul>
<li>Fixed SVG SMIL length animations to reject invalid <code>to</code>, <code>from</code>, and <code>by</code> values such as those with leading whitespace. (<a href="https://commits.webkit.org/315949@main">315949@main</a>)  (118537155)</li>
<li>Fixed Unicode text with complex scripts not rendering correctly along a curved <code>&lt;textPath&gt;</code>. (<a href="https://commits.webkit.org/316144@main">316144@main</a>)  (120284006)</li>
<li>Fixed <code>SVGLength.convertToSpecifiedUnits()</code> failing when converting from <code>px</code> to <code>%</code>, <code>em</code>, or <code>ex</code>. (<a href="https://commits.webkit.org/315953@main">315953@main</a>)  (172056830)</li>
<li>Fixed SVG geometry presentation attributes like <code>cx</code>, <code>cy</code>, <code>r</code>, <code>rx</code>, <code>ry</code>, <code>x</code>, <code>y</code>, <code>width</code>, and <code>height</code> being incorrectly applied to elements such as <code>&lt;g&gt;</code> on which they are not permitted. (<a href="https://commits.webkit.org/315946@main">315946@main</a>)  (175672111)</li>
<li>Fixed an issue where the per-character <code>rotate</code> attribute was discarded on a <code>&lt;textPath&gt;</code>, so it now composes with the path tangent angle. (<a href="https://commits.webkit.org/315786@main">315786@main</a>)  (178044478)</li>
<li>Fixed several SVG styling spec-compliance failures. (<a href="https://commits.webkit.org/316174@main">316174@main</a>)  (181052042)</li>
<li>Fixed dynamic changes to <code>orient</code> and <code>markerUnits</code> on <code>&lt;marker&gt;</code> not repainting elements that reference it. (<a href="https://commits.webkit.org/316350@main">316350@main</a>)  (181106538)</li>
<li>Fixed SVG SMIL <code>number</code>, <code>integer-optional-integer</code>, <code>number-optional-number</code>, and <code>path</code> animations to not apply when their <code>from</code>, <code>to</code>, or <code>by</code> values fail to parse. (<a href="https://commits.webkit.org/316468@main">316468@main</a>)  (181308150)</li>
</ul>
<h3>Scrolling</h3>
<h4>Resolved Issues</h4>
<ul>
<li>Fixed CSS scroll snap points inside zero-sized elements not working correctly. (<a href="https://commits.webkit.org/315948@main">315948@main</a>)  (172863699)</li>
<li>Fixed CSS scroll snap re-snap to prefer a snap area that contains the focused or fragment-targeted element. (<a href="https://commits.webkit.org/315927@main">315927@main</a>)  (180707984)</li>
</ul>
<h3>Security</h3>
<h4>Resolved Issues</h4>
<ul>
<li>Fixed a regression where some websites failed to display and logged Content Security Policy errors in the console. (<a href="https://commits.webkit.org/316290@main">316290@main</a>)  (179684592)</li>
<li>Fixed same-page navigations being incorrectly checked against Content Security Policy. (<a href="https://commits.webkit.org/315759@main">315759@main</a>)  (180342503)</li>
<li>Fixed Content Security Policy <code>frame-ancestors</code> violations in report-only policies being ignored instead of reported. (<a href="https://commits.webkit.org/315753@main">315753@main</a>)  (180447621)</li>
<li>Fixed Content Security Policy parsing to reject trailing characters after the closing quote on <code>nonce-source</code> and <code>hash-source</code> values. (<a href="https://commits.webkit.org/316008@main">316008@main</a>)  (180903857)</li>
<li>Fixed Content Security Policy <code>trusted-types</code> expressions to reject trailing characters after keywords and the wildcard. (<a href="https://commits.webkit.org/316089@main">316089@main</a>)  (180973793)</li>
</ul>
<h3>Storage</h3>
<h4>Resolved Issues</h4>
<ul>
<li>Fixed an issue where IndexedDB transactions could be blocked for an extended period before starting when another page&#8217;s transaction was suspended in the background. (<a href="https://commits.webkit.org/315609@main">315609@main</a>)  (178769599)</li>
</ul>
<h3>Web API</h3>
<h4>Resolved Issues</h4>
<ul>
<li>Fixed the Async Clipboard API to request paste access asynchronously. (<a href="https://commits.webkit.org/315997@main">315997@main</a>)  (75969974)</li>
<li>Fixed Digital Credentials to surface <code>OperationError</code> for platform-cancellation and unknown errors instead of <code>AbortError</code> or <code>UnknownError</code>. (<a href="https://commits.webkit.org/315973@main">315973@main</a>)  (174308268)</li>
<li>Fixed Digital Credentials rejecting with the wrong error code and synchronously; rejections are now queued as a task with the correct error. (<a href="https://commits.webkit.org/315895@main">315895@main</a>)  (174895437)</li>
<li>Fixed <code>KeyboardEvent.getModifierState("AltGraph")</code> and <code>MouseEvent.getModifierState("AltGraph")</code> always returning <code>false</code>. (<a href="https://commits.webkit.org/315804@main">315804@main</a>)  (180597374)</li>
<li>Fixed <code>Credential.type</code> returning <code>"digital-credential"</code> instead of <code>"digital"</code> for digital credentials. (<a href="https://commits.webkit.org/315891@main">315891@main</a>)  (180618646)</li>
<li>Fixed aborting <code>navigator.credentials.get()</code> leaving the digital-credentials document picker stuck on screen. (<a href="https://commits.webkit.org/316494@main">316494@main</a>)  (180812397)</li>
<li>Fixed <code>FileReader.readAsText()</code> ignoring the <code>charset</code> parameter of the <code>Blob</code>&#8216;s MIME type. (<a href="https://commits.webkit.org/315996@main">315996@main</a>)  (180890703)</li>
</ul>
<h3>Web Inspector</h3>
<h4>Resolved Issues</h4>
<ul>
<li>Fixed showing ES2022 class private fields, methods, and accessors when inspecting object instances in the Console. (<a href="https://commits.webkit.org/316171@main">316171@main</a>)  (88527162)</li>
<li>Fixed symbolic breakpoints in the debugger so they work with intrinsic functions. (<a href="https://commits.webkit.org/315713@main">315713@main</a>)  (99037335)</li>
<li>Fixed a JavaScript breakpoint on a line containing only a semicolon not being triggered. (<a href="https://commits.webkit.org/316519@main">316519@main</a>)  (126707973)</li>
<li>Fixed the Console REPL to allow redefinition of variables declared with <code>let</code> and <code>const</code>. (<a href="https://commits.webkit.org/316523@main">316523@main</a>)  (143140659)</li>
<li>Fixed the Timeline exporting and importing the wrong timestamp for <code>performance.mark()</code> records. (<a href="https://commits.webkit.org/316073@main">316073@main</a>)  (145226764)</li>
<li>Fixed local response overrides mapped to a file being interpreted as Latin-1 (ISO-8859-1) instead of their actual encoding. (<a href="https://commits.webkit.org/316074@main">316074@main</a>)  (149847746)</li>
<li>Fixed the Media Logging setting not persisting across page loads. (<a href="https://commits.webkit.org/315758@main">315758@main</a>)  (154766890)</li>
<li>Fixed symbolic breakpoints to work with native constructors such as <code>Array</code>, <code>Date</code>, <code>EventTarget</code>, and <code>Worker</code>. (<a href="https://commits.webkit.org/316262@main">316262@main</a>)  (157178256)</li>
<li>Fixed missing stack traces for MIME type errors when importing modules. (<a href="https://commits.webkit.org/316529@main">316529@main</a>)  (169396940)</li>
<li>Fixed the Accessibility sidebar being empty for nodes inside cross-origin iframes. (<a href="https://commits.webkit.org/316399@main">316399@main</a>)  (178562336)</li>
<li>Fixed inline style invalidation to batch <code>DOM.getAttributes</code> commands per tick in cross-origin iframes instead of issuing one command per node. (<a href="https://commits.webkit.org/316487@main">316487@main</a>)  (178830496)</li>
<li>Fixed DOM Storage read and write commands to resolve against the frame&#8217;s own origin in cross-origin iframes. (<a href="https://commits.webkit.org/316501@main">316501@main</a>)  (179249711)</li>
<li>Fixed a moved breakpoint reverting to its original location after closing and reopening Web Inspector. (<a href="https://commits.webkit.org/315585@main">315585@main</a>)  (180083858)</li>
<li>Fixed showing the formatted parameters string for prototype objects such as <code>Map.prototype</code>. (<a href="https://commits.webkit.org/315599@main">315599@main</a>)  (180298712)</li>
<li>Fixed missing formatted parameter strings for object shorthand methods and arrow functions. (<a href="https://commits.webkit.org/315723@main">315723@main</a>)  (180466459)</li>
<li>Fixed an unnecessary colon appearing in front of non-class function properties. (<a href="https://commits.webkit.org/315731@main">315731@main</a>)  (180476445)</li>
<li>Fixed a self-canceling ternary that produced an incorrect cross-axis direction in the flex overlay. (<a href="https://commits.webkit.org/316429@main">316429@main</a>)  (181198803)</li>
<li>Fixed the color picker force-converting picked colors to Display P3. (<a href="https://commits.webkit.org/316419@main">316419@main</a>)  (181201503)</li>
<li>Fixed <code>Page.searchInResources</code> silently omitting cache-backed resources from search results. (<a href="https://commits.webkit.org/316421@main">316421@main</a>)  (181202027)</li>
<li>Fixed duplicate invalid CSS declarations both incorrectly displaying as Active in the Styles sidebar. (<a href="https://commits.webkit.org/316418@main">316418@main</a>)  (181203080)</li>
<li>Fixed adopted constructable stylesheets being misclassified as User Agent stylesheets in cross-origin iframes. (<a href="https://commits.webkit.org/316433@main">316433@main</a>)  (181204768)</li>
<li>Fixed an unsigned underflow that caused the DOM agent to spuriously report power-efficient playback. (<a href="https://commits.webkit.org/316443@main">316443@main</a>)  (181205602)</li>
<li>Fixed <code>Network.setExtraHTTPHeaders</code> to replace previously set headers instead of accumulating them. (<a href="https://commits.webkit.org/316444@main">316444@main</a>)  (181282814)</li>
</ul>
<h3>WebDriver</h3>
<h4>New Features</h4>
<ul>
<li>Added WebDriver support for the Digital Credentials API, including commands to simulate wallet payloads, indefinite waits, and user rejection. (<a href="https://commits.webkit.org/316435@main">316435@main</a>)  (168941907)</li>
</ul>
<h3>WebRTC</h3>
<h4>Resolved Issues</h4>
<ul>
<li>Fixed the WebProcess <code>AudioSession</code> to remain active while microphone capture is live. (<a href="https://commits.webkit.org/316394@main">316394@main</a>)  (180505014)</li>
<li>Fixed the <code>configurationchange</code> event being dropped when a source-side change occurred while a <code>MediaStreamTrack</code> was muted; the event is now deferred until unmute. (<a href="https://commits.webkit.org/316301@main">316301@main</a>)  (180728609)</li>
</ul>

                            </div>
        </article>

        <aside class="nextrouter" aria-label="Next/Previous posts">
            <div class="bodycopy">
                                    </div>
        </aside>
        <aside class="nextrouter previous" aria-label="Next/Previous posts">
            <div class="bodycopy">
            <a class="page-numbers prev-post" href="https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/" rel="prev"><div class="nextrouter-copy"><span class="label">Previously</span><span class="title">Introducing the Safari MCP server for web developers</span><span class="link">Learn more</span></div></a>            </div>
        </aside>

    
    
    </div><!--.page-width-->
</main><!-- #content -->

<footer>
    <div class="page-width">
        <nav id="footer-nav" aria-label="Footer menu"><div class="menu-footer-menu-container"><ul id="menu-footer-menu" class="menu"><li id="menu-item-7617" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-7617"><a rel="me" href="https://front-end.social/@webkit">@webkit@front-end.social</a></li>
<li id="menu-item-5365" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-5365"><a href="https://webkit.org/sitemap/">Site Map</a></li>
<li id="menu-item-4185" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4185"><a href="http://www.apple.com/legal/privacy/">Privacy Policy</a></li>
<li id="menu-item-4287" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4287"><a href="https://webkit.org/licensing-webkit/">Licensing WebKit</a></li>
<li id="menu-item-4187" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4187"><a href="https://webkit.org/terms-of-use/">WebKit and the WebKit logo are trademarks of A