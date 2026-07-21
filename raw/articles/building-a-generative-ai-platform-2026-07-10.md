---

source_url: https://huyenchip.com//2024/07/25/genai-platform.html
ingested: 2026-07-10
sha256: 3110f8ba485bbce59dbf026ef465a5d411b1072bedf0dbb1d8527229f7a2c764
blog_source: Chip Huyen
---

<!DOCTYPE html>
<html lang="en">

  <head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>Building A Generative AI Platform</title>
  <meta name="description" content="After studying how companies deploy generative AI applications, I noticed many similarities in their platforms. This post outlines the common components of a...">
  
  <link rel="stylesheet" href="/assets/main.css">
  <link rel="canonical" href="https://huyenchip.com/2024/07/25/genai-platform.html">
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
<title>Building A Generative AI Platform | Chip Huyen</title>
<meta name="generator" content="Jekyll v3.10.0" />
<meta property="og:title" content="Building A Generative AI Platform" />
<meta name="author" content="Chip Huyen" />
<meta property="og:locale" content="en_US" />
<meta name="description" content="After studying how companies deploy generative AI applications, I noticed many similarities in their platforms. This post outlines the common components of a generative AI platform, what they do, and how they are implemented. I try my best to keep the architecture general, but certain applications might deviate. This is what the overall architecture looks like." />
<meta property="og:description" content="After studying how companies deploy generative AI applications, I noticed many similarities in their platforms. This post outlines the common components of a generative AI platform, what they do, and how they are implemented. I try my best to keep the architecture general, but certain applications might deviate. This is what the overall architecture looks like." />
<link rel="canonical" href="https://huyenchip.com/2024/07/25/genai-platform.html" />
<meta property="og:url" content="https://huyenchip.com/2024/07/25/genai-platform.html" />
<meta property="og:site_name" content="Chip Huyen" />
<meta property="og:image" content="https://huyenchip.com/assets/pics/genai-platform/1-genai-platform.png" />
<meta property="og:type" content="article" />
<meta property="article:published_time" content="2024-07-25T00:00:00+00:00" />
<meta name="twitter:card" content="summary_large_image" />
<meta property="twitter:image" content="https://huyenchip.com/assets/pics/genai-platform/1-genai-platform.png" />
<meta property="twitter:title" content="Building A Generative AI Platform" />
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Chip Huyen"},"dateModified":"2024-07-25T00:00:00+00:00","datePublished":"2024-07-25T00:00:00+00:00","description":"After studying how companies deploy generative AI applications, I noticed many similarities in their platforms. This post outlines the common components of a generative AI platform, what they do, and how they are implemented. I try my best to keep the architecture general, but certain applications might deviate. This is what the overall architecture looks like.","headline":"Building A Generative AI Platform","image":"https://huyenchip.com/assets/pics/genai-platform/1-genai-platform.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://huyenchip.com/2024/07/25/genai-platform.html"},"url":"https://huyenchip.com/2024/07/25/genai-platform.html"}</script>
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
      <a href="#step_1_enhance_context">Step 1. Enhance Context</a>
<ul class="sidebar-list">
    <li><a href="#rags">RAGs</a>
        <ul>
            <li><a href="#rags_with_tabular_data">RAGs with tabular data</a></li>
            <li><a href="#agentic_rags">Agentic RAGs</a></li>
        </ul>
    </li>
    <li><a href="#query_rewriting">Query rewriting</a></li>
</ul>

<a href="#step_2_put_in_guardrails">Step 2. Put in Guardrails</a>
<ul class="sidebar-list">
    <li><a href="#input_guardrails">Input guardrails</a>
        <ul>
            <li><a href="#leaking_private_information_to_external_apis">Leaking private information to external APIs</a></li>
            <li><a href="#jailbreaking">Model jailbreaking</a></li>
        </ul>
    </li>
    <li><a href="#output_guardrails">Output guardrails</a>
        <ul>
            <li><a href="#output_quality_measurement">Output quality measurement</a></li>
            <li><a href="#failure_management">Failure management</a></li>
        </ul>
    </li>
    <li><a href="#guardrail_tradeoffs">Guardrail tradeoffs</a></li>
</ul>

