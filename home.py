# Home.py

import streamlit as st
import datetime
import base64
import requests

# URLs das suas calculadoras deployadas
URL_CDB_SIMPLES = "https://calculadora-cdb-8bwhu49bmy9ajscylmtrcv.streamlit.app/"
URL_SECUNDARIOS_MULTI = "https://secundarios-qgwpgzdbarxujsm3hqpweg.streamlit.app/"

# URL do seu logo
URL_LOGO_WHITE = "https://ik.imagekit.io/aufhkvnry/logo-traders__bg-white.png"
COR_PRIMARIA_FORM = '#6B48FF' 
TEXTO_PRINCIPAL_ST = "#222222"

# Configuração da página
st.set_page_config(
    page_title="Menu Principal - Traders",
    layout="wide"
)

# Injeção de CSS para centralizar e formatar
st.markdown("""
<style>
/* Limita a largura da coluna principal */
.main .block-container {
    max-width: 70% !important; 
    padding-left: 2rem;
    padding-right: 2rem;
}
/* Centraliza o logo na home */
.logo-container img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    max-width: 450px; 
    height: auto;
    margin-bottom: 20px;
}
/* Estilo para os botões de link */
.stButton>button {
    background-color: #6B48FF; 
    color: white; 
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 18px;
    font-weight: bold;
    border: none;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s;
    width: 100%; /* Ocupa a largura da coluna */
}
.stButton>button:hover {
    background-color: #5A3CD9;
}
</style>
""", unsafe_allow_html=True)


## ⚡ Traders | Menu Principal de Ferramentas

st.markdown(
    f"""<div class="logo-container">
        <img src="{URL_LOGO_WHITE}"> 
    </div>""",
    unsafe_allow_html=True
)

st.markdown(f"<h3 style='text-align: center; color: {TEXTO_PRINCIPAL_ST}; margin-bottom: 30px;'>Selecione uma calculadora para acessar:</h3>", unsafe_allow_html=True)

st.markdown("---")


# === LINKS DE NAVEGAÇÃO USANDO BOTÕES EM MARKDOWN ===
col1, col2 = st.columns(2)

# Função para criar o botão-link em Markdown/HTML
def create_link_button(url, label, icon):
    return f"""
    <div style='text-align: center; padding: 20px; border: 1px solid #e6e6e6; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.05); margin-bottom: 20px;'>
        <h4 style='color: {COR_PRIMARIA_FORM}; margin-top: 0;'>{icon} {label}</h4>
        <p>Clique no botão abaixo para abrir a aplicação em uma nova aba.</p>
        <a href='{url}' target='_blank' style='text-decoration: none;'>
            <button style='
                background-color: {COR_PRIMARIA_FORM}; 
                color: white; 
                border: none; 
                padding: 10px 20px; 
                border-radius: 8px; 
                font-size: 16px; 
                cursor: pointer;
                width: 90%;
            '>
                Acessar Calculadora
            </button>
        </a>
    </div>
    """

# Card 1: Calculadora de CDB Simples
with col1:
    st.markdown(create_link_button(
        URL_CDB_SIMPLES, 
        "Calculadora de CDB Simples", 
        "📈"
    ), unsafe_allow_html=True)

# Card 2: Calculadora de Secundários (Multi Ativos)
with col2:
    st.markdown(create_link_button(
        URL_SECUNDARIOS_MULTI, 
        "Calculadora de Secundários (Multi Ativos)", 
        "📊"
    ), unsafe_allow_html=True)

st.markdown("---")

st.info("As calculadoras serão abertas em novas abas do navegador, mantendo este menu principal acessível.")
