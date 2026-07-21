---
source_url: https://code.visualstudio.com/updates/v1_128
ingested: 2026-07-17
sha256: a796201bb6a948a8940cd5bc64555793d5af61018b2d87dd49cd462b8f4ad70d
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

	<meta name="description" content="Learn what's new in Visual Studio Code 1.128" />
<meta name="keywords" content="" />
<!-- Twitter and Facebook OpenGraph Metadata-->
<meta name="twitter:card" content="summary_large_image" />
<meta property="og:url" content="https://code.visualstudio.com/updates/v1_128" />
<meta property="og:type" content="article" />
<meta property="og:title" content="Visual Studio Code 1.128" />
<meta property="og:description" content="Learn what's new in Visual Studio Code 1.128" />

<meta property="og:image" content="https://code.visualstudio.com/assets/updates/1_128/release-highlights.webp" />



	<link rel="shortcut icon" href="/assets/favicon.ico" sizes="128x128" />
	<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">

	<title>Visual Studio Code 1.128</title>

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
            		
            			<li class="active">
            				<a href="/updates/v1_128" aria-label="Current Page: 1.128">1.128</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_127" >1.127</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_126" >1.126</a>
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
            		
            			<option value="/updates/v1_128" selected>1.128</option>
            		
            			<option value="/updates/v1_127" >1.127</option>
            		
            			<option value="/updates/v1_126" >1.126</option>
            		
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
                <h1>Visual Studio Code 1.128</h1>
<p>Follow us on <a href="https://www.linkedin.com/showcase/vs-code" class="external-link" target="_blank">LinkedIn</a>, <a href="https://go.microsoft.com/fwlink/?LinkID=533687" class="external-link" target="_blank">X</a>, <a href="https://bsky.app/profile/vscode.dev" class="external-link" target="_blank">Bluesky</a></p>
<hr>
<p><em>Release date: July 8, 2026</em></p>
<p><strong>Update 1.128.1</strong>: The update addresses these <a href="https://github.com/microsoft/vscode/issues?q=is%3Aissue+is%3Aclosed+milestone%3A1.128.1" class="external-link" target="_blank">security issues</a>.</p>
<p>Downloads: Windows: <a href="https://update.code.visualstudio.com/1.128.1/win32-x64-user/stable">x64</a> <a href="https://update.code.visualstudio.com/1.128.1/win32-arm64-user/stable">Arm64</a> | Mac: <a href="https://update.code.visualstudio.com/1.128.1/darwin-universal-dmg/stable">Universal</a> <a href="https://update.code.visualstudio.com/1.128.1/darwin-x64-dmg/stable">Intel</a> <a href="https://update.code.visualstudio.com/1.128.1/darwin-arm64-dmg/stable">silicon</a> | Linux: <a href="https://update.code.visualstudio.com/1.128.1/linux-deb-x64/stable">deb</a> <a href="https://update.code.visualstudio.com/1.128.1/linux-rpm-x64/stable">rpm</a> <a href="https://update.code.visualstudio.com/1.128.1/linux-x64/stable">tarball</a> <a href="https://code.visualstudio.com/docs/supporting/faq#_previous-release-versions">Arm</a> <a href="https://update.code.visualstudio.com/1.128.1/linux-snap-x64/stable">snap</a></p>
<hr>
<p>Welcome to the 1.128 release of Visual Studio Code. This release brings richer multi-chat agent sessions, generally available image support in Chat, and OS-level keyboard shortcuts.</p>
<ul>
<li>
<p><a href="#_multiple-chats-in-a-session-now-supports-claude-harness">Multi-chat agent sessions</a>: Run several related chats in one Claude session to compare approaches and work in parallel.</p>
</li>
<li>
<p><a href="#_chat-without-a-selected-workspace-in-the-agents-window">Quick chats</a>: Ask a question in the Agents window without opening a workspace first.</p>
</li>
<li>
<p><a href="#_copilot-vision-is-now-generally-available">Copilot Vision</a>: Attach images and PDFs to Chat by pasting, dragging, or dropping them, now generally available.</p>
</li>
<li>
<p><a href="#_configurable-placement-of-integrated-browser-tabs">Browser tab placement</a>: Choose where integrated browser tabs open: the active group, a dedicated side group, or a separate window.</p>
</li>
<li>
<p><a href="#_os-level-keyboard-shortcuts">OS-level keyboard shortcuts</a>: Trigger VS Code commands with keybindings that work even when VS Code isn't focused.</p>
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
      <li><a href="#agents">Agents</a></li>
      <li><a href="#chat">Chat</a></li>
      <li><a href="#editor-experience">Editor Experience</a></li>
      <li><a href="#enterprise">Enterprise</a></li>
      <li><a href="#thank-you">Thank you</a></li>
    </ul>
  </nav>
  <div class="notes-main">
