---
source_url: https://code.visualstudio.com/updates/v1_129
ingested: 2026-07-17
sha256: 1fac25fa2570dc82bbd7a1255a3c8419b251c744d397ba605e9eb41134dd45cd
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

	<meta name="description" content="Learn what is new in Visual Studio Code 1.129." />
<meta name="keywords" content="" />
<!-- Twitter and Facebook OpenGraph Metadata-->
<meta name="twitter:card" content="summary_large_image" />
<meta property="og:url" content="https://code.visualstudio.com/updates/v1_129" />
<meta property="og:type" content="article" />
<meta property="og:title" content="Visual Studio Code 1.129" />
<meta property="og:description" content="Learn what is new in Visual Studio Code 1.129." />

<meta property="og:image" content="https://code.visualstudio.com/assets/updates/1_129/release-highlights.webp" />



	<link rel="shortcut icon" href="/assets/favicon.ico" sizes="128x128" />
	<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">

	<title>Visual Studio Code 1.129</title>

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
            		
            			<li class="active">
            				<a href="/updates/v1_129" aria-label="Current Page: 1.129">1.129</a>
            			</li>
            		
            			<li >
            				<a href="/updates/v1_128" >1.128</a>
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
            		
            			<option value="/updates/v1_129" selected>1.129</option>
            		
            			<option value="/updates/v1_128" >1.128</option>
            		
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
                <h1>Visual Studio Code 1.129</h1>
<p>Follow us on <a href="https://www.linkedin.com/showcase/vs-code" class="external-link" target="_blank">LinkedIn</a>, <a href="https://go.microsoft.com/fwlink/?LinkID=533687" class="external-link" target="_blank">X</a>, <a href="https://bsky.app/profile/vscode.dev" class="external-link" target="_blank">Bluesky</a></p>
<hr>
<p><em>Release date: July 15, 2026</em></p>
<p>Downloads: Windows: <a href="https://update.code.visualstudio.com/1.129.0/win32-x64-user/stable">x64</a> <a href="https://update.code.visualstudio.com/1.129.0/win32-arm64-user/stable">Arm64</a> | Mac: <a href="https://update.code.visualstudio.com/1.129.0/darwin-universal-dmg/stable">Universal</a> <a href="https://update.code.visualstudio.com/1.129.0/darwin-x64-dmg/stable">Intel</a> <a href="https://update.code.visualstudio.com/1.129.0/darwin-arm64-dmg/stable">silicon</a> | Linux: <a href="https://update.code.visualstudio.com/1.129.0/linux-deb-x64/stable">deb</a> <a href="https://update.code.visualstudio.com/1.129.0/linux-rpm-x64/stable">rpm</a> <a href="https://update.code.visualstudio.com/1.129.0/linux-x64/stable">tarball</a> <a href="https://code.visualstudio.com/docs/supporting/faq#_previous-release-versions">Arm</a> <a href="https://update.code.visualstudio.com/1.129.0/linux-snap-x64/stable">snap</a></p>
<hr>
<p>Welcome to the 1.129 release of Visual Studio Code. This release brings a dedicated agent host, a new editor panel in the Agents window, running commands with <code>!</code>, and a preview of the modern UI.</p>
<ul>
<li>
<p><a href="#_the-agent-host">The agent host</a>: Run agent sessions in a dedicated process and connect to them from multiple windows.</p>
</li>
<li>
<p><a href="#_new-editor-panel-in-the-agents-window-experimental">New editor panel in the Agents window (Experimental)</a>: Review agent-generated files and diffs in a docked editor.</p>
</li>
<li>
<p><a href="#_run-commands-with--prefix">Run commands with <code>!</code> prefix</a>: Run terminal commands directly from chat prompts.</p>
</li>
<li>
<p><a href="#_modern-ui-preview-experimental">Modern UI preview (Experimental)</a>: Get a first look at the updated VS Code workbench appearance.</p>
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
      <li><a href="#editor-experience">Editor experience</a></li>
      <li><a href="#authentication">Authentication</a></li>
      <li><a href="#proposed-apis">Proposed APIs</a></li>
      <li><a href="#thank-you">Thank you</a></li>
    </ul>
  </nav>
  <div class="notes-main">
