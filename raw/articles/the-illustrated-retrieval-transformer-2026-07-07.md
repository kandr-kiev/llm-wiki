---

source_url: http://jalammar.github.io/illustrated-retrieval-transformer/
ingested: 2026-07-07
sha256: 795ddf42fa1ef3bb311288199b4bafeefab7a8fefd340689d81d0af88203a73f
blog_source: Jay Alammar
---

<!DOCTYPE html>
<html>
  <head>
    <title>The Illustrated Retrieval Transformer – Jay Alammar – Visualizing machine learning one concept at a time.</title>

        <meta charset="utf-8" />
    <meta content='text/html; charset=utf-8' http-equiv='Content-Type'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0'>

    
    <meta name="description" content="Discussion: Discussion Thread for comments, corrections, or any feedback. 

Translations:  Korean, Russian


Summary: The latest batch of language models can be much smaller yet achieve GPT-3 like performance by being able to query a database or search the web for information. A key indication is that building larger and larger models is not the only way to improve performance.

Video




The last few years saw the rise of Large Language Models (LLMs) – machine learning models that rapidly improve how machines process and generate language. Some of the highlights since 2017 include:


  The original Transformer breaks previous performance records for machine translation.
  BERT popularizes the pre-training then finetuning process, as well as Transformer-based contextualized word embeddings. It then rapidly starts to power Google Search and Bing Search.
  GPT-2 demonstrates the machine’s ability to write as well as humans do.
  First T5, then T0 push the boundaries of transfer learning (training a model on one task, and then having it do well on other adjacent tasks) and posing a lot of different tasks as text-to-text tasks.
  GPT-3 showed that massive scaling of generative models can lead to shocking emergent applications (the industry continues to train larger models like Gopher, MT-NLG…etc).


For a while, it seemed like scaling larger and larger models is the main way to improve performance. Recent developments in the field, like DeepMind’s RETRO Transformer and OpenAI’s WebGPT, reverse this trend by showing that smaller generative language models can perform on par with massive models if we augment them with a way to search/query for information.

This article breaks down DeepMind’s RETRO (Retrieval-Enhanced TRansfOrmer) and how it works. The model performs on par with GPT-3 despite being 4% its size (7.5 billion parameters vs. 185 billion for GPT-3 Da Vinci).


  
  
  RETRO incorporates information retrieved from a database to free its parameters from being an expensive store of facts and world knowledge.


RETRO was presented in the paper Improving Language Models by Retrieving from Trillions of Tokens. It continues and builds on a wide variety of retrieval work in the research community. This article explains the model and not what is especially novel about it.

" />
    <meta property="og:description" content="Discussion: Discussion Thread for comments, corrections, or any feedback. 

Translations:  Korean, Russian


Summary: The latest batch of language models can be much smaller yet achieve GPT-3 like performance by being able to query a database or search the web for information. A key indication is that building larger and larger models is not the only way to improve performance.

Video




The last few years saw the rise of Large Language Models (LLMs) – machine learning models that rapidly improve how machines process and generate language. Some of the highlights since 2017 include:


  The original Transformer breaks previous performance records for machine translation.
  BERT popularizes the pre-training then finetuning process, as well as Transformer-based contextualized word embeddings. It then rapidly starts to power Google Search and Bing Search.
  GPT-2 demonstrates the machine’s ability to write as well as humans do.
  First T5, then T0 push the boundaries of transfer learning (training a model on one task, and then having it do well on other adjacent tasks) and posing a lot of different tasks as text-to-text tasks.
  GPT-3 showed that massive scaling of generative models can lead to shocking emergent applications (the industry continues to train larger models like Gopher, MT-NLG…etc).


For a while, it seemed like scaling larger and larger models is the main way to improve performance. Recent developments in the field, like DeepMind’s RETRO Transformer and OpenAI’s WebGPT, reverse this trend by showing that smaller generative language models can perform on par with massive models if we augment them with a way to search/query for information.

This article breaks down DeepMind’s RETRO (Retrieval-Enhanced TRansfOrmer) and how it works. The model performs on par with GPT-3 despite being 4% its size (7.5 billion parameters vs. 185 billion for GPT-3 Da Vinci).


  
  
  RETRO incorporates information retrieved from a database to free its parameters from being an expensive store of facts and world knowledge.


RETRO was presented in the paper Improving Language Models by Retrieving from Trillions of Tokens. It continues and builds on a wide variety of retrieval work in the research community. This article explains the model and not what is especially novel about it.

