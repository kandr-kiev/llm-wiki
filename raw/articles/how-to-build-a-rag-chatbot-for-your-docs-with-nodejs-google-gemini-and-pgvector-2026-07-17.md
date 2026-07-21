---
source_url: https://www.freecodecamp.org/news/how-to-build-rag-chatbot-nodejs-gemini-pgvector/
ingested: 2026-07-17
sha256: 5457dbb5020e8007425e5d53f70a867394736d8d5c205066c5ee37e5fb519230
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Build a RAG Chatbot for Your Docs with Node.js, Google Gemini, and pgvector</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-to-build-rag-chatbot-nodejs-gemini-pgvector/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="I was helping a team that had a 200-page API documentation PDF. Every new engineer spent their first two weeks Ctrl+F-ing through it, asking the same questions in Slack, getting redirected to the same">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Build a RAG Chatbot for Your Docs with Node.js, Google Gemini, and pgvector">
    
        <meta property="og:description" content="I was helping a team that had a 200-page API documentation PDF. Every new engineer spent their first two weeks Ctrl+F-ing through it, asking the same questions in Slack, getting redirected to the same">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-to-build-rag-chatbot-nodejs-gemini-pgvector/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/9aa3d8d3-9c51-42a7-8e78-907802394ea1.png">
    <meta property="article:published_time" content="2026-07-15T15:26:34.280Z">
    <meta property="article:modified_time" content="2026-07-15T15:26:34.280Z">
    
        <meta property="article:tag" content="Node.js">
    
        <meta property="article:tag" content="AI">
    
        <meta property="article:tag" content="PostgreSQL">
    
        <meta property="article:tag" content="Tutorial">
    
        <meta property="article:tag" content="JavaScript">
    
        <meta property="article:tag" content="RAG ">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Build a RAG Chatbot for Your Docs with Node.js, Google Gemini, and pgvector">
    
        <meta name="twitter:description" content="I was helping a team that had a 200-page API documentation PDF. Every new engineer spent their first two weeks Ctrl+F-ing through it, asking the same questions in Slack, getting redirected to the same">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-to-build-rag-chatbot-nodejs-gemini-pgvector/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/9aa3d8d3-9c51-42a7-8e78-907802394ea1.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Zia Ullah">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="Node.js, AI, PostgreSQL, Tutorial, JavaScript, RAG ">
    <meta name="twitter:site" content="@freecodecamp">
    
        <meta name="twitter:creator" content="@Zia_Ullah_Khan">
    

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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/9aa3d8d3-9c51-42a7-8e78-907802394ea1.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-to-build-rag-chatbot-nodejs-gemini-pgvector/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-15T15:26:34.280Z",
	"dateModified": "2026-07-15T15:26:34.280Z",
	"keywords": "Node.js, AI, PostgreSQL, Tutorial, JavaScript, RAG ",
	"description": "I was helping a team that had a 200-page API documentation PDF. Every new engineer spent their first two weeks Ctrl+F-ing through it, asking the same questions in Slack, getting redirected to the same",
	"headline": "How to Build a RAG Chatbot for Your Docs with Node.js, Google Gemini, and pgvector",
	"author": {
		"@type": "Person",
		"name": "Zia Ullah",
		"url": "https://www.freecodecamp.org/news/author/ziaullahzia/",
		"sameAs": [
			"https://ziaongit.github.io",
			"https://x.com/Zia_Ullah_Khan"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/uploads/avatars/6a32d4e8d06aa63cd556c4b9/9666ebc0-e7de-4f75-bd06-852d27c30919.jpg",
			"width": 1024,
			"height": 1024
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-15T15:26:34.280Z">
                            July 15, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/nodejs/">
                                #Node.js
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Build a RAG Chatbot for Your Docs with Node.js, Google Gemini, and pgvector</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/uploads/avatars/6a32d4e8d06aa63cd556c4b9/9666ebc0-e7de-4f75-bd06-852d27c30919.jpg 60w" sizes="60px" src="https://cdn.hashnode.com/uploads/avatars/6a32d4e8d06aa63cd556c4b9/9666ebc0-e7de-4f75-bd06-852d27c30919.jpg" class="author-profile-image" alt="Zia Ullah" width="1024" height="1024" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/ziaullahzia/" data-test-label="profile-link">
                    
                        Zia Ullah
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/9aa3d8d3-9c51-42a7-8e78-907802394ea1.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/9aa3d8d3-9c51-42a7-8e78-907802394ea1.png" alt="How to Build a RAG Chatbot for Your Docs with Node.js, Google Gemini, and pgvector" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>I was helping a team that had a 200-page API documentation PDF. Every new engineer spent their first two weeks Ctrl+F-ing through it, asking the same questions in Slack, getting redirected to the same paragraphs on page 47.</p>
<p>The doc was accurate. It was even well-written. But nobody could find anything in it fast enough for it to be useful.</p>
<p>That's the problem RAG, or Retrieval-Augmented Generation, solves.</p>
<p>The naïve approach is to stuff your entire PDF into a prompt and let the model figure it out. That breaks down fast: context windows overflow, costs spike on every request, and the model loses the thread somewhere in the wall of text.</p>
<p>RAG takes a different approach. Your documents get broken into small chunks upfront. Ask it a question and it digs out the 3 or 4 chunks that best match it — those are what the model actually sees. The model gets a tight, focused context. The answer comes from what your document actually says — not from whatever the LLM memorized during training.</p>
<p>In this tutorial, you'll build that from scratch. Upload any PDF — an API reference, an internal spec, a research paper — and ask questions about it in plain English. The system finds the relevant sections and answers from the document itself, not from general training data.</p>
<p>The stack: Node.js with Express, Google Gemini for embeddings, Groq for text generation, and pgvector running in Docker. Every piece of it is free — no credit card, no trial period.</p>
<p>The complete code is on GitHub at <a href="https://github.com/ziaongit/nodejs-rag-chatbot">nodejs-rag-chatbot</a>.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-how-rag-works">How RAG Works</a></p>
</li>
<li><p><a href="#heading-what-were-building">What We're Building</a></p>
</li>
<li><p><a href="#heading-prerequisites">Prerequisites</a></p>
</li>
<li><p><a href="#heading-project-setup">Project Setup</a></p>
</li>
<li><p><a href="#heading-set-up-postgres-with-pgvector-using-docker">Set Up Postgres with pgvector Using Docker</a></p>
</li>
<li><p><a href="#heading-connect-to-the-database">Connect to the Database</a></p>
</li>
<li><p><a href="#heading-build-the-ingestion-pipeline">Build the Ingestion Pipeline</a></p>
</li>
<li><p><a href="#heading-build-the-query-pipeline">Build the Query Pipeline</a></p>
</li>
<li><p><a href="#heading-build-the-chat-api-with-express">Build the Chat API with Express</a></p>
</li>
<li><p><a href="#heading-test-the-chatbot">Test the Chatbot</a></p>
</li>
<li><p><a href="#heading-troubleshooting">Troubleshooting</a></p>
</li>
<li><p><a href="#heading-how-to-swap-in-openai">How to Swap in OpenAI</a></p>
</li>
<li><p><a href="#heading-what-to-build-next">What to Build Next</a></p>
</li>
</ul>
<h2 id="heading-how-rag-works">How RAG Works</h2>
<p>RAG has two phases, and the code maps directly to both.</p>
<p><strong>Ingestion phase</strong> — runs once when you upload a document:</p>
<ol>
<li><p>Pull the raw text out of the PDF</p>
</li>
<li><p>Break it into chunks of 400 to 600 characters each, with a bit of overlap so nothing important gets cut at a boundary</p>
</li>
<li><p>Run each chunk through an embedding model, which turns it into a vector (a long list of numbers that captures what the text means)</p>
</li>
<li><p>Store each chunk and its vector in Postgres</p>
</li>
</ol>
<p><strong>Query phase</strong> — runs every time someone asks a question:</p>
<ol>
<li><p>Embed the user's question using the same model</p>
</li>
<li><p>Search the database for chunks whose vectors are closest to the question vector</p>
</li>
<li><p>Take the top 5 matching chunks and assemble them into a context block</p>
</li>
<li><p>Send <code>context + question</code> to the LLM and return its answer</p>
</li>
</ol>
<p>The reason this works better than keyword search: the embedding model captures <em>meaning</em>, not just exact words. If your doc says "terminate the process" and the user asks "how do I stop it?", vector similarity finds that match. Regular string matching doesn't.</p>
<p>One thing that trips people up: you must use the same embedding model at query time as you did at ingestion. The model defines the geometric space those vectors live in. Switch models halfway through and the coordinates stop meaning the same thing — you'd be comparing apples to completely different apples.</p>
<h2 id="heading-what-were-building">What We're Building</h2>
<p>The architecture is intentionally minimal: two endpoints, with nothing you don't need:</p>
<ul>
<li><p><code>POST /ingest</code>: accepts a PDF upload, chunks it, embeds each chunk, stores vectors in pgvector</p>
</li>
<li><p><code>POST /chat</code>: accepts a question, retrieves the most relevant chunks, returns an LLM-generated answer</p>
</li>
</ul>
<p>The full tech stack:</p>
<ul>
<li><p><strong>Node.js + Express</strong> — API layer</p>
</li>
<li><p><strong>Google Gemini free API</strong> — <code>gemini-embedding-001</code> for embeddings (3,072 dimensions per chunk)</p>
</li>
<li><p><strong>Groq free API</strong> — <code>llama-3.1-8b-instant</code> for text generation</p>
</li>
<li><p><strong>PostgreSQL + pgvector</strong> — vector storage and cosine similarity search, running in Docker</p>
</li>
<li><p><strong>pdf-parse</strong> — extracts raw text from PDF buffers</p>
</li>
</ul>
<p>Gemini handles embeddings and Groq handles generation. Splitting them across two providers isn't arbitrary. Gemini's generation API has a quota limit of zero in certain regions (including Pakistan), while Groq works everywhere with no restrictions. Using Groq for generation means this tutorial runs the same way regardless of where you are.</p>
<h2 id="heading-prerequisites">Prerequisites</h2>
<p>Before you start:</p>
<ul>
<li><p>Node.js 20+ installed on your machine</p>
</li>
<li><p>Docker Desktop running (this is how we'll run Postgres locally)</p>
</li>
<li><p>A free Google Gemini API key (for embeddings)</p>
</li>
<li><p>A free Groq API key (for text generation)</p>
</li>
</ul>
<h3 id="heading-how-to-get-your-free-gemini-api-key">How to Get Your Free Gemini API Key</h3>
<ol>
<li><p>Go to <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a> and sign in with a Google account</p>
</li>
<li><p>Click "Create API key"</p>
</li>
<li><p>Select "Create API key in new project"</p>
</li>
<li><p>Copy the key — it starts with <code>AIzaSy...</code></p>
</li>
</ol>
<p>No credit card or billing required.</p>
<h3 id="heading-how-to-get-your-free-groq-api-key">How to Get Your Free Groq API Key</h3>
<ol>
<li><p>Go to <a href="https://console.groq.com">console.groq.com</a> and sign up with Google</p>
</li>
<li><p>Click "API Keys" in the left sidebar</p>
</li>
<li><p>Click "Create API Key", give it a name, copy the key — it starts with <code>gsk_...</code></p>
</li>
</ol>
<p>Groq is free with generous rate limits and works in all regions.</p>
<h2 id="heading-project-setup">Project Setup</h2>
<p>Create the project directory and initialize it:</p>
<pre><code class="language-bash">mkdir nodejs-rag-chatbot
cd nodejs-rag-chatbot
npm init -y
</code></pre>
<p>Install dependencies:</p>
<pre><code class="language-bash">npm install express pg pdf-parse uuid dotenv multer
npm install --save-dev nodemon
</code></pre>
<p>A quick note on the packages: <code>multer</code> is what makes file uploads work on the <code>/ingest</code> endpoint. Without it, Express can't parse multipart form data.</p>
<p><code>pdf-parse</code> does the heavy lifting on PDFs, though watch out for scanned PDFs. Those are just images with no text layer underneath, so you'll get back an empty string.</p>
<p><code>pg</code> talks to Postgres, <code>uuid</code> gives each row a unique ID, and <code>dotenv</code> loads your keys before the app does anything.</p>
<p>Create a <code>.env</code> in the project root. It needs seven values:</p>
<pre><code class="language-plaintext">GEMINI_API_KEY=AIzaSy...         ← your Gemini key from Google AI Studio
GROQ_API_KEY=gsk_...             ← your Groq key from console.groq.com
POSTGRES_USER=rag_user
POSTGRES_PASSWORD=rag_pass       ← choose any password, this is local only
POSTGRES_DB=rag_db
DATABASE_URL=postgresql://rag_user:rag_pass@localhost:5432/rag_db
PORT=3000
</code></pre>
<p>One thing: the password in <code>POSTGRES_PASSWORD</code> and the one in <code>DATABASE_URL</code> must match exactly. I changed just one of them once and spent way too long debugging a "password authentication failed" error before realising the two values were out of sync.</p>
<p>Update <code>package.json</code> scripts:</p>
<pre><code class="language-json">"scripts": {
  "start": "node src/index.js",
  "dev": "nodemon src/index.js"
}
</code></pre>
<p>Create the <code>src</code> directory:</p>
<pre><code class="language-bash">mkdir src
</code></pre>
<p>Your final folder structure will look like this:</p>
<pre><code class="language-plaintext">nodejs-rag-chatbot/
├── src/
│   ├── index.js        ← Express app entry point
│   ├── db.js           ← Postgres connection and schema setup
│   ├── embeddings.js   ← Gemini embedding + Groq generation
│   ├── ingest.js       ← Document ingestion pipeline
│   └── query.js        ← RAG query pipeline
├── docker-compose.yml
├── .env
└── package.json
</code></pre>
<h2 id="heading-set-up-postgres-with-pgvector-using-docker">Set Up Postgres with pgvector Using Docker</h2>
<p>pgvector adds a <code>vector</code> column type to Postgres and the operators needed to search it by similarity. Normally you'd have to install it yourself, but the <code>pgvector/pgvector</code> Docker image ships with it already baked in. Just pull the image and you're good.</p>
<p>Now add <code>docker-compose.yml</code> to the project root:</p>
<pre><code class="language-yaml">services:
  postgres:
    image: pgvector/pgvector:pg16
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
</code></pre>
<p>Those <code>${VARIABLE}</code> references get swapped out from <code>.env</code> when Compose starts — so <code>docker-compose.yml</code> itself stays clean. This is worth doing from day one. I've seen people skip this and regret it after a repo goes public.</p>
<p>Start it:</p>
<pre><code class="language-bash">docker compose up -d
</code></pre>
<h2 id="heading-connect-to-the-database">Connect to the Database</h2>
<p>Create <code>src/db.js</code>. This sets up the connection pool and creates the <code>documents</code> table on first run:</p>
<pre><code class="language-javascript">const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

async function initDb() {
  await pool.query(`CREATE EXTENSION IF NOT EXISTS vector`);

  await pool.query(`
    CREATE TABLE IF NOT EXISTS documents (
      id UUID PRIMARY KEY,
      content TEXT NOT NULL,
      source TEXT NOT NULL,
      embedding VECTOR(3072)
    )
  `);

  console.log('Database ready');
}

module.exports = { pool, initDb };
</code></pre>
<p>The <code>VECTOR(3072)</code> dimension matches the output of Gemini's <code>gemini-embedding-001</code> model exactly. If you use a different embedding model in the future, check its output dimensions and update this number to match.</p>
<h2 id="heading-build-the-ingestion-pipeline">Build the Ingestion Pipeline</h2>
<p>Start with <code>embeddings.js</code>. This file is the bridge to both external APIs — Gemini for turning text into vectors, Groq for generating the final answer. Keeping both in one place means a single file to touch if you ever swap providers.</p>
<p><strong>src/embeddings.js:</strong></p>
<pre><code class="language-javascript">const GEMINI_KEY = process.env.GEMINI_API_KEY;
const GEMINI_BASE = 'https://generativelanguage.googleapis.com/v1/models';

async function embedText(text) {
  const res = await fetch(
    `${GEMINI_BASE}/gemini-embedding-001:embedContent?key=${GEMINI_KEY}`,
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ content: { parts: [{ text }] } }),
    }
  );
  const data = await res.json();
  if (!res.ok) throw new Error(JSON.stringify(data));
  return data.embedding.values;
}

