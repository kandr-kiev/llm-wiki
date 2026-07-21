---
source_url: https://code.visualstudio.com/blogs/2026/06/18/byok-vscode
ingested: 2026-07-17
sha256: 5de6de76b7575baf33271bc8023e21a5e8b14566263b598beb22ffc4aa592308
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

	<meta name="description" content="Learn how to use bring your own key (BYOK) in VS Code to add models from providers like Azure, Anthropic, Gemini, OpenAI, Huggingface, OpenRouter, or use a local model with Ollama, Foundry Local, and more." />
<meta name="keywords" content="" />
<!-- Twitter and Facebook OpenGraph Metadata-->
<meta name="twitter:card" content="summary_large_image" />
<meta property="og:url" content="https://code.visualstudio.com/blogs/2026/06/18/byok-vscode" />
<meta property="og:type" content="article" />
<meta property="og:title" content="Use your own language model key in VS Code" />
<meta property="og:description" content="Learn how to use bring your own key (BYOK) in VS Code to add models from providers like Azure, Anthropic, Gemini, OpenAI, Huggingface, OpenRouter, or use a local model with Ollama, Foundry Local, and more." />

<meta property="og:image" content="https://code.visualstudio.com/assets/blogs/2026/06/18/language-models-editor.png" />



	<link rel="shortcut icon" href="/assets/favicon.ico" sizes="128x128" />
	<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">

	<title>Use your own language model key in VS Code</title>

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
            		
            			<li >
            				<a href="/blogs/2026/06/19/what-50000-runs-taught-us" >50,000 Runs, One Eval</a>
            			</li>
            		
            			<li class="active">
            				<a href="/blogs/2026/06/18/byok-vscode" aria-label="Current Page: Bring Your Own Key">Bring Your Own Key</a>
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
            		
            			<option value="/blogs/2026/06/19/what-50000-runs-taught-us" >50,000 Runs, One Eval</option>
            		
            			<option value="/blogs/2026/06/18/byok-vscode" selected>Bring Your Own Key</option>
            		
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
                <h1>Use your own language model key in VS Code</h1>
