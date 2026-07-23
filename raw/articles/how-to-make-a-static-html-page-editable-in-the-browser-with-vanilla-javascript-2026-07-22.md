---
source_url: https://www.freecodecamp.org/news/how-to-make-a-static-html-page-editable-in-the-browser-with-vanilla-javascript/
ingested: 2026-07-22
sha256: 0ff4f963bda884b210ce747c1a86da1d64543653cf2fd1539ab677a9db5cf902
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Make a Static HTML Page Editable in the Browser with Vanilla JavaScript</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-to-make-a-static-html-page-editable-in-the-browser-with-vanilla-javascript/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="When you maintain a document for someone else, such as a résumé, a one-page portfolio, or a printable menu, the bottleneck is rarely the layout. It&#39;s the edit loop. Every small change (&quot;move this bull">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Make a Static HTML Page Editable in the Browser with Vanilla JavaScript">
    
        <meta property="og:description" content="When you maintain a document for someone else, such as a résumé, a one-page portfolio, or a printable menu, the bottleneck is rarely the layout. It&#39;s the edit loop. Every small change (&quot;move this bull">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-to-make-a-static-html-page-editable-in-the-browser-with-vanilla-javascript/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/08400ed2-ef6a-404f-a135-b6cefe9d6919.png">
    <meta property="article:published_time" content="2026-07-22T20:22:03.511Z">
    <meta property="article:modified_time" content="2026-07-22T20:22:03.511Z">
    
        <meta property="article:tag" content="HTML">
    
        <meta property="article:tag" content="CSS">
    
        <meta property="article:tag" content="DOM">
    
        <meta property="article:tag" content="JavaScript">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Make a Static HTML Page Editable in the Browser with Vanilla JavaScript">
    
        <meta name="twitter:description" content="When you maintain a document for someone else, such as a résumé, a one-page portfolio, or a printable menu, the bottleneck is rarely the layout. It&#39;s the edit loop. Every small change (&quot;move this bull">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-to-make-a-static-html-page-editable-in-the-browser-with-vanilla-javascript/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/08400ed2-ef6a-404f-a135-b6cefe9d6919.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="timothy ogbemudia">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="HTML, CSS, DOM, JavaScript">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/08400ed2-ef6a-404f-a135-b6cefe9d6919.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-to-make-a-static-html-page-editable-in-the-browser-with-vanilla-javascript/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-22T20:22:03.511Z",
	"dateModified": "2026-07-22T20:22:03.511Z",
	"keywords": "HTML, CSS, DOM, JavaScript",
	"description": "When you maintain a document for someone else, such as a résumé, a one-page portfolio, or a printable menu, the bottleneck is rarely the layout. It&#x27;s the edit loop.\nEvery small change (&quot;move this bull",
	"headline": "How to Make a Static HTML Page Editable in the Browser with Vanilla JavaScript",
	"author": {
		"@type": "Person",
		"name": "timothy ogbemudia",
		"url": "https://www.freecodecamp.org/news/author/glamboyosa/",
		"sameAs": [
			"https://glamboyosa.xyz"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/uploads/avatars/5cf591dcaa34a8856803ec56/b865b84e-9ba4-4241-a118-c10865189843.png",
			"width": 491,
			"height": 491
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-22T20:22:03.511Z">
                            July 22, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/html/">
                                #HTML
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Make a Static HTML Page Editable in the Browser with Vanilla JavaScript</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/uploads/avatars/5cf591dcaa34a8856803ec56/b865b84e-9ba4-4241-a118-c10865189843.png 60w" sizes="60px" src="https://cdn.hashnode.com/uploads/avatars/5cf591dcaa34a8856803ec56/b865b84e-9ba4-4241-a118-c10865189843.png" class="author-profile-image" alt="timothy ogbemudia" width="491" height="491" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/glamboyosa/" data-test-label="profile-link">
                    
                        timothy ogbemudia
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/08400ed2-ef6a-404f-a135-b6cefe9d6919.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/08400ed2-ef6a-404f-a135-b6cefe9d6919.png" alt="How to Make a Static HTML Page Editable in the Browser with Vanilla JavaScript" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>When you maintain a document for someone else, such as a résumé, a one-page portfolio, or a printable menu, the bottleneck is rarely the layout. It's the edit loop.</p>
<p>Every small change ("move this bullet up", "delete that line", "this link is dead") goes through you, the person with the code editor, even though the person requesting the change knows exactly what they want.</p>
<p>I ran into this maintaining a family member's résumé as a single static HTML file. The design was done. The content was theirs. But every revision, whether it was reordering a role, adding a certification, fixing a link, or nudging a print page break, meant another round of "send me the change, I'll edit the file." After the tenth round, the fix became obvious: make the page edit itself.</p>
<p>In this article, you'll build an in-browser editing layer for a static HTML page using <code>contenteditable</code>, about a hundred lines of vanilla JavaScript, and no build step. The person editing can change any text, reorder or delete any block, add new content, edit links, control print pagination, and print to PDF. A refresh restores the original file, untouched.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-prerequisites">Prerequisites</a></p>
</li>
<li><p><a href="#heading-what-you-will-learn">What You Will Learn</a></p>
</li>
<li><p><a href="#heading-what-is-contenteditable">What Iscontenteditable?</a></p>
</li>
<li><p><a href="#heading-why-not-a-react-app">Why Not a React App?</a></p>
</li>
<li><p><a href="#heading-how-to-prepare-the-markup-for-reordering">How to Prepare the Markup for Reordering</a></p>
</li>
<li><p><a href="#heading-how-to-attach-controls-to-every-block">How to Attach Controls to Every Block</a></p>
</li>
<li><p><a href="#heading-how-to-show-controls-only-on-the-innermost-block">How to Show Controls Only on the Innermost Block</a></p>
</li>
<li><p><a href="#heading-how-to-move-and-delete-blocks">How to Move and Delete Blocks</a></p>
</li>
<li><p><a href="#heading-how-to-edit-links-inside-contenteditable">How to Edit Links Insidecontenteditable</a></p>
</li>
<li><p><a href="#heading-how-to-let-users-control-print-pagination">How to Let Users Control Print Pagination</a></p>
</li>
<li><p><a href="#heading-how-to-add-new-content-from-templates">How to Add New Content from Templates</a></p>
</li>
<li><p><a href="#heading-why-nothing-persists">Why Nothing Persists</a></p>
</li>
<li><p><a href="#heading-conclusion">Conclusion</a></p>
</li>
</ul>
<h2 id="heading-prerequisites">Prerequisites</h2>
<p>To follow along, you should have:</p>
<ul>
<li><p>Working knowledge of HTML and CSS, including CSS Grid and <code>@media print</code></p>
</li>
<li><p>Basic understanding of JavaScript DOM APIs (<code>querySelector</code>, event listeners, creating elements)</p>
</li>
<li><p>No frameworks, libraries, or build tools. That's the point.</p>
</li>
</ul>
<h2 id="heading-what-you-will-learn">What You Will Learn</h2>
<ul>
<li><p>What <code>contenteditable</code> gives you for free, and where it stops</p>
</li>
<li><p>How to attach move/delete controls to repeatable blocks with one reusable function</p>
</li>
<li><p>How to show controls only on the innermost hovered block using <code>:has()</code></p>
</li>
<li><p>How to reorder DOM nodes without a framework, and the markup prep that makes it safe</p>
</li>
<li><p>How to edit link URLs inside an editable region</p>
</li>
<li><p>How to let users place print page breaks themselves</p>
</li>
<li><p>How to add new content from templates, with placeholder text pre-selected</p>
</li>
<li><p>Why "nothing persists" can be a feature, not a limitation</p>
</li>
</ul>
<h2 id="heading-what-is-contenteditable">What Is <code>contenteditable</code>?</h2>
<p><code>contenteditable</code> is an HTML attribute that turns any element into an editable region. The browser handles the hard parts: caret placement, text selection, typing, deletion, clipboard, and undo history.</p>
<pre><code class="language-html">&lt;div class="page" contenteditable="true" spellcheck="false"&gt;
  &lt;!-- the entire document --&gt;
&lt;/div&gt;
</code></pre>
<p>That one attribute gets you further than you might expect. Clicking any paragraph places a caret. Cmd+Z undoes typing. Pressing Enter inside a <code>&lt;ul&gt;</code> creates a new <code>&lt;li&gt;</code>. The browser understands list semantics natively, so "add a bullet by pressing Enter" works with zero code.</p>
<p>But <code>contenteditable</code> alone isn't an editor. It has no concept of <em>blocks</em>. It won't move a job entry above another one, delete a card cleanly, or change an <code>href</code>. Clicking a link inside an editable region just places the caret in its text. Everything structural is on you. The rest of this article is about filling that gap.</p>
<h2 id="heading-why-not-a-react-app">Why Not a React App?</h2>
<p>The obvious alternative is to rebuild the page as a "real" app: components, state, a form per section, and an export button. I decided against it, and the tradeoff is important.</p>
<p>The file lives in a <code>public/</code> folder and is served as a static asset. It works from a URL, from disk, or from an email attachment. It has no dependencies to install, no build to run, and no way to rot when a toolchain updates.</p>
<p>The editing needs are small and bounded: change text, move blocks, delete blocks, add blocks, and print. That's DOM manipulation, the thing the DOM API is already good at.</p>
<p>A framework earns its complexity when state outlives the DOM: persistence, collaboration, validation, and syncing. This page has none of those requirements. When your state <em>is</em> the DOM and the lifetime is one session, a framework is an extra layer that buys you nothing.</p>
<h2 id="heading-how-to-prepare-the-markup-for-reordering">How to Prepare the Markup for Reordering</h2>
<p>Before writing any JavaScript, look at your markup for anything positional, meaning elements that only make sense <em>between</em> other elements. In my case, jobs were separated by <code>&lt;hr&gt;</code> dividers:</p>
<pre><code class="language-html">&lt;div class="job"&gt;...&lt;/div&gt;
&lt;hr class="divider"&gt;
&lt;div class="job"&gt;...&lt;/div&gt;
</code></pre>
<p>The moment blocks can move or be deleted, separators like this become landmines. Delete a job and its divider survives as an orphaned line. Move a job and the divider stays behind.</p>
<p>The fix is to delete the <code>&lt;hr&gt;</code> elements entirely and derive the separator from adjacency:</p>
<pre><code class="language-css">.section .job + .job {
  border-top: 0.5px solid var(--rule);
  padding-top: 18px;
}
</code></pre>
<p>The sibling combinator draws a rule above every job that follows another job. Reorder them, delete them, add new ones, and the separators are always exactly where they should be, because they're computed from structure rather than stored in it. This is the same principle as deriving state instead of duplicating it, applied to CSS.</p>
<h2 id="heading-how-to-attach-controls-to-every-block">How to Attach Controls to Every Block</h2>
<p>Each movable block gets a small control cluster with move up, move down, and delete actions, injected by one reusable function:</p>
<pre><code class="language-js">const SELECTORS = ['.section', '.job', '.bullets li', '.cert-card', '.skills-row', '.edu-row'];
const BREAKABLE = new Set(['.section', '.job']);

function makeBlock(el, sel) {
  el.classList.add('blk');
  el.dataset.sel = sel;
  const ctl = document.createElement('span');
  ctl.className = 'ctl';
  ctl.setAttribute('contenteditable', 'false');
  ctl.innerHTML =
    '&lt;button data-act="up" data-tip="Move this up"&gt;↑&lt;/button&gt;' +
    '&lt;button data-act="down" data-tip="Move this down"&gt;↓&lt;/button&gt;' +
    (BREAKABLE.has(sel) ? '&lt;button data-act="brk" data-tip="Page break: start a new printed page here"&gt;⇟&lt;/button&gt;' : '') +
    '&lt;button data-act="del" data-tip="Remove this. Refresh to bring it back"&gt;×&lt;/button&gt;';
  el.appendChild(ctl);
}

SELECTORS.forEach(sel =&gt; {
  page.querySelectorAll(sel).forEach(el =&gt; makeBlock(el, sel));
});
</code></pre>
<p>A few design decisions are worth calling out.</p>
<p>First, <code>contenteditable="false"</code> on the control cluster. Editable regions inherit. Everything inside the page is editable unless you opt out. Without this, the user could place a caret inside your buttons and delete them like text.</p>
<p>Second, <code>el.dataset.sel</code> records <em>which selector matched</em>. This matters later: when a block moves, it should only swap with siblings of its own kind. A bullet moves among bullets, a job among jobs. Storing the selector on the element makes that check trivial.</p>
<p>Third, the controls live <em>inside</em> the block they control. That gives you positioning for free, with <code>position: absolute</code> against the block's own <code>position: relative</code>, and means a block carries its controls with it wherever it moves.</p>
<h2 id="heading-how-to-show-controls-only-on-the-innermost-block">How to Show Controls Only on the Innermost Block</h2>
<p>Blocks nest: a bullet sits inside a job, which sits inside a section. Hovering a bullet technically hovers all three, and naïve CSS shows three control clusters at once. The result is visual noise exactly where the user is trying to focus.</p>
<p>Modern CSS solves this in one line:</p>
<pre><code class="language-css">.blk:hover:not(:has(.blk:hover)) &gt; .ctl { display: inline-flex; }
</code></pre>
<p>Read it inside out: show a block's controls when it's hovered, <em>unless</em> some descendant block is also hovered, in which case that deeper block wins. Hover a bullet, you get bullet controls. Hover the job's title (outside any bullet), you get job controls. One rule, no JavaScript.</p>
<p><code>:has()</code> is supported in every current browser, but a fallback costs one more rule:</p>
<pre><code class="language-css">@supports not selector(:has(*)) {
  .blk:hover &gt; .ctl { display: inline-flex; }
}
</code></pre>
<p>Older browsers get the noisier all-ancestors behavior instead of no controls at all. Degrade loudly, not silently.</p>
<h2 id="heading-how-to-move-and-delete-blocks">How to Move and Delete Blocks</h2>
<p>With controls attached, the actual reordering is short. One delegated listener handles every button on the page:</p>
<pre><code class="language-js">function siblings(el) {
  return [...el.parentElement.children].filter(c =&gt;
    c.classList.contains('blk') &amp;&amp; c.dataset.sel === el.dataset.sel);
}

page.addEventListener('click', e =&gt; {
  const btn = e.target.closest('.ctl button');
  if (!btn) return;
  e.preventDefault();
  const el = btn.closest('.blk');
  const sibs = siblings(el);
  const i = sibs.indexOf(el);
  const act = btn.dataset.act;
  if (act === 'up' &amp;&amp; i &gt; 0) sibs[i - 1].before(el);
  else if (act === 'down' &amp;&amp; i &lt; sibs.length - 1) sibs[i + 1].after(el);
  else if (act === 'del') el.remove();
  else if (act === 'brk') el.classList.toggle('page-break');
});
</code></pre>
<p><code>siblings()</code> is where <code>dataset.sel</code> pays off: it filters the parent's children down to blocks <em>of the same kind</em>, so a job can never swap into the middle of a bullet list. <code>before()</code> and <code>after()</code> move the live node with no cloning or re-rendering, and the block's own controls travel with it.</p>
<p>There's one subtle bug to prevent. Clicking a button inside an editable region moves the text caret first, which can scroll the page or collapse a selection. Suppress it at <code>mousedown</code>, before the browser acts:</p>
<pre><code class="language-js">page.addEventListener('mousedown', e =&gt; {
  if (e.target.closest('.ctl, .add-btn')) e.preventDefault();
});
</code></pre>
<p>Forgetting this is the kind of thing you only notice as a vague feeling that clicking buttons "jumps." It's worth ruling out before it ships.</p>
<h2 id="heading-how-to-edit-links-inside-contenteditable">How to Edit Links Inside <code>contenteditable</code></h2>
<p>Inside an editable region, single-clicking a link places the caret instead of navigating. That's correct for text editing but leaves no way to change the URL itself. The <code>href</code> isn't text, it's an attribute.</p>
<p>Double-click is unclaimed real estate, so hang URL editing off it:</p>
<pre><code class="language-js">page.addEventListener('dblclick', e =&gt; {
  const a = e.target.closest('a');
  if (!a) return;
  e.preventDefault();
  const url = prompt('Link URL (leave empty to remove the link):', a.getAttribute('href'));
  if (url === null) return;
  if (!url.trim()) a.replaceWith(document.createTextNode(a.textContent));
  else a.setAttribute('href', url.trim());
});
</code></pre>
<p>Yes, <code>prompt()</code>. It's unfashionable, but consider what a custom modal would cost: markup, styles, focus management, and an escape handler, all for a dialog that asks one question. <code>prompt()</code> is native, keyboard-accessible, and can't break.</p>
<p>The empty-string branch is a nice touch: it unwraps the link entirely, replacing it with its own text, so "remove this link" doesn't require knowing any HTML.</p>
<p>Since none of this is discoverable, tell the user. A <code>title</code> attribute on every link ("Double-click to change this link") surfaces the affordance exactly where it's needed.</p>
<h2 id="heading-how-to-let-users-control-print-pagination">How to Let Users Control Print Pagination</h2>
<p>If the document's destination is a printed PDF, page breaks are content decisions, like "start my Skills section on page three," and the user should own them. CSS makes the break itself easy:</p>
<pre><code class="language-css">@media print {
  .page-break { break-before: page; page-break-before: always; }
  .job { break-inside: avoid; page-break-inside: avoid; }
}
</code></pre>
<p>The interesting part is the interface. The <code>⇟</code> button you saw in <code>makeBlock</code> just toggles the <code>page-break</code> class on a job or section. On screen, the class renders as a dashed accent line above the block, a visible seam showing where the printed page will end:</p>
<pre><code class="language-css">.page .page-break {
  border-top: 1.5px dashed var(--accent) !important;
  padding-top: 14px !important;
}

@media print {
  .page .page-break { border-top: none !important; padding-top: 0 !important; }
}
</code></pre>
<p>The dashed line exists only on screen. In print it vanishes and the actual break takes its place. The user toggles, glances at the seam, and prints. Nobody edits CSS to re-paginate a document, and just as importantly, nobody asks me to.</p>
<p>The same <code>@media print</code> block hides every piece of editing chrome (<code>.toolbar, .ctl, .add-btn { display: none !important; }</code>), so the printed output is indistinguishable from the original static page.</p>
<h2 id="heading-how-to-add-new-content-from-templates">How to Add New Content from Templates</h2>
<p>Editing and deleting only go so far. Eventually someone needs a new bullet, a new role, or a new certification. Each repeatable container gets a dashed "+ Add" button that builds a blank block from a template:</p>
<pre><code class="language-js">skillsSection.appendChild(newAddBtn('+ Add skill row', 'Adds a blank row. Type over the placeholder.', btn =&gt; {
  const row = document.createElement('div');
  row.className = 'skills-row';
  row.innerHTML =
    '&lt;span class="skill-label"&gt;Label&lt;/span&gt;' +
    '&lt;span class="skill-items"&gt;Skill one, skill two, skill three&lt;/span&gt;';
  skillsSection.insertBefore(row, btn);
  makeBlock(row, '.skills-row');
  selectText(row.querySelector('.skill-label'));
}));
</code></pre>
<p>Two details here do most of the work.</p>
<p>New blocks go through the same <code>makeBlock</code> as everything parsed at load. There is exactly one code path for "this is a block now", so added content is immediately movable and deletable. For roles it gets its own nested "+ Add bullet" button.</p>
<p>If you find yourself writing a second registration path for dynamic content, stop. You're about to fork behavior that must stay identical.</p>
<p>And <code>selectText</code> pre-selects the placeholder:</p>
<pre><code class="language-js">function selectText(node) {
  const range = document.createRange();
  range.selectNodeContents(node);
  const sel = getSelection();
  sel.removeAllRanges();
  sel.addRange(range);
}
</code></pre>
<p>Click "+ Add skill row" and the word <code>Label</code> is already highlighted, so typing replaces it. No clicking into the field, no manually deleting placeholder text, and no placeholders accidentally left in the printed document.</p>
<p>One caveat: select the <em>text node</em>, not the block. The block contains your <code>contenteditable="false"</code> control cluster, and a selection spanning it will delete your buttons along with the placeholder on the first keystroke.</p>
<h2 id="heading-why-nothing-persists">Why Nothing Persists</h2>
<p>Every edit lives in the DOM and dies on refresh. That sounds like the missing feature, but it's the design.</p>
<p>The workflow this page serves is: open, adjust, print to PDF, close. The PDF is the artifact. The page is a template you stamp from. Ephemerality gives you a free, bulletproof undo-everything (refresh), zero risk of a half-finished edit becoming the new baseline, and a canonical version that always matches source control.</p>
<p>The toolbar says it plainly: <em>"Nothing is saved. Refresh resets everything."</em> Stated upfront, it reads as a guarantee rather than a gotcha.</p>
<p>Persistence would also be the complexity cliff. The moment edits survive refresh you inherit serialization, versioning, merge conflicts with the source file, and "which copy is real?" Those are the exact problems this design exists to avoid.</p>
<h2 id="heading-conclusion">Conclusion</h2>
<p>You now have a static HTML page that edits itself: <code>contenteditable</code> for text, one <code>makeBlock</code> function for structure, <code>:has()</code> for focused hover controls, a class toggle for print pagination, and templates with pre-selected placeholders for new content. Around a hundred lines of JavaScript, with no dependencies and no build.</p>
<p>Just as important is knowing when this approach stops being right. If edits must persist, if multiple people edit concurrently, or if the content needs validation and workflow, you've outgrown the DOM-as-state model. In those cases, reach for a real application and a database.</p>
<p>But for the wide middle ground of documents that one person adjusts and prints, such as résumés, invoices, certificates, and programmes, the browser already ships the editor. You just have to turn it on.</p>


                        </section>
                        
                            <div class="sidebar">
                                
                                    
                                    <script>var localizedAdText = "ADVERTISEMENT";</script>
                                
                            </div>
                        
                    </div>
                    <hr>
                    
                        <div class="post-full-author-header" data-test-label="author-header-with-bio">
                            
                                
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/uploads/avatars/5cf591dcaa34a8856803ec56/b865b84e-9ba4-4241-a118-c10865189843.png 60w" sizes="60px" src="https://cdn.hashnode.com/uploads/avatars/5cf591dcaa34a8856803ec56/b865b84e-9ba4-4241-a118-c10865189843.png" class="author-profile-image" alt="timothy ogbemudia" width="491" height="491" onerror="this.style.display='none'" loading="lazy" data-test-label="profile-image">
  
        

        <section class="author-card-content ">
            <span class="author-card-name">
                <a href="/news/author/glamboyosa/" data-test-label="profile-link">
                    
                        timothy ogbemudia
                    
                </a>
            </span>
            
                
                    <p data-test-label="default-bio">
                        Read <a href="/news/author/glamboyosa/">more posts</a>.
                    </p>
                
            
  