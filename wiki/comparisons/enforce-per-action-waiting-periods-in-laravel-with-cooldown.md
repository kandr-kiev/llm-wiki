---
title: "enforce per action waiting periods in laravel with cooldown"
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

# enforce per action waiting periods in laravel with cooldown

> **Source:** enforce-per-action-waiting-periods-in-laravel-with-cooldown-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** # Enforce Per-Action Waiting Periods in Laravel with Cooldown Last updated on July 15th, 2026 by [ Yannick Lyn Fatt ](/@ylynfatt) ![Enforce Per-Action Waiting Periods in Laravel with Cooldown image](h...
> **Sources:**
>   - enforce-per-action-waiting-periods-in-laravel-with-cooldown-2026-07-17.md
> **Links:**
- [[Mesh LLM: distributed AI computing on iroh]]
- [[workers-cache]]
- [[ai-music-video-arena-claude-vs-gpt-56]]
- [[release-v0251]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]

## Key Findings

# Enforce Per-Action Waiting Periods in Laravel with Cooldown
Last updated on
July 15th, 2026
by
[
Yannick Lyn Fatt
](/@ylynfatt)
![Enforce Per-Action Waiting Periods in Laravel with Cooldown image](https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/Laravel-Cooldown-LN.png)
Laravel Cooldown is a package from [Mahedi Zaman Zaber](https://github.com/zaber-dev) for putting a timed lock on a named action: no second OTP for 120 seconds, one password reset request per minute, a payment retry that can't fire again until the window clears. Where Laravel's `RateLimiter` counts how many requests hit an endpoint within a window, Cooldown tracks whether a specific action for a specific owner is still within its waiting period and can persist that state in the database rather than only in the cache.
## #Main features
- **Owner-scoped actions** through `Cooldown::for('resend_verification', $user)`, where the owner can be any model, an IP string, or nothing for a global lock
- **A `HasCooldowns` trait** that puts `$user->cooldown('change_avatar')` on any Eloquent model
- **Route middleware** (`cooldown:action,duration`) with an optional driver argument
- **Atomic execution** via `block()`, which takes a lock around the callback and sets the cooldown on success
- **`enforce()`** to throw a `CooldownActiveException` that renders as HTTP 429
- **An immutable `CooldownInfo` object** with `remainingSeconds()` and `remainingForHumans()`
- **Cache or database backends**, switchable per call with `using()`
- **Pruning** of expired database rows through Laravel's `model:prune` command
## #The Fluent API
A cooldown is a named action, an optional owner, and a duration. Once you name one, you can set it, check it, or clear it:
```
use ZaberDev\Cooldown\Facades\Cooldown; Cooldown::for('rebuild_search_index')->for(600); Cooldown::for('resend_verification', $user)->for(900); Cooldown::for('daily_checkin', $user)->until(now()->endOfDay());
```
When a cooldown is active, `info()` returns an object with the duration details:
```
if (Cooldown::for('resend_verification', $user)->active()) { $info = Cooldown::for('resend_verification', $user)->info();  echo "Please wait " . $info->remainingForHumans() . " before requesting another email."; echo "Seconds remaining: " . $info->remainingSeconds();}
```
If you'd rather stop the request than branch on it, `enforce()` throws when the action is still locked:
```
Cooldown::for('request_password_reset', $user)->enforce();
```
## #Atomic Blocking
Cooldowns exist for exactly this situation: sending an OTP, charging a card, where two concurrent requests can both pass the check before either one sets the lock. `block()` handles this by acquiring a lock, running the callback, and applying the cooldown only if the work succeeds:
```
Cooldown::for('send_login_code', $user)->block(function () use ($smsClient, $user) { $smsClient->sendCode($user->phone);}, duration: 90);
```
If you need to manage the lock yourself, `acquireLock(

## Summary

)` and `releaseLock()` are available for that purpose.
## #Cooldowns on Eloquent Models
Add the `HasCooldowns` trait and the same builder hangs off the model instance, scoped to that record:
```
use ZaberDev\Cooldown\HasCooldowns; class User extends Authenticatable{ use HasCooldowns;}
```
```
$user->cooldown('change_avatar')->for(300); if ($user->cooldown('change_avatar')->active()) { return response()->json(['message' => 'You can change your avatar again shortly.'], 429);} $user->cooldown('change_avatar')->reset();
```
On the database backend, the records are polymorphic, so a model's cooldowns are queryable like any other relation:
```
$activeCooldowns = $user->cooldowns()->where('expires_at', '>', now())->get(); $user->cooldowns()->delete();
```
## #Route Middleware
The `cooldown` middleware takes an action name, a duration in seconds, and an optional driver:
```
Route::post('/feedback', [FeedbackController::class, 'store']) ->middleware('cooldown:submit_feedback,120'); Route::post('/invoices/export', [InvoiceController::class, 'export']) ->middleware('cooldown:invoice_export,600,database');
```
## #Storage Backends
The default driver is `cache`, backed by the store you've configured, so both Redis and Memcached work. The `database` driver writes to a `cooldowns` table instead, which is what you want when the lock is tied to something like billing and can't be removed during a cache flush. You can choose per call:
```
Cooldown::for('poll_job_status', $ip)->using('cache')->for(20); Cooldown::for('renew_subscription', $user)->using('database')->for(86400);
```
If you need somewhere else to keep the state, `Cooldown::extend()` registers a custom driver from a service provider, and expired database rows can be cleared on a schedule with Laravel's `model:prune` command.
## #Installation
The package requires PHP 8.2 and supports Laravel 11, 12, and 13:
```
composer require zaber-dev/laravel-cooldown php artisan vendor:publish --provider="ZaberDev\Cooldown\CooldownServiceProvider"php artisan migrate
```
`config/cooldown.php` sets the default driver (`COOLDOWN_DRIVER`), the cache store and key prefix, the database table name, and whether events are dispatched.
You can find installation instructions and full documentation on [GitHub](https://github.com/zaber-dev/laravel-cooldown).
![Yannick Lyn Fatt photo](https://www.gravatar.com/avatar/d2e1d15c9ca048ffff35a1ba26047471?s=200)
[
Yannick Lyn Fatt
](/@ylynfatt)
Staff Writer at Laravel News and Full stack web developer.
[
![X](https://picperf.io/https://laravel-news.com/images/x.svg)
X
](https://x.com/ylynfatt)
[
![Threads](https://picperf.io/https://laravel-news.com/images/threads.svg)
Threads
](https://threads.net/ylynfatt)
[
![Instagram](https://picperf.io/https://laravel-news.com/images/instagram.svg)
Instagram
](https://instagram.com/ylynfatt)
[
![Github](https://picperf.io/https://laravel-news.com/images/github.svg)
Github
](https://github.com/ylynfatt)
[
![LinkedIn](https://picperf.io/https://larav

## Related Articles

- [[Mesh LLM: distributed AI computing on iroh]]
- [[workers-cache]]
- [[ai-music-video-arena-claude-vs-gpt-56]]
- [[release-v0251]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
