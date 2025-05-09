import streamlit as st
import sys,os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

# Página config
st.set_page_config(
    page_title="Doctor AI Agent",
    page_icon="🩺",
    layout="wide"
)

# Cabeçalho
st.title("🩺 Doctor AI Agent")
st.markdown(
    """
Welcome to **Doctor AI Agent**, your intelligent medical assistant in Portuguese. This tool performs preliminary patient assessments and delivers concise, data-driven insights.

To begin, you’ll need a **GitHub Models API key**—click the button below to generate your key.

When you’re ready to try it out, select **Doctor** from the menu in the top-left corner.
"""
)

st.link_button("Github Models",url="https://github.com/settings/tokens")

st.markdown("---")

# 🌟 Project Overview
st.header("🌟 Project Overview")
st.markdown(
    """
Doctor AI Agent is a state-of-the-art conversational agent that simulates a physician’s diagnostic reasoning. By combining natural language understanding, evidence-based medicine, and secure patient data handling, it:

- **Gathers** symptoms and medical history through an intuitive chat interface  
- **Analyzes** inputs against clinical guidelines and statistical models  
- **Generates** a structured medical report with differential diagnoses, recommendations, and urgency level  
"""
)

# 🎯 Goals & Benefits
st.header("🎯 Goals & Benefits")
st.markdown(
    """
1. **Faster Triage**  
   Streamline the initial patient intake process by automating symptom collection and risk stratification.  
2. **Consistency & Accuracy**  
   Reduce variability in preliminary assessments by anchoring recommendations to up-to-date clinical protocols.  
3. **Enhanced Patient Engagement**  
   Offer patients clear, empathetic explanations of their condition and next steps.  
4. **Clinical Decision Support**  
   Empower healthcare professionals with a second-opinion tool that highlights atypical presentations and rare conditions.  
"""
)

# 🔍 Core Features
st.header("🔍 Core Features")
st.markdown(
    """
| Feature                            | Description                                                                 |
|------------------------------------|-----------------------------------------------------------------------------|
| **Symptom Collection**             | Interactive Q&A to capture onset, duration, intensity, and related factors  |
| **Medical History Integration**    | Queries past diagnoses, medications, allergies, and lifestyle elements      |
| **Differential Diagnosis Engine**  | Ranks possible conditions by probability, flagging “red flag” symptoms      |
| **Report Generation**              | Produces a PDF/HTML summary with charts, lab-test suggestions, and advice   |
| **Urgency & Triage Alarm**         | Color-coded risk levels (low/medium/high), with automated alerts for EMS    |
| **Multi-Language Support**         | English and Portuguese interfaces (coming soon)                             |
"""
)

# 🏗️ System Architecture
st.header("🏗️ System Architecture")
st.code(
    """
[User Chat UI] ──▶ [CrewAI Agent] ──▶ [Web Search Tool] ──▶ [Symptom Analyzer] ──▶ [Clinical Knowledge Base]
                                             │
                                             ▼
                                    [Differential Diagnosis Engine]
                                             │
                                             ▼
                                   [Report & Recommendation Generator]
""",
    language="text"
)
st.markdown(
    """
1. **NLU Module**  
   - Uses transformer models (e.g. GPT-4) fine-tuned on medical dialogues  
2. **Clinical Knowledge Base**  
   - Encodes guidelines from WHO, CDC, and peer-reviewed journals  
3. **Diagnosis Engine**  
   - Bayesian network + rule-based filters to propose ranked conditions  
4. **UI & Reporting**  
   - Streamlit front-end for interactive use; REST API for integration  
"""
)

# 🚀 Getting Started


        
st.header("GitHub Repository")
st.markdown(
    """
   ```bash
 https://github.com/brunopdrocha/doctor_agent
   """
   )

st.markdown(
    """
    <hr style="margin-top: 50px;"/>
    <div style='text-align: center; padding: 10px 0; color: gray; font-size: 0.9em;'>
        © 2025 Doctor Agent | Developed by Bruno Pilão da Rocha
    </div>
    """,
    unsafe_allow_html=True
)
