---

source_url: https://huyenchip.com//2023/10/10/multimodal.html
ingested: 2026-07-10
sha256: 192691bfce58383820119da90c99cf612bb1fb10ffe736ef64905a233ce70213
blog_source: Chip Huyen
---

<!DOCTYPE html>
<html lang="en">

  <head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>Multimodality and Large Multimodal Models (LMMs)</title>
  <meta name="description" content="For a long time, each ML model operated in one data mode – text (translation, language modeling), image (object detection, image classification), or audio (s...">
  
  <link rel="stylesheet" href="/assets/main.css">
  <link rel="canonical" href="https://huyenchip.com/2023/10/10/multimodal.html">
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
<title>Multimodality and Large Multimodal Models (LMMs) | Chip Huyen</title>
<meta name="generator" content="Jekyll v3.10.0" />
<meta property="og:title" content="Multimodality and Large Multimodal Models (LMMs)" />
<meta name="author" content="Chip Huyen" />
<meta property="og:locale" content="en_US" />
<meta name="description" content="For a long time, each ML model operated in one data mode – text (translation, language modeling), image (object detection, image classification), or audio (speech recognition)." />
<meta property="og:description" content="For a long time, each ML model operated in one data mode – text (translation, language modeling), image (object detection, image classification), or audio (speech recognition)." />
<link rel="canonical" href="https://huyenchip.com/2023/10/10/multimodal.html" />
<meta property="og:url" content="https://huyenchip.com/2023/10/10/multimodal.html" />
<meta property="og:site_name" content="Chip Huyen" />
<meta property="og:image" content="https://huyenchip.com/assets/pics/multimodal/4-CLIP-architecture.png" />
<meta property="og:type" content="article" />
<meta property="article:published_time" content="2023-10-10T00:00:00+00:00" />
<meta name="twitter:card" content="summary_large_image" />
<meta property="twitter:image" content="https://huyenchip.com/assets/pics/multimodal/4-CLIP-architecture.png" />
<meta property="twitter:title" content="Multimodality and Large Multimodal Models (LMMs)" />
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Chip Huyen"},"dateModified":"2023-10-10T00:00:00+00:00","datePublished":"2023-10-10T00:00:00+00:00","description":"For a long time, each ML model operated in one data mode – text (translation, language modeling), image (object detection, image classification), or audio (speech recognition).","headline":"Multimodality and Large Multimodal Models (LMMs)","image":"https://huyenchip.com/assets/pics/multimodal/4-CLIP-architecture.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://huyenchip.com/2023/10/10/multimodal.html"},"url":"https://huyenchip.com/2023/10/10/multimodal.html"}</script>
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
      <a href="#part_1_understanding_multimodal">Part 1. Understanding Multimodal</a>
<ul class="sidebar-list">
    <li><a href="#why_multimodal">Why multimodal</a></li>
    <li><a href="#data_modalities">Data modalities</a></li>
    <li><a href="#multimodal_tasks">Multimodal tasks</a>
        <ul>
            <li><a href="#generation">Generation</a></li>
            <li><a href="#vision_language_understanding">Vision-language understanding</a></li>
        </ul>
    </li>
</ul>

<a href="#part_2_multimodal_training">Part 2. Fundamentals of Multimodal Training</a>
<ul class="sidebar-list">
    <li><a href="#clip">CLIP: Contrastive Language-Image Pre-training</a>
        <ul>
            <li><a href="#clip_s_high_level_architecture">CLIP's high-level architecture</a></li>
            <li><a href="#natural_language_supervision">Natural language supervision</a></li>
            <li><a href="#contrastive_learning">Contrastive learning</a>
                <ul>
                    <li><a href="#classifier_objective">Classifier objective</a></li>
                    <li><a href="#lm_objective">Language model objective</a></li>
                    <li><a href="#contrastive_objective">Contrastive objective</a></li>
                </ul>
            </li>
            <li><a href="#clip_applications">CLIP applications</a></li>
        </ul>
    </li>
    <li><a href="#flamingo">Flamingo: the dawns of LMMs</a>
        <ul>
            <li><a href="#flamingo_s_high_level_architecture">Flamingo's high-level architecture</a></li>
            <li><a href="#data">Data</a></li>
            <li><a href="#flamingo_s_vision_encoder">Flamingo's vision encoder</a></li>
            <li><a href="#flamingo_s_language_model">Flamingo's language model</a></li>
        </ul>
    </li>
    <li><a href="#clip_vs_flamingo">TL;DR: CLIP vs. Flamingo</a></li>
</ul>

