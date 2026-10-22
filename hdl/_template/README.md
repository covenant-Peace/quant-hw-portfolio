# <Project Title>

> One-sentence pitch: what the hardware does.

**Track:** SystemVerilog / VHDL · **Level:** <foundation|basic|medium|robust> · **Status:** <planned|in-progress|complete>

## What it is
Block-level description. A small diagram (ASCII or image) goes a long way.

## Interface
| Signal | Dir | Width | Description |
|--------|-----|-------|-------------|
| clk    | in  | 1     | clock |
| rst_n  | in  | 1     | active-low reset |
| ...    |     |       |  |

## Verification
How the testbench checks correctness (self-checking? reference model? coverage?).
At medium/robust level, say what you measured: coverage %, corner cases, assertions.

## Simulate
```bash
make        # compile + run testbench (Icarus Verilog)
make wave   # view waveform in GTKWave
make lint   # Verilator lint
```

## On hardware (if deployed)
Board, toolchain, resource usage (LUTs/FFs/BRAM), and whether it met timing (Fmax).
Link a short demo video/GIF if you have one — hardware demos are persuasive.

## What I'd do next
Honest next steps.

---
*Update this project's entry in [`docs/projects.json`](../../docs/projects.json) when status changes.*
