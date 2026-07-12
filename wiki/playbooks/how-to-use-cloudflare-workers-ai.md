---
type: playbook
title: "How to Use Cloudflare Workers AI"
description: Actionable runbook for deploying and using Cloudflare Workers AI: REST API, model catalog, AI SDK, and production patterns
created: 2026-07-08
updated: 2026-07-08
tags: [playbook, cloudflare, serverless, reference, deployment]
sources: [raw/articles/cloudflare-workers-ai-rest-api-2026.md]
confidence: high
links: [cloudflare-workers-ai-rest-api, how-to-deploy-local-llm]
---# How to Use Cloudflare Workers AI

Actionable runbook for deploying and using Cloudflare Workers AI: REST API, model catalog, AI SDK, and production patterns.

## Prerequisites

- Cloudflare account (free tier available)
- Node.js 18+ or Python 3.10+
- Basic understanding of serverless functions

## Phase 1: Setup & Authentication

### Step 1.1 — Get API credentials

1. Go to Cloudflare Dashboard → Workers AI
2. Select "Use REST API"
3. Create a Workers AI API Token
4. Copy your Account ID from the dashboard

```bash
# Save credentials
export CLOUDFLARE_ACCOUNT_ID="your-account-id"
export CLOUDFLARE_API_TOKEN="your-api-token"
```

### Step 1.2 — Test with cURL

```bash
# Run a model via REST API
curl https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/run/@cf/meta/llama-3.1-8b-instruct \
  -H 'Authorization: Bearer ${CLOUDFLARE_API_TOKEN}' \
  -d '{ "prompt": "Where did the phrase Hello World come from?" }'
```

Expected response:
```json
{
  "result": {
    "response": "Hello, World first appeared in 1974 at Bell Labs..."
  },
  "success": true,
  "errors": [],
  "messages": []
}
```

## Phase 2: Model Catalog

### Step 2.1 — Available model categories

| Category | Models | Use Case |
|---|---|---|
| **Text Generation** | llama-3.1-8b-instruct, mistral-7b-instruct | Chat, text generation |
| **Text Embedding** | text-embedding-ada-002, bge-large | Vector search, RAG |
| **Image Generation** | stable-diffusion-v2-1, flux-schnell | Image creation |
| **Speech-to-Text** | whisper-large-v3 | Transcription |
| **Vision** | llava-1.5-7b, moondream | Image understanding |

### Step 2.2 — Run different models

```bash
# Mistral 7B Instruct
curl https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/run/@cf/mistral/mistral-7b-instruct-v0.1 \
  -H 'Authorization: Bearer ${CLOUDFLARE_API_TOKEN}' \
  -d '{ "prompt": "Explain quantum computing" }'

# Text embedding
curl https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/run/@cf/baai/bge-large-en-v1.5 \
  -H 'Authorization: Bearer ${CLOUDFLARE_API_TOKEN}' \
  -d '{ "text": "Hello, World!" }'

# Image generation
curl https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/run/@cf/stabilityai/stable-diffusion-xl-base-1.0 \
  -H 'Authorization: Bearer ${CLOUDFLARE_API_TOKEN}' \
  -d '{ "prompt": "A futuristic cityscape at sunset" }'
```

## Phase 3: AI SDK Integration

### Step 3.1 — Install SDK

```bash
# Node.js
npm install @cloudflare/ai

# Python
pip install cloudflare
```

### Step 3.2 — Node.js integration

```javascript
import { Cloudflare } from 'cloudflare';

const cf = new Cloudflare({
  apiToken: process.env.CLOUDFLARE_API_TOKEN
});

async function generateText(prompt) {
  const response = await cf.ai.run(
    '@cf/meta/llama-3.1-8b-instruct',
    {
      prompt: prompt,
      max_tokens: 512
    }
  );
  return response.result.response;
}

// Usage
const answer = await generateText('What is RAG?');
console.log(answer);
```

### Step 3.3 — Python integration

```python
from cloudflare import Cloudflare

cf = Cloudflare(api_key="YOUR_API_KEY")

def generate_text(prompt: str) -> str:
    response = cf.ai.run(
        "@cf/meta/llama-3.1-8b-instruct",
        {"prompt": prompt}
    )
    return response.result.response

# Usage
answer = generate_text("What is RAG?")
print(answer)
```

## Phase 4: Workers Integration

### Step 4.1 — Create a Worker with AI

```javascript
// worker.js
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const prompt = url.searchParams.get('q') || 'Hello';

    const response = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
      prompt: prompt,
      max_tokens: 256
    });

    return Response.json({
      answer: response.result.response
    });
  }
};
```

### Step 4.2 — Deploy the Worker

```bash
# Install Wrangler CLI
npm install -g wrangler

# Initialize project
wrangler init my-ai-worker

# Configure wrangler.toml
# [ai]
# binding = "AI"

# Deploy
wrangler deploy
```

### Step 4.3 — Test the deployed Worker

```bash
curl https://your-worker.your-subdomain.workers.dev/?q=What%20is%20AI%3F
```

## Phase 5: Production Patterns

### Step 5.1 — Caching AI responses

```javascript
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const prompt = url.searchParams.get('q');
    const cacheKey = `ai:${prompt}`;
    
    // Check cache first
    const cached = await caches.default.match(cacheKey);
    if (cached) return cached;
    
    // Generate and cache
    const response = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
      prompt: prompt
    });
    
    const result = Response.json({
      answer: response.result.response
    });
    
    // Cache for 1 hour
    ctx.waitUntil(caches.default.put(cacheKey, result.clone()));
    
    return result;
  }
};
```

### Step 5.2 — Streaming responses

```javascript
export default {
  async fetch(request, env) {
    const prompt = new URL(request.url).searchParams.get('q');
    
    const response = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
      prompt: prompt,
      stream: true
    });
    
    // Stream the response
    return new Response(response.result.stream, {
      headers: {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache'
      }
    });
  }
};
```

### Step 5.3 — Rate limiting

```javascript
// Use Cloudflare Rate Limiting rules
// Dashboard → Security → WAF → Rate Limiting Rules

// Example rule:
// - Match: URI pattern /ai/*
// - Condition: Same IP, 10 requests per minute
// - Action: Challenge (CAPTCHA)
```

## Phase 6: Cost Management

### Step 6.1 — Pricing overview

| Model | Price per 1M tokens |
|---|---|
| llama-3.1-8b-instruct | ~$0.20 |
| mistral-7b-instruct | ~$0.15 |
| text-embedding-ada-002 | ~$0.10 |
| Image generation | ~$0.04 per image |

### Step 6.2 — Cost optimization

| Strategy | Impact |
|---|---|
| Cache responses | 50-80% cost reduction |
| Use smaller models for simple tasks | 50-70% cost reduction |
| Batch requests | 20-30% cost reduction |
| Set response token limits | Prevents runaway costs |

## Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| 401 Unauthorized | Invalid API token | Verify token permissions (Read + Edit) |
| 404 Model not found | Wrong model name | Check model catalog URL |
| Timeout | Model cold start | Use on-demand, not serverless |
| Rate limited | Too many requests | Implement backoff, use caching |
| Empty response | Prompt too short | Add system prompt, increase max_tokens |

## Key References

- `` — REST API reference
- `[[playbooks/how-to-deploy-local-llm]]` — Local deployment alternatives
- Workers AI Models: https://developers.cloudflare.com/workers-ai/models/
- Workers AI AI SDK: https://developers.cloudflare.com/workers-ai/configuration/ai-sdk/
- Workers AI Docs: https://developers.cloudflare.com/workers-ai/