<a href="#part_3_research_directions_for_lmms">Part 3. Research Directions for LMMs</a>
<ul class="sidebar-list">
    <li><a href="#incorporating_more_data_modalities">Incorporating more data modalities</a></li>
    <li><a href="#multimodal_systems_for_instruction_following">Multimodal systems for instruction-following</a></li>
    <li><a href="#adapters_for_more_efficient_multimodal_training">Adapters for more efficient multimodal training</a></li>
    <li><a href="#generating_multimodal_outputs">Generating multimodal outputs</a></li>
</ul>

<a href="#conclusion">Conclusion</a><br>
<a href="#resources">Resources</a>

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
    <h1 class="post-title" itemprop="name headline">Multimodality and Large Multimodal Models (LMMs)</h1>
    <p class="post-meta">
      <time datetime="2023-10-10T00:00:00+00:00" itemprop="datePublished">
        
        Oct 10, 2023
      </time>
      
        • <span itemprop="author" itemscope itemtype="http://schema.org/Person"><span itemprop="name">Chip Huyen</span></span>
      </p>
  </header>

  <div class="post-content" itemprop="articleBody">
    <p>For a long time, each ML model operated in one data mode – text (translation, language modeling), image (object detection, image classification), or audio (speech recognition).</p>

<p>However, natural intelligence is not limited to just a single modality. Humans can read, talk, and see. We listen to music to relax and watch out for strange noises to detect danger. Being able to work with multimodal data is essential for us or any AI to operate in the real world.</p>

<p>OpenAI noted in their <a href="https://cdn.openai.com/papers/GPTV_System_Card.pdf">GPT-4V system card</a> that “<em>incorporating additional modalities (such as image inputs) into LLMs is viewed by some as a key frontier in AI research and development</em>.”</p>

<p>Incorporating additional modalities to LLMs (Large Language Models) creates LMMs (Large Multimodal Models). Not all multimodal systems are LMMs. For example, text-to-image models like Midjourney, Stable Diffusion, and Dall-E are multimodal but don’t have a language model component. Multimodal can mean one or more of the following:</p>

<ol>
  <li>Input and output are of different modalities (e.g. text-to-image, image-to-text)</li>
  <li>Inputs are multimodal (e.g. a system that can process both text and images)</li>
  <li>Outputs are multimodal (e.g. a system that can generate both text and images)</li>
</ol>

<p>This post covers multimodal systems in general, including LMMs. It consists of 3 parts.</p>

<ul>
  <li>Part 1 covers the context for multimodality, including why multimodal, different data modalities, and types of multimodal tasks.</li>
  <li>Part 2 discusses the fundamentals of a multimodal system, using the examples of CLIP, which lays the foundation for many future multimodal systems, and Flamingo, whose impressive performance gave rise to LMMs.</li>
  <li>Part 3 discusses some active research areas for LMMs, including generating multimodal outputs and adapters for more efficient multimodal training, covering newer multimodal systems such as BLIP-2, LLaVA, LLaMA-Adapter V2, LAVIN, etc.</li>
</ul>

<p>The post is long. Feel free to skip to the sections most interesting to you.</p>

<p><b>⚠ Ambiguous terminology ⚠</b><br />
Multimodal data can also refer to multimodal distributions, e.g. bimodal distribution, which is different from multimodal data in this post.
<br /><br /></p>

<hr />
<p><b>Table of contents</b><br />
<a href="#part_1_understanding_multimodal">Part 1. Understanding Multimodal</a><br />
…. <a href="#why_multimodal">Why multimodal</a><br />
…. <a href="#data_modalities">Data modalities</a><br />
…. <a href="#multimodal_tasks">Multimodal tasks</a><br />
…….. <a href="#generation">Generation</a><br />
…….. <a href="#vision_language_understanding">Vision-language understanding</a><br />
<a href="#part_2_multimodal_training">Part 2. Fundamentals of Multimodal Training</a><br />
…. <a href="#clip">CLIP: Contrastive Language-Image Pre-training</a><br />
…….. <a href="#clip_s_high_level_architecture">CLIP’s high-level architecture</a><br />
…….. <a href="#natural_language_supervision">Natural language supervision</a><br />
…….. <a href="#contrastive_learning">Contrastive learning</a><br />
…….. <a href="#clip_applications">CLIP applications</a><br />
…. <a href="#flamingo">Flamingo: the dawns of LMMs</a><br />
…….. <a href="#flamingo_s_high_level_architecture">Flamingo’s high-level architecture</a><br />
…….. <a href="#data">Data</a><br />
…….. <a href="#flamingo_s_vision_encoder">Flamingo’s vision encoder</a><br />
…….. <a href="#flamingo_s_language_model">Flamingo’s language model</a><br />
…. <a href="#clip_vs_flamingo">TL;DR: CLIP vs. Flamingo</a><br />
<a href="#part_3_research_directions_for_lmms">Part 3. Research Directions for LMMs</a><br />
…. <a href="#incorporating_more_data_modalities">Incorporating more data modalities</a><br />
…. <a href="#multimodal_systems_for_instruction_following">Multimodal systems for instruction-following</a><br />
…. <a href="#adapters_for_more_efficient_multimodal_training">Adapters for more efficient multimodal training</a><br />
…. <a href="#generating_multimodal_outputs">Generating multimodal outputs</a><br />
<a href="#conclusion">Conclusion</a><br />
<a href="#resources">Resources</a><br /></p>

