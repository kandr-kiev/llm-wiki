---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phpunit/php-text-template/composer.json
ingested: 2026-07-20
sha256: 471cd4d7087805aeba41ee4e557a2a293b834d126213c3e336503ed734db2125
blog_source: local:unknown
---
{
    "name": "phpunit/php-text-template",
    "description": "Simple template engine.",
    "type": "library",
    "keywords": [
        "template"
    ],
    "homepage": "https://github.com/sebastianbergmann/php-text-template/",
    "license": "BSD-3-Clause",
    "authors": [
        {
            "name": "Sebastian Bergmann",
            "email": "sebastian@phpunit.de",
            "role": "lead"
        }
    ],
    "support": {
        "issues": "https://github.com/sebastianbergmann/php-text-template/issues",
        "security": "https://github.com/sebastianbergmann/php-text-template/security/policy"
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
    "autoload": {
        "classmap": [
            "src/"
        ]
    },
    "extra": {
        "branch-alias": {
            "dev-main": "3.0-dev"
        }
    }
}
