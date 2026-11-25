# Practice Projects

Small, end-to-end builds to practice design, testing, and shipping — one folder
per project, each self-contained.

## Convention
- One folder per project: `projects/<project_name>/`.
- Each project owns its own `README.md` (what, why, how to run) and its own
  dependencies / environment, kept isolated so projects don't interfere.
- Capture the goal and what you learned in the project's README.

## Starting a project
```bash
mkdir -p projects/my_project
cd projects/my_project
# add a README, set up a venv / package manager for that stack, and build.
```

## Ideas
- A small REST API (CRUD + auth) with tests.
- A CLI tool (argparse / click) with proper packaging.
- A rate limiter or LRU cache library.
- A mini key-value store or URL shortener (pairs well with the system-design notes).
- A web scraper + small data pipeline.
- A toy version of something you use daily (a job queue, a router, a templating engine).
