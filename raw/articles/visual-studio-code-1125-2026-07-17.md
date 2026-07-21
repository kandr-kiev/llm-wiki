---
source_url: https://code.visualstudio.com/updates/v1_125
ingested: 2026-07-17
sha256: f3c751e264bbca3f4d27ada05368c9fa83f314463b84a82fbf29b9bf30aa6720
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

	<meta name="description" content="Learn what's new in Visual Studio Code 1.125" />
<meta name="keywords" content="" />
<!-- Twitter and Facebook OpenGraph Metadata-->
<meta name="twitter:card" content="summary_large_image" />
<meta property="og:url" content="https://code.visualstudio.com/updates/v1_125" />
<meta property="og:type" content="article" />
<meta property="og:title" content="Visual Studio Code 1.125" />
<meta property="og:description" content="Learn what's new in Visual Studio Code 1.125" />

<meta property="og:image" content="https://code.visualstudio.com/assets/updates/1_125/release-highlights.webp" />



	<link rel="shortcut icon" href="/assets/favicon.ico" sizes="128x128" />
	<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">

	<title>Visual Studio Code 1.125</title>

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
            		
            			<li >
            				<a href="/updates/v1_126" >1.126</a>
            			</li>
            		
            			<li class="active">
            				<a href="/updates/v1_125" aria-label="Current Page: 1.125">1.125</a>
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
            		
            			<option value="/updates/v1_126" >1.126</option>
            		
            			<option value="/updates/v1_125" selected>1.125</option>
            		
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
                <h1>Visual Studio Code 1.125</h1>
<p>Follow us on <a href="https://www.linkedin.com/showcase/vs-code" class="external-link" target="_blank">LinkedIn</a>, <a href="https://go.microsoft.com/fwlink/?LinkID=533687" class="external-link" target="_blank">X</a>, <a href="https://bsky.app/profile/vscode.dev" class="external-link" target="_blank">Bluesky</a></p>
<hr>
<p><em>Release date: June 17, 2026</em></p>
<p><strong>Update 1.125.1</strong>: The update addresses these <a href="https://github.com/microsoft/vscode/issues?q=is%3Aissue+is%3Aclosed+milestone%3A1.125.1" class="external-link" target="_blank">issues</a>.</p>
<p>Downloads: Windows: <a href="https://update.code.visualstudio.com/1.125.1/win32-x64-user/stable">x64</a> <a href="https://update.code.visualstudio.com/1.125.1/win32-arm64-user/stable">Arm64</a> | Mac: <a href="https://update.code.visualstudio.com/1.125.1/darwin-universal-dmg/stable">Universal</a> <a href="https://update.code.visualstudio.com/1.125.1/darwin-x64-dmg/stable">Intel</a> <a href="https://update.code.visualstudio.com/1.125.1/darwin-arm64-dmg/stable">silicon</a> | Linux: <a href="https://update.code.visualstudio.com/1.125.1/linux-deb-x64/stable">deb</a> <a href="https://update.code.visualstudio.com/1.125.1/linux-rpm-x64/stable">rpm</a> <a href="https://update.code.visualstudio.com/1.125.1/linux-x64/stable">tarball</a> <a href="https://code.visualstudio.com/docs/supporting/faq#_previous-release-versions">Arm</a> <a href="https://update.code.visualstudio.com/1.125.1/linux-snap-x64/stable">snap</a></p>
<hr>
<p>Welcome to the 1.125 release of Visual Studio Code. This release brings a smarter integrated browser, more control over extension updates, and stronger enterprise management for Copilot.</p>
<ul>
<li>
<p><a href="#_install-model-providers-from-the-language-models-editor">Install model providers</a>: Discover and install extra models via the Marketplace.</p>
</li>
<li>
<p><a href="#_integrated-browser">Integrated browser</a>: Search the web and securely browse over remote connections without leaving VS Code.</p>
</li>
<li>
<p><a href="#_configurable-extension-auto-update-delay">Configurable auto-update delay</a>: Choose how long VS Code waits before installing extension updates.</p>
</li>
<li>
<p><a href="#_native-mdm-delivery-for-managed-copilot-settings">Copilot policies</a>: Deliver managed Copilot settings through your existing device management tooling.</p>
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
      <li><a href="#language-models">Language Models</a></li>
      <li><a href="#integrated-browser">Integrated Browser</a></li>
      <li><a href="#editor-experience">Editor Experience</a></li>
      <li><a href="#extension-authoring">Extension Authoring</a></li>
      <li><a href="#enterprise">Enterprise</a></li>
      <li><a href="#deprecated-features-and-settings">Deprecated features and settings</a></li>
      <li><a href="#thank-you">Thank you</a></li>
    </ul>
  </nav>
  <div class="notes-main">