Navigation End -->
<h2 id="_agents" data-needslink="_agents">Agents</h2>
<h3 id="_the-agent-host" data-needslink="_the-agent-host">The agent host</h3>
<p>We're rearchitecting how agent sessions work in VS Code around the agent host - a dedicated process that runs agent harnesses such as Copilot, Claude, and Codex, based on the <a href="https://microsoft.github.io/agent-host-protocol/" class="external-link" target="_blank">Agent Host Protocol</a> (AHP). Because a session lives in its own process, the same session can be connected to and rendered from multiple VS Code windows at once. The agent host's Copilot agent is powered by the <a href="https://www.npmjs.com/package/@github/copilot-sdk" class="external-link" target="_blank">Copilot SDK</a>, which means that its behavior and functionality is aligned with the Copilot CLI, the standalone GitHub Copilot app, and other Copilot products.</p>
<p>We're actively developing the agent host and starting to roll it out to users in both the editor window and the <a href="https://code.visualstudio.com/docs/agents/agents-window">Agents window</a>. To opt in, enable <span class="setting"><span class="setting-dropdown" data-setting-id="chat.agentHost.enabled">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      chat.agentHost.enabled
    </span>
    <button 
      type="button"
      class="setting-dropdown-trigger"
      aria-haspopup="menu"
      aria-expanded="false"
      aria-describedby="org-setting-tooltip-chat-agentHost-enabled-237"
      aria-label="Open setting in VS Code">
        <svg class="setting-dropdown-chevron" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path d="M7.976 10.072l4.357-4.357.62.618L8.284 11h-.618L3 6.333l.619-.618 4.357 4.357z"/>
        </svg>
    </button>
    <span class="setting-dropdown-menu" role="menu" aria-label="Open setting">
      <span role="menuitem" class="setting-action-item" data-version="stable" tabindex="0">Open in VS Code</span>
      <span role="menuitem" class="setting-action-item" data-version="insiders" tabindex="-1">Open in VS Code Insiders</span>
    </span>
  </span><span class="sr-only" id="org-setting-tooltip-chat-agentHost-enabled-237">This setting is managed at the organization level. Contact your administrator to change it.</span><span class="badge-org" data-tooltip="This setting is managed at the organization level. Contact your administrator to change it." aria-hidden="true">ORG</span></span> and then pick an agent host harness from the harness dropdown. The screenshot below shows how to select the <code>Copilot</code> harness on the agent host in the editor window:</p>
<p><img src="/assets/updates/1_129/agent-host-harness-dropdown-editor.webp" alt="Screenshot showing the harness dropdown in the editor window." width="1167" height="450" loading="lazy"></p>
<p>As we continue to invest in the agent host, some new features in these release notes may only be available when an agent runs on it. Those features link back to this section and, where relevant, note any additional settings that enable them (for example, <span class="setting"><span class="setting-dropdown" data-setting-id="chat.agents.claude.preferAgentHost">
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
  </span></span> to enable the Claude agent on the agent host).</p>
<h3 id="_new-editor-panel-in-the-agents-window-experimental" data-needslink="_new-editor-panel-in-the-agents-window-experimental">New editor panel in the Agents window (Experimental)</h3>
<p>The <a href="https://code.visualstudio.com/docs/agents/agents-window">Agents window</a> shows your conversation with an agent next to a detail area for the files and changes it produces. This release introduces a redesigned <strong>editor panel</strong> that brings the editor and the detail area together into one docked pane with a shared tab bar, so reviewing an agent's work feels like working in the main editor instead of switching between separate panels.</p>
<p>With the new editor panel, you can:</p>
<ul>
<li>Open files and diffs directly inside the docked editor, next to your chat, and add tabs with a <strong>New Tab</strong> action that matches the chat tab strip.</li>
<li>Review changes in the <strong>Changes</strong> view with an improved diff experience: toggle between inline and side-by-side views, expand or collapse all files at once, and read changes in a more compact diff representation that fits more of the change on screen. The next action, such as <strong>Create Pull Request</strong>, is available right from the editor tab title, and editor keybindings like toggling the diff view work the same as they do in the main VS Code window.</li>
<li>Pick up where you left off. Each session restores its side-pane width, open editors, active editor, and per-file collapsed state across session switches and window reloads.</li>
</ul>
<p>This is an experimental, opt-in layout. To try it, enable <span class="setting"><span class="setting-dropdown" data-setting-id="sessions.layout.singlePaneDetailPanel">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      sessions.layout.singlePaneDetailPanel
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
  </span></span> and reload the window, since the setting is read once at startup.</p>
