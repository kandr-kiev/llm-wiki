---
source_url: https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-rc/
ingested: 2026-07-17
sha256: d574639ead4e4e6df44abfe84e7df2cb0c99ac7007e1adabcefca08cce831493
blog_source: TypeScript Blog
---
<!DOCTYPE html>
<html lang="en-US" theme="light">

<head>
	<meta charset="UTF-8">
	<script>
		// Initialize theme from localStorage or system preference
		let theme = localStorage.getItem('theme') || (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
		document.documentElement.setAttribute('theme', theme);
		const metaTag = document.createElement('meta');
		metaTag.setAttribute('name', 'awa-ver');
		metaTag.content = theme;
		document.head.appendChild(metaTag);
		isDarkTheme = theme === 'dark';
	</script>
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
			<meta name="awa-pageType" content="post" />
				<meta name="awa-product" content="TypeScript" />
				<meta name="awa-asst" content="https://devblogs.microsoft.com/typescript/?p=4962" />
			
			<meta name="awa-xtopic" content="TypeScript">	
		
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<title>Announcing TypeScript 5.9 RC - TypeScript</title>
	<meta name="mobile-web-app-capable" content="yes">
	<meta name="color-scheme" content="dark light">
	<meta name="apple-mobile-web-app-capable" content="yes">
	<meta name="apple-mobile-web-app-title" content="TypeScript - The official blog of the TypeScript team.">
	<link rel="profile" href="http://gmpg.org/xfn/11">
	<link rel="pingback" href="https://devblogs.microsoft.com/typescript/xmlrpc.php">
		<!-- [Begin] JSLL SHIM (1DS) domain prefetch  -->
	<link rel="preconnect" href="//js.monitor.azure.com" crossorigin>
	<link rel="preconnect" href="//browser.events.data.microsoft.com" crossorigin>
	<!-- [END] JSLL SHIM (1DS) domain prefetch  -->
	<meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />

	<!-- This site is optimized with the Yoast SEO Premium plugin v28.0 (Yoast SEO v28.0) - https://yoast.com/product/yoast-seo-premium-wordpress/ -->
	<meta name="description" content="Today we are excited to announce the Release Candidate (RC) of TypeScript 5.9! To get started using the Release Candidate, you can get it through npm with" />
	<link rel="canonical" href="https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-rc/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="Announcing TypeScript 5.9 RC - TypeScript" />
	<meta property="og:description" content="Today we are excited to announce the Release Candidate (RC) of TypeScript 5.9! To get started using the Release Candidate, you can get it through npm with" />
	<meta property="og:url" content="https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-rc/" />
	<meta property="og:site_name" content="TypeScript" />
	<meta property="article:published_time" content="2025-07-25T16:53:10+00:00" />
	<meta property="og:image" content="https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2025/06/bare-hover-5.8-01.png" />
	<meta name="author" content="Daniel Rosenwasser" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:creator" content="@https://twitter.com/drosenwasser" />
	<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https:\/\/schema.org","@graph":[{"@type":"Article","@id":"https:\/\/devblogs.microsoft.com\/typescript\/announcing-typescript-5-9-rc\/#article","isPartOf":{"@id":"https:\/\/devblogs.microsoft.com\/typescript\/announcing-typescript-5-9-rc\/"},"author":{"name":"Daniel Rosenwasser","@id":"https:\/\/devblogs.microsoft.com\/typescript\/#\/schema\/person\/12dfa7bf0f253acafcf55d6ecf078888"},"headline":"Announcing TypeScript 5.9 RC","datePublished":"2025-07-25T16:53:10+00:00","mainEntityOfPage":{"@id":"https:\/\/devblogs.microsoft.com\/typescript\/announcing-typescript-5-9-rc\/"},"wordCount":1553,"image":{"@id":"https:\/\/devblogs.microsoft.com\/typescript\/announcing-typescript-5-9-rc\/#primaryimage"},"thumbnailUrl":"https:\/\/devblogs.microsoft.com\/typescript\/wp-content\/uploads\/sites\/11\/2018\/08\/typescriptfeature.png","articleSection":["TypeScript"],"inLanguage":"en-US"},{"@type":"WebPage","@id":"https:\/\/devblogs.microsoft.com\/typescript\/announcing-typescript-5-9-rc\/","url":"https:\/\/devblogs.microsoft.com\/typescript\/announcing-typescript-5-9-rc\/","name":"Announcing TypeScript 5.9 RC - TypeScript","isPartOf":{"@id":"https:\/\/devblogs.microsoft.com\/typescript\/#website"},"primaryImageOfPage":{"@id":"https:\/\/devblogs.microsoft.com\/typescript\/announcing-typescript-5-9-rc\/#primaryimage"},"image":{"@id":"https:\/\/devblogs.microsoft.com\/typescript\/announcing-typescript-5-9-rc\/#primaryimage"},"thumbnailUrl":"https:\/\/devblogs.microsoft.com\/typescript\/wp-content\/uploads\/sites\/11\/2018\/08\/typescriptfeature.png","datePublished":"2025-07-25T16:53:10+00:00","author":{"@id":"https:\/\/devblogs.microsoft.com\/typescript\/#\/schema\/person\/12dfa7bf0f253acafcf55d6ecf078888"},"description":"Today we are excited to announce the Release Candidate (RC) of TypeScript 5.9! To get started using the Release Candidate, you can get it through npm with","inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https:\/\/devblogs.microsoft.com\/typescript\/announcing-typescript-5-9-rc\/"]}]},{"@type":"ImageObject","inLanguage":"en-US","@id":"https:\/\/devblogs.microsoft.com\/typescript\/announcing-typescript-5-9-rc\/#primaryimage","url":"https:\/\/devblogs.microsoft.com\/typescript\/wp-content\/uploads\/sites\/11\/2018\/08\/typescriptfeature.png","contentUrl":"https:\/\/devblogs.microsoft.com\/typescript\/wp-content\/uploads\/sites\/11\/2018\/08\/typescriptfeature.png","width":562,"height":350},{"@type":"WebSite","@id":"https:\/\/devblogs.microsoft.com\/typescript\/#website","url":"https:\/\/devblogs.microsoft.com\/typescript\/","name":"TypeScript","description":"The official blog of the TypeScript team.","potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https:\/\/devblogs.microsoft.com\/typescript\/?s={search_term_string}"},"query-input":{"@type":"PropertyValueSpecification","valueRequired":true,"valueName":"search_term_string"}}],"inLanguage":"en-US"},{"@type":"Person","@id":"https:\/\/devblogs.microsoft.com\/typescript\/#\/schema\/person\/12dfa7bf0f253acafcf55d6ecf078888","name":"Daniel Rosenwasser","image":{"@type":"ImageObject","inLanguage":"en-US","@id":"https:\/\/devblogs.microsoft.com\/typescript\/wp-content\/uploads\/sites\/11\/2021\/08\/Daniel-Rosenwasser-635x817-1-96x96.png","url":"https:\/\/devblogs.microsoft.com\/typescript\/wp-content\/uploads\/sites\/11\/2021\/08\/Daniel-Rosenwasser-635x817-1-96x96.png","contentUrl":"https:\/\/devblogs.microsoft.com\/typescript\/wp-content\/uploads\/sites\/11\/2021\/08\/Daniel-Rosenwasser-635x817-1-96x96.png","caption":"Daniel Rosenwasser"},"description":"Daniel Rosenwasser is the product manager of the TypeScript team. He has a passion for programming languages, compilers, and great developer tooling.","sameAs":["https:\/\/github.com\/DanielRosenwasser","https:\/\/x.com\/https:\/\/twitter.com\/drosenwasser"],"url":"https:\/\/devblogs.microsoft.com\/typescript\/author\/danielrosenwasser\/"}]}</script>
	<!-- / Yoast SEO Premium plugin. -->


<link rel="alternate" type="application/rss+xml" title="TypeScript &raquo; Announcing TypeScript 5.9 RC Comments Feed" href="https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-rc/feed/" />
<link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://devblogs.microsoft.com/typescript/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-5-9-rc%2F" />
<link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://devblogs.microsoft.com/typescript/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-5-9-rc%2F&#038;format=xml" />
<style id="wp-img-auto-sizes-contain-inline-css">
img:is([sizes=auto i],[sizes^="auto," i]){contain-intrinsic-size:3000px 1500px}
/*# sourceURL=wp-img-auto-sizes-contain-inline-css */
</style>
<style id="wp-emoji-styles-inline-css">

	img.wp-smiley, img.emoji {
		display: inline !important;
		border: none !important;
		box-shadow: none !important;
		height: 1em !important;
		width: 1em !important;
		margin: 0 0.07em !important;
		vertical-align: -0.1em !important;
		background: none !important;
		padding: 0 !important;
	}
/*# sourceURL=wp-emoji-styles-inline-css */
</style>
<style id="wp-block-library-inline-css">
:root{--wp-block-synced-color:#7a00df;--wp-block-synced-color--rgb:122,0,223;--wp-bound-block-color:var(--wp-block-synced-color);--wp-editor-canvas-background:#ddd;--wp-admin-theme-color:#007cba;--wp-admin-theme-color--rgb:0,124,186;--wp-admin-theme-color-darker-10:#006ba1;--wp-admin-theme-color-darker-10--rgb:0,107,160.5;--wp-admin-theme-color-darker-20:#005a87;--wp-admin-theme-color-darker-20--rgb:0,90,135;--wp-admin-border-width-focus:2px}@media (min-resolution:192dpi){:root{--wp-admin-border-width-focus:1.5px}}.wp-element-button{cursor:pointer}:root .has-very-light-gray-background-color{background-color:#eee}:root .has-very-dark-gray-background-color{background-color:#313131}:root .has-very-light-gray-color{color:#eee}:root .has-very-dark-gray-color{color:#313131}:root .has-vivid-green-cyan-to-vivid-cyan-blue-gradient-background{background:linear-gradient(135deg,#00d084,#0693e3)}:root .has-purple-crush-gradient-background{background:linear-gradient(135deg,#34e2e4,#4721fb 50%,#ab1dfe)}:root .has-hazy-dawn-gradient-background{background:linear-gradient(135deg,#faaca8,#dad0ec)}:root .has-subdued-olive-gradient-background{background:linear-gradient(135deg,#fafae1,#67a671)}:root .has-atomic-cream-gradient-background{background:linear-gradient(135deg,#fdd79a,#004a59)}:root .has-nightshade-gradient-background{background:linear-gradient(135deg,#330968,#31cdcf)}:root .has-midnight-gradient-background{background:linear-gradient(135deg,#020381,#2874fc)}:root{--wp--preset--font-size--normal:16px;--wp--preset--font-size--huge:42px}.has-regular-font-size{font-size:1em}.has-larger-font-size{font-size:2.625em}.has-normal-font-size{font-size:var(--wp--preset--font-size--normal)}.has-huge-font-size{font-size:var(--wp--preset--font-size--huge)}:root .has-text-align-center{text-align:center}:root .has-text-align-left{text-align:left}:root .has-text-align-right{text-align:right}.has-fit-text{white-space:nowrap!important}#end-resizable-editor-section{display:none}.aligncenter{clear:both}.items-justified-left{justify-content:flex-start}.items-justified-center{justify-content:center}.items-justified-right{justify-content:flex-end}.items-justified-space-between{justify-content:space-between}.screen-reader-text{word-wrap:normal!important;border:0;clip-path:inset(50%);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}.screen-reader-text:focus{background-color:#ddd;clip-path:none;color:#444;display:block;font-size:1em;height:auto;left:5px;line-height:normal;padding:15px 23px 14px;text-decoration:none;top:5px;width:auto;z-index:100000}html :where(.has-border-color){border-style:solid}html :where([style*=border-color]){border-style:solid}html :where([style*=border-top-color]){border-top-style:solid}html :where([style*=border-right-color]){border-right-style:solid}html :where([style*=border-bottom-color]){border-bottom-style:solid}html :where([style*=border-left-color]){border-left-style:solid}html :where([style*=border-width]){border-style:solid}html :where([style*=border-top-width]){border-top-style:solid}html :where([style*=border-right-width]){border-right-style:solid}html :where([style*=border-bottom-width]){border-bottom-style:solid}html :where([style*=border-left-width]){border-left-style:solid}html :where(img[class*=wp-image-]){height:auto;max-width:100%}:where(figure){margin:0 0 1em}html :where(.is-position-sticky){--wp-admin--admin-bar--position-offset:var(--wp-admin--admin-bar--height,0px)}@media screen and (max-width:600px){html :where(.is-position-sticky){--wp-admin--admin-bar--position-offset:0px}}

/*# sourceURL=/wp-includes/css/dist/block-library/common.min.css */
</style>

<link rel='stylesheet' id='mpp_gutenberg-css' href='https://devblogs.microsoft.com/typescript/wp-content/plugins/metronet-profile-picture/dist/blocks.style.build.css?ver=2.6.4' media='all' />
<link rel='preload' as='style' onload="this.onload=null;this.rel='stylesheet'" id='devblogs-lightbox-css-css' href='https://devblogs.microsoft.com/typescript/wp-content/plugins/devblogs-lightbox/assets/css/lightbox.min.css?ver=1770924660' media='all' />
<noscript><link rel='stylesheet' id='devblogs-lightbox-css-css' href='https://devblogs.microsoft.com/typescript/wp-content/plugins/devblogs-lightbox/assets/css/lightbox.min.css?ver=1770924660' media='all' />
</noscript><link rel='stylesheet' id='newsletter-css' href='https://devblogs.microsoft.com/typescript/wp-content/plugins/newsletter/style.css?ver=9.3.0' media='all' />
<link rel='stylesheet' id='newsletter-country-sync-css-css' href='https://devblogs.microsoft.com/typescript/wp-content/plugins/newsletter-country-sync/css/newsletter-style.css?ver=1770924660' media='all' />
<link rel='preload' as='style' onload="this.onload=null;this.rel='stylesheet'" id='devblogs-evo-styles-css' href='https://devblogs.microsoft.com/typescript/wp-content/themes/devblogs-evo/css/theme.min.css?ver=1.4.0.1784230473' media='all' />
<noscript><link rel='stylesheet' id='devblogs-evo-styles-css' href='https://devblogs.microsoft.com/typescript/wp-content/themes/devblogs-evo/css/theme.min.css?ver=1.4.0.1784230473' media='all' />
</noscript><link rel='stylesheet' id='fabric-icons-css' href='https://devblogs.microsoft.com/typescript/wp-content/plugins/fabric-icon-manager/assets/css/fabric-icons.css?ver=1699358813' media='all' />
<link rel='stylesheet' id='dev-comments-evo-style-css' href='https://devblogs.microsoft.com/typescript/wp-content/plugins/devblogs-comments-evo/admin/css/simplecomments.min.css?ver=1783529315' media='all' />
<link rel='stylesheet' id='dashicons-css' href='https://devblogs.microsoft.com/typescript/wp-includes/css/dashicons.min.css' media='all' />
<link rel='stylesheet' id='editor-buttons-css' href='https://devblogs.microsoft.com/typescript/wp-includes/css/editor.min.css' media='all' />
<link rel='stylesheet' id='block-custom-css' href='https://devblogs.microsoft.com/typescript/wp-content/plugins/devblogs-blocks/assets/block-custom.css' media='all' />
<link rel='preload' as='style' onload="this.onload=null;this.rel='stylesheet'"id='highlight-css-css' href='https://devblogs.microsoft.com/typescript/wp-content/plugins/devblogs-blocks/assets/highlight.min.css' media='all' />
<noscript><link rel='stylesheet'id='highlight-css-css' href='https://devblogs.microsoft.com/typescript/wp-content/plugins/devblogs-blocks/assets/highlight.min.css' media='all' />
</noscript><script type="text/javascript">
            window._nslDOMReady = (function () {
                const executedCallbacks = new Set();
            
                return function (callback) {
                    /**
                    * Third parties might dispatch DOMContentLoaded events, so we need to ensure that we only run our callback once!
                    */
                    if (executedCallbacks.has(callback)) return;
            
                    const wrappedCallback = function () {
                        if (executedCallbacks.has(callback)) return;
                        executedCallbacks.add(callback);
                        callback();
                    };
            
                    if (document.readyState === "complete" || document.readyState === "interactive") {
                        wrappedCallback();
                    } else {
                        document.addEventListener("DOMContentLoaded", wrappedCallback);
                    }
                };
            })();
        </script><script id="jquery-core-js" src="https://devblogs.microsoft.com/typescript/wp-includes/js/jquery/jquery.min.js?ver=3.7.1"></script>
<script id="back-to-top-script-js" src="https://devblogs.microsoft.com/typescript/wp-content/themes/devblogs-evo/js/back-to-top.min.js?ver=1737047887"></script>
<link rel="https://api.w.org/" href="https://devblogs.microsoft.com/typescript/wp-json/" /><link rel="alternate" title="JSON" type="application/json" href="https://devblogs.microsoft.com/typescript/wp-json/wp/v2/posts/4962" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://devblogs.microsoft.com/typescript/xmlrpc.php?rsd" />
<link rel='shortlink' href='https://devblogs.microsoft.com/typescript/?p=4962' />
<script type="application/ld+json">{"@context":"https:\/\/schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Dev Blogs","item":"https:\/\/devblogs.microsoft.com\/"},{"@type":"ListItem","position":2,"name":"TypeScript","item":"https:\/\/devblogs.microsoft.com\/typescript\/"},{"@type":"ListItem","position":3,"name":"Announcing TypeScript 5.9 RC","item":"https:\/\/devblogs.microsoft.com\/typescript\/announcing-typescript-5-9-rc\/"}]}</script><meta name="generator" content="performance-lab 4.2.0; plugins: ">
<style>#respond h3#reply-title{display:none;}</style><link rel="icon" href="https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2018/10/Microsoft-Favicon.png" sizes="32x32" />
<link rel="icon" href="https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2018/10/Microsoft-Favicon.png" sizes="192x192" />
<link rel="apple-touch-icon" href="https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2018/10/Microsoft-Favicon.png" />
<meta name="msapplication-TileImage" content="https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2018/10/Microsoft-Favicon.png" />
<style type="text/css">div.nsl-container[data-align="left"] {
    text-align: left;
}

