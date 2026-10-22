# C++ / Low-Latency Track

Modern C++ for trading and performance-critical systems, from fundamentals to benchmarked low-latency infrastructure.

Each project is a self-contained CMake project with tests. Start a new one by copying [`_template/`](_template/) or running:

```bash
python3 ../scripts/new_project.py --track cpp --level <level> --id <slug> --title "..."
```

**Build pattern** (same for every project):
```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release && cmake --build build -j
ctest --test-dir build --output-on-failure
```

See [`../ROADMAP.md`](../ROADMAP.md) for the planned sequence and [`../docs/workflow.md`](../docs/workflow.md) for the Definition of Done.