<p><video src="/assets/updates/1_129/editor-panel.mp4" title="Video showing the new editor panel in the Agents window: opening files and diffs in the docked editor next to the chat, toggling between inline and side-by-side diffs in the Changes view, expanding and collapsing files, and the layout restoring its state after switching sessions." autoplay loop controls muted></video></p>
<h3 id="_session-management-tools-for-agent-host-sessions" data-needslink="_session-management-tools-for-agent-host-sessions">Session-management tools for Agent Host sessions</h3>
<p>Agents running on <a href="#_the-agent-host">the agent host</a> (Copilot, Claude, and Codex) now have access to a suite of session-management tools, so an agent can enumerate, create, observe, and act on other sessions and chats without you needing to switch away from your current conversation.</p>
<p>With these tools, an agent can:</p>
<ul>
<li>List your sessions with their status, workspace, and changes, so it can find the right one to act on. Archived sessions are excluded unless explicitly requested.</li>
<li>Read another session's recent conversation to understand what it's doing.</li>
<li>Create a new session or a new chat within an existing session to hand off a sub-task, rather than overloading a single conversation with unrelated work.</li>
<li>Send a message to a session or chat it created, to kick off or steer that work.</li>
</ul>
<p>Whenever a tool creates or targets a session, VS Code renders an <strong>Open Session</strong> pill so you can jump straight to it. Sending a message to another session always asks for your confirmation first. An agent can't message its own chat, and a burst of sends is capped so a single request can't fan out into an unbounded number of sessions.</p>
<p><video src="/assets/updates/1_129/agent-create-session.mp4" title="Video showing an agent using a session-management tool to create a new session, with the Open Session pill that opens the newly created session." autoplay loop controls muted></video></p>
<h3 id="_agents-window-improvements" data-needslink="_agents-window-improvements">Agents window improvements</h3>
<p>This release includes several smaller improvements to the <a href="https://code.visualstudio.com/docs/agents/agents-window">Agents window</a> new-session flow:</p>
<ul>
<li><strong>Remembered new-session defaults</strong>: the new-session picker remembers your last agent mode and approvals choices and uses them as the defaults the next time you create a session, so you don't have to reselect the same options for every task.</li>
<li><strong>Worktree checkbox</strong>: instead of choosing between folder and worktree isolation from a dropdown, the new-session configuration shows a single <strong>New Worktree</strong> checkbox. Check it to run the session with Git worktree isolation, which keeps the agent's changes in a separate folder until you're ready to review and merge them, or leave it unchecked to use folder isolation.</li>
</ul>
<h2 id="_chat" data-needslink="_chat">Chat</h2>
<h3 id="_run-commands-with-prefix" data-needslink="_run-commands-with-prefix">Run commands with <code>!</code> prefix</h3>
<p>You can now prefix chat messages with a <code>!</code> to run their contents as terminal commands. This works in <a href="#_the-agent-host">agent host</a> sessions both in the editor and Agents window.</p>
<p><img src="/assets/updates/1_129/bang-commands.webp" alt="Screenshot showing running a terminal command from chat with the ! prefix." width="899" height="227" loading="lazy"></p>
<h3 id="_byok-models-with-the-copilot-agent-harness" data-needslink="_byok-models-with-the-copilot-agent-harness">BYOK models with the Copilot agent harness</h3>
<p>You can now use <a href="https://code.visualstudio.com/docs/agent-customization/language-models#_bring-your-own-language-model-key">Bring Your Own Key (BYOK) models</a> in the Agents window when you select the <strong>Copilot</strong> harness running on <a href="#_the-agent-host">the agent host</a>.</p>
<p><video src="/assets/updates/1_129/byok-agents-window.mp4" title="Video showing a BYOK model used with the Copilot agent harness in the Agents window." autoplay loop controls muted></video></p>
<h3 id="_migrate-prompt-files-to-skills-experimental" data-needslink="_migrate-prompt-files-to-skills-experimental">Migrate prompt files to skills (Experimental)</h3>
<p>Prompt files (<code>*.prompt.md</code>) are used to describe custom slash commands. They are only supported in the Local agent harness while other harnesses express slash commands with skills. For compatibility across harnesses, we recommend to migrate all prompt files to skills.</p>
<p>With <span class="setting"><span class="setting-dropdown" data-setting-id="chat.customizations.promptMigration.enabled">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      chat.customizations.promptMigration.enabled
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
  </span></span> enabled, if you select a harness running on the <a href="#_the-agent-host">the agent host</a> and you have migratable prompt files, you'll now see a 'Migrate Prompts' entry in the AI Customizations overview.</p>
