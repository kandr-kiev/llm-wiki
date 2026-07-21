---
source_url: https://www.freecodecamp.org/news/how-neural-machine-translation-works-build-your-own-translation-app-with-react-native-and-qvac/
ingested: 2026-07-18
sha256: 1da6a3372ac34ac1cb9e803b6827ef0a4028166de5ae4ce97ecbc0f47f9e8323
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How Neural Machine Translation Works: Build Your Own Translation App with React Native and QVAC</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-neural-machine-translation-works-build-your-own-translation-app-with-react-native-and-qvac/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="For the past 10 years, we&#39;ve experienced a massive improvement in translation technologies. We went from robotic-like translations to systems that not only understand the meaning of each word in a sen">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How Neural Machine Translation Works: Build Your Own Translation App with React Native and QVAC">
    
        <meta property="og:description" content="For the past 10 years, we&#39;ve experienced a massive improvement in translation technologies. We went from robotic-like translations to systems that not only understand the meaning of each word in a sen">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-neural-machine-translation-works-build-your-own-translation-app-with-react-native-and-qvac/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/89b0a610-cd98-4112-95cc-fb01597911dc.png">
    <meta property="article:published_time" content="2026-07-17T16:51:58.899Z">
    <meta property="article:modified_time" content="2026-07-17T16:51:58.899Z">
    
        <meta property="article:tag" content="AI">
    
        <meta property="article:tag" content="Machine Learning">
    
        <meta property="article:tag" content="nlp">
    
        <meta property="article:tag" content="React Native">
    
        <meta property="article:tag" content="Mobile Development">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How Neural Machine Translation Works: Build Your Own Translation App with React Native and QVAC">
    
        <meta name="twitter:description" content="For the past 10 years, we&#39;ve experienced a massive improvement in translation technologies. We went from robotic-like translations to systems that not only understand the meaning of each word in a sen">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-neural-machine-translation-works-build-your-own-translation-app-with-react-native-and-qvac/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/89b0a610-cd98-4112-95cc-fb01597911dc.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Jibril-M🍀">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="AI, Machine Learning, nlp, React Native, Mobile Development">
    <meta name="twitter:site" content="@freecodecamp">
    
        <meta name="twitter:creator" content="@djibril_mg">
    

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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/89b0a610-cd98-4112-95cc-fb01597911dc.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-neural-machine-translation-works-build-your-own-translation-app-with-react-native-and-qvac/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-17T16:51:58.899Z",
	"dateModified": "2026-07-17T16:51:58.899Z",
	"keywords": "AI, Machine Learning, nlp, React Native, Mobile Development",
	"description": "For the past 10 years, we&#x27;ve experienced a massive improvement in translation technologies. We went from robotic-like translations to systems that not only understand the meaning of each word in a sen",
	"headline": "How Neural Machine Translation Works: Build Your Own Translation App with React Native and QVAC",
	"author": {
		"@type": "Person",
		"name": "Jibril-M🍀",
		"url": "https://www.freecodecamp.org/news/author/djibrilm/",
		"sameAs": [
			"https://x.com/djibril_mg"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/uploads/avatars/68e4f3e9867c1707d1b057a9/4e66ce35-be97-4e46-a42b-e4c8435bc8e2.jpg",
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-17T16:51:58.899Z">
                            July 17, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/ai/">
                                #AI
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How Neural Machine Translation Works: Build Your Own Translation App with React Native and QVAC</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/uploads/avatars/68e4f3e9867c1707d1b057a9/4e66ce35-be97-4e46-a42b-e4c8435bc8e2.jpg 60w" sizes="60px" src="https://cdn.hashnode.com/uploads/avatars/68e4f3e9867c1707d1b057a9/4e66ce35-be97-4e46-a42b-e4c8435bc8e2.jpg" class="author-profile-image" alt="Jibril-M🍀" width="400" height="400" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/djibrilm/" data-test-label="profile-link">
                    
                        Jibril-M🍀
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/89b0a610-cd98-4112-95cc-fb01597911dc.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/89b0a610-cd98-4112-95cc-fb01597911dc.png" alt="How Neural Machine Translation Works: Build Your Own Translation App with React Native and QVAC" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>For the past 10 years, we've experienced a massive improvement in translation technologies. We went from robotic-like translations to systems that not only understand the meaning of each word in a sentence, but also how the word fits into the context of the full sentence.</p>
<p>For instance, current translation systems know how to differentiate the meaning of "bank" in a sentence like:</p>
<blockquote>
<p>"I can't make the bank deposit today," and "We shall meet near the river bank."</p>
</blockquote>
<p>Both sentences have "bank" in them, but with different meanings.</p>
<p>So how did we get here? This huge revolution started back in June of 2017 when a team of 8 Google researchers, notoriously known as the "8 Samurai," released a research paper titled <a href="https://arxiv.org/abs/1706.03762">"Attention Is All You Need"</a>. This date marked a turning point in modern AI systems and architecture.</p>
<p>For context, this framework is the bedrock of current LLMs like ChatGPT and all large language models.</p>
<p><em>The 8 Google researchers who created the Transformer architecture</em></p>
<img src="https://cdn.hashnode.com/uploads/covers/68e4f3e9867c1707d1b057a9/3826d677-eee8-41bf-ae03-9ab6e805e6f6.png" alt="The 8 Google researchers who created the Transformer architecture" style="display:block;margin:0 auto" width="1185" height="1062" loading="lazy">

<p>So, what is NMT, and how were Google engineers able to develop a framework that enables machines to understand the semantic meaning of each word in a sentence?</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-demystifying-nmt-the-brain-behind-the-screen">Demystifying NMT: The Brain Behind the Screen</a></p>
</li>
<li><p><a href="#heading-how-the-transformer-sees-the-world">How the Transformer Sees the World</a></p>
</li>
<li><p><a href="#heading-why-this-matters">Why This Matters</a></p>
</li>
<li><p><a href="#heading-the-democratization-of-ai">The Democratization of AI</a></p>
</li>
<li><p><a href="#heading-what-is-qvac">What is QVAC?</a></p>
</li>
<li><p><a href="#heading-the-architecture-supported-by-qvac">The Architecture Supported by QVAC</a></p>
</li>
<li><p><a href="#heading-the-inference-pipeline">The Inference Pipeline</a></p>
</li>
<li><p><a href="#heading-setting-up-the-project">Setting Up the Project</a></p>
</li>
<li><p><a href="#heading-complete-implementation">Complete Implementation</a></p>
</li>
<li><p><a href="#heading-conclusion">Conclusion</a></p>
</li>
<li><p><a href="#heading-resources-and-further-reading">Resources and Further Reading</a></p>
</li>
</ul>
<h2 id="heading-demystifying-nmt-the-brain-behind-the-screen">Demystifying NMT: The Brain Behind the Screen</h2>
<p>To understand this breakthrough, we first have to pull back the curtain on what <strong>NMT</strong> (Neural Machine Translation) actually means.</p>
<p>For decades, computer translation was "rule-based." The computer was essentially given a massive bilingual dictionary and a set of grammar rules. It would translate a sentence word-by-word, swap a few positions around, and hope for the best.</p>
<p>This is why early translations felt so incredibly stiff and robotic: the computer was trying to solve language like a math problem.</p>
<p>NMT changed the game by introducing <strong>Neural Networks</strong>, computer systems inspired by the human brain. Instead of memorizing strict rules, an NMT system learns by looking at millions of existing human translations. It looks at how humans translate phrases, captures patterns, and learns how words actually interact in the real world.</p>
<p>But even early NMT systems had a massive flaw: they read sentences sequentially, from left to right. If a sentence was too long, the system would "forget" how it started by the time it reached the end.</p>
<p>This is where the Google researchers made their historic leap.</p>
<h2 id="heading-how-the-transformer-sees-the-world">How the Transformer Sees the World</h2>
<p>The "Attention Is All You Need" paper solved the memory problem by introducing a brand-new architecture called the <strong>Transformer</strong>. Instead of reading a sentence word-by-word, the Transformer reads the entire sentence all at once.</p>
<p>To do this, it splits the job into two main parts: the Encoder and the Decoder.</p>
<h3 id="heading-the-encoder-the-reader">The Encoder (The Reader)</h3>
<p>Think of the Encoder as a highly analytical reader. When you feed a sentence into the system, the Encoder’s job is to read it and build a "mental map" of what the sentence actually means.</p>
<p>It does this using a mechanism called <strong>Self-Attention</strong>. You can think of Self-Attention as a series of spotlights. When the computer looks at a specific word, it shines spotlights on all the other words in the sentence to see how they relate.</p>
<p>Going back to our earlier example:</p>
<blockquote>
<p>"We shall meet near the river bank."</p>
</blockquote>
<p>When the Encoder processes the word <strong>"bank,"</strong> its Self-Attention spotlight instantly flags the word <strong>"river."</strong> Because those two words are highly connected on the AI's mental map, the system immediately knows we're talking about land next to water, not a financial institution. It locks in this "semantic meaning" before moving to the next step.</p>
<h3 id="heading-the-decoder-the-writer">The Decoder (The Writer)</h3>
<p>Once the Encoder has mapped out the true meaning of the sentence, it hands this blueprint over to the <strong>Decoder</strong>.</p>
<p>The Decoder is the writer. Its only job is to translate that blueprint into the target language. But it doesn't just output a pre-written template. It builds the new sentence word-by-word, constantly looking back at the Encoder's blueprint (using a trick called <strong>Cross-Attention</strong>) to make sure it maintains the correct context, tone, and grammar.</p>
<p>If it's translating our river bank sentence into French, it knows to write <em>"la rive"</em> (the bank of the river) instead of <em>"la banque"</em> (the financial bank), because the Encoder's blueprint warned it ahead of time.</p>
<h2 id="heading-why-this-matters">Why This Matters</h2>
<p>By teaching machines to look at the whole picture rather than individual words, Google’s engineers didn't just build a better translator. They built a system that finally understands the nuances, idioms, and context of human language.</p>
<p>And as it turns out, if an AI can understand the context of a sentence well enough to translate it, it can also use that same context to write essays, answer complex questions, and code. The 2017 translation engine accidentally became the foundation of the entire AI era.</p>
<h2 id="heading-the-democratization-of-ai">The Democratization of AI</h2>
<p>A few years after the Transformer's invention, building with it was strictly a toy for the rich. If you wanted to implement even a simple translation feature, you had to pay Big Tech giants like Google a fortune once you went beyond their tiny free tier.</p>
<p>Trying to bypass their dominance was almost impossible because there were practically no resources for independent developers. Back then, just understanding the basic math of a Transformer required an academic PhD. Without a massive research department at your back, trying to build your own solution from scratch was an incredibly expensive nightmare.</p>
<p>Thankfully, the open-source developer community has worked tirelessly to democratize access to AI. Today, we have incredibly powerful models that anyone can download and use freely.</p>
<p>On top of that, the processors in our personal devices have become exceptionally capable. This hardware evolution means that sophisticated AI models can now run locally directly on your smartphone, ensuring maximum data privacy and removing the dependency on external servers.</p>
<p>As the saying goes, <em>"Today it needs a full building to function, tomorrow it will fit in your pocket."</em> Of course, I totally made that quote up 😅, but you get my point!</p>
<p>To put this in action, we'll build a mobile application with Expo and QVAC that translates English to French.</p>
<h2 id="heading-what-is-qvac">What is QVAC?</h2>
<p>QVAC (QuantumVerse Automatic Computer) is a decentralized, local-first AI development platform and SDK created by Tether.</p>
<p>Unlike traditional AI tools that require cloud connectivity, QVAC allows users to run AI models entirely on their own devices. By keeping the computation local and offline, it ensures your data remains private, secure, and entirely under your control.</p>
<h3 id="heading-key-concepts-for-on-device-translation">Key Concepts for On-Device Translation</h3>
<p>To understand how QVAC runs on a mobile device, we must keep a few key concepts in mind:</p>
<h4 id="heading-1-on-device-inference">1. On-Device Inference:</h4>
<p>Running model calculations locally. Rather than relying on a single engine or cloud API, QVAC supports specialized local inference backends depending on the task.</p>
<p>For translation, it uses the Bergamot engine under the hood. These engines memory-map quantized model weights directly into the device's RAM and run calculations using native hardware acceleration.</p>
<h4 id="heading-2-quantization">2. Quantization</h4>
<p>A mathematical optimization technique that compresses the model's weights. This makes it possible for models to fit into the memory constraints of consumer mobile hardware while keeping output quality high.</p>
<h2 id="heading-the-architecture-supported-by-qvac">The Architecture Supported by QVAC</h2>
<p>Before writing code, it's crucial to understand what's actually happening under the hood. To handle local execution without melting your device, the QVAC SDK manages the hardware binding and model lifecycle while hooking into optimized inference backends.</p>
<p>For translation, QVAC utilizes the Bergamot engine. Originally developed as part of the Bergamot project (which powers Firefox's offline translation), this engine is highly optimized for fast, accurate Neural Machine Translation (NMT) on consumer hardware.</p>
<p>At its core, the Bergamot engine takes a source sentence, processes it through its Encoder-Decoder transformer architecture, and predicts the target language tokens in a highly efficient manner.</p>
<h3 id="heading-understanding-language-pairs">Understanding Language Pairs</h3>
<p>It's important to understand the mechanics of how these models are trained. Translation models like the ones used by Bergamot are strictly unidirectional language pairs. This means the <code>BERGAMOT_EN_FR</code> model is designed exclusively to translate from English to French. It can't reverse the process.</p>
<p>If you want to translate French back to English, you would need to download and load a completely separate model trained specifically for that direction.</p>
<p>If a model is trained to be bidirectional (English ↔ French) or multilingual (translating dozens of languages like large language models do), it has to store mathematical representations, vocabulary, and grammar rules for multiple linguistic directions inside a single neural network. This balloons the parameter count, making the file size massive and requiring heavy RAM and compute power to process.</p>
<p>By isolating the task to a single direction (for example <code>BERGAMOT_EN_FR</code>), the model only needs the neural network to "understand" English inputs and "generate" French outputs. It doesn't need the capacity to generate English text.</p>
<p>This extreme specialization is exactly how Bergamot shrinks the model weights down to those incredibly tiny 15–35MB files that can run instantly on a local CPU without freezing your browser.</p>
<h2 id="heading-the-inference-pipeline">The Inference Pipeline</h2>
<p>To visualize how we interact with the translation engine in our codebase, think of local translation as running a dedicated interpreter right in your phone's memory:</p>
<ol>
<li><p><strong>Hiring the interpreter (loading the model):</strong> We map the compressed model file (in this case, the <code>BERGAMOT_EN_FR</code> English-to-French model) directly into the device's RAM.</p>
</li>
<li><p><strong>Handing over the script (text input):</strong> We pass the source text to the loaded engine.</p>
</li>
<li><p><strong>The performance (inference):</strong> The engine reads the text and mathematically predicts the translated tokens, providing the translated result once the process is complete.</p>
</li>
<li><p><strong>Closing the show (unloading):</strong> Because neural network models are memory-intensive, the model can be cleared from RAM to free up resources once the translation is complete or when the user leaves the screen.</p>
</li>
</ol>
<h2 id="heading-setting-up-the-project">Setting Up the Project</h2>
<p>To ensure this guide is completely self-contained, let's start by quickly generating our new Expo application and installing the QVAC SDK. Open your terminal and run the following commands:</p>
<pre><code class="language-bash">npx create-expo-app translator-app --template blank-typescript
cd translator-app
npm install @qvac/sdk jiti
</code></pre>
<p>Next, you need to add the following peer dependencies to your <code>package.json</code> for QVAC to work correctly. Add these lines to their respective sections:</p>
<pre><code class="language-json">  "dependencies": {
    "bare-rpc": "^1.0.0",
    "react-native-bare-kit": "^0.11.5"
  },
  "devDependencies": {
    "bare-pack": "^1.5.1"
  }
</code></pre>
<p>Once added, install the dependencies by running:</p>
<pre><code class="language-bash">npm install
npx expo install expo-file-system expo-build-properties expo-device
</code></pre>
<h3 id="heading-configuring-the-expo-plugin-with-jiti">Configuring the Expo Plugin with JITI</h3>
<p>Next, we need to add the QVAC SDK plugin to our Expo project. Because the QVAC SDK's Expo plugin is distributed as a modern ECMAScript Module (ESM), but Expo's configuration file (<code>app.config.js</code>) runs in a standard Node.js CommonJS environment, we can't use a standard <code>require()</code>.</p>
<p>This is why we installed <code>jiti</code>. It acts as a bridge, allowing us to synchronously load ESM modules inside CommonJS files without breaking the build process.</p>
<p>Create or update your <code>app.config.js</code> file at the root of your project and configure it like this:</p>
<pre><code class="language-javascript">const createJiti = require("jiti");
const jiti = createJiti(__filename);

// Synchronously require the ESM module using jiti
const qvacModule = jiti("@qvac/sdk/expo-plugin");
const withQvacSDK = qvacModule.withQvacSDK || qvacModule.default;

// (Include your withEscapeBundleShellScript helper if needed)

module.exports = ({ config }) =&gt; {
  config.plugins = [
    [
      "expo-build-properties",
      {
        android: { minSdkVersion: 29 },
      },
    ],
    withQvacSDK,
    "expo-router",
    [
      "expo-splash-screen",
      {
        backgroundColor: "#208AEF",
      },
    ],
    withEscapeBundleShellScript, // Custom helper if applicable
  ];

  return config;
};
</code></pre>
<p>This configuration applies the QVAC native setup scripts and ensures Android requires at least SDK version 29 (which is necessary for the native libraries).</p>
<p>With our base configuration ready to go, let's jump straight into the translation code.</p>
<h2 id="heading-complete-implementation">Complete Implementation</h2>
<p>Let's bring it all together. We'll implement an interface that takes English text, manages the downloading and loading states for the Bergamot engine, translates the text to French, and renders the output to the screen.</p>
<p>Replace your entry app file <code>src/app/index.tsx</code> with the following implementation:</p>
<pre><code class="language-tsx">import { View, ScrollView, TextInput, Text, TouchableOpacity, StyleSheet } from "react-native";
import { useState, useEffect } from "react";
import {
  loadModel,
  translate,
  unloadModel,
  BERGAMOT_EN_FR,
  getModelInfo,
} from "@qvac/sdk";
import { Stack } from "expo-router";

type TranslationStatus =
  | "Idle"
  | "Checking model..."
  | "Downloading model..."
  | "Model downloaded successfully."
  | "Loading model..."
  | "Translating..."
  | "Streaming translation..."
  | "Translation finished."
  | `Error: ${string}`;

export default function HomeScreen() {
  const [status, setStatus] = useState&lt;TranslationStatus&gt;("Checking model...");
  const [translatedText, setTranslatedText] = useState&lt;string&gt;("");
  const [inputText, setInputText] = useState&lt;string&gt;("");
  const [isTranslating, setIsTranslating] = useState&lt;boolean&gt;(false);
  const [isDownloaded, setIsDownloaded] = useState&lt;boolean | null&gt;(null);
  const [downloadProgressStr, setDownloadProgressStr] = useState&lt;string&gt;("");

  useEffect(() =&gt; {
    const checkModelStatus = async () =&gt; {
      try {
        const model = await getModelInfo({ name: BERGAMOT_EN_FR.name });
        setIsDownloaded(model.isCached);
        console.log("Model", model);
        setStatus("Idle");
      } catch (error) {
        console.error("Error checking model:", error);
        setStatus("Error: Failed to check model status");
      }
    };
    checkModelStatus();
  }, []);

  const handleDownload = async () =&gt; {
    try {
      setIsTranslating(true);
      setStatus("Downloading model...");
      setDownloadProgressStr("");

      const modelId = await loadModel({
        modelSrc: BERGAMOT_EN_FR,
        modelType: "nmt",
        onProgress: (progress: any) =&gt; {
          let pct = progress.percentage;
          let dl = progress.downloaded;
          let tot = progress.total;
          if (progress.shardInfo) {
            pct = progress.shardInfo.overallPercentage;
            dl = progress.shardInfo.overallDownloaded;
            tot = progress.shardInfo.overallTotal;
          }
          const formatBytes = (bytes: number) =&gt; {
            if (bytes === 0) return "0 B";
            const k = 1024;
            const sizes = ["B", "KB", "MB", "GB"];
            const i = Math.floor(Math.log(bytes) / Math.log(k));
            return (
              parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + " " + sizes[i]
            );
          };
          setDownloadProgressStr(
            `${pct.toFixed(2)}% (${formatBytes(dl)} / ${formatBytes(tot)})`,
          );
        },
        modelConfig: {
          engine: "Bergamot",
          from: "en",
          to: "fr",
          beamsize: 1,
          normalize: 1,
          temperature: 0.2,
          norepeatngramsize: 3,
          lengthpenalty: 1.2,
        },
      });

      await unloadModel({ modelId, clearStorage: false });

      setIsDownloaded(true);
      setStatus("Model downloaded successfully.");
    } catch (error: any) {
      console.error(error);
      setStatus(`Error: ${error.message}`);
    } finally {
      setIsTranslating(false);
      setDownloadProgressStr("");
    }
  };

  const handleTranslate = async () =&gt; {
    if (!inputText.trim()) {
      setStatus("Error: Please enter text to translate");
      return;
    }

    try {
      setIsTranslating(true);
      setTranslatedText("");
      setStatus("Loading model...");

      const modelId = await loadModel({
        modelSrc: BERGAMOT_EN_FR,
        modelType: "nmt",

        modelConfig: {
          engine: "Bergamot",
          from: "en",
          to: "fr",
          beamsize: 1,
          normalize: 1,
          temperature: 0.2,
          norepeatngramsize: 3,
          lengthpenalty: 1.2,
        },
      });

      setStatus(`Translating...`);

      const result = translate({
        modelId,
        text: inputText,
        modelType: "nmt",
        stream: false,
      });

      const text = await result.text;
      setTranslatedText(text);

      const stats = await result.stats;
      if (stats) {
        console.log(`▸ Processing stats:`, stats);
      }

      setStatus("Translation finished.");

      await unloadModel({ modelId, clearStorage: false });
    } catch (error: any) {
      