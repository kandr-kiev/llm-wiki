---
source_url: https://www.freecodecamp.org/news/how-to-create-accessible-modals-and-pop-ups-using-html-css-and-minimal-javascript/
ingested: 2026-07-18
sha256: 1ae1a390217528db72a90169907152d6e47927202597167ece3ca5e9a5e92e59
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Create Accessible Modals and Pop-ups Using HTML, CSS, and Minimal JavaScript</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-to-create-accessible-modals-and-pop-ups-using-html-css-and-minimal-javascript/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="Creating pop-ups and modals on your site can be a complicated process. And it often requires a lot of boilerplate code to get started. But the real challenge comes when you want to make that modal or ">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Create Accessible Modals and Pop-ups Using HTML, CSS, and Minimal JavaScript">
    
        <meta property="og:description" content="Creating pop-ups and modals on your site can be a complicated process. And it often requires a lot of boilerplate code to get started. But the real challenge comes when you want to make that modal or ">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-to-create-accessible-modals-and-pop-ups-using-html-css-and-minimal-javascript/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/e929b316-4b85-459b-9c40-1b7928518077.png">
    <meta property="article:published_time" content="2026-07-17T20:34:10.068Z">
    <meta property="article:modified_time" content="2026-07-17T20:34:10.068Z">
    
        <meta property="article:tag" content="anchor css">
    
        <meta property="article:tag" content="popup">
    
        <meta property="article:tag" content="modal">
    
        <meta property="article:tag" content="html modal">
    
        <meta property="article:tag" content="Accessibility">
    
        <meta property="article:tag" content="CSS">
    
        <meta property="article:tag" content="Dialog">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Create Accessible Modals and Pop-ups Using HTML, CSS, and Minimal JavaScript">
    
        <meta name="twitter:description" content="Creating pop-ups and modals on your site can be a complicated process. And it often requires a lot of boilerplate code to get started. But the real challenge comes when you want to make that modal or ">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-to-create-accessible-modals-and-pop-ups-using-html-css-and-minimal-javascript/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/e929b316-4b85-459b-9c40-1b7928518077.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="jabo Landry">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="anchor css, popup, modal, html modal, Accessibility, CSS, Dialog">
    <meta name="twitter:site" content="@freecodecamp">
    
        <meta name="twitter:creator" content="@ArnoldJabo">
    

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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/e929b316-4b85-459b-9c40-1b7928518077.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-to-create-accessible-modals-and-pop-ups-using-html-css-and-minimal-javascript/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-17T20:34:10.068Z",
	"dateModified": "2026-07-17T20:34:10.068Z",
	"keywords": "anchor css, popup, modal, html modal, Accessibility, CSS, Dialog",
	"description": "Creating pop-ups and modals on your site can be a complicated process. And it often requires a lot of boilerplate code to get started.\nBut the real challenge comes when you want to make that modal or ",
	"headline": "How to Create Accessible Modals and Pop-ups Using HTML, CSS, and Minimal JavaScript",
	"author": {
		"@type": "Person",
		"name": "jabo Landry",
		"url": "https://www.freecodecamp.org/news/author/Arnold-Jabo/",
		"sameAs": [
			"https://jabosite.netlify.app/",
			"https://x.com/ArnoldJabo"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://avatars.githubusercontent.com/u/153087724?v=4",
			"width": 420,
			"height": 420
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-17T20:34:10.068Z">
                            July 17, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/anchor-css/">
                                #anchor css
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Create Accessible Modals and Pop-ups Using HTML, CSS, and Minimal JavaScript</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://avatars.githubusercontent.com/u/153087724?v=4 60w" sizes="60px" src="https://avatars.githubusercontent.com/u/153087724?v=4" class="author-profile-image" alt="jabo Landry" width="420" height="420" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/Arnold-Jabo/" data-test-label="profile-link">
                    
                        jabo Landry
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/e929b316-4b85-459b-9c40-1b7928518077.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/e929b316-4b85-459b-9c40-1b7928518077.png" alt="How to Create Accessible Modals and Pop-ups Using HTML, CSS, and Minimal JavaScript" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>Creating pop-ups and modals on your site can be a complicated process. And it often requires a lot of boilerplate code to get started.</p>
<p>But the real challenge comes when you want to make that modal or pop-up accessible.</p>
<p>Today, I'll show you how you can use <code>&lt;dialog&gt;</code> to create an accessible modal/pop-up with minimal setup using HTML, CSS and JavaScript.</p>
<h2 id="heading-prerequisites">Prerequisites</h2>
<p>Before diving in, it helps if you’re comfortable with a few basics:</p>
<ul>
<li><p><strong>CSS fundamentals</strong>: You should be familiar with common CSS terminology and concepts (selectors, properties, positioning, and so on).</p>
</li>
<li><p><strong>HTML structure</strong>: A working knowledge of how elements are organized in the DOM will make the examples easier to follow.</p>
</li>
<li><p><strong>JavaScript DOM basics</strong>: While this guide uses only minimal JavaScript, understanding how to query and manipulate DOM elements will give you more confidence as you experiment.</p>
</li>
</ul>
<p>That’s all you need. No frameworks, no heavy boilerplate. Just a foundation in the core web technologies.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-prerequisites">Prerequisites</a></p>
</li>
<li><p><a href="#heading-how-to-create-pop-ups-with-popover">How to Create Pop-ups with <code>popover</code></a></p>
</li>
<li><p><a href="#heading-how-to-create-a-modal-using-the-dialog-tag">How to Create a Modal Using the <code>dialog</code> Tag</a></p>
</li>
<li><p><a href="#heading-gotchas-to-pay-attention-to">Gotchas to Pay Attention to</a></p>
</li>
<li><p><a href="#heading-the-backdrop-pseudo-class">The <code>::backdrop pseudo</code> class</a></p>
</li>
<li><p><a href="#heading-final-thoughts">Final Thoughts</a></p>
</li>
</ul>
<h2 id="heading-how-to-create-pop-ups-with-popover">How to Create Pop-ups with <code>popover</code></h2>
<p>Creating a pop-up from scratch using HTML, CSS and JavaScript can be quite challenging. A pop-up is a small dialog box that appears on the screen to show extra information or ask for input. Because it’s temporary by design, users expect it to disappear once they’re done interacting with it, like when they press Escape or click outside of it.</p>
<p>Using the HTML <code>popover</code> and <code>popovertarget</code> attributes, you can have several built-in accessibility and interaction behaviors, such as Escape-to-close and light dismiss, but you still need to choose the right semantic element and test keyboard and screen reader behavior.</p>
<h3 id="heading-setting-up-the-pop-up-with-html">Setting Up the Pop-up with HTML</h3>
<p>To be practical, let's create a common example and use case for pop-ups on a webpage. We'll create a nav element that displays when a user clicks a hamburger menu or the menu list.</p>
<p>First, you'll set the <code>popover</code> attribute on the pop-up container. This tells HTML to treat the containing block as a pop-up and hide it from the screen by default.</p>
<p>Then you set the <code>popovertarget</code> attribute on the element that will trigger the pop-up (like a button element or something else) to unhide the hidden element with an attribute of <code>popover</code>.</p>
<h4 id="heading-example">Example:</h4>
<pre><code class="language-html">&lt;button popovertarget="navbar-menu" id='nav-btn'&gt;open&lt;/button&gt;

&lt;nav id="navbar-menu" popover&gt;
  &lt;a href="#"&gt;Home&lt;/a&gt;
  &lt;a href="#"&gt;About&lt;/a&gt;
  &lt;a href="#"&gt;Address&lt;/a&gt;
&lt;/nav&gt;
</code></pre>
<p>With the above setup, you have a pop-up with useful built-in interaction behaviors, including Escape-to-close and light dismiss. You can hide it from the screen by pressing the <code>ESC</code> key on the keyboard or when you click anywhere else on the page (as long as it's not inside the pop-up section).</p>
<p>Remember that the <code>popover</code> attribute alone doesn't automatically make a pop-up accessible. You still need to use the appropriate semantic elements, provide accessible labels where needed, and test keyboard and screen reader behavior.</p>
<h3 id="heading-how-to-align-the-pop-up">How to Align the Pop-up</h3>
<p>Now you'll want to align the pop-up and place it where you want it to be. By default, the pop-up (or modal) that's created using either the <code>popover</code> attribute or the dialog tag will be centered on the page.</p>
<p>This is because by default elements with <code>popover</code> have a position of <code>fixed</code> and the <code>inset</code> of 0, which centers the pop-up box and a margin of <code>auto</code>.</p>
<p><strong>Note:</strong> <code>inset</code> is the shorthand for top, bottom, left and right of an element's position on the page. If you want to have the same size on all of sides of an element, use inset.</p>
<p>If you don't want your pop-up in the center, you can start by setting the element with <code>popover</code> position to absolute to isolate it from the page's flow:</p>
<pre><code class="language-css">#navbar-menu {
  position: absolute;
}
</code></pre>
<p>You can then disable the margin to 0 and positions (inset) to <code>unset</code>:</p>
<pre><code class="language-css">#navbar-menu {
  position: absolute;
  margin: 0;
  inset: unset;
}
</code></pre>
<p>After this, you can then place the popover element on the side of the page you want.</p>
<h3 id="heading-how-to-use-the-position-anchor-property">How to Use the <code>position-anchor</code> Property</h3>
<p><strong>Note:</strong> CSS Anchor Positioning is a newer feature. Check browser support before relying on it in production and provide a fallback for browsers that don't support it yet.</p>
<p>The next step is to position the element close to the element that triggers it. For it we can use the <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor"><code>position-anchor</code> property of CSS</a>.</p>
<p>The <code>position-anchor</code> property in CSS specifies a default anchor element that an absolutely or fixed-positioned element will "tether" or snap to. It lets you link a floating target (like our pop-up here) to another element on the page using only CSS.</p>
<p>In our example, we have a menu list icon or a hamburger menu that will open and close the nav element as a pop-up. We want the nav bar menu to be attached to/near the menu list that opens it.</p>
<p>So, you can add the <code>anchor-name</code> property to a menu icon. The name must be prefixed with double-dashes (and the name can be anything you want).</p>
<pre><code class="language-css">#nav-btn {
  anchor-name: --nav;
}
</code></pre>
<p>The <code>position-anchor</code> property lets you attach an element to another element identified by an anchor name. Once anchored, you can use the <code>anchor()</code> function to position the element relative to that anchor, like aligning it to the anchor’s top, bottom, or center.</p>
<pre><code class="language-css">#navbar-menu {
  position: absolute;
  margin: 0;
  inset: auto;
  position-anchor: --nav;
  top: anchor(bottom);
  right: anchor(right);
}
</code></pre>
<p>Pass the anchor name you give your anchor as value of <code>position-anchor</code> to align the nav element (<code>#navbar-menu</code> in our example) on the page around the <code>anchor-name</code> of <code>nav</code> which is <code>#nav-btn</code> in our example.</p>
<p>Then the <code>anchor()</code>positions the top of nav element on the bottom side and right side to the menu's right side.</p>
<div class="embed-wrapper"><iframe width="100%" height="350" src="https://codepen.io/jabo-arnold/embed/ogBBNNa" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="CodePen embed" scrolling="no" allowtransparency="true" allowfullscreen="true" loading="lazy"></iframe></div>

<h2 id="heading-how-to-create-a-modal-using-the-dialog-tag">How to Create a Modal Using the <code>dialog</code> Tag</h2>
<p>Using the <code>command</code> and <code>commandfor</code> attributes on a button, you can declaratively control a <code>&lt;dialog&gt;</code>. For example, <code>command="show-modal"</code> opens it as a modal, while <code>command="close"</code> closes it.</p>
<p>Pop-up modals and pop-ups are different: with a pop-up, you can still interact with the page when the pop-up is active. But with modals or pop-up modals you can't interact with the page – modals lock the screen until they're ignored or confirmed.</p>
<p>When a <code>&lt;dialog&gt;</code> is opened as a modal, it's placed in the browser's top layer so that it appears above the rest of the page content. The rest of the document becomes inert, meaning users can't interact with it while the modal is open. The browser also creates a <code>::backdrop</code> behind the modal, which you can style to provide a visual overlay.</p>
<p>Here's an example:</p>
<pre><code class="language-html">&lt;button command="show-modal" commandfor="contact-dialog"&gt;
    open modal
&lt;/button&gt;

 &lt;dialog id="contact-dialog"&gt;
    &lt;button command="close" commandfor="contact-dialog" aria-label="close modal"&gt;
      close modal
    &lt;/button&gt;
    &lt;!--modal contents goes here--&gt;
&lt;/dialog&gt;
</code></pre>
<p>You can use the <code>command</code> attribute to close and show the modal and the <code>commandfor</code> attribute to reference the modal that's being targeted using the modal's id.</p>
<p>The <code>command</code> attribute can receive one of the following options:</p>
<ul>
<li><p><code>show-modal</code>: This option is used on the element that will trigger the modal or the dialog box to open it.</p>
</li>
<li><p><code>close</code>: This option is passed to an element and will close the modal when it's open.</p>
</li>
</ul>
<p>In the code snippet example, you can see that the button with label <code>open modal</code> has a <code>command</code> attribute with the option to <strong>show-modal</strong> and the <code>commandfor</code> attribute that's targeting the dialog element by its id.</p>
<p>The close modal button is using the <strong>close</strong> option on the <code>command</code> attribute to close the modal when clicked. It also uses <code>commandfor</code> to indicate which modal should be closed when the close button is clicked.</p>
<p>Below you'll find a demo of a modal that's created using the <code>command</code> and <code>commandfor</code> attributes:</p>
<div class="embed-wrapper"><iframe width="100%" height="350" src="https://codepen.io/jabo-arnold/embed/NPdRqWK?editors=1100" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="CodePen embed" scrolling="no" allowtransparency="true" allowfullscreen="true" loading="lazy"></iframe></div>

<p>Try clicking the "click to pop a modal!" button on the Code Pen above to see the modal you can create by just using the <code>command</code> and <code>commandfor</code> attributes on a <code>dialog</code> tag.</p>
<h3 id="heading-create-modal-using-showmodal">Create modal using <code>showModal()</code></h3>
<p>The command API may not be supported in older browsers. Alternatively you can use JavaScript's <code>showModal()</code> method, as it's widely available in many browsers compared to <code>command</code> and <code>commandfor</code>.</p>
<pre><code class="language-javascript">const btn = document.querySelector("button");
const dialog = document.querySelector("dialog");

btn.addEventListener("click", () =&gt; {
  dialog.showModal();
});
</code></pre>
<h3 id="heading-how-to-open-a-non-modal-dialog-with-show">How to Open a Non-Modal Dialog with <code>show()</code></h3>
<p>Sometimes you may want to have an element like modal that stays interactive and doesn't block the other pages content like the <code>command</code> and <code>commandfor</code> attributes do. For this, you can use <code>show()</code> on dialog using JavaScript.</p>
<pre><code class="language-javascript">const btn = document.querySelector("button");
const dialog = document.querySelector("dialog");

btn.addEventListener("click", () =&gt; {
  dialog.show();
});
</code></pre>
<p>The above snippet keeps the rest of the page interactive while the dialog is open. This differs from opening a dialog with <code>showModal()</code> or using <code>command="show-modal"</code>, which opens the dialog as a modal and makes the rest of the document inert.</p>
<p><strong>Note</strong>: Keep in mind that <code>show()</code> isn't considered a modal but more of a dialog-like element that doesn't block interaction with the rest of the page.</p>
<h2 id="heading-gotchas-to-pay-attention-to">Gotchas to Pay Attention to</h2>
<p>When you're using element <code>popover</code>, the <code>command</code> and <code>commandfor</code> attributes, or the <code>show()</code> method, there are some "gotchas" to watch out for. Paying attention to these will help you stick to best practices.</p>
<h3 id="heading-dont-use-flex-or-grid">Don't Use Flex or Grid</h3>
<p>Directly applying layout-related styles like Flex or Grid is highly discouraged on both elements with <code>popover</code> and modal elements.</p>
<p>By default, elements with <code>popover</code> attribute, <code>command</code> and <code>commandfor</code> button attributes, and <code>show()</code> have a display of <code>none</code>. This basically means the pop-up or modal is hidden from the screen.</p>
<p>When you add <code>flex</code> or <code>grid</code> directly on element with the <code>popover</code> attribute or on a modal element, you're rewriting the modal or <code>popover</code> element's default behavior and they will be always visible on the screen. This means that you won't be able to hide the modal from the screen.</p>
<p>Check out the below example in the CodePen demo:</p>
<pre><code class="language-css">#navbar-menu {
  display: grid;
/* other styles definition*/
}
</code></pre>
<div class="embed-wrapper"><iframe width="100%" height="350" src="https://codepen.io/jabo-arnold/embed/wBgrJEv" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="CodePen embed" scrolling="no" allowtransparency="true" allowfullscreen="true" loading="lazy"></iframe></div>

