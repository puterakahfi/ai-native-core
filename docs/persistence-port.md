# PersistencePort

## Purpose

`PersistencePort` defines the boundary for storing, querying, and managing structured runtime state for Native AI Framework products and workflows.

It exists so the framework can use databases, cache systems, vector stores, search indexes, and durable state stores without coupling the domain model to a specific database vendor, schema, ORM, or hosting provider.

## Position in the Framework

```text
Domain / Application Logic
→ RepositoryPort / PersistencePort
→ Persistence Adapter
→ Database / Cache / Search / Vector Store / Object Store
```

`PersistencePort` sits between application/domain logic and runtime data storage.

It is not a task management layer, code execution layer, UI design layer, creative rendering layer, or tool integration layer.

## Primary Responsibilities

- Store and query structured runtime data.
- Preserve domain boundaries through repositories or persistence ports.
- Support transactions when required.
- Support migrations and schema evolution.
- Return structured persistence errors.
- Keep secrets and database credentials server-side only.
- Support auditability when storing execution runs, approvals, and workflow events.

## Non-Responsibilities

`PersistencePort` must not:

- define the domain model,
- replace GitHub Project as task source unless explicitly approved,
- execute code tasks,
- render UI or creative outputs,
- store large binary assets when an object storage port is more appropriate,
- bypass repository or domain boundaries,
- mutate production data without approval policy.

## Subtype Ports

```text
PersistencePort
├── RelationalDatabasePort
├── DocumentDatabasePort
├── VectorDatabasePort
├── CachePort
├── SearchIndexPort
└── ObjectStoragePort
```

### RelationalDatabasePort

Used for structured relational data, transactional records, dashboard runtime settings, workflow state, execution runs, approvals, and audit logs.

Example adapters:

```text
PostgreSQLAdapter
MySQLAdapter
SQLiteAdapter
SupabasePostgresAdapter
NeonPostgresAdapter
```

### DocumentDatabasePort

Used for flexible document-style records, dynamic configuration snapshots, event payloads, and semi-structured data.

Example adapters:

```text
MongoDBAdapter
FirestoreAdapter
DynamoDBAdapter
```

### VectorDatabasePort

Used for embeddings, semantic search, long-term memory retrieval, knowledge indexing, and similarity search.

Example adapters:

```text
PgVectorAdapter
PineconeAdapter
QdrantAdapter
WeaviateAdapter
ChromaAdapter
```

### CachePort

Used for short-lived runtime cache, rate limit state, session-adjacent state, queue coordination, and frequently accessed computed data.

Example adapters:

```text
RedisAdapter
UpstashRedisAdapter
ValkeyAdapter
```

### SearchIndexPort

Used for fast text search, filtering, faceted search, and index-backed discovery.

Example adapters:

```text
MeilisearchAdapter
TypesenseAdapter
ElasticsearchAdapter
OpenSearchAdapter
```

### ObjectStoragePort

Used for durable file and asset storage such as images, videos, exports, documents, and generated creative artifacts.

Example adapters:

```text
S3Adapter
CloudflareR2Adapter
GCSAdapter
LocalFileStorageAdapter
```

## Adapter Lifecycle

```text
candidate
→ allowed
→ active
→ deprecated
→ retired
```

- `candidate`: adapter is documented but not yet used as a default workflow component.
- `allowed`: adapter may be used in approved workflows.
- `active`: adapter is the default implementation for a port in a product/app workflow.
- `deprecated`: adapter should be replaced but may still exist for compatibility.
- `retired`: adapter should not be used.

## Default Persistence Workflow

```text
Application Request
→ Repository / Persistence Port
→ Adapter Policy Check
→ Query / Transaction
→ Result Normalization
→ Error Handling
→ Audit Event When Needed
→ Application Response
```

## Data Ownership Rule

The domain model owns business meaning.

The database schema stores persistence representation.

Adapters must not let database schema become the source of truth for domain behavior.

## Source of Truth Rule

For early Native AI Framework dashboard MVP, source of truth remains:

```text
products/**/*.yaml
adapters/**/*.yaml
skills/**/*.md
docs/**/*.md
GitHub Project #9
```

Database adapters should be introduced as runtime state stores, caches, audit stores, or product data stores only when needed.

They must not replace GitHub Project as the task management source unless explicitly approved.

## Candidate Runtime Data

Data that may eventually belong in a persistence adapter:

- execution runs,
- review records,
- approval decisions,
- audit logs,
- workflow events,
- dashboard user settings,
- adapter health snapshots,
- product registry cache,
- task registry cache,
- agent memory indexes,
- evaluation results.

## Input Contract

A persistence request should provide:

```yaml
persistence_input:
  data_model: ""
  operation: ""
  query_request: {}
  transaction_policy: ""
  product: ""
  workflow: ""
  approval_policy: ""
```

## Output Contract

A persistence adapter should return:

```yaml
persistence_output:
  query_result: {}
  transaction_metadata: {}
  audit_log: []
  error_details: null
```

## Quality Gates

Persistence adapters should be checked for:

- domain boundary protection,
- migration strategy,
- structured error handling,
- least-privilege credential use,
- server-side secret handling,
- transaction safety,
- data retention policy,
- backup and restore expectations,
- production mutation approval policy,
- observability and auditability.

## Example Adapter Placement

```text
adapters/persistence/postgresql.adapter.yaml
```

`PostgreSQLAdapter` is a candidate adapter for `PersistencePort` with subtype `RelationalDatabasePort`.

It should be used for structured runtime data such as execution runs, review records, workflow state, audit logs, and dashboard settings.
