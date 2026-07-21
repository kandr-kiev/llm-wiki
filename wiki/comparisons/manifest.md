---
title: "Manifest"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - api
  - library
  - real-time
  - use-case
---

# Manifest

> **Source:** local-ai-education-provendorphar-iomanifestreadmemd-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phar-io/manifest/README.md ingested: 2026-07-20 sha256: 47c8d1538f764b09a92286018f8aadd28a2c76a02726191135e328862efb6a46 blog_source:...
> **Sources:**
>   - local-ai-education-provendorphar-iomanifestreadmemd-2026-07-20.md
> **Links:**
- [[installed.json]]
- [[composer.json]]
- [[Changelog]]
- [[ci.yml]]
- [[Local LLM Wiki Algorithm]]

## Key Findings

---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phar-io/manifest/README.md
ingested: 2026-07-20
sha256: 47c8d1538f764b09a92286018f8aadd28a2c76a02726191135e328862efb6a46
blog_source: local:unknown
---
# Manifest
Component for reading [phar.io](https://phar.io/) manifest information from a [PHP Archive (PHAR)](http://php.net/phar).
## Installation
You can add this library as a local, per-project dependency to your project using [Composer](https://getcomposer.org/):
composer require phar-io/manifest
If you only need this library during development, for instance to run your project's test suite, then you should add it as a development-time dependency:
composer require --dev phar-io/manifest
## Usage Examples
### Read from `manifest.xml`
```php
use PharIo\Manifest\ManifestLoader;
use PharIo\Manifest\ManifestSerializer;
$manifest = ManifestLoader::fromFile('manifest.xml');
var_dump($manifest);
echo (new ManifestSerializer)->serializeToString($manifest);
```
Output
```shell
object(PharIo\Manifest\Manifest)#14 (6) {
["name":"PharIo\Manifest\Manifest":private]=>
object(PharIo\Manifest\ApplicationName)#10 (1) {
["name":"PharIo\Manifest\ApplicationName":private]=>
string(12) "some/library"
}
["version":"PharIo\Manifest\Manifest":private]=>
object(PharIo\Version\Version)#12 (5) {
["originalVersionString":"PharIo\Version\Version":private]=>
string(5) "1.0.0"
["major":"PharIo\Version\Version":private]=>
object(PharIo\Version\VersionNumber)#13 (1) {
["value":"PharIo\Version\VersionNumber":private]=>
int(1)
}
["minor":"PharIo\Version\Version":private]=>
object(PharIo\Version\VersionNumber)#23 (1) {
["value":"PharIo\Version\VersionNumber":private]=>
int(0)
}
["patch":"PharIo\Version\Version":private]=>
object(PharIo\Version\VersionNumber)#22 (1) {
["value":"PharIo\Version\VersionNumber":private]=>
int(0)
}
["preReleaseSuffix":"PharIo\Version\Version":private]=>
NULL
}
["type":"PharIo\Manifest\Manifest":private]=>
object(PharIo\Manifest\Library)#6 (0) {
}
["copyrightInformation":"PharIo\Manifest\Manifest":private]=>
object(PharIo\Manifest\CopyrightInformation)#19 (2) {
["authors":"PharIo\Manifest\CopyrightInformation":private]=>
object(PharIo\Manifest\AuthorCollection)#9 (1) {
["authors":"PharIo\Manifest\AuthorCollection":private]=>
array(1) {
[0]=>
object(PharIo\Manifest\Author)#15 (2) {
["name":"PharIo\Manifest\Author":private]=>
string(13) "Reiner Zufall"
["email":"PharIo\Manifest\Author":private]=>
object(PharIo\Manifest\Email)#16 (1) {
["email":"PharIo\Manifest\Email":private]=>
string(16) "reiner@zufall.de"
}
}
}
}
["license":"PharIo\Manifest\CopyrightInformation":private]=>
object(PharIo\Manifest\License)#11 (2) {
["name":"PharIo\Manifest\License":private]=>
string(12) "BSD-3-Clause"
["url":"PharIo\Manifest\License":private]=>
object(PharIo\Manifest\Url)#18 (1) {
["url":"PharIo\Manifest\Url":private]=>
string(26) "https://domain.tld/LICENSE"
}
}
}
["requirements":"PharIo\Manifest\Manifest":private]=>
object(PharIo\Manifest\RequirementColl

## Summary

See Key Findings for full content.

## Related Articles

- [[installed.json]]
- [[composer.json]]
- [[Changelog]]
- [[ci.yml]]
- [[Local LLM Wiki Algorithm]]
