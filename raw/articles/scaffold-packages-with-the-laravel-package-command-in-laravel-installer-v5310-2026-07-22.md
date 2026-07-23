---
source_url: https://laravel-news.com/laravel-installer-5-31-0?utm_medium=feed&utm_source=feedpress.me&utm_campaign=Feed%3A+laravelnews
ingested: 2026-07-22
sha256: 95a2e55ffc2930d1681ee9b7f613c04ae73ce2ea3dd7366067b602546d8bcfa1
blog_source: Laravel News
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <meta name="csrf-token" content=""/>

    <title>Scaffold Packages with the `laravel package` Command in Laravel Installer v5.31.0 - Laravel News</title>
    
    
    <meta
        name="description"
        content="Laravel Installer v5.31.0 introduces a command to scaffold Laravel packages, along with environment variable propagation for node-less setups and automated PHP version matching for GitHub Actions."
    />
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="Scaffold Packages with the `laravel package` Command in Laravel Installer v5.31.0 - Laravel News"/>
    <meta
        property="og:description"
        content="Laravel Installer v5.31.0 introduces a command to scaffold Laravel packages, along with environment variable propagation for node-less setups and automated PHP version matching for GitHub Actions."
    />
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="Scaffold Packages with the `laravel package` Command in Laravel Installer v5.31.0 - Laravel News"/>
    <meta
        property="og:image"
        content="https://laravelnews.s3.amazonaws.com/featured-images/laravel-installer-featured-LN.png"
    />
    <meta
        property="og:description"
        content="Laravel Installer v5.31.0 introduces a command to scaffold Laravel packages, along with environment variable propagation for node-less setups and automated PHP version matching for GitHub Actions."
    />
    <meta property="og:url" content="https://laravel-news.com/laravel-installer-5-31-0"/>
    <meta property="og:site_name" content="Laravel News"/>
    <meta property="og:locale" content="en_US"/>

    
    <meta name="twitter:card" content="summary_large_image"/>
    <meta name="twitter:site" content="@laravelnews"/>
    <meta name="twitter:title" content="Scaffold Packages with the `laravel package` Command in Laravel Installer v5.31.0 - Laravel News"/>
    <meta
        property="twitter:image"
        content="https://laravelnews.s3.amazonaws.com/featured-images/laravel-installer-featured-LN.png"
    />
    <meta
        name="twitter:description"
        content="Laravel Installer v5.31.0 introduces a command to scaffold Laravel packages, along with environment variable propagation for node-less setups and automated PHP version matching for GitHub Actions."
    />
            <meta name="twitter:creator" content="@ylynfatt"/>
    
    <link href="https://laravel-news.com/laravel-installer-5-31-0" rel="canonical"/>
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
            href="https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/laravel-installer-featured-LN.png"
        />
    
    <script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "NewsArticle",
    "headline": "Scaffold Packages with the `laravel package` Command in Laravel Installer v5.31.0",
    "datePublished": "2026-07-20T09:00:00-04:00",
    "description": "Laravel Installer v5.31.0 introduces a command to scaffold Laravel packages, along with environment variable propagation for node-less setups and automated PHP version matching for GitHub Actions.",
    "image": "https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/laravel-installer-featured-LN.png",
    "dateModified": "2026-07-20T01:09:42-04:00",
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
        "@id": "https://laravel-news.com/laravel-installer-5-31-0"
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
            "name": "Scaffold Packages with the `laravel package` Command in Laravel Installer v5.31.0"
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
                <h1 class="text-4xl font-bold sm:text-5xl md:text-6xl">Scaffold Packages with the `laravel package` Command in Laravel Installer v5.31.0</h1>

                <div class="mt-6 flex items-center gap-3">

                    <p class="text-xs text-gray-600">
                                                    Published on
                            <time
                                itemprop="dateModified"
                                datetime="2026-07-20T09:00:00"
                            >
                                July 20th, 2026
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
                        src="https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/laravel-installer-featured-LN.png"
                        alt="Scaffold Packages with the `laravel package` Command in Laravel Installer v5.31.0 image"
                        class="mt-12 aspect-[2/1] w-full overflow-hidden rounded-xl object-cover shadow-card"
                    />
                            </div>
        </div>
        <div class="mx-auto w-full max-w-4xl px-6 py-20">


            
            <div
                class="prose max-w-4xl break-words prose-a:text-red-600 prose-a:transition prose-a:hover:text-red-700 prose-pre:rounded-lg prose-pre:bg-gray-100/50 prose-pre:p-6 prose-img:mx-auto prose-img:rounded-lg prose-img:border prose-img:border-gray-100"
            >
                <p>The Laravel team released Laravel Installer v5.31.0 with a new command to scaffold Laravel packages, environment variable propagation for node-less setups, automated PHP version matching for GitHub Actions, and various compatibility fixes.</p>
