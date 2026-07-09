---
title: "REST API"
type: comparison
tags:
description: Comparison page for REST API

sources: []
links: []
description: Comparison page for REST API

links: []
confidence: medium
created: 2026-07-08
updated: 2026-07-08
---

# REST API

> **Source:** cloudflare-workers-ai-rest-api-2026.md
> **Type:** comparison
> **Created:** 2026-07-08

## Key Findings

---
source_url: https://developers.cloudflare.com/workers-ai/get-started/rest-api/
ingested: 2026-07-07
sha256: 1f2d4567148f359592a12cc4824253c886d69c9fac70b8bbec7accd3b89c6cbd
---
# REST API
This guide will instruct you through setting up and deploying your first Workers AI project. You will use the Workers AI REST API to experiment with a large language model (LLM).
## Prerequisites
Sign up for a [Cloudflare account ↗](https://dash.cloudflare.com/sign-up/workers-and-pages) if you have not already.
## 1. Get API token and Account ID
You need your API token and Account ID to use the REST API.
To get these values:
1. In the Cloudflare dashboard, go to the Workers AI page. 
[ Go to Workers AI ](https://dash.cloudflare.com/?to=/:account/ai/workers-ai)
2. Select Use REST API.
3. Get your API token:
1. Select Create a Workers AI API Token.
2. Review the prefilled information.
3. Select Create API Token.
4. Select Copy API Token.
5. Save that value for future use. This token will be visible [on your profile](https://developers.cloudflare.com/api/get-started/create-token/).
4. For Get Account ID, copy the value for Account ID. Save that value for future use.
Note
If you choose to [create an API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) instead of using the template, that token will need permissions for both Workers AI - Read and Workers AI - Edit.
## 2. Run a model via API
After creating your API token, authenticate and make requests to the API using your API token in the request.
You will use the [Execute AI model](https://developers.cloudflare.com/api/resources/ai/methods/run/) endpoint to run the [@cf/meta/llama-3.1-8b-instruct](https://developers.cloudflare.com/workers-ai/models/llama-3.1-8b-instruct/) model:
curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/meta/llama-3.1-8b-instruct \
-H 'Authorization: Bearer {API_TOKEN}' \
-d '{ "prompt": "Where did the phrase Hello World come from" }'
Replace the values for {ACCOUNT_ID} and {API_TOKEN}.
The API response will look like the following:
{
"result": {
"response": "Hello, World first appeared in 1974 at Bell Labs when Brian Kernighan included it in the C programming language example. It became widely used as a basic test program due to simplicity and clarity. It represents an inviting greeting from a program to the world."
},
"success": true,
"errors": [],
"messages": []
}
This example execution uses the @cf/meta/llama-3.1-8b-instruct model, but you can use any of the models in the [Workers AI models catalog](https://developers.cloudflare.com/workers-ai/models/). If using another model, you will need to replace {model} with your desired model name.
By completing this guide, you have created a Cloudflare account (if you did not have one already) and an API token that grants Workers AI read permissions to your account. You executed the [@cf/meta/llama-3.1-8b-instruct](https://developers.cloudflare.com/workers-ai/models/llama-3.1-8b-ins

## Summary

See Key Findings for full content.

## Related Articles

- [[how-to-use-cloudflare-workers-ai]]
- [[how-to-use-cloudflare-workers-ai]]
- [[applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07]]
- [[llm-deployment-qa]]
- [[the-illustrated-stable-diffusion-2026-07-07]]
