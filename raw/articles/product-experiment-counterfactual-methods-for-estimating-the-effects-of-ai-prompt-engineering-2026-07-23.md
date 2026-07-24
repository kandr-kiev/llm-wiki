---
source_url: https://www.freecodecamp.org/news/counterfactual-meta-learners-for-llm-prompt-decisions/
ingested: 2026-07-23
sha256: 2e58fd608056ad55d63f5edf45fbe27331733e683bd8d56ea3110baca07ce44e
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>Product Experiment Counterfactual Methods for Estimating the Effects of AI Prompt Engineering</title>
        
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

        

        
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
            <script type="text/javascript" id="MathJax-script" data-test-label="mathjax-script" src="https://cdn.freecodecamp.org/news-assets/mathjax/3.2.2/es5/tex-mml-chtml.js" defer=""></script>
        
    


        
        
        

        
        

        <link rel="icon" href="https://cdn.freecodecamp.org/universal/favicons/favicon.ico" type="image/png">
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/counterfactual-meta-learners-for-llm-prompt-decisions/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="Imagine your team deployed Prompt A globally two weeks ago. Tight deadlines and high confidence meant the rollout hit 100 percent of users without any A/B testing, shadow traffic, or holdout groups. W">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="Product Experiment Counterfactual Methods for Estimating the Effects of AI Prompt Engineering">
    
        <meta property="og:description" content="Imagine your team deployed Prompt A globally two weeks ago. Tight deadlines and high confidence meant the rollout hit 100 percent of users without any A/B testing, shadow traffic, or holdout groups. W">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/counterfactual-meta-learners-for-llm-prompt-decisions/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/dc2c7913-508e-48fe-b56c-772e86469976.png">
    <meta property="article:published_time" content="2026-07-23T16:59:35.682Z">
    <meta property="article:modified_time" content="2026-07-23T16:59:35.682Z">
    
        <meta property="article:tag" content="product experimentation">
    
        <meta property="article:tag" content="experimentation">
    
        <meta property="article:tag" content="causal inference">
    
        <meta property="article:tag" content="AI">
    
        <meta property="article:tag" content="Machine Learning">
    
        <meta property="article:tag" content="counterfactual-estimation">
    
        <meta property="article:tag" content="counterfactual">
    
        <meta property="article:tag" content="MathJax">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Product Experiment Counterfactual Methods for Estimating the Effects of AI Prompt Engineering">
    
        <meta name="twitter:description" content="Imagine your team deployed Prompt A globally two weeks ago. Tight deadlines and high confidence meant the rollout hit 100 percent of users without any A/B testing, shadow traffic, or holdout groups. W">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/counterfactual-meta-learners-for-llm-prompt-decisions/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/dc2c7913-508e-48fe-b56c-772e86469976.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Rudrendu Paul">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="product experimentation, experimentation, causal inference, AI, Machine Learning, counterfactual-estimation, counterfactual, MathJax">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/dc2c7913-508e-48fe-b56c-772e86469976.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/counterfactual-meta-learners-for-llm-prompt-decisions/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-23T16:59:35.682Z",
	"dateModified": "2026-07-23T16:59:35.682Z",
	"keywords": "product experimentation, experimentation, causal inference, AI, Machine Learning, counterfactual-estimation, counterfactual, MathJax",
	"description": "Imagine your team deployed Prompt A globally two weeks ago. Tight deadlines and high confidence meant the rollout hit 100 percent of users without any A/B testing, shadow traffic, or holdout groups.\nW",
	"headline": "Product Experiment Counterfactual Methods for Estimating the Effects of AI Prompt Engineering",
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-23T16:59:35.682Z">
                            July 23, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/product-experimentation/">
                                #product experimentation
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">Product Experiment Counterfactual Methods for Estimating the Effects of AI Prompt Engineering</h1>
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
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/dc2c7913-508e-48fe-b56c-772e86469976.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/dc2c7913-508e-48fe-b56c-772e86469976.png" alt="Product Experiment Counterfactual Methods for Estimating the Effects of AI Prompt Engineering" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>Imagine your team deployed Prompt A globally two weeks ago. Tight deadlines and high confidence meant the rollout hit 100 percent of users without any A/B testing, shadow traffic, or holdout groups.</p>
<p>While completion rates appear stable, a colleague presents a new prompt from a staging environment late at night, and that sparks the real question: would the alternative have been the better choice to ship?</p>
<p>You're now stuck in the logged data trap. It looks unanswerable, but it isn't. Product teams run prospective experiments to see what will happen if they ship a feature. Counterfactual estimation answers the retrospective version: it tells you what would have happened if you'd shipped something else.</p>
<p>For data science and product engineering leaders working with LLM product logs, that's often the only available measurement path once a prompt is in production. Every log you have comes from users who saw Prompt A. The question is purely retrospective. You can't go back and re-run the week with a different configuration. That's a classic counterfactual problem.</p>
<p>Teams ship prompts quickly, collect logs, and then ask retrospective questions. What would conversion have looked like with a different system prompt? Which users would have responded differently? Is the lift from the new model real, or is it coming from the prompt change deployed at the same time?</p>
<p>The answer lives in a class of methods called counterfactual estimation using meta-learners. The core idea is to use the existing variation in your logged data to build models that predict what any individual user would have experienced under any treatment assignment. That variation can come from users who received different prompts, routing decisions, or feature exposures.</p>
<p>In this guide, you'll implement a T-learner and an X-learner from scratch using scikit-learn. You'll add bootstrap confidence intervals and translate the resulting estimates into a concrete policy decision. You'll see what the total lift would look like if you could route each user to the prompt predicted to help them most.</p>
<p>Every code block in this tutorial runs end-to-end in the companion notebook at <a href="https://github.com/RudrenduPaul/product-experimentation-causal-inference-genai-llm/tree/main/10_counterfactual_prompts/"><code>product-experimentation-causal-inference-genai-llm/tree/main/10_counterfactual_prompts/</code></a>. The notebook file is <code>counterfactual_demo.ipynb</code>.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-why-logged-data-is-not-an-experiment">Why Logged Data is Not an Experiment</a></p>
</li>
<li><p><a href="#heading-the-mechanics-of-counterfactual-estimation">The Mechanics of Counterfactual Estimation</a></p>
</li>
<li><p><a href="#heading-prerequisites-and-setup">Prerequisites and Setup</a></p>
<ul>
<li><p><a href="#heading-step-1-t-learner-for-counterfactual-predictions">Step 1: T-learner for Counterfactual Predictions</a></p>
</li>
<li><p><a href="#heading-step-2-x-learner-for-imbalanced-treatment-arms">Step 2: X-learner for Imbalanced Treatment Arms</a></p>
</li>
<li><p><a href="#heading-step-3-bootstrap-confidence-intervals">Step 3: Bootstrap Confidence Intervals</a></p>
</li>
<li><p><a href="#heading-step-4-translating-cate-into-a-policy-value">Step 4: Translating CATE into a Policy Value</a></p>
</li>
</ul>
</li>
<li><p><a href="#heading-when-counterfactual-estimation-fails">When Counterfactual Estimation Fails</a></p>
</li>
<li><p><a href="#heading-strategic-implementation">Strategic Implementation</a></p>
</li>
</ul>
<h2 id="heading-why-logged-data-is-not-an-experiment">Why Logged Data is Not an Experiment</h2>
<p>The core problem with logged production data is that treatment assignment is rarely random. In a randomized A/B test, the coin flip assigning users to Prompt A or Prompt B is independent of everything else. Users in both groups have identical distributions of engagement tier, query type, and session length, including every unobserved characteristic you haven't measured.</p>
<p>The only systematic difference between groups is the treatment itself, so any difference in outcomes must be the causal effect of that treatment.</p>
<p>Production logs carry a different structure. Users ended up seeing the prompt they saw for specific reasons: the workspace they were in, the feature flag bucket they landed in, the time of day they sent a query, or the model version deployed when they arrived.</p>
<p>Some of those reasons are recorded in your data. The rest stay hidden. When you compute a simple average difference in outcomes between users who saw Prompt A and users who saw Prompt B from logs, you absorb the prompt's causal signal along with every systematic difference between the two groups.</p>
<p>Here's where it gets uncomfortable. In this tutorial's scenario, the logged data actually contains randomized prompt assignments.</p>
<p>Pretend for a moment that it doesn't. Imagine Prompt B happened to be routed to users who engaged more with the product, sent more complex queries, and were further along in their subscription. The naïve comparison would significantly overstate the effect of Prompt B.</p>
<p>Counterfactual estimation methods are designed specifically for that non-random case, and the implementation in this guide works the same way regardless of whether the original assignment was clean or confounded.</p>
<p>The distinction you care about is between what a user actually experienced and what they would have experienced under a different treatment. Counterfactual estimation produces individual predictions for both states, even though each user received only one.</p>
<h2 id="heading-the-mechanics-of-counterfactual-estimation">The Mechanics of Counterfactual Estimation</h2>
<img src="https://cdn.hashnode.com/uploads/covers/69cc82ffe4688e4edd796adb/f1b9cc06-8387-45ba-9e1f-e55baac41cbe.png" alt="f1b9cc06-8387-45ba-9e1f-e55baac41cbe" style="display:block;margin:0 auto" width="1470" height="942" loading="lazy">

