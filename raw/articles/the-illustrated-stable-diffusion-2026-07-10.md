---

source_url: http://jalammar.github.io/illustrated-stable-diffusion/
ingested: 2026-07-10
sha256: da68268430441e33afb7830f9c81e4173cf760d3483eee6643e7175fa76a1349
blog_source: Jay Alammar
---

<!DOCTYPE html>
<html>
  <head>
    <title>The Illustrated Stable Diffusion – Jay Alammar – Visualizing machine learning one concept at a time.</title>

        <meta charset="utf-8" />
    <meta content='text/html; charset=utf-8' http-equiv='Content-Type'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0'>

    
    <meta name="description" content="Translations: Chinese, Vietnamese.


(V2 Nov 2022: Updated images for more precise description of forward diffusion. A few more images in this version)

AI image generation is the most recent AI capability blowing people’s minds (mine included). The ability to create striking visuals from text descriptions has a magical quality to it and points clearly to a shift in how humans create art. The release of Stable Diffusion is a clear milestone in this development because it made a high-performance model available to the masses (performance in terms of image quality, as well as speed and relatively low resource/memory requirements).



After experimenting with AI image generation, you may start to wonder how it works.

This is a gentle introduction to how Stable Diffusion works.


  
  



Stable Diffusion is versatile in that it can be used in a number of different ways. Let’s focus at first on image generation from text only (text2img). The image above shows an example text input and the resulting generated image (The actual complete prompt is here). Aside from text to image, another main way of using it is by making it alter images (so inputs are text + image).

" />
    <meta property="og:description" content="Translations: Chinese, Vietnamese.


(V2 Nov 2022: Updated images for more precise description of forward diffusion. A few more images in this version)

AI image generation is the most recent AI capability blowing people’s minds (mine included). The ability to create striking visuals from text descriptions has a magical quality to it and points clearly to a shift in how humans create art. The release of Stable Diffusion is a clear milestone in this development because it made a high-performance model available to the masses (performance in terms of image quality, as well as speed and relatively low resource/memory requirements).



After experimenting with AI image generation, you may start to wonder how it works.

This is a gentle introduction to how Stable Diffusion works.


  
  



Stable Diffusion is versatile in that it can be used in a number of different ways. Let’s focus at first on image generation from text only (text2img). The image above shows an example text input and the resulting generated image (The actual complete prompt is here). Aside from text to image, another main way of using it is by making it alter images (so inputs are text + image).

" />
    
    <meta name="author" content="Jay Alammar" />

    
    <meta property="og:title" content="The Illustrated Stable Diffusion" />
    <meta property="twitter:title" content="The Illustrated Stable Diffusion" />
    

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
  <h1>The Illustrated Stable Diffusion</h1>

  <div class="entry prediction">
    <p><span class="discussion">Translations: <a href="https://blog.csdn.net/yujianmin1990/article/details/129143157">Chinese</a>, <a href="https://trituenhantao.io/kien-thuc/minh-hoa-stable-diffusion/">Vietnamese</a>.
</span></p>

<p>(<strong>V2 Nov 2022</strong>: Updated images for more precise description of forward diffusion. A few more images in this version)</p>

<p>AI image generation is the most recent AI capability blowing people’s minds (mine included). The ability to create striking visuals from text descriptions has a magical quality to it and points clearly to a shift in how humans create art. The release of <a href="https://stability.ai/blog/stable-diffusion-public-release">Stable Diffusion</a> is a clear milestone in this development because it made a high-performance model available to the masses (performance in terms of image quality, as well as speed and relatively low resource/memory requirements).</p>

<iframe width="560" height="315" src="https://www.youtube.com/embed/MXmacOUJUaw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" style="
 width: 100%;
 max-width: 560px;" allowfullscreen=""></iframe>

<p>After experimenting with AI image generation, you may start to wonder how it works.</p>

<p>This is a gentle introduction to how Stable Diffusion works.</p>

<div class="img-div-any-width">
  <img src="/images/stable-diffusion/stable-diffusion-text-to-image.png" />
  <br />

</div>

