# ReliantOps | Real-Time Security Automation

Technical demos focused on **System-Aware Governance**.

## 🛠️ Real-Time Veto Engine (`guardrails_demo.py`)
- **Metric Source:** Reads real system load via `os.getloadavg()`.
- **Performance:** Measured using `time.perf_counter_ns()`.
- **Logic:** Contextual Veto based on CPU state + Command Trajectory.

## ✅ Automated Testing
We use `pytest` to ensure architectural invariants are preserved.
```bash
pip install pytest
pytest demo/test_reliantops.py

