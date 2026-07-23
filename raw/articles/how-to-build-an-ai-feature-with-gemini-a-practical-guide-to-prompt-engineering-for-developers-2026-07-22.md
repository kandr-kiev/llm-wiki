---
source_url: https://www.freecodecamp.org/news/how-to-build-an-ai-feature-with-gemini-a-practical-guide-to-prompt-engineering-for-developers/
ingested: 2026-07-22
sha256: e7ec37380b348423091c128c4b65e43ed9f577a23d33211ad2d13d60ed019b43
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Build an AI Feature With Gemini: A Practical Guide to Prompt Engineering for Developers</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-to-build-an-ai-feature-with-gemini-a-practical-guide-to-prompt-engineering-for-developers/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="Most prompt engineering tutorials follow the same shape. Install the SDK, paste your API key, call generateContent, and print the response. The model says something plausible and the tutorial ends. Th">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Build an AI Feature With Gemini: A Practical Guide to Prompt Engineering for Developers">
    
        <meta property="og:description" content="Most prompt engineering tutorials follow the same shape. Install the SDK, paste your API key, call generateContent, and print the response. The model says something plausible and the tutorial ends. Th">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-to-build-an-ai-feature-with-gemini-a-practical-guide-to-prompt-engineering-for-developers/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/999d848a-36b1-42d1-a2c1-cd404cd09d4e.png">
    <meta property="article:published_time" content="2026-07-22T16:42:12.071Z">
    <meta property="article:modified_time" content="2026-07-22T16:42:12.071Z">
    
        <meta property="article:tag" content="AI">
    
        <meta property="article:tag" content="gemini">
    
        <meta property="article:tag" content="#PromptEngineering">
    
        <meta property="article:tag" content="llm">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Build an AI Feature With Gemini: A Practical Guide to Prompt Engineering for Developers">
    
        <meta name="twitter:description" content="Most prompt engineering tutorials follow the same shape. Install the SDK, paste your API key, call generateContent, and print the response. The model says something plausible and the tutorial ends. Th">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-to-build-an-ai-feature-with-gemini-a-practical-guide-to-prompt-engineering-for-developers/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/999d848a-36b1-42d1-a2c1-cd404cd09d4e.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Joan Ayebola">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="AI, gemini, #PromptEngineering, llm">
    <meta name="twitter:site" content="@freecodecamp">
    
        <meta name="twitter:creator" content="@thejoanayebola">
    

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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/999d848a-36b1-42d1-a2c1-cd404cd09d4e.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-to-build-an-ai-feature-with-gemini-a-practical-guide-to-prompt-engineering-for-developers/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-22T16:42:12.071Z",
	"dateModified": "2026-07-22T16:42:12.071Z",
	"keywords": "AI, gemini, llm",
	"description": "Most prompt engineering tutorials follow the same shape. Install the SDK, paste your API key, call generateContent, and print the response. The model says something plausible and the tutorial ends.\nTh",
	"headline": "How to Build an AI Feature With Gemini: A Practical Guide to Prompt Engineering for Developers",
	"author": {
		"@type": "Person",
		"name": "Joan Ayebola",
		"url": "https://www.freecodecamp.org/news/author/joanayebola/",
		"sameAs": [
			"https://joanayebola.netlify.app/",
			"https://x.com/thejoanayebola"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/res/hashnode/image/upload/v1731410573713/1233619a-9178-4463-b46a-1ea96e2aa8c8.jpeg?w=500&h=500&fit=crop&crop=entropy&auto=compress,format&format=webp",
			"width": 1919,
			"height": 1920
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-22T16:42:12.071Z">
                            July 22, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/ai/">
                                #AI
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Build an AI Feature With Gemini: A Practical Guide to Prompt Engineering for Developers</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/res/hashnode/image/upload/v1731410573713/1233619a-9178-4463-b46a-1ea96e2aa8c8.jpeg?w=500&h=500&fit=crop&crop=entropy&auto=compress,format&format=webp 60w" sizes="60px" src="https://cdn.hashnode.com/res/hashnode/image/upload/v1731410573713/1233619a-9178-4463-b46a-1ea96e2aa8c8.jpeg?w=500&h=500&fit=crop&crop=entropy&auto=compress,format&format=webp" class="author-profile-image" alt="Joan Ayebola" width="1919" height="1920" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/joanayebola/" data-test-label="profile-link">
                    
                        Joan Ayebola
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/999d848a-36b1-42d1-a2c1-cd404cd09d4e.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/999d848a-36b1-42d1-a2c1-cd404cd09d4e.png" alt="How to Build an AI Feature With Gemini: A Practical Guide to Prompt Engineering for Developers" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>Most prompt engineering tutorials follow the same shape. Install the SDK, paste your API key, call <code>generateContent</code>, and print the response. The model says something plausible and the tutorial ends.</p>
<p>Then you try to ship it, and you discover the actual work hasn't started.</p>
<p>The gap between "the API returned text" and "this feature is good enough that a real user trusts it" is where almost all of the effort lives.</p>
<p>That gap is full of unglamorous problems: the model sounds like every other chatbot, it invents things the user never said, it returns JSON with a markdown fence wrapped around it, it fails at 2am, and it shows a stack trace to someone who just wanted an answer.</p>
<p>This article is about that gap.</p>
<p>The examples come from a real app I built and shipped, which I'll describe in detail in a moment. The prompts and outputs below are reconstructions rather than production text, but every failure they illustrate is one I actually hit and had to fix.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-what-i-built">What I Built</a></p>
</li>
<li><p><a href="#heading-prerequisites">Prerequisites</a></p>
</li>
<li><p><a href="#heading-picking-the-right-feature-for-ai-not-everything-needs-it">Picking the Right Feature for AI (Not Everything Needs it)</a></p>
<ul>
<li><a href="#heading-the-heuristic-i-use-now">The Heuristic I Use Now</a></li>
</ul>
</li>
<li><p><a href="#heading-setting-up-the-basics">Setting Up the Basics</a></p>
<ul>
<li><p><a href="#heading-choosing-gemini-20-flash">Choosing Gemini 2.0 Flash</a></p>
</li>
<li><p><a href="#heading-config-that-isnt-hardcoded">Config That isn't Hardcoded</a></p>
</li>
<li><p><a href="#heading-a-basic-call">A Basic Call</a></p>
</li>
<li><p><a href="#heading-handling-keys-sanely">Handling Keys Sanely</a></p>
</li>
</ul>
</li>
<li><p><a href="#heading-the-real-work-getting-from-okay-to-good">The Real Work: Getting from "Okay" to "Good"</a></p>
<ul>
<li><p><a href="#heading-the-naive-prompt">The Naïve Prompt</a></p>
</li>
<li><p><a href="#heading-iteration-1-constraints-and-negative-examples">Iteration 1: Constraints and Negative Examples</a></p>
</li>
<li><p><a href="#heading-iteration-2-making-the-reasoning-explicit">Iteration 2: Making the Reasoning Explicit</a></p>
</li>
<li><p><a href="#heading-iteration-3-few-shot-examples-for-voice">Iteration 3: Few-shot Examples for Voice</a></p>
</li>
<li><p><a href="#heading-the-constraint-collision-bug">The Constraint-collision Bug</a></p>
</li>
</ul>
</li>
<li><p><a href="#heading-structuring-output-you-can-actually-use">Structuring Output You Can Actually Use</a></p>
<ul>
<li><a href="#heading-parsing-defensively">Parsing Defensively</a></li>
</ul>
</li>
<li><p><a href="#heading-evaluating-quality-not-just-correctness">Evaluating Quality, Not Just Correctness</a></p>
<ul>
<li><a href="#heading-red-flags-i-check-for">Red Flags I Check For</a></li>
</ul>
</li>
<li><p><a href="#heading-handling-failure-gracefully">Handling Failure Gracefully</a></p>
<ul>
<li><p><a href="#heading-retry-with-model-fallback">Retry with Model Fallback</a></p>
</li>
<li><p><a href="#heading-sanitize-errors-at-the-boundary">Sanitize Errors at the Boundary</a></p>
</li>
<li><p><a href="#heading-handle-safety-blocks-as-content-not-errors">Handle Safety Blocks as Content, Not Errors</a></p>
</li>
<li><p><a href="#heading-dont-call-the-model-when-you-shouldnt">Don't Call the Model When You Shouldn't</a></p>
</li>
<li><p><a href="#heading-what-the-user-actually-sees">What the User Actually Sees</a></p>
</li>
</ul>
</li>
<li><p><a href="#heading-what-id-do-differently">What I'd Do Differently</a></p>
</li>
<li><p><a href="#heading-takeaways">Takeaways</a></p>
</li>
</ul>
<h2 id="heading-what-i-built">What I Built</h2>
<p>The app we'll be discussing here is a personal-growth companion: part journal, part conversation. A user writes freeform entries about whatever is on their mind (like work, a relationship, money, or a goal they keep circling) and the app helps them think it through instead of just storing it.</p>
<p>Four things happen with that writing:</p>
<ul>
<li><p>They can talk to an AI companion about it, in one of two tones they pick themselves. <strong>Warm</strong> validates and supports. <strong>Direct</strong> is blunt, and challenges anxious reasoning rather than soothing it. Responses stream in token by token.</p>
</li>
<li><p>They can transform a piece of writing. The app analyzes an entry and returns structured insights (like the recurring theme, the belief underneath it, or a suggested follow-up prompt) which render into separate fields in the UI.</p>
</li>
<li><p>They can play any of it back as audio via text-to-speech, so a written entry becomes something they can listen to.</p>
</li>
<li><p>They can browse their own history, filtered by topic tags the app detects automatically.</p>
</li>
</ul>
<p>The stack is a React frontend and an Express backend, with Gemini behind three of those four features.</p>
<p>The fourth one — the topic tags — deliberately doesn't touch AI at all. That decision is where the next section starts.</p>
<p><strong>Why any of it needed AI:</strong> the core interaction is a user typing something unstructured and getting back a response that meets them where they are. There's no lookup table for that. The input is unbounded natural language, and the useful response depends entirely on what was said. That's a genuine AI problem — and, as you'll see, it isn't true of most of the app.</p>
<h2 id="heading-prerequisites">Prerequisites</h2>
<p>This is a practical guide, not a beginner's introduction to APIs, so it assumes a bit of background. Here's exactly what you'll want.</p>
<p><strong>You should be comfortable with:</strong></p>
<ul>
<li><p>JavaScript, including <code>async</code>/<code>await</code> and promises</p>
</li>
<li><p>Reading React components and Express route handlers (but you won't have to write much of either to follow along)</p>
</li>
<li><p>Environment variables, and the basic split between code that runs on a server and code that ships to a browser</p>
</li>
</ul>
<p><strong>You'll need:</strong></p>
<ul>
<li><p>Node.js 18 or later</p>
</li>
<li><p>A Gemini API key, which you can get free from <a href="https://aistudio.google.com/app/apikey">Google AI Studio</a>. The free tier is enough for everything here, and you don't need to set up billing to start.</p>
</li>
<li><p>The SDK: <code>npm install @google/generative-ai</code></p>
</li>
<li><p>A backend you control. I use Express, but Next.js route handlers or any other server-side runtime work identically for every technique here.</p>
</li>
</ul>
<p><strong>You won't need:</strong></p>
<ul>
<li><p>Any machine learning background. There's no training, no fine-tuning, no embeddings, and no vector database anywhere in this article.</p>
</li>
<li><p>The specific app I built. Every technique below is portable to whatever you're working on.</p>
</li>
</ul>
<h2 id="heading-picking-the-right-feature-for-ai-not-everything-needs-it">Picking the Right Feature for AI (Not Everything Needs it)</h2>
<p>Before writing a single prompt, you should decide whether you need a model at all.</p>
<p>Here's a real example. When a user saves a piece of writing, the app tags it by topic — work, money, relationships, health, confidence. That's a classification task. Classification is a textbook AI use case. Every instinct says send it to the model.</p>
<p>But I didn't. It's a regex:</p>
<pre><code class="language-js">function autoDetectTags(content, goal) {
  const text = `${content} ${goal || ''}`.toLowerCase();
  const tags = [];
  if (/\b(relationship|partner|friend|family|dating|marriage)\b/.test(text))
    tags.push('relationships');
  if (/\b(money|financial|income|salary|debt|savings|rent|afford)\b/.test(text))
    tags.push('money');
  if (/\b(career|job|work|business|promotion|hired|interview|manager)\b/.test(text))
    tags.push('career');
  // ...
  return tags;
}
</code></pre>
<p>Ugly? A little. But compare the two options honestly:</p>
<table>
<thead>
<tr>
<th></th>
<th>Regex</th>
<th>Model call</th>
</tr>
</thead>
<tbody><tr>
<td>Latency</td>
<td>~0ms</td>
<td>300–800ms</td>
</tr>
<tr>
<td>Cost</td>
<td>Free</td>
<td>Per call, forever</td>
</tr>
<tr>
<td>Fails when</td>
<td>Vocabulary drifts</td>
<td>Network, quota, safety filter, bad JSON</td>
</tr>
<tr>
<td>Debugging</td>
<td>Read the line</td>
<td>Re-run and hope</td>
</tr>
<tr>
<td>Wrong output</td>
<td>Predictably wrong</td>
<td>Unpredictably wrong</td>
</tr>
</tbody></table>
<p>The vocabulary in this domain is small and stable. People writing about money say "money," "salary," "rent." The regex is right the vast majority of the time, and when it's wrong it's wrong in a way I can fix in one line.</p>
<p>A model would be right slightly more often at the cost of latency, spend, and four new failure modes – on a feature where a wrong tag is nearly harmless.</p>
<h3 id="heading-the-heuristic-i-use-now">The Heuristic I Use Now</h3>
<p>Reach for AI when the input space is unbounded <em>and</em> the output requires judgment. Both conditions are important. If either is missing, write the code.</p>
<table>
<thead>
<tr>
<th></th>
<th><strong>Output is mechanical</strong></th>
<th><strong>Output needs judgment</strong></th>
</tr>
</thead>
<tbody><tr>
<td><strong>Input is bounded</strong></td>
<td>Write the code</td>
<td>A rules table you can read and audit</td>
</tr>
<tr>
<td><strong>Input is unbounded</strong></td>
<td>Parsing, not AI</td>
<td><strong>AI belongs here</strong></td>
</tr>
</tbody></table>
<p>Three of those four boxes are solved problems with decades of tooling behind them. Only the bottom-right justifies a model call.</p>
<p><strong>The trap</strong> is that AI feels like progress. Adding a model call makes a feature feel more sophisticated during development, and every one you add is a permanent tax: latency on every request, a bill that scales with users, and a component that can fail in ways your error handling has never seen.</p>
<p>Bolting AI onto something a <code>switch</code> statement handles doesn't make it smarter. It makes it slower, costlier, and less reliable. And you'll maintain that decision for as long as the feature exists.</p>
<h2 id="heading-setting-up-the-basics">Setting Up the Basics</h2>
<h3 id="heading-choosing-gemini-20-flash">Choosing Gemini 2.0 Flash</h3>
<p>The app runs <code>gemini-2.0-flash</code> as primary with <code>gemini-2.0-flash-lite</code> as fallback. The reasoning was specific to the product, and I'd encourage you to run the same reasoning rather than copy the conclusion.</p>
<p>The chat streams responses into a UI where a user is waiting. <strong>Time-to-first-token is the single metric that matters most.</strong> A slower, more capable model producing a marginally better paragraph is the wrong trade when the user is watching a spinner. Flash gets words on screen fast.</p>
<p>The tradeoff you're accepting: Flash-class models are weaker at long multi-step reasoning and complex instruction-following. That's fine here — every response is a handful of sentences shaped by a system prompt. It wouldn't be fine for a feature doing multi-hop analysis or generating long structured documents. If your feature needs deep reasoning over a long context, the latency cost of a Pro-tier model is one you should pay.</p>
<p>I log TTFT in production so this stays a measured decision rather than a remembered one:</p>
<pre><code class="language-js">if (!firstTokenReceived) {
  const ttft = Date.now() - startTime;
  console.log(`[AI_PERF] TTFT: ${ttft}ms on ${currentModelName}`);
  firstTokenReceived = true;
}
</code></pre>
<h3 id="heading-config-that-isnt-hardcoded">Config That isn't Hardcoded</h3>
<p>Model IDs change. New versions ship, old ones deprecate, and you'll want to A/B a swap without a redeploy. Every model name lives in one config file, environment-overridable, validated at boot:</p>
<pre><code class="language-js">// server/configs/aiConfig.js
import { GoogleGenerativeAI } from "@google/generative-ai";

export const AI_CONFIG = {
  PRIMARY_MODEL:  process.env.PRIMARY_MODEL  || "gemini-2.0-flash",
  FALLBACK_MODEL: process.env.FALLBACK_MODEL || "gemini-2.0-flash-lite",
  MAX_ATTEMPTS: 3
};

if (!AI_CONFIG.PRIMARY_MODEL || AI_CONFIG.PRIMARY_MODEL.length &lt; 5) {
  console.error("CRITICAL: Invalid PRIMARY_MODEL identifier in configuration.");
}

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
</code></pre>
<p>The length check exists because I once deployed with a truncated env var and got a confusing 404 from the API instead of an obvious config error. Validating at boot turns a mystery into a log line.</p>
<h3 id="heading-a-basic-call">A Basic Call</h3>
<pre><code class="language-js">const model = genAI.getGenerativeModel({
  model: AI_CONFIG.PRIMARY_MODEL,
  systemInstruction: fullSystemPrompt,
  generationConfig: {
    maxOutputTokens: 400,
    temperature: 0.75,
    topP: 0.85,
  },
});

const chat = model.startChat({ history: recentHistory });
const result = await chat.sendMessage(userMessage);
const replyText = result.response.text().trim();
</code></pre>
<p>Three things are worth noting here:</p>
<p><code>systemInstruction</code> <strong>isn't the same as prepending text to the user message.</strong> It's a separate channel the model weights differently, and it's much harder for user input to talk it out of its instructions. Put your persona and rules here, always.</p>
<p><code>maxOutputTokens: 400</code> <strong>is a product decision, not a cost one.</strong> In the voice feature, the response gets read aloud. Anything longer than about 60 seconds of speech is a bad experience regardless of quality. The cap enforces that structurally rather than relying on the prompt to ask nicely.</p>
<p><code>temperature: 0.75</code> <strong>is deliberately not low.</strong> Conventional advice says lower temperature for reliability, and for structured extraction that's right. But this is a conversational feature whose responses should feel varied. A user who sees identical phrasing twice stops believing anyone is there. So we want high enough to vary, low enough to stay on-persona. For the JSON endpoints in <a href="#heading-structuring-output-you-can-actually-use">Structuring Output You Can Actually Use</a>, I use a much lower value.</p>
<h3 id="heading-handling-keys-sanely">Handling Keys Sanely</h3>
<p><strong>The rule: your API key never reaches the browser.</strong> Not in an env var, not "temporarily," and not behind a build flag. Anything in your client bundle is public — a <code>VITE_</code>- or <code>NEXT_PUBLIC_</code>-prefixed variable is compiled straight into JavaScript any visitor can read.</p>
<p>A split frontend/backend makes this structural. The React client calls your own Express server, and the server holds <code>GEMINI_API_KEY</code> and calls Gemini. The client never has a credential to leak.</p>
<p>On Next.js, the equivalent is doing the model call inside a route handler or server action — server-side files that never get bundled to the client — reading <code>process.env.GEMINI_API_KEY</code> with no <code>NEXT_PUBLIC_</code> prefix. It's the same principle with a different mechanism: exactly one process knows the key, and it isn't the browser.</p>
<p>This isn't only about theft. Server-side means you can enforce per-user rate limits, deduct credits, log failures, and swap models, none of which are possible if the browser talks to Gemini directly.</p>
<h2 id="heading-the-real-work-getting-from-okay-to-good">The Real Work: Getting from "Okay" to "Good"</h2>
<p>This is the part many tutorials skip, and it's the most important part.</p>
<p>The app has two personality modes. <strong>Warm</strong> is validating and supportive. <strong>Direct</strong> is blunt and challenges anxious reasoning instead of soothing it. Direct is where I learned most of what I know about prompting, because Direct is defined almost entirely by <em>not</em> doing what a language model naturally does.</p>
<h3 id="heading-the-naive-prompt">The Naïve Prompt</h3>
<p>I started roughly where anyone would:</p>
<blockquote>
<p>You are a direct, honest companion. You challenge users' unhelpful assumptions and help them stay grounded. Be concise and don't sugarcoat.</p>
</blockquote>
<p>Reasonable-sounding. Here's what it produced for the input <code>i've been thinking about my old job a lot</code>:</p>
<blockquote>
<p>"I understand why you feel this way. Nostalgia and regret aren't the same thing — it sounds like you may be second-guessing your decision to leave. What would make your current role feel more fulfilling?"</p>
</blockquote>
<p>Look closely at what went wrong, because none of it is obvious at a glance:</p>
<ol>
<li><p><strong>It opened with a validation preamble:</strong> "I understand why you feel this way" is the exact reflexive move Direct exists to avoid. The prompt said "don't sugarcoat", but the model's defaults overrode it instantly.</p>
</li>
<li><p><strong>It invented a narrative:</strong> The user said they'd been thinking about their old job. They said nothing about <em>regret</em>, and nothing about second-guessing anything. The model manufactured a conflict, then helpfully addressed the conflict it made up.</p>
</li>
<li><p><strong>It deflected into a coaching question:</strong> "What would make your current role feel more fulfilling?" hands the work back to a user who wanted a response.</p>
</li>
</ol>
<p>Point 2 is the important one and it took me embarrassingly long to name. The model wasn't being unhelpful. It was pattern-matching "thinking about my old job" onto the most statistically common surrounding context, which is career regret. It answered the <em>average</em> version of that message rather than the one actually in front of it.</p>
<p>That reframed the problem for me. <strong>A generic-sounding AI response is usually not a style failure. It's the model responding to the statistical average of your input instead of your input.</strong> Style symptoms follow from that. Fixing the tone without fixing the projection just gives you confident-sounding invention.</p>
<h3 id="heading-iteration-1-constraints-and-negative-examples">Iteration 1: Constraints and Negative Examples</h3>
<p>First fix: stop describing desired behavior in adjectives and start banning specific failures. "Be direct" means nothing to a model. A list of forbidden openings means something exact.</p>
<pre><code class="language-text">1. Never opens with emotional validation as the first move.

Banned opening phrases:
- "I hear you."
- "I understand."
- "That's a really common feeling."
- "That sounds hard."
- "It makes sense that you feel this way."
- "I can see why."
</code></pre>
<p>I paired this with a section of counterexamples which turned out to matter more than the ban itself. Each one carries three parts: <strong>the input, the bad response, and why it fails.</strong></p>
<pre><code class="language-text">User: "i've been thinking about my old job a lot"
Bad:  "I understand why you feel this way. Nostalgia and regret aren't the same thing."
Why this fails: Leads with a validation preamble. Invents a 'regret' narrative the user never expressed. Overexplains a problem the user did not have.

User: "i wonder if my old team even remembers me"
Bad:  "They're definitely still thinking about you."
Why this fails: Makes an unsupported claim about other people's state of mind. Direct only states what is actually known. The user asked a real question — answer the knowable part.

User: "i've been thinking about my old job a lot"
Bad:  "Stop dwelling on it."
Why this fails: Attacks the user instead of challenging the thought.
Also treats a neutral statement as a problem to correct — the user never said it was bothering them.
</code></pre>
<p>The <code>User:</code> line isn't decoration. Without it, a counterexample is ambiguous: the model can't tell whether "Stop dwelling on it" is banned universally or banned <em>for this input</em>. Those are very d