<a href="#step_3_add_model_router_and_gateway">Step 3. Add Model Router and Gateway</a>
<ul class="sidebar-list">
    <li><a href="#router">Router</a></li>
    <li><a href="#gateway">Gateway</a></li>
</ul>

<a href="#step_4_reduce_latency_with_cache">Step 4. Reduce Latency with Cache</a>
<ul class="sidebar-list">
    <li><a href="#prompt_cache">Prompt cache</a></li>
    <li><a href="#exact_cache">Exact cache</a></li>
    <li><a href="#semantic_cache">Semantic cache</a></li>
</ul>

<a href="#step_5_add_complex_logic_and_write_actions">Step 5. Add Complex Logic and Write Actions</a>
<ul class="sidebar-list">
    <li><a href="#complex_logic">Complex logic</a></li>
    <li><a href="#write_actions">Write actions</a></li>
</ul>

<a href="#observability">Observability</a>
<ul class="sidebar-list">
    <li><a href="#metrics">Metrics</a></li>
    <li><a href="#logs">Logs</a></li>
    <li><a href="#traces">Traces</a></li>
</ul>

<a href="#ai_pipeline_orchestration">AI Pipeline Orchestration</a><br>
<a href="#conclusion">Conclusion</a><br>
<a href="#references_and_acknowledgments">References and Acknowledgments</a>

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
    <h1 class="post-title" itemprop="name headline">Building A Generative AI Platform</h1>
    <p class="post-meta">
      <time datetime="2024-07-25T00:00:00+00:00" itemprop="datePublished">
        
        Jul 25, 2024
      </time>
      
        • <span itemprop="author" itemscope itemtype="http://schema.org/Person"><span itemprop="name">Chip Huyen</span></span>
      </p>
  </header>

  <div class="post-content" itemprop="articleBody">
    <p>After studying how companies deploy generative AI applications, I noticed many similarities in their platforms. This post outlines the common components of a generative AI platform, what they do, and how they are implemented. I try my best to keep the architecture general, but certain applications might deviate. This is what the overall architecture looks like.</p>

<center>
    <figure>
    <img alt="Overview of a genai platform" src="/assets/pics/genai-platform/1-genai-platform.png" style="float: center; max-width: 100%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br />
This is a pretty complex system. This post will start from the simplest architecture and progressively add more components. In its simplest form, your application receives a query and sends it to the model. The model generates a response, which is returned to the user. There are no guardrails, no augmented context, and no optimization. The <strong>Model API</strong> box refers to both third-party APIs (e.g., OpenAI, Google, Anthropic) and self-hosted APIs.</p>

<center>
    <figure>
    <img alt="Overview of a genai platform" src="/assets/pics/genai-platform/2.png" style="float: center; max-width: 50%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br />
From this, you can add more components as needs arise. The order discussed in this post is common, though you don’t need to follow the exact same order. A component can be skipped if your system works well without it. Evaluation is necessary at every step of the development process.</p>

<ol>
  <li>Enhance context input into a model by giving the model access to external data sources and tools for information gathering.</li>
  <li>Put in guardrails to protect your system and your users.</li>
  <li>Add model router and gateway to support complex pipelines and add more security.</li>
  <li>Optimize for latency and costs with cache.</li>
  <li>Add complex logic and write actions to maximize your system’s capabilities.</li>
</ol>

<p>Observability, which allows you to gain visibility into your system for monitoring and debugging, and orchestration, which involves chaining all the components together, are two essential components of the platform. We will discuss them at the end of this post.</p>

<p><strong>» What this post is not «</strong></p>

<p><em>This post focuses on the overall architecture for deploying AI applications. It discusses what components are needed and considerations when building these components. It’s not about how to build AI applications and, therefore, does NOT discuss model evaluation, application evaluation, prompt engineering, finetuning, data annotation guidelines, or chunking strategies for RAGs. All these topics are covered in my upcoming book <a href="https://oreillymedia.pxf.io/GmaeBn">AI Engineering</a>.</em></p>

<p><br /></p>

<h2 id="step_1_enhance_context">Step 1. Enhance Context</h2>

<p>The initial expansion of a platform usually involves adding mechanisms to allow the system to augment each query with the necessary information. Gathering the relevant information is called context construction.</p>

