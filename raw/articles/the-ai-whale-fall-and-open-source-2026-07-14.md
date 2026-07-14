---
source_url: https://minor.gripe/posts/2026-07-13-the_ai_whalefall_and_open_source/
ingested: 2026-07-14
sha256: a44d9f6559b99ce7f9d80a1f5b59ea59b3435bb01168742e80988e4e59b86c3d
blog_source: Hacker News AI
---
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-us" lang="en-us">
<head>
    










    







<script defer language="javascript" type="text/javascript" src="/js/bundle.min.5991d603939a6d188be342b278a4555db90f163903158c623d2c39fde3d82cb3.js"></script>



<script defer data-domain="minor.gripe" src="https://plausible.io/js/script.js"></script>




    
    <meta http-equiv="content-type" content="text/html; charset=utf-8">

    
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    
    <link rel="icon" href=/favicon.png>

    
    





  





  
  
  


<!-- Open Graph image and Twitter Card metadata -->

<title itemprop="name">Minor Gripe - The AI Whale Fall and Open Source</title>
<meta property="og:title" content=Minor&#32;Gripe&#32;-&#32;The&#32;AI&#32;Whale&#32;Fall&#32;and&#32;Open&#32;Source />
<meta name="twitter:title" content=Minor&#32;Gripe&#32;-&#32;The&#32;AI&#32;Whale&#32;Fall&#32;and&#32;Open&#32;Source />
<meta itemprop="name" content=Minor&#32;Gripe&#32;-&#32;The&#32;AI&#32;Whale&#32;Fall&#32;and&#32;Open&#32;Source />
<meta name="application-name" content=Minor&#32;Gripe&#32;-&#32;The&#32;AI&#32;Whale&#32;Fall&#32;and&#32;Open&#32;Source />
<meta property="og:site_name" content="" />


<meta name="description" content="" />
<meta itemprop="description" content="" />
<meta property="og:description" content="" />
<meta name="twitter:description" content="" />


<base href="https://minor.gripe/posts/2026-07-13-the_ai_whalefall_and_open_source/" />
<link rel="canonical" href="https://minor.gripe/posts/2026-07-13-the_ai_whalefall_and_open_source/" itemprop="url" />
<meta name="url" content="https://minor.gripe/posts/2026-07-13-the_ai_whalefall_and_open_source/" />
<meta name="twitter:url" content="https://minor.gripe/posts/2026-07-13-the_ai_whalefall_and_open_source/" />
<meta property="og:url" content="https://minor.gripe/posts/2026-07-13-the_ai_whalefall_and_open_source/" />


<meta property="og:updated_time" content="2026-07-13T16:24:05-05:00" />


<link rel="sitemap" type="application/xml" title="Sitemap" href='https://minor.gripe/sitemap.xml' />

<meta name="robots" content="index,follow" />
<meta name="googlebot" content="index,follow" />



  
    <meta name="twitter:site" content="@crertel" />
    <meta name="twitter:creator" content="@crertel" />

<meta property="fb:admins" content="" />


<meta name="apple-mobile-web-app-title" content="" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="black" />






<meta name="generator" content="Hugo 0.145.0">


    
    

<link type="text/css" rel="stylesheet" href="/css/bundle.min.ebb7214fb8b0958dceb150c2734d55b43a25bc7b5db07425fdc9b00e80560390.css">


    
    <style>
    body {
        --sidebar-bg-color: #202020;
        --sidebar-img-border-color: #515151;
        --sidebar-p-color: #909090;
        --sidebar-h1-color: #FFF;
        --sidebar-a-color: #FFF;
        --sidebar-socials-color: #FFF;
        --text-color: #222;
        --bkg-color: #FAF9F6;
        --post-title-color: #303030;
        --list-color: #5A5A5A;
        --link-color: #268BD2;
        --date-color: #515151;
        --table-border-color: #E5E5E5;
        --table-stripe-color: #F9F9F9;
        --code-color: #000;
        --code-background-color: #E5E5E5;
        --code-block-color: #FFF;
        --code-block-background-color: #272822;
        --moon-sun-color: #FFF;
        --moon-sun-background-color: #515151;
    }
    body.dark-theme {
        --text-color: #EEE;
        --bkg-color: #121212;
        --post-title-color: #DBE2E9;
        --list-color: #9D9D9D;
        --link-color: #268BD2;
        --date-color: #9A9A9A;
        --table-border-color: #515151;
        --table-stripe-color: #202020;
        --code-color: #FFF;
        --code-background-color: #515151;
        --code-block-color: #FFF;
        --code-block-background-color: #272822;
    }
    body {
        background-color: var(--bkg-color);
    }
