# engine.py

import re

# ------------------------------
# DEMO CLAIM DATABASE
# ------------------------------
CLAIM_DATABASE = {
    "CLM-2024-1001": {
        "mobile": "9876543210",
        "claim_amount": 120000,
        "premium_amount": 8000,
        "policy_tenure_days": 12,
        "previous_claims": 1
    },
    "CLM-2023-2004": {
        "mobile": "9123456789",
        "claim_amount": 35000,
        "premium_amount": 15000,
        "policy_tenure_days": 420,
        "previous_claims": 0
    },
    "CLM-2022-3007": {
    "mobile": "9000011111",
    "claim_amount": 20000,
    "premium_amount": 15000,
    "policy_tenure_days": 800,
    "previous_claims": 0
}
    }


# ------------------------------
# AGENT 1 — Identity Verification
# ------------------------------
def identity_verification_agent(claim_id, mobile):
    checks = {}

    checks["Claim ID format"] = bool(re.match(r"CLM-\d{4}-\d{4}", claim_id))
    checks["Mobile format"] = bool(re.match(r"\d{10}", mobile))
    checks["Claim exists"] = claim_id in CLAIM_DATABASE

    status = all(checks.values())

    return status, checks


# ------------------------------
# AGENT 2 — Policy Consistency
# ------------------------------
def policy_consistency_agent(claim):
    claim_amount = claim["claim_amount"]
    premium = claim["premium_amount"]
    tenure = claim["policy_tenure_days"]

    ratio = round(claim_amount / premium, 2)

    flags = {
        "Claim/Premium Ratio": ratio,
        "High Ratio Flag": ratio > 10,
        "Early Claim Flag": tenure < 30
    }

    return flags


# ------------------------------
# AGENT 3 — Risk Feature Agent
# ------------------------------
def risk_feature_agent(policy_flags, previous_claims):
    features = {
        "High claim ratio": policy_flags["High Ratio Flag"],
        "Early policy claim": policy_flags["Early Claim Flag"],
        "Frequent claimant": previous_claims >= 2
    }

    return features


# ------------------------------
# AGENT 4 — Fraud Scoring Agent
# ------------------------------
def fraud_scoring_agent(features):
    score = 0.0

    if features["High claim ratio"]:
        score += 0.4
    if features["Early policy claim"]:
        score += 0.3
    if features["Frequent claimant"]:
        score += 0.3

    score = round(min(score, 0.99), 2)

    if score >= 0.7:
        level = "HIGH"
    elif score >= 0.4:
        level = "MEDIUM"
    else:
        level = "LOW"

    return score, level


# ------------------------------
# AGENT 5 — Recommendation Agent
# ------------------------------
def recommendation_agent(score):
    if score >= 0.7:
        return "ESCALATE TO MANUAL INVESTIGATION"
    elif score >= 0.4:
        return "FLAG FOR REVIEW"
    else:
        return "APPROVE CLAIM"