---
source_url: https://github.com/langchain-ai/langchain/releases/tag/langchain-core==1.4.9
ingested: 2026-07-14
sha256: d20b8ca51af0b6c0252bf939dbb3040739896c54706f66c23bca96863ffa6d71
blog_source: github:langchain-ai/langchain
---
# Release langchain-core==1.4.9

Changes since langchain-core==1.4.8

release(core): 1.4.9 (#38728)
fix(core): improve langsmith loader error messages (#35648)
fix(core): output parser bugs in xml.py and pydantic.py (#35641)
style(core): fix some ruff preview rules (#38656)
fix(core): avoid `dict` shadowing in language models (#38480)
fix(core): `_parse_google_docstring` mishandling continuation lines with colons (#35680)
fix(core): add messages to bare `raise ValueError` calls (#38158)
fix(core): use `asyncio.get_running_loop()` in async contexts (#38157)
chore: bump langsmith from 0.8.0 to 0.8.18 in /libs/core (#38319)
chore: bump jupyterlab from 4.5.7 to 4.5.9 in /libs/core (#38326)
chore: bump vcrpy from 8.1.1 to 8.2.1 in /libs/core (#38327)