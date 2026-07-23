---
source_url: https://github.com/moonshotai/kimi-code/releases/tag/@moonshot-ai/kimi-code@0.29.0
ingested: 2026-07-22
sha256: 3f5f8fd9638931d9ad00e82160ff49a8e4f2570d15989ab8ffaf14e1b6222ea6
blog_source: github:moonshotai/kimi-code
---
# Release @moonshot-ai/kimi-code@0.29.0

### Minor Changes

- [#1992](https://github.com/MoonshotAI/kimi-code/pull/1992) [`a8f1ca3`](https://github.com/MoonshotAI/kimi-code/commit/a8f1ca3f1016a3e84986f297367e833bc731ac39) Thanks [@RealKai42](https://github.com/RealKai42)! - Support selecting a thinking effort level from ACP clients: the thinking picker now lists the current model's declared levels (for example off / low / medium / high) instead of only an on/off toggle. Use the thinking selector in your ACP client (e.g. Zed) to pick a level; the legacy on/off values keep working.

- [#1735](https://github.com/MoonshotAI/kimi-code/pull/1735) [`ce0e3ce`](https://github.com/MoonshotAI/kimi-code/commit/ce0e3ceb04223bdaad8e8931bad46eff561055b6) Thanks [@7Sageer](https://github.com/7Sageer)! - Let custom agent files restrict which sub-agent types they may delegate to (v2 engine only).

- [#1735](https://github.com/MoonshotAI/kimi-code/pull/1735) [`ce0e3ce`](https://github.com/MoonshotAI/kimi-code/commit/ce0e3ceb04223bdaad8e8931bad46eff561055b6) Thanks [@7Sageer](https://github.com/7Sageer)! - Support custom agents defined as Markdown files with frontmatter, usable as the main agent or a sub-agent (v2 engine only).

- [#1735](https://github.com/MoonshotAI/kimi-code/pull/1735) [`ce0e3ce`](https://github.com/MoonshotAI/kimi-code/commit/ce0e3ceb04223bdaad8e8931bad46eff561055b6) Thanks [@7Sageer](https://github.com/7Sageer)! - Add global tool gating to constrain which tools agents may use, with a per-session override (v2 engine only).

- [#2012](https://github.com/MoonshotAI/kimi-code/pull/2012) [`d67a200`](https://github.com/MoonshotAI/kimi-code/commit/d67a2003abf2d8d802dcf24f806e0a811724b83e) Thanks [@sailist](https://github.com/sailist)! - Add a GET /api/v1/fs:content server endpoint that serves any file on the host by absolute path as raw content with Content-Type, ETag, and Range support.

- [#1999](https://github.com/MoonshotAI/kimi-code/pull/1999) [`4c763f6`](https://github.com/MoonshotAI/kimi-code/commit/4c763f6763acb67a73d133f7450d092e71d63692) Thanks [@RealKai42](https://github.com/RealKai42)! - Videos attached to a prompt — pasted in the TUI or uploaded in the web UI — now reach the model together with the prompt, with no extra tool round trip, and stay playable in the chat after a reload.

- [#1735](https://github.com/MoonshotAI/kimi-code/pull/1735) [`ce0e3ce`](https://github.com/MoonshotAI/kimi-code/commit/ce0e3ceb04223bdaad8e8931bad46eff561055b6) Thanks [@7Sageer](https://github.com/7Sageer)! - Support overriding the default main-agent system prompt with a user-level file for every session (v2 engine only).

### Patch Changes

- [#1997](https://github.com/MoonshotAI/kimi-code/pull/1997) [`74da87a`](https://github.com/MoonshotAI/kimi-code/commit/74da87a457c2964694a844dd22a4925f5113b167) Thanks [@sailist](https://github.com/sailist)! - Add agent.created and agent.disposed events to the server session event stream, and expose each agent's disposal time in the transcript API.

- [#2030](https://github.com/MoonshotAI/kimi-code/pull/2030) [`ec88d35`](https://github.com/MoonshotAI/kimi-code/commit/ec88d352e8f4dc5e8ffd1212f016138458f69893) Thanks [@RealKai42](https://github.com/RealKai42)! - Fix catalog-imported Claude models being wrongly locked into always-on thinking, and stop offering a misleading thinking Off option for models that cannot truly disable reasoning (such as Gemini 3). Also normalizes configured thinking effort values and unifies context-usage reporting.

- [#2015](https://github.com/MoonshotAI/kimi-code/pull/2015) [`b5efba7`](https://github.com/MoonshotAI/kimi-code/commit/b5efba7abcaf4041f81ec520097a61e6546e8c50) Thanks [@RealKai42](https://github.com/RealKai42)! - Import many more providers from the models.dev catalog: vendor SDKs like xai and openrouter now import instead of being refused (with a "guessed" note), deprecated and alpha models are filtered out, per-model gateway protocol and endpoint overrides are honored, and context limits are correct (input limit for compaction, total window for completion). Imports lacking a usable endpoint now ask for one via `--base-url` or a prompt.

- [#1993](https://github.com/MoonshotAI/kimi-code/pull/1993) [`37eda4e`](https://github.com/MoonshotAI/kimi-code/commit/37eda4e59aebc8ecafa91be3f43f971ed63963a3) Thanks [@RealKai42](https://github.com/RealKai42)! - Add environment variable overrides for agent loop and background task limits. Set KIMI_LOOP_MAX_STEPS_PER_TURN, KIMI_LOOP_MAX_RETRIES_PER_STEP, or KIMI_CODE_BACKGROUND_MAX_RUNNING_TASKS to take priority over the [loop_control] and [background] config.

- [#1993](https://github.com/MoonshotAI/kimi-code/pull/1993) [`37eda4e`](https://github.com/MoonshotAI/kimi-code/commit/37eda4e59aebc8ecafa91be3f43f971ed63963a3) Thanks [@RealKai42](https://github.com/RealKai42)! - Fix config environment overrides (such as KIMI_IMAGE_MAX_EDGE_PX or KIMI_SUBAGENT_TIMEOUT_MS) being persisted into config.toml by config API writes while the env var is set, and keeping the old value after the env var is changed to an invalid value or removed.

- [#2050](https://github.com/MoonshotAI/kimi-code/pull/2050) [`8250e59`](https://github.com/MoonshotAI/kimi-code/commit/8250e590f3ed5990c233ef5a2c7666468f0bcb05) Thanks [@sailist](https://github.com/sailist)! - Remove references to the non-existent `kimi resume` command from the scheduled-task tool descriptions.

- [#1970](https://github.com/MoonshotAI/kimi-code/pull/1970) [`6dd4fd3`](https://github.com/MoonshotAI/kimi-code/commit/6dd4fd33688b37904d5302436fc2daaf09d66c7d) Thanks [@sailist](https://github.com/sailist)! - Fix cancelled model requests being wrapped as retryable provider errors, so interrupting a request no longer triggers silent retries.

- [#1970](https://github.com/MoonshotAI/kimi-code/pull/1970) [`6dd4fd3`](https://github.com/MoonshotAI/kimi-code/commit/6dd4fd33688b37904d5302436fc2daaf09d66c7d) Thanks [@sailist](https://github.com/sailist)! - Send the session prompt cache key to OpenAI and OpenAI Responses providers, restoring provider-side prompt cache affinity that previously only reached Kimi and Anthropic.

- [#1999](https://github.com/MoonshotAI/kimi-code/pull/1999) [`4c763f6`](https://github.com/MoonshotAI/kimi-code/commit/4c763f6763acb67a73d133f7450d092e71d63692) Thanks [@RealKai42](https://github.com/RealKai42)! - Fix ReadMediaFile failing on videos when the provider has no file upload channel — such videos now fall back to inline delivery.

- [#1968](https://github.com/MoonshotAI/kimi-code/pull/1968) [`71bcfba`](https://github.com/MoonshotAI/kimi-code/commit/71bcfba54a6836f4b6d4e26babde67576b293a64) Thanks [@RealKai42](https://github.com/RealKai42)! - Fix sessions getting stuck on every turn with a provider "message must not be empty" error after a content-filtered response.

- [#2022](https://github.com/MoonshotAI/kimi-code/pull/2022) [`154e082`](https://github.com/MoonshotAI/kimi-code/commit/154e0824880c8573433e4ec7ada083744dbfe9f9) Thanks [@wbxl2000](https://github.com/wbxl2000)! - web: Show transparent images over a checkerboard canvas so white and black content stays visible in both light and dark themes.

- [#1990](https://github.com/MoonshotAI/kimi-code/pull/1990) [`115b096`](https://github.com/MoonshotAI/kimi-code/commit/115b0968cefede7fac1494c6f0154ea5545a89da) Thanks [@liruifengv](https://github.com/liruifengv)! - Fix goal mode continuation prompts leaking into the transcript when resuming a session.

- [#1970](https://github.com/MoonshotAI/kimi-code/pull/1970) [`6dd4fd3`](https://github.com/MoonshotAI/kimi-code/commit/6dd4fd33688b37904d5302436fc2daaf09d66c7d) Thanks [@sailist](https://github.com/sailist)! - Rework the model wire layer in the experimental v2 engine into a small set of protocol bases plus declarative provider trait definitions, so adding a provider no longer means copying adapter code, and per-turn request intent (cache key, thinking effort, sampling) flows as request parameters instead of cloned model objects. The never-functional `[platforms]` config section and the `provider.platformId` field are removed; credential resolution is now a two-layer model → provider lookup.

- [#1976](https://github.com/MoonshotAI/kimi-code/pull/1976) [`e458323`](https://github.com/MoonshotAI/kimi-code/commit/e45832398d0d9cad98dbad1cbf1e5b103a20aace) Thanks [@liruifengv](https://github.com/liruifengv)! - Improve TUI performance and resume speed for long-running sessions.

- [#1991](https://github.com/MoonshotAI/kimi-code/pull/1991) [`92576e4`](https://github.com/MoonshotAI/kimi-code/commit/92576e4d850ada51a24e72fe76a83cc512df922a) Thanks [@7Sageer](https://github.com/7Sageer)! - Reconnect a dropped MCP server connection automatically when one of its tools is called, and retry the call once.

- [#1970](https://github.com/MoonshotAI/kimi-code/pull/1970) [`6dd4fd3`](https://github.com/MoonshotAI/kimi-code/commit/6dd4fd33688b37904d5302436fc2daaf09d66c7d) Thanks [@sailist](https://github.com/sailist)! - Add read-only model resolution inspection and a live connectivity probe to the server's RPC surface, reporting per-field value provenance (config, override, builtin, env, synthesized) for internal debugging tools.

- [#2015](https://github.com/MoonshotAI/kimi-code/pull/2015) [`b5efba7`](https://github.com/MoonshotAI/kimi-code/commit/b5efba7abcaf4041f81ec520097a61e6546e8c50) Thanks [@RealKai42](https://github.com/RealKai42)! - Fix thinking levels being offered for models that do not support them (e.g. phantom levels on Kimi K3): levels now come from each model's declared capabilities. Models that cannot disable reasoning (e.g. gpt-5) no longer offer an Off option, and turning thinking Off on models that support it (e.g. xai grok) now truly disables reasoning.

- [#1735](https://github.com/MoonshotAI/kimi-code/pull/1735) [`ce0e3ce`](https://github.com/MoonshotAI/kimi-code/commit/ce0e3ceb04223bdaad8e8931bad46eff561055b6) Thanks [@7Sageer](https://github.com/7Sageer)! - Warn when a tool allow/deny list entry can never match any tool, for example a misspelled name (v2 engine only).

- [#2005](https://github.com/MoonshotAI/kimi-code/pull/2005) [`a3699dd`](https://github.com/MoonshotAI/kimi-code/commit/a3699dd6aa7b41efd3129a117007d195282379fd) Thanks [@7Sageer](https://github.com/7Sageer)! - Add an `active` flag to each tool in the server's tool listing API.

- [#1995](https://github.com/MoonshotAI/kimi-code/pull/1995) [`73eb5f8`](https://github.com/MoonshotAI/kimi-code/commit/73eb5f89e06fb15d42c7585a147eb1c5caef0725) Thanks [@liruifengv](https://github.com/liruifengv)! - Remove red coloring from syntax highlighting in code previews and markdown code blocks.

- [#2014](https://github.com/MoonshotAI/kimi-code/pull/2014) [`576d650`](https://github.com/MoonshotAI/kimi-code/commit/576d65038035570bea90b58d5824bcd60ca11258) Thanks [@liruifengv](https://github.com/liruifengv)! - Add a reminder for third-party install sources to use the official installer in the update prompt.