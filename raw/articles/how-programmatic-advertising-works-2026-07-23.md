---
source_url: https://www.freecodecamp.org/news/how-programmatic-advertising-works/
ingested: 2026-07-23
sha256: e154cd8a99a80b5137ee3c52003d8bbb974c01a7af074531853dbddc9fff6a6f
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How Programmatic Advertising Works</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-programmatic-advertising-works/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="Most tutorials on programmatic advertising stop at the web banner. That&#39;s a shame, because the idea gets far more interesting once you follow it off the screen and into the physical world. If you&#39;ve n">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How Programmatic Advertising Works">
    
        <meta property="og:description" content="Most tutorials on programmatic advertising stop at the web banner. That&#39;s a shame, because the idea gets far more interesting once you follow it off the screen and into the physical world. If you&#39;ve n">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-programmatic-advertising-works/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/ead3788a-52c2-4821-b5c9-1c626c50d375.png">
    <meta property="article:published_time" content="2026-07-22T22:37:11.821Z">
    <meta property="article:modified_time" content="2026-07-22T22:37:11.821Z">
    
        <meta property="article:tag" content="Advertising">
    
        <meta property="article:tag" content="automation">
    
        <meta property="article:tag" content="Python">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How Programmatic Advertising Works">
    
        <meta name="twitter:description" content="Most tutorials on programmatic advertising stop at the web banner. That&#39;s a shame, because the idea gets far more interesting once you follow it off the screen and into the physical world. If you&#39;ve n">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-programmatic-advertising-works/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/ead3788a-52c2-4821-b5c9-1c626c50d375.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Manish Shivanandhan">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="Advertising, automation, Python">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/ead3788a-52c2-4821-b5c9-1c626c50d375.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-programmatic-advertising-works/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-22T22:37:11.821Z",
	"dateModified": "2026-07-22T22:37:11.821Z",
	"keywords": "Advertising, automation, Python",
	"description": "Most tutorials on programmatic advertising stop at the web banner. That&#x27;s a shame, because the idea gets far more interesting once you follow it off the screen and into the physical world.\nIf you&#x27;ve n",
	"headline": "How Programmatic Advertising Works",
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-22T22:37:11.821Z">
                            July 22, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/advertising/">
                                #Advertising
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How Programmatic Advertising Works</h1>
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
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/ead3788a-52c2-4821-b5c9-1c626c50d375.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/ead3788a-52c2-4821-b5c9-1c626c50d375.png" alt="How Programmatic Advertising Works" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>Most tutorials on <a href="https://advertising.amazon.com/blog/programmatic-advertising#1">programmatic advertising</a> stop at the web banner. That's a shame, because the idea gets far more interesting once you follow it off the screen and into the physical world.</p>
<p>If you've never worked in advertising, don't worry. You don't need any ad industry background to follow along. If you can read basic Python, you have everything you need.</p>
<p>The advertising part is just the setting. The real subject is a skill you'll use everywhere: taking a messy slice of the real world and turning it into data that software can act on.</p>
<p>In this article, you'll learn what programmatic advertising is and why it worked so well on the web. You'll see why bringing it to a billboard is really a data modeling problem, and you'll build small Python models for each step.</p>
<h3 id="heading-what-well-cover">What We'll Cover:</h3>
<ul>
<li><p><a href="#heading-what-is-programmatic-advertising">What Is Programmatic Advertising?</a></p>
</li>
<li><p><a href="#heading-why-the-web-made-programmatic-easy">Why the Web Made Programmatic Easy</a></p>
</li>
<li><p><a href="#heading-the-billboard-problem">The Billboard Problem</a></p>
</li>
<li><p><a href="#heading-step-1-resolve-entities">Step 1: Resolve Entities</a></p>
</li>
<li><p><a href="#heading-step-2-model-location-as-computed-context">Step 2: Model Location as Computed Context</a></p>
</li>
<li><p><a href="#heading-step-3-represent-availability-as-a-schedule-not-a-boolean">Step 3: Represent Availability as a Schedule, Not a Boolean</a></p>
</li>
<li><p><a href="#heading-step-4-express-price-as-a-function-not-a-number">Step 4: Express Price as a Function, Not a Number</a></p>
</li>
<li><p><a href="#heading-putting-it-together">Putting It Together</a></p>
</li>
<li><p><a href="#heading-an-exercise-to-build-the-intuition">An Exercise to Build the Intuition</a></p>
</li>
<li><p><a href="#heading-the-takeaway">The Takeaway</a></p>
</li>
</ul>
<h2 id="heading-what-is-programmatic-advertising">What Is Programmatic Advertising?</h2>
<p>Advertising has two sides. A publisher, such as a news site, has ad space to fill. And an advertiser, such as a shoe brand, wants to fill it. For decades, connecting the two meant phone calls, emails, and paperwork.</p>
<p>Programmatic advertising replaces that manual process with software. No human negotiates the placement. A system looks at an ad slot and decides, in milliseconds, whether to buy it and at what price.</p>
<p>Here's how it works when you open a web page. The page tells an ad exchange that a slot is open, along with some context about the page and the viewer. Advertisers' systems bid on the slot in a live auction. The winning ad appears before the page finishes loading. This process is called <a href="https://en.wikipedia.org/wiki/Real-time_bidding">real-time bidding</a>, and it happens billions of times a day.</p>
<p>Two quick terms will help. Inventory means the ad space a seller has to offer. An impression means one view of an ad by one person.</p>
<p>On the web, this model arrived fast and felt almost effortless. It's worth understanding why.</p>
<h2 id="heading-why-the-web-made-programmatic-easy">Why the Web Made Programmatic Easy</h2>
<p>The web made programmatic easy by accident. Every web ad slot came pre-structured. It had an address, meaning a URL and a position on the page. It sat inside a document with a known shape, the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model">Document Object Model</a>. And it could report back whether an ad had loaded and been seen.</p>
<p>The whole environment was machine-readable from birth, because machines were already serving it. When automated buying showed up, it had a clean surface to work against. The medium had already done the hard modeling work.</p>
<p>Keep that in mind. It's the key to the whole lesson.</p>
<h2 id="heading-the-billboard-problem">The Billboard Problem</h2>
<p>Now point the same idea at a billboard. None of that convenient structure exists.</p>
<p>A physical sign doesn't announce where it is or which way it faces. It doesn't say what it costs this week or whether it's even available. For most of its history, that information lived in rate cards and salespeople's memories, not in anything a program could query.</p>
<p>Here's the insight. Out-of-home advertising, the industry term for billboards, transit posters, and public screens, didn't lag the web because it was a weaker medium. It lagged because it had no machine-readable interface. The audience was always there. The structured data was not.</p>
<p>So the real work of bringing programmatic to the physical world isn't clever bidding logic. It's data modeling.</p>
<p>Let's make that concrete. There are four steps. Each one maps to a pattern you'll see in many other engineering problems.</p>
<h2 id="heading-step-1-resolve-entities">Step 1: Resolve Entities</h2>
<p>The same billboard often shows up in several vendors' datasets. Each vendor gives it a different name and slightly different coordinates. Before you can do anything else, one physical object has to become one record. This is known as <a href="https://en.wikipedia.org/wiki/Record_linkage">record linkage</a>, here with a geographic twist.</p>
<p>A simple approach: treat two records as the same panel if they sit close together and share a similar name. To measure the distance between two coordinates, you can use the <a href="https://en.wikipedia.org/wiki/Haversine_formula">haversine formula</a>.</p>
<pre><code class="language-python">from math import radians, sin, cos, asin, sqrt

