---
source_url: https://www.freecodecamp.org/news/harness-engineering-ai-native-company/
ingested: 2026-07-17
sha256: d4d8d1124b468d3edcef4a99b4e480ffdf6e24bb5d293fd1b0ce2a56425075ad
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How I Used Harness Engineering to Make Our Company AI-Native</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/harness-engineering-ai-native-company/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="Most companies say they want to &quot;adopt AI&quot;. In practice this usually means a chatbot bolted onto a website. Meanwhile, engineers using AI coding tools hit the opposite wall. The AI writes code fast, b">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How I Used Harness Engineering to Make Our Company AI-Native">
    
        <meta property="og:description" content="Most companies say they want to &quot;adopt AI&quot;. In practice this usually means a chatbot bolted onto a website. Meanwhile, engineers using AI coding tools hit the opposite wall. The AI writes code fast, b">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/harness-engineering-ai-native-company/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/0438e6d7-d727-480d-8517-a87c12350326.png">
    <meta property="article:published_time" content="2026-07-15T15:34:41.654Z">
    <meta property="article:modified_time" content="2026-07-15T15:34:41.654Z">
    
        <meta property="article:tag" content="AI">
    
        <meta property="article:tag" content="mcp">
    
        <meta property="article:tag" content="Software Engineering">
    
        <meta property="article:tag" content="documentation">
    
        <meta property="article:tag" content="harnessengineering">
    
        <meta property="article:tag" content="claude">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How I Used Harness Engineering to Make Our Company AI-Native">
    
        <meta name="twitter:description" content="Most companies say they want to &quot;adopt AI&quot;. In practice this usually means a chatbot bolted onto a website. Meanwhile, engineers using AI coding tools hit the opposite wall. The AI writes code fast, b">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/harness-engineering-ai-native-company/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/0438e6d7-d727-480d-8517-a87c12350326.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Tech With RJ">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="AI, mcp, Software Engineering, documentation, harnessengineering, claude">
    <meta name="twitter:site" content="@freecodecamp">
    
        <meta name="twitter:creator" content="@TechWithRJ2">
    

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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/0438e6d7-d727-480d-8517-a87c12350326.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/harness-engineering-ai-native-company/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-15T15:34:41.654Z",
	"dateModified": "2026-07-15T15:34:41.654Z",
	"keywords": "AI, mcp, Software Engineering, documentation, harnessengineering, claude",
	"description": "Most companies say they want to &quot;adopt AI&quot;. In practice this usually means a chatbot bolted onto a website.\nMeanwhile, engineers using AI coding tools hit the opposite wall. The AI writes code fast, b",
	"headline": "How I Used Harness Engineering to Make Our Company AI-Native",
	"author": {
		"@type": "Person",
		"name": "Tech With RJ",
		"url": "https://www.freecodecamp.org/news/author/LeeRenJie/",
		"sameAs": [
			"rjcodes.dev",
			"https://x.com/TechWithRJ2"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/res/hashnode/image/upload/v1616217217557/YR85oIZgJ.jpeg",
			"width": 512,
			"height": 512
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-15T15:34:41.654Z">
                            July 15, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/ai/">
                                #AI
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How I Used Harness Engineering to Make Our Company AI-Native</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/res/hashnode/image/upload/v1616217217557/YR85oIZgJ.jpeg 60w" sizes="60px" src="https://cdn.hashnode.com/res/hashnode/image/upload/v1616217217557/YR85oIZgJ.jpeg" class="author-profile-image" alt="Tech With RJ" width="512" height="512" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/LeeRenJie/" data-test-label="profile-link">
                    
                        Tech With RJ
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/0438e6d7-d727-480d-8517-a87c12350326.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/0438e6d7-d727-480d-8517-a87c12350326.png" alt="How I Used Harness Engineering to Make Our Company AI-Native" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>Most companies say they want to "adopt AI". In practice this usually means a chatbot bolted onto a website.</p>
<p>Meanwhile, engineers using AI coding tools hit the opposite wall. The AI writes code fast, but nobody fully trusts the output, so someone reviews every line and the speed evaporates.</p>
<p>Both problems have the same root. The AI has no structure around it. No checks it must pass, and no access to the data your company actually runs on. Building that structure is a discipline called harness engineering, and it's what this article teaches you.</p>
<p>I'm a full-stack engineer who builds lending systems. Our documentation kept drifting away from the code, so I set out to fix it with Claude Code. What made it work in the end wasn't a smarter model like Fable or Opus. It was structure and guardrails.</p>
<p>In 30 days, I built V1 of an internal documentation platform where most of the code was written by the agent, kept safe by a set of automatic checks. Then I gave the platform a Model Context Protocol (MCP) server, so AI agents could read and write company docs with the same permissions as the person running them.</p>
<p>After rounds of improvement and tweaks, by day 50, the company adopted it. Requirement gathering, development work, and documentation all flow through the platform as one source of truth, in production, for a new project.</p>
<p>This article acts as the playbook, not a product tour. I won't go through all the features I built. I'll walk through the mindset and how it led to this outcome.</p>
<p><strong>What you'll find below:</strong></p>
<ul>
<li><p>What harness engineering means, in plain terms</p>
</li>
<li><p>The four gates that let an AI agent write most of a production system</p>
</li>
<li><p>What an MCP server is and why it matters more than the chatbot</p>
</li>
<li><p>Why "you can only improve what you track" is the core idea behind an AI-native company</p>
</li>
<li><p>How to start with one process in your own company</p>
</li>
</ul>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-what-harness-engineering-means">What Harness Engineering Means</a></p>
</li>
<li><p><a href="#heading-pointing-it-at-a-real-problem">Pointing It at a Real Problem</a></p>
</li>
<li><p><a href="#heading-the-four-gates">The Four Gates</a></p>
</li>
<li><p><a href="#heading-where-the-harness-failed">Where the Harness Failed</a></p>
</li>
<li><p><a href="#heading-what-an-mcp-server-is-and-why-you-should-care">What an MCP Server Is and Why You Should Care</a></p>
</li>
<li><p><a href="#heading-you-can-only-improve-what-you-track">You Can Only Improve What You Track</a></p>
</li>
<li><p><a href="#heading-how-to-start-in-your-own-company">How to Start in Your Own Company</a></p>
</li>
<li><p><a href="#heading-the-real-shift">The Real Shift</a></p>
</li>
</ul>
<h2 id="heading-what-harness-engineering-means">What Harness Engineering Means</h2>
<p>Here's the usual way people use an AI coding agent. You ask for code, it writes some, you read every line because you don't trust it, you fix what's wrong, repeat. The AI is fast, but your review is the bottleneck, so nothing actually got faster.</p>
<p>Harness engineering flips the job. Instead of reviewing every line, you build the environment the agent works in.</p>
<p>The term comes from OpenAI. In a post called <a href="https://openai.com/index/harness-engineering/">Harness engineering</a>, their team describes a five-month experiment where Codex agents wrote roughly a million lines of a production product with no code written by hand.</p>
<p>They define the harness as "the full environment of scaffolding, constraints, and feedback loops" that surrounds an agent and lets it do stable work. In their setup that meant repository structure, CI configuration, formatting rules, project instructions, and tool integrations. The engineer's job shifts from writing the code to designing that environment.</p>
<p>Here's how that applied to us. OpenAI ran the idea with a team of engineers at a million-line scale. I ran it alone, on an internal tool, with four automatic checks, a rules file the agent reads at the start of every session, and a habit of proving each change by running the app and watching it. Same idea, budget version, and it held.</p>
<p>You stop trusting the AI. You start trusting the harness.</p>
<p>This changes what your job is. You spend your time designing checks, writing down rules, and reviewing the output at a higher level. The agent spends its time inside the fence you built.</p>
<p>And this is why one engineer suddenly matters a lot. An agent's speed is worthless when nobody trusts its output, and the harness is the thing that turns speed into output you can trust. Build a good harness and one person ships what used to take a team.</p>
<p>None of this needs permission from your company. My harness was made of things every engineer already knows. A type checker, a test runner, a coverage rule, and a text file with rules in it.</p>
<h2 id="heading-pointing-it-at-a-real-problem">Pointing It at a Real Problem</h2>
<p>The problem I pointed all this at is one every company has. A spec or requirement gets written. Developers build from it. The code changes during review, again in testing, again in production support. Nobody goes back to update the spec, for whatever reason. Six months later the document describes a system that no longer exists.</p>
<p>Most places shrug at this. In regulated lending you don't get to. You need to know what's current, and you sometimes need to show what changed, on what date, and who changed it. A document that quietly stopped being true is a business risk.</p>
<p>So, the case study was an internal documentation platform with one design goal. Docs should tell you when they go stale, instead of waiting for a human to notice.</p>
<p>Every doc declares which code paths it describes. A small script in CI reports code changes to the platform, and any doc whose code moved after its last edit gets flagged as drifting. Add a sign-off workflow where the approval badge turns amber if the doc changes after approval, a health score per document, and a digest that tells owners what needs attention.</p>
<p>Fifty days, 300+ commits, and most of that code was written by Claude Code inside the harness. The plan was mine. We'd worked with a regular wiki for years, so I knew exactly what was missing and what to build. The agent wrote the code. The commits are not the point of the article. They're the evidence that the method works.</p>
<h2 id="heading-the-four-gates">The Four Gates</h2>
<p>Every change the agent made had to pass four gates before it could land. None of them are exotic.</p>
<h3 id="heading-gate-1-the-type-checker">Gate 1: The Type Checker</h3>
<p><code>tsc --noEmit</code> across the whole codebase. No change lands with a type error. This is the cheapest gate and it catches a surprising number of agent mistakes.</p>
<h3 id="heading-gate-2-100-test-coverage-on-the-logic">Gate 2: 100% Test Coverage on the Logic</h3>
<p>Every line, every branch, and every function of the core business logic must be covered by a test, or the build fails. That sounds extreme for a human team, and it is.</p>
<p>For an agent it's perfect, for two reasons. First, the rule is binary, so there's nothing to negotiate. An uncovered branch means a missing test, full stop. Second, the agent has no ego. It never argues that a test is unnecessary. It reads the coverage report like a to-do list and works through it.</p>
<h3 id="heading-gate-3-end-to-end-tests">Gate 3: End-to-End Tests</h3>
<p>A Playwright suite clicks through the real app the way a user would. Unit tests check the logic in isolation. This gate checks the parts users actually touch.</p>
<p>I've written before about <a href="https://www.freecodecamp.org/news/how-i-tested-malaysia-s-open-data-portals-with-plain-english/">testing with plain-English assertions</a>, and the same idea applies here. The e2e suite asserts what a user sees, not what the code intends.</p>
<h3 id="heading-gate-4-verify-by-running-it">Gate 4: Verify by Running It</h3>
<p>After every change, the agent starts the app and watches the behaviour it claims to have changed. This one sounds obvious and gets skipped everywhere. Green tests plus an unverified claim is how a broken change ships with full confidence. Tests confirm the logic. Running the app confirms the claim.</p>
<p>Two text files complete the harness. One is a rules file in the repo. It holds the architecture, the step-by-step recipe every feature follows, and a list of ideas I already rejected, with reasons. Every fresh agent session starts by reading it, so the agent stays consistent and stops re-proposing bad ideas.</p>
<p>The other is a habit. Every feature ships with a short usage page written by the agent, showing the feature working. Writing it forces the agent to actually use what it built. Cheapest integration test I know.</p>
<p>Notice what the harness doesn't include. There's no linter. Style is not what goes wrong in agent-written code. What goes wrong is a plausible-looking branch nobody exercised. Spend your gate budget on behaviour, not formatting.</p>
<h2 id="heading-where-the-harness-failed">Where the Harness Failed</h2>
<p>I want to be honest about the limits, because this is the part most AI articles skip.</p>
<p>The worst bug in the project passed every gate, and I found it by using the platform myself. I renamed a document, the slug got corrupted, and the page stopped loading.</p>
<p>Digging into the rename code showed something worse. The rename rebuilt the record from a partial payload, and any field missing from that payload quietly reset to its default. One of those fields controlled who could see the document. So a rename made a restricted document visible to everyone. Type-safe, fully covered, and wrong, because every test checked the fields the payload carried and no test checked the fields it left out.</p>
<p>Using my own product caught it, not a gate. That's the honest shape of harness engineering. Gates catch the failure types you thought to encode. Using the product and reviewing the output catch the rest. You need both. The harness doesn't remove your judgement from the loop. It spends your judgement where it matters instead of on every line.</p>
<h2 id="heading-what-an-mcp-server-is-and-why-you-should-care">What an MCP Server Is and Why You Should Care</h2>
<p>Everything up to here is about building software with AI. The second half of the story is about what your company does with AI, and this is where MCP comes in.</p>
<p>MCP (Model Context Protocol) is a standard way to give an AI agent access to a system. Think of it as a USB port for your company's tools. Any agent that speaks the protocol can plug into any system that exposes it to read data, take actions, and do work.</p>
<p>I gave the documentation platform an MCP server with 50+ tools. Search the docs, read a page, write a page, comment, check what's drifting, and so on. Any engineer at the company connects their AI agent to it and their agent now works with the company's knowledge base directly.</p>
<p>I got the security model wrong the first time, and the mistake is worth sharing because you might make it. Version one gave the agent direct, trusted access to the database. It was convenient, and broken in three ways: every agent action was anonymous, the agent could read documents its user had no right to see, and there was no way to revoke access.</p>
<p>The fix was to make the MCP server hold no credentials of its own. Each person mints a personal access token in their profile, and every agent action runs as that person, with their exact permissions. A junior's agent can read and comment. An editor's agent can write. Every action lands in the audit trail under the real person's name, and revoking the token cuts the agent off instantly.</p>
<p>The part I like most is how this plays with role-based access control. The token carries no permissions of its own, it only says who you are. Permissions are checked server-side against your current role on every call. So when a person's role changes, or a whole group's access gets tightened, nobody has to hunt down and revoke existing tokens. The agent might still show the same tools in its list, but the server blocks the call the moment the role behind the token no longer allows it.</p>
<p>Here's what that looks like in practice. This is a cut-down version of one tool from my server, using the official TypeScript SDK. The full server is the same pattern repeated 50 times.</p>
<pre><code class="language-typescript">import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const API = process.env.WIKI_API_URL;   // your existing HTTP API
const TOKEN = process.env.WIKI_TOKEN;   // the user's personal access token

const server = new McpServer({ name: "docs-wiki", version: "1.0.0" });

server.registerTool(
  "read_doc",
  {
    description: "Read one document by its slug",
    inputSchema: { slug: z.string() },
  },
  async ({ slug }) =&gt; {
    // The MCP server holds no credentials of its own.
    // It forwards the user's token, and the API checks
    // that user's current role on every single call.
    const res = await fetch(`${API}/docs/${slug}`, {
      headers: { Authorization: `Bearer ${TOKEN}` },
    });

    if (res.status === 403) {
      // Forbidden comes back as a clean tool error,
      // never a crash and never a silent success.
      return {
        content: [{ type: "text", text: "Error: Forbidden." }],
        isError: true,
      };
    }
    if (res.status === 404) {
      // A restricted doc the user can't see returns the same
      // response as a missing one, so its existence never leaks.
      return {
        content: [{ type: "text", text: `No document: ${slug}` }],
        isError: true,
      };
    }

    return { content: [{ type: "text", text: await res.text() }] };
  }
);

await server.connect(new StdioServerTransport());
</code></pre>
<p>Three things in this small file carry all the security weight. The server has no database access, so there's nothing to steal from it. The token travels with every request, so the API applies the real user's permissions and the audit trail gets a real name. And the two error branches make failure boring, a forbidden action reads as a plain error message, and a document the user can't see is indistinguishable from one that doesn't exist.</p>
<p>The rule underneath is simple: <strong>give AI your permission model, not a back door.</strong> That single design decision is why the company trusts agent-written documentation. Nothing the agent does is anonymous or outside what its human could do anyway.</p>
<p>And once agents could write docs safely, something changed. Documentation stopped being a chore after development and became part of it. An agent finishes a feature, writes the doc through the same MCP tools, and flags anything it isn't sure about with an inline <code>[!VERIFY]</code> marker. Anything touching rates or compliance gets an <code>[!SME]</code> marker that blocks approval until an expert signs off. The agent brings speed. The human keeps authority.</p>
<h2 id="heading-you-can-only-improve-what-you-track">You Can Only Improve What You Track</h2>
<p>Here's the belief driving all of this. You can only improve what you track.</p>
<p>Our documentation didn't go stale because people were careless. It went stale because nothing measured staleness. The moment drift became a tracked number, like "this doc's code changed 3 times since its last edit", keeping docs current became a finite, visible job instead of a vague wish.</p>
<p>The same pattern showed up everywhere once I looked for it:</p>
<ul>
<li><p>Every question the AI assistant had no answer for gets logged. An assistant that <a href="https://www.freecodecamp.org/news/how-to-build-an-ai-support-agent-that-knows-when-not-to-answer-tickets/">knows when not to answer</a> turns its own gaps into data. That list is literally a ranked backlog of what to write next, sorted by real demand.</p>
</li>
<li><p>Health scores per document show which owner is overloaded and which corner of the knowledge base needs attention.</p>
</li>
<li><p>The audit log keeps a tamper-evident history of every action. When we need proof of what changed, on what date, by who, it's one query instead of an archaeology dig, and the MCP can read it to compare versions.</p>
</li>
</ul>
<p>None of this needed advanced AI. It needed the data to exist somewhere structured, instead of evaporating in chat messages and inboxes.</p>
<p>That's my working definition of an AI-native company. Not a company with a chatbot. A company whose processes leave trackable data behind, and whose tools are reachable by agents through something like MCP.</p>
<p>Once both are true, the AI does what AI is genuinely good at. It reads more data than any human has patience for, and it points at the patterns. Where work piles up. Which step everyone waits on. What keeps going stale. You stop guessing at bottlenecks and start reading them.</p>
<p>Your company already produces all of this data every day. The question is whether it lands somewhere an agent can read.</p>
<h2 id="heading-how-to-start-in-your-own-company">How to Start in Your Own Company</h2>
<p>You don't need a mandate. I didn't have one. Here's the sequence I'd repeat:</p>
<ol>
<li><p><strong>Pick one process that annoys everyone.</strong> Docs going stale, tickets triaged by hand, release notes nobody writes. Small and real beats big and strategic.</p>
</li>
<li><p><strong>Make its data trackable.</strong> Structured, timestamped, with an owner. This step is boring and it's the one that matters. A spreadsheet is a fine start.</p>
</li>
<li><p><strong>Build the harness before the features.</strong> Decide the checks a change must pass. Write the rules file. Then let the agent build fast inside it.</p>
</li>
<li><p><strong>Expose it over MCP with real permissions.</strong> Personal tokens, actions attributed to real people, revocable. Never a shared back door.</p>
</li>
<li><p><strong>Ask the agent what it sees.</strong> Once the data accumulates, ask where the bottleneck is, what's going stale, what gets asked but never answered. This is the payoff step.</p>
</li>
</ol>
<p>Start low-risk. An internal tool is the perfect first target because your colleagues are forgiving users and the data stays in-house.</p>
<p>In a larger company, you won't get to skip the approval layers, so design for them instead of around them. Reuse the permission model your security team already trusts, keep every agent action attributed to a real person and revocable, and run the pilot inside one team's boundary. Those three properties answer most of the questions a review board will ask before it asks them.</p>
<p>Then let the tracked data make your case. A pilot that shows exactly what it caught, in numbers, is a stronger argument for the next approval than any slide deck.</p>
<h2 id="heading-the-real-shift">The Real Shift</h2>
<p>Fifty days and one engineer changed how a whole company handles its knowledge. But the model didn't do that, and honestly, neither did I in the way it sounds. The harness did the trusting, the MCP did the connecting, and the tracked data did the convincing.</p>
<p>The shift worth copying isn't "use AI to write code faster." It's three habits:</p>
<ul>
<li><p>Build checks so you can mostly trust code you didn't write yourself.</p>
</li>
<li><p>Give agents the same permissions as the person running them, never full access.</p>
</li>
<li><p>Record what your processes do, because you can only improve what you track.</p>
</li>
</ul>
<p>Pick the process that annoys everyone and build the first gate.</p>


                        </section>
                        
                            <div class="sidebar">
                                
                                    
                                    <script>var localizedAdText = "ADVERTISEMENT";</script>
                                
                            </div>
                        
                    </div>
                    <hr>
                    
                        <div class="post-full-author-header" data-test-label="author-header-with-bio">
                            
                                
    
    
    

    <section cla