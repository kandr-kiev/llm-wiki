---
source_url: https://laravel-news.com/laravel-13-21-0?utm_medium=feed&utm_source=feedpress.me&utm_campaign=Feed%3A+laravelnews
ingested: 2026-07-22
sha256: 4ca40d441f4c9fd2808af69d4ed1211007b37e9d83b49c8f85d00f6ecb43926d
blog_source: Laravel News
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <meta name="csrf-token" content=""/>

    <title>RouteKey Model Attribute in Laravel 13.21 - Laravel News</title>
    
    
    <meta
        name="description"
        content="Laravel 13.21 adds a #[RouteKey] attribute for Eloquent route model binding, a base64 validation rule, a RequestAttribute contextual attribute, and new output formats for the Image component."
    />
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="RouteKey Model Attribute in Laravel 13.21 - Laravel News"/>
    <meta
        property="og:description"
        content="Laravel 13.21 adds a #[RouteKey] attribute for Eloquent route model binding, a base64 validation rule, a RequestAttribute contextual attribute, and new output formats for the Image component."
    />
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="RouteKey Model Attribute in Laravel 13.21 - Laravel News"/>
    <meta
        property="og:image"
        content="https://laravelnews.s3.amazonaws.com/featured-images/laravel-13-featured.png"
    />
    <meta
        property="og:description"
        content="Laravel 13.21 adds a #[RouteKey] attribute for Eloquent route model binding, a base64 validation rule, a RequestAttribute contextual attribute, and new output formats for the Image component."
    />
    <meta property="og:url" content="https://laravel-news.com/laravel-13-21-0"/>
    <meta property="og:site_name" content="Laravel News"/>
    <meta property="og:locale" content="en_US"/>

    
    <meta name="twitter:card" content="summary_large_image"/>
    <meta name="twitter:site" content="@laravelnews"/>
    <meta name="twitter:title" content="RouteKey Model Attribute in Laravel 13.21 - Laravel News"/>
    <meta
        property="twitter:image"
        content="https://laravelnews.s3.amazonaws.com/featured-images/laravel-13-featured.png"
    />
    <meta
        name="twitter:description"
        content="Laravel 13.21 adds a #[RouteKey] attribute for Eloquent route model binding, a base64 validation rule, a RequestAttribute contextual attribute, and new output formats for the Image component."
    />
            <meta name="twitter:creator" content="@paulredmond"/>
    
    <link href="https://laravel-news.com/laravel-13-21-0" rel="canonical"/>
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
            href="https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/laravel-13-featured.png"
        />
    
    <script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "NewsArticle",
    "headline": "RouteKey Model Attribute in Laravel 13.21",
    "datePublished": "2026-07-22T09:00:00-04:00",
    "description": "Laravel 13.21 adds a #[RouteKey] attribute for Eloquent route model binding, a base64 validation rule, a RequestAttribute contextual attribute, and new output formats for the Image component.",
    "image": "https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/laravel-13-featured.png",
    "dateModified": "2026-07-21T20:08:43-04:00",
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
        "@id": "https://laravel-news.com/laravel-13-21-0"
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
            "name": "RouteKey Model Attribute in Laravel 13.21"
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
                <h1 class="text-4xl font-bold sm:text-5xl md:text-6xl">RouteKey Model Attribute in Laravel 13.21</h1>

                <div class="mt-6 flex items-center gap-3">

                    <p class="text-xs text-gray-600">
                                                    Last updated on
                            <time
                                itemprop="dateModified"
                                datetime="2026-07-21T20:08:43"
                            >
                                July 21st, 2026
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
                        src="https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/laravel-13-featured.png"
                        alt="RouteKey Model Attribute in Laravel 13.21 image"
                        class="mt-12 aspect-[2/1] w-full overflow-hidden rounded-xl object-cover shadow-card"
                    />
                            </div>
        </div>
        <div class="mx-auto w-full max-w-4xl px-6 py-20">


            
            <div
                class="prose max-w-4xl break-words prose-a:text-red-600 prose-a:transition prose-a:hover:text-red-700 prose-pre:rounded-lg prose-pre:bg-gray-100/50 prose-pre:p-6 prose-img:mx-auto prose-img:rounded-lg prose-img:border prose-img:border-gray-100"
            >
                <p>Laravel 13.21 adds a <code>#[RouteKey]</code> class attribute for customizing route model binding on Eloquent models, a <code>base64</code> validation rule, a <code>#[RequestAttribute]</code> contextual attribute for injecting request attributes, and PNG, GIF, AVIF, and BMP output support in the Image component. The Laravel team tagged v13.21.0 and v13.21.1 on July 21, 2026; the patch tag only bumps the framework's version constant, so the two are covered together here.</p>
