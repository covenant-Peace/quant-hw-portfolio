# SystemVerilog / VHDL Track

RTL design and verification, from logic fundamentals to a RISC-V CPU core and a UVM environment — simulated with open-source tools and deployed on a real FPGA.

**Toolchain (macOS):**
```bash
brew install icarus-verilog verilator gtkwave
```

Each project copies [`_template/`](_template/) (RTL + self-checking testbench + Makefile). Simulate with:
```bash
make        # compile + run testbench
make wave   # view the waveform
make lint   # Verilator lint
```

Vendor FPGA toolchain (Vivado / Quartus / open-source Yosys+nextpnr) is used for synthesis and on-board deployment; put board constraints in each project's `constraints/` folder.

See [`../ROADMAP.md`](../ROADMAP.md) for the planned sequence and [`../docs/workflow.md`](../docs/workflow.md) for the Definition of Done.
