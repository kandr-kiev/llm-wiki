---
source_url: https://laravel-news.com/laravel-legacy-bridge-carry-authenticated-sessions-from-a-legacy-app-into-laravel?utm_medium=feed&utm_source=feedpress.me&utm_campaign=Feed%3A+laravelnews
ingested: 2026-07-17
sha256: 030ec495b9c0b7c6b33561b08bf10524919449ebb3e0d59448db398e17108638
blog_source: Laravel News
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <meta name="csrf-token" content=""/>

    <title>Laravel Legacy Bridge: Carry Authenticated Sessions from a Legacy App into Laravel - Laravel News</title>
    
    
    <meta
        name="description"
        content="Laravel Legacy Bridge reads a legacy PHP session cookie, decodes the payload, and logs the matching user into Laravel, so users mid-migration don&#039;t hit a second login prompt."
    />
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="Laravel Legacy Bridge: Carry Authenticated Sessions from a Legacy App into Laravel - Laravel News"/>
    <meta
        property="og:description"
        content="Laravel Legacy Bridge reads a legacy PHP session cookie, decodes the payload, and logs the matching user into Laravel, so users mid-migration don&#039;t hit a second login prompt."
    />
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="Laravel Legacy Bridge: Carry Authenticated Sessions from a Legacy App into Laravel - Laravel News"/>
    <meta
        property="og:image"
        content="https://laravelnews.s3.amazonaws.com/featured-images/Legacy-Bridge-LN.png"
    />
    <meta
        property="og:description"
        content="Laravel Legacy Bridge reads a legacy PHP session cookie, decodes the payload, and logs the matching user into Laravel, so users mid-migration don&#039;t hit a second login prompt."
    />
    <meta property="og:url" content="https://laravel-news.com/laravel-legacy-bridge-carry-authenticated-sessions-from-a-legacy-app-into-laravel"/>
    <meta property="og:site_name" content="Laravel News"/>
    <meta property="og:locale" content="en_US"/>

    
    <meta name="twitter:card" content="summary_large_image"/>
    <meta name="twitter:site" content="@laravelnews"/>
    <meta name="twitter:title" content="Laravel Legacy Bridge: Carry Authenticated Sessions from a Legacy App into Laravel - Laravel News"/>
    <meta
        property="twitter:image"
        content="https://laravelnews.s3.amazonaws.com/featured-images/Legacy-Bridge-LN.png"
    />
    <meta
        name="twitter:description"
        content="Laravel Legacy Bridge reads a legacy PHP session cookie, decodes the payload, and logs the matching user into Laravel, so users mid-migration don&#039;t hit a second login prompt."
    />
            <meta name="twitter:creator" content="@ylynfatt"/>
    
    <link href="https://laravel-news.com/laravel-legacy-bridge-carry-authenticated-sessions-from-a-legacy-app-into-laravel" rel="canonical"/>
    <link href="https://laravel-news.com/" rel="home"/>

    <link
        rel="alternate"
        type="application/rss+xml"
        title="Laravel News &raquo; Feed"
        href="https://feed.laravel-news.com/"
    />
    <link
        rel="alternate"
        title="Laravel News Feed"
        type="application/json"
        href="https://laravel-news.com/feed/json"
    />
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png"/>
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png"/>
    <link rel="manifest" href="/site.webmanifest"/>
    <meta name="p:domain_verify" content="10fb40c4dd5b036ab42f1d935c6400b6"/>
    <meta name="facebook-domain-verification" content="smr6d95hfkmrn505mfkv7dzalj68g2"/>
    <meta property="fb:admins" content="100007722642618"/>
    <meta property="fb:app_id" content="440569919467159"/>

    
    <link rel="preconnect" href="https://use.typekit.net"/>
    <link rel="preconnect" href="https://fonts.bunny.net"/>
    <link href="https://fonts.bunny.net/css?family=jetbrains-mono:400,400i" rel="stylesheet"/>
    <link rel="stylesheet" href="https://use.typekit.net/rgt0rac.css">

    
    <script src="https://cdn.usefathom.com/script.js" data-site="BYASFNCM" defer></script>

    <meta property="fb:admins" content="100007722642618"/>
    <meta property="fb:app_id" content="440569919467159"/>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-LE9GHTERHJ"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-LE9GHTERHJ');
    </script>

    <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer ></script>

    <link rel="preload" as="style" href="https://laravel-news.com/build/assets/app-57af3fb7.css" /><link rel="modulepreload" as="script" href="https://laravel-news.com/build/assets/app-361f5ee5.js" /><link rel="stylesheet" href="https://laravel-news.com/build/assets/app-57af3fb7.css" data-navigate-track="reload" /><script type="module" src="https://laravel-news.com/build/assets/app-361f5ee5.js" data-navigate-track="reload"></script>
    
    <!-- Livewire Styles --><style >[wire\:loading][wire\:loading], [wire\:loading\.delay][wire\:loading\.delay], [wire\:loading\.inline-block][wire\:loading\.inline-block], [wire\:loading\.inline][wire\:loading\.inline], [wire\:loading\.block][wire\:loading\.block], [wire\:loading\.flex][wire\:loading\.flex], [wire\:loading\.table][wire\:loading\.table], [wire\:loading\.grid][wire\:loading\.grid], [wire\:loading\.inline-flex][wire\:loading\.inline-flex] {display: none;}[wire\:loading\.delay\.none][wire\:loading\.delay\.none], [wire\:loading\.delay\.shortest][wire\:loading\.delay\.shortest], [wire\:loading\.delay\.shorter][wire\:loading\.delay\.shorter], [wire\:loading\.delay\.short][wire\:loading\.delay\.short], [wire\:loading\.delay\.default][wire\:loading\.delay\.default], [wire\:loading\.delay\.long][wire\:loading\.delay\.long], [wire\:loading\.delay\.longer][wire\:loading\.delay\.longer], [wire\:loading\.delay\.longest][wire\:loading\.delay\.longest] {display: none;}[wire\:offline][wire\:offline] {display: none;}[wire\:dirty]:not(textarea):not(input):not(select) {display: none;}:root {--livewire-progress-bar-color: #2299dd;}[x-cloak] {display: none !important;}[wire\:cloak] {display: none !important;}dialog#livewire-error::backdrop {background-color: rgba(0, 0, 0, .6);}</style>
    </head>

<body class="relative antialised min-h-screen bg-white font-sans text-black">


<div x-persist="header">
<header
    x-data="{
        mobileMenuIsOpen: false,
        searchModalIsOpen: false,
        init() {
            document.addEventListener('livewire:navigating', () => {
                this.mobileMenuIsOpen = false;
                this.searchModalIsOpen = false;
            });
        },
    }"
    class="absolute inset-x-0 z-10"