<p>Stable Diffusion is versatile in that it can be used in a number of different ways. Let’s focus at first on image generation from text only (text2img). The image above shows an example text input and the resulting generated image (The actual complete prompt is here). Aside from text to image, another main way of using it is by making it alter images (so inputs are text + image).</p>

<!--more-->

<div class="img-div-any-width">
  <img src="/images/stable-diffusion/stable-diffusion-img2img-image-to-image.png" />
  <br />

</div>

<p>Let’s start to look under the hood because that helps explain the components, how they interact, and what the image generation options/parameters mean.</p>

<h2 id="the-components-of-stable-diffusion">The Components of Stable Diffusion</h2>

<p>Stable Diffusion is a system made up of several components and models. It is not one monolithic model.</p>

<p>As we look under the hood, the first observation we can make is that there’s a text-understanding component that translates the text information into a numeric representation that captures the ideas in the text.</p>

<div class="img-div-any-width">
  <img src="/images/stable-diffusion/stable-diffusion-text-understanding-component-image-generation.png" />
  <br />

</div>

<p>We’re starting with a high-level view and we’ll get into more machine learning details later in this article. However, we can say that this text encoder is a special Transformer language model (technically: the text encoder of a CLIP model). It takes the input text and outputs a list of numbers representing each word/token in the text  (a vector per token).</p>

<p>That information is then presented to the Image Generator, which is composed of a couple of components itself.</p>

<div class="img-div-any-width">
  <img src="/images/stable-diffusion/Stable-diffusion-text-info-to-image-generator.png" />
  <br />

</div>

<p>The image generator goes through two stages:</p>

<p>1- <strong>Image information creator</strong></p>

<p>This component is the secret sauce of Stable Diffusion. It’s where a lot of the performance gain over previous models is achieved.</p>

<p>This component runs for multiple steps to generate image information. This is the <em>steps</em> parameter in Stable Diffusion interfaces and libraries which often defaults to 50 or 100.</p>

<p>The image information creator works completely in the <em>image information space</em> (or <em>latent</em> space). We’ll talk more about what that means later in the post. This property makes it faster than previous diffusion models that worked in pixel space. In technical terms, this component is made up of a UNet neural network and a scheduling algorithm.</p>

<p>The word “diffusion” describes what happens in this component. It is the step by step processing of information that leads to a high-quality image being generated in the end (by the next component, the image decoder).</p>

<div class="img-div-any-width">
  <img src="/images/stable-diffusion/Stable-diffusion-image-generator-information-creator.png" />
  <br />

</div>

<p>2- <strong>Image Decoder</strong></p>

<p>The image decoder paints a picture from the information it got from the information creator. It runs only once at the end of the process to produce the final pixel image.</p>

<div class="img-div-any-width">
  <img src="/images/stable-diffusion/stable-diffusion-cliptext-unet-autoencoder-decoder.png" />
  <br />

</div>

<p>With this we come to see the three main components (each with its own neural network) that make up Stable Diffusion:</p>

<ul>
  <li>
    <p><strong>ClipText</strong> for text encoding. <br />
Input: text. <br />
Output: 77 token embeddings vectors, each in 768 dimensions.</p>
  </li>
  <li>
    <p><strong>UNet + Scheduler</strong> to gradually process/diffuse information in the information (latent) space. <br />
Input: text embeddings and a starting multi-dimensional array (structured lists of numbers, also called a <em>tensor</em>) made up of noise.<br />
Output: A processed information array</p>
  </li>
  <li>
    <p><strong>Autoencoder Decoder</strong> that paints the final image using the processed information array.<br />
Input: The processed information array (dimensions: (4,64,64))  <br />
Output: The resulting image (dimensions: (3, 512, 512) which are (red/green/blue, width, height))</p>
  </li>
</ul>

<div class="img-div-any-width">
  <img src="/images/stable-diffusion/stable-diffusion-components-and-tensors.png" />
  <br />

</div>

<h2 id="what-is-diffusion-anyway">What is Diffusion Anyway?</h2>

<p>Diffusion is the process that takes place inside the pink “image information creator” component. Having the token embeddings that represent the input text, and a random starting <em>image information array</em> (these are also called <em>latents</em>), the process produces an information array that the image decoder uses to paint the final image.</p>

<div class="img-div-any-width">
  <img src="/images/stable-diffusion/stable-diffusion-diffusion-process.png" />
  <br />

