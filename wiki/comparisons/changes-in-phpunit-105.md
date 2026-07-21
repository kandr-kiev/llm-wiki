---
title: "Changes in PHPUnit 10.5"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - data
  - framework
  - open-source
  - pipeline
  - system-design
  - use-case
---

# Changes in PHPUnit 10.5

> **Source:** local-ai-education-provendorphpunitphpunitchangelog-105md-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phpunit/phpunit/ChangeLog-10.5.md ingested: 2026-07-20 sha256: d9aed8dbf25f59acd56f2c7ea7dc436aab00f016c0103a133ad9c25a88338f31 blog_...
> **Sources:**
>   - local-ai-education-provendorphpunitphpunitchangelog-105md-2026-07-20.md
> **Links:**
- [[Change Log]]
- [[Changelog]]
- [[Version]]
- [[get ready for the powerful css border shape property]]
- [[Security Policy]]

## Key Findings

---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phpunit/phpunit/ChangeLog-10.5.md
ingested: 2026-07-20
sha256: d9aed8dbf25f59acd56f2c7ea7dc436aab00f016c0103a133ad9c25a88338f31
blog_source: local:unknown
---
# Changes in PHPUnit 10.5
All notable changes of the PHPUnit 10.5 release series are documented in this file using the [Keep a CHANGELOG](https://keepachangelog.com/) principles.
## [10.5.63] - 2026-01-27
### Fixed
* Regression introduced in PHPUnit 9.6.33
## [10.5.62] - 2026-01-27
### Changed
* To prevent Poisoned Pipeline Execution (PPE) attacks using prepared `.coverage` files in pull requests, a PHPT test will no longer be run if the temporary file for writing code coverage information already exists before the test runs
## [10.5.61] - 2026-01-24
### Changed
* `PHPUnit\Framework\MockObject` exceptions are now subtypes of `PHPUnit\Exception`
## [10.5.60] - 2025-12-06
* No changes; `phpunit.phar` rebuilt with PHP 8.4 to work around PHP-Scoper issue [#1139](https://github.com/humbug/php-scoper/issues/1139)
## [10.5.59] - 2025-12-01
### Changed
* [#6338](https://github.com/sebastianbergmann/phpunit/pull/6338): Removed code from `PHPUnit\Runner\TestSuiteSorter` that was only used in the tests for this class
* Updated list of deprecated PHP configuration settings for PHP 8.4, PHP 8.5, and PHP 8.6
## [10.5.58] - 2025-09-28
### Fixed
* [#6368](https://github.com/sebastianbergmann/phpunit/issues/6368): `failOnPhpunitWarning="false"` has no effect
## [10.5.57] - 2025-09-24
* No changes; `phpunit.phar` rebuilt with updated dependencies
## [10.5.56] - 2025-09-23
* No changes; `phpunit.phar` rebuilt with updated dependencies
## [10.5.55] - 2025-09-14
### Changed
* [#6366](https://github.com/sebastianbergmann/phpunit/issues/6366): Exclude `__sleep()` and `__wakeup()` from test double code generation on PHP >= 8.5
## [10.5.54] - 2025-09-11
### Changed
* Do not use `__sleep()` method (which will be deprecated in PHP 8.5)
## [10.5.53] - 2025-08-20
### Changed
* Do not configure `report_memleaks` setting (which will be deprecated in PHP 8.5) for PHPT processes
## [10.5.52] - 2025-08-16
### Changed
* [#6321](https://github.com/sebastianbergmann/phpunit/issues/6321): Allow `error_reporting=E_ALL` for `--check-php-configuration`
## [10.5.51] - 2025-08-12
### Changed
* [#6308](https://github.com/sebastianbergmann/phpunit/pull/6308): Improve output of `--check-php-configuration`
* The version number for the test result cache file has been incremented to reflect that its structure for PHPUnit 10.5 is not compatible with its structure for PHPUnit 8.5 and PHPUnit 9.6
## [10.5.50] - 2025-08-10
### Changed
* [#6300](https://github.com/sebastianbergmann/phpunit/issues/6300): Emit warning when the name of a data provider method begins with `test`
* Do not use `SplObjectStorage` methods that will be deprecated in PHP 8.5
## [10.5.49] - 2025-08-09
### Added
* [#6297](https://github.com/sebastianbergmann/phpunit/issues/6297): `--check-php-configuration`

## Summary

 CLI option for checking whether PHP is configured for testing
### Fixed
* Errors due to invalid data provided using `#[TestWith]` or `#[TestWithJson]` attributes are now properly reported
## [10.5.48] - 2025-07-11
### Fixed
* [#6254](https://github.com/sebastianbergmann/phpunit/issues/6254): `defects,random`configuration is supported by implementation, but it is not allowed by the XML configuration file schema
## [10.5.47] - 2025-06-20
### Added
* [#6236](https://github.com/sebastianbergmann/phpunit/issues/6236): `failOnPhpunitWarning` attribute on the `` element of the XML configuration file and `--fail-on-phpunit-warning` CLI option for controlling whether PHPUnit should fail on PHPUnit warnings (default: `true`)
* [#6239](https://github.com/sebastianbergmann/phpunit/issues/6239): `--do-not-fail-on-deprecation`, `--do-not-fail-on-phpunit-warning`, `--do-not-fail-on-phpunit-deprecation`, `--do-not-fail-on-empty-test-suite`, `--do-not-fail-on-incomplete`, `--do-not-fail-on-notice`, `--do-not-fail-on-risky`, `--do-not-fail-on-skipped`, and `--do-not-fail-on-warning` CLI options
* `--do-not-report-useless-tests` CLI option as a replacement for `--dont-report-useless-tests`
### Deprecated
* `--dont-report-useless-tests` CLI option (use `--do-not-report-useless-tests` instead)
### Fixed
* [#6243](https://github.com/sebastianbergmann/phpunit/issues/6243): Constraints cannot be implemented without using internal class `ExpectationFailedException`
## [10.5.46] - 2025-05-02
### Added
* `displayDetailsOnAllIssues` attribute on the `` element of the XML configuration file and `--display-all-issues` CLI option for controlling whether PHPUnit should display details on all issues that are triggered (default: `false`)
* `failOnAllIssues` attribute on the `` element of the XML configuration file and `--fail-on-all-issues` CLI option for controlling whether PHPUnit should fail on all issues that are triggered (default: `false`)
### Changed
* [#5956](https://github.com/sebastianbergmann/phpunit/issues/5956): Improved handling of deprecated `E_STRICT` constant
* Improved message when test is considered risky for printing unexpected output
## [10.5.45] - 2025-02-06
### Changed
* [#6117](https://github.com/sebastianbergmann/phpunit/issues/6117): Include source location information for issues triggered during test in `--debug` output
* [#6119](https://github.com/sebastianbergmann/phpunit/issues/6119): Improve message for errors that occur while parsing attributes
## [10.5.44] - 2025-01-31
### Fixed
* [#6115](https://github.com/sebastianbergmann/phpunit/issues/6115): Backed enumerations with values not of type `string` cannot be used in customized TestDox output
## [10.5.43] - 2025-01-29
### Changed
* Do not skip execution of test that depends on a test that is larger than itself
## [10.5.42] - 2025-01-28
### Fixed
* [#6103](https://github.com/sebastianbergmann/phpunit/issues/6103): Output from test run in separate process is printed twice
* [#6109](https://github.co

## Related Articles

- [[Change Log]]
- [[Changelog]]
- [[Version]]
- [[get ready for the powerful css border shape property]]
- [[Security Policy]]