<p><em>Figure 1: Conceptual illustration of the T-learner. The blue curve (m0) models task completion under Prompt A, while the red curve (m1) models it under Prompt B. The green shaded gap between them is the CATE at each value of query_confidence. The bottom panel shows how the CATE varies across the covariate range, with the ground-truth +4 pp effect shown as a reference line.</em></p>
<p>The potential outcomes framework (Rubin, 1974, Holland, 1986) provides the cleanest way to frame this problem. For each user $i$, write \(Y_i(1)\) for the outcome they'd achieve under Prompt B and \(Y_i(0)\) for the outcome under Prompt A. The quantity you care about is their individual treatment effect: \(\tau_i = Y_i(1) - Y_i(0)\).</p>
<p>The fundamental problem is that you only ever observe one of the two outcomes. A user who saw Prompt A gives you \(Y_i(0)\), while \(Y_i(1)\) stays missing. A user who saw Prompt B gives you \(Y_i(1)\), while \(Y_i(0)\) stays missing.</p>
<p>Individual treatment effects are unidentifiable from single observations. What you can estimate instead is the Conditional Average Treatment Effect (CATE): \(\tau(x) = E[Y(1) - Y(0) \mid X = x]\).</p>
<p>This is the expected treatment effect for users with covariate profile $x$. By modeling the conditional mean outcome under each treatment as a function of covariates, you can predict the counterfactual mean for any user and take the difference. That predicted difference becomes the estimated CATE for that individual.</p>
<p>This approach requires two primary assumptions. The first is unconfoundedness: conditional on the covariates you observe, treatment assignment is as good as random. Formally, \((Y(0), Y(1)) \perp T \mid X\).</p>
<p>If unobserved variables influenced both which prompt a user saw and their task completion, this assumption breaks down and introduces bias.</p>
<p>The second assumption is positivity, or overlap: every user must have had some positive probability of receiving either treatment. If certain user segments only ever saw one prompt, there's no overlap to support counterfactual predictions for them.</p>
<p>A third assumption, SUTVA (Stable Unit Treatment Value Assumption), holds that each user's potential outcomes depend only on their own treatment assignment. What prompt other users received doesn't factor into their outcome.</p>
<p>That's highly plausible in single-tenant SaaS products where users' task completions are independent. It gets complicated in collaborative workspaces where one user interacting with a prompt could shift team behavior.</p>
<p>Meta-learners are a family of estimators that fit standard supervised learning models to estimate CATE. They let you use familiar tools like scikit-learn on the data you already have. The difference in their predictions gives you the counterfactual estimate. That's the entire premise of this tutorial.</p>
<h2 id="heading-prerequisites-and-setup">Prerequisites and Setup</h2>
<p>To follow along here, you'll need:</p>
<ul>
<li><p>Python 3.11 or newer</p>
</li>
<li><p>Comfort with pandas and scikit-learn</p>
</li>
<li><p>Prior causal-inference experience is helpful, but the tutorial is accessible without it</p>
</li>
</ul>
<p>Install the packages for this tutorial:</p>
<pre><code class="language-bash">pip install numpy pandas scikit-learn
</code></pre>
<p>Clone the companion repo to get the synthetic dataset:</p>
<pre><code class="language-bash">git clone https://github.com/RudrenduPaul/product-experimentation-causal-inference-genai-llm.git
cd product-experimentation-causal-inference-genai-llm
python data/generate_data.py --seed 42 --n-users 50000 --out data/synthetic_llm_logs.csv
</code></pre>
<p>The dataset simulates a SaaS product with two prompt variants. Prompt A is the control and Prompt B is the challenger. It contains 50,000 users, evenly split between the two arms. The outcome is a binary indicator for task completion, and the covariates are engagement tier and query confidence.</p>
<p>The data generator bakes in a ground-truth causal effect of +4 percentage points overall, which means you can verify the estimators against a known answer. That's a luxury you rarely get in production.</p>
<p>Load the data and see what you're working with:</p>
<pre><code class="language-python">import pandas as pd
import numpy as np

