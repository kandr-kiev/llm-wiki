---
source_url: https://laravel-news.com/enforce-per-action-waiting-periods-in-laravel-with-cooldown?utm_medium=feed&utm_source=feedpress.me&utm_campaign=Feed%3A+laravelnews
ingested: 2026-07-17
sha256: 3ad07d399167f528cf15d4c1bcdabf6072dfb99d6e019be1f1705bb858d0d2a8
blog_source: Laravel News
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <meta name="csrf-token" content=""/>

    <title>Enforce Per-Action Waiting Periods in Laravel with Cooldown - Laravel News</title>
    
    
    <meta
        name="description"
        content="A Laravel package that enforces per-action, per-owner cooldown periods with a fluent API, an Eloquent trait, route middleware, atomic locking, and cache or database storage."
    />
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="Enforce Per-Action Waiting Periods in Laravel with Cooldown - Laravel News"/>
    <meta
        property="og:description"
        content="A Laravel package that enforces per-action, per-owner cooldown periods with a fluent API, an Eloquent trait, route middleware, atomic locking, and cache or database storage."
    />
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="Enforce Per-Action Waiting Periods in Laravel with Cooldown - Laravel News"/>
    <meta
        property="og:image"
        content="https://laravelnews.s3.amazonaws.com/featured-images/Laravel-Cooldown-LN.png"
    />
    <meta
        property="og:description"
        content="A Laravel package that enforces per-action, per-owner cooldown periods with a fluent API, an Eloquent trait, route middleware, atomic locking, and cache or database storage."
    />
    <meta property="og:url" content="https://laravel-news.com/enforce-per-action-waiting-periods-in-laravel-with-cooldown"/>
    <meta property="og:site_name" content="Laravel News"/>
    <meta property="og:locale" content="en_US"/>

    
    <meta name="twitter:card" content="summary_large_image"/>
    <meta name="twitter:site" content="@laravelnews"/>
    <meta name="twitter:title" content="Enforce Per-Action Waiting Periods in Laravel with Cooldown - Laravel News"/>
    <meta
        property="twitter:image"
        content="https://laravelnews.s3.amazonaws.com/featured-images/Laravel-Cooldown-LN.png"
    />
    <meta
        name="twitter:description"
        content="A Laravel package that enforces per-action, per-owner cooldown periods with a fluent API, an Eloquent trait, route middleware, atomic locking, and cache or database storage."
    />
            <meta name="twitter:creator" content="@ylynfatt"/>
    
    <link href="https://laravel-news.com/enforce-per-action-waiting-periods-in-laravel-with-cooldown" rel="canonical"/>
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
            href="https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/Laravel-Cooldown-LN.png"
        />
    
    <script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "NewsArticle",
    "headline": "Enforce Per-Action Waiting Periods in Laravel with Cooldown",
    "datePublished": "2026-07-16T09:00:00-04:00",
    "description": "A Laravel package that enforces per-action, per-owner cooldown periods with a fluent API, an Eloquent trait, route middleware, atomic locking, and cache or database storage.",
    "image": "https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/Laravel-Cooldown-LN.png",
    "dateModified": "2026-07-15T20:24:21-04:00",
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
        "@id": "https://laravel-news.com/enforce-per-action-waiting-periods-in-laravel-with-cooldown"
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
            "name": "Enforce Per-Action Waiting Periods in Laravel with Cooldown"
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
                <h1 class="text-4xl font-bold sm:text-5xl md:text-6xl">Enforce Per-Action Waiting Periods in Laravel with Cooldown</h1>

                <div class="mt-6 flex items-center gap-3">

                    <p class="text-xs text-gray-600">
                                                    Last updated on
                            <time
                                itemprop="dateModified"
                                datetime="2026-07-15T20:24:21"
                            >
                                July 15th, 2026
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
                        src="https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/Laravel-Cooldown-LN.png"
                        alt="Enforce Per-Action Waiting Periods in Laravel with Cooldown image"
                        class="mt-12 aspect-[2/1] w-full overflow-hidden rounded-xl object-cover shadow-card"
                    />
                            </div>
        </div>
        <div class="mx-auto w-full max-w-4xl px-6 py-20">


            
            <div
                class="prose max-w-4xl break-words prose-a:text-red-600 prose-a:transition prose-a:hover:text-red-700 prose-pre:rounded-lg prose-pre:bg-gray-100/50 prose-pre:p-6 prose-img:mx-auto prose-img:rounded-lg prose-img:border prose-img:border-gray-100"
            >
                <p>Laravel Cooldown is a package from <a href="https://github.com/zaber-dev">Mahedi Zaman Zaber</a> for putting a timed lock on a named action: no second OTP for 120 seconds, one password reset request per minute, a payment retry that can't fire again until the window clears. Where Laravel's <code>RateLimiter</code> counts how many requests hit an endpoint within a window, Cooldown tracks whether a specific action for a specific owner is still within its waiting period and can persist that state in the database rather than only in the cache.</p>
