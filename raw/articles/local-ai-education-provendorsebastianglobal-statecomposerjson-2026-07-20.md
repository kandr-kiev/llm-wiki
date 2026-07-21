---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/global-state/composer.json
ingested: 2026-07-20
sha256: 11dd2a43169203ff05844932bf04eca78eedb8e4b3be071146123bf19a5c6cf3
blog_source: local:unknown
---
{
    "name": "sebastian/global-state",
    "description": "Snapshotting of global state",
    "keywords": ["global state"],
    "homepage": "https://www.github.com/sebastianbergmann/global-state",
    "license": "BSD-3-Clause",
    "authors": [
        {
            "name": "Sebastian Bergmann",
            "email": "sebastian@phpunit.de"
        }
    ],
    "support": {
        "issues": "https://github.com/sebastianbergmann/global-state/issues",
        "security": "https://github.com/sebastianbergmann/global-state/security/policy"
    },
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
        "ext-dom": "*",
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
        ],
        "files": [
            "tests/_fixture/SnapshotFunctions.php"
        ]
    },
    "extra": {
        "branch-alias": {
            "dev-main": "6.0-dev"
        }
    }
}
