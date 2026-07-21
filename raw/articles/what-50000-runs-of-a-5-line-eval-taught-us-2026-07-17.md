---
source_url: https://code.visualstudio.com/blogs/2026/06/19/what-50000-runs-taught-us
ingested: 2026-07-17
sha256: a0c47d8700aa056ab841281ec165c40218bbf5cfa978440499e962e4af487723
blog_source: VS Code Blog
---
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8" />
	<meta name="awa-expId" content="cv-downloadv2:1227264;" />
	<meta name="awa-env" content="prod" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="google-site-verification" content="hNs7DXrTySP_X-0P_AC0WulAXvUwgSXEmgfcO2r79dw" />

	<!-- Twitter and Facebook OpenGraph Metadata-->
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:site" content="@code" />

	<meta name="description" content="How AI coding models calibrate effort, token cost, and tool use on even the simplest task, and what that means for model selection and cost." />
<meta name="keywords" content="" />
<!-- Twitter and Facebook OpenGraph Metadata-->
<meta name="twitter:card" content="summary_large_image" />
<meta property="og:url" content="https://code.visualstudio.com/blogs/2026/06/19/what-50000-runs-taught-us" />
<meta property="og:type" content="article" />
<meta property="og:title" content="What 50,000 Runs of a 5-Line Eval Taught Us" />
<meta property="og:description" content="How AI coding models calibrate effort, token cost, and tool use on even the simplest task, and what that means for model selection and cost." />

<meta property="og:image" content="https://code.visualstudio.com/assets/blogs/2026/06/19/5000-runs-social.png" />



	<link rel="shortcut icon" href="/assets/favicon.ico" sizes="128x128" />
	<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">

	<title>What 50,000 Runs of a 5-Line Eval Taught Us</title>

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
            		
            			<li >
            				<a href="/blogs/2026/07/06/optimizing-vscode-coding-harness-model-providers" >GPT-5.5 Prompt Tuning</a>
            			</li>
            		
            			<li >
            				<a href="/blogs/2026/06/26/iterating-faster-with-ts-7" >Iterating faster with TypeScript 7</a>
            			</li>
            		
            			<li class="active">
            				<a href="/blogs/2026/06/19/what-50000-runs-taught-us" aria-label="Current Page: 50,000 Runs, One Eval">50,000 Runs, One Eval</a>
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
            		
            			<option value="/blogs/2026/07/06/optimizing-vscode-coding-harness-model-providers" >GPT-5.5 Prompt Tuning</option>
            		
            			<option value="/blogs/2026/06/26/iterating-faster-with-ts-7" >Iterating faster with TypeScript 7</option>
            		
            			<option value="/blogs/2026/06/19/what-50000-runs-taught-us" selected>50,000 Runs, One Eval</option>
            		
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
                <h1>What 50,000 Runs of a 5-Line Eval Taught Us</h1>
