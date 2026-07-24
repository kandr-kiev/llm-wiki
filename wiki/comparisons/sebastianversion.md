---
title: "sebastian/version"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - library
  - real-time
  - use-case
---

# sebastian/version

> **Source:** local-ai-education-provendorsebastianversionreadmemd-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/version/README.md ingested: 2026-07-20 sha256: aa4c7e29847473bc2bad6ecd0a8c5ad37dd6442bc2e4c1dc368c38f9ef2060c6 blog_source...
> **Sources:**
>   - local-ai-education-provendorsebastianversionreadmemd-2026-07-20.md
> **Links:**
- [[sebastian/code-unit]]
- [[sebastian/type]]
- [[sebastian/complexity]]
- [[version]]
- [[phpunit/php-timer]]

## Key Findings

---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/version/README.md
ingested: 2026-07-20
sha256: aa4c7e29847473bc2bad6ecd0a8c5ad37dd6442bc2e4c1dc368c38f9ef2060c6
blog_source: local:unknown
---
[![Latest Stable Version](https://poser.pugx.org/sebastian/version/v/stable.png)](https://packagist.org/packages/sebastian/version)
# sebastian/version
**sebastian/version** is a library that helps with managing the version number of Git-hosted PHP projects.
## Installation
You can add this library as a local, per-project dependency to your project using [Composer](https://getcomposer.org/):
```
composer require sebastian/version
```
If you only need this library during development, for instance to run your project's test suite, then you should add it as a development-time dependency:
```
composer require --dev sebastian/version
```
## Usage
The constructor of the `SebastianBergmann\Version` class expects two parameters:
* `$release` is the version number of the latest release (`X.Y.Z`, for instance) or the name of the release series (`X.Y`) when no release has been made from that branch / for that release series yet.
* `$path` is the path to the directory (or a subdirectory thereof) where the sourcecode of the project can be found. Simply passing `__DIR__` here usually suffices.
Apart from the constructor, the `SebastianBergmann\Version` class has a single public method: `asString()`.
Here is a contrived example that shows the basic usage:
```php
asString());
```
```
string(18) "1.0.0-17-g00f3408"
```
When a new release is prepared, the string that is passed to the constructor as the first argument needs to be updated.
### How SebastianBergmann\Version::asString() works
* If `$path` is not (part of) a Git repository and `$release` is in `X.Y.Z` format then `$release` is returned as-is.
* If `$path` is not (part of) a Git repository and `$release` is in `X.Y` format then `$release` is returned suffixed with `-dev`.
* If `$path` is (part of) a Git repository and `$release` is in `X.Y.Z` format then the output of `git describe --tags` is returned as-is.
* If `$path` is (part of) a Git repository and `$release` is in `X.Y` format then a string is returned that begins with `X.Y` and ends with information from `git describe --tags`.

## Summary

See Key Findings for full content.

## Related Articles

- [[sebastian/code-unit]]
- [[sebastian/type]]
- [[sebastian/complexity]]
- [[version]]
- [[phpunit/php-timer]]