</style>

</head>

    <body class="dark-theme">
        <div class="wrapper">
            <aside class="sidebar">
    <div class="container sidebar-sticky">
        <div class="light-dark" align="right">
    <button class="btn-light-dark" title="Toggle light/dark mode">
        <svg class="moon" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 16 16">
            <path fill="currentColor" d="M6 .278a.768.768 0 0 1 .08.858a7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277c.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316a.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71C0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z"/>
        </svg>
        <svg class="sun" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 16 16">
            <path fill="currentColor" d="M8 12a4 4 0 1 0 0-8a4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z"/>
        </svg>
    </button>
</div>

        <div class="sidebar-about">
    <h1 class="brand">
        
        
            <a href="https://minor.gripe/">
                <h1>Minor Gripe</h1>
            </a>
        
    </h1>
    <p class="lead">
    
    </p>
</div>

        <nav>
    <ul class="sidebar-nav">

        
        
        
        
            

            
                
                
            
            
                
                
                        
                
                        
                
                        
                
                        
                
            
                
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
            
        
        
            

            
                
                
                    <li class="heading">
                        <a href="/posts/">Posts</a>
                    </li>
                    
                        <li class="sub-heading">
                            Recent
                        </li>
                        
                            <li class="bullet">
                                <a href="https://minor.gripe/posts/2026-07-13-the_ai_whalefall_and_open_source/">The AI Whale Fall and Open Source</a>
                            </li>
                        
                            <li class="bullet">
                                <a href="https://minor.gripe/posts/2026-03-23-against_open_sources_anthropocentrism/">Against Open Source&#39;s Anthropocentrism</a>
                            </li>
                        
                            <li class="bullet">
                                <a href="https://minor.gripe/posts/2026-03-13-millwright_smarter_tool_selection_with_adaptive_toolsheds/">Millwright: Smarter Tool Selection From Agent Experience</a>
                            </li>
                        
                            <li class="bullet">
                                <a href="https://minor.gripe/posts/2026-03-11-my_friend_ellem/">My Friend Ellem</a>
                            </li>
                        
                            <li class="bullet">
                                <a href="https://minor.gripe/posts/2026-03-09-gremlins_ideas_for_cogitation_and_actuation/">Gremlins: Ideas for Cogitation and Actuation</a>
                            </li>
                        
                    
                
            
            
                
                
                        
                
                        
                
                        
                
                        
                
            
                
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
            
        
        
            

            
                
                
            
            
                
                    <li class="heading">
                        <a href="/series/">Series</a>
                    </li>
                
                
                        
                
                        
                
                        
                
                        
                
            
                
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
            
        
        
            

            
                
                
            
            
                
                
                        
                
                        
                
                        
                
                        
                
            
                
                    <li class="heading">
                        <a href="/tags/">Tags</a>
                    </li>
                
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
                        
                
            
        

    </ul>
