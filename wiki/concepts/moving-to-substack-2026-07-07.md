---
type: concept
title: Moving To Substack 2026 07 07
description: Auto-generated wiki page
created: 2026-07-07
updated: 2026-07-07
tags: [llm-wiki, knowledge-base]
sources: [raw/articles/moving-to-substack-2026-07-07.md]
confidence: medium
links: []
---
# Moving To Substack 2026 07 07

> **Source:** [moving-to-substack-2026-07-07.md](http://jalammar.github.io/moving_to_substack/)
> **Relevance:** medium
> **Type:** concept

---

---

source_url: http://jalammar.github.io/moving_to_substack/
ingested: 2026-07-07
sha256: PLACEHOLDER
blog_source: Jay Alammar
---

<!DOCTYPE html>
<html>
  <head>
    <title>Moving To Substack – Jay Alammar – Visualizing machine learning one concept at a time.</title>

        <meta charset="utf-8" />
    <meta content='text/html; charset=utf-8' http-equiv='Content-Type'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0'>

    
    <meta name="description" content="I’m freezing this blog and starting to post on my Substack instead. The authoring experience is much more convenient for me there. Please follow me there, and check out The Illustrated DeepSeek R-1 if you haven’t yet.

And check out our How Transformer LLMs Work course!


" />
    <meta property="og:description" content="I’m freezing this blog and starting to post on my Substack instead. The authoring experience is much more convenient for me there. Please follow me there, and check out The Illustrated DeepSeek R-1 if you haven’t yet.

And check out our How Transformer LLMs Work course!


" />
    
    <meta name="author" content="Jay Alammar" />

    
    <meta property="og:title" content="Moving To Substack" />
    <meta property="twitter:title" content="Moving To Substack" />
    

    <!--[if lt IE 9]>
      <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <script src="/js/jquery-3.1.1.slim.min.js"></script>
    <script type="text/javascript" src="/js/d3.min.js"></script>
    <script type="text/javascript" src="/js/d3-selection-multi.v0.4.min.js"></script>
    <script type="text/javascript" src="/js/d3-jetpack.js"></script>

    <link rel="stylesheet" href="/css/bootstrap.min.css" />
    <link rel="stylesheet" href="/css/bootstrap-theme.min.css" />
    <script src="/js/bootstrap.min.js" > </script>

    <link rel="stylesheet" type="text/css" href="/bower_components/jquery.gifplayer/dist/gifplayer.css"/>
    <script type="text/javascript" src="/bower_components/jquery.gifplayer/dist/jquery.gifplayer.js"></script>

    <!--
    <script data-main="scripts/main" src="scripts/require.js"></script>
    -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/katex.min.css" integrity="sha384-wE+lCONuEo/QSfLb4AfrSk7HjWJtc4Xc1OiB2/aDBzHzjnlBP4SX7vjErTcwlA8C" crossorigin="anonymous">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/katex.min.js" integrity="sha384-tdtuPw3yx/rnUGmnLNWXtfjb9fpmwexsd+lr6HUYnUY4B7JhB5Ty7a1mYd+kto/s" crossorigin="anonymous"></script>

    <link rel="stylesheet" type="text/css" href="/style.css" />
    <link rel="alternate" type="application/rss+xml" title="Jay Alammar - Visualizing machine learning one concept at a time." href="/feed.xml" />

    <meta name="viewport" content="width=device-width">
    <!-- Created with Jekyll Now - http://github.com/barryclark/jekyll-now -->

    <!-- Piwik -->
    <!-- Piwik
    <script type="text/javascript">
        var _paq = _paq || [];
        _paq.push(["setDomains", ["*.example.org"]]);
        _paq.push(['trackPageView']);
        _paq.push(['enableLinkTracking']);
        (function() {
            var u="https://a.jalammar.com/";
            _paq.push(['setTrackerUrl', u+'piwik.php']);
            _paq.push(['setSiteId', '1']);
            var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
            g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'piwik.js'; s.parentNode.insertBefore(g,s);
        })();
    </script>
    <noscript><p><img src="https://a.jalammar.com/piwik.php?idsite=1" style="border:0;" alt="" /></p></noscript>-->
    <!-- End Piwik Code -->

    <!-- End Piwik Code -->
  </head>

  <body>
    <div class="wrapper-masthead">
      <div class="container">
        <header class="masthead clearfix">
          <a href="/" class="site-avatar"><img src="https://avatars0.githubusercontent.com/u/1007956?s=460&v=4" /></a>

          <div class="site-info">
            <h1 class="site-name"><a href="/">Jay Alammar</a></h1>
            <p class="site-description">Visualizing machine learning one concept at a time.<br />Read our book, <a href="https://www.LLM-book.com">Hands-On Large Language Models</a> and follow me on <a href="https://www.linkedin.com/in/jalammar/">LinkedIn</a>, <a href="https://bsky.app/profile/jayalammar.bsky.social">Bluesky</a>, <a href="https://newsletter.languagemodels.co/">Substack</a>, <a href="https://x.com/JayAlammar">X</a>,<a href="https://www.youtube.com/channel/UCmOwsoHty5PrmE-3QhUBfPQ">YouTube </a></p>
          </div>

          <nav>
            <a href="/">Blog</a>
            <a href="/about">About</a>
          </nav>
        </header>
      </div>
    </div>

    <div id="main" role="main" class="container">
      <article class="post">
  <h1>Moving To Substack</h1>

  <div class="entry prediction">
    <p>I’m freezing this blog and starting to post on <a href="https://newsletter.languagemodels.co/">my Substack</a> instead. The authoring experience is much more convenient for me there. Please follow me there, and check out <a href="https://newsletter.languagemodels.co/p/the-illustrated-deepseek-r1">The Illustrated DeepSeek R-1</a> if you haven’t yet.</p>

<p>And check out our <a href="https://bit.ly/4aRnn7Z">How Transformer LLMs Work</a> course!</p>

<iframe width="560" height="315" style="
width: 100%;
max-width: 560px;" src="https://www.youtube.com/embed/k1ILy23t89E?si=M84_P9i1mAzCtTDD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen=""></iframe>

  </div>

  <div class="date">
    Written on March 26, 2025
  </div>

  
</article>

    </div>

    <div style="display: flex; justify-content: center; align-items: center; margin-top: 20px;">
  <iframe src="https://newsletter.languagemodels.co/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>
    </div>

<div style="padding: 10px 0 10px 3%; color: #555; font-size:85%">
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

<br/>
Attribution example:
<br/>
<i>Alammar, J (2018). The Illustrated Transformer [Blog post]. Retrieved from <a href="https://jalammar.github.io/illustrated-transformer/">https://jalammar.github.io/illustrated-transformer/</a></i>

<br/><br/>
Note: If you translate any of the posts, let me know so I can link your translation to the original post. My email is in the <a href="/about">about page</a>.
</div>


    <div class="wrapper-footer">
      <div class="container">
        <footer class="footer">
          



<a href="https://github.com/jalammar"><i class="svg-icon github"></i></a>

<a href="https://www.linkedin.com/in/jalammar"><i class="svg-icon linkedin"></i></a>


<a href="https://www.twitter.com/jayalammar"><i class="svg-icon twitter"></i></a>



        </footer>
      </div>
    </div>

    
	<!-- Google tag (gtag.js) -->
	<script async src="https://www.googletagmanager.com/gtag/js?id=G-R9S1R9LV9P"></script>
	<script>
	  window.dataLayer = window.dataLayer || [];
	  function gtag(){dataLayer.push(arguments);}
	  gtag('js', new Date());

	  gtag('config', 'G-R9S1R9LV9P');
	</script>
	<!-- End Google Analytics -->


  </body>
</html>


---

*Auto-generated from raw source by LLM Wiki Integrator*