<p>June 18, 2026 by <a href="https://github.com/cinnamon-msft" class="external-link" target="_blank">Kayla Cinnamon</a></p>
<p>At Microsoft Build this year, I had the opportunity to present in the opening keynote. One thing I showed was using local models inside VS Code on the new Surface RTX Spark Dev Box. My model was periodically analyzing my log files and giving me summaries, so I could easily diagnose issues without having to look through the logs myself. Check out the <a href="https://build.microsoft.com/sessions/KEY01" class="external-link" target="_blank">recording at 12:18</a>.</p>
<p>Using local models gives you even greater flexibility when working with agents. Sometimes you want the built-in models available through GitHub Copilot. Sometimes you want to try a new model from a provider your team already uses. Sometimes you want to experiment locally. VS Code allows you to do all of these workflows with bring your own language model key (BYOK) and bring your own local model.</p>
<p>With BYOK in VS Code, you can add models from providers like Azure, Anthropic, Huggingface, Gemini, OpenAI, OpenRouter, or you can run a model locally with Ollama, Foundry Local, and more, then use them directly from the Chat model picker.</p>
<p><img src="/assets/blogs/2026/06/18/model-dropdown-change-model-v2.png" alt="Screenshot of the VS Code Chat model picker showing available language models." loading="lazy"></p>
<h2 id="_what-is-byok" data-needslink="_what-is-byok">What is BYOK?</h2>
<p>BYOK lets you use a language model from a supported provider by adding your own API key or endpoint configuration in VS Code. Once configured, those models appear in the same Chat model picker you already use for Copilot. Support is built in for several providers and VS Code is extensible, so any model provider can enable support through an extension.</p>
<p>This gives you more choice for chat and agent workflows. For example, you can:</p>
<ul>
<li>Try models that are not built into VS Code.</li>
<li>Use a provider your organization already has billing or governance set up for.</li>
<li>Connect to local models through providers such as Ollama or Foundry Local.</li>
<li>Pick different models for different tasks, such as quick Q&amp;A, planning, or multi-step agent work.</li>
</ul>
<p>The goal is to allow you to choose the right model and keep working.</p>
<h2 id="_what-byok-works-with" data-needslink="_what-byok-works-with">What BYOK works with</h2>
<p>BYOK models are available for VS Code chat experiences, including agent workflows when the selected model supports the required capabilities.</p>
<p>There are a few important details to keep in mind:</p>
<ul>
<li>BYOK models work <strong>without</strong> signing into a GitHub account and <strong>without</strong> a Copilot plan. You can add and use models entirely with your own API keys, including fully <strong>offline scenarios with local models</strong>.</li>
<li>BYOK applies to chat and utility tasks, not standard code completions.</li>
<li>Some AI features, such as semantic search, inline suggestions, and features that rely on embeddings, still require a GitHub account or Copilot support.</li>
<li>Usage for provider-backed BYOK models is billed directly by that provider and does not count against GitHub Copilot request quotas.</li>
<li>For Copilot Business and Enterprise, organization administrators can control BYOK availability through Copilot policy settings.</li>
</ul>
<p>In other words, BYOK expands model choice in VS Code Chat, but it does not replace every Copilot-powered feature in the editor.</p>
<h2 id="_getting-started-with-byok" data-needslink="_getting-started-with-byok">Getting started with BYOK</h2>
<p>The easiest way to get started is through the <strong>Language Models</strong> editor.</p>
<p>You can open it from the Chat model picker by selecting the <strong>Manage Language Models</strong> gear icon, or you can run <strong>Chat: Manage Language Models</strong> from the Command Palette.</p>
<p><img src="/assets/blogs/2026/06/18/language-models-editor.png" alt="Screenshot of the Language Models editor in VS Code." loading="lazy"></p>
<p>The Language Models editor shows the models available to you, grouped by provider. It also shows useful details like model capabilities, context size, billing information, and whether a model is visible in the picker.</p>
<p>This is also where you can keep the model picker focused. If you are testing several providers, you can hide models you do not use often and keep your day-to-day models easy to find.</p>
<h2 id="_adding-models-from-a-built-in-provider" data-needslink="_adding-models-from-a-built-in-provider">Adding models from a built-in provider</h2>
<p>If the provider you want is built into VS Code, setup is a few clicks.</p>
<ol>
<li>Open <strong>Chat: Manage Language Models</strong>.</li>
<li>Select <strong>Add Models</strong>.</li>
<li>Choose a provider.</li>
<li>Enter a group name for the models. This is the label shown in the model picker and Language Models editor.</li>
<li>Enter the provider details, such as an API key, endpoint, deployment name, or other required configuration.</li>
<li>Select the model from the Chat model picker.</li>
</ol>
<p><img src="/assets/blogs/2026/06/18/model-provider-quick-pick-v2.png" alt="Screenshot of the model provider picker in VS Code." loading="lazy"></p>
<p>Depending on the provider, VS Code might open a <code>chatLanguageModels.json</code> file so you can finish configuring model details.</p>
<p>For example, a Mistral configuration specifies the endpoint URL, API type, and model capabilities:</p>
<pre class="shiki" data-lang="json" shiki-themes dark-plus light-plus" style="--shiki-dark:#D4D4D4;--shiki-light:#000000;--shiki-dark-bg:#1E1E1E;--shiki-light-bg:#FFFFFF" tabindex="0"><code><span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">[</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">  {</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">    "name"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"Mistral"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">,</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">    "vendor"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"customendpoint"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">,</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">    "apiKey"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"&#x3C;your-mistral-api-key>"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">,</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">    "apiType"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"chat-completions"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">,</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">    "models"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: [</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">      {</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">        "id"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"mistral-medium-latest"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">,</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">        "name"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"mistral medium"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">,</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">        "url"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"https://api.mistral.ai/v1/chat/completions"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">,</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">        "toolCalling"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#569CD6;--shiki-light:#0000FF">true</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">,</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">        "vision"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#569CD6;--shiki-light:#0000FF">true</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">,</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">        "maxInputTokens"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#B5CEA8;--shiki-light:#098658">256000</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">,</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">        "maxOutputTokens"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#B5CEA8;--shiki-light:#098658">16000</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">      }</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">    ]</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">  }</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">]</span></span>
<span class="line"></span></code></pre>
<p>The exact fields depend on the provider and model. The important part is that after the provider is configured, the model becomes available from the same picker you use for the rest of Chat. For more information, check out the <a href="https://code.visualstudio.com/docs/agent-customization/language-models#_add-a-model-from-a-built-in-provider">Language Model docs</a>.</p>
<h2 id="_adding-models-from-extensions" data-needslink="_adding-models-from-extensions">Adding models from extensions</h2>
<p>VS Code also supports language model provider extensions. These extensions can contribute models directly into the Language Models editor and Chat model picker.</p>
<p>To find provider extensions:</p>
<ol>
<li>Open the Extensions view.</li>
<li>Search for <code>@tag:language-models</code>.</li>
<li>Install the provider extension you want to use.</li>
<li>Follow the extension's setup instructions.</li>
<li>Select the model from the Chat model picker.</li>
</ol>
<p><img src="/assets/blogs/2026/06/18/language-models-extensions.png" alt="Screenshot of the Extensions view listing extensions that provide language models." loading="lazy"></p>
<p>This extensibility is a big part of the BYOK story. Instead of every provider needing to be hard-coded into VS Code, extensions can bring new model providers into the editor as the ecosystem evolves.</p>
<h2 id="_leveraging-utility-models" data-needslink="_leveraging-utility-models">Leveraging utility models</h2>
<p>VS Code also uses lightweight models in the background for small tasks like generating chat titles, commit messages, and rename suggestions. These default to built-in Copilot models and most users won't need to touch them. But if you're using BYOK without signing into a GitHub account, those defaults aren't available. VS Code will show a notification in the Chat view prompting you to configure them. Set <span class="setting"><span class="setting-dropdown" data-setting-id="chat.utilityModel">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      chat.utilityModel
    </span>
    <button 
      type="button"
      class="setting-dropdown-trigger"
      aria-haspopup="menu"
      aria-expanded="false"
      
      aria-label="Open setting in VS Code">
        <svg class="setting-dropdown-chevron" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path d="M7.976 10.072l4.357-4.357.62.618L8.284 11h-.618L3 6.333l.619-.618 4.357 4.357z"/>
        </svg>
    </button>
    <span class="setting-dropdown-menu" role="menu" aria-label="Open setting">
      <span role="menuitem" class="setting-action-item" data-version="stable" tabindex="0">Open in VS Code</span>
      <span role="menuitem" class="setting-action-item" data-version="insiders" tabindex="-1">Open in VS Code Insiders</span>
    </span>
  </span></span> and <span class="setting"><span class="setting-dropdown" data-setting-id="chat.utilitySmallModel">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      chat.utilitySmallModel
    </span>
    <button 
      type="button"
      class="setting-dropdown-trigger"
      aria-haspopup="menu"
      aria-expanded="false"
      
      aria-label="Open setting in VS Code">
        <svg class="setting-dropdown-chevron" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path d="M7.976 10.072l4.357-4.357.62.618L8.284 11h-.618L3 6.333l.619-.618 4.357 4.357z"/>
        </svg>
    </button>
    <span class="setting-dropdown-menu" role="menu" aria-label="Open setting">
      <span role="menuitem" class="setting-action-item" data-version="stable" tabindex="0">Open in VS Code</span>
      <span role="menuitem" class="setting-action-item" data-version="insiders" tabindex="-1">Open in VS Code Insiders</span>
    </span>
  </span></span> to one of your BYOK models to keep those features working. A fast, inexpensive model works well here.</p>