</nav>

        
    <a target="_blank" class="social" title="GitHub" href="https://github.com/crertel">
        <svg xmlns="http://www.w3.org/2000/svg" width="1.2em" height="1.2em" viewBox="-2 -2 24 24">
            <path fill="currentColor" d="M18.88 1.099C18.147.366 17.265 0 16.233 0H3.746C2.714 0 1.832.366 1.099 1.099C.366 1.832 0 2.714 0 3.746v12.487c0 1.032.366 1.914 1.099 2.647c.733.733 1.615 1.099 2.647 1.099H6.66c.19 0 .333-.007.429-.02a.504.504 0 0 0 .286-.169c.095-.1.143-.245.143-.435l-.007-.885c-.004-.564-.006-1.01-.006-1.34l-.3.052c-.19.035-.43.05-.721.046a5.555 5.555 0 0 1-.904-.091a2.026 2.026 0 0 1-.872-.39a1.651 1.651 0 0 1-.572-.8l-.13-.3a3.25 3.25 0 0 0-.41-.663c-.186-.243-.375-.407-.566-.494l-.09-.065a.956.956 0 0 1-.17-.156a.723.723 0 0 1-.117-.182c-.026-.061-.004-.111.065-.15c.07-.04.195-.059.378-.059l.26.04c.173.034.388.138.643.311a2.1 2.1 0 0 1 .631.677c.2.355.44.626.722.813c.282.186.566.28.852.28c.286 0 .533-.022.742-.065a2.59 2.59 0 0 0 .585-.196c.078-.58.29-1.028.637-1.34a8.907 8.907 0 0 1-1.333-.234a5.314 5.314 0 0 1-1.223-.507a3.5 3.5 0 0 1-1.047-.872c-.277-.347-.505-.802-.683-1.365c-.177-.564-.266-1.215-.266-1.952c0-1.049.342-1.942 1.027-2.68c-.32-.788-.29-1.673.091-2.652c.252-.079.625-.02 1.119.175c.494.195.856.362 1.086.5c.23.14.414.257.553.352a9.233 9.233 0 0 1 2.497-.338c.859 0 1.691.113 2.498.338l.494-.312a6.997 6.997 0 0 1 1.197-.572c.46-.174.81-.221 1.054-.143c.39.98.424 1.864.103 2.653c.685.737 1.028 1.63 1.028 2.68c0 .737-.089 1.39-.267 1.957c-.177.568-.407 1.023-.689 1.366a3.65 3.65 0 0 1-1.053.865c-.42.234-.828.403-1.223.507a8.9 8.9 0 0 1-1.333.235c.45.39.676 1.005.676 1.846v3.11c0 .147.021.266.065.357a.36.36 0 0 0 .208.189c.096.034.18.056.254.064c.074.01.18.013.318.013h2.914c1.032 0 1.914-.366 2.647-1.099c.732-.732 1.099-1.615 1.099-2.647V3.746c0-1.032-.367-1.914-1.1-2.647z"/>
        </svg>
    </a>





    <a target="_blank" class="social" title="X" href="https://x.com/crertel">
        <svg xmlns="http://www.w3.org/2000/svg" width="1.1em" height="1.1em" viewBox="0 0 512 472.799">
            <path fill="currentColor" d="M403.229 0h78.506L310.219 196.04 512 462.799H354.002L230.261 301.007 88.669 462.799h-78.56l183.455-209.683L0 0h161.999l111.856 147.88L403.229 0zm-27.556 415.805h43.505L138.363 44.527h-46.68l283.99 371.278z"/>
        </svg>
    </a>













    <a target="_blank" class="social" title="RSS Feed" href="/posts/index.xml">
        <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1.2em" viewBox="0 0 1280.000000 1280.000000">
            <g transform="translate(0.000000,1280.000000) scale(0.100000,-0.100000)" fill="currentColor">
                <path d="M2295 11929 c-284 -12 -642 -45 -707 -65 -17 -5 -18 -63 -18 -1039 0 -569 4 -1036 8 -1039 5 -3 74 6 153 19 510 86 1168 95 1789 25 1348 -153 2602 -677 3670 -1531 385 -308 820 -744 1126 -1129 842 -1060 1362 -2313 1514 -3650 70 -621 61 -1279 -25 -1789 -13 -79 -22 -148 -19 -153 3 -4 471 -8 1039 -8 l1035 0 5 23 c51 225 85 942 67 1419 -23 605 -77 1044 -198 1617 -294 1400 -927 2734 -1823 3846 -1043 1295 -2364 2259 -3909 2854 -1158 447 -2451 656 -3707 600z"/>
                <path d="M2255 7845 c-269 -25 -620 -81 -667 -106 -17 -9 -18 -55 -18 -899 0 -706 3 -890 13 -890 6 0 66 18 132 41 130 44 288 79 467 105 154 21 577 30 749 15 1207 -107 2267 -823 2814 -1902 166 -327 268 -637 330 -1001 38 -227 48 -384 42 -662 -8 -348 -44 -590 -126 -831 -23 -66 -41 -126 -41 -132 0 -10 184 -13 890 -13 844 0 890 1 899 18 27 50 88 452 110 725 14 162 14 624 1 782 -59 703 -233 1323 -545 1945 -481 956 -1313 1788 -2270 2268 -620 310 -1239 483 -1940 542 -165 14 -669 10 -840 -5z"/>
                <path d="M2519 3815 c-391 -66 -725 -336 -868 -703 -79 -201 -96 -462 -45 -677 83 -344 338 -641 666 -774 116 -47 205 -69 330 -80 412 -39 811 153 1040 500 193 292 240 648 128 981 -135 403 -492 699 -914 757 -100 14 -241 12 -337 -4z"/>
            </g>
        </svg>
    </a>


    <a target="_blank" class="social" title="Email" href="mailto:chris@minor.gripe">
       <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1.2em" viewBox="0 0 485.211 485.211">
            <path fill="currentColor" d="M301.393,241.631L464.866,424.56H20.332l163.474-182.928l58.801,51.443L301.393,241.631z M462.174,60.651H23.027 l219.579,192.142L462.174,60.651z M324.225,221.67l160.986,180.151V80.792L324.225,221.67z M0,80.792v321.029L160.972,221.64 L0,80.792z"/>
       </svg>
    </a>




        <p class="footnote">