Navigation End -->
<h2 id="_agents" data-needslink="_agents">Agents</h2>
<h3 id="_view-your-additional-spend-usage-in-vs-code" data-needslink="_view-your-additional-spend-usage-in-vs-code">View your additional spend usage in VS Code</h3>
<p>To make sure you stay ahead of overage charges, the Copilot status dashboard now shows the percentage of your additional Copilot budget that you've consumed, so you can adjust your usage before you hit your configured limit.</p>
<p><img src="/assets/updates/1_125/additional_budget.webp" alt="Screenshot showing additional spend limits in the Copilot status dashboard." width="500" height="514" loading="lazy"></p>
<p>You can view detailed usage and manage your additional spend in the <a href="https://github.com/settings/copilot/features" class="external-link" target="_blank">Copilot settings</a>.</p>
<h2 id="_language-models" data-needslink="_language-models">Language Models</h2>
<h3 id="_install-model-providers-from-the-language-models-editor" data-needslink="_install-model-providers-from-the-language-models-editor">Install model providers from the Language Models editor</h3>
<p>Beyond Bring Your Own Key (BYOK) models, extensions can contribute their own model providers. Previously, to find such an extension, you needed to know the right tag (<code>language-models</code>) to search for in the Extensions view.</p>
<p>Now the Language Models editor has an <strong>Install Model Providers</strong> button that opens the Extensions view filtered to extensions that contribute model providers, making it easier to discover and install them. After you install a provider, its models appear in the model picker alongside any others you have configured.</p>
<p><video src="/assets/updates/1_125/install-model-provider.mp4" title="Video showing the Install Model Providers button in the Language Models editor opening the Extensions view filtered to model provider extensions." autoplay loop controls muted></video></p>
<p>To learn more, see the <a href="https://code.visualstudio.com/docs/agent-customization/language-models">language models documentation</a>.</p>
<h2 id="_integrated-browser" data-needslink="_integrated-browser">Integrated Browser</h2>
<h3 id="_web-search-from-address-bar" data-needslink="_web-search-from-address-bar">Web search from address bar</h3>
<p><strong>Setting</strong>: <span class="setting"><span class="setting-dropdown" data-setting-id="workbench.browser.searchEngine">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      workbench.browser.searchEngine
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
<p>Look up information without leaving VS Code: type a query into the integrated browser's address bar and it runs against your configured search engine, the same way it would in a standalone browser. Use the <span class="setting"><span class="setting-dropdown" data-setting-id="workbench.browser.searchEngine">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      workbench.browser.searchEngine
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
  </span></span> setting to pick which search engine to use.</p>
<p><img src="/assets/updates/1_125/browser-search.webp" alt="Screenshot showing a web search from the integrated browser's address bar." width="565" height="127" loading="lazy"></p>
<h3 id="_browse-over-remote-connections-preview" data-needslink="_browse-over-remote-connections-preview">Browse over remote connections (Preview)</h3>
<p><strong>Setting</strong>: <span class="setting"><span class="setting-dropdown" data-setting-id="workbench.browser.enableRemoteProxy">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      workbench.browser.enableRemoteProxy
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
<p>When the integrated browser is opened in a remote workspace, web traffic over HTTP(S) can now be proxied via the remote connection. This lets you securely connect to any ports or services that are only accessible from the remote machine.</p>
<p>This is a preview feature, so you might encounter bugs. Enable the <span class="setting"><span class="setting-dropdown" data-setting-id="workbench.browser.enableRemoteProxy">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      workbench.browser.enableRemoteProxy
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
  </span></span> setting to try it out, and file any issues you encounter in the <a href="https://github.com/microsoft/vscode/issues" class="external-link" target="_blank">VS Code repository</a>.</p>
