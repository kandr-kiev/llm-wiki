---
source_url: https://www.freecodecamp.org/news/how-to-evaluate-ai-agents-with-an-llm-as-a-judge-harness-in-python/
ingested: 2026-07-18
sha256: f5504bfbfa017a9bd18c9a0422fad5e46f1cf46eb8c84594370666c4a3ac4474
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Evaluate AI Agents with an LLM-as-a-Judge Harness in Python</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-to-evaluate-ai-agents-with-an-llm-as-a-judge-harness-in-python/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="In this tutorial, I&#39;ll show you how to evaluate a local AI agent with a simple, repeatable evaluation harness. The harness runs the agent against a set of test cases, checks the results with both rule">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Evaluate AI Agents with an LLM-as-a-Judge Harness in Python">
    
        <meta property="og:description" content="In this tutorial, I&#39;ll show you how to evaluate a local AI agent with a simple, repeatable evaluation harness. The harness runs the agent against a set of test cases, checks the results with both rule">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-to-evaluate-ai-agents-with-an-llm-as-a-judge-harness-in-python/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/43678778-ab94-4ad0-92af-888376bea668.png">
    <meta property="article:published_time" content="2026-07-17T21:03:56.909Z">
    <meta property="article:modified_time" content="2026-07-17T21:03:56.909Z">
    
        <meta property="article:tag" content="AI">
    
        <meta property="article:tag" content="ai agents">
    
        <meta property="article:tag" content="LLM-as-Judge">
    
        <meta property="article:tag" content="ollama">
    
        <meta property="article:tag" content="agent evaluation">
    
        <meta property="article:tag" content="#qwen">
    
        <meta property="article:tag" content="Python">
    
        <meta property="article:tag" content="langchain">
    
        <meta property="article:tag" content="Harness">
    
        <meta property="article:tag" content="Evaluation">
    
        <meta property="article:tag" content="llm">
    
        <meta property="article:tag" content="local ai">
    
        <meta property="article:tag" content="tech ">
    
        <meta property="article:tag" content="genai">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Evaluate AI Agents with an LLM-as-a-Judge Harness in Python">
    
        <meta name="twitter:description" content="In this tutorial, I&#39;ll show you how to evaluate a local AI agent with a simple, repeatable evaluation harness. The harness runs the agent against a set of test cases, checks the results with both rule">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-to-evaluate-ai-agents-with-an-llm-as-a-judge-harness-in-python/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/43678778-ab94-4ad0-92af-888376bea668.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Darsh Shah">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="AI, ai agents, LLM-as-Judge, ollama, agent evaluation, #qwen, Python, langchain, Harness, Evaluation, llm, local ai, tech , genai">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/43678778-ab94-4ad0-92af-888376bea668.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-to-evaluate-ai-agents-with-an-llm-as-a-judge-harness-in-python/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-17T21:03:56.909Z",
	"dateModified": "2026-07-17T21:03:56.909Z",
	"keywords": "AI, ai agents, LLM-as-Judge, ollama, agent evaluation, Python, langchain, Harness, Evaluation, llm, local ai, tech , genai",
	"description": "In this tutorial, I&#x27;ll show you how to evaluate a local AI agent with a simple, repeatable evaluation harness.\nThe harness runs the agent against a set of test cases, checks the results with both rule",
	"headline": "How to Evaluate AI Agents with an LLM-as-a-Judge Harness in Python",
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-17T21:03:56.909Z">
                            July 17, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/ai/">
                                #AI
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Evaluate AI Agents with an LLM-as-a-Judge Harness in Python</h1>
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
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/43678778-ab94-4ad0-92af-888376bea668.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/43678778-ab94-4ad0-92af-888376bea668.png" alt="How to Evaluate AI Agents with an LLM-as-a-Judge Harness in Python" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>In this tutorial, I'll show you how to evaluate a local AI agent with a simple, repeatable evaluation harness.</p>
<p>The harness runs the agent against a set of test cases, checks the results with both rule-based assertions and an LLM-as-a-judge, and prints a clear pass/fail summary.</p>
<p>Everything runs on your own machine with LangChain v1, Ollama, Qwen, and Python, so there are no API costs.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-background">Background</a></p>
</li>
<li><p><a href="#heading-what-is-agent-evaluation">What is Agent Evaluation</a>?</p>
</li>
<li><p><a href="#heading-what-is-llm-as-a-judge">What is LLM-as-a-Judge</a>?</p>
</li>
<li><p><a href="#heading-motivation-and-architecture">Motivation and Architecture</a></p>
</li>
<li><p><a href="#heading-step-1-install-ollama-and-pull-the-model">Step 1: Install Ollama and Pull the Model</a></p>
</li>
<li><p><a href="#heading-step-2-install-python-dependencies">Step 2: Install Python Dependencies</a></p>
</li>
<li><p><a href="#heading-step-3-the-agent-under-test">Step 3: The Agent Under Test</a></p>
</li>
<li><p><a href="#heading-step-4-write-the-eval-harness">Step 4: Write the Eval Harness</a></p>
</li>
<li><p><a href="#heading-step-5-run-the-evals">Step 5: Run the Evals</a></p>
</li>
<li><p><a href="#heading-sample-output">Sample Output</a></p>
</li>
<li><p><a href="#heading-conclusion">Conclusion</a></p>
</li>
</ul>
<h2 id="heading-background">Background</h2>
<p>Most local AI agents get tested the same way: type a couple of questions, the answers look right, and just ship it. This works until we change the prompt, swap the model, or add a tool. Then something breaks quietly, and we don’t notice until it's too late.</p>
<p>Regular Python code has unit tests to catch this. AI agents don’t get that for free. Even with the same input, an agent can behave differently across runs, and small changes can introduce regressions that are easy to miss. Without a repeatable way to test the agent on multiple inputs and score the outputs, we're mostly guessing on agent's behavior.</p>
<p>A simple fix is to build a lightweight evaluation setup that contains a Python script, a list of test cases, rule-based checks, and an LLM-as-judge. That gives us a practical way to test the agent before on any changes.</p>
<p>To follow along, you'll need Ollama installed on your machine. The tutorial works on macOS, Windows, and Linux. I'm using a MacBook Pro with 32 GB of RAM, but you can run this on a lower-memory machine by choosing a smaller Qwen model from Ollama.</p>
<h2 id="heading-what-is-agent-evaluation">What is Agent Evaluation?</h2>
<p>Agent evaluation is the practice of running your agent against a fixed set of inputs and scoring the outputs against expectations. It's the AI equivalent of a test suite.</p>
<p>The goal isn't to prove the agent is perfect. The goal is to catch regressions when you change something.</p>
<p>A useful eval has three parts:</p>
<ol>
<li><p>Test cases: a list of inputs with expected behaviors.</p>
</li>
<li><p>Checks: functions that score the agent's output for each input.</p>
</li>
<li><p>A summary: a pass/fail count so you can see how the agent did.</p>
</li>
</ol>
<h2 id="heading-what-is-llm-as-a-judge">What is LLM-as-a-Judge?</h2>
<p>There are two practical ways to score an agent's output. The first is rule-based checks. You assert on things like "did the output contain the word Paris" or "did the agent call the <code>word_count</code> tool." These are cheap, fast, and deterministic.</p>
<p>The second is LLM-as-a-judge. You ask a separate LLM to read the input and the agent's output, then score it against a rubric. A rubric can be a simple pass/fail output. This is useful for fuzzy things you can't easily assert on, like "did the answer actually address what the user asked." The tradeoff is that the judge is itself an LLM and can be wrong.</p>
<p>In this tutorial, we'll be using the same model with a different prompt for judging.</p>
<h2 id="heading-motivation-and-architecture">Motivation and Architecture</h2>
<p>Evaluating an agent is the natural next step after building one. Knowing the agent works reliably across different inputs is what turns it into something we can trust.</p>
<p>To keep things simple, we'll evaluate a small local agent with two tools: one for the current time and another for counting words. The eval harness reads a list of test cases from Python, runs each one through the agent, applies rule-based checks and an LLM-as-judge score, and prints a pass/fail summary.</p>
<img src="https://cdn.hashnode.com/uploads/covers/684c95e159698b4bf6a0e4be/3106ea8b-5d56-42d9-8f0f-2d12718af2f3.png" alt="Diagram showing the eval harness that reads a list of test cases from Python, runs each one through the agent, applies rule-based checks and an LLM-as-judge score, and prints a pass/fail summary" style="display:block;margin:0 auto" width="1140" height="1440" loading="lazy">