<hr />
<p><br /></p>

<h2 id="part_1_understanding_multimodal">Part 1. Understanding Multimodal</h2>

<h2 id="why_multimodal">Why multimodal</h2>

<p>Many use cases are impossible without multimodality, especially those in industries that deal with a mixture of data modalities such as healthcare, robotics, e-commerce, retail, gaming, etc.</p>

<center>
    <figure>
    <img alt="Multimodal AI in healthcare" src="/assets/pics/multimodal/26-healthcare.png" style="float: center; max-width: 70%; margin: 0 0 0em 0em" />
    </figure>
    An example of how multimodality can be used in healthcare. Image from Multimodal biomedical AI (Acosta et al., Nature Medicine 2022)
</center>
<p><br /></p>

<p>Not only that, incorporating data from other modalities can help boost model performance. Shouldn’t a model that can learn from both text and images perform better than a model that can learn from only text or only image?</p>

<p>Multimodal systems can provide a more flexible interface, allowing you to interact with them in whichever way works best for you at the moment. Imagine you can ask a question by typing, talking, or just pointing your camera at something.</p>

<p>One use case that I’m especially excited about, is that multimodality can also enable visually impaired people to browse the Internet and also navigate the real world.</p>

<center>
    <figure>
    <img alt="Some cool multimodal use cases from GPT-4V" src="/assets/pics/multimodal/1-gpt-4v-use-cases.png" style="float: center; max-width: 100%; margin: 0 0 0em 0em" />
    </figure>
    Some cool multimodal use cases from GPT-4V
</center>
<p><br /></p>

<h2 id="data_modalities">Data modalities</h2>

<p>Different data modes are text, image, audio, tabular data, etc. One data mode can be represented or <em>approximated</em> in another data mode. For example:</p>

<ul>
  <li>Audio can be represented as images (mel spectrograms).</li>
  <li>Speech can be transcribed into text, though its text-only representation loses information such as volume, intonation, pauses, etc.</li>
  <li>An image can be represented as a vector, which, in turn, can be flattened and represented as a sequence of text tokens.</li>
  <li>A video is a sequence of images plus audio. ML models today mostly treat videos as sequences of images. This is a severe limitation, as sounds have proved to be just as important as visuals for videos. <a href="https://www.kantar.com/uki/inspiration/advertising-media/the-power-of-tiktok">88% of TikTok users shared that sound is essential for their TikTok experience</a>.</li>
  <li>A text can be represented as an image if you simply take a picture of it.</li>
  <li>A data table can be converted into a chart, which is an image.</li>
</ul>

<hr />
<p><b>How about other data modalities?<b><br /></b></b></p>

<p>All digital data formats can be represented using bitstrings (strings of 0 and 1) or bytestrings. A model that can effectively learn from bitstrings or bytestrings will be very powerful, and it can learn from any data mode.<br /></p>

<p>There are other data modalities we haven’t touched on, such as graphs and 3D assets. We also haven’t touched on the formats used to represent smell and touch (haptics).</p>

<hr />
<p><br />
In ML today, audio is still largely treated as a voice-based alternative to text. The most common use cases for audio are still speech recognition (speech-to-text) and speech synthesis (text-to-speech). Non-speech audio use cases, e.g. music generation, are still pretty niche. See the fake Drake &amp; Weeknd song and <a href="https://huggingface.co/spaces/facebook/MusicGen">MusicGen model on HuggingFace</a>.</p>

<p>Image is perhaps the most versatile format for model inputs, as it can be used to represent text, tabular data, audio, and to some extent, videos. There’s also so much more visual data than text data. We have phones/webcams that constantly take pictures and videos today.</p>

<p>Text is a much more powerful mode for model outputs. A model that can generate images can only be used for image generation, whereas a model that can generate text can be used for many tasks: summarization, translation, reasoning, question answering, etc.</p>

<p>For simplicity, we’ll focus on 2 modalities: images and text. The learnings can be somewhat generalized to other modalities.</p>

<h2 id="multimodal_tasks">Multimodal tasks</h2>
<p>To understand multimodal systems, it’s helpful to look at the tasks they are built to solve. In literature, I commonly see vision-language tasks divided into two groups: <strong>generation</strong> and <strong>vision-language understanding</strong> (VLU), which is the umbrella term for all tasks that don’t require generation. The line between these two groups is blurred, as being able to generate answers requires understanding too.</p>

<h3 id="generation">Generation</h3>

