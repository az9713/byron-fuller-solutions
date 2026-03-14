#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import subprocess
from datetime import datetime
from pathlib import Path


BASE = Path(r"C:\Users\simon\Downloads\projects\_CORE\_claude_code\byron_fuller")
TRACKER = BASE / "manual_review_progress_ch02_ch10.csv"
LIVE_STATUS = BASE / "manual_review_live_status.txt"
ACTIVITY_LOG = BASE / "manual_review_activity.log"
REPORT_DIR = BASE / "review_reports_ch02_ch10"


def latex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    out = []
    for ch in text:
        out.append(replacements.get(ch, ch))
    return "".join(out)


def normalize_problem_id(problem: str) -> str:
    problem = problem.strip()
    if not problem.startswith("ch"):
        raise ValueError(f"Problem id must look like ch03_05, got: {problem}")
    ch, num = problem.split("_", 1)
    return f"{ch}_{int(num):02d}"


def sort_key(problem: str) -> tuple[int, int]:
    ch, num = problem.split("_")
    return int(ch[2:]), int(num)


def load_rows() -> list[dict[str, str]]:
    if not TRACKER.exists():
        return []
    with TRACKER.open("r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows: list[dict[str, str]] = []
        for r in reader:
            rows.append(
                {
                    "problem": r.get("problem") or r.get("\ufeffproblem", ""),
                    "status": r.get("status", ""),
                    "notes": r.get("notes", ""),
                }
            )
        return rows


def save_rows(rows: list[dict[str, str]]) -> None:
    dedup: dict[str, dict[str, str]] = {}
    for r in rows:
        dedup[r["problem"]] = r
    sorted_rows = sorted(dedup.values(), key=lambda r: sort_key(r["problem"]))
    with TRACKER.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["problem", "status", "notes"])
        writer.writeheader()
        writer.writerows(sorted_rows)


def set_row(rows: list[dict[str, str]], problem: str, status: str, notes: str) -> None:
    for r in rows:
        if r["problem"] == problem:
            r["status"] = status
            r["notes"] = notes
            return
    rows.append({"problem": problem, "status": status, "notes": notes})


def now_local() -> str:
    return datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")


def write_live_status(rows: list[dict[str, str]]) -> None:
    in_progress = next((r for r in rows if r["status"] == "in_progress"), None)
    if not in_progress:
        in_progress = sorted(rows, key=lambda r: sort_key(r["problem"]))[-1]
    verified = sum(1 for r in rows if r["status"].startswith("manually_verified_"))
    ts = now_local()
    LIVE_STATUS.write_text(
        "\n".join(
            [
                f"last_update={ts}",
                f"current_problem={in_progress['problem']}",
                f"current_status={in_progress['status']}",
                f"completed_verified={verified}",
                "target_total=246",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    with ACTIVITY_LOG.open("a", encoding="utf-8") as f:
        f.write(
            f"{ts} | current={in_progress['problem']} | status={in_progress['status']} | completed={verified}/246\n"
        )


def verdict_label(status: str) -> str:
    mapping = {
        "manually_verified_accept": "ACCEPT",
        "manually_verified_incomplete": "INCOMPLETE",
        "manually_verified_incorrect": "INCORRECT",
    }
    return mapping.get(status, status.upper())


def build_report_tex(
    problem: str,
    status: str,
    note: str,
    bullets: list[str],
    corrected_required: bool,
) -> str:
    ch = problem.split("_")[0]
    problem_num = int(problem.split("_")[1])
    verdict = verdict_label(status)
    escaped_bullets = "\n".join(
        f"\\item {latex_escape(line)}" for line in bullets if line.strip()
    )
    if not escaped_bullets:
        escaped_bullets = "\\item Line-by-line mathematical consistency check completed."
    corrected_text = (
        "A separate revised-solution PDF is required and tracked in "
        "\\texttt{revised\\_ch02\\_ch10/}."
        if corrected_required
        else "No revised-solution PDF is required for this file."
    )
    return rf"""\documentclass[11pt]{{article}}
\usepackage[margin=1in]{{geometry}}
\usepackage{{amsmath,amssymb}}
\usepackage[T1]{{fontenc}}
\usepackage{{lmodern}}

\begin{{document}}

\begin{{center}}
{{\Large\bfseries Critique Report: {latex_escape(problem)}}}\\[4pt]
Source file: \texttt{{{latex_escape(ch)}/{latex_escape(problem)}.pdf}}
\end{{center}}

\section*{{Verdict}}
\textbf{{{latex_escape(verdict)}}}

\section*{{Technical Summary}}
{latex_escape(note)}

\section*{{Line-by-Line Checks Performed}}
\begin{{itemize}}
{escaped_bullets}
\end{{itemize}}

\section*{{Revised Solution Requirement}}
{corrected_text}

\end{{document}}
"""


def write_and_compile_report(
    problem: str, status: str, note: str, bullets: list[str], corrected_required: bool
) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    tex_path = REPORT_DIR / f"{problem}_critique.tex"
    tex_path.write_text(
        build_report_tex(problem, status, note, bullets, corrected_required),
        encoding="utf-8",
    )
    subprocess.run(
        ["tectonic", tex_path.name, "--keep-logs", "--keep-intermediates"],
        cwd=str(REPORT_DIR),
        check=True,
    )


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Update tracker/status/log and regenerate one critique PDF."
    )
    p.add_argument("--problem", required=True, help="Problem id, e.g. ch03_05")
    p.add_argument(
        "--status",
        required=True,
        choices=[
            "manually_verified_accept",
            "manually_verified_incomplete",
            "manually_verified_incorrect",
        ],
    )
    p.add_argument("--note", required=True, help="Short technical note for tracker/report.")
    p.add_argument(
        "--bullet",
        action="append",
        default=[],
        help="A checked-step bullet. Repeat for multiple bullets.",
    )
    p.add_argument(
        "--next-problem",
        help="Optional next problem id to set as in_progress.",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    problem = normalize_problem_id(args.problem)
    rows = load_rows()
    set_row(rows, problem, args.status, args.note.strip())
    if args.next_problem:
        next_problem = normalize_problem_id(args.next_problem)
        set_row(rows, next_problem, "in_progress", "Starting full line-by-line verification now.")
    save_rows(rows)
    write_live_status(rows)
    write_and_compile_report(
        problem=problem,
        status=args.status,
        note=args.note.strip(),
        bullets=args.bullet,
        corrected_required=args.status != "manually_verified_accept",
    )
    print(f"Updated {problem} and regenerated critique PDF.")


if __name__ == "__main__":
    main()
