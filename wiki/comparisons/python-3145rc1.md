---
title: "python 3145rc1"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - async
  - data
  - image-generation
  - open-source
  - search
  - self-supervised
---

# python 3145rc1

> **Source:** python-3145-release-candidate-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://blog.python.org/2026/05/python-3145rc1/ ingested: 2026-07-17 sha256: 2b19dbaad20fda31655fb3da8ac8722aa4805ec8a8b8531015a9a5bb764597f6 blog_source: Python Insider --- - - - - -...
> **Sources:**
>   - python-3145-release-candidate-2026-07-17.md
> **Links:**
- [[python 3145 is out]]
- [Issue #8330: Dataset Studio and Viewer down](https://github.com/pytorch/pytorch/issues/8330)
- [[Release 5.0.0]]
- [[Release v0.25.1]]
- [[improving accessibility in jetbrains ides what s new and what s next]]

## Key Findings

---
source_url: https://blog.python.org/2026/05/python-3145rc1/
ingested: 2026-07-17
sha256: 2b19dbaad20fda31655fb3da8ac8722aa4805ec8a8b8531015a9a5bb764597f6
blog_source: Python Insider
---
- - - - - - - Python 3.14.5 release candidate | Python Insider- [ - - 
Python Insider
](/) [ Home ](/)[ Blog ](/blog) - Search ⌘K [ ](/rss.xml) # Python 3.14.5 release candidate 
[Hugo van Kemenade](/authors/hugo-van-kemenade) / May 4, 2026 [ releases ](/tags/releases) Python 3.14.5rc1 is a release candidate for the fifth maintenance release of 3.14, containing around 113 bugfixes, build improvements and documentation changes since 3.14.4.
[- python.org/downloads/release/python-3145rc1](https://www.python.org/downloads/release/python-3145rc1/)
## Garbage collector
Notably, the garbage collector (GC) has changed in Python 3.14.5rc1.
The incremental garbage collector shipped in Python 3.14.0-3.14.4 has been reverted back to the generational garbage collector from 3.13, due to a number of [reports](https://github.com/python/cpython/issues/142516) of significant memory pressure in production environments. See [What’s New](https://docs.python.org/3/whatsnew/3.14.html#garbage-collection) and [discuss.python.org](https://discuss.python.org/t/reverting-the-incremental-gc-in-python-3-14-and-3-15/107014) for details.
## Call to action
We ***strongly encourage*** testing of this release candidate, ahead of the planned 3.14.5 final on Friday 2026-05-08.
As always, report any issues to [the Python bug tracker](https://github.com/python/cpython/issues).
Please keep in mind that this is a preview release and its use is ***not*** recommended for production environments.
## Major new features of the 3.14 series, compared to 3.13
Some of the major new features and changes in Python 3.14 are:
### New features
- [PEP 779](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-free-threaded-now-supported): Free-threaded Python is officially supported
- [PEP 649](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-deferred-annotations): The evaluation of annotations is now deferred, improving the semantics of using annotations.
- [PEP 750](https://docs.python.org/3/whatsnew/3.14.html#pep-750-template-string-literals): Template string literals (t-strings) for custom string processing, using the familiar syntax of f-strings.
- [PEP 734](https://docs.python.org/3/whatsnew/3.14.html#pep-734-multiple-interpreters-in-the-standard-library): Multiple interpreters in the stdlib.
- [PEP 784](https://docs.python.org/3/whatsnew/3.14.html#pep-784-zstandard-support-in-the-standard-library): A new module `compression.zstd` providing support for the Zstandard compression algorithm.
- [PEP 758](https://docs.python.org/3/whatsnew/3.14.html#pep-758-allow-except-and-except-expressions-without-brackets): `except` and `except*` expressions may now omit the brackets.
- [Syntax highlighting in PyREPL](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-pyrepl-highlighting), and support for col

## Summary

or in [unittest](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-color-unittest), [argparse](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-color-argparse), [json](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-color-json) and [calendar](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-color-calendar) CLIs.
- [PEP 768](https://docs.python.org/3/whatsnew/3.14.html#pep-768-safe-external-debugger-interface): A zero-overhead external debugger interface for CPython.
- [UUID versions 6-8](https://docs.python.org/3/whatsnew/3.14.html#uuid) are now supported by the `uuid` module, and generation of versions 3-5 are up to 40% faster.
- [PEP 765](https://docs.python.org/3/whatsnew/3.14.html#pep-765-control-flow-in-finally-blocks): Disallow `return`/`break`/`continue` that exit a `finally` block.
- [PEP 741](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-capi-config): An improved C API for configuring Python.
- A [new type of interpreter](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-tail-call-interpreter). For certain newer compilers, this interpreter provides significantly better performance. Opt-in for now, requires building from source.
- [Improved error messages.](https://docs.python.org/3/whatsnew/3.14.html#improved-error-messages)
- [Builtin implementation of HMAC](https://docs.python.org/3/whatsnew/3.14.html#hmac) with formally verified code from the HACL* project.
- A [new command-line interface](https://docs.python.org/3/whatsnew/3.14.html#asyncio-introspection-capabilities) to inspect running Python processes using asynchronous tasks.
- The pdb module now supports [remote attaching to a running Python process](https://docs.python.org/3/whatsnew/3.14.html#pdb).
For more details on the changes to Python 3.14, see [What’s new in Python 3.14](https://docs.python.org/3/whatsnew/3.14.html).
### Build changes
- [PEP 761](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-no-more-pgp): Python 3.14 and onwards no longer provides PGP signatures for release artifacts. Instead, Sigstore is recommended for verifiers.
- Official macOS and Windows release binaries include an [experimental JIT compiler](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-jit-compiler).
- Official [Android binary releases](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-build-changes) are now available.
### Incompatible changes, removals and new deprecations
- [Incompatible changes](https://docs.python.org/3/whatsnew/3.14.html#incompatible-changes)
- Python [removals](https://docs.python.org/3/whatsnew/3.14.html#removed) and [deprecations](https://docs.python.org/3/whatsnew/3.14.html#deprecated)
- C API [removals](https://docs.python.org/3/whatsnew/3.14.html#removed-c-apis) and [deprecations](https://docs.python.org/3/whatsnew/3.14.html#deprecated-c-apis)
- Overview of all [pending deprecations](https://docs.python.org/3/deprecations/index.html)
## Python install manager
The installer we offer for Window

##[Issue #8330: Dataset Studio and Viewer down](https://github.com/pytorch/pytorch/issues/8330)[Issue #8330: Dataset Studio and Viewer down]]
- [[Release 5.0.0]]
- [[Release v0.25.1]]
- [[improving accessibility in jetbrains ides what s new and what s next]]
