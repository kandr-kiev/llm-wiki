---
source_url: https://www.freecodecamp.org/news/how-to-trace-and-monitor-ai-agents-with-langsmith/
ingested: 2026-07-22
sha256: 8591c38aea79afbfd96a2fc71dc379be49575943db0c51f793f4794e1bc612e3
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Trace and Monitor AI Agents with LangSmith</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-to-trace-and-monitor-ai-agents-with-langsmith/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="In this tutorial, I&#39;ll show you how to trace and monitor a local AI agent with LangSmith. We&#39;ll build a small local AI agent and then enable LangSmith tracing for it so that we can inspect model calls">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Trace and Monitor AI Agents with LangSmith">
    
        <meta property="og:description" content="In this tutorial, I&#39;ll show you how to trace and monitor a local AI agent with LangSmith. We&#39;ll build a small local AI agent and then enable LangSmith tracing for it so that we can inspect model calls">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-to-trace-and-monitor-ai-agents-with-langsmith/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/6ff293d4-dea5-462b-b79b-c319d77458f0.png">
    <meta property="article:published_time" content="2026-07-22T19:49:02.753Z">
    <meta property="article:modified_time" content="2026-07-22T19:49:02.753Z">
    
        <meta property="article:tag" content="AI">
    
        <meta property="article:tag" content="ai agents">
    
        <meta property="article:tag" content="LLM&#39;s ">
    
        <meta property="article:tag" content="tracing">
    
        <meta property="article:tag" content="langsmith">
    
        <meta property="article:tag" content="langchain">
    
        <meta property="article:tag" content="observability">
    
        <meta property="article:tag" content="#qwen">
    
        <meta property="article:tag" content="Python">
    
        <meta property="article:tag" content="ollama">
    
        <meta property="article:tag" content="langfuse">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Trace and Monitor AI Agents with LangSmith">
    
        <meta name="twitter:description" content="In this tutorial, I&#39;ll show you how to trace and monitor a local AI agent with LangSmith. We&#39;ll build a small local AI agent and then enable LangSmith tracing for it so that we can inspect model calls">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-to-trace-and-monitor-ai-agents-with-langsmith/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/6ff293d4-dea5-462b-b79b-c319d77458f0.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Darsh Shah">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="AI, ai agents, LLM&#39;s , tracing, langsmith, langchain, observability, #qwen, Python, ollama, langfuse">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/6ff293d4-dea5-462b-b79b-c319d77458f0.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-to-trace-and-monitor-ai-agents-with-langsmith/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-22T19:49:02.753Z",
	"dateModified": "2026-07-22T19:49:02.753Z",
	"keywords": "AI, ai agents, LLM's , tracing, langsmith, langchain, observability, Python, ollama, langfuse",
	"description": "In this tutorial, I&#x27;ll show you how to trace and monitor a local AI agent with LangSmith. We&#x27;ll build a small local AI agent and then enable LangSmith tracing for it so that we can inspect model calls",
	"headline": "How to Trace and Monitor AI Agents with LangSmith",
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-22T19:49:02.753Z">
                            July 22, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/ai/">
                                #AI
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Trace and Monitor AI Agents with LangSmith</h1>
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
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/6ff293d4-dea5-462b-b79b-c319d77458f0.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/6ff293d4-dea5-462b-b79b-c319d77458f0.png" alt="How to Trace and Monitor AI Agents with LangSmith" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>In this tutorial, I'll show you how to trace and monitor a local AI agent with LangSmith. We'll build a small local AI agent and then enable LangSmith tracing for it so that we can inspect model calls, tool usage, and request latency in a web UI.</p>
<p>We'll be using LangChain v1, Ollama, Qwen, and Python. Everything runs on your own machine except the observability layer, so the agent itself has no model API costs.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-background">Background</a></p>
</li>
<li><p><a href="#heading-what-is-observability-and-monitoring">What is Observability and Monitoring?</a></p>
</li>
<li><p><a href="#heading-what-is-langsmith">What is LangSmith?</a></p>
</li>
<li><p><a href="#heading-motivation-and-architecture">Motivation and Architecture</a></p>
</li>
<li><p><a href="#heading-step-1-install-ollama-and-pull-the-model">Step 1: Install Ollama and Pull the Model</a></p>
</li>
<li><p><a href="#heading-step-2-install-python-dependencies">Step 2: Install Python Dependencies</a></p>
</li>
<li><p><a href="#heading-step-3-enable-langsmith-tracing">Step 3: Enable LangSmith tracing</a></p>
</li>
<li><p><a href="#heading-step-4-build-the-agent">Step 4: Build the agent</a></p>
</li>
<li><p><a href="#heading-sample-output">Sample output</a></p>
</li>
<li><p><a href="#heading-next-steps">Next Steps</a></p>
</li>
<li><p><a href="#heading-conclusion">Conclusion</a></p>
</li>
</ul>
<h2 id="heading-background">Background</h2>
<p>Building a local AI agent is the easy part. The harder part starts later, when the agent behaves differently after a prompt change, starts using the wrong tool, or becomes slower without an obvious reason.</p>
<p>With regular software, we usually rely on logs and metrics to understand what changed. Agents need that too, but they also need visibility into the actual chain of decisions inside a request. A single user message might trigger a model call, one or more tool calls, and several intermediate steps before the final answer is returned.</p>
<p>If we only look at the final output, we miss most of what matters. We can tell that something went wrong, but not where it went wrong.</p>
<p>That’s why observability matters for AI agents. In this tutorial, we’ll set up LangSmith tracing for a local LangChain agent so we can inspect each request, see which tools were called, and understand how the agent behaved step by step</p>
<p>To follow along, you’ll need Ollama installed on your machine. The tutorial works on macOS, Windows, and Linux. I’m using a MacBook Pro with 32 GB of RAM, but you can run the same setup on a lower-memory machine by choosing a smaller Qwen model.</p>
<h2 id="heading-what-is-observability-and-monitoring">What is Observability and Monitoring?</h2>
<p>Monitoring tells us that something is wrong. It gives us signals like higher latency, more failures, more tool errors, or rising usage over time.</p>
<p>Observability helps us understand why it's wrong. It lets us inspect what happened inside a request. For an AI agent, that means looking at the prompt, the model calls, the tool calls, the outputs, and the timing for each step.</p>
<p>In practice, observability usually includes three things:</p>
<ul>
<li><p>Traces: the full step-by-step path of a request</p>
</li>
<li><p>Logs: records of events, outputs, and errors</p>
</li>
<li><p>Metrics: numbers tracked over time, like latency, failures, and usage</p>
</li>
</ul>
<p>For AI agents, this matters because the final answer alone usually isn’t enough. If the output is wrong or slow, we need a way to see whether the problem came from the model, the prompt, the tool choice, or something in the middle of the agent loop. The goal is to understand what happened and where it went wrong.</p>
<h2 id="heading-what-is-langsmith">What is LangSmith?</h2>
<p><a href="https://docs.langchain.com/langsmith/observability">LangSmith</a> is LangChain’s observability platform for tracing, debugging, evaluating, and monitoring LLM apps and agents.</p>
<p>The core concepts of LangSmith are:</p>
<ul>
<li><p>Project: a container for related traces</p>
</li>
<li><p>Trace: the full execution of one request</p>
</li>
<li><p>Run: an individual step inside a trace, such as an LLM call or tool call</p>
</li>
<li><p>Thread: a conversation or session grouping, useful for multi-turn agents</p>
</li>
</ul>
<p>LangChain agents built with <code>create_agent</code> automatically support LangSmith tracing, which means you can capture model calls, tool invocations, and execution steps with no code changes. The traces get automatically uploaded to LangSmith server on every agent invocation.</p>
<p>LangSmith features include request traces, step-by-step run inspection, latency and usage monitoring, dashboards, project-based organization, alerts for regressions, and more.</p>
<h2 id="heading-motivation-and-architecture">Motivation and Architecture</h2>
<p>Monitoring is the natural next step after building an agent. Once the agent works, the next question is whether it works reliably and whether we can debug it when it doesn’t. This becomes especially important in production, where debugging real user issues is much harder without traces, metrics, and request-level visibility.</p>
<p>To keep things simple, we’ll monitor a small local agent with two tools: one for the current time and another for counting words. The agent runs locally through Ollama, while LangSmith captures the trace data so we can inspect it in the browser and debug/monitor it.</p>
<h2 id="heading-step-1-install-ollama-and-pull-the-model">Step 1: Install Ollama and Pull the Model</h2>
<p>To get started, install the Ollama application for your platform. We'll use <code>qwen3.5:4b</code>.</p>
<pre><code class="language-plaintext">ollama pull qwen3.5:4b
</code></pre>
<p>If your machine has lower RAM, you can use qwen3.5:0.8b instead.</p>
<h2 id="heading-step-2-install-python-dependencies">Step 2: Install Python Dependencies</h2>
<p>Create a virtual environment and install the required packages:</p>
<pre><code class="language-plaintext">python3 -m venv venv 
source venv/bin/activate 
pip install langchain langchain-core langchain-ollama langsmith
</code></pre>
<p>This tutorial requires <code>langchain&gt;=1.0.0</code>.</p>
<h2 id="heading-step-3-enable-langsmith-tracing">Step 3: Enable LangSmith Tracing</h2>
<p>Create a free LangSmith account on <a href="https://smith.langchain.com">https://smith.langchain.com</a>. Once signed in, create a new project called MyAgentApp.</p>
<img src="https://cdn.hashnode.com/uploads/covers/684c95e159698b4bf6a0e4be/b8b47668-8002-467b-a55f-310bce0e7772.png" alt="LangSmith page to create a new project. We will create MyAgentApp project" width="600" height="400" loading="lazy">