div.nsl-container[data-align="center"] {
    text-align: center;
}

div.nsl-container[data-align="right"] {
    text-align: right;
}


div.nsl-container div.nsl-container-buttons a[data-plugin="nsl"] {
    text-decoration: none;
    box-shadow: none;
    border: 0;
}

div.nsl-container .nsl-container-buttons {
    display: flex;
    padding: 5px 0;
}

div.nsl-container.nsl-container-block .nsl-container-buttons {
    display: inline-grid;
    grid-template-columns: minmax(145px, auto);
}

div.nsl-container-block-fullwidth .nsl-container-buttons {
    flex-flow: column;
    align-items: center;
}

div.nsl-container-block-fullwidth .nsl-container-buttons a,
div.nsl-container-block .nsl-container-buttons a {
    flex: 1 1 auto;
    display: block;
    margin: 5px 0;
    width: 100%;
}

div.nsl-container-inline {
    margin: -5px;
    text-align: left;
}

div.nsl-container-inline .nsl-container-buttons {
    justify-content: center;
    flex-wrap: wrap;
}

div.nsl-container-inline .nsl-container-buttons a {
    margin: 5px;
    display: inline-block;
}

div.nsl-container-grid .nsl-container-buttons {
    flex-flow: row;
    align-items: center;
    flex-wrap: wrap;
}

