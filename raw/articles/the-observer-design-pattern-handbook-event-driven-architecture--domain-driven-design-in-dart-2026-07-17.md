---
source_url: https://www.freecodecamp.org/news/the-observer-design-pattern-handbook-event-driven-architecture-domain-driven-design-in-dart/
ingested: 2026-07-17
sha256: 369c5fb14a3bdd34f6678682e68a40965ba2ee16eac3eb1c8f438b9a08661920
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>The Observer Design Pattern Handbook: Event-Driven Architecture &amp; Domain-Driven Design in Dart</title>
        
        <meta name="HandheldFriendly" content="True">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <script>
            (function() {
                var theme = localStorage.getItem('theme');
                if (theme === 'dark' || (!theme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                    document.documentElement.classList.add('dark-mode');
                }
            })();
        </script>

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="preload" as="style" onload="this.onload=null;this.rel='stylesheet'" href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,300;0,400;0,700;1,400&family=Roboto+Mono:wght@400;700&display=swap">
        

        
        
    <link id="prism-theme-light" rel="preload" as="style" onload="this.onload=null;this.rel='stylesheet'" href="https://cdn.freecodecamp.org/news-assets/prism/1.29.0/themes/prism.min.css">
<noscript>
  <link rel="stylesheet" href="https://cdn.freecodecamp.org/news-assets/prism/1.29.0/themes/prism.min.css">
</noscript>
<link id="prism-theme-dark" rel="preload" as="style" onload="this.onload=null;this.rel='stylesheet'" href="https://cdn.freecodecamp.org/news-assets/prism/1.29.0/themes/prism-dark.min.css">
<noscript>
  <link rel="stylesheet" href="https://cdn.freecodecamp.org/news-assets/prism/1.29.0/themes/prism-dark.min.css">
</noscript>
<script>
  (function() {
    var isDark = document.documentElement.classList.contains('dark-mode');
    var light = document.getElementById('prism-theme-light');
    var dark = document.getElementById('prism-theme-dark');
    if (isDark) {
      light.disabled = true;
    } else {
      dark.disabled = true;
    }
  })();
</script>
<link rel="preload" as="style" onload="this.onload=null;this.rel='stylesheet'" href="https://cdn.freecodecamp.org/news-assets/prism/1.29.0/plugins/unescaped-markup/prism-unescaped-markup.min.css">
<noscript>
  <link rel="stylesheet" href="https://cdn.freecodecamp.org/news-assets/prism/1.29.0/plugins/unescaped-markup/prism-unescaped-markup.min.css">
</noscript>

<script defer="" src="https://cdn.freecodecamp.org/news-assets/prism/1.29.0/components/prism-core.min.js"></script>
<script defer="" src="https://cdn.freecodecamp.org/news-assets/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>



        
        <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/fontawesome.min.css">
        <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/solid.min.css">

        
        <link rel="preload" as="style" onload="this.onload=null;this.rel='stylesheet'" href="/news/assets/css/global-f141287a91.css">
        <link rel="stylesheet" type="text/css" href="/news/assets/css/variables-54e5c7c52a.css">
        <link rel="stylesheet" type="text/css" href="/news/assets/css/print-118c07de60.css">
        <link rel="stylesheet" type="text/css" href="/news/assets/css/screen-a351a10db4.css">
        <link rel="stylesheet" type="text/css" href="/news/assets/css/search-bar-beba8d2b76.css">

        
        <script defer="" src="https://cdn.freecodecamp.org/news-assets/algolia/algoliasearch/5.46.3/lite/browser.umd.js"></script>
        <script defer="" src="https://cdn.freecodecamp.org/news-assets/algolia/autocomplete/1.19.4/index.production.min.js"></script>

        
        <script defer="" src="https://cdn.freecodecamp.org/news-assets/dayjs/1.10.4/dayjs.min.js"></script>
        <script defer="" src="https://cdn.freecodecamp.org/news-assets/dayjs/1.10.4/localizedFormat.min.js"></script>
        <script defer="" src="https://cdn.freecodecamp.org/news-assets/dayjs/1.10.4/relativeTime.min.js"></script>

        
        
            <script defer="" src="https://cdn.freecodecamp.org/news-assets/dayjs/1.10.4/locale/en.min.js"></script>
        

        
        <script>document.addEventListener("DOMContentLoaded",async()=>{const{liteClient:e}=window["algoliasearch/lite"],{autocomplete:t,getAlgoliaResults:n}=window["@algolia/autocomplete-js"],a=e("QMJYL5WYTI","89770b24481654192d7a5c402c6ad9a0"),s=window.screen.width>=767&&window.screen.height>=768?8:5,o=((e,t)=>{let n;return(...a)=>(n&&clearTimeout(n),new Promise(s=>{n=setTimeout(()=>s(e(...a)),t)}))})(e=>Promise.resolve(e),200),i=e=>t({container:e,panelContainer:e,stallThreshold:500,detachedMediaQuery:"none",debug:!0,placeholder:Number("12800")<100?"Search our news articles, tutorials, and books":"Search 12,800+ news articles, tutorials, and books",getSources:()=>o([{sourceId:"links",getItemUrl:({item:e})=>e.url,getItems:({query:e})=>n({searchClient:a,queries:[{indexName:"news",params:{query:e,hitsPerPage:s}}]}),templates:{item:({item:e,components:t,html:n})=>n`<a class="aa-ItemLink" href=${e.url}>
                  <div class="aa-ItemContent">
                    <div class="aa-ItemContentBody">
                      <div class="aa-ItemContentTitle">
                        ${t.Highlight({hit:e,attribute:"title",tagName:"mark"})}
                      </div>
                    </div>
                  </div>
                </a>`,footer({state:e,html:t}){const n=e?.query,a=e?.collections[0]?.items;if(a.length)return t`<a
                    class="aa-ItemLink"
                    href="https://www.freecodecamp.org/news/search?query=${n}"
                    ><div class="aa-ItemContent">
                      See all results for ${n}
                    </div></a
                  >`},noResults:()=>"No results found"}}])}),r=i("#nav-left-search-container");i("#nav-right-search-container");const c=document.querySelectorAll(".fcc-search-container");document.addEventListener("keydown",e=>{e.target instanceof HTMLInputElement||e.target instanceof HTMLTextAreaElement||e.target.isContentEditable||"/"!==e.key&&"s"!==e.key||(e.preventDefault(),c.forEach(e=>{e.checkVisibility()&&e.querySelector("input").focus()}))}),c.forEach(e=>{e.addEventListener("submit",t=>{t.preventDefault();const n=e.querySelector("input").value.trim(),a=e.querySelector(".aa-List");n&&a&&window.location.assign(`https://www.freecodecamp.org/news/search?query=${n}`)})}),document.addEventListener("click",e=>{e.target!==document.querySelector("#nav-left-search-container .aa-Form")&&r.setIsOpen(!1)})}),document.addEventListener("DOMContentLoaded",()=>{dayjs.extend(dayjs_plugin_localizedFormat),dayjs.extend(dayjs_plugin_relativeTime),dayjs.locale("en")});const isAuthenticated=document.cookie.split(";").some(e=>e.trim().startsWith("jwt_access_token=")),isDonor=document.cookie.split(";").some(e=>e.trim().startsWith("isDonor=true"));document.addEventListener("DOMContentLoaded",()=>{const e=[{button:document.getElementById("toggle-lang-button"),menu:document.getElementById("lang-dropdown")},{button:document.getElementById("toggle-menu-button"),menu:document.getElementById("menu-dropdown")}].filter(e=>e.button&&e.menu),t=({button:e,menu:t})=>{t.classList.remove("display-menu"),e.ariaExpanded="false"};e.forEach(n=>{n.button.addEventListener("click",()=>{const a=n.menu.classList.contains("display-menu");e.forEach(t),a||(({button:e,menu:t})=>{t.classList.add("display-menu"),e.ariaExpanded="true"})(n)})}),document.addEventListener("click",n=>{e.forEach(e=>{!e.menu.classList.contains("display-menu")||e.button.contains(n.target)||e.menu.contains(n.target)||t(e)})}),document.addEventListener("focusout",n=>{const a=n.relatedTarget;a&&e.forEach(e=>{!e.menu.classList.contains("display-menu")||e.button.contains(a)||e.menu.contains(a)||t(e)})}),document.addEventListener("keydown",n=>{"Escape"===n.key&&e.forEach(e=>{e.menu.classList.contains("display-menu")&&(t(e),e.button.focus())})})}),document.addEventListener("DOMContentLoaded",()=>{const e=document.getElementById("toggle-dark-mode");if(!e)return;const t=e.querySelector("i"),n=document.getElementById("prism-theme-light"),a=document.getElementById("prism-theme-dark"),s=e=>{t&&(t.classList.toggle("fa-square-check",e),t.classList.toggle("fa-square",!e))},o=e=>{n&&(n.disabled=e),a&&(a.disabled=!e)},i=(t,{persist:n=!0}={})=>{document.documentElement.classList.toggle("dark-mode",t),e.setAttribute("aria-pressed",String(t)),s(t),o(t),n&&localStorage.setItem("theme",t?"dark":"light")},r=document.documentElement.classList.contains("dark-mode");e.setAttribute("aria-pressed",String(r)),s(r),o(r),e.addEventListener("click",()=>{const e=!document.documentElement.classList.contains("dark-mode");i(e)});const c=window.matchMedia("(prefers-color-scheme: dark)"),d=e=>{localStorage.getItem("theme")||i(e.matches,{persist:!1})};"function"==typeof c.addEventListener?c.addEventListener("change",d):"function"==typeof c.addListener&&c.addListener(d)});</script>

        
            <script src="https://securepubads.g.doubleclick.net/tag/js/gpt.js" crossorigin="anonymous" async=""></script>
        

        
        
    
        
            <script>
document.addEventListener('DOMContentLoaded', function() {
    var sidebar = document.querySelector('.sidebar');
    var isSideBarDisplayed = window.getComputedStyle(sidebar).display !== 'none';
    function prepareAdSlot(elementId) {
        // Get the element by ID
        const targetElement = document.getElementById(elementId);

        // Ensure the element exists before proceeding
        if (!targetElement) {
            console.error(`Element with ID ${elementId} not found`);
            return;
        }

        const parentElement = targetElement.parentElement;
        // Change the background color of the parent element

        if (parentElement) {
            console.log(elementId)

            if (elementId === 'gam-ad-bottom' ) {
                parentElement.style.backgroundColor = '#eeeef0';
                if(getComputedStyle(parentElement).visibility === 'hidden') {
                    parentElement.style.visibility = 'inherit'; 
                }
            }

            // Get the sibling elements
            const siblingElements = parentElement.children;

            for (let i = 0; i < siblingElements.length; i++) {
                const sibling = siblingElements[i];

                // Skip the element itself
                if (sibling === targetElement) continue;

                // Log the sibling or perform any other action
                console.log('Found sibling:', sibling);

                // Check visibility
                if(getComputedStyle(sibling).visibility === 'hidden') {
                    sibling.style.visibility = 'inherit'; 
                }

                // Check if display is 'none', then change it to 'block'
                if (getComputedStyle(sibling).display === 'none') {
                    sibling.style.display = 'block'; 
                }
            }
        } else {
            console.warn('No parent element found');
        }
    }

    
    window.googletag = window.googletag || {cmd: []};
    googletag.cmd.push(function() {

        if(isSideBarDisplayed){
            var sidebarHeight = sidebar.offsetHeight;
            var adTextSideBarHeight = 0;
            var sideBarAdContainert = 600 + 17;
        
            var styles = window.getComputedStyle(sidebar);
            var avaiableSideAdSpace = sidebarHeight - adTextSideBarHeight - parseFloat(styles.paddingTop) - parseFloat(styles.paddingBottom);
            var numSideElements = Math.floor(avaiableSideAdSpace / sideBarAdContainert);
            for (var i = 0; i < numSideElements; i++) {
                // container element
                var containerElement = document.createElement('div');
                containerElement.classList.add('ad-wrapper');

                //text element
                var textElement = document.createElement('div');
                textElement.classList.add('ad-text');
                textElement.innerText = localizedAdText;

                // ad element
                var adElement = document.createElement('div');
                var sideAdElementId = 'side-gam-ad-' + i;
                adElement.id = sideAdElementId;
                adElement.classList.add('side-bar-ad-slot');

                // finalize setup
                containerElement.appendChild(textElement);
                containerElement.appendChild(adElement);
                sidebar.appendChild(containerElement);
                googletag.defineSlot('/23075930536/post-side', [[292, 30], [240, 400], [300, 75], [216, 54], [250, 360], [300, 50], 'fluid', [300, 31], [120, 20], [300, 250], [120, 30], [180, 150], [200, 446], [168, 42], [200, 200], [160, 600], [120, 90], [125, 125], [240, 133], [120, 60], [1, 1], [120, 240], [220, 90], [216, 36], [250, 250], [168, 28], [234, 60], [120, 600], [300, 600], [88, 31], [300, 100]], sideAdElementId).addService(googletag.pubads());
            }
        }

        // Define bottom ad
        googletag.defineSlot('/23075930536/post-bottom', ['fluid'], 'gam-ad-bottom').addService(googletag.pubads());

        // Enable lazy loading with default settings.
        googletag.pubads().enableLazyLoad();

        googletag.pubads().addEventListener("slotRequested", (event) => {
            console.log(`Slot ${event.slot.getSlotElementId()} fetched`);
        });

        googletag.pubads().addEventListener("slotOnload", (event) => {
            const elementId = event.slot.getSlotElementId();
            prepareAdSlot(elementId);
            console.log(`Slot ${event.slot.getSlotElementId()} rendered`);
        });

        googletag.pubads().enableSingleRequest();
        googletag.enableServices();


        // Trigger lazy loading
        googletag.display('gam-ad-bottom');

    });
});
</script>

        
    


        
            <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-5D6RKKP');</script>

        

        
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    


        
        
        

        
        

        <link rel="icon" href="https://cdn.freecodecamp.org/universal/favicons/favicon.ico" type="image/png">
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/the-observer-design-pattern-handbook-event-driven-architecture-domain-driven-design-in-dart/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="Every application, at some point, has to deal with a fundamental challenge: something happens, and several other things need to react to it. A user logs in, and the app needs to save a token, cache th">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="The Observer Design Pattern Handbook: Event-Driven Architecture &amp; Domain-Driven Design in Dart">
    
        <meta property="og:description" content="Every application, at some point, has to deal with a fundamental challenge: something happens, and several other things need to react to it. A user logs in, and the app needs to save a token, cache th">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/the-observer-design-pattern-handbook-event-driven-architecture-domain-driven-design-in-dart/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/0621293d-e82e-4f24-bb6e-40dec481c7cd.png">
    <meta property="article:published_time" content="2026-07-16T22:20:44.327Z">
    <meta property="article:modified_time" content="2026-07-16T22:20:44.327Z">
    
        <meta property="article:tag" content="#Domain-Driven-Design">
    
        <meta property="article:tag" content="Dart">
    
        <meta property="article:tag" content="Mobile Development">
    
        <meta property="article:tag" content="Flutter">
    
        <meta property="article:tag" content="Observer Pattern">
    
        <meta property="article:tag" content="design patterns">
    
        <meta property="article:tag" content="behavioural patterns">
    
        <meta property="article:tag" content="Software Engineering">
    
        <meta property="article:tag" content="Riverpod">
    
        <meta property="article:tag" content="Clean Architecture">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="The Observer Design Pattern Handbook: Event-Driven Architecture &amp; Domain-Driven Design in Dart">
    
        <meta name="twitter:description" content="Every application, at some point, has to deal with a fundamental challenge: something happens, and several other things need to react to it. A user logs in, and the app needs to save a token, cache th">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/the-observer-design-pattern-handbook-event-driven-architecture-domain-driven-design-in-dart/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/0621293d-e82e-4f24-bb6e-40dec481c7cd.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Oluwaseyi Fatunmole">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="#Domain-Driven-Design, Dart, Mobile Development, Flutter, Observer Pattern, design patterns, behavioural patterns, Software Engineering, Riverpod, Clean Architecture">
    <meta name="twitter:site" content="@freecodecamp">
    
        <meta name="twitter:creator" content="@devseyi">
    

    <meta property="og:image:width" content="1920">
    <meta property="og:image:height" content="1080">


        
    <script type="application/ld+json">{
	"@context": "https://schema.org",
	"@type": "Article",
	"publisher": {
		"@type": "Organization",
		"name": "freeCodeCamp.org",
		"url": "https://www.freecodecamp.org/news/",
		"logo": {
			"@type": "ImageObject",
			"url": "https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg",
			"width": 2100,
			"height": 240
		}
	},
	"image": {
		"@type": "ImageObject",
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/0621293d-e82e-4f24-bb6e-40dec481c7cd.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/the-observer-design-pattern-handbook-event-driven-architecture-domain-driven-design-in-dart/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-16T22:20:44.327Z",
	"dateModified": "2026-07-16T22:20:44.327Z",
	"keywords": "Dart, Mobile Development, Flutter, Observer Pattern, design patterns, behavioural patterns, Software Engineering, Riverpod, Clean Architecture",
	"description": "Every application, at some point, has to deal with a fundamental challenge: something happens, and several other things need to react to it.\nA user logs in, and the app needs to save a token, cache th",
	"headline": "The Observer Design Pattern Handbook: Event-Driven Architecture &amp; Domain-Driven Design in Dart",
	"author": {
		"@type": "Person",
		"name": "Oluwaseyi Fatunmole",
		"url": "https://www.freecodecamp.org/news/author/foluwaseyi/",
		"sameAs": [
			"https://oluwaseyifatunmole.dev",
			"https://x.com/devseyi"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/uploads/avatars/692776609bbf6fdcde84192d/71ac313f-d9ed-4c0c-8990-e1b362645ecc.png",
			"width": 1302,
			"height": 1452
		}
	}
}</script>


        <meta name="generator" content="Eleventy">
        <link rel="alternate" type="application/rss+xml" title="freeCodeCamp.org" href="https://www.freecodecamp.org/news/rss/">

        
        

        
  <meta name="x-fcc-source" data-test-label="x-fcc-source" content="Hashnode">

    </head>

    
        <body class="home-template">
    

    
        <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5D6RKKP" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

    

        <div class="site-wrapper">
            <nav class="site-nav nav-padding universal-nav">
    <div class="site-nav-left">
        <div id="nav-left-search-container" class="fcc-search-container" data-test-label="fcc-search-container"></div>
    </div>
    <div class="site-nav-middle">
        <a class="site-nav-logo" href="https://www.freecodecamp.org/news/" data-test-label="site-nav-logo"><img src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg" alt="freeCodeCamp.org"></a>
    </div>
    <div class="site-nav-right">
        <button data-test-label="header-toggle-lang-button" id="toggle-lang-button" class="lang-button-nav" title="Change Language" aria-label="Change Language" aria-controls="lang-dropdown" aria-expanded="false">
             <svg aria-hidden="true" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg" data-test-label="globe-icon">
      <path d="M2 12C2 17.5228 6.47715 22 12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
      <path d="M13 2.04932C13 2.04932 16 5.99994 16 11.9999C16 17.9999 13 21.9506 13 21.9506" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
      <path d="M11 21.9506C11 21.9506 8 17.9999 8 11.9999C8 5.99994 11 2.04932 11 2.04932" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
      <path d="M2.62964 15.5H21.3704" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
      <path d="M2.62964 8.5H21.3704" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
    </svg>

        </button>
            <ul data-test-label="header-lang-list" id="lang-dropdown" class="nav-list" aria-labelledby="toggle-lang-button">
                
                    <li>
                        <a data-test-label="header-lang-list-option" class="nav-link nav-lang-list-option" href="https://www.freecodecamp.org/news/" hreflang="en" lang="en" aria-current="true">English</a>
                    </li>
                
                    <li>
                        <a data-test-label="header-lang-list-option" class="nav-link nav-lang-list-option" href="https://www.freecodecamp.org/espanol/news/" hreflang="es" lang="es">Español</a>
                    </li>
                
                    <li>
                        <a data-test-label="header-lang-list-option" class="nav-link nav-lang-list-option" href="https://www.freecodecamp.org/chinese/news/" hreflang="zh" lang="zh">中文（简体字）</a>
                    </li>
                
                    <li>
                        <a data-test-label="header-lang-list-option" class="nav-link nav-lang-list-option" href="https://www.freecodecamp.org/italian/news/" hreflang="it" lang="it">Italiano</a>
                    </li>
                
                    <li>
                        <a data-test-label="header-lang-list-option" class="nav-link nav-lang-list-option" href="https://www.freecodecamp.org/portuguese/news/" hreflang="pt-BR" lang="pt-BR">Português</a>
                    </li>
                
                    <li>
                        <a data-test-label="header-lang-list-option" class="nav-link nav-lang-list-option" href="https://www.freecodecamp.org/ukrainian/news/" hreflang="uk" lang="uk">Українська</a>
                    </li>
                
                    <li>
                        <a data-test-label="header-lang-list-option" class="nav-link nav-lang-list-option" href="https://www.freecodecamp.org/japanese/news/" hreflang="ja" lang="ja">日本語</a>
                    </li>
                
                    <li>
                        <a data-test-label="header-lang-list-option" class="nav-link nav-lang-list-option" href="https://www.freecodecamp.org/korean/news/" hreflang="ko" lang="ko">한국어</a>
                    </li>
                
            </ul>
        <button aria-expanded="false" class="menu-button-nav" id="toggle-menu-button" data-test-label="header-menu-button" aria-label="Menu" aria-controls="menu-dropdown">
            <span class="menu-btn-text">Menu</span>
            <i class="fa-solid fa-bars menu-btn-icon" aria-hidden="true"></i>
        </button>
        <ul id="menu-dropdown" class="nav-list" aria-labelledby="toggle-menu-button" data-test-label="header-menu">
            <li>
                <div id="nav-right-search-container" class="fcc-search-container" data-test-label="fcc-search-container"></div>
            </li>
            <li><a class="nav-link nav-link-flex" id="nav-forum" rel="noopener noreferrer" href="https://forum.freecodecamp.org/" target="_blank" data-test-label="forum-button">Forum</a></li>
            <li><a class="nav-link nav-link-flex" id="nav-learn" rel="noopener noreferrer" href="https://www.freecodecamp.org/learn" target="_blank" data-test-label="learn-button">Curriculum</a></li>
        <li><button class="nav-link nav-link-flex" id="toggle-dark-mode" aria-pressed="false" data-test-label="dark-mode-button">
        <span>Night Mode</span><i class="fa-regular fa-square-check" aria-hidden="true"></i></button></li>
        </ul>
        <a class="donate-button-nav" id="nav-donate" rel="noopener noreferrer" href="https://www.freecodecamp.org/donate/" target="_blank" data-test-label="donate-button">Donate</a>
    </div>
</nav>


            
            <a class="banner" id="banner" data-test-label="banner" rel="noopener noreferrer" target="_blank">
    <p id="banner-text"></p>
</a>


    
    <script>document.addEventListener("DOMContentLoaded",()=>{const e=document.getElementById("banner"),t=document.getElementById("banner-text");if(isAuthenticated){t.innerHTML=isDonor?"Thank you for supporting freeCodeCamp through <span>your donations</span>.":"Support our charity and our mission. <span>Donate to freeCodeCamp.org</span>.",e.href=isDonor?"https://www.freecodecamp.org/news/how-to-donate-to-free-code-camp/":"https://www.freecodecamp.org/donate";const o=isDonor?"donor":"authenticated";e.setAttribute("text-variation",o)}else t.innerHTML="Learn to code — <span>free 3,000-hour curriculum</span>",e.href="https://www.freecodecamp.org/",e.setAttribute("text-variation","default")});</script>


            <div id="error-message"></div>

            
    <main id="site-main" class="post-template site-main outer">
        <div class="inner ad-layout">
            <article class="post-full post">
                <header class="post-full-header">
                    <section class="post-full-meta">
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-16T22:20:44.327Z">
                            July 16, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/domain-driven-design/">
                                ##Domain-Driven-Design
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">The Observer Design Pattern Handbook: Event-Driven Architecture &amp; Domain-Driven Design in Dart</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/uploads/avatars/692776609bbf6fdcde84192d/71ac313f-d9ed-4c0c-8990-e1b362645ecc.png 60w" sizes="60px" src="https://cdn.hashnode.com/uploads/avatars/692776609bbf6fdcde84192d/71ac313f-d9ed-4c0c-8990-e1b362645ecc.png" class="author-profile-image" alt="Oluwaseyi Fatunmole" width="1302" height="1452" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/foluwaseyi/" data-test-label="profile-link">
                    
                        Oluwaseyi Fatunmole
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/0621293d-e82e-4f24-bb6e-40dec481c7cd.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/0621293d-e82e-4f24-bb6e-40dec481c7cd.png" alt="The Observer Design Pattern Handbook: Event-Driven Architecture &amp; Domain-Driven Design in Dart" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>Every application, at some point, has to deal with a fundamental challenge: something happens, and several other things need to react to it.</p>
<p>A user logs in, and the app needs to save a token, cache the user profile, fire an analytics event, and navigate to the home screen.</p>
<p>A payment is confirmed, and the inventory needs to update, the user needs a receipt, and the fulfillment system needs to kick off delivery.</p>
<p>A sensor reading changes, and three different UI panels need to reflect the new value simultaneously.</p>
<p>The naïve solution is to write all of that logic in one place. One function that does everything or one class that knows about everything.</p>
<p>This works at first. Then requirements change. A new reaction needs to be added. An existing one needs to be removed. A side effect starts failing and takes everything else down with it. The code becomes a wall of responsibilities that's impossible to test, painful to extend, and dangerous to touch.</p>
<p>The Observer Design Pattern exists to solve exactly this problem. It gives you a structured, production-grade way to say: when this event happens, notify everyone who cares, without the event source knowing who those people are.</p>
<p>In this handbook, you'll learn the Observer pattern from first principles. You'll see how it's implemented in Dart, understand how it connects to Event-Driven Architecture, and discover how it integrates cleanly with Domain-Driven Design and Riverpod in a real Flutter application.</p>
<p>By the end, you won't just understand the pattern. You'll know how to use it deliberately in production code.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-what-is-the-observer-design-pattern">What is the Observer Design Pattern?</a></p>
</li>
<li><p><a href="#heading-the-problem-it-solves">The Problem It Solves</a></p>
</li>
<li><p><a href="#heading-core-components">Core Components</a></p>
</li>
<li><p><a href="#heading-implementing-observer-in-dart">Implementing Observer in Dart</a></p>
</li>
<li><p><a href="#heading-a-real-world-example-the-login-flow">A Real-World Example: The Login Flow</a></p>
</li>
<li><p><a href="#heading-making-it-production-grade-with-a-generic-eventbus">Making It Production-Grade with a Generic EventBus</a></p>
</li>
<li><p><a href="#heading-observer-is-already-in-your-flutter-code">Observer Is Already in Your Flutter Code</a></p>
</li>
<li><p><a href="#heading-deep-dive-into-event-driven-architecture">Deep Dive Into Event-Driven Architecture</a></p>
</li>
<li><p><a href="#heading-application-in-domain-driven-design">Application in Domain-Driven Design</a></p>
</li>
<li><p><a href="#heading-the-riverpod-hybrid-clean-architecture-in-practice">The Riverpod Hybrid: Clean Architecture in Practice</a></p>
</li>
<li><p><a href="#heading-testing-the-observer-architecture">Testing the Observer Architecture</a></p>
</li>
<li><p><a href="#heading-when-to-use-the-observer-pattern">When to Use the Observer Pattern</a></p>
</li>
<li><p><a href="#heading-when-not-to-use-it">When Not to Use It</a></p>
</li>
<li><p><a href="#heading-conclusion">Conclusion</a></p>
</li>
</ul>
<h2 id="heading-what-is-the-observer-design-pattern">What is the Observer Design Pattern?</h2>
<p>The Observer pattern is a behavioural design pattern that defines a one-to-many dependency between objects. When one object changes state or fires an event, all of its dependents are notified and updated automatically.</p>
<p>Think of a newspaper subscription service. The newspaper publisher doesn't know who its individual subscribers are. It doesn't call each reader personally. It publishes the paper, and every subscriber who signed up receives it.</p>
<p>A subscriber can cancel at any time. A new subscriber can join at any time. The publisher's job never changes. It just publishes.</p>
<p>That's the Observer pattern in plain terms.</p>
<p>The publisher is called the <strong>Subject</strong>. The subscribers are called <strong>Observers</strong>. The newspaper is the <strong>event</strong>.</p>
<p>The pattern was formally defined in the Gang of Four book, Design Patterns: Elements of Reusable Object-Oriented Software. It remains one of the most widely used patterns in software engineering, especially in reactive and event-driven systems.</p>
<h2 id="heading-the-problem-it-solves">The Problem It Solves</h2>
<p>Let's look at what happens without the Observer pattern.</p>
<p>Say you have a login feature. When login succeeds, you need to do four things:</p>
<ul>
<li><p>Save the authentication token to secure storage</p>
</li>
<li><p>Cache the user profile data</p>
</li>
<li><p>Navigate to the home screen</p>
</li>
<li><p>Fire an analytics event</p>
</li>
</ul>
<p>The straightforward approach puts all of this inside the login function:</p>
<pre><code class="language-dart">Future&lt;void&gt; login(String email, String password) async {
  final response = await _authRepository.login(email, password);

  await _secureStorage.write(key: 'token', value: response.token);
  await _userCache.save(response.user);
  _navigationService.navigateTo('/home');
  _analytics.track('login_success', {'userId': response.user.id});
}
</code></pre>
<p>This looks fine at first glance. But count how many reasons this single function has to change:</p>
<ul>
<li><p>The token storage strategy changes. You modify this function.</p>
</li>
<li><p>The navigation destination changes. You modify this function.</p>
</li>
<li><p>The analytics event name or payload changes. You modify this function.</p>
</li>
<li><p>The user caching logic changes. You modify this function.</p>
</li>
</ul>
<p>Every single change to any of these four concerns forces you back into this one function. And every time you touch it, you risk breaking all the other three things it's doing.</p>
<p>Now imagine you need to add a fifth thing, such as enrolling the user in push notifications. You open this function again. You add more code. The function grows. Testing it requires mocking four, then five different dependencies. New teammates struggle to understand what this function is actually responsible for. The answer, of course, is everything. And that's the problem.</p>
<p>This is called tight coupling. The login logic is coupled to every single consequence of a successful login.</p>
<p>The Observer pattern breaks these couplings completely. The login logic does one thing: it performs the login and announces the result. Every consequence is handled by a separate, independent observer. Each observer has one job. None of them know about each other. The login logic doesn't know they exist.</p>
<h2 id="heading-core-components">Core Components</h2>
<p>The Observer pattern has four core building blocks. Understanding each one before writing code makes the implementation much easier to follow.</p>
<h3 id="heading-subject">Subject</h3>
<p>The Subject is the object that something happens to. It holds a list of observers and is responsible for notifying them when an event occurs. It exposes methods for observers to register and unregister themselves. The Subject doesn't care what observers do with the notification. It just delivers it.</p>
<h3 id="heading-observer">Observer</h3>
<p>The Observer is an interface or abstract class that defines the contract all observers must follow. It declares the method or methods the Subject will call when notifying. Any class that wants to react to an event must implement this interface.</p>
<h3 id="heading-concrete-subject">Concrete Subject</h3>
<p>The Concrete Subject is the real implementation of the Subject. It manages the actual list of observers, handles subscriptions, and fires notifications at the right moment.</p>
<h3 id="heading-concrete-observers">Concrete Observers</h3>
<p>These are the real classes that implement the Observer interface. Each one has a specific, focused job to do when notified. One saves the token. One navigates. One fires analytics. They don't know about each other and don't need to.</p>
<p>Here's how they relate to each other:</p>
<pre><code class="language-cpp">Subject (LoginService)
    |
    |-- subscribe(observer)    &lt;- observer registers itself
    |-- unsubscribe(observer)  &lt;- observer removes itself
    |-- notifySuccess(data)    &lt;- fires when login succeeds
    |-- notifyFailure(error)   &lt;- fires when login fails
         |
         |-----&gt; TokenObserver.onLoginSuccess()
         |-----&gt; UserObserver.onLoginSuccess()
         |-----&gt; NavigationObserver.onLoginSuccess()
         |-----&gt; AnalyticsObserver.onLoginSuccess()
</code></pre>
<p>The Subject notifies all of them. They each handle their own job independently.</p>
<h2 id="heading-implementing-observer-in-dart">Implementing Observer in Dart</h2>
<p>Let's build the pattern step by step.</p>
<h3 id="heading-step-1-define-the-observer-interface">Step 1: Define the Observer Interface</h3>
<pre><code class="language-dart">abstract class LoginObserver {
  void onLoginSuccess(UserDto user);
  void onLoginFailed(AppException error);
}
</code></pre>
<p>This is the contract that every observer must sign. Any class that wants to react to login events must implement both of these methods.</p>
<p><code>onLoginSuccess</code> is called when the login succeeds and receives the user data. <code>onLoginFailed</code> is called when the login fails and receives the error.</p>
<h3 id="heading-step-2-define-the-subject-interface">Step 2: Define the Subject Interface</h3>
<pre><code class="language-dart">abstract class LoginSubject {
  void subscribe(LoginObserver observer);
  void unsubscribe(LoginObserver observer);
  void notifySuccess(UserDto user);
  void notifyFailure(AppException error);
}
</code></pre>
<p><code>subscribe</code> lets an observer join the notification list. <code>unsubscribe</code> lets an observer leave the notification list. <code>notifySuccess</code> broadcasts a success event with the user data to all registered observers. <code>notifyFailure</code> broadcasts a failure event with the error to all registered observers.</p>
<p>Defining this as an abstract class instead of going straight to a concrete class is important. It means anything that depends on the subject depends on the abstraction, not the implementation. This makes your code testable and swappable.</p>
<h3 id="heading-step-3-implement-the-concrete-subject">Step 3: Implement the Concrete Subject</h3>
<pre><code class="language-dart">class LoginService implements LoginSubject {
  final List&lt;LoginObserver&gt; _observers = [];

  @override
  void subscribe(LoginObserver observer) {
    _observers.add(observer);
  }

  @override
  void unsubscribe(LoginObserver observer) {
    _observers.remove(observer);
  }

  @override
  void notifySuccess(UserDto user) {
    for (final observer in List.of(_observers)) {
      try {
        observer.onLoginSuccess(user);
      } catch (e) {
        debugPrint('Observer error on success: $e');
      }
    }
  }

  @override
  void notifyFailure(AppException error) {
    for (final observer in List.of(_observers)) {
      try {
        observer.onLoginFailed(error);
      } catch (e) {
        debugPrint('Observer error on failure: $e');
      }
    }
  }
}
</code></pre>
<p>There are two important decisions in this implementation that are easy to miss.</p>
<h4 id="heading-1-snapshot-iteration-with-listof">1. Snapshot iteration with <code>List.of()</code></h4>
<p>Instead of iterating directly over <code>_observers</code>, we iterate over <code>List.of(_observers)</code>, which creates a copy of the list before the loop runs.</p>
<p>Why does this matter? Imagine a <code>NavigationObserver</code> that, after navigating to the home screen, unsubscribes itself because it no longer needs to listen. If it calls <code>unsubscribe</code> while the <code>notifySuccess</code> loop is still running over the same list, Dart throws a <code>ConcurrentModificationError</code>. The list is being modified while it's being read.</p>
<p><code>List.of()</code> prevents this entirely. The loop runs over the snapshot. The original list can be modified freely during iteration without any errors.</p>
<h4 id="heading-2-per-observer-trycatch">2. Per-observer try/catch</h4>
<p>Each observer call is wrapped in its own try/catch block. This is a deliberate choice. If <code>TokenObserver</code> throws an exception while writing to secure storage, you don't want <code>NavigationObserver</code> and <code>AnalyticsObserver</code> to silently never fire. Each observer gets its chance to run regardless of what the others do.</p>
<p>Without this, one failing observer would stop the entire notification chain. That's a hidden bug that's extremely difficult to trace in production.</p>
<h2 id="heading-a-real-world-example-the-login-flow">A Real-World Example: The Login Flow</h2>
<p>Now let's build the full login flow using this foundation.</p>
<h3 id="heading-the-login-logic">The Login Logic</h3>
<pre><code class="language-cpp">class LoginLogic {
  final LoginSubject _subject;
  final AuthRepository _repository;

  LoginLogic({
    required LoginSubject subject,
    required AuthRepository repository,
  })  : _subject = subject,
        _repository = repository;

  Future&lt;void&gt; callLogin(LoginRequest request) async {
    try {
      final user = await _repository.login(request);
      _subject.notifySuccess(user);
    } on AppException catch (e) {
      _subject.notifyFailure(e);
    } catch (e) {
      _subject.notifyFailure(AppException.unknown(message: e.toString()));
    }
  }
}
</code></pre>
<p>Let's walk through this carefully.</p>
<p><code>LoginLogic</code> takes two dependencies through its constructor: a <code>LoginSubject</code> and an <code>AuthRepository</code>. Notice it takes <code>LoginSubject</code>, the abstraction, not <code>LoginService</code>, the concrete class. This means you can swap the implementation in tests or in different environments without changing <code>LoginLogic</code> at all.</p>
<p>Inside <code>callLogin</code>, the logic is straightforward. It calls the repository to perform the actual login. If that succeeds, it calls <code>notifySuccess</code> on the subject with the returned user. If it throws an <code>AppException</code>, it calls <code>notifyFailure</code> with that error. If it throws anything unexpected, it wraps it in an <code>AppException.unknown</code> and notifies failure.</p>
<p>Notice what <code>LoginLogic</code> does NOT do. It doesn't save a token. It doesn't navigate anywhere. It doesn't cache anything. It doesn't fire analytics. And it doesn't know how many observers exist or what they do.</p>
<p>Its entire responsibility is: perform the login, announce the result.</p>
<h3 id="heading-the-concrete-observers">The Concrete Observers</h3>
<pre><code class="language-cpp">class TokenObserver implements LoginObserver {
  final SecureStorageService _storage;

  TokenObserver(this._storage);

  @override
  void onLoginSuccess(UserDto user) {
    _storage.write(key: 'auth_token', value: user.token);
  }

  @override
  void onLoginFailed(AppException error) {
    _storage.delete(key: 'auth_token');
  }
}
</code></pre>
<p><code>TokenObserver</code> has one job: manage the authentication token. On success, it saves the token. On failure, it clears any stale token that might be sitting in storage. It knows nothing about navigation, caching, or analytics.</p>
<pre><code class="language-cpp">class UserObserver implements LoginObserver {
  final UserCacheService _cache;

  UserObserver(this._cache);

  @override
  void onLoginSuccess(UserDto user) {
    _cache.save(user);
  }

  @override
  void onLoginFailed(AppException error) {
    _cache.clear();
  }
}
</code></pre>
<p><code>UserObserver</code> has one job: manage the user cache. On success, it saves the user profile. On failure, it clears the cache. It knows nothing about tokens, navigation, or analytics.</p>
<pre><code class="language-cpp">class NavigationObserver implements LoginObserver {
  final NavigationService _navigation;

  NavigationObserver(this._navigation);

  @override
  void onLoginSuccess(UserDto user) {
    _navigation.navigateTo('/home');
  }

  @override
  void onLoginFailed(AppException error) {
    _navigation.showError(error.message);
  }
}
</code></pre>
<p><code>NavigationObserver</code> has one job: handle navigation after a login attempt. It uses an injected <code>NavigationService</code> abstraction rather than a <code>BuildContext</code>. This is intentional. An observer that depends on <code>BuildContext</code> is tied to the widget lifecycle. Using an abstraction keeps this observer completely independent of the UI layer.</p>
<pre><code class="language-cpp">class AnalyticsObserver implements LoginObserver {
  final AnalyticsService _analytics;

  AnalyticsObserver(this._analytics);

  @override
  void onLoginSuccess(UserDto user) {
    _analytics.track('login_success', {'userId': user.id});
  }

  @override
  void onLoginFailed(AppException error) {
    _analytics.track('login_failed', {'reason': error.message});
  }
}
</code></pre>
<p><code>AnalyticsObserver</code> has one job: fire the right analytics event for each outcome. It has no knowledge of storage, navigation, or caching.</p>
<p>Each observer has exactly one responsibility. Each one has exactly one reason to change. When the analytics payload needs to change, you touch only <code>AnalyticsObserver</code>. When navigation logic changes, you touch only <code>NavigationObserver</code>. Nothing else is affected.</p>
<h3 id="heading-wiring-it-together">Wiring It Together</h3>
<pre><code class="language-cpp">void setupLogin() {
  final service = LoginService();

  service
    ..subscribe(TokenObserver(secureStorage))
    ..subscribe(UserObserver(userCache))
    ..subscribe(NavigationObserver(navigationService))
    ..subscribe(AnalyticsObserver(analyticsService));

  final loginLogic = LoginLogic(
    subject: service,
    repository: authRepository,
  );
}
</code></pre>
<p>This is the composition step. All observers are created with their dependencies and registered onto the service. The cascade operator <code>..</code> calls <code>subscribe</code> multiple times on the same <code>service</code> object, which keeps the setup readable.</p>
<p><code>LoginLogic</code> receives the <code>service</code> as its <code>LoginSubject</code>. From this point forward, every time <code>callLogin</code> is called and an outcome occurs, all four observers are notified automatically.</p>
<p>Adding a fifth observer, say a <code>PushNotificationObserver</code>, means creating the class and adding one line here: <code>..subscribe(PushNotificationObserver(pushService))</code>. Nothing else in the entire codebase changes.</p>
<h2 id="heading-making-it-production-grade-with-a-generic-eventbus">Making It Production-Grade with a Generic EventBus</h2>
<p>The login example above works well, but it's specific to login. In a real application, many features have the same fan-out requirement. Payment confirmed, order placed, profile updated, session expired. All of them need one event to trigger multiple independent reactions.</p>
<p>Rewriting the Subject and Observer interfaces per feature is repetitive and unnecessary. The better approach is a generic <code>EventBus</code> that any feature can use.</p>
<pre><code class="language-cpp">abstract class DomainObserver&lt;T&gt; {
  void onSuccess(T data);
  void onFailure(AppEx