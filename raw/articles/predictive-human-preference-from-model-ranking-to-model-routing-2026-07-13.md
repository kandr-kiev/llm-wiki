---
source_url: https://huyenchip.com//2024/02/28/predictive-human-preference.html
ingested: 2026-07-13
sha256: cc2b2677863219a8660ae4618c7a7fbb7ea1d3a6250adaa6ef89677d6627747e
blog_source: Chip Huyen
---
<!DOCTYPE html>
<html lang="en">

  <head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>Predictive Human Preference: From Model Ranking to Model Routing</title>
  <meta name="description" content="A challenge of building AI applications is choosing which model to use. What if we don’t have to? What if we can predict the best model for any prompt? Predi...">
  
  <link rel="stylesheet" href="/assets/main.css">
  <link rel="canonical" href="https://huyenchip.com/2024/02/28/predictive-human-preference.html">
  <link rel="alternate" type="application/rss+xml" title="Chip Huyen" href="/feed.xml">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css" rel="stylesheet">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/js/lightbox.min.js"></script>

  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-MRNJDX3023"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-MRNJDX3023');
  </script>

  
  
  <script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-103070243-1', 'auto');
  ga('send', 'pageview');

</script>
  

  <!-- for mathjax support -->
  
  <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
    TeX: { equationNumbers: { autoNumber: "AMS" } }
    });
  </script>
  <script type="text/javascript" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
  

  <!--  -->
  <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script type="text/javascript" src="https://pixel-v0.wl.r.appspot.com/static/pixel.js"></script>
<script type="text/javascript">
    let ccid = "huyenchip.com";
    cc(ccid);
</script> -->
  <!-- SEO tags -->
  <!-- Begin Jekyll SEO tag v2.8.0 -->
<title>Predictive Human Preference: From Model Ranking to Model Routing | Chip Huyen</title>
<meta name="generator" content="Jekyll v3.10.0" />
<meta property="og:title" content="Predictive Human Preference: From Model Ranking to Model Routing" />
<meta name="author" content="Chip Huyen" />
<meta property="og:locale" content="en_US" />
<meta name="description" content="A challenge of building AI applications is choosing which model to use. What if we don’t have to? What if we can predict the best model for any prompt? Predictive human preference aims to predict which model users might prefer for a specific query." />
<meta property="og:description" content="A challenge of building AI applications is choosing which model to use. What if we don’t have to? What if we can predict the best model for any prompt? Predictive human preference aims to predict which model users might prefer for a specific query." />
<link rel="canonical" href="https://huyenchip.com/2024/02/28/predictive-human-preference.html" />
<meta property="og:url" content="https://huyenchip.com/2024/02/28/predictive-human-preference.html" />
<meta property="og:site_name" content="Chip Huyen" />
<meta property="og:image" content="https://huyenchip.com/assets/pics/predictive-preference/8-easy-hard-prompts.png" />
<meta property="og:type" content="article" />
<meta property="article:published_time" content="2024-02-28T00:00:00+00:00" />
<meta name="twitter:card" content="summary_large_image" />
<meta property="twitter:image" content="https://huyenchip.com/assets/pics/predictive-preference/8-easy-hard-prompts.png" />
<meta property="twitter:title" content="Predictive Human Preference: From Model Ranking to Model Routing" />
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Chip Huyen"},"dateModified":"2024-02-28T00:00:00+00:00","datePublished":"2024-02-28T00:00:00+00:00","description":"A challenge of building AI applications is choosing which model to use. What if we don’t have to? What if we can predict the best model for any prompt? Predictive human preference aims to predict which model users might prefer for a specific query.","headline":"Predictive Human Preference: From Model Ranking to Model Routing","image":"https://huyenchip.com/assets/pics/predictive-preference/8-easy-hard-prompts.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://huyenchip.com/2024/02/28/predictive-human-preference.html"},"url":"https://huyenchip.com/2024/02/28/predictive-human-preference.html"}</script>
<!-- End Jekyll SEO tag -->

