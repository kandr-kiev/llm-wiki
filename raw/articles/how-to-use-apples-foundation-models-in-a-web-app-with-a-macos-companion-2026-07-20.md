---
source_url: https://www.freecodecamp.org/news/how-to-use-apple-s-foundation-models-in-a-web-app-with-a-macos-companion/
ingested: 2026-07-20
sha256: 302880ac2cc595ff1e7609f7154e5d95f7ed06b59a5af7e7e1ce4b97e6f6e63c
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Use Apple’s Foundation Models in a Web App with a macOS Companion</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-to-use-apple-s-foundation-models-in-a-web-app-with-a-macos-companion/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="Not every AI feature needs a cloud model, with its per-token bills, network round-trips, and private data leaving your machine. If you&#39;re on a modern Mac, a capable language model is already on your d">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Use Apple’s Foundation Models in a Web App with a macOS Companion">
    
        <meta property="og:description" content="Not every AI feature needs a cloud model, with its per-token bills, network round-trips, and private data leaving your machine. If you&#39;re on a modern Mac, a capable language model is already on your d">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-to-use-apple-s-foundation-models-in-a-web-app-with-a-macos-companion/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/7f0e2343-7394-46b5-a4c8-3ef0fecfa57a.png">
    <meta property="article:published_time" content="2026-07-20T21:27:11.624Z">
    <meta property="article:modified_time" content="2026-07-20T21:27:11.624Z">
    
        <meta property="article:tag" content="software development">
    
        <meta property="article:tag" content="AI">
    
        <meta property="article:tag" content="macOS">
    
        <meta property="article:tag" content="React">
    
        <meta property="article:tag" content="Swift">
    
        <meta property="article:tag" content="JavaScript">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Use Apple’s Foundation Models in a Web App with a macOS Companion">
    
        <meta name="twitter:description" content="Not every AI feature needs a cloud model, with its per-token bills, network round-trips, and private data leaving your machine. If you&#39;re on a modern Mac, a capable language model is already on your d">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-to-use-apple-s-foundation-models-in-a-web-app-with-a-macos-companion/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/7f0e2343-7394-46b5-a4c8-3ef0fecfa57a.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Balogun Wahab">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="software development, AI, macOS, React, Swift, JavaScript">
    <meta name="twitter:site" content="@freecodecamp">
    
        <meta name="twitter:creator" content="@03balogun">
    

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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/7f0e2343-7394-46b5-a4c8-3ef0fecfa57a.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-to-use-apple-s-foundation-models-in-a-web-app-with-a-macos-companion/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-20T21:27:11.624Z",
	"dateModified": "2026-07-20T21:27:11.624Z",
	"keywords": "software development, AI, macOS, React, Swift, JavaScript",
	"description": "Not every AI feature needs a cloud model, with its per-token bills, network round-trips, and private data leaving your machine. If you&#x27;re on a modern Mac, a capable language model is already on your d",
	"headline": "How to Use Apple’s Foundation Models in a Web App with a macOS Companion",
	"author": {
		"@type": "Person",
		"name": "Balogun Wahab",
		"url": "https://www.freecodecamp.org/news/author/03balogun/",
		"sameAs": [
			"https://x.com/03balogun"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/res/hashnode/image/upload/v1763399420451/2a853a45-3f5a-4a93-ac27-717df966bb13.jpeg?w=500&h=500&fit=crop&crop=entropy&auto=compress,format&format=webp",
			"width": 2914,
			"height": 2700
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-20T21:27:11.624Z">
                            July 20, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/software-development/">
                                #software development
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Use Apple’s Foundation Models in a Web App with a macOS Companion</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/res/hashnode/image/upload/v1763399420451/2a853a45-3f5a-4a93-ac27-717df966bb13.jpeg?w=500&h=500&fit=crop&crop=entropy&auto=compress,format&format=webp 60w" sizes="60px" src="https://cdn.hashnode.com/res/hashnode/image/upload/v1763399420451/2a853a45-3f5a-4a93-ac27-717df966bb13.jpeg?w=500&h=500&fit=crop&crop=entropy&auto=compress,format&format=webp" class="author-profile-image" alt="Balogun Wahab" width="2914" height="2700" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/03balogun/" data-test-label="profile-link">
                    
                        Balogun Wahab
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/7f0e2343-7394-46b5-a4c8-3ef0fecfa57a.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/7f0e2343-7394-46b5-a4c8-3ef0fecfa57a.png" alt="How to Use Apple’s Foundation Models in a Web App with a macOS Companion" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>Not every AI feature needs a cloud model, with its per-token bills, network round-trips, and private data leaving your machine. If you're on a modern Mac, a capable language model is already on your disk.</p>
<p><strong>Foundation Models</strong> is Apple's Swift framework for working with large language models. It's the on-device model behind Apple Intelligence, Apple's Private Cloud Compute, or another provider's server model.</p>
<p>This tutorial targets the on-device model: you send it a prompt and it runs entirely on the Mac's own hardware locally, free-per-call, and offline-friendly.</p>
<p>Paired with Apple Vision for reading images on device, that's enough to build real AI features like summaries, classification, and structured extraction without the data ever leaving your machine.</p>
<h2 id="heading-table-of-contents">Table Of Contents</h2>
<ul>
<li><p><a href="#heading-what-you-will-build">What You Will Build</a></p>
</li>
<li><p><a href="#heading-prerequisites">Prerequisites</a></p>
</li>
<li><p><a href="#heading-why-a-macos-companion-app">Why a macOS Companion App?</a></p>
</li>
<li><p><a href="#heading-foundation-models-cant-read-images-directly">Foundation Models Can't Read Images Directly</a></p>
</li>
<li><p><a href="#heading-project-structure">Project Structure</a></p>
</li>
<li><p><a href="#heading-build-the-react-app">Build the React App</a></p>
<ul>
<li><p><a href="#heading-check-companion-health">Check Companion Health</a></p>
</li>
<li><p><a href="#heading-convert-the-image-to-base64">Convert the Image to Base64</a></p>
</li>
<li><p><a href="#heading-analyze-immediately-after-upload">Analyze Immediately After Upload</a></p>
</li>
<li><p><a href="#heading-send-the-image-to-the-companion">Send the Image to the Companion</a></p>
</li>
<li><p><a href="#heading-render-the-json-output">Render the JSON Output</a></p>
</li>
</ul>
</li>
<li><p><a href="#heading-build-the-macos-companion-app">Build the macOS Companion App</a></p>
</li>
<li><p><a href="#heading-check-foundation-models-availability">Check Foundation Models Availability</a></p>
</li>
<li><p><a href="#heading-extract-text-with-apple-vision">Extract Text with Apple Vision</a></p>
</li>
<li><p><a href="#heading-ask-foundation-models-to-explain-the-vision-output">Ask Foundation Models to Explain the Vision Output</a></p>
</li>
<li><p><a href="#heading-return-json-to-the-browser">Return JSON to the Browser</a></p>
</li>
<li><p><a href="#heading-run-the-app">Run the App</a></p>
</li>
<li><p><a href="#heading-conclusion">Conclusion</a></p>
</li>
<li><p><a href="#heading-resources">Resources</a></p>
</li>
</ul>
<h2 id="heading-what-you-will-build">What You Will Build</h2>
<p>You'll build <strong>Vision Bridge</strong>, a web app that sends an image to a local macOS companion. The companion reads the image with Apple Vision, reasons about it with Foundation Models, and returns structured JSON to the browser: private, on-device AI behind a plain web interface.</p>
<p>You can find the complete source code in this GitHub repository: <a href="http://github.com/03balogun/vision-bridge">github.com/03balogun/vision-bridge</a>.</p>
<p>The goal isn't to build a giant product but rather to understand the architecture behind how this works.</p>
<img src="https://cdn.hashnode.com/uploads/covers/5db93b3da2342e8354088115/6d18db01-e921-4291-bb2e-26be2c02b304.png" alt="Screenshot of the Vision Bridge app, with image upload on the left and JSON output on the right" style="display:block;margin:0 auto" width="3024" height="1714" loading="lazy">

<p>Vision Bridge has two parts:</p>
<ul>
<li><p>A React app with a split-screen interface.</p>
</li>
<li><p>A macOS companion app that exposes a local API.</p>
</li>
</ul>
<p>The React app has:</p>
<ul>
<li><p>An image upload area</p>
</li>
<li><p>An image preview</p>
</li>
<li><p>Automatic analysis after upload</p>
</li>
<li><p>A JSON output viewer</p>
</li>
<li><p>A companion health status indicator</p>
</li>
</ul>
<p>The macOS companion app has:</p>
<ul>
<li><p><code>GET /v1/health</code></p>
</li>
<li><p><code>POST /v1/analyze-image</code></p>
</li>
<li><p>Apple Vision OCR</p>
</li>
<li><p>Foundation Models availability checks</p>
</li>
<li><p>Foundation Models reasoning over Vision output</p>
</li>
</ul>
<p>The final response looks like this:</p>
<pre><code class="language-json">{
  "support": {
    "visionAvailable": true,
    "foundationModelAvailable": true,
    "foundationModelStatus": "available"
  },
  "image": {
    "filename": "screenshot.png",
    "contentType": "image/png",
    "byteCount": 1048576,
    "width": 1440,
    "height": 900
  },
  "vision": {
    "detectedText": [
      {
        "text": "Build failed",
        "confidence": 0.96,
        "boundingBox": {
          "x": 0.12,
          "y": 0.31,
          "width": 0.45,
          "height": 0.08
        }
      }
    ]
  },
  "model": {
    "summary": "The image appears to show a software build failure.",
    "description": "A developer tool window is showing an error state with diagnostic text.",
    "suggestedTags": ["screenshot", "developer-tool", "error"],
    "possibleUses": [
      "Generate alt text",
      "Summarize screenshots",
      "Extract document data"
    ]
  }
}
</code></pre>
<h2 id="heading-prerequisites">Prerequisites</h2>
<p>To follow along, you need:</p>
<ul>
<li><p>macOS 26 or newer</p>
</li>
<li><p>Xcode with the macOS 26 SDK</p>
</li>
<li><p>Node.js 20 or newer</p>
</li>
<li><p>Basic React knowledge</p>
</li>
<li><p>Basic Swift knowledge</p>
</li>
<li><p>A Mac that supports Apple Intelligence</p>
</li>
</ul>
<p>Foundation Models availability depends on the Mac, the OS version, and Apple Intelligence settings. The companion checks this at runtime, which we'll cover below.</p>
<h2 id="heading-why-a-macos-companion-app">Why a macOS Companion App?</h2>
<p>You can't write this in a regular React app:</p>
<pre><code class="language-ts">import FoundationModels from "apple-frameworks";
</code></pre>
<p>That API doesn't exist in the browser. A native macOS app, however, can use any Apple framework, so the companion acts as a local bridge. The same pattern works for any native capability the web platform doesn't expose.</p>
<h2 id="heading-foundation-models-cant-read-images-directly">Foundation Models Can't Read Images Directly</h2>
<p>The public Foundation Models framework is a language model interface. It doesn't currently expose direct image input the way a multimodal cloud model might, so this tutorial never sends the image to the model. Instead, the companion feeds the Vision OCR observations and image metadata into the prompt. The model reasons over structured text, never the original pixels.</p>
<p>That split plays to each framework's strength: Vision is excellent at pulling machine-readable information out of images, and Foundation Models turns that information into summaries, labels, explanations, and structured output.</p>
<img src="https://cdn.hashnode.com/uploads/covers/5db93b3da2342e8354088115/a5c11ad4-dcac-4690-bc6d-08b27fd6fed8.png" alt="Vision Bridge architecture: the browser sends the image over localhost to the Swift companion, which runs Apple Vision OCR, feeds the observations to Foundation Models, and returns structured JSON" style="display:block;margin:0 auto" width="2492" height="1572" loading="lazy">

<p>The above diagram shows the round trip that the rest of this tutorial builds. The browser sends the uploaded image as base64 JSON over localhost to the Swift companion. Inside the companion, Apple Vision runs OCR on the image and produces text observations: the recognized strings, their confidence scores, and their bounding boxes.</p>
<p>Those observations, not the image itself, are formatted into a prompt for Foundation Models, which generates a summary, description, and tags. The companion then bundles the Vision output and the model output into one JSON response and returns it to the browser.</p>
<h2 id="heading-project-structure">Project Structure</h2>
<p>Create a project with this structure:</p>
<pre><code class="language-text">vision-bridge/
  apps/
    web/
      src/
        main.tsx
        styles.css
      package.json
      vite.config.ts
    macos-companion/
      Package.swift
      Sources/
        VisionBridgeCompanion/
          main.swift
  package.json
  README.md
</code></pre>
<p>The root <code>package.json</code> gives us a few convenient commands:</p>
<pre><code class="language-json">{
  "scripts": {
    "dev": "npm --workspace apps/web run dev",
    "build": "npm --workspace apps/web run build",
    "companion": "swift run --package-path apps/macos-companion VisionBridgeCompanion"
  },
  "workspaces": ["apps/web"]
}
</code></pre>
<h2 id="heading-build-the-react-app">Build the React App</h2>
<p>The web app is intentionally simple. It has one job: let the user pick an image and show the JSON returned by the companion.</p>
<p>The web app uses Vite, React, Lucide icons, and a JSON viewer:</p>
<pre><code class="language-json">{
  "dependencies": {
    "@vitejs/plugin-react": "^6.0.3",
    "lucide-react": "^0.468.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-json-view-lite": "^2.5.0",
    "vite": "^8.1.3"
  }
}
</code></pre>
<p>After defining the dependencies, install them:</p>
<pre><code class="language-plaintext">npm install
</code></pre>
<p>The API base URL points to the local companion:</p>
<pre><code class="language-ts">const API_BASE_URL = "http://127.0.0.1:43119";
</code></pre>
<h3 id="heading-check-companion-health">Check Companion Health</h3>
<p>The web app pings the companion so the UI can show whether the native bridge is online:</p>
<pre><code class="language-ts">async function checkHealth() {
  setHealthError(null);

  try {
    const response = await fetch(`${API_BASE_URL}/v1/health`);
    if (!response.ok) {
      throw new Error(`Health check failed with ${response.status}`);
    }

    const payload = await response.json();
    setHealth(payload);
  } catch (error) {
    setHealth(null);
    setHealthError(error instanceof Error ? error.message : "Companion unavailable");
  }
}
</code></pre>
<img src="https://cdn.hashnode.com/uploads/covers/5db93b3da2342e8354088115/dc3c37eb-1d9c-4b44-82db-f38adada4f19.png" alt="Screenshot of the companion online status pill" style="display:block;margin:0 auto" width="732" height="212" loading="lazy">

<h3 id="heading-convert-the-image-to-base64">Convert the Image to Base64</h3>
<p>When the user selects a file, the app converts it to base64 so it can be sent as JSON:</p>
<pre><code class="language-ts">function readFileAsBase64(file: File) {
  return new Promise&lt;string&gt;((resolve, reject) =&gt; {
    const reader = new FileReader();
    reader.onload = () =&gt; {
      const result = String(reader.result);
      resolve(result.includes(",") ? result.split(",")[1] : result);
    };
    reader.onerror = () =&gt; reject(reader.error);
    reader.readAsDataURL(file);
  });
}
</code></pre>
<p>This isn't the only way to upload files. You could also use <code>multipart/form-data</code>, but JSON keeps the demo easy to inspect.</p>
<h3 id="heading-analyze-immediately-after-upload">Analyze Immediately After Upload</h3>
<p>The app starts analysis as soon as an image is uploaded:</p>
<pre><code class="language-ts">async function handleFile(file: File) {
  if (!file.type.startsWith("image/")) {
    setError("Choose a PNG, JPEG, HEIC, or another browser-readable image.");
    return;
  }

  const base64 = await readFileAsBase64(file);
  const nextImage = {
    file,
    previewUrl: URL.createObjectURL(file),
    base64,
  };

  setSelectedImage(nextImage);
  setAnalysis(null);
  setError(null);
  setCopied(false);

  analyzeImage(nextImage);
}
</code></pre>
<p><code>handleFile</code> does the preparation work for every new image. It rejects anything that isn't a browser-readable image, converts the file to base64, and builds a single object holding everything the rest of the flow needs: the original <code>File</code> (for its name and MIME type), an object URL for the preview, and the base64 payload for the API call.</p>
<p>It then clears out the previous run the old analysis, any error message, and the "copied" indicator so the UI never shows results from the last image next to a new one. Finally, it kicks off <code>analyzeImage(nextImage)</code> immediately.</p>
<p>Note that it passes the fresh object directly instead of relying on the <code>selectedImage</code> state: React state updates don't apply until the next render, so reading the state here would still give you the <em>previous</em> image.</p>
<p>The <code>Analyze</code> button still exists in the UI, but it works as a manual rerun button.</p>
<h3 id="heading-send-the-image-to-the-companion">Send the Image to the Companion</h3>
<p>Here's the core request:</p>
<pre><code class="language-ts">const analysisRequestId = useRef(0);

async function analyzeImage(image = selectedImage) {
  if (!image) {
    setError("Choose an image first.");
    return;
  }

  const requestId = analysisRequestId.current + 1;
  analysisRequestId.current = requestId;

  setRequestState("loading");
  setError(null);
  setCopied(false);

  try {
    const response = await fetch(`${API_BASE_URL}/v1/analyze-image`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        filename: image.file.name,
        mimeType: image.file.type || "application/octet-stream",
        base64: image.base64,
      }),
    });

    const payload = await response.json();

    if (requestId !== analysisRequestId.current) {
      return;
    }

    if (!response.ok) {
      throw new Error(payload.error?.message ?? `Analysis failed with ${response.status}`);
    }

    setAnalysis(payload);
    setRequestState("success");
  } catch (error) {
    if (requestId !== analysisRequestId.current) {
      return;
    }

    setRequestState("error");
    setError(error instanceof Error ? error.message : "Could not analyze image");
  }
}
</code></pre>
<p>This function is the entire client side of the bridge. It flips <code>requestState</code> to <code>loading</code> (which drives the spinner and disables the button), then sends a <code>POST</code> to <code>/v1/analyze-image</code> with a JSON body containing three fields: the filename, the MIME type, and the base64 image data. That body maps one-to-one onto the <code>AnalyzeImageRequest</code> struct the Swift companion decodes later.</p>
<p>Notice that the response is parsed as JSON <em>before</em> checking <code>response.ok</code>. That's deliberate: when the companion rejects a request (bad base64, oversized image), it still returns a JSON body with an <code>error.message</code> field, so the UI can show the companion's own explanation instead of a generic status code. On success, the payload goes straight into state, and the JSON viewer re-renders with the result.</p>
<p>The <code>requestId</code> bookkeeping guards against stale responses. If a user uploads a second image while the first is still analyzing, whichever request finishes <em>last</em> would win, and OCR plus model generation takes long enough that responses can genuinely arrive out of order. So every call increments a counter stored in a ref and remembers its own ID.</p>
<p>After the <code>await</code>, it checks whether it's still the newest request; if a newer upload started in the meantime, the older response is silently discarded instead of overwriting the latest image's result. The same check runs in the <code>catch</code> block, so an old failure can't clobber a newer success either. If you also want to cancel the in-flight HTTP request rather than just ignore its result, an <code>AbortController</code> is the natural next step.</p>
<h3 id="heading-render-the-json-output">Render the JSON Output</h3>
<p>The output pane uses <code>react-json-view-lite</code>:</p>
<pre><code class="language-tsx">&lt;JsonView
  data={jsonData}
  shouldExpandNode={allExpanded}
  style={jsonViewTheme}
