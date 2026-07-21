---
source_url: https://code.visualstudio.com/updates/v1_127
ingested: 2026-07-17
sha256: f5a2486c3415ee9bc8c21242e3621344848ffaf0215e6fc93900d02fd5264480
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

	<meta name="description" content="Learn what is new in Visual Studio Code 1.127" />
<meta name="keywords" content="" />
<!-- Twitter and Facebook OpenGraph Metadata-->
<meta name="twitter:card" content="summary_large_image" />
<meta property="og:url" content="https://code.visualstudio.com/updates/v1_127" />
<meta property="og:type" content="article" />
<meta property="og:title" content="Visual Studio Code 1.127" />
<meta property="og:description" content="Learn what is new in Visual Studio Code 1.127" />

<meta property="og:image" content="https://code.visualstudio.com/assets/updates/1_127/release-highlights.webp" />



	<link rel="shortcut icon" href="/assets/favicon.ico" sizes="128x128" />
	<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">

	<title>Visual Studio Code 1.127</title>

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
            		
            			<li class="active">
            				<a href="/updates/v1_127" aria-label="Current Page: 1.127">1.127</a>
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
            		
            			<option value="/updates/v1_128" >1.128</option>
            		
            			<option value="/updates/v1_127" selected>1.127</option>
            		
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
                <h1>Visual Studio Code 1.127</h1>
<p>Follow us on <a href="https://www.linkedin.com/showcase/vs-code" class="external-link" target="_blank">LinkedIn</a>, <a href="https://go.microsoft.com/fwlink/?LinkID=533687" class="external-link" target="_blank">X</a>, <a href="https://bsky.app/profile/vscode.dev" class="external-link" target="_blank">Bluesky</a></p>
<hr>
<p><em>Release date: July 1, 2026</em></p>
<p>Downloads: Windows: <a href="https://update.code.visualstudio.com/1.127.0/win32-x64-user/stable">x64</a> <a href="https://update.code.visualstudio.com/1.127.0/win32-arm64-user/stable">Arm64</a> | Mac: <a href="https://update.code.visualstudio.com/1.127.0/darwin-universal-dmg/stable">Universal</a> <a href="https://update.code.visualstudio.com/1.127.0/darwin-x64-dmg/stable">Intel</a> <a href="https://update.code.visualstudio.com/1.127.0/darwin-arm64-dmg/stable">silicon</a> | Linux: <a href="https://update.code.visualstudio.com/1.127.0/linux-deb-x64/stable">deb</a> <a href="https://update.code.visualstudio.com/1.127.0/linux-rpm-x64/stable">rpm</a> <a href="https://update.code.visualstudio.com/1.127.0/linux-x64/stable">tarball</a> <a href="https://code.visualstudio.com/docs/supporting/faq#_previous-release-versions">Arm</a> <a href="https://update.code.visualstudio.com/1.127.0/linux-snap-x64/stable">snap</a></p>
<hr>
<p>Welcome to the 1.127 release of Visual Studio Code. This release brings agents that can build and test web apps in the browser, safer per-site browsing, and new ways to keep busy agent sessions organized.</p>
<ul>
<li>
<p><a href="#_agent-tools-are-generally-available">Browser tools for agents</a>: Let agents open pages, take screenshots, and click through to validate their own work, now generally available.</p>
</li>
<li>
<p><a href="#_camera-location-devices-and-more">Per-site browser permissions</a>: Grant pages access to the camera, location, devices, and more, with a prompt for each site.</p>
</li>
<li>
<p><a href="#_use-groups-to-organize-sessions">Agent sessions</a>: Group related sessions and drag and drop to arrange a busy Agents window.</p>
</li>
<li>
<p><a href="#_chat-input-banners">Chat input banners</a>: Act on failing CI checks and incoming pull request comments without leaving the conversation.</p>
</li>
<li>
<p><a href="#_subagent-credits">Subagent credits</a>: Hover over a subagent to see the cost of the work it handled.</p>
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
      <li><a href="#cost-management">Cost management</a></li>
      <li><a href="#chat">Chat</a></li>
      <li><a href="#language-models">Language models</a></li>
      <li><a href="#integrated-browser">Integrated browser</a></li>
      <li><a href="#enterprise">Enterprise</a></li>
      <li><a href="#deprecated-features-and-settings">Deprecated features and settings</a></li>
      <li><a href="#thank-you">Thank you</a></li>
    </ul>
  </nav>
  <div class="notes-main">
