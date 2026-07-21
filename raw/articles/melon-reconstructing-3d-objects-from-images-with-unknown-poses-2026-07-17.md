---
source_url: http://blog.research.google/2024/03/melon-reconstructing-3d-objects-from.html
ingested: 2026-07-17
sha256: 347ca0395ff8a65e6d475390e4a53b83f15f4458eb4a4f6cdaf16308ed12026c
blog_source: Google Research Blog
---




<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8" />
    
        
<link rel="canonical" href="https://research.google/blog/melon-reconstructing-3d-objects-from-images-with-unknown-poses/" /><meta property="og:title" content="MELON: Reconstructing 3D objects from images with unknown poses"><meta property="og:url" content="https://research.google/blog/melon-reconstructing-3d-objects-from-images-with-unknown-poses/"><meta property="og:image" content="https://storage.googleapis.com/gweb-research2023-media/images/HO_previewImage1.width-800.format-jpeg.jpg"><meta property="og:image:secure_url" content="https://storage.googleapis.com/gweb-research2023-media/images/HO_previewImage1.width-800.format-jpeg.jpg"><meta property="og:type" content="Website">

    
    
    <title>MELON: Reconstructing 3D objects from images with unknown poses</title>
    
    <meta name="viewport" content="width=device-width, initial-scale=1 viewport-fit=cover"/>

    
    

    <link rel="icon" type="image/png" href="https://www.gstatic.com/images/branding/googleg_gradient/1x/googleg_gradient_standard_20dp.png">

    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload"
        href="https://fonts.googleapis.com/css2?family=Google+Sans+Flex:opsz,wght@6..144,1..1000&family=Product+Sans&display=swap"
        as="style">
    <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Google+Sans+Flex:opsz,wght@6..144,1..1000&family=Product+Sans&display=swap">
    <link rel="preload"
        href="https://fonts.googleapis.com/css2?family=Product+Sans&family=Google+Sans+Display:ital@0;1&family=Google+Sans:ital,wght@0,400;0,500;0,700;1,400;1,500;1,700&family=Google+Sans+Text:ital,wght@0,400;0,500;0,700;1,400;1,500;1,700&display=swap"
        as="style">
    <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Product+Sans&family=Google+Sans+Display:ital@0;1&family=Google+Sans:ital,wght@0,400;0,500;0,700;1,400;1,500;1,700&family=Google+Sans+Text:ital,wght@0,400;0,500;0,700;1,400;1,500;1,700&display=swap">
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap" rel="stylesheet">
    <link rel="preload" href="https://fonts.googleapis.com/css2?family=Google+Symbols:opsz,wght,FILL,GRAD,ROND@48,100..300,0..1,0,100&display=swap" as="style" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Symbols:opsz,wght,FILL,GRAD,ROND@48,100..300,0..1,0,100&display=swap">

    
    <link href="https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.css" rel="stylesheet" />
    <link href="https://www.gstatic.com/glue/v27_1/glue-material.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="/gr/static/css/googleresearch.css?id=1df8cfd093ef74378ad52e9df6e91ef9">
    
    
    

    
    
      <script id="analyticsScript" data-blog-publish-date="20240318"
          data-blog-word-count="1173">
        window.dataLayer = window.dataLayer || [];
        const blogData = document.querySelector('#analyticsScript')

        dataLayer.push({
          publishDate: blogData?.dataset.blogPublishDate,
          wordCount: blogData?.dataset.blogWordCount,
        });
      </script>
    

    <!-- Google Tag Manager -->
    <script>
      window.dataLayer = window.dataLayer || [];
      function glueCookieNotificationBarLoaded() {
        (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
        new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
        j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
        'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
        })(window,document,'script','dataLayer','GTM-K8QBZ7Q');
      }
    </script>
    <!-- End Google Tag Manager -->
</head>

