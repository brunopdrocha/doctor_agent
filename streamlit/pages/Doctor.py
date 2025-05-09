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

# Variáveis de estado iniciais
if "show_report" not in st.session_state:
    st.session_state.show_report = False
if "resultado" not in st.session_state:
    st.session_state.resultado = ""

# Função de reset
def reset_report():
    st.session_state.show_report = False
    st.session_state.resultado = ""
    # limpa também os inputs para forçar novo preenchimento
    st.session_state.user_api_key = ""
    st.session_state.sintomas = ""

# Título App
st.title("🩺Doctor Agent")
st.markdown(""" Para realizar sua análise necesita criar uma **API key no GitHub Models**. Clique no botão abaixo para gerar sua chave.""")

st.link_button("Github Models",url="https://github.com/settings/tokens")


# Interface para API key (armazenada em session_state para poder resetar)
user_api_key = st.text_input(
    "Insira sua Api Key:", 
    type="password", 
    key="user_api_key"
)

# Input de sintomas (também em session_state)
sintomas = st.text_area(
    "Descreva seus sintomas:", 
    key="sintomas"
)

# Botão para iniciar análise (só habilitado se ambos os campos estiverem preenchidos)
can_analyze = bool(user_api_key and sintomas)
if not user_api_key:
    st.info("🔑 A API Key é obrigatória para prosseguir.")
elif not sintomas:
    st.info("✍️ Descreva seus sintomas para prosseguir.")

if st.button("Analisar", disabled=not can_analyze):
    # Instancia o agente conforme chave
    doctor = DoctorAgent(api_key=user_api_key)
    
    # Spinner enquanto executa análise
    with st.spinner("Analisando os sintomas..."):
        st.session_state.resultado = doctor.run(sintomas)
        st.session_state.show_report = True

# Exibe laudo se disponível
if st.session_state.show_report:
    st.markdown(st.session_state.resultado)
    st.button("Resetar", on_click=reset_report)

# Rodapé
st.markdown(
    """
    <hr style="margin-top: 50px;"/>
    <div style='text-align: center; padding: 10px 0; color: gray; font-size: 0.9em;'>
        © 2025 Doctor Agent | Developed by Bruno Pilão da Rocha
    </div>
    """,
    unsafe_allow_html=True
)
