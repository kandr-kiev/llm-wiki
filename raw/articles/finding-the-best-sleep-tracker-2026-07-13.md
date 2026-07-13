---
source_url: https://karpathy.bearblog.dev/finding-the-best-sleep-tracker/
ingested: 2026-07-13
sha256: 70d713261393e6aede745a5c533729f705c2609c8c1f29158e8afbc32649d232
blog_source: Andrej Karpathy
---
<!DOCTYPE html>
<html lang="en">

<!-- Powered by Bear Blog -->

<head>
  
  
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5">
  
  <title>Finding the Best Sleep Tracker – karpathy</title>
  <link rel="canonical" href="https://karpathy.bearblog.dev/finding-the-best-sleep-tracker/">
  
    

    <meta name="karpathy" content="look-for-the-bear-necessities">
    <meta name="token" content="bVsUXHsaTHIRymMzTkhI">

    
<!-- Primary Meta Tags -->
<meta name="title" content="Finding the Best Sleep Tracker">
<meta name="description" content="Finding the best sleep tracker with data">

<!-- Open Graph / Facebook -->
<meta property="og:site_name" content="karpathy">
<meta property="og:title" content="Finding the Best Sleep Tracker">
<meta property="og:type" content="article">
<meta property="og:url" content="https://karpathy.bearblog.dev/finding-the-best-sleep-tracker/">
<meta property="og:description" content="Finding the best sleep tracker with data">
<meta property="og:image" content="/static/og-image.png">


<!-- Twitter -->
<meta property="twitter:card" content="summary">
<meta property="twitter:url" content="https://karpathy.bearblog.dev/finding-the-best-sleep-tracker/">
<meta property="twitter:title" content="Finding the Best Sleep Tracker">
<meta property="twitter:description" content="Finding the best sleep tracker with data">
<meta property="twitter:image" content="/static/og-image.png">



<!-- Microdata -->
<script type="application/ld+json">
  {
    "@context": "http://schema.org",
    "@type": "article",
    "name": "Finding the Best Sleep Tracker",
    "headline": "Finding the Best Sleep Tracker",
    "url": "https://karpathy.bearblog.dev/finding-the-best-sleep-tracker/",
    "description": "Finding the best sleep tracker with data",
    "image": "/static/og-image.png"
  }
</script>
    <link rel="alternate" type="application/atom+xml" href="/feed/" title="karpathy">
    <link rel="alternate" type="application/rss+xml" href="/feed/?type=rss" title="karpathy">

  
    

    
    <style>pre { line-height: 125%; }
