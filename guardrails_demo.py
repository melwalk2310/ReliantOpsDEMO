import time
import os

def get_real_cpu():
    # Obtiene la carga del sistema en Linux/Mac. Fallback a 0 en Windows.
    try:
        return os.getloadavg()[0] * 10 # Carga promedio de 1 min
    except:
        return 20.0 # Valor simulado si no es Linux

def evaluate_trajectory(command):
    # Medir latencia en nanosegundos
    start_time = time.perf_counter_ns()
    
    cpu_load = get_real_cpu()
    print(f"[OS_METRICS] Real CPU Load: {cpu_load:.2f}")
    
    # Lógica de Veto Contextual
    veto = False
    reason = ""
    
    if cpu_load > 8.0 and "stress" in command: # Si la carga es > 80% (escala 0-10)
        veto = True
        reason = "System resources critical. High-load trajectory blocked."
    
    if "rm -rf /" in command:
        veto = True
        reason = "Forbidden root trajectory detected."
    
    end_time = time.perf_counter_ns()
    latency_ns = end_time - start_time
    
    return {
        "status": "VETO" if veto else "ALLOWED",
        "reason": reason,
        "latency_ns": latency_ns,
        "latency_ms": latency_ns / 1_000_000
    }

if __name__ == "__main__":
    print("--- ReliantOps Real-Time Veto Engine ---")
    result = evaluate_trajectory("rm -rf /data")
    print(f"Result: {result['status']} | {result['reason']}")
    print(f"Latency: {result['latency_ns']} ns ({result['latency_ms']:.4f} ms)")