Navigation End -->
<h2 id="_agents" data-needslink="_agents">Agents</h2>
<h3 id="_agents-window-preview" data-needslink="_agents-window-preview">Agents window (Preview)</h3>
<p>The <a href="https://code.visualstudio.com/docs/agents/agents-window">Agents window</a> is a dedicated companion window optimized for exploring, iterating on, and reviewing agent sessions across projects and machines. This release brings new ways to organize the sessions list and keep a busy list of sessions manageable.</p>
<h4 id="_use-groups-to-organize-sessions" data-needslink="_use-groups-to-organize-sessions">Use groups to organize sessions</h4>
<p>When you run several agent sessions at once, the sessions list can grow quickly and become hard to scan. You can now organize the sessions list into groups to keep related sessions together. Create your own custom groups, and collapse group headers to tidy up the list and focus on what matters.</p>
<p>Each group also offers quick actions: you can start a new session directly in a group, or mark all of its sessions as done with one action.</p>
<p><video src="/assets/updates/1_127/sessions-group.mp4" title="Video showing how to group sessions in the Agents window. The user creates a new group and drags sessions into it." autoplay controls muted></video></p>
<h4 id="_drag-and-drop-in-the-sessions-list" data-needslink="_drag-and-drop-in-the-sessions-list">Drag and drop in the sessions list</h4>
<p>The sessions list now supports drag and drop to further organize your sessions:</p>
<ul>
<li>Reorder sessions by dragging them up or down</li>
<li>Drag session group and workspace headers to rearrange the list</li>
<li>Drag a session onto a group to add it to that group</li>
<li>Drop a session onto the <strong>Pinned</strong> section to pin it</li>
<li>Select multiple sessions to move them together as a block</li>
</ul>
<p><video src="/assets/updates/1_127/sessions-dnd.mp4" title="Video showing how to drag and drop sessions in the Agents window." autoplay controls muted></video></p>
<h4 id="_chat-input-banners" data-needslink="_chat-input-banners">Chat input banners</h4>
<p>When a coding agent session has an open pull request, the Agents window displays a banner directly above the chat input, letting you act on failing checks and incoming feedback right where you're working. Each banner provides a single action to fix or view the issue without leaving your conversation:</p>
<ul>
<li><strong>CI failures:</strong> When checks on the pull request fail, a banner shows how many checks failed (for example, &quot;2 of 5 checks failed&quot;) with quick actions: <strong>Fix Checks</strong> starts an agent fix, and <strong>Reveal Checks</strong> opens the failing checks in the Changes view.</li>
</ul>
<p><video src="/assets/updates/1_127/input-banner-ci.mp4" title="Video showing a banner above the chat input with the text '8 out of 22 checks failed, 7 pending', with actions to reveal and fix failed checks." autoplay controls muted></video></p>
<ul>
<li><strong>Pull request comments:</strong> When new review comments come in, a banner shows the comment count with actions: <strong>Address Comments</strong> hands them to the agent, and <strong>Reveal Comments</strong> opens them in the editor.</li>
</ul>
<p><video src="/assets/updates/1_127/input-banner-pr.mp4" title="Video showing a banner above the chat input with two pull request comments, with actions to reveal and address the comments." autoplay controls muted></video></p>
<h4 id="_onboarding-tours-experimental" data-needslink="_onboarding-tours-experimental">Onboarding tours (Experimental)</h4>
<p>Getting started with agents can be daunting if you're not sure what they can do for you. Onboarding tours are now available in the Agents window to help you get up to speed quickly. These guided walkthroughs highlight key capabilities and show you how to make the most of working with agents, helping you discover the best ways to delegate tasks and stay productive from day one.</p>
<p>We're experimenting with these tours to find the most helpful way to introduce new users to the experience.</p>
<p><video src="/assets/updates/1_127/onboarding.mp4" title="Video showing an onboarding example in the Agents window. The user sends a message, sees a pulse animation on the new session button, and reviews spotlighted workspace and isolation pickers." autoplay controls muted></video></p>
<h4 id="_editor-gutter-feedback-when-reviewing-agent-changes" data-needslink="_editor-gutter-feedback-when-reviewing-agent-changes">Editor gutter feedback when reviewing agent changes</h4>
<p>When reviewing an agent's changes, pointing it at the exact code you want changed should be effortless. You can now leave feedback directly from the editor gutter: hovering over a line reveals an <strong>Add Feedback</strong> glyph in the gutter, and selecting it drops a comment on that line, making it quicker to direct an agent to a specific spot in the code.</p>
<p>This release also brings a round of polish to the agent feedback experience, with refinements to the feedback input, hover behavior, and overall visual consistency.</p>
<p><video src="/assets/updates/1_127/agent-feedback-add-action.mp4" title="Video showing how to add feedback to an agent's changes. The user hovers over a line, selects the add feedback glyph, and enters a comment." autoplay controls muted></video></p>
<h4 id="_better-pull-request-titles-and-descriptions-from-session-context" data-needslink="_better-pull-request-titles-and-descriptions-from-session-context">Better pull request titles and descriptions from session context</h4>
<p>Creating a pull request from the Agents window used to produce generic titles and descriptions that often needed manual editing. The <strong>Create Pull Request</strong> button now uses the session context to generate the pull request title and description, resulting in more accurate and descriptive pull requests that better reflect the work done in the session.</p>
<h4 id="_multi-chat-sessions" data-needslink="_multi-chat-sessions">Multi-chat sessions</h4>
<p>Multi-chat sessions let you run several chats within a single agent host Copilot session. This release builds on that foundation with the following improvements.</p>
<h5>Close, reopen, and delete chats</h5>
<p>Create new chats from the <strong>+ New Chat</strong> button in the session header. Once more than one chat is open, a tab strip appears with a trailing <strong>+</strong> to add more. Closing a chat with the <strong>X</strong> on its tab hides it rather than discarding it—bring it back from the <strong>Conversations</strong> dropdown, where each chat has a checkbox to show or hide it. To permanently remove a chat, open its tab context menu and select <strong>Delete Chat</strong>.</p>
<p><video src="/assets/updates/1_127/multi-chat-session-chat-actions.mp4" title="Video showing the multi-chat session tab strip with the trailing + button to add chats and the Conversations dropdown to show or hide chats." autoplay loop controls muted></video></p>
<h5>Progress and changes across all chats</h5>
<p>Previously, the session only reflected the active chat's activity, making it hard to tell whether peer chats were still working or what they had changed. Progress and file changes are now aggregated across all chats: the session shows as in-progress whenever any chat is working, each tab surfaces its own progress, and the session header Changes pill reflects the combined edits from every peer chat.</p>
<h5>Fork a conversation into a peer chat</h5>
<p>When you fork a conversation in a multi-chat session, the fork now creates a new peer chat in the same session instead of a brand-new top-level session. The forked chat inherits the conversation up to the fork point, runs independently from its siblings, and gets an auto-generated title. Single-chat and non-agent-host sessions keep the existing behavior of forking into a new session.</p>
<p><video src="/assets/updates/1_127/sessions-fork-chat.mp4" title="Video showing forking a conversation in a multi-chat session, which creates a new peer chat in the same session." autoplay loop controls muted></video></p>
<h4 id="_session-layout" data-needslink="_session-layout">Session layout</h4>
<h5>Consistent pills in the session header</h5>
<p>The row of actions under the session title now renders consistently as uniform, compact secondary button pills. A <strong>Workspace pill</strong> shows the workspace icon (cloud, folder, or worktree depending on the workspace kind) and label, with long names truncated. The <strong>Changes pill</strong> (<code>N files +X -Y</code>) reads and opens the session's default changeset, keeping its count and the multi-file diff it opens in agreement for both Copilot and agent-host providers.</p>
<p><img src="/assets/updates/1_127/session-header-pills.webp" alt="Screenshot showing the consistent Workspace and Changes pills in the session header." width="1946" height="208" loading="lazy"></p>
<h5>Focus moves to the chat input when switching sessions</h5>
<p>When you open a session in the Agents window, keyboard focus now lands in the chat input, ready for you to start typing immediately, even when the session has editors open or a Changes view that loads. Highlighting entries in the sessions list with the keyboard does not move focus until you actually open a session.</p>
<p><video src="/assets/updates/1_127/sessions-focus-management.mp4" title="Video showing keyboard focus landing in the chat input when switching to a session in the Agents window." autoplay loop controls muted></video></p>
<h5>Responsive sessions sidebar (Experimental)</h5>
<p><strong>Setting</strong>: <span class="setting"><span class="setting-dropdown" data-setting-id="sessions.layout.autoCollapseSessionsSidebar">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      sessions.layout.autoCollapseSessionsSidebar
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
<p>On a narrow window, showing the editor, side panel, and sessions sidebar at once leaves little room to work. When enabled, the Agents window automatically hides the sessions sidebar when the window is narrow and both the editor and side panel are open, and shows it again when there is room. It respects a manual close and suspends the behavior when multiple sessions are shown at once.</p>
<p><video src="/assets/updates/1_127/sessions-adaptive-layout.mp4" title="Video showing the Agents window automatically hiding the sessions sidebar when the window becomes narrow and showing it again when there is room." autoplay loop controls muted></video></p>
<h3 id="_troubleshoot-agent-behavior-with-troubleshoot" data-needslink="_troubleshoot-agent-behavior-with-troubleshoot">Troubleshoot agent behavior with /troubleshoot</h3>
<p>The troubleshoot skill, invoked with the <code>/troubleshoot</code> command, helps diagnose chat issues by analyzing chat session logs and surfacing insights into the agent's behavior. Use it to investigate why custom instructions are ignored or why responses are slow.</p>
<p>In this release, you can use <code>/troubleshoot</code> to diagnose agent host sessions, including local and remote sessions. In the Agents window, type <code>/troubleshoot</code> in the chat input followed by <code>#session</code>, select the session you want to troubleshoot, and add a question or description of the issue you're experiencing.</p>
<p><img src="/assets/updates/1_127/ahptroubleshoot.jpg" alt="Screenshot showing troubleshoot results for an agent host session in the Agents window." width="1634" height="719" loading="lazy"></p>
<h2 id="_cost-management" data-needslink="_cost-management">Cost management</h2>
<h3 id="_subagent-credits" data-needslink="_subagent-credits">Subagent credits</h3>
<p>When an agent delegates work to a subagent, it can be difficult to know the cost of the delegated work. To make this more transparent, you can now hover over a subagent section in the chat response to see the AI credits used by that subagent.</p>
<p><img src="/assets/updates/1_127/subagent_cost_hover.webp" alt="Screenshot showing the credit usage hover for a subagent section in a chat response." width="1554" height="548" loading="lazy"></p>
<h2 id="_chat" data-needslink="_chat">Chat</h2>
<h3 id="_sandboxing-for-terminal-commands-on-macos-and-linux" data-needslink="_sandboxing-for-terminal-commands-on-macos-and-linux">Sandboxing for terminal commands on macOS and Linux</h3>
<p>Approving every agent-invoked terminal command quickly becomes tedious. Starting with this release, we're rolling out sandboxing for terminal commands on macOS and Linux: commands run with network access blocked and filesystem access restricted, letting the agent work with fewer prompts.</p>
<p>The agent only asks for approval when a command needs to elevate and run outside the sandbox. To learn more, see <a href="https://code.visualstudio.com/docs/agents/concepts/trust-and-safety#_agent-sandboxing">Agent sandboxing</a>.</p>
<p>You can turn this off via the Permissions drop-down:</p>
<p><img src="/assets/updates/1_127/sandboxing-toggle.webp" alt="Screenshot showing the sandboxing toggle available in the Default Approvals mode." width="500" height="375" loading="lazy"></p>
<h2 id="_language-models" data-needslink="_language-models">Language models</h2>
<h3 id="_deprecation-of-the-built-in-ollama-provider" data-needslink="_deprecation-of-the-built-in-ollama-provider">Deprecation of the built-in Ollama provider</h3>
<p>Model providers can contribute models for the VS Code chat experience via an extension. By using an extension, providers can give you faster support for new models and capabilities than a built-in provider could offer.</p>
<p>Ollama now has an <a href="https://marketplace.visualstudio.com/publishers/Ollama" class="external-link" target="_blank">official VS Code extension</a>, which is the recommended way to use local Ollama models in chat.</p>
<p>As a result, the built-in Ollama provider is now deprecated. If you're using the built-in provider to run local models with <a href="https://code.visualstudio.com/docs/copilot/customization/language-models#_bring-your-own-language-model-key">Bring Your Own Key (BYOK)</a>, install the official extension and remove the built-in provider to continue using your Ollama models without interruption. The following video shows how to remove the deprecated provider.</p>
<p><video src="/assets/updates/1_127/ollama-deprecation.mp4" title="Video showing how to remove the deprecated built-in Ollama provider." autoplay controls muted></video></p>
<h2 id="_integrated-browser" data-needslink="_integrated-browser">Integrated browser</h2>
<h3 id="_camera-location-devices-and-more" data-needslink="_camera-location-devices-and-more">Camera, location, devices, and more</h3>
<p>The integrated browser now supports per-site permissions. This enables pages to use more web APIs, including:</p>
<ul>
<li>Geolocation</li>
<li>Camera and microphone</li>
<li>Sensors, such as accelerometer and gyroscope</li>
<li>Clipboard</li>
<li>Devices, such as Bluetooth, USB, serial, and HID</li>
</ul>
<p>When a page requests a permission, VS Code prompts you to allow or deny the request, as you would expect in a traditional browser.</p>
<p><img src="/assets/updates/1_127/browser-permission-prompt.webp" alt="Screenshot showing a system dialog where app.zoom.us requests microphone access, with options to Allow, Block, or Cancel." width="400" height="313" loading="lazy"></p>
<p>Manage permissions for the current site from the <strong>Site Permissions</strong> browser menu item.</p>
<h3 id="_agent-tools-are-generally-available" data-needslink="_agent-tools-are-generally-available">Agent tools are generally available</h3>
<p><strong>Setting</strong>: <span class="setting"><span class="setting-dropdown" data-setting-id="workbench.browser.enableChatTools">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      workbench.browser.enableChatTools
    </span>
    <button 
      type="button"
      class="setting-dropdown-trigger"
      aria-haspopup="menu"
      aria-expanded="false"
      aria-describedby="org-setting-tooltip-workbench-browser-enableChatTools-232"
      aria-label="Open setting in VS Code">
        <svg class="setting-dropdown-chevron" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path d="M7.976 10.072l4.357-4.357.62.618L8.284 11h-.618L3 6.333l.619-.618 4.357 4.357z"/>
        </svg>
    </button>
    <span class="setting-dropdown-menu" role="menu" aria-label="Open setting">
      <span role="menuitem" class="setting-action-item" data-version="stable" tabindex="0">Open in VS Code</span>
      <span role="menuitem" class="setting-action-item" data-version="insiders" tabindex="-1">Open in VS Code Insiders</span>
    </span>
  </span><span class="sr-only" id="org-setting-tooltip-workbench-browser-enableChatTools-232">This setting is managed at the organization level. Contact your administrator to change it.</span><span class="badge-org" data-tooltip="This setting is managed at the organization level. Contact your administrator to change it." aria-hidden="true">ORG</span></span></p>
