---
source_url: http://yummymelon.com/devnull/malleable-computing-emacs-and-you.html
ingested: 2026-07-22
sha256: 4bb88be90090fdf351839cd96621564897be1363d240d82aa8f7d4a9bfaa9546
blog_source: Hacker News
---
<!DOCTYPE html>
<html>
  <head>
  <title>nfdn: Malleable Computing, Emacs, and You</title>
  <link rel='stylesheet' type='text/css' media="only screen and (max-device-width:480px)" href='./theme/css/small-device.css' />
  <link rel='stylesheet' type='text/css' media="only screen and (min-device-width:481px)" href='./theme/css/desktop.css' />
  <link rel='stylesheet' type='text/css' href='./theme/css/color-scheme.css' />
  <link rel='stylesheet' type='text/css' href='./theme/css/main.css?ts=202510281953' />
  <meta name="viewport" content="width=device-width, user-scalable=no, maximum-scale=1.0, minimum-scale=1.0, initial-scale=1.0" />
  <meta content="text/html; charset=UTF-8" http-equiv="Content-Type" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="http://yummymelon.com/devnull/malleable-computing-emacs-and-you.html" />
  <meta property="og:title" content="Malleable Computing, Emacs, and You" />
  <meta property="og:description" content="It all started with a routine task. I use GitHub issues for all of my public-facing projects but my preference is keeping track of things in Org Agenda. To reconcile the two, I would manually..." />
  <meta property="og:image" content="http://yummymelon.com/devnull/images/opengraph-default.jpg" />
  <link rel="alternate" type="application/rss+xml" title="ATOM Feed for notes from /dev/null" href='http://yummymelon.com/devnull/feeds/all.atom.xml' />
  </head>
<body class="body adaptive">
<h1 class='siteTitle'><a href=".">notes from /dev/null</a></h1>
<p>by Charles Choi ìµë¯¼ì</p>
<hr/>
<body>
<div class='base'>
<div class='main' data-pagefind-body>
<h1 class='articleTitle' data-pagefind-meta="title">Malleable Computing, Emacs, and You</h1>
<p>22 Jul 2026&nbsp;&nbsp;Charles Choi</p>


