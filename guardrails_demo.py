import sys
import time

def simulate_guardrail(command):
    dangerous_commands = ["rm -rf", "format c:", "mkfs"]
    print(f"[INPUT] Executing: {command}")
    time.sleep(0.5) # Simular procesamiento de 0.15ms (en demo se nota más con pausa)
    
    for dc in dangerous_commands:
        if dc in command:
            print(f"\033[91m[VETO] Command '{command}' BLOCKED by ReliantOps Guardrail.\033[0m")
            print(f"[LOG] Security Event logged: {time.strftime('%Y-%m-%dT%H:%M:%SZ')}")
            return False
    
    print("\033[92m[PASS] Command allowed.\033[0m")
    return True

if __name__ == "__main__":
    test_cmd = "rm -rf /data"
    simulate_guardrail(test_cmd)
