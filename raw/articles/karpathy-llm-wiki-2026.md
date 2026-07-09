---
source_url: https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ac46de1ad27f92b28ac95459c782c07f6b8c964a/llm-wiki.md
ingested: 2026-07-04
sha256: c6327850ebcdcb8a6004e397b28e8b3c938586c2c137c5850eec004e367e149e
---

[Skip to content](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#start-of-content)

[](https://gist.github.com/)

 Search Gists  Search Gists

[All gists](https://gist.github.com/discover)[Back to GitHub](https://github.com/)[Sign in](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f)[Sign up](https://gist.github.com/join?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f&source=header-gist)

[](https://gist.github.com/)

[Sign in](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f)[Sign up](https://gist.github.com/join?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f&source=header-gist)

You signed in with another tab or window. [Reload](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) to refresh your session.You signed out in another tab or window. [Reload](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) to refresh your session.You switched accounts on another tab or window. [Reload](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) to refresh your session.Dismiss alert

{{ message }}

Instantly share code, notes, and snippets.

[![Image 1: @karpathy](https://avatars.githubusercontent.com/u/241138?s=64&v=4)](https://gist.github.com/karpathy)

# [karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**

 Created April 4, 2026 16:25

Show Gist options

*   [Download ZIP](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/archive/ac46de1ad27f92b28ac95459c782c07f6b8c964a.zip)

*   [Star 5,000+(5,000+)](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f)You must be signed in to star a gist
*   [Fork 5,000+(5,000+)](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f)You must be signed in to fork a gist

*   
 Embed # Select an option    

    *    Embed Embed this gist in your website.
    *    Share Copy sharable link for this gist.
    *    Clone via HTTPS Clone using the web URL.

## No results found

[Learn more about clone URLs](https://docs.github.com/articles/which-remote-url-should-i-use)

 Clone this repository at &lt;script src=&quot;https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f.js&quot;&gt;&lt;/script&gt;  

*   Save karpathy/442a6bf555914893e9891c11519de94f to your computer and use it in GitHub Desktop.

[Code](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)[Revisions 1](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/revisions)[Stars 5,000+](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/stargazers)[Forks 5,000+](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/forks)

 Embed 

# Select an option

*    Embed Embed this gist in your website.
*    Share Copy sharable link for this gist.
*    Clone via HTTPS Clone using the web URL.

## No results found

[Learn more about clone URLs](https://docs.github.com/articles/which-remote-url-should-i-use)

 Clone this repository at &lt;script src=&quot;https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f.js&quot;&gt;&lt;/script&gt;  

Save karpathy/442a6bf555914893e9891c11519de94f to your computer and use it in GitHub Desktop.

[Download ZIP](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/archive/ac46de1ad27f92b28ac95459c782c07f6b8c964a.zip)

 llm-wiki 

[Raw](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ac46de1ad27f92b28ac95459c782c07f6b8c964a/llm-wiki.md)

[**llm-wiki.md**](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#file-llm-wiki-md)

# LLM Wiki

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#llm-wiki)

A pattern for building personal knowledge bases using LLMs.

This is an idea file, it is designed to be copy pasted to your own LLM Agent (e.g. OpenAI Codex, Claude Code, OpenCode / Pi, or etc.). Its goal is to communicate the high level idea, but your agent will build out the specifics in collaboration with you.

## The core idea

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#the-core-idea)

Most people's experience with LLMs and documents looks like RAG: you upload a collection of files, the LLM retrieves relevant chunks at query time, and generates an answer. This works, but the LLM is rediscovering knowledge from scratch on every question. There's no accumulation. Ask a subtle question that requires synthesizing five documents, and the LLM has to find and piece together the relevant fragments every time. Nothing is built up. NotebookLM, ChatGPT file uploads, and most RAG systems work this way.

The idea here is different. Instead of just retrieving from raw documents at query time, the LLM **incrementally builds and maintains a persistent wiki** — a structured, interlinked collection of markdown files that sits between you and the raw sources. When you add a new source, the LLM doesn't just index it for later retrieval. It reads it, extracts the key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting where new data contradicts old claims, strengthening or challenging the evolving synthesis. The knowledge is compiled once and then _kept current_, not re-derived on every query.

This is the key difference: **the wiki is a persistent, compounding artifact.** The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read. The wiki keeps getting richer with every source you add and every question you ask.

You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions. The LLM does all the grunt work — the summarizing, cross-referencing, filing, and bookkeeping that makes a knowledge base actually useful over time. In practice, I have the LLM agent open on one side and Obsidian open on the other. The LLM makes edits based on our conversation, and I browse the results in real time — following links, checking the graph view, reading the updated pages. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

This can apply to a lot of different contexts. A few examples:

*   **Personal**: tracking your own goals, health, psychology, self-improvement — filing journal entries, articles, podcast notes, and building up a structured picture of yourself over time.
*   **Research**: going deep on a topic over weeks or months — reading papers, articles, reports, and incrementally building a comprehensive wiki with an evolving thesis.
*   **Reading a book**: filing each chapter as you go, building out pages for characters, themes, plot threads, and how they connect. By the end you have a rich companion wiki. Think of fan wikis like [Tolkien Gateway](https://tolkiengateway.net/wiki/Main_Page) — thousands of interlinked pages covering characters, places, events, languages, built by a community of volunteers over years. You could build something like that personally as you read, with the LLM doing all the cross-referencing and maintenance.
*   **Business/team**: an internal wiki maintained by LLMs, fed by Slack threads, meeting transcripts, project documents, customer calls. Possibly with humans in the loop reviewing updates. The wiki stays current because the LLM does the maintenance that no one on the team wants to do.
*   **Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives** — anything where you're accumulating knowledge over time and want it organized rather than scattered.

## Architecture

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#architecture)

There are three layers:

**Raw sources** — your curated collection of source documents. Articles, papers, images, data files. These are immutable — the LLM reads from them but never modifies them. This is your source of truth.

**The wiki** — a directory of LLM-generated markdown files. Summaries, entity pages, concept pages, comparisons, an overview, a synthesis. The LLM owns this layer entirely. It creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent. You read it; the LLM writes it.

**The schema** — a document (e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex) that tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow when ingesting sources, answering questions, or maintaining the wiki. This is the key configuration file — it's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot. You and the LLM co-evolve this over time as you figure out what works for your domain.

## Operations

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#operations)

**Ingest.** You drop a new source into the raw collection and tell the LLM to process it. An example flow: the LLM reads the source, discusses key takeaways with you, writes a summary page in the wiki, updates the index, updates relevant entity and concept pages across the wiki, and appends an entry to the log. A single source might touch 10-15 wiki pages. Personally I prefer to ingest sources one at a time and stay involved — I read the summaries, check the updates, and guide the LLM on what to emphasize. But you could also batch-ingest many sources at once with less supervision. It's up to you to develop the workflow that fits your style and document it in the schema for future sessions.

**Query.** You ask questions against the wiki. The LLM searches for relevant pages, reads them, and synthesizes an answer with citations. Answers can take different forms depending on the question — a markdown page, a comparison table, a slide deck (Marp), a chart (matplotlib), a canvas. The important insight: **good answers can be filed back into the wiki as new pages.** A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history. This way your explorations compound in the knowledge base just like ingested sources do.

**Lint.** Periodically, ask the LLM to health-check the wiki. Look for: contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links, important concepts mentioned but lacking their own page, missing cross-references, data gaps that could be filled with a web search. The LLM is good at suggesting new questions to investigate and new sources to look for. This keeps the wiki healthy as it grows.

## Indexing and logging

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#indexing-and-logging)

Two special files help the LLM (and you) navigate the wiki as it grows. They serve different purposes:

**index.md** is content-oriented. It's a catalog of everything in the wiki — each page listed with a link, a one-line summary, and optionally metadata like date or source count. Organized by category (entities, concepts, sources, etc.). The LLM updates it on every ingest. When answering a query, the LLM reads the index first to find relevant pages, then drills into them. This works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure.

**log.md** is chronological. It's an append-only record of what happened and when — ingests, queries, lint passes. A useful tip: if each entry starts with a consistent prefix (e.g. `## [2026-04-02] ingest | Article Title`), the log becomes parseable with simple unix tools — `grep "^## \[" log.md | tail -5` gives you the last 5 entries. The log gives you a timeline of the wiki's evolution and helps the LLM understand what's been done recently.

## Optional: CLI tools

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#optional-cli-tools)

At some point you may want to build small tools that help the LLM operate on the wiki more efficiently. A search engine over the wiki pages is the most obvious one — at small scale the index file is enough, but as the wiki grows you want proper search. [qmd](https://github.com/tobi/qmd) is a good option: it's a local search engine for markdown files with hybrid BM25/vector search and LLM re-ranking, all on-device. It has both a CLI (so the LLM can shell out to it) and an MCP server (so the LLM can use it as a native tool). You could also build something simpler yourself — the LLM can help you vibe-code a naive search script as the need arises.

## Tips and tricks

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#tips-and-tricks)

*   **Obsidian Web Clipper** is a browser extension that converts web articles to markdown. Very useful for quickly getting sources into your raw collection.
*   **Download images locally.** In Obsidian Settings → Files and links, set "Attachment folder path" to a fixed directory (e.g. `raw/assets/`). Then in Settings → Hotkeys, search for "Download" to find "Download attachments for current file" and bind it to a hotkey (e.g. Ctrl+Shift+D). After clipping an article, hit the hotkey and all images get downloaded to local disk. This is optional but useful — it lets the LLM view and reference images directly instead of relying on URLs that may break. Note that LLMs can't natively read markdown with inline images in one pass — the workaround is to have the LLM read the text first, then view some or all of the referenced images separately to gain additional context. It's a bit clunky but works well enough.
*   **Obsidian's graph view** is the best way to see the shape of your wiki — what's connected to what, which pages are hubs, which are orphans.
*   **Marp** is a markdown-based slide deck format. Obsidian has a plugin for it. Useful for generating presentations directly from wiki content.
*   **Dataview** is an Obsidian plugin that runs queries over page frontmatter. If your LLM adds YAML frontmatter to wiki pages (tags, dates, source counts), Dataview can generate dynamic tables and lists.
*   The wiki is just a git repo of markdown files. You get version history, branching, and collaboration for free.

## Why this works

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#why-this-works)

The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else.

The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that.

## Note

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#note)

This document is intentionally abstract. It describes the idea, not a specific implementation. The exact directory structure, the schema conventions, the page formats, the tooling — all of that will depend on your domain, your preferences, and your LLM of choice. Everything mentioned above is optional and modular — pick what's useful, ignore what isn't. For example: your sources might be text-only, so you don't need image handling at all. Your wiki might be small enough that the index file is all you need, no search engine required. You might not care about slide decks and just want markdown pages. You might want a completely different set of output formats. The right way to use this is to share it with your LLM agent and work together to instantiate a version that fits your needs. The document's only job is to communicate the pattern. Your LLM can figure out the rest.

[](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

Load earlier comments...

[![Image 2: @MarcoPorcellato](https://avatars.githubusercontent.com/u/220745401?s=80&v=4)](https://gist.github.com/MarcoPorcellato)

### **[MarcoPorcellato](https://gist.github.com/MarcoPorcellato)** commented [Jun 22, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6211059#gistcomment-6211059)

 Copy link  Copy Markdown 

### What about "Reinforcement Learning (RLHF) for PKMs"?

Right now, our graphs are "flat". Every block or bullet has a static weight of 1.0. Search relies on text matching, but human memory doesn't work like that. Some ideas are core pillars, others are just fleeting notes.

I’m releasing an architectural RFC to the open-source community: Applying Reinforcement Learning from Human Feedback (RLHF) to Personal Knowledge Graphs.

Instead of forcing users to manually rate notes (flashcards/spaced repetition), the database should passively learn from our UI interactions:

*   **Rewards (+ weight):** When you transclude a block ((uuid)) or zoom into it (Focus Mode), the database learns this is a foundational node.

*   **Penalties (- weight):** When a block is ignored in search results (scroll-past) or hasn't been touched in months (temporal decay), its semantic weight drops.

I wrote a detailed Gist outlining the architecture, the pseudo-code for the dynamic weights, and how it alters global search ranking. I've released the concept under the Apache 2.0 license so anyone can experiment with it or build plugins.

You can take a look and contribute here:

[https://gist.github.com/MarcoPorcellato/9e5226408c56048b16957771f9056e28](https://gist.github.com/MarcoPorcellato/9e5226408c56048b16957771f9056e28)

I'm building this into the core of Matryca Brain (next step from Matryca Plumber), but I’d love to hear the thoughts of the Logseq community. Is anyone else exploring dynamic node weighting based on implicit UI feedback? Let's discuss the architecture!

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 3: @SkyHomage](https://avatars.githubusercontent.com/u/4524888?s=80&v=4)](https://gist.github.com/SkyHomage)

### **[SkyHomage](https://gist.github.com/SkyHomage)** commented [Jun 22, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6211145#gistcomment-6211145)

 Copy link  Copy Markdown 

The comment section is unreadable...

I'm just wondering about his idea of sources. For articles/research this makes sense, just add the paper. But one of the example use cases was reading a book. So how would one add a source for a book? Its either copyright protected or will be in the order of MBs per book.

Adding books do seem a bit redundant since surely the LLM was already trained on every printed book at the time. In my experience however getting a LLM to work with me on a certain chapter is a bit difficult without pulling in future chapters (since it knows about it) or random ideas from other wikis/reddit. It would be nice to truly work with the LLM and discover knowledge in tandem when it comes to books.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 4: @perdakovich](https://avatars.githubusercontent.com/u/89806596?s=80&v=4)](https://gist.github.com/perdakovich)

### **[perdakovich](https://gist.github.com/perdakovich)** commented [Jun 22, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6211319#gistcomment-6211319)

 Copy link  Copy Markdown 

lol

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 5: @alexesDev](https://avatars.githubusercontent.com/u/1255344?s=80&v=4)](https://gist.github.com/alexesDev)

### **[alexesDev](https://gist.github.com/alexesDev)** commented [Jun 22, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6211350#gistcomment-6211350)

 Copy link  Copy Markdown 

[@geetansharora](https://github.com/geetansharora) you can keep the MCP setup you've got. What changes is that the wiki itself becomes the shared thing, not a RAG index sitting next to it.

That's basically what we built trip2g for. You sync the markdown vault from Obsidian, and it's served two ways: as a normal site and over MCP. So everyone's agent (Claude, Cursor, Codex, whatever) points at one endpoint. It runs search to find the section, then expand to walk the note's TOC one level at a time, so it only pulls the part it needs instead of the whole note. You can also stitch a few separate bases together with federation behind the same endpoint.

Easiest way to poke at it: the trip2g docs are themselves one of these wikis over MCP, no auth. Add [https://trip2g.com/_system/mcp](https://trip2g.com/_system/mcp) as an MCP server and let your agent search/expand around them.

Self-host writeup: [https://trip2g.com/en/user/agent_memory](https://trip2g.com/en/user/agent_memory)

 the general idea: [https://trip2g.com/en/user/llm_wiki](https://trip2g.com/en/user/llm_wiki)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 6: @equationalapplications](https://avatars.githubusercontent.com/u/65428263?s=80&v=4)](https://gist.github.com/equationalapplications)

### **[equationalapplications](https://gist.github.com/equationalapplications)** commented [Jun 22, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6211662#gistcomment-6211662)•

 edited 

Loading

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

 Copy link  Copy Markdown 

Letting an AI silently maintain a markdown-based knowledge base is incredibly powerful. But as your graph grows, taxonomy drift becomes a nightmare. An unconstrained LLM will generate company, Company, Business, and Organization across different runs, making it impossible to build reliable app UI dashboards on top of your data.

 To solve this, we are brainstorming a Per-Entity Seeded Ontology architecture for our @equationalapplications/core-llm-wiki memory engine.

 As shown in the infographic, this pattern gives developers 3 configurable modes to control how the LLM extracts knowledge graph edges:

 1️⃣ Strict (Seeded): Supply a starter pack of allowed edges (e.g., ['client', 'employed_by']) using a package like @equationalapplications/wiki-ontologies. The LLM is forced to stick to this schema, guaranteeing predictable data structures for hard-coded dashboards. 2️⃣ Emergent (Autogenerated): Give the LLM total freedom to invent relationships dynamically, tracking its own inventions in an ontology_manifest fact. Perfect for flexible "Second Brain" apps where the domain is unknown. 3️⃣ Off (Disabled): Stick to standard, isolated semantic fact extraction when relationship traversal is overkill.

 This perfectly balances rigid app data requirements with the "minimally opinionated" philosophy of the Open Knowledge Format (OKF) v0.1

I would love to get feedback from other developers building agentic memory! Which mode would you use for your app?

 🔗 Links & Resources:

 Core LLM Wiki Engine: [https://github.com/equationalapplications/expo-llm-wiki/tree/main/packages/core](https://github.com/equationalapplications/expo-llm-wiki/tree/main/packages/core)

 Open Knowledge Format (OKF) Spec: [https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)

 Karpathy's LLM Wiki Gist: [https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

 Equational Applications LLC: [https://equationalapplications.com/](https://equationalapplications.com/)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 7: @equationalapplications](https://avatars.githubusercontent.com/u/65428263?s=80&v=4)](https://gist.github.com/equationalapplications)

### **[equationalapplications](https://gist.github.com/equationalapplications)** commented [Jun 22, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6211945#gistcomment-6211945)

 Copy link  Copy Markdown 

An introduction to the Equational Applications LLC collection of LLM Wiki inspired, open-source Typescript packages.

[https://youtu.be/ay9PJ3WXxoo?si=ukTWR9oUADUFJrSD](https://youtu.be/ay9PJ3WXxoo?si=ukTWR9oUADUFJrSD)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 8: @equationalapplications](https://avatars.githubusercontent.com/u/65428263?s=80&v=4)](https://gist.github.com/equationalapplications)

### **[equationalapplications](https://gist.github.com/equationalapplications)** commented [Jun 22, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6212065#gistcomment-6212065)

 Copy link  Copy Markdown 

We are excited to announce that Open Knowledge Format (OKF) Import is officially coming to the @equationalapplications/core-llm-wiki memory engine!

 OKF v0.1 is a vendor-neutral standard that represents knowledge as a directory of markdown files with YAML frontmatter, where the file path serves as the concept's identity. While our ecosystem already supports exporting episodic memory into compliant OKF bundles, this upcoming update introduces the parseOkfBundle adapter to seamlessly read foreign or modified OKF bundles back into your local SQLite database.

 But we aren't just importing flat facts—this update lays the foundational database schema for our upcoming Per-Entity Seeded Ontology roadmap. We are introducing:

 A new okf_type column to preserve the exact YAML frontmatter type strings.

 A lightweight llm_wiki_edges table to extract and persist typed graph relationships directly from markdown cross-links.

 Zero-dependency parsing primitives in our new @equationalapplications/core-okf package.

 Soon, your AI agents will be able to ingest, maintain, and share rich, interconnected knowledge graphs with complete data portability!

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 9: @alexesDev](https://avatars.githubusercontent.com/u/1255344?s=80&v=4)](https://gist.github.com/alexesDev)

### **[alexesDev](https://gist.github.com/alexesDev)** commented [Jun 23, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6212688#gistcomment-6212688)

 Copy link  Copy Markdown 

fwiw the read path is what decides this in practice, and it stays cheap without a typed graph. trip2g serves the vault over MCP as agent memory: search, expand the TOC one level, then read only the section you need. Links are plain `[[wikilinks]]` resolved lazily, so a dangling link is just a "write this later" marker and I've never had to seed an ontology to keep drift under control.

The reason I lean on focused retrieval is token cost. Reading the one section that holds the answer runs ~15× cheaper than dumping the whole note at the median, and ~23× cheaper than grep-and-read. Numbers here: [token economy bench](https://trip2g.com/en/user/token_economy_bench).

And it's actually running, not a thought experiment. On session end each agent writes its own status into a shared vault, and teammates query a federation hub to see who's working on what: [agent status](https://trip2g.com/en/user/agent_status). Same memory model, just federated. Setup overview: [agent memory](https://trip2g.com/en/user/agent_memory).

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 10: @timetxt](https://avatars.githubusercontent.com/u/28048038?s=80&v=4)](https://gist.github.com/timetxt)

### **[timetxt](https://gist.github.com/timetxt)** commented [Jun 23, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6212833#gistcomment-6212833)

 Copy link  Copy Markdown 

This has held up really well for me — keeping the raw sources read-only and letting the model own the markdown made a real difference.

The thing that kept biting me: an agent would re-try a dead end an earlier session had already ruled out. It happened so many times that I ended up building a small open-source Python tool for it (Qiju) — it keeps a plain record of the decisions and the approaches I'd dropped, so the next run doesn't repeat them. Honestly it's been working great.

Have you hit the agent-repeats-a-dead-end problem too? Curious whether you'd keep that history inside the wiki, or in a separate log next to it.

For anyone interested to try: [QiJu](https://github.com/jasonshrepo/qiju)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 11: @sunshineg](https://avatars.githubusercontent.com/u/1147886?s=80&v=4)](https://gist.github.com/sunshineg)

### **[sunshineg](https://gist.github.com/sunshineg)** commented [Jun 23, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6213112#gistcomment-6213112)

 Copy link  Copy Markdown 

Spot on. The shift from raw RAG to compounding LLM-curated synthesis is the next paradigm shift.

We just open-sourced [https://projectbrain.md/](https://projectbrain.md/) — an open, Git-native standard for this exact pattern, purpose-built for builders and agents.

To prove it works in the wild, we spent the last month dogfooding it to build [https://mindmux.ai](https://mindmux.ai/), a local-first desktop workbench for AI-native dev teams.

It structures project context as Markdown + YAML frontmatter + cross-referenced [[wiki-links]] inside a /brain directory. Downstream agents (Cursor, Claude Code, Codex) ingest curated context; humans review Brain Diffs alongside code PRs.

Your write-up is a brilliant crystallization. Seeing this convergence after a month of building on it is incredibly validating.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 12: @MihirModi1421](https://avatars.githubusercontent.com/u/56664987?s=80&v=4)](https://gist.github.com/MihirModi1421)

### **[MihirModi1421](https://gist.github.com/MihirModi1421)** commented [Jun 23, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6213210#gistcomment-6213210)

 Copy link  Copy Markdown 

I tried creating a codebase wiki based on the existing idea (llm-wiki). You can copy this gist into a CLAUDE.md file, then ask Claude to initialize the wiki and see how it behaves:

[https://gist.github.com/MihirModi1421/94b5c2299bf743c346590e322d709046](https://gist.github.com/MihirModi1421/94b5c2299bf743c346590e322d709046)

Any advice or suggestions would be appreciated.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 13: @Sistema2D](https://avatars.githubusercontent.com/u/23338013?s=80&v=4)](https://gist.github.com/Sistema2D)

### **[Sistema2D](https://gist.github.com/Sistema2D)** commented [Jun 23, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6213280#gistcomment-6213280)

 Copy link  Copy Markdown 

# New Release! [![Image 14: Release](https://camo.githubusercontent.com/f76a825e5c0ad989502124384206af2ab378e28dfece39fac4ddecc56c2f404a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f52656c656173652d76302e31322e302d3666343263313f7374796c653d666c61742d737175617265)](https://github.com/Sistema2D/FrameCode-VibeWork/releases)

[![Image 15: image](https://private-user-images.githubusercontent.com/23338013/611855097-108b6bf0-ffd1-4cde-82a3-7a1c70302b86.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODI4OTQ4NDEsIm5iZiI6MTc4Mjg5NDU0MSwicGF0aCI6Ii8yMzMzODAxMy82MTE4NTUwOTctMTA4YjZiZjAtZmZkMS00Y2RlLTgyYTMtN2ExYzcwMzAyYjg2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA3MDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNzAxVDA4MjkwMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWUzNDhmZTdmNDVjYzU4ZTg2NmU3ZDg3MjY3OTM4Njc3MGVjMWJiOTZiMmVmZWViOTRiZTZlYmNlMTdmMTk2YTImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.7rWdXmcyBbyq1eNoS5l-8DsxT4LHlhKPtqN46j3QeNM)](https://private-user-images.githubusercontent.com/23338013/611855097-108b6bf0-ffd1-4cde-82a3-7a1c70302b86.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODI4OTQ4NDEsIm5iZiI6MTc4Mjg5NDU0MSwicGF0aCI6Ii8yMzMzODAxMy82MTE4NTUwOTctMTA4YjZiZjAtZmZkMS00Y2RlLTgyYTMtN2ExYzcwMzAyYjg2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA3MDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNzAxVDA4MjkwMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWUzNDhmZTdmNDVjYzU4ZTg2NmU3ZDg3MjY3OTM4Njc3MGVjMWJiOTZiMmVmZWViOTRiZTZlYmNlMTdmMTk2YTImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.7rWdXmcyBbyq1eNoS5l-8DsxT4LHlhKPtqN46j3QeNM)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 16: @alfadur7](https://avatars.githubusercontent.com/u/6949852?s=80&v=4)](https://gist.github.com/alfadur7)

### **[alfadur7](https://gist.github.com/alfadur7)** commented [Jun 26, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6218432#gistcomment-6218432)

 Copy link  Copy Markdown 

Built an implementation of this pattern and have been running it daily for a while — sharing in case the extensions are useful to anyone here.

**LLM Wiki Newsroom** — [https://github.com/alfadur7/llm-wiki-newsroom](https://github.com/alfadur7/llm-wiki-newsroom) (local-first, no API key; the Python tools run entirely on your machine)

Kept your three-layer split (raw → wiki → schema) and the ingest/query/lint loop intact, but leaned hard into the "bookkeeping is the hard part" idea by structuring the agent as a **newsroom staff** instead of one do-everything assistant:

*   **Authoring and review are different instances.** A "reporter" drafts source/entity stubs, a "columnist" writes the deep cross-source analysis, and a separate "desk" re-reads and critiques it — which curbs the self-grading bias you get when one model checks its own output.
*   **Two-sided publish gate:** deterministic linting (links, citations, structure) _and_ a qualitative review against an editorial rubric (journalism/consulting/encyclopedic forms) both have to pass.
*   **Self-improving guidelines:** when the same review failure recurs, it drafts a fix to the _authoring rules themselves_ and adopts it only after a blind, regression-gated A/B (inspired by the recent Self-Harness and Microsoft SkillOpt work).
*   **Cascading updates** (your "1 doc changes 10–15 pages"), **3-layer contradiction tracking**, a **Leiden-clustered knowledge graph** with an interactive browser, and **Memex-style associative trails** for serendipitous discovery.

Works with Claude Code (full feature set) and basic mode with Codex/Gemini. Feedback very welcome — the schema-as-config idea has held up remarkably well in practice.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 17: @eula01](https://avatars.githubusercontent.com/u/52753311?s=80&v=4)](https://gist.github.com/eula01)

### **[eula01](https://gist.github.com/eula01)** commented [Jun 26, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6218929#gistcomment-6218929)

 Copy link  Copy Markdown 

hilarious how hundreds of people with ai psychosis have pointed their slopcannons at this gist - "implement this gist, make no mistakes"

[![Image 18: image](https://private-user-images.githubusercontent.com/52753311/613777767-a5d255a0-f924-46ad-ab23-26430946b5b1.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODI4OTQ4NDEsIm5iZiI6MTc4Mjg5NDU0MSwicGF0aCI6Ii81Mjc1MzMxMS82MTM3Nzc3NjctYTVkMjU1YTAtZjkyNC00NmFkLWFiMjMtMjY0MzA5NDZiNWIxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA3MDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNzAxVDA4MjkwMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWY3Y2ZhNjhmYWNiOTkyZTNjZGY3NjgzNTQxM2E5OTE2YTVlZjdlMjA4NTY1MmRlYzQ0ODlmMzVhMjE2Mjk1YjMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.wPWAurXaasdTpqoEriUYYEP4JXEmYI3MxixT835kakI)](https://private-user-images.githubusercontent.com/52753311/613777767-a5d255a0-f924-46ad-ab23-26430946b5b1.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODI4OTQ4NDEsIm5iZiI6MTc4Mjg5NDU0MSwicGF0aCI6Ii81Mjc1MzMxMS82MTM3Nzc3NjctYTVkMjU1YTAtZjkyNC00NmFkLWFiMjMtMjY0MzA5NDZiNWIxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA3MDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNzAxVDA4MjkwMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWY3Y2ZhNjhmYWNiOTkyZTNjZGY3NjgzNTQxM2E5OTE2YTVlZjdlMjA4NTY1MmRlYzQ0ODlmMzVhMjE2Mjk1YjMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.wPWAurXaasdTpqoEriUYYEP4JXEmYI3MxixT835kakI)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 19: @Mirorrn](https://avatars.githubusercontent.com/u/16208459?s=80&v=4)](https://gist.github.com/Mirorrn)

### **[Mirorrn](https://gist.github.com/Mirorrn)** commented [Jun 27, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6220062#gistcomment-6220062)

 Copy link  Copy Markdown 

> Hello Andrei and the community. I’m building a Markdown/Obsidian-style knowledge wiki for teaching a health informatics course, using Codex to help ingest sources, maintain links, and later query the wiki for presentations and curriculum design.
> 
> 
> I ran into a token-efficiency problem that may be interesting: the token burn was not mainly from reasoning or output, but from repeated context loading. Codex kept re-reading files like AGENTS.md, wiki/index.md, manifests, handoffs, raw sources, and tool scripts across short sessions. Even small source-ingest tasks became expensive.
> 
> 
> I’ve started moving toward a split workflow: deterministic Python scripts handle source intake, route indexes, validation, and compact handoffs; Codex is reserved for higher-value graph curation, synthesis, and judgment. I’m also using compact routing files instead of asking the model to scan the whole wiki.
> 
> 
> I would be grateful for any advice on the right architecture for this kind of “wiki as working memory” setup. Specifically, how would you structure retrieval, summaries, graph edges, and agent instructions so Codex can reason over a rich knowledge base without repeatedly consuming the entire context?
> 
> 
> Even a few pointers or design principles would be very helpful.

Hi,

 did you try to use subagents for search operations, so that the main agent context window is reserved for orchestration and answering.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 20: @LuminairPrime](https://avatars.githubusercontent.com/u/91862358?s=80&v=4)](https://gist.github.com/LuminairPrime)

### **[LuminairPrime](https://gist.github.com/LuminairPrime)** commented [Jun 28, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6221192#gistcomment-6221192)

 Copy link  Copy Markdown 

Glad to see this new version of llms.txt formalized as Open Knowledge Format. Thank you for your leadership

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 21: @A13x3i](https://avatars.githubusercontent.com/u/14916898?s=80&v=4)](https://gist.github.com/A13x3i)

### **[A13x3i](https://gist.github.com/A13x3i)** commented [Jun 29, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6221568#gistcomment-6221568)

 Copy link  Copy Markdown 

Gezz the AI Slop is storing in this one's comment section... I just wanted to point out that NotebookLM is kinda intended to be this way as well, you get sources extract whatever you need make it a source, disable sources you don't need anymore

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 22: @devmubs](https://avatars.githubusercontent.com/u/77266846?s=80&v=4)](https://gist.github.com/devmubs)

### **[devmubs](https://gist.github.com/devmubs)** commented [Jun 29, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6222191#gistcomment-6222191)

 Copy link  Copy Markdown 

Really interesting approach. I think one challenge that will show up as these systems grow is keeping synthesized knowledge reliable over time. Retrieval is only part of the problem—making sure older summaries stay accurate without constantly rebuilding everything seems much harder.

Keeping the raw sources immutable feels like the right foundation. I also wonder if adding a simple confidence or verification status to wiki pages could help highlight which pages are well-supported and which ones may need another review after new sources are added.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 23: @kibotu](https://avatars.githubusercontent.com/u/3336447?s=80&v=4)](https://gist.github.com/kibotu)

### **[kibotu](https://gist.github.com/kibotu)** commented [Jun 29, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6222233#gistcomment-6222233)

 Copy link  Copy Markdown 

it's also important to reduce the pages to the absolute min. simplification is important in any larger code/knowledge base otherwise you end up with way too much overhead.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 24: @theluk](https://avatars.githubusercontent.com/u/580946?s=80&v=4)](https://gist.github.com/theluk)

### **[theluk](https://gist.github.com/theluk)** commented [Jun 29, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6222277#gistcomment-6222277)

 Copy link  Copy Markdown 

[@A13x3i](https://github.com/A13x3i) yeah crazy isnt it? That's AEO

antways, regarding NotebookLM, I mean sure, but there is more to it. Especially the Linter is I think one real addition. I am btw using this Linter Concept almost everywhere now. So Thanks [@karpathy](https://github.com/karpathy) for that concept idea.

LLMs do make mistakes no matter what you do, that's why you need an agent that iterates over the stuff and verifies that things are working. Here is an example agent I have running on one wiki

```
# Wiki Linter — System Prompt

You are a wiki health checker. When invoked, you run a structured lint pass
over a markdown wiki stored in a knowledge base and produce a report.

You have access to two tools primarily:
- `queryFrontmatter` — filter/sort pages by YAML frontmatter fields
- `readFile` — read individual page content

---

## Lint Checks (run in order)

### 1. Schema Integrity
Use `queryFrontmatter` to find pages missing any of the required fields:
`type`, `title`, `description`, `tags`, `timestamp`, `sources`

For any page missing a field:
- Flag it by name and note which field(s) are absent
- Repair metadata with `setFrontmatter` where the correct value is unambiguous
- Flag for user review where the value is uncertain

### 2. Staleness
Sort all pages by `timestamp` ascending. Surface the 5–10 oldest.
For each, check whether newer pages contradict or supersede their content.
Flag any that do. Propose specific updates but do not apply them unilaterally.

### 3. Coverage Gaps
Scan all `summary`, `entity`, and `concept` pages for mentions of things
(tools, people, projects, concepts) that lack their own dedicated page.
List each gap. Do not create pages — flag them for the ingestor or user.

### 4. Overview Drift
Compare the `timestamp` on `overview.md` against the newest
`summary`, `entity`, and `concept` pages.
If `overview.md` lags by more than one ingest cycle, flag it as drifted.

### 5. Orphan Check
For each page, check whether any other page links to it.
Flag any page with zero inbound links as an orphan.
Suggest which existing pages should link to it.

### 6. Duplicate Detection
Look for multiple files with the same or near-identical names or titles.
List all suspected duplicates with their file IDs.
Do NOT delete anything. Flag for user approval.

---

## Output Format

Produce a markdown report with this structure:

# Lint Report — {DATE}

## Summary
One-line overall health status: 🟢 Green / 🟡 Yellow / 🔴 Red

## 1. Schema Integrity
## 2. Staleness
## 3. Coverage Gaps
## 4. Overview Drift
## 5. Orphan Check
## 6. Duplicate Detection

## Overall Health
Table or bullet list of all checks with pass/fail/warn status.

## Next Steps
Numbered list of actions — note which require user approval before execution.

---

## Hard Rules

- **Never delete files unilaterally.** Flag duplicates and orphans; act only on explicit approval.
- **Never create or edit wiki content pages.** That is the ingestor's job.
- **Do** repair frontmatter metadata (`setFrontmatter`) when the correct value is certain.
- Log the lint pass to `log.md` when done.
```

And I dont do it just for the Knowledge Wiki, I do it for SEO (interlinking checks, quality checks) and more. It's really one helpful agent that can be used in general on data structures that are somehow related.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 25: @william-Johnason](https://avatars.githubusercontent.com/u/4006820?s=80&v=4)](https://gist.github.com/william-Johnason)

### **[william-Johnason](https://gist.github.com/william-Johnason)** commented [Jun 29, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6222281#gistcomment-6222281)

 Copy link  Copy Markdown 

> it's also important to reduce the pages to the absolute min. simplification is important in any larger code/knowledge base otherwise you end up with way too much overhead.

[@kibotu](https://github.com/kibotu) agreed, simplification is the harder problem. One thing that helps is building compression into the ingestion step itself. In Synthadoc, raw sources get compiled into concept pages, so 100 ingested documents might synthesize down to a dozen wiki pages, topics that appear across multiple sources merge rather than accumulate. The active knowledge surface stays small by design, not by discipline.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 26: @william-Johnason](https://avatars.githubusercontent.com/u/4006820?s=80&v=4)](https://gist.github.com/william-Johnason)

### **[william-Johnason](https://gist.github.com/william-Johnason)** commented [Jun 29, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6222282#gistcomment-6222282)

 Copy link  Copy Markdown 

> Really interesting approach. I think one challenge that will show up as these systems grow is keeping synthesized knowledge reliable over time. Retrieval is only part of the problem—making sure older summaries stay accurate without constantly rebuilding everything seems much harder.
> 
> 
> Keeping the raw sources immutable feels like the right foundation. I also wonder if adding a simple confidence or verification status to wiki pages could help highlight which pages are well-supported and which ones may need another review after new sources are added.

[@devmubs](https://github.com/devmubs) the confidence/verification state idea is exactly what we should land on too - each page carries a lifecycle status, so when new sources arrive, the system knows which pages to re-examine rather than rebuilding everything.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 27: @dumanyu666-byte](https://avatars.githubusercontent.com/u/289686706?s=80&v=4)](https://gist.github.com/dumanyu666-byte)

### **[dumanyu666-byte](https://gist.github.com/dumanyu666-byte)** commented [Jun 29, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6222498#gistcomment-6222498)

 Copy link  Copy Markdown 

good thanks

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 28: @Onevirtual](https://avatars.githubusercontent.com/u/11797977?s=80&v=4)](https://gist.github.com/Onevirtual)

### **[Onevirtual](https://gist.github.com/Onevirtual)** commented [Jun 29, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6222811#gistcomment-6222811)

 Copy link  Copy Markdown 

Thanks for the pattern Mr. Karpathy: I've noted added few things that were worth my time.

For the metadata, I am using breadcrumds which enables me to replicate somehow standard .owl relationships from inference engines. It's useful when you are trying to associate pages, oppose pages, label pages or whatever relationships you want to bring in the classification.

For the document structure:

 I use a notepad blended source for the LLM to write in, those are where the main questions from the dialogical interaction takes places.

Then I have a personal notes which I use in order to put my thoughts into, it enables me to enhance my critical thinking and derives from what the llm is generating from my own curated sources. Whenever I use a webfetch tool I also make clear from which source the generation took from.

The skill for this has this purpose : - One is a prompt crawler in which I ask questions within the personal note component in the page area.Using ^[put prompt here], when I am populating the wiki with my thoughts, then I add a footnote next to it ^[put prompt here][^1], that way, I can reread my own thoughts and contrast it with the LLM Response, which is interesting for me because I am always able to tell what was generated versus what I was writing.

And Last I have a go further section which is another prompt then analyses the "idées-forces" between my notes and the llm-generated ones, it gives me direction. It was especially insightful during my readings and commenting of Mumford's Art and Techniques conferences and a Quine's Article.

What I found the most interesting in the pattern is two things :

*   Focusing on the graph and the correct linking of the ideas, I don't trust the LLMs enough to build alone a categorization that is worth and I like to reason on the semantics of clusterization with it.
*   Secondly, it gives me a very good feeling of abstraction ascending. When I am creating an instance, I generally tweak the concept a few times before it becomes a category. The moment where a mono page concept becomes a category of its own is very satisfying and aligning with how inference for human works; derivating rules and organisation through repeated exposures to observations.

Thank you for that, I have rediscovered a lot of books I had on my bookshelves, blending from Homere Odysseus to Philosophy of mind through agentic patterns.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 29: @alfadur7](https://avatars.githubusercontent.com/u/6949852?s=80&v=4)](https://gist.github.com/alfadur7)

### **[alfadur7](https://gist.github.com/alfadur7)** commented [Jun 30, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6223045#gistcomment-6223045)•

 edited 

Loading

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

 Copy link  Copy Markdown 

[@Motya-cobol](https://github.com/Motya-cobol) your split — deterministic scripts for intake/validation, model only for judgment — is exactly the right instinct; it's the same division I landed on.

The piece that helped most on top of it: **never let the agent read page bodies just to find what's relevant.**

 Give it a small CLI to check the "map" first:

*   **shortest path** between two pages
*   a page's **neighbors and cluster**
*   a local **BM25 / vector search**

Let it pick **~10 pages** from that, and _only then_ read those in full. The index stays a one-line-per-entry directory (a link + a one-line summary per page), with sources split into per-cluster sub-catalogs — so it's a _routing file_, not something to scan.

On **[@Mirorrn](https://github.com/Mirorrn)**'s subagent point: +1 to keeping the narrowing off the orchestrator's context. I do it with a deterministic CLI call rather than a separate agent, but same goal — and since it's just Python, it drives fine from Codex too.

Search/traversal CLI if useful → [https://github.com/alfadur7/llm-wiki-newsroom/blob/main/tools/query.py](https://github.com/alfadur7/llm-wiki-newsroom/blob/main/tools/query.py)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 30: @distorx](https://avatars.githubusercontent.com/u/1065150?s=80&v=4)](https://gist.github.com/distorx)

### **[distorx](https://gist.github.com/distorx)** commented [Jun 30, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6223068#gistcomment-6223068)

 Copy link  Copy Markdown 

This maps almost 1:1 to a system we have been running in production for ~6 months to manage infrastructure/ops knowledge. A few notes from actually living with the pattern at ~4000+ interlinked concepts:

*   **The schema file is everything.** Our `CLAUDE.md` is exactly the "disciplined maintainer vs. generic chatbot" config you describe — it encodes the ingest/query/lint workflows + naming conventions, and it co-evolved into the single most important file in the repo.
*   **index.md at scale:** the flat index works great to a few hundred pages. Past that we added hybrid search (SQLite FTS5 + on-device embeddings, reciprocal-rank-fused) rather than standing up embedding-RAG infra — same spirit as qmd. We expose it as both a CLI (agent shells out) and an MCP server (native tool). ~1ms keyword, ~350ms hybrid.
*   **New page vs. edit ([@alinawab](https://github.com/alinawab)):** heuristic that works for us — _new page_ when it is a distinct entity/concept you would link to from elsewhere; _edit in place_ when it is an attribute/update of an existing one. The agent gets this right ~90% of the time once the schema enumerates the page types.
*   **Team sharing ([@geetansharora](https://github.com/geetansharora)):** the wiki is just a private git repo, auto-synced. Teammates browse in Obsidian or hit the same MCP server. Git history doubles as the `log.md` audit trail for free.
*   **Biggest failure mode ([@alinawab](https://github.com/alinawab)):** drift — the agent under-updating cross-references on ingest, so pages silently go stale. The lint pass is _not_ optional; we run it on a timer (orphan detection + contradiction flagging + stale-claim checks) and that is what keeps the graph healthy.

The "compounding artifact" framing is exactly right — after a few thousand concepts the wiki answers questions the raw sources never could, because the synthesis already happened. Thanks for writing it up so cleanly.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 31: @despindola](https://avatars.githubusercontent.com/u/17557563?s=80&v=4)](https://gist.github.com/despindola)

### **[despindola](https://gist.github.com/despindola)** commented [Jun 30, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6224229#gistcomment-6224229)

 Copy link  Copy Markdown 

This pattern is the most important thing I have adopted this year, and thank you for sharing it as an idea rather than a repo.

One observation from outside the dev world: almost everyone I know who would benefit most from this stops at the terminal. Writers, advisors, researchers, founders. The bookkeeping that LLMs handle so well is exactly the part they want, but the setup asks for skills or interests they do not have.

I have been building a hosted version of this same idea, with no terminal or config, aimed squarely at that group. Happy to compare notes with anyone else thinking about the non-technical on-ramp. It feels like it is where most of the latent demand actually is.

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 32: @maurizio-persi](https://avatars.githubusercontent.com/u/291724620?s=80&v=4)](https://gist.github.com/maurizio-persi)

### **[maurizio-persi](https://gist.github.com/maurizio-persi)** commented [Jun 30, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6224363#gistcomment-6224363)

 Copy link  Copy Markdown 

First of all, thanks to **[@karpathy](https://github.com/karpathy)** for introducing and describing the **LLM-Wiki** paradigm: a simple yet brilliant idea that, in my opinion, will revolutionize corporate document management (replacing heavy, complex knowledge bases), help students avoid superficial LLM usage, and serve as a great ally for methodical learning.

I have built a **Personal LLM-Wiki** prioritizing two fundamental aspects:

1.   **Privacy**: All components run completely **offline**.
2.   **Efficiency**: I focused on creating an executable suitable for **modest hardware** (with or without a GPU), making it accessible despite current market prices for graphics cards.

The core concept is straightforward: perform non-LLM-specific operations deterministically using standard Python libraries, which consume significantly fewer resources than a giant language model. It feels inefficient to waste LLM tokens on repetitive tasks that only require classic computational power.

While my initial prototype worked, the model's responses were often too generic or limited to brief definitions. To achieve the exhaustive, structured lessons I envisioned, I integrated a few key components to enrich the context:

### Key Components

*   **Graphify**: Maps relationships between Markdown files, SQL schemas, scripts, and PDFs. It improves navigation based on structural relationships rather than just keywords, creating a navigable "map" directly accessible to the AI or via **Obsidian**. This drastically reduced dependency on compute while improving coherence.
*   **ChromaDB**: A lightweight vector database used as the pillar for semantic search and document retrieval, executing operations efficiently on the CPU.
*   **NetworkX**: Manages a dual data structure in memory with a **lazy cache**: an _Undirected Graph ($G$)_ for generic relationships and a _Directed Graph ($DiG$)_ focused exclusively on formative dependencies. This helps identify correlations and cite diverse sources covering the requested topic.
*   **SQLite**: An embedded, serverless relational database dedicated to managing the system's transactional state and audit logs.

### Operational Flow

```
[Phase 1 (Optional): Pre-processing (Whisper)] ──> 
──> [Phase 2: Synthesis (Qwen3VL)]
──> [Phase 3: Graph Building (Graphify)]
──> [Phase 4: Indexing (ChromaDB)]
──> [Phase 5: Context Assembly]
──> [Phase 6: Inference (Qwen3.5 9B)]
```

_Advanced features included: Semantic Query Cache, Cross-Encoder Re-Ranker, and Reciprocal Rank Fusion (RRF) for HyDE._

### Additional Features

*   **Localization & UI**: Built a lightweight Flask web page with "on-the-fly" language switching managed via simple `.lng` files.
*   **Secure Telegram Bot**: Accessible without exposing ports or reverse proxies (restricted to authorized Telegram IDs). It includes an interactive poll after each response, allowing the user to save the text, export it as a Marp Markdown presentation, or generate an audio podcast.
*   **Quiz Mode**: Generates multiple-choice questions based on the wiki content with customizable difficulty, evaluating errors and explaining _why_ a specific answer was wrong.

### A Critique of the Paradigm: No New Wiki Pages Without Raw Sources

The only critique I have regarding the baseline LLM-Wiki paradigm concerns **creating new wiki pages derived from LLM responses**.

I don't find it useful to generate additional pages beyond those processed during the **Ingest** phase. Reprocessing existing concepts in different forms consumes resources and slows down the system (more pages to scan per query) without introducing genuinely new information. Since the LLM should not invent anything (avoiding hallucinations), it doesn't enrich the source base.

In my implementation, the only generated pages allowed are the Markdown files exported for **Presentations** (Marp syntax)-treated strictly as "output documents" for the user, rather than being re-fed into the pipeline as wiki sources.

* * *

I haven't published the repository on GitHub yet, as I am still refining the integration to make it as user-friendly as possible. I hope this architecture can serve as inspiration for anyone looking to customize or optimize their local LLM-Wiki setup!

* * *

### Below is an example of an answer to the question “Explain me what Kubernetes is.”

[![Image 33: Personal LLM-WIKI](https://private-user-images.githubusercontent.com/291724620/615299575-1e0a9e98-b758-4292-91c0-34213afbade8.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODI4OTQ4NDEsIm5iZiI6MTc4Mjg5NDU0MSwicGF0aCI6Ii8yOTE3MjQ2MjAvNjE1Mjk5NTc1LTFlMGE5ZTk4LWI3NTgtNDI5Mi05MWMwLTM0MjEzYWZiYWRlOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNzAxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDcwMVQwODI5MDFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05ZTMwODYwOTkyNTBhY2FmMjMyMDlhOTdjZGFlZWM4ZDQ0NmQxMWUzZjhmN2IzOGMyYmNmODZhOGE4MDlmOWM0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.j0tXDMy2XG8XF_OJX8tq56teSElBXNUcdx4NIyZptmw)](https://private-user-images.githubusercontent.com/291724620/615299575-1e0a9e98-b758-4292-91c0-34213afbade8.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODI4OTQ4NDEsIm5iZiI6MTc4Mjg5NDU0MSwicGF0aCI6Ii8yOTE3MjQ2MjAvNjE1Mjk5NTc1LTFlMGE5ZTk4LWI3NTgtNDI5Mi05MWMwLTM0MjEzYWZiYWRlOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNzAxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDcwMVQwODI5MDFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05ZTMwODYwOTkyNTBhY2FmMjMyMDlhOTdjZGFlZWM4ZDQ0NmQxMWUzZjhmN2IzOGMyYmNmODZhOGE4MDlmOWM0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.j0tXDMy2XG8XF_OJX8tq56teSElBXNUcdx4NIyZptmw)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 34: @RightL](https://avatars.githubusercontent.com/u/9251452?s=80&v=4)](https://gist.github.com/RightL)

### **[RightL](https://gist.github.com/RightL)** commented [Jul 1, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6224846#gistcomment-6224846)

 Copy link  Copy Markdown 

Love this. I think the key idea is not “chatbot over files,” but “LLM-maintained structure that compounds.” We’re building RightMemory from a very similar motivation, but focused on memory for teams of coding agents.

The core of RightMemory is ordinary Git-backed Markdown, with a small tree + graph schema. The tree gives agents readable local context through headings. The graph gives durable relationships through ids and typed edges, so facts, decisions, preferences, TODOs, and related project knowledge can point across sections and files. The memory stays inspectable as Markdown, but it is structured enough for agents to navigate precisely.

A major design point is that this is not RAG. RightMemory is not primarily a vector database or a chunk retrieval layer. The durable artifact is the maintained Markdown memory itself. Retrieval reads the current structured memory; updates change the memory; consolidation improves it over time. The system is closer to an agent-maintained knowledge graph/wiki than to “embed documents and search at query time.”

Another important part is teams of agents. RightMemory is designed so memory can survive across sessions, devices, agent clients, and collaborating agent teams. Different memory roots can share selected context through controlled shared views, so one project/person/team can expose only the relevant memory to another without dumping the whole private memory store.

We also lean heavily into the CLI direction you mention. The `rightmemory` CLI is the main command surface, so any command-capable coding agent can use the same memory substrate. Codex, Claude Code, and other CLI-style agents can call the same retrieve/update/status/shared-view commands instead of memory being locked into one vendor UI.

One more design choice I care a lot about: the roles are all pure agents with explicit authority boundaries. There is a retriever role for read-oriented memory lookup, an updater role for durable memory edits, a dreamer role for consolidation/restructuring, and a reviewer role for extracting useful memory from prior sessions. The main coding agent does not casually mutate memory while doing unrelated work; memory operations are delegated to the right role.

So the overlap with your LLM Wiki pattern is strong: persistent Markdown, LLM-maintained structure, compounding context, and tooling around the artifact. RightMemory’s specific bet is that coding-agent memory should be tree + graph Markdown, operated through CLI-accessible agent roles, built for teams of agents, and not reduced to a RAG pipeline.

Project: [https://github.com/RightL/RightMemory](https://github.com/RightL/RightMemory)

 Example memory file: [https://github.com/RightL/RightMemory/blob/main/MEMORY.example.md](https://github.com/RightL/RightMemory/blob/main/MEMORY.example.md)

 Schema: [https://github.com/RightL/RightMemory/blob/main/skills/rightmemory-schema.md](https://github.com/RightL/RightMemory/blob/main/skills/rightmemory-schema.md)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[![Image 35: @ojuschugh1](https://avatars.githubusercontent.com/u/79078267?s=80&v=4)](https://gist.github.com/ojuschugh1)

### **[ojuschugh1](https://gist.github.com/ojuschugh1)** commented [Jul 1, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6224960#gistcomment-6224960)

 Copy link  Copy Markdown 

  ███████╗ ██████╗ ███████╗
  ██╔════╝██╔═══██╗╚══███╔╝
  ███████╗██║   ██║  ███╔╝
  ╚════██║██║▄▄ ██║ ███╔╝
  ███████║╚██████╔╝███████╗
  ╚══════╝ ╚══▀▀═╝ ╚══════╝
  
**Compress LLM context to save tokens and reduce costs**

**Real session stats:** 3,003 compressions · **178,442 tokens saved** · 24.7% avg reduction · up to **92%** with dedup

[![Image 36: Featured](https://camo.githubusercontent.com/9f424b754c999087f980222e8f2d783d8a847ade1fc1eb0a60eb6e09e1ab3347/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f253233315f46656174757265642d4e65787447656e5f546563685f496e73696465722d6666363630303f7374796c653d666f722d7468652d6261646765266c6f676f3d6e6577737061706572266c6f676f436f6c6f723d7768697465)](https://thenextgentechinsider.com/pulse/sqz-tool-cuts-llm-token-use-by-92-for-file-heavy-ai-tasks)

[![Image 37: Crates.io](https://camo.githubusercontent.com/5992ef7d1ecd6fc3dbf18deaf91eb8583cc39920ff9bc2e1f5076f9ac99aa66c/68747470733a2f2f696d672e736869656c64732e696f2f6372617465732f762f73717a2d636c693f6c6f676f3d72757374266c6f676f436f6c6f723d7768697465266c6162656c3d6372617465732e696f26636f6c6f723d653635323263)](https://crates.io/crates/sqz-cli)[![Image 38: npm](https://camo.githubusercontent.com/cf6b7ae8cc98c0e20e798bd17ed662aad60a4f76da6b4602466f74b539973fb2/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f73717a2d636c693f6c6f676f3d6e706d266c6f676f436f6c6f723d7768697465266c6162656c3d6e706d26636f6c6f723d636233383337)](https://www.npmjs.com/package/sqz-cli)[![Image 39: PyPI](https://camo.githubusercontent.com/d18c9d3ca7a79bd64676431c7c9cb9b912023a30b0e0d1939aa20525ea72d3ea/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f73717a3f6c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465266c6162656c3d5079504926636f6c6f723d333737356139)](https://pypi.org/project/sqz/)[![Image 40: VS Code](https://camo.githubusercontent.com/b235ee4a2e4e94bba32f008f838cb45788954f51c4a005dc7ce02584d9c17708/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5653253230436f64652d4d61726b6574706c6163652d3030376163633f6c6f676f3d76697375616c2d73747564696f2d636f6465266c6f676f436f6c6f723d7768697465)](https://marketplace.visualstudio.com/items?itemName=ojuschugh1.sqz)[![Image 41: Firefox](https://camo.githubusercontent.com/246171336432b050f4315b52b256f07b3186b9c655bcb2996e3184c5be80cba0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f46697265666f782d4164642d2d6f6e2d6666373133393f6c6f676f3d66697265666f782d62726f77736572266c6f676f436f6c6f723d7768697465)](https://addons.mozilla.org/en-US/firefox/addon/sqz-context-compression/)[![Image 42: JetBrains](https://camo.githubusercontent.com/ac286c235c41b1a24767e226462f86a633b3eace5f4f2a045fe9be268b3b67d6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a6574427261696e732d506c7567696e2d3030303030303f6c6f676f3d6a6574627261696e73266c6f676f436f6c6f723d7768697465)](https://plugins.jetbrains.com/plugin/31240-sqz--context-intelligence/)[![Image 43: Discord](https://camo.githubusercontent.com/0d826cd7a0ab371a4d9cf81809cd58868592eff15400669a872084e333d7e28c/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f313439333235313032393037353233353037363f6c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465266c6162656c3d446973636f726426636f6c6f723d353836354632)](https://discord.gg/j8EEyH5dSB)[![Image 44: Homebrew](https://camo.githubusercontent.com/bbe7d020ee9dcb0590a6a321f169a8aad13ad5a467b98fdbeba51d4294172a8c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f486f6d65627265772d7461702d4642423034303f6c6f676f3d686f6d6562726577266c6f676f436f6c6f723d7768697465)](https://github.com/ojuschugh1/homebrew-sqz)

[Install](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#install) · [How It Works](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#how-it-works) · [Supported Tools](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#supported-tools) · [Changelog](https://gist.github.com/karpathy/CHANGELOG.md) · [Discord](https://discord.gg/j8EEyH5dSB)

* * *

sqz compresses command output before it reaches your LLM. Single Rust binary, zero config.

The real win is dedup: when the same file gets read 5 times in a session, sqz sends it once and returns a 13-token reference for every repeat.

```
Without sqz:                    With sqz:

File read #1:  2,000 tokens     File read #1:  ~800 tokens (compressed)
File read #2:  2,000 tokens     File read #2:  ~13 tokens  (dedup ref)
File read #3:  2,000 tokens     File read #3:  ~13 tokens  (dedup ref)
───────────────────────         ───────────────────────
Total:         6,000 tokens     Total:         ~826 tokens (86% saved)
```

## Token Savings

> **24.7%** average reduction across 3,003 real compressions ·
> 
> **92%** saved on repeated file reads ·
> 
> **86%** on shell/git output ·
> 
> **13-token** refs for cached content

One developer's week, measured from actual `sqz gain` output:

```
$ sqz gain
sqz token savings (last 7 days)
──────────────────────────────────────────────────
  04-13 │                              │   2,329 saved
  04-14 │                              │       0 saved
  04-15 │███                           │  12,954 saved
  04-16 │██                            │   9,223 saved
  04-17 │████                          │  14,752 saved
  04-18 │██████████████████████████████│ 105,569 saved
  04-19 │████████                      │  30,882 saved
  04-20 │█                             │   4,334 saved
──────────────────────────────────────────────────
  Total: 3,003 compressions, 178,442 tokens saved (24.7% avg reduction)
```

### Per-command compression

Single-command compression (measured via `cargo test -p sqz-engine benchmarks`):

| Content | Before | After | Saved |
| --- | ---: | ---: | ---: |
| Repeated log lines | 148 | 62 | **58%** |
| Large JSON array | 259 | 142 | **45%** |
| JSON API response | 64 | 53 | **17%** |
| Git diff | 61 | 54 | **12%** |
| Prose/docs | 124 | 121 | **2%** |
| Stack trace (safe mode) | 82 | 82 | **0%** |

### Session-level with dedup

Where the real savings live — the cache sends each file once, repeats cost 13 tokens:

| Scenario | Without sqz | With sqz | Saved |
| --- | ---: | ---: | ---: |
| Same file read 5× | 10,000 | 826 | **92%** |
| Same JSON response 3× | 192 | 79 | **59%** |
| Test-fix-test cycle (3 runs) | 15,000 | 5,186 | **65%** |

Single-command compression ranges from 2–58% depending on content. Repeated reads drop to 13 tokens each. Your mileage will vary with how repetitive your tool calls are — agentic sessions with many file re-reads see the biggest wins.

## Install

**Prebuilt binaries** (no compiler required — works on every platform):

undefinedshell
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/ojuschugh1/sqz/main/install.sh | sh

# Windows (PowerShell)
irm https://raw.githubusercontent.com/ojuschugh1/sqz/main/install.ps1 | iex

# Any platform via npm
npm install -g sqz-cli

# macOS / Linux via Homebrew
brew tap ojuschugh1/sqz
brew install sqz
undefined

**Build from source via Cargo:**

undefinedshell
cargo install sqz-cli sqz-mcp
undefined

`sqz-cli` provides the `sqz` binary; `sqz-mcp` provides the MCP server. `sqz-engine` is a library dependency — it compiles automatically and does not need to be installed separately.

**Build from source** (`cargo install sqz-cli`) works too, but needs a C toolchain:

*   Linux: `build-essential` (apt) or equivalent
*   macOS: Xcode Command Line Tools (`xcode-select --install`)
*   **Windows: Visual Studio Build Tools with the "Desktop development with C++" workload.** Without these, `cargo install` fails with `linker link.exe not found`. If you don't already have them, use the PowerShell or npm install above instead.

Then initialize:

undefinedshell
sqz init --global     # hooks apply to every project on this machine
# or
sqz init              # hooks apply to just this project (.claude/settings.local.json)
undefined

`--global` writes to `~/.claude/settings.json` (the user scope per the

[Anthropic scope table](https://docs.claude.com/en/docs/claude-code/settings)),

 so the sqz hook fires in every Claude Code session on this machine. This is

 the common case on first install. Your existing `permissions`, `env`,

`statusLine`, and unrelated hooks in `~/.claude/settings.json` are

 preserved — sqz merges its entries rather than overwriting.

Plain `sqz init` (project scope) is useful when you want sqz active only

 inside one repo.

**Only using one agent?** Pass `--only` (or `--skip`) to limit which

 configs are written:

undefinedshell
sqz init --only opencode              # just OpenCode, nothing else
sqz init --only opencode,codex        # OpenCode and Codex
sqz init --skip cursor,windsurf       # everything except Cursor and Windsurf
undefined

Accepted names: `claude`, `cursor`, `windsurf`, `cline`, `gemini`,

`kiro`, `opencode`, `codex`. Aliases (`claude-code`, `gemini-cli`, `roo`,

`kiro-cli`) also work. `--only` and `--skip` can't be combined.

### Manual installation (preserve comments in your config)

`sqz init` round-trips your config file through a JSON parser to merge

 the sqz entry, which drops any comments in your `opencode.jsonc` (and

 the analogous JSON-with-comments files other tools accept). If you've

 commented your config carefully and want to keep them, install by hand

 instead.

**OpenCode** — two steps:

1.   Drop the plugin file in place. `sqz` prints the generated TS to

 stdout so you don't have to hand-write the path-escaping logic:

undefinedshell
mkdir -p ~/.config/opencode/plugins
sqz print-opencode-plugin > ~/.config/opencode/plugins/sqz.ts
undefined

2.   Add the MCP entry to your existing `opencode.jsonc` yourself.

 Append this block inside the top-level `mcp` object (create the

`mcp` object if it doesn't exist):

undefinedjson
"sqz": {
  "type": "local",
  "command": ["sqz-mcp", "--transport", "stdio"],
  "enabled": true
}
undefined

Comments in the rest of your file stay put. OpenCode auto-discovers

 the plugin file; no `plugin` array entry needed (adding one causes

 double-loading, see issue #10).

**Other tools** — Claude Code, Cursor, Windsurf, Cline, Gemini CLI,

 and Codex use plain JSON configs without comment support, so the

 automated path is non-destructive there. Use `sqz init --only <tool>`

 for those.

That's it. Shell hooks installed, AI tool hooks configured.

## How It Works

[![Image 45: sqz system architecture](https://gist.github.com/karpathy/assets/sqz-architecture.png)](https://gist.github.com/karpathy/assets/sqz-architecture.png)

sqz installs a PreToolUse hook that intercepts bash commands before your AI tool runs them. The output gets compressed transparently — the AI tool never knows.

```
Claude → git status → [sqz hook rewrites] → compressed output (85% smaller)
```

What gets compressed:

*   **Shell output** — 40+ per-command formatters (git, cargo, npm/pnpm/yarn, pytest, ruff, go test, docker, kubectl, aws, terraform, gradle, gh, grep/rg, tree, curl, and more)
*   **JSON** — strips nulls, compact encoding, TOON format
*   **Logs** — collapses repeated lines
*   **Test output** — shows failures only (state-machine parsers for Rust, Go, Python, JS, JVM)

What doesn't get compressed:

*   Stack traces, error messages, secrets — routed to safe mode (0% compression)
*   Your prompts and the AI's responses — controlled by the AI tool, not sqz

## Supported Tools

| Tool | Integration | Setup |
| --- | --- | --- |
| Claude Code | PreToolUse hook (transparent) | `sqz init` |
| Cursor | PreToolUse hook (transparent) | `sqz init` |
| Windsurf | PreToolUse hook (transparent) | `sqz init` |
| Cline | PreToolUse hook (transparent) | `sqz init` |
| Gemini CLI | BeforeTool hook (transparent) | `sqz init` |
| Kiro | PreToolUse hook (transparent) | `sqz init` |
| OpenCode | TypeScript plugin (transparent) | `sqz init` |
| VS Code | [Extension](https://marketplace.visualstudio.com/items?itemName=ojuschugh1.sqz) | Install from Marketplace |
| JetBrains | [Plugin](https://plugins.jetbrains.com/plugin/31240-sqz--context-intelligence/) | Install from Marketplace |
| Chrome | Browser extension | ChatGPT, Claude.ai, Gemini, Grok, Perplexity |
| [Firefox](https://addons.mozilla.org/en-US/firefox/addon/sqz-context-compression/) | Browser extension | Same sites |

## CLI

undefinedshell
sqz init --global             # Install hooks for every project on this machine
sqz init                      # Install hooks for just this project
sqz init --only kiro          # Only configure Kiro (skip the rest)
sqz init --only opencode      # Only configure OpenCode (skip the rest)
sqz init --skip cursor        # Configure every agent except Cursor
sqz compress <text>           # Compress (or pipe from stdin)
sqz compress --no-cache       # Compress without dedup (always full output)
sqz expand <ref>              # Recover original content from a §ref:HASH§ token
sqz compact                   # Evict stale context to free tokens
sqz reset                     # Clear dedup cache or compression stats
sqz gain                      # Show daily token savings (bar chart)
sqz gain --project .          # Per-project daily gains
sqz gain --days 30            # Last 30 days
sqz stats                     # Cumulative compression report
sqz stats --breakdown         # Per-command token usage breakdown
sqz stats --project .         # Stats for current project only
sqz stats --project list      # List all tracked projects
sqz discover                  # Find missed savings
sqz resume                    # Re-inject session context after compaction
sqz vizit                     # Live terminal dashboard (like htop for AI agents)
sqz hook claude               # Process a PreToolUse hook (Claude Code)
sqz hook kiro                 # Process a PreToolUse hook (Kiro)
sqz print-opencode-plugin     # Print OpenCode plugin TS for manual install
sqz proxy --port 8080         # API proxy (compresses full request payloads)
undefined

### Dedup Escape Hatch

When sqz sees the same content twice, it returns a compact `§ref:HASH§` token

 instead of the full text. Most models handle this fine, but some (e.g., GLM 5.1)

 can't parse the ref format and loop. Four ways to work around this:

undefinedshell
# 1. Recover original content from a ref
sqz expand a1b2c3d4              # prefix match
sqz expand '§ref:a1b2c3d4§'     # paste the whole token

# 2. Compress without dedup (per-invocation)
echo "..." | sqz compress --no-cache

# 3. Disable dedup globally (env var)
export SQZ_NO_DEDUP=1

# 4. MCP passthrough tool (returns input byte-exact, zero transforms)
# Available via tools/list when sqz-mcp is running
undefined

## Track Your Own Savings

Run `sqz gain` in your shell any time to see your own daily breakdown (see the

 Token Savings section above for what the output looks like), and `sqz stats`

 for the full cumulative report:

undefinedshell
$ sqz stats
  📊 sqz compression stats
  ──────────────────────────────────────────────────

  178,442  tokens saved
  ↓  24.7% average reduction

  Compressions           3,003
  Tokens in              721,840
  Tokens out             543,398
  Tokens saved           178,442
  Avg reduction          24.7%

  🗄️  Cache
  ──────────────────────────────────────────────────
  Entries                43
  Size                   39.1 KB
undefined

Add `--breakdown` to see exactly which commands consume the most tokens:

undefinedshell
$ sqz stats --breakdown

  🔍 Top Token Consumers
  ──────────────────────────────────────────────────────────────────────
  command               calls  tokens in        out    saved
  ──────────────────────────────────────────────────────────────────────
  dedup                   249      45541       3237      93%
  stdin                    51      30851      24289      21%
  auto                    132      18288       7740      58%
  echo                     17       1050        558      47%
  ls -la                    8        948        948       0%
  cargo build               7        170        145      15%
  git status                4         56          8      86%
  ──────────────────────────────────────────────────────────────────────
undefined

**Per-project filtering:**

undefinedshell
sqz stats --project .           # stats for current project only
sqz stats --project list        # list all tracked projects
sqz gain --project .            # daily gains for current project
sqz gain --days 30              # last 30 days instead of 7
sqz gain --days 30 --project .  # combine both
undefined

Stats are stored locally in SQLite under `~/.sqz/sessions.db` — nothing leaves your machine.

## How Compression Works

1.   **Per-command formatters** — 40+ commands across 9 ecosystems get purpose-built compression:

| Ecosystem | Commands |
| --- | --- |
| Git | status, log, diff, show, stash, remote, fetch, push, pull, commit |
| Rust | cargo build/test/clippy/check/nextest |
| JavaScript | npm/pnpm/yarn/bun install/test/audit/outdated, tsc, eslint, vitest |
| Python | pytest, ruff, mypy, pip |
| Go | go test (incl. `-json` stream), go build, go vet, golangci-lint |
| Cloud | aws, terraform plan/apply/init, gcloud |
| Containers | docker/podman ps/images/build, kubectl get/describe/logs/apply |
| JVM | gradle build/test, maven |
| System | grep/rg, tree, find/fd, ls, curl/wget |
| GitHub | gh pr/issue/run (JSON + table) |

Unknown commands fall through to the generic compression pipeline — no output is ever left uncompressed.

2.   **Structural summaries** — code files compressed to imports + function signatures + call graph (~70% reduction). The model sees the architecture, not implementation noise.

3.   **Dedup cache** — SHA-256 content hash, persistent across sessions. Second read = 13-token reference.

4.   **JSON pipeline** — strip nulls → project out debug fields → flatten → collapse arrays → TOON encoding (lossless compact format)

5.   **Safe mode** — stack traces, secrets, migrations detected by entropy analysis and routed through with 0% compression

For the full technical details, see [docs/](https://gist.github.com/karpathy/docs/).

## Configuration

undefinedtoml
# ~/.sqz/presets/default.toml
[preset]
name = "default"
version = "1.0"

[compression.condense]
enabled = true
max_repeated_lines = 3

[compression.strip_nulls]
enabled = true

[budget]
warning_threshold = 0.70
default_window_size = 200000
undefined

## Privacy

*   Zero telemetry — no data transmitted, no crash reports
*   Fully offline — works in air-gapped environments
*   All processing local

## Development

undefinedshell
git clone https://github.com/ojuschugh1/sqz.git
cd sqz
cargo test --workspace
cargo build --release
undefined

## License

[Elastic License 2.0](https://gist.github.com/karpathy/LICENSE) (ELv2) — use, fork, modify freely. Two restrictions: no competing hosted service, no removing license notices.

## Links

*   [White Paper: Pre-Injection Context Compression](https://gist.github.com/karpathy/docs/whitepaper.md)
*   [Benchmark: sqz vs rtk](https://gist.github.com/karpathy/docs/benchmark-vs-rtk.md)
*   [Discord](https://discord.gg/j8EEyH5dSB)
*   [Changelog](https://gist.github.com/karpathy/CHANGELOG.md)

## Star History

[![Image 46: Star History Chart](https://camo.githubusercontent.com/4d6637722d7c5d9f42a6b84d4d7743fe6b7c0fc0ec10301fed71a84efafeeba7/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d6f6a75736368756768312f73717a26747970653d44617465)](https://star-history.com/#ojuschugh1/sqz&Date)

Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

[Sign up for free](https://gist.github.com/join?source=comment-gist)**to join this conversation on GitHub**. Already have an account? [Sign in to comment](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f)

## Footer

[](https://github.com/) © 2026 GitHub,Inc. 

### Footer navigation

*   [Terms](https://docs.github.com/site-policy/github-terms/github-terms-of-service)
*   [Privacy](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)
*   [Security](https://github.com/security)
*   [Status](https://www.githubstatus.com/)
*   [Community](https://github.community/)
*   [Docs](https://docs.github.com/)
*   [Contact](https://support.github.com/?tags=dotcom-footer)
*    Manage cookies 
*    Do not share my personal information 

 You can’t perform that action at this time.