>
    <div
        class="shadow-card z-50 flex items-center justify-center bg-red-600 p-2 text-center text-sm text-white">
        <div id="top-ad" x-init="$ajax('/api/ad/top')">&nbsp;</div>
    </div>
    <div
        class="mt-5 mx-auto flex w-full max-w-7xl items-center justify-between gap-4 px-6 py-6 md:gap-8 md:py-10"
    >
        <div class="xl:gap-18 flex items-center gap-16">
            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 hover:-translate-y-1 hover:opacity-70 focus-visible:ring-offset-2" href="/"
    >
    <img
    class="lg:h-18 lg:w-18 h-12 w-12 sm:h-16 sm:w-16"
    width="87"
    height="86"
    src="https://picperf.io/https://laravel-news.com/images/logo.svg"
    alt="Laravel News"
/>
                <span class="sr-only">Laravel News</span>
</a>
            <div class="hidden items-center gap-4 sm:flex md:gap-8">
                <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 p-1 font-bold hover:text-gray-600" href="/blog"
    >
    Blog
</a>
                <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 p-1 font-bold hover:text-gray-600" href="/category/tutorials"
    >
    Tutorials
</a>
                <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 p-1 font-bold hover:text-gray-600" href="/category/packages"
    >
    Packages
</a>
                <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 !hidden p-1 font-bold hover:text-gray-600 md:!inline-flex" href="/newsletter"
    >
    Newsletter
</a>
                <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 !hidden p-1 font-bold hover:text-gray-600 md:!inline-flex" href="/podcasts"
    >
    Podcasts
</a>
            </div>
        </div>
        <div class="xl:gap-18 flex items-center gap-16">
            <div class="hidden items-center gap-4 md:gap-8 lg:flex">
                
                
                
                
                
                
                
                <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 p-1 font-bold hover:text-gray-600" href="/partners"
            wire:navigate.hover
    >
    Partners
</a>
                <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 p-1 font-bold hover:text-gray-600" href="/links"
            wire:navigate.hover
    >
    Links
</a>
                <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 p-1 font-bold hover:text-gray-600" href="/login"
            wire:navigate.hover
    >
    Your Account
