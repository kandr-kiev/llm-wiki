---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/code-unit/composer.json
ingested: 2026-07-20
sha256: 6aa889acd8567342c450d1afe3b80d5c96e19a69c916524e8947cb98b90a9336
blog_source: local:unknown
---
{
    "name": "sebastian/code-unit",
    "description": "Collection of value objects that represent the PHP code units",
    "type": "library",
    "homepage": "https://github.com/sebastianbergmann/code-unit",
    "license": "BSD-3-Clause",
    "authors": [
        {
            "name": "Sebastian Bergmann",
            "email": "sebastian@phpunit.de",
            "role": "lead"
        }
    ],
    "support": {
        "issues": "https://github.com/sebastianbergmann/code-unit/issues"
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
    "autoload-dev": {
        "classmap": [
            "tests/_fixture"
        ],
        "files": [
            "tests/_fixture/file_with_multiple_code_units.php",
            "tests/_fixture/function.php"
        ]
    },
    "extra": {
        "branch-alias": {
            "dev-main": "2.0-dev"
        }
    }
}
