---
source_url: https://www.jamesdrandall.com/posts/thrust_ai_powered_software_archaeology/
ingested: 2026-07-11
sha256: 3e6b36f7102332b2b9a447c7744292eadc0f6f78558503ae6052c6a958b335a0
blog_source: Hacker News AI
---
<!DOCTYPE html>
<html lang="en">
<head>
    



  
  
    
  


<title>AI Can&#39;t Recreate Thrust (But It Can Help You Understand It) | James Randall</title>
<link rel="canonical" href="https://www.jamesdrandall.com/posts/thrust_ai_powered_software_archaeology/" />
<meta http-equiv="Content-Type" content="text/html" charset="UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="description" content="Recreating a 1986 BBC Micro game by using AI to reverse-engineer 6502 assembly — extracting Q7.8 fixed-point physics, emulating the SN76489 sound chip, and discovering why the original feels the way it does. Software archaeology with a modern accomplice." />

<meta property="og:type" content="article" />
<meta property="og:url" content="https://www.jamesdrandall.com/posts/thrust_ai_powered_software_archaeology/" />
<meta property="og:title" content="AI Can&#39;t Recreate Thrust (But It Can Help You Understand It) | James Randall" />
<meta property="og:description" content="Recreating a 1986 BBC Micro game by using AI to reverse-engineer 6502 assembly — extracting Q7.8 fixed-point physics, emulating the SN76489 sound chip, and discovering why the original feels the way it does. Software archaeology with a modern accomplice." />

<meta property="og:image" content="https://www.jamesdrandall.com/posts/thrust_ai_powered_software_archaeology/metadata.jpg" />

<meta property="og:site_name" content="James Randall" />

<meta property="article:published_time" content="2026-02-23T08:30:00&#43;01:00" />
<meta property="article:modified_time" content="2026-02-23T08:30:00&#43;01:00" />



<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:url" content="https://www.jamesdrandall.com/posts/thrust_ai_powered_software_archaeology/" />
<meta name="twitter:title" content="AI Can&#39;t Recreate Thrust (But It Can Help You Understand It) | James Randall" />
<meta name="twitter:description" content="Recreating a 1986 BBC Micro game by using AI to reverse-engineer 6502 assembly — extracting Q7.8 fixed-point physics, emulating the SN76489 sound chip, and discovering why the original feels the way it does. Software archaeology with a modern accomplice." />

<meta name="twitter:image" content="https://www.jamesdrandall.com/posts/thrust_ai_powered_software_archaeology/metadata.jpg" />



  
<link
    rel="stylesheet"
    href="/css/main.min.dbae71edd2d8be533f1cab854766997f424d0d730d1899bc778164b6cba25c1c.css"
    integrity="sha256-265x7dLYvlM/HKuFR2aZf0JNDXMNGJm8d4FktsuiXBw="
/>

<link rel="stylesheet" href="https://rsms.me/inter/inter.css" />

<link rel="stylesheet" href="/katex/katex.min.css">
<script defer src="/katex/katex.min.js"></script>
<script defer src="/katex/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true},{left: '$', right: '$', display: false},{left: '\\[', right: '\\]', display: true},{left: '\\(', right: '\\)', display: false}]});"></script>

<script
    src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js"
    defer
></script>
    
    <script src="https://cdn.usefathom.com/script.js" data-site="IIZYKIZL" defer></script>
    
</head>
<body class="bg-white">

<div class="relative bg-gray-50 mb-3 sm:mb-6">
  <div class="container">
    <div class="flex justify-between items-center py-6 md:space-x-10">
      <div class="flex justify-start lg:w-0 lg:flex-1">
        <div class="flex flex-col justify-start">
          <a href="/" class="blog-title">
            
            James Randall
          </a>
          <span class="blog-subtitle">Musings on software development, business and technology.</span>
        </div>
      </div>
      <div class="flex flex-row justify-end items-center">
        <a href="https://www.linkedin.com/in/james-randall-46a10310/">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" class="h-8 text-gray-600 hover:text-indigo-600">
            <path fill="currentColor" d="M416 32H31.9C14.3 32 0 46.5 0 64.3v383.4C0 465.5 14.3 480 31.9 480H416c17.6 0 32-14.5 32-32.3V64.3c0-17.8-14.4-32.3-32-32.3zM135.4 416H69V202.2h66.5V416zm-33.2-243c-21.3 0-38.5-17.3-38.5-38.5S80.9 96 102.2 96c21.2 0 38.5 17.3 38.5 38.5 0 21.3-17.2 38.5-38.5 38.5zm282.1 243h-66.4V312c0-24.8-.5-56.7-34.5-56.7-34.6 0-39.9 27-39.9 54.9V416h-66.4V202.2h63.7v29.2h.9c8.9-16.8 30.6-34.5 62.9-34.5 67.2 0 79.7 44.3 79.7 101.9V416z"/>
          </svg>
        </a>
        <a href="https://www.youtube.com/@CapnKroaker">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640" class="h-12 text-gray-600 link ml-3"><path fill="currentColor" d="M581.7 188.1C575.5 164.4 556.9 145.8 533.4 139.5C490.9 128 320.1 128 320.1 128C320.1 128 149.3 128 106.7 139.5C83.2 145.8 64.7 164.4 58.4 188.1C47 231 47 320.4 47 320.4C47 320.4 47 409.8 58.4 452.7C64.7 476.3 83.2 494.2 106.7 500.5C149.3 512 320.1 512 320.1 512C320.1 512 490.9 512 533.5 500.5C557 494.2 575.5 476.3 581.8 452.7C593.2 409.8 593.2 320.4 593.2 320.4C593.2 320.4 593.2 231 581.8 188.1zM264.2 401.6L264.2 239.2L406.9 320.4L264.2 401.6z"/></svg>
      </a>
         
        <a href="https://github.com/JamesRandall">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 496 512" class="h-8 text-gray-600 hover:text-indigo-600 ml-2">
            <path fill="currentColor" d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"/>
          </svg>
        </a>      
        
        <a href="" class="ml-3">
          <img src="/avatar.jpg" class="h-8 rounded-full">
        </a>
      </div>
    </div>
  </div>