</div>

<p>This process happens in a step-by-step fashion. Each step adds more relevant information. To get an intuition of the process, we can inspect the random latents array, and see that it translates to visual noise. Visual inspection in this case is passing it through the image decoder.</p>

<div class="img-div-any-width">
  <img src="/images/stable-diffusion/stable-diffusion-latent-space-pixel-space.png" />
  <br />

</div>

<p>Diffusion happens in multiple steps, each step operates on an input latents array, and produces another latents array that better resembles the input text and all the visual information the model picked up from all images the model was trained on.</p>

<div class="img-div-any-width">
  <img src="/images/stable-diffusion/stable-diffusion-unet-steps.png" />
  <br />

</div>

<p>We can visualize a set of these latents to see what information gets added at each step.</p>

<div class="img-div-any-width">
  <img src="/images/stable-diffusion/stable-diffusion-denoising-steps-latents.png" />
  <br />

</div>

<p>The process is quite breathtaking to look at.</p>

<div class="img-div-any-width">
<video height="auto" loop="" autoplay="" controls="">
  <source src="/images/stable-diffusion/diffusion-steps-all-loop.webm" type="video/webm" />
  Your browser does not support the video tag.
</video>
</div>

<p>Something especially fascinating happens between steps 2 and 4 in this case. It’s as if the outline emerges from the noise.</p>

<div class="img-div-any-width">
<video height="auto" loop="" autoplay="" controls="">
  <source src="/images/stable-diffusion/stable-diffusion-steps-2-4.webm" type="video/webm" />
  Your browser does not support the video tag.
</video>
</div>

<h3 id="how-diffusion-works">How diffusion works</h3>
<p>The central idea of generating images with diffusion models relies on the fact that we have powerful computer vision models. Given a large enough dataset, these models can learn complex operations. Diffusion models approach image generation by framing the problem as following:</p>

<p>Say we have an image, we generate some noise, and add it to the image.</p>

<div class="img-div">
  <img src="/images/stable-diffusion/stable-diffusion-forward-diffusion-training-example.png" />
  <br />

</div>
<p>This can now be considered a training example. We can use this same formula to create lots of training examples to train the central component of our image generation model.</p>

<div class="img-div">
  <img src="/images/stable-diffusion/stable-diffusion-forward-diffusion-training-example-2.png" />
  <br />

</div>

<p>While this example shows a few noise amount values from image (amount 0, no noise) to total noise (amount 4, total noise), we can easily control how much noise to add to the image, and so we can spread it over tens of steps, creating tens of training examples per image for all the images in a training dataset.</p>

<div class="img-div">
  <img src="/images/stable-diffusion/stable-diffusion-u-net-noise-training-examples-2.png" />
  <br />

</div>

<p>With this dataset, we can train the noise predictor and end up with a great noise predictor that actually creates images when run in a certain configuration. A training step should look familiar if you’ve had ML exposure:</p>

<div class="img-div">
<a href="/images/stable-diffusion/stable-diffusion-u-net-noise-training-step.png">
  <img src="/images/stable-diffusion/stable-diffusion-u-net-noise-training-step.png" />
  </a><br />

</div>

<p>Let’s now see how this can generate images.</p>

<h3 id="painting-images-by-removing-noise">Painting images by removing noise</h3>

<p>The trained noise predictor can take a noisy image, and the number of the denoising step, and is able to predict a slice of noise.</p>
<div class="img-div">
  <img src="/images/stable-diffusion/stable-diffusion-denoising-step-1v2.png" />
  <br />

</div>

<p>The sampled noise is predicted so that if we subtract it from the image, we get an image that’s closer to the images the model was trained on (not the exact images themselves, but the <em>distribution</em> - the world of pixel arrangements where the sky is usually blue and above the ground, people have two eyes, cats look a certain way – pointy ears and clearly unimpressed).</p>

<div class="img-div">
  <a href="/images/stable-diffusion/stable-diffusion-denoising-step-2v2.png"><img src="/images/stable-diffusion/stable-diffusion-denoising-step-2v2.png" /></a>
  <br />

</div>

