---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phar-io/manifest/composer.json
ingested: 2026-07-20
sha256: da39b5853bcbf7f493d386a9a92e716d91c8d8f82c45882709dd5e76326a9c33
blog_source: local:unknown
---
{
  "name": "phar-io/manifest",
  "description": "Component for reading phar.io manifest information from a PHP Archive (PHAR)",
  "license": "BSD-3-Clause",
  "authors": [
    {
      "name": "Arne Blankerts",
      "email": "arne@blankerts.de",
      "role": "Developer"
    },
    {
      "name": "Sebastian Heuer",
      "email": "sebastian@phpeople.de",
      "role": "Developer"
    },
    {
      "name": "Sebastian Bergmann",
      "email": "sebastian@phpunit.de",
      "role": "Developer"
    }
  ],
  "support": {
    "issues": "https://github.com/phar-io/manifest/issues"
  },
  "require": {
    "php": "^7.2 || ^8.0",
    "ext-dom": "*",
    "ext-phar": "*",
    "ext-libxml": "*",
    "ext-xmlwriter": "*",
    "phar-io/version": "^3.0.1"
  },
  "autoload": {
    "classmap": [
      "src/"
    ]
  },
  "extra": {
    "branch-alias": {
        "dev-master": "2.0.x-dev"
    }
  }
}
