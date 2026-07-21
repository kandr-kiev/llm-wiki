---

source_url: https://huyenchip.com//2025/01/16/ai-engineering-pitfalls.html
ingested: 2026-07-10
sha256: f11cbd74cbe4ec9a5e8acea1214625978ab6496766f59035a9e23e65963ae75a
blog_source: Chip Huyen
---

<!DOCTYPE html>
<html lang="en">

  <head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>Common pitfalls when building generative AI applications</title>
  <meta name="description" content="As we’re still in the early days of building applications with foundation models, it’s normal to make mistakes. This is a quick note with examples of some of...">
  
  <link rel="stylesheet" href="/assets/main.css">
  <link rel="canonical" href="https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html">
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
<title>Common pitfalls when building generative AI applications | Chip Huyen</title>
<meta name="generator" content="Jekyll v3.10.0" />
<meta property="og:title" content="Common pitfalls when building generative AI applications" />
<meta name="author" content="Chip Huyen" />
<meta property="og:locale" content="en_US" />
<meta name="description" content="As we’re still in the early days of building applications with foundation models, it’s normal to make mistakes. This is a quick note with examples of some of the most common pitfalls that I’ve seen, both from public case studies and from my personal experience." />
<meta property="og:description" content="As we’re still in the early days of building applications with foundation models, it’s normal to make mistakes. This is a quick note with examples of some of the most common pitfalls that I’ve seen, both from public case studies and from my personal experience." />
<link rel="canonical" href="https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html" />
<meta property="og:url" content="https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html" />
<meta property="og:site_name" content="Chip Huyen" />
<meta property="og:image" content="https://huyenchip.com/assets/pics/aie-pitfalls/aie-pitfalls.png" />
<meta property="og:type" content="article" />
<meta property="article:published_time" content="2025-01-16T00:00:00+00:00" />
<meta name="twitter:card" content="summary_large_image" />
<meta property="twitter:image" content="https://huyenchip.com/assets/pics/aie-pitfalls/aie-pitfalls.png" />
<meta property="twitter:title" content="Common pitfalls when building generative AI applications" />
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Chip Huyen"},"dateModified":"2025-01-16T00:00:00+00:00","datePublished":"2025-01-16T00:00:00+00:00","description":"As we’re still in the early days of building applications with foundation models, it’s normal to make mistakes. This is a quick note with examples of some of the most common pitfalls that I’ve seen, both from public case studies and from my personal experience.","headline":"Common pitfalls when building generative AI applications","image":"https://huyenchip.com/assets/pics/aie-pitfalls/aie-pitfalls.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html"},"url":"https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html"}</script>
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
      <a href="#1_use_generative_ai_when_you_don_t_need_generative_ai">1. Use generative AI when you don't need generative AI</a><br>
<a href="#2_confuse_bad_product_with_bad_ai">2. Confuse ‘bad product' with ‘bad AI'</a><br>
<a href="#3_start_too_complex">3. Start too complex</a><br>
<a href="#4_over_index_on_early_success">4. Over-index on early success</a><br>
<a href="#5_forgo_human_evaluation">5. Forgo human evaluation</a><br>
<a href="#6_crowdsource_use_cases">6. Crowdsource use cases</a><br>
<a href="#summary">Summary</a><br>

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
    <h1 class="post-title" itemprop="name headline">Common pitfalls when building generative AI applications</h1>
    <p class="post-meta">
      <time datetime="2025-01-16T00:00:00+00:00" itemprop="datePublished">
        
        Jan 16, 2025
      </time>
      
        • <span itemprop="author" itemscope itemtype="http://schema.org/Person"><span itemprop="name">Chip Huyen</span></span>
      </p>
  </header>

  <div class="post-content" itemprop="articleBody">
    <p>As we’re still in the early days of building applications with foundation models, it’s normal to make mistakes. This is a quick note with examples of some of the most common pitfalls that I’ve seen, both from public case studies and from my personal experience.</p>

