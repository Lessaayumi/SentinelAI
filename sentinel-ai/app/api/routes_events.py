from datetime import datetime, timezone
from fastapi import APIRouter
from app.schemas.event import SecurityEvent
from app.detection.rule_engine import evaluate_rules
from app.detection.risk_engine import calculate_risk
from app.detection.anomaly_detector import AnomalyDetector

router = APIRouter(prefix="/events", tags=["events"])
_detector = AnomalyDetector()

@router.post("/analyze")
def analyze_event(event: SecurityEvent):
    payload = event.model_dump()
    rules = evaluate_rules(payload)
    anomaly = _detector.predict(payload)
    risk = calculate_risk(rules, anomaly)

    return {
        "event_id": event.event_id,
        "analyzed_at": datetime.now(timezone.utc).isoformat(),
        "rules": rules,
        "anomaly": anomaly,
        "risk": risk
    }
