---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phpunit/php-invoker/composer.json
ingested: 2026-07-20
sha256: ae7807e0d9360e1177ab4dbfb8ada7ecbdeb98f550c83daf4955e5a9d2452790
blog_source: local:unknown
---
{
    "name": "phpunit/php-invoker",
    "description": "Invoke callables with a timeout",
    "type": "library",
    "keywords": [
        "process"
    ],
    "homepage": "https://github.com/sebastianbergmann/php-invoker/",
    "license": "BSD-3-Clause",
    "authors": [
        {
            "name": "Sebastian Bergmann",
            "email": "sebastian@phpunit.de",
            "role": "lead"
        }
    ],
    "support": {
        "issues": "https://github.com/sebastianbergmann/php-invoker/issues"
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
        "ext-pcntl": "*",
        "phpunit/phpunit": "^10.0"
    },
    "autoload": {
        "classmap": [
            "src/"
        ]
    },
    "autoload-dev": {
        "classmap": [
            "tests/_fixture/"
        ]
    },
    "suggest": {
        "ext-pcntl": "*"
    },
    "extra": {
        "branch-alias": {
            "dev-main": "4.0-dev"
        }
    }
}