<p>Because these pitfalls are common, if you’ve worked on any AI product, you’ve probably seen them before.</p>

<h2 id="1_use_generative_ai_when_you_don_t_need_generative_ai">1. Use generative AI when you don't need generative AI</h2>

<p>Every time there’s a new technology, I can hear the collective sigh of senior engineers everywhere: “Not everything is a nail.” Generative AI isn’t an exception — its seemingly limitless capabilities only exacerbate the tendency to use generative AI for everything.</p>

<p>A team pitched me the idea of using generative AI to optimize energy consumption. They fed a household’s list of energy-intensive activities and hourly electricity prices into an LLM, then asked it to create a schedule to minimize energy costs. Their experiments showed that this could help reduce a household’s electricity bill by 30%. Free money. Why wouldn’t anyone want to use their app?</p>

<p>I asked: “How does it compare to simply scheduling the most energy-intensive activities when electricity is cheapest? Say, doing your laundry and charging your car after 10pm?”</p>

<p>They said they would try it later and let me know. They never followed up, but they abandoned this app soon after. I suspect that this greedy scheduling can be quite effective. Even if it’s not, there are other much cheaper and more reliable optimization solutions than generative AI, like linear programming.</p>

<p>I’ve seen this scenario over and over again. A big company wants to use generative AI to detect anomalies in network traffic. Another wants to predict upcoming customer call volume. A hospital wants to detect whether a patient is malnourished (really not recommended).</p>

<p>It can often be beneficial to explore a new approach to get a sense of what’s possible, as long as you’re aware that your goal isn’t to solve a problem but to test a solution. “We solve the problem” and “We use generative AI” are two very different headlines, and unfortunately, so many people would rather have the latter.</p>

<h2 id="2_confuse_bad_product_with_bad_ai">2. Confuse 'bad product' with 'bad AI'</h2>

<p>At the other end of the spectrum, many teams dismiss gen AI as a valid solution for their problems because they tried it out and their users hated it. However, other teams successfully used gen AI for similar use cases. I could only look into two of these teams. In both cases, the issue wasn’t with AI, but with product.</p>

<p>Many people have told me that the technical aspects of their AI applications are straightforward. The hard part is user experience (UX). What should the product interface look like? How to seamlessly integrate the product into the user workflow? How to incorporate human-in-the-loop?</p>

<p>UX has always been challenging, but it’s even more so with generative AI. While we know that generative AI is changing how we read, write, learn, teach, work, entertain, etc., we don’t quite know how yet. What will the future of reading/learning/working be like?</p>

<p>Here are some simple examples to show how what users want can be counter-intuitive and need rigorous user study.</p>

<ol>
  <li>
    <p>My friend works on an application that summarizes meeting transcripts. Initially, her team focused on getting the right summary length. Would users prefer 3-sentence summaries or 5-sentence summaries? <br />
 <br />
However, it turned out that their users didn’t care about the actual summary. They only wanted action items specific to them from each meeting.</p>
  </li>
  <li>
    <p>When <a href="https://www.linkedin.com/blog/engineering/generative-ai/musings-on-building-a-generative-ai-product?_l=en_US">LinkedIn</a> developed a chatbot for skill fit assessment, they discovered that users didn’t want correct responses. Users wanted helpful responses. <br />
 <br />
For example, if a user asks a bot whether they’re a fit for a job and the bot responds with: “You’re a terrible fit,” this response might be correct but not very helpful to the user. Users want tips on what the gaps are and what they can do to close the gaps.</p>
  </li>
  <li>
    <p>Intuit built a chatbot to help users answer tax questions. Initially, they got lukewarm feedback — users didn’t find the bot useful. After investigation, they found out that users actually hated typing. Facing a blank chatbot, users didn’t know what the bot could do and what to type. <br />
 <br />