<p>June 19, 2026 by VS Code Eval Team, <a href="https://x.com/code" class="external-link" target="_blank">@code</a></p>
<p>Over the last six months, we have run the same tiny eval more than 50,000 times. It gives the VS Code agent one instruction: write a string to a file. No large codebase to understand, no test suite to debug, no architectural decision to make. It is our smoke test, a quick way to confirm that the end-to-end model interaction still works.</p>
<p>A task this simple gives us an immediate read on the health of the system: how reliably the agent finishes the work and what kinds of failures show up in practice. We didn't intend it to be more than that. But at this scale, it became a surprisingly rich source of insight into how models approach even the simplest request.</p>
<p>In our <a href="https://code.visualstudio.com/blogs/2026/05/15/agent-harnesses-github-copilot-vscode">previous post</a>, we introduced VSC-Bench, the offline evaluation suite we use to measure agent behavior in VS Code. In this blog post, we look at <em>how</em> models solve a simple task and what it tells us about efficiency, model selection, and the value of small, stable evals.</p>
<h2 id="_the-five-line-eval" data-needslink="_the-five-line-eval">The five-line eval</h2>
<p>A simple task is valuable precisely because it removes variables. When the work is unambiguous and the correct answer is fixed, anything that changes between runs comes from the model or the system around it, not from the task itself. That makes a small eval a sensitive instrument: it reacts to harness regressions, infrastructure incidents, and differences in model behavior, without the noise of a complex problem to interpret.</p>
<p>The <code>say_hello</code> task we use for this is built around that idea. Every run starts in the same empty workspace, with the same tools and the same fixed prompt, using our VS Code agent harness. The task asks the agent to &quot;Add HELLO to HELLO.txt&quot; and checks two assertions: that the file exists and that it contains the expected content.</p>
<pre class="shiki" data-lang="yaml" shiki-themes dark-plus light-plus" style="--shiki-dark:#D4D4D4;--shiki-light:#000000;--shiki-dark-bg:#1E1E1E;--shiki-light-bg:#FFFFFF" tabindex="0"><code><span class="line"><span style="--shiki-dark:#569CD6;--shiki-light:#800000">promptSteps</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">:</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">  - </span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">text</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#0000FF">Add HELLO to HELLO.txt.</span></span>
<span class="line"><span style="--shiki-dark:#569CD6;--shiki-light:#800000">    assertions</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">:</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">        - </span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">check</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#0000FF">file_exists("HELLO.txt")</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">        - </span><span style="--shiki-dark:#569CD6;--shiki-light:#800000">check</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#0000FF">file_contains("HELLO.txt", "HELLO")</span></span>
<span class="line"></span></code></pre>
<p>Because <code>say_hello</code> runs as a smoke test before every benchmark suite, it quietly accumulated 50,974 runs across 30 models over six months. That volume turned a basic sanity check into a useful dataset on how differently models handle even the simplest work.</p>
<p>A developer doing this task would recognize that the workspace is empty, create <code>HELLO.txt</code>, and add the requested content. In the most direct VS Code agent path, this translates into a single <code>create_file</code> tool call with <code>HELLO</code> as the file content.</p>
<pre class="shiki" data-lang="yaml" shiki-themes dark-plus light-plus" style="--shiki-dark:#D4D4D4;--shiki-light:#000000;--shiki-dark-bg:#1E1E1E;--shiki-light-bg:#FFFFFF" tabindex="0"><code><span class="line"><span style="--shiki-dark:#569CD6;--shiki-light:#800000">tool</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000"> : </span><span style="--shiki-dark:#CE9178;--shiki-light:#0000FF">create_file</span></span>
<span class="line"><span style="--shiki-dark:#569CD6;--shiki-light:#800000">args</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000"> : {</span></span>
<span class="line"><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">  "filePath"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"/path/to/workspace/HELLO.txt"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">,</span></span>
<span class="line"><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">  "content"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"HELLO"</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">}</span></span>
<span class="line"></span></code></pre>
<div class="markdown-alert note" dir="auto">
      <span>
        <svg class="markdown-alert-icon" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true">
          <path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM6.5 7.75A.75.75 0 0 1 7.25 7h1a.75.75 0 0 1 .75.75v2.75h.25a.75.75 0 0 1 0 1.5h-2a.75.75 0 0 1 0-1.5h.25v-2h-.25a.75.75 0 0 1-.75-.75ZM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z">
          </path>
        </svg>
        Note
      </span><p>The VS Code eval harness includes the workspace state in the initial prompt context. We assume that the model should not perform redundant existence checks.</p>