div.nsl-container-grid .nsl-container-buttons a {
    flex: 1 1 auto;
    display: block;
    margin: 5px;
    max-width: 280px;
    width: 100%;
}

@media only screen and (min-width: 650px) {
    div.nsl-container-grid .nsl-container-buttons a {
        width: auto;
    }
}

div.nsl-container .nsl-button {
    cursor: pointer;
    vertical-align: top;
    border-radius: 4px;
}

div.nsl-container .nsl-button-default {
    color: #fff;
    display: flex;
}

div.nsl-container .nsl-button-icon {
    display: inline-block;
}

div.nsl-container .nsl-button-svg-container {
    flex: 0 0 auto;
    padding: 8px;
    display: flex;
    align-items: center;
}

div.nsl-container svg {
    height: 24px;
    width: 24px;
    vertical-align: top;
}

div.nsl-container .nsl-button-default div.nsl-button-label-container {
    margin: 0 24px 0 12px;
    padding: 10px 0;
    font-family: Helvetica, Arial, sans-serif;
    font-size: 16px;
    line-height: 20px;
    letter-spacing: .25px;
    overflow: hidden;
    text-align: center;
    text-overflow: clip;
    white-space: nowrap;
    flex: 1 1 auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-transform: none;
    display: inline-block;
}