powered by <a target="_blank" href="https://gohugo.io">Hugo</a> | themed with <a target="_blank" href="https://github.com/lukeorth/poison">poison</a>
    <br>
    &copy; 2026 . All rights reserved.
</p>

  </div>
</aside>

            <main class="content container">
                <div class="post">
  <div class="info">
  <h1 class="post-title">
    <a href="https://minor.gripe/posts/2026-07-13-the_ai_whalefall_and_open_source/">The AI Whale Fall and Open Source</a>
  </h1>

  <div class="headline">
    <div>
      
      
      <time datetime=" 2026-07-13T16:24:05-0500" class="post-date">
        July 13, 2026
      </time>
      
      <span> - </span>
      <span class="reading-time">
        
          
        

        <span>5 mins read</span>
      </span>
    </div>

    
    <ul class="tags">
      
      <li class="tag-ai">
        <a href="https://minor.gripe/tags/ai">ai</a>
      </li>
      
      <li class="tag-genai">
        <a href="https://minor.gripe/tags/genai">genai</a>
      </li>
      
      <li class="tag-practices">
        <a href="https://minor.gripe/tags/practices">practices</a>
      </li>
      
      <li class="tag-policy">
        <a href="https://minor.gripe/tags/policy">policy</a>
      </li>
      
      <li class="tag-rant">
        <a href="https://minor.gripe/tags/rant">rant</a>
      </li>
      
    </ul>
    
  </div>

  
  

  
</div>

  <p>Frontier labs are subsidizing AI usage, and we&rsquo;d be fools not to use it to improve the state of open source while that holds out.</p>
<h2 id="how-are-whales-like-frontier-labs">How are whales like frontier labs?</h2>



<aside class="aside-default collapsible">
    
    <details>
        <summary>
            <strong>Aside</strong>
        </summary>
        <div class="aside-content">
            Arguably, whales are more like the <em>institutional investors</em> in frontier labs, but that&rsquo;s neither here nor there.
        </div>
        </details>
        