Navigation End -->
<h2 id="_agents" data-needslink="_agents">Agents</h2>
<h3 id="_multiple-chats-in-a-session-now-supports-claude-agent" data-needslink="_multiple-chats-in-a-session-now-supports-claude-agent">Multiple chats in a session now supports Claude agent</h3>
<p>Claude agent-host sessions in the <a href="https://code.visualstudio.com/docs/agents/agents-window">Agents window</a> provide agentic coding capabilities powered by Anthropic's Claude Agent SDK directly in VS Code. Multiple chats keep related conversation threads in one session instead of spreading them across separate top-level sessions.</p>
<p>Single-chat Claude sessions remain a focused way to work with the agent. With multiple chats, a session can contain related chats, so you can compare approaches, branch from an earlier turn, and run work in parallel. You can add chats, fork a chat from an existing turn, switch between peer chats, and send turns concurrently. Each chat keeps its own history, title, and model selection, and restores with the parent session after restart. Peer chats stay grouped under the Claude session and don't appear as separate top-level sessions.</p>
<p>The following video shows a single Claude session with multiple chats: the main chat adds a <code>/health</code> endpoint to an Express app, while a peer chat writes tests for it in parallel, and a forked chat explores an alternative implementation. Each chat runs independently and stays grouped under the same session.</p>
<p><video src="/assets/updates/1_128/claude-multi-chat-session.mp4" title="Video showing multiple chats running in parallel within a single Claude agent-host session." autoplay loop controls muted></video></p>
<p>This experience is available when using the Claude agent via the agent host. Ensure the agent host is enabled and can be selected for the Claude agent (via the harness picker) with <span class="setting"><span class="setting-dropdown" data-setting-id="chat.agentHost.enabled">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      chat.agentHost.enabled
    </span>
    <button 
      type="button"
      class="setting-dropdown-trigger"
      aria-haspopup="menu"
      aria-expanded="false"
      aria-describedby="org-setting-tooltip-chat-agentHost-enabled-233"
      aria-label="Open setting in VS Code">
        <svg class="setting-dropdown-chevron" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path d="M7.976 10.072l4.357-4.357.62.618L8.284 11h-.618L3 6.333l.619-.618 4.357 4.357z"/>
        </svg>
    </button>
    <span class="setting-dropdown-menu" role="menu" aria-label="Open setting">
      <span role="menuitem" class="setting-action-item" data-version="stable" tabindex="0">Open in VS Code</span>
      <span role="menuitem" class="setting-action-item" data-version="insiders" tabindex="-1">Open in VS Code Insiders</span>
    </span>
  </span><span class="sr-only" id="org-setting-tooltip-chat-agentHost-enabled-233">This setting is managed at the organization level. Contact your administrator to change it.</span><span class="badge-org" data-tooltip="This setting is managed at the organization level. Contact your administrator to change it." aria-hidden="true">ORG</span></span> and <span class="setting"><span class="setting-dropdown" data-setting-id="chat.agents.claude.preferAgentHost">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      chat.agents.claude.preferAgentHost
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
  </span></span>.</p>
