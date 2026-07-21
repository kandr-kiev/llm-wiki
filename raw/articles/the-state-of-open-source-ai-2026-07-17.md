---
source_url: https://stateofopensource.ai/
ingested: 2026-07-17
sha256: 65e4a570cbcd5372ba2d6017fb3dbe9de3e02d8c26924f3820cccf72ce0e49a7
blog_source: Hacker News AI
---
<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-6B196E081B"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-6B196E081B');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The State of Open Source AI — V1.0 · July 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800;900&family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body id="report-root">
<div class="tooltip" id="tip"></div>
<nav>
  <div class="wrap navin">
    <a class="brand" href="#top"><img class="moz-logo nav" src="assets/img/moz-logo.png" alt="Mozilla"><span>State of open source <b>AI</b>.</span></a>
    <div class="nav-btns">
      <a class="nav-cta ghost" href="state-of-open-source-ai-2026.pdf" title="Download the full report (PDF)">Download full report</a>
      <a class="nav-cta" href="#letter" onclick="openLetter(event)">CTO's Letter</a>
    </div>
  </div>
</nav>

<!-- ============ HERO ============ -->
<header class="hero" id="top">
  <div class="wrap">
    <img class="moz-logo reveal" src="assets/img/moz-logo.png" alt="Mozilla">
    <h1 class="reveal">The state of<br>open source <span class="gtxt">AI</span><span class="dot">.</span></h1>
    <p class="hero-intro reveal">V1.0 &middot; Recurring &middot; July 2026</p>
  </div>
</header>

<!-- ============ OPENING LETTER ============ -->
<section class="letter" id="letterquote">
  <div class="wrap">
    <span class="letter-chip reveal">A Letter From Our CTO, Raffi Krikorian</span>
    <span class="qmark reveal">&ldquo;</span>
    <p class="quote reveal">In New Zealand's far north, a M&#257;ori broadcaster trains speech models for te reo &mdash; a language too small for any market &mdash; under a license that keeps the data with its people. PwC, one of the largest accounting firms in the world, fine-tuned an open model on the language of finance and runs it today for hundreds of clients, on its own hardware, with no per-token meter running. Researchers in Lausanne built an open medical model with the Red Cross, tuned to its humanitarian guidelines, and are preparing clinical trials at home and in Tanzania. In East Africa, farmers diagnose cassava disease with a model that runs on the phone itself, offline, in fields the cloud has never reached. In Switzerland, a public consortium trained a national model on public supercomputers and released all of it: weights, data, training code. None of them asked permission, and none of them could have rented this. They own it &mdash; that is the whole idea.</p>
    <p class="quote reveal">We have been here before. Mozilla exists because one company tried to own the front door to the web, and an open community rose up to make sure it never could. Twenty-five years later, someone is running the same play. <span class="qhl">We bet on open the first time. Open won. Together, we can do it again.</span></p>
    <p class="quote reveal">Our belief is simple: the path forward is competition and interoperability. We believe in a world of many models, standard ways to plug them together, and the freedom to walk away from any vendor at any time. Open has a record here. It grew the pie and let more people own a slice of it.</p>
    <p class="quote reveal">Read what follows as a map: where open AI is winning &mdash; some numbers surprised even us &mdash; and where it is exposed. A case that hides its weak points is an advertisement.&rdquo;</p>
    <div class="letter-actions reveal"><a class="letter-link" href="#letter" onclick="openLetter(event)">Read Raffi's full letter here <span class="arrow">&rarr;</span></a><a class="letter-link dl" href="state-of-open-source-ai-2026.pdf" title="Download the full report (PDF)">Download the report here <span class="arrow">&darr;</span></a></div>
  </div>
</section>

<!-- ============ STAT BAND ============ -->
<div class="statband">
  <div class="wrap stats2">
    <div class="stat-lede reveal">Open weights closed the capability gap while the price of intelligence collapsed.</div>
    <div class="stat reveal"><div class="num" data-count="3.3" data-suffix="%">0%</div><div class="lab">Capability gap to the top closed models &mdash; at parity on coding, behind on reasoning</div></div>
    <div class="stat reveal"><div class="num" data-count="50" data-prefix="" data-suffix="&times;">0&times;</div><div class="lab">Fall in GPT-4-class inference cost in 36 months: $20 &rarr; $0.40 per 1M tokens</div></div>
  </div>
</div>