</aside>
<p>A <a href="https://en.wikipedia.org/wiki/Whale_fall" target="_blank">whale fall</a> is the bloom of an ecosystem when the carcass of a whale sinks and lands on the ocean floor, providing food and spurring the creation of new life.</p>
<p>Right now, critics of AI as currently being commercialized will tell you that labs like Anthropic and OpenAI cannot possibly last given the huge sums of money (hundreds of billions in some cases) that somehow must be paid back. They will say that the financial engineering underpinning these orgs has temporarily given a reprieve from market forces, and that is the <em>only</em> reason you can waste time making slop without paying through the nose for the privilege. I&rsquo;m not entirely sure that that is the case, but let&rsquo;s take it as true.</p>
<p>From personal experience as well as that of many <a href="https://github.com/macton/differentiable-collisions-optc" target="_blank">experienced</a> <a href="https://antirez.com/news/158" target="_blank">developers</a>, AI can be a useful tool when writing or maintaining code. I&rsquo;ll write more on this some other time, but there is very clearly a there there and anybody saying otherwise is living in some different reality.</p>
<p>So, we get two things:</p>
<ol>
<li>AI is a useful tool.</li>
<li>AI is a tool that will only be available for a limited time.</li>
</ol>



<aside class="aside-default collapsible">
    
    <details>
        <summary>
            <strong>Aside</strong>
        </summary>
        <div class="aside-content">
            <p>Now, <em>personally</em>, the limited-time thing I think is bullshit&ndash;but, I&rsquo;ll allow it for rhetorical reasons here.</p>
<p>Most-all of the people I&rsquo;ve talked to that are strongly anti-LLM and anti-AI are oddly silent on the subject of models like GLM 5.2 and other modern open-weight models that are &ldquo;good enough&rdquo; for assistance now, and in another year will likely be as good as Fable or 5.6 today. I suspect this is because they are <em>larpers</em> and aren&rsquo;t actually keeping track of the technology.</p>
<p>These same people seem to believe that AI/LLMs, if the bubble bursts, will all just spontaneously disappear and delete themselves from the collective storage of the universe, to presumably be followed by the expensive graphics cards and CPUs and FPGAs that can run them.</p>
<p>As a friend wryly observed:</p>
<blockquote>
<p>Ah yes, it is well-known that after the 2008 sub-prime collapse everybody stopped living in houses.</p></blockquote>

        </div>
        </details>
        
</aside>
<p>The whale carcass will not last forever on the ocean floor, nor too shall the over-leveraged frontier lab. But, in the meantime, there&rsquo;s a chance for the rest of us to pick those tokens clean.</p>
<h2 id="a-feast-of-tokens-if-we-but-choose-to-eat">A feast of tokens, if we but choose to eat</h2>
<p>You&rsquo;ve probably seen some version of the <a href="https://imgs.xkcd.com/comics/dependency_2x.png" target="_blank">classic XKCD image</a>, where there&rsquo;s a tower of babel of software and the critical jenga piece it all happens to be supported by is maintained by some quiet developer in the middle of nowhere. There are a <em>lot</em> of those projects, and honestly, we ain&rsquo;t getting any younger.</p>
<p>Even in theoretically &ldquo;young&rdquo; (flagrantly false in this case, but bear with me) projects like NixOS, you can end up with open PRs (not to mention <em>issues</em>!) numbering in the low <a href="https://github.com/NixOS/nixpkgs/pulls" target="_blank">tens of thousands</a>. These same projects will also then frequently complain about the lack of available manpower.</p>
<p>There are things that I wouldn&rsquo;t trust to an AI right now. I don&rsquo;t think, for example, that large architectural rewrites or feature additions for projects that are meant to be building blocks for other projects are best left to the vibes.</p>
<p>For mechanical work&ndash;things like bumping versions, fixing failing tests, checking documentation for inconsistencies&ndash;the clankers have proven their worth (even before LLMs, anybody remember dependabot?)! <strong>A <em>large part</em> of the technical debt (and debt in developer ergonomics) for these projects is something that could be remediated using these models.</strong></p>
<p>In projects like NixOS&rsquo; nixpkgs, we already make heavy use of automation (<code>r-ryantm</code> and friends) and mechanical verification and CI. Those deterministic systems make improving tests and suggesting minor PR refactors and things <em>even safer</em>. It makes it <em>even easier</em> to trust the contributions of clankers.</p>
<p><strong>We should all be making hay while the sun shines.</strong></p>



<aside class="aside-default collapsible">
    
    <details>
        <summary>
            <strong>Aside</strong>
        </summary>
        <div class="aside-content">
            <p>Another community I&rsquo;ve long been a member of&ndash;the Elixir community&ndash;has been somewhat at the forefront here.</p>
