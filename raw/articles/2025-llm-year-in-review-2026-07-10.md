---

source_url: https://karpathy.bearblog.dev/year-in-review-2025/
ingested: 2026-07-10
sha256: 649cde175f0a85eadb917559693285234a9d3bbf26d734ce5064829fba18d18f
blog_source: Andrej Karpathy
---

<!DOCTYPE html>
<html lang="en">

<!-- Powered by Bear Blog -->

<head>
  
  
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5">
  
  <title>2025 LLM Year in Review – karpathy</title>
  <link rel="canonical" href="https://karpathy.bearblog.dev/year-in-review-2025/">
  
    

    <meta name="karpathy" content="look-for-the-bear-necessities">
    <meta name="token" content="pYRFQjhgQSqsbcTZfNkx">

    
<!-- Primary Meta Tags -->
<meta name="title" content="2025 LLM Year in Review">
<meta name="description" content="2025 Year in Review of LLM paradigm changes">

<!-- Open Graph / Facebook -->
<meta property="og:site_name" content="karpathy">
<meta property="og:title" content="2025 LLM Year in Review">
<meta property="og:type" content="article">
<meta property="og:url" content="https://karpathy.bearblog.dev/year-in-review-2025/">
<meta property="og:description" content="2025 Year in Review of LLM paradigm changes">
<meta property="og:image" content="/static/og-image.png">


<!-- Twitter -->
<meta property="twitter:card" content="summary">
<meta property="twitter:url" content="https://karpathy.bearblog.dev/year-in-review-2025/">
<meta property="twitter:title" content="2025 LLM Year in Review">
<meta property="twitter:description" content="2025 Year in Review of LLM paradigm changes">
<meta property="twitter:image" content="/static/og-image.png">



