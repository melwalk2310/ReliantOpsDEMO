import time

def evaluate_trajectory(command, system_state):
    """
    Veto logic based on State + Command (Trajectory).
    Rule: If CPU is critical, any high-load command is VETOED.
    """
    print(f"\n[SYSTEM_STATE] CPU: {system_state['cpu']}% | Mem: {system_state['mem']}%")
    print(f"[ACTION] Requested: {command}")
    
    # Logic: Contextual Veto
    if system_state['cpu'] > 80 and "stress" in command:
        return "VETO: Resource exhaustion trajectory detected. CPU is at critical levels."
    
    if "rm -rf /" in command:
        return "VETO: Destructive root trajectory detected. Operation forbidden."
        
    return "ALLOWED"

if __name__ == "__main__":
    print("--- ReliantOps Contextual Veto Engine ---")
    # Escenario 1: Comando normal con sistema sano
    print(f"Result: {evaluate_trajectory('ls -la', {'cpu': 15, 'mem': 30})}")
    
    # Escenario 2: Comando de carga con sistema CRÍTICO (TRAYECTORIA)
    print(f"Result: {evaluate_trajectory('stress-ng --cpu 4', {'cpu': 85, 'mem': 40})}")
