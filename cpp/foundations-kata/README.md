# Modern C++ Foundations & Data-Structure Katas

> Three from-scratch, allocation-conscious data structures that show up everywhere in low-latency code — each with self-checking tests and a complexity note.

**Track:** C++ / Low-Latency · **Level:** Foundation · **Status:** in-progress

## What to build

Implement each as a header (templates → header-only is fine). Replace the placeholder
`src/core.*` with these, and add a test file per structure under `tests/`.

### 1. `ring_buffer<T, N>` — fixed-capacity circular buffer
The workhorse of market-data pipelines (bounded, no per-op allocation).
- API: `push(v)` / `try_push(v)`, `pop()` / `try_pop()`, `front()`, `size()`, `empty()`, `full()`, `capacity()`.
- All operations **O(1)**, no heap allocation after construction.
- Edge cases to test: wrap-around, full/empty behavior, FIFO order.

### 2. `static_vector<T, N>` — vector with inline storage
A `std::vector`-like container that never touches the heap (caps at `N`).
- API: `push_back`, `emplace_back`, `pop_back`, `operator[]`, `size`, `capacity`, `begin/end`.
- Teaches: `alignas` + aligned storage, **placement new**, manual destructor calls, correct cleanup in the destructor.
- Edge cases: destructors run exactly once; overflow past `N` is handled (assert or throw — document which).

### 3. `intrusive_list<T>` — intrusive doubly-linked list
Zero-allocation, cache-friendly list where the node stores its own links (an HFT staple).
- The element embeds a `list_hook` (prev/next); the list just threads existing objects.
- API: `push_front`, `push_back`, `erase(iterator)`, `front`, `back`, iteration, `empty`.
- Teaches: why intrusive containers avoid allocation and extra indirection vs `std::list`.
- Edge cases: erase from middle/ends, an element can belong to the list without being copied.

## Definition of Done (Foundation)
- [ ] Builds clean with `-Wall -Wextra -Wpedantic`, no warnings.
- [ ] Each structure has a self-checking test (this project uses Catch2 via CMake).
- [ ] A one-line complexity note per operation in the header.
- [ ] This README's checklist all ticked.

## Build & test
```bash
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build build
ctest --test-dir build --output-on-failure
```

## Notes
Keep a short "what I learned" line here as you go (placement new gotchas, move vs copy,
iterator invalidation…) — it becomes your interview talking points.

---
*Update this project's entry in [`../../docs/projects.json`](../../docs/projects.json) when status changes.*