<meta name="cf-2fa-verify" content="YpmKnmQEEb22PZui8RFD">
</head>


  <body>

    <header class="site-header" role="banner">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">

  <div class="wrapper">
    
    
    <a class="site-title" href="/">Chip Huyen</a>


    
      <nav class="site-nav">
        <input type="checkbox" id="nav-trigger" class="nav-trigger" />
        <label for="nav-trigger">
          <span class="menu-icon">
            <svg viewBox="0 0 18 15" width="18px" height="15px">
              <path fill="#424242" d="M18,1.484c0,0.82-0.665,1.484-1.484,1.484H1.484C0.665,2.969,0,2.304,0,1.484l0,0C0,0.665,0.665,0,1.484,0 h15.031C17.335,0,18,0.665,18,1.484L18,1.484z"/>
              <path fill="#424242" d="M18,7.516C18,8.335,17.335,9,16.516,9H1.484C0.665,9,0,8.335,0,7.516l0,0c0-0.82,0.665-1.484,1.484-1.484 h15.031C17.335,6.031,18,6.696,18,7.516L18,7.516z"/>
              <path fill="#424242" d="M18,13.516C18,14.335,17.335,15,16.516,15H1.484C0.665,15,0,14.335,0,13.516l0,0 c0-0.82,0.665-1.484,1.484-1.484h15.031C17.335,12.031,18,12.696,18,13.516L18,13.516z"/>
            </svg>
          </span>
        </label>

        <div class="trigger">
          
            
              <a class="page-link" href="/blog/">Blog</a>
            
          
            
              <a class="page-link" href="/books/">Books</a>
            
          
            
              <a class="page-link" href="/events/">Events</a>
            
          
            
              <div class="dropdown">
                <a class="dropbtn">AI Guide<i class="fas fa-chevron-down"></i></a>
                <ul class="dropdown-content">
                  
                    <li><a href="/mlops/">AI Roadmap</a></li>
                  
                    <li><a href="https://goodailist.com">Good AI List</a></li>
                  
                    <li><a href="https://huyenchip.com/ml-interviews-book/">ML Interviews</a></li>
                  
                </ul>
              </div>
            
          
            
              <a class="page-link" href="/list-100/">List 100</a>
            
          
            
              <a class="page-link" href="https://instagram.com/chipslib">Chip's Lib</a>
            
          
            
              <a class="page-link" href="https://huyenchip.com/vn/">VN</a>
            
          
        </div>

        <!-- this is the original working code -->
        <!-- <div class="trigger">
          
            <a class="page-link" href="/blog/">Blog</a>
          
            <a class="page-link" href="/books/">Books</a>
          
            <a class="page-link" href="/events/">Events</a>
          
            <a class="page-link" href="">AI Guide</a>
          
            <a class="page-link" href="/list-100/">List 100</a>
          
            <a class="page-link" href="https://instagram.com/chipslib">Chip's Lib</a>
          
            <a class="page-link" href="https://huyenchip.com/vn/">VN</a>
          
        </div> -->

        <!-- No idea what it is -->
        <!-- <div class="trigger">
          
            
            
            <a class="page-link" href="/about/">About</a>
            
          
            
            
            <a class="page-link" href="/stories/anything-i-want.html">Anything I want</a>
            
          
            
            
            <a class="page-link" href="/archive/">Archive</a>
            
          
            
            
            <a class="page-link" href="/blog/">Blog</a>
            
          
            
            
            <a class="page-link" href="/books/">Books</a>
            
          
            
            
            <a class="page-link" href="/communication/">Contact me</a>
            
          
            
            
            <a class="page-link" href="/creators/">Creators&#39; Collective</a>
            
          
            
            
            <a class="page-link" href="/entanglements/">Entanglements That Never End</a>
            
          
            
            
            <a class="page-link" href="/events/">Events</a>
            
          
            
            
          
            
            
            <a class="page-link" href="/stories/how-they-arrived">How they arrived</a>
            
          
            
            
          
            
            
            <a class="page-link" href="/list-100/">List 100</a>
            
          
            
            
            <a class="page-link" href="/llama-devs.html">Open Source LLM Developers</a>
            
          
            
            
            <a class="page-link" href="/llama-police.html">Open Source LLM Tools</a>
            
          
            
            
          
            
            
            <a class="page-link" href="/mlops/">MLOps - tools, best practices, and case studies</a>
            
          
            
            
            <a class="page-link" href="/mlops/">MLOps guide</a>
            
          
            
            
            <a class="page-link" href="/stories/my-posthumous-collection-of-letters.html">My posthumous collection of letters</a>
            
          
            
            
            <a class="page-link" href="/stories/neo-beat">Unnamed</a>
            
          
            
            
            <a class="page-link" href="/research/">Research</a>
            
          
            
            
            <a class="page-link" href="/start/">You made it!</a>
            
          
            
            
            <a class="page-link" href="/stories/the-door.html">The door</a>
            
          
            
            
          
            
            
          
        </div> -->

      </nav>
    
  </div>
</header>


    <main class="page-content" aria-label="Content">
      <div class="wrapper">
        <!-- Sidebar Navigation, which can be customized for each post -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">


  <aside id="sidebar" class="sidebar">
    <span class="toc-title"><b>Table of Contents</b></span>
    <button id="close-sidebar-btn" class="close-btn"><i class="fas fa-chevron-down"></i></button>
      <a href="#ranking_models_using_human_preference">Ranking Models Using Human Preference</a>
<ul class="sidebar-list">
    <li><a href="#how_preferential_ranking_works">How Preferential Ranking Works</a></li>
    <li><a href="#correctness_of_chatbot_arena_ranking">Correctness of Chatbot Arena Ranking</a>
        <ul>
            <li><a href="#eval_data">Eval data</a></li>
            <li><a href="#results">Results</a></li>
        </ul>
    </li>
</ul>

<a href="#predicting_human_preference_for_each_prompt">Predicting Human Preference For Each Prompt</a>
<ul class="sidebar-list">
    <li><a href="#experiment_setup">Experiment setup</a></li>
    <li><a href="#experiment_results">Experiment results</a></li>
    <li><a href="#domain_specific_and_query_specific_leaderboards">Domain-specific and query-specific leaderboards</a></li>
</ul>

<a href="#conclusion">Conclusion</a>

  </aside>

  <!-- Button to reopen the sidebar -->
  <button id="open-sidebar-btn" class="open-btn" style="display:none;">
    Table of Contents <span class="chevron-icon"><i class="fas fa-chevron-up"></i></span>
  </button>


<script>
  
    // Function to handle sidebar visibility on resize
    function handleResize() {
      if (window.innerWidth <= 768) {
        // Automatically minimize the sidebar if it's open on small screens
        document.getElementById('sidebar').classList.add('sidebar-hidden');
        document.getElementById('open-sidebar-btn').style.display = 'block'; // Show open button
      }
    }
  
    // Add event listener for window resize
    window.addEventListener('resize', handleResize);
  
    // Call handleResize on page load to check the initial screen size
    handleResize();
  
    // Close sidebar and show "Table of Contents" button
    document.getElementById('close-sidebar-btn').addEventListener('click', function() {
      document.getElementById('sidebar').classList.add('sidebar-hidden');
      document.getElementById('open-sidebar-btn').style.display = 'block'; // Show open button
    });
  
    // Reopen the sidebar when "Table of Contents" is clicked
    document.getElementById('open-sidebar-btn').addEventListener('click', function() {
      document.getElementById('sidebar').classList.remove('sidebar-hidden');
      document.getElementById('open-sidebar-btn').style.display = 'none'; // Hide open button
    });
  
</script>

<article class="post" itemscope itemtype="http://schema.org/BlogPosting">

  <header class="post-header">
    <h1 class="post-title" itemprop="name headline">Predictive Human Preference: From Model Ranking to Model Routing</h1>
    <p class="post-meta">
      <time datetime="2024-02-28T00:00:00+00:00" itemprop="datePublished">
        
        Feb 28, 2024
      </time>
      
        • <span itemprop="author" itemscope itemtype="http://schema.org/Person"><span itemprop="name">Chip Huyen</span></span>
      </p>
  </header>

  <div class="post-content" itemprop="articleBody">
    <p>A challenge of building AI applications is choosing which model to use. What if we don’t have to? What if we can predict the best model for any prompt? Predictive human preference aims to predict which model users might prefer for a specific query.</p>

