# consórcio-amigo-ai

## 1. Nome do Projeto
Consórcio Amigo AI - Copiloto Financeiro e Inteligência Patrimonial

## 2. Descrição
Plataforma de consultoria e planejamento de consórcios desenvolvida em Python e Streamlit, integrada à API da Groq (modelo openai/gpt-oss-120b). A aplicação realiza análises regionais de mercado, simulações de Custo Efetivo Total (CET), ordenação estratégica de lances e projeções temporais de reajustes.

## 3. Objetivo
O objetivo da ferramenta é auxiliar usuários e consultores no planejamento patrimonial para aquisição de bens (imóveis, veículos, serviços e equipamentos). O sistema avalia a capacidade financeira, analisa a viabilidade da carta pretendida em relação à região informada, otimiza estratégias de lance (recursos próprios, FGTS e lance embutido) e compara de forma realista os custos do consórcio contra o financiamento bancário tradicional.

## Sumário
- Visão Geral
- Tecnologias Utilizadas
- Engenharia de Prompts
- Regras de Negócio e Premissas Financeiras
- Estrutura do Relatório Gerado
- Como Instalar
- Como Executar
- Como Utilizar
- Imagens ou GIF da Aplicação
- Link da Aplicação Publicada
- Configuração de Deploy (Render)
- Possíveis Melhorias Futuras
- Segurança

## Visão Geral
O ConsórcioAmigo AI processa parâmetros informados pelo usuário na interface lateral e gera um diagnóstico executivo detalhado em 7 seções, unificando métricas numéricas entre o painel visual e o relatório gerado pela inteligência artificial.

## 4. Tecnologias Utilizadas
- Linguagem: Python 3.10+
- Interface Gráfica: Streamlit
- Processamento de Linguagem Natural: API Groq (openai/gpt-oss-120b)
- Gerenciamento de Variáveis de Ambiente: python-dotenv
- Hospedagem e Deploy: Render (Web Service)

## Engenharia de Prompts
A integração com o modelo de linguagem segue padrões de prompt engineering para garantir precisão e estabilidade:
1. Alinhamento de Dados: Valores de parcela estimados e comprometimento de renda são calculados via Python e repassados ao prompt para evitar divergências nos relatórios.
2. Nomenclatura Padronizada: Uso obrigatório do termo "Carta inicial" para referir-se ao valor digitado pelo usuário.
3. Tolerância a Tokens: Configuração de max_tokens=4096 para garantir a conclusão integral de todas as seções do relatório.
4. Formatação de Saída: Respostas geradas em Markdown limpo, sem utilização de tags HTML.

## Regras de Negócio e Premissas Financeiras
Financiamento Bancário (CET Realista)
- Imóveis: CET estimado entre 12,4% e 13,8% ao ano (juros nominais de 11,0% a 12,5% a.a. + TR + seguros MIP/DFI e taxas). Prazos típicos de 300 a 360 meses.
- Veículos: CET estimado entre 25% e 35% ao ano (1,8% a 2,5% ao mês). Prazos típicos de 48 a 60 meses.

Consórcio
- Imóveis: Taxa de administração média de 14% a 17% total distribuída no contrato (180 a 200 meses).
- Veículos: Taxa de administração média de 12% a 16% total distribuída no contrato (60 a 72 meses).

Estratégia de Lances
- Média de Mercado: Contemplações por lance livre costumam exigir entre 25% e 50% do valor da carta.
- Uso do FGTS: Permitido isoladamente em imóveis, mesmo com R$ 0,00 de recursos próprios.
- Lance Embutido: Recomendado como complemento (10% a 30% da carta) quando os recursos informados forem insuficientes para a urgência desejada.
- Sem Recursos para Lance: Caso o usuário não possua recursos, o sistema omite a tabela de ranking e apresenta orientações sobre o funcionamento dos sorteios.

Alinhamento com a Urgência
- Imediata (1 a 3 meses): Requer lances competitivos/agressivos (>= 35% a 50%).
- Médio Prazo (até 1 ano): Requer lances intermediários (20% a 35%).
- Nenhuma (Sorteio/Investimento): Foco no longo prazo (60 a 200 meses) e menor custo acumulado.

## Estrutura do Relatório Gerado
O relatório final é composto por 7 seções:
1. Análise de Mercado Regional e Adequação da Carta
2. Veredito e Recomendação do Valor Ideal da Carta
3. Diagnóstico de Orçamento, Comprometimento e Alinhamento de Prazos
4. Estratégia e Análise de Lances
5. Comparativo Tático: Consórcio x Financiamento (CET Realista)
6. Simulação de Impacto de Reajustes e Custos Comparativos (Tabelas temporais e adicionais)
7. Alertas de Segurança e Boas Práticas (Medidas antifraude e verificação na ABAC/Bacen)

## 5. Como Instalar
1. Clone o repositório em sua máquina local:
   git clone https://github.com/SEU_USUARIO/consorcio-amigo-ai.git
   cd consorcio-amigo-ai

2. Crie e ative um ambiente virtual Python:
   python -m venv .venv
   source .venv/bin/activate  # No Linux/Mac
   .venv\Scripts\activate     # No Windows

3. Instale as dependências listadas no projeto:
   pip install -r requirements.txt

## 6. Como Executar
1. Crie um arquivo .env na raiz do projeto contendo sua chave de acesso da Groq:
   GROQ_API_KEY=sua_chave_groq_aqui

2. Inicie a aplicação via Streamlit:
   streamlit run app.py

3. Acesse o endereço local exibido no terminal (geralmente http://localhost:8502).

## 7. Como Utilizar
1. Na barra lateral da interface, selecione o Estado (UF) e informe a cidade de referência.
2. Escolha o tipo de bem (Imóvel, Veículo, etc.) e o padrão específico.
3. Defina o valor da carta pretendida e o nível de urgência para contemplação.
4. Informe se possui recursos próprios em dinheiro e/ou saldo de FGTS para lance.
5. Insira a renda familiar mensal e clique no botão para gerar a análise estratégica avançada.

## 8. Imagens ou GIF da Aplicação
<img width="1895" height="908" alt="image" src="https://github.com/user-attachments/assets/6175a74e-03ec-473f-a80c-011b0107de2f" />


## 9. Link da Aplicação Publicada
Acesse a aplicação em produção: https://consorcio-amigo-ai.onrender.com/

## Configuração de Deploy (Render)
- Comando de compilação: pip install -r requirements.txt
- Comando de inicialização: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
- Variáveis de Ambiente: Adicionar GROQ_API_KEY no painel de configurações do Render.

## 10. Possíveis Melhorias Futuras
- Implementação de funcionalidade para exportação do relatório executivo em formato PDF.
- Integração com dados reais de administradoras de consórcio via web scraping ou APIs de mercado.
- Inclusão de um simulador dinâmico de múltiplos lances embutidos simultâneos.
- Expansão do painel de histórico de simulações para usuários cadastrados.

## Segurança
O arquivo .gitignore está configurado para ignorar o arquivo .env, diretórios de cache (__pycache__/) e pastas temporárias, impedindo a exibição indesejada de credenciais de API no repositório.
---

## Segurança

O arquivo .gitignore está configurado para ignorar o arquivo .env, diretórios de cache (__pycache__/) e pastas temporárias, impedindo a exposição indesejada de credenciais de API no repositório.