</div><h2 id="_how-models-solve-sayhello" data-needslink="_how-models-solve-sayhello">How models solve <code>say_hello</code></h2>
<p>As expected, the <code>say_hello</code> task is easy enough that all models pass it most of the time. The interesting part is not whether they can do the work, but <em>how</em> they do it. Can the model recognize that this is a basic request that only requires a simple solution? Or does it still treat it like a complex problem that requires planning, exploration, and search?</p>
<p>To establish a baseline, we filtered for passing runs that used this one-tool-call path and looked at the lowest output-token counts in that group. Those runs averaged roughly 50 output tokens, including the tool-call structure. We then measured how often each model took that path.</p>
<p><img src="/assets/blogs/2026/06/19/passing-rate.png" alt="Chart showing the percentage of passing runs where the model achieves the one-tool-call direct path." loading="lazy"></p>
<p>One model takes the direct path every time. The broader trend is what stands out: a few models often take the direct path, most do so only occasionally, and five never do.</p>
<p>At the top, Model-A stands alone. It goes straight to file creation in 100% of passing runs, using a single tool call every time. For this simple request, Model-A always creates the file directly without planning or exploring first. Model-B and Model-C follow at 73% and 71%, respectively.</p>
<p>The large middle cluster, Model-D through Model-P, takes the direct path somewhere between 19% and 52% of the time. These models can recognize a simple task, but not consistently. More often than not, they add a small step first, such as reading internal state or doing light workspace exploration, before creating the file.</p>
<p>Below them, Model-Q through Model-X rarely take the direct path, doing so in 0.2% to 6% of passing runs, with five models falling below 1%. For these models, extra work is the default. They almost always plan, explore, or search before producing the same five-character file.</p>
<p>At the bottom, five models, Model-Y through Model-AC, never take the direct path across thousands of passing runs. They always do something else first: plan, reach for a patch tool instead of simple file creation, search and plan, or narrate at length before creating the file. For them, even the simplest request triggers the full machinery of a complex one.</p>
<p>All models create the file with the right content, but they reach the same outcome with very different amounts of work. Even on a task with almost no ambiguity, some models still plan, search, or choose a more complex editing tool. They all pass the eval, but they do not use the same amount of effort to pass it.</p>
<h2 id="_how-models-spend-their-overhead" data-needslink="_how-models-spend-their-overhead">How models spend their overhead</h2>
<p>Because our offline eval harness captures the complete tool-call sequence, we can turn those traces into model behavior patterns. Across runs, models tend to spend their extra effort in a few familiar ways:</p>
<table class="table table-striped">
<thead>
<tr>
<th>Overhead pattern</th>
<th style="text-align:right">Frequency</th>
<th>Representative models</th>
<th>What happens</th>
</tr>
</thead>
<tbody>
<tr>
<td>Planning before acting</td>
<td style="text-align:right">52-99%</td>
<td>Model-AC, Model-Z, Model-S, 13 other models</td>
<td>Drafts a checklist or reads internal state before creating a 5-character file. Every one of the 16 models we could measure does this in at least half of its runs; Model-AC reaches 99% and Model-Z 96%. On one occasion, four planning steps in a single run for a one-step task.</td>
</tr>
<tr>
<td>Exploring an empty workspace</td>
<td style="text-align:right">56-96%</td>
<td>Model-T, Model-Q, Model-AA</td>
<td>Lists directories or searches for files in an empty workspace. Model-T lists the directory in 96% of runs; Model-AA both lists and searches in 56%, looking for clues in an empty room.</td>
</tr>
<tr>
<td>Narrating the reasoning</td>
<td style="text-align:right">1,441-3,676 tokens</td>
<td>Model-AB, Model-M, Model-U</td>
<td>Emits far more text than any tool call needs, walking through its reasoning and reconfirming the task. These three top the output-token chart at 29-74 times the realistic floor, even though the file itself is five characters.</td>
</tr>
<tr>
<td>Using the wrong tool for the job</td>
<td style="text-align:right">About 95%</td>
<td>Model-AA</td>
<td>Uses a complex patch/edit tool (designed for modifying existing files) instead of simple file creation. Like using a CNC machine to cut a piece of paper.</td>
</tr>
<tr>
<td>Running a terminal command</td>
<td style="text-align:right">3-14%</td>
<td>Model-W, Model-Z, Model-V</td>
<td>Runs a terminal command (<code>echo HELLO &gt; HELLO.txt</code>) when a simpler file-creation API is available.</td>
</tr>
</tbody>
</table>
<p>These are not correctness failures. They are signs that the model does not consistently recognize when the shortest path is enough. On longer tasks, planning and exploration can be valuable. On a one-step task, they add latency and cost without improving the result.</p>
<h2 id="_the-cost-of-overthinking" data-needslink="_the-cost-of-overthinking">The cost of overthinking</h2>
<p>Why should you care about how many extra steps a model takes to write a five-character file? Because those extra steps are not free and translate directly into output token usage, which has an actual cost.</p>
<p>For this simple task, about 50 output tokens is a realistic minimum. The following chart shows the range of output tokens used by different models. The selected models range from that minimum to thousands of tokens for the same five-character result!</p>
<p><img src="/assets/blogs/2026/06/19/token-consumption.png" alt="Chart that shows average output tokens per run vary from near the ideal floor to thousands of tokens for the same HELLO.txt task." loading="lazy"></p>
<p>The chart falls into four clear bands. The extreme group includes Model-AB, Model-M, and Model-U, which average 3,676, 2,120, and 1,441 output tokens, respectively. That is 29 to 74 times more than the realistic minimum for the same five-character result. The high-overhead group, from 400 to 1,000 tokens, includes Model-AA, Model-B, Model-N, Model-H, Model-V, Model-E, Model-S, and Model-K. These models are not in the thousands, but they still spend roughly 8x to 12x the realistic minimum.</p>
<p>The moderate group, from 150 to 400 tokens, includes Model-P, Model-D, Model-X, Model-T, Model-G, Model-Z, Model-I, Model-AC, Model-F, Model-J, and Model-Q. They add overhead, but stay far closer to the task's natural size. The efficient group is below 150 tokens: Model-R, Model-A, Model-Y, Model-W, Model-O, Model-C, and Model-L. Model-L comes closest to our realistic minimum at 55 tokens, showing that a model can complete the task with very little extra narration even when it does not always take the direct tool path.</p>
<p>Choosing a model that overthinks less saves both time and money, but knowing which one is most efficient for a task usually means running your own benchmark. To take that burden off you, the VS Code and GitHub Copilot teams keep investing in optimizations and model routing. For example, <a href="/docs/agents/concepts/language-models#_auto-model-selection">automatic model selection</a> lets VS Code pick the best model for your task.</p>
<h2 id="_model-size-does-not-predict-overhead" data-needslink="_model-size-does-not-predict-overhead">Model size does not predict overhead</h2>
<p>Our first hypothesis was that larger models overthink more, but our data contradicts this:</p>
<ul>
<li>
<p>Model-F (a larger model) uses 160 output tokens on average and 2.1 tool calls. The most disciplined model in its family.</p>
</li>
<li>
<p>Model-H (a smaller model from the same family) uses 485 output tokens on average and 3.7 tool calls. More overhead than its larger sibling.</p>
</li>
<li>
<p>Model-AB (a &quot;mini&quot; model) is the single highest-overhead model at 3,676 output tokens on average. The smallest model in this sample does the most work.</p>
</li>
</ul>
<p>Our read is that newer generations within each model family trend more disciplined, regardless of parameter count. This points to training maturity: how well a model scales its effort to the task in front of it. And that calibration isn't an academic curiosity. It shows up directly on the bill.</p>
<h2 id="_where-do-we-go-from-here" data-needslink="_where-do-we-go-from-here">Where do we go from here?</h2>
<p>We wanted to share a few key insights our team took from these runs, and a few learnings you might be able to apply to your own day-to-day flow.</p>
<div class="markdown-alert note" dir="auto">
      <span>
        <svg class="markdown-alert-icon" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true">
          <path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM6.5 7.75A.75.75 0 0 1 7.25 7h1a.75.75 0 0 1 .75.75v2.75h.25a.75.75 0 0 1 0 1.5h-2a.75.75 0 0 1 0-1.5h.25v-2h-.25a.75.75 0 0 1-.75-.75ZM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z">
          </path>
        </svg>
        Note
      </span><p>The <code>say_hello</code> eval gives us great insights but it represents only one task. For harness optimization, we avoid optimizing too narrowly around a single task. We still run the full benchmark regularly across a diverse task set to validate whether changes improve our harness broadly.</p>
