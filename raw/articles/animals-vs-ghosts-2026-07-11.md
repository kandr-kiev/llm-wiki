---
source_url: https://karpathy.bearblog.dev/animals-vs-ghosts/
ingested: 2026-07-11
sha256: 11ae1e789257526ad8c1066962029a17543a7e2d7e253c9e3c253b2515dc7b8d
blog_source: Andrej Karpathy
---
<!DOCTYPE html>
<html lang="en">

<!-- Powered by Bear Blog -->

<head>
  
  
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5">
  
  <title>Animals vs Ghosts – karpathy</title>
  <link rel="canonical" href="https://karpathy.bearblog.dev/animals-vs-ghosts/">
  
    

    <meta name="karpathy" content="look-for-the-bear-necessities">
    <meta name="token" content="SouAbXTdebxrKAPFAWyY">

    
<!-- Primary Meta Tags -->
<meta name="title" content="Animals vs Ghosts">
<meta name="description" content="Today&#x27;s frontier LLM research is not about building animals. It is about summoning ghosts. And a bit more on Sutton&#x27;s Dwarkesh pod.">

<!-- Open Graph / Facebook -->
<meta property="og:site_name" content="karpathy">
<meta property="og:title" content="Animals vs Ghosts">
<meta property="og:type" content="article">
<meta property="og:url" content="https://karpathy.bearblog.dev/animals-vs-ghosts/">
<meta property="og:description" content="Today&#x27;s frontier LLM research is not about building animals. It is about summoning ghosts. And a bit more on Sutton&#x27;s Dwarkesh pod.">
<meta property="og:image" content="/static/og-image.png">


<!-- Twitter -->
<meta property="twitter:card" content="summary">
<meta property="twitter:url" content="https://karpathy.bearblog.dev/animals-vs-ghosts/">
<meta property="twitter:title" content="Animals vs Ghosts">
<meta property="twitter:description" content="Today&#x27;s frontier LLM research is not about building animals. It is about summoning ghosts. And a bit more on Sutton&#x27;s Dwarkesh pod.">
<meta property="twitter:image" content="/static/og-image.png">



