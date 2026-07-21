---

source_url: http://jalammar.github.io/applying-large-language-models-cohere/
ingested: 2026-07-07
sha256: 0030d8c0cd0307333d50b2ecd6e38b7e5a014029f2fcdd0034f8d1ff40eba14f
blog_source: Jay Alammar
---

<!DOCTYPE html>
<html>
  <head>
    <title>Applying massive language models in the real world with Cohere – Jay Alammar – Visualizing machine learning one concept at a time.</title>

        <meta charset="utf-8" />
    <meta content='text/html; charset=utf-8' http-equiv='Content-Type'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0'>

    
    <meta name="description" content="A little less than a year ago, I joined the awesome Cohere team. The company trains massive language models (both GPT-like and BERT-like) and offers them as an API (which also supports finetuning). Its founders include Google Brain alums including co-authors of the original Transformers paper. It’s a fascinating role where I get to help companies and developers put these massive models to work solving real-world problems.

I love that I get to share some of the intuitions developers need to start problem-solving with these models. Even though I’ve been working very closely on pretrained Transformers for the past several years (for this blog and in developing Ecco), I’m enjoying the convenience of problem-solving with managed language models as it frees up the restrictions of model loading/deployment and memory/GPU management.

These are some of the articles I wrote and collaborated on with colleagues over the last few months:

Intro to Large Language Models with Cohere

    
  
    
    
    This is a high-level intro to large language models to people who are new to them. It establishes the difference between generative (GPT-like) and representation (BERT-like) models and examples use cases for them.
    This is one of the first articles I got to write. It's extracted from a much larger document that I wrote to explore some of the visual language to use in explaining the application of these models.
    


A visual guide to prompt engineering 


    
  
    
    
        Massive GPT models open the door for a new way of programming. If you structure the input text in the right way, you can useful (and often fascinating) results for a lot of taasks (e.g. text classification, copy writing, summarization...etc).
        
        This article visually demonstrates four principals to create prompts effectively. 
    


 Text Summarization


    
  
    
    
    This is a walkthrough of creating a simple summarization system. It links to a jupyter notebook which includes the code to start experimenting with text generation and summarization.
    The end of this notebook shows an important idea I want to spend more time on in the future. That of how to rank/filter/select the best from amongst multiple generations.
    


Semantic Search


    
  
    
    
    Semantic search has to be one of the most exciting applications of sentence embedding models. This tutorials implements a "similar questions" functionality using sentence embeddings and a a vector search library.
    The vector search library used here is Annoy from Spotify. There are a bunch of others out there. Faiss is used widely. I experiment with PyNNDescent as well.
    


 Finetuning Representation Models


    
  
    
    
    Finetuning tends to lead to the best results language models can achieve. This article explains the intuitions around finetuning representation/sentence embedding models. I've added a couple more visuals to the Twitter thread.
The research around this area is very interesting. I've highly enjoyed papers like Sentence BERT and Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval
    


Controlling Generation with top-k &amp; top-p


    
  
    
    
        This one is a little bit more technical. It explains the parameters you tweak to adjust a GPT's decoding strategy -- the method with which the system picks output tokens. 
        
    


Text Classification Using Embeddings


    
  
    
    
        
        This is a walkthrough of one of the most common use cases of embedding models -- text classification. It is similar to A Visual Guide to Using BERT for the First Time, but uses Cohere's API.
        
    


You can find these and upcoming articles in the Cohere docs and notebooks repo. I have quite number of experiments and interesting workflows I’d love to be sharing in the coming weeks. So stay tuned!
" />
    <meta property="og:description" content="A little less than a year ago, I joined the awesome Cohere team. The company trains massive language models (both GPT-like and BERT-like) and offers them as an API (which also supports finetuning). Its founders include Google Brain alums including co-authors of the original Transformers paper. It’s a fascinating role where I get to help companies and developers put these massive models to work solving real-world problems.

I love that I get to share some of the intuitions developers need to start problem-solving with these models. Even though I’ve been working very closely on pretrained Transformers for the past several years (for this blog and in developing Ecco), I’m enjoying the convenience of problem-solving with managed language models as it frees up the restrictions of model loading/deployment and memory/GPU management.

These are some of the articles I wrote and collaborated on with colleagues over the last few months:

Intro to Large Language Models with Cohere

    
  
    
    
    This is a high-level intro to large language models to people who are new to them. It establishes the difference between generative (GPT-like) and representation (BERT-like) models and examples use cases for them.
    This is one of the first articles I got to write. It's extracted from a much larger document that I wrote to explore some of the visual language to use in explaining the application of these models.
    