<h3 id="_better-agentic-interaction-with-forwarded-ports" data-needslink="_better-agentic-interaction-with-forwarded-ports">Better agentic interaction with forwarded ports</h3>
<p>If you have forwarded a port in a remote workspace, previously agents could have difficulty opening the browser due to a potentially different port number.</p>
<p>Now, if an agent requests a port that has been forwarded (and the remote proxy is not enabled), the URL is rewritten and the agent is notified of the change.</p>
<h2 id="_editor-experience" data-needslink="_editor-experience">Editor Experience</h2>
<h3 id="_extension-auto-update-setting" data-needslink="_extension-auto-update-setting">Extension auto-update setting</h3>
<p><strong>Setting</strong>: <span class="setting"><span class="setting-dropdown" data-setting-id="extensions.autoUpdate">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      extensions.autoUpdate
    </span>
    <button 
      type="button"
      class="setting-dropdown-trigger"
      aria-haspopup="menu"
      aria-expanded="false"
      aria-describedby="org-setting-tooltip-extensions-autoUpdate-226"
      aria-label="Open setting in VS Code">
        <svg class="setting-dropdown-chevron" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path d="M7.976 10.072l4.357-4.357.62.618L8.284 11h-.618L3 6.333l.619-.618 4.357 4.357z"/>
        </svg>
    </button>
    <span class="setting-dropdown-menu" role="menu" aria-label="Open setting">
      <span role="menuitem" class="setting-action-item" data-version="stable" tabindex="0">Open in VS Code</span>
      <span role="menuitem" class="setting-action-item" data-version="insiders" tabindex="-1">Open in VS Code Insiders</span>
    </span>
  </span><span class="sr-only" id="org-setting-tooltip-extensions-autoUpdate-226">This setting is managed at the organization level. Contact your administrator to change it.</span><span class="badge-org" data-tooltip="This setting is managed at the organization level. Contact your administrator to change it." aria-hidden="true">ORG</span></span></p>
<p>You can enable or disable automatic extension updates with the <span class="setting"><span class="setting-dropdown" data-setting-id="extensions.autoUpdate">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      extensions.autoUpdate
    </span>
    <button 
      type="button"
      class="setting-dropdown-trigger"
      aria-haspopup="menu"
      aria-expanded="false"
      aria-describedby="org-setting-tooltip-extensions-autoUpdate-227"
      aria-label="Open setting in VS Code">
        <svg class="setting-dropdown-chevron" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path d="M7.976 10.072l4.357-4.357.62.618L8.284 11h-.618L3 6.333l.619-.618 4.357 4.357z"/>
        </svg>
    </button>
    <span class="setting-dropdown-menu" role="menu" aria-label="Open setting">
      <span role="menuitem" class="setting-action-item" data-version="stable" tabindex="0">Open in VS Code</span>
      <span role="menuitem" class="setting-action-item" data-version="insiders" tabindex="-1">Open in VS Code Insiders</span>
    </span>
  </span><span class="sr-only" id="org-setting-tooltip-extensions-autoUpdate-227">This setting is managed at the organization level. Contact your administrator to change it.</span><span class="badge-org" data-tooltip="This setting is managed at the organization level. Contact your administrator to change it." aria-hidden="true">ORG</span></span> setting. In this release, we simplified the setting to use <code>on</code> and <code>off</code> values. Previous values such as <code>true</code>, <code>false</code>, <code>onlyEnabledExtensions</code>, and <code>delayed</code> are migrated automatically.</p>
