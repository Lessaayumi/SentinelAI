RULES = {
    "brute_force": lambda e: e["failed_logins"] >= 10,
    "api_abuse": lambda e: e["requests_per_minute"] >= 120,
    "connection_spike": lambda e: e["connections"] >= 50,
    "high_transfer": lambda e: e["bytes_transferred"] >= 10_000_000,
}

WEIGHTS = {
    "brute_force": 35,
    "api_abuse": 30,
    "connection_spike": 20,
    "high_transfer": 15,
}

def evaluate_rules(event: dict) -> dict:
    triggered = []
    score = 0

    for name, rule in RULES.items():
        if rule(event):
            triggered.append(name)
            score += WEIGHTS[name]

    return {
        "triggered": triggered,
        "score": min(score, 100)
    }
