---
source_url: https://www.freecodecamp.org/news/from-manufacturing-to-microservices-universal-lessons-about-reliability/
ingested: 2026-07-20
sha256: 4a056de31ff7e3e0b7a48f393e6d886029a2a5e7db93b27bb544877217dad172
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>From Manufacturing to Microservices: Universal Lessons About Reliability</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/from-manufacturing-to-microservices-universal-lessons-about-reliability/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="Software engineers often think reliability is a modern challenge. We discuss uptime, distributed systems, observability, and fault tolerance as if they belong exclusively to cloud computing. In realit">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="From Manufacturing to Microservices: Universal Lessons About Reliability">
    
        <meta property="og:description" content="Software engineers often think reliability is a modern challenge. We discuss uptime, distributed systems, observability, and fault tolerance as if they belong exclusively to cloud computing. In realit">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/from-manufacturing-to-microservices-universal-lessons-about-reliability/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/0de496b0-e02a-48c2-9631-d32a5152d766.png">
    <meta property="article:published_time" content="2026-07-20T13:53:02.235Z">
    <meta property="article:modified_time" content="2026-07-20T13:53:02.235Z">
    
        <meta property="article:tag" content="Microservices">
    
        <meta property="article:tag" content="Software Engineering">
    
        <meta property="article:tag" content="Reliability">
    
        <meta property="article:tag" content="#manufacturing">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="From Manufacturing to Microservices: Universal Lessons About Reliability">
    
        <meta name="twitter:description" content="Software engineers often think reliability is a modern challenge. We discuss uptime, distributed systems, observability, and fault tolerance as if they belong exclusively to cloud computing. In realit">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/from-manufacturing-to-microservices-universal-lessons-about-reliability/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/0de496b0-e02a-48c2-9631-d32a5152d766.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Manish Shivanandhan">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="Microservices, Software Engineering, Reliability, #manufacturing">
    <meta name="twitter:site" content="@freecodecamp">
    
        <meta name="twitter:creator" content="@@manishmshiva">
    

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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/0de496b0-e02a-48c2-9631-d32a5152d766.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/from-manufacturing-to-microservices-universal-lessons-about-reliability/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-20T13:53:02.235Z",
	"dateModified": "2026-07-20T13:53:02.235Z",
	"keywords": "Microservices, Software Engineering, Reliability",
	"description": "Software engineers often think reliability is a modern challenge.\nWe discuss uptime, distributed systems, observability, and fault tolerance as if they belong exclusively to cloud computing.\nIn realit",
	"headline": "From Manufacturing to Microservices: Universal Lessons About Reliability",
	"author": {
		"@type": "Person",
		"name": "Manish Shivanandhan",
		"url": "https://www.freecodecamp.org/news/author/manishshivanandhan/",
		"sameAs": [
			"https://manishmshiva.me",
			"https://x.com/@manishmshiva"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/res/hashnode/image/upload/v1725238262566/37625c8b-4d87-4b8c-8fb7-b4fdcf34de9e.png?w=500&h=500&fit=crop&crop=entropy&auto=compress,format&format=webp",
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-20T13:53:02.235Z">
                            July 20, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/microservices/">
                                #Microservices
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">From Manufacturing to Microservices: Universal Lessons About Reliability</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/res/hashnode/image/upload/v1725238262566/37625c8b-4d87-4b8c-8fb7-b4fdcf34de9e.png?w=500&h=500&fit=crop&crop=entropy&auto=compress,format&format=webp 60w" sizes="60px" src="https://cdn.hashnode.com/res/hashnode/image/upload/v1725238262566/37625c8b-4d87-4b8c-8fb7-b4fdcf34de9e.png?w=500&h=500&fit=crop&crop=entropy&auto=compress,format&format=webp" class="author-profile-image" alt="Manish Shivanandhan" width="500" height="500" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/manishshivanandhan/" data-test-label="profile-link">
                    
                        Manish Shivanandhan
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/0de496b0-e02a-48c2-9631-d32a5152d766.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/0de496b0-e02a-48c2-9631-d32a5152d766.png" alt="From Manufacturing to Microservices: Universal Lessons About Reliability" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>Software engineers often think reliability is a modern challenge.</p>
<p>We discuss uptime, distributed systems, observability, and fault tolerance as if they belong exclusively to cloud computing.</p>
<p>In reality, engineers have been solving reliability problems for centuries. Manufacturing plants, civil engineering projects, and industrial assembly lines have all faced the same fundamental question: how do you build systems that continue working even when individual components fail?</p>
<p>Whether you're assembling a bridge, manufacturing a vehicle, or deploying a microservice architecture, reliability is never accidental. It comes from thoughtful design, continuous testing, and a willingness to learn from failure.</p>
<p>The technology has changed, but the engineering principles have remained remarkably consistent.</p>
<p>In this article, we'll explore the timeless engineering principles that make systems reliable, whether they're factory assembly lines or cloud-native applications.</p>
<p>You'll see how concepts like redundancy, root cause analysis, realistic testing, and observability have guided engineers for decades, and why these lessons are just as valuable when building modern software.</p>
<p>By the end, you'll have a broader perspective on reliability and practical ideas you can apply to design more resilient systems.</p>
<h3 id="heading-what-well-cover">What We'll Cover:</h3>
<ul>
<li><p><a href="#heading-every-system-is-only-as-reliable-as-its-weakest-link">Every System Is Only as Reliable as Its Weakest Link</a></p>
</li>
<li><p><a href="#heading-small-defects-become-big-problems">Small Defects Become Big Problems</a></p>
</li>
<li><p><a href="#heading-root-cause-analysis-is-more-important-than-finding-someone-to-blame">Root Cause Analysis Is More Important Than Finding Someone to Blame</a></p>
</li>
<li><p><a href="#heading-redundancy-is-an-investment-not-a-waste">Redundancy Is an Investment, Not a Waste</a></p>
</li>
<li><p><a href="#heading-testing-should-simulate-reality">Testing Should Simulate Reality</a></p>
</li>
<li><p><a href="#heading-observability-is-better-than-guesswork">Observability Is Better Than Guesswork</a></p>
</li>
<li><p><a href="#heading-reliability-is-a-continuous-process">Reliability Is a Continuous Process</a></p>
</li>
<li><p><a href="#heading-great-engineering-is-predictable-engineering">Great Engineering Is Predictable Engineering</a></p>
</li>
</ul>
<h2 id="heading-every-system-is-only-as-reliable-as-its-weakest-link"><strong>Every System Is Only as Reliable as Its Weakest Link</strong></h2>
<p>A modern application may consist of dozens or even hundreds of services. Each service depends on databases, APIs, queues, caches, storage systems, and network infrastructure. A failure in any one of these components can ripple throughout the entire application.</p>
<p>Manufacturing systems work in much the same way. A perfectly designed product can still fail if one component is installed incorrectly or if quality checks are skipped during production.</p>
<p>This highlights an important lesson for software engineers: reliability isn't about building perfect components. It's about ensuring the entire system can tolerate imperfections.</p>
<p>Experienced engineering teams rarely assume everything will work perfectly. Instead, they ask questions like:</p>
<ul>
<li><p>What happens if this service becomes unavailable?</p>
</li>
<li><p>Can another component take over?</p>
</li>
<li><p>How quickly can the system recover?</p>
</li>
<li><p>Can users continue working while the issue is resolved?</p>
</li>
</ul>
<p>Designing around failure is often more valuable than trying to eliminate every possible failure.</p>
<h2 id="heading-small-defects-become-big-problems"><strong>Small Defects Become Big Problems</strong></h2>
<p>Many major outages begin with something surprisingly small.</p>
<p>A configuration value is incorrect. A certificate expires. A retry loop overwhelms a downstream service. A cache becomes stale. An API starts returning unexpected responses.</p>
<p>None of these issues appear catastrophic on their own. The real damage comes when multiple small problems combine into a larger system failure.</p>
<p>Manufacturing follows the same pattern. A slightly misaligned component may seem harmless during assembly, but over time it can increase wear, reduce efficiency, and eventually cause an expensive breakdown.</p>
<p>Software systems behave similarly. Small <a href="https://www.ibm.com/think/topics/technical-debt">technical debt</a> accumulates until reliability begins to suffer.</p>
<p>This is why experienced teams invest in routine maintenance. Refactoring, dependency updates, infrastructure improvements, and automated testing may not deliver visible product features, but they significantly reduce operational risk.</p>
<p>Reliability is built through consistent attention to small details.</p>
<h2 id="heading-root-cause-analysis-is-more-important-than-finding-someone-to-blame"><strong>Root Cause Analysis Is More Important Than Finding Someone to Blame</strong></h2>
<p>When production systems fail, organisations often rush to identify who made the mistake.</p>
<p>The better question is why the mistake was possible in the first place.</p>
<p>Perhaps deployment safeguards were missing. Or monitoring failed to detect unusual behaviour. Or the documentation was outdated.</p>
<p>Perhaps code reviews overlooked an important edge case.</p>
<p>Strong engineering cultures focus on improving systems rather than assigning blame.</p>
<p>This philosophy exists throughout engineering disciplines. Manufacturing companies spend significant effort studying common <a href="https://constructiondaily.news/common-failures-in-material-assembly-and-how-to-prevent-them/">failures in material assembly</a> because understanding why defects occur leads to stronger processes, better inspections, and fewer future failures.</p>
<p>Software teams benefit from the same mindset. Every production incident becomes an opportunity to improve automation, monitoring, documentation, and testing rather than simply fixing the immediate issue.</p>
<p>Blameless postmortems encourage engineers to report problems early because they know the goal is learning rather than punishment.</p>
<p>Over time, this creates systems that become progressively more reliable.</p>
<h2 id="heading-redundancy-is-an-investment-not-a-waste"><strong>Redundancy Is an Investment, Not a Waste</strong></h2>
<p>At first glance, redundancy appears inefficient.</p>
<p>Why run multiple application instances? Why maintain replica databases? Why deploy services across multiple regions? Why store multiple backups?</p>
<p>The answer becomes clear when failures occur.</p>
<p>If every critical component has only one instance, every failure becomes a complete outage.</p>
<p>Manufacturing plants frequently maintain backup equipment for exactly this reason. Downtime often costs far more than maintaining spare capacity.</p>
<p>Cloud infrastructure follows the same principle. Load balancers distribute requests across multiple servers. Database replicas reduce the impact of hardware failures. <a href="https://aws.amazon.com/message-queue/">Message queues</a> prevent temporary spikes from overwhelming downstream systems.</p>
<p>Multiple availability zones protect against regional outages.</p>
<p>Redundancy increases costs, but it dramatically improves resilience.</p>
<p>Organisations must decide whether the cost of additional infrastructure is lower than the potential cost of downtime.</p>
<p>For customer-facing applications, the answer is usually yes.</p>
<h2 id="heading-testing-should-simulate-reality"><strong>Testing Should Simulate Reality</strong></h2>
<p>Passing unit tests doesn't necessarily mean software is reliable.</p>
<p>Many production failures occur because real-world environments behave differently than development machines.</p>
<p>Networks become slow. External APIs return unexpected responses. Databases experience temporary latency. Users generate traffic patterns nobody anticipated.</p>
<p>Reliable engineering requires testing under realistic conditions.</p>
<p>Integration tests verify communication between services. Load testing evaluates system behavior under heavy traffic. Chaos engineering intentionally introduces failures to measure resilience.</p>
<p>Disaster recovery exercises ensure backup procedures actually work.</p>
<p>Manufacturing industries also perform stress testing before products reach customers. Components are exposed to extreme temperatures, vibration, pressure, and repeated use to identify weaknesses before they become field failures.</p>
<p>Software deserves the same level of scrutiny. The closer testing resembles production, the fewer surprises engineers encounter after deployment.</p>
<h2 id="heading-observability-is-better-than-guesswork"><strong>Observability Is Better Than Guesswork</strong></h2>
<p>When a production issue occurs, every minute matters. Without visibility into system behaviour, engineers are forced to make educated guesses. Guessing rarely solves outages quickly.</p>
<p>Modern observability combines logs, metrics, traces, and alerts into a complete picture of system health.</p>
<p>Logs explain what happened. Metrics reveal performance trends. Distributed tracing follows requests across multiple services. Dashboards expose unusual behavior before customers notice problems.</p>
<p>Together, these tools dramatically reduce the time required to diagnose incidents. The goal isn't collecting more data. The goal is collecting meaningful data that answers important operational questions:</p>
<ul>
<li><p>Can engineers identify the failing service?</p>
</li>
<li><p>Can they measure customer impact?</p>
</li>
<li><p>Can they determine when the problem began?</p>
</li>
<li><p>Can they verify that a fix actually resolved the issue?</p>
</li>
</ul>
<p>Observability transforms debugging from detective work into engineering.</p>
<h2 id="heading-reliability-is-a-continuous-process"><strong>Reliability Is a Continuous Process</strong></h2>
<p>Many organisations mistakenly treat reliability as a one-time project. They improve monitoring after an outage. They add automated tests after discovering a regression. They introduce deployment pipelines after a failed release.</p>
<p>These improvements help, but reliability isn't something you complete once and forget.</p>
<p>Every new feature introduces additional complexity. Every dependency update changes system behavior. Every scaling decision creates new operational challenges.</p>
<p>Reliable systems require continuous evaluation.</p>
<p>Engineering teams regularly review incidents, remove technical debt, improve automation, and update operational documentation because yesterday's reliable architecture may not meet tomorrow's demands.</p>
<p>Reliability evolves alongside the software itself.</p>
<h2 id="heading-great-engineering-is-predictable-engineering"><strong>Great Engineering Is Predictable Engineering</strong></h2>
<p>Users rarely notice reliable systems. Nobody celebrates an application that simply works every day.</p>
<p>Instead, attention often focuses on new features, product launches, and innovative technologies.</p>
<p>Yet reliability remains one of the strongest competitive advantages any engineering organisation can build.</p>
<p>Customers trust applications that remain available. Developers enjoy working on systems that behave predictably. Businesses avoid the financial and reputational costs associated with outages.</p>
<p>Manufacturing has long understood that quality is built into every stage of production rather than inspected in at the end. Software engineering follows exactly the same principle. Reliability emerges from thoughtful architecture, disciplined testing, effective monitoring, continuous learning, and a culture that treats every failure as an opportunity to improve.</p>
<p>From factory floors to cloud-native microservices, the lesson remains unchanged. Strong systems aren't defined by the absence of failure. They're defined by how well they anticipate it, absorb it, and recover from it.</p>
<p>The technologies may continue to evolve, but the fundamentals of reliable engineering are timeless.</p>
<p>Hope you enjoyed this article. You can <a href="https://linkedin.com/in/manishmshiva">connect with me on LinkedIn</a>.</p>


                        </section>
                        
                            <div class="sidebar">
                                
                                    
                                    <script>var localizedAdText = "ADVERTISEMENT";</script>
                                
                            </div>
                        
                    </div>
                    <hr>
                    
                        <div class="post-full-author-header" data-test-label="author-header-with-bio">
                            
                                
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/res/hashnode/image/upload/v1725238262566/37625c8b-4d87-4b8c-8fb7-b4fdcf34de9e.png?w=500&h=500&fit=crop&crop=entropy&auto=compress,format&format=webp 60w" sizes="60px" src="https://cdn.hashnode.com/res/hashnode/image/upload/v1725238262566/37625c8b-4d87-4b8c-8fb7-b4fdcf34de9e.png?w=500&h=500&fit=crop&crop=entropy&auto=compress,format&format=webp" class="author-profile-image" alt="Manish Shivanandhan" width="500" height="500" onerror="this.style.display='none'" loading="lazy" data-test-label="profile-image">
  
        

        <section class="author-card-content ">
            <span class="author-card-name">
                <a href="/news/author/manishshivanandhan/" data-test-label="profile-link">
                    
                        Manish Shivanandhan
                    
                </a>
            </span>
            
                
                    <p data-test-label="default-bio">
                        Read <a href="/news/author/manishshivanandhan/">more posts</a>.
                    </p>
                
            
        </section>
    </section>

                            
                        </div>
                        <hr>
                    

                    
                    
                        
    


<p data-test-label="social-row-cta" class="social-row">
    If you read this far, thank the author to show them you care. <button id="tweet-btn" class="cta-button" data-test-label="tweet-button">Say Thanks</button>
</p>


    
    <script>document.addEventListener("DOMContentLoaded",()=>{const t=document.getElementById("tweet-btn"),n=window.location,e="From%20Manufacturing%20to%20Microservices%3A%20Universal%20Lessons%20About%20Reliability".replace(/&#39;/g,"%27"),o="",i="@@manishmshiva",r=Boolean("");let s;if(r&&(o||i)){const t={originalPostAuthor:"",currentPostAuthor:"Manish Shivanandhan"};s=encodeURIComponent(`Thank you ${o||t.originalPostAuthor} for writing this helpful article, and ${i||t.currentPostAuthor} for translating it.`)}else!r&&i&&(s=encodeURIComponent(`Thank you ${i} for writing this helpful article.`));const a=`window.open(\n    '${s?`https://x.com/intent/post?text=${s}%0A%0A${e}%0A%0A${n}`:`https://x.com/intent/post?text=${e}%0A%0A${n}`}',\n    'share-twitter',\n    'width=550, height=235'\n  ); return false;`;t.setAttribute("onclick",a)});</script>


                        

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
            <p data-test-label="donation-initiatives">Donations to freeCodeCamp go toward our education initiatives, and help pay for servers, services, and staff.</p>
            <p class="footer-donation" data-test-label="donate-text">
                You can <a href="https://www.freecodecamp.org/donate/" class="inline" rel="noopener noreferrer" target="_blank">make a tax-deductible donation here</a>.
            </p>
        </div>
        <div class="trending-guides" data-test-label="trending-guides">
            <h2 id="trending-guides" class="col-header">Trending Books and Handbooks</h2>
            <ul class="trending-guides-articles" aria-labelledby="trending-guides">
                <li>
                    <a href="https://www.freecodecamp.org/news/build-consume-and-document-a-rest-api/" rel="noopener noreferrer" target="_blank">REST APIs
                    </a>
                </li>
                <li>
                    <a href="https://www.freecodecamp.org/news/how-to-write-clean-code/" rel="noopener noreferrer" target="_blank">Clean Code
                    </a>
                </li>
                <li>
                    <a href="https://www.freecodecamp.org/news/learn-typescript-with-react-handbook/" rel="noopener noreferrer" target="_blank">TypeScript
                    </a>
                </li>
                <li>
                    <a href="https://www.freecodecamp.org/news/learn-javascript-for-beginners/" rel="noopener noreferrer" target="_blank">JavaScript
                    </a>
                </li>
                <li>
                    <a href="https://www.freecodecamp.org/news/how-to-build-an-ai-chatbot-with-redis-python-and-gpt/" rel="noopener noreferrer" target="_blank">AI Chatbots
                    </a>
                </li>
                <li>
                    <a href="https://www.freecodecamp.org/news/command-line-for-beginners/" rel="noopener noreferrer" target="_blank">Command Line
                    </a>
                </li>
                <li>
                    <a href="https://www.freecodecamp.org/news/building-consuming-and-documenting-a-graphql-api/" rel="noopener noreferrer" target="_blank">GraphQL APIs
                    </a>
                </li>
                <li>
                    <a href="https://www.freecodecamp.org/news/complete-guide-to-css-transform-functions-and-properties/" rel="noopener noreferrer" target="_blank">CSS Transforms
                    </a>
                </li>
                <li>
                    <a href="https://www.freecodecamp.org/news/how-to-build-scalable-access-control-for-your-web-app/" rel="noopener noreferrer" target="_blank">Access Control
                    </a>
                </li>
                <li>
                    <a href="https://www.freecodecamp.org/news/rest-api-design-best-practices-build-a-rest-api/" rel="noopener noreferrer" target="_blank">REST API Design
                    </a>
                </li>
                <li>
                    <a href="https://www.freecodecamp.org/news/the-php-handbook/" rel="noopener noreferrer" target="_blank">PHP
                    </a>
                </li>
                <li>
                    <a href="https://www.freecodecamp.org/news/the-java-handbook/" rel="noopener noreferrer" target="_blank">Java
        