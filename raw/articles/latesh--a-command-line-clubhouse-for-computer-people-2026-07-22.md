---
source_url: https://late.sh/
ingested: 2026-07-22
sha256: 9793e5e42ace45c9c664cf34abe5da9ea7ad52644e0598639b830c2a784b8e88
blog_source: Hacker News
---
<!DOCTYPE html>
<html lang="en" class="dark">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>late.sh</title>

    <!-- SEO Meta Tags -->
    <meta name="description" content="A cozy command-line clubhouse for computer people. Chat, music, games, art, coding, and tech news. Connect with any SSH client!">
    <meta name="keywords" content="command line, terminal, ssh, computer people, terminal community, linux, art, coding, clubhouse, multiplayer games, arcade, music, chat, news, tui, rust">
    <meta name="author" content="late.sh">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://late.sh/">
    <meta property="og:title" content="late.sh">
    <meta property="og:description" content="A cozy command-line clubhouse for computer people. Chat, music, games, art, coding, and tech news. Connect with any SSH client!">
    <meta property="og:image" content="https://late.sh/static/og-image.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="late.sh terminal clubhouse preview">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://late.sh/">
    <meta property="twitter:title" content="late.sh">
    <meta property="twitter:description" content="A cozy command-line clubhouse for computer people. Chat, music, games, art, coding, and tech news. Connect with any SSH client!">
    <meta property="twitter:image" content="https://late.sh/static/og-image.png">
    <meta property="twitter:image:alt" content="late.sh terminal clubhouse preview">

    <!-- Favicons -->
    <link rel="icon" href="/static/favicon.svg" type="image/svg+xml" sizes="any">
    <link rel="icon" href="/static/favicon-48x48.png" type="image/png" sizes="48x48">
    <link rel="icon" href="/static/favicon-32x32.png" type="image/png" sizes="32x32">
    <link rel="icon" href="/static/favicon.ico" sizes="16x16 32x32">
    <link rel="apple-touch-icon" href="/static/apple-touch-icon.png" sizes="180x180">
    <link rel="manifest" href="/static/site.webmanifest">
    <meta name="theme-color" content="#111827">

    <!-- Tailwind Output -->
    <link href="/static/style.css" rel="stylesheet">

    <!-- HTMX & Alpine -->
    <script src="https://unpkg.com/htmx.org@2.0.8"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.15.3/dist/cdn.min.js"></script>
</head>

<body class="bg-gray-800 text-gray-200 font-mono antialiased min-h-screen flex flex-col">
    <main class="flex-grow container mx-auto px-4 py-8">
        
<div class="max-w-4xl mx-auto">
    <!--
    <nav class="mb-8 border-b border-gray-700 pb-4 inline-flex items-center gap-6 text-sm">
        <a href="/dashboard" 
           class="inline-flex items-center hover:text-white transition-colors text-gray-400">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mr-2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
            Dashboard
        </a>
        <a href="/stream/demo" 
           class="inline-flex items-center hover:text-white transition-colors text-gray-400">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mr-2"><path d="M9 18V5l12-2v13"></path><circle cx="6" cy="18" r="3"></circle><circle cx="18" cy="16" r="3"></circle></svg>
            Stream
        </a>
        <a href="/connect/123" 
           class="inline-flex items-center hover:text-white transition-colors text-gray-400">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mr-2"><path d="M9 18V5l12-2v13"></path><circle cx="6" cy="18" r="3"></circle><circle cx="18" cy="16" r="3"></circle></svg>
            Connect
        </a>
    </nav>
