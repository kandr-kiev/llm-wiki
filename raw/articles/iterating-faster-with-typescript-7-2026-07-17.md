---
source_url: https://code.visualstudio.com/blogs/2026/06/26/iterating-faster-with-ts-7
ingested: 2026-07-17
sha256: af70be8e1931716ed26b4fb49933aec4da4a16082ce78a43b22f51041d8d2d83
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

	<meta name="description" content="How the VS Code and TypeScript teams collaborated to adopt TypeScript 7 and speed up VS Code development" />
<meta name="keywords" content="" />
<!-- Twitter and Facebook OpenGraph Metadata-->
<meta name="twitter:card" content="summary_large_image" />
<meta property="og:url" content="https://code.visualstudio.com/blogs/2026/06/26/iterating-faster-with-ts-7" />
<meta property="og:type" content="article" />
<meta property="og:title" content="Iterating faster with TypeScript 7" />
<meta property="og:description" content="How the VS Code and TypeScript teams collaborated to adopt TypeScript 7 and speed up VS Code development" />

<meta property="og:image" content="https://code.visualstudio.com/assets/blogs/2026/06/26/ts-7.png" />



	<link rel="shortcut icon" href="/assets/favicon.ico" sizes="128x128" />
	<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">

	<title>Iterating faster with TypeScript 7</title>

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
            		
            			<li class="active">
            				<a href="/blogs/2026/06/26/iterating-faster-with-ts-7" aria-label="Current Page: Iterating faster with TypeScript 7">Iterating faster with TypeScript 7</a>
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
            		
            			<option value="/blogs/2026/07/06/optimizing-vscode-coding-harness-model-providers" >GPT-5.5 Prompt Tuning</option>
            		
            			<option value="/blogs/2026/06/26/iterating-faster-with-ts-7" selected>Iterating faster with TypeScript 7</option>
            		
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
                <h1>Iterating faster with TypeScript 7</h1>
