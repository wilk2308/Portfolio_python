import streamlit as st
from PIL import Image

# Configuração inicial
st.set_page_config(page_title="Portfólio de William", page_icon="🚀", layout="wide")

# Seção de Introdução
st.title("👨‍💻 William - Desenvolvedor Python e Especialista em Automação")
st.subheader("Automação, Integração de Sistemas e Desenvolvimento de APIs")

# Exibir foto de perfil ou logo
imagem_perfil = Image.open("imagens/logo.png")
st.image(imagem_perfil, width=250)

# Seção: Sobre Mim
st.header("Sobre Mim")
st.write("""
Sou um desenvolvedor especializado em Python com foco em automação de processos corporativos, desenvolvimento de APIs e criação de dashboards interativos. Tenho experiência em:
- Desenvolvimento de APIs com Flask e FastAPI
- Automação de tarefas com Python
- Dashboards interativos com Streamlit e Plotly
- Integração com bancos de dados SQL
""")

# Seção: Projetos
st.header("🚀 Projetos em Destaque")

projetos = {
    "API em Flask": "projetos/api_flask.py",
    "Automação de Tarefas": "projetos/automacao_tarefas.py",
    "Dashboard Interativo": "projetos/dashboard_streamlit.py",
}

for nome, caminho in projetos.items():
    st.subheader(f"📌 {nome}")
    st.code(open(caminho, 'r').read()[:200] + '...', language='python')
    st.button(f"Ver Projeto Completo ({nome})", key=nome)

# Seção: Contato
st.header("📬 Contato")
st.write("💼 [LinkedIn](https://linkedin.com/in/seu-linkedin)")
st.write("💻 [GitHub](https://github.com/seu-github)")
st.write("✉️ E-mail: seuemail@example.com")