<p>Many queries require context to answer. The more relevant information there is in the context, the less the model has to rely on its internal knowledge, which can be unreliable due to its training data and training methodology. Studies have shown that having access to relevant information in the context can help the model generate more detailed responses while reducing hallucinations (<a href="https://arxiv.org/abs/2005.11401">Lewis et al.</a>, 2020).</p>

<p>For example, given the query “Will Acme’s fancy-printer-A300 print 100pps?”, the model will be able to respond better if it’s given the specifications of fancy-printer-A300. (Thanks Chetan Tekur for the example.)</p>

<p>Context construction for foundation models is equivalent to feature engineering for classical ML models. They serve the same purpose: giving the model the necessary information to process an input.</p>

<p>In-context learning, learning from the context, is a form of continual learning. It enables a model to incorporate new information continually to make decisions, preventing it from becoming outdated. For example, a model trained on last-week data won’t be able to answer questions about this week unless the new information is included in its context. By updating a model’s context with the latest information, e.g. fancy-printer-A300’s latest specifications, the model remains up-to-date and can respond to queries beyond its cut-off date.</p>

<h3 id="rags">RAGs</h3>

<p>The most well-known pattern for context construction is RAG, Retrieval-Augmented Generation. RAG consists of two components: a generator (e.g. a language model) and a retriever, which retrieves relevant information from external sources.</p>

<center>
    <figure>
    <img alt="Overview of a genai platform" src="/assets/pics/genai-platform/3-rag.png" style="float: center; max-width: 63%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br />
Retrieval isn’t unique to RAGs. It’s the backbone of search engines, recommender systems, log analytics, etc. Many retrieval algorithms developed for traditional retrieval systems can be used for RAGs.</p>

<p>External memory sources typically contain unstructured data, such as memos, contracts, news updates, etc. They can be collectively called <em>documents</em>. A document can be 10 tokens or 1 million tokens. Naively retrieving whole documents can cause your context to be arbitrarily long. RAG typically requires documents to be split into <em>manageable chunks</em>, which can be determined from the model’s maximum context length and your application’s latency requirements. To learn more about chunking and the optimal chunk size, see <a href="https://www.pinecone.io/learn/chunking-strategies/">Pinecone</a>, <a href="https://js.langchain.com/v0.1/docs/modules/data_connection/document_transformers/">Langchain</a>, <a href="https://docs.llamaindex.ai/en/stable/optimizing/production_rag/">Llamaindex</a>, and <a href="https://www.youtube.com/watch?v=8OJC21T2SL4">Greg Kamradt</a>’s tutorials.</p>

<p>Once data from external memory sources has been loaded and chunked, retrieval is performed using two main approaches.</p>

<ol>
  <li><strong>Term-based retrieval</strong> <br />
This can be as simple as keyword search. For example, given the query “transformer”, fetch all documents containing this keyword. More sophisticated algorithms include BM25 (which leverages TF-IDF) and Elasticsearch (which leverages inverted index). <br />
 <br />
Term-based retrieval is usually used for text data, but it also works for images and videos that have text metadata such as titles, tags, captions, comments, etc.
<br />
<br /></li>
  <li>
    <p><strong>Embedding-based retrieval</strong> (also known as vector search) <br />
You convert chunks of data into embedding vectors using an embedding model such as <a href="https://arxiv.org/abs/1810.04805">BERT</a>, <a href="https://github.com/UKPLab/sentence-transformers">sentence-transformers</a>, and proprietary embedding models provided by OpenAI or Google. Given a query, the data whose vectors are closest to the query embedding, as determined by the vector search algorithm, is retrieved. <br />
 <br />
Vector search is usually framed as nearest-neighbor search, using approximate nearest neighbor (ANN) algorithms such as <a href="https://arxiv.org/abs/1702.08734">FAISS</a> (Facebook AI Similarity Search), Google’s <a href="https://research.google/blog/announcing-scann-efficient-vector-similarity-search/">ScaNN</a>, Spotify’s <a href="https://github.com/spotify/annoy">ANNOY</a>, and <a href="https://github.com/nmslib/hnswlib">hnswlib</a> (<a href="https://arxiv.org/abs/1603.09320">Hierarchical Navigable Small World</a>).
  <br />
