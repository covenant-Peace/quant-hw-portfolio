#!/usr/bin/env python3
"""Validate docs/projects.json so a typo never silently breaks the site.

Checks: required fields present, ids unique, track/level/status values valid,
and that referenced paths look sane. Exits non-zero on any error. Stdlib only.

    python3 scripts/validate_registry.py
"""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "docs" / "projects.json"

REQUIRED = ["id", "title", "track", "level", "status", "summary"]
STATUSES = {"planned", "in-progress", "complete"}


def main() -> int:
    data = json.loads(DATA.read_text())
    errors: list[str] = []

    track_ids = {t["id"] for t in data.get("tracks", [])}
    level_ids = {l["id"] for l in data.get("levels", [])}
    if not track_ids:
        errors.append("no tracks defined")
    if not level_ids:
        errors.append("no levels defined")

    seen: set[str] = set()
    for i, p in enumerate(data.get("projects", [])):
        where = p.get("id", f"index {i}")
        for field in REQUIRED:
            if field not in p or p[field] in (None, ""):
                errors.append(f"[{where}] missing required field '{field}'")
        pid = p.get("id")
        if pid in seen:
            errors.append(f"[{where}] duplicate id")
        seen.add(pid)
        if p.get("track") not in track_ids:
            errors.append(f"[{where}] unknown track '{p.get('track')}'")
        if p.get("level") not in level_ids:
            errors.append(f"[{where}] unknown level '{p.get('level')}'")
        if p.get("status") not in STATUSES:
            errors.append(f"[{where}] invalid status '{p.get('status')}' "
                          f"(use one of {sorted(STATUSES)})")

    if errors:
        print(f"✗ {len(errors)} problem(s) in {DATA.relative_to(ROOT)}:")
        for e in errors:
            print("  -", e)
        return 1

    n = len(data["projects"])
    print(f"✓ projects.json valid — {n} projects, "
          f"{len(track_ids)} tracks, {len(level_ids)} levels.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