<!-- Microdata -->
<script type="application/ld+json">
  {
    "@context": "http://schema.org",
    "@type": "article",
    "name": "2025 LLM Year in Review",
    "headline": "2025 LLM Year in Review",
    "url": "https://karpathy.bearblog.dev/year-in-review-2025/",
    "description": "2025 Year in Review of LLM paradigm changes",
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
    

    

    
        <h1>2025 LLM Year in Review</h1>

        <p>
            <i>
                <time datetime="2025-12-19T18:00Z">
    19 Dec, 2025
</time>
            </i>
        </p>
    

    <p><img src="https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/unnamed.webp" alt="unnamed" /></p>
<p>2025 has been a strong and eventful year of progress in LLMs. The following is a list of personally notable and mildly surprising "paradigm changes" - things that altered the landscape and stood out to me conceptually.</p>
<h3 id=1-reinforcement-learning-from-verifiable-rewards-rlvr>1. Reinforcement Learning from Verifiable Rewards (RLVR)</h3><p>At the start of 2025, the LLM production stack in all labs looked something like this:</p>
<ol>
<li>Pretraining (GPT-2/3 of ~2020)</li>
<li>Supervised Finetuning (InstructGPT ~2022) and</li>
<li>Reinforcement Learning from Human Feedback (RLHF ~2022)</li>
</ol>
<p>This was the stable and proven recipe for training a production-grade LLM for a while. In 2025, Reinforcement Learning from Verifiable Rewards (RLVR) emerged as the de facto new major stage to add to this mix. By training LLMs against automatically verifiable rewards across a number of environments (e.g. think math/code puzzles), the LLMs spontaneously develop strategies that look like "reasoning" to humans - they learn to break down problem solving into intermediate calculations and they learn a number of problem solving strategies for going back and forth to figure things out (see DeepSeek R1 paper for examples). These strategies would have been very difficult to achieve in the previous paradigms because it's not clear what the optimal reasoning traces and recoveries look like for the LLM - it has to find what works for it, via the optimization against rewards.</p>
<p>Unlike the SFT and RLHF stage, which are both relatively thin/short stages (minor finetunes computationally), RLVR involves training against objective (non-gameable) reward functions which allows for a lot longer optimization. Running RLVR turned out to offer high capability/$, which gobbled up the compute that was originally intended for pretraining. Therefore, most of the capability progress of 2025 was defined by the LLM labs chewing through the overhang of this new stage and overall we saw ~similar sized LLMs but a lot longer RL runs. Also unique to this new stage, we got a whole new knob (and and associated scaling law) to control capability as a function of test time compute by generating longer reasoning traces and increasing "thinking time". OpenAI o1 (late 2024) was the very first demonstration of an RLVR model, but the o3 release (early 2025) was the obvious point of inflection where you could intuitively feel the difference.</p>
<h3 id=2-ghosts-vs-animals-jagged-intelligence>2. Ghosts vs. Animals / Jagged Intelligence</h3><p>2025 is where I (and I think the rest of the industry also) first started to internalize the "shape" of LLM intelligence in a more intuitive sense. We're not "evolving/growing animals", we are "summoning ghosts". Everything about the LLM stack is different (neural architecture, training data, training algorithms, and especially optimization pressure) so it should be no surprise that we are getting very different entities in the intelligence space, which are inappropriate to think about through an animal lens. Supervision bits-wise, human neural nets are optimized for survival of a tribe in the jungle but LLM neural nets are optimized for imitating humanity's text, collecting rewards in math puzzles, and getting that upvote from a human on the LM Arena. As verifiable domains allow for RLVR, LLMs "spike" in capability in the vicinity of these domains and overall display amusingly jagged performance characteristics - they are at the same time a genius polymath and a confused and cognitively challenged grade schooler, seconds away from getting tricked by a jailbreak to exfiltrate your data.</p>
<p><img src="https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/g6zymj4a0amnjkj.webp" alt="G6zymj4a0AMNJkJ" />(human intelligence: blue, AI intelligence: red. I like this version of the meme (I'm sorry I lost the reference to its original post on X) for pointing out that human intelligence is also jagged in its own different way.)</p>
<p>Related to all this is my general apathy and loss of trust in benchmarks in 2025. The core issue is that benchmarks are almost by construction verifiable environments and are therefore immediately susceptible to RLVR and weaker forms of it via synthetic data generation. In the typical benchmaxxing process, teams in LLM labs inevitably construct environments adjacent to little pockets of the embedding space occupied by benchmarks and grow jaggies to cover them. Training on the test set is a new art form.</p>
<p>What does it look like to crush all the benchmarks but still not get AGI?</p>
<p>I have written a lot more on the topic of this section here:</p>
<ul>
<li><a href='https://karpathy.bearblog.dev/animals-vs-ghosts/'>Animals vs. Ghosts</a></li>
<li><a href='https://karpathy.bearblog.dev/verifiability/'>Verifiability</a></li>
<li><a href='https://karpathy.bearblog.dev/the-space-of-minds'>The Space of Minds</a></li>
</ul>
<h3 id=3-cursor-new-layer-of-llm-apps>3. Cursor / new layer of LLM apps</h3><p>What I find most notable about Cursor (other than its meteoric rise this year) is that it convincingly revealed a new layer of an "LLM app" - people started to talk about "Cursor for X". As I highlighted in my Y Combinator talk this year (<a href='https://www.donnamagi.com/articles/karpathy-yc-talk'>transcript</a> and <a href='https://www.youtube.com/watch?v=LCEmiRjPEtQ'>video</a>), LLM apps like Cursor bundle and orchestrate LLM calls for specific verticals:</p>
<ol>
<li>They do the "context engineering"</li>
<li>They orchestrate multiple LLM calls under the hood strung into increasingly more complex DAGs, carefully balancing performance and cost tradeoffs.</li>
<li>They provide an application-specific GUI for the human in the loop</li>
<li>They offer an "autonomy slider"</li>
</ol>
<p>A lot of chatter has been spent in 2025 on how "thick" this new app layer is. Will the LLM labs capture all applications or are there green pastures for LLM apps? Personally I suspect that LLM labs will trend to graduate the generally capable college student, but LLM apps will organize, finetune and actually animate teams of them into deployed professionals in specific verticals by supplying private data, sensors and actuators and feedback loops.</p>
<h3 id=4-claude-code-ai-that-lives-on-your-computer>4. Claude Code / AI that lives on your computer</h3><p>Claude Code (CC) emerged as the first convincing demonstration of what an LLM Agent looks like - something that in a loopy way strings together tool use and reasoning for extended problem solving. In addition, CC is notable to me in that it runs on your computer and with your private environment, data and context. I think OpenAI got this wrong because they focused their early codex / agent efforts on cloud deployments in containers orchestrated from ChatGPT instead of simply <code>localhost</code>. And while agent swarms running in the cloud feels like the "AGI endgame", we live in an intermediate and slow enough takeoff world of jagged capabilities that it makes more sense to run the agents directly on the developer's computer. Note that the primary distinction that matters is not about where the "AI ops" happen to run (in the cloud, locally or whatever), but about everything else - the already-existing and booted up computer, its installation, context, data, secrets, configuration, and the low-latency interaction. Anthropic got this order of precedence correct and packaged CC into a delightful, minimal CLI form factor that changed what AI looks like - it's not just a website you go to like Google, it's a little spirit/ghost that "lives" on your computer. This is a new, distinct paradigm of interaction with an AI.</p>
<h3 id=5-vibe-coding>5. Vibe coding</h3><p>2025 is the year that AI crossed a capability threshold necessary to build all kinds of impressive programs simply via English, forgetting that the code even exists. Amusingly, I coined the term "vibe coding" in <a href='https://x.com/karpathy/status/1886192184808149383'>this shower of thoughts tweet</a> totally oblivious to how far it would go :). With vibe coding, programming is not strictly reserved for highly trained professionals, it is something anyone can do. In this capacity, it is yet another example of what I wrote about in <a href='https://karpathy.bearblog.dev/power-to-the-people/'>Power to the people: How LLMs flip the script on technology diffusion</a>, on how (in sharp contrast to all other technology so far) regular people benefit a lot more from LLMs compared to professionals, corporations and governments. But not only does vibe coding empower regular people to approach programming, it empowers trained professionals to write a lot more (vibe coded) software that would otherwise never be written. In nanochat, I vibe coded my own custom highly efficient BPE tokenizer in Rust instead of having to adopt existing libraries or learn Rust at that level. I vibe coded many projects this year as quick app demos of something I wanted to exist (e.g. see <a href='https://karpathy.bearblog.dev/vibe-coding-menugen'>menugen</a>, <a href='https://github.com/karpathy/llm-council'>llm-council</a>, <a href='https://github.com/karpathy/reader3'>reader3</a>, <a href='https://github.com/karpathy/hn-time-capsule'>HN time capsule</a>). And I've vibe coded entire ephemeral apps just to find a single bug because why not - code is suddenly free, ephemeral, malleable, discardable after single use. Vibe coding will terraform software and alter job descriptions.</p>
<h3 id=6-nano-banana-llm-gui>6. Nano banana / LLM GUI</h3><p>Google Gemini Nano banana is one of the most incredible, paradigm-shifting models of 2025. In my world view, LLMs are the next major computing paradigm similar to computers of the 1970s, 80s, etc. Therefore, we are going to see similar kinds of innovations for fundamentally similar kinds of reasons. We're going to see equivalents of personal computing, of microcontrollers (cognitive core), or internet (of agents), etc etc. In particular, in terms of the UIUX, "chatting" with LLMs is a bit like issuing commands to a computer console in the 1980s. Text is the raw/favored data representation for computers (and LLMs), but it is not the favored format for people, especially at the input. People actually dislike reading text - it is slow and effortful. Instead, people love to consume information visually and spatially and this is why the GUI has been invented in traditional computing. In the same way, LLMs should speak to us in our favored format - in images, infographics, slides, whiteboards, animations/videos, web apps, etc. The early and present version of this of course are things like emoji and Markdown, which are ways to "dress up" and lay out text visually for easier consumption with titles, bold, italics, lists, tables, etc. But who is actually going to build the LLM GUI? In this world view, nano banana is a first early hint of what that might look like. And importantly, one notable aspect of it is that it's not just about the image generation itself, it's about the joint capability coming from text generation, image generation and world knowledge, all tangled up in the model weights.</p>
<hr />
<p><strong>TLDR</strong>. 2025 was an exciting and mildly surprising year of LLMs. LLMs are emerging as a new kind of intelligence, simultaneously a lot smarter than I expected and a lot dumber than I expected. In any case they are extremely useful and I don't think the industry has realized anywhere near 10% of their potential even at present capability. Meanwhile, there are so many ideas to try and conceptually the field feels wide open. And as I mentioned on my <a href='https://www.dwarkesh.com/p/andrej-karpathy'>Dwarkesh pod</a> earlier this year, I simultaneously (and on the surface paradoxically) believe that we will both see rapid and continued progress <em>and</em> that yet there is a lot of work to be done. Strap in.</p>


    

    
        

        
            <form id="upvote-form" action="/upvote/" method="post" style="display: inline">
    <small>
        <input hidden name="uid" value="pYRFQjhgQSqsbcTZfNkx" style="display:none">
        <input hidden name="title" value="2025 LLM Year in Review" style="display:none">

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

    fetch('/upvote-info/pYRFQjhgQSqsbcTZfNkx/').then(response => response.json()).then(data => {
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
                            token: "pYRFQjhgQSqsbcTZfNkx",
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
