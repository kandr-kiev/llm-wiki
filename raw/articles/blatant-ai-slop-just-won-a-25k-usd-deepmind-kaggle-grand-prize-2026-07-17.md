---
source_url: https://www.kaggle.com/competitions/kaggle-measuring-agi/discussion/724918#3498423
ingested: 2026-07-17
sha256: 3ce7ce2b94a0d8618c6d21290d6d3beda44d550fd9289aa42a5cf10f228a5fc7
blog_source: Hacker News AI
---


<!DOCTYPE html>
<html lang="en">

<head>
  <title>Measuring Progress Toward AGI - Cognitive Abilities | Kaggle</title>
  <meta charset="utf-8" />
    <meta name="robots" content="index, follow" />
  <meta name="description" content="Design high-quality benchmarks that go beyond recall to evaluate how frontier models truly reason, act, and judge." />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, minimum-scale=1.0">
  <meta name="theme-color" content="#008ABC" />
  <script nonce="ythfc9PqVJVb/ENtHZkXeA==" type="text/javascript">
    window["pageRequestStartTime"] = 1784297166934;
    window["pageRequestEndTime"] = 1784297166946;
    window["initialPageLoadStartTime"] = new Date().getTime();
  </script>
  <script nonce="ythfc9PqVJVb/ENtHZkXeA==" id="gsi-client" src="https://accounts.google.com/gsi/client" async defer></script>
  <script nonce="ythfc9PqVJVb/ENtHZkXeA==">window.KAGGLE_JUPYTERLAB_PATH = "/static/assets/jupyterlab-v4/jupyterlab-index-1f1c38e4e7e48ccf.html";</script>
  <link rel="preconnect" href="https://www.google-analytics.com" crossorigin="anonymous" /><link rel="preconnect" href="https://stats.g.doubleclick.net" /><link rel="preconnect" href="https://storage.googleapis.com" /><link rel="preconnect" href="https://apis.google.com" />
    <link href="/static/images/favicon.ico" rel="shortcut icon" type="image/x-icon" id="dynamic-favicon" />
  <link rel="manifest" href="/static/json/manifest.json" crossorigin="use-credentials">


  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />

  <link href="https://fonts.googleapis.com/css?family=Inter:400,400i,500,500i,600,600i,700,700i&display=swap"
    rel="preload" as="style" />
  <link href="https://fonts.googleapis.com/css2?family=Google+Symbols:FILL@0..1&display=block"
    rel="preload" as="style" />
  <link href="https://fonts.googleapis.com/css?family=Inter:400,400i,500,500i,600,600i,700,700i&display=swap"
    rel="stylesheet" media="print" id="async-google-font-1" />
  <link href="https://fonts.googleapis.com/css2?family=Google+Symbols:FILL@0..1&display=block"
    rel="stylesheet" media="print" id="async-google-font-2" />
  <script nonce="ythfc9PqVJVb/ENtHZkXeA==" type="text/javascript">
    const styleSheetIds = ["async-google-font-1", "async-google-font-2"];
    styleSheetIds.forEach(function (id) {
      document.getElementById(id).addEventListener("load", function() {
        this.media = "all";
      });
    });
  </script>


    <link rel="stylesheet" type="text/css" href="/static/assets/app.css?v=a53f951c511cf82e" />

  
    
 
      <script nonce="ythfc9PqVJVb/ENtHZkXeA==">
        try{(function(a,s,y,n,c,h,i,d,e){d=s.createElement("style");
        d.appendChild(s.createTextNode(""));s.head.appendChild(d);d=d.sheet;
        y=y.map(x => d.insertRule(x + "{ opacity: 0 !important }"));
        h.start=1*new Date;h.end=i=function(){y.forEach(x => x<d.cssRules.length ? d.deleteRule(x) : {})};
        (a[n]=a[n]||[]).hide=h;setTimeout(function(){i();h.end=null},c);h.timeout=c;
        })(window,document,['.site-header-react__nav'],'dataLayer',2000,{'GTM-52LNT9S':true});}catch(ex){}
    </script>
    <script nonce="ythfc9PqVJVb/ENtHZkXeA==">
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());
        gtag('config', 'G-T7QHS60L4Q', {
            'optimize_id': 'GTM-52LNT9S',
            'displayFeaturesTask': null,
            'send_page_view': false,
            'content_group1': 'Competitions',
            'user_properties': {
                'logged_in': false,
            }
        });
    </script>
    <script nonce="ythfc9PqVJVb/ENtHZkXeA==" async src="https://www.googletagmanager.com/gtag/js?id=G-T7QHS60L4Q"></script>


  
    
    <meta property="og:title" content="Measuring Progress Toward AGI - Cognitive Abilities" />
    <meta property="og:description" content="Design high-quality benchmarks that go beyond recall to evaluate how frontier models truly reason, act, and judge." />
    <meta property="og:type" content="website"  />
    <meta property="og:url" content="https://kaggle.com/kaggle-measuring-agi" />

        <meta property="og:image" content="https://www.kaggle.com/open-graph/images/Competitions/128852" />
        <meta property="twitter:image" content="https://www.kaggle.com/open-graph/images/Competitions/128852" />
    <meta property="twitter:title" content="Measuring Progress Toward AGI - Cognitive Abilities" />
    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:site" content="@kaggle" />





  <meta name="twitter:site" content="@Kaggle" /> 
  
    

  
    

  
    



    <script nonce="ythfc9PqVJVb/ENtHZkXeA==">window['useKaggleAnalytics'] = true;</script>

  <script id="gapi-target" nonce="ythfc9PqVJVb/ENtHZkXeA==" src="https://apis.google.com/js/api.js" defer
    async></script>
  <script nonce="ythfc9PqVJVb/ENtHZkXeA==" src="/static/assets/runtime.js?v=df1cacb532e952e7"></script>
  <script nonce="ythfc9PqVJVb/ENtHZkXeA==" src="/static/assets/vendor.js?v=f97ba58231a7a93c"></script>
  <script nonce="ythfc9PqVJVb/ENtHZkXeA==" src="/static/assets/app.js?v=25c8b33fc3e01869"></script>
    <script nonce="ythfc9PqVJVb/ENtHZkXeA==" type="text/javascript">
      window.kaggleStackdriverConfig = {
        key: 'AIzaSyA4eNqUdRRskJsCZWVz-qL655Xa5JEMreE',
        projectId: 'kaggle-161607',
        service: 'web-fe',
        version: 'ci',
        userId: '0'
      }
    </script>
</head>
<body>
  <div id="root">
    










  </div>
</body>
</html>
