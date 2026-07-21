---
source_url: https://laravel-news.com/laravel-13-20-0?utm_medium=feed&utm_source=feedpress.me&utm_campaign=Feed%3A+laravelnews
ingested: 2026-07-17
sha256: 12e2030141a64e597780cda4e6c9bf52efd2b1d858b6d749d5b16ca10430c93b
blog_source: Laravel News
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <meta name="csrf-token" content=""/>

    <title>First-Party Image Processing in Laravel 13.20 - Laravel News</title>
    
    
    <meta
        name="description"
        content="Laravel 13.20.0 introduces an Image facade for resizing, converting, and storing images, along with a WithoutMiddleware controller attribute, a separate Redis session prefix, and quiet bulk increment methods on Eloquent."
    />
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="First-Party Image Processing in Laravel 13.20 - Laravel News"/>
    <meta
        property="og:description"
        content="Laravel 13.20.0 introduces an Image facade for resizing, converting, and storing images, along with a WithoutMiddleware controller attribute, a separate Redis session prefix, and quiet bulk increment methods on Eloquent."
    />
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="First-Party Image Processing in Laravel 13.20 - Laravel News"/>
    <meta
        property="og:image"
        content="https://laravelnews.s3.amazonaws.com/featured-images/laravel-13-featured.png"
    />
    <meta
        property="og:description"
        content="Laravel 13.20.0 introduces an Image facade for resizing, converting, and storing images, along with a WithoutMiddleware controller attribute, a separate Redis session prefix, and quiet bulk increment methods on Eloquent."
    />
    <meta property="og:url" content="https://laravel-news.com/laravel-13-20-0"/>
    <meta property="og:site_name" content="Laravel News"/>
    <meta property="og:locale" content="en_US"/>

    
    <meta name="twitter:card" content="summary_large_image"/>
    <meta name="twitter:site" content="@laravelnews"/>
    <meta name="twitter:title" content="First-Party Image Processing in Laravel 13.20 - Laravel News"/>
    <meta
        property="twitter:image"
        content="https://laravelnews.s3.amazonaws.com/featured-images/laravel-13-featured.png"
    />
    <meta
        name="twitter:description"
        content="Laravel 13.20.0 introduces an Image facade for resizing, converting, and storing images, along with a WithoutMiddleware controller attribute, a separate Redis session prefix, and quiet bulk increment methods on Eloquent."
    />
            <meta name="twitter:creator" content="@paulredmond"/>
    
    <link href="https://laravel-news.com/laravel-13-20-0" rel="canonical"/>
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
    "headline": "First-Party Image Processing in Laravel 13.20",
    "datePublished": "2026-07-15T09:00:00-04:00",
    "description": "Laravel 13.20.0 introduces an Image facade for resizing, converting, and storing images, along with a WithoutMiddleware controller attribute, a separate Redis session prefix, and quiet bulk increment methods on Eloquent.",
    "image": "https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/laravel-13-featured.png",
    "dateModified": "2026-07-14T20:24:23-04:00",
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
        "@id": "https://laravel-news.com/laravel-13-20-0"
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
            "name": "First-Party Image Processing in Laravel 13.20"
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
                <h1 class="text-4xl font-bold sm:text-5xl md:text-6xl">First-Party Image Processing in Laravel 13.20</h1>

                <div class="mt-6 flex items-center gap-3">

                    <p class="text-xs text-gray-600">
                                                    Last updated on
                            <time
                                itemprop="dateModified"
                                datetime="2026-07-14T20:24:23"
                            >
                                July 14th, 2026
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
                        alt="First-Party Image Processing in Laravel 13.20 image"
                        class="mt-12 aspect-[2/1] w-full overflow-hidden rounded-xl object-cover shadow-card"
                    />
                            </div>
        </div>
        <div class="mx-auto w-full max-w-4xl px-6 py-20">


            
            <div
                class="prose max-w-4xl break-words prose-a:text-red-600 prose-a:transition prose-a:hover:text-red-700 prose-pre:rounded-lg prose-pre:bg-gray-100/50 prose-pre:p-6 prose-img:mx-auto prose-img:rounded-lg prose-img:border prose-img:border-gray-100"
            >
                <p>Laravel 13.20.0 adds first-party image processing to the framework, with an immutable, driver-based API for transforming images that come from uploads, storage, URLs, or raw bytes. The release also brings a <code>WithoutMiddleware</code> controller attribute, a dedicated session prefix for Redis, and a batch of Eloquent and queue additions.</p>
