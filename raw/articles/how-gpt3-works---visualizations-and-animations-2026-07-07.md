---

source_url: http://jalammar.github.io/how-gpt3-works-visualizations-animations/
ingested: 2026-07-07
sha256: dfa12b9b08daf67aec94a414c3d96391f88a1c4356d32cec9b76a57e97ed4c8f
blog_source: Jay Alammar
---

<!DOCTYPE html>
<html>
  <head>
    <title>How GPT3 Works - Visualizations and Animations – Jay Alammar – Visualizing machine learning one concept at a time.</title>

        <meta charset="utf-8" />
    <meta content='text/html; charset=utf-8' http-equiv='Content-Type'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0'>

    
    <meta name="description" content="Discussions:
Hacker News (397 points, 97 comments), Reddit r/MachineLearning (247 points, 27 comments)


Translations: German, Korean, Chinese (Simplified), Russian, Turkish


The tech world is abuzz with GPT3 hype. Massive language models (like GPT3) are starting to surprise us with their abilities. While not yet completely reliable for most businesses to put in front of their customers, these models are showing sparks of cleverness that are sure to accelerate the march of automation and the possibilities of intelligent computer systems. Let’s remove the aura of mystery around GPT3 and learn how it’s trained and how it works.





A trained language model generates text.

We can optionally pass it some text as input, which influences its output.

The output is generated from what the model “learned” during its training period where it scanned vast amounts of text.


  
  



" />
    <meta property="og:description" content="Discussions:
Hacker News (397 points, 97 comments), Reddit r/MachineLearning (247 points, 27 comments)


Translations: German, Korean, Chinese (Simplified), Russian, Turkish


The tech world is abuzz with GPT3 hype. Massive language models (like GPT3) are starting to surprise us with their abilities. While not yet completely reliable for most businesses to put in front of their customers, these models are showing sparks of cleverness that are sure to accelerate the march of automation and the possibilities of intelligent computer systems. Let’s remove the aura of mystery around GPT3 and learn how it’s trained and how it works.





A trained language model generates text.

We can optionally pass it some text as input, which influences its output.

The output is generated from what the model “learned” during its training period where it scanned vast amounts of text.


  
  



" />
    
    <meta name="author" content="Jay Alammar" />

    
    <meta property="og:title" content="How GPT3 Works - Visualizations and Animations" />
    <meta property="twitter:title" content="How GPT3 Works - Visualizations and Animations" />
    

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
  <h1>How GPT3 Works - Visualizations and Animations</h1>

  <div class="entry prediction">
    <p><span class="discussion">Discussions:
<a href="https://news.ycombinator.com/item?id=23967887" class="hn-link">Hacker News (397 points, 97 comments)</a>, <a href="https://www.reddit.com/r/MachineLearning/comments/hwxn26/p_how_gpt3_works_visuals_and_animations/" class="">Reddit r/MachineLearning (247 points, 27 comments)</a>
</span>
<br />
<span class="discussion">Translations: <a href="https://www.arnevogel.com/wie-gpt3-funktioniert/">German</a>, <a href="https://chloamme.github.io/2021/12/18/how-gpt3-works-visualizations-animations-korean.html">Korean</a>, <a href="https://blogcn.acacess.com/how-gpt3-works-visualizations-and-animations-zhong-yi">Chinese (Simplified)</a>, <a href="https://habr.com/ru/post/514698/">Russian</a>, <a href="https://devrimdanyal.medium.com/g%C3%B6rselle%C5%9Ftirmeler-ve-animasyonlar-ile-gpt3-nas%C4%B1l-%C3%A7al%C4%B1%C5%9F%C4%B1r-e7891ed3fa88">Turkish</a></span>
<br /></p>

<p>The tech world is <a href="https://www.theverge.com/21346343/gpt-3-explainer-openai-examples-errors-agi-potential">abuzz</a> with GPT3 hype. Massive language models (like GPT3) are starting to surprise us with their abilities. While not yet completely reliable for most businesses to put in front of their customers, these models are showing sparks of cleverness that are sure to accelerate the march of automation and the possibilities of intelligent computer systems. Let’s remove the aura of mystery around GPT3 and learn how it’s trained and how it works.</p>

<div style="text-align:center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/MQnJZuBGmSQ" title="YouTube video player" frameborder="0" style="
 width: 100%;
 max-width: 560px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe>
</div>

<p>A trained language model generates text.</p>

<p>We can optionally pass it some text as input, which influences its output.</p>

<p>The output is generated from what the model “learned” during its training period where it scanned vast amounts of text.</p>

<div class="img-div-any-width">
  <img src="/images/gpt3/01-gpt3-language-model-overview.gif" />
  <br />

</div>

<!--more-->

<p>Training is the process of exposing the model to lots of text. That process has been completed. All the experiments you see now are from that one trained model. It was estimated to cost 355 GPU years and cost $4.6m.</p>

<div class="img-div-any-width">
  <img src="/images/gpt3/02-gpt3-training-language-model.gif" />
  <br />

