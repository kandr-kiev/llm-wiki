---
source_url: https://www.freecodecamp.org/news/how-clients-and-servers-communicate-handbook-http-rest-websockets-graphql-grpc-protobuf/
ingested: 2026-07-24
sha256: 3a8c917730aa24d64324e2bbfc0878e3c4ea1b5cb9b9265bacd45d381856e7d9
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How Clients and Servers Communicate: Full Handbook on HTTP/1.1, HTTP/2, REST, WebSockets, GraphQL, gRPC, and Protocol Buffers</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-clients-and-servers-communicate-handbook-http-rest-websockets-graphql-grpc-protobuf/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="You&#39;ve built and consumed APIs. You know what a GET request is, what a JSON response looks like, and how to add an Authorization header. You&#39;ve used REST, maybe tried GraphQL, and perhaps heard of gRP">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How Clients and Servers Communicate: Full Handbook on HTTP/1.1, HTTP/2, REST, WebSockets, GraphQL, gRPC, and Protocol Buffers">
    
        <meta property="og:description" content="You&#39;ve built and consumed APIs. You know what a GET request is, what a JSON response looks like, and how to add an Authorization header. You&#39;ve used REST, maybe tried GraphQL, and perhaps heard of gRP">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-clients-and-servers-communicate-handbook-http-rest-websockets-graphql-grpc-protobuf/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/b44f7067-5398-492a-b1f7-789f73673c34.png">
    <meta property="article:published_time" content="2026-07-23T23:14:49.488Z">
    <meta property="article:modified_time" content="2026-07-23T23:14:49.488Z">
    
        <meta property="article:tag" content="server">
    
        <meta property="article:tag" content="clients">
    
        <meta property="article:tag" content="networking">
    
        <meta property="article:tag" content="software">
    
        <meta property="article:tag" content="engineering">
    
        <meta property="article:tag" content="gRPC">
    
        <meta property="article:tag" content="http">
    
        <meta property="article:tag" content="http2">
    
        <meta property="article:tag" content="protobuf">
    
        <meta property="article:tag" content="handbook">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How Clients and Servers Communicate: Full Handbook on HTTP/1.1, HTTP/2, REST, WebSockets, GraphQL, gRPC, and Protocol Buffers">
    
        <meta name="twitter:description" content="You&#39;ve built and consumed APIs. You know what a GET request is, what a JSON response looks like, and how to add an Authorization header. You&#39;ve used REST, maybe tried GraphQL, and perhaps heard of gRP">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-clients-and-servers-communicate-handbook-http-rest-websockets-graphql-grpc-protobuf/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/b44f7067-5398-492a-b1f7-789f73673c34.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Oluwaseyi Fatunmole">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="server, clients, networking, software, engineering, gRPC, http, http2, protobuf, handbook">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/b44f7067-5398-492a-b1f7-789f73673c34.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-clients-and-servers-communicate-handbook-http-rest-websockets-graphql-grpc-protobuf/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-23T23:14:49.488Z",
	"dateModified": "2026-07-23T23:14:49.488Z",
	"keywords": "server, clients, networking, software, engineering, gRPC, http, http2, protobuf, handbook",
	"description": "You&#x27;ve built and consumed APIs. You know what a GET request is, what a JSON response looks like, and how to add an Authorization header. You&#x27;ve used REST, maybe tried GraphQL, and perhaps heard of gRP",
	"headline": "How Clients and Servers Communicate: Full Handbook on HTTP/1.1, HTTP/2, REST, WebSockets, GraphQL, gRPC, and Protocol Buffers",
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-23T23:14:49.488Z">
                            July 23, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/server/">
                                #server
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How Clients and Servers Communicate: Full Handbook on HTTP/1.1, HTTP/2, REST, WebSockets, GraphQL, gRPC, and Protocol Buffers</h1>
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
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/b44f7067-5398-492a-b1f7-789f73673c34.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/b44f7067-5398-492a-b1f7-789f73673c34.png" alt="How Clients and Servers Communicate: Full Handbook on HTTP/1.1, HTTP/2, REST, WebSockets, GraphQL, gRPC, and Protocol Buffers" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>You've built and consumed APIs. You know what a GET request is, what a JSON response looks like, and how to add an Authorization header. You've used REST, maybe tried GraphQL, and perhaps heard of gRPC.</p>
<p>But do you know what actually happens when your application sends a request? What travels through the wire? Why does HTTP/2 make things faster? Why do WebSockets exist when HTTP already works? What makes Protocol Buffers different from JSON at a fundamental level?</p>
<p>And when you're designing a system, how do you decide which communication approach to use?</p>
<p>These are the questions this handbook answers.</p>
<p>This isn't a beginner's guide to APIs. This is a deep dive into how clients and servers actually communicate: the protocols, the trade-offs, the history of why each approach was built, and the engineering thinking behind choosing one over another.</p>
<p>By the end, you won't just know what these technologies are. You'll understand why they exist, how they work at a level that makes you a better engineer, and how to make deliberate architectural decisions about communication in your systems.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#the-foundation-how-two-machines-talk-to-each-other">The Foundation: How Two Machines Talk to Each Other</a></p>
</li>
<li><p><a href="#http11-the-protocol-that-built-the-web">HTTP/1.1: The Protocol That Built the Web</a></p>
</li>
<li><p><a href="#the-problems-http11-could-not-solve">The Problems HTTP/1.1 Could Not Solve</a></p>
</li>
<li><p><a href="#http2-rebuilding-the-foundation">HTTP/2: Rebuilding the Foundation</a></p>
</li>
<li><p><a href="#http3-and-quic-the-next-evolution">HTTP/3 and QUIC: The Next Evolution</a></p>
</li>
<li><p><a href="#data-formats-how-information-is-encoded">Data Formats: How Information Is Encoded</a></p>
</li>
<li><p><a href="#rest-the-architecture-that-took-over-the-world">REST: The Architecture That Took Over the World</a></p>
</li>
<li><p><a href="#the-limits-of-rest">The Limits of REST</a></p>
</li>
<li><p><a href="#graphql-letting-the-client-decide">GraphQL: Letting the Client Decide</a></p>
</li>
<li><p><a href="#websockets-when-http-is-not-enough">WebSockets: When HTTP Is Not Enough</a></p>
</li>
<li><p><a href="#server-sent-events-the-simpler-real-time-option">Server-Sent Events: The Simpler Real-Time Option</a></p>
</li>
<li><p><a href="#protocol-buffers-a-new-language-for-data">Protocol Buffers: A New Language for Data</a></p>
</li>
<li><p><a href="#grpc-remote-procedure-calls-at-scale">gRPC: Remote Procedure Calls at Scale</a></p>
</li>
<li><p><a href="#the-complete-comparison">The Complete Comparison</a></p>
</li>
<li><p><a href="#how-to-choose-the-engineering-decision-framework">How to Choose: The Engineering Decision Framework</a></p>
</li>
<li><p><a href="#conclusion">Conclusion</a></p>
</li>
</ul>
<h2 id="heading-the-foundation-how-two-machines-talk-to-each-other">The Foundation: How Two Machines Talk to Each Other</h2>
<p>Before any protocol, data format, or architectural style enters the picture, two machines need to establish a connection. Understanding this foundation makes everything else click.</p>
<h3 id="heading-ip-addresses-and-ports">IP Addresses and Ports</h3>
<p>Every device on a network has an IP address: a unique identifier that works like a postal address. When your application sends a request to <code>api.example.com</code>, the first thing that happens is a DNS lookup, which translates that human-readable name into an IP address like <code>93.184.216.34</code>. That IP address is where the packet is going.</p>
<p>But an IP address alone isn't enough. A single server might be running dozens of different services simultaneously: a web server, a database, an email server, an SSH daemon.</p>
<p>Ports tell the operating system which service should handle the incoming connection. Port 80 is the conventional port for HTTP. Port 443 is for HTTPS. Port 5432 is for PostgreSQL. Port 22 is for SSH. When you call <code>api.example.com/users</code>, you are actually calling <code>api.example.com:443/users</code>. The browser fills in the port automatically.</p>
<h3 id="heading-tcp-the-reliable-foundation">TCP: The Reliable Foundation</h3>
<p>Most web communication runs over TCP (Transmission Control Protocol). TCP is a connection-oriented protocol, which means before any data is exchanged, both parties go through a handshake to establish a connection.</p>
<p>The TCP handshake works in three steps, which is why it's called the three-way handshake:</p>
<pre><code class="language-plaintext">Client                    Server
  |                          |
  |-------- SYN -----------&gt;|   "I want to connect"
  |                          |
  |&lt;------- SYN-ACK --------|   "Okay, I acknowledge. Ready?"
  |                          |
  |-------- ACK -----------&gt;|   "Great, let's go"
  |                          |
  [Connection established]