<p>Then generate an API key for the project, and set the environment variables in your terminal. The LangSmith webpage will show the values to set.</p>
<pre><code class="language-bash">export LANGSMITH_TRACING=true
export LANGSMITH_ENDPOINT=https://api.smith.langchain.com
export LANGSMITH_API_KEY=your_langsmith_api_key
export LANGSMITH_PROJECT="MyAgentApp"
</code></pre>
<p>At this point, your app is ready to send traces to LangSmith.</p>
<h2 id="heading-step-4-build-the-agent">Step 4: Build the Agent</h2>
<p>Below is a minimal AI agent using Ollama, LangChain, and two simple tools. This is the simpler version of the tool calling agent that we created in <a href="https://www.freecodecamp.org/news/how-to-build-your-own-local-ai-agent-with-tool-calling-and-memory/#heading-step-3-agent-python-code">How to Build Your Own Local AI Agent with Tool Calling and Memory</a>.</p>
<p>No additional tracing/LangSmith setup is required.</p>
<p>Save this file as <code>trace_agent.py</code>:</p>
<pre><code class="language-python">from datetime import datetime

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

CHAT_MODEL = "qwen3.5:4b"   # Ollama chat model. Must support tool calling.

SYSTEM_PROMPT = (
    "You are a helpful assistant with access to tools for getting the current time and counting words in text. "
    "Use tools when the user's request needs one. "
    "If the question doesn't need a tool, answer directly. "
    "If a tool returns an error, explain the error plainly."
)

