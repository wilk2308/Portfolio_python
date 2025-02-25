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
- Dashboards interativos com Streamlit, Dash e Plotly
- Integração com bancos de dados SQL
""")

# Seção: Projetos
st.header("🚀 Projetos em Destaque")

projetos = {
    "DocumentGPT": {
        "descricao": "🔍 Um sistema inteligente para leitura e análise automatizada de documentos, utilizando NLP e Machine Learning.",
        "link": "https://github.com/wilk2308/DocumentGPT"
    },
    "Portfolio Python": {
        "descricao": "🌐 Meu portfólio desenvolvido em Python usando Streamlit, exibindo projetos e experiências profissionais.",
        "link": "https://github.com/wilk2308/Portfolio_python"
    },
    "AI-PoweredSQLQuery": {
        "descricao": "🤖 Projeto de automação SQL com integração de inteligência artificial para executar queries de maneira inteligente.",
        "link": "https://github.com/wilk2308/AI-PoweredSQLQuery"
    },
    "Dash Indicadores": {
        "descricao": "📊 Dashboard corporativo interativo usando Dash e Plotly, exibindo indicadores de desempenho por áreas como Jurídico, RH e Atendimento.",
        "link": "https://github.com/wilk2308/Dash_Indicadores"
    },
    "RD Automação Leads": {
        "descricao": "🔗 Automação de leads do RD Station com envio de mensagens via WhatsApp usando PyWhatKit e integração com API do Twilio.",
        "link": "https://github.com/wilk2308/RD_AutomacaoLeads"
    }
}

# Exibir os projetos
for nome, dados in projetos.items():
    st.subheader(f"📌 {nome}")
    st.write(dados['descricao'])
    st.write(f"🔗 [Ver no GitHub]({dados['link']})")

# Seção: Contato
st.header("📬 Contato")
st.write("💼 [LinkedIn](https://linkedin.com/in/williamsousa-dev/)")
st.write("💻 [GitHub](https://github.com/wilk2308)")
st.write("✉️ E-mail: william.sousa@wfitech.com.br")