div.nsl-container .nsl-button-google[data-skin="light"] {
    box-shadow: inset 0 0 0 1px #747775;
    color: #1f1f1f;
}

div.nsl-container .nsl-button-google[data-skin="dark"] {
    box-shadow: inset 0 0 0 1px #8E918F;
    color: #E3E3E3;
}

div.nsl-container .nsl-button-google[data-skin="neutral"] {
    color: #1F1F1F;
}

div.nsl-container .nsl-button-google div.nsl-button-label-container {
    font-family: "Roboto Medium", Roboto, Helvetica, Arial, sans-serif;
}

div.nsl-container .nsl-button-apple .nsl-button-svg-container {
    padding: 0 6px;
}

div.nsl-container .nsl-button-apple .nsl-button-svg-container svg {
    height: 40px;
    width: auto;
}

div.nsl-container .nsl-button-apple[data-skin="light"] {
    color: #000;
    box-shadow: 0 0 0 1px #000;
}

div.nsl-container .nsl-button-facebook[data-skin="white"] {
    color: #000;
    box-shadow: inset 0 0 0 1px #000;
}

div.nsl-container .nsl-button-facebook[data-skin="light"] {
    color: #1877F2;
    box-shadow: inset 0 0 0 1px #1877F2;
}

div.nsl-container .nsl-button-spotify[data-skin="white"] {
    color: #191414;
    box-shadow: inset 0 0 0 1px #191414;
}

div.nsl-container .nsl-button-apple div.nsl-button-label-container {
    font-size: 17px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
}

div.nsl-container .nsl-button-slack div.nsl-button-label-container {
    font-size: 17px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
}

div.nsl-container .nsl-button-slack[data-skin="light"] {
    color: #000000;
    box-shadow: inset 0 0 0 1px #DDDDDD;
}

