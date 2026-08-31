from app.detection.rule_engine import evaluate_rules

def test_brute_force_rule():
    event = {
        "failed_logins": 15,
        "requests_per_minute": 10,
        "connections": 2,
        "bytes_transferred": 1000,
    }
    result = evaluate_rules(event)
    assert "brute_force" in result["triggered"]
    assert result["score"] >= 35
