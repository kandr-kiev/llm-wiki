---
source_url: https://laravel-news.com/a-practical-guide-to-laravels-first-party-image-processing?utm_medium=feed&utm_source=feedpress.me&utm_campaign=Feed%3A+laravelnews
ingested: 2026-07-23
sha256: cc444be9e7f0d332387bfa7813f6c248b8047bdbf8eec55ccbff00c344a78d54
blog_source: Laravel News
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <meta name="csrf-token" content=""/>

    <title>A Practical Guide to Laravel&#039;s First-Party Image Processing - Laravel News</title>
    
    
    <meta
        name="description"
        content="Learn how to use Laravel&#039;s new Illuminate\Image API introduced in Laravel 13.20 to resize, transform, convert, and store images with practical examples."
    />
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="A Practical Guide to Laravel&#039;s First-Party Image Processing - Laravel News"/>
    <meta
        property="og:description"
        content="Learn how to use Laravel&#039;s new Illuminate\Image API introduced in Laravel 13.20 to resize, transform, convert, and store images with practical examples."
    />
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="A Practical Guide to Laravel&#039;s First-Party Image Processing - Laravel News"/>
    <meta
        property="og:image"
        content="https://laravelnews.s3.amazonaws.com/featured-images/illuminate-image-featured.png"
    />
    <meta
        property="og:description"
        content="Learn how to use Laravel&#039;s new Illuminate\Image API introduced in Laravel 13.20 to resize, transform, convert, and store images with practical examples."
    />
    <meta property="og:url" content="https://laravel-news.com/a-practical-guide-to-laravels-first-party-image-processing"/>
    <meta property="og:site_name" content="Laravel News"/>
    <meta property="og:locale" content="en_US"/>

    
    <meta name="twitter:card" content="summary_large_image"/>
    <meta name="twitter:site" content="@laravelnews"/>
    <meta name="twitter:title" content="A Practical Guide to Laravel&#039;s First-Party Image Processing - Laravel News"/>
    <meta
        property="twitter:image"
        content="https://laravelnews.s3.amazonaws.com/featured-images/illuminate-image-featured.png"
    />
    <meta
        name="twitter:description"
        content="Learn how to use Laravel&#039;s new Illuminate\Image API introduced in Laravel 13.20 to resize, transform, convert, and store images with practical examples."
    />
            <meta name="twitter:creator" content="@paulredmond"/>
    
    <link href="https://laravel-news.com/a-practical-guide-to-laravels-first-party-image-processing" rel="canonical"/>
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

    <link rel="preload" as="style" href="https://laravel-news.com/build/assets/app-DPg1PIFS.css" /><link rel="modulepreload" as="script" href="https://laravel-news.com/build/assets/app-Dv8fbUhP.js" /><link rel="stylesheet" href="https://laravel-news.com/build/assets/app-DPg1PIFS.css" data-navigate-track="reload" /><script type="module" src="https://laravel-news.com/build/assets/app-Dv8fbUhP.js" data-navigate-track="reload"></script>
    
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
            href="https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/illuminate-image-featured.png"
        />
    
    <script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "A Practical Guide to Laravel's First-Party Image Processing",
    "datePublished": "2026-07-23T09:00:00-04:00",
    "description": "Learn how to use Laravel's new Illuminate\\Image API introduced in Laravel 13.20 to resize, transform, convert, and store images with practical examples.",
    "image": "https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/illuminate-image-featured.png",
    "dateModified": "2026-07-22T21:25:32-04:00",
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
        "@id": "https://laravel-news.com/a-practical-guide-to-laravels-first-party-image-processing"
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
            "name": "Laravel Tutorials",
            "item": "https://laravel-news.com/category/tutorials"
        },
        {
            "@type": "ListItem",
            "position": 3,
            "name": "A Practical Guide to Laravel's First-Party Image Processing"
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
                <h1 class="text-4xl font-bold sm:text-5xl md:text-6xl">A Practical Guide to Laravel&#039;s First-Party Image Processing</h1>

                <div class="mt-6 flex items-center gap-3">

                    <p class="text-xs text-gray-600">
                                                    Last updated on
                            <time
                                itemprop="dateModified"
                                datetime="2026-07-22T21:25:32"
                            >
                                July 22nd, 2026
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
                        src="https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/illuminate-image-featured.png"
                        alt="A Practical Guide to Laravel&#039;s First-Party Image Processing image"
                        class="mt-12 aspect-[2/1] w-full overflow-hidden rounded-xl object-cover shadow-card"
                    />
                            </div>
        </div>
        <div class="mx-auto w-full max-w-4xl px-6 py-20">


            
            <div
                class="prose max-w-4xl break-words prose-a:text-red-600 prose-a:transition prose-a:hover:text-red-700 prose-pre:rounded-lg prose-pre:bg-gray-100/50 prose-pre:p-6 prose-img:mx-auto prose-img:rounded-lg prose-img:border prose-img:border-gray-100"
            >
                <p>Laravel 13.20 introduced first-party image processing via the new <code>Illuminate\Image</code> component in <a href="https://github.com/laravel/framework/pull/59276">Pull Request #59276</a>. Before this release, resizing an avatar or converting an upload to WebP meant reaching for a package directly.</p>
<p>Now the framework ships a fluent, immutable API that covers the common cases: resizing, cropping, format conversion, quality control, effects, and storing the result on any filesystem disk.</p>
<p>In this tutorial, we'll walk through the API using practical examples: processing an avatar upload, generating responsive image variants, and applying transformations conditionally.</p>
<h2><a id="content-setup" href="#content-setup" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Setup</h2>
<p>The GD and Imagick drivers are backed by <a href="https://github.com/Intervention/image">Intervention Image</a> v4, which is a suggested dependency rather than a required one. Install it in your application with the following command:</p>
<pre><code data-theme="github-light" data-lang="shell" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #6F42C1;">composer</span><span style="color: #24292E;"> </span><span style="color: #032F62;">require</span><span style="color: #24292E;"> </span><span style="color: #032F62;">intervention/image:^4.0</span></div></code></pre>
<p>Laravel uses the GD driver by default. If your server has the Imagick extension, you can make it the default via the <code>images.default</code> config value or switch drivers per image at call time:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">usingImagick</span><span style="color: #24292E;">()</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">toBytes</span><span style="color: #24292E;">();</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #6A737D;">// Or by name:</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">using</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;imagick&#39;</span><span style="color: #24292E;">)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">toBytes</span><span style="color: #24292E;">();</span></div></code></pre>
<p>If you call a driver without Intervention Image installed, Laravel throws an <code>ImageException</code> telling you exactly what to install.</p>
<h2><a id="content-creating-an-image-instance" href="#content-creating-an-image-instance" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Creating an Image Instance</h2>
<p>Images can come from anywhere: an upload, a storage disk, a local path, a URL, or raw bytes. The new <code>Request::image()</code> method is the most convenient entry point for uploads:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$image </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> $request</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">image</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;avatar&#39;</span><span style="color: #24292E;">); </span><span style="color: #6A737D;">// ?Illuminate\Image\Image</span></div></code></pre>
<p>It returns <code>null</code> when the field is missing or isn't an uploaded file, so validate the upload first as you normally would.</p>
<p>The <code>Image</code> facade and <code>Storage</code> cover every other source:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Illuminate\Support\Facades\Image</span><span style="color: #24292E;">;</span></div><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Illuminate\Support\Facades\Storage</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">$image </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Image</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">fromPath</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;/path/to/photo.jpg&#39;</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">$image </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Image</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">fromUrl</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;https://example.com/photo.jpg&#39;</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">$image </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Image</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">fromStorage</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;uploads/photo.jpg&#39;</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;s3&#39;</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">$image </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Image</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">fromBytes</span><span style="color: #24292E;">($contents);</span></div><div class='line'><span style="color: #24292E;">$image </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Image</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">fromBase64</span><span style="color: #24292E;">($encoded);</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #6A737D;">// Equivalent to fromStorage():</span></div><div class='line'><span style="color: #24292E;">$image </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Storage</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">disk</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;s3&#39;</span><span style="color: #24292E;">)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">image</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;uploads/photo.jpg&#39;</span><span style="color: #24292E;">);</span></div></code></pre>
<h2><a id="content-how-the-pipeline-works" href="#content-how-the-pipeline-works" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>How the Pipeline Works</h2>
<p>Every transformation returns a <em>new</em> <code>Image</code> instance, and nothing is processed until you ask for output (<code>store()</code>, <code>toBytes()</code>, <code>width()</code>, and so on). This has a nice practical consequence: you can build a base image and branch off multiple variants without the transformations of one variant leaking into another:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$photo </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Image</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">fromStorage</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;uploads/photo.jpg&#39;</span><span style="color: #24292E;">)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">orient</span><span style="color: #24292E;">();</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">$thumbnail </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> $photo</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">cover</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">300</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">300</span><span style="color: #24292E;">)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">quality</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">60</span><span style="color: #24292E;">)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">toWebp</span><span style="color: #24292E;">();</span></div><div class='line'><span style="color: #24292E;">$display </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> $photo</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">scale</span><span style="color: #24292E;">(</span><span style="color: #6F42C1;">width</span><span style="color: #24292E;">: </span><span style="color: #005CC5;">1600</span><span style="color: #24292E;">)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">quality</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">80</span><span style="color: #24292E;">)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">toWebp</span><span style="color: #24292E;">();</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">$thumbnail</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">storeAs</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;photos&#39;</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;photo-thumb.webp&#39;</span><span style="color: #24292E;">, </span><span style="color: #6F42C1;">disk</span><span style="color: #24292E;">: </span><span style="color: #032F62;">&#39;s3&#39;</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">$display</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">storeAs</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;photos&#39;</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;photo-display.webp&#39;</span><span style="color: #24292E;">, </span><span style="color: #6F42C1;">disk</span><span style="color: #24292E;">: </span><span style="color: #032F62;">&#39;s3&#39;</span><span style="color: #24292E;">);</span></div></code></pre>
<p>The <code>orient()</code> call auto-rotates the image based on its EXIF data—worth doing first on any photo that came from a phone camera.</p>
<h2><a id="content-resizing-cover-contain-scale-resize-and-crop" href="#content-resizing-cover-contain-scale-resize-and-crop" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Resizing: cover, contain, scale, resize, and crop</h2>
<p>The API offers five ways to change dimensions, and picking the right one matters:</p>
<ul>
<li><code>cover($width, $height)</code> resizes and crops to fill the exact dimensions. Use it for avatars and thumbnails where you need a fixed size with no distortion.</li>
<li><code>contain($width, $height, $background)</code> fits the full image inside the dimensions, padding with an optional background color.</li>
<li><code>scale($width, $height)</code> resizes proportionally and never upscales—internally it maps to Intervention's <code>scaleDown()</code>. Either dimension can be omitted. This is the safe choice for &quot;shrink to at most X pixels wide.&quot;</li>
<li><code>resize($width, $height)</code> forces exact dimensions and may distort the image.</li>
<li><code>crop($width, $height, $x, $y)</code> cuts a region out of the original at the given offset.</li>
</ul>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">cover</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">512</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">512</span><span style="color: #24292E;">);          </span><span style="color: #6A737D;">// exact square, cropped to fit</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">contain</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">800</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">600</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;#fff&#39;</span><span style="color: #24292E;">); </span><span style="color: #6A737D;">// letterboxed on white</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">scale</span><span style="color: #24292E;">(</span><span style="color: #6F42C1;">width</span><span style="color: #24292E;">: </span><span style="color: #005CC5;">1200</span><span style="color: #24292E;">);        </span><span style="color: #6A737D;">// proportional, no upscaling</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">crop</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">400</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">300</span><span style="color: #24292E;">, </span><span style="color: #6F42C1;">x</span><span style="color: #24292E;">: </span><span style="color: #005CC5;">100</span><span style="color: #24292E;">, </span><span style="color: #6F42C1;">y</span><span style="color: #24292E;">: </span><span style="color: #005CC5;">50</span><span style="color: #24292E;">);</span></div></code></pre>
<h2><a id="content-effects-and-adjustments" href="#content-effects-and-adjustments" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Effects and Adjustments</h2>
<p>A handful of adjustment methods round out the transformation set:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$image</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">rotate</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">90</span><span style="color: #24292E;">)          </span><span style="color: #6A737D;">// clockwise, optional background for exposed corners</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">blur</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">10</span><span style="color: #24292E;">)            </span><span style="color: #6A737D;">// 0–100, defaults to 5</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">sharpen</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">15</span><span style="color: #24292E;">)         </span><span style="color: #6A737D;">// 0–100, defaults to 10</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">grayscale</span><span style="color: #24292E;">()</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">flip</span><span style="color: #24292E;">()              </span><span style="color: #6A737D;">// vertical; flipVertically() also works</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">flop</span><span style="color: #24292E;">();             </span><span style="color: #6A737D;">// horizontal; alias of flipHorizontally()</span></div></code></pre>
<h2><a id="content-formats-quality-and-optimize" href="#content-formats-quality-and-optimize" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Formats, Quality, and optimize()</h2>
<p>Format conversion is simple, using   the <code>toWebp()</code>, <code>toJpg()</code>, <code>toPng()</code>, <code>toGif()</code>, <code>toAvif()</code>, and <code>toBmp()</code> methods. Quality (1–100) applies to the lossy formats—WebP, JPEG, and AVIF:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">toWebp</span><span style="color: #24292E;">()</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">quality</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">80</span><span style="color: #24292E;">);</span></div></code></pre>
<p>The <code>optimize()</code> method is a shortcut that converts to WebP at quality 70 by default, and accepts a format and quality if you want different values:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">optimize</span><span style="color: #24292E;">();             </span><span style="color: #6A737D;">// WebP at quality 70</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">optimize</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;avif&#39;</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">60</span><span style="color: #24292E;">);   </span><span style="color: #6A737D;">// AVIF at quality 60</span></div></code></pre>
<p>The GD and Imagick drivers accept JPEG, PNG, GIF, BMP, and WebP images as input.</p>
<h2><a id="content-storing-and-retrieving-the-result" href="#content-storing-and-retrieving-the-result" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Storing and Retrieving the Result</h2>
<p>The storage methods mirror the <code>UploadedFile</code> API in Laravel, so processed images use the configured disk:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$path </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> $image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">store</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;avatars&#39;</span><span style="color: #24292E;">);                       </span><span style="color: #6A737D;">// random hashed name</span></div><div class='line'><span style="color: #24292E;">$path </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> $image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">storeAs</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;avatars&#39;</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;user-1.webp&#39;</span><span style="color: #24292E;">);      </span><span style="color: #6A737D;">// explicit name</span></div><div class='line'><span style="color: #24292E;">$path </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> $image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">storePublicly</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;avatars&#39;</span><span style="color: #24292E;">, </span><span style="color: #6F42C1;">disk</span><span style="color: #24292E;">: </span><span style="color: #032F62;">&#39;s3&#39;</span><span style="color: #24292E;">);   </span><span style="color: #6A737D;">// public visibility</span></div></code></pre>
<p>The hashed filename automatically gets the correct extension for the output format—store a JPEG upload after calling <code>toWebp()</code> and the file is named <code>*.webp</code>.</p>
<p>When you need the data instead of a file, you acn also use <code>toBytes()</code>, <code>toBase64()</code>, or <code>toDataUri()</code>.</p>
<p>Inspection methods run the pipeline and report on the <em>processed</em> result:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">width</span><span style="color: #24292E;">();       </span><span style="color: #6A737D;">// int</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">height</span><span style="color: #24292E;">();      </span><span style="color: #6A737D;">// int</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">dimensions</span><span style="color: #24292E;">();  </span><span style="color: #6A737D;">// [width, height]</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">mimeType</span><span style="color: #24292E;">();    </span><span style="color: #6A737D;">// e.g. &quot;image/webp&quot;</span></div><div class='line'><span style="color: #24292E;">$image</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">extension</span><span style="color: #24292E;">();   </span><span style="color: #6A737D;">// e.g. &quot;webp&quot;</span></div></code></pre>
<p>A data URI is handy for embedding small previews directly in HTML or emails:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$avatar </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Storage</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">image</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&quot;avatars/{</span><span style="color: #24292E;">$user</span><span style="color: #D73A49;">-&gt;</span><span style="color: #24292E;">avatar</span><span style="color: #032F62;">}&quot;</span><span style="color: #24292E;">)</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">cover</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">64</span><span style="color: #24292E;">, </span><span style="color: #005CC5;">64</span><span style="color: #24292E;">)</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">toDataUri</span><span style="color: #24292E;">();</span></div></code></pre>
<h2><a id="content-putting-it-together-avatar-uploads" href="#content-putting-it-together-avatar-uploads" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Putting It Together: Avatar Uploads</h2>
<p>Here's the whole flow you might use in a controller method that orients the upload, crops a 512x512 size, converts to WebP, and stores it publicly on S3:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">public</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">function</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">update</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">Request</span><span style="color: #24292E;"> $request)</span></div><div class='line'><span style="color: #24292E;">{</span></div><div class='line'><span style="color: #24292E;">    $request</span>