/&gt;
</code></pre>
<h2 id="heading-build-the-macos-companion-app">Build the macOS Companion App</h2>
<p>The companion is a Swift command-line app. It exposes a small local HTTP API.</p>
<p>If you come from the web side, the mapping is simple: Swift Package Manager is Swift's npm, <code>Package.swift</code> is its <code>package.json</code>, and <code>swift run</code> is its <code>npm start</code>. It ships with Xcode, so there's nothing extra to install.</p>
<p>The <code>Package.swift</code> file looks like this:</p>
<pre><code class="language-swift">// swift-tools-version: 6.0

import PackageDescription

let package = Package(
    name: "VisionBridgeCompanion",
    platforms: [
        .macOS("26.0")
    ],
    products: [
        .executable(
            name: "VisionBridgeCompanion",
            targets: ["VisionBridgeCompanion"]
        )
    ],
    targets: [
        .executableTarget(
            name: "VisionBridgeCompanion"
        )
    ]
)
</code></pre>
<p>The companion imports the Apple frameworks it needs:</p>
<pre><code class="language-swift">import Foundation
import FoundationModels
import ImageIO
import Network
import Vision
</code></pre>
<p>It listens on <code>127.0.0.1:43119</code>:</p>
<pre><code class="language-swift">private let defaultPort: UInt16 = 43119
</code></pre>
<p>The app exposes two routes:</p>
<pre><code class="language-swift">switch (request.method, request.path) {
case ("GET", "/v1/health"):
    let health = HealthResponse(support: ModelSupport.current)
    return try json(health)

case ("POST", "/v1/analyze-image"):
    let payload = try JSONDecoder().decode(AnalyzeImageRequest.self, from: request.body)
    let response = try await service.analyze(payload)
    return try json(response)

default:
    return try json(
        ErrorResponse(error: APIErrorPayload(message: "Route not found")),
        status: .notFound
    )
}
</code></pre>
<p>This <code>switch</code> is the companion's entire routing layer — no web framework, just pattern matching on the method and path.</p>
<p>The two routes split the work cleanly:</p>
<ul>
<li><p><code>GET /v1/health</code> is the cheap, read-only route. It runs no analysis, it just reports whether Vision and Foundation Models are usable on this Mac via <code>ModelSupport.current</code> (covered in the next section). The React app calls it on load to render the online/offline status pill, so the user knows the bridge is up before they upload anything.</p>
</li>
<li><p><code>POST /v1/analyze-image</code> is where the real work happens. It decodes the request body into an <code>AnalyzeImageRequest</code> (with the same <code>filename</code>, <code>mimeType</code>, and <code>base64</code> fields the browser sent) and hands it to the analysis service. This validates the image, runs Vision OCR, prompts Foundation Models, and returns the combined result. The <code>try await</code> matters here: analysis is asynchronous, and the route simply waits for it before serializing the response.</p>
</li>
</ul>
<p>Anything else falls through to a JSON 404, so even unknown routes respond in the same format the browser already knows how to parse.</p>
<p>Errors work the same way: thrown errors are caught in one place and converted into JSON error responses with an appropriate status code, which is exactly what the web app's <code>payload.error?.message</code> check reads.</p>
<p>One practical detail: because the browser calls the companion from a different origin (the Vite dev server), every response also carries CORS headers, and the router answers preflight <code>OPTIONS</code> requests with an empty <code>204</code>. Without that, the browser would block the <code>fetch</code> before it ever reached these routes.</p>
<h2 id="heading-check-foundation-models-availability">Check Foundation Models Availability</h2>
<p>The companion shouldn't assume that the model is available. Check it first:</p>
<pre><code class="language-swift">private struct ModelSupport: Encodable {
    let visionAvailable: Bool
    let foundationModelAvailable: Bool
    let foundat