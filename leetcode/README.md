# LeetCode / DSA

Coding practice in Python, organized by topic. Each problem is a **solution
file** plus a **test file** that lives right next to it.

## Workflow

1. **Scaffold** the files:
   ```bash
   make new TOPIC=arrays_hashing NAME=two_sum
   # ...or with metadata (recommended):
   python3 tools/new_problem.py arrays_hashing two_sum \
       --number 1 --title "Two Sum" --method twoSum \
       --url https://leetcode.com/problems/two-sum/
   ```
2. **Write tests first** from the problem's examples (the scaffolded test starts
   red on purpose, to drive a TDD loop).
3. **Implement** until the tests pass:
   ```bash
   pytest leetcode/arrays_hashing/test_two_sum.py
   ```
4. **Document** the approach + complexity in the solution docstring while it's
   fresh — that's what you'll re-read before an interview.

## Topics

Folders follow the NeetCode-150 roadmap order:

| | | |
|---|---|---|
| `arrays_hashing` | `two_pointers` | `sliding_window` |
| `stack` | `binary_search` | `linked_list` |
| `trees` | `tries` | `heap_priority_queue` |
| `backtracking` | `graphs` | `advanced_graphs` |
| `dp_1d` | `dp_2d` | `greedy` |
| `intervals` | `math_geometry` | `bit_manipulation` |

Add a new topic by creating a folder with an empty `__init__.py`.

## Conventions

- Files are `snake_case`, named after the problem (e.g. `two_sum.py`). The
  problem **number lives in the docstring, not the filename**, so every module
  imports cleanly.
- Keep the `Solution` class and method name matching the LeetCode editor
  (e.g. `twoSum`) so the body is drop-in. Tests call that method.
- Tests import by full path: `from leetcode.<topic>.<name> import Solution`.

## Worked example

A complete, passing example to copy the pattern from:
[`arrays_hashing/two_sum.py`](arrays_hashing/two_sum.py) +
[`arrays_hashing/test_two_sum.py`](arrays_hashing/test_two_sum.py).
