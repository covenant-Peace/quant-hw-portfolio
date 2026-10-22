# <Project Title>

> One-sentence pitch: what it does and why it's interesting.

**Track:** C++ / Low-Latency · **Level:** <foundation|basic|medium|robust> · **Status:** <planned|in-progress|complete>

## Problem
What problem does this solve? Where does it show up in real trading / systems work?

## Approach
Key design decisions and *why* you made them. Data structures, algorithms, trade-offs.

## Results
- Correctness: how it's tested (and what the tests cover).
- Performance (if relevant): numbers, methodology, hardware. e.g. `p50 / p99 latency`, `throughput`.

## Build & run
```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j
./build/app
ctest --test-dir build --output-on-failure
```

## What I'd do next
The honest "if I had another week" list — shows self-awareness, which interviewers value.

---
*Remember to update this project's entry in [`docs/projects.json`](../../docs/projects.json) when status changes.*
