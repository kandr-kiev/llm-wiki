---
title: "laravel legacy bridge carry authenticated sessions from a legacy app into laravel"
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
  - prompt-tuning
  - use-case
---

# laravel legacy bridge carry authenticated sessions from a legacy app into laravel

> **Source:** laravel-legacy-bridge-carry-authenticated-sessions-from-a-legacy-app-into-laravel-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** # Laravel Legacy Bridge: Carry Authenticated Sessions from a Legacy App into Laravel Last updated on July 14th, 2026 by [ Yannick Lyn Fatt ](/@ylynfatt) ![Laravel Legacy Bridge: Carry Authenticated Se...
> **Sources:**
>   - laravel-legacy-bridge-carry-authenticated-sessions-from-a-legacy-app-into-laravel-2026-07-17.md
> **Links:**
- [[enforce-per-action-waiting-periods-in-laravel-with-cooldown]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[workers-cache]]
- [[ai-music-video-arena-claude-vs-gpt-56]]

## Key Findings

# Laravel Legacy Bridge: Carry Authenticated Sessions from a Legacy App into Laravel
Last updated on
July 14th, 2026
by
[
Yannick Lyn Fatt
](/@ylynfatt)
![Laravel Legacy Bridge: Carry Authenticated Sessions from a Legacy App into Laravel image](https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/Legacy-Bridge-LN.png)
Migrating an application to Laravel one route at a time leaves you with two apps and one user, and the user only logged into one of them. They sign in on the old CodeIgniter or custom PHP side, cross into a Laravel-handled route, and Laravel, knowing nothing about that session, sends them to a login form. Laravel Legacy Bridge, a package from [Chris Keller](https://github.com/chr15k), reads the legacy session cookie on unauthenticated requests, decodes the session payload out of the legacy database, and authenticates the matching user in Laravel.
Here's what the package covers:
- **A middleware bridge** that runs only on unauthenticated requests and stops consulting the legacy store once Laravel has its own session
- **Payload decoding** for native PHP session encoding, JSON, Laravel's `base64(serialize())` format, and encrypted payloads
- **Resolver drivers** to locate the user ID in the payload: auto-detection, an explicit dot-notation key, or a class of your own
- **Typed events** for successful bridges, known failures, and unexpected exceptions, with no logging of its own
- **Legacy session invalidation** so a given legacy session can only be bridged once
- **An interactive install command** with framework presets, plus a `verify` command to test the wiring before real traffic hits it
- **Optional context carrying** for values like a locale or cart ID that live in the legacy payload
## #How the Bridge Works
Registering one middleware puts the bridge in the request path:
```
->withMiddleware(function (Middleware $middleware) { $middleware->web(append: [ \Chr15k\LegacyBridge\Http\Middleware\LegacySessionBridge::class, ]);})
```
On an unauthenticated request it reads the legacy cookie (`PHPSESSID` by default), looks up the row in the legacy sessions table, decodes the payload, resolves a user ID, and calls `loginUsingId()`. Laravel then writes its own session, and later requests never touch the legacy store. The service provider also excludes the legacy cookie from Laravel's `EncryptCookies` middleware, so there's no `encryptCookies()` list to maintain.
## #Resolvers and Payload Formats
Every legacy app stores the user ID under a different key, so the lookup is configurable. Pick a resolver driver in `config/legacy-bridge.php`:
```
// Auto: tries known patterns (default)'resolver' => ['driver' => 'auto'], // Key: explicit dot-notation path'resolver' => ['driver' => 'key', 'key' => 'user_id'], // Custom: your own implementation'resolver' => ['driver' => 'custom', 'class' => \App\Bridge\LegacyUserResolver::class],
```
The README recommends starting on `auto` and switching to `key` or `custom` before production. A c

## Summary

ustom resolver is also where you'd map old user IDs to new ones if your migration re-seeded the users table. Payload format is a separate setting (`auto`, `php_session`, `json`, `laravel`, or `encrypted`), and the encrypted format reads the legacy app's key from `LEGACY_BRIDGE_APP_KEY`.
## #Events
The bridge writes nothing to your log files. It dispatches `LegacySessionBridged` on success, `LegacySessionBridgeFailed` for known failures, and `LegacySessionBridgeError` for unexpected exceptions, and leaves the reporting to your listeners.
Failures carry a `BridgeFailureReason` enum with eight cases, among them `MissingCookie`, `AmbiguousCookie`, `SessionExpired`, `PayloadDecodeFailed`, and `UserNotResolved`. Some point at a misconfiguration, others are ordinary, like a session that timed out. The failure event also carries a `BridgeContext` DTO holding whatever the bridge resolved before it stopped:
```
$event->context->cookieName$event->context->sessionId // resolved session ID (if reached)$event->context->payload // decoded payload (if reached)$event->context->userId // resolved user ID (if reached)$event->context->requestContext // ['ip', 'path', 'method', 'user_agent']
```
## #Installation
```
composer require chr15k/laravel-legacy-bridgephp artisan legacy-bridge:install
```
The install command is interactive. It includes presets for common legacy frameworks, collects the database credentials, and writes the `.env` entries for you.
## #The Verify Command
A misconfigured bridge fails on real cookies against a real legacy database, which is not what your test suite exercises. The package ships a command that checks the configuration against that database:
```
php artisan legacy-bridge:verifyphp artisan legacy-bridge:verify --session-id=a_real_session_id
```
Run it bare and it checks that the config is readable, the legacy database is reachable, the sessions table exists and has rows, the resolver is configured, and no cookie names collide. Pass a real session ID and it reports what the bridge would do with that session: format detected, payload keys found, user ID resolved, user confirmed to exist. It authenticates no one and modifies nothing.
## #Limitations and Security
The first release supports database sessions only, not the file, Redis, or Memcached drivers. It bridges web requests, not stateless API requests, and only into the default auth guard. It requires Laravel 13 and PHP 8.3 or newer.
Read the security section of the README before you deploy. The bridge deserializes payloads read straight from the legacy sessions table, which makes that database a trust boundary; the author recommends read-only credentials where possible. The legacy cookie travels unencrypted by design, the same way it did on the old app, so both applications need HTTPS. The default `after_write` invalidation strategy deletes the legacy session once Laravel writes its own, and the docs advise against setting it to `never` in production.
The source code and a full use

## Related Articles

- [[enforce-per-action-waiting-periods-in-laravel-with-cooldown]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[sites-that-block-ai-training-crawlers-mostly-ignore-the-answer-time-bots-2026-07-07]]
- [[workers-cache]]
- [[ai-music-video-arena-claude-vs-gpt-56]]