<p>For generative tasks, the output can be unimodal (e.g. text, image, 3D rendering) or multimodal. While unimodal outputs are common today, multimodal outputs are still shaping up. We’ll discuss multimodal outputs at the end of this post.</p>

<h4 id="image-generation-text-to-image-synthesis">Image generation (text-to-image synthesis)</h4>

<p>This category is straightforward. Examples: Dall-E, Stable Diffusion, and Midjourney.</p>

<h4 id="text-generation">Text generation</h4>

<p>A common text generation task is visual question answering. Instead of relying only on text for the context, you can give the model both text and images. Imagine you can point your camera to anything and ask questions like: “My car won’t start. What’s wrong with it?”, “How to make this dish?”, or “What is this meme about?”.</p>

<p>Another common use case is image captioning, which can be used as part of a text-based image retrieval system. An organization might have millions, if not billions, of images: product images, graphs, designs, team pictures, promotional materials, etc. AI can automatically generate captions and metadata for them, making it easier to find the exact images you want.</p>

<h3 id="vision_language_understanding">Vision-language understanding</h3>
<p>We’ll zoom into two task types: classification and text-based image retrieval (TBIR).</p>

<h4 id="classification">Classification</h4>

<p>Classification models can only generate outputs that belong to a pre-determined list of classes. This works when you only care about a fixed number of outcomes. For example, an OCR system only needs to predict if a visual is one of the known characters (e.g. a digit or a letter).</p>

<p><strong>Side note</strong>: An OCR system processes data at the character level. When used together with a system that can understand the broader context, it can improve use cases such as allowing you to “talk” to any textbook, contract, assembly instructions, etc.</p>

<center>
    <figure>
    <img alt="Document processing with GPT-4V" src="/assets/pics/multimodal/2-gpt-4v-ocr.png" style="float: center; max-width: 80%; margin: 0 0 0em 0em" />
    </figure>
    Document processing with GPT-4V. The model's mistake is highlighted in red.
</center>
<p><br /></p>

<p>One related task to classification is <strong>image-to-text retrieval</strong>: given an image and a pool of pre-defined texts, find the text that’s most likely to accompany the image. This can be helpful for product image search, i.e. retrieving product reviews from a picture.</p>

<h4 id="text-based-image-retrieval-image-search">Text-based image retrieval (image search)</h4>

<p>Image search matters not only for search engines but also for enterprises to be able to search through all their internal images and documents. Some people call text-based image retrieval “text-to-image retrieval”.</p>

<p>There are several approaches to text-based image retrieval. Two of them are:</p>

<ol>
  <li>Generate captions and metadata for each image, either manually or automatically (see image captioning in <strong>Text generation</strong>). Given a text query, find images whose captions/metadata are closest to this text query.</li>
  <li>Train a joint embedding space for both images and text. Given a text query, generate an embedding for this query, and find all images whose embeddings are closest to this embedding.</li>
</ol>

<p>The second approach is more flexible, and I believe will be more widely used. This approach requires having a strong joint embedding space for both vision and language, like the one that OpenAI’s <a href="https://arxiv.org/abs/2103.00020">CLIP</a> developed.</p>

<h2 id="part_2_multimodal_training">Part 2. Fundamentals of Multimodal Training</h2>

<p>Given the existence of so many amazing multimodal systems, a challenge of writing this post is choosing which systems to focus on. In the end, I decided to focus on two models: <a href="https://arxiv.org/abs/2103.00020">CLIP</a> (2021) and <a href="https://arxiv.org/abs/2204.14198">Flamingo</a> (2022) both for their significance as well as availability and clarity of public details.</p>

<ul>
  <li>CLIP was the first model that could generalize to multiple <strong>image classification tasks</strong> with zero- and few-shot learning.</li>
  <li>Flamingo wasn’t the first large multimodal model that could <strong>generate open-ended responses</strong> (<a href="https://arxiv.org/abs/2201.12086">Salesforce’s BLIP</a> came out 3 months prior). However, Flamingo’s strong performance prompted some to consider it <a href="https://arxiv.org/abs/2304.08485">the GPT-3 moment in the multimodal domain</a>.</li>
</ul>

<p>Even though these two models are older, many techniques they use are still relevant today. I hope they serve as the foundation to understanding newer models. The multimodal space is evolving repaidly, with many new ideas being developed. We’ll go over these newer models in <a href="#part_3_research_directions_for_lmms">Part 3</a>.</p>

<p>At a high level, a multimodal system consists of the following components:</p>
<ol>
  <li>An <strong>encoder</strong> for each data modality to generate the embeddings for data of that modality.</li>
  <li>A way to <strong>align embeddings</strong> of different modalities into the same <strong>multimodal embedding space</strong>.</li>
  <li>[Generative models only] A <strong>language model to generate text responses</strong>. Since inputs can contain both text and visuals, new techniques need to be developed to allow the language model to condition its responses on not just text, but also visuals.</li>
