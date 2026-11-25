# URL Shortener (e.g. TinyURL / bit.ly)

> Prompt: "Design a URL shortener."  Timebox: ~45 min.
> (Worked example showing the template filled in.)

## 1. Requirements

### Functional
- [x] Create a short link for a long URL.
- [x] Redirect a short link to the original URL.
- [x] Optional custom alias and expiration.

### Non-functional
- High availability — redirects must "always" work.
- Redirect latency < ~50 ms.
- Read-heavy: ~100 : 1 reads : writes.

### Out of scope
- Auth, analytics dashboards, spam detection (mention, don't design).

## 2. Scale & estimations
- 100M new URLs/month ≈ 40 writes/s; ~4,000 redirects/s at peak.
- 5 years ≈ 6B URLs. At ~500 bytes/row ≈ 3 TB.
- Short code: base62, 7 chars → 62⁷ ≈ 3.5T combinations (plenty of headroom).

## 3. API
```
POST /urls        { "long_url", "alias?", "ttl?" }  ->  { "short_url" }
GET  /{code}      ->  301/302 redirect to long_url
```

## 4. Data model
- `urls(code PK, long_url, created_at, expires_at, owner_id?)`.
- Access pattern is a point lookup by `code` → KV store or indexed RDBMS.
- Choice: start with Postgres (simple, transactional) + a cache; move hot reads
  to a KV store (DynamoDB/Redis) if the load demands it.

## 5. High-level design
Client → CDN / LB → API service.
- **Write path:** generate code → persist → return short URL.
- **Read path:** look up code in cache (Redis) → fall back to DB → redirect.

## 6. Deep dives
- **Code generation:** (a) random base62 + collision check, or (b) a counter /
  ticket server (Snowflake-style ID) base62-encoded for uniqueness without
  collision checks. Trade-off: randomness vs coordination.
- **Caching:** cache-aside on `code → long_url`; redirects are highly cacheable
  and CDN-friendly. Use 301 for max cacheability, 302 if you need to change
  targets or measure clicks.

## 7. Bottlenecks & trade-offs
- Hot links → lean on CDN + cache; the DB only sees misses.
- A single global counter is a SPOF → range-allocate ID blocks per server.
- Custom aliases need a uniqueness check (conditional insert).

## 8. Summary
A read-heavy KV problem: generate a unique base62 code, store `code → URL`, and
serve redirects from cache/CDN with the database as the source of truth.
