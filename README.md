# 🩺 Doctor AI Agent
Doctor AI Agent is a intelligent medical assistant in Portuguese that performs preliminary patient assessments and delivers concise, data-driven insights.

[**Try it now**](https://medic-agent.streamlit.app/)

## 🧠 Technologies Used
- Python 3.11.5
- [Streamlit]("https://streamlit.io/")
- [LangChain]("https://www.langchain.com/")
- [CrewAI]("https://www.crewai.com/")
  
## Agent Components
```bash
| Component                | Description                                                                                                            |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **LLM Backbone**         | OpenAI GPT-4 (via `Github Models`) – Handles medical reasoning, triage logic, and natural language generation. |
| **Conversational Chain** | Uses `CrewAI Agent` with a custom `ConversationalAgent` logic.                                    |
| **Prompt Layer**         | Domain-specific prompt templates crafted to guide medical inference .                           |
| **Tools**                | Adds web-enhanced capabilities using LangChain's Tool abstraction (detailed below).                                    |
| **Streamlit Frontend**   | Provides interactive UI for symptom input and displaying results.                                                      |
```
## 🚀 Running Locally

To run the project locally, follow the steps below:

  ```bash
  # 1. Clone the repository
  git clone https://github.com/your-username/doctor-ai-agent.git
  cd doctor-ai-agent

  # 2. (Optional) Create and activate a virtual environment
  python -m venv venv
  source venv/bin/activate        # On Linux/macOS
  .\venv\Scripts\activate       # On Windows

  # 3. Install dependencies
  pip install -r requirements.txt

  # 4. Launch the application
  streamlit run Homepage.py
  ```