<p>If you look at work done by Jose Valim (in marked contrast to, say, Andrew Kelley and how he&rsquo;s handling Zig) and other folks in the Elixir community (Chris McCord, Isaac Yonemoto, Zach Daniels, myself, others), there&rsquo;s a clear embrace of these tools.</p>
<p>It isn&rsquo;t done uncritically&ndash;<a href="https://x.com/josevalim/status/2048698752077025743" target="_blank">Valim himself commented on this during a conference</a>&ndash;but that it is being done <em>at all</em> has yielded and will yield dividends far beyond what we could&rsquo;ve imagined even five years ago.</p>

        </div>
        </details>
        
</aside>
<h2 id="how-to-make-hay">How to make hay</h2>
<p>Random drive-by PRs from clawbots are a real concern for some maintainers (who we should try to help) and are convenient cover for the larpers (who are bozos and should be ignored). &ldquo;We can barely keep on top of the PRs as it is!&rdquo; &ldquo;We don&rsquo;t want to argue with a bot!&rdquo; &ldquo;Issue trackers are for humans only!&rdquo;, etc. I won&rsquo;t deny that can be frustrating.</p>
<p>The way to <em>fix</em> that, of course, is automated processes and mechanical guardrails. Automatic enforcement of style, automatic testing and linting and formatting&ndash;same as ever. If your community review process can&rsquo;t stand up to a clanker, it wasn&rsquo;t going to stand up to a flood of quarrelsome first-time contributors that <em>really wanted</em> their PRs merged.</p>
<p><em>We can use the whale fall tokens to build that machinery</em>. Doing so makes it easier to manage the clanker collaboration down the road&ndash;and there&rsquo;s no future where some degree of clanking does not occur, outside of projects that have decided to follow in the footsteps of the Amish (and even the Amish will selectively, slowly, adopt some good bits of what the English do!).</p>
<p>Whale bones last for decades and even after the fall has been picked clean they function as valuable infrastructure for the opportunists&rsquo; descendants. <strong>We need to use the whale fall to build the tools to make our futures easier, and that can be done even without trying to solve for external clanker contributors.</strong></p>


  <p class="submit-links">
    Want to discuss this post? |
    <a href="mailto:chris@minor.gripe?subject=Re:The%20AI%20Whale%20Fall%20and%20Open%20Source&amp;body=Regarding:https%3A%2F%2Fminor.gripe%2Fposts%2F2026-07-13-the_ai_whalefall_and_open_source%2F">Discuss via email</a> |
    <a href="https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fminor.gripe%2Fposts%2F2026-07-13-the_ai_whalefall_and_open_source%2F&amp;t=The%20AI%20Whale%20Fall%20and%20Open%20Source" target="_blank" rel="noopener">Hacker News</a> |
    <a href="https://lobste.rs/stories/new?url=https%3A%2F%2Fminor.gripe%2Fposts%2F2026-07-13-the_ai_whalefall_and_open_source%2F&amp;title=The%20AI%20Whale%20Fall%20and%20Open%20Source" target="_blank" rel="noopener">Lobsters</a> |
  </p>
  
  
  <hr>
<div class="footer">
    
	    
            <a class="previous-post" href="https://minor.gripe/posts/2026-03-23-against_open_sources_anthropocentrism/?ref=footer"><span style="font-weight:bold;">Â« Previous</span><br>Against Open Source&#39;s Anthropocentrism</a>
        
	    
    
</div>

  
</div>
            </main>
            

<div class="article-toc ">
    <div class="toc-wrapper">
      <h4 id="contents"></h4>
      <nav id="TableOfContents">
  <ul>
    <li><a href="#how-are-whales-like-frontier-labs">How are whales like frontier labs?</a></li>
    <li><a href="#a-feast-of-tokens-if-we-but-choose-to-eat">A feast of tokens, if we but choose to eat</a></li>
    <li><a href="#how-to-make-hay">How to make hay</a></li>
  </ul>
</nav>
    </div>
</div>



        </div>
    </body>
</html>
