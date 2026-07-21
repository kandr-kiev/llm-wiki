---
source_url: https://code.visualstudio.com/blogs/2026/07/06/optimizing-vscode-coding-harness-model-providers
ingested: 2026-07-17
sha256: 8753818eb901c0f5f22ba6bfe046b56d729adedd87cbc4a85ada645035f84553
blog_source: VS Code Blog
---
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8" />
	<meta name="awa-expId" content="tv-downloadv2:1227265;" />
	<meta name="awa-env" content="prod" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="google-site-verification" content="hNs7DXrTySP_X-0P_AC0WulAXvUwgSXEmgfcO2r79dw" />

	<!-- Twitter and Facebook OpenGraph Metadata-->
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:site" content="@code" />

	<meta name="description" content="See how VS Code and OpenAI tested GPT-5.5 system prompt changes in a two-week experiment, cutting tool calls and tail-end token usage while speeding up edits." />
<meta name="keywords" content="" />
<!-- Twitter and Facebook OpenGraph Metadata-->
<meta name="twitter:card" content="summary_large_image" />
<meta property="og:url" content="https://code.visualstudio.com/blogs/2026/07/06/optimizing-vscode-coding-harness-model-providers" />
<meta property="og:type" content="article" />
<meta property="og:title" content="How Prompt Tuning Improved GPT-5.5 in VS Code" />
<meta property="og:description" content="See how VS Code and OpenAI tested GPT-5.5 system prompt changes in a two-week experiment, cutting tool calls and tail-end token usage while speeding up edits." />

<meta property="og:image" content="https://code.visualstudio.com/assets/blogs/2026/07/06/gpt55-metrics-comparison.png" />



	<link rel="shortcut icon" href="/assets/favicon.ico" sizes="128x128" />
	<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">

	<title>How Prompt Tuning Improved GPT-5.5 in VS Code</title>

	<link rel="stylesheet" href="/dist/style.css">

	<script src="https://consentdeliveryfd.azurefd.net/mscc/lib/v2/wcp-consent.js"></script>
	<script type="text/javascript" src="https://js.monitor.azure.com/scripts/c/ms.analytics-web-4.min.js"></script>
	
	<script type="text/javascript">
	// Leave as var; siteConsent is initialized and referenced elsewhere.
	var siteConsent = null;
	
	const GPC_DataSharingOptIn = false;
	WcpConsent.onInitCallback(function () {
		window.appInsights = new oneDS.ApplicationInsights();
		window.appInsights.initialize({
			instrumentationKey: "1a3eb3104447440391ad5f2a6ee06a0a-62879566-bc58-4741-9650-302bf2af703f-7103",
			propertyConfiguration: {
				userConsented: false,
				gpcDataSharingOptIn: false,
				callback: {
					userConsentDetails: siteConsent ? siteConsent.getConsent : undefined
				},
			},
			cookieCfg: {
				ignoreCookies: ["MSCC"]
			},
			webAnalyticsConfiguration:{ // Web Analytics Plugin configuration
				urlCollectQuery: true,
				urlCollectHash: true,
				autoCapture: {
					scroll: true,
					pageView: true,
					onLoad: true,
					onUnload: true,
					click: true,
					resize: true,
					jsError: true
				}
			}
		}, []);
	
		window.appInsights.getPropertyManager().getPropertiesContext().web.gpcDataSharingOptIn = GPC_DataSharingOptIn;
	});
	</script>
	<link rel="alternate" type="application/atom+xml" title="RSS Feed for code.visualstudio.com" href="/feed.xml" />
</head>

