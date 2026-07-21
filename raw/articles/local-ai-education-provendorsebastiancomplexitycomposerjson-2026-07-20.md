---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/complexity/composer.json
ingested: 2026-07-20
sha256: 2da61048c238d077eb79c717c2fa69ce5102592bcc85712d0334b7f569372614
blog_source: local:unknown
---
{
    "name": "sebastian/complexity",
    "description": "Library for calculating the complexity of PHP code units",
    "type": "library",
    "homepage": "https://github.com/sebastianbergmann/complexity",
    "license": "BSD-3-Clause",
    "authors": [
        {
            "name": "Sebastian Bergmann",
            "email": "sebastian@phpunit.de",
            "role": "lead"
        }
    ],
    "support": {
        "issues": "https://github.com/sebastianbergmann/complexity/issues",
        "security": "https://github.com/sebastianbergmann/complexity/security/policy"
    },
    "prefer-stable": true,
    "require": {
        "php": ">=8.1",
        "nikic/php-parser": "^4.18 || ^5.0"
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
            "dev-main": "3.2-dev"
        }
    }
}
