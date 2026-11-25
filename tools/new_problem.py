#!/usr/bin/env python3
"""Scaffold a new LeetCode practice problem.

Creates a solution file and a matching test file inside the given topic
folder, filled in from the templates in ``leetcode/templates/``.

Examples
--------
    python3 tools/new_problem.py arrays_hashing two_sum
    python3 tools/new_problem.py trees max_depth \\
        --number 104 --title "Maximum Depth of Binary Tree" \\
        --url https://leetcode.com/problems/maximum-depth-of-binary-tree/ \\
        --difficulty Easy --method maxDepth
"""
from __future__ import annotations

import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE = REPO_ROOT / "leetcode"
TEMPLATES = LEETCODE / "templates"


def render(template: str, **fields: str) -> str:
    """Replace ``{{KEY}}`` tokens in *template* with the given field values."""
    out = template
    for key, value in fields.items():
        out = out.replace("{{" + key + "}}", value)
    return out


def available_topics() -> list[str]:
    return sorted(
        p.name
        for p in LEETCODE.iterdir()
        if p.is_dir() and p.name != "templates" and not p.name.startswith("__")
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("topic", help="topic folder, e.g. arrays_hashing")
    parser.add_argument("name", help="snake_case problem name, e.g. two_sum")
    parser.add_argument("--number", default="TODO", help="problem number")
    parser.add_argument("--title", default="TODO", help="human-readable title")
    parser.add_argument("--url", default="TODO", help="LeetCode URL")
    parser.add_argument("--difficulty", default="TODO", help="Easy / Medium / Hard")
    parser.add_argument(
        "--method",
        default="solve",
        help="method name matching the LeetCode signature (default: solve)",
    )
    parser.add_argument(
        "--force", action="store_true", help="overwrite files if they already exist"
    )
    args = parser.parse_args(argv)

    topic_dir = LEETCODE / args.topic
    if not topic_dir.is_dir():
        parser.error(
            f"unknown topic {args.topic!r}. Available: {', '.join(available_topics())}"
        )

    # Make sure the topic is an importable package.
    (topic_dir / "__init__.py").touch(exist_ok=True)

    solution_path = topic_dir / f"{args.name}.py"
    test_path = topic_dir / f"test_{args.name}.py"

    if not args.force:
        for path in (solution_path, test_path):
            if path.exists():
                parser.error(
                    f"{path.relative_to(REPO_ROOT)} already exists "
                    f"(use --force to overwrite)"
                )

    fields = {
        "NUMBER": args.number,
        "TITLE": args.title,
        "URL": args.url,
        "DIFFICULTY": args.difficulty,
        "TOPIC": args.topic,
        "MODULE": args.name,
        "METHOD": args.method,
    }

    solution_path.write_text(render((TEMPLATES / "solution_template.py").read_text(), **fields))
    test_path.write_text(render((TEMPLATES / "test_template.py").read_text(), **fields))

    print("Created:")
    print(f"  {solution_path.relative_to(REPO_ROOT)}")
    print(f"  {test_path.relative_to(REPO_ROOT)}")
    print(f"\nNext: implement the solution, then run")
    print(f"  pytest {test_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