<p><img src="/assets/blogs/2026/06/18/chat-utility-model.png" alt="Screenshot of the setting for configuring the Chat Utility Model." loading="lazy"></p>
<h2 id="_choosing-the-right-model" data-needslink="_choosing-the-right-model">Choosing the right model</h2>
<p>One of the best parts of BYOK is that you do not have to use one model for everything.</p>
<p>For everyday work, you might choose:</p>
<ul>
<li>A fast model for quick questions, summaries, and small edits.</li>
<li>A reasoning model for planning, debugging, or complex refactors.</li>
<li>A local model when you want to experiment offline.</li>
<li>A provider-specific model when your team already has workflows around that provider.</li>
</ul>
<p>Simply choose which model you want to use in the model picker below the Chat box.</p>
<p><img src="/assets/blogs/2026/06/18/model-dropdown-change-model-v2.png" alt="Screenshot of the VS Code Chat model picker showing available language models." loading="lazy"></p>
<h2 id="_try-it-out" data-needslink="_try-it-out">Try it out</h2>
<p>BYOK gives you more flexibility in VS Code without adding more tools to your workflow. You can keep using the built-in Copilot models, add models from providers you already use, experiment with local models, and choose the right model for each task from one place.</p>
<p>To learn more, check out the VS Code docs on <a href="https://code.visualstudio.com/docs/agent-customization/language-models">AI language models</a>, the VS Code blog post on <a href="https://code.visualstudio.com/blogs/2025/10/22/bring-your-own-key">Expanding Model Choice in VS Code with Bring Your Own Key</a>, and the GitHub changelog entry for <a href="https://github.blog/changelog/2026-04-22-bring-your-own-language-model-key-in-vs-code-now-available/" class="external-link" target="_blank">BYOK availability in VS Code</a>.</p>
<p>We also have a video for how to <a href="https://www.youtube.com/watch?v=EB7dQv1ALCU" class="external-link" target="_blank">Bring Your Own AI... No Sign-In Required!</a>.</p>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/EB7dQv1ALCU?si=mDo0BJiZ5FLJBPwJ" title="Bring Your Own AI... No Sign-In Required!" frameborder="0" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<p>We are continuing to improve model choice in VS Code, and your feedback helps shape what comes next. Try BYOK with your workflow and let us know what you think in the <a href="https://github.com/microsoft/vscode" class="external-link" target="_blank">VS Code repository</a>.</p>
<p>Happy coding! 💙</p>

            </main>
            
            <!-- Right sidebar - On This Page -->
            <aside class="docs-right-sidebar hidden-xs">
                <nav id="docs-subnavbar" aria-labelledby="docs-subnavbar-label">
                    
                    <h4 id="docs-subnavbar-label"><span class="sr-only">On this page there are 8 sections</span><span
                            aria-hidden="true">On this page</span></h4>
                    <ul class="nav">
                        
                        <li><a href="#_what-is-byok">What is BYOK?</a></li>
                        
                        <li><a href="#_what-byok-works-with">What BYOK works with</a></li>
                        
                        <li><a href="#_getting-started-with-byok">Getting started with BYOK</a></li>
                        
                        <li><a href="#_adding-models-from-a-built-in-provider">Adding models from a built-in provider</a></li>
                        
                        <li><a href="#_adding-models-from-extensions">Adding models from extensions</a></li>
                        
                        <li><a href="#_leveraging-utility-models">Leveraging utility models</a></li>
                        
                        <li><a href="#_choosing-the-right-model">Choosing the right model</a></li>
                        
                        <li><a href="#_try-it-out">Try it out</a></li>
                        
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
				"target": "https://code.visualstudio.com/Search?q={search_term_string}",
				"query-input": "required name=search_term_string"
			},
			"sameAs" : [
				"https://en.wikipedia.org/wiki/Visual_Studio_Code",
				"https://twitter.com/code",
				"https://www.youtube.com/code",
				"https://www.tiktok.com/@vscode",
				"https://github.com/microsoft/vscode"
			]
		}
	</script>
</body>

</html>