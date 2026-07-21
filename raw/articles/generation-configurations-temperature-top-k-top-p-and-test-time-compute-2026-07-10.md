---

source_url: https://huyenchip.com//2024/01/16/sampling.html
ingested: 2026-07-10
sha256: 843b40467ec2a411706245d4f10d870a7c499c9efd22dac7d366db277efbcd88
blog_source: Chip Huyen
---

<!DOCTYPE html>
<html lang="en">

  <head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>Generation configurations: temperature, top-k, top-p, and test time compute</title>
  <meta name="description" content="ML models are probabilistic. Imagine that you want to know what’s the best cuisine in the world. If you ask someone this question twice, a minute apart, thei...">
  
  <link rel="stylesheet" href="/assets/main.css">
  <link rel="canonical" href="https://huyenchip.com/2024/01/16/sampling.html">
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
<title>Generation configurations: temperature, top-k, top-p, and test time compute | Chip Huyen</title>
<meta name="generator" content="Jekyll v3.10.0" />
<meta property="og:title" content="Generation configurations: temperature, top-k, top-p, and test time compute" />
<meta name="author" content="Chip Huyen" />
<meta property="og:locale" content="en_US" />
<meta name="description" content="ML models are probabilistic. Imagine that you want to know what’s the best cuisine in the world. If you ask someone this question twice, a minute apart, their answers both times should be the same. If you ask a model the same question twice, its answer can change. If the model thinks that Vietnamese cuisine has a 70% chance of being the best cuisine and Italian cuisine has a 30% chance, it’ll answer “Vietnamese” 70% of the time, and “Italian” 30%." />
<meta property="og:description" content="ML models are probabilistic. Imagine that you want to know what’s the best cuisine in the world. If you ask someone this question twice, a minute apart, their answers both times should be the same. If you ask a model the same question twice, its answer can change. If the model thinks that Vietnamese cuisine has a 70% chance of being the best cuisine and Italian cuisine has a 30% chance, it’ll answer “Vietnamese” 70% of the time, and “Italian” 30%." />
<link rel="canonical" href="https://huyenchip.com/2024/01/16/sampling.html" />
<meta property="og:url" content="https://huyenchip.com/2024/01/16/sampling.html" />
<meta property="og:site_name" content="Chip Huyen" />
<meta property="og:image" content="https://huyenchip.com/assets/pics/sampling/4-logprobs.png" />
<meta property="og:type" content="article" />
<meta property="article:published_time" content="2024-01-16T00:00:00+00:00" />
<meta name="twitter:card" content="summary_large_image" />
<meta property="twitter:image" content="https://huyenchip.com/assets/pics/sampling/4-logprobs.png" />
<meta property="twitter:title" content="Generation configurations: temperature, top-k, top-p, and test time compute" />
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Chip Huyen"},"dateModified":"2024-01-16T00:00:00+00:00","datePublished":"2024-01-16T00:00:00+00:00","description":"ML models are probabilistic. Imagine that you want to know what’s the best cuisine in the world. If you ask someone this question twice, a minute apart, their answers both times should be the same. If you ask a model the same question twice, its answer can change. If the model thinks that Vietnamese cuisine has a 70% chance of being the best cuisine and Italian cuisine has a 30% chance, it’ll answer “Vietnamese” 70% of the time, and “Italian” 30%.","headline":"Generation configurations: temperature, top-k, top-p, and test time compute","image":"https://huyenchip.com/assets/pics/sampling/4-logprobs.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://huyenchip.com/2024/01/16/sampling.html"},"url":"https://huyenchip.com/2024/01/16/sampling.html"}</script>
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
      <a href="#sampling">Sampling</a>
<ul class="sidebar-list">
    <li><a href="#temperature">Temperature</a></li>
    <li><a href="#top_k">Top-k</a></li>
    <li><a href="#top_p">Top-p</a></li>
    <li><a href="#stopping_condition">Stopping condition</a></li>
</ul>

<a href="#test_time_compute">Test Time Compute</a><br>

