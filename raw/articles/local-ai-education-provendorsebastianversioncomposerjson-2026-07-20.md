---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/version/composer.json
ingested: 2026-07-20
sha256: 489c960758533f3273e4c6d2e036c2be0e3f57dbc1f9e7b14766d6f86279b6ee
blog_source: local:unknown
---
{
    "name": "sebastian/version",
    "description": "Library that helps with managing the version number of Git-hosted PHP projects",
    "homepage": "https://github.com/sebastianbergmann/version",
    "license": "BSD-3-Clause",
    "authors": [
        {
            "name": "Sebastian Bergmann",
            "email": "sebastian@phpunit.de",
            "role": "lead"
        }
    ],
    "support": {
        "issues": "https://github.com/sebastianbergmann/version/issues"
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
