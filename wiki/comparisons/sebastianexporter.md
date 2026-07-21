---
title: "sebastian/exporter"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - ci-cd
  - data
  - library
  - real-time
  - self-supervised
  - use-case
---

# sebastian/exporter

> **Source:** local-ai-education-provendorsebastianexporterreadmemd-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/exporter/README.md ingested: 2026-07-20 sha256: b5df640d0b81f2cd53769c0da5f72517653f3c356913d553907f31f473e0f949 blog_sourc...
> **Sources:**
>   - local-ai-education-provendorsebastianexporterreadmemd-2026-07-20.md
> **Links:**
- [[sebastian/code-unit]]
- [[sebastian/complexity]]
- [[sebastian/diff]]
- [[phpunit/php-timer]]
- [[sebastian/comparator]]

## Key Findings

---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/exporter/README.md
ingested: 2026-07-20
sha256: b5df640d0b81f2cd53769c0da5f72517653f3c356913d553907f31f473e0f949
blog_source: local:unknown
---
[![Latest Stable Version](https://poser.pugx.org/sebastian/exporter/v/stable.png)](https://packagist.org/packages/sebastian/exporter)
[![CI Status](https://github.com/sebastianbergmann/exporter/workflows/CI/badge.svg)](https://github.com/sebastianbergmann/exporter/actions)
[![Type Coverage](https://shepherd.dev/github/sebastianbergmann/exporter/coverage.svg)](https://shepherd.dev/github/sebastianbergmann/exporter)
[![codecov](https://codecov.io/gh/sebastianbergmann/exporter/branch/main/graph/badge.svg)](https://codecov.io/gh/sebastianbergmann/exporter)
# sebastian/exporter
This component provides the functionality to export PHP variables for visualization.
## Installation
You can add this library as a local, per-project dependency to your project using [Composer](https://getcomposer.org/):
```
composer require sebastian/exporter
```
If you only need this library during development, for instance to run your project's test suite, then you should add it as a development-time dependency:
```
composer require --dev sebastian/exporter
```
## Usage
Exporting:
```php
''
'string' => ''
'code' => 0
'file' => '/home/sebastianbergmann/test.php'
'line' => 34
'previous' => null
)
*/
print $exporter->export(new Exception);
```
## Data Types
Exporting simple types:
```php
export(46);
// 4.0
print $exporter->export(4.0);
// 'hello, world!'
print $exporter->export('hello, world!');
// false
print $exporter->export(false);
// NAN
print $exporter->export(acos(8));
// -INF
print $exporter->export(log(0));
// null
print $exporter->export(null);
// resource(13) of type (stream)
print $exporter->export(fopen('php://stderr', 'w'));
// Binary String: 0x000102030405
print $exporter->export(chr(0) . chr(1) . chr(2) . chr(3) . chr(4) . chr(5));
```
Exporting complex types:
```php
Array &1 (
0 => 1
1 => 2
2 => 3
)
1 => Array &2 (
0 => ''
1 => 0
2 => false
)
)
*/
print $exporter->export(array(array(1,2,3), array("",0,FALSE)));
/*
Array &0 (
'self' => Array &1 (
'self' => Array &1
)
)
*/
$array = array();
$array['self'] = &$array;
print $exporter->export($array);
/*
stdClass Object &0000000003a66dcc0000000025e723e2 (
'self' => stdClass Object &0000000003a66dcc0000000025e723e2
)
*/
$obj = new stdClass();
$obj->self = $obj;
print $exporter->export($obj);
```
Compact exports:
```php
shortenedExport(array());
// Array (...)
print $exporter->shortenedExport(array(1,2,3,4,5));
// stdClass Object ()
print $exporter->shortenedExport(new stdClass);
// Exception Object (...)
print $exporter->shortenedExport(new Exception);
// this\nis\na\nsuper\nlong\nstring\nt...\nspace
print $exporter->shortenedExport(
<<<LONG_STRING
this
is
a
super
long
string
that
wraps
a
lot
and
eats
up
a
lot
of
space
LONG_STRING
);
```

## Summary

See Key Findings for full content.

## Related Articles

- [[sebastian/code-unit]]
- [[sebastian/complexity]]
- [[sebastian/diff]]
- [[phpunit/php-timer]]
- [[sebastian/comparator]]
