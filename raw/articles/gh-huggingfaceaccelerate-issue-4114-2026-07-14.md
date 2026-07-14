---
source_url: https://github.com/huggingface/accelerate/issues/4114
ingested: 2026-07-14
sha256: 5409f17874470258501c4bdd6125cdac58caea5494349e04a210d4fcb7a8d96e
blog_source: github:huggingface/accelerate
---
# Issue #4114: Bump the actions group across 1 directory with 5 updates

**State:** open | **Author:** dependabot[bot] | **Created:** 2026-07-13T07:56:54Z

Bumps the actions group with 5 updates in the / directory:

| Package | From | To |
| --- | --- | --- |
| [actions/checkout](https://github.com/actions/checkout) | `6` | `7` |
| [huggingface/doc-builder/.github/workflows/build_main_documentation.yml](https://github.com/huggingface/doc-builder) | `bcff59fca682130d2e7271ca8589911b7ac0b8bf` | `6108e850ae1cf2f71bb0815a600bcd50c39abfa7` |
| [huggingface/doc-builder/.github/workflows/build_pr_documentation.yml](https://github.com/huggingface/doc-builder) | `bcff59fca682130d2e7271ca8589911b7ac0b8bf` | `6108e850ae1cf2f71bb0815a600bcd50c39abfa7` |
| [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog) | `3.95.5` | `3.95.8` |
| [huggingface/doc-builder/.github/workflows/upload_pr_documentation.yml](https://github.com/huggingface/doc-builder) | `bcff59fca682130d2e7271ca8589911b7ac0b8bf` | `6108e850ae1cf2f71bb0815a600bcd50c39abfa7` |


Updates `actions/checkout` from 6 to 7
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/actions/checkout/releases">actions/checkout's releases</a>.</em></p>
<blockquote>
<h2>v7.0.0</h2>
<h2>What's Changed</h2>
<ul>
<li>block checking out fork pr for pull_request_target and workflow_run by <a href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a href="https://redirect.github.com/actions/checkout/pull/2454">actions/checkout#2454</a></li>
<li>Bump actions/publish-immutable-action from 0.0.3 to 0.0.4 in the minor-actions-dependencies group across 1 directory by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/actions/checkout/pull/2458">actions/checkout#2458</a></li>
<li>Bump flatted from 3.3.1 to 3.4.2 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/actions/checkout/pull/2460">actions/checkout#2460</a></li>
<li>Bump js-yaml from 4.1.0 to 4.2.0 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/actions/checkout/pull/2461">actions/checkout#2461</a></li>
<li>Bump <code>@​actions/core</code> and <code>@​actions/tool-cache</code> and Remove uuid by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/actions/checkout/pull/2459">actions/checkout#2459</a></li>
<li>upgrade module to esm and update dependencies by <a href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a href="https://redirect.github.com/actions/checkout/pull/2463">actions/checkout#2463</a></li>
<li>Bump the minor-npm-dependencies group across 1 directory with 3 updates by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/actions/checkout/pull/2462">actions/checkout#2462</a></li>
<li>getting ready for checkout v7 release by <a href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a href="https://redirect.github.com/actions/checkout/pull/2464">actions/checkout#2464</a></li>
<li>update error wording by <a href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a href="https://redirect.github.com/actions/checkout/pull/2467">actions/checkout#2467</a></li>
</ul>
<h2>New Contributors</h2>
<ul>
<li><a href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> made their first contribution in <a href="https://redirect.github.com/actions/checkout/pull/2454">actions/checkout#2454</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/actions/checkout/compare/v6.0.3...v7.0.0">https://github.com/actions/checkout/compare/v6.0.3...v7.0.0</a></p>
<h2>v6.0.3</h2>
<h2>What's Changed</h2>
<ul>
<li>Update changelog by <a href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a href="https://redirect.github.com/actions/checkout/pull/2357">actions/checkout#2357</a></li>
<li>fix: expand merge commit SHA regex and add SHA-256 test cases by <a href="https://github.com/yaananth"><code>@​yaananth</code></a> in <a href="https://redirect.github.com/actions/checkout/pull/2414">actions/checkout#2414</a></li>
<li>Fix checkout init for SHA-256 repositories by <a href="https://github.com/yaananth"><code>@​yaananth</code></a> in <a href="https://redirect.github.com/actions/checkout/pull/2439">actions/checkout#2439</a></li>
<li>Update changelog for v6.0.3 by <a href="https://github.com/yaananth"><code>@​yaananth</code></a> in <a href="https://redirect.github.com/actions/checkout/pull/2446">actions/checkout#2446</a></li>
</ul>
<h2>New Contributors</h2>
<ul>
<li><a href="https://github.com/yaananth"><code>@​yaananth</code></a> made their first contribution in <a href="https://redirect.github.com/actions/checkout/pull/2414">actions/checkout#2414</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/actions/checkout/compare/v6...v6.0.3">https://github.com/actions/checkout/compare/v6...v6.0.3</a></p>
<h2>v6.0.2</h2>
<h2>What's Changed</h2>
<ul>
<li>Add orchestration_id to git user-agent when ACTIONS_ORCHESTRATION_ID is set by <a href="https://github.com/TingluoHuang"><code>@​TingluoHuang</code></a> in <a href="https://redirect.github.com/actions/checkout/pull/2355">actions/checkout#2355</a></li>
<li>Fix tag handling: preserve annotations and explicit fetch-tags by <a href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a href="https://redirect.github.com/actions/checkout/pull/2356">actions/checkout#2356</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/actions/checkout/compare/v6.0.1...v6.0.2">https://github.com/actions/checkout/compare/v6.0.1...v6.0.2</a></p>
<h2>v6.0.1</h2>
<h2>What's Changed</h2>
<ul>
<li>Update all references from v5 and v4 to v6 by <a href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a href="https://redirect.github.com/actions/checkout/pull/2314">actions/checkout#2314</a></li>
<li>Add worktree support for persist-credentials includeIf by <a href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a href="https://redirect.github.com/actions/checkout/pull/2327">actions/checkout#2327</a></li>
<li>Clarify v6 README by <a href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a href="https://redirect.github.com/actions/checkout/pull/2328">actions/checkout#2328</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/actions/checkout/compare/v6...v6.0.1">https://github.com/actions/checkout/compare/v6...v6.0.1</a></p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/actions/checkout/commit/9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0"><code>9c091bb</code></a> update error wording (<a href="https://redirect.github.com/actions/checkout/issues/2467">#2467</a>)</li>
<li><a href="https://github.com/actions/checkout/commit/1044a6dea927916f2c38ba5aeffbc0a847b1221a"><code>1044a6d</code></a> getting ready for checkout v7 release (<a href="https://redirect.github.com/actions/checkout/issues/2464">#2464</a>)</li>
<li><a href="https://github.com/actions/checkout/commit/f0282184c7ce73ab54c7e4ab5a617122602e575f"><code>f028218</code></a> Bump the minor-npm-dependencies group across 1 directory with 3 updates (<a href="https://redirect.github.com/actions/checkout/issues/2462">#2462</a>)</li>
<li><a href="https://github.com/actions/checkout/commit/d914b262ffc244530a203ab40decab34c3abf34d"><code>d914b26</code></a> upgrade module to esm and update dependencies (<a href="https://redirect.github.com/actions/checkout/issues/2463">#2463</a>)</li>
<li><a href="https://github.com/actions/checkout/commit/537c7ef99cef6e5ddb5e7ff5d16d14510503801d"><code>537c7ef</code></a> Bump <code>@​actions/core</code> and <code>@​actions/tool-cache</code> and Remove uuid (<a href="https://redirect.github.com/actions/checkout/issues/2459">#2459</a>)</li>
<li><a href="https://github.com/actions/checkout/commit/130a169078a413d3a5246a393625e8e742f387f6"><code>130a169</code></a> Bump js-yaml from 4.1.0 to 4.2.0 (<a href="https://redirect.github.com/actions/checkout/issues/2461">#2461</a>)</li>
<li><a href="https://github.com/actions/checkout/commit/7d09575332117a40b46e5e020664df234cd416f3"><code>7d09575</code></a> Bump flatted from 3.3.1 to 3.4.2 (<a href="https://redirect.github.com/actions/checkout/issues/2460">#2460</a>)</li>
<li><a href="https://github.com/actions/checkout/commit/0f9f3aa320cb53abeb534aeb54048075d9697a0e"><code>0f9f3aa</code></a> Bump actions/publish-immutable-action (<a href="https://redirect.github.com/actions/checkout/issues/2458">#2458</a>)</li>
<li><a href="https://github.com/actions/checkout/commit/f9e715a95fcd1f9253f77dd28f11e88d2d6460c7"><code>f9e715a</code></a> block checking out fork pr for pull_request_target and workflow_run (<a href="https://redirect.github.com/actions/checkout/issues/2454">#2454</a>)</li>
<li>See full diff in <a href="https://github.com/actions/checkout/compare/v6...v7">compare view</a></li>
</ul>
</details>
<br />

Updates `huggingface/doc-builder/.github/workflows/build_main_documentation.yml` from bcff59fca682130d2e7271ca8589911b7ac0b8bf to 6108e850ae1cf2f71bb0815a600bcd50c39abfa7
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/huggingface/doc-builder/commit/6108e850ae1cf2f71bb0815a600bcd50c39abfa7"><code>6108e85</code></a> Add reachy_mini mock-deps registry entry (<a href="https://redirect.github.com/huggingface/doc-builder/issues/807">#807</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/0f4784322c564503c4a4d67ccb7fba29e32f111a"><code>0f47843</code></a> Mock optimum, torchao, gguf for diffusers docs (<a href="https://redirect.github.com/huggingface/doc-builder/issues/806">#806</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/f8ab2e5246a13eaa31c4b3760701856fc5ab98a6"><code>f8ab2e5</code></a> Add bitsandbytes (mock) and sentencepiece (real) to diffusers doc deps (<a href="https://redirect.github.com/huggingface/doc-builder/issues/805">#805</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/4a384d0ccdeb8502a57f1003acee938b42a5592a"><code>4a384d0</code></a> Fix upload_pr_documentation: drop unused doc-builder install (<a href="https://redirect.github.com/huggingface/doc-builder/issues/804">#804</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/7e6bd45ee271b96e75484eeafea1b3e6139cd0c7"><code>7e6bd45</code></a> Add tomli to openenv real doc-build deps (<a href="https://redirect.github.com/huggingface/doc-builder/issues/803">#803</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/e60a538eea9817ab312196d0d233604b01697265"><code>e60a538</code></a> Add --mock_deps: build docs without installing heavy dependencies (<a href="https://redirect.github.com/huggingface/doc-builder/issues/801">#801</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/a601280c0e9830f86ac8ecde75eeb3cf733e8bef"><code>a601280</code></a> feat: page-level HTML build cache backed by HF storage buckets (<a href="https://redirect.github.com/huggingface/doc-builder/issues/800">#800</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/41c17d14dcd20a51ca1c9b61496d53defc5a63dc"><code>41c17d1</code></a> refactor: modernize build and preview commands (<a href="https://redirect.github.com/huggingface/doc-builder/issues/798">#798</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/2f7376e5d3e4a8857f511d932e9d8f652711e461"><code>2f7376e</code></a> Simplify docstring pipeline: python emits the &lt;Docstring&gt; component directly ...</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/7241b199d3da05f9a1637dae8dbf6f798d5b731b"><code>7241b19</code></a> refactor(kit): migrate components to Svelte 5 runes syntax (<a href="https://redirect.github.com/huggingface/doc-builder/issues/795">#795</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/huggingface/doc-builder/compare/bcff59fca682130d2e7271ca8589911b7ac0b8bf...6108e850ae1cf2f71bb0815a600bcd50c39abfa7">compare view</a></li>
</ul>
</details>
<br />

Updates `huggingface/doc-builder/.github/workflows/build_pr_documentation.yml` from bcff59fca682130d2e7271ca8589911b7ac0b8bf to 6108e850ae1cf2f71bb0815a600bcd50c39abfa7
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/huggingface/doc-builder/commit/6108e850ae1cf2f71bb0815a600bcd50c39abfa7"><code>6108e85</code></a> Add reachy_mini mock-deps registry entry (<a href="https://redirect.github.com/huggingface/doc-builder/issues/807">#807</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/0f4784322c564503c4a4d67ccb7fba29e32f111a"><code>0f47843</code></a> Mock optimum, torchao, gguf for diffusers docs (<a href="https://redirect.github.com/huggingface/doc-builder/issues/806">#806</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/f8ab2e5246a13eaa31c4b3760701856fc5ab98a6"><code>f8ab2e5</code></a> Add bitsandbytes (mock) and sentencepiece (real) to diffusers doc deps (<a href="https://redirect.github.com/huggingface/doc-builder/issues/805">#805</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/4a384d0ccdeb8502a57f1003acee938b42a5592a"><code>4a384d0</code></a> Fix upload_pr_documentation: drop unused doc-builder install (<a href="https://redirect.github.com/huggingface/doc-builder/issues/804">#804</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/7e6bd45ee271b96e75484eeafea1b3e6139cd0c7"><code>7e6bd45</code></a> Add tomli to openenv real doc-build deps (<a href="https://redirect.github.com/huggingface/doc-builder/issues/803">#803</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/e60a538eea9817ab312196d0d233604b01697265"><code>e60a538</code></a> Add --mock_deps: build docs without installing heavy dependencies (<a href="https://redirect.github.com/huggingface/doc-builder/issues/801">#801</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/a601280c0e9830f86ac8ecde75eeb3cf733e8bef"><code>a601280</code></a> feat: page-level HTML build cache backed by HF storage buckets (<a href="https://redirect.github.com/huggingface/doc-builder/issues/800">#800</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/41c17d14dcd20a51ca1c9b61496d53defc5a63dc"><code>41c17d1</code></a> refactor: modernize build and preview commands (<a href="https://redirect.github.com/huggingface/doc-builder/issues/798">#798</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/2f7376e5d3e4a8857f511d932e9d8f652711e461"><code>2f7376e</code></a> Simplify docstring pipeline: python emits the &lt;Docstring&gt; component directly ...</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/7241b199d3da05f9a1637dae8dbf6f798d5b731b"><code>7241b19</code></a> refactor(kit): migrate components to Svelte 5 runes syntax (<a href="https://redirect.github.com/huggingface/doc-builder/issues/795">#795</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/huggingface/doc-builder/compare/bcff59fca682130d2e7271ca8589911b7ac0b8bf...6108e850ae1cf2f71bb0815a600bcd50c39abfa7">compare view</a></li>
</ul>
</details>
<br />

Updates `trufflesecurity/trufflehog` from 3.95.5 to 3.95.8
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/trufflesecurity/trufflehog/releases">trufflesecurity/trufflehog's releases</a>.</em></p>
<blockquote>
<h2>v3.95.8</h2>
<h2>What's Changed</h2>
<ul>
<li>removed &quot;unauthorized&quot; as exception for rotated graphana secrets by <a href="https://github.com/jordanTunstill"><code>@​jordanTunstill</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5068">trufflesecurity/trufflehog#5068</a></li>
<li>fix(azuresastoken): match SAS tokens regardless of parameter order by <a href="https://github.com/genisis0x"><code>@​genisis0x</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5043">trufflesecurity/trufflehog#5043</a></li>
<li>Add prometheus metrics for engine channels and workers by <a href="https://github.com/mcastorina"><code>@​mcastorina</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5095">trufflesecurity/trufflehog#5095</a></li>
<li>[INS-465] Skip unverified JWT Detector results when feature flag is enabled by <a href="https://github.com/MuneebUllahKhan222"><code>@​MuneebUllahKhan222</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5072">trufflesecurity/trufflehog#5072</a></li>
<li>[INS-334] Octopus Deploy detector by <a href="https://github.com/MuneebUllahKhan222"><code>@​MuneebUllahKhan222</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/4787">trufflesecurity/trufflehog#4787</a></li>
<li>Fix Syntax error in feature.go by <a href="https://github.com/MuneebUllahKhan222"><code>@​MuneebUllahKhan222</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5109">trufflesecurity/trufflehog#5109</a></li>
<li>Include encoded resume info instead of clobbering it by <a href="https://github.com/bill-rich"><code>@​bill-rich</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5110">trufflesecurity/trufflehog#5110</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/trufflesecurity/trufflehog/compare/v3.95.7...v3.95.8">https://github.com/trufflesecurity/trufflehog/compare/v3.95.7...v3.95.8</a></p>
<h2>v3.95.7</h2>
<h2>What's Changed</h2>
<ul>
<li>fix(sources/filesystem): order resume comparison by path component by <a href="https://github.com/genisis0x"><code>@​genisis0x</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5041">trufflesecurity/trufflehog#5041</a></li>
<li>test(handlers): point APK test fixture at trufflehog-test-assets by <a href="https://github.com/amanfcp"><code>@​amanfcp</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5053">trufflesecurity/trufflehog#5053</a></li>
<li>fixed regex typo that was causing conf uuid's to be surfaced as non-live atlassian secrets. by <a href="https://github.com/jordanTunstill"><code>@​jordanTunstill</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5029">trufflesecurity/trufflehog#5029</a></li>
<li>Fix GitHub App cross-org member enumeration using per-installation tokens by <a href="https://github.com/dustin-decker"><code>@​dustin-decker</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/4774">trufflesecurity/trufflehog#4774</a></li>
<li>fix: add git worktree support in PrepareRepo by <a href="https://github.com/andoniaf"><code>@​andoniaf</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/4690">trufflesecurity/trufflehog#4690</a></li>
<li>[INS-406] Braintrust detector by <a href="https://github.com/MuneebUllahKhan222"><code>@​MuneebUllahKhan222</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/4826">trufflesecurity/trufflehog#4826</a></li>
<li>huggingface: add bucket scanning by <a href="https://github.com/julien-c"><code>@​julien-c</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5017">trufflesecurity/trufflehog#5017</a></li>
<li>Skip reverification results during deduplication by <a href="https://github.com/mcastorina"><code>@​mcastorina</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5069">trufflesecurity/trufflehog#5069</a></li>
<li>chore(renovate): bump shared config to v1.0.3 by <a href="https://github.com/bryanbeverly"><code>@​bryanbeverly</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5044">trufflesecurity/trufflehog#5044</a></li>
<li>Add scan_all_installations option for multi-org GitHub App scanning by <a href="https://github.com/dustin-decker"><code>@​dustin-decker</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/4775">trufflesecurity/trufflehog#4775</a></li>
<li>Expose <code>SecretParts</code> in the JSON output by <a href="https://github.com/bradlarsen"><code>@​bradlarsen</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5073">trufflesecurity/trufflehog#5073</a></li>
<li>[INS-497] Add Pganalyze Read Key Detector by <a href="https://github.com/MuneebUllahKhan222"><code>@​MuneebUllahKhan222</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/4993">trufflesecurity/trufflehog#4993</a></li>
<li>[INS-197] Add redhatpyxis api key detector by <a href="https://github.com/MuneebUllahKhan222"><code>@​MuneebUllahKhan222</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/4995">trufflesecurity/trufflehog#4995</a></li>
<li>[INS-407] Fixed AWS detector producing non deterministic output by <a href="https://github.com/MuneebUllahKhan222"><code>@​MuneebUllahKhan222</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/4836">trufflesecurity/trufflehog#4836</a></li>
</ul>
<h2>New Contributors</h2>
<ul>
<li><a href="https://github.com/genisis0x"><code>@​genisis0x</code></a> made their first contribution in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5041">trufflesecurity/trufflehog#5041</a></li>
<li><a href="https://github.com/andoniaf"><code>@​andoniaf</code></a> made their first contribution in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/4690">trufflesecurity/trufflehog#4690</a></li>
<li><a href="https://github.com/julien-c"><code>@​julien-c</code></a> made their first contribution in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5017">trufflesecurity/trufflehog#5017</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/trufflesecurity/trufflehog/compare/v3.95.6...v3.95.7">https://github.com/trufflesecurity/trufflehog/compare/v3.95.6...v3.95.7</a></p>
<h2>v3.95.6</h2>
<h2>What's Changed</h2>
<ul>
<li>Enigma detector enhance verification to prevent false verified findings by <a href="https://github.com/shahzadhaider1"><code>@​shahzadhaider1</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5011">trufflesecurity/trufflehog#5011</a></li>
<li>fix: scan files with lines exceeding bufio's default 64 KB token limit by <a href="https://github.com/MuneebUllahKhan222"><code>@​MuneebUllahKhan222</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5022">trufflesecurity/trufflehog#5022</a></li>
<li>fix(postgres): honor ignore tags for default port URLs by <a href="https://github.com/Dawn-Fighter"><code>@​Dawn-Fighter</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/4968">trufflesecurity/trufflehog#4968</a></li>
<li>Move to github.com/moby/moby/client from docker/docker by <a href="https://github.com/trufflesteeeve"><code>@​trufflesteeeve</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/4987">trufflesecurity/trufflehog#4987</a></li>
<li>fix: avoid terminal probes before CLI output by <a href="https://github.com/Hackerchen716"><code>@​Hackerchen716</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/4994">trufflesecurity/trufflehog#4994</a></li>
<li>Update test containers dependency by <a href="https://github.com/trufflesteeeve"><code>@​trufflesteeeve</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/4978">trufflesecurity/trufflehog#4978</a></li>
<li>Re-host pkg/handlers JSON test fixtures under the org by <a href="https://github.com/amanfcp"><code>@​amanfcp</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5023">trufflesecurity/trufflehog#5023</a></li>
<li>[INS-465] Add datadogapikey detector to defaults.go by <a href="https://github.com/mustansir14"><code>@​mustansir14</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/4969">trufflesecurity/trufflehog#4969</a></li>
<li>[INS-470] Add Tly detector to defaults.go, gate it behind feat flag and update its verification logic by <a href="https://github.com/MuneebUllahKhan222"><code>@​MuneebUllahKhan222</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5006">trufflesecurity/trufflehog#5006</a></li>
<li>[INS-473] Add wit detector to defaults.go, gate it behind feat flag and update verification logic by <a href="https://github.com/MuneebUllahKhan222"><code>@​MuneebUllahKhan222</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5008">trufflesecurity/trufflehog#5008</a></li>
<li>Updating Klaviyo PK new format by <a href="https://github.com/breetan"><code>@​breetan</code></a> in <a href="https://redirect.github.com/trufflesecurity/trufflehog/pull/5009">trufflesecurity/trufflehog#5009</a></li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/trufflesecurity/trufflehog/commit/00155c9dc586f34d189adc83d3ac2698c2ec551f"><code>00155c9</code></a> Include encoded resume info instead of clobbering it (<a href="https://redirect.github.com/trufflesecurity/trufflehog/issues/5110">#5110</a>)</li>
<li><a href="https://github.com/trufflesecurity/trufflehog/commit/4d3a66f4780fb722d680db02c31ce0b1df496c77"><code>4d3a66f</code></a> fixed syntax error (<a href="https://redirect.github.com/trufflesecurity/trufflehog/issues/5109">#5109</a>)</li>
<li><a href="https://github.com/trufflesecurity/trufflehog/commit/797f02be367f68a09583034b6e1e535ae7e8c1d1"><code>797f02b</code></a> [INS-334] Octopus Deploy detector (<a href="https://redirect.github.com/trufflesecurity/trufflehog/issues/4787">#4787</a>)</li>
<li><a href="https://github.com/trufflesecurity/trufflehog/commit/7f04a89676cb788e9f85b725eccf81a07e4f4a4d"><code>7f04a89</code></a> [INS-465] Skip unverified JWT Detector results when feature flag is enabled (...</li>
<li><a href="https://github.com/trufflesecurity/trufflehog/commit/459d5a78cbfe19b48391cf407dea916114db862f"><code>459d5a7</code></a> Add prometheus metrics for engine channels and workers (<a href="https://redirect.github.com/trufflesecurity/trufflehog/issues/5095">#5095</a>)</li>
<li><a href="https://github.com/trufflesecurity/trufflehog/commit/f38f8f7dd77530315ba9218e25693b606ec3da21"><code>f38f8f7</code></a> fix(azuresastoken): match SAS tokens regardless of parameter order (<a href="https://redirect.github.com/trufflesecurity/trufflehog/issues/5043">#5043</a>)</li>
<li><a href="https://github.com/trufflesecurity/trufflehog/commit/6261f5cd38e133cdcf00c23e3943f3e9d012d538"><code>6261f5c</code></a> removed &quot;unauthorized&quot; as exception for rotated graphana secrets (<a href="https://redirect.github.com/trufflesecurity/trufflehog/issues/5068">#5068</a>)</li>
<li><a href="https://github.com/trufflesecurity/trufflehog/commit/f446421baf832d6356c42c1743d99abff52ff334"><code>f446421</code></a> [INS-407] Fixed AWS detector producing non deterministic output (<a href="https://redirect.github.com/trufflesecurity/trufflehog/issues/4836">#4836</a>)</li>
<li><a href="https://github.com/trufflesecurity/trufflehog/commit/885fa2d6b0e8347ee3d921bf79ecb6c8510f8ae1"><code>885fa2d</code></a> [INS-197] Add redhatpyxis api key detector (<a href="https://redirect.github.com/trufflesecurity/trufflehog/issues/4995">#4995</a>)</li>
<li><a href="https://github.com/trufflesecurity/trufflehog/commit/c09d72666af2336c402d6a12d0acfd9693432060"><code>c09d726</code></a> [INS-497] Add Pganalyze Read Key Detector (<a href="https://redirect.github.com/trufflesecurity/trufflehog/issues/4993">#4993</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/trufflesecurity/trufflehog/compare/d411fff7b8879a62509f3fa98c07f247ac089a51...00155c9dc586f34d189adc83d3ac2698c2ec551f">compare view</a></li>
</ul>
</details>
<br />

Updates `huggingface/doc-builder/.github/workflows/upload_pr_documentation.yml` from bcff59fca682130d2e7271ca8589911b7ac0b8bf to 6108e850ae1cf2f71bb0815a600bcd50c39abfa7
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/huggingface/doc-builder/commit/6108e850ae1cf2f71bb0815a600bcd50c39abfa7"><code>6108e85</code></a> Add reachy_mini mock-deps registry entry (<a href="https://redirect.github.com/huggingface/doc-builder/issues/807">#807</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/0f4784322c564503c4a4d67ccb7fba29e32f111a"><code>0f47843</code></a> Mock optimum, torchao, gguf for diffusers docs (<a href="https://redirect.github.com/huggingface/doc-builder/issues/806">#806</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/f8ab2e5246a13eaa31c4b3760701856fc5ab98a6"><code>f8ab2e5</code></a> Add bitsandbytes (mock) and sentencepiece (real) to diffusers doc deps (<a href="https://redirect.github.com/huggingface/doc-builder/issues/805">#805</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/4a384d0ccdeb8502a57f1003acee938b42a5592a"><code>4a384d0</code></a> Fix upload_pr_documentation: drop unused doc-builder install (<a href="https://redirect.github.com/huggingface/doc-builder/issues/804">#804</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/7e6bd45ee271b96e75484eeafea1b3e6139cd0c7"><code>7e6bd45</code></a> Add tomli to openenv real doc-build deps (<a href="https://redirect.github.com/huggingface/doc-builder/issues/803">#803</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/e60a538eea9817ab312196d0d233604b01697265"><code>e60a538</code></a> Add --mock_deps: build docs without installing heavy dependencies (<a href="https://redirect.github.com/huggingface/doc-builder/issues/801">#801</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/a601280c0e9830f86ac8ecde75eeb3cf733e8bef"><code>a601280</code></a> feat: page-level HTML build cache backed by HF storage buckets (<a href="https://redirect.github.com/huggingface/doc-builder/issues/800">#800</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/41c17d14dcd20a51ca1c9b61496d53defc5a63dc"><code>41c17d1</code></a> refactor: modernize build and preview commands (<a href="https://redirect.github.com/huggingface/doc-builder/issues/798">#798</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/2f7376e5d3e4a8857f511d932e9d8f652711e461"><code>2f7376e</code></a> Simplify docstring pipeline: python emits the &lt;Docstring&gt; component directly ...</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/7241b199d3da05f9a1637dae8dbf6f798d5b731b"><code>7241b19</code></a> refactor(kit): migrate components to Svelte 5 runes syntax (<a href="https://redirect.github.com/huggingface/doc-builder/issues/795">#795</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/huggingface/doc-builder/compare/bcff59fca682130d2e7271ca8589911b7ac0b8bf...6108e850ae1cf2f71bb0815a600bcd50c39abfa7">compare view</a></li>
</ul>
</details>
<br />


Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

<details>
<summary>Dependabot commands and options</summary>
<br />

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore <dependency name> major version` will close this group update PR and stop Dependabot creating any more for the specific dependency's major version (unless you unignore this specific dependency's major version or upgrade to it yourself)
- `@dependabot ignore <dependency name> minor version` will close this group update PR and stop Dependabot creating any more for the specific dependency's minor version (unless you unignore this specific dependency's minor version or upgrade to it yourself)
- `@dependabot ignore <dependency name>` will close this group update PR and stop Dependabot creating any more for the specific dependency (unless you unignore this specific dependency or upgrade to it yourself)
- `@dependabot unignore <dependency name>` will remove all of the ignore conditions of the specified dependency
- `@dependabot unignore <dependency name> <ignore condition>` will remove the ignore condition of the specified dependency and ignore conditions


</details>