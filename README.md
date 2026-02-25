# 🛡️ ClaimWatch-X  
### Explainable Multi-Agent Insurance Fraud Detection System

ClaimWatch-X is an **agentic AI–inspired insurance fraud detection prototype** that demonstrates how real-world insurance claims are evaluated using **multiple independent verification agents**, transparent reasoning, and a final consensus-based decision.

Instead of a single black-box score, ClaimWatch-X shows **how and why** a claim is flagged or approved — step by step.

---

## 🚀 Problem Statement

Insurance companies lose billions annually due to fraudulent claims.  
Most AI-based systems today:

- Rely on opaque, single-model predictions
- Provide little to no explanation
- Are difficult to audit or trust

ClaimWatch-X addresses this by simulating **real insurance investigation workflows** using a **multi-agent decision pipeline** with transparent intermediate outputs.

---

## 🎯 Key Features

- ✅ Multi-step claim verification flow  
- 🤖 Five specialized AI-inspired agents  
- 📊 Transparent, computed risk indicators (not fake animations)  
- 🔍 Human-readable explanations for every decision  
- ⚠️ Fraud escalation instead of blind rejection  
- 🧠 Realistic insurance logic (claim vs premium, tenure, behavior)

---

## 🧠 Agentic Architecture

ClaimWatch-X uses **five independent agents**, each responsible for a specific verification task:

### 1️⃣ Identity Verification Agent
Validates:
- Claim ID format
- Mobile number format
- Claim existence in the system

---

### 2️⃣ Policy Consistency Agent
Computes:
- Claim amount vs premium ratio
- Policy tenure (early claim detection)

Flags high-risk inconsistencies.

---

### 3️⃣ Risk Feature Agent
Derives interpretable risk features:
- High claim ratio flag
- Early policy claim flag
- Frequent claimant flag

---

### 4️⃣ Fraud Scoring Agent
Aggregates risk features into:
- Fraud probability score
- Risk category (LOW / MEDIUM / HIGH)

---

### 5️⃣ Recommendation Agent
Produces a **business-aligned action**:
- Approve claim
- Flag for review
- Escalate to manual investigation

---

## 🖥️ Application Flow

```text
Page 1: Claim Intake (Mobile Number + Claim ID)
        ↓
Page 2: Multi-Agent Investigation (Step-by-Step)
        ↓
Page 3: Final Fraud Decision + Explanation

Each agent runs sequentially with visible outputs and realistic processing time to simulate real-world investigation workflows.

---

## 🛠️ Technology Stack

- Frontend / UI: Streamlit  
- Backend Logic: Python  
- Agent Orchestration: Custom rule-based workflow  
- Architecture Style: Agentic AI (Explainable & Modular)  

> ⚠️ This is a prototype designed for transparency and reasoning, not a production ML deployment.

---

## 📂 Project Structure
claimwatch-x/ │ ├── app.py          # Streamlit UI & agent workflow ├── engine.py       # Core logic & agent implementations ├── run.bat         # Quick run script (Windows) ├── requirements.txt └── README.md
---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
pip install -r requirements.txt
### 2️⃣ Run the application
streamlit run app.py
### 3️⃣ Open in browser
http://localhost:8501/
---

## 🧪 Sample Test Data

### High-Risk (Fraud-Likely) Case
Mobile Number: 9876543210 Claim ID: CLM-2024-1001
Triggers:
- Very high claim-to-premium ratio  
- Early policy claim  
- High fraud probability  
- Escalation to manual investigation  

---

### Low-Risk (Valid) Case
Mobile Number: 9000011111 Claim ID: CLM-2022-3007
Triggers:
- Low claim-to-premium ratio  
- Long policy tenure  
- Low fraud probability  
- Claim approval  

---

## 💡 Why ClaimWatch-X Stands Out

- ❌ Not a chatbot  
- ❌ Not a black-box model  
- ✅ A decision-oriented system  
- ✅ Transparent and explainable  
- ✅ Mirrors enterprise insurance workflows  
- ✅ Demonstrates real Agentic AI reasoning  

---

## 📌 Limitations & Future Scope

- Replace rule-based scoring with trained ML models  
- Add SHAP-based feature explanations  
- Integrate secure databases or blockchain audit logs  
- Extend to real insurer datasets  
- Add investigator / auditor role views  

---

## 🎓 Ideal Use Cases

- Hackathons (Agentic AI / GenAI / AIML tracks)  
- Academic demonstrations  
- Final-year projects  
- Recruiter portfolios  
- AI explainability showcases  

---

## 📜 License

This project is released for **educational and demonstration purposes only**.

---

## ⭐ Status

✅ Code stable  
✅ Demo-ready  
✅ Judge-friendly  
✅ Recruiter-safe  

If you find this project valuable, consider starring ⭐ the repository.
