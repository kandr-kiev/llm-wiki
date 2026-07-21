---
source_url: https://minikotlin.run
ingested: 2026-07-17
sha256: d36a38c6052de5cacd69610d8d0b077a1f2147b4fc24e20e948995a0219c30e7
blog_source: Hacker News
---
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>minikotlin â a Kotlin compiler that runs in a browser tab</title>
<meta name="description" content="minikotlin is a from-scratch Kotlin-to-WebAssembly compiler written in C. The compiler itself is compiled to WASM, so the whole toolchain runs client-side. Write multi-file Kotlin in the Studio, hit Run, watch output.">
<link rel="icon" href="./assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="./assets/index.css">
</head>
<body>

<header class="top">
  <div class="wrap">
    <a class="brand" href="#top" aria-label="minikotlin home">
      <img class="mark" src="./assets/favicon.svg" alt="" />
      <span class="name"><span class="mini">mini</span><span class="core">kotlin</span></span>
    </a>
    <nav class="nav">
      <a href="#pipeline">pipeline</a>
      <a href="#features">language</a>
      <a href="#lowering">lowerings</a>
      <a href="#specimen">specimen</a>
      <a href="coverage.html">coverage</a>
      <a class="btn btn-primary" href="studio/">Open Studio
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true"><use href="./assets/sprite.svg#ico-arrow"/></svg>
      </a>
    </nav>
  </div>
</header>

<main id="top">

  <!-- ================= HERO ================= -->
  <section class="hero">
    <div class="wrap">
      <div class="copy">
        <span class="eyebrow"><span class="dot"></span>Kotlin <b>â</b> WebAssembly &nbsp;Â·&nbsp; a compiler written in C</span>
        <h1 class="display">A Kotlin compiler<br>that runs in a <em>browser tab.</em></h1>
        <p class="lede">minikotlin is written from scratch in C and emits <strong>WebAssembly&nbsp;GC bytecode by hand</strong> â no JVM, no LLVM, no Binaryen, no Gradle. The compiler is itself compiled to WASM, so <code>.kt</code> source goes in and a running <code>.wasm</code> module comes out, <strong>entirely in the tab</strong>.</p>
        <div class="cta-row">
          <a class="btn btn-primary btn-lg" href="studio/">Open the Studio
            <svg width="15" height="15" viewBox="0 0 16 16" fill="none" aria-hidden="true"><use href="./assets/sprite.svg#ico-arrow"/></svg>
          </a>
          <a class="btn btn-ghost btn-lg" href="#specimen">Read a specimen</a>
        </div>
        <dl class="herometa">
          <div><dt>backend</dt><dd>WASM-GC<small>structs Â· call_ref Â· EH</small></dd></div>
          <div><dt>server</dt><dd>none<small>runs client-side</small></dd></div>
          <div><dt>end-to-end tests</dt><dd>366<small>frontend: 657</small></dd></div>
          <div><dt>runtime deps</dt><dd>0<small>nothing installed</small></dd></div>
        </dl>
      </div>

      <!-- ===== Studio mock ===== -->
      <div class="studio" aria-label="minikotlin Studio preview">
        <div class="studio-bar">
          <span class="tab"><b>greeter</b> â minikotlin Studio</span>
          <button class="run" type="button" tabindex="-1" aria-hidden="true">
            <svg viewBox="0 0 10 10" fill="currentColor"><use href="./assets/sprite.svg#ico-run"/></svg>RUN
          </button>
        </div>
        <div class="studio-body">
          <aside class="rail">
            <div class="grp">greeter / src</div>
            <div class="file active">
              <svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><use href="./assets/sprite.svg#ico-file"/></svg>
              Main.kt
            </div>
            <div class="file">
              <svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><use href="./assets/sprite.svg#ico-file"/></svg>
              Greeter.kt
            </div>
            <div class="grp" style="margin-top:14px">output</div>
            <div class="file">
              <svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><use href="./assets/sprite.svg#ico-console"/></svg>
              Console
            </div>
          </aside>

          <div class="editor">
            <div class="codepane">
              <div class="gutter" aria-hidden="true">
                <span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span>
              </div>
