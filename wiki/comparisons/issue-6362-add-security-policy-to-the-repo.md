---
title: "Issue #6362: Add security policy to the repo"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - foundation-model
  - library
  - open-source
  - policy
  - research
  - security
  - tool
---
# Issue #6362: Add security policy to the repo

> **Source:** gh-huggingfacetrl-issue-6362-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/trl/issues/6362 ingested: 2026-07-11 sha256: 2d664b5bc6239cbd1d83f364c9ad7de23f490c7105bcbbe4436a7ae00c0439df blog_source: github:huggingface/trl --- # I...
> **Sources:**
>   - gh-huggingfacetrl-issue-6362-2026-07-11.md
> **Links:**
- [[issue-6358-add-trlenvironments-submodule-with-sandboxenvironment]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[issue-6359-truncate-gold-on-policy-prompts-before-generation-keeping-the-prompt-end]]
- [[issue-6361-critical-training-chat-template-issue-with-qwen35-models-in-chat_template_utils]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]

## Key Findings

---
source_url: https://github.com/huggingface/trl/issues/6362
ingested: 2026-07-11
sha256: 2d664b5bc6239cbd1d83f364c9ad7de23f490c7105bcbbe4436a7ae00c0439df
blog_source: github:huggingface/trl
---
# Issue #6362: Add security policy to the repo
**State:** open | **Author:** albertvillanova | **Created:** 2026-07-11T10:26:58Z
This PR adds a comprehensive `SECURITY.md` file to the repository, establishing clear guidelines for reporting and handling security vulnerabilities. The document outlines supported versions, reporting procedures, recognition for reporters, required report content, and the project's threat model and scope for vulnerabilities.
CC: @Michellehbn 
### Changes
Security policy and vulnerability reporting:
* Added a detailed security policy in `SECURITY.md`, specifying supported versions, private reporting procedures (via GitHub or email), and recognition for valid reports.
* Defined the required structure and content for vulnerability reports, including proof of concept, impact, and affected versions, to ensure actionable submissions.
Scope and threat model clarification:
* Clearly outlined what is considered in-scope and out-of-scope for security issues, including the risks of loading untrusted artifacts and the boundaries of the library's responsibility.
* Explained the trust boundaries and threat model, emphasizing documented risks and the distinction between library API vulnerabilities and operator/utility tool usage.
Safe harbor and responsible disclosure:
* Included a safe harbor statement to encourage good-faith security research and responsible disclosure practices.
---
> [!NOTE]
> **Low Risk**
> Documentation-only addition with no runtime, API, or dependency changes.
> 
> **Overview**
> Adds a new **`SECURITY.md`** so GitHub and researchers have a single, authoritative security policy for the repo.
> 
> It defines **how to report** (private GitHub advisory preferred, **security@huggingface.co** as fallback), that fixes ship only on the **latest release**, and **recognition** via advisories/CVE credit without a bounty.
> 
> It also sets **triage expectations**: a mandatory report template (version, PoC, impact, scope), a **threat model** (untrusted artifact loading, `safetensors` / revision pinning / `trust_remote_code`, CLI as operator tools), explicit **in-scope vs out-of-scope** rules, and a **safe harbor** for good-faith disclosure.
> 
> Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit bf67dc56cf822afca904fd5550d26bb0fa1663d3. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).

## Summary

See Key Findings for full content.

## Related Articles

- [[issue-6358-add-trlenvironments-submodule-with-sandboxenvironment]]
- [[issue-14167-flashpack-support-for-transformers-pipeline-components]]
- [[issue-6359-truncate-gold-on-policy-prompts-before-generation-keeping-the-prompt-end]]
- [[issue-6361-critical-training-chat-template-issue-with-qwen35-models-in-chat_template_utils]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
