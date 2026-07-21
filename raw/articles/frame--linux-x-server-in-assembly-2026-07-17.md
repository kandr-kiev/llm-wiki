---
source_url: https://isene.org/2026/07/Frame.html
ingested: 2026-07-17
sha256: 655a7878ef53ac1817ba92f55cd758a650490a15eeca9a4bfcc3db4124d09fc9
blog_source: Hacker News
---
<!doctype html>
<!--[if lt IE 7]><html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->
<!--[if (IE 7)&!(IEMobile)]><html class="no-js lt-ie9 lt-ie8" lang="en"><![endif]-->
<!--[if (IE 8)&!(IEMobile)]><html class="no-js lt-ie9" lang="en"><![endif]-->
<!--[if gt IE 8]><!--><html class="no-js" lang="en"><!--<![endif]-->

<head>
    <meta charset="utf-8">
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-123743686-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-123743686-1');
</script>

<title>Frame - the first Linux Assembly X server &#8211; Geir's Everything</title>
<meta name="description" content="Philosophy - Sciences - Geekery - Art - Life - Coaching - Fun < Simplify Everything">
<meta name="keywords" content="Geekery, Technology">

<!-- MathJax -->
<script type="text/javascript" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"></script>





<!-- Open Graph -->
<meta property="og:locale" content="en_US">
<meta property="og:type" content="article">
<meta property="og:title" content="Frame - the first Linux Assembly X server">
<meta property="og:description" content="Philosophy - Sciences - Geekery - Art - Life - Coaching - Fun < Simplify Everything">
<meta property="og:url" content="https://isene.org/2026/07/Frame.html">
<meta property="og:site_name" content="Geir's Everything">





<link rel="canonical" href="https://isene.org/2026/07/Frame.html">
<link href="https://isene.org/feed.xml" type="application/atom+xml" rel="alternate" title="Geir's Everything Feed">

<!-- http://t.co/dKP3o1e -->
<meta name="HandheldFriendly" content="True">
<meta name="MobileOptimized" content="320">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- For all browsers -->
<link rel="stylesheet" href="/assets/css/main.css">
<!-- Webfonts -->
<link href="//fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic" rel="stylesheet" type="text/css">

<meta http-equiv="cleartype" content="on">



<link href="//maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">



    <!-- HEADER IMAGE -->
    <center>
        <span class="main-header-image">
            <a href="https://isene.org/2019/12/Escher.html"><img src="/assets/images/geirisene.png"></a>
        </span>
    </center>
    <br>
    <center>
        <span class="main-header-image">
			<!-- <h1 style="font-weight:100; font-kerning:normal"><a href="/">Geir's Everything</a></h1> -->
			<h3 style="font-weight:100; font-kerning:normal">Philosophy - Sciences - Geekery - Art - Life - Coaching - Fun < Simplify Everything</a></h3>
			<hr>
        </span>
    </center>

    <!-- NAVIGATION -->
    <center>
    <nav class="header-nav">
        <ul class="navigation-bar">
            <li><a href="/">Blog</a></li>
			<li><a href="/onepagebooks">OnePageBooks</a></li>
			<li><a href="/tags/#Podcast">Podcasts</a></li>
			<li><a href="https://isene.com/freewill">Free will</a></li>
			<li><a href="/hyperlist">HyperList</a></li>
			<li><a href="/contributions">Books & Articles</a></li>
        </ul>
    </nav>
    <nav class="header-nav">
        <ul class="navigation-bar">
			<li><a href="/amar">Amar RPG</a></li>
			<li><a href="/photos">Photos</a></li>
			<li><a href="/art">Art</a></li>
			<li><a href="/music">Music</a></li>
			<li><a href="/astro">Astronomy</a></li>
			<li><a href="/hp-41">HP-41</a></li>
			<li><a href="https://github.com/isene">Github</a></li>
			<li><a href="https://isene.org/watt/">Watt</a></li>
			<li><a href="/scientology">Scientology</a></li>
        </ul>
    </nav>
    <nav class="header-nav">
        <ul class="navigation-bar">
			<li><a href="/esport">Esport</a></li>
			<li><a href="/coaching">Coaching</a></li>
			<li><a href="/about">About/Contact</a></li>
            <li><a href="/archives/">ARCHIVE</a></li>
            <li><a href="/tags/">TAGS</a></li>
            <li><a href="/feed.xml">RSS</a></li>
        </ul>
    </nav>
