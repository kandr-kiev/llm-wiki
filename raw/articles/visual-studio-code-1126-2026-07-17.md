---
source_url: https://code.visualstudio.com/updates/v1_126
ingested: 2026-07-17
sha256: 6c07f496760bfa0340a6dd87976bf16c2644f5eb29fa1dad624e7c6b5f2fb1c9
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

	<meta name="description" content="Learn what is new in Visual Studio Code 1.126" />
<meta name="keywords" content="" />
<!-- Twitter and Facebook OpenGraph Metadata-->
<meta name="twitter:card" content="summary_large_image" />
<meta property="og:url" content="https://code.visualstudio.com/updates/v1_126" />
<meta property="og:type" content="article" />
<meta property="og:title" content="Visual Studio Code 1.126" />
<meta property="og:description" content="Learn what is new in Visual Studio Code 1.126" />

<meta property="og:image" content="https://code.visualstudio.com/assets/updates/1_126/release-highlights.webp" />



	<link rel="shortcut icon" href="/assets/favicon.ico" sizes="128x128" />
	<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">

	<title>Visual Studio Code 1.126</title>

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
								<li class="active" ><a id="nav-updates" href="/updates" data-m='{"cN":"Release Notes"}'>Release Notes</a>
								</li>
								<li ><a id="nav-blogs" href="/blogs" data-m='{"cN":"Blog"}'>Blog</a></li>
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
			<div class="body-content docs docs-github-layout release-notes">
    <div class="docs-layout-wrapper">
        <!-- Left sidebar - Table of Contents -->
        <aside class="docs-left-sidebar">
            <nav id="docs-navbar" aria-label="Updates" class="docs-nav updates-nav visible-md visible-lg">
            	<h4>Updates</h4>
            	<ul class="nav">
            		
            			<li >
            				<a href="/updates/v1_130" >Insiders</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_129" >1.129</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_128" >1.128</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_127" >1.127</a>
            			</li>
            		
            			<li class="active">
            				<a href="/updates/v1_126" aria-label="Current Page: 1.126">1.126</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_125" >1.125</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_124" >1.124</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_123" >1.123</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_122" >1.122</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_121" >1.121</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_120" >1.120</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_119" >1.119</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_118" >1.118</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_117" >1.117</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_116" >1.116</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_115" >1.115</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_114" >1.114</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_113" >1.113</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_112" >1.112</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_111" >1.111</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_110" >February 2026</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_109" >January 2026</a>
            			</li>
            		
            		<li >
            			<a href="/updates/archive" class="archive-link" >View All Releases</a>
            		</li>
            	</ul>
            </nav>
            <nav id="small-nav" aria-label="Updates" class="docs-nav updates-nav hidden-md hidden-lg">
            	<label class="faux-h4" for="small-nav-dropdown">Updates</label>
            	<select id="small-nav-dropdown" aria-label="updates">
            		
            			<option value="/updates/v1_130" >Insiders</option>
            		
            			<option value="/updates/v1_129" >1.129</option>
            		
            			<option value="/updates/v1_128" >1.128</option>
            		
            			<option value="/updates/v1_127" >1.127</option>
            		
            			<option value="/updates/v1_126" selected>1.126</option>
            		
            			<option value="/updates/v1_125" >1.125</option>
            		
            			<option value="/updates/v1_124" >1.124</option>
            		
            			<option value="/updates/v1_123" >1.123</option>
            		
            			<option value="/updates/v1_122" >1.122</option>
            		
            			<option value="/updates/v1_121" >1.121</option>
            		
            			<option value="/updates/v1_120" >1.120</option>
            		
            			<option value="/updates/v1_119" >1.119</option>
            		
            			<option value="/updates/v1_118" >1.118</option>
            		
            			<option value="/updates/v1_117" >1.117</option>
            		
            			<option value="/updates/v1_116" >1.116</option>
            		
            			<option value="/updates/v1_115" >1.115</option>
            		
            			<option value="/updates/v1_114" >1.114</option>
            		
            			<option value="/updates/v1_113" >1.113</option>
            		
            			<option value="/updates/v1_112" >1.112</option>
            		
            			<option value="/updates/v1_111" >1.111</option>
            		
            			<option value="/updates/v1_110" >February 2026</option>
            		
            			<option value="/updates/v1_109" >January 2026</option>
            		
            		<option value="/updates/archive" >View All Releases</option>
            	</select>
            </nav>        </aside>
        
        <!-- Content wrapper contains main content + right sidebar -->
        <div class="docs-content-wrapper">
            <!-- Main article content -->
            <main class="docs-main-content body">
                <h1>Visual Studio Code 1.126</h1>
