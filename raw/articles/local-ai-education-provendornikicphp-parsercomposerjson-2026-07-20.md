---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/nikic/php-parser/composer.json
ingested: 2026-07-20
sha256: d6fc40435ab054de4723b51e6dd3c81fd5315e3e942d1440ef5621028c37a89d
blog_source: local:unknown
---
{
    "name": "nikic/php-parser",
    "type": "library",
    "description": "A PHP parser written in PHP",
    "keywords": [
        "php",
        "parser"
    ],
    "license": "BSD-3-Clause",
    "authors": [
        {
            "name": "Nikita Popov"
        }
    ],
    "require": {
        "php": ">=7.4",
        "ext-tokenizer": "*",
        "ext-json": "*",
        "ext-ctype": "*"
    },
    "require-dev": {
        "phpunit/phpunit": "^9.0",
        "ircmaxell/php-yacc": "^0.0.7"
    },
    "extra": {
        "branch-alias": {
            "dev-master": "5.x-dev"
        }
    },
    "autoload": {
        "psr-4": {
            "PhpParser\\": "lib/PhpParser"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "PhpParser\\": "test/PhpParser/"
        }
    },
    "bin": [
        "bin/php-parse"
    ]
}
