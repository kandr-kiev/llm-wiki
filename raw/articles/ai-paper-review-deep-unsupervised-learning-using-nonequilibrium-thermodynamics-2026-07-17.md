---
source_url: https://www.freecodecamp.org/news/ai-paper-review-deep-unsupervised-learning-using-nonequilibrium-thermodynamics/
ingested: 2026-07-17
sha256: 8718732e1b8e6a2ac88bea7863464534c209be1f6116fc0e22be7b92d22f226d
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>AI Paper Review: Deep Unsupervised Learning using Nonequilibrium Thermodynamics</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/ai-paper-review-deep-unsupervised-learning-using-nonequilibrium-thermodynamics/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="Today, diffusion models power some of the most impressive AI systems ever built. They generate photorealistic images, create videos, synthesize speech, design proteins, and increasingly influence fiel">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="AI Paper Review: Deep Unsupervised Learning using Nonequilibrium Thermodynamics">
    
        <meta property="og:description" content="Today, diffusion models power some of the most impressive AI systems ever built. They generate photorealistic images, create videos, synthesize speech, design proteins, and increasingly influence fiel">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/ai-paper-review-deep-unsupervised-learning-using-nonequilibrium-thermodynamics/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/4588c233-fd5f-4a51-86e8-79784b629fb4.png">
    <meta property="article:published_time" content="2026-07-15T15:23:43.056Z">
    <meta property="article:modified_time" content="2026-07-15T15:23:43.056Z">
    
        <meta property="article:tag" content="AI">
    
        <meta property="article:tag" content="MathJax">
    
        <meta property="article:tag" content="Deep Learning">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="AI Paper Review: Deep Unsupervised Learning using Nonequilibrium Thermodynamics">
    
        <meta name="twitter:description" content="Today, diffusion models power some of the most impressive AI systems ever built. They generate photorealistic images, create videos, synthesize speech, design proteins, and increasingly influence fiel">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/ai-paper-review-deep-unsupervised-learning-using-nonequilibrium-thermodynamics/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/4588c233-fd5f-4a51-86e8-79784b629fb4.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Mohammed Fahd Abrah">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="AI, MathJax, Deep Learning">
    <meta name="twitter:site" content="@freecodecamp">
    
        <meta name="twitter:creator" content="@programmingoce">
    

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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/4588c233-fd5f-4a51-86e8-79784b629fb4.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/ai-paper-review-deep-unsupervised-learning-using-nonequilibrium-thermodynamics/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-15T15:23:43.056Z",
	"dateModified": "2026-07-15T15:23:43.056Z",
	"keywords": "AI, MathJax, Deep Learning",
	"description": "Today, diffusion models power some of the most impressive AI systems ever built. They generate photorealistic images, create videos, synthesize speech, design proteins, and increasingly influence fiel",
	"headline": "AI Paper Review: Deep Unsupervised Learning using Nonequilibrium Thermodynamics",
	"author": {
		"@type": "Person",
		"name": "Mohammed Fahd Abrah",
		"url": "https://www.freecodecamp.org/news/author/mohammed-fahd-abrah/",
		"sameAs": [
			"https://www.programming-ocean.com/Mohammed-Al-Abrah-Profile.php",
			"https://x.com/programmingoce"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/uploads/avatars/69ce92860ff860b6de01ed93/6c34e98f-25b2-4e72-8541-69f1ba3cd351.png",
			"width": 400,
			"height": 400
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-15T15:23:43.056Z">
                            July 15, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/ai/">
                                #AI
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">AI Paper Review: Deep Unsupervised Learning using Nonequilibrium Thermodynamics</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/uploads/avatars/69ce92860ff860b6de01ed93/6c34e98f-25b2-4e72-8541-69f1ba3cd351.png 60w" sizes="60px" src="https://cdn.hashnode.com/uploads/avatars/69ce92860ff860b6de01ed93/6c34e98f-25b2-4e72-8541-69f1ba3cd351.png" class="author-profile-image" alt="Mohammed Fahd Abrah" width="400" height="400" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/mohammed-fahd-abrah/" data-test-label="profile-link">
                    
                        Mohammed Fahd Abrah
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/4588c233-fd5f-4a51-86e8-79784b629fb4.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/4588c233-fd5f-4a51-86e8-79784b629fb4.png" alt="AI Paper Review: Deep Unsupervised Learning using Nonequilibrium Thermodynamics" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>Today, diffusion models power some of the most impressive AI systems ever built. They generate photorealistic images, create videos, synthesize speech, design proteins, and increasingly influence fields far beyond computer vision.</p>
<p>Models such as Stable Diffusion, DALL·E, and many modern generative systems all trace their roots back to a single question: How can a model learn an incredibly complex data distribution without becoming mathematically intractable?</p>
<p>For decades, this question remained one of the biggest obstacles in generative modeling. Researchers faced an uncomfortable trade-off. Models that were easy to train and evaluate were often too simple to capture the richness of real-world data. More expressive models could represent complex distributions, but they were notoriously difficult to optimize, sample from, or even evaluate. Countless methods attempted to narrow this gap, yet none fully escaped it.</p>
<p>In 2015, Jascha Sohl-Dickstein and his collaborators proposed a remarkably different way of thinking about the problem. Instead of trying to learn a complex data distribution directly, they asked a surprisingly simple question: What if we first destroyed the data by gradually adding noise, then learned how to reverse that process?</p>
<p>That single idea transformed a seemingly impossible learning problem into a sequence of small, manageable prediction tasks.</p>
<p>The infographic below provides an intuitive overview of the core idea behind diffusion models, showing how a concept borrowed from thermodynamics became the foundation of modern generative AI.</p>
<img src="https://cdn.hashnode.com/uploads/covers/69ce92860ff860b6de01ed93/c6e7fb57-7fff-4292-a9bb-3e04f33c15e0.png" alt="Infographic explaining the intuition behind diffusion models, showing how adding noise to data and learning the reverse denoising process—an idea inspired by thermodynamics—enables modern AI image generation." style="display:block;margin:0 auto" width="1774" height="887" loading="lazy">

<p>At the time, the paper attracted relatively little attention compared with other breakthroughs in deep learning. But looking back, it represents one of the most important turning points in the history of generative AI. It introduced the first practical formulation of <a href="https://en.wikipedia.org/wiki/Diffusion_model">diffusion probabilistic models (DPM)</a>, laying the mathematical foundation for the diffusion revolution that would reshape AI several years later.</p>
<p>In this review, we'll explore the paper step by step, from the motivation behind the idea, through the diffusion algorithm itself, to the experiments that demonstrated its potential. We'll see why this overlooked work ultimately became the starting point of one of the most influential families of generative models in modern AI.</p>
<h2 id="heading-paper-overview"><strong>Paper Overview</strong></h2>
<p><a href="https://arxiv.org/pdf/1503.03585">Deep Unsupervised Learning using Nonequilibrium Thermodynamics (2015)</a> introduced the first practical formulation of diffusion probabilistic models, establishing the foundation for the diffusion models that dominate generative AI today.</p>
<p>Rather than learning a complex data distribution directly, the paper proposes a two-stage process: a <a href="https://en.wikipedia.org/wiki/Diffusion_model">forward diffusion</a> process that gradually transforms data into simple noise, and a <a href="https://en.wikipedia.org/wiki/Reverse_diffusion">reverse diffusion</a> process that learns to reconstruct the original data from that noise.</p>
<p>Drawing inspiration from <a href="https://arxiv.org/pdf/2203.16048">nonequilibrium statistical physics</a>, the authors show that this formulation overcomes the long-standing trade-off between expressive generative models and computational tractability. The framework enables efficient training, exact sampling, likelihood evaluation, and posterior inference within a single probabilistic model.</p>
<p>To validate the approach, the paper demonstrates strong results on synthetic datasets, <a href="https://huggingface.co/datasets/ylecun/mnist">MNIST</a>, <a href="https://cave.cs.toronto.edu/kriz/cifar.html">CIFAR-10</a>, and natural image benchmarks, while also showcasing practical applications such as image denoising and inpainting.</p>
<p>Although initially overlooked, this pioneering work laid the mathematical groundwork for later breakthroughs such as <a href="https://arxiv.org/pdf/2006.11239">DDPMs</a> and <a href="https://arxiv.org/pdf/2011.13456">score-based diffusion models</a>, making it one of the most influential papers in the history of modern generative AI.</p>
<p>And here's a quick infographic of what we'll cover throughout this review, highlighting the paper's main ideas, methodology, key findings, and lasting impact.</p>
<img src="https://cdn.hashnode.com/uploads/covers/69ce92860ff860b6de01ed93/d9cbcaa0-d3c4-41aa-942c-e0c839129407.png" alt="Infographic summarizing the 2015 paper Deep Unsupervised Learning using Nonequilibrium Thermodynamics, covering its abstract, goals, methodology, key findings, conclusion, and limitations, and introducing the foundation of modern diffusion models." style="display:block;margin:0 auto" width="1024" height="1536" loading="lazy">

<h2 id="heading-table-of-contents"><strong>Table of Contents:</strong></h2>
<ul>
<li><p><a href="#heading-abstract">Abstract</a></p>
</li>
<li><p><a href="#heading-introduction">Introduction</a></p>
<ul>
<li><p><a href="#heading-11-diffusion-probabilistic-models">1.1 Diffusion Probabilistic Models</a></p>
</li>
<li><p><a href="#heading-12-relationship-to-other-work">1.2 Relationship to Other Work</a></p>
</li>
</ul>
</li>
<li><p><a href="#heading-2-algorithm">2. Algorithm</a></p>
<ul>
<li><p><a href="#heading-21-forward-trajectory">2.1 Forward Trajectory</a></p>
</li>
<li><p><a href="#heading-22-reverse-trajectory">2.2 Reverse Trajectory</a></p>
</li>
<li><p><a href="#heading-23-model-probability">2.3 Model Probability</a></p>
</li>
<li><p><a href="#heading-24-training">2.4 Training</a></p>
</li>
<li><p><a href="#heading-241-setting-the-diffusion-rate">2.4.1 Setting the Diffusion Rate</a></p>
</li>
<li><p><a href="#heading-25-multiplying-distributions-and-computing-posteriors">2.5 Multiplying Distributions and Computing Posteriors</a></p>
</li>
<li><p><a href="#heading-251-modified-marginal-distributions">2.5.1 Modified Marginal Distributions</a></p>
</li>
<li><p><a href="#heading-252-modified-diffusion-steps">2.5.2 Modified Diffusion Steps</a></p>
</li>
<li><p><a href="#heading-253-applying-the-conditioning-function-rxtrxtrxt">2.5.3 Applying the Conditioning Function</a></p>
</li>
<li><p><a href="#heading-254-choosing-the-conditioning-function-rxtrxtrxt">2.5.4 Choosing the Conditioning Function</a></p>
</li>
<li><p><a href="#heading-26-entropy-of-the-reverse-process">2.6 Entropy of the Reverse Process</a></p>
</li>
</ul>
</li>
<li><p><a href="#heading-3-experiments">3. Experiments</a></p>
<ul>
<li><p><a href="#heading-31-toy-problems">3.1 Toy Problems</a></p>
</li>
<li><p><a href="#heading-312-binary-heartbeat-distribution">3.1.2 Binary Heartbeat Distribution</a></p>
</li>
<li><p><a href="#heading-32-images">3.2 Images</a></p>
</li>
<li><p><a href="#heading-321-datasets">3.2.1 Datasets</a></p>
</li>
</ul>
</li>
<li><p><a href="#heading-4-conclusion">4. Conclusion</a></p>
</li>
<li><p><a href="#heading-resources">Resources</a></p>
</li>
</ul>
<h2 id="heading-prerequisites">Prerequisites</h2>
<p>This review assumes a basic understanding of <a href="https://en.wikipedia.org/wiki/Probability">probability</a>, <a href="https://en.wikipedia.org/wiki/Linear_algebra">linear algebra</a>, and <a href="https://en.wikipedia.org/wiki/Deep_learning">deep learning fundamentals</a>. Familiarity with <a href="https://en.wikipedia.org/wiki/Markov_chain">Markov chains</a>, <a href="https://en.wikipedia.org/wiki/Normal_distribution">Gaussian distributions</a>, and <a href="https://en.wikipedia.org/wiki/Generative_model">generative models</a> such as <a href="https://arxiv.org/pdf/1312.6114">VAEs</a> or <a href="https://arxiv.org/pdf/1406.2661">GANs</a> will help you appreciate the paper's contributions, but no prior knowledge of diffusion models is required.</p>
<p>Throughout the review, we'll build the key ideas step by step.</p>
<h2 id="heading-abstract">Abstract</h2>
<p>By 2015, generative modeling faced a familiar trade-off: models were usually either expressive enough to capture complex real-world data or simple enough to train and evaluate efficiently, but rarely both. This paper set out to bridge that gap by introducing a new kind of generative model inspired by <a href="https://en.wikipedia.org/wiki/Non-equilibrium_thermodynamics">nonequilibrium thermodynamics</a>.</p>
<p>The core idea is surprisingly intuitive. Instead of learning the data distribution directly, the model first gradually corrupts the data through a forward diffusion process, adding small amounts of noise until only a simple, well-understood distribution remains. It then learns the reverse process, step by step, transforming pure noise back into realistic data.</p>
<p>This formulation gives the model an unusual combination of strengths. It remains flexible enough to model complex datasets while keeping learning, sampling, likelihood evaluation, and posterior inference computationally tractable.</p>
<p>The framework scales naturally to thousands of diffusion steps, laying the foundation for what would later evolve into modern diffusion models. To encourage further research, they released an <a href="https://github.com/Sohl-Dickstein/Diffusion-Probabilistic-Models">open-source reference implementation alongside the paper</a>.</p>
<h2 id="heading-introduction">Introduction</h2>
<p>The paper begins by highlighting one of the oldest challenges in probabilistic machine learning: the trade-off between <a href="https://en.wikipedia.org/wiki/Computational_complexity_theory">tractability and flexibility</a>. In practice, researchers had to choose between models that were easy to work with and models that were powerful enough to represent complex data, but rarely both.</p>
<p>Simple probability distributions, such as <a href="https://en.wikipedia.org/wiki/Normal_distribution">Gaussian</a> or <a href="https://en.wikipedia.org/wiki/Laplace_distribution">Laplace distributions</a>, are mathematically convenient. They're easy to train, evaluate, and sample from, making them attractive for practical applications. The downside is that they struggle to capture the rich, highly structured patterns found in real-world data like images, audio, and text.</p>
<p>At the opposite extreme are highly flexible models, which can represent almost any data distribution. Their limitation is computational rather than expressive: evaluating probabilities requires computing a normalization constant that's often intractable. As a result, training and sampling typically rely on expensive <a href="https://en.wikipedia.org/wiki/Monte_Carlo_method">Monte Carlo methods</a>, making these models difficult to use at scale.</p>
<p>The authors acknowledge that many techniques had already been proposed to narrow this gap, including variational inference, contrastive divergence, score matching, pseudolikelihood, belief propagation, and several other approximation methods.</p>
<p>While these approaches improved the situation, they didn't fundamentally eliminate the trade-off. This unresolved problem was the motivation for the diffusion framework introduced in the rest of the paper.</p>
<p>The infographic below summarizes the central dilemma that motivated this paper, along with the major approaches researchers explored before diffusion probabilistic models emerged.</p>
<img src="https://cdn.hashnode.com/uploads/covers/69ce92860ff860b6de01ed93/0ac3361c-35dc-4dd5-8d50-0b1410970edd.png" alt="Infographic explaining the tractability vs. flexibility trade-off in probabilistic machine learning, the limitations of traditional generative models, and how diffusion probabilistic models overcome this long-standing challenge." style="display:block;margin:0 auto" width="1570" height="1001" loading="lazy">

<h3 id="heading-11-diffusion-probabilistic-models">1.1 Diffusion Probabilistic Models</h3>
<p>After introducing the long-standing trade-off between flexibility and tractability, the paper presents its solution: diffusion probabilistic models. Its goal is ambitious: to build a generative model that is expressive, supports exact sampling, allows efficient posterior computation, and still makes likelihood evaluation practical.</p>
<p>The key insight is to model data as a <a href="https://en.wikipedia.org/wiki/Diffusion_process">Markov diffusion process</a>. Instead of learning a complex data distribution directly, the model starts from a simple distribution, such as a Gaussian, and gradually transforms it into the target data distribution through many small diffusion steps. Rather than treating this Markov chain as merely a computational tool, the chain itself becomes the probabilistic model. Because every transition has a tractable probability, the entire process remains analytically manageable.</p>
<p>Training also becomes simpler. Instead of learning one highly complicated distribution all at once, the model only needs to learn the small changes that occur between consecutive diffusion steps. These local transformations are much easier to estimate while remaining expressive enough to approximate virtually any smooth data distribution.</p>
<p>To demonstrate the versatility of the framework, they evaluate it on a diverse collection of datasets, ranging from simple synthetic data and binary sequences to handwritten digits (MNIST) and natural images, including CIFAR-10, bark textures, and dead leaves. This broad evaluation shows that the same diffusion framework can be applied across very different data domains.</p>
<p>The infographic below illustrates the core intuition behind diffusion probabilistic models, showing how data is gradually transformed into noise before the learned reverse process reconstructs it.</p>
<img src="https://cdn.hashnode.com/uploads/covers/69ce92860ff860b6de01ed93/d812d79e-8fb2-4ce8-86ee-1227a9d17d54.png" alt="Infographic explaining the core idea of diffusion probabilistic models, including forward diffusion, reverse denoising, and the physics-inspired intuition behind learning to generate data from noise." style="display:block;margin:0 auto" width="1570" height="1001" loading="lazy">

<h3 id="heading-12-relationship-to-other-work">1.2 Relationship to Other Work</h3>
<p>Before introducing the algorithm in detail, the paper places its contribution within the broader landscape of generative modeling. It acknowledges that many recent methods, particularly <a href="https://arxiv.org/pdf/1312.6114">Variational Autoencoders (VAEs)</a> had already made significant progress by jointly learning generative models and inference networks.</p>
<p>While its training objective shares similarities with the variational <a href="https://en.wikipedia.org/wiki/Upper_and_lower_bounds">lower bound</a> used in those methods, the underlying philosophy is fundamentally different.</p>
<p>Instead of building on variational Bayesian inference, the proposed framework is rooted in <a href="https://en.wikipedia.org/wiki/Statistical_mechanics">statistical physics</a>. It draws inspiration from nonequilibrium thermodynamics, <a href="https://en.wikipedia.org/wiki/Quasistatic_process">quasi-static processes</a>, and <a href="https://arxiv.org/pdf/physics/9803008">annealed importance sampling</a>.</p>
<p>This perspective leads to several practical advantages: it naturally supports posterior computation by combining distributions, simplifies the design of the forward and reverse processes by giving them the same functional form, scales to thousands of diffusion steps, and provides theoretical bounds on entropy throughout the diffusion process.</p>
<p>The authors also place diffusion models alongside many of the leading generative approaches of the time, including <a href="https://www.cs.toronto.edu/~hinton/absps/ws.pdf">Wake-Sleep</a>, <a href="https://arxiv.org/pdf/1503.05571">Generative Stochastic Networks (GSNs)</a>, <a href="https://arxiv.org/pdf/1605.02226">Neural Autoregressive Distribution Estimators (NADEs)</a>, <a href="https://arxiv.org/pdf/1406.2661">Generative Adversarial Networks (GANs)</a>, i<a href="https://arxiv.org/pdf/1410.8516">nvertible generative models</a>, Bayesian network inversion methods, and Gaussian scale mixture models.</p>
<p>Rather than presenting diffusion as a replacement for these methods, they argue that it offers a different path toward the same goal: learning expressive probability distributions while preserving tractable inference and sampling. The experimental section later compares diffusion models directly with several of these approaches, particularly <a href="https://arxiv.org/pdf/1406.2661">GANs</a> and <a href="https://arxiv.org/pdf/1109.4389">MCGSMs</a>.</p>
<p>Finally, the paper highlights the physics concepts that inspired the framework. Ideas such as Annealed Importance Sampling (AIS), <a href="https://en.wikipedia.org/wiki/Langevin_dynamics">Langevin dynamics</a>, the <a href="https://en.wikipedia.org/wiki/Fokker%E2%80%93Planck_equation">Fokker–Planck equation</a>, and the <a href="https://en.wikipedia.org/wiki/Kolmogorov_equations">Kolmogorov forward and backward equations</a> provide the theoretical foundation for viewing generation as the reversal of a diffusion process.</p>
<p>This connection between machine learning and statistical physics would later become one of the defining characteristics of diffusion models.</p>
<h2 id="heading-2-algorithm">2. Algorithm</h2>
<p>With the motivation established, the paper turns to the core of the method: the diffusion algorithm itself. The central idea is to frame generative modeling as learning the reversal of a carefully designed diffusion process.</p>
<p>Instead of modeling the data distribution directly, the method first defines a forward diffusion process that gradually transforms complex data into a simple, tractable distribution, typically Gaussian noise. It then learns to reverse this process, reconstructing realistic data from noise one small step at a time.</p>
<p>The remainder of this section develops the framework piece by piece. It begins by defining the forward diffusion process, then explains how to learn the reverse process that serves as the generative model.</p>
<p>The authors next show how this formulation enables efficient likelihood evaluation, derive entropy bounds for the reverse trajectory, and demonstrate that the learned model can be combined with other probability distributions to perform tasks such as posterior inference, image denoising, and inpainting.</p>
<p>Together, these components establish the complete mathematical foundation of diffusion probabilistic models.</p>
<h3 id="heading-21-forward-trajectory">2.1 Forward Trajectory</h3>
<p>The algorithm begins with an unusual idea: instead of learning how to generate data, it first learns how to destroy it. Starting from the original data distribution, a small amount of noise is added at every step until the rich structure of the data gradually disappears, eventually becoming a simple distribution such as standard Gaussian noise. Because each noising step is small and follows a Markov process, the entire transformation remains easy to analyze while preparing the model for the much harder task of learning how to reverse it.</p>
<p>A key design choice is that each diffusion step makes only a small perturbation to the data. Individually, these changes are almost imperceptible, but after many steps, the accumulated effect completely removes the original structure. Because every transition depends only on the previous state, a defining property of a Markov chain, the entire forward process is mathematically simple and tractable.</p>
<p>The authors experiment with two types of diffusion processes. For continuous data, such as images, they use Gaussian diffusion, which progressively transforms data into standard Gaussian noise. For discrete data, such as 