<p>Human preference has emerged to be both the Northstar and a powerful tool for AI model development. Human preference guides post-training techniques including <a href="https://huyenchip.com/2023/05/02/rlhf.html">RLHF</a> and <a href="https://arxiv.org/abs/2305.18290">DPO</a>. Human preference is also used to rank AI models, as used by LMSYS’s <a href="https://arena.lmsys.org/">Chatbot Arena</a>.</p>

<p>Chatbot Arena aims to determine which model is generally preferred. I wanted to see if it’s possible to predict which model is preferred <em>for each query</em>.</p>

<p>One use case of predictive human preference is model routing. For example, if we know in advance that for a prompt, users will prefer Claude Instant’s response over GPT-4, and Claude Instant is cheaper/faster than GPT-4, we can route this prompt to Claude Instant. Model routing has the potential to increase response quality while reducing costs and latency.</p>

<p>Another use case of predictive human preference is interpretability. Mapping out a model’s performance on different prompts can help us understand this model’s strengths and weaknesses. See section <strong>Experiment results</strong> for examples.</p>

<p>Here’s what predictive human preference for different model pairs looks like for the prompt “<em>What’s the best way to cluster text embeddings?</em>”. The predictions were generated by my toy preference predictor. The bright yellow color for the (GPT-4, GPT-3.5-Turbo) cell means that my predictor thinks GPT-4’s response is very likely to be preferred to that of GPT-3.5-Turbo’s for this prompt.</p>

<center>
    <figure>
    <img alt="Predictive human preference for all LLM model pairs" src="/assets/pics/predictive-preference/1-cluster.png" style="float: center; max-width: 90%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>This post first discusses the correctness of Chatbot Arena, which will then be used as a baseline to evaluate the correctness of preference predictions. It then discusses how to build a preference predictor and the initial results.</p>

<h2 id="ranking_models_using_human_preference">Ranking Models Using Human Preference</h2>

<p>Using preferential signals (comparisons) to rank models has grown in popularity in the last few years. Other than powering LMSYS’s <a href="https://arena.lmsys.org/">Chatbot Arena</a>, it’s also used by many model providers (<a href="https://arxiv.org/abs/2112.00861">Anthropic</a>, Gemini, ChatGPT, etc.) to evaluate their models in production.</p>

<center>
    <figure>
    <img alt="Predictive human preference for all LLM model pairs" src="/assets/pics/predictive-preference/2-chatgpt.png" style="float: center; max-width: 100%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p><strong>Side note</strong>: Friends who have deployed this in production told me that most users don’t read both options and just randomly vote for one. This introduces a lot of noise. However, the signals from the small percentage of users who vote correctly can sometimes be sufficient to help determine which model is preferred, as long as there’s minimal bias in the random voting.</p>

<h3 id="how_preferential_ranking_works">How Preferential Ranking Works</h3>

<p>Preferential ranking works in two steps:</p>

<ol>
  <li>Collect comparison data about user preference.</li>
  <li>Compute a model ranking from these comparisons.</li>
</ol>

<p>For each request, two or more models are selected to respond. An evaluator, which can be human or AI, picks the winner. The evaluator shouldn’t know which models are being judged. Each comparison is called a <em>match</em>. This process results in a series of comparisons.</p>

<table>
    <style>
        table {
          border-collapse: collapse;
          width: 100%;
        }

        th, td {
          padding: 8px;
          text-align: left;
          border-bottom: 1px solid #ddd;
        }
    </style>
    <tr>
      <td><strong>Match ID</strong></td>
    <td><strong>Prompt</strong>
    </td>
    <td><strong>Model A</strong>
    </td>
    <td><strong>Model B</strong>
    </td>
    <td><strong>Winner</strong>
    </td>
    </tr>
    <tr>
    <td>1
    </td>
    <td>…
    </td>
    <td>Model 1
    </td>
    <td>Model 2
    </td>
    <td>Model 1
    </td>
    </tr>
    <tr>
    <td>2
    </td>
    <td>…
    </td>
    <td>Model 3
    </td>
    <td>Model 1
    </td>
    <td>Model 1
    </td>
    </tr>
    <tr>
    <td>3
    </td>
    <td>…
    </td>
    <td>Model 1
    </td>
    <td>Model 4
    </td>
    <td>Model 4
    </td>
    </tr>
    <tr>
    <td> ...
    </td>
    <td> ...
    </td>
    <td> ...
    </td>
    <td> ...
    </td>
    <td> ...
    </td>
    </tr>
</table>
<p><br /></p>

<p>From these comparisons, we need to compute the rankings of all models. The two most common ranking algorithms are <a href="https://en.wikipedia.org/wiki/Elo_rating_system">Elo</a> (from chess) and <a href="https://en.wikipedia.org/wiki/TrueSkill">TrueSkill</a> (from video games).</p>

<p>While Chatbot Arena refers to their model scores “Elo scores”, they actually don’t use Elo. In December 2023, they switched to <a href="https://lmsys.org/blog/2023-12-07-leaderboard/#transition-from-online-elo-rating-system-to-bradley-terry-model">Bradley-Terry</a> but scaled the resulting scores to make them look Elo-like (see their <a href="https://colab.research.google.com/drive/1KdwokPjirkTmpO_P1WByFNFiqxWQquwH#scrollTo=HdZrGr4IcWCl">notebook</a>).</p>

<p>Given a history of match outcomes, the Bradley-Terry algorithm finds the model scores that maximize the likelihood of these match outcomes, turning model scoring into a maximum likelihood estimation problem. The input, for each training example, is the models that participate in the match. The output is the outcome of the match. Assuming there’s no draw, the outcome of a match is either 0 (a wins) or 1 (b wins).</p>

