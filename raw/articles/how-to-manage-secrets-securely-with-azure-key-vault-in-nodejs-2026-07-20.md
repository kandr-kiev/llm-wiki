---
source_url: https://www.freecodecamp.org/news/how-to-manage-secrets-securely-with-azure-key-vault-in-node-js/
ingested: 2026-07-20
sha256: f4118f79613e4ee988f8d6ffac8683a15fdf4bbd6bfce4e0cb593b4a2c84a0dd
blog_source: FreeCodeCamp Blog
---
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        
        
            <title>How to Manage Secrets Securely with Azure Key Vault in Node.js</title>
        
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
        
        
            <link rel="canonical" href="https://www.freecodecamp.org/news/how-to-manage-secrets-securely-with-azure-key-vault-in-node-js/">
        
        <meta name="referrer" content="no-referrer-when-downgrade">

        

        
    <meta name="description" content="Last year a client called me about exactly this. Someone ran git log -p on a hunch and found a .env committed two years earlier, never caught. Database password, Stripe secret, JWT signing key — all s">

    
    <meta property="og:site_name" content="freeCodeCamp.org">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Manage Secrets Securely with Azure Key Vault in Node.js">
    
        <meta property="og:description" content="Last year a client called me about exactly this. Someone ran git log -p on a hunch and found a .env committed two years earlier, never caught. Database password, Stripe secret, JWT signing key — all s">
    
    <meta property="og:url" content="https://www.freecodecamp.org/news/how-to-manage-secrets-securely-with-azure-key-vault-in-node-js/">
    <meta property="og:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/5491b408-9c6b-4d4d-a53e-215119fb2d97.png">
    <meta property="article:published_time" content="2026-07-20T13:50:42.257Z">
    <meta property="article:modified_time" content="2026-07-20T13:50:42.257Z">
    
        <meta property="article:tag" content="JavaScript">
    
        <meta property="article:tag" content="Security">
    
        <meta property="article:tag" content="Devops">
    
        <meta property="article:tag" content="Azure">
    
        <meta property="article:tag" content="Node.js">
    
    <meta property="article:publisher" content="https://www.facebook.com/freecodecamp">
    

    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Manage Secrets Securely with Azure Key Vault in Node.js">
    
        <meta name="twitter:description" content="Last year a client called me about exactly this. Someone ran git log -p on a hunch and found a .env committed two years earlier, never caught. Database password, Stripe secret, JWT signing key — all s">
    
    <meta name="twitter:url" content="https://www.freecodecamp.org/news/how-to-manage-secrets-securely-with-azure-key-vault-in-node-js/">
    <meta name="twitter:image" content="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/5491b408-9c6b-4d4d-a53e-215119fb2d97.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Zia Ullah">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="JavaScript, Security, Devops, Azure, Node.js">
    <meta name="twitter:site" content="@freecodecamp">
    
        <meta name="twitter:creator" content="@Zia_Ullah_Khan">
    

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
		"url": "https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/5491b408-9c6b-4d4d-a53e-215119fb2d97.png",
		"width": 1920,
		"height": 1080
	},
	"url": "https://www.freecodecamp.org/news/how-to-manage-secrets-securely-with-azure-key-vault-in-node-js/",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.freecodecamp.org/news/"
	},
	"datePublished": "2026-07-20T13:50:42.257Z",
	"dateModified": "2026-07-20T13:50:42.257Z",
	"keywords": "JavaScript, Security, Devops, Azure, Node.js",
	"description": "Last year a client called me about exactly this. Someone ran git log -p on a hunch and found a .env committed two years earlier, never caught. Database password, Stripe secret, JWT signing key — all s",
	"headline": "How to Manage Secrets Securely with Azure Key Vault in Node.js",
	"author": {
		"@type": "Person",
		"name": "Zia Ullah",
		"url": "https://www.freecodecamp.org/news/author/ziaullahzia/",
		"sameAs": [
			"https://ziaongit.github.io",
			"https://x.com/Zia_Ullah_Khan"
		],
		"image": {
			"@type": "ImageObject",
			"url": "https://cdn.hashnode.com/uploads/avatars/6a32d4e8d06aa63cd556c4b9/9666ebc0-e7de-4f75-bd06-852d27c30919.jpg",
			"width": 1024,
			"height": 1024
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
                        <time class="post-full-meta-date" data-test-label="post-full-meta-date" datetime="2026-07-20T13:50:42.257Z">
                            July 20, 2026
                        </time>
                        
                            <span class="date-divider">/</span>
                            <a dir="ltr" href="/news/tag/javascript/">
                                #JavaScript
                            </a>
                        
                    </section>
                    <h1 class="post-full-title" data-test-label="post-full-title">How to Manage Secrets Securely with Azure Key Vault in Node.js</h1>
                </header>
                
                    <div class="post-full-author-header" data-test-label="author-header-no-bio">
                        
                            
    
    
    

    <section class="author-card" data-test-label="author-card">
        
            
    <img srcset="https://cdn.hashnode.com/uploads/avatars/6a32d4e8d06aa63cd556c4b9/9666ebc0-e7de-4f75-bd06-852d27c30919.jpg 60w" sizes="60px" src="https://cdn.hashnode.com/uploads/avatars/6a32d4e8d06aa63cd556c4b9/9666ebc0-e7de-4f75-bd06-852d27c30919.jpg" class="author-profile-image" alt="Zia Ullah" width="1024" height="1024" onerror="this.style.display='none'" data-test-label="profile-image">
  
        

        <section class="author-card-content author-card-content-no-bio">
            <span class="author-card-name">
                <a href="/news/author/ziaullahzia/" data-test-label="profile-link">
                    
                        Zia Ullah
                    
                </a>
            </span>
            
        </section>
    </section>

                        
                    </div>
                
                <figure class="post-full-image">
                    
    <picture>
      <source media="(max-width: 700px)" sizes="1px" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 1w">
      <source media="(min-width: 701px)" sizes="(max-width: 800px) 400px, (max-width: 1170px) 700px, 1400px" srcset="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/5491b408-9c6b-4d4d-a53e-215119fb2d97.png">
      <img onerror="this.style.display='none'" src="https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/5491b408-9c6b-4d4d-a53e-215119fb2d97.png" alt="How to Manage Secrets Securely with Azure Key Vault in Node.js" ,="" width="1920" height="1080" data-test-label="feature-image">
    </picture>
  
                </figure>
                <section class="post-full-content">
                    <div class="post-and-sidebar">
                        <section class="post-content " data-test-label="post-content">
                            
<p>Last year a client called me about exactly this. Someone ran <code>git log -p</code> on a hunch and found a <code>.env</code> committed two years earlier, never caught. Database password, Stripe secret, JWT signing key — all still active. All still in production.</p>
<p>IBM's 2024 breach cost report put the average data breach at <strong>$4.88 million</strong> — and that's the average, not the worst cases.</p>
<p>Exposed credentials are consistently near the top of root causes. GitHub found over a million secrets leaked in public repos in 2023 alone, before you even count the private ones nobody ever discovered.</p>
<p>It's not a people problem. The developers I've worked with aren't careless — the architecture is just set up to fail them. A <code>.env</code> file gets committed once by accident. Credentials get copied and pasted into a Slack message to unblock a teammate. A Docker image gets published with secrets baked into a layer. A server gets shut down, and nobody rotates the credentials it was holding.</p>
<p>Azure Key Vault solves this differently. Your application fetches credentials at runtime from a centralized, encrypted service — the <code>.env</code> file stops being a liability because it stops holding anything worth stealing.</p>
<p>What you'll build is a Node.js Express API that fetches every secret from Azure Key Vault at startup. No passwords in the code. When someone quits, there's nothing in the repo to rotate. The <code>.env</code> ends up with one line — the vault name.</p>
<h2 id="heading-prerequisites">Prerequisites</h2>
<ul>
<li><p>Node.js 18+</p>
</li>
<li><p>An Azure account (free tier works)</p>
</li>
<li><p>Azure CLI installed and logged in (<code>az login</code>)</p>
</li>
<li><p>Basic knowledge of Express.js</p>
</li>
<li><p>Docker (optional — only needed for the local database test section)</p>
</li>
</ul>
<h2 id="heading-what-we-will-build">What We Will Build</h2>
<p>A Node.js Express API that:</p>
<ol>
<li><p>Connects to PostgreSQL using credentials fetched from Key Vault at startup</p>
</li>
<li><p>Uses Managed Identity for authentication — no client secrets or passwords anywhere</p>
</li>
<li><p>Caches secrets in memory, so Key Vault isn't called on every request</p>
</li>
<li><p>Works locally via Azure CLI auth and in production via Managed Identity — same code, zero changes</p>
</li>
</ol>
<h2 id="heading-table-of-contents">Table of Contents</h2>
<ol>
<li><p><a href="#heading-how-the-architecture-works">How the Architecture Works</a></p>
</li>
<li><p><a href="#heading-what-is-azure-key-vault">What Is Azure Key Vault?</a></p>
</li>
<li><p><a href="#heading-set-up-the-key-vault">Set Up the Key Vault</a></p>
</li>
<li><p><a href="#heading-create-the-nodejs-project">Create the Node.js Project</a></p>
</li>
<li><p><a href="#heading-connect-to-key-vault-with-managed-identity">Connect to Key Vault with Managed Identity</a></p>
</li>
<li><p><a href="#heading-cache-secrets-at-startup">Cache Secrets at Startup</a></p>
</li>
<li><p><a href="#heading-use-secrets-in-your-express-api">Use Secrets in Your Express API</a></p>
</li>
<li><p><a href="#heading-test-locally">Test Locally</a></p>
</li>
<li><p><a href="#heading-deploy-to-azure-app-service">Deploy to Azure App Service</a></p>
</li>
<li><p><a href="#heading-grant-key-vault-access-to-the-app">Grant Key Vault Access to the App</a></p>
</li>
<li><p><a href="#heading-rotate-secrets-without-redeploying">Rotate Secrets Without Redeploying</a></p>
</li>
<li><p><a href="#heading-troubleshooting">Troubleshooting</a></p>
</li>
<li><p><a href="#heading-wrapping-up">Wrapping Up</a></p>
</li>
</ol>
<h2 id="heading-how-the-architecture-works">How the Architecture Works</h2>
<p>Before writing any code, it helps to see the full picture:</p>
<pre><code class="language-plaintext"> LOCAL DEVELOPMENT
.-------------------------------------------------------.
|                                                        |
|   [Node.js App]                                        |
|        |                                               |
|        v                                               |
|   [DefaultAzureCredential] ---&gt; az login session       |
|        |                                               |
|        v                                               |
|   [Azure Key Vault]  ---&gt; Returns secrets              |
|        |                                               |
|        v                                               |
|   [In-memory cache]  ---&gt; App uses secrets at runtime  |
'-------------------------------------------------------'

 PRODUCTION (Azure)
.-------------------------------------------------------.
|                                                        |
|   [Azure App Service]                                  |
|        |                                               |
|        v                                               |
|   [DefaultAzureCredential] ---&gt; Managed Identity       |
|        |                                               |
|        v                                               |
|   [Azure Key Vault]  ---&gt; Returns secrets              |
|        |                                               |
|        v                                               |
|   [In-memory cache]  ---&gt; App uses secrets at runtime  |
'-------------------------------------------------------'
</code></pre>
<p>Both environments run the exact same code. <code>DefaultAzureCredential</code> figures out where it is — locally it picks up your <code>az login</code> session, on Azure it uses Managed Identity. You don't switch config files and you don't manage credentials. It just works.</p>
<h2 id="heading-what-is-azure-key-vault">What Is Azure Key Vault?</h2>
<p>Azure Key Vault is Microsoft's managed secret store — it handles secrets, keys, and certificates. For this tutorial, we're only using the secrets part: database passwords, API keys, JWT signing keys, anything your app needs to run but has no business being in your Git history.</p>
<p>Compared to <code>.env</code> files, the practical differences are worth understanding before you write any code.</p>
<p>Rotation is the one I notice most on real projects. Update a secret in Key Vault and every app picks it up on the next restart — no hunting down five different environment configs across staging and production.</p>
<p>Access control is the other big one. Each application only gets permission to read the secrets it actually needs. If one service gets compromised, it can't read credentials belonging to other services.</p>
<p>And every read gets logged. When something goes wrong — and eventually something will — you can see exactly which app accessed which secret, and when. That log is what auditors actually want to see.</p>
<p>I've sat in enough security reviews to know that "we use <code>.env</code> files and tell people not to commit them" doesn't satisfy an auditor. SOC 2, HIPAA, GDPR — they all want demonstrable controls. A vault with an access log is demonstrable.</p>
<h2 id="heading-set-up-the-key-vault">Set Up the Key Vault</h2>
<p>Run these commands. The vault name has to be globally unique across all of Azure — not just your own subscription — so pick something specific. Letters, numbers, and hyphens, 3 to 24 characters.</p>
<pre><code class="language-bash"># Create a resource group (skip if you already have one)
az group create \
  --name keyvault-demo-rg \
  --location eastus

# Create the Key Vault (RBAC enabled by default — required for the role assignment later)
az keyvault create \
  --name your-vault-name \
  --resource-group keyvault-demo-rg \
  --location eastus

# Grant yourself permission to manage secrets (required with RBAC — creators are not auto-assigned)
az role assignment create \
  --role "Key Vault Secrets Officer" \
  --assignee-object-id $(az ad signed-in-user show --query id -o tsv) \
  --scope $(az keyvault show \
    --name your-vault-name \
    --resource-group keyvault-demo-rg \
    --query id -o tsv)

# Add your secrets
az keyvault secret set \
  --vault-name your-vault-name \
  --name "DB-HOST" \
  --value "your-db-host.postgres.database.azure.com"

az keyvault secret set \
  --vault-name your-vault-name \
  --name "DB-PASSWORD" \
  --value "your-super-secret-password"

az keyvault secret set \
  --vault-name your-vault-name \
  --name "JWT-SECRET" \
  --value "your-jwt-signing-secret"
</code></pre>
<p>Verify the secrets were stored:</p>
<pre><code class="language-bash">az keyvault secret list --vault-name your-vault-name --query "[].name" -o tsv
</code></pre>
<p>You should see:</p>
<pre><code class="language-plaintext">DB-HOST
DB-PASSWORD
JWT-SECRET
</code></pre>
<h2 id="heading-create-the-nodejs-project">Create the Node.js Project</h2>
<p>Set up the project structure:</p>
<pre><code class="language-bash">mkdir nodejs-azure-keyvault
cd nodejs-azure-keyvault
npm init -y
npm install express pg jsonwebtoken @azure/keyvault-secrets @azure/identity dotenv
</code></pre>
<p>The two Azure packages do all the work:</p>
<ul>
<li><p><code>@azure/keyvault-secrets</code> — connects to your vault and pulls secrets out</p>
</li>
<li><p><code>@azure/identity</code> — handles auth. Locally, it uses your <code>az login</code> session, in production, it switches to Managed Identity automatically</p>
</li>
</ul>
<p>Add a start script to <code>package.json</code>:</p>
<pre><code class="language-bash">npm pkg set scripts.start="node server.js"
</code></pre>
<p>Create the following file structure:</p>
<pre><code class="language-plaintext">nodejs-azure-keyvault/
|-- src/
|   |-- config/
|   |   `-- secrets.js   # Key Vault client and secret loader
|   |-- db/
|   |   `-- index.js     # PostgreSQL pool using secrets
|   `-- routes/
|       `-- users.js     # Example route
|-- app.js               # Express app
`-- server.js            # Entry point -- loads secrets first
</code></pre>
<h2 id="heading-connect-to-key-vault-with-managed-identity">Connect to Key Vault with Managed Identity</h2>
<p>Create the secrets config file:</p>
<pre><code class="language-javascript">// src/config/secrets.js
const { SecretClient } = require('@azure/keyvault-secrets');
const { DefaultAzureCredential } = require('@azure/identity');

const VAULT_URL = `https://${process.env.KEY_VAULT_NAME}.vault.azure.net`;

const credential = new DefaultAzureCredential();
const client = new SecretClient(VAULT_URL, credential);

async function getSecret(name) {
  const secret = await client.getSecret(name);
  return secret.value;
}

module.exports = { getSecret };
</code></pre>
<p><code>DefaultAzureCredential</code> is the most important part of this setup. It tries a chain of authentication methods in order:</p>
<ol>
<li><p>Environment variables (for CI/CD pipelines)</p>
</li>
<li><p>Azure CLI credentials (for local development — <code>az login</code>)</p>
</li>
<li><p>Managed Identity (for deployed apps on Azure)</p>
</li>
</ol>
<p>This means the exact same code works locally and in production with zero changes. Locally, it uses your <code>az login</code> session. In production, it uses the app's Managed Identity. You never touch credentials.</p>
<h2 id="heading-cache-secrets-at-startup">Cache Secrets at Startup</h2>
<p>Calling Key Vault on every request adds latency and costs money. Load all secrets once at startup and cache them in memory. Replace <code>src/config/secrets.js</code> with this complete version:</p>
<pre><code class="language-javascript">// src/config/secrets.js
const { SecretClient } = require('@azure/keyvault-secrets');
const { DefaultAzureCredential } = require('@azure/identity');

const VAULT_URL = `https://${process.env.KEY_VAULT_NAME}.vault.azure.net`;

const credential = new DefaultAzureCredential();
const client = new SecretClient(VAULT_URL, credential);

// In-memory cache
const cache = {};

async function getSecret(name) {
  if (cache[name]) return cache[name];
  const secret = await client.getSecret(name);
  cache[name] = secret.value;
  return secret.value;
}

async function loadAllSecrets() {
  console.log('Loading secrets from Azure Key Vault...');
  const secretNames = ['DB-HOST', 'DB-PASSWORD', 'JWT-SECRET'];

  await Promise.all(
    secretNames.map(async (name) =&gt; {
      cache[name] = await getSecret(name);
      console.log(`  ✓ ${name} loaded`);
    })
  );

  console.log('All secrets loaded successfully.');
}

function getFromCache(name) {
  if (!cache[name]) throw new Error(`Secret "${name}" not loaded. Did loadAllSecrets() run?`);
  return cache[name];
}

module.exports = { loadAllSecrets, getFromCache };
</code></pre>
<p>The <code>loadAllSecrets</code> function runs once when the application starts. After that, all secrets are served from the in-memory cache with zero latency and zero Key Vault calls.</p>
<h2 id="heading-use-secrets-in-your-express-api">Use Secrets in Your Express API</h2>
<p>Set up the database connection using the cached secrets:</p>
<pre><code class="language-javascript">// src/db/index.js
const { Pool } = require('pg');
const { getFromCache } = require('../config/secrets');

let pool;

function getPool() {
  if (!pool) {
    pool = new Pool({
      host:     getFromCache('DB-HOST'),
      database: process.env.DB_NAME || 'myapp',
      user:     process.env.DB_USER || 'dbadmin',
      password: getFromCache('DB-PASSWORD'),
      port:     parseInt(process.env.DB_PORT || '5432'),
      ssl:      process.env.NODE_ENV === 'production'
                  ? { rejectUnauthorized: false }
                  : false,
    });

    pool.on('error', (err) =&gt; {
      console.error('Unexpected database pool error:', err.message);
    });
  }

  return pool;
}

module.exports = { getPool };
</code></pre>
<p>Notice the distinction: <code>DB-HOST</code> and <code>DB-PASSWORD</code> come from Key Vault because they're sensitive. The database name, username, and port are not — they don't need to be protected, so they use environment variables with sensible defaults. Key Vault is for credentials, not all configuration.</p>
<p>The SSL flag is environment-aware: forced on in production, off locally so Docker connections work without a certificate. The <code>rejectUnauthorized: false</code> setting accepts Azure Database for PostgreSQL's certificate without verifying the CA chain — this is standard for Azure-managed databases. For stricter environments, you can download the Azure root CA and pass it via the <code>ca</code> option in the pool config instead.</p>
<p>Create a sample route that uses JWT verification with the secret from Key Vault:</p>
<pre><code class="language-javascript">// src/routes/users.js
const express = require('express');
const jwt     = require('jsonwebtoken');
const { getFromCache } = require('../config/secrets');
const { getPool }      = require('../db');

const router = express.Router();

// Auth middleware — JWT secret comes from Key Vault, not process.env
function authMiddleware(req, res, next) {
  const authHeader = req.headers.authorization;
  if (!authHeader?.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Missing or malformed Authorization header' });
  }

  const token = authHeader.split(' ')[1];

  try {
    req.user = jwt.verify(token, getFromCache('JWT-SECRET'));
    next();
  } catch (err) {
    return res.status(401).json({ error: 'Invalid or expired token' });
  }
}

// GET /api/users — list users (authenticated)
router.get('/', authMiddleware, async (req, res) =&gt; {
  try {
    const result = await getPool().query(
      'SELECT id, email, created_at FROM users ORDER BY created_at DESC LIMIT 20'
    );
    res.json(result.rows);
  } catch (err) {
    console.error('Database error:', err.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// GET /api/users/:id — single user (authenticated)
router.get('/:id', authMiddleware, async (req, res) =&gt; {
  try {
    const result = await getPool().query(
      'SELECT id, email, created_at FROM users WHERE id = $1',
      [req.params.id]
    );
    if (!result.rows[0]) return res.status(404).json({ error: 'User not found' });
    res.json(result.rows[0]);
  } catch (err) {
    console.error('Database error:', err.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

module.exports = router;
</code></pre>
<p>Notice the error handler returns <code>'Internal server error'</code> instead of <code>err.message</code>. Database errors are surprisingly chatty — they'll hand an attacker your table names, column names, and query structure if you let them through.</p>
<p>Set up the Express application. Both files define <code>authMiddleware</code> locally — yes, it's duplicated. In production, I'd pull this into a shared middleware file. For this tutorial, keeping it local means you can read either file without bouncing between three others:</p>
<pre><code class="language-javascript">// app.js
const express = require('express');
const jwt = require('jsonwebtoken');
const { getFromCache } = require('./src/config/secrets');
const usersRouter = require('./src/routes/users');

const app = express();
app.use(express.json());

// Auth middleware — JWT secret comes from Key Vault, not process.env
function authMiddleware(req, res, next) {
  const authHeader = req.headers.authorization;
  if (!authHeader?.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Missing or malformed Authorization header' });
  }
  const token = authHeader.split(' ')[1];
  try {
    req.user = jwt.verify(token, getFromCache('JWT-SECRET'));
    next();
  } catch (err) {
    return res.status(401).json({ error: 'Invalid or expired token' });
  }
}

// Health check — no auth required
app.get('/health', (req, res) =&gt; {
  res.json({ status: 'healthy', timestamp: new Date().toISOString() });
});

// Status endpoint — proves Key Vault integration without needing a database
app.get('/api/status', authMiddleware, (req, res) =&gt; {
  res.json({
    message: 'All secrets loaded from Azure Key Vault',
    vault: process.env.KEY_VAULT_NAME,
    secrets_loaded: ['DB-HOST', 'DB-PASSWORD', 'JWT-SECRET'],
    authenticated_as: req.user.email,
    timestamp: new Date().toISOString()
  });
});

app.use('/api/users', usersRouter);

app.use((req, res) =&gt; res.status(404).json({ error: 'Route not found' }));
app.use((err, req, res, next) =&gt; {
  console.error('Unhandled error:', err.message);
  res.status(500).json({ error: 'Internal server error' });
});

module.exports = app;
</code></pre>
<p>The entry point loads secrets before starting the server. The server doesn't start unless all secrets load successfully:</p>
<pre><code class="language-javascript">// server.js
require('dotenv').config();
const app = require('./app');
const { loadAllSecrets } = require('./src/config/secrets');

const PORT = process.env.PORT || 3000;

async function start() {
  try {
    await loadAllSecrets();
    app.listen(PORT, () =&gt; {
      console.log(`Server running on port ${PORT}`);
    });
  } catch (err) {
    console.error('Failed to start server:', err.message);
    console.error('Hint: Run "az login" for local development, or check Managed Identity for Azure deployments.');
    process.exit(1);
  }
}

start();
</code></pre>
<p>That <code>process.exit(1)</code> is deliberate. I'd rather the app crash loudly at startup than limp along with missing credentials and fail on the first real request two hours later.</p>
<h2 id="heading-test-locally">Test Locally</h2>
<p>Create a <code>.env</code> file for local development. This only contains the Key Vault name, nothing sensitive:</p>
<pre><code class="language-bash"># .env
KEY_VAULT_NAME=your-vault-name
PORT=3000
</code></pre>
<p>Add <code>.env</code> and the deployment zip to <code>.gitignore</code>:</p>
<pre><code class="language-bash">echo ".env" &gt;&gt; .gitignore
echo "app.zip" &gt;&gt; .gitignore
</code></pre>
<p>Make sure you're logged into Azure CLI:</p>
<pre><code class="language-bash">az login
</code></pre>
<p>Start the application:</p>
<pre><code class="language-bash">npm start
</code></pre>
<p>You should see:</p>
<pre><code class="language-plaintext">Loading secrets from Azure Key Vault...
  ✓ JWT-SECRET loaded
  ✓ DB-PASSWORD loaded
  ✓ DB-HOST loaded
All secrets loaded successfully.
Server running on port 3000
</code></pre>
<p>The order secrets load may vary — <code>Promise.all</code> fetches them in parallel and resolves as each one completes. What matters is that all three are confirmed before the server starts.</p>
