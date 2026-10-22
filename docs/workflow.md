# Workflow & Definition of Done

This is the discipline that turns a pile of folders into a portfolio recruiters trust. Keep it light, keep it honest.

## Adding a project

1. **Scaffold + register** in one step:
   ```bash
   python3 scripts/new_project.py --track <cpp|hdl|intersection> \
     --level <foundation|basic|medium|robust> \
     --id <unique-slug> --title "Human Title" --summary "One line."
   ```
2. **Set status** in [`projects.json`](projects.json) to `in-progress` and fill `started`.
3. **Build it.** Fill in the project's `README.md` as you go (it doubles as your write-up).
4. **Finish it** against the Definition of Done below. Set `status: "complete"`, add `completed`, any `metrics`, and the `repo`/`writeup`/`demo` links.
5. **Refresh + validate:**
   ```bash
   python3 scripts/update_tracker.py && python3 scripts/validate_registry.py
   ```
6. **Commit** with a clear message, e.g. `feat(cpp): limit order book — add/cancel/modify + replay tests`.

## `projects.json` field reference

| Field | Meaning |
|-------|---------|
| `id` | Unique slug (e.g. `cpp-limit-order-book`). Never reuse. |
| `track` | `cpp` \| `hdl` \| `intersection`. |
| `level` | `foundation` \| `basic` \| `medium` \| `robust`. |
| `status` | `planned` \| `in-progress` \| `complete`. Drives colors/filters on the site. |
| `summary` | One or two sentences: what it is. |
| `whyItMatters` | The job-relevance hook — why an interviewer should care. |
| `skills` | Short tags shown as chips (e.g. `"CDC / Gray code"`). |
| `metrics` | Headline results, e.g. `"p99 42 ns"`, `"Fmax 180 MHz"`, `"coverage 98%"`. |
| `started` / `completed` | ISO dates (`YYYY-MM-DD`) or `null`. |
| `repo` / `writeup` / `demo` | Links shown as buttons on the card. |

## Definition of Done, by level

Each level is a strict superset of the one before it.

### Foundation ✔
- [ ] Builds / simulates cleanly with no warnings.
- [ ] At least one **self-checking** test (C++ unit test, or SV testbench that `$fatal`s on mismatch).
- [ ] A one-paragraph README: what it is, how to run it.

### Basic ✔ (+ Foundation)
- [ ] Solves a complete, self-contained problem end to end.
- [ ] Tests cover the main cases and at least one edge case.
- [ ] README explains the **why**, not just the how.

### Medium ✔ (+ Basic)
- [ ] Multiple components with a clear interface between them.
- [ ] A **measurement or coverage** number recorded in `metrics` (latency, throughput, functional coverage, resource usage…).
- [ ] Design notes: the key trade-off you made and why.

### Robust ✔ (+ Medium) — *interview-grade*
- [ ] Benchmarked (C++) or verified to a coverage goal / timing-closed on hardware (HDL).
- [ ] A thorough write-up: problem → design → results → "what I'd do next".
- [ ] You can **whiteboard any part of it** cold. If you can't explain it, it isn't robust yet.
- [ ] A demo artifact where it makes sense (GIF, screenshot, numbers table).

## Honesty rules

- `complete` means *actually done to its level*, not "mostly working". Recruiters will open the code.
- Prefer **one robust project over three half-finished ones**. The tracker rewards depth.
- Record real numbers only. A fabricated benchmark is worse than none.
- Keep commits small and frequent — your commit history is itself part of the portfolio story.