The <a href="https://ann-benchmarks.com/">ANN-benchmarks website </a>compares different ANN algorithms on multiple datasets using four main metrics, taking into account the tradeoffs between indexing and querying.</p>

    <ul>
      <li><strong>Recall</strong>: the fraction of the nearest neighbors found by the algorithm.</li>
      <li><strong>Query per second (QPS)</strong>: the number of queries the algorithm can handle per second. This is crucial for high-traffic applications.</li>
      <li><strong>Build time</strong>: the time required to build the index. This metric is important especially if you need to frequently update your index (e.g. because your data changes).</li>
      <li><strong>Index size</strong>: the size of the index created by the algorithm, which is crucial for assessing its scalability and storage requirements.</li>
    </ul>
  </li>
</ol>

<p>This works with not just text documents, but also images, videos, audio, and code. Many teams even try to summarize SQL tables and dataframes and then use these summaries to generate embeddings for retrieval.</p>

<p>Term-based retrieval is much faster and cheaper than embedding-based retrieval. It can work well out of the box, making it an attractive option to start. Both BM25 and Elasticsearch are widely used in the industry and serve as formidable baselines for more complex retrieval systems. Embedding-based retrieval, while computationally expensive, can be significantly improved over time to outperform term-based retrieval.</p>

<p>A production retrieval system typically combines several approaches. Combining term-based retrieval and embedding-based retrieval is called <em>hybrid search</em>.</p>

<p>One common pattern is sequential. First, a cheap, less precise retriever, such as a term-based system, fetches candidates. Then, a more precise but more expensive mechanism, such as k-nearest neighbors, finds the best of these candidates. The second step is also called reranking.</p>

<p>For example, given the term “transformer”, you can fetch all documents that contain the word transformer, regardless of whether they are about the electric device, the neural architecture, or the movie. Then you use vector search to find among these documents those that are actually related to your transformer query.</p>

<p>Context reranking differs from traditional search reranking in that the exact position of items is less critical. In search, the rank (e.g., first or fifth) is crucial. In context reranking, the order of documents still matters because it affects how well a model can process them. Models might better understand documents at the beginning and end of the context, as suggested by the paper <a href="https://arxiv.org/abs/2307.03172">Lost in the middle</a> (Liu et al., 2023). However, as long as a document is included, the impact of its order is less significant compared to in search ranking.</p>

<p>Another pattern is ensemble. Remember that a retriever works by ranking documents by their relevance scores to the query. You use multiple retrievers to fetch candidates at the same time, then combine these different rankings together to generate a final ranking.</p>

<h4 id="rags_with_tabular_data">RAGs with tabular data</h4>

<p>External data sources can also be structured, such as dataframes or SQL tables. Retrieving data from an SQL table is significantly different from retrieving data from unstructured documents. Given a query, the system works as follows.</p>

<ol>
  <li><strong>Text-to-SQL</strong>: Based on the user query and the table schemas, determine what SQL query is needed.</li>
  <li><strong>SQL execution</strong>: Execute the SQL query.</li>
  <li><strong>Generation</strong>: Generate a response based on the SQL result and the original user query.</li>
</ol>

<center>
    <figure>
    <img alt="Overview of a genai platform" src="/assets/pics/genai-platform/4-rag-with-tabular-data.png" style="float: center; max-width: 63%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br />
For the text-to-SQL step, if there are many available tables whose schemas can’t all fit into the model context, you might need an intermediate step to predict what tables to use for each query. Text-to-SQL can be done by the same model used to generate the final response or one of many specialized text-to-SQL models.</p>

<h4 id="agentic_rags">Agentic RAGs</h4>

<p>An important source of data is the Internet. A web search tool like Google or Bing API can give the model access to a rich, up-to-date resource to gather relevant information for each query. For example, given the query “Who won Oscar this year?”, the system searches for information about the latest Oscar and uses this information to generate the final response to the user.</p>

<p>Term-based retrieval, embedding-based retrieval, SQL execution, and web search are actions that a model can take to augment its context. You can think of each action as a function the model can call. A workflow that can incorporate external actions is also called <em>agentic</em>. The architecture then looks like this.</p>

<center>
    <figure>
    <img alt="Overview of a genai platform" src="/assets/pics/genai-platform/5-agentic-rag.png" style="float: center; max-width: 90%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p><strong>» Action vs. tool «</strong></p>

