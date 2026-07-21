---
source_url: https://www.freecodecamp.org/news/build-pdf-signature-tool-javascript/
ingested: 2026-07-20
sha256: f4a3a3bb2989a6c9a01e78ccf67aad94e132440989e9704614ed463c77e17806
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Build a Browser-Based PDF Signature Tool Using JavaScript</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/build-pdf-signature-tool-javascript/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="PDF documents are commonly used for agreements, forms, approvals, invoices, reports, applications, and other documents that may need a signature or additional text before they are shared. A traditiona">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Build a Browser-Based PDF Signature Tool Using JavaScript">
    
        <meta property="og:description" content="PDF documents are commonly used for agreements, forms, approvals, invoices, reports, applications, and other documents that may need a signature or additional text before they are shared. A traditiona">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/build-pdf-signature-tool-javascript/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/175ab1f9-2917-4588-9e67-50607f6fa5a1.png">
    <meta property="article:published_time" content="2026-07-20T20:47:13.569Z">
    <meta property="article:modified_time" content="2026-07-20T20:47:13.569Z">
    
        <meta property="article:tag" content="JavaScript">
    
        <meta property="article:tag" content="Web Development">
    
        <meta property="article:tag" content="pdf">
    
        <meta property="article:tag" content="Tutorial">
    
        <meta property="article:tag" content="Hashnode">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    
        <meta property="article:author" content="AllInOneTools.net">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Build a Browser-Based PDF Signature Tool Using JavaScript">
    
        <meta name="twitter:description" content="PDF documents are commonly used for agreements, forms, approvals, invoices, reports, applications, and other documents that may need a signature or additional text before they are shared. A traditiona">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/build-pdf-signature-tool-javascript/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/175ab1f9-2917-4588-9e67-50607f6fa5a1.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Bhavin Sheth">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="JavaScript, Web Development, pdf, Tutorial, Hashnode">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/175ab1f9-2917-4588-9e67-50607f6fa5a1.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/build-pdf-signature-tool-javascript/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-20T20:47:13.569Z",
	"dateModified": "2026-07-20T20:47:13.569Z",
	"keywords": "JavaScript, Web Development, pdf, Tutorial, Hashnode",
	"description": "PDF documents are commonly used for agreements, forms, approvals, invoices, reports, applications, and other documents that may need a signature or additional text before they are shared.\nA traditiona",
	"headline": "How to Build a Browser-Based PDF Signature Tool Using JavaScript",
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-20T20:47:13.569Z">
                            July 20, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/javascript/">
                                #JavaScript
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Build a Browser-Based PDF Signature Tool Using JavaScript</h1>
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
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/175ab1f9-2917-4588-9e67-50607f6fa5a1.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/175ab1f9-2917-4588-9e67-50607f6fa5a1.png" alt="How to Build a Browser-Based PDF Signature Tool Using JavaScript" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>PDF documents are commonly used for agreements, forms, approvals, invoices, reports, applications, and other documents that may need a signature or additional text before they are shared.</p>
<p>A traditional workflow often involves printing the document, signing it by hand, scanning it again, and sending the new file. For a simple electronic signature, that process adds unnecessary steps.</p>
<p>In this tutorial, you'll build a browser-based PDF Signature Tool using JavaScript. Users will be able to upload a PDF, preview and navigate its pages, and add content directly to the document.</p>
<p>The application will support two main element types: <strong>Signature</strong> and <strong>Text/Stamp</strong>.</p>
<p>For signatures, users can draw directly in the browser, type their name and choose a signature style, or upload an existing signature image. For text-based elements, they can enter custom text or use preset stamps such as <strong>APPROVED</strong>, <strong>CONFIDENTIAL</strong>, <strong>DRAFT</strong>, and <strong>PAID</strong>.</p>
<p>After creating an element, users can position it on the PDF preview and adjust properties such as scale, rotation, opacity, font size, and color. The element can then be applied to the current page, every page, or a specific set of pages.</p>
<p>Once processing is complete, the application generates a new PDF for review. Users can preview the result, rename the output file, check its page count and file size, and download it directly from the browser.</p>
<p>The project uses PDF.js for document rendering and PDF-lib for modifying and generating the final PDF.</p>
<p>By the end of this tutorial, you'll understand how to build an interactive PDF editing workflow that combines canvas-based input, image embedding, text placement, coordinate conversion, page selection, and client-side file generation.</p>
<h3 id="heading-what-well-cover">What We'll Cover:</h3>
<ul>
<li><p><a href="#heading-what-this-pdf-signature-tool-can-do">What This PDF Signature Tool Can Do</a></p>
</li>
<li><p><a href="#heading-electronic-signatures-vs-digital-signatures">Electronic Signatures vs Digital Signatures</a></p>
</li>
<li><p><a href="#heading-how-the-browser-based-workflow-works">How the Browser-Based Workflow Works</a></p>
</li>
<li><p><a href="#heading-project-setup">Project Setup</a></p>
</li>
<li><p><a href="#heading-what-libraries-are-we-using">What Libraries Are We Using?</a></p>
</li>
<li><p><a href="#heading-uploading-and-previewing-the-pdf">Uploading and Previewing the PDF</a></p>
</li>
<li><p><a href="#heading-choosing-an-element-to-add">Choosing an Element to Add</a></p>
</li>
<li><p><a href="#heading-creating-a-signature">Creating a Signature</a></p>
</li>
<li><p><a href="#heading-drawing-a-signature">Drawing a Signature</a></p>
</li>
<li><p><a href="#heading-typing-a-signature">Typing a Signature</a></p>
</li>
<li><p><a href="#heading-uploading-a-signature-image">Uploading a Signature Image</a></p>
</li>
<li><p><a href="#heading-adding-text-and-preset-stamps">Adding Text and Preset Stamps</a></p>
</li>
<li><p><a href="#heading-positioning-and-styling-the-element">Positioning and Styling the Element</a></p>
</li>
<li><p><a href="#heading-applying-the-element-to-selected-pages">Applying the Element to Selected Pages</a></p>
</li>
<li><p><a href="#heading-applying-and-finalizing-the-pdf">Applying and Finalizing the PDF</a></p>
</li>
<li><p><a href="#heading-generating-the-signed-pdf">Generating the Signed PDF</a></p>
</li>
<li><p><a href="#heading-previewing-the-final-pdf">Previewing the Final PDF</a></p>
</li>
<li><p><a href="#heading-renaming-and-downloading-the-final-pdf">Renaming and Downloading the Final PDF</a></p>
</li>
<li><p><a href="#heading-demo-how-the-pdf-signature-tool-works">Demo: How the PDF Signature Tool Works</a></p>
</li>
<li><p><a href="#heading-handling-signature-transparency">Handling Signature Transparency</a></p>
</li>
<li><p><a href="#heading-important-notes-and-common-mistakes">Important Notes and Common Mistakes</a></p>
</li>
<li><p><a href="#heading-conclusion">Conclusion</a></p>
</li>
</ul>
<h2 id="heading-what-this-pdf-signature-tool-can-do">What This PDF Signature Tool Can Do</h2>
<p>The application provides a single editing workflow for adding signatures, text, and common document stamps to PDF pages.</p>
<p>When <strong>Signature</strong> is selected, users can create the signature in three different ways.</p>
<ol>
<li><p>The <strong>Draw</strong> option provides a canvas where the user can write a signature using a mouse, trackpad, stylus, or touch input.</p>
</li>
<li><p>The <strong>Type</strong> option converts entered text into a signature-style element. Users can type their name, adjust the size, and choose from the available signature styles.</p>
</li>
<li><p>The <strong>Upload</strong> option accepts an existing signature image. This is useful for someone who already has a transparent PNG or another supported image of their handwritten signature.</p>
</li>
</ol>
<p>The second element type is <strong>Text/Stamp</strong>. Users can enter custom text such as:</p>
<pre><code class="language-text">Signed on: 08-09-2025
</code></pre>
<p>They can also quickly choose a predefined stamp:</p>
<pre><code class="language-text">APPROVED
CONFIDENTIAL
DRAFT
PAID
</code></pre>
<p>After an element has been created, the application provides controls for its placement and appearance. Users can move it to the required location and adjust its scale, rotation, opacity, and position.</p>
<p>Text and stamp elements can additionally use configurable font sizes and colors.</p>
<p>The page controls determine where the selected element will be applied. A signature may belong only on the final page of a contract, while a <code>CONFIDENTIAL</code> stamp may need to appear on every page.</p>
<p>The application therefore supports:</p>
<pre><code class="language-text">Current page only
All pages
Specific pages
</code></pre>
<p>The goal is to provide one consistent workflow for several common PDF editing tasks without requiring separate tools for each element type.</p>
<h2 id="heading-electronic-signatures-vs-digital-signatures">Electronic Signatures vs Digital Signatures</h2>
<p>Before building the application, it's important to distinguish between an <strong>electronic signature</strong> and a <strong>digital signature</strong>.</p>
<p>The tool in this tutorial creates an electronic signature workflow.</p>
<p>A drawn signature, typed signature, or uploaded signature image is placed visually onto the PDF page. This is similar to signing a document by hand and inserting a visible representation of that signature into the file.</p>
<p>For example, a user might draw a signature on a canvas:</p>
<pre><code class="language-javascript">const signatureImage =
    signatureCanvas.toDataURL("image/png");