</ol>

<p>Ideally, as many of these components should be pretrained and reusable as possible.</p>

<h2 id="clip">CLIP: Contrastive Language-Image Pre-training</h2>

<p>CLIP’s key contribution is its ability to map data of different modalities, text and images, into a shared embedding space. This shared multimodal embedding space makes text-to-image and image-to-text tasks so much easier.</p>

<p>Training this multimodal embedding space also produced a strong image encoder, which allows CLIP to achieve <strong>competitive zero-shot performance on many image classification tasks</strong>. This strong image encoder can be used for many other tasks: image generation, visual question answering, and text-based image retrieval. Flamingo and LLaVa use CLIP as their image encoder. DALL-E uses CLIP to rerank generated images. It’s unclear if GPT-4V uses CLIP.</p>

<center>
    <figure>
    <img alt="Zero-shot image classification with CLIP" src="/assets/pics/multimodal/3-CLIP-image-classification.png" style="float: center; max-width: 75%; margin: 0 0 0em 0em" />
    </figure>
    Zero-shot image classification with CLIP
</center>
<p><br /></p>

<p>CLIP leveraged <strong>natural language supervision</strong> and <strong>contrastive learning</strong>, which allowed CLIP to both scale up their data and make training more efficient. We’ll go over why/how these two techniques work.</p>

<h3 id="clip_s_high_level_architecture">CLIP's high-level architecture</h3>

<center>
    <figure>
    <img alt="Architecture of OpenAI's CLIP" src="/assets/pics/multimodal/4-CLIP-architecture.png" style="float: center; max-width: 100%; margin: 0 0 0em 0em" />
    </figure>
    CLIP's architecture. Both encoders and projection matrices are jointly trained together from scratch. The training goal is to maximize the similarity scores of the right (image, text) pairings while minimizing the similarity scores of the wrong pairings (contrastive learning). 
</center>
<p><br /></p>

<p>For the <strong>image encoder</strong>, the authors experimented with both ResNet and ViT. Their best-performing model is <code class="language-plaintext highlighter-rouge">ViT-L/14@336px</code>:</p>

<ul>
  <li>Large vision transformer (ViT-L)</li>
  <li>14 patches (each image is divided into 14x14 pixel patches/sub-images)</li>
  <li>on 336x336 pixel input</li>
</ul>

<p>For the <strong>text encoder</strong>, CLIP uses a Transformer model similar to <a href="https://openai.com/research/better-language-models">GPT-2</a> but smaller. Their base model has only 63M parameters with 8 attention heads. The authors found CLIP’s performance to be less sensitive to the capacity of the text encoder.</p>

<p>Embeddings generated by the image encoder and text encoder are projected into the same embedding space using two projection matrices \(W_v\) and \(W_l\).</p>

<ul>
  <li>Given an image embedding \(V_i\), the corresponding multimodal embedding is computed as: \(W_vV_i\).</li>
  <li>Given a text embedding \(L_i\), the corresponding multimodal embedding is computed as: \(W_lL_i\).</li>
</ul>

<p>When people say CLIP embeddings, they either refer to these multimodal embeddings or the embeddings generated by CLIP’s image encoder.</p>

<h3 id="natural_language_supervision">Natural language supervision</h3>

<p>For many years, image models were trained with manually annotated (image, text) datasets (e.g. ImageNet, MS COCO). This isn’t scalable. Manual annotation is time-consuming and expensive.</p>

<p>The CLIP paper noted that none of the then-available (image, text) datasets was big and high quality enough. They created their own dataset – 400M (image, text) pairs – as follows.</p>

<ol>
  <li>Construct a list of 500,000 queries. Queries are common words, bigrams, and titles of popular Wikipedia articles.</li>
  <li>Find images matching these queries (string and substring match). The paper mentioned this search did NOT happen on search engines but didn’t specify where. My theory is that since OpenAI already scraped the entire Internet for their GPT models, they probably just queried their internal database.</li>
  <li>Each image is paired with a text that co-occurs with it (e.g. captions, comments) instead of the query since queries are too short to be descriptive.</li>
</ol>

<p>Because some queries are more popular than others, to avoid data imbalance, they used at most 20K images for a query.</p>

<h3 id="contrastive_learning">Contrastive learning</h3>
<p>Pre-CLIP, most vision-language models were trained using a classifier or language model objectives. Contrastive objective is a clever technique that allows CLIP to scale and generalize to multiple tasks.</p>

<p>We’ll show why the constrastive objective works better for CLIP using an example task of image captioning: given an image, generate a text that describes it.</p>

<h4 id="classifier_objective">Classifier objective</h4>