So, for each interaction, Intuit added a few suggested questions for users to click on. This reduced the friction for users to use the bot and gradually built users’ trust. The feedback from users then became much more positive. <br />
<em>(Shared by <a href="https://www.linkedin.com/in/nhungho/">Nhung Ho</a>, VP of AI at Intuit, during our panel at Grace Hopper.)</em></p>
  </li>
</ol>

<p>Because everyone uses the same models nowadays, the AI components of AI products are similar, and the differentiation is product.</p>

<h2 id="3_start_too_complex">3. Start too complex</h2>

<p>Examples of this pitfall:</p>

<ol>
  <li>Use an agentic framework when direct API calls work.</li>
  <li>Agonize over what vector database to use when a simple term-based retrieval solution (that doesn’t require a vectordb) works.</li>
  <li>Insist on finetuning when prompting works.</li>
  <li>Use semantic caching.</li>
</ol>

<p>Given so many shiny new technologies, it’s tempting to jump straight into using them. However, incorporating external tools too early can cause 2 problems:</p>

<ol>
  <li>Abstract away critical details, making it hard to understand and debug your system.</li>
  <li>Introduce unnecessary bugs.</li>
</ol>

<p>Tool developers can make mistakes. For example, I often find typos in default prompts when reviewing a framework’s codebase. If the framework you use updates its prompt without telling you, your application’s behaviors might change and you might not know why.</p>

<p>Eventually, abstractions are good. But abstractions need to incorporate best practices and be tested overtime. As we’re still in the early days of AI engineering, best practices are still evolving, we should be more vigilant when adopting any abstraction.</p>

<h2 id="4_over_index_on_early_success">4. Over-index on early success</h2>

<ol>
  <li>
    <p>It took <a href="https://www.linkedin.com/blog/engineering/generative-ai/musings-on-building-a-generative-ai-product">LinkedIn</a> <em>1 month to achieve 80% of the experience they wanted, and an additional 4 months to surpass 95%</em>. The initial success made them grossly underestimate how challenging it is to improve the product, especially around hallucinations. They found it discouraging how difficult it was to achieve each subsequent 1% gain.</p>
  </li>
  <li>A startup that develops AI sales assistants for ecommerce told me that <em>getting from 0 to 80% took as long as from 80% to 90%</em>. The challenges they faced:
    <ul>
      <li>Accuracy/latency tradeoff: more planning/self-correction = more nodes = higher latency</li>
      <li>Tool calling: hard for agents to differentiate similar tools</li>
      <li>Hard for tonal requests (e.g. <code class="language-plaintext highlighter-rouge">"talk like a luxury brand concierge"</code>) in the system prompt to be perfectly obeyed</li>
      <li>Hard for the agent to completely understand customers’ intent</li>
      <li>Hard to create a specific set of unit tests because the combination of queries is basically infinite</li>
    </ul>

    <p><em>Thanks <a href="https://www.linkedin.com/in/jasontjahjono/">Jason Tjahjono</a> for sharing this.</em></p>
  </li>
  <li>In the paper UltraChat, <a href="https://arxiv.org/abs/2305.14233">Ding et al. (2023)</a> shared that “<em>the journey from 0 to 60 is easy, whereas progressing from 60 to 100 becomes exceedingly challenging</em>.”</li>
</ol>

<p>This is perhaps one of the first painful lessons anyone who has built an AI product quickly learns. It’s easy to build a demo, but hard to build a product. Other than the issues of hallucinations, latency, latency/accuracy tradeoff, tool use, prompting, testing, … as mentioned, teams also run into issues, such as:</p>

<ol>
  <li><strong>Reliability</strong> from the API providers. A team told me that 10% of their API calls timed out. Or product’s behaviors change because the underlying model changes.</li>
  <li><strong>Compliance</strong>, e.g. around AI output copyrights, data access/sharing, user privacy, security risks from retrieval/caching systems, and ambiguity around training data lineage.</li>
  <li><strong>Safety</strong>, e.g. bad actors abusing your product, your product generates insensitive or offensive responses.</li>
</ol>