</code></pre>
<p>The generated image can then be embedded into the PDF.</p>
<p>A digital signature is technically different.</p>
<p>Certificate-based digital signatures use cryptographic methods to help verify document integrity and the identity associated with a signing certificate. They may involve digital certificates, private keys, signature validation, and trust chains.</p>
<p>Simply placing a handwritten signature image on a PDF doesn't create that type of cryptographic verification.</p>
<p>This distinction matters because the terms are sometimes used interchangeably in everyday conversation even though the underlying technologies are different.</p>
<p>The project we're building focuses on <strong>visual electronic signatures and document elements</strong>. It doesn't create certificate-based cryptographic digital signatures.</p>
<p>Keeping that distinction clear makes it easier to understand exactly what the application does and what would require a more advanced signing system.</p>
<h2 id="heading-how-the-browser-based-workflow-works">How the Browser-Based Workflow Works</h2>
<p>The process begins when a user selects a PDF file.</p>
<p>PDF.js loads the document and renders the current page into a browser canvas. Previous and next buttons allow the user to navigate through the PDF before choosing where to place an element.</p>
<p>The user then selects one of two element types:</p>
<pre><code class="language-text">Signature
Text/Stamp
</code></pre>
<p>If <strong>Signature</strong> is selected, the application provides three creation methods:</p>
<pre><code class="language-text">Draw
Type
Upload
</code></pre>
<p>The selected signature is converted into an element that can be displayed over the PDF preview.</p>
<p>If <strong>Text/Stamp</strong> is selected, the application instead creates a text element using either custom content or one of the predefined stamp values.</p>
<p>The complete workflow looks like this:</p>
<pre><code class="language-text">Upload PDF
    ↓