<center>
    <figure>
    <img alt="Predictive human preference for all LLM model pairs" src="/assets/pics/predictive-preference/3-bradley-terry.png" style="float: center; max-width: 90%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<h3 id="correctness_of_chatbot_arena_ranking">Correctness of Chatbot Arena Ranking</h3>

<p>Given the same match outcomes, different ranking algorithms can produce different rankings. For example, the ranking computed by Elo might differ from the ranking computed by Bradley-Terry. How do we know that a ranking is correct?</p>

<p>At its core, model ranking is a predictive problem. We compute a ranking from historical match outcomes and use it to predict future match outcomes. The quality of a ranking is determined by how accurately it can predict future match outcomes.</p>

<p>Let’s say we have a match between model A and model B. If model A has a higher score, meaning that the ranking algorithm predicts that A wins. If users indeed prefer the higher-ranking model, the ranking algorithm makes a correct prediction.</p>

<h4 id="eval_data">Eval data</h4>

<p>To compute the accuracy of Chatbot Arena ranking, I used their data published in July 2023, which consists of <a href="https://drive.google.com/file/d/1ZXiBRtADf9HZ8eEarIFTy-qrPNDUP_H0/view">33K crowd-sourced comparisons</a> for matches among 20 models. I used this smaller dataset instead of <a href="https://drive.google.com/file/d/1ZXiBRtADf9HZ8eEarIFTy-qrPNDUP_H0/view">their Jan 2024 dataset</a> because this smaller dataset contains the prompt used for each match, which I need for predictive human preference. Benchmarking on this dataset allows me to compare my model with the Bradley-Terry algorithm later on.</p>

<p>Here’s an example from their July 2023 dataset.</p>

<table>
    <style>
        table {
          border-collapse: collapse;
          width: 100%;
        }

        th:not(:last-child), td:not(:last-child) {
          padding: 8px;
          text-align: left;
          border-bottom: 1px solid #ddd;
          border-right: 1px solid #ddd;
        }
    </style>
  <tr>
   <td><strong>prompt</strong>
   </td>
   <td><strong>model_a</strong>
   </td>
   <td><strong>model_b</strong>
   </td>
   <td><strong>winner</strong>
   </td>
   <td><strong>model_a's response</strong>
   </td>
   <td><strong>model_b's response</strong>
   </td>
  </tr>
  <tr>
   <td>who was the last monarch of uk
   </td>
   <td>koala-13b
   </td>
   <td>vicuna-13b
   </td>
   <td>model_a
   </td>
   <td>The last monarch of the United Kingdom was Queen Elizabeth II, who reigned from 1952 to 2020.
   </td>
   <td>The current monarch of the United Kingdom is Queen Elizabeth II. She has been the monarch since 1952, and is the longest-reigning monarch in British history.
   </td>
  </tr>
</table>
<p><br /></p>

<p>For reference, the Bradley-Terry (BT) scores of the top 7 models in this dataset are as follows.</p>

<ol>
  <li>GPT-4: 1189</li>
  <li>Claude-v1: 1150</li>
  <li>Claude-instant-v1: 1110</li>
  <li>GPT-3.5-Turbo: 1104</li>
  <li>WizardLM-13B: 1058</li>
  <li>Vicuna-13b: 1040</li>
  <li>Guanaco-33b: 1031</li>
</ol>

<p>To create a test set, I randomly select 10% of the data (3300 examples). Each match has three possible outcomes: model_a wins, model_b wins, or tie. This can still be framed as a binary classification problem if we treat a tied match as two matches: one in which model_a wins and one in which model_b wins.</p>

<h4 id="results">Results</h4>

<p>I found that for all non-tie matches in my test set, the model with the higher Bradley-Terry score is preferred 74.1% of the time. This means that if we always predict the higher-ranked model as the winner for a match, we’d have an accuracy of 74.1%.</p>

<table>
  <tr>
   <td><strong>Test data</strong>
   </td>
   <td><strong>Output classes</strong>
   </td>
   <td><strong># samples</strong>
   </td>
   <td><strong>BT's accuracy</strong>
   </td>
  </tr>
  <tr>
   <td>All matches
   </td>
   <td>
        <ul>
            <li>model_a wins</li>
            <li>model_b wins</li>
            <li>tie</li>
        </ul>  
   </td>
   <td>3,300
   </td>
   <td>53.33%
   </td>
  </tr>
  <tr>
   <td>Non-tie matches
   </td>
   <td>
<ul>
    <li>model_a wins</li>
    <li>model_b wins</li>
</ul>
   </td>
   <td>2,367
   </td>
   <td>74.1%
   </td>
  </tr>
  <tr>
   <td>Non-tie matches involving GPT-4
   </td>
   <td>
        <ul>
            <li>model_a wins</li>
            <li>model_b wins</li>
        </ul>
   </td>
   <td>355
   </td>
   <td>85.1% (always pick GPT-4 as winner) </td>
  </tr>
</table>
<p><br /></p>

<p>Back in July 2023, GPT-4 was considered the strongest model by a long shot (this was before Gemini, Mistral, Claude-v2). Did users always prefer GPT-4 to all other models? They didn’t. In 355 non-tie matches involving GPT-4, GPT-4 wins 85.1%.</p>

<p>This means that even though GPT-4 is the best model overall, there are prompts for which other models can outperform GPT-4. If we can figure out which prompts these are, and which models work best for them, we can route these prompts to the best-performing models, improving the response quality.</p>

<h2 id="predicting_human_preference_for_each_prompt">Predicting Human Preference For Each Prompt</h2>

<p>If a ranking algorithm is about figuring out which model is better overall, predictive human preference is about figuring out which model is better for each prompt. If we know in advance that for a particular prompt, GPT-3.5 works just as well as GPT-4, and GPT-3.5 is cheaper, we can route that prompt to GPT-3.5 instead. Or if we know that Mistral-7B works just as well as GPT-4 and Mistral-7B is faster, we can route our query to Mistral-7B instead.</p>

