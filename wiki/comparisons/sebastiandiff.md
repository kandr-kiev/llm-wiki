---
title: "sebastian/diff"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - best-practice
  - ci-cd
  - library
  - real-time
  - use-case
---

# sebastian/diff

> **Source:** local-ai-education-provendorsebastiandiffreadmemd-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/diff/README.md ingested: 2026-07-20 sha256: cabd5afb55bd5bbc96ce9d620d732c6806c957e4d8ca5435ca1b094ca882fc82 blog_source: l...
> **Sources:**
>   - local-ai-education-provendorsebastiandiffreadmemd-2026-07-20.md
> **Links:**
- [[phpunit/php-timer]]
- [[sebastian/code-unit]]
- [[sebastian/complexity]]
- [[sebastian/cli-parser]]
- [[php-file-iterator]]

## Key Findings

---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/diff/README.md
ingested: 2026-07-20
sha256: cabd5afb55bd5bbc96ce9d620d732c6806c957e4d8ca5435ca1b094ca882fc82
blog_source: local:unknown
---
[![Latest Stable Version](https://poser.pugx.org/sebastian/diff/v/stable.png)](https://packagist.org/packages/sebastian/diff)
[![CI Status](https://github.com/sebastianbergmann/diff/workflows/CI/badge.svg)](https://github.com/sebastianbergmann/diff/actions)
[![Type Coverage](https://shepherd.dev/github/sebastianbergmann/diff/coverage.svg)](https://shepherd.dev/github/sebastianbergmann/diff)
[![codecov](https://codecov.io/gh/sebastianbergmann/diff/branch/main/graph/badge.svg)](https://codecov.io/gh/sebastianbergmann/diff)
# sebastian/diff
Diff implementation for PHP, factored out of PHPUnit into a stand-alone component.
## Installation
You can add this library as a local, per-project dependency to your project using [Composer](https://getcomposer.org/):
```
composer require sebastian/diff
```
If you only need this library during development, for instance to run your project's test suite, then you should add it as a development-time dependency:
```
composer require --dev sebastian/diff
```
### Usage
#### Generating diff
The `Differ` class can be used to generate a textual representation of the difference between two strings:
```php
diff('foo', 'bar');
```
The code above yields the output below:
```diff
--- Original
+++ New
@@ @@
-foo
+bar
```
There are three output builders available in this package:
#### UnifiedDiffOutputBuilder
This is default builder, which generates the output close to udiff and is used by PHPUnit.
```php
diff('foo', 'bar');
```
#### StrictUnifiedDiffOutputBuilder
Generates (strict) Unified diff's (unidiffs) with hunks,
similar to `diff -u` and compatible with `patch` and `git apply`.
```php
true, // ranges of length one are rendered with the trailing `,1`
'commonLineThreshold' => 6, // number of same lines before ending a new hunk and creating a new one (if needed)
'contextLines' => 3, // like `diff: -u, -U NUM, --unified[=NUM]`, for patch/git apply compatibility best to keep at least @ 3
'fromFile' => '',
'fromFileDate' => null,
'toFile' => '',
'toFileDate' => null,
]);
$differ = new Differ($builder);
print $differ->diff('foo', 'bar');
```
#### DiffOnlyOutputBuilder
Output only the lines that differ.
```php
diff('foo', 'bar');
```
#### DiffOutputBuilderInterface
You can pass any output builder to the `Differ` class as longs as it implements the `DiffOutputBuilderInterface`.
#### Parsing diff
The `Parser` class can be used to parse a unified diff into an object graph:
```php
use SebastianBergmann\Diff\Parser;
use SebastianBergmann\Git;
$git = new Git('/usr/local/src/money');
$diff = $git->getDiff(
'948a1a07768d8edd10dcefa8315c1cbeffb31833',
'c07a373d2399f3e686234c4f7f088d635eb9641b'
);
$parser = new Parser;
print_r($parser->parse($diff));
```
The code above yields the output below:
Array
(
[0] => SebastianBergmann

## Summary

See Key Findings for full content.

## Related Articles

- [[phpunit/php-timer]]
- [[sebastian/code-unit]]
- [[sebastian/complexity]]
- [[sebastian/cli-parser]]
- [[php-file-iterator]]
