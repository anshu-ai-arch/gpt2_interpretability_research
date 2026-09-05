# GPT-2 XL Interpretability Research: Phase 4.6

## Project Overview
This repository investigates **Late-Layer Readout Drift** in deep transformer architectures (`gpt2-xl`, 48 layers) and introduces **Gate 5-v2 (Depth-Aware Circuit Localization)** to eliminate false-positive circuit detections.

## Key Findings
* **Gate 5-v1 Issue:** Relative local-window metrics failed on 100% of prompts (50/50 passed) due to high residual-stream storage past layer 35.
* **Gate 5-v2 Solution:** Implements a depth cutoff ($L_{35}$) and mid-network baseline comparison ($L_{12}-L_{28}$), lowering the false-positive candidate rate down to **6% (3/50)**.

## Repository Structure
* `notebooks/phase4_6_circuit_gate.ipynb` - Interactive experiment notebook.
* `src/gates.py` - Core Gate 5-v2 implementation and curve shape analyzer.
* `data/` - Raw layer-by-layer causal recovery curve outputs (`.jsonl`).
