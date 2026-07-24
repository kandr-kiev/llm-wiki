---
title: "laravel quota usage budgets for calendar periods"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - application
  - async
  - data
  - image-generation
  - news
  - offline
  - use-case
  - vector-database
---

# laravel quota usage budgets for calendar periods

> **Source:** laravel-quota-usage-budgets-for-calendar-periods-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** # Laravel Quota: Usage Budgets for Calendar Periods Last updated on July 13th, 2026 by [ Paul Redmond ](/@paulredmond) ![Laravel Quota: Usage Budgets for Calendar Periods image](https://picperf.io/htt...
> **Sources:**
>   - laravel-quota-usage-budgets-for-calendar-periods-2026-07-17.md
> **Links:**
- [[enforce-per-action-waiting-periods-in-laravel-with-cooldown]]
- [[laravel-legacy-bridge-carry-authenticated-sessions-from-a-legacy-app-into-laravel]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[ai-music-video-arena-claude-vs-gpt-56]]

## Key Findings

# Laravel Quota: Usage Budgets for Calendar Periods
Last updated on
July 13th, 2026
by
[
Paul Redmond
](/@paulredmond)
![Laravel Quota: Usage Budgets for Calendar Periods image](https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/laravel-quota-featured.png)
Laravel Quota is a package for tracking and enforcing cumulative usage limits. For example, you could enforce limits like 50 PDF exports a month, 1,000 API queries a day, a pool of AI credits per billing cycle, and more.
It's aimed at a different problem than Laravel's `RateLimiter`: instead of throttling bursts of traffic in a sliding window, it counts consumption against a budget that resets on a calendar boundary, and it can persist that count in the database rather than only in the cache.
Here's what the package gives you:
- **Calendar-aligned periods** — define `perMinute()`, `perHour()`, `perDay()`, `perWeek()`, `perMonth()`, `perYear()`, or `period($start, $end)` for a custom window
- **A `HasQuotas` trait** that puts quotas on any Eloquent model
- **Route middleware** (`quota:exports,50,month`) that only consumes on a successful response
- **Cache or database backends**, switchable per call
- **Atomic consumption** - lock consumption around the work it meters
- **Enforce budgets** - throw an HTTP 429 when the budget is spent
- And more.
## #The Fluent API
A quota is a named counter scoped to an owner, with a limit and a period. Once you've described one, you can inspect it or spend against it:
```
use ZaberDev\Quota\Facades\Quota; $builder = Quota::for('api_queries', $user) ->limit(1000) ->perDay(); $builder->used();$builder->remaining();$builder->isExceeded();$builder->hasCapacity(10); $info = $builder->consume(5);
```
The `consume()` method returns an immutable `QuotaInfo` DTO. If you'd rather fail hard than branch, the `enforce()` method throws an HTTP 429 when the budget is gone:
```
Quota::for('api_queries', $user)->limit(1000)->perDay()->enforce();
```
For work where a double-spend actually matters, `block()` wraps the callback in a lock so two concurrent requests can't both slip through the capacity check:
```
Quota::for('pdf_generation', $user) ->limit(50) ->perMonth() ->block(function () use ($pdfService) { $pdfService->generate(); }, amount: 1, lockSeconds: 30);
```
## #Quotas on Eloquent Models
Add the `HasQuotas` trait and the same builder hangs off the model:
```
use ZaberDev\Quota\HasQuotas; class User extends Authenticatable{ use HasQuotas;}
```
```
$user->quota('pdf_exports')->limit(25)->perMonth()->consume(); $user->quota('pdf_exports')->limit(25)->perMonth()->remaining();
```
On the database backend the records are polymorphic, so you can query a model's quotas like any other relation:
```
$activeQuotas = $user->quotas() ->where('period_end', '>', now()) ->get();
```
## #Route Middleware
The `quota` middleware takes a name, a limit, a period, and an optional driver:
```
Route::post('/exports/generate', [ExportController::class, 'store']) ->middlewa

## Summary

See Key Findings for full content.

## Related Articles

- [[enforce-per-action-waiting-periods-in-laravel-with-cooldown]]
- [[laravel-legacy-bridge-carry-authenticated-sessions-from-a-legacy-app-into-laravel]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[ai-music-video-arena-claude-vs-gpt-56]]
