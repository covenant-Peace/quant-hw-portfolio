<h1 align="center">Engineering Portfolio — Low-Latency C++ &amp; FPGA Digital Design</h1>

<p align="center">
  <em>A tracked, year-long progression toward roles at the intersection of electronic trading and hardware acceleration.</em>
</p>

<p align="center">
  <a href="ROADMAP.md">Roadmap</a> ·
  <a href="docs/projects.json">Project registry</a> ·
  <a href="docs/workflow.md">Workflow &amp; Definition of Done</a> ·
  <strong>Live site:</strong> <code>https://covenant-peace.github.io/quant-hw-portfolio/</code>
</p>

---

## What this is

Two things in one repository:

1. **A showcase** — a GitHub Pages website (in [`docs/`](docs/)) that presents every project to recruiters, with status, skills, metrics, and links.
2. **A tracker** — a single source of truth, [`docs/projects.json`](docs/projects.json), that drives both the website *and* the progress table below. Update one file; everything stays in sync.

The portfolio spans two tracks that deliberately converge:

- **C++ / Low-Latency** — order books, matching engines, backtesting, lock-free infrastructure.
- **SystemVerilog / VHDL** — logic fundamentals up to a RISC-V CPU core and a UVM verification environment, deployed on a real FPGA.
- **HW/SW Co-Design** — the headline: FPGA-accelerated trading, culminating in a hardware feed parser feeding a C++ host.

See [`ROADMAP.md`](ROADMAP.md) for the 12-month plan and the reasoning behind it.

## Repository layout

```
quant-hw-portfolio/
├── docs/                 # GitHub Pages site + projects.json (the source of truth)
│   ├── index.html        # the showcase (loads projects.json, shows live progress)
│   ├── projects.json     # ← edit this: every project's status, metrics, links
│   └── workflow.md       # how to add a project; Definition of Done per level
├── cpp/                  # C++ projects (each self-contained with CMake + tests)
│   └── _template/        # copy this to start a new C++ project
├── hdl/                  # SystemVerilog / VHDL projects (sim + FPGA)
│   └── _template/        # copy this to start a new HDL project
├── intersection/         # HW/SW co-design projects
├── scripts/              # new_project.py · update_tracker.py · validate_registry.py
└── .github/workflows/    # Pages deploy + CI (build C++, lint/sim HDL, validate registry)
```

## Everyday workflow

```bash
# Start a new project (scaffolds the folder AND registers it):
python3 scripts/new_project.py --track cpp --level basic \
  --id cpp-limit-order-book --title "Limit Order Book" \
  --summary "A price-time-priority order book."

# As you work, edit the project's entry in docs/projects.json
# (status -> in-progress/complete, add started/completed dates, metrics, repo link).

# Refresh the progress table in this README:
python3 scripts/update_tracker.py

# Sanity-check the registry before committing:
python3 scripts/validate_registry.py
```

The website updates automatically from `projects.json` — no build step. On push to `main`, GitHub Actions deploys `docs/` to Pages (enable once in **Settings → Pages → Source: GitHub Actions**).

## 📊 Progress Tracker

<!-- TRACKER:START -->
**Overall:** `░░░░░░░░░░░░░░░░░░ 0%`  —  0 complete, 0 in progress, 21 total.

| Track | Progress | Done / Total |
|-------|----------|--------------|
| C++ / Low-Latency | `░░░░░░░░░░░░░░░░░░ 0%` | 0 / 9 |
| SystemVerilog / VHDL | `░░░░░░░░░░░░░░░░░░ 0%` | 0 / 10 |
| HW/SW Co-Design | `░░░░░░░░░░░░░░░░░░ 0%` | 0 / 2 |

| | Project | Track | Level | Status |
|-|---------|-------|-------|--------|
| ⬜ | Modern C++ Foundations & Data-Structure Katas | C++ / Low-Latency | Foundation | planned |
| ⬜ | Market-Data CSV/Tick Parser & Stats Engine | C++ / Low-Latency | Foundation | planned |
| ⬜ | Limit Order Book | C++ / Low-Latency | Basic | planned |
| ⬜ | Moving-Average Strategy Backtester | C++ / Low-Latency | Basic | planned |
| ⬜ | Price-Time Matching Engine | C++ / Low-Latency | Medium | planned |
| ⬜ | Lock-Free SPSC / MPMC Queues | C++ / Low-Latency | Medium | planned |
| ⬜ | Low-Latency Asynchronous Logger | C++ / Low-Latency | Medium | planned |
| ⬜ | Exchange Feed Handler (ITCH-style) | C++ / Low-Latency | Robust | planned |
| ⬜ | Event-Driven Backtesting Framework | C++ / Low-Latency | Robust | planned |
| ⬜ | Combinational Logic + Blinky on FPGA | SystemVerilog / VHDL | Foundation | planned |
| ⬜ | Sequential Logic: Counters, FSMs & Debouncer | SystemVerilog / VHDL | Foundation | planned |
| ⬜ | UART Transmitter / Receiver | SystemVerilog / VHDL | Basic | planned |
| ⬜ | SPI & I2C Master Controllers | SystemVerilog / VHDL | Basic | planned |
| ⬜ | Synchronous & Asynchronous FIFO (CDC) | SystemVerilog / VHDL | Medium | planned |
| ⬜ | Pipelined Fixed-Point FIR Filter | SystemVerilog / VHDL | Medium | planned |
| ⬜ | AXI-Lite / AXI-Stream Peripheral | SystemVerilog / VHDL | Medium | planned |
| ⬜ | Multi-Cycle RISC-V Core (RV32I) | SystemVerilog / VHDL | Robust | planned |
| ⬜ | Pipelined RISC-V Core with Hazard Handling | SystemVerilog / VHDL | Robust | planned |
| ⬜ | UVM Verification Environment | SystemVerilog / VHDL | Robust | planned |
| ⬜ | Hardware Top-of-Book Accelerator | HW/SW Co-Design | Medium | planned |
| ⬜ | FPGA Market-Data Parser + C++ Host Pipeline | HW/SW Co-Design | Robust | planned |

_Last updated 2026-10-22 by `scripts/update_tracker.py`._
<!-- TRACKER:END -->

---

<p align="center"><sub>Edit <code>docs/projects.json</code> → the site and this table follow. Depth over speed — each project is done only when it meets its <a href="docs/workflow.md">Definition of Done</a>.</sub></p>