<div class='articleBase adaptive'>
<p>It all started with a routine task. I use GitHub issues for all of my public-facing projects but my preference is keeping track of things in Org Agenda. To reconcile the two, I would manually copy over the GitHub issue to an Org file, typically the title and description, <em>like an animal</em>.</p>
<p>Despite this separation, the duplicated issue allowed me to treat it as a scratchpad for anything I could express in Org. In this way, I used the duplicated issue in Org as both a dedicated area to take notes and a âstagingâ area to compose follow-up comments that Iâd want to share in the public facing issue.</p>
<p>I manually copied for far longer than I care to admit. Repeat a task enough times in Emacs and the inevitable thought arises: âI should automate this.â</p>
<p>This post recounts how I automated this task and in doing so, highlight the malleable computing capabilities of Emacs. It should also be considered a follow-up to my earlier post â<a href="./in-emacs-everything-looks-like-a-service.html">In Emacs, Everything Looks Like a Service</a>â.</p>
<h1>Requirements</h1>
<p>An essential question to ask in any automation exercise is âWhat do I want done?â</p>
<p>I wanted to be able to:</p>
<ul>
<li>Easily copy a GitHub issue (title, description, some metadata) as an Org task that can be tracked in an Agenda view.</li>
<li>Work primarily from Emacs to minimize the context switching between it and a web browser.</li>
<li>Express my thoughts in Org syntax.</li>
<li>Create a new GitHub issue.</li>
<li>Avoid dealing with GitHub authentication.</li>
<li>From Emacs, open a GitHub issue in a web browser.</li>
</ul>
<p>Another essential question to ask is âWhat do I <em>not</em> want to do?â</p>
<ul>
<li>Install or write a full-featured GitHub client.<ul>
<li>Worry too much about synchronization logic between local (Emacs) and server (GitHub) state.</li>
</ul>
</li>
<li>Spend a lot of time on this (ideally have something working in a day, no more than a week).</li>
</ul>
<h1>Specification</h1>
<p>With the above requirements in place, the next question is âhow do I build this?â</p>
<p>For this particular exercise, I decided to leverage my existing install of the GitHub command line utility <a href="https://cli.github.com">gh</a>. The benefits for this are:</p>
<ul>
<li>GitHub authentication is delegated to <code>gh</code>; no need to mess with it directly from Emacs.</li>
<li>
<p>Emacs can treat <code>gh</code> as a REST service to GitHub as shown in the diagram below</p>
<p><img alt="img" src="images/malleable-computing-emacs/emacs-gh.svg"></p>
</li>
</ul>
<p>To flesh out the rest of our tool, we can leverage using different Elisp packages and programs:</p>
<ul>
<li>
<p>For the user interface, the <a href="https://www.gnu.org/software/emacs/manual/html_node/transient/">Transient</a> and <a href="https://www.gnu.org/software/emacs/manual/html_node/vtable/">Variable Pitch Table (vtable)</a> packages are used for menus and display respectively.</p>
</li>
<li>
<p>For Org to Markdown translation, <a href="https://melpa.org/#/ox-gfm">ox-gfm</a> will be used.</p>
</li>
<li>
<p>For Markdown to Org translation, <a href="https://pandoc.org">Pandoc</a> will be used.</p>
</li>
<li>
<p>Elisp native <a href="https://www.gnu.org/software/emacs/manual/html_node/elisp/Parsing-JSON.html">JSON</a> support will be used for deserializing the JSON responses from <code>gh</code>.</p>
</li>
</ul>
<h1>Implementation</h1>
<p>The implementation of the above is published as the package <a href="https://github.com/kickingvegas/fj">fj</a> with its source available for examination in the file <a href="https://github.com/kickingvegas/fj/blob/main/lisp/fj.el">fj.el</a>. Of note is the function <code>fj-request-issues</code> which does the work of retrieving GitHub issues via <code>gh</code> as shown below.</p>
<div class="highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span class="normal"> 1</span>
<span class="normal"> 2</span>
<span class="normal"> 3</span>
<span class="normal"> 4</span>
<span class="normal"> 5</span>
<span class="normal"> 6</span>
<span class="normal"> 7</span>
<span class="normal"> 8</span>
<span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="p">(</span><span class="nb">defun</span><span class="w"> </span><span class="nv">fj-request-issues</span><span class="w"> </span><span class="p">(</span><span class="nv">repo</span><span class="p">)</span>
<span class="w">  </span><span class="s">&quot;Request issues for REPO.&quot;</span>
<span class="w">  </span><span class="p">(</span><span class="k">let*</span><span class="w"> </span><span class="p">((</span><span class="nv">fields</span><span class="w"> </span><span class="nv">fj-browser-fields</span><span class="p">)</span>
<span class="w">         </span><span class="p">(</span><span class="nv">cmd-list</span><span class="w"> </span><span class="p">(</span><span class="nf">list</span><span class="w"> </span><span class="s">&quot;gh&quot;</span>
<span class="w">                         </span><span class="s">&quot;--repo&quot;</span>
<span class="w">                         </span><span class="p">(</span><span class="nf">format</span><span class="w"> </span><span class="s">&quot;&#39;%s&#39;&quot;</span><span class="w"> </span><span class="nv">repo</span><span class="p">)</span>
<span class="w">                         </span><span class="s">&quot;issue&quot;</span>
<span class="w">                         </span><span class="s">&quot;list&quot;</span>
<span class="w">                         </span><span class="s">&quot;--limit&quot;</span>
<span class="w">                         </span><span class="p">(</span><span class="nf">number-to-string</span><span class="w"> </span><span class="nv">fj-request-issue-count</span><span class="p">)</span>
<span class="w">                         </span><span class="s">&quot;--json&quot;</span>
<span class="w">                         </span><span class="p">(</span><span class="nv">string-join</span><span class="w"> </span><span class="nv">fields</span><span class="w"> </span><span class="s">&quot;,&quot;</span><span class="p">))))</span>

<span class="w">    </span><span class="p">(</span><span class="nv">json-parse-string</span><span class="w"> </span><span class="p">(</span><span class="nv">shell-command-to-string</span>
<span class="w">                        </span><span class="p">(</span><span class="nv">string-join</span><span class="w"> </span><span class="nv">cmd-list</span><span class="w"> </span><span class="s">&quot; &quot;</span><span class="p">))</span>
<span class="w">                       </span><span class="nb">:null-object</span><span class="w"> </span><span class="no">nil</span><span class="p">)))</span>
</code></pre></div></td></tr></table></div>

<p>Consider the high degree of abstraction provided by <code>fj-request-issues</code>:</p>
<ul>
<li>The list <code>cmd-list</code> forms the request (in this case, the arguments to invoke <code>gh</code> with).</li>
<li><code>shell-command-to-string</code> dispatches the request to <code>gh</code>.</li>
<li>The returned JSON response is handled by <code>json-parse-string</code> to deserialize the JSON into an Elisp hash table.</li>
<li>All of the above is accomplished in less than 20 lines of code.</li>
</ul>
<p>The returned hash table result is subsequently processed to populate a vtable as shown below. From the vtable, the user can navigate the list of issues with an ancillary window updated to show the details of a selected issue.</p>
<p><img alt="img" src="images/malleable-computing-emacs/fj-screenshot.png"></p>
<p>Multiple commands and functions working with said hash-table were made to satisfy the requirements above. They are accessible via the Transient menu shown below:</p>
<p><img alt="img" src="images/malleable-computing-emacs/fj-transient.png"></p>
<h1>Malleable Computing Observations</h1>
<p>As Elisp is a <a href="https://en.wikipedia.org/wiki/Dynamic_programming_language">dynamic programming language</a>, the above function (or some variant of it) can be coded and evaluated within a running Emacs session. In Emacs it is routine practice to prototype code behavior without the need to restart it. Contrast this with tools that are built with a static language and have no extensibility, where the <em>edit-compile-debug</em> development cycle must be applied to exercise behavior, provided the source code is available.</p>
<p>Emacs provides numerous ways to edit and evaluate Elisp code, among them:</p>
<ul>
<li>A scratch buffer</li>
<li>An Elisp file</li>
<li>An Org source block</li>
<li>IELM REPL</li>
<li>Eshell</li>
<li><code>eval-expression</code> (<code>M-:</code>)</li>
</ul>
<p>Because there is no isolation between loaded Elisp code, all of it can be orchestrated together in an improvised fashion. Any program accessible to Emacs via shell further adds to this mix.</p>
<p>Provided high abstractions, the amount of code needed to be written for desired behavior can be small. At the time of this writing, <code>fj.el</code> has approximately 400 lines of code has been measured by <code>cloc</code>:</p>
<div class="highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span class="normal">1</span>
<span class="normal">2</span>
<span class="normal">3</span>
<span class="normal">4</span>
<span class="normal">5</span>
<span class="normal">6</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="c">github</span><span class="nt">.</span><span class="c">com/AlDanial/cloc v 2</span><span class="nt">.</span><span class="c">08  T=0</span><span class="nt">.</span><span class="c">01 s (146</span><span class="nt">.</span><span class="c">4 files/s</span><span class="nt">,</span><span class="c"> 76550</span><span class="nt">.</span><span class="c">1 lines/s)</span>
<span class="nb">-------------------------------------------------------------------------------</span>
<span class="c">Language                     files          blank        comment           code</span>
<span class="nb">-------------------------------------------------------------------------------</span>
<span class="c">Lisp                             1             93             38            392</span>
<span class="nb">-------------------------------------------------------------------------------</span>
</code></pre></div></td></tr></table></div>

<p>It took me about 2Â½ hours to build the basic behavior I wanted (request issues from GitHub, then display) and the rest of the day to cover all the original requirements. Everything after that was just refactoring.</p>
<p>Motivated readers are invited to examine <code>fj.el</code> to understand its details. At this point though, Iâd like to take the opportunity to muse on software engineering and malleable computing.</p>
<h2>Software Scope - Some Percentage Anecdotes</h2>
<p>The <a href="https://en.wikipedia.org/wiki/Ninetyâninety_rule">90/90 rule</a> posits that âThe first 90 percent of the code accounts for the first 90 percent of the development time. The remaining 10 percent of the code accounts for the other 90 percent of the development timeâ. Closely related is the <a href="https://en.wikipedia.org/wiki/Pareto_principle">Pareto principle</a> (aka the 80/20 rule) as applied (or more mis-applied) to software development: only 20% of your features will be actually used by 80% of your users.</p>
<p>From control theory there is the concept of <a href="https://en.wikipedia.org/wiki/BIBO_stability">bounded input, bounded output (BIBO) stability</a>. If the system is BIBO stable, then whatever input that is bounded will have an output that is also bounded.</p>
<p>Coupling these ideas together, if the functionality you want (BIBO stability) is within that 20% deliverable then you are positioned to get a desired result <em>faster</em>.</p>
<p>Unfortunately, this observation is not available for many producers shipping a tool that must satisfy a large audience. In Sinofskyâs post â<a href="https://hardcoresoftware.learningbyshipping.com/p/077-what-is-bloat-really?s=w">What is Software Bloat, Really?</a>â, he describes the product definition issues with shipping Microsoft Office, particularly with feature set. From their user research, they were led to this finding: ââ¦ the data was entirely conclusive: Most of Office was used. But no one person used the entire product.â</p>
<p>When discussing product definition, it is helpful to distinguish two informal dynamics: supply and demand.</p>
<p>With software that is only supply-provided (such as the case with MS Office), the weight of product definition is shouldered by the producer. If the producer wants to serve a vast audience, it is likely their feature set and corresponding development scope will be vast as well. On the demand-side, consumers can make requests for new features, but their prioritization is controlled by the producer. In this situation, the roles of producer and consumer are strongly delineated.</p>
<p>Malleable software, where users have agency to adapt and reshape their digital tools, offers a different possibility: producers provide the building blocks and let consumers make their own tools. In this, both existing code and programs are recombined to make new behavior. Stated another way, malleable software takes advantage of combinatorial explosion in that a desired subset of behavior can likely be found within the state space of combining existing libraries (in this case Elisp) with different programs. With malleable software, the roles between producer and consumer are less delineated. A consumer building a new tool out of malleable building blocks now must shoulder the weight of product definition.</p>
<h2>Build for 1 or N</h2>
<p>The scope to build for 1 vs <em>N</em> can be an order of magnitude with the kicker that <em>N</em> need not be large. Choosing to write code for another person (<em>N=2</em>) escalates concerns that could otherwise be brushed aside:</p>
<ul>
<li>Error handling</li>
<li>Code maintainability<ul>
<li>Modularity/Reuse</li>
</ul>
</li>
<li>Documentation</li>
<li>Unit and Integration Testing</li>
<li>Packaging</li>
<li>Distribution</li>
</ul>
<p>Both a blessing and curse of malleable techniques is that they allow for âjust good enoughâ capability. Malleable techniques encourage building for 1 as reaching a state of âit works for meâ is often sufficient to declare victory.</p>
<p>For most software that is only supply-provided, building for <em>N</em> is a requirement. For most software built with malleable techniques, building for <em>N</em> is a choice.</p>
<h2>Malleable Software and User Agency</h2>
<p>Returning back to <code>fj</code>, the benefits of building for 1 are evident:</p>
<p>From within Emacs I can now easily:</p>
<ul>
<li>Peruse GitHub issues for a specified repository.</li>
<li>Copy a GitHub issue into a Org file.</li>
<li>Create a new GitHub issue using Org syntax.</li>
<li>Open a GitHub issue in a web browser.</li>
</ul>
<p>Implementing <code>fj</code> in Emacs was straightforward as I could leverage Elisp packages (both built-in and 3rd party) and external applications (<code>gh</code>, <code>pandoc</code>) to build it. Within a day I had a tool that did what I wanted. I did not have to ask for permission nor required privileged materials (source code) to build <code>fj</code>. With Emacs, I could <em>just do it</em>. Such individual empowerment advanced by malleable techniques is liberating in contrast to working with siloed applications with little to no integration between them.</p>
<h1>Closing Thoughts</h1>
<p>This post muses about the malleable computing capabilities provided by Emacs, showing by concrete example (<code>fj.el</code>) how new behavior can be created leveraging both code and program reuse in an improvised fashion. With measured expectations (requirements, feature set, audience), malleable techniques allow for building tools that would otherwise be infeasible without it.</p>
<h1>Links</h1>
<ul>
<li><a href="https://github.com/kickingvegas/fj">https://github.com/kickingvegas/fj</a></li>
<li>â<a href="https://hardcoresoftware.learningbyshipping.com/p/077-what-is-bloat-really?s=w">What Is Software Bloat, Really?</a>â, Steven Sinofsky.</li>
</ul>
<p align='right'>
 <a href='tag/emacs.html'>emacs</a>
&nbsp; <a href='tag/org-mode.html'>org mode</a>
</p>
</div>

<p/>
<div id="textbox">
<p class="alignright"><a href="in-emacs-everything-looks-like-a-service.html">In Emacs, Everything Looks Like a Service&nbsp;&rarr;</a></p>
</div>
<div style="clear: both;"></div>

</div>
</div>

<div style='height: 0.1in;'>&nbsp;
</div>

<link href="./pagefind/pagefind-ui.css" rel="stylesheet">
<script src="./pagefind/pagefind-ui.js"></script>
<div id="search" style="margin-bottom: 0.2in;"></div>
<script>
    window.addEventListener('DOMContentLoaded', (event) => {
        new PagefindUI({ element: "#search", showSubResults: true });
    });
</script>

<hr/>

<p align='center'>
  <a href="./pages/about.html">About</a>
  â¢ <a href="https://sfba.social/@kickingvegas">Mastodon</a>
  â¢ <a href="https://bsky.app/profile/kickingvegas.bsky.social">Bluesky</a>
  â¢ <a href="https://github.com/kickingvegas">GitHub</a>


<p align='center'><a href="./tags.html">Feeds &amp; Tags</a> â¢ <a href="https://buymeacoffee.com/kickingvegas"><img src="./theme/images/icons/buymecoffee.png" height="30pt" style="vertical-align: -7px;"/></a><br/>
<a href="http://yummymelon.com/scrim" title='Scrim is an Org Protocol Proxy for Emacs on macOS.'>Get Scrim for macOS</a> â¢ <a href="http://yummymelon.com/captee" title='Captee is an app that makes marking up a link (both URL and title) a one-step operation straight from the macOS Share menu.'>Get Captee for macOS</a></p>

<p class='copyright'>&copy; 2009-2026 Charles Y. Choi</p>
<p style='font-size:7pt; text-color: #333333;' align='center'>Powered by <a href='http://getpelican.com'>Pelican</a></p>


</body>
</html>