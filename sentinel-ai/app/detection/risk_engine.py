def calculate_risk(rules: dict, anomaly: dict) -> dict:
    rule_score = float(rules.get("score", 0))
    anomaly_score = float(anomaly.get("risk_contribution", 0))

    total = round(min(rule_score + anomaly_score, 100), 2)

    if total >= 80:
        level = "CRITICAL"
    elif total >= 60:
        level = "HIGH"
    elif total >= 30:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "score": total,
        "level": level
    }
