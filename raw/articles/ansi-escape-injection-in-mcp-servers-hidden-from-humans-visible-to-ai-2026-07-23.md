---
source_url: https://brightsec.com/research/detecting-ansi-escape-sequence-injection-in-mcp-servers-with-dast/
ingested: 2026-07-23
sha256: f40156e77161c0cf2807d744a32888f5b438b8d074198b027285afbe54716555
blog_source: Hacker News AI
---
<!DOCTYPE html><html lang="en-US" prefix="og: https://ogp.me/ns#"><head><script data-no-optimize="1">var litespeed_docref=sessionStorage.getItem("litespeed_docref");litespeed_docref&&(Object.defineProperty(document,"referrer",{get:function(){return litespeed_docref}}),sessionStorage.removeItem("litespeed_docref"));</script> <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
 <script id="google_gtagjs-js-consent-mode-data-layer" type="litespeed/javascript">window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}
gtag('consent','default',{"ad_personalization":"denied","ad_storage":"denied","ad_user_data":"denied","analytics_storage":"denied","functionality_storage":"denied","security_storage":"denied","personalization_storage":"denied","region":["AT","BE","BG","CH","CY","CZ","DE","DK","EE","ES","FI","FR","GB","GR","HR","HU","IE","IS","IT","LI","LT","LU","LV","MT","NL","NO","PL","PT","RO","SE","SI","SK"],"wait_for_update":500});window._googlesitekitConsentCategoryMap={"statistics":["analytics_storage"],"marketing":["ad_storage","ad_user_data","ad_personalization"],"functional":["functionality_storage","security_storage"],"preferences":["personalization_storage"]};window._googlesitekitConsents={"ad_personalization":"denied","ad_storage":"denied","ad_user_data":"denied","analytics_storage":"denied","functionality_storage":"denied","security_storage":"denied","personalization_storage":"denied","region":["AT","BE","BG","CH","CY","CZ","DE","DK","EE","ES","FI","FR","GB","GR","HR","HU","IE","IS","IT","LI","LT","LU","LV","MT","NL","NO","PL","PT","RO","SE","SI","SK"],"wait_for_update":500}</script> <title>Detecting ANSI Escape Sequence Injection in MCP Servers with DAST | Bright Security</title><meta name="description" content="ANSI escape sequences were designed for terminals, not for language models. They are invisible control codes that tell a terminal to change colors, hide text,"/><meta name="robots" content="follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large"/><link rel="canonical" href="https://brightsec.com/research/detecting-ansi-escape-sequence-injection-in-mcp-servers-with-dast/" /><meta property="og:locale" content="en_US" /><meta property="og:type" content="article" /><meta property="og:title" content="Detecting ANSI Escape Sequence Injection in MCP Servers with DAST | Bright Security" /><meta property="og:description" content="ANSI escape sequences were designed for terminals, not for language models. They are invisible control codes that tell a terminal to change colors, hide text," /><meta property="og:url" content="https://brightsec.com/research/detecting-ansi-escape-sequence-injection-in-mcp-servers-with-dast/" /><meta property="og:site_name" content="Bright Security" /><meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="Detecting ANSI Escape Sequence Injection in MCP Servers with DAST | Bright Security" /><meta name="twitter:description" content="ANSI escape sequences were designed for terminals, not for language models. They are invisible control codes that tell a terminal to change colors, hide text," /><link rel='dns-prefetch' href='//cdn.jsdelivr.net' /><link rel='dns-prefetch' href='//www.googletagmanager.com' /><link rel="alternate" type="application/rss+xml" title="Bright Security &raquo; Feed" href="https://brightsec.com/feed/" /><link rel="alternate" type="application/rss+xml" title="Bright Security &raquo; Comments Feed" href="https://brightsec.com/comments/feed/" /><link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://brightsec.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fbrightsec.com%2Fresearch%2Fdetecting-ansi-escape-sequence-injection-in-mcp-servers-with-dast%2F" /><link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://brightsec.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fbrightsec.com%2Fresearch%2Fdetecting-ansi-escape-sequence-injection-in-mcp-servers-with-dast%2F&#038;format=xml" /><style id="wp-img-auto-sizes-contain-inline-css">img:is([sizes=auto i],[sizes^="auto," i]){contain-intrinsic-size:3000px 1500px}
/*# sourceURL=wp-img-auto-sizes-contain-inline-css */</style><link data-optimized="2" rel="stylesheet" href="https://brightsec.com/wp-content/litespeed/css/3346fcb2a9711d3ee2871039fd1a2052.css?ver=ee4c4" /><style id="wp-block-library-inline-css">:root{--wp-block-synced-color:#7a00df;--wp-block-synced-color--rgb:122,0,223;--wp-bound-block-color:var(--wp-block-synced-color);--wp-editor-canvas-background:#ddd;--wp-admin-theme-color:#007cba;--wp-admin-theme-color--rgb:0,124,186;--wp-admin-theme-color-darker-10:#006ba1;--wp-admin-theme-color-darker-10--rgb:0,107,160.5;--wp-admin-theme-color-darker-20:#005a87;--wp-admin-theme-color-darker-20--rgb:0,90,135;--wp-admin-border-width-focus:2px}@media (min-resolution:192dpi){:root{--wp-admin-border-width-focus:1.5px}}.wp-element-button{cursor:pointer}:root .has-very-light-gray-background-color{background-color:#eee}:root .has-very-dark-gray-background-color{background-color:#313131}:root .has-very-light-gray-color{color:#eee}:root .has-very-dark-gray-color{color:#313131}:root .has-vivid-green-cyan-to-vivid-cyan-blue-gradient-background{background:linear-gradient(135deg,#00d084,#0693e3)}:root .has-purple-crush-gradient-background{background:linear-gradient(135deg,#34e2e4,#4721fb 50%,#ab1dfe)}:root .has-hazy-dawn-gradient-background{background:linear-gradient(135deg,#faaca8,#dad0ec)}:root .has-subdued-olive-gradient-background{background:linear-gradient(135deg,#fafae1,#67a671)}:root .has-atomic-cream-gradient-background{background:linear-gradient(135deg,#fdd79a,#004a59)}:root .has-nightshade-gradient-background{background:linear-gradient(135deg,#330968,#31cdcf)}:root .has-midnight-gradient-background{background:linear-gradient(135deg,#020381,#2874fc)}:root{--wp--preset--font-size--normal:16px;--wp--preset--font-size--huge:42px}.has-regular-font-size{font-size:1em}.has-larger-font-size{font-size:2.625em}.has-normal-font-size{font-size:var(--wp--preset--font-size--normal)}.has-huge-font-size{font-size:var(--wp--preset--font-size--huge)}:root .has-text-align-center{text-align:center}:root .has-text-align-left{text-align:left}:root .has-text-align-right{text-align:right}.has-fit-text{white-space:nowrap!important}#end-resizable-editor-section{display:none}.aligncenter{clear:both}.items-justified-left{justify-content:flex-start}.items-justified-center{justify-content:center}.items-justified-right{justify-content:flex-end}.items-justified-space-between{justify-content:space-between}.screen-reader-text{word-wrap:normal!important;border:0;clip-path:inset(50%);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}.screen-reader-text:focus{background-color:#ddd;clip-path:none;color:#444;display:block;font-size:1em;height:auto;left:5px;line-height:normal;padding:15px 23px 14px;text-decoration:none;top:5px;width:auto;z-index:100000}html :where(.has-border-color){border-style:solid}html :where([style*=border-color]){border-style:solid}html :where([style*=border-top-color]){border-top-style:solid}html :where([style*=border-right-color]){border-right-style:solid}html :where([style*=border-bottom-color]){border-bottom-style:solid}html :where([style*=border-left-color]){border-left-style:solid}html :where([style*=border-width]){border-style:solid}html :where([style*=border-top-width]){border-top-style:solid}html :where([style*=border-right-width]){border-right-style:solid}html :where([style*=border-bottom-width]){border-bottom-style:solid}html :where([style*=border-left-width]){border-left-style:solid}html :where(img[class*=wp-image-]){height:auto;max-width:100%}:where(figure){margin:0 0 1em}html :where(.is-position-sticky){--wp-admin--admin-bar--position-offset:var(--wp-admin--admin-bar--height,0px)}@media screen and (max-width:600px){html :where(.is-position-sticky){--wp-admin--admin-bar--position-offset:0px}}

/*# sourceURL=/wp-includes/css/dist/block-library/common.min.css */</style><style id="wp-block-heading-inline-css">h1:where(.wp-block-heading).has-background,h2:where(.wp-block-heading).has-background,h3:where(.wp-block-heading).has-background,h4:where(.wp-block-heading).has-background,h5:where(.wp-block-heading).has-background,h6:where(.wp-block-heading).has-background{padding:1.25em 2.375em}h1.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h1.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h2.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h2.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h3.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h3.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h4.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h4.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h5.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h5.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h6.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h6.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]){rotate:180deg}
/*# sourceURL=https://brightsec.com/wp-includes/blocks/heading/style.min.css */</style><style id="wp-block-list-inline-css">ol,ul{box-sizing:border-box}:root :where(.wp-block-list.has-background){padding:1.25em 2.375em}
/*# sourceURL=https://brightsec.com/wp-includes/blocks/list/style.min.css */</style><style id="wp-block-paragraph-inline-css">.is-small-text{font-size:.875em}.is-regular-text{font-size:1em}.is-large-text{font-size:2.25em}.is-larger-text{font-size:3em}.has-drop-cap:not(:focus):first-letter{float:left;font-size:8.4em;font-style:normal;font-weight:100;line-height:.68;margin:.05em .1em 0 0;text-transform:uppercase}body.rtl .has-drop-cap:not(:focus):first-letter{float:none;margin-left:.1em}p.has-drop-cap.has-background{overflow:hidden}:root :where(p.has-background){padding:1.25em 2.375em}:where(p.has-text-color:not(.has-link-color)) a{color:inherit}p.has-text-align-left[style*="writing-mode:vertical-lr"],p.has-text-align-right[style*="writing-mode:vertical-rl"]{rotate:180deg}
/*# sourceURL=https://brightsec.com/wp-includes/blocks/paragraph/style.min.css */</style><style id="classic-theme-styles-inline-css">/*! This file is auto-generated */
.wp-block-button__link{color:#fff;background-color:#32373c;border-radius:9999px;box-shadow:none;text-decoration:none;padding:calc(.667em + 2px) calc(1.333em + 2px);font-size:1.125em}.wp-block-file__button{background:#32373c;color:#fff;text-decoration:none}
/*# sourceURL=/wp-includes/css/classic-themes.min.css */</style><style id="global-styles-inline-css">:root{--wp--preset--aspect-ratio--square: 1;--wp--preset--aspect-ratio--4-3: 4/3;--wp--preset--aspect-ratio--3-4: 3/4;--wp--preset--aspect-ratio--3-2: 3/2;--wp--preset--aspect-ratio--2-3: 2/3;--wp--preset--aspect-ratio--16-9: 16/9;--wp--preset--aspect-ratio--9-16: 9/16;--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgb(6,147,227) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgb(252,185,0) 0%,rgb(255,105,0) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgb(255,105,0) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgb(255, 255, 255), 6px 6px rgb(0, 0, 0);--wp--preset--shadow--crisp: 6px 6px 0px rgb(0, 0, 0);}:where(body) { margin: 0; }:where(.is-layout-flex){gap: 0.5em;}:where(.is-layout-grid){gap: 0.5em;}body .is-layout-flex{display: flex;}.is-layout-flex{flex-wrap: wrap;align-items: center;}.is-layout-flex > :is(*, div){margin: 0;}body .is-layout-grid{display: grid;}.is-layout-grid > :is(*, div){margin: 0;}body{padding-top: 0px;padding-right: 0px;padding-bottom: 0px;padding-left: 0px;}:root :where(.wp-element-button, .wp-block-button__link){background-color: #32373c;border-width: 0;color: #fff;font-family: inherit;font-size: inherit;font-style: inherit;font-weight: inherit;letter-spacing: inherit;line-height: inherit;padding-top: calc(0.667em + 2px);padding-right: calc(1.333em + 2px);padding-bottom: calc(0.667em + 2px);padding-left: calc(1.333em + 2px);text-decoration: none;text-transform: inherit;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
/*# sourceURL=global-styles-inline-css */</style><style id="bs-multi-style-inline-css">/* ===== BrightSecure Multi Mega Menu CSS (bs- prefix) ===== */

		
		
		
		.bs-acc-panel a span::after{
			content: none !important;
		}
	  
	  .bs-business-grid a span::after{
			content: none !important;
		}
	  
	  li#menu-item-3371 a span::after{
		 content: none !important; 
  }
/* LANDSCAPE: ensure primary menu & mega menus fully visible (no clipping) */
@media (max-width: 900px) and (orientation: landscape) {

  /* allow header/menu container to expand and not clip */
  header.header,
  .header__menu,
  .header__container,
  #main-navigation-wrapper,
  nav {
    height: auto !important;
    max-height: none !important;
    overflow: visible !important;
  }

  /* make the main menu flexible: try wrapping to new rows first (so items stay visible) */
  #main-menu,
  #main-menu > ul,
  #main-menu > .menu {
    display: flex !important;
    flex-wrap: wrap !important;
    align-items: center !important;
    gap: 8px !important;
  }

  /* ensure each li doesn't collapse and keeps its content on one line */
  #main-menu > li,
  #main-menu li {
    flex: 0 0 auto !important;
    white-space: nowrap !important;
    min-width: 0 !important;
  }

  /* if wrapping still can't fit (very long), allow horizontal scroll on the menu row */
  /* wrap the actual menu row in a scrollable container — fallback */
  #main-navigation-wrapper {
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    scroll-behavior: smooth !important;
    white-space: nowrap !important;
  }
  /* make sure the UL doesn't force clipping */
  #main-navigation-wrapper ul {
    display: inline-flex !important;
    flex-wrap: nowrap !important;
  }

  /* MEGA MENU: full height and scrollable in landscape */
  .bs-mega-wrap {
    position: fixed !important;
    left: 0 !important;
    right: 0 !important;
    top: calc(var(--site-header-height, 50px)) !important; /* fallback to 50px if var not set */
    height: calc(100vh - calc(var(--site-header-height, 50px))) !important;
    max-height: calc(100vh - calc(var(--site-header-height, 50px))) !important;
    overflow-y: auto !important;
    -webkit-overflow-scrolling: touch !important;
    overflow-x: hidden !important;
    width: 100% !important;
    box-shadow: none !important;
    border-radius: 0 !important;
  }

  /* ensure inner containers don't clip */
  .bs-mega-wrap .menu-sec,
  .bs-mega-wrap .bs-cols,
  .bs-mega-wrap .bs-col,
  .bs-mega-wrap .bs-accordion,
  .bs-mega-wrap .bs-acc-panel,
  .bs-mega-wrap .bs-resources-grid,
  .bs-mega-wrap .bs-company-grid {
    max-height: none !important;
    height: auto !important;
    overflow: visible !important;
  }

  /* If header uses a fixed height via CSS variable, set it (you can tweak 50px) */
  :root { --site-header-height: 50px; }

  /* small safety: ensure body/html overflow won't hide fixed elements */
  html, body {
    height: 100% !important;
        overflow: visible !important;

  }
}		
		
