---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/environment/composer.json
ingested: 2026-07-20
sha256: ecb64ff225c75eeb2defa57eb7203b088477da6c59b2c7587d1a870b1deb84fc
blog_source: local:unknown
---
{
    "name": "sebastian/environment",
    "description": "Provides functionality to handle HHVM/PHP environments",
    "keywords": ["environment","hhvm","xdebug"],
    "homepage": "https://github.com/sebastianbergmann/environment",
    "license": "BSD-3-Clause",
    "authors": [
        {
            "name": "Sebastian Bergmann",
            "email": "sebastian@phpunit.de"
        }
    ],
    "support": {
        "issues": "https://github.com/sebastianbergmann/environment/issues",
        "security": "https://github.com/sebastianbergmann/environment/security/policy"
    },
    "config": {
        "platform": {
            "php": "8.1.0"
        },
        "optimize-autoloader": true,
        "sort-packages": true
    },
    "prefer-stable": true,
    "require": {
        "php": ">=8.1"
    },
    "require-dev": {
        "phpunit/phpunit": "^10.0"
    },
    "suggest": {
        "ext-posix": "*"
    },
    "autoload": {
        "classmap": [
            "src/"
        ]
    },
    "extra": {
        "branch-alias": {
            "dev-main": "6.1-dev"
        }
    }
}
