---
source_url: https://www.freecodecamp.org/news/what-is-hyde-how-to-improve-rag-with-hypothetical-documents/
ingested: 2026-07-22
sha256: ea70c0f23a9937e08721e48a9cd346670b8c8ebd24e8fe950c8c751142f09c98
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>What Is HyDE? How to Improve RAG with Hypothetical Documents</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/what-is-hyde-how-to-improve-rag-with-hypothetical-documents/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="Retrieval-Augmented Generation, commonly known as RAG, has become one of the most widely used approaches for building applications with large language models. Instead of asking an LLM to answer entire">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="What Is HyDE? How to Improve RAG with Hypothetical Documents">
    
        <meta property="og:description" content="Retrieval-Augmented Generation, commonly known as RAG, has become one of the most widely used approaches for building applications with large language models. Instead of asking an LLM to answer entire">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/what-is-hyde-how-to-improve-rag-with-hypothetical-documents/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/71e96334-b1b2-42db-9f0d-d0d9552acb44.png">
    <meta property="article:published_time" content="2026-07-22T21:32:17.262Z">
    <meta property="article:modified_time" content="2026-07-22T21:32:17.262Z">
    
        <meta property="article:tag" content="RAG ">
    
        <meta property="article:tag" content="AI">
    
        <meta property="article:tag" content="ai agents">
    
        <meta property="article:tag" content="llm">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="What Is HyDE? How to Improve RAG with Hypothetical Documents">
    
        <meta name="twitter:description" content="Retrieval-Augmented Generation, commonly known as RAG, has become one of the most widely used approaches for building applications with large language models. Instead of asking an LLM to answer entire">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/what-is-hyde-how-to-improve-rag-with-hypothetical-documents/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/71e96334-b1b2-42db-9f0d-d0d9552acb44.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Sameer Shukla">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="RAG , AI, ai agents, llm">
    <meta name="twitter:site" content="@freecodecamp">
    
        <meta name="twitter:creator" content="@SameerKShukla">
    

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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/71e96334-b1b2-42db-9f0d-d0d9552acb44.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/what-is-hyde-how-to-improve-rag-with-hypothetical-documents/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-22T21:32:17.262Z",
	"dateModified": "2026-07-22T21:32:17.262Z",
	"keywords": "RAG , AI, ai agents, llm",
	"description": "Retrieval-Augmented Generation, commonly known as RAG, has become one of the most widely used approaches for building applications with large language models.\nInstead of asking an LLM to answer entire",
	"headline": "What Is HyDE? How to Improve RAG with Hypothetical Documents",
	"author": {
		"@type": "Person",
		"name": "Sameer Shukla",
		"url": "https://www.freecodecamp.org/news/author/sshukla/",
		"sameAs": [
			"https://x.com/SameerKShukla"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/res/hashnode/image/upload/v1689436451185/01b582fb-814d-4ef2-8e21-2e92b96e1b27.jpeg",
			"width": 96,
			"height": 96
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-22T21:32:17.262Z">
                            July 22, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/rag/">
                                #RAG 
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">What Is HyDE? How to Improve RAG with Hypothetical Documents</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/res/hashnode/image/upload/v1689436451185/01b582fb-814d-4ef2-8e21-2e92b96e1b27.jpeg 60w" sizes="60px" src="https://cdn.hashnode.com/res/hashnode/image/upload/v1689436451185/01b582fb-814d-4ef2-8e21-2e92b96e1b27.jpeg" class="author-profile-image" alt="Sameer Shukla" width="96" height="96" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/sshukla/" data-test-label="profile-link">
                    
                        Sameer Shukla
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/71e96334-b1b2-42db-9f0d-d0d9552acb44.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/71e96334-b1b2-42db-9f0d-d0d9552acb44.png" alt="What Is HyDE? How to Improve RAG with Hypothetical Documents" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>Retrieval-Augmented Generation, commonly known as RAG, has become one of the most widely used approaches for building applications with large language models.</p>
<p>Instead of asking an LLM to answer entirely from its training data, a RAG system retrieves relevant information from an external knowledge base and provides that information to the model as context.</p>
<p>The basic idea is straightforward:</p>
<ul>
<li><p>Convert the user’s question into an embedding.</p>
</li>
<li><p>Search a vector database for semantically similar document chunks.</p>
</li>
<li><p>Pass the retrieved chunks to an LLM.</p>
</li>
<li><p>Generate an answer grounded in those chunks.</p>
</li>
</ul>
<img src="https://cdn.hashnode.com/uploads/covers/64b2c122c21d916a1b725c11/8cda4575-53dc-4531-8f7b-6c930bd743e4.png" alt=" Figure1:  Retrieval-Augmented Generation (RAG) workflow " style="display:block;margin-left:auto" width="600" height="400" loading="lazy">

<p>But this apparently simple process has a major weakness: the user’s question and the document containing the answer may be written very differently.</p>
<p>A user might ask:</p>
<blockquote>
<p>Why does my AWS Glue job become significantly slower after processing several million records?</p>
</blockquote>
<p>The relevant document in the knowledge base might say:</p>
<blockquote>
<p>Performance degradation can occur when Spark executors experience excessive shuffle operations, skewed partitions, memory pressure, or repeated spilling to disk.</p>
</blockquote>
<p>The query and the document discuss the same problem, but they use different vocabulary, structure, and levels of detail. A direct query embedding may therefore fail to place them close enough in the embedding space.</p>
<p>This is the problem that Hypothetical Document Embeddings, or HyDE, was designed to solve.</p>
<h2 id="heading-table-of-contents"><strong>Table of Contents</strong></h2>
<ul>
<li><p><a href="#heading-prerequisites">Prerequisites</a></p>
</li>
<li><p><a href="#heading-what-is-hyde">What is HyDE?</a></p>
</li>
<li><p><a href="#heading-the-mechanics-of-hyde">The Mechanics of HyDE</a></p>
</li>
<li><p><a href="#heading-minimal-implementation">Minimal Implementation</a></p>
</li>
<li><p><a href="#heading-why-hallucination-doesnt-automatically-break-hyde">Why Hallucination Doesn't Automatically Break HyDE</a></p>
</li>
<li><p><a href="#heading-production-guardrails">Production Guardrails</a></p>
</li>
<li><p><a href="#heading-summary">Summary</a></p>
</li>
</ul>
<h2 id="heading-prerequisites"><strong>Prerequisites</strong></h2>
<p>To get the most out of this article, there are a few things you should know and have.</p>
<p>What you need to know:</p>
<ul>
<li><p>Basic familiarity with <a href="https://www.freecodecamp.org/news/rag-explained-simply-with-a-real-project/">RAG and why it's used</a>.</p>
</li>
<li><p>How vector embeddings work, at a conceptual level.</p>
</li>
<li><p>Working knowledge of Python.</p>
</li>
</ul>
<p>What you need to have:</p>
<ul>
<li><p>A local Python environment with numpy, sentence-transformers, and Anthropic installed</p>
</li>
<li><p>An Anthropic API key if you want to run the HyDE code sample (available at <a href="http://console.anthropic.com">console.anthropic.com</a>)</p>
</li>
</ul>
<h2 id="heading-what-is-hyde"><strong>What is HyDE?</strong></h2>
<p>HyDE stands for Hypothetical Document Embeddings. The technique is simple. At query time, you prompt an LLM to generate a hypothetical document that would answer the user's question, embed that document instead of the query, and use its vector to search your index. That's the whole idea. Everything else is engineering.</p>
<img src="https://cdn.hashnode.com/uploads/covers/64b2c122c21d916a1b725c11/50c5909c-c7fa-4c92-bf11-c7a1b3411142.png" alt="50c5909c-c7fa-4c92-bf11-c7a1b3411142" style="display:block;margin-left:auto" width="600" height="400" loading="lazy">

<p>Figure 2: The HyDE process</p>
<p>The hypothetical document isn't treated as the final answer. It's used only as a bridge between the user’s query and the real documents stored in the knowledge base.</p>
<p>This distinction is critical.</p>
<p>The generated document may contain incorrect details. That's not necessarily a failure, because the system doesn't present it directly to the user. Its purpose is to produce a richer semantic representation of the information being sought.</p>
<p>The original HyDE approach used a language model to generate hypothetical documents and an unsupervised dense retriever to map those documents into an embedding space. The embedding acts as a search instruction for retrieving real documents from the corpus.</p>
<h3 id="heading-why-hyde-works">Why HyDE Works</h3>
<p>The intuition is geometric. A dense retriever projects text into a semantic space, and similarity between two pieces of text is the cosine of the angle between their vectors.</p>
<p>When you embed a question and compare it to a passage, you're measuring an angle between two shapes of text that were never meant to be close. Your embedding model was trained to place semantically similar text near each other, but it wasn't trained to place a question near its answer. Those are different geometries.</p>
<p>HyDE closes that gap by making both sides of the comparison the same shape. The hypothetical passage sits in the same neighborhood of the vector space as real documentation, because it was written in the same register, with the same vocabulary, at the same level of detail. The vector search is now comparing answers to answers rather than questions to answers, and the similarity signal is cleaner.</p>
<p>That's the entire mechanism. Everything else – the prompt engineering, model selection, and caching – is downstream of this one geometric fact.</p>
<h2 id="heading-the-mechanics-of-hyde"><strong>The Mechanics of HyDE</strong></h2>
<p>First, let's say that the user asks: why does my Lambda function take longer to respond when it hasn't been called in a while?</p>
<p>Then you ask the LLM that question in a short prompt: "Write a passage from technical documentation that answers this question."</p>
<p>The LLM responds with something like:</p>
<blockquote>
<p>"AWS Lambda will reclaim execution environments that have been idle for some time. When the function is invoked again, a cold start occurs, which involves setting up the runtime and loading dependencies. This adds additional latency for the first invocation following an idle period."</p>
</blockquote>
<p>Now you embed that generated passage. Not the original question –&nbsp;the passage.</p>
<p>You use that embedding to search your vector store. The hypothetical passage was formatted like a real doc, so now the real AWS docs on cold starts are near each other in the vector space.</p>
<p>Next, you take the top k retrieved documents and pass them to the generator, along with the original user question. The generator answers using the real docs it retrieved. The hypothetical is discarded.</p>
<p>The LLM was used twice, but for different jobs: once to rewrite the query as a document, and again to answer the question using retrieved documents. The first call is cheap and low stakes. The second is the one that matters.</p>
<img src="https://cdn.hashnode.com/uploads/covers/64b2c122c21d916a1b725c11/b8fb1260-392c-4248-bcea-1328813dfe7d.png" alt="Figure3:  Comparison of Naive RAG and HyDE pipelines. " style="display:block;margin:0 auto" width="600" height="400" loading="lazy">

<p>Figure3: &nbsp;Comparison of Naïve RAG and HyDE pipelines.</p>
<h2 id="heading-minimal-implementation">Minimal Implementation</h2>
<p>The naïve RAG may look like this:</p>
<pre><code class="language-python">import numpy as np
from sentence_transformers import SentenceTransformer

collection = [
    "AWS Lambda reclaims idle execution environments after a period of inactivity, causing a cold start on the next invocation that includes runtime bootstrap and dependency loading.",
    "Apache Airflow schedules tasks using a directed acyclic graph, where each node represents a unit of work.",
    "AWS Glue crawlers infer schemas from source data and populate the Glue Data Catalog automatically.",
    "Amazon Bedrock exposes foundation models behind a single API and handles provisioning transparently.",
    "DynamoDB partitions data across nodes using the partition key, which determines physical placement.",
]

embedder = SentenceTransformer("all-MiniLM-L6-v2")
collection_embeddings = embedder.encode(collection, normalize_embeddings=True)

def retrieve(query: str, k: int = 2) -&gt; list[str]:
    query_embedding = embedder.encode(query, normalize_embeddings=True)
    scores = collection_embeddings @ query_embedding
    top_k = np.argsort(scores)[::-1][:k]
    return [collection[i] for i in top_k]

query = "Why does my Lambda function take longer to respond when it hasn't been called in a while?"
for passage in retrieve(query):
    print(passage)
</code></pre>
<p>On this sample collection, it will likely return the right passage at rank 1. Scale to fifty thousand documents with real query variance, and the correct passage starts sliding down the ranking.</p>
<p>The line to notice, for what comes next, is the one inside retrieve where <code>embedder.encode(query, ...)</code> runs. That's where the raw question becomes a vector, and this is the line HyDE changes.</p>
<p>In the HyDE variant, the delta is one function:</p>
<pre><code class="language-python">import numpy as np
from anthropic import Anthropic
from sentence_transformers import SentenceTransformer

# collection. In production this is your vector store.

collection = [
    "AWS Lambda reclaims idle execution environments after a period of inactivity, causing a cold start on the next invocation that includes runtime bootstrap and dependency loading.",
    "Apache Airflow schedules tasks using a directed acyclic graph, where each node represents a unit of work.",
    "AWS Glue crawlers infer schemas from source data and populate the Glue Data Catalog automatically.",
    "Amazon Bedrock exposes foundation models behind a single API and handles provisioning transparently.",
    "DynamoDB partitions data across nodes using the partition key, which determines physical placement.",
]

embedder = SentenceTransformer("all-MiniLM-L6-v2")
corpus_embeddings = embedder.encode(collection, normalize_embeddings=True)

client = Anthropic()

# HyDE: generate a hypothetical answer, embed that, then search.

HYDE_PROMPT = (
    "Write a short passage from technical documentation that would answer "
    "the following question. Write in the register of official docs: "
    "declarative, precise, no hedging. Do not include the question itself. "
    "Passage only, two to four sentences.\n\n"
    "Question: {query}"
)

def generate_hypothetical(query: str) -&gt; str:
    """Ask an LLM to write a fake documentation passage answering the query."""
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=200,
        messages=[
            {"role": "user", "content": HYDE_PROMPT.format(query=query)}
        ],
    )
    return message.content[0].text

def retrieve_hyde(query: str, k: int = 2) -&gt; list[str]:
    """Generate a hypothetical passage, embed it, and search with that vector."""
    hypothetical = generate_hypothetical(query)
    hyde_embedding = embedder.encode(hypothetical, normalize_embeddings=True)
    scores = corpus_embeddings @ hyde_embedding
    top_k_indices = np.argsort(scores)[::-1][:k]
    return [collection[i] for i in top_k_indices]

if __name__ == "__main__":
    query = (
        "Why does my Lambda function take longer to respond "
        "when it hasn't been called in a while?"
    )
    for passage in retrieve_hyde(query):
        print(passage)
</code></pre>
<p>That's the whole technique. There's one extra LLM call, one extra function, and everything else is identical to the baseline. The hypothetical text is thrown away after embedding and never reaches the generator.</p>
<p>The naïve baseline vectorizes the question directly and performs the cosine similarity search on the collection vectors. It's precisely this one-line code, which invokes <code>embedder.encode(query, ...)</code>, where the question is vectorized into a vector of question shape rather than an answer vector shape, and it's the sole cause of the retrieval quality issue discussed in this article.</p>
<p>The difference in the HyDE approach is made in one thing only. Before the embedding takes place, an LLM is asked to generate a small piece of text in the register of technical documentation answering the question, and the vector is computed for this text rather than for the original question. Everything else remains exactly the same – the same embedding model, cosine similarity search, and top-k selections are used.</p>
<p>This hypothetical passage is never used for anything other than for generating the search vector. The difference isn't made by any difference in the retrieval method but only by changing the shape of the text to compare.</p>
<h2 id="heading-why-hallucination-doesnt-automatically-break-hyde">Why Hallucination Doesn't Automatically Break HyDE</h2>
<p>At first, HyDE appears contradictory. Why would a system improve factual retrieval by asking a language model to generate information before retrieving the facts?</p>
<p>The answer is that HyDE uses the generated document as a retrieval representation, not as trusted knowledge.</p>
<p>Suppose the user asks: What caused the database outage on July 18? The LLM can't know the actual cause from a private incident report. It has to make something up.</p>
<p>So it might say something like,</p>
<blockquote>
<p>"The July 18 database outage was caused by a misconfiguration of the failover on the primary replica, which caused cascading connection timeouts in the dependent services. Engineers restored service by rerouting traffic to the secondary region and rebuilding the connection pool."</p>
</blockquote>
<p>That passage is a complete fabrication. The real cause might have been a disk failure, a bad deploy, a certificate expiry, anything. But look at what the passage contains: words like outage, failover, replica, cascading timeout, connection pool, secondary region. Those are the exact words that will appear in your real incident postmortem, whatever the actual cause was.</p>
<p>Postmortems for database outages sound like postmortems for database outages. They share vocabulary, register, and structure regardless of the specific root cause.</p>
<p>The LLM's generated passage might also touch on connection saturation, lock contention, storage latency, failed deployment, or resource exhaustion. Some of those details may be wrong, but it doesn't matter. Each of those terms still pulls the embedding toward the same neighborhood as real outage analyses, root cause reports, database metrics, and postmortem documents.</p>
<p>When you embed that fabricated passage, the vector lands in the neighborhood where your real postmortem lives. The vector search retrieves the correct postmortem. Only then does the generator read the actual document and produce the true answer.</p>
<p>The hypothetical was wrong about the facts, but it was right about the shape. Shape is what the embedding sees. Facts are what the retrieved document provides.</p>
<p>The real risk here isn't the hallucination itself but what you do with it. If the system mistakenly passes the hypothetical document to the final answer generator as though it were retrieved evidence, the fabrication reaches the user.</p>
<p>The mitigation is architectural, not statistical: keep the hypothetical strictly inside the retrieval step and never let it leak into the generation context. The next section covers this in detail.</p>
<h2 id="heading-production-guardrails">Production Guardrails</h2>
<p>HyDE adds an LLM to the retrieval path, which introduces new engineering concerns. Here are some production guardrails you can add that'll make things safer and more reliable:</p>
<h3 id="heading-apply-timeouts-and-fallbacks">Apply Timeouts and Fallbacks</h3>
<p>If hypothetical generation is slow or fails, degrade to naïve retrieval instead of blocking the user.</p>
<pre><code class="language-python">def retrieve_with_fallback(query: str, k: int = 2) -&gt; list[str]:
    try:
        hypothetical = generate_hypothetical(query)
        search_vector = embedder.encode(hypothetical, normalize_embeddings=True)
    except Exception:
        logger.exception(
            "HyDE generation failed; falling back to the original query."
        ) 
        # Fall back to embedding the raw query
        search_vector = embedder.encode(query, normalize_embeddings=True)

    scores = corpus_embeddings @ search_vector
    top_k = np.argsort(scores)[::-1][:k]
    return [collection[i] for i in top_k]
</code></pre>
<p>Set an explicit timeout on the client itself [Anthropic(timeout=3.0)]</p>
<h3 id="heading-limit-generation-length">Limit Generation Length</h3>
<p>Long hypothetical documents introduce unrelated concepts and dilute the embedding. Cap the output at the LLM call.</p>
<pre><code class="language-python">message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=200,   # keep the hypothetical dense
    messages=[{"role": "user", "content": HYDE_PROMPT.format(query=query)}],
)
</code></pre>
<p>200 tokens should be sufficient for a targeted piece of text in the domain of technical documentation. Anything beyond that typically makes retrieval harder.</p>
<h3 id="heading-protect-sensitive-data-before-sending-to-an-external-model-provider">Protect Sensitive Data Before Sending to an External Model Provider</h3>
<p>Strip personal identification data from the input before running the hypothesis generation, and enforce it at the interface level instead of relying on downstream callers.</p>
<pre><code class="language-python">PII_PATTERNS = {
    "email": r'\b[\w.-]+@[\w.-]+\.\w+\b',
    "ssn":   r'\b\d{3}-\d{2}-\d{4}\b',
    "card":  r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b',
}

