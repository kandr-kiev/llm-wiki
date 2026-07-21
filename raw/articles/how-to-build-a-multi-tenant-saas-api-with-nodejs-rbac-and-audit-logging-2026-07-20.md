---
source_url: https://www.freecodecamp.org/news/how-to-build-a-multi-tenant-saas-api-with-nodejs-rbac-and-audit-logging/
ingested: 2026-07-20
sha256: 03e92323fe38e17276a4e8b7f528166ff5b74ccf651eb7bb17d1401ecf16d47e
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Build a Multi-Tenant SaaS API with Node.js, RBAC, and Audit Logging</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-to-build-a-multi-tenant-saas-api-with-nodejs-rbac-and-audit-logging/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="A colleague asked me to help debug what looked like a permissions issue in their SaaS project management tool. Users were seeing resources they hadn&#39;t created. I pulled up the query logs expecting som">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Build a Multi-Tenant SaaS API with Node.js, RBAC, and Audit Logging">
    
        <meta property="og:description" content="A colleague asked me to help debug what looked like a permissions issue in their SaaS project management tool. Users were seeing resources they hadn&#39;t created. I pulled up the query logs expecting som">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-to-build-a-multi-tenant-saas-api-with-nodejs-rbac-and-audit-logging/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/69793fe0-fe0e-4c9c-839d-12a134f65287.png">
    <meta property="article:published_time" content="2026-07-20T20:46:12.670Z">
    <meta property="article:modified_time" content="2026-07-20T20:46:12.670Z">
    
        <meta property="article:tag" content="Node.js">
    
        <meta property="article:tag" content="api">
    
        <meta property="article:tag" content="PostgreSQL">
    
        <meta property="article:tag" content="Security">
    
        <meta property="article:tag" content="backend">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Build a Multi-Tenant SaaS API with Node.js, RBAC, and Audit Logging">
    
        <meta name="twitter:description" content="A colleague asked me to help debug what looked like a permissions issue in their SaaS project management tool. Users were seeing resources they hadn&#39;t created. I pulled up the query logs expecting som">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-to-build-a-multi-tenant-saas-api-with-nodejs-rbac-and-audit-logging/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/69793fe0-fe0e-4c9c-839d-12a134f65287.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Zia Ullah">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="Node.js, api, PostgreSQL, Security, backend">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/69793fe0-fe0e-4c9c-839d-12a134f65287.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-to-build-a-multi-tenant-saas-api-with-nodejs-rbac-and-audit-logging/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-20T20:46:12.670Z",
	"dateModified": "2026-07-20T20:46:12.670Z",
	"keywords": "Node.js, api, PostgreSQL, Security, backend",
	"description": "A colleague asked me to help debug what looked like a permissions issue in their SaaS project management tool. Users were seeing resources they hadn&#x27;t created.\nI pulled up the query logs expecting som",
	"headline": "How to Build a Multi-Tenant SaaS API with Node.js, RBAC, and Audit Logging",
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-20T20:46:12.670Z">
                            July 20, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/nodejs/">
                                #Node.js
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Build a Multi-Tenant SaaS API with Node.js, RBAC, and Audit Logging</h1>
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
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/69793fe0-fe0e-4c9c-839d-12a134f65287.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/69793fe0-fe0e-4c9c-839d-12a134f65287.png" alt="How to Build a Multi-Tenant SaaS API with Node.js, RBAC, and Audit Logging" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>A colleague asked me to help debug what looked like a permissions issue in their SaaS project management tool. Users were seeing resources they hadn't created.</p>
<p>I pulled up the query logs expecting something subtle. It was not. The list endpoint had no <code>tenant_id</code> filter at all. Every tenant in the database could read every other tenant's projects. The application never threw an error. It just returned whatever was there.</p>
<p>Missing tenant filters don't throw errors. They return the wrong data without any complaint, and nothing in your logs will flag it. I've seen this run in production for weeks before a support ticket pointed anyone at the query logs.</p>
<p>When it does surface, who finds it first matters a lot. A customer noticing it is bad. A compliance auditor noticing it during a SOC 2 review is a different kind of problem.</p>
<p>Isolation built in from the start is a day of work. The time I spent helping a team retrofit it after a compliance review was considerably longer than that, and involved more customer emails than anyone wanted to write.</p>
<p>The stack is Node.js with PostgreSQL. CRUD is the easy part. Tenant isolation, RBAC, and audit logging take more care, and where those checks run in the stack matters. I put all three in middleware, before any route handler fires. A handler that never calls the isolation logic directly can't accidentally skip it.</p>
<h2 id="heading-prerequisites">Prerequisites</h2>
<ul>
<li><p>Node.js 18+</p>
</li>
<li><p>PostgreSQL 14+</p>
</li>
<li><p>Basic knowledge of Express.js and JWT</p>
</li>
</ul>
<h2 id="heading-what-we-will-build">What We Will Build</h2>
<p>A multi-tenant Express REST API that enforces:</p>
<ol>
<li><p><strong>Tenant isolation:</strong> every database query scopes to the <code>tenant_id</code> from the verified JWT. The client can't influence which tenant the query runs against.</p>
</li>
<li><p><strong>RBAC:</strong> four roles, each with a numeric level (SuperAdmin is highest, Viewer lowest). Middleware checks the level before the handler runs.</p>
</li>
<li><p><strong>Audit logging:</strong> any write or sensitive read appends a row to the audit table. The app can't modify those rows afterward. The database enforces this directly. If a bug in the app tries to UPDATE an audit row, the database refuses it. Application-level enforcement alone can't give you that guarantee.</p>
</li>
<li><p><strong>Per-tenant rate limiting:</strong> request counts in Redis, keyed to the tenant. I've seen IP-based limiting break an enterprise rollout when fifty users came through a single corporate proxy.</p>
</li>
<li><p><strong>Tenant isolation tests:</strong> a dedicated test file that proves cross-tenant data can't leak. Wire it into CI and it catches broken isolation before it ships.</p>
</li>
</ol>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ol>
<li><p><a href="#heading-how-multi-tenancy-works">How Multi-Tenancy Works</a></p>
</li>
<li><p><a href="#heading-architecture-overview">Architecture Overview</a></p>
</li>
<li><p><a href="#heading-database-schema-design">Database Schema Design</a></p>
</li>
<li><p><a href="#heading-project-setup">Project Setup</a></p>
</li>
<li><p><a href="#heading-jwt-design-for-multi-tenancy">JWT Design for Multi-Tenancy</a></p>
</li>
<li><p><a href="#heading-auth-and-rbac-middleware">Auth and RBAC Middleware</a></p>
</li>
<li><p><a href="#heading-the-tenant-safe-repository-layer">The Tenant-Safe Repository Layer</a></p>
</li>
<li><p><a href="#heading-audit-logging-service">Audit Logging Service</a></p>
</li>
<li><p><a href="#heading-per-tenant-rate-limiting">Per-Tenant Rate Limiting</a></p>
</li>
<li><p><a href="#heading-building-the-routes">Building the Routes</a></p>
</li>
<li><p><a href="#heading-testing-tenant-isolation">Testing Tenant Isolation</a></p>
</li>
<li><p><a href="#heading-troubleshooting">Troubleshooting</a></p>
</li>
<li><p><a href="#heading-wrapping-up">Wrapping Up</a></p>
</li>
</ol>
<h2 id="heading-how-multi-tenancy-works">How Multi-Tenancy Works</h2>
<p>This tutorial uses a <strong>shared database with row-level isolation</strong>: a <code>tenant_id</code> column on every table, a filter on every query. The database holds everyone's data together. The application decides what each tenant can see.</p>
<p>Two other approaches exist: schema-per-tenant and database-per-tenant. I've talked to teams on schema-per-tenant who ended up spending more engineering time on migration tooling than on their actual product. Database-per-tenant gives stronger guarantees but a connection pool that balloons with every new customer signup.</p>
<p>Neither scales cheaply. Row-level isolation scales further than most teams expect. The ones I know who moved off it did so years in, usually under specific regulatory pressure, not because the approach stopped working.</p>
<p>The one thing in this design that can't be optional: <code>tenant_id</code> <strong>must always come from the verified JWT.</strong> Not from the request body, not from the URL. Users control what they put in both of those. They don't control what gets signed into a JWT on your server.</p>
<h2 id="heading-architecture-overview">Architecture Overview</h2>
<pre><code class="language-plaintext">HTTP Request
     │
     ▼