<ul>
<li>New <code>laravel package</code> command to scaffold packages from the CLI</li>
<li>Automated PHP version matching for continuous integration workflow files</li>
<li>Propagation of the <code>--no-node</code> option to starter kit installer hooks</li>
<li>Fallback output when <code>Laravel\Prompts\callout()</code> is not available</li>
<li>Windows compatibility fix adding <code>--timeout=0</code> to development queue listeners</li>
</ul>
<h2><a id="content-whats-new" href="#content-whats-new" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>What's New</h2>
<h3><a id="content-the-laravel-package-command" href="#content-the-laravel-package-command" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>The <code>laravel package</code> Command</h3>
<p>You can now scaffold new Laravel packages directly from the command line. This command clones the official <a href="https://github.com/laravel/package-skeleton">laravel/package-skeleton</a> repository, cleans the git history, installs dependencies, and then runs the skeleton's configuration script.</p>
<p>To create a new package:</p>
<pre><code data-theme="github-light" data-lang="bash" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #6F42C1;">laravel</span><span style="color: #24292E;"> </span><span style="color: #032F62;">package</span><span style="color: #24292E;"> </span><span style="color: #032F62;">my-new-package</span></div></code></pre>
<p>By default, the command runs interactively, prompting you for package configuration and details. It also supports various flags to predefine your package's features:</p>
<ul>
<li><code>--config</code>: Include a configuration file</li>
<li><code>--routes</code>: Include routes</li>
<li><code>--views</code>: Include views</li>
<li><code>--translations</code>: Include translations</li>
<li><code>--migrations</code>: Include migrations</li>
<li><code>--assets</code>: Include assets</li>
<li><code>--commands</code>: Include commands</li>
<li><code>--facade</code>: Include a facade</li>
<li><code>--boost-skill</code>: Include a Laravel Boost skill</li>
</ul>
<p>You can also pass metadata options directly:</p>
<ul>
<li><code>--author-name</code>: Author name</li>
<li><code>--author-email</code>: Author email</li>
<li><code>--package-name</code>: Package name</li>
<li><code>--package-name-human</code>: Package display name</li>
<li><code>--package-description</code>: Package description</li>
<li><code>--vendor-namespace</code>: Vendor namespace</li>
<li><code>--class-name</code>: Main class name</li>
</ul>
<p>The command works with the installer's non-interactive AI agent detection, allowing agents to automate package setup.</p>
<p><strong>PR:</strong> <a href="https://github.com/laravel/installer/pull/546">laravel/installer#546</a></p>
<h3><a id="content-local-php-version-matching-in-ci-workflows" href="#content-local-php-version-matching-in-ci-workflows" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Local PHP Version Matching in CI Workflows</h3>
<p>When setting up a starter kit, the installer now detects the PHP version running on your local machine and configures the generated GitHub Actions workflow (<code>.github/workflows/tests.yml</code>) to use the same major and minor version. This ensures that your continuous integration environment tests against the same PHP version you use for local development.</p>
<p><strong>PR:</strong> <a href="https://github.com/laravel/installer/pull/553">laravel/installer#553</a></p>
<h3><a id="content-propagating---no-node-to-starter-kit-hooks" href="#content-propagating---no-node-to-starter-kit-hooks" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Propagating <code>--no-node</code> to Starter Kit Hooks</h3>
<p>If you run <code>laravel new</code> with the <code>--no-node</code> flag, the installer now passes a <code>LARAVEL_INSTALLER_NO_NODE=1</code> environment variable to any post-create starter kit hooks. This allows starter kits to bypass npm and Node-related tasks when you want to avoid Node.js dependencies.</p>
<p><strong>PR:</strong> <a href="https://github.com/laravel/installer/pull/552">laravel/installer#552</a></p>
<h3><a id="content-fallback-prompt-output" href="#content-fallback-prompt-output" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Fallback Prompt Output</h3>
<p>The installer now checks for the existence of <code>Laravel\Prompts\callout()</code> before invoking it. If the function is not available (for example, when running with older versions of Laravel Prompts), the installer falls back to writing directly to the standard output rather than throwing an error.</p>
<p><strong>PR:</strong> <a href="https://github.com/laravel/installer/pull/549">laravel/installer#549</a></p>
<h3><a id="content-windows-queue-listener-timeout-fix" href="#content-windows-queue-listener-timeout-fix" class="not-prose mr-1 text-gray-600 font-normal heading-permalink" aria-hidden="true" title="Permalink">#</a>Windows Queue Listener Timeout Fix</h3>
<p>During local development setup on Windows, the installer configures the <code>dev</code> script in <code>composer.json</code> to run processes concurrently. To prevent the queue listener from stopping unexpectedly, this update adds the <code>--timeout=0</code> flag to <code>php artisan queue:listen</code>.</p>
<p><strong>PR:</strong> <a href="https://github.com/laravel/installer/pull/550">laravel/installer#550</a></p>
<p><strong>Upgrade Notes</strong></p>
<p>No breaking changes are expected for typical applications. To update your globally installed Laravel installer, run:</p>
<pre><code data-theme="github-light" data-lang="bash" class='torchlight' style='background-color: #fff; --theme-selection-background: #e2e5e9;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color: #6F42C1;">composer</span><span style="color: #24292E;"> </span><span style="color: #032F62;">global</span><span style="color: #24292E;"> </span><span style="color: #032F62;">update</span><span style="color: #24292E;"> </span><span style="color: #032F62;">laravel/installer</span></div></code></pre>
<p><strong>References</strong></p>
<ul>
<li><a href="https://github.com/laravel/installer/compare/v5.30.0...v5.31.0">Full Changelog</a></li>
</ul>
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
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 inline-flex !rounded-full px-4 py-2 text-xs font-bold leading-4 hover:opacity-80 focus-visible:ring-offset-1 bg-red-600 text-white" href="/tag/tools"
            wire:navigate.hover
    >
    Tools
