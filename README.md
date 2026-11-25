# Interview practice

Coding problems, system design notes, behavioral prep and small practice builds in one place.

## Layout

| Folder | What lives here |
|--------|-----------------|
| [`Data Structures & Algorithms/`](Data%20Structures%20%26%20Algorithms/) | Solutions submitted on [NeetCode.io](https://neetcode.io), pushed here automatically by its GitHub Sync (`<problem>/submission-N.py`). Don't edit by hand. |
| [`leetcode/`](leetcode/) | Hand-written practice in Python, by topic, each problem with tests |
| [`system_design/`](system_design/) | A design-doc template, fundamentals notes and worked case studies |
| [`behavioral/`](behavioral/) | STAR template, a story bank and common questions |
| [`projects/`](projects/) | Small end-to-end practice builds, one folder each |
| [`tools/`](tools/) | Helper scripts, such as scaffolding a new problem |

## Quick start

```bash
# one-time: install dev dependencies (pytest)
make install                 # or: pip install -r requirements-dev.txt

# scaffold a new problem: creates the solution + test from templates
make new TOPIC=arrays_hashing NAME=two_sum
# ...or call the script directly for full options:
python3 tools/new_problem.py arrays_hashing two_sum \
    --number 1 --title "Two Sum" --url https://leetcode.com/problems/two-sum/

# run everything
make test                    # or: pytest

# run a single topic / file
pytest leetcode/arrays_hashing
pytest leetcode/arrays_hashing/test_two_sum.py
```

## How the `leetcode/` practice works

Each problem is **two files** in its topic folder:

```
leetcode/arrays_hashing/
├── two_sum.py            # the solution
└── test_two_sum.py       # the tests (also doubles as your scratch cases)
```

- Solutions expose a `Solution` class (matching LeetCode's editor) with the
  problem number, title, link, and a short approach + complexity note in the
  docstring.
- Tests import the solution by its full path:
  `from leetcode.arrays_hashing.two_sum import Solution`.
- The workflow: scaffold → write failing tests from the examples → make them
  pass → jot down the approach/complexity in the docstring.

See [`leetcode/README.md`](leetcode/README.md) for the topic list and the
recommended practice loop.

## NeetCode sync

NeetCode's GitHub Sync commits each submission into `Data Structures & Algorithms/`.
Its settings (auto-commit, accepted-only, bulk sync) live at
[neetcode.io/profile/github](https://neetcode.io/profile/github). If the repo is
ever renamed, update the target there too, or the sync stops.

## Conventions

- **Language:** Python 3.11+.
- **Naming:** `snake_case` files named after the problem (no leading digits, so
  they import cleanly); the problem number goes in the docstring.
