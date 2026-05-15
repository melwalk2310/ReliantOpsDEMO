import statistics
import json

def detect_anomalies(data):
    if len(data) < 2: return []
    
    mean = statistics.mean(data)
    std_dev = statistics.stdev(data)
    threshold = 2.0 # Sigma-2 threshold
    
    results = []
    for i, val in enumerate(data):
        # Calculate real Z-Score
        z_score = abs(val - mean) / std_dev if std_dev > 0 else 0
        results.append({
            "index": i,
            "value": val,
            "z_score": round(z_score, 2),
            "anomaly": z_score > threshold
        })
    return results

if __name__ == "__main__":
    print("--- ReliantOps Statistical Engine (Z-Score) ---")
    data = [12, 11, 13, 12, 105, 11, 12, 98, 11, 12]
    anomalies = detect_anomalies(data)
    print(json.dumps(anomalies, indent=2))
    
    found = [a["value"] for a in anomalies if a["anomaly"]]
    print(f"\n[RESULT] Identified anomalies: {found}")
