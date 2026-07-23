---
source_url: https://www.freecodecamp.org/news/relaxation-and-its-role-in-vision-the-1977-phd-thesis-that-helped-shape-modern-ai-research/
ingested: 2026-07-21
sha256: 2e706a0dc0e66c0372e5fb9d4eb2feb9bbb182f3ee3c6b50af216bfb1263efc9
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>&quot;Relaxation and its Role in Vision&quot;: The 1977 PhD Thesis That Helped Shape Modern AI Research</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/relaxation-and-its-role-in-vision-the-1977-phd-thesis-that-helped-shape-modern-ai-research/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="When people think of Geoffrey Hinton, they usually think of backpropagation, Boltzmann Machines, Deep Belief Networks, or the deep learning revolution that transformed artificial intelligence. But few">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="&quot;Relaxation and its Role in Vision&quot;: The 1977 PhD Thesis That Helped Shape Modern AI Research">
    
        <meta property="og:description" content="When people think of Geoffrey Hinton, they usually think of backpropagation, Boltzmann Machines, Deep Belief Networks, or the deep learning revolution that transformed artificial intelligence. But few">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/relaxation-and-its-role-in-vision-the-1977-phd-thesis-that-helped-shape-modern-ai-research/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/f1fe2707-f951-401a-9b08-54c5e1c2a3d9.png">
    <meta property="article:published_time" content="2026-07-21T17:39:01.805Z">
    <meta property="article:modified_time" content="2026-07-21T17:39:01.805Z">
    
        <meta property="article:tag" content="AI">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="&quot;Relaxation and its Role in Vision&quot;: The 1977 PhD Thesis That Helped Shape Modern AI Research">
    
        <meta name="twitter:description" content="When people think of Geoffrey Hinton, they usually think of backpropagation, Boltzmann Machines, Deep Belief Networks, or the deep learning revolution that transformed artificial intelligence. But few">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/relaxation-and-its-role-in-vision-the-1977-phd-thesis-that-helped-shape-modern-ai-research/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/f1fe2707-f951-401a-9b08-54c5e1c2a3d9.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Mohammed Fahd Abrah">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="AI">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/f1fe2707-f951-401a-9b08-54c5e1c2a3d9.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/relaxation-and-its-role-in-vision-the-1977-phd-thesis-that-helped-shape-modern-ai-research/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-21T17:39:01.805Z",
	"dateModified": "2026-07-21T17:39:01.805Z",
	"keywords": "AI",
	"description": "When people think of Geoffrey Hinton, they usually think of backpropagation, Boltzmann Machines, Deep Belief Networks, or the deep learning revolution that transformed artificial intelligence.\nBut few",
	"headline": "&quot;Relaxation and its Role in Vision&quot;: The 1977 PhD Thesis That Helped Shape Modern AI Research",
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-21T17:39:01.805Z">
                            July 21, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/ai/">
                                #AI
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">&quot;Relaxation and its Role in Vision&quot;: The 1977 PhD Thesis That Helped Shape Modern AI Research</h1>
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
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/f1fe2707-f951-401a-9b08-54c5e1c2a3d9.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/f1fe2707-f951-401a-9b08-54c5e1c2a3d9.png" alt="&quot;Relaxation and its Role in Vision&quot;: The 1977 PhD Thesis That Helped Shape Modern AI Research" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>When people think of Geoffrey Hinton, they usually think of backpropagation, Boltzmann Machines, Deep Belief Networks, or the deep learning revolution that transformed artificial intelligence.</p>
<p>But few people look further back to the beginning of his research career.</p>
<p>In 1977, nearly a decade before the famous backpropagation paper, Hinton completed his PhD thesis at the University of Edinburgh titled "Relaxation and its Role in Vision." At first glance, it seems to be a thesis about computer vision and relaxation methods. That was exactly what I expected when I began reading it.</p>
<p>As I worked through the thesis, however, I realized that it was about much more than a vision algorithm. Many of the ideas that would later define Hinton's research were already taking shape. The terminology was different, the math was simpler, and neural networks hadn't yet become the focus of his work. But the same way of thinking was already there.</p>
<p>This review isn't a chapter-by-chapter summary of the thesis. Instead, it focuses on the ideas that stood out to me while reading it and explores how many of them reappeared in Hinton's later work. Some of these ideas became central to modern AI, while others remain surprisingly overlooked despite being discussed nearly fifty years ago.</p>
<p>Looking back, what impressed me most was not that the thesis predicted specific algorithms. It was that it introduced a consistent way of thinking about intelligence, perception, and computation that would continue to shape Hinton's research for decades.</p>
<p>I hope this review encourages more people to read this remarkable thesis, not simply as a historical document, but as the starting point of one of the most influential research journeys in artificial intelligence.</p>
<h2 id="heading-thesis-overview">Thesis Overview</h2>
<p>In this review, we'll explore Geoffrey Hinton's 1977 PhD thesis, "Relaxation and its Role in Vision", completed at the University of Edinburgh.</p>
<p>We'll begin by looking at the central problem Hinton set out to solve and the ideas that motivated his relaxation approach. From there, we'll explore how the thesis represents uncertainty, reasons about competing hypotheses, and searches for globally consistent interpretations.</p>
<p>Next, we'll examine the puppet program, the relaxation operator, the role of schemas and stored knowledge, the SETTLE system, and Hinton's comparisons with other approaches of the time. We'll also discuss the limitations he identified in his own method and why they mattered.</p>
<p>Finally, we'll look at how many of the ideas introduced in this thesis reappeared throughout Hinton's later work and helped shape the development of modern AI.</p>
<p>If you'd like to follow along, you can also read the original thesis:</p>
<p><a href="https://era.ed.ac.uk/items/02e3dc47-0325-4574-a4d9-b09c3063b4ee"><strong>Geoffrey Hinton. <em>Relaxation and its Role in Vision</em>. PhD thesis, University of Edinburgh, 1977.</strong></a></p>
<p>Here is an infographic gives a quick overview of Geoffrey Hinton's 1977 PhD thesis. It summarizes the main ideas, how the relaxation method works, its applications, its limitations, and why many of these ideas still matter today.</p>
<img src="https://cdn.hashnode.com/uploads/covers/69ce92860ff860b6de01ed93/255a53c5-2e86-4fa5-b80d-07deb770dda0.png" alt="Infographic summarizing Geoffrey Hinton's 1977 PhD thesis, Relaxation and Its Role in Vision. It highlights the thesis's main ideas, methodology, key findings, applications, limitations, and its influence on modern AI." style="display:block;margin:0 auto" width="1024" height="1536" loading="lazy">

