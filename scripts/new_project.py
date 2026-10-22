#!/usr/bin/env python3
"""Scaffold a new project from a template and register it in docs/projects.json.

Usage:
    python3 scripts/new_project.py \
        --track cpp \
        --level basic \
        --id cpp-limit-order-book \
        --title "Limit Order Book" \
        --summary "A price-time-priority order book."

- Copies cpp/_template or hdl/_template into the right folder (skips if it exists).
- Adds a project entry to docs/projects.json if the id isn't already there.
Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "docs" / "projects.json"

TEMPLATE_DIR = {"cpp": "cpp/_template", "hdl": "hdl/_template", "intersection": "hdl/_template"}
BASE_DIR = {"cpp": "cpp", "hdl": "hdl", "intersection": "intersection"}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--track", required=True, choices=["cpp", "hdl", "intersection"])
    ap.add_argument("--level", required=True,
                    choices=["foundation", "basic", "medium", "robust"])
    ap.add_argument("--id", required=True, help="unique slug, e.g. cpp-limit-order-book")
    ap.add_argument("--title", required=True)
    ap.add_argument("--summary", default="")
    ap.add_argument("--dir", default=None, help="folder name (defaults to id minus track prefix)")
    args = ap.parse_args()

    folder = args.dir or args.id.replace(f"{args.track}-", "").replace("x-", "")
    dest = ROOT / BASE_DIR[args.track] / folder
    template = ROOT / TEMPLATE_DIR[args.track]

    if dest.exists():
        print(f"! {dest.relative_to(ROOT)} already exists — not copying template.")
    else:
        shutil.copytree(template, dest)
        print(f"+ scaffolded {dest.relative_to(ROOT)} from {template.relative_to(ROOT)}")

    data = json.loads(DATA.read_text())
    if any(p["id"] == args.id for p in data["projects"]):
        print(f"! id '{args.id}' already in projects.json — leaving registry unchanged.")
    else:
        data["projects"].append({
            "id": args.id,
            "title": args.title,
            "track": args.track,
            "level": args.level,
            "status": "planned",
            "summary": args.summary,
            "whyItMatters": "",
            "skills": [],
            "path": str((BASE_DIR[args.track] + "/" + folder)),
            "repo": "", "writeup": "", "demo": "",
            "started": None, "completed": None, "metrics": [], "tags": [],
        })
        DATA.write_text(json.dumps(data, indent=2) + "\n")
        print(f"+ registered '{args.id}' in {DATA.relative_to(ROOT)}")

    print("\nNext: edit the project's README, set status to 'in-progress' in projects.json,")
    print("then run  python3 scripts/update_tracker.py  to refresh the README tracker.")


if __name__ == "__main__":
    main()