<ul>
<li><code>#[RouteKey]</code> attribute for Eloquent route model binding</li>
<li>New <code>base64</code> validation rule</li>
<li><code>#[RequestAttribute]</code> contextual attribute</li>
<li>PNG, GIF, AVIF, and BMP output formats for the Image component</li>
<li>Customizable application builder and an <code>illuminate/concurrency</code> subsplit</li>
</ul>
<h2><a id="content-whats-new" href="#content-whats-new" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>What's New</h2>
<h3><a id="content-routekey-attribute-for-eloquent-models" href="#content-routekey-attribute-for-eloquent-models" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a><code>#[RouteKey]</code> Attribute for Eloquent Models</h3>
<p>Customizing the column used for route model binding has always meant overriding <code>getRouteKeyName()</code> on the model. Following the pattern set by <code>#[ObservedBy]</code> and <code>#[ScopedBy]</code>, models can now declare the route key with a class attribute instead:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Illuminate\Database\Eloquent\Attributes\RouteKey</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">#[</span><span style="color: #005CC5;">RouteKey</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;slug&#39;</span><span style="color: #24292E;">)]</span></div><div class='line'><span style="color: #D73A49;">class</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">Post</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">extends</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">Model</span></div><div class='line'><span style="color: #24292E;">{</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #6A737D;">// ...</span></div><div class='line'><span style="color: #24292E;">}</span></div></code></pre>
<p>With the attribute in place, implicit route model binding resolves <code>Post</code> by its <code>slug</code> column, and <code>getRouteKeyName()</code> falls back to the primary key when no attribute is present. Contributed by <a href="https://github.com/nimnaherath">@nimnaherath</a> in <a href="https://github.com/laravel/framework/pull/60841">#60841</a>.</p>
<h3><a id="content-base64-validation-rule" href="#content-base64-validation-rule" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a><code>base64</code> Validation Rule</h3>
<p>A <code>base64</code> rule joins the validator's string format checks, filling a gap that libraries like Zod already cover. The rule verifies that a value is a valid RFC 4648 Base64 string:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$request</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">validate</span><span style="color: #24292E;">([</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #032F62;">&#39;signature&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> [</span><span style="color: #032F62;">&#39;required&#39;</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;base64&#39;</span><span style="color: #24292E;">],</span></div><div class='line'><span style="color: #24292E;">]);</span></div></code></pre>
<p>The check requires a canonical encoding: the value must decode in strict mode and re-encode to the exact same string, so padding mistakes and stray characters fail validation. Contributed by <a href="https://github.com/lucasmichot">@lucasmichot</a> in <a href="https://github.com/laravel/framework/pull/60808">#60808</a>.</p>
<h3><a id="content-requestattribute-contextual-attribute" href="#content-requestattribute-contextual-attribute" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a><code>#[RequestAttribute]</code> Contextual Attribute</h3>
<p>Middleware often stashes resolved objects on the request's attribute bag, a tenant or organization resolved from an API key, for example. Pulling those back out means calling <code>$request-&gt;attributes-&gt;get()</code> and type-hinting by hand. The new <code>#[RequestAttribute]</code> contextual attribute injects the value directly into a resolved parameter:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Illuminate\Container\Attributes\RequestAttribute</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #D73A49;">class</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">InventoryController</span></div><div class='line'><span style="color: #24292E;">{</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">public</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">function</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">index</span><span style="color: #24292E;">(#[</span><span style="color: #005CC5;">RequestAttribute</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;org&#39;</span><span style="color: #24292E;">)] </span><span style="color: #005CC5;">Organization</span><span style="color: #24292E;"> $org)</span></div><div class='line'><span style="color: #24292E;">    {</span></div><div class='line'><span style="color: #24292E;">        </span><span style="color: #D73A49;">return</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">$this</span><span style="color: #D73A49;">-&gt;</span><span style="color: #24292E;">inventoryService</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">getForOrg</span><span style="color: #24292E;">($org);</span></div><div class='line'><span style="color: #24292E;">    }</span></div><div class='line'><span style="color: #24292E;">}</span></div></code></pre>
<p>Contributed by <a href="https://github.com/cosmastech">@cosmastech</a> in <a href="https://github.com/laravel/framework/pull/60847">#60847</a>.</p>
<h3><a id="content-more-output-formats-for-the-image-component" href="#content-more-output-formats-for-the-image-component" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>More Output Formats for the Image Component</h3>
<p>The Image component introduced in <a href="https://laravel-news.com/laravel-13-20-0">Laravel 13.20</a> could only convert to WebP, JPG, and JPEG through its fluent methods, even though the bundled Intervention Image encoders support more. This release adds <code>toPng()</code>, <code>toGif()</code>, <code>toAvif()</code>, and <code>toBmp()</code>:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Illuminate\Support\Facades\Image</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #005CC5;">Image</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">fromUpload</span><span style="color: #24292E;">($request</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">file</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;avatar&#39;</span><span style="color: #24292E;">))</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">cover</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">400</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">400</span><span style="color: #24292E;">)</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">toAvif</span><span style="color: #24292E;">()</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">quality</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">80</span><span style="color: #24292E;">)</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">store</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;avatars&#39;</span><span style="color: #24292E;">);</span></div></code></pre>
<p>The change also fixes <code>Image::extension()</code>, which was missing the <code>image/avif</code> MIME mapping and would have produced a <code>.bin</code> extension for stored AVIF output. Contributed by <a href="https://github.com/Tresor-Kasenda">@Tresor-Kasenda</a> in <a href="https://github.com/laravel/framework/pull/60713">#60713</a>.</p>
<h3><a id="content-customizable-application-builder" href="#content-customizable-application-builder" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Customizable Application Builder</h3>
<p><code>Application::configure()</code> previously hardcoded the <code>ApplicationBuilder</code> class, so packages extending Laravel's <code>Application</code> had to override the whole method to swap it out. A protected static <code>$applicationBuilder</code> property now lets subclasses provide their own builder class while keeping the existing API. See <a href="https://github.com/laravel/framework/pull/60848">#60848</a>.</p>
<h3><a id="content-concurrency-subsplit" href="#content-concurrency-subsplit" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Concurrency Subsplit</h3>
<p>The <code>Illuminate\Concurrency</code> component now has its own read-only subsplit, joining the other Illuminate components published as standalone packages. See <a href="https://github.com/laravel/framework/pull/60836">#60836</a>.</p>
<h3><a id="content-other-fixes-and-improvements" href="#content-other-fixes-and-improvements" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Other Fixes and Improvements</h3>
<ul>
<li>Database transaction rollback callbacks now fire correctly (<a href="https://github.com/laravel/framework/pull/60777">#60777</a>), and a new lost connection message is detected for automatic reconnects (<a href="https://github.com/laravel/framework/pull/60819">#60819</a>)</li>
<li>Question marks are escaped in <code>Grammar::whereColumn()</code> (<a href="https://github.com/laravel/framework/pull/60832">#60832</a>)</li>
<li><code>InvalidPayloadException</code> messages now include the job name and queue (<a href="https://github.com/laravel/framework/pull/60799">#60799</a>)</li>
<li>Passing an enum to <code>LogManager::forgetChannel()</code> no longer throws a <code>TypeError</code> (<a href="https://github.com/laravel/framework/pull/60801">#60801</a>), and <code>RedisTaggedCache::decrement()</code> handles enum keys (<a href="https://github.com/laravel/framework/pull/60821">#60821</a>)</li>
<li><code>Str::wordWrap()</code> handles multibyte strings correctly (<a href="https://github.com/laravel/framework/pull/60814">#60814</a>)</li>
<li>Contextual attribute caching no longer collides across properties of the same class (<a href="https://github.com/laravel/framework/pull/60815">#60815</a>), and falsey concurrency exception parameters are preserved (<a href="https://github.com/laravel/framework/pull/60822">#60822</a>)</li>
<li>Fixed host port parsing in the <code>serve</code> command (<a href="https://github.com/laravel/framework/pull/60828">#60828</a>) and an undefined index in <code>Pipeline\Hub::pipe()</code> (<a href="https://github.com/laravel/framework/pull/60802">#60802</a>)</li>
</ul>
<p><strong>References</strong></p>
<ul>
<li><a href="https://github.com/laravel/framework/blob/13.x/CHANGELOG.md">Official changelog</a></li>
<li><a href="https://github.com/laravel/framework/compare/v13.20.0...v13.21.0">Compare v13.20.0...v13.21.0</a></li>
<li><a href="https://github.com/laravel/framework/compare/v13.21.0...v13.21.1">Compare v13.21.0...v13.21.1</a></li>
<li>PR: <a href="https://github.com/laravel/framework/pull/60841">#60841</a> (<code>#[RouteKey]</code> attribute)</li>
<li>PR: <a href="https://github.com/laravel/framework/pull/60808">#60808</a> (<code>base64</code> validation rule)</li>
<li>PR: <a href="https://github.com/laravel/framework/pull/60847">#60847</a> (<code>#[RequestAttribute]</code> contextual attribute)</li>
<li>PR: <a href="https://github.com/laravel/framework/pull/60713">#60713</a> (Image component output formats)</li>
<li>PR: <a href="https://github.com/laravel/framework/pull/60848">#60848</a> (Customizable application builder)</li>
</ul>
            </div>
            <div class="mt-12">
                <div class="flex flex-col items-start space-y-4 sm:flex-row sm:space-x-6 sm:space-y-0"  data-statdive-tags="author-paulredmond">

    <img
        class="h-20 w-20 rounded-lg object-cover"
        src="https://www.gravatar.com/avatar/d9691184a54bfa1defe3dc7d625bc959?s=200"
        alt="Paul Redmond photo"
    />

    <div>
        <p class="font-display text-2xl font-bold leading-none text-black" itemprop="author">
            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80" href="/@paulredmond" rel="author"
            wire:navigate.hover
    >
    Paul Redmond
</a>
        </p>
        <div
            class="prose prose-sm mt-2 text-gray-600 prose-a:text-red-600 prose-a:transition prose-a:hover:text-red-700"
        >
            <p>Staff writer at Laravel News. Full stack web developer and author.</p>

        </div>
        <div class="mt-4 flex gap-2">
            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 inline-flex h-5 w-5 items-center justify-center !rounded-full hover:opacity-80" href="https://x.com/paulredmond" target="_blank" rel="noopener noreferrer"
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
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 inline-flex h-5 w-5 items-center justify-center !rounded-full hover:opacity-80" href="https://github.com/paulredmond" target="_blank" rel="noopener noreferrer"
    >
    <img
                class="h-4 w-4"
                src="https://picperf.io/https://laravel-news.com/images/github.svg"
                loading="lazy"
                alt="Github"
            />
            <span class="sr-only">Github</span>
</a>
    

    

    

    
        </div>
    </div>
</div>
            </div>
            <div class="mt-6 flex flex-wrap items-center gap-x-3 gap-y-2" data-statdive-tags="category-news">
                <span class="text-gray-600">Filed in:</span>
                <div class="flex flex-wrap items-center gap-x-2 gap-y-2">
                    <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 inline-flex !rounded-full px-4 py-2 text-xs font-bold leading-4 hover:opacity-80 focus-visible:ring-offset-1 bg-red-600 text-white" href="/category/news"
            wire:navigate.hover
    >
    News
</a>
                                            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 inline-flex !rounded-full px-4 py-2 text-xs font-bold leading-4 hover:opacity-80 focus-visible:ring-offset-1 bg-red-600 text-white" href="/tag/releases"
            wire:navigate.hover
    >
    Laravel Releases
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
                <div
            class="w-56 translate-x-6 rounded-lg border border-gray-100 px-4 py-3 text-xs font-bold shadow-sm truncate"
        >
            <a href="https://larajobs.com/job/3904?ref=laravelnews&utm_source=laravelnews&utm_medium=referral">
                Full-Stack Developer (Laravel + Inertia/Vue)
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
                            src="https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/laravel-cloud-featured-new.png"
                            alt="image"
                            height="100"
                            width="230"
                            loading="lazy"
                        />
                    </div>
                    <div class="pt-2 text-sm">
                        <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 font-bold text-[##565454]" href="https://lrvl.co/cloud-ln"
    >
    Laravel Cloud
</a>
                        <p class="mt-1 text-sm xl:text-xs">
                            Easily create and manage your servers and deploy your Laravel applications in seconds.
                        </p>
                    </div>
                </div>
                <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 absolute inset-0 !block h-full w-full !rounded-lg" href="https://lrvl.co/cloud-ln" onclick="fathom.trackEvent('laravelcloud|article|click', {_value: 100});"
    >
    <span class="sr-only">Visit Laravel Cloud</span>
</a>
                <script>
                    window.addEventListener('load', (event) => {
                        if (typeof fathom !== 'undefined' && fathom.trackEvent) {
                            fathom.trackEvent('laravelcloud|article|show');
                        }
                    });
                </script>
            </div>
        </div>
    </div>
    </div>
    <section class="bg-gradient-to-r from-gray-100 to-white py-24 sm:py-32">
    <div class="mx-auto w-full max-w-2xl px-6 lg:max-w-7xl">
        <div class="flex flex-wrap items-center justify-between gap-x-8 gap-y-3">
            <h2 class="text-3xl font-bold sm:text-4xl lg:text-[40px]">
                <a href="/partners" class="hover:text-red-600">Partners</a>
            </h2>
            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 font-bold text-red-600 hover:text-red-700" href="/partners"
            wire:navigate.hover
    >
    View all &rarr;
</a>
        </div>
        <div class="mt-12 grid gap-8 md:mt-16 md:grid-cols-2 lg:grid-cols-3">
                            <div
    class="group relative bg-white rounded-lg shadow-card 