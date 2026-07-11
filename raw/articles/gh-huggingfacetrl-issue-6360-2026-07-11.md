---
source_url: https://github.com/huggingface/trl/issues/6360
ingested: 2026-07-11
sha256: 3b9fe72b7130843d06d0adc3e23fd6ab6e5d6bf30142047c789e126703144c1d
blog_source: github:huggingface/trl
---
# Issue #6360: Bump the actions group with 9 updates

**State:** open | **Author:** dependabot[bot] | **Created:** 2026-07-11T09:37:34Z

Bumps the actions group with 9 updates:

| Package | From | To |
| --- | --- | --- |
| [huggingface/doc-builder/.github/workflows/build_main_documentation.yml](https://github.com/huggingface/doc-builder) | `4a384d0ccdeb8502a57f1003acee938b42a5592a` | `0f4784322c564503c4a4d67ccb7fba29e32f111a` |
| [huggingface/doc-builder/.github/workflows/build_pr_documentation.yml](https://github.com/huggingface/doc-builder) | `4a384d0ccdeb8502a57f1003acee938b42a5592a` | `0f4784322c564503c4a4d67ccb7fba29e32f111a` |
| [github/codeql-action/init](https://github.com/github/codeql-action) | `4.36.2` | `4.36.3` |
| [github/codeql-action/analyze](https://github.com/github/codeql-action) | `4.36.2` | `4.36.3` |
| [docker/setup-buildx-action](https://github.com/docker/setup-buildx-action) | `4.1.0` | `4.2.0` |
| [docker/login-action](https://github.com/docker/login-action) | `4.2.0` | `4.4.0` |
| [docker/build-push-action](https://github.com/docker/build-push-action) | `7.2.0` | `7.3.0` |
| [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog) | `3.95.6` | `3.95.8` |
| [huggingface/doc-builder/.github/workflows/upload_pr_documentation.yml](https://github.com/huggingface/doc-builder) | `4a384d0ccdeb8502a57f1003acee938b42a5592a` | `0f4784322c564503c4a4d67ccb7fba29e32f111a` |

Updates `huggingface/doc-builder/.github/workflows/build_main_documentation.yml` from 4a384d0ccdeb8502a57f1003acee938b42a5592a to 0f4784322c564503c4a4d67ccb7fba29e32f111a
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/huggingface/doc-builder/commit/0f4784322c564503c4a4d67ccb7fba29e32f111a"><code>0f47843</code></a> Mock optimum, torchao, gguf for diffusers docs (<a href="https://redirect.github.com/huggingface/doc-builder/issues/806">#806</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/f8ab2e5246a13eaa31c4b3760701856fc5ab98a6"><code>f8ab2e5</code></a> Add bitsandbytes (mock) and sentencepiece (real) to diffusers doc deps (<a href="https://redirect.github.com/huggingface/doc-builder/issues/805">#805</a>)</li>
<li>See full diff in <a href="https://github.com/huggingface/doc-builder/compare/4a384d0ccdeb8502a57f1003acee938b42a5592a...0f4784322c564503c4a4d67ccb7fba29e32f111a">compare view</a></li>
</ul>
</details>
<br />

Updates `huggingface/doc-builder/.github/workflows/build_pr_documentation.yml` from 4a384d0ccdeb8502a57f1003acee938b42a5592a to 0f4784322c564503c4a4d67ccb7fba29e32f111a
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/huggingface/doc-builder/commit/0f4784322c564503c4a4d67ccb7fba29e32f111a"><code>0f47843</code></a> Mock optimum, torchao, gguf for diffusers docs (<a href="https://redirect.github.com/huggingface/doc-builder/issues/806">#806</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/f8ab2e5246a13eaa31c4b3760701856fc5ab98a6"><code>f8ab2e5</code></a> Add bitsandbytes (mock) and sentencepiece (real) to diffusers doc deps (<a href="https://redirect.github.com/huggingface/doc-builder/issues/805">#805</a>)</li>
<li>See full diff in <a href="https://github.com/huggingface/doc-builder/compare/4a384d0ccdeb8502a57f1003acee938b42a5592a...0f4784322c564503c4a4d67ccb7fba29e32f111a">compare view</a></li>
</ul>
</details>
<br />

Updates `github/codeql-action/init` from 4.36.2 to 4.36.3
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/github/codeql-action/releases">github/codeql-action/init's releases</a>.</em></p>
<blockquote>
<h2>v4.36.3</h2>
<p>No user facing changes.</p>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/github/codeql-action/blob/main/CHANGELOG.md">github/codeql-action/init's changelog</a>.</em></p>
<blockquote>
<h1>CodeQL Action Changelog</h1>
<p>See the <a href="https://github.com/github/codeql-action/releases">releases page</a> for the relevant changes to the CodeQL CLI and language packs.</p>
<h2>[UNRELEASED]</h2>
<ul>
<li><em>Upcoming breaking change</em>: Add a deprecation warning for customers using CodeQL version 2.20.6 and earlier. These versions of CodeQL were discontinued on 1 July 2026 alongside GitHub Enterprise Server 3.16, and will be unsupported by the next minor release of the CodeQL Action. <a href="https://redirect.github.com/github/codeql-action/pull/3956">#3956</a></li>
</ul>
<h2>4.37.0 - 08 Jul 2026</h2>
<ul>
<li>Update default CodeQL bundle version to <a href="https://github.com/github/codeql-action/releases/tag/codeql-bundle-v2.26.0">2.26.0</a>. <a href="https://redirect.github.com/github/codeql-action/pull/3995">#3995</a></li>
<li>In addition to the existing input format, the <code>config-file</code> input for the <code>codeql-action/init</code> step will soon support a new <code>[owner/]repo[@ref][:path]</code> format. All components except the repository name are optional. If omitted, <code>owner</code> defaults to the same owner as the repository the analysis is running for, <code>ref</code> to <code>main</code>, and <code>path</code> to <code>.github/codeql-action.yaml</code>. Support for this format ships in this version of the CodeQL Action, but will only be enabled over the coming weeks. <a href="https://redirect.github.com/github/codeql-action/pull/3973">#3973</a></li>
</ul>
<h2>4.36.3 - 01 Jul 2026</h2>
<p>No user facing changes.</p>
<h2>4.36.2 - 04 Jun 2026</h2>
<ul>
<li>Cache CodeQL CLI version information across Actions steps. <a href="https://redirect.github.com/github/codeql-action/pull/3943">#3943</a></li>
<li>Reduce requests while waiting for analysis processing by using exponential backoff when polling SARIF processing status. <a href="https://redirect.github.com/github/codeql-action/pull/3937">#3937</a></li>
<li>Update default CodeQL bundle version to <a href="https://github.com/github/codeql-action/releases/tag/codeql-bundle-v2.25.6">2.25.6</a>. <a href="https://redirect.github.com/github/codeql-action/pull/3948">#3948</a></li>
</ul>
<h2>4.36.1 - 02 Jun 2026</h2>
<p>No user facing changes.</p>
<h2>4.36.0 - 22 May 2026</h2>
<ul>
<li><em>Breaking change</em>: Bump the minimum required CodeQL bundle version to 2.19.4. <a href="https://redirect.github.com/github/codeql-action/pull/3894">#3894</a></li>
<li>Add support for SHA-256 Git object IDs. <a href="https://redirect.github.com/github/codeql-action/pull/3893">#3893</a></li>
<li>Update default CodeQL bundle version to <a href="https://github.com/github/codeql-action/releases/tag/codeql-bundle-v2.25.5">2.25.5</a>. <a href="https://redirect.github.com/github/codeql-action/pull/3926">#3926</a></li>
</ul>
<h2>4.35.5 - 15 May 2026</h2>
<ul>
<li>We have improved how the JavaScript bundles for the CodeQL Action are generated to avoid duplication across bundles and reduce the size of the repository by around 70%. This should have no effect on the runtime behaviour of the CodeQL Action. <a href="https://redirect.github.com/github/codeql-action/pull/3899">#3899</a></li>
<li>For performance and accuracy reasons, <a href="https://redirect.github.com/github/roadmap/issues/1158">improved incremental analysis</a> will now only be enabled on a pull request when diff-informed analysis is also enabled for that run. If diff-informed analysis is unavailable (for example, because the PR diff ranges could not be computed), the action will fall back to a full analysis. <a href="https://redirect.github.com/github/codeql-action/pull/3791">#3791</a></li>
<li>If multiple inputs are provided for the GitHub-internal <code>analysis-kinds</code> input, only <code>code-scanning</code> will be enabled. The <code>analysis-kinds</code> input is experimental, for GitHub-internal use only, and may change without notice at any time. <a href="https://redirect.github.com/github/codeql-action/pull/3892">#3892</a></li>
<li>Added an experimental change which, when running a Code Scanning analysis for a PR with <a href="https://redirect.github.com/github/roadmap/issues/1158">improved incremental analysis</a> enabled, prefers CodeQL CLI versions that have a cached overlay-base database for the configured languages. This speeds up analysis for a repository when there is not yet a cached overlay-base database for the latest CLI version. We expect to roll this change out to everyone in May. <a href="https://redirect.github.com/github/codeql-action/pull/3880">#3880</a></li>
</ul>
<h2>4.35.4 - 07 May 2026</h2>
<ul>
<li>Update default CodeQL bundle version to <a href="https://github.com/github/codeql-action/releases/tag/codeql-bundle-v2.25.4">2.25.4</a>. <a href="https://redirect.github.com/github/codeql-action/pull/3881">#3881</a></li>
</ul>
<h2>4.35.3 - 01 May 2026</h2>
<ul>
<li><em>Upcoming breaking change</em>: Add a deprecation warning for customers using CodeQL version 2.19.3 and earlier. These versions of CodeQL were discontinued on 9 April 2026 alongside GitHub Enterprise Server 3.15, and will be unsupported by the next minor release of the CodeQL Action. <a href="https://redirect.github.com/github/codeql-action/pull/3837">#3837</a></li>
<li>Configurations for private registries that use Cloudsmith or GCP OIDC are now accepted. <a href="https://redirect.github.com/github/codeql-action/pull/3850">#3850</a></li>
<li>Best-effort connection tests for private registries now use <code>GET</code> requests instead of <code>HEAD</code> for better compatibility with various registry implementations. For NuGet feeds, the test is now always performed against the service index. <a href="https://redirect.github.com/github/codeql-action/pull/3853">#3853</a></li>
<li>Fixed a bug where two diagnostics produced within the same millisecond could overwrite each other on disk, causing one of them to be lost. <a href="https://redirect.github.com/github/codeql-action/pull/3852">#3852</a></li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/github/codeql-action/commit/54f647b7e1bb85c95cddabcd46b0c578ec92bc1a"><code>54f647b</code></a> Merge pull request <a href="https://redirect.github.com/github/codeql-action/issues/3984">#3984</a> from github/update-v4.36.3-1f34ec164</li>
<li><a href="https://github.com/github/codeql-action/commit/e78819e05527766c3c5919e3177647e280c6cb83"><code>e78819e</code></a> Trigger checks</li>
<li><a href="https://github.com/github/codeql-action/commit/2c9d3d63eb4941734e2d29468953529a56f5ff1c"><code>2c9d3d6</code></a> Update changelog for v4.36.3</li>
<li><a href="https://github.com/github/codeql-action/commit/1f34ec16430d82636d18716acc7aaa6d843b35a9"><code>1f34ec1</code></a> Merge pull request <a href="https://redirect.github.com/github/codeql-action/issues/3983">#3983</a> from github/mbg/repo-props/ff-for-config-file-prop</li>
<li><a href="https://github.com/github/codeql-action/commit/d5f0145480025b49d8b08c3f6b36e6ad41a68c90"><code>d5f0145</code></a> Log when repository property has a value but is ignored</li>
<li><a href="https://github.com/github/codeql-action/commit/f27f56386a3c745af8d7bbfb806098c714a5e32a"><code>f27f563</code></a> Add test for when the FF is off</li>
<li><a href="https://github.com/github/codeql-action/commit/0025d0f2b5676fde748a0be9725dcce18dd9f986"><code>0025d0f</code></a> Use FF</li>
<li><a href="https://github.com/github/codeql-action/commit/f7fa18f05d107ff6735857c3510fbff190c9a1eb"><code>f7fa18f</code></a> Add FF for config file repo property</li>
<li><a href="https://github.com/github/codeql-action/commit/628fc3f124e68b0151f0d2a5d81e864ee1e42335"><code>628fc3f</code></a> Merge pull request <a href="https://redirect.github.com/github/codeql-action/issues/3979">#3979</a> from github/henrymercer/overlay-db-cleanup-size-tele...</li>
<li><a href="https://github.com/github/codeql-action/commit/9cfb67bab9b32441237f92d4ba29a7f3ccff259f"><code>9cfb67b</code></a> Add clarifying comments</li>
<li>Additional commits viewable in <a href="https://github.com/github/codeql-action/compare/8aad20d150bbac5944a9f9d289da16a4b0d87c1e...54f647b7e1bb85c95cddabcd46b0c578ec92bc1a">compare view</a></li>
</ul>
</details>
<br />

Updates `github/codeql-action/analyze` from 4.36.2 to 4.36.3
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/github/codeql-action/releases">github/codeql-action/analyze's releases</a>.</em></p>
<blockquote>
<h2>v4.36.3</h2>
<p>No user facing changes.</p>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/github/codeql-action/blob/main/CHANGELOG.md">github/codeql-action/analyze's changelog</a>.</em></p>
<blockquote>
<h1>CodeQL Action Changelog</h1>
<p>See the <a href="https://github.com/github/codeql-action/releases">releases page</a> for the relevant changes to the CodeQL CLI and language packs.</p>
<h2>[UNRELEASED]</h2>
<ul>
<li><em>Upcoming breaking change</em>: Add a deprecation warning for customers using CodeQL version 2.20.6 and earlier. These versions of CodeQL were discontinued on 1 July 2026 alongside GitHub Enterprise Server 3.16, and will be unsupported by the next minor release of the CodeQL Action. <a href="https://redirect.github.com/github/codeql-action/pull/3956">#3956</a></li>
</ul>
<h2>4.37.0 - 08 Jul 2026</h2>
<ul>
<li>Update default CodeQL bundle version to <a href="https://github.com/github/codeql-action/releases/tag/codeql-bundle-v2.26.0">2.26.0</a>. <a href="https://redirect.github.com/github/codeql-action/pull/3995">#3995</a></li>
<li>In addition to the existing input format, the <code>config-file</code> input for the <code>codeql-action/init</code> step will soon support a new <code>[owner/]repo[@ref][:path]</code> format. All components except the repository name are optional. If omitted, <code>owner</code> defaults to the same owner as the repository the analysis is running for, <code>ref</code> to <code>main</code>, and <code>path</code> to <code>.github/codeql-action.yaml</code>. Support for this format ships in this version of the CodeQL Action, but will only be enabled over the coming weeks. <a href="https://redirect.github.com/github/codeql-action/pull/3973">#3973</a></li>
</ul>
<h2>4.36.3 - 01 Jul 2026</h2>
<p>No user facing changes.</p>
<h2>4.36.2 - 04 Jun 2026</h2>
<ul>
<li>Cache CodeQL CLI version information across Actions steps. <a href="https://redirect.github.com/github/codeql-action/pull/3943">#3943</a></li>
<li>Reduce requests while waiting for analysis processing by using exponential backoff when polling SARIF processing status. <a href="https://redirect.github.com/github/codeql-action/pull/3937">#3937</a></li>
<li>Update default CodeQL bundle version to <a href="https://github.com/github/codeql-action/releases/tag/codeql-bundle-v2.25.6">2.25.6</a>. <a href="https://redirect.github.com/github/codeql-action/pull/3948">#3948</a></li>
</ul>
<h2>4.36.1 - 02 Jun 2026</h2>
<p>No user facing changes.</p>
<h2>4.36.0 - 22 May 2026</h2>
<ul>
<li><em>Breaking change</em>: Bump the minimum required CodeQL bundle version to 2.19.4. <a href="https://redirect.github.com/github/codeql-action/pull/3894">#3894</a></li>
<li>Add support for SHA-256 Git object IDs. <a href="https://redirect.github.com/github/codeql-action/pull/3893">#3893</a></li>
<li>Update default CodeQL bundle version to <a href="https://github.com/github/codeql-action/releases/tag/codeql-bundle-v2.25.5">2.25.5</a>. <a href="https://redirect.github.com/github/codeql-action/pull/3926">#3926</a></li>
</ul>
<h2>4.35.5 - 15 May 2026</h2>
<ul>
<li>We have improved how the JavaScript bundles for the CodeQL Action are generated to avoid duplication across bundles and reduce the size of the repository by around 70%. This should have no effect on the runtime behaviour of the CodeQL Action. <a href="https://redirect.github.com/github/codeql-action/pull/3899">#3899</a></li>
<li>For performance and accuracy reasons, <a href="https://redirect.github.com/github/roadmap/issues/1158">improved incremental analysis</a> will now only be enabled on a pull request when diff-informed analysis is also enabled for that run. If diff-informed analysis is unavailable (for example, because the PR diff ranges could not be computed), the action will fall back to a full analysis. <a href="https://redirect.github.com/github/codeql-action/pull/3791">#3791</a></li>
<li>If multiple inputs are provided for the GitHub-internal <code>analysis-kinds</code> input, only <code>code-scanning</code> will be enabled. The <code>analysis-kinds</code> input is experimental, for GitHub-internal use only, and may change without notice at any time. <a href="https://redirect.github.com/github/codeql-action/pull/3892">#3892</a></li>
<li>Added an experimental change which, when running a Code Scanning analysis for a PR with <a href="https://redirect.github.com/github/roadmap/issues/1158">improved incremental analysis</a> enabled, prefers CodeQL CLI versions that have a cached overlay-base database for the configured languages. This speeds up analysis for a repository when there is not yet a cached overlay-base database for the latest CLI version. We expect to roll this change out to everyone in May. <a href="https://redirect.github.com/github/codeql-action/pull/3880">#3880</a></li>
</ul>
<h2>4.35.4 - 07 May 2026</h2>
<ul>
<li>Update default CodeQL bundle version to <a href="https://github.com/github/codeql-action/releases/tag/codeql-bundle-v2.25.4">2.25.4</a>. <a href="https://redirect.github.com/github/codeql-action/pull/3881">#3881</a></li>
</ul>
<h2>4.35.3 - 01 May 2026</h2>
<ul>
<li><em>Upcoming breaking change</em>: Add a deprecation warning for customers using CodeQL version 2.19.3 and earlier. These versions of CodeQL were discontinued on 9 April 2026 alongside GitHub Enterprise Server 3.15, and will be unsupported by the next minor release of the CodeQL Action. <a href="https://redirect.github.com/github/codeql-action/pull/3837">#3837</a></li>
<li>Configurations for private registries that use Cloudsmith or GCP OIDC are now accepted. <a href="https://redirect.github.com/github/codeql-action/pull/3850">#3850</a></li>
<li>Best-effort connection tests for private registries now use <code>GET</code> requests instead of <code>HEAD</code> for better compatibility with various registry implementations. For NuGet feeds, the test is now always performed against the service index. <a href="https://redirect.github.com/github/codeql-action/pull/3853">#3853</a></li>
<li>Fixed a bug where two diagnostics produced within the same millisecond could overwrite each other on disk, causing one of them to be lost. <a href="https://redirect.github.com/github/codeql-action/pull/3852">#3852</a></li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/github/codeql-action/commit/54f647b7e1bb85c95cddabcd46b0c578ec92bc1a"><code>54f647b</code></a> Merge pull request <a href="https://redirect.github.com/github/codeql-action/issues/3984">#3984</a> from github/update-v4.36.3-1f34ec164</li>
<li><a href="https://github.com/github/codeql-action/commit/e78819e05527766c3c5919e3177647e280c6cb83"><code>e78819e</code></a> Trigger checks</li>
<li><a href="https://github.com/github/codeql-action/commit/2c9d3d63eb4941734e2d29468953529a56f5ff1c"><code>2c9d3d6</code></a> Update changelog for v4.36.3</li>
<li><a href="https://github.com/github/codeql-action/commit/1f34ec16430d82636d18716acc7aaa6d843b35a9"><code>1f34ec1</code></a> Merge pull request <a href="https://redirect.github.com/github/codeql-action/issues/3983">#3983</a> from github/mbg/repo-props/ff-for-config-file-prop</li>
<li><a href="https://github.com/github/codeql-action/commit/d5f0145480025b49d8b08c3f6b36e6ad41a68c90"><code>d5f0145</code></a> Log when repository property has a value but is ignored</li>
<li><a href="https://github.com/github/codeql-action/commit/f27f56386a3c745af8d7bbfb806098c714a5e32a"><code>f27f563</code></a> Add test for when the FF is off</li>
<li><a href="https://github.com/github/codeql-action/commit/0025d0f2b5676fde748a0be9725dcce18dd9f986"><code>0025d0f</code></a> Use FF</li>
<li><a href="https://github.com/github/codeql-action/commit/f7fa18f05d107ff6735857c3510fbff190c9a1eb"><code>f7fa18f</code></a> Add FF for config file repo property</li>
<li><a href="https://github.com/github/codeql-action/commit/628fc3f124e68b0151f0d2a5d81e864ee1e42335"><code>628fc3f</code></a> Merge pull request <a href="https://redirect.github.com/github/codeql-action/issues/3979">#3979</a> from github/henrymercer/overlay-db-cleanup-size-tele...</li>
<li><a href="https://github.com/github/codeql-action/commit/9cfb67bab9b32441237f92d4ba29a7f3ccff259f"><code>9cfb67b</code></a> Add clarifying comments</li>
<li>Additional commits viewable in <a href="https://github.com/github/codeql-action/compare/8aad20d150bbac5944a9f9d289da16a4b0d87c1e...54f647b7e1bb85c95cddabcd46b0c578ec92bc1a">compare view</a></li>
</ul>
</details>
<br />

Updates `docker/setup-buildx-action` from 4.1.0 to 4.2.0
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/docker/setup-buildx-action/releases">docker/setup-buildx-action's releases</a>.</em></p>
<blockquote>
<h2>v4.2.0</h2>
<ul>
<li>Preserve names in esbuild bundle by <a href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a href="https://redirect.github.com/docker/setup-buildx-action/pull/572">docker/setup-buildx-action#572</a></li>
<li>Bump <code>@​actions/core</code> from 3.0.0 to 3.0.1 in <a href="https://redirect.github.com/docker/setup-buildx-action/pull/551">docker/setup-buildx-action#551</a></li>
<li>Bump <code>@​docker/actions-toolkit</code> from 0.90.0 to 0.92.0 in <a href="https://redirect.github.com/docker/setup-buildx-action/pull/557">docker/setup-buildx-action#557</a> <a href="https://redirect.github.com/docker/setup-buildx-action/pull/580">docker/setup-buildx-action#580</a></li>
<li>Bump <code>@​sigstore/core</code> from 3.1.0 to 3.2.1 in <a href="https://redirect.github.com/docker/setup-buildx-action/pull/573">docker/setup-buildx-action#573</a></li>
<li>Bump <code>@​sigstore/verify</code> from 3.1.0 to 3.1.1 in <a href="https://redirect.github.com/docker/setup-buildx-action/pull/576">docker/setup-buildx-action#576</a></li>
<li>Bump js-yaml from 4.1.1 to 5.2.0 in <a href="https://redirect.github.com/docker/setup-buildx-action/pull/562">docker/setup-buildx-action#562</a></li>
<li>Bump sigstore from 4.1.0 to 4.1.1 in <a href="https://redirect.github.com/docker/setup-buildx-action/pull/577">docker/setup-buildx-action#577</a></li>
<li>Bump tmp from 0.2.5 to 0.2.7 in <a href="https://redirect.github.com/docker/setup-buildx-action/pull/556">docker/setup-buildx-action#556</a></li>
<li>Bump undici from 6.25.0 to 6.27.0 in <a href="https://redirect.github.com/docker/setup-buildx-action/pull/570">docker/setup-buildx-action#570</a></li>
<li>Bump vite from 7.3.2 to 7.3.6 in <a href="https://redirect.github.com/docker/setup-buildx-action/pull/569">docker/setup-buildx-action#569</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/docker/setup-buildx-action/compare/v4.1.0...v4.2.0">https://github.com/docker/setup-buildx-action/compare/v4.1.0...v4.2.0</a></p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/docker/setup-buildx-action/commit/bb05f3f5519dd87d3ba754cc423b652a5edd6d2c"><code>bb05f3f</code></a> Merge pull request <a href="https://redirect.github.com/docker/setup-buildx-action/issues/580">#580</a> from docker/dependabot/npm_and_yarn/docker/actions-to...</li>
<li><a href="https://github.com/docker/setup-buildx-action/commit/321c814cb51fbe4af8eca00249525cc0973ea66f"><code>321c814</code></a> [dependabot skip] chore: update generated content</li>
<li><a href="https://github.com/docker/setup-buildx-action/commit/b9a36ef79ba42cfc611885a1e8c388fbf8b8cb3f"><code>b9a36ef</code></a> build(deps): bump <code>@​docker/actions-toolkit</code> from 0.91.0 to 0.92.0</li>
<li><a href="https://github.com/docker/setup-buildx-action/commit/ebeab241289497cd564ac98b3cfc9e64607bb276"><code>ebeab24</code></a> Merge pull request <a href="https://redirect.github.com/docker/setup-buildx-action/issues/570">#570</a> from docker/dependabot/npm_and_yarn/undici-6.27.0</li>
<li><a href="https://github.com/docker/setup-buildx-action/commit/5c7b8ae78cec97a3215d4d86679b1d072eaa80cb"><code>5c7b8ae</code></a> [dependabot skip] chore: update generated content</li>
<li><a href="https://github.com/docker/setup-buildx-action/commit/037e618cd98e95e81525b15ff0e9c96f507e6a0e"><code>037e618</code></a> build(deps): bump undici from 6.25.0 to 6.27.0</li>
<li><a href="https://github.com/docker/setup-buildx-action/commit/66080e5802281ec2e72b7f3108915643e702db85"><code>66080e5</code></a> Merge pull request <a href="https://redirect.github.com/docker/setup-buildx-action/issues/577">#577</a> from docker/dependabot/npm_and_yarn/sigstore-4.1.1</li>
<li><a href="https://github.com/docker/setup-buildx-action/commit/409aef0aa3f48f0a742e7dec4e0e04ab19afe93c"><code>409aef0</code></a> Merge pull request <a href="https://redirect.github.com/docker/setup-buildx-action/issues/562">#562</a> from docker/dependabot/npm_and_yarn/js-yaml-4.2.0</li>
<li><a href="https://github.com/docker/setup-buildx-action/commit/49c6e42949280fa0d70fb327633591be54efbfb6"><code>49c6e42</code></a> build(deps): bump sigstore from 4.1.0 to 4.1.1</li>
<li><a href="https://github.com/docker/setup-buildx-action/commit/2211273e8121ecf9ecb7d6c7c0fcd55526d530c7"><code>2211273</code></a> [dependabot skip] chore: update generated content</li>
<li>Additional commits viewable in <a href="https://github.com/docker/setup-buildx-action/compare/d7f5e7f509e45cec5c76c4d5afdd7de93d0b3df5...bb05f3f5519dd87d3ba754cc423b652a5edd6d2c">compare view</a></li>
</ul>
</details>
<br />

Updates `docker/login-action` from 4.2.0 to 4.4.0
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/docker/login-action/releases">docker/login-action's releases</a>.</em></p>
<blockquote>
<h2>v4.4.0</h2>
<ul>
<li>Skip empty <code>registry-auth</code> secret mask by <a href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a href="https://redirect.github.com/docker/login-action/pull/1035">docker/login-action#1035</a></li>
<li>Bump <code>@​aws-sdk/client-ecr</code> and <code>@​aws-sdk/client-ecr-public</code> to 3.1077.0 <a href="https://redirect.github.com/docker/login-action/pull/1034">docker/login-action#1034</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/docker/login-action/compare/v4.3.0...v4.4.0">https://github.com/docker/login-action/compare/v4.3.0...v4.4.0</a></p>
<h2>v4.3.0</h2>
<ul>
<li>Preserve names in esbuild bundle by <a href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a href="https://redirect.github.com/docker/login-action/pull/1022">docker/login-action#1022</a></li>
<li>Bump <code>@​aws-sdk/client-ecr</code> and <code>@​aws-sdk/client-ecr-public</code> to 3.1076.0 <a href="https://redirect.github.com/docker/login-action/pull/999">docker/login-action#999</a> <a href="https://redirect.github.com/docker/login-action/pull/1030">docker/login-action#1030</a></li>
<li>Bump <code>@​docker/actions-toolkit</code> from 0.90.0 to 0.92.0 in <a href="https://redirect.github.com/docker/login-action/pull/1004">docker/login-action#1004</a> <a href="https://redirect.github.com/docker/login-action/pull/1027">docker/login-action#1027</a></li>
<li>Bump <code>@​sigstore/core</code> from 3.1.0 to 3.2.1 in <a href="https://redirect.github.com/docker/login-action/pull/1023">docker/login-action#1023</a></li>
<li>Bump <code>@​sigstore/verify</code> from 3.1.0 to 3.1.1 in <a href="https://redirect.github.com/docker/login-action/pull/1029">docker/login-action#1029</a></li>
<li>Bump http-proxy-agent and https-proxy-agent to 9.1.0 in <a href="https://redirect.github.com/docker/login-action/pull/1017">docker/login-action#1017</a></li>
<li>Bump js-yaml from 4.1.1 to 5.2.0 in <a href="https://redirect.github.com/docker/login-action/pull/1028">docker/login-action#1028</a></li>
<li>Bump sigstore from 4.1.0 to 4.1.1 in <a href="https://redirect.github.com/docker/login-action/pull/1031">docker/login-action#1031</a></li>
<li>Bump tmp from 0.2.5 to 0.2.7 in <a href="https://redirect.github.com/docker/login-action/pull/1002">docker/login-action#1002</a></li>
<li>Bump undici from 6.24.1 to 6.27.0 in <a href="https://redirect.github.com/docker/login-action/pull/1020">docker/login-action#1020</a></li>
<li>Bump vite from 7.3.3 to 7.3.6 in <a href="https://redirect.github.com/docker/login-action/pull/1019">docker/login-action#1019</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/docker/login-action/compare/v4.2.0...v4.3.0">https://github.com/docker/login-action/compare/v4.2.0...v4.3.0</a></p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/docker/login-action/commit/af1e73f918a031802d376d3c8bbc3fe56130a9b0"><code>af1e73f</code></a> Merge pull request <a href="https://redirect.github.com/docker/login-action/issues/1034">#1034</a> from docker/dependabot/npm_and_yarn/aws-sdk-dependen...</li>
<li><a href="https://github.com/docker/login-action/commit/da722bde43bacb027adfc67d42dbaa4c0f9e550b"><code>da722bd</code></a> [dependabot skip] chore: update generated content</li>
<li><a href="https://github.com/docker/login-action/commit/2916ad60bd5cb72f07aa54c69fdcc61749c09b7a"><code>2916ad6</code></a> build(deps): bump the aws-sdk-dependencies group across 1 directory with 2 up...</li>
<li><a href="https://github.com/docker/login-action/commit/ca0a662f786e4cfddce972005bd68f3dafc3a903"><code>ca0a662</code></a> Merge pull request <a href="https://redirect.github.com/docker/login-action/issues/1035">#1035</a> from crazy-max/fix-registry-auth-empty-mask</li>
<li><a href="https://github.com/docker/login-action/commit/c455755a579833bf0d2e4e54e3beb413ef10cc80"><code>c455755</code></a> chore: update generated content</li>
<li><a href="https://github.com/docker/login-action/commit/48351901f89581a7c12870c787d3f06d1f498438"><code>4835190</code></a> skip empty registry-auth secret mask</li>
<li><a href="https://github.com/docker/login-action/commit/992421c6e6806a7f6df609d1bfff374f9eca3004"><code>992421c</code></a> Merge pull request <a href="https://redirect.github.com/docker/login-action/issues/1033">#1033</a> from docker/dependabot/github_actions/docker/bake-ac...</li>
<li><a href="https://github.com/docker/login-action/commit/b249b43765525dd7951068267a34cf63f22ab4f0"><code>b249b43</code></a> Merge pull request <a href="https://redirect.github.com/docker/login-action/issues/1032">#1032</a> from docker/dependabot/github_actions/docker/bake-ac...</li>
<li><a href="https://github.com/docker/login-action/commit/1b67977736863551a88ff218642a2d7628b10520"><code>1b67977</code></a> build(deps): bump docker/bake-action from 7.2.0 to 7.3.0</li>
<li><a href="https://github.com/docker/login-action/commit/9d49d6a3234c78daa10c3c12183ef7b6caa8e69e"><code>9d49d6a</code></a> build(deps): bump docker/bake-action/subaction/matrix</li>
<li>Additional commits viewable in <a href="https://github.com/docker/login-action/compare/650006c6eb7dba73a995cc03b0b2d7f5ca915bee...af1e73f918a031802d376d3c8bbc3fe56130a9b0">compare view</a></li>
</ul>
</details>
<br />

Updates `docker/build-push-action` from 7.2.0 to 7.3.0
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/docker/build-push-action/releases">docker/build-push-action's releases</a>.</em></p>
<blockquote>
<h2>v7.3.0</h2>
<ul>
<li>Preserve names in esbuild bundle by <a href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a href="https://redirect.github.com/docker/build-push-action/pull/1567">docker/build-push-action#1567</a></li>
<li>Bump <code>@​docker/actions-toolkit</code> from 0.90.0 to 0.92.0 in <a href="https://redirect.github.com/docker/build-push-action/pull/1545">docker/build-push-action#1545</a> <a href="https://redirect.github.com/docker/build-push-action/pull/1572">docker/build-push-action#1572</a></li>
<li>Bump <code>@​sigstore/core</code> from 3.1.0 to 3.2.1 in <a href="https://redirect.github.com/docker/build-push-action/pull/1568">docker/build-push-action#1568</a></li>
<li>Bump js-yaml from 4.1.1 to 4.3.0 in <a href="https://redirect.github.com/docker/build-push-action/pull/1566">docker/build-push-action#1566</a></li>
<li>Bump tmp from 0.2.5 to 0.2.7 in <a href="https://redirect.github.com/docker/build-push-action/pull/1547">docker/build-push-action#1547</a></li>
<li>Bump undici from 6.24.1 to 6.27.0 in <a href="https://redirect.github.com/docker/build-push-action/pull/1564">docker/build-push-action#1564</a></li>
<li>Bump vite from 7.3.2 to 7.3.6 in <a href="https://redirect.github.com/docker/build-push-action/pull/1563">docker/build-push-action#1563</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/docker/build-push-action/compare/v7.2.0...v7.3.0">https://github.com/docker/build-push-action/compare/v7.2.0...v7.3.0</a></p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/docker/build-push-action/commit/53b7df96c91f9c12dcc8a07bcb9ccacbed38856a"><code>53b7df9</code></a> Merge pull request <a href="https://redirect.github.com/docker/build-push-action/issues/1572">#1572</a> from docker/dependabot/npm_and_yarn/docker/actions-t...</li>
<li><a href="https://github.com/docker/build-push-action/commit/154298c1ca89be1c0e019084f0611ddca621aafc"><code>154298c</code></a> [dependabot skip] chore: update generated content</li>
<li><a href="https://github.com/docker/build-push-action/commit/cb1238b9c9eb453d106b4e4142a5bd9cde710040"><code>cb1238b</code></a> chore(deps): Bump <code>@​docker/actions-toolkit</code> from 0.91.0 to 0.92.0</li>
<li><a href="https://github.com/docker/build-push-action/commit/24f845d5cbe75d2d350a984fd0e18cb7a3f29c1c"><code>24f845d</code></a> Merge pull request <a href="https://redirect.github.com/docker/build-push-action/issues/1566">#1566</a> from docker/dependabot/npm_and_yarn/js-yaml-4.2.0</li>
<li><a href="https://github.com/docker/build-push-action/commit/9c6973007b52c322651c38915d5e8824cea95c50"><code>9c69730</code></a> [dependabot skip] chore: update generated content</li>
<li><a href="https://github.com/docker/build-push-action/commit/bc3a3a5f72a6dca16c2c2468d1dfc55ee66d2193"><code>bc3a3a5</code></a> Merge pull request <a href="https://redirect.github.com/docker/build-push-action/issues/1574">#1574</a> from docker/dependabot/github_actions/aws-actions/co...</li>
<li><a href="https://github.com/docker/build-push-action/commit/a82c504a2387bb8bedc50072f9c554ae2a7dab5d"><code>a82c504</code></a> chore(deps): Bump js-yaml from 4.1.1 to 4.3.0</li>
<li><a href="https://github.com/docker/build-push-action/commit/0285a75190c039d6dac52b7711abcef3f5d8f6f6"><code>0285a75</code></a> Merge pull request <a href="https://redirect.github.com/docker/build-push-action/issues/1573">#1573</a> from docker/dependabot/github_actions/actions/cache-...</li>
<li><a href="https://github.com/docker/build-push-action/commit/c6ad2a3f9644680619de938b97c8a10a87b2a88d"><code>c6ad2a3</code></a> Merge pull request <a href="https://redirect.github.com/docker/build-push-action/issues/1575">#1575</a> from docker/dependabot/github_actions/actions/checko...</li>
<li><a href="https://github.com/docker/build-push-action/commit/d37484fb9737c5442a257e2f0ae5a8d756ed7d92"><code>d37484f</code></a> Merge pull request <a href="https://redirect.github.com/docker/build-push-action/issues/1564">#1564</a> from docker/dependabot/npm_and_yarn/undici-6.27.0</li>
<li>Additional commits viewable in <a href="https://github.com/docker/build-push-action/compare/f9f3042f7e2789586610d6e8b85c8f03e5195baf...53b7df96c91f9c12dcc8a07bcb9ccacbed38856a">compare view</a></li>
</ul>
</details>
<br />

Updates `trufflesecurity/trufflehog` from 3.95.6 to 3.95.8
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
</blockquote>
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
<li>Additional commits viewable in <a href="https://github.com/trufflesecurity/trufflehog/compare/30d5bb91af1a771378349dbbb0c82129392acf70...00155c9dc586f34d189adc83d3ac2698c2ec551f">compare view</a></li>
</ul>
</details>
<br />

Updates `huggingface/doc-builder/.github/workflows/upload_pr_documentation.yml` from 4a384d0ccdeb8502a57f1003acee938b42a5592a to 0f4784322c564503c4a4d67ccb7fba29e32f111a
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/huggingface/doc-builder/commit/0f4784322c564503c4a4d67ccb7fba29e32f111a"><code>0f47843</code></a> Mock optimum, torchao, gguf for diffusers docs (<a href="https://redirect.github.com/huggingface/doc-builder/issues/806">#806</a>)</li>
<li><a href="https://github.com/huggingface/doc-builder/commit/f8ab2e5246a13eaa31c4b3760701856fc5ab98a6"><code>f8ab2e5</code></a> Add bitsandbytes (mock) and sentencepiece (real) to diffusers doc deps (<a href="https://redirect.github.com/huggingface/doc-builder/issues/805">#805</a>)</li>
<li>See full diff in <a href="https://github.com/huggingface/doc-builder/compare/4a384d0ccdeb8502a57f1003acee938b42a5592a...0f4784322c564503c4a4d67ccb7fba29e32f111a">compare view</a></li>
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

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Routine CI dependency bumps with no runtime or product code changes; Docker and secret-scanning workflows use the same inputs and secrets as before.
> 
> **Overview**
> Bumps pinned **GitHub Actions** versions across CI workflows only; no application or library code changes.
> 
> **Documentation** workflows (`build_documentation`, `build_pr_documentation`, `upload_pr_documentation`) now call `huggingface/doc-builder` reusable workflows at commit `0f478432` instead of `4a384d0`.
> 
> **CodeQL** (`codeQL.yml`) updates `github/codeql-action` **init** and **analyze** from **v4.36.2** to **v4.36.3**.
> 
> **Docker** (`docker-build.yml`) bumps **setup-buildx-action** to **v4.2.0**, **login-action** to **v4.4.0**, and **build-push-action** to **v7.3.0** for both `trl` and `trl-dev` jobs.
> 
> **Secret scanning** (`trufflehog.yml`) moves **trufflesecurity/trufflehog** from **v3.95.6** to **v3.95.8**.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit 3da571da502d95273aee0c10983bbfcba91bc8c7. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->