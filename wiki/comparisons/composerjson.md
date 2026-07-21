---
title: "composer.json"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - deep-learning
  - library
---

# composer.json

> **Source:** local-ai-education-provendormyclabsdeep-copycomposerjson-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/AI-Education-Pro/vendor/myclabs/deep-copy/composer.json ingested: 2026-07-20 sha256: 36c96afa05923f8f7eacde67a64f69e826f1d32b93e0803b62cd5cf93e83cd16 blog_so...
> **Sources:**
>   - local-ai-education-provendormyclabsdeep-copycomposerjson-2026-07-20.md
> **Links:**
- [[installed.json]]
- [[package.json]]
- [[Local LLM Wiki Algorithm]]
- [[add lesson]]
- [[database setup]]

## Key Findings

---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/myclabs/deep-copy/composer.json
ingested: 2026-07-20
sha256: 36c96afa05923f8f7eacde67a64f69e826f1d32b93e0803b62cd5cf93e83cd16
blog_source: local:unknown
---
{
"name": "myclabs/deep-copy",
"description": "Create deep copies (clones) of your objects",
"license": "MIT",
"type": "library",
"keywords": [
"clone",
"copy",
"duplicate",
"object",
"object graph"
],
"require": {
"php": "^7.1 || ^8.0"
},
"require-dev": {
"doctrine/collections": "^1.6.8",
"doctrine/common": "^2.13.3 || ^3.2.2",
"phpspec/prophecy": "^1.10",
"phpunit/phpunit": "^7.5.20 || ^8.5.23 || ^9.5.13"
},
"conflict": {
"doctrine/collections": "=3 <3.2.2"
},
"autoload": {
"psr-4": {
"DeepCopy\\": "src/DeepCopy/"
},
"files": [
"src/DeepCopy/deep_copy.php"
]
},
"autoload-dev": {
"psr-4": {
"DeepCopyTest\\": "tests/DeepCopyTest/",
"DeepCopy\\": "fixtures/"
}
},
"config": {
"sort-packages": true
}
}

## Summary

See Key Findings for full content.

## Related Articles

- [[installed.json]]
- [[package.json]]
- [[Local LLM Wiki Algorithm]]
- [[add lesson]]
- [[database setup]]