<p>When auto-update is enabled, VS Code updates only enabled extensions. Disabled extensions are no longer updated automatically. They update the next time you enable them.</p>
<blockquote><p><strong>Note</strong>: Administrators can centrally manage the <span class="setting"><span class="setting-dropdown" data-setting-id="extensions.autoUpdate">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      extensions.autoUpdate
    </span>
    <button 
      type="button"
      class="setting-dropdown-trigger"
      aria-haspopup="menu"
      aria-expanded="false"
      aria-describedby="org-setting-tooltip-extensions-autoUpdate-228"
      aria-label="Open setting in VS Code">
        <svg class="setting-dropdown-chevron" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path d="M7.976 10.072l4.357-4.357.62.618L8.284 11h-.618L3 6.333l.619-.618 4.357 4.357z"/>
        </svg>
    </button>
    <span class="setting-dropdown-menu" role="menu" aria-label="Open setting">
      <span role="menuitem" class="setting-action-item" data-version="stable" tabindex="0">Open in VS Code</span>
      <span role="menuitem" class="setting-action-item" data-version="insiders" tabindex="-1">Open in VS Code Insiders</span>
    </span>
  </span><span class="sr-only" id="org-setting-tooltip-extensions-autoUpdate-228">This setting is managed at the organization level. Contact your administrator to change it.</span><span class="badge-org" data-tooltip="This setting is managed at the organization level. Contact your administrator to change it." aria-hidden="true">ORG</span></span> and <span class="setting"><span class="setting-dropdown" data-setting-id="extensions.autoUpdateDelay">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      extensions.autoUpdateDelay
    </span>
    <button 
      type="button"
      class="setting-dropdown-trigger"
      aria-haspopup="menu"
      aria-expanded="false"
      aria-describedby="org-setting-tooltip-extensions-autoUpdateDelay-229"
      aria-label="Open setting in VS Code">
        <svg class="setting-dropdown-chevron" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path d="M7.976 10.072l4.357-4.357.62.618L8.284 11h-.618L3 6.333l.619-.618 4.357 4.357z"/>
        </svg>
    </button>
    <span class="setting-dropdown-menu" role="menu" aria-label="Open setting">
      <span role="menuitem" class="setting-action-item" data-version="stable" tabindex="0">Open in VS Code</span>
      <span role="menuitem" class="setting-action-item" data-version="insiders" tabindex="-1">Open in VS Code Insiders</span>
    </span>
  </span><span class="sr-only" id="org-setting-tooltip-extensions-autoUpdateDelay-229">This setting is managed at the organization level. Contact your administrator to change it.</span><span class="badge-org" data-tooltip="This setting is managed at the organization level. Contact your administrator to change it." aria-hidden="true">ORG</span></span> settings with <a href="https://code.visualstudio.com/docs/enterprise/policies">enterprise policies</a>.</p>
</blockquote><h3 id="_configurable-extension-auto-update-delay" data-needslink="_configurable-extension-auto-update-delay">Configurable extension auto-update delay</h3>
<p><strong>Setting</strong>: <span class="setting"><span class="setting-dropdown" data-setting-id="extensions.autoUpdateDelay">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      extensions.autoUpdateDelay
    </span>
    <button 
      type="button"
      class="setting-dropdown-trigger"
      aria-haspopup="menu"
      aria-expanded="false"
      aria-describedby="org-setting-tooltip-extensions-autoUpdateDelay-230"
      aria-label="Open setting in VS Code">
        <svg class="setting-dropdown-chevron" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path d="M7.976 10.072l4.357-4.357.62.618L8.284 11h-.618L3 6.333l.619-.618 4.357 4.357z"/>
        </svg>
    </button>
    <span class="setting-dropdown-menu" role="menu" aria-label="Open setting">
      <span role="menuitem" class="setting-action-item" data-version="stable" tabindex="0">Open in VS Code</span>
      <span role="menuitem" class="setting-action-item" data-version="insiders" tabindex="-1">Open in VS Code Insiders</span>
    </span>
  </span><span class="sr-only" id="org-setting-tooltip-extensions-autoUpdateDelay-230">This setting is managed at the organization level. Contact your administrator to change it.</span><span class="badge-org" data-tooltip="This setting is managed at the organization level. Contact your administrator to change it." aria-hidden="true">ORG</span></span></p>
