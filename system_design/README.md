# System Design

Notes, a reusable design-doc template, and worked case studies.

## How to practice

Pick a prompt, copy [`template.md`](template.md) into `case_studies/`, and
timebox yourself to ~45 minutes. Drive the discussion through this framework:

1. **Requirements** — functional + non-functional; clarify scope and scale.
2. **Estimations** — QPS, storage, bandwidth (back-of-envelope).
3. **API design** — the core endpoints / interfaces.
4. **Data model** — entities, access patterns, SQL vs NoSQL.
5. **High-level design** — boxes and arrows; the happy path first.
6. **Deep dives** — the 1–2 genuinely hard parts (consistency, hot keys, fan-out…).
7. **Bottlenecks & trade-offs** — what breaks at 10x, and how you'd evolve it.

## Contents

- [`template.md`](template.md) — copy this to start a new design.
- [`fundamentals/`](fundamentals/) — concept notes (scaling, caching, DBs…).
- [`case_studies/`](case_studies/) — worked designs.
  - [`url_shortener.md`](case_studies/url_shortener.md) — example using the template.

## Suggested practice list

Easier → harder: URL shortener, Pastebin, rate limiter, Twitter/X timeline,
Instagram, chat (WhatsApp), news feed, YouTube, Google Drive/Dropbox, Uber,
ticket booking, web crawler, notification system, ad-click aggregator.
