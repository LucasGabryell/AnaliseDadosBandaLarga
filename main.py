import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import plotly.express as px

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
opcao_grafico = st.selectbox("Escolha o Gráfico", ["Gráfico de Acessos", "Gráfico de Tipo de Transmissão"])

# Função para criar e mostrar o gráfico de Acessos
def plot_acessos():
    acessos_por_mes = dados.groupby('mes')['acessos'].sum().reset_index()
    fig = px.bar(acessos_por_mes, x='mes', y='acessos', labels={'mes': 'Mês', 'acessos': 'Acessos'})
    fig.update_layout(title='Acessos por Mês', xaxis_title='Mês', yaxis_title='Acessos')
    st.write("### Gráfico de Acessos por Mês:")
    st.plotly_chart(fig)


# Função para criar e mostrar o gráfico de Tipo de Transmissão
def plot_transmissao():
    fig = px.bar(dados, x='mes', y='transmissao', color='transmissao',
                 labels={'mes': 'Mês', 'transmissao': 'Tipo de Transmissão'},
                 title='Tipo de Transmissão de Rede ao Longo do Tempo')
    fig.update_xaxes(title='Mês')
    fig.update_yaxes(title='Contagem')
    st.write("### Gráfico de Tipo de Transmissão de Rede ao Longo do Tempo:")
    st.plotly_chart(fig)


# Mostrar o gráfico selecionado com base na escolha do usuário
if opcao_grafico == "Gráfico de Acessos":
    plot_acessos()
elif opcao_grafico == "Gráfico de Tipo de Transmissão":
    plot_transmissao()