def haversine_m(lat1, lon1, lat2, lon2):
    """Distance between two coordinates in meters."""
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    a = sin((lat2 - lat1) / 2) ** 2 + \
        cos(lat1) * cos(lat2) * sin((lon2 - lon1) / 2) ** 2
    return 6371000 * 2 * asin(sqrt(a))

def same_panel(a, b, max_distance_m=25):
    close = haversine_m(a["lat"], a["lon"], b["lat"], b["lon"]) &lt;= max_distance_m
    similar_name = a["name"].lower().split()[0] == b["name"].lower().split()[0]
    return close and similar_name

vendor_a = {"name": "I-95 North Bulletin", "lat": 25.7907, "lon": -80.1300}
vendor_b = {"name": "I-95 Bulletin #4421", "lat": 25.7908, "lon": -80.1301}

print(same_panel(vendor_a, vendor_b))  # True – one billboard, one record
</code></pre>
<p>Real systems use fuzzier matching and more signals, but the principle is the same. Entity resolution comes first, or every later step counts the same billboard twice.</p>
<h2 id="heading-step-2-model-location-as-computed-context">Step 2: Model Location as Computed Context</h2>
<p>A coordinate is not an audience. To make a panel useful to a buying system, you have to represent it as a point with an orientation. Then you estimate who actually passes it by joining it against road and traffic data.</p>
<p>The useful value is computed, not given:</p>
<pre><code class="language-python">def estimate_impressions(panel, traffic_by_road):
    """Estimate daily impressions from road traffic data."""
    daily_vehicles = traffic_by_road[panel["road_id"]]
    # Only traffic moving toward the panel's face can see it
    facing_share = 0.5
    avg_occupancy = 1.4  # people per vehicle
    return int(daily_vehicles * facing_share * avg_occupancy)

panel = {"id": "P-4421", "road_id": "I-95-N", "facing": "south"}
traffic = {"I-95-N": 120000}

print(estimate_impressions(panel, traffic))  # 84000
</code></pre>
<p>Notice what happened. The raw record was just a point on a map. It got enriched into something a buyer can reason about: 84,000 estimated daily impressions. This pattern shows up everywhere in data work. A raw record plus outside data equals a useful field.</p>
<h2 id="heading-step-3-represent-availability-as-a-schedule-not-a-boolean">Step 3: Represent Availability as a Schedule, Not a Boolean</h2>
<p>A web ad slot is either open right now or it isn't. In code, that's a boolean: a value that is simply true or false. A billboard gets booked in date ranges, and its state changes underneath you. Inventory gets held, booked, and released. You need live data, not a snapshot.</p>
<pre><code class="language-python">from datetime import date