<pre class="code"><span class="cm">// Main.kt + Greeter.kt compile as one unit</span>
<span class="kw">fun</span> <span class="fn">main</span>() {
    <span class="kw">val</span> g = <span class="ty">Greeter</span>(<span class="st">"WebAssembly"</span>)
    <span class="fn">println</span>(g.greet())
    (<span class="nu">1</span>..<span class="nu">3</span>).<span class="fn">forEach</span> { <span class="fn">println</span>(<span class="st">"tick </span>$<span class="mu">it</span><span class="st">"</span>) }
}</pre>
            </div>
            <div class="console" aria-label="console output">
              <div class="ln"><span class="meta2">build </span><span class="prompt">2 .kt &rarr; main.wasm</span> <span class="meta2">Â·</span> <span class="ok">ok, 41ms</span></div>
              <div class="ln">Hello, WebAssembly</div>
              <div class="ln">tick 1</div>
              <div class="ln">tick 2</div>
              <div class="ln">tick 3<span class="caret"></span></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== static pipeline rule (no marquee) ===== -->
  <div class="pipeband">
    <div class="wrap">
      <span class="lead">the pipeline</span>
      <span class="stg"><b>.kt</b></span><span class="arr">â</span>
      <span class="stg">lex</span><span class="arr">â</span>
      <span class="stg">parse</span><span class="arr">â</span>
      <span class="stg">sema</span><span class="arr">â</span>
      <span class="stg"><b>HIR</b></span><span class="arr">â</span>
      <span class="stg"><b>MIR</b></span><span class="arr">â</span>
      <span class="stg"><b>WASM-GC</b></span><span class="arr">â</span>
      <span class="stg">run</span>
    </div>
  </div>

  <!-- ================= PIPELINE ================= -->
  <section id="pipeline">
    <div class="wrap">
      <div class="sec-head">
        <span class="sec-num">01</span>
        <h2>One pass, all the way down to bytecode.</h2>
        <p class="sub">No intermediate VM, no external backend. The frontend â lexer, parser, semantic analysis (it&rsquo;s called <b>mkf</b>) â hands off to two of its own IRs before writing WASM-GC by hand.</p>
      </div>

      <div class="pipe">
        <div class="stage in">
          <div class="k"><i></i>input</div>
          <div class="v">Kotlin source</div>
          <div class="d">Multiple <code>.kt</code> files, compiled as one unit so they can see each other.</div>
        </div>
        <div class="stage">
          <div class="k"><i></i>frontend Â· mkf</div>
          <div class="v">lex Â· parse Â· sema</div>
          <div class="d">Names, types and smart-casts resolved. 657 frontend tests.</div>
        </div>
        <div class="stage">
          <div class="k"><i></i>high IR</div>
          <div class="v">HIR</div>
          <div class="d">A desugared, typed tree that still sits close to the language.</div>
        </div>
        <div class="stage">
          <div class="k"><i></i>mid IR</div>
          <div class="v">MIR</div>
          <div class="d">Lowered to ops, locals, struct layouts and vtables.</div>
        </div>
        <div class="stage">
          <div class="k"><i></i>codegen</div>
          <div class="v">WASM-GC</div>
          <div class="d">Bytecode emitted directly. No LLVM, no Binaryen in the loop.</div>
        </div>
        <div class="stage out">
          <div class="k"><i></i>output</div>
          <div class="v">main.wasm</div>
          <div class="d">Instantiated and run in the same browser tab.</div>
        </div>
      </div>
      <p class="pipe-foot">The compiler <b>ships as WASM itself</b>, so it runs where your code runs â no toolchain to install.</p>
    </div>
  </section>

  <hr class="rule">

  <!-- ================= LANGUAGE / SPEC ================= -->
  <section id="features">
    <div class="wrap">
      <div class="sec-head">
        <span class="sec-num">02</span>
        <h2>The Kotlin it speaks today.</h2>
        <p class="sub">Not a token subset. These are lowered properly onto the WASM-GC type system â each one has end-to-end tests behind it.</p>
      </div>

      <dl class="spec">
        <div class="row">
          <dt>Classes &amp; objects<small>object model</small></dt>
          <dd>Inheritance (<code>open</code>/<code>override</code>), interfaces with default methods, <code>data class</code> with generated <code>equals</code>/<code>hashCode</code>/<code>copy</code>, <code>enum</code>, and named, companion &amp; anonymous <code>object</code> expressions.</dd>
        </div>
        <div class="row">
          <dt>Sealed &amp; smart-casts<small>control flow</small></dt>
          <dd><code>sealed</code> hierarchies with exhaustive <code>when</code>, <code>is</code> checks compiled to <code>ref.test</code>, and flow-sensitive smart-casting that holds across branches.</dd>
        </div>
        <div class="row">
          <dt>Null safety<small>types</small></dt>
          <dd>Nullable types end to end â <code>?.</code> safe calls, <code>?:</code> elvis and <code>!!</code> assertions â including nullable primitives, boxed through <code>Any</code>.</dd>
        </div>
        <div class="row">
          <dt>Generics<small>types</small></dt>
          <dd>Type parameters on functions and classes â <code>fun &lt;T&gt; id(x: T): T</code> â lowered over a boxed <code>Any</code> representation.</dd>
        </div>
        <div class="row">
          <dt>Operators &amp; extensions<small>ergonomics</small></dt>
          <dd>Operator overloading (<code>plus</code>, <code>get</code>, &hellip;) dispatched to the LHS class, extension functions in their own namespace, and custom accessors with a backing <code>field</code>.</dd>
        </div>
        <div class="row">
          <dt>Coroutines<small>non-blocking</small></dt>
          <dd><code>launch</code>, <code>delay</code> and <code>coroutineScope</code> â real suspension compiled as CPS over closures, with no Asyncify, no JSPI and no threads.</dd>
        </div>
        <div class="row">
          <dt>Standard library<small>hand-written</small></dt>
          <dd><code>String</code>/<code>Char</code> operations, list higher-order functions (<code>map</code>/<code>filter</code>/<code>forEach</code>&hellip;), <code>kotlin.math</code>, and the scope functions <code>let</code>/<code>apply</code>/<code>run</code>/<code>also</code>/<code>with</code>.</dd>
        </div>
      </dl>
    </div>
  </section>

  <hr class="rule">

  <!-- ================= LOWERING (the hook) ================= -->
  <section id="lowering">
    <div class="wrap">
      <div class="sec-head">
        <span class="sec-num">03</span>
        <h2>How a Kotlin idea becomes a WASM instruction.</h2>
        <p class="sub">The lowering is the interesting part of any compiler. Four real ones â each maps a language construct onto a concrete WASM-GC mechanism, written by hand.</p>
      </div>

      <div class="two">
        <div class="cell">
          <div class="n">L.01</div>
          <h3>class instance <span class="ar">â</span> <span class="mono">struct.new</span></h3>
          <p>Every class becomes a GC <code>struct</code> type; properties are real struct fields. Allocation is <code>struct.new</code>, not a hand-rolled heap of bytes.</p>
        </div>
        <div class="cell">
          <div class="n">L.02</div>
          <h3>virtual call <span class="ar">â</span> <span class="mono">call_ref</span></h3>
          <p>Open and overridden methods go through a per-class vtable. A virtual call is a function-reference load followed by <code>call_ref</code> â true dynamic dispatch.</p>
        </div>
        <div class="cell">
          <div class="n">L.03</div>
          <h3>type check <span class="ar">â</span> <span class="mono">ref.test</span></h3>
          <p>An <code>is</code> check and a <code>when (x) { is T -&gt; }</code> arm compile to <code>ref.test</code>, and the narrowed value is reused through a <code>ref.cast</code> â smart-casting for free.</p>
        </div>
        <div class="cell">
          <div class="n">L.04</div>
          <h3>coroutine <span class="ar">â</span> <span class="mono">CPS closure</span></h3>
          <p>A suspension point splits the function at the seam and captures the rest as a continuation. A bare <code>delay</code> hands a token to the host and resumes from <code>setTimeout</code> â genuinely off the stack.</p>
        </div>
      </div>
    </div>
  </section>

  <hr class="rule">

  <!-- ================= SPECIMEN / COROUTINES ================= -->
  <section id="specimen">
    <div class="wrap">
      <div class="sec-head">
        <span class="sec-num">04</span>
        <h2>A specimen, compiled and run.</h2>
        <p class="sub">Everything below is supported Kotlin. The Studio highlights it with the compiler&rsquo;s own lexer, then runs the resulting WASM in place.</p>
      </div>

      <div class="specimen">
        <div class="card">
          <div class="cap">
            <svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><use href="./assets/sprite.svg#ico-file"/></svg>
            Race.kt
          </div>
