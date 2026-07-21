---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/object-enumerator/composer.json
ingested: 2026-07-20
sha256: f64a9f427b0a66b3751d8c222aefff6672b9e4756157909775de511d998052df
blog_source: local:unknown
---
{
    "name": "sebastian/object-enumerator",
    "description": "Traverses array structures and object graphs to enumerate all referenced objects",
    "homepage": "https://github.com/sebastianbergmann/object-enumerator/",
    "license": "BSD-3-Clause",
    "authors": [
        {
            "name": "Sebastian Bergmann",
            "email": "sebastian@phpunit.de"
        }
    ],
    "prefer-stable": true,
    "config": {
        "platform": {
            "php": "8.1.0"
        },
        "optimize-autoloader": true,
        "sort-packages": true
    },
    "require": {
        "php": ">=8.1",
        "sebastian/object-reflector": "^3.0",
        "sebastian/recursion-context": "^5.0"
    },
    "require-dev": {
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
    "extra": {
        "branch-alias": {
            "dev-main": "5.0-dev"
        }
    }
}
