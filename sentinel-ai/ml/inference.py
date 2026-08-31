from app.detection.anomaly_detector import AnomalyDetector

def predict(event: dict):
    return AnomalyDetector().predict(event)

if __name__ == "__main__":
    sample = {
        "failed_logins": 20,
        "requests_per_minute": 300,
        "connections": 90,
        "bytes_transferred": 20_000_000,
        "hour": 2,
    }
    print(predict(sample))