<!-- ============ SECTION 01: CURRENT STATE ============ -->
<section id="state">
  <div class="wrap">
    <div class="section-tag reveal"><span class="section-num">01</span><span class="section-label">The current state of open-source AI</span></div>
    <h2 class="sec reveal">Parity reached. The contest is one layer up.</h2>
    <p class="lede reveal">Open weights are no longer a compromise. They are where the work happens: a majority of production tokens now route through them, and the five highest-volume models on OpenRouter are all open. Closed models still lead at the frontier, on reasoning and multimodality, but the frontier is not what most workloads need. Commodity inputs do not hold pricing power. Value moves up, to the agentic harness.</p>

    <div class="panel reveal">
      <div class="panel-title">The capability gap: 8.04% &rarr; 0.5% &rarr; 3.3%</div>
      <div class="panel-sub">Open-vs-closed gap on Chatbot Arena over 24 months. By August 2024, the gap had collapsed to 0.5%, and in February 2025 DeepSeek-R1 briefly matched the top US model. By March 2026 it had reopened to 3.3% as closed reasoning models pulled ahead. But 3.3% is an average over a jagged frontier: open is at or near parity on coding, instruction-following and general knowledge, while the gap concentrates in reasoning, long-context retrieval and agentic tasks. The question is no longer whether open models are good enough. It's what you need for your workload. Hover the points.</div>
      <div id="gapChart"></div>
      <div class="caption">Source: Chatbot Arena, Jan 2024 &ndash; Mar 2026.</div>
    </div>

    <div class="grid2">
      <div class="panel reveal">
        <div class="panel-title">Inference fell 50&times; in 36 months</div>
        <div class="panel-sub">GPT-4-equivalent price per 1M tokens &mdash; faster than dotcom-era bandwidth or PC-compute price curves. Log scale.</div>
        <div id="costChart"></div>
        <div class="caption">Sources: Stanford HAI AI Index 2025 (280&times; GPT-3.5-class drop over 18 months); Epoch AI (9&ndash;900&times; annual decay); Nov 2025 MIT study (5&ndash;10&times;/yr at the frontier, hardware-adjusted).</div>
      </div>
      <div class="panel reveal">
        <div class="panel-title">Open weights win the tokens</div>
        <div class="panel-sub">The share of tokens routed on OpenRouter through open-weight models grew from a negligible base to a third by late 2025 to a majority by mid-2026.</div>
        <div id="shareChart"></div>
        <div class="caption">Source: OpenRouter 100T-token study (Nov 2024&ndash;Nov 2025) and live leaderboard; intermediate points interpolated. By request count, closed US providers still lead &mdash; the open lead is a token-volume lead, concentrated in coding and agentic workloads.</div>
      </div>
    </div>

    <div class="panel reveal">
      <div class="panel-title">OpenRouter live leaderboard &mdash; trailing month, tokens routed</div>
      <div class="panel-sub">The five highest-volume models are all open weights. Anthropic's closed Claude models are the next US-built entrants.</div>
      <div class="legend"><span><i style="background:var(--green)"></i>Open weights</span><span><i style="background:var(--grey-1)"></i>Closed</span></div>
      <div id="lbChart"></div>
      <div class="caption">By mid-2026 the top nine models route roughly 18T weekly tokens for Chinese-built models against ~5.5T for US-built ones &mdash; more than 3:1 (FT analysis). Where developers route by cost, they route to open weights.</div>
    </div>

    <h2 class="sec reveal" style="margin-top:110px">Open ships easy.<br>Open deploys hard.</h2>
    <p class="lede reveal">Data from the Mozilla / SlashData 2026 developer survey. Open models lead in adoption: 79% of developers adding AI functionality use them, against 71% for closed, and the two are largely complementary, with half of developers using both. But production is where teams stall: only 51% of open-model teams reach production versus 63% for closed. The gap is operational tooling and trust, not model capability.</p>

    <div class="grid2">
      <div class="panel reveal">
        <div class="panel-title">Open models lead in adoption, and mostly coexist with closed</div>
        <div class="panel-sub">Share of developers adding AI functionality to their applications who currently use each model type, and how the two overlap.</div>
        <div class="adopt-pair"><div class="lbl">Open models</div><div class="fund-bar-wrap"><div class="fund-bar adb" data-w="79" style="background:var(--green)"></div></div><div class="fund-val">79%</div></div>
        <div class="adopt-pair"><div class="lbl">Closed models</div><div class="fund-bar-wrap"><div class="fund-bar adb" data-w="71" style="background:var(--grey-1)"></div></div><div class="fund-val">71%</div></div>
        <div style="font-family:var(--mono);font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;margin:22px 0 0">How they combine</div>
        <div class="venn-split" id="vennSplit">
          <div data-tip="<b>29% open only</b><br>Use open-source models exclusively" style="width:29%;background:var(--green)">29%<small>OS only</small></div>
          <div data-tip="<b>50% use both</b><br>The two are largely complementary" style="width:50%;background:var(--seed-1)">50%<small>Both</small></div>
          <div data-tip="<b>21% closed only</b><br>Use closed-source models exclusively" style="width:21%;background:var(--grey-1)">21%<small>CS only</small></div>
        </div>
        <div class="caption">Source: Mozilla / SlashData 2026 developer survey. Open and closed aren't substitutes for most teams: 50% run both, 29% open only, 21% closed only.</div>
      </div>
      <div class="panel reveal">
        <div class="panel-title">Where open adoption peaks, and where closed still edges it</div>
        <div class="panel-sub">Open-model adoption by region. Greater China and East Asia lead at 89%; South America and Western Europe are the only two regions where closed adoption exceeds open.</div>
        <div id="regionChart"></div>
        <div class="caption">Same survey, by developer region. In South America and Western Europe, and only there, closed-model adoption runs ahead of open.</div>
      </div>
    </div>

    <div class="grid2">
      <div class="panel reveal">
        <div class="panel-title">Production rate by company size</div>
        <div class="panel-sub">If the gap were about resources, scale would close it, and it doesn't. Closed climbs 54% &rarr; 73% with scale. Open barely moves: 53% &rarr; 57%.</div>
        <div class="legend"><span><i style="background:var(--grey-1)"></i>Closed models</span><span><i style="background:var(--green)"></i>Open models</span></div>
        <div id="prodChart"></div>
        <div class="caption">Enterprises can buy their way through closed deployment. Open deployment waits on tooling nobody has finished. Source: Mozilla / SlashData 2026 developer survey.</div>
      </div>
      <div class="panel reveal">
        <div class="panel-title">Why teams churn: challenges with open models</div>
        <div class="panel-sub">&Delta; = churned &minus; still using, in percentage points. The biggest gaps (performance, integration, maintenance) are operational, not capability. Hover the bars.</div>
        <div class="legend"><span><i style="background:var(--green)"></i>Still using open</span><span><i style="background:var(--orange)"></i>Churned away</span></div>
        <div id="churnChart"></div>
        <div class="caption">Mozilla survey, n=1,410. &ldquo;What are the main challenges you face when working with open or open-source AI models?&rdquo;</div>
      </div>
    </div>

    <div class="panel reveal">
      <div class="panel-title">The same challenges, everywhere: what blocks open by region</div>
      <div class="panel-sub">Share of current and churned open-model developers naming each challenge, by region. Warmer cells mean more developers blocked. The top rows are operational in every region: infrastructure cost, security and compliance, maintenance, deployment complexity. South Asia leans hardest on security and support; only North America and Greater China have more than 15% reporting no major challenges.</div>
      <div class="heat-scroll"><table class="fintab moz t3">
        <tr><th>Challenge</th><th>W. Europe & Israel</th><th>N. America</th><th>Greater China</th><th>South Asia</th><th>East Asia ex GC</th><th>S. America</th><th>E. Europe & CIS</th><th>Oceania</th><th>All</th></tr>
        <tr><td class="co">High infrastructure or compute costs</td><td class="num" style="background:#FFD9BC">25%</td><td class="num" style="background:#FFD9BC">26%</td><td class="num" style="background:#FFD9BC">29%</td><td class="num" style="background:#FFD9BC">28%</td><td class="num" style="background:#FFD9BC">28%</td><td class="num" style="background:#FFD9BC">28%</td><td class="num" style="background:#FFD9BC">29%</td><td class="num" style="background:#FFF6EF">18%</td><td class="num" style="background:#FFD9BC">27%</td></tr><tr><td class="co">Security, privacy, or compliance concerns</td><td class="num" style="background:#FFEBDD">20%</td><td class="num" style="background:#FFD9BC">27%</td><td class="num" style="background:#FFF6EF">18%</td><td class="num" style="background:var(--orange)">39%</td><td class="num" style="background:#FFD9BC">29%</td><td class="num" style="background:#FFD9BC">28%</td><td class="num" style="background:#FFD9BC">25%</td><td class="num" style="background:#FFEBDD">22%</td><td class="num" style="background:#FFD9BC">26%</td></tr><tr><td class="co">Ongoing maintenance and updates</td><td class="num" style="background:#FFD9BC">27%</td><td class="num" style="background:#FFD9BC">26%</td><td class="num" style="background:#FFF6EF">18%</td><td class="num" style="background:#FFD9BC">26%</td><td class="num" style="background:#FFF6EF">20%</td><td class="num" style="background:var(--orange)">31%</td><td class="num" style="background:#FFEBDD">21%</td><td class="num" style="background:#FFD9BC">25%</td><td class="num" style="background:#FFEBDD">24%</td></tr><tr><td class="co">Complexity of deployment, hosting, or scaling</td><td class="num" style="background:#FFD9BC">27%</td><td class="num" style="background:#FFEBDD">24%</td><td class="num" style="background:#FFF6EF">19%</td><td class="num" style="background:#FFEBDD">24%</td><td class="num" style="background:#fff">11%</td><td class="num" style="background:var(--orange)">30%</td><td class="num" style="background:#FFD9BC">26%</td><td class="num" style="background:#FFD9BC">25%</td><td class="num" style="background:#FFEBDD">23%</td></tr><tr><td class="co">Lack of specialised support</td><td class="num" style="background:#FFF6EF">17%</td><td class="num" style="background:#FFF6EF">16%</td><td class="num" style="background:#FFEBDD">21%</td><td class="num" style="background:var(--orange)">31%</td><td class="num" style="background:#FFEBDD">24%</td><td class="num" style="background:#FFEBDD">23%</td><td class="num" style="background:#FFEBDD">23%</td><td class="num" style="background:var(--orange)">32%</td><td class="num" style="background:#FFEBDD">22%</td></tr><tr><td class="co">Difficulty evaluating or comparing models</td><td class="num" style="background:#fff">14%</td><td class="num" style="background:#FFF6EF">17%</td><td class="num" style="background:#fff">14%</td><td class="num" style="background:#FFEBDD">23%</td><td class="num" style="background:#FFF6EF">16%</td><td class="num" style="background:#FFD9BC">26%</td><td class="num" style="background:#FFD9BC">25%</td><td class="num" style="background:#FFF6EF">18%</td><td class="num" style="background:#FFF6EF">18%</td></tr><tr><td class="co">Difficulty fine-tuning or customising</td><td class="num" style="background:#FFEBDD">22%</td><td class="num" style="background:#FFF6EF">18%</td><td class="num" style="background:#FFF6EF">18%</td><td class="num" style="background:#FFF6EF">20%</td><td class="num" style="background:#fff">11%</td><td class="num" style="background:#FFEBDD">22%</td><td class="num" style="background:#FFF6EF">18%</td><td class="num" style="background:#fff">12%</td><td class="num" style="background:#FFF6EF">18%</td></tr><tr><td class="co">Difficulty integrating into existing systems</td><td class="num" style="background:#FFF6EF">19%</td><td class="num" style="background:#FFEBDD">21%</td><td class="num" style="background:#fff">14%</td><td class="num" style="background:#FFEBDD">20%</td><td class="num" style="background:#fff">7%</td><td class="num" style="background:#FFD9BC">26%</td><td class="num" style="background:#FFF6EF">19%</td><td class="num" style="background:#FFEBDD">20%</td><td class="num" style="background:#FFF6EF">18%</td></tr><tr><td class="co">Insufficient documentation or learning resources</td><td class="num" style="background:#FFF6EF">18%</td><td class="num" style="background:#fff">15%</td><td class="num" style="background:#FFF6EF">15%</td><td class="num" style="background:#FFF6EF">17%</td><td class="num" style="background:#FFF6EF">15%</td><td class="num" style="background:#FFF6EF">20%</td><td class="num" style="background:#FFEBDD">24%</td><td class="num" style="background:#FFF6EF">15%</td><td class="num" style="background:#FFF6EF">17%</td></tr><tr><td class="co">Model performance is not good enough</td><td class="num" style="background:#FFF6EF">18%</td><td class="num" style="background:#FFF6EF">15%</td><td class="num" style="background:#fff">13%</td><td class="num" style="background:#FFEBDD">22%</td><td class="num" style="background:#FFF6EF">16%</td><td class="num" style="background:#FFF6EF">17%</td><td class="num" style="background:#FFF6EF">19%</td><td class="num" style="background:#fff">8%</td><td class="num" style="background:#FFF6EF">17%</td></tr><tr><td class="co">No major challenges</td><td class="num" style="background:#fff">9%</td><td class="num" style="background:#FFEBDD">21%</td><td class="num" style="background:#FFF6EF">16%</td><td class="num" style="background:#fff">5%</td><td class="num" style="background:#fff">14%</td><td class="num" style="background:#fff">4%</td><td class="num" style="background:#fff">8%</td><td class="num" style="background:#fff">12%</td><td class="num" style="background:#fff">12%</td></tr>
        <tr class="nrow"><td class="co">Weighted sample size</td><td class="num">286</td><td class="num">277</td><td class="num">206</td><td class="num">192</td><td class="num">164</td><td class="num">147</td><td class="num t1mid">98</td><td class="num t1low">39</td><td class="num">1411</td></tr>
      </table></div>
      <div class="caption">Source: Mozilla / SlashData 2026 developer survey (MZCS1). n=1,410 current or churned open-model developers; the Oceania column (n=39) and Eastern Europe &amp; CIS (n=98) fall below reliable thresholds.</div>
    </div>
  </div>