<h2 id="heading-table-of-contents">Table of Contents:</h2>
<ul>
<li><p><a href="#heading-the-core-challenge-why-visual-systems-cant-afford-to-guess-too-soon">The Core Challenge: Why Visual Systems Can't Afford to Guess Too Soon</a></p>
</li>
<li><p><a href="#heading-the-first-appearance-of-thinking-as-optimization">The First Appearance of Thinking as Optimization</a></p>
</li>
<li><p><a href="#heading-vision-is-inference-not-pattern-matching">Vision Is Inference, Not Pattern Matching</a></p>
</li>
<li><p><a href="#heading-why-perception-requires-hypotheses">Why Perception Requires Hypotheses</a></p>
</li>
<li><p><a href="#heading-from-binary-decisions-to-degrees-of-belief">From Binary Decisions to Degrees of Belief</a></p>
</li>
<li><p><a href="#heading-distributed-computation-before-neural-networks">Distributed Computation Before Neural Networks</a></p>
</li>
<li><p><a href="#heading-parallelism-as-the-natural-way-to-compute">Parallelism as the Natural Way to Compute</a></p>
</li>
<li><p><a href="#heading-constraint-propagation">Constraint Propagation</a></p>
</li>
<li><p><a href="#heading-local-rules-can-produce-global-intelligence">Local Rules Can Produce Global Intelligence</a></p>
</li>
<li><p><a href="#heading-why-local-consistency-is-not-enough">Why Local Consistency Is Not Enough</a></p>
</li>
<li><p><a href="#heading-relaxation-as-a-way-of-reasoning">Relaxation as a Way of Reasoning</a></p>
</li>
<li><p><a href="#heading-the-importance-of-equilibrium">The Importance of Equilibrium</a></p>
</li>
<li><p><a href="#heading-from-symbolic-decisions-to-numerical-reasoning">From Symbolic Decisions to Numerical Reasoning</a></p>
</li>
<li><p><a href="#heading-why-perception-is-a-search-problem">Why Perception Is a Search Problem</a></p>
</li>
<li><p><a href="#heading-beyond-pattern-recognition-why-internal-representations-matter-more-than-the-final-output">Beyond Pattern Recognition: Why Internal Representations Matter More Than the Final Output</a></p>
</li>
<li><p><a href="#heading-the-importance-of-intermediate-and-hierarchical-representations">The Importance of Intermediate and Hierarchical Representations</a></p>
</li>
<li><p><a href="#heading-schemas-and-stored-knowledge">Schemas and Stored Knowledge</a></p>
</li>
<li><p><a href="#heading-the-settle-system">The SETTLE System</a></p>
</li>
<li><p><a href="#heading-uncertainty-and-ambiguity-as-the-foundation-of-reasoning">Uncertainty and Ambiguity as the Foundation of Reasoning</a></p>
</li>
<li><p><a href="#heading-the-whole-picture">The Whole Picture</a></p>
</li>
<li><p><a href="#heading-a-consistent-philosophy-across-five-decades">A Consistent Philosophy Across Five Decades</a></p>
</li>
<li><p><a href="#heading-permission-to-publish">Permission to Publish</a></p>
</li>
<li><p><a href="#heading-further-reading">Further Reading</a></p>
</li>
</ul>
<h2 id="heading-the-core-challenge-why-visual-systems-cant-afford-to-guess-too-soon">The Core Challenge: Why Visual Systems Can't Afford to Guess Too Soon</h2>
<p>Before exploring the ideas in Hinton's thesis, it helps to understand the problem he set out to solve. The opening chapter asks a deceptively simple question: <strong>How can a visual system choose the correct interpretation when a single image may support many plausible explanations?</strong></p>
<p>This is the central challenge of visual perception. Real-world scenes are often ambiguous or partially hidden, so a system can't afford to commit to one interpretation too early. A premature decision can introduce errors that spread through the rest of the reasoning process and lead to an incorrect understanding of the entire scene.</p>
<p>The real challenge is to keep multiple plausible interpretations alive until there is enough evidence to determine which one is most consistent.</p>
<p>Hinton argues that the common approaches of the 1970s didn't solve this problem. One approach, known as the <strong>principle of least commitment</strong>, delayed decisions by leaving information unspecified. According to Hinton, this simply postponed the real issue because it offered no way to compare competing hypotheses or determine how they should become consistent with one another.</p>
<p>Another approach assigned fixed meanings to low-level visual features. But since the meaning of a feature depends on its surrounding context, these rigid definitions often failed when objects were partially hidden or appeared in different situations.</p>
<p>The infographic below summarizes the central challenge Hinton identifies at the beginning of his thesis. Rather than committing to the first plausible interpretation of a visual scene, he argues that a vision system should maintain many competing hypotheses simultaneously and allow them to interact until they converge on a single, globally consistent explanation.</p>
<p>It also highlights two contemporary approaches that Hinton rejects, the <em>principle of least commitment</em> and <em>rigid feature semantics</em>, because, in his view, they avoid the core problem instead of solving it.</p>
<p>This framing establishes the motivation for the relaxation framework developed throughout the rest of the thesis.</p>
<img src="https://cdn.hashnode.com/uploads/covers/69ce92860ff860b6de01ed93/2e04e5d9-5ad0-4a2b-8e87-c117b28d6b34.png" alt="Infographic on Hinton 1977 PhD thesis explaining parallel relaxation." style="display:block;margin:0 auto" width="1536" height="1024" loading="lazy">

