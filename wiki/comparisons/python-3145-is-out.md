---
title: "python 3145 is out"
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

# python 3145 is out

> **Source:** python-3145-is-out-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://blog.python.org/2026/05/python-3145-is-out/ ingested: 2026-07-17 sha256: 55bf8269c78c813ce2009835d70205f3051ab766e25e86bc7f36aa01d7576df3 blog_source: Python Insider --- - - -...
> **Sources:**
>   - python-3145-is-out-2026-07-17.md
> **Links:**
- [[Release 5.0.0]]
- [[Issue #8330: Dataset Studio and Viewer down]]
- [[v0.27.0]]
- [[Issue #8140: Add logging support for better observability]]
- [[Release v0.25.1]]

## Key Findings

---
source_url: https://blog.python.org/2026/05/python-3145-is-out/
ingested: 2026-07-17
sha256: 55bf8269c78c813ce2009835d70205f3051ab766e25e86bc7f36aa01d7576df3
blog_source: Python Insider
---
- - - - - - - Python 3.14.5 is out! | Python Insider- [ - - 
Python Insider
](/) [ Home ](/)[ Blog ](/blog) - Search ⌘K [ ](/rss.xml) # Python 3.14.5 is out! 
[Hugo van Kemenade](/authors/hugo-van-kemenade) / May 10, 2026 [ releases ](/tags/releases) Python 3.14.5 final is the fifth maintenance release of 3.14, containing around 154 bugfixes, build improvements and documentation changes since 3.14.4.
[- python.org/downloads/release/python-3145](https://www.python.org/downloads/release/python-3145/)
## Garbage collector
Notably, the garbage collector (GC) has changed in Python 3.14.5.
The incremental garbage collector shipped in Python 3.14.0-3.14.4 has been reverted back to the generational garbage collector from 3.13, due to a number of [reports](https://github.com/python/cpython/issues/142516) of significant memory pressure in production environments. See [What’s New](https://docs.python.org/3/whatsnew/3.14.html#garbage-collection) and [discuss.python.org](https://discuss.python.org/t/reverting-the-incremental-gc-in-python-3-14-and-3-15/107014) for details.
## Tcl/Tk 9 on macOS
The official macOS installer has been updated to use Tcl/Tk 9.0.3 instead of 8.6.17.
## Major new features of the 3.14 series, compared to 3.13
Some of the major new features and changes in Python 3.14 are:
### New features
- [PEP 779](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-free-threaded-now-supported): Free-threaded Python is officially supported
- [PEP 649](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-deferred-annotations): The evaluation of annotations is now deferred, improving the semantics of using annotations.
- [PEP 750](https://docs.python.org/3/whatsnew/3.14.html#pep-750-template-string-literals): Template string literals (t-strings) for custom string processing, using the familiar syntax of f-strings.
- [PEP 734](https://docs.python.org/3/whatsnew/3.14.html#pep-734-multiple-interpreters-in-the-standard-library): Multiple interpreters in the stdlib.
- [PEP 784](https://docs.python.org/3/whatsnew/3.14.html#pep-784-zstandard-support-in-the-standard-library): A new module `compression.zstd` providing support for the Zstandard compression algorithm.
- [PEP 758](https://docs.python.org/3/whatsnew/3.14.html#pep-758-allow-except-and-except-expressions-without-brackets): `except` and `except*` expressions may now omit the brackets.
- [Syntax highlighting in PyREPL](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-pyrepl-highlighting), and support for color in [unittest](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-color-unittest), [argparse](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-color-argparse), [json](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-color-json) and [calendar](https://docs.python.org/3/

## Summary

whatsnew/3.14.html#whatsnew314-color-calendar) CLIs.
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
### Removals and new deprecations
- Python [removals](https://docs.python.org/3/whatsnew/3.14.html#removed) and [deprecations](https://docs.python.org/3/whatsnew/3.14.html#deprecated)
- C API [removals](https://docs.python.org/3/whatsnew/3.14.html#removed-c-apis) and [deprecations](https://docs.python.org/3/whatsnew/3.14.html#deprecated-c-apis)
- Overview of all [pending removals](https://docs.python.org/3/deprecations/index.html)
## Python install manager
The installer we offer for Windows is being replaced by our new install manager, which can be installed from [the Windows Store](https://apps.microsoft.com/detail/9NQ7512CXL7T) or from its [download page](https://www.python.org/downloads/latest/pymanager/). See [our documentation](https://docs.python.org/3/using/windows.html) for more information. The JSON file available for download contains the list of all the installable packages availab

## Related Articles

- [[Release 5.0.0]]
- [[Issue #8330: Dataset Studio and Viewer down]]
- [[v0.27.0]]
- [[Issue #8140: Add logging support for better observability]]
- [[Release v0.25.1]]
