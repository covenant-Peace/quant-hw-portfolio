# Constraints

Put your board-specific constraints here (pin assignments + clock/timing):

- **Xilinx (Vivado):** `*.xdc` — pin locations, I/O standards, `create_clock`.
- **Intel/Altera (Quartus):** `*.qsf` / `*.sdc`.
- **Lattice (open-source: Yosys + nextpnr):** `*.lpf` or `*.pcf`.

Keep timing constraints (clock period, input/output delays) here too — a design
isn't "done" at the robust level until it meets timing on your actual board.

> Fill in your FPGA board + toolchain here once, then copy this folder per project.
