from pathlib import Path
import numpy as np
import pandas as pd

def main():
    rng = np.random.default_rng(42)
    n_normal = 1500
    n_anomaly = 150

    normal = pd.DataFrame({
        "failed_logins": rng.poisson(1, n_normal),
        "requests_per_minute": rng.normal(25, 8, n_normal).clip(0),
        "connections": rng.normal(8, 3, n_normal).clip(0),
        "bytes_transferred": rng.normal(150_000, 50_000, n_normal).clip(0),
        "hour": rng.integers(7, 23, n_normal),
    })

    anomaly = pd.DataFrame({
        "failed_logins": rng.integers(12, 50, n_anomaly),
        "requests_per_minute": rng.integers(130, 500, n_anomaly),
        "connections": rng.integers(55, 180, n_anomaly),
        "bytes_transferred": rng.integers(10_000_000, 100_000_000, n_anomaly),
        "hour": rng.integers(0, 7, n_anomaly),
    })

    df = pd.concat([normal, anomaly], ignore_index=True)
    out = Path("data/raw/security_events.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print(f"Dataset saved to {out} ({len(df)} rows)")

if __name__ == "__main__":
    main()
