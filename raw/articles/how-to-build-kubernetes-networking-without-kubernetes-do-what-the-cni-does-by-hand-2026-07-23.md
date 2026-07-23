---
source_url: https://www.freecodecamp.org/news/how-to-build-kubernetes-networking-without-kubernetes-do-what-the-cni-does-by-hand/
ingested: 2026-07-23
sha256: 16069428789f727cd7008e8bac44ef97ad57e50cd1c78a65b99fe40c69616195
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Build Kubernetes Networking Without Kubernetes: Do What the CNI Does By Hand</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-to-build-kubernetes-networking-without-kubernetes-do-what-the-cni-does-by-hand/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="In this article, you&#39;ll build an accurate mental model of what a Container Network Interface (CNI) actually does. Not by reading YAML, but by doing every single step it does by hand with raw Linux ker">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Build Kubernetes Networking Without Kubernetes: Do What the CNI Does By Hand">
    
        <meta property="og:description" content="In this article, you&#39;ll build an accurate mental model of what a Container Network Interface (CNI) actually does. Not by reading YAML, but by doing every single step it does by hand with raw Linux ker">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-to-build-kubernetes-networking-without-kubernetes-do-what-the-cni-does-by-hand/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8fc3683f-15c8-45ff-8424-bb1b427f68e2.png">
    <meta property="article:published_time" content="2026-07-22T23:15:29.968Z">
    <meta property="article:modified_time" content="2026-07-22T23:15:29.968Z">
    
        <meta property="article:tag" content="Kubernetes">
    
        <meta property="article:tag" content="networking">
    
        <meta property="article:tag" content="cni">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Build Kubernetes Networking Without Kubernetes: Do What the CNI Does By Hand">
    
        <meta name="twitter:description" content="In this article, you&#39;ll build an accurate mental model of what a Container Network Interface (CNI) actually does. Not by reading YAML, but by doing every single step it does by hand with raw Linux ker">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-to-build-kubernetes-networking-without-kubernetes-do-what-the-cni-does-by-hand/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8fc3683f-15c8-45ff-8424-bb1b427f68e2.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Shubham Katara">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="Kubernetes, networking, cni">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8fc3683f-15c8-45ff-8424-bb1b427f68e2.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-to-build-kubernetes-networking-without-kubernetes-do-what-the-cni-does-by-hand/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-22T23:15:29.968Z",
	"dateModified": "2026-07-22T23:15:29.968Z",
	"keywords": "Kubernetes, networking, cni",
	"description": "In this article, you&#x27;ll build an accurate mental model of what a Container Network Interface (CNI) actually does. Not by reading YAML, but by doing every single step it does by hand with raw Linux ker",
	"headline": "How to Build Kubernetes Networking Without Kubernetes: Do What the CNI Does By Hand",
	"author": {
		"@type": "Person",
		"name": "Shubham Katara",
		"url": "https://www.freecodecamp.org/news/author/katara/",
		"sameAs": [
			"https://katara.hashnode.dev"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/res/hashnode/image/upload/v1675689472065/wxn78xg7Q.jfif",
			"width": 450,
			"height": 450
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-22T23:15:29.968Z">
                            July 22, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/kubernetes/">
                                #Kubernetes
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Build Kubernetes Networking Without Kubernetes: Do What the CNI Does By Hand</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/res/hashnode/image/upload/v1675689472065/wxn78xg7Q.jfif 60w" sizes="60px" src="https://cdn.hashnode.com/res/hashnode/image/upload/v1675689472065/wxn78xg7Q.jfif" class="author-profile-image" alt="Shubham Katara" width="450" height="450" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/katara/" data-test-label="profile-link">
                    
                        Shubham Katara
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8fc3683f-15c8-45ff-8424-bb1b427f68e2.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8fc3683f-15c8-45ff-8424-bb1b427f68e2.png" alt="How to Build Kubernetes Networking Without Kubernetes: Do What the CNI Does By Hand" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>In this article, you'll build an accurate mental model of what a Container Network Interface (CNI) actually does. Not by reading YAML, but by doing every single step it does by hand with raw Linux kernel primitives.</p>
<p>The Container Network Interface (CNI) is one of the great black boxes of Kubernetes. Most people who run clusters every day have never once looked inside it. They know the <em>name</em> of their CNI ("we run Calico," "we're on Cilium") the way you know the brand of the alternator in your car: as a label, not as a thing you actually understand.</p>
<p>It lives at the very bottom of the stack, beneath the kubelet, beneath your pods, quietly moving every single packet. And precisely because it never fails loudly on a good day, almost nobody learns what it does.</p>
<p>We won't run <code>helm install cilium</code>. We won't apply a single manifest. Instead, we'll wire up pod networking from scratch, feel exactly where it breaks the moment traffic tries to leave a physical machine, and fix it manually.</p>
<p>By the end, you'll understand it in your bones, not just in theory, why tools like Cilium exist and what they're really solving under the hood.</p>
<p><strong>Who this is for:</strong></p>
<ul>
<li><p>Developers, platform engineers, and SREs who use Kubernetes every day but quietly treat pod-to-pod networking as magic.</p>
</li>
<li><p>Anyone who has ever watched a pod flip to <code>Running</code> and assumed the network "just works" and wants to know what's actually happening.</p>
</li>
</ul>
<p><strong>What you'll build with your own hands:</strong></p>
<ul>
<li><p>Two isolated network namespaces wired together with a virtual cable (<code>veth</code> pair).</p>
</li>
<li><p>A three-namespace virtual switch using a Linux bridge, the same trick legacy CNIs use on a single node.</p>
</li>
<li><p>A deliberately broken two-node setup where a packet gets dropped on the floor, plus the manual fix that makes it work.</p>
</li>
<li><p>A clear picture of the three jobs every CNI does, and why cloud providers force advanced CNIs like Cilium to use overlays and eBPF.</p>
</li>
</ul>
<p><strong>Note:</strong> Every command here needs a Linux host and <code>root</code>. Run this in a throwaway VM or lab environment, not on anything you care about. The whole point is to make a mess and learn from it.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-prerequisites">Prerequisites</a></p>
</li>
<li><p><a href="#heading-the-illusion-kubernetes-routes-zero-packets">The Illusion: Kubernetes Routes Zero Packets</a></p>
</li>
<li><p><a href="#heading-the-foundation-virtual-ethernet-veth-pairs">The Foundation: Virtual Ethernet (veth) Pairs</a></p>
</li>
<li><p><a href="#heading-how-to-scale-locally-with-a-linux-bridge">How to Scale Locally with a Linux Bridge</a></p>
</li>
<li><p><a href="#heading-the-multi-node-boundary-problem">The Multi-Node Boundary Problem</a></p>
</li>
<li><p><a href="#heading-how-to-fix-it-manually-with-direct-routing">How to Fix It Manually with Direct Routing</a></p>
</li>
<li><p><a href="#heading-so-what-is-a-cni-really">So What Is a CNI, Really?</a></p>
</li>
<li><p><a href="#heading-the-cloud-catch-and-why-cilium-changes-the-game">The Cloud Catch and Why Cilium Changes the Game</a></p>
</li>
<li><p><a href="#heading-conclusion">Conclusion</a></p>
</li>
</ul>
<h2 id="heading-prerequisites">Prerequisites</h2>
<p>Before following along, you'll need:</p>
<ul>
<li><p>Two Linux VMs on the same network for the multi-node section so you can watch traffic cross a real machine boundary.</p>
</li>
<li><p>The <code>ip</code> command from the <code>iproute2</code> package (already installed on virtually every modern distro).</p>
</li>
<li><p>A basic comfort with IP addresses, subnets, and the word "gateway." You don't need to be a network engineer.</p>
</li>
<li><p><strong>No Kubernetes.</strong> That's not a typo. We're going underneath Kubernetes on purpose.</p>
</li>
</ul>
<h2 id="heading-the-illusion-kubernetes-routes-zero-packets">The Illusion: Kubernetes Routes Zero Packets</h2>
<p>Here's the uncomfortable truth most people never confront: <strong>Kubernetes can't route a single network packet.</strong></p>
<p>Not one. Kubernetes is a orchestrator. It schedules pods, watches their health, and updates state in etcd. But when it comes to actually moving a packet from one container to another, it has zero built-in capability. None.</p>
<p>So how do your pods talk to each other? They rely completely on an external agent to wire up the virtual network plumbing on every node. That agent is the <strong>Container Network Interface (CNI)</strong>. What the CNI does under the hood quietly, is what we would do ourselves to feel the pain and then the solution a CNI provides.</p>
<p>Here's the proof that it's load-bearing. Spin up a brand-new cluster with <code>kubeadm</code> and look at your nodes:</p>
<pre><code class="language-bash">$ kubectl get nodes
NAME       STATUS     ROLES                  AGE   VERSION   INTERNAL-IP     EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION                        CONTAINER-RUNTIME
no-cni     NotReady   control-plane,master   52s   v1.35.0   192.168.117.2   &lt;none&gt;        Ubuntu 24.04.3 LTS   7.0.11-orbstack-00360-gc9bc4d96ac70   containerd://2.1.6
worker-1   NotReady   &lt;none&gt;                 46s   v1.35.0   192.168.117.3   &lt;none&gt;        Ubuntu 24.04.3 LTS   7.0.11-orbstack-00360-gc9bc4d96ac70   containerd://2.1.6
worker-2   NotReady   &lt;none&gt;                 40s   v1.35.0   192.168.117.4   &lt;none&gt;        Ubuntu 24.04.3 LTS   7.0.11-orbstack-00360-gc9bc4d96ac70   containerd://2.1.6
</code></pre>
<p><code>NotReady</code>. Every node. The control plane is healthy, etcd is up, the scheduler is alive, and the cluster still flatly refuses to be <code>Ready</code>. If you describe the node, it tells you precisely what's missing:</p>
<pre><code class="language-plaintext">Conditions:
  Type             Status  LastHeartbeatTime                 LastTransitionTime                Reason                       Message
  ----             ------  -----------------                 ------------------                ------                       -------
  Ready            False   Sat, 18 Jul 2026 10:25:51 +0200   Sat, 18 Jul 2026 10:25:20 +0200   KubeletNotReady              container runtime network not ready: NetworkReady=false reason:NetworkPluginNotReady message:Network plugin returns error: cni plugin not initialized
</code></pre>
<p>Read that again: <strong>your cluster is not</strong> <code>Ready</code> <strong>until you install a CNI.</strong> Not "mostly ready." Not "ready except for networking." <code>NotReady</code>, full stop. Until an external plugin shows up and takes responsibility for the packets Kubernetes itself refuses to touch.</p>
<p>A cluster without a CNI is a telephone exchange with no lines plugged in: every operator is present and ready, but not a single call is able to connect.</p>
<p>So what do most people do at this exact moment? They copy one line from a getting-started page:</p>
<pre><code class="language-bash">kubectl apply -f https://.../calico.yaml
</code></pre>
<p>They watch the nodes flip to <code>Ready</code>, and they move on. That's the entire relationship most engineers have with the single component that makes their cluster work. They wing it. It works, so they never ask what "it" is.</p>
<p>This matters because "the network just works" is a dangerous story to tell yourself. The moment something breaks (a pod can't reach a service, cross-node traffic vanishes, a cloud migration mysteriously blackholes packets), you're standing in front of a system you never actually understood. So let's understand it. From the bottom up.</p>
<h2 id="heading-the-foundation-virtual-ethernet-veth-pairs">The Foundation: Virtual Ethernet (veth) Pairs</h2>
<p>To understand container networking, you first have to understand how Linux isolates it.</p>
<p>When a container (or a Kubernetes pod) is created, the kernel wraps it in an isolated <strong>Network Namespace</strong> (<code>netns</code>). Think of a fresh network namespace as an island with no bridges to the mainland. By default it's completely blind to the outside world: no interfaces, no IP addresses, and no routing tables. It can't talk to anything, and nothing can talk to it.</p>
<img src="https://cdn.hashnode.com/uploads/covers/63d79ac66a29d3450a1f08f7/9acf8795-df14-49e3-ad68-900308ae51a0.png" alt="A new network namespace is an island: disconnected from everything." style="display:block;margin:0 auto" width="1536" height="1024" loading="lazy">

<p>So how do we get off the island? With a kernel primitive called a <strong>Virtual Ethernet (</strong><code>veth</code><strong>) pair</strong>.</p>
<p>A <code>veth</code> pair is a virtual network cable. Whatever packet enters one end immediately pops out the other end, even if the two ends live in different namespaces. Plug one end into the island and the other end into the mainland, and suddenly you have a connection.</p>
<p>Let's wire two isolated namespaces, <code>red</code> and <code>blue</code>, directly together.</p>
<pre><code class="language-bash"># Step 1: Create the isolated network namespaces
sudo ip netns add red
sudo ip netns add blue

# Step 2: Create the virtual ethernet cable (veth pair)
sudo ip link add veth-red type veth peer name veth-blue

# Step 3: Move each end of the cable into its namespace
sudo ip link set veth-red netns red
sudo ip link set veth-blue netns blue

# Step 4: Assign IP addresses and bring the interfaces UP
sudo ip netns exec red ip addr add 10.0.0.1/24 dev veth-red
sudo ip netns exec red ip link set veth-red up

sudo ip netns exec blue ip addr add 10.0.0.2/24 dev veth-blue
sudo ip netns exec blue ip link set veth-blue up
</code></pre>
<p>Now test the connection by pinging <code>blue</code> from inside <code>red</code>:</p>
<pre><code class="language-bash">sudo ip netns exec red ping -c 2 10.0.0.2
</code></pre>
<img src="https://cdn.hashnode.com/uploads/covers/63d79ac66a29d3450a1f08f7/33c0c06b-60a2-4ad5-b2ec-2d6acf08b922.png" alt="A new network namespace is an island: now connected with mainland using veth pairs." style="display:block;margin:0 auto" width="1536" height="1024" loading="lazy">

<p>In the end, it would look something like this:</p>
<ul>
<li><p>Isolation broken safely: The container transitions from an unreachable, isolated namespace (no IP, no routing) to an addressable endpoint (10.1.1.2) linked directly to the host network.</p>
</li>
<li><p>Bi-directional traffic flow: Packets originating inside the container can reach external public IP networks, and incoming response packets from the internet can traverse back through the host's eth0 interface (192.168.1.10) directly into the container's veth pairs.</p>
</li>
<li><p>Zero-latency in-kernel bridging: The veth pair (veth-island &lt;--&gt; veth-mainland) acts as a direct virtual pipe, allowing instant packet transit between distinct Linux network namespaces (netns) without requiring external physical hardware .</p>
</li>
</ul>
<p><strong>The verdict:</strong> the ping succeeds. You just manually wired two isolated environments together with nothing but a virtual cable.</p>
<p>But here's the problem with this approach: it scales horribly. It does not scale well because a <code>veth</code> pair is strictly point to point.</p>
<p>Following is the number of pairs need to be configured for the number of containers:</p>
<ul>
<li><p>2 containers: 1 pair</p>
</li>
<li><p>3 containers: 3 pairs</p>
</li>
<li><p>4 containers: 6 cables</p>
</li>
</ul>
<p>For ten, you'd need 45 cables to connect every pair.</p>
<ul>
<li><p>Explodes in cable count: The number of veth pairs grow quadratically as containers increase</p>
</li>
<li><p>Complex to manage: Too many interfaces, routes and rules to configure and maintain.</p>
</li>
</ul>
<img src="https://cdn.hashnode.com/uploads/covers/63d79ac66a29d3450a1f08f7/c20651dd-8932-46bb-8e1b-b99846f56854.png" alt="Image illustrating the problem with single veth pairs at scale" style="display:block;margin:0 auto" width="1536" height="1024" loading="lazy">

<p>This is the same reason data centers don't run a physical cable between every pair of servers. You need a switch.</p>
<h2 id="heading-how-to-scale-locally-with-a-linux-bridge">How to Scale Locally with a Linux Bridge</h2>
<p>When you need to connect more than two interfaces on a single host, you stop running cables between everything and plug everything into a central hub instead. In the Linux kernel, that hub is a <strong>Linux Bridge</strong>. It's a software Layer 2 virtual switch (you'll often see it named <code>br0</code> or <code>cni0</code>).</p>
<p>A bridge does exactly what a physical switch does: it learns MAC addresses and forwards frames across every connected interface in the same broadcast domain.</p>
<p>The pattern changes slightly. Instead of connecting namespaces directly to each other, you attach one end of a <code>veth</code> pair to the namespace, and plug the <em>other</em> end into the host's bridge.</p>
<img src="https://cdn.hashnode.com/uploads/covers/63d79ac66a29d3450a1f08f7/c70ac344-0c3b-46ef-8e6f-f81bc52224df.png" alt="Image showing how veth pairs connect islands to mainland via Linux bridge" style="display:block;margin:0 auto" width="1536" height="1024" loading="lazy">

<p>Let's tear down the old setup and build a three-namespace switch: <code>red</code>, <code>blue</code>, and <code>green</code>. They'll all share one broadcast domain.</p>
<pre><code class="language-bash"># Clean up any previous configuration
sudo ip netns del red 2&gt;/dev/null || true
sudo ip netns del blue 2&gt;/dev/null || true
sudo ip netns del green 2&gt;/dev/null || true
sudo ip link del br0 2&gt;/dev/null || true

# Step 1: Create the host switch (bridge) and bring it up
sudo ip link add br0 type bridge
sudo ip link set br0 up

# Step 2: Wire namespace 1 (red) into the bridge
sudo ip netns add red
sudo ip link add veth-red type veth peer name veth-red-host
sudo ip link set veth-red netns red
sudo ip link set veth-red-host master br0
sudo ip link set veth-red-host up
sudo ip netns exec red ip addr add 10.0.0.1/24 dev veth-red
sudo ip netns exec red ip link set veth-red up

# Step 3: Wire namespace 2 (blue) into the bridge
sudo ip netns add blue
sudo ip link add veth-blue type veth peer name veth-blue-host
sudo ip link set veth-blue netns blue
sudo ip link set veth-blue-host master br0
sudo ip link set veth-blue-host up
sudo ip netns exec blue ip addr add 10.0.0.2/24 dev veth-blue
sudo ip netns exec blue ip link set veth-blue up

# Step 4: Wire namespace 3 (green) into the bridge
sudo ip netns add green
sudo ip link add veth-green type veth peer name veth-green-host
sudo ip link set veth-green netns green
sudo ip link set veth-green-host master br0
sudo ip link set veth-green-host up
sudo ip netns exec green ip addr add 10.0.0.3/24 dev veth-green
sudo ip netns exec green ip link set veth-green up
</code></pre>
<p>Because all three namespaces are connected to the shared <code>br0</code> device, they can communicate freely with each other across the virtual network switch. But how do they actually "find" each other on the network? This is where ARP comes in.</p>
<p><strong>ARP</strong> stands for Address Resolution Protocol. It's a fundamental part of local networking. When one computer (or namespace, in our case) wants to talk to another using an IP address, it needs to discover the other computer's hardware address (called a MAC address) to actually send packets on the network.</p>
<p>ARP is the system that allows this to happen — it sends out a broadcast asking "Who has IP address X? Please tell me your MAC address," and the right system answers back.</p>
<p>Thanks to ARP, all the namespaces plugged into <code>br0</code> can learn each other's MAC addresses automatically and send packets directly within their shared network segment. Let's prove it by pinging every pair, both ways:</p>
<pre><code class="language-bash"># red reaches blue and green
sudo ip netns exec red ping -c 1 10.0.0.2
sudo ip netns exec red ping -c 1 10.0.0.3

# blue reaches red and green
sudo ip netns exec blue ping -c 1 10.0.0.1
sudo ip netns exec blue ping -c 1 10.0.0.3

# green reaches red and blue
sudo ip netns exec green ping -c 1 10.0.0.1
sudo ip netns exec green ping -c 1 10.0.0.2
</code></pre>
<p>All six pings succeed. And notice there isn't a single routing rule involved anywhere. Every namespace lives in the same <code>10.0.0.0/24</code> subnet on the same Layer 2 switch, so the kernel resolves the whole mesh with plain ARP.</p>
<p>This is <em>exactly</em> how legacy single-node CNIs (the old <code>kubenet</code>) operate. On one machine, it's clean and simple.</p>
<p>But Kubernetes is a distributed system designed to scale across thousands of physical machines. So here's the question that breaks everything: what happens when our namespaces need to leave the host?</p>
<h2 id="heading-the-multi-node-boundary-problem">The Multi-Node Boundary Problem</h2>
<p>Everything so far has lived on one machine. Kubernetes doesn't. So let's do the honest thing: stand up two real VMs and watch the single-node trick fall apart. Don't take my word for it: build this and watch the packet die.</p>
<p>Here's the setup:</p>
<ul>
<li><p><strong>VM 1</strong> (host IP <code>10.1.44.216</code>): home to the <code>red</code> namespace, pod subnet <code>10.0.1.0/24</code>.</p>
</li>
<li><p><strong>VM 2</strong> (host IP <code>10.1.44.178</code>): home to the <code>blue</code> namespace, pod subnet <code>10.0.2.0/24</code>.</p>
</li>
</ul>
<p>Two things to notice before we start. First, each node gets its <strong>own</strong> pod subnet (<code>10.0.1.0/24</code> on VM 1, <code>10.0.2.0/24</code> on VM 2) because if both nodes handed out <code>10.0.0.x</code> addresses, you'd get IP collisions the instant two pods landed on the same number.</p>
<p>Second, because the subnets now differ, each namespace needs a <strong>gateway</strong> to route through, and that gateway is its own host's bridge.</p>
<p><strong>Note:</strong> this is the <a href="http://cleanup-multinode.sh">cleanup-multinode.sh</a> script that should only be used in case you make any errors while setting up the cross node routes and veth pairs.</p>
<pre><code class="language-shell">#!/usr/bin/env bash
#
# cleanup-multinode.sh
# Tears down the manual multi-node CNI lab (bridge + namespaces + veth
# pairs + cross-node static routes) from "Build a Mental Model for
# Kubernetes CNI by Doing It Manually."
#
# Safe to run on BOTH VMs. Every step is idempotent: anything that was
# never created on this host is skipped instead of erroring out, so
# re-running it is harmless.
#
# Usage:  sudo ./cleanup-multinode.sh
#
set -u

if [[ $EUID -ne 0 ]]; then
  echo "This script needs root. Run:  sudo $0" &gt;&amp;2
  exit 1
fi

echo "==&gt; Deleting network namespaces (this also destroys their veth pairs)..."
ip netns del red  2&gt;/dev/null &amp;&amp; echo "    - removed netns 'red'"  || true
ip netns del blue 2&gt;/dev/null &amp;&amp; echo "    - removed netns 'blue'" || true

echo "==&gt; Removing any orphaned host-side veth interfaces..."
ip link del veth-red-host  2&gt;/dev/null &amp;&amp; echo "    - removed veth-red-host"  || true
ip link del veth-blue-host 2&gt;/dev/null &amp;&amp; echo "    - removed veth-blue-host" || true

echo "==&gt; Deleting the bridge..."
ip link del br0 2&gt;/dev/null &amp;&amp; echo "    - removed bridge 'br0'" || true

echo "==&gt; Removing cross-node static routes..."
ip route del 10.0.1.0/24 2&gt;/dev/null &amp;&amp; echo "    - removed route to 10.0.1.0/24" || true
ip route del 10.0.2.0/24 2&gt;/dev/null &amp;&amp; echo "    - removed route to 10.0.2.0/24" || true

echo "==&gt; Disabling IP forwarding (non-persistent; resets on reboot anyway)..."
sysctl -w net.ipv4.ip_forward=0 &gt;/dev/null

# --- Optional: undo the 'Common Gotchas' tweaks, ONLY if you applied them ---
# On a throwaway lab VM, leaving FORWARD at ACCEPT or rp_filter at 0 is
# usually harmless, so these are opt-in. Uncomment whatever you changed.
# sysctl -w net.ipv4.conf.all.rp_filter=1 &gt;/dev/null
# iptables -P FORWARD DROP

echo
echo "==&gt; Teardown complete. Verifying nothing is left behind:"
echo "--- namespaces (expect: no red/blue) ---"
out=$(ip netns list);                          echo "${out:-  (none)}"
echo "--- bridges (expect: no br0) ---"
out=$(ip -br link show type bridge 2&gt;/dev/null); echo "${out:-  (none)}"
echo "--- lab routes (expect: none) ---"
out=$(ip route | grep -E