# ----- Tools -----
@tool
def current_time() -&gt; str:
    """Return the current local date and time.
    Use this when the user asks what time or date it is.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@tool
def word_count(text: str) -&gt; int:
    """Count the number of words in a piece of text.
    Use this when the user asks how long a piece of writing is,
    or asks you to count the words in something they've shared.
    Returns the word count as an integer.
    """
    return len(text.split())


TOOLS = [current_time, word_count]


# ----- Agent -----

def build_agent():
    model = ChatOllama(model=CHAT_MODEL, reasoning=False, temperature=0)

    return create_agent(
        model=model,
        tools=TOOLS,
        system_prompt=SYSTEM_PROMPT
    )


def main():
    agent = build_agent()

    print("Ready! Ask the agent something.\n")

    # Track how many messages existed before this turn, so we can slice out
    # only the new ones (tool calls + final answer) from the returned state.
    prev_message_count = 0

    while True:
        question = input("You: ").strip()
        if not question or question.lower() == "exit":
            break

        result = agent.invoke(
            {"messages": [{"role": "user", "content": question}]}
        )

        # Only look at messages added during this turn, not the full history.
        new_messages = result["messages"][prev_message_count:]

        # Print any tool calls made in this turn.
        for msg in new_messages:
            tool_calls = getattr(msg, "tool_calls", None)
            if tool_calls:
                for call in tool_calls:
                    print(f"[tool call] {call['name']}({call['args']})")

        print(f"\nAnswer: {result['messages'][-1].content}\n")

        # Update the count for the next turn.
        prev_message_count = len(result["messages"])


if __name__ == "__main__":
    main()
</code></pre>
<p>Because this agent is created with LangChain’s agent APIs, LangSmith tracing should capture the end-to-end execution: input, model interactions, tool calls, and final output without any additional configuration.</p>
<p>Run the agent:</p>
<pre><code class="language-plaintext">python trace_agent.py
</code></pre>
<h2 id="heading-sample-output">Sample Output</h2>
<p>The output looks like below. I asked the agent four questions. It invoked tools for finding the time and word length.</p>
<pre><code class="language-text">$python trace_agent.py 
Ready! Ask the agent something.

You: Hello, how are you?

Answer: I'm doing well! How about you? Is there anything specific I can help you with today?

You: What is the current time
[tool call] current_time({})

Answer: The current local date and time is July 17, 2026 at 13:56. Is there anything else you'd like to know?

You: What is the word count for "LangSmith is awesome"
[tool call] word_count({'text': 'LangSmith is awesome'})

Answer: The phrase "LangSmith is awesome" has a word count of 3. Let me know if you need anything else!

You: What is capital of France

Answer: The capital of France is Paris.
</code></pre>
<p>Now, we'll see how LangSmith traced the request. Go to the LangSmith Web UI and sign in. Click on your project and you can see:</p>
<ul>
<li><p>traces in your project</p>
</li>
<li><p>the request and responses</p>
</li>
<li><p>tool calling information</p>
</li>
<li><p>token consumption</p>
</li>
<li><p>latency information and other key metrics</p>
</li>
</ul>
<p>For the above output, I can see four traces (each agent invocation creates its own trace):</p>
<img src="https://cdn.hashnode.com/uploads/covers/684c95e159698b4bf6a0e4be/a2f80d11-8bb5-4f43-a937-20a01bef3607.png" alt="Image showing all four traces in MyAgentApp project in LangSmith UI" width="3300" height="1144" loading="lazy">

<p>Inspecting trace 2, I can see the request, response, and tool calling information. I can also see the tokens consumed.</p>
<img src="https://cdn.hashnode.com/uploads/covers/684c95e159698b4bf6a0e4be/b871eeda-9efd-453f-a966-185393384868.png" alt="Image showing one trace request and response  in MyAgentApp project in LangSmith UI" width="2854" height="1700" loading="lazy">

<p>I can see the overall count, latency, error rate, and other metrics for my app. This can help in checking the overall usage and health of your AI agent.</p>
<img src="https://cdn.hashnode.com/uploads/covers/684c95e159698b4bf6a0e4be/c1863bf6-f383-4205-915d-bad6a315bade.png" alt="Image showing monitoring dashboard with count, latency and error rate metrics in LangSmith UI" width="2812" height="1816" loading="lazy">

<p>Lastly, I can setup alerts to monitor and notify if something goes wrong. For example, we can configure an alert called HighUsage and it will alert if the run count is more than once in the last 5 minutes.</p>
<img src="https://cdn.hashnode.com/uploads/covers/684c95e159698b4bf6a0e4be/c4d11b88-5ceb-4e4e-8614-e18bd2eb1c94.png" alt="Image showing Alert setup window in LangSmith UI. " width="3118" height="1540" loading="lazy">

<p>The above setup gives you a very quick way to setup observability and monitoring for your AI Agent.</p>
<h2 id="heading-next-steps">Next Steps</h2>
<p>Once tracing works, the next improvement is to add metadata and tags so traces become easier to filter and analyze. LangSmith supports custom metadata and tags to label requests by environment, app version, user tier, or workflow.</p>
<p>For example, you might add the below option in the config:</p>
<ul>
<li><p><code>environment=dev</code></p>
</li>
<li><p><code>agent_name=local-ollama-agent</code></p>
</li>
<li><p><code>model=qwen3</code></p>
</li>
</ul>
<pre><code class="language-python">result = agent.invoke(
            {"messages": [{"role": "user", "content": question}]},

config={
        "tags": ["dev", "local-ollama-agent"],
        "metadata": {
            "environment": "dev",
            "agent_name": "local-ollama-agent",
            "model": "qwen3"
        }
    }
)
</code></pre>
<p>This becomes useful when comparing across agents, models and enviroments.</p>
<p>One caveat is that LangSmith is proprietary. Using it means your trace data is sent to LangSmith’s hosted service, and there's usually a cost attached as your usage grows. For this tutorial, it's free as the trace volume is low. For most projects, it will be fine to use LangSmith.</p>
<p>An open-source alternative to LangSmith is <a href="https://langfuse.com">Langfuse</a>. It provides LLM observability with traces, sessions, metadata, dashboards, and metrics, and it can be self-hosted. It provides similar features like capturing traces of LLM calls, tool executions, timing, inputs, outputs, and metadata, along with customizable dashboards and metadata-based filtering.</p>
<h2 id="heading-conclusion">Conclusion</h2>
<p>In this tutorial, we took a local AI agent and added observability with LangSmith using LangChain v1, Ollama, Qwen, and Python. The result is a simple monitoring and observability setup that shows what the agent did, which tools it called, and how long each step took.</p>
<p>From here, you can extend the setup by adding metadata, creating separate projects for dev and prod, or trying an open-source alternative like Langfuse. The core loop stays the same: run the agent, capture the trace, inspect the result, and use that signal to improve the system.</p>
<p>If you enjoyed this tutorial, you can find more of my writing on my <a href="http://darshshah.org/blog">blog</a> (recent posts include a system design paper series), my work on my personal <a href="https://darshshah.org/">website</a>, and updates on <a href="https://www.linkedin.com/in/darshs">LinkedIn</a>.</p>


                        </section>
                        
                            <div class="sidebar">
                                
                                    
                                    <script>var localizedAdText = "ADVERTISEMENT";</script>
                                
                            </div>
                        
                    </div>
                    <hr>
                    
                        <div class="post-full-author-header" data-test-label="author-header-with-bio">
                            
                                
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/uploads/avatars/684c95e159698b4bf6a0e4be/1551f7e1-25fa-44ea-aaee-25b5fa4377a9.jpg 60w" sizes="60px" src="https://cdn.hashnode.com/uploads/avatars/684c95e159698b4bf6a0e4be/1551f7e1-25fa-44ea-aaee-25b5fa4377a9.jpg" class="author-profile-image" alt="Darsh Shah" width="2954" height="2057" onerror="this.style.display='none'" loading="lazy" data-test-label="profile-image">
  
        

        <section class="author-card-content ">
            <span class="author-card-name">
                <a href="/news/author/darshs/" data-test-label="profile-link">
                    
                        Darsh Shah
                    
                </a>
            </span>
            
                
                    <p data-test-label="author-bio">https://darshshah.org/</p>
                
            
        </section>
    </section>

                            
                        </div>
                        <hr>
                    

                    
                    
                        
    


<p data-test-label="social-row-cta" class="social-row">
    If this article was helpful, <button id="tweet-btn" class="cta-button" data-test-label="tweet-button">share it</button>.
</p>


    
    <script>document.addEventListener("DOMContentLoaded",()=>{const t=document.getElementById("tweet-btn"),n=window.location,e="How%20to%20Trace%20and%20Monitor%20AI%20Agents%20with%20LangSmith".replace(/&#39;/g,"%27"),o="",i="",r=Boolean("");let a;if(r&&(o||i)){const t={originalPostAuthor:"",currentPostAuthor:"Darsh Shah"};a=encodeURIComponent(`Thank you ${o||t.originalPostAuthor} for writing this helpful article, and ${i||t.currentPostAuthor} for translating it.`)}else!r&&i&&(a=encodeURIComponent(`Thank you ${i} for writing this helpful article.`));const h=`window.open(\n    '${a?`https://x.com/intent/post?text=${a}%0A%0A${e}%0A%0A${n}`:`https://x.com/intent/post?text=${e}%0A%0A${n}`}',\n    'share-twitter',\n    'width=550, height=235'\n  ); return false;`;t.setAttribute("onclick",h)});</script>


                        

<div class="learn-cta-row" data-test-label="learn-cta-row">
    <p>
        Learn to code for free. freeCodeCamp's open source curriculum has helped more than 40,000 people get jobs as developers. <a href="https://www.freecodecamp.org/learn" class="cta-button" id="learn-to-code-cta" rel="noopener noreferrer" target="_blank">Get started</a>
    </p>
</div>

                    
                </section>
                
                    <div class="banner-ad-bottom">
                        
                            

<div class="ad-text" data-test-label="ad-text">ADVERTISEMENT</div>
<div style="display: block; height: auto" id="gam-ad-bottom">
</div>

                        
                    </div>
                
            </article>
        </div>
    </main>


            


<footer class="site-footer">
    <div class="footer-top">
        <div class="footer-desc-col">
            <p data-test-label="tax-exempt-status">freeCodeCamp is a donor-supported tax-exempt 501(c)(3) charity organization (United States Federal Tax Identification Number: 82-0779546)</p>
            <p data-test-label="mission-statement">Our mission: to help people learn to code for free. We accomplish this by creating thousands of videos, articles, and interactive coding lessons - all freely available to the public.</p>
            <p data