from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_event():
    payload = {
        "event_id": "evt-001",
        "timestamp": "2026-08-31T14:00:00Z",
        "source_ip": "192.0.2.10",
        "event_type": "authentication",
        "failed_logins": 20,
        "requests_per_minute": 250,
        "connections": 80,
        "bytes_transferred": 20_000_000,
        "hour": 2
    }

    response = client.post("/api/v1/events/analyze", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "risk" in body
    assert body["risk"]["level"] in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}