</center>

</head>

<!-- BODY -->
<body id="post-index">
    <!--[if lt IE 9]><div class="upgrade"><strong><a href="http://whatbrowser.org/">Your browser is quite old!</strong> Why not upgrade to a different browser to better enjoy this site?</a></div><![endif]-->

    <div id="main" role="main">
        <article class="hentry">

            <div class="featured-image">
            <img src="" style="width:100%">
            </div>

            <!-- MAIN -->
            <h1 class="entry-title">
                <a>Frame - the first Linux Assembly X server</a>
            </h1>
            <h3 class="entry-subtitle">
                <a href="https://isene.org" rel="bookmark" title="" itemprop="url"></a>
            </h3>

            <hr>

            <!-- POST CONTENT -->
            <div class="entry-content">
                <p><img src="/assets/posts/framestack.png" alt="Frame" /></p>

<p>On my quest to <a href="/2026/04/MyTools.html">own my software</a>, one foundational piece kept itching… the X server. The underlying graphics engine, the thing that puts pixels on the screen. <a href="https://www.x.org/">X11</a> is 4 million lines of code, a beast very few can claim they understand. So I did the reasonable thing. I wrote my own, in Assembly.</p>

<p>It is called <a href="https://github.com/isene/frame">frame</a>. No dependencies, no libraries, no garbage collector. No hot paths, no unnecessary wakeups. When it is idle, it sits still. It shuts up unless spoken to. My kind of software. It clocks in at some 20 thousand lines, and it already runs my whole desktop plus Firefox and <a href="/2026/07/Fable-to-the-Rescue.html">GIMP</a> whenever I need that. It is still young, and there is a long list of X protocol left to chew through. But it boots, it draws, and I am typing this on it.</p>

<p>So the stack now looks like this: The Linux kernel at the bottom. On top of that, frame. Then the window manager <a href="https://github.com/isene/tile">tile</a> with the info bar <a href="https://github.com/isene/tile">strip</a>. Inside tile runs the terminal <a href="https://github.com/isene/glass">glass</a>, and in glass lives the shell <a href="https://github.com/isene/bare">bare</a>. <a href="https://github.com/isene/bolt">Bolt</a> has been promoted from screen locker to greeter, showing gdm the door. All of it Assembly. All of <a href="https://isene.org/chasm/">CHasm</a> together is about 100 thousand lines. The stack it replaced (gdm, X11, i3, conky, wezterm, zsh) is somewhere north of fifty times that. I did it for the <a href="/2026/05/Baseline.html">battery life</a>. I am not sure this laptop has a fan anymore. Except me.</p>

<p>Today I put numbers on it. Idle on battery, frame and Xorg pull the same watts, because the panel and the wifi own that number anyway. But Xorg burns almost three times the CPU that frame needs to do nothing. And tile and glass used zero milliseconds over three minutes of measuring. The desktop sits completely still until I touch it.</p>

<p>Beyond the desktop I have my <a href="https://isene.org/fe2o3/">Fe₂O₃ suite</a> of Rust tools, which by now has replaced everything else I used to run. Except Firefox. That is the last GUI standing that I regularly use. The rest is terminal interfaces with the same keybindings everywhere, and a fraction of the size and electrical appetite of what they replaced.</p>

<p><img src="/assets/posts/framescrot.png" alt="Frame screenshot" /></p>