<p>Model routing can also help with budget planning. Say, you only have enough budget to serve 50% of queries on the strongest model, and the rest to a weaker model, you want to make sure that you send to the weaker model only the queries that you’re confident it can do well on.</p>

<h3 id="experiment_setup">Experiment setup</h3>

<p>I treat predictive human preference as a binary classification task. Given a match between 2 models, predict which one wins. If the probability of model_a winning is around 0.5, it can be considered a tie. If a Bradley-Terry model takes only <code class="language-plaintext highlighter-rouge">(model_a, model_b)</code> as the input, a preference predictor takes <code class="language-plaintext highlighter-rouge">(prompt, model_a, model_b)</code> as the input.</p>

<center>
    <figure>
    <img alt="Predictive human preference for all LLM model pairs" src="/assets/pics/predictive-preference/4-preference-predictor.png" style="float: center; max-width: 90%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>The architecture of my preference predictor looks like this. The model encoder and preference predictor are neural networks that can be trained independently or together. I used DistilBERT as my prompt encoder.</p>

<center>
    <figure>
    <img alt="Predictive human preference for all LLM model pairs" src="/assets/pics/predictive-preference/5-predictive-preference-architecture.png" style="float: center; max-width: 100%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>To train my model, I used 90% of LMSYS’s July 2023 dataset. I found that the predictor performed better using only non-tie matches (as opposed to using both tie and non-tie matches). I randomly flipped the order of models in a match 50% of the time.</p>

<p>To evaluate my model, I used 10% of this data. This is the same test data used to evaluate the correctness of Chatbot Arena’s ranking above.</p>

<table>
  <tr>
   <td><strong>Split</strong>
   </td>
   <td><strong>All matches</strong>
   </td>
   <td><strong>Non-tie matches</strong>
   </td>
  </tr>
  <tr>
   <td>Train
   </td>
   <td>29,700
   </td>
   <td>20,927
   </td>
  </tr>
  <tr>
   <td>Test
   </td>
   <td>3,300
   </td>
   <td>2,367
   </td>
  </tr>
</table>
<p><br /></p>

<p><strong>Note</strong>: I should’ve made a separate validation set for hyperparameter tuning. However, given that I didn’t have a lot of data and this is only a proof of concept, I didn’t do it. (I’m also lazy.) The matches are among 20 models, corresponding to 190 model pairs. 20,927 comparisons mean that, on average, there are only 110 comparisons per model pair.</p>

<h3 id="experiment_results">Experiment results</h3>

<p>I evaluated my preference predictor under two settings:</p>

<ol>
  <li>Using only <code class="language-plaintext highlighter-rouge">model_a</code> and <code class="language-plaintext highlighter-rouge">model_b</code> as the input. This is to see whether this predictor, using only model names, can make better predictions about match outcomes than Chatbot Arena scores.</li>
  <li>Using <code class="language-plaintext highlighter-rouge">(prompt, model_a, model_b)</code> as the input. This is to see whether including prompts helps improve match outcome prediction.</li>
</ol>

<p>I found that for all non-tie matches, my preference predictor can predict the match outcome accurately 75% of the time if not using prompts, and 76.2% of the time if using prompts. This suggests that human preference for models does change depending on the prompt. While the improvement doesn’t seem much, a 2.1% improvement can be significant at scale.</p>

<table>
  <tr>
   <td><strong>Eval data</strong>
   </td>
   <td><strong># eval samples</strong>
   </td>
   <td><strong>Chatbot Arena</strong>
   </td>
   <td><strong>Preference predictor</strong><br />(without prompts)
   </td>
   <td><strong>Preference predictor</strong><br />(with prompts)
   </td>
  </tr>
  <tr>
   <td>Non-tie matches
   </td>
   <td>2,367
   </td>
   <td>74.1%
   </td>
   <td>75%
   </td>
   <td>76.2%
   </td>
  </tr>
  <tr>
   <td>Non-tie matches involving GPT-4
   </td>
   <td>355
   </td>
   <td>85.1%
   </td>
   <td>86.2%
   </td>
   <td>87%
   </td>
  </tr>
</table>
<p><br /></p>

<p>Keep in mind that this predictor was trained with a small amount of crowd-sourced (e.g. noisy) data. The prompts crowdsourced are also simple. Among <a href="https://huggingface.co/datasets/lmsys/chatbot_arena_conversations">33K prompts</a>, 180 (0.55%) of them are “hello” and “hi”. These simple prompts are insufficient to distinguish strong models from weak ones. I suspect that with more/better data, the performance of this predictor can significantly improve.</p>

<h3 id="domain_specific_and_query_specific_leaderboards">Domain-specific and query-specific leaderboards</h3>

<p>Recall that 20 models correspond to 190 model pairs. To visualize how the predictor captures human preference, for each evaluation prompt, I generated 190 different inputs, one for each model pair.</p>

<center>
    <figure>
    <img alt="Predictive human preference for all LLM model pairs" src="/assets/pics/predictive-preference/6-model-pairs.png" style="float: center; max-width: 50%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>I then visualized the 190 predictions for 190 model pairs in a 20 x 20 grid, as shown below for the prompt “Derive the elastic wave equation.” I only included 9 models in the plot to make it readable. The diagonal values refer to comparing a model to itself, so the predicted preference should be 0.5.</p>

<center>
    <figure>
    <img alt="Predictive human preference for all LLM model pairs" src="/assets/pics/predictive-preference/7-derive.png" style="float: center; max-width: 90%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>Given the predicted preference for all model pairs for a prompt, I used a Bradley-Terry model (the same ranking algorithm that LMSYS uses) to create a leaderboard for this prompt. I used the same scaling that LMSYS uses to make the scores look Elo-like. Here’s the ranking of the 9 models shown above for the query “Derive the elastic wave equation.”</p>

<p>This also means that with this preference predictor, we can create a leaderboard for any arbitrary subset of data. We can have a leaderboard specific to any domain.</p>

