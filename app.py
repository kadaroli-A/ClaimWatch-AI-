# app.py

import time
import streamlit as st
from engine import (
    CLAIM_DATABASE,
    identity_verification_agent,
    policy_consistency_agent,
    risk_feature_agent,
    fraud_scoring_agent,
    recommendation_agent
)

# -------------------------------------------------
# SESSION STATE INITIALIZATION (CRITICAL)
# -------------------------------------------------
if "stage" not in st.session_state:
    st.session_state.stage = 1

if "claim_id" not in st.session_state:
    st.session_state.claim_id = None

if "mobile" not in st.session_state:
    st.session_state.mobile = None

if "score" not in st.session_state:
    st.session_state.score = None

if "action" not in st.session_state:
    st.session_state.action = None


# -------------------------------------------------
# PAGE 1 — CLAIM INTAKE
# -------------------------------------------------
if st.session_state.stage == 1:
    st.title("ClaimWatch-X 🛡️")
    st.caption("Enterprise Insurance Claim Verification System")

    st.subheader("🔐 Claim Intake")

    mobile = st.text_input("Registered Mobile Number", placeholder="10-digit mobile number")
    claim_id = st.text_input("Insurance Claim ID", placeholder="CLM-2024-1001")

    if st.button("Verify & Proceed"):
        st.session_state.mobile = mobile
        st.session_state.claim_id = claim_id
        st.session_state.stage = 2
        st.rerun()


# -------------------------------------------------
# PAGE 2 — AGENTIC INVESTIGATION WORKFLOW
# -------------------------------------------------
if st.session_state.stage == 2:
    st.title("🤖 Multi-Agent Fraud Investigation")

    claim_id = st.session_state.claim_id
    mobile = st.session_state.mobile

    progress = st.progress(0)

    # -------- AGENT 1: Identity Verification --------
    with st.status("Identity Verification Agent", expanded=True) as status_box:
        valid, checks = identity_verification_agent(claim_id, mobile)

        for check, result in checks.items():
            st.write(f"{check}: {'✅' if result else '❌'}")

        time.sleep(3)
        status_box.update(state="complete" if valid else "error")
        progress.progress(20)

    if not valid:
        st.session_state.score = 1.0
        st.session_state.action = "BLOCK CLAIM — INVALID IDENTIFICATION"
        st.session_state.stage = 3
        st.rerun()

    claim = CLAIM_DATABASE[claim_id]

    # -------- AGENT 2: Policy Consistency --------
    with st.status("Policy Consistency Agent", expanded=True) as status_box:
        policy_flags = policy_consistency_agent(claim)

        for k, v in policy_flags.items():
            st.write(f"{k}: {v}")

        time.sleep(3)
        status_box.update(state="complete")
        progress.progress(40)

    # -------- AGENT 3: Risk Feature Engineering --------
    with st.status("Risk Feature Agent", expanded=True) as status_box:
        features = risk_feature_agent(policy_flags, claim["previous_claims"])

        for k, v in features.items():
            st.write(f"{k}: {v}")

        time.sleep(3)
        status_box.update(state="complete")
        progress.progress(60)

    # -------- AGENT 4: Fraud Scoring --------
    with st.status("Fraud Scoring Agent", expanded=True) as status_box:
        score, level = fraud_scoring_agent(features)

        st.write(f"Fraud Probability: {score}")
        st.write(f"Risk Level: {level}")

        time.sleep(3)
        status_box.update(state="complete")
        progress.progress(80)

    # -------- AGENT 5: Recommendation --------
    with st.status("Recommendation Agent", expanded=True) as status_box:
        action = recommendation_agent(score)

        st.write(f"Recommended Action: {action}")

        time.sleep(3)
        status_box.update(state="complete")
        progress.progress(100)

    st.session_state.score = score
    st.session_state.action = action
    st.session_state.stage = 3
    st.rerun()


# -------------------------------------------------
# PAGE 3 — FINAL DECISION
# -------------------------------------------------
if st.session_state.stage == 3:
    st.title("📊 Final Fraud Decision")

    if st.session_state.score is None:
        st.error("No analysis found. Please restart verification.")
        st.stop()

    if st.session_state.score >= 0.7:
        st.error("🚨 HIGH FRAUD RISK DETECTED")
    elif st.session_state.score >= 0.4:
        st.warning("⚠️ MEDIUM FRAUD RISK")
    else:
        st.success("✅ CLAIM VERIFIED SUCCESSFULLY")

    st.metric("Fraud Probability", st.session_state.score)
    st.markdown(f"### 🧾 Recommended Action: **{st.session_state.action}**")

    if st.button("🔁 Start New Verification"):
        st.session_state.stage = 1
        st.session_state.score = None
        st.session_state.action = None
        st.rerun()