</a>
            </div>
            <div class="-mr-1 flex items-center gap-2">
                <button
                    class="inline-flex rounded-sm p-1 leading-none text-black transition duration-300 hover:text-gray-600 focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 focus-visible:ring-offset-4 focus-visible:ring-offset-white"
                    @click.prevent="searchModalIsOpen = true"
                >
                    <img
                        src="https://picperf.io/https://laravel-news.com/images/icons/search.svg"
                        class="h-6 w-6"
                        alt="Search"
                    />
                    <span class="sr-only">Search</span>
                </button>
                <button
                    class="inline-flex rounded-sm p-1 leading-none text-black transition duration-300 hover:text-gray-600 focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 focus-visible:ring-offset-4 focus-visible:ring-offset-white lg:hidden"
                    @click.prevent="mobileMenuIsOpen = true"
                >
                    <img src="https://picperf.io/https://laravel-news.com/images/icons/menu.svg" class="h-6 w-6" alt="Menu"/>
                    <span class="sr-only">Menu</span>
                </button>
            </div>
        </div>
    </div>
    <template x-teleport="body">
    <div
        x-dialog
        x-model="mobileMenuIsOpen"
        x-cloak
        class="fixed inset-0 z-50 overflow-hidden lg:hidden"
    >
        
        <div x-dialog:overlay x-transition.opacity class="fixed inset-0 bg-black/50"></div>

        
        <div class="fixed inset-y-0 right-0 w-full max-w-lg">
            <div
                x-dialog:panel
                x-transition:enter="transition duration-300 ease-out"
                x-transition:enter-start="translate-x-full"
                x-transition:enter-end="translate-x-0"
                x-transition:leave="transition duration-300 ease-in"
                x-transition:leave-start="translate-x-0"
                x-transition:leave-end="translate-x-full"
                class="h-full w-full"
            >
                <div
                    class="flex h-full flex-col justify-between overflow-y-auto bg-white shadow-card"
                >
                    <div class="p-6 md:p-10">
                        <div class="flex items-center justify-between">
                            
                            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 hover:-translate-y-1 hover:opacity-70 focus-visible:ring-offset-2" href="/"
            wire:navigate.hover
    >
    <img
    class="h-12 w-12 sm:h-16 sm:w-16"
    width="87"
    height="86"
    src="https://picperf.io/https://laravel-news.com/images/logo.svg"
    alt="Laravel News"
/>
                                <h2 x-dialog:title class="sr-only">Laravel News</h2>
</a>

                            
                            <button
                                type="button"
                                @click="$dialog.close()"
                                class="rounded-sm p-1 focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 focus-visible:ring-offset-4"
                            >
                                <span class="sr-only">Close menu</span>

                                <img
                                    src="https://picperf.io/https://laravel-news.com/images/icons/close.svg"
                                    class="h-6 w-6"
                                    alt="Close menu"
                                />
                            </button>
                        </div>
                        <div class="-mx-1 mt-12 flex flex-col gap-4">
                            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 p-1 hover:text-gray-600" href="/blog"
            wire:navigate.hover
    >
    Blog
</a>
                            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 p-1 hover:text-gray-600" href="/category/tutorials"
            wire:navigate.hover
    >
    Tutorials
</a>
                            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 p-1 hover:text-gray-600" href="/category/packages"
            wire:navigate.hover
    >
    Packages
</a>
                            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 p-1 hover:text-gray-600" href="/podcasts"
    >
    Podcasts
</a>
                            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 p-1 hover:text-gray-600" href="/newsletter"
            wire:navigate.hover
    >
    Newsletter
</a>
                            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 p-1 hover:text-gray-600" href="/links"
            wire:navigate.hover
    >
    Community Links
</a>
                            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 p-1 hover:text-gray-600" href="/partners"
            wire:navigate.hover
    >
    Partners
</a>
                            <div class="px-1 py-3">
                                <hr class="border-gray-600/30"/>
                            </div>
                            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 p-1 hover:text-gray-600" href="/login"
            wire:navigate.hover
    >
    Your Account
</a>
                            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 p-1 hover:text-gray-600" href="/partnerships"
            wire:navigate.hover
    >
    Advertising
</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    <template x-teleport="body">
    <div
        x-data="{
            initialized: false,
            init() {
                $watch('searchModalIsOpen', (value) => {
                    if (! this.initialized) {
                        search.start();

                        this.initialized = true;
                    }

                    if (value) {
                        setTimeout(() => {
                            this.$el.querySelector('input').focus();
                        }, 100);
                    }
                });
            },
        }"
        x-dialog
        x-model="searchModalIsOpen"
        x-cloak
        class="fixed inset-0 z-10"
        @keydown.slash.meta.window="searchModalIsOpen = !searchModalIsOpen"
        @keydown.k.meta.window="searchModalIsOpen = !searchModalIsOpen"
        @keydown.escape.window="searchModalIsOpen = false"
    >
        <div
            x-dialog:overlay
            x-transition.opacity
            class="fixed inset-0 bg-black/60 backdrop-blur-sm"
        ></div>

        <div class="relative flex min-h-screen items-center justify-center p-4">
            <div
                x-dialog:panel
                x-transition.opacity.duration.400ms
                class="relative h-[88vh] w-full max-w-3xl overflow-y-auto rounded-lg border border-gray-100 bg-white shadow-card"
            >
                <div class="p-6 lg:p-12">
                    <div class="flex items-center justify-between gap-4">
                        <h2 x-dialog:title class="text-2xl font-bold">Search Articles
                            
                        </h2>
                        <button
                            type="button"
                            @click="$dialog.close()"
                            class="rounded-sm p-1 focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 focus-visible:ring-offset-4"
                        >
                            <span class="sr-only">Close search</span>

                            <img
                                src="https://picperf.io/https://laravel-news.com/images/icons/close.svg"
                                class="h-6 w-6"
                                alt="Close menu"
                            />
                        </button>
                    </div>

                    <div class="ais-InstantSearch mt-10">
                        <div id="searchbox"></div>
                        <div id="hits"></div>
                        <div class="mt-1 border-gray-200 border-t">
                            <p class="mt-4">
                                Or try
                                <a href="/search"
                                   class="focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 font-bold text-red-600 hover:text-red-700">
                                    paginated search →
                                </a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