<table>
  <tr>
   <td colspan="2"><center><strong>Model ranking for the prompt</strong><em>"Derive the elastic wave equation."</em></center>
   </td>
  </tr>
  <tr>
   <td>gpt-4
   </td>
   <td>1214
   </td>
  </tr>
  <tr>
   <td>claude-v1
   </td>
   <td>1162
   </td>
  </tr>
  <tr>
   <td>gpt-3.5-turbo
   </td>
   <td>1104
   </td>
  </tr>
  <tr>
   <td>claude-instant-v1
   </td>
   <td>1110
   </td>
  </tr>
  <tr>
   <td>guanaco-33b
   </td>
   <td>1023
   </td>
  </tr>
  <tr>
   <td>vicuna-13b
   </td>
   <td>1007
   </td>
  </tr>
  <tr>
   <td>vicuna-7b
   </td>
   <td>985
   </td>
  </tr>
  <tr>
   <td>RWKV-4-Raven-14B
   </td>
   <td>970
   </td>
  </tr>
  <tr>
   <td>gpt4all-13b-snoozy
   </td>
   <td>915
   </td>
  </tr>
</table>
<p><br /></p>

<p>Despite being a toy predictor, the model seems to be able to capture different models’ performance patterns. One pattern is that for simple prompts, weak models can do (nearly) as well as strong models. For more challenging prompts, however, users are much more likely to prefer stronger models. Here’s a visualization of predicted human preference for an easy prompt (“hello, how are you?”) and a challenging prompt (“Explain why Planc length …”).</p>

<center>
    <figure>
    <img alt="Predictive human preference for all LLM model pairs" src="/assets/pics/predictive-preference/8-easy-hard-prompts.png" style="float: center; max-width: 100%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>Here are the model rankings for these two prompts. The score spread for the simple prompt is much less than the score spread for the challenging prompt. The models that are ranked differently for these two prompts are highlighted in red.</p>

<center>
    <figure>
    <img alt="Predictive human preference for all LLM model pairs" src="/assets/pics/predictive-preference/10-ranking.png" style="float: center; max-width: 80%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>The predictor is also the most confident that GPT-4 will be preferred for queries in Russian and queries that involve code writing. For example, the average predicted win rate for the following Russian query of GPT-4 against all other models is 91.55%. Notice that for this query, while claude-v1 is predicted to do well on this query, claude-instant-v1 is predicted to do poorly.</p>

<center>
    <figure>
    <img alt="Predictive human preference for all LLM model pairs" src="/assets/pics/predictive-preference/9-russian.png" style="float: center; max-width: 90%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<h2 id="conclusion">Conclusion</h2>
<p>My primitive experiment suggests that predictive human preference is feasible using a surprisingly small amount of data. There are many potential use cases for predictive human preference – model routing and interpretability are just two of them.</p>

<p>Predictive human reference is the first and the most important step in model routing (the other key step is routing strategy). With more and more models being developed, each with different capabilities and a cost structure, model routing has clear economic values.</p>

<p>I’m aware of four groups (two in stealth) that are working on model routing. One startup is Martian, which announced its <a href="https://techcrunch.com/2023/11/15/martians-tool-automatically-switches-between-llms-to-reduce-costs/">$9M seed round</a>. LMSYS is also working on model routing, which I think is a natural progression from their work in comparative evaluation.</p>

<p>While my experiment used human-annotated comparisons, LMSYS folks told me that due to the noisiness of crowd-sourced annotations and the costs of expert annotations, they’ve found that using GPT-4 to compare two responses works better. Depending on the complexity of the queries, generating 10,000 comparisons using GPT-4 would cost only $200 - 500, making this very affordable for companies that want to test it out.</p>

<p>This is the most fun side project I’ve worked on in a while, so I’d love to talk more about it. For those interested, I’ll be hosting a casual 30-minute discussion on predictive human preference on Tuesday, Mar 5, 9.30am PST. Join our <a href="https://discord.gg/Bgxhua5XVR">Discord</a> or email me if you want an invite!</p>

<h2 id="acknowledgment">Acknowledgment</h2>

<p>Thanks <a href="https://twitter.com/luke_metz">Luke Metz</a> for helping me with the experiments and coercing me into using JAX. While JAX is super cool and makes a lot of things easy, it also caused some of the weirdest bugs I’ve ever seen. I’m glad I used it though. Thanks <a href="https://www.linkedin.com/in/hanchunglee/">Han-chung Lee</a> for feedback on the plots.</p>

  </div>

  <!-- Twitter cards -->
  <meta name="twitter:site"    content="@chipro">
  <meta name="twitter:creator" content="@Chip Huyen">
  <meta name="twitter:title"   content="Predictive Human Preference: From Model Ranking to Model Routing">

  
  <meta name="twitter:description" content="One use case of predictive human preference is model routing. For example, if we know in advance that for a prompt, users will prefer Claude Instant’s response over GPT-4, and Claude Instant is cheaper/faster than GPT-4, we can route this prompt to Claude Instant. Model routing has the potential to increase response quality while reducing costs and latency.">
  

  
  <meta name="twitter:card"  content="summary_large_image">
  <meta name="twitter:image" content="https://huyenchip.com/assets/pics/predictive-preference/8-easy-hard-prompts.png">
  
  <!-- end of Twitter cards -->
  
  <!-- <div id="collective_recsys"></div> -->
  <!-- <script async data-uid="45ca838230" src="https://chiphuyen.ck.page/45ca838230/index.js"></script> -->
  <br>
  
  
    
  <div id="disqus_thread"></div>
  <script>
    var disqus_config = function () {
      this.page.url = 'https://huyenchip.com/2024/02/28/predictive-human-preference.html';
      this.page.identifier = 'https://huyenchip.com/2024/02/28/predictive-human-preference.html';
    };

    (function() {
      var d = document, s = d.createElement('script');

      s.src = 'https://chiphuyen.disqus.com/embed.js';

      s.setAttribute('data-timestamp', +new Date());
      (d.head || d.body).appendChild(s);
    })();
  </script>
  <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>

  