<body >
	<!-- Setting theme here to avoid FOUC -->
	<script>
		function setTheme(themeName) {
			if (themeName === 'dark') {
				document.documentElement.removeAttribute('data-theme'); // dark is default, so no data-theme attribute needed
			}

			if (themeName === 'light') {
				document.documentElement.setAttribute('data-theme', themeName);
			}
			return;
		}

		// Determine initial theme: user preference or system preference
		let theme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
		setTheme(theme); // Apply the initial theme

		// Listen for changes in the system theme preference
		window.matchMedia('(prefers-color-scheme: dark)').addListener(e => {
			if (!localStorage.getItem('theme')) { // Only if no user preference is saved
				setTheme(e.matches ? 'dark' : 'light');
			}
		});
	</script>

	<div id="main">
		<div class="navbar-fixed-container">
			<div class="navbar navbar-inverse navbar-fixed-top ">
				<div id='cookie-banner'></div>		<nav role="navigation" aria-label="Top Level">
					<div class="container">
						<div class="nav navbar-header">
							<a class="navbar-brand" href="/"><span>Visual Studio Code</span></a>
						</div>
						<div class="navbar-collapse collapse">
							<ul class="nav navbar-nav navbar-left" data-m='{"cN":"top-navbar","aN":"navigation"}'>
								<li class="nav-dropdown">
									<a id="nav-features" href="#" class="nav-dropdown-toggle" role="button" aria-haspopup="true" aria-expanded="false" data-m='{"cN":"Features","aN":"navigation","cT":"toggle"}'>
										Features <span class="nav-dropdown-caret" aria-hidden="true"></span>
									</a>
									<ul class="nav-dropdown-menu" role="menu">
										<li role="none"><a role="menuitem" href="/features/agents" data-m='{"cN":"Agents","aN":"navigation - Features"}'>Agents</a></li>
									</ul>
								</li>
								<li class="nav-dropdown">
									<a id="nav-docs" href="#" class="nav-dropdown-toggle" role="button" aria-haspopup="true" aria-expanded="false" data-m='{"cN":"Docs","aN":"navigation","cT":"toggle"}'>
										Docs <span class="nav-dropdown-caret" aria-hidden="true"></span>
									</a>
									<ul class="nav-dropdown-menu" role="menu">
										<li role="none"><a role="menuitem" href="/docs" data-m='{"cN":"Documentation","aN":"navigation - Docs"}'>Documentation</a></li>
										<li role="none"><a role="menuitem" href="/api" data-m='{"cN":"API","aN":"navigation - Docs"}'>API</a></li>
										<li role="none"><a role="menuitem" id="nav-faqs" href="/docs/supporting/faq" data-m='{"cN":"FAQ","aN":"navigation - Docs"}'>FAQ</a></li>
									</ul>
								</li>
								<li ><a id="nav-updates" href="/updates" data-m='{"cN":"Release Notes"}'>Release Notes</a>
								</li>
								<li class="active" ><a id="nav-blogs" href="/blogs" data-m='{"cN":"Blog"}'>Blog</a></li>
								<li ><a id="nav-learn" href="/learn" data-m='{"cN":"Learn"}'>Learn</a></li>
								<li><a id="nav-events" href="https://aka.ms/vscode/live" target="_blank" rel="noopener" data-m='{"cN":"Events"}'>Events<span class="codicon codicon-link-external nav-external-icon" aria-hidden="true"></span></a></li>
								<li class="nav-dropdown">
									<a id="nav-resources" href="#" class="nav-dropdown-toggle" role="button" aria-haspopup="true" aria-expanded="false" data-m='{"cN":"Resources","aN":"navigation","cT":"toggle"}'>
										Resources <span class="nav-dropdown-caret" aria-hidden="true"></span>
									</a>
									<ul class="nav-dropdown-menu" role="menu">
										<li role="none"><a role="menuitem" href="https://marketplace.visualstudio.com/VSCode" target="_blank" rel="noopener"
												id="nav-extensions" data-m='{"cN":"Extensions","aN":"navigation - Resources"}'>Extensions<span class="codicon codicon-link-external nav-external-icon" aria-hidden="true"></span></a></li>
										<li role="none"><a role="menuitem" id="nav-mcp" href="/mcp" target="_blank" rel="noopener" data-m='{"cN":"MCP","aN":"navigation - Resources"}'>MCP<span class="codicon codicon-link-external nav-external-icon" aria-hidden="true"></span></a></li>
									</ul>
								</li>
							</ul>
							<ul class="nav navbar-nav navbar-right" role="presentation">
								<li>
									<a class="link-button" href="/download" id="nav-download">
										<span>Download</span>
									</a>
								</li>
							</ul>
						</div>
						<div class="navbar-actions">
							<div class="search" role="presentation">
								<div class="nav-search search-control" role="button" tabindex="0" aria-label="Open search dialog">
									<div class="input-group" role="presentation">
										<span class="input-group-btn">
											<span class="btn search-icon-container" aria-hidden="true">
												<img class="search-icon-dark" src="/assets/icons/search-dark.svg" alt="" />
												<img class="search-icon-light" src="/assets/icons/search.svg" alt="" />
											</span>
										</span>
										<span class="search-box form-control" aria-hidden="true" role="presentation"></span>
										<span class="search-shortcut-placeholder">Search</span>
										<span class="search-shortcut-overlay"></span>
									</div>
								</div>					</div>
							<button type="button" class="theme-switch" id="theme-toggle">
								<img class="theme-icon-light" src="/assets/icons/theme-light.svg" alt="Switch to the dark theme" />
								<img class="theme-icon-dark" src="/assets/icons/theme-dark.svg" alt="Switch to the light theme" />
							</button>
							<a class="link-button navbar-actions-download" href="/Download">
								<span>Download</span>
							</a>
						</div>
						<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse"
							aria-label="Expand and Collapse Menu">
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
						</button>
					</div>
				</nav>
			</div>
		</div>		<div data-announcement-version="2026-06-01-vscode-live-build" class="updates-banner ">
			<div class="container">
				<p class="message"><a href="https://aka.ms/VSCode/Livestage?source=vsc-website-banner" target="_blank" rel="noopener">📼 Rewatch VS Code Live at MS Build 2026</a></p>
			</div>
			<div tabindex="0" role="button" title="Dismiss this update" class="dismiss-btn" id="banner-dismiss-btn"><span class="sr-only">Dismiss this update</span><span aria-hidden="true" class="glyph-icon"></span></div>
		</div>
		<script>
			// Hide the banner synchronously (before first paint) if this version was
			// already dismissed, to avoid a flicker/layout shift once the main bundle loads.
			(function () {
				try {
					var banner = document.currentScript.previousElementSibling;
					if (banner && localStorage.getItem('dismissedAnnouncementVersion') === banner.getAttribute('data-announcement-version')) {
						banner.classList.add('js-hidden');
					}
				} catch (e) { /* ignore */ }
			})();
		</script>
		<!-- This div wraps around the entire site -->
		<!-- The body itself should already have a main tag -->
		<main id="main-content">
			<div class="body-content docs docs-github-layout">
    <div class="docs-layout-wrapper">
        <!-- Left sidebar - Table of Contents -->
        <aside class="docs-left-sidebar">
            <nav id="docs-navbar" aria-label="Blog posts" class="docs-nav updates-nav visible-md visible-lg">
            	<h4>Blog posts</h4>
            	<ul class="nav">
            		
            			<li class="active">
            				<a href="/blogs/2026/07/06/optimizing-vscode-coding-harness-model-providers" aria-label="Current Page: GPT-5.5 Prompt Tuning">GPT-5.5 Prompt Tuning</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2026/06/26/iterating-faster-with-ts-7" >Iterating faster with TypeScript 7</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2026/06/19/what-50000-runs-taught-us" >50,000 Runs, One Eval</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2026/06/18/byok-vscode" >Bring Your Own Key</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2026/06/17/improving-token-efficiency-in-github-copilot" >Improving Token Efficiency</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2026/05/15/agent-harnesses-github-copilot-vscode" >Coding Harness</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2026/03/13/how-VS-Code-Builds-with-AI" >How VS Code Builds with AI</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2026/03/05/making-agents-practical-for-real-world-development" >Agents for Real-World Dev</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2026/02/26/long-distance-nes" >Long Distance NES</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2026/02/05/multi-agent-development" >Multi-Agent Development</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2026/01/26/mcp-apps-support" >MCP Apps Support</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2026/01/15/docfind" >Building docfind</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2025/12/03/introducing-vs-code-insiders-podcast" >Introducing the VS Code Insiders Podcast</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2025/11/18/PrivateMarketplace" >Announcing Private Marketplace for VS Code</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2025/11/04/openSourceAIEditorSecondMilestone" >Open Source AI Editor: Second Milestone</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2025/11/03/unified-agent-experience" >A Unified Agent Experience</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2025/10/22/bring-your-own-key" >Expanding Model Choice</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2025/09/15/autoModelSelection" >Introducing auto model selection (preview)</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2025/07/17/copilot-coding-agent" >Command GitHub's Coding Agent from VS Code</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2025/06/30/openSourceAIEditorFirstMilestone" >Open Source AI Editor: First Milestone</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2025/06/12/full-mcp-spec-support" >Full MCP Spec Support</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2025/05/27/ai-and-remote" >Enhance productivity with AI + Remote Dev</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2025/05/19/openSourceAIEditor" >Open Source AI Editor</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2025/05/12/agent-mode-meets-mcp" >Adding MCP in VS Code</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2025/03/26/custom-instructions" >Better AI results with custom instructions</a>
            			</li>
            		
            		<li >
            			<a href="/blogs/archive" class="archive-link" >View All Posts</a>
            		</li>
            	</ul>
            </nav>
            <nav id="small-nav" aria-label="Blog posts" class="docs-nav updates-nav hidden-md hidden-lg">
            	<label class="faux-h4" for="small-nav-dropdown">Blogs</label>
            	<select id="small-nav-dropdown" aria-label="blog posts">
            		
            			<option value="/blogs/2026/07/06/optimizing-vscode-coding-harness-model-providers" selected>GPT-5.5 Prompt Tuning</option>
            		
            			<option value="/blogs/2026/06/26/iterating-faster-with-ts-7" >Iterating faster with TypeScript 7</option>
            		
            			<option value="/blogs/2026/06/19/what-50000-runs-taught-us" >50,000 Runs, One Eval</option>
            		
            			<option value="/blogs/2026/06/18/byok-vscode" >Bring Your Own Key</option>
            		
            			<option value="/blogs/2026/06/17/improving-token-efficiency-in-github-copilot" >Improving Token Efficiency</option>
            		
            			<option value="/blogs/2026/05/15/agent-harnesses-github-copilot-vscode" >Coding Harness</option>
            		
            			<option value="/blogs/2026/03/13/how-VS-Code-Builds-with-AI" >How VS Code Builds with AI</option>
            		
            			<option value="/blogs/2026/03/05/making-agents-practical-for-real-world-development" >Agents for Real-World Dev</option>
            		
            			<option value="/blogs/2026/02/26/long-distance-nes" >Long Distance NES</option>
            		
            			<option value="/blogs/2026/02/05/multi-agent-development" >Multi-Agent Development</option>
            		
            			<option value="/blogs/2026/01/26/mcp-apps-support" >MCP Apps Support</option>
            		
            			<option value="/blogs/2026/01/15/docfind" >Building docfind</option>
            		
            			<option value="/blogs/2025/12/03/introducing-vs-code-insiders-podcast" >Introducing the VS Code Insiders Podcast</option>
            		
            			<option value="/blogs/2025/11/18/PrivateMarketplace" >Announcing Private Marketplace for VS Code</option>
            		
            			<option value="/blogs/2025/11/04/openSourceAIEditorSecondMilestone" >Open Source AI Editor: Second Milestone</option>
            		
            			<option value="/blogs/2025/11/03/unified-agent-experience" >A Unified Agent Experience</option>
            		
            			<option value="/blogs/2025/10/22/bring-your-own-key" >Expanding Model Choice</option>
            		
            			<option value="/blogs/2025/09/15/autoModelSelection" >Introducing auto model selection (preview)</option>
            		
            			<option value="/blogs/2025/07/17/copilot-coding-agent" >Command GitHub's Coding Agent from VS Code</option>
            		
            			<option value="/blogs/2025/06/30/openSourceAIEditorFirstMilestone" >Open Source AI Editor: First Milestone</option>
            		
            			<option value="/blogs/2025/06/12/full-mcp-spec-support" >Full MCP Spec Support</option>
            		
            			<option value="/blogs/2025/05/27/ai-and-remote" >Enhance productivity with AI + Remote Dev</option>
            		
            			<option value="/blogs/2025/05/19/openSourceAIEditor" >Open Source AI Editor</option>
            		
            			<option value="/blogs/2025/05/12/agent-mode-meets-mcp" >Adding MCP in VS Code</option>
            		
            			<option value="/blogs/2025/03/26/custom-instructions" >Better AI results with custom instructions</option>
            		
            		<option value="/blogs/archive" >View All Posts</option>
            	</select>
            </nav>        </aside>
        
        <!-- Content wrapper contains main content + right sidebar -->
        <div class="docs-content-wrapper">
            <!-- Main article content -->
            <main class="docs-main-content body">
                <h1>How Prompt Tuning Improved GPT-5.5 in VS Code</h1>