</code></pre>
<p>SYN stands for synchronize. ACK stands for acknowledge. After these three packets, the connection exists and data can flow.</p>
<p>TCP guarantees three things that make it the foundation of reliable communication:</p>
<ol>
<li><p><strong>Delivery</strong>: if a packet is lost in transit, TCP detects this and retransmits it automatically. The application layer never has to worry about lost packets.</p>
</li>
<li><p><strong>Order</strong>: packets arrive in the same order they were sent. If packets arrive out of order (which happens frequently on real networks), TCP reorders them before delivering them to the application.</p>
</li>
<li><p><strong>Error detection</strong>: every TCP packet includes a checksum. If the data is corrupted in transit, TCP detects and discards the corrupted packet, then requests a retransmission.</p>
</li>
</ol>
<p>This reliability comes at a cost: the overhead of the handshake, the acknowledgment packets, and the retransmission logic.</p>
<p>For many use cases, this cost is worth it. For some (live video streaming, online gaming, DNS lookups), UDP (User Datagram Protocol) is preferred because it sends packets without any of this overhead, accepting some loss in exchange for speed. HTTP/3, which we'll cover later, is built on a protocol that brings reliability to UDP.</p>
<h3 id="heading-tls-encrypting-the-connection">TLS: Encrypting the Connection</h3>
<p>On the modern web, most connections use HTTPS rather than plain HTTP. The S stands for Secure, and the security is provided by TLS (Transport Layer Security), the successor to SSL.</p>
<p>TLS adds an additional handshake on top of the TCP connection. During the TLS handshake:</p>
<ol>
<li><p>The client and the server agree on which version of TLS to use and which encryption algorithms to support</p>
</li>
<li><p>The server presents its digital certificate (issued by a trusted Certificate Authority)</p>
</li>
<li><p>The client verifies the certificate is valid and belongs to the server it intended to reach</p>
</li>
<li><p>They exchange encryption keys using asymmetric cryptography</p>
</li>
<li><p>From that point forward, all communication is encrypted with symmetric encryption</p>
</li>
</ol>
<p>The TLS handshake adds latency. In TLS 1.2, it takes two round trips before any application data can flow. TLS 1.3, released in 2018, reduced this to one round trip, and even supports zero round-trip resumption for returning connections.</p>
<p>Understanding TCP and TLS matters because every protocol we discuss runs on top of them (until HTTP/3, which changes the underlying transport). When people talk about the "overhead" of HTTPS or the "cost" of establishing a connection, they're talking about the time and packets spent on these handshakes before a single byte of your actual request travels.</p>
<h2 id="heading-http11-the-protocol-that-built-the-web">HTTP/1.1: The Protocol That Built the Web</h2>
<p>HTTP (HyperText Transfer Protocol) was invented by Tim Berners-Lee in 1991 to transfer HTML documents between computers. HTTP/1.0 was simple: one request per connection, then the connection closes.</p>
<p>HTTP/1.1, standardized in 1997, brought significant improvements and became the dominant version of HTTP for nearly two decades. It introduced persistent connections (keep connections open across multiple requests), chunked transfer encoding, and more sophisticated caching mechanisms.</p>
<h3 id="heading-how-an-http11-request-works">How an HTTP/1.1 Request Works</h3>
<p>An HTTP request is a text message with a specific structure:</p>
<pre><code class="language-plaintext">POST /api/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiJ9...
Accept: application/json
Content-Length: 45
User-Agent: MyApp/2.0