<p>You can see from the example that the nav element is always visible even if we click on the menu button to hide it again.</p>
<h4 id="heading-suggested-approach">Suggested Approach</h4>
<p>In this situation, you can either use the <code>popover-open</code> pseudo-class on an element on a property that has <code>popover</code> attributes, or you can use <code>dialog[open]</code> on the dialog element.</p>
<p>The pseudo-class styles the element based on its state when interacting with the page. So, in this case we want to give the pop-up or a modal a different layout when it's in the open state.</p>
<p>Example:</p>
<pre><code class="language-css">/* element with a popover*/
#navbar-menu:popover-open {
  display: grid;
  gap: 2rem;
}

/* using a dialog element*/
dialog[open] {
  display: grid;
  gap: 2rem;
}
</code></pre>
<h3 id="heading-background-scrolling">Background Scrolling</h3>
<p>Another thing to consider when using the <code>&lt;dialog&gt;</code> element is background scrolling. Depending on the browser and platform, the underlying page may still be scrollable while a modal dialog is open. If you want to prevent this behavior, you can explicitly disable scrolling while the dialog is open.</p>
<p>Take a look at this CodePen example:</p>
<div class="embed-wrapper"><iframe width="100%" height="350" src="https://codepen.io/jabo-arnold/embed/NPdRqWK?editors=1100" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="CodePen embed" scrolling="no" allowtransparency="true" allowfullscreen="true" loading="lazy"></iframe></div>