<p>A tool allows one or more actions. For example, a people search tool might allow two actions: search by name and search by email. However, the difference is minimal, so many people use <em>action</em> and <em>tool</em> interchangeably.</p>

<p><strong>» Read-only actions vs. write actions «</strong></p>

<p>Actions that retrieve information from external sources but don’t change their states are read-only actions. Giving a model write actions, e.g. updating the values in a table, enables the model to perform more tasks but also poses more risks, which will be discussed later.</p>

<h3 id="query_rewriting">Query rewriting</h3>

<p>Often, a user query needs to be rewritten to increase the likelihood of fetching the right information. Consider the following conversation.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>User: When was the last time John Doe bought something from us?
AI: John last bought a Fruity Fedora hat from us two weeks ago, on January 3, 2030.
User: How about Emily Doe?
</code></pre></div></div>

<p>The last question, “How about Emily Doe?”, is ambiguous. If you use this query verbatim to retrieve documents, you’ll likely get irrelevant results. You need to rewrite this query to reflect what the user is actually asking. The new query should make sense on its own. The last question should be rewritten to “When was the last time Emily Doe bought something from us?”</p>

<p>Query rewriting is typically done using other AI models, using a prompt similar to “Given the following conversation, rewrite the last user input to reflect what the user is actually asking.”</p>

<center>
    <figure>
    <img alt="Overview of a genai platform" src="/assets/pics/genai-platform/6-query-rewriting.png" style="float: center; max-width: 70%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>Query rewriting can get complicated, especially if you need to do identity resolution or incorporate other knowledge. If the user asks “How about his wife?”, you will first need to query your database to find out who his wife is. If you don’t have this information, the rewriting model should acknowledge that this query isn’t solvable instead of hallucinating a name, leading to a wrong answer.</p>

<h2 id="step_2_put_in_guardrails">Step 2. Put in Guardrails</h2>

<p>Guardrails help reduce AI risks and protect not just your users but also you, the developers. They should be placed whenever there is potential for failures. This post discusses two types of guardrails: input guardrails and output guardrails.</p>

<h3 id="input_guardrails">Input guardrails</h3>

<p>Input guardrails are typically protection against two types of risks: leaking private information to external APIs, and executing bad prompts that compromise your system (model jailbreaking).</p>

<h4 id="leaking_private_information_to_external_apis">Leaking private information to external APIs</h4>

<p>This risk is specific to using external model APIs when you need to send your data outside your organization. For example, an employee might copy the company’s secret or a user’s private information into a prompt and send it to wherever the model is hosted. <br />
 <br />
One of the most notable early incidents was when Samsung employees put Samsung’s proprietary information into ChatGPT, accidentally <a href="https://www.techradar.com/news/samsung-workers-leaked-company-secrets-by-using-chatgpt">leaking the company’s secrets</a>. It’s unclear how Samsung discovered this leak and how the leaked information was used against Samsung. However, the incident was serious enough for Samsung to <a href="https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak">ban ChatGPT in May 2023</a>. <br />
 <br />
There’s no airtight way to eliminate potential leaks when using third-party APIs. However, you can mitigate them with guardrails. You can use one of the many available tools that automatically detect sensitive data. What sensitive data to detect is specified by you. Common sensitive data classes are:</p>

<ul>
  <li>Personal information (ID numbers, phone numbers, bank accounts).</li>
  <li>Human faces.</li>
  <li>Specific keywords and phrases associated with the company’s intellectual properties or privileged information.</li>
</ul>

<p>Many sensitive data detection tools use AI to identify potentially sensitive information, such as determining if a string resembles a valid home address. If a query is found to contain sensitive information, you have two options: block the entire query or remove the sensitive information from it. For instance, you can mask a user’s phone number with the placeholder [PHONE NUMBER]. If the generated response contains this placeholder, use a PII reversible dictionary that maps this placeholder to the original information so that you can unmask it, as shown below.</p>

<center>
    <figure>
    <img alt="Overview of a genai platform" src="/assets/pics/genai-platform/7-reversible-pii-mapping.png" style="float: center; max-width: 100%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>
<h4 id="jailbreaking">Model jailbreaking</h4>

