---
source_url: https://laravel-news.com/build-a-laravel-scout-search-endpoint-with-the-http-query-method?utm_medium=feed&utm_source=feedpress.me&utm_campaign=Feed%3A+laravelnews
ingested: 2026-07-17
sha256: 7c722a6135373b179f7165c5ce895d2dd75201bb4c494001730700b0346e51e2
blog_source: Laravel News
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <meta name="csrf-token" content=""/>

    <title>Build a Laravel Scout Search Endpoint With the HTTP QUERY Method - Laravel News</title>
    
    
    <meta
        name="description"
        content="Learn how to define a Laravel route that responds to the new HTTP QUERY method and use Laravel Scout&#039;s database driver to build a search API endpoint."
    />
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="Build a Laravel Scout Search Endpoint With the HTTP QUERY Method - Laravel News"/>
    <meta
        property="og:description"
        content="Learn how to define a Laravel route that responds to the new HTTP QUERY method and use Laravel Scout&#039;s database driver to build a search API endpoint."
    />
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="Build a Laravel Scout Search Endpoint With the HTTP QUERY Method - Laravel News"/>
    <meta
        property="og:image"
        content="https://laravelnews.s3.amazonaws.com/featured-images/laravel-query-routes.png"
    />
    <meta
        property="og:description"
        content="Learn how to define a Laravel route that responds to the new HTTP QUERY method and use Laravel Scout&#039;s database driver to build a search API endpoint."
    />
    <meta property="og:url" content="https://laravel-news.com/build-a-laravel-scout-search-endpoint-with-the-http-query-method"/>
    <meta property="og:site_name" content="Laravel News"/>
    <meta property="og:locale" content="en_US"/>

    
    <meta name="twitter:card" content="summary_large_image"/>
    <meta name="twitter:site" content="@laravelnews"/>
    <meta name="twitter:title" content="Build a Laravel Scout Search Endpoint With the HTTP QUERY Method - Laravel News"/>
    <meta
        property="twitter:image"
        content="https://laravelnews.s3.amazonaws.com/featured-images/laravel-query-routes.png"
    />
    <meta
        name="twitter:description"
        content="Learn how to define a Laravel route that responds to the new HTTP QUERY method and use Laravel Scout&#039;s database driver to build a search API endpoint."
    />
            <meta name="twitter:creator" content="@paulredmond"/>
    
    <link href="https://laravel-news.com/build-a-laravel-scout-search-endpoint-with-the-http-query-method" rel="canonical"/>
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
            href="https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/laravel-query-routes.png"
        />
    
    <script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "NewsArticle",
    "headline": "Build a Laravel Scout Search Endpoint With the HTTP QUERY Method",
    "datePublished": "2026-07-16T09:15:00-04:00",
    "description": "Learn how to define a Laravel route that responds to the new HTTP QUERY method and use Laravel Scout's database driver to build a search API endpoint.",
    "image": "https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/laravel-query-routes.png",
    "dateModified": "2026-07-15T22:54:49-04:00",
    "author": {
        "@type": "Person",
        "name": "Paul Redmond",
        "url": "https://laravel-news.com/@paulredmond"
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
        "@id": "https://laravel-news.com/build-a-laravel-scout-search-endpoint-with-the-http-query-method"
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
            "name": "News",
            "item": "https://laravel-news.com/category/news"
        },
        {
            "@type": "ListItem",
            "position": 3,
            "name": "Build a Laravel Scout Search Endpoint With the HTTP QUERY Method"
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
                <h1 class="text-4xl font-bold sm:text-5xl md:text-6xl">Build a Laravel Scout Search Endpoint With the HTTP QUERY Method</h1>

                <div class="mt-6 flex items-center gap-3">

                    <p class="text-xs text-gray-600">
                                                    Last updated on
                            <time
                                itemprop="dateModified"
                                datetime="2026-07-15T22:54:49"
                            >
                                July 15th, 2026
                            </time>
                                                by
                        <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 hover:text-red-600" href="/@paulredmond" rel="author"
            wire:navigate.hover
    >
    Paul Redmond
</a>

                    </p>
                </div>
                                    <img
                        src="https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/laravel-query-routes.png"
                        alt="Build a Laravel Scout Search Endpoint With the HTTP QUERY Method image"
                        class="mt-12 aspect-[2/1] w-full overflow-hidden rounded-xl object-cover shadow-card"
                    />
                            </div>
        </div>
        <div class="mx-auto w-full max-w-4xl px-6 py-20">


            
            <div
                class="prose max-w-4xl break-words prose-a:text-red-600 prose-a:transition prose-a:hover:text-red-700 prose-pre:rounded-lg prose-pre:bg-gray-100/50 prose-pre:p-6 prose-img:mx-auto prose-img:rounded-lg prose-img:border prose-img:border-gray-100"
            >
                <p>The HTTP QUERY method is a new addition to the HTTP spec (<a href="https://www.rfc-editor.org/rfc/rfc10008">RFC 10008</a>) designed for exactly one thing: queries. It is a safe, cacheable method that carries its parameters in the request body, giving you the expressiveness of a POST payload without giving up the read-only semantics of GET—and without cramming complex filters into a URL that may hit length limits along the way.</p>
<p>Laravel 13.19 added <a href="https://laravel-news.com/laravel-13-19-0"><code>Http::query()</code> to the HTTP client</a> along with <code>query()</code> and <code>queryJson()</code> testing helpers. A first-class <code>Route::query()</code> helper <a href="https://github.com/laravel/framework/pull/60655">has been merged for Laravel 14</a>, but you don't have to wait: Laravel's router already accepts custom verbs today via <code>Route::match()</code>. In this tutorial, we'll use it to build a small search endpoint backed by Laravel Scout's database driver.</p>
<p>A single search string like ours doesn't strictly need QUERY—the method starts paying for itself as the request grows into something GET can't carry comfortably:</p>
<ul>
<li>Structured filters with ranges, arrays, and and/or groups (product or listing search)</li>
<li>Geospatial queries that send polygon coordinates (&quot;search within this map area&quot;)</li>
<li>Batch lookups that fetch hundreds of records by ID</li>
<li>Searches on sensitive values like emails or phone numbers, which don't belong in URLs, access logs, or browser history</li>
<li>Reporting endpoints with date ranges and group-bys that are reads but get modeled as <code>POST /reports/run</code> today</li>
</ul>
<h2><a id="content-setting-up" href="#content-setting-up" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Setting Up</h2>
<p>Starting from a fresh Laravel 13 application, install the API routes file and Scout:</p>
<pre><code data-theme="github-light" data-lang="shell" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #6F42C1;">php</span><span style="color: #24292E;"> </span><span style="color: #032F62;">artisan</span><span style="color: #24292E;"> </span><span style="color: #032F62;">install:api</span></div><div class='line'><span style="color: #6F42C1;">composer</span><span style="color: #24292E;"> </span><span style="color: #032F62;">require</span><span style="color: #24292E;"> </span><span style="color: #032F62;">laravel/scout</span></div></code></pre>
<p>Scout's database driver needs no external search service—it uses <code>WHERE LIKE</code> queries against your existing database, which is a good fit for small-to-medium datasets. Enable it in your <code>.env</code> file:</p>
<pre><code data-theme="github-light" data-lang="ini" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">SCOUT_DRIVER</span><span style="color: #24292E;">=database</span></div></code></pre>
<p>Next, create an <code>Article</code> model with a migration and factory:</p>
<pre><code data-theme="github-light" data-lang="shell" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #6F42C1;">php</span><span style="color: #24292E;"> </span><span style="color: #032F62;">artisan</span><span style="color: #24292E;"> </span><span style="color: #032F62;">make:model</span><span style="color: #24292E;"> </span><span style="color: #032F62;">Article</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">-mf</span></div></code></pre>
<p>The migration defines a <code>title</code> and <code>body</code>:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #005CC5;">Schema</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">create</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;articles&#39;</span><span style="color: #24292E;">, </span><span style="color: #D73A49;">function</span><span style="color: #24292E;"> (</span><span style="color: #005CC5;">Blueprint</span><span style="color: #24292E;"> $table) {</span></div><div class='line'><span style="color: #24292E;">    $table</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">id</span><span style="color: #24292E;">();</span></div><div class='line'><span style="color: #24292E;">    $table</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">string</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;title&#39;</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">    $table</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">text</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;body&#39;</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">    $table</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">timestamps</span><span style="color: #24292E;">();</span></div><div class='line'><span style="color: #24292E;">});</span></div></code></pre>
<p>Add the <code>Searchable</code> trait to the model and define which columns Scout should search:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">namespace</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">App\Models</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Illuminate\Database\Eloquent\Factories\HasFactory</span><span style="color: #24292E;">;</span></div><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Illuminate\Database\Eloquent\Model</span><span style="color: #24292E;">;</span></div><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Laravel\Scout\Searchable</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #D73A49;">class</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">Article</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">extends</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">Model</span></div><div class='line'><span style="color: #24292E;">{</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">HasFactory</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">Searchable</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">protected</span><span style="color: #24292E;"> $fillable </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> [</span><span style="color: #032F62;">&#39;title&#39;</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;body&#39;</span><span style="color: #24292E;">];</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">public</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">function</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">toSearchableArray</span><span style="color: #24292E;">()</span><span style="color: #D73A49;">:</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">array</span></div><div class='line'><span style="color: #24292E;">    {</span></div><div class='line'><span style="color: #24292E;">        </span><span style="color: #D73A49;">return</span><span style="color: #24292E;"> [</span></div><div class='line'><span style="color: #24292E;">            </span><span style="color: #032F62;">&#39;title&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">$this</span><span style="color: #D73A49;">-&gt;</span><span style="color: #24292E;">title,</span></div><div class='line'><span style="color: #24292E;">            </span><span style="color: #032F62;">&#39;body&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">$this</span><span style="color: #D73A49;">-&gt;</span><span style="color: #24292E;">body,</span></div><div class='line'><span style="color: #24292E;">        ];</span></div><div class='line'><span style="color: #24292E;">    }</span></div><div class='line'><span style="color: #24292E;">}</span></div></code></pre>
<h2><a id="content-defining-a-query-route" href="#content-defining-a-query-route" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Defining a QUERY Route</h2>
<p>Laravel's router doesn't support <code>Route::query()</code> in Laravel 13 (it will be available starting in Laravel 14). However, Laravel's router registers routes for any verb you pass to <code>Route::match()</code>, including QUERY.</p>
<p>Add the following to <code>routes/api.php</code>:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">App\Models\Article</span><span style="color: #24292E;">;</span></div><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Illuminate\Http\Request</span><span style="color: #24292E;">;</span></div><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Illuminate\Support\Facades\Route</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #005CC5;">Route</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">match</span><span style="color: #24292E;">([</span><span style="color: #032F62;">&#39;QUERY&#39;</span><span style="color: #24292E;">], </span><span style="color: #032F62;">&#39;/articles/search&#39;</span><span style="color: #24292E;">, </span><span style="color: #D73A49;">function</span><span style="color: #24292E;"> (</span><span style="color: #005CC5;">Request</span><span style="color: #24292E;"> $request) {</span></div><div class='line'><span style="color: #24292E;">    $validated </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> $request</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">validate</span><span style="color: #24292E;">([</span></div><div class='line'><span style="color: #24292E;">        </span><span style="color: #032F62;">&#39;search&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> [</span><span style="color: #032F62;">&#39;required&#39;</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;string&#39;</span><span style="color: #24292E;">],</span></div><div class='line'><span style="color: #24292E;">        </span><span style="color: #032F62;">&#39;per_page&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> [</span><span style="color: #032F62;">&#39;sometimes&#39;</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;integer&#39;</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;between:1,50&#39;</span><span style="color: #24292E;">],</span></div><div class='line'><span style="color: #24292E;">    ]);</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">return</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Article</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">search</span><span style="color: #24292E;">($validated[</span><span style="color: #032F62;">&#39;search&#39;</span><span style="color: #24292E;">])</span></div><div class='line'><span style="color: #24292E;">        </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">paginate</span><span style="color: #24292E;">($validated[</span><span style="color: #032F62;">&#39;per_page&#39;</span><span style="color: #24292E;">] </span><span style="color: #D73A49;">??</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">15</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">});</span></div></code></pre>
<p>Note that validation and <code>$request-&gt;input()</code> read from the JSON request body just like they would for a POST request—no extra work required. Running <code>php artisan route:list</code> confirms the route is registered with the QUERY verb:</p>
<pre><code data-theme="github-light" data-lang="text" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292e;">QUERY  api/articles/search</span></div></code></pre>
<p>A request to this endpoint looks like a POST with GET semantics—the search criteria travel in the body:</p>
<pre><code data-theme="github-light" data-lang="http" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292e;">QUERY /api/articles/search HTTP/1.1</span></div><div class='line'><span style="color: #24292e;">Content-Type: application/json</span></div><div class='line'><span style="color: #24292e;">Accept: application/json</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292e;">{&quot;search&quot;: &quot;scout&quot;, &quot;per_page&quot;: 10}</span></div></code></pre>
<h2><a id="content-testing-the-endpoint" href="#content-testing-the-endpoint" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Testing the Endpoint</h2>
<p>Laravel 13.19's <code>queryJson()</code> testing helper mirrors <code>postJson()</code> and friends, so exercising the endpoint feels familiar:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">namespace</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">Tests\Feature</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">App\Models\Article</span><span style="color: #24292E;">;</span></div><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Illuminate\Foundation\Testing\RefreshDatabase</span><span style="color: #24292E;">;</span></div><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Tests\TestCase</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #D73A49;">class</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">ArticleSearchTest</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">extends</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">TestCase</span></div><div class='line'><span style="color: #24292E;">{</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">RefreshDatabase</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">public</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">function</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">test_it_searches_articles_with_the_query_method</span><span style="color: #24292E;">()</span><span style="color: #D73A49;">:</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">void</span></div><div class='line'><span style="color: #24292E;">    {</span></div><div class='line'><span style="color: #24292E;">        </span><span style="color: #005CC5;">Article</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">factory</span><span style="color: #24292E;">()</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">create</span><span style="color: #24292E;">([</span><span style="color: #032F62;">&#39;title&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #032F62;">&#39;Getting Started With Laravel Scout&#39;</span><span style="color: #24292E;">]);</span></div><div class='line'><span style="color: #24292E;">        </span><span style="color: #005CC5;">Article</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">factory</span><span style="color: #24292E;">()</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">create</span><span style="color: #24292E;">([</span><span style="color: #032F62;">&#39;title&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #032F62;">&#39;Queues in Depth&#39;</span><span style="color: #24292E;">]);</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">        </span><span style="color: #005CC5;">$this</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">queryJson</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;/api/articles/search&#39;</span><span style="color: #24292E;">, [</span><span style="color: #032F62;">&#39;search&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #032F62;">&#39;scout&#39;</span><span style="color: #24292E;">])</span></div><div class='line'><span style="color: #24292E;">            </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">assertOk</span><span style="color: #24292E;">()</span></div><div class='line'><span style="color: #24292E;">            </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">assertJsonCount</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">1</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;data&#39;</span><span style="color: #24292E;">)</span></div><div class='line'><span style="color: #24292E;">            </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">assertJsonPath</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;data.0.title&#39;</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;Getting Started With Laravel Scout&#39;</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">    }</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">public</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">function</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">test_it_validates_the_search_term</span><span style="color: #24292E;">()</span><span style="color: #D73A49;">:</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">void</span></div><div class='line'><span style="color: #24292E;">    {</span></div><div class='line'><span style="color: #24292E;">        </span><span style="color: #005CC5;">$this</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">queryJson</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;/api/articles/search&#39;</span><span style="color: #24292E;">, [])</span></div><div class='line'><span style="color: #24292E;">            </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">assertUnprocessable</span><span style="color: #24292E;">()</span></div><div class='line'><span style="color: #24292E;">            </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">assertJsonValidationErrors</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;search&#39;</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">    }</span></div><div class='line'><span style="color: #24292E;">}</span></div></code></pre>
<p>On the consuming side, Laravel's HTTP client can call QUERY endpoints with the <code>Http::query()</code> method added in 13.19:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Illuminate\Support\Facades\Http</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">$response </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Http</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">acceptJson</span><span style="color: #24292E;">()</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">query</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;https://example.com/api/articles/search&#39;</span><span style="color: #24292E;">, [</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #032F62;">&#39;search&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #032F62;">&#39;scout&#39;</span><span style="color: #24292E;">,</span></div><div class='line'><span style="color: #24292E;">]);</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">$articles </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> $response</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">json</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;data&#39;</span><span style="color: #24292E;">);</span></div></code></pre>
<h2><a id="content-a-gotcha-phps-built-in-server" href="#content-a-gotcha-phps-built-in-server" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>A Gotcha: PHP's Built-in Server</h2>
<p>If you develop with <code>php artisan serve</code>, requests using the QUERY method get a <code>501 Not Implemented</code> response before they ever reach Laravel—the built-in server hard-codes the request methods it accepts. Nginx-based environments like Laravel Herd and Valet pass the method through to your application. Laravel's HTTP testing helpers avoid the issue entirely since they dispatch requests through the framework directly.</p>
<h2><a id="content-using-query-on-web-routes" href="#content-using-query-on-web-routes" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Using QUERY on Web Routes</h2>
<p>Our endpoint lives in <code>routes/api.php</code>, so CSRF protection never enters the picture. If you register a QUERY route in <code>routes/web.php</code>, however, you'll hit a <code>419</code> error: Laravel 13's <code>PreventRequestForgery</code> middleware only treats <code>GET</code>, <code>HEAD</code>, and <code>OPTIONS</code> as read requests, so QUERY gets the same token check as POST. RFC 10008 defines QUERY as a safe method, and <a href="https://github.com/laravel/framework/pull/60655">Laravel's next major release exempts it accordingly</a>—but until then, you have two options.</p>
<p>The first option backports the upcoming behavior by extending the middleware and adding QUERY to its list of read verbs:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">namespace</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">App\Http\Middleware</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span>