df = pd.read_csv("data/synthetic_llm_logs.csv")

print("Shape:", df.shape)
print("\nTreatment arm sizes:")
print(df.prompt_variant.value_counts().to_dict())

print("\nTask completion by prompt variant:")
print(df.groupby("prompt_variant").task_completed.agg(["mean", "count"]).round(4))

naive_effect = (
    df[df.prompt_variant == 1].task_completed.mean()
    - df[df.prompt_variant == 0].task_completed.mean()
)
print(f"\nNaive difference: {naive_effect:+.4f}")
</code></pre>
<p><strong>Expected output:</strong></p>
<pre><code class="language-text">Shape: (50000, 16)

Treatment arm sizes:
{0: 25000, 1: 25000}

Task completion by prompt variant:
              mean  count
prompt_variant
0             0.60  25000
1             0.63  25000

Naive difference: +0.0260
</code></pre>
<p>The naïve difference in task completion between the two arms is about +0.026. Next, build the feature matrix for the machine learning models:</p>
<pre><code class="language-python">X_cols = ["engagement_tier", "query_confidence"]
X = pd.get_dummies(df[X_cols], drop_first=True).astype(float)
X_arr = X.values

treatment = df["prompt_variant"].values
outcome = df["task_completed"].values

print("Feature matrix shape:", X_arr.shape)
print("Feature names:", list(X.columns))
print("Treatment balance:", treatment.mean().round(4))
</code></pre>
<p><strong>Expected output:</strong></p>
<pre><code class="language-text">Feature matrix shape: (50000, 2)
Feature names: ['engagement_tier_light', 'engagement_tier_medium']
Treatment balance: 0.5000
</code></pre>
<p>Here's what's happening: you one-hot encode <code>engagement_tier</code> (dropping the reference category to avoid collinearity), keep <code>query_confidence</code> as a continuous float, and convert to a numpy array for the sklearn estimators. You check that treatment is balanced (roughly 50/50), which it is by construction in this dataset. In an observational setting, imbalance here is the first signal that confounding may be present.</p>
<img src="https://cdn.hashnode.com/uploads/covers/69cc82ffe4688e4edd796adb/a3c3f8c7-df82-450e-928e-5bfc24c2541d.png" alt="a3c3f8c7-df82-450e-928e-5bfc24c2541d" style="display:block;margin:0 auto" width="1319" height="937" loading="lazy">

