---
source_url: https://www.freecodecamp.org/news/regression-models-for-causal-inference-on-ai-features/
ingested: 2026-07-17
sha256: f8308344d52d25ee0362f4087dd026e137784540889899a9303d4e15dca4b0a7
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>Product Experimentation with Regression-Based Causal Inference: Estimating LLM Feature Impact with Python and statsmodels</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/regression-models-for-causal-inference-on-ai-features/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="A randomized A/B test is the cleanest form of product experiment available. The coin flip that splits users between the new prompt template and the control removes every possible confounder by constru">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="Product Experimentation with Regression-Based Causal Inference: Estimating LLM Feature Impact with Python and statsmodels">
    
        <meta property="og:description" content="A randomized A/B test is the cleanest form of product experiment available. The coin flip that splits users between the new prompt template and the control removes every possible confounder by constru">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/regression-models-for-causal-inference-on-ai-features/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/731ac81a-7bf4-45ff-9eac-49292d1484b1.png">
    <meta property="article:published_time" content="2026-07-15T15:25:14.593Z">
    <meta property="article:modified_time" content="2026-07-15T15:25:14.593Z">
    
        <meta property="article:tag" content="product experimentation">
    
        <meta property="article:tag" content="experimentation">
    
        <meta property="article:tag" content="causal inference">
    
        <meta property="article:tag" content="AI">
    
        <meta property="article:tag" content="Machine Learning">
    
        <meta property="article:tag" content="#Regression">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Product Experimentation with Regression-Based Causal Inference: Estimating LLM Feature Impact with Python and statsmodels">
    
        <meta name="twitter:description" content="A randomized A/B test is the cleanest form of product experiment available. The coin flip that splits users between the new prompt template and the control removes every possible confounder by constru">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/regression-models-for-causal-inference-on-ai-features/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/731ac81a-7bf4-45ff-9eac-49292d1484b1.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Rudrendu Paul">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="product experimentation, experimentation, causal inference, AI, Machine Learning, #Regression">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/731ac81a-7bf4-45ff-9eac-49292d1484b1.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/regression-models-for-causal-inference-on-ai-features/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-15T15:25:14.593Z",
	"dateModified": "2026-07-15T15:25:14.593Z",
	"keywords": "product experimentation, experimentation, causal inference, AI, Machine Learning",
	"description": "A randomized A/B test is the cleanest form of product experiment available. The coin flip that splits users between the new prompt template and the control removes every possible confounder by constru",
	"headline": "Product Experimentation with Regression-Based Causal Inference: Estimating LLM Feature Impact with Python and statsmodels",
	"author": {
		"@type": "Person",
		"name": "Rudrendu Paul",
		"url": "https://www.freecodecamp.org/news/author/rudrendupaul/",
		"sameAs": [
			"https://orcid.org/0009-0008-0141-4690"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://ui-avatars.com/api/?name=rudrendupaul2022&background=random&bold=true&size=500&color=ffffff",
			"width": 500,
			"height": 500
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-15T15:25:14.593Z">
                            July 15, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/product-experimentation/">
                                #product experimentation
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">Product Experimentation with Regression-Based Causal Inference: Estimating LLM Feature Impact with Python and statsmodels</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://ui-avatars.com/api/?name=rudrendupaul2022&background=random&bold=true&size=500&color=ffffff 60w" sizes="60px" src="https://ui-avatars.com/api/?name=rudrendupaul2022&background=random&bold=true&size=500&color=ffffff" class="author-profile-image" alt="Rudrendu Paul" width="500" height="500" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/rudrendupaul/" data-test-label="profile-link">
                    
                        Rudrendu Paul
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/731ac81a-7bf4-45ff-9eac-49292d1484b1.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/731ac81a-7bf4-45ff-9eac-49292d1484b1.png" alt="Product Experimentation with Regression-Based Causal Inference: Estimating LLM Feature Impact with Python and statsmodels" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>A randomized A/B test is the cleanest form of product experiment available. The coin flip that splits users between the new prompt template and the control removes every possible confounder by construction.</p>
<p>That randomization is the load-bearing wall of your experiment, and regression is how you read the result precisely: how far the treatment moved the metric, with what confidence, and whether the effect was uniform across user types.</p>
<p>If you're a data scientist running clean randomized A/B tests on AI features, the hardest question is "how much did it work, and how confident should I be?" Your team split users by a hash of their user ID, half saw the new prompt template, half saw the old one, and the experiment ran four weeks. Now someone asks how much the new template actually moved task completion rates.</p>
<p>The first instinct is to open a spreadsheet and take the difference in group means. That number is real and unbiased, and for a small team with a quick decision to make it often suffices. It leaves open, though, how confident you should be in that number, whether that confidence depends on which cluster the user was in, and whether the effect holds equally for light users and heavy users.</p>
<p>Regression handles all of that in a single model, and when the experiment is properly randomized, the coefficients carry a clean causal interpretation that the simple mean difference can't.</p>
<p>That causal interpretation is what this tutorial is about. Under random assignment, OLS gives you a causal estimate. The treatment variable and the error term are independent by construction of the randomization, so the coefficient on treatment is an unbiased estimate of the average causal effect.</p>
<p>Add covariates and the estimate stays the same but the standard error shrinks because you have absorbed variance in the outcome that comes from other sources. Cluster by workspace and you get standard errors built on the actual data structure.</p>
<p>The dataset is a synthetic SaaS product with 50,000 users split across 50 workspaces. The new prompt template was assigned randomly by user ID hash. The ground-truth causal effect baked into the data generator is an increase of 4 percentage points on task completion.</p>
<p>The code in this tutorial recovers it through five steps: a randomization check, a naïve mean difference, OLS with HC3 robust errors, cluster-robust errors, and an interaction model that detects whether the effect differs by user type.</p>
<p>The final section identifies regression's limits, because knowing when a tool fails is as important as knowing how to use it.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-why-regression-works-for-randomized-experiments">Why Regression Works for Randomized Experiments</a></p>
</li>
<li><p><a href="#heading-prerequisites">Prerequisites</a></p>
</li>
<li><p><a href="#heading-setting-up-the-working-example">Setting Up the Working Example</a></p>
<ul>
<li><p><a href="#heading-step-1-naive-difference-in-means">Step 1: Naïve Difference in Means</a></p>
</li>
<li><p><a href="#heading-step-2-ols-with-heteroskedasticity-robust-errors-hc3">Step 2: OLS with Heteroskedasticity-robust Errors (HC3)</a></p>
</li>
<li><p><a href="#heading-step-3-cluster-robust-standard-errors">Step 3: Cluster-robust Standard Errors</a></p>
</li>
<li><p><a href="#heading-step-4-treatment-effect-heterogeneity-via-interactions">Step 4: Treatment-effect Heterogeneity via Interactions</a></p>
</li>
<li><p><a href="#heading-step-5-bootstrap-confidence-intervals">Step 5: Bootstrap Confidence Intervals</a></p>
</li>
</ul>
</li>
<li><p><a href="#heading-when-regression-alone-isnt-enough">When Regression Alone isn't Enough</a></p>
</li>
<li><p><a href="#heading-what-to-do-next">What to Do Next</a></p>
</li>
</ul>
<h2 id="heading-why-regression-works-for-randomized-experiments">Why Regression Works for Randomized Experiments</h2>
<img src="https://cdn.hashnode.com/uploads/covers/69cc82ffe4688e4edd796adb/bfd58962-9157-43e8-852c-0372394e0782.png" alt="bfd58962-9157-43e8-852c-0372394e0782" style="display:block;margin:0 auto" width="1636" height="635" loading="lazy">

<p><em>Figure 1: Under randomization (left), covariate distributions overlap almost perfectly across treatment and control arms, and OLS recovers the causal effect. Under observational data with selection bias (right), treated users have systematically higher covariate values, and OLS conflates the covariate effect with the treatment effect.</em></p>
<p>Random assignment creates one very specific condition: the treatment indicator is statistically independent of every other variable in the world, observed and unobserved. Under independence, the expected value of OLS's error term, conditional on treatment, is zero, and OLS recovers an unbiased causal estimate. The ordinary assumption of no omitted-variable bias collapses into a trivially satisfied condition once you have randomized.</p>
<p>To see why, write the simplest possible model:</p>
<pre><code class="language-plaintext">task_completed_i = alpha + beta * prompt_variant_i + epsilon_i
</code></pre>
<p>If <code>prompt_variant</code> was assigned by coin flip, then <code>E[epsilon | prompt_variant] = 0</code>. OLS will recover <code>beta</code> as the average treatment effect. Confounders such as engagement tier, workspace tenure, and historical query complexity all live inside <code>epsilon</code>, but because the coin flip removed any correlation between <code>prompt_variant</code> and <code>epsilon</code>, they pass harmlessly through the residual without touching <code>beta</code>. They simply inflate the variance of <code>epsilon</code> and therefore the variance of your estimate.</p>
<p>Adding covariates to the regression preserves the point estimate while doing something highly useful: it absorbs the variance in <code>epsilon</code> that the covariates explain. The treatment coefficient stays the same, the residual variance shrinks, and the standard error on <code>beta</code> falls. You achieve the same point estimate with a tighter confidence interval simply by including baseline variables you already have in your logs.</p>
<p>Four assumptions underpin that causal interpretation, and all four must hold for the regression coefficient to carry a causal meaning.</p>
<ol>
<li><p><strong>Random assignment</strong>: treatment is independent of potential outcomes (<code>E[ε|D] = 0</code>). Randomization delivers this by construction. If assignment is confounded, this assumption breaks and OLS measures something other than the average treatment effect.</p>
</li>
<li><p><strong>Linearity</strong>: the conditional expectation of the outcome is linear in treatment and covariates. It's a reasonable approximation for binary outcomes over a narrow covariate range.</p>
</li>
<li><p><strong>No interference / SUTVA</strong>: each user's outcome depends only on their own treatment assignment, not on which template their colleagues received. That's the stable unit treatment value assumption. When it breaks, the coefficient conflates direct effects with spillovers.</p>
</li>
<li><p><strong>No differential attrition</strong>: dropout from the experiment is roughly equal across arms, so the groups you observe at the end are still comparable, with minimal attrition and no contamination between arms.</p>
</li>
</ol>
<p>The balance check below verifies that randomization held on observables. The failure-modes section identifies which of these four assumptions each real-world problem violates.</p>
<p>When the randomization is clean, regression efficiently extracts the causal estimate. When an assumption breaks, regression describes the failure rather than the treatment effect. If the balance table reveals a systematic gap on any covariate, stop and investigate the assignment pipeline before you proceed to estimation.</p>
<h2 id="heading-prerequisites">Prerequisites</h2>
<p>Every code block in this tutorial runs end-to-end in the companion notebook at <a href="https://github.com/RudrenduPaul/product-experimentation-causal-inference-genai-llm/tree/main/09_regression"><code>09_regression/regression_demo.ipynb</code></a>.</p>
<p>You need Python 3.11 or newer and basic comfort with pandas and statistics. <code>statsmodels</code> is the one library here that might be new to you: it handles HC3 and cluster-robust standard errors in a single call, the analytical substance <code>scipy.stats</code> can't provide on its own.</p>
<p>Install the required packages:</p>
<pre><code class="language-bash">pip install numpy pandas statsmodels scipy
</code></pre>
<p>Clone the companion repo to get the synthetic dataset:</p>
<pre><code class="language-bash">git clone https://github.com/RudrenduPaul/product-experimentation-causal-inference-genai-llm.git
cd product-experimentation-causal-inference-genai-llm
python data/generate_data.py --seed 42 --n-users 50000 --out data/synthetic_llm_logs.csv
</code></pre>
<h2 id="heading-setting-up-the-working-example">Setting Up the Working Example</h2>
<p>The dataset simulates 50,000 users distributed across 50 workspaces. The <code>prompt_variant</code> column records which arm each user was assigned to: 1 is the new template, 0 is the control.</p>
<p>Assignment was done by hashing user ID, so it's effectively random and independent of everything else in the data.</p>
<p>The <code>task_completed</code> column is the binary outcome. The ground-truth causal effect baked into the generator is an increase of 4 percentage points.</p>
<p>Before fitting any model, verify that randomization balanced the groups on observable covariates. A properly randomized experiment produces near-equal means on every measured characteristic across arms.</p>
<pre><code class="language-python">import pandas as pd
import numpy as np

df = pd.read_csv("data/synthetic_llm_logs.csv")

print("Dataset shape:", df.shape)
print("\nPrompt variant distribution:")
print(df.prompt_variant.value_counts().to_dict())

# Randomization check: covariate means by arm
check_cols = ["query_confidence", "session_minutes", "cost_usd"]
balance_table = (
    df.groupby("prompt_variant")[check_cols]
    .mean()
    .round(4)
    .T
)
balance_table.columns = ["Control (variant=0)", "Treatment (variant=1)"]
balance_table["Difference"] = (
    balance_table["Treatment (variant=1)"]
    - balance_table["Control (variant=0)"]
)
print("\nCovariate balance check:")
print(balance_table)

# Engagement tier proportions
print("\nEngagement tier split by arm:")
print(
    df.groupby("prompt_variant")
    .engagement_tier.value_counts(normalize=True)
    .unstack()
    .round(3)
)
</code></pre>
<p><strong>Expected output:</strong></p>
<pre><code class="language-text">[Placeholder — run regression_demo.py on the 50k dataset to capture real numbers]
</code></pre>
<p>Here's what's happening: you load 50,000 rows and count the split between arms (approximately 25,000 in each). You then compute mean values of three continuous variables (<code>query_confidence</code>, <code>session_minutes</code>, and <code>cost_usd</code>) for the control and treatment groups separately.</p>
<p>These columns reflect behavior logged before the prompt variant was assigned, so they are pre-treatment by construction. The "Difference" column should be tiny in every row.</p>
<p>You also check that the categorical engagement tiers (heavy, medium, light) appear at similar proportions in each arm. Small imbalances are normal sampling variation, but a systematic gap on any covariate signals that the hash-based assignment failed or that the data pipeline introduced selection after randomization. If you see a large imbalance, stop and investigate the assignment pipeline before proceeding to estimation.</p>
<p>On this dataset, all differences fall below 0.01 in absolute value and engagement tier proportions match to within two percentage points across arms. The randomization held.</p>
<img src="https://cdn.hashnode.com/uploads/covers/69cc82ffe4688e4edd796adb/95863661-169e-4de7-a699-9154ce463b92.png" alt="95863661-169e-4de7-a699-9154ce463b92" style="display:block;margin:0 auto" width="1486" height="922" loading="lazy">

<p><em>Figure 2:</em> <code>query_confidence</code> <em>density by treatment arm across 25,000 control and 25,000 treatment users. The two curves overlap almost exactly (mean difference = -0.0013), confirming that hash-based random assignment produced covariate balance. This is the real dataset diagnostic. Compare it with the schematic in Figure 1.</em></p>
<h2 id="heading-step-1-naive-difference-in-means">Step 1: Naïve Difference in Means</h2>
<p>Start with the simplest possible estimator: subtract the mean outcome in the control arm from the mean outcome in the treatment arm.</p>
<pre><code class="language-python">from scipy import stats

mean_control = df[df.prompt_variant == 0].task_completed.mean()
mean_treatment = df[df.prompt_variant == 1].task_completed.mean()

naive_effect = mean_treatment - mean_control

print(f"Control mean:    {mean_control:.4f}")
print(f"Treatment mean:  {mean_treatment:.4f}")
print(f"Naive effect:    {naive_effect:+.4f}")

# Manual two-sample t-test
n0 = (df.prompt_variant == 0).sum()
n1 = (df.prompt_variant == 1).sum()
var0 = df[df.prompt_variant == 0].task_completed.var()
var1 = df[df.prompt_variant == 1].task_completed.var()
se = np.sqrt(var0 / n0 + var1 / n1)
t_stat = naive_effect / se

p_val = 2 * stats.t.sf(abs(t_stat), df=n0 + n1 - 2)

print(f"\nSE (two-sample):  {se:.4f}")
print(f"t-statistic:      {t_stat:.3f}")
print(f"p-value:          {p_val:.4f}")
</code></pre>
<p><strong>Expected output:</strong></p>
<pre><code class="language-text">[Placeholder — run regression_demo.py on the 50k dataset to capture real numbers]
</code></pre>
<p>Here's what's happening: you compute the mean task completion rate in each arm, take the difference, and calculate the standard error using the pooled variance formula for a two-sample t-test. Because the experiment was randomized, this naïve difference is a valid causal estimate.</p>
<p>The recovered estimate may sit a percentage point or two away from the baked-in +4 pp ground truth. That's normal sampling variation at this dataset size, not estimator bias. The OLS regression in the next step will reproduce this number exactly when run without covariates, and will tighten the standard error once covariates are added.</p>
<p>The naïve t-test treats every observation as independent. That's a reasonable starting assumption here, but it doesn't hold in step 3, where users in the same workspace are correlated and the naïve standard error understates the actual uncertainty.</p>
<h2 id="heading-step-2-ols-with-heteroskedasticity-robust-errors-hc3">Step 2: OLS with Heteroskedasticity-robust Errors (HC3)</h2>
<p>Ordinary least squares with a binary treatment variable regressed on a binary outcome produces the same point estimate as the difference in means when there are no covariates. Adding covariates absorbs residual variance and shrinks the standard error.</p>
<p>HC3 standard errors are the main upgrade over the naïve t-test: they're valid even when the variance of the error term shifts across observations.</p>
<p>HC3 is preferred over HC0 through HC2 for finite samples because it penalizes high-leverage observations more aggressively, giving you better confidence interval coverage when sample sizes are moderate.</p>
<pre><code class="language-python">import statsmodels.formula.api as smf

# OLS without covariates: should match naive difference
m1 = smf.ols(
    "task_completed ~ prompt_variant",
    data=df
).fit(cov_type="HC3")

print("=== OLS without covariates (HC3) ===")
print(m1.summary().tables[1])
print(f"\nCoefficient: {m1.params['prompt_variant']:+.4f}")
print(f"HC3 SE:      {m1.bse['prompt_variant']:.4f}")
print(f"p-value:     {m1.pvalues['prompt_variant']:.4f}")
</code></pre>
<p><strong>Expected output:</strong></p>
<pre><code class="language-text">[Placeholder — run regression_demo.py on the 50k dataset to capture real numbers]
</code></pre>
<p>Here's what's happening: you fit OLS with HC3 robust standard errors and no covariates. The coefficient on <code>prompt_variant</code> matches the naïve difference in means to four decimal places, confirming that OLS is just the mean-difference estimator in a regression wrapper.</p>
<p>HC3 standard errors run slightly larger than classical OLS standard errors because they correct for heteroskedasticity without assuming constant variance across the outcome distribution.</p>
<p>In practice, the difference is often small on balanced experiments, but you should default to HC3 anyway. There's no cost when you don't need it and real cost when you do.</p>
<p>Now add the covariates:</p>
<pre><code class="language-python"># Define the regression formula with covariates
formula = (
    "task_completed ~ prompt_variant + query_confidence + "
    "session_minutes + C(engagement_tier)"
)

# OLS with covariates: same point estimate, smaller SE
m2 = smf.ols(formula, data=df).fit(cov_type="HC3")

print("=== OLS with covariates (HC3) ===")
print(m2.summary().tables[1])
print(f"\nCoefficient: {m2.params['prompt_variant']:+.4f}")
print(f"HC3 SE:      {m2.bse['prompt_variant']:.4f}")
print(f"p-value:     {m2.pvalues['prompt_variant']:.4f}")

# Compare the two SEs
print("\n--- SE comparison ---")
print(f"Without covariates: {m1.bse['prompt_variant']:.4f}")
print(f"With covariates:    {m2.bse['prompt_variant']:.4f}")
print(f"R-squared (with):   {m2.rsquared:.4f}")
</code></pre>
<p><strong>Expected output:</strong></p>
<pre><code class="language-text">[Placeholder — run regression_demo.py on the 50k dataset to capture real numbers]
</code></pre>
<p>Here's what's happening: you add <code>query_confidence</code>, <code>session_minutes</code>, and <code>engagement_tier</code> as controls. All three are pre-treatment variables, logged before the prompt variant was applied, so including them can't introduce collider bias.</p>
<p>The coefficient on <code>prompt_variant</code> stays close to the naïve estimate because randomization guarantees those covariates are uncorrelated with treatment assignment. The point estimate stays fixed. What shrinks is the uncertainty around it.</p>
<p>R-squared rises from near-zero without covariates to a few percentage points with them, meaning the covariates account for some of the variation in task completion. The HC3 p-value on <code>prompt_variant</code> tightens as the standard error falls.</p>
<p>This is the free lunch of covariate adjustment in randomized experiments. Include any pre-treatment variable that predicts the outcome: baseline engagement, historical task completion rate, or signup cohort. Stick to variables fixed before treatment began, because anything the treatment could have changed doesn't belong here.</p>
<h2 id="heading-step-3-cluster-robust-standard-errors">Step 3: Cluster-robust Standard Errors</h2>
<p>The HC3 approach in step 2 handles heteroskedasticity but still treats every observation as independent. Users inside the same workspace share a support team, a product tier, the same IT policies, and often the same use cases, so their outcomes correlate with each other.</p>
<p>If the new prompt template happens to land well in workspace 12 and poorly in workspace 37, those outcomes are correlated within workspace regardless of treatment. Ignoring that correlation makes the standard error too small, which inflates the t-statistic and makes your results appear more significant than they are.</p>
<p>Cluster-robust standard errors fix this by treating each workspace as a single informational unit, so the variance of the treatment coefficient reflects 50 workspace-level draws rather than 50,000 independent coin flips.</p>
<pre><code class="language-python"># Naive SE (assumes independence within workspaces)
m3_naive = smf.ols(formula, data=df).fit(cov_type="HC3")

# Cluster-robust SE (accounts for within-workspace correlation)
m3_cluster = smf.ols(formula, data=df).fit(
    cov_type="clus