<h2 id="heading-the-first-appearance-of-thinking-as-optimization">The First Appearance of Thinking as Optimization</h2>
<p>One of the most interesting ideas in Hinton's thesis is that perception isn't a matter of instantly recognizing an object. Instead, he treats it as a process of finding the best explanation for what the eyes are seeing.</p>
<p>Rather than committing to a single interpretation from the start, the system considers many possible hypotheses at the same time. Some support each other, others compete, and their confidence changes as they interact. Through repeated updates, weak explanations gradually disappear while the strongest and most consistent interpretation emerges.</p>
<p>Although Hinton applies this idea to visual perception, the underlying principle reaches far beyond computer vision. It introduces a way of thinking about intelligence as an optimization problem: many possible explanations compete until the system settles on the one that best fits the available evidence.</p>
<p>Looking back, this idea feels surprisingly familiar. The same general philosophy later appeared in probabilistic inference, energy-based models, Conditional Random Fields (CRFs), Boltzmann Machines, and many other approaches where intelligence emerges by searching for the most consistent solution rather than making a single immediate decision.</p>
<h2 id="heading-vision-is-inference-not-pattern-matching">Vision Is Inference, Not Pattern Matching</h2>
<p>One idea that stands out throughout the thesis is Hinton's view of what it actually means to see. He argues that vision is not simply recognizing patterns or assigning an image to a category. Instead, perception is the process of building an internal explanation of the scene.</p>
<p>A visual system doesn't immediately know what it's looking at. It must decide which objects are present, how they relate to one another, and which interpretation best explains the available evidence. In other words, seeing is a process of inference, not just recognition.</p>
<p>Hinton also rejects the idea that perception works by simply comparing an input with a collection of stored templates. He argues that this view is too limited to explain how we understand complex and unfamiliar scenes.</p>
<p>Instead, perception is presented as a constructive process. The system builds an interpretation by combining evidence, relationships, and prior knowledge until a coherent explanation emerges. It's not retrieving an answer from memory but actively constructing one.</p>
<p>Reading this today is striking because it closely resembles ideas that became popular decades later. Modern generative models and latent variable methods are also built around the idea of explaining observations by inferring the hidden structure that produced them.</p>
<p>These ideas also feel remarkably close to modern representation learning, where the goal isn't to memorize examples but to learn meaningful internal representations that can explain new observations.</p>
<p>Hinton was exploring these ways of thinking in 1977, long before they became a central theme in modern AI.</p>
<h2 id="heading-why-perception-requires-hypotheses">Why Perception Requires Hypotheses</h2>
<p>Hinton argues that perception can't be a purely reactive process. A visual system often receives incomplete, ambiguous, or even misleading information, so it can't simply accept the first interpretation that comes to mind.</p>
<p>Instead, it must begin with several possible explanations. As more evidence is considered, some hypotheses become more convincing while others are weakened or rejected. The final interpretation is reached only after this process of evaluation and refinement.</p>
<p>Although Hinton doesn't describe it using modern Bayesian terminology, the underlying idea is remarkably similar. Rather than making an immediate decision, the system continuously updates its beliefs as evidence accumulates until the most consistent explanation remains.</p>
<h2 id="heading-from-binary-decisions-to-degrees-of-belief">From Binary Decisions to Degrees of Belief</h2>
<p>Another idea that feels remarkably modern is Hinton's decision to avoid treating hypotheses as simply true or false. Instead, every hypothesis is assigned a value between 0 and 1 that reflects how strongly the system currently believes it. As the relaxation process unfolds, these values are updated repeatedly until the most consistent interpretation stands out while the others gradually fade away.</p>
<p>Today, we use different terms for similar concepts, including probabilities, belief values, confidence scores, activations, and logits. The terminology has evolved over the years, but the underlying idea remains the same: intelligence often depends on representing uncertainty instead of making immediate, irreversible decisions.</p>
<p>The infographic below illustrates how Hinton's relaxation process operates after hypotheses have been assigned continuous belief values.</p>
<p>Rather than selecting a single answer immediately, the system repeatedly updates all competing hypotheses in parallel, using both numerical constraints and individual preferences until one coherent interpretation gradually emerges.</p>
<p>By replacing rigid yes-or-no decisions with continuous optimization, the relaxation framework makes it possible to search efficiently for a globally consistent solution.</p>
<img src="https://cdn.hashnode.com/uploads/covers/69ce92860ff860b6de01ed93/4ab39c8f-8a0d-41db-a2a5-3f0669c52010.png" alt="Infographic showing Hinton's idea of giving each hypothesis a confidence value between 0 and 1 instead of a true-or-false decision. It illustrates how these values are repeatedly updated until the most consistent interpretation remains." style="display:block;margin:0 auto" width="1536" height="1024" loading="lazy">

