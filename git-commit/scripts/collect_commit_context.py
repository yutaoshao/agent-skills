#!/usr/bin/env python3
"""Print a structured summary of the current repository changes."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Sequence

RECENT_COMMIT_COUNT = 5
EMPTY_VALUE = "(none)"


def run_git(repo: Path, args: Sequence[str]) -> str:
    command = ["git", *args]
    result = subprocess.run(
        command,
        cwd=repo,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 0:
        return result.stdout.rstrip()

    stderr = result.stderr.strip()
    stdout = result.stdout.strip()
    message = stderr or stdout or "git command failed"
    raise RuntimeError(f"$ {' '.join(command)}\n{message}")


def resolve_repo(candidate: str | None) -> Path:
    base = Path(candidate or ".").resolve()
    output = run_git(base, ["rev-parse", "--show-toplevel"])
    return Path(output.strip())


def parse_porcelain(output: str) -> tuple[list[str], list[str], list[str], list[str]]:
    combined: list[str] = []
    staged: list[str] = []
    unstaged: list[str] = []
    untracked: list[str] = []

    for line in output.splitlines():
        if not line:
            continue

        combined.append(line)
        if line.startswith("?? "):
            untracked.append(line[3:])
            continue

        staged_code = line[0]
        unstaged_code = line[1]
        path = line[3:]
        if staged_code != " ":
            staged.append(f"{staged_code} {path}")
        if unstaged_code != " ":
            unstaged.append(f"{unstaged_code} {path}")

    return combined, staged, unstaged, untracked


def to_lines(output: str) -> list[str]:
    return [line for line in output.splitlines() if line.strip()]


def print_section(title: str, lines: Sequence[str]) -> None:
    print(f"## {title}")
    if not lines:
        print(EMPTY_VALUE)
        print()
        return

    for line in lines:
        print(line)
    print()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Summarize git status and diff stats for commit drafting.",
    )
    parser.add_argument(
        "--repo",
        help="Repository path. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--recent-count",
        type=int,
        default=RECENT_COMMIT_COUNT,
        help="Number of recent commit subjects to print.",
    )
    return parser


def has_commit_history(repo: Path) -> bool:
    command = ["git", "rev-parse", "--verify", "HEAD"]
    result = subprocess.run(
        command,
        cwd=repo,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0


def get_recent_commits(repo: Path, recent_count: int) -> list[str]:
    if recent_count < 1:
        raise RuntimeError("--recent-count must be at least 1")
    if not has_commit_history(repo):
        return []
    return to_lines(run_git(repo, ["log", "--oneline", f"-{recent_count}"]))


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        repo = resolve_repo(args.repo)
        branch = run_git(repo, ["branch", "--show-current"]) or "(detached HEAD)"
        porcelain = run_git(repo, ["status", "--short"])
        status_lines, staged, unstaged, untracked = parse_porcelain(porcelain)
        staged_names = to_lines(run_git(repo, ["diff", "--cached", "--name-status"]))
        unstaged_names = to_lines(run_git(repo, ["diff", "--name-status"]))
        staged_stat = to_lines(run_git(repo, ["diff", "--cached", "--stat"]))
        unstaged_stat = to_lines(run_git(repo, ["diff", "--stat"]))
        recent = get_recent_commits(repo, args.recent_count)
    except RuntimeError as error:
        print(str(error), file=sys.stderr)
        return 1

    print("# Git Commit Context")
    print()
    print(f"repo: {repo}")
    print(f"branch: {branch}")
    print()
    print_section("Working Tree Status", status_lines)
    print_section("Staged Files", staged)
    print_section("Unstaged Files", unstaged)
    print_section("Untracked Files", untracked)
    print_section("Staged Name Status", staged_names)
    print_section("Staged Diff Stat", staged_stat)
    print_section("Unstaged Name Status", unstaged_names)
    print_section("Unstaged Diff Stat", unstaged_stat)
    print_section("Recent Commits", recent)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