</div>

  
<main class="container mx-auto px-4 bg-white">
  <div class="max-w-7xl mx-auto ">
    <div>
      <div>
        <div class="post-title">AI Can&#39;t Recreate Thrust (But It Can Help You Understand It)</div>
        <div>
</div>
        <div class="my-8 border border-gray-300 border-l-4 bg-gray-50 p-4 promo:p-5" style="border-left-color:#059669">
  <div class="flex flex-col promo:flex-row promo:items-center gap-4 promo:gap-5">
    <img
      src="/annhex-gameplay-wide.jpg"
      alt="Annhexation gameplay — a hex-based 4X strategy map"
      class="w-full h-40 object-cover border border-gray-300 promo:hidden" />
    <img
      src="/annhex-gameplay.jpg"
      alt="Annhexation gameplay — a hex-based 4X strategy map"
      class="hidden promo:block promo:w-32 promo:h-32 flex-shrink-0 object-cover border border-gray-300" />
    <div class="flex flex-col">
      <div class="flex items-center flex-wrap gap-x-2 gap-y-1">
        <span class="text-lg promo:text-xl font-extrabold tracking-tight text-gray-900">Annhexation</span>
        <span class="text-xs font-semibold uppercase tracking-wide text-green-800 bg-green-100 px-2 py-0.5 rounded">Early access</span>
      </div>
      <p class="mt-1 text-sm promo:text-base text-gray-600 leading-snug">A turn-based 4X strategy game I built from scratch &mdash; custom WebGPU engine, eight civilisations, no install. Play it in your browser right now.</p>
      <div class="mt-3 flex flex-col promo:flex-row promo:flex-wrap gap-2">
        <a
          href="https://annhexation.com"
          class="inline-flex items-center justify-center promo:justify-start gap-2 rounded-md bg-green-600 hover:bg-green-500 px-4 py-2 text-sm font-semibold text-white transition duration-150 ease-in-out">
          <svg class="h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path d="M6.3 3.5A1 1 0 0 0 4.75 4.34v11.32a1 1 0 0 0 1.55.84l8.49-5.66a1 1 0 0 0 0-1.68L6.3 3.5Z"/></svg>
          Play free in browser
        </a>
        <a
          href="https://store.steampowered.com/app/4663920/Annhexation/"
          class="inline-flex items-center justify-center promo:justify-start gap-2 rounded-md border border-gray-400 hover:border-gray-500 hover:bg-gray-100 px-4 py-2 text-sm font-semibold text-gray-900 transition duration-150 ease-in-out">
          <svg class="h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M9.05 2.93a1.06 1.06 0 0 1 1.9 0l1.83 3.72 4.1.6a1.06 1.06 0 0 1 .59 1.8l-2.97 2.9.7 4.08a1.06 1.06 0 0 1-1.54 1.12L10 15.31l-3.66 1.92a1.06 1.06 0 0 1-1.54-1.11l.7-4.09-2.97-2.9a1.06 1.06 0 0 1 .59-1.8l4.1-.6 1.83-3.71Z"/></svg>
          Wishlist on Steam
        </a>
      </div>
    </div>
  </div>
</div>

        <div class="markdown-content"><p>I asked Claude to recreate the classic 1986 game Thrust for me in the browser. It created slop but then things spiralled out of control.</p>