</header>
</div>

<div>
    <link
            rel="preload"
            fetchpriority="high"
            as="image"
            href="https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/Legacy-Bridge-LN.png"
        />
    
    <script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "NewsArticle",
    "headline": "Laravel Legacy Bridge: Carry Authenticated Sessions from a Legacy App into Laravel",
    "datePublished": "2026-07-15T08:45:00-04:00",
    "description": "Laravel Legacy Bridge reads a legacy PHP session cookie, decodes the payload, and logs the matching user into Laravel, so users mid-migration don't hit a second login prompt.",
    "image": "https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/Legacy-Bridge-LN.png",
    "dateModified": "2026-07-14T20:29:25-04:00",
    "author": {
        "@type": "Person",
        "name": "Yannick Lyn Fatt",
        "url": "https://laravel-news.com/@ylynfatt"
    },
    "publisher": {
        "@type": "Organization",
        "name": "Laravel News",
        "logo": {
            "@type": "ImageObject",
            "url": "https://laravel-news.com/android-chrome-512x512.png"
        }
    },
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://laravel-news.com/laravel-legacy-bridge-carry-authenticated-sessions-from-a-legacy-app-into-laravel"
    }
}
</script>

    <script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://laravel-news.com"
        },
        {
            "@type": "ListItem",
            "position": 2,
            "name": "Laravel Packages",
            "item": "https://laravel-news.com/category/packages"
        },
        {
            "@type": "ListItem",
            "position": 3,
            "name": "Laravel Legacy Bridge: Carry Authenticated Sessions from a Legacy App into Laravel"
        }
    ]
}
</script>
    <article>
        <div class="relative bg-gradient-to-r from-gray-100 to-white">
            <div class="h-[160px] sm:h-[148px] md:h-[180px]"></div>
            
            <div class="absolute inset-x-0 bottom-0 h-1/4 w-full bg-white"></div>

            <div
                class=" relative mx-auto w-full max-w-4xl px-6 pt-10"
            >
                <h1 class="text-4xl font-bold sm:text-5xl md:text-6xl">Laravel Legacy Bridge: Carry Authenticated Sessions from a Legacy App into Laravel</h1>

                <div class="mt-6 flex items-center gap-3">

                    <p class="text-xs text-gray-600">
                                                    Last updated on
                            <time
                                itemprop="dateModified"
                                datetime="2026-07-14T20:29:25"
                            >
                                July 14th, 2026
                            </time>
                                                by
                        <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 hover:text-red-600" href="/@ylynfatt" rel="author"
            wire:navigate.hover
    >
    Yannick Lyn Fatt
</a>

                    </p>
                </div>
                                    <img
                        src="https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/Legacy-Bridge-LN.png"
                        alt="Laravel Legacy Bridge: Carry Authenticated Sessions from a Legacy App into Laravel image"
                        class="mt-12 aspect-[2/1] w-full overflow-hidden rounded-xl object-cover shadow-card"
                    />
                            </div>
        </div>
        <div class="mx-auto w-full max-w-4xl px-6 py-20">


            
            <div
                class="prose max-w-4xl break-words prose-a:text-red-600 prose-a:transition prose-a:hover:text-red-700 prose-pre:rounded-lg prose-pre:bg-gray-100/50 prose-pre:p-6 prose-img:mx-auto prose-img:rounded-lg prose-img:border prose-img:border-gray-100"
            >
                <p>Migrating an application to Laravel one route at a time leaves you with two apps and one user, and the user only logged into one of them. They sign in on the old CodeIgniter or custom PHP side, cross into a Laravel-handled route, and Laravel, knowing nothing about that session, sends them to a login form. Laravel Legacy Bridge, a package from <a href="https://github.com/chr15k">Chris Keller</a>, reads the legacy session cookie on unauthenticated requests, decodes the session payload out of the legacy database, and authenticates the matching user in Laravel.</p>
