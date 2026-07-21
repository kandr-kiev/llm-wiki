---
source_url: https://www.freecodecamp.org/news/how-to-implement-paypal-in-a-microservice-architecture-using-nestjs-grpc-and-docker/
ingested: 2026-07-17
sha256: 733c87b7fc54bc3ed0e2a240df5c31a1be499195d64a78c60676612eb1dc0917
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Implement PayPal in a Microservice Architecture Using NestJS, gRPC, and Docker</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-to-implement-paypal-in-a-microservice-architecture-using-nestjs-grpc-and-docker/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="In this tutorial, you&#39;ll build a production-ready PayPal payment service using NestJS microservices. Along the way, you&#39;ll learn how to isolate payment logic into its own service, communicate between ">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Implement PayPal in a Microservice Architecture Using NestJS, gRPC, and Docker">
    
        <meta property="og:description" content="In this tutorial, you&#39;ll build a production-ready PayPal payment service using NestJS microservices. Along the way, you&#39;ll learn how to isolate payment logic into its own service, communicate between ">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-to-implement-paypal-in-a-microservice-architecture-using-nestjs-grpc-and-docker/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/665e54b7-b47e-4abe-a417-49b51569868f.png">
    <meta property="article:published_time" content="2026-07-16T22:56:30.311Z">
    <meta property="article:modified_time" content="2026-07-16T22:56:30.311Z">
    
        <meta property="article:tag" content="Microservices">
    
        <meta property="article:tag" content="PayPal">
    
        <meta property="article:tag" content="payments">
    
        <meta property="article:tag" content="nestjs">
    
        <meta property="article:tag" content="Docker">
    
        <meta property="article:tag" content="containers">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Implement PayPal in a Microservice Architecture Using NestJS, gRPC, and Docker">
    
        <meta name="twitter:description" content="In this tutorial, you&#39;ll build a production-ready PayPal payment service using NestJS microservices. Along the way, you&#39;ll learn how to isolate payment logic into its own service, communicate between ">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-to-implement-paypal-in-a-microservice-architecture-using-nestjs-grpc-and-docker/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/665e54b7-b47e-4abe-a417-49b51569868f.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Md Tarikul Islam">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="Microservices, PayPal, payments, nestjs, Docker, containers">
    <meta name="twitter:site" content="@freecodecamp">
    
        <meta name="twitter:creator" content="@MDTARIK46263152">
    

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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/665e54b7-b47e-4abe-a417-49b51569868f.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-to-implement-paypal-in-a-microservice-architecture-using-nestjs-grpc-and-docker/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-16T22:56:30.311Z",
	"dateModified": "2026-07-16T22:56:30.311Z",
	"keywords": "Microservices, PayPal, payments, nestjs, Docker, containers",
	"description": "In this tutorial, you&#x27;ll build a production-ready PayPal payment service using NestJS microservices. Along the way, you&#x27;ll learn how to isolate payment logic into its own service, communicate between ",
	"headline": "How to Implement PayPal in a Microservice Architecture Using NestJS, gRPC, and Docker",
	"author": {
		"@type": "Person",
		"name": "Md Tarikul Islam",
		"url": "https://www.freecodecamp.org/news/author/Tarikul001/",
		"sameAs": [
			"https://www.youtube.com/@BugCode420",
			"https://x.com/MDTARIK46263152"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/uploads/avatars/66cb39fcaa2a09f9a8d691c1/6042a598-84a2-4058-833f-1b7a1215c03d.jpg",
			"width": 3072,
			"height": 4096
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-16T22:56:30.311Z">
                            July 16, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/microservices/">
                                #Microservices
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Implement PayPal in a Microservice Architecture Using NestJS, gRPC, and Docker</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/uploads/avatars/66cb39fcaa2a09f9a8d691c1/6042a598-84a2-4058-833f-1b7a1215c03d.jpg 60w" sizes="60px" src="https://cdn.hashnode.com/uploads/avatars/66cb39fcaa2a09f9a8d691c1/6042a598-84a2-4058-833f-1b7a1215c03d.jpg" class="author-profile-image" alt="Md Tarikul Islam" width="3072" height="4096" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/Tarikul001/" data-test-label="profile-link">
                    
                        Md Tarikul Islam
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/665e54b7-b47e-4abe-a417-49b51569868f.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/665e54b7-b47e-4abe-a417-49b51569868f.png" alt="How to Implement PayPal in a Microservice Architecture Using NestJS, gRPC, and Docker" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>In this tutorial, you'll build a production-ready PayPal payment service using NestJS microservices. Along the way, you'll learn how to isolate payment logic into its own service, communicate between services using gRPC, publish payment events with RabbitMQ, and deploy everything with Docker.</p>
<p>By the end, you'll have a scalable payment architecture that can be reused across multiple business domains.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-introduction">Introduction</a></p>
</li>
<li><p><a href="#heading-why-use-a-dedicated-payment-service">Why Use a Dedicated Payment Service?</a></p>
</li>
<li><p><a href="#heading-architecture-overview">Architecture Overview</a></p>
<ul>
<li><a href="#heading-payment-state-machine">Payment State Machine</a></li>
</ul>
</li>
<li><p><a href="#heading-prerequisites">Prerequisites</a></p>
</li>
<li><p><a href="#heading-paypal-concepts-you-need-to-know">PayPal Concepts You Need to Know</a></p>
<ul>
<li><p><a href="#heading-sandbox-vs-live">Sandbox vs Live</a></p>
</li>
<li><p><a href="#heading-orders-api-flow-what-we-use">Orders API Flow (What We Use)</a></p>
</li>
<li><p><a href="#heading-environment-variables">Environment Variables</a></p>
</li>
</ul>
</li>
<li><p><a href="#heading-project-structure">Project Structure</a></p>
</li>
<li><p><a href="#heading-step-1-create-the-payment-service">Step 1 — Create the Payment Service</a></p>
</li>
<li><p><a href="#heading-step-2-define-the-grpc-contract">Step 2 — Define the gRPC Contract</a></p>
</li>
<li><p><a href="#heading-step-3-implement-the-paypal-service">Step 3 — Implement the PayPal Service</a></p>
</li>
<li><p><a href="#heading-step-4-build-the-payment-flow-create-approve-capture">Step 4 — Build the Payment Flow (Create → Approve → Capture)</a></p>
<ul>
<li><p><a href="#heading-4a-create-payment">4a. Create Payment</a></p>
</li>
<li><p><a href="#heading-4b-user-approves-on-paypal">4b. User Approves on PayPal</a></p>
</li>
<li><p><a href="#heading-4c-capture-payment">4c. Capture Payment</a></p>
</li>
</ul>
</li>
<li><p><a href="#heading-step-5-connect-domain-services-via-grpc">Step 5 — Connect Domain Services via gRPC</a></p>
<ul>
<li><a href="#heading-domain-service-business-logic-example">Domain Service Business Logic Example</a></li>
</ul>
</li>
<li><p><a href="#heading-step-6-add-the-api-gateway-layer">Step 6 — Add the API Gateway Layer</a></p>
</li>
<li><p><a href="#heading-step-7-publish-payment-events-with-rabbitmq">Step 7 — Publish Payment Events with RabbitMQ</a></p>
<ul>
<li><a href="#heading-two-paths-to-mark-an-order-as-paid">Two Paths to Mark an Order as Paid</a></li>
</ul>
</li>
<li><p><a href="#heading-step-8-database-schema-and-migrations">Step 8 — Database Schema and Migrations</a></p>
<ul>
<li><a href="#heading-production-migration-gotcha">Production Migration Gotcha</a></li>
</ul>
</li>
<li><p><a href="#heading-step-9-local-development-setup-docker">Step 9 — Local Development Setup (Docker)</a></p>
<ul>
<li><p><a href="#heading-environment-variables-env">Environment Variables (.env)</a></p>
</li>
<li><p><a href="#heading-docker-compose-local">Docker Compose (Local)</a></p>
</li>
<li><p><a href="#heading-start-services">Start Services</a></p>
</li>
<li><p><a href="#heading-verify-health">Verify Health</a></p>
</li>
<li><p><a href="#heading-test-payment-flow">Test Payment Flow</a></p>
</li>
</ul>
</li>
<li><p><a href="#heading-step-10-production-deployment">Step 10 — Production Deployment</a></p>
<ul>
<li><p><a href="#heading-paypal-live-credentials">PayPal Live Credentials</a></p>
</li>
<li><p><a href="#heading-production-env-on-server-never-commit">Production .env</a></p>
</li>
<li><p><a href="#heading-docker-compose-production">Docker Compose (Production)</a></p>
</li>
<li><p><a href="#heading-deploy-commands">Deploy Commands</a></p>
</li>
<li><p><a href="#heading-verify-production">Verify Production</a></p>
</li>
<li><p><a href="#heading-frontend-domain-in-production">Frontend Domain in Production</a></p>
</li>
</ul>
</li>
<li><p><a href="#heading-step-11-health-checks-and-monitoring">Step 11 — Health Checks and Monitoring</a></p>
</li>
<li><p><a href="#heading-complete-request-flow-real-example">Complete Request Flow (Real Example)</a></p>
</li>
<li><p><a href="#heading-coupon-support-optional">Coupon Support (Optional)</a></p>
</li>
<li><p><a href="#heading-paypal-webhooks-optional-but-recommended">PayPal Webhooks (Optional but Recommended)</a></p>
</li>
<li><p><a href="#heading-testing-checklist">Testing Checklist</a></p>
</li>
<li><p><a href="#heading-wrapping-up">Wrapping Up</a></p>
</li>
<li><p><a href="#heading-further-reading">Further Reading</a></p>
</li>
</ul>
<h2 id="heading-introduction">Introduction</h2>
<p>Payment logic doesn't belong inside every microservice. When you scatter PayPal API calls across <code>user-service</code>, <code>order-service</code>, and <code>billing-service</code>, you end up with:</p>
<ul>
<li><p>Duplicated PayPal credentials and SDK code</p>
</li>
<li><p>Inconsistent error handling and idempotency</p>
</li>
<li><p>Hard-to-audit payment records</p>
</li>
<li><p>Painful environment switching (sandbox to live)</p>
</li>
</ul>
<p>The solution is a dedicated payment microservice that owns all PayPal interactions. Other services call it over gRPC, and payment outcomes are broadcast over RabbitMQ so domain services can update their own data.</p>
<p>This guide walks you through that pattern using a real-world stack:</p>
<table>
<thead>
<tr>
<th>Layer</th>
<th>Technology</th>
</tr>
</thead>
<tbody><tr>
<td>Payment service</td>
<td>NestJS</td>
</tr>
<tr>
<td>Inter-service communication</td>
<td>gRPC</td>
</tr>
<tr>
<td>Event bus</td>
<td>RabbitMQ</td>
</tr>
<tr>
<td>Database</td>
<td>PostgreSQL</td>
</tr>
<tr>
<td>API exposure</td>
<td>API Gateway (HTTP)</td>
</tr>
<tr>
<td>Containerization</td>
<td>Docker Compose</td>
</tr>
<tr>
<td>PayPal API</td>
<td>Orders v2 (Create, Approve, Capture)</td>
</tr>
</tbody></table>
<h2 id="heading-why-use-a-dedicated-payment-service">Why Use a Dedicated Payment Service?</h2>
<p>A dedicated payment service centralizes all payment-related responsibilities in one place. Instead of every microservice communicating directly with PayPal, they simply request payment operations from the payment service.</p>
<p>This service manages PayPal authentication, order creation, payment captures, wallet updates, ledger records, and webhook processing. Meanwhile, domain services remain focused on business logic such as student applications or subscriptions.</p>
<p>Domain services only need to know:</p>
<ol>
<li><p>How much to charge</p>
</li>
<li><p>Who is paying</p>
</li>
<li><p>What business entity the payment is for (<code>referenceId</code>)</p>
</li>
<li><p>Where to redirect the user after payment (<code>returnUrl</code> / <code>cancelUrl</code>)</p>
</li>
</ol>
<p>They do <strong>not</strong> need PayPal credentials.</p>
<h2 id="heading-architecture-overview">Architecture Overview</h2>
<p>Users initiate payments from the Frontend, and requests are routed through the API Gateway to the Students Service. The service uses gRPC to communicate with the Payment Service, which handles all interactions with PayPal.</p>
<p>Once the payment is completed, the Payment Service publishes an event to RabbitMQ, enabling the Students Service to update the payment status asynchronously.</p>
<pre><code class="language-plaintext">┌────────────────────────────────────────────────────────────┐
│                     PRESENTATION LAYER                     │
├────────────────────────────────────────────────────────────┤
│ Frontend (React)                                           │
└───────────────────────┬────────────────────────────────────┘
                        │ HTTP
                        ▼

┌────────────────────────────────────────────────────────────┐
│                       GATEWAY LAYER                        │
├────────────────────────────────────────────────────────────┤
│ student-apigw                                               │
└───────────────────────┬────────────────────────────────────┘
                        │ gRPC
                        ▼

┌────────────────────────────────────────────────────────────┐
│                       DOMAIN LAYER                         │
├────────────────────────────────────────────────────────────┤
│ students-service                                            │
└───────────────────────┬────────────────────────────────────┘
                        │ gRPC
                        ▼

┌────────────────────────────────────────────────────────────┐
│                      PAYMENT LAYER                         │
├────────────────────────────────────────────────────────────┤
│ payment-service                                             │
│                                                            │
│ • Create Payment                                           │
│ • Capture Payment                                          │
│ • Wallet Management                                        │
│ • Ledger                                                   │
│ • Webhooks                                                 │
│ • Event Publishing                                         │
└──────────────┬───────────────────────┬─────────────────────┘
               │                       │
               │ REST                  │ RabbitMQ
               ▼                       ▼

      ┌───────────────┐      ┌────────────────────┐
      │    PayPal     │      │   payment_events   │
      │   Checkout    │      │       Queue        │
      └───────────────┘      └─────────┬──────────┘
                                       │
                                       ▼

                           ┌────────────────────┐
                           │ students-service   │
                           │ Event Consumer     │
                           └────────────────────┘
</code></pre>
<h3 id="heading-payment-state-machine">Payment State Machine</h3>
<p>A payment state machine represents the lifecycle of a payment, tracking its progress from creation to completion (or failure). Each state reflects the current status of the payment, making it easier to monitor, retry, and prevent invalid operations.</p>
<pre><code class="language-plaintext">NOT_STARTED → EXECUTING → SUCCESS
                      └→ FAILED
</code></pre>
<ul>
<li><p><strong>NOT_STARTED</strong> — order record created in DB</p>
</li>
<li><p><strong>EXECUTING</strong> — PayPal order created, waiting for user approval</p>
</li>
<li><p><strong>SUCCESS</strong> — funds captured, ledger updated, event published</p>
</li>
<li><p><strong>FAILED</strong> — capture failed or user cancelled</p>
</li>
</ul>
<h2 id="heading-prerequisites">Prerequisites</h2>
<p>Before you start, make sure you have:</p>
<ul>
<li><p><a href="https://nodejs.org/">Node.js 18+</a></p>
</li>
<li><p><a href="https://docs.docker.com/get-docker/">Docker and Docker Compose</a></p>
</li>
<li><p><a href="https://nestjs.com/">NestJS</a> basics</p>
</li>
<li><p>A <a href="https://developer.paypal.com/">PayPal Developer</a> account</p>
</li>
<li><p>Basic understanding of gRPC and message queues</p>
</li>
</ul>
<h2 id="heading-paypal-concepts-you-need-to-know">PayPal Concepts You Need to Know</h2>
<p>Before integrating PayPal, it's helpful to understand a few core concepts. PayPal provides separate environments for development and production, along with an order-based payment workflow that your application follows.</p>
<h3 id="heading-sandbox-vs-live">Sandbox vs Live</h3>
<table>
<thead>
<tr>
<th>Environment</th>
<th>API Base URL</th>
<th>Checkout URL</th>
</tr>
</thead>
<tbody><tr>
<td>Sandbox (dev)</td>
<td><code>https://api-m.sandbox.paypal.com</code></td>
<td><code>https://www.sandbox.paypal.com/checkoutnow?token=...</code></td>
</tr>
<tr>
<td>Live (prod)</td>
<td><code>https://api-m.paypal.com</code></td>
<td><code>https://www.paypal.com/checkoutnow?token=...</code></td>
</tr>
</tbody></table>
<p>Always develop in <strong>sandbox</strong>. Switch to live only in production.</p>
<h3 id="heading-orders-api-flow-what-we-use">Orders API Flow (What We Use)</h3>
<p>PayPal's Orders v2 API follows three steps:</p>
<ol>
<li><p><strong>Create Order</strong>: your backend creates an order with amount and return URLs</p>
</li>
<li><p><strong>Approve</strong>: user is redirected to PayPal and approves payment</p>
</li>
<li><p><strong>Capture</strong>: your backend captures the approved funds</p>
</li>
</ol>
<p>This is different from the older Payments REST API. Orders v2 is the recommended approach for new integrations.</p>
<h3 id="heading-environment-variables">Environment Variables</h3>
<p>The PayPal service reads its configuration from environment variables. This keeps sensitive credentials out of your source code and makes it easy to switch between sandbox and production environments.</p>
<pre><code class="language-bash">PAYPAL_CLIENT_ID=your_client_id
PAYPAL_CLIENT_SECRET=your_client_secret
PAYPAL_API_BASE=https://api-m.sandbox.paypal.com   # or https://api-m.paypal.com for live
</code></pre>
<p>Never commit real credentials to Git. Use <code>.env</code> files and Docker environment injection.</p>
<h2 id="heading-project-structure">Project Structure</h2>
<pre><code class="language-plaintext">apps/
├── core/
│   └── payment-service/          # Owns all PayPal logic
│       ├── src/
│       │   ├── app/payment/
│       │   │   ├── paypal/paypal.service.ts
│       │   │   ├── payment.service.ts
│       │   │   ├── payment.grpc.controller.ts
│       │   │   ├── payment.http.controller.ts
│       │   │   └── events/payment-events.publisher.ts
│       │   ├── migrations/       # DB schema
│       │   └── routes/health.routes.ts
│       └── Dockerfile
├── services/
│   └── students-service/         # Domain service example
│       └── src/app/payment/
│           ├── payment-client.service.ts      # gRPC client
│           ├── application-payment.service.ts # business logic
│           └── payment-events.consumer.ts     # RabbitMQ listener
└── gateways/
    └── student-apigw/            # HTTP API for frontend
libs/
└── shared/dto/src/lib/payment/
    └── payment.proto             # Shared gRPC contract
</code></pre>
<h2 id="heading-step-1-create-the-payment-service">Step 1 — Create the Payment Service</h2>
<p>The payment service runs two servers in one process</p>
<table>
<thead>
<tr>
<th>Protocol</th>
<th>Port</th>
<th>Purpose</th>
</tr>
</thead>
<tbody><tr>
<td>HTTP</td>
<td>3003</td>
<td>Health checks, webhooks, admin APIs</td>
</tr>
<tr>
<td>gRPC</td>
<td>50061</td>
<td>Internal service-to-service calls</td>
</tr>
</tbody></table>
<p>The payment service exposes both an HTTP server and a gRPC server in the same NestJS application. The HTTP server handles health checks, webhooks, and external requests, while the gRPC server accepts internal requests from other microservices.</p>
<pre><code class="language-typescript">
// apps/core/payment-service/src/main.ts

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // Health route (outside /api prefix)
  app.use('/health', healthRouter);

  // gRPC microservice
  app.connectMicroservice&lt;MicroserviceOptions&gt;({
    transport: Transport.GRPC,
    options: {
      package: 'payment',
      protoPath: join(process.cwd(), 'libs/shared/dto/src/lib/payment/payment.proto'),
      url: `0.0.0.0:${process.env.GRPC_PORT || '50061'}`,
    },
  });

  app.setGlobalPrefix('api');
  await app.startAllMicroservices();
  await app.listen(process.env.PORT || 3003);
}
</code></pre>
<p>During startup, NestJS initializes both servers, allowing external clients and internal services to communicate through the appropriate protocol.</p>
<p><strong>Key design choice:</strong> HTTP is for external/webhook traffic. gRPC is for fast, typed internal calls between services.</p>
<h2 id="heading-step-2-define-the-grpc-contract">Step 2 — Define the gRPC Contract</h2>
<p>Next, you'll create a shared <code>.proto</code> file so all services speak the same language:</p>
<p>A gRPC contract defines the API shared between microservices. Using a <code>.proto</code> file ensures that every service communicates with the payment service using the same request and response structure, regardless of the programming language.</p>
<pre><code class="language-protobuf">// libs/shared/dto/src/lib/payment/payment.proto

syntax = "proto3";
package payment;

service PaymentService {
  rpc CreatePayment(CreatePaymentRequest) returns (CreatePaymentResponse) {}
  rpc CapturePayment(CapturePaymentRequest) returns (CapturePaymentResponse) {}
  rpc GetPaymentStatus(GetPaymentStatusRequest) returns (GetPaymentStatusResponse) {}
  rpc ListPayments(ListPaymentsRequest) returns (ListPaymentsResponse) {}
}

message CreatePaymentRequest {
  string checkout_id = 1;
  string payment_order_id = 2;
  string domain = 3;           // e.g. "application", "subscription"
  string reference_id = 4;     // business entity ID
  string payer_id = 5;
  string amount = 6;
  string currency = 7;
  string buyer_email = 8;
  string seller_account = 9;
  string payment_category = 10;
  string return_url = 11;      // PayPal redirect on success
  string cancel_url = 12;      // PayPal redirect on cancel
  string idempotency_key = 13;
  string metadata = 14;
  string description = 15;
}

message CreatePaymentResponse {
  int32 status = 1;
  string message = 2;
  string payment_order_id = 3;
  string paypal_order_id = 4;
  string approve_url = 5;      // Redirect user here
  string payment_order_status = 6;
}
</code></pre>
<p>The <code>domain</code> + <code>reference_id</code> pair lets one payment service handle payments for applications, subscriptions, university fees, and more without coupling to any single business model.</p>
<h2 id="heading-step-3-implement-the-paypal-service">Step 3 — Implement the PayPal Service</h2>
<p>Now, you'll create a dedicated <code>PayPalService</code> that wraps the PayPal REST API.</p>
<p>Instead of calling the PayPal API throughout the application, we encapsulate all PayPal communication inside a dedicated service. This keeps authentication, order creation, and payment capture logic centralized and easier to maintain.</p>
<pre><code class="language-typescript">// apps/core/payment-service/src/app/payment/paypal/paypal.service.ts

@Injectable()
export class PayPalService {
  private accessToken: string | null = null;
  private tokenExpiresAt = 0;

  private get apiBase(): string {
    return this.configService.get('PAYPAL_API_BASE')
      || 'https://api-m.sandbox.paypal.com';
  }

  // Step 1: Get OAuth access token (cached until expiry)
  private async getAccessToken(): Promise&lt;string&gt; {
    const now = Date.now();
    if (this.accessToken &amp;&amp; now &lt; this.tokenExpiresAt) {
      return this.accessToken;
    }

    const response = await axios.post(
      `${this.apiBase}/v1/oauth2/token`,
      'grant_type=client_credentials',
      {
        auth: {
          username: this.configService.get('PAYPAL_CLIENT_ID'),
          password: this.configService.get('PAYPAL_CLIENT_SECRET'),
        },
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      }
    );

    this.accessToken = response.data.access_token;
    this.tokenExpiresAt = now + (response.data.expires_in - 60) * 1000;
    return this.accessToken;
  }

  // Step 2: Create PayPal checkout order
  async createOrder(input: PayPalCreateOrderInput) {
    const token = await this.getAccessToken();

    const response = await axios.post(
      `${this.apiBase}/v2/checkout/orders`,
      {
        intent: 'CAPTURE',
        purchase_units: [{
          custom_id: input.paymentOrderId,
          description: input.description,
          amount: {
            currency_code: input.currency,
            value: input.amount,
          },
        }],
        application_context: {
          return_url: input.returnUrl,
          cancel_url: input.cancelUrl,
          brand_name: 'YourApp',
          user_action: 'PAY_NOW',
      