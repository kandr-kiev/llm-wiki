---
source_url: https://dylancastillo.co/posts/pelicanmaxxing.html
ingested: 2026-07-22
sha256: 3518b32cc947227f6735a5a2f620ddc045f2b774db640b0ed39290398118bd4f
blog_source: Hacker News AI
---
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en"><head>

<meta charset="utf-8">
<meta name="generator" content="quarto-1.9.38">

<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">

<meta name="author" content="Dylan Castillo">
<meta name="dcterms.date" content="2026-07-18">
<meta name="description" content="I generated 1,000+ SVGs across 7 frontier models to test whether AI labs are training on Simon Willison’s pelican-riding-a-bicycle benchmark.">

<title>Are AI labs pelicanmaxxing? – Dylan Castillo</title>
<style>
/* Default styles provided by pandoc.
** See https://pandoc.org/MANUAL.html#variables-for-html for config info.
*/
code{white-space: pre-wrap;}
span.smallcaps{font-variant: small-caps;}
div.columns{display: flex; gap: min(4vw, 1.5em);}
div.column{flex: auto; overflow-x: auto;}
div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
ul.task-list{list-style: none;}
ul.task-list li input[type="checkbox"] {
  width: 0.8em;
  margin: 0 0.8em 0.2em -1em; /* quarto-specific, see https://github.com/quarto-dev/quarto-cli/issues/4556 */ 
  vertical-align: middle;
}
</style>


<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js" integrity="sha512-bLT0Qm9VnAYZDflyKcBaQ2gg0hSYNQrJ8RilYldYQ1FxQYoCLtUjuuRuZo+fjqhx/qtq/1itJ0C2ejDxltZVFg==" crossorigin="anonymous" type="5f8209360523110751b003df-text/javascript"></script><script src="../site_libs/quarto-nav/quarto-nav.js" type="5f8209360523110751b003df-text/javascript"></script>
<script src="../site_libs/quarto-nav/headroom.min.js" type="5f8209360523110751b003df-text/javascript"></script>
<script src="../site_libs/clipboard/clipboard.min.js" type="5f8209360523110751b003df-text/javascript"></script>
<script src="../site_libs/quarto-search/autocomplete.umd.js" type="5f8209360523110751b003df-text/javascript"></script>
<script src="../site_libs/quarto-search/fuse.min.js" type="5f8209360523110751b003df-text/javascript"></script>
<script src="../site_libs/quarto-search/quarto-search.js" type="5f8209360523110751b003df-text/javascript"></script>
<meta name="quarto:offset" content="../">
<link href="../images/logo.webp" rel="icon">
<script src="../site_libs/quarto-html/quarto.js" type="5f8209360523110751b003df-module"></script>
<script src="../site_libs/quarto-html/tabsets/tabsets.js" type="5f8209360523110751b003df-module"></script>
<script src="../site_libs/quarto-html/popper.min.js" type="5f8209360523110751b003df-text/javascript"></script>
<script src="../site_libs/quarto-html/tippy.umd.min.js" type="5f8209360523110751b003df-text/javascript"></script>
<script src="../site_libs/quarto-html/anchor.min.js" type="5f8209360523110751b003df-text/javascript"></script>
<link href="../site_libs/quarto-html/tippy.css" rel="stylesheet">
<link href="../site_libs/quarto-html/quarto-syntax-highlighting-dark-0a6b7249c26820e032cb0bd839ff02b1.css" rel="stylesheet" id="quarto-text-highlighting-styles">
<script src="../site_libs/bootstrap/bootstrap.min.js" type="5f8209360523110751b003df-text/javascript"></script>
<link href="../site_libs/bootstrap/bootstrap-icons.css" rel="stylesheet">
<link href="../site_libs/bootstrap/bootstrap-955d070f4b17be565f0204175e96f90d.min.css" rel="stylesheet" append-hash="true" id="quarto-bootstrap" data-mode="dark">
<script src="../site_libs/quarto-contrib/iconify-2.1.0/iconify-icon.min.js" type="5f8209360523110751b003df-text/javascript"></script>
<script id="quarto-search-options" type="application/json">{
  "location": "navbar",
  "copy-button": false,
  "collapse-after": 3,
  "panel-placement": "end",
  "type": "overlay",
  "limit": 50,
  "keyboard-shortcut": [
    "f",
    "/",
    "s"
  ],
  "show-item-context": false,
  "language": {
    "search-no-results-text": "No results",
    "search-matching-documents-text": "matching documents",
    "search-copy-link-title": "Copy link to search",
    "search-hide-matches-text": "Hide additional matches",
    "search-more-match-text": "more match in this document",
    "search-more-matches-text": "more matches in this document",
    "search-clear-button-title": "Clear",
    "search-text-placeholder": "",
    "search-detached-cancel-button-title": "Cancel",
    "search-submit-button-title": "Submit",
    "search-label": "Search"
  }
}</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.6/require.min.js" integrity="sha512-c3Nl8+7g4LMSTdrm621y7kf9v3SDPnhxLNhcjFJbKECVnmZHTdo+IRO05sNLTH/D3vA6u1X32ehoLC7WFVdheg==" crossorigin="anonymous" type="5f8209360523110751b003df-text/javascript"></script>

<script type="5f8209360523110751b003df-application/javascript">define('jquery', [],function() {return window.jQuery;})</script>
<link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&amp;display=swap" rel="stylesheet">
<script src="https://cdn.usefathom.com/script.js" data-site="ZJFQREIA" defer="" type="5f8209360523110751b003df-text/javascript"></script>
<link rel="stylesheet" href="../custom/pelican-explorer.css">


<meta property="og:title" content="Are AI labs pelicanmaxxing? – Dylan Castillo">
<meta property="og:description" content="">
<meta property="og:image" content="https://dylancastillo.co/posts/images/social_media_card.webp">
<meta property="og:site_name" content="Dylan Castillo">
<meta name="twitter:title" content="Are AI labs pelicanmaxxing? – Dylan Castillo">
<meta name="twitter:description" content="">
<meta name="twitter:image" content="https://dylancastillo.co/posts/images/social_media_card.webp">
<meta name="twitter:creator" content="@dylanjcastillo">
<meta name="twitter:site" content="@dylanjcastillo">
<meta name="twitter:card" content="summary_large_image">
</head>

<body class="nav-fixed quarto-light">

<div id="quarto-search-results"></div>
  <header id="quarto-header" class="headroom fixed-top">
    <nav class="navbar navbar-expand-lg " data-bs-theme="dark">
      <div class="navbar-container container-fluid">
            <div id="quarto-search" class="" title="Search"></div>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" role="menu" aria-expanded="false" aria-label="Toggle navigation" onclick="if (!window.__cfRLUnblockHandlers) return false; if (window.quartoToggleHeadroom) { window.quartoToggleHeadroom(); }" data-cf-modified-5f8209360523110751b003df-="">
  <span class="navbar-toggler-icon"></span>
