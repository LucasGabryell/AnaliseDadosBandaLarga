import streamlit as st
import pandas as pd
import graphicsFunctions

# Título do aplicativo
st.title("Análise de Dados de Banda Larga")

# Substitua 'seu_arquivo.csv' pelo caminho real do seu arquivo CSV
caminho_arquivo_csv = 'testeDados.csv'

# Use o método 'read_csv' do pandas para ler o arquivo CSV
dados = pd.read_csv(caminho_arquivo_csv)

# Exibir os dados no Streamlit
st.write("### Dados do arquivo CSV:")
st.write(dados)

# Barra de seleção para escolher o gráfico
opcao_grafico = st.selectbox("Escolha o Gráfico", ["Gráfico de Acessos", "Gráfico de Tipo de Transmissão/Tempo",
                                                   "Gráfico de Tipo de Transmissão/Velocidade", "Gráfico de empresas"])

# Mostrar o gráfico selecionado com base na escolha do usuário
if opcao_grafico == "Gráfico de Acessos":
    graphicsFunctions.plot_acessos(dados)
elif opcao_grafico == "Gráfico de Tipo de Transmissão/Tempo":
    graphicsFunctions.plot_transmissao(dados)
elif opcao_grafico == "Gráfico de Tipo de Transmissão/Velocidade":
    graphicsFunctions.plot_transmissao_velocidade_tecnologia(dados)
elif opcao_grafico == "Gráfico de empresas":
    graphicsFunctions.plot_empresas(dados)
