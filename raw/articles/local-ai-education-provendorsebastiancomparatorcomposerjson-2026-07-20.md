---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/comparator/composer.json
ingested: 2026-07-20
sha256: 58e1b061966aa7617ece4872b8272bd0acf5db9ab25b6bf7f87f2093a16b184f
blog_source: local:unknown
---
{
    "name": "sebastian/comparator",
    "description": "Provides the functionality to compare PHP values for equality",
    "keywords": ["comparator","compare","equality"],
    "homepage": "https://github.com/sebastianbergmann/comparator",
    "license": "BSD-3-Clause",
    "authors": [
        {
            "name": "Sebastian Bergmann",
            "email": "sebastian@phpunit.de"
        },
        {
            "name": "Jeff Welch",
            "email": "whatthejeff@gmail.com"
        },
        {
            "name": "Volker Dusch",
            "email": "github@wallbash.com"
        },
        {
            "name": "Bernhard Schussek",
            "email": "bschussek@2bepublished.at"
        }
    ],
    "support": {
        "issues": "https://github.com/sebastianbergmann/comparator/issues",
        "security": "https://github.com/sebastianbergmann/comparator/security/policy"
    },
    "prefer-stable": true,
    "require": {
        "php": ">=8.1",
        "sebastian/diff": "^5.0",
        "sebastian/exporter": "^5.0",
        "ext-dom": "*",
        "ext-mbstring": "*"
    },
    "require-dev": {
        "phpunit/phpunit": "^10.5"
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
        ]
    },
    "extra": {
        "branch-alias": {
            "dev-main": "5.0-dev"
        }
    }
}

