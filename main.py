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
opcao_grafico = st.selectbox("Escolha o Gráfico", ["Gráfico de Acessos", "Gráfico de Tipo de Transmissão/Tempo",
                                                   "Gráfico de Tipo de Transmissão/Velocidade"])


# Função para criar e mostrar o gráfico de Acessos
def plot_acessos(dados):
    # Adicione uma barra de seleção para filtrar o ano
    anos = dados['ano'].unique()
    anos = ['Todos os Anos'] + list(anos)  # Adiciona a opção "Todos os Anos"
    ano_selecionado = st.selectbox('Selecione o Ano', anos)

    # Filtrar os dados com base no ano selecionado
    if ano_selecionado == 'Todos os Anos':
        dados_filtrados = dados
        titulo = 'Acessos por Mês (Todos os Anos)'
    else:
        dados_filtrados = dados[dados['ano'] == ano_selecionado]
        titulo = f'Acessos por Mês em {ano_selecionado}'

    acessos_por_mes = dados_filtrados.groupby('mes')['acessos'].sum().reset_index()

    # Crie o gráfico de barras
    fig = px.bar(acessos_por_mes, x='mes', y='acessos', labels={'mes': 'Mês', 'acessos': 'Acessos'})
    fig.update_layout(title=titulo, xaxis_title='Mês', yaxis_title='Acessos')
    st.write("### Gráfico de Acessos por Mês:")
    st.plotly_chart(fig)


# Função para criar e mostrar o gráfico de Tipo de Transmissão
def plot_transmissao(dados):
    # Adicione uma barra de seleção para filtrar o ano
    anos = dados['ano'].unique()
    anos = ['Todos os Anos'] + list(anos)  # Adiciona a opção "Todos os Anos"
    ano_selecionado = st.selectbox('Selecione o Ano', anos)

    # Filtrar os dados com base no ano selecionado
    if ano_selecionado == 'Todos os Anos':
        dados_filtrados = dados
        titulo = 'Contagem de Tipo de Transmissão de Rede ao Longo do Tempo (Todos os Anos)'
    else:
        dados_filtrados = dados[dados['ano'] == ano_selecionado]
        titulo = f'Contagem de Tipo de Transmissão de Rede em {ano_selecionado}'

    # Agrupe os dados por mês e tipo de transmissão e conte as ocorrências
    dados_agrupados = dados_filtrados.groupby(['mes', 'transmissao']).size().reset_index(name='contagem')

    # Crie o gráfico de barras empilhadas
    fig = px.bar(dados_agrupados, x='mes', y='contagem', color='transmissao',
                 labels={'mes': 'Mês', 'contagem': 'Contagem', 'transmissao': 'Tipo de Transmissão'},
                 title=titulo)
    fig.update_xaxes(title='Mês')
    fig.update_yaxes(title='Contagem')
    st.write("### Gráfico de Tipo de Transmissão de Rede ao Longo do Tempo:")
    st.plotly_chart(fig)


# Função para criar e mostrar o gráfico de Tipo de Transmissão/Velocidade/Tecnologia
def plot_transmissao_velocidade_tecnologia(dados):
    # Adicione uma barra de seleção para filtrar o ano
    anos = dados['ano'].unique()
    anos = ['Todos os Anos'] + list(anos)  # Adiciona a opção "Todos os Anos"
    ano_selecionado = st.selectbox('Selecione o Ano', anos)

    # Adicione uma barra de seleção para filtrar a velocidade
    velocidades = dados['velocidade'].unique()
    velocidades = ['Todas as Velocidades'] + list(velocidades)  # Adiciona a opção "Todas as Velocidades"
    velocidade_selecionada = st.selectbox('Selecione a Velocidade', velocidades)

    # Filtrar os dados com base no ano e velocidade selecionados
    if ano_selecionado == 'Todos os Anos' and velocidade_selecionada == 'Todas as Velocidades':
        dados_filtrados = dados
        titulo = 'Contagem de Tipo de Transmissão de Rede ao Longo do Tempo (Todos os Anos, Todas as Velocidades)'
    elif ano_selecionado == 'Todos os Anos':
        dados_filtrados = dados[dados['velocidade'] == velocidade_selecionada]
        titulo = f'Contagem de Tipo de Transmissão de Rede por Tecnologia em Todas as Velocidades ({velocidade_selecionada})'
    elif velocidade_selecionada == 'Todas as Velocidades':
        dados_filtrados = dados[dados['ano'] == ano_selecionado]
        titulo = f'Contagem de Tipo de Transmissão de Rede por Tecnologia em {ano_selecionado} (Todas as Velocidades)'
    else:
        dados_filtrados = dados[(dados['ano'] == ano_selecionado) & (dados['velocidade'] == velocidade_selecionada)]
        titulo = f'Contagem de Tipo de Transmissão de Rede por Tecnologia em {ano_selecionado} ({velocidade_selecionada})'

    # Agrupe os dados por transmissao, tecnologia e conte as ocorrências
    dados_agrupados = dados_filtrados.groupby(['transmissao', 'tecnologia']).size().reset_index(name='contagem')

    # Crie o gráfico de barras empilhadas 2D com cores para representar a tecnologia
    fig = px.bar(dados_agrupados, x='transmissao', y='contagem', color='tecnologia',
                 labels={'transmissao': 'Tipo de Transmissão', 'contagem': 'Contagem'},
                 title=titulo)
    fig.update_xaxes(title='Tipo de Transmissão')
    fig.update_yaxes(title='Contagem')
    st.write("### Gráfico de Tipo de Transmissão de Rede por Tecnologia:")
    st.plotly_chart(fig)


# Mostrar o gráfico selecionado com base na escolha do usuário
if opcao_grafico == "Gráfico de Acessos":
    plot_acessos(dados)
elif opcao_grafico == "Gráfico de Tipo de Transmissão/Tempo":
    plot_transmissao(dados)
elif opcao_grafico == "Gráfico de Tipo de Transmissão/Velocidade":
    plot_transmissao_velocidade_tecnologia(dados)
