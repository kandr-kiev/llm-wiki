---
source_url: https://github.com/huggingface/accelerate/issues/4115
ingested: 2026-07-14
sha256: 9371bf9c8b090ab4b957c5f3c6394651013b06ef4c8230514481f1989889624f
blog_source: github:huggingface/accelerate
---
# Issue #4115: Fix environment conversion docstring example

**State:** open | **Author:** cupkk | **Created:** 2026-07-13T23:10:07Z

The `convert_dict_to_env_variables` example currently imports and calls `verify_env`, which is not defined in the module. Update the snippet to use the function it documents so it can be copied and run as written.

```console
$ pytest tests/test_utils.py -k convert_dict_to_env_variables -q
1 passed, 48 deselected
```

`make quality` passes with the project's pinned Ruff version.