</button>
          <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav navbar-nav-scroll me-auto">
  <li class="nav-item">
    <a class="nav-link" href="../index.html"> 
<span class="menu-text">Home</span></a>
  </li>  
  <li class="nav-item">
    <a class="nav-link" href="../projects.html"> 
<span class="menu-text">Projects</span></a>
  </li>  
  <li class="nav-item">
    <a class="nav-link" href="../about.html"> 
<span class="menu-text">About</span></a>
  </li>  
</ul>
            <ul class="navbar-nav navbar-nav-scroll ms-auto">
  <li class="nav-item">
    <a class="nav-link" href="https://github.com/dylanjcastillo"> 
<span class="menu-text"><iconify-icon role="img" inline="" icon="fa6-brands:github" aria-label="Icon github from fa6-brands Iconify.design set." title="Icon github from fa6-brands Iconify.design set."></iconify-icon></span></a>
  </li>  
  <li class="nav-item">
    <a class="nav-link" href="https://www.linkedin.com/in/dylanjcastillo/"> 
<span class="menu-text"><iconify-icon role="img" inline="" icon="fa6-brands:linkedin" aria-label="Icon linkedin from fa6-brands Iconify.design set." title="Icon linkedin from fa6-brands Iconify.design set."></iconify-icon></span></a>
  </li>  
</ul>
          </div> <!-- /navcollapse -->
            <div class="quarto-navbar-tools">
</div>
      </div> <!-- /container-fluid -->
    </nav>
</header>
<!-- content -->
<div id="quarto-content" class="quarto-container page-columns page-rows-contents page-layout-article page-navbar">
<!-- sidebar -->
<!-- margin-sidebar -->
    <div id="quarto-margin-sidebar" class="sidebar margin-sidebar">
        <nav id="TOC" role="doc-toc" class="toc-active">
    <h2 id="toc-title">On this page</h2>
   
  <ul>
  <li><a href="#how-i-tested-it" id="toc-how-i-tested-it" class="nav-link active" data-scroll-target="#how-i-tested-it">How I tested it</a></li>
  <li><a href="#evidence-1-the-pelicans-on-bicycles-dont-look-any-better" id="toc-evidence-1-the-pelicans-on-bicycles-dont-look-any-better" class="nav-link" data-scroll-target="#evidence-1-the-pelicans-on-bicycles-dont-look-any-better">Evidence #1: The pelicans on bicycles don’t look any better</a></li>
  <li><a href="#evidence-2-labs-are-not-better-at-drawing-pelicans" id="toc-evidence-2-labs-are-not-better-at-drawing-pelicans" class="nav-link" data-scroll-target="#evidence-2-labs-are-not-better-at-drawing-pelicans">Evidence #2: Labs are not better at drawing pelicans</a></li>
  <li><a href="#evidence-3-labs-are-not-better-at-drawing-bicycles" id="toc-evidence-3-labs-are-not-better-at-drawing-bicycles" class="nav-link" data-scroll-target="#evidence-3-labs-are-not-better-at-drawing-bicycles">Evidence #3: Labs are not better at drawing bicycles</a></li>
  <li><a href="#evidence-4-labs-are-not-better-at-drawing-pelicans-on-bicycles-even-adjusting-for-difficulty" id="toc-evidence-4-labs-are-not-better-at-drawing-pelicans-on-bicycles-even-adjusting-for-difficulty" class="nav-link" data-scroll-target="#evidence-4-labs-are-not-better-at-drawing-pelicans-on-bicycles-even-adjusting-for-difficulty">Evidence #4: Labs are not better at drawing pelicans on bicycles, even adjusting for difficulty</a></li>
  <li><a href="#evidence-5-the-pelican-bicycle-scenes-dont-look-memorized" id="toc-evidence-5-the-pelican-bicycle-scenes-dont-look-memorized" class="nav-link" data-scroll-target="#evidence-5-the-pelican-bicycle-scenes-dont-look-memorized">Evidence #5: The pelican-bicycle scenes don’t look memorized</a></li>
  <li><a href="#limitations" id="toc-limitations" class="nav-link" data-scroll-target="#limitations">Limitations</a></li>
  <li><a href="#conclusion" id="toc-conclusion" class="nav-link" data-scroll-target="#conclusion">Conclusion</a></li>
  </ul>
</nav>
    <div class="quarto-margin-footer"><div class="margin-footer-item">
<button onclick="if (!window.__cfRLUnblockHandlers) return false; window.location.href='https://subscribe.dylancastillo.co'" style="background-color: #eb841b; color: white; padding: 12px 24px; border: none; border-radius: 6px; font-size: 12px; font-weight: bold; cursor: pointer; transition: background-color 0.3s ease;" data-cf-modified-5f8209360523110751b003df-="">
Subscribe to my newsletter
</button>
</div></div></div>
<!-- main -->
<main class="content page-columns page-full" id="quarto-document-content">

<header id="title-block-header" class="quarto-title-block default">
<div class="quarto-title">
<h1 class="title">Are AI labs pelicanmaxxing?</h1>
  <div class="quarto-categories">
    <div class="quarto-category">llm</div>
    <div class="quarto-category">evals</div>
    <div class="quarto-category">python</div>
  </div>
  </div>


<div class="quarto-title-meta-author">
  <div class="quarto-title-meta-heading">Author</div>
  <div class="quarto-title-meta-heading">Affiliation</div>
  
    <div class="quarto-title-meta-contents">
    <p class="author"><a href="https://dylancastillo.co">Dylan Castillo</a> </p>
  </div>
  <div class="quarto-title-meta-contents">
        <p class="affiliation">
            <a href="https://iwanalabs.com">
            Iwana Labs
            </a>
          </p>
      </div>
  </div>

<div class="quarto-title-meta">

      
    <div>
    <div class="quarto-title-meta-heading">Published</div>
    <div class="quarto-title-meta-contents">
      <p class="date">July 18, 2026</p>
    </div>
  </div>
  
    <div>
    <div class="quarto-title-meta-heading">Modified</div>
    <div class="quarto-title-meta-contents">
      <p class="date-modified">July 22, 2026</p>
    </div>
  </div>
    
  </div>
  


</header>