{"name": "John Smith", "email": "john@example.com"}
</code></pre>
<p>The first line is the request line: the HTTP method (POST), the path (/api/users), and the protocol version.</p>
<p>Below that are the headers: key-value pairs that provide metadata about the request. The host, the content type, the authorization token, what format the client accepts, and how large the body is.</p>
<p>After a blank line comes the body: the actual data being sent.</p>
<p>The server processes this and responds:</p>
<pre><code class="language-plaintext">HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/users/usr_789
Date: Mon, 21 Jul 2026 09:15:00 GMT
Content-Length: 89

{"id": "usr_789", "name": "John Smith", "email": "john@example.com", "created_at": "..."}
</code></pre>
<p>The response has a status line (the protocol version, the status code, and a reason phrase), headers, and a body.</p>
<h3 id="heading-http-methods-and-their-semantics">HTTP Methods and Their Semantics</h3>
<p>HTTP/1.1 defines several methods, each with specific semantics:</p>
<ul>
<li><p><strong>GET</strong> retrieves a resource. A GET request should have no side effects. It shouldn't create or modify anything. It's safe and idempotent, meaning calling it multiple times has the same effect as calling it once.</p>
</li>
<li><p><strong>POST</strong> submits data to create a new resource or trigger an action. It's neither safe nor idempotent: calling POST twice typically creates two resources.</p>
</li>
<li><p><strong>PUT</strong> replaces a resource entirely with the provided data. It's idempotent: calling PUT twice with the same data has the same effect as calling it once.</p>
</li>
<li><p><strong>PATCH</strong> partially updates a resource. Only the fields provided are changed.</p>
</li>
<li><p><strong>DELETE</strong> removes a resource. It's idempotent: deleting something that doesn't exist is still considered successful.</p>
</li>
<li><p><strong>HEAD</strong> is identical to GET but the server only returns headers, not the body. It's used to check if a resource exists or has been modified without downloading the full content.</p>
</li>
<li><p><strong>OPTIONS</strong> asks the server what methods are allowed for a resource. It's used in CORS preflight requests.</p>
</li>
</ul>
<h3 id="heading-status-codes">Status Codes</h3>
<p>HTTP status codes are three-digit numbers grouped into five categories:</p>
<p><strong>1xx Informational</strong> — the server has received the request and is continuing to process it. These are rarely seen in practice outside of specific use cases like HTTP upgrade (used to establish WebSocket connections).</p>
<p><strong>2xx Success</strong> — the request was received, understood, and accepted.</p>
<ul>
<li><p>200 OK: standard success response</p>
</li>
<li><p>201 Created: a new resource was created</p>
</li>
<li><p>204 No Content: success but nothing to return (common for DELETE)</p>
</li>
</ul>
<p><strong>3xx Redirection</strong> — further action is required to complete the request.</p>
<ul>
<li><p>301 Moved Permanently: the resource has a new URL forever</p>
</li>
<li><p>302 Found: temporary redirect</p>
</li>
<li><p>304 Not Modified: the cached version is still valid (used with ETags)</p>
</li>
</ul>
<p><strong>4xx Client Error</strong> — the request contains bad syntax or can't be fulfilled.</p>
<ul>
<li><p>400 Bad Request: the request is malformed</p>
</li>
<li><p>401 Unauthorized: authentication is required (despite the name, it means unauthenticated)</p>
</li>
<li><p>403 Forbidden: authenticated but not authorized to access this resource</p>
</li>
<li><p>404 Not Found: the resource doesn't exist</p>
</li>
<li><p>422 Unprocessable Entity: the request is syntactically valid but semantically wrong (common for validation errors)</p>
</li>
<li><p>429 Too Many Requests: rate limit exceeded</p>
</li>
</ul>
<p><strong>5xx Server Error</strong> — the server failed to fulfill a valid request.</p>
<ul>
<li><p>500 Internal Server Error: something went wrong on the server</p>
</li>
<li><p>502 Bad Gateway: the server received an invalid response from an upstream server</p>
</li>
<li><p>503 Service Unavailable: the server is temporarily unavailable</p>
</li>
<li><p>504 Gateway Timeout: the upstream server did not respond in time</p>
</li>
</ul>
<h3 id="heading-caching-in-http11">Caching in HTTP/1.1</h3>
<p>One of HTTP/1.1's most powerful features is its built-in caching model. Responses can include headers that tell clients and intermediate caches how long to store a response and when to revalidate it.</p>
<ul>
<li><p><code>Cache-Control: max-age=3600</code> tells the client to cache this response for one hour.</p>
</li>
<li><p><code>Cache-Control: no-cache</code> tells the client to always revalidate with the server before using a cached response.</p>
</li>
<li><p><code>Cache-Control: no-store</code> tells the client never to cache this response.</p>
</li>
</ul>
<p><code>ETag</code> is a fingerprint of the response content. When the client makes a subsequent request, it sends the ETag back in an <code>If-None-Match</code> header. If the content hasn't changed, the server responds with 304 Not Modified and no body, saving bandwidth.</p>
<p><code>Last-Modified</code> works similarly: the client sends <code>If-Modified-Since</code> and the server confirms whether the content has changed.</p>
<p>Caching is one of the key reasons REST over HTTP became dominant. GET requests to well-designed REST APIs can be cached at the CDN level, meaning the same response is served to thousands of users without the request ever reaching your origin server.</p>
<h2 id="heading-the-problems-http11-could-not-solve">The Problems HTTP/1.1 Could Not Solve</h2>
<p>HTTP/1.1 served the web well for two decades. But as the web grew more complex, applications more dynamic, and user expectations higher, its architectural limitations became significant performance bottlenecks.</p>
<h3 id="heading-head-of-line-blocking">Head-of-Line Blocking</h3>
<p>HTTP/1.1 processes requests sequentially on a single connection. The server must finish responding to one request before the next one on the same connection begins.</p>
<pre><code class="language-plaintext">Connection 1:
Request 1 (slow database query) -----&gt; [3 seconds] -----&gt; Response 1
Request 2 (fast in-memory read) -----&gt; [waits 3 seconds] -----&gt; Response 2
Request 3 (static file) -----------&gt; [waits 3+ seconds] -----&gt; Response 3
</code></pre>
<p>Request 2 and Request 3 are fast operations. But they're stuck waiting for Request 1 to complete. This is head-of-line blocking: the head of the queue blocks everything behind it.</p>
<p>Browsers worked around this by opening multiple parallel TCP connections to the same server, typically six. But each connection requires its own TCP handshake and TLS negotiation, consuming resources on both the client and server.</p>
<h3 id="heading-verbose-headers-on-every-request">Verbose Headers on Every Request</h3>
<p>Every HTTP/1.1 request sends its complete headers as plain text. Consider a mobile application making fifty requests during a session. On every single request, the following headers are sent in full:</p>
<pre><code class="language-plaintext">Host: api.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c3JfMTIzIn0...
Content-Type: application/json
Accept: application/json
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)...
</code></pre>
<p>The Authorization header alone, carrying a JWT, can be 400 to 600 bytes. Multiplied by fifty requests, that is 20 to 30 kilobytes of data carrying nothing but headers that haven't changed between requests.</p>
<p>On a 4G mobile connection with limited bandwidth, this is waste. On a 2G connection in a network-constrained environment, it's a significant performance penalty.</p>
<h3 id="heading-no-server-push">No Server Push</h3>
<p>HTTP/1.1 is strictly request-response. The server can't send data until the client asks for it. This fundamental limitation means the server can never proactively inform the client of changes.</p>
<p>For applications requiring real-time updates, short polling became a common workaround: the client sends a request every few seconds asking "has anything changed?" This is inefficient because most polling requests receive a "no, nothing has changed" response, consuming bandwidth and server resources for no purpose.</p>
<p>Long polling was a refinement: the client sends a request and the server holds it open until something changes or a timeout occurs. This reduces unnecessary responses but keeps connections open indefinitely, consuming server resources.</p>
<p>Both are workarounds for a fundamental limitation of HTTP/1.1's request-response model.</p>
<h3 id="heading-inefficient-use-of-connections">Inefficient Use of Connections</h3>
<p>Opening a new TCP connection requires the three-way handshake plus the TLS handshake: a process that can take 200 to 500 milliseconds on a mobile connection.</p>
<p>HTTP/1.1 introduced keep-alive connections to reuse connections across multiple requests, but head-of-line blocking made this only partially effective. Browsers opened multiple connections to compensate, but six parallel connections per domain is both a client limitation and a server resource concern at scale.</p>
<h2 id="heading-http2-rebuilding-the-foundation">HTTP/2: Rebuilding the Foundation</h2>
<p>Google published a protocol called SPDY (pronounced "speedy") in 2009, designed to address HTTP/1.1's performance limitations. SPDY demonstrated that significant improvements were possible without changing the fundamental HTTP semantics. HTTP/2, standardized by the IETF in 2015, was heavily based on SPDY and became the successor to HTTP/1.1.</p>
<p>HTTP/2 doesn't change what you send. From the application developer's perspective, requests still have methods, paths, headers, and bodies. Responses still have status codes, headers, and bodies. What HTTP/2 changes is how all of this is transmitted.</p>
<h3 id="heading-binary-framing-the-core-change">Binary Framing: The Core Change</h3>
<p>HTTP/1.1 is a text protocol. Headers, status lines, and method names are all ASCII text. Machines must parse this text character by character to interpret it.</p>
<p>HTTP/2 is a binary protocol. Every piece of information is encoded as binary frames rather than text. Binary is more compact and significantly faster for machines to parse. Instead of tokenizing a string looking for colons and newlines to separate header names from values, a binary parser reads fixed-length fields directly from memory.</p>
<p>The binary framing layer is the foundation everyt