<a href="#structured_outputs">Structured Outputs</a>
<ul class="sidebar-list">
    <li><a href="#how_to_generate_structured_outputs">How to generate structured outputs</a></li>
    <li><a href="#constraint_sampling">Constraint sampling</a></li>
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
    <h1 class="post-title" itemprop="name headline">Generation configurations: temperature, top-k, top-p, and test time compute</h1>
    <p class="post-meta">
      <time datetime="2024-01-16T00:00:00+00:00" itemprop="datePublished">
        
        Jan 16, 2024
      </time>
      
        • <span itemprop="author" itemscope itemtype="http://schema.org/Person"><span itemprop="name">Chip Huyen</span></span>
      </p>
  </header>

  <div class="post-content" itemprop="articleBody">
    <p>ML models are probabilistic. Imagine that you want to know what’s the best cuisine in the world. If you ask someone this question twice, a minute apart, their answers both times should be the same. If you ask a model the same question twice, its answer can change. If the model thinks that Vietnamese cuisine has a 70% chance of being the best cuisine and Italian cuisine has a 30% chance, it’ll answer “Vietnamese” 70% of the time, and “Italian” 30%.</p>

<p>This probabilistic nature makes AI great for creative tasks. What is creativity but the ability to explore beyond the common possibilities, to think outside the box?</p>

<p>However, this probabilistic nature also causes inconsistency and hallucinations. It’s fatal for tasks that depend on factuality. Recently, I went over 3 months’ worth of customer support requests of an AI startup I advise and found that ⅕ of the questions are because users don’t understand or don’t know how to work with this probabilistic nature.</p>

<p>To understand why AI’s responses are probabilistic, we need to understand how models generate responses, a process known as sampling (or decoding). This post consists of 3 parts.</p>

<ol>
  <li><strong>Sampling</strong>: sampling strategies and sampling variables including temperature, top-k, and top-p.</li>
  <li><strong>Test time compute</strong>: increasing the compute allocated to inference, e.g. sampling multiple outputs, to help improve a model’s performance.</li>
  <li><strong>Structured outputs</strong>: how to get models to generate outputs in a certain format.</li>
</ol>

<h2 id="sampling">Sampling</h2>

<p>Given an input, a neural network produces an output by first computing the probabilities of all possible values. For a classifier, possible values are the available classes. For example, if a model is trained to classify whether an email is spam, there are only two possible values: spam and not spam. The model computes the probability of each of these two values, say being spam is 90% and not spam is 10%.</p>

<p>To generate the next token, a language model first computes the probability distribution over all tokens in the vocabulary.</p>

<center>
    <figure>
    <img alt="Sampling the next token based on token probabilities" src="/assets/pics/sampling/1-sampling-tokens.png" style="float: center; max-width: 83%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>For the spam email classification task, it’s okay to output the value with the highest probability. If the email has a 90% chance of being spam, you classify the email as spam. However, for a language model, always picking the most likely token, <em>greedy sampling</em>, creates boring outputs. Imagine a model that, for whichever question you ask, always responds with the most common words.</p>

<p>Instead of always picking the next most likely token, we can sample the next token according to the probability distribution over all possible values. Given the context of <code class="language-plaintext highlighter-rouge">My favorite color is ...</code>, if <code class="language-plaintext highlighter-rouge">red</code> has a 30% chance of being the next token and <code class="language-plaintext highlighter-rouge">green</code> has a 50% chance, <code class="language-plaintext highlighter-rouge">red</code> will be picked 30% of the time, and “green” 50% of the time.</p>

<h3 id="temperature">Temperature</h3>

<p>One problem with sampling the next token according to the probability distribution is that the model can be less creative. In the previous example, common words for colors like <code class="language-plaintext highlighter-rouge">red</code>, <code class="language-plaintext highlighter-rouge">green</code>, <code class="language-plaintext highlighter-rouge">purple</code>, etc. have the highest probabilities. The language model’s answer ends up sounding like that of a five-year-old: <code class="language-plaintext highlighter-rouge">My favorite color is green.</code> Because <code class="language-plaintext highlighter-rouge">the</code> has a low probability, the model has a low chance of generating a creative sentence such as <code class="language-plaintext highlighter-rouge">My favorite color is the color of a still lake on a spring morning.</code></p>