</a>
                                            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 inline-flex !rounded-full px-4 py-2 text-xs font-bold leading-4 hover:opacity-80 focus-visible:ring-offset-1 bg-red-600 text-white" href="/tag/laravel-installer-releases"
            wire:navigate.hover
    >
    Laravel Installer Releases
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
                            src="https://picperf.io/https://laravelnews.s3.amazonaws.com/images/01KGFP6DE7G6CAJ22KPXAZ7658.png"
                            alt="image"
                            height="100"
                            width="230"
                            loading="lazy"
                        />
                    </div>
                    <div class="pt-2 text-sm">
                        <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 font-bold text-[##565454]" href="https://acquaintsoft.com/hire-laravel-developers"
    >
    Acquaint Softtech
</a>
                        <p class="mt-1 text-sm xl:text-xs">
                            Hire Laravel developers with AI expertise at $20/hr. Get started in 48 hours.
                        </p>
                    </div>
                </div>
                <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 absolute inset-0 !block h-full w-full !rounded-lg" href="https://acquaintsoft.com/hire-laravel-developers" onclick="fathom.trackEvent('acquaintsoft|article|click', {_value: 100});"
    >
    <span class="sr-only">Visit Acquaint Softtech</span>
</a>
                <script>
                    window.addEventListener('load', (event) => {
                        if (typeof fathom !== 'undefined' && fathom.trackEvent) {
                            fathom.trackEvent('acquaintsoft|article|show');
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
    class="group relative bg-white rounded-lg shadow-card border border-gray-100 p-8 w-full shrink-0 lg:p-12"
>
    <img
        src="https://picperf.io/https://laravelnews.s3.amazonaws.com/partners/logos/laravelcloud.png"
        alt="Laravel Cloud logo"
        class="h-10 object-contain object-left-top transition group-hover:opacity-80"
        height="40"
        width="300px"
        loading="lazy"
    />

    <h3 class="sr-only">
        Laravel Cloud
    </h3>

    <p class="mt-6 text-gray-600 group-hover:opacity-80">Easily create and manage your servers and deploy your Laravel applications in seconds.</p>

            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 absolute inset-0 !block h-full w-full !rounded-lg" href="https://go.laravel.news/cloud/home" target="_blank"
    >
    <span class="sr-only">Laravel Cloud</span>
</a>
    
</div>
                            <div
    class="group relative bg-white rounded-lg shadow-card border border-gray-100 p-8 w-full shrink-0 lg:p-12"
>
    <img
        src="https://picperf.io/https://laravelnews.s3.amazonaws.com/partners/logos/acquaint.png"
        alt="Acquaint Softtech logo"
        class="h-10 object-contain object-left-top transition group-hover:opacity-80"
        height="40"
        width="300px"
        loading="lazy"
    />

    <h3 class="sr-only">
        Acquaint Softtech
    </h3>

    <p class="mt-6 text-gray-600 group-hover:opacity-80">Acquaint Softtech offers AI-ready Laravel developers who onboard in 48 hours at $3000/Month with no lengthy sales process and a 100 percent money-back guarantee.</p>

            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 absolute inset-0 !block h-full w-full !rounded-lg" href="https://acquaintsoft.com/hire-laravel-developers" target="_blank"
    >
    <span class="sr-only">Acquaint Softtech</span>
</a>
    
</div>
                            <div
    class="group relative bg-white rounded-lg shadow-card border border-gray-100 p-8 w-full shrink-0 lg:p-12"
>
    <img
        src="https://picperf.io/https://laravelnews.s3.amazonaws.com/partners/logos/kirschbaum-new.png"
        alt="Kirschbaum logo"
        class="h-10 object-contain object-left-top transition group-hover:opacity-80"
        height="40"
        width="300px"
        loading="lazy"
    />

    <h3 class="sr-only">
        Kirschbaum
    </h3>

    <p class="mt-6 text-gray-600 group-hover:opacity-80">Providing innovation and stability to ensure your web application succeeds.</p>

            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 absolute inset-0 !block h-full w-full !rounded-lg" href="http://kirschbaumdevelopment.com/" target="_blank"
    >
    <span class="sr-only">Kirschbaum</span>
</a>
    
</div>
                            <div
    class="group relative bg-white rounded-lg shadow-card border border-gray-100 p-8 w-full shrink-0 lg:p-12"
>
    <img
        src="https://picperf.io/https://laravelnews.s3.amazonaws.com/partners/logos/qMZ85wCJw4QwTO8pF4Mo2UOUz94WgASnQRKCWB3e.png"
        alt="SaaSykit: Laravel SaaS Starter Kit logo"
        class="h-10 object-contain object-left-top transition group-hover:opacity-80"
        height="40"
        width="300px"
        loading="lazy"
    />

    <h3 class="sr-only">
        SaaSykit: Laravel SaaS Starter Kit
    </h3>

    <p class="mt-6 text-gray-600 group-hover:opacity-80">SaaSykit is a Multi-tenant Laravel SaaS Starter Kit that comes with all features required to run a modern SaaS. Payments, Beautiful Checkout, Admin Panel, User dashboard, Auth, Ready Components, Stats, Blog, Docs and more.
</p>

            <a
    class="inline-flex rounded-sm transition duration-300 leading-none focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600/80 absolute inset-0 !block h-full w-full !rounded-lg" href="https://saasykit.com/?utm_campaign=laravel&amp;utm_source=laravelnews" target="_blank"
    >
    <span class="sr-only">SaaSykit: Laravel SaaS Starter Kit</span>
</a>
    
</div>
                            <div
    class="group relative bg-white rounded-lg shadow-card border border-gray-100 p-8 w-full shrink-0 lg:p-12"
>
    <img
        src="https://picperf.io/https://laravelnews.s3.amazonaws.com/partners/laravel-shift-logo.svg"
        alt="Shift logo"
        class="h-10 object-contain object-left-top transition group-hover:opacity-80"
        height="40"
        width="300px"
        loading="lazy"
    />

    <h3 class="sr-only">
        Shift
    </h3>

    <p class="mt-6 text-gray-600 group-hover:opacity-80">Running an old Laravel version? Instant, automated Laravel upgrades and code modernization to keep your applications fresh.</p>

            <a
    class="inline-fle