<pre><span class="kw">import</span> kotlinx.coroutines.*

<span class="kw">sealed class</span> <span class="ty">Lane</span>(<span class="kw">val</span> id: <span class="ty">Int</span>)
<span class="kw">class</span> <span class="ty">Fast</span> : <span class="ty">Lane</span>(<span class="nu">1</span>)
<span class="kw">class</span> <span class="ty">Slow</span> : <span class="ty">Lane</span>(<span class="nu">2</span>)

<span class="kw">fun</span> <span class="ty">Lane</span>.<span class="fn">pace</span>(): <span class="ty">Long</span> = <span class="kw">when</span> (<span class="kw">this</span>) {
    <span class="kw">is</span> <span class="ty">Fast</span> -> <span class="nu">120</span>
    <span class="kw">is</span> <span class="ty">Slow</span> -> <span class="nu">300</span>
}

<span class="kw">fun</span> <span class="fn">main</span>() = <span class="fn">runBlocking</span> {
    <span class="kw">val</span> lanes = <span class="fn">listOf</span>(<span class="ty">Fast</span>(), <span class="ty">Slow</span>())
    <span class="fn">coroutineScope</span> {
        lanes.<span class="fn">forEach</span> { lane -><span class="cm"></span>
            <span class="fn">launch</span> {
                <span class="fn">delay</span>(lane.<span class="fn">pace</span>())
                <span class="fn">println</span>(<span class="st">"lane </span>$<span class="mu">{lane.id}</span><span class="st"> in"</span>)
            }
        }
    }
    <span class="fn">println</span>(<span class="st">"race over"</span>)
}</pre>
        </div>

        <div class="prose">
          <h3>Two coroutines, actually racing.</h3>
          <p>Each <code>launch</code> suspends at its <code>delay</code> and yields. The faster lane resumes first; <code>coroutineScope</code> waits for both children before the last line runs. <strong>No blocking and no Asyncify</strong> â the suspension is compiled into continuation closures.</p>
          <p>The sealed <code>Lane</code>, the <code>when (this) { is &hellip; }</code> dispatch and the <code>Lane.pace()</code> extension are all lowered for real, not interpreted.</p>
          <div class="out">
            <div><span class="meta2">&gt;</span> lane 1 in</div>
            <div><span class="meta2">&gt;</span> lane 2 in</div>
            <div><span class="ok">&gt;</span> race over</div>
          </div>
        </div>
      </div>
    </div>
  </section>