<p>Thrust was one of my favourite games on the BBC Micro — written by Jeremy C. Smith and published in 1986, it&rsquo;s a deceptively deep game with amazing physics and gameplay. You pilot a ship through caverns, collecting fuel, avoiding turret fire, and retrieving a pod for bonus points while fighting gravity and momentum. Jeremy went on to create the even more impressive Exile with Peter Irvin before tragically dying in an accident in 1992. He was somewhere between 16 and 18 when he wrote Thrust. You can <a href="http://bbcmicro.co.uk/game.php?id=432">play the original online</a>.</p>
<p>I&rsquo;ve got a BBC Master on the desk beside me and I still occasionally fire up Thrust on there along with some of the other classics. It&rsquo;s one of those games I keep returning to along with Elite, Exile and Holed Out. I&rsquo;ve now recreated three of these in different ways&hellip; the fourth is looking increasingly unavoidable.</p>
<h2 id="starting-with-slop">Starting with slop</h2>
<p>Anyway. I guess I&rsquo;d been thinking about Thrust as one morning recently I somewhat casually asked Claude Code to create it for me in the browser. I think I&rsquo;d been reading the latest proclamations of capability from OpenAI and Anthropic and so I put together quite a comprehensive spec, gave it access to the original disassembled source code, screenshots, and said &ldquo;go and recreate Thrust for me.&rdquo;.</p>
<p>It created something for which the term slop would be too kind, it very vaguely resembled Thrust — it had the scanline stuff, sort of — but it was truly dreadful. It hadn&rsquo;t even got gravity working right, the ship didn&rsquo;t fall properly, the controls felt weird, and it was just&hellip; grim. In some ways its amazing that it created something that sort of worked and sort of looked like Thrust but it was not playable and nothing close to the elegance and beautfy of the real thing.</p>
<p>And that&rsquo;s the thing about a game like Thrust. You could knock out something superficially similar pretty quickly — just run at the device frame rate, use standard delta-time physics, draw some caverns. But it would feel nothing like Thrust. The magic is in the specific timings, the weight of the ship, the way momentum builds. Particularly if you&rsquo;ve played the original then those details are everything, and an AI working from a text description, and it turns out even the original source, can&rsquo;t capture them.</p>
<h2 id="the-archaeology">The archaeology</h2>
<p>But it got me curious. How <em>did</em> the original work? I find the tricks developers used to make this stuff work on the 8-bits fascinating, and it became a bit of an archaeology session. I quickly found <a href="https://github.com/kieranhj/thrust-disassembly">this brilliant commented disassembly</a> of the original source by Kieran Connell and found myself feeding it into Claude and asking questions.</p>
<p>This is where things got interesting. Not because AI wrote the code — the code itself isn&rsquo;t complicated, it&rsquo;s a 1986 game that ran in 32K of RAM — but because Claude turned out to be an extraordinary tool for interrogating 6502 assembly. I could feed in a block of disassembled source and ask &ldquo;how does the level data work?&rdquo; or &ldquo;what&rsquo;s the physics model doing here?&rdquo; and get detailed, accurate explanations of what the original code was doing.</p>
<p>Now to be fair I was working from some commented disassembled source code but even given that it was able to extract information from both the comments and the assembly and come up with detailed descriptions of how the game worked. My sense is without the comments helping to focus it at the right areas it would have been much less useful - but even so, it made the job an awful lot simpler and more enjoyable. And yes it seems likely I&rsquo;ll strip the comments from the code and see how well Claude does then.</p>
<p>While doing this I realised I could use the answers as the basis to recreate the original game and started asking Claude to create specifications for the various subsystems. Most of the specifications I generated can be found in a <a href="https://github.com/JamesRandall/ts-thrust/tree/main/specs">specs folder</a> in the source code. I might write them up properly at some point but for now they give a good insight into the nuances in the original — there&rsquo;s quite a lot going on, more than I&rsquo;d realised. For example I&rsquo;d never noticed that the turrets stop firing for a time if you hit the generator, and there are subtleties in their firing angles that only become apparent when you read the actual code.</p>
<h2 id="the-physics">The Physics</h2>
<p>The physics was one of the most interesting areas to dig into. Thrust uses Q7.8 fixed-point arithmetic — a common technique on 8-bit machines where you don&rsquo;t have floating point hardware. The rotation system uses 32 steps with lookup tables for the force components.</p>
<p>But the really tricky part was timing. My first implementation used the correct constants from the disassembly — the same gravity, the same thrust values, the same drag — but the ship was far too fast and too agile. It didn&rsquo;t have the right weight. The constants were identical to the original so it had to be a timing problem.</p>
<p>And it was. The original doesn&rsquo;t run its physics at the BBC Micro&rsquo;s 50 Hz VSync rate. The tick loop waits at least 3 centiseconds per frame, giving an effective rate of about 33.33 Hz. But it goes further than that: within each tick, physics updates are gated to only 6 active slots per 16-tick window. The core of the physics step looks like this:</p>
<div class="highlight"><pre tabindex="0" style="color:#f8f8f2;background-color:#272822;-moz-tab-size:4;-o-tab-size:4;tab-size:4;"><code class="language-typescript" data-lang="typescript"><span style="display:flex;"><span><span style="color:#75715e">/** The 6 active physics slots per 16-tick window */</span>
</span></span><span style="display:flex;"><span><span style="color:#66d9ef">private</span> <span style="color:#66d9ef">static</span> <span style="color:#66d9ef">readonly</span> <span style="color:#a6e22e">ACTIVE_SLOTS</span> <span style="color:#f92672">=</span> <span style="color:#66d9ef">new</span> <span style="color:#a6e22e">Set</span>([<span style="color:#ae81ff">0</span>, <span style="color:#ae81ff">3</span>, <span style="color:#ae81ff">5</span>, <span style="color:#ae81ff">8</span>, <span style="color:#ae81ff">11</span>, <span style="color:#ae81ff">13</span>]);
</span></span><span style="display:flex;"><span>
</span></span><span style="display:flex;"><span><span style="color:#66d9ef">private</span> <span style="color:#a6e22e">tickStep</span>(<span style="color:#a6e22e">input</span>: <span style="color:#66d9ef">ThrustInput</span>)<span style="color:#f92672">:</span> <span style="color:#66d9ef">void</span> {
</span></span><span style="display:flex;"><span>  <span style="color:#66d9ef">const</span> <span style="color:#a6e22e">slot</span> <span style="color:#f92672">=</span> <span style="color:#66d9ef">this</span>.<span style="color:#a6e22e">tickCounter</span> <span style="color:#f92672">&amp;</span> <span style="color:#ae81ff">0x0F</span>;
</span></span><span style="display:flex;"><span>  <span style="color:#66d9ef">this</span>.<span style="color:#a6e22e">tickCounter</span> <span style="color:#f92672">=</span> (<span style="color:#66d9ef">this</span>.<span style="color:#a6e22e">tickCounter</span> <span style="color:#f92672">+</span> <span style="color:#ae81ff">1</span>) <span style="color:#f92672">&amp;</span> <span style="color:#ae81ff">0xFF</span>;
</span></span><span style="display:flex;"><span>
</span></span><span style="display:flex;"><span>  <span style="color:#75715e">// Rotation: 3 out of every 4 ticks, integer steps only
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#66d9ef">if</span> ((<span style="color:#a6e22e">slot</span> <span style="color:#f92672">&amp;</span> <span style="color:#ae81ff">0x03</span>) <span style="color:#f92672">!==</span> <span style="color:#ae81ff">0</span> <span style="color:#f92672">&amp;&amp;</span> <span style="color:#a6e22e">input</span>.<span style="color:#a6e22e">rotate</span> <span style="color:#f92672">!==</span> <span style="color:#ae81ff">0</span>) {
</span></span><span style="display:flex;"><span>    <span style="color:#a6e22e">s</span>.<span style="color:#a6e22e">angle</span> <span style="color:#f92672">=</span> ((<span style="color:#a6e22e">s</span>.<span style="color:#a6e22e">angle</span> <span style="color:#f92672">+</span> <span style="color:#a6e22e">input</span>.<span style="color:#a6e22e">rotate</span>) <span style="color:#f92672">+</span> <span style="color:#ae81ff">32</span>) <span style="color:#f92672">%</span> <span style="color:#ae81ff">32</span>;
</span></span><span style="display:flex;"><span>  }
</span></span><span style="display:flex;"><span>
</span></span><span style="display:flex;"><span>  <span style="color:#66d9ef">const</span> <span style="color:#a6e22e">isActiveSlot</span> <span style="color:#f92672">=</span> <span style="color:#a6e22e">ThrustPhysics</span>.<span style="color:#a6e22e">ACTIVE_SLOTS</span>.<span style="color:#a6e22e">has</span>(<span style="color:#a6e22e">slot</span>);
</span></span><span style="display:flex;"><span>
</span></span><span style="display:flex;"><span>  <span style="color:#75715e">// Force calculation — active slots only (6 of every 16 ticks)
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#66d9ef">if</span> (<span style="color:#a6e22e">isActiveSlot</span>) {
</span></span><span style="display:flex;"><span>    <span style="color:#a6e22e">s</span>.<span style="color:#a6e22e">forceY</span> <span style="color:#f92672">+=</span> <span style="color:#66d9ef">this</span>.<span style="color:#a6e22e">gravity</span>;
</span></span><span style="display:flex;"><span>
</span></span><span style="display:flex;"><span>    <span style="color:#66d9ef">if</span> (<span style="color:#a6e22e">input</span>.<span style="color:#a6e22e">thrust</span>) {
</span></span><span style="display:flex;"><span>      <span style="color:#a6e22e">s</span>.<span style="color:#a6e22e">forceY</span> <span style="color:#f92672">+=</span> <span style="color:#a6e22e">ANGLE_Y</span>[<span style="color:#a6e22e">angleIdx</span>] <span style="color:#f92672">/</span> (<span style="color:#ae81ff">1</span> <span style="color:#f92672">&lt;&lt;</span> <span style="color:#66d9ef">this</span>.<span style="color:#a6e22e">massShift</span>);
</span></span><span style="display:flex;"><span>      <span style="color:#a6e22e">s</span>.<span style="color:#a6e22e">forceX</span> <span style="color:#f92672">+=</span> <span style="color:#a6e22e">ANGLE_X</span>[<span style="color:#a6e22e">angleIdx</span>] <span style="color:#f92672">/</span> (<span style="color:#ae81ff">1</span> <span style="color:#f92672">&lt;&lt;</span> <span style="color:#66d9ef">this</span>.<span style="color:#a6e22e">massShift</span>);
</span></span><span style="display:flex;"><span>    }
</span></span><span style="display:flex;"><span>
</span></span><span style="display:flex;"><span>    <span style="color:#75715e">// Linear drag
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>    <span style="color:#a6e22e">s</span>.<span style="color:#a6e22e">forceX</span> <span style="color:#f92672">*=</span> <span style="color:#ae81ff">1</span> <span style="color:#f92672">-</span> <span style="color:#ae81ff">1</span><span style="color:#f92672">/</span><span style="color:#ae81ff">64</span>;   <span style="color:#75715e">// X: *= 63/64
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>    <span style="color:#a6e22e">s</span>.<span style="color:#a6e22e">forceY</span> <span style="color:#f92672">*=</span> <span style="color:#ae81ff">1</span> <span style="color:#f92672">-</span> <span style="color:#ae81ff">1</span><span style="color:#f92672">/</span><span style="color:#ae81ff">256</span>;  <span style="color:#75715e">// Y: *= 255/256
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  }
</span></span><span style="display:flex;"><span>
</span></span><span style="display:flex;"><span>  <span style="color:#75715e">// Position integration — every tick
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#a6e22e">s</span>.<span style="color:#a6e22e">x</span> <span style="color:#f92672">+=</span> <span style="color:#a6e22e">s</span>.<span style="color:#a6e22e">forceX</span>;
</span></span><span style="display:flex;"><span>  <span style="color:#a6e22e">s</span>.<span style="color:#a6e22e">y</span> <span style="color:#f92672">+=</span> <span style="color:#a6e22e">s</span>.<span style="color:#a6e22e">forceY</span>;
</span></span><span style="display:flex;"><span>}
</span></span></code></pre></div><p>That gating gives an effective force/drag rate of roughly 12.5 Hz — gravity and thrust only apply on those 6 specific ticks, not every frame. Even rotation has its own gating: it skips every fourth tick. These aren&rsquo;t arbitrary numbers; they&rsquo;re the exact patterns from the 6502 source, and they define the feel of the game - if you pull them around things quickly start to feel off. The asymmetric drag is interesting too — much stronger on the X axis (63/64) than Y (255/256), which is why horizontal movement feels &ldquo;stickier&rdquo; than vertical.</p>
<p>Once I got these timings right — matching the original&rsquo;s exact update cadence rather than just its constants — it felt perfect. You can switch between the BBC emulator and my version and the controls feel the same.</p>
<p>That&rsquo;s what became genuinely interesting to me. Creating a Thrust-like game with normal physics is trivial - particularly using a coding AI. Recreating <em>Thrust</em> — with all its specific feel and weight — required understanding exactly how the original worked, right down to the timing of individual physics updates within the game loop.</p>
<h2 id="the-sound">The Sound</h2>
<p>The other area that required some real focus was the sound. When I did my <a href="https://www.jamesdrandall.com/projects/webglite/">TypeScript version of Elite</a> I sampled the sounds directly from the emulator. That worked because Elite&rsquo;s sounds are quite discrete — short, sharp effects. Though the beam and military laser effects are off. But in Thrust the engine is a continuous drone that responds to key presses, and the explosions have specific envelopes. I could have sampled them but it just felt&hellip; wrong.</p>
<p>So instead I decided to take a different approach and instead recreated the SN76489 sound chip (the same chip that was in the Sega Master System, as I learned while working on this) and the BBC MOS interface to it. The MOS — the BBC&rsquo;s Machine Operating System — provided the interface through which games talked to the sound chip, using OSWORD calls and memory-mapped I/O.</p>
<p>A big help in this was the <a href="https://tobylobster.github.io/mos/">disassembled MOS code</a> that Toby Nelson has put together, along with the BBC Advanced User Guide and the SN76489 chip specifications. I was able to feed all of this into Claude, generate a comprehensive spec for the sound system, and from that build an emulated sound system running in an AudioWorklet. The full BBC MOS envelope processor (OSWORD 7/8) drives the chip emulator on the audio thread.</p>
<p>The result? The sounds are identical. And it would have been really difficult to get that by any other means — it&rsquo;s so timing-specific, so dependent on the exact envelope shapes and chip behaviour, that you really do need to emulate the actual hardware.</p>
<p>The sound system itself is quite elegant in how it layers. At the top level, playing a sound means sending the same OSWORD 7 parameters the original game used — channel, amplitude, pitch, duration:</p>
<div class="highlight"><pre tabindex="0" style="color:#f8f8f2;background-color:#272822;-moz-tab-size:4;-o-tab-size:4;tab-size:4;"><code class="language-typescript" data-lang="typescript"><span style="display:flex;"><span><span style="color:#66d9ef">const</span> <span style="color:#a6e22e">sounds</span> <span style="color:#f92672">=</span> {
</span></span><span style="display:flex;"><span>  <span style="color:#a6e22e">own_gun</span><span style="color:#f92672">:</span>     { <span style="color:#a6e22e">channel</span>: <span style="color:#66d9ef">0x0012</span>, <span style="color:#a6e22e">amplitude</span>: <span style="color:#66d9ef">1</span>,   <span style="color:#a6e22e">pitch</span>: <span style="color:#66d9ef">0x50</span>, <span style="color:#a6e22e">duration</span>: <span style="color:#66d9ef">2</span>   },
</span></span><span style="display:flex;"><span>  <span style="color:#a6e22e">explosion_1</span><span style="color:#f92672">:</span> { <span style="color:#a6e22e">channel</span>: <span style="color:#66d9ef">0x0011</span>, <span style="color:#a6e22e">amplitude</span>: <span style="color:#66d9ef">2</span>,   <span style="color:#a6e22e">pitch</span>: <span style="color:#66d9ef">0x96</span>, <span style="color:#a6e22e">duration</span>: <span style="color:#66d9ef">100</span> },
</span></span><span style="display:flex;"><span>  <span style="color:#a6e22e">explosion_2</span><span style="color:#f92672">:</span> { <span style="color:#a6e22e">channel</span>: <span style="color:#66d9ef">0x0010</span>, <span style="color:#a6e22e">amplitude</span>: <span style="color:#66d9ef">3</span>,   <span style="color:#a6e22e">pitch</span>: <span style="color:#66d9ef">0x07</span>, <span style="color:#a6e22e">duration</span>: <span style="color:#66d9ef">100</span> },
</span></span><span style="display:flex;"><span>  <span style="color:#a6e22e">hostile_gun</span><span style="color:#f92672">:</span> { <span style="color:#a6e22e">channel</span>: <span style="color:#66d9ef">0x0013</span>, <span style="color:#a6e22e">amplitude</span>: <span style="color:#66d9ef">4</span>,   <span style="color:#a6e22e">pitch</span>: <span style="color:#66d9ef">0x1e</span>, <span style="color:#a6e22e">duration</span>: <span style="color:#66d9ef">20</span>  },
</span></span><span style="display:flex;"><span>  <span style="color:#a6e22e">engine</span><span style="color:#f92672">:</span>      { <span style="color:#a6e22e">channel</span>: <span style="color:#66d9ef">0x0010</span>, <span style="color:#a6e22e">amplitude</span><span style="color:#f92672">:</span> <span style="color:#f92672">-</span><span style="color:#ae81ff">10</span>,  <span style="color:#a6e22e">pitch</span>: <span style="color:#66d9ef">0x05</span>, <span style="color:#a6e22e">duration</span>: <span style="color:#66d9ef">3</span>   },
</span></span><span style="display:flex;"><span>};
</span></span></code></pre></div><p>Those parameters feed into a MOS envelope processor that drives the SN76489 chip emulator, both running in an AudioWorklet on the audio thread. The chip emulator generates samples at the hardware level — tone channels with 10-bit period counters, a noise channel with a 15-bit linear feedback shift register, and a volume table with -2dB per step matching the original silicon:</p>
<div class="highlight"><pre tabindex="0" style="color:#f8f8f2;background-color:#272822;-moz-tab-size:4;-o-tab-size:4;tab-size:4;"><code class="language-typescript" data-lang="typescript"><span style="display:flex;"><span><span style="color:#a6e22e">generate</span>(<span style="color:#a6e22e">out</span>: <span style="color:#66d9ef">Float32Array</span>, <span style="color:#a6e22e">offset</span>: <span style="color:#66d9ef">number</span>, <span style="color:#a6e22e">length</span>: <span style="color:#66d9ef">number</span>, <span style="color:#a6e22e">sampleRate</span>: <span style="color:#66d9ef">number</span>)<span style="color:#f92672">:</span> <span style="color:#66d9ef">void</span> {
</span></span><span style="display:flex;"><span>  <span style="color:#66d9ef">const</span> <span style="color:#a6e22e">step</span> <span style="color:#f92672">=</span> <span style="color:#ae81ff">250000.0</span> <span style="color:#f92672">/</span> <span style="color:#a6e22e">sampleRate</span>; <span style="color:#75715e">// chip clocks per audio sample
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>
</span></span><span style="display:flex;"><span>  <span style="color:#66d9ef">for</span> (<span style="color:#66d9ef">let</span> <span style="color:#a6e22e">i</span> <span style="color:#f92672">=</span> <span style="color:#ae81ff">0</span>; <span style="color:#a6e22e">i</span> <span style="color:#f92672">&lt;</span> <span style="color:#a6e22e">length</span>; <span style="color:#a6e22e">i</span><span style="color:#f92672">++</span>) {
</span></span><span style="display:flex;"><span>    <span style="color:#66d9ef">let</span> <span style="color:#a6e22e">sample</span> <span style="color:#f92672">=</span> <span style="color:#ae81ff">0</span>;
</span></span><span style="display:flex;"><span>
</span></span><span style="display:flex;"><span>    <span style="color:#75715e">// Tone channels 0–2
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>    <span style="color:#66d9ef">for</span> (<span style="color:#66d9ef">let</span> <span style="color:#a6e22e">ch</span> <span style="color:#f92672">=</span> <span style="color:#ae81ff">0</span>; <span style="color:#a6e22e">ch</span> <span style="color:#f92672">&lt;</span> <span style="color:#ae81ff">3</span>; <span style="color:#a6e22e">ch</span><span style="color:#f92672">++</span>) {
</span></span><span style="display:flex;"><span>      <span style="color:#66d9ef">this</span>.<span style="color:#a6e22e">counter</span>[<span style="color:#a6e22e">ch</span>] <span style="color:#f92672">-=</span> <span style="color:#a6e22e">step</span>;
</span></span><span style="display:flex;"><span>      <span style="color:#66d9ef">if</span> (<span style="color:#66d9ef">this</span>.<span style="color:#a6e22e">counter</span>[<span style="color:#a6e22e">ch</span>] <span style="color:#f92672">&lt;=</span> <span style="color:#ae81ff">0</span>) {
</span></span><span style="display:flex;"><span>        <span style="color:#66d9ef">const</span> <span style="color:#a6e22e">p</span> <span style="color:#f92672">=</span> <span style="color:#66d9ef">this</span>.<span style="color:#a6e22e">period</span>[<span style="color:#a6e22e">ch</span>] <span style="color:#f92672">||</span> <span style="color:#ae81ff">1024</span>;
</span></span><span style="display:flex;"><span>        <span style="color:#66d9ef">this</span>.<span style="color:#a6e22e">counter</span>[<span style="color:#a6e22e">ch</span>] <span style="color:#f92672">+=</span> <span style="color:#a6e22e">p</span>;
</span></span><span style="display:flex;"><span>        <span style="color:#66d9ef">this</span>.<span style="color:#a6e22e">polarity</span>[<span style="color:#a6e22e">ch</span>] <span style="color:#f92672">=</span> <span style="color:#f92672">-</span><span style="color:#66d9ef">this</span>.<span style="color:#a6e22e">polarity</span>[<span style="color:#a6e22e">ch</span>];
</span></span><span style="display:flex;"><span>      }
</span></span><span style="display:flex;"><span>      <span style="color:#a6e22e">sample</span> <span style="color:#f92672">+=</span> <span style="color:#66d9ef">this</span>.<span style="color:#a6e22e">polarity</span>[<span style="color:#a6e22e">ch</span>] <span style="color:#f92672">*</span> <span style="color:#66d9ef">this</span>.<span style="color:#a6e22e">vol</span>[<span style="color:#a6e22e">ch</span>];
</span></span><span style="display:flex;"><span>    }
</span></span><span style="display:flex;"><span>
</span></span><span style="display:flex;"><span>    <span style="color:#75715e">// Noise channel — 15-bit LFSR
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>    <span style="color:#75715e">// ...
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>    <span style="color:#a6e22e">sample</span> <span style="color:#f92672">+=</span> ((<span style="color:#66d9ef">this</span>.<span style="color:#a6e22e">lfsr</span> <span style="color:#f92672">&amp;</span> <span style="color:#ae81ff">1</span>) <span style="color:#f92672">?</span> <span style="color:#ae81ff">1</span> <span style="color:#f92672">:</span> <span style="color:#f92672">-</span><span style="color:#ae81ff">1</span>) <span style="color:#f92672">*</span> <span style="color:#66d9ef">this</span>.<span style="color:#a6e22e">vol</span>[<span style="color:#ae81ff">3</span>];
</span></span><span style="display:flex;"><span>    <span style="color:#a6e22e">out</span>[<span style="color:#a6e22e">offset</span> <span style="color:#f92672">+</span> <span style="color:#a6e22e">i</span>] <span style="color:#f92672">=</span> <span style="color:#a6e22e">sample</span>;
</span></span><span style="display:flex;"><span>  }
</span></span><span style="display:flex;"><span>}
</span></span></code></pre></div><p>It&rsquo;s emulation all the way down. The MOS ticks at 100 Hz on the audio thread, processing envelopes and updating the chip registers at the same rate the real BBC hardware would have and the resulting sounds are authentic.</p>
<h2 id="the-graphics-and-levels">The Graphics and Levels</h2>
<p>The font, graphics, and level data I was able to extract from the disassembled source relatively easily. You can find <a href="https://github.com/JamesRandall/ts-thrust/tree/main/tools">a couple of tools in the source</a> that do that — one decodes the level terrain data, another extracts the ship rotation sprites by emulating the BBC&rsquo;s frame buffer and converting the output to PNGs.</p>
<p>I&rsquo;d initially tried a vector approach for the ship — just drawing it mathematically at each rotation — but it looked rough at BBC resolution as it turned out the original had hard-coded sprites for each of the 32 rotation angles, hand-optimised by Jeremy Smith to look right at each position. Once I extracted and used those actual sprites, it looked correct.</p>
<p>The terrain rendering uses the original&rsquo;s scanline-parity polygon fill — drawing every other line — which gives it that characteristic BBC Micro look. The internal resolution is 320×256, matching the original. My version has a slightly larger viewport — the original has a border around it, likely to keep the scrolling fast enough on the BBC — and I might add a toggle for that at some point.</p>
<h2 id="the-demo-mode">The Demo Mode</h2>
<p>One of the last things I added was the demo mode — the attract sequence where the game plays itself on the title screen. Digging into how the original implemented this was satisfying: it simply injects key presses into the game loop at timed intervals. There&rsquo;s no separate demo renderer — the normal game engine runs with fake inputs from a pair of parallel tables:</p>
<div class="highlight"><pre tabindex="0" style="color:#f8f8f2;background-color:#272822;-moz-tab-size:4;-o-tab-size:4;tab-size:4;"><code class="language-typescript" data-lang="typescript"><span style="display:flex;"><span><span style="color:#75715e">// Which keys to hold for each segment
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span><span style="color:#66d9ef">const</span> <span style="color:#a6e22e">DEMO_KEYPRESS_BIT_MASK_TABLE</span> <span style="color:#f92672">=</span> [
</span></span><span style="display:flex;"><span>  <span style="color:#ae81ff">0x00</span>,                          <span style="color:#75715e">//  0: freefall
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#a6e22e">INPUT_ROTATE_RIGHT</span>,            <span style="color:#75715e">//  1: rotate right
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#ae81ff">0x00</span>,                          <span style="color:#75715e">//  2: nothing
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#a6e22e">INPUT_FIRE</span>,                    <span style="color:#75715e">//  3: fire at turret
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#a6e22e">INPUT_ROTATE_LEFT</span>,             <span style="color:#75715e">//  4: rotate left
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#a6e22e">INPUT_SHIELD_TRACTOR</span>,          <span style="color:#75715e">//  5: shield/tractor
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#a6e22e">INPUT_THRUST</span> <span style="color:#f92672">|</span> <span style="color:#a6e22e">INPUT_SHIELD</span>,   <span style="color:#75715e">//  6: thrust + shield
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#75715e">// ... 18 entries total
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>];
</span></span><span style="display:flex;"><span>
</span></span><span style="display:flex;"><span><span style="color:#75715e">// How long (in game ticks) to hold each entry
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span><span style="color:#66d9ef">const</span> <span style="color:#a6e22e">demoKeypressTimerTable</span> <span style="color:#f92672">=</span> [
</span></span><span style="display:flex;"><span>  <span style="color:#ae81ff">0x18</span>,  <span style="color:#75715e">// 24 ticks of freefall
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#ae81ff">0x0F</span>,  <span style="color:#75715e">// 15 ticks rotate right
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#ae81ff">0x05</span>,  <span style="color:#75715e">//  5 ticks nothing
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#ae81ff">0x05</span>,  <span style="color:#75715e">//  5 ticks fire
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#ae81ff">0x08</span>,  <span style="color:#75715e">//  8 ticks rotate left
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#ae81ff">0x14</span>,  <span style="color:#75715e">// 20 ticks shield/tractor
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#ae81ff">0x17</span>,  <span style="color:#75715e">// 23 ticks thrust + shield
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>  <span style="color:#75715e">// ...
</span></span></span><span style="display:flex;"><span><span style="color:#75715e"></span>];
</span></span></code></pre></div><p>Three of the timer slots are randomised at the start of each demo run — small variations like <code>(rnd &amp; 0x03) + 0x08</code> for a range of 8–11 ticks, and a 75/25 split between a long and short spiral at the end. Elegant and simple: it creates just enough variation that repeated attract sequences don&rsquo;t feel mechanical.</p>
<p>Getting it working required understanding yet another layer of timing, and it exposed a small inaccuracy in the player starting position — just enough that the demo sequence missed a turret it should have hit. That led me to discover I&rsquo;d slightly miscalculated the spawn points, which in turn revealed there were multiple spawn points per level, something I&rsquo;d overlooked in the initial level decoding.</p>
<p>That this works as it does demonstrates that the physics recreation is accurate - if it wasn&rsquo;t timed keypresses would result in different behaviours and its unlikely the shot would hit the turret and the player escape with the pod.</p>
<h2 id="the-teleport-animation">The Teleport Animation</h2>
<p>One moment that impressed me with the coding assistant: the teleport animation — the effect when you warp into a level — wasn&rsquo;t matching the original based on the spec I&rsquo;d extracted from the disassembly. Rather than spend more time on the code, I recorded the original game as a video, captured the animation frames, pasted them into Claude Code and said &ldquo;recreate that.&rdquo; It nailed it almost perfectly in about five minutes. Not hard code — something I could have done in half an hour — but a good example of where AI saves time on the uninteresting stuff so you can focus on the interesting stuff.</p>
<h2 id="the-crt-effects">The CRT Effects</h2>
<p>To round things off I added a few CRT post-processing effects: scanlines, green phosphor, amber phosphor, black and white TV, and a VCR look. These are implemented as WebGPU compute shaders in WGSL, falling back gracefully when WebGPU isn&rsquo;t available. Nothing particularly difficult — I pulled most of them from my Elite conversion and added the black and white filter.</p>
<p>I didn&rsquo;t get much time to play the BBC on a colour TV. When I first got one I was playing on a tiny 12-inch black and white set, and later a small green screen monitor. The filters are just a bit of fun, but they do give it an authentic feel.</p>
<h2 id="what-this-was-really-about">What This Was Really About</h2>
<p>The interesting thing about this process wasn&rsquo;t writing the code. The code is straightforward — by modern standards, a 1986 game that ran in 32K is not particularly complicated. That&rsquo;s not a slight on the original developer and it&rsquo;s amazing that Jeremy Smith got this working on an 8-bit machine, and Exile is something else entirely. But with a high-level language and all the power we have today, the resources online, the coding tools then the implementation is the easy part.</p>
<p>What was interesting was the understanding. Using AI to drill into the original 6502 assembly, to extract and document the subsystems, to understand the specific timings and fixed-point arithmetic and hardware interfaces — that&rsquo;s where the value was. The recreation forced me to understand every system deeply, because getting the feel right meant getting the details right.</p>
<p>AI couldn&rsquo;t recreate Thrust for me — that was proved pretty conclusively in the first five minutes. But it could help me understand the original well enough to recreate it myself.</p>
<p>The source is <a href="https://github.com/JamesRandall/ts-thrust">on GitHub</a> and you can <a href="https://www.jamesdrandall.com/thrust/">play it here</a>. Going through these codebases from the 8-bit era gives you real respect for the developers. It&rsquo;s amazing what they squeezed into such limited hardware. There&rsquo;s also a <a href="https://youtu.be/mzytBDzlqrY">YouTube video</a> I created on the process.</p>
<p>I really enjoyed it. I played this game a lot when I was young and it&rsquo;s great to have gained this understanding of how it really works - having done so I appreciate the work Jeremy Smith did even more.</p>
<div role="list" class="grid sm:grid-cols-4 lg:grid-cols-4 gap-8 mt-8">
    <a href="/projects/thrust/images/0.jpg"><img src="/projects/thrust/images/0.jpg" /></a>
    <a href="/projects/thrust/images/1.jpg"><img src="/projects/thrust/images/1.jpg" /></a>
    <a href="/projects/thrust/images/2.jpg"><img src="/projects/thrust/images/2.jpg" /></a>
    <a href="/projects/thrust/images/3.jpg"><img src="/projects/thrust/images/3.jpg" /></a>
