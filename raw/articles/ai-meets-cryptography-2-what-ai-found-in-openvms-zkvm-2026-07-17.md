---
source_url: https://blog.zksecurity.xyz/posts/openvm-bugs/
ingested: 2026-07-17
sha256: 176a49169e30285ee994ebb6db96611a7b29777ec7377fffaab75e45da99af62
blog_source: Hacker News AI
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI meets Cryptography 2: What AI Found in OpenVM's zkVM - ZK/SEC Quarterly</title>
    <meta name="description" content="We turned zkao (our AI auditor) on OpenVM, a state-of-the-art zkVM, and it found a critical soundness bug: the pairing check accepted a prover-supplied witness without proper subfield checking, which lets a malicious prover forge any pairing equality. It is fixed in OpenVM 1.6.0 and tracked as CVE-2026-46669. This is the second post in our series on bugs our agents found across open source cryptography.">
    <meta name="author" content="Stefanos Chaliasos, Hao Pham">

    <!-- OpenGraph meta tags -->
    <meta property="og:title" content="AI meets Cryptography 2: What AI Found in OpenVM's zkVM">
    <meta property="og:description" content="We turned zkao (our AI auditor) on OpenVM, a state-of-the-art zkVM, and it found a critical soundness bug: the pairing check accepted a prover-supplied witness without proper subfield checking, which lets a malicious prover forge any pairing equality. It is fixed in OpenVM 1.6.0 and tracked as CVE-2026-46669. This is the second post in our series on bugs our agents found across open source cryptography.">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://blog.zksecurity.xyz/posts/openvm-bugs/">
    <meta property="og:site_name" content="ZK/SEC Quarterly">
    <meta property="article:author" content="Stefanos Chaliasos, Hao Pham">
    <meta property="article:published_time" content="July 17, 2026">

    <!-- Twitter Card meta tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="AI meets Cryptography 2: What AI Found in OpenVM's zkVM">
    <meta name="twitter:description" content="We turned zkao (our AI auditor) on OpenVM, a state-of-the-art zkVM, and it found a critical soundness bug: the pairing check accepted a prover-supplied witness without proper subfield checking, which lets a malicious prover forge any pairing equality. It is fixed in OpenVM 1.6.0 and tracked as CVE-2026-46669. This is the second post in our series on bugs our agents found across open source cryptography.">

    <link rel="icon" type="image/x-icon" href="../../static/images/favicon.ico">
    <link rel="alternate" type="application/rss+xml" title="ZK/SEC Quarterly RSS Feed" href="https://blog.zksecurity.xyz/feed.xml">
    <!-- LLMs: see /posts/openvm-bugs.md for a markdown version of this page -->
    <link rel="alternate" type="text/markdown" href="../../posts/openvm-bugs.md" title="AI meets Cryptography 2: What AI Found in OpenVM's zkVM (Markdown)">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Libre+Baskerville:wght@400;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../../static/css/style.css">
    <link rel="stylesheet" href="../../static/css/pygments.css">
    <script src="../../static/js/theme-toggle.js"></script>

    <!-- MathJax for LaTeX rendering -->
    <script>
    MathJax = {
      tex: {
        inlineMath: [['$', '$']],
        displayMath: [['$$', '$$']],
        processEscapes: true
      }
    };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <link rel="canonical" href="https://blog.zksecurity.xyz/posts/openvm-bugs/" />
</head>
<body>
    <!-- Dark Mode Toggle -->
    <button class="theme-toggle" aria-label="Toggle dark mode">
        <svg class="moon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
        </svg>
        <svg class="sun-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="5"></circle>
            <line x1="12" y1="1" x2="12" y2="3"></line>
            <line x1="12" y1="21" x2="12" y2="23"></line>
            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
            <line x1="1" y1="12" x2="3" y2="12"></line>
            <line x1="21" y1="12" x2="23" y2="12"></line>
            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
        </svg>
    </button>

    <header class="site-header">
        <div class="container">
            <h1 class="site-title"><a href="../../index.html">ZK/SEC Quarterly</a></h1>
        </div>
    </header>

    <a href="../../index.html" class="back-link">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M10 13l-5-5 5-5"/>
        </svg>
        Back to all posts
    </a>

    <article>
        <header class="post-header">
            <h1 class="post-title">AI meets Cryptography 2: What AI Found in OpenVM's zkVM</h1>
            <div class="post-meta">
                <span class="post-author">Stefanos Chaliasos, Hao Pham</span>
                <span class="post-date">July 17, 2026</span>
                <span class="post-reading-time">13 min read</span>
            </div>
            
            <div class="post-tags">
                
                <span class="tag">security</span>
                
                <span class="tag">crypto</span>
                
                <span class="tag">AI</span>
                
                <span class="tag">zkao</span>
                
                <span class="tag">audit</span>
                
                <span class="tag">zkvm</span>
                
            </div>
            
        </header>

        <div class="post-body">
            <p><img alt="Thumbnail" src="./thumbnail.png" /></p>
