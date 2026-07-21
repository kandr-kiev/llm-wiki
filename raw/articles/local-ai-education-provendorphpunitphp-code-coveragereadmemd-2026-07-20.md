---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phpunit/php-code-coverage/README.md
ingested: 2026-07-20
sha256: 7bbdb95c5f533e92a81fd11f1226e05e44300f7a86b8cc179b90d9cc18e4c82d
blog_source: local:unknown
---
# phpunit/php-code-coverage

[![Latest Stable Version](https://poser.pugx.org/phpunit/php-code-coverage/v/stable.png)](https://packagist.org/packages/phpunit/php-code-coverage)
[![CI Status](https://github.com/sebastianbergmann/php-code-coverage/workflows/CI/badge.svg)](https://github.com/sebastianbergmann/php-code-coverage/actions)
[![Type Coverage](https://shepherd.dev/github/sebastianbergmann/php-code-coverage/coverage.svg)](https://shepherd.dev/github/sebastianbergmann/php-code-coverage)
[![codecov](https://codecov.io/gh/sebastianbergmann/php-code-coverage/branch/main/graph/badge.svg)](https://codecov.io/gh/sebastianbergmann/php-code-coverage)

Provides collection, processing, and rendering functionality for PHP code coverage information.

## Installation

You can add this library as a local, per-project dependency to your project using [Composer](https://getcomposer.org/):

```
composer require phpunit/php-code-coverage
```

If you only need this library during development, for instance to run your project's test suite, then you should add it as a development-time dependency:

```
composer require --dev phpunit/php-code-coverage
```

## Usage

```php
<?php declare(strict_types=1);
use SebastianBergmann\CodeCoverage\Filter;
use SebastianBergmann\CodeCoverage\Driver\Selector;
use SebastianBergmann\CodeCoverage\CodeCoverage;
use SebastianBergmann\CodeCoverage\Report\Html\Facade as HtmlReport;

$filter = new Filter;

$filter->includeFiles(
    [
        '/path/to/file.php',
        '/path/to/another_file.php',
    ]
);

$coverage = new CodeCoverage(
    (new Selector)->forLineCoverage($filter),
    $filter
);

$coverage->start('<name of test>');

// ...

$coverage->stop();


(new HtmlReport)->process($coverage, '/tmp/code-coverage-report');
```
