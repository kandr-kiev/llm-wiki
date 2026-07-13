---
title: "rollbacks for workflows"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - async
  - data
  - edge
  - image-generation
  - multi-agent
  - nlp
---
# rollbacks for workflows

> **Source:** how-we-built-saga-rollbacks-for-cloudflare-workflows-2026-07-07.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://blog.cloudflare.com/rollbacks-for-workflows/ ingested: 2026-07-07 sha256: 4a8158b2334bc26b0dd11924efecb9e7b3a18989d881eb535e2e06cea2efbb26 blog_source: Cloudflare Blog --- How...
> **Sources:**
>   - how-we-built-saga-rollbacks-for-cloudflare-workflows-2026-07-07.md
> **Links:**
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[automating-ai-away-2026-07-07]]
- [[away]]
- [[chemical-hygiene]]
- [[finding-the-best-sleep-tracker]]

## Key Findings

---
source_url: https://blog.cloudflare.com/rollbacks-for-workflows/
ingested: 2026-07-07
sha256: 4a8158b2334bc26b0dd11924efecb9e7b3a18989d881eb535e2e06cea2efbb26
blog_source: Cloudflare Blog
---
How we built saga rollbacks for Cloudflare Workflows- - - - - - - - - - - - - 
- - <astro-island uid="1TqJ3W" component-url="/_astro/GoogleAnalytics.Buaiy_s2.js" component-export="GoogleAnalytics" renderer-url="/_astro/client.CpQ9otmg.js" props="{"title":[0,"How we built saga rollbacks for Cloudflare Workflows"],"canonical":[0,"https://blog.cloudflare.com/rollbacks-for-workflows"],"info":[0,{"id":[0,"6BmERiKIIt4pIJoFmNy7Jn"],"title":[0,"How we built saga rollbacks for Cloudflare Workflows"],"slug":[0,"rollbacks-for-workflows"],"excerpt":[0,"Cloudflare Workflows, our durable execution engine for multi-step applications, now supports saga-style rollbacks, allowing developers to specify a compensating action for each step.do(). "],"featured":[0,false],"html":[0,"<p>Cloudflare Workflows allows you to build durable, multi-step applications with built-in retries and state persistence across long-running processes. When a <a href=\"https://developers.cloudflare.com/workflows/\" target=\"_blank\" rel=\"noopener noreferrer\"><u>Workflow</u></a> executes, each step can call external systems, retry failures, and persist state across restarts. But if one step fails, it may leave earlier work from completed steps in an inconsistent or partial state.</p><p>Today weâre shipping saga rollbacks for Workflows, allowing you to declare rollback logic within the step itself, in case of failure.</p><p>For example, consider a workflow for transferring funds between accounts at two different banks:</p><ol><li><p>Debit from account at Bank A</p></li><li><p>Credit to account at Bank B</p></li><li><p>Send email confirmation to both account owners</p></li></ol><p>What happens if Step 2, the credit to account at Bank B, fails? Once the debit succeeds at Bank A, the transaction is committed and the money has left its system. As the orchestrator of the transaction, you cannot simply âundoâ the operation in Bank A's system. Instead, the money must be credited back to the account at Bank A through a new operation that semantically reverses the first one.</p>\n <figure class=\"kg-card kg-image-card\">\n <Image src=\"https://cf-assets.www.cloudflare.com/zkvhlag99gkb/1j8xfDeKb3FCgE2Ktxf4fq/723e2b9e34189747d3c8eb65f906fb41/BLOG-3317_image6.png\" alt=\"BLOG-3317 image6\" class=\"kg-image\" width=\"1376\" height=\"1310\" loading=\"lazy\"/>\n </figure><p>\nThis pairing of an operation and its compensation logic is called the <a href=\"https://www.youtube.com/watch?v=xDuwrtwYHu8\" target=\"_blank\" rel=\"noopener noreferrer\"><u>saga pattern</u></a>.</p><p>Before today, developers had to implement their own compensation logic to track what succeeded, what failed, and what actions should be taken upon failure, outside of the stepsâ direct definitions. Now, you can define compensation

## Summary

 logic for each <code>step.do()</code> as an argument within the steps themselves, maintaining your workflowâs durability for the rollback as well.</p>\n <pre class=\"language-TypeScript\"><code class=\"language-TypeScript\">// track what completed so we know what to undo\nlet debitA;\nlet creditB;\ntry {\n debitA = await step.do("debit-bank-a", () => bankA.debit(from, amount));\n creditB = await step.do("credit-bank-b", () => bankB.credit(to, amount));\n await step.do("notify", () => notifyBoth(from, to, amount));\n} catch (error) {\n // unwind in reverse. each undo is its own durable step,\n // must be idempotent, and must keep going if one fails.\n if (creditB) {\n try {\n await step.do("reverse-credit-b", () => bankB.debit(to, amount, creditB.id));\n } catch (e) {\n await alertOnCall("reverse-credit-b failed", e);\n }\n }\n if (debitA) {\n try {\n await step.do("refund-debit-a", () => bankA.credit(from, amount, debitA.id));\n } catch (e) {\n await alertOnCall("refund-debit-a failed", e);\n }\n }\n throw error;\n}</pre></code>\n <p><i><sup>Without rollbacks</sup></i></p>\n <pre class=\"language-TypeScript\"><code class=\"language-TypeScript\">// each step ships with its own undo. add a step,\n// add its rollback right here. no growing catch\n// block, no manual ordering, no replay logic.\nawait step.do("debit-bank-a", () => bankA.debit(from, amount), {\n rollback: async ({ output }) => bankA.credit(from, amount, output.id),\n});\nawait step.do("credit-bank-b", () => bankB.credit(to, amount), {\n rollback: async ({ output }) => bankB.debit(to, amount, output.id),\n});\nawait step.do("notify", () => notifyBoth(from, to, amount));</pre></code>\n <p><i><sup>With rollbacks</sup></i></p>\n <div class=\"flex anchor relative\">\n <h2 id=\"try-it-out\">Try it out</h2>\n <a href=\"#try-it-out\" aria-hidden=\"true\" class=\"relative sm:absolute sm:-start-5\">\n <svg width=\"16\" height=\"16\" viewBox=\"0 0 24 24\"><path fill=\"currentcolor\" d=\"m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z\"></path></svg>\n </a>\n </div>\n <p>To use rollbacks, just pass an options object containing a <code>rollback</code> function as the last argument to <code>step.do()</code>.</p>\n <pre class=\"language-TypeScript\"><code class=\"language-TypeScript\">const debit = await step.do(\n "debit-account-a",\n async () => {\n return await bankA.debit({\n accountId: fromAccountId,\n amount,\n idempotencyKey: `${transferId}:debit-accou

## Related Articles

- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[automating-ai-away-2026-07-07]]
- [[away]]
- [[chemical-hygiene]]
- [[finding-the-best-sleep-tracker]]
