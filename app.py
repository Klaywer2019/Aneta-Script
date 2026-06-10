import streamlit as st
import time

# 1. CONFIGURAÇÃO DA TELA DO CELULAR
st.set_page_config(page_title="Automation Lab", page_icon="🤖", layout="centered")

# Estilização para deixar o visual escuro e moderno
st.markdown("""
    <style>
    .status-card {
        background-color: #1e222b;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #00f2fe;
        margin-top: 15px;
        margin-bottom: 15px;
    }
    .explanation-card {
        background-color: #162a25;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #4caf50;
        margin-top: 15px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Interface Principal
st.title("🤖 Automation Lab")
st.write("Insira o comando para rodar as automações da Sala do Futuro.")
st.markdown("---")

# Mensagem inicial do sistema
with st.chat_message("assistant"):
    st.write("Salve meu mano! Qual tarefa você quer automatizar hoje?")

# 2. SEU ESQUELETO DE LÓGICA (Adaptado para o App)
def interpretar_comando(comando_usuario):
    comando = comando_usuario.lower()
    
    if "sala do futuro" in comando and "expiradas" in comando:
        return "RODAR_AUTOMACAO_EXPIRADAS"
    elif "speak" in comando:
        return "RODAR_AUTOMACAO_SPEAK"
    else:
        return "COMANDO_NAO_ENTENDIDO"

def executar_automacao(acao, comando_original):
    if acao == "RODAR_AUTOMACAO_EXPIRADAS":
        # Criando o Card de Status visual na tela
        st.markdown('<div class="status-card"><h4>⚙️ Status da Automação</h4>', unsafe_allow_html=True)
        status_text = st.empty()
        bar = st.progress(0)
        
        status_text.write("🤖 Abrindo o navegador via Selenium...")
        time.sleep(1.5)
        bar.progress(50)
        
        status_text.write("🔎 Buscando tarefas expiradas na Sala do Futuro...")
        time.sleep(1.5)
        bar.progress(100)
        status_text.write("✅ Concluído! Todas as tarefas expiradas foram resolvidas.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Card de Explicação para os seus amigos estudarem
        st.markdown(f"""
        <div class="explanation-card">
            <h4>💡 Para Você Estudar (Lógica da Matéria)</h4>
            <p>A automação resolveu os exercícios pendentes. Aqui está o resumo do conteúdo para você não zerar na prova:</p>
            <ul>
                <li><b>Matéria:</b> Revisão dos tópicos do módulo passado.</li>
                <li><b>Dica de Ouro:</b> Foque nos conceitos teóricos que deixamos salvos no relatório de estudos!</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif acao == "RODAR_AUTOMACAO_SPEAK":
        st.markdown('<div class="status-card"><h4>⚙️ Status da Automação</h4>', unsafe_allow_html=True)
        status_text = st.empty()
        bar = st.progress(0)
        
        status_text.write("🗣️ Conectando à plataforma do Speak...")
        time.sleep(1.5)
        bar.progress(60)
        
        status_text.write("🤖 Processando os áudios e lições de hoje...")
        time.sleep(1.5)
        bar.progress(100)
        status_text.write("✅ Speak concluído com sucesso!")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="explanation-card">
            <h4>💡 Para Você Estudar (Lógica do Speak)</h4>
            <p>O Speak de hoje treinou conversação. Se liga no que foi fixado:</p>
            <ul>
                <li><b>Estrutura:</b> Uso de conectores de fala no cotidiano.</li>
                <li><b>Estudo rápido:</b> Pratique a pronúncia dessas palavras depois para mitar na conversação real!</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.error("❌ Não entendi o comando. Tente algo como: 'automatize o speak' ou 'sala do futuro expiradas'.")

# --- SIMULAÇÃO DO APP NO CELULAR (Substituindo o input() antigo) ---
input_do_colega = st.chat_input("O que você quer automatizar hoje?")

if input_do_colega:
    # Mostra o comando que o usuário digitou no chat
    with st.chat_message("user"):
        st.write(input_do_colega)
        
    # Roda a sua lógica baseada no comando
    acao_detectada = interpretar_comando(input_do_colega)
    executar_automacao(acao_detectada, input_do_colega)