<p>If the training dataset was of aesthetically pleasing images (e.g., <a href="https://laion.ai/blog/laion-aesthetics/">LAION Aesthetics</a>, which Stable Diffusion was trained on), then the resulting image would tend to be aesthetically pleasing. If the we train it on images of logos, we end up with a logo-generating model.</p>

<div class="img-div">
<a href="/images/stable-diffusion/stable-diffusion-image-generation-v2.png">
  <img src="/images/stable-diffusion/stable-diffusion-image-generation-v2.png" />
</a>
  <br />

</div>

<p>This concludes the description of image generation by diffusion models mostly as described in <a href="https://arxiv.org/abs/2006.11239">Denoising Diffusion Probabilistic Models</a>. Now that you have this intuition of diffusion, you know the main components of not only Stable Diffusion, but also Dall-E 2 and Google’s Imagen.</p>

<p>Note that the diffusion process we described so far generates images without using any text data. So if we deploy this model, it would generate great looking images, but we’d have no way of controlling if it’s an image of a pyramid or a cat or anything else. In the next sections we’ll describe how text is incorporated in the process in order to control what type of image the model generates.</p>

<h2 id="speed-boost-diffusion-on-compressed-latent-data-instead-of-the-pixel-image">Speed Boost: Diffusion on Compressed (Latent) Data Instead of the Pixel Image</h2>

<p>To speed up the image generation process, the Stable Diffusion paper runs the diffusion process not on the pixel images themselves, but on a compressed version of the image. <a href="https://arxiv.org/abs/2112.10752">The paper</a> calls this “Departure to Latent Space”.</p>

<p>This compression (and later decompression/painting) is done via an autoencoder. The autoencoder compresses the image into the latent space using its encoder, then reconstructs it using only the compressed information using the decoder.</p>

<div class="img-div">
  <img src="/images/stable-diffusion/stable-diffusion-autoencoder.png" />
  <br />

</div>

<p>Now the forward diffusion process is done on the compressed latents. The slices of noise are of noise applied to those latents, not to the pixel image. And so the noise predictor is actually trained to predict noise in the compressed representation (the latent space).</p>

<div class="img-div">
<a href="/images/stable-diffusion/stable-diffusion-latent-forward-process-v2.png">
  <img src="/images/stable-diffusion/stable-diffusion-latent-forward-process-v2.png" />
</a>
  <br />

</div>

<p>The forward process (using the autoencoder’s encoder) is how we generate the data to train the noise predictor. Once it’s trained, we can generate images by running the reverse process (using the autoencoder’s decoder).</p>

<div class="img-div">
<a href="/images/stable-diffusion/stable-diffusion-forward-and-reverse-process-v2.png">
  <img src="/images/stable-diffusion/stable-diffusion-forward-and-reverse-process-v2.png" />
</a>
  <br />

</div>

<p>These two flows are what’s shown in Figure 3 of the LDM/Stable Diffusion paper:</p>

<div class="img-div">
  <img src="/images/stable-diffusion/article-Figure3-1-1536x762.png" />
  <br />

</div>

<p>This figure additionally shows the “conditioning” components, which in this case is the text prompts describing what image the model should generate. So let’s dig into the text components.</p>

<h3 id="the-text-encoder-a-transformer-language-model">The Text Encoder: A Transformer Language Model</h3>

<p>A Transformer language model is used as the language understanding component that takes the text prompt and produces token embeddings. The released Stable Diffusion model uses ClipText (A <a href="/illustrated-gpt2/">GPT-based model</a>), while the paper used <a href="/illustrated-bert/">BERT</a>.</p>

<p>The choice of language model is shown by the Imagen paper to be an important one. Swapping in larger language models had more of an effect on generated image quality than larger image generation components.</p>

<div class="img-div">
  <img src="/images/stable-diffusion/text-language-models-clip-image-generation.png" />
  <br />

  Larger/better language models have a significant effect on the quality of image generation models. Source: <a href="https://arxiv.org/abs/2205.11487">Google Imagen paper by Saharia et. al.</a>. Figure A.5.

</div>