<p>Temperature is a technique used to redistribute the probabilities of the possible values. Intuitively, it reduces the probabilities of common tokens, and as a result, increases the probabilities of rarer tokens. This enables models to create more creative responses.</p>

<p>To understand how temperature works, let’s take a step back to see how a model computes the probabilities. Given an input, a neural network processes this input and outputs a logit vector. Each logit corresponds to one possible. In the case of a language model, each logit corresponds to one token in the model’s vocabulary. The logit vector size is the size of the vocabulary.</p>

<center>
    <figure>
    <img alt="Sampling the next token based on token probabilities" src="/assets/pics/sampling/2-logits.png" style="float: center; max-width: 57%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>While larger logits correspond to higher probabilities, the logits don’t represent the probabilities. Logits don’t sum up to one. Logits can even be negative, while probabilities have to be non-negative. To convert logits to probabilities, a softmax layer is often used. Let’s say the model has a vocabulary of N and the logit vector is \([x_1, x_2, ..., x_N]\). The probability for the \(i^{th}\) token, \(p_i\), is computed as follows:</p>

\[p_i = \text{softmax}(x_i) = \frac{e^{x_i}}{\sum_j e^{x_j}}\]

<p>Temperature is a constant used to adjust the logits before the softmax transformation. Logits are divided by temperature. For a given temperature of \(T\), the adjusted logit for the \(i^{th}\) token is \(\frac{x_i}{T}\). Softmax is then applied on this adjusted logit instead of on \(x_i\).</p>

<p>Let’s walk through a simple example to understand the effect of temperature on probabilities. Imagine that we have a model that has only two possible outputs: A and B. The logits computed from the last layer are <code class="language-plaintext highlighter-rouge">[1, 3]</code>. The logit for A is 1 and B is 3.</p>

<ul>
  <li>Without using temperature, equivalent to temperature = 1, the softmax probabilities are <code class="language-plaintext highlighter-rouge">[0.12, 0.88]</code>. The model picks B 88% of the time.</li>
  <li>With temperature = 0.5, the probabilities are <code class="language-plaintext highlighter-rouge">[0.02, 0.98]</code>. The model picks B 98% of the time.</li>
  <li>With temperature = 2, the probabilities are <code class="language-plaintext highlighter-rouge">[0.27, 0.73]</code>. The model picks B 73% of the time.</li>
</ul>

<p>The higher the temperature, the less likely the model is going to pick the most obvious value (the value with the highest logit), making the model’s outputs more creative but potentially less coherent. The lower the temperature, the more likely the model is going to pick the most obvious value, making the model’s out more consistent but potentially more boring.</p>

<p>The graph below shows the softmax probability for token B at different temperatures. As the temperature gets closer to 0, the probability that the model picks token B becomes closer to 1. In our example, for temperature below 0.1, the model almost always outputs B. Model providers typically limit temperature to be between 0 and 2. If you own your model, you can use any non-negative temperature. A temperature of 0.7 is often recommended for creative use cases, as it balances creativity and determinism, but you should experiment and find the temperature that works best for you.</p>

<center>
    <figure>
    <img alt="Sampling the next token based on token probabilities using temperature" src="/assets/pics/sampling/3-temperature.png" style="float: center; max-width: 100%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>It’s common practice to set the temperature to 0 for the model’s outputs to be more consistent. Technically, temperature can never be 0 – logits can’t be divided by 0. In practice, when we set the temperature to 0, the model just picks the token with the value with the largest logit, e.g. performing an <code class="language-plaintext highlighter-rouge">argmax</code>, without doing the logit adjustment and softmax calculation.</p>

<p>A common debugging technique when working with an AI model is looking at the probabilities this model computes for given inputs. For example, if the probabilities look random, the model hasn’t learned much. OpenAI returns probabilities generated by their models as <em><a href="https://cookbook.openai.com/examples/using_logprobs">logprobs</a></em>. Logprobs, short for log probabilities, are probabilities in the log scale. Log scale is preferred when working with a neural network’s probabilities because it helps reduce the underflow problem. A language model can work with a vocabulary size of 100,000, which means the probabilities for many of the tokens can be too small to be represented by a machine. The small numbers might be rounded down to 0. Log scale helps reduce this problem.</p>