</section>

<hr class="hr">

<!-- ============ SECTION 02: THE STACK ============ -->
<section id="stack">
  <div class="wrap">
    <div class="section-tag reveal"><span class="section-num">02</span><span class="section-label">The open-source AI stack</span></div>
    <h2 class="sec reveal">The open stack scores high on capability,<br>low on operations.</h2>
    <p class="lede reveal">Nine layers and 48 components of the stack scored across 10 criteria (1&ndash;5). Click a layer to open its components: each carries its own criterion scores, maturity grade, open-vs-closed parity verdict, and surfaces some of its most-starred open-source projects.</p>
    <p class="lede reveal" style="margin-top:10px">Hover any cell for detail.</p>
    <div class="legend reveal" style="margin-top:26px"><span><i style="background:var(--green)"></i>Strong</span><span><i style="background:var(--seed)"></i>Viable, but fragmented</span><span><i style="background:var(--orange)"></i>Early stage</span></div>

    <div class="heat-scroll reveal"><div class="stack" id="stackAcc" style="margin-top:0;min-width:1020px"></div></div>
    <div class="heat-legend reveal">
      <span><i style="background:var(--green)"></i>Strong (&ge;4.0)</span>
      <span><i style="background:#9FE894"></i>3.5&ndash;3.9</span>
      <span><i style="background:var(--green-1)"></i>3.0&ndash;3.4</span>
      <span><i style="background:#FFD9BC"></i>2.5&ndash;2.9</span>
      <span><i style="background:var(--orange)"></i>Weak (&lt;2.5)</span>
      <span class="opgap">the operational gap = standardization + enterprise readiness</span>
    </div>
    <div class="caption reveal">Cells are scores per maturity criterion (1&ndash;5), ordered strongest to weakest left to right; layer rows are the means of their components. The two coldest columns, standardization and enterprise readiness, repeat down every layer and every component: that repeating cold edge is the operational gap. Source: Mozilla stack map, June 2026 (48 components, 1,361 projects).</div>
  </div>