<h3 id="_chat-without-a-selected-workspace-in-the-agents-window" data-needslink="_chat-without-a-selected-workspace-in-the-agents-window">Chat without a selected workspace in the Agents window</h3>
<p>The Agents window gives you a dedicated place to create, resume, and manage agent sessions. For project work, those sessions keep the chat, files, and changes together with the workspace.</p>
<p>For questions not tied to a folder, you can now start a chat in the Agents window without selecting a workspace. These chats appear in the <strong>Chats</strong> section and open focused and ready for input. Start a quick chat with <span class="dynamic-keybinding" data-commandId="sessionsView.newQuickChat" data-osx="⌘K ⌘N" data-win="cmd+K cmd+N" data-linux="cmd+K cmd+N"><span class="keybinding">⌘K ⌘N</span> (Windows, Linux <span class="keybinding">cmd+K cmd+N</span>)</span> or the plus button on the <strong>Chats</strong> section header.</p>
<p><video src="/assets/updates/1_128/quick-chat.mp4" title="Video showing starting a workspace-less quick chat in the Agents window." autoplay loop controls muted></video></p>
<p>Because a quick chat is workspace-less, it does not show the workspace-specific <strong>Changes</strong> or <strong>Files</strong> side pane. Quick chats are restored with your other sessions after reload and remain separate from workspace sessions.</p>
<p>Chats without a workspace are supported only by agent host sessions, so this experience is available when the agent host is enabled (and selected via the harness picker) with <span class="setting"><span class="setting-dropdown" data-setting-id="chat.agentHost.enabled">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      chat.agentHost.enabled
    </span>
    <button 
      type="button"
      class="setting-dropdown-trigger"
      aria-haspopup="menu"
      aria-expanded="false"
      aria-describedby="org-setting-tooltip-chat-agentHost-enabled-234"
      aria-label="Open setting in VS Code">
        <svg class="setting-dropdown-chevron" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path d="M7.976 10.072l4.357-4.357.62.618L8.284 11h-.618L3 6.333l.619-.618 4.357 4.357z"/>
        </svg>
    </button>
    <span class="setting-dropdown-menu" role="menu" aria-label="Open setting">
      <span role="menuitem" class="setting-action-item" data-version="stable" tabindex="0">Open in VS Code</span>
      <span role="menuitem" class="setting-action-item" data-version="insiders" tabindex="-1">Open in VS Code Insiders</span>
    </span>
  </span><span class="sr-only" id="org-setting-tooltip-chat-agentHost-enabled-234">This setting is managed at the organization level. Contact your administrator to change it.</span><span class="badge-org" data-tooltip="This setting is managed at the organization level. Contact your administrator to change it." aria-hidden="true">ORG</span></span>.</p>
<p>The <strong>Pinned</strong> and <strong>Chats</strong> groups stay visible when empty by default. Use <span class="setting"><span class="setting-dropdown" data-setting-id="sessions.list.showEmptyDefaultGroups">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      sessions.list.showEmptyDefaultGroups
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
  </span></span> to hide these default groups until they contain sessions.</p>
<h3 id="_read-only-subagent-chats-in-the-agents-window-preview" data-needslink="_read-only-subagent-chats-in-the-agents-window-preview">Read-only subagent chats in the Agents window (Preview)</h3>
<p>When an agent delegates work to subagents, you can follow each worker's progress without interrupting or steering it from the main conversation. The Agents window provides a dedicated space for agent-driven workflows across projects, with chat and sessions as the primary interface.</p>
<p>When a session spawns <a href="https://code.visualstudio.com/docs/agents/subagents">subagents</a>, their transcripts appear as read-only peer chats. Subagent chats are hidden from the tab strip until you open them from the Conversations menu, the running-subagents chip, or the inline subagent pill in the parent transcript. Opened subagent chats show their live progress, use the subagent title when available, and omit the composer and mutating chat actions so the worker transcript stays view-only.</p>
<p><video src="/assets/updates/1_128/sub-agent-chats.mp4" title="Video showing read-only subagent chats opened from a running session in the Agents window." autoplay loop controls muted></video></p>
<p>This experience is available when using Copilot via the agent host. Ensure the agent host is enabled (and selected via the harness picker) with <span class="setting"><span class="setting-dropdown" data-setting-id="chat.agentHost.enabled">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      chat.agentHost.enabled
    </span>
    <button 
      type="button"
      class="setting-dropdown-trigger"
      aria-haspopup="menu"
      aria-expanded="false"
      aria-describedby="org-setting-tooltip-chat-agentHost-enabled-235"
      aria-label="Open setting in VS Code">
        <svg class="setting-dropdown-chevron" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path d="M7.976 10.072l4.357-4.357.62.618L8.284 11h-.618L3 6.333l.619-.618 4.357 4.357z"/>
        </svg>
    </button>
    <span class="setting-dropdown-menu" role="menu" aria-label="Open setting">
      <span role="menuitem" class="setting-action-item" data-version="stable" tabindex="0">Open in VS Code</span>
      <span role="menuitem" class="setting-action-item" data-version="insiders" tabindex="-1">Open in VS Code Insiders</span>
    </span>
  </span><span class="sr-only" id="org-setting-tooltip-chat-agentHost-enabled-235">This setting is managed at the organization level. Contact your administrator to change it.</span><span class="badge-org" data-tooltip="This setting is managed at the organization level. Contact your administrator to change it." aria-hidden="true">ORG</span></span>.</p>