<p>When planning a product’s milestones and resources, make sure to take into account these potential roadblocks. A friend calls this “being cautiously optimistic”. However, remember that many cool demos don’t lead to wonderful products.</p>

<h2 id="5_forgo_human_evaluation">5. Forgo human evaluation</h2>

<p>To automatically evaluate AI applications, many teams opt for the AI-as-a-judge (also called LLM-as-a-judge) approach — using AI models to evaluate AI outputs. A common pitfall is forgoing human evaluation to rely entirely on AI judges.</p>

<p>While AI judges can be very useful, they aren’t deterministic. The quality of a judge depends on the underlying judge’s model, the judge’s prompt, and the use case. If the AI judge isn’t developed properly, it can give misleading evaluations about your application’s performance. AI judges must be evaluated and iterated over time, just like all other AI applications.</p>

<center>
    <figure>
    <img alt="Agent pattern" src="/assets/pics/aie-pitfalls/ai-judge.png" style="float: center; max-width: 100%; margin: 0 0 0em 0em" />
    </figure>
</center>

<p>The teams with the best products I’ve seen all have human evaluation to supplement their automated evaluation. Every day, they have human experts evaluate a subset of their application’s outputs, which can be anywhere from 30 - 1000 examples.</p>

<p>Daily manual evaluation serves 3 purposes:</p>

<ol>
  <li>Correlate human judgments with AI judgments. If the score by human evaluators is decreasing but the score by AI judges is increasing, you might want to investigate your AI judges.</li>
  <li>Gain a better understanding of how users use your application, which can give you ideas to improve your application.</li>
  <li>Detect patterns and changes in users’ behaviors, using your knowledge of current events, that automated data exploration might miss.</li>
</ol>

<p>The reliability of human evaluation also depends on well-crafted annotation guidelines. These annotation guidelines can help improve the model’s instructions (if a human has a hard time following the instructions, the model will, too). It can also be reused to create finetuning data later if you choose to finetune.</p>

<p>In every project I’ve worked on, <em>staring at data for just 15 minutes usually gives me some insight that could save me hours of headaches</em>. <a href="https://x.com/gdb/status/1622683988736479232">Greg Brockman</a> tweeted: “<em>Manual inspection of data has probably the highest value-to-prestige ratio of any activity in machine learning.</em>”</p>

<h2 id="6_crowdsource_use_cases">6. Crowdsource use cases</h2>

<p>This is a mistake I saw in the early days when enterprises were in a frenzy to adopt generative AI. Unable to come up with a strategy for what use cases to focus on, many tech executives crowdsourced ideas from the whole company. “We hire smart people. Let them tell us what to do.” They then try to implement these ideas one by one.</p>

<p>And that’s how we ended up with a million text-to-SQL models, a million Slack bots, and a billion code plugins.</p>

<p>While it’s indeed a good idea to listen to the smart people that you hire, individuals might be biased toward the problems that immediately affect their day-to-day work instead of problems that might bring the highest returns on investment. Without an overall strategy that considers the big picture, it’s easy to get sidetracked into a series of small, low-impact applications and come to the wrong conclusion that gen AI has no ROI.</p>

<h2 id="summary">Summary</h2>

<p>In short, here are the common AI engineering pitfalls:</p>

<ol>
  <li>
    <p><strong>Use generative AI when you don’t need generative AI</strong><br />
 Gen AI isn’t a one-size-fits-all solution to all problems. Many problems don’t even need AI.</p>
  </li>
  <li>
    <p><strong>Confuse ‘bad product’ with ‘bad AI’</strong><br />
 For many AI product, AI is the easy part, product is the hard part.</p>
  </li>
  <li>
    <p><strong>Start too complex</strong><br />
 While fancy new frameworks and finetuning can be useful for many projects, they shouldn’t be your first course of action.</p>
  </li>
  <li>
    <p><strong>Over-index on early success</strong><br />
 Initial success can be misleading. Going from demo-ready to production-ready can take much longer than getting to the first demo.</p>
  </li>
  <li>
    <p><strong>Forgo human evaluation</strong><br />
 AI judges should be validated and correlated with systematic human evaluation.</p>
  </li>
  <li>
    <p><strong>Crowdsource use cases</strong><br />
 Have a big-picture strategy to maximize return on investment.</p>
  </li>