<p>For the past few years, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle/">Simon Willison</a> has tested every major LLM release with the same prompt: “Generate an SVG of a pelican riding a bicycle”.</p>
<p>What began as a tongue-in-cheek benchmark has become one of the most famous informal benchmarks in AI. Simon’s pelican-on-a-bicycle results are often among the most upvoted comments on Hacker News threads announcing new releases from AI labs.</p>
<p>The benchmark is now famous enough that there’s <a href="https://news.ycombinator.com/item?id=48994959">plenty</a> <a href="https://news.ycombinator.com/item?id=48994217">of</a> <a href="https://news.ycombinator.com/item?id=48956159">discussion</a> about its usefulness and about whether AI labs might be benchmaxxing<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a> on it. When billions or even trillions of dollars are at stake, and a strong result could help persuade users, wouldn’t it be tempting to pelicanmaxx your model just a bit?</p>
<p>I wanted to find out, so I put together a small experiment. I generated 1,008 SVGs across seven frontier models, scored them with an LLM judge, and used Claude Fable 5 for the analysis.</p>
<p>This article presents the results. All the code is available on <a href="https://github.com/dylanjcastillo/blog/tree/main/_extras/pelicanmaxxing">Github</a>.</p>
<section id="how-i-tested-it" class="level2">
<h2 class="anchored" data-anchor-id="how-i-tested-it">How I tested it</h2>
<p>I built a grid of 8 animals × 6 vehicles = 48 prompts, where the famous prompt is one cell:</p>
<ol type="1">
<li><strong>Animals</strong>: pelican, flamingo, heron, otter, raccoon, antelope, whale, cat</li>
<li><strong>Vehicles</strong>: bicycle, unicycle, skateboard, scooter, plane, boat</li>
</ol>
<p>Every prompt uses almost identical phrasing to Simon’s, only switching the animal and vehicle. The animal and vehicle selection wasn’t done in a very rigorous manner, but I tried to vary both similarity to the original prompt and difficulty. Flamingo and heron are quite similar to pelicans; cat, raccoon, and otter are easy cases; antelope is hard; and whale is as different as you can get.</p>
<p>I tested seven models through <a href="https://openrouter.ai/">OpenRouter</a>: <em>GPT-5.6 Terra</em>, <em>Claude Sonnet 5</em>, <em>Gemini 3.5 Flash</em>, <em>Grok 4.5</em>, <em>Qwen3.7-Max</em>, <em>GLM-5.2</em>, and <em>DeepSeek V4 Pro</em>. I generated 3 samples per prompt, at temperature 1.0, requesting the same reasoning effort from every model. That resulted in 1,008 SVGs.</p>
<p>Then I ran each image through a three-stage pipeline:</p>
<ol type="1">
<li><strong>Rendering</strong>: Each SVG is rendered to PNG. If a model returns no SVG or one that fails to render, I regenerate until it produces a valid one, and record the number of attempts. There were only 11 retries across the 1,008 generations.</li>
<li><strong>Judging</strong>: <em>GPT-5.6 Luna</em> scores each image with 1-5 ratings for the animal, the vehicle, and the coherence of the action. When I rank animals or vehicles below, I use the matching rating on its own. When I need one number per image, I use the average of the three, which I call the judge score.</li>
<li><strong>Feature extraction</strong>: For a more detailed analysis, I also passed each rendered image to <em>Gemini 3.1 Flash-Lite</em>, which recorded the animal and vehicle it recognized, which way the subject faces, and an open-ended list of scene elements.</li>
</ol>
<p>My hypothesis is that if a lab trained on the benchmark, it should show up in some combination of the pelican row scoring above what the animal deserves, the bicycle column scoring above what the vehicle deserves, or the specific pelican-bicycle cell beating both.</p>
</section>
<section id="evidence-1-the-pelicans-on-bicycles-dont-look-any-better" class="level2">
<h2 class="anchored" data-anchor-id="evidence-1-the-pelicans-on-bicycles-dont-look-any-better">Evidence #1: The pelicans on bicycles don’t look any better</h2>
<p>Before any scoring, the simplest test is to look at the images yourself. Pick a lab to see everything it drew, with the judge’s score under each image (click to open full size):</p>
<div class="pelican-explorer" data-config="{
       &quot;base&quot;: &quot;https://s3.eu-west-1.amazonaws.com/images.dylancastillo.co/pelicanmaxxing&quot;,
       &quot;models&quot;: [
         {&quot;slug&quot;: &quot;openai__gpt-5.6-terra&quot;, &quot;name&quot;: &quot;GPT-5.6 Terra&quot;},
         {&quot;slug&quot;: &quot;anthropic__claude-sonnet-5&quot;, &quot;name&quot;: &quot;Claude Sonnet 5&quot;},
         {&quot;slug&quot;: &quot;google__gemini-3.5-flash&quot;, &quot;name&quot;: &quot;Gemini 3.5 Flash&quot;},
         {&quot;slug&quot;: &quot;x-ai__grok-4.5&quot;, &quot;name&quot;: &quot;Grok 4.5&quot;},
         {&quot;slug&quot;: &quot;qwen__qwen3.7-max&quot;, &quot;name&quot;: &quot;Qwen3.7-Max&quot;},
         {&quot;slug&quot;: &quot;z-ai__glm-5.2&quot;, &quot;name&quot;: &quot;GLM-5.2&quot;},
         {&quot;slug&quot;: &quot;deepseek__deepseek-v4-pro&quot;, &quot;name&quot;: &quot;DeepSeek V4 Pro&quot;}
       ],
       &quot;animals&quot;: [&quot;pelican&quot;, &quot;flamingo&quot;, &quot;heron&quot;, &quot;otter&quot;, &quot;raccoon&quot;, &quot;antelope&quot;, &quot;whale&quot;, &quot;cat&quot;],
       &quot;vehicles&quot;: [&quot;bicycle&quot;, &quot;unicycle&quot;, &quot;skateboard&quot;, &quot;scooter&quot;, &quot;plane&quot;, &quot;boat&quot;],
       &quot;samples&quot;: 3
     }">

