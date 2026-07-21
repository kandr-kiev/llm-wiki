---
source_url: https://www.freecodecamp.org/news/why-it-worked-on-my-machine-still-happens-in-2026/
ingested: 2026-07-17
sha256: 14fc35dad962e2db471b34db5e2f813578adfea8d6cf3ab0339b3c36f2602a69
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>Why &quot;It Worked on My Machine&quot; Still Happens in 2026</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/why-it-worked-on-my-machine-still-happens-in-2026/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="Every engineering team has said it at least once: &quot;It works on my machine.&quot; The phrase has become a running joke in software, but it&#39;s rarely funny when it happens in production. A feature passes ever">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="Why &quot;It Worked on My Machine&quot; Still Happens in 2026">
    
        <meta property="og:description" content="Every engineering team has said it at least once: &quot;It works on my machine.&quot; The phrase has become a running joke in software, but it&#39;s rarely funny when it happens in production. A feature passes ever">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/why-it-worked-on-my-machine-still-happens-in-2026/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8435d1c8-af34-4cff-8891-087ac2a3ad9d.png">
    <meta property="article:published_time" content="2026-07-15T18:18:11.786Z">
    <meta property="article:modified_time" content="2026-07-15T18:18:11.786Z">
    
        <meta property="article:tag" content="software development">
    
        <meta property="article:tag" content="PaaS">
    
        <meta property="article:tag" content="deployment">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Why &quot;It Worked on My Machine&quot; Still Happens in 2026">
    
        <meta name="twitter:description" content="Every engineering team has said it at least once: &quot;It works on my machine.&quot; The phrase has become a running joke in software, but it&#39;s rarely funny when it happens in production. A feature passes ever">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/why-it-worked-on-my-machine-still-happens-in-2026/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8435d1c8-af34-4cff-8891-087ac2a3ad9d.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Manish Shivanandhan">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="software development, PaaS, deployment">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8435d1c8-af34-4cff-8891-087ac2a3ad9d.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/why-it-worked-on-my-machine-still-happens-in-2026/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-15T18:18:11.786Z",
	"dateModified": "2026-07-15T18:18:11.786Z",
	"keywords": "software development, PaaS, deployment",
	"description": "Every engineering team has said it at least once: &quot;It works on my machine.&quot;\nThe phrase has become a running joke in software, but it&#x27;s rarely funny when it happens in production.\nA feature passes ever",
	"headline": "Why &quot;It Worked on My Machine&quot; Still Happens in 2026",
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-15T18:18:11.786Z">
                            July 15, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/software-development/">
                                #software development
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">Why &quot;It Worked on My Machine&quot; Still Happens in 2026</h1>
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
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8435d1c8-af34-4cff-8891-087ac2a3ad9d.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8435d1c8-af34-4cff-8891-087ac2a3ad9d.png" alt="Why &quot;It Worked on My Machine&quot; Still Happens in 2026" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>Every engineering team has said it at least once: "It works on my machine."</p>
<p>The phrase has become a running joke in software, but it's rarely funny when it happens in production.</p>
<p>A feature passes every local test, the pull request gets approved, the deployment finishes successfully, and then users start reporting failures.</p>
<p>On-call engineers get paged. Incident channels fill up. A fix that took ten minutes to write takes four hours to trace back to a missing environment variable or a runtime version mismatch nobody noticed.</p>
<p>The strange part is that this still happens in 2026.</p>
<p>Modern development has better tooling than ever. Containers, automated testing, cloud infrastructure, CI/CD pipelines, infrastructure as code, and AI coding assistants have all made building software considerably faster.</p>
<p>And yet engineering teams running customer-facing applications continue to lose significant time chasing bugs that only appear outside a developer's laptop.</p>
<p>One <a href="https://queue.acm.org/detail.cfm?id=3068754/">industry survey</a> found that developers spend roughly 40% of their time on tasks unrelated to writing features,&nbsp; and environment debugging is a leading culprit.</p>
<p>The reason isn't that engineers are careless. Most software doesn't fail because of bad code. It fails because code runs inside an environment, and those environments are rarely identical.</p>
<p>The gap between a developer's laptop and a production cluster is still one of the most consistent sources of engineering waste these days.</p>
<p>The real question is no longer why this problem exists. Every experienced engineering team understands environment drift. The better question is why so many product teams are still spending engineering time managing it.</p>
<h3 id="heading-what-well-cover">What We'll Cover:</h3>
<ul>
<li><p><a href="#heading-every-machine-tells-a-slightly-different-story">Every Machine Tells a Slightly Different Story</a></p>
</li>
<li><p><a href="#heading-dependencies-are-moving-targets">Dependencies Are Moving Targets</a></p>
</li>
<li><p><a href="#heading-configuration-causes-more-incidents-than-code-does">Configuration Causes More Incidents Than Code Does</a></p>
</li>
<li><p><a href="#heading-the-real-cost-of-managing-multiple-environments">The Real Cost of Managing Multiple Environments</a></p>
</li>
<li><p><a href="#heading-why-are-teams-still-managing-this-themselves-in-2026">Why Are Teams Still Managing This Themselves in 2026?</a></p>
</li>
<li><p><a href="#heading-local-success-doesnt-reflect-production-conditions">Local Success Doesn't Reflect Production Conditions</a></p>
</li>
<li><p><a href="#heading-why-are-more-engineering-teams-choosing-managed-platforms">Why Are More Engineering Teams Choosing Managed Platforms?</a></p>
</li>
<li><p><a href="#heading-what-a-basic-paas-setup-actually-looks-like">What a Basic PaaS Setup Actually Looks Like</a></p>
</li>
<li><p><a href="#heading-consistency-is-an-ownership-question-not-a-tooling-question">Consistency is an Ownership Question, Not a Tooling Question</a></p>
</li>
</ul>
<h2 id="heading-every-machine-tells-a-slightly-different-story"><strong>Every Machine Tells a Slightly Different Story</strong></h2>
<p>A production application depends on much more than source code.</p>
<p>It depends on the operating system, runtime versions, environment variables, databases, third-party services, networking rules, file permissions, installed libraries, and CPU architecture.</p>
<p>A developer running Node.js 24 LTS may be pairing with a teammate still on 22. One laptop has a newer OpenSSL version installed as a transitive dependency update. Another has a cached <a href="https://www.incredibuild.com/glossary/build-artifacts">build artefact</a> from three months ago that quietly changed behaviour after a library patch.</p>
<p>None of these differences looks significant on their own. Together, they create a local environment that behaves differently from every other environment in the pipeline.</p>
<p>This is how a test suite passes green on a developer's machine and fails in CI twenty minutes later. It's how an application boots cleanly on macOS but crashes on the Debian container your cloud provider runs.</p>
<p>It's why a microservice that handled 500 requests per second last Tuesday starts timing out this Monday after what appeared to be an unrelated dependency bump.</p>
<p>The code hasn't changed. The environment has.</p>
<h2 id="heading-dependencies-are-moving-targets"><strong>Dependencies Are Moving Targets</strong></h2>
<p>Package managers have made software development productive, but they've also dramatically increased the surface area of a running application.</p>
<p>A typical Node.js web application today has between 500 and 1,500 packages in its dependency tree, including indirect dependencies, even when a developer explicitly installs only a handful.</p>
<p>A Python service using common data processing and web frameworks can pull in 200 to 400 packages. Most engineers have no direct relationship with the vast majority of packages their application ships.</p>
<p>When dependency versions aren't locked correctly, two developers installing the same project on the same day can receive materially different software stacks. Lock files like package-lock.json, pnpm-lock.yaml, poetry.lock, Cargo.lock&nbsp;exist precisely to prevent this, and they help. But they're one layer of control in a much larger consistency problem.</p>
<p>Runtime versions still differ. System libraries still differ. Base OS images in containers drift across patch cycles. A Docker image built from node:22 today isn't the same image that gets built in six weeks when the upstream tag has been updated. Teams that don't pin their base images precisely are unknowingly accepting environment drift at the foundation of every deployment.</p>
<h2 id="heading-configuration-causes-more-incidents-than-code-does"><strong>Configuration Causes More Incidents Than Code Does</strong></h2>
<p>Many of the most disruptive production incidents on engineering teams have nothing to do with programming logic.</p>
<p>They come from configuration.</p>
<p>An environment variable is missing in the new deployment target. A database connection string points to staging instead of production. A feature flag is set to true in the developer's .env file but defaults to false in the deployed service, silently disabling a critical code path. An API key was rotated but the secret manager reference was updated in one environment and not the other.</p>
<p>These mistakes are common, and genuinely difficult to prevent,&nbsp;because configuration lives outside the application. It's managed separately, documented inconsistently, and almost never covered by standard test suites.</p>
<p>Post-incident reviews regularly surface configuration drift as the root cause of outages that took hours to diagnose because the application code looked completely correct.</p>
<p>The problem compounds across environments. A team running development, staging, pre-production, and production has four separate configuration states to keep aligned.</p>
<p>When an engineer adds a new environment variable, that change has to propagate through every environment reliably. In practice, it often doesn't. One environment gets missed. An old value lingers. The application behaves differently, and the investigation starts from scratch.</p>
<h2 id="heading-the-real-cost-of-managing-multiple-environments"><strong>The Real Cost of Managing Multiple Environments</strong></h2>
<p>Engineering leadership often underestimates how much time is consumed by environment management, not because it's hard to observe, but because it's distributed across dozens of small tasks that never appear as line items.</p>
<p>Someone updates the Node runtime in the base Docker image and spends an afternoon chasing a downstream test failure that turned out to be a transitive dependency incompatibility.</p>
<p>Someone provisions a new staging environment and spends a day replicating the production configuration by hand. Someone rotates credentials, misses one service, and triggers a silent failure that takes until the next deployment cycle to surface. Someone joins the team and spends the first two days getting a local environment running instead of shipping work.</p>
<p>Estimates from engineering productivity research suggest that infrastructure and environment-related tasks consume between 15 - 25% of total engineering capacity at companies that own their own deployment infrastructure. For a team of ten engineers, that's effectively two to three people running hard and producing no customer-facing output.</p>
<p>This is the cost that doesn't appear on sprint boards. It lives in Slack threads, in incident retrospectives, and in the quiet acknowledgement that the team is slower than it should be.</p>
<p>None of this work appears on a roadmap. Customers never ask for it. It doesn’t create differentiation. Yet product teams spend hundreds of engineering hours every year maintaining consistency between environments simply to keep software deployable. Environment drift isn't just a reliability problem. It's an engineering capacity problem.</p>
<h2 id="heading-why-are-teams-still-managing-this-themselves-in-2026"><strong>Why Are Teams Still Managing This Themselves in 2026?</strong></h2>
<p>Given all of this, the reasonable question is why so many engineering teams are still owning this complexity directly.</p>
<p>Part of the answer is inertia. Teams that built their infrastructure several years ago, when Kubernetes was the obvious answer to every scaling question and "we control our own stack" felt like a competitive advantage, now maintain that infrastructure because changing it has a cost.</p>
<p>The investment is already made. The tooling is already familiar. The pain is distributed and chronic rather than acute, which makes it easier to absorb than to address.</p>
<p>Part of the answer is organisational habit. Hiring a platform or DevOps engineer to manage infrastructure feels like the right response to environmental problems. But that engineer becomes responsible for maintaining the consistency layer indefinitely. Patching base images, updating runtime versions, managing certificate renewals, and debugging networking issues across environments, rather than delivering product leverage.</p>
<p>Part of the answer is a belief that more control produces better outcomes. Running your own infrastructure gives complete visibility into every configuration decision.</p>
<p>But complete control also means complete responsibility. Every decision the platform team makes is a decision the platform team must maintain, document, and revisit every time something upstream changes.</p>
<p>Most product engineering teams aren't in the infrastructure business. They're in the business of building software for customers, and every hour spent on environment consistency is an hour not spent on that.</p>
<p>The honest answer is that many teams are managing this complexity themselves because they haven't yet found a clear path to stopping.</p>
<h2 id="heading-local-success-doesnt-reflect-production-conditions"><strong>Local Success Doesn't Reflect Production Conditions</strong></h2>
<p>One consistent failure mode is treating a passing local test as a signal that a deployment is safe.</p>
<p>Production environments impose conditions that development machines never encounter. A service that starts cleanly on a laptop with no concurrent users will behave differently when handling 2,000 requests per second with three application instances competing for a shared database connection pool.</p>
<p>A background job that completes in milliseconds locally may time out in production when it runs simultaneously with twelve other jobs against a database under real write load.</p>
<p>Staging environments exist to surface these differences before they reach users. But staging only provides value when it actually resembles production, like the same infrastructure, the same runtime versions, the same configuration shape, same network topology.</p>
<p>Many teams treat staging as a best-effort approximation. Over time, configuration drift between staging and production means that staging stops catching the failures it was designed to catch. Teams end up discovering environment-related issues in production anyway, which is the worst place to find them.</p>
<p>Maintaining genuine parity across three or four environments is expensive and requires continuous attention. Infrastructure updates must be applied uniformly. Runtime versions must stay synchronised. Configuration must be propagated reliably.</p>
<p>Without active discipline, staging drifts away from production, and the safety net disappears.</p>
<h2 id="heading-why-are-more-engineering-teams-choosing-managed-platforms"><strong>Why Are More Engineering Teams Choosing Managed Platforms?</strong></h2>
<p>At some point, every engineering organisation has to ask a more fundamental question. Should we keep investing engineering time into maintaining environments, or should we move that responsibility to a platform built for it?</p>
<p>This is the context in which <a href="https://www.freecodecamp.org/news/my-team-s-experience-moving-from-aws-to-a-paas/">Platform as a Service</a> has become a more serious consideration for teams that previously managed their own infrastructure.</p>
<p>A well-designed PaaS doesn't remove engineering responsibility. It relocates it.</p>
<p>Developers still write code. They still define environment variables and build processes. They still decide what their application needs. The difference is that the platform provides a consistent, maintained runtime across every environment like development, staging, and production, without the team owning the underlying infrastructure.</p>
<p>The same application definition runs everywhere. Environment parity becomes a property of the platform rather than a discipline the team has to enforce continuously.</p>
<p>This matters most to engineering teams with real deployment velocity, the teams shipping multiple times per day, running several services, and operating with the expectation that deployments are predictable.</p>
<p>When the platform standardises the environment, deployments stop being experiments. Engineers stop discovering production-only failures at the worst possible time.</p>
<p>The operational tradeoff is real. Some organisations require control over their infrastructure for compliance, regulatory, or architectural reasons that a PaaS can't accommodate. But many teams that believe they need that control have never closely examined the cost of maintaining it.</p>
<p>The question isn't whether owning infrastructure gives you control. It's whether that control is producing outcomes that justify the engineering capacity it consumes.</p>
<h2 id="heading-what-a-basic-paas-setup-actually-looks-like"><strong>What a Basic PaaS Setup Actually Looks Like</strong></h2>
<p>The argument for a managed platform is easier to evaluate with a concrete picture of what adopting one involves. The details vary across providers like Render, Railway, Sevalla, etc, but the setup's shape is remarkably consistent and smaller than most teams expect.</p>
<p><strong>Step 1: Connect your repository.</strong> Every mainstream PaaS starts from your Git repository. You authorise the platform against GitHub or GitLab, point it at a repo, and choose a branch to deploy from. From that moment, the platform watches for pushes. There's no CI pipeline to write for the basic case, since build-and-deploy on push is the default behaviour.</p>
<img src="https://cdn.hashnode.com/uploads/covers/66c6d8f04fa7fe6a6e337edd/46fdb46c-5b94-408c-ad69-bfca34992776.png" alt="Connect repository" style="display:block;margin:0 auto" width="1000" height="825" loading="lazy">