<p>Follow us on <a href="https://www.linkedin.com/showcase/vs-code" class="external-link" target="_blank">LinkedIn</a>, <a href="https://go.microsoft.com/fwlink/?LinkID=533687" class="external-link" target="_blank">X</a>, <a href="https://bsky.app/profile/vscode.dev" class="external-link" target="_blank">Bluesky</a></p>
<hr>
<p><em>Release date: June 24, 2026</em></p>
<p>Downloads: Windows: <a href="https://update.code.visualstudio.com/1.126.0/win32-x64-user/stable">x64</a> <a href="https://update.code.visualstudio.com/1.126.0/win32-arm64-user/stable">Arm64</a> | Mac: <a href="https://update.code.visualstudio.com/1.126.0/darwin-universal-dmg/stable">Universal</a> <a href="https://update.code.visualstudio.com/1.126.0/darwin-x64-dmg/stable">Intel</a> <a href="https://update.code.visualstudio.com/1.126.0/darwin-arm64-dmg/stable">silicon</a> | Linux: <a href="https://update.code.visualstudio.com/1.126.0/linux-deb-x64/stable">deb</a> <a href="https://update.code.visualstudio.com/1.126.0/linux-rpm-x64/stable">rpm</a> <a href="https://update.code.visualstudio.com/1.126.0/linux-x64/stable">tarball</a> <a href="https://code.visualstudio.com/docs/supporting/faq#_previous-release-versions">Arm</a> <a href="https://update.code.visualstudio.com/1.126.0/linux-snap-x64/stable">snap</a></p>
<hr>
<p>Welcome to the 1.126 release of Visual Studio Code. This release brings clearer cost transparency, simpler model tuning, and safer browsing of unfamiliar code.</p>
<ul>
<li>
<p><a href="#_session-level-cost-information">Session-level cost</a>: See the total cost of a chat session to spot expensive conversations.</p>
</li>
<li>
<p><a href="#_multiple-chats-in-an-agent-host-copilot-session">Multiple chats per session</a>: Run several chats side by side in one agent host Copilot session.</p>
</li>
<li>
<p><a href="#_open-new-folders-in-restricted-mode">Workspace trust</a>: Browse new folders safely in restricted mode.</p>
</li>
</ul>
<p>Happy Coding!</p>
<hr>
<p>VS Code is rolling out gradually to all users. Use <strong>Check for Updates</strong> in VS Code to get the latest version immediately.</p>
<p>To try new features as soon as possible, <a href="https://code.visualstudio.com/insiders"><strong>download the nightly Insiders build</strong></a>, which includes the latest updates as soon as they are available.</p>
<hr>
<!-- TOC
<div class="toc-nav-layout">
  <nav id="toc-nav">
    <div>In this update</div>
    <ul>
      <li><a href="#cost-management">Cost management</a></li>
      <li><a href="#language-models">Language models</a></li>
      <li><a href="#agents-window-preview">Agents window</a></li>
      <li><a href="#editor-experience">Editor experience</a></li>
      <li><a href="#engineering">Engineering</a></li>
      <li><a href="#website">Website</a></li>
      <li><a href="#deprecated-features-and-settings">Deprecated features and settings</a></li>
      <li><a href="#thank-you">Thank you</a></li>
    </ul>
  </nav>
  <div class="notes-main">
