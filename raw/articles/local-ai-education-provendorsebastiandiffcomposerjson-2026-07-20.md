---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/diff/composer.json
ingested: 2026-07-20
sha256: 8509b6b7ba666538a64300700a67bb9e287fba212ff5aa679eeb9dd6492f8324
blog_source: local:unknown
---
{
    "name": "sebastian/diff",
    "description": "Diff implementation",
    "keywords": ["diff", "udiff", "unidiff", "unified diff"],
    "homepage": "https://github.com/sebastianbergmann/diff",
    "license": "BSD-3-Clause",
    "authors": [
        {
            "name": "Sebastian Bergmann",
            "email": "sebastian@phpunit.de"
        },
        {
            "name": "Kore Nordmann",
            "email": "mail@kore-nordmann.de"
        }
    ],
    "support": {
        "issues": "https://github.com/sebastianbergmann/diff/issues",
        "security": "https://github.com/sebastianbergmann/diff/security/policy"
    },
    "prefer-stable": true,
    "config": {
        "platform": {
            "php": "8.1.0"
        },
        "optimize-autoloader": true,
        "sort-packages": true
    },
    "require": {
        "php": ">=8.1"
    },
    "require-dev": {
        "phpunit/phpunit": "^10.0",
        "symfony/process": "^6.4"
    },
    "autoload": {
        "classmap": [
            "src/"
        ]
    },
    "autoload-dev": {
        "classmap": [
            "tests/"
        ]
    },
    "extra": {
        "branch-alias": {
            "dev-main": "5.1-dev"
        }
    }
}