<p>This is the second post in the series.
In case you have not read the <a href="../circl-bugs">first one on Cloudflare's CIRCL</a>, it has more context on why we run these experiments and how our pipeline is set up.
In this post, we pointed <a href="https://zkao.io/">zkao</a>, our AI auditor, at <a href="https://github.com/openvm-org/openvm">OpenVM's zkVM</a>, and it found a critical soundness bug in its guest library <code>openvm-pairing</code> that lets a malicious prover forge any pairing equality.
Note that this is not a soundness bug in the zkVM's proving system itself; it only affects code that uses the vulnerable library.</p>
<p>The bug in this post was assigned <a href="https://github.com/openvm-org/openvm/security/advisories/GHSA-76mq-v757-53gr">CVE-2026-46669</a> and fixed in OpenVM 1.6.0.
As far as we know, all partners building on OpenVM have since upgraded to that version.</p>
<div class="callout callout-note">
<div class="callout-title">Note</div>
<div class="callout-body">
<p><strong>Clarification</strong>, same as in the first post: the AI produced a candidate finding, not a final report.
Humans on our team then validated the issue, confirmed exploitability, understood the full impact and affected projects, and handled disclosure.
In this case, a very quick manual triage was enough to decide it was worth sharing with the OpenVM team, thanks to the detailed report and a minimal PoC that zkao produced itself.</p>
</div>
</div>
<h2 id="how-it-happened">How it happened</h2>
<p>Four months ago, we scanned <a href="https://github.com/openvm-org/openvm">OpenVM</a> as part of our AI experiment, the same way we scan everything at first: an LLM with a simple prompt, and then an LLM with our expert-maintained skills.
We ran it with Opus 4.6 and Codex 5.3.
As soon as Opus 4.7 and Codex 5.4 came out, we ran them again.
The candidate findings were all valid observations, and the models confidently labeled several of them as Critical or High, but none of them were actually exploitable.</p>
<p>Our hypothesis was that a zkVM is simply too complex for a naive LLM setup to handle with 300K tokens or even 1M tokens of context.
The dependencies between modules are far denser than in a typical library.
A cryptography library can often be audited in parallel by simply handing each subagent a folder that maps to a single cryptographic primitive.
Each subagent reads a small number of lines, applies only the relevant skills, writes its findings to a markdown file, and the main agent stitches those files together.
All of this happens out of the box with popular agentic coding tools such as Claude Code and Codex, with little human steering.</p>
<p>That approach does not transfer to a more complex codebase, like OpenVM.
There, except for the low-hanging fruit, a subagent's useful output is not a list of bugs.
You can have a provably secure module A and a provably secure module B whose composition is still not secure.
So, hunting for bugs in that "isolated" mode cannot catch meaningful bugs.
Instead, a subagent's output should be <em>knowledge</em> about a module: what it assumes, what it delegates to its callers, and what invariant it is silently relying on.
However, representing that kind of output well is the hard part.
Too short and it skips the implementation detail that the bug actually sits on.
Too long and it overflows the main agent's context before it can be combined with anything else.
From what we have seen, at least at the time of writing, this problem is not solved efficiently by the agentic coding tools mentioned above.</p>
<p>With that hypothesis in mind, we decided to run <a href="https://zkao.io/">zkao</a> on OpenVM, even though our original rule for these experiments was to run zkao only <em>after</em> the plain LLMs had already found a real bug.
We have spent a lot of time on context engineering for zkao, and we have encoded the working methods of our own experts into it as reusable flows for finding vulnerabilities, so it seemed like the right tool for exactly this situation.
After more than nine and a half hours of scanning, it returned many findings.
Similar to the prior experiment, we did not have time to go over every finding in depth. 
After a quick pass, one stood out immediately: a critical soundness bug in the pairing check in one of the guest libraries.
Our hypothesis held up, and months of effort had paid off!</p>
<p>Although there is only one bug to share, to stay consistent with the first post, here is the bug at a glance.</p>
<h2 id="severities-and-fixes-at-a-glance">Severities and fixes at a glance</h2>
<table>
<thead>
<tr>
<th>#</th>
<th>Bug</th>
<th>AI severity</th>
<th>OpenVM severity</th>
<th>Fix commit</th>
<th>Found by</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><a href="#bug-1-openvm-pairing-pairing-check-missing-proper-subfield-check-on-scaling-factor"><code>openvm-pairing</code> pairing check missing proper subfield check on scaling factor</a></td>
<td>Critical</td>
<td>Critical</td>
<td><a href="https://github.com/openvm-org/openvm/commit/a720e2c7ba529becd101dbad24c879bd5c1257f4"><code>a720e2c</code></a></td>
<td><a href="https://zkao.io/">zkao</a></td>
</tr>
</tbody>
</table>
<p>This time, the AI severity and the maintainer severity agree.</p>
<h2 id="bug-1-openvm-pairing-pairing-check-missing-proper-subfield-check-on-scaling-factor">Bug 1: <code>openvm-pairing</code> pairing check missing proper subfield check on scaling factor</h2>
<h3 id="background">Background</h3>
<p>Pairings are the engine under Groth16, PLONK with KZG, and BLS signatures.
In all of these protocols, the verifier is usually not asking for one pairing value.
It is asking whether a product of pairings is one:</p>
$$ \prod_i e(P_i, Q_i) = 1. $$

