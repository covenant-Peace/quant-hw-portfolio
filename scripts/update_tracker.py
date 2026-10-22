#!/usr/bin/env python3
"""Regenerate the progress tracker section of README.md from docs/projects.json.

No third-party dependencies (stdlib only). Run from anywhere:

    python3 scripts/update_tracker.py

It rewrites the block between the <!-- TRACKER:START --> and <!-- TRACKER:END -->
markers in README.md so the README always reflects the current project state.
"""
from __future__ import annotations

import datetime as dt
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "docs" / "projects.json"
README = ROOT / "README.md"

START = "<!-- TRACKER:START -->"
END = "<!-- TRACKER:END -->"

STATUS_ICON = {"complete": "✅", "in-progress": "🔨", "planned": "⬜"}


def bar(done: int, total: int, width: int = 18) -> str:
    if total == 0:
        return "─" * width + " 0%"
    filled = round(width * done / total)
    pct = round(100 * done / total)
    return "█" * filled + "░" * (width - filled) + f" {pct}%"


def build_tracker(data: dict) -> str:
    projects = data["projects"]
    tracks = {t["id"]: t for t in data["tracks"]}
    levels = {l["id"]: l for l in data["levels"]}

    done = sum(1 for p in projects if p["status"] == "complete")
    prog = sum(1 for p in projects if p["status"] == "in-progress")
    total = len(projects)

    out: list[str] = []
    out.append(f"**Overall:** `{bar(done, total)}`  —  {done} complete, "
               f"{prog} in progress, {total} total.")
    out.append("")

    # Per-track bars
    out.append("| Track | Progress | Done / Total |")
    out.append("|-------|----------|--------------|")
    for tid, t in tracks.items():
        tl = [p for p in projects if p["track"] == tid]
        d = sum(1 for p in tl if p["status"] == "complete")
        out.append(f"| {t['label']} | `{bar(d, len(tl))}` | {d} / {len(tl)} |")
    out.append("")

    # Full project table, grouped by track then level order
    level_order = {l: i for i, l in enumerate(levels)}
    out.append("| | Project | Track | Level | Status |")
    out.append("|-|---------|-------|-------|--------|")
    ordered = sorted(
        projects,
        key=lambda p: (list(tracks).index(p["track"]), level_order.get(p["level"], 99)),
    )
    for p in ordered:
        icon = STATUS_ICON.get(p["status"], "⬜")
        name = f"[{p['title']}]({p['repo']})" if p.get("repo") else p["title"]
        out.append(
            f"| {icon} | {name} | {tracks[p['track']]['label']} "
            f"| {levels[p['level']]['label']} | {p['status']} |"
        )
    out.append("")
    out.append(f"_Last updated {dt.date.today().isoformat()} by "
               f"`scripts/update_tracker.py`._")
    return "\n".join(out)


def main() -> None:
    data = json.loads(DATA.read_text())
    tracker = build_tracker(data)

    text = README.read_text()
    if START in text and END in text:
        pre = text.split(START)[0]
        post = text.split(END)[1]
        text = f"{pre}{START}\n{tracker}\n{END}{post}"
    else:  # markers missing — append a tracker section
        text = text.rstrip() + f"\n\n## 📊 Progress Tracker\n\n{START}\n{tracker}\n{END}\n"

    README.write_text(text)
    print(f"Updated {README.relative_to(ROOT)} tracker "
          f"({sum(1 for p in data['projects'] if p['status'] == 'complete')} complete).")


if __name__ == "__main__":
    main()
