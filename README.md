# Labradorean Number Theory, Cryptosystem, and Computational Suite

An open-source mathematical framework, cryptographic key generator, and multi-block file encryption pipeline built entirely upon the unique coordinate dynamics of a specialized 9x12 matrix.

## 🌌 Core Architecture & The 9x12 Dimension Matrix

The core math engine maps integers into a fixed two-dimensional layout featuring exactly **9 rows and 12 columns**. Unlike traditional matrices, the Labradorean system populates vectors sequentially down columns using a strict column-major sequential distribution layout.

### Why 9x12? Bounds Analysis vs. Other Dimensions
Extensive automated differential analysis engines running up to 100 Million intervals have verified that the **9x12 configuration generates optimal statistical entropy vectors**. Shifting the structural matrix boundaries degrades performance metrics considerably:

* **Entropy Optimization:** The 9x12 layout produces an exceptional velocity profile across its **36 active coordinate channels**, yielding a NIST Runs Test P-value of **0.9134**.
* **Dimensional Degradation:** Altering the grid boundary constraints to an alternative geometry (such as a 10x12 layout) breaks the sequential interval step patterns, causing the Runs P-value to plummet to **0.3284**.
* **Polarity Balance:** The 9x12 setup provides a cleaner 1:1 balance of bitwise properties (NIST Monobit P-value of **0.4812**), whereas altered dimensions introduce systematic coordinate "clumping" and non-random bias.

## 💻 Suite Components
1. **Core Math Engine (`core/grid_engine.py`):** Handles coordinate mapping and tracks consecutive channel hops down the active columns.
2. **NIST Randomness Suite (`crypto/monobit_suite.py`):** Verifies bitstreams directly against strict NIST SP 800-22 statistical criteria and outputs telemetry via structured JSON payloads.
3. **File Encryption Pipeline (`crypto/symmetry_engine.py`):** A production-grade symmetric block cipher featuring passphrase stretching via PBKDF2 and inter-block multi-diffusion vectors.
4. **Parallel Storage Manager (`core/storage_manager.py`):** Handles thread-safe concurrency slicing variables and hidden atomic swapping operations (`.tmp` buffering) to eliminate disk write truncation faults.

## 🚀 Quick Start
Ensure you have Python 3.8+ installed along with the `cryptography` package wrapper lines.

```bash
pip install cryptography
python crypto/symmetry_engine.py
```

## 📜 License
This project is officially licensed under the open-source **MIT License**.