<body class=" js-google-tag-wrapper" data-gt-page-path="https://research.google/blog/melon-reconstructing-3d-objects-from-images-with-unknown-poses/" data-env="production">
    
    <div class="button-group skip-link">
      <a href="#page-content" class="glue-button glue-button--high-emphasis">Skip to main content</a>
    </div>
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-K8QBZ7Q"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->
    
    
      




  
    
    
      
        
  <site-nav>
    <header class="site-navigation-isolation header glue-header glue-header--no-cta deepai-header js-header js-site-navigation">
      <div class="header-container">
        <div class="header__background mobile tablet"></div>
        
          <div class="header flyout__desktop-container">
            
              
                
<nav class="header flyout desktop"
    data-section="Research"
    aria-labelledby="Research">
  <div class="flyout__container grid">
    
    <div class="flyout__intro">
      <div>
        <h2 class="headline-6">Explore our many areas of focus</h2>
        
      </div>
      
        <div class="button-group button-group--compact">
          <div class="button-group__buttons">
            
              



  
  
    <a href="/research-areas/"
      
      
       class="glue-button glue-button--medium-emphasis cta-small"
      
      
        data-gtm-event="nav_select"
        data-event-nav-type="subheader"
        data-event-nav-name="Research - Explore all research areas"
      
      
      >
      <div class="button__label">
        
          Explore all research areas
        
      </div>
    </a>
  


            
          </div>
        </div>
      
    </div>

    
    <div class="flyout__content-desktop">
      <div class="flyout__subnav subnav subnav--3-column">
        
          <div class="subnav__column">
            <div class="subnav__content">
              
                <div class="subnav__header">
                  
                    <div class="cta-small">Applied AI &amp; sciences</div>
                  
                  
                </div>
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/google-earth-ai/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/earth_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="earth_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Earth AI</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/health-ai/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/health_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="health_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Health AI</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/science-ai/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/science_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="science_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Science AI</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/sustainability-crisis-resilience/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/sustainability_crisis_resilience_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="sustainability_crisis_resilience_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Sustainability &amp; crisis resilience</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
          <div class="subnav__column">
            <div class="subnav__content">
              
                <div class="subnav__header">
                  
                    <div class="cta-small">Foundational ML &amp; algorithms</div>
                  
                  
                </div>
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/algorithms-and-theory/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/algorithms_theory_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="algorithms_theory_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Algorithms &amp; theory</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/information-retrieval/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/information_retrieval_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="information_retrieval_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Information retrieval</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/machine-intelligence/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/machine_intelligence_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="machine_intelligence_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Machine intelligence</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/machine-perception/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/machine_perception_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="machine_perception_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Machine perception</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/natural-language-processing/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/NLP_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="NLP_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Natural language processing</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
          <div class="subnav__column">
            <div class="subnav__content">
              
                <div class="subnav__header">
                  
                    <div class="cta-small">People, systems &amp; quantum AI</div>
                  
                  
                </div>
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/human-computer-interaction-and-visualization/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/human_computer_interaction_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="human_computer_interaction_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Human-computer interaction and visualization</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/networking/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/networking_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="networking_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Networking</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/quantum-computing/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/quantum_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="quantum_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Quantum AI</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/responsible-ai/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/responsible_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="responsible_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Responsible AI</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/anti-abuse/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/anti_abuse_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="anti_abuse_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Anti abuse</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/software-engineering/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/software_engineering_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="software_engineering_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Software engineering</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/research-areas/software-systems/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/software_systems_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="software_systems_nav1">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Software systems</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
          <div class="subnav__column">
            <div class="subnav__content">
              
                <div class="subnav__header">
                  
                    <div class="cta-small">Learn More</div>
                  
                  
                </div>
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/pubs/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/publications_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="publications_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Publications</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small "
                          href="/resources/our-projects/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--small">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/projects_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="projects_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Projects</div>
                          <div class="small-text"></div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
      </div>
    </div>
  </div>