<center>
    <figure>
    <img alt="Sampling the next token based on token probabilities using logprobs" src="/assets/pics/sampling/4-logprobs.png" style="float: center; max-width: 100%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<h3 id="top_k">Top-k</h3>

<p>Top-k is a sampling strategy to reduce the computation workload without sacrificing too much of the model’s response diversity. Recall that to compute the probability distribution over all possible values, a softmax layer is used. Softmax requires two passes over all possible values: one to perform the exponential sum \(\sum_j e^{x_j}\) and one to perform \(\frac{e^{x_i}}{\sum_j e^{x_j}}\) for each value. For a language model with a large vocabulary, this process is computationally expensive.</p>

<p>To avoid this problem, after the model has computed the logits, we pick the top k logits and perform softmax over these top k logits only. Depending on how diverse you want your application to be, k can be anywhere from 50 to 500, much smaller than a model’s vocabulary size. The model then samples from these top values. A smaller k value makes the text more predictable but less interesting, as the model is limited to a smaller set of likely words.</p>

<h3 id="top_p">Top-p</h3>

<p>In top-k sampling, the number of values considered is fixed to k. However, this number should change depending on the situation. For example, given the prompt <code class="language-plaintext highlighter-rouge">Do you like music? Answer with only yes or no.</code>, the number of values considered should be two: <code class="language-plaintext highlighter-rouge">yes</code> and <code class="language-plaintext highlighter-rouge">no</code>. Given the prompt <code class="language-plaintext highlighter-rouge">What's the meaning of life?</code>, the number of values considered should be much larger.</p>

<p>Top-p, also known as nucleus sampling, allows for a more dynamic selection of values to be sampled from. In top-p sampling, the model sums the probabilities of the most likely next values in descending order and stops when the sum reaches p. Only the values within this cumulative probability are considered. Common values for top-p (nucleus) sampling in language models typically range from 0.9 to 0.95. A top-p value of 0.9, for example, means that the model will consider the smallest set of values whose cumulative probability exceeds 90%.</p>

<p>Let’s say the probabilities of all tokens are as shown in the image below. If top_p = 90%, only <code class="language-plaintext highlighter-rouge">yes</code> and <code class="language-plaintext highlighter-rouge">maybe</code> will be considered, as their cumulative probability is greater than 90%. If top_p = 99%, then <code class="language-plaintext highlighter-rouge">yes</code>, <code class="language-plaintext highlighter-rouge">maybe</code>, and <code class="language-plaintext highlighter-rouge">no</code> are considered.</p>

<center>
    <figure>
    <img alt="Sampling the next token based on token probabilities with top-p" src="/assets/pics/sampling/5-top-p.png" style="float: center; max-width: 50%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>Unlike top-k, top-p doesn’t necessarily reduce the softmax computation load. Its benefit is that because it focuses on only the set of most relevant values for each context, it allows outputs to be more contextually appropriate. In theory, there doesn’t seem to be a lot of benefits to top-p sampling. However, in practice, top-p has proven to work well, causing its popularity to rise.</p>

<h3 id="stopping_condition">Stopping condition</h3>

<p>An autoregressive language model generates sequences of tokens by generating one token after another. A long output sequence takes more time, costs more compute (money), and can sometimes be annoying to users. We might want to set a condition for the model to stop the sequence.</p>

<p>One easy method is to ask models to stop generating after a fixed number of tokens. The downside is that the output is likely to be cut off mid-sentence. Another method is to use stop tokens. For example, you can ask models to stop generating when it encounters “&lt;EOS&gt;”. Stopping conditions are helpful to keep the latency and cost down.</p>

<h2 id="test_time_compute">Test Time Compute</h2>

<p>One simple way to improve a model’s performance is to generate multiple outputs and select the best one. This approach is called <em>test time compute</em> (or <em>test time sampling</em>).</p>

<p>You can either show users multiple outputs and let them choose the one that works best for them or devise a method to select the best one. If you want your model’s responses to be consistent, you want to keep all sampling variables fixed. However, if you want to generate multiple outputs and pick the best one, you don’t want to vary your sampling variables.</p>

