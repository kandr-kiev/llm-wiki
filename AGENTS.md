# Local LLM Wiki — Agent Contract

## Mission
Maintain `/workspace/llm-wiki` as a persistent, markdown-first, agent-readable knowledge base for LLM systems, automation patterns, and local business-process intelligence.

## Mandatory Orientation
Before writing or answering:
1. Read `SCHEMA.md` (root — tag taxonomy & conventions).
2. Read `wiki/index.md` (wiki page index).
3. Read recent `log.md` (root — action log).
4. Search for existing relevant pages.

## Ground Truth
- `raw/` wins over `wiki/`.
- `wiki/` is synthesis and may be stale.
- Never edit raw sources after ingest.

## Operations

### ingest
Capture raw source, write to `raw/`, update concepts/entities/comparisons, update index, append log, run lint.

### query
Answer from `wiki/` first, then `raw/` if needed. File valuable synthesis into `wiki/queries/` or `wiki/comparisons/`.

### lint
Run `python3 tools/wiki_lint.py` from `/workspace/llm-wiki` or inspect manually if Python is unavailable. Fix structural problems only when explicitly asked.

## Page Rules
- Every wiki page has YAML frontmatter matching `SCHEMA.md`.
- Every wiki page appears in `index.md`.
- Every material action appends to `log.md`.
- Cross-link concepts with `[[slug]]`.
- Use approved tags from `SCHEMA.md` only.

## Graph-First Query Protocol (MANDATORY)

Before answering ANY knowledge question, you MUST use the knowledge graph as the primary discovery layer. Only fall back to direct wiki/ reading or LLM when the graph provides no relevant results.

### Algorithm: graph → wiki → synthesis

1. **Load graph:** `python3 -c "import json; g=json.load(open('graphify-out/graph.json'))"` — get nodes, edges, communities
2. **Seed BFS:** Find the most relevant node(s) for the query topic → BFS(depth=2) to discover connected pages
3. **Community filter:** If node has a community, prioritize pages from that community
4. **Content load:** Read only the top-5 wiki pages from BFS results: `wiki/{slug}.md`
5. **Synthesize:** Answer from the loaded pages. If graph returned 0 results → read wiki/index.md, search by keyword
6. **Report structure:** When returning an answer, mention the graph path used: "discovered via graph BFS from {seed} → {n} connected pages"

### Why graph-first?

- **Graph** gives structure: which pages are related, community membership, bridge nodes
- **Wiki** gives content: actual text, analysis, context
- **Graph-first** prevents reading irrelevant pages and ensures comprehensive coverage
- **BFS depth 2** covers 80% of relevant context without noise

### Quick graph queries

```python
# BFS from seed
import json
g = json.load(open('graphify-out/graph.json'))
def bfs(seed, depth=2):
    visited = {seed}; queue = [(seed, 0)]; result = []
    while queue:
        node, d = queue.pop(0)
        if d > depth: continue
        result.append(node)
        for e in g['edges']:
            if e['source'] == node and e['target'] not in visited:
                visited.add(e['target']); queue.append((e['target'], d+1))
            elif e['target'] == node and e['source'] not in visited:
                visited.add(e['source']); queue.append((e['source'], d+1))
    return result

# God nodes (most linked)
top = sorted(g['nodes'], key=lambda n: n.get('inbound',0), reverse=True)[:5]

# Orphans (0 inbound, 0 outbound)
orphans = [n for n in g['nodes'] if n.get('inbound',0)==0 and n.get('outbound',0)==0]

# Community by tag
comm = [n for n in g['nodes'] if 'llm' in n.get('tags',[])]
```

### Graph maintenance (cron jobs)

- **Every 6h** (`graphify-scan`): Run `wiki_graph_generator.py` → `graphify_bridge.py --auto-fix`
- **Weekly** (`llm-wiki graphify weekly scan`): Full gap analysis + orphan report

### Graphify CLI (advanced)

- `graphify query "question" --graph graphify-out/graph.json` — BFS traversal
- `graphify path "A" "B" --graph graphify-out/graph.json` — shortest path
- `graphify explain "X" --graph graphify-out/graph.json` — node + neighbors
- `graphify watch wiki/` — auto-rebuild on changes

## Claude Code Handoff
When asked to implement:
1. Treat `docs/ARCHITECTURE.md` and `docs/ALGORITHM.md` as the software requirements.
2. Modify only files inside `/workspace/llm-wiki` unless explicitly instructed.
3. Do not read secrets or config files outside the workspace.
4. Verify with lint before reporting success.

