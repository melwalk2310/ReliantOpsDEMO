import statistics
import json

def detect_anomalies(data):
    if len(data) < 2: return []
    mean = statistics.mean(data)
    std_dev = statistics.stdev(data)
    threshold = 2.0 # Standard Sigma-2
    
    results = []
    for i, val in enumerate(data):
        z_score = abs(val - mean) / std_dev if std_dev > 0 else 0
        results.append({
            "index": i, "value": val,
            "z_score": round(z_score, 2),
            "anomaly": z_score > threshold
        })
    return results

if __name__ == "__main__":
    print("--- ReliantOps Statistical Engine (Z-Score) ---")
    data = [12, 11, 13, 12, 105, 11, 12, 98, 11, 12]
    print(json.dumps(detect_anomalies(data), indent=2))

