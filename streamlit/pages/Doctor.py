
# Bibliotecas para o streamlit
import streamlit as st
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
from agent.crewAgent import DoctorAgent

# Página config
st.set_page_config(
    page_title="Doctor AI Agent",
    page_icon="🩺",
    layout="wide"
)

# Titulo App 
st.title("Doctor Agent")


# Interface para API key
user_api_key = st.text_input("Insert your Api Key:", type="password")


# Botão para iniciar análise
sintomas = st.text_area("Describe your symptoms:")
if st.button("Analise"):
    # Verifica se tem key do usuário
    if user_api_key:
        # Cria o agente com a chave do usuário
        doctor = DoctorAgent(api_key=user_api_key)
    else:
        # Usa a chave padrão do .env
        doctor = DoctorAgent()
    
    # Executa a análise
    resultado = doctor.run(sintomas)
    st.markdown(resultado)