div.nsl-container .nsl-button-tiktok[data-skin="light"] {
    color: #161823;
    box-shadow: 0 0 0 1px rgba(22, 24, 35, 0.12);
}


div.nsl-container .nsl-button-kakao {
    color: rgba(0, 0, 0, 0.85);
}

.nsl-clear {
    clear: both;
}

.nsl-container {
    clear: both;
}

.nsl-disabled-provider .nsl-button {
    filter: grayscale(1);
    opacity: 0.8;
}

/*Button align start*/

div.nsl-container-inline[data-align="left"] .nsl-container-buttons {
    justify-content: flex-start;
}

div.nsl-container-inline[data-align="center"] .nsl-container-buttons {
    justify-content: center;
}

div.nsl-container-inline[data-align="right"] .nsl-container-buttons {
    justify-content: flex-end;
}


div.nsl-container-grid[data-align="left"] .nsl-container-buttons {
    justify-content: flex-start;
}

div.nsl-container-grid[data-align="center"] .nsl-container-buttons {
    justify-content: center;
}

div.nsl-container-grid[data-align="right"] .nsl-container-buttons {
    justify-content: flex-end;
}

div.nsl-container-grid[data-align="space-around"] .nsl-container-buttons {
    justify-content: space-around;
}

div.nsl-container-grid[data-align="space-between"] .nsl-container-buttons {
    justify-content: space-between;
}

/* Button align end*/

/* Redirect */

#nsl-redirect-overlay {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: fixed;
    z-index: 1000000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    backdrop-filter: blur(1px);
    background-color: RGBA(0, 0, 0, .32);;
}

#nsl-redirect-overlay-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: white;
    padding: 30px;
    border-radius: 10px;
}

#nsl-redirect-overlay-spinner {
    content: '';
    display: block;
    margin: 20px;
    border: 9px solid RGBA(0, 0, 0, .6);
    border-top: 9px solid #fff;
    border-radius: 50%;
    box-shadow: inset 0 0 0 1px RGBA(0, 0, 0, .6), 0 0 0 1px RGBA(0, 0, 0, .6);
    width: 40px;
    height: 40px;
    animation: nsl-loader-spin 2s linear infinite;
}

@keyframes nsl-loader-spin {
    0% {
        transform: rotate(0deg)
    }
    to {
        transform: rotate(360deg)
    }
}

#nsl-redirect-overlay-title {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
    font-size: 18px;
    font-weight: bold;
    color: #3C434A;
}

#nsl-redirect-overlay-text {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
    text-align: center;
    font-size: 14px;
    color: #3C434A;
}

/* Redirect END*/</style><style type="text/css">/* Notice fallback */
#nsl-notices-fallback {
    position: fixed;
    right: 10px;
    top: 10px;
    z-index: 10000;
}

.admin-bar #nsl-notices-fallback {
    top: 42px;
}

#nsl-notices-fallback > div {
    position: relative;
    background: #fff;
    border-left: 4px solid #fff;
    box-shadow: 0 1px 1px 0 rgba(0, 0, 0, .1);
    margin: 5px 15px 2px;
    padding: 1px 20px;
}

#nsl-notices-fallback > div.error {
    display: block;
    border-left-color: #dc3232;
}

#nsl-notices-fallback > div.updated {
    display: block;
    border-left-color: #46b450;
}

#nsl-notices-fallback p {
    margin: .5em 0;
    padding: 2px;
}

