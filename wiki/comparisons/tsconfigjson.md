---
title: "tsconfig.json"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
---

# tsconfig.json

> **Source:** local-ai-education-proclienttsconfigjson-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/AI-Education-Pro/client/tsconfig.json ingested: 2026-07-20 sha256: 53c72fe767c5b91e916bbae32bf2d1a05104573a35db158b48fa94c8204be580 blog_source: local:unknow...
> **Sources:**
>   - local-ai-education-proclienttsconfigjson-2026-07-20.md
> **Links:**
- [[package.json]]
- [[app.js]]
- [[database setup]]
- [[add lesson]]
- [[deploy]]

## Key Findings

---
source_url: file:///workspace/Projects/AI-Education-Pro/client/tsconfig.json
ingested: 2026-07-20
sha256: 53c72fe767c5b91e916bbae32bf2d1a05104573a35db158b48fa94c8204be580
blog_source: local:unknown
---
{
"compilerOptions": {
"target": "ES2020",
"useDefineForClassFields": true,
"lib": [
"ES2020",
"DOM",
"DOM.Iterable"
],
"module": "ESNext",
"skipLibCheck": true,
"esModuleInterop": true,
"allowSyntheticDefaultImports": true,
"moduleResolution": "bundler",
"allowImportingTsExtensions": true,
"resolveJsonModule": true,
"isolatedModules": true,
"noEmit": true,
"jsx": "react-jsx",
"strict": true,
"noUnusedLocals": true,
"noUnusedParameters": true,
"noFallthroughCasesInSwitch": true
},
"include": [
"src"
],
"references": [
{
"path": "./tsconfig.node.json"
}
]
}

## Summary

See Key Findings for full content.

## Related Articles

- [[package.json]]
- [[app.js]]
- [[database setup]]
- [[add lesson]]
- [[deploy]]