<p><strong>Step 2: Define the application, once, in a file.</strong> Instead of configuring servers, you describe what your application is: the runtime, the build command, the start command, and the services it needs. Most platforms let you do this through a dashboard, but the better practice is a declarative file that lives in the repo.</p>
<pre><code class="language-yaml">services:
  - type: web
    name: my-api
    runtime: node
    buildCommand: npm ci
    startCommand: npm run start
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: my-api-db
          property: connectionString
      - key: NODE_ENV
        value: production

databases:
  - name: my-api-db
    plan: basic
</code></pre>
<p>This file is the payoff of the whole model. It's the single source of truth for how the application runs, it's version-controlled alongside the code, and, critically, it's the <em>same definition</em> in every environment.</p>
<p>The drift described earlier in this article, where staging quietly diverges from production, has nowhere to live, because there is no second copy of the environment to fall out of sync.</p>
<p><strong>Step 3: Set your environment variables in the platform, not in files.</strong> Secrets and configuration move out of scattered <code>.env</code> files and into the platform's environment settings, scoped per environment.</p>
<img src="https://cdn.hashnode.com/uploads/covers/66c6d8f04fa7fe6a6e337edd/153f83a9-7aab-4f08-9f19-f6d73b7ccafa.png" alt="Environment variables" style="display:block;margin:0 auto" width="1000" height="293" loading="lazy">