<p>From that one yes-or-no answer, a verifier concludes that a SNARK proof is valid, that a KZG opening is correct, or that a signature verifies.
So if a prover can make a false pairing product appear to be one, everything built on top of it is no longer sound.</p>
<p>A pairing is a bilinear map</p>
$$
e : G_1 \times G_2 \to G_T,
$$

<p>where $G_1, G_2, G_T$ are abelian groups. In our case, $G_1$ and $G_2$ are elliptic-curve groups and $G_T$ is a multiplicative subgroup of $\mathbb{F}_{p^{12}}^{*}$.</p>
<p>The most important property of pairing is bilinearity:</p>
$$ e([a]P, [b]Q) = e(P, Q)^{ab}. $$

<p>This is why pairings are useful, but we will not actually need this property to understand the bug. So you can just ignore it.</p>
<p>Computing a pairing $e(P, Q)$ has two main steps (except for Weil pairing).</p>
<p><strong>The first step</strong> is the Miller loop.
It evaluates a Miller function $f_{r, Q}(P)$, which we can just view as a black box for simplicity.
This stage outputs an element in $\mathbb{F}_{p^{12}}^{*}$.
For a product of pairings, the circuit can run all the Miller loops and multiply their outputs together.
Let us call that combined output $f$, i.e. $f = \prod_i f_{r, Q_i}(P_i)$.</p>
<p>The catch is that $f$ is not the pairing product yet.
It is only one representative of the equivalence class $\mathbb{F}_{p^{12}}^{*} / (\mathbb{F}_{p^{12}}^{*})^r$.
This is one of the main observations from Novakovic and Eagen's <a href="https://eprint.iacr.org/2024/640.pdf">paper</a>: Miller-loop outputs are unique only up to multiplication by an $r$-th power.
In other words, $f_1$ and $f_2$ stand for the same pairing whenever there is a non-zero $c$ with $f_1 = f_2 \cdot c^r$.
That undetermined factor $c$ is what makes a direct equality check tricky.</p>
<p>That is why <strong>the second step</strong> exists. The final exponentiation raises $f$ to</p>
$$ h = \frac{p^{12} - 1}{r}. $$

<p>This removes the ambiguity, because for every non-zero $c$, we have:</p>
$$ (f \cdot c^r)^h = f^h \cdot c^{p^{12}-1} = f^h. $$

<p>The last term disappears because every non-zero element of $\mathbb{F}_{p^{12}}$ satisfies $x^{p^{12}-1} = 1$.
After this exponentiation, the result lands in $G_T$, the group of $r$-th roots of unity.
So the real pairing-product check is:</p>
$$ f^h = 1. $$

<p>The problem is that the exponent $h$ is far too expensive to raise to inside the circuit, while it is fine to let the prover compute $c$ outside the circuit and pass it in as a hint.
Checking $f = c^r$ is much cheaper than computing the $f^h$ exponentiation.
So to prove $\prod_i e(P_i, Q_i) = f^h = 1$, instead of computing $f^h$ directly, the prover only needs to provide a non-zero $c$ with $f = c^r$, which holds exactly when $f^h = 1$.</p>
<p>This is the core idea behind the optimization.
OpenVM implements it with the residue-witness trick from Novakovic and Eagen's <a href="https://eprint.iacr.org/2024/640.pdf">paper</a>: the prover supplies a few extra values and the circuit checks a cheap equation instead of running the full exponentiation.</p>
<p>The actual optimized equation is slightly different from $f = c^r$:</p>
$$ f \cdot u = c^{\lambda} \wedge u^{d^i} = 1$$