<p>Here's what the package covers:</p>
<ul>
<li><strong>A middleware bridge</strong> that runs only on unauthenticated requests and stops consulting the legacy store once Laravel has its own session</li>
<li><strong>Payload decoding</strong> for native PHP session encoding, JSON, Laravel's <code>base64(serialize())</code> format, and encrypted payloads</li>
<li><strong>Resolver drivers</strong> to locate the user ID in the payload: auto-detection, an explicit dot-notation key, or a class of your own</li>
<li><strong>Typed events</strong> for successful bridges, known failures, and unexpected exceptions, with no logging of its own</li>
<li><strong>Legacy session invalidation</strong> so a given legacy session can only be bridged once</li>
<li><strong>An interactive install command</strong> with framework presets, plus a <code>verify</code> command to test the wiring before real traffic hits it</li>
<li><strong>Optional context carrying</strong> for values like a locale or cart ID that live in the legacy payload</li>
</ul>
<h2><a id="content-how-the-bridge-works" href="#content-how-the-bridge-works" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>How the Bridge Works</h2>
<p>Registering one middleware puts the bridge in the request path:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">withMiddleware</span><span style="color: #24292E;">(</span><span style="color: #D73A49;">function</span><span style="color: #24292E;"> (</span><span style="color: #005CC5;">Middleware</span><span style="color: #24292E;"> $middleware) {</span></div><div class='line'><span style="color: #24292E;">    $middleware</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">web</span><span style="color: #24292E;">(</span><span style="color: #6F42C1;">append</span><span style="color: #24292E;">: [</span></div><div class='line'><span style="color: #24292E;">        </span><span style="color: #005CC5;">\Chr15k\LegacyBridge\Http\Middleware\LegacySessionBridge</span><span style="color: #D73A49;">::class</span><span style="color: #24292E;">,</span></div><div class='line'><span style="color: #24292E;">    ]);</span></div><div class='line'><span style="color: #24292E;">})</span></div></code></pre>
<p>On an unauthenticated request it reads the legacy cookie (<code>PHPSESSID</code> by default), looks up the row in the legacy sessions table, decodes the payload, resolves a user ID, and calls <code>loginUsingId()</code>. Laravel then writes its own session, and later requests never touch the legacy store. The service provider also excludes the legacy cookie from Laravel's <code>EncryptCookies</code> middleware, so there's no <code>encryptCookies()</code> list to maintain.</p>
<h2><a id="content-resolvers-and-payload-formats" href="#content-resolvers-and-payload-formats" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Resolvers and Payload Formats</h2>
<p>Every legacy app stores the user ID under a different key, so the lookup is configurable. Pick a resolver driver in <code>config/legacy-bridge.php</code>:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #6A737D;">// Auto: tries known patterns (default)</span></div><div class='line'><span style="color: #032F62;">&#39;resolver&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> [</span><span style="color: #032F62;">&#39;driver&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #032F62;">&#39;auto&#39;</span><span style="color: #24292E;">],</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #6A737D;">// Key: explicit dot-notation path</span></div><div class='line'><span style="color: #032F62;">&#39;resolver&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> [</span><span style="color: #032F62;">&#39;driver&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #032F62;">&#39;key&#39;</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;key&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #032F62;">&#39;user_id&#39;</span><span style="color: #24292E;">],</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #6A737D;">// Custom: your own implementation</span></div><div class='line'><span style="color: #032F62;">&#39;resolver&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> [</span><span style="color: #032F62;">&#39;driver&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #032F62;">&#39;custom&#39;</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;class&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">\App\Bridge\LegacyUserResolver</span><span style="color: #D73A49;">::class</span><span style="color: #24292E;">],</span></div></code></pre>
<p>The README recommends starting on <code>auto</code> and switching to <code>key</code> or <code>custom</code> before production. A custom resolver is also where you'd map old user IDs to new ones if your migration re-seeded the users table. Payload format is a separate setting (<code>auto</code>, <code>php_session</code>, <code>json</code>, <code>laravel</code>, or <code>encrypted</code>), and the encrypted format reads the legacy app's key from <code>LEGACY_BRIDGE_APP_KEY</code>.</p>
<h2><a id="content-events" href="#content-events" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Events</h2>
<p>The bridge writes nothing to your log files. It dispatches <code>LegacySessionBridged</code> on success, <code>LegacySessionBridgeFailed</code> for known failures, and <code>LegacySessionBridgeError</code> for unexpected exceptions, and leaves the reporting to your listeners.</p>
<p>Failures carry a <code>BridgeFailureReason</code> enum with eight cases, among them <code>MissingCookie</code>, <code>AmbiguousCookie</code>, <code>SessionExpired</code>, <code>PayloadDecodeFailed</code>, and <code>UserNotResolved</code>. Some point at a misconfiguration, others are ordinary, like a session that timed out. The failure event also carries a <code>BridgeContext</code> DTO holding whatever the bridge resolved before it stopped:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$event</span><span style="color: #D73A49;">-&gt;</span><span style="color: #24292E;">context</span><span style="color: #D73A49;">-&gt;</span><span style="color: #24292E;">cookieName</span></div><div class='line'><span style="color: #24292E;">$event</span><span style="color: #D73A49;">-&gt;</span><span style="color: #24292E;">context</span><span style="color: #D73A49;">-&gt;</span><span style="color: #24292E;">sessionId      </span><span style="color: #6A737D;">// resolved session ID (if reached)</span></div><div class='line'><span style="color: #24292E;">$event</span><span style="color: #D73A49;">-&gt;</span><span style="color: #24292E;">context</span><span style="color: #D73A49;">-&gt;</span><span style="color: #24292E;">payload        </span><span style="color: #6A737D;">// decoded payload (if reached)</span></div><div class='line'><span style="color: #24292E;">$event</span><span style="color: #D73A49;">-&gt;</span><span style="color: #24292E;">context</span><span style="color: #D73A49;">-&gt;</span><span style="color: #24292E;">userId         </span><span style="color: #6A737D;">// resolved user ID (if reached)</span></div><div class='line'><span style="color: #24292E;">$event</span><span style="color: #D73A49;">-&gt;</span><span style="color: #24292E;">context</span><span style="color: #D73A49;">-&gt;</span><span style="color: #24292E;">requestContext </span><span style="color: #6A737D;">// [&#39;ip&#39;, &#39;path&#39;, &#39;method&#39;, &#39;user_agent&#39;]</span></div></code></pre>
<h2><a id="content-installation" href="#content-installation" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Installation</h2>
<pre><code data-theme="github-light" data-lang="bash" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #6F42C1;">composer</span><span style="color: #24292E;"> </span><span style="color: #032F62;">require</span><span style="color: #24292E;"> </span><span style="color: #032F62;">chr15k/laravel-legacy-bridge</span></div><div class='line'><span style="color: #6F42C1;">php</span><span style="color: #24292E;"> </span><span style="color: #032F62;">artisan</span><span style="color: #24292E;"> </span><span style="color: #032F62;">legacy-bridge:install</span></div></code></pre>
<p>The install command is interactive. It includes presets for common legacy frameworks, collects the database credentials, and writes the <code>.env</code> entries for you.</p>
<h2><a id="content-the-verify-command" href="#content-the-verify-command" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>The Verify Command</h2>
<p>A misconfigured bridge fails on real cookies against a real legacy database, which is not what your test suite exercises. The package ships a command that checks the configuration against that database:</p>
<pre><code data-theme="github-light" data-lang="bash" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #6F42C1;">php</span><span style="color: #24292E;"> </span><span style="color: #032F62;">artisan</span><span style="color: #24292E;"> </span><span style="color: #032F62;">legacy-bridge:verify</span></div><div class='line'><span style="color: #6F42C1;">php</span><span style="color: #24292E;"> </span><span style="color: #032F62;">artisan</span><span style="color: #24292E;"> </span><span style="color: #032F62;">legacy-bridge:verify</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">--session-id=a_real_session_id</span></div></code></pre>
<p>Run it bare and it checks that the config is readable, the legacy database is reachable, the sessions table exists and has rows, the resolver is configured, and no cookie names collide. Pass a real session ID and it reports what the bridge would do with that session: format detected, payload keys found, user ID resolved, user confirmed to exist. It authenticates no one and modifies nothing.</p>
<h2><a id="content-limitations-and-security" href="#content-limitations-and-security" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Limitations and Security</h2>
<p>The first release supports database sessions only, not the file, Redis, or Memcached drivers. It bridges web requests, not stateless API requests, and only into the default auth guard. It requires Laravel 13 and PHP 8.3 or newer.</p>
<p>Read the security section of the README before you deploy. The bridge deserializes payloads read straight from the legacy sessions table, which makes that database a trust boundary; the author recommends read-only credentials where possible. The legacy cookie travels unencrypted by design, the same way it did on the old app, so both applications need HTTPS. The default <code>after_write</code> invalidation strategy deletes the legacy session once Laravel writes its own, and the docs advise against setting it to <code>never</code> in production.</p>
<p>The source code and a full user guide covering framework presets, invalidation strategies, and troubleshooting are on <a href="https://github.com/chr15k/laravel-legacy-bridge">GitHub</a>.</p>
            </div>
            <div class="mt-12">
                <div class="flex flex-col items-start space-y-4 sm:flex-row sm:space-x-6 sm:space-y-0"  data-statdive-tags="author-ylynfatt">

    <img
        class="h-20 w-20 rounded-lg object-cover"
        src="https://www.gravatar.com/avatar/d2e1d15c9ca048ffff35a1ba26047471?s=200"
        alt="Yannick Lyn Fatt photo"
    />

    <div>
        <p class="font-display text-2xl font-bold leading-none text-black" itemprop="author">
            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80" href="/@ylynfatt" rel="author"
            wire:navigate.hover
    >
    Yannick Lyn Fatt