</div>

</div>
        <div class="my-8 border border-gray-300 border-l-4 bg-gray-50 p-4 promo:p-5" style="border-left-color:#059669">
  <div class="flex flex-col promo:flex-row promo:items-center gap-4 promo:gap-5">
    <img
      src="/annhex-gameplay-wide.jpg"
      alt="Annhexation gameplay — a hex-based 4X strategy map"
      class="w-full h-40 object-cover border border-gray-300 promo:hidden" />
    <img
      src="/annhex-gameplay.jpg"
      alt="Annhexation gameplay — a hex-based 4X strategy map"
      class="hidden promo:block promo:w-32 promo:h-32 flex-shrink-0 object-cover border border-gray-300" />
    <div class="flex flex-col">
      <div class="flex items-center flex-wrap gap-x-2 gap-y-1">
        <span class="text-lg promo:text-xl font-extrabold tracking-tight text-gray-900">Annhexation</span>
        <span class="text-xs font-semibold uppercase tracking-wide text-green-800 bg-green-100 px-2 py-0.5 rounded">Early access</span>
      </div>
      <p class="mt-1 text-sm promo:text-base text-gray-600 leading-snug">Forty-two years after I first started programming, I built a browser-native 4X from scratch &mdash; a custom WebGPU engine, eight civilisations, and an AI opponent I'm still teaching to play. No install, no sign-up. Play it right now.</p>
      <div class="mt-3 flex flex-col promo:flex-row promo:flex-wrap gap-2">
        <a
          href="https://annhexation.com"
          class="inline-flex items-center justify-center promo:justify-start gap-2 rounded-md bg-green-600 hover:bg-green-500 px-4 py-2 text-sm font-semibold text-white transition duration-150 ease-in-out">
          <svg class="h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path d="M6.3 3.5A1 1 0 0 0 4.75 4.34v11.32a1 1 0 0 0 1.55.84l8.49-5.66a1 1 0 0 0 0-1.68L6.3 3.5Z"/></svg>
          Play free in browser
        </a>
        <a
          href="https://store.steampowered.com/app/4663920/Annhexation/"
          class="inline-flex items-center justify-center promo:justify-start gap-2 rounded-md border border-gray-400 hover:border-gray-500 hover:bg-gray-100 px-4 py-2 text-sm font-semibold text-gray-900 transition duration-150 ease-in-out">
          <svg class="h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M9.05 2.93a1.06 1.06 0 0 1 1.9 0l1.83 3.72 4.1.6a1.06 1.06 0 0 1 .59 1.8l-2.97 2.9.7 4.08a1.06 1.06 0 0 1-1.54 1.12L10 15.31l-3.66 1.92a1.06 1.06 0 0 1-1.54-1.11l.7-4.09-2.97-2.9a1.06 1.06 0 0 1 .59-1.8l4.1-.6 1.83-3.71Z"/></svg>
          Wishlist on Steam
        </a>
      </div>
    </div>
  </div>
