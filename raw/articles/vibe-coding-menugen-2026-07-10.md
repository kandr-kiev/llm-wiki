---

source_url: https://karpathy.bearblog.dev/vibe-coding-menugen/
ingested: 2026-07-10
sha256: 3123d10ddb3c481296b0f68ed101cd1d19b0c881b4bd12e1a85e6125b3e06843
blog_source: Andrej Karpathy
---

<!DOCTYPE html>
<html lang="en">

<!-- Powered by Bear Blog -->

<head>
  
  
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5">
  
  <title>Vibe coding MenuGen – karpathy</title>
  <link rel="canonical" href="https://karpathy.bearblog.dev/vibe-coding-menugen/">
  
    

    <meta name="karpathy" content="look-for-the-bear-necessities">
    <meta name="token" content="IiFpKQhBuJiZeNbhUqtN">

    
<!-- Primary Meta Tags -->
<meta name="title" content="Vibe coding MenuGen">
<meta name="description" content="Work log of vibe coding menugen app">

<!-- Open Graph / Facebook -->
<meta property="og:site_name" content="karpathy">
<meta property="og:title" content="Vibe coding MenuGen">
<meta property="og:type" content="article">
<meta property="og:url" content="https://karpathy.bearblog.dev/vibe-coding-menugen/">
<meta property="og:description" content="Work log of vibe coding menugen app">
<meta property="og:image" content="/static/og-image.png">


<!-- Twitter -->
<meta property="twitter:card" content="summary">
<meta property="twitter:url" content="https://karpathy.bearblog.dev/vibe-coding-menugen/">
<meta property="twitter:title" content="Vibe coding MenuGen">
<meta property="twitter:description" content="Work log of vibe coding menugen app">
<meta property="twitter:image" content="/static/og-image.png">



<!-- Microdata -->
<script type="application/ld+json">
  {
    "@context": "http://schema.org",
    "@type": "article",
    "name": "Vibe coding MenuGen",
    "headline": "Vibe coding MenuGen",
    "url": "https://karpathy.bearblog.dev/vibe-coding-menugen/",
    "description": "Work log of vibe coding menugen app",
    "image": "/static/og-image.png"
  }
</script>
    <link rel="alternate" type="application/atom+xml" href="/feed/" title="karpathy">
    <link rel="alternate" type="application/rss+xml" href="/feed/?type=rss" title="karpathy">

  
    

    
    
  
  
  
    
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
    

    

    
        <h1>Vibe coding MenuGen</h1>

        <p>
            <i>
                <time datetime="2025-04-27T12:00Z">
    27 Apr, 2025
</time>
            </i>
        </p>
    

    <p>Very often, I sit down at a restaurant, look through their menu, and feel... kind of stuck. What is Pâté again? What is a Tagine? Cavatappi... that's a pasta right? Sweetbread sounds delicious (I have a huge sweet tooth). It can get really out of hand sometimes. <em>"Confit tubers folded with matured curd and finished with a beurre noisette infusion."</em> okay so... what is this exactly? I've spent so much of my life googling pictures of foods that when the time came to attend a recent vibe coding hackathon, I knew it was the perfect opportunity to finally build the app I always wanted, but could nowhere find. And here it is in flesh, I call it... 🥁🥁🥁 ... <strong>MenuGen</strong>:</p>