<h2 id="heading-distributed-computation-before-neural-networks">Distributed Computation Before Neural Networks</h2>
<p>One of the most forward-looking ideas in the thesis is that intelligence shouldn't depend on a single central controller making every decision. Instead, Hinton describes a system made up of many local hypotheses that interact with one another at the same time. Each contributes a small part of the final solution, and together they produce a coherent interpretation.</p>
<p>Instead of focusing on individual components, Hinton emphasizes how these connections allow information to flow through the system until a consistent interpretation emerges.</p>
<p>This way of thinking feels surprisingly familiar today. Modern neural networks are also built on the idea that complex behavior can emerge from the combined activity of many simple units rather than from one component directing the entire process.</p>
<p>The terminology is different from modern deep learning, but the emphasis on networks, interactions, and distributed computation is already clearly visible.</p>
<h2 id="heading-parallelism-as-the-natural-way-to-compute">Parallelism as the Natural Way to Compute</h2>
<p>Another idea that stands out is Hinton's emphasis on parallel computation. At a time when most computers were designed to execute instructions one after another, he argued that perception is better viewed as many processes working simultaneously and influencing one another.</p>
<p>Looking back, this was an unusually forward-looking perspective. Decades before massively parallel hardware became common, Hinton was already describing computation in a way that closely resembles how modern neural networks run today, with many simple operations happening at the same time rather than one step after another.</p>
<h2 id="heading-constraint-propagation">Constraint Propagation</h2>
<p>A recurring idea throughout the thesis is that no hypothesis should be evaluated in isolation. Instead, each one influences the others through a network of constraints. When the confidence of one hypothesis changes, that change spreads across the network, strengthening compatible explanations and weakening conflicting ones.</p>
<p>This idea later became a common theme in several areas of AI. Graphical models, factor graphs, message passing, and belief propagation all rely on the same basic intuition: local interactions can gradually lead to a globally consistent solution.</p>
<p>Although these methods were developed later and use different mathematical frameworks, it's not difficult to see the conceptual connection.</p>
<p>To demonstrate how constraints interact during relaxation, Hinton chose a deliberately simplified vision problem instead of real photographs.</p>
<p>A user first drew several transparent, overlapping rectangles on a graphics terminal. Some rectangles represented genuine parts of a stick-figure puppet, such as the torso, arms, or legs, while others acted as irrelevant distractors.</p>
<p>Every overlap between rectangles became a candidate joint, and the system generated competing hypotheses about which rectangles belonged to the puppet and which overlaps represented real connections. Its goal was to identify the interpretation with the greatest number of mutually consistent instantiated joints, while remaining robust to missing body parts and irrelevant clutter.</p>
<p>By removing the complexity of natural images, Hinton isolated the combinatorial challenge of visual interpretation while keeping the problem mathematically manageable.</p>
<p>The infographic below illustrates how Hinton used this simplified puppet domain to evaluate the relaxation framework. By reducing vision to identifying consistent body parts and joints, the example isolates the core challenge of combining many competing local hypotheses into a single globally consistent interpretation.</p>
<p>Although intentionally simple, the puppet experiment captures the essential reasoning problem of computer vision: many local hypotheses compete simultaneously, constraints propagate between them, and only the globally most consistent interpretation survives.</p>
<p>Hinton presents the domain as a controlled laboratory for studying these interactions before extending the same relaxation principles to more realistic vision problems.</p>
<img src="https://cdn.hashnode.com/uploads/covers/69ce92860ff860b6de01ed93/f62ac4d9-75bb-448a-9485-b3bf8ee26284.png" alt="Infographic showing Hinton's puppet test problem, where overlapping rectangles represent possible body parts. The system uses constraints and relaxation to identify the combination of rectangles that forms the most consistent stick-figure puppet." style="display:block;margin:0 auto" width="1536" height="1024" loading="lazy">

<h2 id="heading-local-rules-can-produce-global-intelligence">Local Rules Can Produce Global Intelligence</h2>
<p>One of the ideas I enjoyed most in this thesis is how a complex solution emerges from simple local interactions. Each hypothesis only needs to communicate with the hypotheses directly connected to it. There's no central component that knows the correct answer or controls the entire process.</p>
<p>As information flows through the network, the system gradually settles on a consistent interpretation. The final result emerges from cooperation rather than command.</p>
<p>This same principle continues to appear throughout AI research. Neural networks, swarm intelligence, graph neural networks, and belief propagation all demons