</article>

<!-- Add the scroll detection script here -->
<script>
  // Get all h2 and h3 and h4 elements within the .post-content
  const sections = document.querySelectorAll(".post-content h2, .post-content h3, .post-content h4");

  // Get all links in the sidebar
  const navLinks = document.querySelectorAll(".sidebar a");

  // Function to update active link
  function updateActiveLink() {
    let currentSection = "";

    // Get the distance from the top of the page to the top of the first section
    const firstSectionTop = sections[0].offsetTop;

    // Only run the active class update if you've scrolled past the first section
    if (window.pageYOffset < firstSectionTop - 100) {
      // If we're at the top of the page, make sure all links are inactive
      navLinks.forEach((link) => {
        link.classList.remove("active");
      });
      return; // Stop execution here so no links are marked active
    }

    // Loop through sections to find the current section in view
    sections.forEach((section) => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.clientHeight;

      // Check if the section is in the viewport
      if (pageYOffset >= sectionTop - sectionHeight / 3) {
        currentSection = section.getAttribute("id");
      }
    });

    // Update active class on the sidebar links
    navLinks.forEach((link) => {
      link.classList.remove("active");
      // if (link.getAttribute("href").includes(currentSection)) {
      //   link.classList.add("active");
      // }
      // Extract the href value and match exactly with the current section
      const linkHref = link.getAttribute("href").replace("#", ""); // Remove the '#' to match the section id
      if (linkHref === currentSection) {
        link.classList.add("active");
      }
    });
  }

  // Add scroll event listener to update active link while scrolling
  window.addEventListener("scroll", updateActiveLink);
</script>
      </div>
    </main>

    <footer class="site-footer">

  <div class="wrapper">

    <!-- <h2 class="footer-heading">Chip Huyen</h2> -->

    <div class="footer-col-wrapper">
      <div class="footer-col footer-col-1">
        <ul class="contact-list">
          <!--li>
            
            Chip Huyen
            
          </li-->
          
          <li>
            <a><span class="icon icon--github"><svg viewBox="0 4.801209 28.3499966 18.7475815" enable-background="new 0 4.801209 28.3499966 18.7475815">
<path fill="#828282" d="M15.699194,17.7568531c-0.4572582,0.3048401-0.9145174,0.6096783-1.5241938,0.6096783
	c-0.6096773,0-1.0669355-0.15242-1.5241938-0.6096783L0,6.7826605v16.1564522C0,23.2439518,0.3048387,23.54879,0.6096774,23.54879
	h27.1306419c0.3048401,0,0.6096764-0.3048382,0.6096764-0.6096764V6.7826605L15.699194,17.7568531z"/>
<path fill="#828282" d="M14.9370966,15.7754021L27.587904,4.801209H0.9145162l12.6508064,10.9741936
	C13.870162,16.0802422,14.4798384,16.0802422,14.9370966,15.7754021z"/>
</svg>
</span><span class="username">hi@[thiswebsite]</span></a>

          </li>
          
          
          
          <li>
            <a href="https://twitter.com/chipro"><span class="icon icon--twitter"><svg viewBox="0 0 16 16" width="16px" height="16px"><path fill="#828282" d="M15.969,3.058c-0.586,0.26-1.217,0.436-1.878,0.515c0.675-0.405,1.194-1.045,1.438-1.809c-0.632,0.375-1.332,0.647-2.076,0.793c-0.596-0.636-1.446-1.033-2.387-1.033c-1.806,0-3.27,1.464-3.27,3.27 c0,0.256,0.029,0.506,0.085,0.745C5.163,5.404,2.753,4.102,1.14,2.124C0.859,2.607,0.698,3.168,0.698,3.767 c0,1.134,0.577,2.135,1.455,2.722C1.616,6.472,1.112,6.325,0.671,6.08c0,0.014,0,0.027,0,0.041c0,1.584,1.127,2.906,2.623,3.206 C3.02,9.402,2.731,9.442,2.433,9.442c-0.211,0-0.416-0.021-0.615-0.059c0.416,1.299,1.624,2.245,3.055,2.271 c-1.119,0.877-2.529,1.4-4.061,1.4c-0.264,0-0.524-0.015-0.78-0.046c1.447,0.928,3.166,1.469,5.013,1.469 c6.015,0,9.304-4.983,9.304-9.304c0-0.142-0.003-0.283-0.009-0.423C14.976,4.29,15.531,3.714,15.969,3.058z"/></svg>
</span><span class="username">chipro</span></a>

          </li>
          

          
          <li>
            <a href="https://www.linkedin.com/in/chiphuyen"><span class="icon icon--linkedin"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg></span><span class="username">chiphuyen</span></a>

          </li>
          

          
          <li>
            <a href="https://chiphuyen.substack.com"><span class="icon icon--linkedin"><?xml version="1.0" encoding="UTF-8"?>
<svg viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg">
  <title>Substack logo</title>
  <g fill="#FF6719">
    <!-- top stripe -->
    <rect x="0" y="40" width="256" height="32" />
    <!-- middle stripe -->
    <rect x="0" y="96" width="256" height="32" />
    <!-- bookmark shape -->
    <polygon points="0,160 256,160 256,256 128,208 0,256"/>
  </g>
</svg>
</span><span class="username">chiphuyen</span></a>

          </li>
          

          
          <li>
            <a href="https://facebook.com/chipiscrazy"><span class="icon icon--facebook"><svg viewBox="0 0 155 155" width="16px" height="16px"><path id="f_1_" d="M89.584,155.139V84.378h23.742l3.562-27.585H89.584V39.184   c0-7.984,2.208-13.425,13.67-13.425l14.595-0.006V1.08C115.325,0.752,106.661,0,96.577,0C75.52,0,61.104,12.853,61.104,36.452   v20.341H37.29v27.585h23.814v70.761H89.584z" fill="#828282"/></svg>
