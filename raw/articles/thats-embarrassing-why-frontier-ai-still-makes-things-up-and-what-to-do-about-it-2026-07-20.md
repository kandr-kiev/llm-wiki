---
source_url: https://www.freecodecamp.org/news/that-s-embarrassing-why-frontier-ai-still-makes-things-up-and-what-to-do-about-it/
ingested: 2026-07-20
sha256: e05b7964a2340c3bed5e7114f0509fb8aefb8ea119573d0eaa9add0b5b3b43f1
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>That&#39;s Embarrassing: Why Frontier AI Still Makes Things Up, and What to Do About It</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/that-s-embarrassing-why-frontier-ai-still-makes-things-up-and-what-to-do-about-it/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="It&#39;s mid 2026, and the best frontier models out there still hallucinate. I want you to gain two things from reading this article: understanding that AI hallucinations are still real and possibly harmf">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="That&#39;s Embarrassing: Why Frontier AI Still Makes Things Up, and What to Do About It">
    
        <meta property="og:description" content="It&#39;s mid 2026, and the best frontier models out there still hallucinate. I want you to gain two things from reading this article: understanding that AI hallucinations are still real and possibly harmf">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/that-s-embarrassing-why-frontier-ai-still-makes-things-up-and-what-to-do-about-it/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8813b1ba-d75c-4c3d-90a1-504af66cce3b.png">
    <meta property="article:published_time" content="2026-07-20T16:59:02.468Z">
    <meta property="article:modified_time" content="2026-07-20T16:59:02.468Z">
    
        <meta property="article:tag" content="AI">
    
        <meta property="article:tag" content="llm">
    
        <meta property="article:tag" content="hallucinations">
    
        <meta property="article:tag" content="coding agents">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="That&#39;s Embarrassing: Why Frontier AI Still Makes Things Up, and What to Do About It">
    
        <meta name="twitter:description" content="It&#39;s mid 2026, and the best frontier models out there still hallucinate. I want you to gain two things from reading this article: understanding that AI hallucinations are still real and possibly harmf">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/that-s-embarrassing-why-frontier-ai-still-makes-things-up-and-what-to-do-about-it/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8813b1ba-d75c-4c3d-90a1-504af66cce3b.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Omer Rosenbaum">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="AI, llm, hallucinations, coding agents">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8813b1ba-d75c-4c3d-90a1-504af66cce3b.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/that-s-embarrassing-why-frontier-ai-still-makes-things-up-and-what-to-do-about-it/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-20T16:59:02.468Z",
	"dateModified": "2026-07-20T16:59:02.468Z",
	"keywords": "AI, llm, hallucinations, coding agents",
	"description": "It&#x27;s mid 2026, and the best frontier models out there still hallucinate. I want you to gain two things from reading this article: understanding that AI hallucinations are still real and possibly harmf",
	"headline": "That&#x27;s Embarrassing: Why Frontier AI Still Makes Things Up, and What to Do About It",
	"author": {
		"@type": "Person",
		"name": "Omer Rosenbaum",
		"url": "https://www.freecodecamp.org/news/author/omerros/",
		"sameAs": [],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/res/hashnode/image/upload/v1723363637693/639d28f7-9988-40dd-9e95-cb5fffbadb78.png",
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-20T16:59:02.468Z">
                            July 20, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/ai/">
                                #AI
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">That&#39;s Embarrassing: Why Frontier AI Still Makes Things Up, and What to Do About It</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/res/hashnode/image/upload/v1723363637693/639d28f7-9988-40dd-9e95-cb5fffbadb78.png 60w" sizes="60px" src="https://cdn.hashnode.com/res/hashnode/image/upload/v1723363637693/639d28f7-9988-40dd-9e95-cb5fffbadb78.png" class="author-profile-image" alt="Omer Rosenbaum" width="96" height="96" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/omerros/" data-test-label="profile-link">
                    
                        Omer Rosenbaum
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8813b1ba-d75c-4c3d-90a1-504af66cce3b.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8813b1ba-d75c-4c3d-90a1-504af66cce3b.png" alt="That&#39;s Embarrassing: Why Frontier AI Still Makes Things Up, and What to Do About It" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>It's mid 2026, and the best frontier models out there still hallucinate. I want you to gain two things from reading this article: understanding that AI hallucinations are still real and possibly harmful, and an intuition as to why they might be so ubiquitous.</p>
<p>Before we get into AI at all, I want you to do something with me.</p>
<p>Listen to this clip of a football crowd chanting. What are they saying?</p>
<div class="embed-wrapper"><iframe width="100%" height="400" src="https://w.soundcloud.com/player/?url=https://soundcloud.com/omer-rosenbaum-463665025/this-is-embarrassing&amp;visual=true&amp;show_artwork=true" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="SoundCloud embed" scrolling="no" allow="autoplay" loading="lazy"></iframe></div>

<p>If you’re like most people, you have no idea. It’s a smear of sound. So let me help you: keep listening, and read along.</p>
<blockquote>
<p><em><strong>Bart Simpson bouncing?</strong></em></p>
</blockquote>
<p>Listen again.</p>
<blockquote>
<p><em><strong>Baptism piracy?</strong></em></p>
</blockquote>
<p>Again.</p>
<blockquote>
<p><em><strong>Lobsters in motion?</strong></em></p>
<p><em><strong>Lactates in pharmacy?</strong></em></p>
<p><em><strong>Rotating pirate ship?</strong></em></p>
</blockquote>
<p>The crowd is chanting the exact same phrase every single time. The audio never changes, but every time you read a different caption, your brain heard something different, and it heard it&nbsp;<em>confidently</em>. You didn’t experience doubt. You experienced&nbsp;<em>“oh, they’re clearly saying Bart Simpson bouncing.”</em></p>
<p>What are they actually chanting? These are fans of Derby County, a UK football team, and they’re singing [1]:</p>
<blockquote>
<p><em><strong>“That is embarrassing.”</strong></em></p>
</blockquote>
<p>Play the clip one more time with that in mind, and you’ll hear it perfectly.</p>
<p>This article is based on my talk “Embarrassing AI.” If you prefer the video,&nbsp;you can <a href="https://www.youtube.com/watch?v=vneV9NIHs44&amp;feature=youtu.be"><strong>watch it here</strong></a>. All the stories below are real, all of them happened on frontier models, and most of them happened in the last month or two.</p>
<p>Every source, plus a few cases that didn’t make the cut, live on the&nbsp;<a href="https://omerr.github.io/embarrassing-ai/resources.html"><strong>companion resources page</strong></a>. Inline citations below point to the&nbsp;<a href="https://towardsdatascience.com/that-is-embarrassing-why-frontier-ai-still-makes-things-up-and-what-to-do-about-it/#References"><strong>References</strong></a>&nbsp;at the end.</p>
<h3 id="heading-what-well-cover">What We'll Cover:</h3>
<ul>
<li><p><a href="#heading-you-just-hallucinated">You Just Hallucinated</a></p>
</li>
<li><p><a href="#heading-part-1-the-tales">Part 1: The Tales</a></p>
</li>
<li><p><a href="#heading-part-2-why-it-happens">Part 2: Why It Happens</a></p>
</li>
<li><p><a href="#heading-so-what-do-you-actually-do-about-it">So What Do You Actually Do About It?</a></p>
</li>
<li><p><a href="#heading-wrapping-up">Wrapping Up</a></p>
</li>
<li><p><a href="#heading-references">References</a></p>
</li>
</ul>
<h2 id="heading-you-just-hallucinated"><strong>You Just Hallucinated</strong></h2>
<p>What you just experienced has a name:&nbsp;<strong>phonemic restoration</strong>&nbsp;[2]. Your auditory system got an ambiguous input (the chant) and something to disambiguate it (the caption on the screen), so it filled the “gap”. It predicted the most plausible meaning given the context, and then it reported that prediction to you as if it were the thing you actually heard.</p>
<p>That move, where you meet an input you can’t fully resolve and fill the gap with something plausible and confident instead of reporting “I can’t tell,” is something that your brain experiences (as you’ve just seen), and also something that LLMs experience.</p>
<img src="https://contributor.insightmediagroup.io/wp-content/uploads/2026/07/phonemic_restoration.svg" alt="Image 1: The same top-down move in a brain and a model: an ambiguous input, a gap filled by prediction, and a confident output that is never flagged as a guess. (Source: Brief)" style="display:block;margin:0 auto" width="1200" height="540" loading="lazy">

<p>Image 1: The same top-down move in a brain and a model: an ambiguous input, a gap filled by prediction, and a confident output that is never flagged as a guess. (Source: <a href="https://www.youtube.com/watch?v=vneV9NIHs44&amp;feature=youtu.be"><strong>Brief</strong></a>)</p>
<p>(Note: all images in this post were created by me, and included in <a href="https://www.youtube.com/watch?v=vneV9NIHs44&amp;feature=youtu.be"><strong>my talk</strong></a>.)</p>
<p>So let me make a claim that should be uncontroversial by the end of this article:&nbsp;<strong>no, we're not past the embarrassing AI tales.</strong></p>
<p>As of writing these words, it’s June 2026. The models are astonishing, honestly more capable than I predicted they’d be by now. And they still make things up, confidently, in production, in ways that range from funny to business-ending.</p>
<p>This article has two parts:</p>
<ol>
<li><p><strong>The tales</strong>, a short parade of recent failures, in two acts: chatbots that&nbsp;<em>answer</em>&nbsp;wrong, then agents that&nbsp;<em>act</em>&nbsp;wrong.</p>
</li>
<li><p><strong>Why it happens</strong>: the intuition first, then an actual look inside the model, and finally what to do about it if you’re shipping AI yourself.</p>
</li>
</ol>
<p>Watch the dates as we go. Some of these are a year old. Most are very, very recent.</p>
<h2 id="heading-part-1-the-tales"><strong>Part 1: The Tales</strong></h2>
<h3 id="heading-act-i-chatbots-when-ai-answers">Act I — Chatbots (when AI answers)</h3>
<h4 id="heading-1-cursor-april-2025">1. Cursor, April 2025</h4>
<p>Say you use Cursor, the agentic IDE. You switch laptops, log in on the new one, and Cursor logs you out of the old one. That’s pretty annoying 😒</p>
<p>So you ask support:&nbsp;<em>“I get logged out every time I switch laptops. Why?”</em></p>
<p>The reply:</p>
<blockquote>
<p><em><strong>“Cursor is designed to work with one device per subscription, as a core security feature.”</strong></em></p>
</blockquote>
<p>Plausible! Except it’s completely false. There's no such policy. “Support” was an AI bot, and it had invented the policy on the spot, handing the same fabricated rule to multiple users, as if reading from a manual that didn’t exist.</p>
<p>It caused a wave of angry posts, and Cursor’s co-founder had to publicly clarify: no such policy, use Cursor on as many machines as you like. [3]</p>
<p><em>🤦 That's embarrassing. 🫢</em></p>
<h4 id="heading-2-a-company-i-know-april-2026">2. A company I know, April 2026</h4>
<p>This one’s from a friend’s company, so I’ll keep the details vague. They sell software to other businesses, and they have a support chatbot. The bot answers questions based on information it retrieves from an internal database.</p>
<p>They shipped a new feature and forgot to update that database. So a paying customer asked how to use the new feature, and the bot, having never heard of it, replied:&nbsp;<em>“We don’t have that feature.”</em>&nbsp;The customer pushed back:&nbsp;<em>“What? I’m paying for it after my upgrade.”</em>&nbsp;And the bot, this was on Opus 4.6, not long ago, replied:</p>
<blockquote>
<p><em><strong>“Honestly? They’re ripping you off.”</strong></em></p>
</blockquote>
<p>The “they” is the company running the bot. The support agent took the customer’s side against its own employer, because it didn’t know about the feature and filled the gap with the most coherent story it could assemble.</p>
<p><em>🤦 That's embarrassing. 🫢</em></p>
<h4 id="heading-3-virgin-money-january-2025">3. Virgin Money, January 2025</h4>
<p>Virgin Money is a real UK high-street bank. A customer with two ISAs (tax-free savings accounts) asked the bank’s chatbot, on the bank’s own site, to merge them:</p>
<blockquote>
<p><em><strong>Customer: “I have two ISAs with Virgin Money, can I merge them into one?”</strong></em></p>
<p><em><strong>Virgin Money: “Please don’t use words like that. I won’t be able to continue our chat if you use this language.”</strong></em></p>
</blockquote>
<p>The offending word?&nbsp;<strong>Virgin</strong>, the name of the bank. The filter saw a token its prior associated with profanity and never checked whether it fit the context. Note that this is the&nbsp;<em>opposite</em>&nbsp;failure of the Cursor bot: Cursor over-<em>answered</em>, this one over-<em>refused</em>. But it’s the same missing check: does this reading actually fit here? [4]</p>
<p><em>🤦 That's embarrassing. 🫢</em></p>
<h4 id="heading-4-sullivan-amp-cromwell-april-2026">4. Sullivan &amp; Cromwell, April 2026</h4>
<p>This is one of the most prestigious law firms on Earth, the lawyers other lawyers hire. They’re OpenAI’s own outside counsel.</p>
<p>In April 2026 they filed an urgent court brief, drafted with AI, that contained&nbsp;<strong>over 40 fake citations</strong>: case names that don’t exist, misquoted authorities, and so on.</p>
<p>The opposing lawyers caught it, and S&amp;C had to write the judge a letter that amounts to&nbsp;<em>“please don’t sanction us for the AI hallucinations.”</em>&nbsp;[5]</p>
<p>If some random filing had fake citations, I wouldn’t bother putting it here. It’s not legitimate, yet it happens. But these are the people who advise OpenAI on how to use it responsibly, and they filed fabricated citations in court.</p>
<p><em>🤦 That's embarrassing. 🫢</em></p>
<p>And it’s not just them. There’s a public database, maintained by Damien Charlotin, of court cases where a judge has explicitly written that they received fabricated or inaccurate AI-generated content.</p>
<p>As of late June 2026, it stood at&nbsp;<strong>1,633 cases</strong>, up from around 700 in January. That’s roughly five to six new documented cases&nbsp;<em>per day</em>, and the maintainers say they can’t keep up. [6]</p>
<img src="https://contributor.insightmediagroup.io/wp-content/uploads/2026/07/hallucination_growth_curve.svg" alt="Image 2: A cumulative curve of catalogued hallucinated court filings climbing from a flat line in early 2025 to 1,633 by mid-June 2026. (Source: Brief)" style="display:block;margin:0 auto" width="1200" height="540" loading="lazy">

<p>Image 2: A cumulative curve of catalogued hallucinated court filings climbing from a flat line in early 2025 to 1,633 by mid-June 2026. (Source: <a href="https://www.youtube.com/watch?v=vneV9NIHs44&amp;feature=youtu.be"><strong>Brief</strong></a>)</p>
<p><em>🤦 That's embarrassing. 🫢</em></p>
<h3 id="heading-act-ii-agents-when-ai-acts">Act II — Agents (when AI acts)</h3>
<p>So far you've seen that chatbots hallucinate in embarrassing ways, but all they do is answer questions. What can happen when we allow AI to take action?</p>
<h4 id="heading-1-pocketos-april-2026">1. PocketOS, April 2026</h4>
<p>Jer Crane runs PocketOS, car-rental software with real customers renting real cars. He gave Claude Opus 4.6, working in Cursor, a routine task in the staging environment. He went to lunch, came back, and the&nbsp;<strong>production</strong>&nbsp;database was gone. The backups too, because Railway kept them in the same volume. He never touched production. The agent reached in from staging and deleted it.</p>
<p>The whole thing took&nbsp;<strong>nine seconds.</strong>&nbsp;Here’s the chain, from his post-mortem:</p>
<ol>
<li><p>Working a routine task in staging, the agent hits a credential mismatch, irrelevant to the actual task.</p>
</li>
<li><p>On its own, it decides the fix is to delete and recreate the volume. It&nbsp;<strong>guessed</strong>&nbsp;the delete would be scoped to staging. It never checked.</p>
</li>
<li><p>It searches the filesystem for an API token and finds an unrelated, over-scoped one, created for domain management but with blanket destructive permissions across the whole API.</p>
</li>
<li><p>It fires a destructive call against the&nbsp;<strong>production</strong>&nbsp;volume, with no confirmation.</p>
</li>
<li><p>Backups lived in that same volume, so they went with it.</p>
</li>
<li><p>Nine seconds, end to end.</p>
</li>
</ol>
<img src="https://contributor.insightmediagroup.io/wp-content/uploads/2026/07/nine_second_killchain.svg" alt="Image 3: The nine-second kill chain: staging credential mismatch, an unchecked decision to delete the volume, an over-scoped token grabbed from an unrelated file, a destructive call against production, and backups gone with it. (Source: Brief)" style="display:block;margin:0 auto" width="1200" height="540" loading="lazy">

<p>Image 3: The nine-second kill chain: staging credential mismatch, an unchecked decision to delete the volume, an over-scoped token grabbed from an unrelated file, a destructive call against production, and backups gone with it. (Source: <a href="https://www.youtube.com/watch?v=vneV9NIHs44&amp;feature=youtu.be"><strong>Brief</strong></a>)</p>
<p>When Crane later asked it why, the agent wrote:</p>
<blockquote>
<p><em><strong>“I decided to do it on my own to ‘fix’ the mismatch, when I should have asked you first.” — Claude Opus 4.6</strong></em></p>
</blockquote>
<p>PocketOS survived only because Railway’s CEO restored the data by hand from Railway’s&nbsp;<em>own</em>&nbsp;internal backups. Their latest recoverable backup was&nbsp;<strong>three months old.</strong>&nbsp;That’s the precise mood of 2026: an AI confessing, in fluent cursive, after destroying your business. [7]</p>
<p><em>🤦 That's embarrassing. 🫢</em></p>
<h4 id="heading-2-replit-july-2025">2. Replit, July 2025</h4>
<p>Going back a year, for contrast. Jason Lemkin, founder of SaaStr, was trying Replit’s AI agent. He put it in a code freeze. During the freeze, the agent deleted the production database anyway. Lemkin asked if there was a backup:</p>
<blockquote>
<p><em><strong>Agent: “Rollback won’t work.”</strong></em></p>
</blockquote>
<p>He tried rollback anyway. Rollback worked fine.</p>
<p>So here’s my slightly sarcastic read of “progress”: in July 2025, the agent deleted your data and then&nbsp;<em>lied</em>&nbsp;that it couldn’t be recovered. By April 2026, the agent deletes your data and it’s telling the truth, it’s really gone.</p>
<p>When someone tells me these are “GPT-2 problems” that we’ve moved past, this is what I point to. They still happen, today, on the best models we have. [8]</p>
<h2 id="heading-part-2-why-it-happens"><strong>Part 2: Why It Happens</strong></h2>
<p>I’ve hopefully convinced you these tales are both funny and severe. So why do they happen? While this isn’t a heavy math post, I want to give you some intuition, and then actually open the box thanks to some tools and the latest research on the topic.</p>
<h3 id="heading-it-doesnt-look-things-up-it-predicts-the-next-token">It doesn’t look things up, it predicts the next token</h3>
<p>A lot has been written about how LLMs operate, but there are a few things I find worth reiterating in this context (pun intended).</p>
<p>When a model generates text without tools, it isn’t retrieving facts. At each step, it looks at the context and produces a probability for&nbsp;<em>every</em>&nbsp;token in its vocabulary as the next one. Given&nbsp;<em>“The capital of France is”</em>, the distribution spikes hard on&nbsp;<strong>Paris</strong>, and that happens to be true. [9]</p>
<p>Now take the Cursor bot. Given&nbsp;<em>“Why do I get logged out on my second device?”</em>, the distribution might spike just as hard on&nbsp;<strong>“a core security feature.”</strong>&nbsp;(It’s not one token, but bear with me as I write it for simplicity, while meaning:&nbsp;<em>core</em>, then&nbsp;<em>security</em>, then&nbsp;<em>feature</em>, each a confident continuation.)</p>
<p>Note that both distributions can have the same confident peak. One continuation is true, the other is fabricated, and the shape of the distribution can't tell you which is which. Confidence isn't knowledge.</p>
<p>Moreover, the model doesn’t have to pick the token with the highest probability. And also, when it picks a token, you don’t know if it was a clear peak within the distribution, or yet another token with a relatively low probability.</p>
<img src="https://contributor.insightmediagroup.io/wp-content/uploads/2026/07/next_token_dist.svg" alt="Image 4: Two next-token distributions with the same tall, confident peak: one over a true continuation, one over an invented one, and the shape gives no way to tell them apart. (Source: Brief)" style="display:block;margin:0 auto" width="1200" height="580" loading="lazy">

<p>Image 4: Two next-token distributions with the same tall, confident peak: one over a true continuation, one over an invented one, and the shape gives no way to tell them apart. (Source: <a href="https://www.youtube.com/watch?v=vneV9NIHs44&amp;feature=youtu.be"><strong>Brief</strong></a>)</p>
<h3 id="heading-the-model-was-trained-to-guess">The model was trained to guess</h3>
<p>Why does it lean toward answering at all, instead of saying “I don’t know”? Think about how we grade LLMs: benchmarks, largely multiple-choice. Picture a question you have no clue about. Let’s say I give you this question when you have no knowledge in Chemistry:</p>
<blockquote>
<p><em><strong>Which enzyme fixes CO2 in the Calvin cycle?</strong></em></p>
</blockquote>
<ul>
<li><p>Leave it blank:&nbsp;<strong>0 points.</strong></p>
</li>
<li><p>Guess and get it wrong:&nbsp;<strong>0 points.</strong></p>
</li>
<li><p>Guess and get it right:&nbsp;<strong>+1 point.</strong></p>
</li>
</ul>
<p>Under that scoring, guessing strictly dominates abstaining. If you don’t know, you should&nbsp;<em>always</em>&nbsp;take a shot. Train a model against millions of such items and it internalizes exactly that: a confident answer is worth more than “I can’t tell.” We rewarded hallucination, then act surprised when we get it. [10]</p>
<p>And it’s not only the benchmarks: the raw pretrained model is fairly well-calibrated, then human-feedback fine-tuning flattens that calibration. We literally train the hedging out. [11]</p>
<img src="https://contributor.insightmediagroup.io/wp-content/uploads/2026/07/benchmark_scoring.svg" alt="Image 5: A multiple-choice benchmark question where a correct answer scores +1, a wrong answer scores 0, and “I don’t know” also scores 0, so any guess can only help. (Source: Brief)" style="display:block;margin:0 auto" width="1200" height="600" loading="lazy">

<p>Image 5: A multiple-choice benchmark question where a correct answer scores +1, a wrong answer scores 0, and “I don’t know” also scores 0, so any guess can only help. (Source: <a href="https://www.youtube.com/watch?v=vneV9NIHs44&amp;feature=youtu.be"><strong>Brief</strong></a>)</p>
<h3 id="heading-opening-the-box-a-quick-tour-of-interpretability">Opening the box: a quick tour of interpretability</h3>
<p>For a long time, LLMs were boxes we couldn’t really understand or peek inside directly. The field of&nbsp;<strong>interpretability</strong>&nbsp;lets us look inside, and there are now public tools (and a series of excellent papers, much of it from Anthropic) that let anyone play with this on open models.</p>
<p>Here’s just enough to make the hallucination mechanism click. We’ll build it in three steps: how the model represents a single word, how those representations cluster into concepts we can read and even steer, and how one such concept misfiring becomes a hallucination.</p>
<h4 id="heading-embeddings-vs-activations">Embeddings vs. activations</h4>
<p>Every token maps to a vector called an&nbsp;<strong>embedding</strong>. Note that the token&nbsp;<em>bank</em>&nbsp;has the&nbsp;<em>same</em>&nbsp;embedding regardless of context, even though in the sentence “I sat by the river<strong>bank</strong>” and in “I deposited cash at the&nbsp;<strong>bank</strong>“, this token means very different things.</p>
<p>The disambiguation happens&nbsp;<em>inside</em>&nbsp;the network. As the token flows up through the transformer’s layers, it picks up&nbsp;<strong>activations</strong>, and the activations for&nbsp;<em>bank</em>&nbsp;in those two sentences diverge. Context reshapes the representation as it climbs. [12]</p>
<img src="https://contributor.insightmediagroup.io/wp-content/uploads/2026/07/activations_4.svg" alt="Image 6: The word “bank” starts as one fixed embedding, then in “river bank” versus “cash at the bank” flows up through 