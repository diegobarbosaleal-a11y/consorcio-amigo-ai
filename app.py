import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração da página do Streamlit com layout amplo
st.set_page_config(
    page_title="ConsórcioAmigo AI | Copiloto Financeiro Avançado",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS customizada para um visual corporativo/fintech
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .stButton>button {
            width: 100%;
            background-color: #ff6b00;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.6rem;
            border: none;
        }
        .stButton>button:hover {
            background-color: #e05e00;
            color: white;
        }
        div.stMetric {
            background-color: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

# Inicialização da API da Groq
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("⚠️ Chave de API da Groq não encontrada. Verifique o seu arquivo `.env`.")
    st.stop()

client = Groq(api_key=api_key)

# Cabeçalho Moderno
col_logo, col_title = st.columns([1, 10])
with col_logo:
    st.markdown("### 🤝")
with col_title:
    st.title("ConsórcioAmigo AI — Inteligência Patrimonial")
    st.markdown("**Copiloto Avançado de Planejamento, Análise e Estratégias**")

st.markdown("---")

# Painel de Entrada de Dados (Sidebar)
st.sidebar.header("⚙️ Parâmetros e Inteligência Regional")

with st.sidebar.container():
    # Localização
    col_uf, col_cidade = st.columns([1, 2])
    with col_uf:
        estado = st.selectbox("UF", ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"], index=24) # SP por padrão
    with col_cidade:
        cidade = st.text_input("Cidade", value="", placeholder="Ex: Guarulhos, Curitiba...")

    tipo_bem = st.selectbox(
        "Qual o tipo de bem?",
        ["Imóvel (Casa/Apto/Terreno)", "Veículo (Carro/Moto)", "Reforma / Serviços", "Máquinas / Equipamentos"]
    )

    # Dicionário de sugestão automática de valores médios de carta conforme a categoria
    sugestoes_valores = {
        "Residencial Econômico / Popular": 200000,
        "Residencial Médio Padrão": 450000,
        "Residencial Alto Padrão / Luxo": 1200000,
        "Comercial / Terreno": 350000,
        "Hatch / Sedan Convencional (Popular)": 65000,
        "SUV / SUV Médio": 140000,
        "Veículo de Luxo / Alto Padrão": 300000,
        "Moto": 25000,
        "Padrão de Mercado": 50000
    }

    # Subtipo dinâmico conforme o bem
    if "Imóvel" in tipo_bem:
        subtipo_bem = st.selectbox("Padrão do Imóvel", ["Residencial Econômico / Popular", "Residencial Médio Padrão", "Residencial Alto Padrão / Luxo", "Comercial / Terreno"])
    elif "Veículo" in tipo_bem:
        subtipo_bem = st.selectbox("Categoria do Veículo", ["Hatch / Sedan Convencional (Popular)", "SUV / SUV Médio", "Veículo de Luxo / Alto Padrão", "Moto"])
    else:
        subtipo_bem = st.selectbox("Categoria", ["Padrão de Mercado"])

    # Valor sugerido automaticamente com base no subtipo selecionado
    valor_sugerido = sugestoes_valores.get(subtipo_bem, 100000)

    valor_bem = st.number_input(
        "Valor da Carta inicial pretendida (R$):",
        min_value=5000,
        max_value=5000000,
        value=valor_sugerido,
        step=5000,
        help="Sugerimos um valor padrão para esta categoria, mas você pode editar livremente."
    )

    urgencia = st.select_slider(
        "Qual a sua urgência para a contemplação?",
        options=["Nenhuma (Sorteio / Investimento)", "Médio Prazo (até 1 ano)", "Imediata (Preciso agora)"]
    )

    # Ajuste do lance: Recursos próprios e/ou FGTS
    possui_lance = st.radio("Possui recursos próprios ou FGTS para oferta de lance?", ["Sim", "Não"])

    valor_lance = 0
    valor_fgts = 0

    if possui_lance == "Sim":
        valor_lance = st.number_input(
            "Recursos próprios em dinheiro (R$):",
            min_value=0,
            max_value=int(valor_bem),
            value=0,
            step=1000,
            help="Coloque 0 se pretender utilizar apenas o FGTS."
        )
        
        if "Imóvel" in tipo_bem:
            valor_fgts = st.number_input(
                "Saldo de FGTS disponível para lance (R$):",
                min_value=0,
                max_value=1000000,
                value=20000,
                step=1000,
                help="Pode ser utilizado isoladamente ou combinado com dinheiro próprio."
            )

    renda_mensal = st.number_input(
        "Renda familiar mensal (R$):",
        min_value=1000,
        value=10000,
        step=500
    )

    pergunta_livre = st.text_input("Deseja colocar alguma diretriz ou dúvida específica? (Opcional)")

    st.markdown("---")
    gerar = st.button("🚀 Gerar Análise Estratégica Avançada")

# Área Principal
if gerar:
    cidade_final = cidade.strip() if cidade.strip() else "sua região"
    
    with st.spinner(f"🔄 A analisar o mercado em {cidade_final}/{estado}, gerando relatório completo sem cortes..."):
        
        total_lance_direto = (valor_lance + valor_fgts) if possui_lance == "Sim" else 0
        pct_lance_proprio = (valor_lance / valor_bem) * 100 if valor_bem > 0 else 0
        pct_lance_fgts = (valor_fgts / valor_bem) * 100 if valor_bem > 0 else 0
        pct_lance_total = (total_lance_direto / valor_bem) * 100 if valor_bem > 0 else 0

        tem_lance_real = possui_lance == "Sim" and total_lance_direto > 0

        # Cálculo exato unificado da parcela e comprometimento para garantir 100% de coerência
        prazo_meses = 180 if "Imóvel" in tipo_bem else 60
        taxa_admin_total = 0.15 if "Imóvel" in tipo_bem else 0.14
        parcela_estimada_exata = (valor_bem * (1 + taxa_admin_total)) / prazo_meses
        comp_renda_exato = (parcela_estimada_exata / renda_mensal) * 100

        if "Imóvel" in tipo_bem:
            taxa_financiamento_ref = "11,0% a 12,5% a.a. + TR (CET ~12,4% a 13,8% a.a.)"
            prazo_financiamento_ref = "300 a 360 meses (25 a 30 anos)"
            taxa_consorcio_ref = "Taxa de administração ~15% TOTAL em 180 meses"
            parcela_financ_inicial = valor_bem * 0.0105
            indice_reajuste_consorcio = "INCC (~4,0% a.a.)"
        else:
            taxa_financiamento_ref = "1,8% a 2,5% a.m. (CET ~25% a 35% a.a.)"
            prazo_financiamento_ref = "48 a 60 meses (4 a 5 anos)"
            taxa_consorcio_ref = "Taxa de administração ~14% TOTAL em 60 meses"
            parcela_financ_inicial = valor_bem * 0.028
            indice_reajuste_consorcio = "IPCA (~3,5% a.a.)"

        user_prompt = f"""
        Por favor, analise o perfil do usuário com base nos DADOS EXATOS DE CÁLCULO fornecidos abaixo:
        
        - **Localização:** {cidade_final} - {estado}
        - **Tipo de Bem pretendido:** {tipo_bem} (Subcategoria: {subtipo_bem})
        - **Valor da Carta inicial:** R$ {valor_bem:,.2f}
        - **Urgência para ter o bem:** {urgencia}
        - **Possui Recursos para Lance:** {'Sim' if tem_lance_real else 'Não'}
        - **Lance Próprio em Dinheiro:** R$ {valor_lance:,.2f} ({pct_lance_proprio:.1f}% da carta)
        - **Lance via FGTS:** R$ {valor_fgts:,.2f} ({pct_lance_fgts:.1f}% da carta)
        - **Soma Total do Lance Direto:** R$ {total_lance_direto:,.2f} ({pct_lance_total:.1f}% da carta)
        - **Renda familiar mensal:** R$ {renda_mensal:,.2f}
        - **DADOS EXATOS CALCULADOS:**
          * Parcela mensal estimada do consórcio inicial: **R$ {parcela_estimada_exata:,.2f}**
          * Comprometimento exato da renda (Consórcio): **{comp_renda_exato:.1f}%**
          * Parcela estimada inicial do Financiamento: **R$ {parcela_financ_inicial:,.2f}**
        - **Observação / Dúvida:** {pergunta_livre if pergunta_livre else 'Nenhuma'}
        """

        system_prompt = f"""
        Você é o ConsórcioAmigo AI, um consultor financeiro sênior e especialista em engenharia de consórcios, inteligência de mercado imobiliário/automotivo e planejamento patrimonial no Brasil.
        
        Siga ESTRITAMENTE as regras de formatação abaixo:
        - JAMAIS utilize tags HTML (como <br>, <font>, <span>, <div>). Use APENAS quebras de linha Markdown normais.
        - Utilize APENAS Markdown limpo, direto e profissional.
        - Formate valores monetários sempre no padrão brasileiro limpo (exemplo: **R$ 1.800,00** ou **R$ 300.000,00**).
        - SEMPRE refira-se ao valor inserido pelo usuário como "**Carta inicial**".
        
        **COERÊNCIA DE NÚMEROS E CONCISÃO (CRÍTICO PARA NÃO CORTAR):**
        - Utilize rigorosamente a Parcela inicial de **R$ {parcela_estimada_exata:,.2f}** e o Comprometimento de **{comp_renda_exato:.1f}%**.
        - Seja altamente objetivo nas explicações após as tabelas para garantir que TODAS AS SEÇÕES SEJAM CONCLUÍDAS.

        **ESTRUTURA DA RESPOSTA (DEVE CONTER AS 7 SEÇÕES COMPLETAS):**
        1. 📍 **Análise de Mercado Regional ({cidade_final}/{estado}) & Adequação da Carta**
        2. 🎯 **Veredito & Recomendação do Valor Ideal da Carta**
        3. 🎯 **Diagnóstico de Orçamento, Comprometimento & Alinhamento de Prazos**
        4. 🏆 **Estratégia & Análise de Lances**
        5. 📊 **Comparativo Tático: Consórcio vs. Financiamento (CET Realista)**
        6. 💡 **Simulação de Impacto de Reajustes & Custos Comparativos**:
           - Tabela 1: Evolução das parcelas (Anos 1, 3, 5, 10) comparando Consórcio vs Financiamento.
           - Tabela 2: Custos Adicionais Previstos (Taxa de Administração/Fundo Reserva vs Seguros MIP/DFI, IOF e Vistoria).
           - Resumo em 2 bullet points curtos.
        7. 🛡️ **Alertas de Segurança & Boas Práticas**: (NUNCA OMITA ESTA SEÇÃO) Liste exatamente 4 tópicos curtos e diretos sobre fraude de cota contemplada, consulta à ABAC/Bacen, custos fora de contrato e pagamentos seguros.
        """

        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                model="openai/gpt-oss-120b",
                temperature=0.3,
                max_tokens=4096
            )
            
            resposta = chat_completion.choices[0].message.content
            
            # Bloco de Métricas Executivas no topo dos resultados
            st.markdown(f"### 📊 Relatório Executivo Regional ({cidade_final} - {estado})")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric(label="Região", value=f"{estado}", delta=cidade_final)
            with col2:
                st.metric(label="Carta Inicial", value=f"R$ {valor_bem:,.0f}", delta=subtipo_bem.split()[0])
            with col3:
                st.metric(label="Comprometimento Consórcio", value=f"{comp_renda_exato:.1f}% Renda", delta="Saudável" if comp_renda_exato <= 30 else "Atenção (> 30%)")
            with col4:
                if tem_lance_real:
                    st.metric(label="Potencial de Lance", value=f"{pct_lance_total:.1f}% Carta", delta="100% FGTS" if valor_lance == 0 else f"R$ {total_lance_direto:,.0f}")
                else:
                    st.metric(label="Estratégia", value="Via Sorteio", delta=urgencia.split()[0])

            st.markdown("---")
            
            # Exibir resposta detalhada da IA
            st.markdown(resposta)

        except Exception as e:
            st.error(f"Ocorreu um erro ao comunicar com a API: {e}")
else:
    # Estado inicial de boas-vindas
    st.info("👈 Selecione o seu Estado, informe a sua Cidade, o tipo de bem e as configurações de lance no painel lateral para gerar a consultoria patrimonial inteligente.")
    
    st.markdown("### 🧠 O que a nova Inteligência Regional e Estratégia de Lances oferece:")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 📍 Carta Inicial vs. Carta Ideal")
        st.write("Valida se a sua carta inicial é suficiente para a sua região e calcula a carta ideal para o seu objetivo.")
    with c2:
        st.markdown("#### 🏆 Prazos & Composição do Lance")
        st.write("Permite usar Recursos Próprios, FGTS isoladamente ou a combinação com Lance Embutido para atingir a meta.")
    with c3:
        st.markdown("#### 📊 Comparativo CET Realista & Reajustes")
        st.write("Compara a evolução temporal das parcelas do consórcio vs. financiamento bancário, incluindo reajustes setoriais e seguros (MIP/DFI).")