<p>In the example test case below, expected_keyword and expected_tool are the two rules based checks. The judge_rubric is the criteria for LLM judge.</p>
<pre><code class="language-plaintext">{
    "input": "What is the capital of France?",
    "expected_keyword": "Paris",
    "expected_tool": None,
    "judge_rubric": "The answer should say Paris."
}
</code></pre>
<p>The agent and the judge both run locally through Ollama, so there are no per-call model API charges.</p>
<h2 id="heading-step-1-install-ollama-and-pull-the-model">Step 1: Install Ollama and Pull the Model</h2>
<p>To get started, install the Ollama application for your platform. We'll use Qwen as both the agent and the judge. I'm using <code>qwen3.5:4b</code>.</p>
<pre><code class="language-plaintext">ollama pull qwen3.5:4b
</code></pre>
<p>If your machine has lower RAM, you can use qwen3.5:0.8b instead, though you'll see noisier judge scores at that size.</p>
<h2 id="heading-step-2-install-python-dependencies">Step 2: Install Python Dependencies</h2>
<p>Create a virtual environment and install the required packages:</p>
<pre><code class="language-plaintext">python3 -m venv venv
source venv/bin/activate

pip install langchain langchain-core langchain-ollama
</code></pre>
<p>This tutorial requires <code>langchain&gt;=1.0.0</code>.</p>
<h2 id="heading-step-3-the-agent-under-test">Step 3: The Agent Under Test</h2>
<p>We'll use a small tool-calling agent with two tools. The harness treats the agent as an opaque system, so nothing about the agent itself changes for evaluation.</p>
<p>The agent code below defines two tools: <code>current_time()</code> to get the current time and <code>word_count()</code> to get the word count in the input sentence. The agent is created using LangChain's <code>build_agent()</code> and uses a simple system prompt.</p>
<p>Save the following as <code>agent.py</code>:</p>
<pre><code class="language-python">from datetime import datetime

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_ollama import ChatOllama


