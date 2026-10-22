# HW/SW Co-Design Track — the headline story

Projects where C++ and the FPGA work *together* for low-latency trading. This is the differentiator: very few candidates can credibly show both software and hardware solving the same problem, with a measured comparison between them.

These projects depend on the C++ and HDL tracks (e.g. the hardware top-of-book accelerator is compared against the C++ limit order book). Build the prerequisites first — see [`../ROADMAP.md`](../ROADMAP.md).

Each project should answer: **what moved to hardware, why, and what latency did it buy?**

Start one with:
```bash
python3 ../scripts/new_project.py --track intersection --level <level> --id <slug> --title "..."
```