</div>

      </div>      
    </div>
  </div>  
</main>

<div class="container mx-auto mt-6 mb-6 sm:mb-16 sm:mt-12">
  <div class="flex flex-col justify-start items-center">
    <span class="footer sm:mx-12 text-center mt-1 sm:mt-3">
      <span>Built by James Randall — tool-maker, system builder, and occasional cyclist.</span>
      <span class="block">Walking the hills with my four-legged friend when I'm not building worlds.</span>
    </span>
    <div class="flex flex-row justify-end items-center mt-2 sm:mt-6">
      <a href="/index.xml">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" class="h-8 text-gray-600 hover:text-indigo-600 mx-3">
  <path fill="currentColor" d="M128.081 415.959c0 35.369-28.672 64.041-64.041 64.041S0 451.328 0 415.959s28.672-64.041 64.041-64.041 64.04 28.673 64.04 64.041zm175.66 47.25c-8.354-154.6-132.185-278.587-286.95-286.95C7.656 175.765 0 183.105 0 192.253v48.069c0 8.415 6.49 15.472 14.887 16.018 111.832 7.284 201.473 96.702 208.772 208.772.547 8.397 7.604 14.887 16.018 14.887h48.069c9.149.001 16.489-7.655 15.995-16.79zm144.249.288C439.596 229.677 251.465 40.445 16.503 32.01 7.473 31.686 0 38.981 0 48.016v48.068c0 8.625 6.835 15.645 15.453 15.999 191.179 7.839 344.627 161.316 352.465 352.465.353 8.618 7.373 15.453 15.999 15.453h48.068c9.034-.001 16.329-7.474 16.005-16.504z"/>
</svg>