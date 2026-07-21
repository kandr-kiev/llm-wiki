---
source_url: https://www.freecodecamp.org/news/how-to-fix-common-web-application-security-vulnerabilities-in-node-js/
ingested: 2026-07-17
sha256: ad39c8908a7e37705cc75aa9619d643f1375deff0862324ef9cb4c258ae919f6
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Fix Common Web Application Security Vulnerabilities in Node.js</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-to-fix-common-web-application-security-vulnerabilities-in-node-js/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="Here&#39;s something that tends to surprise developers who are new to security: most web vulnerabilities aren&#39;t the result of sophisticated attacks. They come from code patterns that look completely reaso">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Fix Common Web Application Security Vulnerabilities in Node.js">
    
        <meta property="og:description" content="Here&#39;s something that tends to surprise developers who are new to security: most web vulnerabilities aren&#39;t the result of sophisticated attacks. They come from code patterns that look completely reaso">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-to-fix-common-web-application-security-vulnerabilities-in-node-js/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/b2ec81b6-d6eb-41f0-9fa5-7570914ef97d.png">
    <meta property="article:published_time" content="2026-07-15T23:48:53.155Z">
    <meta property="article:modified_time" content="2026-07-15T23:48:53.155Z">
    
        <meta property="article:tag" content="Node.js">
    
        <meta property="article:tag" content="Security">
    
        <meta property="article:tag" content="owasp">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Fix Common Web Application Security Vulnerabilities in Node.js">
    
        <meta name="twitter:description" content="Here&#39;s something that tends to surprise developers who are new to security: most web vulnerabilities aren&#39;t the result of sophisticated attacks. They come from code patterns that look completely reaso">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-to-fix-common-web-application-security-vulnerabilities-in-node-js/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/b2ec81b6-d6eb-41f0-9fa5-7570914ef97d.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Hackita">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="Node.js, Security, owasp">
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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/b2ec81b6-d6eb-41f0-9fa5-7570914ef97d.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-to-fix-common-web-application-security-vulnerabilities-in-node-js/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-15T23:48:53.155Z",
	"dateModified": "2026-07-15T23:48:53.155Z",
	"keywords": "Node.js, Security, owasp",
	"description": "Here&#x27;s something that tends to surprise developers who are new to security: most web vulnerabilities aren&#x27;t the result of sophisticated attacks. They come from code patterns that look completely reaso",
	"headline": "How to Fix Common Web Application Security Vulnerabilities in Node.js",
	"author": {
		"@type": "Person",
		"name": "Hackita",
		"url": "https://www.freecodecamp.org/news/author/hackita-/",
		"sameAs": [
			"https://hackita.it"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://lh3.googleusercontent.com/a/ACg8ocJvQ0RSUcdrQNtIG_b1jubi40RPgN9-w_vEL-Fz4qXjCqWw3A=s96-c",
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-15T23:48:53.155Z">
                            July 15, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/nodejs/">
                                #Node.js
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Fix Common Web Application Security Vulnerabilities in Node.js</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://lh3.googleusercontent.com/a/ACg8ocJvQ0RSUcdrQNtIG_b1jubi40RPgN9-w_vEL-Fz4qXjCqWw3A=s96-c 60w" sizes="60px" src="https://lh3.googleusercontent.com/a/ACg8ocJvQ0RSUcdrQNtIG_b1jubi40RPgN9-w_vEL-Fz4qXjCqWw3A=s96-c" class="author-profile-image" alt="Hackita" width="96" height="96" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/hackita-/" data-test-label="profile-link">
                    
                        Hackita
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/b2ec81b6-d6eb-41f0-9fa5-7570914ef97d.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/b2ec81b6-d6eb-41f0-9fa5-7570914ef97d.png" alt="How to Fix Common Web Application Security Vulnerabilities in Node.js" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>Here's something that tends to surprise developers who are new to security: most web vulnerabilities aren't the result of sophisticated attacks. They come from code patterns that look completely reasonable: trusting a value from the URL, applying a request body to a database update, or running two queries where one should've been enough.</p>
<p>This guide covers six of those patterns. For each one, you'll see a real code example that creates the vulnerability, an explanation of what makes it dangerous, and a corrected version with notes on exactly what changed and why.</p>
<p>No security background is required to follow along here. It'll just help to have some familiarity with Node.js and SQL.</p>
<h2 id="heading-prerequisites">Prerequisites</h2>
<p>The examples assume you're comfortable with:</p>
<ul>
<li><p>Node.js and Express.js basics</p>
</li>
<li><p>SQL queries</p>
</li>
<li><p>How HTTP requests and responses work</p>
</li>
<li><p>Basic authentication concepts (sessions, tokens)</p>
</li>
</ul>
<p><strong>Note on code examples</strong>: Throughout this tutorial, <code>db.query()</code> is a fictional database helper that returns a single row object for <code>SELECT</code> queries (or <code>null</code> if not found), and a result object for <code>INSERT</code>/<code>UPDATE</code> queries. The <code>connection.query()</code> in the race conditions section uses the <a href="https://github.com/sidorares/node-mysql2">mysql2</a> promise API directly, where <code>query()</code> returns <code>[rows, fields]</code>. Adapt the syntax to the database driver you use.</p>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ul>
<li><p><a href="#heading-1-broken-access-control-and-idor">1. Broken Access Control and IDOR</a></p>
</li>
<li><p><a href="#heading-2-mass-assignment">2. Mass Assignment</a></p>
</li>
<li><p><a href="#heading-3-prototype-pollution">3. Prototype Pollution</a></p>
</li>
<li><p><a href="#heading-4-race-conditions">4. Race Conditions</a></p>
</li>
<li><p><a href="#heading-5-business-logic-flaws">5. Business Logic Flaws</a></p>
</li>
<li><p><a href="#heading-6-jwt-misconfiguration">6. JWT Misconfiguration</a></p>
</li>
<li><p><a href="#heading-summary">Summary</a></p>
</li>
</ul>
<h2 id="heading-1-broken-access-control-and-idor">1. Broken Access Control and IDOR</h2>
<p><a href="https://owasp.org/Top10/A01_2021-Broken_Access_Control/">Broken Access Control</a> has topped the OWASP Top 10 since 2021, and it's not hard to see why. The most common form is <strong>Insecure Direct Object Reference (IDOR)</strong>: the application exposes a database ID in a URL, a user changes the number, and suddenly they're looking at someone else's data.</p>
<p>The fix seems obvious in hindsight. But it keeps appearing in production code because authentication and authorization get conflated. Confirming that a user is logged in is not the same as confirming they're allowed to access a specific resource.</p>
<h3 id="heading-how-to-identify-this-vulnerability-in-your-code">How to Identify This Vulnerability in Your Code</h3>
<p>Here's a typical user profile endpoint:</p>
<pre><code class="language-javascript">// Express.js - Vulnerable
app.get('/api/users/:id/profile', authenticate, async (req, res) =&gt; {
  const userId = req.params.id;

  const user = await db.query(
    'SELECT id, name, email, address FROM users WHERE id = ?',
    [userId]
  );

  if (!user) {
    return res.status(404).json({ error: 'User not found' });
  }

  res.json(user);
});
</code></pre>
<p>The <code>authenticate</code> middleware confirms that the request includes a valid token. But it doesn't confirm whether the authenticated user is allowed to access the requested resource.</p>
<p>Any authenticated user can request <code>/api/users/1/profile</code>, <code>/api/users/2/profile</code>, and so on and retrieve other users' data.</p>
<h3 id="heading-why-this-matters">Why This Matters</h3>
<p>Authentication confirms <em>who</em> you are. Authorization confirms <em>what you're allowed to do</em>. The code above does the first and skips the second entirely.</p>
<p>With a sequential numeric ID, a curious user doesn't need any special tools. They can just change <code>1</code> to <code>2</code> in the URL. But the same problem exists with UUIDs or slugs if the ownership check is missing.</p>
<h3 id="heading-how-to-fix-this-vulnerability">How to Fix This Vulnerability</h3>
<p>Verify server-side that the authenticated user owns — or is explicitly authorized to access — the requested resource:</p>
<pre><code class="language-javascript">// Express.js - Secure
app.get('/api/users/:id/profile', authenticate, async (req, res) =&gt; {
  // Reject anything that isn't a string of digits — parseInt("12abc") would return 12
  if (!/^\d+$/.test(req.params.id)) {
    return res.status(400).json({ error: 'Invalid user ID' });
  }

  const requestedId = Number(req.params.id);

  if (requestedId &lt; 1) {
    return res.status(400).json({ error: 'Invalid user ID' });
  }

  // The authenticated user's ID is set by the authenticate middleware
  const authenticatedId = req.user.id;

  // Enforce ownership: users can only access their own profile
  if (requestedId !== authenticatedId) {
    return res.status(403).json({ error: 'Forbidden' });
  }

  const user = await db.query(
    'SELECT id, name, email, address FROM users WHERE id = ?',
    [requestedId]
  );

  if (!user) {
    return res.status(404).json({ error: 'User not found' });
  }

  res.json(user);
});
</code></pre>
<p>For admin endpoints that legitimately need to access any user, enforce role-based authorization explicitly:</p>
<pre><code class="language-javascript">// Admin endpoint with explicit role check
app.get('/api/admin/users/:id', authenticate, requireRole('admin'), async (req, res) =&gt; {
  if (!/^\d+$/.test(req.params.id)) {
    return res.status(400).json({ error: 'Invalid user ID' });
  }

  const userId = Number(req.params.id);

  const user = await db.query(
    'SELECT id, name, email, role FROM users WHERE id = ?',
    [userId]
  );

  if (!user) {
    return res.status(404).json({ error: 'User not found' });
  }

  res.json(user);
});
</code></pre>
<p>Here's what changed and why:</p>
<ul>
<li><p><code>/^\d+$/.test(req.params.id)</code> rejects anything that isn't a pure string of digits. <code>parseInt("12abc", 10)</code> would silently return <code>12</code> and pass further checks. The regex prevents this.</p>
</li>
<li><p><code>Number(req.params.id)</code> converts the already-validated string to a number safely.</p>
</li>
<li><p>The comparison <code>requestedId !== authenticatedId</code> enforces ownership.</p>
</li>
<li><p>Admin functionality is a separate endpoint with its own authorization check.</p>
</li>
</ul>
<p><strong>Never infer authorization from a URL parameter. Derive it from the authenticated session.</strong></p>
<h2 id="heading-2-mass-assignment">2. Mass Assignment</h2>
<p>Mass assignment is one of those vulnerabilities that's almost invisible when you write it. You're just being efficient, right? Why iterate over fields manually when you can pass the whole object?</p>
<p>The problem is that your database table knows about fields your users were never supposed to touch.</p>
<h3 id="heading-how-to-identify-this-vulnerability-in-your-code">How to Identify This Vulnerability in Your Code</h3>
<p>Here's a user profile update endpoint:</p>
<pre><code class="language-javascript">// Express.js - Vulnerable
app.put('/api/users/me', authenticate, async (req, res) =&gt; {
  const userId = req.user.id;

  // req.body contains everything the client sends
  const updates = req.body;

  await db.query(
    'UPDATE users SET ? WHERE id = ?',
    [updates, userId]
  );

  res.json({ success: true });
});
</code></pre>
<p>The <code>users</code> table has these columns:</p>
<pre><code class="language-sql">CREATE TABLE users (
  id           INT PRIMARY KEY,
  name         VARCHAR(100),
  email        VARCHAR(100),
  bio          TEXT,
  role         ENUM('user', 'moderator', 'admin') DEFAULT 'user',
  credits      INT DEFAULT 0,
  is_banned    BOOLEAN DEFAULT false
);
</code></pre>
<p>The developer intended users to update <code>name</code>, <code>email</code>, and <code>bio</code>. But <code>role</code>, <code>credits</code>, and <code>is_banned</code> are also in the table — and the query updates whatever fields the client sends.</p>
<h3 id="heading-why-this-matters">Why This Matters</h3>
<p>That request body goes straight into the SQL query. The <code>users</code> table also has <code>role</code>, <code>credits</code>, and <code>is_banned</code> — and the query doesn't know or care which fields the developer "intended" to expose.</p>
<p>A user who sends this:</p>
<pre><code class="language-json">{
  "name": "Alice",
  "role": "admin",
  "credits": 100000,
  "is_banned": false
}
</code></pre>
<p>Has just promoted themselves to admin, cleared their ban, and given themselves a hundred thousand credits.</p>
<h3 id="heading-how-to-fix-this-vulnerability">How to Fix This Vulnerability</h3>
<p>Build the update object yourself, field by field, using an explicit allowlist:</p>
<pre><code class="language-javascript">// Express.js - Secure
app.put('/api/users/me', authenticate, async (req, res) =&gt; {
  const userId = req.user.id;

  // Only these fields may be updated by the user
  const ALLOWED_FIELDS = ['name', 'email', 'bio'];
  const updates = {};

  for (const field of ALLOWED_FIELDS) {
    if (req.body[field] !== undefined) {
      updates[field] = req.body[field];
    }
  }

  if (Object.keys(updates).length === 0) {
    return res.status(400).json({ error: 'No valid fields provided' });
  }

  // Validate individual fields
  // isValidEmail is a simple helper: /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
  if (updates.email &amp;&amp; !isValidEmail(updates.email)) {
    return res.status(400).json({ error: 'Invalid email format' });
  }

  if (updates.name &amp;&amp; (typeof updates.name !== 'string' || updates.name.length &gt; 100)) {
    return res.status(400).json({ error: 'Name must be a string of 100 characters or fewer' });
  }

  await db.query(
    'UPDATE users SET ? WHERE id = ?',
    [updates, userId]
  );

  res.json({ success: true });
});
</code></pre>
<p>For admin operations that legitimately update sensitive fields, use a separate endpoint with its own authorization:</p>
<pre><code class="language-javascript">// Admin-only endpoint for changing user roles
app.put('/api/admin/users/:id/role', authenticate, requireRole('admin'), async (req, res) =&gt; {
  if (!/^\d+$/.test(req.params.id)) {
    return res.status(400).json({ error: 'Invalid user ID' });
  }

  const userId = Number(req.params.id);
  const { role } = req.body;

  const VALID_ROLES = ['user', 'moderator', 'admin'];

  if (!VALID_ROLES.includes(role)) {
    return res.status(400).json({ error: 'Invalid role' });
  }

  await db.query(
    'UPDATE users SET role = ? WHERE id = ?',
    [role, userId]
  );

  res.json({ success: true });
});
</code></pre>
<p><strong>Don't spread</strong> <code>req.body</code> <strong>into a database query. Build the update object field by field.</strong></p>
<h2 id="heading-3-prototype-pollution">3. Prototype Pollution</h2>
<p>Prototype pollution occurs when untrusted data is merged into an object recursively, allowing an attacker to inject properties into <code>Object.prototype</code> (the base object that every plain JavaScript object inherits from).</p>
<p>The OWASP Top 10 covers this under <a href="https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/">Software and Data Integrity Failures (A08:2021)</a>.</p>
<h3 id="heading-how-to-identify-this-vulnerability-in-your-code">How to Identify This Vulnerability in Your Code</h3>
<p>A configuration merge utility that processes user-supplied settings:</p>
<pre><code class="language-javascript">// Vulnerable recursive merge function
function mergeConfig(target, source) {
  for (const key of Object.keys(source)) {
    if (typeof source[key] === 'object' &amp;&amp; source[key] !== null) {
      if (!target[key]) target[key] = {};
      mergeConfig(target[key], source[key]); // recursive call
    } else {
      target[key] = source[key]; // triggers __proto__ setter via bracket notation
    }
  }
}

app.post('/api/settings', authenticate, (req, res) =&gt; {
  const userSettings = {};
  mergeConfig(userSettings, req.body); // merge untrusted input
  applySettings(userSettings);
  res.json({ success: true });
});
</code></pre>
<h3 id="heading-why-this-matters">Why This Matters</h3>
<p>An attacker sends this request body:</p>
<pre><code class="language-json">{
  "__proto__": {
    "isAdmin": true
  }
}
</code></pre>
<p>The recursive <code>mergeConfig</code> function reaches the <code>__proto__</code> key and executes <code>target['__proto__']['isAdmin'] = true</code>. Because <code>__proto__</code> is JavaScript's prototype accessor, this writes directly to <code>Object.prototype</code>. After the merge:</p>
<pre><code class="language-javascript">const anyObject = {};
console.log(anyObject.isAdmin); // true — inherited from Object.prototype
</code></pre>
<p>Every plain object in the running application now inherits <code>isAdmin: true</code>. If any authorization check looks like this:</p>
<pre><code class="language-javascript">if (user.isAdmin) { /* grant admin access */ }
</code></pre>
<p>That check now passes for every user, regardless of their actual role.</p>
<h3 id="heading-how-to-fix-this-vulnerability">How to Fix This Vulnerability</h3>
<p>Store user state server-side and validate each field individually. Never recursively merge untrusted input:</p>
<pre><code class="language-javascript">// Express.js - Secure
app.post('/api/settings', authenticate, async (req, res) =&gt; {
  // Load current settings from the database — never from the client
  const current = await db.query(
    'SELECT theme, language, notifications FROM user_settings WHERE user_id = ?',
    [req.user.id]
  );

  // Validate each field against an explicit allowlist
  const safeSettings = {
    theme: validateEnum(req.body.theme, ['light', 'dark'], current.theme),
    language: validateEnum(req.body.language, ['en', 'es', 'fr', 'de'], current.language),
    notifications: typeof req.body.notifications === 'boolean'
      ? req.body.notifications
      : current.notifications
  };

  await db.query(
    'UPDATE user_settings SET ? WHERE user_id = ?',
    [safeSettings, req.user.id]
  );

  res.json({ success: true });
});

function validateEnum(value, allowed, defaultValue) {
  return allowed.includes(value) ? value : defaultValue;
}
</code></pre>
<p>If you need a merge utility, use <code>Object.create(null)</code> as the base — it has no prototype, so <code>__proto__</code> can't be polluted — and allowlist keys explicitly:</p>
<pre><code class="language-javascript">// Safe merge: base object with no prototype
function safeMerge(allowedKeys, source) {
  const result = Object.create(null); // no prototype = no pollution possible

  for (const key of allowedKeys) {
    if (key in source &amp;&amp; typeof source[key] !== 'object') {
      result[key] = source[key];
    }
  }

  return result;
}
</code></pre>
<p><strong>Rules</strong>:</p>
<ul>
<li><p>Never recursively merge untrusted input into a plain object.</p>
</li>
<li><p>Store application state server-side. Don't trust clients to carry it.</p>
</li>
<li><p>Use <code>Object.create(null)</code> for data containers that will hold untrusted keys.</p>
</li>
<li><p>Validate each field by type and allowed values before using it.</p>
</li>
</ul>
<h2 id="heading-4-race-conditions">4. Race Conditions</h2>
<p>Race conditions are tricky because the code is perfectly correct. It's the timing that breaks it. Two requests arrive at almost the same moment, both check the same condition, both see a valid result, and both proceed. The result is something that should only happen once, happening twice.</p>
<p>This is called a <strong>Time-of-Check to Time-of-Use (TOCTOU)</strong> problem: the state you checked is no longer the state you're acting on.</p>
<h3 id="heading-how-to-identify-this-pattern-in-your-code">How to Identify This Pattern in Your Code</h3>
<p>A single-use coupon redemption endpoint:</p>
<pre><code class="language-javascript">// Express.js - Vulnerable
app.post('/api/redeem-coupon', authenticate, async (req, res) =&gt; {
  const { couponCode } = req.body;
  const userId = req.user.id;

  // Step 1: Check if the coupon is still valid
  const coupon = await db.query(
    'SELECT id, discount_amount, used FROM coupons WHERE code = ? AND used = false',
    [couponCode]
  );

  if (!coupon) {
    return res.status(400).json({ error: 'Invalid or already used coupon' });
  }

  // Time gap: another request can pass Step 1 here before Step 3 runs

  // Step 2: Apply the discount
  await applyDiscountToOrder(userId, coupon.discount_amount);

  // Step 3: Mark coupon as used
  await db.query(
    'UPDATE coupons SET used = true, used_by = ? WHERE code = ?',
    [userId, couponCode]
  );

  res.json({ success: true });
});
</code></pre>
<h3 id="heading-why-this-matters">Why This Matters</h3>
<p>Two requests arrive with the same coupon code at nearly the same time. Both hit Step 1 before either reaches Step 3. Both read <code>used = false</code>. Both apply the discount. One coupon, used twice.</p>
<p>The same window exists anywhere you read-then-write: balance checks before deductions, inventory checks before reservations, vote checks before incrementing. Any of them can be exploited the same way.</p>
<h3 id="heading-how-to-fix-this-vulnerability">How to Fix This Vulnerability</h3>
<p>Replace the check-then-act pattern with an atomic operation. An atomic database update guarantees that the condition check and the write happen as a single indivisible unit:</p>
<pre><code class="language-javascript">// Express.js - Secure
app.post('/api/redeem-coupon', authenticate, async (req, res) =&gt; {
  const { couponCode } = req.body;
  const userId = req.user.id;

  const connection = await db.getConnection();

  try {
    await connection.beginTransaction();

    // Atomic: only one request can update a row where used = false.
    // The database row lock ensures only one request succeeds.
    const [result] = await connection.query(
      `UPDATE coupons
       SET used = true, used_by = ?, used_at = NOW()
       WHERE code = ? AND used = false`,
      [userId, couponCode]
    );

    if (result.affectedRows === 0) {
      await connection.rollback();
      return res.status(400).json({ error: 'Invalid or already used coupon' });
    }

    const [couponRows] = await connection.query(
      'SELECT discount_amount FROM coupons WHERE code = ?',
      [couponCode]
    );
    const coupon = couponRows[0];

    await applyDiscountToOrder(userId, coupon.discount_amount, connection);

    await connection.commit();

    res.json({ success: true, discount: coupon.discount_amount });

  } catch (error) {
    await connection.rollback();
    console.error('Coupon redemption failed:', error);
    res.status(500).json({ error: 'Could not process the coupon' });
  } finally {
    connection.release();
  }
});
</code></pre>
<p>The key change is <code>UPDATE ... WHERE code = ? AND used = false</code>. The database acquires a row lock during the update. Only one concurrent request can succeed. The second request finds <code>affectedRows = 0</code> and returns an error — correctly.</p>
<p><strong>Any time you read a value to make a decision before writing — that's a potential race condition. Make the check and the write atomic.</strong></p>
<h2 id="heading-5-business-logic-flaws">5. Business Logic Flaws</h2>
<p>Business logic flaws are the hardest category to catch. Automated scanners won't find them, and code review might miss them too, because the code works exactly as written. The problem is in what the code was designed to do, not how it does it.</p>
<p>The most common form: trusting the client to send sensible numeric values.</p>
<h3 id="heading-how-to-identify-this-vulnerability-in-your-code">How to Identify This Vulnerability in Your Code</h3>
<p>An e-commerce checkout endpoint:</p>
<pre><code class="language-javascript">// Express.js - Vulnerable
app.post('/api/checkout', authenticate, async (req, res) =&gt; {
  const { items } = req.body;

  let total = 0;
  const processedItems = [];

  for (const item of items) {
    const product = await db.query(
      'SELECT id, price FROM products WHERE id = ?',
      [item.productId]
    );

    if (!product) {
      return res.status(400).json({ error: `Product not found: ${item.productId}` });
    }

    // Trust the quantity value from the client
    const itemTotal = produ