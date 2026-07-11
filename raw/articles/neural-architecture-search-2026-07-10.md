---

source_url: https://lilianweng.github.io/lil-log/2020/08/06/neural-architecture-search.html
ingested: 2026-07-10
sha256: ea8183cf6480b62cc6b0f6459da26af169d2899881d998f726860324ea68b00e
blog_source: Lilian Weng
---

<!DOCTYPE html>
<html lang="en">

  <head>
    
      






    

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Neural Architecture Search</title>

    <meta name="description" content="">

    <meta content="Lil'Log" property="og:site_name">
    
        <meta content="Neural Architecture Search" property="og:title">
    
    
        <meta content="article" property="og:type">
    
    
        <meta content="" property="og:description">
    
    
        <meta content="https://lilianweng.github.io/2020/08/06/neural-architecture-search.html" property="og:url">
    
    
        <meta content="2020-08-06T00:00:00+00:00" property="article:published_time">
        <meta content="https://lilianweng.github.io/about/" property="article:author">
    
    
    
        
    

    <link rel="shortcut icon" href="/lil-log/assets/favicon_peach.ico">
    <link rel="stylesheet" href="/lil-log/assets/css/main.css">
    <link rel="canonical" href="https://lilianweng.github.io/lil-log/2020/08/06/neural-architecture-search.html">

    <!-- For Latex -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

    <!-- Google Analytics -->
    <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

        ga('create', 'UA-8161570-6', 'auto');
        ga('send', 'pageview');
    </script>

    <!-- For Facebook share button -->
    <div id="fb-root"></div>
    <script>
      (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.9";
        fjs.parentNode.insertBefore(js, fjs);
      }(document, 'script', 'facebook-jssdk'));
    </script>

    <!-- Twitter cards -->
    <meta name="twitter:site"    content="@lilianweng">
    <meta name="twitter:creator" content="@Lilian Weng">
    <meta name="twitter:title"   content="Neural Architecture Search">

    
        <meta name="twitter:description" content="<meta http-equiv="Refresh" content="0; url='https://lilianweng.github.io/posts/2020-08-06-nas/'" />

">
    

    
        <meta name="twitter:card"  content="summary">
        <meta name="twitter:image" content="">
    
    <!-- end of Twitter cards -->

</head>


  <body>

    <header class="site-header" role="banner" id='header-bar'>

    <div class="wrapper">
        
        <a class="site-title" href="/lil-log/">Lil&#39;Log</a>

        <!-- <nav class="site-nav">
            <a class="page-link" href="http://lilianweng.github.io" target="_blank">&#x1f349; About</a>
        </nav> -->
        <nav class="site-nav">
            <a class="page-link" href="https://www.emojisearch.app/" target="_blank">&#x1F642; Emoji</a>
        </nav>
        <nav class="site-nav">
            <a class="page-link" href="/lil-log/contact.html">&#x1f984; Contact</a>
        </nav>
        <nav class="site-nav">
            <a class="page-link" href="/lil-log/FAQ.html">&#x1F64B; FAQ</a>
        </nav>
        <nav class="site-nav">
            <a class="page-link" href="/lil-log/archive.html">&#x231b; Archive</a>
        </nav>

    </div>

</header>


    <!-- Back to top button -->
    <script src="/lil-log/assets/vanilla-back-to-top.min.js"></script>
    <script>addBackToTop()</script>

    <main class="page-content" aria-label="Content">
      <div class="wrapper">
        <article class="post" itemscope itemtype="http://schema.org/BlogPosting">

  <header class="post-header">
    <h1 class="post-title" itemprop="name headline">Neural Architecture Search</h1>
    <p class="post-meta">

      <time datetime="2020-08-06T00:00:00+00:00" itemprop="datePublished">
        
        Aug 6, 2020
      </time>

      <span itemprop="author" itemscope itemtype="http://schema.org/Person">
        by <span itemprop="name">Lilian Weng</span>
      </span>

      <span>
        
      </span>
      <!--
      <span class="share-buttons">
        <span class="share-button"><a class="twitter-share-button" href="https://twitter.com/share" data-show-count="false">Tweet</a><script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script></span>

        <span class="share-button"><span class="fb-like" data-href="/2020/08/06/neural-architecture-search.html" data-layout="button_count" data-action="like" data-size="small" data-show-faces="false" data-share="true"></span></span>
      </span>
      <div style="clear: both;"/>
      -->

    </p>
  </header>

  <div class="post-content" itemprop="articleBody">
    <meta http-equiv="Refresh" content="0; url='https://lilianweng.github.io/posts/2020-08-06-nas/'" />


  </div>


  <div class="page-navigation">
    
      <a class="prev" href="/lil-log/2020/06/07/exploration-strategies-in-deep-reinforcement-learning.html">&larr; Exploration Strategies In Deep Reinforcement Learning</a>
    

    
      <a class="next" href="/lil-log/2020/10/29/open-domain-question-answering.html">Open Domain Question Answering &rarr;</a>
    
  </div>

  

</article>

      </div>
    </main>

    <div style="clear: both;"/>
<footer class="site-footer">
    2021 &copy; by Lilian Weng. All Rights Reserved. Built by <a href="https://jekyllrb.com/" target="_blank">Jekyll</a>. | View on <a href="https://github.com/lilianweng/lil-log/tree/gh-pages" target="_blank">Github</a> | <a href="/lil-log/tags.html">Tags</a> | <a href="/lil-log/contact.html">Contact</a> | <a href="/lil-log/FAQ.html">FAQ</a>

    <p>
        <a href="/lil-log/feed.xml" target="_blank">
            <img src="/lil-log/assets/images/logo_rss.png" />
        </a>
        <a href="https://scholar.google.com/citations?user=dCa-pW8AAAAJ&hl=en&oi=ao" target="_blank">
            <img src="/lil-log/assets/images/logo_scholar.png" />
        </a>
        <a href="https://github.com/lilianweng" target="_blank">
            <img src="/lil-log/assets/images/logo_github.png" />
        </a>
        <a href="https://www.instagram.com/lilianweng/" target="_blank">
            <img src="/lil-log/assets/images/logo_instagram.png" />
        </a>
        <a href="https://twitter.com/lilianweng/" target="_blank">
            <img src="/lil-log/assets/images/logo_twitter.png" />
        </a>
    </p>
</footer>


  </body>

</html>