-->

    
<style>
    @keyframes cursor-blink {

        0%,
        49% {
            opacity: 1;
        }

        50%,
        100% {
            opacity: 0;
        }
    }

    .cursor-blink {
        animation: cursor-blink 1s step-end infinite;
    }

    @keyframes fade-up {
        from {
            opacity: 0;
            transform: translateY(6px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .stagger {
        opacity: 0;
        animation: fade-up 0.4s ease forwards;
    }

    .stagger-1 {
        animation-delay: 0s;
    }

    .stagger-2 {
        animation-delay: 0.07s;
    }

    .stagger-3 {
        animation-delay: 0.14s;
    }

    .stagger-4 {
        animation-delay: 0.21s;
    }

    .stagger-5 {
        animation-delay: 0.28s;
    }

    @media (prefers-reduced-motion: reduce) {
        .stagger {
            opacity: 1;
            animation: none;
        }
    }
</style>

<div x-data="{ copied: null, copy(text) { navigator.clipboard.writeText(text); this.copied = text; setTimeout(() => this.copied = null, 2000); } }" class="max-w-lg mx-auto pt-8 sm:pt-16">

    <div class="stagger stagger-1 mb-14">
        <div class="flex items-baseline justify-between gap-4">
            <h1 class="text-3xl sm:text-4xl text-green-500 tracking-tight">late.sh</h1>
            <div class="text-xs shrink-0" hx-get="/status" hx-trigger="load, every 5s" hx-swap="innerHTML"></div>
        </div>
        <p class="text-gray-500 mt-2">a cozy command-line clubhouse for computer people</p>
    </div>

    <div class="stagger stagger-2 mb-12">
        <button @click="copy('ssh late.sh')"
            class="group w-full text-left border border-gray-700 hover:border-green-900 px-5 py-4 transition-colors duration-200 bg-gray-900/40">
            <div class="flex items-center justify-between gap-4">
                <span class="text-lg min-w-0 truncate">
                    <span class="text-gray-600">$ </span>
                    <span class="text-gray-100">ssh late.sh</span>
                    <span class="cursor-blink text-green-500 ml-px">&#9612;</span>
                </span>
                <span class="shrink-0 text-right text-xs">
                    <span x-cloak x-show="copied !== 'ssh late.sh'"
                        class="text-gray-700 group-hover:text-gray-500 transition-colors">copy</span>
                    <span x-cloak x-show="copied === 'ssh late.sh'" class="text-green-600">copied</span>
                </span>
            </div>
            <div class="mt-2 text-xs text-gray-600">
                if it fails, generate a key first: <span class="text-gray-400">ssh-keygen -t ed25519</span>
            </div>
        </button>
    </div>

    <div class="stagger stagger-3 mb-4">
        <button @click="copy('curl -fsSL https://cli.late.sh/install.sh | bash')"
            class="group w-full text-left border border-gray-800 hover:border-green-950 px-5 py-4 transition-colors duration-200 bg-gray-900/20">
            <div class="flex items-center justify-between gap-4">
                <span class="text-sm sm:text-base text-gray-300 min-w-0 truncate">
                    <span class="text-gray-600">$ </span>
                    <span class="text-gray-100">curl -fsSL https://cli.late.sh/install.sh | bash</span>
                </span>
                <span class="shrink-0 text-right text-xs">
                    <span x-cloak x-show="copied !== 'curl -fsSL https://cli.late.sh/install.sh | bash'"
                        class="text-gray-700 group-hover:text-gray-500 transition-colors">copy</span>
                    <span x-cloak x-show="copied === 'curl -fsSL https://cli.late.sh/install.sh | bash'" class="text-green-600">copied</span>
                </span>
            </div>
            <div class="mt-2 text-xs text-gray-600">
                installs the local `late` companion CLI on macOS, Linux, or Termux
            </div>
        </button>
    </div>

    <div class="stagger stagger-3 mb-4">
        <button @click="copy('irm https://cli.late.sh/install.ps1 | iex')"
            class="group w-full text-left border border-gray-800 hover:border-green-950 px-5 py-4 transition-colors duration-200 bg-gray-900/20">
            <div class="flex items-center justify-between gap-4">
                <span class="text-sm sm:text-base text-gray-300 min-w-0 truncate">
                    <span class="text-gray-600">PS&gt; </span>
                    <span class="text-gray-100">irm https://cli.late.sh/install.ps1 | iex</span>
                </span>
                <span class="shrink-0 text-right text-xs">
                    <span x-cloak x-show="copied !== 'irm https://cli.late.sh/install.ps1 | iex'"
                        class="text-gray-700 group-hover:text-gray-500 transition-colors">copy</span>
                    <span x-cloak x-show="copied === 'irm https://cli.late.sh/install.ps1 | iex'" class="text-green-600">copied</span>
                </span>
            </div>
            <div class="mt-2 text-xs text-gray-600">
                installs `late.exe` on Windows PowerShell
            </div>
        </button>
    </div>

    <div class="stagger stagger-3 mb-12">
        <button @click="copy('git clone https://github.com/mpiorowski/late-sh && cd late-sh && cargo build --release --bin late')"
            class="group w-full text-left border border-gray-800 hover:border-green-950 px-5 py-4 transition-colors duration-200 bg-gray-900/20">
            <div class="flex items-center justify-between gap-4">
                <span class="text-xs sm:text-sm text-gray-300 min-w-0 truncate">
                    <span class="text-gray-600">$ </span>
                    <span class="text-gray-100">git clone https://github.com/mpiorowski/late-sh &amp;&amp; cd late-sh &amp;&amp; cargo build --release</span>
                </span>
                <span class="shrink-0 text-right text-xs">
                    <span x-cloak x-show="copied !== 'git clone https://github.com/mpiorowski/late-sh && cd late-sh && cargo build --release --bin late'"
                        class="text-gray-700 group-hover:text-gray-500 transition-colors">copy</span>
                    <span x-cloak x-show="copied === 'git clone https://github.com/mpiorowski/late-sh && cd late-sh && cargo build --release --bin late'"
                        class="text-green-600">copied</span>
                </span>
            </div>
            <div class="mt-2 text-xs text-gray-600">
                or build the companion CLI from source
            </div>
        </button>
    </div>

    <div class="stagger stagger-4 mb-14 text-sm leading-loose">
        <div class="text-gray-500"><span class="text-gray-700">&#9500;&#9472;</span> chill radio, classical, and guest stations</div>
        <div class="text-gray-500"><span class="text-gray-700">&#9500;&#9472;</span> the arcade <span class="text-gray-700">(2048, sudoku, nonograms, solitaire)</span></div>
        <div class="text-gray-500"><span class="text-gray-700">&#9500;&#9472;</span> collaborative artboard</div>
        <div class="text-gray-500"><span class="text-gray-700">&#9500;&#9472;</span> daily challenges &amp; streaks</div>
        <div class="text-gray-500"><span class="text-gray-700">&#9500;&#9472;</span> live chat</div>
        <div class="text-gray-500"><span class="text-gray-700">&#9500;&#9472;</span> share &amp; discuss news</div>
        <div class="text-gray-500"><span class="text-gray-700">&#9492;&#9472;</span> multiplayer games <span class="text-gray-700">(coming soon)</span></div>
    </div>

    <div class="stagger stagger-5 mb-4 text-xs leading-relaxed">
        <div class="text-gray-600 mb-3"><span class="text-gray-700">#</span> artboard</div>
        <div class="text-gray-500">a shared <span class="text-green-600">ASCII canvas</span>. paint, erase, sign your work.</div>
        <div class="text-gray-500">each cell remembers who placed it.</div>
        <div class="text-gray-600 mt-3">snapshots are saved daily and monthly,</div>
        <div class="text-gray-600">so the history sticks around as the board keeps changing.</div>
    </div>

    <div class="stagger stagger-5 mb-14">
        <a href="/gallery"
            class="group block w-full text-left border border-gray-700 hover:border-green-900 px-5 py-4 transition-colors duration-200 bg-gray-900/40">
            <div class="flex items-center justify-between gap-4">
                <span class="text-lg min-w-0 truncate">
                    <span class="text-gray-100">/gallery</span>
                </span>
                <span class="shrink-0 text-xs text-gray-700 group-hover:text-green-600 transition-colors">browse &rarr;</span>
            </div>
            <div class="mt-2 text-xs text-gray-600">
                full-screen viewer with pan, zoom, and per-cell author info
            </div>
        </a>
    </div>

    <div class="stagger stagger-5 mb-4 text-xs leading-relaxed">
        <div class="text-gray-600 mb-3"><span class="text-gray-700">#</span> work</div>
        <div class="text-gray-500">who's around, what they build, who's <span class="text-green-600">open to gigs</span>.</div>
        <div class="text-gray-500">one profile per person, posted from the TUI.</div>
        <div class="text-gray-600 mt-3">headline, status, skills, links &mdash; plus an</div>
        <div class="text-gray-600">optional bio, late.fetch readout, and showcase.</div>
        <div class="text-gray-600 mt-3">to post yours, <span class="text-gray-400">ssh late.sh</span>, open the work room, press <span class="text-gray-400">i</span>.</div>
    </div>

    <div class="stagger stagger-5 mb-14">
        <a href="/profiles"
            class="group block w-full text-left border border-gray-700 hover:border-green-900 px-5 py-4 transition-colors duration-200 bg-gray-900/40">
            <div class="flex items-center justify-between gap-4">
                <span class="text-lg min-w-0 truncate">
                    <span class="text-gray-100">/profiles</span>
                </span>
                <span class="shrink-0 text-xs text-gray-700 group-hover:text-green-600 transition-colors">browse &rarr;</span>
            </div>
            <div class="mt-2 text-xs text-gray-600">
                everyone's work profiles, open gigs first
            </div>
        </a>
    </div>

    <div class="stagger stagger-5 mb-4 text-xs leading-relaxed">
        <div class="text-gray-600 mb-3"><span class="text-gray-700">#</span> play</div>
        <div class="text-gray-500">a <span class="text-green-600">read-only peek</span> at the TUI in your browser.</div>
        <div class="text-gray-500">tab around, see what's inside.</div>
        <div class="text-gray-600 mt-3">no typing, no chat, no games &mdash; just a window</div>
        <div class="text-gray-600">into a shared demo session.</div>
        <div class="text-gray-600 mt-3">for the real thing, <span class="text-gray-400">ssh late.sh</span>.</div>
    </div>

    <div class="stagger stagger-5 mb-14">
        <a href="/play"
            class="group block w-full text-left border border-gray-700 hover:border-green-900 px-5 py-4 transition-colors duration-200 bg-gray-900/40">
            <div class="flex items-center justify-between gap-4">
                <span class="text-lg min-w-0 truncate">
                    <span class="text-gray-100">/play</span>
                </span>
                <span class="shrink-0 text-xs text-gray-700 group-hover:text-green-600 transition-colors">peek &rarr;</span>
            </div>
            <div class="mt-2 text-xs text-gray-600">
                live demo session, navigation only
            </div>
        </a>
    </div>

    <div class="stagger stagger-5 mb-14 text-xs leading-relaxed">
        <div class="text-gray-600 mb-3"><span class="text-gray-700">#</span> identity</div>
        <div class="text-gray-500">no passwords. no OAuth. no accounts.</div>
        <div class="text-gray-500">your <span class="text-green-600">ssh key</span> is your identity.</div>
        <div class="text-gray-600 mt-3">chats, scores, and streaks are tied to your</div>
        <div class="text-gray-600">public key fingerprint. same key, same data.</div>
    </div>

    <div class="stagger stagger-5 mb-8 text-xs leading-relaxed">
        <div class="text-gray-600 mb-3"><span class="text-gray-700">#</span> privacy</div>
        <div class="text-gray-500">we store your key <span class="text-green-600">fingerprint</span>, not the full public key.</div>
        <div class="text-gray-500">no IP logging. no tracking. no analytics.</div>
        <div class="text-gray-600 mt-3">chat messages and game scores are stored in</div>
        <div class="text-gray-600">postgres, tied only to your fingerprint.</div>
        <div class="text-gray-600 mt-3">don't trust us? use a throwaway key:</div>
    </div>

    <div class="stagger stagger-5 mb-14">
        <button @click="copy('ssh-keygen -t ed25519 -f ~/.ssh/late_throwaway && ssh -o IdentitiesOnly=yes -i ~/.ssh/late_throwaway late.sh')"
            class="group w-full text-left border border-gray-800 hover:border-green-950 px-5 py-4 transition-colors duration-200 bg-gray-900/20">
            <div class="flex items-center justify-between gap-4">
                <span class="text-xs text-gray-300 min-w-0 truncate">
                    <span class="text-gray-600">$ </span>
                    <span class="text-gray-100">ssh-keygen -t ed25519 -f ~/.ssh/late_throwaway && ssh -o IdentitiesOnly=yes -i ~/.ssh/late_throwaway late.sh</span>
                </span>
                <span class="shrink-0 text-right text-xs">
                    <span x-cloak x-show="copied !== 'ssh-keygen -t ed25519 -f ~/.ssh/late_throwaway && ssh -o IdentitiesOnly=yes -i ~/.ssh/late_throwaway late.sh'"
                        class="text-gray-700 group-hover:text-gray-500 transition-colors">copy</span>
                    <span x-cloak x-show="copied === 'ssh-keygen -t ed25519 -f ~/.ssh/late_throwaway && ssh -o IdentitiesOnly=yes -i ~/.ssh/late_throwaway late.sh'"
                        class="text-green-600">copied</span>
                </span>
            </div>
            <div class="mt-2 text-xs text-gray-600">
                generates a disposable key &mdash; zero risk, full experience
            </div>
        </button>
    </div>

</div>

</div>

    </main>
</body>

</html>