" />
    
    <meta name="author" content="Jay Alammar" />

    
    <meta property="og:title" content="The Illustrated Retrieval Transformer" />
    <meta property="twitter:title" content="The Illustrated Retrieval Transformer" />
    

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
  <h1>The Illustrated Retrieval Transformer</h1>

  <div class="entry prediction">
    <p><span class="discussion">Discussion: <a href="https://github.com/jalammar/jalammar.github.io/discussions/21">Discussion Thread</a> for comments, corrections, or any feedback. </span>
<br />
<span class="discussion">Translations:  <a href="https://chloamme.github.io/2022/01/08/illustrated-retrieval-transformer-korean.html">Korean</a>, <a href="https://habr.com/ru/post/648705/">Russian</a>
<br /></span></p>

<p><strong>Summary</strong>: The latest batch of language models can be much smaller yet achieve GPT-3 like performance by being able to query a database or search the web for information. A key indication is that building larger and larger models is not the only way to improve performance.</p>

<h2 id="video">Video</h2>
<iframe width="560" height="315" src="https://www.youtube.com/embed/sMPq4cVS4kg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" style="
width: 100%;
max-width: 560px;" allowfullscreen=""></iframe>

<hr />

<p>The last few years saw the rise of Large Language Models (LLMs) – machine learning models that rapidly improve how machines process and generate language. Some of the highlights since 2017 include:</p>

<ul>
  <li>The original <a href="/illustrated-transformer/">Transformer</a> breaks previous performance records for machine translation.</li>
  <li><a href="/illustrated-bert/">BERT</a> popularizes the pre-training then finetuning process, as well as Transformer-based contextualized word embeddings. It then rapidly starts to power <a href="https://blog.google/products/search/search-language-understanding-bert/">Google Search</a> and <a href="https://azure.microsoft.com/en-us/blog/bing-delivers-its-largest-improvement-in-search-experience-using-azure-gpus/">Bing Search</a>.</li>
  <li><a href="/illustrated-gpt2/">GPT-2</a> demonstrates the machine’s ability to write as well as humans do.</li>
  <li>First <a href="https://arxiv.org/abs/1910.10683">T5</a>, then <a href="https://huggingface.co/bigscience/T0pp">T0</a> push the boundaries of transfer learning (training a model on one task, and then having it do well on other adjacent tasks) and posing a lot of different tasks as text-to-text tasks.</li>
  <li><a href="/how-gpt3-works-visualizations-animations/">GPT-3</a> showed that massive scaling of generative models can lead to shocking emergent applications (the industry continues to train larger models like <a href="https://deepmind.com/research/publications/2021/scaling-language-models-methods-analysis-insights-from-training-gopher">Gopher</a>, <a href="https://www.microsoft.com/en-us/research/blog/using-deepspeed-and-megatron-to-train-megatron-turing-nlg-530b-the-worlds-largest-and-most-powerful-generative-language-model/">MT-NLG</a>…etc).</li>
</ul>

<p>For a while, it seemed like scaling larger and larger models is the main way to improve performance. Recent developments in the field, like DeepMind’s <a href="https://deepmind.com/research/publications/2021/improving-language-models-by-retrieving-from-trillions-of-tokens">RETRO Transformer</a> and OpenAI’s <a href="https://openai.com/blog/improving-factual-accuracy/">WebGPT</a>, reverse this trend by showing that smaller generative language models can perform on par with massive models if we augment them with a way to search/query for information.</p>

<p>This article breaks down DeepMind’s RETRO (<strong>R</strong>etrieval-<strong>E</strong>nhanced <strong>TR</strong>ansf<strong>O</strong>rmer) and how it works. The model performs on par with GPT-3 despite being 4% its size (7.5 billion parameters vs. 185 billion for GPT-3 Da Vinci).</p>

<div class="img-div">
  <img src="/images/retro/deepmind-retro-retrieval-transformer.png" />
  <br />
  RETRO incorporates information retrieved from a database to free its parameters from being an expensive store of facts and world knowledge.
</div>

<p>RETRO was presented in the paper <a href="https://arxiv.org/abs/2112.04426">Improving Language Models by Retrieving from Trillions of Tokens</a>. It continues and builds on a wide variety of retrieval <a href="http://www.crm.umontreal.ca/2018/Langue18/pdf/Cheung.pdf">work</a> <a href="https://ai.facebook.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/">in</a> <a href="https://openreview.net/forum?id=HklBjCEKvH">the</a> <a href="https://arxiv.org/abs/2102.02557">research</a> <a href="https://openreview.net/forum?id=B184E5qee">community</a>. This article explains the model and not what is especially novel about it.</p>

<!--more-->