<p>July 6, 2026 by VS Code Team, <a href="https://x.com/code" class="external-link" target="_blank">@code</a></p>
<p>In our <a href="https://code.visualstudio.com/blogs/2026/05/15/agent-harnesses-github-copilot-vscode">previous post</a>, we introduced the VS Code coding harness, the layer that connects the model to tools, context, instructions, and the agent loop, giving the model the ability to perform coding tasks.</p>
<p>Each model responds to tool calls and instructions differently, and the harness can adapt to improve results. This post walks through a two-week experiment we ran in partnership with OpenAI to tune the <code>GPT-5.5</code> system prompt in VS Code. The question was simple: if we nudge the agent to explore less and validate sooner, can it get faster and cheaper without getting worse? With OpenAI's model expertise and our harness data, we tested two small prompt changes, measured them against a control on live traffic, and shipped the winner.</p>
<p>This matters more with usage-based billing in place. Token efficiency isn't only an infrastructure metric: every token the agent spends wandering is a token you pay for and wait on. An agent that reaches a grounded edit sooner is both a better experience and a smaller bill.</p>
<h2 id="_the-hypothesis-explore-less-validate-sooner" data-needslink="_the-hypothesis-explore-less-validate-sooner">The hypothesis: explore less, validate sooner</h2>
<p>Following the launch of <code>GPT-5.5</code>, we looked at how the model spent tokens inside the VS Code agent harness, as part of the work described in <a href="https://code.visualstudio.com/blogs/2026/06/17/improving-token-efficiency-in-github-copilot/">Improving token efficiency in GitHub Copilot</a>. Two patterns stood out: where the model spent tokens, and where it over-explored before acting. Agents can spend a lot of effort searching, rereading, and comparing nearby paths before making a useful edit.</p>
<p>That pointed to a single, testable idea: the agent should spend less effort wandering and more effort moving through a deliberate loop of evidence, action, and validation.</p>
<p><img src="/assets/blogs/2026/07/06/gpt55-agent-loop.svg" alt="Diagram contrasting an agent that over-explores with many scattered search and read steps before its first edit, versus a Treatment B agent that moves through a deliberate anchor, gather minimal context, edit, and validate loop." loading="lazy"></p>
<p>After testing different hypotheses and running offline evaluations, we turned that idea into two variants of the <code>GPT-5.5</code> system prompt, both were promising in offline evals, and we tested them against the current default on live traffic.</p>
<h2 id="_inside-the-experiment" data-needslink="_inside-the-experiment">Inside the experiment</h2>
<p>We ran the experiment in VS Code over a two-week window, splitting <code>GPT-5.5</code> agent traffic across two treatment groups and one control group with a 25/25/25 split. Both treatments test the same hypothesis but differ in how much structure they add to the prompt.</p>
<table class="table table-striped">
<thead>
<tr>
<th>Group</th>
<th>Variant name</th>
<th>Description</th>
<th style="text-align:right">Traffic allocation</th>
</tr>
</thead>
<tbody>
<tr>
<td>Control</td>
<td><code>PRPT_CTRL</code></td>
<td>Current default prompt</td>
<td style="text-align:right">25%</td>
</tr>
<tr>
<td>Treatment A</td>
<td><code>PRPT_SRCH</code></td>
<td>Economical search and edit: single, compact reminder to limit exploration before acting</td>
<td style="text-align:right">25%</td>
</tr>
<tr>
<td>Treatment B</td>
<td><code>PRPT_LRG</code></td>
<td>Large prompt sections: broader restructure covering the full edit-and-validate loop</td>
<td style="text-align:right">25%</td>
</tr>
</tbody>
</table>
<blockquote><p><strong>Note:</strong> The allocations add up to 75% because the experiment scorecard compares evenly sized groups. The remaining <code>GPT-5.5</code> traffic continued to use the default prompt outside this scorecard slice, so we could compare the treatments and control across the same kind of user traffic.</p>
</blockquote><h3 id="_treatment-a-economical-search-and-edit" data-needslink="_treatment-a-economical-search-and-edit">Treatment A: economical search and edit</h3>
<p>Treatment A makes a small, focused change: a single, compact reminder that nudges the model to reduce unnecessary exploration.</p>
<p>The <code>&lt;economical_search_and_edit&gt;</code> section in the prompt instructs the agent to <strong>start from a concrete anchor, gather only enough local context, avoid broad exploration, act once there is a cheap discriminating check, and avoid rereading unchanged context.</strong></p>
<p>You can find the complete implementation details in <a href="https://github.com/microsoft/vscode/blob/56d74126ee02bf1104e813bf4a41f10e90b2119c/extensions/copilot/src/extension/prompts/node/agent/openai/gpt55BasePrompt.tsx#L172-L178" class="external-link" target="_blank"><code>gpt55BasePrompt.tsx</code></a>:</p>
<pre class="shiki" data-lang="tsx" shiki-themes dark-plus light-plus" style="--shiki-dark:#D4D4D4;--shiki-light:#000000;--shiki-dark-bg:#1E1E1E;--shiki-light-bg:#FFFFFF" tabindex="0"><code><span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">{</span><span style="--shiki-dark:#9CDCFE;--shiki-light:#001080">economicalSearchAndEditEnabled</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000"> &#x26;&#x26; </span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;</span><span style="--shiki-dark:#4EC9B0;--shiki-light:#267F99">Tag</span><span style="--shiki-dark:#9CDCFE;--shiki-light:#E50000"> name</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">=</span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">'economical_search_and_edit'</span><span style="--shiki-dark:#808080;--shiki-light:#800000">></span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">    - Start from the most concrete available anchor: a file, symbol, failing behavior, failing command, or nearby implementation surface.</span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;</span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">br</span><span style="--shiki-dark:#808080;--shiki-light:#800000"> /></span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">    - Gather only enough nearby context to choose one plausible local hypothesis and one cheap check that could disconfirm it.</span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;</span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">br</span><span style="--shiki-dark:#808080;--shiki-light:#800000"> /></span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">    - Prefer one targeted search or nearby read over broad repo exploration.</span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;</span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">br</span><span style="--shiki-dark:#808080;--shiki-light:#800000"> /></span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">    - Once the cheapest discriminating check is known, act.</span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;</span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">br</span><span style="--shiki-dark:#808080;--shiki-light:#800000"> /></span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">    - Do not re-read unchanged context unless a new result makes it relevant.</span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;</span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">br</span><span style="--shiki-dark:#808080;--shiki-light:#800000"> /></span></span>
<span class="line"><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;/</span><span style="--shiki-dark:#4EC9B0;--shiki-light:#267F99">Tag</span><span style="--shiki-dark:#808080;--shiki-light:#800000">></span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">}</span></span>
<span class="line"></span></code></pre>
<h3 id="_treatment-b-large-prompt-sections" data-needslink="_treatment-b-large-prompt-sections">Treatment B: large prompt sections</h3>
<p>Treatment B tested a broader version of the same idea of limiting exploration. Instead of adding a single, compact reminder about economical search, it reorganizes the agent workflow into explicit <code>&lt;Before_the_first_edit&gt;</code> and <code>&lt;After_the_first_edit&gt;</code> sections. Unlike Treatment A, these additions make the system prompt itself larger, so a key question was whether the added structure would still improve efficiency, not just agent behavior.</p>
<p>The goal was to solve the full loop and not only the search step: <strong>form a local hypothesis before editing</strong>, <strong>avoid broad exploration</strong>, <strong>make a grounded first edit</strong>, and <strong>validate immediately after the first substantive edit</strong>.</p>
<p>You can find the complete implementation details in <a href="https://github.com/microsoft/vscode/blob/56d74126ee02bf1104e813bf4a41f10e90b2119c/extensions/copilot/src/extension/prompts/node/agent/openai/gpt55BasePrompt.tsx#L33-L62" class="external-link" target="_blank"><code>gpt55BasePrompt.tsx</code></a>:</p>
<pre class="shiki" data-lang="tsx" shiki-themes dark-plus light-plus" style="--shiki-dark:#D4D4D4;--shiki-light:#000000;--shiki-dark-bg:#1E1E1E;--shiki-light-bg:#FFFFFF" tabindex="0"><code><span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">{</span><span style="--shiki-dark:#9CDCFE;--shiki-light:#001080">largePromptSectionsEnabled</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000"> &#x26;&#x26; </span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;></span></span>
<span class="line"><span style="--shiki-dark:#808080;--shiki-light:#800000">    &#x3C;</span><span style="--shiki-dark:#4EC9B0;--shiki-light:#267F99">Tag</span><span style="--shiki-dark:#9CDCFE;--shiki-light:#E50000"> name</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">=</span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">'Before_the_first_edit'</span><span style="--shiki-dark:#808080;--shiki-light:#800000">></span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">        - Start from the most concrete anchor available: a file, symbol, failing behavior, failing command, test, or nearby implementation surface. If the request does not name one explicitly, use the first targeted search or nearby read to identify that anchor, then continue locally from there.</span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;</span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">br</span><span style="--shiki-dark:#808080;--shiki-light:#800000"> /></span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">        - Before the first edit, gather only enough nearby evidence to state one falsifiable local hypothesis about how the requested behavior should work or why it is failing, and one cheap check that could disconfirm it.</span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;</span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">br</span><span style="--shiki-dark:#808080;--shiki-light:#800000"> /></span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">        [...]</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">        - Once you can state one falsifiable local hypothesis, the nearby code path it depends on, one cheap check that could disconfirm it, and one small edit that would test it, the next action must be a grounded edit.</span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;</span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">br</span><span style="--shiki-dark:#808080;--shiki-light:#800000"> /></span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">        - If confidence is incomplete, the first edit may be a small reversible probe that exposes missing types, behavior mismatches, control-flow gaps, or validation failures.</span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;</span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">br</span><span style="--shiki-dark:#808080;--shiki-light:#800000"> /></span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">        - If you find yourself still searching after that local-routing budget, treat that as drift. Recover by choosing the best current hypothesis and the best available nearby check, then make the smallest plausible edit that will let that check discriminate.</span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;</span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">br</span><span style="--shiki-dark:#808080;--shiki-light:#800000"> /></span></span>
<span class="line"><span style="--shiki-dark:#808080;--shiki-light:#800000">    &#x3C;/</span><span style="--shiki-dark:#4EC9B0;--shiki-light:#267F99">Tag</span><span style="--shiki-dark:#808080;--shiki-light:#800000">></span></span>
<span class="line"><span style="--shiki-dark:#808080;--shiki-light:#800000">    &#x3C;</span><span style="--shiki-dark:#4EC9B0;--shiki-light:#267F99">Tag</span><span style="--shiki-dark:#9CDCFE;--shiki-light:#E50000"> name</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">=</span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">'After_the_first_edit'</span><span style="--shiki-dark:#808080;--shiki-light:#800000">></span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">        - Prefer this order for that first validation action:</span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;</span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">br</span><span style="--shiki-dark:#808080;--shiki-light:#800000"> /></span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">        - the cheapest behavior-scoped or failing check that can falsify the current hypothesis</span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;</span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">br</span><span style="--shiki-dark:#808080;--shiki-light:#800000"> /></span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">        - a narrow test for the touched slice</span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;</span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">br</span><span style="--shiki-dark:#808080;--shiki-light:#800000"> /></span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">        - a narrow compile, lint, or typecheck command for the touched slice</span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;</span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">br</span><span style="--shiki-dark:#808080;--shiki-light:#800000"> /></span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">        [...]</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">        - Finish with at least one post-edit executable validation step whenever the environment provides one. Only fall back to diff-only validation when no focused command exists or commands are unavailable.</span><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;</span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">br</span><span style="--shiki-dark:#808080;--shiki-light:#800000"> /></span></span>
<span class="line"><span style="--shiki-dark:#808080;--shiki-light:#800000">    &#x3C;/</span><span style="--shiki-dark:#4EC9B0;--shiki-light:#267F99">Tag</span><span style="--shiki-dark:#808080;--shiki-light:#800000">></span></span>
<span class="line"><span style="--shiki-dark:#808080;--shiki-light:#800000">&#x3C;/></span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">}</span></span>
<span class="line"></span></code></pre>
<h2 id="_what-the-two-week-scorecard-showed" data-needslink="_what-the-two-week-scorecard-showed">What the two-week scorecard showed</h2>
<p>We tracked the treatments across three dimensions: quality (does the code stick), latency (how fast the first edit lands), and efficiency (tokens and tool calls). Each treatment is compared with the control group in the table below.</p>
<details>
<summary>What each metric measures</summary>
<ul>
<li><strong>10-minute survival rate (by user):</strong> Of the code the model wrote, how much is <em>still in the file 10 minutes later</em> (not deleted or rewritten). It's our proxy for &quot;did the AI's code actually stick.&quot; Measured as surviving characters ÷ total characters written, as a %. <em>E.g. ~90% — roughly 9 of every 10 characters the model added are kept.</em></li>
<li><strong>Commit survival rate (by user):</strong> Narrower and stricter: of the AI-written code, how much survives all the way into a <em>git commit</em>. This is &quot;did it make it into real, saved work.&quot; Same character-ratio calculation, but only counting code present at commit time. <em>E.g. ~87%.</em></li>
<li><strong>p50 Time to First Edit (by turn):</strong> For a typical request, how long from hitting enter until the <em>first actual change lands in your code</em> — not just the model talking, but real work appearing. Measured in seconds. <em>E.g. ~74s for the median turn.</em></li>
<li><strong>p95 Time to First Edit (by turn):</strong> The same clock, but for the <em>worst 5% of requests</em> — the &quot;why is this taking so long?&quot; cases. A key tail-latency guardrail. <em>E.g. ~6.4 min (383K ms), where hard tasks or lots of exploration delay the first edit.</em></li>
<li><strong>p50 total tokens (by user):</strong> How much the model reads + writes for a typical user across their day — a proxy for cost and context load per person. Sum of tokens per user, median across users. <em>E.g. ~12.9M tokens/user/day.</em></li>
<li><strong>p95 total tokens (by turn):</strong> The token weight of the <em>heaviest 5% of individual turns</em> — the big, sprawling requests that drive cost spikes and hit context limits. <em>E.g. a single turn running into the millions of tokens, vs a ~500K–900K median.</em></li>
<li><strong>Average tool calls (by turn):</strong> How many actions (read file, search, run terminal, edit…) the agent takes per request to get the job done. Lower can mean more efficient; too low can mean less thorough. Mean tool calls per turn. <em>E.g. ~24 per turn.</em></li>
</ul>
</details>
<p>Signal legend: <span style="color: #107c10;">●</span> favorable and highly significant (p &lt; 0.001), <span style="color: #107c10;">○</span> favorable and statistically significant (p &lt; 0.05), <span style="color: #d13438;">●</span> unfavorable and highly significant, <span style="color: #d13438;">○</span> unfavorable and statistically significant, <code>-</code> not statistically significant.</p>
<table class="table table-striped">
<thead>
<tr>
<th>Metric</th>
<th style="text-align:right">Treatment A (<code>PRPT_SRCH</code>) impact</th>
<th style="text-align:right">P-value</th>
<th style="text-align:center">Signal</th>
<th style="text-align:right">Treatment B (<code>PRPT_LRG</code>) impact</th>
<th style="text-align:right">P-value</th>
<th style="text-align:center">Signal</th>
</tr>
</thead>
<tbody>
<tr>
<td>10-minute survival rate (by user)</td>
<td style="text-align:right">-0.40% (-0.37 pp)</td>
<td style="text-align:right">0.0707</td>
<td style="text-align:center">-</td>
<td style="text-align:right">-0.44% (-0.41 pp)</td>
<td style="text-align:right">0.0493</td>
<td style="text-align:center"><span style="color: #d13438;">○</span></td>
</tr>
<tr>
<td>Commit survival rate (by user)</td>
<td style="text-align:right">-0.48% (-0.41 pp)</td>
<td style="text-align:right">0.3200</td>
<td style="text-align:center">-</td>
<td style="text-align:right">+0.68% (+0.57 pp)</td>
<td style="text-align:right">0.1533</td>
<td style="text-align:center">-</td>
</tr>
<tr>
<td>p50 Time to First Edit (by turn)</td>
<td style="text-align:right">-2.88% (2.0s faster)</td>
<td style="text-align:right">0.0271</td>
<td style="text-align:center"><span style="color: #107c10;">○</span></td>
<td style="text-align:right">-5.68% (3.9s faster)</td>
<td style="text-align:right">2e-5</td>
<td style="text-align:center"><span style="color: #107c10;">●</span></td>
</tr>
<tr>
<td>p95 Time to First Edit (by turn)</td>
<td style="text-align:right">-1.93% (8.0s faster)</td>
<td style="text-align:right">0.1928</td>
<td style="text-align:center">-</td>
<td style="text-align:right">-9.30% (38.8s faster)</td>
<td style="text-align:right">1e-10</td>
<td style="text-align:center"><span style="color: #107c10;">●</span></td>
</tr>
<tr>
<td>p50 total tokens (by user)</td>
<td style="text-align:right">-2.54% (0.2M fewer tokens)</td>
<td style="text-align:right">0.3429</td>
<td style="text-align:center">-</td>
<td style="text-align:right">-3.25% (0.3M fewer tokens)</td>
<td style="text-align:right">0.2094</td>
<td style="text-align:center">-</td>
</tr>
<tr>
<td>p95 total tokens (by turn)</td>
<td style="text-align:right">-5.19% (0.3M fewer tokens)</td>
<td style="text-align:right">0.0157</td>
<td style="text-align:center"><span style="color: #107c10;">○</span></td>
<td style="text-align:right">-7.64% (0.5M fewer tokens)</td>
<td style="text-align:right">0.0003</td>
<td style="text-align:center"><span style="color: #107c10;">●</span></td>
</tr>
<tr>
<td>Average tool calls (by turn)</td>
<td style="text-align:right">-3.19% (0.77 fewer tool calls)</td>
<td style="text-align:right">0.0091</td>
<td style="text-align:center"><span style="color: #107c10;">○</span></td>
<td style="text-align:right">-8.54% (2.04 fewer tool calls)</td>
<td style="text-align:right">1e-12</td>
<td style="text-align:center"><span style="color: #107c10;">●</span></td>
</tr>
</tbody>
</table>
<p><img src="/assets/blogs/2026/07/06/gpt55-metrics-comparison.svg" alt="Grouped bar chart comparing the percentage impact of Treatment A and Treatment B against the control baseline across seven metrics, showing that Treatment B produces the largest reductions in latency, token usage, and tool calls." loading="lazy"></p>
<ul>
<li>
<p><strong>Quality</strong>: the guardrail metrics stayed mostly healthy. Commit survival rate moved slightly up for Treatment B (+0.68%) and slightly down for Treatment A (-0.48%), <strong>neither statistically significant</strong>. The 10-minute survival rate moved slightly down for both treatments: -0.44% for Treatment B and -0.40% for Treatment A. Only the Treatment B movement crossed the statistical significance threshold, and just barely (p=0.0493), unlike the highly significant efficiency wins. We treated that as a real tradeoff to weigh, but the movement was small and the other quality guardrail did not regress.</p>
</li>
<li>
<p><strong>Latency</strong>: Treatment B delivered the strongest edit-latency wins, and both were <strong>highly statistically significant</strong>: p50 Time to First Edit improved -5.68% (3.9s faster, p=2e-5), and p95 Time to First Edit improved -9.30% (38.8s faster, p=1e-10). Treatment A moved in the right direction, but the edit-latency effects were weaker: p50 Time to First Edit -2.88% (2.0s faster, p=0.0271), and p95 Time to First Edit -1.93% (not significant).</p>
</li>
<li>
<p><strong>Token efficiency</strong>: both treatments reduced median total tokens per user, but those p50 movements were <strong>not statistically significant</strong>: -3.25% for Treatment B and -2.54% for Treatment A. At the upper tail, Treatment B reduced p95 total tokens by -7.64%, <strong>highly statistically significant</strong> (p=0.0003). Treatment A also reduced p95 total tokens by -5.19%, <strong>statistically significant</strong> (p=0.0157). Both variants reduced average tool calls per turn: -8.54% (2.04 fewer tool calls) for Treatment B, <strong>highly statistically significant</strong> (p=1e-12), and -3.19% (0.77 fewer tool calls) for Treatment A, <strong>statistically significant</strong> (p=0.0091).</p>
</li>
</ul>
<p>Treatment B had the strongest overall profile: clear latency wins, significant upper-tail token reductions, fewer tool calls, and mostly stable quality guardrails. The one movement worth watching, the small drop in 10-minute survival, was only lightly significant (p=0.0493), while the latency, token, and tool-call gains were larger and far more robust. Treatment A moved several metrics in the right direction, but Treatment B was more consistent across the measures that matter most for VS Code.</p>
<p>So we shipped it: Treatment B, <code>LargePromptSections</code>, is now the default <code>GPT-5.5</code> system prompt.</p>
<p>The takeaway isn't only that the numbers moved. The movement was tied to a specific, testable harness hypothesis from provider feedback, validated offline first and then confirmed online over a two-week production window. That's the loop we want to keep running.</p>
<h2 id="_continuous-optimization" data-needslink="_continuous-optimization">Continuous optimization</h2>
<p>This experiment is one example of how we work with model providers beyond launch day. A model release is not the end of the tuning loop. It is another chance to look at real VS Code behavior, test focused improvements, and find new ways to make the experience faster, more reliable, and more efficient.</p>
<p>We'll keep looking for those improvements across models, prompts, tools, and the VS Code coding harness, so more of each agent's budget goes to the work that matters instead of unnecessary exploration.</p>
<p>Try <a href="/docs/getstarted/getting-started">agents in VS Code</a>, switch between models, and compare how different models approach the same task. Share your feedback in <a href="https://github.com/microsoft/vscode" class="external-link" target="_blank">our GitHub repo</a>. It helps us keep improving the experience.</p>
<p>Happy coding! 💙</p>

            </main>
            
            <!-- Right sidebar - On This Page -->
            <aside class="docs-right-sidebar hidden-xs">
                <nav id="docs-subnavbar" aria-labelledby="docs-subnavbar-label">
                    
                    <h4 id="docs-subnavbar-label"><span class="sr-only">On this page there are 4 sections</span><span
                            aria-hidden="true">On this page</span></h4>
                    <ul class="nav">
                        
                        <li><a href="#_the-hypothesis-explore-less-validate-sooner">The hypothesis: explore less, validate sooner</a></li>
                        
                        <li><a href="#_inside-the-experiment">Inside the experiment</a></li>
                        
                        <li><a href="#_what-the-two-week-scorecard-showed">What the two-week scorecard showed</a></li>
                        
                        <li><a href="#_continuous-optimization">Continuous optimization</a></li>
                        
                    </ul>
                    
                </nav>
            </aside>
        </div>
        
        <!-- Mobile connect widget -->
        <div class="docs-mobile-widgets visible-xs">
            <div class="connect-widget"></div>
        </div>
    </div>
