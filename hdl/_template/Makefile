# Simulation Makefile — open-source tools (install via Homebrew on macOS):
#   brew install icarus-verilog verilator gtkwave
#
#   make        -> compile + run the testbench (Icarus Verilog)
#   make wave   -> open the waveform in GTKWave
#   make lint   -> lint the RTL with Verilator (catches many bugs early)
#   make clean

TOP     := tb_dut
RTL     := $(wildcard rtl/*.sv)
TB      := $(wildcard tb/*.sv)
BUILD   := build
VVP     := $(BUILD)/$(TOP).vvp
VCD     := $(TOP).vcd

.PHONY: all sim wave lint clean
all: sim

sim: $(VVP)
	@vvp $(VVP)

$(VVP): $(RTL) $(TB) | $(BUILD)
	iverilog -g2012 -Wall -s $(TOP) -o $@ $(RTL) $(TB)

$(BUILD):
	@mkdir -p $(BUILD)

wave: $(VCD)
	gtkwave $(VCD) &

lint:
	verilator --lint-only -Wall -Irtl $(RTL)

clean:
	rm -rf $(BUILD) $(VCD)