<h3 id="_keyboard-shortcuts-for-chats-in-the-agents-window" data-needslink="_keyboard-shortcuts-for-chats-in-the-agents-window">Keyboard shortcuts for chats in the Agents window</h3>
<!-- TODO(next release): Document the single-pane detail panel for the Agents window (Experimental, setting sessions.layout.singlePaneDetailPanel). Removed from 1.128.0 — to be documented in the next release. -->
<p>The Agents window supports multi-chat sessions, where one agent session can contain multiple related chats. Keyboard-driven chat navigation helps you move between chats and manage chat tabs without leaving the keyboard.</p>
<ul>
<li>Create a chat with <span class="dynamic-keybinding" data-commandId="sessions.chatCompositeBar.addChat" data-osx="⌘T" data-win="cmd+T" data-linux="cmd+T"><span class="keybinding">⌘T</span> (Windows, Linux <span class="keybinding">cmd+T</span>)</span>.</li>
<li>Reopen the last closed chat with <span class="dynamic-keybinding" data-commandId="sessions.chatCompositeBar.reopenLastClosedChat" data-osx="⇧⌘T" data-win="Shift+cmd+T" data-linux="Shift+cmd+T"><span class="keybinding">⇧⌘T</span> (Windows, Linux <span class="keybinding">Shift+cmd+T</span>)</span>.</li>
<li>Go to the next or previous chat with <span class="dynamic-keybinding" data-commandId="sessions.chatCompositeBar.navigateNextChat" data-osx="⇧⌘]" data-win="Shift+cmd+]" data-linux="Shift+cmd+]"><span class="keybinding">⇧⌘]</span> (Windows, Linux <span class="keybinding">Shift+cmd+]</span>)</span> and <span class="dynamic-keybinding" data-commandId="sessions.chatCompositeBar.navigatePreviousChat" data-osx="⇧⌘[" data-win="Shift+cmd+[" data-linux="Shift+cmd+["><span class="keybinding">⇧⌘[</span> (Windows, Linux <span class="keybinding">Shift+cmd+[</span>)</span>.</li>
<li>Quickly switch between open chats with <span class="dynamic-keybinding" data-commandId="sessions.quickSwitchNextChat" data-osx="⌃Tab" data-win="Ctrl+Tab" data-linux="Ctrl+Tab"><span class="keybinding">⌃Tab</span> (Windows, Linux <span class="keybinding">Ctrl+Tab</span>)</span> and <span class="dynamic-keybinding" data-commandId="sessions.quickSwitchPreviousChat" data-osx="⌃⇧Tab" data-win="Ctrl+Shift+Tab" data-linux="Ctrl+Shift+Tab"><span class="keybinding">⌃⇧Tab</span> (Windows, Linux <span class="keybinding">Ctrl+Shift+Tab</span>)</span>.</li>
<li>Close the active chat tab with <span class="dynamic-keybinding" data-commandId="sessions.chatCompositeBar.closeChat" data-osx="⌘W" data-win="cmd+W" data-linux="cmd+W"><span class="keybinding">⌘W</span> (Windows, Linux <span class="keybinding">cmd+W</span>)</span>.</li>
<li>Delete the active non-main chat with <span class="dynamic-keybinding" data-commandId="sessions.chatCompositeBar.deleteChat" data-osx="⌘Backspace" data-win="cmd+Backspace" data-linux="cmd+Backspace"><span class="keybinding">⌘Backspace</span> (Windows, Linux <span class="keybinding">cmd+Backspace</span>)</span>.</li>
<li>Open a searchable picker for open and closed chats with <span class="dynamic-keybinding" data-commandId="sessions.showChatsPicker" data-osx="⇧⌘O" data-win="Shift+cmd+O" data-linux="Shift+cmd+O"><span class="keybinding">⇧⌘O</span> (Windows, Linux <span class="keybinding">Shift+cmd+O</span>)</span>.</li>
</ul>
<p>These shortcuts are scoped to the Agents window and fall back to the existing session-level behavior when there is no chat-specific action to perform.</p>
<h2 id="_chat" data-needslink="_chat">Chat</h2>
<h3 id="_copilot-vision-is-now-generally-available" data-needslink="_copilot-vision-is-now-generally-available">Copilot Vision is now generally available</h3>
<p>Multimodal support is now generally available in VS Code, starting with this latest release. Attach images and PDFs by pasting them into Chat, dragging and dropping them, or using the context menu. Images may also be read by the agent via a tool call.</p>
<p>Check out this <a href="https://github.blog/changelog/2026-07-01-copilot-vision-is-generally-available/" class="external-link" target="_blank">GitHub changelog</a> for supported formats and availability details.</p>
<h3 id="_byok-models-in-agent-host-copilot-sessions-experimental" data-needslink="_byok-models-in-agent-host-copilot-sessions-experimental">BYOK models in agent host Copilot sessions (Experimental)</h3>
<p><strong>Setting</strong>: <span class="setting"><span class="setting-dropdown" data-setting-id="chat.agentHost.byokModels.enabled">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      chat.agentHost.byokModels.enabled
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
<p>Use <a href="https://code.visualstudio.com/docs/agent-customization/language-models#_bring-your-own-language-model-key">Bring Your Own Key (BYOK) models</a> when you run sessions on an agent host. Enable <span class="setting"><span class="setting-dropdown" data-setting-id="chat.agentHost.byokModels.enabled">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      chat.agentHost.byokModels.enabled
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
  </span></span> and restart the agent host process for the change to take effect.</p>
<p>This feature is experimental and is still under active development. Ensure the agent host is enabled and can be selected with <span class="setting"><span class="setting-dropdown" data-setting-id="chat.agentHost.enabled">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      chat.agentHost.enabled
    </span>
    <button 
      type="button"
      class="setting-dropdown-trigger"
      aria-haspopup="menu"
      aria-expanded="false"
      aria-describedby="org-setting-tooltip-chat-agentHost-enabled-236"
      aria-label="Open setting in VS Code">
        <svg class="setting-dropdown-chevron" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path d="M7.976 10.072l4.357-4.357.62.618L8.284 11h-.618L3 6.333l.619-.618 4.357 4.357z"/>
        </svg>
    </button>
    <span class="setting-dropdown-menu" role="menu" aria-label="Open setting">
      <span role="menuitem" class="setting-action-item" data-version="stable" tabindex="0">Open in VS Code</span>
      <span role="menuitem" class="setting-action-item" data-version="insiders" tabindex="-1">Open in VS Code Insiders</span>
    </span>
  </span><span class="sr-only" id="org-setting-tooltip-chat-agentHost-enabled-236">This setting is managed at the organization level. Contact your administrator to change it.</span><span class="badge-org" data-tooltip="This setting is managed at the organization level. Contact your administrator to change it." aria-hidden="true">ORG</span></span>.</p>
<h3 id="_configure-sampling-parameters-for-custom-endpoint-models" data-needslink="_configure-sampling-parameters-for-custom-endpoint-models">Configure sampling parameters for custom endpoint models</h3>
<p>You can configure <code>temperature</code> and <code>top_p</code> for each <a href="https://code.visualstudio.com/docs/agent-customization/language-models#_add-a-custom-endpoint-model">Custom Endpoint model</a>, so requests work with providers that have strict parameter requirements.</p>
<p>Add the <code>modelOptions</code> object to a model's JSON configuration:</p>
<pre class="shiki" data-lang="json" shiki-themes dark-plus light-plus" style="--shiki-dark:#D4D4D4;--shiki-light:#000000;--shiki-dark-bg:#1E1E1E;--shiki-light-bg:#FFFFFF" tabindex="0"><code><span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">{</span></span>
<span class="line"><span style="--shiki-dark:#F44747;--shiki-light:#CD3131">   ...</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">   "models"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: [</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">   {</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">     "id"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"&#x3C;model-id>"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">,</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">     "modelOptions"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: {</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">       "temperature"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#B5CEA8;--shiki-light:#098658">1</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">,</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">       "top_p"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#569CD6;--shiki-light:#0000FF">null</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">     },</span></span>
<span class="line"><span style="--shiki-dark:#F44747;--shiki-light:#CD3131">     ...</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">   }</span></span>
<span class="line"><span style="--shiki-dark:#F44747;--shiki-light:#CD3131">}</span></span>
<span class="line"></span></code></pre>
<p>Set a property to a number to override the default value that VS Code sends. Set it to <code>null</code> to omit the parameter from requests and use the model server's default. These options apply to Chat Completions, Responses, and Messages-compatible endpoints.</p>
<h3 id="_configure-the-default-utility-model-for-byok" data-needslink="_configure-the-default-utility-model-for-byok">Configure the default utility model for BYOK</h3>
<p><strong>Setting</strong>: <span class="setting"><span class="setting-dropdown" data-setting-id="chat.byokUtilityModelDefault">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      chat.byokUtilityModelDefault
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
<p>When you use a bring your own key (BYOK) model as the main agent model, you can change the default behavior used by built-in utility flows, such as generating a chat title or a commit message. Set <span class="setting"><span class="setting-dropdown" data-setting-id="chat.byokUtilityModelDefault">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      chat.byokUtilityModelDefault
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
  </span></span> to use the main agent model, use a model provided by GitHub Copilot, or not use a default utility model.</p>
<blockquote><p><strong>Note:</strong> The default behavior is that no utility models are used with BYOK models as the main agent. Background tasks such as chat title generation and commit message generation do not work unless this option is set.</p>
</blockquote><p>This setting has no effect when the main agent model is provided by GitHub Copilot. A model configured with <span class="setting"><span class="setting-dropdown" data-setting-id="chat.utilityModel">
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
  </span></span> or <span class="setting"><span class="setting-dropdown" data-setting-id="chat.utilitySmallModel">
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
  </span></span> takes precedence over this default.</p>
<h3 id="_deep-links-to-a-specific-chat" data-needslink="_deep-links-to-a-specific-chat">Deep links to a specific chat</h3>
<p>The Agents window helps you manage agent sessions and return to their associated workspaces and chats. Deep links can take you directly back to the relevant chat, so you don't have to open the workspace first and then manually find the session in Chat.</p>
<p>When an app opens a <code>vscode://</code> deep link for a session, VS Code opens the workspace and focuses the specific chat identified by the link's <code>session</code> query parameter. The <strong>Open in VS Code</strong> action in the Agents window uses the same behavior, opening both the session's workspace folder and its active chat in the new VS Code window.</p>
<h2 id="_editor-experience" data-needslink="_editor-experience">Editor Experience</h2>
<h3 id="_configurable-placement-of-integrated-browser-tabs" data-needslink="_configurable-placement-of-integrated-browser-tabs">Configurable placement of integrated browser tabs</h3>
<p><strong>Setting</strong>: <span class="setting"><span class="setting-dropdown" data-setting-id="workbench.browser.newTabPlacement">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      workbench.browser.newTabPlacement
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
<p>Keeping tabs organized can be a challenge. With this release, you can configure a location for browser tabs to open via the <span class="setting"><span class="setting-dropdown" data-setting-id="workbench.browser.newTabPlacement">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      workbench.browser.newTabPlacement
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
  </span></span> setting. The setting can take the following values:</p>
<ul>
<li><strong><code>activeGroup</code></strong> (default): Browser tabs always open in the active editor group.</li>
<li><strong><code>sideGroup</code></strong>: Browser tabs open in a dedicated group to the side. This group is locked so only browser tabs open there.</li>
<li><strong><code>window</code></strong>: Browser tabs open in a dedicated auxiliary window. This window group is also locked to only browser tabs.</li>
</ul>
<p>You can still reorganiz