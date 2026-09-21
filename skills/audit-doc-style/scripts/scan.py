#!/usr/bin/env python3
"""Heuristic flags for Google developer-doc style. Not a grade.

Prints Markdown table hits for audit-doc-style. Skips fenced code and
vendored trees. Treat output as candidates; quoted UI and identifiers can
be fine.

Usage:
  python3 scan.py --list [PATH ...]
  python3 scan.py PATH [PATH ...]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "node_modules",
    "vendor",
    "dist",
    "build",
    "target",
    "__pycache__",
    ".tox",
    "site-packages",
}
DOC_SUFFIXES = {".md", ".mdx", ".markdown", ".html", ".htm"}

# severity, compiled pattern, hint
# Keep this list small and high-signal. Voice still needs a human/agent.
RULES: list[tuple[str, re.Pattern[str], str]] = [
    ("dont", re.compile(r"\bplease\b", re.I), "omit please in instructions"),
    ("dont", re.compile(r"\bclick here\b", re.I), "descriptive link text"),
    ("dont", re.compile(r"\bclick on\b", re.I), "click, not click on"),
    ("dont", re.compile(r"\bsimply\b|\bit's easy\b|\bit's that simple\b", re.I), "omit simply/easy"),
    ("dont", re.compile(r"\blet's\b", re.I), "you / imperative, not let's"),
    ("dont", re.compile(r"\bwhitelist|\bblacklist|\bgraylist", re.I), "allowlist / blocklist, or rewrite"),
    ("dont", re.compile(r"\bsanity[- ]check\b|\bdummy variable\b", re.I), "quick check / placeholder"),
    ("dont", re.compile(r"\bhamburger(?: menu)?\b|\bzippy\b|\bkebab menu\b", re.I), "use the control's accessible name"),
    ("dont", re.compile(r"\bhover over\b|\bhovering\b", re.I), "hold the pointer over"),
    ("dont", re.compile(r"\be\.g\.|\bi\.e\.", re.I), "for example / that is"),
    ("dont", re.compile(r"\betc\.", re.I), "such as / like; don't use etc."),
    ("dont", re.compile(r"\band so on\b|\band so forth\b", re.I), "such as / like"),
    ("dont", re.compile(r"\bin order to\b", re.I), "to, unless ambiguous"),
    ("dont", re.compile(r"\bleverage\b|\butilize\b", re.I), "use"),
    ("dont", re.compile(r"\bvia\b", re.I), "by using / through / over"),
    ("dont", re.compile(r"\bright-hand\b|\bleft-hand\b|\bon the left\b|\bon the right\b", re.I), "no directional UI language"),
    ("caution", re.compile(r"\babove\b|\bbelow\b", re.I), "preceding / following, not above/below"),
    ("caution", re.compile(r"\beasily\b|\bvery easy\b", re.I), "omit easily"),
    ("caution", re.compile(r"\ballows you to\b|\benables you to\b", re.I), "lets you"),
    ("caution", re.compile(r"\(optional\)", re.I), "Optional: at the start of the step"),
    ("caution", re.compile(r"\bwe will\b|\bwe'll\b|\bwe can\b|\bwe recommend you\b", re.I), "you, unless we is the org"),
    ("caution", re.compile(r"\btl;dr\b|\bymmv\b", re.I), "no internet slang"),
]


def iter_doc_files(roots: list[Path]) -> list[Path]:
    files: list[Path] = []
    for root in roots:
        root = root.resolve()
        if root.is_file():
            if root.suffix.lower() in DOC_SUFFIXES:
                files.append(root)
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            if path.suffix.lower() in DOC_SUFFIXES:
                files.append(path)
    return sorted(set(files))


def prose_lines(text: str) -> list[tuple[int, str]]:
    """Yield (1-based line number, line) with fenced code stripped."""
    out: list[tuple[int, str]] = []
    in_fence = False
    for i, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        out.append((i, line))
    return out


def strip_inline_code(line: str) -> str:
    return re.sub(r"`[^`]*`", " ", line)


def scan_file(path: Path) -> list[tuple[int, str, str, str]]:
    hits: list[tuple[int, str, str, str]] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"warning: skip {path}: {exc}", file=sys.stderr)
        return hits
    for lineno, line in prose_lines(text):
        sample = strip_inline_code(line)
        for severity, pattern, hint in RULES:
            if pattern.search(sample):
                snippet = line.strip()
                if len(snippet) > 120:
                    snippet = snippet[:117] + "..."
                hits.append((lineno, severity, hint, snippet))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", default=["."], help="Files or directories")
    parser.add_argument("--list", action="store_true", help="Print discovered doc paths only")
    args = parser.parse_args()
    roots = [Path(p) for p in args.paths]
    files = iter_doc_files(roots)
    if args.list:
        for path in files:
            print(path)
        return 0
    if not files:
        print("No Markdown/HTML files found.", file=sys.stderr)
        return 1
    print("| File | Line | Severity | Hint | Snippet |")
    print("|---|---:|---|---|---|")
    total = 0
    for path in files:
        for lineno, severity, hint, snippet in scan_file(path):
            safe = snippet.replace("|", "\\|")
            print(f"| `{path}` | {lineno} | {severity} | {hint} | {safe} |")
            total += 1
    print(f"\n{total} hit(s) in {len(files)} file(s). Heuristic only — score with the rubric.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
