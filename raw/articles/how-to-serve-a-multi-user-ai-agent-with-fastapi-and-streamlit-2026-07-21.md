---
source_url: https://www.freecodecamp.org/news/how-to-serve-a-multi-user-ai-agent-with-fastapi-and-streamlit/
ingested: 2026-07-21
sha256: 122d35af2d98cd365bb98f622a0f450478907a0e933a5d8ee0208e473ad8c8b0
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Serve a Multi-User AI Agent with FastAPI and Streamlit</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-to-serve-a-multi-user-ai-agent-with-fastapi-and-streamlit/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="In this tutorial, I’ll show you how to serve a multi-user local AI agent as a REST API using FastAPI, then add a lightweight Streamlit UI on top. Instead of interacting with the agent through a termin">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Serve a Multi-User AI Agent with FastAPI and Streamlit">
    
        <meta property="og:description" content="In this tutorial, I’ll show you how to serve a multi-user local AI agent as a REST API using FastAPI, then add a lightweight Streamlit UI on top. Instead of interacting with the agent through a termin">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-to-serve-a-multi-user-ai-agent-with-fastapi-and-streamlit/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/e5bf4093-e618-4388-954c-f1a49bc87cfe.png">
    <meta property="article:published_time" content="2026-07-20T22:07:49.427Z">
    <meta property="article:modified_time" content="2026-07-20T22:07:49.427Z">
    
        <meta property="article:tag" content="AI">
    
        <meta property="article:tag" content="ai-agent">
    
        <meta property="article:tag" content="ollama">
    
        <meta property="article:tag" content="#qwen">
    
        <meta property="article:tag" content="FastAPI">
    
        <meta property="article:tag" content="api">
    
        <meta property="article:tag" content="streamlit">
    
        <meta property="article:tag" content="UI">
    
        <meta property="article:tag" content="Python">
    
        <meta property="article:tag" content="llm">
    
        <meta property="article:tag" content="streaming">
    
        <meta property="article:tag" content="chatgpt">
    
        <meta property="article:tag" content="agentic">
    
        <meta property="article:tag" content="Streaming API">
    
        <meta property="article:tag" content="langgraph">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Serve a Multi-User AI Agent with FastAPI and Streamlit">
    
        <meta name="twitter:description" content="In this tutorial, I’ll show you how to serve a multi-user local AI agent as a REST API using FastAPI, then add a lightweight Streamlit UI on top. Instead of interacting with the agent through a termin">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-to-serve-a-multi-user-ai-agent-with-fastapi-and-streamlit/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/e5bf4093-e618-4388-954c-f1a49bc87cfe.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Darsh Shah">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="AI, ai-agent, ollama, #qwen, FastAPI, api, streamlit, UI, Python, llm, streaming, chatgpt, agentic, Streaming API, langgraph">
    <meta name="twitter:site" content="@freecodecamp">
    

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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/e5bf4093-e618-4388-954c-f1a49bc87cfe.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-to-serve-a-multi-user-ai-agent-with-fastapi-and-streamlit/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-20T22:07:49.427Z",
	"dateModified": "2026-07-20T22:07:49.427Z",
	"keywords": "AI, ai-agent, ollama, FastAPI, api, streamlit, UI, Python, llm, streaming, chatgpt, agentic, Streaming API, langgraph",
	"description": "In this tutorial, I’ll show you how to serve a multi-user local AI agent as a REST API using FastAPI, then add a lightweight Streamlit UI on top.\nInstead of interacting with the agent through a termin",
	"headline": "How to Serve a Multi-User AI Agent with FastAPI and Streamlit",
	"author": {
		"@type": "Person",
		"name": "Darsh Shah",
		"url": "https://www.freecodecamp.org/news/author/darshs/",
		"sameAs": [
			"https://darshshah.org"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/uploads/avatars/684c95e159698b4bf6a0e4be/1551f7e1-25fa-44ea-aaee-25b5fa4377a9.jpg",
			"width": 2954,
			"height": 2057
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-20T22:07:49.427Z">
                            July 20, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/ai/">
                                #AI
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Serve a Multi-User AI Agent with FastAPI and Streamlit</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/uploads/avatars/684c95e159698b4bf6a0e4be/1551f7e1-25fa-44ea-aaee-25b5fa4377a9.jpg 60w" sizes="60px" src="https://cdn.hashnode.com/uploads/avatars/684c95e159698b4bf6a0e4be/1551f7e1-25fa-44ea-aaee-25b5fa4377a9.jpg" class="author-profile-image" alt="Darsh Shah" width="2954" height="2057" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/darshs/" data-test-label="profile-link">
                    
                        Darsh Shah
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/e5bf4093-e618-4388-954c-f1a49bc87cfe.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/e5bf4093-e618-4388-954c-f1a49bc87cfe.png" alt="How to Serve a Multi-User AI Agent with FastAPI and Streamlit" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>In this tutorial, I’ll show you how to serve a multi-user local AI agent as a REST API using FastAPI, then add a lightweight Streamlit UI on top.</p>
<p>Instead of interacting with the agent through a terminal, we’ll expose it over HTTP so multiple users can access it through a chat-style frontend interface. Each session will maintain its own conversation history and streamed responses.</p>
<p>The local AI agent will be built with LangChain v1, Ollama, Qwen, and Python, running on your own machine and ready to plug into larger applications without any per-call model API charges.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-background">Background</a></p>
</li>
<li><p><a href="#heading-what-is-fastapi">What is FastAPI</a>?</p>
</li>
<li><p><a href="#heading-what-is-streamlit">What is Streamlit</a>?</p>
</li>
<li><p><a href="#heading-what-is-multi-user-support">What Is Multi-User Support</a>?</p>
</li>
<li><p><a href="#heading-motivation-and-architecture">Motivation and Architecture</a></p>
</li>
<li><p><a href="#heading-step-1-install-ollama-and-pull-the-model">Step 1: Install Ollama and Pull the Model</a></p>
</li>
<li><p><a href="#heading-step-2-install-python-dependencies">Step 2: Install Python Dependencies</a></p>
</li>
<li><p><a href="#heading-step-3-build-the-agent-and-api-layer-with-fastapi">Step 3: Build the agent and API layer with FastAPI</a></p>
</li>
<li><p><a href="#heading-step-4-build-streamlit-ui">Step 4: Build Streamlit UI</a></p>
</li>
<li><p><a href="#heading-step-5-run-the-backend-app">Step 5: Run the backend app</a></p>
</li>
<li><p><a href="#heading-step-6-run-the-frontend-app">Step 6: Run the frontend app</a></p>
</li>
<li><p><a href="#heading-sample-output">Sample Output</a></p>
</li>
<li><p><a href="#heading-what-to-improve-before-production">What to Improve Before Production</a></p>
</li>
<li><p><a href="#heading-conclusion">Conclusion</a></p>
</li>
</ul>
<h2 id="heading-background">Background</h2>
<p>Many AI agents start out as simple Python scripts that run in a command-line terminal. You type a message, the agent responds, and everything happens in a single local session.</p>
<p>That setup is great for development and testing, but it becomes limiting when you want other people or applications to interact with the agent.</p>
<p>To make an AI agent truly useful, we need to expose it through an interface that other users can access. A REST API is a practical way to do that.</p>
<p>To follow this tutorial, you'll need Ollama installed on your machine. The tutorial works on macOS, Windows, and Linux. I'm using a MacBook Pro with 32 GB of RAM, but you can run this on a lower-memory machine by choosing a smaller Qwen model from Ollama.</p>
<h2 id="heading-what-is-fastapi"><strong>What is FastAPI?</strong></h2>
<p><a href="https://github.com/fastapi/fastapi">FastAPI</a> is a Python web framework for building APIs. In this tutorial, it gives us a simple way to expose the agent over HTTP so other apps, scripts, or services can call it.</p>
<p>FastAPI is a good fit for AI apps because it gives us a clean boundary around the system. We define the request and response models in Python, FastAPI validates them automatically, and it turns HTTP requests into Python objects and Python objects back into JSON. It also generates interactive API docs for free and supports async endpoints, which is useful for AI workloads that may take longer to respond.</p>
<h2 id="heading-what-is-streamlit"><strong>What is Streamlit?</strong></h2>
<p><a href="https://streamlit.io">Streamlit</a> is a Python framework for building lightweight web interfaces with minimal frontend work. It lets us create interactive browser-based apps using normal Python code instead of HTML, CSS, and JavaScript.</p>
<p>In this tutorial, Streamlit sits on top of the FastAPI backend as a thin client. FastAPI exposes the AI agent over HTTP, and Streamlit gives us a simple UI for calling that API and displaying the results. That separation keeps the backend reusable while still making the agent easy to use in the browser.</p>
<h2 id="heading-what-is-multi-user-support"><strong>What Is Multi-User Support?</strong></h2>
<p>Multi-user support means the AI agent can handle requests from more than one user while keeping each user’s session separate.</p>
<p>For example, User 1&nbsp;asks the agent one question and User 2&nbsp;asks a different question. The agent should remember the correct context for each user independently. Without multi-user support, all users may end up sharing the same conversation state, which can lead to mixed responses, incorrect memory, or overwritten context.</p>
<h2 id="heading-motivation-and-architecture"><strong>Motivation and Architecture</strong></h2>
<p>Turning an AI agent into an API is the natural next step after building it locally. A Python script is great for experimenting, but an API makes the agent reusable. And adding multi-user support makes the agent extensible to be used by others.</p>
<p>To keep things simple, we’ll use a small local agent powered by Ollama and Qwen. The agent has two tools: one for checking the current time and another for counting words.</p>
<p>FastAPI provides the HTTP layer by exposing one endpoint called <code>/chat/stream</code>. When the request comes in with a user message, Pydantic validates the request, LangChain handles the agent loop and tool calling, and the final answer is returned as stream. Streamlit sits on top of that API and acts as a frontend that sends requests to the API and displays the results.</p>
<img src="https://cdn.hashnode.com/uploads/covers/684c95e159698b4bf6a0e4be/21a2b03d-b4c3-4211-82b1-aa265ac6fb1e.png" alt="image showing the sequence diagram of user calling the streamlit UI. The it goes to FastAPI layer, then to AI agent and finally Qwen and tool calls" style="display:block;margin:0 auto" width="1478" height="1000" loading="lazy">

<p>Example request:</p>
<pre><code class="language-json">{ 
    "message": "How many words are in: LangChain makes tool calling easier",
    "user_id":"123e4567-e89b-12d3-a456-426614174000"
 }
</code></pre>
<p>Example response:</p>
<pre><code class="language-json">{
  "answer": "There are **5** words in LangChain makes tool calling easier."
}
</code></pre>
<p>The model runs locally through Ollama, so there are no per-call model API charges.</p>
<h2 id="heading-step-1-install-ollama-and-pull-the-model"><strong>Step 1: Install Ollama and Pull the Model</strong></h2>
<p>To get started, install the Ollama application for your platform.</p>
<p>We’ll use Qwen as the chat model. I’m using <code>qwen3.5:4b</code>. If your machine has less RAM, you can use <code>qwen3.5:0.8b</code> instead.</p>
<pre><code class="language-plaintext">ollama pull qwen3.5:4b
</code></pre>
<h2 id="heading-step-2-install-python-dependencies"><strong>Step 2: Install Python Dependencies</strong></h2>
<p>Create a virtual environment and install the required packages:</p>
<pre><code class="language-plaintext">python3 -m venv venv
source venv/bin/activate

pip install fastapi uvicorn streamlit requests langchain langchain-core langchain-ollama langgraph
</code></pre>
<p>If tutorial requires LangChain &gt;= 1.0.0.</p>
<h2 id="heading-step-3-build-the-agent-and-api-layer-with-fastapi">Step 3: <strong>Build the Agent and API Layer with FastAPI</strong></h2>
<p>This application has three main responsibilities. FastAPI exposes the HTTP endpoint, Pydantic validates the incoming request data, and LangChain runs the agent, including tool calling and short-term memory.</p>
<p>The <code>user_id</code> sent with each request is used as the thread identifier, allowing the checkpointer to keep each user’s conversation history separate. This memory is per session. So every new session will have its own memory.</p>
<p>Another important detail is that the agent is created only once at startup with <code>agent = build_agent()</code>. Reusing the same agent instance avoids rebuilding the model and tool list for every request, which reduces overhead and improves response times while still supporting multiple users.</p>
<p>Inside the <code>/chat/stream</code> endpoint, the backend uses <a href="https://docs.langchain.com/oss/python/langchain/event-streaming">LangChain’s</a> <code>stream_events(..., version="v3")</code> to generate the response as a stream instead of waiting for the full answer all at once. FastAPI then wraps that stream in a <code>StreamingResponse</code>, so the frontend can receive the output gradually as it's produced. This makes the app feel much more interactive, because users can start reading the answer immediately while the rest is still being generated.</p>
<p>Put together, this gives you a lightweight backend that validates input, preserves separate memory for each user, and streams responses to the UI in real time.</p>
<p>Save the following code as <code>app.py</code>:</p>
<pre><code class="language-python">from datetime import datetime
from uuid import UUID

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse

from pydantic import BaseModel

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver

CHAT_MODEL = "qwen3.5:4b"

SYSTEM_PROMPT = (
    "You are a helpful assistant with access to tools for getting the current time "
    "and counting words in text. "
    "Use tools when needed. If the question does not need a tool, answer directly."
)

# -----------------------------
# Request model
# -----------------------------

class ChatRequest(BaseModel):
    user_id: UUID
    message: str

# -----------------------------
# Tools
# -----------------------------

@tool
def current_time() -&gt; str:
    """Return the current local date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@tool
def word_count(text: str) -&gt; int:
    """Count the number of words in a piece of text."""
    return len(text.split())


# -----------------------------
# Agent + checkpoint memory
# -----------------------------

# Store conversation history in short term memory
checkpointer = InMemorySaver()

def build_agent():
    model = ChatOllama(model=CHAT_MODEL, temperature=0)
    return create_agent(
        model=model,
        tools=[current_time, word_count],
        system_prompt=SYSTEM_PROMPT,
        checkpointer=checkpointer,
    )


agent = build_agent()

# -----------------------------
# Streaming endpoint
# -----------------------------

app = FastAPI()

@app.post("/chat/stream")
def chat_stream(req: ChatRequest):
    def generate():
        run = agent.stream_events(
            {
                "messages": [{"role": "user", "content": req.message}],
            },
            config={
                "configurable": {
                    # Keep each user's short-term memory isolated
                    # by using their user_id as the thread ID.
                    "thread_id": str(req.user_id),
                }
            },
            version="v3",
        )

        for message in run.messages:
            for token in message.text:
                yield token

    return StreamingResponse(generate(), media_type="text/plain")
</code></pre>
<h2 id="heading-step-4-build-streamlit-ui">Step 4: Build Streamlit UI</h2>
<p>The Streamlit code creates a simple chat interface for the AI agent and keeps each browser session tied to a unique user_id.</p>
<p>When the app first loads, it generates and stores a UUID in st.session_state, which is later sent to the backend so the agent can keep that user’s conversation history separate from other users. It also creates a chat_history list in session state so previous messages remain visible every time Streamlit reruns the script. The app then loops through that saved history and displays each message in a chat-style format using st.chat_message().</p>
<p>When the user enters a new message through st.chat_input(), the app immediately saves and displays it, then sends it to the backend API with a POST request to <code>http://127.0.0.1:8001/chat/stream</code> along with the session’s user_id.</p>
<p>The request is made with stream=True, which allows the response to arrive gradually instead of all at once. As each chunk of text is received from the backend, the code appends it to full_answer and updates a placeholder on the page, creating a live streaming effect. Once the response is complete, the final assistant message is stored in chat_history so it remains part of the conversation on the page</p>
<p>Save the below as <code>streamlit_app.py</code></p>
<pre><code class="language-python">import uuid
import requests
import streamlit as st

API_URL = "http://127.0.0.1:8001/chat/stream"

st.title("Local AI Agent")

if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show previous messages
for item in st.session_state.chat_history:
    with st.chat_message(item["role"]):
        st.markdown(item["content"])

message = st.chat_input("Enter a message")

if message:
    # Save and show user message
    st.session_state.chat_history.append({"role": "user", "content": message})
    with st.chat_message("user"):
        st.markdown(message)

    # Stream assistant response
    full_answer = ""
    with st.chat_message("assistant"):
        placeholder = st.empty()

        # Send the reqeust to backend API via POST request
        with requests.post(
            API_URL,
            json={
                "message": message,
                "user_id": st.session_state.user_id,
            },
            stream=True,
        ) as response:
            response.raise_for_status()

            for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
                if chunk:
                    full_answer += chunk
                    placeholder.markdown(full_answer)

    # Save final assistant response
    st.session_state.chat_history.append(
        {"role": "assistant", "content": full_answer}
    )
</code></pre>
<h2 id="heading-step-5-run-the-backend-app">Step 5: Run the Backend App</h2>
<p>Start the server with Uvicorn:</p>
<pre><code class="language-bash">uvicorn app:app --reload --port 8001
</code></pre>
<p>Once the application starts, open:</p>
<ul>
<li><p><code>http://127.0.0.1:8001/</code></p>
</li>
<li><p><code>http://127.0.0.1:8001/docs</code></p>
</li>
</ul>
<p>The <code>/docs</code> endpoint is automatically generated by FastAPI using your Pydantic models. It provides an interactive interface where you can test the API without writing any client code.</p>
<img src="https://cdn.hashnode.com/uploads/covers/684c95e159698b4bf6a0e4be/5cf32ff0-273c-47cd-80be-ebf807e4443d.png" alt="Api docs that was generated by FastAPI. It includes /chat/stream  endpoint and schema" style="display:block;margin:0 auto" width="2712" height="1034" loading="lazy">

<p>You can send requests directly from <code>curl</code>. In your terminal, run these commands to invoke the API for the AI agent and check the output:</p>
<pre><code class="language-bash">$ curl -X POST http://127.0.0.1:8001/chat/stream \
  -H "Content-Type: application/json" \
  -d '{"message":"What time is it?","user_id":"123e4567-e89b-12d3-a456-426614174000"}'

$ curl -X POST http://127.0.0.1:8001/chat/stream \
  -H "Content-Type: application/json" \
  -d '{"message":"How many words are in: LangChain makes tool calling easier","user_id":"123e4567-e89b-12d3-a456-426614174000"}'

$ curl -X POST "http://127.0.0.1:8001/chat/stream" \
-H "Content-Type: application/json" \
-d '{"message":"What is the capital of France?","user_id":"123e4567-e89b-12d3-a456-426614174000"}'
</code></pre>
<p>To stop the server, press Ctrl+C in the terminal.</p>
<h2 id="heading-step-6-run-the-frontend-app"><strong>Step 6: Run the Frontend App</strong></h2>
<p>In another terminal, go to the project directory:</p>
<pre><code class="language-plaintext">source venv/bin/activate
streamlit run streamlit_app.py
</code></pre>
<p>That opens the frontend in your browser at <code>http://localhost:8501/</code>. Try the example prompts like "What is the capital of France". You should see the answer in a chat style interface.</p>
<img src="https://cdn.hashnode.com/uploads/covers/684c95e159698b4bf6a0e4be/1030735a-49ed-43e1-995d-07b122c2c965.png" alt="Streamlit UI provides a simple chat frontend for the local AI agent" style="display:block;margin:0 auto" width="1848" height="1710" loading="lazy">

<p>The UI is calling the FastAPI endpoint and invoking the AI agent. You now have a working end to end application for your local AI agent that you can play with.</p>
<p>To stop the server, press Ctrl+C in the terminal.</p>
<h2 id="heading-sample-output">Sample Output</h2>
<p>The image below show two browser sessions of the app running side by side on the same endpoint. Each session is assigned a unique id, which allows the backend to maintain a separate conversation history for each user.</p>
<p>Even though both users ask the same question, “Who am I?”, the responses are different because each session’s answer is based on its own prior messages.</p>
<img src="https://cdn.hashnode.com/uploads/covers/684c95e159698b4bf6a0e4be/b97b8efa-6fca-4e80-9c0a-d0d2601fc2b6.png" alt="Image showing two sessions with the agent and it gives different answers based on the the conversation history" style="display:block;margin:0 auto" width="2914" height="1906" loading="lazy">

<h2 id="heading-what-to-improve-before-production">What to Improve Before Production</h2>
<p>Although this application is fully functional, it's still intentionally minimal. It already supports a reusable FastAPI backend, a Streamlit chat interface, per-user conversation history, and streaming responses.</p>
<p>If you wanted to take it further, the next steps would be adding authentication, persistent storage, structured logging, monitoring, and more robust deployment setup.</p>
<p>It's also worth noting that if your goal is simply to get a polished self-hosted chat UI up and running quickly, you may not need to build the frontend yourself. Projects like <a href="https://www.librechat.ai/">LibreChat</a> and <a href="https://docs.openwebui.com/">Open WebUI</a> already provide richer interfaces and broader features out of the box.</p>
<p>This tutorial takes a different approach: instead of adopting a full platform, it shows how to build a lightweight custom stack yourself so you can better understand the architecture and have more control over how the agent is exposed.</p>
<h2 id="heading-conclusion">Conclusion</h2>
<p>In this tutorial, we took a local AI agent, wrapped it in a FastAPI app, and used Streamlit UI on top of it.</p>
<p>This transforms the AI agent from a standalone script into a reusable service. Instead of only working in a terminal, it can now be accessed through a simple HTTP endpoint by other apps, scripts, or internal tools.</p>
<p>By assigning each session a unique id, the service can also maintain separate conversation history for multiple users, making it possible to support a chat-style interface with isolated memory per session.</p>
<p>From here, you can continue extending the same service by adding authentication or production-ready features. Happy tinkering!</p>
<p>If you enjoyed this tutorial, you can find more of my writing on my&nbsp;<a href="https://darshshah.org/blog/">blog</a>&nbsp;(recent posts include system design paper series), my work on my&nbsp;<a href="https://darshshah.org/">personal website</a>, and updates on&nbsp;<a href="https://www.linkedin.com/in/darshs">LinkedIn</a>.</p>


                    