<p>When you click on the button to show the modal, you can still see the scrollbar on the page, and you can scroll around the page.</p>
<h4 id="heading-suggested-approach">Suggested Approach</h4>
<p>To deal with this issue we can use the <code>has</code> pseudo class. <code>has</code> helps select the parent element based on its children's state. On the root element or HTML element, you can check if it has an open modal. If so, you can set the root element or HTML element overflow to hidden.</p>
<p>For example:</p>
<pre><code class="language-css">html:has(dialog[open]) {
  overflow: hidden;
}
</code></pre>
<p>This will hide the scrollbar on the page when the modal is open. Keep in mind that you can also use any parent element to wrap the <code>dialog</code> tag with the <code>has</code> pseudo class. It doesn't always have to be the root element or HTML element.</p>
<h2 id="heading-the-backdrop-pseudo-class">The <code>::backdrop</code> Pseudo Class</h2>
<p>If you want to use a customized overlay color on the <code>popover</code> element or modal element, you can use the <code>::backdrop</code> pseudo class to customize the appearance for the modal overlay color.</p>
<p><strong>Example:</strong></p>
<pre><code class="language-css">dialog::backdrop {
  background: rgba(43, 50, 200, 0.4);
}
</code></pre>
<p>This will apply the overlay with defined <code>RGB</code> colors and the <code>opacity</code> of 0.4 on the overlay to have a little transparent on the overlay.</p>
<h2 id="heading-final-thoughts">Final Thoughts</h2>
<p>I hope you've gained something new from this article, and that it will help you start using these techniques in your projects.</p>


                        </section>
                        
                            <div class="sidebar">
                                
                                    
                                    <script>var localizedAdText = "ADVERTISEMENT";</script>
                                
                            </div>
                        
                    </div>
                    <hr>
                    
                        <div class="post-full-author-header" data-test-label="author-header-with-bio">
                            
                                
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://avatars.githubusercontent.com/u/153087724?v=4 60w" sizes="60px" src="https://avatars.githubusercontent.com/u/153087724?v=4" class="author-profile-image" alt="jabo Landry" width="420" height="420" onerror="this.style.display='none'" loading="lazy" data-test-label="profile-image">
  
        

        <section class="author-card-content ">
            <span class="author-card-name">
                <a href="/news/author/Arnold-Jabo/" data-test-label="profile-link">
                    
                        jabo Landry
                    
                </a>
            </span>
            
                
                    <p data-test-label="author-bio">I am a developer Prototype</p>
                
            
        </section>
    </section>

                            
                        </div>
                        <hr>
                    

                    
                    
                        
    