A visual guide to prompt engineering 


    
  
    
    
        Massive GPT models open the door for a new way of programming. If you structure the input text in the right way, you can useful (and often fascinating) results for a lot of taasks (e.g. text classification, copy writing, summarization...etc).
        
        This article visually demonstrates four principals to create prompts effectively. 
    


 Text Summarization


    
  
    
    
    This is a walkthrough of creating a simple summarization system. It links to a jupyter notebook which includes the code to start experimenting with text generation and summarization.
    The end of this notebook shows an important idea I want to spend more time on in the future. That of how to rank/filter/select the best from amongst multiple generations.
    


Semantic Search


    
  
    
    
    Semantic search has to be one of the most exciting applications of sentence embedding models. This tutorials implements a "similar questions" functionality using sentence embeddings and a a vector search library.
    The vector search library used here is Annoy from Spotify. There are a bunch of others out there. Faiss is used widely. I experiment with PyNNDescent as well.
    


 Finetuning Representation Models


    
  
    
    
    Finetuning tends to lead to the best results language models can achieve. This article explains the intuitions around finetuning representation/sentence embedding models. I've added a couple more visuals to the Twitter thread.
The research around this area is very interesting. I've highly enjoyed papers like Sentence BERT and Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval
    


Controlling Generation with top-k &amp; top-p


    
  
    
    
        This one is a little bit more technical. It explains the parameters you tweak to adjust a GPT's decoding strategy -- the method with which the system picks output tokens. 
        
    


Text Classification Using Embeddings


    
  
    
    
        
        This is a walkthrough of one of the most common use cases of embedding models -- text classification. It is similar to A Visual Guide to Using BERT for the First Time, but uses Cohere's API.
        
    


You can find these and upcoming articles in the Cohere docs and notebooks repo. I have quite number of experiments and interesting workflows I’d love to be sharing in the coming weeks. So stay tuned!
" />
    
    <meta name="author" content="Jay Alammar" />

    
    <meta property="og:title" content="Applying massive language models in the real world with Cohere" />
    <meta property="twitter:title" content="Applying massive language models in the real world with Cohere" />
    

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
  <h1>Applying massive language models in the real world with Cohere</h1>

  <div class="entry prediction">
    <p>A little less than a year ago, I joined the awesome <a href="https://cohere.ai">Cohere</a> team. The company trains massive language models (both GPT-like and BERT-like) and offers them as an API (which also supports finetuning). Its founders include Google Brain alums including co-authors of the original Transformers paper. It’s a fascinating role where I get to help companies and developers put these massive models to work solving real-world problems.</p>

<p>I love that I get to share some of the intuitions developers need to start problem-solving with these models. Even though I’ve been working very closely on pretrained Transformers for the past several years (for this blog and in developing <a href="https://github.com/jalammar/ecco">Ecco</a>), I’m enjoying the convenience of problem-solving with managed language models as it frees up the restrictions of model loading/deployment and memory/GPU management.</p>

<p>These are some of the articles I wrote and collaborated on with colleagues over the last few months:</p>

<h3 id="intro-to-large-language-models-with-cohere"><a href="https://docs.cohere.ai/intro-to-llms/">Intro to Large Language Models with Cohere</a></h3>
<div class="row two-column-text">
    <div class="col-md-6 col-xs-12">
  <a href="https://docs.cohere.ai/intro-to-llms/"><img src="https://files.readme.io/0a9715d-IntroToLLM_Visual_1.svg" class="small-image" /></a>
    </div>
    <div class="col-md-6 col-xs-12">
    <p>This is a high-level intro to large language models to people who are new to them. It establishes the difference between generative (GPT-like) and representation (BERT-like) models and examples use cases for them.</p>
    <p>This is one of the first articles I got to write. It's extracted from a much larger document that I wrote to explore some of the visual language to use in explaining the application of these models.</p>
    </div>
</div>

<h3 id="a-visual-guide-to-prompt-engineering-"><a href="https://docs.cohere.ai/prompt-engineering-wiki/">A visual guide to prompt engineering </a></h3>

<div class="row two-column-text">
    <div class="col-md-6 col-xs-12">
  <a href="https://docs.cohere.ai/prompt-engineering-wiki/"><img src="https://files.readme.io/db285b8-PromptEngineering_Visual_2.svg" class="small-image" /></a>
    </div>
    <div class="col-md-6 col-xs-12">
        <p>Massive GPT models open the door for a new way of programming. If you structure the input text in the right way, you can useful (and often fascinating) results for a lot of taasks (e.g. text classification, copy writing, summarization...etc).
        </p>
        <p>This article visually demonstrates four principals to create prompts effectively. </p>
    </div>
