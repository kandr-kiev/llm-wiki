---
title: "ci.yml"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - ci-cd
---

# ci.yml

> **Source:** local-ai-education-provendorphar-iomanifestgithubworkflowsciyml-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phar-io/manifest/.github/workflows/ci.yml ingested: 2026-07-20 sha256: c6dcd51f30550a08e5f1e0487bd107ce503f85578f46d07534b021ff48da06...
> **Sources:**
>   - local-ai-education-provendorphar-iomanifestgithubworkflowsciyml-2026-07-20.md
> **Links:**
- [[Changelog]]
- [[composer.json]]
- [[installed.json]]
- [[package.json]]
- [[DeepCopy]]

## Key Findings

---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phar-io/manifest/.github/workflows/ci.yml
ingested: 2026-07-20
sha256: c6dcd51f30550a08e5f1e0487bd107ce503f85578f46d07534b021ff48da0686
blog_source: local:unknown
---
name: "CI"
on:
push:
branches:
- "master"
pull_request: null
jobs:
qa:
name: "QA"
runs-on: "ubuntu-latest"
steps:
- name: "Checkout"
uses: "actions/checkout@v3.5.2"
- name: "Set up PHP"
uses: "shivammathur/setup-php@2.25.1"
with:
coverage: "none"
php-version: "8.0"
tools: "phive"
- name: "Install dependencies with composer"
run: "composer install --no-interaction --optimize-autoloader --prefer-dist"
- name: "Install dependencies with phive"
env:
GITHUB_AUTH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
run: "ant install-tools"
- name: "Run php-cs-fixer"
run: "ant php-cs-fixer"
- name: "Run psalm"
run: "ant psalm"
tests:
name: "Tests"
runs-on: "ubuntu-latest"
strategy:
fail-fast: false
matrix:
php-versions:
- "7.2"
- "7.3"
- "7.4"
- "8.0"
- "8.1"
- "8.2"
steps:
- name: "Checkout"
uses: "actions/checkout@v3.5.2"
- name: "Set up PHP"
uses: "shivammathur/setup-php@2.25.1"
env:
COMPOSER_TOKEN: "${{ secrets.GITHUB_TOKEN }}"
with:
coverage: "pcov"
extensions: "${{ env.extensions }}"
ini-values: "display_errors=On, error_reporting=-1, memory_limit=2G"
php-version: "${{ matrix.php-versions }}"
tools: "phive"
- name: "Install dependencies with composer"
run: "composer install --no-interaction --optimize-autoloader --prefer-dist"
- name: "Install dependencies with phive"
env:
GITHUB_AUTH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
run: "ant install-tools"
- name: "Run PHPUnit"
run: "tools/phpunit --coverage-clover build/logs/clover.xml"
- name: "Send code coverage report to codecov.io"
uses: "codecov/codecov-action@v3.1.4"
with:
files: "build/logs/clover.xml"

## Summary

See Key Findings for full content.

## Related Articles

- [[Changelog]]
- [[composer.json]]
- [[installed.json]]
- [[package.json]]
- [[DeepCopy]]