<p><img src="https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/02pm.webp" alt="Screenshot 2025-04-26 at 1" /></p>
<p>MenuGen is super simple. You take a picture of a menu and it generates images for all the menu items. It visualizes the menu. Obviously it's not <em>exactly</em> what you will be served in that specific restaurant, but it gives you the basic idea: Some of these dishes are salads, this is a fish, this is a soup, etc. I found it so helpful in my personal use that after the hackathon (where I got the first version to work on localhost) I continued vibe coding a bit to deploy it, add authentication, payments, and generally make it real. So here it is, give it a shot the next time you go out :): <a href='https://www.menugen.app/'>menugen.app</a>!</p>
<p>MenuGen is my first end-to-end vibe coded app, where I (someone who tinkers but has little to no actual web development experience) went from scratch all the way to a real product that people can sign up for, pay for, get utility out of, and where I pocket some good and honest 10% markup. It's pretty cool. But in addition to the utility of the app, MenuGen was interesting to me as an exploration of vibe coding apps and how feasible it is today. As such, I did not write any code directly; 100% of the code was written by Cursor+Claude and I basically don't really know how MenuGen works in the conventional sense that I am used to. So now that the project is "done" (as in the first version seems to work), I wanted to write up this quick post on my experience - what it looks like today for a non-webdev to vibe code a web app.</p>
<p><strong>First, local version</strong>. In what is a relatively common experience in vibe coding, the very first prototype of the app running on my local machine took very little time. I took Cursor + Claude 3.7, I gave it the description of the app, and it wrote all the React frontend components very quickly, laying out a beautiful web page with smooth, multicolored fonts, little CSS animations, responsive design and all that, except for the actual backend functionality. Seeing a new website materialize so quickly is a strong hook. I felt like I was 80% done but (foreshadowing...) it was a bit closer to 20%.</p>
<p><strong>OpenAI API</strong>. Around here is where some of the troubles started. I needed to call OpenAI APIs to OCR the menu items from the image. I had to get the OpenAI API keys. I had to navigate slightly convoluted menus asking me about "projects" and detailed permissions. Claude kept hallucinating deprecated APIs, model names, and input/output conventions that have all changed recently, which was confusing, but it resolved them after I copy pasted the docs back and forth for a while. Once the individual API calls were working, I immediately ran into some heavy rate limiting of the API calls, allowing me to only issue a few queries every 10 minutes.</p>
<p><strong>Replicate API</strong>. Next, I needed to generate images given the descriptions. I signed up for a new Replicate API key and ran into similar issues relatively quickly. My queries didn't work because LLM knowledge was deprecated, but in addition, this time even the official docs were a little bit out of date due to recent changes in the API, which now don't return the JSON directly but instead some kind of a Streaming object that neither I or Claude understood. I then faced rate limiting on the API so it was difficult to debug the app. I was told later that these are common protection measures by these services to mitigate fraud, but they also make it harder to get started with new, legitimate accounts. I'm told Replicate is moving to a different approach where you pre-purchase credits, which might help going forward.</p>
<p><strong>Vercel deploy</strong>. At this point at least, the app was working locally so I was quite happy. It was time to deploy the basic first version. Sign up for Vercel, add project, configure it, point it at my GitHub repo, push to master, watch a new Deployment build and... ERROR. The logs showed some linting errors due to unused variables and other basic things like that, but it was hard to understand or debug because everything worked fine on local and only broke on Vercel build, so I debugged the issues by pushing fake debugging commits to master to force redeploys. Once I fixed these issues, the site still refused to work. I asked Claude. I asked ChatGPT. I consulted docs. I googled around. 1 hour later I finally realized my silly mistake - My <code>.env.local</code> file stored the API keys to OpenAI and Replicate, but this file is (correctly!) part of <code>.gitignore</code> and doesn't get pushed to git, so you have to manually navigate to Vercel project settings, find the right place, and add your environment keys manually. I kind of understood the issue relatively quickly, but I could see an aspiring vibe coder get stuck on this for a while. Once the deployment finally succeeded, Vercel happily offered a URL. This surprised me again because my project was a private git repo that was not ready to see the light of day. I didn't realize that Vercel will take your <em>!private!</em> repo of an unfinished project and auto-deploy it on a totally public and easy to guess url just like that, hah.</p>
<p><strong>Clerk authentication</strong>. Claude suggested that we use Clerk for authentication, so I went along with it. Signed up for Clerk, configured the project, got my API keys. At this point Claude hallucinated about 1000 lines of code that appeared to be deprecated Clerk APIs. I had to copy paste a lot of the docs back and forth to get things gradually unstuck. Next, so far, Clerk was running in a "Development" deployment. To move to a "Production" deployment, there were more hoops to jump through. Clerk demands that you host your app on a custom domain that you own. <code>menugen.vercel.com</code> will not work. So I had to purchase the domain name <a href=''>menugen.app</a>. Then I had to wire the domain to my Vercel project. Then I had to change the DNS records. Then I had to pick an OAuth provider, e.g. I went with Google. But to do that was its own <a href='https://clerk.com/docs/authentication/social-connections/google'>configuration adventure</a> . I had to enable an "SSO connection". I had to go over to Google Cloud Console and create a new project, and add a new OAuth Credential. I had to wait some time for an approval process around here. I then had to go back and forth between the nested settings of all of Vercel, Clerk and Google for a while to wire it up properly. I thought of quitting the project around here, but I felt better when I woke up the next morning.</p>
<p><strong>Stripe payments</strong>. Next I wanted to add payments so that people can purchase credits. This means another website, another account, more docs, more keys. I select "Next.js" as the backend, copy paste the very first snippet of code from the "getting started" docs into my app and... ERROR. I realized later that Stripe gives you JavaScript code when you select Next.js, but my app is built in TypeScript, so every time I pasted a snippet of code it made Cursor unhappy with linter errors, but Claude patched things up ok over time after I told it to "fix errors" a few times and after I threatened to switch to ChatGPT. Then back in the Stripe dashboard we create a Product, we create a Price, we find the price key (not the product key!), copy paste all the keys around. Around here, I caught Claude using a really bad idea approach to match up a successful Stripe payment to user credits (it tried to match up the email addresses, but the email the user might give in the Stripe checkout may not be the email of the Google account they signed up with, so the user might not actually get the credits that they purchased). I point this out to Claude and it immediately apologizes and rewrites it correctly by passing around unique user ids in the request metadata. It thanks me for pointing out the issue and tells me that it will do it correctly in the future, which I know is just gaslighting. But since our quick test works, only a few more clicks to upgrade the deployment from Development to Production, now re-do a new Product, redo a new Price, re-copy paste all the keys and ids, locally and in the Vercel settings... and then it worked :)</p>
<p><strong>Database? Work queues?</strong> So far, all of the processing is done "in the moment" - it's just requests and results right there and then, nothing is cached, saved, or etc. So the results are ephemeral and if the response takes too long (e.g. because the menu is too long and has too many items, or because the APIs show too much latency), the request can time out and break. If you refresh the page, everything is gone too. The correct way to do this is to have a database where we register and keep track of work, and the client just displays the latest state as it's ready. I realized I'd have to connect a database from the Marketplace, something like Supabase PostgreSQL (even when Claude pitched me on using Vercel KV, which I know is actually deprecated). And then we'd also need some queue service like Upstash or so to run the actual processing. It would mean more services. More logins. More API keys. More configurations. More docs. More suffering. It was too much bear. Leave as future work.</p>
<p><strong>TLDR</strong>. Vibe coding menugen was exhilarating and fun escapade as a local demo, but a bit of a painful slog as a deployed, real app. Building a modern app is a bit like assembling IKEA future. There are all these services, docs, API keys, configurations, dev/prod deployments, team and security features, rate limits, pricing tiers... Meanwhile the LLMs have slightly outdated knowledge of everything, they make subtle but critical design mistakes when you watch them closely, and sometimes they hallucinate or gaslight you about solutions. But the most interesting part to me was that I didn't even spend all that much work in the code editor itself. I spent most of it in the browser, moving between tabs and settings and configuring and gluing a monster. All of this work and state is not even accessible or manipulatable by an LLM - how are we supposed to be automating society by 2027 like this?</p>
<p><strong>Going forward</strong>. As an exploration of what it's like to vibe code an app today if you have little to no web dev background, I'm left with an equal mix of amazement (it's actually possible and much easier/faster than what was possible before!) and a bit of frustration of what could be. Part of the pain of course is that none of this infrastructure was really designed to be used like this. The intended target audience are teams of professional web developers living in a pre-LLM world. Not vibe coding solo devs prototyping apps. Some thoughts on solutions that could make super simple apps like MenuGen a lot easier to create:</p>
<ul>
<li>Some app development platform could come with all the batteries included. Something that looks like the opposite of Vercel Marketplace. Something opinionated, concrete, preconfigured with all the basics that everyone wants: domain, hosting, authentication, payments, database, server functions. If some service made these easy and "just work" out of the box, it could be amazing.</li>
<li>All of these services could become more LLM friendly. Everything you tell the user will be basically right away copy pasted to an LLM, so you might as well talk directly to the LLM. Your service could have a CLI tool. The backend could be configured with curl commands. The docs could be Markdown. All of these are ergonomically a lot friendlier surfaces and abstractions for an LLM. Don't talk to a developer. Don't ask a developer to visit, look, or click. Instruct and empower their LLM.</li>
<li>For my next app I'm considering rolling with basic HTML/CSS/JS + Python backend (FastAPI + Fly.io style or so?), something a lot simpler than the serverless multiverse of "modern web development". It's possible that a simple app like MenuGen (or apps like it) could have been significantly easier in that paradigm.</li>
<li>Finally, it's quite likely that MenuGen shouldn't be a full-featured app at all. The "app" is simply one call to GPT to OCR a menu, and then a for loop over results to generate the images for each item and present them nicely to the user. This almost sounds like a simple custom GPT (in the terminology of the original GPT "app store" that OpenAI released earlier). Could MenuGen be just a prompt? Could the LLM respond not with text but with a simple webpage to present the results, along the lines of Artifacts? Could many other apps look like this too? Could I publish it as an app on a store and earn markup in the same way?</li>
</ul>
<p>For now, I'm pretty happy to have vibe coded my first super custom app through the finish line of something that is real, solves a need I've had for a long time, and is shareable with friends. Thank you to all the services above that I've used to build it. In principle, it could earn some $ if others like it too, in a completely passive way - the <a href='https://x.com/levelsio'>@levelsio</a> dream. Ultimately, vibe coding full web apps today is kind of messy and not a good idea for anything of actual importance. But there are clear hints of greatness and I think the industry just needs a bit of time to adapt to the new world of LLMs. I'm personally quite excited to see the barrier to app drop to ~zero, where anyone could build and publish an app just as easily as they can make a TikTok. These kinds of hyper-custom automations could become a beautiful new canvas for human creativity.</p>
<p>The companion tweet (and the "comments section") is on my X <a href='https://x.com/karpathy/status/1917961248031080455'>@karpathy</a>.</p>


    

    
        

        
            <form id="upvote-form" action="/upvote/" method="post" style="display: inline">
    <small>
        <input hidden name="uid" value="IiFpKQhBuJiZeNbhUqtN" style="display:none">
        <input hidden name="title" value="Vibe coding MenuGen" style="display:none">

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

    fetch('/upvote-info/IiFpKQhBuJiZeNbhUqtN/').then(response => response.json()).then(data => {
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
                            token: "IiFpKQhBuJiZeNbhUqtN",
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