</div>
<p>I looked through the images myself before running the analysis below. Nothing jumped out at me. I couldn’t find a case where the pelican-bicycle images looked noticeably better than the rest of that model’s grid. Maybe in GLM-5.2’s first sample it felt slightly better than the rest, but that batch also produced a pretty cool heron on a skateboard, so I cannot say for sure. Otherwise they look like the rest of what each model draws, and the labs that draw good pelicans on bicycles also do a good job drawing other animal-vehicle combinations.</p>
<p>But this test is hard to replicate, and everyone will have a different opinion. So I wanted something more quantitative, which is why I opted for the method detailed above.</p>
</section>
<section id="evidence-2-labs-are-not-better-at-drawing-pelicans" class="level2 page-columns page-full">
<h2 class="anchored" data-anchor-id="evidence-2-labs-are-not-better-at-drawing-pelicans">Evidence #2: Labs are not better at drawing pelicans</h2>
<p>Here’s the mean animal rating per animal, pooled across all models:</p>
<div id="cell-fig-animal-scores" class="cell page-columns page-full" data-execution_count="2">
<div id="fig-animal-scores" class="cell-output cell-output-display quarto-float quarto-figure quarto-figure-center anchored page-columns page-full">
<figure class="quarto-float quarto-float-fig figure page-columns page-full">
<div aria-describedby="fig-animal-scores-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
<div>            <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG" type="5f8209360523110751b003df-text/javascript"></script><script type="5f8209360523110751b003df-text/javascript">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}</script>                <script type="5f8209360523110751b003df-text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-3.0.1.min.js" type="5f8209360523110751b003df-text/javascript"></script>                <div id="afeb5f52-40e0-49b3-8508-ebc0b82365c5" class="plotly-graph-div" style="height:340px; width:100%;"></div>            <script type="5f8209360523110751b003df-text/javascript">                window.PLOTLYENV=window.PLOTLYENV || {};                                if (document.getElementById("afeb5f52-40e0-49b3-8508-ebc0b82365c5")) {                    Plotly.newPlot(                        "afeb5f52-40e0-49b3-8508-ebc0b82365c5",                        [{"hovertemplate":"\u003cb\u003e%{y}\u003c\u002fb\u003e\u003cbr\u003e%{x:.2f} out of 5\u003cextra\u003e\u003c\u002fextra\u003e","marker":{"color":["#71717a","#71717a","#eb841b","#71717a","#71717a","#71717a","#71717a","#71717a"]},"orientation":"h","text":["3.95","4.07","4.08","4.21","4.42","4.48","4.62","4.63"],"textfont":{"color":"#a1a1aa","size":12},"textposition":"outside","width":0.6,"x":{"dtype":"f8","bdata":"6Xme53meD0CSJEmSJEkQQBRFURRFURBAt23btm3bEEDsuq7ruq4RQHqe53me5xFAnud5nud5EkCjKIqiKIoSQA=="},"y":["otter","flamingo","pelican","antelope","heron","raccoon","whale","cat"],"type":"bar"}],                        {"template":{"data":{"scatter":[{"type":"scatter"}]},"layout":{"margin":{"b":0,"l":0,"r":0,"t":30}}},"title":{"font":{"size":15,"color":"#e4e4e7"},"text":"Mean animal rating by animal (1-5)","x":0.5,"xanchor":"center"},"font":{"family":"Georgia, serif","size":13,"color":"#e4e4e7"},"margin":{"l":10,"r":10,"t":60,"b":40},"hoverlabel":{"font":{"family":"Georgia, serif","size":12,"color":"#e4e4e7"},"bgcolor":"#27272a","bordercolor":"#eb841b","align":"left"},"paper_bgcolor":"#18181b","plot_bgcolor":"#18181b","height":340,"showlegend":false,"dragmode":false,"xaxis":{"gridcolor":"#3f3f46","zeroline":false,"linecolor":"#3f3f46","tickcolor":"#3f3f46","automargin":true,"showgrid":false,"showticklabels":false,"visible":false,"range":[0,5.33015873015873]},"yaxis":{"gridcolor":"#3f3f46","zeroline":false,"linecolor":"#3f3f46","tickcolor":"#3f3f46","automargin":true,"showgrid":false}},                        {"displayModeBar": false, "responsive": true}                    ).then(function(){
                            
var gd = document.getElementById('afeb5f52-40e0-49b3-8508-ebc0b82365c5');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };            </script>        </div>
</div>
<figcaption class="quarto-float-caption-margin quarto-float-caption quarto-float-fig margin-caption" id="fig-animal-scores-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
Figure&nbsp;1: Mean animal rating by animal, all models pooled.
</figcaption>
</figure>
</div>
</div>
<p>The pelican is 6th of 8, behind cat, whale, raccoon, heron, and antelope. If AI labs were training on the benchmark, you’d expect pelicans at the top. Instead they’re in the bottom half. All seven labs draw cats, whales, and raccoons better than pelicans.</p>
<p>Of course, a pelican may simply be harder to draw than a cat. A lab could train on pelicans and still not push them past the easy animals, so this ranking alone can’t rule that out. I’ll adjust for difficulty in Evidence #4.</p>
</section>
<section id="evidence-3-labs-are-not-better-at-drawing-bicycles" class="level2 page-columns page-full">
<h2 class="anchored" data-anchor-id="evidence-3-labs-are-not-better-at-drawing-bicycles">Evidence #3: Labs are not better at drawing bicycles</h2>
<p>Bicycles fare even worse. They sit second from last, in a near-tie with planes, which come in last:</p>
<div id="cell-fig-vehicle-scores" class="cell page-columns page-full" data-execution_count="3">
<div id="fig-vehicle-scores" class="cell-output cell-output-display quarto-float quarto-figure quarto-figure-center anchored page-columns page-full">
<figure class="quarto-float quarto-float-fig figure page-columns page-full">
<div aria-describedby="fig-vehicle-scores-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
<div>            <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG" type="5f8209360523110751b003df-text/javascript"></script><script type="5f8209360523110751b003df-text/javascript">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}</script>                <script type="5f8209360523110751b003df-text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-3.0.1.min.js" type="5f8209360523110751b003df-text/javascript"></script>                <div id="23431786-936b-4372-a607-623c685650d7" class="plotly-graph-div" style="height:300px; width:100%;"></div>            <script type="5f8209360523110751b003df-text/javascript">                window.PLOTLYENV=window.PLOTLYENV || {};                                if (document.getElementById("23431786-936b-4372-a607-623c685650d7")) {                    Plotly.newPlot(                        "23431786-936b-4372-a607-623c685650d7",                        [{"hovertemplate":"\u003cb\u003e%{y}\u003c\u002fb\u003e\u003cbr\u003e%{x:.2f} out of 5\u003cextra\u003e\u003c\u002fextra\u003e","marker":{"color":["#71717a","#eb841b","#71717a","#71717a","#71717a","#71717a"]},"orientation":"h","text":["3.88","3.90","3.98","4.78","4.89","4.93"],"textfont":{"color":"#a1a1aa","size":12},"textposition":"outside","width":0.6,"x":{"dtype":"f8","bdata":"AAAAAAAAD0ANwzAMwzAPQLdt27Zt2w9A6Hme53keE0AlSZIkSZITQM\u002fzPM\u002fzvBNA"},"y":["plane","bicycle","unicycle","scooter","skateboard","boat"],"type":"bar"}],                        {"template":{"data":{"scatter":[{"type":"scatter"}]},"layout":{"margin":{"b":0,"l":0,"r":0,"t":30}}},"title":{"font":{"size":15,"color":"#e4e4e7"},"text":"Mean vehicle rating by vehicle (1-5)","x":0.5,"xanchor":"center"},"font":{"family":"Georgia, serif","size":13,"color":"#e4e4e7"},"margin":{"l":10,"r":10,"t":60,"b":40},"hoverlabel":{"font":{"family":"Georgia, serif","size":12,"color":"#e4e4e7"},"bgcolor":"#27272a","bordercolor":"#eb841b","align":"left"},"paper_bgcolor":"#18181b","plot_bgcolor":"#18181b","height":300,"showlegend":false,"dragmode":false,"xaxis":{"gridcolor":"#3f3f46","zeroline":false,"linecolor":"#3f3f46","tickcolor":"#3f3f46","automargin":true,"showgrid":false,"showticklabels":false,"visible":false,"range":[0,5.674702380952381]},"yaxis":{"gridcolor":"#3f3f46","zeroline":false,"linecolor":"#3f3f46","tickcolor":"#3f3f46","automargin":true,"showgrid":false}},                        {"displayModeBar": false, "responsive": true}                    ).then(function(){
                            