</ol>

  </div>

  <!-- Twitter cards -->
  <meta name="twitter:site"    content="@chipro">
  <meta name="twitter:creator" content="@Chip Huyen">
  <meta name="twitter:title"   content="Common pitfalls when building generative AI applications">

  
  <meta name="twitter:description" content="Foundation models enable many new application interfaces, but one that has especially grown in popularity is the conversational interface, such as with chatbots and assistants. The conversational interface makes it easier for users to give feedback but harder for developers to extract signals. This post will discuss what conversational AI feedback looks like and how to design a system to collect the right feedback without hurting user experience.">
  

  
  <meta name="twitter:card"  content="summary_large_image">
  <meta name="twitter:image" content="https://huyenchip.com/assets/pics/aie-pitfalls/aie-pitfalls.png">
  
  <!-- end of Twitter cards -->
  
  <!-- <div id="collective_recsys"></div> -->
  <!-- <script async data-uid="45ca838230" src="https://chiphuyen.ck.page/45ca838230/index.js"></script> -->
  <br>
  
  
    
  <div id="disqus_thread"></div>
  <script>
    var disqus_config = function () {
      this.page.url = 'https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html';
      this.page.identifier = 'https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html';
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
            <a href="https://github.com/chiphuyen"><span class="icon icon--github"><svg viewBox="0 0 16 16" width="16px" height="16px"><path fill="#828282" d="M7.999,0.431c-4.285,0-7.76,3.474-7.76,7.761 c0,3.428,2.223,6.337,5.307,7.363c0.388,0.071,0.53-0.168,0.53-0.374c0-0.184-0.007-0.672-0.01-1.32 c-2.159,0.469-2.614-1.04-2.614-1.04c-0.353-0.896-0.862-1.135-0.862-1.135c-0.705-0.481,0.053-0.472,0.053-0.472 c0.779,0.055,1.189,0.8,1.189,0.8c0.692,1.186,1.816,0.843,2.258,0.645c0.071-0.502,0.271-0.843,0.493-1.037 C4.86,11.425,3.049,10.76,3.049,7.786c0-0.847,0.302-1.54,0.799-2.082C3.768,5.507,3.501,4.718,3.924,3.65 c0,0,0.652-0.209,2.134,0.796C6.677,4.273,7.34,4.187,8,4.184c0.659,0.003,1.323,0.089,1.943,0.261 c1.482-1.004,2.132-0.796,2.132-0.796c0.423,1.068,0.157,1.857,0.077,2.054c0.497,0.542,0.798,1.235,0.798,2.082 c0,2.981-1.814,3.637-3.543,3.829c0.279,0.24,0.527,0.713,0.527,1.437c0,1.037-0.01,1.874-0.01,2.129 c0,0.208,0.14,0.449,0.534,0.373c3.081-1.028,5.302-3.935,5.302-7.362C15.76,3.906,12.285,0.431,7.999,0.431z"/></svg>
</span><span class="username">chiphuyen</span></a>

          </li>
          
        </ul>
      </div>

      <div class="footer-col footer-col-2">
        <p>I work to bring AI into production. I write about AI system design.
</p>
        <!-- <p><b>I&#39;m thinking about starting a newsletter. Sign up to be the first to know!
</b></p> -->

        <p>I don't have a <a href='https://chiphuyen.substack.com/'>Substack</a> yet, but if more people nudge me, I might actually start it.</p>
        <div class="substack-box">
        <iframe src="https://chiphuyen.substack.com/embed" width="480" height="150" style="border:0px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>
        </div>
        
      </div>
    </div>

  </div>

</footer>


  </body>

</html>