.nav-primary>ul#main-menu li.menu-item a span::after {
    /* content: "\f0de"; */
    font-family: 'dashicons';
    content: "\f142";
    font-size: 15px;
    vertical-align: middle;
}	
.menu-sec ul li a span::after{
	content: none !important;
}			 
li#menu-item-3368:has(.bs-star-wrap[style*="display: block"]) > a span::after {
    font-family: 'dashicons';
    content: "\f140" !important;
}	
li#menu-item-3369:has(.bs-platform-wrap[style*="display: block"]) > a span::after {
    font-family: 'dashicons';
    content: "\f140" !important;
}	
li#menu-item-3370:has(.bs-resources-wrap[style*="display: block"]) > a span::after {
    font-family: 'dashicons';
    content: "\f140" !important;
}				 
li#menu-item-3372:has(.bs-company-wrap[style*="display: block"]) > a span::after {
    font-family: 'dashicons';
    content: "\f140" !important;
}				 
li#menu-item-3368:has(.bs-star-wrap[style*="display: block"]) > a span {
    color: #fff !important;
}		
.bs-mega-common { font-family: Inter, system-ui, sans-serif; }
header.header.header--loaded.header--sticky {
    background: #FCFCFD;
}
	  header.header.header--loaded{
		   background: #FCFCFD;  
	  }