#nsl-notices-fallback > div:after {
    position: absolute;
    right: 5px;
    top: 5px;
    content: '\00d7';
    display: block;
    height: 16px;
    width: 16px;
    line-height: 16px;
    text-align: center;
    font-size: 20px;
    cursor: pointer;
}</style>	<!-- Start JSLL SHIM(1DS) Tags -->
	<script src="https://js.monitor.azure.com/scripts/c/ms.jsll-4.min.js" type="text/javascript"></script>
	<script type="text/javascript">
		var config = {
			useDefaultContentName: true,
			useShortNameForContentBlob: false,
//			disablePageUnloadEvents: [0, 1, 2],  // Try at top level for JSLL
			autoCapture: {
				pageView: true,
				onLoad: true,
				lineage: true,
				click: true,
				scroll: true,
				resize: false,
				jsError: true,
				addin: true,
				perf: true
			},
			disableUnloadBeacon: true,  // Disable deprecated unload event listeners
			urlCollectHash: true,
			urlCollectQuery: true,
			instrumentationKey: "31b03416b80d4fec81330cf396b8bf63-2db31b2d-ee29-4371-af87-871cba555f5a-7031",
			coreData: {
				appId: "MSDevBlogs",
			},
			// Initially set the GPC_DataSharingOptIn flag property in 1DS (One Data Source) to false
			advancedConfig: {
				propertyConfiguration: {
					gpcDataSharingOptIn: false
				}
			},
			callback: {
				pageName: function () { return document.title },
				contentUpdatePageTags: function () {

					return {
						metaTags: {
							'ver': theme
						},
					}
				},
				pageActionContentTags: function () {

					return {
						metaTags: {
							'ver': theme
						},
					}
				},
				pageActionPageTags: function () {

					return {
																			"pageType": "post",
																																													"pgauth": "Daniel Rosenwasser",
																																									"authtype": "site_owner",
																																																						"pgtop": "TypeScript, ",
							 
					 				  metaTags: {
																					"publishedDate": '20250725',
											  'ver': theme
						},
					}
				},
				pageViewPageTags: function () {
					return {
																	"pageType": "post",
																																									"pgauth": "Daniel Rosenwasser",
																																							"authtype": "site_owner",
																																																			"pgtop": "TypeScript, ",
																																							"metaTags": {
									"publishedDate": '20250725',
								}
												  
		  					}
				},
			}
		};
		awa.init(config);

		// Suppress Microsoft JSLL v4 internal unload event deprecation warnings
		// TODO: Remove when Microsoft updates JSLL to fix internal Application Insights Core JS deprecation
		(function() {
			const originalWarn = console.warn;
			console.warn = function(...args) {
				const message = args.join(' ');
				// Suppress specific deprecation warning from Microsoft's Application Insights SDK
				// Pattern specifically targets Microsoft SDK file path to avoid false positives
				if (message.includes('EventHelpers.js') && message.includes('deprecated')) {
					// Optionally log once for debugging (comment out for production)
					// if (!window._jsllWarningSuppressed) {
					//     console.log('[Suppressed JSLL SDK deprecation warning]');
					//     window._jsllWarningSuppressed = true;
					// }
					return;
				}
				originalWarn.apply(console, args);
			};
		})();	
	</script>
	<!-- END JSLL SHIM(1DS) Integration -->
	<script>
		/*! lazysizes - v4.1.3 | For lazy loading images */
		!function (a, b) { var c = b(a, a.document); a.lazySizes = c, "object" == typeof module && module.exports && (module.exports = c) }(window, function (a, b) { "use strict"; if (b.getElementsByClassName) { var c, d, e = b.documentElement, f = a.Date, g = a.HTMLPictureElement, h = "addEventListener", i = "getAttribute", j = a[h], k = a.setTimeout, l = a.requestAnimationFrame || k, m = a.requestIdleCallback, n = /^picture$/i, o = ["load", "error", "lazyincluded", "_lazyloaded"], p = {}, q = Array.prototype.forEach, r = function (a, b) { return p[b] || (p[b] = new RegExp("(\\s|^)" + b + "(\\s|$)")), p[b].test(a[i]("class") || "") && p[b] }, s = function (a, b) { r(a, b) || a.setAttribute("class", (a[i]("class") || "").trim() + " " + b) }, t = function (a, b) { var c; (c = r(a, b)) && a.setAttribute("class", (a[i]("class") || "").replace(c, " ")) }, u = function (a, b, c) { var d = c ? h : "removeEventListener"; c && u(a, b), o.forEach(function (c) { a[d](c, b) }) }, v = function (a, d, e, f, g) { var h = b.createEvent("Event"); return e || (e = {}), e.instance = c, h.initEvent(d, !f, !g), h.detail = e, a.dispatchEvent(h), h }, w = function (b, c) { var e; !g && (e = a.picturefill || d.pf) ? (c && c.src && !b[i]("srcset") && b.setAttribute("srcset", c.src), e({ reevaluate: !0, elements: [b] })) : c && c.src && (b.src = c.src) }, x = function (a, b) { return (getComputedStyle(a, null) || {})[b] }, y = function (a, b, c) { for (c = c || a.offsetWidth; c < d.minSize && b && !a._lazysizesWidth;)c = b.offsetWidth, b = b.parentNode; return c }, z = function () { var a, c, d = [], e = [], f = d, g = function () { var b = f; for (f = d.length ? e : d, a = !0, c = !1; b.length;)b.shift()(); a = !1 }, h = function (d, e) { a && !e ? d.apply(this, arguments) : (f.push(d), c || (c = !0, (b.hidden ? k : l)(g))) }; return h._lsFlush = g, h }(), A = function (a, b) { return b ? function () { z(a) } : function () { var b = this, c = arguments; z(function () { a.apply(b, c) }) } }, B = function (a) { var b, c = 0, e = d.throttleDelay, g = d.ricTimeout, h = function () { b = !1, c = f.now(), a() }, i = m && g > 49 ? function () { m(h, { timeout: g }), g !== d.ricTimeout && (g = d.ricTimeout) } : A(function () { k(h) }, !0); return function (a) { var d; (a = a === !0) && (g = 33), b || (b = !0, d = e - (f.now() - c), 0 > d && (d = 0), a || 9 > d ? i() : k(i, d)) } }, C = function (a) { var b, c, d = 99, e = function () { b = null, a() }, g = function () { var a = f.now() - c; d > a ? k(g, d - a) : (m || e)(e) }; return function () { c = f.now(), b || (b = k(g, d)) } }; !function () { var b, c = { lazyClass: "lazyload", loadedClass: "lazyloaded", loadingClass: "lazyloading", preloadClass: "lazypreload", errorClass: "lazyerror", autosizesClass: "lazyautosizes", srcAttr: "data-src", srcsetAttr: "data-srcset", sizesAttr: "data-sizes", minSize: 40, customMedia: {}, init: !0, expFactor: 1.5, hFac: .8, loadMode: 2, loadHidden: !0, ricTimeout: 0, throttleDelay: 125 }; d = a.lazySizesConfig || a.lazysizesConfig || {}; for (b in c) b in d || (d[b] = c[b]); a.lazySizesConfig = d, k(function () { d.init && F() }) }(); var D = function () { var g, l, m, o, p, y, D, F, G, H, I, J, K, L, M = /^img$/i, N = /^iframe$/i, O = "onscroll" in a && !/(gle|ing)bot/.test(navigator.userAgent), P = 0, Q = 0, R = 0, S = -1, T = function (a) { R--, a && a.target && u(a.target, T), (!a || 0 > R || !a.target) && (R = 0) }, U = function (a, c) { var d, f = a, g = "hidden" == x(b.body, "visibility") || "hidden" != x(a.parentNode, "visibility") && "hidden" != x(a, "visibility"); for (F -= c, I += c, G -= c, H += c; g && (f = f.offsetParent) && f != b.body && f != e;)g = (x(f, "opacity") || 1) > 0, g && "visible" != x(f, "overflow") && (d = f.getBoundingClientRect(), g = H > d.left && G < d.right && I > d.top - 1 && F < d.bottom + 1); return g }, V = function () { var a, f, h, j, k, m, n, p, q, r = c.elements; if ((o = d.loadMode) && 8 > R && (a = r.length)) { f = 0, S++, null == K && ("expand" in d || (d.expand = e.clientHeight > 500 && e.clientWidth > 500 ? 500 : 370), J = d.expand, K = J * d.expFactor), K > Q && 1 > R && S > 2 && o > 2 && !b.hidden ? (Q = K, S = 0) : Q = o > 1 && S > 1 && 6 > R ? J : P; for (; a > f; f++)if (r[f] && !r[f]._lazyRace) if (O) if ((p = r[f][i]("data-expand")) && (m = 1 * p) || (m = Q), q !== m && (y = innerWidth + m * L, D = innerHeight + m, n = -1 * m, q = m), h = r[f].getBoundingClientRect(), (I = h.bottom) >= n && (F = h.top) <= D && (H = h.right) >= n * L && (G = h.left) <= y && (I || H || G || F) && (d.loadHidden || "hidden" != x(r[f], "visibility")) && (l && 3 > R && !p && (3 > o || 4 > S) || U(r[f], m))) { if (ba(r[f]), k = !0, R > 9) break } else !k && l && !j && 4 > R && 4 > S && o > 2 && (g[0] || d.preloadAfterLoad) && (g[0] || !p && (I || H || G || F || "auto" != r[f][i](d.sizesAttr))) && (j = g[0] || r[f]); else ba(r[f]); j && !k && ba(j) } }, W = B(V), X = function (a) { s(a.target, d.loadedClass), t(a.target, d.loadingClass), u(a.target, Z), v(a.target, "lazyloaded") }, Y = A(X), Z = function (a) { Y({ target: a.target }) }, $ = function (a, b) { try { a.contentWindow.location.replace(b) } catch (c) { a.src = b } }, _ = function (a) { var b, c = a[i](d.srcsetAttr); (b = d.customMedia[a[i]("data-media") || a[i]("media")]) && a.setAttribute("media", b), c && a.setAttribute("srcset", c) }, aa = A(function (a, b, c, e, f) { var g, h, j, l, o, p; (o = v(a, "lazybeforeunveil", b)).defaultPrevented || (e && (c ? s(a, d.autosizesClass) : a.setAttribute("sizes", e)), h = a[i](d.srcsetAttr), g = a[i](d.srcAttr), f && (j = a.parentNode, l = j && n.test(j.nodeName || "")), p = b.firesLoad || "src" in a && (h || g || l), o = { target: a }, p && (u(a, T, !0), clearTimeout(m), m = k(T, 2500), s(a, d.loadingClass), u(a, Z, !0)), l && q.call(j.getElementsByTagName("source"), _), h ? a.setAttribute("srcset", h) : g && !l && (N.test(a.nodeName) ? $(a, g) : a.src = g), f && (h || l) && w(a, { src: g })), a._lazyRace && delete a._lazyRace, t(a, d.lazyClass), z(function () { (!p || a.complete && a.naturalWidth > 1) && (p ? T(o) : R--, X(o)) }, !0) }), ba = function (a) { var b, c = M.test(a.nodeName), e = c && (a[i](d.sizesAttr) || a[i]("sizes")), f = "auto" == e; (!f && l || !c || !a[i]("src") && !a.srcset || a.complete || r(a, d.errorClass) || !r(a, d.lazyClass)) && (b = v(a, "lazyunveilread").detail, f && E.updateElem(a, !0, a.offsetWidth), a._lazyRace = !0, R++, aa(a, b, f, e, c)) }, ca = function () { if (!l) { if (f.now() - p < 999) return void k(ca, 999); var a = C(function () { d.loadMode = 3, W() }); l = !0, d.loadMode = 3, W(), j("scroll", function () { 3 == d.loadMode && (d.loadMode = 2), a() }, !0) } }; return { _: function () { p = f.now(), c.elements = b.getElementsByClassName(d.lazyClass), g = b.getElementsByClassName(d.lazyClass + " " + d.preloadClass), L = d.hFac, j("scroll", W, !0), j("resize", W, !0), a.MutationObserver ? new MutationObserver(W).observe(e, { childList: !0, subtree: !0, attributes: !0 }) : (e[h]("DOMNodeInserted", W, !0), e[h]("DOMAttrModified", W, !0), setInterval(W, 999)), j("hashchange", W, !0), ["focus", "mouseover", "click", "load", "transitionend", "animationend", "webkitAnimationEnd"].forEach(function (a) { b[h](a, W, !0) }), /d$|^c/.test(b.readyState) ? ca() : (j("load", ca), b[h]("DOMContentLoaded", W), k(ca, 2e4)), c.elements.length ? (V(), z._lsFlush()) : W() }, checkElems: W, unveil: ba } }(), E = function () { var a, c = A(function (a, b, c, d) { var e, f, g; if (a._lazysizesWidth = d, d += "px", a.setAttribute("sizes", d), n.test(b.nodeName || "")) for (e = b.getElementsByTagName("source"), f = 0, g = e.length; g > f; f++)e[f].setAttribute("sizes", d); c.detail.dataAttr || w(a, c.detail) }), e = function (a, b, d) { var e, f = a.parentNode; f && (d = y(a, f, d), e = v(a, "lazybeforesizes", { width: d, dataAttr: !!b }), e.defaultPrevented || (d = e.detail.width, d && d !== a._lazysizesWidth && c(a, f, e, d))) }, f = function () { var b, c = a.length; if (c) for (b = 0; c > b; b++)e(a[b]) }, g = C(f); return { _: function () { a = b.getElementsByClassName(d.autosizesClass), j("resize", g) }, checkElems: g, updateElem: e } }(), F = function () { F.i || (F.i = !0, E._(), D._()) }; return c = { cfg: d, autoSizer: E, loader: D, init: F, uP: w, aC: s, rC: t, hC: r, fire: v, gW: y, rAF: z } } });
	</script>
	<div id="sr-announcer" class="visually-hidden" role="status" aria-live="polite"></div>
