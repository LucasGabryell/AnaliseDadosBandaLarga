import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

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
    acessos_por_mes = dados.groupby('mes')['acessos'].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.patch.set_facecolor('none')
    ax.bar(acessos_por_mes.index, acessos_por_mes.values, color='dodgerblue', edgecolor='white')
    plt.xlabel('Mês', color='white')
    plt.ylabel('Acessos', color='white')
    plt.title('Acessos por Mês', color='white')
    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')
    st.write("### Gráfico de Acessos por Mês:")
    st.pyplot(fig, facecolor='none')

# Função para criar e mostrar o gráfico de Tipo de Transmissão
def plot_transmissao():
    plt.figure(figsize=(10, 6))
    plt.plot(dados['mes'], dados['transmissao'], marker='o', color='green', linestyle='-', markersize=6)
    plt.xlabel('Mês', color='white')
    plt.ylabel('Tipo de Transmissão', color='white')
    plt.title('Tipo de Transmissão de Rede ao Longo do Tempo', color='white')
    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')
    plt.grid(True, linestyle='--', alpha=0.7)
    tmp_file = BytesIO()
    plt.savefig(tmp_file, format='png', bbox_inches='tight', transparent=True)
    tmp_file.seek(0)
    st.write("### Gráfico de Tipo de Transmissão de Rede ao Longo do Tempo:")
    st.image(tmp_file, use_column_width=True)

# Mostrar o gráfico selecionado com base na escolha do usuário
if opcao_grafico == "Gráfico de Acessos":
    plot_acessos()
elif opcao_grafico == "Gráfico de Tipo de Transmissão":
    plot_transmissao()
