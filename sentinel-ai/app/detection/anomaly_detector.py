from pathlib import Path
import numpy as np

FEATURES = [
    "failed_logins",
    "requests_per_minute",
    "connections",
    "bytes_transferred",
    "hour",
]

class AnomalyDetector:
    def __init__(self, model_path="ml/models/isolation_forest.joblib"):
        self.model = None
        path = Path(model_path)
        if path.exists():
            import joblib
            self.model = joblib.load(path)

    def predict(self, event: dict) -> dict:
        if self.model is None:
            return {
                "is_anomaly": False,
                "score": 0.0,
                "risk_contribution": 0.0,
                "status": "model_not_trained"
            }

        values = np.array([[event.get(feature, 0) for feature in FEATURES]])
        prediction = int(self.model.predict(values)[0])
        decision = float(self.model.decision_function(values)[0])

        is_anomaly = prediction == -1
        contribution = 40.0 if is_anomaly else 0.0

        return {
            "is_anomaly": is_anomaly,
            "score": round(decision, 4),
            "risk_contribution": contribution,
            "status": "ok"
        }