<p>One selection method is to pick the output with the highest probability. A language model’s output is a sequence of tokens, each token has a probability computed by the model. The probability of an output is the product of the probabilities of all tokens in the output.</p>

<p>Consider the sequence of tokens [<code class="language-plaintext highlighter-rouge">I</code>, <code class="language-plaintext highlighter-rouge">love</code>, <code class="language-plaintext highlighter-rouge">food</code>] and:</p>

<ul>
  <li>the probability for <code class="language-plaintext highlighter-rouge">I</code> is 0.2</li>
  <li>the probability for <code class="language-plaintext highlighter-rouge">love</code> given <code class="language-plaintext highlighter-rouge">I</code> is 0.1</li>
  <li>the probability for <code class="language-plaintext highlighter-rouge">food</code> given <code class="language-plaintext highlighter-rouge">I</code> and <code class="language-plaintext highlighter-rouge">love</code> is 0.3</li>
</ul>

<p>The sequence’s probability is then: 0.2 * 0.1 * 0.3 = 0.006.</p>

<p>Mathematically, this can be denoted as follows:</p>

\[p(\text{I love food}) = p(\text{I}) \times p(\text{love}|\text{I}) \times p(\text{food}|\text{I, love})\]

<p>Remember that it’s easier to work with probabilities on a log scale. The logarithm of a product is equal to a sum of logarithms, so the logprob of a sequence of tokens is the sum of the logprob of all tokens in the sequence.</p>

\[\text{logprob}(\text{I love food}) = \text{logprob}(\text{I}) + \text{logprob}(\text{love}|\text{I}) + \text{logprob}(\text{food}|\text{I, love})\]

<p>With summing, longer sequences are likely to have to lower total logprob (log(1) = 0, and log of all positive values less than 1 is negative). To avoid biasing towards short sequences, we use the average logprob by dividing the sum by its sequence length. After sampling multiple outputs, we pick the one with the highest average logprob. As of writing, this is what OpenAI API uses. You can set the parameter <em><a href="https://platform.openai.com/docs/api-reference/completions/create#completions-create-best_of">best_of</a></em> to a specific value, say 10, to ask OpenAI models to return the output with the highest average logprob out of 10 different outputs.</p>

<p>Another method is to use a reward model to score each output, as discussed in the previous section. Recall that both <a href="https://multithreaded.stitchfix.com/blog/2023/03/06/expert-in-the-loop-generative-ai-at-stitch-fix/">Stitch Fix</a> and <a href="https://engineering.grab.com/llm-powered-data-classification">Grab</a> pick the outputs given high scores by their reward models or verifiers. OpenAI also trained verifiers to help their models pick the best solutions to math problems (<a href="https://arxiv.org/pdf/2110.14168.pdf">Cobbe et al., 2021</a>). They found that sampling more outputs led to better performance, but only up to a certain point. In their experiment, this point is 400 outputs. Beyond this point, performance starts to decrease, as shown below. They hypothesized that as the number of sampled outputs increases, the chance of finding adversarial outputs that can fool the verifiers also increases. While this is an interesting experiment, I don’t believe anyone in production samples 400 different outputs for each input. The cost would be astronomical.</p>

<center>
    <figure>
    <img alt="Sampling the next token based on token probabilities" src="/assets/pics/sampling/6-test-time-sampling.png" style="float: center; max-width: 50%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>You can also choose heuristics based on the needs of your application. For example, if your application benefits from shorter responses, you can pick the shortest one. If your application is to convert from natural language to SQL queries, you can pick the valid SQL query that is the most efficient.</p>

<p>Sampling multiple outputs can be useful for tasks that expect exact answers. For example, given a math problem, the model can solve it multiple times and pick the most frequent answer as its final solution. Similarly, for a multiple-choice question, a model can pick the most frequently output option. This is what Google did when <a href="https://storage.googleapis.com/deepmind-media/gemini/gemini_1_report.pdf">evaluating their model Gemini on MMLU</a>, a benchmark of multiple-choice questions. They sampled 32 outputs for each question. While this helped Gemini achieve a high score on this benchmark, it’s unclear whether their model is better than another model that gets a lower score by only generating one output for each question.</p>