</div>

<h3 id="-text-summarization"><a href="https://docs.cohere.ai/text-summarization-example/"> Text Summarization</a></h3>

<div class="row two-column-text">
    <div class="col-md-6 col-xs-12">
  <a href="https://docs.cohere.ai/text-summarization-example/"><img src="https://files.readme.io/296454c-TextSummarization_Visual_1.svg" class="small-image" /></a>
    </div>
    <div class="col-md-6 col-xs-12">
    <p>This is a walkthrough of creating a simple summarization system. It links to a jupyter notebook which includes the code to start experimenting with text generation and summarization.</p>
    <p>The end of this notebook shows an important idea I want to spend more time on in the future. That of how to rank/filter/select the best from amongst multiple generations.</p>
    </div>
</div>

<h3 id="semantic-search"><a href="https://docs.cohere.ai/semantic-search/">Semantic Search</a></h3>

<div class="row two-column-text">
    <div class="col-md-6 col-xs-12">
  <a href="https://docs.cohere.ai/semantic-search/"><img src="https://files.readme.io/4ec00e1-SemanticSearch_Visual_1.svg" class="small-image" /></a>
    </div>
    <div class="col-md-6 col-xs-12">
    <p>Semantic search has to be one of the most exciting applications of sentence embedding models. This tutorials implements a "similar questions" functionality using sentence embeddings and a a vector search library.</p>
    <p>The vector search library used here is <a href="https://github.com/spotify/annoy">Annoy</a> from Spotify. There are a bunch of others out there. <a href="https://github.com/facebookresearch/faiss">Faiss</a> is used widely. I experiment with <a href="https://github.com/lmcinnes/pynndescent">PyNNDescent</a> as well.</p>
    </div>
</div>

<h3 id="-finetuning-representation-models"><a href="https://docs.cohere.ai/finetuning-representation-models/"> Finetuning Representation Models</a></h3>

<div class="row two-column-text">
    <div class="col-md-6 col-xs-12">
  <a href="https://docs.cohere.ai/docs/training-a-representation-model"><img src="https://files.readme.io/699aead-TrainingRepModels_Visual_4.svg" class="small-image" /></a>
    </div>
    <div class="col-md-6 col-xs-12">
    <p>Finetuning tends to lead to the best results language models can achieve. This article explains the intuitions around finetuning representation/sentence embedding models. I've added a couple more visuals to the <a href="https://twitter.com/JayAlammar/status/1490712428686024705">Twitter thread</a>.</p>
<p>The research around this area is very interesting. I've highly enjoyed papers like <a href="https://arxiv.org/abs/1908.10084">Sentence BERT</a> and <a href="https://arxiv.org/abs/2007.00808">Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval</a></p>
    </div>
</div>

<h3 id="controlling-generation-with-top-k--top-p"><a href="https://docs.cohere.ai/token-picking/">Controlling Generation with top-k &amp; top-p</a></h3>

<div class="row two-column-text">
    <div class="col-md-6 col-xs-12">
  <a href="https://docs.cohere.ai/token-picking/"><img src="https://files.readme.io/ab291f6-Top-KTop-P_Visual_4.svg" class="small-image" /></a>
    </div>
    <div class="col-md-6 col-xs-12">
        <p>This one is a little bit more technical. It explains the parameters you tweak to adjust a GPT's <i>decoding strategy</i> -- the method with which the system picks output tokens. 
        </p>
    </div>
</div>

<h3 id="text-classification-using-embeddings"><a href="https://docs.cohere.ai/text-classification-embeddings/">Text Classification Using Embeddings</a></h3>

<div class="row two-column-text">
    <div class="col-md-6 col-xs-12">
  <a href="https://docs.cohere.ai/text-classification-embeddings/"><img src="https://files.readme.io/ee56264-Controlling_Generation_with_Top-K__Top-P_Visual_1.svg" class="small-image" /></a>
    </div>
    <div class="col-md-6 col-xs-12">
        <p>
        This is a walkthrough of one of the most common use cases of embedding models -- text classification. It is similar to <a href="http://127.0.0.1:4000/a-visual-guide-to-using-bert-for-the-first-time/">A Visual Guide to Using BERT for the First Time</a>, but uses Cohere's API.
        </p>
    </div>
</div>

<p>You can find these and upcoming articles in the <a href="https://docs.cohere.ai/">Cohere docs</a> and <a href="https://github.com/cohere-ai/notebooks">notebooks repo</a>. I have quite number of experiments and interesting workflows I’d love to be sharing in the coming weeks. So stay tuned!</p>

  </div>

  <div class="date">
    Written on March  7, 2022
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
