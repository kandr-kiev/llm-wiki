---
source_url: https://www.freecodecamp.org/news/how-to-train-a-tumor-segmentation-model-on-ultrasound-data-with-monai/
ingested: 2026-07-22
sha256: bb0ed0527ade6b4e175e9c09048b8456a345b325c726d642e9f94ccf6fac5eb2
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Train a Tumor Segmentation Model on Ultrasound Data with MONAI</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-to-train-a-tumor-segmentation-model-on-ultrasound-data-with-monai/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="Most segmentation tutorials begin by choosing a model, feeding images into it, and tuning hyperparameters until the metric improves. But this skips the step that often matters most: understanding the ">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Train a Tumor Segmentation Model on Ultrasound Data with MONAI">
    
        <meta property="og:description" content="Most segmentation tutorials begin by choosing a model, feeding images into it, and tuning hyperparameters until the metric improves. But this skips the step that often matters most: understanding the ">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-to-train-a-tumor-segmentation-model-on-ultrasound-data-with-monai/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/3e7cfe47-858c-4ce9-b8f9-1c5fc22f29b7.png">
    <meta property="article:published_time" content="2026-07-22T16:53:24.986Z">
    <meta property="article:modified_time" content="2026-07-22T16:53:24.986Z">
    
        <meta property="article:tag" content="Healthcare AI">
    
        <meta property="article:tag" content="Machine Learning">
    
        <meta property="article:tag" content="Medical Imaging">
    
        <meta property="article:tag" content="Deep Learning">
    
        <meta property="article:tag" content="monai">
    
        <meta property="article:tag" content="medical image segmentation">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Train a Tumor Segmentation Model on Ultrasound Data with MONAI">
    
        <meta name="twitter:description" content="Most segmentation tutorials begin by choosing a model, feeding images into it, and tuning hyperparameters until the metric improves. But this skips the step that often matters most: understanding the ">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-to-train-a-tumor-segmentation-model-on-ultrasound-data-with-monai/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/3e7cfe47-858c-4ce9-b8f9-1c5fc22f29b7.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Lakshmi Mahabaleshwara">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="Healthcare AI, Machine Learning, Medical Imaging, Deep Learning, monai, medical image segmentation">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/3e7cfe47-858c-4ce9-b8f9-1c5fc22f29b7.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-to-train-a-tumor-segmentation-model-on-ultrasound-data-with-monai/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-22T16:53:24.986Z",
	"dateModified": "2026-07-22T16:53:24.986Z",
	"keywords": "Healthcare AI, Machine Learning, Medical Imaging, Deep Learning, monai, medical image segmentation",
	"description": "Most segmentation tutorials begin by choosing a model, feeding images into it, and tuning hyperparameters until the metric improves. But this skips the step that often matters most: understanding the ",
	"headline": "How to Train a Tumor Segmentation Model on Ultrasound Data with MONAI",
	"author": {
		"@type": "Person",
		"name": "Lakshmi Mahabaleshwara",
		"url": "https://www.freecodecamp.org/news/author/lakshmi-mahabalesh/",
		"sameAs": [],
		"image": {
			"@type": "ImageObject",
			"url": "https://avatars.githubusercontent.com/u/17552390?v=4",
			"width": 460,
			"height": 460
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-22T16:53:24.986Z">
                            July 22, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/healthcare-ai/">
                                #Healthcare AI
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Train a Tumor Segmentation Model on Ultrasound Data with MONAI</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://avatars.githubusercontent.com/u/17552390?v=4 60w" sizes="60px" src="https://avatars.githubusercontent.com/u/17552390?v=4" class="author-profile-image" alt="Lakshmi Mahabaleshwara" width="460" height="460" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/lakshmi-mahabalesh/" data-test-label="profile-link">
                    
                        Lakshmi Mahabaleshwara
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/3e7cfe47-858c-4ce9-b8f9-1c5fc22f29b7.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/3e7cfe47-858c-4ce9-b8f9-1c5fc22f29b7.png" alt="How to Train a Tumor Segmentation Model on Ultrasound Data with MONAI" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>Most segmentation tutorials begin by choosing a model, feeding images into it, and tuning hyperparameters until the metric improves. But this skips the step that often matters most: understanding the data.</p>
<p>In this tutorial we’ll profile the dataset first, then let those observations drive every design decision in a MONAI segmentation pipeline.</p>
<h2 id="heading-what-well-cover">What We'll Cover:</h2>
<ul>
<li><p><a href="#heading-who-is-this-for">Who is This For?</a></p>
</li>
<li><p><a href="#heading-about-the-dataset">About the Dataset</a></p>
</li>
<li><p><a href="#heading-what-is-monai-and-why-use-it">What is MONAI, and Why Use it?</a></p>
</li>
<li><p><a href="#heading-what-is-dice">What is Dice?</a></p>
</li>
<li><p><a href="#heading-part-1-data-profile-before-modeling">Part 1 — Data Profile Before Modeling</a></p>
<ul>
<li><p><a href="#heading-class-balance-drives-the-toss">Class Balance Drives the Toss</a></p>
</li>
<li><p><a href="#heading-patient-counts-drive-the-split">Patient Counts Drive the Split</a></p>
</li>
</ul>
</li>
<li><p><a href="#heading-part-2-building-the-pipeline">Part 2 — Building the Pipeline</a></p>
<ul>
<li><p><a href="#heading-a-single-config-object">A Single Config Object</a></p>
</li>
<li><p><a href="#heading-the-patient-grouped-split">The Patient-grouped Split</a></p>
</li>
<li><p><a href="#heading-transforms-chosen-by-the-snapshot">Transforms, Chosen by the Snapshot</a></p>
</li>
<li><p><a href="#heading-model-loss-and-metric">Model, Loss, and Metric</a></p>
</li>
</ul>
</li>
<li><p><a href="#heading-reading-the-results">Reading the Results</a></p>
</li>
<li><p><a href="#heading-prediction-visualization">Prediction Visualization</a></p>
</li>
<li><p><a href="#heading-the-failure-modes-matter-more-than-the-average">The Failure Modes Matter More Than the Average</a></p>
</li>
<li><p><a href="#heading-where-to-go-next">Where to Go Next</a></p>
</li>
<li><p><a href="#heading-takeaway">Takeaway</a></p>
</li>
<li><p><a href="#heading-reference">Reference</a></p>
</li>
</ul>
<h2 id="heading-who-is-this-for">Who is This For?</h2>
<p>This walkthrough assumes you have some comfort with Python and the basics of training a neural network. It explains the MONAI-specific pieces (dictionary transforms, <code>DiceCELoss</code>, <code>DiceMetric</code>) and the medical-imaging terms (BI-RADS, hypoechoic, patient-grouped folds) as they come up. No prior ultrasound experience is needed.</p>
<h2 id="heading-about-the-dataset">About the Dataset</h2>
<p>The dataset is <a href="https://www.kaggle.com/datasets/orvile/bus-bra-a-breast-ultrasound-dataset">BUS-BRA</a>, a public collection of breast ultrasound images with biopsy-proven labels and tumor segmentation masks.</p>
<p>Each image carries a benign/malignant label, a BI-RADS (Breast Imaging Reporting and Data System)&nbsp;category (a radiologist's suspicion score from 2 to 5), a histology string, and a binary tumor mask. The CSV that ships with it also includes predefined cross-validation folds.</p>
<p>The task is binary: separate tumor from background. BUS-BRA contains 1,875 B-mode breast ultrasound images from 1,064 patients, acquired on four scanners at a cancer institute in Brazil.</p>
<img src="https://cdn.hashnode.com/uploads/covers/69fd77e89f93a850a46d376f/24ecadc1-13ff-4dfb-a6fc-61ab03785a7e.png" alt="Example from the BUS-BRA dataset showing a breast ultrasound image, its binary tumor segmentation mask, and the mask overlaid on the original image." style="display:block;margin:0 auto" width="640" height="409" loading="lazy">

<h2 id="heading-what-is-monai-and-why-use-it">What is MONAI, and Why Use it?</h2>
<p>MONAI (Medical Open Network for AI) is an open-source PyTorch framework built specifically for medical imaging. It's a domain-specific layer that sits on top of PyTorch: you still write standard PyTorch training loops, but MONAI provides the medical imaging-specific components so you don't have to build them yourself.</p>
<p>It gives you:</p>
<ul>
<li><p><strong>Transforms</strong> for medical data, loading formats like DICOM and NIfTI, normalizing intensities, resizing, and augmenting, all in a dictionary-based pipeline that keeps an image and its mask in sync.</p>
</li>
<li><p><strong>Network architectures</strong> common in medical segmentation (U-Net, UNETR, SegResNet, and others) ready to instantiate.</p>
</li>
<li><p><strong>Loss functions and metrics</strong> designed for segmentation, including Dice-based losses and the Dice metric.</p>
</li>
</ul>
<p>The result is less boilerplate and fewer chances for an image and its mask to drift out of alignment.</p>
<h2 id="heading-what-is-dice">What is Dice?</h2>
<p>Dice (the Dice similarity coefficient) measures how much two regions overlap. In segmentation, it compares the model's predicted mask against the ground-truth mask and returns a score from 0 to 1: 0 means no overlap at all, 1 means a perfect match.</p>
<p>The formula is:</p>
<p><code>Dice = 2 × (overlap) / (predicted area + true area)</code></p>
<p>The "2 ×" in the numerator is what keeps the score in the 0-to-1 range even though the denominator counts the overlapping pixels on both sides.</p>
<p>Two roles it plays in this tutorial:</p>
<ul>
<li><p>As a <strong>metric</strong>, Dice is how the run is scored. A validation Dice of 0.876 means the predicted tumor masks overlap the true masks by about 88% on average.</p>
</li>
<li><p>As a <strong>loss</strong> (<code>DiceCELoss</code>), a Dice-based term is what the model trains against. This is the part that matters for the class-imbalance problem: because Dice measures overlap rather than per-pixel correctness, a model can't score well by labeling everything as background. A small tumor counts as much as a large one, so the model is pushed to actually find the tumor region.</p>
</li>
</ul>
<h2 id="heading-part-1-data-profile-before-modeling">Part 1 — Data Profile Before Modeling</h2>
<p>This first pass is data profiling. It reads every image and mask once and answers a short list of questions whose answers determine how the pipeline must be built. Running these checks takes a few seconds and saves a lot of guesswork later.</p>
<p>The snapshot below summarizes the properties that directly influenced the pipeline design. We’ll let these observations determine each step of the workflow.</p>
<table>
<thead>
<tr>
<th>What the snapshot measured</th>
<th>The number</th>
<th>What it forces</th>
</tr>
</thead>
<tbody><tr>
<td>Distinct image resolutions</td>
<td>Hundreds of different (width, height) pairs</td>
<td>Images must be resized to a fixed size before batching</td>
</tr>
<tr>
<td>Class balance</td>
<td>Background : foreground ≈ 10.6 : 1</td>
<td>A plain pixel-wise loss may converge toward predicting mostly background because doing so already yields high pixel accuracy on this imbalanced dataset.</td>
</tr>
<tr>
<td>Per-image brightness</td>
<td>Wide spread across the dataset</td>
<td>Intensity normalization belongs in the transform pipeline</td>
</tr>
<tr>
<td>Patients vs. images</td>
<td>1,064 patients, 1,875 images (paired left/right views)</td>
<td>Splits must be grouped by patient, or the same person leaks across train and validation</td>
</tr>
<tr>
<td>Mask components</td>
<td>Every mask is a single connected region</td>
<td>A prediction with several disconnected blobs is provably wrong</td>
</tr>
<tr>
<td>Pixel format</td>
<td>Images are 8-bit grayscale, masks are 1-bit binary</td>
<td>Load as single-channel, binarize the mask after loading</td>
</tr>
</tbody></table>
<p>Two of these deserve a closer look because they shape the two most important decisions.</p>
<h3 id="heading-class-balance-drives-the-toss">Class Balance Drives the Toss</h3>
<p>Tumors are small. Across the dataset, background pixels outnumber tumor pixels by more than ten to one.</p>
<p>A model trained with ordinary binary cross-entropy can score around 91% pixel accuracy by labeling everything as background. This high number reflects the imbalance rather than any ability to find the tumor.</p>
<p>The fix is a loss that rewards overlap with the actual tumor region, which points directly at Dice.</p>
<img src="https://cdn.hashnode.com/uploads/covers/69fd77e89f93a850a46d376f/69c14498-7119-4f15-a29b-9bf34fdcd51f.png" alt="Bar chart comparing foreground and background pixels in the BUS-BRA dataset. Background pixels outnumber tumor pixels by approximately 10.6 to 1, illustrating the strong class imbalance." style="display:block;margin:0 auto" width="1731" height="649" loading="lazy">

<h3 id="heading-patient-counts-drive-the-split">Patient Counts Drive the Split</h3>
<p>There are fewer patients than images because many patients contribute both a left-side and a right-side scan. If a random split puts one patient's left scan in training and their right scan in validation, the validation score is inflated by leakage.</p>
<p>The dataset authors already solved this: the CSV ships a <code>K5P</code> column: a 5-fold split where <strong>P</strong> stands for patient-grouped, meaning every image from a given patient lands in the same fold. Reusing it is safer than rebuilding the same grouping by hand.</p>
<p>With those answers in hand, the pipeline has a specification to build now.</p>
<h2 id="heading-part-2-building-the-pipeline">Part 2 — Building the Pipeline</h2>
<p>Everything below uses MONAI for the segmentation-specific work:<br>transforms, dataset wrapping, the network, the loss, and the metric.</p>
<h3 id="heading-a-single-config-object">A Single Config Object</h3>
<p>The pipeline reads all its knobs from one dataclass. Nothing downstream hard-codes a constant, so re-running an experiment with a different fold or image size is a single edit.</p>
<pre><code class="language-python">from dataclasses import dataclass
from typing import Tuple, Optional
from pathlib import Path

@dataclass
class TrainConfig:
    data_root: Optional[Path] = None
     fold_column: str = "K5P"          # patient-grouped 5-fold (dev set)
    val_fold: int = 1                 # which K5P fold is validation
    test_column: str = "HOP"          # patient-grouped hold-out partition
    test_group: int = 1               # HOP value reserved as the test set

    image_size: Tuple[int, int] = (256, 256)
    batch_size: int = 16
    lr: float = 1e-3
    epochs: int = 30
    use_amp: bool = True              # mixed precision
    ckpt_path: str = "best_model.pt"

cfg = TrainConfig()
</code></pre>
<p>The code above defines a <code>TrainConfig</code> dataclass holding every setting the pipeline needs: the fold column and which fold to validate on, the target image size, batch size, learning rate, epoch count, a mixed-precision switch, and where to save the best model. Creating <code>cfg</code> once gives every later step a single place to read its settings from.</p>
<h3 id="heading-the-patient-grouped-split">The Patient-grouped Split</h3>
<p>The split uses two predefined columns. <code>HOP</code> (Hold-Out Partition) reserves a patient-disjoint slice as the test set, untouched until the very end. Within the remaining development set, one <code>K5P</code> fold becomes validation and the other four are training. Short assertions confirm no patient appears in more than one split.</p>
<pre><code class="language-python">dev_df   = manifest[manifest[cfg.test_column] != cfg.test_group]
test_df  = manifest[manifest[cfg.test_column] == cfg.test_group]

train_df = dev_df[dev_df[cfg.fold_column] != cfg.val_fold]
val_df   = dev_df[dev_df[cfg.fold_column] == cfg.val_fold]

# no patient may appear in more than one split
for a, b in [(train_df, val_df), (train_df, test_df), (val_df, test_df)]:
    assert not (set(a["Case"]) &amp; set(b["Case"])), "patient leakage"
</code></pre>
<p>The above code first splits off the <code>HOP</code> test set, then divides the remaining development rows into validation (the chosen <code>K5P</code> fold) and training (the rest). It then checks that every pair of splits shares no patient <code>Case</code>. If any does, the assertion fails immediately.</p>
<h3 id="heading-transforms-chosen-by-the-snapshot">Transforms, Chosen by the Snapshot</h3>
<p>MONAI's dictionary transforms operate on records keyed by name (<code>"image"</code> and <code>"label"</code>) and apply matched operations to both. Each step here answers a <strong>Part 1 data profile</strong> finding.</p>
<pre><code class="language-python">from monai.transforms import (
    Compose, LoadImaged, EnsureChannelFirstd, ScaleIntensityd,
    AsDiscreted, Resized, RandFlipd, EnsureTyped,
)
import torch

base = [
    LoadImaged(keys=["image", "label"], reader="PILReader", image_only=True),
    EnsureChannelFirstd(keys=["image", "label"]),
    ScaleIntensityd(keys="image"),                       # brightness spread
    AsDiscreted(keys="label", threshold=0.5),            # clean {0, 1} mask
    Resized(keys=["image", "label"],                     # hundreds of sizes
            spatial_size=cfg.image_size,
            mode=("bilinear", "nearest")),
]

train_transforms = Compose(base + [
    RandFlipd(keys=["image", "label"], prob=0.5, spatial_axis=1),  # horizontal
    EnsureTyped(keys=["image", "label"], dtype=torch.float32),
])
val_transforms = Compose(base + [
    EnsureTyped(keys=["image", "label"], dtype=torch.float32),
])
</code></pre>
<p>The above code builds a shared list of base steps, loads the PNG, moves the channel to the front, scales the image to [0, 1], binarizes the mask, and resizes both to 256×256. It then wraps that list in two pipelines. The training pipeline adds a random horizontal flip, and the validation pipeline does not, so evaluation always sees the image as-is.</p>
<p>Horizontal flips are a simple augmentation that preserve anatomical plausibility in this dataset. More aggressive augmentations, such as large rotations or elastic deformations, should be validated carefully because they may distort clinically meaningful structures.</p>
<p>Images use bilinear interpolation to preserve intensity gradients, while masks use nearest-neighbor interpolation so class labels remain strictly 0 or 1. Bilinear interpolation on masks would create artificial label values along object boundaries.</p>
<h3 id="heading-model-loss-and-metric">Model, Loss, and Metric</h3>
<p>The network is a MONAI <code>UNet</code> with one input channel (grayscale) and one output channel (the tumor logit). The loss is the one the class-balance finding pointed at.</p>
<p>U-Net consists of an encoder that captures context at progressively coarser resolutions and a decoder that reconstructs fine spatial detail. Skip connections transfer high-resolution features directly from encoder to decoder, making U-Net especially effective for medical segmentation where boundaries matter.</p>
<pre><code class="language-python">from monai.networks.nets import UNet
from monai.losses import DiceCELoss
from monai.metrics import DiceMetric
from monai.transforms import Activations, AsDiscrete

model = UNet(
    spatial_dims=2, in_channels=1, out_channels=1,
    channels=(16, 32, 64, 128, 256), strides=(2, 2, 2, 2),
    num_res_units=2,
).to(device)

loss_fn = DiceCELoss(sigmoid=True)       # Dice handles the imbalance; CE smooths the gradient
metric  = DiceMetric(include_background=True, reduction="mean")
post_pred = Compose([Activations(sigmoid=True), AsDiscrete(threshold=0.5)])
   
</code></pre>
<p>The above code creates the U-Net (five resolution levels, one input and one output channel) and moves it to the GPU. It then defines the three pieces that surround it: the loss, the validation metric, and a <code>post_pred</code> step that turns raw model outputs into a clean 0/1 mask by applying a sigmoid and thresholding at 0.5.</p>
<p><code>DiceCELoss</code> combines two terms. The Dice part is scale-invariant in the foreground area, so a small tumor counts as much as a large one and the model can't win by ignoring tumors. The cross-entropy part adds a smoother gradient where Dice is flat. The <code>sigmoid=True</code> flag tells the loss to apply the activation itself, so the model outputs raw logits and the <code>post_pred</code> step handles the sigmoid-and-threshold at evaluation time. This U-Net comes out to about 1.6 million parameters.</p>
<p>The training loop itself is mostly standard PyTorch. MONAI stays out of the optimization logic, the only segmentation-specific pieces are the loss, transforms, and evaluation metric.</p>
<pre><code class="language-python">for epoch in range(1, cfg.epochs + 1):
    model.train()
    for batch in train_loader:
        img, lab = batch["image"].to(device), batch["label"].to(device)
        optimizer.zero_grad(set_to_none=True)
        with torch.amp.autocast("cuda", enabled=cfg.use_amp):
            loss = loss_fn(model(img), lab)
        scaler.scale(loss).backward()
        scaler.step(optimizer); scaler.update()

    model.eval(); metric.reset()
    with torch.no_grad():
        for batch in val_loader:
            img, lab = batch["image"].to(device), batch["label"].to(device)
            pred = post_pred(model(img))
            metric(y_pred=pred, y=lab)
    val_dice = metric.aggregate().item()
    if val_dice &gt; best_dice:
        best_dice = val_dice
        torch.save(model.state_dict(), cfg.ckpt_path)
</code></pre>
<p>In the above code, each epoch runs two passes. The training pass moves every batch to the GPU, computes the loss under mixed precision, and updates the weights through the gradient scaler. The validation pass then runs with gradients turned off, converts predictions with <code>post_pred</code>, and accumulates Dice across the fold. Whenever the epoch's Dice beats the best seen so far, the model weights are saved to disk.</p>
<h2 id="heading-reading-the-results">Reading the Results</h2>
<p>Two curves summarize the run. Training loss falls steadily and flattens near 0.12. Validation Dice climbs from about 0.57 to a plateau, with a best of <strong>0.866</strong> reached at epoch 28.</p>
<img src="https://cdn.hashnode.com/uploads/covers/69fd77e89f93a850a46d376f/2a70807b-9d3d-4ff1-9610-7100aaaac984.png" alt="Training curves showing loss decreasing steadily over 30 epochs while validation Dice increases and plateaus around 0.866, indicating convergence with mild overfitting." style="display:block;margin:0 auto" width="1526" height="470" loading="lazy">

<p>A few things are worth reading off these curves:</p>
<ul>
<li><p>The loss decreasing monotonically means the model is learning. The gradient signal is real.</p>
</li>
<li><p>The loss flattening above zero rather than reaching it is expected. <code>DiceCELoss</code> has a floor, because the cross-entropy term never fully vanishes on ambiguous boundary pixels. A loss that reached zero would be a warning sign, not a triumph.</p>
</li>
<li><p>Validation Dice plateauing above ~0.85 while training loss keeps falling is the mild-overfitting signature. Extra epochs mostly lower train loss without moving val Dice. It's not severe here, so the 30-epoch budget is fine, but a patience-based early-stopping rule would be a reasonable add.</p>
</li>
</ul>
<p>A validation Dice of 0.866 sits in a reasonable range for a plain 2D U-Net on this dataset. But validation Dice measures a checkpoint chosen using that same set, so it runs a little optimistic.</p>
<p>The final, untouched check is the <code>HOP</code> test set, scored exactly once, after all training and model selection are done. It comes in at <strong>0.864</strong>, essentially matching the 0.866 validation figure. The model generalizes to patients it never saw during training or selection, and the validation number wasn't hiding leakage.</p>
<h2 id="heading-prediction-visualization"><strong>Prediction Visualization</strong></h2>
<p>Metrics summarize overall performance, but they don’t show <em>how</em> the model is segmenting individual tumors.</p>
<p>The figure below presents a representative validation example. From left to right are the input ultrasound image, the ground-truth mask, the model’s predicted mask, and the prediction overlaid on the original image.</p>
<p>The close agreement between the prediction and the ground-truth annotation illustrates how the model localizes both the position and the boundary of the lesion.</p>
<img src="https://cdn.hashnode.com/uploads/covers/69fd77e89f93a850a46d376f/ada82859-b2ba-4fd4-bc45-086177990a3f.png" alt="Four-panel visualization showing a representative segmentation result: the 