<p>But is it stable? Stable enough that I daily-drive it, write this post on it, and only occasionally yell. When something breaks or I want a feature, I turn to my buddy <a href="https://claude.com/claude-code">Claude</a> and describe the itch. He never gets tired, is not opinionated, and turns out to be a really good teacher. I now know more about hardware layers, cursor painting, GPU handoffs and event watchers than I ever planned to.</p>

<p>The <a href="/2026/05/Nomad.html">phone got the same treatment</a>, with my own launcher, a daily personalized news digest and a pile of apps tailored for an audience of exactly one.</p>

<p>The upside is simple. I have what I need and want. I control and own the software, and all of it is given to the Public Domain. Software designed for a large audience fits everyone a little. This fits one person exactly.</p>

<hr />

<p>Link to this post: https://isene.org/2026/07/Frame.html</p>

            </div>
            <!--- DIVIDING LINE -->
            <hr>

            <!-- POST TAGS -->
            <div class="inline-tags">
                <span>
                    
                        <a href="/tags/#Geekery">#Geekery&nbsp;&nbsp;&nbsp;</a>
                    
                        <a href="/tags/#Technology">#Technology&nbsp;&nbsp;&nbsp;</a>
                    
                </span>
            </div>

            <br>

            <!-- POST DATE -->
            <div class="post-date">
                
            </div>
			<a id="comments"></a>
<script src="https://giscus.app/client.js"
        data-repo="isene/isene.github.io"
        data-repo-id="MDEwOlJlcG9zaXRvcnkxNDM2NjUwNjU="
        data-category="General"
        data-category-id="DIC_kwDOCJAnqc4C5Y-d"
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="top"
        data-theme="dark"
        data-lang="en"
        crossorigin="anonymous"
        async>
</script>

        </article>
    </div>
	<!-- FOOTER -->
	<footer>
		<div class="footer-wrapper">
			<footer role="contentinfo">
					<center><div class="shorthr"><hr></div></center>
	<form action="https://www.google.com/search" class="searchform" method="get" name="searchform" target="_blank">
		<input name="sitesearch" type="hidden" value="isene.org">
		<input autocomplete="on" class="field" name="q" placeholder="Search in isene.org" required="required"  type="text">
		<button class="button" type="submit">Search</button>
	</form>
	<center><div class="shorthr"><hr></div></center>
	<span>
		<p>
			<a href="https://follow.it/geir-s-everything?action=followPub">Subscribe to isene.org</a>
		</p>
		<p>
			Contact me: &nbsp;
			<a class="icon" href="mailto:g@isene.com"><i class="fa fa-envelope" title="Email"></i></a> &nbsp;
			<a class="icon" href="https://github.com/isene"><i class="fa fa-github" title="Github"></i></a> &nbsp;&nbsp;
			<a class="icon" href="https://in.linkedin.com/in/isene"><i class="fa fa-linkedin" title="Linkedin"></i></a> &nbsp;&nbsp;
			<a class="icon" href="https://twitter.com/isene"><i class="fa fa-twitter" title="Twitter"></i></a> &nbsp;&nbsp;
			<a class="icon" href="https://facebook.com/geir.isene"><i class="fa fa-facebook" title="Facebook"></i></a> &nbsp;&nbsp;
			<a class="icon" href="https://www.instagram.com/geir_isene/?hl=en"><i class="fa fa-instagram" title="Instagram"></i></a> &nbsp;&nbsp;
			<a class="icon" href="https://www.youtube.com/channel/UCX4w9Kdr3i0k2vc6iKQOAlg"><i class="fa fa-youtube" title="Youtube"></i></a>
		</p>
		<p>By Geir Isene (2026). No Rights Reserved. Powered by <a target="_blank" href="https://jekyllrb.com" rel="nofollow">Jekyll</a> w/modified <a target="_blank" href="https://github.com/benradford/Slate-and-Simple-Jekyll-Theme">Slate+Simple</a> theme.</p>
	</span>



			</footer>
		</div>
	</footer>
</body>

</html>