<p>It’s become an online sport to try to jailbreak AI models, getting them to say or do bad things. While some might find it amusing to get ChatGPT to make controversial statements, it’s much less fun if your customer support chatbot, branded with your name and logo, does the same thing. This can be especially dangerous for AI systems that have access to tools. Imagine if a user finds a way to get your system to execute an SQL query that corrupts your data. <br />
 <br />
To combat this, you should first put guardrails on your system so that no harmful actions can be automatically executed. For example, no SQL queries that can insert, delete, or update data can be executed without human approval. The downside of this added security is that it can slow down your system.</p>

<p>To prevent your application from making outrageous statements it shouldn’t be making, you can define out-of-scope topics for your application. For example, if your application is a customer support chatbot, it shouldn’t answer political or social questions. A simple way to do so is to filter out inputs that contain predefined phrases typically associated with controversial topics, such as “immigration” or “antivax”. More sophisticated algorithms use AI to classify whether an input is about one of the pre-defined restricted topics. <br />
 <br />
If harmful prompts are rare in your system, you can use an anomaly detection algorithm to identify unusual prompts.</p>

<h3 id="output_guardrails">Output guardrails</h3>

<p>AI models are probabilistic, making their outputs unreliable. You can put in guardrails to significantly improve your application’s reliability. Output guardrails have two main functionalities:</p>

<ol>
  <li>Evaluate the quality of each generation.</li>
  <li>Specify the policy to deal with different failure modes.</li>
</ol>

<h4 id="output_quality_measurement">Output quality measurement</h4>

<p>To catch outputs that fail to meet your standards, you need to understand what failures look like. Here are examples of failure modes and how to catch them.</p>

<ol>
  <li>
    <p><strong>Empty responses</strong>.</p>
  </li>
  <li>
    <p><strong>Malformatted responses</strong> that don’t follow the expected output format. For example, if the application expects JSON and the generated response has a missing closing bracket. There are validators for certain formats, such as regex, JSON, and Python code validators. There are also tools for <a href="https://huyenchip.com/2024/01/16/sampling.html#constraint_sampling">constrained sampling</a> such as guidance, outlines, and instructor.</p>
  </li>
  <li>
    <p><strong>Toxic responses</strong>, such as those that are racist or sexist. These responses can be caught using one of many toxicity detection tools.</p>
  </li>
  <li>
    <p><strong>Factual inconsistent responses</strong> hallucinated by the model. Hallucination detection is an active area of research with solutions such as <a href="https://arxiv.org/abs/2303.08896">SelfCheckGPT</a> (Manakul et al., 2023) and <a href="https://arxiv.org/abs/2403.18802">SAFE</a>, Search Engine Factuality Evaluator (Wei et al., 2024). You can mitigate hallucinations by providing models with sufficient context and prompting techniques such as chain-of-thought. Hallucination detection and mitigation are discussed further in my upcoming book <a href="https://learning.oreilly.com/library/view/ai-engineering/9781098166298/">AI Engineering</a>.</p>
  </li>
  <li><strong>Responses that contain sensitive information</strong>. This can happen in two scenarios.
    <ol>
      <li>Your model was trained on sensitive data and regurgitates it back.</li>
      <li>Your system retrieves sensitive information from your internal database to enrich its context, and then it passes this sensitive information on to the response.</li>
    </ol>

    <p>This failure mode can be prevented by not training your model on sensitive data and not allowing it to retrieve sensitive data in the first place. Sensitive data in outputs can be detected using the same tools used for input guardrails.</p>
  </li>
  <li>
    <p><strong>Brand-risk responses</strong>, such as responses that mischaracterize your company or your competitors. An example is when Grok, a model trained by X, generated a response <a href="https://x.com/JaxWinterbourne/status/1733339886155968714">suggesting that Grok was trained by OpenAI</a>, causing the Internet to suspect X of stealing OpenAI’s data. This failure mode can be mitigated with keyword monitoring. Once you’ve identified outputs concerning your brands and competitors, you can either block these outputs, pass them onto human reviewers, or use other models to detect the sentiment of these outputs to ensure that only the right sentiments are returned.</p>
  </li>
  <li><strong>Generally bad responses</strong>. For example, if you ask the model to write an essay and that essay is just bad, or if you ask the model for a low-calorie cake recipe and the generated recipe contains an excessive amount of sugar. It’s become a popular practice to use AI judges to evaluate the quality of models’ responses. These AI judges can be general-purpose models (think ChatGPT, Claude) or specialized scorers trained to output a concrete score for a response given a query.</li>
