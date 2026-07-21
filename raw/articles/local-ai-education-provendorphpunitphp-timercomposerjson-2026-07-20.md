---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phpunit/php-timer/composer.json
ingested: 2026-07-20
sha256: cfb1469765fbee27eec3e824b264f2fa1a4b11dbc0c6890e51ae93050a83d23f
blog_source: local:unknown
---
{
    "name": "phpunit/php-timer",
    "description": "Utility class for timing",
    "type": "library",
    "keywords": [
        "timer"
    ],
    "homepage": "https://github.com/sebastianbergmann/php-timer/",
    "license": "BSD-3-Clause",
    "authors": [
        {
            "name": "Sebastian Bergmann",
            "email": "sebastian@phpunit.de",
            "role": "lead"
        }
    ],
    "support": {
        "issues": "https://github.com/sebastianbergmann/php-timer/issues"
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
            "dev-main": "6.0-dev"
        }
    }
}

