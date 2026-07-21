---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/cli-parser/composer.json
ingested: 2026-07-20
sha256: d6c00323d2524feac5dea3cdeb9fa0269aed0bbb9921fbdbe730d9cc2bd85564
blog_source: local:unknown
---
{
    "name": "sebastian/cli-parser",
    "description": "Library for parsing CLI options",
    "type": "library",
    "homepage": "https://github.com/sebastianbergmann/cli-parser",
    "license": "BSD-3-Clause",
    "authors": [
        {
            "name": "Sebastian Bergmann",
            "email": "sebastian@phpunit.de",
            "role": "lead"
        }
    ],
    "support": {
        "issues": "https://github.com/sebastianbergmann/cli-parser/issues",
        "security": "https://github.com/sebastianbergmann/cli-parser/security/policy"
    },
    "prefer-stable": true,
    "require": {
        "php": ">=8.1"
    },
    "require-dev": {
        "phpunit/phpunit": "^10.0"
    },
    "config": {
        "platform": {
            "php": "8.1.0"
        },
        "optimize-autoloader": true,
        "sort-packages": true
    },
    "autoload": {
        "classmap": [
            "src/"
        ]
    },
    "extra": {
        "branch-alias": {
            "dev-main": "2.0-dev"
        }
    }
}