<p>The migration interface lets you:</p>
<ul>
<li>View prompt files from both workspace (<code>.github/prompts/</code>) and user data locations.</li>
<li>Migrate selected files to skills and open the newly created skills.</li>
</ul>
<p><img src="/assets/updates/1_129/migrate-prompt-files.webp" alt="migrate prompt files" width="1478" height="720" loading="lazy"></p>
<h2 id="_editor-experience" data-needslink="_editor-experience">Editor experience</h2>
<h3 id="_reopen-an-editor-from-the-editor-toolbar" data-needslink="_reopen-an-editor-from-the-editor-toolbar">Reopen an editor from the editor toolbar</h3>
<p>When a file or diff supports multiple editors, you can switch editors directly from the editor toolbar. Open the <strong>...</strong> menu and select an editor from the <strong>Reopen Editor With</strong> submenu. This makes alternative editors easier to discover without using the Command Palette.</p>
<h3 id="_modern-ui-preview-experimental" data-needslink="_modern-ui-preview-experimental">Modern UI preview (Experimental)</h3>
<p><strong>Setting</strong>: <span class="setting"><span class="setting-dropdown" data-setting-id="workbench.experimental.modernUI">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      workbench.experimental.modernUI
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
<p>You can now preview a modernized VS Code UI that updates the look and feel of the editor workbench. This is currently an experimental feature that you can enable with the <span class="setting"><span class="setting-dropdown" data-setting-id="workbench.experimental.modernUI">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      workbench.experimental.modernUI
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
  </span></span> setting and is enabled by default in Insiders builds.</p>
<p><video src="/assets/updates/1_129/modern-editor-workbench-ui.mp4" title="Video showing the modernized VS Code editor workbench UI." autoplay loop controls muted></video></p>
<h2 id="_authentication" data-needslink="_authentication">Authentication</h2>
<h3 id="_github-enterprise-support-for-copilot-in-the-agent-host" data-needslink="_github-enterprise-support-for-copilot-in-the-agent-host">GitHub Enterprise support for Copilot in the agent host</h3>
<p>Developers whose GitHub Copilot access is provided through a GitHub Enterprise (GHE) instance can sign in and use Copilot in VS Code. Previously, the agent host's Copilot authentication only supported github.com, so a GHE-backed Copilot subscription could not complete sign-in: both the OAuth flow and the Copilot token request targeted github.com.</p>
<p>With this release, VS Code can authenticate Copilot against a GitHub Enterprise instance. When you sign in to Copilot, choose your GitHub Enterprise instance, and VS Code runs the sign-in flow and requests Copilot access tokens from that host instead of github.com. This works in both the editor window and the <a href="https://code.visualstudio.com/docs/agents/agents-window">Agents window</a>, and with both the Copilot and Claude agents.</p>
<p>Because this support is part of <a href="#_the-agent-host">the agent host</a>, ensure the agent host is enabled with <span class="setting"><span class="setting-dropdown" data-setting-id="chat.agentHost.enabled">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      chat.agentHost.enabled
    </span>
    <button 
      type="button"
      class="setting-dropdown-trigger"
      aria-haspopup="menu"
      aria-expanded="false"
      aria-describedby="org-setting-tooltip-chat-agentHost-enabled-238"
      aria-label="Open setting in VS Code">
        <svg class="setting-dropdown-chevron" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path d="M7.976 10.072l4.357-4.357.62.618L8.284 11h-.618L3 6.333l.619-.618 4.357 4.357z"/>
        </svg>
    </button>
    <span class="setting-dropdown-menu" role="menu" aria-label="Open setting">
      <span role="menuitem" class="setting-action-item" data-version="stable" tabindex="0">Open in VS Code</span>
      <span role="menuitem" class="setting-action-item" data-version="insiders" tabindex="-1">Open in VS Code Insiders</span>
    </span>
  </span><span class="sr-only" id="org-setting-tooltip-chat-agentHost-enabled-238">This setting is managed at the organization level. Contact your administrator to change it.</span><span class="badge-org" data-tooltip="This setting is managed at the organization level. Contact your administrator to change it." aria-hidden="true">ORG</span></span>.</p>
