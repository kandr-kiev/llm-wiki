---
source_url: http://jalammar.github.io/explainable-ai/
ingested: 2026-07-11
sha256: 73af8900b08724f335e9a671eda80e0ebf60c9940c77eef8ae8d5428c2bfe8ce
blog_source: Jay Alammar
---
<!DOCTYPE html>
<html>
<head>
    <title>Explainable AI Cheat Sheet – Jay Alammar – Visualizing machine learning one concept at a time.</title>
        <meta charset="utf-8" />
    <meta content='text/html; charset=utf-8' http-equiv='Content-Type'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0'>

    
    <meta name="description" content="Introducing the Explainable AI Cheat Sheet, your high-level guide to the set of tools and methods that helps humans understand AI/ML models and their predictions.

 

I introduce the cheat sheet in this brief video:


 
 

" />
    <meta property="og:description" content="Introducing the Explainable AI Cheat Sheet, your high-level guide to the set of tools and methods that helps humans understand AI/ML models and their predictions.

 

I introduce the cheat sheet in this brief video:


 
 

" />
    
    <meta name="author" content="Jay Alammar" />

    
    <meta property="og:title" content="Explainable AI Cheat Sheet" />
    <meta property="twitter:title" content="Explainable AI Cheat Sheet" />
    

    <!--[if lt IE 9]>
    <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->


    <link rel="stylesheet" type="text/css" href="/bower_components/jquery.gifplayer/dist/gifplayer.css"/>

    <!--
    <script data-main="scripts/main" src="scripts/require.js"></script>
    -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/katex.min.css" integrity="sha384-wE+lCONuEo/QSfLb4AfrSk7HjWJtc4Xc1OiB2/aDBzHzjnlBP4SX7vjErTcwlA8C" crossorigin="anonymous">

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
                <p class="site-description">Visualizing machine learning one concept at a time.<br /><a href="https://twitter.com/JayAlammar">@JayAlammar</a> on Twitter. <a href="https://www.youtube.com/channel/UCmOwsoHty5PrmE-3QhUBfPQ">YouTube Channel</a></a></p>
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
    <h1>Explainable AI Cheat Sheet</h1>

    <div class="entry prediction">
        <p>Introducing the <a href="https://ex.pegg.io">Explainable AI Cheat Sheet</a>, your high-level guide to the set of tools and methods that helps humans understand AI/ML models and their predictions.</p>

<p><a href="https://ex.pegg.io"> <img src="/images/Explainable-AI-cheat-sheet-v0.2.1080.png" /></a></p>

<p>I introduce the cheat sheet in this brief video:</p>

<div style="text-align:center">
 
 <iframe width="560" height="315" src="https://www.youtube.com/embed/Yg3q5x7yDeM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" style="
 width: 100%;
 max-width: 560px;" allowfullscreen=""></iframe>
</div>

    </div>

    <div class="date">
        Written on May  4, 2021
    </div>

    
</article>

</div>



<!-- Begin Mailchimp Signup Form -->
<link href="//cdn-images.mailchimp.com/embedcode/classic-10_7.css" rel="stylesheet" type="text/css">
<style type="text/css">
    #mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif; }
    /* Add your own Mailchimp form style overrides in your site stylesheet or in this style block.
       We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */
</style>
<div id="mc_embed_signup">
    <form action="https://github.us19.list-manage.com/subscribe/post?u=2a4ade7dafcdbbf2eb4aae3cf&amp;id=f1f8c03f13" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
        <div id="mc_embed_signup_scroll">
            <h2>Subscribe to get notified about upcoming posts by email</h2>
            <div class="mc-field-group">
                <label for="mce-EMAIL">Email Address </label>
                <input type="email" value="" name="EMAIL" class="required email" id="mce-EMAIL">
            </div>
            <div id="mce-responses" class="clear">
                <div class="response" id="mce-error-response" style="display:none"></div>
                <div class="response" id="mce-success-response" style="display:none"></div>
            </div>    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
            <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_2a4ade7dafcdbbf2eb4aae3cf_f1f8c03f13" tabindex="-1" value=""></div>
            <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
        </div>
    </form>
</div>
<script type='text/javascript' src='//s3.amazonaws.com/downloads.mailchimp.com/js/mc-validate.js'></script><script type='text/javascript'>(function($) {window.fnames = new Array(); window.ftypes = new Array();fnames[0]='EMAIL';ftypes[0]='email';fnames[1]='FNAME';ftypes[1]='text';fnames[2]='LNAME';ftypes[2]='text';fnames[3]='ADDRESS';ftypes[3]='address';fnames[4]='PHONE';ftypes[4]='phone';fnames[5]='BIRTHDAY';ftypes[5]='birthday';}(jQuery));var $mcj = jQuery.noConflict(true);</script>
<!--End mc_embed_signup-->

<div style="padding: 10px 0 10px 3%; color: #555; font-size:85%">
    <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

    <br/>
    Attribution example:
    <br/>
    <i>Alammar, Jay (2018). The Illustrated Transformer [Blog post]. Retrieved from <a href="https://jalammar.github.io/illustrated-transformer/">https://jalammar.github.io/illustrated-transformer/</a></i>

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