var gd = document.getElementById('23431786-936b-4372-a607-623c685650d7');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };            </script>        </div>
</div>
<figcaption class="quarto-float-caption-margin quarto-float-caption quarto-float-fig margin-caption" id="fig-vehicle-scores-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
Figure&nbsp;2: Mean vehicle rating by vehicle, all models pooled.
</figcaption>
</figure>
</div>
</div>
<p>If labs were training on the benchmark, you’d expect bicycles near the top of this ranking. They’re not. However, the same caveat applies here. A bicycle is harder to draw than a skateboard: it needs two matching wheels, a frame that reaches both axles, handlebars, a seat, and pedals. The judge flags a missing or disconnected one of those on 2/3 of the bicycle images. You can train on bicycle images and still not do a great job relative to simpler vehicles.</p>
<p>One note on the plane, though: I should’ve picked “airplane” instead of “plane” because models often read it geometrically. They drew the animal standing on a flat surface instead of flying an aircraft. The plane is the only vehicle where the feature extractor sometimes found no vehicle at all (25 of 168 images, against zero for the other five), and 20% of plane images scored a 1 or 2 on the vehicle rating, against 5% for bicycles and none at all for boats, scooters, or skateboards.</p>
</section>
<section id="evidence-4-labs-are-not-better-at-drawing-pelicans-on-bicycles-even-adjusting-for-difficulty" class="level2 page-columns page-full">
<h2 class="anchored" data-anchor-id="evidence-4-labs-are-not-better-at-drawing-pelicans-on-bicycles-even-adjusting-for-difficulty">Evidence #4: Labs are not better at drawing pelicans on bicycles, even adjusting for difficulty</h2>
<p>Put the two together and the “pelican on a bicycle” ends up near the bottom of the ranking, at #42 of 48:</p>
<div id="cell-fig-cell-ranking" class="cell page-columns page-full" data-execution_count="4">
<div id="fig-cell-ranking" class="cell-output cell-output-display quarto-float quarto-figure quarto-figure-center anchored page-columns page-full">
<figure class="quarto-float quarto-float-fig figure page-columns page-full">
<div aria-describedby="fig-cell-ranking-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
<div>            <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG" type="5f8209360523110751b003df-text/javascript"></script><script type="5f8209360523110751b003df-text/javascript">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}</script>                <script type="5f8209360523110751b003df-text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-3.0.1.min.js" type="5f8209360523110751b003df-text/javascript"></script>                <div id="8894c22d-c9ac-424e-894b-f6677dbb9254" class="plotly-graph-div" style="height:950px; width:100%;"></div>            <script type="5f8209360523110751b003df-text/javascript">                window.PLOTLYENV=window.PLOTLYENV || {};                                if (document.getElementById("8894c22d-c9ac-424e-894b-f6677dbb9254")) {                    Plotly.newPlot(                        "8894c22d-c9ac-424e-894b-f6677dbb9254",                        [{"hoverinfo":"skip","line":{"color":"#3f3f46","width":1},"mode":"lines","x":[1,3.4603174603174605,null,1,3.4603174603174605,null,1,3.7142857142857144,null,1,3.761904761904762,null,1,3.793650793650794,null,1,3.8412698412698414,null,1,3.8888888888888893,null,1,3.8888888888888893,null,1,3.9365079365079367,null,1,4.031746031746032,null,1,4.031746031746032,null,1,4.0476190476190474,null,1,4.07936507936508,null,1,4.07936507936508,null,1,4.111111111111111,null,1,4.111111111111111,null,1,4.142857142857143,null,1,4.158730158730158,null,1,4.2063492063492065,null,1,4.222222222222221,null,1,4.222222222222222,null,1,4.253968253968254,null,1,4.301587301587301,null,1,4.301587301587301,null,1,4.333333333333333,null,1,4.333333333333333,null,1,4.380952380952381,null,1,4.412698412698413,null,1,4.428571428571429,null,1,4.444444444444445,null,1,4.4603174603174605,null,1,4.507936507936508,null,1,4.507936507936508,null,1,4.507936507936508,null,1,4.571428571428571,null,1,4.571428571428571,null,1,4.587301587301588,null,1,4.603174603174604,null,1,4.619047619047619,null,1,4.619047619047619,null,1,4.666666666666667,null,1,4.666666666666667,null,1,4.682539682539682,null,1,4.714285714285714,null,1,4.714285714285714,null,1,4.777777777777778,null,1,4.841269841269842,null,1,4.873015873015873,null],"y":["antelope + plane","antelope + plane",null,"heron + plane","heron + plane",null,"whale + bicycle","whale + bicycle",null,"flamingo + bicycle","flamingo + bicycle",null,"antelope + bicycle","antelope + bicycle",null,"otter + unicycle","otter + unicycle",null,"pelican + bicycle","pelican + bicycle",null,"flamingo + plane","flamingo + plane",null,"otter + bicycle","otter + bicycle",null,"whale + plane","whale + plane",null,"antelope + unicycle","antelope + unicycle",null,"cat + bicycle","cat + bicycle",null,"flamingo + unicycle","flamingo + unicycle",null,"whale + unicycle","whale + unicycle",null,"raccoon + unicycle","raccoon + unicycle",null,"pelican + unicycle","pelican + unicycle",null,"pelican + scooter","pelican + scooter",null,"raccoon + bicycle","raccoon + bicycle",null,"cat + unicycle","cat + unicycle",null,"whale + scooter","whale + scooter",null,"heron + bicycle","heron + bicycle",null,"antelope + scooter","antelope + scooter",null,"otter + scooter","otter + scooter",null,"heron + unicycle","heron + unicycle",null,"cat + scooter","cat + scooter",null,"flamingo + scooter","flamingo + scooter",null,"otter + plane","otter + plane",null,"raccoon + scooter","raccoon + scooter",null,"raccoon + plane","raccoon + plane",null,"otter + skateboard","otter + skateboard",null,"pelican + plane","pelican + plane",null,"whale + skateboard","whale + skateboard",null,"antelope + skateboard","antelope + skateboard",null,"flamingo + boat","flamingo + boat",null,"pelican + skateboard","pelican + skateboard",null,"whale + boat","whale + boat",null,"heron + scooter","heron + scooter",null,"flamingo + skateboard","flamingo + skateboard",null,"heron + skateboard","heron + skateboard",null,"otter + boat","otter + boat",null,"raccoon + skateboard","raccoon + skateboard",null,"cat + plane","cat + plane",null,"pelican + boat","pelican + boat",null,"cat + skateboard","cat + skateboard",null,"antelope + boat","antelope + boat",null,"heron + boat","heron + boat",null,"raccoon + boat","raccoon + boat",null,"cat + boat","cat + boat",null],"type":"scatter"},{"hovertemplate":"\u003cb\u003e%{y}\u003c\u002fb\u003e\u003cbr\u003e%{x:.2f} out of 5\u003cextra\u003e\u003c\u002fextra\u003e","marker":{"color":["#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#eb841b","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a","#71717a"],"size":[8,8,8,8,8,8,13,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]},"mode":"markers","x":{"dtype":"f8","bdata":"7Lqu67quC0Dsuq7ruq4LQG7btm3btg1AhmEYhmEYDkCXZVmWZVkOQK\u002fruq7rug5AyHEcx3EcD0DIcRzHcRwPQOD3fd\u002f3fQ9ACIIgCIIgEEAIgiAIgiAQQAzDMAzDMBBAFUVRFEVREEAVRVEURVEQQBzHcRzHcRBAHMdxHMdxEEAlSZIkSZIQQCiKoiiKohBANU3TNE3TEEA4juM4juMQQDmO4ziO4xBAQRAEQRAEEUBN0zRN0zQRQE3TNE3TNBFAVVVVVVVVEUBVVVVVVVURQGIYhmEYhhFAapqmaZqmEUBu27Zt27YRQHIcx3EcxxFAdl3XdV3XEUCCIAiCIAgSQIIgCIIgCBJAgiAIgiAIEkCSJEmSJEkSQJIkSZIkSRJAl2VZlmVZEkCbpmmapmkSQJ7neZ7neRJAnud5nud5EkCrqqqqqqoSQKuqqqqqqhJAruu6ruu6EkC3bdu2bdsSQLdt27Zt2xJAx3Ecx3EcE0DYdV3XdV0TQN\u002f3fd\u002f3fRNA"},"y":["antelope + plane","heron + plane","whale + bicycle","flamingo + bicycle","antelope + bicycle","otter + unicycle","pelican + bicycle","flamingo + plane","otter + bicycle","whale + plane","antelope + unicycle","cat + bicycle","flamingo + unicycle","whale + unicycle","raccoon + unicycle","pelican + unicycle","pelican + scooter","raccoon + bicycle","cat + unicycle","whale + scooter","heron + bicycle","antelope + scooter","otter + scooter","heron + unicycle","cat + scooter","flamingo + scooter","otter + plane","raccoon + scooter","raccoon + plane","otter + skateboard","pelican + plane","whale + skateboard","antelope + skateboard","flamingo + boat","pelican + skateboard","whale + boat","heron + scooter","flamingo + skateboard","heron + skateboard","otter + boat","raccoon + skateboard","cat + plane","pelican + boat","cat + skateboard","antelope + boat","heron + boat","raccoon + boat","cat + boat"],"type":"scatter"}],                        {"template":{"data":{"scatter":[{"type":"scatter"}]},"layout":{"margin":{"b":0,"l":0,"r":0,"t":30}}},"title":{"font":{"size":15,"color":"#e4e4e7"},"text":"All 48 combos ranked — pelican + bicycle is #42","x":0.5,"xanchor":"center"},"font":{"family":"Georgia, serif","size":13,"color":"#e4e4e7"},"margin":{"l":10,"r":10,"t":60,"b":40},"hoverlabel":{"font":{"family":"Georgia, serif","size":12,"color":"#e4e4e7"},"bgcolor":"#27272a","bordercolor":"#eb841b","align":"left"},"paper_bgcolor":"#18181b","plot_bgcolor":"#18181b","height":950,"showlegend":false,"dragmode":false,"xaxis":{"gridcolor":"#3f3f46","zeroline":false,"linecolor":"#3f3f46","tickcolor":"#3f3f46","automargin":true,"title":{"font":{"color":"#a1a1aa"},"text":"Mean judge score (1-5)"},"range":[1,5]},"yaxis":{"gridcolor":"#3f3f46","zeroline":false,"linecolor":"#3f3f46","tickcolor":"#3f3f46","automargin":true,"tickfont":{"size":11},"showgrid":false}},                        {"displayModeBar": false, "responsive": true}                    ).then(function(){
                            
