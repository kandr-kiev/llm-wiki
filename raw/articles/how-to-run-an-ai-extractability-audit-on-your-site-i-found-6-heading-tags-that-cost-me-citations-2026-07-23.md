---
source_url: https://www.freecodecamp.org/news/how-to-run-an-ai-extractability-audit/
ingested: 2026-07-23
sha256: ca44181de358d599ad95236cc4d2ca4ea9b6ef413238bca9d8064c351988d52a
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Run an AI Extractability Audit on Your Site (I Found 6 Heading Tags That Cost Me Citations)</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-to-run-an-ai-extractability-audit/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="When an AI assistant answers a question, it lifts sentences from a handful of pages and cites them. Whether your page is liftable is not a mystery or a vibe. It&#39;s a set of mechanical properties of you">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Run an AI Extractability Audit on Your Site (I Found 6 Heading Tags That Cost Me Citations)">
    
        <meta property="og:description" content="When an AI assistant answers a question, it lifts sentences from a handful of pages and cites them. Whether your page is liftable is not a mystery or a vibe. It&#39;s a set of mechanical properties of you">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-to-run-an-ai-extractability-audit/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/9c86b8bb-fdda-4f95-9175-623de49c584c.png">
    <meta property="article:published_time" content="2026-07-22T23:16:07.709Z">
    <meta property="article:modified_time" content="2026-07-22T23:16:07.709Z">
    
        <meta property="article:tag" content="SEO">
    
        <meta property="article:tag" content="Artificial Intelligence">
    
        <meta property="article:tag" content="Web Development">
    
        <meta property="article:tag" content="Python">
    
        <meta property="article:tag" content="web scraping">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Run an AI Extractability Audit on Your Site (I Found 6 Heading Tags That Cost Me Citations)">
    
        <meta name="twitter:description" content="When an AI assistant answers a question, it lifts sentences from a handful of pages and cites them. Whether your page is liftable is not a mystery or a vibe. It&#39;s a set of mechanical properties of you">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-to-run-an-ai-extractability-audit/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/9c86b8bb-fdda-4f95-9175-623de49c584c.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Chudi Nnorukam">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="SEO, Artificial Intelligence, Web Development, Python, web scraping">
    <meta name="twitter:site" content="@freecodecamp">
    
        <meta name="twitter:creator" content="@chudinnorukam">
    

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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/9c86b8bb-fdda-4f95-9175-623de49c584c.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-to-run-an-ai-extractability-audit/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-22T23:16:07.709Z",
	"dateModified": "2026-07-22T23:16:07.709Z",
	"keywords": "SEO, Artificial Intelligence, Web Development, Python, web scraping",
	"description": "When an AI assistant answers a question, it lifts sentences from a handful of pages and cites them. Whether your page is liftable is not a mystery or a vibe. It&#x27;s a set of mechanical properties of you",
	"headline": "How to Run an AI Extractability Audit on Your Site (I Found 6 Heading Tags That Cost Me Citations)",
	"author": {
		"@type": "Person",
		"name": "Chudi Nnorukam",
		"url": "https://www.freecodecamp.org/news/author/chudinnorukam/",
		"sameAs": [
			"https://chudi.dev",
			"https://x.com/chudinnorukam"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/uploads/avatars/69d995ffc8e5007ddb1e81bb/457cd6e3-cc78-47d3-a70f-a1d2b20042fa.png",
			"width": 1254,
			"height": 1254
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-22T23:16:07.709Z">
                            July 22, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/seo/">
                                #SEO
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Run an AI Extractability Audit on Your Site (I Found 6 Heading Tags That Cost Me Citations)</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/uploads/avatars/69d995ffc8e5007ddb1e81bb/457cd6e3-cc78-47d3-a70f-a1d2b20042fa.png 60w" sizes="60px" src="https://cdn.hashnode.com/uploads/avatars/69d995ffc8e5007ddb1e81bb/457cd6e3-cc78-47d3-a70f-a1d2b20042fa.png" class="author-profile-image" alt="Chudi Nnorukam" width="1254" height="1254" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/chudinnorukam/" data-test-label="profile-link">
                    
                        Chudi Nnorukam
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/9c86b8bb-fdda-4f95-9175-623de49c584c.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/9c86b8bb-fdda-4f95-9175-623de49c584c.png" alt="How to Run an AI Extractability Audit on Your Site (I Found 6 Heading Tags That Cost Me Citations)" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>When an AI assistant answers a question, it lifts sentences from a handful of pages and cites them. Whether your page is liftable is not a mystery or a vibe. It's a set of mechanical properties of your HTML that you can measure, score, and fix.</p>
<p>This tutorial walks through the exact audit I ran on my own site, the six invisible heading tags it caught, the one-commit fix, and the CI gate that keeps the problem from coming back.</p>
<p>Here is the punchline up front: my homepage scored 65 out of 100 on extractability. The cause was five UI card components that rendered their titles as <code>&lt;h2&gt;</code> and <code>&lt;h3&gt;</code> tags. Demoting those six headings to ARIA-preserving paragraphs, without changing a single visible pixel or removing one word of content, took the page to 100.</p>
<p>Over the last 90 days, Microsoft's Bing Webmaster Tools reports 1,600 AI citations across 33 of my pages. Extraction is the stage of that pipeline this tutorial teaches you to audit.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-what-an-extractability-audit-actually-tests">What an Extractability Audit Actually Tests</a></p>
</li>
<li><p><a href="#heading-prerequisites">Prerequisites</a></p>
</li>
<li><p><a href="#heading-step-1-pick-the-pages-worth-auditing">Step 1: Pick the Pages Worth Auditing</a></p>
</li>
<li><p><a href="#heading-step-2-run-the-five-checks">Step 2: Run the Five Checks</a></p>
</li>
<li><p><a href="#heading-step-3-read-your-failure-classes">Step 3: Read Your Failure Classes</a></p>
</li>
<li><p><a href="#heading-step-4-find-the-components-emitting-fake-headings">Step 4: Find the Components Emitting Fake Headings</a></p>
</li>
<li><p><a href="#heading-step-5-demote-the-headings-without-breaking-accessibility">Step 5: Demote the Headings Without Breaking Accessibility</a></p>
</li>
<li><p><a href="#heading-step-6-gate-the-fix-in-ci">Step 6: Gate the Fix in CI</a></p>
</li>
<li><p><a href="#heading-what-actually-moved">What Actually Moved</a></p>
</li>
<li><p><a href="#heading-what-i-rejected-and-why">What I Rejected, and Why</a></p>
</li>
<li><p><a href="#heading-faq">FAQ</a></p>
</li>
<li><p><a href="#heading-what-you-accomplished">What You Accomplished</a></p>
</li>
</ul>
<h2 id="heading-what-an-extractability-audit-actually-tests">What an Extractability Audit Actually Tests</h2>
<p>A citation from an AI engine is the last step of a three-stage machine pipeline, and your page has to pass every stage:</p>
<ol>
<li><p><strong>Retrieve</strong>: the engine's crawler is allowed to fetch your page, and does.</p>
</li>
<li><p><strong>Extract</strong>: the model finds a clean, self-contained answer in your markup.</p>
</li>
<li><p><strong>Attribute</strong>: the engine is confident enough about who said it to put your name next to it.</p>
</li>
</ol>
<img src="https://cdn.hashnode.com/uploads/covers/69d995ffc8e5007ddb1e81bb/793015f2-359e-497a-b18b-4238999aa83e.png" alt="Three-stage pipeline diagram labeled Retrieve, Extract, Attribute, showing that an AI engine must fetch a page, lift a clean answer from its markup, and identify the author before a citation appears." style="display:block;margin:0 auto" width="1600" height="1000" loading="lazy">

<p>Most AI-visibility advice concentrates on stage 1 (robots.txt, sitemaps, llms.txt) and stage 3 (schema, entity signals). Stage 2 is where I've found the cheapest wins, because it's pure HTML engineering, and because it fails silently: a page that retrieves fine and attributes fine but extracts poorly simply never appears in answers, and nothing tells you why.</p>
<p><strong>Extractability</strong> is the measurable version of stage 2: can a parser walking your rendered HTML find self-contained answer blocks under clearly scoped headings? The audit in this tutorial scores that on a 0 to 100 scale using five checks, each of which you can verify by hand:</p>
<table>
<thead>
<tr>
<th>Check</th>
<th>What it tests</th>
<th>Weight</th>
</tr>
</thead>
<tbody><tr>
<td>F1</td>
<td>The first sentence under every H2 stands alone as an answer</td>
<td>30</td>
</tr>
<tr>
<td>F2</td>
<td>The first 200 tokens of the page contain a direct answer</td>
<td>20</td>
</tr>
<tr>
<td>F3</td>
<td>Each H2 section opens with an answer in the 40 to 60 word band</td>
<td>20</td>
</tr>
<tr>
<td>F4</td>
<td>Share of H2/H3 headings phrased as questions a user would type</td>
<td>20</td>
</tr>
<tr>
<td>F5</td>
<td>An FAQ section exists at the article footer</td>
<td>10</td>
</tr>
</tbody></table>
<p>A score of 75 or above lands in the EXTRACTABLE band. 40 to 74 is PARTIALLY-EXTRACTABLE. Below 40 is NOT-EXTRACTABLE. The bands come from the AI Visibility Readiness framework I maintain, but the five checks themselves are engine-agnostic: they encode how retrieval-augmented systems chunk pages by heading, embed the chunks, and lift the opening sentences of whichever chunk matches the query.</p>
<p>The critical detail for this tutorial: <strong>the audit counts every</strong> <code>&lt;h1&gt;</code><strong>,</strong> <code>&lt;h2&gt;</code><strong>, and</strong> <code>&lt;h3&gt;</code> <strong>in your rendered DOM.</strong> Not the headings you wrote in your CMS. The headings your component library emits. That gap is where my six invisible failures lived.</p>
<h2 id="heading-prerequisites">Prerequisites</h2>
<ul>
<li><p>A live website you can measure and deploy (Any stack. My examples are SvelteKit, and every fix translates to React, Vue, or plain HTML.)</p>
</li>
<li><p>Python 3.10+ with <code>requests</code> and <code>beautifulsoup4</code> (<code>pip install requests beautifulsoup4</code>)</p>
</li>
<li><p>Access to your search console data (Google Search Console or Bing Webmaster Tools) to pick pages</p>
</li>
<li><p>A CI system (the example uses GitHub Actions)</p>
</li>
<li><p>About 90 minutes: 20 for the audit, 40 for the fix, 30 for the CI gate</p>
</li>
</ul>
<h2 id="heading-step-1-pick-the-pages-worth-auditing">Step 1: Pick the Pages Worth Auditing</h2>
<p>Don't audit your whole sitemap. Audit the pages that already have distribution, because extraction fixes multiply whatever retrieval you already earn.</p>
<p>Open Google Search Console, go to Performance, sort pages by impressions over the last 28 days, and look at where your distribution actually lives.</p>
<p>Here's the top of my own report from that export (July 21):</p>
<table>
<thead>
<tr>
<th>Page</th>
<th>Impressions (28d)</th>
<th>Clicks</th>
<th>Avg position</th>
</tr>
</thead>
<tbody><tr>
<td>/blog/claude-fable-5-vs-opus-4-8</td>
<td>17,315</td>
<td>462</td>
<td>6.2</td>
</tr>
<tr>
<td>/blog/how-i-built-polymarket-trading-bot</td>
<td>13,649</td>
<td>104</td>
<td>7.6</td>
</tr>
<tr>
<td>/blog/claude-code-production-trading-bot</td>
<td>6,540</td>
<td>94</td>
<td>8.5</td>
</tr>
<tr>
<td>/blog/aeo-answer-engine-optimization-explained</td>
<td>4,189</td>
<td>1</td>
<td>8.2</td>
</tr>
</tbody></table>
<p>Individual posts dominate the impressions, but notice what every one of those posts has in common: they're all rendered by the same layout and card components.</p>
<p>Fixing a component fixes every page that uses it at once, which is why I scoped the audit to the top 3 to 5 <strong>content-index pages</strong> instead of individual posts: the homepage, your blog index, your topic or category hubs.</p>
<p>Index pages are assembled almost entirely from repeating cards, so they show component damage in its most concentrated form, and any fix propagates to everything else.</p>
<p>I chose these three:</p>
<ul>
<li><p><code>chudi.dev/</code> (the homepage)</p>
</li>
<li><p><code>chudi.dev/blog</code> (the writing index)</p>
</li>
<li><p><code>chudi.dev/topics</code> (the topic hub)</p>
</li>
</ul>
<p><strong>Artifact check:</strong> you should now have a written list of 3 to 5 URLs. That list is the audit's scope.</p>
<h2 id="heading-step-2-run-the-five-checks">Step 2: Run the Five Checks</h2>
<p>You can score the five checks with about 60 lines of Python. This is a deliberately minimal version of the auditor I run in production. It implements the two checks that catch component damage (F3 and F4) plus a full heading census, which is enough to find the class of bug this tutorial fixes.</p>
<pre><code class="language-python">import re
import sys
import requests
from bs4 import BeautifulSoup

QUESTION = re.compile(
    r"^\s*(what|how|why|when|where|who|which|is|are|can|do|does|should|will|did)\b|\?\s*$",
    re.IGNORECASE,
)

def audit(url):
    html = requests.get(url, timeout=8, headers={"User-Agent": "extract-audit/1.0"}).text
    soup = BeautifulSoup(html, "html.parser")

    headings = [(h.name, " ".join(h.get_text().split())) for h in soup.find_all(["h1", "h2", "h3"])]
    subheads = [(n, t) for n, t in headings if n in ("h2", "h3")]

    question_rate = (
        sum(1 for _, t in subheads if QUESTION.search(t)) / len(subheads) if subheads else 0.0
    )

    in_band = 0
    h2s = soup.find_all("h2")
    for h2 in h2s:
        first_p = h2.find_next("p")
        words = len(first_p.get_text().split()) if first_p else 0
        if 40 &lt;= words &lt;= 60:
            in_band += 1

    print(f"URL: {url}")
    print(f"Heading census ({len(headings)} total):")
    for name, text in headings:
        print(f"  &lt;{name}&gt; {text[:70]}")
    print(f"F4 question-format rate: {question_rate:.1%} (target &gt;= 50%)")
    print(f"F3 sections opening in the 40-60 word band: {in_band}/{len(h2s)}")

if __name__ == "__main__":
    audit(sys.argv[1])
</code></pre>
<p>Run it against each page on your list:</p>
<pre><code class="language-bash">python3 extract_audit.py https://yoursite.com/
</code></pre>
<p>The heading census is the part to stare at. It prints every H1/H2/H3 a parser sees, in order, which is frequently not the outline you think you published.</p>
<p>If you want the full five-check scored version with the weighted 0 to 100 composite, the <a href="https://citability.dev">automated audit on citability.dev</a> runs all five checks plus retrieval and attribution layers. The manual version above is enough to complete this tutorial.</p>
<p><strong>Artifact check:</strong> a terminal output per page showing the heading census, the F4 rate, and the F3 band count. Screenshot it. It is your before-state.</p>
<h2 id="heading-step-3-read-your-failure-classes">Step 3: Read Your Failure Classes</h2>
<p>Here's what the audit said about my homepage before the fix, pulled from the commit record of the remediation (2026-05-23):</p>
<ul>
<li><p>Score: <strong>65/100, PARTIALLY-EXTRACTABLE</strong>, ten points under the threshold</p>
</li>
<li><p>F4 question-format rate: <strong>26.7%</strong>, far below the 50% pass line</p>
</li>
<li><p>Cause: more than ten headings in the census that I never wrote as headings</p>
</li>
</ul>
<p>The census made the cause obvious. Alongside the section headings I had deliberately tuned ("How do I see it run live?", "What is the retrieval header?") sat a pile of statements like blog post titles and project names, each wrapped in <code>&lt;h2&gt;</code> or <code>&lt;h3&gt;</code>. I hadn't typed a single one of them into a heading field. My card components had.</p>
<p>This is the general lesson, and it is worth stating as a rule:</p>
<p><strong>The denominator is the design problem.</strong> Every heading your components emit joins the denominator of every ratio check an extraction parser runs. Ten card titles as H3s means your carefully tuned question headings are outvoted 10 to 4 by markup you never see.</p>
<p>Failure classes map to fixes like this:</p>
<table>
<thead>
<tr>
<th>Symptom in the census</th>
<th>Failure class</th>
<th>Fix (Step)</th>
</tr>
</thead>
<tbody><tr>
<td>Headings you never wrote, repeated in card-sized clusters</td>
<td>Component-emitted headings</td>
<td>Steps 4 and 5</td>
</tr>
<tr>
<td>Your own H2s are statements, not questions</td>
<td>Authored heading style</td>
<td>Rephrase to question form</td>
</tr>
<tr>
<td>Sections open with a 15-word teaser or a 120-word ramble</td>
<td>Answer-band miss</td>
<td>Densify openers to 40 to 60 words</td>
</tr>
<tr>
<td>No FAQ block</td>
<td>Missing F5 surface</td>
<td>Add one at the footer</td>
</tr>
</tbody></table>
<p>I had all four classes across my three pages. The component class was the biggest single scorer, and it's the one nobody catches by reading their CMS, so it gets the deep treatment here. (For the record, the authored fixes on my other pages were exactly what the table says: two H2s on my framework page rephrased into question form, and a topic-hub opener expanded from 37 words to roughly 50 to enter the answer band.)</p>
<p><strong>Artifact check:</strong> your census annotated with the four failure classes. Count how many headings you didn't author.</p>
<h2 id="heading-step-4-find-the-components-emitting-fake-headings">Step 4: Find the Components Emitting Fake Headings</h2>
<p>The census tells you fake headings exist. Your component library tells you where they come from. Grep for heading tags inside your component directory, not your content:</p>
<pre><code class="language-bash">grep -rn "&lt;h[23]" src/lib/components/ --include="*.svelte"
</code></pre>
<p>(React: <code>grep -rn "&lt;h[23]" src/components/ --include="*.tsx"</code>. Vue: same idea with <code>.vue</code>.)</p>
<p>On my site, this surfaced six heading sites across five components:</p>
<table>
<thead>
<tr>
<th>Component</th>
<th>Emitted</th>
<th>Instances</th>
</tr>
</thead>
<tbody><tr>
<td><code>BlogCard.svelte</code></td>
<td><code>&lt;h3&gt;</code> post title</td>
<td>2</td>
</tr>
<tr>
<td><code>BlogCardFeatured.svelte</code></td>
<td><code>&lt;h2&gt;</code> post title</td>
<td>1</td>
</tr>
<tr>
<td><code>ProductCard.svelte</code></td>
<td><code>&lt;h3&gt;</code> product name</td>
<td>1</td>
</tr>
<tr>
<td><code>ProjectCard.svelte</code></td>
<td><code>&lt;h2&gt;</code> project name</td>
<td>1</td>
</tr>
<tr>
<td><code>JourneyCard.svelte</code></td>
<td><code>&lt;h2&gt;</code> milestone title</td>
<td>1</td>
</tr>
</tbody></table>
<p>Six tags doesn't sound like much until you remember that cards repeat. One blog index rendering ten <code>BlogCard</code> instances injects ten <code>&lt;h3&gt;</code> statements into that page's census. Every card-built page on the site inherits the same dilution, which is exactly why my content-index pages scored worst.</p>
<p>Why do component libraries do this? Because a card title <em>looks</em> like a heading, and because accessibility guidance rightly encourages semantic HTML.</p>
<p>The mistake is subtler: a card title is a <strong>link label into another document</strong>, not a section heading of <strong>this</strong> document. The page's real outline is "here are my featured posts", not the title of each post teased below it. HTML has no tag for "title of a different page", so components default to H2/H3, and every parser that walks the page inherits a false outline.</p>
<p><strong>Artifact check:</strong> a table like the one above: component, tag emitted, instance count. This is your fix list.</p>
<h2 id="heading-step-5-demote-the-headings-without-breaking-accessibility">Step 5: Demote the Headings Without Breaking Accessibility</h2>
<p>The obvious fix, swapping <code>&lt;h3&gt;</code> for a styled <code>&lt;span&gt;</code> or <code>&lt;p&gt;</code>, has a real cost: screen reader users navigate by heading structure, and card titles are genuinely useful landmarks when scanning a list of posts. Deleting the semantics entirely trades an AI-extraction win for an accessibility loss. That trade isn't necessary.</p>
<p>The fix that preserves both is <strong>ARIA heading demotion</strong>: replace the literal tag with a paragraph carrying <code>role="heading"</code> and an explicit <code>aria-level</code>.</p>
<p>One important clarification before the diff: the first rule of ARIA is to prefer native HTML elements, and this fix doesn't violate it. The rule applies when the text genuinely is a heading of the current document, and the whole point of Step 4 was establishing that card titles are not. They are link labels into other documents.</p>
<p>Native <code>&lt;h3&gt;</code> was the wrong semantics, while the ARIA role is a courtesy that keeps the list-scanning navigation screen reader users already rely on.</p>
<p>Here's the actual diff from my <code>BlogCard.svelte</code>, unchanged except for wrapping:</p>
<pre><code class="language-diff">-&lt;h3 class="text-[20px] md:text-[22px] font-bold leading-snug
+&lt;p role="heading" aria-level="3" class="text-[20px] md:text-[22px] font-bold leading-snug
   text-[var(--color-text-primary)]
   group-hover:text-[var(--color-primary)]
   transition-colors line-clamp-2"&gt;
   {post.title}
-&lt;/h3&gt;
+&lt;/p&gt;
</code></pre>
<p>What changes and what does not:</p>
<ul>
<li><p><strong>Assistive technology sees the same outline.</strong> <code>role="heading"</code> plus <code>aria-level="3"</code> is the ARIA-standard equivalent of an <code>&lt;h3&gt;</code>. Screen readers that navigate by heading still stop here and still announce the level.</p>
</li>
<li><p><strong>Visual styling is untouched.</strong> Every class stays on the element. Zero pixels move.</p>
</li>
<li><p><strong>Content is untouched.</strong> The fix removes zero words. This matters because most extraction advice tells you to rewrite. But this class of bug needs no rewriting.</p>
</li>
<li><p><strong>HTML-tag parsers stop counting it.</strong> Extraction pipelines chunk by literal <code>h1</code>/<code>h2</code>/<code>h3</code> elements. The card title exits the census, your authored headings get the denominator back, and the ratios you tuned start passing.</p>
</li>
</ul>
<p>Apply the same one-line change at every site on your Step 4 fix list. Mine was one commit touching five components, six occurrences.</p>
<p>Then redeploy and re-run the Step 2 audit. My homepage went from 65 to <strong>100/100 EXTRACTABLE</strong> on the post-deploy re-score, with the question-format rate recovering from 26.7% to above the 50% threshold, because the four question headings I had authored were finally the only H2/H3 population on the page.</p>
<p><strong>Artifact check:</strong> the after-audit terminal output next to your before screenshot. The heading census should now contain only headings you wrote on purpose.</p>
<h2 id="heading-step-6-gate-the-fix-in-ci">Step 6: Gate the Fix in CI</h2>
<p>Here's the uncomfortable truth about extraction scores: they drift. Content changes, components get added, or a redesign ships a new card.</p>
<p>My homepage, re-audited live while writing this tutorial (July 21), sits at 80: still EXTRACTABLE, but down from its post-fix 100, because a homepage redesign in the intervening weeks changed the section structure again. The blog index and topic hub both still score 100.</p>
<p>That drift is why the durable deliverable of this tutorial isn't the fix. It's the regression gate. Without one, the next well-meaning component ships a new <code>&lt;h2&gt;</code> and your score quietly decays. Nothing visible breaks, so nothing gets caught in review.</p>
<p>Mine runs as a GitHub Actions workflow triggered by every successful production deployment, and hard-fails if any audited URL drops out of the EXTRACTABLE band:</p>
<pre><code class="language-yaml">name: Post-Deploy Extractability Audit

on:
  deployment_status:

jobs:
  audit:
    if: |
      github.event.deployment_status.state == 'success' &amp;&amp;
      github.event.deployment.environment == 'Production'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.13"
      - run: pip install requests beautifulsoup4
      - name: Audit extractability on the live URLs
        run: |
          for url in "https://yoursite.com/" "https://yoursite.com/blog"; do
            python3 scripts/extract_audit.py "$url" --min-score 75 || exit 1
          done
</code></pre>
<p>To make the minimal auditor CI-ready, add a <code>--min-score</code> flag that exits nonzero below the threshold. That's a five-line change to the Step 2 script (compute the weighted score from the checks you implement, compare, <code>sys.exit(1)</code>).</p>
<p>The production version of my gate audits 