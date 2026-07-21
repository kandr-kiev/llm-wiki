---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/sebastian/recursion-context/composer.json
ingested: 2026-07-20
sha256: b9cb836ab664ae1123871161ec7ebadefdec2fea74a3a55b48df38167e99274a
blog_source: local:unknown
---
{
    "name": "sebastian/recursion-context",
    "description": "Provides functionality to recursively process PHP variables",
    "homepage": "https://github.com/sebastianbergmann/recursion-context",
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
            "name": "Adam Harvey",
            "email": "aharvey@php.net"
        }
    ],
    "support": {
        "issues": "https://github.com/sebastianbergmann/recursion-context/issues",
        "security": "https://github.com/sebastianbergmann/recursion-context/security/policy"
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
        "php": ">=8.1"
    },
    "require-dev": {
        "phpunit/phpunit": "^10.5"
    },
    "autoload": {
        "classmap": [
            "src/"
        ]
    },
    "extra": {
        "branch-alias": {
            "dev-main": "5.0-dev"
        }
    }
}