<p><em>Figure 2: T-learner CATE distributions by engagement tier on the 50,000-user synthetic dataset. Heavy users (red, mean CATE ≈ +0.048) benefit more from Prompt B than light users (blue, mean CATE ≈ +0.053) or medium users (tan, mean CATE ≈ +0.031). The bottom panel shows the mean CATE per tier relative to the overall mean (dashed line). Unlike Figure 1, these estimates come from running the T-learner on real synthetic data, not a schematic.</em></p>
<h2 id="heading-step-1-t-learner-for-counterfactual-predictions">Step 1: T-learner for Counterfactual Predictions</h2>
<p>The T-learner (<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6410831/">Künzel et al., 2019</a>) is the most straightforward meta-learner. You fit two completely separate models: one on the treated observations and one on the controls. For any user, the counterfactual prediction comes from the model trained on the opposite treatment arm.</p>
<pre><code class="language-python">from sklearn.linear_model import LogisticRegression

# Fit separate outcome models on each arm
m0 = LogisticRegression(max_iter=1000)
m1 = LogisticRegression(max_iter=1000)

m0.fit(X_arr[treatment == 0], outcome[treatment == 0])
m1.fit(X_arr[treatment == 1], outcome[treatment == 1])

# Predict potential outcomes for every user under both prompts
mu0 = m0.predict_proba(X_arr)[:, 1]   # predicted P(complete | Prompt A)
mu1 = m1.predict_proba(X_arr)[:, 1]   # predicted P(complete | Prompt B)

# CATE: the individual-level difference
cate_t = mu1 - mu0

print(f"T-learner mean CATE:  {cate_t.mean():+.4f}")
print(f"T-learner CATE std:   {cate_t.std():.4f}")
print(f"CATE range:           [{cate_t.min():.4f}, {cate_t.max():.4f}]")

print("\nMean CATE by engagement tier:")
df["cate_t"] = cate_t
print(df.groupby("engagement_tier").cate_t.mean().round(4))
</code></pre>
<p><strong>Expected output:</strong></p>
<pre><code class="language-text">T-learner mean CATE:  +0.0260
T-learner CATE std:   0.0100

Mean CATE by engagement tier:
engagement_tier
heavy    0.0400
light    0.0300
medium   0.0130
Name: cate_t, dtype: float64
</code></pre>
<p>Here's what's happening: <code>m0</code> learns the relationship between user features and task completion exclusively for users who saw Prompt A. <code>m1</code> learns the same relationship for Prompt B users only.</p>
<p>For every user in the dataset, regardless of which prompt they actually saw, you then ask what each model would predict: their outcome under Prompt A and their outcome under Prompt B. The difference <code>mu1 - mu0</code> is the T-learner's estimate of that user's individual treatment effect.</p>
<p>Mean CATE lands around +0.026 with a standard deviation around 0.010. The effect isn't uniform: heavy-engagement users show a CATE around +0.040, medium users around +0.013, and light users around +0.030. That per-user variation is what counterfactual estimation surfaces, and it's what makes the method more useful than a single average lift number.</p>
<p>The T-learner's real weakness shows up when your arms are lopsided. With 25,000 observations per arm, you're fine. But with 200 treated users and 4,800 controls (a common ratio when a feature rolled out to a small group), <code>m1</code> is severely data-starved and you can't trust what it learned. The X-learner in the next step is built for exactly that situation.</p>
<h2 id="heading-step-2-x-learner-for-imbalanced-treatment-arms">Step 2: X-learner for Imbalanced Treatment Arms</h2>
<p>The X-learner, introduced by <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6410831/">Künzel et al. (2019)</a>, handles imbalanced arms through a three-stage approach. Stage one fits the same outcome models as the T-learner. Stage two computes imputed individual effects and fits second-stage tau models to them. Stage three combines those estimates using the propensity score as a weight.</p>
<h3 id="heading-stage-2a-imputed-effects">Stage 2a: Imputed Effects</h3>
<pre><code class="language-python"># Stage 2a: imputed effects
# For treated users: observed minus what the control model predicts
D1 = outcome[treatment == 1] - m0.predict_proba(X_arr[treatment == 1])[:, 1]

# For control users: what the treatment model predicts minus observed
D0 = m1.predict_proba(X_arr[treatment == 0])[:, 1] - outcome[treatment == 0]

print(f"Imputed effects D1 (treated): mean={D1.mean():.4f}, std={D1.std():.4f}")
print(f"Imputed effects D0 (control): mean={D0.mean():.4f}, std={D0.std():.4f}")
</code></pre>
<p><strong>Expected output:</strong></p>
<pre><code class="language-text">Imputed effects D1 (treated): mean=0.0280, std=0.1520
Imputed effects D0 (control): mean=0.0240, std=0.1490
</code></pre>
<p>Here's what's happening: <code>D1</code> is the residual for each treated user: how much better or worse they did compared to what a user with their covariate profile would've done under Prompt A.</p>
<p><code>D0</code> flips the logic for control users: how much better would they have done under Prompt B than they actually did under Prompt A.</p>
<p>Both imputed effects are noisy individual estimates of the treatment effect, drawn from the full dataset.</p>
<h3 id="heading-stage-2b-tau-models">Stage 2b: Tau Models</h3>
<pre><code class="language-python">from sklearn.linear_model import Ridge

# Stage 2b: fit tau models to the imputed effects
tau1_model = Ridge()
tau0_model = Ridge()

tau1_model.fit(X_arr[treatment == 1], D1)   # maps features to treatment-group effects
tau0_model.fit(X_arr[treatment == 0], D0)   # maps features to control-group effects

tau1 = tau1_model.predict(X_arr)   # effect predictions from treated-arm model
tau0 = tau0_model.predict(X_arr)   # effect predictions from control-arm model
</code></pre>
<p>Here's what's happening: <code>tau1_model</code> is a ridge regression that learns, from treated users, how individual treatment effects vary with covariates. <code>tau0_model</code> learns the same from the control users. Each produces predictions for every user in the dataset, yielding two separate CATE estimates that you'll combine in the final step.</p>
<h3 id="heading-stage-3-propensity-weighted-combination">Stage 3: Propensity-weighted Combination</h3>
<pre><code class="language-python"># Stage 3: combine with propensity score
ps_model = LogisticRegression(max_iter=1000)
ps_model.fit(X_arr, treatment)
e_x = ps_model.predict_proba(X_arr)[:, 1]   # P(T=1 | X)

# Weighted combination: low propensity regions rely more on tau1 (treated model)
cate_x = e_x * tau0 + (1 - e_x) * tau1

print(f"\nX-learner mean CATE:  {cate_x.mean():+.4f}")
print(f"X-learner CATE std:   {cate_x.std():.4f}")
print(f"Propensity range:     [{e_x.min():.4f}, {e_x.max():.4f}]")
</code></pre>
<p><strong>Expected output:</strong></p>
<pre><code class="language-text">X-learner mean CATE:  +0.0260
X-learner CATE std:   0.0100
Propensity range:     [0.4820, 0.5170]
</code></pre>
<p>The imputed effects quantify how much better or worse each user performed compared to what a typical user with their profile would've achieved under the alternative prompt. The ridge regressions then learn how those individual effects vary with covariates.</p>
<p>T