<p>Here $\lambda = m \cdot r$ is a curve-specific exponent whose structure lets the circuit evaluate $c^\lambda$ cheaply through the Frobenius map, and $u$ is called the scaling factor.
In the OpenVM code this scaling factor is called <code>u</code> for BN254 and <code>s</code> for BLS12-381.
The remaining symbols are $d = \gcd(m, h)$ and $i = v_d(h)$.</p>
<p>The scaling factor is needed because $\lambda$ does not line up perfectly with the original $r$-residue check.
Theorem 3 of the paper closes that gap by requiring the scaling factor to satisfy a small root-of-unity relation, which is the $u^{d^i} = 1$ condition above.</p>
<p>For these particular curves, the paper gives an even cheaper route: instead of checking $u^{d^i} = 1$ directly, it is enough to restrict the scaling factor to the proper subfield $\mathbb{F}_{p^6} \subset \mathbb{F}_{p^{12}}$.
<img alt="Restrict &lt;!--MATHBLOCK44--&gt; to subfield" src="subfield_check.png" />
And this check is very cheap.
OpenVM stores an $\mathbb{F}_{p^{12}}$ element as six $\mathbb{F}_{p^2}$ coefficients:</p>
$$ [c_0, c_1, c_2, c_3, c_4, c_5]. $$

<p>Being in the $\mathbb{F}_{p^6}$ subfield means the odd-indexed coefficients are zero:</p>
$$ c_1 = c_3 = c_5 = 0. $$

<p>So the whole security-critical subfield test is just three equality checks.</p>
<h3 id="the-bug">The bug</h3>
<p>Recall the shape of the check.
The circuit has a combined Miller-loop output $f$, and it should accept only when the pairing product would become one after final exponentiation.
OpenVM avoided that expensive exponentiation by checking the optimized relation:</p>
$$ f \cdot u = c^\lambda. $$

<p>But that relation is sound only if $u$ is constrained to the right subfield.
OpenVM only checked that the hint $c$ was non-zero, and stopped there.
It did not check that the scaling factor was in $\mathbb{F}_{p^6}$.
Here is the BLS12-381 <a href="https://github.com/openvm-org/openvm/blob/69373ff1d06b613025fe4e7a02d735a1609412c4/guest-libs/pairing/src/bls12_381/pairing.rs#L320-L352">code path</a> before the fix:</p>
<div class="highlight"><pre><span></span><code><span class="c1">// guest-libs/pairing/src/bls12_381/pairing.rs</span>
<span class="kd">let</span><span class="w"> </span><span class="p">(</span><span class="n">c</span><span class="p">,</span><span class="w"> </span><span class="n">s</span><span class="p">)</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="bp">Self</span><span class="p">::</span><span class="n">pairing_check_hint</span><span class="p">(</span><span class="n">P</span><span class="p">,</span><span class="w"> </span><span class="n">Q</span><span class="p">);</span>
<span class="c1">// ... no check that s lies in Fp6 ...</span>
<span class="kd">let</span><span class="w"> </span><span class="n">c_conj</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">c</span><span class="p">.</span><span class="n">conjugate</span><span class="p">();</span>
<span class="k">if</span><span class="w"> </span><span class="n">c_conj</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">Fp12</span><span class="p">::</span><span class="n">ZERO</span><span class="w"> </span><span class="p">{</span><span class="w">   </span><span class="c1">// only rejects c == 0</span>
<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="nb">None</span><span class="p">;</span>
<span class="p">}</span>
</code></pre></div>
<p>BN254 had <a href="https://github.com/openvm-org/openvm/blob/69373ff1d06b613025fe4e7a02d735a1609412c4/guest-libs/pairing/src/bn254/pairing.rs#L351-L383">the same pattern</a>, just with <code>if c == Fp12::ZERO { return None; }</code>.
So the circuit rejected a zero $c$, but accepted any scaling factor.</p>
<p>At that point the optimized equation no longer proves the real pairing check.
For any Miller output $f$, even one coming from a false pairing equation, the prover can set:</p>
$$ c = 1, \qquad u = f^{-1}. $$

<p>Then $c^\lambda = 1$, and the checked relation becomes:</p>
$$ f \cdot f^{-1} = 1 = c^\lambda. $$