</div>

<p>The dataset of 300 billion tokens of text is used to generate training examples for the model. For example, these are three training examples generated from the one sentence at the top.</p>

<p>You can see how you can slide a window across all the text and make lots of examples.</p>

<div class="img-div-any-width">
  <img src="/images/gpt3/gpt3-training-examples-sliding-window.png" />
  <br />

</div>

<p>The model is presented with an example. We only show it the features and ask it to predict the next word.</p>

<p>The model’s prediction will be wrong. We calculate the error in its prediction and update the model so next time it makes a better prediction.</p>

<p>Repeat millions of times</p>

<div class="img-div-any-width">
  <img src="/images/gpt3/03-gpt3-training-step-back-prop.gif" />
  <br />

</div>

<p>Now let’s look at these same steps with a bit more detail.</p>

<p>GPT3 actually generates output one token at a time (let’s assume a token is a word for now).</p>

<div class="img-div-any-width">
  <img src="/images/gpt3/04-gpt3-generate-tokens-output.gif" />
  <br />

</div>

<p>Please note: This is a description of how GPT-3 works and not a discussion of what is novel about it (which is mainly the ridiculously large scale). The architecture is a transformer decoder model based on this paper https://arxiv.org/pdf/1801.10198.pdf</p>

<p>GPT3 is MASSIVE. It encodes what it learns from training in 175 billion numbers (called parameters). These numbers are used to calculate which token to generate at each run.</p>

<p>The untrained model starts with random parameters. Training finds values that lead to better predictions.</p>

<div class="img-div-any-width">
  <img src="/images/gpt3/gpt3-parameters-weights.png" />
  <br />

</div>

<p>These numbers are part of hundreds of matrices inside the model. Prediction is mostly a lot of matrix multiplication.</p>

<p>In my <a href="https://youtube.com/watch?v=mSTCzNgDJy4">Intro to AI on YouTube</a>, I showed a simple ML model with one parameter. A good start to unpack this 175B monstrosity.</p>

<p>To shed light on how these parameters are distributed and used, we’ll need to open the model and look inside.</p>

<p>GPT3 is 2048 tokens wide. That is its “context window”. That means it has 2048 tracks along which tokens are processed.</p>

<div class="img-div-any-width">
  <img src="/images/gpt3/05-gpt3-generate-output-context-window.gif" />
  <br />

</div>

<p>Let’s follow the purple track. How does a system process the word “robotics” and produce “A”?</p>

<p>High-level steps:</p>

<ol>
  <li>Convert the word to <a href="https://jalammar.github.io/illustrated-word2vec/">a vector (list of numbers) representing the word</a></li>
  <li>Compute prediction</li>
  <li>Convert resulting vector to word</li>
</ol>

<div class="img-div-any-width">
  <img src="/images/gpt3/06-gpt3-embedding.gif" />
  <br />

</div>

<p>The important calculations of the GPT3 occur inside its stack of 96 transformer decoder layers.</p>

<p>See all these layers? This is the “depth” in “deep learning”.</p>

<p>Each of these layers has its own 1.8B parameter to make its calculations. That is where the “magic” happens. This is a high-level view of that process:</p>

<div class="img-div-any-width">
  <img src="/images/gpt3/07-gpt3-processing-transformer-blocks.gif" />
  <br />

</div>

<p>You can see a detailed explanation of everything inside the decoder in my blog post <a href="https://jalammar.github.io/illustrated-gpt2/">The Illustrated GPT2</a>.</p>

<p>The difference with GPT3 is the alternating dense and <a href="https://arxiv.org/pdf/1904.10509.pdf">sparse self-attention layers</a>.</p>

<p>This is an X-ray of an input and response (“Okay human”) within GPT3. Notice how every token flows through the entire layer stack. We don’t care about the output of the first words. When the input is done, we start caring about the output. We feed every word back into the model.</p>

<div class="img-div-any-width">
  <img src="/images/gpt3/08-gpt3-tokens-transformer-blocks.gif" />
  <br />

</div>

<p>In the <a href="https://twitter.com/sharifshameem/status/1284421499915403264">React code generation example</a>, the description would be the input prompt (in green), in addition to a couple of examples of description=&gt;code, I believe. And the react code would be generated like the pink tokens here token after token.</p>

<p>My assumption is that the priming examples and the description are appended as input, with specific tokens separating examples and the results. Then fed into the model.</p>

<div class="img-div-any-width">
  <img src="/images/gpt3/09-gpt3-generating-react-code-example.gif" />
  <br />

</div>

<p>It’s impressive that this works like this. Because you just wait until fine-tuning is rolled out for the GPT3. The possibilities will be even more amazing.</p>

<p>Fine-tuning actually updates the model’s weights to make the model better at a certain task.</p>

<div class="img-div-any-width">
  <img src="/images/gpt3/10-gpt3-fine-tuning.gif" />
  <br />

</div>

  </div>

  <div class="date">
    Written on July 27, 2020
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