</section>

<hr class="hr">

<!-- ============ SECTION 03: WHO'S BETTING ============ -->
<section id="betting">
  <div class="wrap">
    <div class="section-tag reveal"><span class="section-num">03</span><span class="section-label">Who's betting on it</span></div>
    <h2 class="sec reveal">Open source is a business model.</h2>
    <p class="lede reveal">Open-weight AI is a commercial market at multi-hundred-billion-dollar scale, built by funded companies and run in production by global enterprises. Databricks crossed a $5.4B run-rate; Mistral scaled 20&times; to ~$400M ARR in twelve months; DeepSeek reached ~$220M ARR and recently raised $7.4B at a valuation over $50B. Five revenue models are proven at scale: hosted inference, enterprise platforms, on-prem licensing, fine-tuning services, and harness tooling.</p>

    <div class="panel reveal">
      <div class="panel-title">The venture-funded open-source ecosystem: total disclosed funding, USD M</div>
      <div class="panel-sub">Bars grow as you scroll. Color by region of the company.</div>
      <div class="legend"><span><i style="background:var(--green)"></i>North America</span><span><i style="background:var(--orange)"></i>China</span><span><i style="background:var(--aqua)"></i>Europe &amp; rest of world</span></div>
      <div id="fundChart"></div>
      <div class="caption">Selected companies; Zhipu AI and MiniMax went public (HK IPO 2026) with undisclosed totals. Corporate strategics (Nvidia, Salesforce, AMD, Google, IBM, ASML, Tencent, CATL, Schwarz Group) back the same ecosystem across model, inference, and tooling layers.</div>
    </div>
    <div class="panel reveal">
      <div class="panel-title">Financial maturity of the open ecosystem</div>
      <div class="panel-sub">Funding, valuation and revenue traction for the companies carrying the open stack. The ecosystem has moved from grants to venture scale to public markets.</div>
      <div class="heat-scroll"><table class="fintab" id="finTable">
        <tr><th>Company</th><th>HQ</th><th>Layer</th><th>Disclosed funding</th><th>Valuation</th><th>Revenue signal</th><th>Leading investors</th><th>Stage</th></tr>
        <tr><td class="co">Databricks</td><td>USA</td><td>Enterprise platform</td><td>&mdash;</td><td>&mdash;</td><td class="rev">$5.4B run-rate</td><td class="inv">&mdash;</td><td>Pre-IPO</td></tr>
        <tr><td class="co">DeepSeek</td><td>China</td><td>Frontier open weights</td><td>$7.4B</td><td>$50B+</td><td class="rev">~$220M ARR</td><td class="inv">Liang Wenfeng; Tencent; CATL; China National AI Fund</td><td>Private</td></tr>
        <tr><td class="co">Mistral AI</td><td>France</td><td>Open weights + platform</td><td>$3.05B</td><td>~$14B (talks at &euro;20B)</td><td class="rev">~$400M ARR, 20&times; YoY</td><td class="inv">ASML; a16z; Lightspeed; Nvidia</td><td>Private</td></tr>
        <tr><td class="co">Moonshot AI</td><td>China</td><td>Open weights (Kimi)</td><td>$3.9B</td><td>&mdash;</td><td>&mdash;</td><td class="inv">Meituan/Long-Z; Alibaba; Tencent; HongShan</td><td>Private</td></tr>
        <tr><td class="co">Zhipu AI</td><td>China</td><td>Open weights (GLM)</td><td>Undisclosed</td><td>Public</td><td>&mdash;</td><td class="inv">Public (HK IPO 2026); prior Alibaba, Tencent</td><td class="pub">HK IPO 2026</td></tr>
        <tr><td class="co">MiniMax</td><td>China</td><td>Open weights</td><td>Undisclosed</td><td>Public</td><td>&mdash;</td><td class="inv">Public (HK IPO 2026)</td><td class="pub">HK IPO 2026</td></tr>
        <tr><td class="co">Cohere</td><td>Canada</td><td>Enterprise / on-prem</td><td>$1.7B</td><td>&mdash;</td><td>Command A+ open-sourced May 2026</td><td class="inv">Radical Ventures; Nvidia; AMD; Schwarz Group</td><td>Private</td></tr>
        <tr><td class="co">Cerebras</td><td>USA</td><td>Compute</td><td>$2.1B</td><td>&mdash;</td><td>&mdash;</td><td class="inv">Fidelity; Atreides; G42; Tiger Global</td><td>Private</td></tr>
        <tr><td class="co">Reflection AI</td><td>USA</td><td>Open weights</td><td>$2.13B</td><td>&mdash;</td><td>&mdash;</td><td class="inv">Nvidia; Disruptive; Sequoia; Lightspeed; DST Global</td><td>Private</td></tr>
        <tr><td class="co">Together AI</td><td>USA</td><td>Inference cloud</td><td>$1.334B</td><td>&mdash;</td><td>&mdash;</td><td class="inv">Aramco Ventures; General Catalyst; Prosperity7; Nvidia</td><td>Private</td></tr>
        <tr><td class="co">Hugging Face</td><td>USA</td><td>Hub</td><td>$400M</td><td>&mdash;</td><td>&mdash;</td><td class="inv">Salesforce; Google; Nvidia; IBM</td><td>Private</td></tr>
        <tr><td class="co">LangChain</td><td>USA</td><td>Harness tooling</td><td>$260M</td><td>&mdash;</td><td>126k+ stars, 60% dev share</td><td class="inv">IVP; Sequoia; Benchmark; CapitalG</td><td>Private</td></tr>
      </table></div>
      <div class="caption">Five revenue models are proven at scale: hosted inference, enterprise platforms, on-prem licensing, fine-tuning services, and harness tooling. &ldquo;&mdash;&rdquo; = not publicly disclosed.</div>
    </div>

    <div class="grid2">
      <div class="panel reveal">
        <div class="panel-title">The metered model breaks at scale</div>
        <div class="panel-sub">Closed frontier models are sold by the token &mdash; and at production scale the meter becomes the problem.</div>
        <div id="meterCards"></div>
      </div>
      <div class="panel reveal">
        <div class="panel-title">A fifth of the usage, 4% of the revenue</div>
        <div class="panel-sub">On OpenRouter (May&ndash;Sep 2025), closed models held ~80% of usage and ~96% of revenue. Price drives it: at ~90% parity, closed costs ~6&times; more per call.</div>
        <div id="decoupleChart"></div>
        <div class="big-callout" data-tip="<b>Nagle&ndash;Yue study, Linux Foundation</b><br>At ~90% parity, closed models cost ~6&times; more per call. The asymmetry compounds to ~$24.8B a year."><div class="bc-num">~$24.8B</div><div class="bc-lab">in unrealized annual savings &mdash; the Nagle&ndash;Yue study for the Linux Foundation's estimate of the open-vs-closed price asymmetry, at ~6&times; the cost per call for comparable capability</div></div>
        <div class="caption">Where developers route by cost, they route to open weights.</div>
      </div>
    </div>
  </div>