</main>

<!-- ================= CLOSING ================= -->
<section class="closing">
  <div class="wrap">
    <div>
      <h2>The Studio is the <em>whole thing.</em></h2>
      <p>Make a project, write a few <code>.kt</code> files that compile as one unit so they can see each other, hit Run, and read the output â all in the tab, nothing installed.</p>
    </div>
    <div class="act">
      <a class="btn btn-primary btn-lg" href="studio/">Open the Studio
        <svg width="15" height="15" viewBox="0 0 16 16" fill="none" aria-hidden="true"><use href="./assets/sprite.svg#ico-arrow"/></svg>
      </a>
      <span class="note">multi-file editor Â· runs offline Â· 0 dependencies</span>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="foot-left">
      <a class="brand" href="#top" aria-label="minikotlin home">
        <img class="mark" src="./assets/favicon.svg" alt="" style="width:20px;height:20px" />
        <span class="name"><span class="mini">mini</span><span class="core">kotlin</span></span>
      </a>
      <span class="credit">Made by <a href="https://toprak.run" target="_blank" rel="noopener">UÄur&nbsp;Toprakdeviren</a></span>
    </div>
    <div class="meta">
      A from-scratch Kotlin <b>&rarr;</b> WebAssembly compiler, written in <b>C</b>.<br>
      No JVM Â· no LLVM Â· no Gradle Â· no server. It runs in the browser tab.
    </div>
  </div>
</footer>

</body>
</html>