<h2 id="why-this-is-important-separating-language-information-from-world-knowledge-information">Why This is Important: Separating Language Information from World Knowledge Information</h2>

<p>Language modeling trains models to predict the next word–to fill-in-the-blank at the end of the sentence, essentially.</p>

<p>Filling the blank sometimes requires knowledge of factual information (e.g. names or dates). For example:</p>

<div class="img-div">
  <img src="/images/retro/prompt-1.png" />
  <br />
  Input prompt: The Dune film was released in ....
</div>

<p>Other times, familiarity with the language is enough to guess what goes in the blank. For example:</p>

<div class="img-div">
  <img src="/images/retro/prompt-2.png" />
  <br />
  Input prompt: its popularity spread by word-of-mouth to allow Herbert to start working full ....
</div>

<p>This distinction is important because LLMs encoded everything they know in their model parameters. While this makes sense for language information, it is inefficient for factual and world-knowledge information.</p>

<p>By including a retrieval method in the language model, the model can be much smaller. A neural database aids it with retrieving factual information it needs during text generation.</p>

<div class="img-div-any-width">
  <img src="/images/retro/Large-GPT-vs-Retro-transformer-world-knowledge-information.png" />
  <br />
  Aiding language models with retrieval methods allows us to reduce the amount of information a language model needs to encode in its parameters to perform well at text generation.
</div>

<p>Training becomes fast with small language models, as training data memorization is reduced. Anyone can deploy these models on smaller and more affordable GPUs and tweak them as per need.</p>

<p>Mechanically, RETRO is an encoder-decoder model just like the original transformer. However, it augments the input sequence with the help of a retrieval database. The model finds the most probable sequences in the database and adds them to the input. RETRO works its magic to generate the output prediction.</p>

<div class="img-div">
  <img src="/images/retro/dune-prompt-into-retro-transformer-4.png" />
  <br />
  RETRO utilizes a database to augment its input prompt. The prompt is used to retrieve relevant information from the database.
</div>

<p>Before we explore the model architecture, let’s dig deeper into the retrieval database.</p>

<h2 id="inspecting-retros-retrieval-database">Inspecting RETRO’s Retrieval Database</h2>

<p>The database is a key-value store.</p>

<p>The key is a standard BERT sentence embedding.</p>

<p>The value is text in two parts:</p>

<ol>
  <li>
    <p>Neighbor, which is used to compute the key</p>
  </li>
  <li>
    <p>Completion, the continuation of the text in the original document.</p>
  </li>
</ol>

<p>RETRO’s database contains 2 trillion multi-lingual tokens based on the <em>MassiveText</em> dataset. Both the neighbor and completion chunks are at most 64 tokens long.</p>

<div class="img-div-any-width">
  <img src="/images/retro/database-key-value-examples.png" />
  <br />
  A look inside RETRO's database shows examples of key-value pairs in the RETRO database. The value contains a neighbor chunk and a completion chunk.
</div>

<p>RETRO breaks the input prompt into multiple chunks. For simplicity, we’ll focus on how one chunk is augmented with retrieved text. The model, however, does this process for each chunk (except the first) in the input prompt.</p>

<h2 id="the-database-lookup">The Database Lookup</h2>

<p>Before hitting RETRO, the input prompt goes into BERT. The output contextualized vectors are then averaged to construct a sentence embedding vector. That vector is then used to query the database.</p>

<div class="img-div-any-width">
  <img src="/images/retro/bert-sentence-embedding.png" />
  <br />
  Processing the input prompt with BERT produces contextualized token embeddings. Averaging them produces a sentence embedding.
</div>

