---
source_url: https://www.freecodecamp.org/news/remote-procedure-calls-protocol-buffers-and-modern-distributed-systems-communication/
ingested: 2026-07-23
sha256: ee71747c1b9423d97765531fd19364c16ea875b9d668799591a4e48c48483e0f
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>From RPC to gRPC: Understanding Remote Procedure Calls, Protocol Buffers, and Modern Distributed Systems Communication </title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/remote-procedure-calls-protocol-buffers-and-modern-distributed-systems-communication/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="Every application, at some point, needs to talk to another system. A mobile app talks to a backend. A backend service talks to a payment gateway. An authentication service talks to a user service. A d">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="From RPC to gRPC: Understanding Remote Procedure Calls, Protocol Buffers, and Modern Distributed Systems Communication ">
    
        <meta property="og:description" content="Every application, at some point, needs to talk to another system. A mobile app talks to a backend. A backend service talks to a payment gateway. An authentication service talks to a user service. A d">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/remote-procedure-calls-protocol-buffers-and-modern-distributed-systems-communication/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/1205581e-5729-44fa-837e-0f30981ea059.png">
    <meta property="article:published_time" content="2026-07-22T22:36:09.756Z">
    <meta property="article:modified_time" content="2026-07-22T22:36:09.756Z">
    
        <meta property="article:tag" content="gRPC">
    
        <meta property="article:tag" content="RPC">
    
        <meta property="article:tag" content="Dart">
    
        <meta property="article:tag" content="Flutter">
    
        <meta property="article:tag" content="Google">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="From RPC to gRPC: Understanding Remote Procedure Calls, Protocol Buffers, and Modern Distributed Systems Communication ">
    
        <meta name="twitter:description" content="Every application, at some point, needs to talk to another system. A mobile app talks to a backend. A backend service talks to a payment gateway. An authentication service talks to a user service. A d">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/remote-procedure-calls-protocol-buffers-and-modern-distributed-systems-communication/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/1205581e-5729-44fa-837e-0f30981ea059.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Oluwaseyi Fatunmole">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="gRPC, RPC, Dart, Flutter, Google">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/1205581e-5729-44fa-837e-0f30981ea059.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/remote-procedure-calls-protocol-buffers-and-modern-distributed-systems-communication/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-22T22:36:09.756Z",
	"dateModified": "2026-07-22T22:36:09.756Z",
	"keywords": "gRPC, RPC, Dart, Flutter, Google",
	"description": "Every application, at some point, needs to talk to another system. A mobile app talks to a backend. A backend service talks to a payment gateway. An authentication service talks to a user service. A d",
	"headline": "From RPC to gRPC: Understanding Remote Procedure Calls, Protocol Buffers, and Modern Distributed Systems Communication ",
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-22T22:36:09.756Z">
                            July 22, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/grpc/">
                                #gRPC
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">From RPC to gRPC: Understanding Remote Procedure Calls, Protocol Buffers, and Modern Distributed Systems Communication </h1>
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
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/1205581e-5729-44fa-837e-0f30981ea059.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/1205581e-5729-44fa-837e-0f30981ea059.png" alt="From RPC to gRPC: Understanding Remote Procedure Calls, Protocol Buffers, and Modern Distributed Systems Communication " ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>Every application, at some point, needs to talk to another system. A mobile app talks to a backend. A backend service talks to a payment gateway. An authentication service talks to a user service. A data pipeline talks to a storage layer.</p>
<p>The question is never whether systems need to communicate. The question is always how.</p>
<p>For years, REST over HTTP with JSON was the default answer. It works, it's simple, and the tooling is everywhere. But as systems grow in scale (in the number of services talking to each other, the volume of data being exchanged, and the need for real-time communication), REST starts to show its limits.</p>
<p>This is where Remote Procedure Calls, Protocol Buffers, and gRPC enter the picture.</p>
<p>In this handbook, you'll learn what RPC is and the problem it was designed to solve. You'll also understand Protocol Buffers: what they are, why they exist, and how they work.</p>
<p>You'll then see how Google combined these ideas into gRPC, one of the most powerful communication frameworks in modern distributed systems. You'll learn all four gRPC communication patterns, see code generated across multiple languages from a single contract file, and walk through a complete end-to-end Flutter implementation with production-grade concerns including authentication, error handling, and timeouts.</p>
<p>By the end, you won't just know what gRPC is. You'll understand when to use it, when not to, and how to think about service communication as a systems engineer.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-what-is-a-remote-procedure-call">What is a Remote Procedure Call</a>?</p>
</li>
<li><p><a href="#heading-the-problem-rpc-solves">The Problem RPC Solves</a></p>
</li>
<li><p><a href="#heading-why-grpc-over-rest-the-real-case">Why gRPC Over REST: The Real Case</a></p>
</li>
<li><p><a href="#heading-protocol-buffers-a-new-language-for-data">Protocol Buffers: A New Language for Data</a></p>
</li>
<li><p><a href="#heading-the-proto-file">The Proto File</a></p>
</li>
<li><p><a href="#heading-json-vs-protocol-buffers">JSON vs Protocol Buffers</a></p>
</li>
<li><p><a href="#heading-the-protoc-compiler-and-code-generation">The Protoc Compiler and Code Generation</a></p>
</li>
<li><p><a href="#heading-what-is-grpc">What is gRPC</a>?</p>
</li>
<li><p><a href="#heading-why-http2-matters-for-grpc">Why HTTP/2 Matters for gRPC</a></p>
</li>
<li><p><a href="#heading-the-four-grpc-communication-patterns">The Four gRPC Communication Patterns</a></p>
</li>
<li><p><a href="#heading-the-protobuf-repository-organizational-best-practice">The Protobuf Repository: Organizational Best Practice</a></p>
</li>
<li><p><a href="#heading-building-a-complete-grpc-system-with-dart-and-flutter">Building a Complete gRPC System with Dart and Flutter</a></p>
</li>
<li><p><a href="#heading-production-concerns">Production Concerns</a></p>
</li>
<li><p><a href="#heading-grpc-vs-rest-vs-websockets-when-to-use-what">gRPC vs REST vs WebSockets: When to Use What</a></p>
</li>
<li><p><a href="#heading-the-hybrid-architecture">The Hybrid Architecture</a></p>
</li>
<li><p><a href="#heading-conclusion">Conclusion</a></p>
</li>
</ul>
<h2 id="heading-what-is-a-remote-procedure-call">What is a Remote Procedure Call?</h2>
<p>To understand RPCs, you first need to understand what a procedure call is.</p>
<p>A procedure call means invoking a procedure or function so that its code executes. For example, in Dart:</p>
<pre><code class="language-dart">double calculateTax(double amount) {
  return amount * 0.075;
}