</nav>
              
            
              
                
<nav class="header flyout desktop"
    data-section="Resources"
    aria-labelledby="Resources">
  <div class="flyout__container grid">
    
    <div class="flyout__intro">
      <div>
        <h2 class="headline-6">Building a collaborative ecosystem</h2>
        
      </div>
      
    </div>

    
    <div class="flyout__content-desktop">
      <div class="flyout__subnav subnav subnav--2-column">
        
          <div class="subnav__column">
            <div class="subnav__content">
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="https://research.google/resources/#datasets-1"
                          
                            target="_self"
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/dataset_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="dataset_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Datasets</div>
                          <div class="small-text">Access high-quality datasets to accelerate your research.</div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="https://research.google/resources/#tools-services-2"
                          
                            target="_self"
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/models_products_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="models_products_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Tools &amp; services</div>
                          <div class="small-text">Explore our latest AI models and products.</div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
          <div class="subnav__column">
            <div class="subnav__content">
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="https://research.google/resources/#open-source-3"
                          
                            target="_self"
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/software_engineering_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="software_engineering_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Open source</div>
                          <div class="small-text">Discover open-source code and collaborate with the community.</div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
      </div>
    </div>
  </div>
</nav>
              
            
              
            
              
                
<nav class="header flyout desktop"
    data-section="Careers"
    aria-labelledby="Careers">
  <div class="flyout__container grid">
    
    <div class="flyout__intro">
      <div>
        <h2 class="headline-6">Shaping the future together</h2>
        
      </div>
      
        <div class="button-group button-group--compact">
          <div class="button-group__buttons">
            
              



  
  
    <a href="/programs-and-events/"
      
      
       class="glue-button glue-button--medium-emphasis cta-small"
      
      
        data-gtm-event="nav_select"
        data-event-nav-type="subheader"
        data-event-nav-name="Careers - See all programs"
      
      
      >
      <div class="button__label">
        
          See all programs
        
      </div>
    </a>
  


            
          </div>
        </div>
      
    </div>

    
    <div class="flyout__content-desktop">
      <div class="flyout__subnav subnav subnav--2-column">
        
          <div class="subnav__column">
            <div class="subnav__content">
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="/programs-and-events/faculty-engagement/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/faculty_programs_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="faculty_programs_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Faculty programs</div>
                          <div class="small-text">Participating in the academic research community through meaningful engagement with university faculty.</div>
                        </div>
                      </a>
                      
                    
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="/programs-and-events/student-engagement/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/student_programs_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="student_programs_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Student programs</div>
                          <div class="small-text">Supporting the next generation of researchers through a wide range of programming.</div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
          <div class="subnav__column">
            <div class="subnav__content">
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="/careers/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/locations_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="locations_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Locations</div>
                          <div class="small-text">Find your place in our global offices and research labs.</div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
      </div>
    </div>
  </div>
</nav>
              
            
              
            
              
                
<nav class="header flyout desktop"
    data-section="About"
    aria-labelledby="About">
  <div class="flyout__container grid">
    
    <div class="flyout__intro">
      <div>
        <h2 class="headline-6">Translating discovery into real-world impact</h2>
        
      </div>
      
    </div>

    
    <div class="flyout__content-desktop">
      <div class="flyout__subnav subnav subnav--2-column">
        
          <div class="subnav__column">
            <div class="subnav__content">
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="/people/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/earth_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="earth_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">People</div>
                          <div class="small-text">Our researchers drive advancements in computer science through both fundamental and applied research.</div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
          <div class="subnav__column">
            <div class="subnav__content">
              

              
              
                <div class="subnav__links">
                  
                    
                      
                      <a class="subnav__link cta-small  subnav__link--has-icon"
                          href="/teams/"
                          
                            
                          >
                        
                          <div class="subnav__link-image subnav__link-image--large">
                            <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/teams_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="teams_nav">
      
      
    
  


      
    
  </div>