<!-- Microdata -->
<script type="application/ld+json">
  {
    "@context": "http://schema.org",
    "@type": "article",
    "name": "Animals vs Ghosts",
    "headline": "Animals vs Ghosts",
    "url": "https://karpathy.bearblog.dev/animals-vs-ghosts/",
    "description": "Today&#x27;s frontier LLM research is not about building animals. It is about summoning ghosts. And a bit more on Sutton&#x27;s Dwarkesh pod.",
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
    

    

    
        <h1>Animals vs Ghosts</h1>

        <p>
            <i>
                <time datetime="2025-10-01T17:00Z">
    01 Oct, 2025
</time>
            </i>
        </p>
    

    <p>Finally had a chance to listen through this <a href='https://www.youtube.com/watch?v=21EYKqUsPfg'>Dwarkesh pod with Sutton</a>, which was interesting and amusing.</p>
<p>As background, Sutton's "<a href='http://www.incompleteideas.net/IncIdeas/BitterLesson.html'>The Bitter Lesson</a>" has become a bit of biblical text in frontier LLM circles. Researchers routinely talk about and ask whether this or that approach or idea is sufficiently "bitter lesson pilled" (meaning arranged so that it benefits from added computation for free) as a proxy for whether it's going to work or worth even pursuing. The underlying assumption being that LLMs are of course highly "bitter lesson pilled" indeed, just look at LLM scaling laws where if you put compute on the x-axis, number go up and to the right. So it's amusing to see that Sutton, the author of the post, is not so sure that LLMs are "bitter lesson pilled" at all. They are trained on giant datasets of fundamentally human data, which is both 1) human generated and 2) finite. What do you do when you run out? How do you prevent a human bias? So there you have it, bitter lesson pilled LLM researchers taken down by the author of the bitter lesson - rough!</p>
<p>In some sense, Dwarkesh (who represents the LLM researchers viewpoint in the pod) and Sutton are slightly speaking past each other because Sutton has a very different architecture in mind and LLMs break a lot of its principles. He calls himself a "classicist" and evokes the original concept of Alan Turing of building a "child machine" - a system capable of learning through experience by dynamically interacting with the world. There's no giant pretraining stage of imitating internet webpages. There's also no supervised finetuning, which he points out is absent in the animal kingdom (it's a subtle point but Sutton is right in the strong sense: animals may of course observe demonstrations, but their actions are not directly forced/"teleoperated" by other animals). Another important note he makes is that even if you just treat pretraining as an initialization of a prior before you finetune with reinforcement learning, Sutton sees the approach as tainted with human bias and fundamentally off course, a bit like when AlphaZero (which has never seen human games of Go) beats AlphaGo (which initializes from them). In Sutton's world view, all there is is an interaction with a world via reinforcement learning, where the reward functions are partially environment specific, but also intrinsically motivated, e.g. "fun", "curiosity", and related to the quality of the prediction in your world model. And the agent is always learning at test time by default, it's not trained once and then deployed thereafter. Overall, Sutton is a lot more interested in what we have common with the animal kingdom instead of what differentiates us. "If we understood a squirrel, we'd be almost done".</p>
<p>As for my take...</p>
<p>First, I should say that I think Sutton was a great guest for the pod and I like that the AI field maintains entropy of thought and that not everyone is exploiting the next local iteration LLMs. AI has gone through too many discrete transitions of the dominant approach to lose that. And I also think that his criticism of LLMs as not bitter lesson pilled is not inadequate. Frontier LLMs are now highly complex artifacts with a lot of humanness involved at all the stages - the foundation (the pretraining data) is all human text, the finetuning data is human and curated, the reinforcement learning environment mixture is tuned by human engineers. We do not in fact have an actual, single, clean, actually bitter lesson pilled, "turn the crank" algorithm that you could unleash upon the world and see it learn automatically from experience alone.</p>
<p>Does such an algorithm even exist? Finding it would of course be a huge AI breakthrough. Two "example proofs" are commonly offered to argue that such a thing is possible. The first example is the success of AlphaZero learning to play Go completely from scratch with no human supervision whatsoever. But the game of Go is clearly such a simple, closed, environment that it's difficult to see the analogous formulation in the messiness of reality. I love Go, but algorithmically and categorically, it is essentially a harder version of tic tac toe. The second example is that of animals, like squirrels. And here, personally, I am also quite hesitant whether it's appropriate because animals arise by a very different computational process and via different constraints than what we have practically available to us in the industry. Animal brains are nowhere near the blank slate they appear to be at birth. First, a lot of what is commonly attributed to "learning" is imo a lot more "maturation". And second, even that which clearly is "learning" and not maturation is a lot more "finetuning" on top of something clearly powerful and preexisting. Example. A baby zebra is born and within a few dozen minutes it can run around the savannah and follow its mother. This is a highly complex sensory-motor task and there is no way in my mind that this is achieved from scratch, tabula rasa. The brains of animals and the billions of parameters within have a powerful initialization encoded in the ATCGs of their DNA, trained via the "outer loop" optimization in the course of evolution. If the baby zebra spasmed its muscles around at random as a reinforcement learning policy would have you do at initialization, it wouldn't get very far at all. Similarly, our AIs now also have neural networks with billions of parameters. These parameters need their own rich, high information density supervision signal. We are not going to re-run evolution. But we do have mountains of internet documents. Yes it is basically supervised learning that is ~absent in the animal kingdom. But it is a way to practically gather enough soft constraints over billions of parameters, to try to get to a point where you're not starting from scratch. TLDR: Pretraining is our crappy evolution. It is one candidate solution to the cold start problem, to be followed later by finetuning on tasks that look more correct, e.g. within the reinforcement learning framework, as state of the art frontier LLM labs now do pervasively.</p>
<p>I still think it is worth to be inspired by animals. I think there are multiple powerful ideas that LLM agents are algorithmically missing that can still be adapted from animal intelligence. And I still think the bitter lesson is correct, but I see it more as something platonic to pursue, not necessarily to reach, in our real world and practically speaking. And I say both of these with double digit percent uncertainty and cheer the work of those who disagree, especially those a lot more ambitious bitter lesson wise.</p>
<p>So that brings us to where we are. Stated plainly, today's frontier LLM research is not about building animals. It is about summoning ghosts. You can think of ghosts as a fundamentally different kind of point in the space of possible intelligences. They are muddled by humanity. Thoroughly engineered by it. They are these imperfect replicas, a kind of statistical distillation of humanity's documents with some sprinkle on top. They are not platonically bitter lesson pilled, but they are perhaps "practically" bitter lesson pilled, at least compared to a lot of what came before. It seems possibly to me that over time, we can further finetune our ghosts more and more in the direction of animals; That it's not so much a fundamental incompatibility but a matter of initialization in the intelligence space. But it's also quite possible that they diverge even further and end up permanently different, un-animal-like, but still incredibly helpful and properly world-altering. It's possible that ghosts:animals :: planes:birds.</p>
<p>Anyway, in summary, overall and actionably, I think this pod is solid "real talk" from Sutton to the frontier LLM researchers, who might be gear shifted a little too much in the exploit mode. Probably we are still not sufficiently bitter lesson pilled and there is a very good chance of more powerful ideas and paradigms, other than exhaustive benchbuilding and benchmaxxing. And animals might be a good source of inspiration. Intrinsic motivation, fun, curiosity, empowerment, multi-agent self-play, culture. Use your imagination.</p>
<ul>
<li>Also available as <a href='https://x.com/karpathy/status/1973435013875314729'>tweet here</a>, should you wish to reply/comment.</li>
<li>Also available as <a href='https://chatgpt.com/share/68dd6833-67c4-8007-8f37-331eb5bd9ee0'>ChatGPT conversation</a>, should you wish to fork the conversation and ask any questions with all of the context (the podcast transcript, bitter lesson post, and this blog post).</li>
</ul>
<h3 id=appendix>Appendix</h3><ul>
<li>I agree with Sutton that animals don't do supervised learning. I realize it's a subtle point that will confuse a lot of people. Animals do observe demonstrations, but they are not strictly speaking directly supervised with actions, like supervised learning does. Animals are never teleoperated in training mode. The closest thing I can think of is if you for example help a child eat with a spoon or something, by literally holding their hand and showing the motion. Even then, it's not clear that their brains are literally training on that. It might still be in the realm of what is more accurately described as observation. But in any case, these instances are very rare overall, while in the case of LLMs it is the default mode of learning during pretraining and SFT. Maybe another way to put it is that the analogue in LLM land to what humans do is something along the lines of: Given this math problem AND human example solution in the context, solve the problem. Reward of 1 if correct. It's not SFT, it's RL.</li>
<li>Dwarkesh briefly made the point that LLMs do have their own continual learning at test time, it's just not based on weight training, but I think Sutton didn't fully react to that. In context learning is a form of test time adaptation and e.g. why few shot prompting works. A lot of recent work is also very interested in memory (think CLAUDE.md files) as a mechanism for test-time learning that uses the text/context as the substrate instead of weights.</li>
<li>Dwarkesh brings up the example of very long-horizon sparse rewards (e.g. building a successful startup) and how that might work. Sutton offered the resolution of temporal difference learning and essentially future reward discounting, which I don't find particularly compelling. I wrote about this a bit more previously, I think something else is going on and imo it's not reinforcement learning.</li>
<li>There was a lot about "gradient descent will not make you generalize well" and related discussion which I didn't follow.</li>
<li>Someone pointed out that ghosts are scary. Not necessarily, look at <a href='https://en.wikipedia.org/wiki/Casper_the_Friendly_Ghost'>Casper</a>, my childhood favorite.</li>
</ul>


    

    
        

        
            <form id="upvote-form" action="/upvote/" method="post" style="display: inline">
    <small>
        <input hidden name="uid" value="SouAbXTdebxrKAPFAWyY" style="display:none">
        <input hidden name="title" value="Animals vs Ghosts" style="display:none">

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

    fetch('/upvote-info/SouAbXTdebxrKAPFAWyY/').then(response => response.json()).then(data => {
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
                            token: "SouAbXTdebxrKAPFAWyY",
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
