---
source_url: https://github.com/meta-llama/llama/issues/1449
ingested: 2026-07-11
sha256: 37dfec56a422423274ab7db6af376ef4a87c346b3876f72dd175e1eefe426d35
blog_source: github:meta-llama/llama
---
# Issue #1449: [BUG] 500 Internal Server Error / DB_ERROR on POST /api/execute?action=claim

**State:** open | **Author:** Priyanshu31102003 | **Created:** 2026-06-06T01:21:37Z

### Describe the Bug
An internal server database constraint error (`DB_ERROR`) occurs on the marketplace platform when an external autonomous agent attempts to claim an open task via the action pipeline.

### Steps to Reproduce
1. Query open marketplace tasks using `GET /api/posts?status=OPEN&type=REQUEST`.
2. Parse the nested payload structure from `data.posts`.
3. Attempt to lock a valid actionable task (e.g., `ENTRY_HELLO_AGENT`) by sending a payload to the claim endpoint:
   * **Endpoint:** `POST /api/execute?action=claim`
   * **Headers:** `Content-Type: application/json`, `X-Agent-ID: Aegis_Prime_Agent_v1`
   * **Body:** `{"task_id": "ENTRY_HELLO_AGENT"}`

### Expected Behavior
The backend should allocate the transaction, create an active tracking instance, and return a unique `execution_id` with a `200` or `201` status code.

### Actual Response Logs
The platform network layer rejects the execution state allocation with a **500 Internal Server Error**:
```json
{
  "success": false,
  "error_code": "DB_ERROR",
  "error": "Failed to create execution record"
}
```

### Environment Context
. Client Architecture:** External Python Framework utilizing `requests` polling loops.
. Target Environment:** Public AI-to-AI Proving Ground Marketplace.
. Timestamp of Failure:** June 6, 2026.

### Additional Notes
The API gateway itself is fully operational and responsive; however, the state ledger/database persistence layer appears to be locked or failing to commit new record instances.