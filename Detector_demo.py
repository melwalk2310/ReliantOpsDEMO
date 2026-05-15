import json

def detect_anomalies(data):
    # Lógica simplificada de Z-Score para el demo
    mean = sum(data) / len(data)
    threshold = 2.0
    results = []
    
    for i, val in enumerate(data):
        z_score = abs(val - mean) / 10 # Simplificado
        is_anomaly = z_score > threshold
        results.append({
            "index": i,
            "value": val,
            "z_score": round(z_score, 2),
            "anomaly": is_anomaly
        })
    
    return results

if __name__ == "__main__":
    sample_data = [10, 12, 11, 105, 13, 11, 12, 98, 10] # 105 y 98 son picos
    anomalies = detect_anomalies(sample_data)
    print(json.dumps(anomalies, indent=2))