</a>
        </p>
        <div
            class="prose prose-sm mt-2 text-gray-600 prose-a:text-red-600 prose-a:transition prose-a:hover:text-red-700"
        >
            <p>Staff Writer at Laravel News and Full stack web developer.</p>

        </div>
        <div class="mt-4 flex gap-2">
            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 inline-flex h-5 w-5 items-center justify-center !rounded-full hover:opacity-80" href="https://x.com/ylynfatt" target="_blank" rel="noopener noreferrer"
    >
    <img
                class="h-4 w-4"
                src="https://picperf.io/https://laravel-news.com/images/x.svg"
                loading="lazy"
                alt="X"
            />
            <span class="sr-only">X</span>
</a>
    

            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 inline-flex h-5 w-5 items-center justify-center !rounded-full hover:opacity-80" href="https://threads.net/ylynfatt" target="_blank" rel="noopener noreferrer"
    >
    <img
                class="h-4 w-4"
                src="https://picperf.io/https://laravel-news.com/images/threads.svg"
                loading="lazy"
                alt="Threads"
            />
            <span class="sr-only">Threads</span>
</a>
    

            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 inline-flex h-5 w-5 items-center justify-center !rounded-full hover:opacity-80" href="https://instagram.com/ylynfatt" target="_blank" rel="noopener noreferrer"
    >
    <img
                class="h-4 w-4"
                src="https://picperf.io/https://laravel-news.com/images/instagram.svg"
                loading="lazy"
                alt="Instagram"
            />
            <span class="sr-only">Instagram</span>
