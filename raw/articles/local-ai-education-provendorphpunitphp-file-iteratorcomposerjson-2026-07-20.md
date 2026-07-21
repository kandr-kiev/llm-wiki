---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phpunit/php-file-iterator/composer.json
ingested: 2026-07-20
sha256: ef5eb6acc21c577c63025625600631e55b1446e38062d1b9ea66b394864dd66b
blog_source: local:unknown
---
{
    "name": "phpunit/php-file-iterator",
    "description": "FilterIterator implementation that filters files based on a list of suffixes.",
    "type": "library",
    "keywords": [
        "iterator",
        "filesystem"
    ],
    "homepage": "https://github.com/sebastianbergmann/php-file-iterator/",
    "license": "BSD-3-Clause",
    "authors": [
        {
            "name": "Sebastian Bergmann",
            "email": "sebastian@phpunit.de",
            "role": "lead"
        }
    ],
    "support": {
        "issues": "https://github.com/sebastianbergmann/php-file-iterator/issues",
        "security": "https://github.com/sebastianbergmann/php-file-iterator/security/policy"
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
            "dev-main": "4.0-dev"
        }
    }
}