<h2><a id="content-main-features" href="#content-main-features" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Main features</h2>
<ul>
<li><strong>Owner-scoped actions</strong> through <code>Cooldown::for('resend_verification', $user)</code>, where the owner can be any model, an IP string, or nothing for a global lock</li>
<li><strong>A <code>HasCooldowns</code> trait</strong> that puts <code>$user-&gt;cooldown('change_avatar')</code> on any Eloquent model</li>
<li><strong>Route middleware</strong> (<code>cooldown:action,duration</code>) with an optional driver argument</li>
<li><strong>Atomic execution</strong> via <code>block()</code>, which takes a lock around the callback and sets the cooldown on success</li>
<li><strong><code>enforce()</code></strong> to throw a <code>CooldownActiveException</code> that renders as HTTP 429</li>
<li><strong>An immutable <code>CooldownInfo</code> object</strong> with <code>remainingSeconds()</code> and <code>remainingForHumans()</code></li>
<li><strong>Cache or database backends</strong>, switchable per call with <code>using()</code></li>
<li><strong>Pruning</strong> of expired database rows through Laravel's <code>model:prune</code> command</li>
</ul>
<h2><a id="content-the-fluent-api" href="#content-the-fluent-api" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>The Fluent API</h2>
<p>A cooldown is a named action, an optional owner, and a duration. Once you name one, you can set it, check it, or clear it:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">ZaberDev\Cooldown\Facades\Cooldown</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #005CC5;">Cooldown</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">for</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;rebuild_search_index&#39;</span><span style="color: #24292E;">)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">for</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">600</span><span style="color: #24292E;">);</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #005CC5;">Cooldown</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">for</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;resend_verification&#39;</span><span style="color: #24292E;">, $user)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">for</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">900</span><span style="color: #24292E;">);</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #005CC5;">Cooldown</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">for</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;daily_checkin&#39;</span><span style="color: #24292E;">, $user)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">until</span><span style="color: #24292E;">(</span><span style="color: #6F42C1;">now</span><span style="color: #24292E;">()</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">endOfDay</span><span style="color: #24292E;">());</span></div></code></pre>
<p>When a cooldown is active, <code>info()</code> returns an object with the duration details:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">if</span><span style="color: #24292E;"> (</span><span style="color: #005CC5;">Cooldown</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">for</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;resend_verification&#39;</span><span style="color: #24292E;">, $user)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">active</span><span style="color: #24292E;">()) {</span></div><div class='line'><span style="color: #24292E;">    $info </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">Cooldown</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">for</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;resend_verification&#39;</span><span style="color: #24292E;">, $user)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">info</span><span style="color: #24292E;">();</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">    </span><span style="color: #005CC5;">echo</span><span style="color: #24292E;"> </span><span style="color: #032F62;">&quot;Please wait &quot;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">.</span><span style="color: #24292E;"> $info</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">remainingForHumans</span><span style="color: #24292E;">() </span><span style="color: #D73A49;">.</span><span style="color: #24292E;"> </span><span style="color: #032F62;">&quot; before requesting another email.&quot;</span><span style="color: #24292E;">;</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #005CC5;">echo</span><span style="color: #24292E;"> </span><span style="color: #032F62;">&quot;Seconds remaining: &quot;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">.</span><span style="color: #24292E;"> $info</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">remainingSeconds</span><span style="color: #24292E;">();</span></div><div class='line'><span style="color: #24292E;">}</span></div></code></pre>
<p>If you'd rather stop the request than branch on it, <code>enforce()</code> throws when the action is still locked:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #005CC5;">Cooldown</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">for</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;request_password_reset&#39;</span><span style="color: #24292E;">, $user)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">enforce</span><span style="color: #24292E;">();</span></div></code></pre>
<h2><a id="content-atomic-blocking" href="#content-atomic-blocking" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Atomic Blocking</h2>
<p>Cooldowns exist for exactly this situation: sending an OTP, charging a card, where two concurrent requests can both pass the check before either one sets the lock. <code>block()</code> handles this by acquiring a lock, running the callback, and applying the cooldown only if the work succeeds:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #005CC5;">Cooldown</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">for</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;send_login_code&#39;</span><span style="color: #24292E;">, $user)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">block</span><span style="color: #24292E;">(</span><span style="color: #D73A49;">function</span><span style="color: #24292E;"> () </span><span style="color: #D73A49;">use</span><span style="color: #24292E;"> ($smsClient, $user) {</span></div><div class='line'><span style="color: #24292E;">    $smsClient</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">sendCode</span><span style="color: #24292E;">($user</span><span style="color: #D73A49;">-&gt;</span><span style="color: #24292E;">phone);</span></div><div class='line'><span style="color: #24292E;">}, </span><span style="color: #6F42C1;">duration</span><span style="color: #24292E;">: </span><span style="color: #005CC5;">90</span><span style="color: #24292E;">);</span></div></code></pre>
<p>If you need to manage the lock yourself, <code>acquireLock()</code> and <code>releaseLock()</code> are available for that purpose.</p>
<h2><a id="content-cooldowns-on-eloquent-models" href="#content-cooldowns-on-eloquent-models" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Cooldowns on Eloquent Models</h2>
<p>Add the <code>HasCooldowns</code> trait and the same builder hangs off the model instance, scoped to that record:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">ZaberDev\Cooldown\HasCooldowns</span><span style="color: #24292E;">;</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #D73A49;">class</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">User</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">extends</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">Authenticatable</span></div><div class='line'><span style="color: #24292E;">{</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">use</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">HasCooldowns</span><span style="color: #24292E;">;</span></div><div class='line'><span style="color: #24292E;">}</span></div></code></pre>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$user</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">cooldown</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;change_avatar&#39;</span><span style="color: #24292E;">)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">for</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">300</span><span style="color: #24292E;">);</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #D73A49;">if</span><span style="color: #24292E;"> ($user</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">cooldown</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;change_avatar&#39;</span><span style="color: #24292E;">)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">active</span><span style="color: #24292E;">()) {</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">return</span><span style="color: #24292E;"> </span><span style="color: #6F42C1;">response</span><span style="color: #24292E;">()</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">json</span><span style="color: #24292E;">([</span><span style="color: #032F62;">&#39;message&#39;</span><span style="color: #24292E;"> </span><span style="color: #D73A49;">=&gt;</span><span style="color: #24292E;"> </span><span style="color: #032F62;">&#39;You can change your avatar again shortly.&#39;</span><span style="color: #24292E;">], </span><span style="color: #005CC5;">429</span><span style="color: #24292E;">);</span></div><div class='line'><span style="color: #24292E;">}</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">$user</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">cooldown</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;change_avatar&#39;</span><span style="color: #24292E;">)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">reset</span><span style="color: #24292E;">();</span></div></code></pre>
<p>On the database backend, the records are polymorphic, so a model's cooldowns are queryable like any other relation:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #24292E;">$activeCooldowns </span><span style="color: #D73A49;">=</span><span style="color: #24292E;"> $user</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">cooldowns</span><span style="color: #24292E;">()</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">where</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;expires_at&#39;</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;&gt;&#39;</span><span style="color: #24292E;">, </span><span style="color: #6F42C1;">now</span><span style="color: #24292E;">())</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">get</span><span style="color: #24292E;">();</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #24292E;">$user</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">cooldowns</span><span style="color: #24292E;">()</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">delete</span><span style="color: #24292E;">();</span></div></code></pre>
<h2><a id="content-route-middleware" href="#content-route-middleware" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Route Middleware</h2>
<p>The <code>cooldown</code> middleware takes an action name, a duration in seconds, and an optional driver:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #005CC5;">Route</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">post</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;/feedback&#39;</span><span style="color: #24292E;">, [</span><span style="color: #005CC5;">FeedbackController</span><span style="color: #D73A49;">::class</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;store&#39;</span><span style="color: #24292E;">])</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">middleware</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;cooldown:submit_feedback,120&#39;</span><span style="color: #24292E;">);</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #005CC5;">Route</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">post</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;/invoices/export&#39;</span><span style="color: #24292E;">, [</span><span style="color: #005CC5;">InvoiceController</span><span style="color: #D73A49;">::class</span><span style="color: #24292E;">, </span><span style="color: #032F62;">&#39;export&#39;</span><span style="color: #24292E;">])</span></div><div class='line'><span style="color: #24292E;">    </span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">middleware</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;cooldown:invoice_export,600,database&#39;</span><span style="color: #24292E;">);</span></div></code></pre>
<h2><a id="content-storage-backends" href="#content-storage-backends" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Storage Backends</h2>
<p>The default driver is <code>cache</code>, backed by the store you've configured, so both Redis and Memcached work. The <code>database</code> driver writes to a <code>cooldowns</code> table instead, which is what you want when the lock is tied to something like billing and can't be removed during a cache flush. You can choose per call:</p>
<pre><code data-theme="github-light" data-lang="php" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #005CC5;">Cooldown</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">for</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;poll_job_status&#39;</span><span style="color: #24292E;">, $ip)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">using</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;cache&#39;</span><span style="color: #24292E;">)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">for</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">20</span><span style="color: #24292E;">);</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #005CC5;">Cooldown</span><span style="color: #D73A49;">::</span><span style="color: #6F42C1;">for</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;renew_subscription&#39;</span><span style="color: #24292E;">, $user)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">using</span><span style="color: #24292E;">(</span><span style="color: #032F62;">&#39;database&#39;</span><span style="color: #24292E;">)</span><span style="color: #D73A49;">-&gt;</span><span style="color: #6F42C1;">for</span><span style="color: #24292E;">(</span><span style="color: #005CC5;">86400</span><span style="color: #24292E;">);</span></div></code></pre>
<p>If you need somewhere else to keep the state, <code>Cooldown::extend()</code> registers a custom driver from a service provider, and expired database rows can be cleared on a schedule with Laravel's <code>model:prune</code> command.</p>
<h2><a id="content-installation" href="#content-installation" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Installation</h2>
<p>The package requires PHP 8.2 and supports Laravel 11, 12, and 13:</p>
<pre><code data-theme="github-light" data-lang="bash" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #6F42C1;">composer</span><span style="color: #24292E;"> </span><span style="color: #032F62;">require</span><span style="color: #24292E;"> </span><span style="color: #032F62;">zaber-dev/laravel-cooldown</span></div><div class='line'>&nbsp;</div><div class='line'><span style="color: #6F42C1;">php</span><span style="color: #24292E;"> </span><span style="color: #032F62;">artisan</span><span style="color: #24292E;"> </span><span style="color: #032F62;">vendor:publish</span><span style="color: #24292E;"> </span><span style="color: #005CC5;">--provider=</span><span style="color: #032F62;">&quot;ZaberDev\Cooldown\CooldownServiceProvider&quot;</span></div><div class='line'><span style="color: #6F42C1;">php</span><span style="color: #24292E;"> </span><span style="color: #032F62;">artisan</span><span style="color: #24292E;"> </span><span style="color: #032F62;">migrate</span></div></code></pre>
<p><code>config/cooldown.php</code> sets the default driver (<code>COOLDOWN_DRIVER</code>), the cache store and key prefix, the database table name, and whether events are dispatched.</p>
<p>You can find installation instructions and full documentation on <a href="https://github.com/zaber-dev/laravel-cooldown">GitHub</a>.</p>
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
                