Render and Navigate Pages
    ↓
Choose Signature or Text/Stamp
    ↓
Create the Element
    ↓
Position and Style It
    ↓
Choose Target Pages
    ↓
Apply &amp; Finalize
    ↓
Generate the New PDF
    ↓
Preview the Result
    ↓
Rename and Download
</code></pre>
<p>During editing, the element displayed over the PDF preview is only a browser-side representation. Its position must later be translated into coordinates that match the actual PDF page.</p>
<p>For example, the application may store an element like this:</p>
<pre><code class="language-javascript">const element = {
    type: "signature",
    x: 622,
    y: 496,
    scale: 1.14,
    rotation: 0,
    opacity: 1
};
</code></pre>
<p>When the user clicks <strong>Apply &amp; Finalize</strong>, those values are used to calculate the final placement inside the PDF.</p>
<p>This separation between the interactive preview and the final PDF generation is the foundation of the project. It allows users to visually prepare the document first and create the modified PDF only after the placement is ready.</p>
<h2 id="heading-project-setup">Project Setup</h2>
<p>To keep the project easy to understand, we'll use three main files:</p>
<pre><code class="language-text">pdf-signature-tool/
│
├── index.html
├── style.css
└── script.js
</code></pre>
<p>The HTML file contains the upload interface, PDF preview, editing controls, final preview, and download section.</p>
<p>The CSS file handles the layout and visual states.</p>
<p>The JavaScript file manages PDF loading, page rendering, signature creation, text and stamp elements, positioning, final PDF generation, and downloading.</p>
<p>Start with the basic HTML structure:</p>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;

    &lt;meta charset="UTF-8"&gt;

    &lt;meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"&gt;

    &lt;title&gt;PDF Signature Tool&lt;/title&gt;

    &lt;link
        rel="stylesheet"
        href="style.css"&gt;

&lt;/head&gt;