</div>
		</main>
	</div>

	<div id="search-popup-overlay" class="search-popup-overlay" role="dialog" aria-modal="true" aria-label="Search">
		<div class="search-popup-container">
			<div class="search-popup-header">
				<form class="search-popup-form">
					<div class="input-group">
						<input type="text" name="q" class="search-box form-control" placeholder="Search the website"
							aria-label="Search text" role="combobox" aria-expanded="false"
							aria-autocomplete="list" aria-controls="search-results-listbox"
							aria-activedescendant="" />
						<span class="input-group-btn">
							<button tabindex="0" class="btn" type="submit" aria-label="Search">
								<img class="search-icon-dark" src="/assets/icons/search-dark.svg" alt="Search" />
								<img class="search-icon-light" src="/assets/icons/search.svg" alt="Search" />
							</button>
						</span>
					</div>
				</form>
				<button class="search-popup-close" type="button" aria-label="Close search"><i class="codicon codicon-close" aria-hidden="true"></i></button>
			</div>
			<div class="search-popup-results">
				<ul class="search-popup-results-list" id="search-results-listbox" role="listbox" aria-label="Search results"></ul>
			</div>
			<div class="sr-only" role="status" aria-live="polite" aria-atomic="true" id="search-popup-status"></div>
		</div>
	</div>


	<footer role="contentinfo" class="container">
		<div class="footer-container">
			<div class="footer-row">
				<div class="footer-social">
					<ul class="links">
						<li>
							<a href="https://github.com/microsoft/vscode"><img src="/assets/icons/github-icon.svg" alt="VS Code on Github"></a>
						</li>
						<li>
							<a href="https://go.microsoft.com/fwlink/?LinkID=533687"><img src="/assets/icons/x-icon.svg" class="x-icon" alt="Follow us on X"></a>
						</li>
						<li>
							<a href="https://www.linkedin.com/showcase/vs-code"><img src="/assets/icons/linkedin-icon.svg" alt="VS Code on LinkedIn"></a>
						</li>
						<li>
							<a href="https://bsky.app/profile/vscode.dev"><img src="/assets/icons/bluesky-icon.svg" alt="VS Code on Bluesky"></a>
						</li>
						<li>
							<a href="https://www.reddit.com/r/vscode/"><img src="/assets/icons/reddit-icon.svg" alt="Join the VS Code community on Reddit"></a>
						</li>
						<li>
							<a href="https://www.vscodepodcast.com"><img src="/assets/icons/podcast-icon.svg" alt="The VS Code Insiders Podcast"></a>
						</li>
						<li>
							<a href="https://www.tiktok.com/@vscode"><img src="/assets/icons/tiktok-icon.svg" alt="VS Code on TikTok"></a>
						</li>
						<li>
							<a href="https://www.youtube.com/@code"><img src="/assets/icons/youtube-icon.svg" alt="VS Code on YouTube"></a>
						</li>
						<script>
							function manageConsent() {
								if (siteConsent && siteConsent.isConsentRequired) {
									siteConsent.manageConsent();
								}
							}
						</script>
					</ul>
					<a id="footer-microsoft-link" class="microsoft-logo" href="https://www.microsoft.com">
						<img src="/assets/icons/microsoft.svg" alt="Microsoft homepage" />
					</a>
				</div>
			</div>
			<div class="footer-row">
				<ul class="links">
					<li><a id="footer-support-link" href="https://support.serviceshub.microsoft.com/supportforbusiness/create?sapId=d66407ed-3967-b000-4cfb-2c318cad363d"
						target="_blank" rel="noopener" title="Get support for VS Code"
						aria-label="Get support for VS Code (opens in new tab)">Support</a></li>
					<li><a id="footer-privacy-link" href="https://go.microsoft.com/fwlink/?LinkId=521839"
