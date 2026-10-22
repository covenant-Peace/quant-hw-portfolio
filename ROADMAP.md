# Roadmap — 12 Months to Job-Ready

**Start:** 2026-10-22  **Target:** 2027-10-22
**Thesis:** Build a portfolio that tells one coherent story — *low-latency C++ and FPGA digital design, converging on hardware-accelerated trading.* That intersection is a real, well-paid niche (electronic trading / HFT firms, hardware-acceleration teams), and very few candidates can show both sides credibly. You will.

This roadmap is the plan; [`docs/projects.json`](docs/projects.json) is the live state. Keep them in agreement — when you finish something, update the JSON (status, dates, metrics, links) and the website + README tracker reflect it automatically.

---

## How to think about the levels

| Level | What it proves | Definition of Done (short) |
|-------|----------------|----------------------------|
| **Foundation** | You know the tools and the basics cold. | Builds, simulates/runs, has a self-checking test, has a 1-paragraph README. |
| **Basic** | You can finish a small real thing. | A complete feature; tests; README explaining *what & why*. |
| **Medium** | You can make engineering trade-offs. | Multiple components; measurements or coverage; design notes. |
| **Robust** | Interview-grade, defensible work. | Benchmarked/verified; thorough write-up; you can whiteboard any part. |

Full criteria live in [`docs/workflow.md`](docs/workflow.md).

---

## The two tracks, converging

```
C++ / Low-Latency            SystemVerilog / VHDL           HW/SW Co-Design
───────────────────          ──────────────────────         ─────────────────
Foundations & katas          Logic + blinky on FPGA
Market-data parser           Counters / FSM / debounce
Limit order book             UART
MA backtester                SPI / I2C
Matching engine       ┐      Sync/async FIFO (CDC)
Lock-free queues      │      Pipelined FIR filter
Low-latency logger    │      AXI peripheral
Feed handler (ITCH)   ├────▶ RISC-V (multi-cycle)    ┐
Backtesting framework ┘      RISC-V (pipelined)       ├──▶ HW top-of-book accelerator
                             UVM verification env     ┘    FPGA feed parser + C++ host  ◀── CAPSTONE
```

---

## Suggested quarter-by-quarter pacing

> ~2 projects/month is the target cadence, but **depth beats speed** — a robust project you can defend end-to-end is worth more than three rushed ones. Adjust freely; the tracker measures *completion*, not guilt.

### Q1 (months 1–3) — Foundations, both hands
Get both toolchains fluent and ship small wins.
- **C++:** Foundations & data-structure katas → Market-data parser.
- **HDL:** Logic + blinky on FPGA → Counters/FSM/debouncer.
- **Milestone:** both toolchains set up, CI green, first LED blinking, first ticks parsed.

### Q2 (months 4–6) — First real projects
- **C++:** Limit order book → MA backtester.
- **HDL:** UART → SPI/I2C (talk to real hardware).
- **Milestone:** a working order book and a UART demo you can show on video.

### Q3 (months 7–9) — Depth & trade-offs
- **C++:** Matching engine → lock-free queues → low-latency logger.
- **HDL:** Sync/async FIFO (CDC) → pipelined FIR → AXI peripheral.
- **Milestone:** first latency/throughput benchmarks; first timing-closed design.

### Q4 (months 10–12) — Flagships & the intersection
- **C++:** ITCH-style feed handler → backtesting framework.
- **HDL:** RISC-V core (multi-cycle → pipelined) → UVM environment.
- **Intersection:** HW top-of-book accelerator → **FPGA feed parser + C++ host (capstone)**.
- **Milestone:** one flagship CPU core, one verification env with coverage, and the end-to-end HW/SW capstone with a measured latency number.

---

## What "job-ready" looks like at the finish line

By 2027-10-22 you want to be able to point a recruiter at this site and have them see:

1. **A CPU core on real FPGA hardware** (RISC-V) — the headline hardware project.
2. **A UVM verification environment with coverage closure** — proves you can verify, not just design.
3. **A limit order book + matching engine in C++** — the canonical trading projects, done well.
4. **Benchmarked low-latency infrastructure** (lock-free queues, logger) with real numbers.
5. **The capstone**: an FPGA feed parser streaming to a C++ host, with an end-to-end latency figure.
6. **Write-ups** for each flagship: the problem, your design choices, the trade-offs, and what you'd do next.

Plus the soft signal the tracker itself sends: *this person sets a long-term plan and executes it consistently.* That story, visible in your commit history and this dashboard, is worth as much as any single project.

---

## Companies this profile targets

- **Electronic trading / HFT:** Optiver, IMC, Jump Trading, Jane Street, Hudson River Trading, Citadel Securities, DRW, Maven, XTX.
- **FPGA / hardware acceleration:** NVIDIA, AMD/Xilinx, Intel, Arista, Marvell, plus the hardware teams inside the trading firms above.
- **Intersection roles:** "FPGA Engineer (Trading)", "Low-Latency Developer", "Hardware Acceleration Engineer" — the sweet spot this portfolio aims at.

Tailor which projects you foreground per application; the portfolio holds them all.