div#main-navigation-wrapper ul#main-menu li span {
    color: #757785;
    font-size: 12px;
    font-weight: 500;
}
div#main-navigation-wrapper ul#main-menu li {
    margin-inline: 17px;
}

li#menu-item-3368:has(.bs-star-wrap[style*="display: block"]) > a span {
    color: #fff;
}			 
			 
.header__actions a.c-btn.c-btn-secondary.c-btn--variation-pink.c-btn--variation-default.c-btn--variation-arrow-right {
    background: #E784D5;
    border-radius: 12px;
}
.header__actions a.c-btn.c-btn-secondary.c-btn--variation-pink.c-btn--variation-default.c-btn--variation-arrow-right svg {
    display: none;
}			 
	.menu-item-star.active-star > a {
  background: linear-gradient(90.17deg, #DE6143 0.3%, #EC9EDD 69.08%);
  color: #fff !important;
  border-radius: 6px;
  padding: 6px 10px;
}	
/* Remove STAR highlight whenever ANY mega menu (except STAR) is open */
li#menu-item-3368:has(.bs-star-wrap[style*="display: block"]) > a {
background: linear-gradient(97.95deg, #DE6143 -0.24%, #EC9EDD 93.93%);
  color:#fff !important;
  border-radius:6px;
 padding: 5px 8px;	
}

/* BUT if ANY other mega menu is open → STAR highlight remove */
ul#main-menu:has(.bs-platform-wrap[style*="display: block"]) li#menu-item-3368 > a,
ul#main-menu:has(.bs-resources-wrap[style*="display: block"]) li#menu-item-3368 > a,
ul#main-menu:has(.bs-company-wrap[style*="display: block"]) li#menu-item-3368 > a {
  background: none !important;
  color: inherit !important;
}
/* general mega wrap */
.bs-mega-wrap {
  background:#F1F4F7;
  border:1px solid rgba(16,24,40,0.06);
  border-radius:10px;
  box-shadow:0 12px 36px rgba(16,24,40,0.10);
  padding:16px;
  display:none;
  position:absolute;
  left:0;
  top:100%;
  z-index:99999;
  transform-origin:top center;
  animation: bsFade .16s ease both;
  width: 100%;
}
	li#menu-item-3369:has(.bs-platform-wrap[style*="display: block"]) > a {
  border: 2px solid #E4CD64;
 border-radius:12px;
	padding: 5px 8px;						  
}	
	li#menu-item-3370:has(.bs-resources-wrap[style*="display: block"]) > a {
  border: 2px solid #E48973;
 border-radius:12px;
	padding: 5px 8px;						  
}								  
	li#menu-item-3372:has(.bs-company-wrap[style*="display: block"]) > a {
  border: 2px solid #E784D5;
 border-radius:12px;
	padding: 5px 8px;						  
}			
		li#menu-item-3377:has(.bs-business-wrap[style*="display: block"]) > a {
  border: 2px solid #E784D5;
 border-radius:12px;
	padding: 5px 8px;						  
}			
			
