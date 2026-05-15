# ReliantOps | Security Automation & Infrastructure Resilience

A collection of Python components exploring **Deterministic Governance** patterns and **System-Aware Security**.

## 🚀 Technical Proof-of-Concept
This repository contains functional demos of the ReliantOps architectural concepts, focusing on contextual command validation and statistical anomaly detection.

### 1. Contextual Veto Engine (`guardrails_demo.py`)
Demonstrates a **System-Aware Veto** logic. Unlike static blacklists, it evaluates real-time system state (CPU load via `os.getloadavg`) before deciding whether a command trajectory is safe.
- **Latency:** Measured using `time.perf_counter_ns()`. Decisions typically execute in sub-millisecond timeframes in local environments.

### 2. Statistical Anomaly Detector (`Detector_demo.py`)
Implements an outlier detection engine using a standard **Z-Score (Sigma-2)** algorithm. It identifies system perturbations based on real-time standard deviation.

### 3. Automated Testing (`test_reliantops.py`)
We use `pytest` to ensure that security invariants (like blocking root destruction or critical resource exhaustion) are consistently preserved.

## 🛠️ Installation & Usage
```bash
# Clone the repository
git clone https://github.com/melwalk2310/ReliantOpsDEMO
cd ReliantOpsDEMO

# Install dependencies
pip install pytest

# Run the demos
python guardrails_demo.py
python Detector_demo.py

# Run the tests
pytest test_reliantops.py