</div><h3 id="_match-the-model-to-your-task" data-needslink="_match-the-model-to-your-task">Match the model to your task</h3>
<p>With <a href="https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/" class="external-link" target="_blank">usage-based billing</a>, output tokens represent both money and time. The difference between the leanest and heaviest model on this task is roughly 70× for identical output. The obvious lesson would be &quot;don't reach for the biggest model to write HELLO.&quot; But that lesson is too blunt, and seeing why is the most useful thing <code>say_hello</code> taught us.</p>
<p>There is an important caveat to these results. <code>say_hello</code> is a short-horizon task with one step and one correct answer. On long-horizon work, planning, exploration, and reasoning can prevent expensive mistakes and improve the odds of finishing. The goal is not to eliminate planning. It is to understand whether a model can tell the difference between a one-step task and a 30-step task.</p>
<p>That is one reason why we think model selection should not become the developer's burden. Signals like effort calibration, token efficiency, and tool discipline can help automatic model routing pick the right model for the task at hand without asking developers to reason about every tradeoff.We continue to invest in and research <a href="/docs/agents/concepts/language-models#_auto-model-selection">automatic model selection in VS Code</a>, so the product can make more of these choices for you over time.</p>
<h3 id="_start-small-measure-well" data-needslink="_start-small-measure-well">Start small, measure well</h3>
<p>Most teams do not start with a private offline benchmark suite they can run every day. Even a simple task, run consistently and logged well, can reveal useful changes in model or system behavior.</p>
<p>Start with the smallest task that has an unambiguous correct answer. Then run it constantly: use it as a preflight check before nightly evals, model onboarding, and infrastructure changes. The task does not need to be clever; it needs to be stable enough that changes in pass rate, latency, tool use, or failure mode mean something.</p>
<p>The important part is to capture enough structure to explain what changed. Record the tool-call sequence, not just the count. Knowing there were 4 tool calls is useful, but incomplete. Knowing that the model planned, explored, searched, and then created the file tells you where the overhead came from and why the run cost more.</p>
<pre class="shiki" data-lang="jsonc" shiki-themes dark-plus light-plus" style="--shiki-dark:#D4D4D4;--shiki-light:#000000;--shiki-dark-bg:#1E1E1E;--shiki-light-bg:#FFFFFF" tabindex="0"><code><span class="line"><span style="--shiki-dark:#6A9955;--shiki-light:#008000">// What most harnesses log:</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">{ </span><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">"tool_calls"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#B5CEA8;--shiki-light:#098658">4</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">, </span><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">"pass"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#569CD6;--shiki-light:#0000FF">true</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000"> }</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-dark:#6A9955;--shiki-light:#008000">// What you actually need:</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">{</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">  "tool_sequence"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: [</span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"plan"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">, </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"list_directory"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">, </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"search_files"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">, </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"create_file"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">],</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">  "output_tokens"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#B5CEA8;--shiki-light:#098658">617</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">,</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">  "pass"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#569CD6;--shiki-light:#0000FF">true</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">}</span></span>
<span class="line"></span></code></pre>
<h2 id="_from-smoke-test-to-signal" data-needslink="_from-smoke-test-to-signal">From smoke test to signal</h2>
<p>The surprising part of <code>say_hello</code> was not that models could write <code>HELLO.txt</code>. It was that a five-character edit made effort visible: which models scaled down, which kept planning or searching, and which system failures only appeared after thousands of runs.</p>
<p>Try the same request with your preferred model in VS Code, inspect its tool calls in the <a href="/docs/agents/agent-troubleshooting/chat-debug-view">Chat Debug View</a>, and consider what your own smallest useful task might be. Share what you find in the <a href="https://github.com/microsoft/vscode" class="external-link" target="_blank">VS Code repository</a>.</p>
<p>Happy coding! 💙</p>

            </main>
            
            <!-- Right sidebar - On This Page -->
            <aside class="docs-right-sidebar hidden-xs">
                <nav id="docs-subnavbar" aria-labelledby="docs-subnavbar-label">
                    
                    <h4 id="docs-subnavbar-label"><span class="sr-only">On this page there are 7 sections</span><span
                            aria-hidden="true">On this page</span></h4>
                    <ul class="nav">
                        
                        <li><a href="#_the-five-line-eval">The five-line eval</a></li>
                        
                        <li><a href="#_how-models-solve-sayhello">How models solve `say_hello`</a></li>
                        
                        <li><a href="#_how-models-spend-their-overhead">How models spend their overhead</a></li>
                        
                        <li><a href="#_the-cost-of-overthinking">The cost of overthinking</a></li>
                        
                        <li><a href="#_model-size-does-not-predict-overhead">Model size does not predict overhead</a></li>
                        
                        <li><a href="#_where-do-we-go-from-here">Where do we go from here?</a></li>
                        
                        <li><a href="#_from-smoke-test-to-signal">From smoke test to signal</a></li>
                        
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
						target="_blank" rel="noopener" title="View the Microsoft privacy statement"
						aria-label="Microsoft privacy statement (opens in new tab)">Privacy</a></li>
					<li style="display: none;"><a id="footer-cookie-link" style="cursor: pointer;" onclick="manageConsent()"
						target="_blank" rel="noopener">Manage Cookies</a></li>
					<li><a id="footer-terms-link" href="https://www.microsoft.com/legal/terms-of-use"
						target="_blank" rel="noopener" title="View the Microsoft Terms of Use"
						aria-label="Microsoft Terms of Use (opens in new tab)">Terms of Use</a></li>
					<li><a id="footer-license-link" href="/License"
						target="_blank" rel="noopener" title="View the Visual Studio Code license"
						aria-label="Visual Studio Code license (opens in new tab)">License</a></li>
				</ul>
			</div>
			<div class="footer-row">
				<ul class="links">
					<li>
						<svg class="privacy-choices" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 14" xml:space="preserve" height="16" width="43">
							<title>Your Privacy Choices Opt-Out Icon</title>
							<path d="M7.4 12.8h6.8l3.1-11.6H7.4C4.2 1.2 1.6 3.8 1.6 7s2.6 5.8 5.8 5.8z" style="fill-rule:evenodd;clip-rule:evenodd;fill:#fff"></path>
							<path d="M22.6 0H7.4c-3.9 0-7 3.1-7 7s3.1 7 7 7h15.2c3.9 0 7-3.1 7-7s-3.2-7-7-7zm-21 7c0-3.2 2.6-5.8 5.8-5.8h9.9l-3.1 11.6H7.4c-3.2 0-5.8-2.6-5.8-5.8z" style="fill-rule:evenodd;clip-rule:evenodd;fill:#06f"></path>
							<path d="M24.6 4c.2.2.2.6 0 .8L22.5 7l2.2 2.2c.2.2.2.6 0 .8-.2.2-.6.2-.8 0l-2.2-2.2-2.2 2.2c-.2.2-.6.2-.8 0-.2-.2-.2-.6 0-.8L20.8 7l-2.2-2.2c-.2-.2-.2-.6 0-.8.2-.2.6-.2.8 0l2.2 2.2L23.8 4c.2-.2.6-.2.8 0z" style="fill:#fff"></path>
							<path d="M12.7 4.1c.2.2.3.6.1.8L8.6 9.8c-.1.1-.2.2-.3.2-.2.1-.5.1-.7-.1L5.4 7.7c-.2-.2-.2-.6 0-.8.2-.2.6-.2.8 0L8 8.6l3.8-4.5c.2-.2.6-.2.9 0z" style="fill:#06f"></path>
						</svg>
						<a id="footer-privacy-choices-link" href="https://aka.ms/YourCaliforniaPrivacyChoices"
						target="_blank" rel="noopener" title="View Your Privacy Choices"
						aria-label="Your Privacy Choices (opens in new tab)">Your Privacy Choices</a></li>
					<li><a id="footer-consumer-health-privacy-link" href="https://go.microsoft.com/fwlink/?linkid=2259814"
						target="_blank" rel="noopener" title="View the Microsoft Consumer Health Privacy policy"
						aria-label="Microsoft Consumer Health Privacy policy (opens in new tab)">Consumer Health Privacy</a></li>
				</ul>
			</div>
		</div>
	</footer>
	<script type="module">
		document.addEventListener('DOMContentLoaded', () => {
			const copilotDeepLinks = document.querySelectorAll('.copilot-deep-link');
			if (copilotDeepLinks.length === 0) {
				return;
			}
			if (window.innerWidth < 992) {
				for (const link of copilotDeepLinks) {
					link.href = 'https://aka.ms/vscode-activatecopilotfree';
				}
			}
		});
	</script>

	<script src="/dist/index.js"></script>

	

	<script type="application/ld+json">
		{
			"@context" : "http://schema.org",
			"@type" : "SoftwareApplication",
			"name" : "Visual Studio Code",
			"softwareVersion": "1.129",
			"offers": {
				"@type": "Offer",
				"price": "0",
				"priceCurrency": "USD"
			},
			"applicationCategory": "DeveloperApplication",
			"applicationSubCategory": "AI Code Editor",
			"description": "Visual Studio Code is a free, open source AI code editor for agent-first development. Build with AI agents, manage multi-agent workflows, and code across any environment.",
			"alternateName": "VS Code",
			"datePublished": "2021-11-03",
			"operatingSystem": "Mac, Linux, Windows",
			"logo": "https://code.visualstudio.com/assets/apple-touch-icon.png",
			"screenshot": "https://code.visualstudio.com/assets/images/product-screenshot.png",
			"releaseNotes": "https://code.visualstudio.com/updates",
			"downloadUrl": "https://code.visualstudio.com/download",
			"license": "https://code.visualstudio.com/license",
			"softwareRequirements": "https://code.visualstudio.com/docs/supporting/requirements",
			"url" : "https://code.visualstudio.com",
			"author": {
				"@type": "Organization",
				"name": "Microsoft"
			},
			"publisher": {
				"@type": "Organization",
				"name": "Microsoft"
			},
			"maintainer": {
				"@type": "Organization",
				"name": "Microsoft"
			},
			"potentialAction": {
				"@type": "SearchAction",
				"target": "https://code.visualstudio.com/Search?q={search_term_