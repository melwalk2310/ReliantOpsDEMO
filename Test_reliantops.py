import pytest
from guardrails_demo import evaluate_trajectory

def test_root_veto():
    result = evaluate_trajectory("rm -rf /")
    assert result["status"] == "VETO"
    assert "root" in result["reason"]

def test_normal_command():
    # Simulamos comando normal
    result = evaluate_trajectory("ls -la")
    assert result["status"] == "ALLOWED"

def test_performance_threshold():
    # Verificamos que el veto sea rápido (< 1ms)
    result = evaluate_trajectory("test")
    assert result["latency_ms"] < 1.0