</span><span class="username">chipiscrazy</span></a>

          </li>
          

          
          <li>
            <a href="https://instagram.com/huyenchip19"><span class="icon icon--instagram"><?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg width="256px" height="256px" viewBox="0 0 256 256" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" preserveAspectRatio="xMidYMid">
    <g>
        <path d="M127.999746,23.06353 C162.177385,23.06353 166.225393,23.1936027 179.722476,23.8094161 C192.20235,24.3789926 198.979853,26.4642218 203.490736,28.2166477 C209.464938,30.5386501 213.729395,33.3128586 218.208268,37.7917319 C222.687141,42.2706052 225.46135,46.5350617 227.782844,52.5092638 C229.535778,57.0201472 231.621007,63.7976504 232.190584,76.277016 C232.806397,89.7746075 232.93647,93.8226147 232.93647,128.000254 C232.93647,162.177893 232.806397,166.225901 232.190584,179.722984 C231.621007,192.202858 229.535778,198.980361 227.782844,203.491244 C225.46135,209.465446 222.687141,213.729903 218.208268,218.208776 C213.729395,222.687649 209.464938,225.461858 203.490736,227.783352 C198.979853,229.536286 192.20235,231.621516 179.722476,232.191092 C166.227425,232.806905 162.179418,232.936978 127.999746,232.936978 C93.8200742,232.936978 89.772067,232.806905 76.277016,232.191092 C63.7971424,231.621516 57.0196391,229.536286 52.5092638,227.783352 C46.5345536,225.461858 42.2700971,222.687649 37.7912238,218.208776 C33.3123505,213.729903 30.538142,209.465446 28.2166477,203.491244 C26.4637138,198.980361 24.3784845,192.202858 23.808908,179.723492 C23.1930946,166.225901 23.0630219,162.177893 23.0630219,128.000254 C23.0630219,93.8226147 23.1930946,89.7746075 23.808908,76.2775241 C24.3784845,63.7976504 26.4637138,57.0201472 28.2166477,52.5092638 C30.538142,46.5350617 33.3123505,42.2706052 37.7912238,37.7917319 C42.2700971,33.3128586 46.5345536,30.5386501 52.5092638,28.2166477 C57.0196391,26.4642218 63.7971424,24.3789926 76.2765079,23.8094161 C89.7740994,23.1936027 93.8221066,23.06353 127.999746,23.06353 M127.999746,0 C93.2367791,0 88.8783247,0.147348072 75.2257637,0.770274749 C61.601148,1.39218523 52.2968794,3.55566141 44.1546281,6.72008828 C35.7374966,9.99121548 28.5992446,14.3679613 21.4833489,21.483857 C14.3674532,28.5997527 9.99070739,35.7380046 6.71958019,44.1551362 C3.55515331,52.2973875 1.39167714,61.6016561 0.769766653,75.2262718 C0.146839975,88.8783247 0,93.2372872 0,128.000254 C0,162.763221 0.146839975,167.122183 0.769766653,180.774236 C1.39167714,194.398852 3.55515331,203.703121 6.71958019,211.845372 C9.99070739,220.261995 14.3674532,227.400755 21.4833489,234.516651 C28.5992446,241.632547 35.7374966,246.009293 44.1546281,249.28042 C52.2968794,252.444847 61.601148,254.608323 75.2257637,255.230233 C88.8783247,255.85316 93.2367791,256 127.999746,256 C162.762713,256 167.121675,255.85316 180.773728,255.230233 C194.398344,254.608323 203.702613,252.444847 211.844864,249.28042 C220.261995,246.009293 227.400247,241.632547 234.516143,234.516651 C241.632039,227.400755 246.008785,220.262503 249.279912,211.845372 C252.444339,203.703121 254.607815,194.398852 255.229725,180.774236 C255.852652,167.122183 256,162.763221 256,128.000254 C256,93.2372872 255.852652,88.8783247 255.229725,75.2262718 C254.607815,61.6016561 252.444339,52.2973875 249.279912,44.1551362 C246.008785,35.7380046 241.632039,28.5997527 234.516143,21.483857 C227.400247,14.3679613 220.261995,9.99121548 211.844864,6.72008828 C203.702613,3.55566141 194.398344,1.39218523 180.773728,0.770274749 C167.121675,0.147348072 162.762713,0 127.999746,0 Z M127.999746,62.2703115 C91.698262,62.2703115 62.2698034,91.69877 62.2698034,128.000254 C62.2698034,164.301738 91.698262,193.730197 127.999746,193.730197 C164.30123,193.730197 193.729689,164.301738 193.729689,128.000254 C193.729689,91.69877 164.30123,62.2703115 127.999746,62.2703115 Z M127.999746,170.667175 C104.435741,170.667175 85.3328252,151.564259 85.3328252,128.000254 C85.3328252,104.436249 104.435741,85.3333333 127.999746,85.3333333 C151.563751,85.3333333 170.666667,104.436249 170.666667,128.000254 C170.666667,151.564259 151.563751,170.667175 127.999746,170.667175 Z M211.686338,59.6734287 C211.686338,68.1566129 204.809755,75.0337031 196.326571,75.0337031 C187.843387,75.0337031 180.966297,68.1566129 180.966297,59.6734287 C180.966297,51.1902445 187.843387,44.3136624 196.326571,44.3136624 C204.809755,44.3136624 211.686338,51.1902445 211.686338,59.6734287 Z" fill="#0A0A08"></path>
    </g>
</svg>
</span><span class="username">huyenchip19</span></a>

          </li>
          

          
          <li>
            <a href="https://github.com/chiphuyen"><span class="icon icon--github"><svg viewBox="0 0 16 16" width="16px" height="16px"><path fill="#828282" d="M7.999,0.431c-4.285,0-7.76,3.474-7.76,7.761 c0,3.428,2.223,6.337,5.307,7.363c0.388,0.071,0.53-0.168,0.53-0.374c0-0.184-0.007-0.672-0.01-1.32 c-2.159,0.469-2.614-1.04-2.614-1.04c-0.353-0.896-0.862-1.135-0.862-1.135c-0.705-0.481,0.053-0.472,0.053-0.472 c0.7