<p>A classifier predicts the correct class among a predetermined list of classes. This works when the output space is finite. Previous models that work with (image, text) pair datasets all had this limitation. For example, models working with <a href="https://www.image-net.org/challenges/LSVRC/2012/">ILSVRC-2012</a> limited themselves to 1,000 classes, and <a href="https://arxiv.org/abs/1707.02968">JFT-300M</a> to 18,291 classes.</p>

<p>This objective limits not only the model’s capacity to output meaningful responses but also its capacity for zero-shot learning. Say, if the model was trained to predict among 10 classes, it won’t work for a task that has 100 classes.</p>

<h4 id="lm_objective">Language model objective</h4>

<p>If a classifier outputs only one class for each input, a language model outputs a sequence of classes. Each generated class is called a token. Each token is from a predetermined list, the vocabulary, of the language model.</p>

<center>
    <figure>
    <img alt="Classifier vs. language model objectives" src="/assets/pics/multimodal/5-classifier-vs-language-model-objectives.png" style="float: center; max-width: 90%; margin: 0 0 0em 0em" />
    </figure>
    Classifier vs. language model objectives
</center>
<p><br /></p>

<h4 id="contrastive_objective">Contrastive objective</h4>

<p>While the language model objective allows for vastly more flexible outputs, CLIP authors noted this objective made the training difficult. They hypothesized that this is because the model tries to generate <em>exactly</em> the text accompanying each image, while many possible texts can accompany an image: alt-text, caption, comments, etc.</p>

<p>For example, in the <a href="https://arxiv.org/abs/1509.04942">Flickr30K dataset</a>, each image has 5 captions provided by human annotators, and the captions for the same image can be very different.</p>

<center>
    <figure>
    <img alt="Multiple captions for the same image" src="/assets/pics/multimodal/6-multiple-captions.png" style="float: center; max-width: 85%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>Contrastive learning is to overcome this challenge. Instead of predicting the exact text of each image, CLIP was trained to predict whether a text is more likely to accompany an image than other texts.</p>

<p>For each batch of \(N\) (image, text) pairs, the model generates N text embeddings and N image embeddings.</p>

<ul>
  <li>Let \(V_1, V_2, ..., V_n\) be the embeddings for the \(N\) images.</li>
  <li>Let \(L_1, L_2, ..., L_n\) be the embeddings for the \(N\) texts.</li>
</ul>

<p>CLIP computes the cosine similarity scores of the \(N^2\) possible (\(V_i, L_j\)) pairings. The model is trained to maximize the similarity scores of the \(N\) correct pairings while minimizing the scores of the \(N^2 - N\) incorrect pairings. For CLIP, \(N = 32,768\).</p>

<center>
    <figure>
    <img alt="How CLIP works" src="/assets/pics/multimodal/7-clip.png" style="float: center; max-width: 100%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>Another way to look at this is that each training batch of CLIP is two classification tasks.</p>

<ol>
  <li>
    <p>Each image can be paired with N possible texts, and the model tries to predict the correct one. This is the same setup as image-to-text retrieval.</p>

\[L_{\text{contrastive:txt2im}} = -\frac{1}{N}\sum_i^N\log(\frac{\exp(L_i^TV_i\beta)}{\sum_j^N\exp(L_i^TV_j\beta)})\]
  </li>
  <li>
    <p>Each text can be paired with N possible images, and the model tries to predict the correct image. This is the same setup as text-to-image retrieval.</p>

\[L_{\text{contrastive:im2txt}} = -\frac{1}{N}\sum_i^N\log(\frac{\exp(V_i^TL_i\beta)}{\sum_j^N\exp(V_i^TL_j\beta)})\]
  </li>
</ol>

<p>The sum of these two losses is minimized. 𝛽 is a trainable inverse temperature parameter.</p>

<p>This is what it all looks like in pseudocode.</p>

<center>
    <figure>
    <img alt="CLIP pseudocode" src="/assets/pics/multimodal/8-clip-pseudocode.png" style="float: center; max-width: 60%; margin: 0 0 0em 0em" />
    </figure>
</center>

<p>CLIP authors found that the contrastive objective provided a 12x improvement in efficiency compared to the language model objective baseline while producing higher-quality image embeddings.</p>

<center>
    <figure>
    <img alt="CLIP constrastive learning" src="/assets/pics/multimodal/9-contrastive-learning-efficiency.png" style="float: center; max-width: 60%; margin: 0 0 0em 0em" />
    </figure>
</center>

<h3 id="clip_applications">CLIP applications</h3>

<h4 id="classification-1">Classification</h4>

<p>Today, for many image classification tasks, CLIP is still a strong out-of-the-box baseline to be used as-is or fine-tuned.</p>

<center>
    <figure>
    <img alt="CLIP as a strong baseline for image classification" src="/assets/pics/multimodal/10-clip-perf.png" style="float: center; max-width: 50%; margin: 0 0 0em 0em" />
    </figure>