<p>Browser tools let an agent open pages in the integrated browser, read content and console errors, take screenshots, and select, type, and navigate to verify its own work, all without an external MCP server. After several milestones in preview, browser tools are generally available and enabled by default.</p>
<p>A big thank you to everyone who ran the preview, filed issues, and shared feedback. Your testing directly shaped the per-session tab isolation, the explicit page-sharing controls, and the permission model that ship in this release.</p>
<p>Ask an agent to build and validate a web app, or follow the step-by-step <a href="https://code.visualstudio.com/docs/agents/guides/browser-agent-testing-guide">Build and test web apps with browser agent tools</a> guide to see the closed build-test-fix loop in action. For the full reference, see <a href="https://code.visualstudio.com/docs/debugtest/integrated-browser#_browser-tools-for-agents">Browser tools for agents</a>.</p>
<p>Administrators can govern browser tools through enterprise policy: disable them entirely with the <code>BrowserChatTools</code> policy, or restrict which domains agent tools can reach with agent network filtering (<code>ChatAgentNetworkFilter</code> plus allow and deny domain lists). See <a href="https://code.visualstudio.com/docs/enterprise/ai-settings#_configure-agent-network-filtering">Configure AI settings for your organization</a>.</p>
<h2 id="_enterprise" data-needslink="_enterprise">Enterprise</h2>
<h3 id="_file-based-delivery-for-managed-copilot-settings" data-needslink="_file-based-delivery-for-managed-copilot-settings">File-based delivery for managed Copilot settings</h3>
<p>Administrators can now deliver managed GitHub Copilot settings from a JSON file on disk, in addition to the <a href="https://code.visualstudio.com/updates/v1_125#_native-mdm-delivery-for-managed-copilot-settings">native MDM channels</a> and the account-based enterprise settings file.</p>
<p>This gives organizations a straightforward way to apply policies on machines that aren't enrolled in a device management solution, or where provisioning a file through existing tooling (such as a configuration management system or imaging pipeline) is simpler than authoring native MDM payloads.</p>
<p>VS Code reads a <code>managed-settings.json</code> file from a well-known per-OS location.  This file is honored only when MDM or account-based enterprise settings are not present.</p>
<ul>
<li><strong>macOS</strong>: <code>/Library/Application Support/GitHubCopilot/managed-settings.json</code></li>
<li><strong>Linux</strong>: <code>/etc/github-copilot/managed-settings.json</code></li>
<li><strong>Windows</strong>: <code>%ProgramFiles%\GitHubCopilot\managed-settings.json</code></li>
</ul>
<p>The file contains a JSON object using the same schema an administrator authors through GitHub.com, for example:</p>
<pre class="shiki" data-lang="json" shiki-themes dark-plus light-plus" style="--shiki-dark:#D4D4D4;--shiki-light:#000000;--shiki-dark-bg:#1E1E1E;--shiki-light-bg:#FFFFFF" tabindex="0"><code><span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">{</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">  "permissions"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: {</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">    "disableBypassPermissionsMode"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#CE9178;--shiki-light:#A31515">"disable"</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">  },</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">  "enabledPlugins"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: {</span></span>
<span class="line"><span style="--shiki-dark:#9CDCFE;--shiki-light:#0451A5">    "plugin@marketplace"</span><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">: </span><span style="--shiki-dark:#569CD6;--shiki-light:#0000FF">false</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">  }</span></span>
<span class="line"><span style="--shiki-dark:#D4D4D4;--shiki-light:#000000">}</span></span>
<span class="line"></span></code></pre>
<p>To learn more, see GitHub's documentation on <a href="https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/configure-enterprise-plugin-standards" class="external-link" target="_blank">Enterprise managed client settings</a>.</p>
<h2 id="_deprecated-features-and-settings" data-needslink="_deprecated-features-and-settings">Deprecated features and settings</h2>
<p>None</p>
<h2 id="_thank-you" data-needslink="_thank-you">Thank you</h2>
<p>Contributions to <code>vscode</code>:</p>
<ul>
<li><a href="https://github.com/aaronpowell" class="external-link" target="_blank">@aaronpowell (Aaron Powell)</a>: Handle plugin marketplace pull recovery <a href="https://github.com/microsoft/vscode/pull/318270" class="external-link" target="_blank">PR #318270</a></li>
<li><a href="https://github.com/gjsjohnmurray" class="external-link" target="_blank">@gjsjohnmurray (John Murray)</a>
<ul>
<li>Allow disabling AuthenticationProvider extension for workspace if not used by Settings Sync <a href="https://github.com/microsoft/vscode/pull/320415" class="external-link" target="_blank">PR #320415</a></li>
<li>:lipstick: correct command capitalization in /causedByExtension response <a href="https://github.com/microsoft/vscode/pull/298925" class="external-link" target="_blank">PR #298925</a></li>
</ul>
</li>
<li><a href="https://github.com/rfeltis" class="external-link" target="_blank">@rfeltis (Ralph Feltis)</a>
<ul>
<li>Add quota checkpoint to notification telemetry <a href="https://github.com/microsoft/vscode/pull/322767" class="external-link" target="_blank">PR #322767</a></li>
<li>Add chat quota trajectory nudge <a href="https://github.com/microsoft/vscode/pull/320683" class="external-link" target="_blank">PR #320683</a></li>
</ul>
</li>
<li><a href="https://github.com/romalpani" class="external-link" target="_blank">@romalpani (Rohan Malpani)</a>: Give ask-questions carousel a visible box in the Agents window <a href="https://github.com/microsoft/vscode/pull/322188" class="external-link" target="_blank">PR #322188</a></li>
<li><a href="https://github.com/Sid200026" class="external-link" target="_blank">@Sid200026 (Siddharth Singha Roy)</a>: Add chatSessionId to chat.modelChange telemetry <a href="https://github.com/microsoft/vscode/pull/322579" class="external-link" target="_blank">PR #322579</a></li>
<li><a href="https://github.com/tamuratak" class="external-link" target="_blank">@tamuratak (Takashi Tamura)</a>: Fix: CancellationToken not propagating to <code>provideLanguageModelChatResponse</code> on chat stop <a href="https://github.com/microsoft/vscode/pull/319098" class="external-link" target="_blank">PR #319098</a></li>
<li><a href="https://github.com/yavanosta" class="external-link" target="_blank">@yavanosta (Dmitry Guketlev)</a>: Fix <code>handleEndOfLifetime</code> <code>supersededBy</code> tracking for inline completions <a href="https://github.com/microsoft/vscode/pull/320143" class="external-link" target="_blank">PR #320143</a></li>
<li><a href="https://github.com/yulia-vasyura" class="external-link" target="_blank">@yulia-vasyura</a>: Renamed &quot;Apply Update...&quot; command to &quot;Apply Update from File...&quot;. <a href="https://github.com/microsoft/vscode/pull/322504" class="external-link" target="_blank">PR #322504</a></li>
</ul>
<p>Contributions to <code>node-pty</code>:</p>
<ul>
<li><a href="https://github.com/codebytere-ant" class="external-link" target="_blank">@codebytere-ant (Shelley Vohr)</a>
<ul>
<li>fix: close kqueue fd in SetupExitCallback on macOS <a href="https://github.com/microsoft/node-pty/pull/931" class="external-link" target="_blank">PR #931</a></li>
<li>fix: surface CreateProcessW failures as 'exit' instead of uncaughtException on Windows <a href="https://github.com/microsoft/node-pty/pull/934" class="external-link" target="_blank">PR #934</a></li>
<li>fix: close pipe handles and free attribute list when conpty spawn fails <a href="https://github.com/microsoft/node-pty/pull/935" class="external-link" target="_blank">PR #935</a></li>
</ul>
</li>
</ul>
<h3 id="_issue-tracking" data-needslink="_issue-tracking">Issue tracking</h3>
<p>Contributions to our issue tracking:</p>
<ul>
<li><a href="https://github.com/RedCMD" class="external-link" target="_blank">@RedCMD (RedCMD)</a></li>
<li><a href="https://github.com/gjsjohnmurray" class="external-link" target="_blank">@gjsjohnmurray (John Murray)</a></li>
<li><a href="https://github.com/mantasu" class="external-link" target="_blank">@mantasu (Mantas)</a></li>
<li><a href="https://github.com/davemcom" class="external-link" target="_blank">@davemcom (DaveM.)</a></li>
</ul>
<hr>
<p>We really appreciate people trying our new features as soon as they are ready, so check back here often and learn what's new.</p>
<blockquote><p>If you'd like to read release notes for previous VS Code versions, go to <a href="https://code.visualstudio.com/updates">Updates</a> on <a href="https://code.visualstudio.com">code.visualstudio.com</a>.</p>
</blockquote><p><a id="scroll-to-top" role="button" title="Scroll to top" aria-label="scroll to top" href="#"><span class="icon"></span></a></p>

                <div class="feedback" data-edit-url="https://vscode.dev/github/microsoft/vscode-docs/blob/main/release-notes/v1_127.md"></div>
            </main>
            
            <!-- Right sidebar - On This Page -->
            <aside class="docs-right-sidebar hidden-xs">
                <nav id="docs-subnavbar" aria-label="On Page">
                    
                    <h4><span class="sr-only">On this page there are 8 sections</span><span
                            aria-hidden="true">On this page</span></h4>
                    <ul class="nav">
                        
                        <li><a href="#_agents">Agents</a></li>
                        
                        <li><a href="#_cost-management">Cost management</a></li>
                        
                        <li><a href="#_chat">Chat</a></li>
                        
                        <li><a href="#_language-models">Language models</a></li>
                        
                        <li><a href="#_integrated-browser">Integrated browser</a></li>
                        
                        <li><a href="#_enterprise">Enterprise</a></li>
                        
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
							<a href="https://bsky.ap