<p>The more fickle a model is, the more we can benefit from sampling multiple outputs. The optimal thing to do with a fickle model, however, is to swap it out for another. For one project, we used AI to extract certain information from an image of the product. We found that for the same image, our model could read the information only half of the time. For the other half, the model said that the image was too blurry or the text was too small to read. For each image, we queried the model at most three times, until it could extract the information.</p>

<p>While we can usually expect some model performance improvement by sampling multiple outputs, it’s expensive. On average, generating two outputs costs approximately twice as much as generating one.</p>

<h2 id="structured_outputs">Structured Outputs</h2>

<p>Oftentimes, in production, we need models to generate text following certain formats. Having structured outputs is essential for the following two scenarios.</p>

<ol>
  <li>Tasks whose outputs need to follow certain grammar. For example, for text-to-SQL or text-to-regex, outputs have to be valid SQL queries and regexes. For classification, outputs have to be valid classes.</li>
  <li>Tasks whose outputs are then parsed by downstream applications. For example, if you use an AI model to write product descriptions, you want to extract only the product descriptions without buffer texts like “<em>Here’s the description</em>” or “<em>As a language model, I can’t …</em>”. Ideally, for this scenario, models should generate structured outputs, such as JSON with specific keys, that can be parseable.</li>
</ol>

<p>OpenAI was the first model provider to introduce <em><a href="https://platform.openai.com/docs/guides/text-generation/json-mode">JSON mode</a></em> in their text generation API. Note that their JSON mode guarantees only that the outputs are valid JSON, not what’s inside the JSON.  As of writing, OpenAI’s JSON mode doesn’t yet work for vision models, but I’m sure it’ll just be a matter of time.</p>

<p>The generated JSONs can also be truncated due to the model’s stopping condition, such as when it reaches the maximum output token length. If the max token length is set too short, the output JSONs can be truncated and hence not parseable. If it’s set too long, the model’s responses become both too slow and expensive.</p>

<p>Independent tools like <a href="https://github.com/guidance-ai/guidance">guidance</a> and <a href="https://github.com/outlines-dev/outlines">outlines</a> let you structure the outputs of certain models. Here are two examples of using guidance to generate outputs constrained to a set of options and a regex.</p>

<center>
    <figure>
    <img alt="Sampling structured outputs" src="/assets/pics/sampling/7-guidance.png" style="float: center; max-width: 81%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<h3 id="how_to_generate_structured_outputs">How to generate structured outputs</h3>

<p>You can guide a model to generate constrained outputs at different layers of the AI stack: during prompting, sampling, and finetuning. Prompting is currently the easiest but least effective method. You can instruct a model to output valid JSON following a specific schema. However, there’s no guarantee that the model will always follow this instruction.</p>

<p>Finetuning is currently the go-to approach to get models to generate outputs in the style and format that you want. You can do finetuning with or without changing the model’s architecture. For example, you can finetune a model on examples with the output format you want. While this still doesn’t guarantee the model will always output the expected format, this is much more reliable than prompting. It also has the added benefit of reducing inference costs, assuming that you no longer have to include instructions and examples of the desirable format in your prompt.</p>

<p>For certain tasks, you can guarantee the output format with finetuning by modifying the model’s architecture. For example, for classification, you can append a classifier head to the foundation model’s architecture to make sure that the model only outputs one of the pre-specified classes. During finetuing, you can retrain the entire architecture or only this classifier head.</p>

<center>
    <figure>
    <img alt="Sampling the next token based on token probabilities" src="/assets/pics/sampling/8-finetuning-classifier.png" style="float: center; max-width: 95%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>Both sampling and finetuning techniques are needed because of the assumption that the model, by itself, isn’t capable of doing it. As models become more powerful, we can expect them to get better at following instructions. I suspect that in the future, it’ll be easier to get models to output exactly what we need with minimal prompting, and these techniques will become less important.</p>

<h3 id="constraint_sampling">Constraint sampling</h3>

<p>Constraint sampling is a technique used to guide the generation of text towards certain constraints. The simplest but expensive way to do so is to keep on generating outputs until you find one that fits your constraints, as discussed in the section <a href="#test_time_compute"> Test Time Compute </a>.</p>