</center>

<h4 id="text-based-image-retrieval">Text-based image retrieval</h4>

<p>Since CLIP’s training process was conceptually similar to image-to-text retrieval and text-to-image retrieval, CLIP “<em>displays significant promise for widely-applicable tasks like image retrieval or search</em>.” However, “<em>on image retrieval, CLIP’s performance relative to the overall state of the art is noticeably lower.</em>”</p>

<p>There are attempts to use CLIP for image retrieval. For example, <a href="https://github.com/rom1504/clip-retrieval">clip-retrieval</a> package works as follows:</p>

<ol>
  <li>Generate CLIP embeddings for all your images and store them in a vector database.</li>
  <li>For each text query, generate a CLIP embedding for this text.</li>
  <li>Query in the vector database for all images whose embeddings are close to this text query embedding.</li>
</ol>

<h4 id="image-generation">Image generation</h4>

<p>CLIP’s joint image-text embeddings are useful for image generation. Given a text prompt, <a href="https://openai.com/research/dall-e">DALL-E</a> (2021) generates many different visuals and uses CLIP to rerank these visuals before showing the top visuals to users.</p>

<p>In 2022, OpenAI introduced <a href="https://openai.com/research/hierarchical-text-conditional-image-generation-with-clip-latents">unCLIP</a>, a text-to-image synthesis model conditioned on CLIP latents. It consists of two main components:</p>

<ol>
  <li>CLIP is trained and frozen. The pretrained CLIP model can generate embeddings for both text and images in the same embedding space.</li>
  <li>Two things happen at image generation:
    <ul>
      <li>Use CLIP to generate embedding for this text.</li>
      <li>Use a diffusion decoder to generate images conditioned on this embedding.</li>
    </ul>
  </li>
</ol>

<center>
    <figure>
    <img alt="unCLIP" src="/assets/pics/multimodal/11-unCLIP.png" style="float: center; max-width: 100%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<h4 id="text-generation-visual-question-answering-captioning">Text generation: visual question answering, captioning</h4>

<p>CLIP authors did attempt to create a model for text generation. One version they experimented with is called LM RN50. Though this model could generate text responses, its performance was consistently around 10% below CLIP’s best-performing model on all the vision-language understanding tasks that CLIP was evaluated on.</p>

<p>While today CLIP isn’t used directly for text generation, its image encoder is often the backbone for LMMs that can generate texts.</p>

<h2 id="flamingo">Flamingo: the dawns of LMMs</h2>

<p>Unlike CLIP, Flamingo can generate text responses. In a reductive view, Flamingo is CLIP + a language model, with added techniques to make it possible for the language model to generate text tokens conditioned on both visual and text inputs.</p>

<center>
    <figure>
    <img alt="Conversations with Flamingo LMMs" src="/assets/pics/multimodal/12-flamingo-chatbots.png" style="float: center; max-width: 100%; margin: 0 0 0em 0em" />
    </figure>
    Flamingo can generate text responses conditioned on both text and images
</center>
<p><br /></p>

<h3 id="flamingo_s_high_level_architecture">Flamingo's high-level architecture</h3>

<p>At a high level, Flamingo consists of 2 parts:</p>

<ol>
  <li><strong>Vision encoder</strong>: a CLIP-like model is trained using contrastive learning. The text encoder of this model is then discarded. The vision encoder is frozen to be used in the main model.</li>
  <li><strong>Language model</strong>: Flamingo finetunes Chinchilla to generate text tokens, conditioned on visuals and text, using language model loss, with two additional components Perceiver Resampler and GATED XATTN-DENSE layers. We’ll discuss them later in this blog.</li>
</ol>

<center>
    <figure>
    <img alt="Flamingo high level architecture" src="/assets/pics/multimodal/13-flamingo-architecture.png" style="float: center; max-width: 100%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<h3 id="data">Data</h3>

<p>Flamingo used 4 datasets: 2 (image, text) pair datasets, 1 (video, text) pair dataset, and 1 interleaved image and text dataset.</p>

