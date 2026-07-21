---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/object-reflector/composer.json
ingested: 2026-07-20
sha256: 45e841aed6891c0cb1ed8c7c7fb509eb0ed29c2f3902de37778ade859dd645ce
blog_source: local:unknown
---
{
    "name": "sebastian/object-reflector",
    "description": "Allows reflection of object attributes, including inherited and non-public ones",
    "homepage": "https://github.com/sebastianbergmann/object-reflector/",
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
    "autoload-dev": {
        "classmap": [
            "tests/_fixture/"
        ]
    },
    "extra": {
        "branch-alias": {
            "dev-main": "3.0-dev"
        }
    }
}