<p>To give you more control over when extension updates are installed, you can now configure a delay for automatic extension updates. This builds on the <a href="https://code.visualstudio.com/updates/v1_123#_delayed-extension-autoupdates">delayed extension auto-updates</a> feature introduced in the previous release.</p>
<p>Use the <span class="setting"><span class="setting-dropdown" data-setting-id="extensions.autoUpdateDelay">
    <span class="setting-link-main">
      <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>
      extensions.autoUpdateDelay
    </span>
    <button 
      type="button"
      class="setting-dropdown-trigger"
      aria-haspopup="menu"
      aria-expanded="false"
      aria-describedby="org-setting-tooltip-extensions-autoUpdateDelay-231"
      aria-label="Open setting in VS Code">
        <svg class="setting-dropdown-chevron" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path d="M7.976 10.072l4.357-4.357.62.618L8.284 11h-.618L3 6.333l.619-.618 4.357 4.357z"/>
        </svg>
    </button>
    <span class="setting-dropdown-menu" role="menu" aria-label="Open setting">
      <span role="menuitem" class="setting-action-item" data-version="stable" tabindex="0">Open in VS Code</span>
      <span role="menuitem" class="setting-action-item" data-version="insiders" tabindex="-1">Open in VS Code Insiders</span>
    </span>
  </span><span class="sr-only" id="org-setting-tooltip-extensions-autoUpdateDelay-231">This setting is managed at the organization level. Contact your administrator to change it.</span><span class="badge-org" data-tooltip="This setting is managed at the organization level. Contact your administrator to change it." aria-hidden="true">ORG</span></span> setting to configure the delay in hours. By default, VS Code waits two hours before installing extension updates. The delay only applies when auto-update is enabled.</p>