<p>June 26, 2026 by VS Code Team, <a href="https://x.com/code" class="external-link" target="_blank">@code</a></p>
<p>VS Code and TypeScript practically grew up together. We made a bet early on to write VS Code in TypeScript, and we have always worked closely with the TypeScript team to provide great built-in TypeScript and JavaScript language support in VS Code. This post is about the next step of that journey: TypeScript 7, and how collaborating on adopting TypeScript 7 sped up our builds, improved the day-to-day editing loop for both developers and agents, and helped the TypeScript team ship a more tested release.</p>
<p>TypeScript 7 is a <a href="https://devblogs.microsoft.com/typescript/typescript-native-port/" class="external-link" target="_blank">complete port of the TypeScript compiler and language tooling in Go</a>. That means it's fast, more than 10x faster in many cases. VS Code had a lot to gain from those speedups, so we were naturally eager to adopt TypeScript 7 as soon as we could.</p>
<p>However, we also knew that this would take time. When we started this process in the summer of 2025, TypeScript 7 was actually already shockingly far along for a complete rewrite, but it still had type checking inconsistencies and lacked many features we needed. Even so, we wanted to start testing and providing feedback right away. Adopting TypeScript 7 while it was still being built may sound a little crazy, but it turned out to be a great decision for both VS Code and TypeScript.</p>
<h2 id="_an-incremental-migration" data-needslink="_an-incremental-migration">An incremental migration</h2>
<p>The VS Code team has never been afraid to take on large engineering efforts, whether that's enabling <a href="https://code.visualstudio.com/blogs/2019/05/23/strict-null">strict null checking in our codebase</a>, adding <a href="https://code.visualstudio.com/blogs/2019/05/02/remote-development">remote development support</a>, or addressing and preventing dangerous code patterns across thousands of files. A common theme across these efforts is that we try to take an incremental approach. This means breaking big, complex problems down into small steps. Those steps happen in the main codebase (no forks or long-lived branches), and each one usually brings a small improvement as it lands. Take enough little steps, and eventually you can look back and realize that you've quietly conquered that once seemingly insurmountable challenge.</p>
<p>We wanted to take the same approach to adopting TypeScript 7. For us, that meant gradually introducing TypeScript 7 into different parts of our workflows and codebases, starting with lower-impact, lower-risk areas before eventually moving on to the main areas of VS Code. There are many benefits to working incrementally, but two were especially important for this effort:</p>
<ul>
<li>
<p>Reduced risk. Each step of the adoption was relatively small, so if something went wrong, it was easy to identify the cause and revert.</p>
</li>
<li>
<p>Early feedback. We wanted to start testing and providing high-quality feedback to the TS team early in TS 7's development. That meant getting as much usage of TypeScript 7 as possible, but without negatively impacting developer productivity on the VS Code team.</p>
<p>This testing helped us find bugs and limitations that they could then prioritize fixing. And as we adopted TS 7 in more parts of our codebase, those areas also became informal regression tests for each new TypeScript 7 nightly release.</p>
</li>
</ul>
<p>In practice, that incremental philosophy unfolded as a series of phases over about six months. Each phase increased our use and testing of TypeScript 7 a little more, moving in step with TypeScript 7's own progress and helping shape it along the way. Here's how it played out:</p>
<p><strong>Exploration (summer and early fall 2025)</strong></p>
<p>TypeScript 7 was <a href="https://devblogs.microsoft.com/typescript/typescript-native-port/" class="external-link" target="_blank">publicly announced in March 2025</a>. By the summer, it was ready for initial testing, although at this point it still had known bugs and limitations.</p>
<p>Type checking was farther along than emit (the process of generating JavaScript output files), so most of our early testing focused on manually running the <a href="https://www.npmjs.com/package/@typescript/native-preview" class="external-link" target="_blank"><code>@typescript/native-preview</code> npm package</a> on some of our smaller extensions with <code>--noEmit</code>. We reported issues as we found them, and because the <code>native-preview</code> package was updated daily, we could test new changes and fixes quickly.</p>
<p>As part of TypeScript 7, the TypeScript team was also building up the new language server that would power VS Code's in-editor TypeScript and JavaScript support. This was shipped using the <a href="https://marketplace.visualstudio.com/items?itemName=TypeScriptTeam.native-preview" class="external-link" target="_blank">TypeScript native preview VS Code extension</a>, which replaces VS Code's built-in JavaScript and TypeScript IntelliSense with the new TypeScript 7 language server. We worked with the TypeScript team to make it easy to switch back and forth between the two TypeScript versions. That flexibility mattered because TypeScript 7 was still missing a number of basic language features at this point. We wanted developers to feel that they could try it out with as little effort and risk as possible.</p>
<p>We also made it easy to report TypeScript 7 issues directly from VS Code. Making reporting easy meant that developers would not think twice about filing even small annoyances. Those reports fed a steady stream of real world feedback for the TypeScript team.</p>
<p>At this stage, most testing was done by a small number of motivated VS Code team members who were interested in alpha testing and were OK working around some annoyances.</p>
<p><strong>The TS 6 bridge (fall 2025)</strong></p>
<p>Meanwhile the TypeScript team was thinking through how to ease the transition to TypeScript 7 instead of leaving users to make one big jump. Now it being 2025, this thinking was inexplicably accompanied by a bewildering hand gesture, with the result being the aptly named TypeScript 6.0:</p>
<blockquote><p>TypeScript 6.0 acts as the bridge between TypeScript 5.9 and 7. As such, most changes in TypeScript 6.0 are meant to help align and prepare for adopting TypeScript 7</p>
<p>— <a href="https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/" class="external-link" target="_blank">https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/</a></p>
</blockquote><p>Such a bridge was necessary because TypeScript 7 gave the team a chance to fix and modernize certain long-standing annoyances in TypeScript tooling. For example, older TypeScript releases defaulted to targeting ES5. That made sense in 2014, when ES6 (aka ECMAScript 2015) had not been finalized yet, but it felt wildly anachronistic in 2025. It was also a footgun for new developers who would end up accidentally generating larger, less efficient JavaScript files simply because they forgot to set <code>target</code>. Similarly, TypeScript 5 did not enable strict null checks by default, so many users were missing out on this truly game-changing feature just because they did not know they needed to enable it.</p>
<p>For us on the VS Code team, switching to TypeScript 6 was a small, low-risk step compared to the prospect of adopting an entirely rewritten TypeScript 7. It required only a few minor code changes. Still, this small step made us more confident that our codebase was in a good state and that once TypeScript 7 was ready, we'd be able to switch to it without many issues.</p>
<p><strong>TS 6 and 7 in parallel (fall 2025)</strong></p>
<p>Next it was time to start using TypeScript 7 in earnest. We started with the lowest-risk area: using TypeScript 7 to type check our built-in extensions. During this phase, we continued to run TypeScript 6 for full type checking and JavaScript generation (emit). We set up our continuous integration so that both TypeScript 6 and 7 builds needed to pass. Generally, the type checking between TypeScript 6 and 7 matched, but running both did help catch a few differences that we reported.</p>
<p>By this point, thanks to steady work from the TypeScript team, the language server in TypeScript 7 was also further along, so we added the TypeScript 7 extension as a dependency in the VS Code repo so that our developers could easily switch to it. Our goal was to gradually improve our editor support so that developers could spend more and more time using TypeScript 7. We prioritized anything that caused developers to switch back to TypeScript 6, whether that was a bug or missing functionality.</p>
<p>One of the most common initial reasons developers switched back to TypeScript 6 may be a bit surprising: code formatting. You can generally live with suggestions not being perfect and even with <code>Go to Definition</code> behaving inconsistently, but formatting differences between TypeScript 6 and 7 would cause our PR pre-commit checks and continuous integration formatting checks to fail. That gave even little formatting inconsistencies—such as extra whitespace—outsized priority. Over time, those formatting issues were ironed out and developers had to switch back to TypeScript 6 less and less.</p>
<p><strong>Adopting TypeScript 7 for most extensions (January and February 2026)</strong></p>
<p>By early 2026, TypeScript 7 had everything we needed to start using it fully. The TypeScript team had done truly amazing work making type checking trustworthy, finishing up emit, and improving the language tooling in the editor. It was time to start switching over to TypeScript 7 fully.</p>
<p>As always, we wanted to move carefully and incrementally, so we started migrating our built-in extensions one by one. These built-in extensions are fundamentally quite similar to a VS Code extension you can create using <code>yo code</code>. Before the switch, those extensions used the following build tools:</p>
<ul>
<li><code>tsc</code> (TypeScript 6) for type checking and development builds.</li>
<li><code>webpack</code> for production and web bundles.</li>
<li><code>esbuild</code> for fast emit.</li>
</ul>
<p>As part of the TypeScript 7 migration, we decided to simplify our builds by switching our bundling to use esbuild instead of webpack. This simplified our build tooling and significantly reduced the time it took to generate bundles.</p>
<p>Our new built setup was simpler:</p>
<ul>
<li><code>tsgo</code> (TypeScript 7) for type checking and development builds.</li>
<li><code>esbuild</code> for production and web bundles.</li>
</ul>
<p>We migrated the extensions in small groups to minimize the impact of any regressions. This also let us start with the simplest extensions, building up our knowledge and confidence before moving on to more complex extensions. This process generally went smoothly, which shouldn't be a huge surprise given that we had already been building this code using TypeScript 7.</p>
<p><strong>Adopting TypeScript 7 as the default (February 2026)</strong></p>
<p>The final move was to switch to TypeScript 7 for our normal development. By then, the TypeScript team's fixes had removed the blockers we had been working around, and because the incremental steps had already done most of the work, the code change for this was actually pretty minor. <a href="https://github.com/microsoft/vscode/commit/86da9175ebfa985451eb324d2f94152d867ae3af" class="external-link" target="_blank">Here's the change</a> that switches our normal watch task to use TypeScript 7, for example.</p>
<p>We also made TypeScript 7 the default version used in the editor for the VS Code repo. We still support switching back to the older TypeScript as an escape hatch, but it has rarely been needed in practice. Most developers are happy to stay on TypeScript 7 because of its significantly better performance.</p>
<h2 id="_the-numbers" data-needslink="_the-numbers">The numbers</h2>
<p>So, was it all worth it? The answer is a clear and resounding yes.</p>
<p>Here's a before-and-after comparison for type checking the main VS Code source code:</p>
<pre class="shiki" data-lang="text" shiki-themes dark-plus light-plus" style="--shiki-dark:#D4D4D4;--shiki-light:#000000;--shiki-dark-bg:#1E1E1E;--shiki-light-bg:#FFFFFF" tabindex="0"><code><span class="line"><span># TS 6.0</span></span>
<span class="line"><span>tsc --noEmit -p src/tsconfig.json</span></span>
<span class="line"><span>36 seconds</span></span>
<span class="line"><span></span></span>
<span class="line"><span># TS 7</span></span>
<span class="line"><span>tsgo --noEmit -p src/tsconfig.json</span></span>
<span class="line"><span>5 seconds</span></span>
<span class="line"><span></span></span></code></pre>
<p>TypeScript 7 is more than seven times faster! That's especially impressive when you consider that these two tasks are doing the same work: they type check the same files with the same level of thoroughness and report the same errors. Just by switching from TypeScript 6 to TypeScript 7, we sped up our type checking by 7x.</p>
<p>With TypeScript 7, we can also now type check almost all of our built-in extensions in well under a second. The only exception is our larger Copilot extension, and that still only takes 2.5 seconds.</p>
<p>The results get even more impressive when we look at compiling and type checking all of VS Code, i.e. both our main source code and our roughly fifty built-in extension <code>tsconfig</code> projects. This is what the <code>npm run watch</code> command does, and it is also the command that developers working on VS Code typically run.</p>
<p>With TypeScript 6, <code>npm run watch</code> takes around 80 seconds to complete. After migrating to TypeScript 7, we dropped this time to just over 20 seconds: roughly four times faster. That's a whole minute saved in normal development and agent-assisted iteration every time a build needs to be restarted (re-checks after the initial watch completes are around a second at most).</p>
<p>Those improvements also translate into better language tooling performance in the editor. For TypeScript language features in the editor, we need to load the whole <code>tsconfig</code> project before we can provide proper errors and complex features like auto imports. For the main VS Code project, that used to take close to a minute. Now it's around 10 seconds. That's roughly 50 seconds saved. With VS Code developers often reloading their editor windows multiple times per day, those saved seconds really add up. No more quick coffee runs while the editor tools are loading.</p>
<p>Seeing these numbers really puts the scale of the improvements in perspective. It was easy to lose track of the total impact because our incremental approach meant that many improvements arrived gradually instead of in one big PR. Early steps might only have saved a second here or a few hundred milliseconds there. By the end, however, those small wins had added up into something significant. It's amazing to see how the TypeScript team delivered on their initial promise too: it's full TypeScript, just way faster.</p>
<h2 id="_better-through-collaboration" data-needslink="_better-through-collaboration">Better through collaboration</h2>
<p>Adopting TypeScript 7 has been a big win for developers working on VS Code, but there's another result of this effort that is less tangible and perhaps even more impactful. VS Code's large, complex codebase turned out to be an excellent way to find real-world bugs in TypeScript 7 and polish its editor tooling.</p>
<p>The developers on the VS Code team also were not afraid to provide feedback about missing features or when something just did not feel right. Every time a developer hit a rough edge and switched back to TypeScript 6, it was a signal for the TypeScript team to decide what to fix next. The result is a more tested and polished version of TypeScript 7, one that we know works well beyond the VS Code codebase.</p>
<p>Although we've focused on the VS Code side of the story in this post, the TypeScript team really deserves almost all of the credit. They were the ones building TypeScript 7 after all, while also responding to all the feedback from those pesky VS Code devs. From myself and the rest of the VS Code team, thank you!</p>
<p>TypeScript 7 is an exciting step forward for the language. Whether you're editing code in VS Code, kicking off compiles on the command line, or asking an agent to iterate on a project, the performance improvements are significant and noticeable. Thanks to the work of the TypeScript team and the testing and feedback process outlined here, switching to TypeScript 7 should be a relatively smooth process and an easy win for many codebases.</p>
<p>More than anything though, I hope this post shows the value of working incrementally, testing early and often, and building tight feedback loops for close collaboration. These are values VS Code has always held, and they continued to serve us well again on this effort. I hope that this story motivates you to think differently about how you can tackle large engineering efforts in your own projects and ultimately ship better code.</p>
<p>Happy coding! 💙</p>

            </main>
            
            <!-- Right sidebar - On This Page -->
            <aside class="docs-right-sidebar hidden-xs">
                <nav id="docs-subnavbar" aria-labelledby="docs-subnavbar-label">
                    
                    <h4 id="docs-subnavbar-label"><span class="sr-only">On this page there are 3 sections</span><span
                            aria-hidden="true">On this page</span></h4>
                    <ul class="nav">
                        
                        <li><a href="#_an-incremental-migration">An incremental migration</a></li>
                        
                        <li><a href="#_the-numbers">The numbers</a></li>
                        
                        <li><a href="#_better-through-collaboration">Better through collaboration</a></li>
                        
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