┌─────────────────────────────────────────┐
│           Express Middleware Stack       │
│                                         │
│  1. Rate Limiter (per tenant_id)        │
│  2. Auth Middleware (verify JWT)        │
│     └─► Extracts: userId, tenantId,    │
│          role, permissions              │
│  3. RBAC Middleware (check role)        │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│           Route Handler                  │
│                                         │
│  1. Call Repository (tenant-safe query) │
│  2. Call Audit Service (fire &amp; forget)  │
│  3. Return response                     │
└──────────────┬──────────────────────────┘
               │
     ┌─────────┴──────────┐
     ▼                    ▼
┌─────────┐        ┌────────────┐
│ Projects│        │ Audit Logs │
│  Table  │        │   Table    │
│(+tenant)│        │(append only│
└─────────┘        └────────────┘
</code></pre>
<p>Rate limiting, auth, and RBAC all run before any handler sees the request. Writes pass through the audit service. The repository takes <code>tenantId</code> from <code>req.user</code> and the handler never touches tenant scoping directly, so there's no path around it.</p>
<h2 id="heading-database-schema-design">Database Schema Design</h2>
<pre><code class="language-sql">-- Tenants table
CREATE TABLE tenants (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name        VARCHAR(255) NOT NULL,
  plan        VARCHAR(50) NOT NULL DEFAULT 'free', -- 'free', 'pro', 'enterprise'
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Users table
CREATE TABLE users (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id   UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  email       VARCHAR(255) NOT NULL,
  role        VARCHAR(50) NOT NULL DEFAULT 'Member', -- 'SuperAdmin','TenantAdmin','Member','Viewer'
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE(tenant_id, email)
);

CREATE INDEX idx_users_tenant ON users(tenant_id);

-- Projects table (example resource — replace with your domain entity)
CREATE TABLE projects (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id   UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  name        VARCHAR(255) NOT NULL,
  description TEXT,
  created_by  UUID NOT NULL REFERENCES users(id),
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_projects_tenant ON projects(tenant_id);

-- Audit log table (append-only — never UPDATE or DELETE rows here)
CREATE TABLE audit_logs (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id   UUID NOT NULL,
  user_id     UUID NOT NULL,
  user_email  TEXT NOT NULL,
  user_role   TEXT NOT NULL,        -- role at time of action
  action      TEXT NOT NULL,        -- 'CREATE', 'UPDATE', 'DELETE', 'VIEW'
  resource    TEXT NOT NULL,        -- table name
  resource_id TEXT,
  old_values  JSONB,
  new_values  JSONB,
  ip_address  INET,
  user_agent  TEXT,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_audit_tenant ON audit_logs(tenant_id);
CREATE INDEX idx_audit_created ON audit_logs(created_at DESC);

-- Protect audit log at database level
-- Use a DO block so this runs safely in Docker where app_user is the superuser
DO $$
BEGIN
  IF current_user &lt;&gt; 'app_user' THEN
    REVOKE DELETE, UPDATE ON audit_logs FROM app_user;
  END IF;
END $$;
</code></pre>
<p>The <code>REVOKE</code> matters. Application bugs happen. If something in your codebase accidentally tries to UPDATE an audit row, you want the database to refuse it outright, not silently comply.</p>
<h2 id="heading-project-setup">Project Setup</h2>
<pre><code class="language-bash">mkdir nodejs-multitenant-saas-api
cd nodejs-multitenant-saas-api
npm init -y
npm install express pg jsonwebtoken bcryptjs express-rate-limit rate-limit-redis ioredis dotenv
npm install --save-dev jest supertest
</code></pre>
<h3 id="heading-starting-postgresql-and-redis-with-docker">Starting PostgreSQL and Redis with Docker</h3>
<p>Skip the local installs. One <code>docker-compose.yml</code> in the project root brings up both PostgreSQL and Redis:</p>
<pre><code class="language-yaml">services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: saas_api
      POSTGRES_USER: app_user
      POSTGRES_PASSWORD: app_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./schema.sql:/docker-entrypoint-initdb.d/01_schema.sql

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
</code></pre>
<p>That <code>schema.sql</code> mount runs your SQL automatically when the container first starts. No psql required.</p>
<pre><code class="language-bash">docker compose up -d
</code></pre>
<p><code>.env</code> in the project root:</p>
<pre><code class="language-plaintext">DATABASE_URL=postgresql://app_user:app_password@localhost:5432/saas_api
REDIS_URL=redis://localhost:6379
JWT_SECRET=your_random_secret_here
PORT=3000
NODE_ENV=development
</code></pre>
<p>Don't type a <code>JWT_SECRET</code> by hand. Run this to generate one:</p>
<pre><code class="language-bash">node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
</code></pre>
<p>File structure:</p>
<pre><code class="language-plaintext">nodejs-multitenant-saas-api/
├── src/
│   ├── middleware/
│   │   ├── auth.js          # JWT verification + tenant extraction
│   │   ├── rbac.js          # Role enforcement
│   │   └── rateLimiter.js   # Per-tenant rate limiting
│   ├── services/
│   │   └── auditService.js  # Append-only audit logger
│   ├── repositories/
│   │   └── projectRepo.js   # Tenant-safe DB queries
│   ├── routes/
│   │   └── projects.js      # Route handlers
│   └── utils/
│       └── token.js         # JWT token generation
├── db/
│   ├── index.js             # PostgreSQL pool
│   └── redis.js             # Redis client
├── docker-compose.yml
├── app.js
├── server.js
└── tests/
    └── tenantIsolation.test.js
</code></pre>
<h3 id="heading-boilerplate-files">Boilerplate Files</h3>
<p>There are four files the tutorial doesn't cover in detail, but the test file needs all of them to run:</p>
<pre><code class="language-javascript">// db/index.js
const { Pool } = require('pg');

const pool = new Pool({ connectionString: process.env.DATABASE_URL });

pool.on('error', (err) =&gt; console.error('PostgreSQL error:', err.message));

module.exports = { pool };
</code></pre>
<pre><code class="language-javascript">// db/redis.js
const Redis = require('ioredis');

const redisClient = new Redis(process.env.REDIS_URL);

redisClient.on('error', (err) =&gt; console.error('Redis error:', err.message));

module.exports = { redisClient };
</code></pre>
<pre><code class="language-javascript">// app.js
require('dotenv').config();
const express = require('express');
const projectsRouter = require('./src/routes/projects');

const app = express();
app.use(express.json());

app.use('/api/projects', projectsRouter);

// Global error handler — must have 4 parameters to be recognised by Express
app.use((err, req, res, next) =&gt; {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal server error' });
});

module.exports = app;
</code></pre>
<pre><code class="language-javascript">// server.js
const app = require('./app');

const PORT = process.env.PORT || 3000;
app.listen(PORT, () =&gt; console.log(`Server running on port ${PORT}`));
</code></pre>
<p><code>bcryptjs</code> is included for a login endpoint with proper password hashing. That part isn't covered here, but the GitHub repo has a working <code>/api/auth/login</code> example.</p>
<h2 id="heading-jwt-design-for-multi-tenancy">JWT Design for Multi-Tenancy</h2>
<p>Both <code>tenantId</code> and <code>role</code> go into the JWT payload. Everything downstream reads from these two fields. Get them wrong, and nothing behaves correctly.</p>
<pre><code class="language-javascript">// Example JWT payload
{
  "userId": "usr_abc123",
  "tenantId": "ten_xyz789",
  "email": "alice@acme.com",
  "role": "TenantAdmin",
  "iat": 1720000000,
  "exp": 1720086400
}
</code></pre>
<p>The roles in order of privilege:</p>
<ul>
<li><p><strong>SuperAdmin:</strong> cross-tenant access for your internal team only</p>
</li>
<li><p><strong>TenantAdmin:</strong> full access within their tenant</p>
</li>
<li><p><strong>Member:</strong> read and write within their tenant</p>
</li>
<li><p><strong>Viewer:</strong> read-only within their tenant</p>
</li>
</ul>
<p>Generate a token (used for testing and your auth endpoint):</p>
<pre><code class="language-javascript">// src/utils/token.js
const jwt = require('jsonwebtoken');

function generateToken({ userId, tenantId, email, role }) {
  return jwt.sign(
    { userId, tenantId, email, role },
    process.env.JWT_SECRET,
    { expiresIn: '24h' }
  );
}

module.exports = { generateToken };
</code></pre>
<h2 id="heading-auth-and-rbac-middleware">Auth and RBAC Middleware</h2>
<p>The auth middleware does two things: verifies the JWT signature and extracts the tenant context into <code>req.user</code>.</p>
<p>That second part is what the entire system depends on. Every query downstream reads <code>req.user.tenantId</code>. The client has no say in what that value is. They send a token the server signed, and the server reads back what it put in.</p>
<pre><code class="language-javascript">// src/middleware/auth.js
const jwt = require('jsonwebtoken');

function authMiddleware(req, res, next) {
  const authHeader = req.headers.authorization;
  if (!authHeader?.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Missing or malformed Authorization header' });
  }

  const token = authHeader.split(' ')[1];

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);

    // tenantId always comes from the verified token — never req.body or req.params
    req.user = {
      userId:   decoded.userId,
      tenantId: decoded.tenantId,
      email:    decoded.email,
      role:     decoded.role,
    };

    next();
  } catch (err) {
    return res.status(401).json({ error: 'Invalid or expired token' });
  }
}

module.exports = { authMiddleware };
</code></pre>
<p>The RBAC middleware is separate from auth by design. Auth runs on every route. Role enforcement only applies where a minimum role is required. You pass the allowed roles to <code>requireRole()</code> and it compares the user's level against the hierarchy. A Viewer trying to delete something hits the 403 before the handler ever runs.</p>
<pre><code class="language-javascript">// src/middleware/rbac.js
const ROLE_HIERARCHY = {
  SuperAdmin:   4,
  TenantAdmin:  3,
  Member:       2,
  Viewer:       1,
};

// requireRole('TenantAdmin') — user must be TenantAdmin or higher
function requireRole(...roles) {
  return (req, res, next) =&gt; {
    const userLevel = ROLE_HIERARCHY[req.user?.role] ?? 0;
    const requiredLevel = Math.min(...roles.map(r =&gt; ROLE_HIERARCHY[r] ?? 999));

    if (userLevel &lt; requiredLevel) {
      return res.status(403).json({
        error: 'Insufficient permissions',
        required: roles,
        current: req.user?.role,
      });
    }

    next();
  };
}

module.exports = { requireRole };
</code></pre>
<h2 id="heading-the-tenant-safe-repository-layer">The Tenant-Safe Repository Layer</h2>
<p>Isolation lives here. Every function takes <code>tenantId</code> as a required argument, pulled from <code>req.user</code> by the handler. There's no way to call these without providing a tenant scope. I've watched teams try to handle this with a URL parameter instead (<code>GET /api/projects?tenantId=xyz</code>) and call it isolated. It is not. Any client sends whatever it wants in a query string.</p>
<pre><code class="language-javascript">// src/repositories/projectRepo.js
const { pool } = require('../../db');

// List all projects for a tenant — tenantId is ALWAYS from the JWT
async function listProjects(tenantId) {
  const result = await pool.query(
    `SELECT id, name, description, created_by, created_at
     FROM projects
     WHERE tenant_id = $1
     ORDER BY created_at DESC`,
    [tenantId]
  );
  return result.rows;
}

// Get a single project — returns null if it belongs to a different tenant
// NOTE: Returns 404 (not 403) intentionally — don't reveal the resource exists
async function getProject(id, tenantId) {
  const result = await pool.query(
    `SELECT id, name, description, created_by, created_at
     FROM projects
     WHERE id = $1 AND tenant_id = $2`,
    [id, tenantId]
  );
  return result.rows[0] || null;
}

async function createProject({ tenantId, name, description, createdBy }) {
  const result = await pool.query(
    `INSERT INTO projects (tenant_id, name, description, created_by)
     VALUES ($1, $2, $3, $4)
     RETURNING *`,
    [tenantId, name, description, createdBy]
  );
  return result.rows[0];
}

async function updateProject(id, tenantId, updates) {
  const result = await pool.query(
    `UPDATE projects
     SET name = COALESCE($3, name),
         description = COALESCE($4, description),
         updated_at = NOW()
     WHERE id = $1 AND tenant_id = $2
     RETURNING *`,
    [id, tenantId, updates.name, updates.description]
  );
  return result.rows[0] || null;
}

async function deleteProject(id, tenantId) {
  const result = await pool.query(
    `DELETE FROM projects WHERE id = $1 AND tenant_id = $2 RETURNING id`,
    [id, tenantId]
  );
  return result.rows[0] || null;
}

module.exports = { listProjects, getProject, createProject, updateProject, deleteProject };
</code></pre>
<p>Notice what <code>getProject</code> does when Tenant A tries to fetch a Tenant B resource. The query runs with Tenant A's <code>tenantId</code>. The condition <code>id = $1 AND tenant_id = $2</code> matches nothing, <code>null</code> comes back, and the handler sends a <code>404</code>. Not a <code>403</code>. A 403 tells the caller the resource exists, but they can't access it, which is information they shouldn't have.</p>
<h2 id="heading-audit-logging-service">Audit Logging Service</h2>
<pre><code class="language-javascript">// src/services/auditService.js
const { pool } = require('../../db');

async function log({
  tenantId,
  userId,
  userEmail,
  userRole,          // role at time of action — roles change, log should not
  action,            // 'CREATE' | 'UPDATE' | 'DELETE' | 'VIEW'
  resource,          // table name
  resourceId = null,
  oldValues = null,
  newValues = null,
  ipAddress = null,
  userAgent = null,
}) {
  const query = `
    INSERT INTO audit_logs
      (tenant_id, user_id, user_email, user_role, action, resource,
       resource_id, old_values, new_values, ip_address, user_agent)
    VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)
  `;

  const values = [
    tenantId, userId, userEmail, userRole, action, resource,
    resourceId,
    oldValues  ? JSON.stringify(oldValues)  : null,
    newValues  ? JSON.stringify(newValues)  : null,
   