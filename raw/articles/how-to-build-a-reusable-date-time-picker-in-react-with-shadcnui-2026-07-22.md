---
source_url: https://www.freecodecamp.org/news/build-a-reusable-date-time-picker-in-react-with-shadcn-ui/
ingested: 2026-07-22
sha256: a5b1bd9c580fc07abab73f003f893d9238dc6f34619df09c97c0a5691e9dffc8
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Build a Reusable Date-Time Picker in React with shadcn/ui</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/build-a-reusable-date-time-picker-in-react-with-shadcn-ui/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="A date and time picker is one of those components that looks small in a design file and turns into a real time sink once you start building it. You need a calendar, a time selector, a state that keeps">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Build a Reusable Date-Time Picker in React with shadcn/ui">
    
        <meta property="og:description" content="A date and time picker is one of those components that looks small in a design file and turns into a real time sink once you start building it. You need a calendar, a time selector, a state that keeps">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/build-a-reusable-date-time-picker-in-react-with-shadcn-ui/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/7dcddc1c-2a9d-4af7-8f02-ffb76bea2c7b.png">
    <meta property="article:published_time" content="2026-07-22T16:47:40.245Z">
    <meta property="article:modified_time" content="2026-07-22T16:47:40.245Z">
    
        <meta property="article:tag" content="shadcn ui">
    
        <meta property="article:tag" content="JavaScript">
    
        <meta property="article:tag" content="React">
    
        <meta property="article:tag" content="Web Development">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Build a Reusable Date-Time Picker in React with shadcn/ui">
    
        <meta name="twitter:description" content="A date and time picker is one of those components that looks small in a design file and turns into a real time sink once you start building it. You need a calendar, a time selector, a state that keeps">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/build-a-reusable-date-time-picker-in-react-with-shadcn-ui/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/7dcddc1c-2a9d-4af7-8f02-ffb76bea2c7b.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Vaibhav Gupta">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="shadcn ui, JavaScript, React, Web Development">
    <meta name="twitter:site" content="@freecodecamp">
    
        <meta name="twitter:creator" content="@gupta05_vaibhav">
    

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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/7dcddc1c-2a9d-4af7-8f02-ffb76bea2c7b.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/build-a-reusable-date-time-picker-in-react-with-shadcn-ui/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-22T16:47:40.245Z",
	"dateModified": "2026-07-22T16:47:40.245Z",
	"keywords": "shadcn ui, JavaScript, React, Web Development",
	"description": "A date and time picker is one of those components that looks small in a design file and turns into a real time sink once you start building it. You need a calendar, a time selector, a state that keeps",
	"headline": "How to Build a Reusable Date-Time Picker in React with shadcn/ui",
	"author": {
		"@type": "Person",
		"name": "Vaibhav Gupta",
		"url": "https://www.freecodecamp.org/news/author/vaibhavg/",
		"sameAs": [
			"https://shadcnspace.com/",
			"https://x.com/gupta05_vaibhav"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/uploads/avatars/68b53a3d851476bd2ce87f12/36933dbd-163e-4180-8160-5390f7f67860.jpg",
			"width": 1280,
			"height": 960
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-22T16:47:40.245Z">
                            July 22, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/shadcn-ui/">
                                #shadcn ui
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Build a Reusable Date-Time Picker in React with shadcn/ui</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/uploads/avatars/68b53a3d851476bd2ce87f12/36933dbd-163e-4180-8160-5390f7f67860.jpg 60w" sizes="60px" src="https://cdn.hashnode.com/uploads/avatars/68b53a3d851476bd2ce87f12/36933dbd-163e-4180-8160-5390f7f67860.jpg" class="author-profile-image" alt="Vaibhav Gupta" width="1280" height="960" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/vaibhavg/" data-test-label="profile-link">
                    
                        Vaibhav Gupta
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/7dcddc1c-2a9d-4af7-8f02-ffb76bea2c7b.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/7dcddc1c-2a9d-4af7-8f02-ffb76bea2c7b.png" alt="How to Build a Reusable Date-Time Picker in React with shadcn/ui" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>A date and time picker is one of those components that looks small in a design file and turns into a real time sink once you start building it. You need a calendar, a time selector, a state that keeps both in sync, and usually a range mode and a translated version somewhere down the line, too.</p>
<p>This guide walks through ready-made picker patterns you can drop into a React project today: a combined date and time picker, a date range picker, and a time picker.</p>
<p>Every one of these is available as a <a href="https://shadcnspace.com/components/date-picker"><strong>Shadcn Date Picker</strong></a> component you can install with a single CLI command instead of building from scratch.</p>
<p>These components are built on both Radix and Base UI primitives, and the versions below use Base UI. They also support copy-prompt functionality, so you can paste them straight into v0, Lovable, or Bolt if that's part of your workflow.</p>
<h2 id="heading-table-of-contents"><strong>Table of Contents</strong></h2>
<ul>
<li><p><a href="#heading-prerequisites">Prerequisites</a></p>
</li>
<li><p><a href="#heading-what-youll-build">What You'll Build</a></p>
</li>
<li><p><a href="#heading-how-to-install-a-shadcn-date-time-picker">How to Install a Shadcn Date Time Picker</a></p>
</li>
<li><p><a href="#heading-how-to-build-a-date-and-time-picker">How to Build a Date and Time Picker</a></p>
</li>
<li><p><a href="#heading-how-to-build-a-date-range-picker">How to Build a Date Range Picker</a></p>
</li>
<li><p><a href="#heading-how-to-build-a-time-picker">How to Build a Time Picker</a></p>
</li>
<li><p><a href="#heading-live-preview-of-the-components">Live Preview of the components</a></p>
</li>
<li><p><a href="#heading-key-concepts-recap">Key Concepts Recap</a></p>
</li>
<li><p><a href="#heading-conclusion">Conclusion</a></p>
</li>
<li><p><a href="#heading-resources">Resources</a></p>
</li>
</ul>
<h2 id="heading-prerequisites">Prerequisites</h2>
<p>To follow along, you should know:</p>
<ul>
<li><p>The basics of React, including <code>useState</code> and props</p>
</li>
<li><p>How to install components with the shadcn/ui CLI</p>
</li>
<li><p>Basic Tailwind CSS class names</p>
</li>
</ul>
<p>You also need a React project with shadcn/ui already set up. If you haven't done that yet, run the shadcn/ui CLI setup command in your project before continuing.</p>
<h2 id="heading-what-youll-build">What You'll Build</h2>
<ul>
<li><p>A <code>DateTimePicker</code> component that combines a calendar and time slots into one value.</p>
</li>
<li><p>A <code>TimePicker</code> variant that reuses the same time-slot logic without a calendar.</p>
</li>
<li><p>A <code>DateRangePicker</code> that lets a user pick a start and end date.</p>
</li>
</ul>
<h2 id="heading-how-to-install-a-shadcn-date-time-picker"><strong>How to Install a Shadcn Date Time Picker</strong></h2>
<p>All the components below install through the same CLI pattern. Pick the package manager you use:</p>
<p><strong>pnpm</strong></p>
<pre><code class="language-javascript">pnpm dlx shadcn@latest add @shadcn-space/date-picker-01
</code></pre>
<p><strong>npm</strong></p>
<pre><code class="language-javascript">npx shadcn@latest add @shadcn-space/date-picker-01
</code></pre>
<p><strong>yarn</strong></p>
<pre><code class="language-javascript">yarn dlx shadcn@latest add @shadcn-space/date-picker-01
</code></pre>
<p><strong>bun</strong></p>
<pre><code class="language-javascript">bunx --bun shadcn@latest add @shadcn-space/date-picker-01
</code></pre>
<p>Every other component below installs the same way: just swap the package name at the end of the command. If you haven't set up the CLI in your project yet, this <a href="https://shadcnspace.com/docs/getting-started/how-to-use-shadcn-cli"><strong>getting-started guide</strong></a> covers that first and shows how to integrate these components when you're working through an MCP-connected editor.</p>
<h2 id="heading-how-to-build-a-date-and-time-picker"><strong>How to Build a Date and Time Picker</strong></h2>
<p>This is the combined picker: a calendar popover for the date, plus start and end time fields, wrapped around a booking confirmation flow.</p>
<p><strong>Folder structure:</strong></p>
<pre><code class="language-javascript">components
└── shadcn-space
    └── date-picker
        └── date-picker-01.tsx
</code></pre>
<p><strong>Component code:</strong></p>
<pre><code class="language-javascript">"use client";
import { useState } from "react";
import { format } from "date-fns";
import { CalendarIcon, Clock, ChevronDown, Check } from "lucide-react";
import { cn } from "@/lib/utils";

import { Button } from "@/components/ui/button";
import { Calendar } from "@/components/ui/calendar";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";

const DateAndTimePickerDemo = () =&gt; {
  const [open, setOpen] = useState(false);
  const [date, setDate] = useState&lt;Date | undefined&gt;(undefined);
  const [bookingStatus, setBookingStatus] = useState&lt;
    "idle" | "loading" | "success"
  &gt;("idle");

  const handleBooking = () =&gt; {
    setBookingStatus("loading");
    setTimeout(() =&gt; setBookingStatus("success"), 1500);
  };

  return (
    &lt;&gt;
      &lt;div className="grid gap-6"&gt;
        &lt;div className="grid gap-2"&gt;
          &lt;Label htmlFor="date" className="text-sm font-semibold"&gt;
            Select Date
          &lt;/Label&gt;
          &lt;Popover open={open} onOpenChange={setOpen}&gt;
            &lt;PopoverTrigger
              onPointerDown={() =&gt; setBookingStatus("idle")}
              render={
                &lt;Button
                  variant="outline"
                  id="date"
                  className={cn(
                    "w-full justify-start text-left font-normal h-10 transition-all hover:bg-muted/50 cursor-pointer",
                    !date &amp;&amp; "text-muted-foreground",
                  )}
                &gt;
                  &lt;CalendarIcon className="mr-2 h-4 w-4 opacity-70" /&gt;
                  {date ? format(date, "PPP") : &lt;span&gt;Select a date&lt;/span&gt;}
                  &lt;ChevronDown className="ml-auto h-4 w-4 opacity-50" /&gt;
                &lt;/Button&gt;
              }
            /&gt;
            &lt;PopoverContent
              className="w-auto p-0 border-muted-foreground/10 shadow-2xl"
              align="start"
            &gt;
              &lt;Calendar
                mode="single"
                selected={date}
                onSelect={(d) =&gt; {
                  setDate(d);
                  setOpen(false);
                }}
                className="rounded-md border-none"
              /&gt;
            &lt;/PopoverContent&gt;
          &lt;/Popover&gt;
        &lt;/div&gt;

        &lt;div className="grid grid-cols-2 gap-4"&gt;
          &lt;div className="grid gap-2"&gt;
            &lt;Label
              htmlFor="time-from"
              className="text-sm font-semibold text-muted-foreground flex items-center gap-1.5"
            &gt;
              &lt;Clock className="size-3.5" /&gt; Start Time
            &lt;/Label&gt;
            &lt;Input
              type="time"
              id="time-from"
              defaultValue="09:00"
              className="h-10 bg-background appearance-none transition-all focus:ring-2 focus:ring-primary/20"
            /&gt;
          &lt;/div&gt;
          &lt;div className="grid gap-2"&gt;
            &lt;Label
              htmlFor="time-to"
              className="text-sm font-semibold text-muted-foreground flex items-center gap-1.5"
            &gt;
              &lt;Clock className="size-3.5" /&gt; End Time
            &lt;/Label&gt;
            &lt;Input
              type="time"
              id="time-to"
              defaultValue="10:00"
              className="h-10 bg-background appearance-none transition-all focus:ring-2 focus:ring-primary/20"
            /&gt;
          &lt;/div&gt;
        &lt;/div&gt;

        &lt;Button
          className="w-full h-11 font-semibold transition-all group overflow-hidden relative cursor-pointer"
          onClick={handleBooking}
          disabled={!date || bookingStatus !== "idle"}
        &gt;
          {bookingStatus === "idle" &amp;&amp; (
            &lt;span className="flex items-center gap-2"&gt;Confirm Meet&lt;/span&gt;
          )}
          {bookingStatus === "loading" &amp;&amp; (
            &lt;div className="flex items-center gap-2"&gt;
              &lt;div className="h-4 w-4 animate-spin rounded-full border-2 border-current border-t-transparent" /&gt;
              Processing...
            &lt;/div&gt;
          )}
          {bookingStatus === "success" &amp;&amp; (
            &lt;span className="flex items-center gap-2 animate-in zoom-in-50 duration-300"&gt;
              &lt;Check className="h-4 w-4" /&gt;
              Meet Scheduled!
            &lt;/span&gt;
          )}
        &lt;/Button&gt;
      &lt;/div&gt;
    &lt;/&gt;
  );
};

export default DateAndTimePickerDemo;
</code></pre>
<h3 id="heading-how-this-component-works">How This Component Works</h3>
<p>This component combines three pieces of state into a simple booking flow:</p>
<ul>
<li><p>The selected date</p>
</li>
<li><p>Start and end times</p>
</li>
<li><p>The booking status (idle, loading, success)</p>
</li>
</ul>
<p>The date is stored using React state:</p>
<pre><code class="language-javascript">const [date, setDate] = useState&lt;Date | undefined&gt;(undefined);
</code></pre>
<p>When a user selects a day from the calendar, the <code>onSelect</code> callback updates the state and closes the popover:</p>
<pre><code class="language-javascript">onSelect={(d) =&gt; {
  setDate(d);
  setOpen(false);
}}
</code></pre>
<p>The calendar itself lives inside a <code>Popover</code>, which keeps the UI compact. Clicking the trigger button opens the calendar panel:</p>
<pre><code class="language-plaintext">&lt;Popover open={open} onOpenChange={setOpen}&gt;
</code></pre>
<p>The displayed date uses <code>date-fns</code> formatting:</p>
<pre><code class="language-plaintext">format(date, "PPP")
</code></pre>
<p>This converts a JavaScript <code>Date</code> object into a readable format such as:</p>
<pre><code class="language-plaintext">July 22, 2026
</code></pre>
<p>The time fields use native HTML inputs:</p>
<pre><code class="language-plaintext">&lt;Input type="time" /&gt;
</code></pre>
<p>Native time inputs provide built-in browser support, mobile pickers, keyboard accessibility, and locale-aware formatting without additional libraries.</p>
<p>The booking button demonstrates how UI state can change during an async action:</p>
<pre><code class="language-plaintext">"idle" → "loading" → "success"
</code></pre>
<p>In a real application, <code>handleBooking()</code> would typically call an API endpoint instead of using <code>setTimeout</code>.</p>
<p>This pattern works well for:</p>
<ul>
<li><p>Meeting schedulers</p>
</li>
<li><p>Appointment systems</p>
</li>
<li><p>Interview booking tools</p>
</li>
<li><p>Event registration forms</p>
</li>
<li><p>SaaS scheduling workflows</p>
</li>
</ul>
<h2 id="heading-how-to-build-a-date-range-picker"><strong>How to Build a Date Range Picker</strong></h2>
<p>For anything involving a stay, a rental, or a multi-day booking, you need a range instead of a single date. This component pairs a two-month calendar view with a formatted range label and a computed night count.</p>
<p><strong>Folder structure:</strong></p>
<pre><code class="language-javascript">components
└── shadcn-space
    └── date-picker
        └── date-picker-02.tsx
</code></pre>
<p>Install this Shadcn Date Range Picker with:</p>
<pre><code class="language-javascript">npx shadcn@latest add @shadcn-space/date-picker-02
</code></pre>
<p><strong>Component code:</strong></p>
<pre><code class="language-javascript">"use client";
import * as React from "react";
import { CalendarIcon, ChevronDown } from "lucide-react";
import { addDays, format } from "date-fns";
import { DateRange } from "react-day-picker";

import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Calendar } from "@/components/ui/calendar";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import { Label } from "@/components/ui/label";

const DateRangePickerDemo = () =&gt; {
  const [date, setDate] = React.useState&lt;DateRange | undefined&gt;({
    from: new Date(),
    to: addDays(new Date(), 7),
  });

  return (
    &lt;div className="grid gap-3 max-w-sm mx-auto"&gt;
      &lt;Label htmlFor="date-range" className="text-sm font-medium px-1"&gt;
        Select Travel Dates
      &lt;/Label&gt;
      &lt;div className={cn("grid gap-2")}&gt;
        &lt;Popover&gt;
          &lt;PopoverTrigger
            render={
              &lt;Button
                id="date-range"
                variant={"outline"}
                className={cn(
                  "w-full justify-start text-left font-normal h-11 transition-all hover:bg-muted/50 focus:ring-2 focus:ring-primary/20 cursor-pointer",
                  !date &amp;&amp; "text-muted-foreground",
                )}
              &gt;
                &lt;CalendarIcon className="mr-2 h-4 w-4 opacity-70" /&gt;
                {date?.from ? (
                  date.to ? (
                    &lt;&gt;
                      {format(date.from, "LLL dd, y")} -{" "}
                      {format(date.to, "LLL dd, y")}
                    &lt;/&gt;
                  ) : (
                    format(date.from, "LLL dd, y")
                  )
                ) : (
                  &lt;span&gt;Pick a range&lt;/span&gt;
                )}
                &lt;ChevronDown className="ml-auto h-4 w-4 opacity-50" /&gt;
              &lt;/Button&gt;
            }
          /&gt;
          &lt;PopoverContent
            className="w-auto p-0 border-muted/20 shadow-xl"
            align="start"
          &gt;
            &lt;Calendar
              mode="range"
              defaultMonth={date?.from}
              selected={date}
              onSelect={setDate}
              numberOfMonths={2}
              className="p-3"
            /&gt;
          &lt;/PopoverContent&gt;
        &lt;/Popover&gt;
      &lt;/div&gt;
      &lt;p className="text-xs text-muted-foreground px-1"&gt;
        {date?.from &amp;&amp; date?.to
          ? `Stay duration: ${Math.round((date.to.getTime() - date.from.getTime()) / (1000 * 60 * 60 * 24))} nights`
          : "Please select a valid date range."}
      &lt;/p&gt;
    &lt;/div&gt;
  );
};

export default DateRangePickerDemo;
</code></pre>
<h3 id="heading-how-the-date-range-picker-works">How the Date Range Picker Works</h3>
<p>This version switches the Calendar component from single-date mode to range mode:</p>
<pre><code class="language-javascript">mode="range"
</code></pre>
<p>Instead of storing one <code>Date</code>, the component stores a <code>DateRange</code> object:</p>
<pre><code class="language-javascript">{
  from: Date,
  to: Date
}
</code></pre>
<p>This makes it easy to work with booking systems, hotel stays, travel forms, and rental applications.</p>
<p>The component displays two calendar months:</p>
<pre><code class="language-javascript">numberOfMonths={2}
</code></pre>
<p>Showing two months reduces navigation and improves the selection experience for longer stays.</p>
<p>The stay duration is calculated directly from the selected dates:</p>
<pre><code class="language-javascript">(date.to.getTime() - date.from.getTime())
</code></pre>
<p>This avoids additional libraries and keeps the logic simple.</p>
<p>Compared to the first example:</p>
<ul>
<li><p>Uses <code>DateRange</code> instead of a single <code>Date</code></p>
</li>
<li><p>Uses <code>mode="range"</code></p>
</li>
<li><p>Displays two months</p>
</li>
<li><p>Adds derived data like total nights</p>
</li>
</ul>
<h2 id="heading-how-to-build-a-time-picker"><strong>How to Build a Time Picker</strong></h2>
<p>Not every form needs a calendar. This one wraps the native in an InputGroup with a clock icon that triggers the browser's own time picker UI on click.</p>
<p><strong>Folder structure:</strong></p>
<pre><code class="language-javascript">components
└── shadcn-space
    └── date-picker
        └── date-picker-03.tsx
</code></pre>
<p>Install this Shadcn Time Picker with:</p>
<pre><code class="language-javascript">npx shadcn@latest add @shadcn-space/date-picker-03
</code></pre>
<p><strong>Component code:</strong></p>
<pre><code class="language-javascript">"use client";
import { useRef } from "react";
import { Label } from "@/components/ui/label";
import {
  InputGroup,
  InputGroupAddon,
  InputGroupInput,
} from "@/components/ui/input-group";
import { Clock8Icon } from "lucide-react";

const TimePickerWithIconDemo = () =&gt; {
  const inputRef = useRef&lt;HTMLInputElement&gt;(null);

  const handleShowPicker = () =&gt; {
    if (inputRef.current &amp;&amp; "showPicker" in inputRef.current) {
      try {
        inputRef.current.showPicker();
      } catch (error) {
        console.error("Failed to open native picker:", error);
      }
    }
  };

  return (
    &lt;div className="flex w-full max-w-xs flex-col gap-2"&gt;
      &lt;Label htmlFor="time-picker"&gt;Select Slot&lt;/Label&gt;
      &lt;InputGroup&gt;
        &lt;InputGroupAddon
          align="inline-start"
          className="cursor-pointer hover:text-foreground transition-colors"
          onClick={handleShowPicker}
          title="Open time picker"
        &gt;
          &lt;Clock8Icon className="size-4" /&gt;
        &lt;/InputGroupAddon&gt;
        &lt;InputGroupInput
          ref={inputRef}
          type="time"
          id="time-picker"
          step="1"
          defaultValue="08:30:00"
          className="appearance-none [&amp;::-webkit-calendar-picker-indicator]:hidden [&amp;::-webkit-calendar-picker-indicator]:appearance-none"
        /&gt;
      &lt;/InputGroup&gt;
    &lt;/div&gt;
  );
};
export default TimePickerWithIconDemo;
</code></pre>
<h3 id="heading-how-the-time-picker-works">How the Time Picker Works</h3>
<p>This component uses the browser's native time picker instead of building a custom dropdown.</p>
<p>The input is referenced with <code>useRef</code>:</p>
<pre><code class="language-javascript">const inputRef = useRef&lt;HTMLInputElement&gt;(null);
</code></pre>
<p>This allows the icon button to access the input element directly.</p>
<p>When users click the clock icon, the browser's picker opens programmatically:</p>
<pre><code class="language-javascript">inputRef.current.showPicker();
</code></pre>
<p>The <code>showPicker()</code> method is a modern browser API that opens the same interface users would see if they clicked the input manually.</p>
<p>The component wraps the input inside an <code>InputGroup</code>:</p>
<pre><code class="language-plaintext">&lt;InputGroup&gt;
</code></pre>
<p>This creates a cleaner layout where the icon behaves as part of the field rather than a separate button.</p>
<p>The browser's default picker icon is hidden:</p>
<pre><code class="language-plaintext">[&amp;::-webkit-calendar-picker-indicator]:hidden
</code></pre>
<p>This prevents duplicate icons and gives full control over the UI.</p>
<p>The benefit of this approach is that it keeps:</p>
<ul>
<li><p>Native accessibility</p>
</li>
<li><p>Mobile keyboard support</p>
</li>
<li><p>Locale-aware formatting</p>
</li>
<li><p>Better browser compatibility</p>
</li>
</ul>
<p>Instead of rebuilding time selection from scratch, the component improves the native experience with custom styling.</p>
<h2 id="heading-live-preview-of-the-components"><strong>Live Preview of the Components</strong></h2>
<img src="https://cdn.hashnode.com/uploads/covers/68b53a3d851476bd2ce87f12/f815455d-9f2d-4ad1-ac9c-155c37aae094.gif" alt="f815455d-9f2d-4ad1-ac9c-155c37aae094" style="display:block;margin:0 auto" width="1152" height="648" loading="lazy">

<h2 id="heading-key-concepts-recap"><strong>Key Concepts Recap</strong></h2>
<ul>
<li><p><strong>Pick the pattern that matches the data you're collecting</strong>: A single date and time for bookings, a range for stays, a bare time field for slots.</p>
</li>
<li><p><strong>Every component installs the same way</strong>: One CLI command per component: <code>pnpm</code>, <code>npm</code>, <code>yarn</code>, and <code>bun</code>. All are supported. Adding a new picker to a project takes one line, not a manual build.</p>
</li>
<li><p><strong>Th