final tax = calculateTax(50000); // local procedure call
</code></pre>
<p>You call <code>calculateTax</code>, pass an argument, and get a result back. The function lives on the same machine, in the same process, in the same memory space. This is a local procedure call.</p>
<p>A Remote Procedure Call takes this same idea and stretches it across a network. The function you're calling lives on a different machine, in a different process, and potentially in a different country. But from the caller's perspective, it feels exactly like calling a local function.</p>
<pre><code class="language-dart">// This looks like a local function call
final tax = await taxService.calculateTax(amount: 50000);

// But under the hood, this:
// 1. Serializes the argument into a binary format
// 2. Sends it over a network connection to a remote server
// 3. The server executes calculateTax with your argument
// 4. Serializes the result
// 5. Sends it back over the network
// 6. Deserializes it into a Dart object
// 7. Returns it to you as if it were local
</code></pre>
<p>The network complexity is completely hidden. You call a function. You get a result. Everything in between is handled by the RPC framework.</p>
<p>This is the fundamental idea behind RPC: make calling a remote function feel as natural as calling a local one.</p>
<h2 id="heading-the-problem-rpc-solves">The Problem RPC Solves</h2>
<p>To appreciate why RPC matters, you need to understand what the alternative looks like.</p>
<p>Without RPC, calling a remote service looks like this:</p>
<pre><code class="language-dart">Future&lt;double&gt; calculateTax(double amount) async {
  final response = await http.post(
    Uri.parse('https://tax-service.internal/api/v1/calculate'),
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer $token',
    },
    body: jsonEncode({'amount': amount}),
  );

  if (response.statusCode != 200) {
    throw Exception('Tax calculation failed: ${response.statusCode}');
  }

  final data = jsonDecode(response.body);
  return (data['tax'] as num).toDouble();
}
</code></pre>
<p>Every service call requires you to:</p>
<ul>
<li><p>Know and hardcode the endpoint URL</p>
</li>
<li><p>Know the correct HTTP method</p>
</li>
<li><p>Manually serialize your request to JSON</p>
</li>
<li><p>Handle HTTP status codes yourself</p>
</li>
<li><p>Manually deserialize the response from JSON</p>
</li>
<li><p>Cast dynamic types to the types you actually expect</p>
</li>
<li><p>Hope the field names in the response match what you think they are</p>
</li>
</ul>
<p>Now multiply this by every single service call in your application. An authentication service, a user service, a payment service, a notification service, a transaction service. Every one of them requires the same manual boilerplate. Every one of them introduces the possibility of a typo in a field name, a wrong status code assumption, or a JSON deserialization failure that only surfaces at runtime.</p>
<p>With RPC:</p>
<pre><code class="language-dart">// Feels like a local function call
final tax = await taxService.calculateTax(
  TaxRequest(amount: 50000),
);
// tax is already a strongly typed TaxResponse object
// No URLs. No HTTP methods. No JSON parsing. No casting.
</code></pre>
<p>The framework handles everything. The function signature is defined in a contract file that both the client and server use. The types are enforced at compile time. If the server changes the response shape, the client fails to compile before anything reaches production.</p>
<p>This is what RPC solves: it removes the accidental complexity of network communication and lets you focus on what you're actually trying to do.</p>
<h2 id="heading-why-grpc-over-rest-the-real-case">Why gRPC Over REST: The Real Case</h2>
<p>Before going into the technical details of Protocol Buffers and gRPC, it's important to make a solid case for why you'd choose gRPC over REST in specific scenarios. This isn't a claim that gRPC is always better. It's a clear look at where it genuinely wins.</p>
<h3 id="heading-large-payloads-called-by-many-internal-systems">Large Payloads Called by Many Internal Systems</h3>
<p>Consider an internal enterprise API in a large telecommunications company. A single request and response payload for a plan registration or activation flow can contain over a thousand fields. This endpoint is called by dozens of internal applications: billing systems, CRM platforms, customer-facing mobile apps, internal dashboards, and partner portals.</p>
<p>With REST and JSON, every one of those applications sends and receives that thousand-field payload as text. Field names like <code>subscription_activation_status</code>, <code>rate_plan_identifier</code>, and <code>network_provisioning_reference</code> travel over the wire as strings on every single request. A significant portion of every payload isn't data. It's labels for data.</p>
<p>With Protocol Buffers, field names never appear in the payload at all. Only field numbers and values travel over the wire. That thousand-field payload shrinks dramatically. For an endpoint called millions of times per day by dozens of systems, the bandwidth saving is enormous and translates directly to infrastructure cost reduction.</p>
<p>Beyond size, the generated client guarantee is equally important. With REST, each of those dozens of applications reads the API documentation and builds its own understanding of the contract. When the backend changes a field name or type, not every application finds out immediately. Some find out in production when they break.</p>
<p>With a shared <code>.proto</code> file, every application generates its own strongly typed client from the same source. A contract change means every application regenerates. The compiler immediately reports where the breaking change affects each codebase. Nothing reaches production in a broken state.</p>
<h3 id="heading-low-bandwidth-and-remote-network-conditions">Low Bandwidth and Remote Network Conditions</h3>
<p>This is one of the most under-appreciated advantages of gRPC in markets where network quality varies significantly.</p>
<p>In many regions, a substantial portion of mobile users are on 2G or 3G connections. On a 2G connection, bandwidth can be as low as 50 to 100 kilobits per second. A REST JSON response that is 80 kilobytes takes over 6 seconds to download on a 2G connection. The equivalent protobuf binary, which can be 3 to 10 times smaller, takes under 2 seconds.</p>
<p>That difference isn't a technical footnote. It's the line between an application that feels usable and one that feels broken to a significant portion of your users. For any product that operates in markets with variable network conditions, protobuf's binary efficiency is a direct competitive advantage.</p>
<p>Beyond size, gRPC runs over HTTP/2 which maintains a single persistent connection rather than opening a new connection for every request. On slow networks where connection establishment (the TCP handshake and TLS negotiation) can itself take hundreds of milliseconds, reusing a single connection across many calls saves significant time over a session.</p>
<h3 id="heading-microservice-to-microservice-communication">Microservice to Microservice Communication</h3>
<p>When two internal services need to communicate, you have options. A message bus like Kafka or RabbitMQ is excellent when you don't need an immediate response, when the operation can happen asynchronously, and when you're broadcasting something that happened to multiple consumers.</p>
<p>But many service-to-service calls are synchronous by nature. An authentication service needs to validate a token right now before the request proceeds. A fraud detection service needs to assess a transaction right now before the payment is authorized. A pricing service needs to calculate a rate right now before the quote is generated. These operations can't publish an event and wait.</p>
<p>For synchronous service-to-service calls at high frequency, gRPC over HTTP/2 with protobuf encoding is significantly more efficient than REST. The persistent multiplexed connection means no connection setup overhead per call. The binary encoding means no JSON serialization and deserialization overhead on every hop. The generated clients mean both services compile against the same contract.</p>
<p>At scale, when two services are calling each other thousands of times per second, these efficiency differences compound into real performance and cost differences.</p>
<h3 id="heading-managing-api-contracts-across-multiple-teams">Managing API Contracts Across Multiple Teams</h3>
<p>In a large engineering organization, multiple teams build services that others depend on. REST API contracts live in documentation. Documentation goes stale. The backend team changes a field name. The mobile team finds out when users report crashes. The data team finds out when their pipeline throws an error at 2am.</p>
<p>gRPC's protobuf repository approach transforms contract management from a documentation problem into a code problem. Contract changes go through pull requests. Every dependent team reviews the change. Breaking changes are caught at compile time. Nobody is surprised in production.</p>
<p>This governance benefit scales with team size. The larger the organization, the more valuable it becomes.</p>
<h3 id="heading-real-time-communication">Real-Time Communication</h3>
<p>REST is request-response. The client asks and the server answers. The conversation ends. For real-time features, you either poll (wasteful) or bolt on a separate WebSocket server alongside your REST API (two different systems to maintain).</p>
<p>gRPC's streaming patterns handle real-time communication natively within the same framework you use for regular calls. A live balance update, a real-time transaction notification, or a bidirectional chat session all use the same generated client, the same connection, and the same protobuf encoding as your regular unary calls.</p>
<p>One framework with all communication patterns. No separate infrastructure.</p>
<h2 id="heading-protocol-buffers-a-new-language-for-data">Protocol Buffers: A New Language for Data</h2>
<p>RPC is a concept. To implement it, you need two things: a way to define the contract between client and server, and a way to serialize data efficiently for transmission over the network.</p>
<p>This is where Protocol Buffers comes in.</p>
<p>Protocol Buffers, commonly called protobuf, is a language-neutral, platform-neutral, extensible mechanism for serializing structured data. It was developed at Google in 2001, used internally for years, and open-sourced in 2008.</p>
<h3 id="heading-the-json-problem-at-scale">The JSON Problem at Scale</h3>
<p>JSON is the dominant data format for web APIs. It's human-readable, flexible, and universally supported. For many use cases, it's the right choice.</p>
<p>But JSON has structural inefficiencies that become painful at scale.</p>
<p>Consider a user profile response:</p>
<pre><code class="language-json">{
  "id": "usr_001",
  "first_name": "John",
  "last_name": "Smith",
  "email": "john@example.com",
  "phone_number": "+2348012345678",
  "account_type": "savings",
  "balance": 500000.00,
  "currency": "NGN",
  "is_verified": true,
  "is_active": true,
  "kyc_level": 3,
  "created_at": "2024-01-15T10:30:00Z",
  "last_login": "2026-07-20T09:15:00Z"
}
</code></pre>
<p>Every field name travels over the network as a string on every single response. <code>"first_name"</code>, <code>"account_type"</code>, <code>"phone_number"</code> aren't data. They're labels for data. But they consume bytes on every request.</p>
<p>Now consider an internal enterprise API with over a thousand fields in its request and response payload, being called by dozens of internal applications thousands of times per day. A significant portion of every payload is field name strings, not actual data. The overhead accumulates into real bandwidth and processing costs.</p>
<p>Beyond size, JSON has another problem: it has no schema at the network level. Nothing prevents a backend engineer from renaming <code>"first_name"</code> to <code>"firstName"</code> in a new deployment. The client breaks at runtime in production with real users.</p>
<h3 id="heading-what-protocol-buffers-do-differently">What Protocol Buffers Do Differently</h3>
<p>Protocol Buffers solve both problems with a fundamentally different approach to data encoding.</p>
<p>Instead of encoding data as human-readable text with field names, protobuf encodes data as compact binary using only field numbers and values. Field names never travel over the network.</p>
<p>Here's the same user profile defined in protobuf:</p>
<pre><code class="language-protobuf">message UserProfile {
  string id = 1;
  string first_name = 2;
  string last_name = 3;
  string email = 4;
  string phone_number = 5;
  string account_type = 6;
  double balance = 7;
  string currency = 8;
  bool is_verified = 9;
  bool is_active = 10;
  int32 kyc_level = 11;
  string created_at = 12;
  string last_login = 13;
}
</code></pre>
<p>When protobuf encodes this data, the output is binary that no human can read. But to a machine, it's extremely compact and fast to parse. The field numbers (1, 2, 3...) identify each field. The names never appear in the encoded output at all.</p>
<p>The result: the same user profile that's approximately 280 bytes in JSON is approximately 95 bytes in protobuf. That's three times smaller. For a thousand-field enterprise payload, this difference is enormous.</p>
<p>And because the schema is defined in a <code>.proto</code> file that both client and server compile against, field name changes are caught at compile time, not at runtime.</p>
<h2 id="heading-the-proto-file">The Proto File</h2>
<p>The <code>.proto</code> file is the heart of everything in the protobuf and gRPC ecosystem. It's where you define your data models and your service contracts.</p>
<p>It's written in Protocol Buffer Language (proto3) – not Go, not Dart, not Python, not Java. You write it in any text editor. VS Code with the <code>vscode-proto3</code> extension gives you syntax highlighting, autocomplete, and inline validation.</p>
<p>Here's a complete <code>.proto</code> file for a fintech platform:</p>
<pre><code class="language-csharp">syntax = "proto3";