Navigation End -->
<h2 id="_cost-management" data-needslink="_cost-management">Cost management</h2>
<h3 id="_session-level-cost-information" data-needslink="_session-level-cost-information">Session-level cost information</h3>
<p>You can now see the cost for an entire chat session, not just for individual turns. This gives you better transparency into which sessions consume the most credits, making it easier to spot expensive conversations and manage your usage over time.</p>
<p><img src="/assets/updates/1_126/session-token-usage.webp" alt="Screenshot showing the session info popover with session cost in credits and context window token usage for the whole chat session." width="500" height="372" loading="lazy"></p>
<h2 id="_language-models" data-needslink="_language-models">Language models</h2>
<h3 id="_unified-model-customization-picker" data-needslink="_unified-model-customization-picker">Unified model customization picker</h3>
<p>To simplify language model configuration, we have combined the context size and reasoning (thinking) effort controls into a single model customization picker. From one place, you can adjust both settings when tuning a model, instead of working with two separate dropdowns.</p>
<p><img src="/assets/updates/1_126/model-customization-picker.webp" alt="Screenshot showing the model customization picker with combined context size and reasoning effort controls." width="500" height="468" loading="lazy"></p>
<h3 id="_simplified-model-hover" data-needslink="_simplified-model-hover">Simplified model hover</h3>
<p>We cleaned up the model hover to make it easier to scan. It now shows a concise one-word descriptor of the model's capabilities and includes deep link buttons that take you directly to the relevant configuration.</p>
<p><img src="/assets/updates/1_126/model-hover.webp" alt="Screenshot showing the simplified model hover with a one-word capability descriptor and deep link configuration buttons." width="500" height="426" loading="lazy"></p>
<h2 id="_agents-window-preview" data-needslink="_agents-window-preview">Agents window (Preview)</h2>
<p>The <a href="https://aka.ms/VSCode/Agents/docs" class="external-link" target="_blank">Agents window</a> is a dedicated companion window optimized for exploring, iterating on, and reviewing agent sessions across projects and machines.</p>
<h3 id="_multiple-chats-in-an-agent-host-copilot-session" data-needslink="_multiple-chats-in-an-agent-host-copilot-session">Multiple chats in an agent host Copilot session</h3>
<blockquote><p><strong>Applies to</strong>: Copilot sessions running on an <a href="#_agent-host-protocol-ahp">agent host</a>.</p>
</blockquote><p>The Agents window lets you run and manage multiple agent sessions side by side. In this release, a Copilot session started from an agent host can hold several chats at once. Because the chats share the same session and working context, you can keep more than one conversation going in the same workspace at the same time.</p>
<p>Say your primary chat is busy implementing a feature. Instead of waiting or interrupting it, select <strong>New Chat</strong> (<code>+</code>) in the session toolbar to open a second chat in the same session, then use it to review the changes so far, draft tests, or write the documentation. Both run at once, and each chat keeps its own conversation. You can switch between tabs and pick up right where you left off.</p>
<p>Chats are persisted and restored across a window reload. Step away and come back to every conversation in the session, not just the first one.</p>
<p>You can rename a chat directly in its tab to keep track of what each one is for, just like renaming a session from the session header:</p>
<ul>
<li><strong>Double-click</strong> a tab, or select <strong>Rename</strong> from its context menu, to edit the title in place.</li>
<li>Press <strong>Enter</strong> to commit the rename, or <strong>Escape</strong> to cancel. Selecting another tab while editing also cancels the edit and switches to that tab.</li>
</ul>
<p>A chat's title is independent of the session title, so renaming the session does not overwrite a chat you renamed.</p>
<p><video src="/assets/updates/1_126/multi-chat-sessions.mp4" title="Video showing multiple chats running in a single agent host Copilot session, with new chats added from the session toolbar and switching between chat tabs." autoplay loop controls muted></video></p>
<h3 id="_agentic-code-feedback-with-agent-host-harnesses" data-needslink="_agentic-code-feedback-with-agent-host-harnesses">Agentic code feedback with agent host harnesses</h3>
<p>In the Agents window, comments you leave on generated code are now stored on the agent host, so the agent can interact with your feedback by using server-side tools such as <code>listComments</code> and <code>resolveComments</code>. This works even when you disconnect the client, since the comments live on the server rather than in your local session.</p>
<p>The agent can also create the comments for you by using the <code>addComment</code> tool. When you run a review skill such as <code>/code-review</code>, it reviews your code and adds comments inline, which you can then accept or delete before submitting them to an agent to address.</p>
<p>Pull request review comments work the same way. You can accept the PR review comments and submit them to the agent, or ask the agent to resolve all PR comments. When you ask the agent to resolve PR comments that you haven't accepted yet, it first requests your permission to view them, and once you grant access, it addresses the PR review items.</p>
<h2 id="_editor-experience" data-needslink="_editor-experience">Editor experience</h2>
<h3 id="_open-new-folders-in-restricted-mode" data-needslink="_open-new-folders-in-restricted-mode">Open new folders in Restricted Mode</h3>
<p><strong>Setting</strong>: <span class="setting"><span class="setting-dropdown" data-setting-id="security.workspace.trust.startupPrompt">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      security.workspace.trust.startupPrompt
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
  </span></span></p>
