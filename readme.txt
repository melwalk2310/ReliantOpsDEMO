# ReliantOps GEN-369 | Engineering Demos

This is not a "blacklist" or a simple script. These demos illustrate the **Deterministic Veto Logic** and **Statistical Anomaly Detection** used in the Sovereign Kernel.

### 🧠 Contextual Veto (Trajectory)
Unlike static firewalls, ReliantOps evaluates the **System State** before a command is executed.
- `guardrails_demo.py`: Demonstrates a Veto triggered by **Context** (High CPU + Stress Command).

### 📈 Statistical Engine
- `detector_demo.py`: Implements a standard **Z-Score (Sigma-2)** outlier detection using real-time standard deviation.

### 🛡️ Verified Integrity
All outputs are hash-chained (RSM pattern) in the full implementation to ensure forensic auditability.