td.linenos .normal { color: #666666; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: #666666; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.highlight .hll { background-color: #ffffcc }
.highlight { background: #f0f0f0; }
.highlight .c { color: #60A0B0; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #F00 } /* Error */
.highlight .k { color: #007020; font-weight: bold } /* Keyword */
.highlight .o { color: #666 } /* Operator */
.highlight .ch { color: #60A0B0; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #60A0B0; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #007020 } /* Comment.Preproc */
.highlight .cpf { color: #60A0B0; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #60A0B0; font-style: italic } /* Comment.Single */
.highlight .cs { color: #60A0B0; background-color: #FFF0F0 } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .ges { font-weight: bold; font-style: italic } /* Generic.EmphStrong */
.highlight .gr { color: #F00 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888 } /* Generic.Output */
.highlight .gp { color: #C65D09; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #04D } /* Generic.Traceback */
.highlight .kc { color: #007020; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #007020; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #007020; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #007020 } /* Keyword.Pseudo */
.highlight .kr { color: #007020; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #902000 } /* Keyword.Type */
.highlight .m { color: #40A070 } /* Literal.Number */
.highlight .s { color: #4070A0 } /* Literal.String */
.highlight .na { color: #4070A0 } /* Name.Attribute */
.highlight .nb { color: #007020 } /* Name.Builtin */
.highlight .nc { color: #0E84B5; font-weight: bold } /* Name.Class */
.highlight .no { color: #60ADD5 } /* Name.Constant */
.highlight .nd { color: #555; font-weight: bold } /* Name.Decorator */
.highlight .ni { color: #D55537; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #007020 } /* Name.Exception */
.highlight .nf { color: #06287E } /* Name.Function */
.highlight .nl { color: #002070; font-weight: bold } /* Name.Label */
.highlight .nn { color: #0E84B5; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #062873; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #BB60D5 } /* Name.Variable */
.highlight .ow { color: #007020; font-weight: bold } /* Operator.Word */
.highlight .w { color: #BBB } /* Text.Whitespace */
.highlight .mb { color: #40A070 } /* Literal.Number.Bin */
.highlight .mf { color: #40A070 } /* Literal.Number.Float */
.highlight .mh { color: #40A070 } /* Literal.Number.Hex */
.highlight .mi { color: #40A070 } /* Literal.Number.Integer */
.highlight .mo { color: #40A070 } /* Literal.Number.Oct */
.highlight .sa { color: #4070A0 } /* Literal.String.Affix */
.highlight .sb { color: #4070A0 } /* Literal.String.Backtick */
.highlight .sc { color: #4070A0 } /* Literal.String.Char */
.highlight .dl { color: #4070A0 } /* Literal.String.Delimiter */
.highlight .sd { color: #4070A0; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #4070A0 } /* Literal.String.Double */
.highlight .se { color: #4070A0; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #4070A0 } /* Literal.String.Heredoc */
.highlight .si { color: #70A0D0; font-style: italic } /* Literal.String.Interpol */
.highlight .sx { color: #C65D09 } /* Literal.String.Other */
.highlight .sr { color: #235388 } /* Literal.String.Regex */
.highlight .s1 { color: #4070A0 } /* Literal.String.Single */
.highlight .ss { color: #517918 } /* Literal.String.Symbol */
.highlight .bp { color: #007020 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #06287E } /* Name.Function.Magic */
.highlight .vc { color: #BB60D5 } /* Name.Variable.Class */
.highlight .vg { color: #BB60D5 } /* Name.Variable.Global */
.highlight .vi { color: #BB60D5 } /* Name.Variable.Instance */
.highlight .vm { color: #BB60D5 } /* Name.Variable.Magic */
.highlight .il { color: #40A070 } /* Literal.Number.Integer.Long */
</style>
  
  
  
    
        <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20100%20100'%3E%3Ctext%20y='.9em'%20font-size='90'%3E🤖%3C/text%3E%3C/svg%3E">
    



  <style data-name="default">
      
      
    
:root {
    --width: 720px;
    --font-main: Verdana, sans-serif;
    --font-secondary: Verdana, sans-serif;
    --font-scale: 1em;
    --background-color: #fff;
    --heading-color: #222;
    --text-color: #444;
    --link-color: #3273dc;
    --visited-color:  #8b6fcb;
    --code-background-color: #f2f2f2;
    --code-color: #222;
    --blockquote-color: #222;
}

@media (prefers-color-scheme: dark) {
    :root {
        --background-color: #01242e;
        --heading-color: #eee;
        --text-color: #ddd;
        --link-color: #8cc2dd;
        --visited-color:  #8b6fcb;
        --code-background-color: #000;
        --code-color: #ddd;
        --blockquote-color: #ccc;
    }
}

body {
    font-family: var(--font-secondary);
    font-size: var(--font-scale);
    margin: auto;
    padding: 20px;
    max-width: var(--width);
    text-align: left;
    background-color: var(--background-color);
    word-wrap: break-word;
    overflow-wrap: break-word;
    line-height: 1.5;
    color: var(--text-color);
}

h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-main);
    color: var(--heading-color);
}

a {
    color: var(--link-color);
    cursor: pointer;
    text-decoration: none;
}

a:hover {
    text-decoration: underline; 
}

nav a {
    margin-right: 8px;
}

strong, b {
    color: var(--heading-color);
}

button {
    margin: 0;
    cursor: pointer;
}

time {
 	font-family: monospace;
  	font-style: normal;
  	font-size: 15px;
}

main {
    line-height: 1.6;
}

table {
    width: 100%;
}

hr {
    border: 0;
    border-top: 1px dashed;
}

img {
    max-width: 100%;
}

code {
    font-family: monospace;
    padding: 2px;
    background-color: var(--code-background-color);
    color: var(--code-color);
    border-radius: 3px;
}

blockquote {
    border-left: 1px solid #999;
    color: var(--code-color);
    padding-left: 20px;
    font-style: italic;
}

footer {
    padding: 25px 0;
    text-align: center;
}

.title:hover {
    text-decoration: none;
}

.title h1 {
    font-size: 1.5em;
}

.inline {
    width: auto !important;
}

.highlight, .code {
    padding: 1px 15px;
    background-color: var(--code-background-color);
    color: var(--code-color);
    border-radius: 3px;
    margin-block-start: 1em;
    margin-block-end: 1em;
    overflow-x: auto;
}

/* blog post list */
ul.blog-posts {
    list-style-type: none;
    padding: unset;
}

ul.blog-posts li {
    display: flex;
}

ul.blog-posts li span {
    flex: 0 0 130px;
}

ul.blog-posts li a:visited {
    color: var(--visited-color);
}

sub {
	display: block;
	font-style: italic;
}
    .upvote-button {
        padding: 0;
        margin: 0;
        border: 0;
        background-color: inherit;
        color: inherit;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .upvote-button.upvoted {
        color: salmon;
    }
    .upvote-count {
        margin-top: -3px;
    }

      
  </style>
</head>

<body class="post " onload="(function() { document.cookie = `timezone=${Intl.DateTimeFormat().resolvedOptions().timeZone};path=/`; })()">
  
  <header>
    <a class="title" href="/">
      <h1>
        karpathy
      </h1>
    </a>
    <nav>
      <p><a href='/'>Home</a> <a href='/blog/'>Blog</a></p>

    </nav>
  </header>
  <main>
    

    

    
        <h1>Finding the Best Sleep Tracker</h1>

        <p>
            <i>
                <time datetime="2025-03-24T23:00Z">
    24 Mar, 2025
</time>
            </i>
        </p>
    

    <p>About 2 months ago I stumbled by this Bryan Johnson video on <a href='https://www.youtube.com/watch?v=Wk9p3dhMYdk'>How I FIXED My Terrible Sleep - 10 Habits</a>. I resolved that day to listen to Bryan and try to improve my sleep. But before we can improve it, first - how should we measure it? Bryan Johnson seems to use <a href='https://www.whoop.com/us/en/'>Whoop</a>, but at that time I only had my Apple Watch (coupled with one of the popular sleep apps - <a href='https://apps.apple.com/us/app/autosleep-track-sleep-on-watch/id1164801111'>AutoSleep</a>). And then a long time ago I used and liked <a href='https://ouraring.com/'>Oura</a>. And I also had an order in for the new and fancy <a href='https://www.eightsleep.com/'>8Sleep Pod 4 Ultra</a>, which I was aware offers some sleep tracking too. So I found myself in a bit of a pickle - which one should I pick to track my sleep? And the answer of course is... to initiate a comprehensive tracking project to compare the 4 major candidates and find the. best. sleep. tracker. So that's what I did. This is me fully geared up and ready for bed:</p>
<p><img src="https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/sleep_edit.webp" alt="sleep_edit" /></p>
<p>I've now gathered roughly 2 months of data. I kept the raw data in a simple spreadsheet, recording some of the basic measurements: the amount of sleep (Light, REM, Deep, and Awake tossing and turning), heart rate measurements (Resting Heart Rate (RHR), Heart Rate Variability (HRV)), and the sleep Score offered by each app. I'd log these every day right when I wake up so that I can compare and contrast the numbers and relate them to how I felt that morning. You can find my <a href='https://docs.google.com/spreadsheets/d/1mJeKtLuDE9hOuc2e_WjfaP1sds22k_sO2foIvSZLohw/edit?usp=sharing'>raw data in this spreadsheet</a>, it looks like this:</p>
<p><img src="https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/sleep_data.webp" alt="sleep_data" /></p>
<p><strong>Qualitative assessment</strong>. Now, to spare you some suspense, after 2 months of data collection and staring at the results basically every morning, it was very pretty easy to guess that Oura and Whoop are both "Tier 1" - fairly similar and quite high quality in their sleep tracking. They both give similar scores that also correlated with the way I felt in the morning <em>most of the time</em>. Next is 8Sleep, which is ok. And finally, I was sad to learn that Apple Watch + AutoSleep (which I had used in the past for many months) was really, really terrible. Its scores are basically almost random and they swing around wildly, with little correlation to how I felt in the morning in comparison.</p>
<p>Let's now look at some of the data. First, let's look at the values that all 4 signals take on over the 2 months, with their histograms:</p>
<p><img src="https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/signals.webp" alt="signals" /></p>
<p>As we can see, AutoSleep and 8Sleep are way too easy to please, giving out really high scores and pushing against the 100 score boundary. Whoop is also a little too easy to please, giving out 100 scores. Oura is the most difficult to please, shows a relatively nice gaussian distribution of scores, and offering the most dynamic range. I take this to be a good and nice property of Oura. Indeed, after 2 months my highest ever score on Oura was 92, while I can get 100 on Whoop fairly regularly. This means that I can keep going and striving for even more optimal sleep, one day.</p>
<p>Next, I was very curious about the correlation analysis between the trackers. We take all the scores and plot pairwise correlation scatter plots to see which of the trackers "agree the most" with each other. Here it is:</p>
<p><img src="https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/corr.webp" alt="corr" /></p>
<p>And here are the correlations sorted:</p>
<div class="highlight"><pre><span></span>Whoop vs Oura: 0.65
Oura vs 8Sleep: 0.59
Oura vs AutoSleep: 0.47
8Sleep vs AutoSleep: 0.42
Whoop vs 8Sleep: 0.38
Whoop vs AutoSleep: 0.14
</pre></div>
<p>Whoop and Oura seem to enjoy the highest correlation at ~0.65, while the other trackers are a bit all over the place. In particular, Whoop and AutoSleep are almost uncorrelated (0.14!). If we think that Whoop is good (which I think it is), AutoSleep looks almost like a noise generator.</p>
<p><strong>Matters of Heart Rate</strong>. Next, I was interested to look at the Resting Heart Rate (RHR) and Heart Rate Variability (HRV). First, all trackers except 8Sleep agree quite highly on the heart rate during the night, including the Apple Watch. 8 Sleep is the worst because... it's a mattress so it doesn't have a direct measurement of the heart rate. I'm actually a bit impressed that it has a correlation this high:</p>
<div class="highlight"><pre><span></span>           AutoSleep    8Sleep      Oura     Whoop
AutoSleep   1.000000  0.947151  0.908987  0.942587
8Sleep      0.947151  1.000000  0.947977  0.878552
Oura        0.908987  0.947977  1.000000  0.904023
Whoop       0.942587  0.878552  0.904023  1.000000
</pre></div>
<p>Having established that all 3 devices (Oura, Whoop, AutoSleep) give a good and consistent measurement of resting heart rate during the night, I was curious if there is a correlation with the sleep score, as this is something Bryan mentioned a few times in his videos. In other words, is a lower RHR associated with better sleep score? Keep in mind that this is just correlation analysis, indeed, I have no idea if the apps take RHR as one of the measurements when they calculate the sleep score. For Whoop, it seems like there is a tiny bit of a correlation, i.e. lower RHR comes with higher sleep score (~0.13).</p>
<p><img src="https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/whoopcorr.webp" alt="whoopcorr" /></p>
<p>But for Oura there is none:</p>
<p><img src="https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/ouracorr.webp" alt="ouracorr" /></p>
<p>So... I'm not sure what to make of this. Going in, I thought that lower RHR would correlate quite well to better score but this doesn't seem to be the case.</p>
<p>Lastly, during the 2 months of data collection I was exercising regularly, getting about 30 minutes on average of Zone 2 cardio every day, except twice a week also doing a 4x4x4 HIIT (4 min off, 4 min on, 4 times). I was curious if this showed up and indeed it seems like it does, pretty cool:</p>
<p><img src="https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/improvement.webp" alt="improvement" /></p>
<p>Using Whoop-Oura average measurement of both RHR and HRV, my resting heart rate has improved (decreased) by a bit less than 3 bpm over the duration of these 60 days (from ~51 bpm -> 48 ~bpm), which is awesome. In addition, my HRV has also improved (increased), (from ~49 -> 54). I love to see exercise adaptations in the data. For some unknown reason, notice also that the HRV values from Whoop seem to be inflated above those of Oura by about 5. I'm not exactly sure why, possibly they calculate it differently... but it's a bit surprising and unexplained.</p>
<p>Lastly, over the duration of 2 months I tried to improve my sleep quality, but it's all mixed up with a bunch of random events, parties, injuries, and also random experiments I tried to run here and there. As another example, my last week was rough because I was obsessed with a technical problem and couldn't sleep well. So unfortunately, overall, I am not seeing a dramatic increase in my sleep quality just yet. But I see this as a long-term project and I hope to increase these scores on average over the duration of the year. Maybe if squint hard enough my sleep has improved a tiny amount (?), but let's face it this is cope hah:</p>
<p><img src="https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/sleepovertime.webp" alt="sleepovertime" /></p>
<p><strong>Yes, sleep matters</strong>. Overall, I will say with absolute certainty that Bryan is basically right, and my sleep scores correlate strongly with the quality of work I am able to do that day. When my score is low, I lack agency, I lack courage, I lack creativity, I'm simply tired. When my sleep score is high, I can power through anything. On my best days, I can sit down and work through 14 hours and barely notice the passage of time. It's not subtle. The effects are not a function of a single day's sleep but of the accumulated sleep debt over a duration of last few days. So in other words a single bad night is usually ok. But a few in a row is bad news. And vice versa. Listen to Bryan.</p>
<p><strong>Shopping recommendations</strong>. Finally, I wanted to close with some recommendations to others who might want to undertake sleep tracking and improve their sleep.</p>
<ul>
<li><p>Oura is Tier 1 / super solid tracker. The app is excellent and I love the single "overview pane" with all the data about that sleep (Whoop needs a lot more clicking around the app). I love that Oura score doesn't saturate that easily, that its scores are a gaussian, and that it has dynamic range. Unfortunately, I find the ring form factor quite inconvenient because it's a little thick, and fingers are used extensively (e.g. hand washing, food preparation, etc.) When I go to the gym, I find myself removing the ring often because it interferes with my grip strength, and it could get scratched. The ring has to be sized correctly and your finger changes its size. Sometimes it's a little too snug, sometimes a little too loose. The ring also has to be rotated correctly for the best results (the notch has to be down), so you'll keep finding it rotated wrong and correcting it. I also don't love having to take the ring on and off to charge it.</p>
</li>
<li><p>Whoop is also a Tier 1 / super solid tracker. The app is excellent. It can be a bit overwhelming at first and requires quite a bit of moving around, but it is very comprehensive, full-featured and customizable, more than Oura. It also has a pretty neat and useful LLM integration. I also really like the Community feature, though it is severely undercooked, under-designed, and feels orphaned. I think Oura has a better "grand overview" page for a single dense summary of one night of sleep. I don't like that Whoop saturates at 100 fairly easily. I find that Whoop is significantly better when it comes to the form factor. Having the tracker on your wrist is just so significantly easier and less intrusive into your daily life. In addition, you never have to take it off because the charger attaches on and off onto it!</p>
</li>
<li><p>I didn't find 8Sleep to be very reliable in its sleep tracking. The scores don't make as much sense to me when I wake up, and as we saw above they don't correlate very strongly with Whoop or Oura.</p>
</li>
<li><p>AutoSleep is basically a random number generator. Maybe there is a better app on Apple Watch for sleep tracking, but I haven't found it. Do not use.</p>
</li>
</ul>
<p><img src="https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/apps.webp" alt="apps" /></p>
<p>Above: The 4 apps. Left to right: <strong>Oura</strong> - I love this "grand overview" summary page, it's dense with just the info you want, and it's super easy to swipe left/right for other days. <strong>Whoop</strong> - less dense, you have to move around a lot to "treasure hunt" the information you want. <strong>8Sleep</strong> - pretty decent. <strong>AutoSleep</strong> - looks cool but the numbers are all wrong so <code>¯\(ツ)/¯</code>.</p>
<p>Summarizing all of that into my advice right now: Get Whoop for 9.5/10, reliable, convenient sleep tracking with an excellent app (once you get to know it a bit). Get Oura for 10/10 tracking, if you're ok with the ring form factor.</p>
<p>Did I skip your favorite obviously best sleep tracker? Let me know on X <a href='https://x.com/karpathy'>@karpathy</a>.</p>


    

    
        

        
            <form id="upvote-form" action="/upvote/" method="post" style="display: inline">
    <small>
        <input hidden name="uid" value="bVsUXHsaTHIRymMzTkhI" style="display:none">
        <input hidden name="title" value="Finding the Best Sleep Tracker" style="display:none">

        <button
            class="upvote-button"
            aria-label="Toast this post"
            title="Toast this post"
        >
            <svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1">
                <polyline points="17 11 12 6 7 11"></polyline>
                <polyline points="17 18 12 13 7 18"></polyline>
            </svg>
            <small class="upvote-count" aria-hidden="true">&nbsp;</small>
        </button>
    </small>        
</form>

<script>
    const $upvoteButton = document.querySelector('.upvote-button');
    const $upvoteCount =  document.querySelector('.upvote-count')

    fetch('/upvote-info/bVsUXHsaTHIRymMzTkhI/').then(response => response.json()).then(data => {
        $upvoteCount.innerText = data.upvote_count;
        if (data.upvoted) {
            $upvoteButton.disabled = true
            $upvoteButton.style.color = "salmon"
            $upvoteButton.ariaLabel = "Toasted"
            $upvoteButton.title = "Toasted"
        }
        $upvoteButton.ariaLabel += ` (${data.upvote_count})`
    });

    let moved = false;
    let pageLoaded = Date.now();

    document.addEventListener('touchmove', () => moved = true);
    document.addEventListener('mousemove', () => moved = true);

    document.querySelector('#upvote-form').addEventListener('submit', (e) => {
        e.preventDefault();

        if (moved) {
            document.querySelector('input[name="title"]').value = "";
        }
        if (Date.now() - pageLoaded < 2000 || !moved) {
            return;
        }

        fetch(e.target.action, {
            method: 'post',
            body: new FormData(e.target),
        });
        
        $upvoteButton.disabled = true
        $upvoteButton.style.color = "salmon"
        $upvoteButton.ariaLabel = "Toasted"
        $upvoteButton.title = "Toasted"
        const newUpvoteCount = `${(parseInt($upvoteCount.innerHTML.split(" ")[0]) + 1)}`
        $upvoteCount.innerHTML = newUpvoteCount
        $upvoteButton.ariaLabel += ` (${newUpvoteCount})`
    });
</script>
        

        
            <script>
            window.addEventListener("load", () => {
                if (navigator.webdriver !== true) {
                    const sendHit = score => {
                        const params = new URLSearchParams({
                            blog: "karpathy",
                            token: "bVsUXHsaTHIRymMzTkhI",
                            referrer: document.referrer.includes("karpathy.bearblog.dev") ? "" : document.referrer,
                            title: "",
                            score: score
                        });
                        new Image().src = `/hit/?${params.toString()}`;
                    };

                    document.addEventListener('touchmove', () => sendHit(100), { once: true });
                    document.addEventListener('mousemove', () => sendHit(100), { once: true });
                }
            });
            </script>
        
    


  </main>
  <footer>
    
    
    <span>
        Powered by <a href="https://bearblog.dev">Bear <span role="img" class="bear" aria-label="ASCII bear logo">ʕ•ᴥ•ʔ</span></a>
    </span>

  </footer>

  
  <script>
        (() => {
          "use strict";
          const times = document.querySelectorAll('time');
          const format_string = "d M, Y" || "d M, Y"

          times.forEach(time => {
              time.innerText = formatDate(time.dateTime, format_string)
          });

          function formatDate(dateStr, formatStr) {
            const date = new Date(dateStr);
            const day = date.getDate();
            const month = date.getMonth();
            const year = date.getFullYear();
            const weekday = date.getDay();
            const hours = date.getHours();
            const minutes = date.getMinutes();
            const monthsFull = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
            const monthsShort = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
            const daysFull = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
            const daysShort = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
            
            function getOrdinal(n) {
                const s = ['th', 'st', 'nd', 'rd'];
                const v = n % 100;
                return s[(v - 20) % 10] || s[v] || s[0];
            }
            
            const map = {
                'd': () => day.toString().padStart(2, '0'),
                'm': () => (month + 1).toString().padStart(2, '0'),
                'Y': () => year.toString(),
                'y': () => year.toString().slice(-2),
                'F': () => monthsFull[month],
                'j': () => day.toString(),
                'D': () => daysShort[weekday],
                'l': () => daysFull[weekday],
                'S': () => getOrdinal(day),
                'M': () => monthsShort[month],
                'H': () => hours.toString().padStart(2, '0'),
                'h': () => {
                    let h = hours % 12;
                    h = h === 0 ? 12 : h;
                    return h.toString().padStart(2, '0');
                },
                'g': () => {
                    let h = hours % 12;
                    return h === 0 ? '12' : h.toString();
                },
                'i': () => minutes.toString().padStart(2, '0'),
                'a': () => hours < 12 ? 'am' : 'pm',
                'A': () => hours < 12 ? 'AM' : 'PM',
            };
            
            let result = '';
            for (let char of formatStr) {
                result += map[char] ? map[char]() : char;
            }
            return result;
        }
        })();
    </script>
    
</body>
<!-- ID: karpathy -->
<!-- 🐻 -->
</html>