async function generateAnswer(context, question) {
  const res = await fetch(
    'https://api.groq.com/openai/v1/chat/completions',
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.GROQ_API_KEY}`,
      },
      body: JSON.stringify({
        model: 'llama-3.1-8b-instant',
        messages: [
          {
            role: 'system',
            content: 'You are a helpful assistant. Answer the question using only the context provided. If the context does not contain enough information, say so clearly.',
          },
          {
            role: 'user',
            content: `Context:\n${context}\n\nQuestion: ${question}`,
          },
        ],
      }),
    }
  );
  const data = await res.json();
  if (!res.ok) throw new Error(JSON.stringify(data));
  return data.choices[0].message.content;
}

module.exports = { embedText, generateAnswer };
</code></pre>
<p>We're calling both APIs directly with Node.js's built-in <code>fetch</code> rather than the official SDKs. The reason is practical: Google's Node.js SDK routes requests through the <code>v1beta</code> endpoint by default, and <code>gemini-embedding-001</code> isn't available there — only on <code>v1</code>. Direct fetch sidesteps that entirely and keeps the dependency count low.</p>
<p><strong>src/ingest.js:</strong></p>
<pre><code class="language-javascript">const pdfParse = require('pdf-parse');
const { v4: uuidv4 } = require('uuid');
const { pool } = require('./db');
const { embedText } = require('./embeddings');

function chunkText(text, chunkSize = 500, overlap = 50) {
  const chunks = [];
  let start = 0;

  while (start &lt; text.length) {
    const end = Math.min(start + chunkSize, text.length);
    chunks.push(text.slice(start, end).trim());
    start += chunkSize - overlap;
  }

  return chunks.filter(chunk =&gt; chunk.length &gt; 50);
}

async function ingestDocument(buffer, filename) {
  const { text } = await pdfParse(buffer);
  const chunks = chunkText(text);

  console.log(`Processing ${chunks.length} chunks from "${filename}"`);

  for (const chunk of chunks) {
    const embedding = await embedText(chunk);

    await pool.query(
      `INSERT INTO documents (id, content, source, embedding)
       VALUES ($1, $2, $3, $4::vector)`,
      [uuidv4(), chunk, filename, JSON.stringify(embedding)]
    );
  }

  return chunks.length;
}

module.exports = { ingestDocument };
</code></pre>
<p>500 characters per chunk, with 50 characters of overlap between neighbours.</p>
<p>Why the overlap? Without it, a sentence that straddles a boundary gets split, half in one chunk, half in the next — and neither piece makes sense on its own when retrieved. The overlap keeps those boundary sentences intact.</p>
<p>For most technical docs, 500 is a good starting point. Dense legal or financial text tends to need something closer to 300.</p>
<h2 id="heading-build-the-query-pipeline">Build the Query Pipeline</h2>
<p><strong>src/query.js:</strong></p>
<pre><code class="language-javascript">const { pool } = require('./db');
const { embedText, generateAnswer } = require('./embeddings');

async function queryDocuments(question) {
  const questionEmbedding = await embedText(question);

  const { rows } = await pool.query(
    `SELECT content, source,
            1 - (embedding &lt;=&gt; $1::vector) AS similarity
     FROM documents
     ORDER BY embedding &lt;=&gt; $1::vector
     LIMIT 5`,
    [JSON.stringify(questionEmbedding)]
  );

  if (rows.length === 0) {
    return { answer: 'No relevant documents found.', sources: [] };
  }

  const context = rows.map(r =&gt; r.content).join('\n\n---\n\n');
  const answer = await generateAnswer(context, question);

  return {
    answer,
    sources: [...new Set(rows.map(r =&gt; r.source))],
    topSimilarity: parseFloat(rows[0].similarity).toFixed(3),
  };
}

module.exports = { queryDocuments };
</code></pre>
<p>The <code>&lt;=&gt;</code> operator is pgvector's cosine distance. Semantically similar text produces vectors that point in the same direction — so the distance between them is small. Flip that with <code>1 - distance</code> and you get a similarity score, where anything close to 1 means a strong match.</p>
<p>I found 0.7 to be a reliable threshold in my testing — chunks above that were almost always relevant. Anything below 0.5 and the retrieval was really stretching, pulling chunks that shared a keyword or two but weren't actually answering the question.</p>
<p>When that happens, the system prompt instruction ("if the context does not contain enough information, say so clearly") becomes important. A well-behaved model will tell the user it doesn't know rather than guess.</p>
<p>We also surface the source filename. Once you've ingested more than one document, users need to know whether that answer came from the architecture spec or the incident report.</p>
<h2 id="heading-build-the-chat-api-with-express">Build the Chat API with Express</h2>
<p><strong>src/index.js:</strong></p>
<pre><code class="language-javascript">require('dotenv').config();
const express = require('express');
const multer = require('multer');
const { initDb } = require('./db');
const { ingestDocument } = require('./ingest');
const { queryDocuments } = require('./query');

const app = express();
const upload = multer({ storage: multer.memoryStorage() });

app.use(express.json());

app.post('/ingest', upload.single('file'), async (req, res) =&gt; {
  if (!req.file) {
    return res.status(400).json({ error: 'No file uploaded' });
  }

  if (!req.file.mimetype.includes('pdf')) {
    return res.status(400).json({ error: 'Only PDF files are supported' });
  }

  try {
    const count = await ingestDocument(req.file.buffer, req.file.originalname);
    res.json({ message: `Ingested ${count} chunks from "${req.file.originalname}"` });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Ingestion failed', detail: err.message });
  }
});

app.post('/chat', async (req, res) =&gt; {
  const { question } = req.body;

  if (!question || typeof question !== 'string') {
    return res.status(400).json({ error: 'question is required' });
  }

  try {
    const result = await queryDocuments(question);
    res.json(result);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Query failed', detail: err.message });
  }
});

const PORT = process.env.PORT || 3000;

initDb().then(() =&gt; {
  app.listen(PORT, () =&gt; {
    console.log(`RAG chatbot running on port ${PORT}`);
  });
});
</code></pre>
<p><code>memoryStorage()</code> keeps the uploaded file in a buffer instead of writing it to disk. We parse it and store the chunks immediately, so there's nothing to save.</p>
<h2 id="heading-test-the-chatbot">Test the Chatbot</h2>
<p>Start the server:</p>
<pre><code class="language-bash">npm run dev
</code></pre>
<p>You should see:</p>
<pre><code class="language-plaintext">Database ready
RAG chatbot running on port 3000
</code></pre>
<p>Upload a PDF. Any PDF works. I tested with a copy of a Node.js best practices guide:</p>
<pre><code class="language-bash"># Linux / macOS
curl -X POST http://localhost:3000/ingest -F "file=@your-document.pdf"

# Windows PowerShell
curl.exe -X POST http://localhost:3000/ingest -F "file=@your-document.pdf"
</code></pre>
<p>Response:</p>
<pre><code class="language-json">{ "message": "Ingested 142 chunks from \"your-document.pdf\"" }
</code></pre>
<p>Now ask a question:</p>
<pre><code class="language-bash"># Linux / macOS
curl -X POST http://localhost:3000/chat \
  -H "Content-Type: application/json" \
  -d '{ "question": "How should I handle errors in async functions?" }'

# Windows PowerShell
curl.exe -X POST http://localhost:3000/chat -H "Content-Type: application/json" -d "{\"question\": \"How should I handle errors in async functions?\"}"
</code></pre>
<p>Response:</p>
<pre><code class="language-json">{
  "answer": "For async functions in Node.js, wrap your logic in a try/cat