var gd = document.getElementById('8894c22d-c9ac-424e-894b-f6677dbb9254');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };            </script>        </div>
</div>
<figcaption class="quarto-float-caption-margin quarto-float-caption quarto-float-fig margin-caption" id="fig-cell-ranking-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
Figure&nbsp;3: All 48 combos ranked; pelican + bicycle highlighted.
</figcaption>
</figure>
</div>
</div>
<p>But again, some combinations might be just harder to draw than others.</p>
<p>To account for that, I fit a fixed-effects regression on all 1,008 images: score ~ lab + animal × vehicle, plus per-lab interaction terms for pelican, bicycle, and the pelican-bicycle cell, with robust standard errors. The animal × vehicle terms absorb the inherent difficulty of all 48 combinations. The interactions measure each lab’s benchmark-specific boost relative to the average lab, with confidence intervals.</p>
<p>The results:</p>
<ol type="1">
<li>Every per-lab pelican effect (the lab’s boost on pelicans across all six vehicles) lands between -0.11 and +0.14 judge points, and none comes close to significance (smallest p = 0.25).</li>
<li>The per-lab bicycle effects (the lab’s boost on bicycles across all eight animals) run from <em>Grok 4.5</em> at -0.18 (p=0.11) to <em>Gemini 3.5 Flash</em> at +0.27 (p=0.022). Only Gemini clears p &lt; 0.05, and the seven point in both directions.</li>
<li>No pelican-bicycle cell effect (the <em>extra</em> boost on the specific combination, on top of the lab’s pelican and bicycle effects) clears p &lt; 0.05. The largest positive is <em>GLM-5.2</em> at +0.35 (p=0.12), which is the one I mentioned earlier. It’s the closest thing to a signal in this experiment, but still within chance.</li>
</ol>
<p>Here are the full per-lab estimates. A pelicanmaxxing lab would show dots to the right of the zero line across its whole row:</p>
<div id="cell-fig-regression-effects" class="cell page-columns page-full" data-execution_count="5">
<div id="fig-regression-effects" class="cell-output cell-output-display quarto-float quarto-figure quarto-figure-center anchored page-columns page-full">
<figure class="quarto-float quarto-float-fig figure page-columns page-full">
<div aria-describedby="fig-regression-effects-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
<div>            <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG" type="5f8209360523110751b003df-text/javascript"></script><script type="5f8209360523110751b003df-text/javascript">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}</script>                <script type="5f8209360523110751b003df-text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-3.0.1.min.js" type="5f8209360523110751b003df-text/javascript"></script>                <div id="54f86adb-be26-4562-ac45-df33d31e3594" class="plotly-graph-div" style="height:420px; width:100%;"></div>            <script type="5f8209360523110751b003df-text/javascript">                window.PLOTLYENV=window.PLOTLYENV || {};                                if (document.getElementById("54f86adb-be26-4562-ac45-df33d31e3594")) {                    Plotly.newPlot(                        "54f86adb-be26-4562-ac45-df33d31e3594",                        [{"hoverinfo":"skip","line":{"color":"#71717a","width":2},"mode":"lines","x":[-0.2461852684750736,0.2552555632596561],"y":["claude-sonnet-5","claude-sonnet-5"],"type":"scatter","xaxis":"x","yaxis":"y"},{"hovertemplate":"%{hovertext}\u003cextra\u003e\u003c\u002fextra\u003e","hovertext":["\u003cb\u003eclaude-sonnet-5\u003c\u002fb\u003e\u003cbr\u003e+0.00 judge points\u003cbr\u003e95% CI -0.25 to +0.26\u003cbr\u003ep = 0.972"],"marker":{"color":"#71717a","size":9},"mode":"markers","x":[0.0045351473922912],"y":["claude-sonnet-5"],"type":"scatter","xaxis":"x","yaxis":"y"},{"hoverinfo":"skip","line":{"color":"#71717a","width":2},"mode":"lines","x":[-0.322215384681117,0.1027142508942681],"y":["gemini-3.5-flash","gemini-3.5-flash"],"type":"scatter","xaxis":"x","yaxis":"y"},{"hovertemplate":"%{hovertext}\u003cextra\u003e\u003c\u002fextra\u003e","hovertext":["\u003cb\u003egemini-3.5-flash\u003c\u002fb\u003e\u003cbr\u003e-0.11 judge points\u003cbr\u003e95% CI -0.32 to +0.10\u003cbr\u003ep = 0.311"],"marker":{"color":"#71717a","size":9},"mode":"markers","x":[-0.1097505668934244],"y":["gemini-3.5-flash"],"type":"scatter","xaxis":"x","yaxis":"y"},{"hoverinfo":"skip","line":{"color":"#71717a","width":2},"mode":"lines","x":[-0.0852415404954648,0.2530419940102044],"y":["deepseek-v4-pro","deepseek-v4-pro"],"type":"scatter","xaxis":"x","yaxis":"y"},{"hovertemplate":"%{hovertext}\u003cextra\u003e\u003c\u002fextra\u003e","hovertext":["\u003cb\u003edeepseek-v4-pro\u003c\u002fb\u003e\u003cbr\u003e+0.08 judge points\u003cbr\u003e95% CI -0.09 to +0.25\u003cbr\u003ep = 0.331"],"marker":{"color":"#71717a","size":9},"mode":"markers","x":[0.0839002267573697],"y":["deepseek-v4-pro"],"type":"scatter","xaxis":"x","yaxis":"y"},{"hoverinfo":"skip","line":{"color":"#71717a","width":2},"mode":"lines","x":[-0.3062733060468178,0.1439150294028262],"y":["grok-4.5","grok-4.5"],"type":"scatter","xaxis":"x","yaxis":"y"},{"hovertemplate":"%{hovertext}\u003cextra\u003e\u003c\u002fextra\u003e","hovertext":["\u003cb\u003egrok-4.5\u003c\u002fb\u003e\u003cbr\u003e-0.08 judge points\u003cbr\u003e95% CI -0.31 to +0.14\u003cbr\u003ep = 0.480"],"marker":{"color":"#71717a","size":9},"mode":"markers","x":[-0.0811791383219958],"y":["grok-4.5"],"type":"scatter","xaxis":"x","yaxis":"y"},{"hoverinfo":"skip","line":{"color":"#71717a","width":2},"mode":"lines","x":[-0.1914546061324122,0.1878264882185777],"y":["qwen3.7-max","qwen3.7-max"],"type":"scatter","xaxis":"x","yaxis":"y"},{"hovertemplate":"%{hovertext}\u003cextra\u003e\u003c\u002fextra\u003e","hovertext":["\u003cb\u003eqwen3.7-max\u003c\u002fb\u003e\u003cbr\u003e-0.00 judge points\u003cbr\u003e95% CI -0.19 to +0.19\u003cbr\u003ep = 0.985"],"marker":{"color":"#71717a","size":9},"mode":"markers","x":[-0.0018140589569172],"y":["qwen3.7-max"],"type":"scatter","xaxis":"x","yaxis":"y"},{"hoverinfo":"skip","line":{"color":"#71717a","width":2},"mode":"lines","x":[-0.238119480726064,0.1773485056693746],"y":["gpt-5.6-terra","gpt-5.6-terra"],"type":"scatter","xaxis":"x","yaxis":"y"},{"hovertemplate":"%{hovertext}\u003cextra\u003e\u003c\u002fextra\u003e","hovertext":["\u003cb\u003egpt-5.6-terra\u003c\u002fb\u003e\u003cbr\u003e-0.03 judge points\u003cbr\u003e95% CI -0.24 to +0.18\u003cbr\u003ep = 0.774"],"marker":{"color":"#71717a","size":9},"mode":"markers","x":[-0.0303854875283446],"y":["gpt-5.6-terra"],"type":"scatter","xaxis":"x","yaxis":"y"},{"hoverinfo":"skip","line":{"color":"#71717a","width":2},"mode":"lines","x":[-0.0931924446300317,0.362580199732074],"y":["glm-5.2","glm-5.2"],"type":"scatter","xaxis":"x","yaxis":"y"},{"hovertemplate":"%{hovertext}\u003cextra\u003e\u003c\u002fextra\u003e","hovertext":["\u003cb\u003eglm-5.2\u003c\u002fb\u003e\u003cbr\u003e+0.13 judge points\u003cbr\u003e95% CI -0.09 to +0.36\u003cbr\u003ep = 0.247"],"marker":{"color":"#71717a","size":9},"mode":"markers","x":[0.1346938775510211],"y":["glm-5.2"],"type":"scatter","xaxis":"x","yaxis":"y"},{"hoverinfo":"skip","line":{"color":"#71717a","width":2},"mode":"lines","x":[-0.1470057489214034,0.2286384019826284],"y":["claude-sonnet-5","claude-sonnet-5"],"type":"scatter","xaxis":"x2","yaxis":"y2"},{"hovertemplate":"%{hovertext}\u003cextra\u003e\u003c\u002fextra\u003e","hovertext":["\u003cb\u003eclaude-sonnet-5\u003c\u002fb\u003e\u003cbr\u003e+0.04 judge points\u003cbr\u003e95% CI -0.15 to +0.23\u003cbr\u003ep = 0.670"],"marker":{"color":"#71717a","size":9},"mode":"markers","x":[0.0408163265306124],"y":["claude-sonnet-5"],"type":"scatter","xaxis":"x2","yaxis":"y2"},{"hoverinfo":"skip","line":{"color":"#eb841b","width":2},"mode":"lines","x":[0.0382336260680011,0.494192677786876],"y":["gemini-3.5-flash","gemini-3.5-flash"],"type":"scatter","xaxis":"x2","yaxis":"y2"},{"hovertemplate":"%{hovertext}\u003cextra\u003e\u003c\u002fextra\u003e","hovertext":["\u003cb\u003egemini-3.5-flash\u003c\u002fb\u003e\u003cbr\u003e+0.27 judge points\u003cbr\u003e95% CI +0.04 to +0.49\u003cbr\u003ep = 0.022"],"marker":{"color":"#eb841b","size":9},"mode":"markers","x":[0.2662131519274386],"y":["gemini-3.5-flash"],"type":"scatter","xaxis":"x2","yaxis":"y2"},{"hoverinfo":"skip","line":{"color":"#71717a","width":2},"mode":"lines","x":[-0.3486476171287027,0.1826612225708767],"y":["deepseek-v4-pro","deepseek-v4-pro"],"type":"scatter","xaxis":"x2","yaxis":"y2"},{"hovertemplate":"%{hovertext}\u003cextra\u003e\u003c\u002fextra\u003e","hovertext":["\u003cb\u003edeepseek-v4-pro\u003c\u002fb\u003e\u003cbr\u003e-0.08 judge points\u003cbr\u003e95% CI -0.35 to +0.18\u003cbr\u003ep = 0.540"],"marker":{"color":"#71717a","size":9},"mode":"markers","x":[-0.0829931972789129],"y":["deepseek-v4-pro"],"type":"scatter","xaxis":"x2","yaxis":"y2"},{"hoverinfo":"skip","line":{"color":"#71717a","width":2},"mode":"lines","x":[-0.3899316385505862,0.0398182598657805],"y":["grok-4.5","grok-4.5"],"type":"scatter","xaxis":"x2","yaxis":"y2"},{"hovertemplate":"%{hovertext}\u003cextra\u003e\u003c\u002fextra\u003e","hovertext":["\u003cb\u003egrok-4.5\u003c\u002fb\u003e\u003cbr\u003e-0.18 judge points\u003cbr\u003e95% CI -0.39 to +0.04\u003cbr\u003ep = 0.110"],"marker":{"color":"#71717a","size":9},"mode":"markers","x":[-0.1750566893424028],"y":["grok-4.5"],"type":"scatter","xaxis":"x2","yaxis":"y2"},{"hoverinfo":"skip","line":{"color":"#71717a","width":2},"mode":"lines","x":[-0.1878011664980676,0.1995925497180254],"y":["qwen3.7-max","qwen3.7-max"],"type":"scatter","xaxis":"x2","yaxis":"y2"},{"hovertemplate":"%{hovertext}\u003cextra\u003e\u003c\u002fextra\u003e","hovertext":["\u003cb\u003eqwen3.7-max\u003c\u002fb\u003e\u003cbr\u003e+0.01 judge points\u003cbr\u003e95% CI -0.19 to +0.20\u003cbr\u003ep = 0.952"],"marker":{"color":"#71717a","size":9},"mode":"markers","x":[0.0058956916099789],"y":["qwen3.7-max"],"type":"scatter","xaxis":"x2","yaxis":"y2"},{"hoverinfo":"skip","line":{"color":"#71717a","width":2},"mode":"lines","x":[-0.180817267666618,0.2116562699341891],"y":["gpt-5.6-terra","gpt-5.6-terra"],"type":"scatter","xaxis":"x2","yaxis":"y2"},{"hovertemplate":"%{hovertext}\u003cextra\u003e\u003c\u002fextra\u003e","hovertext":["\u003cb\u003egpt-5.6-terra\u003c\u002fb\u003e\u003cbr\u003e+0.02 judge points\u003cbr\u003e95% CI -0.18 to +0.21\u003cbr\u003ep = 0.878"],"marker":{"color":"#71717a","size":9},"mode":"markers","x":[0.0154195011337855],"y":["gpt-5.6-terra"],"type":"scatter","xaxis":"x2","yaxis":"y2"},{"hoverinfo":"skip","line":{"color":"#71717a","width":2},"mode":"lines","x":[-0.2939865851192713,0.1533970159582718],"y":["glm-5.2","glm-5.2"],"type":"scatter","xaxis":"x2","yaxis":"y2"},{"hovertemplate":"%{hovertext}\u003cextra\u003e\u003c\u002fextra\u003e","hovertext":["\u003cb\u003eglm-5.2\u003c\u002fb\u003e\u003cbr\u003e-0.07 judge points\u003cbr\u003e95% CI -0.29 to +0.15\u003cbr\u003ep = 0.538"],"marker":{"color":"#71717a","size":9},"mode":"markers","x":[-0.0702947845804997],"y":["glm-5.2"],"type":"scatter","xaxis":"x2","yaxis":"y2"},{"hoverinfo":"skip","line":{"color":"#71717a","width":2},"mode":"lines","x":[-1.1678600300574509,0.006862297631147],"y":["claude-sonnet-5","claude-sonnet-5"],"type":"scatter","xaxis":"x3","yaxis":"y3"},{"hovertemplate":"%{hovertext}\u003cextra\u003e\u003c\u0