</section>

<hr class="hr">
<!-- ============ SECTION 04: SOVEREIGNTY MAP ============ -->
<section id="sovereignty">
  <div class="wrap">
    <div class="section-tag reveal"><span class="section-num">04</span><span class="section-label">Why it's happening everywhere</span></div>
    <h2 class="sec reveal">Open isn't a vendor choice.<br>It's a sovereignty choice.</h2>
    <p class="lede reveal">More than 70 national AI strategies are live. The strategic question has shifted from whether to have a national AI policy to which layer of the stack a country can own.</p>
    <p class="lede reveal" style="margin-top:10px">Click a marker or a country below.</p>

    <div class="grid2">
      <div class="panel reveal">
        <div class="panel-title">The case for open is optionality</div>
        <div class="panel-sub">Optionality stopped being abstract in June 2026, and it stopped being a procurement question. Three days after Claude Fable 5 went on sale, a single government's export order forced Anthropic to cut access for every foreign national on earth. No other capital was consulted. None could have been. Selective compliance was impossible, so the models went dark for everyone at 5:21 p.m. on a Friday. Anyone who had built on that model inherited a shutdown they had no warning of and no part in. A provider can switch off a model. Nobody can switch off a copy already running on a machine you hold, and that holds whether the machine is a startup's server or a national supercomputer. For a company, weights on disk are a hedge. For a state, they are the difference between a policy and a permission.</div>
        <div class="panel-sub" style="margin-bottom:8px">The strategic case for open is the ability to leave, and the cloud era proved the cost of its absence:</div>
        <div class="opt-stats">
          <div class="opt-stat" data-tip="<b>The exit penalty is real</b><br>Moving a single petabyte out of AWS S3 runs roughly $90,000&ndash;$120,000 in egress fees"><b>$90&ndash;120k</b><span>to move one petabyte out of AWS S3</span></div>
          <div class="opt-stat" data-tip="<b>IDC</b><br>About 80% of enterprises are now repatriating some workloads; 61% report cost reductions above 25%"><b>80%</b><span>of enterprises now repatriating workloads</span></div>
          <div class="opt-stat" data-tip="<b>37signals</b><br>Cut a $3.2M annual cloud bill to under $1M; AWS waived a $250,000 egress fee to let it leave"><b>$3.2M &rarr; &lt;$1M</b><span>37signals' cloud bill after leaving</span></div>
          <div class="opt-stat" data-tip="<b>GEICO</b><br>Repatriated after cloud costs ran 2.5&times; expectations"><b>2.5&times;</b><span>what GEICO's cloud costs ran over plan</span></div>
        </div>
        <div class="caption" style="margin-top:14px">Closed model APIs reproduce the same trap: build on a proprietary endpoint and you inherit the vendor's pricing changes with no clean exit. Open weights are exit rights.</div>
      </div>
      <div class="panel reveal">
        <div class="panel-title">The largest source of open weights is China. By design.</div>
        <div class="panel-sub">Cumulative Hugging Face downloads, March 2026:</div>
        <div id="dlChart"></div>
        <div class="panel-sub" style="margin:14px 0 0">In February 2026 Qwen out-downloaded the next eight organizations combined. On OpenRouter, Chinese open-weight models rose from under 2% of tokens in late 2024 to more than 45% of weekly traffic by April 2026, and about 61% among the ten most-used models. DeepSeek reports 26,000+ enterprise accounts; 58% of new AI startups in 2025 included it in their stack, even as at least eight jurisdictions restricted the hosted service. The resolution is architectural: enterprises ban the hosted app and adopt the weights anyway, self-hosted or via Western endpoints.
        <br><br>This is intentional policy. The State Council's "AI Plus" Initiative (Aug 2025) and the national Five-Year Plan (Mar 2026) codify open-source proliferation as a core directive, and releasing public weights doubles as a macro hedge against semiconductor export controls, offloading global inference onto end users' local hardware. Across the Global South the draw is diversification away from US technology monopolies; elsewhere it is purely financial. Even Microsoft is exploring a secured, Azure-hosted DeepSeek V4 for its heaviest Copilot workload.</div>
      </div>
    </div>

    <div class="map-legend reveal" id="mapLegend"></div>
    <div class="map-grid reveal">
      <div class="map-canvas" id="mapCanvas">
        <div class="map-foot">Marker size &asymp; scale of committed public/strategic capital &middot; Equirectangular projection</div>
      </div>
      <aside class="detail" id="detailPanel"></aside>
    </div>
    <div class="country-chips reveal" id="countryChips"></div>
    <div class="caption reveal">Source: Open Source AI jurisdictions dataset, July 2026. Marker size scales with committed public and strategic capital.</div>
  </div>