<p>The check passes.
The same substitution works on both curves: $c = 1, u = f^{-1}$ for BN254 and $c = 1, s = f^{-1}$ for BLS12-381.</p>
<p>Normally $f^{-1}$ is a full $\mathbb{F}_{p^{12}}$ element, not an element of the $\mathbb{F}_{p^6}$ subfield. That is exactly why the subfield check would have rejected the forgery.</p>
<p>There is also a subtle control-flow detail.
Because the optimized routine returned success, the slower fallback that would have performed the full final exponentiation was never reached.</p>
<h3 id="impact">Impact</h3>
<p>Forging an arbitrary pairing check breaks the cryptographic floor that a lot of things stand on:</p>
<ul>
<li>On BLS12-381, a prover can forge KZG opening proofs, which breaks the polynomial commitment schemes behind data availability, blob verification, and PLONK or KZG verifiers.</li>
<li>On BN254, the same forgery breaks Groth16 SNARK verifiers, BLS signature checks, and any bridge or protocol that relies on a pairing equation.</li>
<li>Any zkVM guest emulating the Ethereum <code>ecPairing</code> precompile at address <code>0x08</code> through OpenVM's pairing check would produce forged results, leading to incorrect EVM execution.</li>
</ul>
<p>So any L2 rollup, bridge, or privacy protocol that verifies a pairing inside an OpenVM guest program inherits the problem.
<a href="https://zkao.io/">zkao</a> rated it Critical, and the OpenVM maintainers confirmed it as Critical.</p>
<h3 id="the-fix">The fix</h3>
<p>The fix was to add the missing subfield membership test. It asserts that the odd-indexed coefficients of the scaling factor are zero:</p>
<div class="highlight"><pre><span></span><code><span class="c1">// the scaling factor is an honest hint only if it lies in the subfield Fp6</span>
<span class="k">for</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">3</span><span class="p">,</span><span class="w"> </span><span class="mi">5</span><span class="p">]</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="n">s</span><span class="p">.</span><span class="n">c</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">Fp2</span><span class="p">::</span><span class="n">ZERO</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="nb">None</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</code></pre></div>
<p>A scaling factor like $f^{-1}$ usually has non-zero odd coefficients, so it is rejected and the forgery disappears.
The fix landed in commit <a href="https://github.com/openvm-org/openvm/commit/a720e2c7ba529becd101dbad24c879bd5c1257f4"><code>a720e2c</code></a> and shipped in OpenVM 1.6.0.</p>
<h2 id="a-few-things-we-learned">A few things we learned</h2>
<p><strong>A naive LLM still hits a wall on a complex codebase.</strong>
This is the observation we opened with, and the experiment confirmed it: across two model generations, the plain LLM passes produced findings that all triaged down to Informative on OpenVM.
The reason is the one described above.
A zkVM does not decompose into independent primitives the way a library does, so the unit of work an agent has to pass upward is <em>knowledge about a module</em>, and that is genuinely hard to represent.</p>
<div class="callout callout-note">
<div class="callout-title">Note</div>
<div class="callout-body">
<p>Closing that gap is most of what context engineering for <a href="https://zkao.io/">zkao</a> is about, and we approach it both heuristically, by encoding how our experts actually read code in many past manual audits, and systematically, in how the harness moves information between agents without overflowing any single context window.
zkao found this bug by a flow named <code>cryptopsy</code>.
We will leave the details of how this flow works for a future blog post, but basically it combines comprehensive analysis with back-and-forth between the implementation and the academic literature behind it: known attacks, pitfalls, cryptanalysis results, and so on.
This simulates a small part of our manual audit process.</p>
</div>
</div>
<p><strong>Triage cannot just ask an LLM to produce a working PoC.</strong>
One of our first attempts at automated triage was to ask whether the LLM could turn its own report into a working PoC.
The idea was simple: if the PoC runs, the bug is real.
In practice, that signal was much weaker than it looked.
The model was very good at producing PoCs that passed, even when the reported issue was not real.
Enough nonsensical comments, hidden assumptions, patched helper functions, disabled checks, mocked state, and suspicious run flags can make almost any exploit look successful.
Validating those PoCs ended up taking more time than triaging the original report.
This is why we have spent much time since then on zkao and have improved its triaging process to reduce false positives. 
In another post, we will discuss how we achieved that and how zkao also learns from users who triage bugs, so that after the first few triages in a project, false positives are reduced even further.</p>
<h2 id="whats-next">What's next</h2>
<p>Our thanks to the OpenVM team, who triaged and fixed this quickly and shipped the fix in 1.6.0.
We thank <a href="https://x.com/theyisun">Yi Sun</a>, co-founder of <a href="https://www.axiom.xyz/">Axiom</a>, for valuable feedback on this blog post.
After this report, we worked with the OpenVM team on a more targeted engagement for OpenVM 2.0 release. <a href="https://zkao.io/">zkao</a> found additional high-impact issues there, and we will write about those in future blogs once the details are ready to share.</p>
<p>This is the second post in the series. We will keep publishing confirmed bugs from other projects as they are resolved, especially when they teach us something useful where AI auditing works, where it still fails, and what kind of human review is needed around it.</p>
<p>If you maintain a zkVM or a cryptography project and this is interesting to you, we would love to look at it alongside you, so that serious bugs get found and fixed before they ship.
Continuous AI coverage of this kind is exactly what <a href="https://zkao.io/">zkao</a> is built for.
Reach out at <a href="https://zksecurity.xyz/contact">zksecurity.xyz/contact</a>.</p>
        </div>

        <!-- Social Sharing -->
        <div class="social-sharing">
            <h3 class="social-sharing-title">Share This Article</h3>
            <div class="social-buttons">
                <a href="#" class="social-button twitter" id="share-twitter" target="_blank" rel="noopener noreferrer">
                    <svg viewBox="0 0 24 24" fill="currentColor">
                        <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path>
                    </svg>
                    Share on X
                </a>
                <a href="#" class="social-button linkedin" id="share-linkedin" target="_blank" rel="noopener noreferrer">
                    <svg viewBox="0 0 24 24" fill="currentColor">
                        <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"></path>
                    </svg>
                    Share on LinkedIn
                </a>
                <a href="#" class="social-button email" id="share-email">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                        <polyline points="22,6 12,13 2,6"></polyline>
                    </svg>
                    Share via Email
                </a>
            </div>
        </div>

        <!-- zkSecurity Services Signature -->
        <div class="zksecurity-signature">
            <p class="signature-text">
                <strong>zkSecurity</strong> offers auditing, research, and development services for cryptographic systems including zero-knowledge proofs, MPCs, FHE, consensus protocols and more.
            </p>
            <a href="https://zksecurity.xyz" target="_blank" rel="noopener noreferrer" class="signature-link">
                Learn More →
            </a>
        </div>
    </article>

    <!-- Related Posts Section -->
    <div class="related-posts-section">
        <div class="related-posts-columns">
            <!-- Latest Posts Column -->
            
            <div class="related-posts-column">
                <h2 class="related-posts-title">Latest Posts</h2>
                
                <a href="../../posts/circl-bugs/index.html" class="related-post-card">
                    <h3 class="related-post-title">AI meets Cryptography 1: What AI Found in Cloudflare's CIRCL</h3>
                    <div class="related-post-meta">
                        <span class="related-post-author">Stefanos Chaliasos, Hao Pham, False Witness team</span>
                        <span class="related-post-date">July 07, 2026</span>
                    </div>
                    
                    <div class="post-tags">
                        
                        <span class="tag">security</span>
                        
                        <span class="tag">crypto</span>
                        
                        <span class="tag">AI</span>
                        
                        <span class="tag">zkao</span>
                        
                        <span class="tag">audit</span>
                        
                    </div>
                    
                    <p class="related-post-summary">We pointed our AI audit pipeline at Cloudflare's CIRCL experimental cryptography library and confirmed seven real bugs, from a critical float64 precision loss in threshold RSA to a complete access-control break in attribute-based encryption. All seven are now fixed upstream. This is the first post in a series on bugs our agents found across open source cryptography.</p>
                </a>
                
                <a href="../../posts/zkgolf/index.html" class="related-post-card">
                    <h3 class="related-post-title">zk.golf: Fearless and Collaborative Optimization of Circuits</h3>
                    <div class="related-post-meta">
                        <span class="related-post-author">Giorgio Dell'Immagine, Mathias Hall-Andersen</span>
                        <span class="related-post-date">July 02, 2026</span>
                    </div>
                    
                    <div class="post-tags">
                        
                        <span class="tag">announcement</span>
                        
                        <span class="tag">zk</span>
                        
                        <span class="tag">optimization</span>
                        
                        <span class="tag">clean</span>
                        
                    </div>
                    
                    <p class="related-post-summary">zk.golf is a platform where people can compete on creating the most efficient zk circuits for specific problems. It is enabled by what we call "fearless optimization", which is achieved by combining formal verification and frontier AI models. By the end, you will be convinced that nobody should look at constraints ever again in their life.</p>
                </a>
                
                <a href="../../posts/mpc-pitfalls-bug-tracker/index.html" class="related-post-card">
                    <h3 class="related-post-title">New on mpcsec.org: An MPC Bug Tracker, Templates, and a Cleaner UI</h3>
                    <div class="related-post-meta">
                        <span class="related-post-author">ZK/SEC</span>
                        <span class="related-post-date">June 25, 2026</span>
                    </div>
                    
                    <div class="post-tags">
                        
                        <span class="tag">educative</span>
                        
                        <span class="tag">security</span>
                        
                        <span class="tag">MPC</span>
                        
                    </div>
                    
                    <p class="related-post-summary">A month after launching mpcsec.org, we added a searchable tracker of real-world MPC bugs, expanded the pitfall taxonomy, published contribution templates and refreshed the site UI.</p>
                </a>
                
            </div>
            

            <!-- Recommended Posts Column -->
            
            <div class="related-posts-column">
                <h2 class="related-posts-title">Recommended Reading</h2>
                
                <a href="../../posts/circl-bugs/index.html" class="related-post-card">
                    <h3 class="related-post-title">AI meets Cryptography 1: What AI Found in Cloudflare's CIRCL</h3>
                    <div class="related-post-meta">
                        <span class="related-post-author">Stefanos Chaliasos, Hao Pham, False Witness team</span>
                        <span class="related-post-date">July 07, 2026</span>
                    </div>
                    
                    <div class="post-tags">
                        
                        <span class="tag">security</span>
                        
                        <span class="tag">crypto</span>
                        
                        <span class="tag">AI</span>
                        
                        <span class="tag">zkao</span>
                        
                        <span class="tag">audit</span>
                        
                    </div>
                    
                    <p class="related-post-summary">We pointed our AI audit pipeline at Cloudflare's CIRCL experimental cryptography library and confirmed seven real bugs, from a critical float64 precision loss in threshold RSA to a complete access-control break in attribute-based encryption. All seven are now fixed upstream. This is the first post in a series on bugs our agents found across open source cryptography.</p>
                </a>
                
                <a href="../../posts/zkao-launch/index.html" class="related-post-card">
                    <h3 class="related-post-title">zkao: Security That Compounds</h3>
                    <div class="related-post-meta">
                        <span class="related-post-author">ZK/SEC</span>
                        <span class="related-post-date">February 07, 2026</span>
                    </div>
                    
                    <div class="post-tags">
                        
                        <span class="tag">zkao</span>
                        
                        <span class="tag">security</span>
                        
                        <span class="tag">zk</span>
                        
                        <span class="tag">AI</span>
                        
                    </div>
                    
                    <p class="related-post-summary">Today we're launching zkao, a product by zkSecurity that makes AI security research work the way fuzzing works: not as a one-shot event, but as something you run continuously until coverage compounds.</p>
                </a>
                
                <a href="../../posts/zkvm-security/index.html" class="related-post-card">
                    <h3 class="related-post-title">zkVM Security: What Could Go Wrong?</h3>
                    <div class="related-post-meta">
                        <span class="related-post-author">Suneal Gong</span>
                        <span class="related-post-date">November 21, 2024</span>
                    </div>
                    
                    <div class="post-tags">
                        
                        <span class="tag">educative</span>
                        
                        <span class="tag">security</span>
                        
                        <span class="tag">zk</span>
                        
                        <span class="tag">zkvm</span>
                        
                    </div>
                    
                    <p class="related-post-summary">Ever wondered how zkVMs simplify the use of zero-knowledge proofs in coding? We dive into how they let developers focus more on application logic by abstracting complex cryptographic aspects, using familiar languages like Rust or C++. But hold on, it's not all smooth sailing. Despite these benefits, a single bug anywhere in the complex system of compilers, proof systems, or verification can lead to serious security issues. In the post, we break down the zkVM workflow, explore common vulnerabilities at each phase, and highlight the importance of understanding these layers to build more secure, zk-powered applications. Curious about how this all plays out? Let’s unravel it together!</p>
                </a>
                
                <a href="../../posts/llms-in-research/index.html" class="related-post-card">
                    <h3 class="related-post-title">When LLM Review Cryptography Papers</h3>
                    <div class="related-post-meta">
                        <span class="related-post-author">Nicolas Mohnblatt</span>
                        <span class="related-post-date">February 10, 2026</span>
                    </div>
                    
                    <div class="post-tags">
                        
                        <span class="tag">educative</span>
                        
                        <span class="tag">security</span>
                        
                        <span class="tag">zk</span>
                        
                        <span class="tag">AI</span>
                        
                    </div>
                    
                    <p class="related-post-summary">Google Research used Gemini to find a bug in a cryptography paper on SNARGs from LWE. We summarize how those events unfolded, look at their iterative self-correction prompting strategy and discuss the growing role of LLMs in academic research.</p>
                </a>
                
            </div>
            

            <!-- Random Posts Column -->
            
            <div class="related-posts-column">
                <h2 class="related-posts-title">More to Explore</h2>
                
                <a href="../../posts/pcs-survey/index.html" class="related-post-card">
                    <h3 class="related-post-title">KZG vs IPA vs FRI: Picking the Right Polynomial Commitment Scheme</h3>
                    <div class="related-post-meta">
                        <span class="related-post-author">ZK/SEC, University of Padua</span>
                        <span class="related-post-date">March 23, 2026</span>
                    </div>
                    
                    <div class="post-tags">
                        
                        <span class="tag">educative</span>
                        
                        <span class="tag">zk</span>
                        
                        <span class="tag">pcs</span>
                        
                        <span class="tag">polynomial-commitment</span>
                        
                    </div>
                    
                    <p class="related-post-summary">A practical guide to the trade-offs between KZG, IPA/Halo, and FRI, the three major polynomial commitment scheme families powering modern zero-knowledge proof systems. We compare proof sizes, verification costs, trust assumptions, benchmarks, and on-chain gas costs.</p>
                </a>
                
                <a href="../../posts/barrett-tighter-bound/index.html" class="related-post-card">
                    <h3 class="related-post-title">Optimizing Barrett Reduction: Tighter Bounds Eliminate Redundant Subtractions</h3>
                    <div class="related-post-meta">
                        <span class="related-post-author">Suneal Gong</span>
                        <span class="related-post-date">May 01, 2025</span>
                    </div>
                    
                    <div class="post-tags">
                        
                        <span class="tag">educative</span>
                        
                    </div>
                    
                    <p class="related-post-summary">In this blog post, we explore an optimization for Barrett reduction, a popular method for modular arithmetic. We discovered that the error bound can be tighter than traditionally thought, meaning you often only need a single subtraction instead of two. This tweak can speed up cryptographic operations like those in the RustCrypto library by 14% when applied to NIST curves, which is a game changer for both encryption and performance. Dive into the details to see how this simple change can lead to significant improvements in real-world applications!</p>
                </a>
                
                <a href="../../posts/stark-evm-adapter/index.html" class="related-post-card">
                    <h3 class="related-post-title">Verifying Cairo proofs on Ethereum</h3>
                    <div class="related-post-meta">
                        <span class="related-post-author">Jason Park</span>
                        <span class="related-post-date">August 06, 2024</span>
                    </div>
                    
                    <div class="post-tags">
                        
                        <span class="tag">tools</span>
                        
                        <span class="tag">zk</span>
                        
                    </div>
                    
                    <p class="related-post-summary">We've been teaming up with StarkWare to create the EVM adapter, and we're thrilled to say that we've recently verified Cairo proofs on the Ethereum mainnet! Building on the work of Andrew Milson and Aditya Bisht, we're making StarkWare’s technology more accessible to everyone. Our blog dives into how Cairo programs are verified on Ethereum and showcases our new library, `stark-evm-adapter`, which helps parse Cairo proofs for Ethereum. Interested in seeing how it works? Check out our demo and learn how to integrate this tech into your system. Plus, stay tuned for future updates as we refine and expand this exciting tool!</p>
                </a>
                
            </div>
            
        </div>

        <div style="text-align: center; margin-top: 2rem;">
            <a href="../../index.html" class="back-link" style="display: inline-flex; align-items: center; gap: 0.5rem;">
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M10 13l-5-5 5-5"/>
                </svg>
                View all articles
            </a>
        </div>
    </div>

    <footer class="site-footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <span class="footer-label">Research Publication</span>
                    <span class="footer-value">ZK/SEC Quarterly</span>
                </div>
                <div class="footer-section">
                    <span class="footer-label">Volume</span>
                    <span class="footer-value">2026</span>
                </div>
                <div class="footer-section">
                    <span class="footer-label">Author</span>
                    <span class="footer-value">Stefanos Chaliasos, Hao Pham</span>
                </div>
                <div class="footer-section">
                    <span class="footer-label">Links</span>
                    <div class="footer-links-section">
                        <a href="https://zksecurity.xyz" class="footer-value-link" target="_blank" rel="noopener noreferrer">Home</a>
                        <a href="https://reports.zksecurity.xyz" class="footer-value-link" target="_blank" rel="noopener noreferrer">Reports</a>
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <!-- Reading progress indicator -->
    <div class="reading-progress"></div>

    <script>
        document.addEventListener("DOMContentLoaded", function() {
            // Social sharing
            const pageUrl = encodeURIComponent(window.location.href);
            const pageTitle = encodeURIComponent(document.title);

            // Twitter/X
            const twitterBtn = document.getElementById('share-twitter');
            if (twitterBtn) {
                twitterBtn.href = `https://twitter.com/intent/tweet?url=${pageUrl}&text=${pageTitle}`;
            }

            // LinkedIn
            const linkedinBtn = document.getElementById('share-linkedin');
            if (linkedinBtn) {
                linkedinBtn.href = `https://www.linkedin.com/sharing/share-offsite/?url=${pageUrl}`;
            }

            // Email
            const emailBtn = document.getElementById('share-email');
            if (emailBtn) {
                emailBtn.href = `mailto:?subject=${pageTitle}&body=Check out this article: ${pageUrl}`;
            }

            // Reading progress indicator
            const progressBar = document.querySelector('.reading-progress');
            if (progressBar) {
                window.addEventListener('scroll', function() {
                    const article = document.querySelector('.post-body');
                    if (!article) return;

                    const articleTop = article.offsetTop;
                    const articleHeight = article.offsetHeight;
                    const windowHeight = window.innerHeight;
                    const scrollTop = window.scrollY;

                    const progress = Math.min(100, Math.max(0,
                        ((scrollTop - articleTop + windowHeight/2) / articleHeight) * 100
                    ));

                    progressBar.style.width = progress + '%';
                });
            }
        });
    </script>
</body>
</html>