<style id="global-styles-inline-css">
:root{--wp--preset--aspect-ratio--square: 1;--wp--preset--aspect-ratio--4-3: 4/3;--wp--preset--aspect-ratio--3-4: 3/4;--wp--preset--aspect-ratio--3-2: 3/2;--wp--preset--aspect-ratio--2-3: 2/3;--wp--preset--aspect-ratio--16-9: 16/9;--wp--preset--aspect-ratio--9-16: 9/16;--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgb(6,147,227) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgb(252,185,0) 0%,rgb(255,105,0) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgb(255,105,0) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgb(255, 255, 255), 6px 6px rgb(0, 0, 0);--wp--preset--shadow--crisp: 6px 6px 0px rgb(0, 0, 0);}:root { --wp--style--global--content-size: 840px;--wp--style--global--wide-size: 840px; }:where(body) { margin: 0; }.wp-site-blocks > .alignleft { float: left; margin-right: 2em; }.wp-site-blocks > .alignright { float: right; margin-left: 2em; }.wp-site-blocks > .aligncenter { justify-content: center; margin-left: auto; margin-right: auto; }:where(.is-layout-flex){gap: 0.5em;}:where(.is-layout-grid){gap: 0.5em;}.is-layout-flow > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}.is-layout-flow > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}.is-layout-flow > .aligncenter{margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}.is-layout-constrained > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}.is-layout-constrained > .aligncenter{margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > :where(:not(.alignleft):not(.alignright):not(.alignfull)){max-width: var(--wp--style--global--content-size);margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > .alignwide{max-width: var(--wp--style--global--wide-size);}body .is-layout-flex{display: flex;}.is-layout-flex{flex-wrap: wrap;align-items: center;}.is-layout-flex > :is(*, div){margin: 0;}body .is-layout-grid{display: grid;}.is-layout-grid > :is(*, div){margin: 0;}body{padding-top: 0px;padding-right: 0px;padding-bottom: 0px;padding-left: 0px;}:root :where(.wp-element-button, .wp-block-button__link){background-color: #32373c;border-width: 0;color: #fff;font-family: inherit;font-size: inherit;font-style: inherit;font-weight: inherit;letter-spacing: inherit;line-height: inherit;padding-top: calc(0.667em + 2px);padding-right: calc(1.333em + 2px);padding-bottom: calc(0.667em + 2px);padding-left: calc(1.333em + 2px);text-decoration: none;text-transform: inherit;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
/*# sourceURL=global-styles-inline-css */
</style>
<link rel='stylesheet' id='buttons-css' href='https://devblogs.microsoft.com/typescript/wp-includes/css/buttons.min.css' media='all' />

</head>

<body class="wp-singular post-template-default single single-post postid-4962 single-format-standard wp-theme-devblogs-evo">
	<!-- Star cookies banner  -->
	<script src="https://wcpstatic.microsoft.com/mscc/lib/v2/wcp-consent.js" defer></script>

	<div id="cookie-banner"></div>
	
	<!-- end cookies banner  -->
		<!-- UHF header -->
	<uhf-header locale="en-us" partnerId="DEV_Blogs" headerId="Dev_header-main" theme="light">
    <a slot="skip-link" class="uhf-skip-link" href="#mainContent" data-m='{"compnm": "UHF", "view": "UHF", "pa": "UniversalHeader", "hn": "SkipToMain", "cN": "Skip to content_nonnav", "ecn": "Skip to content_nonnav", "ehn": "SkipToMain"}'>Skip to main content</a>
    
<uhf-brand slot="brand">
    <a href="https://www.microsoft.com" class="uhf-microsoft-logo" slot="microsoft-logo" aria-label="Microsoft" data-m="{&quot;compnm&quot;: &quot;UHF&quot;, &quot;view&quot;: &quot;UHF&quot;, &quot;pa&quot;: &quot;UniversalHeader&quot;, &quot;hn&quot;: &quot;Anchor&quot;, &quot;cN&quot;: &quot;GlobalNav_Logo_cont&quot;, &quot;ecn&quot;: &quot;GlobalNav_Logo_cont&quot;, &quot;ehn&quot;: &quot;Anchor&quot;}">
        <img src="https://uhf.microsoft.com/images/microsoft/RE1Mu3b.png" alt="Microsoft" />
    </a>
            <a href="https://devblogs.microsoft.com" class="uhf-site-logo" slot="brand-logo" aria-label="Dev Blogs" data-m="{&quot;compnm&quot;: &quot;UHF&quot;, &quot;view&quot;: &quot;UHF&quot;, &quot;pa&quot;: &quot;UniversalHeader&quot;, &quot;hn&quot;: &quot;Anchor&quot;, &quot;cN&quot;: &quot;CatNav_Logo_cont&quot;, &quot;ecn&quot;: &quot;CatNav_Logo_cont&quot;, &quot;ehn&quot;: &quot;Anchor&quot;}">
 <span>Dev Blogs</span>             </a>
</uhf-brand>


<uhf-contextual-nav 
    slot="contextual-nav" 
    overflowText="More" 
    brand="Dev Blogs" 
    homeUrl="https://devblogs.microsoft.com" 
    homeText="Home"
    data-nav-label="Contextual menu"
    theme=cat-theme-blue
    >


    <a class="