---
source_url: https://www.freecodecamp.org/news/how-to-build-an-internal-developer-platform-a-complete-guide-to-backstage-argocd-and-crossplane/
ingested: 2026-07-18
sha256: af3c15e159d1c8ee45a87e549a7303fea345bbc7bcba5e52c291685b9a329c6d
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Build an Internal Developer Platform: A Complete Guide to Backstage, ArgoCD, and Crossplane</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-to-build-an-internal-developer-platform-a-complete-guide-to-backstage-argocd-and-crossplane/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="Every fast-growing engineering team eventually hits the same wall. A developer needs a new staging environment, so they file a ticket. The platform team queues it. Two weeks later, the environment exi">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Build an Internal Developer Platform: A Complete Guide to Backstage, ArgoCD, and Crossplane">
    
        <meta property="og:description" content="Every fast-growing engineering team eventually hits the same wall. A developer needs a new staging environment, so they file a ticket. The platform team queues it. Two weeks later, the environment exi">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-to-build-an-internal-developer-platform-a-complete-guide-to-backstage-argocd-and-crossplane/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/4e45df2a-5af9-4feb-84fa-f7eb1c04ee91.png">
    <meta property="article:published_time" content="2026-07-17T20:31:41.070Z">
    <meta property="article:modified_time" content="2026-07-17T20:31:41.070Z">
    
        <meta property="article:tag" content="Platform Engineering ">
    
        <meta property="article:tag" content="Devops">
    
        <meta property="article:tag" content="Kubernetes">
    
        <meta property="article:tag" content="gitops">
    
        <meta property="article:tag" content="Cloud Computing">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Build an Internal Developer Platform: A Complete Guide to Backstage, ArgoCD, and Crossplane">
    
        <meta name="twitter:description" content="Every fast-growing engineering team eventually hits the same wall. A developer needs a new staging environment, so they file a ticket. The platform team queues it. Two weeks later, the environment exi">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-to-build-an-internal-developer-platform-a-complete-guide-to-backstage-argocd-and-crossplane/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/4e45df2a-5af9-4feb-84fa-f7eb1c04ee91.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Ayobami Adejumo">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="Platform Engineering , Devops, Kubernetes, gitops, Cloud Computing">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/4e45df2a-5af9-4feb-84fa-f7eb1c04ee91.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-to-build-an-internal-developer-platform-a-complete-guide-to-backstage-argocd-and-crossplane/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-17T20:31:41.070Z",
	"dateModified": "2026-07-17T20:31:41.070Z",
	"keywords": "Platform Engineering , Devops, Kubernetes, gitops, Cloud Computing",
	"description": "Every fast-growing engineering team eventually hits the same wall.\nA developer needs a new staging environment, so they file a ticket. The platform team queues it.\nTwo weeks later, the environment exi",
	"headline": "How to Build an Internal Developer Platform: A Complete Guide to Backstage, ArgoCD, and Crossplane",
	"author": {
		"@type": "Person",
		"name": "Ayobami Adejumo",
		"url": "https://www.freecodecamp.org/news/author/aayostem/",
		"sameAs": [],
		"image": {
			"@type": "ImageObject",
			"url": "https://lh3.googleusercontent.com/a/ACg8ocK7fWyBswxJ1N2BtJ9YSAKesdcHLSULl1nnWuKITGTqdWMgWQ=s96-c",
			"width": 96,
			"height": 96
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-17T20:31:41.070Z">
                            July 17, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/platform-engineering/">
                                #Platform Engineering 
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Build an Internal Developer Platform: A Complete Guide to Backstage, ArgoCD, and Crossplane</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://lh3.googleusercontent.com/a/ACg8ocK7fWyBswxJ1N2BtJ9YSAKesdcHLSULl1nnWuKITGTqdWMgWQ=s96-c 60w" sizes="60px" src="https://lh3.googleusercontent.com/a/ACg8ocK7fWyBswxJ1N2BtJ9YSAKesdcHLSULl1nnWuKITGTqdWMgWQ=s96-c" class="author-profile-image" alt="Ayobami Adejumo" width="96" height="96" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/aayostem/" data-test-label="profile-link">
                    
                        Ayobami Adejumo
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/4e45df2a-5af9-4feb-84fa-f7eb1c04ee91.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/4e45df2a-5af9-4feb-84fa-f7eb1c04ee91.png" alt="How to Build an Internal Developer Platform: A Complete Guide to Backstage, ArgoCD, and Crossplane" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>Every fast-growing engineering team eventually hits the same wall.</p>
<p>A developer needs a new staging environment, so they file a ticket. The platform team queues it.</p>
<p>Two weeks later, the environment exists. It's configured slightly differently from the last one, with a naming convention that doesn't match the production setup, missing the observability stack the previous environment had. The developer deploys. Something breaks. Nobody knows why.</p>
<p>The problem isn't the ticket queue. The problem is the absence of a platform: a paved road where developers can self-serve infrastructure, deployments, and environments that are consistent, auditable, and safe without requiring a platform engineer for every request.</p>
<p>An Internal Developer Platform (IDP) solves this. Not by removing platform engineers from the picture, but by shifting their work from executing individual requests to building the systems that execute those requests automatically.</p>
<p>This handbook builds a production-grade IDP from the three CNCF tools that form its core in 2026: Backstage as the developer portal and software catalog, ArgoCD as the GitOps continuous delivery engine, and Crossplane as the Kubernetes-native infrastructure control plane.</p>
<p>By the end, developers on your platform will be able to provision a cloud database, deploy an application to staging, and register a new service in the catalog — all without filing a single ticket.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-what-youll-learn">What You'll Learn</a></p>
</li>
<li><p><a href="#heading-prerequisites">Prerequisites</a></p>
</li>
<li><p><a href="#heading-part-1-idp-architecture-the-three-layer-model">Part 1: IDP Architecture — The Three-Layer Model</a></p>
</li>
<li><p><a href="#heading-part-2-argocd-the-gitops-foundation">Part 2: ArgoCD — The GitOps Foundation</a></p>
</li>
<li><p><a href="#heading-part-3-crossplane-infrastructure-as-kubernetes-resources">Part 3: Crossplane — Infrastructure as Kubernetes Resources</a></p>
</li>
<li><p><a href="#heading-part-4-backstage-the-developer-portal">Part 4: Backstage — The Developer Portal</a></p>
</li>
<li><p><a href="#heading-part-5-wiring-it-together-the-golden-path">Part 5: Wiring It Together — The Golden Path</a></p>
</li>
<li><p><a href="#heading-part-6-finops-integration-cost-attribution-on-the-idp">Part 6: FinOps Integration — Cost Attribution on the IDP</a></p>
</li>
<li><p><a href="#heading-part-7-the-platform-maturity-model-measuring-what-youve-built">Part 7: The Platform Maturity Model — Measuring What You've Built</a></p>
</li>
<li><p><a href="#heading-best-practices-summary">Best Practices Summary</a></p>
</li>
<li><p><a href="#heading-resources">Resources</a></p>
</li>
</ul>
<h2 id="heading-what-youll-learn">What You'll Learn</h2>
<ul>
<li><p>The three-layer IDP architecture and why each layer must be implemented in a specific order</p>
</li>
<li><p>How to install and configure ArgoCD with ApplicationSets for multi-environment GitOps delivery</p>
</li>
<li><p>How to define cloud infrastructure as Kubernetes custom resources using Crossplane Compositions</p>
</li>
<li><p>How to deploy and configure Backstage with a software catalog and Software Templates</p>
</li>
<li><p>How to wire Backstage, ArgoCD, and Crossplane together into a single self-service golden path</p>
</li>
<li><p>How to implement cost attribution on your IDP so every resource provisioned through it carries team and cost center metadata</p>
</li>
<li><p>How to measure your IDP's maturity using the CNCF Platform Engineering Maturity Model</p>
</li>
</ul>
<p>Let's build it.</p>
<h2 id="heading-prerequisites">Prerequisites</h2>
<p>Before following along, you should have:</p>
<p><strong>Knowledge:</strong></p>
<ul>
<li><p>Working familiarity with Kubernetes: you can deploy applications, write YAML manifests, and understand namespaces and RBAC</p>
</li>
<li><p>Basic GitOps understanding: you know what "Git as source of truth" means in practice</p>
</li>
<li><p>Comfort with Helm, Terraform HCL, and TypeScript at a reading level</p>
</li>
<li><p>Understanding of AWS services: EKS, RDS, S3, IAM</p>
</li>
</ul>
<p><strong>Tools and access:</strong></p>
<ul>
<li><p>An EKS cluster running Kubernetes 1.28 or later with at least 3 nodes (m5.xlarge or equivalent)</p>
</li>
<li><p><code>kubectl</code> configured and pointing at your cluster</p>
</li>
<li><p><code>helm</code> 3.12 or later installed</p>
</li>
<li><p>AWS CLI v2 configured with admin-level permissions for the provisioning steps</p>
</li>
<li><p>Node.js 18 or later and Yarn (for Backstage)</p>
</li>
<li><p>A GitHub organisation you control (for the GitOps repositories and Backstage GitHub integration)</p>
</li>
</ul>
<p><strong>Companion repository:</strong></p>
<pre><code class="language-bash">git clone https://github.com/aayostem/platform-toolkit
cd platform-toolkit
</code></pre>
<p>The repository contains all manifests, Helm values files, Crossplane Compositions, and Backstage templates referenced in this guide. Each part maps to a directory in the repo.</p>
<p><strong>Estimated time:</strong> The full implementation takes one to two days for an experienced platform engineer. Parts 1–3 can be completed in the morning and produce a working GitOps delivery layer.</p>
<h2 id="heading-part-1-idp-architecture-the-three-layer-model">Part 1: IDP Architecture — The Three-Layer Model</h2>
<h3 id="heading-11-what-an-idp-actually-is">1.1 What an IDP Actually Is</h3>
<p>An Internal Developer Platform isn't a tool. It's a product: a collection of tools, workflows, and abstractions that platform teams build and maintain so that application developers can move fast without managing infrastructure directly.</p>
<p>The distinction matters because it shapes every architectural decision. A tool is installed and configured. A product is designed for users, iterated based on feedback, and measured by whether those users actually adopt it. The platform teams that build the IDPs that developers love think like product managers, not system administrators.</p>
<p><a href="https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report">The DORA 2025 report</a> found that nearly 90% of enterprises now have some form of internal platform. But having a platform and having a platform that developers actually use are different things.</p>
<p>The survey found that developer satisfaction with internal platforms varied dramatically. And the gap between satisfied and unsatisfied teams correlated directly with whether the platform team treated the IDP as a product with a roadmap and user research, or as an infrastructure project with a ticket queue.</p>
<p>The three tools in this guide — Backstage, ArgoCD, and Crossplane — are the most widely adopted open-source stack for production IDPs in 2026. But the architecture that connects them matters as much as the tools themselves.</p>
<h3 id="heading-12-the-three-layer-architecture">1.2 The Three-Layer Architecture</h3>
<p>A production IDP has three distinct layers, each with a single responsibility:</p>
<pre><code class="language-plaintext">Layer 1: Developer Interface (Backstage)
├── Software catalog — inventory of all services, APIs, and resources
├── Software Templates — self-service forms that trigger provisioning workflows
├── TechDocs — documentation co-located with each catalog entity
└── Plugins — integrations with ArgoCD, Kubernetes, PagerDuty, Grafana

Layer 2: Delivery Layer (ArgoCD)
├── GitOps sync — continuous reconciliation of cluster state to Git
├── ApplicationSets — multi-environment deployment from a single definition
├── Rollout management — progressive delivery with health checks
└── Audit trail — every deployment change linked to a Git commit

Layer 3: Infrastructure Layer (Crossplane)
├── Composite Resources — cloud resources defined as Kubernetes CRDs
├── Compositions — templates that expand a simple claim into full AWS infrastructure
├── ProviderConfigs — credentials and region configuration for each cloud provider
└── Usage tracking — every provisioned resource tagged with team and cost centre
</code></pre>
<p>The critical architectural rule: Backstage never talks directly to Kubernetes or cloud APIs. When a developer submits a Software Template in Backstage, the output is a Git commit — a YAML file representing a Crossplane claim or an ArgoCD Application manifest. ArgoCD picks up that commit and applies it to the cluster. Crossplane translates the cluster resource into actual cloud infrastructure.</p>
<p>This indirect path isn't complexity for complexity's sake. It means every infrastructure change is a Git commit, with an author, a timestamp, a pull request, and a review. The audit trail is automatic. The rollback mechanism is <code>git revert</code>.</p>
<pre><code class="language-plaintext">Developer → Backstage Template → Git commit → ArgoCD → Crossplane → AWS
                                     ↑
                          Single source of truth
                          Full audit trail
                          Rollback = git revert
</code></pre>
<p>Here's what the incorrect alternative looks like — Backstage calling cloud APIs directly:</p>
<pre><code class="language-typescript">// Bad: Backstage template calling AWS SDK directly
// No audit trail, no rollback, no reconciliation loop
// If the call fails halfway, you have partial infrastructure with no record
import { S3Client, CreateBucketCommand } from "@aws-sdk/client-s3";

const client = new S3Client({ region: "us-east-1" });
await client.send(new CreateBucketCommand({ Bucket: bucketName }));
</code></pre>
<p>And the correct approach — Backstage outputting a Crossplane claim to Git:</p>
<pre><code class="language-yaml"># Good: Backstage template output — a Crossplane claim committed to Git
# ArgoCD applies it, Crossplane reconciles it, AWS creates the bucket
# Every step is tracked, auditable, and reversible
apiVersion: platform.cloudfrugal.com/v1alpha1
kind: S3Bucket
metadata:
  name: ${{ values.bucket_name }}
  namespace: ${{ values.team_namespace }}
  labels:
    team: ${{ values.team_name }}
    cost-centre: ${{ values.cost_centre }}
    environment: ${{ values.environment }}
spec:
  versioning: true
  encryption: AES256
  region: us-east-1
</code></pre>
<h3 id="heading-13-implementation-order">1.3 Implementation Order</h3>
<p>Build in this order. Deviating from it creates integration problems that are difficult to debug:</p>
<pre><code class="language-plaintext">Step 1: ArgoCD — the delivery foundation everything else depends on
Step 2: Crossplane — infrastructure control plane, delivered by ArgoCD
Step 3: Backstage — the portal, pointing at ArgoCD and Crossplane as backends
Step 4: Wire together — Software Templates that produce GitOps manifests
Step 5: FinOps layer — cost attribution metadata in every provisioned resource
</code></pre>
<h2 id="heading-part-2-argocd-the-gitops-foundation">Part 2: ArgoCD — The GitOps Foundation</h2>
<p>ArgoCD is a declarative continuous delivery tool for Kubernetes that implements the GitOps pattern. If you haven't used a GitOps tool before, the core idea is simple: your Git repository is the single source of truth for what should be running in your cluster, and ArgoCD continuously reconciles actual cluster state to match it.</p>
<p>If a developer manually changes a resource in the cluster, ArgoCD detects the drift and resyncs from Git. If Git changes, ArgoCD applies the change to the cluster. Human intervention isn't required, and is actively discouraged — the goal is a cluster whose state is always fully explained by what's in Git.</p>
<p>ArgoCD is a CNCF Graduated project, meaning it's production-ready and widely used. It runs as a set of pods in your cluster with a web UI, a CLI, and a REST API. Everything you need to manage deployments across multiple environments lives in one place.</p>
<h3 id="heading-21-installing-argocd">2.1 Installing ArgoCD</h3>
<pre><code class="language-bash"># Create the ArgoCD namespace
kubectl create namespace argocd

# Install ArgoCD using the official manifest
kubectl apply -n argocd \
  -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Wait for all pods to be running before proceeding
kubectl wait --for=condition=Ready pods \
  --all -n argocd --timeout=300s

# Get the initial admin password
argocd_password=$(kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d)

echo "ArgoCD initial password: $argocd_password"
echo "Save this somewhere secure before proceeding"

# Port-forward to access the ArgoCD UI locally
kubectl port-forward svc/argocd-server -n argocd 8080:443 &amp;

# Login via CLI
argocd login localhost:8080 \
  --username admin \
  --password "$argocd_password" \
  --insecure

# Change the password immediately
argocd account update-password \
  --current-password "$argocd_password" \
  --new-password "your-secure-password"
</code></pre>
<h3 id="heading-22-repository-structure-for-gitops">2.2 Repository Structure for GitOps</h3>
<p>The repository structure ArgoCD watches determines how you manage multiple environments. The pattern that scales best is environment-per-directory, with overlays managed by Kustomize.</p>
<p>Kustomize is a Kubernetes-native configuration management tool that lets you define a base configuration once and layer environment-specific overrides on top of it. This means your staging and production configurations share the same YAML structure but differ in replica counts, image tags, and resource limits.</p>
<pre><code class="language-plaintext">gitops-repo/
├── apps/
│   ├── base/                    # Shared configuration across all environments
│   │   ├── payment-api/
│   │   │   ├── deployment.yaml
│   │   │   ├── service.yaml
│   │   │   └── kustomization.yaml
│   │   └── user-api/
│   │       ├── deployment.yaml
│   │       ├── service.yaml
│   │       └── kustomization.yaml
│   └── overlays/
│       ├── staging/             # Staging-specific overrides
│       │   ├── payment-api/
│       │   │   └── kustomization.yaml   # Override: 1 replica, staging image tag
│       │   └── kustomization.yaml
│       └── production/          # Production-specific overrides
│           ├── payment-api/
│           │   └── kustomization.yaml   # Override: 3 replicas, pinned image tag
│           └── kustomization.yaml
└── infrastructure/
    ├── crossplane/              # Crossplane installation and providers
    ├── monitoring/              # Prometheus, Grafana
    └── ingress/                 # NGINX or ALB ingress controller
</code></pre>
<h3 id="heading-23-applicationsets-managing-multiple-environments">2.3 ApplicationSets — Managing Multiple Environments</h3>
<p>An ApplicationSet is an ArgoCD resource that generates multiple Application objects from a single template. Instead of creating one Application manifest per service per environment — which becomes unmanageable at scale — you define one ApplicationSet that covers all services across all environments. A matrix generator combines a list of environments with a Git directory scan to produce every combination automatically:</p>
<pre><code class="language-yaml"># applicationset-apps.yaml
# This single resource generates one ArgoCD Application
# for each combination of environment and application directory
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: platform-apps
  namespace: argocd
spec:
  generators:
    - matrix:
        generators:
          # Generator 1: environments
          - list:
              elements:
                - environment: staging
                  cluster: https://staging.eks.cluster.local
                - environment: production
                  cluster: https://production.eks.cluster.local

          # Generator 2: application directories in the overlay
          - git:
              repoURL: https://github.com/your-org/gitops-repo
              revision: HEAD
              directories:
                - path: apps/overlays/{{environment}}/*

  template:
    metadata:
      name: "{{environment}}-{{path.basename}}"
      labels:
        environment: "{{environment}}"
        app: "{{path.basename}}"
    spec:
      project: default
      source:
        repoURL: https://github.com/your-org/gitops-repo
        targetRevision: HEAD
        path: "apps/overlays/{{environment}}/{{path.basename}}"
      destination:
        server: "{{cluster}}"
        namespace: "{{path.basename}}"
      syncPolicy:
        automated:
          prune: true        # Delete resources removed from Git
          selfHeal: true     # Revert manual cluster changes
        syncOptions:
          - CreateNamespace=true
          - PrunePropagationPolicy=foreground
</code></pre>
<p>Verify the ApplicationSet is generating the expected Applications:</p>
<pre><code class="language-bash"># List all generated Applications
kubectl get applications -n argocd

# Expected output: one Application per environment per app
# staging-payment-api    Synced    Healthy
# staging-user-api       Synced    Healthy
# production-payment-api Synced    Healthy
# production-user-api    Synced    Healthy

# Check sync status for a specific application
argocd app get staging-payment-api
</code></pre>
<h3 id="heading-24-argocd-rbac-for-platform-teams">2.4 ArgoCD RBAC for Platform Teams</h3>
<p>In a multi-team IDP, different teams need different levels of access to ArgoCD. Application teams should be able to view and sync their own applications. Platform teams should have broader access. Nobody should have unrestricted cluster admin through ArgoCD.</p>
<p>The default policy is <code>readonly</code> — every authenticated user can see everything but change nothing:</p>
<pre><code class="language-yaml"># argocd-rbac-configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-rbac-cm
  namespace: argocd
data:
  policy.default: role:readonly
  policy.csv: |
    # Platform team: full access to all applications
    p, role:platform-team, applications, *, */*, allow
    p, role:platform-team, clusters, get, *, allow
    p, role:platform-team, repositories, *, *, allow

    # Application teams: sync and get their own namespace only
    p, role:app-team, applications, get, */staging-*, allow
    p, role:app-team, applications, sync, */staging-*, allow

    # Bind roles to GitHub teams
    g, your-org:platform-engineers, role:platform-team
    g, your-org:developers, role:app-team

  scopes: '[groups]'
</code></pre>
<h2 id="heading-part-3-crossplane-infrastructure-as-kubernetes-resources">Part 3: Crossplane — Infrastructure as Kubernetes Resources</h2>
<p>Crossplane is a CNCF Graduated open-source framework that extends Kubernetes into a universal infrastructure control plane.</p>
<p>The core idea: instead of managing cloud resources with separate tools like Terraform or CloudFormation that live outside your cluster, you define cloud resources — RDS databases, S3 buckets, VPCs, IAM roles — as Kubernetes custom resource definitions.</p>
<p>Once you apply a Crossplane resource to the cluster, Crossplane's controllers take over and reconcile the desired state to the actual AWS state, exactly the way Kubernetes reconciles a Deployment to a set of running pods.</p>
<p>The key abstraction Crossplane adds on top of that is the Composite Resource. A platform team defines a high-level <code>PostgreSQLDatabase</code> type that abstracts over the thirty-plus configuration fields an actual RDS instance requires.</p>
<p>Developers interact with the simple type. Crossplane expands it into the full AWS resource configuration behind the scenes, applying the platform team's security and operational standards automatically — standards that developers can't bypass because they never see the underlying fields.</p>
<h3 id="heading-31-installing-crossplane">3.1 Installing Crossplane</h3>
<p>Crossplane is delivered to your cluster by ArgoCD — the first integration between the two tools. By installing Crossplane through an ArgoCD Application rather than running <code>helm install</code> directly, you make Crossplane itself part of the GitOps-managed infrastructure. Any chan