&lt;body&gt;

    &lt;main class="pdf-signature-tool"&gt;

        &lt;section id="uploadSection"&gt;

            &lt;h1&gt;PDF Signature Tool&lt;/h1&gt;

            &lt;p&gt;
                Upload your PDF to add your
                electronic signature.
            &lt;/p&gt;

            &lt;div id="dropZone"&gt;

                &lt;p&gt;Drag &amp; Drop PDF Here&lt;/p&gt;

                &lt;p&gt;Or click to browse file&lt;/p&gt;

                &lt;button id="selectPdfButton"&gt;
                    Select PDF
                &lt;/button&gt;

                &lt;input
                    type="file"
                    id="pdfInput"
                    accept="application/pdf"
                    hidden&gt;

            &lt;/div&gt;

        &lt;/section&gt;

        &lt;section
            id="editorSection"
            hidden&gt;

            &lt;div class="pdf-preview"&gt;

                &lt;div id="previewContainer"&gt;

                    &lt;canvas id="pdfCanvas"&gt;&lt;/canvas&gt;

                    &lt;div id="elementLayer"&gt;&lt;/div&gt;

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

            &lt;aside id="editorControls"&gt;

                &lt;!-- Signature and text controls
                     will be added here --&gt;

            &lt;/aside&gt;

        &lt;/section&gt;

        &lt;section
            id="resultSection"
            hidden&gt;

            &lt;!-- Final preview and download
                 controls will be added here --&gt;

        &lt;/section&gt;

    &lt;/main&gt;

    &lt;script src="script.js"&gt;&lt;/script&gt;

&lt;/body&gt;
&lt;/html&gt;
</code></pre>
<p>The <code>previewContainer</code> is especially important.</p>
<p>It contains two layers:</p>
<pre><code class="language-text">PDF Canvas
    +
Interactive Element Layer
</code></pre>
<p>The PDF page is rendered onto the canvas, while signatures, text, and stamps are displayed in a separate overlay.</p>
<p>This allows users to move and style an element without modifying the original PDF every time they make a small adjustment.</p>
<p>The overlay should match the dimensions and position of the PDF canvas.</p>
<pre><code class="language-css">#previewContainer {
    position: relative;
    display: inline-block;
}

#pdfCanvas {
    display: block;
}

#elementLayer {
    position: absolute;
    inset: 0;
    pointer-events: none;
}
</code></pre>
<p>Individual signature and text elements can later enable their own pointer interactions.</p>
<pre><code class="language-css">.pdf-element {
    position: absolute;
    cursor: move;
    pointer-events: auto;
    transform-origin: center;
}
</code></pre>
<p>This layered structure becomes the foundation of the interactive editor.</p>
<h2 id="heading-what-libraries-are-we-using">What Libraries Are We Using?</h2>
<p>This project uses two JavaScript libraries for different parts of the PDF workflow.</p>
<h3 id="heading-pdfjs-for-rendering-and-previewing">PDF.js for Rendering and Previewing</h3>
<p>PDF.js is responsible for reading the uploaded document and rendering its pages inside the browser.</p>
<p>A page can be loaded like this:</p>
<pre><code class="language-javascript">const page =
    await pdfDocument.getPage(
        currentPage
    );
</code></pre>
<p>The page is then rendered to a canvas:</p>
<pre><code class="language-javascript">const viewport =
    page.getViewport({
        scale: 1.5
    });

const context =
    pdfCanvas.getContext("2d");

pdfCanvas.width =
    viewport.width;

pdfCanvas.height =
    viewport.height;

await page.render({

    canvasContext: context,

    viewport

}).promise;
</code></pre>
<p>PDF.js handles the visual preview.</p>
<h3 id="heading-pdf-lib-for-modifying-the-pdf">PDF-lib for Modifying the PDF</h3>
<p>PDF-lib is used later when the user clicks <strong>Apply &amp; Finalize</strong>.</p>
<p>It allows us to load the original PDF bytes and add content to its pages.</p>
<p>For example:</p>
<pre><code class="language-javascript">const pdfDoc =
    await PDFLib.PDFDocument.load(
        originalPdfBytes
    );
</code></pre>
<p>An uploaded PNG signature can then be embedded:</p>
<pre><code class="language-javascript">const signatureImage =
    await pdfDoc.embedPng(
        signatureBytes
    );