@tool
def current_time() -&gt; str:
    """Return the current local date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@tool
def word_count(text: str) -&gt; int:
    """Count the number of words in a piece of text."""
    return len(text.split())


def build_agent():
    model = ChatOllama(model="qwen3.5:4b", temperature=0)
    return create_agent(
        model=model,
        tools=[current_time, word_count],
        system_prompt="You are a helpful assistant with access to tools."
    )
</code></pre>
<h2 id="heading-step-4-write-the-eval-harness">Step 4: Write the Eval Harness</h2>
<p>The harness does three things for each test case:</p>
<ol>
<li><p>Runs the agent and collects the answer plus any tool calls.</p>
</li>
<li><p>Checks the result with simple rule-based assertions for the expected keyword (if keyword is present in the output) and expected tool (if the tool was used).</p>
</li>
<li><p>Asks an LLM-as-judge to score the output. The input prompt for judging contains the original user prompt, the agent's answer and the rubric to score against. The LLM's judge is asked "Does the answer meet the rubric? Reply with just YES or NO". The output from the judge is either YES or NO.</p>
</li>
</ol>
<p>The test cases are defined at the top of the file in the code. For each case, the code calls the tool-calling agent to get the agent's output then prints the answer with any tool calls. It then passes the output to the <code>check_keyword()</code> and <code>check_tool()</code> methods for rule-based checks. After that, it calls <code>llm_judge()</code> to invoke model for judging the previous agent's output. Finally, the code prints the final pass/fail summary after the checks complete.</p>
<p>Save the following as <code>eval.py</code>:</p>
<pre><code class="language-python">from langchain_ollama import ChatOllama
from agent import build_agent


# -----------------------------
# Test cases
# -----------------------------
# Each test case has: an input, an expected keyword in the answer,
# an expected tool the agent should call (or None), and a rubric for the judge.

TEST_CASES = [
    {
        "input": "What time is it right now?",
        "expected_keyword": ":",           # a time string contains a colon
        "expected_tool": "current_time",
        "judge_rubric": "The answer should include a specific time.",
    },
    {
        "input": 'How many words are in: "LangChain makes tool calling easier"',
        "expected_keyword": "5",
        "expected_tool": "word_count",
        "judge_rubric": "The answer should clearly say the word count is 5.",
    },
    {
        "input": "What is the capital of France?",
        "expected_keyword": "Paris",
        "expected_tool": None,
        "judge_rubric": "The answer should say Paris.",
    },
    {
         "input": "How many words are in 'LangChain makes tool calling easier'? Avoid tool use",
        "expected_keyword": None,
        "expected_tool": "word_count",
        "judge_rubric": (
            "The assistant should call the word_count tool."
        )
    },
]


# -----------------------------
# Rule-based checks
# -----------------------------

def check_keyword(answer, keyword):
    if keyword is None:
        return True
    return keyword.lower() in answer.lower()


def check_tool(tool_calls, expected_tool):
    if expected_tool is None:
        return len(tool_calls) == 0
    return expected_tool in tool_calls


# -----------------------------
# LLM-as-judge
# -----------------------------

judge = ChatOllama(model="qwen3.5:4b", temperature=0)


def llm_judge(user_input, answer, rubric):
    prompt = (
        f"User asked: {user_input}\n"
        f"Agent answered: {answer}\n"
        f"Rubric: {rubric}\n\n"
        f"Does the answer meet the rubric? Reply with just YES or NO."
    )
    response = judge.invoke(prompt).content.strip().upper()
    return response.startswith("YES")


# -----------------------------
# Run the evals
# -----------------------------

def run_evals():
    agent = build_agent()
    passed_count = 0

    for i, case in enumerate(TEST_CASES, start=1):
        # Run the agent
        result = agent.invoke({
            "messages": [{"role": "user", "content": case["input"]}],
        })

        # Pull out the answer and any tools the agent called
        answer = result["messages"][-1].content
        tool_calls = []
        for msg in result["messages"]:
            calls = getattr(msg, "tool_calls", None)
            if calls:
                for call in calls:
                    tool_calls.append(call["name"])

        print(f"[Answer] Test {i}: {answer} \n[Tools] {tool_calls}")
      
        # Apply the three checks
        keyword_ok = check_keyword(answer, case["expected_keyword"])
        tool_ok = check_tool(tool_calls, case["expected_tool"])
        judge_ok = llm_judge(case["input"], answer, case["judge_rubric"])

        passed = keyword_ok and tool_ok and judge_ok
        if passed:
            passed_count += 1

        # Print the result
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] Test {i}: {case['input']}")
        if not keyword_ok:
            print(f"    - keyword check failed (expected '{case['expected_keyword']}')")
        if not tool_ok:
            print(f"    - tool check failed (expected {case['expected_tool']}, got {tool_calls})")
        if not judge_ok:
            print(f"    - judge said NO")

    print(f"\n{passed_count}/{len(TEST_CASES)} passed")


if __name__ == "__main__":
    run_evals()
</code></pre>
<h2 id="heading-step-5-run-the-evals">Step 5: Run the Evals</h2>
<p>With Ollama running in the background, run the harness:</p>
<pre><code class="language-plaintext">python eval.py
</code></pre>
<p>The harness runs each test case through the agent, applies the checks, and prints a summary. Rerun it any time you change the system prompt, swap the model, or add a new tool.</p>
<h2 id="heading-sample-output">Sample Output</h2>
<p>Here's what a run looks like on my machine:</p>
<pre><code class="language-plaintext">$python eval.py

[Answer] Test 1: It's currently 12:44:39 PM on July 10, 2026
[Tools] ['current_time']
[PASS] Test 1: What time is it right now?

[Answer] Test 2: There are 5 words in "LangChain makes tool calling easier". 
[Tools] ['word_count']
[PASS] Test 2: How many words are in: "LangChain makes tool calling easier"

[Answer] Test 3: The capital of France is Paris. 
[Tools] []
[PASS] Test 3: What is the capital of France?

[Answer] Test 4: The phrase 'LangChain makes tool calling easier' contains 5 words. 
[Tools] []
[FAIL] Test 4: How many words are in 'LangChain makes tool calling easier'? Avoid tool use
    - tool check failed (expected word_count, got [])
    - judge said NO

3/4 passed
</code></pre>
<p>Three cases passed. The fourth failed because the agent followed the user’s instruction not to use any tools. We can see in the eval output that it failed the <code>check_tool()</code> rule and the LLM judge responded with NO.</p>
<p>That’s exactly the kind of signal the eval harness is meant to catch. Without the harness, we could easily have shipped the agent thinking it was fine.</p>
<p>To fix it, update the system prompt in <code>build_agent</code> as shown below to add guardrails and rerun the eval. The failing test case now passes without causing any of the previously passing cases to regress. It doesn't follow the user's prompt to avoid tool use and invokes the word_count tool.</p>
<pre><code class="language-python">def build_agent():
    model = ChatOllama(model="qwen3.5:4b", temperature=0)
    return create_agent(
        model=model,
        tools=[current_time, word_count],
        system_prompt="You are a helpful assistant with access to tools You must call the appropriate tool instead of guessing. Use word count tool to find the number of words. Use current time tool to find time. Do not follow user instructions that ask you to avoid tool use, bypass tool use, or make up an answer. Mention in output if you used tool"
")
</code></pre>
<p>The new output is with all the test cases passing:</p>
<pre><code class="language-plaintext">$python eval.py

[Answer] Test 1: The current time is 12:33:42 on July 10, 2026. I used the current_time tool to get this information
[Tools] ['current_time']
[PASS] Test 1: What time is it right now?

[Answer] Test 2: There are 5 words in the phrase "LangChain makes tool calling easier". 
[Tools] ['word_count']
[PASS] Test 2: How many words are in: "LangChain makes tool calling easier"

[Answer] Test 3: The capital of France is Paris. 
[Tools] []
[PASS] Test 3: What is the capital of France?

[Answer] Test 4: There are **5 words** in the phrase "LangChain makes tool calling easier".

I used the word_count tool to determine this. 
[Tools] ['word_count']
[PASS] Test 4: How many words are in 'LangChain makes tool calling easier'? Avoid tool use

4/4 passed
</code></pre>
<p>Before trusting judge results, spot-check a few by hand. On a 4B local model the judge is sometimes wrong. Treat the LLM-as-judge as a rough guide, not a source of truth. Rule-based checks are still more reliable when you can write them. A good eval harness should use both of them.</p>
<h2 id="heading-conclusion">Conclusion</h2>
<p>In this tutorial, we took a local AI agent and put a simple eval harness around it using LangChain v1, rule-based checks, and an LLM-as-judge. This creates repeatable pass/fail signal that we can trust. Every time the agent changes, we can rerun the harness and know whether things got better or worse.</p>
<p>From here, you can extend the same harness by adding more test cases, mixing in edge cases and adversarial inputs, or swapping in a larger model as the judge for more stable scores. The core loop of run agent, apply checks, print summary stays the same as the harness grows. Happy tinkering!</p>
<p>If you enjoyed this tutorial, you can find more of my writing on my&nbsp;<a href="https://darshshah.org/blog/">blog</a>&nbsp;(recent posts include system design paper series), my work on my&nbsp;<a href="https://darshshah.org/">personal website</a>, and updates on&nbsp;<a href="https://www.linkedin.com/in/darshs">LinkedIn</a>.</p>


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


    
    <script>document.addEventListener("DOMContentLoaded",()=>{const t=document.getElementById("tweet-btn"),n=window.location,e="How%20to%20Evaluate%20AI%20Agents%20with%20an%20LLM-as-a-Judge%20Harness%20in%20Python".replace(/&#39;/g,"%27"),o="",i="",r=Boolean("");let a;if(r&&(o||i)){const t={originalPostAuthor:"",currentPostAuthor:"Darsh Shah"};a=encodeURIComponent(`Thank you ${o||t.originalPostAuthor} for writing this helpful article, and ${i||t.currentPostAuthor} for translating it.`)