</div>
                          </div>
                        
                        <div class="subnav__link-text">
                          <div class="cta-small">Teams</div>
                          <div class="small-text">Collaborative groups tackling the world&#x27;s most challenging AI problems.</div>
                        </div>
                      </a>
                      
                    
                  
                </div>
              

              
              
            </div>
          </div>
        
      </div>
    </div>
  </div>
</nav>
              
            
          </div>
        

        

<nav class="header flyout mobile">
  <div class="flyout__container">
    <div class="flyout__content-mobile">
      
        
          <div class="flyout__accordion">
            
            <button type="button" data-title="Research"
                class="main-menu__label-tablet flyout__accordion__toggle text-call-to-action"
                aria-expanded="false" aria-controls="submenu-1">
              <span class="flyout__accordion__label cta">Research</span>
              <span class="button-group button-group--compact" aria-hidden="true">
                <span class="button-group__buttons">
                  
                  <span class="button flyout__accordion__icon open">
                    <span class="icon-md-outlined">
                      
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="M480-357.85 253.85-584l32.61-32.61L480-423.08l193.54-193.53L706.15-584 480-357.85Z" />
  
</svg>

                    </span>
                  </span>
                  <span class="button flyout__accordion__icon close">
                    <span class="icon-md-outlined">
                      
<svg xmlns="http://www.w3.org/2000/svg"
     height="18px"
     width="18px"
     viewBox="0 -960 960 960"
     fill="currentColor"
     class=""
     aria-hidden="true"
     role="presentation">
  
    <path d="m480-541.85-184 184L253.85-400 480-626.15 706.15-400 664-357.85l-184-184Z" />
  
</svg>

                    </span>
                  </span>
                </span>
              </span>
            </button>
            
            <div id="submenu-1" class="flyout__accordion__content"
                data-section="Research" hidden>
              <div class="flyout__accordion__content-inner">
                <div class="flyout__intro">
                  <div>
                    <h2 class="flyout__title headline-5">Explore our many areas of focus</h2>
                    
                  </div>
                  
                    <div class="button-group button-group--row_start button-group--compact">
                      <div class="button-group__buttons">
                        
                          



  
  
    <a href="/research-areas/"
      
      
       class="glue-button glue-button--medium-emphasis cta-small"
      
      
        data-gtm-event="nav_select"
        data-event-nav-type="subheader"
        data-event-nav-name="Research - Explore all research areas"
      
      
      >
      <div class="button__label">
        
          Explore all research areas
        
      </div>
    </a>
  


                        
                      </div>
                    </div>
                  
                </div>
                <div class="flyout__subnav subnav subnav--3-column">
                  
                    <div class="subnav__column">
                      <div class="subnav__content">
                        
                        
                          
                            <div class="subnav__header">
                              
                                <div class="subnav__title">Applied AI &amp; sciences</div>
                              
                              
                            </div>
                          
                        
                        <div class="subnav__links">
                        
                          
                          
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/google-earth-ai/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/earth_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="earth_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Earth AI</div>
                                    <div class="subnav__link-description small-text"></div>
                                  </div>
                                </a>
                              
                            
                              
                                <a class="subnav__link"
                                    href="/research-areas/health-ai/"
                                    
                                      
                                    >
                                  
                                    <div class="subnav__link-image subnav__link-image--small">
                                      <div class="block-icon">


  
  <div class="media-image-block no-light-mode-mobile no-dark-mode no-dark-mode-mobile has-default-media">
    
      
      
      



  
    
      
      
        <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/health_AI_nav.svg" class="image image--svg picture__image " loading="lazy"  alt="health_AI_nav">
      
      
    
  


      
    
  </div>

</div>
                                    </div>
                                  
                                  <div class="subnav__link-text">
                                    <div class="subnav__link-label caption">Health AI</div>
                                    <div class="subnav__link-description small-text"></div>
       