<p>That sentence embedding is then used in an approximate nearest neighbor search (<a href="https://github.com/google-research/google-research/tree/master/scann">https://github.com/google-research/google-research/tree/master/scann</a>).</p>

<p>The two nearest neighbors are retrieved, and their text becomes a part of the input into RETRO.</p>

<div class="img-div">
  <img src="/images/retro/neighbor-retrieval-from-retro-neural-database-with-bert-embeddings.png" />
  <br />
  The BERT sentence embedding is used to retrieve the nearest neighbors from RETRO's neural database. These are then added to the input of the language model.
</div>

<p>This is now the input to RETRO. The input prompt and its two nearest neighbors from the database (and their continuations).</p>

<p>From here, the Transformer and RETRO Blocks incorporate the information into their processing.</p>

<div class="img-div">
  <img src="/images/retro/input-prompt-and-retrieved-text-retro-transformer.png" />
  <br />
  The retrieved neighbors are added to the input of the language model. They're treated a little differently inside the model, however.
</div>

<h2 id="retro-architecture-at-a-high-level">RETRO Architecture at a High Level</h2>

<p>RETRO’s architecture is an encoder stack and a decoder stack.</p>

<div class="img-div">
  <img src="/images/retro/Retro-transformer-encoder-decoder-stacks-2.png" />
  <br />
  A RETRO transformer consists of an encoder stack (to process the neighbors) and a decoder stack (to process the input)
</div>

<p>The encoder is made up of standard Transformer encoder blocks (self-attention + FFNN). To my best understanding, Retro uses an encoder made up of two Transformer Encoder Blocks.</p>

<p>The decoder stack interleaves two kinds of decoder blocks:</p>

<ul>
  <li>Standard transformer decoder block (ATTN + FFNN)</li>
  <li>RETRO decoder block (ATTN + Chunked cross attention (CCA) + FFNN)</li>
</ul>

<div class="img-div">
  <img src="/images/retro/retro-transformer-blocks-4.png" />
  <br />
  The three types of Transformer blocks that make up RETRO
</div>

<p>Let’s start by looking at the encoder stack, which processes the retrieved neighbors, resulting in KEYS and VALUES matrices that will later be used for attention (see <a href="https://jalammar.github.io/illustrated-transformer/">The Illustrated Transformer</a> for a refresher).</p>

<div class="img-div">
  <img src="/images/retro/retro-encoder-block-keys-values-2.png" />
  <br />
  The encoder stack processes the retrieved neighbors resulting in KEYS and VALUE matrices
</div>

<p>Decoder blocks process the input text just like a GPT would. It applies self-attention on the prompt token (causally, so only attending to previous tokens), then passes through a FFNN layer.</p>

<div class="img-div">
  <img src="/images/retro/retro-transformer-decoders-2.png" />
  <br />
  Input prompt passes through standard decoder block containing self-attention and FFNN layers
</div>

<p>It’s only when a RETRO decoder is reached do we start to incorporate the retrieved information. Every third block starting from 9 is a RETRO block (that allows its input to attend to the neighbors). So layers 9, 12, 15…32 are RETRO blocks. (The two smaller Retro models, and the Retrofit models have these layers starting from the 6th instead of the 9th layer).</p>

<div class="img-div">
  <img src="/images/retro/retro-decoder-attention-2.png" />
  <br />
  Input prompt reaches RETRO Decoder block to start information retrieval
</div>

<p>So effectively, this is the step where the retrieved information can glance at the dates it needs to complete the prompt.</p>

<div class="img-div">
  <img src="/images/retro/retro-decoder-chunked-cross-attention.png" />
  <br />
  RETRO Decoder block retrieving information from nearest neighbour chunks using Chunked Cross-Attention
</div>

<h2 id="previous-work">Previous Work</h2>

<p>Aiding language models with retrieval techniques has been an active area of research. Some of the previous work in the space includes:</p>

<ul>
  <li><a href="https://openreview.net/forum?id=B184E5qee">Improving Neural Language Models with a Continuous Cache</a></li>
  <li><a href="https://openreview.net/forum?id=HklBjCEKvH">Generalization through Memorization: Nearest Neighbor Language Models</a></li>
  <li>Read the <a href="https://ai.facebook.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/">Retrieval Augmented Generation</a> blog from Meta AI and go through Jackie Chi Kit Cheung’s lecture on <a href="http://www.crm.umontreal.ca/2018/Langue18/pdf/Cheung.pdf">Leveraging External Knowledge in Natural Language Understanding Systems</a></li>
  <li>SPALM: <a href="https://arxiv.org/abs/2102.02557">Adaptive Semiparametric Language Models</a></li>
  <li>DPR: <a href="https://aclanthology.org/2020.emnlp-main.550/">Dense Passage Retrieval for Open-Domain Question Answering</a></li>
  <li><a href="https://arxiv.org/abs/2002.08909">REALM: Retrieval-Augmented Language Model Pre-Training</a></li>
  <li>FiD: <a href="https://aclanthology.org/2021.eacl-main.74/">Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering</a></li>
  <li>EMDR: <a href="https://arxiv.org/abs/2106.05346">End-to-End Training of Multi-Document Reader and Retriever for Open-Domain Question Answering</a></li>
  <li>BlenderBot 2.0: <a href="https://arxiv.org/abs/2107.07566">Internet-Augmented Dialogue Generation</a></li>
</ul>

<p>Please post in <a href="https://github.com/jalammar/jalammar.github.io/discussions/21">this thread</a> or reach out to me on <a href="https://twitter.com/JayAlammar">Twitter</a> for any corrections or feedback.</p>

  </div>

  <div class="date">
    Written on January  3, 2022
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