def scrub_pii(text: str) -&gt; str:
    for label, pattern in PII_PATTERNS.items():
        text = re.sub(pattern, f"[REDACTED_{label.upper()}]", text)
    return text

def safe_generate_hypothetical(query: str) -&gt; str:
    return generate_hypothetical(scrub_pii(query))
</code></pre>
<p>This will be the lowest requirement for regulated data. Add more controls above it.</p>
<h3 id="heading-trace-every-stage">Trace Every Stage</h3>
<p>Without visibility at every stage, there's no way to debug retrieval problems. Collect the query, prompt, hypothetical response, delays, IDs retrieved, and similarity scores for all queries.</p>
<pre><code class="language-python">import time
import logging

logger = logging.getLogger(__name__)

def traced_retrieve_hyde(query: str, k: int = 2) -&gt; HyDEContext:
    t0 = time.time()
    hypothetical = generate_hypothetical(query)
    gen_ms = int((time.time() - t0) * 1000)

    t1 = time.time()
    search_vector = embedder.encode(hypothetical, normalize_embeddings=True)
    embed_ms = int((time.time() - t1) * 1000)

    scores = corpus_embeddings @ search_vector
    top_k = np.argsort(scores)[::-1][:k]

    logger.info(
        "hyde_retrieval",
        extra={
            "query": query,
            "prompt_version": "v1",
            "hypothetical": hypothetical,
            "gen_latency_ms": gen_ms,
            "embed_latency_ms": embed_ms,
            "retrieved_ids": top_k.tolist(),
            "similarity_scores": [float(scores[i]) for i in top_k],
        },
    )
    return HyDEContext(
        original_query=query,
        hypothetical=hypothetical,
        retrieved_documents=[collection[i] for i in top_k],
    )
</code></pre>
<p>The structured log forms the basis for latency dashboards, drift alerts, and offline retrieval evaluations.</p>
<h3 id="heading-when-to-use-hyde-and-when-not-to">When to Use HyDE, and When Not to</h3>
<p>Use HyDE when:</p>
<ul>
<li><p>Your embedding model fails to fully grasp your domain.</p>
</li>
<li><p>You don’t have labeled query-document pairs to fine-tune a retriever.</p>
</li>
<li><p>Users ask conversational questions, but your documents are formal or technical.</p>
</li>
<li><p>You can afford an extra LLM call before retrieval.</p>
</li>
</ul>
<p>Avoid HyDE if:</p>
<ul>
<li><p>Your application has strict latency requirements.</p>
</li>
<li><p>A general-purpose LLM may generate the wrong domain terminology.</p>
</li>
<li><p>Your queries already contain strong keywords, identifiers, or error codes.</p>
</li>
<li><p>BM25 or hybrid search already retrieves relevant results.</p>
</li>
<li><p>You have enough label