<h2 id="_extension-authoring" data-needslink="_extension-authoring">Extension Authoring</h2>
<h3 id="_language-server-protocol" data-needslink="_language-server-protocol">Language Server Protocol</h3>
<p>Extension authors who build language servers can now adopt the latest protocol features by updating to <a href="https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/" class="external-link" target="_blank">version 3.18 of the Language Server Protocol</a>. The corresponding VS Code client and server packages are available as <code>vscode-languageclient@10.0.0</code> and <code>vscode-languageserver@10.0.0</code>. For the full list of protocol additions and breaking changes, see the <a href="https://github.com/microsoft/vscode-languageserver-node/blob/main/README.md#3180-protocol-900-json-rpc-1000-client-and-1000-server" class="external-link" target="_blank">vscode-languageserver-node changelog</a>.</p>
<h2 id="_enterprise" data-needslink="_enterprise">Enterprise</h2>
<h3 id="_native-mdm-delivery-for-managed-copilot-settings" data-needslink="_native-mdm-delivery-for-managed-copilot-settings">Native MDM delivery for managed Copilot settings</h3>
<p>Administrators can now deliver managed GitHub Copilot settings through native device management (MDM) channels on Windows and macOS, in addition to the account-based enterprise settings file. This builds on the <a href="https://code.visualstudio.com/updates/v1_124#_enterprise">enterprise-managed Copilot plugin policies</a> and lets organizations enforce Copilot configuration using their existing device management tooling, without depending on per-user sign-in to apply policy.</p>
<p>For developers, settings delivered through MDM appear as policy-enforced in VS Code and cannot be overridden locally. Future updates expand the set of supported policy keys across Copilot surfaces.</p>
<h2 id="_deprecated-features-and-settings" data-needslink="_deprecated-features-and-settings">Deprecated features and settings</h2>
<p>None</p>
<h2 id="_thank-you" data-needslink="_thank-you">Thank you</h2>
<p>Contributions to <code>vscode</code>:</p>
<ul>
<li><a href="https://github.com/arun-357" class="external-link" target="_blank">@arun-357 (Arunachalam Nachiappan)</a>
<ul>
<li>Fix raw markdown shown in image carousel caption <a href="https://github.com/microsoft/vscode/pull/320754" class="external-link" target="_blank">PR #320754</a></li>
<li>Fix image carousel showing UUID on hover in modal editor title <a href="https://github.com/microsoft/vscode/pull/320739" class="external-link" target="_blank">PR #320739</a></li>
<li>Use a media icon for the Images Preview editor label <a href="https://github.com/microsoft/vscode/pull/320951" class="external-link" target="_blank">PR #320951</a></li>
</ul>
</li>
<li><a href="https://github.com/dymaaaj7" class="external-link" target="_blank">@dymaaaj7 (Dimitrije)</a>: Fix declaration order of File and Reference in CompletionItemKind <a href="https://github.com/microsoft/vscode/pull/314958" class="external-link" target="_blank">PR #314958</a></li>
<li><a href="https://github.com/g0w6y" class="external-link" target="_blank">@g0w6y (ⳕⲛτⲉⲅⲥⲉⳏτⲟⲅ 🕵🏻)</a>: Validate redirect scheme and strip credentials on cross-origin redirects in MCP HTTP client <a href="https://github.com/microsoft/vscode/pull/320347" class="external-link" target="_blank">PR #320347</a></li>
<li><a href="https://github.com/guomaggie" class="external-link" target="_blank">@guomaggie</a>: Switch from Copilot Proxy to CAPI V3 <a href="https://github.com/microsoft/vscode/pull/320472" class="external-link" target="_blank">PR #320472</a></li>
<li><a href="https://github.com/kangarko" class="external-link" target="_blank">@kangarko (Matej)</a>: Add setting to open changed chat files in an editor instead of a diff <a href="https://github.com/microsoft/vscode/pull/320948" class="external-link" target="_blank">PR #320948</a></li>
<li><a href="https://github.com/lucaspar" class="external-link" target="_blank">@lucaspar (Lucas Parzianello)</a>: Fixed typo in cli update <a href="https://github.com/microsoft/vscode/pull/245751" class="external-link" target="_blank">PR #245751</a></li>
<li><a href="https://github.com/merfanian" class="external-link" target="_blank">@merfanian (Mahdi Erfanian)</a>: Preserve image source provenance across chat reference API boundary <a href="https://github.com/microsoft/vscode/pull/320624" class="external-link" target="_blank">PR #320624</a></li>
<li><a href="https://github.com/RedCMD" class="external-link" target="_blank">@RedCMD (RedCMD)</a>: fix: Restrict continue comment to whitespace separated slashes <a href="https://github.com/microsoft/vscode/pull/321230" class="external-link" target="_blank">PR #321230</a></li>
<li><a href="https://github.com/Tyriar" class="external-link" target="_blank">@Tyriar (Daniel Imms)</a>: fix(terminal): track ligatures addon config for change detection <a href="https://github.com/microsoft/vscode/pull/318992" class="external-link" target="_blank">PR #318992</a></li>
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

                <div class="feedback" data-edit-url="https://vscode.dev/github/microsoft/vscode-docs/blob/main/release-notes/v1_125.md"></div>
            </main>
            
            <!-- Right sidebar - On This Page -->
            <aside class="docs-right-sidebar hidden-xs">
                <nav id="docs-subnavbar" aria-label="On Page">
                    
                    <h4><span class="sr-only">On this page there are 8 sections</span><span
                            aria-hidden="true">On this page</span></h4>
                    <ul class="nav">
                        
                        <li><a href="#_agents">Agents</a></li>
                        
                        <li><a href="#_language-models">Language Models</a></li>
                        
                        <li><a href="#_integrated-browser">Integrated Browser</a></li>
                        
                        <li><a href="#_editor-experience">Editor Experience</a></li>
                        
                        <li><a href="#_extension-authoring">Extension Authoring</a></li>
                        
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
							<path d="M24.6 4c.2.2.2.6