<ul>
<li>First-party image processing via the new <code>Image</code> facade</li>
<li>A new <code>#[WithoutMiddleware]</code> controller attribute</li>
<li>Configure a separate Redis prefix for sessions</li>
<li>Quietly increment and decrement on Eloquent models</li>
<li>Enums accepted as <code>WithoutOverlapping</code> queue keys</li>
<li>And more</li>
</ul>
<h2><a id="content-whats-new" href="#content-whats-new" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>What's New</h2>
<h3><a id="content-first-party-image-processing" href="#content-first-party-image-processing" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>First-Party Image Processing</h3>
<p>Laravel 13.20 introduces an <code>Illuminate\Image</code> component that handles resizing, cropping, format conversion, and storage without reaching for a third-party wrapper.</p>
<p>Images are immutable: every transformation returns a new instance, and the queued transformations are applied when you ask for the result.</p>
<p>The most common path starts with an upload. <code>Request::image()</code> returns an <code>Image</code> instance for a given file key, or <code>null</code> if the key does not hold an uploaded file:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$request</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">image</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;avatar&#39;</span><span style="color: #24292E;">)</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">cover</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">200</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">200</span><span style="color: #24292E;">)</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">toWebp</span><span style="color: #24292E;">()</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">store</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;avatars&#39;</span><span style="color: #24292E;">);</span></div></code></pre>
<p>You can also build an image from a path, a URL, raw bytes, base64, or a storage disk:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #005CC5;">Image</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">fromPath</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;/path/to/photo.jpg&#39;</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #005CC5;">Image</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">fromUrl</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;https://example.com/photo.jpg&#39;</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #005CC5;">Image</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">fromBytes</span><span style="color: #24292E;">($bytes);</span></div><div class='line'><span style="color: #005CC5;">Image</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">fromStorage</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;photos/avatar.jpg&#39;</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;s3&#39;</span><span style="color: #24292E;">);</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #005CC5;">Storage</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">disk</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;s3&#39;</span><span style="color: #24292E;">)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">image</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;photos/avatar.jpg&#39;</span><span style="color: #24292E;">);</span></div></code></pre>
<p>Transformations, output options, and inspection methods are all available on the instance:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #6A737D;">// Transformations...</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">cover</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">200</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">200</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">contain</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">800</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">600</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">crop</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">200</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">200</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">resize</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">1024</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">768</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">scale</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">1200</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">800</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">rotate</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">90</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">blur</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">10</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">sharpen</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">10</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">grayscale</span><span style="color: #24292E;">();</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">flip</span><span style="color: #24292E;">();</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">flop</span><span style="color: #24292E;">();</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">orient</span><span style="color: #24292E;">(); </span><span style="color: #6A737D;">// Applies EXIF rotation...</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #6A737D;">// Output format and quality...</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">toWebp</span><span style="color: #24292E;">();</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">toJpg</span><span style="color: #24292E;">()</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">quality</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">80</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">optimize</span><span style="color: #24292E;">(); </span><span style="color: #6A737D;">// WebP at quality 70...</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">optimize</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;jpg&#39;</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">85</span><span style="color: #24292E;">);</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #6A737D;">// Reading and inspecting...</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">toBytes</span><span style="color: #24292E;">();</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">toBase64</span><span style="color: #24292E;">();</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">toDataUri</span><span style="color: #24292E;">();</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">width</span><span style="color: #24292E;">();</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">height</span><span style="color: #24292E;">();</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">dimensions</span><span style="color: #24292E;">();</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">mimeType</span><span style="color: #24292E;">();</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">extension</span><span style="color: #24292E;">();</span></div></code></pre>
<p>Because instances are immutable, you can branch from one source image to produce several variants:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$image </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> $request</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">image</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;photo&#39;</span><span style="color: #24292E;">);</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">cover</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">200</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">200</span><span style="color: #24292E;">)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">toWebp</span><span style="color: #24292E;">()</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">store</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;thumbnails&#39;</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">grayscale</span><span style="color: #24292E;">()</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">toWebp</span><span style="color: #24292E;">()</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">store</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;grayscale&#39;</span><span style="color: #24292E;">);</span></div></code></pre>
<p>Two drivers ship with the component, both backed by Intervention Image v4: GD and Imagick. You can pick a driver per image, and the <code>Image</code> facade lets you override how a driver handles a given transformation:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Illuminate\Image\Transformations\Sharpen</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #6A737D;">// Pick a driver per image...</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">using</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;imagick&#39;</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">usingGd</span><span style="color: #24292E;">();</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">usingImagick</span><span style="color: #24292E;">();</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #6A737D;">// Override how a driver handles a transformation...</span></div><div class='line'><span style="color: #005CC5;">Image</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">transformUsing</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;gd&#39;</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">Sharpen</span><span style="color: #D73A49;">::class</span><span style="color: #24292E;">, </span><span style="color: #D73A49;">function</span><span style="color: #24292E;"> ($image, </span><span style="color: #005CC5;">Sharpen</span><span style="color: #24292E;"> $sharpen) {</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #6A737D;">// Custom sharpen handling for the GD driver...</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">return</span><span style="color: #24292E;"> $image;</span></div><div class='line'><span style="color: #24292E;">});</span></div></code></pre>
<p>Intervention Image is a suggested dependency rather than a required one, so you install it yourself:</p>
<pre><code data-theme="github-light" data-lang="shell" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #6F42C1;">composer</span><span style="color: #24292E;"> </span><span style="color: #032F62;">require</span><span style="color: #24292E;"> </span><span style="color: #032F62;">intervention/image</span></div></code></pre>
<p>See <a href="https://github.com/laravel/framework/pull/59276">#59276</a>.</p>
<h3><a id="content-a-withoutmiddleware-controller-attribute" href="#content-a-withoutmiddleware-controller-attribute" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>A <code>#[WithoutMiddleware]</code> Controller Attribute</h3>
<p>The routing attributes gain a counterpart to <code>#[Middleware]</code>. Where the latter attaches middleware to a controller class or method, <code>#[WithoutMiddleware]</code> excludes it, giving you the &quot;excluding middleware&quot; behavior of route groups at the attribute level:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">App\Http\Middleware\EnsureTokenIsValid</span><span style="color: #24292E;">;</span></div><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Illuminate\Routing\Controllers\Attributes\Middleware</span><span style="color: #24292E;">;</span></div><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Illuminate\Routing\Controllers\Attributes\WithoutMiddleware</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">#[</span><span style="color: #005CC5;">Middleware</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">EnsureTokenIsValid</span><span style="color: #D73A49;">::class</span><span style="color: #24292E;">)]</span></div><div class='line'><span style="color: #D73A49;">class</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">UserController</span></div><div class='line'><span style="color: #24292E;">{</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">public</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">function</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">index</span><span style="color: #24292E;">()</span></div><div class='line'><span style="color: #24292E;">    {</span></div><div class='line'><span style="color: #24292E;">        </span><span style="color: #6A737D;">// Middleware applies here...</span></div><div class='line'><span style="color: #24292E;">    }</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">    #[</span><span style="color: #005CC5;">WithoutMiddleware</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">EnsureTokenIsValid</span><span style="color: #D73A49;">::class</span><span style="color: #24292E;">)]</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">public</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">function</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">profile</span><span style="color: #24292E;">()</span></div><div class='line'><span style="color: #24292E;">    {</span></div><div class='line'><span style="color: #24292E;">        </span><span style="color: #6A737D;">// ...but not here.</span></div><div class='line'><span style="color: #24292E;">    }</span></div><div class='line'><span style="color: #24292E;">}</span></div></code></pre>
<p>Matching uses <code>ReflectionAttribute::IS_INSTANCEOF</code>, so subclasses of a middleware are excluded too. See <a href="https://github.com/laravel/framework/pull/60709">#60709</a>.</p>
<h3><a id="content-redis-session-prefix" href="#content-redis-session-prefix" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Redis Session Prefix</h3>
<p>Applications that point both <code>SESSION_DRIVER</code> and <code>CACHE_STORE</code> at Redis have until now had sessions inherit the cache prefix, which makes session keys hard to pick out when you are cleaning up or debugging a shared keystore. A new <code>prefix</code> option in <code>config/session.php</code> lets you set a separate one:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #032F62;">&#39;prefix&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">env</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;SESSION_PREFIX&#39;</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">Str</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">slug</span><span style="color: #24292E;">((</span><span style="color: #D73A49;">string</span><span style="color: #24292E;">) </span><span style="color: #6F42C1;">env</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;APP_NAME&#39;</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;laravel&#39;</span><span style="color: #24292E;">))</span><span style="color: #D73A49;">.</span><span style="color: #032F62;">&#39;-session-&#39;</span><span style="color: #24292E;">),</span></div></code></pre>
<p>The cache store is cloned before the session prefix is applied, so setting it does not affect cache keys. The option is opt-in and mirrors the existing <code>session.connection</code> setting. See <a href="https://github.com/laravel/framework/pull/60700">#60700</a>.</p>
<h3><a id="content-quiet-bulk-increments-on-eloquent" href="#content-quiet-bulk-increments-on-eloquent" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Quiet Bulk Increments on Eloquent</h3>
<p>Eloquent already had <code>incrementQuietly()</code> and <code>decrementQuietly()</code> for single columns. This release fills in the multi-column gap with <code>incrementEachQuietly()</code> and <code>decrementEachQuietly()</code>, which update several columns at once while suppressing model events:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$user</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">incrementEachQuietly</span><span style="color: #24292E;">([</span><span style="color: #032F62;">&#39;posts_count&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">1</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;points&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">10</span><span style="color: #24292E;">]);</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">$user</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">decrementEachQuietly</span><span style="color: #24292E;">([</span><span style="color: #032F62;">&#39;credits&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">3</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;tokens&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">2</span><span style="color: #24292E;">]);</span></div></code></pre>
<p>See <a href="https://github.com/laravel/framework/pull/60720">#60720</a> and the follow-up fix for dynamic calls in <a href="https://github.com/laravel/framework/pull/60737">#60737</a>.</p>
<h3><a id="content-enums-as-queue-overlap-keys" href="#content-enums-as-queue-overlap-keys" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Enums as Queue Overlap Keys</h3>
<p>The <code>WithoutOverlapping</code> job middleware now accepts a PHP enum as its key, so jobs keyed by an enumerated value no longer need a manual conversion to a string:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">class</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">UpdateCategory</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">implements</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">ShouldQueue</span></div><div class='line'><span style="color: #24292E;">{</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Queueable</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</d