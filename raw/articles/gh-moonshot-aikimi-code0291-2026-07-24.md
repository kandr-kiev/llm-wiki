---
source_url: https://github.com/moonshotai/kimi-code/releases/tag/@moonshot-ai/kimi-code@0.29.1
ingested: 2026-07-24
sha256: 4c613908fc1c7e0c13cb8a2e3a4365625b0a78b34891bb07eac0ac5ee854f5f3
blog_source: github:moonshotai/kimi-code
---
# Release @moonshot-ai/kimi-code@0.29.1

### Patch Changes

- [#2065](https://github.com/MoonshotAI/kimi-code/pull/2065) [`527d485`](https://github.com/MoonshotAI/kimi-code/commit/527d485d9296fe20f473a4a578d9e6a499c20cd9) Thanks [@7Sageer](https://github.com/7Sageer)! - Add global default MCP server timeouts in `config.toml` and env vars.

- [#2104](https://github.com/MoonshotAI/kimi-code/pull/2104) [`66f611a`](https://github.com/MoonshotAI/kimi-code/commit/66f611aae99887ad2076aa3482a0df5e415d3511) Thanks [@RealKai42](https://github.com/RealKai42)! - Fix loss of thinking content with OpenAI-compatible endpoints that return reasoning under a different field name (e.g. newer vLLM); the reasoning field is now detected per endpoint and echoed back on follow-up requests.

- [#2089](https://github.com/MoonshotAI/kimi-code/pull/2089) [`ca38b7e`](https://github.com/MoonshotAI/kimi-code/commit/ca38b7ed864ad5fa2b2e3c8b96d8a7b10a734445) Thanks [@liruifengv](https://github.com/liruifengv)! - Remove the toolbar tip that suggested trying the "superpowers" plugin.

- [#2064](https://github.com/MoonshotAI/kimi-code/pull/2064) [`7b62ed5`](https://github.com/MoonshotAI/kimi-code/commit/7b62ed5b2c2709719f360c01a2f513dee34ae179) Thanks [@7Sageer](https://github.com/7Sageer)! - Add experimental secondary-model bindings for newly spawned subagents, including per-agent model preferences and subagent-only model overrides.

- [#2096](https://github.com/MoonshotAI/kimi-code/pull/2096) [`5fdbdb4`](https://github.com/MoonshotAI/kimi-code/commit/5fdbdb4a22b86ae6f7ba7c775741689aaaf215f0) Thanks [@7Sageer](https://github.com/7Sageer)! - Add environment variables to configure the web search and web fetch services without OAuth login.