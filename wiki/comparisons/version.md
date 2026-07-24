---
title: "Version"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - ci-cd
  - compliance
  - library
  - real-time
  - use-case
---

# Version

> **Source:** local-ai-education-provendorphar-ioversionreadmemd-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phar-io/version/README.md ingested: 2026-07-20 sha256: 5b22b08ba710857a8b50cdc44cbca89fba49f75bdc8fd8e56f8d0b44e0d39ed0 blog_source:...
> **Sources:**
>   - local-ai-education-provendorphar-ioversionreadmemd-2026-07-20.md
> **Links:**
- [[manifest]]
- [[changelog]]
- [[installed.json]]
- [[composer.json]]
- [[ci.yml]]

## Key Findings

---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phar-io/version/README.md
ingested: 2026-07-20
sha256: 5b22b08ba710857a8b50cdc44cbca89fba49f75bdc8fd8e56f8d0b44e0d39ed0
blog_source: local:unknown
---
# Version
Library for handling version information and constraints
[![Build Status](https://travis-ci.org/phar-io/version.svg?branch=master)](https://travis-ci.org/phar-io/version)
## Installation
You can add this library as a local, per-project dependency to your project using [Composer](https://getcomposer.org/):
composer require phar-io/version
If you only need this library during development, for instance to run your project's test suite, then you should add it as a development-time dependency:
composer require --dev phar-io/version
## Version constraints
A Version constraint describes a range of versions or a discrete version number. The format of version numbers follows the schema of [semantic versioning](http://semver.org): `..`. A constraint might contain an operator that describes the range.
Beside the typical mathematical operators like `=`, there are two special operators:
*Caret operator*: `^1.0`
can be written as `>=1.0.0 =1.0.0 parse( '^7.0' );
$caret_constraint->complies( new Version( '7.0.17' ) ); // true
$caret_constraint->complies( new Version( '7.1.0' ) ); // true
$caret_constraint->complies( new Version( '6.4.34' ) ); // false
$tilde_constraint = $parser->parse( '~1.1.0' );
$tilde_constraint->complies( new Version( '1.1.4' ) ); // true
$tilde_constraint->complies( new Version( '1.2.0' ) ); // false
```
As of version 2.0.0, pre-release labels are supported and taken into account when comparing versions:
```php
$leftVersion = new PharIo\Version\Version('3.0.0-alpha.1');
$rightVersion = new PharIo\Version\Version('3.0.0-alpha.2');
$leftVersion->isGreaterThan($rightVersion); // false
$rightVersion->isGreaterThan($leftVersion); // true
```

## Summary

See Key Findings for full content.

## Related Articles

- [[manifest]]
- [[changelog]]
- [[installed.json]]
- [[composer.json]]
- [[ci.yml]]