</a>
    

            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 inline-flex h-5 w-5 items-center justify-center !rounded-full hover:opacity-80" href="https://github.com/ylynfatt" target="_blank" rel="noopener noreferrer"
    >
    <img
                class="h-4 w-4"
                src="https://picperf.io/https://laravel-news.com/images/github.svg"
                loading="lazy"
                alt="Github"
            />
            <span class="sr-only">Github</span>
</a>
    

    

    

            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 inline-flex h-5 w-5 items-center justify-center !rounded-full hover:opacity-80" href="https://linkedin.com/in/yannick-l-50123b2" target="_blank" rel="noopener noreferrer"
    >
    <img
                class="h-4 w-4"
                src="https://picperf.io/https://laravel-news.com/images/linkedin.svg"
                loading="lazy"
                alt="LinkedIn"
            />
            <span class="sr-only">LinkedIn</span>
</a>
    
        </div>
    </div>
</div>
            </div>
            <div class="mt-6 flex flex-wrap items-center gap-x-3 gap-y-2" data-statdive-tags="category-packages">
                <span class="text-gray-600">Filed in:</span>
                <div class="flex flex-wrap items-center gap-x-2 gap-y-2">
                    <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 inline-flex !rounded-full px-4 py-2 text-xs font-bold leading-4 hover:opacity-80 focus-visible:ring-offset-1 bg-red-600 text-white" href="/category/packages"
            wire:navigate.hover
    >
    Laravel Packages
</a>
                                    </div>
            </div>
        </div>
    </article>
    <div class="mx-auto max-w-4xl px-6 pb-32 pt-10">
        <div class="relative">
    <img
    delay="1500" class="absolute -top-10 right-16 z-10 lg:-top-6 lg:left-1/3 lg:right-auto"
    x-data="{
        initializeAnimation: false,
        init() {
            setTimeout(() => {
                this.initializeAnimation = true;
            }, 1500);
        },
    }"
    :class="initializeAnimation ? 'animate-cube' : ''"
    src="https://picperf.io/https://laravel-news.com/images/cube.svg"
    alt="Cube"
/>
    <div
        class="relative flex flex-wrap items-center justify-between gap-8 overflow-hidden rounded-lg border border-gray-100 bg-white p-8 shadow-card lg:flex-nowrap"
    >
        <span class="absolute inset-y-0 left-0 w-1 bg-red-600"></span>
        <div>
            <h2 class="text-2xl font-bold sm:text-3xl">Laravel Newsletter</h2>
            <p class="mt-1 text-gray-600">
                Join 40k+ other developers and never miss out on new tips, tutorials, and more.
            </p>
        </div>
        <div class="lg:shrink-0">
            <div id="newsletter-signup-article">
        <form x-target="newsletter-signup-article" method="POST" action="https://laravel-news.com/newsletter-signup">
        <input type="hidden" name="location" value="article">
        <div class="flex w-full flex-wrap items-stretch gap-4">
            <label class="relative flex min-w-[240px] flex-1 items-center bg-white">
                <span class="sr-only">Email</span>
                <img
                    src="https://picperf.io/https://laravel-news.com/images/icons/newsletter.svg"
                    alt="Newsletter icon"
                    class="pointer-events-none absolute left-3 top-3"
                />
                <input
                    name="email"
                    type="email"
                    class="w-full rounded-lg border-gray-100 bg-transparent px-12 py-3 text-gray-600 placeholder-gray-600/50 transition focus:border-gray-100 focus:bg-gray-100/40 focus:outline-none focus:ring-2 focus:ring-red-600/80 focus:ring-offset-2"
                    placeholder="Email"
                />
            </label>
            <button
    type="submit" class="inline-flex items-center justify-center leading-none bg-red-600 border border-transparent rounded-lg font-bold text-base text-white hover:bg-red-700 focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 focus-visible:ring-offset-2 disabled:bg-red-600/50 disabled:cursor-not-allowed transition ease-in-out duration-300 px-6 py-4"