</ol>

<h4 id="failure_management">Failure management</h4>

<p>AI models are probabilistic, which means that if you try a query again, you might get a different response. Many failures can be mitigated using a basic retry logic. For example, if the response is empty, try again X times or until you get a non-empty response. Similarly, if the response is malformatted, try again until the model generates a correctly formatted response.</p>

<p>This retry policy, however, can incur extra latency and cost. One retry means 2x the number of API calls. If the retry is carried out after failure, the latency experienced by the user will double. To reduce latency, you can make calls in parallel. For example, for each query, instead of waiting for the first query to fail before retrying, you send this query to the model twice at the same time, get back two responses, and pick the better one. This increases the number of redundant API calls but keeps latency manageable.</p>

<p>It’s also common to fall back on humans to handle tricky queries. For example, you can transfer a query to human operators if it contains specific key phrases. Some teams use a specialized model, potentially trained in-house, to decide when to transfer a conversation to humans. One team, for instance, transfers a conversation to human operators when their sentiment analysis model detects that the user is getting angry. Another team transfers a conversation after a certain number of turns to prevent users from getting stuck in an infinite loop.</p>

<h3 id="guardrail_tradeoffs">Guardrail tradeoffs</h3>

<p><strong>Reliability vs. latency tradeoff</strong>: While acknowledging the importance of guardrails, some teams told me that latency is more important. They decided not to implement guardrails because they can significantly increase their application’s latency. However, these teams are in the minority. Most teams find that the increased risks are more costly than the added latency.</p>

<p>Output guardrails might not work well in the stream completion mode. By default, the whole response is generated before shown to the user, which can take a long time. In the stream completion mode, new tokens are streamed to the user as they are generated, reducing the time the user has to wait to see the response. The downside is that it’s hard to evaluate partial responses, so unsafe responses might be streamed to users before the system guardrails can determine that they should be blocked.</p>

<p><strong>Self-hosted vs. third-party API tradeoff</strong>: Self-hosting your models means that you don’t have to send your data to a third party, reducing the need for input guardrails. However, it also means that you must implement all the necessary guardrails yourself, rather than relying on the guardrails provided by third-party services.</p>

<p>Our platform now looks like this. Guardrails can be independent tools or parts of model gateways, as discussed later. Scorers, if used, are grouped under model APIs since scorers are typically AI models, too. Models used for scoring are typically smaller and faster than models used for generation.</p>

<center>
    <figure>
    <img alt="Overview of a genai platform" src="/assets/pics/genai-platform/8-guardrails.png" style="float: center; max-width: 100%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<h2 id="step_3_add_model_router_and_gateway">Step 3. Add Model Router and Gateway</h2>

<p>As applications grow in complexity and involve more models, two types of tools emerged to help you work with multiple models: routers and gateways.</p>

<h3 id="router">Router</h3>
<p>An application can use different models to respond to different types of queries. Having different solutions for different queries has several benefits. First, this allows you to have specialized solutions, such as one model specialized in technical troubleshooting and another specialized in subscriptions. Specialized models can potentially perform better than a general-purpose model. Second, this can help you save costs. Instead of routing all queries to an expensive model, you can route simpler queries to cheaper models.</p>

<p>A router typically consists of <strong>an intent classifier</strong> that predicts what the user is trying to do. Based on the predicted intent, the query is routed to the appropriate solution. For example, for a customer support chatbot, if the intent is:</p>
<ul>
  <li>To reset a password –&gt; route this user to the page about password resetting.</li>
  <li>To correct a billing mistake –&gt; route this user to a human operator.</li>
  <li>To troubleshoot a technical issue –&gt; route this query to a model finetuned for troubleshooting.</li>
</ul>

<p>An intent classifier can also help your system avoid out-of-scope conversations. For example, you can have an intent classifier that predicts whether a query is out of the scope. If the query is deemed inappropriate (e.g. if the user asks who you would vote for in the upcoming election), the chatbot can politely decline to engage using one of the stock responses (“As a chatbot, I don’t have the ability to vote. If you have questions about our products, I’d be happy to help.”) without wasting an API call.</p>

