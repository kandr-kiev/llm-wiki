---
title: "Issue #2846: Add recipe: parse any document with the Unstructured Transform MCP server"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - foundation-model
  - guide
  - integration
  - multi-agent
  - open-source
  - pipeline
  - real-time
  - review
  - self-supervised
  - tool
---
# Issue #2846: Add recipe: parse any document with the Unstructured Transform MCP server

> **Source:** gh-openaiopenai-cookbook-issue-2846-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/openai/openai-cookbook/issues/2846 ingested: 2026-07-11 sha256: 0ca5ed7408b9283fa21971dccdb7a345ae56121190c26184fea04461392d04b8 blog_source: github:openai/openai-co...
> **Sources:**
>   - gh-openaiopenai-cookbook-issue-2846-2026-07-11.md
> **Links:**
- [[away]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[issue-6358-add-trlenvironments-submodule-with-sandboxenvironment]]
- [[issue-6361-critical-training-chat-template-issue-with-qwen35-models-in-chat_template_utils]]
- [[issue-6362-add-security-policy-to-the-repo]]

## Key Findings

---
source_url: https://github.com/openai/openai-cookbook/issues/2846
ingested: 2026-07-11
sha256: 0ca5ed7408b9283fa21971dccdb7a345ae56121190c26184fea04461392d04b8
blog_source: github:openai/openai-cookbook
---
# Issue #2846: Add recipe: parse any document with the Unstructured Transform MCP server
**State:** open | **Author:** ajaykrish-uns | **Created:** 2026-07-10T17:57:00Z
## Summary
Adds a new Cookbook recipe: **Parse documents with the Unstructured Transform MCP server**
(`examples/mcp/unstructured-transform/`). It shows how to connect Unstructured's hosted
Transform MCP server (`https://mcp.transform.unstructured.io/`) to the OpenAI **Responses API**
as an `mcp` tool, have the model parse a complex, table-heavy PDF ("Attention Is All You Need")
into clean markdown, and then answer questions grounded in the parsed content. Includes the
`registry.yaml` and `authors.yaml` entries.
## Motivation
Real-world documents likr scanned PDFs, multi-column layouts, nested tables are hard to feed to a
model directly, and building/hosting a parsing pipeline is a common blocker. This recipe shows a
minimal, fully hosted path: the model calls a remote MCP server on demand to turn 60+ file types
into clean structured output, with no custom extraction code. 
The Cookbook currently has a general MCP tool guide but no document-parsing integration, so this adds a practical, end-to-end example of combining the Responses API MCP tool with a third-party remote MCP server (bearer-token auth,
out-of-band result handling, and grounded Q&A).
---
## For new content
- [x] I have added a new entry in registry.yaml (and, optionally, in authors.yaml) so that my content renders on the cookbook website.
- [x] I have conducted a self-review of my content based on the contribution guidelines:
- [x] Relevance: This content is related to building with OpenAI technologies and is useful to others.
- [x] Uniqueness: I have searched for related examples in the OpenAI Cookbook, and verified that my content offers new insights or unique information compared to existing documentation.
- [x] Spelling and Grammar: I have checked for spelling or grammatical mistakes.
- [x] Clarity: I have done a final read-through and verified that my submission is well-organized and easy to understand.
- [x] Correctness: The information I include is correct and all of my code executes successfully.
- [x] Completeness: I have explained everything fully, including all necessary references and citations.

## Summary

See Key Findings for full content.

## Related Articles

- [[away]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[issue-6358-add-trlenvironments-submodule-with-sandboxenvironment]]
- [[issue-6361-critical-training-chat-template-issue-with-qwen35-models-in-chat_template_utils]]
- [[issue-6362-add-security-policy-to-the-repo]]