>
    Join free
</button>
        </div>
            </form>
    </div>
        </div>
    </div>
</div>
        <div class="mt-10">
            <div class="relative flex justify-between rounded-lg bg-white border border-gray-100 shadow-card">
    <img
    delay="0" class="absolute left-0 top-3 -translate-x-1/2"
    x-data="{
        initializeAnimation: false,
        init() {
            setTimeout(() => {
                this.initializeAnimation = true;
            }, 0);
        },
    }"
    :class="initializeAnimation ? 'animate-cube' : ''"
    src="https://picperf.io/https://laravel-news.com/images/cube.svg"
    alt="Cube"
/>
    <div class="px-8 py-12 lg:p-12">
        <h2 class="text-3xl font-bold">Laravel Jobs</h2>
        <p class="mt-2 text-gray-600">Explore hundreds of open positions today.</p>
        <a href="https://larajobs.com" class="mt-6 inline-flex items-center px-6 py-4 leading-none bg-black border border-transparent rounded-lg font-bold text-base text-white hover:bg-gray-600 focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 focus-visible:ring-offset-2 transition ease-in-out duration-300">
            View all jobs
        </a>
    </div>
    <div class="hidden flex-col gap-1 overflow-hidden py-2 sm:flex relative">
                <div
            class="w-56 translate-x-6 rounded-lg border border-gray-100 px-4 py-3 text-xs font-bold shadow-sm truncate"
        >
            <a href="https://larajobs.com/job/3896?ref=laravelnews&utm_source=laravelnews&utm_medium=referral">
                Senior Fullstack Engineer
            </a>
        </div>
                <div
            class="w-56 translate-x-6 rounded-lg border border-gray-100 px-4 py-3 text-xs font-bold shadow-sm truncate"
        >
            <a href="https://larajobs.com/job/3899?ref=laravelnews&utm_source=laravelnews&utm_medium=referral">
                Laravel &amp; Wordpress Web Developer
            </a>
        </div>
                <div
            class="w-56 translate-x-6 rounded-lg border border-gray-100 px-4 py-3 text-xs font-bold shadow-sm truncate"
        >
            <a href="https://larajobs.com/job/3901?ref=laravelnews&utm_source=laravelnews&utm_medium=referral">
                Forwardly Deployed Engineer
            </a>
        </div>
                <div
            class="w-56 translate-x-6 rounded-lg border border-gray-100 px-4 py-3 text-xs font-bold shadow-sm truncate"
        >
            <a href="https://larajobs.com/job/3902?ref=laravelnews&utm_source=laravelnews&utm_medium=referral">
                Senior Full-Stack Laravel Developer
            </a>
        </div>
                <div
            class="w-56 translate-x-6 rounded-lg border border-gray-100 px-4 py-3 text-xs font-bold shadow-sm truncate"
        >
            <a href="https://larajobs.com/job/3903?ref=laravelnews&utm_source=laravelnews&utm_medium=referral">
                Senior Native IOS &amp; Laravel Developer
            </a>
        </div>
            </div>
</div>
        </div>
        <div id="iconBarJs"></div>
        <div>
            <div
            class="relative mt-4 max-w-full rounded-lg border border-gray-100 bg-[#f7f8fb] p-5 xl:z-50 xl:fixed xl:bottom-6 xl:right-6"
        >
            <div
                class="group relative max-h-[150px] md:max-h-full xl:max-w-[160px]"
            >
                <div class="flex items-center text-sm text-gray-600 xl:block xl:text-xs">
                    <div class="mr-4 xl:mr-0">
                        <img
                            src="https://picperf.io/https://laravelnews.s3.amazonaws.com/images/01KJ5XMS7AG6WN0HYNZXMHPVD3.png"
                            alt="image"
                            height="100"
                            width="230"
                            loading="lazy"
                        />
                    </div>
                    <div class="pt-2 text-sm">
                        <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 font-bold text-[##565454]" href="https://serpapi.com/?utm_source=laravelnews"
    >
    SerpApi
</a>
                        <p class="mt-1 text-sm xl:text-xs">
                            The Web Search API for Your LLM and AI Applications
                        </p>
                    </div>
                </div>
                <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 absolute inset-0 !block h-full w-full !rounded-lg" href="https://serpapi.com/?utm_source=laravelnews" onclick="fathom.trackEvent('serpapi|article|click', {_value: 100});"
    >
    <span class="sr-only">Visit SerpApi</span>
</a>
                <script>
                    window.addEventListener('load', (event) => {
                        if (typeof fathom !== 'undefined' && fathom.trackEvent) {
                            fathom.trackEvent('serpapi|article|show');
                        }
                    });
                </script>
            </div>
        </div>
    </div>