<p>Constraint sampling can also be done during token sampling. I wasn’t able to find a lot of literature on how companies today are doing it. What’s written below is from my understanding, which can be wrong, so feedback and pointers are welcome!</p>

<p>At a high level, to generate a token, the model samples among values that meet the constraints. Recall that to generate a token, your model first outputs a logit vector, each logit corresponds to one possible value. With constrained sampling, we filter this logit vector to keep only the values that meet our constraints. Then we sample from these valid values.</p>

<center>
    <figure>
    <img alt="Sampling the next token based on token probabilities" src="/assets/pics/sampling/9-constrained-sampling.png" style="float: center; max-width: 85%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>In the above example, the constraint is straightforward to filter for. However, in most cases, it’s not that straightforward. We need to have a grammar that specifies what is and isn’t allowed at each step. For example, JSON grammar dictates that after <code class="language-plaintext highlighter-rouge">{</code>, we can’t have another <code class="language-plaintext highlighter-rouge">{</code> unless it’s part of a string, as in <code class="language-plaintext highlighter-rouge">{"key": ""}</code>.</p>

<p>Building out that grammar and incorporating that grammar into the sampling process is non-trivial. We’d need a separate grammar for every output format we want: JSON, regex, CSV, etc. Some are against constrained sampling because they believe the resources needed for constrained sampling are better invested in training models to become better at following instructions.</p>

<h2 id="conclusion">Conclusion</h2>

<p>I believe understanding how an AI model samples its outputs is essential for anyone who wishes to leverage AI to solve their problems. Probability is magical but can also be confusing. Writing this post has been a lot of fun as it gave me a chance to dig deeper into many concepts that I’ve been curious about for a long time.</p>

<p>As always, feedback is much appreciated. Thanks <a href="https://leehanchung.github.io/">Han Lee</a> and <a href="https://twitter.com/luke_metz">Luke Metz</a> for graciously agreeing to be my first readers.</p>

  </div>

  <!-- Twitter cards -->
  <meta name="twitter:site"    content="@chipro">
  <meta name="twitter:creator" content="@Chip Huyen">
  <meta name="twitter:title"   content="Generation configurations: temperature, top-k, top-p, and test time compute">

  
  <meta name="twitter:description" content="ML models are probabilistic. This probabilistic nature makes AI great for creative tasks, but fatal for tasks that depend on consistency and factuality. To understand why AI’s responses are probabilistic, we need to understand how models generate responses, a process known as sampling. In this post, we'll go over different sampling strategies and variables, including temperature, top-k, and top-p. We'll also discuss how to sample multiple outputs to improve a model's performance, and how to get a model to generate outputs of a certain format.">
  

  
  <meta name="twitter:card"  content="summary_large_image">
  <meta name="twitter:image" content="https://huyenchip.com/assets/pics/sampling/4-logprobs.png">
  
  <!-- end of Twitter cards -->
  
  <!-- <div id="collective_recsys"></div> -->
  <!-- <script async data-uid="45ca838230" src="https://chiphuyen.ck.page/45ca838230/index.js"></script> -->
  <br>
  
  
    
  <div id="disqus_thread"></div>
  <script>
    var disqus_config = function () {
      this.page.url = 'https://huyenchip.com/2024/01/16/sampling.html';
      this.page.identifier = 'https://huyenchip.com/2024/01/16/sampling.html';
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
        <path d="M127.999746,23.06353 C162.177385,23.06353 166.225393,23.1936027 179.722476,23.8094161 C192.20235,24.3789926 198.979853,26.4642218 203.490736,28.2166477 C209.464938,30.5386501 213.729395,33.3128586 218.208268,37.7917319 C222.687141,42.2706052 225.46135,46.5350617 227.782844,52.5092638 C229.535778,57.0201472 231.621007,63.7976504 232.190584,76.277016 C232.806397,89.7746075 232.93647,93.8226147 232.93647,128.000254 C232.93647,162.177893 232.806397,166.225901 232.190584,179.722984 C231.621007,192.202858 229.535778,198.980361 227.782844,203.491244 C225.46135,209.465446 222.687141,213.729903 218.208268,218.208776 C213.729395,222.687649 209.464938,225.461858 203.490736,227.783352 C198.9