</code></pre>
<p>Text can also be drawn directly onto a PDF page:</p>
<pre><code class="language-javascript">page.drawText(
    "APPROVED",
    {
        x: 100,
        y: 100,
        size: 18
    }
);
</code></pre>
<p>The two libraries therefore have separate responsibilities:</p>
<pre><code class="language-text">PDF.js
→ Load and visually render PDF pages

PDF-lib
→ Modify pages and generate the final PDF
</code></pre>
<p>Separating these responsibilities keeps the editor easier to manage.</p>
<p>Include both libraries in the project before <code>script.js</code>.</p>
<pre><code class="language-html">&lt;script
    src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"&gt;
&lt;/script&gt;

&lt;script
    src="https://unpkg.com/pdf-lib/dist/pdf-lib.min.js"&gt;
&lt;/script&gt;

&lt;script src="script.js"&gt;&lt;/script&gt;
</code></pre>
<p>Configure the PDF.js worker as well:</p>
<pre><code class="language-javascript">pdfjsLib.GlobalWorkerOptions.workerSrc =
    "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js";
</code></pre>
<p>For a production project, pin and test the exact library versions you use rather than automatically loading an unspecified latest release.</p>
<h2 id="heading-uploading-and-previewing-the-pdf">Uploading and Previewing the PDF</h2>
<p>The first interactive step is accepting the user's PDF.</p>
<p>Get references to the required elements:</p>
<pre><code class="language-javascript">const pdfInput =
    document.getElementById(
        "pdfInput"
    );

const selectPdfButton =
    document.getElementById(
        "selectPdfButton"
    );

const dropZone =
    document.getElementById(
        "dropZone"
    );

const uploadSection =
    document.getElementById(
        "uploadSection"
    );

const editorSection =
    document.getElementById(
        "editorSection"
    );

const pdfCanvas =
    document.getElementById(
        "pdfCanvas"
    );
</code></pre>
<p>We also need a few variables to store the current document state.</p>
<pre><code class="language-javascript">let pdfDocument = null;

let originalPdfBytes = null;

let currentPage = 1;

let totalPages = 0;
</code></pre>
<p>Clicking the custom button opens the hidden file input.</p>
<pre><code class="language-javascript">selectPdfButton.addEventListener(
    "click",
    () =&gt; {

        pdfInput.click();

    }
);
</code></pre>
<p>When a file is selected, pass it to the PDF loading function.</p>
<pre><code class="language-javascript">pdfInput.addEventListener(
    "change",
    event =&gt; {

        const file =
            event.target.files[0];

        if (file) {

            loadPdf(file);

        }

    }
);
</code></pre>
<p>Before processing the file, validate its type.</p>
<pre><code class="language-javascript">async function loadPdf(file) {

    if (
        file.type !==
        "application/pdf"
    ) {

        alert(
            "Please select a valid PDF file."
        );

        return;

    }

}
</code></pre>
<p>Read the file as an <code>ArrayBuffer</code>.</p>
<pre><code class="language-javascript">const arrayBuffer =
    await file.arrayBuffer();
</code></pre>
<p>Keep a copy of the original bytes because PDF.js and PDF-lib will use the document at different stages.</p>
<pre><code class="language-javascript">originalPdfBytes =
    new Uint8Array(
        arrayBuffer
    );
</code></pre>
<p>Now load the document with PDF.js.</p>
<pre><code class="language-javascript">pdfDocument =
    await pdfjsLib
        .getDocument({
            data:
                originalPdfBytes.slice()
        })
        .promise;
</code></pre>
<p>Store the number of pages.</p>
<pre><code class="language-javascript">totalPages =
    pdfDocument.numPages;

currentPage = 1;
</code></pre>
<p>Switch from the upload interface to the editor.</p>
<pre><code class="language-javascript">uploadSection.hidden = true;

editorSection.hidden = false;
</code></pre>
<p>Finally, render the first page.</p>
<pre><code class="language-javascript">await renderPage(currentPage);
</code></pre>
<p>The complete loading function becomes:</p>
<pre><code class="language-javascript">async function loadPdf(file) {

    if (
        file.type !==
        "application/pdf"
    ) {

        alert(
            "Please select a valid PDF file."
        );

        return;

    }

    const arrayBuffer =
        await file.arrayBuffer();

    originalPdfBytes =
        new Uint8Array(
            arrayBuffer
        );

    pdfDocument =
        await pdfjsLib
            .getDocument({
                data:
                    originalPdfBytes.slice()
            })
            .promise;

    tota