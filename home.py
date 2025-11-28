# Home.py

import streamlit as st
import datetime
import base64
import requests

# URL do seu logo (a mesma usada nas calculadoras)
URL_LOGO_WHITE = "https://ik.imagekit.io/aufhkvnry/logo-traders__bg-white.png"
COR_PRIMARIA_FORM = '#6B48FF' 

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
    max-width: 60% !important; 
    padding-left: 2rem;
    padding-right: 2rem;
}
/* Centraliza o logo na home */
.stMarkdown > div > img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    max-width: 450px; 
    height: auto;
    margin-bottom: 20px;
}
/* Estilo para os cards do menu (opcional, apenas para embelezar) */
.menu-card {
    border: 1px solid #e6e6e6;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    background-color: #f9f9f9;
    transition: transform 0.2s;
}
.menu-card:hover {
    transform: translateY(-5px);
    box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.15);
}
</style>
""", unsafe_allow_html=True)


## ⚡ Traders | Menu Principal de Ferramentas

# Exibição do Logo (Opcional, se quiser)
st.markdown(
    f"""<div style="text-align: center;">
        <img src="{URL_LOGO_WHITE}"> 
    </div>""",
    unsafe_allow_html=True
)

st.markdown(f"<h3 style='text-align: center; color: #222222; margin-bottom: 30px;'>Selecione uma calculadora para começar a simulação:</h3>", unsafe_allow_html=True)

st.markdown("---")


# === CARDS DE NAVEGAÇÃO ===
# Usaremos a barra lateral padrão do Streamlit para navegação, mas os botões abaixo 
# servem como um menu visual na página principal.

col1, col2 = st.columns(2)

# Card 1: Calculadora de CDB Simples
with col1:
    st.markdown(
        f"""
        <div class="menu-card">
            <h4 style='color: {COR_PRIMARIA_FORM};'>📈 1. Calculadora de CDB Simples</h4>
            <p>Simulação básica de investimento em um único Certificado de Depósito Bancário (CDB). Ideal para cenários simplificados e análise de tributação.</p>
            <p><i>Acesse no menu lateral: <b>1 CDB Simples</b></i></p>
        </div>
        """, unsafe_allow_html=True
    )

# Card 2: Calculadora de Secundários (Multi Ativos)
with col2:
    st.markdown(
        f"""
        <div class="menu-card">
            <h4 style='color: {COR_PRIMARIA_FORM};'>📊 2. Calculadora de Secundários</h4>
            <p>Simulação consolidada de múltiplos papéis (CDBs Secundários), permitindo projeções de liquidez, tributação e rentabilidade total da carteira.</p>
            <p><i>Acesse no menu lateral: <b>2 Secundarios Multi</b></i></p>
        </div>
        """, unsafe_allow_html=True
    )

st.markdown("---")

st.info("Para navegar entre as calculadoras, utilize a **barra lateral** que o Streamlit gerou automaticamente. Se a barra estiver oculta, clique na seta `>` no canto superior esquerdo.")