</section>

<hr class="hr">

<!-- ============ SECTION 05: HARNESS ============ -->
<section id="harness">
  <div class="wrap">
    <div class="section-tag reveal"><span class="section-num">05</span><span class="section-label">The harness is the new frontier</span></div>
    <h2 class="sec reveal">The agentic harness is another user agent.</h2>
    <p class="lede reveal">The browser was the user agent of the open web: code on the user's side, negotiating with servers on their behalf. That role is being recreated one layer up. Above the model now sits the agentic harness &mdash; the orchestration loop, tools, memory, sandboxes, and permission model. It is where production difficulty concentrates, and where the open-vs-closed, owner-vs-renter contest restarts.</p>

    <div class="harness reveal">
      <div class="hbar"><b>The user &middot; other agents &middot; the world</b><small>humans &middot; systems &middot; data &middot; money</small></div>
      <div class="hband govern">
        <div class="hband-lab"><b>Govern</b><small>one plane over many harnesses</small></div>
        <div class="hcells">
          <div class="hcell"><b>Stateful policy</b><small>what the session already did</small></div>
          <div class="hcell"><b>Registry &amp; lineage</b><small>which agent did what</small></div>
          <div class="hcell"><b>Budget &amp; revocation</b><small>cost caps &middot; kill switch</small></div>
        </div>
      </div>
      <div class="hstrip">Meta-harness &middot; Omnigent &middot; OPA &middot; Agent governance toolkit</div>
      <div class="hband">
        <div class="hband-lab"><b>Surface</b><small>meets user &amp; money</small></div>
        <div class="hcells">
          <div class="hcell"><b>Interface</b><small>AG-UI &middot; A2UI</small></div>
          <div class="hcell"><b>Payment &amp; metering</b><small>x402 &middot; AP2 &middot; UCP</small></div>
        </div>
      </div>
      <div class="hband">
        <div class="hband-lab"><b>Action</b><small>do things, safely</small></div>
        <div class="hcells">
          <div class="hcell"><b>Sandboxes &amp; execution</b><small>E2B &middot; Daytona &middot; Modal</small></div>
          <div class="hcell gap"><b>Permission &amp; identity</b><small>the write surface &mdash; the unsolved gap</small></div>
          <div class="hcell"><b>Eval &amp; observability</b><small>Langfuse &middot; Phoenix</small></div>
        </div>
      </div>
      <div class="hband">
        <div class="hband-lab"><b>Reach</b><small>connect &amp; remember</small></div>
        <div class="hcells">
          <div class="hcell"><b>Tools &amp; context</b><small>MCP</small></div>
          <div class="hcell"><b>Agent-to-agent</b><small>A2A</small></div>
          <div class="hcell"><b>Memory</b><small>Mem0 &middot; Letta &middot; Zep</small></div>
        </div>
      </div>
      <div class="hband">
        <div class="hband-lab"><b>Control</b><small>drive the loop</small></div>
        <div class="hcells">
          <div class="hcell"><b>Orchestration loop</b><small>LangGraph &middot; CrewAI &middot; AutoGen &middot; LlamaIndex &mdash; the reason-and-act cycle that turns a model into an agent</small></div>
        </div>
      </div>
      <div class="hbar" style="border-top:2px solid var(--black)"><b>The model &mdash; the weights</b><small>open or closed &middot; swappable &middot; commoditizing toward zero</small></div>
    </div>
    <div class="caption reveal">The layer is already a product category: LangChain alone has 126,000+ GitHub stars and a 60% developer share; MCP reached 97M monthly SDK downloads and 10,000+ active servers in its first year, growing 4,750% in 16 months &mdash; and was donated to the Linux Foundation's Agentic AI Foundation in December 2025. Adoption outpaces governance: only ~21% of companies report mature agent governance.</div>

    <div class="panel reveal" style="margin-top:64px">
      <div class="panel-title">The model is eating the harness, and that's the opening for open</div>
      <div class="panel-sub"><a href="https://www.tbench.ai/leaderboard/terminal-bench/2.0" target="_blank" rel="noopener">Terminal-Bench 2.0</a> (May 2026) made the harness look like a free lunch anyone could capture: a third-party scaffold ran Anthropic's own weights to 79.8% while Claude Code managed 58.0% on the same model, a 21.8-point spread that put the harness ahead of the weights. Eight weeks later, <a href="https://www.tbench.ai/leaderboard/terminal-bench/2.1" target="_blank" rel="noopener">Terminal-Bench 2.1</a> reversed it. The frontier labs read that result and pulled the harness in-house: on every model where both appear, the lab's own harness now wins, and the 21.8-point gap has compressed to roughly 3 at the top: the model eating its way up the stack, weights and scaffold shipped as one product.</div>
      <div class="grid2" style="margin-top:8px">
        <div><div class="panel-title" style="color:var(--grey--1)">May 2026 &middot; Terminal-Bench 2.0</div><div id="tb20"></div></div>
        <div><div class="panel-title" style="color:var(--grey--1)">July 2026 &middot; Terminal-Bench 2.1 &middot; official board, verified top tier</div><div id="tb21"></div></div>
      </div>
      <div class="caption">That integration is a moat in formation, and the labs have every incentive to deepen it. A harness tuned tightly to one lab's weights becomes a fit rather than a neutral layer. It degrades on anyone else's model, so the tighter the tuning, the less swappable the weights underneath. Lock-in arrives as a side effect of optimization. The open models have no first-party harness to answer with, which is why none appear in the verified top tier of the official board at all.</div>

      <div class="panel-title" style="margin-top:36px">But absence isn't inability: put every model on one neutral scaffold and the gap collapses</div>
      <div class="panel-sub"><a href="https://www.vals.ai/benchmarks/terminal-bench-2-1" target="_blank" rel="noopener">vals.ai's Terminus-2 run of Terminal-Bench 2.1</a>: the same benchmark, one neutral harness for everyone. Capability bars in points; cost per task in the label.</div>
      <div id="tbNeutral"></div>
      <div class="caption">On a fair harness the capability gap is a few points; the price gap is 5&times;. The strongest open model, <a href="https://venturebeat.com/technology/z-ais-open-weights-glm-5-2-beats-gpt-5-5-on-multiple-long-horizon-coding-benchmarks-for-1-6th-the-cost" target="_blank" rel="noopener">GLM 5.2</a>, lands a fraction behind Claude Opus 4.7 and about four points behind Opus 4.8 at roughly a fifth the cost. Integration buys the labs a second edge open deployments lack: a data flywheel where real usage through the lab's harness feeds straight back into the next model. That edge is real, and it cuts both ways: the usage exhaust trains whoever owns the harness, and the only question is whether that's the closed endpoint or your own stack. The labs have proven the harness is worth owning. The same move is open, a harness co-designed with open weights, and the window to keep it a layer is now, before the closed stacks finish welding model and scaffold into one rented product.</div>
    </div>

    <div class="panel reveal">
      <div class="panel-title">The write surface: the unsolved hole at the center of the harness</div>
      <div class="rw-grid">
        <div class="rw reads"><div class="rw-h">Reads</div><p>Reversible and low-consequence. Fetching a document, querying a database, listing a calendar. These can largely be permitted by default; a bad read costs little and can be repeated safely.</p></div>
        <div class="rw writes"><div class="rw-h">Writes</div><p>Side effects that are costly or irreversible. Sending a message, spending against a budget, modifying a record, executing a transaction. This is where confirmation, approval thresholds, cost caps and revocation must concentrate.</p></div>
      </div>
      <div class="panel-sub" style="margin-top:18px;margin-bottom:0">The unsolved permission problem is a write problem. The harness ecosystem now spans roughly a dozen frameworks, ten harnesses and three peer protocols, yet no portable model defines which writes an agent may perform unattended, which require human approval, and which are forbidden, across an MCP host, an A2A peer, a direct tool invocation and a framework boundary. The protocols hardened the front door and stopped there: MCP's 2025-11-25 specification moved authorization onto OAuth 2.1, and A2A v1.0 standardized signed Agent Cards, but both stop at authentication. Knowing who an agent is says nothing about what it may do.
      <br><br>The human backstop is failing too. CoSAI's MCP threat model lists consent fatigue, the pattern in which users approve the large majority of prompts, as a top-tier threat. Consent fatigue is itself a write-side failure, because the prompts that matter are the ones authorizing action.
      <br><br>Industry responses are bypassing the framework deadlock by pulling control up to the meta-harness layer. Instead of fragile prompt-based filters inside individual agents, emerging cross-harness architectures (like <a href="https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents" target="_blank" rel="noopener">Databricks' open-sourced Omnigent</a>) enforce stateful, contextual policies that track what a session has done and gate the next write accordingly: requiring human approval for a code push once an agent has pulled an unverified package, or enforcing cost caps that pause a session after a set spend. These controls govern the write surface from a layer above any single harness, which is where the durable permission model is most likely to form. It is the single highest-leverage gap in the layer.</div>
    </div>

    <div class="grid2">
      <div class="panel reveal">
        <div class="panel-title">Closed is not the same as secure</div>
        <div class="panel-sub" style="margin-bottom:0">A closed API feels safe because of filtering, monitoring, and revocation. All three are functions of the serving layer. Keeping the weights secret does not provide any of them. The same controls live at the harness layer and apply to self-hosted open models. In 2025, authorization failures rated CVSS 9.3&ndash;9.4 hit Anthropic, Microsoft, ServiceNow and Salesforce, all closed systems. The NTIA studied whether the US government should restrict open weights and recommended that it monitor them instead. Security concerns are best addressed by investing in the harness. They do not require renting a closed model.</div>
      </div>
      <div class="panel reveal">
        <div class="panel-title">Where closed still leads</div>
        <div class="panel-sub" style="margin-bottom:0">Closed systems still lead in four places. The first is the integrated harness. No open model appears in the verified top tier of the official Terminal-Bench 2.1 board, and even on a neutral scaffold the best open model trails Opus 4.8 by about four points. Behind that harness sits a data flywheel, since usage routed through a lab's own scaffold feeds back into its next model. The second is long-context fidelity at 1M tokens, where Gemini 3 holds 89% multi-needle retrieval against DeepSeek V4-Pro's 41%. The third is turnkey compliance, with SOC 2, HIPAA, and zero data retention available by default. The fourth is accountability, meaning a counterparty the customer can hold liable.<br><br>Compliance and accountability are contracting problems. The integrated harness is a tooling problem. Long-context fidelity is a model problem, and closing it is work only the open labs can do.</div>
      </div>
    </div>
  </div>
</section>

<hr class="hr">

<!-- ============ SECTION 06: FIVE BETS ============ -->
<section id="bets">
  <div class="wrap">
    <div class="section-tag reveal"><span class="section-num">06</span><span class="section-label">Opportunities</span></div>
    <h2 class="sec reveal">Five bets. None requires beating the frontier.</h2>
    <p class="lede reveal">They require owning the layers above it &mdash; the harness, the memory, the permission model &mdash; while those layers are still open.</p>
    <div class="bets" id="betCards"></div>
  </div>
</section>

<hr class="hr">

<!-- ============ WATCHLIST ============ -->
<section id="watchlist">
  <div class="wrap">
    <div class="section-tag reveal"><span class="section-num">07</span><span class="section-label">The watchlist</span></div>
    <h2 class="sec reveal">Signals that keep the layer open.</h2>
    <div class="watch reveal">
      <div class="wlane"><h4><i></i>Capability &amp; adoption</h4><p>The 3.3% gap (at parity on coding, behind on reasoning and agentic), and open's OpenRouter token share, especially in agentic coding.</p><p class="rev"><b>Reverses if:</b> token share stalls while the reasoning gap widens.</p></div>
      <div class="wlane"><h4><i></i>The harness</h4><p>The Terminal-Bench spread between lab-owned and independent scaffolds; MCP/A2A governance under the AAIF; the portable permission spec that still doesn't exist.</p><p class="rev"><b>Reverses if:</b> the lab-harness lead widens, or a closed platform sets the permission standard first.</p></div>
      <div class="wlane"><h4><i></i>Market structure</h4><p>Open-lab economics (ARR, raises, the Zhipu/MiniMax IPOs) against metered-pricing breakpoints (~2027&ndash;28), with sovereign capacity as counterweight.</p><p class="rev"><b>Reverses if:</b> sovereign funding lapses or open-lab economics fail to scale.</p></div>
      <div class="wlane"><h4><i></i>Trust &amp; safety</h4><p>Tracked, not settled: misuse capability and how easily safety tuning strips from open weights; hard-friction zones, above all synthetic CSAM and NCII; whether NTIA's &ldquo;monitor, don't restrict&rdquo; holds.</p><p class="rev"><b>Reverses if:</b> a major misuse event, or a shift from monitoring to restriction.</p></div>
    </div>
  </div>
</section>



<!-- ============ CLOSING ============ -->
<div class="closing">
  <div class="wrap">
    <p class="reveal">There is a test you can run for the rest of this. Look at who is seated in the rooms where AI gets decided, and with what status. The day they seat the people who keep AI open, portable, and widely deployed on equal footing, the shift from renting to owning will have happened. The window is open now. It is closing slowly enough that we can pretend it isn't, and the lease is shorter than it looks. <span class="build">Build with us.</span></p>
  </div>
</div>


<section id="feedback">
  <div class="wrap">
    <h2 class="sec reveal" style="font-size:clamp(28px,3.6vw,46px)">This is V1. We'd like to hear from you.</h2>
    <div class="cta-row reveal">
      <a class="cta-icon" href="mailto:opensource@mozilla.org" title="Email us: opensource@mozilla.org" aria-label="Email">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="0"/><path d="M2 6l10 7L22 6"/></svg>
      </a>
      <a class="cta-icon" href="https://x.com/mozilla" target="_blank" rel="noopener" title="Mozilla on X" aria-label="X">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.9 2H22l-6.8 7.8L23.2 22h-6.3l-4.9-6.4L6.4 22H3.3l7.3-8.3L1.2 2h6.4l4.4 5.9L18.9 2zm-1.1 18h1.7L7.1 3.7H5.2L17.8 20z"/></svg>
      </a>
      <a class="cta-icon" href="https://www.linkedin.com/company/mozilla-corporation/posts/?feedView=all" target="_blank" rel="noopener" title="Mozilla on LinkedIn" aria-label="LinkedIn">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5A2.49 2.49 0 1 1 0 3.5a2.49 2.49 0 0 1 4.98 0zM.4 8.4h4.6V24H.4V8.4zm7.6 0h4.4v2.1h.1c.6-1.2 2.1-2.4 4.3-2.4 4.6 0 5.5 3 5.5 7v8.9h-4.6v-7.9c0-1.9 0-4.3-2.6-4.3s-3 2-3 4.2V24H8V8.4z"/></svg>
      </a>
      <a class="cta-icon" href="https://bsky.app/profile/mozilla.org" target="_blank" rel="noopener" title="Mozilla on Bluesky" aria-label="Bluesky">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 10.8c-1.1-2.1-4-6-6.7-7.9C2.7 1.1 1.7 1.4 1 1.7.3 2.1 0 3.3 0 4c0 .7.4 5.8.7 6.7.9 3 4.1 4 7 3.7-4.3.6-8.1 2.2-3.1 7.7 5.5 5.7 7.5-1.2 7.4-2.8 0 1.6 2 8.5 7.4 2.8 5-5.5 1.2-7.1-3.1-7.7 2.9.3 6.1-.7 7-3.7.3-.9.7-6 .7-6.7 0-.7-.3-1.9-1-2.3-.7-.3-1.7-.6-4.3 1.2-2.7 1.9-5.6 5.8-6.7 7.9z"/></svg>
      </a>
      <a class="letter-link" style="margin:0" href="https://www.mozillafoundation.org/en/festival/" target="_blank" rel="noopener">Sign up for MozFest <span class="arrow">&rarr;</span></a>
    </div>
  </div>
</section>

<hr class="hr">
<section id="sources">
  <div class="wrap">
    <h2 class="reveal" style="font-family:var(--mono);font-size:13px;font-weight: