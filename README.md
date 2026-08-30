# CPython Runtime Mechanics & Deep Optimization Engine

[![Python Version](https://shields.io)](https://python.org)
[![License: MIT](https://shields.io)](https://opensource.org)

An architectural deep-dive portfolio focusing on CPython memory optimization, runtime mechanics, and low-level object behaviors. Built systematically to establish the high-performance foundation required for designing large-scale Deep Learning pipelines and AI model serving infrastructure.

## 📊 Milestone Tracking Dashboard
- **Current Progress:** 🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜ **32 / 161 Lectures Completed**
- **Target Track:** AI System Architect / Production MLOps Engineer

## 🛠️ Low-Level Dissections Completed
### 📦 Section 1: Variable References & Memory Management (Lectures 1-30)
* **Reference Counting Engine:** Probed `sys.getrefcount` pointers to visualize CPython heap allocation cycles.
* **Garbage Collection Optimization:** Analyzed cyclic reference traps and designed strategies using `gc.collect()` to prevent memory leaks in long-running processes.
* **Object Mutability & Shared Cache:** Dissected memory IDs to map string interning and pointer tracking mechanics.

### 🔢 Section 2: Numeric Types & Integer Interning (Lectures 31-32)
* **Dunder Math Architecture:** Mapped high-level symbols (`//`, `%`) to compiled C routines (`__floordiv__`, `__mod__`).
* **Arbitrary Precision Logic:** Explored CPython's internal array structure (`ob_digit`) for unlimited size integers.
* **Radix Serialization Boundaries:** Probed lexical parsing security walls, ASCII symbol lookups, and explicit radix string-to-base constructor constraints.