<p data-test-label="social-row-cta" class="social-row">
    If you read this far, thank the author to show them you care. <button id="tweet-btn" class="cta-button" data-test-label="tweet-button">Say Thanks</button>
</p>


    
    <script>document.addEventListener("DOMContentLoaded",()=>{const t=document.getElementById("tweet-btn"),n=window.location,o="How%20to%20Create%20Accessible%20Modals%20and%20Pop-ups%20Using%20HTML%2C%20CSS%2C%20and%20Minimal%20JavaScript".replace(/&#39;/g,"%27"),e="",i="@ArnoldJabo",r=Boolean("");let a;if(r&&(e||i)){const t={originalPostAuthor:"",currentPostAuthor:"jabo Landry"};a=encodeURIComponent(`Thank you ${e||t.originalPostAuthor} for writing this helpful article, and ${i||t.currentPostAuthor} for translating it.`)}else!r&&i&&(a=encodeURIComponent(`Thank you ${i} for writing this helpful article.`));const s=`window.open(\n    '${a?`https://x.com/intent/post?text=${a}%0A%0A${o}%0A%0A${n}`:`https://x.com/intent/post?text=${o}%0A%0A${n}`}',\n    'share-twitter',\n    'width=550, height=235'\n  ); return false;`;t.setAttribute("onclick",s)});</script>


                        

<div class="learn-cta-row" data-test-label="learn-cta-row">
    <p>
        Le