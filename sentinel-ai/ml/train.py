from pathlib import Path
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

FEATURES = [
    "failed_logins",
    "requests_per_minute",
    "connections",
    "bytes_transferred",
    "hour",
]

def main():
    dataset = Path("data/raw/security_events.csv")
    if not dataset.exists():
        from data.generate_dataset import main as generate
        generate()

    df = pd.read_csv(dataset)

    # Treinamento não supervisionado: somente o baseline normal.
    normal = df[
        (df["failed_logins"] < 10) &
        (df["requests_per_minute"] < 120) &
        (df["connections"] < 50) &
        (df["bytes_transferred"] < 10_000_000)
    ]

    model = IsolationForest(
        n_estimators=200,
        contamination=0.08,
        random_state=42
    )
    model.fit(normal[FEATURES])

    output = Path("ml/models/isolation_forest.joblib")
    output.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output)
    print(f"Model saved to {output}")
    print(f"Training samples: {len(normal)}")

if __name__ == "__main__":
    main()