class PanelSchedule:
    def __init__(self):
        self.bookings = []  # list of (start, end) tuples

    def book(self, start, end):
        if not self.is_available(start, end):
            raise ValueError("Panel not available for that range")
        self.bookings.append((start, end))

    def is_available(self, start, end):
        return all(end &lt; b_start or start &gt; b_end
                   for b_start, b_end in self.bookings)

schedule = PanelSchedule()
schedule.book(date(2026, 8, 1), date(2026, 8, 14))

print(schedule.is_available(date(2026, 8, 10), date(2026, 8, 20)))  # False
print(schedule.is_available(date(2026, 8, 15), date(2026, 8, 31)))  # True
</code></pre>
<p>The lesson carries over. Whenever you model the real world, ask whether a value is truly fixed. Often it's state that changes over time. Availability, stock levels, and seat maps are all schedules pretending to be booleans.</p>
<h2 id="heading-step-4-express-price-as-a-function-not-a-number">Step 4: Express Price as a Function, Not a Number</h2>
<p>The rate card says one number. Reality prices by date, demand, and how much inventory is left:</p>
<pre><code class="language-python">def price_for(base_rate, start, weeks_out, occupancy):
    """Price a booking based on lead time and demand."""
    demand_multiplier = 1 + occupancy          # busier market, higher price
    urgency_discount = 0.9 if weeks_out &gt; 8 else 1.0  # reward early booking
    return round(base_rate * demand_multiplier * urgency_discount, 2)

print(price_for(base_rate=3000, start=date(2026, 12, 1),
                weeks_out=19, occupancy=0.85))  # 4995.0
print(price_for(base_rate=3000, start=date(2026, 8, 1),
                weeks_out=2, occupancy=0.40))   # 4200.0
</code></pre>
<p>Once price is a function, software can compare thousands of panels and dates instantly. That's exactly what automated buying needs.</p>
<h2 id="heading-putting-it-together">Putting It Together</h2>
<p>You now have resolved entities, computed audience, live availability, and dynamic pricing. With that in place, <a href="https://www.adquick.com/guides/programmatic-dooh">programmatic digital out of home</a> advertising works in the physical world the same way it does online. Software can plan a campaign across physical screens, buy them automatically, adjust in near real time, and measure the result.</p>
<p>It was never really about the web. It was about whether the inventory had a schema, meaning a defined structure that tells software what each piece of data is. Once you give the physical world a schema, the automation follows.</p>
<h2 id="heading-an-exercise-to-build-the-intuition">An Exercise to Build the Intuition</h2>
<p>You don't need special access to practice this. Take any messy, location-based public dataset and rehearse the four steps. A good source is <a href="https://www.openstreetmap.org/">OpenStreetMap</a>, which offers free data on millions of real-world places.</p>
<p>First, resolve duplicates by merging records that describe the same real-world thing. Second, enrich each point with computed context instead of treating the raw record as complete. Third, model one field as state that changes over time rather than a fixed value. Fourth, wrap the result in a clean interface, such as a class or a small API, that something else could query.</p>
<p>You won't have built an ad platform, but you'll have practiced the exact skills that let automated buying reach a new field.</p>
<h2 id="heading-the-takeaway">The Takeaway</h2>
<p>A good abstraction survives contact with the real world.</p>
<p>When you first learn a concept in a tidy setting, it's easy to think the tidiness is part of the concept. It rarely is. You only find out how general an idea is when you drag it somewhere messy and watch it still work.</p>
<p>Programmatic buying, moved off the screen and onto a wall by a road, is one of the cleaner proofs of that. Keep an eye out for the same pattern elsewhere: a rich domain waiting on nothing but a schema.</p>
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


    
    <script>document.addEventListener("DOMContentLoaded",()=>{const t=document.getElementById("tweet-btn"),n=window.location,e="How%20Programmatic%20Advertising%20Works".replace(/&#39;/g,"%27"),o="",i="@@manishmshiva",r=Boolean("");let a;if(r&&(o||i)){const t={originalPostAuthor:"",currentPostAuthor:"Manish Shivanandhan"};a=encodeURIComponent(`Thank you ${o||t.originalPostAuthor} for writing this helpful article, and ${i||t.currentPostAuthor} for translating it.`)}else!r&&i&&(a=encodeURIComponent(`Thank you ${i} for writing this helpful article.`));const s=`window.open(\n    '${a?`https://x.com/intent/post?text=${a}%0A%0A${e}%0A%0A${n}`:`https://x.com/intent/post?text=${e}%0A%0A${n}`}',\n    'share-twitter',\n    'width=550, height=235'\n  ); return false;`;t.setAttribute("onclick",s)});</script>


                        

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
                    </a>
                </li>
                <li>
                    <a href="https://www.freecodecamp.org/news/learn-linux-for-beginners-book-basic-to-advanced/" rel="noopener noreferrer" target="_blank">Linux
                    </a>
                </li>
                <li>
                    <a href="https://www.freecodecamp.org/news/react-for-beginners-handbook/" rel="noopener noreferrer" target="_blank">React
                    </a>
                </li>
                <li>
      