<p>If your system has access to multiple actions, a router can involve a <strong>next-action predictor</strong> to help the system decide what action to take next. One valid action is to ask for clarification if the query is ambiguous. For example, in response to the query “Freezing,” the system might ask, “Do you want to freeze your account or are you talking about the weather?” or simply say, “I’m sorry. Can you elaborate?”</p>

<p>Intent classifiers and next-action predictors can be general-purpose models or specialized classification models. Specialized classification models are typically much smaller and faster than general-purpose models, allowing your system to use multiple of them without incurring significant extra latency and cost.</p>

<p>When routing queries to models with varying context limits, the query’s context might need to be adjusted accordingly. Consider a query of 1,000 tokens that is slated for a model with a 4K context limit. The system then takes an action, e.g. web search, that brings back 8,000-token context. You can either truncate the query’s context to fit the originally intended model or route the query to a model with a larger context limit.</p>

<h3 id="gateway">Gateway</h3>
<p>A model gateway is an intermediate layer that allows your organization to interface with different models in a unified and secure manner. The most basic functionality of a model gateway is to enable developers to access different models – be it self-hosted models or models behind commercial APIs such as OpenAI or Google – the same way. A model gateway makes it easier to maintain your code. If a model API changes, you only need to update the model gateway instead of having to update all applications that use this model API.</p>

<center>
    <figure>
    <img alt="Overview of a genai platform" src="/assets/pics/genai-platform/9-llm-gateway.png" style="float: center; max-width: 80%; margin: 0 0 0em 0em" />
    </figure>
</center>
<p><br /></p>

<p>In its simplest form, a model gateway is a unified wrapper that looks like the following code example. This example is to give you an idea of how a model gateway might be implemented. It’s not meant to be functional as it doesn’t contain any error checking or optimization.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>import google.generativeai as genai
import openai

def openai_model(input_data, model_name, max_tokens):
    openai.api_key = os.environ["OPENAI_API_KEY"]
    response = openai.Completion.create(
        engine=model_name,
        prompt=input_data,
        max_tokens=max_tokens
    )
    return {"response": response.choices[0].text.strip()}

def gemini_model(input_data, model_name, max_tokens):
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel(model_name=model_name)
    response = model.generate_content(input_data, max_tokens=max_tokens)
    return {"response": response["choices"][0]["message"]["content"]}

@app.route('/model', methods=['POST'])
def model_gateway():
    data = request.get_json()
    model_type = data.get("model_type")
    model_name = data.get("model_name")
    input_data = data.get("input_data")
    max_tokens = data.get("max_tokens")

    if model_type == "openai":
        result = openai_model(input_data, model_name, max_tokens)
    elif model_type == "gemini":
        result = gemini_model(input_data, model_name, max_tokens)
    return jsonify(result)
</code></pre></div></div>

<p>A model gateway is <strong>access control and cost management</strong>. Instead of giving everyone who wants access to the OpenAI API your organizational tokens, which can be easily leaked, you only give people access to the model gateway, creating a centralized and controlled point of access. The gateway can also implement fine-grained access controls, specifying which user or application should have access to which model. Moreover, the gateway can monitor and limit the usage of API calls, preventing abuse and managing costs effectively.</p>

<p>A model gateway can also be used to implement fallback policies to overcome rate limits or API failures (the latter is unfortunately common). When the primary API is unavailable, the gateway can route requests to alternative models, retry after a short wait, or handle failures in other graceful manners. This ensures that your application can operate smoothly without interruptions.</p>

<p>Since requests and responses are already flowing through the gateway, it’s a good place to implement other functionalities such as load balancing, logging, and analytics. Some gateway services even provide caching and guardrails.</p>

<p>Given that gateways are relatively straightforward to implement, there are many off-the-shelf gateways. Examples include Portkey’s <a href="https://github.com/Portkey-AI/gateway">gateway</a>, <a href="https://mlflow.org/docs/latest/llms/gateway/index.html">MLflow AI Gateway</a>, WealthSimple’s <a href="https://github.com/wealthsimple/llm-gateway">llm-gateway</a>, <a href="https://docs.truefoundry.com/docs/ai-gateway">TrueFoundry</a>, <a href="https://konghq.com/products/kong-ai-gateway