ul.bs-res-list li {
    margin-inline: 0px !important;
    padding-inline: 0px;
}							  
	
ul.bs-list li {
    margin-inline: 0px !important;
    padding-inline: 0px;
}							  
.bs-col a {
    display: flex;
    justify-content: space-between;
    align-items: center; /* Fix vertical alignment */
}
.chev-icon {
    font-size: 0 !important; /* Hide text arrow */
    display: flex; /* Ensure flex for centering */
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    color: #757785 !important;
    flex-shrink: 0; /* Prevent icon from shrinking */
}
.chev-icon::before {
    content: "\f345"; /* Right arrow dashicon */
    font-family: 'dashicons';
    font-size: 20px; /* Increased size */
    visibility: visible;
}	  
							  
@keyframes bsFade { from{opacity:0; transform:translateY(-8px)} to{opacity:1; transform:translateY(0)} }

/* ---------- STAR specific (slightly narrower) ---------- */
.bs-star-wrap { width:-webkit-fill-available; }
.bs-acc-row:nth-child(1) { border-top: 0px; padding-top: 0px; }
.bs-star-banner { background: linear-gradient(90.2deg, #DE6143 -9.19%, #EC9EDD 89.37%);
color: #fff; padding: 9px 10px; border-radius: 0px; display: flex; flex-flow: row; gap: 6px; margin-bottom: 14px; margin-top: 20px;     justify-content: space-between; align-items: center;}
.bs-acc-row { display:flex; justify-content:space-between; align-items:center; padding:14px 8px; border-top:1px solid #D1D2D6; cursor:pointer; }
.menu-sec h4 { margin:0; font-size:16px; font-weight:600; }
.menu-sec p { margin:4px 0 0 0; font-size:12px !important; color:#474A5D !important; }
.bs-chev { font-size:29px; transition:transform .18s ease; color:#474A5D; }
.bs-acc-panel { display:none; padding:12px 0;  width: 98.7%; margin: 0 auto;}
.bs-cols { display:flex; gap:20px; margin-bottom:10px; }
.bs-cols-grid { display:grid; grid-template-columns: repeat(2, 1fr) !important; gap:20px; margin-bottom: 10px; }
.bs-col { flex:1; }
.bs-col a { 
    display: flex !important; 
    flex-direction: row !important;
    justify-content: space-between !important; 
    align-items: center !important; 
    text-decoration: none; 
}
/* More specific selector for accordion items */
.bs-acc-panel .bs-col a {
    display: flex !important; 
    flex-direction: row !important;
    justify-content: space-between !important; 
    align-items: center !important; 
}
.bs-col a > div { flex: 1; min-width: 0; }
.bs-col h5 { margin:0 0 6px; font-size:12px; font-weight:600; color: #474A5D;}
.bs-col p { margin:0; font-size:10px !important; color:#474A5D;  font-weight:400;}
.menu-sec h4 { color: #2F3551; font-size: 16px; }
.menu-sec {width: 85%; margin: 0 auto; }
.bs-star-banner .title { font-size: 16px; font-weight: 600; justify-content: space-between;}
.bs-star-banner .desc { font-size: 13px; font-weight: 500; }

/* ---------- PLATFORM specific (wider 3-column) ---------- */
ul.bs-list li strong { margin: 0; font-size: 16px; font-weight: 600; color: #2F3551; }
.bs-platform-wrap { width:-webkit-fill-available; padding:20px; }
.bs-grid { display:flex; gap:28px; align-items:flex-start; }
.bs-col-wide { flex:1; min-width:0; }
.bs-col-wide h4 { margin:0 0 10px 0; font-size:15px; font-weight:700; border-bottom:2px solid rgba(209,111,255,0.06); padding-bottom:8px; }
.bs-list { margin:12px 0 0 0; padding:0; list-style:none; }
.bs-list li { padding:12px 6px; border-bottom:1px solid rgba(16,24,40,0.03); display:flex; justify-content:space-between; align-items:center; }
.bs-list li a { color:inherit; text-decoration:none; display:flex!important; gap:12px; align-items:center; width:100%; }
.bs-list li p { margin:0; font-size:13px; color:#6b7076; }
ul li .bs-item-chip { width:32px; height:32px; border-radius:50%; display:flex; align-items:center; justify-content:center; color: #757785;}
ul li .bs-item-chip::before {
    font-family: 'dashicons';
    content: "\f142";
    font-size: 15px;
    vertical-align: middle;
}

/* featured block */
.bs-featured { display:flex; gap:12px; align-items:flex-start; min-height:120px; flex-flow:column; }
.bs-featured .thumb { width:-webkit-fill-available; height:250px; background:#A3A5AE; border-radius:20px; flex:0 0 auto; }
.bs-featured .meta { flex:1; }
.bs-featured .meta h5 { margin:0 0 6px 0; font-size:14px; font-weight:700; color: #2F3551;}
.bs-featured .meta p { margin:0; font-size:12px; color:#474A5D; font-weight:400;}

/* ---------- RESOURCES specific (two-column left list + right featured) ---------- */
ul.bs-res-list li strong { margin: 0; font-size: 16px; font-weight: 600; color: #2F3551;}
ul.bs-res-list li p { margin:0; font-size:13px; color:#6b7076; }
.bs-resources-wrap { width:-webkit-fill-available; padding:18px; }
.bs-resources-grid { display:flex; gap:28px; align-items:flex-start; }
.bs-resources-left { flex:1.2; }
.bs-resources-right { flex:0.8; }

/* small tweaks for list in resources */
.bs-res-list { list-style:none; margin:6px 0 0 0; padding:0; }
.bs-res-list li { padding:12px 6px; border-bottom:1px solid rgba(16,24,40,0.03); display:flex; justify-content:space-between; align-items:center; }
.bs-res-list li a { text-decoration:none; color:inherit; display:flex!important; gap:12px; align-items:center; width:100%; justify-content: space-between; }
.bs-res-list li p { margin:0; font-size:13px; color:#6b7076; }

/* ---------- COMPANY specific (two-column simple lists) ---------- */
ul.bs-list li a { justify-content: space-between;}
.bs-company-wrap { width:-webkit-fill-available; padding:18px; }
.bs-company-grid { display:flex; gap:28px; align-items:flex-start; }
.bs-company-grid .bs-col { flex:1; }
.bs-company-grid h4 { margin:0 0 10px 0; font-size:15px; font-weight:700; border-bottom:2px solid rgba(209,111,255,0.06); padding-bottom:8px; }

/* responsive common */
@media (max-width:1000px) {
  .bs-mega-wrap { position:fixed; left:12px; right:12px; top:70px; width:auto; }
  .bs-grid, .bs-cols, .bs-resources-grid, .bs-company-grid { flex-direction:column; }
  .bs-cols-grid { grid-template-columns: 1fr; }
  .bs-featured .thumb { width:100%; height:140px; }
}

/* attach helpers */
nav .menu-item-star, nav .menu-item-platform, nav .menu-item-resources, nav .menu-item-company, nav .menu-item-business-impact { position:static !important; }
nav li.bs-mega-parent { position:static !important; }
nav .menu-item-star .bs-star-wrap, nav .menu-item-platform .bs-platform-wrap, nav .menu-item-resources .bs-resources-wrap, nav .menu-item-company .bs-company-wrap, nav .menu-item-business-impact .bs-business-wrap { left:0; top:100%; }

	/* ================= MOBILE-SPECIFIC: make header like Figma ================= */
@media (max-width: 768px) {
.nav-primary>ul#main-menu li.menu-item a span::after{
content: "\f139" ;
}
	.menu-sec ul li a span::after{
	content: none !important;
		display:none !important;
}		
	span.chev-icon::after{
	content: none !important;
		display:none !important;
}					   
	div#main-navigation-wrapper ul#main-menu li span {
    color: #757785;
    font-size: 12px;
    font-weight: 500;
    display: flex;
    justify-content: space-between !important;
}			   
  /* header background white */
  header.header.header--loaded,
  header.header.header--loaded.header--sticky,
  .header__container,
  .header__menu {
    background: #ffffff !important;
  }
  /* Book demo = pink, big pill button centered at bottom of menu */
  .header__actions a.c-btn.c-btn-secondary.c-btn--variation-pink.c-btn--variation-default.c-btn--variation-arrow-right,
  .bs-cta,
  .bs-mega-wrap .book-demo-btn {
    background: linear-gradient(90deg,#F2A6D9,#E884D5) !important;
    color: #ffffff !important;
    border-radius: 12px !important;
    padding: 10px 18px !important;
    text-align: center !important;
    display: inline-block;
    font-weight:700;
  }

  /* Mega overlay full visible and fixed */
  .bs-mega-wrap {
position: fixed !important;
        left: 0px !important;
        right: 0px !important;
        top: 5px !important;
        margin: 0 auto !important;
        width: -webkit-fill-available !important;
        z-index: 2147483647 !important;
        max-height: 100% !important;
        overflow-y: auto !important;
        -webkit-overflow-scrolling: touch !important;
        display: none;
        background: #ffffff !important;
        color: #2f3243 !important;
        border-radius: 0px !important;
        padding: 0 !important;
        box-shadow: unset !important;
        border: 0px !important;
	  max-height: 100vh !important;
  }
.bs-mega-wrap.bs-platform-wrap {
        max-height: 500px !important;
        height: 500px !important;
}
								
	.bs-mega-wrap.bs-resources-wrap {
    max-height: 190vh !important;
    height: 85vh;
}		
.bs-mega-wrap.bs-star-wrap {
    max-height: 190vh !important;
    height: 85vh;
}								
								
  /* container inside overlay to match figma paddings */
  .bs-mega-wrap .menu-sec {
    padding: 12px 7px 20px !important;
	  width: 100% !important;
  }
  /* 2) Internal sections must not clip content */
  .bs-mega-wrap .menu-sec,
  .bs-mega-wrap .bs-cols,
  .bs-mega-wrap .bs-col,
  .bs-mega-wrap .bs-accordion,
  .bs-mega-wrap .bs-acc-panel,
  .bs-mega-wrap .bs-resources-grid,
  .bs-mega-wrap .bs-company-grid,
  .bs-mega-wrap .bs-col-wide {
    max-height: none !important;
    height: auto !important;
    overflow: visible !important;
  }

  /* 3) Theme's mobile menu container is LIMITING height — remove that */
  .header__menu.header__menu--has-transition {
    height: auto !important;
    min-height: auto !important;
    max-height: none !important;
    overflow: visible !important;
  }
  /* Top gradient bar for STAR item like Figma */
  .bs-mega-wrap .bs-star-top {
    background: linear-gradient(90deg,#DE6143 0%, #EC9EDD 100%);
    color: #ffffff;
    padding: 10px 16px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    font-weight:700;
  }
  .bs-mega-wrap .bs-star-top .label { font-size:15px; }
  .bs-mega-wrap .bs-star-top .chev { font-size:14px; opacity:0.95; }

  /* Menu items list style (no p text, separators) */
  .bs-mega-wrap ul,
  .bs-mega-wrap .bs-list,
  .bs-mega-wrap .bs-res-list {
    list-style:none;
    margin: 0;
    padding: 0;
  }
  .bs-mega-wrap li {
    padding: 16px 16px;
    border-bottom: 1px solid rgba(47,51,67,0.06);
    display:flex;
    justify-content:space-between;
    align-items:center;
  }

  /* remove all descriptions on mobile */
  .bs-mega-wrap p,
  .bs-mega-wrap .desc,
  .bs-mega-wrap .meta p,
  .bs-mega-wrap .bs-col p,
  .bs-mega-wrap .menu-sec p {
    display: none !important;
  }

  /* STAR menu link in nav: no background and align label to right */
  li#menu-item-3368 > a {
    background: none !important;
    box-shadow: none !important;
    border: 0 !important;
     justify-content: space-between !important; 
    align-items: center;
    color: inherit !important;
    width: 100%;
  }
  li#menu-item-3368 > a span { margin-left: 0 !important; }

  /* small chevron on right of each menu item */
  .bs-mega-wrap li .bs-item-chip,
  .bs-mega-wrap li .chev-icon {
    width: 22px;
    height: 22px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    background: transparent;
    color: #D1A3D6;
    font-weight:700;
  }

  /* Book demo button wrapper at bottom of overlay */
  .bs-mega-wrap .menu-footer {
    padding: 16px;
    display:flex;
    justify-content:center;
  }
  .bs-mega-wrap .menu-footer .book-demo-btn {
    width: 85%;
    text-align:center;
  }

  /* Back link / small header row (like your figma) */
  .bs-mega-wrap .mobile-header {
    display:flex;
    align-items:center;
    gap:12px;
    padding: 12px 16px;
  }
  .bs-mega-wrap .mobile-header .back {
    font-size:14px;
    color:#8b8fa0;
    cursor:pointer;
  }
  .bs-mega-wrap .mobile-header .title {
    flex:1;
    text-align:left;
    font-weight:700;
    color:#2f3243;
  }

  /* ensure internal panels are full-width stacked */
  .bs-grid, .bs-cols, .bs-resources-grid, .bs-company-grid { flex-direction:column; }

  /* featured thumb reduced */
  .bs-featured .thumb { height:120px; border-radius:8px; }
// li#menu-item-3368:has(.bs-star-wrap[style*="display: block"]) > a {
//     text-align: right !important;
//     justify-content: flex-end !important;
// }
.header__menu {
    padding: 10px 2px !important;
}	
h4.overview {
    display: none;
}
								
li#menu-item-3369:has(.bs-platform-wrap[style*="display: block"]) > a {
    border: 0px !important;
    border-radius:  0px !important;
    padding: 5px 8px;
	    text-align: right !important;
    justify-content: flex-end !important;							
}								
// .bs-mega-wrap.bs-platform-wrap{
// 	        top: 11px !important;
// }		

			
.bs-col-wide {
    width: 100% !important;
}								
.bs-resources-left {
    width: 100% !important;
}								
.bs-company-grid .bs-col {
    width: 100% !important;
}								
.bs-mega-wrap.bs-star-wrap .bs-mobile-top {
    border-bottom: 2px solid;
    border-image-source: linear-gradient(90.17deg, #DE6143 0.3%, #EC9EDD 69.08%);
    border-image-slice: 1;
    line-height: 30px;
}						
										 
.bs-mega-wrap.bs-platform-wrap .bs-mobile-top {
    border-bottom: 2px solid #E4CD64;
    line-height: 30px;
}											 
.bs-mega-wrap.bs-resources-wrap .bs-mobile-top {
    border-bottom: 2px solid #E48973;
    line-height: 30px;
}		
.bs-mega-wrap.bs-company-wrap .bs-mobile-top {
    border-bottom: 0px;
    line-height: 30px;
}												 
.bs-mega-wrap.bs-resources-wrap a.book-demo-btn{
	background: #E48973 !important;
}		
		.bs-mega-wrap.bs-platform-wrap	a.book-demo-btn{
	background: #E4CD64 !important;
}									 
										 
  .bs-mega-wrap .menu-footer { 
    display:flex;
    justify-content:center;
    padding: 14px 16px;
    border-top: 1px solid rgba(47,51,67,0.04);
    background: transparent;
  }
	    .bs-mega-wrap.bs-resources-wrap {
        max-height: 500px !important;
        height: 500px !important;
    }									 
  .bs-mega-wrap .menu-footer .book-demo-btn {
    width: 92%;
    max-width: 420px;
    display: inline-block;
    text-align: center;
    padding: 12px 16px;
    border-radius: 22px;
    background: linear-gradient(90deg,#F2A6D9 6%, #E884D5 94%) !important;
    color: #ffffff !important;
    font-weight: 700;
    text-decoration: none;
    box-shadow: 0 6px 18px rgba(232,132,213,0.12);
  }								
					
}		
										  @media (min-width: 769px) {
			  .bs-mobile-top {
    display: none !important;
}
    .bs-mega-wrap .menu-footer { display: none !important; }

  }	
								
								
							
/*# sourceURL=bs-multi-style-inline-css */</style><style id="main-css-fixed-inline-css">.modal{--bs-modal-zindex:1055;--bs-modal-width:500px;--bs-modal-padding:1rem;--bs-modal-margin:.5rem;--bs-modal-color:;--bs-modal-bg:var(--bs-body-bg);--bs-modal-border-color:var(--bs-border-color-translucent);--bs-modal-border-width:var(--bs-border-width);--bs-modal-border-radius:var(--bs-border-radius-lg);--bs-modal-box-shadow:var(--bs-box-shadow-sm);--bs-modal-inner-border-radius:calc(var(--bs-border-radius-lg) - (var(--bs-border-width)));--bs-modal-header-padding-x:1rem;--bs-modal-header-padding-y:1rem;--bs-modal-header-padding:1rem 1rem;--bs-modal-header-border-color:var(--bs-border-color);--bs-modal-header-border-width:var(--bs-border-width);--bs-modal-title-line-height:1.5;--bs-modal-footer-gap:.5rem;--bs-modal-footer-bg:;--bs-modal-footer-border-color:var(--bs-border-color);--bs-modal-footer-border-width:var(--bs-border-width);z-index:var(--bs-modal-zindex);outline:0;width:100%;height:100%;display:none;position:fixed;top:0;left:0;overflow:hidden auto}.modal-dialog{width:auto;margin:var(--bs-modal-margin);pointer-events:none;position:relative}.modal.fade .modal-dialog{transition:transform .3s ease-out;transform:translateY(-50px)}@media (prefers-reduced-motion:reduce){.modal.fade .modal-dialog{transition:none}}.modal.show .modal-dialog{transform:none}.modal.modal-static .modal-dialog{transform:scale(1.02)}.modal-dialog-scrollable{height:calc(100% - var(--bs-modal-margin)*2)}.modal-dialog-scrollable .modal-content{max-height:100%;overflow:hidden}.modal-dialog-scrollable .modal-body{overflow-y:auto}.modal-dialog-centered{min-height:calc(100% - var(--bs-modal-margin)*2);align-items:center;display:flex}.modal-content{width:100%;color:var(--bs-modal-color);pointer-events:auto;background-color:var(--bs-modal-bg);border:var(--bs-modal-border-width)solid var(--bs-modal-border-color);border-radius:var(--bs-modal-border-radius);background-clip:padding-box;outline:0;flex-direction:column;display:flex;position:relative}.modal-backdrop{--bs-backdrop-zindex:1050;--bs-backdrop-bg:#000;--bs-backdrop-opacity:.5;z-index:var(--bs-backdrop-zindex);background-color:var(--bs-backdrop-bg);width:100vw;height:100vh;position:fixed;top:0;left:0}.modal-backdrop.fade{opacity:0}.modal-backdrop.show{opacity:var(--bs-backdrop-opacity)}.modal-header{padding:var(--bs-modal-header-padding);border-bottom:var(--bs-modal-header-border-width)solid var(--bs-modal-header-border-color);border-top-left-radius:var(--bs-modal-inner-border-radius);border-top-right-radius:var(--bs-modal-inner-border-radius);flex-shrink:0;align-items:center;display:flex}.modal-header .btn-close{padding:calc(var(--bs-modal-header-padding-y)*.5)calc(var(--bs-modal-header-padding-x)*.5);margin:calc(-.5*var(--bs-modal-header-padding-y))calc(-.5*var(--bs-modal-header-padding-x))calc(-.5*var(--bs-modal-header-padding-y))auto}.modal-title{line-height:var(--bs-modal-title-line-height);margin-bottom:0}.modal-body{padding:var(--bs-modal-padding);flex:auto;position:relative}.modal-footer{padding:calc(var(--bs-modal-padding) - var(--bs-modal-footer-gap)*.5);background-color:var(--bs-modal-footer-bg);border-top:var(--bs-modal-footer-border-width)solid var(--bs-modal-footer-border-color);border-bottom-right-radius:var(--bs-modal-inner-border-radius);border-bottom-left-radius:var(--bs-modal-inner-border-radius);flex-wrap:wrap;flex-shrink:0;justify-content:flex-end;align-items:center;display:flex}.modal-footer>*{margin:calc(var(--bs-modal-footer-gap)*.5)}@media (width>=576px){.modal{--bs-modal-margin:1.75rem;--bs-modal-box-shadow:var(--bs-box-shadow)}.modal-dialog{max-width:var(--bs-modal-width);margin-left:auto;margin-right:auto}.modal-sm{--bs-modal-width:300px}}@media (width>=992px){.modal-lg,.modal-xl{--bs-modal-width:800px}}@media (width>=1200px){.modal-xl{--bs-modal-width:1140px}}.modal-fullscreen{width:100vw;max-width:none;height:100%;margin:0}.modal-fullscreen .modal-content{border:0;border-radius:0;height:100%}.modal-fullscreen .modal-header,.modal-fullscreen .modal-footer{border-radius:0}.modal-fullscreen .modal-body{overflow-y:auto}@media (width<=575.98px){.modal-fullscreen-sm-down{width:100vw;max-width:none;height:100%;margin:0}.modal-fullscreen-sm-down .modal-content{border:0;border-radius:0;height:100%}.modal-fullscreen-sm-down .modal-header,.modal-fullscreen-sm-down .modal-footer{border-radius:0}.modal-fullscreen-sm-down .modal-body{overflow-y:auto}}@media (width<=767.98px){.modal-fullscreen-md-down{width:100vw;max-width:none;height:100%;margin:0}.modal-fullscreen-md-down .modal-content{border:0;border-radius:0;height:100%}.modal-fullscreen-md-down .modal-header,.modal-fullscreen-md-down .modal-footer{border-radius:0}.modal-fullscreen-md-down .modal-body{overflow-y:auto}}@media (width<=991.98px){.modal-fullscreen-lg-down{width:100vw;max-width:none;height:100%;margin:0}.modal-fullscreen-lg-down .modal-content{border:0;border-radius:0;height:100%}.modal-fullscreen-lg-down .modal-header,.modal-fullscreen-lg-down .modal-footer{border-radius:0}.modal-fullscreen-lg-down .modal-body{overflow-y:auto}}@media (width<=1199.98px){.modal-fullscreen-xl-down{width:100vw;max-width:none;height:100%;margin:0}.modal-fullscreen-xl-down .modal-content{border:0;border-radius:0;height:100%}.modal-fullscreen-xl-down .modal-header,.modal-fullscreen-xl-down .modal-footer{border-radius:0}.modal-fullscreen-xl-down .modal-body{overflow-y:auto}}@media (width<=1399.98px){.modal-fullscreen-xxl-down{width:100vw;max-width:none;height:100%;margin:0}.modal-fullscreen-xxl-down .modal-content{border:0;border-radius:0;height:100%}.modal-fullscreen-xxl-down .modal-header,.modal-fullscreen-xxl-down .modal-footer{border-radius:0}.modal-fullscreen-xxl-down .modal-body{overflow-y:auto}}.fade{transition:opacity .15s linear}@media (prefers-reduced-motion:reduce){.fade{transition:none}}.fade:not(.show){opacity:0}.collapse:not(.show){display:none}.collapsing{height:0;transition:height .35s;overflow:hidden}@media (prefers-reduced-motion:reduce){.collapsing{transition:none}}.collapsing.collapse-horizontal{width:0;height:auto;transition:width .35s}@media (prefers-reduced-motion:reduce){.collapsing.collapse-horizontal{transition:none}}@font-face{ font-display:swap;font-family:swiper-icons;src:url("data:application/font-woff;charset=utf-8;base64, d09GRgABAAAAAAZgABAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABGRlRNAAAGRAAAABoAAAAci6qHkUdERUYAAAWgAAAAIwAAACQAYABXR1BPUwAABhQAAAAuAAAANuAY7+xHU1VCAAAFxAAAAFAAAABm2fPczU9TLzIAAAHcAAAASgAAAGBP9V5RY21hcAAAAkQAAACIAAABYt6F0cBjdnQgAAACzAAAAAQAAAAEABEBRGdhc3AAAAWYAAAACAAAAAj//wADZ2x5ZgAAAywAAADMAAAD2MHtryVoZWFkAAABbAAAADAAAAA2E2+eoWhoZWEAAAGcAAAAHwAAACQC9gDzaG10eAAAAigAAAAZAAAArgJkABFsb2NhAAAC0AAAAFoAAABaFQAUGG1heHAAAAG8AAAAHwAAACAAcABAbmFtZQAAA/gAAAE5AAACXvFdBwlwb3N0AAAFNAAAAGIAAACE5s74hXjaY2BkYGAAYpf5Hu/j+W2+MnAzMYDAzaX6QjD6/4//Bxj5GA8AuRwMYGkAPywL13jaY2BkYGA88P8Agx4j+/8fQDYfA1AEBWgDAIB2BOoAeNpjYGRgYNBh4GdgYgABEMnIABJzYNADCQAACWgAsQB42mNgYfzCOIGBlYGB0YcxjYGBwR1Kf2WQZGhhYGBiYGVmgAFGBiQQkOaawtDAoMBQxXjg/wEGPcYDDA4wNUA2CCgwsAAAO4EL6gAAeNpj2M0gyAACqxgGNWBkZ2D4/wMA+xkDdgAAAHjaY2BgYGaAYBkGRgYQiAHyGMF8FgYHIM3DwMHABGQrMOgyWDLEM1T9/w8UBfEMgLzE////P/5//f/V/xv+r4eaAAeMbAxwIUYmIMHEgKYAYjUcsDAwsLKxc3BycfPw8jEQA/gZBASFhEVExcQlJKWkZWTl5BUUlZRVVNXUNTQZBgMAAMR+E+gAEQFEAAAAKgAqACoANAA+AEgAUgBcAGYAcAB6AIQAjgCYAKIArAC2AMAAygDUAN4A6ADyAPwBBgEQARoBJAEuATgBQgFMAVYBYAFqAXQBfgGIAZIBnAGmAbIBzgHsAAB42u2NMQ6CUAyGW568x9AneYYgm4MJbhKFaExIOAVX8ApewSt4Bic4AfeAid3VOBixDxfPYEza5O+Xfi04YADggiUIULCuEJK8VhO4bSvpdnktHI5QCYtdi2sl8ZnXaHlqUrNKzdKcT8cjlq+rwZSvIVczNiezsfnP/uznmfPFBNODM2K7MTQ45YEAZqGP81AmGGcF3iPqOop0r1SPTaTbVkfUe4HXj97wYE+yNwWYxwWu4v1ugWHgo3S1XdZEVqWM7ET0cfnLGxWfkgR42o2PvWrDMBSFj/IHLaF0zKjRgdiVMwScNRAoWUoH78Y2icB/yIY09An6AH2Bdu/UB+yxopYshQiEvnvu0dURgDt8QeC8PDw7Fpji3fEA4z/PEJ6YOB5hKh4dj3EvXhxPqH/SKUY3rJ7srZ4FZnh1PMAtPhwP6fl2PMJMPDgeQ4rY8YT6Gzao0eAEA409DuggmTnFnOcSCiEiLMgxCiTI6Cq5DZUd3Qmp10vO0LaLTd2cjN4fOumlc7lUYbSQcZFkutRG7g6JKZKy0RmdLY680CDnEJ+UMkpFFe1RN7nxdVpXrC4aTtnaurOnYercZg2YVmLN/d/gczfEimrE/fs/bOuq29Zmn8tloORaXgZgGa78yO9/cnXm2BpaGvq25Dv9S4E9+5SIc9PqupJKhYFSSl47+Qcr1mYNAAAAeNptw0cKwkAAAMDZJA8Q7OUJvkLsPfZ6zFVERPy8qHh2YER+3i/BP83vIBLLySsoKimrqKqpa2hp6+jq6RsYGhmbmJqZSy0sraxtbO3sHRydnEMU4uR6yx7JJXveP7WrDycAAAAAAAH//wACeNpjYGRgYOABYhkgZgJCZgZNBkYGLQZtIJsFLMYAAAw3ALgAeNolizEKgDAQBCchRbC2sFER0YD6qVQiBCv/H9ezGI6Z5XBAw8CBK/m5iQQVauVbXLnOrMZv2oLdKFa8Pjuru2hJzGabmOSLzNMzvutpB3N42mNgZGBg4GKQYzBhYMxJLMlj4GBgAYow/P/PAJJhLM6sSoWKfWCAAwDAjgbRAAB42mNgYGBkAIIbCZo5IPrmUn0hGA0AO8EFTQAA")format("woff");font-weight:400;font-style:normal }:root{--swiper-theme-color:#007aff}:host{z-index:1;margin-left:auto;margin-right:auto;display:block;position:relative}.swiper{z-index:1;margin-left:auto;margin-righ