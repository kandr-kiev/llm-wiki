---
source_url: https://www.abuseofcats.com
ingested: 2026-07-18
sha256: e37a2274903f308ccc10a333662a8af11c16374e21994abaa19e2b1bf098fde0
blog_source: Hacker News
---
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>abuseofcats.com — stop abusing cat(1)</title>
<meta name="description" content="cat file | grep is abuse. grep can open files by itself. Stop the useless use of cat.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0D1117;
    --fg: #C9D1D9;
    --dim: #8B949E;
    --green: #3FB950;
    --red: #F85149;
    --rule: #21262D;
    --code-bg: #161B22;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    background: var(--bg);
    color: var(--fg);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 16px;
    line-height: 1.7;
    display: flex;
    min-height: 100vh;
    justify-content: center;
  }
  main {
    width: 100%;
    max-width: 680px;
    padding: 10vh 24px 64px;
  }
  a { color: var(--fg); }
  .dim { color: var(--dim); }
  .prompt { color: var(--green); user-select: none; }
  .bad { color: var(--red); }
  .good { color: var(--green); }
  h1 {
    font-size: 16px;
    font-weight: 400;
    color: var(--dim);
  }
  .block { margin-top: 44px; }
  pre.codeblock {
    background: var(--code-bg);
    border: 1px solid var(--rule);
    border-radius: 6px;
    padding: 16px 20px;
    font-family: inherit;
    font-size: clamp(15px, 3vw, 19px);
    font-weight: 600;
    overflow-x: auto;
  }
  .block.abuse pre.codeblock { border-left: 3px solid var(--red); }
  .block.humane pre.codeblock { border-left: 3px solid var(--green); }
  .strike { text-decoration: line-through; text-decoration-color: var(--red); text-decoration-thickness: 2px; }
  .verdict { margin-top: 10px; }
  .ascii {
    white-space: pre;
    line-height: 1.25;
    margin-top: 16px;
    display: inline-block;
  }
  .why { margin-top: 44px; max-width: 60ch; }
  .why p + p { margin-top: 16px; }
  .also { margin-top: 44px; border-top: 1px solid var(--rule); padding-top: 28px; }
  .also table { border-collapse: collapse; margin-top: 12px; font-size: 14px; }
  .also td { padding: 5px 0; vertical-align: top; }
  .also td:first-child { padding-right: 20px; }
  .also .bad { text-decoration: line-through; text-decoration-thickness: 1.5px; }
  @media (max-width: 560px) {
    .also td { display: block; }
    .also td:first-child { padding-top: 12px; }
  }
  footer {
    margin-top: 56px;
    border-top: 1px solid var(--rule);
    padding-top: 24px;
    font-size: 14px;
    color: var(--dim);
  }
</style>
</head>
<body>
<main>
  <h1>abuseofcats.com — a public service announcement about <a href="https://man7.org/linux/man-pages/man1/cat.1.html">cat(1)</a></h1>

  <div class="block abuse">
    <pre class="codeblock"><span class="prompt">$</span> <span class="strike">cat /etc/app/config | grep -v '^#'</span></pre>
    <div class="verdict bad">abuse. this cat did nothing wrong.</div>
    <span class="ascii bad"> /\_/\
( ;_; )
 &gt; ^ &lt;</span>
  </div>

  <div class="block humane">
    <pre class="codeblock"><span class="prompt">$</span> grep -v '^#' /etc/app/config</pre>
    <div class="verdict good">humane. same output, one less process.</div>
    <span class="ascii good"> /\_/\
( ^.^ )
 &gt; ^ &lt;</span>
  </div>

  <div class="why">
    <p>grep can open files by itself. Piping a single file through
    cat spawns an entire process whose only job is to copy bytes to a
    program that already knew how to read them.</p>
    <p><a href="https://man7.org/linux/man-pages/man1/cat.1.html">cat(1)</a> is for con<strong>cat</strong>enating files. Let cat be cat.</p>
  </div>

  <div class="also">
    <span class="dim">other cats in danger:</span>
    <table>
      <tr><td class="bad">cat file | wc -l</td><td class="good">wc -l &lt; file</td></tr>
      <tr><td class="bad">cat file | head -n 5</td><td class="good">head -n 5 file</td></tr>
      <tr><td class="bad">cat file | awk '{print $1}'</td><td class="good">awk '{print $1}' file</td></tr>
      <tr><td class="bad">cat file | sort</td><td class="good">sort file</td></tr>
    </table>
  </div>

  <footer>
    by <a href="https://www.jeremieking.com">Scooter aka Jeremie King</a> · feedback&commat;jeremieking.com
  </footer>
</main>
</body>
</html>