<p>When an engineer adds a new variable, the platform surfaces it in one place rather than requiring a manual update across four deployment targets. Most platforms also support environment groups, so shared configuration is defined once and inherited.</p>
<p><strong>Step 4: Attach managed services.</strong> Databases, caches, and cron jobs are provisioned by the platform rather than installed and patched by your team.</p>
<p>In the example above, the database is declared in the same file as the application, and its connection string is injected automatically, so there's no connection string to copy incorrectly into staging.</p>
<p><strong>Step 5: Push, and let preview environments do the rest.</strong> This is where the parity argument becomes tangible. Most modern PaaS providers spin up a preview environment for every pull request: a full, disposable copy of the application, built from the same definition file, running on the same infrastructure as production.</p>
<img src="https://cdn.hashnode.com/uploads/covers/66c6d8f04fa7fe6a6e337edd/2867152a-233a-4c12-91d3-3f05b56f79e2.png" alt="Deployment" style="display:block;margin:0 auto" width="1000" height="483" loading="lazy">

<p>"Works on my machine" stops being the standard of evidence, because every reviewer is looking at the code running in a production-shaped environment before it merges. When the PR closes, the environment is destroyed.</p>
<p>That's the whole setup. For a typical web service, going from repository to a deployed, auto-updating application with a managed database takes an afternoon, not a quarter.</p>
<p>For teams with existing infrastructure, the sensible starting point isn't a migration project. It's one service , ideally something low-risk and self-contained, like an internal tool or a background worker.</p>
<p>Run it on a platform for a month, compare the operational load against its Kubernetes-hosted siblings, and let the result inform the larger decision. Most teams that make this comparison discover the question isn't whether the platform can handle their workload. It's how much of their engineering week they'd been spending to get a worse version of the same guarantee.</p>
<h2 id="heading-consistency-is-an-ownership-question-not-a-tooling-question"><strong>Consistency is an Ownership Question, Not a Tooling Question</strong></h2>
<p>"It worked on my machine" gets framed as a process problem, or a testing problem, or occasionally a culture problem. The real framing is more useful: it's an ownership problem.</p>
<p>Every difference between environments like runtime versions, dependency trees, configuration values, and infrastructure state increases the probability that software behaves unexpectedly in production. The conventional response is to invest in better tooling: stricter lock files, more comprehensive CI, better container discipline,