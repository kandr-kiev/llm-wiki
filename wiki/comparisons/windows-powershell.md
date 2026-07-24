---
title: "Windows PowerShell"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - async
  - container
  - edge
  - gemini
  - gpt
  - news
  - rag
  - search
---

# Windows PowerShell

> **Source:** how-to-build-a-rag-chatbot-for-your-docs-with-nodejs-google-gemini-and-pgvector-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://www.freecodecamp.org/news/how-to-build-rag-chatbot-nodejs-gemini-pgvector/ ingested: 2026-07-17 sha256: 5457dbb5020e8007425e5d53f70a867394736d8d5c205066c5ee37e5fb519230 blog_so...
> **Sources:**
>   - how-to-build-a-rag-chatbot-for-your-docs-with-nodejs-google-gemini-and-pgvector-2026-07-17.md
> **Links:**
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[automating-ai-away-2026-07-07]]
- [[5-agent-skills-i-use-every-day]]
- [[workers-cache]]

## Key Findings

---
source_url: https://www.freecodecamp.org/news/how-to-build-rag-chatbot-nodejs-gemini-pgvector/
ingested: 2026-07-17
sha256: 5457dbb5020e8007425e5d53f70a867394736d8d5c205066c5ee37e5fb519230
blog_source: FreeCodeCamp Blog
---
How to Build a RAG Chatbot for Your Docs with Node.js, Google Gemini, and pgvector
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
[![freeCodeCamp.org](https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg)](https://www.freecodecamp.org/news/)
- 
English
- 
Español
- 
中文（简体字）
- 
Italiano
- 
Português
- 
Українська
- 
日本語
- 
한국어
Menu
- 
- Forum
- Curriculum
- 
Night Mode
Donate
July 15, 2026
/
#Node.js
# How to Build a RAG Chatbot for Your Docs with Node.js, Google Gemini, and pgvector
![Zia Ullah](https://cdn.hashnode.com/uploads/avatars/6a32d4e8d06aa63cd556c4b9/9666ebc0-e7de-4f75-bd06-852d27c30919.jpg)
[
Zia Ullah
](/news/author/ziaullahzia/)
![How to Build a RAG Chatbot for Your Docs with Node.js, Google Gemini, and pgvector](https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/9aa3d8d3-9c51-42a7-8e78-907802394ea1.png)
I was helping a team that had a 200-page API documentation PDF. Every new engineer spent their first two weeks Ctrl+F-ing through it, asking the same questions in Slack, getting redirected to the same paragraphs on page 47.
The doc was accurate. It was even well-written. But nobody could find anything in it fast enough for it to be useful.
That's the problem RAG, or Retrieval-Augmented Generation, solves.
The naïve approach is to stuff your entire PDF into a prompt and let the model figure it out. That breaks down fast: context windows overflow, costs spike on every request, and the model loses the thread somewhere in the wall of text.
RAG takes a different approach. Your documents get broken into small chunks upfront. Ask it a question and it digs out the 3 or 4 chunks that best match it — those are what the model actually sees. The model gets a tight, focused context. The answer comes from what your document actually says — not from whatever the LLM memorized during training.
In this tutorial, you'll build that from scratch. Upload any PDF — an API reference, an internal spec, a research paper — and ask questions about it in plain English. The system finds the relevant sections and answers from the document itself, not from general training data.
The stack: Node.js with Express, Google Gemini for embeddings, Groq for text generation, and pgvector running in Docker. Every piece of it is free — no credit card, no trial period.
The complete code is on GitHub at [nodejs-rag-chatbot](https://github.com/ziaongit/nodejs-rag-chatbot).
## Table of Contents
- [How RAG Works](#heading-how-rag-works)
- [What We're Building](#heading-what-were-building)
- [Prerequisites](#heading-prerequisites)
- [Project Setup](#heading-project-setup)
- [Set Up Postgres with pgvector Using Docker](#heading-set-up-postgres-with-pgvector-using-docker)
- [Connect to the Database](#heading-connect-to-the-d

## Summary

atabase)
- [Build the Ingestion Pipeline](#heading-build-the-ingestion-pipeline)
- [Build the Query Pipeline](#heading-build-the-query-pipeline)
- [Build the Chat API with Express](#heading-build-the-chat-api-with-express)
- [Test the Chatbot](#heading-test-the-chatbot)
- [Troubleshooting](#heading-troubleshooting)
- [How to Swap in OpenAI](#heading-how-to-swap-in-openai)
- [What to Build Next](#heading-what-to-build-next)
## How RAG Works
RAG has two phases, and the code maps directly to both.
**Ingestion phase** — runs once when you upload a document:
- Pull the raw text out of the PDF
- Break it into chunks of 400 to 600 characters each, with a bit of overlap so nothing important gets cut at a boundary
- Run each chunk through an embedding model, which turns it into a vector (a long list of numbers that captures what the text means)
- Store each chunk and its vector in Postgres
**Query phase** — runs every time someone asks a question:
- Embed the user's question using the same model
- Search the database for chunks whose vectors are closest to the question vector
- Take the top 5 matching chunks and assemble them into a context block
- Send `context + question` to the LLM and return its answer
The reason this works better than keyword search: the embedding model captures *meaning*, not just exact words. If your doc says "terminate the process" and the user asks "how do I stop it?", vector similarity finds that match. Regular string matching doesn't.
One thing that trips people up: you must use the same embedding model at query time as you did at ingestion. The model defines the geometric space those vectors live in. Switch models halfway through and the coordinates stop meaning the same thing — you'd be comparing apples to completely different apples.
## What We're Building
The architecture is intentionally minimal: two endpoints, with nothing you don't need:
- `POST /ingest`: accepts a PDF upload, chunks it, embeds each chunk, stores vectors in pgvector
- `POST /chat`: accepts a question, retrieves the most relevant chunks, returns an LLM-generated answer
The full tech stack:
- **Node.js + Express** — API layer
- **Google Gemini free API** — `gemini-embedding-001` for embeddings (3,072 dimensions per chunk)
- **Groq free API** — `llama-3.1-8b-instant` for text generation
- **PostgreSQL + pgvector** — vector storage and cosine similarity search, running in Docker
- **pdf-parse** — extracts raw text from PDF buffers
Gemini handles embeddings and Groq handles generation. Splitting them across two providers isn't arbitrary. Gemini's generation API has a quota limit of zero in certain regions (including Pakistan), while Groq works everywhere with no restrictions. Using Groq for generation means this tutorial runs the same way regardless of where you are.
## Prerequisites
Before you start:
- Node.js 20+ installed on your machine
- Docker Desktop running (this is how we'll run Postgres locally)
- A free Google Gemini API key (for embeddings)
- A fr

## Related Articles

- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[automating-ai-away-2026-07-07]]
- [[5-agent-skills-i-use-every-day]]
- [[workers-cache]]