<p><a href="https://code.visualstudio.com/docs/editing/workspaces/workspace-trust">Workspace Trust</a> lets you decide whether your project folders can automatically run code, which adds a layer of security when you work with unfamiliar code.</p>
<p>Previously, opening a new folder immediately interrupted you with a dialog asking whether to trust the folder before you could look at its contents. Now, new folders open in <a href="https://code.visualstudio.com/docs/editing/workspaces/workspace-trust#_restricted-mode">Restricted Mode</a> and only show the trust banner. This lets you browse the code safely first and trust the folder when you're ready.</p>
<p><img src="/assets/updates/1_126/restricted-mode-banner.webp" alt="Screenshot showing the Restricted Mode banner that appears when a new folder opens, with a message that Restricted Mode is intended for safe code browsing and links to trust the folder." width="1800" height="253" loading="lazy"></p>
<p>This changes the default value of the <span class="setting"><span class="setting-dropdown" data-setting-id="security.workspace.trust.startupPrompt">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      security.workspace.trust.startupPrompt
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
  </span></span> setting from <code>once</code> to <code>never</code>. To restore the previous behavior and be prompted the first time you open a folder, set the value back to <code>once</code>.</p>
<h3 id="_removed-trust-parent-from-the-workspace-trust-editor" data-needslink="_removed-trust-parent-from-the-workspace-trust-editor">Removed trust parent from the Workspace Trust editor</h3>
<p>The Workspace Trust editor previously showed a <strong>Trust Parent</strong> button next to the <strong>Trust</strong> button. Because it looked just like <strong>Trust</strong> but trusted the entire parent folder, it was easy to select by mistake and trust more folders than you intended.</p>
<p>To reduce that risk, the <strong>Trust Parent</strong> button is removed. You can still trust a parent folder by adding its path to the <strong>Trusted Folders &amp; Workspaces</strong> list in the Workspace Trust editor.</p>
<p><img src="/assets/updates/1_126/trust-parent-button.webp" alt="Screenshot showing the Workspace Trust editor with a single Trust button after the Trust Parent button was removed." width="1200" height="709" loading="lazy"></p>
<h2 id="_engineering" data-needslink="_engineering">Engineering</h2>
<h3 id="_agent-host-protocol-ahp" data-needslink="_agent-host-protocol-ahp">Agent Host Protocol (AHP)</h3>
<p>As part of rearchitecting how agent sessions work in VS Code, we are adopting the <a href="https://microsoft.github.io/agent-host-protocol/" class="external-link" target="_blank">Agent Host Protocol</a> (AHP). AHP lets us connect and render the same agent session from multiple clients and VS Code windows at the same time.</p>
<p>This unlocks scenarios like seeing the same session in both a regular VS Code window and the Agents window. The work is ongoing, but you can already try it out in VS Code Insiders and we would welcome <a href="https://github.com/microsoft/vscode/issues" class="external-link" target="_blank">your feedback</a>.</p>
<h2 id="_website" data-needslink="_website">Website</h2>
<h3 id="_vs-code-blog" data-needslink="_vs-code-blog">VS Code blog</h3>
<p>As the team has been writing more and more blog posts, in quick succession, we realized that our blogs section could use some love. Previously, when you open the blog section, you were directly taken to the last blog post, leaving previous posts often overlooked. We have now added a <a href="https://code.visualstudio.com/blogs">blog landing page</a> that highlights the several recent posts.</p>
<p><img src="/assets/updates/1_126/blog-landing-page.webp" alt="Screenshot showing the new blog landing page with a list of recent blog posts and a link to the blog archive." width="1727" height="1372" loading="lazy"></p>
<p>And if you are looking for the full list of all blog posts, you can now find it in the <a href="https://code.visualstudio.com/blogs/archive">blog archive</a>.</p>
<h3 id="_vs-code-documentation" data-needslink="_vs-code-documentation">VS Code documentation</h3>
<p>We've restructured our documentation table of contents to make it more scannable and easier to navigate. All our agentic documentation is now grouped under a single &quot;Agents&quot; section, and anything related to editing code and configuring VS Code is grouped under &quot;Editor&quot;.</p>
<p>Previously, the documentation for supported languages and specific extensions was individually listed in the table of contents. We have now moved them under &quot;Languages and Runtimes&quot; and &quot;Extension Docs&quot; respectively, so you can find all the information you need in one place.</p>
<p>Let us know what you think of the new structure by <a href="https://github.com/microsoft/vscode-docs/issues" class="external-link" target="_blank">submitting feedback</a> in the microsoft/vscode-docs repository.</p>
<h2 id="_deprecated-features-and-settings" data-needslink="_deprecated-features-and-settings">Deprecated features and settings</h2>
<h3 id="_edit-mode" data-needslink="_edit-mode">Edit mode</h3>
<p>We have deprecated the built-in Edit mode, and removed the <code>chat.editMode.hidden</code> setting. We recommend using <a href="https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode">Agent mode</a> instead, which covers the same editing scenarios while also being able to run tasks and tools on your behalf. Alternatively, you can create a <a href="https://code.visualstudio.com/docs/agent-customization/custom-agents">custom agent</a> to mimic the Edit mode experience.</p>
<p>Users who have Agent mode disabled (<code>chat.agent.enabled</code>) by policy will still see the legacy Edit mode.</p>
<h2 id="_thank-you" data-needslink="_thank-you">Thank you</h2>
<p>Contributions to <code>vscode</code>:</p>
<ul>
<li><a href="https://github.com/bikeshgyawali" class="external-link" target="_blank">@bikeshgyawali (Bikesh)</a>:  Add missing unit test coverage for prefixedUuid in uuid.ts <a href="https://github.com/microsoft/vscode/pull/322146" class="external-link" target="_blank">PR #322146</a></li>
<li><a href="https://github.com/Bryan2333" class="external-link" target="_blank">@Bryan2333 (BryanLiang)</a>: fix issue 300307 <a href="https://github.com/microsoft/vscode/pull/322104" class="external-link" target="_blank">PR #322104</a></li>
<li><a href="https://github.com/carlbrochu" class="external-link" target="_blank">@carlbrochu (Carl Brochu)</a>: Add SKU to enhance GH telemetry events <a href="https://github.com/microsoft/vscode/pull/321046" class="external-link" target="_blank">PR #321046</a></li>
<li><a href="https://github.com/cavalloJustinEmery" class="external-link" target="_blank">@cavalloJustinEmery (Justin Emery)</a>: fix: plugin skill files not accessible when connected to remote <a href="https://github.com/microsoft/vscode/pull/309465" class="external-link" target="_blank">PR #309465</a></li>
<li><a href="https://github.com/guomaggie" class="external-link" target="_blank">@guomaggie</a>: select correct subagent model <a href="https://github.com/microsoft/vscode/pull/321061" class="external-link" target="_blank">PR #321061</a></li>
<li><a href="https://github.com/mjbvz" class="external-link" target="_blank">@mjbvz (Matt Bierner)</a>
<ul>
<li>Update contribution names <a href="https://github.com/microsoft/vscode/pull/321503" class="external-link" target="_blank">PR #321503</a></li>
<li>Fully switch normal <code>npm run compile</code> to use tsgo too <a href="https://github.com/microsoft/vscode/pull/321646" class="external-link" target="_blank">PR #321646</a></li>
<li>Kill and restart esbuild instances during watch mode <a href="https://github.com/microsoft/vscode/pull/321219" class="external-link" target="_blank">PR #321219</a></li>
</ul>
</li>
<li><a href="https://github.com/rfeltis" class="external-link" target="_blank">@rfeltis (Ralph Feltis)</a>: Add telemetry for chat quota notification banners <a href="https://github.com/microsoft/vscode/pull/321793" class="external-link" target="_blank">PR #321793</a></li>
<li><a href="https://github.com/romalpani" class="external-link" target="_blank">@romalpani (Rohan Malpani)</a>: Update new chat in session tip text <a href="https://github.com/microsoft/vscode/pull/321965" class="external-link" target="_blank">PR #321965</a></li>
<li><a href="https://github.com/wszgrcy" class="external-link" target="_blank">@wszgrcy (chen)</a>: fix: registerToolDefinition loss tags <a href="https://github.com/microsoft/vscode/pull/319922" class="external-link" target="_blank">PR #319922</a></li>
</ul>
<h3 id="_issue-tracking" data-needslink="_issue-tracking">Issue tracking</h3>
<p>Contributions to our issue tracking:</p>
<ul>
<li><a href="https://github.com/gjsjohnmurray" class="external-link" target="_blank">@gjsjohnmurray (John Murray)</a></li>
<li><a href="https://github.com/RedCMD" class="external-link" target="_blank">@RedCMD (RedCMD)</a></li>
<li><a href="https://github.com/IllusionMH" class="external-link" target="_blank">@IllusionMH (Andrii Dieiev)</a></li>
<li><a href="https://github.com/albertosantini" class="external-link" target="_blank">@albertosantini (Alberto Santini)</a></li>
</ul>
<hr>
<p>We really appreciate people trying our new features as soon as they are ready, so check back here often and learn what's new.</p>
<blockquote><p>If you'd like to read release notes for previous VS Code versions, go to <a href="https://code.visualstudio.com/updates">Updates</a> on <a href="https://code.visualstudio.com">code.visualstudio.com</a>.</p>
</blockquote><p><a id="scroll-to-top" role="button" title="Scroll to top" aria-label="scroll to top" href="#"><span class="icon"></span></a></p>

                <div class="feedback" data-edit-url="https://vscode.dev/github/microsoft/vscode-docs/blob/main/release-notes/v1_126.md"></div>
            </main>
            
            <!-- Right sidebar - On This Page -->
            <aside class="docs-right-sidebar hidden-xs">
                <nav id="docs-subnavbar" aria-label="On Page">
                    
                    <h4><span class="sr-only">On this page there are 8 sections</span><span
                            aria-hidden="true">On this page</span></h4>
                    <ul class="nav">
                        
                        <li><a href="#_cost-management">Cost management</a></li>
                        
                        <li><a href="#_language-models">Language models</a></li>
                        
                        <li><a href="#_agents-window-preview">Agents window (Preview)</a></li>
                        
                        <li><a href="#_editor-experience">Editor experience</a></li>
                        
                        <li><a href="#_engineering">Engineering</a></li>
                        
                        <li><a href="#_website">Website</a></li>
                        
                        <li><a href="#_deprecated-features-and-settings">Deprecated features and settings</a></li>
                        
                        <li><a href="#_thank-you">Thank you</a></li>
                        
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