<h2 id="_proposed-apis" data-needslink="_proposed-apis">Proposed APIs</h2>
<h3 id="_configure-custom-editors-for-diff-and-merge-editors" data-needslink="_configure-custom-editors-for-diff-and-merge-editors">Configure custom editors for diff and merge editors</h3>
<p>Custom editors now opt out of diff and merge editors by default. As a result, a file can continue to open in a custom editor while its diffs and merges open in the built-in text editors. You might notice this change if you previously saw a custom editor when opening a diff or merge editor.</p>
<p>To open a diff in another editor, use the <a href="#_reopen-an-editor-from-the-editor-toolbar"><strong>Reopen Editor With</strong> submenu</a> in the editor toolbar. To always use a specific editor for matching diffs, configure the <span class="setting"><span class="setting-dropdown" data-setting-id="workbench.diffEditorAssociations">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      workbench.diffEditorAssociations
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
  </span></span> setting.</p>
<p>The proposed <code>customEditorPriority</code> API provides separate priorities for files, diffs, and merge editors:</p>
<pre class="shiki" data-lang="json" shiki-themes dark-plus light-plus" style="--shiki-dark:#D4D4D4;--shiki-light:#000000;--shiki-dark-bg:#1E1E1E;--shiki-light-bg:#FFFFFF" tabindex="0"><code><span class="line"><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"priority"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: {</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">  "textEditor"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"default"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">,</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">  "diffEditor"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"option"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">,</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">  "mergeEditor"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"never"</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">}</span></span>
<span class="line"></span></code></pre>
<p>The new <code>never</code> priority prevents automatic selection for that editor type while keeping the editor available for explicit selection.</p>
<p>If the text diff editor cannot display binary content, VS Code still falls back to a compatible custom diff editor.</p>
<h2 id="_thank-you" data-needslink="_thank-you">Thank you</h2>
<p>Contributions to <code>vscode</code>:</p>
<ul>
<li><a href="https://github.com/accnops" class="external-link" target="_blank">@accnops (Arthur Cnops)</a>: chat/voice: land voice answers on question carousels (fix Skipped) <a href="https://github.com/microsoft/vscode/pull/323161" class="external-link" target="_blank">PR #323161</a></li>
<li><a href="https://github.com/cipheraxat" class="external-link" target="_blank">@cipheraxat (Akshat Anand)</a>: Fix Modern UI editor tab decoration color on full label <a href="https://github.com/microsoft/vscode/pull/325291" class="external-link" target="_blank">PR #325291</a></li>
<li><a href="https://github.com/danielrobbins" class="external-link" target="_blank">@danielrobbins (Daniel Robbins)</a>: Fix bugs related to setting the right Chat model. (Fixes Issue #323765) <a href="https://github.com/microsoft/vscode/pull/323767" class="external-link" target="_blank">PR #323767</a></li>
<li><a href="https://github.com/dobbydobap" class="external-link" target="_blank">@dobbydobap (varshitha)</a>
<ul>
<li>Fix second Rerun Last Task failing to launch for reevaluateOnRerun tasks <a href="https://github.com/microsoft/vscode/pull/324571" class="external-link" target="_blank">PR #324571</a></li>
<li>Unstick a pinned tab dragged to the start of the unpinned row <a href="https://github.com/microsoft/vscode/pull/324734" class="external-link" target="_blank">PR #324734</a></li>
</ul>
</li>
<li><a href="https://github.com/JeffreyCA" class="external-link" target="_blank">@JeffreyCA</a>: Update Fig spec for Azure Developer CLI (azd) <a href="https://github.com/microsoft/vscode/pull/321221" class="external-link" target="_blank">PR #321221</a></li>
<li><a href="https://github.com/Kaidesuyoo" class="external-link" target="_blank">@Kaidesuyoo (Kaidesuyo)</a>: fix persistent workbench UI performance degradation <a href="https://github.com/microsoft/vscode/pull/324986" class="external-link" target="_blank">PR #324986</a></li>
<li><a href="https://github.com/myselfsiddharth" class="external-link" target="_blank">@myselfsiddharth (Siddharth Mehta)</a>: debug: right-align toolbar actions in exception widget <a href="https://github.com/microsoft/vscode/pull/325077" class="external-link" target="_blank">PR #325077</a></li>
<li><a href="https://github.com/theanarkh" class="external-link" target="_blank">@theanarkh (theanarkh)</a>
<ul>
<li>workbench: fix ObjectSettingCheckboxWidget memory leaky <a href="https://github.com/microsoft/vscode/pull/323670" class="external-link" target="_blank">PR #323670</a></li>
<li>fix: make sure register handler when ipc emitter add listener <a href="https://github.com/microsoft/vscode/pull/323663" class="external-link" target="_blank">PR #323663</a></li>
</ul>
</li>
<li><a href="https://github.com/yavanosta" class="external-link" target="_blank">@yavanosta (Dmitry Guketlev)</a>: Use startColumn in growUntilVariableBoundaries <a href="https://github.com/microsoft/vscode/pull/324523" class="external-link" target="_blank">PR #324523</a></li>
</ul>
<h3 id="_issue-tracking" data-needslink="_issue-tracking">Issue tracking</h3>
<p>Contributions to our issue tracking:</p>
<ul>
<li><a href="https://github.com/gjsjohnmurray" class="external-link" target="_blank">@gjsjohnmurray (John Murray)</a></li>
<li><a href="https://github.com/RedCMD" class="external-link" target="_blank">@RedCMD (RedCMD)</a></li>
<li><a href="https://github.com/IllusionMH" class="external-link" target="_blank">@IllusionMH (Andrii Dieiev)</a></li>
<li><a href="https://github.com/albertosantini" class="external-link" target="_blank">@albertosantini (Alberto Santini)</a></li>
<li><a href="https://github.com/dobbydobap" class="external-link" target="_blank">@dobbydobap (varshitha)</a></li>
<li><a href="https://github.com/hogiSp" class="external-link" target="_blank">@hogiSp (hogiSp)</a></li>
</ul>
<hr>
<p>We really appreciate people trying our new features as soon as they are ready, so check back here often and learn what's new.</p>
<blockquote><p>If you'd like to read release notes for previous VS Code versions, go to <a href="https://code.visualstudio.com/updates">Updates</a> on <a href="https://code.visualstudio.com">code.visualstudio.com</a>.</p>
</blockquote><p><a id="scroll-to-top" role="button" title="Scroll to top" aria-label="scroll to top" href="#"><span class="icon"></span></a></p>

                <div class="feedback" data-edit-url="https://vscode.dev/github/microsoft/vscode-docs/blob/main/release-notes/v1_129.md"></div>
            </main>
            
            <!-- Right sidebar - On This Page -->
            <aside class="docs-right-sidebar hidden-xs">
                <nav id="docs-subnavbar" aria-label="On Page">
                    
                    <h4><span class="sr-only">On this page there are 6 sections</span><span
                            aria-hidden="true">On this page</span></h4>
                    <ul class="nav">
                        
                        <li><a href="#_agents">Agents</a></li>
                        
                        <li><a href="#_chat">Chat</a></li>
                        
                        <li><a href="#_editor-experience">Editor experience</a></li>
                        
                        <li><a href="#_authentication">Authentication</a></li>
                        
                        <li><a href="#_proposed-apis">Proposed APIs</a></li>
                        
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
						<img src="/assets/ic