<p>The early Stable Diffusion models just plugged in the pre-trained ClipText model released by OpenAI. It’s possible that future models may switch to the newly released and much larger <a href="https://laion.ai/blog/large-openclip/">OpenCLIP</a> variants of CLIP (Nov2022 update: True enough, <a href="https://stability.ai/blog/stable-diffusion-v2-release">Stable Diffusion V2 uses OpenClip</a>). This new batch includes text models of sizes up to 354M parameters, as opposed to the 63M parameters in ClipText.</p>

<h4 id="how-clip-is-trained">How CLIP is trained</h4>

<p>CLIP is trained on a dataset of images and their captions. Think of a dataset looking like this, only with 400 million images and their captions:</p>

<div class="img-div">
  <img src="/images/stable-diffusion/images-and-captions-dataset.png" />
  <br />
  A dataset of images and their captions.
</div>

<p>In actuality, CLIP was trained on images crawled from the web along with their “alt” tags.</p>

<p>CLIP is a combination of an image encoder and a text encoder. Its training process can be simplified to thinking of taking an image and its caption. We encode them both with the image and text encoders respectively.</p>

<div class="img-div">
  <img src="/images/stable-diffusion/clip-training-step-1.png" />
  <br />
  
</div>

<p>We then compare the resulting embeddings using cosine similarity. When we begin the training process, the similarity will be low, even if the text describes the image correctly.</p>

<div class="img-div">
  <img src="/images/stable-diffusion/clip-training-step-2.png" />
  <br />
  
</div>

<p>We update the two models so that the next time we embed them, the resulting embeddings are similar.</p>

<div class="img-div">
  <img src="/images/stable-diffusion/clip-training-step-3.png" />
  <br />
  
</div>

<p>By repeating this across the dataset and with large batch sizes, we end up with the encoders being able to produce embeddings where an image of a dog and the sentence “a picture of a dog” are similar. Just like in <a href="/illustrated-word2vec/">word2vec</a>, the training process also needs to include <strong>negative examples</strong> of images and captions that don’t match, and the model needs to assign them low similarity scores.</p>

<h2 id="feeding-text-information-into-the-image-generation-process">Feeding Text Information Into The Image Generation Process</h2>

<p>To make text a part of the image generation process, we have to adjust our noise predictor to use the text as an input.</p>

<div class="img-div">
<a href="/images/stable-diffusion/stable-diffusion-unet-inputs-v2.png">
  <img src="/images/stable-diffusion/stable-diffusion-unet-inputs-v2.png" />
  </a><br />

</div>

<p>Our dataset now includes the encoded text. Since we’re operating in the latent space, both the input images and predicted noise are in the latent space.</p>

<div class="img-div">
  <img src="/images/stable-diffusion/stable-diffusion-text-dataset-v2.png" />
  <br />

</div>

<p>To get a better sense of how the text tokens are used in the Unet, let’s look deeper inside the Unet.</p>

<h3 id="layers-of-the-unet-noise-predictor-without-text">Layers of the Unet Noise predictor (without text)</h3>

<p>Let’s first look at a diffusion Unet that does not use text. Its inputs and outputs would look like this:</p>

<div class="img-div-any-width">
  <img src="/images/stable-diffusion/unet-inputs-outputs-v2.png" />
  <br />

</div>

<p>Inside, we see that:</p>

<ul>
  <li>The Unet is a series of layers that work on transforming the latents array</li>
  <li>Each layer operates on the output of the previous layer</li>
  <li>Some of the outputs are fed (via residual connections) into the processing later in the network</li>
  <li>The timestep is transformed into a time step embedding vector, and that’s what gets used in the layers</li>
</ul>

<div class="img-div-any-width">
  <img src="/images/stable-diffusion/unit-resnet-steps-v2.png" />
  <br />

</div>

<h3 id="layers-of-the-unet-noise-predictor-with-text">Layers of the Unet Noise predictor WITH text</h3>

<p>Let’s now look how to alter this system to include attention to the text.</p>

<div class="img-div-any-width">
  <img src="/images/stable-diffusion/unet-with-text-inputs-outputs-v2.png" />
  <br />

</div>

<p>The main change to the system we need to add support for text inputs (technical term: text conditioning) is to add an attention layer between the ResNet blocks.</p>

<div class="img-div-any-width">
  <img src="/images/stable-diffusion/unet-with-text-steps-v2.png" />
  <br />

