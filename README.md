# 🩺 Doctor AI Agent
Doctor AI Agent is a intelligent medical assistant in Portuguese that performs preliminary patient assessments and delivers concise, data-driven insights.

[**Try it now**](https://medic-agent.streamlit.app/)

---

## 🧠 Technologies Used
- Python 3.11.5
- [Streamlit]("https://streamlit.io/")
- [LangChain]("https://www.langchain.com/")
- [CrewAI]("https://www.crewai.com/")
  
## 🧠 Agent Architecture (Detailed)

The Doctor AI Agent is designed as a modular, reasoning-first medical assistant that leverages Large Language Models (LLMs) enhanced by external tools for real-time medical knowledge retrieval.

---

### 🔧 Core Components

| Component                | Description                                                                                                            |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **LLM Backbone**         | OpenAI GPT-4 (via `Github Models`) – Handles medical reasoning, triage logic, and natural language generation.         |
| **Conversational Chain** | Built using the `CrewAI` framework with a custom `ConversationalAgent` logic for task delegation and memory handling.  |
| **Prompt Layer**         | Domain-specific prompt templates crafted to guide medical inference and decision-making.                               |
| **Tools**                | Web-enhanced capabilities via LangChain Tool abstraction, including search and scraping (see below).                   |
| **Streamlit Frontend**   | Provides an intuitive interface for symptom input and returns structured, explainable medical feedback.                |

---

### 🛠️ Tools Overview

The agent leverages tools to enhance factual accuracy and access real-time information:

#### 🔍 DuckDuckGo Search Tool
- **Function**: Performs real-time web searches for symptoms, conditions, and recent health-related updates.
- **Implementation**: `DuckDuckGoSearchResults` via LangChain.
- **Purpose**: Assists the agent in retrieving recent or unknown data not embedded in the model.

#### 🧪 Web Scraping Tool
- **Function**: Extracts medical content from trusted sources using `requests` + `BeautifulSoup`.
- **Safeguards**: Domain whitelisting ensures reliability and medical accuracy.
- **Use Case**: Activated when high-precision, structured information is needed (e.g., MedlinePlus or NIH articles).

---
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