package banking;

option go_package = "./banking";
option java_package = "com.fintech.banking";



service BankingService {
  // Unary: one request, one response
  rpc Login (LoginRequest) returns (LoginResponse);

  // Unary: fetch user profile
  rpc GetProfile (ProfileRequest) returns (UserProfile);

  // Server streaming: real-time balance updates
  rpc WatchBalance (BalanceRequest) returns (stream BalanceResponse);

  // Server streaming: live transaction feed
  rpc StreamTransactions (TransactionRequest) returns (stream Transaction);

  // Client streaming: upload KYC documents in chunks
  rpc UploadDocument (stream DocumentChunk) returns (UploadResponse);

  // Bidirectional streaming: live chat support
  rpc Chat (stream ChatMessage) returns (stream ChatMessage);
}



message LoginRequest {
  string email = 1;
  string password = 2;
}

message LoginResponse {
  string token = 1;
  string user_id = 2;
  int64 expires_at = 3;
}

message ProfileRequest {
  string user_id = 1;
}

message UserProfile {
  string id = 1;
  string first_name = 2;
  string last_name = 3;
  string email = 4;
  string phone_number = 5;
  string account_type = 6;
  double balance = 7;
  string currency = 8;
  bool is_verified = 9;
  int32 kyc_level = 10;
}

message BalanceRequest {
  string user_id = 1;
}

message BalanceResponse {
  double balance = 1;
  string currency = 2;
  int64 timestamp = 3;
}

message TransactionRequest {
  string user_id = 1;
  int32 limit = 2;
}

message Transaction {
  string id = 1;
  double amount = 2;
  string description = 3;
  string type = 4;
  int64 timestamp = 5;
}

message DocumentChunk {
  bytes data = 1;
  string document_type = 2;
  int32 chunk_index = 3;
  bool is_last = 4;
}

message UploadResponse {
  bool success = 1;
  string document_id = 2;
  string message = 3;
}

message ChatMessage {
  string sender_id = 1;
  string content = 2;
  int64 timestamp = 3;
}
</code></pre>
<p>Let's walk through every part of this file carefully.</p>
<h3 id="heading-the-syntax-declaration">The Syntax Declaration</h3>
<pre><code class="language-csharp">syntax = "proto3";
</code></pre>
<p>This tells the protobuf compiler which version of the Protocol