</div>

<p>Note that the ResNet block doesn’t directly look at the text. But the attention layers merge those text representations in the latents. And now the next ResNet can utilize that incorporated text information in its processing.</p>

<h2 id="conclusion">Conclusion</h2>

<p>I hope this gives you a good first intuition about how Stable Diffusion works. Lots of other concepts are involved, but I believe they’re easier to understand once you’re familiar with the building blocks above. The resources below are great next steps that I found useful. Please reach out to me on <a href="https://twitter.com/JayAlammar">Twitter</a> for any corrections or feedback.</p>

<h2 id="resources">Resources</h2>

<ul>
  <li>I have a <a href="https://youtube.com/shorts/qL6mKRyjK-0?feature=share">one-minute YouTube short</a> on using <a href="https://beta.dreamstudio.ai/">Dream Studio</a> to generate images with Stable Diffusion.</li>
  <li><a href="https://huggingface.co/blog/stable_diffusion">Stable Diffusion with 🧨 Diffusers</a></li>
  <li><a href="https://huggingface.co/blog/annotated-diffusion">The Annotated Diffusion Model</a></li>
  <li><a href="https://www.youtube.com/watch?v=J87hffSMB60">How does Stable Diffusion work? – Latent Diffusion Models EXPLAINED</a> [Video]</li>
  <li><a href="https://www.youtube.com/watch?v=ltLNYA3lWAQ">Stable Diffusion - What, Why, How?</a> [Video]</li>
  <li><a href="https://ommer-lab.com/research/latent-diffusion-models/">High-Resolution Image Synthesis with Latent Diffusion Models</a> [The Stable Diffusion paper]</li>
  <li>For a more in-depth look at the algorithms and math, see Lilian Weng’s <a href="https://lilianweng.github.io/posts/2021-07-11-diffusion-models/">What are Diffusion Models?</a></li>
  <li>Watch the <a href="https://www.youtube.com/watch?v=_7rMfsA24Ls&amp;ab_channel=JeremyHoward">great Stable Diffusion videos from fast.ai</a></li>
</ul>

<h2 id="acknowledgements">Acknowledgements</h2>

<p>Thanks to Robin Rombach, Jeremy Howard, Hamel Husain, Dennis Soemers, Yan Sidyakin, Freddie Vargus, Anna Golubeva, and the <a href="https://cohere.for.ai/">Cohere For AI</a> community for feedback on earlier versions of this article.</p>

<h2 id="contribute">Contribute</h2>
<p>Please help me make this article better. Possible ways:</p>

<ul>
  <li>Send any feedback or corrections on <a href="https://twitter.com/JayAlammar">Twitter</a> or as a <a href="https://github.com/jalammar/jalammar.github.io">Pull Request</a></li>
  <li>Help make the article more accessible by suggesting captions and alt-text to the visuals (best as a pull request)</li>
  <li>Translate it to another language and post it to your blog. Send me the link and I’ll add a link to it here. Translators of previous articles have always mentioned how much deeper they understood the concepts by going through the translation process.</li>
</ul>

<h2 id="discuss">Discuss</h2>

<p>If you’re interested in discussing the overlap of image generation models with language models, feel free to post in the #images-and-words channel in the <a href="https://discord.gg/co-mmunity">Cohere community on Discord</a>. There, we discuss areas of overlap, including:</p>

<ul>
  <li>fine-tuning language models to produce good image generation prompts</li>
  <li>Using LLMs to split the subject, and style components of an image captioning prompt</li>
  <li>Image-to-prompt (via tools like <a href="https://colab.research.google.com/github/pharmapsychotic/clip-interrogator/blob/main/clip_interrogator.ipynb">Clip Interrogator</a>)</li>
</ul>

<h2 id="citation">Citation</h2>

<p>If you found this work helpful for your research, please cite it as following:</p>

<div class="cite">

  <pre><code class="language-code">@misc{alammar2022diffusion, 
  title={The Illustrated Stable Diffusion},
  author={Alammar, J},
  year={2022},
  url={https://jalammar.github.io/illustrated-stable-diffusion/}
}
</code></pre>

</div>

  </div>

  <div class="date">
    Written on October  4, 2022
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
