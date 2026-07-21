---
source_url: https://www.freecodecamp.org/news/build-pdf-redaction-tool-javascript/
ingested: 2026-07-18
sha256: 5be3606f5d9e3d62457d66e7b530433ad5e1cec2157ebe346fd23287678b9da6
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Build a Browser-Based PDF Redaction Tool Using JavaScript</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/build-pdf-redaction-tool-javascript/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="PDF documents are frequently used to share invoices, contracts, reports, legal records, customer documents, financial statements, and internal business files. But before these documents are shared, th">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Build a Browser-Based PDF Redaction Tool Using JavaScript">
    
        <meta property="og:description" content="PDF documents are frequently used to share invoices, contracts, reports, legal records, customer documents, financial statements, and internal business files. But before these documents are shared, th">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/build-pdf-redaction-tool-javascript/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/18191d9d-9abf-44a3-8330-e452ce7194c2.png">
    <meta property="article:published_time" content="2026-07-17T20:33:11.227Z">
    <meta property="article:modified_time" content="2026-07-17T20:33:11.227Z">
    
        <meta property="article:tag" content="JavaScript">
    
        <meta property="article:tag" content="Web Development">
    
        <meta property="article:tag" content="pdf">
    
        <meta property="article:tag" content="Online PDF Tools">
    
        <meta property="article:tag" content="pdf tutorial">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    
        <meta property="article:author" content="AllInOneTools.net">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Build a Browser-Based PDF Redaction Tool Using JavaScript">
    
        <meta name="twitter:description" content="PDF documents are frequently used to share invoices, contracts, reports, legal records, customer documents, financial statements, and internal business files. But before these documents are shared, th">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/build-pdf-redaction-tool-javascript/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/18191d9d-9abf-44a3-8330-e452ce7194c2.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Bhavin Sheth">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="JavaScript, Web Development, pdf, Online PDF Tools, pdf tutorial">
    <meta name="twitter:site" content="@freecodecamp">
    
        <meta name="twitter:creator" content="@allinonetools">
    

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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/18191d9d-9abf-44a3-8330-e452ce7194c2.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/build-pdf-redaction-tool-javascript/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-17T20:33:11.227Z",
	"dateModified": "2026-07-17T20:33:11.227Z",
	"keywords": "JavaScript, Web Development, pdf, Online PDF Tools, pdf tutorial",
	"description": "PDF documents are frequently used to share invoices, contracts, reports, legal records, customer documents, financial statements, and internal business files. But before these documents are shared, th",
	"headline": "How to Build a Browser-Based PDF Redaction Tool Using JavaScript",
	"author": {
		"@type": "Person",
		"name": "Bhavin Sheth",
		"url": "https://www.freecodecamp.org/news/author/allinonetools/",
		"sameAs": [
			"https://allinonetools.net/",
			"https://www.facebook.com/AllInOneTools.net",
			"https://x.com/allinonetools"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/res/hashnode/image/upload/v1769591816718/c151b08b-2f7b-4e54-b68e-262a3b4d998a.png?w=500&h=500&fit=crop&crop=entropy&auto=compress,format&format=webp",
			"width": 507,
			"height": 492
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-17T20:33:11.227Z">
                            July 17, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/javascript/">
                                #JavaScript
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Build a Browser-Based PDF Redaction Tool Using JavaScript</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/res/hashnode/image/upload/v1769591816718/c151b08b-2f7b-4e54-b68e-262a3b4d998a.png?w=500&h=500&fit=crop&crop=entropy&auto=compress,format&format=webp 60w" sizes="60px" src="https://cdn.hashnode.com/res/hashnode/image/upload/v1769591816718/c151b08b-2f7b-4e54-b68e-262a3b4d998a.png?w=500&h=500&fit=crop&crop=entropy&auto=compress,format&format=webp" class="author-profile-image" alt="Bhavin Sheth" width="507" height="492" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/allinonetools/" data-test-label="profile-link">
                    
                        Bhavin Sheth
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/18191d9d-9abf-44a3-8330-e452ce7194c2.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/18191d9d-9abf-44a3-8330-e452ce7194c2.png" alt="How to Build a Browser-Based PDF Redaction Tool Using JavaScript" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>PDF documents are frequently used to share invoices, contracts, reports, legal records, customer documents, financial statements, and internal business files. But before these documents are shared, they may contain information that shouldn't be visible to the recipient.</p>
<p>An invoice might include an account number. A customer document may contain a home address or phone number. A legal file could reveal confidential case information, while an internal report may contain names, references, or business data intended only for employees.</p>
<p>This is where PDF redaction becomes useful.</p>
<p>Redaction allows users to select sensitive areas of a document and permanently cover those areas before creating a new PDF. A practical redaction tool should also support multiple redaction areas, page selection, document preview, and final output verification.</p>
<p>In this tutorial, you'll build a browser-based PDF Redaction Tool using JavaScript. Users will upload a PDF, navigate through its pages, draw redaction boxes directly on the document preview, manage multiple redactions, apply them to selected pages, preview the processed document, rename the final file, and download the redacted PDF.</p>
<p>The entire workflow runs inside the browser. This is particularly useful for privacy-focused document tools because PDF processing can happen locally without requiring a backend server.</p>
<p>By the end of this tutorial, you'll understand not only how to draw redaction areas but also how to translate browser coordinates into PDF coordinates and apply those selections to the actual document.</p>
<h3 id="heading-table-of-contents">Table of Contents</h3>
<ul>
<li><p><a href="#heading-redaction-is-not-the-same-as-drawing-a-black-box">Redaction Is Not the Same as Drawing a Black Box</a></p>
</li>
<li><p><a href="#heading-how-browser-based-pdf-redaction-works">How Browser-Based PDF Redaction Works</a></p>
</li>
<li><p><a href="#heading-understanding-pdf-and-canvas-coordinates">Understanding PDF and Canvas Coordinates</a></p>
</li>
<li><p><a href="#heading-project-setup">Project Setup</a></p>
</li>
<li><p><a href="#heading-what-libraries-are-we-using">What Libraries Are We Using?</a></p>
</li>
<li><p><a href="#heading-creating-the-pdf-upload-interface">Creating the PDF Upload Interface</a></p>
</li>
<li><p><a href="#heading-previewing-uploaded-pdf-pages">Previewing Uploaded PDF Pages</a></p>
</li>
<li><p><a href="#heading-drawing-redaction-areas-on-the-pdf">Drawing Redaction Areas on the PDF</a></p>
</li>
<li><p><a href="#heading-storing-and-managing-redactions">Storing and Managing Redactions</a></p>
</li>
<li><p><a href="#heading-applying-redactions-to-selected-pages">Applying Redactions to Selected Pages</a></p>
</li>
<li><p><a href="#heading-generating-the-redacted-pdf">Generating the Redacted PDF</a></p>
</li>
<li><p><a href="#heading-previewing-and-renaming-the-final-pdf">Previewing and Renaming the Final PDF</a></p>
</li>
<li><p><a href="#heading-downloading-the-final-pdf">Downloading the Final PDF</a></p>
</li>
<li><p><a href="#heading-demo-how-the-pdf-redaction-tool-works">Demo: How the PDF Redaction Tool Works</a></p>
</li>
<li><p><a href="#heading-how-to-verify-the-redacted-pdf">How to Verify the Redacted PDF</a></p>
</li>
<li><p><a href="#heading-performance-optimization-tips">Performance Optimization Tips</a></p>
</li>
<li><p><a href="#heading-important-notes-and-common-mistakes">Important Notes and Common Mistakes</a></p>
</li>
<li><p><a href="#heading-conclusion">Conclusion</a></p>
</li>
</ul>
<h2 id="heading-redaction-is-not-the-same-as-drawing-a-black-box">Redaction Is Not the Same as Drawing a Black Box</h2>
<p>A common mistake is assuming that placing a black rectangle over text automatically makes the information secure.</p>
<p>Visually, the document may look redacted. But depending on how the PDF is modified, the original text or image content may still exist underneath the rectangle.</p>
<p>For example, imagine adding a black box as a new annotation layer above an account number. The number is no longer visible on the page, but the underlying PDF content may still be present.</p>
<p>In some poorly redacted documents, users may be able to select, copy, search, or recover the hidden content.</p>
<p>This is why redaction must be treated differently from simple visual decoration.</p>
<p>In our browser-based workflow, the selected areas are applied while generating the processed PDF. The final document should then be reviewed carefully before it's shared.</p>
<p>Never assume that a black rectangle alone guarantees secure removal of underlying PDF content. For high-security or legally sensitive documents, the final file should be validated with a dedicated redaction verification process.</p>
<h2 id="heading-how-browser-based-pdf-redaction-works">How Browser-Based PDF Redaction Works</h2>
<p>The redaction workflow can be divided into a few clear stages.</p>
<p>First, the browser reads the uploaded PDF and renders a page preview. The preview gives users a visual surface where they can identify sensitive information.</p>
<p>Next, users click and drag over the preview to create redaction rectangles.</p>
<p>Each rectangle is stored as a set of coordinates.</p>
<pre><code class="language-javascript">const redaction = {
    page: 7,
    x: 420,
    y: 35,
    width: 310,
    height: 220
};
</code></pre>
<p>The application can store multiple rectangles for the same page.</p>
<pre><code class="language-javascript">redactions.push(redaction);
</code></pre>
<p>When users click <strong>Apply &amp; Finalize</strong>, the application determines which pages should receive the selected redactions.</p>
<p>The redaction coordinates are then converted from preview coordinates to actual PDF page coordinates. Finally, the application modifies the PDF and generates a new document for preview and download.</p>
<p>The overall workflow looks like this:</p>
<pre><code class="language-text">Upload PDF
    ↓
Render Page Preview
    ↓
Draw Redaction Areas
    ↓
Store Coordinates
    ↓
Select Target Pages
    ↓
Apply Redactions
    ↓
Generate New PDF
    ↓
Preview and Download
</code></pre>
<p>Separating the interface from the PDF processing logic makes the application easier to manage and debug.</p>
<h2 id="heading-understanding-pdf-and-canvas-coordinates">Understanding PDF and Canvas Coordinates</h2>
<p>One of the most important technical parts of this project is coordinate conversion.</p>
<p>The PDF page shown inside the browser is usually scaled to fit the available screen space. A PDF page may have an actual width of 842 points, while the browser preview is displayed at only 600 pixels wide.</p>
<p>This means a rectangle drawn at <code>x = 300</code> on the preview can't simply be placed at <code>x = 300</code> in the PDF.</p>
<p>We'll first calculate the scale difference.</p>
<pre><code class="language-javascript">const scaleX =
    pdfPageWidth / canvasWidth;

const scaleY =
    pdfPageHeight / canvasHeight;
</code></pre>
<p>The selected rectangle can then be converted.</p>
<pre><code class="language-javascript">const pdfX =
    redaction.x * scaleX;

const pdfWidth =
    redaction.width * scaleX;

const pdfHeight =
    redaction.height * scaleY;
</code></pre>
<p>The Y coordinate requires extra attention because browser canvases and PDF pages commonly use different coordinate origins.</p>
<p>Canvas coordinates generally begin at the top-left corner. PDF coordinates commonly work from the bottom-left.</p>
<p>The Y position can therefore be converted like this:</p>
<pre><code class="language-javascript">const pdfY =
    pdfPageHeight -
    ((redaction.y + redaction.height) * scaleY);
</code></pre>
<p>This small calculation is critical.</p>
<p>Without correct coordinate conversion, a redaction box drawn over a phone number might appear several centimeters away from that number in the generated PDF.</p>
<p>Accurate coordinate mapping ensures that the redaction users draw in the browser matches the same area in the final document.</p>
<h2 id="heading-project-setup">Project Setup</h2>
<p>We'll keep the project structure simple because the redaction workflow runs entirely inside the browser.</p>
<p>Create a new project folder with three files:</p>
<pre><code class="language-text">pdf-redaction-tool/
│
├── index.html
├── style.css
└── script.js
</code></pre>
<p>The <code>index.html</code> file contains the upload interface, PDF preview, redaction controls, and final download section.</p>
<p>The <code>style.css</code> file handles the page layout and redaction overlay styling.</p>
<p>The <code>script.js</code> file contains the PDF loading, rendering, coordinate tracking, redaction management, and final PDF generation logic.</p>
<p>Start with a basic HTML structure.</p>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;

&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;

    &lt;meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"&gt;

    &lt;title&gt;PDF Redaction Tool&lt;/title&gt;

    &lt;link
        rel="stylesheet"
        href="style.css"&gt;
&lt;/head&gt;

&lt;body&gt;

    &lt;main id="app"&gt;

        &lt;section id="uploadSection"&gt;&lt;/section&gt;

        &lt;section id="editorSection"&gt;&lt;/section&gt;

        &lt;section id="resultSection"&gt;&lt;/section&gt;

    &lt;/main&gt;

    &lt;script src="script.js"&gt;&lt;/script&gt;

&lt;/body&gt;

&lt;/html&gt;
</code></pre>
<p>Separating the upload, editor, and result sections makes it easier to show and hide different parts of the interface as users move through the redaction workflow.</p>
<h2 id="heading-what-libraries-are-we-using">What Libraries Are We Using?</h2>
<p>We'll use <strong>PDF.js</strong> and <strong>PDF-lib</strong> for this project.</p>
<p>PDF.js handles PDF loading and page rendering. It allows us to display an uploaded PDF page inside a canvas so users can visually select the areas they want to redact.</p>
<p>PDF-lib handles the final document modification. After the user creates redaction areas, PDF-lib opens the original PDF, accesses the selected pages, and applies the redaction rectangles before generating a new file.</p>
<p>Add both libraries before your main JavaScript file.</p>
<pre><code class="language-html">&lt;script
src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"&gt;
&lt;/script&gt;

&lt;script
src="https://cdn.jsdelivr.net/npm/pdf-lib/dist/pdf-lib.min.js"&gt;
&lt;/script&gt;

&lt;script src="script.js"&gt;&lt;/script&gt;
</code></pre>
<p>Configure the PDF.js worker.</p>
<pre><code class="language-javascript">pdfjsLib.GlobalWorkerOptions.workerSrc =
    "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js";
</code></pre>
<p>We'll also create a few variables for storing the active document and redaction data.</p>
<pre><code class="language-javascript">let pdfDocument = null;

let pdfBytes = null;

let currentPage = 1;

let redactions = {};
</code></pre>
<p>Instead of storing every redaction in one flat array, we can organize them by page number.</p>
<pre><code class="language-javascript">redactions = {
    1: [],
    2: [],
    7: []
};
</code></pre>
<p>This structure makes page navigation and per-page redaction management much easier.</p>
<h2 id="heading-creating-the-pdf-upload-interface">Creating the PDF Upload Interface</h2>
<p>The first screen users see is the PDF upload area.</p>
<p>Users can drag a document onto the upload box or click the <strong>Select PDF</strong> button to open the browser's file picker.</p>
<p>Create the upload interface.</p>
<pre><code class="language-html">&lt;section id="uploadSection"&gt;

    &lt;h1&gt;PDF Redaction Tool&lt;/h1&gt;

    &lt;p&gt;
        Upload your PDF to permanently black out
        sensitive information.
    &lt;/p&gt;

    &lt;div id="dropZone" class="drop-zone"&gt;

        &lt;div class="upload-icon"&gt;☁&lt;/div&gt;

        &lt;h2&gt;Drag &amp; Drop PDF Here&lt;/h2&gt;

        &lt;p&gt;Or click to browse file&lt;/p&gt;

        &lt;button id="selectPdfButton"&gt;
            Select PDF
        &lt;/button&gt;

        &lt;input
            id="pdfInput"
            type="file"
            accept="application/pdf"
            hidden&gt;

    &lt;/div&gt;

&lt;/section&gt;
</code></pre>
<p>Connect the button to the hidden file input.</p>
<pre><code class="language-javascript">const pdfInput =
    document.getElementById("pdfInput");

const selectPdfButton =
    document.getElementById("selectPdfButton");

selectPdfButton.addEventListener("click", () =&gt; {

    pdfInput.click();

});
</code></pre>
<p>Next, listen for file selection.</p>
<pre><code class="language-javascript">pdfInput.addEventListener("change", async event =&gt; {

    const file = event.target.files[0];

    if (!file) {
        return;
    }

    await loadPdfFile(file);

});
</code></pre>
<p>Before loading the document, validate the selected file.</p>
<pre><code class="language-javascript">async function loadPdfFile(file) {

    if (file.type !== "application/pdf") {

        alert("Please select a valid PDF file.");

        return;

    }

    pdfBytes =
        await file.arrayBuffer();

}
</code></pre>
<p>We can also support drag-and-drop uploads.</p>
<pre><code class="language-javascript">dropZone.addEventListener("dragover", event =&gt; {

    event.preventDefault();

    dropZone.classList.add("dragging");

});

dropZone.addEventListener("dragleave", () =&gt; {

    dropZone.classList.remove("dragging");

});

dropZone.addEventListener("drop", async event =&gt; {

    event.preventDefault();

    dropZone.classList.remove("dragging");

    const file =
        event.dataTransfer.files[0];

    if (file) {

        await loadPdfFile(file);

    }

});
</code></pre>
<p>After reading the file, load it with PDF.js.</p>
<pre><code class="language-javascript">pdfDocument =
    await pdfjsLib
        .getDocument({
            data: pdfBytes.slice(0)
        })
        .promise;

currentPage = 1;

await renderPage(currentPage);
</code></pre>
<p>At this point, the document is ready for preview and redaction.</p>
<img src="https://cdn.hashnode.com/uploads/covers/6979d22f93bc273cc33971b1/0a6bd531-08d2-4619-a84a-512cc3a4a698.png" alt="PDF Redaction Tool upload interface with drag-and-drop area and Select PDF button." style="display:block;margin:0 auto" width="640" height="654" loading="lazy">

<h2 id="heading-previewing-uploaded-pdf-pages">Previewing Uploaded PDF Pages</h2>
<p>Once the PDF has loaded, the application displays the current page inside a canvas.</p>
<p>The canvas serves two purposes. First, it gives users an accurate preview of the document. Second, it becomes the visual surface where redaction rectangles will be drawn.</p>
<p>Create the editor preview.</p>
<pre><code class="language-html">&lt;section id="editorSection"&gt;

    &lt;div class="preview-wrapper"&gt;

        &lt;div id="pageContainer"&gt;

            &lt;canvas id="pdfCanvas"&gt;&lt;/canvas&gt;

            &lt;div id="redactionLayer"&gt;&lt;/div&gt;

        &lt;/div&gt;

        &lt;div class="page-navigation"&gt;

            &lt;button id="previousPage"&gt;
                &amp;lt;
            &lt;/button&gt;

            &lt;span id="pageInfo"&gt;
                Page 1 of 1
            &lt;/span&gt;

            &lt;button id="nextPage"&gt;
                &amp;gt;
            &lt;/button&gt;

        &lt;/div&gt;

    &lt;/div&gt;

&lt;/section&gt;
</code></pre>
<p>The <code>pdfCanvas</code> displays the PDF page.</p>
<p>The <code>redactionLayer</code> sits above the canvas and contains the selection boxes created by the user.</p>
<p>Render the active page using PDF.js.</p>
<pre><code class="language-javascript">async function renderPage(pageNumber) {

    const page =
        await pdfDocument.getPage(pageNumber);

    const viewport =
        page.getViewport({
            scale: 1.4
        });

    const canvas =
        document.getElementById("pdfCanvas");

    const context =
        canvas.getContext("2d");

    canvas.width =
        viewport.width;

    canvas.height =
        viewport.height;

    await page.render({

        canvasContext: context,

        viewport: viewport

    }).promise;

    updatePageInformation();

    renderSavedRedactions();

}
</code></pre>
<p>Update the page navigation information.</p>
<pre><code class="language-javascript">function updatePageInformation() {

    document
        .getElementById("pageInfo")
        .textContent =
        `Page ${currentPage} of ${pdfDocument.numPages}`;

}
</code></pre>
<p>Users can move to the previous page.</p>
<pre><code class="language-javascript">previousPage.addEventListener("click", async () =&gt; {

    if (currentPage &lt;= 1) {
        return;
    }

    currentPage--;

    await renderPage(currentPage);

});
</code></pre>
<p>The next-page button works in the same way.</p>
<pre><code class="language-javascript">nextPage.addEventListener("click", async () =&gt; {

    if (
        currentPage &gt;= pdfDocument.numPages
    ) {
        return;
    }

    currentPage++;

    await renderPage(currentPage);

});
</code></pre>
<p>Whenever users change pages, the canvas renders the selected PDF page and restores any redaction boxes already saved for that page.</p>
<p>This is important because redactions are page-specific. A rectangle created on page 7 should not automatically appear on page 8 unless the user later chooses to apply that selection to multiple pages.</p>
<img src="https://cdn.hashnode.com/uploads/covers/6979d22f93bc273cc33971b1/1cd5c990-ba70-490e-8904-6870d9c7c38c.png" alt="Alt Text: Uploaded PDF page preview with previous and next page navigation controls in the PDF Redaction Tool." style="display:block;margin:0 auto" width="642" height="539" loading="lazy">

<p>The PDF is now loaded, rendered, and ready for user interaction.</p>
<h2 id="heading-drawing-redaction-areas-on-the-pdf">Drawing Redaction Areas on the PDF</h2>
<p>Now that the PDF page is visible, users need a simple way to mark the information they want to hide.</p>
<p>In this project, users can click and drag directly over the page preview to create a redaction rectangle. The interaction is similar to selecting an area in an image editor.</p>
<p>We'll first track the starting position of the pointer.</p>
<pre><code class="language-javascript">let isDrawing = false;

let startX = 0;
let startY = 0;

let activeBox = null;
</code></pre>
<p>Listen for the pointer-down event on the redaction layer.</p>
<pre><code class="language-javascript">redactionLayer.addEventListener(
    "pointerdown",
    event =&gt; {

        isDrawing = true;

        const bounds =
            redactionLayer.getBoundingClientRect();

        startX =
            event.clientX - bounds.left;

        startY =
            event.clientY - bounds.top;

        activeBox =
            document.createElement("div");

        activeBox.className =
            "redaction-box";

        activeBox.style.left =
            `${startX}px`;

        activeBox.style.top =
            `${startY}px`;

        redactionLayer.appendChild(activeBox);

    }
);
</code></pre>
<p>As the pointer moves, update the rectangle dimensions.</p>
<pre><code class="language-javascript">redactionLayer.addEventListener(
    "pointermove",
    event =&gt; {

        if (!isDrawing) {
            return;
        }

        const bounds =
            redactionLayer.getBoundingClientRect();

        const currentX =
            event.clientX - bounds.left;

        const currentY =
            event.clientY - bounds.top;

        const width =
            Math.abs(currentX - startX);

        const height =
            Math.abs(currentY - startY);

        activeBox.style.width =
            `${width}px`;

        activeBox.style.height =
            `${height}px`;

        activeBox.style.left =
            `${Math.min(startX, currentX)}px`;

        activeBox.style.top =
            `${Math.min(startY, currentY)}px`;

    }
);
</code></pre>
<p>The <code>Math.min()</code> calls are important because users may drag in any direction. They can begin at the top-left and move down, or start at the bottom-