<center>
    <figure>
    <img alt="Flamingo's 4 datasets" src="/assets/pics/multimodal/14-flamingo-data.png" style="float: center; max-width: 100%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

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
   <td><strong>Dataset</strong>
   </td>
   <td><strong>Type</strong>
   </td>
   <td><strong>Size</strong>
   </td>
   <td><strong>How</strong>
   </td>
   <td><strong>Training weight</strong>
   </td>
  </tr>
  <tr>
   <td>M3W
   </td>
   <td>Interleaved image and text dataset
   </td>
   <td>43M webpages
   </td>
   <td>For each webpage, they sample a random subsequence of 256 tokens and take up to the first 5 images included in the sampled sequence.
   </td>
   <td>1.0
   </td>
  </tr>
  <tr>
   <td>ALIGN
   </td>
   <td>(Image, text) pairs
   </td>
   <td>1.8B pairs
   </td>
   <td>Texts are alt-texts, averaging 12 tokens/text.
   </td>
   <td>0.2
   </td>
  </tr>
  <tr>
   <td>LTIP
   </td>
   <td>(Image, text) pairs
   </td>
   <td>312M pairs
   </td>
   <td>Texts are long descriptions, averaging 20.5 tokens/text.
   </td>
   <td>0.2
   </td>
  </tr>
  <tr>
   <td>VTP
   </td>
   <td>(Video, text) pairs
   </td>
   <td>27M short videos
   </td>
   <td>~22 seconds/video on average
   </td>
   <td>0.03
   </td>
  </tr>
</table>
<p><br /></p>

<h3 id="flamingo_s_vision_encoder">Flamingo's vision encoder</h3>

<p>Flamingo first trains a CLIP-like model from scratch using contrastive learning. This component only uses the 2 (image, text) pair datasets, ALIGN and LTIP, totaling 2.1B (image, text) pairs. This is 5x larger than the dataset CLIP was trained on.</p>

<ul>
  <li>For the text encoder, Flamingo uses BERT instead of GPT-2.</li>
  <li>For the vision encoder, Flamingo uses a NormalizerFree ResNet (NFNet) F6 model.</li>
  <li>Text and vision embeddings are meanpooled before being projected to the joint embedding space.</li>
</ul>

<h3 id="flamingo_s_language_model">Flamingo's language model</h3>

<p>Flamingo uses Chinchilla as their language model. More specifically, they freeze the 9 pretrained Chinchilla LM layers. A traditional language model predicts the next text token based on the preceding text tokens. Flamingo predicts the next text token based on both the preceding text and visual tokens.</p>

<center>
    <figure>
    <img alt="Flamingo's 4 datasets" src="/assets/pics/multimodal/15-lmm-text-generation.png" style="float: center; max-width: 53%; margin: 0 0 0em 0em" />
    </figure>
    Next token generation is conditioned on both text and visual tokens. Illustration taken from Chunyuan Li's CVPR 2023 tutorial: Large Multimodal Models.
</center>
<p><br /></p>

<p>To be able to generate text conditioned on both text and visual inputs, Flamingo relied on Perceiver Resampler and GATED XATTN-DENSE layers.</p>

<h4 id="perceiver-resampler">Perceiver Resampler</h4>

<p>As the visual inputs can be both images and videos, the vision encoder can produce a variable number of image or video features. Perceiver Resampler converts these variable features into a consistent 64 visual outputs.</p>

<p>Interestingly enough, while training the vision encoder, the resolution used was 288 x 288. However, at this phase, visual inputs are resized to 320 × 320. It’s been shown that <a href="https://arxiv.org/abs/1906.06423">a higher test-time resolution can lead to improved performance when using CNNs</a>.</p>

<center>
    <figure>
    <img alt="Flamingo's Perceiver Resampler" src="/assets/pics/multimodal/16-flamingo-perceiver-resampler.png" style="float: center; max-width: 90%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<h4 id="gated-xattn-dense-layers">GATED XATTN-DENSE layers</h4>

<p>GATED XATTN-DENSE layers are inserted between existing and frozen LM layers to allow the language model to attend more efficiently to the visual tokens when generating text tokens. Without these layers, Flamingo authors noted a drop of 4.2% in the overall score.</p>

<center>
    <figure>
    <img alt="Flamingo's GATED ATTN-DENSE layers" src="/assets/pics/multimodal/17-gated xattn-dense.png" style="float: center; max-width: 73%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<h4 id="loss-function">Loss function</h4>
<p>Flamingo computes the likelihood of text \(y\) conditioned on the interleaved images and videos \(x\).</p>

\[p(y|x) = \prod_{l=1}^N p(y_l|y_{&lt;l}, x_{\leq l})\]

<p>The training loss function was a weighted sum of expected negative log-likelihoods of generated text across all 4 datasets, with \(\lambda_m\) being the training weight of dataset \(m\).</p>

\[\sum_{m=1}^M \lambda_m E_{(x, y)\sim D_m} [ -\sum_{l=1}^L \log p(y|x)]\]

<h4 id="training">Training</h4>

<p>While the Chinchilla LM layers are finetuned and frozen, the additional components are trained from scratch, using all 4 Flamingo datasets, with different weights. <em>Finding the right per-dataset weights was key to performance.</em> The weight for each dataset is in the <strong>Training weight</strong> column in the dataset table above.</p>

<p>VTP’s weight is much smaller than other datasets (0.03 compared to 0.2 and 1), so its contribution to the training should be minimal. However, the authors noted that removing this dataset negatively affects performance on all video tasks.</p>

<p>While Flamin